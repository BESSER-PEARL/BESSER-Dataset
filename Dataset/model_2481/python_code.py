from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_Transition:

    pass
class fsm_FSM:

    pass
class fsm_State:

    pass
class NoAnnotationSuper:

    pass
class fsm_NoAnnotation(NoAnnotationSuper):

    def __init__(self, a: str, b: str, fsm_NoAnnotation: set["fsm_State"] = None, fsm_NoAnnotation2: "fsm_FSM" = None):
        self.a = a
        self.b = b
        self.fsm_NoAnnotation = fsm_NoAnnotation if fsm_NoAnnotation is not None else set()
        self.fsm_NoAnnotation2 = fsm_NoAnnotation2
        
    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def fsm_NoAnnotation2(self):
        return self.__fsm_NoAnnotation2

    @fsm_NoAnnotation2.setter
    def fsm_NoAnnotation2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_NoAnnotation__fsm_NoAnnotation2", None)
        self.__fsm_NoAnnotation2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM"):
                opp_val = getattr(old_value, "fsm_FSM", None)
                if opp_val == self:
                    setattr(old_value, "fsm_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM"):
                opp_val = getattr(value, "fsm_FSM", None)
                setattr(value, "fsm_FSM", self)

    @property
    def fsm_NoAnnotation(self):
        return self.__fsm_NoAnnotation

    @fsm_NoAnnotation.setter
    def fsm_NoAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_NoAnnotation__fsm_NoAnnotation", None)
        self.__fsm_NoAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_State"):
                    opp_val = getattr(item, "fsm_State", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_State"):
                    opp_val = getattr(item, "fsm_State", None)
                    
                    setattr(item, "fsm_State", self)
                    

    def j(self, arg0: str, arg1: str):
        # TODO: Implement j method
        pass

    def k(self, arg0: str) -> str:
        # TODO: Implement k method
        pass

class fsm_NoAnnotationSuper:

    pass