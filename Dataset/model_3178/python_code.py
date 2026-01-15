from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class AbstractElement:

    pass
class iot_Expression(AbstractElement):

    pass
class iot_IfStatement(AbstractElement):

    pass
class iot_AbstractElement:

    pass
class Expression:

    pass
class iot_Plus(Expression):

    pass
class iot_BoolConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class iot_Equality(Expression):

    def __init__(self, op: str, iot_Equality: "iot_Expression" = None, iot_Equality44: "iot_Expression" = None):
        self.op = op
        self.iot_Equality = iot_Equality
        self.iot_Equality44 = iot_Equality44
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def iot_Equality44(self):
        return self.__iot_Equality44

    @iot_Equality44.setter
    def iot_Equality44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Equality__iot_Equality44", None)
        self.__iot_Equality44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Expression45"):
                opp_val = getattr(old_value, "iot_Expression45", None)
                if opp_val == self:
                    setattr(old_value, "iot_Expression45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Expression45"):
                opp_val = getattr(value, "iot_Expression45", None)
                setattr(value, "iot_Expression45", self)

    @property
    def iot_Equality(self):
        return self.__iot_Equality

    @iot_Equality.setter
    def iot_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Equality__iot_Equality", None)
        self.__iot_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Expression42"):
                opp_val = getattr(old_value, "iot_Expression42", None)
                if opp_val == self:
                    setattr(old_value, "iot_Expression42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Expression42"):
                opp_val = getattr(value, "iot_Expression42", None)
                setattr(value, "iot_Expression42", self)

class iot_Not(Expression):

    pass
class iot_And(Expression):

    pass
class iot_StringConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class iot_Comparison(Expression):

    def __init__(self, op: str, iot_Comparison: "iot_Expression" = None, iot_Comparison49: "iot_Expression" = None):
        self.op = op
        self.iot_Comparison = iot_Comparison
        self.iot_Comparison49 = iot_Comparison49
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def iot_Comparison49(self):
        return self.__iot_Comparison49

    @iot_Comparison49.setter
    def iot_Comparison49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Comparison__iot_Comparison49", None)
        self.__iot_Comparison49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Expression50"):
                opp_val = getattr(old_value, "iot_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "iot_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Expression50"):
                opp_val = getattr(value, "iot_Expression50", None)
                setattr(value, "iot_Expression50", self)

    @property
    def iot_Comparison(self):
        return self.__iot_Comparison

    @iot_Comparison.setter
    def iot_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Comparison__iot_Comparison", None)
        self.__iot_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Expression47"):
                opp_val = getattr(old_value, "iot_Expression47", None)
                if opp_val == self:
                    setattr(old_value, "iot_Expression47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Expression47"):
                opp_val = getattr(value, "iot_Expression47", None)
                setattr(value, "iot_Expression47", self)

class iot_IntConstant(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class iot_VariableRef(Expression):

    pass
class iot_MulOrDiv(Expression):

    def __init__(self, op: str, iot_MulOrDiv: "iot_Expression" = None, iot_MulOrDiv64: "iot_Expression" = None):
        self.op = op
        self.iot_MulOrDiv = iot_MulOrDiv
        self.iot_MulOrDiv64 = iot_MulOrDiv64
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def iot_MulOrDiv(self):
        return self.__iot_MulOrDiv

    @iot_MulOrDiv.setter
    def iot_MulOrDiv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_MulOrDiv__iot_MulOrDiv", None)
        self.__iot_MulOrDiv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Expression62"):
                opp_val = getattr(old_value, "iot_Expression62", None)
                if opp_val == self:
                    setattr(old_value, "iot_Expression62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Expression62"):
                opp_val = getattr(value, "iot_Expression62", None)
                setattr(value, "iot_Expression62", self)

    @property
    def iot_MulOrDiv64(self):
        return self.__iot_MulOrDiv64

    @iot_MulOrDiv64.setter
    def iot_MulOrDiv64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_MulOrDiv__iot_MulOrDiv64", None)
        self.__iot_MulOrDiv64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Expression65"):
                opp_val = getattr(old_value, "iot_Expression65", None)
                if opp_val == self:
                    setattr(old_value, "iot_Expression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Expression65"):
                opp_val = getattr(value, "iot_Expression65", None)
                setattr(value, "iot_Expression65", self)

class iot_Minus(Expression):

    pass
class iot_Or(Expression):

    pass
class iot_Variable(AbstractElement):

    def __init__(self, name: str, iot_Variable: "iot_Expression" = None, iot_Variable69: "iot_VariableRef" = None):
        self.name = name
        self.iot_Variable = iot_Variable
        self.iot_Variable69 = iot_Variable69
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot_Variable(self):
        return self.__iot_Variable

    @iot_Variable.setter
    def iot_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Variable__iot_Variable", None)
        self.__iot_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Expression30"):
                opp_val = getattr(old_value, "iot_Expression30", None)
                if opp_val == self:
                    setattr(old_value, "iot_Expression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Expression30"):
                opp_val = getattr(value, "iot_Expression30", None)
                setattr(value, "iot_Expression30", self)

    @property
    def iot_Variable69(self):
        return self.__iot_Variable69

    @iot_Variable69.setter
    def iot_Variable69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Variable__iot_Variable69", None)
        self.__iot_Variable69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_VariableRef"):
                opp_val = getattr(old_value, "iot_VariableRef", None)
                if opp_val == self:
                    setattr(old_value, "iot_VariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_VariableRef"):
                opp_val = getattr(value, "iot_VariableRef", None)
                setattr(value, "iot_VariableRef", self)

class iot_IfBlock:

    pass
class iot_Dispositivo:

    def __init__(self, name: str, iot_Dispositivo3: "iot_Dispositivo" = None, iot_Dispositivo1: "iot_Dispositivo" = None, iot_Dispositivo5: set["iot_Etiqueta"] = None, iot_Dispositivo7: set["iot_Estado"] = None, iot_Dispositivo9: set["iot_Evento"] = None, iot_Dispositivo11: set["iot_Transicion"] = None, iot_Dispositivo: "iot_Model" = None):
        self.name = name
        self.iot_Dispositivo3 = iot_Dispositivo3
        self.iot_Dispositivo1 = iot_Dispositivo1
        self.iot_Dispositivo5 = iot_Dispositivo5 if iot_Dispositivo5 is not None else set()
        self.iot_Dispositivo7 = iot_Dispositivo7 if iot_Dispositivo7 is not None else set()
        self.iot_Dispositivo9 = iot_Dispositivo9 if iot_Dispositivo9 is not None else set()
        self.iot_Dispositivo11 = iot_Dispositivo11 if iot_Dispositivo11 is not None else set()
        self.iot_Dispositivo = iot_Dispositivo
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot_Dispositivo7(self):
        return self.__iot_Dispositivo7

    @iot_Dispositivo7.setter
    def iot_Dispositivo7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Dispositivo__iot_Dispositivo7", None)
        self.__iot_Dispositivo7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot_Estado"):
                    opp_val = getattr(item, "iot_Estado", None)
                    
                    if opp_val == self:
                        setattr(item, "iot_Estado", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot_Estado"):
                    opp_val = getattr(item, "iot_Estado", None)
                    
                    setattr(item, "iot_Estado", self)
                    

    @property
    def iot_Dispositivo5(self):
        return self.__iot_Dispositivo5

    @iot_Dispositivo5.setter
    def iot_Dispositivo5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Dispositivo__iot_Dispositivo5", None)
        self.__iot_Dispositivo5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot_Etiqueta"):
                    opp_val = getattr(item, "iot_Etiqueta", None)
                    
                    if opp_val == self:
                        setattr(item, "iot_Etiqueta", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot_Etiqueta"):
                    opp_val = getattr(item, "iot_Etiqueta", None)
                    
                    setattr(item, "iot_Etiqueta", self)
                    

    @property
    def iot_Dispositivo(self):
        return self.__iot_Dispositivo

    @iot_Dispositivo.setter
    def iot_Dispositivo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Dispositivo__iot_Dispositivo", None)
        self.__iot_Dispositivo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Model"):
                opp_val = getattr(old_value, "iot_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Model"):
                opp_val = getattr(value, "iot_Model", None)
                if opp_val is None:
                    setattr(value, "iot_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot_Dispositivo11(self):
        return self.__iot_Dispositivo11

    @iot_Dispositivo11.setter
    def iot_Dispositivo11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Dispositivo__iot_Dispositivo11", None)
        self.__iot_Dispositivo11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot_Transicion"):
                    opp_val = getattr(item, "iot_Transicion", None)
                    
                    if opp_val == self:
                        setattr(item, "iot_Transicion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot_Transicion"):
                    opp_val = getattr(item, "iot_Transicion", None)
                    
                    setattr(item, "iot_Transicion", self)
                    

    @property
    def iot_Dispositivo1(self):
        return self.__iot_Dispositivo1

    @iot_Dispositivo1.setter
    def iot_Dispositivo1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Dispositivo__iot_Dispositivo1", None)
        self.__iot_Dispositivo1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Dispositivo3"):
                opp_val = getattr(old_value, "iot_Dispositivo3", None)
                if opp_val == self:
                    setattr(old_value, "iot_Dispositivo3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Dispositivo3"):
                opp_val = getattr(value, "iot_Dispositivo3", None)
                setattr(value, "iot_Dispositivo3", self)

    @property
    def iot_Dispositivo9(self):
        return self.__iot_Dispositivo9

    @iot_Dispositivo9.setter
    def iot_Dispositivo9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Dispositivo__iot_Dispositivo9", None)
        self.__iot_Dispositivo9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot_Evento"):
                    opp_val = getattr(item, "iot_Evento", None)
                    
                    if opp_val == self:
                        setattr(item, "iot_Evento", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot_Evento"):
                    opp_val = getattr(item, "iot_Evento", None)
                    
                    setattr(item, "iot_Evento", self)
                    

    @property
    def iot_Dispositivo3(self):
        return self.__iot_Dispositivo3

    @iot_Dispositivo3.setter
    def iot_Dispositivo3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Dispositivo__iot_Dispositivo3", None)
        self.__iot_Dispositivo3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Dispositivo1"):
                opp_val = getattr(old_value, "iot_Dispositivo1", None)
                if opp_val == self:
                    setattr(old_value, "iot_Dispositivo1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Dispositivo1"):
                opp_val = getattr(value, "iot_Dispositivo1", None)
                setattr(value, "iot_Dispositivo1", self)

class iot_Model:

    pass
class iot_Transicion:

    pass
class iot_Evento:

    def __init__(self, typeName: str, name: str, iot_Evento: "iot_Dispositivo" = None, iot_Evento16: "iot_Transicion" = None):
        self.typeName = typeName
        self.name = name
        self.iot_Evento = iot_Evento
        self.iot_Evento16 = iot_Evento16
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot_Evento(self):
        return self.__iot_Evento

    @iot_Evento.setter
    def iot_Evento(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Evento__iot_Evento", None)
        self.__iot_Evento = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Dispositivo9"):
                opp_val = getattr(old_value, "iot_Dispositivo9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Dispositivo9"):
                opp_val = getattr(value, "iot_Dispositivo9", None)
                if opp_val is None:
                    setattr(value, "iot_Dispositivo9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot_Evento16(self):
        return self.__iot_Evento16

    @iot_Evento16.setter
    def iot_Evento16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Evento__iot_Evento16", None)
        self.__iot_Evento16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Transicion15"):
                opp_val = getattr(old_value, "iot_Transicion15", None)
                if opp_val == self:
                    setattr(old_value, "iot_Transicion15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Transicion15"):
                opp_val = getattr(value, "iot_Transicion15", None)
                setattr(value, "iot_Transicion15", self)

class iot_Estado:

    def __init__(self, name: str, iot_Estado: "iot_Dispositivo" = None, iot_Estado13: set["iot_AbstractElement"] = None, iot_Estado19: "iot_Transicion" = None):
        self.name = name
        self.iot_Estado = iot_Estado
        self.iot_Estado13 = iot_Estado13 if iot_Estado13 is not None else set()
        self.iot_Estado19 = iot_Estado19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot_Estado19(self):
        return self.__iot_Estado19

    @iot_Estado19.setter
    def iot_Estado19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Estado__iot_Estado19", None)
        self.__iot_Estado19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Transicion18"):
                opp_val = getattr(old_value, "iot_Transicion18", None)
                if opp_val == self:
                    setattr(old_value, "iot_Transicion18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Transicion18"):
                opp_val = getattr(value, "iot_Transicion18", None)
                setattr(value, "iot_Transicion18", self)

    @property
    def iot_Estado(self):
        return self.__iot_Estado

    @iot_Estado.setter
    def iot_Estado(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Estado__iot_Estado", None)
        self.__iot_Estado = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Dispositivo7"):
                opp_val = getattr(old_value, "iot_Dispositivo7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Dispositivo7"):
                opp_val = getattr(value, "iot_Dispositivo7", None)
                if opp_val is None:
                    setattr(value, "iot_Dispositivo7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot_Estado13(self):
        return self.__iot_Estado13

    @iot_Estado13.setter
    def iot_Estado13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Estado__iot_Estado13", None)
        self.__iot_Estado13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot_AbstractElement"):
                    opp_val = getattr(item, "iot_AbstractElement", None)
                    
                    if opp_val == self:
                        setattr(item, "iot_AbstractElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot_AbstractElement"):
                    opp_val = getattr(item, "iot_AbstractElement", None)
                    
                    setattr(item, "iot_AbstractElement", self)
                    

class iot_Etiqueta:

    def __init__(self, typeName: str, name: str, value: str, iot_Etiqueta: "iot_Dispositivo" = None):
        self.typeName = typeName
        self.name = name
        self.value = value
        self.iot_Etiqueta = iot_Etiqueta
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def iot_Etiqueta(self):
        return self.__iot_Etiqueta

    @iot_Etiqueta.setter
    def iot_Etiqueta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Etiqueta__iot_Etiqueta", None)
        self.__iot_Etiqueta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Dispositivo5"):
                opp_val = getattr(old_value, "iot_Dispositivo5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Dispositivo5"):
                opp_val = getattr(value, "iot_Dispositivo5", None)
                if opp_val is None:
                    setattr(value, "iot_Dispositivo5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
