from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DirectedRelationship:

    pass
class UsecaseDSL_MultiplicityElement_c(ABC):

    def __init__(self, sourceLower: str, sourceUpper: str, targetLower: str, targetUpper: str):
        self.sourceLower = sourceLower
        self.sourceUpper = sourceUpper
        self.targetLower = targetLower
        self.targetUpper = targetUpper
        
        pass
    @property
    def targetLower(self):
        return self.__targetLower

    @targetLower.setter
    def targetLower(self, targetLower: str):
        self.__targetLower = targetLower


    @property
    def sourceLower(self):
        return self.__sourceLower

    @sourceLower.setter
    def sourceLower(self, sourceLower: str):
        self.__sourceLower = sourceLower


    @property
    def sourceUpper(self):
        return self.__sourceUpper

    @sourceUpper.setter
    def sourceUpper(self, sourceUpper: str):
        self.__sourceUpper = sourceUpper


    @property
    def targetUpper(self):
        return self.__targetUpper

    @targetUpper.setter
    def targetUpper(self, targetUpper: str):
        self.__targetUpper = targetUpper


class Namespace:

    pass
class UsecaseDSL_Classifier(Namespace):

    pass
class NamedElement:

    pass
class UsecaseDSL_Extend_c(NamedElement, DirectedRelationship):

    def __init__(self, Expression: str, UsecaseDSL_Extend_c: "UsecaseDSL_UseCase" = None, UsecaseDSL_Extend_c36: "UsecaseDSL_UseCase" = None, UsecaseDSL_Extend_c39: "UsecaseDSL_UseCase" = None):
        self.Expression = Expression
        self.UsecaseDSL_Extend_c = UsecaseDSL_Extend_c
        self.UsecaseDSL_Extend_c36 = UsecaseDSL_Extend_c36
        self.UsecaseDSL_Extend_c39 = UsecaseDSL_Extend_c39
        
        pass
    @property
    def Expression(self):
        return self.__Expression

    @Expression.setter
    def Expression(self, Expression: str):
        self.__Expression = Expression


    @property
    def UsecaseDSL_Extend_c(self):
        return self.__UsecaseDSL_Extend_c

    @UsecaseDSL_Extend_c.setter
    def UsecaseDSL_Extend_c(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UsecaseDSL_Extend_c__UsecaseDSL_Extend_c", None)
        self.__UsecaseDSL_Extend_c = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UsecaseDSL_UseCase32"):
                opp_val = getattr(old_value, "UsecaseDSL_UseCase32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UsecaseDSL_UseCase32"):
                opp_val = getattr(value, "UsecaseDSL_UseCase32", None)
                if opp_val is None:
                    setattr(value, "UsecaseDSL_UseCase32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UsecaseDSL_Extend_c39(self):
        return self.__UsecaseDSL_Extend_c39

    @UsecaseDSL_Extend_c39.setter
    def UsecaseDSL_Extend_c39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UsecaseDSL_Extend_c__UsecaseDSL_Extend_c39", None)
        self.__UsecaseDSL_Extend_c39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UsecaseDSL_UseCase40"):
                opp_val = getattr(old_value, "UsecaseDSL_UseCase40", None)
                if opp_val == self:
                    setattr(old_value, "UsecaseDSL_UseCase40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UsecaseDSL_UseCase40"):
                opp_val = getattr(value, "UsecaseDSL_UseCase40", None)
                setattr(value, "UsecaseDSL_UseCase40", self)

    @property
    def UsecaseDSL_Extend_c36(self):
        return self.__UsecaseDSL_Extend_c36

    @UsecaseDSL_Extend_c36.setter
    def UsecaseDSL_Extend_c36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UsecaseDSL_Extend_c__UsecaseDSL_Extend_c36", None)
        self.__UsecaseDSL_Extend_c36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UsecaseDSL_UseCase37"):
                opp_val = getattr(old_value, "UsecaseDSL_UseCase37", None)
                if opp_val == self:
                    setattr(old_value, "UsecaseDSL_UseCase37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UsecaseDSL_UseCase37"):
                opp_val = getattr(value, "UsecaseDSL_UseCase37", None)
                setattr(value, "UsecaseDSL_UseCase37", self)

class UsecaseDSL_ExtensionPoint(NamedElement):

    pass
class UsecaseDSL_Include(NamedElement, DirectedRelationship):

    pass
class UsecaseDSL_Namespace(NamedElement):

    pass
class UsecaseDSL_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class MultiplicityElement_c:

    pass
class Classifier:

    pass
class UsecaseDSL_System_c(Classifier):

    pass
class UsecaseDSL_Actor(Classifier):

    pass
class UsecaseDSL_UseCase(Classifier):

    pass
class UsecaseDSL_UseCaseDiagram_c(Classifier):

    pass
class Relationship:

    pass
class UsecaseDSL_Association_c(MultiplicityElement_c, Classifier, Relationship):

    pass
class UsecaseDSL_DirectedRelationship(Relationship):

    pass
class UsecaseDSL_Relationship(ABC):

    pass
class UsecaseDSL_Generalization(DirectedRelationship):

    pass