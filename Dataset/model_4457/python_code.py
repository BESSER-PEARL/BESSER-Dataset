from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EstadoSucesso(Enum):
    Sucesso = "Sucesso"
    Falha = "Falha"
    Decorrer = "Decorrer"
class EstadoDecorrer(Enum):
    Sucesso = "Sucesso"
    Falha = "Falha"
    Decorrer = "Decorrer"
class EstadoFalha(Enum):
    Falha = "Falha"
    Sucesso = "Sucesso"
    Decorrer = "Decorrer"
class TipoDistancia(Enum):
    Menor = "Menor"
    Maior = "Maior"
class EscolhaBumper(Enum):
    Esquerdo = "Esquerdo"
    Direito = "Direito"
class EstadoDaLuz(Enum):
    Ligado = "Ligado"
    Desligado = "Desligado"


############################################
# Definition of Classes
############################################

class Actuate:

    pass
class farrusco_LED(Actuate):

    def __init__(self, Nome: str, Ligado_ou_Desligado: str):
        self.Nome = Nome
        self.Ligado_ou_Desligado = Ligado_ou_Desligado
        
    @property
    def Ligado_ou_Desligado(self) -> str:
        return self.__Ligado_ou_Desligado

    @Ligado_ou_Desligado.setter
    def Ligado_ou_Desligado(self, Ligado_ou_Desligado: str):
        self.__Ligado_ou_Desligado = Ligado_ou_Desligado

    @property
    def Nome(self) -> str:
        return self.__Nome

    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

class farrusco_Servo(Actuate):

    def __init__(self, Nome: str, Posicao_Minima: int, Posicao_Maxima: int, Passo_a_Passo: int):
        self.Nome = Nome
        self.Posicao_Minima = Posicao_Minima
        self.Posicao_Maxima = Posicao_Maxima
        self.Passo_a_Passo = Passo_a_Passo
        
    @property
    def Nome(self) -> str:
        return self.__Nome

    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def Posicao_Maxima(self) -> int:
        return self.__Posicao_Maxima

    @Posicao_Maxima.setter
    def Posicao_Maxima(self, Posicao_Maxima: int):
        self.__Posicao_Maxima = Posicao_Maxima

    @property
    def Passo_a_Passo(self) -> int:
        return self.__Passo_a_Passo

    @Passo_a_Passo.setter
    def Passo_a_Passo(self, Passo_a_Passo: int):
        self.__Passo_a_Passo = Passo_a_Passo

    @property
    def Posicao_Minima(self) -> int:
        return self.__Posicao_Minima

    @Posicao_Minima.setter
    def Posicao_Minima(self, Posicao_Minima: int):
        self.__Posicao_Minima = Posicao_Minima

class farrusco_Motor(Actuate):

    def __init__(self, Nome: str, Motor_Esquerdo: int, Motor_Direito: int):
        self.Nome = Nome
        self.Motor_Esquerdo = Motor_Esquerdo
        self.Motor_Direito = Motor_Direito
        
    @property
    def Motor_Esquerdo(self) -> int:
        return self.__Motor_Esquerdo

    @Motor_Esquerdo.setter
    def Motor_Esquerdo(self, Motor_Esquerdo: int):
        self.__Motor_Esquerdo = Motor_Esquerdo

    @property
    def Motor_Direito(self) -> int:
        return self.__Motor_Direito

    @Motor_Direito.setter
    def Motor_Direito(self, Motor_Direito: int):
        self.__Motor_Direito = Motor_Direito

    @property
    def Nome(self) -> str:
        return self.__Nome

    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

class Condition:

    pass
class farrusco_Bumpers(Condition):

    def __init__(self, Nome: str, Bumper_Esquerdo_ou_Direito: str):
        self.Nome = Nome
        self.Bumper_Esquerdo_ou_Direito = Bumper_Esquerdo_ou_Direito
        
    @property
    def Nome(self) -> str:
        return self.__Nome

    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def Bumper_Esquerdo_ou_Direito(self) -> str:
        return self.__Bumper_Esquerdo_ou_Direito

    @Bumper_Esquerdo_ou_Direito.setter
    def Bumper_Esquerdo_ou_Direito(self, Bumper_Esquerdo_ou_Direito: str):
        self.__Bumper_Esquerdo_ou_Direito = Bumper_Esquerdo_ou_Direito

class farrusco_Distancia(Condition):

    def __init__(self, Nome: str, distancia: int, Menor_Maior: str):
        self.Nome = Nome
        self.distancia = distancia
        self.Menor_Maior = Menor_Maior
        
    @property
    def Menor_Maior(self) -> str:
        return self.__Menor_Maior

    @Menor_Maior.setter
    def Menor_Maior(self, Menor_Maior: str):
        self.__Menor_Maior = Menor_Maior

    @property
    def distancia(self) -> int:
        return self.__distancia

    @distancia.setter
    def distancia(self, distancia: int):
        self.__distancia = distancia

    @property
    def Nome(self) -> str:
        return self.__Nome

    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

class Action:

    pass
class farrusco_Actuate(Action):

    pass
class farrusco_Condition(Action):

    pass
class Behavior:

    pass
class farrusco_AlterarEstado(Behavior):

    def __init__(self, Nome: str, Alterar_Sucesso: str, Alterar_Falha: str, Alterar_Decorrer: str):
        self.Nome = Nome
        self.Alterar_Sucesso = Alterar_Sucesso
        self.Alterar_Falha = Alterar_Falha
        self.Alterar_Decorrer = Alterar_Decorrer
        
    @property
    def Nome(self) -> str:
        return self.__Nome

    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def Alterar_Falha(self) -> str:
        return self.__Alterar_Falha

    @Alterar_Falha.setter
    def Alterar_Falha(self, Alterar_Falha: str):
        self.__Alterar_Falha = Alterar_Falha

    @property
    def Alterar_Decorrer(self) -> str:
        return self.__Alterar_Decorrer

    @Alterar_Decorrer.setter
    def Alterar_Decorrer(self, Alterar_Decorrer: str):
        self.__Alterar_Decorrer = Alterar_Decorrer

    @property
    def Alterar_Sucesso(self) -> str:
        return self.__Alterar_Sucesso

    @Alterar_Sucesso.setter
    def Alterar_Sucesso(self, Alterar_Sucesso: str):
        self.__Alterar_Sucesso = Alterar_Sucesso

class farrusco_Sequencial(Behavior):

    def __init__(self, Nome: str):
        self.Nome = Nome
        
    @property
    def Nome(self) -> str:
        return self.__Nome

    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

class farrusco_Paralelo(Behavior):

    def __init__(self, Nome: str):
        self.Nome = Nome
        
    @property
    def Nome(self) -> str:
        return self.__Nome

    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

class farrusco_Espera(Condition):

    def __init__(self, Nome: str, Tempo: int):
        self.Nome = Nome
        self.Tempo = Tempo
        
    @property
    def Tempo(self) -> int:
        return self.__Tempo

    @Tempo.setter
    def Tempo(self, Tempo: int):
        self.__Tempo = Tempo

    @property
    def Nome(self) -> str:
        return self.__Nome

    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

class farrusco_Irmao:

    pass
class farrusco_Filho:

    pass
class farrusco_Node:

    pass
class farrusco_Robot:

    def __init__(self, Nome: str, farrusco_Robot: set["farrusco_Node"] = None, farrusco_Robot2: set["farrusco_Filho"] = None, farrusco_Robot4: set["farrusco_Irmao"] = None):
        self.Nome = Nome
        self.farrusco_Robot = farrusco_Robot if farrusco_Robot is not None else set()
        self.farrusco_Robot2 = farrusco_Robot2 if farrusco_Robot2 is not None else set()
        self.farrusco_Robot4 = farrusco_Robot4 if farrusco_Robot4 is not None else set()
        
    @property
    def Nome(self) -> str:
        return self.__Nome

    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def farrusco_Robot2(self):
        return self.__farrusco_Robot2

    @farrusco_Robot2.setter
    def farrusco_Robot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farrusco_Robot__farrusco_Robot2", None)
        self.__farrusco_Robot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "farrusco_Filho"):
                    opp_val = getattr(item, "farrusco_Filho", None)
                    
                    if opp_val == self:
                        setattr(item, "farrusco_Filho", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "farrusco_Filho"):
                    opp_val = getattr(item, "farrusco_Filho", None)
                    
                    setattr(item, "farrusco_Filho", self)
                    

    @property
    def farrusco_Robot4(self):
        return self.__farrusco_Robot4

    @farrusco_Robot4.setter
    def farrusco_Robot4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farrusco_Robot__farrusco_Robot4", None)
        self.__farrusco_Robot4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "farrusco_Irmao"):
                    opp_val = getattr(item, "farrusco_Irmao", None)
                    
                    if opp_val == self:
                        setattr(item, "farrusco_Irmao", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "farrusco_Irmao"):
                    opp_val = getattr(item, "farrusco_Irmao", None)
                    
                    setattr(item, "farrusco_Irmao", self)
                    

    @property
    def farrusco_Robot(self):
        return self.__farrusco_Robot

    @farrusco_Robot.setter
    def farrusco_Robot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farrusco_Robot__farrusco_Robot", None)
        self.__farrusco_Robot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "farrusco_Node"):
                    opp_val = getattr(item, "farrusco_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "farrusco_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "farrusco_Node"):
                    opp_val = getattr(item, "farrusco_Node", None)
                    
                    setattr(item, "farrusco_Node", self)
                    

class farrusco_Prioridade(Behavior):

    def __init__(self, Nome: str):
        self.Nome = Nome
        
    @property
    def Nome(self) -> str:
        return self.__Nome

    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

class Node:

    pass
class farrusco_Behavior(Node):

    pass
class farrusco_Action(Node):

    pass