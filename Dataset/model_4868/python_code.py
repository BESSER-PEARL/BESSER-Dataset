from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class FlowDesigner_Source(ABC):

    def __init__(self, FlowDesigner_Source: set["FlowDesigner_Event"] = None):
        self.FlowDesigner_Source = FlowDesigner_Source if FlowDesigner_Source is not None else set()
        
    @property
    def FlowDesigner_Source(self):
        return self.__FlowDesigner_Source

    @FlowDesigner_Source.setter
    def FlowDesigner_Source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlowDesigner_Source__FlowDesigner_Source", None)
        self.__FlowDesigner_Source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FlowDesigner_Event2"):
                    opp_val = getattr(item, "FlowDesigner_Event2", None)
                    
                    if opp_val == self:
                        setattr(item, "FlowDesigner_Event2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FlowDesigner_Event2"):
                    opp_val = getattr(item, "FlowDesigner_Event2", None)
                    
                    setattr(item, "FlowDesigner_Event2", self)
                    

    def canBeSource(self, target: Target) -> bool:
        # TODO: Implement canBeSource method
        pass

class FlowDesigner_Target(ABC):

    def __init__(self, FlowDesigner_Target: "FlowDesigner_Event" = None):
        self.FlowDesigner_Target = FlowDesigner_Target
        
    @property
    def FlowDesigner_Target(self):
        return self.__FlowDesigner_Target

    @FlowDesigner_Target.setter
    def FlowDesigner_Target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlowDesigner_Target__FlowDesigner_Target", None)
        self.__FlowDesigner_Target = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowDesigner_Event"):
                opp_val = getattr(old_value, "FlowDesigner_Event", None)
                if opp_val == self:
                    setattr(old_value, "FlowDesigner_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowDesigner_Event"):
                opp_val = getattr(value, "FlowDesigner_Event", None)
                setattr(value, "FlowDesigner_Event", self)

    def canBeTarget(self, source: Source) -> bool:
        # TODO: Implement canBeTarget method
        pass

class FlowDesigner_Event:

    def __init__(self, event: str, action: str, guard: str, FlowDesigner_Event: "FlowDesigner_Target" = None, FlowDesigner_Event2: "FlowDesigner_Source" = None):
        self.event = event
        self.action = action
        self.guard = guard
        self.FlowDesigner_Event = FlowDesigner_Event
        self.FlowDesigner_Event2 = FlowDesigner_Event2
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def FlowDesigner_Event(self):
        return self.__FlowDesigner_Event

    @FlowDesigner_Event.setter
    def FlowDesigner_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlowDesigner_Event__FlowDesigner_Event", None)
        self.__FlowDesigner_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowDesigner_Target"):
                opp_val = getattr(old_value, "FlowDesigner_Target", None)
                if opp_val == self:
                    setattr(old_value, "FlowDesigner_Target", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowDesigner_Target"):
                opp_val = getattr(value, "FlowDesigner_Target", None)
                setattr(value, "FlowDesigner_Target", self)

    @property
    def FlowDesigner_Event2(self):
        return self.__FlowDesigner_Event2

    @FlowDesigner_Event2.setter
    def FlowDesigner_Event2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlowDesigner_Event__FlowDesigner_Event2", None)
        self.__FlowDesigner_Event2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowDesigner_Source"):
                opp_val = getattr(old_value, "FlowDesigner_Source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowDesigner_Source"):
                opp_val = getattr(value, "FlowDesigner_Source", None)
                if opp_val is None:
                    setattr(value, "FlowDesigner_Source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedState:

    pass
class FlowDesigner_ViewState(NamedState):

    def __init__(self, view: str):
        self.view = view
        
    @property
    def view(self) -> str:
        return self.__view

    @view.setter
    def view(self, view: str):
        self.__view = view

class FlowDesigner_ActionState(NamedState):

    pass
class Target:

    pass
class FlowDesigner_FinalState(Target):

    def __init__(self, finalize: str, FlowDesigner_FinalState: "FlowDesigner_Flow" = None):
        self.finalize = finalize
        self.FlowDesigner_FinalState = FlowDesigner_FinalState
        
    @property
    def finalize(self) -> str:
        return self.__finalize

    @finalize.setter
    def finalize(self, finalize: str):
        self.__finalize = finalize

    @property
    def FlowDesigner_FinalState(self):
        return self.__FlowDesigner_FinalState

    @FlowDesigner_FinalState.setter
    def FlowDesigner_FinalState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlowDesigner_FinalState__FlowDesigner_FinalState", None)
        self.__FlowDesigner_FinalState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowDesigner_Flow7"):
                opp_val = getattr(old_value, "FlowDesigner_Flow7", None)
                if opp_val == self:
                    setattr(old_value, "FlowDesigner_Flow7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowDesigner_Flow7"):
                opp_val = getattr(value, "FlowDesigner_Flow7", None)
                setattr(value, "FlowDesigner_Flow7", self)

class Source:

    pass
class FlowDesigner_NamedState(Source, Target):

    def __init__(self, exit: str, entry: str, name: str, activity: str, FlowDesigner_NamedState: "FlowDesigner_Flow" = None):
        self.exit = exit
        self.entry = entry
        self.name = name
        self.activity = activity
        self.FlowDesigner_NamedState = FlowDesigner_NamedState
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def exit(self) -> str:
        return self.__exit

    @exit.setter
    def exit(self, exit: str):
        self.__exit = exit

    @property
    def activity(self) -> str:
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity

    @property
    def entry(self) -> str:
        return self.__entry

    @entry.setter
    def entry(self, entry: str):
        self.__entry = entry

    @property
    def FlowDesigner_NamedState(self):
        return self.__FlowDesigner_NamedState

    @FlowDesigner_NamedState.setter
    def FlowDesigner_NamedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlowDesigner_NamedState__FlowDesigner_NamedState", None)
        self.__FlowDesigner_NamedState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowDesigner_Flow5"):
                opp_val = getattr(old_value, "FlowDesigner_Flow5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowDesigner_Flow5"):
                opp_val = getattr(value, "FlowDesigner_Flow5", None)
                if opp_val is None:
                    setattr(value, "FlowDesigner_Flow5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FlowDesigner_InitialState(Source):

    def __init__(self, initialize: str, FlowDesigner_InitialState: "FlowDesigner_Flow" = None):
        self.initialize = initialize
        self.FlowDesigner_InitialState = FlowDesigner_InitialState
        
    @property
    def initialize(self) -> str:
        return self.__initialize

    @initialize.setter
    def initialize(self, initialize: str):
        self.__initialize = initialize

    @property
    def FlowDesigner_InitialState(self):
        return self.__FlowDesigner_InitialState

    @FlowDesigner_InitialState.setter
    def FlowDesigner_InitialState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlowDesigner_InitialState__FlowDesigner_InitialState", None)
        self.__FlowDesigner_InitialState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowDesigner_Flow"):
                opp_val = getattr(old_value, "FlowDesigner_Flow", None)
                if opp_val == self:
                    setattr(old_value, "FlowDesigner_Flow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowDesigner_Flow"):
                opp_val = getattr(value, "FlowDesigner_Flow", None)
                setattr(value, "FlowDesigner_Flow", self)

class FlowDesigner_Flow:

    def __init__(self, FlowDesigner_Flow: "FlowDesigner_InitialState" = None, FlowDesigner_Flow5: set["FlowDesigner_NamedState"] = None, FlowDesigner_Flow7: "FlowDesigner_FinalState" = None):
        self.FlowDesigner_Flow = FlowDesigner_Flow
        self.FlowDesigner_Flow5 = FlowDesigner_Flow5 if FlowDesigner_Flow5 is not None else set()
        self.FlowDesigner_Flow7 = FlowDesigner_Flow7
        
    @property
    def FlowDesigner_Flow5(self):
        return self.__FlowDesigner_Flow5

    @FlowDesigner_Flow5.setter
    def FlowDesigner_Flow5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlowDesigner_Flow__FlowDesigner_Flow5", None)
        self.__FlowDesigner_Flow5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FlowDesigner_NamedState"):
                    opp_val = getattr(item, "FlowDesigner_NamedState", None)
                    
                    if opp_val == self:
                        setattr(item, "FlowDesigner_NamedState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FlowDesigner_NamedState"):
                    opp_val = getattr(item, "FlowDesigner_NamedState", None)
                    
                    setattr(item, "FlowDesigner_NamedState", self)
                    

    @property
    def FlowDesigner_Flow7(self):
        return self.__FlowDesigner_Flow7

    @FlowDesigner_Flow7.setter
    def FlowDesigner_Flow7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlowDesigner_Flow__FlowDesigner_Flow7", None)
        self.__FlowDesigner_Flow7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowDesigner_FinalState"):
                opp_val = getattr(old_value, "FlowDesigner_FinalState", None)
                if opp_val == self:
                    setattr(old_value, "FlowDesigner_FinalState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowDesigner_FinalState"):
                opp_val = getattr(value, "FlowDesigner_FinalState", None)
                setattr(value, "FlowDesigner_FinalState", self)

    @property
    def FlowDesigner_Flow(self):
        return self.__FlowDesigner_Flow

    @FlowDesigner_Flow.setter
    def FlowDesigner_Flow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlowDesigner_Flow__FlowDesigner_Flow", None)
        self.__FlowDesigner_Flow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowDesigner_InitialState"):
                opp_val = getattr(old_value, "FlowDesigner_InitialState", None)
                if opp_val == self:
                    setattr(old_value, "FlowDesigner_InitialState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowDesigner_InitialState"):
                opp_val = getattr(value, "FlowDesigner_InitialState", None)
                setattr(value, "FlowDesigner_InitialState", self)

    def findStateByName(self, name: str) -> NamedState:
        # TODO: Implement findStateByName method
        pass

    def hasLastState(self) -> bool:
        # TODO: Implement hasLastState method
        pass
