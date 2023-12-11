from pydantic import BaseModel
from typing import Optional, List
from model.apanhado import Apanhado
import json
import numpy as np

class ApanhadoSchema(BaseModel):
    """ Define como um novo dado é inserido deve ser representado
    """
    id: int = "1"
    age: int = "31"
    gender: int = '2'
    height: int = '175'
    weight: float = '75.3'
    ap_hi: int = "120"
    ap_lo: int = "80"
    cholesterol: int = "1"
    gluc: int = "3"
    smoke: int = "1"
    alco: int = "2"
    active: int = "2"
    cardio: int = "1"
    
class ApanhadoViewSchema(BaseModel):
    """Define como um Apanhado será retornado
    """
    id: int = "1"
    age: int = "31"
    gender: int = '2'
    height: int = '175'
    weight: float = '75.3'
    ap_hi: int = "120"
    ap_lo: int = "80"
    cholesterol: int = "1"
    gluc: int = "3"
    smoke: int = "1"
    alco: int = "2"
    active: int = "2"
    cardio: int = "1"
    
class ApanhadoBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no dado do Apanhado.
    """
    id: str = "1" 

class ListaApanhadosSchema(BaseModel):
    """Define como uma lista de apanhados será Apanhadoada
    """
    apanhados: List[ApanhadoSchema]

    
class ApanhadoDelSchema(BaseModel):
    """Define como um Apanhado para deleção será representado
    """
    id: int = "1"
    
# Apresenta apenas os dados de um apanhado    
def apresenta_apanhado(apanhado: Apanhado):
    """ Retorna uma representação do Apanhado seguindo o schema definido em
        ApanhadoViewSchema.
    """
    return {
        "id": apanhado.id,
        "age": apanhado.age,
        "gender": apanhado.gender,
        "height": apanhado.height,
        "weight": apanhado.weight,
        "ap_hi": apanhado.ap_hi,
        "ap_lo": apanhado.ap_lo,
        "cholesterol": apanhado.cholesterol,
        "gluc": apanhado.gluc,
        "smoke": apanhado.smoke,
        "alco": apanhado.alco,
        "active": apanhado.active,
        "cardio": apanhado.cardio

    }
    
# Apresenta uma lista de apanhados
def apresenta_apanhados(apanhados: List[Apanhado]):
    """ Retorna uma representação do Apanhado seguindo o schema definido em
        ApanhadoViewSchema.
    """
    result = []
    for apanhado in apanhados:
        result.append({
            "id": apanhado.id,
            "age": apanhado.age,
            "gender": apanhado.gender,
            "height": apanhado.height,
            "weight": apanhado.weight,
            "ap_hi": apanhado.ap_hi,
            "ap_lo": apanhado.ap_lo,
            "cholesterol": apanhado.cholesterol,
            "gluc": apanhado.gluc,
            "smoke": apanhado.smoke,
            "alco": apanhado.alco,
            "active": apanhado.active,
            "cardio": apanhado.cardio
        })

    return {"apanhados": result}

