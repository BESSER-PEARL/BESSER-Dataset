from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class mIO(Enum):
    in_ = "in_"
    out = "out"
    inout = "inout"


############################################
# Definition of Classes
############################################

class metaCompo_mTransition:

    def __init__(self, name: str, triggerExp: str, guard: str, action: str, mTransition29: "metaCompo_mState" = None, outgoingTransitions: "metaCompo_mState" = None, incomingTransitions: "metaCompo_mState" = None, metaCompo_mTransition: set["metaCompo_mVariable"] = None, metaCompo_mTransition40: set["metaCompo_mPort"] = None, mTransition: "metaCompo_mState" = None):
        self.name = name
        self.triggerExp = triggerExp
        self.guard = guard
        self.action = action
        self.mTransition29 = mTransition29
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        self.metaCompo_mTransition = metaCompo_mTransition if metaCompo_mTransition is not None else set()
        self.metaCompo_mTransition40 = metaCompo_mTransition40 if metaCompo_mTransition40 is not None else set()
        self.mTransition = mTransition
        
        pass
    @property
    def guard(self):
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard


    @property
    def triggerExp(self):
        return self.__triggerExp

    @triggerExp.setter
    def triggerExp(self, triggerExp: str):
        self.__triggerExp = triggerExp


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mTransition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mState36"):
                opp_val = getattr(old_value, "mState36", None)
                if opp_val == self:
                    setattr(old_value, "mState36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mState36"):
                opp_val = getattr(value, "mState36", None)
                setattr(value, "mState36", self)

    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mTransition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mState34"):
                opp_val = getattr(old_value, "mState34", None)
                if opp_val == self:
                    setattr(old_value, "mState34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mState34"):
                opp_val = getattr(value, "mState34", None)
                setattr(value, "mState34", self)

    @property
    def metaCompo_mTransition40(self):
        return self.__metaCompo_mTransition40

    @metaCompo_mTransition40.setter
    def metaCompo_mTransition40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mTransition__metaCompo_mTransition40", None)
        self.__metaCompo_mTransition40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metaCompo_mPort41"):
                    opp_val = getattr(item, "metaCompo_mPort41", None)
                    
                    if opp_val == self:
                        setattr(item, "metaCompo_mPort41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metaCompo_mPort41"):
                    opp_val = getattr(item, "metaCompo_mPort41", None)
                    
                    setattr(item, "metaCompo_mPort41", self)
                    

    @property
    def mTransition29(self):
        return self.__mTransition29

    @mTransition29.setter
    def mTransition29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mTransition__mTransition29", None)
        self.__mTransition29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "destination"):
                opp_val = getattr(old_value, "destination", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "destination"):
                opp_val = getattr(value, "destination", None)
                if opp_val is None:
                    setattr(value, "destination", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mTransition(self):
        return self.__mTransition

    @mTransition.setter
    def mTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mTransition__mTransition", None)
        self.__mTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metaCompo_mTransition(self):
        return self.__metaCompo_mTransition

    @metaCompo_mTransition.setter
    def metaCompo_mTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mTransition__metaCompo_mTransition", None)
        self.__metaCompo_mTransition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metaCompo_mVariable38"):
                    opp_val = getattr(item, "metaCompo_mVariable38", None)
                    
                    if opp_val == self:
                        setattr(item, "metaCompo_mVariable38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metaCompo_mVariable38"):
                    opp_val = getattr(item, "metaCompo_mVariable38", None)
                    
                    setattr(item, "metaCompo_mVariable38", self)
                    

class metaCompo_mComp:

    def __init__(self, type: str, name: str, metaCompo_mComp: "metaCompo_mComp" = None, metaCompo_mComp0: set["metaCompo_mComp"] = None, metaCompo_mComp3: set["metaCompo_mPort"] = None, component: set["metaCompo_mFSM"] = None, metaCompo_mComp6: set["metaCompo_mVariable"] = None, mComp: "metaCompo_mFSM" = None):
        self.type = type
        self.name = name
        self.metaCompo_mComp = metaCompo_mComp
        self.metaCompo_mComp0 = metaCompo_mComp0 if metaCompo_mComp0 is not None else set()
        self.metaCompo_mComp3 = metaCompo_mComp3 if metaCompo_mComp3 is not None else set()
        self.component = component if component is not None else set()
        self.metaCompo_mComp6 = metaCompo_mComp6 if metaCompo_mComp6 is not None else set()
        self.mComp = mComp
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def metaCompo_mComp0(self):
        return self.__metaCompo_mComp0

    @metaCompo_mComp0.setter
    def metaCompo_mComp0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mComp__metaCompo_mComp0", None)
        self.__metaCompo_mComp0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metaCompo_mComp"):
                    opp_val = getattr(item, "metaCompo_mComp", None)
                    
                    if opp_val == self:
                        setattr(item, "metaCompo_mComp", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metaCompo_mComp"):
                    opp_val = getattr(item, "metaCompo_mComp", None)
                    
                    setattr(item, "metaCompo_mComp", self)
                    

    @property
    def metaCompo_mComp(self):
        return self.__metaCompo_mComp

    @metaCompo_mComp.setter
    def metaCompo_mComp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mComp__metaCompo_mComp", None)
        self.__metaCompo_mComp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mComp0"):
                opp_val = getattr(old_value, "metaCompo_mComp0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mComp0"):
                opp_val = getattr(value, "metaCompo_mComp0", None)
                if opp_val is None:
                    setattr(value, "metaCompo_mComp0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def component(self):
        return self.__component

    @component.setter
    def component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mComp__component", None)
        self.__component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mFSM"):
                    opp_val = getattr(item, "mFSM", None)
                    
                    if opp_val == self:
                        setattr(item, "mFSM", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mFSM"):
                    opp_val = getattr(item, "mFSM", None)
                    
                    setattr(item, "mFSM", self)
                    

    @property
    def mComp(self):
        return self.__mComp

    @mComp.setter
    def mComp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mComp__mComp", None)
        self.__mComp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMs"):
                opp_val = getattr(old_value, "FSMs", None)
                if opp_val == self:
                    setattr(old_value, "FSMs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMs"):
                opp_val = getattr(value, "FSMs", None)
                setattr(value, "FSMs", self)

    @property
    def metaCompo_mComp3(self):
        return self.__metaCompo_mComp3

    @metaCompo_mComp3.setter
    def metaCompo_mComp3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mComp__metaCompo_mComp3", None)
        self.__metaCompo_mComp3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metaCompo_mPort"):
                    opp_val = getattr(item, "metaCompo_mPort", None)
                    
                    if opp_val == self:
                        setattr(item, "metaCompo_mPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metaCompo_mPort"):
                    opp_val = getattr(item, "metaCompo_mPort", None)
                    
                    setattr(item, "metaCompo_mPort", self)
                    

    @property
    def metaCompo_mComp6(self):
        return self.__metaCompo_mComp6

    @metaCompo_mComp6.setter
    def metaCompo_mComp6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mComp__metaCompo_mComp6", None)
        self.__metaCompo_mComp6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metaCompo_mVariable"):
                    opp_val = getattr(item, "metaCompo_mVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "metaCompo_mVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metaCompo_mVariable"):
                    opp_val = getattr(item, "metaCompo_mVariable", None)
                    
                    setattr(item, "metaCompo_mVariable", self)
                    

class metaCompo_mState:

    def __init__(self, name: str, destination: set["metaCompo_mTransition"] = None, metaCompo_mState32: "metaCompo_mState" = None, metaCompo_mState30: set["metaCompo_mState"] = None, mState34: "metaCompo_mTransition" = None, mState36: "metaCompo_mTransition" = None, metaCompo_mState: "metaCompo_mFSM" = None, metaCompo_mState21: "metaCompo_mFSM" = None, mState: "metaCompo_mFSM" = None, states: "metaCompo_mFSM" = None, metaCompo_mState25: set["metaCompo_mVariable"] = None, source: set["metaCompo_mTransition"] = None):
        self.name = name
        self.destination = destination if destination is not None else set()
        self.metaCompo_mState32 = metaCompo_mState32
        self.metaCompo_mState30 = metaCompo_mState30 if metaCompo_mState30 is not None else set()
        self.mState34 = mState34
        self.mState36 = mState36
        self.metaCompo_mState = metaCompo_mState
        self.metaCompo_mState21 = metaCompo_mState21
        self.mState = mState
        self.states = states
        self.metaCompo_mState25 = metaCompo_mState25 if metaCompo_mState25 is not None else set()
        self.source = source if source is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def metaCompo_mState25(self):
        return self.__metaCompo_mState25

    @metaCompo_mState25.setter
    def metaCompo_mState25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mState__metaCompo_mState25", None)
        self.__metaCompo_mState25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metaCompo_mVariable26"):
                    opp_val = getattr(item, "metaCompo_mVariable26", None)
                    
                    if opp_val == self:
                        setattr(item, "metaCompo_mVariable26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metaCompo_mVariable26"):
                    opp_val = getattr(item, "metaCompo_mVariable26", None)
                    
                    setattr(item, "metaCompo_mVariable26", self)
                    

    @property
    def metaCompo_mState32(self):
        return self.__metaCompo_mState32

    @metaCompo_mState32.setter
    def metaCompo_mState32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mState__metaCompo_mState32", None)
        self.__metaCompo_mState32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mState30"):
                opp_val = getattr(old_value, "metaCompo_mState30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mState30"):
                opp_val = getattr(value, "metaCompo_mState30", None)
                if opp_val is None:
                    setattr(value, "metaCompo_mState30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mState__destination", None)
        self.__destination = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mTransition29"):
                    opp_val = getattr(item, "mTransition29", None)
                    
                    if opp_val == self:
                        setattr(item, "mTransition29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mTransition29"):
                    opp_val = getattr(item, "mTransition29", None)
                    
                    setattr(item, "mTransition29", self)
                    

    @property
    def mState(self):
        return self.__mState

    @mState.setter
    def mState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mState__mState", None)
        self.__mState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningFSM"):
                opp_val = getattr(old_value, "owningFSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningFSM"):
                opp_val = getattr(value, "owningFSM", None)
                if opp_val is None:
                    setattr(value, "owningFSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metaCompo_mState(self):
        return self.__metaCompo_mState

    @metaCompo_mState.setter
    def metaCompo_mState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mState__metaCompo_mState", None)
        self.__metaCompo_mState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mFSM18"):
                opp_val = getattr(old_value, "metaCompo_mFSM18", None)
                if opp_val == self:
                    setattr(old_value, "metaCompo_mFSM18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mFSM18"):
                opp_val = getattr(value, "metaCompo_mFSM18", None)
                setattr(value, "metaCompo_mFSM18", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mState__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mTransition"):
                    opp_val = getattr(item, "mTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "mTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mTransition"):
                    opp_val = getattr(item, "mTransition", None)
                    
                    setattr(item, "mTransition", self)
                    

    @property
    def metaCompo_mState21(self):
        return self.__metaCompo_mState21

    @metaCompo_mState21.setter
    def metaCompo_mState21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mState__metaCompo_mState21", None)
        self.__metaCompo_mState21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mFSM20"):
                opp_val = getattr(old_value, "metaCompo_mFSM20", None)
                if opp_val == self:
                    setattr(old_value, "metaCompo_mFSM20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mFSM20"):
                opp_val = getattr(value, "metaCompo_mFSM20", None)
                setattr(value, "metaCompo_mFSM20", self)

    @property
    def metaCompo_mState30(self):
        return self.__metaCompo_mState30

    @metaCompo_mState30.setter
    def metaCompo_mState30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mState__metaCompo_mState30", None)
        self.__metaCompo_mState30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metaCompo_mState32"):
                    opp_val = getattr(item, "metaCompo_mState32", None)
                    
                    if opp_val == self:
                        setattr(item, "metaCompo_mState32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metaCompo_mState32"):
                    opp_val = getattr(item, "metaCompo_mState32", None)
                    
                    setattr(item, "metaCompo_mState32", self)
                    

    @property
    def mState34(self):
        return self.__mState34

    @mState34.setter
    def mState34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mState__mState34", None)
        self.__mState34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingTransitions"):
                opp_val = getattr(old_value, "outgoingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outgoingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingTransitions"):
                opp_val = getattr(value, "outgoingTransitions", None)
                setattr(value, "outgoingTransitions", self)

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mState__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mFSM23"):
                opp_val = getattr(old_value, "mFSM23", None)
                if opp_val == self:
                    setattr(old_value, "mFSM23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mFSM23"):
                opp_val = getattr(value, "mFSM23", None)
                setattr(value, "mFSM23", self)

    @property
    def mState36(self):
        return self.__mState36

    @mState36.setter
    def mState36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mState__mState36", None)
        self.__mState36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingTransitions"):
                opp_val = getattr(old_value, "incomingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "incomingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingTransitions"):
                opp_val = getattr(value, "incomingTransitions", None)
                setattr(value, "incomingTransitions", self)

class metaCompo_mVariable:

    def __init__(self, name: str, type: str, metaCompo_mVariable38: "metaCompo_mTransition" = None, metaCompo_mVariable: "metaCompo_mComp" = None, metaCompo_mVariable12: "metaCompo_mPort" = None, metaCompo_mVariable15: "metaCompo_mFSM" = None, metaCompo_mVariable26: "metaCompo_mState" = None):
        self.name = name
        self.type = type
        self.metaCompo_mVariable38 = metaCompo_mVariable38
        self.metaCompo_mVariable = metaCompo_mVariable
        self.metaCompo_mVariable12 = metaCompo_mVariable12
        self.metaCompo_mVariable15 = metaCompo_mVariable15
        self.metaCompo_mVariable26 = metaCompo_mVariable26
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def metaCompo_mVariable12(self):
        return self.__metaCompo_mVariable12

    @metaCompo_mVariable12.setter
    def metaCompo_mVariable12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mVariable__metaCompo_mVariable12", None)
        self.__metaCompo_mVariable12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mPort11"):
                opp_val = getattr(old_value, "metaCompo_mPort11", None)
                if opp_val == self:
                    setattr(old_value, "metaCompo_mPort11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mPort11"):
                opp_val = getattr(value, "metaCompo_mPort11", None)
                setattr(value, "metaCompo_mPort11", self)

    @property
    def metaCompo_mVariable(self):
        return self.__metaCompo_mVariable

    @metaCompo_mVariable.setter
    def metaCompo_mVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mVariable__metaCompo_mVariable", None)
        self.__metaCompo_mVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mComp6"):
                opp_val = getattr(old_value, "metaCompo_mComp6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mComp6"):
                opp_val = getattr(value, "metaCompo_mComp6", None)
                if opp_val is None:
                    setattr(value, "metaCompo_mComp6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metaCompo_mVariable26(self):
        return self.__metaCompo_mVariable26

    @metaCompo_mVariable26.setter
    def metaCompo_mVariable26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mVariable__metaCompo_mVariable26", None)
        self.__metaCompo_mVariable26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mState25"):
                opp_val = getattr(old_value, "metaCompo_mState25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mState25"):
                opp_val = getattr(value, "metaCompo_mState25", None)
                if opp_val is None:
                    setattr(value, "metaCompo_mState25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metaCompo_mVariable15(self):
        return self.__metaCompo_mVariable15

    @metaCompo_mVariable15.setter
    def metaCompo_mVariable15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mVariable__metaCompo_mVariable15", None)
        self.__metaCompo_mVariable15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mFSM"):
                opp_val = getattr(old_value, "metaCompo_mFSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mFSM"):
                opp_val = getattr(value, "metaCompo_mFSM", None)
                if opp_val is None:
                    setattr(value, "metaCompo_mFSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metaCompo_mVariable38(self):
        return self.__metaCompo_mVariable38

    @metaCompo_mVariable38.setter
    def metaCompo_mVariable38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mVariable__metaCompo_mVariable38", None)
        self.__metaCompo_mVariable38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mTransition"):
                opp_val = getattr(old_value, "metaCompo_mTransition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mTransition"):
                opp_val = getattr(value, "metaCompo_mTransition", None)
                if opp_val is None:
                    setattr(value, "metaCompo_mTransition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metaCompo_mFSM:

    def __init__(self, name: str, metaCompo_mFSM18: "metaCompo_mState" = None, metaCompo_mFSM20: "metaCompo_mState" = None, mFSM: "metaCompo_mComp" = None, FSMs: "metaCompo_mComp" = None, metaCompo_mFSM: set["metaCompo_mVariable"] = None, owningFSM: set["metaCompo_mState"] = None, mFSM23: "metaCompo_mState" = None):
        self.name = name
        self.metaCompo_mFSM18 = metaCompo_mFSM18
        self.metaCompo_mFSM20 = metaCompo_mFSM20
        self.mFSM = mFSM
        self.FSMs = FSMs
        self.metaCompo_mFSM = metaCompo_mFSM if metaCompo_mFSM is not None else set()
        self.owningFSM = owningFSM if owningFSM is not None else set()
        self.mFSM23 = mFSM23
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def metaCompo_mFSM18(self):
        return self.__metaCompo_mFSM18

    @metaCompo_mFSM18.setter
    def metaCompo_mFSM18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mFSM__metaCompo_mFSM18", None)
        self.__metaCompo_mFSM18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mState"):
                opp_val = getattr(old_value, "metaCompo_mState", None)
                if opp_val == self:
                    setattr(old_value, "metaCompo_mState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mState"):
                opp_val = getattr(value, "metaCompo_mState", None)
                setattr(value, "metaCompo_mState", self)

    @property
    def metaCompo_mFSM20(self):
        return self.__metaCompo_mFSM20

    @metaCompo_mFSM20.setter
    def metaCompo_mFSM20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mFSM__metaCompo_mFSM20", None)
        self.__metaCompo_mFSM20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mState21"):
                opp_val = getattr(old_value, "metaCompo_mState21", None)
                if opp_val == self:
                    setattr(old_value, "metaCompo_mState21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mState21"):
                opp_val = getattr(value, "metaCompo_mState21", None)
                setattr(value, "metaCompo_mState21", self)

    @property
    def metaCompo_mFSM(self):
        return self.__metaCompo_mFSM

    @metaCompo_mFSM.setter
    def metaCompo_mFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mFSM__metaCompo_mFSM", None)
        self.__metaCompo_mFSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metaCompo_mVariable15"):
                    opp_val = getattr(item, "metaCompo_mVariable15", None)
                    
                    if opp_val == self:
                        setattr(item, "metaCompo_mVariable15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metaCompo_mVariable15"):
                    opp_val = getattr(item, "metaCompo_mVariable15", None)
                    
                    setattr(item, "metaCompo_mVariable15", self)
                    

    @property
    def mFSM23(self):
        return self.__mFSM23

    @mFSM23.setter
    def mFSM23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mFSM__mFSM23", None)
        self.__mFSM23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states"):
                opp_val = getattr(old_value, "states", None)
                if opp_val == self:
                    setattr(old_value, "states", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states"):
                opp_val = getattr(value, "states", None)
                setattr(value, "states", self)

    @property
    def FSMs(self):
        return self.__FSMs

    @FSMs.setter
    def FSMs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mFSM__FSMs", None)
        self.__FSMs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mComp"):
                opp_val = getattr(old_value, "mComp", None)
                if opp_val == self:
                    setattr(old_value, "mComp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mComp"):
                opp_val = getattr(value, "mComp", None)
                setattr(value, "mComp", self)

    @property
    def mFSM(self):
        return self.__mFSM

    @mFSM.setter
    def mFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mFSM__mFSM", None)
        self.__mFSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component"):
                opp_val = getattr(old_value, "component", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component"):
                opp_val = getattr(value, "component", None)
                if opp_val is None:
                    setattr(value, "component", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owningFSM(self):
        return self.__owningFSM

    @owningFSM.setter
    def owningFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mFSM__owningFSM", None)
        self.__owningFSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mState"):
                    opp_val = getattr(item, "mState", None)
                    
                    if opp_val == self:
                        setattr(item, "mState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mState"):
                    opp_val = getattr(item, "mState", None)
                    
                    setattr(item, "mState", self)
                    

class metaCompo_mPort:

    def __init__(self, name: str, io: str, type: str, metaCompo_mPort41: "metaCompo_mTransition" = None, metaCompo_mPort: "metaCompo_mComp" = None, metaCompo_mPort9: "metaCompo_mPort" = None, metaCompo_mPort7: "metaCompo_mPort" = None, metaCompo_mPort11: "metaCompo_mVariable" = None):
        self.name = name
        self.io = io
        self.type = type
        self.metaCompo_mPort41 = metaCompo_mPort41
        self.metaCompo_mPort = metaCompo_mPort
        self.metaCompo_mPort9 = metaCompo_mPort9
        self.metaCompo_mPort7 = metaCompo_mPort7
        self.metaCompo_mPort11 = metaCompo_mPort11
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def io(self):
        return self.__io

    @io.setter
    def io(self, io: str):
        self.__io = io


    @property
    def metaCompo_mPort41(self):
        return self.__metaCompo_mPort41

    @metaCompo_mPort41.setter
    def metaCompo_mPort41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mPort__metaCompo_mPort41", None)
        self.__metaCompo_mPort41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mTransition40"):
                opp_val = getattr(old_value, "metaCompo_mTransition40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mTransition40"):
                opp_val = getattr(value, "metaCompo_mTransition40", None)
                if opp_val is None:
                    setattr(value, "metaCompo_mTransition40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metaCompo_mPort(self):
        return self.__metaCompo_mPort

    @metaCompo_mPort.setter
    def metaCompo_mPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mPort__metaCompo_mPort", None)
        self.__metaCompo_mPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mComp3"):
                opp_val = getattr(old_value, "metaCompo_mComp3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mComp3"):
                opp_val = getattr(value, "metaCompo_mComp3", None)
                if opp_val is None:
                    setattr(value, "metaCompo_mComp3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metaCompo_mPort7(self):
        return self.__metaCompo_mPort7

    @metaCompo_mPort7.setter
    def metaCompo_mPort7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mPort__metaCompo_mPort7", None)
        self.__metaCompo_mPort7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mPort9"):
                opp_val = getattr(old_value, "metaCompo_mPort9", None)
                if opp_val == self:
                    setattr(old_value, "metaCompo_mPort9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mPort9"):
                opp_val = getattr(value, "metaCompo_mPort9", None)
                setattr(value, "metaCompo_mPort9", self)

    @property
    def metaCompo_mPort9(self):
        return self.__metaCompo_mPort9

    @metaCompo_mPort9.setter
    def metaCompo_mPort9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mPort__metaCompo_mPort9", None)
        self.__metaCompo_mPort9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mPort7"):
                opp_val = getattr(old_value, "metaCompo_mPort7", None)
                if opp_val == self:
                    setattr(old_value, "metaCompo_mPort7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mPort7"):
                opp_val = getattr(value, "metaCompo_mPort7", None)
                setattr(value, "metaCompo_mPort7", self)

    @property
    def metaCompo_mPort11(self):
        return self.__metaCompo_mPort11

    @metaCompo_mPort11.setter
    def metaCompo_mPort11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metaCompo_mPort__metaCompo_mPort11", None)
        self.__metaCompo_mPort11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaCompo_mVariable12"):
                opp_val = getattr(old_value, "metaCompo_mVariable12", None)
                if opp_val == self:
                    setattr(old_value, "metaCompo_mVariable12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaCompo_mVariable12"):
                opp_val = getattr(value, "metaCompo_mVariable12", None)
                setattr(value, "metaCompo_mVariable12", self)
