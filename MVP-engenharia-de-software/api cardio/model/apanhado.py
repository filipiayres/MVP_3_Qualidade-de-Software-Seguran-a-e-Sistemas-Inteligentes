from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = age,gender,height,weight,ap_hi,ap_lo,
# cholesterol,gluc,smoke,alco,active,cardio,data_insercao

class Apanhado(Base):
    __tablename__ = 'apanhados'
    
    id = Column(Integer, autoincrement=int, primary_key=True)
    age = Column(Integer)
    gender= Column("gender", String(50))
    height = Column("height", String(50))
    weight = Column("weight", String(50))
    ap_hi = Column("ap_hi", Integer)
    ap_lo = Column("ap_lo", Integer)
    cholesterol = Column("cholesterol", Integer)
    gluc = Column("gluc", Integer)
    smoke = Column("smoke", Integer)
    alco = Column("alco", Integer)
    active = Column("active", Integer)
    cardio = Column("cardio", Integer)
    
    
    def __init__(self, id:int, 
                 age:int, 
                 gender:int, 
                 height:int,
                 weight:float, 
                 ap_hi:int, 
                 ap_lo:int, 
                 cholesterol:float, 
                 gluc:int,
                 smoke:int,
                 alco:int,
                 active:int,
                 cardio:int):
    

        """
        Cria um Apanhado
        Arguments:
            id: id 
            age: idade
            gender: Genero
            height: Altura
            weight: peso 
            ap_hi: Pressão sistólica 
            ap_lo:Pressão diastólica
            cholesterol: Colesterol
            gluc: glicose
            smoke: tabagista
            alco: Etilista
            active: Pratica de atividades físicas
            cardio: É ou nao hipertenso
        """
        self.id=id
        self.age=age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.ap_lo = ap_lo
        self.ap_hi = ap_hi
        self.cholesterol = cholesterol
        self.gluc = gluc
        self.smoke = smoke
        self.alco = alco
        self.active = active
        self.cardio = cardio

        