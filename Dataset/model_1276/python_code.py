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

class essentialoclcs_Variable:

    pass
class essentialoclcs_Property:

    pass
class essentialoclcs_TypeRefCS:

    pass
class essentialoclcs_Operation:

    pass
class VariableExpCS:

    pass
class PropertyCallExpCS:

    pass
class OperationCallExpCS:

    pass
class VariableCS:

    pass
class essentialoclcs_TupleLiteralPartCS(VariableCS):

    pass
class IterateCallExpCS:

    pass
class ShadowExpCS:

    pass
class AssociationClassCallExpCS:

    pass
class IterationCallExpCS:

    pass
class essentialoclcs_NameExpCS(IterationCallExpCS, ShadowExpCS, AssociationClassCallExpCS, OperationCallExpCS, PropertyCallExpCS, IterateCallExpCS, VariableExpCS):

    pass
class essentialoclcs_IterateCallExpCS(IterationCallExpCS):

    pass
class OperatorExpCS:

    pass
class essentialoclcs_PrefixExpCS(OperatorExpCS):

    pass
class essentialoclcs_InfixExpCS(OperatorExpCS):

    pass
class essentialoclcs_Iteration:

    pass
class SpecificationCS:

    pass
class essentialoclcs_ExpSpecificationCS(SpecificationCS):

    pass
class essentialoclcs_Precedence:

    pass
class ContextLessElementCS:

    pass
class TypedRefCS:

    pass
class essentialoclcs_TypeNameExpCS(TypedRefCS):

    pass
class essentialoclcs_CollectionPatternCS(TypedRefCS):

    def __init__(self, restVariableName: str, essentialoclcs_CollectionPatternCS: set["essentialoclcs_PatternExpCS"] = None, essentialoclcs_CollectionPatternCS27: "essentialoclcs_ExpCS" = None, essentialoclcs_CollectionPatternCS30: "essentialoclcs_CollectionTypeCS" = None):
        self.restVariableName = restVariableName
        self.essentialoclcs_CollectionPatternCS = essentialoclcs_CollectionPatternCS if essentialoclcs_CollectionPatternCS is not None else set()
        self.essentialoclcs_CollectionPatternCS27 = essentialoclcs_CollectionPatternCS27
        self.essentialoclcs_CollectionPatternCS30 = essentialoclcs_CollectionPatternCS30
        
    @property
    def restVariableName(self) -> str:
        return self.__restVariableName

    @restVariableName.setter
    def restVariableName(self, restVariableName: str):
        self.__restVariableName = restVariableName

    @property
    def essentialoclcs_CollectionPatternCS(self):
        return self.__essentialoclcs_CollectionPatternCS

    @essentialoclcs_CollectionPatternCS.setter
    def essentialoclcs_CollectionPatternCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_CollectionPatternCS__essentialoclcs_CollectionPatternCS", None)
        self.__essentialoclcs_CollectionPatternCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "essentialoclcs_PatternExpCS"):
                    opp_val = getattr(item, "essentialoclcs_PatternExpCS", None)
                    
                    if opp_val == self:
                        setattr(item, "essentialoclcs_PatternExpCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "essentialoclcs_PatternExpCS"):
                    opp_val = getattr(item, "essentialoclcs_PatternExpCS", None)
                    
                    setattr(item, "essentialoclcs_PatternExpCS", self)
                    

    @property
    def essentialoclcs_CollectionPatternCS27(self):
        return self.__essentialoclcs_CollectionPatternCS27

    @essentialoclcs_CollectionPatternCS27.setter
    def essentialoclcs_CollectionPatternCS27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_CollectionPatternCS__essentialoclcs_CollectionPatternCS27", None)
        self.__essentialoclcs_CollectionPatternCS27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS28"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS28", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS28"):
                opp_val = getattr(value, "essentialoclcs_ExpCS28", None)
                setattr(value, "essentialoclcs_ExpCS28", self)

    @property
    def essentialoclcs_CollectionPatternCS30(self):
        return self.__essentialoclcs_CollectionPatternCS30

    @essentialoclcs_CollectionPatternCS30.setter
    def essentialoclcs_CollectionPatternCS30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_CollectionPatternCS__essentialoclcs_CollectionPatternCS30", None)
        self.__essentialoclcs_CollectionPatternCS30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_CollectionTypeCS31"):
                opp_val = getattr(old_value, "essentialoclcs_CollectionTypeCS31", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_CollectionTypeCS31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_CollectionTypeCS31"):
                opp_val = getattr(value, "essentialoclcs_CollectionTypeCS31", None)
                setattr(value, "essentialoclcs_CollectionTypeCS31", self)

class ModelElementCS:

    pass
class essentialoclcs_MapLiteralPartCS(ModelElementCS):

    pass
class essentialoclcs_NavigatingArgCS(ModelElementCS):

    def __init__(self, prefix: str, role: str, essentialoclcs_NavigatingArgCS: "essentialoclcs_ExpCS" = None, essentialoclcs_NavigatingArgCS107: "essentialoclcs_ExpCS" = None, essentialoclcs_NavigatingArgCS110: "essentialoclcs_TypedRefCS" = None, ownedArguments: "essentialoclcs_RoundBracketedClauseCS" = None, NavigatingArgCS: "essentialoclcs_RoundBracketedClauseCS" = None):
        self.prefix = prefix
        self.role = role
        self.essentialoclcs_NavigatingArgCS = essentialoclcs_NavigatingArgCS
        self.essentialoclcs_NavigatingArgCS107 = essentialoclcs_NavigatingArgCS107
        self.essentialoclcs_NavigatingArgCS110 = essentialoclcs_NavigatingArgCS110
        self.ownedArguments = ownedArguments
        self.NavigatingArgCS = NavigatingArgCS
        
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
    def essentialoclcs_NavigatingArgCS(self):
        return self.__essentialoclcs_NavigatingArgCS

    @essentialoclcs_NavigatingArgCS.setter
    def essentialoclcs_NavigatingArgCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_NavigatingArgCS__essentialoclcs_NavigatingArgCS", None)
        self.__essentialoclcs_NavigatingArgCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS105"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS105", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS105"):
                opp_val = getattr(value, "essentialoclcs_ExpCS105", None)
                setattr(value, "essentialoclcs_ExpCS105", self)

    @property
    def essentialoclcs_NavigatingArgCS110(self):
        return self.__essentialoclcs_NavigatingArgCS110

    @essentialoclcs_NavigatingArgCS110.setter
    def essentialoclcs_NavigatingArgCS110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_NavigatingArgCS__essentialoclcs_NavigatingArgCS110", None)
        self.__essentialoclcs_NavigatingArgCS110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_TypedRefCS111"):
                opp_val = getattr(old_value, "essentialoclcs_TypedRefCS111", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_TypedRefCS111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_TypedRefCS111"):
                opp_val = getattr(value, "essentialoclcs_TypedRefCS111", None)
                setattr(value, "essentialoclcs_TypedRefCS111", self)

    @property
    def essentialoclcs_NavigatingArgCS107(self):
        return self.__essentialoclcs_NavigatingArgCS107

    @essentialoclcs_NavigatingArgCS107.setter
    def essentialoclcs_NavigatingArgCS107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_NavigatingArgCS__essentialoclcs_NavigatingArgCS107", None)
        self.__essentialoclcs_NavigatingArgCS107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS108"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS108", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS108"):
                opp_val = getattr(value, "essentialoclcs_ExpCS108", None)
                setattr(value, "essentialoclcs_ExpCS108", self)

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
            if hasattr(old_value, "owningRoundBracketedClause"):
                opp_val = getattr(old_value, "owningRoundBracketedClause", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningRoundBracketedClause"):
                opp_val = getattr(value, "owningRoundBracketedClause", None)
                if opp_val is None:
                    setattr(value, "owningRoundBracketedClause", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedArguments(self):
        return self.__ownedArguments

    @ownedArguments.setter
    def ownedArguments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_NavigatingArgCS__ownedArguments", None)
        self.__ownedArguments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoundBracketedClauseCS113"):
                opp_val = getattr(old_value, "RoundBracketedClauseCS113", None)
                if opp_val == self:
                    setattr(old_value, "RoundBracketedClauseCS113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoundBracketedClauseCS113"):
                opp_val = getattr(value, "RoundBracketedClauseCS113", None)
                setattr(value, "RoundBracketedClauseCS113", self)

class essentialoclcs_CollectionLiteralPartCS(ModelElementCS):

    pass
class LiteralExpCS:

    pass
class essentialoclcs_PrimitiveLiteralExpCS(LiteralExpCS):

    pass
class essentialoclcs_LambdaLiteralExpCS(LiteralExpCS):

    pass
class essentialoclcs_MapLiteralExpCS(LiteralExpCS):

    pass
class essentialoclcs_TupleLiteralExpCS(LiteralExpCS):

    pass
class essentialoclcs_TypeLiteralExpCS(LiteralExpCS):

    pass
class essentialoclcs_CollectionLiteralExpCS(LiteralExpCS):

    pass
class essentialoclcs_ExpCS(ModelElementCS):

    def __init__(self, hasError: bool, essentialoclcs_ExpCS: "essentialoclcs_CallExpCS" = None, essentialoclcs_ExpCS15: "essentialoclcs_CallExpCS" = None, essentialoclcs_ExpCS21: "essentialoclcs_CollectionLiteralPartCS" = None, essentialoclcs_ExpCS24: "essentialoclcs_CollectionLiteralPartCS" = None, essentialoclcs_ExpCS28: "essentialoclcs_CollectionPatternCS" = None, essentialoclcs_ExpCS35: "essentialoclcs_ContextCS" = None, essentialoclcs_ExpCS53: "essentialoclcs_Precedence" = None, essentialoclcs_ExpCS55: "essentialoclcs_ExpSpecificationCS" = None, essentialoclcs_ExpCS40: "essentialoclcs_ExpCS" = None, essentialoclcs_ExpCS38: "essentialoclcs_ExpCS" = None, essentialoclcs_ExpCS43: "essentialoclcs_ExpCS" = None, essentialoclcs_ExpCS41: "essentialoclcs_ExpCS" = None, essentialoclcs_ExpCS45: "essentialoclcs_OperatorExpCS" = None, essentialoclcs_ExpCS48: "essentialoclcs_ExpCS" = None, essentialoclcs_ExpCS46: "essentialoclcs_ExpCS" = None, essentialoclcs_ExpCS51: "essentialoclcs_ExpCS" = None, essentialoclcs_ExpCS49: "essentialoclcs_ExpCS" = None, essentialoclcs_ExpCS83: "essentialoclcs_LambdaLiteralExpCS" = None, essentialoclcs_ExpCS57: "essentialoclcs_IfExpCS" = None, essentialoclcs_ExpCS60: "essentialoclcs_IfExpCS" = None, essentialoclcs_ExpCS65: "essentialoclcs_IfExpCS" = None, essentialoclcs_ExpCS68: "essentialoclcs_IfThenExpCS" = None, essentialoclcs_ExpCS71: "essentialoclcs_IfThenExpCS" = None, essentialoclcs_ExpCS73: "essentialoclcs_InfixExpCS" = None, essentialoclcs_ExpCS76: "essentialoclcs_InfixExpCS" = None, essentialoclcs_ExpCS85: "essentialoclcs_LetExpCS" = None, essentialoclcs_ExpCS94: "essentialoclcs_MapLiteralPartCS" = None, essentialoclcs_ExpCS97: "essentialoclcs_MapLiteralPartCS" = None, essentialoclcs_ExpCS119: "essentialoclcs_OperatorExpCS" = None, essentialoclcs_ExpCS122: "essentialoclcs_OperatorExpCS" = None, essentialoclcs_ExpCS105: "essentialoclcs_NavigatingArgCS" = None, essentialoclcs_ExpCS108: "essentialoclcs_NavigatingArgCS" = None, essentialoclcs_ExpCS115: "essentialoclcs_NestedExpCS" = None, essentialoclcs_ExpCS134: "essentialoclcs_ShadowPartCS" = None, essentialoclcs_ExpCS163: "essentialoclcs_VariableCS" = None, essentialoclcs_ExpCS141: "essentialoclcs_SquareBracketedClauseCS" = None, essentialoclcs_ExpCS160: "essentialoclcs_TypeNameExpCS" = None):
        self.hasError = hasError
        self.essentialoclcs_ExpCS = essentialoclcs_ExpCS
        self.essentialoclcs_ExpCS15 = essentialoclcs_ExpCS15
        self.essentialoclcs_ExpCS21 = essentialoclcs_ExpCS21
        self.essentialoclcs_ExpCS24 = essentialoclcs_ExpCS24
        self.essentialoclcs_ExpCS28 = essentialoclcs_ExpCS28
        self.essentialoclcs_ExpCS35 = essentialoclcs_ExpCS35
        self.essentialoclcs_ExpCS53 = essentialoclcs_ExpCS53
        self.essentialoclcs_ExpCS55 = essentialoclcs_ExpCS55
        self.essentialoclcs_ExpCS40 = essentialoclcs_ExpCS40
        self.essentialoclcs_ExpCS38 = essentialoclcs_ExpCS38
        self.essentialoclcs_ExpCS43 = essentialoclcs_ExpCS43
        self.essentialoclcs_ExpCS41 = essentialoclcs_ExpCS41
        self.essentialoclcs_ExpCS45 = essentialoclcs_ExpCS45
        self.essentialoclcs_ExpCS48 = essentialoclcs_ExpCS48
        self.essentialoclcs_ExpCS46 = essentialoclcs_ExpCS46
        self.essentialoclcs_ExpCS51 = essentialoclcs_ExpCS51
        self.essentialoclcs_ExpCS49 = essentialoclcs_ExpCS49
        self.essentialoclcs_ExpCS83 = essentialoclcs_ExpCS83
        self.essentialoclcs_ExpCS57 = essentialoclcs_ExpCS57
        self.essentialoclcs_ExpCS60 = essentialoclcs_ExpCS60
        self.essentialoclcs_ExpCS65 = essentialoclcs_ExpCS65
        self.essentialoclcs_ExpCS68 = essentialoclcs_ExpCS68
        self.essentialoclcs_ExpCS71 = essentialoclcs_ExpCS71
        self.essentialoclcs_ExpCS73 = essentialoclcs_ExpCS73
        self.essentialoclcs_ExpCS76 = essentialoclcs_ExpCS76
        self.essentialoclcs_ExpCS85 = essentialoclcs_ExpCS85
        self.essentialoclcs_ExpCS94 = essentialoclcs_ExpCS94
        self.essentialoclcs_ExpCS97 = essentialoclcs_ExpCS97
        self.essentialoclcs_ExpCS119 = essentialoclcs_ExpCS119
        self.essentialoclcs_ExpCS122 = essentialoclcs_ExpCS122
        self.essentialoclcs_ExpCS105 = essentialoclcs_ExpCS105
        self.essentialoclcs_ExpCS108 = essentialoclcs_ExpCS108
        self.essentialoclcs_ExpCS115 = essentialoclcs_ExpCS115
        self.essentialoclcs_ExpCS134 = essentialoclcs_ExpCS134
        self.essentialoclcs_ExpCS163 = essentialoclcs_ExpCS163
        self.essentialoclcs_ExpCS141 = essentialoclcs_ExpCS141
        self.essentialoclcs_ExpCS160 = essentialoclcs_ExpCS160
        
    @property
    def hasError(self) -> bool:
        return self.__hasError

    @hasError.setter
    def hasError(self, hasError: bool):
        self.__hasError = hasError

    @property
    def essentialoclcs_ExpCS48(self):
        return self.__essentialoclcs_ExpCS48

    @essentialoclcs_ExpCS48.setter
    def essentialoclcs_ExpCS48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS48", None)
        self.__essentialoclcs_ExpCS48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS46"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS46", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS46"):
                opp_val = getattr(value, "essentialoclcs_ExpCS46", None)
                setattr(value, "essentialoclcs_ExpCS46", self)

    @property
    def essentialoclcs_ExpCS108(self):
        return self.__essentialoclcs_ExpCS108

    @essentialoclcs_ExpCS108.setter
    def essentialoclcs_ExpCS108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS108", None)
        self.__essentialoclcs_ExpCS108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_NavigatingArgCS107"):
                opp_val = getattr(old_value, "essentialoclcs_NavigatingArgCS107", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_NavigatingArgCS107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_NavigatingArgCS107"):
                opp_val = getattr(value, "essentialoclcs_NavigatingArgCS107", None)
                setattr(value, "essentialoclcs_NavigatingArgCS107", self)

    @property
    def essentialoclcs_ExpCS83(self):
        return self.__essentialoclcs_ExpCS83

    @essentialoclcs_ExpCS83.setter
    def essentialoclcs_ExpCS83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS83", None)
        self.__essentialoclcs_ExpCS83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_LambdaLiteralExpCS"):
                opp_val = getattr(old_value, "essentialoclcs_LambdaLiteralExpCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_LambdaLiteralExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_LambdaLiteralExpCS"):
                opp_val = getattr(value, "essentialoclcs_LambdaLiteralExpCS", None)
                setattr(value, "essentialoclcs_LambdaLiteralExpCS", self)

    @property
    def essentialoclcs_ExpCS49(self):
        return self.__essentialoclcs_ExpCS49

    @essentialoclcs_ExpCS49.setter
    def essentialoclcs_ExpCS49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS49", None)
        self.__essentialoclcs_ExpCS49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS51"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS51", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS51"):
                opp_val = getattr(value, "essentialoclcs_ExpCS51", None)
                setattr(value, "essentialoclcs_ExpCS51", self)

    @property
    def essentialoclcs_ExpCS41(self):
        return self.__essentialoclcs_ExpCS41

    @essentialoclcs_ExpCS41.setter
    def essentialoclcs_ExpCS41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS41", None)
        self.__essentialoclcs_ExpCS41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS43"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS43", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS43"):
                opp_val = getattr(value, "essentialoclcs_ExpCS43", None)
                setattr(value, "essentialoclcs_ExpCS43", self)

    @property
    def essentialoclcs_ExpCS35(self):
        return self.__essentialoclcs_ExpCS35

    @essentialoclcs_ExpCS35.setter
    def essentialoclcs_ExpCS35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS35", None)
        self.__essentialoclcs_ExpCS35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ContextCS"):
                opp_val = getattr(old_value, "essentialoclcs_ContextCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ContextCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ContextCS"):
                opp_val = getattr(value, "essentialoclcs_ContextCS", None)
                setattr(value, "essentialoclcs_ContextCS", self)

    @property
    def essentialoclcs_ExpCS24(self):
        return self.__essentialoclcs_ExpCS24

    @essentialoclcs_ExpCS24.setter
    def essentialoclcs_ExpCS24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS24", None)
        self.__essentialoclcs_ExpCS24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_CollectionLiteralPartCS23"):
                opp_val = getattr(old_value, "essentialoclcs_CollectionLiteralPartCS23", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_CollectionLiteralPartCS23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_CollectionLiteralPartCS23"):
                opp_val = getattr(value, "essentialoclcs_CollectionLiteralPartCS23", None)
                setattr(value, "essentialoclcs_CollectionLiteralPartCS23", self)

    @property
    def essentialoclcs_ExpCS46(self):
        return self.__essentialoclcs_ExpCS46

    @essentialoclcs_ExpCS46.setter
    def essentialoclcs_ExpCS46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS46", None)
        self.__essentialoclcs_ExpCS46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS48"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS48", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS48"):
                opp_val = getattr(value, "essentialoclcs_ExpCS48", None)
                setattr(value, "essentialoclcs_ExpCS48", self)

    @property
    def essentialoclcs_ExpCS65(self):
        return self.__essentialoclcs_ExpCS65

    @essentialoclcs_ExpCS65.setter
    def essentialoclcs_ExpCS65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS65", None)
        self.__essentialoclcs_ExpCS65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_IfExpCS64"):
                opp_val = getattr(old_value, "essentialoclcs_IfExpCS64", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_IfExpCS64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_IfExpCS64"):
                opp_val = getattr(value, "essentialoclcs_IfExpCS64", None)
                setattr(value, "essentialoclcs_IfExpCS64", self)

    @property
    def essentialoclcs_ExpCS85(self):
        return self.__essentialoclcs_ExpCS85

    @essentialoclcs_ExpCS85.setter
    def essentialoclcs_ExpCS85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS85", None)
        self.__essentialoclcs_ExpCS85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_LetExpCS"):
                opp_val = getattr(old_value, "essentialoclcs_LetExpCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_LetExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_LetExpCS"):
                opp_val = getattr(value, "essentialoclcs_LetExpCS", None)
                setattr(value, "essentialoclcs_LetExpCS", self)

    @property
    def essentialoclcs_ExpCS40(self):
        return self.__essentialoclcs_ExpCS40

    @essentialoclcs_ExpCS40.setter
    def essentialoclcs_ExpCS40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS40", None)
        self.__essentialoclcs_ExpCS40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS38"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS38", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS38"):
                opp_val = getattr(value, "essentialoclcs_ExpCS38", None)
                setattr(value, "essentialoclcs_ExpCS38", self)

    @property
    def essentialoclcs_ExpCS53(self):
        return self.__essentialoclcs_ExpCS53

    @essentialoclcs_ExpCS53.setter
    def essentialoclcs_ExpCS53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS53", None)
        self.__essentialoclcs_ExpCS53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_Precedence"):
                opp_val = getattr(old_value, "essentialoclcs_Precedence", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_Precedence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_Precedence"):
                opp_val = getattr(value, "essentialoclcs_Precedence", None)
                setattr(value, "essentialoclcs_Precedence", self)

    @property
    def essentialoclcs_ExpCS134(self):
        return self.__essentialoclcs_ExpCS134

    @essentialoclcs_ExpCS134.setter
    def essentialoclcs_ExpCS134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS134", None)
        self.__essentialoclcs_ExpCS134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ShadowPartCS133"):
                opp_val = getattr(old_value, "essentialoclcs_ShadowPartCS133", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ShadowPartCS133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ShadowPartCS133"):
                opp_val = getattr(value, "essentialoclcs_ShadowPartCS133", None)
                setattr(value, "essentialoclcs_ShadowPartCS133", self)

    @property
    def essentialoclcs_ExpCS119(self):
        return self.__essentialoclcs_ExpCS119

    @essentialoclcs_ExpCS119.setter
    def essentialoclcs_ExpCS119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS119", None)
        self.__essentialoclcs_ExpCS119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_OperatorExpCS118"):
                opp_val = getattr(old_value, "essentialoclcs_OperatorExpCS118", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_OperatorExpCS118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_OperatorExpCS118"):
                opp_val = getattr(value, "essentialoclcs_OperatorExpCS118", None)
                setattr(value, "essentialoclcs_OperatorExpCS118", self)

    @property
    def essentialoclcs_ExpCS57(self):
        return self.__essentialoclcs_ExpCS57

    @essentialoclcs_ExpCS57.setter
    def essentialoclcs_ExpCS57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS57", None)
        self.__essentialoclcs_ExpCS57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_IfExpCS"):
                opp_val = getattr(old_value, "essentialoclcs_IfExpCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_IfExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_IfExpCS"):
                opp_val = getattr(value, "essentialoclcs_IfExpCS", None)
                setattr(value, "essentialoclcs_IfExpCS", self)

    @property
    def essentialoclcs_ExpCS21(self):
        return self.__essentialoclcs_ExpCS21

    @essentialoclcs_ExpCS21.setter
    def essentialoclcs_ExpCS21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS21", None)
        self.__essentialoclcs_ExpCS21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_CollectionLiteralPartCS20"):
                opp_val = getattr(old_value, "essentialoclcs_CollectionLiteralPartCS20", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_CollectionLiteralPartCS20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_CollectionLiteralPartCS20"):
                opp_val = getattr(value, "essentialoclcs_CollectionLiteralPartCS20", None)
                setattr(value, "essentialoclcs_CollectionLiteralPartCS20", self)

    @property
    def essentialoclcs_ExpCS28(self):
        return self.__essentialoclcs_ExpCS28

    @essentialoclcs_ExpCS28.setter
    def essentialoclcs_ExpCS28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS28", None)
        self.__essentialoclcs_ExpCS28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_CollectionPatternCS27"):
                opp_val = getattr(old_value, "essentialoclcs_CollectionPatternCS27", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_CollectionPatternCS27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_CollectionPatternCS27"):
                opp_val = getattr(value, "essentialoclcs_CollectionPatternCS27", None)
                setattr(value, "essentialoclcs_CollectionPatternCS27", self)

    @property
    def essentialoclcs_ExpCS45(self):
        return self.__essentialoclcs_ExpCS45

    @essentialoclcs_ExpCS45.setter
    def essentialoclcs_ExpCS45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS45", None)
        self.__essentialoclcs_ExpCS45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_OperatorExpCS"):
                opp_val = getattr(old_value, "essentialoclcs_OperatorExpCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_OperatorExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_OperatorExpCS"):
                opp_val = getattr(value, "essentialoclcs_OperatorExpCS", None)
                setattr(value, "essentialoclcs_OperatorExpCS", self)

    @property
    def essentialoclcs_ExpCS68(self):
        return self.__essentialoclcs_ExpCS68

    @essentialoclcs_ExpCS68.setter
    def essentialoclcs_ExpCS68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS68", None)
        self.__essentialoclcs_ExpCS68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_IfThenExpCS67"):
                opp_val = getattr(old_value, "essentialoclcs_IfThenExpCS67", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_IfThenExpCS67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_IfThenExpCS67"):
                opp_val = getattr(value, "essentialoclcs_IfThenExpCS67", None)
                setattr(value, "essentialoclcs_IfThenExpCS67", self)

    @property
    def essentialoclcs_ExpCS15(self):
        return self.__essentialoclcs_ExpCS15

    @essentialoclcs_ExpCS15.setter
    def essentialoclcs_ExpCS15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS15", None)
        self.__essentialoclcs_ExpCS15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_CallExpCS14"):
                opp_val = getattr(old_value, "essentialoclcs_CallExpCS14", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_CallExpCS14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_CallExpCS14"):
                opp_val = getattr(value, "essentialoclcs_CallExpCS14", None)
                setattr(value, "essentialoclcs_CallExpCS14", self)

    @property
    def essentialoclcs_ExpCS55(self):
        return self.__essentialoclcs_ExpCS55

    @essentialoclcs_ExpCS55.setter
    def essentialoclcs_ExpCS55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS55", None)
        self.__essentialoclcs_ExpCS55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpSpecificationCS"):
                opp_val = getattr(old_value, "essentialoclcs_ExpSpecificationCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpSpecificationCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpSpecificationCS"):
                opp_val = getattr(value, "essentialoclcs_ExpSpecificationCS", None)
                setattr(value, "essentialoclcs_ExpSpecificationCS", self)

    @property
    def essentialoclcs_ExpCS94(self):
        return self.__essentialoclcs_ExpCS94

    @essentialoclcs_ExpCS94.setter
    def essentialoclcs_ExpCS94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS94", None)
        self.__essentialoclcs_ExpCS94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_MapLiteralPartCS93"):
                opp_val = getattr(old_value, "essentialoclcs_MapLiteralPartCS93", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_MapLiteralPartCS93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_MapLiteralPartCS93"):
                opp_val = getattr(value, "essentialoclcs_MapLiteralPartCS93", None)
                setattr(value, "essentialoclcs_MapLiteralPartCS93", self)

    @property
    def essentialoclcs_ExpCS141(self):
        return self.__essentialoclcs_ExpCS141

    @essentialoclcs_ExpCS141.setter
    def essentialoclcs_ExpCS141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS141", None)
        self.__essentialoclcs_ExpCS141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_SquareBracketedClauseCS"):
                opp_val = getattr(old_value, "essentialoclcs_SquareBracketedClauseCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_SquareBracketedClauseCS"):
                opp_val = getattr(value, "essentialoclcs_SquareBracketedClauseCS", None)
                if opp_val is None:
                    setattr(value, "essentialoclcs_SquareBracketedClauseCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def essentialoclcs_ExpCS43(self):
        return self.__essentialoclcs_ExpCS43

    @essentialoclcs_ExpCS43.setter
    def essentialoclcs_ExpCS43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS43", None)
        self.__essentialoclcs_ExpCS43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS41"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS41", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS41"):
                opp_val = getattr(value, "essentialoclcs_ExpCS41", None)
                setattr(value, "essentialoclcs_ExpCS41", self)

    @property
    def essentialoclcs_ExpCS163(self):
        return self.__essentialoclcs_ExpCS163

    @essentialoclcs_ExpCS163.setter
    def essentialoclcs_ExpCS163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS163", None)
        self.__essentialoclcs_ExpCS163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_VariableCS162"):
                opp_val = getattr(old_value, "essentialoclcs_VariableCS162", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_VariableCS162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_VariableCS162"):
                opp_val = getattr(value, "essentialoclcs_VariableCS162", None)
                setattr(value, "essentialoclcs_VariableCS162", self)

    @property
    def essentialoclcs_ExpCS(self):
        return self.__essentialoclcs_ExpCS

    @essentialoclcs_ExpCS.setter
    def essentialoclcs_ExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS", None)
        self.__essentialoclcs_ExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_CallExpCS"):
                opp_val = getattr(old_value, "essentialoclcs_CallExpCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_CallExpCS"):
                opp_val = getattr(value, "essentialoclcs_CallExpCS", None)
                if opp_val is None:
                    setattr(value, "essentialoclcs_CallExpCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def essentialoclcs_ExpCS105(self):
        return self.__essentialoclcs_ExpCS105

    @essentialoclcs_ExpCS105.setter
    def essentialoclcs_ExpCS105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS105", None)
        self.__essentialoclcs_ExpCS105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_NavigatingArgCS"):
                opp_val = getattr(old_value, "essentialoclcs_NavigatingArgCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_NavigatingArgCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_NavigatingArgCS"):
                opp_val = getattr(value, "essentialoclcs_NavigatingArgCS", None)
                setattr(value, "essentialoclcs_NavigatingArgCS", self)

    @property
    def essentialoclcs_ExpCS51(self):
        return self.__essentialoclcs_ExpCS51

    @essentialoclcs_ExpCS51.setter
    def essentialoclcs_ExpCS51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS51", None)
        self.__essentialoclcs_ExpCS51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS49"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS49", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS49"):
                opp_val = getattr(value, "essentialoclcs_ExpCS49", None)
                setattr(value, "essentialoclcs_ExpCS49", self)

    @property
    def essentialoclcs_ExpCS38(self):
        return self.__essentialoclcs_ExpCS38

    @essentialoclcs_ExpCS38.setter
    def essentialoclcs_ExpCS38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS38", None)
        self.__essentialoclcs_ExpCS38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS40"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS40", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS40"):
                opp_val = getattr(value, "essentialoclcs_ExpCS40", None)
                setattr(value, "essentialoclcs_ExpCS40", self)

    @property
    def essentialoclcs_ExpCS160(self):
        return self.__essentialoclcs_ExpCS160

    @essentialoclcs_ExpCS160.setter
    def essentialoclcs_ExpCS160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS160", None)
        self.__essentialoclcs_ExpCS160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_TypeNameExpCS159"):
                opp_val = getattr(old_value, "essentialoclcs_TypeNameExpCS159", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_TypeNameExpCS159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_TypeNameExpCS159"):
                opp_val = getattr(value, "essentialoclcs_TypeNameExpCS159", None)
                setattr(value, "essentialoclcs_TypeNameExpCS159", self)

    @property
    def essentialoclcs_ExpCS73(self):
        return self.__essentialoclcs_ExpCS73

    @essentialoclcs_ExpCS73.setter
    def essentialoclcs_ExpCS73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS73", None)
        self.__essentialoclcs_ExpCS73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_InfixExpCS"):
                opp_val = getattr(old_value, "essentialoclcs_InfixExpCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_InfixExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_InfixExpCS"):
                opp_val = getattr(value, "essentialoclcs_InfixExpCS", None)
                setattr(value, "essentialoclcs_InfixExpCS", self)

    @property
    def essentialoclcs_ExpCS60(self):
        return self.__essentialoclcs_ExpCS60

    @essentialoclcs_ExpCS60.setter
    def essentialoclcs_ExpCS60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS60", None)
        self.__essentialoclcs_ExpCS60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_IfExpCS59"):
                opp_val = getattr(old_value, "essentialoclcs_IfExpCS59", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_IfExpCS59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_IfExpCS59"):
                opp_val = getattr(value, "essentialoclcs_IfExpCS59", None)
                setattr(value, "essentialoclcs_IfExpCS59", self)

    @property
    def essentialoclcs_ExpCS115(self):
        return self.__essentialoclcs_ExpCS115

    @essentialoclcs_ExpCS115.setter
    def essentialoclcs_ExpCS115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS115", None)
        self.__essentialoclcs_ExpCS115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_NestedExpCS"):
                opp_val = getattr(old_value, "essentialoclcs_NestedExpCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_NestedExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_NestedExpCS"):
                opp_val = getattr(value, "essentialoclcs_NestedExpCS", None)
                setattr(value, "essentialoclcs_NestedExpCS", self)

    @property
    def essentialoclcs_ExpCS71(self):
        return self.__essentialoclcs_ExpCS71

    @essentialoclcs_ExpCS71.setter
    def essentialoclcs_ExpCS71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS71", None)
        self.__essentialoclcs_ExpCS71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_IfThenExpCS70"):
                opp_val = getattr(old_value, "essentialoclcs_IfThenExpCS70", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_IfThenExpCS70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_IfThenExpCS70"):
                opp_val = getattr(value, "essentialoclcs_IfThenExpCS70", None)
                setattr(value, "essentialoclcs_IfThenExpCS70", self)

    @property
    def essentialoclcs_ExpCS97(self):
        return self.__essentialoclcs_ExpCS97

    @essentialoclcs_ExpCS97.setter
    def essentialoclcs_ExpCS97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS97", None)
        self.__essentialoclcs_ExpCS97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_MapLiteralPartCS96"):
                opp_val = getattr(old_value, "essentialoclcs_MapLiteralPartCS96", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_MapLiteralPartCS96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_MapLiteralPartCS96"):
                opp_val = getattr(value, "essentialoclcs_MapLiteralPartCS96", None)
                setattr(value, "essentialoclcs_MapLiteralPartCS96", self)

    @property
    def essentialoclcs_ExpCS76(self):
        return self.__essentialoclcs_ExpCS76

    @essentialoclcs_ExpCS76.setter
    def essentialoclcs_ExpCS76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS76", None)
        self.__essentialoclcs_ExpCS76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_InfixExpCS75"):
                opp_val = getattr(old_value, "essentialoclcs_InfixExpCS75", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_InfixExpCS75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_InfixExpCS75"):
                opp_val = getattr(value, "essentialoclcs_InfixExpCS75", None)
                setattr(value, "essentialoclcs_InfixExpCS75", self)

    @property
    def essentialoclcs_ExpCS122(self):
        return self.__essentialoclcs_ExpCS122

    @essentialoclcs_ExpCS122.setter
    def essentialoclcs_ExpCS122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ExpCS__essentialoclcs_ExpCS122", None)
        self.__essentialoclcs_ExpCS122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_OperatorExpCS121"):
                opp_val = getattr(old_value, "essentialoclcs_OperatorExpCS121", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_OperatorExpCS121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_OperatorExpCS121"):
                opp_val = getattr(value, "essentialoclcs_OperatorExpCS121", None)
                setattr(value, "essentialoclcs_OperatorExpCS121", self)

    def isLocalRightAncestorOf(self, csExp: ExpCS) -> bool:
        # TODO: Implement isLocalRightAncestorOf method
        pass

    def isLocalLeftAncestorOf(self, csExp: ExpCS) -> bool:
        # TODO: Implement isLocalLeftAncestorOf method
        pass

class AbstractNameExpCS:

    pass
class essentialoclcs_VariableExpCS(AbstractNameExpCS):

    pass
class essentialoclcs_ShadowExpCS(AbstractNameExpCS):

    def __init__(self, value: str, essentialoclcs_ShadowExpCS: set["essentialoclcs_ShadowPartCS"] = None, essentialoclcs_ShadowExpCS131: "essentialoclcs_TypeNameExpCS" = None):
        self.value = value
        self.essentialoclcs_ShadowExpCS = essentialoclcs_ShadowExpCS if essentialoclcs_ShadowExpCS is not None else set()
        self.essentialoclcs_ShadowExpCS131 = essentialoclcs_ShadowExpCS131
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def essentialoclcs_ShadowExpCS(self):
        return self.__essentialoclcs_ShadowExpCS

    @essentialoclcs_ShadowExpCS.setter
    def essentialoclcs_ShadowExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ShadowExpCS__essentialoclcs_ShadowExpCS", None)
        self.__essentialoclcs_ShadowExpCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "essentialoclcs_ShadowPartCS"):
                    opp_val = getattr(item, "essentialoclcs_ShadowPartCS", None)
                    
                    if opp_val == self:
                        setattr(item, "essentialoclcs_ShadowPartCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "essentialoclcs_ShadowPartCS"):
                    opp_val = getattr(item, "essentialoclcs_ShadowPartCS", None)
                    
                    setattr(item, "essentialoclcs_ShadowPartCS", self)
                    

    @property
    def essentialoclcs_ShadowExpCS131(self):
        return self.__essentialoclcs_ShadowExpCS131

    @essentialoclcs_ShadowExpCS131.setter
    def essentialoclcs_ShadowExpCS131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_ShadowExpCS__essentialoclcs_ShadowExpCS131", None)
        self.__essentialoclcs_ShadowExpCS131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_TypeNameExpCS"):
                opp_val = getattr(old_value, "essentialoclcs_TypeNameExpCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_TypeNameExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_TypeNameExpCS"):
                opp_val = getattr(value, "essentialoclcs_TypeNameExpCS", None)
                setattr(value, "essentialoclcs_TypeNameExpCS", self)

class essentialoclcs_CallExpCS(AbstractNameExpCS):

    pass
class RootCS:

    pass
class NamedElementCS:

    pass
class essentialoclcs_VariableCS(NamedElementCS):

    pass
class essentialoclcs_ContextCS(NamedElementCS, RootCS):

    pass
class essentialoclcs_TypedRefCS:

    pass
class Nameable:

    pass
class essentialoclcs_ShadowPartCS(Nameable, ModelElementCS):

    pass
class essentialoclcs_CollectionTypeCS(Nameable, TypedRefCS):

    def __init__(self, name: str, essentialoclcs_CollectionTypeCS33: "essentialoclcs_TypedRefCS" = None, essentialoclcs_CollectionTypeCS: "essentialoclcs_CollectionLiteralExpCS" = None, essentialoclcs_CollectionTypeCS31: "essentialoclcs_CollectionPatternCS" = None):
        self.name = name
        self.essentialoclcs_CollectionTypeCS33 = essentialoclcs_CollectionTypeCS33
        self.essentialoclcs_CollectionTypeCS = essentialoclcs_CollectionTypeCS
        self.essentialoclcs_CollectionTypeCS31 = essentialoclcs_CollectionTypeCS31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def essentialoclcs_CollectionTypeCS31(self):
        return self.__essentialoclcs_CollectionTypeCS31

    @essentialoclcs_CollectionTypeCS31.setter
    def essentialoclcs_CollectionTypeCS31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_CollectionTypeCS__essentialoclcs_CollectionTypeCS31", None)
        self.__essentialoclcs_CollectionTypeCS31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_CollectionPatternCS30"):
                opp_val = getattr(old_value, "essentialoclcs_CollectionPatternCS30", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_CollectionPatternCS30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_CollectionPatternCS30"):
                opp_val = getattr(value, "essentialoclcs_CollectionPatternCS30", None)
                setattr(value, "essentialoclcs_CollectionPatternCS30", self)

    @property
    def essentialoclcs_CollectionTypeCS33(self):
        return self.__essentialoclcs_CollectionTypeCS33

    @essentialoclcs_CollectionTypeCS33.setter
    def essentialoclcs_CollectionTypeCS33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_CollectionTypeCS__essentialoclcs_CollectionTypeCS33", None)
        self.__essentialoclcs_CollectionTypeCS33 = value
        
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
            if hasattr(old_value, "essentialoclcs_CollectionLiteralExpCS18"):
                opp_val = getattr(old_value, "essentialoclcs_CollectionLiteralExpCS18", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_CollectionLiteralExpCS18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_CollectionLiteralExpCS18"):
                opp_val = getattr(value, "essentialoclcs_CollectionLiteralExpCS18", None)
                setattr(value, "essentialoclcs_CollectionLiteralExpCS18", self)

class essentialoclcs_MapTypeCS(Nameable, TypedRefCS):

    def __init__(self, name: str, essentialoclcs_MapTypeCS99: "essentialoclcs_TypedRefCS" = None, essentialoclcs_MapTypeCS102: "essentialoclcs_TypedRefCS" = None, essentialoclcs_MapTypeCS: "essentialoclcs_MapLiteralExpCS" = None):
        self.name = name
        self.essentialoclcs_MapTypeCS99 = essentialoclcs_MapTypeCS99
        self.essentialoclcs_MapTypeCS102 = essentialoclcs_MapTypeCS102
        self.essentialoclcs_MapTypeCS = essentialoclcs_MapTypeCS
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def essentialoclcs_MapTypeCS(self):
        return self.__essentialoclcs_MapTypeCS

    @essentialoclcs_MapTypeCS.setter
    def essentialoclcs_MapTypeCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_MapTypeCS__essentialoclcs_MapTypeCS", None)
        self.__essentialoclcs_MapTypeCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_MapLiteralExpCS91"):
                opp_val = getattr(old_value, "essentialoclcs_MapLiteralExpCS91", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_MapLiteralExpCS91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_MapLiteralExpCS91"):
                opp_val = getattr(value, "essentialoclcs_MapLiteralExpCS91", None)
                setattr(value, "essentialoclcs_MapLiteralExpCS91", self)

    @property
    def essentialoclcs_MapTypeCS102(self):
        return self.__essentialoclcs_MapTypeCS102

    @essentialoclcs_MapTypeCS102.setter
    def essentialoclcs_MapTypeCS102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_MapTypeCS__essentialoclcs_MapTypeCS102", None)
        self.__essentialoclcs_MapTypeCS102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_TypedRefCS103"):
                opp_val = getattr(old_value, "essentialoclcs_TypedRefCS103", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_TypedRefCS103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_TypedRefCS103"):
                opp_val = getattr(value, "essentialoclcs_TypedRefCS103", None)
                setattr(value, "essentialoclcs_TypedRefCS103", self)

    @property
    def essentialoclcs_MapTypeCS99(self):
        return self.__essentialoclcs_MapTypeCS99

    @essentialoclcs_MapTypeCS99.setter
    def essentialoclcs_MapTypeCS99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_MapTypeCS__essentialoclcs_MapTypeCS99", None)
        self.__essentialoclcs_MapTypeCS99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_TypedRefCS100"):
                opp_val = getattr(old_value, "essentialoclcs_TypedRefCS100", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_TypedRefCS100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_TypedRefCS100"):
                opp_val = getattr(value, "essentialoclcs_TypedRefCS100", None)
                setattr(value, "essentialoclcs_TypedRefCS100", self)

class essentialoclcs_Type:

    pass
class essentialoclcs_SquareBracketedClauseCS(ContextLessElementCS):

    pass
class essentialoclcs_RoundBracketedClauseCS(ContextLessElementCS):

    pass
class essentialoclcs_PathNameCS:

    pass
class essentialoclcs_CurlyBracketedClauseCS(ContextLessElementCS):

    def __init__(self, value: str, CurlyBracketedClauseCS: "essentialoclcs_AbstractNameExpCS" = None, owningCurlyBracketClause: set["essentialoclcs_ShadowPartCS"] = None, ownedCurlyBracketedClause: "essentialoclcs_AbstractNameExpCS" = None, CurlyBracketedClauseCS136: "essentialoclcs_ShadowPartCS" = None, essentialoclcs_CurlyBracketedClauseCS: "essentialoclcs_TypeNameExpCS" = None):
        self.value = value
        self.CurlyBracketedClauseCS = CurlyBracketedClauseCS
        self.owningCurlyBracketClause = owningCurlyBracketClause if owningCurlyBracketClause is not None else set()
        self.ownedCurlyBracketedClause = ownedCurlyBracketedClause
        self.CurlyBracketedClauseCS136 = CurlyBracketedClauseCS136
        self.essentialoclcs_CurlyBracketedClauseCS = essentialoclcs_CurlyBracketedClauseCS
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def ownedCurlyBracketedClause(self):
        return self.__ownedCurlyBracketedClause

    @ownedCurlyBracketedClause.setter
    def ownedCurlyBracketedClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_CurlyBracketedClauseCS__ownedCurlyBracketedClause", None)
        self.__ownedCurlyBracketedClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractNameExpCS"):
                opp_val = getattr(old_value, "AbstractNameExpCS", None)
                if opp_val == self:
                    setattr(old_value, "AbstractNameExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractNameExpCS"):
                opp_val = getattr(value, "AbstractNameExpCS", None)
                setattr(value, "AbstractNameExpCS", self)

    @property
    def CurlyBracketedClauseCS136(self):
        return self.__CurlyBracketedClauseCS136

    @CurlyBracketedClauseCS136.setter
    def CurlyBracketedClauseCS136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_CurlyBracketedClauseCS__CurlyBracketedClauseCS136", None)
        self.__CurlyBracketedClauseCS136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedParts"):
                opp_val = getattr(old_value, "ownedParts", None)
                if opp_val == self:
                    setattr(old_value, "ownedParts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedParts"):
                opp_val = getattr(value, "ownedParts", None)
                setattr(value, "ownedParts", self)

    @property
    def essentialoclcs_CurlyBracketedClauseCS(self):
        return self.__essentialoclcs_CurlyBracketedClauseCS

    @essentialoclcs_CurlyBracketedClauseCS.setter
    def essentialoclcs_CurlyBracketedClauseCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_CurlyBracketedClauseCS__essentialoclcs_CurlyBracketedClauseCS", None)
        self.__essentialoclcs_CurlyBracketedClauseCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_TypeNameExpCS154"):
                opp_val = getattr(old_value, "essentialoclcs_TypeNameExpCS154", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_TypeNameExpCS154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_TypeNameExpCS154"):
                opp_val = getattr(value, "essentialoclcs_TypeNameExpCS154", None)
                setattr(value, "essentialoclcs_TypeNameExpCS154", self)

    @property
    def CurlyBracketedClauseCS(self):
        return self.__CurlyBracketedClauseCS

    @CurlyBracketedClauseCS.setter
    def CurlyBracketedClauseCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_CurlyBracketedClauseCS__CurlyBracketedClauseCS", None)
        self.__CurlyBracketedClauseCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningNameExp"):
                opp_val = getattr(old_value, "owningNameExp", None)
                if opp_val == self:
                    setattr(old_value, "owningNameExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningNameExp"):
                opp_val = getattr(value, "owningNameExp", None)
                setattr(value, "owningNameExp", self)

    @property
    def owningCurlyBracketClause(self):
        return self.__owningCurlyBracketClause

    @owningCurlyBracketClause.setter
    def owningCurlyBracketClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_CurlyBracketedClauseCS__owningCurlyBracketClause", None)
        self.__owningCurlyBracketClause = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ShadowPartCS"):
                    opp_val = getattr(item, "ShadowPartCS", None)
                    
                    if opp_val == self:
                        setattr(item, "ShadowPartCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ShadowPartCS"):
                    opp_val = getattr(item, "ShadowPartCS", None)
                    
                    setattr(item, "ShadowPartCS", self)
                    

class ExpCS:

    pass
class essentialoclcs_PatternExpCS(ExpCS):

    def __init__(self, patternVariableName: str, essentialoclcs_PatternExpCS: "essentialoclcs_CollectionPatternCS" = None, essentialoclcs_PatternExpCS124: "essentialoclcs_TypeRefCS" = None):
        self.patternVariableName = patternVariableName
        self.essentialoclcs_PatternExpCS = essentialoclcs_PatternExpCS
        self.essentialoclcs_PatternExpCS124 = essentialoclcs_PatternExpCS124
        
    @property
    def patternVariableName(self) -> str:
        return self.__patternVariableName

    @patternVariableName.setter
    def patternVariableName(self, patternVariableName: str):
        self.__patternVariableName = patternVariableName

    @property
    def essentialoclcs_PatternExpCS124(self):
        return self.__essentialoclcs_PatternExpCS124

    @essentialoclcs_PatternExpCS124.setter
    def essentialoclcs_PatternExpCS124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_PatternExpCS__essentialoclcs_PatternExpCS124", None)
        self.__essentialoclcs_PatternExpCS124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_TypeRefCS"):
                opp_val = getattr(old_value, "essentialoclcs_TypeRefCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_TypeRefCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_TypeRefCS"):
                opp_val = getattr(value, "essentialoclcs_TypeRefCS", None)
                setattr(value, "essentialoclcs_TypeRefCS", self)

    @property
    def essentialoclcs_PatternExpCS(self):
        return self.__essentialoclcs_PatternExpCS

    @essentialoclcs_PatternExpCS.setter
    def essentialoclcs_PatternExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_PatternExpCS__essentialoclcs_PatternExpCS", None)
        self.__essentialoclcs_PatternExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_CollectionPatternCS"):
                opp_val = getattr(old_value, "essentialoclcs_CollectionPatternCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_CollectionPatternCS"):
                opp_val = getattr(value, "essentialoclcs_CollectionPatternCS", None)
                if opp_val is None:
                    setattr(value, "essentialoclcs_CollectionPatternCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
class essentialoclcs_IfThenExpCS(ExpCS):

    pass
class essentialoclcs_OperatorExpCS(NamedElementCS, ExpCS):

    pass
class essentialoclcs_LetVariableCS(ExpCS, VariableCS):

    pass
class essentialoclcs_IfExpCS(ExpCS):

    def __init__(self, isImplicit: bool, essentialoclcs_IfExpCS: "essentialoclcs_ExpCS" = None, essentialoclcs_IfExpCS59: "essentialoclcs_ExpCS" = None, essentialoclcs_IfExpCS62: set["essentialoclcs_IfThenExpCS"] = None, essentialoclcs_IfExpCS64: "essentialoclcs_ExpCS" = None):
        self.isImplicit = isImplicit
        self.essentialoclcs_IfExpCS = essentialoclcs_IfExpCS
        self.essentialoclcs_IfExpCS59 = essentialoclcs_IfExpCS59
        self.essentialoclcs_IfExpCS62 = essentialoclcs_IfExpCS62 if essentialoclcs_IfExpCS62 is not None else set()
        self.essentialoclcs_IfExpCS64 = essentialoclcs_IfExpCS64
        
    @property
    def isImplicit(self) -> bool:
        return self.__isImplicit

    @isImplicit.setter
    def isImplicit(self, isImplicit: bool):
        self.__isImplicit = isImplicit

    @property
    def essentialoclcs_IfExpCS59(self):
        return self.__essentialoclcs_IfExpCS59

    @essentialoclcs_IfExpCS59.setter
    def essentialoclcs_IfExpCS59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_IfExpCS__essentialoclcs_IfExpCS59", None)
        self.__essentialoclcs_IfExpCS59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS60"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS60", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS60"):
                opp_val = getattr(value, "essentialoclcs_ExpCS60", None)
                setattr(value, "essentialoclcs_ExpCS60", self)

    @property
    def essentialoclcs_IfExpCS(self):
        return self.__essentialoclcs_IfExpCS

    @essentialoclcs_IfExpCS.setter
    def essentialoclcs_IfExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_IfExpCS__essentialoclcs_IfExpCS", None)
        self.__essentialoclcs_IfExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS57"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS57", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS57"):
                opp_val = getattr(value, "essentialoclcs_ExpCS57", None)
                setattr(value, "essentialoclcs_ExpCS57", self)

    @property
    def essentialoclcs_IfExpCS64(self):
        return self.__essentialoclcs_IfExpCS64

    @essentialoclcs_IfExpCS64.setter
    def essentialoclcs_IfExpCS64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_IfExpCS__essentialoclcs_IfExpCS64", None)
        self.__essentialoclcs_IfExpCS64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS65"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS65", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS65"):
                opp_val = getattr(value, "essentialoclcs_ExpCS65", None)
                setattr(value, "essentialoclcs_ExpCS65", self)

    @property
    def essentialoclcs_IfExpCS62(self):
        return self.__essentialoclcs_IfExpCS62

    @essentialoclcs_IfExpCS62.setter
    def essentialoclcs_IfExpCS62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_IfExpCS__essentialoclcs_IfExpCS62", None)
        self.__essentialoclcs_IfExpCS62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "essentialoclcs_IfThenExpCS"):
                    opp_val = getattr(item, "essentialoclcs_IfThenExpCS", None)
                    
                    if opp_val == self:
                        setattr(item, "essentialoclcs_IfThenExpCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "essentialoclcs_IfThenExpCS"):
                    opp_val = getattr(item, "essentialoclcs_IfThenExpCS", None)
                    
                    setattr(item, "essentialoclcs_IfThenExpCS", self)
                    

class essentialoclcs_LetExpCS(ExpCS):

    def __init__(self, isImplicit: bool, essentialoclcs_LetExpCS: "essentialoclcs_ExpCS" = None, owningLetExpression: set["essentialoclcs_LetVariableCS"] = None, LetExpCS: "essentialoclcs_LetVariableCS" = None):
        self.isImplicit = isImplicit
        self.essentialoclcs_LetExpCS = essentialoclcs_LetExpCS
        self.owningLetExpression = owningLetExpression if owningLetExpression is not None else set()
        self.LetExpCS = LetExpCS
        
    @property
    def isImplicit(self) -> bool:
        return self.__isImplicit

    @isImplicit.setter
    def isImplicit(self, isImplicit: bool):
        self.__isImplicit = isImplicit

    @property
    def owningLetExpression(self):
        return self.__owningLetExpression

    @owningLetExpression.setter
    def owningLetExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_LetExpCS__owningLetExpression", None)
        self.__owningLetExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LetVariableCS"):
                    opp_val = getattr(item, "LetVariableCS", None)
                    
                    if opp_val == self:
                        setattr(item, "LetVariableCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LetVariableCS"):
                    opp_val = getattr(item, "LetVariableCS", None)
                    
                    setattr(item, "LetVariableCS", self)
                    

    @property
    def essentialoclcs_LetExpCS(self):
        return self.__essentialoclcs_LetExpCS

    @essentialoclcs_LetExpCS.setter
    def essentialoclcs_LetExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_LetExpCS__essentialoclcs_LetExpCS", None)
        self.__essentialoclcs_LetExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_ExpCS85"):
                opp_val = getattr(old_value, "essentialoclcs_ExpCS85", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_ExpCS85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_ExpCS85"):
                opp_val = getattr(value, "essentialoclcs_ExpCS85", None)
                setattr(value, "essentialoclcs_ExpCS85", self)

    @property
    def LetExpCS(self):
        return self.__LetExpCS

    @LetExpCS.setter
    def LetExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_LetExpCS__LetExpCS", None)
        self.__LetExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedVariables"):
                opp_val = getattr(old_value, "ownedVariables", None)
                if opp_val == self:
                    setattr(old_value, "ownedVariables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedVariables"):
                opp_val = getattr(value, "ownedVariables", None)
                setattr(value, "ownedVariables", self)

class essentialoclcs_NestedExpCS(ExpCS):

    pass
class essentialoclcs_AbstractNameExpCS(ExpCS):

    def __init__(self, isPre: bool, owningNameExp: "essentialoclcs_CurlyBracketedClauseCS" = None, essentialoclcs_AbstractNameExpCS: "essentialoclcs_PathNameCS" = None, owningNameExp3: "essentialoclcs_RoundBracketedClauseCS" = None, owningNameExp5: set["essentialoclcs_SquareBracketedClauseCS"] = None, essentialoclcs_AbstractNameExpCS7: "essentialoclcs_Type" = None, essentialoclcs_AbstractNameExpCS9: "essentialoclcs_Type" = None, AbstractNameExpCS: "essentialoclcs_CurlyBracketedClauseCS" = None, AbstractNameExpCS128: "essentialoclcs_RoundBracketedClauseCS" = None, AbstractNameExpCS143: "essentialoclcs_SquareBracketedClauseCS" = None):
        self.isPre = isPre
        self.owningNameExp = owningNameExp
        self.essentialoclcs_AbstractNameExpCS = essentialoclcs_AbstractNameExpCS
        self.owningNameExp3 = owningNameExp3
        self.owningNameExp5 = owningNameExp5 if owningNameExp5 is not None else set()
        self.essentialoclcs_AbstractNameExpCS7 = essentialoclcs_AbstractNameExpCS7
        self.essentialoclcs_AbstractNameExpCS9 = essentialoclcs_AbstractNameExpCS9
        self.AbstractNameExpCS = AbstractNameExpCS
        self.AbstractNameExpCS128 = AbstractNameExpCS128
        self.AbstractNameExpCS143 = AbstractNameExpCS143
        
    @property
    def isPre(self) -> bool:
        return self.__isPre

    @isPre.setter
    def isPre(self, isPre: bool):
        self.__isPre = isPre

    @property
    def AbstractNameExpCS128(self):
        return self.__AbstractNameExpCS128

    @AbstractNameExpCS128.setter
    def AbstractNameExpCS128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_AbstractNameExpCS__AbstractNameExpCS128", None)
        self.__AbstractNameExpCS128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedRoundBracketedClause"):
                opp_val = getattr(old_value, "ownedRoundBracketedClause", None)
                if opp_val == self:
                    setattr(old_value, "ownedRoundBracketedClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedRoundBracketedClause"):
                opp_val = getattr(value, "ownedRoundBracketedClause", None)
                setattr(value, "ownedRoundBracketedClause", self)

    @property
    def AbstractNameExpCS(self):
        return self.__AbstractNameExpCS

    @AbstractNameExpCS.setter
    def AbstractNameExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_AbstractNameExpCS__AbstractNameExpCS", None)
        self.__AbstractNameExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedCurlyBracketedClause"):
                opp_val = getattr(old_value, "ownedCurlyBracketedClause", None)
                if opp_val == self:
                    setattr(old_value, "ownedCurlyBracketedClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedCurlyBracketedClause"):
                opp_val = getattr(value, "ownedCurlyBracketedClause", None)
                setattr(value, "ownedCurlyBracketedClause", self)

    @property
    def owningNameExp3(self):
        return self.__owningNameExp3

    @owningNameExp3.setter
    def owningNameExp3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_AbstractNameExpCS__owningNameExp3", None)
        self.__owningNameExp3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoundBracketedClauseCS"):
                opp_val = getattr(old_value, "RoundBracketedClauseCS", None)
                if opp_val == self:
                    setattr(old_value, "RoundBracketedClauseCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoundBracketedClauseCS"):
                opp_val = getattr(value, "RoundBracketedClauseCS", None)
                setattr(value, "RoundBracketedClauseCS", self)

    @property
    def essentialoclcs_AbstractNameExpCS7(self):
        return self.__essentialoclcs_AbstractNameExpCS7

    @essentialoclcs_AbstractNameExpCS7.setter
    def essentialoclcs_AbstractNameExpCS7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_AbstractNameExpCS__essentialoclcs_AbstractNameExpCS7", None)
        self.__essentialoclcs_AbstractNameExpCS7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_Type"):
                opp_val = getattr(old_value, "essentialoclcs_Type", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_Type"):
                opp_val = getattr(value, "essentialoclcs_Type", None)
                setattr(value, "essentialoclcs_Type", self)

    @property
    def essentialoclcs_AbstractNameExpCS(self):
        return self.__essentialoclcs_AbstractNameExpCS

    @essentialoclcs_AbstractNameExpCS.setter
    def essentialoclcs_AbstractNameExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_AbstractNameExpCS__essentialoclcs_AbstractNameExpCS", None)
        self.__essentialoclcs_AbstractNameExpCS = value
        
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
    def essentialoclcs_AbstractNameExpCS9(self):
        return self.__essentialoclcs_AbstractNameExpCS9

    @essentialoclcs_AbstractNameExpCS9.setter
    def essentialoclcs_AbstractNameExpCS9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_AbstractNameExpCS__essentialoclcs_AbstractNameExpCS9", None)
        self.__essentialoclcs_AbstractNameExpCS9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialoclcs_Type10"):
                opp_val = getattr(old_value, "essentialoclcs_Type10", None)
                if opp_val == self:
                    setattr(old_value, "essentialoclcs_Type10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialoclcs_Type10"):
                opp_val = getattr(value, "essentialoclcs_Type10", None)
                setattr(value, "essentialoclcs_Type10", self)

    @property
    def owningNameExp5(self):
        return self.__owningNameExp5

    @owningNameExp5.setter
    def owningNameExp5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_AbstractNameExpCS__owningNameExp5", None)
        self.__owningNameExp5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SquareBracketedClauseCS"):
                    opp_val = getattr(item, "SquareBracketedClauseCS", None)
                    
                    if opp_val == self:
                        setattr(item, "SquareBracketedClauseCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SquareBracketedClauseCS"):
                    opp_val = getattr(item, "SquareBracketedClauseCS", None)
                    
                    setattr(item, "SquareBracketedClauseCS", self)
                    

    @property
    def AbstractNameExpCS143(self):
        return self.__AbstractNameExpCS143

    @AbstractNameExpCS143.setter
    def AbstractNameExpCS143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_AbstractNameExpCS__AbstractNameExpCS143", None)
        self.__AbstractNameExpCS143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedSquareBracketedClauses"):
                opp_val = getattr(old_value, "ownedSquareBracketedClauses", None)
                if opp_val == self:
                    setattr(old_value, "ownedSquareBracketedClauses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedSquareBracketedClauses"):
                opp_val = getattr(value, "ownedSquareBracketedClauses", None)
                setattr(value, "ownedSquareBracketedClauses", self)

    @property
    def owningNameExp(self):
        return self.__owningNameExp

    @owningNameExp.setter
    def owningNameExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialoclcs_AbstractNameExpCS__owningNameExp", None)
        self.__owningNameExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CurlyBracketedClauseCS"):
                opp_val = getattr(old_value, "CurlyBracketedClauseCS", None)
                if opp_val == self:
                    setattr(old_value, "CurlyBracketedClauseCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CurlyBracketedClauseCS"):
                opp_val = getattr(value, "CurlyBracketedClauseCS", None)
                setattr(value, "CurlyBracketedClauseCS", self)

class PrimitiveLiteralExpCS:

    pass
class essentialoclcs_NullLiteralExpCS(PrimitiveLiteralExpCS):

    pass
class essentialoclcs_StringLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, segments: str):
        self.segments = segments
        
    @property
    def segments(self) -> str:
        return self.__segments

    @segments.setter
    def segments(self, segments: str):
        self.__segments = segments

class essentialoclcs_InvalidLiteralExpCS(PrimitiveLiteralExpCS):

    pass
class essentialoclcs_UnlimitedNaturalLiteralExpCS(PrimitiveLiteralExpCS):

    pass
class essentialoclcs_NumberLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class essentialoclcs_BooleanLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class essentialoclcs_AssociationClass:

    pass
class CallExpCS:

    pass
class essentialoclcs_OperationCallExpCS(CallExpCS):

    pass
class essentialoclcs_IterationCallExpCS(CallExpCS):

    pass
class essentialoclcs_PropertyCallExpCS(CallExpCS):

    pass
class essentialoclcs_AssociationClassCallExpCS(CallExpCS):

    pass