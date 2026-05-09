from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class AbstractState:

    pass
class model_State(AbstractState):

    def __init__(self):
        
        pass
    def onEnter(self):
        # TODO: Implement onEnter method
        pass

    def onExit(self):
        # TODO: Implement onExit method
        pass

class model_Transition:

    def __init__(self, name: str, trigger: str, Transition: "model_AbstractState" = None, outgoings: "model_AbstractState" = None, model_Transition: "model_AbstractState" = None):
        self.name = name
        self.trigger = trigger
        self.Transition = Transition
        self.outgoings = outgoings
        self.model_Transition = model_Transition
        
        pass
    @property
    def trigger(self):
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def model_Transition(self):
        return self.__model_Transition

    @model_Transition.setter
    def model_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__model_Transition", None)
        self.__model_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractState10"):
                opp_val = getattr(old_value, "model_AbstractState10", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractState10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractState10"):
                opp_val = getattr(value, "model_AbstractState10", None)
                setattr(value, "model_AbstractState10", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__Transition", None)
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
    def outgoings(self):
        return self.__outgoings

    @outgoings.setter
    def outgoings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__outgoings", None)
        self.__outgoings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractState8"):
                opp_val = getattr(old_value, "AbstractState8", None)
                if opp_val == self:
                    setattr(old_value, "AbstractState8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractState8"):
                opp_val = getattr(value, "AbstractState8", None)
                setattr(value, "AbstractState8", self)

    def on(self, model_event) :
        # TODO: Implement on method
        pass

    def accepts(self, model_event):
        # TODO: Implement accepts method
        pass

class model_AbstractState:

    def __init__(self, name: bool, states: "model_FiniteStateMachine" = None, model_AbstractState: "model_FiniteStateMachine" = None, AbstractState: "model_FiniteStateMachine" = None, model_AbstractState6: "model_FiniteStateMachine" = None, AbstractState8: "model_Transition" = None, model_AbstractState10: "model_Transition" = None, source: set["model_Transition"] = None):
        self.name = name
        self.states = states
        self.model_AbstractState = model_AbstractState
        self.AbstractState = AbstractState
        self.model_AbstractState6 = model_AbstractState6
        self.AbstractState8 = AbstractState8
        self.model_AbstractState10 = model_AbstractState10
        self.source = source if source is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name


    @property
    def AbstractState(self):
        return self.__AbstractState

    @AbstractState.setter
    def AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__AbstractState", None)
        self.__AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def AbstractState8(self):
        return self.__AbstractState8

    @AbstractState8.setter
    def AbstractState8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__AbstractState8", None)
        self.__AbstractState8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoings"):
                opp_val = getattr(old_value, "outgoings", None)
                if opp_val == self:
                    setattr(old_value, "outgoings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoings"):
                opp_val = getattr(value, "outgoings", None)
                setattr(value, "outgoings", self)

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FiniteStateMachine"):
                opp_val = getattr(old_value, "FiniteStateMachine", None)
                if opp_val == self:
                    setattr(old_value, "FiniteStateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FiniteStateMachine"):
                opp_val = getattr(value, "FiniteStateMachine", None)
                setattr(value, "FiniteStateMachine", self)

    @property
    def model_AbstractState10(self):
        return self.__model_AbstractState10

    @model_AbstractState10.setter
    def model_AbstractState10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__model_AbstractState10", None)
        self.__model_AbstractState10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Transition"):
                opp_val = getattr(old_value, "model_Transition", None)
                if opp_val == self:
                    setattr(old_value, "model_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Transition"):
                opp_val = getattr(value, "model_Transition", None)
                setattr(value, "model_Transition", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__source", None)
        self.__source = value if value is not None else set()
        
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
    def model_AbstractState(self):
        return self.__model_AbstractState

    @model_AbstractState.setter
    def model_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__model_AbstractState", None)
        self.__model_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FiniteStateMachine"):
                opp_val = getattr(old_value, "model_FiniteStateMachine", None)
                if opp_val == self:
                    setattr(old_value, "model_FiniteStateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FiniteStateMachine"):
                opp_val = getattr(value, "model_FiniteStateMachine", None)
                setattr(value, "model_FiniteStateMachine", self)

    @property
    def model_AbstractState6(self):
        return self.__model_AbstractState6

    @model_AbstractState6.setter
    def model_AbstractState6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__model_AbstractState6", None)
        self.__model_AbstractState6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FiniteStateMachine5"):
                opp_val = getattr(old_value, "model_FiniteStateMachine5", None)
                if opp_val == self:
                    setattr(old_value, "model_FiniteStateMachine5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FiniteStateMachine5"):
                opp_val = getattr(value, "model_FiniteStateMachine5", None)
                setattr(value, "model_FiniteStateMachine5", self)

    def onEnter(self):
        # TODO: Implement onEnter method
        pass

    def on(self, model_event) :
        # TODO: Implement on method
        pass

    def onExit(self):
        # TODO: Implement onExit method
        pass

class model_FiniteStateMachine(AbstractState):

    def __init__(self, FiniteStateMachine: "model_AbstractState" = None, model_FiniteStateMachine: "model_AbstractState" = None, parent: set["model_AbstractState"] = None, model_FiniteStateMachine5: "model_AbstractState" = None):
        self.FiniteStateMachine = FiniteStateMachine
        self.model_FiniteStateMachine = model_FiniteStateMachine
        self.parent = parent if parent is not None else set()
        self.model_FiniteStateMachine5 = model_FiniteStateMachine5
        
        pass
    @property
    def model_FiniteStateMachine5(self):
        return self.__model_FiniteStateMachine5

    @model_FiniteStateMachine5.setter
    def model_FiniteStateMachine5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FiniteStateMachine__model_FiniteStateMachine5", None)
        self.__model_FiniteStateMachine5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractState6"):
                opp_val = getattr(old_value, "model_AbstractState6", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractState6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractState6"):
                opp_val = getattr(value, "model_AbstractState6", None)
                setattr(value, "model_AbstractState6", self)

    @property
    def FiniteStateMachine(self):
        return self.__FiniteStateMachine

    @FiniteStateMachine.setter
    def FiniteStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FiniteStateMachine__FiniteStateMachine", None)
        self.__FiniteStateMachine = value
        
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
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FiniteStateMachine__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractState"):
                    opp_val = getattr(item, "AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractState"):
                    opp_val = getattr(item, "AbstractState", None)
                    
                    setattr(item, "AbstractState", self)
                    

    @property
    def model_FiniteStateMachine(self):
        return self.__model_FiniteStateMachine

    @model_FiniteStateMachine.setter
    def model_FiniteStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FiniteStateMachine__model_FiniteStateMachine", None)
        self.__model_FiniteStateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractState"):
                opp_val = getattr(old_value, "model_AbstractState", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractState"):
                opp_val = getattr(value, "model_AbstractState", None)
                setattr(value, "model_AbstractState", self)

    def onEnter(self):
        # TODO: Implement onEnter method
        pass

    def main(self):
        # TODO: Implement main method
        pass

    def on(self, model_event) :
        # TODO: Implement on method
        pass

    def enterInitialState(self, model_args):
        # TODO: Implement enterInitialState method
        pass
