# MVP SPRINT 3

Este pequeno projeto faz parte do material diático da Disciplina **Qualidade de Software, Segurança e Sistemas Inteligentes** 

O objetivo aqui é ilustrar o conteúdo apresentado ao longo das disciplinas.

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ python -m venv env
```
Agora será necessário acessar o ambiente virtual 

```
(env)$ source env/bin/activate
```

Instale as dependências 

```
(env)$ pip install -r requirements.txt
```

Para executar o pytest:
```
(env)$ pytest test_modelos.py 
```

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
