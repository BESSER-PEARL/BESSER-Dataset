from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class fiacre_Init(State):

    def __init__(self):
        
    def Assignment(self):
        # TODO: Implement Assignment method
        pass

class EModelElement:

    pass
class fiacre_DataType(EModelElement):

    pass
class fiacre_Process(EModelElement):

    def __init__(self, ID: str, fiacre_Process: set["fiacre_State"] = None, fiacre_Process3: set["fiacre_Transition"] = None, process: set["fiacre_Variable"] = None, fiacre_Process11: "fiacre_Component" = None, Process: "fiacre_Variable" = None, fiacre_Process21: "fiacre_Program" = None):
        self.ID = ID
        self.fiacre_Process = fiacre_Process if fiacre_Process is not None else set()
        self.fiacre_Process3 = fiacre_Process3 if fiacre_Process3 is not None else set()
        self.process = process if process is not None else set()
        self.fiacre_Process11 = fiacre_Process11
        self.Process = Process
        self.fiacre_Process21 = fiacre_Process21
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def process(self):
        return self.__process

    @process.setter
    def process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Process__process", None)
        self.__process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    setattr(item, "Variable", self)
                    

    @property
    def Process(self):
        return self.__Process

    @Process.setter
    def Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Process__Process", None)
        self.__Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variable"):
                opp_val = getattr(old_value, "variable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variable"):
                opp_val = getattr(value, "variable", None)
                if opp_val is None:
                    setattr(value, "variable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacre_Process21(self):
        return self.__fiacre_Process21

    @fiacre_Process21.setter
    def fiacre_Process21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Process__fiacre_Process21", None)
        self.__fiacre_Process21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Program20"):
                opp_val = getattr(old_value, "fiacre_Program20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Program20"):
                opp_val = getattr(value, "fiacre_Program20", None)
                if opp_val is None:
                    setattr(value, "fiacre_Program20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacre_Process3(self):
        return self.__fiacre_Process3

    @fiacre_Process3.setter
    def fiacre_Process3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Process__fiacre_Process3", None)
        self.__fiacre_Process3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacre_Transition"):
                    opp_val = getattr(item, "fiacre_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacre_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacre_Transition"):
                    opp_val = getattr(item, "fiacre_Transition", None)
                    
                    setattr(item, "fiacre_Transition", self)
                    

    @property
    def fiacre_Process11(self):
        return self.__fiacre_Process11

    @fiacre_Process11.setter
    def fiacre_Process11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Process__fiacre_Process11", None)
        self.__fiacre_Process11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Component"):
                opp_val = getattr(old_value, "fiacre_Component", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Component"):
                opp_val = getattr(value, "fiacre_Component", None)
                if opp_val is None:
                    setattr(value, "fiacre_Component", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacre_Process(self):
        return self.__fiacre_Process

    @fiacre_Process.setter
    def fiacre_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Process__fiacre_Process", None)
        self.__fiacre_Process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacre_State"):
                    opp_val = getattr(item, "fiacre_State", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacre_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacre_State"):
                    opp_val = getattr(item, "fiacre_State", None)
                    
                    setattr(item, "fiacre_State", self)
                    

class fiacre_Transition(EModelElement):

    def __init__(self, fiacre_Transition: "fiacre_Process" = None, Transition: "fiacre_State" = None, transition: set["fiacre_State"] = None):
        self.fiacre_Transition = fiacre_Transition
        self.Transition = Transition
        self.transition = transition if transition is not None else set()
        
    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Transition__transition", None)
        self.__transition = value if value is not None else set()
        
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state"):
                opp_val = getattr(old_value, "state", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state"):
                opp_val = getattr(value, "state", None)
                if opp_val is None:
                    setattr(value, "state", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacre_Transition(self):
        return self.__fiacre_Transition

    @fiacre_Transition.setter
    def fiacre_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Transition__fiacre_Transition", None)
        self.__fiacre_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Process3"):
                opp_val = getattr(old_value, "fiacre_Process3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Process3"):
                opp_val = getattr(value, "fiacre_Process3", None)
                if opp_val is None:
                    setattr(value, "fiacre_Process3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def Action(self):
        # TODO: Implement Action method
        pass

    def Trigger(self):
        # TODO: Implement Trigger method
        pass

    def Guard(self):
        # TODO: Implement Guard method
        pass

class fiacre_Program(EModelElement):

    pass
class fiacre_Component(EModelElement):

    def __init__(self, ID: str, fiacre_Component: set["fiacre_Process"] = None, component: set["fiacre_Variable"] = None, Component: "fiacre_Variable" = None, fiacre_Component15: "fiacre_Program" = None):
        self.ID = ID
        self.fiacre_Component = fiacre_Component if fiacre_Component is not None else set()
        self.component = component if component is not None else set()
        self.Component = Component
        self.fiacre_Component15 = fiacre_Component15
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def fiacre_Component(self):
        return self.__fiacre_Component

    @fiacre_Component.setter
    def fiacre_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Component__fiacre_Component", None)
        self.__fiacre_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacre_Process11"):
                    opp_val = getattr(item, "fiacre_Process11", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacre_Process11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacre_Process11"):
                    opp_val = getattr(item, "fiacre_Process11", None)
                    
                    setattr(item, "fiacre_Process11", self)
                    

    @property
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Component__Component", None)
        self.__Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variable9"):
                opp_val = getattr(old_value, "variable9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variable9"):
                opp_val = getattr(value, "variable9", None)
                if opp_val is None:
                    setattr(value, "variable9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacre_Component15(self):
        return self.__fiacre_Component15

    @fiacre_Component15.setter
    def fiacre_Component15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Component__fiacre_Component15", None)
        self.__fiacre_Component15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Program"):
                opp_val = getattr(old_value, "fiacre_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Program"):
                opp_val = getattr(value, "fiacre_Program", None)
                if opp_val is None:
                    setattr(value, "fiacre_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def component(self):
        return self.__component

    @component.setter
    def component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Component__component", None)
        self.__component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable13"):
                    opp_val = getattr(item, "Variable13", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable13"):
                    opp_val = getattr(item, "Variable13", None)
                    
                    setattr(item, "Variable13", self)
                    

class fiacre_State(EModelElement):

    def __init__(self, ID: str, fiacre_State: "fiacre_Process" = None, state: set["fiacre_Transition"] = None, State: "fiacre_Transition" = None):
        self.ID = ID
        self.fiacre_State = fiacre_State
        self.state = state if state is not None else set()
        self.State = State
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def fiacre_State(self):
        return self.__fiacre_State

    @fiacre_State.setter
    def fiacre_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_State__fiacre_State", None)
        self.__fiacre_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Process"):
                opp_val = getattr(old_value, "fiacre_Process", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Process"):
                opp_val = getattr(value, "fiacre_Process", None)
                if opp_val is None:
                    setattr(value, "fiacre_Process", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_State__state", None)
        self.__state = value if value is not None else set()
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transition"):
                opp_val = getattr(old_value, "transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transition"):
                opp_val = getattr(value, "transition", None)
                if opp_val is None:
                    setattr(value, "transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def StateInvariant(self):
        # TODO: Implement StateInvariant method
        pass

class fiacre_Variable(EModelElement):

    def __init__(self, ID: str, Variable: "fiacre_Process" = None, Variable13: "fiacre_Component" = None, fiacre_Variable: "fiacre_DataType" = None, variable: set["fiacre_Process"] = None, variable9: set["fiacre_Component"] = None, fiacre_Variable18: "fiacre_Program" = None):
        self.ID = ID
        self.Variable = Variable
        self.Variable13 = Variable13
        self.fiacre_Variable = fiacre_Variable
        self.variable = variable if variable is not None else set()
        self.variable9 = variable9 if variable9 is not None else set()
        self.fiacre_Variable18 = fiacre_Variable18
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def fiacre_Variable(self):
        return self.__fiacre_Variable

    @fiacre_Variable.setter
    def fiacre_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Variable__fiacre_Variable", None)
        self.__fiacre_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_DataType"):
                opp_val = getattr(old_value, "fiacre_DataType", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_DataType"):
                opp_val = getattr(value, "fiacre_DataType", None)
                setattr(value, "fiacre_DataType", self)

    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Variable__variable", None)
        self.__variable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Process"):
                    opp_val = getattr(item, "Process", None)
                    
                    if opp_val == self:
                        setattr(item, "Process", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process"):
                    opp_val = getattr(item, "Process", None)
                    
                    setattr(item, "Process", self)
                    

    @property
    def Variable13(self):
        return self.__Variable13

    @Variable13.setter
    def Variable13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Variable__Variable13", None)
        self.__Variable13 = value
        
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
    def fiacre_Variable18(self):
        return self.__fiacre_Variable18

    @fiacre_Variable18.setter
    def fiacre_Variable18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Variable__fiacre_Variable18", None)
        self.__fiacre_Variable18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Program17"):
                opp_val = getattr(old_value, "fiacre_Program17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Program17"):
                opp_val = getattr(value, "fiacre_Program17", None)
                if opp_val is None:
                    setattr(value, "fiacre_Program17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def variable9(self):
        return self.__variable9

    @variable9.setter
    def variable9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Variable__variable9", None)
        self.__variable9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Component"):
                    opp_val = getattr(item, "Component", None)
                    
                    if opp_val == self:
                        setattr(item, "Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Component"):
                    opp_val = getattr(item, "Component", None)
                    
                    setattr(item, "Component", self)
                    

    @property
    def Variable(self):
        return self.__Variable

    @Variable.setter
    def Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Variable__Variable", None)
        self.__Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "process"):
                opp_val = getattr(old_value, "process", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "process"):
                opp_val = getattr(value, "process", None)
                if opp_val is None:
                    setattr(value, "process", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
