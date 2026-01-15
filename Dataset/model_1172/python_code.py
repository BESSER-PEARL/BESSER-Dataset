from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class JavaBody:

    pass
class atlext_OCL_GetAppliedStereotypesBody(JavaBody):

    pass
class atlext_OCL_TypedElement(ABC):

    pass
class OclModelElement:

    pass
class NumericType:

    pass
class atlext_OCL_RealType(NumericType):

    pass
class atlext_OCL_IntegerType(NumericType):

    pass
class OclFeature:

    pass
class atlext_OCL_Operation(OclFeature):

    def __init__(self, name: str, atlext_OCL_Operation: set["Parameter"] = None, 317: "OclType" = None, 320: "OclExpression" = None, 295: "atlext_OCL_OclFeatureDefinition"):
        self.name = name
        self.atlext_OCL_Operation = atlext_OCL_Operation if atlext_OCL_Operation is not None else set()
        self.317 = 317
        self.320 = 320
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 317(self):
        return self.__317

    @317.setter
    def 317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Operation__317", None)
        self.__317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "318"):
                opp_val = getattr(old_value, "318", None)
                if opp_val == self:
                    setattr(old_value, "318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "318"):
                opp_val = getattr(value, "318", None)
                setattr(value, "318", self)

    @property
    def 320(self):
        return self.__320

    @320.setter
    def 320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Operation__320", None)
        self.__320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "321"):
                opp_val = getattr(old_value, "321", None)
                if opp_val == self:
                    setattr(old_value, "321", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "321"):
                opp_val = getattr(value, "321", None)
                setattr(value, "321", self)

    @property
    def atlext_OCL_Operation(self):
        return self.__atlext_OCL_Operation

    @atlext_OCL_Operation.setter
    def atlext_OCL_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Operation__atlext_OCL_Operation", None)
        self.__atlext_OCL_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter315"):
                    opp_val = getattr(item, "Parameter315", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter315", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter315"):
                    opp_val = getattr(item, "Parameter315", None)
                    
                    setattr(item, "Parameter315", self)
                    

class atlext_OCL_Attribute(OclFeature):

    def __init__(self, name: str, 312: "OclType" = None, 309: "OclExpression" = None, 295: "atlext_OCL_OclFeatureDefinition"):
        self.name = name
        self.312 = 312
        self.309 = 309
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 309(self):
        return self.__309

    @309.setter
    def 309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Attribute__309", None)
        self.__309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "310"):
                opp_val = getattr(old_value, "310", None)
                if opp_val == self:
                    setattr(old_value, "310", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "310"):
                opp_val = getattr(value, "310", None)
                setattr(value, "310", self)

    @property
    def 312(self):
        return self.__312

    @312.setter
    def 312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Attribute__312", None)
        self.__312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "313"):
                opp_val = getattr(old_value, "313", None)
                if opp_val == self:
                    setattr(old_value, "313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "313"):
                opp_val = getattr(value, "313", None)
                setattr(value, "313", self)

class TupleType:

    pass
class MapType:

    pass
class OclContextDefinition:

    pass
class Primitive:

    pass
class atlext_OCL_BooleanType(Primitive):

    pass
class atlext_OCL_NumericType(Primitive):

    pass
class atlext_OCL_StringType(Primitive):

    pass
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class atlext_OCL_BagType(CollectionType):

    pass
class atlext_OCL_OrderedSetType(CollectionType):

    pass
class atlext_OCL_SetType(CollectionType):

    pass
class atlext_OCL_SequenceType(CollectionType):

    pass
class VariableExp:

    pass
class IterateExp:

    pass
class ResolveTempResolution:

    pass
class MapExp:

    pass
class MapElement:

    pass
class ContextHelper:

    pass
class NumericExp:

    pass
class atlext_OCL_RealExp(NumericExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class PrimitiveExp:

    pass
class atlext_OCL_NumericExp(PrimitiveExp):

    pass
class atlext_OCL_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class atlext_OCL_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class TupleExp:

    pass
class TuplePart:

    pass
class atlext_OCL_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class CollectionExp:

    pass
class atlext_OCL_SequenceExp(CollectionExp):

    pass
class atlext_OCL_OrderedSetExp(CollectionExp):

    pass
class atlext_OCL_BagExp(CollectionExp):

    pass
class atlext_OCL_SetExp(CollectionExp):

    pass
class IfExp:

    pass
class OclType:

    pass
class atlext_OCL_Primitive(OclType):

    pass
class atlext_OCL_MapType(OclType):

    pass
class atlext_OCL_OclModelElement(OclType):

    pass
class atlext_OCL_CollectionType(OclType):

    pass
class atlext_OCL_TupleType(OclType):

    pass
class atlext_OCL_OclAnyType(OclType):

    pass
class OCL_TypedElement:

    pass
class ATL_LocatedElement:

    pass
class atlext_OCL_VariableDeclaration(OCL_TypedElement, ATL_LocatedElement):

    def __init__(self, id: str, varName: str, 228: "OclType" = None, 231: "OclExpression" = None, 234: "LetExp" = None, 237: "IterateExp" = None, 240: set["VariableExp"] = None):
        self.id = id
        self.varName = varName
        self.228 = 228
        self.231 = 231
        self.234 = 234
        self.237 = 237
        self.240 = 240 if 240 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def 228(self):
        return self.__228

    @228.setter
    def 228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__228", None)
        self.__228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "229"):
                opp_val = getattr(old_value, "229", None)
                if opp_val == self:
                    setattr(old_value, "229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "229"):
                opp_val = getattr(value, "229", None)
                setattr(value, "229", self)

    @property
    def 231(self):
        return self.__231

    @231.setter
    def 231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__231", None)
        self.__231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "232"):
                opp_val = getattr(old_value, "232", None)
                if opp_val == self:
                    setattr(old_value, "232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "232"):
                opp_val = getattr(value, "232", None)
                setattr(value, "232", self)

    @property
    def 240(self):
        return self.__240

    @240.setter
    def 240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__240", None)
        self.__240 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "241"):
                    opp_val = getattr(item, "241", None)
                    
                    if opp_val == self:
                        setattr(item, "241", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "241"):
                    opp_val = getattr(item, "241", None)
                    
                    setattr(item, "241", self)
                    

    @property
    def 237(self):
        return self.__237

    @237.setter
    def 237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__237", None)
        self.__237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "238"):
                opp_val = getattr(old_value, "238", None)
                if opp_val == self:
                    setattr(old_value, "238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "238"):
                opp_val = getattr(value, "238", None)
                setattr(value, "238", self)

    @property
    def 234(self):
        return self.__234

    @234.setter
    def 234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__234", None)
        self.__234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "235"):
                opp_val = getattr(old_value, "235", None)
                if opp_val == self:
                    setattr(old_value, "235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "235"):
                opp_val = getattr(value, "235", None)
                setattr(value, "235", self)

class atlext_OCL_OclExpression(OCL_TypedElement, ATL_LocatedElement):

    def __init__(self, implicitlyCasted: str, 146: "LetExp" = None, 149: "LoopExp" = None, 152: "OperationCallExp" = None, 155: "VariableDeclaration" = None, 158: "IfExp" = None, 161: "Operation" = None, 164: "IfExp" = None, 167: "Attribute" = None, 134: "OclType" = None, 137: "IfExp" = None, 140: "PropertyCallExp" = None, 143: "CollectionExp" = None):
        self.implicitlyCasted = implicitlyCasted
        self.146 = 146
        self.149 = 149
        self.152 = 152
        self.155 = 155
        self.158 = 158
        self.161 = 161
        self.164 = 164
        self.167 = 167
        self.134 = 134
        self.137 = 137
        self.140 = 140
        self.143 = 143
        
    @property
    def implicitlyCasted(self) -> str:
        return self.__implicitlyCasted

    @implicitlyCasted.setter
    def implicitlyCasted(self, implicitlyCasted: str):
        self.__implicitlyCasted = implicitlyCasted

    @property
    def 167(self):
        return self.__167

    @167.setter
    def 167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__167", None)
        self.__167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "168"):
                opp_val = getattr(old_value, "168", None)
                if opp_val == self:
                    setattr(old_value, "168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "168"):
                opp_val = getattr(value, "168", None)
                setattr(value, "168", self)

    @property
    def 155(self):
        return self.__155

    @155.setter
    def 155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__155", None)
        self.__155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "156"):
                opp_val = getattr(old_value, "156", None)
                if opp_val == self:
                    setattr(old_value, "156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "156"):
                opp_val = getattr(value, "156", None)
                setattr(value, "156", self)

    @property
    def 164(self):
        return self.__164

    @164.setter
    def 164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__164", None)
        self.__164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "165"):
                opp_val = getattr(old_value, "165", None)
                if opp_val == self:
                    setattr(old_value, "165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "165"):
                opp_val = getattr(value, "165", None)
                setattr(value, "165", self)

    @property
    def 134(self):
        return self.__134

    @134.setter
    def 134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__134", None)
        self.__134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "135"):
                opp_val = getattr(old_value, "135", None)
                if opp_val == self:
                    setattr(old_value, "135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "135"):
                opp_val = getattr(value, "135", None)
                setattr(value, "135", self)

    @property
    def 152(self):
        return self.__152

    @152.setter
    def 152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__152", None)
        self.__152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "153"):
                opp_val = getattr(old_value, "153", None)
                if opp_val == self:
                    setattr(old_value, "153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "153"):
                opp_val = getattr(value, "153", None)
                setattr(value, "153", self)

    @property
    def 140(self):
        return self.__140

    @140.setter
    def 140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__140", None)
        self.__140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "141"):
                opp_val = getattr(old_value, "141", None)
                if opp_val == self:
                    setattr(old_value, "141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "141"):
                opp_val = getattr(value, "141", None)
                setattr(value, "141", self)

    @property
    def 146(self):
        return self.__146

    @146.setter
    def 146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__146", None)
        self.__146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "147"):
                opp_val = getattr(old_value, "147", None)
                if opp_val == self:
                    setattr(old_value, "147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "147"):
                opp_val = getattr(value, "147", None)
                setattr(value, "147", self)

    @property
    def 143(self):
        return self.__143

    @143.setter
    def 143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__143", None)
        self.__143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "144"):
                opp_val = getattr(old_value, "144", None)
                if opp_val == self:
                    setattr(old_value, "144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "144"):
                opp_val = getattr(value, "144", None)
                setattr(value, "144", self)

    @property
    def 158(self):
        return self.__158

    @158.setter
    def 158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__158", None)
        self.__158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "159"):
                opp_val = getattr(old_value, "159", None)
                if opp_val == self:
                    setattr(old_value, "159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "159"):
                opp_val = getattr(value, "159", None)
                setattr(value, "159", self)

    @property
    def 149(self):
        return self.__149

    @149.setter
    def 149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__149", None)
        self.__149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "150"):
                opp_val = getattr(old_value, "150", None)
                if opp_val == self:
                    setattr(old_value, "150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "150"):
                opp_val = getattr(value, "150", None)
                setattr(value, "150", self)

    @property
    def 161(self):
        return self.__161

    @161.setter
    def 161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__161", None)
        self.__161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "162"):
                opp_val = getattr(old_value, "162", None)
                if opp_val == self:
                    setattr(old_value, "162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "162"):
                opp_val = getattr(value, "162", None)
                setattr(value, "162", self)

    @property
    def 137(self):
        return self.__137

    @137.setter
    def 137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__137", None)
        self.__137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "138"):
                opp_val = getattr(old_value, "138", None)
                if opp_val == self:
                    setattr(old_value, "138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "138"):
                opp_val = getattr(value, "138", None)
                setattr(value, "138", self)

class Attribute:

    pass
class Operation:

    pass
class OperationCallExp:

    pass
class atlext_OCL_OperatorCallExp(OperationCallExp):

    pass
class atlext_OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class LoopExp:

    pass
class atlext_OCL_IterateExp(LoopExp):

    pass
class atlext_OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, 244: "atlext_OCL_Iterator", 150: "atlext_OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class LetExp:

    pass
class MatchedRule:

    pass
class atlext_ATL_RuleResolutionInfo:

    pass
class atlext_ATL_CallableParameter:

    def __init__(self, name: str, atlext_ATL_CallableParameter: "VariableDeclaration" = None):
        self.name = name
        self.atlext_ATL_CallableParameter = atlext_ATL_CallableParameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atlext_ATL_CallableParameter(self):
        return self.__atlext_ATL_CallableParameter

    @atlext_ATL_CallableParameter.setter
    def atlext_ATL_CallableParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_CallableParameter__atlext_ATL_CallableParameter", None)
        self.__atlext_ATL_CallableParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration"):
                opp_val = getattr(old_value, "VariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration"):
                opp_val = getattr(value, "VariableDeclaration", None)
                setattr(value, "VariableDeclaration", self)

class atlext_ATL_StringToStringMap:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class RuleResolutionInfo:

    pass
class atlext_OCL_ResolveTempResolution(RuleResolutionInfo):

    pass
class Statement:

    pass
class atlext_ATL_ForStat(Statement):

    pass
class atlext_ATL_BindingStat(Statement):

    def __init__(self, propertyName: str, isAssignment: str, atlext_ATL_BindingStat: "OclExpression" = None, atlext_ATL_BindingStat110: "OclExpression" = None, Statement119: "atlext_ATL_IfStat", Statement: "atlext_ATL_ActionBlock", Statement116: "atlext_ATL_IfStat", Statement127: "atlext_ATL_ForStat"):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.atlext_ATL_BindingStat = atlext_ATL_BindingStat
        self.atlext_ATL_BindingStat110 = atlext_ATL_BindingStat110
        
    @property
    def isAssignment(self) -> str:
        return self.__isAssignment

    @isAssignment.setter
    def isAssignment(self, isAssignment: str):
        self.__isAssignment = isAssignment

    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def atlext_ATL_BindingStat110(self):
        return self.__atlext_ATL_BindingStat110

    @atlext_ATL_BindingStat110.setter
    def atlext_ATL_BindingStat110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_BindingStat__atlext_ATL_BindingStat110", None)
        self.__atlext_ATL_BindingStat110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression111"):
                opp_val = getattr(old_value, "OclExpression111", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression111"):
                opp_val = getattr(value, "OclExpression111", None)
                setattr(value, "OclExpression111", self)

    @property
    def atlext_ATL_BindingStat(self):
        return self.__atlext_ATL_BindingStat

    @atlext_ATL_BindingStat.setter
    def atlext_ATL_BindingStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_BindingStat__atlext_ATL_BindingStat", None)
        self.__atlext_ATL_BindingStat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression108"):
                opp_val = getattr(old_value, "OclExpression108", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression108"):
                opp_val = getattr(value, "OclExpression108", None)
                setattr(value, "OclExpression108", self)

class atlext_ATL_ExpressionStat(Statement):

    pass
class atlext_ATL_IfStat(Statement):

    pass
class PatternElement:

    pass
class atlext_ATL_InPatternElement(PatternElement):

    pass
class VariableDeclaration:

    pass
class atlext_ATL_RuleVariableDeclaration(VariableDeclaration):

    pass
class atlext_OCL_TuplePart(VariableDeclaration):

    pass
class atlext_OCL_Iterator(VariableDeclaration):

    pass
class atlext_OCL_Parameter(VariableDeclaration):

    pass
class atlext_ATL_PatternElement(VariableDeclaration):

    pass
class Iterator:

    pass
class Binding:

    pass
class atlext_ATL_OutPatternElement(PatternElement):

    pass
class OutPatternElement:

    pass
class atlext_ATL_SimpleOutPatternElement(OutPatternElement):

    pass
class atlext_ATL_ForEachOutPatternElement(OutPatternElement):

    pass
class DropPattern:

    pass
class RuleWithPattern:

    pass
class InPattern:

    pass
class Rule:

    pass
class atlext_ATL_RuleWithPattern(Rule):

    def __init__(self, isAbstract: str, isRefining: str, isNoDefault: str, atlext_ATL_RuleWithPattern: "InPattern" = None, 40: set["RuleWithPattern"] = None, 43: "RuleWithPattern" = None, 53: "atlext_ATL_OutPattern", 97: "atlext_ATL_RuleVariableDeclaration", 103: "atlext_ATL_ActionBlock"):
        self.isAbstract = isAbstract
        self.isRefining = isRefining
        self.isNoDefault = isNoDefault
        self.atlext_ATL_RuleWithPattern = atlext_ATL_RuleWithPattern
        self.40 = 40 if 40 is not None else set()
        self.43 = 43
        
    @property
    def isNoDefault(self) -> str:
        return self.__isNoDefault

    @isNoDefault.setter
    def isNoDefault(self, isNoDefault: str):
        self.__isNoDefault = isNoDefault

    @property
    def isRefining(self) -> str:
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining

    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def 43(self):
        return self.__43

    @43.setter
    def 43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_RuleWithPattern__43", None)
        self.__43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "44"):
                opp_val = getattr(old_value, "44", None)
                if opp_val == self:
                    setattr(old_value, "44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "44"):
                opp_val = getattr(value, "44", None)
                setattr(value, "44", self)

    @property
    def atlext_ATL_RuleWithPattern(self):
        return self.__atlext_ATL_RuleWithPattern

    @atlext_ATL_RuleWithPattern.setter
    def atlext_ATL_RuleWithPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_RuleWithPattern__atlext_ATL_RuleWithPattern", None)
        self.__atlext_ATL_RuleWithPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InPattern"):
                opp_val = getattr(old_value, "InPattern", None)
                if opp_val == self:
                    setattr(old_value, "InPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InPattern"):
                opp_val = getattr(value, "InPattern", None)
                setattr(value, "InPattern", self)

    @property
    def 40(self):
        return self.__40

    @40.setter
    def 40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_RuleWithPattern__40", None)
        self.__40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "41"):
                    opp_val = getattr(item, "41", None)
                    
                    if opp_val == self:
                        setattr(item, "41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "41"):
                    opp_val = getattr(item, "41", None)
                    
                    setattr(item, "41", self)
                    

class CallableParameter:

    pass
class InPatternElement:

    pass
class atlext_ATL_SimpleInPatternElement(InPatternElement):

    pass
class Parameter:

    pass
class StaticRule:

    pass
class atlext_ATL_CalledRule(StaticRule):

    def __init__(self, isEntrypoint: str, isEndpoint: str, atlext_ATL_CalledRule: set["Parameter"] = None):
        self.isEntrypoint = isEntrypoint
        self.isEndpoint = isEndpoint
        self.atlext_ATL_CalledRule = atlext_ATL_CalledRule if atlext_ATL_CalledRule is not None else set()
        
    @property
    def isEntrypoint(self) -> str:
        return self.__isEntrypoint

    @isEntrypoint.setter
    def isEntrypoint(self, isEntrypoint: str):
        self.__isEntrypoint = isEntrypoint

    @property
    def isEndpoint(self) -> str:
        return self.__isEndpoint

    @isEndpoint.setter
    def isEndpoint(self, isEndpoint: str):
        self.__isEndpoint = isEndpoint

    @property
    def atlext_ATL_CalledRule(self):
        return self.__atlext_ATL_CalledRule

    @atlext_ATL_CalledRule.setter
    def atlext_ATL_CalledRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_CalledRule__atlext_ATL_CalledRule", None)
        self.__atlext_ATL_CalledRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

class ATL_StaticRule:

    pass
class ATL_RuleWithPattern:

    pass
class atlext_ATL_LazyRule(ATL_RuleWithPattern, ATL_StaticRule):

    def __init__(self, isUnique: str):
        self.isUnique = isUnique
        
    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

class atlext_ATL_MatchedRule(RuleWithPattern):

    pass
class OclFeatureDefinition:

    pass
class Library:

    pass
class Query:

    pass
class ATL_Callable:

    pass
class ATL_ModuleElement:

    pass
class atlext_ATL_Helper(ATL_Callable, ATL_ModuleElement):

    def __init__(self, hasContext: bool, isAttribute: str, 17: "Query" = None, 20: "Library" = None, atlext_ATL_Helper: "OclFeatureDefinition" = None):
        self.hasContext = hasContext
        self.isAttribute = isAttribute
        self.17 = 17
        self.20 = 20
        self.atlext_ATL_Helper = atlext_ATL_Helper
        
    @property
    def isAttribute(self) -> str:
        return self.__isAttribute

    @isAttribute.setter
    def isAttribute(self, isAttribute: str):
        self.__isAttribute = isAttribute

    @property
    def hasContext(self) -> bool:
        return self.__hasContext

    @hasContext.setter
    def hasContext(self, hasContext: bool):
        self.__hasContext = hasContext

    @property
    def 20(self):
        return self.__20

    @20.setter
    def 20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__20", None)
        self.__20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "21"):
                opp_val = getattr(old_value, "21", None)
                if opp_val == self:
                    setattr(old_value, "21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "21"):
                opp_val = getattr(value, "21", None)
                setattr(value, "21", self)

    @property
    def atlext_ATL_Helper(self):
        return self.__atlext_ATL_Helper

    @atlext_ATL_Helper.setter
    def atlext_ATL_Helper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__atlext_ATL_Helper", None)
        self.__atlext_ATL_Helper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclFeatureDefinition"):
                opp_val = getattr(old_value, "OclFeatureDefinition", None)
                if opp_val == self:
                    setattr(old_value, "OclFeatureDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclFeatureDefinition"):
                opp_val = getattr(value, "OclFeatureDefinition", None)
                setattr(value, "OclFeatureDefinition", self)

    @property
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__17", None)
        self.__17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "18"):
                opp_val = getattr(old_value, "18", None)
                if opp_val == self:
                    setattr(old_value, "18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "18"):
                opp_val = getattr(value, "18", None)
                setattr(value, "18", self)

class atlext_ATL_Callable(ABC):

    pass
class Callable:

    pass
class atlext_ATL_ModuleCallable(Callable):

    pass
class ATL_Rule:

    pass
class RuleVariableDeclaration:

    pass
class ActionBlock:

    pass
class OutPattern:

    pass
class PropertyCallExp:

    pass
class atlext_OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, 200: set["OclExpression"] = None, atlext_OCL_OperationCallExp: set["ResolveTempResolution"] = None, 25: "atlext_ATL_ContextHelper", 141: "atlext_OCL_OclExpression", PropertyCallExp: "atlext_ATL_Callable"):
        self.operationName = operationName
        self.200 = 200 if 200 is not None else set()
        self.atlext_OCL_OperationCallExp = atlext_OCL_OperationCallExp if atlext_OCL_OperationCallExp is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def 200(self):
        return self.__200

    @200.setter
    def 200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OperationCallExp__200", None)
        self.__200 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "201"):
                    opp_val = getattr(item, "201", None)
                    
                    if opp_val == self:
                        setattr(item, "201", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "201"):
                    opp_val = getattr(item, "201", None)
                    
                    setattr(item, "201", self)
                    

    @property
    def atlext_OCL_OperationCallExp(self):
        return self.__atlext_OCL_OperationCallExp

    @atlext_OCL_OperationCallExp.setter
    def atlext_OCL_OperationCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OperationCallExp__atlext_OCL_OperationCallExp", None)
        self.__atlext_OCL_OperationCallExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResolveTempResolution"):
                    opp_val = getattr(item, "ResolveTempResolution", None)
                    
                    if opp_val == self:
                        setattr(item, "ResolveTempResolution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResolveTempResolution"):
                    opp_val = getattr(item, "ResolveTempResolution", None)
                    
                    setattr(item, "ResolveTempResolution", self)
                    

class atlext_OCL_LoopExp(PropertyCallExp):

    pass
class atlext_OCL_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str, 25: "atlext_ATL_ContextHelper", 141: "atlext_OCL_OclExpression", PropertyCallExp: "atlext_ATL_Callable"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ATL_ModuleCallable:

    pass
class atlext_ATL_StaticRule(ATL_Rule, ATL_ModuleCallable):

    pass
class ATL_Helper:

    pass
class atlext_ATL_StaticHelper(ATL_Helper, ATL_ModuleCallable):

    pass
class LocatedElement:

    pass
class atlext_OCL_OclFeatureDefinition(LocatedElement):

    pass
class atlext_ATL_ActionBlock(LocatedElement):

    pass
class atlext_ATL_Statement(LocatedElement):

    pass
class atlext_ATL_ModuleElement(LocatedElement):

    pass
class atlext_ATL_LibraryRef(LocatedElement):

    def __init__(self, name: str, 99: "Unit" = None):
        self.name = name
        self.99 = 99
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 99(self):
        return self.__99

    @99.setter
    def 99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_LibraryRef__99", None)
        self.__99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "100"):
                opp_val = getattr(old_value, "100", None)
                if opp_val == self:
                    setattr(old_value, "100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "100"):
                opp_val = getattr(value, "100", None)
                setattr(value, "100", self)

class atlext_ATL_OutPattern(LocatedElement):

    pass
class atlext_ATL_InPattern(LocatedElement):

    pass
class atlext_OCL_OclFeature(LocatedElement):

    pass
class atlext_OCL_OclModel(LocatedElement):

    def __init__(self, name: str, 323: "OclModel" = None, 326: set["OclModelElement"] = None, 329: set["OclModel"] = None):
        self.name = name
        self.323 = 323
        self.326 = 326 if 326 is not None else set()
        self.329 = 329 if 329 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 329(self):
        return self.__329

    @329.setter
    def 329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclModel__329", None)
        self.__329 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "330"):
                    opp_val = getattr(item, "330", None)
                    
                    if opp_val == self:
                        setattr(item, "330", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "330"):
                    opp_val = getattr(item, "330", None)
                    
                    setattr(item, "330", self)
                    

    @property
    def 323(self):
        return self.__323

    @323.setter
    def 323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclModel__323", None)
        self.__323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "324"):
                opp_val = getattr(old_value, "324", None)
                if opp_val == self:
                    setattr(old_value, "324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "324"):
                opp_val = getattr(value, "324", None)
                setattr(value, "324", self)

    @property
    def 326(self):
        return self.__326

    @326.setter
    def 326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclModel__326", None)
        self.__326 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "327"):
                    opp_val = getattr(item, "327", None)
                    
                    if opp_val == self:
                        setattr(item, "327", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "327"):
                    opp_val = getattr(item, "327", None)
                    
                    setattr(item, "327", self)
                    

class atlext_ATL_Binding(LocatedElement):

    def __init__(self, propertyName: str, isAssignment: str, atlext_ATL_Binding: "OclExpression" = None, 91: "OutPatternElement" = None, atlext_ATL_Binding94: set["RuleResolutionInfo"] = None):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.atlext_ATL_Binding = atlext_ATL_Binding
        self.91 = 91
        self.atlext_ATL_Binding94 = atlext_ATL_Binding94 if atlext_ATL_Binding94 is not None else set()
        
    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def isAssignment(self) -> str:
        return self.__isAssignment

    @isAssignment.setter
    def isAssignment(self, isAssignment: str):
        self.__isAssignment = isAssignment

    @property
    def atlext_ATL_Binding94(self):
        return self.__atlext_ATL_Binding94

    @atlext_ATL_Binding94.setter
    def atlext_ATL_Binding94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Binding__atlext_ATL_Binding94", None)
        self.__atlext_ATL_Binding94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RuleResolutionInfo"):
                    opp_val = getattr(item, "RuleResolutionInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "RuleResolutionInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RuleResolutionInfo"):
                    opp_val = getattr(item, "RuleResolutionInfo", None)
                    
                    setattr(item, "RuleResolutionInfo", self)
                    

    @property
    def 91(self):
        return self.__91

    @91.setter
    def 91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Binding__91", None)
        self.__91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "92"):
                opp_val = getattr(old_value, "92", None)
                if opp_val == self:
                    setattr(old_value, "92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "92"):
                opp_val = getattr(value, "92", None)
                setattr(value, "92", self)

    @property
    def atlext_ATL_Binding(self):
        return self.__atlext_ATL_Binding

    @atlext_ATL_Binding.setter
    def atlext_ATL_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Binding__atlext_ATL_Binding", None)
        self.__atlext_ATL_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression89"):
                opp_val = getattr(old_value, "OclExpression89", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression89"):
                opp_val = getattr(value, "OclExpression89", None)
                setattr(value, "OclExpression89", self)

class atlext_OCL_MapElement(LocatedElement):

    pass
class atlext_ATL_DropPattern(LocatedElement):

    pass
class atlext_OCL_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, 282: "TupleType" = None, 279: "OclType" = None):
        self.name = name
        self.282 = 282
        self.279 = 279
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 279(self):
        return self.__279

    @279.setter
    def 279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_TupleTypeAttribute__279", None)
        self.__279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "280"):
                opp_val = getattr(old_value, "280", None)
                if opp_val == self:
                    setattr(old_value, "280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "280"):
                opp_val = getattr(value, "280", None)
                setattr(value, "280", self)

    @property
    def 282(self):
        return self.__282

    @282.setter
    def 282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_TupleTypeAttribute__282", None)
        self.__282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "283"):
                opp_val = getattr(old_value, "283", None)
                if opp_val == self:
                    setattr(old_value, "283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "283"):
                opp_val = getattr(value, "283", None)
                setattr(value, "283", self)

class atlext_OCL_OclContextDefinition(LocatedElement):

    pass
class atlext_ATL_Unit(LocatedElement):

    def __init__(self, name: str, : set["LibraryRef"] = None):
        self.name = name
        self. =  if  is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Unit__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "2"):
                    opp_val = getattr(item, "2", None)
                    
                    if opp_val == self:
                        setattr(item, "2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "2"):
                    opp_val = getattr(item, "2", None)
                    
                    setattr(item, "2", self)
                    

class StringToStringMap:

    pass
class ModuleElement:

    pass
class atlext_ATL_Rule(ModuleElement):

    def __init__(self, name: str, 27: "OutPattern" = None, 30: "ActionBlock" = None, 33: set["RuleVariableDeclaration"] = None, ModuleElement: "atlext_ATL_Module"):
        self.name = name
        self.27 = 27
        self.30 = 30
        self.33 = 33 if 33 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 30(self):
        return self.__30

    @30.setter
    def 30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Rule__30", None)
        self.__30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "31"):
                opp_val = getattr(old_value, "31", None)
                if opp_val == self:
                    setattr(old_value, "31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "31"):
                opp_val = getattr(value, "31", None)
                setattr(value, "31", self)

    @property
    def 33(self):
        return self.__33

    @33.setter
    def 33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Rule__33", None)
        self.__33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "34"):
                    opp_val = getattr(item, "34", None)
                    
                    if opp_val == self:
                        setattr(item, "34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "34"):
                    opp_val = getattr(item, "34", None)
                    
                    setattr(item, "34", self)
                    

    @property
    def 27(self):
        return self.__27

    @27.setter
    def 27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Rule__27", None)
        self.__27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "28"):
                opp_val = getattr(old_value, "28", None)
                if opp_val == self:
                    setattr(old_value, "28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "28"):
                opp_val = getattr(value, "28", None)
                setattr(value, "28", self)

class OclModel:

    pass
class OclExpression:

    pass
class atlext_OCL_OclUndefinedExp(OclExpression):

    pass
class atlext_OCL_LetExp(OclExpression):

    pass
class atlext_OCL_CollectionExp(OclExpression):

    pass
class atlext_OCL_MapExp(OclExpression):

    pass
class atlext_OCL_TupleExp(OclExpression):

    pass
class atlext_OCL_PropertyCallExp(OclExpression):

    def __init__(self, isStaticCall: bool, 193: "OclExpression" = None, atlext_OCL_PropertyCallExp: "Callable" = None, 197: set["ContextHelper"] = None, 310: "atlext_OCL_Attribute", OclExpression50: "atlext_ATL_InPattern", 217: "atlext_OCL_LetExp", 194: "atlext_OCL_PropertyCallExp", OclExpression85: "atlext_ATL_ForEachOutPatternElement", 174: "atlext_OCL_CollectionExp", 201: "atlext_OCL_OperationCallExp", OclExpression: "atlext_ATL_Query", 226: "atlext_OCL_IfExp", 220: "atlext_OCL_IfExp", 321: "atlext_OCL_Operation", OclExpression124: "atlext_ATL_ForStat", OclExpression106: "atlext_ATL_ExpressionStat", OclExpression188: "atlext_OCL_MapElement", 223: "atlext_OCL_IfExp", 253: "atlext_OCL_OclType", 232: "atlext_OCL_VariableDeclaration", OclExpression83: "atlext_ATL_SimpleOutPatternElement", OclExpression89: "atlext_ATL_Binding", OclExpression113: "atlext_ATL_IfStat", OclExpression108: "atlext_ATL_BindingStat", 205: "atlext_OCL_LoopExp", OclExpression191: "atlext_OCL_MapElement", OclExpression111: "atlext_ATL_BindingStat"):
        self.isStaticCall = isStaticCall
        self.193 = 193
        self.atlext_OCL_PropertyCallExp = atlext_OCL_PropertyCallExp
        self.197 = 197 if 197 is not None else set()
        
    @property
    def isStaticCall(self) -> bool:
        return self.__isStaticCall

    @isStaticCall.setter
    def isStaticCall(self, isStaticCall: bool):
        self.__isStaticCall = isStaticCall

    @property
    def 197(self):
        return self.__197

    @197.setter
    def 197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__197", None)
        self.__197 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "198"):
                    opp_val = getattr(item, "198", None)
                    
                    if opp_val == self:
                        setattr(item, "198", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "198"):
                    opp_val = getattr(item, "198", None)
                    
                    setattr(item, "198", self)
                    

    @property
    def 193(self):
        return self.__193

    @193.setter
    def 193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__193", None)
        self.__193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "194"):
                opp_val = getattr(old_value, "194", None)
                if opp_val == self:
                    setattr(old_value, "194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "194"):
                opp_val = getattr(value, "194", None)
                setattr(value, "194", self)

    @property
    def atlext_OCL_PropertyCallExp(self):
        return self.__atlext_OCL_PropertyCallExp

    @atlext_OCL_PropertyCallExp.setter
    def atlext_OCL_PropertyCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__atlext_OCL_PropertyCallExp", None)
        self.__atlext_OCL_PropertyCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Callable"):
                opp_val = getattr(old_value, "Callable", None)
                if opp_val == self:
                    setattr(old_value, "Callable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Callable"):
                opp_val = getattr(value, "Callable", None)
                setattr(value, "Callable", self)

class atlext_OCL_JavaBody(OclExpression):

    pass
class atlext_OCL_OclType(OclExpression):

    def __init__(self, name: str, 258: "MapType" = None, 261: "Attribute" = None, 264: "MapType" = None, 267: "CollectionType" = None, 270: "TupleTypeAttribute" = None, 273: "VariableDeclaration" = None, 249: "OclContextDefinition" = None, 252: "OclExpression" = None, 255: "Operation" = None, 310: "atlext_OCL_Attribute", OclExpression50: "atlext_ATL_InPattern", 217: "atlext_OCL_LetExp", 194: "atlext_OCL_PropertyCallExp", OclExpression85: "atlext_ATL_ForEachOutPatternElement", 174: "atlext_OCL_CollectionExp", 201: "atlext_OCL_OperationCallExp", OclExpression: "atlext_ATL_Query", 226: "atlext_OCL_IfExp", 220: "atlext_OCL_IfExp", 321: "atlext_OCL_Operation", OclExpression124: "atlext_ATL_ForStat", OclExpression106: "atlext_ATL_ExpressionStat", OclExpression188: "atlext_OCL_MapElement", 223: "atlext_OCL_IfExp", 253: "atlext_OCL_OclType", 232: "atlext_OCL_VariableDeclaration", OclExpression83: "atlext_ATL_SimpleOutPatternElement", OclExpression89: "atlext_ATL_Binding", OclExpression113: "atlext_ATL_IfStat", OclExpression108: "atlext_ATL_BindingStat", 205: "atlext_OCL_LoopExp", OclExpression191: "atlext_OCL_MapElement", OclExpression111: "atlext_ATL_BindingStat"):
        self.name = name
        self.258 = 258
        self.261 = 261
        self.264 = 264
        self.267 = 267
        self.270 = 270
        self.273 = 273
        self.249 = 249
        self.252 = 252
        self.255 = 255
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 252(self):
        return self.__252

    @252.setter
    def 252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__252", None)
        self.__252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "253"):
                opp_val = getattr(old_value, "253", None)
                if opp_val == self:
                    setattr(old_value, "253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "253"):
                opp_val = getattr(value, "253", None)
                setattr(value, "253", self)

    @property
    def 273(self):
        return self.__273

    @273.setter
    def 273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__273", None)
        self.__273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "274"):
                opp_val = getattr(old_value, "274", None)
                if opp_val == self:
                    setattr(old_value, "274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "274"):
                opp_val = getattr(value, "274", None)
                setattr(value, "274", self)

    @property
    def 267(self):
        return self.__267

    @267.setter
    def 267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__267", None)
        self.__267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "268"):
                opp_val = getattr(old_value, "268", None)
                if opp_val == self:
                    setattr(old_value, "268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "268"):
                opp_val = getattr(value, "268", None)
                setattr(value, "268", self)

    @property
    def 258(self):
        return self.__258

    @258.setter
    def 258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__258", None)
        self.__258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "259"):
                opp_val = getattr(old_value, "259", None)
                if opp_val == self:
                    setattr(old_value, "259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "259"):
                opp_val = getattr(value, "259", None)
                setattr(value, "259", self)

    @property
    def 249(self):
        return self.__249

    @249.setter
    def 249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__249", None)
        self.__249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "250"):
                opp_val = getattr(old_value, "250", None)
                if opp_val == self:
                    setattr(old_value, "250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "250"):
                opp_val = getattr(value, "250", None)
                setattr(value, "250", self)

    @property
    def 264(self):
        return self.__264

    @264.setter
    def 264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__264", None)
        self.__264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "265"):
                opp_val = getattr(old_value, "265", None)
                if opp_val == self:
                    setattr(old_value, "265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "265"):
                opp_val = getattr(value, "265", None)
                setattr(value, "265", self)

    @property
    def 255(self):
        return self.__255

    @255.setter
    def 255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__255", None)
        self.__255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "256"):
                opp_val = getattr(old_value, "256", None)
                if opp_val == self:
                    setattr(old_value, "256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "256"):
                opp_val = getattr(value, "256", None)
                setattr(value, "256", self)

    @property
    def 261(self):
        return self.__261

    @261.setter
    def 261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__261", None)
        self.__261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "262"):
                opp_val = getattr(old_value, "262", None)
                if opp_val == self:
                    setattr(old_value, "262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "262"):
                opp_val = getattr(value, "262", None)
                setattr(value, "262", self)

    @property
    def 270(self):
        return self.__270

    @270.setter
    def 270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__270", None)
        self.__270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "271"):
                opp_val = getattr(old_value, "271", None)
                if opp_val == self:
                    setattr(old_value, "271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "271"):
                opp_val = getattr(value, "271", None)
                setattr(value, "271", self)

class atlext_OCL_PrimitiveExp(OclExpression):

    pass
class atlext_OCL_SuperExp(OclExpression):

    pass
class atlext_OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, 310: "atlext_OCL_Attribute", OclExpression50: "atlext_ATL_InPattern", 217: "atlext_OCL_LetExp", 194: "atlext_OCL_PropertyCallExp", OclExpression85: "atlext_ATL_ForEachOutPatternElement", 174: "atlext_OCL_CollectionExp", 201: "atlext_OCL_OperationCallExp", OclExpression: "atlext_ATL_Query", 226: "atlext_OCL_IfExp", 220: "atlext_OCL_IfExp", 321: "atlext_OCL_Operation", OclExpression124: "atlext_ATL_ForStat", OclExpression106: "atlext_ATL_ExpressionStat", OclExpression188: "atlext_OCL_MapElement", 223: "atlext_OCL_IfExp", 253: "atlext_OCL_OclType", 232: "atlext_OCL_VariableDeclaration", OclExpression83: "atlext_ATL_SimpleOutPatternElement", OclExpression89: "atlext_ATL_Binding", OclExpression113: "atlext_ATL_IfStat", OclExpression108: "atlext_ATL_BindingStat", 205: "atlext_OCL_LoopExp", OclExpression191: "atlext_OCL_MapElement", OclExpression111: "atlext_ATL_BindingStat"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class atlext_OCL_IfExp(OclExpression):

    pass
class atlext_OCL_VariableExp(OclExpression):

    pass
class Helper:

    pass
class atlext_ATL_ContextHelper(Helper):

    pass
class Unit:

    pass
class atlext_ATL_Module(Unit):

    def __init__(self, isRefining: str, atlext_ATL_Module: set["OclModel"] = None, atlext_ATL_Module12: set["OclModel"] = None, atlext_ATL_Module15: set["ModuleElement"] = None, 100: "atlext_ATL_LibraryRef"):
        self.isRefining = isRefining
        self.atlext_ATL_Module = atlext_ATL_Module if atlext_ATL_Module is not None else set()
        self.atlext_ATL_Module12 = atlext_ATL_Module12 if atlext_ATL_Module12 is not None else set()
        self.atlext_ATL_Module15 = atlext_ATL_Module15 if atlext_ATL_Module15 is not None else set()
        
    @property
    def isRefining(self) -> str:
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining

    @property
    def atlext_ATL_Module(self):
        return self.__atlext_ATL_Module

    @atlext_ATL_Module.setter
    def atlext_ATL_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Module__atlext_ATL_Module", None)
        self.__atlext_ATL_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel"):
                    opp_val = getattr(item, "OclModel", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel"):
                    opp_val = getattr(item, "OclModel", None)
                    
                    setattr(item, "OclModel", self)
                    

    @property
    def atlext_ATL_Module12(self):
        return self.__atlext_ATL_Module12

    @atlext_ATL_Module12.setter
    def atlext_ATL_Module12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Module__atlext_ATL_Module12", None)
        self.__atlext_ATL_Module12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel13"):
                    opp_val = getattr(item, "OclModel13", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel13"):
                    opp_val = getattr(item, "OclModel13", None)
                    
                    setattr(item, "OclModel13", self)
                    

    @property
    def atlext_ATL_Module15(self):
        return self.__atlext_ATL_Module15

    @atlext_ATL_Module15.setter
    def atlext_ATL_Module15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Module__atlext_ATL_Module15", None)
        self.__atlext_ATL_Module15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModuleElement"):
                    opp_val = getattr(item, "ModuleElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ModuleElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModuleElement"):
                    opp_val = getattr(item, "ModuleElement", None)
                    
                    setattr(item, "ModuleElement", self)
                    

class atlext_ATL_Query(Unit):

    pass
class atlext_ATL_Library(Unit):

    pass
class LibraryRef:

    pass
class atlext_ATL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str, fileLocation: str, fileObject: str, atlext_ATL_LocatedElement: set["StringToStringMap"] = None):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        self.fileLocation = fileLocation
        self.fileObject = fileObject
        self.atlext_ATL_LocatedElement = atlext_ATL_LocatedElement if atlext_ATL_LocatedElement is not None else set()
        
    @property
    def fileObject(self) -> str:
        return self.__fileObject

    @fileObject.setter
    def fileObject(self, fileObject: str):
        self.__fileObject = fileObject

    @property
    def commentsBefore(self) -> str:
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore

    @property
    def fileLocation(self) -> str:
        return self.__fileLocation

    @fileLocation.setter
    def fileLocation(self, fileLocation: str):
        self.__fileLocation = fileLocation

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

    @property
    def atlext_ATL_LocatedElement(self):
        return self.__atlext_ATL_LocatedElement

    @atlext_ATL_LocatedElement.setter
    def atlext_ATL_LocatedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_LocatedElement__atlext_ATL_LocatedElement", None)
        self.__atlext_ATL_LocatedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToStringMap"):
                    opp_val = getattr(item, "StringToStringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToStringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToStringMap"):
                    opp_val = getattr(item, "StringToStringMap", None)
                    
                    setattr(item, "StringToStringMap", self)
                    
