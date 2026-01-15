from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class NavigationRole(Enum):
    ITERATOR = "ITERATOR"
    ACCUMULATOR = "ACCUMULATOR"
    EXPRESSION = "EXPRESSION"


############################################
# Definition of Classes
############################################

class essentialoclcs_Type:

    pass
class BinaryOperatorCS:

    pass
class essentialoclcs_NavigationOperatorCS(BinaryOperatorCS):

    pass
class essentialoclcs_PathNameCS:

    pass
class AbstractNameExpCS:

    pass
class essentialoclcs_NamedExpCS(AbstractNameExpCS):

    pass
class essentialoclcs_NameExpCS(AbstractNameExpCS):

    def __init__(self, atPre: bool, essentialoclcs_NameExpCS: "essentialoclcs_PathNameCS" = None, essentialoclcs_NameExpCS49: "essentialoclcs_NamedExpCS" = None):
        self.atPre = atPre
        self.essentialoclcs_NameExpCS = essentialoclcs_NameExpCS
        self.essentialoclcs_NameExpCS49 = essentialoclcs_NameExpCS49
        
    @property
    def atPre(self) -> bool:
        return self.__atPre

    @atPre.setter
    def atPre(self, atPre: bool):
        self.__atPre = atPre

    @property
    def essentialoclcs_NameExpCS(self):
        return self.__essentialoclcs_NameExpCS

    @essentialoclcs_NameExpCS.setter
    def essentialoclcs_NameExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_NameExpCS__essentialoclcs_NameExpCS", None)
        self.__essentialoclcs_NameExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_PathNameCS"):
                opp_val = getattr(old_value, "essentialoclcs_PathNameCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_PathNameCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_PathNameCS"):
                opp_val = getattr(value, "essentialoclcs_PathNameCS", None)
                setattr(value, "essentialoclcs_PathNameCS", self)

    @property
    def essentialoclcs_NameExpCS49(self):
        return self.__essentialoclcs_NameExpCS49

    @essentialoclcs_NameExpCS49.setter
    def essentialoclcs_NameExpCS49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_NameExpCS__essentialoclcs_NameExpCS49", None)
        self.__essentialoclcs_NameExpCS49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_NamedExpCS"):
                opp_val = getattr(old_value, "essentialoclcs_NamedExpCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_NamedExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_NamedExpCS"):
                opp_val = getattr(value, "essentialoclcs_NamedExpCS", None)
                setattr(value, "essentialoclcs_NamedExpCS", self)

class VariableCS:

    pass
class essentialoclcs_TupleLiteralPartCS(VariableCS):

    pass
class SpecificationCS:

    pass
class essentialoclcs_ExpSpecificationCS(SpecificationCS):

    pass
class RootCS:

    pass
class NamedElementCS:

    pass
class essentialoclcs_VariableCS(NamedElementCS):

    pass
class essentialoclcs_ContextCS(NamedElementCS, RootCS):

    pass
class essentialoclcs_Property:

    pass
class NamedExpCS:

    pass
class essentialoclcs_InvocationExpCS(NamedExpCS):

    pass
class essentialoclcs_IndexExpCS(NamedExpCS):

    def __init__(self, atPre: bool, essentialoclcs_IndexExpCS: set["essentialoclcs_ExpCS"] = None, essentialoclcs_IndexExpCS35: set["essentialoclcs_ExpCS"] = None):
        self.atPre = atPre
        self.essentialoclcs_IndexExpCS = essentialoclcs_IndexExpCS if essentialoclcs_IndexExpCS is not None else set()
        self.essentialoclcs_IndexExpCS35 = essentialoclcs_IndexExpCS35 if essentialoclcs_IndexExpCS35 is not None else set()
        
    @property
    def atPre(self) -> bool:
        return self.__atPre

    @atPre.setter
    def atPre(self, atPre: bool):
        self.__atPre = atPre

    @property
    def essentialoclcs_IndexExpCS(self):
        return self.__essentialoclcs_IndexExpCS

    @essentialoclcs_IndexExpCS.setter
    def essentialoclcs_IndexExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_IndexExpCS__essentialoclcs_IndexExpCS", None)
        self.__essentialoclcs_IndexExpCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "essentialoclcs_ExpCS33"):
                    opp_val = getattr(item, "essentialoclcs_ExpCS33", None)
                    
                    if opp_val == self:
                        setattr(item, "essentialoclcs_ExpCS33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "essentialoclcs_ExpCS33"):
                    opp_val = getattr(item, "essentialoclcs_ExpCS33", None)
                    
                    setattr(item, "essentialoclcs_ExpCS33", self)
                    

    @property
    def essentialoclcs_IndexExpCS35(self):
        return self.__essentialoclcs_IndexExpCS35

    @essentialoclcs_IndexExpCS35.setter
    def essentialoclcs_IndexExpCS35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_IndexExpCS__essentialoclcs_IndexExpCS35", None)
        self.__essentialoclcs_IndexExpCS35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "essentialoclcs_ExpCS36"):
                    opp_val = getattr(item, "essentialoclcs_ExpCS36", None)
                    
                    if opp_val == self:
                        setattr(item, "essentialoclcs_ExpCS36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "essentialoclcs_ExpCS36"):
                    opp_val = getattr(item, "essentialoclcs_ExpCS36", None)
                    
                    setattr(item, "essentialoclcs_ExpCS36", self)
                    

class essentialoclcs_ConstructorExpCS(NamedExpCS):

    def __init__(self, value: str, essentialoclcs_ConstructorExpCS: set["essentialoclcs_ConstructorPartCS"] = None):
        self.value = value
        self.essentialoclcs_ConstructorExpCS = essentialoclcs_ConstructorExpCS if essentialoclcs_ConstructorExpCS is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def essentialoclcs_ConstructorExpCS(self):
        return self.__essentialoclcs_ConstructorExpCS

    @essentialoclcs_ConstructorExpCS.setter
    def essentialoclcs_ConstructorExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ConstructorExpCS__essentialoclcs_ConstructorExpCS", None)
        self.__essentialoclcs_ConstructorExpCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "essentialoclcs_ConstructorPartCS"):
                    opp_val = getattr(item, "essentialoclcs_ConstructorPartCS", None)
                    
                    if opp_val == self:
                        setattr(item, "essentialoclcs_ConstructorPartCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "essentialoclcs_ConstructorPartCS"):
                    opp_val = getattr(item, "essentialoclcs_ConstructorPartCS", None)
                    
                    setattr(item, "essentialoclcs_ConstructorPartCS", self)
                    

class ModelElementCS:

    pass
class essentialoclcs_NavigatingArgCS(ModelElementCS):

    def __init__(self, role: str, prefix: str, NavigatingArgCS: "essentialoclcs_InvocationExpCS" = None, argument: "essentialoclcs_InvocationExpCS" = None, essentialoclcs_NavigatingArgCS: "essentialoclcs_ExpCS" = None, essentialoclcs_NavigatingArgCS54: "essentialoclcs_TypedRefCS" = None, essentialoclcs_NavigatingArgCS57: "essentialoclcs_ExpCS" = None):
        self.role = role
        self.prefix = prefix
        self.NavigatingArgCS = NavigatingArgCS
        self.argument = argument
        self.essentialoclcs_NavigatingArgCS = essentialoclcs_NavigatingArgCS
        self.essentialoclcs_NavigatingArgCS54 = essentialoclcs_NavigatingArgCS54
        self.essentialoclcs_NavigatingArgCS57 = essentialoclcs_NavigatingArgCS57
        
    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def essentialoclcs_NavigatingArgCS57(self):
        return self.__essentialoclcs_NavigatingArgCS57

    @essentialoclcs_NavigatingArgCS57.setter
    def essentialoclcs_NavigatingArgCS57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_NavigatingArgCS__essentialoclcs_NavigatingArgCS57", None)
        self.__essentialoclcs_NavigatingArgCS57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS58"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS58", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS58"):
                opp_val = getattr(value, "essentialoclcs_ExpCS58", None)
                setattr(value, "essentialoclcs_ExpCS58", self)

    @property
    def argument(self):
        return self.__argument

    @argument.setter
    def argument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_NavigatingArgCS__argument", None)
        self.__argument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InvocationExpCS"):
                opp_val = getattr(old_value, "InvocationExpCS", None)
                if opp_val == self:
                    setattr(old_value, "InvocationExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InvocationExpCS"):
                opp_val = getattr(value, "InvocationExpCS", None)
                setattr(value, "InvocationExpCS", self)

    @property
    def essentialoclcs_NavigatingArgCS54(self):
        return self.__essentialoclcs_NavigatingArgCS54

    @essentialoclcs_NavigatingArgCS54.setter
    def essentialoclcs_NavigatingArgCS54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_NavigatingArgCS__essentialoclcs_NavigatingArgCS54", None)
        self.__essentialoclcs_NavigatingArgCS54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_TypedRefCS55"):
                opp_val = getattr(old_value, "essentialoclcs_TypedRefCS55", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_TypedRefCS55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_TypedRefCS55"):
                opp_val = getattr(value, "essentialoclcs_TypedRefCS55", None)
                setattr(value, "essentialoclcs_TypedRefCS55", self)

    @property
    def NavigatingArgCS(self):
        return self.__NavigatingArgCS

    @NavigatingArgCS.setter
    def NavigatingArgCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_NavigatingArgCS__NavigatingArgCS", None)
        self.__NavigatingArgCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "navigatingExp"):
                opp_val = getattr(old_value, "navigatingExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "navigatingExp"):
                opp_val = getattr(value, "navigatingExp", None)
                if opp_val is None:
                    setattr(value, "navigatingExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def essentialoclcs_NavigatingArgCS(self):
        return self.__essentialoclcs_NavigatingArgCS

    @essentialoclcs_NavigatingArgCS.setter
    def essentialoclcs_NavigatingArgCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_NavigatingArgCS__essentialoclcs_NavigatingArgCS", None)
        self.__essentialoclcs_NavigatingArgCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS52"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS52", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS52"):
                opp_val = getattr(value, "essentialoclcs_ExpCS52", None)
                setattr(value, "essentialoclcs_ExpCS52", self)

class essentialoclcs_CollectionLiteralPartCS(ModelElementCS):

    pass
class LiteralExpCS:

    pass
class essentialoclcs_TypeLiteralExpCS(LiteralExpCS):

    pass
class essentialoclcs_PrimitiveLiteralExpCS(LiteralExpCS):

    pass
class essentialoclcs_TupleLiteralExpCS(LiteralExpCS):

    pass
class essentialoclcs_CollectionLiteralExpCS(LiteralExpCS):

    pass
class PrimitiveLiteralExpCS:

    pass
class essentialoclcs_InvalidLiteralExpCS(PrimitiveLiteralExpCS):

    pass
class essentialoclcs_NumberLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class essentialoclcs_NullLiteralExpCS(PrimitiveLiteralExpCS):

    pass
class essentialoclcs_StringLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class essentialoclcs_UnlimitedNaturalLiteralExpCS(PrimitiveLiteralExpCS):

    pass
class essentialoclcs_BooleanLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class essentialoclcs_ExpCS(ModelElementCS):

    pass
class OperatorCS:

    pass
class essentialoclcs_UnaryOperatorCS(OperatorCS):

    pass
class essentialoclcs_BinaryOperatorCS(OperatorCS):

    pass
class ExpCS:

    pass
class essentialoclcs_OperatorCS(NamedElementCS, ExpCS):

    pass
class essentialoclcs_SelfExpCS(ExpCS):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class essentialoclcs_LiteralExpCS(ExpCS):

    pass
class essentialoclcs_IfExpCS(ExpCS):

    pass
class essentialoclcs_LetExpCS(ExpCS):

    pass
class essentialoclcs_PrefixExpCS(ExpCS):

    pass
class essentialoclcs_NestedExpCS(ExpCS):

    pass
class essentialoclcs_LetVariableCS(VariableCS, ExpCS):

    pass
class essentialoclcs_InfixExpCS(ExpCS):

    pass
class essentialoclcs_AbstractNameExpCS(ExpCS):

    def __init__(self):
        
    def getPathName(self) -> str:
        # TODO: Implement getPathName method
        pass

    def getNamedElement(self) -> str:
        # TODO: Implement getNamedElement method
        pass

    def getNameExp(self) -> str:
        # TODO: Implement getNameExp method
        pass

class essentialoclcs_TypedRefCS:

    pass
class Nameable:

    pass
class essentialoclcs_ConstructorPartCS(ModelElementCS, Nameable):

    pass
class TypedRefCS:

    pass
class essentialoclcs_TypeNameExpCS(TypedRefCS):

    pass
class essentialoclcs_CollectionTypeCS(TypedRefCS, Nameable):

    def __init__(self, name: str, essentialoclcs_CollectionTypeCS: "essentialoclcs_CollectionLiteralExpCS" = None, essentialoclcs_CollectionTypeCS11: "essentialoclcs_TypedRefCS" = None):
        self.name = name
        self.essentialoclcs_CollectionTypeCS = essentialoclcs_CollectionTypeCS
        self.essentialoclcs_CollectionTypeCS11 = essentialoclcs_CollectionTypeCS11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def essentialoclcs_CollectionTypeCS11(self):
        return self.__essentialoclcs_CollectionTypeCS11

    @essentialoclcs_CollectionTypeCS11.setter
    def essentialoclcs_CollectionTypeCS11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_CollectionTypeCS__essentialoclcs_CollectionTypeCS11", None)
        self.__essentialoclcs_CollectionTypeCS11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_TypedRefCS"):
                opp_val = getattr(old_value, "essentialoclcs_TypedRefCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_TypedRefCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_TypedRefCS"):
                opp_val = getattr(value, "essentialoclcs_TypedRefCS", None)
                setattr(value, "essentialoclcs_TypedRefCS", self)

    @property
    def essentialoclcs_CollectionTypeCS(self):
        return self.__essentialoclcs_CollectionTypeCS

    @essentialoclcs_CollectionTypeCS.setter
    def essentialoclcs_CollectionTypeCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_CollectionTypeCS__essentialoclcs_CollectionTypeCS", None)
        self.__essentialoclcs_CollectionTypeCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_CollectionLiteralExpCS"):
                opp_val = getattr(old_value, "essentialoclcs_CollectionLiteralExpCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_CollectionLiteralExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_CollectionLiteralExpCS"):
                opp_val = getattr(value, "essentialoclcs_CollectionLiteralExpCS", None)
                setattr(value, "essentialoclcs_CollectionLiteralExpCS", self)
