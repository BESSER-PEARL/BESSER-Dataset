from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_State:

    def __init__(self, name: str, myDsl_State8: "myDsl_XExpression" = None, myDsl_State10: set["myDsl_Transition"] = None, myDsl_State: "myDsl_Statemachine" = None, myDsl_State16: "myDsl_Transition" = None):
        self.name = name
        self.myDsl_State8 = myDsl_State8
        self.myDsl_State10 = myDsl_State10 if myDsl_State10 is not None else set()
        self.myDsl_State = myDsl_State
        self.myDsl_State16 = myDsl_State16
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def myDsl_State8(self):
        return self.__myDsl_State8

    @myDsl_State8.setter
    def myDsl_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_State__myDsl_State8", None)
        self.__myDsl_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_XExpression"):
                opp_val = getattr(old_value, "myDsl_XExpression", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_XExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_XExpression"):
                opp_val = getattr(value, "myDsl_XExpression", None)
                setattr(value, "myDsl_XExpression", self)

    @property
    def myDsl_State(self):
        return self.__myDsl_State

    @myDsl_State.setter
    def myDsl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_State__myDsl_State", None)
        self.__myDsl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statemachine4"):
                opp_val = getattr(old_value, "myDsl_Statemachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statemachine4"):
                opp_val = getattr(value, "myDsl_Statemachine4", None)
                if opp_val is None:
                    setattr(value, "myDsl_Statemachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_State16(self):
        return self.__myDsl_State16

    @myDsl_State16.setter
    def myDsl_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_State__myDsl_State16", None)
        self.__myDsl_State16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Transition15"):
                opp_val = getattr(old_value, "myDsl_Transition15", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Transition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Transition15"):
                opp_val = getattr(value, "myDsl_Transition15", None)
                setattr(value, "myDsl_Transition15", self)

    @property
    def myDsl_State10(self):
        return self.__myDsl_State10

    @myDsl_State10.setter
    def myDsl_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_State__myDsl_State10", None)
        self.__myDsl_State10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Transition"):
                    opp_val = getattr(item, "myDsl_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Transition"):
                    opp_val = getattr(item, "myDsl_Transition", None)
                    
                    setattr(item, "myDsl_Transition", self)
                    

class myDsl_Transition:

    pass
class myDsl_XExpression:

    pass
class myDsl_JvmTypeReference:

    pass
class myDsl_Service:

    def __init__(self, name: str, myDsl_Service: "myDsl_Statemachine" = None, myDsl_Service6: "myDsl_JvmTypeReference" = None):
        self.name = name
        self.myDsl_Service = myDsl_Service
        self.myDsl_Service6 = myDsl_Service6
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def myDsl_Service(self):
        return self.__myDsl_Service

    @myDsl_Service.setter
    def myDsl_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service", None)
        self.__myDsl_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statemachine2"):
                opp_val = getattr(old_value, "myDsl_Statemachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statemachine2"):
                opp_val = getattr(value, "myDsl_Statemachine2", None)
                if opp_val is None:
                    setattr(value, "myDsl_Statemachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Service6(self):
        return self.__myDsl_Service6

    @myDsl_Service6.setter
    def myDsl_Service6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service6", None)
        self.__myDsl_Service6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_JvmTypeReference"):
                opp_val = getattr(old_value, "myDsl_JvmTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_JvmTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_JvmTypeReference"):
                opp_val = getattr(value, "myDsl_JvmTypeReference", None)
                setattr(value, "myDsl_JvmTypeReference", self)

class myDsl_Event:

    def __init__(self, resetEvent: bool, name: str, myDsl_Event: "myDsl_Statemachine" = None, myDsl_Event13: "myDsl_Transition" = None):
        self.resetEvent = resetEvent
        self.name = name
        self.myDsl_Event = myDsl_Event
        self.myDsl_Event13 = myDsl_Event13
        
        pass
    @property
    def resetEvent(self):
        return self.__resetEvent

    @resetEvent.setter
    def resetEvent(self, resetEvent: bool):
        self.__resetEvent = resetEvent


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def myDsl_Event(self):
        return self.__myDsl_Event

    @myDsl_Event.setter
    def myDsl_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Event__myDsl_Event", None)
        self.__myDsl_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statemachine"):
                opp_val = getattr(old_value, "myDsl_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statemachine"):
                opp_val = getattr(value, "myDsl_Statemachine", None)
                if opp_val is None:
                    setattr(value, "myDsl_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Event13(self):
        return self.__myDsl_Event13

    @myDsl_Event13.setter
    def myDsl_Event13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Event__myDsl_Event13", None)
        self.__myDsl_Event13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Transition12"):
                opp_val = getattr(old_value, "myDsl_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Transition12"):
                opp_val = getattr(value, "myDsl_Transition12", None)
                setattr(value, "myDsl_Transition12", self)

class myDsl_Statemachine:

    pass