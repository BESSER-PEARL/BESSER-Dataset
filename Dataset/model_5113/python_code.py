from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class demo1_RatioExpression:

    def __init__(self, ratio: int, demo1_RatioExpression: "demo1_RuleExpression" = None):
        self.ratio = ratio
        self.demo1_RatioExpression = demo1_RatioExpression
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def demo1_RatioExpression(self):
        return self.__demo1_RatioExpression

    @demo1_RatioExpression.setter
    def demo1_RatioExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_demo1_RatioExpression__demo1_RatioExpression", None)
        self.__demo1_RatioExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "demo1_RuleExpression10"):
                opp_val = getattr(old_value, "demo1_RuleExpression10", None)
                if opp_val == self:
                    setattr(old_value, "demo1_RuleExpression10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "demo1_RuleExpression10"):
                opp_val = getattr(value, "demo1_RuleExpression10", None)
                setattr(value, "demo1_RuleExpression10", self)

class demo1_TestExpression:

    pass
class demo1_EObject:

    pass
class demo1_RuleExpression:

    pass
class demo1_Rule:

    pass
class demo1_Category:

    def __init__(self, name: str, demo1_Category: "demo1_Model" = None, demo1_Category13: "demo1_TestExpression" = None):
        self.name = name
        self.demo1_Category = demo1_Category
        self.demo1_Category13 = demo1_Category13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def demo1_Category(self):
        return self.__demo1_Category

    @demo1_Category.setter
    def demo1_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_demo1_Category__demo1_Category", None)
        self.__demo1_Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "demo1_Model"):
                opp_val = getattr(old_value, "demo1_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "demo1_Model"):
                opp_val = getattr(value, "demo1_Model", None)
                if opp_val is None:
                    setattr(value, "demo1_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def demo1_Category13(self):
        return self.__demo1_Category13

    @demo1_Category13.setter
    def demo1_Category13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_demo1_Category__demo1_Category13", None)
        self.__demo1_Category13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "demo1_TestExpression12"):
                opp_val = getattr(old_value, "demo1_TestExpression12", None)
                if opp_val == self:
                    setattr(old_value, "demo1_TestExpression12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "demo1_TestExpression12"):
                opp_val = getattr(value, "demo1_TestExpression12", None)
                setattr(value, "demo1_TestExpression12", self)

class demo1_Model:

    pass