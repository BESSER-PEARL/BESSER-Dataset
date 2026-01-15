from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Model_PhaseTransition(ABC):

    pass
class Model_Event:

    pass
class PhaseTransition:

    pass
class Model_Port(ABC):

    def __init__(self, portId: str, Model_Port26: "Model_EClassifier" = None, Model_Port: "Model_DEVS" = None, Model_Port58: "Model_Event" = None):
        self.portId = portId
        self.Model_Port26 = Model_Port26
        self.Model_Port = Model_Port
        self.Model_Port58 = Model_Port58
        
    @property
    def portId(self) -> str:
        return self.__portId

    @portId.setter
    def portId(self, portId: str):
        self.__portId = portId

    @property
    def Model_Port58(self):
        return self.__Model_Port58

    @Model_Port58.setter
    def Model_Port58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Port__Model_Port58", None)
        self.__Model_Port58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_Event57"):
                opp_val = getattr(old_value, "Model_Event57", None)
                if opp_val == self:
                    setattr(old_value, "Model_Event57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_Event57"):
                opp_val = getattr(value, "Model_Event57", None)
                setattr(value, "Model_Event57", self)

    @property
    def Model_Port(self):
        return self.__Model_Port

    @Model_Port.setter
    def Model_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Port__Model_Port", None)
        self.__Model_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_DEVS24"):
                opp_val = getattr(old_value, "Model_DEVS24", None)
                if opp_val == self:
                    setattr(old_value, "Model_DEVS24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_DEVS24"):
                opp_val = getattr(value, "Model_DEVS24", None)
                setattr(value, "Model_DEVS24", self)

    @property
    def Model_Port26(self):
        return self.__Model_Port26

    @Model_Port26.setter
    def Model_Port26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Port__Model_Port26", None)
        self.__Model_Port26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_EClassifier"):
                opp_val = getattr(old_value, "Model_EClassifier", None)
                if opp_val == self:
                    setattr(old_value, "Model_EClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_EClassifier"):
                opp_val = getattr(value, "Model_EClassifier", None)
                setattr(value, "Model_EClassifier", self)

class Port:

    pass
class Model_EOC:

    pass
class Model_IC:

    pass
class Model_EIC:

    pass
class Model_Variable:

    def __init__(self, name: str, Model_Variable: "Model_AtomicDEVS" = None, Model_Variable64: "Model_Phase" = None, Model_Variable71: "Model_EClassifier" = None):
        self.name = name
        self.Model_Variable = Model_Variable
        self.Model_Variable64 = Model_Variable64
        self.Model_Variable71 = Model_Variable71
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Model_Variable(self):
        return self.__Model_Variable

    @Model_Variable.setter
    def Model_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Variable__Model_Variable", None)
        self.__Model_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_AtomicDEVS14"):
                opp_val = getattr(old_value, "Model_AtomicDEVS14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_AtomicDEVS14"):
                opp_val = getattr(value, "Model_AtomicDEVS14", None)
                if opp_val is None:
                    setattr(value, "Model_AtomicDEVS14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Model_Variable71(self):
        return self.__Model_Variable71

    @Model_Variable71.setter
    def Model_Variable71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Variable__Model_Variable71", None)
        self.__Model_Variable71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_EClassifier72"):
                opp_val = getattr(old_value, "Model_EClassifier72", None)
                if opp_val == self:
                    setattr(old_value, "Model_EClassifier72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_EClassifier72"):
                opp_val = getattr(value, "Model_EClassifier72", None)
                setattr(value, "Model_EClassifier72", self)

    @property
    def Model_Variable64(self):
        return self.__Model_Variable64

    @Model_Variable64.setter
    def Model_Variable64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Variable__Model_Variable64", None)
        self.__Model_Variable64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_Phase63"):
                opp_val = getattr(old_value, "Model_Phase63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_Phase63"):
                opp_val = getattr(value, "Model_Phase63", None)
                if opp_val is None:
                    setattr(value, "Model_Phase63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Model_Phase:

    def __init__(self, phaseID: str, timeAdvance: float, Model_Phase: "Model_AtomicDEVS" = None, Model_Phase63: set["Model_Variable"] = None, Model_Phase66: "Model_PhaseTransition" = None, Model_Phase69: "Model_PhaseTransition" = None):
        self.phaseID = phaseID
        self.timeAdvance = timeAdvance
        self.Model_Phase = Model_Phase
        self.Model_Phase63 = Model_Phase63 if Model_Phase63 is not None else set()
        self.Model_Phase66 = Model_Phase66
        self.Model_Phase69 = Model_Phase69
        
    @property
    def timeAdvance(self) -> float:
        return self.__timeAdvance

    @timeAdvance.setter
    def timeAdvance(self, timeAdvance: float):
        self.__timeAdvance = timeAdvance

    @property
    def phaseID(self) -> str:
        return self.__phaseID

    @phaseID.setter
    def phaseID(self, phaseID: str):
        self.__phaseID = phaseID

    @property
    def Model_Phase69(self):
        return self.__Model_Phase69

    @Model_Phase69.setter
    def Model_Phase69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Phase__Model_Phase69", None)
        self.__Model_Phase69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_PhaseTransition68"):
                opp_val = getattr(old_value, "Model_PhaseTransition68", None)
                if opp_val == self:
                    setattr(old_value, "Model_PhaseTransition68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_PhaseTransition68"):
                opp_val = getattr(value, "Model_PhaseTransition68", None)
                setattr(value, "Model_PhaseTransition68", self)

    @property
    def Model_Phase63(self):
        return self.__Model_Phase63

    @Model_Phase63.setter
    def Model_Phase63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Phase__Model_Phase63", None)
        self.__Model_Phase63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Model_Variable64"):
                    opp_val = getattr(item, "Model_Variable64", None)
                    
                    if opp_val == self:
                        setattr(item, "Model_Variable64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Model_Variable64"):
                    opp_val = getattr(item, "Model_Variable64", None)
                    
                    setattr(item, "Model_Variable64", self)
                    

    @property
    def Model_Phase(self):
        return self.__Model_Phase

    @Model_Phase.setter
    def Model_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Phase__Model_Phase", None)
        self.__Model_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_AtomicDEVS12"):
                opp_val = getattr(old_value, "Model_AtomicDEVS12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_AtomicDEVS12"):
                opp_val = getattr(value, "Model_AtomicDEVS12", None)
                if opp_val is None:
                    setattr(value, "Model_AtomicDEVS12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Model_Phase66(self):
        return self.__Model_Phase66

    @Model_Phase66.setter
    def Model_Phase66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Phase__Model_Phase66", None)
        self.__Model_Phase66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_PhaseTransition"):
                opp_val = getattr(old_value, "Model_PhaseTransition", None)
                if opp_val == self:
                    setattr(old_value, "Model_PhaseTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_PhaseTransition"):
                opp_val = getattr(value, "Model_PhaseTransition", None)
                setattr(value, "Model_PhaseTransition", self)

class Model_ExtTrans(PhaseTransition):

    pass
class Model_ConfTrans(PhaseTransition):

    pass
class Model_IntTransition(PhaseTransition):

    pass
class DEVS:

    pass
class Model_CoupledDEVS(DEVS):

    pass
class Model_AtomicDEVS(DEVS):

    pass
class Model_OPort(Port):

    pass
class Model_IPort(Port):

    pass
class Model_EClassifier:

    pass
class Model_DEVS(ABC):

    def __init__(self, name: str, Model_DEVS: "Model_DEVS" = None, Model_DEVS0: "Model_DEVS" = None, Model_DEVS3: set["Model_IPort"] = None, Model_DEVS5: set["Model_OPort"] = None, Model_DEVS16: "Model_CoupledDEVS" = None, Model_DEVS24: "Model_Port" = None):
        self.name = name
        self.Model_DEVS = Model_DEVS
        self.Model_DEVS0 = Model_DEVS0
        self.Model_DEVS3 = Model_DEVS3 if Model_DEVS3 is not None else set()
        self.Model_DEVS5 = Model_DEVS5 if Model_DEVS5 is not None else set()
        self.Model_DEVS16 = Model_DEVS16
        self.Model_DEVS24 = Model_DEVS24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Model_DEVS16(self):
        return self.__Model_DEVS16

    @Model_DEVS16.setter
    def Model_DEVS16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_DEVS__Model_DEVS16", None)
        self.__Model_DEVS16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_CoupledDEVS"):
                opp_val = getattr(old_value, "Model_CoupledDEVS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_CoupledDEVS"):
                opp_val = getattr(value, "Model_CoupledDEVS", None)
                if opp_val is None:
                    setattr(value, "Model_CoupledDEVS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Model_DEVS(self):
        return self.__Model_DEVS

    @Model_DEVS.setter
    def Model_DEVS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_DEVS__Model_DEVS", None)
        self.__Model_DEVS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_DEVS0"):
                opp_val = getattr(old_value, "Model_DEVS0", None)
                if opp_val == self:
                    setattr(old_value, "Model_DEVS0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_DEVS0"):
                opp_val = getattr(value, "Model_DEVS0", None)
                setattr(value, "Model_DEVS0", self)

    @property
    def Model_DEVS0(self):
        return self.__Model_DEVS0

    @Model_DEVS0.setter
    def Model_DEVS0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_DEVS__Model_DEVS0", None)
        self.__Model_DEVS0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_DEVS"):
                opp_val = getattr(old_value, "Model_DEVS", None)
                if opp_val == self:
                    setattr(old_value, "Model_DEVS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_DEVS"):
                opp_val = getattr(value, "Model_DEVS", None)
                setattr(value, "Model_DEVS", self)

    @property
    def Model_DEVS3(self):
        return self.__Model_DEVS3

    @Model_DEVS3.setter
    def Model_DEVS3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_DEVS__Model_DEVS3", None)
        self.__Model_DEVS3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Model_IPort"):
                    opp_val = getattr(item, "Model_IPort", None)
                    
                    if opp_val == self:
                        setattr(item, "Model_IPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Model_IPort"):
                    opp_val = getattr(item, "Model_IPort", None)
                    
                    setattr(item, "Model_IPort", self)
                    

    @property
    def Model_DEVS5(self):
        return self.__Model_DEVS5

    @Model_DEVS5.setter
    def Model_DEVS5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_DEVS__Model_DEVS5", None)
        self.__Model_DEVS5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Model_OPort"):
                    opp_val = getattr(item, "Model_OPort", None)
                    
                    if opp_val == self:
                        setattr(item, "Model_OPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Model_OPort"):
                    opp_val = getattr(item, "Model_OPort", None)
                    
                    setattr(item, "Model_OPort", self)
                    

    @property
    def Model_DEVS24(self):
        return self.__Model_DEVS24

    @Model_DEVS24.setter
    def Model_DEVS24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_DEVS__Model_DEVS24", None)
        self.__Model_DEVS24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model_Port"):
                opp_val = getattr(old_value, "Model_Port", None)
                if opp_val == self:
                    setattr(old_value, "Model_Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model_Port"):
                opp_val = getattr(value, "Model_Port", None)
                setattr(value, "Model_Port", self)
