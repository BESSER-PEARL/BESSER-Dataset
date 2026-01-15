from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class RelationOperator(Enum):
    different = "different"
    equal = "equal"
    morethan = "morethan"
    lessthan = "lessthan"
    moreequalthan = "moreequalthan"
    lessequalthan = "lessequalthan"
class ConfigTypeType1(Enum):
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
class MetricType(Enum):
    time = "time"
    collectedData = "collectedData"
    quest = "quest"
    artefact = "artefact"
class AnswerType(Enum):
    comboBox = "comboBox"
    checkBox = "checkBox"
    text = "text"
    paragraphText = "paragraphText"
class PriorityTypeMember0(Enum):
    highest = "highest"
    high = "high"
    normal = "normal"
    low = "low"
    lowest = "lowest"
class BooleanType(Enum):
    yes = "yes"
    no = "no"
    true = "true"
    false = "false"
    on = "on"
    off = "off"
class QuestionnaireType(Enum):
    Pre = "Pre"
    Post = "Post"
class DoEType(Enum):
    LS = "LS"
    CRD = "CRD"
    RCBD = "RCBD"
    other = "other"
class TypeTypeMember1(Enum):
    taskEnd = "taskEnd"
    beforeSignal = "beforeSignal"
    afterSignal = "afterSignal"
    superstateEnter = "superstateEnter"
    superstateLeave = "superstateLeave"
    timerCreate = "timerCreate"
    subprocessCreated = "subprocessCreated"
    subprocessEnd = "subprocessEnd"
    nodeEnter = "nodeEnter"
    nodeLeave = "nodeLeave"
    processStart = "processStart"
    processEnd = "processEnd"
    taskCreate = "taskCreate"
    taskAssign = "taskAssign"
    taskStart = "taskStart"
class ConfigTypeType(Enum):
    field = "field"
    bean = "bean"
    constructor = "constructor"
    configurationProperty = "configurationProperty"
class HypothesisType(Enum):
    null_ = "null_"
    alternative = "alternative"
class ArtefactType(Enum):
    input = "input"
    output = "output"
    inoutput = "inoutput"
class ConfigType(Enum):
    field = "field"
    bean = "bean"
    constructor = "constructor"
    configurationProperty = "configurationProperty"


############################################
# Definition of Classes
############################################

class jpdl31_Design:

    def __init__(self, DoE: str, jpdl31_Design410: set["jpdl31_Factor"] = None, jpdl31_Design413: set["jpdl31_Parameter"] = None, jpdl31_Design415: set["jpdl31_StatisticalTest"] = None, jpdl31_Design: "jpdl31_ExperimentalPlan" = None, jpdl31_Design417: set["jpdl31_DependentVariable"] = None):
        self.DoE = DoE
        self.jpdl31_Design410 = jpdl31_Design410 if jpdl31_Design410 is not None else set()
        self.jpdl31_Design413 = jpdl31_Design413 if jpdl31_Design413 is not None else set()
        self.jpdl31_Design415 = jpdl31_Design415 if jpdl31_Design415 is not None else set()
        self.jpdl31_Design = jpdl31_Design
        self.jpdl31_Design417 = jpdl31_Design417 if jpdl31_Design417 is not None else set()
        
    @property
    def DoE(self) -> str:
        return self.__DoE

    @DoE.setter
    def DoE(self, DoE: str):
        self.__DoE = DoE

    @property
    def jpdl31_Design413(self):
        return self.__jpdl31_Design413

    @jpdl31_Design413.setter
    def jpdl31_Design413(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Design__jpdl31_Design413", None)
        self.__jpdl31_Design413 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Parameter"):
                    opp_val = getattr(item, "jpdl31_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Parameter"):
                    opp_val = getattr(item, "jpdl31_Parameter", None)
                    
                    setattr(item, "jpdl31_Parameter", self)
                    

    @property
    def jpdl31_Design(self):
        return self.__jpdl31_Design

    @jpdl31_Design.setter
    def jpdl31_Design(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Design__jpdl31_Design", None)
        self.__jpdl31_Design = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ExperimentalPlan408"):
                opp_val = getattr(old_value, "jpdl31_ExperimentalPlan408", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_ExperimentalPlan408", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ExperimentalPlan408"):
                opp_val = getattr(value, "jpdl31_ExperimentalPlan408", None)
                setattr(value, "jpdl31_ExperimentalPlan408", self)

    @property
    def jpdl31_Design410(self):
        return self.__jpdl31_Design410

    @jpdl31_Design410.setter
    def jpdl31_Design410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Design__jpdl31_Design410", None)
        self.__jpdl31_Design410 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Factor411"):
                    opp_val = getattr(item, "jpdl31_Factor411", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Factor411", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Factor411"):
                    opp_val = getattr(item, "jpdl31_Factor411", None)
                    
                    setattr(item, "jpdl31_Factor411", self)
                    

    @property
    def jpdl31_Design415(self):
        return self.__jpdl31_Design415

    @jpdl31_Design415.setter
    def jpdl31_Design415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Design__jpdl31_Design415", None)
        self.__jpdl31_Design415 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_StatisticalTest"):
                    opp_val = getattr(item, "jpdl31_StatisticalTest", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_StatisticalTest", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_StatisticalTest"):
                    opp_val = getattr(item, "jpdl31_StatisticalTest", None)
                    
                    setattr(item, "jpdl31_StatisticalTest", self)
                    

    @property
    def jpdl31_Design417(self):
        return self.__jpdl31_Design417

    @jpdl31_Design417.setter
    def jpdl31_Design417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Design__jpdl31_Design417", None)
        self.__jpdl31_Design417 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_DependentVariable418"):
                    opp_val = getattr(item, "jpdl31_DependentVariable418", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_DependentVariable418", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_DependentVariable418"):
                    opp_val = getattr(item, "jpdl31_DependentVariable418", None)
                    
                    setattr(item, "jpdl31_DependentVariable418", self)
                    

class jpdl31_StatisticalTest:

    pass
class jpdl31_Parameter:

    def __init__(self, key: str, value: str, jpdl31_Parameter: "jpdl31_Design" = None):
        self.key = key
        self.value = value
        self.jpdl31_Parameter = jpdl31_Parameter
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def jpdl31_Parameter(self):
        return self.__jpdl31_Parameter

    @jpdl31_Parameter.setter
    def jpdl31_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Parameter__jpdl31_Parameter", None)
        self.__jpdl31_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Design413"):
                opp_val = getattr(old_value, "jpdl31_Design413", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Design413"):
                opp_val = getattr(value, "jpdl31_Design413", None)
                if opp_val is None:
                    setattr(value, "jpdl31_Design413", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_Alternative:

    def __init__(self, description: str, jpdl31_Alternative: "jpdl31_Question" = None):
        self.description = description
        self.jpdl31_Alternative = jpdl31_Alternative
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def jpdl31_Alternative(self):
        return self.__jpdl31_Alternative

    @jpdl31_Alternative.setter
    def jpdl31_Alternative(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Alternative__jpdl31_Alternative", None)
        self.__jpdl31_Alternative = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Question394"):
                opp_val = getattr(old_value, "jpdl31_Question394", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Question394"):
                opp_val = getattr(value, "jpdl31_Question394", None)
                if opp_val is None:
                    setattr(value, "jpdl31_Question394", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_Question:

    def __init__(self, description: str, type: str, required: str, jpdl31_Question: "jpdl31_Questionnaire" = None, jpdl31_Question394: set["jpdl31_Alternative"] = None, jpdl31_Question397: "jpdl31_Question" = None, jpdl31_Question395: "jpdl31_Question" = None):
        self.description = description
        self.type = type
        self.required = required
        self.jpdl31_Question = jpdl31_Question
        self.jpdl31_Question394 = jpdl31_Question394 if jpdl31_Question394 is not None else set()
        self.jpdl31_Question397 = jpdl31_Question397
        self.jpdl31_Question395 = jpdl31_Question395
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def required(self) -> str:
        return self.__required

    @required.setter
    def required(self, required: str):
        self.__required = required

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def jpdl31_Question395(self):
        return self.__jpdl31_Question395

    @jpdl31_Question395.setter
    def jpdl31_Question395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Question__jpdl31_Question395", None)
        self.__jpdl31_Question395 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Question397"):
                opp_val = getattr(old_value, "jpdl31_Question397", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_Question397", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Question397"):
                opp_val = getattr(value, "jpdl31_Question397", None)
                setattr(value, "jpdl31_Question397", self)

    @property
    def jpdl31_Question397(self):
        return self.__jpdl31_Question397

    @jpdl31_Question397.setter
    def jpdl31_Question397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Question__jpdl31_Question397", None)
        self.__jpdl31_Question397 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Question395"):
                opp_val = getattr(old_value, "jpdl31_Question395", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_Question395", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Question395"):
                opp_val = getattr(value, "jpdl31_Question395", None)
                setattr(value, "jpdl31_Question395", self)

    @property
    def jpdl31_Question394(self):
        return self.__jpdl31_Question394

    @jpdl31_Question394.setter
    def jpdl31_Question394(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Question__jpdl31_Question394", None)
        self.__jpdl31_Question394 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Alternative"):
                    opp_val = getattr(item, "jpdl31_Alternative", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Alternative", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Alternative"):
                    opp_val = getattr(item, "jpdl31_Alternative", None)
                    
                    setattr(item, "jpdl31_Alternative", self)
                    

    @property
    def jpdl31_Question(self):
        return self.__jpdl31_Question

    @jpdl31_Question.setter
    def jpdl31_Question(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Question__jpdl31_Question", None)
        self.__jpdl31_Question = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Questionnaire389"):
                opp_val = getattr(old_value, "jpdl31_Questionnaire389", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Questionnaire389"):
                opp_val = getattr(value, "jpdl31_Questionnaire389", None)
                if opp_val is None:
                    setattr(value, "jpdl31_Questionnaire389", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_Factor:

    def __init__(self, name: str, isTreament: str, jpdl31_Factor: set["jpdl31_Level"] = None, jpdl31_Factor411: "jpdl31_Design" = None):
        self.name = name
        self.isTreament = isTreament
        self.jpdl31_Factor = jpdl31_Factor if jpdl31_Factor is not None else set()
        self.jpdl31_Factor411 = jpdl31_Factor411
        
    @property
    def isTreament(self) -> str:
        return self.__isTreament

    @isTreament.setter
    def isTreament(self, isTreament: str):
        self.__isTreament = isTreament

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl31_Factor411(self):
        return self.__jpdl31_Factor411

    @jpdl31_Factor411.setter
    def jpdl31_Factor411(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Factor__jpdl31_Factor411", None)
        self.__jpdl31_Factor411 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Design410"):
                opp_val = getattr(old_value, "jpdl31_Design410", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Design410"):
                opp_val = getattr(value, "jpdl31_Design410", None)
                if opp_val is None:
                    setattr(value, "jpdl31_Design410", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_Factor(self):
        return self.__jpdl31_Factor

    @jpdl31_Factor.setter
    def jpdl31_Factor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Factor__jpdl31_Factor", None)
        self.__jpdl31_Factor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Level384"):
                    opp_val = getattr(item, "jpdl31_Level384", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Level384", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Level384"):
                    opp_val = getattr(item, "jpdl31_Level384", None)
                    
                    setattr(item, "jpdl31_Level384", self)
                    

class jpdl31_Goal:

    def __init__(self, description: str, id: str, jpdl31_Goal: "jpdl31_Hyphotesis" = None, jpdl31_Goal399: set["jpdl31_Hyphotesis"] = None, jpdl31_Goal403: "jpdl31_ExperimentalPlan" = None):
        self.description = description
        self.id = id
        self.jpdl31_Goal = jpdl31_Goal
        self.jpdl31_Goal399 = jpdl31_Goal399 if jpdl31_Goal399 is not None else set()
        self.jpdl31_Goal403 = jpdl31_Goal403
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def jpdl31_Goal399(self):
        return self.__jpdl31_Goal399

    @jpdl31_Goal399.setter
    def jpdl31_Goal399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Goal__jpdl31_Goal399", None)
        self.__jpdl31_Goal399 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Hyphotesis400"):
                    opp_val = getattr(item, "jpdl31_Hyphotesis400", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Hyphotesis400", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Hyphotesis400"):
                    opp_val = getattr(item, "jpdl31_Hyphotesis400", None)
                    
                    setattr(item, "jpdl31_Hyphotesis400", self)
                    

    @property
    def jpdl31_Goal403(self):
        return self.__jpdl31_Goal403

    @jpdl31_Goal403.setter
    def jpdl31_Goal403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Goal__jpdl31_Goal403", None)
        self.__jpdl31_Goal403 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ExperimentalPlan402"):
                opp_val = getattr(old_value, "jpdl31_ExperimentalPlan402", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ExperimentalPlan402"):
                opp_val = getattr(value, "jpdl31_ExperimentalPlan402", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ExperimentalPlan402", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_Goal(self):
        return self.__jpdl31_Goal

    @jpdl31_Goal.setter
    def jpdl31_Goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Goal__jpdl31_Goal", None)
        self.__jpdl31_Goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Hyphotesis369"):
                opp_val = getattr(old_value, "jpdl31_Hyphotesis369", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_Hyphotesis369", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Hyphotesis369"):
                opp_val = getattr(value, "jpdl31_Hyphotesis369", None)
                setattr(value, "jpdl31_Hyphotesis369", self)

class jpdl31_DependentVariable:

    def __init__(self, name: str, description: str, jpdl31_DependentVariable: "jpdl31_Hyphotesis" = None, jpdl31_DependentVariable381: set["jpdl31_Metric"] = None, jpdl31_DependentVariable379: "jpdl31_Subhypotheses" = None, jpdl31_DependentVariable418: "jpdl31_Design" = None):
        self.name = name
        self.description = description
        self.jpdl31_DependentVariable = jpdl31_DependentVariable
        self.jpdl31_DependentVariable381 = jpdl31_DependentVariable381 if jpdl31_DependentVariable381 is not None else set()
        self.jpdl31_DependentVariable379 = jpdl31_DependentVariable379
        self.jpdl31_DependentVariable418 = jpdl31_DependentVariable418
        
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
    def jpdl31_DependentVariable(self):
        return self.__jpdl31_DependentVariable

    @jpdl31_DependentVariable.setter
    def jpdl31_DependentVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DependentVariable__jpdl31_DependentVariable", None)
        self.__jpdl31_DependentVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Hyphotesis373"):
                opp_val = getattr(old_value, "jpdl31_Hyphotesis373", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_Hyphotesis373", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Hyphotesis373"):
                opp_val = getattr(value, "jpdl31_Hyphotesis373", None)
                setattr(value, "jpdl31_Hyphotesis373", self)

    @property
    def jpdl31_DependentVariable379(self):
        return self.__jpdl31_DependentVariable379

    @jpdl31_DependentVariable379.setter
    def jpdl31_DependentVariable379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DependentVariable__jpdl31_DependentVariable379", None)
        self.__jpdl31_DependentVariable379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Subhypotheses378"):
                opp_val = getattr(old_value, "jpdl31_Subhypotheses378", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_Subhypotheses378", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Subhypotheses378"):
                opp_val = getattr(value, "jpdl31_Subhypotheses378", None)
                setattr(value, "jpdl31_Subhypotheses378", self)

    @property
    def jpdl31_DependentVariable381(self):
        return self.__jpdl31_DependentVariable381

    @jpdl31_DependentVariable381.setter
    def jpdl31_DependentVariable381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DependentVariable__jpdl31_DependentVariable381", None)
        self.__jpdl31_DependentVariable381 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Metric382"):
                    opp_val = getattr(item, "jpdl31_Metric382", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Metric382", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Metric382"):
                    opp_val = getattr(item, "jpdl31_Metric382", None)
                    
                    setattr(item, "jpdl31_Metric382", self)
                    

    @property
    def jpdl31_DependentVariable418(self):
        return self.__jpdl31_DependentVariable418

    @jpdl31_DependentVariable418.setter
    def jpdl31_DependentVariable418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DependentVariable__jpdl31_DependentVariable418", None)
        self.__jpdl31_DependentVariable418 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Design417"):
                opp_val = getattr(old_value, "jpdl31_Design417", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Design417"):
                opp_val = getattr(value, "jpdl31_Design417", None)
                if opp_val is None:
                    setattr(value, "jpdl31_Design417", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_Level:

    def __init__(self, name: str, jpdl31_Level: "jpdl31_Hyphotesis" = None, jpdl31_Level384: "jpdl31_Factor" = None, jpdl31_Level376: "jpdl31_Subhypotheses" = None):
        self.name = name
        self.jpdl31_Level = jpdl31_Level
        self.jpdl31_Level384 = jpdl31_Level384
        self.jpdl31_Level376 = jpdl31_Level376
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl31_Level(self):
        return self.__jpdl31_Level

    @jpdl31_Level.setter
    def jpdl31_Level(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Level__jpdl31_Level", None)
        self.__jpdl31_Level = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Hyphotesis371"):
                opp_val = getattr(old_value, "jpdl31_Hyphotesis371", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Hyphotesis371"):
                opp_val = getattr(value, "jpdl31_Hyphotesis371", None)
                if opp_val is None:
                    setattr(value, "jpdl31_Hyphotesis371", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_Level384(self):
        return self.__jpdl31_Level384

    @jpdl31_Level384.setter
    def jpdl31_Level384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Level__jpdl31_Level384", None)
        self.__jpdl31_Level384 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Factor"):
                opp_val = getattr(old_value, "jpdl31_Factor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Factor"):
                opp_val = getattr(value, "jpdl31_Factor", None)
                if opp_val is None:
                    setattr(value, "jpdl31_Factor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_Level376(self):
        return self.__jpdl31_Level376

    @jpdl31_Level376.setter
    def jpdl31_Level376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Level__jpdl31_Level376", None)
        self.__jpdl31_Level376 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Subhypotheses375"):
                opp_val = getattr(old_value, "jpdl31_Subhypotheses375", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_Subhypotheses375", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Subhypotheses375"):
                opp_val = getattr(value, "jpdl31_Subhypotheses375", None)
                setattr(value, "jpdl31_Subhypotheses375", self)

class jpdl31_Subhypotheses:

    def __init__(self, relationOp: str, jpdl31_Subhypotheses: "jpdl31_Hyphotesis" = None, jpdl31_Subhypotheses375: "jpdl31_Level" = None, jpdl31_Subhypotheses378: "jpdl31_DependentVariable" = None):
        self.relationOp = relationOp
        self.jpdl31_Subhypotheses = jpdl31_Subhypotheses
        self.jpdl31_Subhypotheses375 = jpdl31_Subhypotheses375
        self.jpdl31_Subhypotheses378 = jpdl31_Subhypotheses378
        
    @property
    def relationOp(self) -> str:
        return self.__relationOp

    @relationOp.setter
    def relationOp(self, relationOp: str):
        self.__relationOp = relationOp

    @property
    def jpdl31_Subhypotheses378(self):
        return self.__jpdl31_Subhypotheses378

    @jpdl31_Subhypotheses378.setter
    def jpdl31_Subhypotheses378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Subhypotheses__jpdl31_Subhypotheses378", None)
        self.__jpdl31_Subhypotheses378 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DependentVariable379"):
                opp_val = getattr(old_value, "jpdl31_DependentVariable379", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_DependentVariable379", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DependentVariable379"):
                opp_val = getattr(value, "jpdl31_DependentVariable379", None)
                setattr(value, "jpdl31_DependentVariable379", self)

    @property
    def jpdl31_Subhypotheses375(self):
        return self.__jpdl31_Subhypotheses375

    @jpdl31_Subhypotheses375.setter
    def jpdl31_Subhypotheses375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Subhypotheses__jpdl31_Subhypotheses375", None)
        self.__jpdl31_Subhypotheses375 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Level376"):
                opp_val = getattr(old_value, "jpdl31_Level376", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_Level376", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Level376"):
                opp_val = getattr(value, "jpdl31_Level376", None)
                setattr(value, "jpdl31_Level376", self)

    @property
    def jpdl31_Subhypotheses(self):
        return self.__jpdl31_Subhypotheses

    @jpdl31_Subhypotheses.setter
    def jpdl31_Subhypotheses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Subhypotheses__jpdl31_Subhypotheses", None)
        self.__jpdl31_Subhypotheses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Hyphotesis"):
                opp_val = getattr(old_value, "jpdl31_Hyphotesis", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Hyphotesis"):
                opp_val = getattr(value, "jpdl31_Hyphotesis", None)
                if opp_val is None:
                    setattr(value, "jpdl31_Hyphotesis", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_Hyphotesis:

    def __init__(self, relationOp: str, description: str, type: str, id: str, jpdl31_Hyphotesis: set["jpdl31_Subhypotheses"] = None, jpdl31_Hyphotesis371: set["jpdl31_Level"] = None, jpdl31_Hyphotesis373: "jpdl31_DependentVariable" = None, jpdl31_Hyphotesis369: "jpdl31_Goal" = None, jpdl31_Hyphotesis400: "jpdl31_Goal" = None, jpdl31_Hyphotesis406: "jpdl31_ExperimentalPlan" = None):
        self.relationOp = relationOp
        self.description = description
        self.type = type
        self.id = id
        self.jpdl31_Hyphotesis = jpdl31_Hyphotesis if jpdl31_Hyphotesis is not None else set()
        self.jpdl31_Hyphotesis371 = jpdl31_Hyphotesis371 if jpdl31_Hyphotesis371 is not None else set()
        self.jpdl31_Hyphotesis373 = jpdl31_Hyphotesis373
        self.jpdl31_Hyphotesis369 = jpdl31_Hyphotesis369
        self.jpdl31_Hyphotesis400 = jpdl31_Hyphotesis400
        self.jpdl31_Hyphotesis406 = jpdl31_Hyphotesis406
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def relationOp(self) -> str:
        return self.__relationOp

    @relationOp.setter
    def relationOp(self, relationOp: str):
        self.__relationOp = relationOp

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def jpdl31_Hyphotesis400(self):
        return self.__jpdl31_Hyphotesis400

    @jpdl31_Hyphotesis400.setter
    def jpdl31_Hyphotesis400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Hyphotesis__jpdl31_Hyphotesis400", None)
        self.__jpdl31_Hyphotesis400 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Goal399"):
                opp_val = getattr(old_value, "jpdl31_Goal399", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Goal399"):
                opp_val = getattr(value, "jpdl31_Goal399", None)
                if opp_val is None:
                    setattr(value, "jpdl31_Goal399", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_Hyphotesis371(self):
        return self.__jpdl31_Hyphotesis371

    @jpdl31_Hyphotesis371.setter
    def jpdl31_Hyphotesis371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Hyphotesis__jpdl31_Hyphotesis371", None)
        self.__jpdl31_Hyphotesis371 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Level"):
                    opp_val = getattr(item, "jpdl31_Level", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Level", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Level"):
                    opp_val = getattr(item, "jpdl31_Level", None)
                    
                    setattr(item, "jpdl31_Level", self)
                    

    @property
    def jpdl31_Hyphotesis(self):
        return self.__jpdl31_Hyphotesis

    @jpdl31_Hyphotesis.setter
    def jpdl31_Hyphotesis(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Hyphotesis__jpdl31_Hyphotesis", None)
        self.__jpdl31_Hyphotesis = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Subhypotheses"):
                    opp_val = getattr(item, "jpdl31_Subhypotheses", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Subhypotheses", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Subhypotheses"):
                    opp_val = getattr(item, "jpdl31_Subhypotheses", None)
                    
                    setattr(item, "jpdl31_Subhypotheses", self)
                    

    @property
    def jpdl31_Hyphotesis406(self):
        return self.__jpdl31_Hyphotesis406

    @jpdl31_Hyphotesis406.setter
    def jpdl31_Hyphotesis406(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Hyphotesis__jpdl31_Hyphotesis406", None)
        self.__jpdl31_Hyphotesis406 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ExperimentalPlan405"):
                opp_val = getattr(old_value, "jpdl31_ExperimentalPlan405", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ExperimentalPlan405"):
                opp_val = getattr(value, "jpdl31_ExperimentalPlan405", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ExperimentalPlan405", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_Hyphotesis373(self):
        return self.__jpdl31_Hyphotesis373

    @jpdl31_Hyphotesis373.setter
    def jpdl31_Hyphotesis373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Hyphotesis__jpdl31_Hyphotesis373", None)
        self.__jpdl31_Hyphotesis373 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DependentVariable"):
                opp_val = getattr(old_value, "jpdl31_DependentVariable", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_DependentVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DependentVariable"):
                opp_val = getattr(value, "jpdl31_DependentVariable", None)
                setattr(value, "jpdl31_DependentVariable", self)

    @property
    def jpdl31_Hyphotesis369(self):
        return self.__jpdl31_Hyphotesis369

    @jpdl31_Hyphotesis369.setter
    def jpdl31_Hyphotesis369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Hyphotesis__jpdl31_Hyphotesis369", None)
        self.__jpdl31_Hyphotesis369 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Goal"):
                opp_val = getattr(old_value, "jpdl31_Goal", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_Goal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Goal"):
                opp_val = getattr(value, "jpdl31_Goal", None)
                setattr(value, "jpdl31_Goal", self)

class jpdl31_Model:

    pass
class jpdl31_MetricInfo:

    def __init__(self, name: str, jpdl31_MetricInfo: "jpdl31_TaskNodeType" = None, jpdl31_MetricInfo323: "jpdl31_TaskType" = None, jpdl31_MetricInfo365: "jpdl31_Metric" = None):
        self.name = name
        self.jpdl31_MetricInfo = jpdl31_MetricInfo
        self.jpdl31_MetricInfo323 = jpdl31_MetricInfo323
        self.jpdl31_MetricInfo365 = jpdl31_MetricInfo365
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl31_MetricInfo323(self):
        return self.__jpdl31_MetricInfo323

    @jpdl31_MetricInfo323.setter
    def jpdl31_MetricInfo323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_MetricInfo__jpdl31_MetricInfo323", None)
        self.__jpdl31_MetricInfo323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskType322"):
                opp_val = getattr(old_value, "jpdl31_TaskType322", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskType322"):
                opp_val = getattr(value, "jpdl31_TaskType322", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskType322", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_MetricInfo365(self):
        return self.__jpdl31_MetricInfo365

    @jpdl31_MetricInfo365.setter
    def jpdl31_MetricInfo365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_MetricInfo__jpdl31_MetricInfo365", None)
        self.__jpdl31_MetricInfo365 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Metric366"):
                opp_val = getattr(old_value, "jpdl31_Metric366", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_Metric366", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Metric366"):
                opp_val = getattr(value, "jpdl31_Metric366", None)
                setattr(value, "jpdl31_Metric366", self)

    @property
    def jpdl31_MetricInfo(self):
        return self.__jpdl31_MetricInfo

    @jpdl31_MetricInfo.setter
    def jpdl31_MetricInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_MetricInfo__jpdl31_MetricInfo", None)
        self.__jpdl31_MetricInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskNodeType305"):
                opp_val = getattr(old_value, "jpdl31_TaskNodeType305", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskNodeType305"):
                opp_val = getattr(value, "jpdl31_TaskNodeType305", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskNodeType305", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_Artefact:

    def __init__(self, name: str, type: str, description: str, jpdl31_Artefact: "jpdl31_TaskNodeType" = None, jpdl31_Artefact320: "jpdl31_TaskType" = None):
        self.name = name
        self.type = type
        self.description = description
        self.jpdl31_Artefact = jpdl31_Artefact
        self.jpdl31_Artefact320 = jpdl31_Artefact320
        
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
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def jpdl31_Artefact320(self):
        return self.__jpdl31_Artefact320

    @jpdl31_Artefact320.setter
    def jpdl31_Artefact320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Artefact__jpdl31_Artefact320", None)
        self.__jpdl31_Artefact320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskType319"):
                opp_val = getattr(old_value, "jpdl31_TaskType319", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskType319"):
                opp_val = getattr(value, "jpdl31_TaskType319", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskType319", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_Artefact(self):
        return self.__jpdl31_Artefact

    @jpdl31_Artefact.setter
    def jpdl31_Artefact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Artefact__jpdl31_Artefact", None)
        self.__jpdl31_Artefact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskNodeType303"):
                opp_val = getattr(old_value, "jpdl31_TaskNodeType303", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskNodeType303"):
                opp_val = getattr(value, "jpdl31_TaskNodeType303", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskNodeType303", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_SubProcessType:

    def __init__(self, name: str, version: str, jpdl31_SubProcessType: "jpdl31_ProcessStateType" = None):
        self.name = name
        self.version = version
        self.jpdl31_SubProcessType = jpdl31_SubProcessType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

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
            if hasattr(old_value, "jpdl31_ProcessStateType205"):
                opp_val = getattr(old_value, "jpdl31_ProcessStateType205", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessStateType205"):
                opp_val = getattr(value, "jpdl31_ProcessStateType205", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessStateType205", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_Metric:

    def __init__(self, name: str, description: str, type: str, refname: str, jpdl31_Metric: "jpdl31_DocumentRoot" = None, jpdl31_Metric366: "jpdl31_MetricInfo" = None, jpdl31_Metric382: "jpdl31_DependentVariable" = None, jpdl31_Metric386: set["jpdl31_ProcessDefinitionType"] = None):
        self.name = name
        self.description = description
        self.type = type
        self.refname = refname
        self.jpdl31_Metric = jpdl31_Metric
        self.jpdl31_Metric366 = jpdl31_Metric366
        self.jpdl31_Metric382 = jpdl31_Metric382
        self.jpdl31_Metric386 = jpdl31_Metric386 if jpdl31_Metric386 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def refname(self) -> str:
        return self.__refname

    @refname.setter
    def refname(self, refname: str):
        self.__refname = refname

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
    def jpdl31_Metric386(self):
        return self.__jpdl31_Metric386

    @jpdl31_Metric386.setter
    def jpdl31_Metric386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Metric__jpdl31_Metric386", None)
        self.__jpdl31_Metric386 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ProcessDefinitionType387"):
                    opp_val = getattr(item, "jpdl31_ProcessDefinitionType387", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ProcessDefinitionType387", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ProcessDefinitionType387"):
                    opp_val = getattr(item, "jpdl31_ProcessDefinitionType387", None)
                    
                    setattr(item, "jpdl31_ProcessDefinitionType387", self)
                    

    @property
    def jpdl31_Metric366(self):
        return self.__jpdl31_Metric366

    @jpdl31_Metric366.setter
    def jpdl31_Metric366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Metric__jpdl31_Metric366", None)
        self.__jpdl31_Metric366 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_MetricInfo365"):
                opp_val = getattr(old_value, "jpdl31_MetricInfo365", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_MetricInfo365", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_MetricInfo365"):
                opp_val = getattr(value, "jpdl31_MetricInfo365", None)
                setattr(value, "jpdl31_MetricInfo365", self)

    @property
    def jpdl31_Metric(self):
        return self.__jpdl31_Metric

    @jpdl31_Metric.setter
    def jpdl31_Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Metric__jpdl31_Metric", None)
        self.__jpdl31_Metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot74"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot74"):
                opp_val = getattr(value, "jpdl31_DocumentRoot74", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_Metric382(self):
        return self.__jpdl31_Metric382

    @jpdl31_Metric382.setter
    def jpdl31_Metric382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Metric__jpdl31_Metric382", None)
        self.__jpdl31_Metric382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DependentVariable381"):
                opp_val = getattr(old_value, "jpdl31_DependentVariable381", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DependentVariable381"):
                opp_val = getattr(value, "jpdl31_DependentVariable381", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DependentVariable381", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_ExperimentalPlan:

    pass
class jpdl31_Questionnaire:

    def __init__(self, name: str, type: str, jpdl31_Questionnaire: "jpdl31_DocumentRoot" = None, jpdl31_Questionnaire389: set["jpdl31_Question"] = None, jpdl31_Questionnaire391: set["jpdl31_ProcessDefinitionType"] = None):
        self.name = name
        self.type = type
        self.jpdl31_Questionnaire = jpdl31_Questionnaire
        self.jpdl31_Questionnaire389 = jpdl31_Questionnaire389 if jpdl31_Questionnaire389 is not None else set()
        self.jpdl31_Questionnaire391 = jpdl31_Questionnaire391 if jpdl31_Questionnaire391 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl31_Questionnaire391(self):
        return self.__jpdl31_Questionnaire391

    @jpdl31_Questionnaire391.setter
    def jpdl31_Questionnaire391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Questionnaire__jpdl31_Questionnaire391", None)
        self.__jpdl31_Questionnaire391 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ProcessDefinitionType392"):
                    opp_val = getattr(item, "jpdl31_ProcessDefinitionType392", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ProcessDefinitionType392", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ProcessDefinitionType392"):
                    opp_val = getattr(item, "jpdl31_ProcessDefinitionType392", None)
                    
                    setattr(item, "jpdl31_ProcessDefinitionType392", self)
                    

    @property
    def jpdl31_Questionnaire(self):
        return self.__jpdl31_Questionnaire

    @jpdl31_Questionnaire.setter
    def jpdl31_Questionnaire(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Questionnaire__jpdl31_Questionnaire", None)
        self.__jpdl31_Questionnaire = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_DocumentRoot70"):
                opp_val = getattr(old_value, "jpdl31_DocumentRoot70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_DocumentRoot70"):
                opp_val = getattr(value, "jpdl31_DocumentRoot70", None)
                if opp_val is None:
                    setattr(value, "jpdl31_DocumentRoot70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_Questionnaire389(self):
        return self.__jpdl31_Questionnaire389

    @jpdl31_Questionnaire389.setter
    def jpdl31_Questionnaire389(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Questionnaire__jpdl31_Questionnaire389", None)
        self.__jpdl31_Questionnaire389 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Question"):
                    opp_val = getattr(item, "jpdl31_Question", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Question", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Question"):
                    opp_val = getattr(item, "jpdl31_Question", None)
                    
                    setattr(item, "jpdl31_Question", self)
                    

class jpdl31_VariableType:

    def __init__(self, any: str, access: str, mappedName: str, name: str, jpdl31_VariableType: "jpdl31_DocumentRoot" = None, jpdl31_VariableType208: "jpdl31_ProcessStateType" = None):
        self.any = any
        self.access = access
        self.mappedName = mappedName
        self.name = name
        self.jpdl31_VariableType = jpdl31_VariableType
        self.jpdl31_VariableType208 = jpdl31_VariableType208
        
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
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def mappedName(self) -> str:
        return self.__mappedName

    @mappedName.setter
    def mappedName(self, mappedName: str):
        self.__mappedName = mappedName

    @property
    def jpdl31_VariableType208(self):
        return self.__jpdl31_VariableType208

    @jpdl31_VariableType208.setter
    def jpdl31_VariableType208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_VariableType__jpdl31_VariableType208", None)
        self.__jpdl31_VariableType208 = value
        
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

class jpdl31_TaskNodeType:

    def __init__(self, group: str, endTasks: str, name: str, signal: str, async: str, createTasks: str, description: str, jpdl31_TaskNodeType: "jpdl31_DocumentRoot" = None, jpdl31_TaskNodeType164: "jpdl31_ProcessDefinitionType" = None, jpdl31_TaskNodeType253: "jpdl31_SuperStateType" = None, jpdl31_TaskNodeType288: set["jpdl31_TaskType"] = None, jpdl31_TaskNodeType291: set["jpdl31_EventType"] = None, jpdl31_TaskNodeType294: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_TaskNodeType297: set["jpdl31_TimerType"] = None, jpdl31_TaskNodeType300: set["jpdl31_TransitionType"] = None, jpdl31_TaskNodeType303: set["jpdl31_Artefact"] = None, jpdl31_TaskNodeType305: set["jpdl31_MetricInfo"] = None):
        self.group = group
        self.endTasks = endTasks
        self.name = name
        self.signal = signal
        self.async = async
        self.createTasks = createTasks
        self.description = description
        self.jpdl31_TaskNodeType = jpdl31_TaskNodeType
        self.jpdl31_TaskNodeType164 = jpdl31_TaskNodeType164
        self.jpdl31_TaskNodeType253 = jpdl31_TaskNodeType253
        self.jpdl31_TaskNodeType288 = jpdl31_TaskNodeType288 if jpdl31_TaskNodeType288 is not None else set()
        self.jpdl31_TaskNodeType291 = jpdl31_TaskNodeType291 if jpdl31_TaskNodeType291 is not None else set()
        self.jpdl31_TaskNodeType294 = jpdl31_TaskNodeType294 if jpdl31_TaskNodeType294 is not None else set()
        self.jpdl31_TaskNodeType297 = jpdl31_TaskNodeType297 if jpdl31_TaskNodeType297 is not None else set()
        self.jpdl31_TaskNodeType300 = jpdl31_TaskNodeType300 if jpdl31_TaskNodeType300 is not None else set()
        self.jpdl31_TaskNodeType303 = jpdl31_TaskNodeType303 if jpdl31_TaskNodeType303 is not None else set()
        self.jpdl31_TaskNodeType305 = jpdl31_TaskNodeType305 if jpdl31_TaskNodeType305 is not None else set()
        
    @property
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

    @property
    def createTasks(self) -> str:
        return self.__createTasks

    @createTasks.setter
    def createTasks(self, createTasks: str):
        self.__createTasks = createTasks

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
    def signal(self) -> str:
        return self.__signal

    @signal.setter
    def signal(self, signal: str):
        self.__signal = signal

    @property
    def endTasks(self) -> str:
        return self.__endTasks

    @endTasks.setter
    def endTasks(self, endTasks: str):
        self.__endTasks = endTasks

    @property
    def jpdl31_TaskNodeType253(self):
        return self.__jpdl31_TaskNodeType253

    @jpdl31_TaskNodeType253.setter
    def jpdl31_TaskNodeType253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskNodeType__jpdl31_TaskNodeType253", None)
        self.__jpdl31_TaskNodeType253 = value
        
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
                if hasattr(item, "jpdl31_EventType292"):
                    opp_val = getattr(item, "jpdl31_EventType292", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType292", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType292"):
                    opp_val = getattr(item, "jpdl31_EventType292", None)
                    
                    setattr(item, "jpdl31_EventType292", self)
                    

    @property
    def jpdl31_TaskNodeType297(self):
        return self.__jpdl31_TaskNodeType297

    @jpdl31_TaskNodeType297.setter
    def jpdl31_TaskNodeType297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskNodeType__jpdl31_TaskNodeType297", None)
        self.__jpdl31_TaskNodeType297 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType298"):
                    opp_val = getattr(item, "jpdl31_TimerType298", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType298", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType298"):
                    opp_val = getattr(item, "jpdl31_TimerType298", None)
                    
                    setattr(item, "jpdl31_TimerType298", self)
                    

    @property
    def jpdl31_TaskNodeType303(self):
        return self.__jpdl31_TaskNodeType303

    @jpdl31_TaskNodeType303.setter
    def jpdl31_TaskNodeType303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskNodeType__jpdl31_TaskNodeType303", None)
        self.__jpdl31_TaskNodeType303 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Artefact"):
                    opp_val = getattr(item, "jpdl31_Artefact", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Artefact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Artefact"):
                    opp_val = getattr(item, "jpdl31_Artefact", None)
                    
                    setattr(item, "jpdl31_Artefact", self)
                    

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
                if hasattr(item, "jpdl31_ExceptionHandlerType295"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType295", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType295", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType295"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType295", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType295", self)
                    

    @property
    def jpdl31_TaskNodeType305(self):
        return self.__jpdl31_TaskNodeType305

    @jpdl31_TaskNodeType305.setter
    def jpdl31_TaskNodeType305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskNodeType__jpdl31_TaskNodeType305", None)
        self.__jpdl31_TaskNodeType305 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_MetricInfo"):
                    opp_val = getattr(item, "jpdl31_MetricInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_MetricInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_MetricInfo"):
                    opp_val = getattr(item, "jpdl31_MetricInfo", None)
                    
                    setattr(item, "jpdl31_MetricInfo", self)
                    

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
                if hasattr(item, "jpdl31_TaskType289"):
                    opp_val = getattr(item, "jpdl31_TaskType289", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TaskType289", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TaskType289"):
                    opp_val = getattr(item, "jpdl31_TaskType289", None)
                    
                    setattr(item, "jpdl31_TaskType289", self)
                    

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
    def jpdl31_TaskNodeType300(self):
        return self.__jpdl31_TaskNodeType300

    @jpdl31_TaskNodeType300.setter
    def jpdl31_TaskNodeType300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskNodeType__jpdl31_TaskNodeType300", None)
        self.__jpdl31_TaskNodeType300 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType301"):
                    opp_val = getattr(item, "jpdl31_TransitionType301", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType301", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType301"):
                    opp_val = getattr(item, "jpdl31_TransitionType301", None)
                    
                    setattr(item, "jpdl31_TransitionType301", self)
                    

    @property
    def jpdl31_TaskNodeType164(self):
        return self.__jpdl31_TaskNodeType164

    @jpdl31_TaskNodeType164.setter
    def jpdl31_TaskNodeType164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskNodeType__jpdl31_TaskNodeType164", None)
        self.__jpdl31_TaskNodeType164 = value
        
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

class jpdl31_TaskType:

    def __init__(self, group: str, blocking: str, description: str, duedate: str, name: str, priority: str, signalling: str, swimlane: str, jpdl31_TaskType: "jpdl31_DocumentRoot" = None, jpdl31_TaskType203: "jpdl31_ProcessDefinitionType" = None, jpdl31_TaskType223: "jpdl31_StartStateType" = None, jpdl31_TaskType289: "jpdl31_TaskNodeType" = None, jpdl31_TaskType307: set["jpdl31_AssignmentType"] = None, jpdl31_TaskType310: set["jpdl31_Delegation"] = None, jpdl31_TaskType313: set["jpdl31_EventType"] = None, jpdl31_TaskType316: set["jpdl31_TimerType"] = None, jpdl31_TaskType319: set["jpdl31_Artefact"] = None, jpdl31_TaskType322: set["jpdl31_MetricInfo"] = None):
        self.group = group
        self.blocking = blocking
        self.description = description
        self.duedate = duedate
        self.name = name
        self.priority = priority
        self.signalling = signalling
        self.swimlane = swimlane
        self.jpdl31_TaskType = jpdl31_TaskType
        self.jpdl31_TaskType203 = jpdl31_TaskType203
        self.jpdl31_TaskType223 = jpdl31_TaskType223
        self.jpdl31_TaskType289 = jpdl31_TaskType289
        self.jpdl31_TaskType307 = jpdl31_TaskType307 if jpdl31_TaskType307 is not None else set()
        self.jpdl31_TaskType310 = jpdl31_TaskType310 if jpdl31_TaskType310 is not None else set()
        self.jpdl31_TaskType313 = jpdl31_TaskType313 if jpdl31_TaskType313 is not None else set()
        self.jpdl31_TaskType316 = jpdl31_TaskType316 if jpdl31_TaskType316 is not None else set()
        self.jpdl31_TaskType319 = jpdl31_TaskType319 if jpdl31_TaskType319 is not None else set()
        self.jpdl31_TaskType322 = jpdl31_TaskType322 if jpdl31_TaskType322 is not None else set()
        
    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

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
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def duedate(self) -> str:
        return self.__duedate

    @duedate.setter
    def duedate(self, duedate: str):
        self.__duedate = duedate

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
    def jpdl31_TaskType319(self):
        return self.__jpdl31_TaskType319

    @jpdl31_TaskType319.setter
    def jpdl31_TaskType319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType319", None)
        self.__jpdl31_TaskType319 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Artefact320"):
                    opp_val = getattr(item, "jpdl31_Artefact320", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Artefact320", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Artefact320"):
                    opp_val = getattr(item, "jpdl31_Artefact320", None)
                    
                    setattr(item, "jpdl31_Artefact320", self)
                    

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
    def jpdl31_TaskType289(self):
        return self.__jpdl31_TaskType289

    @jpdl31_TaskType289.setter
    def jpdl31_TaskType289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType289", None)
        self.__jpdl31_TaskType289 = value
        
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
    def jpdl31_TaskType316(self):
        return self.__jpdl31_TaskType316

    @jpdl31_TaskType316.setter
    def jpdl31_TaskType316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType316", None)
        self.__jpdl31_TaskType316 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType317"):
                    opp_val = getattr(item, "jpdl31_TimerType317", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType317", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType317"):
                    opp_val = getattr(item, "jpdl31_TimerType317", None)
                    
                    setattr(item, "jpdl31_TimerType317", self)
                    

    @property
    def jpdl31_TaskType322(self):
        return self.__jpdl31_TaskType322

    @jpdl31_TaskType322.setter
    def jpdl31_TaskType322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType322", None)
        self.__jpdl31_TaskType322 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_MetricInfo323"):
                    opp_val = getattr(item, "jpdl31_MetricInfo323", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_MetricInfo323", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_MetricInfo323"):
                    opp_val = getattr(item, "jpdl31_MetricInfo323", None)
                    
                    setattr(item, "jpdl31_MetricInfo323", self)
                    

    @property
    def jpdl31_TaskType307(self):
        return self.__jpdl31_TaskType307

    @jpdl31_TaskType307.setter
    def jpdl31_TaskType307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType307", None)
        self.__jpdl31_TaskType307 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_AssignmentType308"):
                    opp_val = getattr(item, "jpdl31_AssignmentType308", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_AssignmentType308", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_AssignmentType308"):
                    opp_val = getattr(item, "jpdl31_AssignmentType308", None)
                    
                    setattr(item, "jpdl31_AssignmentType308", self)
                    

    @property
    def jpdl31_TaskType203(self):
        return self.__jpdl31_TaskType203

    @jpdl31_TaskType203.setter
    def jpdl31_TaskType203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType203", None)
        self.__jpdl31_TaskType203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType202"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType202", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType202"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType202", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType202", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TaskType310(self):
        return self.__jpdl31_TaskType310

    @jpdl31_TaskType310.setter
    def jpdl31_TaskType310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType310", None)
        self.__jpdl31_TaskType310 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Delegation311"):
                    opp_val = getattr(item, "jpdl31_Delegation311", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Delegation311", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Delegation311"):
                    opp_val = getattr(item, "jpdl31_Delegation311", None)
                    
                    setattr(item, "jpdl31_Delegation311", self)
                    

    @property
    def jpdl31_TaskType223(self):
        return self.__jpdl31_TaskType223

    @jpdl31_TaskType223.setter
    def jpdl31_TaskType223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType223", None)
        self.__jpdl31_TaskType223 = value
        
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
    def jpdl31_TaskType313(self):
        return self.__jpdl31_TaskType313

    @jpdl31_TaskType313.setter
    def jpdl31_TaskType313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TaskType__jpdl31_TaskType313", None)
        self.__jpdl31_TaskType313 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType314"):
                    opp_val = getattr(item, "jpdl31_EventType314", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType314", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType314"):
                    opp_val = getattr(item, "jpdl31_EventType314", None)
                    
                    setattr(item, "jpdl31_EventType314", self)
                    

class jpdl31_SwimlaneType:

    def __init__(self, name: str, jpdl31_SwimlaneType: "jpdl31_DocumentRoot" = None, jpdl31_SwimlaneType152: "jpdl31_ProcessDefinitionType" = None, jpdl31_SwimlaneType285: "jpdl31_AssignmentType" = None):
        self.name = name
        self.jpdl31_SwimlaneType = jpdl31_SwimlaneType
        self.jpdl31_SwimlaneType152 = jpdl31_SwimlaneType152
        self.jpdl31_SwimlaneType285 = jpdl31_SwimlaneType285
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl31_SwimlaneType152(self):
        return self.__jpdl31_SwimlaneType152

    @jpdl31_SwimlaneType152.setter
    def jpdl31_SwimlaneType152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SwimlaneType__jpdl31_SwimlaneType152", None)
        self.__jpdl31_SwimlaneType152 = value
        
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
    def jpdl31_SwimlaneType285(self):
        return self.__jpdl31_SwimlaneType285

    @jpdl31_SwimlaneType285.setter
    def jpdl31_SwimlaneType285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SwimlaneType__jpdl31_SwimlaneType285", None)
        self.__jpdl31_SwimlaneType285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_AssignmentType286"):
                opp_val = getattr(old_value, "jpdl31_AssignmentType286", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_AssignmentType286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_AssignmentType286"):
                opp_val = getattr(value, "jpdl31_AssignmentType286", None)
                setattr(value, "jpdl31_AssignmentType286", self)

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

class jpdl31_TransitionType:

    def __init__(self, group: str, to: str, name: str, jpdl31_TransitionType: "jpdl31_DocumentRoot" = None, jpdl31_TransitionType113: "jpdl31_ForkType" = None, jpdl31_TransitionType125: "jpdl31_JoinType" = None, jpdl31_TransitionType149: "jpdl31_NodeType" = None, jpdl31_TransitionType220: "jpdl31_ProcessStateType" = None, jpdl31_TransitionType226: "jpdl31_StartStateType" = None, jpdl31_TransitionType244: "jpdl31_StateType" = None, jpdl31_TransitionType283: "jpdl31_SuperStateType" = None, jpdl31_TransitionType301: "jpdl31_TaskNodeType" = None, jpdl31_TransitionType337: set["jpdl31_CreateTimerType"] = None, jpdl31_TransitionType331: set["jpdl31_ActionType"] = None, jpdl31_TransitionType334: set["jpdl31_ScriptType"] = None, jpdl31_TransitionType340: set["jpdl31_CancelTimerType"] = None, jpdl31_TransitionType343: set["jpdl31_ExceptionHandlerType"] = None):
        self.group = group
        self.to = to
        self.name = name
        self.jpdl31_TransitionType = jpdl31_TransitionType
        self.jpdl31_TransitionType113 = jpdl31_TransitionType113
        self.jpdl31_TransitionType125 = jpdl31_TransitionType125
        self.jpdl31_TransitionType149 = jpdl31_TransitionType149
        self.jpdl31_TransitionType220 = jpdl31_TransitionType220
        self.jpdl31_TransitionType226 = jpdl31_TransitionType226
        self.jpdl31_TransitionType244 = jpdl31_TransitionType244
        self.jpdl31_TransitionType283 = jpdl31_TransitionType283
        self.jpdl31_TransitionType301 = jpdl31_TransitionType301
        self.jpdl31_TransitionType337 = jpdl31_TransitionType337 if jpdl31_TransitionType337 is not None else set()
        self.jpdl31_TransitionType331 = jpdl31_TransitionType331 if jpdl31_TransitionType331 is not None else set()
        self.jpdl31_TransitionType334 = jpdl31_TransitionType334 if jpdl31_TransitionType334 is not None else set()
        self.jpdl31_TransitionType340 = jpdl31_TransitionType340 if jpdl31_TransitionType340 is not None else set()
        self.jpdl31_TransitionType343 = jpdl31_TransitionType343 if jpdl31_TransitionType343 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def jpdl31_TransitionType337(self):
        return self.__jpdl31_TransitionType337

    @jpdl31_TransitionType337.setter
    def jpdl31_TransitionType337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType337", None)
        self.__jpdl31_TransitionType337 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CreateTimerType338"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType338", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CreateTimerType338", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CreateTimerType338"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType338", None)
                    
                    setattr(item, "jpdl31_CreateTimerType338", self)
                    

    @property
    def jpdl31_TransitionType125(self):
        return self.__jpdl31_TransitionType125

    @jpdl31_TransitionType125.setter
    def jpdl31_TransitionType125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType125", None)
        self.__jpdl31_TransitionType125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_JoinType124"):
                opp_val = getattr(old_value, "jpdl31_JoinType124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_JoinType124"):
                opp_val = getattr(value, "jpdl31_JoinType124", None)
                if opp_val is None:
                    setattr(value, "jpdl31_JoinType124", set([self]))
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
    def jpdl31_TransitionType220(self):
        return self.__jpdl31_TransitionType220

    @jpdl31_TransitionType220.setter
    def jpdl31_TransitionType220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType220", None)
        self.__jpdl31_TransitionType220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessStateType219"):
                opp_val = getattr(old_value, "jpdl31_ProcessStateType219", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessStateType219"):
                opp_val = getattr(value, "jpdl31_ProcessStateType219", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessStateType219", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType149(self):
        return self.__jpdl31_TransitionType149

    @jpdl31_TransitionType149.setter
    def jpdl31_TransitionType149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType149", None)
        self.__jpdl31_TransitionType149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_NodeType148"):
                opp_val = getattr(old_value, "jpdl31_NodeType148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_NodeType148"):
                opp_val = getattr(value, "jpdl31_NodeType148", None)
                if opp_val is None:
                    setattr(value, "jpdl31_NodeType148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType113(self):
        return self.__jpdl31_TransitionType113

    @jpdl31_TransitionType113.setter
    def jpdl31_TransitionType113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType113", None)
        self.__jpdl31_TransitionType113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ForkType112"):
                opp_val = getattr(old_value, "jpdl31_ForkType112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ForkType112"):
                opp_val = getattr(value, "jpdl31_ForkType112", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ForkType112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType340(self):
        return self.__jpdl31_TransitionType340

    @jpdl31_TransitionType340.setter
    def jpdl31_TransitionType340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType340", None)
        self.__jpdl31_TransitionType340 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CancelTimerType341"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType341", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CancelTimerType341", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CancelTimerType341"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType341", None)
                    
                    setattr(item, "jpdl31_CancelTimerType341", self)
                    

    @property
    def jpdl31_TransitionType301(self):
        return self.__jpdl31_TransitionType301

    @jpdl31_TransitionType301.setter
    def jpdl31_TransitionType301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType301", None)
        self.__jpdl31_TransitionType301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskNodeType300"):
                opp_val = getattr(old_value, "jpdl31_TaskNodeType300", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskNodeType300"):
                opp_val = getattr(value, "jpdl31_TaskNodeType300", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskNodeType300", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType331(self):
        return self.__jpdl31_TransitionType331

    @jpdl31_TransitionType331.setter
    def jpdl31_TransitionType331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType331", None)
        self.__jpdl31_TransitionType331 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ActionType332"):
                    opp_val = getattr(item, "jpdl31_ActionType332", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ActionType332", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ActionType332"):
                    opp_val = getattr(item, "jpdl31_ActionType332", None)
                    
                    setattr(item, "jpdl31_ActionType332", self)
                    

    @property
    def jpdl31_TransitionType226(self):
        return self.__jpdl31_TransitionType226

    @jpdl31_TransitionType226.setter
    def jpdl31_TransitionType226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType226", None)
        self.__jpdl31_TransitionType226 = value
        
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

    @property
    def jpdl31_TransitionType343(self):
        return self.__jpdl31_TransitionType343

    @jpdl31_TransitionType343.setter
    def jpdl31_TransitionType343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType343", None)
        self.__jpdl31_TransitionType343 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType344"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType344", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType344", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType344"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType344", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType344", self)
                    

    @property
    def jpdl31_TransitionType244(self):
        return self.__jpdl31_TransitionType244

    @jpdl31_TransitionType244.setter
    def jpdl31_TransitionType244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType244", None)
        self.__jpdl31_TransitionType244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_StateType243"):
                opp_val = getattr(old_value, "jpdl31_StateType243", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_StateType243"):
                opp_val = getattr(value, "jpdl31_StateType243", None)
                if opp_val is None:
                    setattr(value, "jpdl31_StateType243", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType283(self):
        return self.__jpdl31_TransitionType283

    @jpdl31_TransitionType283.setter
    def jpdl31_TransitionType283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType283", None)
        self.__jpdl31_TransitionType283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType282"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType282", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType282"):
                opp_val = getattr(value, "jpdl31_SuperStateType282", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType282", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TransitionType334(self):
        return self.__jpdl31_TransitionType334

    @jpdl31_TransitionType334.setter
    def jpdl31_TransitionType334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType__jpdl31_TransitionType334", None)
        self.__jpdl31_TransitionType334 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ScriptType335"):
                    opp_val = getattr(item, "jpdl31_ScriptType335", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ScriptType335", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ScriptType335"):
                    opp_val = getattr(item, "jpdl31_ScriptType335", None)
                    
                    setattr(item, "jpdl31_ScriptType335", self)
                    

class jpdl31_TimerType:

    def __init__(self, name: str, repeat: str, transition: str, duedate: str, jpdl31_TimerType: "jpdl31_DocumentRoot" = None, jpdl31_TimerType110: "jpdl31_ForkType" = None, jpdl31_TimerType122: "jpdl31_JoinType" = None, jpdl31_TimerType146: "jpdl31_NodeType" = None, jpdl31_TimerType217: "jpdl31_ProcessStateType" = None, jpdl31_TimerType241: "jpdl31_StateType" = None, jpdl31_TimerType280: "jpdl31_SuperStateType" = None, jpdl31_TimerType298: "jpdl31_TaskNodeType" = None, jpdl31_TimerType317: "jpdl31_TaskType" = None, jpdl31_TimerType325: "jpdl31_ActionType" = None, jpdl31_TimerType328: "jpdl31_ScriptType" = None):
        self.name = name
        self.repeat = repeat
        self.transition = transition
        self.duedate = duedate
        self.jpdl31_TimerType = jpdl31_TimerType
        self.jpdl31_TimerType110 = jpdl31_TimerType110
        self.jpdl31_TimerType122 = jpdl31_TimerType122
        self.jpdl31_TimerType146 = jpdl31_TimerType146
        self.jpdl31_TimerType217 = jpdl31_TimerType217
        self.jpdl31_TimerType241 = jpdl31_TimerType241
        self.jpdl31_TimerType280 = jpdl31_TimerType280
        self.jpdl31_TimerType298 = jpdl31_TimerType298
        self.jpdl31_TimerType317 = jpdl31_TimerType317
        self.jpdl31_TimerType325 = jpdl31_TimerType325
        self.jpdl31_TimerType328 = jpdl31_TimerType328
        
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
    def repeat(self) -> str:
        return self.__repeat

    @repeat.setter
    def repeat(self, repeat: str):
        self.__repeat = repeat

    @property
    def transition(self) -> str:
        return self.__transition

    @transition.setter
    def transition(self, transition: str):
        self.__transition = transition

    @property
    def jpdl31_TimerType241(self):
        return self.__jpdl31_TimerType241

    @jpdl31_TimerType241.setter
    def jpdl31_TimerType241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType241", None)
        self.__jpdl31_TimerType241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_StateType240"):
                opp_val = getattr(old_value, "jpdl31_StateType240", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_StateType240"):
                opp_val = getattr(value, "jpdl31_StateType240", None)
                if opp_val is None:
                    setattr(value, "jpdl31_StateType240", set([self]))
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
    def jpdl31_TimerType317(self):
        return self.__jpdl31_TimerType317

    @jpdl31_TimerType317.setter
    def jpdl31_TimerType317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType317", None)
        self.__jpdl31_TimerType317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskType316"):
                opp_val = getattr(old_value, "jpdl31_TaskType316", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskType316"):
                opp_val = getattr(value, "jpdl31_TaskType316", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskType316", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TimerType217(self):
        return self.__jpdl31_TimerType217

    @jpdl31_TimerType217.setter
    def jpdl31_TimerType217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType217", None)
        self.__jpdl31_TimerType217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessStateType216"):
                opp_val = getattr(old_value, "jpdl31_ProcessStateType216", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessStateType216"):
                opp_val = getattr(value, "jpdl31_ProcessStateType216", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessStateType216", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TimerType146(self):
        return self.__jpdl31_TimerType146

    @jpdl31_TimerType146.setter
    def jpdl31_TimerType146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType146", None)
        self.__jpdl31_TimerType146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_NodeType145"):
                opp_val = getattr(old_value, "jpdl31_NodeType145", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_NodeType145"):
                opp_val = getattr(value, "jpdl31_NodeType145", None)
                if opp_val is None:
                    setattr(value, "jpdl31_NodeType145", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TimerType328(self):
        return self.__jpdl31_TimerType328

    @jpdl31_TimerType328.setter
    def jpdl31_TimerType328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType328", None)
        self.__jpdl31_TimerType328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ScriptType329"):
                opp_val = getattr(old_value, "jpdl31_ScriptType329", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_ScriptType329", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ScriptType329"):
                opp_val = getattr(value, "jpdl31_ScriptType329", None)
                setattr(value, "jpdl31_ScriptType329", self)

    @property
    def jpdl31_TimerType122(self):
        return self.__jpdl31_TimerType122

    @jpdl31_TimerType122.setter
    def jpdl31_TimerType122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType122", None)
        self.__jpdl31_TimerType122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_JoinType121"):
                opp_val = getattr(old_value, "jpdl31_JoinType121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_JoinType121"):
                opp_val = getattr(value, "jpdl31_JoinType121", None)
                if opp_val is None:
                    setattr(value, "jpdl31_JoinType121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TimerType298(self):
        return self.__jpdl31_TimerType298

    @jpdl31_TimerType298.setter
    def jpdl31_TimerType298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType298", None)
        self.__jpdl31_TimerType298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskNodeType297"):
                opp_val = getattr(old_value, "jpdl31_TaskNodeType297", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskNodeType297"):
                opp_val = getattr(value, "jpdl31_TaskNodeType297", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskNodeType297", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TimerType325(self):
        return self.__jpdl31_TimerType325

    @jpdl31_TimerType325.setter
    def jpdl31_TimerType325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType325", None)
        self.__jpdl31_TimerType325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ActionType326"):
                opp_val = getattr(old_value, "jpdl31_ActionType326", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_ActionType326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ActionType326"):
                opp_val = getattr(value, "jpdl31_ActionType326", None)
                setattr(value, "jpdl31_ActionType326", self)

    @property
    def jpdl31_TimerType110(self):
        return self.__jpdl31_TimerType110

    @jpdl31_TimerType110.setter
    def jpdl31_TimerType110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType110", None)
        self.__jpdl31_TimerType110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ForkType109"):
                opp_val = getattr(old_value, "jpdl31_ForkType109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ForkType109"):
                opp_val = getattr(value, "jpdl31_ForkType109", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ForkType109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_TimerType280(self):
        return self.__jpdl31_TimerType280

    @jpdl31_TimerType280.setter
    def jpdl31_TimerType280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TimerType__jpdl31_TimerType280", None)
        self.__jpdl31_TimerType280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType279"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType279", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType279"):
                opp_val = getattr(value, "jpdl31_SuperStateType279", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType279", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_StateType:

    def __init__(self, nodeContentElements: str, name: str, async: str, jpdl31_StateType: "jpdl31_DocumentRoot" = None, jpdl31_StateType161: "jpdl31_ProcessDefinitionType" = None, jpdl31_StateType234: set["jpdl31_EventType"] = None, jpdl31_StateType237: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_StateType240: set["jpdl31_TimerType"] = None, jpdl31_StateType243: set["jpdl31_TransitionType"] = None, jpdl31_StateType250: "jpdl31_SuperStateType" = None):
        self.nodeContentElements = nodeContentElements
        self.name = name
        self.async = async
        self.jpdl31_StateType = jpdl31_StateType
        self.jpdl31_StateType161 = jpdl31_StateType161
        self.jpdl31_StateType234 = jpdl31_StateType234 if jpdl31_StateType234 is not None else set()
        self.jpdl31_StateType237 = jpdl31_StateType237 if jpdl31_StateType237 is not None else set()
        self.jpdl31_StateType240 = jpdl31_StateType240 if jpdl31_StateType240 is not None else set()
        self.jpdl31_StateType243 = jpdl31_StateType243 if jpdl31_StateType243 is not None else set()
        self.jpdl31_StateType250 = jpdl31_StateType250
        
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
    def nodeContentElements(self) -> str:
        return self.__nodeContentElements

    @nodeContentElements.setter
    def nodeContentElements(self, nodeContentElements: str):
        self.__nodeContentElements = nodeContentElements

    @property
    def jpdl31_StateType250(self):
        return self.__jpdl31_StateType250

    @jpdl31_StateType250.setter
    def jpdl31_StateType250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StateType__jpdl31_StateType250", None)
        self.__jpdl31_StateType250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType249"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType249", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType249"):
                opp_val = getattr(value, "jpdl31_SuperStateType249", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType249", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_StateType240(self):
        return self.__jpdl31_StateType240

    @jpdl31_StateType240.setter
    def jpdl31_StateType240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StateType__jpdl31_StateType240", None)
        self.__jpdl31_StateType240 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType241"):
                    opp_val = getattr(item, "jpdl31_TimerType241", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType241", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType241"):
                    opp_val = getattr(item, "jpdl31_TimerType241", None)
                    
                    setattr(item, "jpdl31_TimerType241", self)
                    

    @property
    def jpdl31_StateType161(self):
        return self.__jpdl31_StateType161

    @jpdl31_StateType161.setter
    def jpdl31_StateType161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StateType__jpdl31_StateType161", None)
        self.__jpdl31_StateType161 = value
        
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
    def jpdl31_StateType243(self):
        return self.__jpdl31_StateType243

    @jpdl31_StateType243.setter
    def jpdl31_StateType243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StateType__jpdl31_StateType243", None)
        self.__jpdl31_StateType243 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType244"):
                    opp_val = getattr(item, "jpdl31_TransitionType244", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType244", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType244"):
                    opp_val = getattr(item, "jpdl31_TransitionType244", None)
                    
                    setattr(item, "jpdl31_TransitionType244", self)
                    

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
                if hasattr(item, "jpdl31_EventType235"):
                    opp_val = getattr(item, "jpdl31_EventType235", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType235", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType235"):
                    opp_val = getattr(item, "jpdl31_EventType235", None)
                    
                    setattr(item, "jpdl31_EventType235", self)
                    

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
                if hasattr(item, "jpdl31_ExceptionHandlerType238"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType238", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType238", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType238"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType238", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType238", self)
                    

class jpdl31_StartStateType:

    def __init__(self, name: str, group: str, jpdl31_StartStateType: "jpdl31_DocumentRoot" = None, jpdl31_StartStateType155: "jpdl31_ProcessDefinitionType" = None, jpdl31_StartStateType231: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_StartStateType222: set["jpdl31_TaskType"] = None, jpdl31_StartStateType225: set["jpdl31_TransitionType"] = None, jpdl31_StartStateType228: set["jpdl31_EventType"] = None):
        self.name = name
        self.group = group
        self.jpdl31_StartStateType = jpdl31_StartStateType
        self.jpdl31_StartStateType155 = jpdl31_StartStateType155
        self.jpdl31_StartStateType231 = jpdl31_StartStateType231 if jpdl31_StartStateType231 is not None else set()
        self.jpdl31_StartStateType222 = jpdl31_StartStateType222 if jpdl31_StartStateType222 is not None else set()
        self.jpdl31_StartStateType225 = jpdl31_StartStateType225 if jpdl31_StartStateType225 is not None else set()
        self.jpdl31_StartStateType228 = jpdl31_StartStateType228 if jpdl31_StartStateType228 is not None else set()
        
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
    def jpdl31_StartStateType155(self):
        return self.__jpdl31_StartStateType155

    @jpdl31_StartStateType155.setter
    def jpdl31_StartStateType155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StartStateType__jpdl31_StartStateType155", None)
        self.__jpdl31_StartStateType155 = value
        
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
    def jpdl31_StartStateType231(self):
        return self.__jpdl31_StartStateType231

    @jpdl31_StartStateType231.setter
    def jpdl31_StartStateType231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StartStateType__jpdl31_StartStateType231", None)
        self.__jpdl31_StartStateType231 = value if value is not None else set()
        
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
                if hasattr(item, "jpdl31_TaskType223"):
                    opp_val = getattr(item, "jpdl31_TaskType223", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TaskType223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TaskType223"):
                    opp_val = getattr(item, "jpdl31_TaskType223", None)
                    
                    setattr(item, "jpdl31_TaskType223", self)
                    

    @property
    def jpdl31_StartStateType228(self):
        return self.__jpdl31_StartStateType228

    @jpdl31_StartStateType228.setter
    def jpdl31_StartStateType228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_StartStateType__jpdl31_StartStateType228", None)
        self.__jpdl31_StartStateType228 = value if value is not None else set()
        
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
                if hasattr(item, "jpdl31_TransitionType226"):
                    opp_val = getattr(item, "jpdl31_TransitionType226", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType226"):
                    opp_val = getattr(item, "jpdl31_TransitionType226", None)
                    
                    setattr(item, "jpdl31_TransitionType226", self)
                    

class jpdl31_SuperStateType:

    def __init__(self, group: str, async: str, name: str, jpdl31_SuperStateType: "jpdl31_DocumentRoot" = None, jpdl31_SuperStateType167: "jpdl31_ProcessDefinitionType" = None, jpdl31_SuperStateType258: set["jpdl31_ProcessStateType"] = None, jpdl31_SuperStateType261: set["jpdl31_ForkType"] = None, jpdl31_SuperStateType246: set["jpdl31_NodeType"] = None, jpdl31_SuperStateType249: set["jpdl31_StateType"] = None, jpdl31_SuperStateType252: set["jpdl31_TaskNodeType"] = None, jpdl31_SuperStateType256: "jpdl31_SuperStateType" = None, jpdl31_SuperStateType254: set["jpdl31_SuperStateType"] = None, jpdl31_SuperStateType270: set["jpdl31_EndStateType"] = None, jpdl31_SuperStateType264: set["jpdl31_JoinType"] = None, jpdl31_SuperStateType267: set["jpdl31_DecisionType"] = None, jpdl31_SuperStateType282: set["jpdl31_TransitionType"] = None, jpdl31_SuperStateType273: set["jpdl31_EventType"] = None, jpdl31_SuperStateType276: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_SuperStateType279: set["jpdl31_TimerType"] = None):
        self.group = group
        self.async = async
        self.name = name
        self.jpdl31_SuperStateType = jpdl31_SuperStateType
        self.jpdl31_SuperStateType167 = jpdl31_SuperStateType167
        self.jpdl31_SuperStateType258 = jpdl31_SuperStateType258 if jpdl31_SuperStateType258 is not None else set()
        self.jpdl31_SuperStateType261 = jpdl31_SuperStateType261 if jpdl31_SuperStateType261 is not None else set()
        self.jpdl31_SuperStateType246 = jpdl31_SuperStateType246 if jpdl31_SuperStateType246 is not None else set()
        self.jpdl31_SuperStateType249 = jpdl31_SuperStateType249 if jpdl31_SuperStateType249 is not None else set()
        self.jpdl31_SuperStateType252 = jpdl31_SuperStateType252 if jpdl31_SuperStateType252 is not None else set()
        self.jpdl31_SuperStateType256 = jpdl31_SuperStateType256
        self.jpdl31_SuperStateType254 = jpdl31_SuperStateType254 if jpdl31_SuperStateType254 is not None else set()
        self.jpdl31_SuperStateType270 = jpdl31_SuperStateType270 if jpdl31_SuperStateType270 is not None else set()
        self.jpdl31_SuperStateType264 = jpdl31_SuperStateType264 if jpdl31_SuperStateType264 is not None else set()
        self.jpdl31_SuperStateType267 = jpdl31_SuperStateType267 if jpdl31_SuperStateType267 is not None else set()
        self.jpdl31_SuperStateType282 = jpdl31_SuperStateType282 if jpdl31_SuperStateType282 is not None else set()
        self.jpdl31_SuperStateType273 = jpdl31_SuperStateType273 if jpdl31_SuperStateType273 is not None else set()
        self.jpdl31_SuperStateType276 = jpdl31_SuperStateType276 if jpdl31_SuperStateType276 is not None else set()
        self.jpdl31_SuperStateType279 = jpdl31_SuperStateType279 if jpdl31_SuperStateType279 is not None else set()
        
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
    def jpdl31_SuperStateType167(self):
        return self.__jpdl31_SuperStateType167

    @jpdl31_SuperStateType167.setter
    def jpdl31_SuperStateType167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType167", None)
        self.__jpdl31_SuperStateType167 = value
        
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
                if hasattr(item, "jpdl31_EndStateType271"):
                    opp_val = getattr(item, "jpdl31_EndStateType271", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EndStateType271", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EndStateType271"):
                    opp_val = getattr(item, "jpdl31_EndStateType271", None)
                    
                    setattr(item, "jpdl31_EndStateType271", self)
                    

    @property
    def jpdl31_SuperStateType279(self):
        return self.__jpdl31_SuperStateType279

    @jpdl31_SuperStateType279.setter
    def jpdl31_SuperStateType279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType279", None)
        self.__jpdl31_SuperStateType279 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType280"):
                    opp_val = getattr(item, "jpdl31_TimerType280", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType280", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType280"):
                    opp_val = getattr(item, "jpdl31_TimerType280", None)
                    
                    setattr(item, "jpdl31_TimerType280", self)
                    

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
                if hasattr(item, "jpdl31_JoinType265"):
                    opp_val = getattr(item, "jpdl31_JoinType265", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_JoinType265", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_JoinType265"):
                    opp_val = getattr(item, "jpdl31_JoinType265", None)
                    
                    setattr(item, "jpdl31_JoinType265", self)
                    

    @property
    def jpdl31_SuperStateType254(self):
        return self.__jpdl31_SuperStateType254

    @jpdl31_SuperStateType254.setter
    def jpdl31_SuperStateType254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType254", None)
        self.__jpdl31_SuperStateType254 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_SuperStateType256"):
                    opp_val = getattr(item, "jpdl31_SuperStateType256", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_SuperStateType256", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_SuperStateType256"):
                    opp_val = getattr(item, "jpdl31_SuperStateType256", None)
                    
                    setattr(item, "jpdl31_SuperStateType256", self)
                    

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
                if hasattr(item, "jpdl31_ExceptionHandlerType277"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType277", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType277", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType277"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType277", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType277", self)
                    

    @property
    def jpdl31_SuperStateType282(self):
        return self.__jpdl31_SuperStateType282

    @jpdl31_SuperStateType282.setter
    def jpdl31_SuperStateType282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType282", None)
        self.__jpdl31_SuperStateType282 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType283"):
                    opp_val = getattr(item, "jpdl31_TransitionType283", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType283", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType283"):
                    opp_val = getattr(item, "jpdl31_TransitionType283", None)
                    
                    setattr(item, "jpdl31_TransitionType283", self)
                    

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
                if hasattr(item, "jpdl31_DecisionType268"):
                    opp_val = getattr(item, "jpdl31_DecisionType268", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_DecisionType268", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_DecisionType268"):
                    opp_val = getattr(item, "jpdl31_DecisionType268", None)
                    
                    setattr(item, "jpdl31_DecisionType268", self)
                    

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
    def jpdl31_SuperStateType249(self):
        return self.__jpdl31_SuperStateType249

    @jpdl31_SuperStateType249.setter
    def jpdl31_SuperStateType249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType249", None)
        self.__jpdl31_SuperStateType249 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_StateType250"):
                    opp_val = getattr(item, "jpdl31_StateType250", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_StateType250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_StateType250"):
                    opp_val = getattr(item, "jpdl31_StateType250", None)
                    
                    setattr(item, "jpdl31_StateType250", self)
                    

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
                if hasattr(item, "jpdl31_ForkType262"):
                    opp_val = getattr(item, "jpdl31_ForkType262", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ForkType262", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ForkType262"):
                    opp_val = getattr(item, "jpdl31_ForkType262", None)
                    
                    setattr(item, "jpdl31_ForkType262", self)
                    

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
                if hasattr(item, "jpdl31_NodeType247"):
                    opp_val = getattr(item, "jpdl31_NodeType247", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_NodeType247", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_NodeType247"):
                    opp_val = getattr(item, "jpdl31_NodeType247", None)
                    
                    setattr(item, "jpdl31_NodeType247", self)
                    

    @property
    def jpdl31_SuperStateType256(self):
        return self.__jpdl31_SuperStateType256

    @jpdl31_SuperStateType256.setter
    def jpdl31_SuperStateType256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_SuperStateType__jpdl31_SuperStateType256", None)
        self.__jpdl31_SuperStateType256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SuperStateType254"):
                opp_val = getattr(old_value, "jpdl31_SuperStateType254", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SuperStateType254"):
                opp_val = getattr(value, "jpdl31_SuperStateType254", None)
                if opp_val is None:
                    setattr(value, "jpdl31_SuperStateType254", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "jpdl31_EventType274"):
                    opp_val = getattr(item, "jpdl31_EventType274", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType274", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType274"):
                    opp_val = getattr(item, "jpdl31_EventType274", None)
                    
                    setattr(item, "jpdl31_EventType274", self)
                    

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
                if hasattr(item, "jpdl31_TaskNodeType253"):
                    opp_val = getattr(item, "jpdl31_TaskNodeType253", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TaskNodeType253", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TaskNodeType253"):
                    opp_val = getattr(item, "jpdl31_TaskNodeType253", None)
                    
                    setattr(item, "jpdl31_TaskNodeType253", self)
                    

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
                if hasattr(item, "jpdl31_ProcessStateType259"):
                    opp_val = getattr(item, "jpdl31_ProcessStateType259", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ProcessStateType259", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ProcessStateType259"):
                    opp_val = getattr(item, "jpdl31_ProcessStateType259", None)
                    
                    setattr(item, "jpdl31_ProcessStateType259", self)
                    

class jpdl31_ProcessDefinitionType:

    def __init__(self, group: str, name: str, quantity: str, jpdl31_ProcessDefinitionType: "jpdl31_DocumentRoot" = None, jpdl31_ProcessDefinitionType151: set["jpdl31_SwimlaneType"] = None, jpdl31_ProcessDefinitionType163: set["jpdl31_TaskNodeType"] = None, jpdl31_ProcessDefinitionType166: set["jpdl31_SuperStateType"] = None, jpdl31_ProcessDefinitionType154: set["jpdl31_StartStateType"] = None, jpdl31_ProcessDefinitionType157: set["jpdl31_NodeType"] = None, jpdl31_ProcessDefinitionType160: set["jpdl31_StateType"] = None, jpdl31_ProcessDefinitionType178: set["jpdl31_DecisionType"] = None, jpdl31_ProcessDefinitionType169: set["jpdl31_ProcessStateType"] = None, jpdl31_ProcessDefinitionType172: set["jpdl31_ForkType"] = None, jpdl31_ProcessDefinitionType175: set["jpdl31_JoinType"] = None, jpdl31_ProcessDefinitionType190: set["jpdl31_CreateTimerType"] = None, jpdl31_ProcessDefinitionType193: set["jpdl31_CancelTimerType"] = None, jpdl31_ProcessDefinitionType181: set["jpdl31_EndStateType"] = None, jpdl31_ProcessDefinitionType184: set["jpdl31_ActionType"] = None, jpdl31_ProcessDefinitionType187: set["jpdl31_ScriptType"] = None, jpdl31_ProcessDefinitionType202: set["jpdl31_TaskType"] = None, jpdl31_ProcessDefinitionType196: set["jpdl31_EventType"] = None, jpdl31_ProcessDefinitionType199: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_ProcessDefinitionType387: "jpdl31_Metric" = None, jpdl31_ProcessDefinitionType392: "jpdl31_Questionnaire" = None):
        self.group = group
        self.name = name
        self.quantity = quantity
        self.jpdl31_ProcessDefinitionType = jpdl31_ProcessDefinitionType
        self.jpdl31_ProcessDefinitionType151 = jpdl31_ProcessDefinitionType151 if jpdl31_ProcessDefinitionType151 is not None else set()
        self.jpdl31_ProcessDefinitionType163 = jpdl31_ProcessDefinitionType163 if jpdl31_ProcessDefinitionType163 is not None else set()
        self.jpdl31_ProcessDefinitionType166 = jpdl31_ProcessDefinitionType166 if jpdl31_ProcessDefinitionType166 is not None else set()
        self.jpdl31_ProcessDefinitionType154 = jpdl31_ProcessDefinitionType154 if jpdl31_ProcessDefinitionType154 is not None else set()
        self.jpdl31_ProcessDefinitionType157 = jpdl31_ProcessDefinitionType157 if jpdl31_ProcessDefinitionType157 is not None else set()
        self.jpdl31_ProcessDefinitionType160 = jpdl31_ProcessDefinitionType160 if jpdl31_ProcessDefinitionType160 is not None else set()
        self.jpdl31_ProcessDefinitionType178 = jpdl31_ProcessDefinitionType178 if jpdl31_ProcessDefinitionType178 is not None else set()
        self.jpdl31_ProcessDefinitionType169 = jpdl31_ProcessDefinitionType169 if jpdl31_ProcessDefinitionType169 is not None else set()
        self.jpdl31_ProcessDefinitionType172 = jpdl31_ProcessDefinitionType172 if jpdl31_ProcessDefinitionType172 is not None else set()
        self.jpdl31_ProcessDefinitionType175 = jpdl31_ProcessDefinitionType175 if jpdl31_ProcessDefinitionType175 is not None else set()
        self.jpdl31_ProcessDefinitionType190 = jpdl31_ProcessDefinitionType190 if jpdl31_ProcessDefinitionType190 is not None else set()
        self.jpdl31_ProcessDefinitionType193 = jpdl31_ProcessDefinitionType193 if jpdl31_ProcessDefinitionType193 is not None else set()
        self.jpdl31_ProcessDefinitionType181 = jpdl31_ProcessDefinitionType181 if jpdl31_ProcessDefinitionType181 is not None else set()
        self.jpdl31_ProcessDefinitionType184 = jpdl31_ProcessDefinitionType184 if jpdl31_ProcessDefinitionType184 is not None else set()
        self.jpdl31_ProcessDefinitionType187 = jpdl31_ProcessDefinitionType187 if jpdl31_ProcessDefinitionType187 is not None else set()
        self.jpdl31_ProcessDefinitionType202 = jpdl31_ProcessDefinitionType202 if jpdl31_ProcessDefinitionType202 is not None else set()
        self.jpdl31_ProcessDefinitionType196 = jpdl31_ProcessDefinitionType196 if jpdl31_ProcessDefinitionType196 is not None else set()
        self.jpdl31_ProcessDefinitionType199 = jpdl31_ProcessDefinitionType199 if jpdl31_ProcessDefinitionType199 is not None else set()
        self.jpdl31_ProcessDefinitionType387 = jpdl31_ProcessDefinitionType387
        self.jpdl31_ProcessDefinitionType392 = jpdl31_ProcessDefinitionType392
        
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
    def quantity(self) -> str:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: str):
        self.__quantity = quantity

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
                if hasattr(item, "jpdl31_EndStateType182"):
                    opp_val = getattr(item, "jpdl31_EndStateType182", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EndStateType182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EndStateType182"):
                    opp_val = getattr(item, "jpdl31_EndStateType182", None)
                    
                    setattr(item, "jpdl31_EndStateType182", self)
                    

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
                if hasattr(item, "jpdl31_ProcessStateType170"):
                    opp_val = getattr(item, "jpdl31_ProcessStateType170", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ProcessStateType170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ProcessStateType170"):
                    opp_val = getattr(item, "jpdl31_ProcessStateType170", None)
                    
                    setattr(item, "jpdl31_ProcessStateType170", self)
                    

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
                if hasattr(item, "jpdl31_CreateTimerType191"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType191", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CreateTimerType191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CreateTimerType191"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType191", None)
                    
                    setattr(item, "jpdl31_CreateTimerType191", self)
                    

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
                if hasattr(item, "jpdl31_EventType197"):
                    opp_val = getattr(item, "jpdl31_EventType197", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType197", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType197"):
                    opp_val = getattr(item, "jpdl31_EventType197", None)
                    
                    setattr(item, "jpdl31_EventType197", self)
                    

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
                if hasattr(item, "jpdl31_ActionType185"):
                    opp_val = getattr(item, "jpdl31_ActionType185", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ActionType185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ActionType185"):
                    opp_val = getattr(item, "jpdl31_ActionType185", None)
                    
                    setattr(item, "jpdl31_ActionType185", self)
                    

    @property
    def jpdl31_ProcessDefinitionType199(self):
        return self.__jpdl31_ProcessDefinitionType199

    @jpdl31_ProcessDefinitionType199.setter
    def jpdl31_ProcessDefinitionType199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType199", None)
        self.__jpdl31_ProcessDefinitionType199 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType200"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType200", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType200", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType200"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType200", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType200", self)
                    

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
                if hasattr(item, "jpdl31_StateType161"):
                    opp_val = getattr(item, "jpdl31_StateType161", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_StateType161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_StateType161"):
                    opp_val = getattr(item, "jpdl31_StateType161", None)
                    
                    setattr(item, "jpdl31_StateType161", self)
                    

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
                if hasattr(item, "jpdl31_SuperStateType167"):
                    opp_val = getattr(item, "jpdl31_SuperStateType167", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_SuperStateType167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_SuperStateType167"):
                    opp_val = getattr(item, "jpdl31_SuperStateType167", None)
                    
                    setattr(item, "jpdl31_SuperStateType167", self)
                    

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
                if hasattr(item, "jpdl31_SwimlaneType152"):
                    opp_val = getattr(item, "jpdl31_SwimlaneType152", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_SwimlaneType152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_SwimlaneType152"):
                    opp_val = getattr(item, "jpdl31_SwimlaneType152", None)
                    
                    setattr(item, "jpdl31_SwimlaneType152", self)
                    

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
                if hasattr(item, "jpdl31_TaskNodeType164"):
                    opp_val = getattr(item, "jpdl31_TaskNodeType164", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TaskNodeType164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TaskNodeType164"):
                    opp_val = getattr(item, "jpdl31_TaskNodeType164", None)
                    
                    setattr(item, "jpdl31_TaskNodeType164", self)
                    

    @property
    def jpdl31_ProcessDefinitionType392(self):
        return self.__jpdl31_ProcessDefinitionType392

    @jpdl31_ProcessDefinitionType392.setter
    def jpdl31_ProcessDefinitionType392(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType392", None)
        self.__jpdl31_ProcessDefinitionType392 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Questionnaire391"):
                opp_val = getattr(old_value, "jpdl31_Questionnaire391", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Questionnaire391"):
                opp_val = getattr(value, "jpdl31_Questionnaire391", None)
                if opp_val is None:
                    setattr(value, "jpdl31_Questionnaire391", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ProcessDefinitionType202(self):
        return self.__jpdl31_ProcessDefinitionType202

    @jpdl31_ProcessDefinitionType202.setter
    def jpdl31_ProcessDefinitionType202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType202", None)
        self.__jpdl31_ProcessDefinitionType202 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TaskType203"):
                    opp_val = getattr(item, "jpdl31_TaskType203", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TaskType203", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TaskType203"):
                    opp_val = getattr(item, "jpdl31_TaskType203", None)
                    
                    setattr(item, "jpdl31_TaskType203", self)
                    

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
                if hasattr(item, "jpdl31_JoinType176"):
                    opp_val = getattr(item, "jpdl31_JoinType176", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_JoinType176", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_JoinType176"):
                    opp_val = getattr(item, "jpdl31_JoinType176", None)
                    
                    setattr(item, "jpdl31_JoinType176", self)
                    

    @property
    def jpdl31_ProcessDefinitionType387(self):
        return self.__jpdl31_ProcessDefinitionType387

    @jpdl31_ProcessDefinitionType387.setter
    def jpdl31_ProcessDefinitionType387(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessDefinitionType__jpdl31_ProcessDefinitionType387", None)
        self.__jpdl31_ProcessDefinitionType387 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Metric386"):
                opp_val = getattr(old_value, "jpdl31_Metric386", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Metric386"):
                opp_val = getattr(value, "jpdl31_Metric386", None)
                if opp_val is None:
                    setattr(value, "jpdl31_Metric386", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "jpdl31_DecisionType179"):
                    opp_val = getattr(item, "jpdl31_DecisionType179", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_DecisionType179", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_DecisionType179"):
                    opp_val = getattr(item, "jpdl31_DecisionType179", None)
                    
                    setattr(item, "jpdl31_DecisionType179", self)
                    

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
                if hasattr(item, "jpdl31_ForkType173"):
                    opp_val = getattr(item, "jpdl31_ForkType173", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ForkType173", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ForkType173"):
                    opp_val = getattr(item, "jpdl31_ForkType173", None)
                    
                    setattr(item, "jpdl31_ForkType173", self)
                    

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
                if hasattr(item, "jpdl31_CancelTimerType194"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType194", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CancelTimerType194", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CancelTimerType194"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType194", None)
                    
                    setattr(item, "jpdl31_CancelTimerType194", self)
                    

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
                if hasattr(item, "jpdl31_StartStateType155"):
                    opp_val = getattr(item, "jpdl31_StartStateType155", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_StartStateType155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_StartStateType155"):
                    opp_val = getattr(item, "jpdl31_StartStateType155", None)
                    
                    setattr(item, "jpdl31_StartStateType155", self)
                    

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
                if hasattr(item, "jpdl31_NodeType158"):
                    opp_val = getattr(item, "jpdl31_NodeType158", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_NodeType158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_NodeType158"):
                    opp_val = getattr(item, "jpdl31_NodeType158", None)
                    
                    setattr(item, "jpdl31_NodeType158", self)
                    

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
                if hasattr(item, "jpdl31_ScriptType188"):
                    opp_val = getattr(item, "jpdl31_ScriptType188", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ScriptType188", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ScriptType188"):
                    opp_val = getattr(item, "jpdl31_ScriptType188", None)
                    
                    setattr(item, "jpdl31_ScriptType188", self)
                    

class jpdl31_ProcessStateType:

    def __init__(self, group: str, async: str, name: str, jpdl31_ProcessStateType: "jpdl31_DocumentRoot" = None, jpdl31_ProcessStateType170: "jpdl31_ProcessDefinitionType" = None, jpdl31_ProcessStateType207: set["jpdl31_VariableType"] = None, jpdl31_ProcessStateType210: set["jpdl31_EventType"] = None, jpdl31_ProcessStateType205: set["jpdl31_SubProcessType"] = None, jpdl31_ProcessStateType213: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_ProcessStateType216: set["jpdl31_TimerType"] = None, jpdl31_ProcessStateType219: set["jpdl31_TransitionType"] = None, jpdl31_ProcessStateType259: "jpdl31_SuperStateType" = None):
        self.group = group
        self.async = async
        self.name = name
        self.jpdl31_ProcessStateType = jpdl31_ProcessStateType
        self.jpdl31_ProcessStateType170 = jpdl31_ProcessStateType170
        self.jpdl31_ProcessStateType207 = jpdl31_ProcessStateType207 if jpdl31_ProcessStateType207 is not None else set()
        self.jpdl31_ProcessStateType210 = jpdl31_ProcessStateType210 if jpdl31_ProcessStateType210 is not None else set()
        self.jpdl31_ProcessStateType205 = jpdl31_ProcessStateType205 if jpdl31_ProcessStateType205 is not None else set()
        self.jpdl31_ProcessStateType213 = jpdl31_ProcessStateType213 if jpdl31_ProcessStateType213 is not None else set()
        self.jpdl31_ProcessStateType216 = jpdl31_ProcessStateType216 if jpdl31_ProcessStateType216 is not None else set()
        self.jpdl31_ProcessStateType219 = jpdl31_ProcessStateType219 if jpdl31_ProcessStateType219 is not None else set()
        self.jpdl31_ProcessStateType259 = jpdl31_ProcessStateType259
        
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
    def jpdl31_ProcessStateType259(self):
        return self.__jpdl31_ProcessStateType259

    @jpdl31_ProcessStateType259.setter
    def jpdl31_ProcessStateType259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessStateType__jpdl31_ProcessStateType259", None)
        self.__jpdl31_ProcessStateType259 = value
        
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
    def jpdl31_ProcessStateType170(self):
        return self.__jpdl31_ProcessStateType170

    @jpdl31_ProcessStateType170.setter
    def jpdl31_ProcessStateType170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessStateType__jpdl31_ProcessStateType170", None)
        self.__jpdl31_ProcessStateType170 = value
        
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
    def jpdl31_ProcessStateType205(self):
        return self.__jpdl31_ProcessStateType205

    @jpdl31_ProcessStateType205.setter
    def jpdl31_ProcessStateType205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessStateType__jpdl31_ProcessStateType205", None)
        self.__jpdl31_ProcessStateType205 = value if value is not None else set()
        
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
                if hasattr(item, "jpdl31_VariableType208"):
                    opp_val = getattr(item, "jpdl31_VariableType208", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_VariableType208", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_VariableType208"):
                    opp_val = getattr(item, "jpdl31_VariableType208", None)
                    
                    setattr(item, "jpdl31_VariableType208", self)
                    

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
                if hasattr(item, "jpdl31_EventType211"):
                    opp_val = getattr(item, "jpdl31_EventType211", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType211"):
                    opp_val = getattr(item, "jpdl31_EventType211", None)
                    
                    setattr(item, "jpdl31_EventType211", self)
                    

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
    def jpdl31_ProcessStateType216(self):
        return self.__jpdl31_ProcessStateType216

    @jpdl31_ProcessStateType216.setter
    def jpdl31_ProcessStateType216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessStateType__jpdl31_ProcessStateType216", None)
        self.__jpdl31_ProcessStateType216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType217"):
                    opp_val = getattr(item, "jpdl31_TimerType217", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType217", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType217"):
                    opp_val = getattr(item, "jpdl31_TimerType217", None)
                    
                    setattr(item, "jpdl31_TimerType217", self)
                    

    @property
    def jpdl31_ProcessStateType219(self):
        return self.__jpdl31_ProcessStateType219

    @jpdl31_ProcessStateType219.setter
    def jpdl31_ProcessStateType219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ProcessStateType__jpdl31_ProcessStateType219", None)
        self.__jpdl31_ProcessStateType219 = value if value is not None else set()
        
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
                if hasattr(item, "jpdl31_ExceptionHandlerType214"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType214", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType214"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType214", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType214", self)
                    

class jpdl31_JoinType:

    def __init__(self, nodeContentElements: str, async: str, name: str, jpdl31_JoinType: "jpdl31_DocumentRoot" = None, jpdl31_JoinType124: set["jpdl31_TransitionType"] = None, jpdl31_JoinType115: set["jpdl31_EventType"] = None, jpdl31_JoinType118: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_JoinType121: set["jpdl31_TimerType"] = None, jpdl31_JoinType176: "jpdl31_ProcessDefinitionType" = None, jpdl31_JoinType265: "jpdl31_SuperStateType" = None):
        self.nodeContentElements = nodeContentElements
        self.async = async
        self.name = name
        self.jpdl31_JoinType = jpdl31_JoinType
        self.jpdl31_JoinType124 = jpdl31_JoinType124 if jpdl31_JoinType124 is not None else set()
        self.jpdl31_JoinType115 = jpdl31_JoinType115 if jpdl31_JoinType115 is not None else set()
        self.jpdl31_JoinType118 = jpdl31_JoinType118 if jpdl31_JoinType118 is not None else set()
        self.jpdl31_JoinType121 = jpdl31_JoinType121 if jpdl31_JoinType121 is not None else set()
        self.jpdl31_JoinType176 = jpdl31_JoinType176
        self.jpdl31_JoinType265 = jpdl31_JoinType265
        
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
                if hasattr(item, "jpdl31_ExceptionHandlerType119"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType119", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType119"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType119", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType119", self)
                    

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
                if hasattr(item, "jpdl31_EventType116"):
                    opp_val = getattr(item, "jpdl31_EventType116", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType116"):
                    opp_val = getattr(item, "jpdl31_EventType116", None)
                    
                    setattr(item, "jpdl31_EventType116", self)
                    

    @property
    def jpdl31_JoinType176(self):
        return self.__jpdl31_JoinType176

    @jpdl31_JoinType176.setter
    def jpdl31_JoinType176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_JoinType__jpdl31_JoinType176", None)
        self.__jpdl31_JoinType176 = value
        
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
    def jpdl31_JoinType121(self):
        return self.__jpdl31_JoinType121

    @jpdl31_JoinType121.setter
    def jpdl31_JoinType121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_JoinType__jpdl31_JoinType121", None)
        self.__jpdl31_JoinType121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType122"):
                    opp_val = getattr(item, "jpdl31_TimerType122", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType122"):
                    opp_val = getattr(item, "jpdl31_TimerType122", None)
                    
                    setattr(item, "jpdl31_TimerType122", self)
                    

    @property
    def jpdl31_JoinType124(self):
        return self.__jpdl31_JoinType124

    @jpdl31_JoinType124.setter
    def jpdl31_JoinType124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_JoinType__jpdl31_JoinType124", None)
        self.__jpdl31_JoinType124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType125"):
                    opp_val = getattr(item, "jpdl31_TransitionType125", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType125"):
                    opp_val = getattr(item, "jpdl31_TransitionType125", None)
                    
                    setattr(item, "jpdl31_TransitionType125", self)
                    

    @property
    def jpdl31_JoinType265(self):
        return self.__jpdl31_JoinType265

    @jpdl31_JoinType265.setter
    def jpdl31_JoinType265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_JoinType__jpdl31_JoinType265", None)
        self.__jpdl31_JoinType265 = value
        
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

class jpdl31_ForkType:

    def __init__(self, group: str, name: str, async: str, jpdl31_ForkType: "jpdl31_DocumentRoot" = None, jpdl31_ForkType103: set["jpdl31_EventType"] = None, jpdl31_ForkType106: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_ForkType100: set["jpdl31_ScriptType"] = None, jpdl31_ForkType109: set["jpdl31_TimerType"] = None, jpdl31_ForkType112: set["jpdl31_TransitionType"] = None, jpdl31_ForkType173: "jpdl31_ProcessDefinitionType" = None, jpdl31_ForkType262: "jpdl31_SuperStateType" = None):
        self.group = group
        self.name = name
        self.async = async
        self.jpdl31_ForkType = jpdl31_ForkType
        self.jpdl31_ForkType103 = jpdl31_ForkType103 if jpdl31_ForkType103 is not None else set()
        self.jpdl31_ForkType106 = jpdl31_ForkType106 if jpdl31_ForkType106 is not None else set()
        self.jpdl31_ForkType100 = jpdl31_ForkType100 if jpdl31_ForkType100 is not None else set()
        self.jpdl31_ForkType109 = jpdl31_ForkType109 if jpdl31_ForkType109 is not None else set()
        self.jpdl31_ForkType112 = jpdl31_ForkType112 if jpdl31_ForkType112 is not None else set()
        self.jpdl31_ForkType173 = jpdl31_ForkType173
        self.jpdl31_ForkType262 = jpdl31_ForkType262
        
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
                if hasattr(item, "jpdl31_ExceptionHandlerType107"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType107", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType107"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType107", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType107", self)
                    

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
                if hasattr(item, "jpdl31_ScriptType101"):
                    opp_val = getattr(item, "jpdl31_ScriptType101", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ScriptType101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ScriptType101"):
                    opp_val = getattr(item, "jpdl31_ScriptType101", None)
                    
                    setattr(item, "jpdl31_ScriptType101", self)
                    

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
                if hasattr(item, "jpdl31_EventType104"):
                    opp_val = getattr(item, "jpdl31_EventType104", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType104"):
                    opp_val = getattr(item, "jpdl31_EventType104", None)
                    
                    setattr(item, "jpdl31_EventType104", self)
                    

    @property
    def jpdl31_ForkType112(self):
        return self.__jpdl31_ForkType112

    @jpdl31_ForkType112.setter
    def jpdl31_ForkType112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ForkType__jpdl31_ForkType112", None)
        self.__jpdl31_ForkType112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType113"):
                    opp_val = getattr(item, "jpdl31_TransitionType113", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType113"):
                    opp_val = getattr(item, "jpdl31_TransitionType113", None)
                    
                    setattr(item, "jpdl31_TransitionType113", self)
                    

    @property
    def jpdl31_ForkType173(self):
        return self.__jpdl31_ForkType173

    @jpdl31_ForkType173.setter
    def jpdl31_ForkType173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ForkType__jpdl31_ForkType173", None)
        self.__jpdl31_ForkType173 = value
        
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

    @property
    def jpdl31_ForkType262(self):
        return self.__jpdl31_ForkType262

    @jpdl31_ForkType262.setter
    def jpdl31_ForkType262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ForkType__jpdl31_ForkType262", None)
        self.__jpdl31_ForkType262 = value
        
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
    def jpdl31_ForkType109(self):
        return self.__jpdl31_ForkType109

    @jpdl31_ForkType109.setter
    def jpdl31_ForkType109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ForkType__jpdl31_ForkType109", None)
        self.__jpdl31_ForkType109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType110"):
                    opp_val = getattr(item, "jpdl31_TimerType110", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType110"):
                    opp_val = getattr(item, "jpdl31_TimerType110", None)
                    
                    setattr(item, "jpdl31_TimerType110", self)
                    

class jpdl31_NodeType:

    def __init__(self, nodeContentElements: str, async: str, name: str, description: str, jpdl31_NodeType: "jpdl31_DocumentRoot" = None, jpdl31_NodeType136: "jpdl31_CancelTimerType" = None, jpdl31_NodeType139: set["jpdl31_EventType"] = None, jpdl31_NodeType127: "jpdl31_ActionType" = None, jpdl31_NodeType130: "jpdl31_ScriptType" = None, jpdl31_NodeType133: "jpdl31_CreateTimerType" = None, jpdl31_NodeType148: set["jpdl31_TransitionType"] = None, jpdl31_NodeType142: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_NodeType145: set["jpdl31_TimerType"] = None, jpdl31_NodeType158: "jpdl31_ProcessDefinitionType" = None, jpdl31_NodeType247: "jpdl31_SuperStateType" = None):
        self.nodeContentElements = nodeContentElements
        self.async = async
        self.name = name
        self.description = description
        self.jpdl31_NodeType = jpdl31_NodeType
        self.jpdl31_NodeType136 = jpdl31_NodeType136
        self.jpdl31_NodeType139 = jpdl31_NodeType139 if jpdl31_NodeType139 is not None else set()
        self.jpdl31_NodeType127 = jpdl31_NodeType127
        self.jpdl31_NodeType130 = jpdl31_NodeType130
        self.jpdl31_NodeType133 = jpdl31_NodeType133
        self.jpdl31_NodeType148 = jpdl31_NodeType148 if jpdl31_NodeType148 is not None else set()
        self.jpdl31_NodeType142 = jpdl31_NodeType142 if jpdl31_NodeType142 is not None else set()
        self.jpdl31_NodeType145 = jpdl31_NodeType145 if jpdl31_NodeType145 is not None else set()
        self.jpdl31_NodeType158 = jpdl31_NodeType158
        self.jpdl31_NodeType247 = jpdl31_NodeType247
        
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
    def jpdl31_NodeType148(self):
        return self.__jpdl31_NodeType148

    @jpdl31_NodeType148.setter
    def jpdl31_NodeType148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType148", None)
        self.__jpdl31_NodeType148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TransitionType149"):
                    opp_val = getattr(item, "jpdl31_TransitionType149", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TransitionType149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TransitionType149"):
                    opp_val = getattr(item, "jpdl31_TransitionType149", None)
                    
                    setattr(item, "jpdl31_TransitionType149", self)
                    

    @property
    def jpdl31_NodeType136(self):
        return self.__jpdl31_NodeType136

    @jpdl31_NodeType136.setter
    def jpdl31_NodeType136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType136", None)
        self.__jpdl31_NodeType136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_CancelTimerType137"):
                opp_val = getattr(old_value, "jpdl31_CancelTimerType137", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_CancelTimerType137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_CancelTimerType137"):
                opp_val = getattr(value, "jpdl31_CancelTimerType137", None)
                setattr(value, "jpdl31_CancelTimerType137", self)

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
            if hasattr(old_value, "jpdl31_ScriptType131"):
                opp_val = getattr(old_value, "jpdl31_ScriptType131", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_ScriptType131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ScriptType131"):
                opp_val = getattr(value, "jpdl31_ScriptType131", None)
                setattr(value, "jpdl31_ScriptType131", self)

    @property
    def jpdl31_NodeType145(self):
        return self.__jpdl31_NodeType145

    @jpdl31_NodeType145.setter
    def jpdl31_NodeType145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType145", None)
        self.__jpdl31_NodeType145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_TimerType146"):
                    opp_val = getattr(item, "jpdl31_TimerType146", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_TimerType146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_TimerType146"):
                    opp_val = getattr(item, "jpdl31_TimerType146", None)
                    
                    setattr(item, "jpdl31_TimerType146", self)
                    

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
            if hasattr(old_value, "jpdl31_ActionType128"):
                opp_val = getattr(old_value, "jpdl31_ActionType128", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_ActionType128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ActionType128"):
                opp_val = getattr(value, "jpdl31_ActionType128", None)
                setattr(value, "jpdl31_ActionType128", self)

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
                if hasattr(item, "jpdl31_ExceptionHandlerType143"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType143", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType143"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType143", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType143", self)
                    

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
                if hasattr(item, "jpdl31_EventType140"):
                    opp_val = getattr(item, "jpdl31_EventType140", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType140"):
                    opp_val = getattr(item, "jpdl31_EventType140", None)
                    
                    setattr(item, "jpdl31_EventType140", self)
                    

    @property
    def jpdl31_NodeType133(self):
        return self.__jpdl31_NodeType133

    @jpdl31_NodeType133.setter
    def jpdl31_NodeType133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType133", None)
        self.__jpdl31_NodeType133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_CreateTimerType134"):
                opp_val = getattr(old_value, "jpdl31_CreateTimerType134", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_CreateTimerType134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_CreateTimerType134"):
                opp_val = getattr(value, "jpdl31_CreateTimerType134", None)
                setattr(value, "jpdl31_CreateTimerType134", self)

    @property
    def jpdl31_NodeType247(self):
        return self.__jpdl31_NodeType247

    @jpdl31_NodeType247.setter
    def jpdl31_NodeType247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType247", None)
        self.__jpdl31_NodeType247 = value
        
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

    @property
    def jpdl31_NodeType158(self):
        return self.__jpdl31_NodeType158

    @jpdl31_NodeType158.setter
    def jpdl31_NodeType158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_NodeType__jpdl31_NodeType158", None)
        self.__jpdl31_NodeType158 = value
        
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

class jpdl31_EndStateType:

    def __init__(self, group: str, name: str, jpdl31_EndStateType: "jpdl31_DocumentRoot" = None, jpdl31_EndStateType76: set["jpdl31_EventType"] = None, jpdl31_EndStateType79: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_EndStateType182: "jpdl31_ProcessDefinitionType" = None, jpdl31_EndStateType271: "jpdl31_SuperStateType" = None):
        self.group = group
        self.name = name
        self.jpdl31_EndStateType = jpdl31_EndStateType
        self.jpdl31_EndStateType76 = jpdl31_EndStateType76 if jpdl31_EndStateType76 is not None else set()
        self.jpdl31_EndStateType79 = jpdl31_EndStateType79 if jpdl31_EndStateType79 is not None else set()
        self.jpdl31_EndStateType182 = jpdl31_EndStateType182
        self.jpdl31_EndStateType271 = jpdl31_EndStateType271
        
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
    def jpdl31_EndStateType79(self):
        return self.__jpdl31_EndStateType79

    @jpdl31_EndStateType79.setter
    def jpdl31_EndStateType79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EndStateType__jpdl31_EndStateType79", None)
        self.__jpdl31_EndStateType79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType80"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType80", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType80"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType80", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType80", self)
                    

    @property
    def jpdl31_EndStateType182(self):
        return self.__jpdl31_EndStateType182

    @jpdl31_EndStateType182.setter
    def jpdl31_EndStateType182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EndStateType__jpdl31_EndStateType182", None)
        self.__jpdl31_EndStateType182 = value
        
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

    @property
    def jpdl31_EndStateType271(self):
        return self.__jpdl31_EndStateType271

    @jpdl31_EndStateType271.setter
    def jpdl31_EndStateType271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EndStateType__jpdl31_EndStateType271", None)
        self.__jpdl31_EndStateType271 = value
        
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
    def jpdl31_EndStateType76(self):
        return self.__jpdl31_EndStateType76

    @jpdl31_EndStateType76.setter
    def jpdl31_EndStateType76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EndStateType__jpdl31_EndStateType76", None)
        self.__jpdl31_EndStateType76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_EventType77"):
                    opp_val = getattr(item, "jpdl31_EventType77", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_EventType77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_EventType77"):
                    opp_val = getattr(item, "jpdl31_EventType77", None)
                    
                    setattr(item, "jpdl31_EventType77", self)
                    

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

class jpdl31_EStringToStringMapEntry:

    pass
class jpdl31_DocumentRoot:

    def __init__(self, mixed: str, jpdl31_DocumentRoot12: set["jpdl31_EStringToStringMapEntry"] = None, jpdl31_DocumentRoot: set["jpdl31_EStringToStringMapEntry"] = None, jpdl31_DocumentRoot20: set["jpdl31_CancelTimerType"] = None, jpdl31_DocumentRoot15: set["jpdl31_ActionType"] = None, jpdl31_DocumentRoot18: set["jpdl31_AssignmentType"] = None, jpdl31_DocumentRoot28: set["jpdl31_DecisionType"] = None, jpdl31_DocumentRoot22: set["jpdl31_Delegation"] = None, jpdl31_DocumentRoot25: set["jpdl31_CreateTimerType"] = None, jpdl31_DocumentRoot31: set["jpdl31_EndStateType"] = None, jpdl31_DocumentRoot33: set["jpdl31_EventType"] = None, jpdl31_DocumentRoot36: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_DocumentRoot39: set["jpdl31_ForkType"] = None, jpdl31_DocumentRoot41: set["jpdl31_JoinType"] = None, jpdl31_DocumentRoot47: set["jpdl31_ProcessStateType"] = None, jpdl31_DocumentRoot43: set["jpdl31_NodeType"] = None, jpdl31_DocumentRoot45: set["jpdl31_ProcessDefinitionType"] = None, jpdl31_DocumentRoot56: set["jpdl31_SuperStateType"] = None, jpdl31_DocumentRoot49: set["jpdl31_ScriptType"] = None, jpdl31_DocumentRoot52: set["jpdl31_StartStateType"] = None, jpdl31_DocumentRoot54: set["jpdl31_StateType"] = None, jpdl31_DocumentRoot64: set["jpdl31_TimerType"] = None, jpdl31_DocumentRoot66: set["jpdl31_TransitionType"] = None, jpdl31_DocumentRoot58: set["jpdl31_SwimlaneType"] = None, jpdl31_DocumentRoot60: set["jpdl31_TaskType"] = None, jpdl31_DocumentRoot62: set["jpdl31_TaskNodeType"] = None, jpdl31_DocumentRoot68: set["jpdl31_VariableType"] = None, jpdl31_DocumentRoot70: set["jpdl31_Questionnaire"] = None, jpdl31_DocumentRoot72: set["jpdl31_ExperimentalPlan"] = None, jpdl31_DocumentRoot74: set["jpdl31_Metric"] = None, jpdl31_DocumentRoot363: "jpdl31_Model" = None):
        self.mixed = mixed
        self.jpdl31_DocumentRoot12 = jpdl31_DocumentRoot12 if jpdl31_DocumentRoot12 is not None else set()
        self.jpdl31_DocumentRoot = jpdl31_DocumentRoot if jpdl31_DocumentRoot is not None else set()
        self.jpdl31_DocumentRoot20 = jpdl31_DocumentRoot20 if jpdl31_DocumentRoot20 is not None else set()
        self.jpdl31_DocumentRoot15 = jpdl31_DocumentRoot15 if jpdl31_DocumentRoot15 is not None else set()
        self.jpdl31_DocumentRoot18 = jpdl31_DocumentRoot18 if jpdl31_DocumentRoot18 is not None else set()
        self.jpdl31_DocumentRoot28 = jpdl31_DocumentRoot28 if jpdl31_DocumentRoot28 is not None else set()
        self.jpdl31_DocumentRoot22 = jpdl31_DocumentRoot22 if jpdl31_DocumentRoot22 is not None else set()
        self.jpdl31_DocumentRoot25 = jpdl31_DocumentRoot25 if jpdl31_DocumentRoot25 is not None else set()
        self.jpdl31_DocumentRoot31 = jpdl31_DocumentRoot31 if jpdl31_DocumentRoot31 is not None else set()
        self.jpdl31_DocumentRoot33 = jpdl31_DocumentRoot33 if jpdl31_DocumentRoot33 is not None else set()
        self.jpdl31_DocumentRoot36 = jpdl31_DocumentRoot36 if jpdl31_DocumentRoot36 is not None else set()
        self.jpdl31_DocumentRoot39 = jpdl31_DocumentRoot39 if jpdl31_DocumentRoot39 is not None else set()
        self.jpdl31_DocumentRoot41 = jpdl31_DocumentRoot41 if jpdl31_DocumentRoot41 is not None else set()
        self.jpdl31_DocumentRoot47 = jpdl31_DocumentRoot47 if jpdl31_DocumentRoot47 is not None else set()
        self.jpdl31_DocumentRoot43 = jpdl31_DocumentRoot43 if jpdl31_DocumentRoot43 is not None else set()
        self.jpdl31_DocumentRoot45 = jpdl31_DocumentRoot45 if jpdl31_DocumentRoot45 is not None else set()
        self.jpdl31_DocumentRoot56 = jpdl31_DocumentRoot56 if jpdl31_DocumentRoot56 is not None else set()
        self.jpdl31_DocumentRoot49 = jpdl31_DocumentRoot49 if jpdl31_DocumentRoot49 is not None else set()
        self.jpdl31_DocumentRoot52 = jpdl31_DocumentRoot52 if jpdl31_DocumentRoot52 is not None else set()
        self.jpdl31_DocumentRoot54 = jpdl31_DocumentRoot54 if jpdl31_DocumentRoot54 is not None else set()
        self.jpdl31_DocumentRoot64 = jpdl31_DocumentRoot64 if jpdl31_DocumentRoot64 is not None else set()
        self.jpdl31_DocumentRoot66 = jpdl31_DocumentRoot66 if jpdl31_DocumentRoot66 is not None else set()
        self.jpdl31_DocumentRoot58 = jpdl31_DocumentRoot58 if jpdl31_DocumentRoot58 is not None else set()
        self.jpdl31_DocumentRoot60 = jpdl31_DocumentRoot60 if jpdl31_DocumentRoot60 is not None else set()
        self.jpdl31_DocumentRoot62 = jpdl31_DocumentRoot62 if jpdl31_DocumentRoot62 is not None else set()
        self.jpdl31_DocumentRoot68 = jpdl31_DocumentRoot68 if jpdl31_DocumentRoot68 is not None else set()
        self.jpdl31_DocumentRoot70 = jpdl31_DocumentRoot70 if jpdl31_DocumentRoot70 is not None else set()
        self.jpdl31_DocumentRoot72 = jpdl31_DocumentRoot72 if jpdl31_DocumentRoot72 is not None else set()
        self.jpdl31_DocumentRoot74 = jpdl31_DocumentRoot74 if jpdl31_DocumentRoot74 is not None else set()
        self.jpdl31_DocumentRoot363 = jpdl31_DocumentRoot363
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

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
    def jpdl31_DocumentRoot72(self):
        return self.__jpdl31_DocumentRoot72

    @jpdl31_DocumentRoot72.setter
    def jpdl31_DocumentRoot72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot72", None)
        self.__jpdl31_DocumentRoot72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExperimentalPlan"):
                    opp_val = getattr(item, "jpdl31_ExperimentalPlan", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExperimentalPlan", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExperimentalPlan"):
                    opp_val = getattr(item, "jpdl31_ExperimentalPlan", None)
                    
                    setattr(item, "jpdl31_ExperimentalPlan", self)
                    

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
    def jpdl31_DocumentRoot70(self):
        return self.__jpdl31_DocumentRoot70

    @jpdl31_DocumentRoot70.setter
    def jpdl31_DocumentRoot70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot70", None)
        self.__jpdl31_DocumentRoot70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Questionnaire"):
                    opp_val = getattr(item, "jpdl31_Questionnaire", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Questionnaire", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Questionnaire"):
                    opp_val = getattr(item, "jpdl31_Questionnaire", None)
                    
                    setattr(item, "jpdl31_Questionnaire", self)
                    

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
    def jpdl31_DocumentRoot363(self):
        return self.__jpdl31_DocumentRoot363

    @jpdl31_DocumentRoot363.setter
    def jpdl31_DocumentRoot363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot363", None)
        self.__jpdl31_DocumentRoot363 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_Model"):
                opp_val = getattr(old_value, "jpdl31_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_Model"):
                opp_val = getattr(value, "jpdl31_Model", None)
                if opp_val is None:
                    setattr(value, "jpdl31_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def jpdl31_DocumentRoot74(self):
        return self.__jpdl31_DocumentRoot74

    @jpdl31_DocumentRoot74.setter
    def jpdl31_DocumentRoot74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DocumentRoot__jpdl31_DocumentRoot74", None)
        self.__jpdl31_DocumentRoot74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_Metric"):
                    opp_val = getattr(item, "jpdl31_Metric", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_Metric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_Metric"):
                    opp_val = getattr(item, "jpdl31_Metric", None)
                    
                    setattr(item, "jpdl31_Metric", self)
                    

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
                    

class jpdl31_TransitionType1:

    def __init__(self, group: str, name: str, to: str, jpdl31_TransitionType1: "jpdl31_DecisionType" = None, jpdl31_TransitionType1348: set["jpdl31_ActionType"] = None, jpdl31_TransitionType1346: set["jpdl31_ConditionType"] = None, jpdl31_TransitionType1357: set["jpdl31_CancelTimerType"] = None, jpdl31_TransitionType1351: set["jpdl31_ScriptType"] = None, jpdl31_TransitionType1354: set["jpdl31_CreateTimerType"] = None, jpdl31_TransitionType1360: set["jpdl31_ExceptionHandlerType"] = None):
        self.group = group
        self.name = name
        self.to = to
        self.jpdl31_TransitionType1 = jpdl31_TransitionType1
        self.jpdl31_TransitionType1348 = jpdl31_TransitionType1348 if jpdl31_TransitionType1348 is not None else set()
        self.jpdl31_TransitionType1346 = jpdl31_TransitionType1346 if jpdl31_TransitionType1346 is not None else set()
        self.jpdl31_TransitionType1357 = jpdl31_TransitionType1357 if jpdl31_TransitionType1357 is not None else set()
        self.jpdl31_TransitionType1351 = jpdl31_TransitionType1351 if jpdl31_TransitionType1351 is not None else set()
        self.jpdl31_TransitionType1354 = jpdl31_TransitionType1354 if jpdl31_TransitionType1354 is not None else set()
        self.jpdl31_TransitionType1360 = jpdl31_TransitionType1360 if jpdl31_TransitionType1360 is not None else set()
        
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
    def jpdl31_TransitionType1348(self):
        return self.__jpdl31_TransitionType1348

    @jpdl31_TransitionType1348.setter
    def jpdl31_TransitionType1348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType1__jpdl31_TransitionType1348", None)
        self.__jpdl31_TransitionType1348 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ActionType349"):
                    opp_val = getattr(item, "jpdl31_ActionType349", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ActionType349", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ActionType349"):
                    opp_val = getattr(item, "jpdl31_ActionType349", None)
                    
                    setattr(item, "jpdl31_ActionType349", self)
                    

    @property
    def jpdl31_TransitionType1346(self):
        return self.__jpdl31_TransitionType1346

    @jpdl31_TransitionType1346.setter
    def jpdl31_TransitionType1346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType1__jpdl31_TransitionType1346", None)
        self.__jpdl31_TransitionType1346 = value if value is not None else set()
        
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
    def jpdl31_TransitionType1360(self):
        return self.__jpdl31_TransitionType1360

    @jpdl31_TransitionType1360.setter
    def jpdl31_TransitionType1360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType1__jpdl31_TransitionType1360", None)
        self.__jpdl31_TransitionType1360 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ExceptionHandlerType361"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType361", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ExceptionHandlerType361", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ExceptionHandlerType361"):
                    opp_val = getattr(item, "jpdl31_ExceptionHandlerType361", None)
                    
                    setattr(item, "jpdl31_ExceptionHandlerType361", self)
                    

    @property
    def jpdl31_TransitionType1357(self):
        return self.__jpdl31_TransitionType1357

    @jpdl31_TransitionType1357.setter
    def jpdl31_TransitionType1357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType1__jpdl31_TransitionType1357", None)
        self.__jpdl31_TransitionType1357 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CancelTimerType358"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType358", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CancelTimerType358", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CancelTimerType358"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType358", None)
                    
                    setattr(item, "jpdl31_CancelTimerType358", self)
                    

    @property
    def jpdl31_TransitionType1351(self):
        return self.__jpdl31_TransitionType1351

    @jpdl31_TransitionType1351.setter
    def jpdl31_TransitionType1351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType1__jpdl31_TransitionType1351", None)
        self.__jpdl31_TransitionType1351 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ScriptType352"):
                    opp_val = getattr(item, "jpdl31_ScriptType352", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ScriptType352", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ScriptType352"):
                    opp_val = getattr(item, "jpdl31_ScriptType352", None)
                    
                    setattr(item, "jpdl31_ScriptType352", self)
                    

    @property
    def jpdl31_TransitionType1354(self):
        return self.__jpdl31_TransitionType1354

    @jpdl31_TransitionType1354.setter
    def jpdl31_TransitionType1354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_TransitionType1__jpdl31_TransitionType1354", None)
        self.__jpdl31_TransitionType1354 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CreateTimerType355"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType355", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CreateTimerType355", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CreateTimerType355"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType355", None)
                    
                    setattr(item, "jpdl31_CreateTimerType355", self)
                    

class jpdl31_EventType:

    def __init__(self, actionElements: str, type: str, jpdl31_EventType: "jpdl31_DecisionType" = None, jpdl31_EventType34: "jpdl31_DocumentRoot" = None, jpdl31_EventType77: "jpdl31_EndStateType" = None, jpdl31_EventType82: set["jpdl31_ActionType"] = None, jpdl31_EventType85: set["jpdl31_ScriptType"] = None, jpdl31_EventType88: set["jpdl31_CreateTimerType"] = None, jpdl31_EventType91: set["jpdl31_CancelTimerType"] = None, jpdl31_EventType104: "jpdl31_ForkType" = None, jpdl31_EventType116: "jpdl31_JoinType" = None, jpdl31_EventType140: "jpdl31_NodeType" = None, jpdl31_EventType197: "jpdl31_ProcessDefinitionType" = None, jpdl31_EventType211: "jpdl31_ProcessStateType" = None, jpdl31_EventType229: "jpdl31_StartStateType" = None, jpdl31_EventType235: "jpdl31_StateType" = None, jpdl31_EventType274: "jpdl31_SuperStateType" = None, jpdl31_EventType292: "jpdl31_TaskNodeType" = None, jpdl31_EventType314: "jpdl31_TaskType" = None):
        self.actionElements = actionElements
        self.type = type
        self.jpdl31_EventType = jpdl31_EventType
        self.jpdl31_EventType34 = jpdl31_EventType34
        self.jpdl31_EventType77 = jpdl31_EventType77
        self.jpdl31_EventType82 = jpdl31_EventType82 if jpdl31_EventType82 is not None else set()
        self.jpdl31_EventType85 = jpdl31_EventType85 if jpdl31_EventType85 is not None else set()
        self.jpdl31_EventType88 = jpdl31_EventType88 if jpdl31_EventType88 is not None else set()
        self.jpdl31_EventType91 = jpdl31_EventType91 if jpdl31_EventType91 is not None else set()
        self.jpdl31_EventType104 = jpdl31_EventType104
        self.jpdl31_EventType116 = jpdl31_EventType116
        self.jpdl31_EventType140 = jpdl31_EventType140
        self.jpdl31_EventType197 = jpdl31_EventType197
        self.jpdl31_EventType211 = jpdl31_EventType211
        self.jpdl31_EventType229 = jpdl31_EventType229
        self.jpdl31_EventType235 = jpdl31_EventType235
        self.jpdl31_EventType274 = jpdl31_EventType274
        self.jpdl31_EventType292 = jpdl31_EventType292
        self.jpdl31_EventType314 = jpdl31_EventType314
        
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
    def jpdl31_EventType140(self):
        return self.__jpdl31_EventType140

    @jpdl31_EventType140.setter
    def jpdl31_EventType140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType140", None)
        self.__jpdl31_EventType140 = value
        
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
    def jpdl31_EventType274(self):
        return self.__jpdl31_EventType274

    @jpdl31_EventType274.setter
    def jpdl31_EventType274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType274", None)
        self.__jpdl31_EventType274 = value
        
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
                if hasattr(item, "jpdl31_ActionType83"):
                    opp_val = getattr(item, "jpdl31_ActionType83", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ActionType83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ActionType83"):
                    opp_val = getattr(item, "jpdl31_ActionType83", None)
                    
                    setattr(item, "jpdl31_ActionType83", self)
                    

    @property
    def jpdl31_EventType104(self):
        return self.__jpdl31_EventType104

    @jpdl31_EventType104.setter
    def jpdl31_EventType104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType104", None)
        self.__jpdl31_EventType104 = value
        
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
    def jpdl31_EventType235(self):
        return self.__jpdl31_EventType235

    @jpdl31_EventType235.setter
    def jpdl31_EventType235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType235", None)
        self.__jpdl31_EventType235 = value
        
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
    def jpdl31_EventType314(self):
        return self.__jpdl31_EventType314

    @jpdl31_EventType314.setter
    def jpdl31_EventType314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType314", None)
        self.__jpdl31_EventType314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskType313"):
                opp_val = getattr(old_value, "jpdl31_TaskType313", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskType313"):
                opp_val = getattr(value, "jpdl31_TaskType313", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskType313", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EventType211(self):
        return self.__jpdl31_EventType211

    @jpdl31_EventType211.setter
    def jpdl31_EventType211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType211", None)
        self.__jpdl31_EventType211 = value
        
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
    def jpdl31_EventType229(self):
        return self.__jpdl31_EventType229

    @jpdl31_EventType229.setter
    def jpdl31_EventType229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType229", None)
        self.__jpdl31_EventType229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_StartStateType228"):
                opp_val = getattr(old_value, "jpdl31_StartStateType228", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_StartStateType228"):
                opp_val = getattr(value, "jpdl31_StartStateType228", None)
                if opp_val is None:
                    setattr(value, "jpdl31_StartStateType228", set([self]))
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
                if hasattr(item, "jpdl31_ScriptType86"):
                    opp_val = getattr(item, "jpdl31_ScriptType86", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ScriptType86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ScriptType86"):
                    opp_val = getattr(item, "jpdl31_ScriptType86", None)
                    
                    setattr(item, "jpdl31_ScriptType86", self)
                    

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
    def jpdl31_EventType77(self):
        return self.__jpdl31_EventType77

    @jpdl31_EventType77.setter
    def jpdl31_EventType77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType77", None)
        self.__jpdl31_EventType77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_EndStateType76"):
                opp_val = getattr(old_value, "jpdl31_EndStateType76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_EndStateType76"):
                opp_val = getattr(value, "jpdl31_EndStateType76", None)
                if opp_val is None:
                    setattr(value, "jpdl31_EndStateType76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_EventType91(self):
        return self.__jpdl31_EventType91

    @jpdl31_EventType91.setter
    def jpdl31_EventType91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType91", None)
        self.__jpdl31_EventType91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CancelTimerType92"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType92", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CancelTimerType92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CancelTimerType92"):
                    opp_val = getattr(item, "jpdl31_CancelTimerType92", None)
                    
                    setattr(item, "jpdl31_CancelTimerType92", self)
                    

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
    def jpdl31_EventType197(self):
        return self.__jpdl31_EventType197

    @jpdl31_EventType197.setter
    def jpdl31_EventType197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType197", None)
        self.__jpdl31_EventType197 = value
        
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
    def jpdl31_EventType292(self):
        return self.__jpdl31_EventType292

    @jpdl31_EventType292.setter
    def jpdl31_EventType292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType292", None)
        self.__jpdl31_EventType292 = value
        
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
    def jpdl31_EventType88(self):
        return self.__jpdl31_EventType88

    @jpdl31_EventType88.setter
    def jpdl31_EventType88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType88", None)
        self.__jpdl31_EventType88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_CreateTimerType89"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType89", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_CreateTimerType89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_CreateTimerType89"):
                    opp_val = getattr(item, "jpdl31_CreateTimerType89", None)
                    
                    setattr(item, "jpdl31_CreateTimerType89", self)
                    

    @property
    def jpdl31_EventType116(self):
        return self.__jpdl31_EventType116

    @jpdl31_EventType116.setter
    def jpdl31_EventType116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_EventType__jpdl31_EventType116", None)
        self.__jpdl31_EventType116 = value
        
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

class jpdl31_Delegation:

    def __init__(self, class: str, mixed: str, any: str, configType: str, jpdl31_Delegation: "jpdl31_DecisionType" = None, jpdl31_Delegation23: "jpdl31_DocumentRoot" = None, jpdl31_Delegation311: "jpdl31_TaskType" = None):
        self.class = class
        self.mixed = mixed
        self.any = any
        self.configType = configType
        self.jpdl31_Delegation = jpdl31_Delegation
        self.jpdl31_Delegation23 = jpdl31_Delegation23
        self.jpdl31_Delegation311 = jpdl31_Delegation311
        
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
    def jpdl31_Delegation311(self):
        return self.__jpdl31_Delegation311

    @jpdl31_Delegation311.setter
    def jpdl31_Delegation311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_Delegation__jpdl31_Delegation311", None)
        self.__jpdl31_Delegation311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskType310"):
                opp_val = getattr(old_value, "jpdl31_TaskType310", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskType310"):
                opp_val = getattr(value, "jpdl31_TaskType310", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskType310", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_ExceptionHandlerType:

    def __init__(self, group: str, exceptionClass: str, jpdl31_ExceptionHandlerType: "jpdl31_DecisionType" = None, jpdl31_ExceptionHandlerType37: "jpdl31_DocumentRoot" = None, jpdl31_ExceptionHandlerType80: "jpdl31_EndStateType" = None, jpdl31_ExceptionHandlerType94: set["jpdl31_ActionType"] = None, jpdl31_ExceptionHandlerType107: "jpdl31_ForkType" = None, jpdl31_ExceptionHandlerType97: set["jpdl31_ScriptType"] = None, jpdl31_ExceptionHandlerType119: "jpdl31_JoinType" = None, jpdl31_ExceptionHandlerType143: "jpdl31_NodeType" = None, jpdl31_ExceptionHandlerType200: "jpdl31_ProcessDefinitionType" = None, jpdl31_ExceptionHandlerType214: "jpdl31_ProcessStateType" = None, jpdl31_ExceptionHandlerType232: "jpdl31_StartStateType" = None, jpdl31_ExceptionHandlerType238: "jpdl31_StateType" = None, jpdl31_ExceptionHandlerType277: "jpdl31_SuperStateType" = None, jpdl31_ExceptionHandlerType295: "jpdl31_TaskNodeType" = None, jpdl31_ExceptionHandlerType344: "jpdl31_TransitionType" = None, jpdl31_ExceptionHandlerType361: "jpdl31_TransitionType1" = None):
        self.group = group
        self.exceptionClass = exceptionClass
        self.jpdl31_ExceptionHandlerType = jpdl31_ExceptionHandlerType
        self.jpdl31_ExceptionHandlerType37 = jpdl31_ExceptionHandlerType37
        self.jpdl31_ExceptionHandlerType80 = jpdl31_ExceptionHandlerType80
        self.jpdl31_ExceptionHandlerType94 = jpdl31_ExceptionHandlerType94 if jpdl31_ExceptionHandlerType94 is not None else set()
        self.jpdl31_ExceptionHandlerType107 = jpdl31_ExceptionHandlerType107
        self.jpdl31_ExceptionHandlerType97 = jpdl31_ExceptionHandlerType97 if jpdl31_ExceptionHandlerType97 is not None else set()
        self.jpdl31_ExceptionHandlerType119 = jpdl31_ExceptionHandlerType119
        self.jpdl31_ExceptionHandlerType143 = jpdl31_ExceptionHandlerType143
        self.jpdl31_ExceptionHandlerType200 = jpdl31_ExceptionHandlerType200
        self.jpdl31_ExceptionHandlerType214 = jpdl31_ExceptionHandlerType214
        self.jpdl31_ExceptionHandlerType232 = jpdl31_ExceptionHandlerType232
        self.jpdl31_ExceptionHandlerType238 = jpdl31_ExceptionHandlerType238
        self.jpdl31_ExceptionHandlerType277 = jpdl31_ExceptionHandlerType277
        self.jpdl31_ExceptionHandlerType295 = jpdl31_ExceptionHandlerType295
        self.jpdl31_ExceptionHandlerType344 = jpdl31_ExceptionHandlerType344
        self.jpdl31_ExceptionHandlerType361 = jpdl31_ExceptionHandlerType361
        
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
    def jpdl31_ExceptionHandlerType119(self):
        return self.__jpdl31_ExceptionHandlerType119

    @jpdl31_ExceptionHandlerType119.setter
    def jpdl31_ExceptionHandlerType119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType119", None)
        self.__jpdl31_ExceptionHandlerType119 = value
        
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
    def jpdl31_ExceptionHandlerType344(self):
        return self.__jpdl31_ExceptionHandlerType344

    @jpdl31_ExceptionHandlerType344.setter
    def jpdl31_ExceptionHandlerType344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType344", None)
        self.__jpdl31_ExceptionHandlerType344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType343"):
                opp_val = getattr(old_value, "jpdl31_TransitionType343", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType343"):
                opp_val = getattr(value, "jpdl31_TransitionType343", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType343", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType143(self):
        return self.__jpdl31_ExceptionHandlerType143

    @jpdl31_ExceptionHandlerType143.setter
    def jpdl31_ExceptionHandlerType143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType143", None)
        self.__jpdl31_ExceptionHandlerType143 = value
        
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
    def jpdl31_ExceptionHandlerType232(self):
        return self.__jpdl31_ExceptionHandlerType232

    @jpdl31_ExceptionHandlerType232.setter
    def jpdl31_ExceptionHandlerType232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType232", None)
        self.__jpdl31_ExceptionHandlerType232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_StartStateType231"):
                opp_val = getattr(old_value, "jpdl31_StartStateType231", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_StartStateType231"):
                opp_val = getattr(value, "jpdl31_StartStateType231", None)
                if opp_val is None:
                    setattr(value, "jpdl31_StartStateType231", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType361(self):
        return self.__jpdl31_ExceptionHandlerType361

    @jpdl31_ExceptionHandlerType361.setter
    def jpdl31_ExceptionHandlerType361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType361", None)
        self.__jpdl31_ExceptionHandlerType361 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType1360"):
                opp_val = getattr(old_value, "jpdl31_TransitionType1360", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType1360"):
                opp_val = getattr(value, "jpdl31_TransitionType1360", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType1360", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType238(self):
        return self.__jpdl31_ExceptionHandlerType238

    @jpdl31_ExceptionHandlerType238.setter
    def jpdl31_ExceptionHandlerType238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType238", None)
        self.__jpdl31_ExceptionHandlerType238 = value
        
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
    def jpdl31_ExceptionHandlerType214(self):
        return self.__jpdl31_ExceptionHandlerType214

    @jpdl31_ExceptionHandlerType214.setter
    def jpdl31_ExceptionHandlerType214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType214", None)
        self.__jpdl31_ExceptionHandlerType214 = value
        
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
    def jpdl31_ExceptionHandlerType277(self):
        return self.__jpdl31_ExceptionHandlerType277

    @jpdl31_ExceptionHandlerType277.setter
    def jpdl31_ExceptionHandlerType277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType277", None)
        self.__jpdl31_ExceptionHandlerType277 = value
        
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
    def jpdl31_ExceptionHandlerType200(self):
        return self.__jpdl31_ExceptionHandlerType200

    @jpdl31_ExceptionHandlerType200.setter
    def jpdl31_ExceptionHandlerType200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType200", None)
        self.__jpdl31_ExceptionHandlerType200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ProcessDefinitionType199"):
                opp_val = getattr(old_value, "jpdl31_ProcessDefinitionType199", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ProcessDefinitionType199"):
                opp_val = getattr(value, "jpdl31_ProcessDefinitionType199", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ProcessDefinitionType199", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType97(self):
        return self.__jpdl31_ExceptionHandlerType97

    @jpdl31_ExceptionHandlerType97.setter
    def jpdl31_ExceptionHandlerType97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType97", None)
        self.__jpdl31_ExceptionHandlerType97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ScriptType98"):
                    opp_val = getattr(item, "jpdl31_ScriptType98", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ScriptType98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ScriptType98"):
                    opp_val = getattr(item, "jpdl31_ScriptType98", None)
                    
                    setattr(item, "jpdl31_ScriptType98", self)
                    

    @property
    def jpdl31_ExceptionHandlerType94(self):
        return self.__jpdl31_ExceptionHandlerType94

    @jpdl31_ExceptionHandlerType94.setter
    def jpdl31_ExceptionHandlerType94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType94", None)
        self.__jpdl31_ExceptionHandlerType94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpdl31_ActionType95"):
                    opp_val = getattr(item, "jpdl31_ActionType95", None)
                    
                    if opp_val == self:
                        setattr(item, "jpdl31_ActionType95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpdl31_ActionType95"):
                    opp_val = getattr(item, "jpdl31_ActionType95", None)
                    
                    setattr(item, "jpdl31_ActionType95", self)
                    

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
    def jpdl31_ExceptionHandlerType80(self):
        return self.__jpdl31_ExceptionHandlerType80

    @jpdl31_ExceptionHandlerType80.setter
    def jpdl31_ExceptionHandlerType80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType80", None)
        self.__jpdl31_ExceptionHandlerType80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_EndStateType79"):
                opp_val = getattr(old_value, "jpdl31_EndStateType79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_EndStateType79"):
                opp_val = getattr(value, "jpdl31_EndStateType79", None)
                if opp_val is None:
                    setattr(value, "jpdl31_EndStateType79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ExceptionHandlerType295(self):
        return self.__jpdl31_ExceptionHandlerType295

    @jpdl31_ExceptionHandlerType295.setter
    def jpdl31_ExceptionHandlerType295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType295", None)
        self.__jpdl31_ExceptionHandlerType295 = value
        
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
    def jpdl31_ExceptionHandlerType107(self):
        return self.__jpdl31_ExceptionHandlerType107

    @jpdl31_ExceptionHandlerType107.setter
    def jpdl31_ExceptionHandlerType107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ExceptionHandlerType__jpdl31_ExceptionHandlerType107", None)
        self.__jpdl31_ExceptionHandlerType107 = value
        
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

class jpdl31_DecisionType:

    def __init__(self, group: str, async: str, expression: str, name: str, jpdl31_DecisionType7: set["jpdl31_ExceptionHandlerType"] = None, jpdl31_DecisionType: set["jpdl31_Delegation"] = None, jpdl31_DecisionType5: set["jpdl31_EventType"] = None, jpdl31_DecisionType9: set["jpdl31_TransitionType1"] = None, jpdl31_DecisionType29: "jpdl31_DocumentRoot" = None, jpdl31_DecisionType179: "jpdl31_ProcessDefinitionType" = None, jpdl31_DecisionType268: "jpdl31_SuperStateType" = None):
        self.group = group
        self.async = async
        self.expression = expression
        self.name = name
        self.jpdl31_DecisionType7 = jpdl31_DecisionType7 if jpdl31_DecisionType7 is not None else set()
        self.jpdl31_DecisionType = jpdl31_DecisionType if jpdl31_DecisionType is not None else set()
        self.jpdl31_DecisionType5 = jpdl31_DecisionType5 if jpdl31_DecisionType5 is not None else set()
        self.jpdl31_DecisionType9 = jpdl31_DecisionType9 if jpdl31_DecisionType9 is not None else set()
        self.jpdl31_DecisionType29 = jpdl31_DecisionType29
        self.jpdl31_DecisionType179 = jpdl31_DecisionType179
        self.jpdl31_DecisionType268 = jpdl31_DecisionType268
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

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
    def jpdl31_DecisionType268(self):
        return self.__jpdl31_DecisionType268

    @jpdl31_DecisionType268.setter
    def jpdl31_DecisionType268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DecisionType__jpdl31_DecisionType268", None)
        self.__jpdl31_DecisionType268 = value
        
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
    def jpdl31_DecisionType179(self):
        return self.__jpdl31_DecisionType179

    @jpdl31_DecisionType179.setter
    def jpdl31_DecisionType179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_DecisionType__jpdl31_DecisionType179", None)
        self.__jpdl31_DecisionType179 = value
        
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

class jpdl31_ScriptType:

    def __init__(self, mixed: str, any: str, acceptPropagatedEvents: str, name: str, jpdl31_ScriptType: "jpdl31_CreateTimerType" = None, jpdl31_ScriptType50: "jpdl31_DocumentRoot" = None, jpdl31_ScriptType86: "jpdl31_EventType" = None, jpdl31_ScriptType98: "jpdl31_ExceptionHandlerType" = None, jpdl31_ScriptType101: "jpdl31_ForkType" = None, jpdl31_ScriptType131: "jpdl31_NodeType" = None, jpdl31_ScriptType188: "jpdl31_ProcessDefinitionType" = None, jpdl31_ScriptType329: "jpdl31_TimerType" = None, jpdl31_ScriptType335: "jpdl31_TransitionType" = None, jpdl31_ScriptType352: "jpdl31_TransitionType1" = None):
        self.mixed = mixed
        self.any = any
        self.acceptPropagatedEvents = acceptPropagatedEvents
        self.name = name
        self.jpdl31_ScriptType = jpdl31_ScriptType
        self.jpdl31_ScriptType50 = jpdl31_ScriptType50
        self.jpdl31_ScriptType86 = jpdl31_ScriptType86
        self.jpdl31_ScriptType98 = jpdl31_ScriptType98
        self.jpdl31_ScriptType101 = jpdl31_ScriptType101
        self.jpdl31_ScriptType131 = jpdl31_ScriptType131
        self.jpdl31_ScriptType188 = jpdl31_ScriptType188
        self.jpdl31_ScriptType329 = jpdl31_ScriptType329
        self.jpdl31_ScriptType335 = jpdl31_ScriptType335
        self.jpdl31_ScriptType352 = jpdl31_ScriptType352
        
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
    def jpdl31_ScriptType86(self):
        return self.__jpdl31_ScriptType86

    @jpdl31_ScriptType86.setter
    def jpdl31_ScriptType86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType86", None)
        self.__jpdl31_ScriptType86 = value
        
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
    def jpdl31_ScriptType352(self):
        return self.__jpdl31_ScriptType352

    @jpdl31_ScriptType352.setter
    def jpdl31_ScriptType352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType352", None)
        self.__jpdl31_ScriptType352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType1351"):
                opp_val = getattr(old_value, "jpdl31_TransitionType1351", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType1351"):
                opp_val = getattr(value, "jpdl31_TransitionType1351", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType1351", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def jpdl31_ScriptType101(self):
        return self.__jpdl31_ScriptType101

    @jpdl31_ScriptType101.setter
    def jpdl31_ScriptType101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType101", None)
        self.__jpdl31_ScriptType101 = value
        
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
    def jpdl31_ScriptType329(self):
        return self.__jpdl31_ScriptType329

    @jpdl31_ScriptType329.setter
    def jpdl31_ScriptType329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType329", None)
        self.__jpdl31_ScriptType329 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TimerType328"):
                opp_val = getattr(old_value, "jpdl31_TimerType328", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_TimerType328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TimerType328"):
                opp_val = getattr(value, "jpdl31_TimerType328", None)
                setattr(value, "jpdl31_TimerType328", self)

    @property
    def jpdl31_ScriptType335(self):
        return self.__jpdl31_ScriptType335

    @jpdl31_ScriptType335.setter
    def jpdl31_ScriptType335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType335", None)
        self.__jpdl31_ScriptType335 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType334"):
                opp_val = getattr(old_value, "jpdl31_TransitionType334", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType334"):
                opp_val = getattr(value, "jpdl31_TransitionType334", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType334", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ScriptType188(self):
        return self.__jpdl31_ScriptType188

    @jpdl31_ScriptType188.setter
    def jpdl31_ScriptType188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType188", None)
        self.__jpdl31_ScriptType188 = value
        
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
    def jpdl31_ScriptType98(self):
        return self.__jpdl31_ScriptType98

    @jpdl31_ScriptType98.setter
    def jpdl31_ScriptType98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType98", None)
        self.__jpdl31_ScriptType98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ExceptionHandlerType97"):
                opp_val = getattr(old_value, "jpdl31_ExceptionHandlerType97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ExceptionHandlerType97"):
                opp_val = getattr(value, "jpdl31_ExceptionHandlerType97", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ExceptionHandlerType97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def jpdl31_ScriptType131(self):
        return self.__jpdl31_ScriptType131

    @jpdl31_ScriptType131.setter
    def jpdl31_ScriptType131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ScriptType__jpdl31_ScriptType131", None)
        self.__jpdl31_ScriptType131 = value
        
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

class jpdl31_CreateTimerType:

    def __init__(self, duedate: str, name: str, repeat: str, transition: str, jpdl31_CreateTimerType: "jpdl31_ActionType" = None, jpdl31_CreateTimerType2: "jpdl31_ScriptType" = None, jpdl31_CreateTimerType26: "jpdl31_DocumentRoot" = None, jpdl31_CreateTimerType89: "jpdl31_EventType" = None, jpdl31_CreateTimerType134: "jpdl31_NodeType" = None, jpdl31_CreateTimerType191: "jpdl31_ProcessDefinitionType" = None, jpdl31_CreateTimerType338: "jpdl31_TransitionType" = None, jpdl31_CreateTimerType355: "jpdl31_TransitionType1" = None):
        self.duedate = duedate
        self.name = name
        self.repeat = repeat
        self.transition = transition
        self.jpdl31_CreateTimerType = jpdl31_CreateTimerType
        self.jpdl31_CreateTimerType2 = jpdl31_CreateTimerType2
        self.jpdl31_CreateTimerType26 = jpdl31_CreateTimerType26
        self.jpdl31_CreateTimerType89 = jpdl31_CreateTimerType89
        self.jpdl31_CreateTimerType134 = jpdl31_CreateTimerType134
        self.jpdl31_CreateTimerType191 = jpdl31_CreateTimerType191
        self.jpdl31_CreateTimerType338 = jpdl31_CreateTimerType338
        self.jpdl31_CreateTimerType355 = jpdl31_CreateTimerType355
        
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
    def jpdl31_CreateTimerType89(self):
        return self.__jpdl31_CreateTimerType89

    @jpdl31_CreateTimerType89.setter
    def jpdl31_CreateTimerType89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CreateTimerType__jpdl31_CreateTimerType89", None)
        self.__jpdl31_CreateTimerType89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_EventType88"):
                opp_val = getattr(old_value, "jpdl31_EventType88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_EventType88"):
                opp_val = getattr(value, "jpdl31_EventType88", None)
                if opp_val is None:
                    setattr(value, "jpdl31_EventType88", set([self]))
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
    def jpdl31_CreateTimerType134(self):
        return self.__jpdl31_CreateTimerType134

    @jpdl31_CreateTimerType134.setter
    def jpdl31_CreateTimerType134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CreateTimerType__jpdl31_CreateTimerType134", None)
        self.__jpdl31_CreateTimerType134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_NodeType133"):
                opp_val = getattr(old_value, "jpdl31_NodeType133", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_NodeType133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_NodeType133"):
                opp_val = getattr(value, "jpdl31_NodeType133", None)
                setattr(value, "jpdl31_NodeType133", self)

    @property
    def jpdl31_CreateTimerType191(self):
        return self.__jpdl31_CreateTimerType191

    @jpdl31_CreateTimerType191.setter
    def jpdl31_CreateTimerType191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CreateTimerType__jpdl31_CreateTimerType191", None)
        self.__jpdl31_CreateTimerType191 = value
        
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
    def jpdl31_CreateTimerType355(self):
        return self.__jpdl31_CreateTimerType355

    @jpdl31_CreateTimerType355.setter
    def jpdl31_CreateTimerType355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CreateTimerType__jpdl31_CreateTimerType355", None)
        self.__jpdl31_CreateTimerType355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType1354"):
                opp_val = getattr(old_value, "jpdl31_TransitionType1354", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType1354"):
                opp_val = getattr(value, "jpdl31_TransitionType1354", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType1354", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

    @property
    def jpdl31_CreateTimerType338(self):
        return self.__jpdl31_CreateTimerType338

    @jpdl31_CreateTimerType338.setter
    def jpdl31_CreateTimerType338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CreateTimerType__jpdl31_CreateTimerType338", None)
        self.__jpdl31_CreateTimerType338 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType337"):
                opp_val = getattr(old_value, "jpdl31_TransitionType337", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType337"):
                opp_val = getattr(value, "jpdl31_TransitionType337", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType337", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_ConditionType:

    def __init__(self, group: str, mixed: str, any: str, expression: str, jpdl31_ConditionType: "jpdl31_TransitionType1" = None):
        self.group = group
        self.mixed = mixed
        self.any = any
        self.expression = expression
        self.jpdl31_ConditionType = jpdl31_ConditionType
        
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
    def jpdl31_ConditionType(self):
        return self.__jpdl31_ConditionType

    @jpdl31_ConditionType.setter
    def jpdl31_ConditionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ConditionType__jpdl31_ConditionType", None)
        self.__jpdl31_ConditionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType1346"):
                opp_val = getattr(old_value, "jpdl31_TransitionType1346", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType1346"):
                opp_val = getattr(value, "jpdl31_TransitionType1346", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType1346", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_CancelTimerType:

    def __init__(self, name: str, jpdl31_CancelTimerType: "jpdl31_DocumentRoot" = None, jpdl31_CancelTimerType92: "jpdl31_EventType" = None, jpdl31_CancelTimerType137: "jpdl31_NodeType" = None, jpdl31_CancelTimerType194: "jpdl31_ProcessDefinitionType" = None, jpdl31_CancelTimerType341: "jpdl31_TransitionType" = None, jpdl31_CancelTimerType358: "jpdl31_TransitionType1" = None):
        self.name = name
        self.jpdl31_CancelTimerType = jpdl31_CancelTimerType
        self.jpdl31_CancelTimerType92 = jpdl31_CancelTimerType92
        self.jpdl31_CancelTimerType137 = jpdl31_CancelTimerType137
        self.jpdl31_CancelTimerType194 = jpdl31_CancelTimerType194
        self.jpdl31_CancelTimerType341 = jpdl31_CancelTimerType341
        self.jpdl31_CancelTimerType358 = jpdl31_CancelTimerType358
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jpdl31_CancelTimerType137(self):
        return self.__jpdl31_CancelTimerType137

    @jpdl31_CancelTimerType137.setter
    def jpdl31_CancelTimerType137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CancelTimerType__jpdl31_CancelTimerType137", None)
        self.__jpdl31_CancelTimerType137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_NodeType136"):
                opp_val = getattr(old_value, "jpdl31_NodeType136", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_NodeType136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_NodeType136"):
                opp_val = getattr(value, "jpdl31_NodeType136", None)
                setattr(value, "jpdl31_NodeType136", self)

    @property
    def jpdl31_CancelTimerType92(self):
        return self.__jpdl31_CancelTimerType92

    @jpdl31_CancelTimerType92.setter
    def jpdl31_CancelTimerType92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CancelTimerType__jpdl31_CancelTimerType92", None)
        self.__jpdl31_CancelTimerType92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_EventType91"):
                opp_val = getattr(old_value, "jpdl31_EventType91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_EventType91"):
                opp_val = getattr(value, "jpdl31_EventType91", None)
                if opp_val is None:
                    setattr(value, "jpdl31_EventType91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_CancelTimerType341(self):
        return self.__jpdl31_CancelTimerType341

    @jpdl31_CancelTimerType341.setter
    def jpdl31_CancelTimerType341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CancelTimerType__jpdl31_CancelTimerType341", None)
        self.__jpdl31_CancelTimerType341 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType340"):
                opp_val = getattr(old_value, "jpdl31_TransitionType340", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType340"):
                opp_val = getattr(value, "jpdl31_TransitionType340", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType340", set([self]))
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
    def jpdl31_CancelTimerType358(self):
        return self.__jpdl31_CancelTimerType358

    @jpdl31_CancelTimerType358.setter
    def jpdl31_CancelTimerType358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CancelTimerType__jpdl31_CancelTimerType358", None)
        self.__jpdl31_CancelTimerType358 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType1357"):
                opp_val = getattr(old_value, "jpdl31_TransitionType1357", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType1357"):
                opp_val = getattr(value, "jpdl31_TransitionType1357", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType1357", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_CancelTimerType194(self):
        return self.__jpdl31_CancelTimerType194

    @jpdl31_CancelTimerType194.setter
    def jpdl31_CancelTimerType194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_CancelTimerType__jpdl31_CancelTimerType194", None)
        self.__jpdl31_CancelTimerType194 = value
        
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

class Delegation:

    pass
class jpdl31_AssignmentType(Delegation):

    def __init__(self, expression: str, actorId: str, pooledActors: str, jpdl31_AssignmentType: "jpdl31_DocumentRoot" = None, jpdl31_AssignmentType286: "jpdl31_SwimlaneType" = None, jpdl31_AssignmentType308: "jpdl31_TaskType" = None):
        self.expression = expression
        self.actorId = actorId
        self.pooledActors = pooledActors
        self.jpdl31_AssignmentType = jpdl31_AssignmentType
        self.jpdl31_AssignmentType286 = jpdl31_AssignmentType286
        self.jpdl31_AssignmentType308 = jpdl31_AssignmentType308
        
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
    def actorId(self) -> str:
        return self.__actorId

    @actorId.setter
    def actorId(self, actorId: str):
        self.__actorId = actorId

    @property
    def jpdl31_AssignmentType286(self):
        return self.__jpdl31_AssignmentType286

    @jpdl31_AssignmentType286.setter
    def jpdl31_AssignmentType286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_AssignmentType__jpdl31_AssignmentType286", None)
        self.__jpdl31_AssignmentType286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_SwimlaneType285"):
                opp_val = getattr(old_value, "jpdl31_SwimlaneType285", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_SwimlaneType285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_SwimlaneType285"):
                opp_val = getattr(value, "jpdl31_SwimlaneType285", None)
                setattr(value, "jpdl31_SwimlaneType285", self)

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
    def jpdl31_AssignmentType308(self):
        return self.__jpdl31_AssignmentType308

    @jpdl31_AssignmentType308.setter
    def jpdl31_AssignmentType308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_AssignmentType__jpdl31_AssignmentType308", None)
        self.__jpdl31_AssignmentType308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TaskType307"):
                opp_val = getattr(old_value, "jpdl31_TaskType307", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TaskType307"):
                opp_val = getattr(value, "jpdl31_TaskType307", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TaskType307", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpdl31_ActionType:

    def __init__(self, acceptPropagatedEvents: str, mixed: str, any: str, async: str, class: str, configType: str, expression: str, name: str, refName: str, jpdl31_ActionType: "jpdl31_CreateTimerType" = None, jpdl31_ActionType16: "jpdl31_DocumentRoot" = None, jpdl31_ActionType83: "jpdl31_EventType" = None, jpdl31_ActionType95: "jpdl31_ExceptionHandlerType" = None, jpdl31_ActionType128: "jpdl31_NodeType" = None, jpdl31_ActionType185: "jpdl31_ProcessDefinitionType" = None, jpdl31_ActionType326: "jpdl31_TimerType" = None, jpdl31_ActionType332: "jpdl31_TransitionType" = None, jpdl31_ActionType349: "jpdl31_TransitionType1" = None):
        self.acceptPropagatedEvents = acceptPropagatedEvents
        self.mixed = mixed
        self.any = any
        self.async = async
        self.class = class
        self.configType = configType
        self.expression = expression
        self.name = name
        self.refName = refName
        self.jpdl31_ActionType = jpdl31_ActionType
        self.jpdl31_ActionType16 = jpdl31_ActionType16
        self.jpdl31_ActionType83 = jpdl31_ActionType83
        self.jpdl31_ActionType95 = jpdl31_ActionType95
        self.jpdl31_ActionType128 = jpdl31_ActionType128
        self.jpdl31_ActionType185 = jpdl31_ActionType185
        self.jpdl31_ActionType326 = jpdl31_ActionType326
        self.jpdl31_ActionType332 = jpdl31_ActionType332
        self.jpdl31_ActionType349 = jpdl31_ActionType349
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def async(self) -> str:
        return self.__async

    @async.setter
    def async(self, async: str):
        self.__async = async

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
    def refName(self) -> str:
        return self.__refName

    @refName.setter
    def refName(self, refName: str):
        self.__refName = refName

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
    def jpdl31_ActionType349(self):
        return self.__jpdl31_ActionType349

    @jpdl31_ActionType349.setter
    def jpdl31_ActionType349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType349", None)
        self.__jpdl31_ActionType349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType1348"):
                opp_val = getattr(old_value, "jpdl31_TransitionType1348", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType1348"):
                opp_val = getattr(value, "jpdl31_TransitionType1348", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType1348", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ActionType95(self):
        return self.__jpdl31_ActionType95

    @jpdl31_ActionType95.setter
    def jpdl31_ActionType95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType95", None)
        self.__jpdl31_ActionType95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_ExceptionHandlerType94"):
                opp_val = getattr(old_value, "jpdl31_ExceptionHandlerType94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_ExceptionHandlerType94"):
                opp_val = getattr(value, "jpdl31_ExceptionHandlerType94", None)
                if opp_val is None:
                    setattr(value, "jpdl31_ExceptionHandlerType94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpdl31_ActionType128(self):
        return self.__jpdl31_ActionType128

    @jpdl31_ActionType128.setter
    def jpdl31_ActionType128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType128", None)
        self.__jpdl31_ActionType128 = value
        
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
    def jpdl31_ActionType185(self):
        return self.__jpdl31_ActionType185

    @jpdl31_ActionType185.setter
    def jpdl31_ActionType185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType185", None)
        self.__jpdl31_ActionType185 = value
        
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
    def jpdl31_ActionType83(self):
        return self.__jpdl31_ActionType83

    @jpdl31_ActionType83.setter
    def jpdl31_ActionType83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType83", None)
        self.__jpdl31_ActionType83 = value
        
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
    def jpdl31_ActionType326(self):
        return self.__jpdl31_ActionType326

    @jpdl31_ActionType326.setter
    def jpdl31_ActionType326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType326", None)
        self.__jpdl31_ActionType326 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TimerType325"):
                opp_val = getattr(old_value, "jpdl31_TimerType325", None)
                if opp_val == self:
                    setattr(old_value, "jpdl31_TimerType325", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TimerType325"):
                opp_val = getattr(value, "jpdl31_TimerType325", None)
                setattr(value, "jpdl31_TimerType325", self)

    @property
    def jpdl31_ActionType332(self):
        return self.__jpdl31_ActionType332

    @jpdl31_ActionType332.setter
    def jpdl31_ActionType332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpdl31_ActionType__jpdl31_ActionType332", None)
        self.__jpdl31_ActionType332 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpdl31_TransitionType331"):
                opp_val = getattr(old_value, "jpdl31_TransitionType331", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpdl31_TransitionType331"):
                opp_val = getattr(value, "jpdl31_TransitionType331", None)
                if opp_val is None:
                    setattr(value, "jpdl31_TransitionType331", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
