from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class rell_Minus(Expression):

    pass
class rell_BoolConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class rell_Not(Expression):

    pass
class rell_Plus(Expression):

    pass
class rell_StringConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class rell_Comparison(Expression):

    def __init__(self, op: str, rell_Comparison: "rell_Expression" = None, rell_Comparison73: "rell_Expression" = None):
        self.op = op
        self.rell_Comparison = rell_Comparison
        self.rell_Comparison73 = rell_Comparison73
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def rell_Comparison(self):
        return self.__rell_Comparison

    @rell_Comparison.setter
    def rell_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_Comparison__rell_Comparison", None)
        self.__rell_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Expression71"):
                opp_val = getattr(old_value, "rell_Expression71", None)
                if opp_val == self:
                    setattr(old_value, "rell_Expression71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Expression71"):
                opp_val = getattr(value, "rell_Expression71", None)
                setattr(value, "rell_Expression71", self)

    @property
    def rell_Comparison73(self):
        return self.__rell_Comparison73

    @rell_Comparison73.setter
    def rell_Comparison73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_Comparison__rell_Comparison73", None)
        self.__rell_Comparison73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Expression74"):
                opp_val = getattr(old_value, "rell_Expression74", None)
                if opp_val == self:
                    setattr(old_value, "rell_Expression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Expression74"):
                opp_val = getattr(value, "rell_Expression74", None)
                setattr(value, "rell_Expression74", self)

class rell_MulOrDiv(Expression):

    def __init__(self, op: str, rell_MulOrDiv: "rell_Expression" = None, rell_MulOrDiv90: "rell_Expression" = None):
        self.op = op
        self.rell_MulOrDiv = rell_MulOrDiv
        self.rell_MulOrDiv90 = rell_MulOrDiv90
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def rell_MulOrDiv(self):
        return self.__rell_MulOrDiv

    @rell_MulOrDiv.setter
    def rell_MulOrDiv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_MulOrDiv__rell_MulOrDiv", None)
        self.__rell_MulOrDiv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Expression88"):
                opp_val = getattr(old_value, "rell_Expression88", None)
                if opp_val == self:
                    setattr(old_value, "rell_Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Expression88"):
                opp_val = getattr(value, "rell_Expression88", None)
                setattr(value, "rell_Expression88", self)

    @property
    def rell_MulOrDiv90(self):
        return self.__rell_MulOrDiv90

    @rell_MulOrDiv90.setter
    def rell_MulOrDiv90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_MulOrDiv__rell_MulOrDiv90", None)
        self.__rell_MulOrDiv90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Expression91"):
                opp_val = getattr(old_value, "rell_Expression91", None)
                if opp_val == self:
                    setattr(old_value, "rell_Expression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Expression91"):
                opp_val = getattr(value, "rell_Expression91", None)
                setattr(value, "rell_Expression91", self)

class rell_IntConstant(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class rell_VariableRef(Expression):

    pass
class rell_Or(Expression):

    pass
class rell_Equality(Expression):

    def __init__(self, op: str, rell_Equality: "rell_Expression" = None, rell_Equality68: "rell_Expression" = None):
        self.op = op
        self.rell_Equality = rell_Equality
        self.rell_Equality68 = rell_Equality68
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def rell_Equality68(self):
        return self.__rell_Equality68

    @rell_Equality68.setter
    def rell_Equality68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_Equality__rell_Equality68", None)
        self.__rell_Equality68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Expression69"):
                opp_val = getattr(old_value, "rell_Expression69", None)
                if opp_val == self:
                    setattr(old_value, "rell_Expression69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Expression69"):
                opp_val = getattr(value, "rell_Expression69", None)
                setattr(value, "rell_Expression69", self)

    @property
    def rell_Equality(self):
        return self.__rell_Equality

    @rell_Equality.setter
    def rell_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_Equality__rell_Equality", None)
        self.__rell_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Expression66"):
                opp_val = getattr(old_value, "rell_Expression66", None)
                if opp_val == self:
                    setattr(old_value, "rell_Expression66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Expression66"):
                opp_val = getattr(value, "rell_Expression66", None)
                setattr(value, "rell_Expression66", self)

class rell_And(Expression):

    pass
class rell_ClassType:

    pass
class rell_PrimitiveType:

    def __init__(self, primitiveType: str, rell_PrimitiveType: "rell_TypeReference" = None):
        self.primitiveType = primitiveType
        self.rell_PrimitiveType = rell_PrimitiveType
        
    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

    @property
    def rell_PrimitiveType(self):
        return self.__rell_PrimitiveType

    @rell_PrimitiveType.setter
    def rell_PrimitiveType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_PrimitiveType__rell_PrimitiveType", None)
        self.__rell_PrimitiveType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_TypeReference49"):
                opp_val = getattr(old_value, "rell_TypeReference49", None)
                if opp_val == self:
                    setattr(old_value, "rell_TypeReference49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_TypeReference49"):
                opp_val = getattr(value, "rell_TypeReference49", None)
                setattr(value, "rell_TypeReference49", self)

class rell_TypeReference:

    pass
class rell_ConditionElement:

    def __init__(self, compareName: str, rell_ConditionElement26: "rell_Expression" = None, rell_ConditionElement: "rell_Conditions" = None):
        self.compareName = compareName
        self.rell_ConditionElement26 = rell_ConditionElement26
        self.rell_ConditionElement = rell_ConditionElement
        
    @property
    def compareName(self) -> str:
        return self.__compareName

    @compareName.setter
    def compareName(self, compareName: str):
        self.__compareName = compareName

    @property
    def rell_ConditionElement(self):
        return self.__rell_ConditionElement

    @rell_ConditionElement.setter
    def rell_ConditionElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_ConditionElement__rell_ConditionElement", None)
        self.__rell_ConditionElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Conditions24"):
                opp_val = getattr(old_value, "rell_Conditions24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Conditions24"):
                opp_val = getattr(value, "rell_Conditions24", None)
                if opp_val is None:
                    setattr(value, "rell_Conditions24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rell_ConditionElement26(self):
        return self.__rell_ConditionElement26

    @rell_ConditionElement26.setter
    def rell_ConditionElement26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_ConditionElement__rell_ConditionElement26", None)
        self.__rell_ConditionElement26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Expression27"):
                opp_val = getattr(old_value, "rell_Expression27", None)
                if opp_val == self:
                    setattr(old_value, "rell_Expression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Expression27"):
                opp_val = getattr(value, "rell_Expression27", None)
                setattr(value, "rell_Expression27", self)

class Statement:

    pass
class rell_Variable(Statement):

    pass
class rell_Statement:

    pass
class rell_VariableInit(Statement):

    pass
class Relational:

    pass
class rell_Delete(Relational):

    pass
class rell_Create(Relational):

    pass
class rell_Update(Relational):

    pass
class rell_Conditions:

    pass
class rell_Relational(Statement):

    def __init__(self, entity: str, rell_Relational: "rell_Relational" = None, rell_Relational18: "rell_Relational" = None, rell_Relational21: "rell_Conditions" = None):
        self.entity = entity
        self.rell_Relational = rell_Relational
        self.rell_Relational18 = rell_Relational18
        self.rell_Relational21 = rell_Relational21
        
    @property
    def entity(self) -> str:
        return self.__entity

    @entity.setter
    def entity(self, entity: str):
        self.__entity = entity

    @property
    def rell_Relational(self):
        return self.__rell_Relational

    @rell_Relational.setter
    def rell_Relational(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_Relational__rell_Relational", None)
        self.__rell_Relational = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Relational18"):
                opp_val = getattr(old_value, "rell_Relational18", None)
                if opp_val == self:
                    setattr(old_value, "rell_Relational18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Relational18"):
                opp_val = getattr(value, "rell_Relational18", None)
                setattr(value, "rell_Relational18", self)

    @property
    def rell_Relational18(self):
        return self.__rell_Relational18

    @rell_Relational18.setter
    def rell_Relational18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_Relational__rell_Relational18", None)
        self.__rell_Relational18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Relational"):
                opp_val = getattr(old_value, "rell_Relational", None)
                if opp_val == self:
                    setattr(old_value, "rell_Relational", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Relational"):
                opp_val = getattr(value, "rell_Relational", None)
                setattr(value, "rell_Relational", self)

    @property
    def rell_Relational21(self):
        return self.__rell_Relational21

    @rell_Relational21.setter
    def rell_Relational21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_Relational__rell_Relational21", None)
        self.__rell_Relational21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Conditions"):
                opp_val = getattr(old_value, "rell_Conditions", None)
                if opp_val == self:
                    setattr(old_value, "rell_Conditions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Conditions"):
                opp_val = getattr(value, "rell_Conditions", None)
                setattr(value, "rell_Conditions", self)

class rell_Expression:

    pass
class rell_VariableDeclaration:

    def __init__(self, name: str, rell_VariableDeclaration: "rell_Variable" = None, rell_VariableDeclaration33: "rell_VariableInit" = None, rell_VariableDeclaration42: "rell_RelAttrubutesList" = None, rell_VariableDeclaration47: "rell_TypeReference" = None, rell_VariableDeclaration45: "rell_Attribute" = None, rell_VariableDeclaration86: "rell_VariableRef" = None):
        self.name = name
        self.rell_VariableDeclaration = rell_VariableDeclaration
        self.rell_VariableDeclaration33 = rell_VariableDeclaration33
        self.rell_VariableDeclaration42 = rell_VariableDeclaration42
        self.rell_VariableDeclaration47 = rell_VariableDeclaration47
        self.rell_VariableDeclaration45 = rell_VariableDeclaration45
        self.rell_VariableDeclaration86 = rell_VariableDeclaration86
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rell_VariableDeclaration42(self):
        return self.__rell_VariableDeclaration42

    @rell_VariableDeclaration42.setter
    def rell_VariableDeclaration42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_VariableDeclaration__rell_VariableDeclaration42", None)
        self.__rell_VariableDeclaration42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_RelAttrubutesList41"):
                opp_val = getattr(old_value, "rell_RelAttrubutesList41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_RelAttrubutesList41"):
                opp_val = getattr(value, "rell_RelAttrubutesList41", None)
                if opp_val is None:
                    setattr(value, "rell_RelAttrubutesList41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rell_VariableDeclaration86(self):
        return self.__rell_VariableDeclaration86

    @rell_VariableDeclaration86.setter
    def rell_VariableDeclaration86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_VariableDeclaration__rell_VariableDeclaration86", None)
        self.__rell_VariableDeclaration86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_VariableRef"):
                opp_val = getattr(old_value, "rell_VariableRef", None)
                if opp_val == self:
                    setattr(old_value, "rell_VariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_VariableRef"):
                opp_val = getattr(value, "rell_VariableRef", None)
                setattr(value, "rell_VariableRef", self)

    @property
    def rell_VariableDeclaration33(self):
        return self.__rell_VariableDeclaration33

    @rell_VariableDeclaration33.setter
    def rell_VariableDeclaration33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_VariableDeclaration__rell_VariableDeclaration33", None)
        self.__rell_VariableDeclaration33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_VariableInit32"):
                opp_val = getattr(old_value, "rell_VariableInit32", None)
                if opp_val == self:
                    setattr(old_value, "rell_VariableInit32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_VariableInit32"):
                opp_val = getattr(value, "rell_VariableInit32", None)
                setattr(value, "rell_VariableInit32", self)

    @property
    def rell_VariableDeclaration47(self):
        return self.__rell_VariableDeclaration47

    @rell_VariableDeclaration47.setter
    def rell_VariableDeclaration47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_VariableDeclaration__rell_VariableDeclaration47", None)
        self.__rell_VariableDeclaration47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_TypeReference"):
                opp_val = getattr(old_value, "rell_TypeReference", None)
                if opp_val == self:
                    setattr(old_value, "rell_TypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_TypeReference"):
                opp_val = getattr(value, "rell_TypeReference", None)
                setattr(value, "rell_TypeReference", self)

    @property
    def rell_VariableDeclaration(self):
        return self.__rell_VariableDeclaration

    @rell_VariableDeclaration.setter
    def rell_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_VariableDeclaration__rell_VariableDeclaration", None)
        self.__rell_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Variable15"):
                opp_val = getattr(old_value, "rell_Variable15", None)
                if opp_val == self:
                    setattr(old_value, "rell_Variable15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Variable15"):
                opp_val = getattr(value, "rell_Variable15", None)
                setattr(value, "rell_Variable15", self)

    @property
    def rell_VariableDeclaration45(self):
        return self.__rell_VariableDeclaration45

    @rell_VariableDeclaration45.setter
    def rell_VariableDeclaration45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_VariableDeclaration__rell_VariableDeclaration45", None)
        self.__rell_VariableDeclaration45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Attribute44"):
                opp_val = getattr(old_value, "rell_Attribute44", None)
                if opp_val == self:
                    setattr(old_value, "rell_Attribute44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Attribute44"):
                opp_val = getattr(value, "rell_Attribute44", None)
                setattr(value, "rell_Attribute44", self)

class rell_RelAttrubutesList:

    pass
class rell_Attribute:

    def __init__(self, modificator: str, rell_Attribute: "rell_ClassDefinition" = None, rell_Attribute44: "rell_VariableDeclaration" = None):
        self.modificator = modificator
        self.rell_Attribute = rell_Attribute
        self.rell_Attribute44 = rell_Attribute44
        
    @property
    def modificator(self) -> str:
        return self.__modificator

    @modificator.setter
    def modificator(self, modificator: str):
        self.__modificator = modificator

    @property
    def rell_Attribute(self):
        return self.__rell_Attribute

    @rell_Attribute.setter
    def rell_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_Attribute__rell_Attribute", None)
        self.__rell_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_ClassDefinition7"):
                opp_val = getattr(old_value, "rell_ClassDefinition7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_ClassDefinition7"):
                opp_val = getattr(value, "rell_ClassDefinition7", None)
                if opp_val is None:
                    setattr(value, "rell_ClassDefinition7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rell_Attribute44(self):
        return self.__rell_Attribute44

    @rell_Attribute44.setter
    def rell_Attribute44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_Attribute__rell_Attribute44", None)
        self.__rell_Attribute44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_VariableDeclaration45"):
                opp_val = getattr(old_value, "rell_VariableDeclaration45", None)
                if opp_val == self:
                    setattr(old_value, "rell_VariableDeclaration45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_VariableDeclaration45"):
                opp_val = getattr(value, "rell_VariableDeclaration45", None)
                setattr(value, "rell_VariableDeclaration45", self)

class rell_Operation:

    def __init__(self, name: str, rell_Operation: "rell_Model" = None, rell_Operation9: "rell_RelAttrubutesList" = None, rell_Operation11: set["rell_Statement"] = None):
        self.name = name
        self.rell_Operation = rell_Operation
        self.rell_Operation9 = rell_Operation9
        self.rell_Operation11 = rell_Operation11 if rell_Operation11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rell_Operation(self):
        return self.__rell_Operation

    @rell_Operation.setter
    def rell_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_Operation__rell_Operation", None)
        self.__rell_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Model2"):
                opp_val = getattr(old_value, "rell_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Model2"):
                opp_val = getattr(value, "rell_Model2", None)
                if opp_val is None:
                    setattr(value, "rell_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rell_Operation11(self):
        return self.__rell_Operation11

    @rell_Operation11.setter
    def rell_Operation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_Operation__rell_Operation11", None)
        self.__rell_Operation11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rell_Statement"):
                    opp_val = getattr(item, "rell_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "rell_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rell_Statement"):
                    opp_val = getattr(item, "rell_Statement", None)
                    
                    setattr(item, "rell_Statement", self)
                    

    @property
    def rell_Operation9(self):
        return self.__rell_Operation9

    @rell_Operation9.setter
    def rell_Operation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_Operation__rell_Operation9", None)
        self.__rell_Operation9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_RelAttrubutesList"):
                opp_val = getattr(old_value, "rell_RelAttrubutesList", None)
                if opp_val == self:
                    setattr(old_value, "rell_RelAttrubutesList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_RelAttrubutesList"):
                opp_val = getattr(value, "rell_RelAttrubutesList", None)
                setattr(value, "rell_RelAttrubutesList", self)

class rell_ClassDefinition:

    def __init__(self, name: str, rell_ClassDefinition: "rell_Model" = None, rell_ClassDefinition5: "rell_ClassDefinition" = None, rell_ClassDefinition3: "rell_ClassDefinition" = None, rell_ClassDefinition7: set["rell_Attribute"] = None, rell_ClassDefinition54: "rell_ClassType" = None):
        self.name = name
        self.rell_ClassDefinition = rell_ClassDefinition
        self.rell_ClassDefinition5 = rell_ClassDefinition5
        self.rell_ClassDefinition3 = rell_ClassDefinition3
        self.rell_ClassDefinition7 = rell_ClassDefinition7 if rell_ClassDefinition7 is not None else set()
        self.rell_ClassDefinition54 = rell_ClassDefinition54
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rell_ClassDefinition54(self):
        return self.__rell_ClassDefinition54

    @rell_ClassDefinition54.setter
    def rell_ClassDefinition54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_ClassDefinition__rell_ClassDefinition54", None)
        self.__rell_ClassDefinition54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_ClassType53"):
                opp_val = getattr(old_value, "rell_ClassType53", None)
                if opp_val == self:
                    setattr(old_value, "rell_ClassType53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_ClassType53"):
                opp_val = getattr(value, "rell_ClassType53", None)
                setattr(value, "rell_ClassType53", self)

    @property
    def rell_ClassDefinition3(self):
        return self.__rell_ClassDefinition3

    @rell_ClassDefinition3.setter
    def rell_ClassDefinition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_ClassDefinition__rell_ClassDefinition3", None)
        self.__rell_ClassDefinition3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_ClassDefinition5"):
                opp_val = getattr(old_value, "rell_ClassDefinition5", None)
                if opp_val == self:
                    setattr(old_value, "rell_ClassDefinition5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_ClassDefinition5"):
                opp_val = getattr(value, "rell_ClassDefinition5", None)
                setattr(value, "rell_ClassDefinition5", self)

    @property
    def rell_ClassDefinition5(self):
        return self.__rell_ClassDefinition5

    @rell_ClassDefinition5.setter
    def rell_ClassDefinition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_ClassDefinition__rell_ClassDefinition5", None)
        self.__rell_ClassDefinition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_ClassDefinition3"):
                opp_val = getattr(old_value, "rell_ClassDefinition3", None)
                if opp_val == self:
                    setattr(old_value, "rell_ClassDefinition3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_ClassDefinition3"):
                opp_val = getattr(value, "rell_ClassDefinition3", None)
                setattr(value, "rell_ClassDefinition3", self)

    @property
    def rell_ClassDefinition(self):
        return self.__rell_ClassDefinition

    @rell_ClassDefinition.setter
    def rell_ClassDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_ClassDefinition__rell_ClassDefinition", None)
        self.__rell_ClassDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rell_Model"):
                opp_val = getattr(old_value, "rell_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rell_Model"):
                opp_val = getattr(value, "rell_Model", None)
                if opp_val is None:
                    setattr(value, "rell_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rell_ClassDefinition7(self):
        return self.__rell_ClassDefinition7

    @rell_ClassDefinition7.setter
    def rell_ClassDefinition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rell_ClassDefinition__rell_ClassDefinition7", None)
        self.__rell_ClassDefinition7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rell_Attribute"):
                    opp_val = getattr(item, "rell_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "rell_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rell_Attribute"):
                    opp_val = getattr(item, "rell_Attribute", None)
                    
                    setattr(item, "rell_Attribute", self)
                    

class rell_Model:

    pass