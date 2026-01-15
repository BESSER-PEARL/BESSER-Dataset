from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class State:

    pass
class StateMachineDiagram_Meta_Event(State):

    pass
class StateMachineDiagram_Meta_Screen(State):

    pass
class StateMachineDiagram_Meta_StateMachine:

    def __init__(self, name: str, StateMachineDiagram_Meta_StateMachine2: set["StateMachineDiagram_Meta_Vertex"] = None, StateMachineDiagram_Meta_StateMachine4: set["StateMachineDiagram_Meta_Transition"] = None, StateMachineDiagram_Meta_StateMachine: "StateMachineDiagram_Meta_Application" = None, StateMachineDiagram_Meta_StateMachine12: "StateMachineDiagram_Meta_State" = None):
        self.name = name
        self.StateMachineDiagram_Meta_StateMachine2 = StateMachineDiagram_Meta_StateMachine2 if StateMachineDiagram_Meta_StateMachine2 is not None else set()
        self.StateMachineDiagram_Meta_StateMachine4 = StateMachineDiagram_Meta_StateMachine4 if StateMachineDiagram_Meta_StateMachine4 is not None else set()
        self.StateMachineDiagram_Meta_StateMachine = StateMachineDiagram_Meta_StateMachine
        self.StateMachineDiagram_Meta_StateMachine12 = StateMachineDiagram_Meta_StateMachine12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StateMachineDiagram_Meta_StateMachine4(self):
        return self.__StateMachineDiagram_Meta_StateMachine4

    @StateMachineDiagram_Meta_StateMachine4.setter
    def StateMachineDiagram_Meta_StateMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineDiagram_Meta_StateMachine__StateMachineDiagram_Meta_StateMachine4", None)
        self.__StateMachineDiagram_Meta_StateMachine4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachineDiagram_Meta_Transition"):
                    opp_val = getattr(item, "StateMachineDiagram_Meta_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachineDiagram_Meta_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachineDiagram_Meta_Transition"):
                    opp_val = getattr(item, "StateMachineDiagram_Meta_Transition", None)
                    
                    setattr(item, "StateMachineDiagram_Meta_Transition", self)
                    

    @property
    def StateMachineDiagram_Meta_StateMachine(self):
        return self.__StateMachineDiagram_Meta_StateMachine

    @StateMachineDiagram_Meta_StateMachine.setter
    def StateMachineDiagram_Meta_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineDiagram_Meta_StateMachine__StateMachineDiagram_Meta_StateMachine", None)
        self.__StateMachineDiagram_Meta_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachineDiagram_Meta_Application"):
                opp_val = getattr(old_value, "StateMachineDiagram_Meta_Application", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachineDiagram_Meta_Application"):
                opp_val = getattr(value, "StateMachineDiagram_Meta_Application", None)
                if opp_val is None:
                    setattr(value, "StateMachineDiagram_Meta_Application", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachineDiagram_Meta_StateMachine12(self):
        return self.__StateMachineDiagram_Meta_StateMachine12

    @StateMachineDiagram_Meta_StateMachine12.setter
    def StateMachineDiagram_Meta_StateMachine12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineDiagram_Meta_StateMachine__StateMachineDiagram_Meta_StateMachine12", None)
        self.__StateMachineDiagram_Meta_StateMachine12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachineDiagram_Meta_State"):
                opp_val = getattr(old_value, "StateMachineDiagram_Meta_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachineDiagram_Meta_State"):
                opp_val = getattr(value, "StateMachineDiagram_Meta_State", None)
                if opp_val is None:
                    setattr(value, "StateMachineDiagram_Meta_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachineDiagram_Meta_StateMachine2(self):
        return self.__StateMachineDiagram_Meta_StateMachine2

    @StateMachineDiagram_Meta_StateMachine2.setter
    def StateMachineDiagram_Meta_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineDiagram_Meta_StateMachine__StateMachineDiagram_Meta_StateMachine2", None)
        self.__StateMachineDiagram_Meta_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachineDiagram_Meta_Vertex"):
                    opp_val = getattr(item, "StateMachineDiagram_Meta_Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachineDiagram_Meta_Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachineDiagram_Meta_Vertex"):
                    opp_val = getattr(item, "StateMachineDiagram_Meta_Vertex", None)
                    
                    setattr(item, "StateMachineDiagram_Meta_Vertex", self)
                    

class StateMachineDiagram_Meta_Application:

    def __init__(self, name: str, StateMachineDiagram_Meta_Application: set["StateMachineDiagram_Meta_StateMachine"] = None):
        self.name = name
        self.StateMachineDiagram_Meta_Application = StateMachineDiagram_Meta_Application if StateMachineDiagram_Meta_Application is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StateMachineDiagram_Meta_Application(self):
        return self.__StateMachineDiagram_Meta_Application

    @StateMachineDiagram_Meta_Application.setter
    def StateMachineDiagram_Meta_Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineDiagram_Meta_Application__StateMachineDiagram_Meta_Application", None)
        self.__StateMachineDiagram_Meta_Application = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachineDiagram_Meta_StateMachine"):
                    opp_val = getattr(item, "StateMachineDiagram_Meta_StateMachine", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachineDiagram_Meta_StateMachine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachineDiagram_Meta_StateMachine"):
                    opp_val = getattr(item, "StateMachineDiagram_Meta_StateMachine", None)
                    
                    setattr(item, "StateMachineDiagram_Meta_StateMachine", self)
                    

class Vertex:

    pass
class StateMachineDiagram_Meta_State(Vertex):

    def __init__(self, name: str, StateMachineDiagram_Meta_State: set["StateMachineDiagram_Meta_StateMachine"] = None):
        self.name = name
        self.StateMachineDiagram_Meta_State = StateMachineDiagram_Meta_State if StateMachineDiagram_Meta_State is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StateMachineDiagram_Meta_State(self):
        return self.__StateMachineDiagram_Meta_State

    @StateMachineDiagram_Meta_State.setter
    def StateMachineDiagram_Meta_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineDiagram_Meta_State__StateMachineDiagram_Meta_State", None)
        self.__StateMachineDiagram_Meta_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachineDiagram_Meta_StateMachine12"):
                    opp_val = getattr(item, "StateMachineDiagram_Meta_StateMachine12", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachineDiagram_Meta_StateMachine12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachineDiagram_Meta_StateMachine12"):
                    opp_val = getattr(item, "StateMachineDiagram_Meta_StateMachine12", None)
                    
                    setattr(item, "StateMachineDiagram_Meta_StateMachine12", self)
                    

class StateMachineDiagram_Meta_Pseudostate(Vertex):

    pass
class StateMachineDiagram_Meta_Transition:

    def __init__(self, name: str, trigger: str, StateMachineDiagram_Meta_Transition: "StateMachineDiagram_Meta_StateMachine" = None, Transition: "StateMachineDiagram_Meta_Vertex" = None, Transition7: "StateMachineDiagram_Meta_Vertex" = None, outgoing: set["StateMachineDiagram_Meta_Vertex"] = None, incoming: set["StateMachineDiagram_Meta_Vertex"] = None):
        self.name = name
        self.trigger = trigger
        self.StateMachineDiagram_Meta_Transition = StateMachineDiagram_Meta_Transition
        self.Transition = Transition
        self.Transition7 = Transition7
        self.outgoing = outgoing if outgoing is not None else set()
        self.incoming = incoming if incoming is not None else set()
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineDiagram_Meta_Transition__outgoing", None)
        self.__outgoing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Vertex"):
                    opp_val = getattr(item, "Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Vertex"):
                    opp_val = getattr(item, "Vertex", None)
                    
                    setattr(item, "Vertex", self)
                    

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineDiagram_Meta_Transition__incoming", None)
        self.__incoming = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Vertex10"):
                    opp_val = getattr(item, "Vertex10", None)
                    
                    if opp_val == self:
                        setattr(item, "Vertex10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Vertex10"):
                    opp_val = getattr(item, "Vertex10", None)
                    
                    setattr(item, "Vertex10", self)
                    

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineDiagram_Meta_Transition__Transition", None)
        self.__Transition = value
        
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
    def Transition7(self):
        return self.__Transition7

    @Transition7.setter
    def Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineDiagram_Meta_Transition__Transition7", None)
        self.__Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachineDiagram_Meta_Transition(self):
        return self.__StateMachineDiagram_Meta_Transition

    @StateMachineDiagram_Meta_Transition.setter
    def StateMachineDiagram_Meta_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineDiagram_Meta_Transition__StateMachineDiagram_Meta_Transition", None)
        self.__StateMachineDiagram_Meta_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachineDiagram_Meta_StateMachine4"):
                opp_val = getattr(old_value, "StateMachineDiagram_Meta_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachineDiagram_Meta_StateMachine4"):
                opp_val = getattr(value, "StateMachineDiagram_Meta_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "StateMachineDiagram_Meta_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StateMachineDiagram_Meta_Vertex(ABC):

    pass