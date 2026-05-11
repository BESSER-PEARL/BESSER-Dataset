from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fM_Child:

    def __init__(self, mandatory: bool, name: str, fM_Child: "fM_FeatureDiagram" = None, fM_Child6: "fM_Node" = None):
        self.mandatory = mandatory
        self.name = name
        self.fM_Child = fM_Child
        self.fM_Child6 = fM_Child6
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def mandatory(self):
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory


    @property
    def fM_Child(self):
        return self.__fM_Child

    @fM_Child.setter
    def fM_Child(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fM_Child__fM_Child", None)
        self.__fM_Child = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fM_FeatureDiagram4"):
                opp_val = getattr(old_value, "fM_FeatureDiagram4", None)
                if opp_val == self:
                    setattr(old_value, "fM_FeatureDiagram4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fM_FeatureDiagram4"):
                opp_val = getattr(value, "fM_FeatureDiagram4", None)
                setattr(value, "fM_FeatureDiagram4", self)

    @property
    def fM_Child6(self):
        return self.__fM_Child6

    @fM_Child6.setter
    def fM_Child6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fM_Child__fM_Child6", None)
        self.__fM_Child6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fM_Node"):
                opp_val = getattr(old_value, "fM_Node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fM_Node"):
                opp_val = getattr(value, "fM_Node", None)
                if opp_val is None:
                    setattr(value, "fM_Node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fM_Constraints:

    pass
class fM_FeatureDiagram:

    pass
class fM_FeatureModel:

    pass
class Formula:

    pass
class fM_Var(Formula):

    def __init__(self, not_: bool, name: str, fM_Var14: "fM_RuleElement" = None, fM_Var: "fM_RuleElement" = None):
        self.not_ = not_
        self.name = name
        self.fM_Var14 = fM_Var14
        self.fM_Var = fM_Var
        
        pass
    @property
    def not_(self):
        return self.__not_

    @not_.setter
    def not_(self, not_: bool):
        self.__not_ = not_


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def fM_Var(self):
        return self.__fM_Var

    @fM_Var.setter
    def fM_Var(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fM_Var__fM_Var", None)
        self.__fM_Var = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fM_RuleElement"):
                opp_val = getattr(old_value, "fM_RuleElement", None)
                if opp_val == self:
                    setattr(old_value, "fM_RuleElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fM_RuleElement"):
                opp_val = getattr(value, "fM_RuleElement", None)
                setattr(value, "fM_RuleElement", self)

    @property
    def fM_Var14(self):
        return self.__fM_Var14

    @fM_Var14.setter
    def fM_Var14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fM_Var__fM_Var14", None)
        self.__fM_Var14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fM_RuleElement13"):
                opp_val = getattr(old_value, "fM_RuleElement13", None)
                if opp_val == self:
                    setattr(old_value, "fM_RuleElement13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fM_RuleElement13"):
                opp_val = getattr(value, "fM_RuleElement13", None)
                setattr(value, "fM_RuleElement13", self)

class fM_RuleElement(Formula):

    def __init__(self, open_operator: str, close_operator: str, fM_RuleElement13: "fM_Var" = None, fM_RuleElement: "fM_Var" = None):
        self.open_operator = open_operator
        self.close_operator = close_operator
        self.fM_RuleElement13 = fM_RuleElement13
        self.fM_RuleElement = fM_RuleElement
        
        pass
    @property
    def close_operator(self):
        return self.__close_operator

    @close_operator.setter
    def close_operator(self, close_operator: str):
        self.__close_operator = close_operator


    @property
    def open_operator(self):
        return self.__open_operator

    @open_operator.setter
    def open_operator(self, open_operator: str):
        self.__open_operator = open_operator


    @property
    def fM_RuleElement(self):
        return self.__fM_RuleElement

    @fM_RuleElement.setter
    def fM_RuleElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fM_RuleElement__fM_RuleElement", None)
        self.__fM_RuleElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fM_Var"):
                opp_val = getattr(old_value, "fM_Var", None)
                if opp_val == self:
                    setattr(old_value, "fM_Var", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fM_Var"):
                opp_val = getattr(value, "fM_Var", None)
                setattr(value, "fM_Var", self)

    @property
    def fM_RuleElement13(self):
        return self.__fM_RuleElement13

    @fM_RuleElement13.setter
    def fM_RuleElement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fM_RuleElement__fM_RuleElement13", None)
        self.__fM_RuleElement13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fM_Var14"):
                opp_val = getattr(old_value, "fM_Var14", None)
                if opp_val == self:
                    setattr(old_value, "fM_Var14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fM_Var14"):
                opp_val = getattr(value, "fM_Var14", None)
                setattr(value, "fM_Var14", self)

class fM_Formula:

    pass
class fM_Rule:

    pass
class Child:

    pass
class fM_Node(Child):

    def __init__(self, open_relation: str, close_relation: str, fM_Node: set["fM_Child"] = None):
        self.open_relation = open_relation
        self.close_relation = close_relation
        self.fM_Node = fM_Node if fM_Node is not None else set()
        
        pass
    @property
    def close_relation(self):
        return self.__close_relation

    @close_relation.setter
    def close_relation(self, close_relation: str):
        self.__close_relation = close_relation


    @property
    def open_relation(self):
        return self.__open_relation

    @open_relation.setter
    def open_relation(self, open_relation: str):
        self.__open_relation = open_relation


    @property
    def fM_Node(self):
        return self.__fM_Node

    @fM_Node.setter
    def fM_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fM_Node__fM_Node", None)
        self.__fM_Node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fM_Child6"):
                    opp_val = getattr(item, "fM_Child6", None)
                    
                    if opp_val == self:
                        setattr(item, "fM_Child6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fM_Child6"):
                    opp_val = getattr(item, "fM_Child6", None)
                    
                    setattr(item, "fM_Child6", self)
                    

class fM_Leaf(Child):

    pass