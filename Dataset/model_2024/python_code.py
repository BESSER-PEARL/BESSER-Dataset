from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class traces_Value:

    def __init__(self, clockMin: float, clockMax: float, valueMin: float, valueMax: float, Value: "traces_Variable" = None, values: "traces_Variable" = None):
        self.clockMin = clockMin
        self.clockMax = clockMax
        self.valueMin = valueMin
        self.valueMax = valueMax
        self.Value = Value
        self.values = values
        
    @property
    def clockMax(self) -> float:
        return self.__clockMax

    @clockMax.setter
    def clockMax(self, clockMax: float):
        self.__clockMax = clockMax

    @property
    def valueMax(self) -> float:
        return self.__valueMax

    @valueMax.setter
    def valueMax(self, valueMax: float):
        self.__valueMax = valueMax

    @property
    def clockMin(self) -> float:
        return self.__clockMin

    @clockMin.setter
    def clockMin(self, clockMin: float):
        self.__clockMin = clockMin

    @property
    def valueMin(self) -> float:
        return self.__valueMin

    @valueMin.setter
    def valueMin(self, valueMin: float):
        self.__valueMin = valueMin

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_Value__values", None)
        self.__values = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable4"):
                opp_val = getattr(old_value, "Variable4", None)
                if opp_val == self:
                    setattr(old_value, "Variable4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable4"):
                opp_val = getattr(value, "Variable4", None)
                setattr(value, "Variable4", self)

    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_Value__Value", None)
        self.__Value = value
        
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

class traces_Variable:

    def __init__(self, name: str, Variable: "traces_SimulatorRun" = None, variables: "traces_SimulatorRun" = None, variable: set["traces_Value"] = None, Variable4: "traces_Value" = None):
        self.name = name
        self.Variable = Variable
        self.variables = variables
        self.variable = variable if variable is not None else set()
        self.Variable4 = Variable4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Variable4(self):
        return self.__Variable4

    @Variable4.setter
    def Variable4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_Variable__Variable4", None)
        self.__Variable4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "values"):
                opp_val = getattr(old_value, "values", None)
                if opp_val == self:
                    setattr(old_value, "values", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "values"):
                opp_val = getattr(value, "values", None)
                setattr(value, "values", self)

    @property
    def variables(self):
        return self.__variables

    @variables.setter
    def variables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_Variable__variables", None)
        self.__variables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimulatorRun"):
                opp_val = getattr(old_value, "SimulatorRun", None)
                if opp_val == self:
                    setattr(old_value, "SimulatorRun", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimulatorRun"):
                opp_val = getattr(value, "SimulatorRun", None)
                setattr(value, "SimulatorRun", self)

    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_Variable__variable", None)
        self.__variable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Value"):
                    opp_val = getattr(item, "Value", None)
                    
                    if opp_val == self:
                        setattr(item, "Value", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Value"):
                    opp_val = getattr(item, "Value", None)
                    
                    setattr(item, "Value", self)
                    

    @property
    def Variable(self):
        return self.__Variable

    @Variable.setter
    def Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_Variable__Variable", None)
        self.__Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "run"):
                opp_val = getattr(old_value, "run", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "run"):
                opp_val = getattr(value, "run", None)
                if opp_val is None:
                    setattr(value, "run", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class traces_SimulatorRun:

    def __init__(self, id: int, timestamp: date, behaviorName: str, run: set["traces_Variable"] = None, SimulatorRun: "traces_Variable" = None):
        self.id = id
        self.timestamp = timestamp
        self.behaviorName = behaviorName
        self.run = run if run is not None else set()
        self.SimulatorRun = SimulatorRun
        
    @property
    def behaviorName(self) -> str:
        return self.__behaviorName

    @behaviorName.setter
    def behaviorName(self, behaviorName: str):
        self.__behaviorName = behaviorName

    @property
    def timestamp(self) -> date:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: date):
        self.__timestamp = timestamp

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def SimulatorRun(self):
        return self.__SimulatorRun

    @SimulatorRun.setter
    def SimulatorRun(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_SimulatorRun__SimulatorRun", None)
        self.__SimulatorRun = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variables"):
                opp_val = getattr(old_value, "variables", None)
                if opp_val == self:
                    setattr(old_value, "variables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variables"):
                opp_val = getattr(value, "variables", None)
                setattr(value, "variables", self)

    @property
    def run(self):
        return self.__run

    @run.setter
    def run(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_SimulatorRun__run", None)
        self.__run = value if value is not None else set()
        
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
                    
