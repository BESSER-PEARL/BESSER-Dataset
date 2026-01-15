from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class operandos(Enum):
    menor = "menor"
    mayor = "mayor"
    menorigual = "menorigual"
    mayorigual = "mayorigual"
    igual = "igual"
    diferente = "diferente"


############################################
# Definition of Classes
############################################

class Bloques:

    pass
class arduino_While(Bloques):

    def __init__(self, operando: str, referencia: str, valor: str):
        self.operando = operando
        self.referencia = referencia
        self.valor = valor
        
    @property
    def operando(self) -> str:
        return self.__operando

    @operando.setter
    def operando(self, operando: str):
        self.__operando = operando

    @property
    def valor(self) -> str:
        return self.__valor

    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

    @property
    def referencia(self) -> str:
        return self.__referencia

    @referencia.setter
    def referencia(self, referencia: str):
        self.__referencia = referencia

class arduino_If(Bloques):

    def __init__(self, operando: str, referencia: str, valor: str):
        self.operando = operando
        self.referencia = referencia
        self.valor = valor
        
    @property
    def operando(self) -> str:
        return self.__operando

    @operando.setter
    def operando(self, operando: str):
        self.__operando = operando

    @property
    def referencia(self) -> str:
        return self.__referencia

    @referencia.setter
    def referencia(self, referencia: str):
        self.__referencia = referencia

    @property
    def valor(self) -> str:
        return self.__valor

    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

class arduino_Bloques(ABC):

    pass
class arduino_Instrucciones(ABC):

    pass
class arduino_Actuadores(ABC):

    def __init__(self, pin: str, arduino_Actuadores: "arduino_Sketch" = None, arduino_Actuadores8: "arduino_Instrucciones" = None, arduino_Actuadores12: "arduino_Sensores" = None, arduino_Actuadores29: "arduino_Bloques" = None, arduino_Actuadores38: "arduino_Bloques" = None):
        self.pin = pin
        self.arduino_Actuadores = arduino_Actuadores
        self.arduino_Actuadores8 = arduino_Actuadores8
        self.arduino_Actuadores12 = arduino_Actuadores12
        self.arduino_Actuadores29 = arduino_Actuadores29
        self.arduino_Actuadores38 = arduino_Actuadores38
        
    @property
    def pin(self) -> str:
        return self.__pin

    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def arduino_Actuadores29(self):
        return self.__arduino_Actuadores29

    @arduino_Actuadores29.setter
    def arduino_Actuadores29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Actuadores__arduino_Actuadores29", None)
        self.__arduino_Actuadores29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Bloques28"):
                opp_val = getattr(old_value, "arduino_Bloques28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Bloques28"):
                opp_val = getattr(value, "arduino_Bloques28", None)
                if opp_val is None:
                    setattr(value, "arduino_Bloques28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_Actuadores38(self):
        return self.__arduino_Actuadores38

    @arduino_Actuadores38.setter
    def arduino_Actuadores38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Actuadores__arduino_Actuadores38", None)
        self.__arduino_Actuadores38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Bloques37"):
                opp_val = getattr(old_value, "arduino_Bloques37", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Bloques37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Bloques37"):
                opp_val = getattr(value, "arduino_Bloques37", None)
                setattr(value, "arduino_Bloques37", self)

    @property
    def arduino_Actuadores8(self):
        return self.__arduino_Actuadores8

    @arduino_Actuadores8.setter
    def arduino_Actuadores8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Actuadores__arduino_Actuadores8", None)
        self.__arduino_Actuadores8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Instrucciones9"):
                opp_val = getattr(old_value, "arduino_Instrucciones9", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Instrucciones9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Instrucciones9"):
                opp_val = getattr(value, "arduino_Instrucciones9", None)
                setattr(value, "arduino_Instrucciones9", self)

    @property
    def arduino_Actuadores12(self):
        return self.__arduino_Actuadores12

    @arduino_Actuadores12.setter
    def arduino_Actuadores12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Actuadores__arduino_Actuadores12", None)
        self.__arduino_Actuadores12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sensores11"):
                opp_val = getattr(old_value, "arduino_Sensores11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sensores11"):
                opp_val = getattr(value, "arduino_Sensores11", None)
                if opp_val is None:
                    setattr(value, "arduino_Sensores11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_Actuadores(self):
        return self.__arduino_Actuadores

    @arduino_Actuadores.setter
    def arduino_Actuadores(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Actuadores__arduino_Actuadores", None)
        self.__arduino_Actuadores = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sketch2"):
                opp_val = getattr(old_value, "arduino_Sketch2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sketch2"):
                opp_val = getattr(value, "arduino_Sketch2", None)
                if opp_val is None:
                    setattr(value, "arduino_Sketch2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduino_Sensores(ABC):

    def __init__(self, pin: str, med: str, arduino_Sensores: "arduino_Sketch" = None, arduino_Sensores11: set["arduino_Actuadores"] = None, arduino_Sensores15: "arduino_Variar" = None, arduino_Sensores35: "arduino_Bloques" = None):
        self.pin = pin
        self.med = med
        self.arduino_Sensores = arduino_Sensores
        self.arduino_Sensores11 = arduino_Sensores11 if arduino_Sensores11 is not None else set()
        self.arduino_Sensores15 = arduino_Sensores15
        self.arduino_Sensores35 = arduino_Sensores35
        
    @property
    def pin(self) -> str:
        return self.__pin

    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def med(self) -> str:
        return self.__med

    @med.setter
    def med(self, med: str):
        self.__med = med

    @property
    def arduino_Sensores35(self):
        return self.__arduino_Sensores35

    @arduino_Sensores35.setter
    def arduino_Sensores35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sensores__arduino_Sensores35", None)
        self.__arduino_Sensores35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Bloques34"):
                opp_val = getattr(old_value, "arduino_Bloques34", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Bloques34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Bloques34"):
                opp_val = getattr(value, "arduino_Bloques34", None)
                setattr(value, "arduino_Bloques34", self)

    @property
    def arduino_Sensores11(self):
        return self.__arduino_Sensores11

    @arduino_Sensores11.setter
    def arduino_Sensores11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sensores__arduino_Sensores11", None)
        self.__arduino_Sensores11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Actuadores12"):
                    opp_val = getattr(item, "arduino_Actuadores12", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Actuadores12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Actuadores12"):
                    opp_val = getattr(item, "arduino_Actuadores12", None)
                    
                    setattr(item, "arduino_Actuadores12", self)
                    

    @property
    def arduino_Sensores(self):
        return self.__arduino_Sensores

    @arduino_Sensores.setter
    def arduino_Sensores(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sensores__arduino_Sensores", None)
        self.__arduino_Sensores = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sketch"):
                opp_val = getattr(old_value, "arduino_Sketch", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sketch"):
                opp_val = getattr(value, "arduino_Sketch", None)
                if opp_val is None:
                    setattr(value, "arduino_Sketch", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_Sensores15(self):
        return self.__arduino_Sensores15

    @arduino_Sensores15.setter
    def arduino_Sensores15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sensores__arduino_Sensores15", None)
        self.__arduino_Sensores15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Variar"):
                opp_val = getattr(old_value, "arduino_Variar", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Variar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Variar"):
                opp_val = getattr(value, "arduino_Variar", None)
                setattr(value, "arduino_Variar", self)

class arduino_Sketch:

    def __init__(self, Nombre: str, arduino_Sketch: set["arduino_Sensores"] = None, arduino_Sketch2: set["arduino_Actuadores"] = None, arduino_Sketch4: set["arduino_Instrucciones"] = None, arduino_Sketch6: set["arduino_Bloques"] = None):
        self.Nombre = Nombre
        self.arduino_Sketch = arduino_Sketch if arduino_Sketch is not None else set()
        self.arduino_Sketch2 = arduino_Sketch2 if arduino_Sketch2 is not None else set()
        self.arduino_Sketch4 = arduino_Sketch4 if arduino_Sketch4 is not None else set()
        self.arduino_Sketch6 = arduino_Sketch6 if arduino_Sketch6 is not None else set()
        
    @property
    def Nombre(self) -> str:
        return self.__Nombre

    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def arduino_Sketch6(self):
        return self.__arduino_Sketch6

    @arduino_Sketch6.setter
    def arduino_Sketch6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch6", None)
        self.__arduino_Sketch6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Bloques"):
                    opp_val = getattr(item, "arduino_Bloques", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Bloques", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Bloques"):
                    opp_val = getattr(item, "arduino_Bloques", None)
                    
                    setattr(item, "arduino_Bloques", self)
                    

    @property
    def arduino_Sketch4(self):
        return self.__arduino_Sketch4

    @arduino_Sketch4.setter
    def arduino_Sketch4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch4", None)
        self.__arduino_Sketch4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Instrucciones"):
                    opp_val = getattr(item, "arduino_Instrucciones", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Instrucciones", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Instrucciones"):
                    opp_val = getattr(item, "arduino_Instrucciones", None)
                    
                    setattr(item, "arduino_Instrucciones", self)
                    

    @property
    def arduino_Sketch2(self):
        return self.__arduino_Sketch2

    @arduino_Sketch2.setter
    def arduino_Sketch2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch2", None)
        self.__arduino_Sketch2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Actuadores"):
                    opp_val = getattr(item, "arduino_Actuadores", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Actuadores", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Actuadores"):
                    opp_val = getattr(item, "arduino_Actuadores", None)
                    
                    setattr(item, "arduino_Actuadores", self)
                    

    @property
    def arduino_Sketch(self):
        return self.__arduino_Sketch

    @arduino_Sketch.setter
    def arduino_Sketch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch", None)
        self.__arduino_Sketch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Sensores"):
                    opp_val = getattr(item, "arduino_Sensores", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Sensores", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Sensores"):
                    opp_val = getattr(item, "arduino_Sensores", None)
                    
                    setattr(item, "arduino_Sensores", self)
                    

class Instrucciones:

    pass
class arduino_Esperar(Instrucciones):

    def __init__(self, miliseg: str, arduino_Esperar: "arduino_Apagar" = None, arduino_Esperar17: "arduino_Apagar" = None, arduino_Esperar20: "arduino_Encender" = None, arduino_Esperar23: "arduino_Encender" = None):
        self.miliseg = miliseg
        self.arduino_Esperar = arduino_Esperar
        self.arduino_Esperar17 = arduino_Esperar17
        self.arduino_Esperar20 = arduino_Esperar20
        self.arduino_Esperar23 = arduino_Esperar23
        
    @property
    def miliseg(self) -> str:
        return self.__miliseg

    @miliseg.setter
    def miliseg(self, miliseg: str):
        self.__miliseg = miliseg

    @property
    def arduino_Esperar20(self):
        return self.__arduino_Esperar20

    @arduino_Esperar20.setter
    def arduino_Esperar20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Esperar__arduino_Esperar20", None)
        self.__arduino_Esperar20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Encender"):
                opp_val = getattr(old_value, "arduino_Encender", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Encender", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Encender"):
                opp_val = getattr(value, "arduino_Encender", None)
                setattr(value, "arduino_Encender", self)

    @property
    def arduino_Esperar23(self):
        return self.__arduino_Esperar23

    @arduino_Esperar23.setter
    def arduino_Esperar23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Esperar__arduino_Esperar23", None)
        self.__arduino_Esperar23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Encender22"):
                opp_val = getattr(old_value, "arduino_Encender22", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Encender22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Encender22"):
                opp_val = getattr(value, "arduino_Encender22", None)
                setattr(value, "arduino_Encender22", self)

    @property
    def arduino_Esperar(self):
        return self.__arduino_Esperar

    @arduino_Esperar.setter
    def arduino_Esperar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Esperar__arduino_Esperar", None)
        self.__arduino_Esperar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Apagar"):
                opp_val = getattr(old_value, "arduino_Apagar", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Apagar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Apagar"):
                opp_val = getattr(value, "arduino_Apagar", None)
                setattr(value, "arduino_Apagar", self)

    @property
    def arduino_Esperar17(self):
        return self.__arduino_Esperar17

    @arduino_Esperar17.setter
    def arduino_Esperar17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Esperar__arduino_Esperar17", None)
        self.__arduino_Esperar17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Apagar18"):
                opp_val = getattr(old_value, "arduino_Apagar18", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Apagar18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Apagar18"):
                opp_val = getattr(value, "arduino_Apagar18", None)
                setattr(value, "arduino_Apagar18", self)

class arduino_Variar(Instrucciones):

    def __init__(self, pwm: str, arduino_Variar: "arduino_Sensores" = None):
        self.pwm = pwm
        self.arduino_Variar = arduino_Variar
        
    @property
    def pwm(self) -> str:
        return self.__pwm

    @pwm.setter
    def pwm(self, pwm: str):
        self.__pwm = pwm

    @property
    def arduino_Variar(self):
        return self.__arduino_Variar

    @arduino_Variar.setter
    def arduino_Variar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Variar__arduino_Variar", None)
        self.__arduino_Variar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sensores15"):
                opp_val = getattr(old_value, "arduino_Sensores15", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Sensores15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sensores15"):
                opp_val = getattr(value, "arduino_Sensores15", None)
                setattr(value, "arduino_Sensores15", self)

class arduino_Encender(Instrucciones):

    pass
class arduino_Apagar(Instrucciones):

    pass
class Sensores:

    pass
class arduino_Boton(Sensores):

    pass
class arduino_Potenciometro(Sensores):

    pass
class arduino_PIR(Sensores):

    pass
class arduino_Temperatura(Sensores):

    def __init__(self, temperatura: str):
        self.temperatura = temperatura
        
    @property
    def temperatura(self) -> str:
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura: str):
        self.__temperatura = temperatura

class arduino_LDR(Sensores):

    pass
class Actuadores:

    pass
class arduino_Buzzer(Actuadores):

    pass
class arduino_Servo(Actuadores):

    def __init__(self, angulo: str, libreria: str):
        self.angulo = angulo
        self.libreria = libreria
        
    @property
    def angulo(self) -> str:
        return self.__angulo

    @angulo.setter
    def angulo(self, angulo: str):
        self.__angulo = angulo

    @property
    def libreria(self) -> str:
        return self.__libreria

    @libreria.setter
    def libreria(self, libreria: str):
        self.__libreria = libreria

class arduino_Led(Actuadores):

    pass