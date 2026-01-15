from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AnalogID(Enum):
    A0 = "A0"
    A1 = "A1"
    A2 = "A2"
    A3 = "A3"
    A4 = "A4"
    A5 = "A5"
    A6 = "A6"
class DigitalID(Enum):
    D2 = "D2"
    D4 = "D4"
    D7 = "D7"
    D8 = "D8"
    D12 = "D12"
    D13 = "D13"
class PinMode(Enum):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"
    INPUT_PULLUP = "INPUT_PULLUP"


############################################
# Definition of Classes
############################################

class ArduinoMetamodel_Transition:

    pass
class ArduinoMetamodel_State:

    def __init__(self, isInitial: bool, name: str, State: "ArduinoMetamodel_Transition" = None, State17: "ArduinoMetamodel_Transition" = None, ArduinoMetamodel_State: "ArduinoMetamodel_FiniteStateMachine" = None, target: set["ArduinoMetamodel_Transition"] = None, source: set["ArduinoMetamodel_Transition"] = None):
        self.isInitial = isInitial
        self.name = name
        self.State = State
        self.State17 = State17
        self.ArduinoMetamodel_State = ArduinoMetamodel_State
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        
    @property
    def isInitial(self) -> bool:
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State17(self):
        return self.__State17

    @State17.setter
    def State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoMetamodel_State__State17", None)
        self.__State17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoMetamodel_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoMetamodel_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition13"):
                    opp_val = getattr(item, "Transition13", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition13"):
                    opp_val = getattr(item, "Transition13", None)
                    
                    setattr(item, "Transition13", self)
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoMetamodel_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def ArduinoMetamodel_State(self):
        return self.__ArduinoMetamodel_State

    @ArduinoMetamodel_State.setter
    def ArduinoMetamodel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoMetamodel_State__ArduinoMetamodel_State", None)
        self.__ArduinoMetamodel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArduinoMetamodel_FiniteStateMachine19"):
                opp_val = getattr(old_value, "ArduinoMetamodel_FiniteStateMachine19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArduinoMetamodel_FiniteStateMachine19"):
                opp_val = getattr(value, "ArduinoMetamodel_FiniteStateMachine19", None)
                if opp_val is None:
                    setattr(value, "ArduinoMetamodel_FiniteStateMachine19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Instruccion:

    pass
class ArduinoMetamodel_delay(Instruccion):

    pass
class ArduinoMetamodel_Instruccion:

    def __init__(self, codigo: str, ArduinoMetamodel_Instruccion: "ArduinoMetamodel_Metodo" = None):
        self.codigo = codigo
        self.ArduinoMetamodel_Instruccion = ArduinoMetamodel_Instruccion
        
    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo

    @property
    def ArduinoMetamodel_Instruccion(self):
        return self.__ArduinoMetamodel_Instruccion

    @ArduinoMetamodel_Instruccion.setter
    def ArduinoMetamodel_Instruccion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoMetamodel_Instruccion__ArduinoMetamodel_Instruccion", None)
        self.__ArduinoMetamodel_Instruccion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArduinoMetamodel_Metodo10"):
                opp_val = getattr(old_value, "ArduinoMetamodel_Metodo10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArduinoMetamodel_Metodo10"):
                opp_val = getattr(value, "ArduinoMetamodel_Metodo10", None)
                if opp_val is None:
                    setattr(value, "ArduinoMetamodel_Metodo10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Analog:

    pass
class ArduinoMetamodel_PWM(Analog):

    pass
class ArduinoMetamodel_Action:

    pass
class ArduinoMetamodel_Metodo:

    def __init__(self, nombre: str, ArduinoMetamodel_Metodo: "ArduinoMetamodel_Project" = None, ArduinoMetamodel_Metodo10: set["ArduinoMetamodel_Instruccion"] = None):
        self.nombre = nombre
        self.ArduinoMetamodel_Metodo = ArduinoMetamodel_Metodo
        self.ArduinoMetamodel_Metodo10 = ArduinoMetamodel_Metodo10 if ArduinoMetamodel_Metodo10 is not None else set()
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def ArduinoMetamodel_Metodo(self):
        return self.__ArduinoMetamodel_Metodo

    @ArduinoMetamodel_Metodo.setter
    def ArduinoMetamodel_Metodo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoMetamodel_Metodo__ArduinoMetamodel_Metodo", None)
        self.__ArduinoMetamodel_Metodo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArduinoMetamodel_Project2"):
                opp_val = getattr(old_value, "ArduinoMetamodel_Project2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArduinoMetamodel_Project2"):
                opp_val = getattr(value, "ArduinoMetamodel_Project2", None)
                if opp_val is None:
                    setattr(value, "ArduinoMetamodel_Project2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ArduinoMetamodel_Metodo10(self):
        return self.__ArduinoMetamodel_Metodo10

    @ArduinoMetamodel_Metodo10.setter
    def ArduinoMetamodel_Metodo10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoMetamodel_Metodo__ArduinoMetamodel_Metodo10", None)
        self.__ArduinoMetamodel_Metodo10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArduinoMetamodel_Instruccion"):
                    opp_val = getattr(item, "ArduinoMetamodel_Instruccion", None)
                    
                    if opp_val == self:
                        setattr(item, "ArduinoMetamodel_Instruccion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArduinoMetamodel_Instruccion"):
                    opp_val = getattr(item, "ArduinoMetamodel_Instruccion", None)
                    
                    setattr(item, "ArduinoMetamodel_Instruccion", self)
                    

class ArduinoMetamodel_ArduinoBoardUNO:

    pass
class ArduinoMetamodel_Project:

    pass
class Pin:

    pass
class ArduinoMetamodel_Pin(ABC):

    def __init__(self, label: str, pinMode: str):
        self.label = label
        self.pinMode = pinMode
        
    @property
    def pinMode(self) -> str:
        return self.__pinMode

    @pinMode.setter
    def pinMode(self, pinMode: str):
        self.__pinMode = pinMode

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class ArduinoMetamodel_Analog(Pin):

    def __init__(self, ID: str, ArduinoMetamodel_Analog: "ArduinoMetamodel_ArduinoBoardUNO" = None):
        self.ID = ID
        self.ArduinoMetamodel_Analog = ArduinoMetamodel_Analog
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def ArduinoMetamodel_Analog(self):
        return self.__ArduinoMetamodel_Analog

    @ArduinoMetamodel_Analog.setter
    def ArduinoMetamodel_Analog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoMetamodel_Analog__ArduinoMetamodel_Analog", None)
        self.__ArduinoMetamodel_Analog = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArduinoMetamodel_ArduinoBoardUNO8"):
                opp_val = getattr(old_value, "ArduinoMetamodel_ArduinoBoardUNO8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArduinoMetamodel_ArduinoBoardUNO8"):
                opp_val = getattr(value, "ArduinoMetamodel_ArduinoBoardUNO8", None)
                if opp_val is None:
                    setattr(value, "ArduinoMetamodel_ArduinoBoardUNO8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ArduinoMetamodel_Digital(Pin):

    def __init__(self, ID: str, ArduinoMetamodel_Digital: "ArduinoMetamodel_ArduinoBoardUNO" = None):
        self.ID = ID
        self.ArduinoMetamodel_Digital = ArduinoMetamodel_Digital
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def ArduinoMetamodel_Digital(self):
        return self.__ArduinoMetamodel_Digital

    @ArduinoMetamodel_Digital.setter
    def ArduinoMetamodel_Digital(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoMetamodel_Digital__ArduinoMetamodel_Digital", None)
        self.__ArduinoMetamodel_Digital = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArduinoMetamodel_ArduinoBoardUNO6"):
                opp_val = getattr(old_value, "ArduinoMetamodel_ArduinoBoardUNO6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArduinoMetamodel_ArduinoBoardUNO6"):
                opp_val = getattr(value, "ArduinoMetamodel_ArduinoBoardUNO6", None)
                if opp_val is None:
                    setattr(value, "ArduinoMetamodel_ArduinoBoardUNO6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ArduinoMetamodel_FiniteStateMachine:

    pass