from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class UMLRealTimeStateMach_RTTrigger:

    pass
class UMLRealTimeStateMach_Pseudostate:

    pass
class UMLRealTimeStateMach_Operation:

    pass
class UMLRealTimeStateMach_RTPseudostate:

    def __init__(self, UMLRealTimeStateMach_RTPseudostate: "UMLRealTimeStateMach_Pseudostate" = None):
        self.UMLRealTimeStateMach_RTPseudostate = UMLRealTimeStateMach_RTPseudostate
        
        pass
    @property
    def UMLRealTimeStateMach_RTPseudostate(self):
        return self.__UMLRealTimeStateMach_RTPseudostate

    @UMLRealTimeStateMach_RTPseudostate.setter
    def UMLRealTimeStateMach_RTPseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLRealTimeStateMach_RTPseudostate__UMLRealTimeStateMach_RTPseudostate", None)
        self.__UMLRealTimeStateMach_RTPseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLRealTimeStateMach_Pseudostate"):
                opp_val = getattr(old_value, "UMLRealTimeStateMach_Pseudostate", None)
                if opp_val == self:
                    setattr(old_value, "UMLRealTimeStateMach_Pseudostate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLRealTimeStateMach_Pseudostate"):
                opp_val = getattr(value, "UMLRealTimeStateMach_Pseudostate", None)
                setattr(value, "UMLRealTimeStateMach_Pseudostate", self)

    def RTstatemachinesdonotsupportconcurrencyorshallowhistory(self, UMLRealTimeStateMach_diagnostics, UMLRealTimeStateMach_context) :
        # TODO: Implement RTstatemachinesdonotsupportconcurrencyorshallowhistory method
        pass

class UMLRealTimeStateMach_State:

    pass
class UMLRealTimeStateMach_RTState:

    def __init__(self, UMLRealTimeStateMach_RTState: "UMLRealTimeStateMach_State" = None):
        self.UMLRealTimeStateMach_RTState = UMLRealTimeStateMach_RTState
        
        pass
    @property
    def UMLRealTimeStateMach_RTState(self):
        return self.__UMLRealTimeStateMach_RTState

    @UMLRealTimeStateMach_RTState.setter
    def UMLRealTimeStateMach_RTState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLRealTimeStateMach_RTState__UMLRealTimeStateMach_RTState", None)
        self.__UMLRealTimeStateMach_RTState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLRealTimeStateMach_State"):
                opp_val = getattr(old_value, "UMLRealTimeStateMach_State", None)
                if opp_val == self:
                    setattr(old_value, "UMLRealTimeStateMach_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLRealTimeStateMach_State"):
                opp_val = getattr(value, "UMLRealTimeStateMach_State", None)
                setattr(value, "UMLRealTimeStateMach_State", self)

    def AcomposteRTstatehasexactlyoneregion(self, UMLRealTimeStateMach_diagnostics, UMLRealTimeStateMach_context) :
        # TODO: Implement AcomposteRTstatehasexactlyoneregion method
        pass

    def Constraint5(self, UMLRealTimeStateMach_diagnostics, UMLRealTimeStateMach_context) :
        # TODO: Implement Constraint5 method
        pass

    def RTstatemachinescannothaveanydeferredtriggers(self, UMLRealTimeStateMach_diagnostics, UMLRealTimeStateMach_context) :
        # TODO: Implement RTstatemachinescannothaveanydeferredtriggers method
        pass

    def RTstatemachinesdonotsupportdoactivities(self, UMLRealTimeStateMach_diagnostics, UMLRealTimeStateMach_context) :
        # TODO: Implement RTstatemachinesdonotsupportdoactivities method
        pass

    def RTdoesnotsupportsubmachinestates(self, UMLRealTimeStateMach_diagnostics, UMLRealTimeStateMach_context) :
        # TODO: Implement RTdoesnotsupportsubmachinestates method
        pass

class UMLRealTimeStateMach_Region:

    pass
class UMLRealTimeStateMach_RTRegion:

    def __init__(self, UMLRealTimeStateMach_RTRegion: "UMLRealTimeStateMach_Region" = None):
        self.UMLRealTimeStateMach_RTRegion = UMLRealTimeStateMach_RTRegion
        
        pass
    @property
    def UMLRealTimeStateMach_RTRegion(self):
        return self.__UMLRealTimeStateMach_RTRegion

    @UMLRealTimeStateMach_RTRegion.setter
    def UMLRealTimeStateMach_RTRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLRealTimeStateMach_RTRegion__UMLRealTimeStateMach_RTRegion", None)
        self.__UMLRealTimeStateMach_RTRegion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLRealTimeStateMach_Region"):
                opp_val = getattr(old_value, "UMLRealTimeStateMach_Region", None)
                if opp_val == self:
                    setattr(old_value, "UMLRealTimeStateMach_Region", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLRealTimeStateMach_Region"):
                opp_val = getattr(value, "UMLRealTimeStateMach_Region", None)
                setattr(value, "UMLRealTimeStateMach_Region", self)

    def RegionsinRTstatemachinescannothaveafinalstate(self, UMLRealTimeStateMach_context, UMLRealTimeStateMach_diagnostics) :
        # TODO: Implement RegionsinRTstatemachinescannothaveafinalstate method
        pass

class UMLRealTimeStateMach_StateMachine:

    pass
class UMLRealTimeStateMach_RTStateMachine:

    def __init__(self, isPassive: str, UMLRealTimeStateMach_RTStateMachine: "UMLRealTimeStateMach_StateMachine" = None):
        self.isPassive = isPassive
        self.UMLRealTimeStateMach_RTStateMachine = UMLRealTimeStateMach_RTStateMachine
        
        pass
    @property
    def isPassive(self):
        return self.__isPassive

    @isPassive.setter
    def isPassive(self, isPassive: str):
        self.__isPassive = isPassive


    @property
    def UMLRealTimeStateMach_RTStateMachine(self):
        return self.__UMLRealTimeStateMach_RTStateMachine

    @UMLRealTimeStateMach_RTStateMachine.setter
    def UMLRealTimeStateMach_RTStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLRealTimeStateMach_RTStateMachine__UMLRealTimeStateMach_RTStateMachine", None)
        self.__UMLRealTimeStateMach_RTStateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLRealTimeStateMach_StateMachine"):
                opp_val = getattr(old_value, "UMLRealTimeStateMach_StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "UMLRealTimeStateMach_StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLRealTimeStateMach_StateMachine"):
                opp_val = getattr(value, "UMLRealTimeStateMach_StateMachine", None)
                setattr(value, "UMLRealTimeStateMach_StateMachine", self)

    def RTstatemachinesdonothaveparametersorparametersets(self, UMLRealTimeStateMach_context, UMLRealTimeStateMach_diagnostics) :
        # TODO: Implement RTstatemachinesdonothaveparametersorparametersets method
        pass

    def RTstatemachinesmusthaveacontextanditmustbeaClass(self, UMLRealTimeStateMach_diagnostics, UMLRealTimeStateMach_context) :
        # TODO: Implement RTstatemachinesmusthaveacontextanditmustbeaClass method
        pass

    def AnRTstatemachineisneverreentrant(self, UMLRealTimeStateMach_context, UMLRealTimeStateMach_diagnostics) :
        # TODO: Implement AnRTstatemachineisneverreentrant method
        pass

    def Passivestatemachineareonlyallowedonpassivedataclasses(self, UMLRealTimeStateMach_context, UMLRealTimeStateMach_diagnostics) :
        # TODO: Implement Passivestatemachineareonlyallowedonpassivedataclasses method
        pass

    def AnRTstatemachinehasexactlyoneregion(self, UMLRealTimeStateMach_diagnostics, UMLRealTimeStateMach_context) :
        # TODO: Implement AnRTstatemachinehasexactlyoneregion method
        pass
