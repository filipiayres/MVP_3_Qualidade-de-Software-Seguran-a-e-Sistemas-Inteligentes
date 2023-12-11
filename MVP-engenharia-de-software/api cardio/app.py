from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Apanhado, Model
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
apanhado_tag = Tag(name="Apanhado", description="Adição, visualização, remoção e predição de dados sobre doeça renal")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de apanhados
@app.get('/apanhados', tags=[apanhado_tag],
         responses={"200": ApanhadoViewSchema, "404": ErrorSchema})
def get_apanhados():
    """Lista todos os apanhados cadastrados na base
    Retorna uma lista de apanhados cadastrados na base.
    
    Args:
        id (str): nome do apanhado
        
    Returns:
        list: lista de apanhados cadastrados na base
    """
    session = Session()
    
    # Buscando todos os apanhados
    apanhados = session.query(Apanhado).all()
    
    if not apanhados:
        logger.warning("Não há apanhados cadastrados na base :/")
        return {"message": "Não há apanhados cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d apanhados econtrados" % len(apanhados))
        return apresenta_apanhados(apanhados), 200


# Rota de adição de apanhado
@app.post('/apanhado', tags=[apanhado_tag],
          responses={"200": ApanhadoViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: ApanhadoSchema):
    """Adiciona um novo Apanhado à base de apanhados
    Retorna uma representação dos apanhados.
    
    Args:

        Id (int): Id do paciente
        age (int): Idade do paciente
        gender (str): genero
        height (int): altura
        weight(str): peso 
        ap_hi(int): pressão sistólica (mais alta)
        ap_lo (int): Pressão diastólica (mais baixa)
        gluc (int): Glicose 
        smoke (int): tabagista 
        alco (int): etilista  
        active (int): patrica atividade física  
        cardio (int): tem problema cardíaco
       
    Returns:
        dict: representação do apanhado .
    """
    
    # Carregando modelo
    ml_path = 'ml_model/cardio_lr.pkl'
    #modelo = Model.carrega_modelo(ml_path)
    
    apanhado = Apanhado(
        id=form.id,
        age=form.age,
        gender=form.gender,
        height=form.height,
        weight=form.weight,
        ap_hi=form.ap_hi,
        ap_lo=form.ap_lo,
        cholesterol=form.cholesterol,
        gluc=form.gluc,
        smoke=form.smoke,
        alco=form.alco,
        active=form.active,
        cardio=form.cardio,
        
        
    )
    logger.debug(f"Adicionando dado: '{apanhado.id}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se apanhado já existe na base
        if session.query(Apanhado).filter(Apanhado.id == form.id).first():
            error_msg = "Apanhado já existente na base :/"
            logger.warning(f"Erro ao adicionar apanhado '{apanhado.id}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando apanhado
        session.add(apanhado)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado apanhado de cardio: '{apanhado.id}'")
        return apresenta_apanhado(apanhado), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar apanhado '{apanhado.id}', {error_msg}")
        return {"message": error_msg}, 400
    

# Métodos baseados em cardio
# Rota de busca de apanhado por id
@app.get('/apanhado', tags=[apanhado_tag],
         responses={"200": ApanhadoViewSchema, "404": ErrorSchema})
def get_apanhado(query: ApanhadoBuscaSchema):    
    """Faz a busca por um apanhado cadastrado na base a partir do id

    Args:
        id (str): id do apanhado
        
    Returns:
        dict: representação do apanhado e diagnóstico associado
    """
    
    apanhado_id = query.id
    logger.debug(f"Coletando dados sobre produto #{apanhado_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    apanhado = session.query(Apanhado).filter(Apanhado.id == apanhado_id).first()
    
    if not apanhado:
        # se o apanhado não foi encontrado
        error_msg = f"apanhado {apanhado_id} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{apanhado_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"apanhado econtrado: '{apanhado.id}'")
        # retorna a representação do apanhado
        return apresenta_apanhado(apanhado), 200
   
    
# Rota de remoção de apanhado por id
@app.delete('/apanhado', tags=[apanhado_tag],
            responses={"200": ApanhadoViewSchema, "404": ErrorSchema})
def delete_apanhado(query: ApanhadoBuscaSchema):
    """Remove um apanhado cadastrado na base a partir do id

    Args:
        id (str): id do apanhado
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    apanhado_id = unquote(query.id)
    logger.debug(f"Deletando dados sobre apanhado #{apanhado_id}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando apanhado
    apanhado = session.query(Apanhado).filter(Apanhado.id == apanhado_id).first()
    
    if not apanhado:
        error_msg = "apanhado não encontrado na base :/"
        logger.warning(f"Erro ao deletar apanhado '{apanhado_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(apanhado)
        session.commit()
        logger.debug(f"Deletado apanhado #{apanhado_id}")
        return {"message": f"apanhado {apanhado_id} removido com sucesso!"}, 200