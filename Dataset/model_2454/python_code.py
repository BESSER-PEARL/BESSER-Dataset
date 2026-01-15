from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ConfigTypeType1(Enum):
    field = "field"
    bean = "bean"
    constructor = "constructor"
    configurationProperty = "configurationProperty"
class ConfigType(Enum):
    field = "field"
    bean = "bean"
    constructor = "constructor"
    configurationProperty = "configurationProperty"
class ConfigTypeType(Enum):
    field = "field"
    bean = "bean"
    constructor = "constructor"
    configurationProperty = "configurationProperty"
class SignalType(Enum):
    unsynchronized = "unsynchronized"
    never = "never"
    first = "first"
    firstWait = "firstWait"
    last = "last"
    lastWait = "lastWait"
class BooleanType(Enum):
    yes = "yes"
    no = "no"
    true = "true"
    false = "false"
    on = "on"
    off = "off"
class TypeTypeMember1(Enum):
    nodeEnter = "nodeEnter"
    nodeLeave = "nodeLeave"
    processStart = "processStart"
    processEnd = "processEnd"
    taskCreate = "taskCreate"
    taskAssign = "taskAssign"
    taskStart = "taskStart"
    taskEnd = "taskEnd"
    beforeSignal = "beforeSignal"
    afterSignal = "afterSignal"
    superstateEnter = "superstateEnter"
    superstateLeave = "superstateLeave"
    timerCreate = "timerCreate"
    subprocessCreated = "subprocessCreated"
    subprocessEnd = "subprocessEnd"
class PriorityTypeMember0(Enum):
    highest = "highest"
    high = "high"
    normal = "normal"
    low = "low"
    lowest = "lowest"


############################################
# Definition of Classes
############################################

class jpdl31_SubProcessType:

    def __init__(self, name: str, version: str, jpdl31_SubProcessType: "jpdl31_ProcessStateType" = None):
        self.name = name
        self.version = version
        self.jpdl31_SubProcessType = jpdl31_SubProcessType
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl31_SubProcessType(self):
        return self.__jpdl31_SubProcessType

    @jpdl31_SubProcessType.setter
    def jpdl31_SubProcessType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SubProcessType__jpdl31_SubProcessType", None)
        self.__jpdl31_SubProcessType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessStateType199"):
                opp_val = getattr(old_value, "jpdl31_ProcessStateType199", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessStateType199"):
                opp_val = getattr(value, "jpdl31_ProcessStateType199", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessStateType199", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_TaskNodeType:

    def __init__(self, group: str, async: str, createTasks: str, endTasks: str, name: str, signal: str, jpdl31_TaskNodeType: "jpdl31_DocumentRoot" = None, jpdl31_TaskNodeType158: "jpdl31_ProcessDefinitionType" = None, jpdl31_TaskNodeType247: "jpdl31_SuperStateType" = None, jpdl31_TaskNodeType282: set["jpdl31_TaskType"] = None, jpdl31_TaskNodeType285: set["jpdl31_EventType"] = None, jpdl31_TaskNodeType288: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_TaskNodeType294: set["jpdl31_TransitionType"] = None, jpdl31_TaskNodeType291: set["jpdl31_TimerType"] = None):
        self.group = group
        self.async = async
        self.createTasks = createTasks
        self.endTasks = endTasks
        self.name = name
        self.signal = signal
        self.jpdl31_TaskNodeType = jpdl31_TaskNodeType
        self.jpdl31_TaskNodeType158 = jpdl31_TaskNodeType158
        self.jpdl31_TaskNodeType247 = jpdl31_TaskNodeType247
        self.jpdl31_TaskNodeType282 = jpdl31_TaskNodeType282 if jpdl31_TaskNodeType282 is not None else set()
        self.jpdl31_TaskNodeType285 = jpdl31_TaskNodeType285 if jpdl31_TaskNodeType285 is not None else set()
        self.jpdl31_TaskNodeType288 = jpdl31_TaskNodeType288 if jpdl31_TaskNodeType288 is not None else set()
        self.jpdl31_TaskNodeType294 = jpdl31_TaskNodeType294 if jpdl31_TaskNodeType294 is not None else set()
        self.jpdl31_TaskNodeType291 = jpdl31_TaskNodeType291 if jpdl31_TaskNodeType291 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def createTasks(self) -> str:
        return self.__createTasks

    @createTasks.setter
    def createTasks(self, createTasks: str):
        self.__createTasks = createTasks

    @property
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

    @property
    def signal(self) -> str:
        return self.__signal

    @signal.setter
    def signal(self, signal: str):
        self.__signal = signal

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def endTasks(self) -> str:
        return self.__endTasks

    @endTasks.setter
    def endTasks(self, endTasks: str):
        self.__endTasks = endTasks

    @property
    def jpdl31_TaskNodeType285(self):
        return self.__jpdl31_TaskNodeType285

    @jpdl31_TaskNodeType285.setter
    def jpdl31_TaskNodeType285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskNodeType__jpdl31_TaskNodeType285", None)
        self.__jpdl31_TaskNodeType285 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType286"):
                    opp_val = getattr(item, "jpdl31_EventType286", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType286", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType286"):
                    opp_val = getattr(item, "jpdl31_EventType286", None)
                    
                    setattr(item, "jpdl31_EventType286", self)
                    

    @property
    def jpdl31_TaskNodeType294(self):
        return self.__jpdl31_TaskNodeType294

    @jpdl31_TaskNodeType294.setter
    def jpdl31_TaskNodeType294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskNodeType__jpdl31_TaskNodeType294", None)
        self.__jpdl31_TaskNodeType294 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType295"):
                    opp_val = getattr(item, "jpdl31_TransitionType295", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType295", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType295"):
                    opp_val = getattr(item, "jpdl31_TransitionType295", None)
                    
                    setattr(item, "jpdl31_TransitionType295", self)
                    

    @property
    def jpdl31_TaskNodeType282(self):
        return self.__jpdl31_TaskNodeType282

    @jpdl31_TaskNodeType282.setter
    def jpdl31_TaskNodeType282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskNodeType__jpdl31_TaskNodeType282", None)
        self.__jpdl31_TaskNodeType282 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TaskType283"):
                    opp_val = getattr(item, "jpdl31_TaskType283", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TaskType283", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TaskType283"):
                    opp_val = getattr(item, "jpdl31_TaskType283", None)
                    
                    setattr(item, "jpdl31_TaskType283", self)
                    

    @property
    def jpdl31_TaskNodeType158(self):
        return self.__jpdl31_TaskNodeType158

    @jpdl31_TaskNodeType158.setter
    def jpdl31_TaskNodeType158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskNodeType__jpdl31_TaskNodeType158", None)
        self.__jpdl31_TaskNodeType158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType157"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType157"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType157", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TaskNodeType291(self):
        return self.__jpdl31_TaskNodeType291

    @jpdl31_TaskNodeType291.setter
    def jpdl31_TaskNodeType291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskNodeType__jpdl31_TaskNodeType291", None)
        self.__jpdl31_TaskNodeType291 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType292"):
                    opp_val = getattr(item, "jpdl31_TimerType292", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType292", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType292"):
                    opp_val = getattr(item, "jpdl31_TimerType292", None)
                    
                    setattr(item, "jpdl31_TimerType292", self)
                    

    @property
    def jpdl31_TaskNodeType(self):
        return self.__jpdl31_TaskNodeType

    @jpdl31_TaskNodeType.setter
    def jpdl31_TaskNodeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskNodeType__jpdl31_TaskNodeType", None)
        self.__jpdl31_TaskNodeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot62"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot62"):
                opp_val = getattr(value, "jpdl31_DocumentRoot62", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TaskNodeType288(self):
        return self.__jpdl31_TaskNodeType288

    @jpdl31_TaskNodeType288.setter
    def jpdl31_TaskNodeType288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskNodeType__jpdl31_TaskNodeType288", None)
        self.__jpdl31_TaskNodeType288 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType289"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType289", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType289", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType289"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType289", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType289", self)
                    

    @property
    def jpdl31_TaskNodeType247(self):
        return self.__jpdl31_TaskNodeType247

    @jpdl31_TaskNodeType247.setter
    def jpdl31_TaskNodeType247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskNodeType__jpdl31_TaskNodeType247", None)
        self.__jpdl31_TaskNodeType247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType246"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType246", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType246"):
                opp_val = getattr(value, "jpdl31_SuperStateType246", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType246", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_VariableType:

    def __init__(self, name: str, any: str, access: str, mappedName: str, jpdl31_VariableType: "jpdl31_DocumentRoot" = None, jpdl31_VariableType202: "jpdl31_ProcessStateType" = None):
        self.name = name
        self.any = any
        self.access = access
        self.mappedName = mappedName
        self.jpdl31_VariableType = jpdl31_VariableType
        self.jpdl31_VariableType202 = jpdl31_VariableType202
        
    @property
    def mappedName(self) -> str:
        return self.__mappedName

    @mappedName.setter
    def mappedName(self, mappedName: str):
        self.__mappedName = mappedName

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def access(self) -> str:
        return self.__access

    @access.setter
    def access(self, access: str):
        self.__access = access

    @property
    def jpdl31_VariableType(self):
        return self.__jpdl31_VariableType

    @jpdl31_VariableType.setter
    def jpdl31_VariableType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_VariableType__jpdl31_VariableType", None)
        self.__jpdl31_VariableType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot68"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot68"):
                opp_val = getattr(value, "jpdl31_DocumentRoot68", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_VariableType202(self):
        return self.__jpdl31_VariableType202

    @jpdl31_VariableType202.setter
    def jpdl31_VariableType202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_VariableType__jpdl31_VariableType202", None)
        self.__jpdl31_VariableType202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessStateType201"):
                opp_val = getattr(old_value, "jpdl31_ProcessStateType201", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessStateType201"):
                opp_val = getattr(value, "jpdl31_ProcessStateType201", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessStateType201", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_TransitionType:

    def __init__(self, group: str, name: str, to: str, jpdl31_TransitionType: "jpdl31_DocumentRoot" = None, jpdl31_TransitionType107: "jpdl31_ForkType" = None, jpdl31_TransitionType119: "jpdl31_JoinType" = None, jpdl31_TransitionType143: "jpdl31_NodeType" = None, jpdl31_TransitionType214: "jpdl31_ProcessStateType" = None, jpdl31_TransitionType220: "jpdl31_StartStateType" = None, jpdl31_TransitionType238: "jpdl31_StateType" = None, jpdl31_TransitionType277: "jpdl31_SuperStateType" = None, jpdl31_TransitionType295: "jpdl31_TaskNodeType" = None, jpdl31_TransitionType315: set["jpdl31_ActionType"] = None, jpdl31_TransitionType321: set["jpdl31_CreateTimerType"] = None, jpdl31_TransitionType324: set["jpdl31_CancelTimerType"] = None, jpdl31_TransitionType327: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_TransitionType318: set["jpdl31_ScriptType"] = None):
        self.group = group
        self.name = name
        self.to = to
        self.jpdl31_TransitionType = jpdl31_TransitionType
        self.jpdl31_TransitionType107 = jpdl31_TransitionType107
        self.jpdl31_TransitionType119 = jpdl31_TransitionType119
        self.jpdl31_TransitionType143 = jpdl31_TransitionType143
        self.jpdl31_TransitionType214 = jpdl31_TransitionType214
        self.jpdl31_TransitionType220 = jpdl31_TransitionType220
        self.jpdl31_TransitionType238 = jpdl31_TransitionType238
        self.jpdl31_TransitionType277 = jpdl31_TransitionType277
        self.jpdl31_TransitionType295 = jpdl31_TransitionType295
        self.jpdl31_TransitionType315 = jpdl31_TransitionType315 if jpdl31_TransitionType315 is not None else set()
        self.jpdl31_TransitionType321 = jpdl31_TransitionType321 if jpdl31_TransitionType321 is not None else set()
        self.jpdl31_TransitionType324 = jpdl31_TransitionType324 if jpdl31_TransitionType324 is not None else set()
        self.jpdl31_TransitionType327 = jpdl31_TransitionType327 if jpdl31_TransitionType327 is not None else set()
        self.jpdl31_TransitionType318 = jpdl31_TransitionType318 if jpdl31_TransitionType318 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def jpdl31_TransitionType143(self):
        return self.__jpdl31_TransitionType143

    @jpdl31_TransitionType143.setter
    def jpdl31_TransitionType143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType143", None)
        self.__jpdl31_TransitionType143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_NodeType142"):
                opp_val = getattr(old_value, "jpdl31_NodeType142", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_NodeType142"):
                opp_val = getattr(value, "jpdl31_NodeType142", None)
                if opp_val is None:
                    setattr(value, "jpdl31_NodeType142", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType277(self):
        return self.__jpdl31_TransitionType277

    @jpdl31_TransitionType277.setter
    def jpdl31_TransitionType277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType277", None)
        self.__jpdl31_TransitionType277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType276"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType276", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType276"):
                opp_val = getattr(value, "jpdl31_SuperStateType276", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType276", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType321(self):
        return self.__jpdl31_TransitionType321

    @jpdl31_TransitionType321.setter
    def jpdl31_TransitionType321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType321", None)
        self.__jpdl31_TransitionType321 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CreateTimerType322"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType322", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CreateTimerType322", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CreateTimerType322"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType322", None)
                    
                    setattr(item, "jpdl31_CreateTimerType322", self)
                    

    @property
    def jpdl31_TransitionType214(self):
        return self.__jpdl31_TransitionType214

    @jpdl31_TransitionType214.setter
    def jpdl31_TransitionType214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType214", None)
        self.__jpdl31_TransitionType214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessStateType213"):
                opp_val = getattr(old_value, "jpdl31_ProcessStateType213", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessStateType213"):
                opp_val = getattr(value, "jpdl31_ProcessStateType213", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessStateType213", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType(self):
        return self.__jpdl31_TransitionType

    @jpdl31_TransitionType.setter
    def jpdl31_TransitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType", None)
        self.__jpdl31_TransitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot66"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot66"):
                opp_val = getattr(value, "jpdl31_DocumentRoot66", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType318(self):
        return self.__jpdl31_TransitionType318

    @jpdl31_TransitionType318.setter
    def jpdl31_TransitionType318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType318", None)
        self.__jpdl31_TransitionType318 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ScriptType319"):
                    opp_val = getattr(item, "jpdl31_ScriptType319", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ScriptType319", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ScriptType319"):
                    opp_val = getattr(item, "jpdl31_ScriptType319", None)
                    
                    setattr(item, "jpdl31_ScriptType319", self)
                    

    @property
    def jpdl31_TransitionType238(self):
        return self.__jpdl31_TransitionType238

    @jpdl31_TransitionType238.setter
    def jpdl31_TransitionType238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType238", None)
        self.__jpdl31_TransitionType238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_StateType237"):
                opp_val = getattr(old_value, "jpdl31_StateType237", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_StateType237"):
                opp_val = getattr(value, "jpdl31_StateType237", None)
                if opp_val is None:
                    setattr(value, "jpdl31_StateType237", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType327(self):
        return self.__jpdl31_TransitionType327

    @jpdl31_TransitionType327.setter
    def jpdl31_TransitionType327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType327", None)
        self.__jpdl31_TransitionType327 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType328"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType328", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType328", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType328"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType328", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType328", self)
                    

    @property
    def jpdl31_TransitionType107(self):
        return self.__jpdl31_TransitionType107

    @jpdl31_TransitionType107.setter
    def jpdl31_TransitionType107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType107", None)
        self.__jpdl31_TransitionType107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ForkType106"):
                opp_val = getattr(old_value, "jpdl31_ForkType106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ForkType106"):
                opp_val = getattr(value, "jpdl31_ForkType106", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ForkType106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType220(self):
        return self.__jpdl31_TransitionType220

    @jpdl31_TransitionType220.setter
    def jpdl31_TransitionType220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType220", None)
        self.__jpdl31_TransitionType220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_StartStateType219"):
                opp_val = getattr(old_value, "jpdl31_StartStateType219", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_StartStateType219"):
                opp_val = getattr(value, "jpdl31_StartStateType219", None)
                if opp_val is None:
                    setattr(value, "jpdl31_StartStateType219", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType295(self):
        return self.__jpdl31_TransitionType295

    @jpdl31_TransitionType295.setter
    def jpdl31_TransitionType295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType295", None)
        self.__jpdl31_TransitionType295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskNodeType294"):
                opp_val = getattr(old_value, "jpdl31_TaskNodeType294", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskNodeType294"):
                opp_val = getattr(value, "jpdl31_TaskNodeType294", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskNodeType294", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType315(self):
        return self.__jpdl31_TransitionType315

    @jpdl31_TransitionType315.setter
    def jpdl31_TransitionType315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType315", None)
        self.__jpdl31_TransitionType315 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ActionType316"):
                    opp_val = getattr(item, "jpdl31_ActionType316", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ActionType316", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ActionType316"):
                    opp_val = getattr(item, "jpdl31_ActionType316", None)
                    
                    setattr(item, "jpdl31_ActionType316", self)
                    

    @property
    def jpdl31_TransitionType324(self):
        return self.__jpdl31_TransitionType324

    @jpdl31_TransitionType324.setter
    def jpdl31_TransitionType324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType324", None)
        self.__jpdl31_TransitionType324 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CancelTimerType325"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType325", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CancelTimerType325", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CancelTimerType325"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType325", None)
                    
                    setattr(item, "jpdl31_CancelTimerType325", self)
                    

    @property
    def jpdl31_TransitionType119(self):
        return self.__jpdl31_TransitionType119

    @jpdl31_TransitionType119.setter
    def jpdl31_TransitionType119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType119", None)
        self.__jpdl31_TransitionType119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_JoinType118"):
                opp_val = getattr(old_value, "jpdl31_JoinType118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_JoinType118"):
                opp_val = getattr(value, "jpdl31_JoinType118", None)
                if opp_val is None:
                    setattr(value, "jpdl31_JoinType118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_TimerType:

    def __init__(self, duedate: str, name: str, repeat: str, transition: str, jpdl31_TimerType: "jpdl31_DocumentRoot" = None, jpdl31_TimerType104: "jpdl31_ForkType" = None, jpdl31_TimerType116: "jpdl31_JoinType" = None, jpdl31_TimerType140: "jpdl31_NodeType" = None, jpdl31_TimerType211: "jpdl31_ProcessStateType" = None, jpdl31_TimerType235: "jpdl31_StateType" = None, jpdl31_TimerType274: "jpdl31_SuperStateType" = None, jpdl31_TimerType292: "jpdl31_TaskNodeType" = None, jpdl31_TimerType307: "jpdl31_TaskType" = None, jpdl31_TimerType309: "jpdl31_ActionType" = None, jpdl31_TimerType312: "jpdl31_ScriptType" = None):
        self.duedate = duedate
        self.name = name
        self.repeat = repeat
        self.transition = transition
        self.jpdl31_TimerType = jpdl31_TimerType
        self.jpdl31_TimerType104 = jpdl31_TimerType104
        self.jpdl31_TimerType116 = jpdl31_TimerType116
        self.jpdl31_TimerType140 = jpdl31_TimerType140
        self.jpdl31_TimerType211 = jpdl31_TimerType211
        self.jpdl31_TimerType235 = jpdl31_TimerType235
        self.jpdl31_TimerType274 = jpdl31_TimerType274
        self.jpdl31_TimerType292 = jpdl31_TimerType292
        self.jpdl31_TimerType307 = jpdl31_TimerType307
        self.jpdl31_TimerType309 = jpdl31_TimerType309
        self.jpdl31_TimerType312 = jpdl31_TimerType312
        
    @property
    def transition(self) -> str:
        return self.__transition

    @transition.setter
    def transition(self, transition: str):
        self.__transition = transition

    @property
    def duedate(self) -> str:
        return self.__duedate

    @duedate.setter
    def duedate(self, duedate: str):
        self.__duedate = duedate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def repeat(self) -> str:
        return self.__repeat

    @repeat.setter
    def repeat(self, repeat: str):
        self.__repeat = repeat

    @property
    def jpdl31_TimerType292(self):
        return self.__jpdl31_TimerType292

    @jpdl31_TimerType292.setter
    def jpdl31_TimerType292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType292", None)
        self.__jpdl31_TimerType292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskNodeType291"):
                opp_val = getattr(old_value, "jpdl31_TaskNodeType291", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskNodeType291"):
                opp_val = getattr(value, "jpdl31_TaskNodeType291", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskNodeType291", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TimerType307(self):
        return self.__jpdl31_TimerType307

    @jpdl31_TimerType307.setter
    def jpdl31_TimerType307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType307", None)
        self.__jpdl31_TimerType307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskType306"):
                opp_val = getattr(old_value, "jpdl31_TaskType306", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskType306"):
                opp_val = getattr(value, "jpdl31_TaskType306", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskType306", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TimerType116(self):
        return self.__jpdl31_TimerType116

    @jpdl31_TimerType116.setter
    def jpdl31_TimerType116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType116", None)
        self.__jpdl31_TimerType116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_JoinType115"):
                opp_val = getattr(old_value, "jpdl31_JoinType115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_JoinType115"):
                opp_val = getattr(value, "jpdl31_JoinType115", None)
                if opp_val is None:
                    setattr(value, "jpdl31_JoinType115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TimerType309(self):
        return self.__jpdl31_TimerType309

    @jpdl31_TimerType309.setter
    def jpdl31_TimerType309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType309", None)
        self.__jpdl31_TimerType309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ActionType310"):
                opp_val = getattr(old_value, "jpdl31_ActionType310", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_ActionType310", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ActionType310"):
                opp_val = getattr(value, "jpdl31_ActionType310", None)
                setattr(value, "jpdl31_ActionType310", self)

    @property
    def jpdl31_TimerType104(self):
        return self.__jpdl31_TimerType104

    @jpdl31_TimerType104.setter
    def jpdl31_TimerType104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType104", None)
        self.__jpdl31_TimerType104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ForkType103"):
                opp_val = getattr(old_value, "jpdl31_ForkType103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ForkType103"):
                opp_val = getattr(value, "jpdl31_ForkType103", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ForkType103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TimerType(self):
        return self.__jpdl31_TimerType

    @jpdl31_TimerType.setter
    def jpdl31_TimerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType", None)
        self.__jpdl31_TimerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot64"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot64"):
                opp_val = getattr(value, "jpdl31_DocumentRoot64", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TimerType235(self):
        return self.__jpdl31_TimerType235

    @jpdl31_TimerType235.setter
    def jpdl31_TimerType235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType235", None)
        self.__jpdl31_TimerType235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_StateType234"):
                opp_val = getattr(old_value, "jpdl31_StateType234", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_StateType234"):
                opp_val = getattr(value, "jpdl31_StateType234", None)
                if opp_val is None:
                    setattr(value, "jpdl31_StateType234", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TimerType211(self):
        return self.__jpdl31_TimerType211

    @jpdl31_TimerType211.setter
    def jpdl31_TimerType211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType211", None)
        self.__jpdl31_TimerType211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessStateType210"):
                opp_val = getattr(old_value, "jpdl31_ProcessStateType210", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessStateType210"):
                opp_val = getattr(value, "jpdl31_ProcessStateType210", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessStateType210", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TimerType312(self):
        return self.__jpdl31_TimerType312

    @jpdl31_TimerType312.setter
    def jpdl31_TimerType312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType312", None)
        self.__jpdl31_TimerType312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ScriptType313"):
                opp_val = getattr(old_value, "jpdl31_ScriptType313", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_ScriptType313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ScriptType313"):
                opp_val = getattr(value, "jpdl31_ScriptType313", None)
                setattr(value, "jpdl31_ScriptType313", self)

    @property
    def jpdl31_TimerType140(self):
        return self.__jpdl31_TimerType140

    @jpdl31_TimerType140.setter
    def jpdl31_TimerType140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType140", None)
        self.__jpdl31_TimerType140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_NodeType139"):
                opp_val = getattr(old_value, "jpdl31_NodeType139", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_NodeType139"):
                opp_val = getattr(value, "jpdl31_NodeType139", None)
                if opp_val is None:
                    setattr(value, "jpdl31_NodeType139", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TimerType274(self):
        return self.__jpdl31_TimerType274

    @jpdl31_TimerType274.setter
    def jpdl31_TimerType274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType274", None)
        self.__jpdl31_TimerType274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType273"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType273", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType273"):
                opp_val = getattr(value, "jpdl31_SuperStateType273", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType273", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_ProcessStateType:

    def __init__(self, group: str, async: str, name: str, jpdl31_ProcessStateType: "jpdl31_DocumentRoot" = None, jpdl31_ProcessStateType164: "jpdl31_ProcessDefinitionType" = None, jpdl31_ProcessStateType199: set["jpdl31_SubProcessType"] = None, jpdl31_ProcessStateType207: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_ProcessStateType210: set["jpdl31_TimerType"] = None, jpdl31_ProcessStateType213: set["jpdl31_TransitionType"] = None, jpdl31_ProcessStateType201: set["jpdl31_VariableType"] = None, jpdl31_ProcessStateType204: set["jpdl31_EventType"] = None, jpdl31_ProcessStateType253: "jpdl31_SuperStateType" = None):
        self.group = group
        self.async = async
        self.name = name
        self.jpdl31_ProcessStateType = jpdl31_ProcessStateType
        self.jpdl31_ProcessStateType164 = jpdl31_ProcessStateType164
        self.jpdl31_ProcessStateType199 = jpdl31_ProcessStateType199 if jpdl31_ProcessStateType199 is not None else set()
        self.jpdl31_ProcessStateType207 = jpdl31_ProcessStateType207 if jpdl31_ProcessStateType207 is not None else set()
        self.jpdl31_ProcessStateType210 = jpdl31_ProcessStateType210 if jpdl31_ProcessStateType210 is not None else set()
        self.jpdl31_ProcessStateType213 = jpdl31_ProcessStateType213 if jpdl31_ProcessStateType213 is not None else set()
        self.jpdl31_ProcessStateType201 = jpdl31_ProcessStateType201 if jpdl31_ProcessStateType201 is not None else set()
        self.jpdl31_ProcessStateType204 = jpdl31_ProcessStateType204 if jpdl31_ProcessStateType204 is not None else set()
        self.jpdl31_ProcessStateType253 = jpdl31_ProcessStateType253
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl31_ProcessStateType(self):
        return self.__jpdl31_ProcessStateType

    @jpdl31_ProcessStateType.setter
    def jpdl31_ProcessStateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessStateType__jpdl31_ProcessStateType", None)
        self.__jpdl31_ProcessStateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot47"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot47"):
                opp_val = getattr(value, "jpdl31_DocumentRoot47", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ProcessStateType164(self):
        return self.__jpdl31_ProcessStateType164

    @jpdl31_ProcessStateType164.setter
    def jpdl31_ProcessStateType164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessStateType__jpdl31_ProcessStateType164", None)
        self.__jpdl31_ProcessStateType164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType163"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType163"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType163", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ProcessStateType204(self):
        return self.__jpdl31_ProcessStateType204

    @jpdl31_ProcessStateType204.setter
    def jpdl31_ProcessStateType204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessStateType__jpdl31_ProcessStateType204", None)
        self.__jpdl31_ProcessStateType204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType205"):
                    opp_val = getattr(item, "jpdl31_EventType205", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType205", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType205"):
                    opp_val = getattr(item, "jpdl31_EventType205", None)
                    
                    setattr(item, "jpdl31_EventType205", self)
                    

    @property
    def jpdl31_ProcessStateType199(self):
        return self.__jpdl31_ProcessStateType199

    @jpdl31_ProcessStateType199.setter
    def jpdl31_ProcessStateType199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessStateType__jpdl31_ProcessStateType199", None)
        self.__jpdl31_ProcessStateType199 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_SubProcessType"):
                    opp_val = getattr(item, "jpdl31_SubProcessType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_SubProcessType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_SubProcessType"):
                    opp_val = getattr(item, "jpdl31_SubProcessType", None)
                    
                    setattr(item, "jpdl31_SubProcessType", self)
                    

    @property
    def jpdl31_ProcessStateType210(self):
        return self.__jpdl31_ProcessStateType210

    @jpdl31_ProcessStateType210.setter
    def jpdl31_ProcessStateType210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessStateType__jpdl31_ProcessStateType210", None)
        self.__jpdl31_ProcessStateType210 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType211"):
                    opp_val = getattr(item, "jpdl31_TimerType211", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType211"):
                    opp_val = getattr(item, "jpdl31_TimerType211", None)
                    
                    setattr(item, "jpdl31_TimerType211", self)
                    

    @property
    def jpdl31_ProcessStateType213(self):
        return self.__jpdl31_ProcessStateType213

    @jpdl31_ProcessStateType213.setter
    def jpdl31_ProcessStateType213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessStateType__jpdl31_ProcessStateType213", None)
        self.__jpdl31_ProcessStateType213 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType214"):
                    opp_val = getattr(item, "jpdl31_TransitionType214", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType214"):
                    opp_val = getattr(item, "jpdl31_TransitionType214", None)
                    
                    setattr(item, "jpdl31_TransitionType214", self)
                    

    @property
    def jpdl31_ProcessStateType201(self):
        return self.__jpdl31_ProcessStateType201

    @jpdl31_ProcessStateType201.setter
    def jpdl31_ProcessStateType201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessStateType__jpdl31_ProcessStateType201", None)
        self.__jpdl31_ProcessStateType201 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_VariableType202"):
                    opp_val = getattr(item, "jpdl31_VariableType202", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_VariableType202", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_VariableType202"):
                    opp_val = getattr(item, "jpdl31_VariableType202", None)
                    
                    setattr(item, "jpdl31_VariableType202", self)
                    

    @property
    def jpdl31_ProcessStateType207(self):
        return self.__jpdl31_ProcessStateType207

    @jpdl31_ProcessStateType207.setter
    def jpdl31_ProcessStateType207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessStateType__jpdl31_ProcessStateType207", None)
        self.__jpdl31_ProcessStateType207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType208"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType208", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType208", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType208"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType208", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType208", self)
                    

    @property
    def jpdl31_ProcessStateType253(self):
        return self.__jpdl31_ProcessStateType253

    @jpdl31_ProcessStateType253.setter
    def jpdl31_ProcessStateType253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessStateType__jpdl31_ProcessStateType253", None)
        self.__jpdl31_ProcessStateType253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType252"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType252", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType252"):
                opp_val = getattr(value, "jpdl31_SuperStateType252", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType252", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_TaskType:

    def __init__(self, group: str, blocking: str, description: str, duedate: str, name: str, priority: str, signalling: str, swimlane: str, jpdl31_TaskType: "jpdl31_DocumentRoot" = None, jpdl31_TaskType197: "jpdl31_ProcessDefinitionType" = None, jpdl31_TaskType217: "jpdl31_StartStateType" = None, jpdl31_TaskType283: "jpdl31_TaskNodeType" = None, jpdl31_TaskType297: set["jpdl31_AssignmentType"] = None, jpdl31_TaskType303: set["jpdl31_EventType"] = None, jpdl31_TaskType306: set["jpdl31_TimerType"] = None, jpdl31_TaskType300: set["jpdl31_Delegation"] = None):
        self.group = group
        self.blocking = blocking
        self.description = description
        self.duedate = duedate
        self.name = name
        self.priority = priority
        self.signalling = signalling
        self.swimlane = swimlane
        self.jpdl31_TaskType = jpdl31_TaskType
        self.jpdl31_TaskType197 = jpdl31_TaskType197
        self.jpdl31_TaskType217 = jpdl31_TaskType217
        self.jpdl31_TaskType283 = jpdl31_TaskType283
        self.jpdl31_TaskType297 = jpdl31_TaskType297 if jpdl31_TaskType297 is not None else set()
        self.jpdl31_TaskType303 = jpdl31_TaskType303 if jpdl31_TaskType303 is not None else set()
        self.jpdl31_TaskType306 = jpdl31_TaskType306 if jpdl31_TaskType306 is not None else set()
        self.jpdl31_TaskType300 = jpdl31_TaskType300 if jpdl31_TaskType300 is not None else set()
        
    @property
    def duedate(self) -> str:
        return self.__duedate

    @duedate.setter
    def duedate(self, duedate: str):
        self.__duedate = duedate

    @property
    def signalling(self) -> str:
        return self.__signalling

    @signalling.setter
    def signalling(self, signalling: str):
        self.__signalling = signalling

    @property
    def blocking(self) -> str:
        return self.__blocking

    @blocking.setter
    def blocking(self, blocking: str):
        self.__blocking = blocking

    @property
    def swimlane(self) -> str:
        return self.__swimlane

    @swimlane.setter
    def swimlane(self, swimlane: str):
        self.__swimlane = swimlane

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def jpdl31_TaskType197(self):
        return self.__jpdl31_TaskType197

    @jpdl31_TaskType197.setter
    def jpdl31_TaskType197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType197", None)
        self.__jpdl31_TaskType197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType196"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType196", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType196"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType196", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType196", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TaskType297(self):
        return self.__jpdl31_TaskType297

    @jpdl31_TaskType297.setter
    def jpdl31_TaskType297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType297", None)
        self.__jpdl31_TaskType297 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_AssignmentType298"):
                    opp_val = getattr(item, "jpdl31_AssignmentType298", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_AssignmentType298", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_AssignmentType298"):
                    opp_val = getattr(item, "jpdl31_AssignmentType298", None)
                    
                    setattr(item, "jpdl31_AssignmentType298", self)
                    

    @property
    def jpdl31_TaskType300(self):
        return self.__jpdl31_TaskType300

    @jpdl31_TaskType300.setter
    def jpdl31_TaskType300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType300", None)
        self.__jpdl31_TaskType300 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Delegation301"):
                    opp_val = getattr(item, "jpdl31_Delegation301", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Delegation301", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Delegation301"):
                    opp_val = getattr(item, "jpdl31_Delegation301", None)
                    
                    setattr(item, "jpdl31_Delegation301", self)
                    

    @property
    def jpdl31_TaskType303(self):
        return self.__jpdl31_TaskType303

    @jpdl31_TaskType303.setter
    def jpdl31_TaskType303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType303", None)
        self.__jpdl31_TaskType303 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType304"):
                    opp_val = getattr(item, "jpdl31_EventType304", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType304", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType304"):
                    opp_val = getattr(item, "jpdl31_EventType304", None)
                    
                    setattr(item, "jpdl31_EventType304", self)
                    

    @property
    def jpdl31_TaskType306(self):
        return self.__jpdl31_TaskType306

    @jpdl31_TaskType306.setter
    def jpdl31_TaskType306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType306", None)
        self.__jpdl31_TaskType306 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType307"):
                    opp_val = getattr(item, "jpdl31_TimerType307", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType307", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType307"):
                    opp_val = getattr(item, "jpdl31_TimerType307", None)
                    
                    setattr(item, "jpdl31_TimerType307", self)
                    

    @property
    def jpdl31_TaskType(self):
        return self.__jpdl31_TaskType

    @jpdl31_TaskType.setter
    def jpdl31_TaskType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType", None)
        self.__jpdl31_TaskType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot60"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot60"):
                opp_val = getattr(value, "jpdl31_DocumentRoot60", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TaskType283(self):
        return self.__jpdl31_TaskType283

    @jpdl31_TaskType283.setter
    def jpdl31_TaskType283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType283", None)
        self.__jpdl31_TaskType283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskNodeType282"):
                opp_val = getattr(old_value, "jpdl31_TaskNodeType282", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskNodeType282"):
                opp_val = getattr(value, "jpdl31_TaskNodeType282", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskNodeType282", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TaskType217(self):
        return self.__jpdl31_TaskType217

    @jpdl31_TaskType217.setter
    def jpdl31_TaskType217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType217", None)
        self.__jpdl31_TaskType217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_StartStateType216"):
                opp_val = getattr(old_value, "jpdl31_StartStateType216", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_StartStateType216"):
                opp_val = getattr(value, "jpdl31_StartStateType216", None)
                if opp_val is None:
                    setattr(value, "jpdl31_StartStateType216", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_SwimlaneType:

    def __init__(self, name: str, jpdl31_SwimlaneType: "jpdl31_DocumentRoot" = None, jpdl31_SwimlaneType146: "jpdl31_ProcessDefinitionType" = None, jpdl31_SwimlaneType279: "jpdl31_AssignmentType" = None):
        self.name = name
        self.jpdl31_SwimlaneType = jpdl31_SwimlaneType
        self.jpdl31_SwimlaneType146 = jpdl31_SwimlaneType146
        self.jpdl31_SwimlaneType279 = jpdl31_SwimlaneType279
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl31_SwimlaneType146(self):
        return self.__jpdl31_SwimlaneType146

    @jpdl31_SwimlaneType146.setter
    def jpdl31_SwimlaneType146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SwimlaneType__jpdl31_SwimlaneType146", None)
        self.__jpdl31_SwimlaneType146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType145"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType145", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType145"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType145", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType145", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_SwimlaneType279(self):
        return self.__jpdl31_SwimlaneType279

    @jpdl31_SwimlaneType279.setter
    def jpdl31_SwimlaneType279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SwimlaneType__jpdl31_SwimlaneType279", None)
        self.__jpdl31_SwimlaneType279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_AssignmentType280"):
                opp_val = getattr(old_value, "jpdl31_AssignmentType280", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_AssignmentType280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_AssignmentType280"):
                opp_val = getattr(value, "jpdl31_AssignmentType280", None)
                setattr(value, "jpdl31_AssignmentType280", self)

    @property
    def jpdl31_SwimlaneType(self):
        return self.__jpdl31_SwimlaneType

    @jpdl31_SwimlaneType.setter
    def jpdl31_SwimlaneType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SwimlaneType__jpdl31_SwimlaneType", None)
        self.__jpdl31_SwimlaneType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot58"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot58"):
                opp_val = getattr(value, "jpdl31_DocumentRoot58", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_SuperStateType:

    def __init__(self, group: str, async: str, name: str, jpdl31_SuperStateType: "jpdl31_DocumentRoot" = None, jpdl31_SuperStateType161: "jpdl31_ProcessDefinitionType" = None, jpdl31_SuperStateType240: set["jpdl31_NodeType"] = None, jpdl31_SuperStateType246: set["jpdl31_TaskNodeType"] = None, jpdl31_SuperStateType250: "jpdl31_SuperStateType" = None, jpdl31_SuperStateType248: set["jpdl31_SuperStateType"] = None, jpdl31_SuperStateType252: set["jpdl31_ProcessStateType"] = None, jpdl31_SuperStateType255: set["jpdl31_ForkType"] = None, jpdl31_SuperStateType258: set["jpdl31_JoinType"] = None, jpdl31_SuperStateType243: set["jpdl31_StateType"] = None, jpdl31_SuperStateType267: set["jpdl31_EventType"] = None, jpdl31_SuperStateType270: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_SuperStateType273: set["jpdl31_TimerType"] = None, jpdl31_SuperStateType276: set["jpdl31_TransitionType"] = None, jpdl31_SuperStateType261: set["jpdl31_DecisionType"] = None, jpdl31_SuperStateType264: set["jpdl31_EndStateType"] = None):
        self.group = group
        self.async = async
        self.name = name
        self.jpdl31_SuperStateType = jpdl31_SuperStateType
        self.jpdl31_SuperStateType161 = jpdl31_SuperStateType161
        self.jpdl31_SuperStateType240 = jpdl31_SuperStateType240 if jpdl31_SuperStateType240 is not None else set()
        self.jpdl31_SuperStateType246 = jpdl31_SuperStateType246 if jpdl31_SuperStateType246 is not None else set()
        self.jpdl31_SuperStateType250 = jpdl31_SuperStateType250
        self.jpdl31_SuperStateType248 = jpdl31_SuperStateType248 if jpdl31_SuperStateType248 is not None else set()
        self.jpdl31_SuperStateType252 = jpdl31_SuperStateType252 if jpdl31_SuperStateType252 is not None else set()
        self.jpdl31_SuperStateType255 = jpdl31_SuperStateType255 if jpdl31_SuperStateType255 is not None else set()
        self.jpdl31_SuperStateType258 = jpdl31_SuperStateType258 if jpdl31_SuperStateType258 is not None else set()
        self.jpdl31_SuperStateType243 = jpdl31_SuperStateType243 if jpdl31_SuperStateType243 is not None else set()
        self.jpdl31_SuperStateType267 = jpdl31_SuperStateType267 if jpdl31_SuperStateType267 is not None else set()
        self.jpdl31_SuperStateType270 = jpdl31_SuperStateType270 if jpdl31_SuperStateType270 is not None else set()
        self.jpdl31_SuperStateType273 = jpdl31_SuperStateType273 if jpdl31_SuperStateType273 is not None else set()
        self.jpdl31_SuperStateType276 = jpdl31_SuperStateType276 if jpdl31_SuperStateType276 is not None else set()
        self.jpdl31_SuperStateType261 = jpdl31_SuperStateType261 if jpdl31_SuperStateType261 is not None else set()
        self.jpdl31_SuperStateType264 = jpdl31_SuperStateType264 if jpdl31_SuperStateType264 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

    @property
    def jpdl31_SuperStateType255(self):
        return self.__jpdl31_SuperStateType255

    @jpdl31_SuperStateType255.setter
    def jpdl31_SuperStateType255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType255", None)
        self.__jpdl31_SuperStateType255 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ForkType256"):
                    opp_val = getattr(item, "jpdl31_ForkType256", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ForkType256", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ForkType256"):
                    opp_val = getattr(item, "jpdl31_ForkType256", None)
                    
                    setattr(item, "jpdl31_ForkType256", self)
                    

    @property
    def jpdl31_SuperStateType243(self):
        return self.__jpdl31_SuperStateType243

    @jpdl31_SuperStateType243.setter
    def jpdl31_SuperStateType243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType243", None)
        self.__jpdl31_SuperStateType243 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_StateType244"):
                    opp_val = getattr(item, "jpdl31_StateType244", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_StateType244", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_StateType244"):
                    opp_val = getattr(item, "jpdl31_StateType244", None)
                    
                    setattr(item, "jpdl31_StateType244", self)
                    

    @property
    def jpdl31_SuperStateType(self):
        return self.__jpdl31_SuperStateType

    @jpdl31_SuperStateType.setter
    def jpdl31_SuperStateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType", None)
        self.__jpdl31_SuperStateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot56"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot56"):
                opp_val = getattr(value, "jpdl31_DocumentRoot56", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_SuperStateType248(self):
        return self.__jpdl31_SuperStateType248

    @jpdl31_SuperStateType248.setter
    def jpdl31_SuperStateType248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType248", None)
        self.__jpdl31_SuperStateType248 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_SuperStateType250"):
                    opp_val = getattr(item, "jpdl31_SuperStateType250", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_SuperStateType250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_SuperStateType250"):
                    opp_val = getattr(item, "jpdl31_SuperStateType250", None)
                    
                    setattr(item, "jpdl31_SuperStateType250", self)
                    

    @property
    def jpdl31_SuperStateType252(self):
        return self.__jpdl31_SuperStateType252

    @jpdl31_SuperStateType252.setter
    def jpdl31_SuperStateType252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType252", None)
        self.__jpdl31_SuperStateType252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ProcessStateType253"):
                    opp_val = getattr(item, "jpdl31_ProcessStateType253", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ProcessStateType253", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ProcessStateType253"):
                    opp_val = getattr(item, "jpdl31_ProcessStateType253", None)
                    
                    setattr(item, "jpdl31_ProcessStateType253", self)
                    

    @property
    def jpdl31_SuperStateType161(self):
        return self.__jpdl31_SuperStateType161

    @jpdl31_SuperStateType161.setter
    def jpdl31_SuperStateType161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType161", None)
        self.__jpdl31_SuperStateType161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType160"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType160"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType160", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_SuperStateType246(self):
        return self.__jpdl31_SuperStateType246

    @jpdl31_SuperStateType246.setter
    def jpdl31_SuperStateType246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType246", None)
        self.__jpdl31_SuperStateType246 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TaskNodeType247"):
                    opp_val = getattr(item, "jpdl31_TaskNodeType247", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TaskNodeType247", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TaskNodeType247"):
                    opp_val = getattr(item, "jpdl31_TaskNodeType247", None)
                    
                    setattr(item, "jpdl31_TaskNodeType247", self)
                    

    @property
    def jpdl31_SuperStateType258(self):
        return self.__jpdl31_SuperStateType258

    @jpdl31_SuperStateType258.setter
    def jpdl31_SuperStateType258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType258", None)
        self.__jpdl31_SuperStateType258 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_JoinType259"):
                    opp_val = getattr(item, "jpdl31_JoinType259", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_JoinType259", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_JoinType259"):
                    opp_val = getattr(item, "jpdl31_JoinType259", None)
                    
                    setattr(item, "jpdl31_JoinType259", self)
                    

    @property
    def jpdl31_SuperStateType264(self):
        return self.__jpdl31_SuperStateType264

    @jpdl31_SuperStateType264.setter
    def jpdl31_SuperStateType264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType264", None)
        self.__jpdl31_SuperStateType264 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EndStateType265"):
                    opp_val = getattr(item, "jpdl31_EndStateType265", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EndStateType265", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EndStateType265"):
                    opp_val = getattr(item, "jpdl31_EndStateType265", None)
                    
                    setattr(item, "jpdl31_EndStateType265", self)
                    

    @property
    def jpdl31_SuperStateType267(self):
        return self.__jpdl31_SuperStateType267

    @jpdl31_SuperStateType267.setter
    def jpdl31_SuperStateType267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType267", None)
        self.__jpdl31_SuperStateType267 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType268"):
                    opp_val = getattr(item, "jpdl31_EventType268", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType268", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType268"):
                    opp_val = getattr(item, "jpdl31_EventType268", None)
                    
                    setattr(item, "jpdl31_EventType268", self)
                    

    @property
    def jpdl31_SuperStateType261(self):
        return self.__jpdl31_SuperStateType261

    @jpdl31_SuperStateType261.setter
    def jpdl31_SuperStateType261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType261", None)
        self.__jpdl31_SuperStateType261 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_DecisionType262"):
                    opp_val = getattr(item, "jpdl31_DecisionType262", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_DecisionType262", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_DecisionType262"):
                    opp_val = getattr(item, "jpdl31_DecisionType262", None)
                    
                    setattr(item, "jpdl31_DecisionType262", self)
                    

    @property
    def jpdl31_SuperStateType270(self):
        return self.__jpdl31_SuperStateType270

    @jpdl31_SuperStateType270.setter
    def jpdl31_SuperStateType270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType270", None)
        self.__jpdl31_SuperStateType270 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType271"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType271", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType271", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType271"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType271", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType271", self)
                    

    @property
    def jpdl31_SuperStateType250(self):
        return self.__jpdl31_SuperStateType250

    @jpdl31_SuperStateType250.setter
    def jpdl31_SuperStateType250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType250", None)
        self.__jpdl31_SuperStateType250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType248"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType248", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType248"):
                opp_val = getattr(value, "jpdl31_SuperStateType248", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType248", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_SuperStateType240(self):
        return self.__jpdl31_SuperStateType240

    @jpdl31_SuperStateType240.setter
    def jpdl31_SuperStateType240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType240", None)
        self.__jpdl31_SuperStateType240 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_NodeType241"):
                    opp_val = getattr(item, "jpdl31_NodeType241", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_NodeType241", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_NodeType241"):
                    opp_val = getattr(item, "jpdl31_NodeType241", None)
                    
                    setattr(item, "jpdl31_NodeType241", self)
                    

    @property
    def jpdl31_SuperStateType276(self):
        return self.__jpdl31_SuperStateType276

    @jpdl31_SuperStateType276.setter
    def jpdl31_SuperStateType276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType276", None)
        self.__jpdl31_SuperStateType276 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType277"):
                    opp_val = getattr(item, "jpdl31_TransitionType277", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType277", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType277"):
                    opp_val = getattr(item, "jpdl31_TransitionType277", None)
                    
                    setattr(item, "jpdl31_TransitionType277", self)
                    

    @property
    def jpdl31_SuperStateType273(self):
        return self.__jpdl31_SuperStateType273

    @jpdl31_SuperStateType273.setter
    def jpdl31_SuperStateType273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType273", None)
        self.__jpdl31_SuperStateType273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType274"):
                    opp_val = getattr(item, "jpdl31_TimerType274", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType274", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType274"):
                    opp_val = getattr(item, "jpdl31_TimerType274", None)
                    
                    setattr(item, "jpdl31_TimerType274", self)
                    

class jpdl31_StateType:

    def __init__(self, nodeContentElements: str, async: str, name: str, jpdl31_StateType: "jpdl31_DocumentRoot" = None, jpdl31_StateType155: "jpdl31_ProcessDefinitionType" = None, jpdl31_StateType228: set["jpdl31_EventType"] = None, jpdl31_StateType231: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_StateType234: set["jpdl31_TimerType"] = None, jpdl31_StateType237: set["jpdl31_TransitionType"] = None, jpdl31_StateType244: "jpdl31_SuperStateType" = None):
        self.nodeContentElements = nodeContentElements
        self.async = async
        self.name = name
        self.jpdl31_StateType = jpdl31_StateType
        self.jpdl31_StateType155 = jpdl31_StateType155
        self.jpdl31_StateType228 = jpdl31_StateType228 if jpdl31_StateType228 is not None else set()
        self.jpdl31_StateType231 = jpdl31_StateType231 if jpdl31_StateType231 is not None else set()
        self.jpdl31_StateType234 = jpdl31_StateType234 if jpdl31_StateType234 is not None else set()
        self.jpdl31_StateType237 = jpdl31_StateType237 if jpdl31_StateType237 is not None else set()
        self.jpdl31_StateType244 = jpdl31_StateType244
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nodeContentElements(self) -> str:
        return self.__nodeContentElements

    @nodeContentElements.setter
    def nodeContentElements(self, nodeContentElements: str):
        self.__nodeContentElements = nodeContentElements

    @property
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

    @property
    def jpdl31_StateType244(self):
        return self.__jpdl31_StateType244

    @jpdl31_StateType244.setter
    def jpdl31_StateType244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StateType__jpdl31_StateType244", None)
        self.__jpdl31_StateType244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType243"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType243", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType243"):
                opp_val = getattr(value, "jpdl31_SuperStateType243", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType243", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_StateType155(self):
        return self.__jpdl31_StateType155

    @jpdl31_StateType155.setter
    def jpdl31_StateType155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StateType__jpdl31_StateType155", None)
        self.__jpdl31_StateType155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType154"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType154"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType154", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_StateType237(self):
        return self.__jpdl31_StateType237

    @jpdl31_StateType237.setter
    def jpdl31_StateType237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StateType__jpdl31_StateType237", None)
        self.__jpdl31_StateType237 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType238"):
                    opp_val = getattr(item, "jpdl31_TransitionType238", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType238", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType238"):
                    opp_val = getattr(item, "jpdl31_TransitionType238", None)
                    
                    setattr(item, "jpdl31_TransitionType238", self)
                    

    @property
    def jpdl31_StateType(self):
        return self.__jpdl31_StateType

    @jpdl31_StateType.setter
    def jpdl31_StateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StateType__jpdl31_StateType", None)
        self.__jpdl31_StateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot54"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot54"):
                opp_val = getattr(value, "jpdl31_DocumentRoot54", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_StateType228(self):
        return self.__jpdl31_StateType228

    @jpdl31_StateType228.setter
    def jpdl31_StateType228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StateType__jpdl31_StateType228", None)
        self.__jpdl31_StateType228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType229"):
                    opp_val = getattr(item, "jpdl31_EventType229", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType229"):
                    opp_val = getattr(item, "jpdl31_EventType229", None)
                    
                    setattr(item, "jpdl31_EventType229", self)
                    

    @property
    def jpdl31_StateType231(self):
        return self.__jpdl31_StateType231

    @jpdl31_StateType231.setter
    def jpdl31_StateType231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StateType__jpdl31_StateType231", None)
        self.__jpdl31_StateType231 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType232"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType232", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType232", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType232"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType232", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType232", self)
                    

    @property
    def jpdl31_StateType234(self):
        return self.__jpdl31_StateType234

    @jpdl31_StateType234.setter
    def jpdl31_StateType234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StateType__jpdl31_StateType234", None)
        self.__jpdl31_StateType234 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType235"):
                    opp_val = getattr(item, "jpdl31_TimerType235", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType235", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType235"):
                    opp_val = getattr(item, "jpdl31_TimerType235", None)
                    
                    setattr(item, "jpdl31_TimerType235", self)
                    

class jpdl31_StartStateType:

    def __init__(self, group: str, name: str, jpdl31_StartStateType: "jpdl31_DocumentRoot" = None, jpdl31_StartStateType149: "jpdl31_ProcessDefinitionType" = None, jpdl31_StartStateType216: set["jpdl31_TaskType"] = None, jpdl31_StartStateType219: set["jpdl31_TransitionType"] = None, jpdl31_StartStateType225: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_StartStateType222: set["jpdl31_EventType"] = None):
        self.group = group
        self.name = name
        self.jpdl31_StartStateType = jpdl31_StartStateType
        self.jpdl31_StartStateType149 = jpdl31_StartStateType149
        self.jpdl31_StartStateType216 = jpdl31_StartStateType216 if jpdl31_StartStateType216 is not None else set()
        self.jpdl31_StartStateType219 = jpdl31_StartStateType219 if jpdl31_StartStateType219 is not None else set()
        self.jpdl31_StartStateType225 = jpdl31_StartStateType225 if jpdl31_StartStateType225 is not None else set()
        self.jpdl31_StartStateType222 = jpdl31_StartStateType222 if jpdl31_StartStateType222 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl31_StartStateType149(self):
        return self.__jpdl31_StartStateType149

    @jpdl31_StartStateType149.setter
    def jpdl31_StartStateType149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StartStateType__jpdl31_StartStateType149", None)
        self.__jpdl31_StartStateType149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType148"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType148"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType148", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_StartStateType219(self):
        return self.__jpdl31_StartStateType219

    @jpdl31_StartStateType219.setter
    def jpdl31_StartStateType219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StartStateType__jpdl31_StartStateType219", None)
        self.__jpdl31_StartStateType219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType220"):
                    opp_val = getattr(item, "jpdl31_TransitionType220", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType220"):
                    opp_val = getattr(item, "jpdl31_TransitionType220", None)
                    
                    setattr(item, "jpdl31_TransitionType220", self)
                    

    @property
    def jpdl31_StartStateType222(self):
        return self.__jpdl31_StartStateType222

    @jpdl31_StartStateType222.setter
    def jpdl31_StartStateType222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StartStateType__jpdl31_StartStateType222", None)
        self.__jpdl31_StartStateType222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType223"):
                    opp_val = getattr(item, "jpdl31_EventType223", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType223"):
                    opp_val = getattr(item, "jpdl31_EventType223", None)
                    
                    setattr(item, "jpdl31_EventType223", self)
                    

    @property
    def jpdl31_StartStateType(self):
        return self.__jpdl31_StartStateType

    @jpdl31_StartStateType.setter
    def jpdl31_StartStateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StartStateType__jpdl31_StartStateType", None)
        self.__jpdl31_StartStateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot52"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot52"):
                opp_val = getattr(value, "jpdl31_DocumentRoot52", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_StartStateType216(self):
        return self.__jpdl31_StartStateType216

    @jpdl31_StartStateType216.setter
    def jpdl31_StartStateType216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StartStateType__jpdl31_StartStateType216", None)
        self.__jpdl31_StartStateType216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TaskType217"):
                    opp_val = getattr(item, "jpdl31_TaskType217", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TaskType217", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TaskType217"):
                    opp_val = getattr(item, "jpdl31_TaskType217", None)
                    
                    setattr(item, "jpdl31_TaskType217", self)
                    

    @property
    def jpdl31_StartStateType225(self):
        return self.__jpdl31_StartStateType225

    @jpdl31_StartStateType225.setter
    def jpdl31_StartStateType225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StartStateType__jpdl31_StartStateType225", None)
        self.__jpdl31_StartStateType225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType226"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType226", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType226"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType226", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType226", self)
                    

class jpdl31_ProcessDefinitionType:

    def __init__(self, group: str, name: str, jpdl31_ProcessDefinitionType: "jpdl31_DocumentRoot" = None, jpdl31_ProcessDefinitionType151: set["jpdl31_NodeType"] = None, jpdl31_ProcessDefinitionType154: set["jpdl31_StateType"] = None, jpdl31_ProcessDefinitionType157: set["jpdl31_TaskNodeType"] = None, jpdl31_ProcessDefinitionType160: set["jpdl31_SuperStateType"] = None, jpdl31_ProcessDefinitionType163: set["jpdl31_ProcessStateType"] = None, jpdl31_ProcessDefinitionType166: set["jpdl31_ForkType"] = None, jpdl31_ProcessDefinitionType145: set["jpdl31_SwimlaneType"] = None, jpdl31_ProcessDefinitionType148: set["jpdl31_StartStateType"] = None, jpdl31_ProcessDefinitionType175: set["jpdl31_EndStateType"] = None, jpdl31_ProcessDefinitionType178: set["jpdl31_ActionType"] = None, jpdl31_ProcessDefinitionType181: set["jpdl31_ScriptType"] = None, jpdl31_ProcessDefinitionType184: set["jpdl31_CreateTimerType"] = None, jpdl31_ProcessDefinitionType187: set["jpdl31_CancelTimerType"] = None, jpdl31_ProcessDefinitionType169: set["jpdl31_JoinType"] = None, jpdl31_ProcessDefinitionType172: set["jpdl31_DecisionType"] = None, jpdl31_ProcessDefinitionType193: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_ProcessDefinitionType196: set["jpdl31_TaskType"] = None, jpdl31_ProcessDefinitionType190: set["jpdl31_EventType"] = None):
        self.group = group
        self.name = name
        self.jpdl31_ProcessDefinitionType = jpdl31_ProcessDefinitionType
        self.jpdl31_ProcessDefinitionType151 = jpdl31_ProcessDefinitionType151 if jpdl31_ProcessDefinitionType151 is not None else set()
        self.jpdl31_ProcessDefinitionType154 = jpdl31_ProcessDefinitionType154 if jpdl31_ProcessDefinitionType154 is not None else set()
        self.jpdl31_ProcessDefinitionType157 = jpdl31_ProcessDefinitionType157 if jpdl31_ProcessDefinitionType157 is not None else set()
        self.jpdl31_ProcessDefinitionType160 = jpdl31_ProcessDefinitionType160 if jpdl31_ProcessDefinitionType160 is not None else set()
        self.jpdl31_ProcessDefinitionType163 = jpdl31_ProcessDefinitionType163 if jpdl31_ProcessDefinitionType163 is not None else set()
        self.jpdl31_ProcessDefinitionType166 = jpdl31_ProcessDefinitionType166 if jpdl31_ProcessDefinitionType166 is not None else set()
        self.jpdl31_ProcessDefinitionType145 = jpdl31_ProcessDefinitionType145 if jpdl31_ProcessDefinitionType145 is not None else set()
        self.jpdl31_ProcessDefinitionType148 = jpdl31_ProcessDefinitionType148 if jpdl31_ProcessDefinitionType148 is not None else set()
        self.jpdl31_ProcessDefinitionType175 = jpdl31_ProcessDefinitionType175 if jpdl31_ProcessDefinitionType175 is not None else set()
        self.jpdl31_ProcessDefinitionType178 = jpdl31_ProcessDefinitionType178 if jpdl31_ProcessDefinitionType178 is not None else set()
        self.jpdl31_ProcessDefinitionType181 = jpdl31_ProcessDefinitionType181 if jpdl31_ProcessDefinitionType181 is not None else set()
        self.jpdl31_ProcessDefinitionType184 = jpdl31_ProcessDefinitionType184 if jpdl31_ProcessDefinitionType184 is not None else set()
        self.jpdl31_ProcessDefinitionType187 = jpdl31_ProcessDefinitionType187 if jpdl31_ProcessDefinitionType187 is not None else set()
        self.jpdl31_ProcessDefinitionType169 = jpdl31_ProcessDefinitionType169 if jpdl31_ProcessDefinitionType169 is not None else set()
        self.jpdl31_ProcessDefinitionType172 = jpdl31_ProcessDefinitionType172 if jpdl31_ProcessDefinitionType172 is not None else set()
        self.jpdl31_ProcessDefinitionType193 = jpdl31_ProcessDefinitionType193 if jpdl31_ProcessDefinitionType193 is not None else set()
        self.jpdl31_ProcessDefinitionType196 = jpdl31_ProcessDefinitionType196 if jpdl31_ProcessDefinitionType196 is not None else set()
        self.jpdl31_ProcessDefinitionType190 = jpdl31_ProcessDefinitionType190 if jpdl31_ProcessDefinitionType190 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def jpdl31_ProcessDefinitionType187(self):
        return self.__jpdl31_ProcessDefinitionType187

    @jpdl31_ProcessDefinitionType187.setter
    def jpdl31_ProcessDefinitionType187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType187", None)
        self.__jpdl31_ProcessDefinitionType187 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CancelTimerType188"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType188", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CancelTimerType188", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CancelTimerType188"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType188", None)
                    
                    setattr(item, "jpdl31_CancelTimerType188", self)
                    

    @property
    def jpdl31_ProcessDefinitionType154(self):
        return self.__jpdl31_ProcessDefinitionType154

    @jpdl31_ProcessDefinitionType154.setter
    def jpdl31_ProcessDefinitionType154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType154", None)
        self.__jpdl31_ProcessDefinitionType154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_StateType155"):
                    opp_val = getattr(item, "jpdl31_StateType155", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_StateType155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_StateType155"):
                    opp_val = getattr(item, "jpdl31_StateType155", None)
                    
                    setattr(item, "jpdl31_StateType155", self)
                    

    @property
    def jpdl31_ProcessDefinitionType151(self):
        return self.__jpdl31_ProcessDefinitionType151

    @jpdl31_ProcessDefinitionType151.setter
    def jpdl31_ProcessDefinitionType151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType151", None)
        self.__jpdl31_ProcessDefinitionType151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_NodeType152"):
                    opp_val = getattr(item, "jpdl31_NodeType152", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_NodeType152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_NodeType152"):
                    opp_val = getattr(item, "jpdl31_NodeType152", None)
                    
                    setattr(item, "jpdl31_NodeType152", self)
                    

    @property
    def jpdl31_ProcessDefinitionType190(self):
        return self.__jpdl31_ProcessDefinitionType190

    @jpdl31_ProcessDefinitionType190.setter
    def jpdl31_ProcessDefinitionType190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType190", None)
        self.__jpdl31_ProcessDefinitionType190 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType191"):
                    opp_val = getattr(item, "jpdl31_EventType191", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType191"):
                    opp_val = getattr(item, "jpdl31_EventType191", None)
                    
                    setattr(item, "jpdl31_EventType191", self)
                    

    @property
    def jpdl31_ProcessDefinitionType175(self):
        return self.__jpdl31_ProcessDefinitionType175

    @jpdl31_ProcessDefinitionType175.setter
    def jpdl31_ProcessDefinitionType175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType175", None)
        self.__jpdl31_ProcessDefinitionType175 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EndStateType176"):
                    opp_val = getattr(item, "jpdl31_EndStateType176", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EndStateType176", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EndStateType176"):
                    opp_val = getattr(item, "jpdl31_EndStateType176", None)
                    
                    setattr(item, "jpdl31_EndStateType176", self)
                    

    @property
    def jpdl31_ProcessDefinitionType(self):
        return self.__jpdl31_ProcessDefinitionType

    @jpdl31_ProcessDefinitionType.setter
    def jpdl31_ProcessDefinitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType", None)
        self.__jpdl31_ProcessDefinitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot45"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot45"):
                opp_val = getattr(value, "jpdl31_DocumentRoot45", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ProcessDefinitionType166(self):
        return self.__jpdl31_ProcessDefinitionType166

    @jpdl31_ProcessDefinitionType166.setter
    def jpdl31_ProcessDefinitionType166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType166", None)
        self.__jpdl31_ProcessDefinitionType166 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ForkType167"):
                    opp_val = getattr(item, "jpdl31_ForkType167", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ForkType167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ForkType167"):
                    opp_val = getattr(item, "jpdl31_ForkType167", None)
                    
                    setattr(item, "jpdl31_ForkType167", self)
                    

    @property
    def jpdl31_ProcessDefinitionType148(self):
        return self.__jpdl31_ProcessDefinitionType148

    @jpdl31_ProcessDefinitionType148.setter
    def jpdl31_ProcessDefinitionType148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType148", None)
        self.__jpdl31_ProcessDefinitionType148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_StartStateType149"):
                    opp_val = getattr(item, "jpdl31_StartStateType149", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_StartStateType149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_StartStateType149"):
                    opp_val = getattr(item, "jpdl31_StartStateType149", None)
                    
                    setattr(item, "jpdl31_StartStateType149", self)
                    

    @property
    def jpdl31_ProcessDefinitionType163(self):
        return self.__jpdl31_ProcessDefinitionType163

    @jpdl31_ProcessDefinitionType163.setter
    def jpdl31_ProcessDefinitionType163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType163", None)
        self.__jpdl31_ProcessDefinitionType163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ProcessStateType164"):
                    opp_val = getattr(item, "jpdl31_ProcessStateType164", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ProcessStateType164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ProcessStateType164"):
                    opp_val = getattr(item, "jpdl31_ProcessStateType164", None)
                    
                    setattr(item, "jpdl31_ProcessStateType164", self)
                    

    @property
    def jpdl31_ProcessDefinitionType172(self):
        return self.__jpdl31_ProcessDefinitionType172

    @jpdl31_ProcessDefinitionType172.setter
    def jpdl31_ProcessDefinitionType172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType172", None)
        self.__jpdl31_ProcessDefinitionType172 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_DecisionType173"):
                    opp_val = getattr(item, "jpdl31_DecisionType173", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_DecisionType173", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_DecisionType173"):
                    opp_val = getattr(item, "jpdl31_DecisionType173", None)
                    
                    setattr(item, "jpdl31_DecisionType173", self)
                    

    @property
    def jpdl31_ProcessDefinitionType184(self):
        return self.__jpdl31_ProcessDefinitionType184

    @jpdl31_ProcessDefinitionType184.setter
    def jpdl31_ProcessDefinitionType184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType184", None)
        self.__jpdl31_ProcessDefinitionType184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CreateTimerType185"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType185", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CreateTimerType185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CreateTimerType185"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType185", None)
                    
                    setattr(item, "jpdl31_CreateTimerType185", self)
                    

    @property
    def jpdl31_ProcessDefinitionType181(self):
        return self.__jpdl31_ProcessDefinitionType181

    @jpdl31_ProcessDefinitionType181.setter
    def jpdl31_ProcessDefinitionType181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType181", None)
        self.__jpdl31_ProcessDefinitionType181 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ScriptType182"):
                    opp_val = getattr(item, "jpdl31_ScriptType182", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ScriptType182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ScriptType182"):
                    opp_val = getattr(item, "jpdl31_ScriptType182", None)
                    
                    setattr(item, "jpdl31_ScriptType182", self)
                    

    @property
    def jpdl31_ProcessDefinitionType157(self):
        return self.__jpdl31_ProcessDefinitionType157

    @jpdl31_ProcessDefinitionType157.setter
    def jpdl31_ProcessDefinitionType157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType157", None)
        self.__jpdl31_ProcessDefinitionType157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TaskNodeType158"):
                    opp_val = getattr(item, "jpdl31_TaskNodeType158", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TaskNodeType158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TaskNodeType158"):
                    opp_val = getattr(item, "jpdl31_TaskNodeType158", None)
                    
                    setattr(item, "jpdl31_TaskNodeType158", self)
                    

    @property
    def jpdl31_ProcessDefinitionType145(self):
        return self.__jpdl31_ProcessDefinitionType145

    @jpdl31_ProcessDefinitionType145.setter
    def jpdl31_ProcessDefinitionType145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType145", None)
        self.__jpdl31_ProcessDefinitionType145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_SwimlaneType146"):
                    opp_val = getattr(item, "jpdl31_SwimlaneType146", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_SwimlaneType146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_SwimlaneType146"):
                    opp_val = getattr(item, "jpdl31_SwimlaneType146", None)
                    
                    setattr(item, "jpdl31_SwimlaneType146", self)
                    

    @property
    def jpdl31_ProcessDefinitionType196(self):
        return self.__jpdl31_ProcessDefinitionType196

    @jpdl31_ProcessDefinitionType196.setter
    def jpdl31_ProcessDefinitionType196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType196", None)
        self.__jpdl31_ProcessDefinitionType196 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TaskType197"):
                    opp_val = getattr(item, "jpdl31_TaskType197", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TaskType197", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TaskType197"):
                    opp_val = getattr(item, "jpdl31_TaskType197", None)
                    
                    setattr(item, "jpdl31_TaskType197", self)
                    

    @property
    def jpdl31_ProcessDefinitionType160(self):
        return self.__jpdl31_ProcessDefinitionType160

    @jpdl31_ProcessDefinitionType160.setter
    def jpdl31_ProcessDefinitionType160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType160", None)
        self.__jpdl31_ProcessDefinitionType160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_SuperStateType161"):
                    opp_val = getattr(item, "jpdl31_SuperStateType161", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_SuperStateType161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_SuperStateType161"):
                    opp_val = getattr(item, "jpdl31_SuperStateType161", None)
                    
                    setattr(item, "jpdl31_SuperStateType161", self)
                    

    @property
    def jpdl31_ProcessDefinitionType169(self):
        return self.__jpdl31_ProcessDefinitionType169

    @jpdl31_ProcessDefinitionType169.setter
    def jpdl31_ProcessDefinitionType169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType169", None)
        self.__jpdl31_ProcessDefinitionType169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_JoinType170"):
                    opp_val = getattr(item, "jpdl31_JoinType170", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_JoinType170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_JoinType170"):
                    opp_val = getattr(item, "jpdl31_JoinType170", None)
                    
                    setattr(item, "jpdl31_JoinType170", self)
                    

    @property
    def jpdl31_ProcessDefinitionType193(self):
        return self.__jpdl31_ProcessDefinitionType193

    @jpdl31_ProcessDefinitionType193.setter
    def jpdl31_ProcessDefinitionType193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType193", None)
        self.__jpdl31_ProcessDefinitionType193 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType194"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType194", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType194", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType194"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType194", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType194", self)
                    

    @property
    def jpdl31_ProcessDefinitionType178(self):
        return self.__jpdl31_ProcessDefinitionType178

    @jpdl31_ProcessDefinitionType178.setter
    def jpdl31_ProcessDefinitionType178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType178", None)
        self.__jpdl31_ProcessDefinitionType178 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ActionType179"):
                    opp_val = getattr(item, "jpdl31_ActionType179", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ActionType179", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ActionType179"):
                    opp_val = getattr(item, "jpdl31_ActionType179", None)
                    
                    setattr(item, "jpdl31_ActionType179", self)
                    

class jpdl31_NodeType:

    def __init__(self, nodeContentElements: str, async: str, name: str, jpdl31_NodeType: "jpdl31_DocumentRoot" = None, jpdl31_NodeType121: "jpdl31_ActionType" = None, jpdl31_NodeType124: "jpdl31_ScriptType" = None, jpdl31_NodeType127: "jpdl31_CreateTimerType" = None, jpdl31_NodeType130: "jpdl31_CancelTimerType" = None, jpdl31_NodeType133: set["jpdl31_EventType"] = None, jpdl31_NodeType142: set["jpdl31_TransitionType"] = None, jpdl31_NodeType136: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_NodeType139: set["jpdl31_TimerType"] = None, jpdl31_NodeType152: "jpdl31_ProcessDefinitionType" = None, jpdl31_NodeType241: "jpdl31_SuperStateType" = None):
        self.nodeContentElements = nodeContentElements
        self.async = async
        self.name = name
        self.jpdl31_NodeType = jpdl31_NodeType
        self.jpdl31_NodeType121 = jpdl31_NodeType121
        self.jpdl31_NodeType124 = jpdl31_NodeType124
        self.jpdl31_NodeType127 = jpdl31_NodeType127
        self.jpdl31_NodeType130 = jpdl31_NodeType130
        self.jpdl31_NodeType133 = jpdl31_NodeType133 if jpdl31_NodeType133 is not None else set()
        self.jpdl31_NodeType142 = jpdl31_NodeType142 if jpdl31_NodeType142 is not None else set()
        self.jpdl31_NodeType136 = jpdl31_NodeType136 if jpdl31_NodeType136 is not None else set()
        self.jpdl31_NodeType139 = jpdl31_NodeType139 if jpdl31_NodeType139 is not None else set()
        self.jpdl31_NodeType152 = jpdl31_NodeType152
        self.jpdl31_NodeType241 = jpdl31_NodeType241
        
    @property
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

    @property
    def nodeContentElements(self) -> str:
        return self.__nodeContentElements

    @nodeContentElements.setter
    def nodeContentElements(self, nodeContentElements: str):
        self.__nodeContentElements = nodeContentElements

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl31_NodeType152(self):
        return self.__jpdl31_NodeType152

    @jpdl31_NodeType152.setter
    def jpdl31_NodeType152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType152", None)
        self.__jpdl31_NodeType152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType151"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType151"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType151", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_NodeType136(self):
        return self.__jpdl31_NodeType136

    @jpdl31_NodeType136.setter
    def jpdl31_NodeType136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType136", None)
        self.__jpdl31_NodeType136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType137"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType137", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType137"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType137", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType137", self)
                    

    @property
    def jpdl31_NodeType139(self):
        return self.__jpdl31_NodeType139

    @jpdl31_NodeType139.setter
    def jpdl31_NodeType139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType139", None)
        self.__jpdl31_NodeType139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType140"):
                    opp_val = getattr(item, "jpdl31_TimerType140", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType140"):
                    opp_val = getattr(item, "jpdl31_TimerType140", None)
                    
                    setattr(item, "jpdl31_TimerType140", self)
                    

    @property
    def jpdl31_NodeType241(self):
        return self.__jpdl31_NodeType241

    @jpdl31_NodeType241.setter
    def jpdl31_NodeType241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType241", None)
        self.__jpdl31_NodeType241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType240"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType240", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType240"):
                opp_val = getattr(value, "jpdl31_SuperStateType240", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType240", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_NodeType133(self):
        return self.__jpdl31_NodeType133

    @jpdl31_NodeType133.setter
    def jpdl31_NodeType133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType133", None)
        self.__jpdl31_NodeType133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType134"):
                    opp_val = getattr(item, "jpdl31_EventType134", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType134"):
                    opp_val = getattr(item, "jpdl31_EventType134", None)
                    
                    setattr(item, "jpdl31_EventType134", self)
                    

    @property
    def jpdl31_NodeType127(self):
        return self.__jpdl31_NodeType127

    @jpdl31_NodeType127.setter
    def jpdl31_NodeType127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType127", None)
        self.__jpdl31_NodeType127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_CreateTimerType128"):
                opp_val = getattr(old_value, "jpdl31_CreateTimerType128", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_CreateTimerType128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_CreateTimerType128"):
                opp_val = getattr(value, "jpdl31_CreateTimerType128", None)
                setattr(value, "jpdl31_CreateTimerType128", self)

    @property
    def jpdl31_NodeType(self):
        return self.__jpdl31_NodeType

    @jpdl31_NodeType.setter
    def jpdl31_NodeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType", None)
        self.__jpdl31_NodeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot43"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot43"):
                opp_val = getattr(value, "jpdl31_DocumentRoot43", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_NodeType121(self):
        return self.__jpdl31_NodeType121

    @jpdl31_NodeType121.setter
    def jpdl31_NodeType121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType121", None)
        self.__jpdl31_NodeType121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ActionType122"):
                opp_val = getattr(old_value, "jpdl31_ActionType122", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_ActionType122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ActionType122"):
                opp_val = getattr(value, "jpdl31_ActionType122", None)
                setattr(value, "jpdl31_ActionType122", self)

    @property
    def jpdl31_NodeType142(self):
        return self.__jpdl31_NodeType142

    @jpdl31_NodeType142.setter
    def jpdl31_NodeType142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType142", None)
        self.__jpdl31_NodeType142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType143"):
                    opp_val = getattr(item, "jpdl31_TransitionType143", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType143"):
                    opp_val = getattr(item, "jpdl31_TransitionType143", None)
                    
                    setattr(item, "jpdl31_TransitionType143", self)
                    

    @property
    def jpdl31_NodeType130(self):
        return self.__jpdl31_NodeType130

    @jpdl31_NodeType130.setter
    def jpdl31_NodeType130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType130", None)
        self.__jpdl31_NodeType130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_CancelTimerType131"):
                opp_val = getattr(old_value, "jpdl31_CancelTimerType131", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_CancelTimerType131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_CancelTimerType131"):
                opp_val = getattr(value, "jpdl31_CancelTimerType131", None)
                setattr(value, "jpdl31_CancelTimerType131", self)

    @property
    def jpdl31_NodeType124(self):
        return self.__jpdl31_NodeType124

    @jpdl31_NodeType124.setter
    def jpdl31_NodeType124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType124", None)
        self.__jpdl31_NodeType124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ScriptType125"):
                opp_val = getattr(old_value, "jpdl31_ScriptType125", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_ScriptType125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ScriptType125"):
                opp_val = getattr(value, "jpdl31_ScriptType125", None)
                setattr(value, "jpdl31_ScriptType125", self)

class jpdl31_JoinType:

    def __init__(self, nodeContentElements: str, async: str, name: str, jpdl31_JoinType: "jpdl31_DocumentRoot" = None, jpdl31_JoinType109: set["jpdl31_EventType"] = None, jpdl31_JoinType112: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_JoinType118: set["jpdl31_TransitionType"] = None, jpdl31_JoinType115: set["jpdl31_TimerType"] = None, jpdl31_JoinType170: "jpdl31_ProcessDefinitionType" = None, jpdl31_JoinType259: "jpdl31_SuperStateType" = None):
        self.nodeContentElements = nodeContentElements
        self.async = async
        self.name = name
        self.jpdl31_JoinType = jpdl31_JoinType
        self.jpdl31_JoinType109 = jpdl31_JoinType109 if jpdl31_JoinType109 is not None else set()
        self.jpdl31_JoinType112 = jpdl31_JoinType112 if jpdl31_JoinType112 is not None else set()
        self.jpdl31_JoinType118 = jpdl31_JoinType118 if jpdl31_JoinType118 is not None else set()
        self.jpdl31_JoinType115 = jpdl31_JoinType115 if jpdl31_JoinType115 is not None else set()
        self.jpdl31_JoinType170 = jpdl31_JoinType170
        self.jpdl31_JoinType259 = jpdl31_JoinType259
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

    @property
    def nodeContentElements(self) -> str:
        return self.__nodeContentElements

    @nodeContentElements.setter
    def nodeContentElements(self, nodeContentElements: str):
        self.__nodeContentElements = nodeContentElements

    @property
    def jpdl31_JoinType109(self):
        return self.__jpdl31_JoinType109

    @jpdl31_JoinType109.setter
    def jpdl31_JoinType109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_JoinType__jpdl31_JoinType109", None)
        self.__jpdl31_JoinType109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType110"):
                    opp_val = getattr(item, "jpdl31_EventType110", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType110"):
                    opp_val = getattr(item, "jpdl31_EventType110", None)
                    
                    setattr(item, "jpdl31_EventType110", self)
                    

    @property
    def jpdl31_JoinType170(self):
        return self.__jpdl31_JoinType170

    @jpdl31_JoinType170.setter
    def jpdl31_JoinType170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_JoinType__jpdl31_JoinType170", None)
        self.__jpdl31_JoinType170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType169"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType169", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType169"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType169", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType169", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_JoinType115(self):
        return self.__jpdl31_JoinType115

    @jpdl31_JoinType115.setter
    def jpdl31_JoinType115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_JoinType__jpdl31_JoinType115", None)
        self.__jpdl31_JoinType115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType116"):
                    opp_val = getattr(item, "jpdl31_TimerType116", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType116"):
                    opp_val = getattr(item, "jpdl31_TimerType116", None)
                    
                    setattr(item, "jpdl31_TimerType116", self)
                    

    @property
    def jpdl31_JoinType(self):
        return self.__jpdl31_JoinType

    @jpdl31_JoinType.setter
    def jpdl31_JoinType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_JoinType__jpdl31_JoinType", None)
        self.__jpdl31_JoinType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot41"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot41"):
                opp_val = getattr(value, "jpdl31_DocumentRoot41", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_JoinType259(self):
        return self.__jpdl31_JoinType259

    @jpdl31_JoinType259.setter
    def jpdl31_JoinType259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_JoinType__jpdl31_JoinType259", None)
        self.__jpdl31_JoinType259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType258"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType258", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType258"):
                opp_val = getattr(value, "jpdl31_SuperStateType258", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType258", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_JoinType112(self):
        return self.__jpdl31_JoinType112

    @jpdl31_JoinType112.setter
    def jpdl31_JoinType112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_JoinType__jpdl31_JoinType112", None)
        self.__jpdl31_JoinType112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType113"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType113", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType113"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType113", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType113", self)
                    

    @property
    def jpdl31_JoinType118(self):
        return self.__jpdl31_JoinType118

    @jpdl31_JoinType118.setter
    def jpdl31_JoinType118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_JoinType__jpdl31_JoinType118", None)
        self.__jpdl31_JoinType118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType119"):
                    opp_val = getattr(item, "jpdl31_TransitionType119", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType119"):
                    opp_val = getattr(item, "jpdl31_TransitionType119", None)
                    
                    setattr(item, "jpdl31_TransitionType119", self)
                    

class jpdl31_ForkType:

    def __init__(self, group: str, async: str, name: str, jpdl31_ForkType: "jpdl31_DocumentRoot" = None, jpdl31_ForkType94: set["jpdl31_ScriptType"] = None, jpdl31_ForkType97: set["jpdl31_EventType"] = None, jpdl31_ForkType106: set["jpdl31_TransitionType"] = None, jpdl31_ForkType100: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_ForkType103: set["jpdl31_TimerType"] = None, jpdl31_ForkType167: "jpdl31_ProcessDefinitionType" = None, jpdl31_ForkType256: "jpdl31_SuperStateType" = None):
        self.group = group
        self.async = async
        self.name = name
        self.jpdl31_ForkType = jpdl31_ForkType
        self.jpdl31_ForkType94 = jpdl31_ForkType94 if jpdl31_ForkType94 is not None else set()
        self.jpdl31_ForkType97 = jpdl31_ForkType97 if jpdl31_ForkType97 is not None else set()
        self.jpdl31_ForkType106 = jpdl31_ForkType106 if jpdl31_ForkType106 is not None else set()
        self.jpdl31_ForkType100 = jpdl31_ForkType100 if jpdl31_ForkType100 is not None else set()
        self.jpdl31_ForkType103 = jpdl31_ForkType103 if jpdl31_ForkType103 is not None else set()
        self.jpdl31_ForkType167 = jpdl31_ForkType167
        self.jpdl31_ForkType256 = jpdl31_ForkType256
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def jpdl31_ForkType94(self):
        return self.__jpdl31_ForkType94

    @jpdl31_ForkType94.setter
    def jpdl31_ForkType94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ForkType__jpdl31_ForkType94", None)
        self.__jpdl31_ForkType94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ScriptType95"):
                    opp_val = getattr(item, "jpdl31_ScriptType95", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ScriptType95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ScriptType95"):
                    opp_val = getattr(item, "jpdl31_ScriptType95", None)
                    
                    setattr(item, "jpdl31_ScriptType95", self)
                    

    @property
    def jpdl31_ForkType256(self):
        return self.__jpdl31_ForkType256

    @jpdl31_ForkType256.setter
    def jpdl31_ForkType256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ForkType__jpdl31_ForkType256", None)
        self.__jpdl31_ForkType256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType255"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType255", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType255"):
                opp_val = getattr(value, "jpdl31_SuperStateType255", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType255", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ForkType167(self):
        return self.__jpdl31_ForkType167

    @jpdl31_ForkType167.setter
    def jpdl31_ForkType167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ForkType__jpdl31_ForkType167", None)
        self.__jpdl31_ForkType167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType166"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType166", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType166"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType166", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType166", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ForkType97(self):
        return self.__jpdl31_ForkType97

    @jpdl31_ForkType97.setter
    def jpdl31_ForkType97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ForkType__jpdl31_ForkType97", None)
        self.__jpdl31_ForkType97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType98"):
                    opp_val = getattr(item, "jpdl31_EventType98", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType98"):
                    opp_val = getattr(item, "jpdl31_EventType98", None)
                    
                    setattr(item, "jpdl31_EventType98", self)
                    

    @property
    def jpdl31_ForkType106(self):
        return self.__jpdl31_ForkType106

    @jpdl31_ForkType106.setter
    def jpdl31_ForkType106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ForkType__jpdl31_ForkType106", None)
        self.__jpdl31_ForkType106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType107"):
                    opp_val = getattr(item, "jpdl31_TransitionType107", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType107"):
                    opp_val = getattr(item, "jpdl31_TransitionType107", None)
                    
                    setattr(item, "jpdl31_TransitionType107", self)
                    

    @property
    def jpdl31_ForkType(self):
        return self.__jpdl31_ForkType

    @jpdl31_ForkType.setter
    def jpdl31_ForkType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ForkType__jpdl31_ForkType", None)
        self.__jpdl31_ForkType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot39"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot39"):
                opp_val = getattr(value, "jpdl31_DocumentRoot39", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ForkType100(self):
        return self.__jpdl31_ForkType100

    @jpdl31_ForkType100.setter
    def jpdl31_ForkType100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ForkType__jpdl31_ForkType100", None)
        self.__jpdl31_ForkType100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType101"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType101", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType101"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType101", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType101", self)
                    

    @property
    def jpdl31_ForkType103(self):
        return self.__jpdl31_ForkType103

    @jpdl31_ForkType103.setter
    def jpdl31_ForkType103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ForkType__jpdl31_ForkType103", None)
        self.__jpdl31_ForkType103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType104"):
                    opp_val = getattr(item, "jpdl31_TimerType104", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType104"):
                    opp_val = getattr(item, "jpdl31_TimerType104", None)
                    
                    setattr(item, "jpdl31_TimerType104", self)
                    

class jpdl31_EndStateType:

    def __init__(self, group: str, name: str, jpdl31_EndStateType: "jpdl31_DocumentRoot" = None, jpdl31_EndStateType70: set["jpdl31_EventType"] = None, jpdl31_EndStateType73: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_EndStateType176: "jpdl31_ProcessDefinitionType" = None, jpdl31_EndStateType265: "jpdl31_SuperStateType" = None):
        self.group = group
        self.name = name
        self.jpdl31_EndStateType = jpdl31_EndStateType
        self.jpdl31_EndStateType70 = jpdl31_EndStateType70 if jpdl31_EndStateType70 is not None else set()
        self.jpdl31_EndStateType73 = jpdl31_EndStateType73 if jpdl31_EndStateType73 is not None else set()
        self.jpdl31_EndStateType176 = jpdl31_EndStateType176
        self.jpdl31_EndStateType265 = jpdl31_EndStateType265
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def jpdl31_EndStateType73(self):
        return self.__jpdl31_EndStateType73

    @jpdl31_EndStateType73.setter
    def jpdl31_EndStateType73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EndStateType__jpdl31_EndStateType73", None)
        self.__jpdl31_EndStateType73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType74"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType74", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType74"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType74", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType74", self)
                    

    @property
    def jpdl31_EndStateType176(self):
        return self.__jpdl31_EndStateType176

    @jpdl31_EndStateType176.setter
    def jpdl31_EndStateType176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EndStateType__jpdl31_EndStateType176", None)
        self.__jpdl31_EndStateType176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType175"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType175"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType175", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EndStateType(self):
        return self.__jpdl31_EndStateType

    @jpdl31_EndStateType.setter
    def jpdl31_EndStateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EndStateType__jpdl31_EndStateType", None)
        self.__jpdl31_EndStateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot31"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot31"):
                opp_val = getattr(value, "jpdl31_DocumentRoot31", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EndStateType70(self):
        return self.__jpdl31_EndStateType70

    @jpdl31_EndStateType70.setter
    def jpdl31_EndStateType70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EndStateType__jpdl31_EndStateType70", None)
        self.__jpdl31_EndStateType70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType71"):
                    opp_val = getattr(item, "jpdl31_EventType71", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType71"):
                    opp_val = getattr(item, "jpdl31_EventType71", None)
                    
                    setattr(item, "jpdl31_EventType71", self)
                    

    @property
    def jpdl31_EndStateType265(self):
        return self.__jpdl31_EndStateType265

    @jpdl31_EndStateType265.setter
    def jpdl31_EndStateType265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EndStateType__jpdl31_EndStateType265", None)
        self.__jpdl31_EndStateType265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType264"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType264", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType264"):
                opp_val = getattr(value, "jpdl31_SuperStateType264", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType264", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_DocumentRoot:

    def __init__(self, mixed: str, jpdl31_DocumentRoot: set["jpdl31_EStringToStringMapEntry"] = None, jpdl31_DocumentRoot12: set["jpdl31_EStringToStringMapEntry"] = None, jpdl31_DocumentRoot15: set["jpdl31_ActionType"] = None, jpdl31_DocumentRoot18: set["jpdl31_AssignmentType"] = None, jpdl31_DocumentRoot20: set["jpdl31_CancelTimerType"] = None, jpdl31_DocumentRoot22: set["jpdl31_Delegation"] = None, jpdl31_DocumentRoot31: set["jpdl31_EndStateType"] = None, jpdl31_DocumentRoot33: set["jpdl31_EventType"] = None, jpdl31_DocumentRoot36: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_DocumentRoot39: set["jpdl31_ForkType"] = None, jpdl31_DocumentRoot41: set["jpdl31_JoinType"] = None, jpdl31_DocumentRoot43: set["jpdl31_NodeType"] = None, jpdl31_DocumentRoot45: set["jpdl31_ProcessDefinitionType"] = None, jpdl31_DocumentRoot25: set["jpdl31_CreateTimerType"] = None, jpdl31_DocumentRoot28: set["jpdl31_DecisionType"] = None, jpdl31_DocumentRoot49: set["jpdl31_ScriptType"] = None, jpdl31_DocumentRoot52: set["jpdl31_StartStateType"] = None, jpdl31_DocumentRoot54: set["jpdl31_StateType"] = None, jpdl31_DocumentRoot56: set["jpdl31_SuperStateType"] = None, jpdl31_DocumentRoot58: set["jpdl31_SwimlaneType"] = None, jpdl31_DocumentRoot60: set["jpdl31_TaskType"] = None, jpdl31_DocumentRoot47: set["jpdl31_ProcessStateType"] = None, jpdl31_DocumentRoot64: set["jpdl31_TimerType"] = None, jpdl31_DocumentRoot66: set["jpdl31_TransitionType"] = None, jpdl31_DocumentRoot68: set["jpdl31_VariableType"] = None, jpdl31_DocumentRoot62: set["jpdl31_TaskNodeType"] = None):
        self.mixed = mixed
        self.jpdl31_DocumentRoot = jpdl31_DocumentRoot if jpdl31_DocumentRoot is not None else set()
        self.jpdl31_DocumentRoot12 = jpdl31_DocumentRoot12 if jpdl31_DocumentRoot12 is not None else set()
        self.jpdl31_DocumentRoot15 = jpdl31_DocumentRoot15 if jpdl31_DocumentRoot15 is not None else set()
        self.jpdl31_DocumentRoot18 = jpdl31_DocumentRoot18 if jpdl31_DocumentRoot18 is not None else set()
        self.jpdl31_DocumentRoot20 = jpdl31_DocumentRoot20 if jpdl31_DocumentRoot20 is not None else set()
        self.jpdl31_DocumentRoot22 = jpdl31_DocumentRoot22 if jpdl31_DocumentRoot22 is not None else set()
        self.jpdl31_DocumentRoot31 = jpdl31_DocumentRoot31 if jpdl31_DocumentRoot31 is not None else set()
        self.jpdl31_DocumentRoot33 = jpdl31_DocumentRoot33 if jpdl31_DocumentRoot33 is not None else set()
        self.jpdl31_DocumentRoot36 = jpdl31_DocumentRoot36 if jpdl31_DocumentRoot36 is not None else set()
        self.jpdl31_DocumentRoot39 = jpdl31_DocumentRoot39 if jpdl31_DocumentRoot39 is not None else set()
        self.jpdl31_DocumentRoot41 = jpdl31_DocumentRoot41 if jpdl31_DocumentRoot41 is not None else set()
        self.jpdl31_DocumentRoot43 = jpdl31_DocumentRoot43 if jpdl31_DocumentRoot43 is not None else set()
        self.jpdl31_DocumentRoot45 = jpdl31_DocumentRoot45 if jpdl31_DocumentRoot45 is not None else set()
        self.jpdl31_DocumentRoot25 = jpdl31_DocumentRoot25 if jpdl31_DocumentRoot25 is not None else set()
        self.jpdl31_DocumentRoot28 = jpdl31_DocumentRoot28 if jpdl31_DocumentRoot28 is not None else set()
        self.jpdl31_DocumentRoot49 = jpdl31_DocumentRoot49 if jpdl31_DocumentRoot49 is not None else set()
        self.jpdl31_DocumentRoot52 = jpdl31_DocumentRoot52 if jpdl31_DocumentRoot52 is not None else set()
        self.jpdl31_DocumentRoot54 = jpdl31_DocumentRoot54 if jpdl31_DocumentRoot54 is not None else set()
        self.jpdl31_DocumentRoot56 = jpdl31_DocumentRoot56 if jpdl31_DocumentRoot56 is not None else set()
        self.jpdl31_DocumentRoot58 = jpdl31_DocumentRoot58 if jpdl31_DocumentRoot58 is not None else set()
        self.jpdl31_DocumentRoot60 = jpdl31_DocumentRoot60 if jpdl31_DocumentRoot60 is not None else set()
        self.jpdl31_DocumentRoot47 = jpdl31_DocumentRoot47 if jpdl31_DocumentRoot47 is not None else set()
        self.jpdl31_DocumentRoot64 = jpdl31_DocumentRoot64 if jpdl31_DocumentRoot64 is not None else set()
        self.jpdl31_DocumentRoot66 = jpdl31_DocumentRoot66 if jpdl31_DocumentRoot66 is not None else set()
        self.jpdl31_DocumentRoot68 = jpdl31_DocumentRoot68 if jpdl31_DocumentRoot68 is not None else set()
        self.jpdl31_DocumentRoot62 = jpdl31_DocumentRoot62 if jpdl31_DocumentRoot62 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def jpdl31_DocumentRoot(self):
        return self.__jpdl31_DocumentRoot

    @jpdl31_DocumentRoot.setter
    def jpdl31_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot", None)
        self.__jpdl31_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EStringToStringMapEntry"):
                    opp_val = getattr(item, "jpdl31_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EStringToStringMapEntry"):
                    opp_val = getattr(item, "jpdl31_EStringToStringMapEntry", None)
                    
                    setattr(item, "jpdl31_EStringToStringMapEntry", self)
                    

    @property
    def jpdl31_DocumentRoot20(self):
        return self.__jpdl31_DocumentRoot20

    @jpdl31_DocumentRoot20.setter
    def jpdl31_DocumentRoot20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot20", None)
        self.__jpdl31_DocumentRoot20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CancelTimerType"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CancelTimerType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CancelTimerType"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType", None)
                    
                    setattr(item, "jpdl31_CancelTimerType", self)
                    

    @property
    def jpdl31_DocumentRoot15(self):
        return self.__jpdl31_DocumentRoot15

    @jpdl31_DocumentRoot15.setter
    def jpdl31_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot15", None)
        self.__jpdl31_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ActionType16"):
                    opp_val = getattr(item, "jpdl31_ActionType16", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ActionType16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ActionType16"):
                    opp_val = getattr(item, "jpdl31_ActionType16", None)
                    
                    setattr(item, "jpdl31_ActionType16", self)
                    

    @property
    def jpdl31_DocumentRoot62(self):
        return self.__jpdl31_DocumentRoot62

    @jpdl31_DocumentRoot62.setter
    def jpdl31_DocumentRoot62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot62", None)
        self.__jpdl31_DocumentRoot62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TaskNodeType"):
                    opp_val = getattr(item, "jpdl31_TaskNodeType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TaskNodeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TaskNodeType"):
                    opp_val = getattr(item, "jpdl31_TaskNodeType", None)
                    
                    setattr(item, "jpdl31_TaskNodeType", self)
                    

    @property
    def jpdl31_DocumentRoot68(self):
        return self.__jpdl31_DocumentRoot68

    @jpdl31_DocumentRoot68.setter
    def jpdl31_DocumentRoot68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot68", None)
        self.__jpdl31_DocumentRoot68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_VariableType"):
                    opp_val = getattr(item, "jpdl31_VariableType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_VariableType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_VariableType"):
                    opp_val = getattr(item, "jpdl31_VariableType", None)
                    
                    setattr(item, "jpdl31_VariableType", self)
                    

    @property
    def jpdl31_DocumentRoot47(self):
        return self.__jpdl31_DocumentRoot47

    @jpdl31_DocumentRoot47.setter
    def jpdl31_DocumentRoot47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot47", None)
        self.__jpdl31_DocumentRoot47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ProcessStateType"):
                    opp_val = getattr(item, "jpdl31_ProcessStateType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ProcessStateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ProcessStateType"):
                    opp_val = getattr(item, "jpdl31_ProcessStateType", None)
                    
                    setattr(item, "jpdl31_ProcessStateType", self)
                    

    @property
    def jpdl31_DocumentRoot12(self):
        return self.__jpdl31_DocumentRoot12

    @jpdl31_DocumentRoot12.setter
    def jpdl31_DocumentRoot12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot12", None)
        self.__jpdl31_DocumentRoot12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EStringToStringMapEntry13"):
                    opp_val = getattr(item, "jpdl31_EStringToStringMapEntry13", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EStringToStringMapEntry13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EStringToStringMapEntry13"):
                    opp_val = getattr(item, "jpdl31_EStringToStringMapEntry13", None)
                    
                    setattr(item, "jpdl31_EStringToStringMapEntry13", self)
                    

    @property
    def jpdl31_DocumentRoot66(self):
        return self.__jpdl31_DocumentRoot66

    @jpdl31_DocumentRoot66.setter
    def jpdl31_DocumentRoot66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot66", None)
        self.__jpdl31_DocumentRoot66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType"):
                    opp_val = getattr(item, "jpdl31_TransitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType"):
                    opp_val = getattr(item, "jpdl31_TransitionType", None)
                    
                    setattr(item, "jpdl31_TransitionType", self)
                    

    @property
    def jpdl31_DocumentRoot54(self):
        return self.__jpdl31_DocumentRoot54

    @jpdl31_DocumentRoot54.setter
    def jpdl31_DocumentRoot54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot54", None)
        self.__jpdl31_DocumentRoot54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_StateType"):
                    opp_val = getattr(item, "jpdl31_StateType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_StateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_StateType"):
                    opp_val = getattr(item, "jpdl31_StateType", None)
                    
                    setattr(item, "jpdl31_StateType", self)
                    

    @property
    def jpdl31_DocumentRoot45(self):
        return self.__jpdl31_DocumentRoot45

    @jpdl31_DocumentRoot45.setter
    def jpdl31_DocumentRoot45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot45", None)
        self.__jpdl31_DocumentRoot45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ProcessDefinitionType"):
                    opp_val = getattr(item, "jpdl31_ProcessDefinitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ProcessDefinitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ProcessDefinitionType"):
                    opp_val = getattr(item, "jpdl31_ProcessDefinitionType", None)
                    
                    setattr(item, "jpdl31_ProcessDefinitionType", self)
                    

    @property
    def jpdl31_DocumentRoot22(self):
        return self.__jpdl31_DocumentRoot22

    @jpdl31_DocumentRoot22.setter
    def jpdl31_DocumentRoot22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot22", None)
        self.__jpdl31_DocumentRoot22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Delegation23"):
                    opp_val = getattr(item, "jpdl31_Delegation23", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Delegation23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Delegation23"):
                    opp_val = getattr(item, "jpdl31_Delegation23", None)
                    
                    setattr(item, "jpdl31_Delegation23", self)
                    

    @property
    def jpdl31_DocumentRoot36(self):
        return self.__jpdl31_DocumentRoot36

    @jpdl31_DocumentRoot36.setter
    def jpdl31_DocumentRoot36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot36", None)
        self.__jpdl31_DocumentRoot36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType37"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType37", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType37"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType37", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType37", self)
                    

    @property
    def jpdl31_DocumentRoot43(self):
        return self.__jpdl31_DocumentRoot43

    @jpdl31_DocumentRoot43.setter
    def jpdl31_DocumentRoot43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot43", None)
        self.__jpdl31_DocumentRoot43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_NodeType"):
                    opp_val = getattr(item, "jpdl31_NodeType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_NodeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_NodeType"):
                    opp_val = getattr(item, "jpdl31_NodeType", None)
                    
                    setattr(item, "jpdl31_NodeType", self)
                    

    @property
    def jpdl31_DocumentRoot18(self):
        return self.__jpdl31_DocumentRoot18

    @jpdl31_DocumentRoot18.setter
    def jpdl31_DocumentRoot18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot18", None)
        self.__jpdl31_DocumentRoot18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_AssignmentType"):
                    opp_val = getattr(item, "jpdl31_AssignmentType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_AssignmentType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_AssignmentType"):
                    opp_val = getattr(item, "jpdl31_AssignmentType", None)
                    
                    setattr(item, "jpdl31_AssignmentType", self)
                    

    @property
    def jpdl31_DocumentRoot58(self):
        return self.__jpdl31_DocumentRoot58

    @jpdl31_DocumentRoot58.setter
    def jpdl31_DocumentRoot58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot58", None)
        self.__jpdl31_DocumentRoot58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_SwimlaneType"):
                    opp_val = getattr(item, "jpdl31_SwimlaneType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_SwimlaneType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_SwimlaneType"):
                    opp_val = getattr(item, "jpdl31_SwimlaneType", None)
                    
                    setattr(item, "jpdl31_SwimlaneType", self)
                    

    @property
    def jpdl31_DocumentRoot33(self):
        return self.__jpdl31_DocumentRoot33

    @jpdl31_DocumentRoot33.setter
    def jpdl31_DocumentRoot33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot33", None)
        self.__jpdl31_DocumentRoot33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType34"):
                    opp_val = getattr(item, "jpdl31_EventType34", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType34"):
                    opp_val = getattr(item, "jpdl31_EventType34", None)
                    
                    setattr(item, "jpdl31_EventType34", self)
                    

    @property
    def jpdl31_DocumentRoot64(self):
        return self.__jpdl31_DocumentRoot64

    @jpdl31_DocumentRoot64.setter
    def jpdl31_DocumentRoot64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot64", None)
        self.__jpdl31_DocumentRoot64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType"):
                    opp_val = getattr(item, "jpdl31_TimerType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType"):
                    opp_val = getattr(item, "jpdl31_TimerType", None)
                    
                    setattr(item, "jpdl31_TimerType", self)
                    

    @property
    def jpdl31_DocumentRoot41(self):
        return self.__jpdl31_DocumentRoot41

    @jpdl31_DocumentRoot41.setter
    def jpdl31_DocumentRoot41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot41", None)
        self.__jpdl31_DocumentRoot41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_JoinType"):
                    opp_val = getattr(item, "jpdl31_JoinType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_JoinType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_JoinType"):
                    opp_val = getattr(item, "jpdl31_JoinType", None)
                    
                    setattr(item, "jpdl31_JoinType", self)
                    

    @property
    def jpdl31_DocumentRoot60(self):
        return self.__jpdl31_DocumentRoot60

    @jpdl31_DocumentRoot60.setter
    def jpdl31_DocumentRoot60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot60", None)
        self.__jpdl31_DocumentRoot60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TaskType"):
                    opp_val = getattr(item, "jpdl31_TaskType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TaskType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TaskType"):
                    opp_val = getattr(item, "jpdl31_TaskType", None)
                    
                    setattr(item, "jpdl31_TaskType", self)
                    

    @property
    def jpdl31_DocumentRoot39(self):
        return self.__jpdl31_DocumentRoot39

    @jpdl31_DocumentRoot39.setter
    def jpdl31_DocumentRoot39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot39", None)
        self.__jpdl31_DocumentRoot39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ForkType"):
                    opp_val = getattr(item, "jpdl31_ForkType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ForkType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ForkType"):
                    opp_val = getattr(item, "jpdl31_ForkType", None)
                    
                    setattr(item, "jpdl31_ForkType", self)
                    

    @property
    def jpdl31_DocumentRoot31(self):
        return self.__jpdl31_DocumentRoot31

    @jpdl31_DocumentRoot31.setter
    def jpdl31_DocumentRoot31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot31", None)
        self.__jpdl31_DocumentRoot31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EndStateType"):
                    opp_val = getattr(item, "jpdl31_EndStateType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EndStateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EndStateType"):
                    opp_val = getattr(item, "jpdl31_EndStateType", None)
                    
                    setattr(item, "jpdl31_EndStateType", self)
                    

    @property
    def jpdl31_DocumentRoot25(self):
        return self.__jpdl31_DocumentRoot25

    @jpdl31_DocumentRoot25.setter
    def jpdl31_DocumentRoot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot25", None)
        self.__jpdl31_DocumentRoot25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CreateTimerType26"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType26", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CreateTimerType26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CreateTimerType26"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType26", None)
                    
                    setattr(item, "jpdl31_CreateTimerType26", self)
                    

    @property
    def jpdl31_DocumentRoot56(self):
        return self.__jpdl31_DocumentRoot56

    @jpdl31_DocumentRoot56.setter
    def jpdl31_DocumentRoot56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot56", None)
        self.__jpdl31_DocumentRoot56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_SuperStateType"):
                    opp_val = getattr(item, "jpdl31_SuperStateType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_SuperStateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_SuperStateType"):
                    opp_val = getattr(item, "jpdl31_SuperStateType", None)
                    
                    setattr(item, "jpdl31_SuperStateType", self)
                    

    @property
    def jpdl31_DocumentRoot49(self):
        return self.__jpdl31_DocumentRoot49

    @jpdl31_DocumentRoot49.setter
    def jpdl31_DocumentRoot49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot49", None)
        self.__jpdl31_DocumentRoot49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ScriptType50"):
                    opp_val = getattr(item, "jpdl31_ScriptType50", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ScriptType50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ScriptType50"):
                    opp_val = getattr(item, "jpdl31_ScriptType50", None)
                    
                    setattr(item, "jpdl31_ScriptType50", self)
                    

    @property
    def jpdl31_DocumentRoot28(self):
        return self.__jpdl31_DocumentRoot28

    @jpdl31_DocumentRoot28.setter
    def jpdl31_DocumentRoot28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot28", None)
        self.__jpdl31_DocumentRoot28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_DecisionType29"):
                    opp_val = getattr(item, "jpdl31_DecisionType29", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_DecisionType29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_DecisionType29"):
                    opp_val = getattr(item, "jpdl31_DecisionType29", None)
                    
                    setattr(item, "jpdl31_DecisionType29", self)
                    

    @property
    def jpdl31_DocumentRoot52(self):
        return self.__jpdl31_DocumentRoot52

    @jpdl31_DocumentRoot52.setter
    def jpdl31_DocumentRoot52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot52", None)
        self.__jpdl31_DocumentRoot52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_StartStateType"):
                    opp_val = getattr(item, "jpdl31_StartStateType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_StartStateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_StartStateType"):
                    opp_val = getattr(item, "jpdl31_StartStateType", None)
                    
                    setattr(item, "jpdl31_StartStateType", self)
                    

class jpdl31_EStringToStringMapEntry:

    pass
class jpdl31_EventType:

    def __init__(self, actionElements: str, type: str, jpdl31_EventType: "jpdl31_DecisionType" = None, jpdl31_EventType34: "jpdl31_DocumentRoot" = None, jpdl31_EventType71: "jpdl31_EndStateType" = None, jpdl31_EventType76: set["jpdl31_ActionType"] = None, jpdl31_EventType79: set["jpdl31_ScriptType"] = None, jpdl31_EventType82: set["jpdl31_CreateTimerType"] = None, jpdl31_EventType85: set["jpdl31_CancelTimerType"] = None, jpdl31_EventType98: "jpdl31_ForkType" = None, jpdl31_EventType110: "jpdl31_JoinType" = None, jpdl31_EventType134: "jpdl31_NodeType" = None, jpdl31_EventType191: "jpdl31_ProcessDefinitionType" = None, jpdl31_EventType205: "jpdl31_ProcessStateType" = None, jpdl31_EventType229: "jpdl31_StateType" = None, jpdl31_EventType223: "jpdl31_StartStateType" = None, jpdl31_EventType268: "jpdl31_SuperStateType" = None, jpdl31_EventType286: "jpdl31_TaskNodeType" = None, jpdl31_EventType304: "jpdl31_TaskType" = None):
        self.actionElements = actionElements
        self.type = type
        self.jpdl31_EventType = jpdl31_EventType
        self.jpdl31_EventType34 = jpdl31_EventType34
        self.jpdl31_EventType71 = jpdl31_EventType71
        self.jpdl31_EventType76 = jpdl31_EventType76 if jpdl31_EventType76 is not None else set()
        self.jpdl31_EventType79 = jpdl31_EventType79 if jpdl31_EventType79 is not None else set()
        self.jpdl31_EventType82 = jpdl31_EventType82 if jpdl31_EventType82 is not None else set()
        self.jpdl31_EventType85 = jpdl31_EventType85 if jpdl31_EventType85 is not None else set()
        self.jpdl31_EventType98 = jpdl31_EventType98
        self.jpdl31_EventType110 = jpdl31_EventType110
        self.jpdl31_EventType134 = jpdl31_EventType134
        self.jpdl31_EventType191 = jpdl31_EventType191
        self.jpdl31_EventType205 = jpdl31_EventType205
        self.jpdl31_EventType229 = jpdl31_EventType229
        self.jpdl31_EventType223 = jpdl31_EventType223
        self.jpdl31_EventType268 = jpdl31_EventType268
        self.jpdl31_EventType286 = jpdl31_EventType286
        self.jpdl31_EventType304 = jpdl31_EventType304
        
    @property
    def actionElements(self) -> str:
        return self.__actionElements

    @actionElements.setter
    def actionElements(self, actionElements: str):
        self.__actionElements = actionElements

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def jpdl31_EventType76(self):
        return self.__jpdl31_EventType76

    @jpdl31_EventType76.setter
    def jpdl31_EventType76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType76", None)
        self.__jpdl31_EventType76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ActionType77"):
                    opp_val = getattr(item, "jpdl31_ActionType77", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ActionType77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ActionType77"):
                    opp_val = getattr(item, "jpdl31_ActionType77", None)
                    
                    setattr(item, "jpdl31_ActionType77", self)
                    

    @property
    def jpdl31_EventType(self):
        return self.__jpdl31_EventType

    @jpdl31_EventType.setter
    def jpdl31_EventType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType", None)
        self.__jpdl31_EventType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DecisionType5"):
                opp_val = getattr(old_value, "jpdl31_DecisionType5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DecisionType5"):
                opp_val = getattr(value, "jpdl31_DecisionType5", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DecisionType5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EventType268(self):
        return self.__jpdl31_EventType268

    @jpdl31_EventType268.setter
    def jpdl31_EventType268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType268", None)
        self.__jpdl31_EventType268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType267"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType267", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType267"):
                opp_val = getattr(value, "jpdl31_SuperStateType267", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType267", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EventType98(self):
        return self.__jpdl31_EventType98

    @jpdl31_EventType98.setter
    def jpdl31_EventType98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType98", None)
        self.__jpdl31_EventType98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ForkType97"):
                opp_val = getattr(old_value, "jpdl31_ForkType97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ForkType97"):
                opp_val = getattr(value, "jpdl31_ForkType97", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ForkType97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EventType205(self):
        return self.__jpdl31_EventType205

    @jpdl31_EventType205.setter
    def jpdl31_EventType205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType205", None)
        self.__jpdl31_EventType205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessStateType204"):
                opp_val = getattr(old_value, "jpdl31_ProcessStateType204", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessStateType204"):
                opp_val = getattr(value, "jpdl31_ProcessStateType204", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessStateType204", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EventType286(self):
        return self.__jpdl31_EventType286

    @jpdl31_EventType286.setter
    def jpdl31_EventType286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType286", None)
        self.__jpdl31_EventType286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskNodeType285"):
                opp_val = getattr(old_value, "jpdl31_TaskNodeType285", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskNodeType285"):
                opp_val = getattr(value, "jpdl31_TaskNodeType285", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskNodeType285", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EventType304(self):
        return self.__jpdl31_EventType304

    @jpdl31_EventType304.setter
    def jpdl31_EventType304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType304", None)
        self.__jpdl31_EventType304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskType303"):
                opp_val = getattr(old_value, "jpdl31_TaskType303", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskType303"):
                opp_val = getattr(value, "jpdl31_TaskType303", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskType303", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EventType85(self):
        return self.__jpdl31_EventType85

    @jpdl31_EventType85.setter
    def jpdl31_EventType85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType85", None)
        self.__jpdl31_EventType85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CancelTimerType86"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType86", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CancelTimerType86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CancelTimerType86"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType86", None)
                    
                    setattr(item, "jpdl31_CancelTimerType86", self)
                    

    @property
    def jpdl31_EventType34(self):
        return self.__jpdl31_EventType34

    @jpdl31_EventType34.setter
    def jpdl31_EventType34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType34", None)
        self.__jpdl31_EventType34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot33"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot33"):
                opp_val = getattr(value, "jpdl31_DocumentRoot33", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EventType110(self):
        return self.__jpdl31_EventType110

    @jpdl31_EventType110.setter
    def jpdl31_EventType110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType110", None)
        self.__jpdl31_EventType110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_JoinType109"):
                opp_val = getattr(old_value, "jpdl31_JoinType109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_JoinType109"):
                opp_val = getattr(value, "jpdl31_JoinType109", None)
                if opp_val is None:
                    setattr(value, "jpdl31_JoinType109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EventType191(self):
        return self.__jpdl31_EventType191

    @jpdl31_EventType191.setter
    def jpdl31_EventType191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType191", None)
        self.__jpdl31_EventType191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType190"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType190", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType190"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType190", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType190", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EventType79(self):
        return self.__jpdl31_EventType79

    @jpdl31_EventType79.setter
    def jpdl31_EventType79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType79", None)
        self.__jpdl31_EventType79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ScriptType80"):
                    opp_val = getattr(item, "jpdl31_ScriptType80", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ScriptType80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ScriptType80"):
                    opp_val = getattr(item, "jpdl31_ScriptType80", None)
                    
                    setattr(item, "jpdl31_ScriptType80", self)
                    

    @property
    def jpdl31_EventType229(self):
        return self.__jpdl31_EventType229

    @jpdl31_EventType229.setter
    def jpdl31_EventType229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType229", None)
        self.__jpdl31_EventType229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_StateType228"):
                opp_val = getattr(old_value, "jpdl31_StateType228", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_StateType228"):
                opp_val = getattr(value, "jpdl31_StateType228", None)
                if opp_val is None:
                    setattr(value, "jpdl31_StateType228", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EventType82(self):
        return self.__jpdl31_EventType82

    @jpdl31_EventType82.setter
    def jpdl31_EventType82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType82", None)
        self.__jpdl31_EventType82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CreateTimerType83"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType83", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CreateTimerType83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CreateTimerType83"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType83", None)
                    
                    setattr(item, "jpdl31_CreateTimerType83", self)
                    

    @property
    def jpdl31_EventType134(self):
        return self.__jpdl31_EventType134

    @jpdl31_EventType134.setter
    def jpdl31_EventType134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType134", None)
        self.__jpdl31_EventType134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_NodeType133"):
                opp_val = getattr(old_value, "jpdl31_NodeType133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_NodeType133"):
                opp_val = getattr(value, "jpdl31_NodeType133", None)
                if opp_val is None:
                    setattr(value, "jpdl31_NodeType133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EventType223(self):
        return self.__jpdl31_EventType223

    @jpdl31_EventType223.setter
    def jpdl31_EventType223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType223", None)
        self.__jpdl31_EventType223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_StartStateType222"):
                opp_val = getattr(old_value, "jpdl31_StartStateType222", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_StartStateType222"):
                opp_val = getattr(value, "jpdl31_StartStateType222", None)
                if opp_val is None:
                    setattr(value, "jpdl31_StartStateType222", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EventType71(self):
        return self.__jpdl31_EventType71

    @jpdl31_EventType71.setter
    def jpdl31_EventType71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType71", None)
        self.__jpdl31_EventType71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_EndStateType70"):
                opp_val = getattr(old_value, "jpdl31_EndStateType70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_EndStateType70"):
                opp_val = getattr(value, "jpdl31_EndStateType70", None)
                if opp_val is None:
                    setattr(value, "jpdl31_EndStateType70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_TransitionType1:

    def __init__(self, group: str, name: str, to: str, jpdl31_TransitionType1: "jpdl31_DecisionType" = None, jpdl31_TransitionType1330: set["jpdl31_ConditionType"] = None, jpdl31_TransitionType1332: set["jpdl31_ActionType"] = None, jpdl31_TransitionType1335: set["jpdl31_ScriptType"] = None, jpdl31_TransitionType1344: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_TransitionType1338: set["jpdl31_CreateTimerType"] = None, jpdl31_TransitionType1341: set["jpdl31_CancelTimerType"] = None):
        self.group = group
        self.name = name
        self.to = to
        self.jpdl31_TransitionType1 = jpdl31_TransitionType1
        self.jpdl31_TransitionType1330 = jpdl31_TransitionType1330 if jpdl31_TransitionType1330 is not None else set()
        self.jpdl31_TransitionType1332 = jpdl31_TransitionType1332 if jpdl31_TransitionType1332 is not None else set()
        self.jpdl31_TransitionType1335 = jpdl31_TransitionType1335 if jpdl31_TransitionType1335 is not None else set()
        self.jpdl31_TransitionType1344 = jpdl31_TransitionType1344 if jpdl31_TransitionType1344 is not None else set()
        self.jpdl31_TransitionType1338 = jpdl31_TransitionType1338 if jpdl31_TransitionType1338 is not None else set()
        self.jpdl31_TransitionType1341 = jpdl31_TransitionType1341 if jpdl31_TransitionType1341 is not None else set()
        
    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def jpdl31_TransitionType1344(self):
        return self.__jpdl31_TransitionType1344

    @jpdl31_TransitionType1344.setter
    def jpdl31_TransitionType1344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType1__jpdl31_TransitionType1344", None)
        self.__jpdl31_TransitionType1344 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType345"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType345", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType345", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType345"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType345", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType345", self)
                    

    @property
    def jpdl31_TransitionType1330(self):
        return self.__jpdl31_TransitionType1330

    @jpdl31_TransitionType1330.setter
    def jpdl31_TransitionType1330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType1__jpdl31_TransitionType1330", None)
        self.__jpdl31_TransitionType1330 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ConditionType"):
                    opp_val = getattr(item, "jpdl31_ConditionType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ConditionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ConditionType"):
                    opp_val = getattr(item, "jpdl31_ConditionType", None)
                    
                    setattr(item, "jpdl31_ConditionType", self)
                    

    @property
    def jpdl31_TransitionType1335(self):
        return self.__jpdl31_TransitionType1335

    @jpdl31_TransitionType1335.setter
    def jpdl31_TransitionType1335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType1__jpdl31_TransitionType1335", None)
        self.__jpdl31_TransitionType1335 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ScriptType336"):
                    opp_val = getattr(item, "jpdl31_ScriptType336", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ScriptType336", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ScriptType336"):
                    opp_val = getattr(item, "jpdl31_ScriptType336", None)
                    
                    setattr(item, "jpdl31_ScriptType336", self)
                    

    @property
    def jpdl31_TransitionType1(self):
        return self.__jpdl31_TransitionType1

    @jpdl31_TransitionType1.setter
    def jpdl31_TransitionType1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType1__jpdl31_TransitionType1", None)
        self.__jpdl31_TransitionType1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DecisionType9"):
                opp_val = getattr(old_value, "jpdl31_DecisionType9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DecisionType9"):
                opp_val = getattr(value, "jpdl31_DecisionType9", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DecisionType9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType1332(self):
        return self.__jpdl31_TransitionType1332

    @jpdl31_TransitionType1332.setter
    def jpdl31_TransitionType1332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType1__jpdl31_TransitionType1332", None)
        self.__jpdl31_TransitionType1332 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ActionType333"):
                    opp_val = getattr(item, "jpdl31_ActionType333", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ActionType333", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ActionType333"):
                    opp_val = getattr(item, "jpdl31_ActionType333", None)
                    
                    setattr(item, "jpdl31_ActionType333", self)
                    

    @property
    def jpdl31_TransitionType1338(self):
        return self.__jpdl31_TransitionType1338

    @jpdl31_TransitionType1338.setter
    def jpdl31_TransitionType1338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType1__jpdl31_TransitionType1338", None)
        self.__jpdl31_TransitionType1338 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CreateTimerType339"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType339", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CreateTimerType339", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CreateTimerType339"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType339", None)
                    
                    setattr(item, "jpdl31_CreateTimerType339", self)
                    

    @property
    def jpdl31_TransitionType1341(self):
        return self.__jpdl31_TransitionType1341

    @jpdl31_TransitionType1341.setter
    def jpdl31_TransitionType1341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType1__jpdl31_TransitionType1341", None)
        self.__jpdl31_TransitionType1341 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CancelTimerType342"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType342", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CancelTimerType342", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CancelTimerType342"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType342", None)
                    
                    setattr(item, "jpdl31_CancelTimerType342", self)
                    

class jpdl31_ExceptionHandlerType:

    def __init__(self, exceptionClass: str, group: str, jpdl31_ExceptionHandlerType: "jpdl31_DecisionType" = None, jpdl31_ExceptionHandlerType37: "jpdl31_DocumentRoot" = None, jpdl31_ExceptionHandlerType74: "jpdl31_EndStateType" = None, jpdl31_ExceptionHandlerType88: set["jpdl31_ActionType"] = None, jpdl31_ExceptionHandlerType91: set["jpdl31_ScriptType"] = None, jpdl31_ExceptionHandlerType101: "jpdl31_ForkType" = None, jpdl31_ExceptionHandlerType113: "jpdl31_JoinType" = None, jpdl31_ExceptionHandlerType137: "jpdl31_NodeType" = None, jpdl31_ExceptionHandlerType194: "jpdl31_ProcessDefinitionType" = None, jpdl31_ExceptionHandlerType208: "jpdl31_ProcessStateType" = None, jpdl31_ExceptionHandlerType226: "jpdl31_StartStateType" = None, jpdl31_ExceptionHandlerType232: "jpdl31_StateType" = None, jpdl31_ExceptionHandlerType271: "jpdl31_SuperStateType" = None, jpdl31_ExceptionHandlerType289: "jpdl31_TaskNodeType" = None, jpdl31_ExceptionHandlerType328: "jpdl31_TransitionType" = None, jpdl31_ExceptionHandlerType345: "jpdl31_TransitionType1" = None):
        self.exceptionClass = exceptionClass
        self.group = group
        self.jpdl31_ExceptionHandlerType = jpdl31_ExceptionHandlerType
        self.jpdl31_ExceptionHandlerType37 = jpdl31_ExceptionHandlerType37
        self.jpdl31_ExceptionHandlerType74 = jpdl31_ExceptionHandlerType74
        self.jpdl31_ExceptionHandlerType88 = jpdl31_ExceptionHandlerType88 if jpdl31_ExceptionHandlerType88 is not None else set()
        self.jpdl31_ExceptionHandlerType91 = jpdl31_ExceptionHandlerType91 if jpdl31_ExceptionHandlerType91 is not None else set()
        self.jpdl31_ExceptionHandlerType101 = jpdl31_ExceptionHandlerType101
        self.jpdl31_ExceptionHandlerType113 = jpdl31_ExceptionHandlerType113
        self.jpdl31_ExceptionHandlerType137 = jpdl31_ExceptionHandlerType137
        self.jpdl31_ExceptionHandlerType194 = jpdl31_ExceptionHandlerType194
        self.jpdl31_ExceptionHandlerType208 = jpdl31_ExceptionHandlerType208
        self.jpdl31_ExceptionHandlerType226 = jpdl31_ExceptionHandlerType226
        self.jpdl31_ExceptionHandlerType232 = jpdl31_ExceptionHandlerType232
        self.jpdl31_ExceptionHandlerType271 = jpdl31_ExceptionHandlerType271
        self.jpdl31_ExceptionHandlerType289 = jpdl31_ExceptionHandlerType289
        self.jpdl31_ExceptionHandlerType328 = jpdl31_ExceptionHandlerType328
        self.jpdl31_ExceptionHandlerType345 = jpdl31_ExceptionHandlerType345
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def exceptionClass(self) -> str:
        return self.__exceptionClass

    @exceptionClass.setter
    def exceptionClass(self, exceptionClass: str):
        self.__exceptionClass = exceptionClass

    @property
    def jpdl31_ExceptionHandlerType271(self):
        return self.__jpdl31_ExceptionHandlerType271

    @jpdl31_ExceptionHandlerType271.setter
    def jpdl31_ExceptionHandlerType271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType271", None)
        self.__jpdl31_ExceptionHandlerType271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType270"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType270", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType270"):
                opp_val = getattr(value, "jpdl31_SuperStateType270", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType270", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType328(self):
        return self.__jpdl31_ExceptionHandlerType328

    @jpdl31_ExceptionHandlerType328.setter
    def jpdl31_ExceptionHandlerType328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType328", None)
        self.__jpdl31_ExceptionHandlerType328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType327"):
                opp_val = getattr(old_value, "jpdl31_TransitionType327", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType327"):
                opp_val = getattr(value, "jpdl31_TransitionType327", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType327", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType(self):
        return self.__jpdl31_ExceptionHandlerType

    @jpdl31_ExceptionHandlerType.setter
    def jpdl31_ExceptionHandlerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType", None)
        self.__jpdl31_ExceptionHandlerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DecisionType7"):
                opp_val = getattr(old_value, "jpdl31_DecisionType7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DecisionType7"):
                opp_val = getattr(value, "jpdl31_DecisionType7", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DecisionType7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType88(self):
        return self.__jpdl31_ExceptionHandlerType88

    @jpdl31_ExceptionHandlerType88.setter
    def jpdl31_ExceptionHandlerType88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType88", None)
        self.__jpdl31_ExceptionHandlerType88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ActionType89"):
                    opp_val = getattr(item, "jpdl31_ActionType89", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ActionType89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ActionType89"):
                    opp_val = getattr(item, "jpdl31_ActionType89", None)
                    
                    setattr(item, "jpdl31_ActionType89", self)
                    

    @property
    def jpdl31_ExceptionHandlerType289(self):
        return self.__jpdl31_ExceptionHandlerType289

    @jpdl31_ExceptionHandlerType289.setter
    def jpdl31_ExceptionHandlerType289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType289", None)
        self.__jpdl31_ExceptionHandlerType289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskNodeType288"):
                opp_val = getattr(old_value, "jpdl31_TaskNodeType288", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskNodeType288"):
                opp_val = getattr(value, "jpdl31_TaskNodeType288", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskNodeType288", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType208(self):
        return self.__jpdl31_ExceptionHandlerType208

    @jpdl31_ExceptionHandlerType208.setter
    def jpdl31_ExceptionHandlerType208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType208", None)
        self.__jpdl31_ExceptionHandlerType208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessStateType207"):
                opp_val = getattr(old_value, "jpdl31_ProcessStateType207", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessStateType207"):
                opp_val = getattr(value, "jpdl31_ProcessStateType207", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessStateType207", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType101(self):
        return self.__jpdl31_ExceptionHandlerType101

    @jpdl31_ExceptionHandlerType101.setter
    def jpdl31_ExceptionHandlerType101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType101", None)
        self.__jpdl31_ExceptionHandlerType101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ForkType100"):
                opp_val = getattr(old_value, "jpdl31_ForkType100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ForkType100"):
                opp_val = getattr(value, "jpdl31_ForkType100", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ForkType100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType91(self):
        return self.__jpdl31_ExceptionHandlerType91

    @jpdl31_ExceptionHandlerType91.setter
    def jpdl31_ExceptionHandlerType91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType91", None)
        self.__jpdl31_ExceptionHandlerType91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ScriptType92"):
                    opp_val = getattr(item, "jpdl31_ScriptType92", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ScriptType92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ScriptType92"):
                    opp_val = getattr(item, "jpdl31_ScriptType92", None)
                    
                    setattr(item, "jpdl31_ScriptType92", self)
                    

    @property
    def jpdl31_ExceptionHandlerType113(self):
        return self.__jpdl31_ExceptionHandlerType113

    @jpdl31_ExceptionHandlerType113.setter
    def jpdl31_ExceptionHandlerType113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType113", None)
        self.__jpdl31_ExceptionHandlerType113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_JoinType112"):
                opp_val = getattr(old_value, "jpdl31_JoinType112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_JoinType112"):
                opp_val = getattr(value, "jpdl31_JoinType112", None)
                if opp_val is None:
                    setattr(value, "jpdl31_JoinType112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType345(self):
        return self.__jpdl31_ExceptionHandlerType345

    @jpdl31_ExceptionHandlerType345.setter
    def jpdl31_ExceptionHandlerType345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType345", None)
        self.__jpdl31_ExceptionHandlerType345 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType1344"):
                opp_val = getattr(old_value, "jpdl31_TransitionType1344", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType1344"):
                opp_val = getattr(value, "jpdl31_TransitionType1344", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType1344", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType137(self):
        return self.__jpdl31_ExceptionHandlerType137

    @jpdl31_ExceptionHandlerType137.setter
    def jpdl31_ExceptionHandlerType137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType137", None)
        self.__jpdl31_ExceptionHandlerType137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_NodeType136"):
                opp_val = getattr(old_value, "jpdl31_NodeType136", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_NodeType136"):
                opp_val = getattr(value, "jpdl31_NodeType136", None)
                if opp_val is None:
                    setattr(value, "jpdl31_NodeType136", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType37(self):
        return self.__jpdl31_ExceptionHandlerType37

    @jpdl31_ExceptionHandlerType37.setter
    def jpdl31_ExceptionHandlerType37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType37", None)
        self.__jpdl31_ExceptionHandlerType37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot36"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot36"):
                opp_val = getattr(value, "jpdl31_DocumentRoot36", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType74(self):
        return self.__jpdl31_ExceptionHandlerType74

    @jpdl31_ExceptionHandlerType74.setter
    def jpdl31_ExceptionHandlerType74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType74", None)
        self.__jpdl31_ExceptionHandlerType74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_EndStateType73"):
                opp_val = getattr(old_value, "jpdl31_EndStateType73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_EndStateType73"):
                opp_val = getattr(value, "jpdl31_EndStateType73", None)
                if opp_val is None:
                    setattr(value, "jpdl31_EndStateType73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType232(self):
        return self.__jpdl31_ExceptionHandlerType232

    @jpdl31_ExceptionHandlerType232.setter
    def jpdl31_ExceptionHandlerType232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType232", None)
        self.__jpdl31_ExceptionHandlerType232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_StateType231"):
                opp_val = getattr(old_value, "jpdl31_StateType231", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_StateType231"):
                opp_val = getattr(value, "jpdl31_StateType231", None)
                if opp_val is None:
                    setattr(value, "jpdl31_StateType231", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType194(self):
        return self.__jpdl31_ExceptionHandlerType194

    @jpdl31_ExceptionHandlerType194.setter
    def jpdl31_ExceptionHandlerType194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType194", None)
        self.__jpdl31_ExceptionHandlerType194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType193"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType193", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType193"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType193", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType193", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType226(self):
        return self.__jpdl31_ExceptionHandlerType226

    @jpdl31_ExceptionHandlerType226.setter
    def jpdl31_ExceptionHandlerType226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType226", None)
        self.__jpdl31_ExceptionHandlerType226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_StartStateType225"):
                opp_val = getattr(old_value, "jpdl31_StartStateType225", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_StartStateType225"):
                opp_val = getattr(value, "jpdl31_StartStateType225", None)
                if opp_val is None:
                    setattr(value, "jpdl31_StartStateType225", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_Delegation:

    def __init__(self, mixed: str, any: str, class: str, configType: str, jpdl31_Delegation: "jpdl31_DecisionType" = None, jpdl31_Delegation23: "jpdl31_DocumentRoot" = None, jpdl31_Delegation301: "jpdl31_TaskType" = None):
        self.mixed = mixed
        self.any = any
        self.class = class
        self.configType = configType
        self.jpdl31_Delegation = jpdl31_Delegation
        self.jpdl31_Delegation23 = jpdl31_Delegation23
        self.jpdl31_Delegation301 = jpdl31_Delegation301
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def configType(self) -> str:
        return self.__configType

    @configType.setter
    def configType(self, configType: str):
        self.__configType = configType

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def jpdl31_Delegation301(self):
        return self.__jpdl31_Delegation301

    @jpdl31_Delegation301.setter
    def jpdl31_Delegation301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Delegation__jpdl31_Delegation301", None)
        self.__jpdl31_Delegation301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskType300"):
                opp_val = getattr(old_value, "jpdl31_TaskType300", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskType300"):
                opp_val = getattr(value, "jpdl31_TaskType300", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskType300", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_Delegation23(self):
        return self.__jpdl31_Delegation23

    @jpdl31_Delegation23.setter
    def jpdl31_Delegation23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Delegation__jpdl31_Delegation23", None)
        self.__jpdl31_Delegation23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot22"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot22"):
                opp_val = getattr(value, "jpdl31_DocumentRoot22", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_Delegation(self):
        return self.__jpdl31_Delegation

    @jpdl31_Delegation.setter
    def jpdl31_Delegation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Delegation__jpdl31_Delegation", None)
        self.__jpdl31_Delegation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DecisionType"):
                opp_val = getattr(old_value, "jpdl31_DecisionType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DecisionType"):
                opp_val = getattr(value, "jpdl31_DecisionType", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DecisionType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_DecisionType:

    def __init__(self, group: str, async: str, expression: str, name: str, jpdl31_DecisionType7: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_DecisionType9: set["jpdl31_TransitionType1"] = None, jpdl31_DecisionType: set["jpdl31_Delegation"] = None, jpdl31_DecisionType5: set["jpdl31_EventType"] = None, jpdl31_DecisionType29: "jpdl31_DocumentRoot" = None, jpdl31_DecisionType173: "jpdl31_ProcessDefinitionType" = None, jpdl31_DecisionType262: "jpdl31_SuperStateType" = None):
        self.group = group
        self.async = async
        self.expression = expression
        self.name = name
        self.jpdl31_DecisionType7 = jpdl31_DecisionType7 if jpdl31_DecisionType7 is not None else set()
        self.jpdl31_DecisionType9 = jpdl31_DecisionType9 if jpdl31_DecisionType9 is not None else set()
        self.jpdl31_DecisionType = jpdl31_DecisionType if jpdl31_DecisionType is not None else set()
        self.jpdl31_DecisionType5 = jpdl31_DecisionType5 if jpdl31_DecisionType5 is not None else set()
        self.jpdl31_DecisionType29 = jpdl31_DecisionType29
        self.jpdl31_DecisionType173 = jpdl31_DecisionType173
        self.jpdl31_DecisionType262 = jpdl31_DecisionType262
        
    @property
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def jpdl31_DecisionType(self):
        return self.__jpdl31_DecisionType

    @jpdl31_DecisionType.setter
    def jpdl31_DecisionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DecisionType__jpdl31_DecisionType", None)
        self.__jpdl31_DecisionType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Delegation"):
                    opp_val = getattr(item, "jpdl31_Delegation", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Delegation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Delegation"):
                    opp_val = getattr(item, "jpdl31_Delegation", None)
                    
                    setattr(item, "jpdl31_Delegation", self)
                    

    @property
    def jpdl31_DecisionType262(self):
        return self.__jpdl31_DecisionType262

    @jpdl31_DecisionType262.setter
    def jpdl31_DecisionType262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DecisionType__jpdl31_DecisionType262", None)
        self.__jpdl31_DecisionType262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType261"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType261", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType261"):
                opp_val = getattr(value, "jpdl31_SuperStateType261", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType261", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_DecisionType7(self):
        return self.__jpdl31_DecisionType7

    @jpdl31_DecisionType7.setter
    def jpdl31_DecisionType7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DecisionType__jpdl31_DecisionType7", None)
        self.__jpdl31_DecisionType7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType", self)
                    

    @property
    def jpdl31_DecisionType9(self):
        return self.__jpdl31_DecisionType9

    @jpdl31_DecisionType9.setter
    def jpdl31_DecisionType9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DecisionType__jpdl31_DecisionType9", None)
        self.__jpdl31_DecisionType9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType1"):
                    opp_val = getattr(item, "jpdl31_TransitionType1", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType1"):
                    opp_val = getattr(item, "jpdl31_TransitionType1", None)
                    
                    setattr(item, "jpdl31_TransitionType1", self)
                    

    @property
    def jpdl31_DecisionType29(self):
        return self.__jpdl31_DecisionType29

    @jpdl31_DecisionType29.setter
    def jpdl31_DecisionType29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DecisionType__jpdl31_DecisionType29", None)
        self.__jpdl31_DecisionType29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot28"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot28"):
                opp_val = getattr(value, "jpdl31_DocumentRoot28", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_DecisionType5(self):
        return self.__jpdl31_DecisionType5

    @jpdl31_DecisionType5.setter
    def jpdl31_DecisionType5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DecisionType__jpdl31_DecisionType5", None)
        self.__jpdl31_DecisionType5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType"):
                    opp_val = getattr(item, "jpdl31_EventType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType"):
                    opp_val = getattr(item, "jpdl31_EventType", None)
                    
                    setattr(item, "jpdl31_EventType", self)
                    

    @property
    def jpdl31_DecisionType173(self):
        return self.__jpdl31_DecisionType173

    @jpdl31_DecisionType173.setter
    def jpdl31_DecisionType173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DecisionType__jpdl31_DecisionType173", None)
        self.__jpdl31_DecisionType173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType172"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType172", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType172"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType172", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType172", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_ScriptType:

    def __init__(self, acceptPropagatedEvents: str, name: str, mixed: str, any: str, jpdl31_ScriptType: "jpdl31_CreateTimerType" = None, jpdl31_ScriptType50: "jpdl31_DocumentRoot" = None, jpdl31_ScriptType80: "jpdl31_EventType" = None, jpdl31_ScriptType92: "jpdl31_ExceptionHandlerType" = None, jpdl31_ScriptType95: "jpdl31_ForkType" = None, jpdl31_ScriptType125: "jpdl31_NodeType" = None, jpdl31_ScriptType182: "jpdl31_ProcessDefinitionType" = None, jpdl31_ScriptType313: "jpdl31_TimerType" = None, jpdl31_ScriptType319: "jpdl31_TransitionType" = None, jpdl31_ScriptType336: "jpdl31_TransitionType1" = None):
        self.acceptPropagatedEvents = acceptPropagatedEvents
        self.name = name
        self.mixed = mixed
        self.any = any
        self.jpdl31_ScriptType = jpdl31_ScriptType
        self.jpdl31_ScriptType50 = jpdl31_ScriptType50
        self.jpdl31_ScriptType80 = jpdl31_ScriptType80
        self.jpdl31_ScriptType92 = jpdl31_ScriptType92
        self.jpdl31_ScriptType95 = jpdl31_ScriptType95
        self.jpdl31_ScriptType125 = jpdl31_ScriptType125
        self.jpdl31_ScriptType182 = jpdl31_ScriptType182
        self.jpdl31_ScriptType313 = jpdl31_ScriptType313
        self.jpdl31_ScriptType319 = jpdl31_ScriptType319
        self.jpdl31_ScriptType336 = jpdl31_ScriptType336
        
    @property
    def acceptPropagatedEvents(self) -> str:
        return self.__acceptPropagatedEvents

    @acceptPropagatedEvents.setter
    def acceptPropagatedEvents(self, acceptPropagatedEvents: str):
        self.__acceptPropagatedEvents = acceptPropagatedEvents

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def jpdl31_ScriptType336(self):
        return self.__jpdl31_ScriptType336

    @jpdl31_ScriptType336.setter
    def jpdl31_ScriptType336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType336", None)
        self.__jpdl31_ScriptType336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType1335"):
                opp_val = getattr(old_value, "jpdl31_TransitionType1335", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType1335"):
                opp_val = getattr(value, "jpdl31_TransitionType1335", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType1335", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ScriptType95(self):
        return self.__jpdl31_ScriptType95

    @jpdl31_ScriptType95.setter
    def jpdl31_ScriptType95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType95", None)
        self.__jpdl31_ScriptType95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ForkType94"):
                opp_val = getattr(old_value, "jpdl31_ForkType94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ForkType94"):
                opp_val = getattr(value, "jpdl31_ForkType94", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ForkType94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ScriptType80(self):
        return self.__jpdl31_ScriptType80

    @jpdl31_ScriptType80.setter
    def jpdl31_ScriptType80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType80", None)
        self.__jpdl31_ScriptType80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_EventType79"):
                opp_val = getattr(old_value, "jpdl31_EventType79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_EventType79"):
                opp_val = getattr(value, "jpdl31_EventType79", None)
                if opp_val is None:
                    setattr(value, "jpdl31_EventType79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ScriptType319(self):
        return self.__jpdl31_ScriptType319

    @jpdl31_ScriptType319.setter
    def jpdl31_ScriptType319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType319", None)
        self.__jpdl31_ScriptType319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType318"):
                opp_val = getattr(old_value, "jpdl31_TransitionType318", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType318"):
                opp_val = getattr(value, "jpdl31_TransitionType318", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType318", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ScriptType313(self):
        return self.__jpdl31_ScriptType313

    @jpdl31_ScriptType313.setter
    def jpdl31_ScriptType313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType313", None)
        self.__jpdl31_ScriptType313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TimerType312"):
                opp_val = getattr(old_value, "jpdl31_TimerType312", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_TimerType312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TimerType312"):
                opp_val = getattr(value, "jpdl31_TimerType312", None)
                setattr(value, "jpdl31_TimerType312", self)

    @property
    def jpdl31_ScriptType(self):
        return self.__jpdl31_ScriptType

    @jpdl31_ScriptType.setter
    def jpdl31_ScriptType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType", None)
        self.__jpdl31_ScriptType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_CreateTimerType2"):
                opp_val = getattr(old_value, "jpdl31_CreateTimerType2", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_CreateTimerType2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_CreateTimerType2"):
                opp_val = getattr(value, "jpdl31_CreateTimerType2", None)
                setattr(value, "jpdl31_CreateTimerType2", self)

    @property
    def jpdl31_ScriptType92(self):
        return self.__jpdl31_ScriptType92

    @jpdl31_ScriptType92.setter
    def jpdl31_ScriptType92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType92", None)
        self.__jpdl31_ScriptType92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ExceptionHandlerType91"):
                opp_val = getattr(old_value, "jpdl31_ExceptionHandlerType91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ExceptionHandlerType91"):
                opp_val = getattr(value, "jpdl31_ExceptionHandlerType91", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ExceptionHandlerType91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ScriptType125(self):
        return self.__jpdl31_ScriptType125

    @jpdl31_ScriptType125.setter
    def jpdl31_ScriptType125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType125", None)
        self.__jpdl31_ScriptType125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_NodeType124"):
                opp_val = getattr(old_value, "jpdl31_NodeType124", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_NodeType124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_NodeType124"):
                opp_val = getattr(value, "jpdl31_NodeType124", None)
                setattr(value, "jpdl31_NodeType124", self)

    @property
    def jpdl31_ScriptType50(self):
        return self.__jpdl31_ScriptType50

    @jpdl31_ScriptType50.setter
    def jpdl31_ScriptType50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType50", None)
        self.__jpdl31_ScriptType50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot49"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot49"):
                opp_val = getattr(value, "jpdl31_DocumentRoot49", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ScriptType182(self):
        return self.__jpdl31_ScriptType182

    @jpdl31_ScriptType182.setter
    def jpdl31_ScriptType182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType182", None)
        self.__jpdl31_ScriptType182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType181"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType181", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType181"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType181", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType181", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_CreateTimerType:

    def __init__(self, duedate: str, name: str, repeat: str, transition: str, jpdl31_CreateTimerType: "jpdl31_ActionType" = None, jpdl31_CreateTimerType2: "jpdl31_ScriptType" = None, jpdl31_CreateTimerType26: "jpdl31_DocumentRoot" = None, jpdl31_CreateTimerType83: "jpdl31_EventType" = None, jpdl31_CreateTimerType128: "jpdl31_NodeType" = None, jpdl31_CreateTimerType185: "jpdl31_ProcessDefinitionType" = None, jpdl31_CreateTimerType322: "jpdl31_TransitionType" = None, jpdl31_CreateTimerType339: "jpdl31_TransitionType1" = None):
        self.duedate = duedate
        self.name = name
        self.repeat = repeat
        self.transition = transition
        self.jpdl31_CreateTimerType = jpdl31_CreateTimerType
        self.jpdl31_CreateTimerType2 = jpdl31_CreateTimerType2
        self.jpdl31_CreateTimerType26 = jpdl31_CreateTimerType26
        self.jpdl31_CreateTimerType83 = jpdl31_CreateTimerType83
        self.jpdl31_CreateTimerType128 = jpdl31_CreateTimerType128
        self.jpdl31_CreateTimerType185 = jpdl31_CreateTimerType185
        self.jpdl31_CreateTimerType322 = jpdl31_CreateTimerType322
        self.jpdl31_CreateTimerType339 = jpdl31_CreateTimerType339
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def duedate(self) -> str:
        return self.__duedate

    @duedate.setter
    def duedate(self, duedate: str):
        self.__duedate = duedate

    @property
    def transition(self) -> str:
        return self.__transition

    @transition.setter
    def transition(self, transition: str):
        self.__transition = transition

    @property
    def repeat(self) -> str:
        return self.__repeat

    @repeat.setter
    def repeat(self, repeat: str):
        self.__repeat = repeat

    @property
    def jpdl31_CreateTimerType322(self):
        return self.__jpdl31_CreateTimerType322

    @jpdl31_CreateTimerType322.setter
    def jpdl31_CreateTimerType322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CreateTimerType__jpdl31_CreateTimerType322", None)
        self.__jpdl31_CreateTimerType322 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType321"):
                opp_val = getattr(old_value, "jpdl31_TransitionType321", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType321"):
                opp_val = getattr(value, "jpdl31_TransitionType321", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType321", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_CreateTimerType26(self):
        return self.__jpdl31_CreateTimerType26

    @jpdl31_CreateTimerType26.setter
    def jpdl31_CreateTimerType26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CreateTimerType__jpdl31_CreateTimerType26", None)
        self.__jpdl31_CreateTimerType26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot25"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot25"):
                opp_val = getattr(value, "jpdl31_DocumentRoot25", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_CreateTimerType339(self):
        return self.__jpdl31_CreateTimerType339

    @jpdl31_CreateTimerType339.setter
    def jpdl31_CreateTimerType339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CreateTimerType__jpdl31_CreateTimerType339", None)
        self.__jpdl31_CreateTimerType339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType1338"):
                opp_val = getattr(old_value, "jpdl31_TransitionType1338", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType1338"):
                opp_val = getattr(value, "jpdl31_TransitionType1338", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType1338", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_CreateTimerType83(self):
        return self.__jpdl31_CreateTimerType83

    @jpdl31_CreateTimerType83.setter
    def jpdl31_CreateTimerType83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CreateTimerType__jpdl31_CreateTimerType83", None)
        self.__jpdl31_CreateTimerType83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_EventType82"):
                opp_val = getattr(old_value, "jpdl31_EventType82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_EventType82"):
                opp_val = getattr(value, "jpdl31_EventType82", None)
                if opp_val is None:
                    setattr(value, "jpdl31_EventType82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_CreateTimerType2(self):
        return self.__jpdl31_CreateTimerType2

    @jpdl31_CreateTimerType2.setter
    def jpdl31_CreateTimerType2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CreateTimerType__jpdl31_CreateTimerType2", None)
        self.__jpdl31_CreateTimerType2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ScriptType"):
                opp_val = getattr(old_value, "jpdl31_ScriptType", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_ScriptType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ScriptType"):
                opp_val = getattr(value, "jpdl31_ScriptType", None)
                setattr(value, "jpdl31_ScriptType", self)

    @property
    def jpdl31_CreateTimerType185(self):
        return self.__jpdl31_CreateTimerType185

    @jpdl31_CreateTimerType185.setter
    def jpdl31_CreateTimerType185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CreateTimerType__jpdl31_CreateTimerType185", None)
        self.__jpdl31_CreateTimerType185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType184"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType184", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType184"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType184", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType184", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_CreateTimerType128(self):
        return self.__jpdl31_CreateTimerType128

    @jpdl31_CreateTimerType128.setter
    def jpdl31_CreateTimerType128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CreateTimerType__jpdl31_CreateTimerType128", None)
        self.__jpdl31_CreateTimerType128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_NodeType127"):
                opp_val = getattr(old_value, "jpdl31_NodeType127", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_NodeType127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_NodeType127"):
                opp_val = getattr(value, "jpdl31_NodeType127", None)
                setattr(value, "jpdl31_NodeType127", self)

    @property
    def jpdl31_CreateTimerType(self):
        return self.__jpdl31_CreateTimerType

    @jpdl31_CreateTimerType.setter
    def jpdl31_CreateTimerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CreateTimerType__jpdl31_CreateTimerType", None)
        self.__jpdl31_CreateTimerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ActionType"):
                opp_val = getattr(old_value, "jpdl31_ActionType", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_ActionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ActionType"):
                opp_val = getattr(value, "jpdl31_ActionType", None)
                setattr(value, "jpdl31_ActionType", self)

class jpdl31_CancelTimerType:

    def __init__(self, name: str, jpdl31_CancelTimerType: "jpdl31_DocumentRoot" = None, jpdl31_CancelTimerType86: "jpdl31_EventType" = None, jpdl31_CancelTimerType131: "jpdl31_NodeType" = None, jpdl31_CancelTimerType188: "jpdl31_ProcessDefinitionType" = None, jpdl31_CancelTimerType325: "jpdl31_TransitionType" = None, jpdl31_CancelTimerType342: "jpdl31_TransitionType1" = None):
        self.name = name
        self.jpdl31_CancelTimerType = jpdl31_CancelTimerType
        self.jpdl31_CancelTimerType86 = jpdl31_CancelTimerType86
        self.jpdl31_CancelTimerType131 = jpdl31_CancelTimerType131
        self.jpdl31_CancelTimerType188 = jpdl31_CancelTimerType188
        self.jpdl31_CancelTimerType325 = jpdl31_CancelTimerType325
        self.jpdl31_CancelTimerType342 = jpdl31_CancelTimerType342
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl31_CancelTimerType188(self):
        return self.__jpdl31_CancelTimerType188

    @jpdl31_CancelTimerType188.setter
    def jpdl31_CancelTimerType188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CancelTimerType__jpdl31_CancelTimerType188", None)
        self.__jpdl31_CancelTimerType188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType187"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType187", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType187"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType187", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType187", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_CancelTimerType131(self):
        return self.__jpdl31_CancelTimerType131

    @jpdl31_CancelTimerType131.setter
    def jpdl31_CancelTimerType131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CancelTimerType__jpdl31_CancelTimerType131", None)
        self.__jpdl31_CancelTimerType131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_NodeType130"):
                opp_val = getattr(old_value, "jpdl31_NodeType130", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_NodeType130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_NodeType130"):
                opp_val = getattr(value, "jpdl31_NodeType130", None)
                setattr(value, "jpdl31_NodeType130", self)

    @property
    def jpdl31_CancelTimerType86(self):
        return self.__jpdl31_CancelTimerType86

    @jpdl31_CancelTimerType86.setter
    def jpdl31_CancelTimerType86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CancelTimerType__jpdl31_CancelTimerType86", None)
        self.__jpdl31_CancelTimerType86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_EventType85"):
                opp_val = getattr(old_value, "jpdl31_EventType85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_EventType85"):
                opp_val = getattr(value, "jpdl31_EventType85", None)
                if opp_val is None:
                    setattr(value, "jpdl31_EventType85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_CancelTimerType342(self):
        return self.__jpdl31_CancelTimerType342

    @jpdl31_CancelTimerType342.setter
    def jpdl31_CancelTimerType342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CancelTimerType__jpdl31_CancelTimerType342", None)
        self.__jpdl31_CancelTimerType342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType1341"):
                opp_val = getattr(old_value, "jpdl31_TransitionType1341", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType1341"):
                opp_val = getattr(value, "jpdl31_TransitionType1341", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType1341", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_CancelTimerType(self):
        return self.__jpdl31_CancelTimerType

    @jpdl31_CancelTimerType.setter
    def jpdl31_CancelTimerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CancelTimerType__jpdl31_CancelTimerType", None)
        self.__jpdl31_CancelTimerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot20"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot20"):
                opp_val = getattr(value, "jpdl31_DocumentRoot20", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_CancelTimerType325(self):
        return self.__jpdl31_CancelTimerType325

    @jpdl31_CancelTimerType325.setter
    def jpdl31_CancelTimerType325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CancelTimerType__jpdl31_CancelTimerType325", None)
        self.__jpdl31_CancelTimerType325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType324"):
                opp_val = getattr(old_value, "jpdl31_TransitionType324", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType324"):
                opp_val = getattr(value, "jpdl31_TransitionType324", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType324", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_ConditionType:

    def __init__(self, mixed: str, group: str, any: str, expression: str, jpdl31_ConditionType: "jpdl31_TransitionType1" = None):
        self.mixed = mixed
        self.group = group
        self.any = any
        self.expression = expression
        self.jpdl31_ConditionType = jpdl31_ConditionType
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def jpdl31_ConditionType(self):
        return self.__jpdl31_ConditionType

    @jpdl31_ConditionType.setter
    def jpdl31_ConditionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ConditionType__jpdl31_ConditionType", None)
        self.__jpdl31_ConditionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType1330"):
                opp_val = getattr(old_value, "jpdl31_TransitionType1330", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType1330"):
                opp_val = getattr(value, "jpdl31_TransitionType1330", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType1330", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Delegation:

    pass
class jpdl31_AssignmentType(Delegation):

    def __init__(self, actorId: str, expression: str, pooledActors: str, jpdl31_AssignmentType: "jpdl31_DocumentRoot" = None, jpdl31_AssignmentType280: "jpdl31_SwimlaneType" = None, jpdl31_AssignmentType298: "jpdl31_TaskType" = None):
        self.actorId = actorId
        self.expression = expression
        self.pooledActors = pooledActors
        self.jpdl31_AssignmentType = jpdl31_AssignmentType
        self.jpdl31_AssignmentType280 = jpdl31_AssignmentType280
        self.jpdl31_AssignmentType298 = jpdl31_AssignmentType298
        
    @property
    def actorId(self) -> str:
        return self.__actorId

    @actorId.setter
    def actorId(self, actorId: str):
        self.__actorId = actorId

    @property
    def pooledActors(self) -> str:
        return self.__pooledActors

    @pooledActors.setter
    def pooledActors(self, pooledActors: str):
        self.__pooledActors = pooledActors

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def jpdl31_AssignmentType280(self):
        return self.__jpdl31_AssignmentType280

    @jpdl31_AssignmentType280.setter
    def jpdl31_AssignmentType280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_AssignmentType__jpdl31_AssignmentType280", None)
        self.__jpdl31_AssignmentType280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SwimlaneType279"):
                opp_val = getattr(old_value, "jpdl31_SwimlaneType279", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_SwimlaneType279", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SwimlaneType279"):
                opp_val = getattr(value, "jpdl31_SwimlaneType279", None)
                setattr(value, "jpdl31_SwimlaneType279", self)

    @property
    def jpdl31_AssignmentType(self):
        return self.__jpdl31_AssignmentType

    @jpdl31_AssignmentType.setter
    def jpdl31_AssignmentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_AssignmentType__jpdl31_AssignmentType", None)
        self.__jpdl31_AssignmentType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot18"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot18"):
                opp_val = getattr(value, "jpdl31_DocumentRoot18", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_AssignmentType298(self):
        return self.__jpdl31_AssignmentType298

    @jpdl31_AssignmentType298.setter
    def jpdl31_AssignmentType298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_AssignmentType__jpdl31_AssignmentType298", None)
        self.__jpdl31_AssignmentType298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskType297"):
                opp_val = getattr(old_value, "jpdl31_TaskType297", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskType297"):
                opp_val = getattr(value, "jpdl31_TaskType297", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskType297", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_ActionType:

    def __init__(self, mixed: str, any: str, class: str, configType: str, expression: str, name: str, refName: str, acceptPropagatedEvents: str, async: str, jpdl31_ActionType: "jpdl31_CreateTimerType" = None, jpdl31_ActionType16: "jpdl31_DocumentRoot" = None, jpdl31_ActionType77: "jpdl31_EventType" = None, jpdl31_ActionType89: "jpdl31_ExceptionHandlerType" = None, jpdl31_ActionType122: "jpdl31_NodeType" = None, jpdl31_ActionType179: "jpdl31_ProcessDefinitionType" = None, jpdl31_ActionType310: "jpdl31_TimerType" = None, jpdl31_ActionType316: "jpdl31_TransitionType" = None, jpdl31_ActionType333: "jpdl31_TransitionType1" = None):
        self.mixed = mixed
        self.any = any
        self.class = class
        self.configType = configType
        self.expression = expression
        self.name = name
        self.refName = refName
        self.acceptPropagatedEvents = acceptPropagatedEvents
        self.async = async
        self.jpdl31_ActionType = jpdl31_ActionType
        self.jpdl31_ActionType16 = jpdl31_ActionType16
        self.jpdl31_ActionType77 = jpdl31_ActionType77
        self.jpdl31_ActionType89 = jpdl31_ActionType89
        self.jpdl31_ActionType122 = jpdl31_ActionType122
        self.jpdl31_ActionType179 = jpdl31_ActionType179
        self.jpdl31_ActionType310 = jpdl31_ActionType310
        self.jpdl31_ActionType316 = jpdl31_ActionType316
        self.jpdl31_ActionType333 = jpdl31_ActionType333
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def acceptPropagatedEvents(self) -> str:
        return self.__acceptPropagatedEvents

    @acceptPropagatedEvents.setter
    def acceptPropagatedEvents(self, acceptPropagatedEvents: str):
        self.__acceptPropagatedEvents = acceptPropagatedEvents

    @property
    def configType(self) -> str:
        return self.__configType

    @configType.setter
    def configType(self, configType: str):
        self.__configType = configType

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def refName(self) -> str:
        return self.__refName

    @refName.setter
    def refName(self, refName: str):
        self.__refName = refName

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def jpdl31_ActionType316(self):
        return self.__jpdl31_ActionType316

    @jpdl31_ActionType316.setter
    def jpdl31_ActionType316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType316", None)
        self.__jpdl31_ActionType316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType315"):
                opp_val = getattr(old_value, "jpdl31_TransitionType315", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType315"):
                opp_val = getattr(value, "jpdl31_TransitionType315", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType315", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ActionType77(self):
        return self.__jpdl31_ActionType77

    @jpdl31_ActionType77.setter
    def jpdl31_ActionType77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType77", None)
        self.__jpdl31_ActionType77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_EventType76"):
                opp_val = getattr(old_value, "jpdl31_EventType76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_EventType76"):
                opp_val = getattr(value, "jpdl31_EventType76", None)
                if opp_val is None:
                    setattr(value, "jpdl31_EventType76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ActionType89(self):
        return self.__jpdl31_ActionType89

    @jpdl31_ActionType89.setter
    def jpdl31_ActionType89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType89", None)
        self.__jpdl31_ActionType89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ExceptionHandlerType88"):
                opp_val = getattr(old_value, "jpdl31_ExceptionHandlerType88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ExceptionHandlerType88"):
                opp_val = getattr(value, "jpdl31_ExceptionHandlerType88", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ExceptionHandlerType88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ActionType333(self):
        return self.__jpdl31_ActionType333

    @jpdl31_ActionType333.setter
    def jpdl31_ActionType333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType333", None)
        self.__jpdl31_ActionType333 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType1332"):
                opp_val = getattr(old_value, "jpdl31_TransitionType1332", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType1332"):
                opp_val = getattr(value, "jpdl31_TransitionType1332", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType1332", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ActionType(self):
        return self.__jpdl31_ActionType

    @jpdl31_ActionType.setter
    def jpdl31_ActionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType", None)
        self.__jpdl31_ActionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_CreateTimerType"):
                opp_val = getattr(old_value, "jpdl31_CreateTimerType", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_CreateTimerType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_CreateTimerType"):
                opp_val = getattr(value, "jpdl31_CreateTimerType", None)
                setattr(value, "jpdl31_CreateTimerType", self)

    @property
    def jpdl31_ActionType179(self):
        return self.__jpdl31_ActionType179

    @jpdl31_ActionType179.setter
    def jpdl31_ActionType179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType179", None)
        self.__jpdl31_ActionType179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType178"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType178", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType178"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType178", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType178", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ActionType310(self):
        return self.__jpdl31_ActionType310

    @jpdl31_ActionType310.setter
    def jpdl31_ActionType310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType310", None)
        self.__jpdl31_ActionType310 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TimerType309"):
                opp_val = getattr(old_value, "jpdl31_TimerType309", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_TimerType309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TimerType309"):
                opp_val = getattr(value, "jpdl31_TimerType309", None)
                setattr(value, "jpdl31_TimerType309", self)

    @property
    def jpdl31_ActionType122(self):
        return self.__jpdl31_ActionType122

    @jpdl31_ActionType122.setter
    def jpdl31_ActionType122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType122", None)
        self.__jpdl31_ActionType122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_NodeType121"):
                opp_val = getattr(old_value, "jpdl31_NodeType121", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_NodeType121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_NodeType121"):
                opp_val = getattr(value, "jpdl31_NodeType121", None)
                setattr(value, "jpdl31_NodeType121", self)

    @property
    def jpdl31_ActionType16(self):
        return self.__jpdl31_ActionType16

    @jpdl31_ActionType16.setter
    def jpdl31_ActionType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType16", None)
        self.__jpdl31_ActionType16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot15"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot15"):
                opp_val = getattr(value, "jpdl31_DocumentRoot15", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
