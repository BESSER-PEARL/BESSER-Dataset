from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Acoes_Modificaveis:

    pass
class arduino_Cabeca_Modificavel(Acoes_Modificaveis):

    def __init__(self, graus: int):
        self.graus = graus
        
    @property
    def graus(self) -> int:
        return self.__graus

    @graus.setter
    def graus(self, graus: int):
        self.__graus = graus

class arduino_Corpo_Modificavel(Acoes_Modificaveis):

    def __init__(self, tempo: int, evitarObstaculo: bool):
        self.tempo = tempo
        self.evitarObstaculo = evitarObstaculo
        
    @property
    def evitarObstaculo(self) -> bool:
        return self.__evitarObstaculo

    @evitarObstaculo.setter
    def evitarObstaculo(self, evitarObstaculo: bool):
        self.__evitarObstaculo = evitarObstaculo

    @property
    def tempo(self) -> int:
        return self.__tempo

    @tempo.setter
    def tempo(self, tempo: int):
        self.__tempo = tempo

class Condicao:

    pass
class arduino_Distancia_Infra_Vermelhos(Condicao):

    def __init__(self, distancia: int):
        self.distancia = distancia
        
    @property
    def distancia(self) -> int:
        return self.__distancia

    @distancia.setter
    def distancia(self, distancia: int):
        self.__distancia = distancia

class Unica_Cor:

    pass
class arduino_Bumper_Pressionado(Condicao):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Ligar_Azul(Unica_Cor):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class Varias_Cores:

    pass
class arduino_Ligar_Cores_Arco_Iris(Varias_Cores):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Ligar_Cores_Policia(Varias_Cores):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class Acoes_Condicionais:

    pass
class arduino_If(Acoes_Condicionais):

    def __init__(self, nome: str, arduino_If: "arduino_Acao" = None):
        self.nome = nome
        self.arduino_If = arduino_If
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def arduino_If(self):
        return self.__arduino_If

    @arduino_If.setter
    def arduino_If(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_If__arduino_If", None)
        self.__arduino_If = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Acao16"):
                opp_val = getattr(old_value, "arduino_Acao16", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Acao16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Acao16"):
                opp_val = getattr(value, "arduino_Acao16", None)
                setattr(value, "arduino_Acao16", self)

class arduino_While(Acoes_Condicionais):

    def __init__(self, nome: str, arduino_While: "arduino_Acao" = None):
        self.nome = nome
        self.arduino_While = arduino_While
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def arduino_While(self):
        return self.__arduino_While

    @arduino_While.setter
    def arduino_While(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_While__arduino_While", None)
        self.__arduino_While = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Acao14"):
                opp_val = getattr(old_value, "arduino_Acao14", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Acao14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Acao14"):
                opp_val = getattr(value, "arduino_Acao14", None)
                setattr(value, "arduino_Acao14", self)

class arduino_Desligar_Cores(Varias_Cores):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Desligar_Cor(Unica_Cor):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Ligar_Vermelho(Unica_Cor):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Ligar_Verde(Unica_Cor):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class Tricolor:

    pass
class arduino_Unica_Cor(Tricolor):

    pass
class arduino_Varias_Cores(Tricolor):

    pass
class Verde:

    pass
class arduino_Desligar_LED_Verde(Verde):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Ligar_Intermitencia(Verde):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Desligar_Intermitencia(Verde):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Ligar_LED_Verde(Verde):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class LED:

    pass
class arduino_Tricolor(LED):

    pass
class arduino_Verde(LED):

    pass
class Acoes_Predefinidas:

    pass
class arduino_Corpo(Acoes_Predefinidas):

    def __init__(self, evitarObstaculo: bool):
        self.evitarObstaculo = evitarObstaculo
        
    @property
    def evitarObstaculo(self) -> bool:
        return self.__evitarObstaculo

    @evitarObstaculo.setter
    def evitarObstaculo(self, evitarObstaculo: bool):
        self.__evitarObstaculo = evitarObstaculo

class arduino_Cabeca(Acoes_Predefinidas):

    pass
class arduino_LED(Acoes_Predefinidas):

    pass
class Corpo_Modificavel:

    pass
class arduino_Parar_Tempo(Corpo_Modificavel):

    pass
class arduino_Rodar_Esquerda_Tempo(Corpo_Modificavel):

    pass
class Cabeca:

    pass
class arduino_Virar_45_Drt(Cabeca):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Virar_45_Esq(Cabeca):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Centrar(Cabeca):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Virar_Max_Esq(Cabeca):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Virar_Max_Drt(Cabeca):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class Cabeca_Modificavel:

    pass
class arduino_Virar_para_X_Graus(Cabeca_Modificavel):

    pass
class arduino_Mover_Tras_Tempo(Corpo_Modificavel):

    pass
class arduino_Mover_Frente_Tempo(Corpo_Modificavel):

    pass
class Acao:

    pass
class arduino_Acoes_Condicionais(Acao):

    pass
class arduino_Acoes_Modificaveis(Acao):

    pass
class arduino_Fim(Acao):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Inicio(Acao):

    def __init__(self, nome: str, evitarObstaculo: bool):
        self.nome = nome
        self.evitarObstaculo = evitarObstaculo
        
    @property
    def evitarObstaculo(self) -> bool:
        return self.__evitarObstaculo

    @evitarObstaculo.setter
    def evitarObstaculo(self, evitarObstaculo: bool):
        self.__evitarObstaculo = evitarObstaculo

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Acoes_Predefinidas(Acao):

    pass
class arduino_Rodar_Direita_Tempo(Corpo_Modificavel):

    pass
class arduino_Robo:

    def __init__(self, Nome: str, arduino_Robo: set["arduino_Acao"] = None, arduino_Robo2: set["arduino_Transicoes"] = None, arduino_Robo4: set["arduino_Condicao"] = None):
        self.Nome = Nome
        self.arduino_Robo = arduino_Robo if arduino_Robo is not None else set()
        self.arduino_Robo2 = arduino_Robo2 if arduino_Robo2 is not None else set()
        self.arduino_Robo4 = arduino_Robo4 if arduino_Robo4 is not None else set()
        
    @property
    def Nome(self) -> str:
        return self.__Nome

    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def arduino_Robo4(self):
        return self.__arduino_Robo4

    @arduino_Robo4.setter
    def arduino_Robo4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Robo__arduino_Robo4", None)
        self.__arduino_Robo4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Condicao"):
                    opp_val = getattr(item, "arduino_Condicao", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Condicao", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Condicao"):
                    opp_val = getattr(item, "arduino_Condicao", None)
                    
                    setattr(item, "arduino_Condicao", self)
                    

    @property
    def arduino_Robo(self):
        return self.__arduino_Robo

    @arduino_Robo.setter
    def arduino_Robo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Robo__arduino_Robo", None)
        self.__arduino_Robo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Acao"):
                    opp_val = getattr(item, "arduino_Acao", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Acao", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Acao"):
                    opp_val = getattr(item, "arduino_Acao", None)
                    
                    setattr(item, "arduino_Acao", self)
                    

    @property
    def arduino_Robo2(self):
        return self.__arduino_Robo2

    @arduino_Robo2.setter
    def arduino_Robo2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Robo__arduino_Robo2", None)
        self.__arduino_Robo2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Transicoes"):
                    opp_val = getattr(item, "arduino_Transicoes", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Transicoes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Transicoes"):
                    opp_val = getattr(item, "arduino_Transicoes", None)
                    
                    setattr(item, "arduino_Transicoes", self)
                    

class Corpo:

    pass
class arduino_Mover_Frente(Corpo):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Parar(Corpo):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Mover_Aleatoriamente(Corpo):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Mover_Tras(Corpo):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Virar_Direita(Corpo):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Virar_Esquerda(Corpo):

    def __init__(self, nome: str):
        self.nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

class arduino_Condicao(ABC):

    pass
class arduino_Transicoes:

    pass
class arduino_Acao(ABC):

    pass