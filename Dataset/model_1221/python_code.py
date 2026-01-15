from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ocl_ecore_StringLiteralExp:

    pass
class ocl_ecore_StateExp:

    pass
class ocl_ecore_VariableExp:

    pass
class ocl_ecore_Variable:

    pass
class ocl_ecore_UnspecifiedValueExp:

    pass
class ocl_ecore_TypeExp:

    pass
class ocl_ecore_TupleLiteralPart:

    pass
class ocl_ecore_TupleLiteralExp:

    pass
class ocl_ecore_LetExp:

    pass
class ocl_ecore_IteratorExp:

    pass
class ocl_ecore_RealLiteralExp:

    pass
class ocl_ecore_IterateExp:

    pass
class ocl_ecore_PropertyCallExp:

    pass
class ocl_ecore_InvalidLiteralExp:

    pass
class ocl_ecore_PrimitiveLiteralExp(ABC):

    pass
class ocl_ecore_UnlimitedNaturalLiteralExp:

    pass
class ocl_ecore_OperationCallExp:

    pass
class ocl_ecore_IntegerLiteralExp:

    pass
class ocl_ecore_OCLExpression(ABC):

    pass
class ocl_ecore_NumericLiteralExp(ABC):

    pass
class ocl_ecore_NullLiteralExp:

    pass
class ocl_ecore_NavigationCallExp(ABC):

    pass
class ocl_ecore_MessageExp:

    pass
class ocl_ecore_LoopExp(ABC):

    pass
class ocl_ecore_LiteralExp(ABC):

    pass
class ocl_ecore_CallExp(ABC):

    pass
class ocl_ecore_BooleanLiteralExp:

    pass
class ocl_ecore_AssociationClassCallExp:

    pass
class ocl_ecore_ExpressionInOCL:

    pass
class ecore_ocl_EClass:

    pass
class ocl_ecore_SendSignalAction:

    pass
class ecore_ocl_EModelElement:

    pass
class ocl_ecore_IfExp:

    pass
class ocl_ecore_FeatureCallExp(ABC):

    pass
class ENamedElement:

    pass
class ocl_ecore_Constraint(ENamedElement):

    def __init__(self, stereotype: str, ocl_ecore_Constraint: set["ecore_ocl_EModelElement"] = None):
        self.stereotype = stereotype
        self.ocl_ecore_Constraint = ocl_ecore_Constraint if ocl_ecore_Constraint is not None else set()
        
    @property
    def stereotype(self) -> str:
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, stereotype: str):
        self.__stereotype = stereotype

    @property
    def ocl_ecore_Constraint(self):
        return self.__ocl_ecore_Constraint

    @ocl_ecore_Constraint.setter
    def ocl_ecore_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_ecore_Constraint__ocl_ecore_Constraint", None)
        self.__ocl_ecore_Constraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_ocl_EModelElement"):
                    opp_val = getattr(item, "ecore_ocl_EModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_ocl_EModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_ocl_EModelElement"):
                    opp_val = getattr(item, "ecore_ocl_EModelElement", None)
                    
                    setattr(item, "ecore_ocl_EModelElement", self)
                    

class ocl_ecore_EnumLiteralExp:

    pass
class ecore_ocl_EOperation:

    pass
class ocl_ecore_CallOperationAction:

    pass
class ocl_ecore_CollectionRange:

    pass
class ocl_ecore_VoidType:

    pass
class ocl_ecore_CollectionLiteralPart(ABC):

    pass
class ocl_ecore_CollectionLiteralExp:

    pass
class ocl_ecore_TypeType:

    pass
class ocl_ecore_CollectionItem:

    pass
class ocl_ecore_TupleType:

    pass
class ocl_ecore_TemplateParameterType:

    pass
class ocl_ecore_SetType:

    pass
class ocl_ecore_SequenceType:

    pass
class ocl_ecore_PrimitiveType:

    pass
class ocl_ecore_OrderedSetType:

    pass
class ocl_ecore_MessageType:

    pass
class ocl_ecore_InvalidType:

    pass
class types_ElementType:

    pass
class EClass:

    pass
class ocl_ecore_ElementType(types_ElementType, EClass):

    pass
class ocl_ecore_BagType:

    pass
class ocl_ecore_AnyType:

    pass
class ocl_ecore_CollectionType:

    pass