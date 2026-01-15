from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class cgimodel_Expr:

    def __init__(self, value: str, cgimodel_Expr: "cgimodel_State" = None, cgimodel_Expr14: "cgimodel_Transition" = None):
        self.value = value
        self.cgimodel_Expr = cgimodel_Expr
        self.cgimodel_Expr14 = cgimodel_Expr14
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def cgimodel_Expr(self):
        return self.__cgimodel_Expr

    @cgimodel_Expr.setter
    def cgimodel_Expr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cgimodel_Expr__cgimodel_Expr", None)
        self.__cgimodel_Expr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cgimodel_State"):
                opp_val = getattr(old_value, "cgimodel_State", None)
                if opp_val == self:
                    setattr(old_value, "cgimodel_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cgimodel_State"):
                opp_val = getattr(value, "cgimodel_State", None)
                setattr(value, "cgimodel_State", self)

    @property
    def cgimodel_Expr14(self):
        return self.__cgimodel_Expr14

    @cgimodel_Expr14.setter
    def cgimodel_Expr14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cgimodel_Expr__cgimodel_Expr14", None)
        self.__cgimodel_Expr14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cgimodel_Transition13"):
                opp_val = getattr(old_value, "cgimodel_Transition13", None)
                if opp_val == self:
                    setattr(old_value, "cgimodel_Transition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cgimodel_Transition13"):
                opp_val = getattr(value, "cgimodel_Transition13", None)
                setattr(value, "cgimodel_Transition13", self)

class BaseState:

    pass
class cgimodel_OrState(BaseState):

    pass
class cgimodel_State(BaseState):

    def __init__(self, set: bool, cgimodel_State: "cgimodel_Expr" = None, cgimodel_State11: "cgimodel_Transition" = None):
        self.set = set
        self.cgimodel_State = cgimodel_State
        self.cgimodel_State11 = cgimodel_State11
        
    @property
    def set(self) -> bool:
        return self.__set

    @set.setter
    def set(self, set: bool):
        self.__set = set

    @property
    def cgimodel_State(self):
        return self.__cgimodel_State

    @cgimodel_State.setter
    def cgimodel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cgimodel_State__cgimodel_State", None)
        self.__cgimodel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cgimodel_Expr"):
                opp_val = getattr(old_value, "cgimodel_Expr", None)
                if opp_val == self:
                    setattr(old_value, "cgimodel_Expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cgimodel_Expr"):
                opp_val = getattr(value, "cgimodel_Expr", None)
                setattr(value, "cgimodel_Expr", self)

    @property
    def cgimodel_State11(self):
        return self.__cgimodel_State11

    @cgimodel_State11.setter
    def cgimodel_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cgimodel_State__cgimodel_State11", None)
        self.__cgimodel_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cgimodel_Transition10"):
                opp_val = getattr(old_value, "cgimodel_Transition10", None)
                if opp_val == self:
                    setattr(old_value, "cgimodel_Transition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cgimodel_Transition10"):
                opp_val = getattr(value, "cgimodel_Transition10", None)
                setattr(value, "cgimodel_Transition10", self)

class cgimodel_Transition:

    pass
class cgimodel_BaseState(ABC):

    def __init__(self, name: str, cgimodel_BaseState: "cgimodel_StateModel" = None, cgimodel_BaseState5: "cgimodel_OrState" = None, cgimodel_BaseState8: "cgimodel_Transition" = None):
        self.name = name
        self.cgimodel_BaseState = cgimodel_BaseState
        self.cgimodel_BaseState5 = cgimodel_BaseState5
        self.cgimodel_BaseState8 = cgimodel_BaseState8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cgimodel_BaseState(self):
        return self.__cgimodel_BaseState

    @cgimodel_BaseState.setter
    def cgimodel_BaseState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cgimodel_BaseState__cgimodel_BaseState", None)
        self.__cgimodel_BaseState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cgimodel_StateModel"):
                opp_val = getattr(old_value, "cgimodel_StateModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cgimodel_StateModel"):
                opp_val = getattr(value, "cgimodel_StateModel", None)
                if opp_val is None:
                    setattr(value, "cgimodel_StateModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cgimodel_BaseState8(self):
        return self.__cgimodel_BaseState8

    @cgimodel_BaseState8.setter
    def cgimodel_BaseState8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cgimodel_BaseState__cgimodel_BaseState8", None)
        self.__cgimodel_BaseState8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cgimodel_Transition7"):
                opp_val = getattr(old_value, "cgimodel_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "cgimodel_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cgimodel_Transition7"):
                opp_val = getattr(value, "cgimodel_Transition7", None)
                setattr(value, "cgimodel_Transition7", self)

    @property
    def cgimodel_BaseState5(self):
        return self.__cgimodel_BaseState5

    @cgimodel_BaseState5.setter
    def cgimodel_BaseState5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cgimodel_BaseState__cgimodel_BaseState5", None)
        self.__cgimodel_BaseState5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cgimodel_OrState"):
                opp_val = getattr(old_value, "cgimodel_OrState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cgimodel_OrState"):
                opp_val = getattr(value, "cgimodel_OrState", None)
                if opp_val is None:
                    setattr(value, "cgimodel_OrState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isSet(self) -> bool:
        # TODO: Implement isSet method
        pass

class cgimodel_StateModel:

    def __init__(self, name: str, cgimodel_StateModel16: "cgimodel_StateModels" = None, cgimodel_StateModel: set["cgimodel_BaseState"] = None, cgimodel_StateModel2: set["cgimodel_Transition"] = None):
        self.name = name
        self.cgimodel_StateModel16 = cgimodel_StateModel16
        self.cgimodel_StateModel = cgimodel_StateModel if cgimodel_StateModel is not None else set()
        self.cgimodel_StateModel2 = cgimodel_StateModel2 if cgimodel_StateModel2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cgimodel_StateModel16(self):
        return self.__cgimodel_StateModel16

    @cgimodel_StateModel16.setter
    def cgimodel_StateModel16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cgimodel_StateModel__cgimodel_StateModel16", None)
        self.__cgimodel_StateModel16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cgimodel_StateModels"):
                opp_val = getattr(old_value, "cgimodel_StateModels", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cgimodel_StateModels"):
                opp_val = getattr(value, "cgimodel_StateModels", None)
                if opp_val is None:
                    setattr(value, "cgimodel_StateModels", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cgimodel_StateModel(self):
        return self.__cgimodel_StateModel

    @cgimodel_StateModel.setter
    def cgimodel_StateModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cgimodel_StateModel__cgimodel_StateModel", None)
        self.__cgimodel_StateModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cgimodel_BaseState"):
                    opp_val = getattr(item, "cgimodel_BaseState", None)
                    
                    if opp_val == self:
                        setattr(item, "cgimodel_BaseState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cgimodel_BaseState"):
                    opp_val = getattr(item, "cgimodel_BaseState", None)
                    
                    setattr(item, "cgimodel_BaseState", self)
                    

    @property
    def cgimodel_StateModel2(self):
        return self.__cgimodel_StateModel2

    @cgimodel_StateModel2.setter
    def cgimodel_StateModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cgimodel_StateModel__cgimodel_StateModel2", None)
        self.__cgimodel_StateModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cgimodel_Transition"):
                    opp_val = getattr(item, "cgimodel_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "cgimodel_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cgimodel_Transition"):
                    opp_val = getattr(item, "cgimodel_Transition", None)
                    
                    setattr(item, "cgimodel_Transition", self)
                    

class cgimodel_StateModels:

    pass