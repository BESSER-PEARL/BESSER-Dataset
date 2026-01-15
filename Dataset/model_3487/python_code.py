from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Expression:

    pass
class model_PrimaryExpression(Expression):

    def __init__(self, featureId: str):
        self.featureId = featureId
        
    @property
    def featureId(self) -> str:
        return self.__featureId

    @featureId.setter
    def featureId(self, featureId: str):
        self.__featureId = featureId

class model_Negation(Expression):

    pass
class model_ForAllContextualExpression(Expression):

    def __init__(self, contextId: str, model_ForAllContextualExpression: "model_Expression" = None):
        self.contextId = contextId
        self.model_ForAllContextualExpression = model_ForAllContextualExpression
        
    @property
    def contextId(self) -> str:
        return self.__contextId

    @contextId.setter
    def contextId(self, contextId: str):
        self.__contextId = contextId

    @property
    def model_ForAllContextualExpression(self):
        return self.__model_ForAllContextualExpression

    @model_ForAllContextualExpression.setter
    def model_ForAllContextualExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ForAllContextualExpression__model_ForAllContextualExpression", None)
        self.__model_ForAllContextualExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Expression"):
                opp_val = getattr(old_value, "model_Expression", None)
                if opp_val == self:
                    setattr(old_value, "model_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Expression"):
                opp_val = getattr(value, "model_Expression", None)
                setattr(value, "model_Expression", self)

class model_Expression(ABC):

    pass
class model_Conjunction(Expression):

    pass
class model_Disjunction(Expression):

    pass
class model_Implication(Expression):

    pass
class model_Equation(Expression):

    pass
class model_ExistsContextualExpression(Expression):

    def __init__(self, contextId: str, model_ExistsContextualExpression: "model_Expression" = None):
        self.contextId = contextId
        self.model_ExistsContextualExpression = model_ExistsContextualExpression
        
    @property
    def contextId(self) -> str:
        return self.__contextId

    @contextId.setter
    def contextId(self, contextId: str):
        self.__contextId = contextId

    @property
    def model_ExistsContextualExpression(self):
        return self.__model_ExistsContextualExpression

    @model_ExistsContextualExpression.setter
    def model_ExistsContextualExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ExistsContextualExpression__model_ExistsContextualExpression", None)
        self.__model_ExistsContextualExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Expression2"):
                opp_val = getattr(old_value, "model_Expression2", None)
                if opp_val == self:
                    setattr(old_value, "model_Expression2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Expression2"):
                opp_val = getattr(value, "model_Expression2", None)
                setattr(value, "model_Expression2", self)
