from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class myDsl_Not(Expression):

    pass
class myDsl_BoolConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class myDsl_And(Expression):

    pass
class myDsl_Comparison(Expression):

    def __init__(self, op: str, myDsl_Comparison: "myDsl_Expression" = None, myDsl_Comparison39: "myDsl_Expression" = None):
        self.op = op
        self.myDsl_Comparison = myDsl_Comparison
        self.myDsl_Comparison39 = myDsl_Comparison39
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def myDsl_Comparison(self):
        return self.__myDsl_Comparison

    @myDsl_Comparison.setter
    def myDsl_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Comparison__myDsl_Comparison", None)
        self.__myDsl_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression37"):
                opp_val = getattr(old_value, "myDsl_Expression37", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression37"):
                opp_val = getattr(value, "myDsl_Expression37", None)
                setattr(value, "myDsl_Expression37", self)

    @property
    def myDsl_Comparison39(self):
        return self.__myDsl_Comparison39

    @myDsl_Comparison39.setter
    def myDsl_Comparison39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Comparison__myDsl_Comparison39", None)
        self.__myDsl_Comparison39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression40"):
                opp_val = getattr(old_value, "myDsl_Expression40", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression40"):
                opp_val = getattr(value, "myDsl_Expression40", None)
                setattr(value, "myDsl_Expression40", self)

class myDsl_MulOrDiv(Expression):

    def __init__(self, op: str, myDsl_MulOrDiv: "myDsl_Expression" = None, myDsl_MulOrDiv54: "myDsl_Expression" = None):
        self.op = op
        self.myDsl_MulOrDiv = myDsl_MulOrDiv
        self.myDsl_MulOrDiv54 = myDsl_MulOrDiv54
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def myDsl_MulOrDiv(self):
        return self.__myDsl_MulOrDiv

    @myDsl_MulOrDiv.setter
    def myDsl_MulOrDiv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MulOrDiv__myDsl_MulOrDiv", None)
        self.__myDsl_MulOrDiv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression52"):
                opp_val = getattr(old_value, "myDsl_Expression52", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression52"):
                opp_val = getattr(value, "myDsl_Expression52", None)
                setattr(value, "myDsl_Expression52", self)

    @property
    def myDsl_MulOrDiv54(self):
        return self.__myDsl_MulOrDiv54

    @myDsl_MulOrDiv54.setter
    def myDsl_MulOrDiv54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MulOrDiv__myDsl_MulOrDiv54", None)
        self.__myDsl_MulOrDiv54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression55"):
                opp_val = getattr(old_value, "myDsl_Expression55", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression55"):
                opp_val = getattr(value, "myDsl_Expression55", None)
                setattr(value, "myDsl_Expression55", self)

class myDsl_VariableConstant(Expression):

    pass
class myDsl_Minus(Expression):

    pass
class myDsl_Equality(Expression):

    def __init__(self, op: str, myDsl_Equality: "myDsl_Expression" = None, myDsl_Equality34: "myDsl_Expression" = None):
        self.op = op
        self.myDsl_Equality = myDsl_Equality
        self.myDsl_Equality34 = myDsl_Equality34
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def myDsl_Equality(self):
        return self.__myDsl_Equality

    @myDsl_Equality.setter
    def myDsl_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Equality__myDsl_Equality", None)
        self.__myDsl_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression32"):
                opp_val = getattr(old_value, "myDsl_Expression32", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression32"):
                opp_val = getattr(value, "myDsl_Expression32", None)
                setattr(value, "myDsl_Expression32", self)

    @property
    def myDsl_Equality34(self):
        return self.__myDsl_Equality34

    @myDsl_Equality34.setter
    def myDsl_Equality34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Equality__myDsl_Equality34", None)
        self.__myDsl_Equality34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression35"):
                opp_val = getattr(old_value, "myDsl_Expression35", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression35"):
                opp_val = getattr(value, "myDsl_Expression35", None)
                setattr(value, "myDsl_Expression35", self)

class myDsl_Plus(Expression):

    pass
class myDsl_Or(Expression):

    pass
class myDsl_StringConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class myDsl_IntConstant(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class myDsl_Expression:

    pass
class myDsl_Condition:

    pass
class myDsl_Rule:

    pass
class myDsl_ArrayElement:

    pass
class ElementType:

    pass
class myDsl_ArrayType(ElementType):

    pass
class myDsl_BasicType(ElementType):

    pass
class myDsl_EntityType(ElementType):

    pass
class myDsl_ElementType:

    pass
class myDsl_ValueType:

    pass
class myDsl_Attribute:

    def __init__(self, name: str, myDsl_Attribute: "myDsl_Entity" = None, myDsl_Attribute5: "myDsl_ValueType" = None, myDsl_Attribute59: "myDsl_VariableConstant" = None):
        self.name = name
        self.myDsl_Attribute = myDsl_Attribute
        self.myDsl_Attribute5 = myDsl_Attribute5
        self.myDsl_Attribute59 = myDsl_Attribute59
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Attribute5(self):
        return self.__myDsl_Attribute5

    @myDsl_Attribute5.setter
    def myDsl_Attribute5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Attribute__myDsl_Attribute5", None)
        self.__myDsl_Attribute5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ValueType"):
                opp_val = getattr(old_value, "myDsl_ValueType", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ValueType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ValueType"):
                opp_val = getattr(value, "myDsl_ValueType", None)
                setattr(value, "myDsl_ValueType", self)

    @property
    def myDsl_Attribute(self):
        return self.__myDsl_Attribute

    @myDsl_Attribute.setter
    def myDsl_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Attribute__myDsl_Attribute", None)
        self.__myDsl_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Entity3"):
                opp_val = getattr(old_value, "myDsl_Entity3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Entity3"):
                opp_val = getattr(value, "myDsl_Entity3", None)
                if opp_val is None:
                    setattr(value, "myDsl_Entity3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Attribute59(self):
        return self.__myDsl_Attribute59

    @myDsl_Attribute59.setter
    def myDsl_Attribute59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Attribute__myDsl_Attribute59", None)
        self.__myDsl_Attribute59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_VariableConstant"):
                opp_val = getattr(old_value, "myDsl_VariableConstant", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_VariableConstant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_VariableConstant"):
                opp_val = getattr(value, "myDsl_VariableConstant", None)
                setattr(value, "myDsl_VariableConstant", self)

class myDsl_IsServer:

    def __init__(self, value: str, myDsl_IsServer: "myDsl_Entity" = None):
        self.value = value
        self.myDsl_IsServer = myDsl_IsServer
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def myDsl_IsServer(self):
        return self.__myDsl_IsServer

    @myDsl_IsServer.setter
    def myDsl_IsServer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_IsServer__myDsl_IsServer", None)
        self.__myDsl_IsServer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Entity"):
                opp_val = getattr(old_value, "myDsl_Entity", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Entity"):
                opp_val = getattr(value, "myDsl_Entity", None)
                setattr(value, "myDsl_Entity", self)

class Member:

    pass
class myDsl_Verb(Member):

    def __init__(self, verb: str, qa: str, myDsl_Verb: set["myDsl_Rule"] = None):
        self.verb = verb
        self.qa = qa
        self.myDsl_Verb = myDsl_Verb if myDsl_Verb is not None else set()
        
    @property
    def verb(self) -> str:
        return self.__verb

    @verb.setter
    def verb(self, verb: str):
        self.__verb = verb

    @property
    def qa(self) -> str:
        return self.__qa

    @qa.setter
    def qa(self, qa: str):
        self.__qa = qa

    @property
    def myDsl_Verb(self):
        return self.__myDsl_Verb

    @myDsl_Verb.setter
    def myDsl_Verb(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Verb__myDsl_Verb", None)
        self.__myDsl_Verb = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Rule"):
                    opp_val = getattr(item, "myDsl_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Rule"):
                    opp_val = getattr(item, "myDsl_Rule", None)
                    
                    setattr(item, "myDsl_Rule", self)
                    

class myDsl_Entity(Member):

    def __init__(self, name: str, myDsl_Entity: "myDsl_IsServer" = None, myDsl_Entity3: set["myDsl_Attribute"] = None, myDsl_Entity9: "myDsl_EntityType" = None):
        self.name = name
        self.myDsl_Entity = myDsl_Entity
        self.myDsl_Entity3 = myDsl_Entity3 if myDsl_Entity3 is not None else set()
        self.myDsl_Entity9 = myDsl_Entity9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Entity9(self):
        return self.__myDsl_Entity9

    @myDsl_Entity9.setter
    def myDsl_Entity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Entity__myDsl_Entity9", None)
        self.__myDsl_Entity9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_EntityType"):
                opp_val = getattr(old_value, "myDsl_EntityType", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_EntityType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_EntityType"):
                opp_val = getattr(value, "myDsl_EntityType", None)
                setattr(value, "myDsl_EntityType", self)

    @property
    def myDsl_Entity(self):
        return self.__myDsl_Entity

    @myDsl_Entity.setter
    def myDsl_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Entity__myDsl_Entity", None)
        self.__myDsl_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_IsServer"):
                opp_val = getattr(old_value, "myDsl_IsServer", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_IsServer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_IsServer"):
                opp_val = getattr(value, "myDsl_IsServer", None)
                setattr(value, "myDsl_IsServer", self)

    @property
    def myDsl_Entity3(self):
        return self.__myDsl_Entity3

    @myDsl_Entity3.setter
    def myDsl_Entity3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Entity__myDsl_Entity3", None)
        self.__myDsl_Entity3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Attribute"):
                    opp_val = getattr(item, "myDsl_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Attribute"):
                    opp_val = getattr(item, "myDsl_Attribute", None)
                    
                    setattr(item, "myDsl_Attribute", self)
                    

class BasicType:

    pass
class myDsl_BoolType(BasicType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class myDsl_StringType(BasicType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class myDsl_IntType(BasicType):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class myDsl_Member:

    pass
class myDsl_Model:

    pass