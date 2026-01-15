from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ConfigType(Enum):
    field = "field"
    bean = "bean"
    constructor = "constructor"
    configurationProperty = "configurationProperty"
class PriorityTypeMember0(Enum):
    highest = "highest"
    high = "high"
    normal = "normal"
    low = "low"
    lowest = "lowest"
class BindingType(Enum):
    late = "late"
    early = "early"
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
class SignalType(Enum):
    unsynchronized = "unsynchronized"
    never = "never"
    first = "first"
    firstWait = "firstWait"
    last = "last"
    lastWait = "lastWait"


############################################
# Definition of Classes
############################################

class jpdl32_ReminderType:

    def __init__(self, duedate: str, repeat: str, jpdl32_ReminderType: "jpdl32_TaskType" = None):
        self.duedate = duedate
        self.repeat = repeat
        self.jpdl32_ReminderType = jpdl32_ReminderType
        
    @property
    def duedate(self) -> str:
        return self.__duedate

    @duedate.setter
    def duedate(self, duedate: str):
        self.__duedate = duedate

    @property
    def repeat(self) -> str:
        return self.__repeat

    @repeat.setter
    def repeat(self, repeat: str):
        self.__repeat = repeat

    @property
    def jpdl32_ReminderType(self):
        return self.__jpdl32_ReminderType

    @jpdl32_ReminderType.setter
    def jpdl32_ReminderType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ReminderType__jpdl32_ReminderType", None)
        self.__jpdl32_ReminderType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TaskType341"):
                opp_val = getattr(old_value, "jpdl32_TaskType341", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TaskType341"):
                opp_val = getattr(value, "jpdl32_TaskType341", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TaskType341", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_SubProcessType:

    def __init__(self, version: str, binding: str, name: str, jpdl32_SubProcessType: "jpdl32_ProcessStateType" = None):
        self.version = version
        self.binding = binding
        self.name = name
        self.jpdl32_SubProcessType = jpdl32_SubProcessType
        
    @property
    def binding(self) -> str:
        return self.__binding

    @binding.setter
    def binding(self, binding: str):
        self.__binding = binding

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
    def jpdl32_SubProcessType(self):
        return self.__jpdl32_SubProcessType

    @jpdl32_SubProcessType.setter
    def jpdl32_SubProcessType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SubProcessType__jpdl32_SubProcessType", None)
        self.__jpdl32_SubProcessType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessStateType228"):
                opp_val = getattr(old_value, "jpdl32_ProcessStateType228", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessStateType228"):
                opp_val = getattr(value, "jpdl32_ProcessStateType228", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessStateType228", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_TimerType:

    def __init__(self, name: str, repeat: str, transition: str, duedate: str, jpdl32_TimerType: "jpdl32_DocumentRoot" = None, jpdl32_TimerType112: "jpdl32_ForkType" = None, jpdl32_TimerType124: "jpdl32_JoinType" = None, jpdl32_TimerType136: "jpdl32_MailNodeType" = None, jpdl32_TimerType163: "jpdl32_NodeType" = None, jpdl32_TimerType240: "jpdl32_ProcessStateType" = None, jpdl32_TimerType264: "jpdl32_StateType" = None, jpdl32_TimerType306: "jpdl32_SuperStateType" = None, jpdl32_TimerType324: "jpdl32_TaskNodeType" = None, jpdl32_TimerType339: "jpdl32_TaskType" = None, jpdl32_TimerType346: "jpdl32_ScriptType" = None, jpdl32_TimerType349: "jpdl32_CreateTimerType" = None, jpdl32_TimerType352: "jpdl32_CancelTimerType" = None, jpdl32_TimerType343: "jpdl32_ActionType" = None, jpdl32_TimerType355: "jpdl32_MailType" = None):
        self.name = name
        self.repeat = repeat
        self.transition = transition
        self.duedate = duedate
        self.jpdl32_TimerType = jpdl32_TimerType
        self.jpdl32_TimerType112 = jpdl32_TimerType112
        self.jpdl32_TimerType124 = jpdl32_TimerType124
        self.jpdl32_TimerType136 = jpdl32_TimerType136
        self.jpdl32_TimerType163 = jpdl32_TimerType163
        self.jpdl32_TimerType240 = jpdl32_TimerType240
        self.jpdl32_TimerType264 = jpdl32_TimerType264
        self.jpdl32_TimerType306 = jpdl32_TimerType306
        self.jpdl32_TimerType324 = jpdl32_TimerType324
        self.jpdl32_TimerType339 = jpdl32_TimerType339
        self.jpdl32_TimerType346 = jpdl32_TimerType346
        self.jpdl32_TimerType349 = jpdl32_TimerType349
        self.jpdl32_TimerType352 = jpdl32_TimerType352
        self.jpdl32_TimerType343 = jpdl32_TimerType343
        self.jpdl32_TimerType355 = jpdl32_TimerType355
        
    @property
    def duedate(self) -> str:
        return self.__duedate

    @duedate.setter
    def duedate(self, duedate: str):
        self.__duedate = duedate

    @property
    def repeat(self) -> str:
        return self.__repeat

    @repeat.setter
    def repeat(self, repeat: str):
        self.__repeat = repeat

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def transition(self) -> str:
        return self.__transition

    @transition.setter
    def transition(self, transition: str):
        self.__transition = transition

    @property
    def jpdl32_TimerType343(self):
        return self.__jpdl32_TimerType343

    @jpdl32_TimerType343.setter
    def jpdl32_TimerType343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType343", None)
        self.__jpdl32_TimerType343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ActionType344"):
                opp_val = getattr(old_value, "jpdl32_ActionType344", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_ActionType344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ActionType344"):
                opp_val = getattr(value, "jpdl32_ActionType344", None)
                setattr(value, "jpdl32_ActionType344", self)

    @property
    def jpdl32_TimerType324(self):
        return self.__jpdl32_TimerType324

    @jpdl32_TimerType324.setter
    def jpdl32_TimerType324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType324", None)
        self.__jpdl32_TimerType324 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TaskNodeType323"):
                opp_val = getattr(old_value, "jpdl32_TaskNodeType323", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TaskNodeType323"):
                opp_val = getattr(value, "jpdl32_TaskNodeType323", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TaskNodeType323", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TimerType306(self):
        return self.__jpdl32_TimerType306

    @jpdl32_TimerType306.setter
    def jpdl32_TimerType306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType306", None)
        self.__jpdl32_TimerType306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SuperStateType305"):
                opp_val = getattr(old_value, "jpdl32_SuperStateType305", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SuperStateType305"):
                opp_val = getattr(value, "jpdl32_SuperStateType305", None)
                if opp_val is None:
                    setattr(value, "jpdl32_SuperStateType305", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TimerType163(self):
        return self.__jpdl32_TimerType163

    @jpdl32_TimerType163.setter
    def jpdl32_TimerType163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType163", None)
        self.__jpdl32_TimerType163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_NodeType162"):
                opp_val = getattr(old_value, "jpdl32_NodeType162", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_NodeType162"):
                opp_val = getattr(value, "jpdl32_NodeType162", None)
                if opp_val is None:
                    setattr(value, "jpdl32_NodeType162", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TimerType(self):
        return self.__jpdl32_TimerType

    @jpdl32_TimerType.setter
    def jpdl32_TimerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType", None)
        self.__jpdl32_TimerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot68"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot68"):
                opp_val = getattr(value, "jpdl32_DocumentRoot68", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TimerType124(self):
        return self.__jpdl32_TimerType124

    @jpdl32_TimerType124.setter
    def jpdl32_TimerType124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType124", None)
        self.__jpdl32_TimerType124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_JoinType123"):
                opp_val = getattr(old_value, "jpdl32_JoinType123", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_JoinType123"):
                opp_val = getattr(value, "jpdl32_JoinType123", None)
                if opp_val is None:
                    setattr(value, "jpdl32_JoinType123", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TimerType112(self):
        return self.__jpdl32_TimerType112

    @jpdl32_TimerType112.setter
    def jpdl32_TimerType112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType112", None)
        self.__jpdl32_TimerType112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ForkType111"):
                opp_val = getattr(old_value, "jpdl32_ForkType111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ForkType111"):
                opp_val = getattr(value, "jpdl32_ForkType111", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ForkType111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TimerType136(self):
        return self.__jpdl32_TimerType136

    @jpdl32_TimerType136.setter
    def jpdl32_TimerType136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType136", None)
        self.__jpdl32_TimerType136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_MailNodeType135"):
                opp_val = getattr(old_value, "jpdl32_MailNodeType135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_MailNodeType135"):
                opp_val = getattr(value, "jpdl32_MailNodeType135", None)
                if opp_val is None:
                    setattr(value, "jpdl32_MailNodeType135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TimerType349(self):
        return self.__jpdl32_TimerType349

    @jpdl32_TimerType349.setter
    def jpdl32_TimerType349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType349", None)
        self.__jpdl32_TimerType349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_CreateTimerType350"):
                opp_val = getattr(old_value, "jpdl32_CreateTimerType350", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_CreateTimerType350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_CreateTimerType350"):
                opp_val = getattr(value, "jpdl32_CreateTimerType350", None)
                setattr(value, "jpdl32_CreateTimerType350", self)

    @property
    def jpdl32_TimerType264(self):
        return self.__jpdl32_TimerType264

    @jpdl32_TimerType264.setter
    def jpdl32_TimerType264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType264", None)
        self.__jpdl32_TimerType264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_StateType263"):
                opp_val = getattr(old_value, "jpdl32_StateType263", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_StateType263"):
                opp_val = getattr(value, "jpdl32_StateType263", None)
                if opp_val is None:
                    setattr(value, "jpdl32_StateType263", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TimerType346(self):
        return self.__jpdl32_TimerType346

    @jpdl32_TimerType346.setter
    def jpdl32_TimerType346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType346", None)
        self.__jpdl32_TimerType346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ScriptType347"):
                opp_val = getattr(old_value, "jpdl32_ScriptType347", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_ScriptType347", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ScriptType347"):
                opp_val = getattr(value, "jpdl32_ScriptType347", None)
                setattr(value, "jpdl32_ScriptType347", self)

    @property
    def jpdl32_TimerType240(self):
        return self.__jpdl32_TimerType240

    @jpdl32_TimerType240.setter
    def jpdl32_TimerType240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType240", None)
        self.__jpdl32_TimerType240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessStateType239"):
                opp_val = getattr(old_value, "jpdl32_ProcessStateType239", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessStateType239"):
                opp_val = getattr(value, "jpdl32_ProcessStateType239", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessStateType239", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TimerType352(self):
        return self.__jpdl32_TimerType352

    @jpdl32_TimerType352.setter
    def jpdl32_TimerType352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType352", None)
        self.__jpdl32_TimerType352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_CancelTimerType353"):
                opp_val = getattr(old_value, "jpdl32_CancelTimerType353", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_CancelTimerType353", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_CancelTimerType353"):
                opp_val = getattr(value, "jpdl32_CancelTimerType353", None)
                setattr(value, "jpdl32_CancelTimerType353", self)

    @property
    def jpdl32_TimerType339(self):
        return self.__jpdl32_TimerType339

    @jpdl32_TimerType339.setter
    def jpdl32_TimerType339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType339", None)
        self.__jpdl32_TimerType339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TaskType338"):
                opp_val = getattr(old_value, "jpdl32_TaskType338", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TaskType338"):
                opp_val = getattr(value, "jpdl32_TaskType338", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TaskType338", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TimerType355(self):
        return self.__jpdl32_TimerType355

    @jpdl32_TimerType355.setter
    def jpdl32_TimerType355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TimerType__jpdl32_TimerType355", None)
        self.__jpdl32_TimerType355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_MailType356"):
                opp_val = getattr(old_value, "jpdl32_MailType356", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_MailType356", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_MailType356"):
                opp_val = getattr(value, "jpdl32_MailType356", None)
                setattr(value, "jpdl32_MailType356", self)

class jpdl32_VariableType:

    def __init__(self, mappedName: str, name: str, any: str, access: str, jpdl32_VariableType: "jpdl32_DocumentRoot" = None, jpdl32_VariableType231: "jpdl32_ProcessStateType" = None):
        self.mappedName = mappedName
        self.name = name
        self.any = any
        self.access = access
        self.jpdl32_VariableType = jpdl32_VariableType
        self.jpdl32_VariableType231 = jpdl32_VariableType231
        
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
    def mappedName(self) -> str:
        return self.__mappedName

    @mappedName.setter
    def mappedName(self, mappedName: str):
        self.__mappedName = mappedName

    @property
    def jpdl32_VariableType(self):
        return self.__jpdl32_VariableType

    @jpdl32_VariableType.setter
    def jpdl32_VariableType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_VariableType__jpdl32_VariableType", None)
        self.__jpdl32_VariableType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot73"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot73"):
                opp_val = getattr(value, "jpdl32_DocumentRoot73", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_VariableType231(self):
        return self.__jpdl32_VariableType231

    @jpdl32_VariableType231.setter
    def jpdl32_VariableType231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_VariableType__jpdl32_VariableType231", None)
        self.__jpdl32_VariableType231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessStateType230"):
                opp_val = getattr(old_value, "jpdl32_ProcessStateType230", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessStateType230"):
                opp_val = getattr(value, "jpdl32_ProcessStateType230", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessStateType230", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_SuperStateType:

    def __init__(self, group: str, description: str, async: str, name: str, jpdl32_SuperStateType: "jpdl32_DocumentRoot" = None, jpdl32_SuperStateType184: "jpdl32_ProcessDefinitionType" = None, jpdl32_SuperStateType279: "jpdl32_SuperStateType" = None, jpdl32_SuperStateType277: set["jpdl32_SuperStateType"] = None, jpdl32_SuperStateType269: set["jpdl32_NodeType"] = None, jpdl32_SuperStateType272: set["jpdl32_StateType"] = None, jpdl32_SuperStateType275: set["jpdl32_TaskNodeType"] = None, jpdl32_SuperStateType287: set["jpdl32_JoinType"] = None, jpdl32_SuperStateType281: set["jpdl32_ProcessStateType"] = None, jpdl32_SuperStateType284: set["jpdl32_ForkType"] = None, jpdl32_SuperStateType290: set["jpdl32_DecisionType"] = None, jpdl32_SuperStateType293: set["jpdl32_EndStateType"] = None, jpdl32_SuperStateType296: set["jpdl32_MailNodeType"] = None, jpdl32_SuperStateType308: set["jpdl32_TransitionType"] = None, jpdl32_SuperStateType299: set["jpdl32_EventType"] = None, jpdl32_SuperStateType302: set["jpdl32_ExceptionHandlerType"] = None, jpdl32_SuperStateType305: set["jpdl32_TimerType"] = None):
        self.group = group
        self.description = description
        self.async = async
        self.name = name
        self.jpdl32_SuperStateType = jpdl32_SuperStateType
        self.jpdl32_SuperStateType184 = jpdl32_SuperStateType184
        self.jpdl32_SuperStateType279 = jpdl32_SuperStateType279
        self.jpdl32_SuperStateType277 = jpdl32_SuperStateType277 if jpdl32_SuperStateType277 is not None else set()
        self.jpdl32_SuperStateType269 = jpdl32_SuperStateType269 if jpdl32_SuperStateType269 is not None else set()
        self.jpdl32_SuperStateType272 = jpdl32_SuperStateType272 if jpdl32_SuperStateType272 is not None else set()
        self.jpdl32_SuperStateType275 = jpdl32_SuperStateType275 if jpdl32_SuperStateType275 is not None else set()
        self.jpdl32_SuperStateType287 = jpdl32_SuperStateType287 if jpdl32_SuperStateType287 is not None else set()
        self.jpdl32_SuperStateType281 = jpdl32_SuperStateType281 if jpdl32_SuperStateType281 is not None else set()
        self.jpdl32_SuperStateType284 = jpdl32_SuperStateType284 if jpdl32_SuperStateType284 is not None else set()
        self.jpdl32_SuperStateType290 = jpdl32_SuperStateType290 if jpdl32_SuperStateType290 is not None else set()
        self.jpdl32_SuperStateType293 = jpdl32_SuperStateType293 if jpdl32_SuperStateType293 is not None else set()
        self.jpdl32_SuperStateType296 = jpdl32_SuperStateType296 if jpdl32_SuperStateType296 is not None else set()
        self.jpdl32_SuperStateType308 = jpdl32_SuperStateType308 if jpdl32_SuperStateType308 is not None else set()
        self.jpdl32_SuperStateType299 = jpdl32_SuperStateType299 if jpdl32_SuperStateType299 is not None else set()
        self.jpdl32_SuperStateType302 = jpdl32_SuperStateType302 if jpdl32_SuperStateType302 is not None else set()
        self.jpdl32_SuperStateType305 = jpdl32_SuperStateType305 if jpdl32_SuperStateType305 is not None else set()
        
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
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

    @property
    def jpdl32_SuperStateType281(self):
        return self.__jpdl32_SuperStateType281

    @jpdl32_SuperStateType281.setter
    def jpdl32_SuperStateType281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType281", None)
        self.__jpdl32_SuperStateType281 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ProcessStateType282"):
                    opp_val = getattr(item, "jpdl32_ProcessStateType282", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ProcessStateType282", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ProcessStateType282"):
                    opp_val = getattr(item, "jpdl32_ProcessStateType282", None)
                    
                    setattr(item, "jpdl32_ProcessStateType282", self)
                    

    @property
    def jpdl32_SuperStateType299(self):
        return self.__jpdl32_SuperStateType299

    @jpdl32_SuperStateType299.setter
    def jpdl32_SuperStateType299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType299", None)
        self.__jpdl32_SuperStateType299 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EventType300"):
                    opp_val = getattr(item, "jpdl32_EventType300", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EventType300", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EventType300"):
                    opp_val = getattr(item, "jpdl32_EventType300", None)
                    
                    setattr(item, "jpdl32_EventType300", self)
                    

    @property
    def jpdl32_SuperStateType287(self):
        return self.__jpdl32_SuperStateType287

    @jpdl32_SuperStateType287.setter
    def jpdl32_SuperStateType287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType287", None)
        self.__jpdl32_SuperStateType287 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_JoinType288"):
                    opp_val = getattr(item, "jpdl32_JoinType288", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_JoinType288", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_JoinType288"):
                    opp_val = getattr(item, "jpdl32_JoinType288", None)
                    
                    setattr(item, "jpdl32_JoinType288", self)
                    

    @property
    def jpdl32_SuperStateType279(self):
        return self.__jpdl32_SuperStateType279

    @jpdl32_SuperStateType279.setter
    def jpdl32_SuperStateType279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType279", None)
        self.__jpdl32_SuperStateType279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SuperStateType277"):
                opp_val = getattr(old_value, "jpdl32_SuperStateType277", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SuperStateType277"):
                opp_val = getattr(value, "jpdl32_SuperStateType277", None)
                if opp_val is None:
                    setattr(value, "jpdl32_SuperStateType277", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_SuperStateType284(self):
        return self.__jpdl32_SuperStateType284

    @jpdl32_SuperStateType284.setter
    def jpdl32_SuperStateType284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType284", None)
        self.__jpdl32_SuperStateType284 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ForkType285"):
                    opp_val = getattr(item, "jpdl32_ForkType285", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ForkType285", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ForkType285"):
                    opp_val = getattr(item, "jpdl32_ForkType285", None)
                    
                    setattr(item, "jpdl32_ForkType285", self)
                    

    @property
    def jpdl32_SuperStateType302(self):
        return self.__jpdl32_SuperStateType302

    @jpdl32_SuperStateType302.setter
    def jpdl32_SuperStateType302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType302", None)
        self.__jpdl32_SuperStateType302 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ExceptionHandlerType303"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType303", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ExceptionHandlerType303", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ExceptionHandlerType303"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType303", None)
                    
                    setattr(item, "jpdl32_ExceptionHandlerType303", self)
                    

    @property
    def jpdl32_SuperStateType269(self):
        return self.__jpdl32_SuperStateType269

    @jpdl32_SuperStateType269.setter
    def jpdl32_SuperStateType269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType269", None)
        self.__jpdl32_SuperStateType269 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_NodeType270"):
                    opp_val = getattr(item, "jpdl32_NodeType270", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_NodeType270", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_NodeType270"):
                    opp_val = getattr(item, "jpdl32_NodeType270", None)
                    
                    setattr(item, "jpdl32_NodeType270", self)
                    

    @property
    def jpdl32_SuperStateType308(self):
        return self.__jpdl32_SuperStateType308

    @jpdl32_SuperStateType308.setter
    def jpdl32_SuperStateType308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType308", None)
        self.__jpdl32_SuperStateType308 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TransitionType309"):
                    opp_val = getattr(item, "jpdl32_TransitionType309", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TransitionType309", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TransitionType309"):
                    opp_val = getattr(item, "jpdl32_TransitionType309", None)
                    
                    setattr(item, "jpdl32_TransitionType309", self)
                    

    @property
    def jpdl32_SuperStateType275(self):
        return self.__jpdl32_SuperStateType275

    @jpdl32_SuperStateType275.setter
    def jpdl32_SuperStateType275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType275", None)
        self.__jpdl32_SuperStateType275 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TaskNodeType276"):
                    opp_val = getattr(item, "jpdl32_TaskNodeType276", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TaskNodeType276", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TaskNodeType276"):
                    opp_val = getattr(item, "jpdl32_TaskNodeType276", None)
                    
                    setattr(item, "jpdl32_TaskNodeType276", self)
                    

    @property
    def jpdl32_SuperStateType272(self):
        return self.__jpdl32_SuperStateType272

    @jpdl32_SuperStateType272.setter
    def jpdl32_SuperStateType272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType272", None)
        self.__jpdl32_SuperStateType272 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_StateType273"):
                    opp_val = getattr(item, "jpdl32_StateType273", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_StateType273", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_StateType273"):
                    opp_val = getattr(item, "jpdl32_StateType273", None)
                    
                    setattr(item, "jpdl32_StateType273", self)
                    

    @property
    def jpdl32_SuperStateType277(self):
        return self.__jpdl32_SuperStateType277

    @jpdl32_SuperStateType277.setter
    def jpdl32_SuperStateType277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType277", None)
        self.__jpdl32_SuperStateType277 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_SuperStateType279"):
                    opp_val = getattr(item, "jpdl32_SuperStateType279", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_SuperStateType279", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_SuperStateType279"):
                    opp_val = getattr(item, "jpdl32_SuperStateType279", None)
                    
                    setattr(item, "jpdl32_SuperStateType279", self)
                    

    @property
    def jpdl32_SuperStateType184(self):
        return self.__jpdl32_SuperStateType184

    @jpdl32_SuperStateType184.setter
    def jpdl32_SuperStateType184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType184", None)
        self.__jpdl32_SuperStateType184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType183"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType183", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType183"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType183", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType183", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_SuperStateType296(self):
        return self.__jpdl32_SuperStateType296

    @jpdl32_SuperStateType296.setter
    def jpdl32_SuperStateType296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType296", None)
        self.__jpdl32_SuperStateType296 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_MailNodeType297"):
                    opp_val = getattr(item, "jpdl32_MailNodeType297", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_MailNodeType297", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_MailNodeType297"):
                    opp_val = getattr(item, "jpdl32_MailNodeType297", None)
                    
                    setattr(item, "jpdl32_MailNodeType297", self)
                    

    @property
    def jpdl32_SuperStateType305(self):
        return self.__jpdl32_SuperStateType305

    @jpdl32_SuperStateType305.setter
    def jpdl32_SuperStateType305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType305", None)
        self.__jpdl32_SuperStateType305 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TimerType306"):
                    opp_val = getattr(item, "jpdl32_TimerType306", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TimerType306", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TimerType306"):
                    opp_val = getattr(item, "jpdl32_TimerType306", None)
                    
                    setattr(item, "jpdl32_TimerType306", self)
                    

    @property
    def jpdl32_SuperStateType293(self):
        return self.__jpdl32_SuperStateType293

    @jpdl32_SuperStateType293.setter
    def jpdl32_SuperStateType293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType293", None)
        self.__jpdl32_SuperStateType293 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EndStateType294"):
                    opp_val = getattr(item, "jpdl32_EndStateType294", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EndStateType294", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EndStateType294"):
                    opp_val = getattr(item, "jpdl32_EndStateType294", None)
                    
                    setattr(item, "jpdl32_EndStateType294", self)
                    

    @property
    def jpdl32_SuperStateType(self):
        return self.__jpdl32_SuperStateType

    @jpdl32_SuperStateType.setter
    def jpdl32_SuperStateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType", None)
        self.__jpdl32_SuperStateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot60"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot60"):
                opp_val = getattr(value, "jpdl32_DocumentRoot60", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_SuperStateType290(self):
        return self.__jpdl32_SuperStateType290

    @jpdl32_SuperStateType290.setter
    def jpdl32_SuperStateType290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SuperStateType__jpdl32_SuperStateType290", None)
        self.__jpdl32_SuperStateType290 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_DecisionType291"):
                    opp_val = getattr(item, "jpdl32_DecisionType291", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_DecisionType291", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_DecisionType291"):
                    opp_val = getattr(item, "jpdl32_DecisionType291", None)
                    
                    setattr(item, "jpdl32_DecisionType291", self)
                    

class jpdl32_TaskNodeType:

    def __init__(self, group: str, description: str, async: str, createTasks: str, endTasks: str, name: str, signal: str, jpdl32_TaskNodeType: "jpdl32_DocumentRoot" = None, jpdl32_TaskNodeType181: "jpdl32_ProcessDefinitionType" = None, jpdl32_TaskNodeType276: "jpdl32_SuperStateType" = None, jpdl32_TaskNodeType314: set["jpdl32_TaskType"] = None, jpdl32_TaskNodeType317: set["jpdl32_EventType"] = None, jpdl32_TaskNodeType320: set["jpdl32_ExceptionHandlerType"] = None, jpdl32_TaskNodeType323: set["jpdl32_TimerType"] = None, jpdl32_TaskNodeType326: set["jpdl32_TransitionType"] = None):
        self.group = group
        self.description = description
        self.async = async
        self.createTasks = createTasks
        self.endTasks = endTasks
        self.name = name
        self.signal = signal
        self.jpdl32_TaskNodeType = jpdl32_TaskNodeType
        self.jpdl32_TaskNodeType181 = jpdl32_TaskNodeType181
        self.jpdl32_TaskNodeType276 = jpdl32_TaskNodeType276
        self.jpdl32_TaskNodeType314 = jpdl32_TaskNodeType314 if jpdl32_TaskNodeType314 is not None else set()
        self.jpdl32_TaskNodeType317 = jpdl32_TaskNodeType317 if jpdl32_TaskNodeType317 is not None else set()
        self.jpdl32_TaskNodeType320 = jpdl32_TaskNodeType320 if jpdl32_TaskNodeType320 is not None else set()
        self.jpdl32_TaskNodeType323 = jpdl32_TaskNodeType323 if jpdl32_TaskNodeType323 is not None else set()
        self.jpdl32_TaskNodeType326 = jpdl32_TaskNodeType326 if jpdl32_TaskNodeType326 is not None else set()
        
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
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def createTasks(self) -> str:
        return self.__createTasks

    @createTasks.setter
    def createTasks(self, createTasks: str):
        self.__createTasks = createTasks

    @property
    def endTasks(self) -> str:
        return self.__endTasks

    @endTasks.setter
    def endTasks(self, endTasks: str):
        self.__endTasks = endTasks

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
    def jpdl32_TaskNodeType314(self):
        return self.__jpdl32_TaskNodeType314

    @jpdl32_TaskNodeType314.setter
    def jpdl32_TaskNodeType314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskNodeType__jpdl32_TaskNodeType314", None)
        self.__jpdl32_TaskNodeType314 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TaskType315"):
                    opp_val = getattr(item, "jpdl32_TaskType315", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TaskType315", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TaskType315"):
                    opp_val = getattr(item, "jpdl32_TaskType315", None)
                    
                    setattr(item, "jpdl32_TaskType315", self)
                    

    @property
    def jpdl32_TaskNodeType276(self):
        return self.__jpdl32_TaskNodeType276

    @jpdl32_TaskNodeType276.setter
    def jpdl32_TaskNodeType276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskNodeType__jpdl32_TaskNodeType276", None)
        self.__jpdl32_TaskNodeType276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SuperStateType275"):
                opp_val = getattr(old_value, "jpdl32_SuperStateType275", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SuperStateType275"):
                opp_val = getattr(value, "jpdl32_SuperStateType275", None)
                if opp_val is None:
                    setattr(value, "jpdl32_SuperStateType275", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TaskNodeType181(self):
        return self.__jpdl32_TaskNodeType181

    @jpdl32_TaskNodeType181.setter
    def jpdl32_TaskNodeType181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskNodeType__jpdl32_TaskNodeType181", None)
        self.__jpdl32_TaskNodeType181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType180"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType180", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType180"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType180", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType180", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TaskNodeType326(self):
        return self.__jpdl32_TaskNodeType326

    @jpdl32_TaskNodeType326.setter
    def jpdl32_TaskNodeType326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskNodeType__jpdl32_TaskNodeType326", None)
        self.__jpdl32_TaskNodeType326 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TransitionType327"):
                    opp_val = getattr(item, "jpdl32_TransitionType327", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TransitionType327", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TransitionType327"):
                    opp_val = getattr(item, "jpdl32_TransitionType327", None)
                    
                    setattr(item, "jpdl32_TransitionType327", self)
                    

    @property
    def jpdl32_TaskNodeType323(self):
        return self.__jpdl32_TaskNodeType323

    @jpdl32_TaskNodeType323.setter
    def jpdl32_TaskNodeType323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskNodeType__jpdl32_TaskNodeType323", None)
        self.__jpdl32_TaskNodeType323 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TimerType324"):
                    opp_val = getattr(item, "jpdl32_TimerType324", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TimerType324", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TimerType324"):
                    opp_val = getattr(item, "jpdl32_TimerType324", None)
                    
                    setattr(item, "jpdl32_TimerType324", self)
                    

    @property
    def jpdl32_TaskNodeType(self):
        return self.__jpdl32_TaskNodeType

    @jpdl32_TaskNodeType.setter
    def jpdl32_TaskNodeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskNodeType__jpdl32_TaskNodeType", None)
        self.__jpdl32_TaskNodeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot66"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot66"):
                opp_val = getattr(value, "jpdl32_DocumentRoot66", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TaskNodeType320(self):
        return self.__jpdl32_TaskNodeType320

    @jpdl32_TaskNodeType320.setter
    def jpdl32_TaskNodeType320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskNodeType__jpdl32_TaskNodeType320", None)
        self.__jpdl32_TaskNodeType320 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ExceptionHandlerType321"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType321", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ExceptionHandlerType321", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ExceptionHandlerType321"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType321", None)
                    
                    setattr(item, "jpdl32_ExceptionHandlerType321", self)
                    

    @property
    def jpdl32_TaskNodeType317(self):
        return self.__jpdl32_TaskNodeType317

    @jpdl32_TaskNodeType317.setter
    def jpdl32_TaskNodeType317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskNodeType__jpdl32_TaskNodeType317", None)
        self.__jpdl32_TaskNodeType317 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EventType318"):
                    opp_val = getattr(item, "jpdl32_EventType318", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EventType318", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EventType318"):
                    opp_val = getattr(item, "jpdl32_EventType318", None)
                    
                    setattr(item, "jpdl32_EventType318", self)
                    

class jpdl32_TaskType:

    def __init__(self, description: str, group: str, notify: str, priority: str, signalling: str, swimlane: str, blocking: str, description1: str, duedate: str, name: str, jpdl32_TaskType: "jpdl32_DocumentRoot" = None, jpdl32_TaskType226: "jpdl32_ProcessDefinitionType" = None, jpdl32_TaskType246: "jpdl32_StartStateType" = None, jpdl32_TaskType315: "jpdl32_TaskNodeType" = None, jpdl32_TaskType338: set["jpdl32_TimerType"] = None, jpdl32_TaskType329: set["jpdl32_AssignmentType"] = None, jpdl32_TaskType332: set["jpdl32_Delegation"] = None, jpdl32_TaskType335: set["jpdl32_EventType"] = None, jpdl32_TaskType341: set["jpdl32_ReminderType"] = None):
        self.description = description
        self.group = group
        self.notify = notify
        self.priority = priority
        self.signalling = signalling
        self.swimlane = swimlane
        self.blocking = blocking
        self.description1 = description1
        self.duedate = duedate
        self.name = name
        self.jpdl32_TaskType = jpdl32_TaskType
        self.jpdl32_TaskType226 = jpdl32_TaskType226
        self.jpdl32_TaskType246 = jpdl32_TaskType246
        self.jpdl32_TaskType315 = jpdl32_TaskType315
        self.jpdl32_TaskType338 = jpdl32_TaskType338 if jpdl32_TaskType338 is not None else set()
        self.jpdl32_TaskType329 = jpdl32_TaskType329 if jpdl32_TaskType329 is not None else set()
        self.jpdl32_TaskType332 = jpdl32_TaskType332 if jpdl32_TaskType332 is not None else set()
        self.jpdl32_TaskType335 = jpdl32_TaskType335 if jpdl32_TaskType335 is not None else set()
        self.jpdl32_TaskType341 = jpdl32_TaskType341 if jpdl32_TaskType341 is not None else set()
        
    @property
    def signalling(self) -> str:
        return self.__signalling

    @signalling.setter
    def signalling(self, signalling: str):
        self.__signalling = signalling

    @property
    def duedate(self) -> str:
        return self.__duedate

    @duedate.setter
    def duedate(self, duedate: str):
        self.__duedate = duedate

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def swimlane(self) -> str:
        return self.__swimlane

    @swimlane.setter
    def swimlane(self, swimlane: str):
        self.__swimlane = swimlane

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
    def description1(self) -> str:
        return self.__description1

    @description1.setter
    def description1(self, description1: str):
        self.__description1 = description1

    @property
    def blocking(self) -> str:
        return self.__blocking

    @blocking.setter
    def blocking(self, blocking: str):
        self.__blocking = blocking

    @property
    def notify(self) -> str:
        return self.__notify

    @notify.setter
    def notify(self, notify: str):
        self.__notify = notify

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def jpdl32_TaskType246(self):
        return self.__jpdl32_TaskType246

    @jpdl32_TaskType246.setter
    def jpdl32_TaskType246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskType__jpdl32_TaskType246", None)
        self.__jpdl32_TaskType246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_StartStateType245"):
                opp_val = getattr(old_value, "jpdl32_StartStateType245", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_StartStateType245"):
                opp_val = getattr(value, "jpdl32_StartStateType245", None)
                if opp_val is None:
                    setattr(value, "jpdl32_StartStateType245", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TaskType335(self):
        return self.__jpdl32_TaskType335

    @jpdl32_TaskType335.setter
    def jpdl32_TaskType335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskType__jpdl32_TaskType335", None)
        self.__jpdl32_TaskType335 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EventType336"):
                    opp_val = getattr(item, "jpdl32_EventType336", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EventType336", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EventType336"):
                    opp_val = getattr(item, "jpdl32_EventType336", None)
                    
                    setattr(item, "jpdl32_EventType336", self)
                    

    @property
    def jpdl32_TaskType338(self):
        return self.__jpdl32_TaskType338

    @jpdl32_TaskType338.setter
    def jpdl32_TaskType338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskType__jpdl32_TaskType338", None)
        self.__jpdl32_TaskType338 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TimerType339"):
                    opp_val = getattr(item, "jpdl32_TimerType339", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TimerType339", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TimerType339"):
                    opp_val = getattr(item, "jpdl32_TimerType339", None)
                    
                    setattr(item, "jpdl32_TimerType339", self)
                    

    @property
    def jpdl32_TaskType332(self):
        return self.__jpdl32_TaskType332

    @jpdl32_TaskType332.setter
    def jpdl32_TaskType332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskType__jpdl32_TaskType332", None)
        self.__jpdl32_TaskType332 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_Delegation333"):
                    opp_val = getattr(item, "jpdl32_Delegation333", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_Delegation333", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_Delegation333"):
                    opp_val = getattr(item, "jpdl32_Delegation333", None)
                    
                    setattr(item, "jpdl32_Delegation333", self)
                    

    @property
    def jpdl32_TaskType(self):
        return self.__jpdl32_TaskType

    @jpdl32_TaskType.setter
    def jpdl32_TaskType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskType__jpdl32_TaskType", None)
        self.__jpdl32_TaskType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot64"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot64"):
                opp_val = getattr(value, "jpdl32_DocumentRoot64", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TaskType226(self):
        return self.__jpdl32_TaskType226

    @jpdl32_TaskType226.setter
    def jpdl32_TaskType226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskType__jpdl32_TaskType226", None)
        self.__jpdl32_TaskType226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType225"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType225", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType225"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType225", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType225", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TaskType315(self):
        return self.__jpdl32_TaskType315

    @jpdl32_TaskType315.setter
    def jpdl32_TaskType315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskType__jpdl32_TaskType315", None)
        self.__jpdl32_TaskType315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TaskNodeType314"):
                opp_val = getattr(old_value, "jpdl32_TaskNodeType314", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TaskNodeType314"):
                opp_val = getattr(value, "jpdl32_TaskNodeType314", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TaskNodeType314", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TaskType341(self):
        return self.__jpdl32_TaskType341

    @jpdl32_TaskType341.setter
    def jpdl32_TaskType341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskType__jpdl32_TaskType341", None)
        self.__jpdl32_TaskType341 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ReminderType"):
                    opp_val = getattr(item, "jpdl32_ReminderType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ReminderType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ReminderType"):
                    opp_val = getattr(item, "jpdl32_ReminderType", None)
                    
                    setattr(item, "jpdl32_ReminderType", self)
                    

    @property
    def jpdl32_TaskType329(self):
        return self.__jpdl32_TaskType329

    @jpdl32_TaskType329.setter
    def jpdl32_TaskType329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TaskType__jpdl32_TaskType329", None)
        self.__jpdl32_TaskType329 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_AssignmentType330"):
                    opp_val = getattr(item, "jpdl32_AssignmentType330", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_AssignmentType330", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_AssignmentType330"):
                    opp_val = getattr(item, "jpdl32_AssignmentType330", None)
                    
                    setattr(item, "jpdl32_AssignmentType330", self)
                    

class jpdl32_SwimlaneType:

    def __init__(self, name: str, jpdl32_SwimlaneType: "jpdl32_DocumentRoot" = None, jpdl32_SwimlaneType169: "jpdl32_ProcessDefinitionType" = None, jpdl32_SwimlaneType311: "jpdl32_AssignmentType" = None):
        self.name = name
        self.jpdl32_SwimlaneType = jpdl32_SwimlaneType
        self.jpdl32_SwimlaneType169 = jpdl32_SwimlaneType169
        self.jpdl32_SwimlaneType311 = jpdl32_SwimlaneType311
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl32_SwimlaneType311(self):
        return self.__jpdl32_SwimlaneType311

    @jpdl32_SwimlaneType311.setter
    def jpdl32_SwimlaneType311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SwimlaneType__jpdl32_SwimlaneType311", None)
        self.__jpdl32_SwimlaneType311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_AssignmentType312"):
                opp_val = getattr(old_value, "jpdl32_AssignmentType312", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_AssignmentType312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_AssignmentType312"):
                opp_val = getattr(value, "jpdl32_AssignmentType312", None)
                setattr(value, "jpdl32_AssignmentType312", self)

    @property
    def jpdl32_SwimlaneType169(self):
        return self.__jpdl32_SwimlaneType169

    @jpdl32_SwimlaneType169.setter
    def jpdl32_SwimlaneType169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SwimlaneType__jpdl32_SwimlaneType169", None)
        self.__jpdl32_SwimlaneType169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType168"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType168", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType168"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType168", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType168", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_SwimlaneType(self):
        return self.__jpdl32_SwimlaneType

    @jpdl32_SwimlaneType.setter
    def jpdl32_SwimlaneType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_SwimlaneType__jpdl32_SwimlaneType", None)
        self.__jpdl32_SwimlaneType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot62"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot62"):
                opp_val = getattr(value, "jpdl32_DocumentRoot62", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_NodeType:

    def __init__(self, nodeContentElements: str, description: str, async: str, name: str, jpdl32_NodeType: "jpdl32_DocumentRoot" = None, jpdl32_NodeType141: "jpdl32_ActionType" = None, jpdl32_NodeType144: "jpdl32_ScriptType" = None, jpdl32_NodeType147: "jpdl32_CreateTimerType" = None, jpdl32_NodeType150: "jpdl32_CancelTimerType" = None, jpdl32_NodeType153: "jpdl32_MailType" = None, jpdl32_NodeType162: set["jpdl32_TimerType"] = None, jpdl32_NodeType156: set["jpdl32_EventType"] = None, jpdl32_NodeType159: set["jpdl32_ExceptionHandlerType"] = None, jpdl32_NodeType165: set["jpdl32_TransitionType"] = None, jpdl32_NodeType175: "jpdl32_ProcessDefinitionType" = None, jpdl32_NodeType270: "jpdl32_SuperStateType" = None):
        self.nodeContentElements = nodeContentElements
        self.description = description
        self.async = async
        self.name = name
        self.jpdl32_NodeType = jpdl32_NodeType
        self.jpdl32_NodeType141 = jpdl32_NodeType141
        self.jpdl32_NodeType144 = jpdl32_NodeType144
        self.jpdl32_NodeType147 = jpdl32_NodeType147
        self.jpdl32_NodeType150 = jpdl32_NodeType150
        self.jpdl32_NodeType153 = jpdl32_NodeType153
        self.jpdl32_NodeType162 = jpdl32_NodeType162 if jpdl32_NodeType162 is not None else set()
        self.jpdl32_NodeType156 = jpdl32_NodeType156 if jpdl32_NodeType156 is not None else set()
        self.jpdl32_NodeType159 = jpdl32_NodeType159 if jpdl32_NodeType159 is not None else set()
        self.jpdl32_NodeType165 = jpdl32_NodeType165 if jpdl32_NodeType165 is not None else set()
        self.jpdl32_NodeType175 = jpdl32_NodeType175
        self.jpdl32_NodeType270 = jpdl32_NodeType270
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

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
    def jpdl32_NodeType(self):
        return self.__jpdl32_NodeType

    @jpdl32_NodeType.setter
    def jpdl32_NodeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_NodeType__jpdl32_NodeType", None)
        self.__jpdl32_NodeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot47"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot47"):
                opp_val = getattr(value, "jpdl32_DocumentRoot47", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_NodeType165(self):
        return self.__jpdl32_NodeType165

    @jpdl32_NodeType165.setter
    def jpdl32_NodeType165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_NodeType__jpdl32_NodeType165", None)
        self.__jpdl32_NodeType165 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TransitionType166"):
                    opp_val = getattr(item, "jpdl32_TransitionType166", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TransitionType166", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TransitionType166"):
                    opp_val = getattr(item, "jpdl32_TransitionType166", None)
                    
                    setattr(item, "jpdl32_TransitionType166", self)
                    

    @property
    def jpdl32_NodeType150(self):
        return self.__jpdl32_NodeType150

    @jpdl32_NodeType150.setter
    def jpdl32_NodeType150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_NodeType__jpdl32_NodeType150", None)
        self.__jpdl32_NodeType150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_CancelTimerType151"):
                opp_val = getattr(old_value, "jpdl32_CancelTimerType151", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_CancelTimerType151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_CancelTimerType151"):
                opp_val = getattr(value, "jpdl32_CancelTimerType151", None)
                setattr(value, "jpdl32_CancelTimerType151", self)

    @property
    def jpdl32_NodeType153(self):
        return self.__jpdl32_NodeType153

    @jpdl32_NodeType153.setter
    def jpdl32_NodeType153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_NodeType__jpdl32_NodeType153", None)
        self.__jpdl32_NodeType153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_MailType154"):
                opp_val = getattr(old_value, "jpdl32_MailType154", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_MailType154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_MailType154"):
                opp_val = getattr(value, "jpdl32_MailType154", None)
                setattr(value, "jpdl32_MailType154", self)

    @property
    def jpdl32_NodeType147(self):
        return self.__jpdl32_NodeType147

    @jpdl32_NodeType147.setter
    def jpdl32_NodeType147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_NodeType__jpdl32_NodeType147", None)
        self.__jpdl32_NodeType147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_CreateTimerType148"):
                opp_val = getattr(old_value, "jpdl32_CreateTimerType148", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_CreateTimerType148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_CreateTimerType148"):
                opp_val = getattr(value, "jpdl32_CreateTimerType148", None)
                setattr(value, "jpdl32_CreateTimerType148", self)

    @property
    def jpdl32_NodeType156(self):
        return self.__jpdl32_NodeType156

    @jpdl32_NodeType156.setter
    def jpdl32_NodeType156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_NodeType__jpdl32_NodeType156", None)
        self.__jpdl32_NodeType156 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EventType157"):
                    opp_val = getattr(item, "jpdl32_EventType157", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EventType157", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EventType157"):
                    opp_val = getattr(item, "jpdl32_EventType157", None)
                    
                    setattr(item, "jpdl32_EventType157", self)
                    

    @property
    def jpdl32_NodeType141(self):
        return self.__jpdl32_NodeType141

    @jpdl32_NodeType141.setter
    def jpdl32_NodeType141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_NodeType__jpdl32_NodeType141", None)
        self.__jpdl32_NodeType141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ActionType142"):
                opp_val = getattr(old_value, "jpdl32_ActionType142", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_ActionType142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ActionType142"):
                opp_val = getattr(value, "jpdl32_ActionType142", None)
                setattr(value, "jpdl32_ActionType142", self)

    @property
    def jpdl32_NodeType162(self):
        return self.__jpdl32_NodeType162

    @jpdl32_NodeType162.setter
    def jpdl32_NodeType162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_NodeType__jpdl32_NodeType162", None)
        self.__jpdl32_NodeType162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TimerType163"):
                    opp_val = getattr(item, "jpdl32_TimerType163", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TimerType163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TimerType163"):
                    opp_val = getattr(item, "jpdl32_TimerType163", None)
                    
                    setattr(item, "jpdl32_TimerType163", self)
                    

    @property
    def jpdl32_NodeType159(self):
        return self.__jpdl32_NodeType159

    @jpdl32_NodeType159.setter
    def jpdl32_NodeType159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_NodeType__jpdl32_NodeType159", None)
        self.__jpdl32_NodeType159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ExceptionHandlerType160"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType160", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ExceptionHandlerType160", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ExceptionHandlerType160"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType160", None)
                    
                    setattr(item, "jpdl32_ExceptionHandlerType160", self)
                    

    @property
    def jpdl32_NodeType144(self):
        return self.__jpdl32_NodeType144

    @jpdl32_NodeType144.setter
    def jpdl32_NodeType144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_NodeType__jpdl32_NodeType144", None)
        self.__jpdl32_NodeType144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ScriptType145"):
                opp_val = getattr(old_value, "jpdl32_ScriptType145", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_ScriptType145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ScriptType145"):
                opp_val = getattr(value, "jpdl32_ScriptType145", None)
                setattr(value, "jpdl32_ScriptType145", self)

    @property
    def jpdl32_NodeType270(self):
        return self.__jpdl32_NodeType270

    @jpdl32_NodeType270.setter
    def jpdl32_NodeType270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_NodeType__jpdl32_NodeType270", None)
        self.__jpdl32_NodeType270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SuperStateType269"):
                opp_val = getattr(old_value, "jpdl32_SuperStateType269", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SuperStateType269"):
                opp_val = getattr(value, "jpdl32_SuperStateType269", None)
                if opp_val is None:
                    setattr(value, "jpdl32_SuperStateType269", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_NodeType175(self):
        return self.__jpdl32_NodeType175

    @jpdl32_NodeType175.setter
    def jpdl32_NodeType175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_NodeType__jpdl32_NodeType175", None)
        self.__jpdl32_NodeType175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType174"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType174", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType174"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType174", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType174", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_StateType:

    def __init__(self, description: str, nodeContentElements: str, async: str, name: str, jpdl32_StateType: "jpdl32_DocumentRoot" = None, jpdl32_StateType178: "jpdl32_ProcessDefinitionType" = None, jpdl32_StateType266: set["jpdl32_TransitionType"] = None, jpdl32_StateType257: set["jpdl32_EventType"] = None, jpdl32_StateType260: set["jpdl32_ExceptionHandlerType"] = None, jpdl32_StateType263: set["jpdl32_TimerType"] = None, jpdl32_StateType273: "jpdl32_SuperStateType" = None):
        self.description = description
        self.nodeContentElements = nodeContentElements
        self.async = async
        self.name = name
        self.jpdl32_StateType = jpdl32_StateType
        self.jpdl32_StateType178 = jpdl32_StateType178
        self.jpdl32_StateType266 = jpdl32_StateType266 if jpdl32_StateType266 is not None else set()
        self.jpdl32_StateType257 = jpdl32_StateType257 if jpdl32_StateType257 is not None else set()
        self.jpdl32_StateType260 = jpdl32_StateType260 if jpdl32_StateType260 is not None else set()
        self.jpdl32_StateType263 = jpdl32_StateType263 if jpdl32_StateType263 is not None else set()
        self.jpdl32_StateType273 = jpdl32_StateType273
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

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
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

    @property
    def jpdl32_StateType(self):
        return self.__jpdl32_StateType

    @jpdl32_StateType.setter
    def jpdl32_StateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_StateType__jpdl32_StateType", None)
        self.__jpdl32_StateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot58"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot58"):
                opp_val = getattr(value, "jpdl32_DocumentRoot58", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_StateType266(self):
        return self.__jpdl32_StateType266

    @jpdl32_StateType266.setter
    def jpdl32_StateType266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_StateType__jpdl32_StateType266", None)
        self.__jpdl32_StateType266 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TransitionType267"):
                    opp_val = getattr(item, "jpdl32_TransitionType267", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TransitionType267", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TransitionType267"):
                    opp_val = getattr(item, "jpdl32_TransitionType267", None)
                    
                    setattr(item, "jpdl32_TransitionType267", self)
                    

    @property
    def jpdl32_StateType260(self):
        return self.__jpdl32_StateType260

    @jpdl32_StateType260.setter
    def jpdl32_StateType260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_StateType__jpdl32_StateType260", None)
        self.__jpdl32_StateType260 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ExceptionHandlerType261"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType261", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ExceptionHandlerType261", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ExceptionHandlerType261"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType261", None)
                    
                    setattr(item, "jpdl32_ExceptionHandlerType261", self)
                    

    @property
    def jpdl32_StateType257(self):
        return self.__jpdl32_StateType257

    @jpdl32_StateType257.setter
    def jpdl32_StateType257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_StateType__jpdl32_StateType257", None)
        self.__jpdl32_StateType257 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EventType258"):
                    opp_val = getattr(item, "jpdl32_EventType258", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EventType258", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EventType258"):
                    opp_val = getattr(item, "jpdl32_EventType258", None)
                    
                    setattr(item, "jpdl32_EventType258", self)
                    

    @property
    def jpdl32_StateType178(self):
        return self.__jpdl32_StateType178

    @jpdl32_StateType178.setter
    def jpdl32_StateType178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_StateType__jpdl32_StateType178", None)
        self.__jpdl32_StateType178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType177"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType177", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType177"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType177", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType177", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_StateType263(self):
        return self.__jpdl32_StateType263

    @jpdl32_StateType263.setter
    def jpdl32_StateType263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_StateType__jpdl32_StateType263", None)
        self.__jpdl32_StateType263 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TimerType264"):
                    opp_val = getattr(item, "jpdl32_TimerType264", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TimerType264", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TimerType264"):
                    opp_val = getattr(item, "jpdl32_TimerType264", None)
                    
                    setattr(item, "jpdl32_TimerType264", self)
                    

    @property
    def jpdl32_StateType273(self):
        return self.__jpdl32_StateType273

    @jpdl32_StateType273.setter
    def jpdl32_StateType273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_StateType__jpdl32_StateType273", None)
        self.__jpdl32_StateType273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SuperStateType272"):
                opp_val = getattr(old_value, "jpdl32_SuperStateType272", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SuperStateType272"):
                opp_val = getattr(value, "jpdl32_SuperStateType272", None)
                if opp_val is None:
                    setattr(value, "jpdl32_SuperStateType272", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_StartStateType:

    def __init__(self, group: str, description: str, name: str, jpdl32_StartStateType: "jpdl32_DocumentRoot" = None, jpdl32_StartStateType172: "jpdl32_ProcessDefinitionType" = None, jpdl32_StartStateType251: set["jpdl32_EventType"] = None, jpdl32_StartStateType245: set["jpdl32_TaskType"] = None, jpdl32_StartStateType248: set["jpdl32_TransitionType"] = None, jpdl32_StartStateType254: set["jpdl32_ExceptionHandlerType"] = None):
        self.group = group
        self.description = description
        self.name = name
        self.jpdl32_StartStateType = jpdl32_StartStateType
        self.jpdl32_StartStateType172 = jpdl32_StartStateType172
        self.jpdl32_StartStateType251 = jpdl32_StartStateType251 if jpdl32_StartStateType251 is not None else set()
        self.jpdl32_StartStateType245 = jpdl32_StartStateType245 if jpdl32_StartStateType245 is not None else set()
        self.jpdl32_StartStateType248 = jpdl32_StartStateType248 if jpdl32_StartStateType248 is not None else set()
        self.jpdl32_StartStateType254 = jpdl32_StartStateType254 if jpdl32_StartStateType254 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def jpdl32_StartStateType(self):
        return self.__jpdl32_StartStateType

    @jpdl32_StartStateType.setter
    def jpdl32_StartStateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_StartStateType__jpdl32_StartStateType", None)
        self.__jpdl32_StartStateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot56"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot56"):
                opp_val = getattr(value, "jpdl32_DocumentRoot56", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_StartStateType245(self):
        return self.__jpdl32_StartStateType245

    @jpdl32_StartStateType245.setter
    def jpdl32_StartStateType245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_StartStateType__jpdl32_StartStateType245", None)
        self.__jpdl32_StartStateType245 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TaskType246"):
                    opp_val = getattr(item, "jpdl32_TaskType246", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TaskType246", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TaskType246"):
                    opp_val = getattr(item, "jpdl32_TaskType246", None)
                    
                    setattr(item, "jpdl32_TaskType246", self)
                    

    @property
    def jpdl32_StartStateType254(self):
        return self.__jpdl32_StartStateType254

    @jpdl32_StartStateType254.setter
    def jpdl32_StartStateType254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_StartStateType__jpdl32_StartStateType254", None)
        self.__jpdl32_StartStateType254 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ExceptionHandlerType255"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType255", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ExceptionHandlerType255", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ExceptionHandlerType255"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType255", None)
                    
                    setattr(item, "jpdl32_ExceptionHandlerType255", self)
                    

    @property
    def jpdl32_StartStateType251(self):
        return self.__jpdl32_StartStateType251

    @jpdl32_StartStateType251.setter
    def jpdl32_StartStateType251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_StartStateType__jpdl32_StartStateType251", None)
        self.__jpdl32_StartStateType251 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EventType252"):
                    opp_val = getattr(item, "jpdl32_EventType252", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EventType252", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EventType252"):
                    opp_val = getattr(item, "jpdl32_EventType252", None)
                    
                    setattr(item, "jpdl32_EventType252", self)
                    

    @property
    def jpdl32_StartStateType172(self):
        return self.__jpdl32_StartStateType172

    @jpdl32_StartStateType172.setter
    def jpdl32_StartStateType172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_StartStateType__jpdl32_StartStateType172", None)
        self.__jpdl32_StartStateType172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType171"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType171", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType171"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType171", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType171", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_StartStateType248(self):
        return self.__jpdl32_StartStateType248

    @jpdl32_StartStateType248.setter
    def jpdl32_StartStateType248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_StartStateType__jpdl32_StartStateType248", None)
        self.__jpdl32_StartStateType248 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TransitionType249"):
                    opp_val = getattr(item, "jpdl32_TransitionType249", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TransitionType249", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TransitionType249"):
                    opp_val = getattr(item, "jpdl32_TransitionType249", None)
                    
                    setattr(item, "jpdl32_TransitionType249", self)
                    

class jpdl32_ProcessStateType:

    def __init__(self, group: str, description: str, async: str, binding: str, name: str, jpdl32_ProcessStateType: "jpdl32_DocumentRoot" = None, jpdl32_ProcessStateType187: "jpdl32_ProcessDefinitionType" = None, jpdl32_ProcessStateType230: set["jpdl32_VariableType"] = None, jpdl32_ProcessStateType228: set["jpdl32_SubProcessType"] = None, jpdl32_ProcessStateType239: set["jpdl32_TimerType"] = None, jpdl32_ProcessStateType233: set["jpdl32_EventType"] = None, jpdl32_ProcessStateType236: set["jpdl32_ExceptionHandlerType"] = None, jpdl32_ProcessStateType242: set["jpdl32_TransitionType"] = None, jpdl32_ProcessStateType282: "jpdl32_SuperStateType" = None):
        self.group = group
        self.description = description
        self.async = async
        self.binding = binding
        self.name = name
        self.jpdl32_ProcessStateType = jpdl32_ProcessStateType
        self.jpdl32_ProcessStateType187 = jpdl32_ProcessStateType187
        self.jpdl32_ProcessStateType230 = jpdl32_ProcessStateType230 if jpdl32_ProcessStateType230 is not None else set()
        self.jpdl32_ProcessStateType228 = jpdl32_ProcessStateType228 if jpdl32_ProcessStateType228 is not None else set()
        self.jpdl32_ProcessStateType239 = jpdl32_ProcessStateType239 if jpdl32_ProcessStateType239 is not None else set()
        self.jpdl32_ProcessStateType233 = jpdl32_ProcessStateType233 if jpdl32_ProcessStateType233 is not None else set()
        self.jpdl32_ProcessStateType236 = jpdl32_ProcessStateType236 if jpdl32_ProcessStateType236 is not None else set()
        self.jpdl32_ProcessStateType242 = jpdl32_ProcessStateType242 if jpdl32_ProcessStateType242 is not None else set()
        self.jpdl32_ProcessStateType282 = jpdl32_ProcessStateType282
        
    @property
    def binding(self) -> str:
        return self.__binding

    @binding.setter
    def binding(self, binding: str):
        self.__binding = binding

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
    def jpdl32_ProcessStateType228(self):
        return self.__jpdl32_ProcessStateType228

    @jpdl32_ProcessStateType228.setter
    def jpdl32_ProcessStateType228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessStateType__jpdl32_ProcessStateType228", None)
        self.__jpdl32_ProcessStateType228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_SubProcessType"):
                    opp_val = getattr(item, "jpdl32_SubProcessType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_SubProcessType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_SubProcessType"):
                    opp_val = getattr(item, "jpdl32_SubProcessType", None)
                    
                    setattr(item, "jpdl32_SubProcessType", self)
                    

    @property
    def jpdl32_ProcessStateType230(self):
        return self.__jpdl32_ProcessStateType230

    @jpdl32_ProcessStateType230.setter
    def jpdl32_ProcessStateType230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessStateType__jpdl32_ProcessStateType230", None)
        self.__jpdl32_ProcessStateType230 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_VariableType231"):
                    opp_val = getattr(item, "jpdl32_VariableType231", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_VariableType231", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_VariableType231"):
                    opp_val = getattr(item, "jpdl32_VariableType231", None)
                    
                    setattr(item, "jpdl32_VariableType231", self)
                    

    @property
    def jpdl32_ProcessStateType236(self):
        return self.__jpdl32_ProcessStateType236

    @jpdl32_ProcessStateType236.setter
    def jpdl32_ProcessStateType236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessStateType__jpdl32_ProcessStateType236", None)
        self.__jpdl32_ProcessStateType236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ExceptionHandlerType237"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType237", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ExceptionHandlerType237", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ExceptionHandlerType237"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType237", None)
                    
                    setattr(item, "jpdl32_ExceptionHandlerType237", self)
                    

    @property
    def jpdl32_ProcessStateType(self):
        return self.__jpdl32_ProcessStateType

    @jpdl32_ProcessStateType.setter
    def jpdl32_ProcessStateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessStateType__jpdl32_ProcessStateType", None)
        self.__jpdl32_ProcessStateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot51"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot51"):
                opp_val = getattr(value, "jpdl32_DocumentRoot51", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ProcessStateType242(self):
        return self.__jpdl32_ProcessStateType242

    @jpdl32_ProcessStateType242.setter
    def jpdl32_ProcessStateType242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessStateType__jpdl32_ProcessStateType242", None)
        self.__jpdl32_ProcessStateType242 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TransitionType243"):
                    opp_val = getattr(item, "jpdl32_TransitionType243", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TransitionType243", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TransitionType243"):
                    opp_val = getattr(item, "jpdl32_TransitionType243", None)
                    
                    setattr(item, "jpdl32_TransitionType243", self)
                    

    @property
    def jpdl32_ProcessStateType233(self):
        return self.__jpdl32_ProcessStateType233

    @jpdl32_ProcessStateType233.setter
    def jpdl32_ProcessStateType233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessStateType__jpdl32_ProcessStateType233", None)
        self.__jpdl32_ProcessStateType233 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EventType234"):
                    opp_val = getattr(item, "jpdl32_EventType234", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EventType234", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EventType234"):
                    opp_val = getattr(item, "jpdl32_EventType234", None)
                    
                    setattr(item, "jpdl32_EventType234", self)
                    

    @property
    def jpdl32_ProcessStateType282(self):
        return self.__jpdl32_ProcessStateType282

    @jpdl32_ProcessStateType282.setter
    def jpdl32_ProcessStateType282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessStateType__jpdl32_ProcessStateType282", None)
        self.__jpdl32_ProcessStateType282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SuperStateType281"):
                opp_val = getattr(old_value, "jpdl32_SuperStateType281", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SuperStateType281"):
                opp_val = getattr(value, "jpdl32_SuperStateType281", None)
                if opp_val is None:
                    setattr(value, "jpdl32_SuperStateType281", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ProcessStateType187(self):
        return self.__jpdl32_ProcessStateType187

    @jpdl32_ProcessStateType187.setter
    def jpdl32_ProcessStateType187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessStateType__jpdl32_ProcessStateType187", None)
        self.__jpdl32_ProcessStateType187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType186"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType186"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType186", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType186", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ProcessStateType239(self):
        return self.__jpdl32_ProcessStateType239

    @jpdl32_ProcessStateType239.setter
    def jpdl32_ProcessStateType239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessStateType__jpdl32_ProcessStateType239", None)
        self.__jpdl32_ProcessStateType239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TimerType240"):
                    opp_val = getattr(item, "jpdl32_TimerType240", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TimerType240", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TimerType240"):
                    opp_val = getattr(item, "jpdl32_TimerType240", None)
                    
                    setattr(item, "jpdl32_TimerType240", self)
                    

class jpdl32_ProcessDefinitionType:

    def __init__(self, group: str, description: str, name: str, jpdl32_ProcessDefinitionType: "jpdl32_DocumentRoot" = None, jpdl32_ProcessDefinitionType168: set["jpdl32_SwimlaneType"] = None, jpdl32_ProcessDefinitionType180: set["jpdl32_TaskNodeType"] = None, jpdl32_ProcessDefinitionType171: set["jpdl32_StartStateType"] = None, jpdl32_ProcessDefinitionType174: set["jpdl32_NodeType"] = None, jpdl32_ProcessDefinitionType177: set["jpdl32_StateType"] = None, jpdl32_ProcessDefinitionType192: set["jpdl32_JoinType"] = None, jpdl32_ProcessDefinitionType183: set["jpdl32_SuperStateType"] = None, jpdl32_ProcessDefinitionType186: set["jpdl32_ProcessStateType"] = None, jpdl32_ProcessDefinitionType189: set["jpdl32_ForkType"] = None, jpdl32_ProcessDefinitionType204: set["jpdl32_ActionType"] = None, jpdl32_ProcessDefinitionType195: set["jpdl32_DecisionType"] = None, jpdl32_ProcessDefinitionType198: set["jpdl32_EndStateType"] = None, jpdl32_ProcessDefinitionType201: set["jpdl32_MailNodeType"] = None, jpdl32_ProcessDefinitionType207: set["jpdl32_ScriptType"] = None, jpdl32_ProcessDefinitionType210: set["jpdl32_CreateTimerType"] = None, jpdl32_ProcessDefinitionType213: set["jpdl32_CancelTimerType"] = None, jpdl32_ProcessDefinitionType225: set["jpdl32_TaskType"] = None, jpdl32_ProcessDefinitionType216: set["jpdl32_MailType"] = None, jpdl32_ProcessDefinitionType219: set["jpdl32_EventType"] = None, jpdl32_ProcessDefinitionType222: set["jpdl32_ExceptionHandlerType"] = None):
        self.group = group
        self.description = description
        self.name = name
        self.jpdl32_ProcessDefinitionType = jpdl32_ProcessDefinitionType
        self.jpdl32_ProcessDefinitionType168 = jpdl32_ProcessDefinitionType168 if jpdl32_ProcessDefinitionType168 is not None else set()
        self.jpdl32_ProcessDefinitionType180 = jpdl32_ProcessDefinitionType180 if jpdl32_ProcessDefinitionType180 is not None else set()
        self.jpdl32_ProcessDefinitionType171 = jpdl32_ProcessDefinitionType171 if jpdl32_ProcessDefinitionType171 is not None else set()
        self.jpdl32_ProcessDefinitionType174 = jpdl32_ProcessDefinitionType174 if jpdl32_ProcessDefinitionType174 is not None else set()
        self.jpdl32_ProcessDefinitionType177 = jpdl32_ProcessDefinitionType177 if jpdl32_ProcessDefinitionType177 is not None else set()
        self.jpdl32_ProcessDefinitionType192 = jpdl32_ProcessDefinitionType192 if jpdl32_ProcessDefinitionType192 is not None else set()
        self.jpdl32_ProcessDefinitionType183 = jpdl32_ProcessDefinitionType183 if jpdl32_ProcessDefinitionType183 is not None else set()
        self.jpdl32_ProcessDefinitionType186 = jpdl32_ProcessDefinitionType186 if jpdl32_ProcessDefinitionType186 is not None else set()
        self.jpdl32_ProcessDefinitionType189 = jpdl32_ProcessDefinitionType189 if jpdl32_ProcessDefinitionType189 is not None else set()
        self.jpdl32_ProcessDefinitionType204 = jpdl32_ProcessDefinitionType204 if jpdl32_ProcessDefinitionType204 is not None else set()
        self.jpdl32_ProcessDefinitionType195 = jpdl32_ProcessDefinitionType195 if jpdl32_ProcessDefinitionType195 is not None else set()
        self.jpdl32_ProcessDefinitionType198 = jpdl32_ProcessDefinitionType198 if jpdl32_ProcessDefinitionType198 is not None else set()
        self.jpdl32_ProcessDefinitionType201 = jpdl32_ProcessDefinitionType201 if jpdl32_ProcessDefinitionType201 is not None else set()
        self.jpdl32_ProcessDefinitionType207 = jpdl32_ProcessDefinitionType207 if jpdl32_ProcessDefinitionType207 is not None else set()
        self.jpdl32_ProcessDefinitionType210 = jpdl32_ProcessDefinitionType210 if jpdl32_ProcessDefinitionType210 is not None else set()
        self.jpdl32_ProcessDefinitionType213 = jpdl32_ProcessDefinitionType213 if jpdl32_ProcessDefinitionType213 is not None else set()
        self.jpdl32_ProcessDefinitionType225 = jpdl32_ProcessDefinitionType225 if jpdl32_ProcessDefinitionType225 is not None else set()
        self.jpdl32_ProcessDefinitionType216 = jpdl32_ProcessDefinitionType216 if jpdl32_ProcessDefinitionType216 is not None else set()
        self.jpdl32_ProcessDefinitionType219 = jpdl32_ProcessDefinitionType219 if jpdl32_ProcessDefinitionType219 is not None else set()
        self.jpdl32_ProcessDefinitionType222 = jpdl32_ProcessDefinitionType222 if jpdl32_ProcessDefinitionType222 is not None else set()
        
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
    def jpdl32_ProcessDefinitionType192(self):
        return self.__jpdl32_ProcessDefinitionType192

    @jpdl32_ProcessDefinitionType192.setter
    def jpdl32_ProcessDefinitionType192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType192", None)
        self.__jpdl32_ProcessDefinitionType192 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_JoinType193"):
                    opp_val = getattr(item, "jpdl32_JoinType193", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_JoinType193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_JoinType193"):
                    opp_val = getattr(item, "jpdl32_JoinType193", None)
                    
                    setattr(item, "jpdl32_JoinType193", self)
                    

    @property
    def jpdl32_ProcessDefinitionType216(self):
        return self.__jpdl32_ProcessDefinitionType216

    @jpdl32_ProcessDefinitionType216.setter
    def jpdl32_ProcessDefinitionType216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType216", None)
        self.__jpdl32_ProcessDefinitionType216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_MailType217"):
                    opp_val = getattr(item, "jpdl32_MailType217", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_MailType217", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_MailType217"):
                    opp_val = getattr(item, "jpdl32_MailType217", None)
                    
                    setattr(item, "jpdl32_MailType217", self)
                    

    @property
    def jpdl32_ProcessDefinitionType219(self):
        return self.__jpdl32_ProcessDefinitionType219

    @jpdl32_ProcessDefinitionType219.setter
    def jpdl32_ProcessDefinitionType219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType219", None)
        self.__jpdl32_ProcessDefinitionType219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EventType220"):
                    opp_val = getattr(item, "jpdl32_EventType220", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EventType220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EventType220"):
                    opp_val = getattr(item, "jpdl32_EventType220", None)
                    
                    setattr(item, "jpdl32_EventType220", self)
                    

    @property
    def jpdl32_ProcessDefinitionType186(self):
        return self.__jpdl32_ProcessDefinitionType186

    @jpdl32_ProcessDefinitionType186.setter
    def jpdl32_ProcessDefinitionType186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType186", None)
        self.__jpdl32_ProcessDefinitionType186 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ProcessStateType187"):
                    opp_val = getattr(item, "jpdl32_ProcessStateType187", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ProcessStateType187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ProcessStateType187"):
                    opp_val = getattr(item, "jpdl32_ProcessStateType187", None)
                    
                    setattr(item, "jpdl32_ProcessStateType187", self)
                    

    @property
    def jpdl32_ProcessDefinitionType207(self):
        return self.__jpdl32_ProcessDefinitionType207

    @jpdl32_ProcessDefinitionType207.setter
    def jpdl32_ProcessDefinitionType207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType207", None)
        self.__jpdl32_ProcessDefinitionType207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ScriptType208"):
                    opp_val = getattr(item, "jpdl32_ScriptType208", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ScriptType208", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ScriptType208"):
                    opp_val = getattr(item, "jpdl32_ScriptType208", None)
                    
                    setattr(item, "jpdl32_ScriptType208", self)
                    

    @property
    def jpdl32_ProcessDefinitionType210(self):
        return self.__jpdl32_ProcessDefinitionType210

    @jpdl32_ProcessDefinitionType210.setter
    def jpdl32_ProcessDefinitionType210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType210", None)
        self.__jpdl32_ProcessDefinitionType210 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_CreateTimerType211"):
                    opp_val = getattr(item, "jpdl32_CreateTimerType211", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_CreateTimerType211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_CreateTimerType211"):
                    opp_val = getattr(item, "jpdl32_CreateTimerType211", None)
                    
                    setattr(item, "jpdl32_CreateTimerType211", self)
                    

    @property
    def jpdl32_ProcessDefinitionType195(self):
        return self.__jpdl32_ProcessDefinitionType195

    @jpdl32_ProcessDefinitionType195.setter
    def jpdl32_ProcessDefinitionType195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType195", None)
        self.__jpdl32_ProcessDefinitionType195 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_DecisionType196"):
                    opp_val = getattr(item, "jpdl32_DecisionType196", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_DecisionType196", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_DecisionType196"):
                    opp_val = getattr(item, "jpdl32_DecisionType196", None)
                    
                    setattr(item, "jpdl32_DecisionType196", self)
                    

    @property
    def jpdl32_ProcessDefinitionType225(self):
        return self.__jpdl32_ProcessDefinitionType225

    @jpdl32_ProcessDefinitionType225.setter
    def jpdl32_ProcessDefinitionType225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType225", None)
        self.__jpdl32_ProcessDefinitionType225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TaskType226"):
                    opp_val = getattr(item, "jpdl32_TaskType226", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TaskType226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TaskType226"):
                    opp_val = getattr(item, "jpdl32_TaskType226", None)
                    
                    setattr(item, "jpdl32_TaskType226", self)
                    

    @property
    def jpdl32_ProcessDefinitionType204(self):
        return self.__jpdl32_ProcessDefinitionType204

    @jpdl32_ProcessDefinitionType204.setter
    def jpdl32_ProcessDefinitionType204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType204", None)
        self.__jpdl32_ProcessDefinitionType204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ActionType205"):
                    opp_val = getattr(item, "jpdl32_ActionType205", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ActionType205", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ActionType205"):
                    opp_val = getattr(item, "jpdl32_ActionType205", None)
                    
                    setattr(item, "jpdl32_ActionType205", self)
                    

    @property
    def jpdl32_ProcessDefinitionType168(self):
        return self.__jpdl32_ProcessDefinitionType168

    @jpdl32_ProcessDefinitionType168.setter
    def jpdl32_ProcessDefinitionType168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType168", None)
        self.__jpdl32_ProcessDefinitionType168 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_SwimlaneType169"):
                    opp_val = getattr(item, "jpdl32_SwimlaneType169", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_SwimlaneType169", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_SwimlaneType169"):
                    opp_val = getattr(item, "jpdl32_SwimlaneType169", None)
                    
                    setattr(item, "jpdl32_SwimlaneType169", self)
                    

    @property
    def jpdl32_ProcessDefinitionType174(self):
        return self.__jpdl32_ProcessDefinitionType174

    @jpdl32_ProcessDefinitionType174.setter
    def jpdl32_ProcessDefinitionType174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType174", None)
        self.__jpdl32_ProcessDefinitionType174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_NodeType175"):
                    opp_val = getattr(item, "jpdl32_NodeType175", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_NodeType175", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_NodeType175"):
                    opp_val = getattr(item, "jpdl32_NodeType175", None)
                    
                    setattr(item, "jpdl32_NodeType175", self)
                    

    @property
    def jpdl32_ProcessDefinitionType213(self):
        return self.__jpdl32_ProcessDefinitionType213

    @jpdl32_ProcessDefinitionType213.setter
    def jpdl32_ProcessDefinitionType213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType213", None)
        self.__jpdl32_ProcessDefinitionType213 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_CancelTimerType214"):
                    opp_val = getattr(item, "jpdl32_CancelTimerType214", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_CancelTimerType214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_CancelTimerType214"):
                    opp_val = getattr(item, "jpdl32_CancelTimerType214", None)
                    
                    setattr(item, "jpdl32_CancelTimerType214", self)
                    

    @property
    def jpdl32_ProcessDefinitionType222(self):
        return self.__jpdl32_ProcessDefinitionType222

    @jpdl32_ProcessDefinitionType222.setter
    def jpdl32_ProcessDefinitionType222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType222", None)
        self.__jpdl32_ProcessDefinitionType222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ExceptionHandlerType223"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType223", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ExceptionHandlerType223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ExceptionHandlerType223"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType223", None)
                    
                    setattr(item, "jpdl32_ExceptionHandlerType223", self)
                    

    @property
    def jpdl32_ProcessDefinitionType198(self):
        return self.__jpdl32_ProcessDefinitionType198

    @jpdl32_ProcessDefinitionType198.setter
    def jpdl32_ProcessDefinitionType198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType198", None)
        self.__jpdl32_ProcessDefinitionType198 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EndStateType199"):
                    opp_val = getattr(item, "jpdl32_EndStateType199", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EndStateType199", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EndStateType199"):
                    opp_val = getattr(item, "jpdl32_EndStateType199", None)
                    
                    setattr(item, "jpdl32_EndStateType199", self)
                    

    @property
    def jpdl32_ProcessDefinitionType171(self):
        return self.__jpdl32_ProcessDefinitionType171

    @jpdl32_ProcessDefinitionType171.setter
    def jpdl32_ProcessDefinitionType171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType171", None)
        self.__jpdl32_ProcessDefinitionType171 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_StartStateType172"):
                    opp_val = getattr(item, "jpdl32_StartStateType172", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_StartStateType172", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_StartStateType172"):
                    opp_val = getattr(item, "jpdl32_StartStateType172", None)
                    
                    setattr(item, "jpdl32_StartStateType172", self)
                    

    @property
    def jpdl32_ProcessDefinitionType189(self):
        return self.__jpdl32_ProcessDefinitionType189

    @jpdl32_ProcessDefinitionType189.setter
    def jpdl32_ProcessDefinitionType189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType189", None)
        self.__jpdl32_ProcessDefinitionType189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ForkType190"):
                    opp_val = getattr(item, "jpdl32_ForkType190", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ForkType190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ForkType190"):
                    opp_val = getattr(item, "jpdl32_ForkType190", None)
                    
                    setattr(item, "jpdl32_ForkType190", self)
                    

    @property
    def jpdl32_ProcessDefinitionType180(self):
        return self.__jpdl32_ProcessDefinitionType180

    @jpdl32_ProcessDefinitionType180.setter
    def jpdl32_ProcessDefinitionType180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType180", None)
        self.__jpdl32_ProcessDefinitionType180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TaskNodeType181"):
                    opp_val = getattr(item, "jpdl32_TaskNodeType181", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TaskNodeType181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TaskNodeType181"):
                    opp_val = getattr(item, "jpdl32_TaskNodeType181", None)
                    
                    setattr(item, "jpdl32_TaskNodeType181", self)
                    

    @property
    def jpdl32_ProcessDefinitionType201(self):
        return self.__jpdl32_ProcessDefinitionType201

    @jpdl32_ProcessDefinitionType201.setter
    def jpdl32_ProcessDefinitionType201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType201", None)
        self.__jpdl32_ProcessDefinitionType201 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_MailNodeType202"):
                    opp_val = getattr(item, "jpdl32_MailNodeType202", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_MailNodeType202", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_MailNodeType202"):
                    opp_val = getattr(item, "jpdl32_MailNodeType202", None)
                    
                    setattr(item, "jpdl32_MailNodeType202", self)
                    

    @property
    def jpdl32_ProcessDefinitionType177(self):
        return self.__jpdl32_ProcessDefinitionType177

    @jpdl32_ProcessDefinitionType177.setter
    def jpdl32_ProcessDefinitionType177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType177", None)
        self.__jpdl32_ProcessDefinitionType177 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_StateType178"):
                    opp_val = getattr(item, "jpdl32_StateType178", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_StateType178", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_StateType178"):
                    opp_val = getattr(item, "jpdl32_StateType178", None)
                    
                    setattr(item, "jpdl32_StateType178", self)
                    

    @property
    def jpdl32_ProcessDefinitionType183(self):
        return self.__jpdl32_ProcessDefinitionType183

    @jpdl32_ProcessDefinitionType183.setter
    def jpdl32_ProcessDefinitionType183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType183", None)
        self.__jpdl32_ProcessDefinitionType183 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_SuperStateType184"):
                    opp_val = getattr(item, "jpdl32_SuperStateType184", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_SuperStateType184", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_SuperStateType184"):
                    opp_val = getattr(item, "jpdl32_SuperStateType184", None)
                    
                    setattr(item, "jpdl32_SuperStateType184", self)
                    

    @property
    def jpdl32_ProcessDefinitionType(self):
        return self.__jpdl32_ProcessDefinitionType

    @jpdl32_ProcessDefinitionType.setter
    def jpdl32_ProcessDefinitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ProcessDefinitionType__jpdl32_ProcessDefinitionType", None)
        self.__jpdl32_ProcessDefinitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot49"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot49"):
                opp_val = getattr(value, "jpdl32_DocumentRoot49", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_EndStateType:

    def __init__(self, group: str, description: str, endCompleteProcess: str, name: str, jpdl32_EndStateType: "jpdl32_DocumentRoot" = None, jpdl32_EndStateType75: set["jpdl32_EventType"] = None, jpdl32_EndStateType78: set["jpdl32_ExceptionHandlerType"] = None, jpdl32_EndStateType199: "jpdl32_ProcessDefinitionType" = None, jpdl32_EndStateType294: "jpdl32_SuperStateType" = None):
        self.group = group
        self.description = description
        self.endCompleteProcess = endCompleteProcess
        self.name = name
        self.jpdl32_EndStateType = jpdl32_EndStateType
        self.jpdl32_EndStateType75 = jpdl32_EndStateType75 if jpdl32_EndStateType75 is not None else set()
        self.jpdl32_EndStateType78 = jpdl32_EndStateType78 if jpdl32_EndStateType78 is not None else set()
        self.jpdl32_EndStateType199 = jpdl32_EndStateType199
        self.jpdl32_EndStateType294 = jpdl32_EndStateType294
        
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
    def endCompleteProcess(self) -> str:
        return self.__endCompleteProcess

    @endCompleteProcess.setter
    def endCompleteProcess(self, endCompleteProcess: str):
        self.__endCompleteProcess = endCompleteProcess

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def jpdl32_EndStateType199(self):
        return self.__jpdl32_EndStateType199

    @jpdl32_EndStateType199.setter
    def jpdl32_EndStateType199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EndStateType__jpdl32_EndStateType199", None)
        self.__jpdl32_EndStateType199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType198"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType198", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType198"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType198", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType198", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EndStateType75(self):
        return self.__jpdl32_EndStateType75

    @jpdl32_EndStateType75.setter
    def jpdl32_EndStateType75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EndStateType__jpdl32_EndStateType75", None)
        self.__jpdl32_EndStateType75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EventType76"):
                    opp_val = getattr(item, "jpdl32_EventType76", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EventType76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EventType76"):
                    opp_val = getattr(item, "jpdl32_EventType76", None)
                    
                    setattr(item, "jpdl32_EventType76", self)
                    

    @property
    def jpdl32_EndStateType(self):
        return self.__jpdl32_EndStateType

    @jpdl32_EndStateType.setter
    def jpdl32_EndStateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EndStateType__jpdl32_EndStateType", None)
        self.__jpdl32_EndStateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot31"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot31"):
                opp_val = getattr(value, "jpdl32_DocumentRoot31", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EndStateType78(self):
        return self.__jpdl32_EndStateType78

    @jpdl32_EndStateType78.setter
    def jpdl32_EndStateType78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EndStateType__jpdl32_EndStateType78", None)
        self.__jpdl32_EndStateType78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ExceptionHandlerType79"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType79", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ExceptionHandlerType79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ExceptionHandlerType79"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType79", None)
                    
                    setattr(item, "jpdl32_ExceptionHandlerType79", self)
                    

    @property
    def jpdl32_EndStateType294(self):
        return self.__jpdl32_EndStateType294

    @jpdl32_EndStateType294.setter
    def jpdl32_EndStateType294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EndStateType__jpdl32_EndStateType294", None)
        self.__jpdl32_EndStateType294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SuperStateType293"):
                opp_val = getattr(old_value, "jpdl32_SuperStateType293", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SuperStateType293"):
                opp_val = getattr(value, "jpdl32_SuperStateType293", None)
                if opp_val is None:
                    setattr(value, "jpdl32_SuperStateType293", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_MailNodeType:

    def __init__(self, group: str, subject: str, text: str, description: str, text1: str, to: str, actors: str, async: str, name: str, subject1: str, template: str, jpdl32_MailNodeType: "jpdl32_DocumentRoot" = None, jpdl32_MailNodeType138: set["jpdl32_TransitionType"] = None, jpdl32_MailNodeType129: set["jpdl32_EventType"] = None, jpdl32_MailNodeType132: set["jpdl32_ExceptionHandlerType"] = None, jpdl32_MailNodeType135: set["jpdl32_TimerType"] = None, jpdl32_MailNodeType202: "jpdl32_ProcessDefinitionType" = None, jpdl32_MailNodeType297: "jpdl32_SuperStateType" = None):
        self.group = group
        self.subject = subject
        self.text = text
        self.description = description
        self.text1 = text1
        self.to = to
        self.actors = actors
        self.async = async
        self.name = name
        self.subject1 = subject1
        self.template = template
        self.jpdl32_MailNodeType = jpdl32_MailNodeType
        self.jpdl32_MailNodeType138 = jpdl32_MailNodeType138 if jpdl32_MailNodeType138 is not None else set()
        self.jpdl32_MailNodeType129 = jpdl32_MailNodeType129 if jpdl32_MailNodeType129 is not None else set()
        self.jpdl32_MailNodeType132 = jpdl32_MailNodeType132 if jpdl32_MailNodeType132 is not None else set()
        self.jpdl32_MailNodeType135 = jpdl32_MailNodeType135 if jpdl32_MailNodeType135 is not None else set()
        self.jpdl32_MailNodeType202 = jpdl32_MailNodeType202
        self.jpdl32_MailNodeType297 = jpdl32_MailNodeType297
        
    @property
    def text1(self) -> str:
        return self.__text1

    @text1.setter
    def text1(self, text1: str):
        self.__text1 = text1

    @property
    def subject1(self) -> str:
        return self.__subject1

    @subject1.setter
    def subject1(self, subject1: str):
        self.__subject1 = subject1

    @property
    def template(self) -> str:
        return self.__template

    @template.setter
    def template(self, template: str):
        self.__template = template

    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def actors(self) -> str:
        return self.__actors

    @actors.setter
    def actors(self, actors: str):
        self.__actors = actors

    @property
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

    @property
    def jpdl32_MailNodeType135(self):
        return self.__jpdl32_MailNodeType135

    @jpdl32_MailNodeType135.setter
    def jpdl32_MailNodeType135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_MailNodeType__jpdl32_MailNodeType135", None)
        self.__jpdl32_MailNodeType135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TimerType136"):
                    opp_val = getattr(item, "jpdl32_TimerType136", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TimerType136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TimerType136"):
                    opp_val = getattr(item, "jpdl32_TimerType136", None)
                    
                    setattr(item, "jpdl32_TimerType136", self)
                    

    @property
    def jpdl32_MailNodeType138(self):
        return self.__jpdl32_MailNodeType138

    @jpdl32_MailNodeType138.setter
    def jpdl32_MailNodeType138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_MailNodeType__jpdl32_MailNodeType138", None)
        self.__jpdl32_MailNodeType138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TransitionType139"):
                    opp_val = getattr(item, "jpdl32_TransitionType139", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TransitionType139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TransitionType139"):
                    opp_val = getattr(item, "jpdl32_TransitionType139", None)
                    
                    setattr(item, "jpdl32_TransitionType139", self)
                    

    @property
    def jpdl32_MailNodeType129(self):
        return self.__jpdl32_MailNodeType129

    @jpdl32_MailNodeType129.setter
    def jpdl32_MailNodeType129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_MailNodeType__jpdl32_MailNodeType129", None)
        self.__jpdl32_MailNodeType129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EventType130"):
                    opp_val = getattr(item, "jpdl32_EventType130", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EventType130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EventType130"):
                    opp_val = getattr(item, "jpdl32_EventType130", None)
                    
                    setattr(item, "jpdl32_EventType130", self)
                    

    @property
    def jpdl32_MailNodeType(self):
        return self.__jpdl32_MailNodeType

    @jpdl32_MailNodeType.setter
    def jpdl32_MailNodeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_MailNodeType__jpdl32_MailNodeType", None)
        self.__jpdl32_MailNodeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot45"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot45"):
                opp_val = getattr(value, "jpdl32_DocumentRoot45", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_MailNodeType202(self):
        return self.__jpdl32_MailNodeType202

    @jpdl32_MailNodeType202.setter
    def jpdl32_MailNodeType202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_MailNodeType__jpdl32_MailNodeType202", None)
        self.__jpdl32_MailNodeType202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType201"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType201", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType201"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType201", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType201", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_MailNodeType132(self):
        return self.__jpdl32_MailNodeType132

    @jpdl32_MailNodeType132.setter
    def jpdl32_MailNodeType132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_MailNodeType__jpdl32_MailNodeType132", None)
        self.__jpdl32_MailNodeType132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ExceptionHandlerType133"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType133", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ExceptionHandlerType133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ExceptionHandlerType133"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType133", None)
                    
                    setattr(item, "jpdl32_ExceptionHandlerType133", self)
                    

    @property
    def jpdl32_MailNodeType297(self):
        return self.__jpdl32_MailNodeType297

    @jpdl32_MailNodeType297.setter
    def jpdl32_MailNodeType297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_MailNodeType__jpdl32_MailNodeType297", None)
        self.__jpdl32_MailNodeType297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SuperStateType296"):
                opp_val = getattr(old_value, "jpdl32_SuperStateType296", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SuperStateType296"):
                opp_val = getattr(value, "jpdl32_SuperStateType296", None)
                if opp_val is None:
                    setattr(value, "jpdl32_SuperStateType296", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_MailType:

    def __init__(self, actors: str, async: str, group: str, subject: str, text: str, name: str, subject1: str, template: str, text1: str, to: str, jpdl32_MailType: "jpdl32_DocumentRoot" = None, jpdl32_MailType94: "jpdl32_EventType" = None, jpdl32_MailType154: "jpdl32_NodeType" = None, jpdl32_MailType217: "jpdl32_ProcessDefinitionType" = None, jpdl32_MailType356: "jpdl32_TimerType" = None, jpdl32_MailType373: "jpdl32_TransitionType" = None):
        self.actors = actors
        self.async = async
        self.group = group
        self.subject = subject
        self.text = text
        self.name = name
        self.subject1 = subject1
        self.template = template
        self.text1 = text1
        self.to = to
        self.jpdl32_MailType = jpdl32_MailType
        self.jpdl32_MailType94 = jpdl32_MailType94
        self.jpdl32_MailType154 = jpdl32_MailType154
        self.jpdl32_MailType217 = jpdl32_MailType217
        self.jpdl32_MailType356 = jpdl32_MailType356
        self.jpdl32_MailType373 = jpdl32_MailType373
        
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
    def template(self) -> str:
        return self.__template

    @template.setter
    def template(self, template: str):
        self.__template = template

    @property
    def actors(self) -> str:
        return self.__actors

    @actors.setter
    def actors(self, actors: str):
        self.__actors = actors

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def text1(self) -> str:
        return self.__text1

    @text1.setter
    def text1(self, text1: str):
        self.__text1 = text1

    @property
    def subject1(self) -> str:
        return self.__subject1

    @subject1.setter
    def subject1(self, subject1: str):
        self.__subject1 = subject1

    @property
    def jpdl32_MailType154(self):
        return self.__jpdl32_MailType154

    @jpdl32_MailType154.setter
    def jpdl32_MailType154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_MailType__jpdl32_MailType154", None)
        self.__jpdl32_MailType154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_NodeType153"):
                opp_val = getattr(old_value, "jpdl32_NodeType153", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_NodeType153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_NodeType153"):
                opp_val = getattr(value, "jpdl32_NodeType153", None)
                setattr(value, "jpdl32_NodeType153", self)

    @property
    def jpdl32_MailType356(self):
        return self.__jpdl32_MailType356

    @jpdl32_MailType356.setter
    def jpdl32_MailType356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_MailType__jpdl32_MailType356", None)
        self.__jpdl32_MailType356 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TimerType355"):
                opp_val = getattr(old_value, "jpdl32_TimerType355", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_TimerType355", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TimerType355"):
                opp_val = getattr(value, "jpdl32_TimerType355", None)
                setattr(value, "jpdl32_TimerType355", self)

    @property
    def jpdl32_MailType373(self):
        return self.__jpdl32_MailType373

    @jpdl32_MailType373.setter
    def jpdl32_MailType373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_MailType__jpdl32_MailType373", None)
        self.__jpdl32_MailType373 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TransitionType372"):
                opp_val = getattr(old_value, "jpdl32_TransitionType372", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TransitionType372"):
                opp_val = getattr(value, "jpdl32_TransitionType372", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TransitionType372", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_MailType94(self):
        return self.__jpdl32_MailType94

    @jpdl32_MailType94.setter
    def jpdl32_MailType94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_MailType__jpdl32_MailType94", None)
        self.__jpdl32_MailType94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_EventType93"):
                opp_val = getattr(old_value, "jpdl32_EventType93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_EventType93"):
                opp_val = getattr(value, "jpdl32_EventType93", None)
                if opp_val is None:
                    setattr(value, "jpdl32_EventType93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_MailType217(self):
        return self.__jpdl32_MailType217

    @jpdl32_MailType217.setter
    def jpdl32_MailType217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_MailType__jpdl32_MailType217", None)
        self.__jpdl32_MailType217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType216"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType216", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType216"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType216", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType216", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_MailType(self):
        return self.__jpdl32_MailType

    @jpdl32_MailType.setter
    def jpdl32_MailType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_MailType__jpdl32_MailType", None)
        self.__jpdl32_MailType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot43"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot43"):
                opp_val = getattr(value, "jpdl32_DocumentRoot43", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_JoinType:

    def __init__(self, nodeContentElements: str, description: str, async: str, name: str, jpdl32_JoinType: "jpdl32_DocumentRoot" = None, jpdl32_JoinType117: set["jpdl32_EventType"] = None, jpdl32_JoinType120: set["jpdl32_ExceptionHandlerType"] = None, jpdl32_JoinType123: set["jpdl32_TimerType"] = None, jpdl32_JoinType126: set["jpdl32_TransitionType"] = None, jpdl32_JoinType193: "jpdl32_ProcessDefinitionType" = None, jpdl32_JoinType288: "jpdl32_SuperStateType" = None):
        self.nodeContentElements = nodeContentElements
        self.description = description
        self.async = async
        self.name = name
        self.jpdl32_JoinType = jpdl32_JoinType
        self.jpdl32_JoinType117 = jpdl32_JoinType117 if jpdl32_JoinType117 is not None else set()
        self.jpdl32_JoinType120 = jpdl32_JoinType120 if jpdl32_JoinType120 is not None else set()
        self.jpdl32_JoinType123 = jpdl32_JoinType123 if jpdl32_JoinType123 is not None else set()
        self.jpdl32_JoinType126 = jpdl32_JoinType126 if jpdl32_JoinType126 is not None else set()
        self.jpdl32_JoinType193 = jpdl32_JoinType193
        self.jpdl32_JoinType288 = jpdl32_JoinType288
        
    @property
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

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
    def jpdl32_JoinType117(self):
        return self.__jpdl32_JoinType117

    @jpdl32_JoinType117.setter
    def jpdl32_JoinType117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_JoinType__jpdl32_JoinType117", None)
        self.__jpdl32_JoinType117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EventType118"):
                    opp_val = getattr(item, "jpdl32_EventType118", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EventType118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EventType118"):
                    opp_val = getattr(item, "jpdl32_EventType118", None)
                    
                    setattr(item, "jpdl32_EventType118", self)
                    

    @property
    def jpdl32_JoinType193(self):
        return self.__jpdl32_JoinType193

    @jpdl32_JoinType193.setter
    def jpdl32_JoinType193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_JoinType__jpdl32_JoinType193", None)
        self.__jpdl32_JoinType193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType192"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType192", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType192"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType192", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType192", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_JoinType(self):
        return self.__jpdl32_JoinType

    @jpdl32_JoinType.setter
    def jpdl32_JoinType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_JoinType__jpdl32_JoinType", None)
        self.__jpdl32_JoinType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot41"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot41"):
                opp_val = getattr(value, "jpdl32_DocumentRoot41", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_JoinType126(self):
        return self.__jpdl32_JoinType126

    @jpdl32_JoinType126.setter
    def jpdl32_JoinType126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_JoinType__jpdl32_JoinType126", None)
        self.__jpdl32_JoinType126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TransitionType127"):
                    opp_val = getattr(item, "jpdl32_TransitionType127", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TransitionType127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TransitionType127"):
                    opp_val = getattr(item, "jpdl32_TransitionType127", None)
                    
                    setattr(item, "jpdl32_TransitionType127", self)
                    

    @property
    def jpdl32_JoinType288(self):
        return self.__jpdl32_JoinType288

    @jpdl32_JoinType288.setter
    def jpdl32_JoinType288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_JoinType__jpdl32_JoinType288", None)
        self.__jpdl32_JoinType288 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SuperStateType287"):
                opp_val = getattr(old_value, "jpdl32_SuperStateType287", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SuperStateType287"):
                opp_val = getattr(value, "jpdl32_SuperStateType287", None)
                if opp_val is None:
                    setattr(value, "jpdl32_SuperStateType287", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_JoinType120(self):
        return self.__jpdl32_JoinType120

    @jpdl32_JoinType120.setter
    def jpdl32_JoinType120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_JoinType__jpdl32_JoinType120", None)
        self.__jpdl32_JoinType120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ExceptionHandlerType121"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType121", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ExceptionHandlerType121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ExceptionHandlerType121"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType121", None)
                    
                    setattr(item, "jpdl32_ExceptionHandlerType121", self)
                    

    @property
    def jpdl32_JoinType123(self):
        return self.__jpdl32_JoinType123

    @jpdl32_JoinType123.setter
    def jpdl32_JoinType123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_JoinType__jpdl32_JoinType123", None)
        self.__jpdl32_JoinType123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TimerType124"):
                    opp_val = getattr(item, "jpdl32_TimerType124", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TimerType124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TimerType124"):
                    opp_val = getattr(item, "jpdl32_TimerType124", None)
                    
                    setattr(item, "jpdl32_TimerType124", self)
                    

class jpdl32_ForkType:

    def __init__(self, group: str, description: str, async: str, name: str, jpdl32_ForkType: "jpdl32_DocumentRoot" = None, jpdl32_ForkType102: set["jpdl32_ScriptType"] = None, jpdl32_ForkType114: set["jpdl32_TransitionType"] = None, jpdl32_ForkType105: set["jpdl32_EventType"] = None, jpdl32_ForkType108: set["jpdl32_ExceptionHandlerType"] = None, jpdl32_ForkType111: set["jpdl32_TimerType"] = None, jpdl32_ForkType190: "jpdl32_ProcessDefinitionType" = None, jpdl32_ForkType285: "jpdl32_SuperStateType" = None):
        self.group = group
        self.description = description
        self.async = async
        self.name = name
        self.jpdl32_ForkType = jpdl32_ForkType
        self.jpdl32_ForkType102 = jpdl32_ForkType102 if jpdl32_ForkType102 is not None else set()
        self.jpdl32_ForkType114 = jpdl32_ForkType114 if jpdl32_ForkType114 is not None else set()
        self.jpdl32_ForkType105 = jpdl32_ForkType105 if jpdl32_ForkType105 is not None else set()
        self.jpdl32_ForkType108 = jpdl32_ForkType108 if jpdl32_ForkType108 is not None else set()
        self.jpdl32_ForkType111 = jpdl32_ForkType111 if jpdl32_ForkType111 is not None else set()
        self.jpdl32_ForkType190 = jpdl32_ForkType190
        self.jpdl32_ForkType285 = jpdl32_ForkType285
        
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
    def jpdl32_ForkType105(self):
        return self.__jpdl32_ForkType105

    @jpdl32_ForkType105.setter
    def jpdl32_ForkType105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ForkType__jpdl32_ForkType105", None)
        self.__jpdl32_ForkType105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EventType106"):
                    opp_val = getattr(item, "jpdl32_EventType106", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EventType106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EventType106"):
                    opp_val = getattr(item, "jpdl32_EventType106", None)
                    
                    setattr(item, "jpdl32_EventType106", self)
                    

    @property
    def jpdl32_ForkType190(self):
        return self.__jpdl32_ForkType190

    @jpdl32_ForkType190.setter
    def jpdl32_ForkType190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ForkType__jpdl32_ForkType190", None)
        self.__jpdl32_ForkType190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType189"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType189"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType189", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ForkType285(self):
        return self.__jpdl32_ForkType285

    @jpdl32_ForkType285.setter
    def jpdl32_ForkType285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ForkType__jpdl32_ForkType285", None)
        self.__jpdl32_ForkType285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SuperStateType284"):
                opp_val = getattr(old_value, "jpdl32_SuperStateType284", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SuperStateType284"):
                opp_val = getattr(value, "jpdl32_SuperStateType284", None)
                if opp_val is None:
                    setattr(value, "jpdl32_SuperStateType284", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ForkType108(self):
        return self.__jpdl32_ForkType108

    @jpdl32_ForkType108.setter
    def jpdl32_ForkType108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ForkType__jpdl32_ForkType108", None)
        self.__jpdl32_ForkType108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ExceptionHandlerType109"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType109", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ExceptionHandlerType109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ExceptionHandlerType109"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType109", None)
                    
                    setattr(item, "jpdl32_ExceptionHandlerType109", self)
                    

    @property
    def jpdl32_ForkType102(self):
        return self.__jpdl32_ForkType102

    @jpdl32_ForkType102.setter
    def jpdl32_ForkType102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ForkType__jpdl32_ForkType102", None)
        self.__jpdl32_ForkType102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ScriptType103"):
                    opp_val = getattr(item, "jpdl32_ScriptType103", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ScriptType103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ScriptType103"):
                    opp_val = getattr(item, "jpdl32_ScriptType103", None)
                    
                    setattr(item, "jpdl32_ScriptType103", self)
                    

    @property
    def jpdl32_ForkType114(self):
        return self.__jpdl32_ForkType114

    @jpdl32_ForkType114.setter
    def jpdl32_ForkType114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ForkType__jpdl32_ForkType114", None)
        self.__jpdl32_ForkType114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TransitionType115"):
                    opp_val = getattr(item, "jpdl32_TransitionType115", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TransitionType115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TransitionType115"):
                    opp_val = getattr(item, "jpdl32_TransitionType115", None)
                    
                    setattr(item, "jpdl32_TransitionType115", self)
                    

    @property
    def jpdl32_ForkType(self):
        return self.__jpdl32_ForkType

    @jpdl32_ForkType.setter
    def jpdl32_ForkType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ForkType__jpdl32_ForkType", None)
        self.__jpdl32_ForkType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot39"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot39"):
                opp_val = getattr(value, "jpdl32_DocumentRoot39", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ForkType111(self):
        return self.__jpdl32_ForkType111

    @jpdl32_ForkType111.setter
    def jpdl32_ForkType111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ForkType__jpdl32_ForkType111", None)
        self.__jpdl32_ForkType111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TimerType112"):
                    opp_val = getattr(item, "jpdl32_TimerType112", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TimerType112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TimerType112"):
                    opp_val = getattr(item, "jpdl32_TimerType112", None)
                    
                    setattr(item, "jpdl32_TimerType112", self)
                    

class jpdl32_EStringToStringMapEntry:

    pass
class jpdl32_DocumentRoot:

    def __init__(self, mixed: str, description: str, recipients: str, template: str, text: str, subject: str, to: str, jpdl32_DocumentRoot: set["jpdl32_EStringToStringMapEntry"] = None, jpdl32_DocumentRoot18: set["jpdl32_AssignmentType"] = None, jpdl32_DocumentRoot20: set["jpdl32_CancelTimerType"] = None, jpdl32_DocumentRoot22: set["jpdl32_Delegation"] = None, jpdl32_DocumentRoot25: set["jpdl32_CreateTimerType"] = None, jpdl32_DocumentRoot28: set["jpdl32_DecisionType"] = None, jpdl32_DocumentRoot12: set["jpdl32_EStringToStringMapEntry"] = None, jpdl32_DocumentRoot15: set["jpdl32_ActionType"] = None, jpdl32_DocumentRoot33: set["jpdl32_EventType"] = None, jpdl32_DocumentRoot36: set["jpdl32_ExceptionHandlerType"] = None, jpdl32_DocumentRoot39: set["jpdl32_ForkType"] = None, jpdl32_DocumentRoot41: set["jpdl32_JoinType"] = None, jpdl32_DocumentRoot43: set["jpdl32_MailType"] = None, jpdl32_DocumentRoot45: set["jpdl32_MailNodeType"] = None, jpdl32_DocumentRoot31: set["jpdl32_EndStateType"] = None, jpdl32_DocumentRoot49: set["jpdl32_ProcessDefinitionType"] = None, jpdl32_DocumentRoot51: set["jpdl32_ProcessStateType"] = None, jpdl32_DocumentRoot53: set["jpdl32_ScriptType"] = None, jpdl32_DocumentRoot56: set["jpdl32_StartStateType"] = None, jpdl32_DocumentRoot58: set["jpdl32_StateType"] = None, jpdl32_DocumentRoot47: set["jpdl32_NodeType"] = None, jpdl32_DocumentRoot62: set["jpdl32_SwimlaneType"] = None, jpdl32_DocumentRoot64: set["jpdl32_TaskType"] = None, jpdl32_DocumentRoot66: set["jpdl32_TaskNodeType"] = None, jpdl32_DocumentRoot60: set["jpdl32_SuperStateType"] = None, jpdl32_DocumentRoot70: set["jpdl32_TransitionType"] = None, jpdl32_DocumentRoot73: set["jpdl32_VariableType"] = None, jpdl32_DocumentRoot68: set["jpdl32_TimerType"] = None):
        self.mixed = mixed
        self.description = description
        self.recipients = recipients
        self.template = template
        self.text = text
        self.subject = subject
        self.to = to
        self.jpdl32_DocumentRoot = jpdl32_DocumentRoot if jpdl32_DocumentRoot is not None else set()
        self.jpdl32_DocumentRoot18 = jpdl32_DocumentRoot18 if jpdl32_DocumentRoot18 is not None else set()
        self.jpdl32_DocumentRoot20 = jpdl32_DocumentRoot20 if jpdl32_DocumentRoot20 is not None else set()
        self.jpdl32_DocumentRoot22 = jpdl32_DocumentRoot22 if jpdl32_DocumentRoot22 is not None else set()
        self.jpdl32_DocumentRoot25 = jpdl32_DocumentRoot25 if jpdl32_DocumentRoot25 is not None else set()
        self.jpdl32_DocumentRoot28 = jpdl32_DocumentRoot28 if jpdl32_DocumentRoot28 is not None else set()
        self.jpdl32_DocumentRoot12 = jpdl32_DocumentRoot12 if jpdl32_DocumentRoot12 is not None else set()
        self.jpdl32_DocumentRoot15 = jpdl32_DocumentRoot15 if jpdl32_DocumentRoot15 is not None else set()
        self.jpdl32_DocumentRoot33 = jpdl32_DocumentRoot33 if jpdl32_DocumentRoot33 is not None else set()
        self.jpdl32_DocumentRoot36 = jpdl32_DocumentRoot36 if jpdl32_DocumentRoot36 is not None else set()
        self.jpdl32_DocumentRoot39 = jpdl32_DocumentRoot39 if jpdl32_DocumentRoot39 is not None else set()
        self.jpdl32_DocumentRoot41 = jpdl32_DocumentRoot41 if jpdl32_DocumentRoot41 is not None else set()
        self.jpdl32_DocumentRoot43 = jpdl32_DocumentRoot43 if jpdl32_DocumentRoot43 is not None else set()
        self.jpdl32_DocumentRoot45 = jpdl32_DocumentRoot45 if jpdl32_DocumentRoot45 is not None else set()
        self.jpdl32_DocumentRoot31 = jpdl32_DocumentRoot31 if jpdl32_DocumentRoot31 is not None else set()
        self.jpdl32_DocumentRoot49 = jpdl32_DocumentRoot49 if jpdl32_DocumentRoot49 is not None else set()
        self.jpdl32_DocumentRoot51 = jpdl32_DocumentRoot51 if jpdl32_DocumentRoot51 is not None else set()
        self.jpdl32_DocumentRoot53 = jpdl32_DocumentRoot53 if jpdl32_DocumentRoot53 is not None else set()
        self.jpdl32_DocumentRoot56 = jpdl32_DocumentRoot56 if jpdl32_DocumentRoot56 is not None else set()
        self.jpdl32_DocumentRoot58 = jpdl32_DocumentRoot58 if jpdl32_DocumentRoot58 is not None else set()
        self.jpdl32_DocumentRoot47 = jpdl32_DocumentRoot47 if jpdl32_DocumentRoot47 is not None else set()
        self.jpdl32_DocumentRoot62 = jpdl32_DocumentRoot62 if jpdl32_DocumentRoot62 is not None else set()
        self.jpdl32_DocumentRoot64 = jpdl32_DocumentRoot64 if jpdl32_DocumentRoot64 is not None else set()
        self.jpdl32_DocumentRoot66 = jpdl32_DocumentRoot66 if jpdl32_DocumentRoot66 is not None else set()
        self.jpdl32_DocumentRoot60 = jpdl32_DocumentRoot60 if jpdl32_DocumentRoot60 is not None else set()
        self.jpdl32_DocumentRoot70 = jpdl32_DocumentRoot70 if jpdl32_DocumentRoot70 is not None else set()
        self.jpdl32_DocumentRoot73 = jpdl32_DocumentRoot73 if jpdl32_DocumentRoot73 is not None else set()
        self.jpdl32_DocumentRoot68 = jpdl32_DocumentRoot68 if jpdl32_DocumentRoot68 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def recipients(self) -> str:
        return self.__recipients

    @recipients.setter
    def recipients(self, recipients: str):
        self.__recipients = recipients

    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def template(self) -> str:
        return self.__template

    @template.setter
    def template(self, template: str):
        self.__template = template

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def jpdl32_DocumentRoot31(self):
        return self.__jpdl32_DocumentRoot31

    @jpdl32_DocumentRoot31.setter
    def jpdl32_DocumentRoot31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot31", None)
        self.__jpdl32_DocumentRoot31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EndStateType"):
                    opp_val = getattr(item, "jpdl32_EndStateType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EndStateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EndStateType"):
                    opp_val = getattr(item, "jpdl32_EndStateType", None)
                    
                    setattr(item, "jpdl32_EndStateType", self)
                    

    @property
    def jpdl32_DocumentRoot60(self):
        return self.__jpdl32_DocumentRoot60

    @jpdl32_DocumentRoot60.setter
    def jpdl32_DocumentRoot60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot60", None)
        self.__jpdl32_DocumentRoot60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_SuperStateType"):
                    opp_val = getattr(item, "jpdl32_SuperStateType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_SuperStateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_SuperStateType"):
                    opp_val = getattr(item, "jpdl32_SuperStateType", None)
                    
                    setattr(item, "jpdl32_SuperStateType", self)
                    

    @property
    def jpdl32_DocumentRoot68(self):
        return self.__jpdl32_DocumentRoot68

    @jpdl32_DocumentRoot68.setter
    def jpdl32_DocumentRoot68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot68", None)
        self.__jpdl32_DocumentRoot68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TimerType"):
                    opp_val = getattr(item, "jpdl32_TimerType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TimerType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TimerType"):
                    opp_val = getattr(item, "jpdl32_TimerType", None)
                    
                    setattr(item, "jpdl32_TimerType", self)
                    

    @property
    def jpdl32_DocumentRoot49(self):
        return self.__jpdl32_DocumentRoot49

    @jpdl32_DocumentRoot49.setter
    def jpdl32_DocumentRoot49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot49", None)
        self.__jpdl32_DocumentRoot49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ProcessDefinitionType"):
                    opp_val = getattr(item, "jpdl32_ProcessDefinitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ProcessDefinitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ProcessDefinitionType"):
                    opp_val = getattr(item, "jpdl32_ProcessDefinitionType", None)
                    
                    setattr(item, "jpdl32_ProcessDefinitionType", self)
                    

    @property
    def jpdl32_DocumentRoot22(self):
        return self.__jpdl32_DocumentRoot22

    @jpdl32_DocumentRoot22.setter
    def jpdl32_DocumentRoot22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot22", None)
        self.__jpdl32_DocumentRoot22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_Delegation23"):
                    opp_val = getattr(item, "jpdl32_Delegation23", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_Delegation23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_Delegation23"):
                    opp_val = getattr(item, "jpdl32_Delegation23", None)
                    
                    setattr(item, "jpdl32_Delegation23", self)
                    

    @property
    def jpdl32_DocumentRoot28(self):
        return self.__jpdl32_DocumentRoot28

    @jpdl32_DocumentRoot28.setter
    def jpdl32_DocumentRoot28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot28", None)
        self.__jpdl32_DocumentRoot28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_DecisionType29"):
                    opp_val = getattr(item, "jpdl32_DecisionType29", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_DecisionType29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_DecisionType29"):
                    opp_val = getattr(item, "jpdl32_DecisionType29", None)
                    
                    setattr(item, "jpdl32_DecisionType29", self)
                    

    @property
    def jpdl32_DocumentRoot18(self):
        return self.__jpdl32_DocumentRoot18

    @jpdl32_DocumentRoot18.setter
    def jpdl32_DocumentRoot18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot18", None)
        self.__jpdl32_DocumentRoot18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_AssignmentType"):
                    opp_val = getattr(item, "jpdl32_AssignmentType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_AssignmentType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_AssignmentType"):
                    opp_val = getattr(item, "jpdl32_AssignmentType", None)
                    
                    setattr(item, "jpdl32_AssignmentType", self)
                    

    @property
    def jpdl32_DocumentRoot47(self):
        return self.__jpdl32_DocumentRoot47

    @jpdl32_DocumentRoot47.setter
    def jpdl32_DocumentRoot47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot47", None)
        self.__jpdl32_DocumentRoot47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_NodeType"):
                    opp_val = getattr(item, "jpdl32_NodeType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_NodeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_NodeType"):
                    opp_val = getattr(item, "jpdl32_NodeType", None)
                    
                    setattr(item, "jpdl32_NodeType", self)
                    

    @property
    def jpdl32_DocumentRoot53(self):
        return self.__jpdl32_DocumentRoot53

    @jpdl32_DocumentRoot53.setter
    def jpdl32_DocumentRoot53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot53", None)
        self.__jpdl32_DocumentRoot53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ScriptType54"):
                    opp_val = getattr(item, "jpdl32_ScriptType54", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ScriptType54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ScriptType54"):
                    opp_val = getattr(item, "jpdl32_ScriptType54", None)
                    
                    setattr(item, "jpdl32_ScriptType54", self)
                    

    @property
    def jpdl32_DocumentRoot20(self):
        return self.__jpdl32_DocumentRoot20

    @jpdl32_DocumentRoot20.setter
    def jpdl32_DocumentRoot20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot20", None)
        self.__jpdl32_DocumentRoot20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_CancelTimerType"):
                    opp_val = getattr(item, "jpdl32_CancelTimerType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_CancelTimerType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_CancelTimerType"):
                    opp_val = getattr(item, "jpdl32_CancelTimerType", None)
                    
                    setattr(item, "jpdl32_CancelTimerType", self)
                    

    @property
    def jpdl32_DocumentRoot36(self):
        return self.__jpdl32_DocumentRoot36

    @jpdl32_DocumentRoot36.setter
    def jpdl32_DocumentRoot36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot36", None)
        self.__jpdl32_DocumentRoot36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ExceptionHandlerType37"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType37", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ExceptionHandlerType37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ExceptionHandlerType37"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType37", None)
                    
                    setattr(item, "jpdl32_ExceptionHandlerType37", self)
                    

    @property
    def jpdl32_DocumentRoot41(self):
        return self.__jpdl32_DocumentRoot41

    @jpdl32_DocumentRoot41.setter
    def jpdl32_DocumentRoot41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot41", None)
        self.__jpdl32_DocumentRoot41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_JoinType"):
                    opp_val = getattr(item, "jpdl32_JoinType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_JoinType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_JoinType"):
                    opp_val = getattr(item, "jpdl32_JoinType", None)
                    
                    setattr(item, "jpdl32_JoinType", self)
                    

    @property
    def jpdl32_DocumentRoot15(self):
        return self.__jpdl32_DocumentRoot15

    @jpdl32_DocumentRoot15.setter
    def jpdl32_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot15", None)
        self.__jpdl32_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ActionType16"):
                    opp_val = getattr(item, "jpdl32_ActionType16", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ActionType16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ActionType16"):
                    opp_val = getattr(item, "jpdl32_ActionType16", None)
                    
                    setattr(item, "jpdl32_ActionType16", self)
                    

    @property
    def jpdl32_DocumentRoot12(self):
        return self.__jpdl32_DocumentRoot12

    @jpdl32_DocumentRoot12.setter
    def jpdl32_DocumentRoot12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot12", None)
        self.__jpdl32_DocumentRoot12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EStringToStringMapEntry13"):
                    opp_val = getattr(item, "jpdl32_EStringToStringMapEntry13", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EStringToStringMapEntry13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EStringToStringMapEntry13"):
                    opp_val = getattr(item, "jpdl32_EStringToStringMapEntry13", None)
                    
                    setattr(item, "jpdl32_EStringToStringMapEntry13", self)
                    

    @property
    def jpdl32_DocumentRoot56(self):
        return self.__jpdl32_DocumentRoot56

    @jpdl32_DocumentRoot56.setter
    def jpdl32_DocumentRoot56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot56", None)
        self.__jpdl32_DocumentRoot56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_StartStateType"):
                    opp_val = getattr(item, "jpdl32_StartStateType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_StartStateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_StartStateType"):
                    opp_val = getattr(item, "jpdl32_StartStateType", None)
                    
                    setattr(item, "jpdl32_StartStateType", self)
                    

    @property
    def jpdl32_DocumentRoot39(self):
        return self.__jpdl32_DocumentRoot39

    @jpdl32_DocumentRoot39.setter
    def jpdl32_DocumentRoot39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot39", None)
        self.__jpdl32_DocumentRoot39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ForkType"):
                    opp_val = getattr(item, "jpdl32_ForkType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ForkType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ForkType"):
                    opp_val = getattr(item, "jpdl32_ForkType", None)
                    
                    setattr(item, "jpdl32_ForkType", self)
                    

    @property
    def jpdl32_DocumentRoot66(self):
        return self.__jpdl32_DocumentRoot66

    @jpdl32_DocumentRoot66.setter
    def jpdl32_DocumentRoot66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot66", None)
        self.__jpdl32_DocumentRoot66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TaskNodeType"):
                    opp_val = getattr(item, "jpdl32_TaskNodeType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TaskNodeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TaskNodeType"):
                    opp_val = getattr(item, "jpdl32_TaskNodeType", None)
                    
                    setattr(item, "jpdl32_TaskNodeType", self)
                    

    @property
    def jpdl32_DocumentRoot43(self):
        return self.__jpdl32_DocumentRoot43

    @jpdl32_DocumentRoot43.setter
    def jpdl32_DocumentRoot43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot43", None)
        self.__jpdl32_DocumentRoot43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_MailType"):
                    opp_val = getattr(item, "jpdl32_MailType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_MailType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_MailType"):
                    opp_val = getattr(item, "jpdl32_MailType", None)
                    
                    setattr(item, "jpdl32_MailType", self)
                    

    @property
    def jpdl32_DocumentRoot33(self):
        return self.__jpdl32_DocumentRoot33

    @jpdl32_DocumentRoot33.setter
    def jpdl32_DocumentRoot33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot33", None)
        self.__jpdl32_DocumentRoot33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EventType34"):
                    opp_val = getattr(item, "jpdl32_EventType34", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EventType34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EventType34"):
                    opp_val = getattr(item, "jpdl32_EventType34", None)
                    
                    setattr(item, "jpdl32_EventType34", self)
                    

    @property
    def jpdl32_DocumentRoot64(self):
        return self.__jpdl32_DocumentRoot64

    @jpdl32_DocumentRoot64.setter
    def jpdl32_DocumentRoot64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot64", None)
        self.__jpdl32_DocumentRoot64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TaskType"):
                    opp_val = getattr(item, "jpdl32_TaskType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TaskType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TaskType"):
                    opp_val = getattr(item, "jpdl32_TaskType", None)
                    
                    setattr(item, "jpdl32_TaskType", self)
                    

    @property
    def jpdl32_DocumentRoot70(self):
        return self.__jpdl32_DocumentRoot70

    @jpdl32_DocumentRoot70.setter
    def jpdl32_DocumentRoot70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot70", None)
        self.__jpdl32_DocumentRoot70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TransitionType71"):
                    opp_val = getattr(item, "jpdl32_TransitionType71", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TransitionType71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TransitionType71"):
                    opp_val = getattr(item, "jpdl32_TransitionType71", None)
                    
                    setattr(item, "jpdl32_TransitionType71", self)
                    

    @property
    def jpdl32_DocumentRoot45(self):
        return self.__jpdl32_DocumentRoot45

    @jpdl32_DocumentRoot45.setter
    def jpdl32_DocumentRoot45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot45", None)
        self.__jpdl32_DocumentRoot45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_MailNodeType"):
                    opp_val = getattr(item, "jpdl32_MailNodeType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_MailNodeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_MailNodeType"):
                    opp_val = getattr(item, "jpdl32_MailNodeType", None)
                    
                    setattr(item, "jpdl32_MailNodeType", self)
                    

    @property
    def jpdl32_DocumentRoot51(self):
        return self.__jpdl32_DocumentRoot51

    @jpdl32_DocumentRoot51.setter
    def jpdl32_DocumentRoot51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot51", None)
        self.__jpdl32_DocumentRoot51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ProcessStateType"):
                    opp_val = getattr(item, "jpdl32_ProcessStateType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ProcessStateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ProcessStateType"):
                    opp_val = getattr(item, "jpdl32_ProcessStateType", None)
                    
                    setattr(item, "jpdl32_ProcessStateType", self)
                    

    @property
    def jpdl32_DocumentRoot62(self):
        return self.__jpdl32_DocumentRoot62

    @jpdl32_DocumentRoot62.setter
    def jpdl32_DocumentRoot62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot62", None)
        self.__jpdl32_DocumentRoot62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_SwimlaneType"):
                    opp_val = getattr(item, "jpdl32_SwimlaneType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_SwimlaneType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_SwimlaneType"):
                    opp_val = getattr(item, "jpdl32_SwimlaneType", None)
                    
                    setattr(item, "jpdl32_SwimlaneType", self)
                    

    @property
    def jpdl32_DocumentRoot58(self):
        return self.__jpdl32_DocumentRoot58

    @jpdl32_DocumentRoot58.setter
    def jpdl32_DocumentRoot58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot58", None)
        self.__jpdl32_DocumentRoot58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_StateType"):
                    opp_val = getattr(item, "jpdl32_StateType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_StateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_StateType"):
                    opp_val = getattr(item, "jpdl32_StateType", None)
                    
                    setattr(item, "jpdl32_StateType", self)
                    

    @property
    def jpdl32_DocumentRoot73(self):
        return self.__jpdl32_DocumentRoot73

    @jpdl32_DocumentRoot73.setter
    def jpdl32_DocumentRoot73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot73", None)
        self.__jpdl32_DocumentRoot73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_VariableType"):
                    opp_val = getattr(item, "jpdl32_VariableType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_VariableType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_VariableType"):
                    opp_val = getattr(item, "jpdl32_VariableType", None)
                    
                    setattr(item, "jpdl32_VariableType", self)
                    

    @property
    def jpdl32_DocumentRoot25(self):
        return self.__jpdl32_DocumentRoot25

    @jpdl32_DocumentRoot25.setter
    def jpdl32_DocumentRoot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot25", None)
        self.__jpdl32_DocumentRoot25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_CreateTimerType26"):
                    opp_val = getattr(item, "jpdl32_CreateTimerType26", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_CreateTimerType26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_CreateTimerType26"):
                    opp_val = getattr(item, "jpdl32_CreateTimerType26", None)
                    
                    setattr(item, "jpdl32_CreateTimerType26", self)
                    

    @property
    def jpdl32_DocumentRoot(self):
        return self.__jpdl32_DocumentRoot

    @jpdl32_DocumentRoot.setter
    def jpdl32_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DocumentRoot__jpdl32_DocumentRoot", None)
        self.__jpdl32_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EStringToStringMapEntry"):
                    opp_val = getattr(item, "jpdl32_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EStringToStringMapEntry"):
                    opp_val = getattr(item, "jpdl32_EStringToStringMapEntry", None)
                    
                    setattr(item, "jpdl32_EStringToStringMapEntry", self)
                    

class jpdl32_TransitionType:

    def __init__(self, group: str, description: str, name: str, to: str, jpdl32_TransitionType: "jpdl32_DecisionType" = None, jpdl32_TransitionType71: "jpdl32_DocumentRoot" = None, jpdl32_TransitionType115: "jpdl32_ForkType" = None, jpdl32_TransitionType127: "jpdl32_JoinType" = None, jpdl32_TransitionType139: "jpdl32_MailNodeType" = None, jpdl32_TransitionType166: "jpdl32_NodeType" = None, jpdl32_TransitionType243: "jpdl32_ProcessStateType" = None, jpdl32_TransitionType249: "jpdl32_StartStateType" = None, jpdl32_TransitionType267: "jpdl32_StateType" = None, jpdl32_TransitionType309: "jpdl32_SuperStateType" = None, jpdl32_TransitionType327: "jpdl32_TaskNodeType" = None, jpdl32_TransitionType360: set["jpdl32_ActionType"] = None, jpdl32_TransitionType363: set["jpdl32_ScriptType"] = None, jpdl32_TransitionType366: set["jpdl32_CreateTimerType"] = None, jpdl32_TransitionType358: set["jpdl32_ConditionType"] = None, jpdl32_TransitionType372: set["jpdl32_MailType"] = None, jpdl32_TransitionType375: set["jpdl32_ExceptionHandlerType"] = None, jpdl32_TransitionType369: set["jpdl32_CancelTimerType"] = None):
        self.group = group
        self.description = description
        self.name = name
        self.to = to
        self.jpdl32_TransitionType = jpdl32_TransitionType
        self.jpdl32_TransitionType71 = jpdl32_TransitionType71
        self.jpdl32_TransitionType115 = jpdl32_TransitionType115
        self.jpdl32_TransitionType127 = jpdl32_TransitionType127
        self.jpdl32_TransitionType139 = jpdl32_TransitionType139
        self.jpdl32_TransitionType166 = jpdl32_TransitionType166
        self.jpdl32_TransitionType243 = jpdl32_TransitionType243
        self.jpdl32_TransitionType249 = jpdl32_TransitionType249
        self.jpdl32_TransitionType267 = jpdl32_TransitionType267
        self.jpdl32_TransitionType309 = jpdl32_TransitionType309
        self.jpdl32_TransitionType327 = jpdl32_TransitionType327
        self.jpdl32_TransitionType360 = jpdl32_TransitionType360 if jpdl32_TransitionType360 is not None else set()
        self.jpdl32_TransitionType363 = jpdl32_TransitionType363 if jpdl32_TransitionType363 is not None else set()
        self.jpdl32_TransitionType366 = jpdl32_TransitionType366 if jpdl32_TransitionType366 is not None else set()
        self.jpdl32_TransitionType358 = jpdl32_TransitionType358 if jpdl32_TransitionType358 is not None else set()
        self.jpdl32_TransitionType372 = jpdl32_TransitionType372 if jpdl32_TransitionType372 is not None else set()
        self.jpdl32_TransitionType375 = jpdl32_TransitionType375 if jpdl32_TransitionType375 is not None else set()
        self.jpdl32_TransitionType369 = jpdl32_TransitionType369 if jpdl32_TransitionType369 is not None else set()
        
    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

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
    def jpdl32_TransitionType249(self):
        return self.__jpdl32_TransitionType249

    @jpdl32_TransitionType249.setter
    def jpdl32_TransitionType249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType249", None)
        self.__jpdl32_TransitionType249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_StartStateType248"):
                opp_val = getattr(old_value, "jpdl32_StartStateType248", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_StartStateType248"):
                opp_val = getattr(value, "jpdl32_StartStateType248", None)
                if opp_val is None:
                    setattr(value, "jpdl32_StartStateType248", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TransitionType372(self):
        return self.__jpdl32_TransitionType372

    @jpdl32_TransitionType372.setter
    def jpdl32_TransitionType372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType372", None)
        self.__jpdl32_TransitionType372 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_MailType373"):
                    opp_val = getattr(item, "jpdl32_MailType373", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_MailType373", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_MailType373"):
                    opp_val = getattr(item, "jpdl32_MailType373", None)
                    
                    setattr(item, "jpdl32_MailType373", self)
                    

    @property
    def jpdl32_TransitionType375(self):
        return self.__jpdl32_TransitionType375

    @jpdl32_TransitionType375.setter
    def jpdl32_TransitionType375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType375", None)
        self.__jpdl32_TransitionType375 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ExceptionHandlerType376"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType376", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ExceptionHandlerType376", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ExceptionHandlerType376"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType376", None)
                    
                    setattr(item, "jpdl32_ExceptionHandlerType376", self)
                    

    @property
    def jpdl32_TransitionType309(self):
        return self.__jpdl32_TransitionType309

    @jpdl32_TransitionType309.setter
    def jpdl32_TransitionType309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType309", None)
        self.__jpdl32_TransitionType309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SuperStateType308"):
                opp_val = getattr(old_value, "jpdl32_SuperStateType308", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SuperStateType308"):
                opp_val = getattr(value, "jpdl32_SuperStateType308", None)
                if opp_val is None:
                    setattr(value, "jpdl32_SuperStateType308", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TransitionType115(self):
        return self.__jpdl32_TransitionType115

    @jpdl32_TransitionType115.setter
    def jpdl32_TransitionType115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType115", None)
        self.__jpdl32_TransitionType115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ForkType114"):
                opp_val = getattr(old_value, "jpdl32_ForkType114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ForkType114"):
                opp_val = getattr(value, "jpdl32_ForkType114", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ForkType114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TransitionType(self):
        return self.__jpdl32_TransitionType

    @jpdl32_TransitionType.setter
    def jpdl32_TransitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType", None)
        self.__jpdl32_TransitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DecisionType9"):
                opp_val = getattr(old_value, "jpdl32_DecisionType9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DecisionType9"):
                opp_val = getattr(value, "jpdl32_DecisionType9", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DecisionType9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TransitionType166(self):
        return self.__jpdl32_TransitionType166

    @jpdl32_TransitionType166.setter
    def jpdl32_TransitionType166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType166", None)
        self.__jpdl32_TransitionType166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_NodeType165"):
                opp_val = getattr(old_value, "jpdl32_NodeType165", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_NodeType165"):
                opp_val = getattr(value, "jpdl32_NodeType165", None)
                if opp_val is None:
                    setattr(value, "jpdl32_NodeType165", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TransitionType369(self):
        return self.__jpdl32_TransitionType369

    @jpdl32_TransitionType369.setter
    def jpdl32_TransitionType369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType369", None)
        self.__jpdl32_TransitionType369 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_CancelTimerType370"):
                    opp_val = getattr(item, "jpdl32_CancelTimerType370", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_CancelTimerType370", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_CancelTimerType370"):
                    opp_val = getattr(item, "jpdl32_CancelTimerType370", None)
                    
                    setattr(item, "jpdl32_CancelTimerType370", self)
                    

    @property
    def jpdl32_TransitionType358(self):
        return self.__jpdl32_TransitionType358

    @jpdl32_TransitionType358.setter
    def jpdl32_TransitionType358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType358", None)
        self.__jpdl32_TransitionType358 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ConditionType"):
                    opp_val = getattr(item, "jpdl32_ConditionType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ConditionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ConditionType"):
                    opp_val = getattr(item, "jpdl32_ConditionType", None)
                    
                    setattr(item, "jpdl32_ConditionType", self)
                    

    @property
    def jpdl32_TransitionType127(self):
        return self.__jpdl32_TransitionType127

    @jpdl32_TransitionType127.setter
    def jpdl32_TransitionType127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType127", None)
        self.__jpdl32_TransitionType127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_JoinType126"):
                opp_val = getattr(old_value, "jpdl32_JoinType126", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_JoinType126"):
                opp_val = getattr(value, "jpdl32_JoinType126", None)
                if opp_val is None:
                    setattr(value, "jpdl32_JoinType126", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TransitionType360(self):
        return self.__jpdl32_TransitionType360

    @jpdl32_TransitionType360.setter
    def jpdl32_TransitionType360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType360", None)
        self.__jpdl32_TransitionType360 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ActionType361"):
                    opp_val = getattr(item, "jpdl32_ActionType361", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ActionType361", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ActionType361"):
                    opp_val = getattr(item, "jpdl32_ActionType361", None)
                    
                    setattr(item, "jpdl32_ActionType361", self)
                    

    @property
    def jpdl32_TransitionType243(self):
        return self.__jpdl32_TransitionType243

    @jpdl32_TransitionType243.setter
    def jpdl32_TransitionType243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType243", None)
        self.__jpdl32_TransitionType243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessStateType242"):
                opp_val = getattr(old_value, "jpdl32_ProcessStateType242", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessStateType242"):
                opp_val = getattr(value, "jpdl32_ProcessStateType242", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessStateType242", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TransitionType71(self):
        return self.__jpdl32_TransitionType71

    @jpdl32_TransitionType71.setter
    def jpdl32_TransitionType71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType71", None)
        self.__jpdl32_TransitionType71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot70"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot70"):
                opp_val = getattr(value, "jpdl32_DocumentRoot70", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TransitionType366(self):
        return self.__jpdl32_TransitionType366

    @jpdl32_TransitionType366.setter
    def jpdl32_TransitionType366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType366", None)
        self.__jpdl32_TransitionType366 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_CreateTimerType367"):
                    opp_val = getattr(item, "jpdl32_CreateTimerType367", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_CreateTimerType367", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_CreateTimerType367"):
                    opp_val = getattr(item, "jpdl32_CreateTimerType367", None)
                    
                    setattr(item, "jpdl32_CreateTimerType367", self)
                    

    @property
    def jpdl32_TransitionType267(self):
        return self.__jpdl32_TransitionType267

    @jpdl32_TransitionType267.setter
    def jpdl32_TransitionType267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType267", None)
        self.__jpdl32_TransitionType267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_StateType266"):
                opp_val = getattr(old_value, "jpdl32_StateType266", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_StateType266"):
                opp_val = getattr(value, "jpdl32_StateType266", None)
                if opp_val is None:
                    setattr(value, "jpdl32_StateType266", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TransitionType363(self):
        return self.__jpdl32_TransitionType363

    @jpdl32_TransitionType363.setter
    def jpdl32_TransitionType363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType363", None)
        self.__jpdl32_TransitionType363 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ScriptType364"):
                    opp_val = getattr(item, "jpdl32_ScriptType364", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ScriptType364", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ScriptType364"):
                    opp_val = getattr(item, "jpdl32_ScriptType364", None)
                    
                    setattr(item, "jpdl32_ScriptType364", self)
                    

    @property
    def jpdl32_TransitionType139(self):
        return self.__jpdl32_TransitionType139

    @jpdl32_TransitionType139.setter
    def jpdl32_TransitionType139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType139", None)
        self.__jpdl32_TransitionType139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_MailNodeType138"):
                opp_val = getattr(old_value, "jpdl32_MailNodeType138", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_MailNodeType138"):
                opp_val = getattr(value, "jpdl32_MailNodeType138", None)
                if opp_val is None:
                    setattr(value, "jpdl32_MailNodeType138", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_TransitionType327(self):
        return self.__jpdl32_TransitionType327

    @jpdl32_TransitionType327.setter
    def jpdl32_TransitionType327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_TransitionType__jpdl32_TransitionType327", None)
        self.__jpdl32_TransitionType327 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TaskNodeType326"):
                opp_val = getattr(old_value, "jpdl32_TaskNodeType326", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TaskNodeType326"):
                opp_val = getattr(value, "jpdl32_TaskNodeType326", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TaskNodeType326", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_ExceptionHandlerType:

    def __init__(self, group: str, exceptionClass: str, jpdl32_ExceptionHandlerType: "jpdl32_DecisionType" = None, jpdl32_ExceptionHandlerType37: "jpdl32_DocumentRoot" = None, jpdl32_ExceptionHandlerType79: "jpdl32_EndStateType" = None, jpdl32_ExceptionHandlerType99: set["jpdl32_ScriptType"] = None, jpdl32_ExceptionHandlerType96: set["jpdl32_ActionType"] = None, jpdl32_ExceptionHandlerType109: "jpdl32_ForkType" = None, jpdl32_ExceptionHandlerType121: "jpdl32_JoinType" = None, jpdl32_ExceptionHandlerType133: "jpdl32_MailNodeType" = None, jpdl32_ExceptionHandlerType160: "jpdl32_NodeType" = None, jpdl32_ExceptionHandlerType223: "jpdl32_ProcessDefinitionType" = None, jpdl32_ExceptionHandlerType237: "jpdl32_ProcessStateType" = None, jpdl32_ExceptionHandlerType255: "jpdl32_StartStateType" = None, jpdl32_ExceptionHandlerType261: "jpdl32_StateType" = None, jpdl32_ExceptionHandlerType303: "jpdl32_SuperStateType" = None, jpdl32_ExceptionHandlerType321: "jpdl32_TaskNodeType" = None, jpdl32_ExceptionHandlerType376: "jpdl32_TransitionType" = None):
        self.group = group
        self.exceptionClass = exceptionClass
        self.jpdl32_ExceptionHandlerType = jpdl32_ExceptionHandlerType
        self.jpdl32_ExceptionHandlerType37 = jpdl32_ExceptionHandlerType37
        self.jpdl32_ExceptionHandlerType79 = jpdl32_ExceptionHandlerType79
        self.jpdl32_ExceptionHandlerType99 = jpdl32_ExceptionHandlerType99 if jpdl32_ExceptionHandlerType99 is not None else set()
        self.jpdl32_ExceptionHandlerType96 = jpdl32_ExceptionHandlerType96 if jpdl32_ExceptionHandlerType96 is not None else set()
        self.jpdl32_ExceptionHandlerType109 = jpdl32_ExceptionHandlerType109
        self.jpdl32_ExceptionHandlerType121 = jpdl32_ExceptionHandlerType121
        self.jpdl32_ExceptionHandlerType133 = jpdl32_ExceptionHandlerType133
        self.jpdl32_ExceptionHandlerType160 = jpdl32_ExceptionHandlerType160
        self.jpdl32_ExceptionHandlerType223 = jpdl32_ExceptionHandlerType223
        self.jpdl32_ExceptionHandlerType237 = jpdl32_ExceptionHandlerType237
        self.jpdl32_ExceptionHandlerType255 = jpdl32_ExceptionHandlerType255
        self.jpdl32_ExceptionHandlerType261 = jpdl32_ExceptionHandlerType261
        self.jpdl32_ExceptionHandlerType303 = jpdl32_ExceptionHandlerType303
        self.jpdl32_ExceptionHandlerType321 = jpdl32_ExceptionHandlerType321
        self.jpdl32_ExceptionHandlerType376 = jpdl32_ExceptionHandlerType376
        
    @property
    def exceptionClass(self) -> str:
        return self.__exceptionClass

    @exceptionClass.setter
    def exceptionClass(self, exceptionClass: str):
        self.__exceptionClass = exceptionClass

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def jpdl32_ExceptionHandlerType109(self):
        return self.__jpdl32_ExceptionHandlerType109

    @jpdl32_ExceptionHandlerType109.setter
    def jpdl32_ExceptionHandlerType109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType109", None)
        self.__jpdl32_ExceptionHandlerType109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ForkType108"):
                opp_val = getattr(old_value, "jpdl32_ForkType108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ForkType108"):
                opp_val = getattr(value, "jpdl32_ForkType108", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ForkType108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ExceptionHandlerType121(self):
        return self.__jpdl32_ExceptionHandlerType121

    @jpdl32_ExceptionHandlerType121.setter
    def jpdl32_ExceptionHandlerType121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType121", None)
        self.__jpdl32_ExceptionHandlerType121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_JoinType120"):
                opp_val = getattr(old_value, "jpdl32_JoinType120", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_JoinType120"):
                opp_val = getattr(value, "jpdl32_JoinType120", None)
                if opp_val is None:
                    setattr(value, "jpdl32_JoinType120", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ExceptionHandlerType237(self):
        return self.__jpdl32_ExceptionHandlerType237

    @jpdl32_ExceptionHandlerType237.setter
    def jpdl32_ExceptionHandlerType237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType237", None)
        self.__jpdl32_ExceptionHandlerType237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessStateType236"):
                opp_val = getattr(old_value, "jpdl32_ProcessStateType236", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessStateType236"):
                opp_val = getattr(value, "jpdl32_ProcessStateType236", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessStateType236", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ExceptionHandlerType79(self):
        return self.__jpdl32_ExceptionHandlerType79

    @jpdl32_ExceptionHandlerType79.setter
    def jpdl32_ExceptionHandlerType79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType79", None)
        self.__jpdl32_ExceptionHandlerType79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_EndStateType78"):
                opp_val = getattr(old_value, "jpdl32_EndStateType78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_EndStateType78"):
                opp_val = getattr(value, "jpdl32_EndStateType78", None)
                if opp_val is None:
                    setattr(value, "jpdl32_EndStateType78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ExceptionHandlerType96(self):
        return self.__jpdl32_ExceptionHandlerType96

    @jpdl32_ExceptionHandlerType96.setter
    def jpdl32_ExceptionHandlerType96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType96", None)
        self.__jpdl32_ExceptionHandlerType96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ActionType97"):
                    opp_val = getattr(item, "jpdl32_ActionType97", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ActionType97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ActionType97"):
                    opp_val = getattr(item, "jpdl32_ActionType97", None)
                    
                    setattr(item, "jpdl32_ActionType97", self)
                    

    @property
    def jpdl32_ExceptionHandlerType321(self):
        return self.__jpdl32_ExceptionHandlerType321

    @jpdl32_ExceptionHandlerType321.setter
    def jpdl32_ExceptionHandlerType321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType321", None)
        self.__jpdl32_ExceptionHandlerType321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TaskNodeType320"):
                opp_val = getattr(old_value, "jpdl32_TaskNodeType320", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TaskNodeType320"):
                opp_val = getattr(value, "jpdl32_TaskNodeType320", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TaskNodeType320", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ExceptionHandlerType261(self):
        return self.__jpdl32_ExceptionHandlerType261

    @jpdl32_ExceptionHandlerType261.setter
    def jpdl32_ExceptionHandlerType261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType261", None)
        self.__jpdl32_ExceptionHandlerType261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_StateType260"):
                opp_val = getattr(old_value, "jpdl32_StateType260", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_StateType260"):
                opp_val = getattr(value, "jpdl32_StateType260", None)
                if opp_val is None:
                    setattr(value, "jpdl32_StateType260", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ExceptionHandlerType37(self):
        return self.__jpdl32_ExceptionHandlerType37

    @jpdl32_ExceptionHandlerType37.setter
    def jpdl32_ExceptionHandlerType37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType37", None)
        self.__jpdl32_ExceptionHandlerType37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot36"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot36"):
                opp_val = getattr(value, "jpdl32_DocumentRoot36", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ExceptionHandlerType133(self):
        return self.__jpdl32_ExceptionHandlerType133

    @jpdl32_ExceptionHandlerType133.setter
    def jpdl32_ExceptionHandlerType133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType133", None)
        self.__jpdl32_ExceptionHandlerType133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_MailNodeType132"):
                opp_val = getattr(old_value, "jpdl32_MailNodeType132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_MailNodeType132"):
                opp_val = getattr(value, "jpdl32_MailNodeType132", None)
                if opp_val is None:
                    setattr(value, "jpdl32_MailNodeType132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ExceptionHandlerType376(self):
        return self.__jpdl32_ExceptionHandlerType376

    @jpdl32_ExceptionHandlerType376.setter
    def jpdl32_ExceptionHandlerType376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType376", None)
        self.__jpdl32_ExceptionHandlerType376 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TransitionType375"):
                opp_val = getattr(old_value, "jpdl32_TransitionType375", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TransitionType375"):
                opp_val = getattr(value, "jpdl32_TransitionType375", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TransitionType375", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ExceptionHandlerType303(self):
        return self.__jpdl32_ExceptionHandlerType303

    @jpdl32_ExceptionHandlerType303.setter
    def jpdl32_ExceptionHandlerType303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType303", None)
        self.__jpdl32_ExceptionHandlerType303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SuperStateType302"):
                opp_val = getattr(old_value, "jpdl32_SuperStateType302", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SuperStateType302"):
                opp_val = getattr(value, "jpdl32_SuperStateType302", None)
                if opp_val is None:
                    setattr(value, "jpdl32_SuperStateType302", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ExceptionHandlerType255(self):
        return self.__jpdl32_ExceptionHandlerType255

    @jpdl32_ExceptionHandlerType255.setter
    def jpdl32_ExceptionHandlerType255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType255", None)
        self.__jpdl32_ExceptionHandlerType255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_StartStateType254"):
                opp_val = getattr(old_value, "jpdl32_StartStateType254", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_StartStateType254"):
                opp_val = getattr(value, "jpdl32_StartStateType254", None)
                if opp_val is None:
                    setattr(value, "jpdl32_StartStateType254", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ExceptionHandlerType(self):
        return self.__jpdl32_ExceptionHandlerType

    @jpdl32_ExceptionHandlerType.setter
    def jpdl32_ExceptionHandlerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType", None)
        self.__jpdl32_ExceptionHandlerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DecisionType7"):
                opp_val = getattr(old_value, "jpdl32_DecisionType7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DecisionType7"):
                opp_val = getattr(value, "jpdl32_DecisionType7", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DecisionType7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ExceptionHandlerType223(self):
        return self.__jpdl32_ExceptionHandlerType223

    @jpdl32_ExceptionHandlerType223.setter
    def jpdl32_ExceptionHandlerType223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType223", None)
        self.__jpdl32_ExceptionHandlerType223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType222"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType222", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType222"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType222", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType222", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ExceptionHandlerType160(self):
        return self.__jpdl32_ExceptionHandlerType160

    @jpdl32_ExceptionHandlerType160.setter
    def jpdl32_ExceptionHandlerType160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType160", None)
        self.__jpdl32_ExceptionHandlerType160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_NodeType159"):
                opp_val = getattr(old_value, "jpdl32_NodeType159", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_NodeType159"):
                opp_val = getattr(value, "jpdl32_NodeType159", None)
                if opp_val is None:
                    setattr(value, "jpdl32_NodeType159", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ExceptionHandlerType99(self):
        return self.__jpdl32_ExceptionHandlerType99

    @jpdl32_ExceptionHandlerType99.setter
    def jpdl32_ExceptionHandlerType99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ExceptionHandlerType__jpdl32_ExceptionHandlerType99", None)
        self.__jpdl32_ExceptionHandlerType99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ScriptType100"):
                    opp_val = getattr(item, "jpdl32_ScriptType100", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ScriptType100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ScriptType100"):
                    opp_val = getattr(item, "jpdl32_ScriptType100", None)
                    
                    setattr(item, "jpdl32_ScriptType100", self)
                    

class jpdl32_EventType:

    def __init__(self, actionElements: str, type: str, jpdl32_EventType: "jpdl32_DecisionType" = None, jpdl32_EventType34: "jpdl32_DocumentRoot" = None, jpdl32_EventType76: "jpdl32_EndStateType" = None, jpdl32_EventType81: set["jpdl32_ActionType"] = None, jpdl32_EventType93: set["jpdl32_MailType"] = None, jpdl32_EventType84: set["jpdl32_ScriptType"] = None, jpdl32_EventType87: set["jpdl32_CreateTimerType"] = None, jpdl32_EventType90: set["jpdl32_CancelTimerType"] = None, jpdl32_EventType106: "jpdl32_ForkType" = None, jpdl32_EventType118: "jpdl32_JoinType" = None, jpdl32_EventType130: "jpdl32_MailNodeType" = None, jpdl32_EventType157: "jpdl32_NodeType" = None, jpdl32_EventType220: "jpdl32_ProcessDefinitionType" = None, jpdl32_EventType234: "jpdl32_ProcessStateType" = None, jpdl32_EventType252: "jpdl32_StartStateType" = None, jpdl32_EventType258: "jpdl32_StateType" = None, jpdl32_EventType300: "jpdl32_SuperStateType" = None, jpdl32_EventType318: "jpdl32_TaskNodeType" = None, jpdl32_EventType336: "jpdl32_TaskType" = None):
        self.actionElements = actionElements
        self.type = type
        self.jpdl32_EventType = jpdl32_EventType
        self.jpdl32_EventType34 = jpdl32_EventType34
        self.jpdl32_EventType76 = jpdl32_EventType76
        self.jpdl32_EventType81 = jpdl32_EventType81 if jpdl32_EventType81 is not None else set()
        self.jpdl32_EventType93 = jpdl32_EventType93 if jpdl32_EventType93 is not None else set()
        self.jpdl32_EventType84 = jpdl32_EventType84 if jpdl32_EventType84 is not None else set()
        self.jpdl32_EventType87 = jpdl32_EventType87 if jpdl32_EventType87 is not None else set()
        self.jpdl32_EventType90 = jpdl32_EventType90 if jpdl32_EventType90 is not None else set()
        self.jpdl32_EventType106 = jpdl32_EventType106
        self.jpdl32_EventType118 = jpdl32_EventType118
        self.jpdl32_EventType130 = jpdl32_EventType130
        self.jpdl32_EventType157 = jpdl32_EventType157
        self.jpdl32_EventType220 = jpdl32_EventType220
        self.jpdl32_EventType234 = jpdl32_EventType234
        self.jpdl32_EventType252 = jpdl32_EventType252
        self.jpdl32_EventType258 = jpdl32_EventType258
        self.jpdl32_EventType300 = jpdl32_EventType300
        self.jpdl32_EventType318 = jpdl32_EventType318
        self.jpdl32_EventType336 = jpdl32_EventType336
        
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
    def jpdl32_EventType336(self):
        return self.__jpdl32_EventType336

    @jpdl32_EventType336.setter
    def jpdl32_EventType336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType336", None)
        self.__jpdl32_EventType336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TaskType335"):
                opp_val = getattr(old_value, "jpdl32_TaskType335", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TaskType335"):
                opp_val = getattr(value, "jpdl32_TaskType335", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TaskType335", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EventType93(self):
        return self.__jpdl32_EventType93

    @jpdl32_EventType93.setter
    def jpdl32_EventType93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType93", None)
        self.__jpdl32_EventType93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_MailType94"):
                    opp_val = getattr(item, "jpdl32_MailType94", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_MailType94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_MailType94"):
                    opp_val = getattr(item, "jpdl32_MailType94", None)
                    
                    setattr(item, "jpdl32_MailType94", self)
                    

    @property
    def jpdl32_EventType90(self):
        return self.__jpdl32_EventType90

    @jpdl32_EventType90.setter
    def jpdl32_EventType90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType90", None)
        self.__jpdl32_EventType90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_CancelTimerType91"):
                    opp_val = getattr(item, "jpdl32_CancelTimerType91", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_CancelTimerType91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_CancelTimerType91"):
                    opp_val = getattr(item, "jpdl32_CancelTimerType91", None)
                    
                    setattr(item, "jpdl32_CancelTimerType91", self)
                    

    @property
    def jpdl32_EventType106(self):
        return self.__jpdl32_EventType106

    @jpdl32_EventType106.setter
    def jpdl32_EventType106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType106", None)
        self.__jpdl32_EventType106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ForkType105"):
                opp_val = getattr(old_value, "jpdl32_ForkType105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ForkType105"):
                opp_val = getattr(value, "jpdl32_ForkType105", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ForkType105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EventType318(self):
        return self.__jpdl32_EventType318

    @jpdl32_EventType318.setter
    def jpdl32_EventType318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType318", None)
        self.__jpdl32_EventType318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TaskNodeType317"):
                opp_val = getattr(old_value, "jpdl32_TaskNodeType317", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TaskNodeType317"):
                opp_val = getattr(value, "jpdl32_TaskNodeType317", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TaskNodeType317", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EventType87(self):
        return self.__jpdl32_EventType87

    @jpdl32_EventType87.setter
    def jpdl32_EventType87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType87", None)
        self.__jpdl32_EventType87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_CreateTimerType88"):
                    opp_val = getattr(item, "jpdl32_CreateTimerType88", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_CreateTimerType88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_CreateTimerType88"):
                    opp_val = getattr(item, "jpdl32_CreateTimerType88", None)
                    
                    setattr(item, "jpdl32_CreateTimerType88", self)
                    

    @property
    def jpdl32_EventType34(self):
        return self.__jpdl32_EventType34

    @jpdl32_EventType34.setter
    def jpdl32_EventType34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType34", None)
        self.__jpdl32_EventType34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot33"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot33"):
                opp_val = getattr(value, "jpdl32_DocumentRoot33", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EventType(self):
        return self.__jpdl32_EventType

    @jpdl32_EventType.setter
    def jpdl32_EventType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType", None)
        self.__jpdl32_EventType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DecisionType5"):
                opp_val = getattr(old_value, "jpdl32_DecisionType5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DecisionType5"):
                opp_val = getattr(value, "jpdl32_DecisionType5", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DecisionType5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EventType118(self):
        return self.__jpdl32_EventType118

    @jpdl32_EventType118.setter
    def jpdl32_EventType118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType118", None)
        self.__jpdl32_EventType118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_JoinType117"):
                opp_val = getattr(old_value, "jpdl32_JoinType117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_JoinType117"):
                opp_val = getattr(value, "jpdl32_JoinType117", None)
                if opp_val is None:
                    setattr(value, "jpdl32_JoinType117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EventType258(self):
        return self.__jpdl32_EventType258

    @jpdl32_EventType258.setter
    def jpdl32_EventType258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType258", None)
        self.__jpdl32_EventType258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_StateType257"):
                opp_val = getattr(old_value, "jpdl32_StateType257", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_StateType257"):
                opp_val = getattr(value, "jpdl32_StateType257", None)
                if opp_val is None:
                    setattr(value, "jpdl32_StateType257", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EventType76(self):
        return self.__jpdl32_EventType76

    @jpdl32_EventType76.setter
    def jpdl32_EventType76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType76", None)
        self.__jpdl32_EventType76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_EndStateType75"):
                opp_val = getattr(old_value, "jpdl32_EndStateType75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_EndStateType75"):
                opp_val = getattr(value, "jpdl32_EndStateType75", None)
                if opp_val is None:
                    setattr(value, "jpdl32_EndStateType75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EventType252(self):
        return self.__jpdl32_EventType252

    @jpdl32_EventType252.setter
    def jpdl32_EventType252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType252", None)
        self.__jpdl32_EventType252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_StartStateType251"):
                opp_val = getattr(old_value, "jpdl32_StartStateType251", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_StartStateType251"):
                opp_val = getattr(value, "jpdl32_StartStateType251", None)
                if opp_val is None:
                    setattr(value, "jpdl32_StartStateType251", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EventType157(self):
        return self.__jpdl32_EventType157

    @jpdl32_EventType157.setter
    def jpdl32_EventType157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType157", None)
        self.__jpdl32_EventType157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_NodeType156"):
                opp_val = getattr(old_value, "jpdl32_NodeType156", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_NodeType156"):
                opp_val = getattr(value, "jpdl32_NodeType156", None)
                if opp_val is None:
                    setattr(value, "jpdl32_NodeType156", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EventType300(self):
        return self.__jpdl32_EventType300

    @jpdl32_EventType300.setter
    def jpdl32_EventType300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType300", None)
        self.__jpdl32_EventType300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SuperStateType299"):
                opp_val = getattr(old_value, "jpdl32_SuperStateType299", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SuperStateType299"):
                opp_val = getattr(value, "jpdl32_SuperStateType299", None)
                if opp_val is None:
                    setattr(value, "jpdl32_SuperStateType299", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EventType130(self):
        return self.__jpdl32_EventType130

    @jpdl32_EventType130.setter
    def jpdl32_EventType130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType130", None)
        self.__jpdl32_EventType130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_MailNodeType129"):
                opp_val = getattr(old_value, "jpdl32_MailNodeType129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_MailNodeType129"):
                opp_val = getattr(value, "jpdl32_MailNodeType129", None)
                if opp_val is None:
                    setattr(value, "jpdl32_MailNodeType129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EventType84(self):
        return self.__jpdl32_EventType84

    @jpdl32_EventType84.setter
    def jpdl32_EventType84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType84", None)
        self.__jpdl32_EventType84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ScriptType85"):
                    opp_val = getattr(item, "jpdl32_ScriptType85", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ScriptType85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ScriptType85"):
                    opp_val = getattr(item, "jpdl32_ScriptType85", None)
                    
                    setattr(item, "jpdl32_ScriptType85", self)
                    

    @property
    def jpdl32_EventType234(self):
        return self.__jpdl32_EventType234

    @jpdl32_EventType234.setter
    def jpdl32_EventType234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType234", None)
        self.__jpdl32_EventType234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessStateType233"):
                opp_val = getattr(old_value, "jpdl32_ProcessStateType233", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessStateType233"):
                opp_val = getattr(value, "jpdl32_ProcessStateType233", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessStateType233", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EventType220(self):
        return self.__jpdl32_EventType220

    @jpdl32_EventType220.setter
    def jpdl32_EventType220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType220", None)
        self.__jpdl32_EventType220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType219"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType219", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType219"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType219", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType219", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_EventType81(self):
        return self.__jpdl32_EventType81

    @jpdl32_EventType81.setter
    def jpdl32_EventType81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_EventType__jpdl32_EventType81", None)
        self.__jpdl32_EventType81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ActionType82"):
                    opp_val = getattr(item, "jpdl32_ActionType82", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ActionType82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ActionType82"):
                    opp_val = getattr(item, "jpdl32_ActionType82", None)
                    
                    setattr(item, "jpdl32_ActionType82", self)
                    

class jpdl32_Delegation:

    def __init__(self, mixed: str, any: str, class: str, configType: str, jpdl32_Delegation: "jpdl32_DecisionType" = None, jpdl32_Delegation23: "jpdl32_DocumentRoot" = None, jpdl32_Delegation333: "jpdl32_TaskType" = None):
        self.mixed = mixed
        self.any = any
        self.class = class
        self.configType = configType
        self.jpdl32_Delegation = jpdl32_Delegation
        self.jpdl32_Delegation23 = jpdl32_Delegation23
        self.jpdl32_Delegation333 = jpdl32_Delegation333
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def configType(self) -> str:
        return self.__configType

    @configType.setter
    def configType(self, configType: str):
        self.__configType = configType

    @property
    def jpdl32_Delegation(self):
        return self.__jpdl32_Delegation

    @jpdl32_Delegation.setter
    def jpdl32_Delegation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_Delegation__jpdl32_Delegation", None)
        self.__jpdl32_Delegation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DecisionType"):
                opp_val = getattr(old_value, "jpdl32_DecisionType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DecisionType"):
                opp_val = getattr(value, "jpdl32_DecisionType", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DecisionType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_Delegation333(self):
        return self.__jpdl32_Delegation333

    @jpdl32_Delegation333.setter
    def jpdl32_Delegation333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_Delegation__jpdl32_Delegation333", None)
        self.__jpdl32_Delegation333 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TaskType332"):
                opp_val = getattr(old_value, "jpdl32_TaskType332", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TaskType332"):
                opp_val = getattr(value, "jpdl32_TaskType332", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TaskType332", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_Delegation23(self):
        return self.__jpdl32_Delegation23

    @jpdl32_Delegation23.setter
    def jpdl32_Delegation23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_Delegation__jpdl32_Delegation23", None)
        self.__jpdl32_Delegation23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot22"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot22"):
                opp_val = getattr(value, "jpdl32_DocumentRoot22", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_DecisionType:

    def __init__(self, group: str, description: str, name: str, async: str, expression: str, jpdl32_DecisionType: set["jpdl32_Delegation"] = None, jpdl32_DecisionType5: set["jpdl32_EventType"] = None, jpdl32_DecisionType7: set["jpdl32_ExceptionHandlerType"] = None, jpdl32_DecisionType9: set["jpdl32_TransitionType"] = None, jpdl32_DecisionType29: "jpdl32_DocumentRoot" = None, jpdl32_DecisionType196: "jpdl32_ProcessDefinitionType" = None, jpdl32_DecisionType291: "jpdl32_SuperStateType" = None):
        self.group = group
        self.description = description
        self.name = name
        self.async = async
        self.expression = expression
        self.jpdl32_DecisionType = jpdl32_DecisionType if jpdl32_DecisionType is not None else set()
        self.jpdl32_DecisionType5 = jpdl32_DecisionType5 if jpdl32_DecisionType5 is not None else set()
        self.jpdl32_DecisionType7 = jpdl32_DecisionType7 if jpdl32_DecisionType7 is not None else set()
        self.jpdl32_DecisionType9 = jpdl32_DecisionType9 if jpdl32_DecisionType9 is not None else set()
        self.jpdl32_DecisionType29 = jpdl32_DecisionType29
        self.jpdl32_DecisionType196 = jpdl32_DecisionType196
        self.jpdl32_DecisionType291 = jpdl32_DecisionType291
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def jpdl32_DecisionType7(self):
        return self.__jpdl32_DecisionType7

    @jpdl32_DecisionType7.setter
    def jpdl32_DecisionType7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DecisionType__jpdl32_DecisionType7", None)
        self.__jpdl32_DecisionType7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_ExceptionHandlerType"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_ExceptionHandlerType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_ExceptionHandlerType"):
                    opp_val = getattr(item, "jpdl32_ExceptionHandlerType", None)
                    
                    setattr(item, "jpdl32_ExceptionHandlerType", self)
                    

    @property
    def jpdl32_DecisionType196(self):
        return self.__jpdl32_DecisionType196

    @jpdl32_DecisionType196.setter
    def jpdl32_DecisionType196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DecisionType__jpdl32_DecisionType196", None)
        self.__jpdl32_DecisionType196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType195"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType195", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType195"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType195", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType195", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_DecisionType(self):
        return self.__jpdl32_DecisionType

    @jpdl32_DecisionType.setter
    def jpdl32_DecisionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DecisionType__jpdl32_DecisionType", None)
        self.__jpdl32_DecisionType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_Delegation"):
                    opp_val = getattr(item, "jpdl32_Delegation", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_Delegation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_Delegation"):
                    opp_val = getattr(item, "jpdl32_Delegation", None)
                    
                    setattr(item, "jpdl32_Delegation", self)
                    

    @property
    def jpdl32_DecisionType9(self):
        return self.__jpdl32_DecisionType9

    @jpdl32_DecisionType9.setter
    def jpdl32_DecisionType9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DecisionType__jpdl32_DecisionType9", None)
        self.__jpdl32_DecisionType9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_TransitionType"):
                    opp_val = getattr(item, "jpdl32_TransitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_TransitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_TransitionType"):
                    opp_val = getattr(item, "jpdl32_TransitionType", None)
                    
                    setattr(item, "jpdl32_TransitionType", self)
                    

    @property
    def jpdl32_DecisionType29(self):
        return self.__jpdl32_DecisionType29

    @jpdl32_DecisionType29.setter
    def jpdl32_DecisionType29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DecisionType__jpdl32_DecisionType29", None)
        self.__jpdl32_DecisionType29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot28"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot28"):
                opp_val = getattr(value, "jpdl32_DocumentRoot28", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_DecisionType5(self):
        return self.__jpdl32_DecisionType5

    @jpdl32_DecisionType5.setter
    def jpdl32_DecisionType5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DecisionType__jpdl32_DecisionType5", None)
        self.__jpdl32_DecisionType5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl32_EventType"):
                    opp_val = getattr(item, "jpdl32_EventType", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl32_EventType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl32_EventType"):
                    opp_val = getattr(item, "jpdl32_EventType", None)
                    
                    setattr(item, "jpdl32_EventType", self)
                    

    @property
    def jpdl32_DecisionType291(self):
        return self.__jpdl32_DecisionType291

    @jpdl32_DecisionType291.setter
    def jpdl32_DecisionType291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_DecisionType__jpdl32_DecisionType291", None)
        self.__jpdl32_DecisionType291 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SuperStateType290"):
                opp_val = getattr(old_value, "jpdl32_SuperStateType290", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SuperStateType290"):
                opp_val = getattr(value, "jpdl32_SuperStateType290", None)
                if opp_val is None:
                    setattr(value, "jpdl32_SuperStateType290", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_ConditionType:

    def __init__(self, mixed: str, group: str, any: str, expression: str, jpdl32_ConditionType: "jpdl32_TransitionType" = None):
        self.mixed = mixed
        self.group = group
        self.any = any
        self.expression = expression
        self.jpdl32_ConditionType = jpdl32_ConditionType
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def jpdl32_ConditionType(self):
        return self.__jpdl32_ConditionType

    @jpdl32_ConditionType.setter
    def jpdl32_ConditionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ConditionType__jpdl32_ConditionType", None)
        self.__jpdl32_ConditionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TransitionType358"):
                opp_val = getattr(old_value, "jpdl32_TransitionType358", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TransitionType358"):
                opp_val = getattr(value, "jpdl32_TransitionType358", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TransitionType358", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_CancelTimerType:

    def __init__(self, name: str, jpdl32_CancelTimerType: "jpdl32_DocumentRoot" = None, jpdl32_CancelTimerType91: "jpdl32_EventType" = None, jpdl32_CancelTimerType151: "jpdl32_NodeType" = None, jpdl32_CancelTimerType214: "jpdl32_ProcessDefinitionType" = None, jpdl32_CancelTimerType353: "jpdl32_TimerType" = None, jpdl32_CancelTimerType370: "jpdl32_TransitionType" = None):
        self.name = name
        self.jpdl32_CancelTimerType = jpdl32_CancelTimerType
        self.jpdl32_CancelTimerType91 = jpdl32_CancelTimerType91
        self.jpdl32_CancelTimerType151 = jpdl32_CancelTimerType151
        self.jpdl32_CancelTimerType214 = jpdl32_CancelTimerType214
        self.jpdl32_CancelTimerType353 = jpdl32_CancelTimerType353
        self.jpdl32_CancelTimerType370 = jpdl32_CancelTimerType370
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl32_CancelTimerType151(self):
        return self.__jpdl32_CancelTimerType151

    @jpdl32_CancelTimerType151.setter
    def jpdl32_CancelTimerType151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_CancelTimerType__jpdl32_CancelTimerType151", None)
        self.__jpdl32_CancelTimerType151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_NodeType150"):
                opp_val = getattr(old_value, "jpdl32_NodeType150", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_NodeType150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_NodeType150"):
                opp_val = getattr(value, "jpdl32_NodeType150", None)
                setattr(value, "jpdl32_NodeType150", self)

    @property
    def jpdl32_CancelTimerType(self):
        return self.__jpdl32_CancelTimerType

    @jpdl32_CancelTimerType.setter
    def jpdl32_CancelTimerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_CancelTimerType__jpdl32_CancelTimerType", None)
        self.__jpdl32_CancelTimerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot20"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot20"):
                opp_val = getattr(value, "jpdl32_DocumentRoot20", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_CancelTimerType214(self):
        return self.__jpdl32_CancelTimerType214

    @jpdl32_CancelTimerType214.setter
    def jpdl32_CancelTimerType214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_CancelTimerType__jpdl32_CancelTimerType214", None)
        self.__jpdl32_CancelTimerType214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType213"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType213", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType213"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType213", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType213", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_CancelTimerType370(self):
        return self.__jpdl32_CancelTimerType370

    @jpdl32_CancelTimerType370.setter
    def jpdl32_CancelTimerType370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_CancelTimerType__jpdl32_CancelTimerType370", None)
        self.__jpdl32_CancelTimerType370 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TransitionType369"):
                opp_val = getattr(old_value, "jpdl32_TransitionType369", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TransitionType369"):
                opp_val = getattr(value, "jpdl32_TransitionType369", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TransitionType369", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_CancelTimerType353(self):
        return self.__jpdl32_CancelTimerType353

    @jpdl32_CancelTimerType353.setter
    def jpdl32_CancelTimerType353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_CancelTimerType__jpdl32_CancelTimerType353", None)
        self.__jpdl32_CancelTimerType353 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TimerType352"):
                opp_val = getattr(old_value, "jpdl32_TimerType352", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_TimerType352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TimerType352"):
                opp_val = getattr(value, "jpdl32_TimerType352", None)
                setattr(value, "jpdl32_TimerType352", self)

    @property
    def jpdl32_CancelTimerType91(self):
        return self.__jpdl32_CancelTimerType91

    @jpdl32_CancelTimerType91.setter
    def jpdl32_CancelTimerType91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_CancelTimerType__jpdl32_CancelTimerType91", None)
        self.__jpdl32_CancelTimerType91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_EventType90"):
                opp_val = getattr(old_value, "jpdl32_EventType90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_EventType90"):
                opp_val = getattr(value, "jpdl32_EventType90", None)
                if opp_val is None:
                    setattr(value, "jpdl32_EventType90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_ScriptType:

    def __init__(self, acceptPropagatedEvents: str, mixed: str, any: str, name: str, jpdl32_ScriptType: "jpdl32_CreateTimerType" = None, jpdl32_ScriptType54: "jpdl32_DocumentRoot" = None, jpdl32_ScriptType85: "jpdl32_EventType" = None, jpdl32_ScriptType100: "jpdl32_ExceptionHandlerType" = None, jpdl32_ScriptType103: "jpdl32_ForkType" = None, jpdl32_ScriptType145: "jpdl32_NodeType" = None, jpdl32_ScriptType208: "jpdl32_ProcessDefinitionType" = None, jpdl32_ScriptType347: "jpdl32_TimerType" = None, jpdl32_ScriptType364: "jpdl32_TransitionType" = None):
        self.acceptPropagatedEvents = acceptPropagatedEvents
        self.mixed = mixed
        self.any = any
        self.name = name
        self.jpdl32_ScriptType = jpdl32_ScriptType
        self.jpdl32_ScriptType54 = jpdl32_ScriptType54
        self.jpdl32_ScriptType85 = jpdl32_ScriptType85
        self.jpdl32_ScriptType100 = jpdl32_ScriptType100
        self.jpdl32_ScriptType103 = jpdl32_ScriptType103
        self.jpdl32_ScriptType145 = jpdl32_ScriptType145
        self.jpdl32_ScriptType208 = jpdl32_ScriptType208
        self.jpdl32_ScriptType347 = jpdl32_ScriptType347
        self.jpdl32_ScriptType364 = jpdl32_ScriptType364
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def acceptPropagatedEvents(self) -> str:
        return self.__acceptPropagatedEvents

    @acceptPropagatedEvents.setter
    def acceptPropagatedEvents(self, acceptPropagatedEvents: str):
        self.__acceptPropagatedEvents = acceptPropagatedEvents

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def jpdl32_ScriptType145(self):
        return self.__jpdl32_ScriptType145

    @jpdl32_ScriptType145.setter
    def jpdl32_ScriptType145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ScriptType__jpdl32_ScriptType145", None)
        self.__jpdl32_ScriptType145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_NodeType144"):
                opp_val = getattr(old_value, "jpdl32_NodeType144", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_NodeType144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_NodeType144"):
                opp_val = getattr(value, "jpdl32_NodeType144", None)
                setattr(value, "jpdl32_NodeType144", self)

    @property
    def jpdl32_ScriptType(self):
        return self.__jpdl32_ScriptType

    @jpdl32_ScriptType.setter
    def jpdl32_ScriptType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ScriptType__jpdl32_ScriptType", None)
        self.__jpdl32_ScriptType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_CreateTimerType2"):
                opp_val = getattr(old_value, "jpdl32_CreateTimerType2", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_CreateTimerType2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_CreateTimerType2"):
                opp_val = getattr(value, "jpdl32_CreateTimerType2", None)
                setattr(value, "jpdl32_CreateTimerType2", self)

    @property
    def jpdl32_ScriptType100(self):
        return self.__jpdl32_ScriptType100

    @jpdl32_ScriptType100.setter
    def jpdl32_ScriptType100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ScriptType__jpdl32_ScriptType100", None)
        self.__jpdl32_ScriptType100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ExceptionHandlerType99"):
                opp_val = getattr(old_value, "jpdl32_ExceptionHandlerType99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ExceptionHandlerType99"):
                opp_val = getattr(value, "jpdl32_ExceptionHandlerType99", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ExceptionHandlerType99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ScriptType54(self):
        return self.__jpdl32_ScriptType54

    @jpdl32_ScriptType54.setter
    def jpdl32_ScriptType54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ScriptType__jpdl32_ScriptType54", None)
        self.__jpdl32_ScriptType54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot53"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot53"):
                opp_val = getattr(value, "jpdl32_DocumentRoot53", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ScriptType364(self):
        return self.__jpdl32_ScriptType364

    @jpdl32_ScriptType364.setter
    def jpdl32_ScriptType364(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ScriptType__jpdl32_ScriptType364", None)
        self.__jpdl32_ScriptType364 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TransitionType363"):
                opp_val = getattr(old_value, "jpdl32_TransitionType363", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TransitionType363"):
                opp_val = getattr(value, "jpdl32_TransitionType363", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TransitionType363", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ScriptType347(self):
        return self.__jpdl32_ScriptType347

    @jpdl32_ScriptType347.setter
    def jpdl32_ScriptType347(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ScriptType__jpdl32_ScriptType347", None)
        self.__jpdl32_ScriptType347 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TimerType346"):
                opp_val = getattr(old_value, "jpdl32_TimerType346", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_TimerType346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TimerType346"):
                opp_val = getattr(value, "jpdl32_TimerType346", None)
                setattr(value, "jpdl32_TimerType346", self)

    @property
    def jpdl32_ScriptType208(self):
        return self.__jpdl32_ScriptType208

    @jpdl32_ScriptType208.setter
    def jpdl32_ScriptType208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ScriptType__jpdl32_ScriptType208", None)
        self.__jpdl32_ScriptType208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType207"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType207", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType207"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType207", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType207", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ScriptType85(self):
        return self.__jpdl32_ScriptType85

    @jpdl32_ScriptType85.setter
    def jpdl32_ScriptType85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ScriptType__jpdl32_ScriptType85", None)
        self.__jpdl32_ScriptType85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_EventType84"):
                opp_val = getattr(old_value, "jpdl32_EventType84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_EventType84"):
                opp_val = getattr(value, "jpdl32_EventType84", None)
                if opp_val is None:
                    setattr(value, "jpdl32_EventType84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ScriptType103(self):
        return self.__jpdl32_ScriptType103

    @jpdl32_ScriptType103.setter
    def jpdl32_ScriptType103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ScriptType__jpdl32_ScriptType103", None)
        self.__jpdl32_ScriptType103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ForkType102"):
                opp_val = getattr(old_value, "jpdl32_ForkType102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ForkType102"):
                opp_val = getattr(value, "jpdl32_ForkType102", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ForkType102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_CreateTimerType:

    def __init__(self, duedate: str, name: str, repeat: str, transition: str, jpdl32_CreateTimerType: "jpdl32_ActionType" = None, jpdl32_CreateTimerType2: "jpdl32_ScriptType" = None, jpdl32_CreateTimerType26: "jpdl32_DocumentRoot" = None, jpdl32_CreateTimerType88: "jpdl32_EventType" = None, jpdl32_CreateTimerType148: "jpdl32_NodeType" = None, jpdl32_CreateTimerType211: "jpdl32_ProcessDefinitionType" = None, jpdl32_CreateTimerType350: "jpdl32_TimerType" = None, jpdl32_CreateTimerType367: "jpdl32_TransitionType" = None):
        self.duedate = duedate
        self.name = name
        self.repeat = repeat
        self.transition = transition
        self.jpdl32_CreateTimerType = jpdl32_CreateTimerType
        self.jpdl32_CreateTimerType2 = jpdl32_CreateTimerType2
        self.jpdl32_CreateTimerType26 = jpdl32_CreateTimerType26
        self.jpdl32_CreateTimerType88 = jpdl32_CreateTimerType88
        self.jpdl32_CreateTimerType148 = jpdl32_CreateTimerType148
        self.jpdl32_CreateTimerType211 = jpdl32_CreateTimerType211
        self.jpdl32_CreateTimerType350 = jpdl32_CreateTimerType350
        self.jpdl32_CreateTimerType367 = jpdl32_CreateTimerType367
        
    @property
    def repeat(self) -> str:
        return self.__repeat

    @repeat.setter
    def repeat(self, repeat: str):
        self.__repeat = repeat

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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl32_CreateTimerType26(self):
        return self.__jpdl32_CreateTimerType26

    @jpdl32_CreateTimerType26.setter
    def jpdl32_CreateTimerType26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_CreateTimerType__jpdl32_CreateTimerType26", None)
        self.__jpdl32_CreateTimerType26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot25"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot25"):
                opp_val = getattr(value, "jpdl32_DocumentRoot25", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_CreateTimerType350(self):
        return self.__jpdl32_CreateTimerType350

    @jpdl32_CreateTimerType350.setter
    def jpdl32_CreateTimerType350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_CreateTimerType__jpdl32_CreateTimerType350", None)
        self.__jpdl32_CreateTimerType350 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TimerType349"):
                opp_val = getattr(old_value, "jpdl32_TimerType349", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_TimerType349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TimerType349"):
                opp_val = getattr(value, "jpdl32_TimerType349", None)
                setattr(value, "jpdl32_TimerType349", self)

    @property
    def jpdl32_CreateTimerType88(self):
        return self.__jpdl32_CreateTimerType88

    @jpdl32_CreateTimerType88.setter
    def jpdl32_CreateTimerType88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_CreateTimerType__jpdl32_CreateTimerType88", None)
        self.__jpdl32_CreateTimerType88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_EventType87"):
                opp_val = getattr(old_value, "jpdl32_EventType87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_EventType87"):
                opp_val = getattr(value, "jpdl32_EventType87", None)
                if opp_val is None:
                    setattr(value, "jpdl32_EventType87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_CreateTimerType148(self):
        return self.__jpdl32_CreateTimerType148

    @jpdl32_CreateTimerType148.setter
    def jpdl32_CreateTimerType148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_CreateTimerType__jpdl32_CreateTimerType148", None)
        self.__jpdl32_CreateTimerType148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_NodeType147"):
                opp_val = getattr(old_value, "jpdl32_NodeType147", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_NodeType147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_NodeType147"):
                opp_val = getattr(value, "jpdl32_NodeType147", None)
                setattr(value, "jpdl32_NodeType147", self)

    @property
    def jpdl32_CreateTimerType367(self):
        return self.__jpdl32_CreateTimerType367

    @jpdl32_CreateTimerType367.setter
    def jpdl32_CreateTimerType367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_CreateTimerType__jpdl32_CreateTimerType367", None)
        self.__jpdl32_CreateTimerType367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TransitionType366"):
                opp_val = getattr(old_value, "jpdl32_TransitionType366", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TransitionType366"):
                opp_val = getattr(value, "jpdl32_TransitionType366", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TransitionType366", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_CreateTimerType2(self):
        return self.__jpdl32_CreateTimerType2

    @jpdl32_CreateTimerType2.setter
    def jpdl32_CreateTimerType2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_CreateTimerType__jpdl32_CreateTimerType2", None)
        self.__jpdl32_CreateTimerType2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ScriptType"):
                opp_val = getattr(old_value, "jpdl32_ScriptType", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_ScriptType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ScriptType"):
                opp_val = getattr(value, "jpdl32_ScriptType", None)
                setattr(value, "jpdl32_ScriptType", self)

    @property
    def jpdl32_CreateTimerType(self):
        return self.__jpdl32_CreateTimerType

    @jpdl32_CreateTimerType.setter
    def jpdl32_CreateTimerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_CreateTimerType__jpdl32_CreateTimerType", None)
        self.__jpdl32_CreateTimerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ActionType"):
                opp_val = getattr(old_value, "jpdl32_ActionType", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_ActionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ActionType"):
                opp_val = getattr(value, "jpdl32_ActionType", None)
                setattr(value, "jpdl32_ActionType", self)

    @property
    def jpdl32_CreateTimerType211(self):
        return self.__jpdl32_CreateTimerType211

    @jpdl32_CreateTimerType211.setter
    def jpdl32_CreateTimerType211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_CreateTimerType__jpdl32_CreateTimerType211", None)
        self.__jpdl32_CreateTimerType211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType210"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType210", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType210"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType210", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType210", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Delegation:

    pass
class jpdl32_AssignmentType(Delegation):

    def __init__(self, actorId: str, expression: str, pooledActors: str, jpdl32_AssignmentType: "jpdl32_DocumentRoot" = None, jpdl32_AssignmentType312: "jpdl32_SwimlaneType" = None, jpdl32_AssignmentType330: "jpdl32_TaskType" = None):
        self.actorId = actorId
        self.expression = expression
        self.pooledActors = pooledActors
        self.jpdl32_AssignmentType = jpdl32_AssignmentType
        self.jpdl32_AssignmentType312 = jpdl32_AssignmentType312
        self.jpdl32_AssignmentType330 = jpdl32_AssignmentType330
        
    @property
    def pooledActors(self) -> str:
        return self.__pooledActors

    @pooledActors.setter
    def pooledActors(self, pooledActors: str):
        self.__pooledActors = pooledActors

    @property
    def actorId(self) -> str:
        return self.__actorId

    @actorId.setter
    def actorId(self, actorId: str):
        self.__actorId = actorId

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def jpdl32_AssignmentType(self):
        return self.__jpdl32_AssignmentType

    @jpdl32_AssignmentType.setter
    def jpdl32_AssignmentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_AssignmentType__jpdl32_AssignmentType", None)
        self.__jpdl32_AssignmentType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot18"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot18"):
                opp_val = getattr(value, "jpdl32_DocumentRoot18", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_AssignmentType312(self):
        return self.__jpdl32_AssignmentType312

    @jpdl32_AssignmentType312.setter
    def jpdl32_AssignmentType312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_AssignmentType__jpdl32_AssignmentType312", None)
        self.__jpdl32_AssignmentType312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_SwimlaneType311"):
                opp_val = getattr(old_value, "jpdl32_SwimlaneType311", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_SwimlaneType311", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_SwimlaneType311"):
                opp_val = getattr(value, "jpdl32_SwimlaneType311", None)
                setattr(value, "jpdl32_SwimlaneType311", self)

    @property
    def jpdl32_AssignmentType330(self):
        return self.__jpdl32_AssignmentType330

    @jpdl32_AssignmentType330.setter
    def jpdl32_AssignmentType330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_AssignmentType__jpdl32_AssignmentType330", None)
        self.__jpdl32_AssignmentType330 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TaskType329"):
                opp_val = getattr(old_value, "jpdl32_TaskType329", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TaskType329"):
                opp_val = getattr(value, "jpdl32_TaskType329", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TaskType329", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl32_ActionType:

    def __init__(self, class: str, configType: str, expression: str, name: str, refName: str, mixed: str, any: str, acceptPropagatedEvents: str, async: str, jpdl32_ActionType: "jpdl32_CreateTimerType" = None, jpdl32_ActionType16: "jpdl32_DocumentRoot" = None, jpdl32_ActionType82: "jpdl32_EventType" = None, jpdl32_ActionType97: "jpdl32_ExceptionHandlerType" = None, jpdl32_ActionType142: "jpdl32_NodeType" = None, jpdl32_ActionType205: "jpdl32_ProcessDefinitionType" = None, jpdl32_ActionType344: "jpdl32_TimerType" = None, jpdl32_ActionType361: "jpdl32_TransitionType" = None):
        self.class = class
        self.configType = configType
        self.expression = expression
        self.name = name
        self.refName = refName
        self.mixed = mixed
        self.any = any
        self.acceptPropagatedEvents = acceptPropagatedEvents
        self.async = async
        self.jpdl32_ActionType = jpdl32_ActionType
        self.jpdl32_ActionType16 = jpdl32_ActionType16
        self.jpdl32_ActionType82 = jpdl32_ActionType82
        self.jpdl32_ActionType97 = jpdl32_ActionType97
        self.jpdl32_ActionType142 = jpdl32_ActionType142
        self.jpdl32_ActionType205 = jpdl32_ActionType205
        self.jpdl32_ActionType344 = jpdl32_ActionType344
        self.jpdl32_ActionType361 = jpdl32_ActionType361
        
    @property
    def acceptPropagatedEvents(self) -> str:
        return self.__acceptPropagatedEvents

    @acceptPropagatedEvents.setter
    def acceptPropagatedEvents(self, acceptPropagatedEvents: str):
        self.__acceptPropagatedEvents = acceptPropagatedEvents

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

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
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def configType(self) -> str:
        return self.__configType

    @configType.setter
    def configType(self, configType: str):
        self.__configType = configType

    @property
    def refName(self) -> str:
        return self.__refName

    @refName.setter
    def refName(self, refName: str):
        self.__refName = refName

    @property
    def jpdl32_ActionType82(self):
        return self.__jpdl32_ActionType82

    @jpdl32_ActionType82.setter
    def jpdl32_ActionType82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ActionType__jpdl32_ActionType82", None)
        self.__jpdl32_ActionType82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_EventType81"):
                opp_val = getattr(old_value, "jpdl32_EventType81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_EventType81"):
                opp_val = getattr(value, "jpdl32_EventType81", None)
                if opp_val is None:
                    setattr(value, "jpdl32_EventType81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ActionType(self):
        return self.__jpdl32_ActionType

    @jpdl32_ActionType.setter
    def jpdl32_ActionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ActionType__jpdl32_ActionType", None)
        self.__jpdl32_ActionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_CreateTimerType"):
                opp_val = getattr(old_value, "jpdl32_CreateTimerType", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_CreateTimerType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_CreateTimerType"):
                opp_val = getattr(value, "jpdl32_CreateTimerType", None)
                setattr(value, "jpdl32_CreateTimerType", self)

    @property
    def jpdl32_ActionType97(self):
        return self.__jpdl32_ActionType97

    @jpdl32_ActionType97.setter
    def jpdl32_ActionType97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ActionType__jpdl32_ActionType97", None)
        self.__jpdl32_ActionType97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ExceptionHandlerType96"):
                opp_val = getattr(old_value, "jpdl32_ExceptionHandlerType96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ExceptionHandlerType96"):
                opp_val = getattr(value, "jpdl32_ExceptionHandlerType96", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ExceptionHandlerType96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ActionType142(self):
        return self.__jpdl32_ActionType142

    @jpdl32_ActionType142.setter
    def jpdl32_ActionType142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ActionType__jpdl32_ActionType142", None)
        self.__jpdl32_ActionType142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_NodeType141"):
                opp_val = getattr(old_value, "jpdl32_NodeType141", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_NodeType141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_NodeType141"):
                opp_val = getattr(value, "jpdl32_NodeType141", None)
                setattr(value, "jpdl32_NodeType141", self)

    @property
    def jpdl32_ActionType16(self):
        return self.__jpdl32_ActionType16

    @jpdl32_ActionType16.setter
    def jpdl32_ActionType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ActionType__jpdl32_ActionType16", None)
        self.__jpdl32_ActionType16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_DocumentRoot15"):
                opp_val = getattr(old_value, "jpdl32_DocumentRoot15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_DocumentRoot15"):
                opp_val = getattr(value, "jpdl32_DocumentRoot15", None)
                if opp_val is None:
                    setattr(value, "jpdl32_DocumentRoot15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ActionType205(self):
        return self.__jpdl32_ActionType205

    @jpdl32_ActionType205.setter
    def jpdl32_ActionType205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ActionType__jpdl32_ActionType205", None)
        self.__jpdl32_ActionType205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_ProcessDefinitionType204"):
                opp_val = getattr(old_value, "jpdl32_ProcessDefinitionType204", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_ProcessDefinitionType204"):
                opp_val = getattr(value, "jpdl32_ProcessDefinitionType204", None)
                if opp_val is None:
                    setattr(value, "jpdl32_ProcessDefinitionType204", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ActionType361(self):
        return self.__jpdl32_ActionType361

    @jpdl32_ActionType361.setter
    def jpdl32_ActionType361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ActionType__jpdl32_ActionType361", None)
        self.__jpdl32_ActionType361 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TransitionType360"):
                opp_val = getattr(old_value, "jpdl32_TransitionType360", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TransitionType360"):
                opp_val = getattr(value, "jpdl32_TransitionType360", None)
                if opp_val is None:
                    setattr(value, "jpdl32_TransitionType360", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl32_ActionType344(self):
        return self.__jpdl32_ActionType344

    @jpdl32_ActionType344.setter
    def jpdl32_ActionType344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl32_ActionType__jpdl32_ActionType344", None)
        self.__jpdl32_ActionType344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl32_TimerType343"):
                opp_val = getattr(old_value, "jpdl32_TimerType343", None)
                if opp_val == self:
                    setattr(old_value, "jpdl32_TimerType343", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl32_TimerType343"):
                opp_val = getattr(value, "jpdl32_TimerType343", None)
                setattr(value, "jpdl32_TimerType343", self)
