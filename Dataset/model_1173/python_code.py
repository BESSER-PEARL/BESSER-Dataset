from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RuleResolutionStatus(Enum):
    RESOLUTION_UNKNOWN = "RESOLUTION_UNKNOWN"
    RESOLUTION_CONFIRMED = "RESOLUTION_CONFIRMED"
    RESOLUTION_DISCARDED = "RESOLUTION_DISCARDED"


############################################
# Definition of Classes
############################################

class CollectionOperationCallExp:

    pass
class atlext_OCL2_SelectByKind(CollectionOperationCallExp):

    def __init__(self, isExact: bool):
        self.isExact = isExact
        
    @property
    def isExact(self) -> bool:
        return self.__isExact

    @isExact.setter
    def isExact(self, isExact: bool):
        self.__isExact = isExact

class JavaBody:

    pass
class atlext_OCL_GetAppliedStereotypesBody(JavaBody):

    pass
class atlext_OCL_TypedElement(ABC):

    pass
class OclModelElement:

    pass
class OclFeature:

    pass
class atlext_OCL_Operation(OclFeature):

    def __init__(self, name: str, atlext_OCL_Operation: set["Parameter"] = None, OclType310: "OclType" = None, OclExpression313: "OclExpression" = None, OCL288: "atlext_OCL_OclFeatureDefinition"):
        self.name = name
        self.atlext_OCL_Operation = atlext_OCL_Operation if atlext_OCL_Operation is not None else set()
        self.OclType310 = OclType310
        self.OclExpression313 = OclExpression313
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclExpression313(self):
        return self.__OclExpression313

    @OclExpression313.setter
    def OclExpression313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Operation__OclExpression313", None)
        self.__OclExpression313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL314"):
                opp_val = getattr(old_value, "OCL314", None)
                if opp_val == self:
                    setattr(old_value, "OCL314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL314"):
                opp_val = getattr(value, "OCL314", None)
                setattr(value, "OCL314", self)

    @property
    def OclType310(self):
        return self.__OclType310

    @OclType310.setter
    def OclType310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Operation__OclType310", None)
        self.__OclType310 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL311"):
                opp_val = getattr(old_value, "OCL311", None)
                if opp_val == self:
                    setattr(old_value, "OCL311", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL311"):
                opp_val = getattr(value, "OCL311", None)
                setattr(value, "OCL311", self)

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
                if hasattr(item, "Parameter308"):
                    opp_val = getattr(item, "Parameter308", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter308", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter308"):
                    opp_val = getattr(item, "Parameter308", None)
                    
                    setattr(item, "Parameter308", self)
                    

class atlext_OCL_Attribute(OclFeature):

    def __init__(self, name: str, OclExpression302: "OclExpression" = None, OclType305: "OclType" = None, OCL288: "atlext_OCL_OclFeatureDefinition"):
        self.name = name
        self.OclExpression302 = OclExpression302
        self.OclType305 = OclType305
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclType305(self):
        return self.__OclType305

    @OclType305.setter
    def OclType305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Attribute__OclType305", None)
        self.__OclType305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL306"):
                opp_val = getattr(old_value, "OCL306", None)
                if opp_val == self:
                    setattr(old_value, "OCL306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL306"):
                opp_val = getattr(value, "OCL306", None)
                setattr(value, "OCL306", self)

    @property
    def OclExpression302(self):
        return self.__OclExpression302

    @OclExpression302.setter
    def OclExpression302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_Attribute__OclExpression302", None)
        self.__OclExpression302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL303"):
                opp_val = getattr(old_value, "OCL303", None)
                if opp_val == self:
                    setattr(old_value, "OCL303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL303"):
                opp_val = getattr(value, "OCL303", None)
                setattr(value, "OCL303", self)

class TupleType:

    pass
class NumericType:

    pass
class atlext_OCL_RealType(NumericType):

    pass
class atlext_OCL_IntegerType(NumericType):

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
class atlext_OCL_OrderedSetType(CollectionType):

    pass
class atlext_OCL_SetType(CollectionType):

    pass
class atlext_OCL_BagType(CollectionType):

    pass
class atlext_OCL_SequenceType(CollectionType):

    pass
class MapType:

    pass
class OclContextDefinition:

    pass
class VariableExp:

    pass
class IterateExp:

    pass
class ResolveTempResolution:

    pass
class ContextHelper:

    pass
class OCL_atlext_EObject:

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

class MapExp:

    pass
class PrimitiveExp:

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

class atlext_OCL_NumericExp(PrimitiveExp):

    pass
class atlext_OCL_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class MapElement:

    pass
class TupleExp:

    pass
class OCL_atlext_Type:

    pass
class TuplePart:

    pass
class Attribute:

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

class LetExp:

    pass
class CollectionExp:

    pass
class atlext_OCL_OrderedSetExp(CollectionExp):

    pass
class atlext_OCL_BagExp(CollectionExp):

    pass
class atlext_OCL_SetExp(CollectionExp):

    pass
class atlext_OCL_SequenceExp(CollectionExp):

    pass
class IfExp:

    pass
class OclType:

    pass
class atlext_OCL_TupleType(OclType):

    pass
class atlext_OCL_OclModelElement(OclType):

    pass
class atlext_OCL_CollectionType(OclType):

    pass
class atlext_OCL_MapType(OclType):

    pass
class atlext_OCL_OclAnyType(OclType):

    pass
class atlext_OCL_Primitive(OclType):

    pass
class OCL_TypedElement:

    pass
class ATL_LocatedElement:

    pass
class atlext_OCL_VariableDeclaration(OCL_TypedElement, ATL_LocatedElement):

    def __init__(self, id: str, varName: str, OclType227: "OclType" = None, OclExpression230: "OclExpression" = None, LetExp233: "LetExp" = None, IterateExp: "IterateExp" = None, VariableExp: set["VariableExp"] = None, atlext_OCL_VariableDeclaration: "OCL_atlext_Type" = None):
        self.id = id
        self.varName = varName
        self.OclType227 = OclType227
        self.OclExpression230 = OclExpression230
        self.LetExp233 = LetExp233
        self.IterateExp = IterateExp
        self.VariableExp = VariableExp if VariableExp is not None else set()
        self.atlext_OCL_VariableDeclaration = atlext_OCL_VariableDeclaration
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def IterateExp(self):
        return self.__IterateExp

    @IterateExp.setter
    def IterateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__IterateExp", None)
        self.__IterateExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL236"):
                opp_val = getattr(old_value, "OCL236", None)
                if opp_val == self:
                    setattr(old_value, "OCL236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL236"):
                opp_val = getattr(value, "OCL236", None)
                setattr(value, "OCL236", self)

    @property
    def atlext_OCL_VariableDeclaration(self):
        return self.__atlext_OCL_VariableDeclaration

    @atlext_OCL_VariableDeclaration.setter
    def atlext_OCL_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__atlext_OCL_VariableDeclaration", None)
        self.__atlext_OCL_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL_atlext_Type240"):
                opp_val = getattr(old_value, "OCL_atlext_Type240", None)
                if opp_val == self:
                    setattr(old_value, "OCL_atlext_Type240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL_atlext_Type240"):
                opp_val = getattr(value, "OCL_atlext_Type240", None)
                setattr(value, "OCL_atlext_Type240", self)

    @property
    def LetExp233(self):
        return self.__LetExp233

    @LetExp233.setter
    def LetExp233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__LetExp233", None)
        self.__LetExp233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL234"):
                opp_val = getattr(old_value, "OCL234", None)
                if opp_val == self:
                    setattr(old_value, "OCL234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL234"):
                opp_val = getattr(value, "OCL234", None)
                setattr(value, "OCL234", self)

    @property
    def OclExpression230(self):
        return self.__OclExpression230

    @OclExpression230.setter
    def OclExpression230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__OclExpression230", None)
        self.__OclExpression230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL231"):
                opp_val = getattr(old_value, "OCL231", None)
                if opp_val == self:
                    setattr(old_value, "OCL231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL231"):
                opp_val = getattr(value, "OCL231", None)
                setattr(value, "OCL231", self)

    @property
    def OclType227(self):
        return self.__OclType227

    @OclType227.setter
    def OclType227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__OclType227", None)
        self.__OclType227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL228"):
                opp_val = getattr(old_value, "OCL228", None)
                if opp_val == self:
                    setattr(old_value, "OCL228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL228"):
                opp_val = getattr(value, "OCL228", None)
                setattr(value, "OCL228", self)

    @property
    def VariableExp(self):
        return self.__VariableExp

    @VariableExp.setter
    def VariableExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_VariableDeclaration__VariableExp", None)
        self.__VariableExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL238"):
                    opp_val = getattr(item, "OCL238", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL238", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL238"):
                    opp_val = getattr(item, "OCL238", None)
                    
                    setattr(item, "OCL238", self)
                    

class atlext_OCL_OclExpression(OCL_TypedElement, ATL_LocatedElement):

    def __init__(self, implicitlyCasted: bool, LoopExp: "LoopExp" = None, OperationCallExp: "OperationCallExp" = None, VariableDeclaration152: "VariableDeclaration" = None, IfExp155: "IfExp" = None, Operation: "Operation" = None, OclType: "OclType" = None, IfExp: "IfExp" = None, PropertyCallExp141: "PropertyCallExp" = None, CollectionExp: "CollectionExp" = None, LetExp: "LetExp" = None, IfExp160: "IfExp" = None, Attribute: "Attribute" = None, atlext_OCL_OclExpression: "OCL_atlext_Type" = None):
        self.implicitlyCasted = implicitlyCasted
        self.LoopExp = LoopExp
        self.OperationCallExp = OperationCallExp
        self.VariableDeclaration152 = VariableDeclaration152
        self.IfExp155 = IfExp155
        self.Operation = Operation
        self.OclType = OclType
        self.IfExp = IfExp
        self.PropertyCallExp141 = PropertyCallExp141
        self.CollectionExp = CollectionExp
        self.LetExp = LetExp
        self.IfExp160 = IfExp160
        self.Attribute = Attribute
        self.atlext_OCL_OclExpression = atlext_OCL_OclExpression
        
    @property
    def implicitlyCasted(self) -> bool:
        return self.__implicitlyCasted

    @implicitlyCasted.setter
    def implicitlyCasted(self, implicitlyCasted: bool):
        self.__implicitlyCasted = implicitlyCasted

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL163"):
                opp_val = getattr(old_value, "OCL163", None)
                if opp_val == self:
                    setattr(old_value, "OCL163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL163"):
                opp_val = getattr(value, "OCL163", None)
                setattr(value, "OCL163", self)

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL158"):
                opp_val = getattr(old_value, "OCL158", None)
                if opp_val == self:
                    setattr(old_value, "OCL158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL158"):
                opp_val = getattr(value, "OCL158", None)
                setattr(value, "OCL158", self)

    @property
    def IfExp155(self):
        return self.__IfExp155

    @IfExp155.setter
    def IfExp155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__IfExp155", None)
        self.__IfExp155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL156"):
                opp_val = getattr(old_value, "OCL156", None)
                if opp_val == self:
                    setattr(old_value, "OCL156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL156"):
                opp_val = getattr(value, "OCL156", None)
                setattr(value, "OCL156", self)

    @property
    def CollectionExp(self):
        return self.__CollectionExp

    @CollectionExp.setter
    def CollectionExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__CollectionExp", None)
        self.__CollectionExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL144"):
                opp_val = getattr(old_value, "OCL144", None)
                if opp_val == self:
                    setattr(old_value, "OCL144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL144"):
                opp_val = getattr(value, "OCL144", None)
                setattr(value, "OCL144", self)

    @property
    def OclType(self):
        return self.__OclType

    @OclType.setter
    def OclType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__OclType", None)
        self.__OclType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL137"):
                opp_val = getattr(old_value, "OCL137", None)
                if opp_val == self:
                    setattr(old_value, "OCL137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL137"):
                opp_val = getattr(value, "OCL137", None)
                setattr(value, "OCL137", self)

    @property
    def PropertyCallExp141(self):
        return self.__PropertyCallExp141

    @PropertyCallExp141.setter
    def PropertyCallExp141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__PropertyCallExp141", None)
        self.__PropertyCallExp141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL142"):
                opp_val = getattr(old_value, "OCL142", None)
                if opp_val == self:
                    setattr(old_value, "OCL142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL142"):
                opp_val = getattr(value, "OCL142", None)
                setattr(value, "OCL142", self)

    @property
    def LoopExp(self):
        return self.__LoopExp

    @LoopExp.setter
    def LoopExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__LoopExp", None)
        self.__LoopExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL148"):
                opp_val = getattr(old_value, "OCL148", None)
                if opp_val == self:
                    setattr(old_value, "OCL148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL148"):
                opp_val = getattr(value, "OCL148", None)
                setattr(value, "OCL148", self)

    @property
    def IfExp(self):
        return self.__IfExp

    @IfExp.setter
    def IfExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__IfExp", None)
        self.__IfExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL139"):
                opp_val = getattr(old_value, "OCL139", None)
                if opp_val == self:
                    setattr(old_value, "OCL139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL139"):
                opp_val = getattr(value, "OCL139", None)
                setattr(value, "OCL139", self)

    @property
    def IfExp160(self):
        return self.__IfExp160

    @IfExp160.setter
    def IfExp160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__IfExp160", None)
        self.__IfExp160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL161"):
                opp_val = getattr(old_value, "OCL161", None)
                if opp_val == self:
                    setattr(old_value, "OCL161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL161"):
                opp_val = getattr(value, "OCL161", None)
                setattr(value, "OCL161", self)

    @property
    def atlext_OCL_OclExpression(self):
        return self.__atlext_OCL_OclExpression

    @atlext_OCL_OclExpression.setter
    def atlext_OCL_OclExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__atlext_OCL_OclExpression", None)
        self.__atlext_OCL_OclExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL_atlext_Type"):
                opp_val = getattr(old_value, "OCL_atlext_Type", None)
                if opp_val == self:
                    setattr(old_value, "OCL_atlext_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL_atlext_Type"):
                opp_val = getattr(value, "OCL_atlext_Type", None)
                setattr(value, "OCL_atlext_Type", self)

    @property
    def OperationCallExp(self):
        return self.__OperationCallExp

    @OperationCallExp.setter
    def OperationCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__OperationCallExp", None)
        self.__OperationCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL150"):
                opp_val = getattr(old_value, "OCL150", None)
                if opp_val == self:
                    setattr(old_value, "OCL150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL150"):
                opp_val = getattr(value, "OCL150", None)
                setattr(value, "OCL150", self)

    @property
    def VariableDeclaration152(self):
        return self.__VariableDeclaration152

    @VariableDeclaration152.setter
    def VariableDeclaration152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__VariableDeclaration152", None)
        self.__VariableDeclaration152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL153"):
                opp_val = getattr(old_value, "OCL153", None)
                if opp_val == self:
                    setattr(old_value, "OCL153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL153"):
                opp_val = getattr(value, "OCL153", None)
                setattr(value, "OCL153", self)

    @property
    def LetExp(self):
        return self.__LetExp

    @LetExp.setter
    def LetExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__LetExp", None)
        self.__LetExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL146"):
                opp_val = getattr(old_value, "OCL146", None)
                if opp_val == self:
                    setattr(old_value, "OCL146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL146"):
                opp_val = getattr(value, "OCL146", None)
                setattr(value, "OCL146", self)

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

    def __init__(self, name: str, OCL243: "atlext_OCL_Iterator", OCL148: "atlext_OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class MatchedRule:

    pass
class atlext_ATL_RuleResolutionInfo:

    def __init__(self, status: str, atlext_ATL_RuleResolutionInfo: "MatchedRule" = None, atlext_ATL_RuleResolutionInfo134: set["MatchedRule"] = None):
        self.status = status
        self.atlext_ATL_RuleResolutionInfo = atlext_ATL_RuleResolutionInfo
        self.atlext_ATL_RuleResolutionInfo134 = atlext_ATL_RuleResolutionInfo134 if atlext_ATL_RuleResolutionInfo134 is not None else set()
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def atlext_ATL_RuleResolutionInfo(self):
        return self.__atlext_ATL_RuleResolutionInfo

    @atlext_ATL_RuleResolutionInfo.setter
    def atlext_ATL_RuleResolutionInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_RuleResolutionInfo__atlext_ATL_RuleResolutionInfo", None)
        self.__atlext_ATL_RuleResolutionInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MatchedRule"):
                opp_val = getattr(old_value, "MatchedRule", None)
                if opp_val == self:
                    setattr(old_value, "MatchedRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MatchedRule"):
                opp_val = getattr(value, "MatchedRule", None)
                setattr(value, "MatchedRule", self)

    @property
    def atlext_ATL_RuleResolutionInfo134(self):
        return self.__atlext_ATL_RuleResolutionInfo134

    @atlext_ATL_RuleResolutionInfo134.setter
    def atlext_ATL_RuleResolutionInfo134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_RuleResolutionInfo__atlext_ATL_RuleResolutionInfo134", None)
        self.__atlext_ATL_RuleResolutionInfo134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MatchedRule135"):
                    opp_val = getattr(item, "MatchedRule135", None)
                    
                    if opp_val == self:
                        setattr(item, "MatchedRule135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MatchedRule135"):
                    opp_val = getattr(item, "MatchedRule135", None)
                    
                    setattr(item, "MatchedRule135", self)
                    

class atlext_ATL_CallableParameter:

    def __init__(self, name: str, atlext_ATL_CallableParameter: "ATL_atlext_Type" = None, atlext_ATL_CallableParameter131: "VariableDeclaration" = None):
        self.name = name
        self.atlext_ATL_CallableParameter = atlext_ATL_CallableParameter
        self.atlext_ATL_CallableParameter131 = atlext_ATL_CallableParameter131
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atlext_ATL_CallableParameter131(self):
        return self.__atlext_ATL_CallableParameter131

    @atlext_ATL_CallableParameter131.setter
    def atlext_ATL_CallableParameter131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_CallableParameter__atlext_ATL_CallableParameter131", None)
        self.__atlext_ATL_CallableParameter131 = value
        
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
            if hasattr(old_value, "ATL_atlext_Type129"):
                opp_val = getattr(old_value, "ATL_atlext_Type129", None)
                if opp_val == self:
                    setattr(old_value, "ATL_atlext_Type129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL_atlext_Type129"):
                opp_val = getattr(value, "ATL_atlext_Type129", None)
                setattr(value, "ATL_atlext_Type129", self)

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
class Iterator:

    pass
class Statement:

    pass
class atlext_ATL_ExpressionStat(Statement):

    pass
class atlext_ATL_IfStat(Statement):

    pass
class atlext_ATL_ForStat(Statement):

    pass
class atlext_ATL_BindingStat(Statement):

    def __init__(self, propertyName: str, isAssignment: str, atlext_ATL_BindingStat: "OclExpression" = None, atlext_ATL_BindingStat110: "OclExpression" = None, Statement119: "atlext_ATL_IfStat", Statement116: "atlext_ATL_IfStat", Statement: "atlext_ATL_ActionBlock", Statement127: "atlext_ATL_ForStat"):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.atlext_ATL_BindingStat = atlext_ATL_BindingStat
        self.atlext_ATL_BindingStat110 = atlext_ATL_BindingStat110
        
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

class PatternElement:

    pass
class atlext_ATL_OutPatternElement(PatternElement):

    pass
class atlext_ATL_InPatternElement(PatternElement):

    pass
class VariableDeclaration:

    pass
class atlext_ATL_RuleVariableDeclaration(VariableDeclaration):

    pass
class atlext_OCL_Iterator(VariableDeclaration):

    pass
class atlext_OCL_TuplePart(VariableDeclaration):

    pass
class atlext_OCL_Parameter(VariableDeclaration):

    pass
class atlext_ATL_PatternElement(VariableDeclaration):

    pass
class Binding:

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
class atlext_ATL_LazyRule(ATL_StaticRule, ATL_RuleWithPattern):

    def __init__(self, isUnique: str):
        self.isUnique = isUnique
        
    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

class RuleWithPattern:

    pass
class atlext_ATL_MatchedRule(RuleWithPattern):

    pass
class InPattern:

    pass
class Rule:

    pass
class atlext_ATL_RuleWithPattern(Rule):

    def __init__(self, isAbstract: str, isRefining: str, isNoDefault: str, atlext_ATL_RuleWithPattern: "InPattern" = None, RuleWithPattern: set["RuleWithPattern"] = None, RuleWithPattern43: "RuleWithPattern" = None, ATL98: "atlext_ATL_RuleVariableDeclaration", ATL51: "atlext_ATL_OutPattern", ATL103: "atlext_ATL_ActionBlock"):
        self.isAbstract = isAbstract
        self.isRefining = isRefining
        self.isNoDefault = isNoDefault
        self.atlext_ATL_RuleWithPattern = atlext_ATL_RuleWithPattern
        self.RuleWithPattern = RuleWithPattern if RuleWithPattern is not None else set()
        self.RuleWithPattern43 = RuleWithPattern43
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def isRefining(self) -> str:
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining

    @property
    def isNoDefault(self) -> str:
        return self.__isNoDefault

    @isNoDefault.setter
    def isNoDefault(self, isNoDefault: str):
        self.__isNoDefault = isNoDefault

    @property
    def RuleWithPattern43(self):
        return self.__RuleWithPattern43

    @RuleWithPattern43.setter
    def RuleWithPattern43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_RuleWithPattern__RuleWithPattern43", None)
        self.__RuleWithPattern43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL44"):
                opp_val = getattr(old_value, "ATL44", None)
                if opp_val == self:
                    setattr(old_value, "ATL44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL44"):
                opp_val = getattr(value, "ATL44", None)
                setattr(value, "ATL44", self)

    @property
    def RuleWithPattern(self):
        return self.__RuleWithPattern

    @RuleWithPattern.setter
    def RuleWithPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_RuleWithPattern__RuleWithPattern", None)
        self.__RuleWithPattern = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL41"):
                    opp_val = getattr(item, "ATL41", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL41"):
                    opp_val = getattr(item, "ATL41", None)
                    
                    setattr(item, "ATL41", self)
                    

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

class CallableParameter:

    pass
class OutPatternElement:

    pass
class atlext_ATL_ForEachOutPatternElement(OutPatternElement):

    pass
class atlext_ATL_SimpleOutPatternElement(OutPatternElement):

    pass
class DropPattern:

    pass
class InPatternElement:

    pass
class atlext_ATL_SimpleInPatternElement(InPatternElement):

    pass
class OutPattern:

    pass
class PropertyCallExp:

    pass
class atlext_OCL_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str, OCL: "atlext_ATL_ContextHelper", PropertyCallExp36: "atlext_ATL_Callable", OCL142: "atlext_OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class atlext_OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, OclExpression199: set["OclExpression"] = None, atlext_OCL_OperationCallExp: set["ResolveTempResolution"] = None, OCL: "atlext_ATL_ContextHelper", PropertyCallExp36: "atlext_ATL_Callable", OCL142: "atlext_OCL_OclExpression"):
        self.operationName = operationName
        self.OclExpression199 = OclExpression199 if OclExpression199 is not None else set()
        self.atlext_OCL_OperationCallExp = atlext_OCL_OperationCallExp if atlext_OCL_OperationCallExp is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

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
                    

    @property
    def OclExpression199(self):
        return self.__OclExpression199

    @OclExpression199.setter
    def OclExpression199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OperationCallExp__OclExpression199", None)
        self.__OclExpression199 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL200"):
                    opp_val = getattr(item, "OCL200", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL200", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL200"):
                    opp_val = getattr(item, "OCL200", None)
                    
                    setattr(item, "OCL200", self)
                    

class atlext_OCL_LoopExp(PropertyCallExp):

    pass
class ATL_ModuleCallable:

    pass
class ATL_Helper:

    pass
class atlext_ATL_StaticHelper(ATL_Helper, ATL_ModuleCallable):

    pass
class ATL_atlext_Type:

    pass
class OclFeatureDefinition:

    pass
class Library:

    pass
class atlext_ATL_Callable(ABC):

    pass
class Callable:

    pass
class atlext_ATL_ModuleCallable(Callable):

    pass
class ATL_Rule:

    pass
class atlext_ATL_StaticRule(ATL_ModuleCallable, ATL_Rule):

    pass
class RuleVariableDeclaration:

    pass
class ActionBlock:

    pass
class OclModel:

    pass
class OclExpression:

    pass
class atlext_OCL_TupleExp(OclExpression):

    pass
class atlext_OCL_OclType(OclExpression):

    def __init__(self, name: str, OclContextDefinition: "OclContextDefinition" = None, OclExpression250: "OclExpression" = None, Operation253: "Operation" = None, MapType: "MapType" = None, Attribute258: "Attribute" = None, MapType261: "MapType" = None, CollectionType: "CollectionType" = None, TupleTypeAttribute: "TupleTypeAttribute" = None, VariableDeclaration268: "VariableDeclaration" = None, OCL219: "atlext_OCL_IfExp", OCL204: "atlext_OCL_LoopExp", OclExpression113: "atlext_ATL_IfStat", OclExpression180: "atlext_OCL_MapElement", OclExpression: "atlext_ATL_Query", OCL200: "atlext_OCL_OperationCallExp", OCL216: "atlext_OCL_LetExp", OclExpression124: "atlext_ATL_ForStat", OclExpression49: "atlext_ATL_InPattern", OCL186: "atlext_OCL_PropertyCallExp", OclExpression111: "atlext_ATL_BindingStat", OclExpression84: "atlext_ATL_Binding", OCL314: "atlext_OCL_Operation", OCL225: "atlext_OCL_IfExp", OclExpression78: "atlext_ATL_SimpleOutPatternElement", OCL170: "atlext_OCL_CollectionExp", OclExpression108: "atlext_ATL_BindingStat", OCL222: "atlext_OCL_IfExp", OCL251: "atlext_OCL_OclType", OclExpression106: "atlext_ATL_ExpressionStat", OCL303: "atlext_OCL_Attribute", OclExpression80: "atlext_ATL_ForEachOutPatternElement", OCL231: "atlext_OCL_VariableDeclaration", OclExpression183: "atlext_OCL_MapElement"):
        self.name = name
        self.OclContextDefinition = OclContextDefinition
        self.OclExpression250 = OclExpression250
        self.Operation253 = Operation253
        self.MapType = MapType
        self.Attribute258 = Attribute258
        self.MapType261 = MapType261
        self.CollectionType = CollectionType
        self.TupleTypeAttribute = TupleTypeAttribute
        self.VariableDeclaration268 = VariableDeclaration268
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TupleTypeAttribute(self):
        return self.__TupleTypeAttribute

    @TupleTypeAttribute.setter
    def TupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__TupleTypeAttribute", None)
        self.__TupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL266"):
                opp_val = getattr(old_value, "OCL266", None)
                if opp_val == self:
                    setattr(old_value, "OCL266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL266"):
                opp_val = getattr(value, "OCL266", None)
                setattr(value, "OCL266", self)

    @property
    def OclExpression250(self):
        return self.__OclExpression250

    @OclExpression250.setter
    def OclExpression250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__OclExpression250", None)
        self.__OclExpression250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL251"):
                opp_val = getattr(old_value, "OCL251", None)
                if opp_val == self:
                    setattr(old_value, "OCL251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL251"):
                opp_val = getattr(value, "OCL251", None)
                setattr(value, "OCL251", self)

    @property
    def OclContextDefinition(self):
        return self.__OclContextDefinition

    @OclContextDefinition.setter
    def OclContextDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__OclContextDefinition", None)
        self.__OclContextDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL248"):
                opp_val = getattr(old_value, "OCL248", None)
                if opp_val == self:
                    setattr(old_value, "OCL248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL248"):
                opp_val = getattr(value, "OCL248", None)
                setattr(value, "OCL248", self)

    @property
    def Operation253(self):
        return self.__Operation253

    @Operation253.setter
    def Operation253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__Operation253", None)
        self.__Operation253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL254"):
                opp_val = getattr(old_value, "OCL254", None)
                if opp_val == self:
                    setattr(old_value, "OCL254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL254"):
                opp_val = getattr(value, "OCL254", None)
                setattr(value, "OCL254", self)

    @property
    def VariableDeclaration268(self):
        return self.__VariableDeclaration268

    @VariableDeclaration268.setter
    def VariableDeclaration268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__VariableDeclaration268", None)
        self.__VariableDeclaration268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL269"):
                opp_val = getattr(old_value, "OCL269", None)
                if opp_val == self:
                    setattr(old_value, "OCL269", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL269"):
                opp_val = getattr(value, "OCL269", None)
                setattr(value, "OCL269", self)

    @property
    def MapType261(self):
        return self.__MapType261

    @MapType261.setter
    def MapType261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__MapType261", None)
        self.__MapType261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL262"):
                opp_val = getattr(old_value, "OCL262", None)
                if opp_val == self:
                    setattr(old_value, "OCL262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL262"):
                opp_val = getattr(value, "OCL262", None)
                setattr(value, "OCL262", self)

    @property
    def Attribute258(self):
        return self.__Attribute258

    @Attribute258.setter
    def Attribute258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__Attribute258", None)
        self.__Attribute258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL259"):
                opp_val = getattr(old_value, "OCL259", None)
                if opp_val == self:
                    setattr(old_value, "OCL259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL259"):
                opp_val = getattr(value, "OCL259", None)
                setattr(value, "OCL259", self)

    @property
    def MapType(self):
        return self.__MapType

    @MapType.setter
    def MapType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__MapType", None)
        self.__MapType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL256"):
                opp_val = getattr(old_value, "OCL256", None)
                if opp_val == self:
                    setattr(old_value, "OCL256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL256"):
                opp_val = getattr(value, "OCL256", None)
                setattr(value, "OCL256", self)

    @property
    def CollectionType(self):
        return self.__CollectionType

    @CollectionType.setter
    def CollectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclType__CollectionType", None)
        self.__CollectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL264"):
                opp_val = getattr(old_value, "OCL264", None)
                if opp_val == self:
                    setattr(old_value, "OCL264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL264"):
                opp_val = getattr(value, "OCL264", None)
                setattr(value, "OCL264", self)

class atlext_OCL_IfExp(OclExpression):

    pass
class atlext_OCL_MapExp(OclExpression):

    pass
class atlext_OCL_PrimitiveExp(OclExpression):

    pass
class atlext_OCL_PropertyCallExp(OclExpression):

    def __init__(self, isStaticCall: bool, OclExpression185: "OclExpression" = None, atlext_OCL_PropertyCallExp: "OCL_atlext_EObject" = None, atlext_OCL_PropertyCallExp189: set["OCL_atlext_EObject"] = None, atlext_OCL_PropertyCallExp192: "OCL_atlext_EObject" = None, atlext_OCL_PropertyCallExp195: "Callable" = None, ContextHelper: set["ContextHelper"] = None, OCL219: "atlext_OCL_IfExp", OCL204: "atlext_OCL_LoopExp", OclExpression113: "atlext_ATL_IfStat", OclExpression180: "atlext_OCL_MapElement", OclExpression: "atlext_ATL_Query", OCL200: "atlext_OCL_OperationCallExp", OCL216: "atlext_OCL_LetExp", OclExpression124: "atlext_ATL_ForStat", OclExpression49: "atlext_ATL_InPattern", OCL186: "atlext_OCL_PropertyCallExp", OclExpression111: "atlext_ATL_BindingStat", OclExpression84: "atlext_ATL_Binding", OCL314: "atlext_OCL_Operation", OCL225: "atlext_OCL_IfExp", OclExpression78: "atlext_ATL_SimpleOutPatternElement", OCL170: "atlext_OCL_CollectionExp", OclExpression108: "atlext_ATL_BindingStat", OCL222: "atlext_OCL_IfExp", OCL251: "atlext_OCL_OclType", OclExpression106: "atlext_ATL_ExpressionStat", OCL303: "atlext_OCL_Attribute", OclExpression80: "atlext_ATL_ForEachOutPatternElement", OCL231: "atlext_OCL_VariableDeclaration", OclExpression183: "atlext_OCL_MapElement"):
        self.isStaticCall = isStaticCall
        self.OclExpression185 = OclExpression185
        self.atlext_OCL_PropertyCallExp = atlext_OCL_PropertyCallExp
        self.atlext_OCL_PropertyCallExp189 = atlext_OCL_PropertyCallExp189 if atlext_OCL_PropertyCallExp189 is not None else set()
        self.atlext_OCL_PropertyCallExp192 = atlext_OCL_PropertyCallExp192
        self.atlext_OCL_PropertyCallExp195 = atlext_OCL_PropertyCallExp195
        self.ContextHelper = ContextHelper if ContextHelper is not None else set()
        
    @property
    def isStaticCall(self) -> bool:
        return self.__isStaticCall

    @isStaticCall.setter
    def isStaticCall(self, isStaticCall: bool):
        self.__isStaticCall = isStaticCall

    @property
    def ContextHelper(self):
        return self.__ContextHelper

    @ContextHelper.setter
    def ContextHelper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__ContextHelper", None)
        self.__ContextHelper = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL197"):
                    opp_val = getattr(item, "ATL197", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL197", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL197"):
                    opp_val = getattr(item, "ATL197", None)
                    
                    setattr(item, "ATL197", self)
                    

    @property
    def atlext_OCL_PropertyCallExp195(self):
        return self.__atlext_OCL_PropertyCallExp195

    @atlext_OCL_PropertyCallExp195.setter
    def atlext_OCL_PropertyCallExp195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__atlext_OCL_PropertyCallExp195", None)
        self.__atlext_OCL_PropertyCallExp195 = value
        
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
            if hasattr(old_value, "OCL_atlext_EObject"):
                opp_val = getattr(old_value, "OCL_atlext_EObject", None)
                if opp_val == self:
                    setattr(old_value, "OCL_atlext_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL_atlext_EObject"):
                opp_val = getattr(value, "OCL_atlext_EObject", None)
                setattr(value, "OCL_atlext_EObject", self)

    @property
    def atlext_OCL_PropertyCallExp192(self):
        return self.__atlext_OCL_PropertyCallExp192

    @atlext_OCL_PropertyCallExp192.setter
    def atlext_OCL_PropertyCallExp192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__atlext_OCL_PropertyCallExp192", None)
        self.__atlext_OCL_PropertyCallExp192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL_atlext_EObject193"):
                opp_val = getattr(old_value, "OCL_atlext_EObject193", None)
                if opp_val == self:
                    setattr(old_value, "OCL_atlext_EObject193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL_atlext_EObject193"):
                opp_val = getattr(value, "OCL_atlext_EObject193", None)
                setattr(value, "OCL_atlext_EObject193", self)

    @property
    def OclExpression185(self):
        return self.__OclExpression185

    @OclExpression185.setter
    def OclExpression185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__OclExpression185", None)
        self.__OclExpression185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL186"):
                opp_val = getattr(old_value, "OCL186", None)
                if opp_val == self:
                    setattr(old_value, "OCL186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL186"):
                opp_val = getattr(value, "OCL186", None)
                setattr(value, "OCL186", self)

    @property
    def atlext_OCL_PropertyCallExp189(self):
        return self.__atlext_OCL_PropertyCallExp189

    @atlext_OCL_PropertyCallExp189.setter
    def atlext_OCL_PropertyCallExp189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__atlext_OCL_PropertyCallExp189", None)
        self.__atlext_OCL_PropertyCallExp189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL_atlext_EObject190"):
                    opp_val = getattr(item, "OCL_atlext_EObject190", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL_atlext_EObject190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL_atlext_EObject190"):
                    opp_val = getattr(item, "OCL_atlext_EObject190", None)
                    
                    setattr(item, "OCL_atlext_EObject190", self)
                    

class atlext_OCL_OclUndefinedExp(OclExpression):

    pass
class atlext_OCL_VariableExp(OclExpression):

    pass
class atlext_OCL_SuperExp(OclExpression):

    pass
class atlext_OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OCL219: "atlext_OCL_IfExp", OCL204: "atlext_OCL_LoopExp", OclExpression113: "atlext_ATL_IfStat", OclExpression180: "atlext_OCL_MapElement", OclExpression: "atlext_ATL_Query", OCL200: "atlext_OCL_OperationCallExp", OCL216: "atlext_OCL_LetExp", OclExpression124: "atlext_ATL_ForStat", OclExpression49: "atlext_ATL_InPattern", OCL186: "atlext_OCL_PropertyCallExp", OclExpression111: "atlext_ATL_BindingStat", OclExpression84: "atlext_ATL_Binding", OCL314: "atlext_OCL_Operation", OCL225: "atlext_OCL_IfExp", OclExpression78: "atlext_ATL_SimpleOutPatternElement", OCL170: "atlext_OCL_CollectionExp", OclExpression108: "atlext_ATL_BindingStat", OCL222: "atlext_OCL_IfExp", OCL251: "atlext_OCL_OclType", OclExpression106: "atlext_ATL_ExpressionStat", OCL303: "atlext_OCL_Attribute", OclExpression80: "atlext_ATL_ForEachOutPatternElement", OCL231: "atlext_OCL_VariableDeclaration", OclExpression183: "atlext_OCL_MapElement"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class atlext_OCL_LetExp(OclExpression):

    pass
class atlext_OCL_CollectionExp(OclExpression):

    pass
class atlext_OCL_JavaBody(OclExpression):

    pass
class Helper:

    pass
class atlext_ATL_ContextHelper(Helper):

    pass
class Unit:

    pass
class atlext_ATL_Query(Unit):

    pass
class atlext_ATL_Module(Unit):

    def __init__(self, isRefining: str, atlext_ATL_Module: set["OclModel"] = None, atlext_ATL_Module12: set["OclModel"] = None, atlext_ATL_Module15: set["ModuleElement"] = None, ATL100: "atlext_ATL_LibraryRef"):
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
                    

class atlext_ATL_Library(Unit):

    pass
class LibraryRef:

    pass
class LocatedElement:

    pass
class atlext_OCL_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, OclType274: "OclType" = None, TupleType: "TupleType" = None):
        self.name = name
        self.OclType274 = OclType274
        self.TupleType = TupleType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclType274(self):
        return self.__OclType274

    @OclType274.setter
    def OclType274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_TupleTypeAttribute__OclType274", None)
        self.__OclType274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL275"):
                opp_val = getattr(old_value, "OCL275", None)
                if opp_val == self:
                    setattr(old_value, "OCL275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL275"):
                opp_val = getattr(value, "OCL275", None)
                setattr(value, "OCL275", self)

    @property
    def TupleType(self):
        return self.__TupleType

    @TupleType.setter
    def TupleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_TupleTypeAttribute__TupleType", None)
        self.__TupleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL277"):
                opp_val = getattr(old_value, "OCL277", None)
                if opp_val == self:
                    setattr(old_value, "OCL277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL277"):
                opp_val = getattr(value, "OCL277", None)
                setattr(value, "OCL277", self)

class atlext_OCL_OclContextDefinition(LocatedElement):

    pass
class atlext_ATL_InPattern(LocatedElement):

    pass
class atlext_ATL_Statement(LocatedElement):

    pass
class atlext_ATL_Binding(LocatedElement):

    def __init__(self, propertyName: str, isAssignment: str, atlext_ATL_Binding: "OclExpression" = None, OutPatternElement86: "OutPatternElement" = None, atlext_ATL_Binding89: "ATL_atlext_EObject" = None, atlext_ATL_Binding92: "ATL_atlext_Type" = None, atlext_ATL_Binding95: set["RuleResolutionInfo"] = None):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.atlext_ATL_Binding = atlext_ATL_Binding
        self.OutPatternElement86 = OutPatternElement86
        self.atlext_ATL_Binding89 = atlext_ATL_Binding89
        self.atlext_ATL_Binding92 = atlext_ATL_Binding92
        self.atlext_ATL_Binding95 = atlext_ATL_Binding95 if atlext_ATL_Binding95 is not None else set()
        
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
    def OutPatternElement86(self):
        return self.__OutPatternElement86

    @OutPatternElement86.setter
    def OutPatternElement86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Binding__OutPatternElement86", None)
        self.__OutPatternElement86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL87"):
                opp_val = getattr(old_value, "ATL87", None)
                if opp_val == self:
                    setattr(old_value, "ATL87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL87"):
                opp_val = getattr(value, "ATL87", None)
                setattr(value, "ATL87", self)

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
            if hasattr(old_value, "OclExpression84"):
                opp_val = getattr(old_value, "OclExpression84", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression84"):
                opp_val = getattr(value, "OclExpression84", None)
                setattr(value, "OclExpression84", self)

    @property
    def atlext_ATL_Binding92(self):
        return self.__atlext_ATL_Binding92

    @atlext_ATL_Binding92.setter
    def atlext_ATL_Binding92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Binding__atlext_ATL_Binding92", None)
        self.__atlext_ATL_Binding92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL_atlext_Type93"):
                opp_val = getattr(old_value, "ATL_atlext_Type93", None)
                if opp_val == self:
                    setattr(old_value, "ATL_atlext_Type93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL_atlext_Type93"):
                opp_val = getattr(value, "ATL_atlext_Type93", None)
                setattr(value, "ATL_atlext_Type93", self)

    @property
    def atlext_ATL_Binding95(self):
        return self.__atlext_ATL_Binding95

    @atlext_ATL_Binding95.setter
    def atlext_ATL_Binding95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Binding__atlext_ATL_Binding95", None)
        self.__atlext_ATL_Binding95 = value if value is not None else set()
        
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
    def atlext_ATL_Binding89(self):
        return self.__atlext_ATL_Binding89

    @atlext_ATL_Binding89.setter
    def atlext_ATL_Binding89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Binding__atlext_ATL_Binding89", None)
        self.__atlext_ATL_Binding89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL_atlext_EObject90"):
                opp_val = getattr(old_value, "ATL_atlext_EObject90", None)
                if opp_val == self:
                    setattr(old_value, "ATL_atlext_EObject90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL_atlext_EObject90"):
                opp_val = getattr(value, "ATL_atlext_EObject90", None)
                setattr(value, "ATL_atlext_EObject90", self)

class atlext_OCL_OclModel(LocatedElement):

    def __init__(self, name: str, OclModel316: "OclModel" = None, OclModelElement: set["OclModelElement"] = None, OclModel321: set["OclModel"] = None):
        self.name = name
        self.OclModel316 = OclModel316
        self.OclModelElement = OclModelElement if OclModelElement is not None else set()
        self.OclModel321 = OclModel321 if OclModel321 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclModelElement(self):
        return self.__OclModelElement

    @OclModelElement.setter
    def OclModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclModel__OclModelElement", None)
        self.__OclModelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL319"):
                    opp_val = getattr(item, "OCL319", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL319", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL319"):
                    opp_val = getattr(item, "OCL319", None)
                    
                    setattr(item, "OCL319", self)
                    

    @property
    def OclModel321(self):
        return self.__OclModel321

    @OclModel321.setter
    def OclModel321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclModel__OclModel321", None)
        self.__OclModel321 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL322"):
                    opp_val = getattr(item, "OCL322", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL322", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL322"):
                    opp_val = getattr(item, "OCL322", None)
                    
                    setattr(item, "OCL322", self)
                    

    @property
    def OclModel316(self):
        return self.__OclModel316

    @OclModel316.setter
    def OclModel316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclModel__OclModel316", None)
        self.__OclModel316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL317"):
                opp_val = getattr(old_value, "OCL317", None)
                if opp_val == self:
                    setattr(old_value, "OCL317", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL317"):
                opp_val = getattr(value, "OCL317", None)
                setattr(value, "OCL317", self)

class atlext_OCL_OclFeatureDefinition(LocatedElement):

    pass
class atlext_ATL_LibraryRef(LocatedElement):

    def __init__(self, name: str, Unit: "Unit" = None):
        self.name = name
        self.Unit = Unit
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Unit(self):
        return self.__Unit

    @Unit.setter
    def Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_LibraryRef__Unit", None)
        self.__Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL100"):
                opp_val = getattr(old_value, "ATL100", None)
                if opp_val == self:
                    setattr(old_value, "ATL100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL100"):
                opp_val = getattr(value, "ATL100", None)
                setattr(value, "ATL100", self)

class atlext_OCL_OclFeature(LocatedElement):

    pass
class atlext_OCL_MapElement(LocatedElement):

    pass
class atlext_ATL_ActionBlock(LocatedElement):

    pass
class atlext_ATL_DropPattern(LocatedElement):

    pass
class atlext_ATL_OutPattern(LocatedElement):

    pass
class atlext_ATL_Unit(LocatedElement):

    def __init__(self, name: str, LibraryRef: set["LibraryRef"] = None):
        self.name = name
        self.LibraryRef = LibraryRef if LibraryRef is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LibraryRef(self):
        return self.__LibraryRef

    @LibraryRef.setter
    def LibraryRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Unit__LibraryRef", None)
        self.__LibraryRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL"):
                    opp_val = getattr(item, "ATL", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL"):
                    opp_val = getattr(item, "ATL", None)
                    
                    setattr(item, "ATL", self)
                    

class StringToStringMap:

    pass
class Query:

    pass
class ATL_Callable:

    pass
class ATL_ModuleElement:

    pass
class atlext_ATL_Helper(ATL_ModuleElement, ATL_Callable):

    def __init__(self, hasContext: bool, isAttribute: bool, Query: "Query" = None, Library: "Library" = None, atlext_ATL_Helper: "OclFeatureDefinition" = None, atlext_ATL_Helper22: "ATL_atlext_Type" = None, atlext_ATL_Helper24: "ATL_atlext_Type" = None):
        self.hasContext = hasContext
        self.isAttribute = isAttribute
        self.Query = Query
        self.Library = Library
        self.atlext_ATL_Helper = atlext_ATL_Helper
        self.atlext_ATL_Helper22 = atlext_ATL_Helper22
        self.atlext_ATL_Helper24 = atlext_ATL_Helper24
        
    @property
    def hasContext(self) -> bool:
        return self.__hasContext

    @hasContext.setter
    def hasContext(self, hasContext: bool):
        self.__hasContext = hasContext

    @property
    def isAttribute(self) -> bool:
        return self.__isAttribute

    @isAttribute.setter
    def isAttribute(self, isAttribute: bool):
        self.__isAttribute = isAttribute

    @property
    def Query(self):
        return self.__Query

    @Query.setter
    def Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__Query", None)
        self.__Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL17"):
                opp_val = getattr(old_value, "ATL17", None)
                if opp_val == self:
                    setattr(old_value, "ATL17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL17"):
                opp_val = getattr(value, "ATL17", None)
                setattr(value, "ATL17", self)

    @property
    def atlext_ATL_Helper24(self):
        return self.__atlext_ATL_Helper24

    @atlext_ATL_Helper24.setter
    def atlext_ATL_Helper24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__atlext_ATL_Helper24", None)
        self.__atlext_ATL_Helper24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL_atlext_Type25"):
                opp_val = getattr(old_value, "ATL_atlext_Type25", None)
                if opp_val == self:
                    setattr(old_value, "ATL_atlext_Type25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL_atlext_Type25"):
                opp_val = getattr(value, "ATL_atlext_Type25", None)
                setattr(value, "ATL_atlext_Type25", self)

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
    def atlext_ATL_Helper22(self):
        return self.__atlext_ATL_Helper22

    @atlext_ATL_Helper22.setter
    def atlext_ATL_Helper22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__atlext_ATL_Helper22", None)
        self.__atlext_ATL_Helper22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL_atlext_Type"):
                opp_val = getattr(old_value, "ATL_atlext_Type", None)
                if opp_val == self:
                    setattr(old_value, "ATL_atlext_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL_atlext_Type"):
                opp_val = getattr(value, "ATL_atlext_Type", None)
                setattr(value, "ATL_atlext_Type", self)

    @property
    def Library(self):
        return self.__Library

    @Library.setter
    def Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__Library", None)
        self.__Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL19"):
                opp_val = getattr(old_value, "ATL19", None)
                if opp_val == self:
                    setattr(old_value, "ATL19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL19"):
                opp_val = getattr(value, "ATL19", None)
                setattr(value, "ATL19", self)

class atlext_ATL_ModuleElement(LocatedElement):

    pass
class ModuleElement:

    pass
class atlext_ATL_Rule(ModuleElement):

    def __init__(self, name: str, ActionBlock: "ActionBlock" = None, RuleVariableDeclaration: set["RuleVariableDeclaration"] = None, OutPattern: "OutPattern" = None, ModuleElement: "atlext_ATL_Module"):
        self.name = name
        self.ActionBlock = ActionBlock
        self.RuleVariableDeclaration = RuleVariableDeclaration if RuleVariableDeclaration is not None else set()
        self.OutPattern = OutPattern
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ActionBlock(self):
        return self.__ActionBlock

    @ActionBlock.setter
    def ActionBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Rule__ActionBlock", None)
        self.__ActionBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL32"):
                opp_val = getattr(old_value, "ATL32", None)
                if opp_val == self:
                    setattr(old_value, "ATL32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL32"):
                opp_val = getattr(value, "ATL32", None)
                setattr(value, "ATL32", self)

    @property
    def OutPattern(self):
        return self.__OutPattern

    @OutPattern.setter
    def OutPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Rule__OutPattern", None)
        self.__OutPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL30"):
                opp_val = getattr(old_value, "ATL30", None)
                if opp_val == self:
                    setattr(old_value, "ATL30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL30"):
                opp_val = getattr(value, "ATL30", None)
                setattr(value, "ATL30", self)

    @property
    def RuleVariableDeclaration(self):
        return self.__RuleVariableDeclaration

    @RuleVariableDeclaration.setter
    def RuleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Rule__RuleVariableDeclaration", None)
        self.__RuleVariableDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL34"):
                    opp_val = getattr(item, "ATL34", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL34"):
                    opp_val = getattr(item, "ATL34", None)
                    
                    setattr(item, "ATL34", self)
                    

class ATL_atlext_EObject:

    pass
class atlext_ATL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str, fileLocation: str, fileObject: str, atlext_ATL_LocatedElement: set["ATL_atlext_EObject"] = None, atlext_ATL_LocatedElement2: set["StringToStringMap"] = None):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        self.fileLocation = fileLocation
        self.fileObject = fileObject
        self.atlext_ATL_LocatedElement = atlext_ATL_LocatedElement if atlext_ATL_LocatedElement is not None else set()
        self.atlext_ATL_LocatedElement2 = atlext_ATL_LocatedElement2 if atlext_ATL_LocatedElement2 is not None else set()
        
    @property
    def fileObject(self) -> str:
        return self.__fileObject

    @fileObject.setter
    def fileObject(self, fileObject: str):
        self.__fileObject = fileObject

    @property
    def fileLocation(self) -> str:
        return self.__fileLocation

    @fileLocation.setter
    def fileLocation(self, fileLocation: str):
        self.__fileLocation = fileLocation

    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def commentsBefore(self) -> str:
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore

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
                if hasattr(item, "ATL_atlext_EObject"):
                    opp_val = getattr(item, "ATL_atlext_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL_atlext_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL_atlext_EObject"):
                    opp_val = getattr(item, "ATL_atlext_EObject", None)
                    
                    setattr(item, "ATL_atlext_EObject", self)
                    

    @property
    def atlext_ATL_LocatedElement2(self):
        return self.__atlext_ATL_LocatedElement2

    @atlext_ATL_LocatedElement2.setter
    def atlext_ATL_LocatedElement2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_LocatedElement__atlext_ATL_LocatedElement2", None)
        self.__atlext_ATL_LocatedElement2 = value if value is not None else set()
        
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
                    
