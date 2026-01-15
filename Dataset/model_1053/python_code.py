from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Event:

    pass
class devs_OutputEvent(Event):

    pass
class devs_InputEvent(Event):

    pass
class Transition:

    pass
class devs_ExternalTransition(Transition):

    pass
class devs_InternalTransition(Transition):

    pass
class devs_OutputFunction:

    def __init__(self, name: str, OutputFunction: "devs_AtomicModel" = None, OutputFunction13: "devs_State" = None, OutputFunction19: "devs_OutputEvent" = None, outF: "devs_State" = None, outputFunction: "devs_OutputEvent" = None, outputFunction31: "devs_AtomicModel" = None):
        self.name = name
        self.OutputFunction = OutputFunction
        self.OutputFunction13 = OutputFunction13
        self.OutputFunction19 = OutputFunction19
        self.outF = outF
        self.outputFunction = outputFunction
        self.outputFunction31 = outputFunction31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OutputFunction(self):
        return self.__OutputFunction

    @OutputFunction.setter
    def OutputFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_OutputFunction__OutputFunction", None)
        self.__OutputFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atomicModel6"):
                opp_val = getattr(old_value, "atomicModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atomicModel6"):
                opp_val = getattr(value, "atomicModel6", None)
                if opp_val is None:
                    setattr(value, "atomicModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outF(self):
        return self.__outF

    @outF.setter
    def outF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_OutputFunction__outF", None)
        self.__outF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State28"):
                opp_val = getattr(old_value, "State28", None)
                if opp_val == self:
                    setattr(old_value, "State28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State28"):
                opp_val = getattr(value, "State28", None)
                setattr(value, "State28", self)

    @property
    def outputFunction31(self):
        return self.__outputFunction31

    @outputFunction31.setter
    def outputFunction31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_OutputFunction__outputFunction31", None)
        self.__outputFunction31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AtomicModel32"):
                opp_val = getattr(old_value, "AtomicModel32", None)
                if opp_val == self:
                    setattr(old_value, "AtomicModel32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AtomicModel32"):
                opp_val = getattr(value, "AtomicModel32", None)
                setattr(value, "AtomicModel32", self)

    @property
    def OutputFunction13(self):
        return self.__OutputFunction13

    @OutputFunction13.setter
    def OutputFunction13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_OutputFunction__OutputFunction13", None)
        self.__OutputFunction13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source12"):
                opp_val = getattr(old_value, "source12", None)
                if opp_val == self:
                    setattr(old_value, "source12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source12"):
                opp_val = getattr(value, "source12", None)
                setattr(value, "source12", self)

    @property
    def outputFunction(self):
        return self.__outputFunction

    @outputFunction.setter
    def outputFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_OutputFunction__outputFunction", None)
        self.__outputFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutputEvent"):
                opp_val = getattr(old_value, "OutputEvent", None)
                if opp_val == self:
                    setattr(old_value, "OutputEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutputEvent"):
                opp_val = getattr(value, "OutputEvent", None)
                setattr(value, "OutputEvent", self)

    @property
    def OutputFunction19(self):
        return self.__OutputFunction19

    @OutputFunction19.setter
    def OutputFunction19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_OutputFunction__OutputFunction19", None)
        self.__OutputFunction19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputEvent"):
                opp_val = getattr(old_value, "outputEvent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputEvent"):
                opp_val = getattr(value, "outputEvent", None)
                if opp_val is None:
                    setattr(value, "outputEvent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class devs_Transition:

    def __init__(self, name: str, Transition: "devs_AtomicModel" = None, Transition8: "devs_State" = None, Transition10: "devs_State" = None, out: "devs_State" = None, in: "devs_State" = None, transition: "devs_AtomicModel" = None):
        self.name = name
        self.Transition = Transition
        self.Transition8 = Transition8
        self.Transition10 = Transition10
        self.out = out
        self.in = in
        self.transition = transition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_Transition__transition", None)
        self.__transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AtomicModel25"):
                opp_val = getattr(old_value, "AtomicModel25", None)
                if opp_val == self:
                    setattr(old_value, "AtomicModel25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AtomicModel25"):
                opp_val = getattr(value, "AtomicModel25", None)
                setattr(value, "AtomicModel25", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atomicModel4"):
                opp_val = getattr(old_value, "atomicModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atomicModel4"):
                opp_val = getattr(value, "atomicModel4", None)
                if opp_val is None:
                    setattr(value, "atomicModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def out(self):
        return self.__out

    @out.setter
    def out(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_Transition__out", None)
        self.__out = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State21"):
                opp_val = getattr(old_value, "State21", None)
                if opp_val == self:
                    setattr(old_value, "State21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State21"):
                opp_val = getattr(value, "State21", None)
                setattr(value, "State21", self)

    @property
    def Transition10(self):
        return self.__Transition10

    @Transition10.setter
    def Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_Transition__Transition10", None)
        self.__Transition10 = value
        
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
    def Transition8(self):
        return self.__Transition8

    @Transition8.setter
    def Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_Transition__Transition8", None)
        self.__Transition8 = value
        
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
    def in(self):
        return self.__in

    @in.setter
    def in(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_Transition__in", None)
        self.__in = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State23"):
                opp_val = getattr(old_value, "State23", None)
                if opp_val == self:
                    setattr(old_value, "State23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State23"):
                opp_val = getattr(value, "State23", None)
                setattr(value, "State23", self)

class devs_Event:

    def __init__(self, name: str, Event: "devs_AtomicModel" = None, event: "devs_AtomicModel" = None):
        self.name = name
        self.Event = Event
        self.event = event
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Event(self):
        return self.__Event

    @Event.setter
    def Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_Event__Event", None)
        self.__Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atomicModel2"):
                opp_val = getattr(old_value, "atomicModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atomicModel2"):
                opp_val = getattr(value, "atomicModel2", None)
                if opp_val is None:
                    setattr(value, "atomicModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_Event__event", None)
        self.__event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AtomicModel16"):
                opp_val = getattr(old_value, "AtomicModel16", None)
                if opp_val == self:
                    setattr(old_value, "AtomicModel16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AtomicModel16"):
                opp_val = getattr(value, "AtomicModel16", None)
                setattr(value, "AtomicModel16", self)

class devs_State:

    def __init__(self, lifeTime: float, name: str, State: "devs_AtomicModel" = None, target: set["devs_Transition"] = None, source: set["devs_Transition"] = None, source12: "devs_OutputFunction" = None, state: "devs_AtomicModel" = None, State21: "devs_Transition" = None, State23: "devs_Transition" = None, State28: "devs_OutputFunction" = None):
        self.lifeTime = lifeTime
        self.name = name
        self.State = State
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.source12 = source12
        self.state = state
        self.State21 = State21
        self.State23 = State23
        self.State28 = State28
        
    @property
    def lifeTime(self) -> float:
        return self.__lifeTime

    @lifeTime.setter
    def lifeTime(self, lifeTime: float):
        self.__lifeTime = lifeTime

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atomicModel"):
                opp_val = getattr(old_value, "atomicModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atomicModel"):
                opp_val = getattr(value, "atomicModel", None)
                if opp_val is None:
                    setattr(value, "atomicModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source12(self):
        return self.__source12

    @source12.setter
    def source12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_State__source12", None)
        self.__source12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutputFunction13"):
                opp_val = getattr(old_value, "OutputFunction13", None)
                if opp_val == self:
                    setattr(old_value, "OutputFunction13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutputFunction13"):
                opp_val = getattr(value, "OutputFunction13", None)
                setattr(value, "OutputFunction13", self)

    @property
    def State21(self):
        return self.__State21

    @State21.setter
    def State21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_State__State21", None)
        self.__State21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out"):
                opp_val = getattr(old_value, "out", None)
                if opp_val == self:
                    setattr(old_value, "out", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out"):
                opp_val = getattr(value, "out", None)
                setattr(value, "out", self)

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_State__state", None)
        self.__state = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AtomicModel"):
                opp_val = getattr(old_value, "AtomicModel", None)
                if opp_val == self:
                    setattr(old_value, "AtomicModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AtomicModel"):
                opp_val = getattr(value, "AtomicModel", None)
                setattr(value, "AtomicModel", self)

    @property
    def State23(self):
        return self.__State23

    @State23.setter
    def State23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_State__State23", None)
        self.__State23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "in"):
                opp_val = getattr(old_value, "in", None)
                if opp_val == self:
                    setattr(old_value, "in", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in"):
                opp_val = getattr(value, "in", None)
                setattr(value, "in", self)

    @property
    def State28(self):
        return self.__State28

    @State28.setter
    def State28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_State__State28", None)
        self.__State28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outF"):
                opp_val = getattr(old_value, "outF", None)
                if opp_val == self:
                    setattr(old_value, "outF", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outF"):
                opp_val = getattr(value, "outF", None)
                setattr(value, "outF", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition8"):
                    opp_val = getattr(item, "Transition8", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition8"):
                    opp_val = getattr(item, "Transition8", None)
                    
                    setattr(item, "Transition8", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition10"):
                    opp_val = getattr(item, "Transition10", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition10"):
                    opp_val = getattr(item, "Transition10", None)
                    
                    setattr(item, "Transition10", self)
                    

class devs_AtomicModel:

    def __init__(self, name: str, atomicModel: set["devs_State"] = None, atomicModel2: set["devs_Event"] = None, atomicModel4: set["devs_Transition"] = None, atomicModel6: set["devs_OutputFunction"] = None, AtomicModel: "devs_State" = None, AtomicModel25: "devs_Transition" = None, AtomicModel32: "devs_OutputFunction" = None, AtomicModel16: "devs_Event" = None):
        self.name = name
        self.atomicModel = atomicModel if atomicModel is not None else set()
        self.atomicModel2 = atomicModel2 if atomicModel2 is not None else set()
        self.atomicModel4 = atomicModel4 if atomicModel4 is not None else set()
        self.atomicModel6 = atomicModel6 if atomicModel6 is not None else set()
        self.AtomicModel = AtomicModel
        self.AtomicModel25 = AtomicModel25
        self.AtomicModel32 = AtomicModel32
        self.AtomicModel16 = AtomicModel16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atomicModel(self):
        return self.__atomicModel

    @atomicModel.setter
    def atomicModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_AtomicModel__atomicModel", None)
        self.__atomicModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

    @property
    def AtomicModel32(self):
        return self.__AtomicModel32

    @AtomicModel32.setter
    def AtomicModel32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_AtomicModel__AtomicModel32", None)
        self.__AtomicModel32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputFunction31"):
                opp_val = getattr(old_value, "outputFunction31", None)
                if opp_val == self:
                    setattr(old_value, "outputFunction31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputFunction31"):
                opp_val = getattr(value, "outputFunction31", None)
                setattr(value, "outputFunction31", self)

    @property
    def AtomicModel(self):
        return self.__AtomicModel

    @AtomicModel.setter
    def AtomicModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_AtomicModel__AtomicModel", None)
        self.__AtomicModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state"):
                opp_val = getattr(old_value, "state", None)
                if opp_val == self:
                    setattr(old_value, "state", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state"):
                opp_val = getattr(value, "state", None)
                setattr(value, "state", self)

    @property
    def AtomicModel25(self):
        return self.__AtomicModel25

    @AtomicModel25.setter
    def AtomicModel25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_AtomicModel__AtomicModel25", None)
        self.__AtomicModel25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transition"):
                opp_val = getattr(old_value, "transition", None)
                if opp_val == self:
                    setattr(old_value, "transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transition"):
                opp_val = getattr(value, "transition", None)
                setattr(value, "transition", self)

    @property
    def atomicModel6(self):
        return self.__atomicModel6

    @atomicModel6.setter
    def atomicModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_AtomicModel__atomicModel6", None)
        self.__atomicModel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputFunction"):
                    opp_val = getattr(item, "OutputFunction", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputFunction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputFunction"):
                    opp_val = getattr(item, "OutputFunction", None)
                    
                    setattr(item, "OutputFunction", self)
                    

    @property
    def atomicModel2(self):
        return self.__atomicModel2

    @atomicModel2.setter
    def atomicModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_AtomicModel__atomicModel2", None)
        self.__atomicModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    if opp_val == self:
                        setattr(item, "Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    setattr(item, "Event", self)
                    

    @property
    def atomicModel4(self):
        return self.__atomicModel4

    @atomicModel4.setter
    def atomicModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_AtomicModel__atomicModel4", None)
        self.__atomicModel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def AtomicModel16(self):
        return self.__AtomicModel16

    @AtomicModel16.setter
    def AtomicModel16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_devs_AtomicModel__AtomicModel16", None)
        self.__AtomicModel16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event"):
                opp_val = getattr(old_value, "event", None)
                if opp_val == self:
                    setattr(old_value, "event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event"):
                opp_val = getattr(value, "event", None)
                setattr(value, "event", self)
