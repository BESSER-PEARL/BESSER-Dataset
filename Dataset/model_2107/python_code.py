from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SignalTypeEnum(Enum):
    SIGNAL = "SIGNAL"
    ENVIRONMENT = "ENVIRONMENT"
    SYSTEM = "SYSTEM"
    UNDEFINED = "UNDEFINED"
class CreationModeEnum(Enum):
    IMPORTED = "IMPORTED"
    USER_DEFINED = "USER_DEFINED"
class TraceabilityArtifactEnum(Enum):
    REQUIREMENT = "REQUIREMENT"
    TEST = "TEST"
    BUG = "BUG"
    OTHERS = "OTHERS"
class ExecutionStatueTypeEnum(Enum):
    NOT_EXECUTED = "NOT_EXECUTED"
    PASS = "PASS"
    FAIL = "FAIL"
class OperatorTypeEnum(Enum):
    eq = "eq"
    ne = "ne"
    gt = "gt"
    lt = "lt"
    bt = "bt"


############################################
# Definition of Classes
############################################

class DiagnosticParamValueType:

    pass
class DiagonosticModel_OneOf(DiagnosticParamValueType):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class DiagonosticModel_Range(DiagnosticParamValueType):

    def __init__(self, from: int, to: int):
        self.from = from
        self.to = to
        
    @property
    def to(self) -> int:
        return self.__to

    @to.setter
    def to(self, to: int):
        self.__to = to

    @property
    def from(self) -> int:
        return self.__from

    @from.setter
    def from(self, from: int):
        self.__from = from

class DiagonosticModel_Var(DiagnosticParamValueType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class BlockAction:

    pass
class DiagonosticModel_WhileLoop(BlockAction):

    def __init__(self, value: str, valueTo: str, operator: str):
        self.value = value
        self.valueTo = valueTo
        self.operator = operator
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def valueTo(self) -> str:
        return self.__valueTo

    @valueTo.setter
    def valueTo(self, valueTo: str):
        self.__valueTo = valueTo

class DiagonosticModel_ForLoop(BlockAction):

    def __init__(self, loopVar: str, stopValue: int, startValue: int):
        self.loopVar = loopVar
        self.stopValue = stopValue
        self.startValue = startValue
        
    @property
    def loopVar(self) -> str:
        return self.__loopVar

    @loopVar.setter
    def loopVar(self, loopVar: str):
        self.__loopVar = loopVar

    @property
    def startValue(self) -> int:
        return self.__startValue

    @startValue.setter
    def startValue(self, startValue: int):
        self.__startValue = startValue

    @property
    def stopValue(self) -> int:
        return self.__stopValue

    @stopValue.setter
    def stopValue(self, stopValue: int):
        self.__stopValue = stopValue

class TestStep:

    pass
class DiagonosticModel_BlockAction(TestStep):

    pass
class DiagonosticModel_Action(TestStep):

    def __init__(self, value: str, wait: float, valueTo: str):
        self.value = value
        self.wait = wait
        self.valueTo = valueTo
        
    @property
    def wait(self) -> float:
        return self.__wait

    @wait.setter
    def wait(self, wait: float):
        self.__wait = wait

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def valueTo(self) -> str:
        return self.__valueTo

    @valueTo.setter
    def valueTo(self, valueTo: str):
        self.__valueTo = valueTo

class DiagonosticModel_DiagnosticParamValueType(ABC):

    pass
class DiagonosticModel_DiagnosticParam:

    def __init__(self, copyToVar: str, qualifier: str, DiagonosticModel_DiagnosticParam: "DiagonosticModel_DiagnosticRequest" = None, DiagonosticModel_DiagnosticParam54: "DiagonosticModel_DiagnosticParamValueType" = None, DiagonosticModel_DiagnosticParam52: "DiagonosticModel_DiagnosticResponse" = None):
        self.copyToVar = copyToVar
        self.qualifier = qualifier
        self.DiagonosticModel_DiagnosticParam = DiagonosticModel_DiagnosticParam
        self.DiagonosticModel_DiagnosticParam54 = DiagonosticModel_DiagnosticParam54
        self.DiagonosticModel_DiagnosticParam52 = DiagonosticModel_DiagnosticParam52
        
    @property
    def copyToVar(self) -> str:
        return self.__copyToVar

    @copyToVar.setter
    def copyToVar(self, copyToVar: str):
        self.__copyToVar = copyToVar

    @property
    def qualifier(self) -> str:
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier

    @property
    def DiagonosticModel_DiagnosticParam54(self):
        return self.__DiagonosticModel_DiagnosticParam54

    @DiagonosticModel_DiagnosticParam54.setter
    def DiagonosticModel_DiagnosticParam54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_DiagnosticParam__DiagonosticModel_DiagnosticParam54", None)
        self.__DiagonosticModel_DiagnosticParam54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_DiagnosticParamValueType"):
                opp_val = getattr(old_value, "DiagonosticModel_DiagnosticParamValueType", None)
                if opp_val == self:
                    setattr(old_value, "DiagonosticModel_DiagnosticParamValueType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_DiagnosticParamValueType"):
                opp_val = getattr(value, "DiagonosticModel_DiagnosticParamValueType", None)
                setattr(value, "DiagonosticModel_DiagnosticParamValueType", self)

    @property
    def DiagonosticModel_DiagnosticParam(self):
        return self.__DiagonosticModel_DiagnosticParam

    @DiagonosticModel_DiagnosticParam.setter
    def DiagonosticModel_DiagnosticParam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_DiagnosticParam__DiagonosticModel_DiagnosticParam", None)
        self.__DiagonosticModel_DiagnosticParam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_DiagnosticRequest49"):
                opp_val = getattr(old_value, "DiagonosticModel_DiagnosticRequest49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_DiagnosticRequest49"):
                opp_val = getattr(value, "DiagonosticModel_DiagnosticRequest49", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_DiagnosticRequest49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagonosticModel_DiagnosticParam52(self):
        return self.__DiagonosticModel_DiagnosticParam52

    @DiagonosticModel_DiagnosticParam52.setter
    def DiagonosticModel_DiagnosticParam52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_DiagnosticParam__DiagonosticModel_DiagnosticParam52", None)
        self.__DiagonosticModel_DiagnosticParam52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_DiagnosticResponse51"):
                opp_val = getattr(old_value, "DiagonosticModel_DiagnosticResponse51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_DiagnosticResponse51"):
                opp_val = getattr(value, "DiagonosticModel_DiagnosticResponse51", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_DiagnosticResponse51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DiagonosticModel_CAPLParam:

    def __init__(self, name: str, type: str, value: str, DiagonosticModel_CAPLParam: "DiagonosticModel_CAPLTestCase" = None, DiagonosticModel_CAPLParam44: "DiagonosticModel_CAPLTestStep" = None):
        self.name = name
        self.type = type
        self.value = value
        self.DiagonosticModel_CAPLParam = DiagonosticModel_CAPLParam
        self.DiagonosticModel_CAPLParam44 = DiagonosticModel_CAPLParam44
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def DiagonosticModel_CAPLParam44(self):
        return self.__DiagonosticModel_CAPLParam44

    @DiagonosticModel_CAPLParam44.setter
    def DiagonosticModel_CAPLParam44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_CAPLParam__DiagonosticModel_CAPLParam44", None)
        self.__DiagonosticModel_CAPLParam44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_CAPLTestStep"):
                opp_val = getattr(old_value, "DiagonosticModel_CAPLTestStep", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_CAPLTestStep"):
                opp_val = getattr(value, "DiagonosticModel_CAPLTestStep", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_CAPLTestStep", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagonosticModel_CAPLParam(self):
        return self.__DiagonosticModel_CAPLParam

    @DiagonosticModel_CAPLParam.setter
    def DiagonosticModel_CAPLParam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_CAPLParam__DiagonosticModel_CAPLParam", None)
        self.__DiagonosticModel_CAPLParam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_CAPLTestCase42"):
                opp_val = getattr(old_value, "DiagonosticModel_CAPLTestCase42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_CAPLTestCase42"):
                opp_val = getattr(value, "DiagonosticModel_CAPLTestCase42", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_CAPLTestCase42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DiagonosticModel_DiagnosticResponse:

    def __init__(self, primitive: str, DiagonosticModel_DiagnosticResponse: "DiagonosticModel_DiagnosticService" = None, DiagonosticModel_DiagnosticResponse51: set["DiagonosticModel_DiagnosticParam"] = None):
        self.primitive = primitive
        self.DiagonosticModel_DiagnosticResponse = DiagonosticModel_DiagnosticResponse
        self.DiagonosticModel_DiagnosticResponse51 = DiagonosticModel_DiagnosticResponse51 if DiagonosticModel_DiagnosticResponse51 is not None else set()
        
    @property
    def primitive(self) -> str:
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: str):
        self.__primitive = primitive

    @property
    def DiagonosticModel_DiagnosticResponse51(self):
        return self.__DiagonosticModel_DiagnosticResponse51

    @DiagonosticModel_DiagnosticResponse51.setter
    def DiagonosticModel_DiagnosticResponse51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_DiagnosticResponse__DiagonosticModel_DiagnosticResponse51", None)
        self.__DiagonosticModel_DiagnosticResponse51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_DiagnosticParam52"):
                    opp_val = getattr(item, "DiagonosticModel_DiagnosticParam52", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_DiagnosticParam52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_DiagnosticParam52"):
                    opp_val = getattr(item, "DiagonosticModel_DiagnosticParam52", None)
                    
                    setattr(item, "DiagonosticModel_DiagnosticParam52", self)
                    

    @property
    def DiagonosticModel_DiagnosticResponse(self):
        return self.__DiagonosticModel_DiagnosticResponse

    @DiagonosticModel_DiagnosticResponse.setter
    def DiagonosticModel_DiagnosticResponse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_DiagnosticResponse__DiagonosticModel_DiagnosticResponse", None)
        self.__DiagonosticModel_DiagnosticResponse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_DiagnosticService40"):
                opp_val = getattr(old_value, "DiagonosticModel_DiagnosticService40", None)
                if opp_val == self:
                    setattr(old_value, "DiagonosticModel_DiagnosticService40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_DiagnosticService40"):
                opp_val = getattr(value, "DiagonosticModel_DiagnosticService40", None)
                setattr(value, "DiagonosticModel_DiagnosticService40", self)

class DiagonosticModel_DiagnosticRequest:

    pass
class Action:

    pass
class DiagonosticModel_DiagnosticService(Action):

    def __init__(self, result: str, ecu: str, service: str, DiagonosticModel_DiagnosticService: "DiagonosticModel_DiagnosticRequest" = None, DiagonosticModel_DiagnosticService40: "DiagonosticModel_DiagnosticResponse" = None):
        self.result = result
        self.ecu = ecu
        self.service = service
        self.DiagonosticModel_DiagnosticService = DiagonosticModel_DiagnosticService
        self.DiagonosticModel_DiagnosticService40 = DiagonosticModel_DiagnosticService40
        
    @property
    def result(self) -> str:
        return self.__result

    @result.setter
    def result(self, result: str):
        self.__result = result

    @property
    def service(self) -> str:
        return self.__service

    @service.setter
    def service(self, service: str):
        self.__service = service

    @property
    def ecu(self) -> str:
        return self.__ecu

    @ecu.setter
    def ecu(self, ecu: str):
        self.__ecu = ecu

    @property
    def DiagonosticModel_DiagnosticService(self):
        return self.__DiagonosticModel_DiagnosticService

    @DiagonosticModel_DiagnosticService.setter
    def DiagonosticModel_DiagnosticService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_DiagnosticService__DiagonosticModel_DiagnosticService", None)
        self.__DiagonosticModel_DiagnosticService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_DiagnosticRequest"):
                opp_val = getattr(old_value, "DiagonosticModel_DiagnosticRequest", None)
                if opp_val == self:
                    setattr(old_value, "DiagonosticModel_DiagnosticRequest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_DiagnosticRequest"):
                opp_val = getattr(value, "DiagonosticModel_DiagnosticRequest", None)
                setattr(value, "DiagonosticModel_DiagnosticRequest", self)

    @property
    def DiagonosticModel_DiagnosticService40(self):
        return self.__DiagonosticModel_DiagnosticService40

    @DiagonosticModel_DiagnosticService40.setter
    def DiagonosticModel_DiagnosticService40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_DiagnosticService__DiagonosticModel_DiagnosticService40", None)
        self.__DiagonosticModel_DiagnosticService40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_DiagnosticResponse"):
                opp_val = getattr(old_value, "DiagonosticModel_DiagnosticResponse", None)
                if opp_val == self:
                    setattr(old_value, "DiagonosticModel_DiagnosticResponse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_DiagnosticResponse"):
                opp_val = getattr(value, "DiagonosticModel_DiagnosticResponse", None)
                setattr(value, "DiagonosticModel_DiagnosticResponse", self)

class DiagonosticModel_CAPLTestStep(Action):

    pass
class DiagonosticModel_CheckAction(Action):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class DiagonosticModel_WaitAction(Action):

    pass
class DiagonosticModel_SignalType:

    def __init__(self, name: str, type: str, MessageName: str, node: str, namespace: str, creationMode: str, lookupValues: str, DiagonosticModel_SignalType: "DiagonosticModel_TestStep" = None, DiagonosticModel_SignalType47: "DiagonosticModel_ImportArtifact" = None):
        self.name = name
        self.type = type
        self.MessageName = MessageName
        self.node = node
        self.namespace = namespace
        self.creationMode = creationMode
        self.lookupValues = lookupValues
        self.DiagonosticModel_SignalType = DiagonosticModel_SignalType
        self.DiagonosticModel_SignalType47 = DiagonosticModel_SignalType47
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def MessageName(self) -> str:
        return self.__MessageName

    @MessageName.setter
    def MessageName(self, MessageName: str):
        self.__MessageName = MessageName

    @property
    def node(self) -> str:
        return self.__node

    @node.setter
    def node(self, node: str):
        self.__node = node

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def creationMode(self) -> str:
        return self.__creationMode

    @creationMode.setter
    def creationMode(self, creationMode: str):
        self.__creationMode = creationMode

    @property
    def lookupValues(self) -> str:
        return self.__lookupValues

    @lookupValues.setter
    def lookupValues(self, lookupValues: str):
        self.__lookupValues = lookupValues

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DiagonosticModel_SignalType47(self):
        return self.__DiagonosticModel_SignalType47

    @DiagonosticModel_SignalType47.setter
    def DiagonosticModel_SignalType47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_SignalType__DiagonosticModel_SignalType47", None)
        self.__DiagonosticModel_SignalType47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_ImportArtifact46"):
                opp_val = getattr(old_value, "DiagonosticModel_ImportArtifact46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_ImportArtifact46"):
                opp_val = getattr(value, "DiagonosticModel_ImportArtifact46", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_ImportArtifact46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagonosticModel_SignalType(self):
        return self.__DiagonosticModel_SignalType

    @DiagonosticModel_SignalType.setter
    def DiagonosticModel_SignalType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_SignalType__DiagonosticModel_SignalType", None)
        self.__DiagonosticModel_SignalType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestStep37"):
                opp_val = getattr(old_value, "DiagonosticModel_TestStep37", None)
                if opp_val == self:
                    setattr(old_value, "DiagonosticModel_TestStep37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestStep37"):
                opp_val = getattr(value, "DiagonosticModel_TestStep37", None)
                setattr(value, "DiagonosticModel_TestStep37", self)

class DiagonosticModel_SetAction(Action):

    pass
class DiagonosticModel_TestStep(ABC):

    def __init__(self, title: str, DiagonosticModel_TestStep27: "DiagonosticModel_TestCase" = None, DiagonosticModel_TestStep35: "DiagonosticModel_TestStep" = None, DiagonosticModel_TestStep33: "DiagonosticModel_TestStep" = None, DiagonosticModel_TestStep: "DiagonosticModel_TestCase" = None, DiagonosticModel_TestStep24: "DiagonosticModel_TestCase" = None, DiagonosticModel_TestStep37: "DiagonosticModel_SignalType" = None, DiagonosticModel_TestStep56: "DiagonosticModel_BlockAction" = None):
        self.title = title
        self.DiagonosticModel_TestStep27 = DiagonosticModel_TestStep27
        self.DiagonosticModel_TestStep35 = DiagonosticModel_TestStep35
        self.DiagonosticModel_TestStep33 = DiagonosticModel_TestStep33
        self.DiagonosticModel_TestStep = DiagonosticModel_TestStep
        self.DiagonosticModel_TestStep24 = DiagonosticModel_TestStep24
        self.DiagonosticModel_TestStep37 = DiagonosticModel_TestStep37
        self.DiagonosticModel_TestStep56 = DiagonosticModel_TestStep56
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def DiagonosticModel_TestStep(self):
        return self.__DiagonosticModel_TestStep

    @DiagonosticModel_TestStep.setter
    def DiagonosticModel_TestStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestStep__DiagonosticModel_TestStep", None)
        self.__DiagonosticModel_TestStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestCase18"):
                opp_val = getattr(old_value, "DiagonosticModel_TestCase18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestCase18"):
                opp_val = getattr(value, "DiagonosticModel_TestCase18", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_TestCase18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagonosticModel_TestStep27(self):
        return self.__DiagonosticModel_TestStep27

    @DiagonosticModel_TestStep27.setter
    def DiagonosticModel_TestStep27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestStep__DiagonosticModel_TestStep27", None)
        self.__DiagonosticModel_TestStep27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestCase26"):
                opp_val = getattr(old_value, "DiagonosticModel_TestCase26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestCase26"):
                opp_val = getattr(value, "DiagonosticModel_TestCase26", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_TestCase26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagonosticModel_TestStep33(self):
        return self.__DiagonosticModel_TestStep33

    @DiagonosticModel_TestStep33.setter
    def DiagonosticModel_TestStep33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestStep__DiagonosticModel_TestStep33", None)
        self.__DiagonosticModel_TestStep33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestStep35"):
                opp_val = getattr(old_value, "DiagonosticModel_TestStep35", None)
                if opp_val == self:
                    setattr(old_value, "DiagonosticModel_TestStep35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestStep35"):
                opp_val = getattr(value, "DiagonosticModel_TestStep35", None)
                setattr(value, "DiagonosticModel_TestStep35", self)

    @property
    def DiagonosticModel_TestStep24(self):
        return self.__DiagonosticModel_TestStep24

    @DiagonosticModel_TestStep24.setter
    def DiagonosticModel_TestStep24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestStep__DiagonosticModel_TestStep24", None)
        self.__DiagonosticModel_TestStep24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestCase23"):
                opp_val = getattr(old_value, "DiagonosticModel_TestCase23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestCase23"):
                opp_val = getattr(value, "DiagonosticModel_TestCase23", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_TestCase23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagonosticModel_TestStep37(self):
        return self.__DiagonosticModel_TestStep37

    @DiagonosticModel_TestStep37.setter
    def DiagonosticModel_TestStep37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestStep__DiagonosticModel_TestStep37", None)
        self.__DiagonosticModel_TestStep37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_SignalType"):
                opp_val = getattr(old_value, "DiagonosticModel_SignalType", None)
                if opp_val == self:
                    setattr(old_value, "DiagonosticModel_SignalType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_SignalType"):
                opp_val = getattr(value, "DiagonosticModel_SignalType", None)
                setattr(value, "DiagonosticModel_SignalType", self)

    @property
    def DiagonosticModel_TestStep56(self):
        return self.__DiagonosticModel_TestStep56

    @DiagonosticModel_TestStep56.setter
    def DiagonosticModel_TestStep56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestStep__DiagonosticModel_TestStep56", None)
        self.__DiagonosticModel_TestStep56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_BlockAction"):
                opp_val = getattr(old_value, "DiagonosticModel_BlockAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_BlockAction"):
                opp_val = getattr(value, "DiagonosticModel_BlockAction", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_BlockAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagonosticModel_TestStep35(self):
        return self.__DiagonosticModel_TestStep35

    @DiagonosticModel_TestStep35.setter
    def DiagonosticModel_TestStep35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestStep__DiagonosticModel_TestStep35", None)
        self.__DiagonosticModel_TestStep35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestStep33"):
                opp_val = getattr(old_value, "DiagonosticModel_TestStep33", None)
                if opp_val == self:
                    setattr(old_value, "DiagonosticModel_TestStep33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestStep33"):
                opp_val = getattr(value, "DiagonosticModel_TestStep33", None)
                setattr(value, "DiagonosticModel_TestStep33", self)

class DiagonosticModel_TracebilityArtifact:

    def __init__(self, type: str, url: str, DiagonosticModel_TracebilityArtifact: "DiagonosticModel_TestCase" = None):
        self.type = type
        self.url = url
        self.DiagonosticModel_TracebilityArtifact = DiagonosticModel_TracebilityArtifact
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def DiagonosticModel_TracebilityArtifact(self):
        return self.__DiagonosticModel_TracebilityArtifact

    @DiagonosticModel_TracebilityArtifact.setter
    def DiagonosticModel_TracebilityArtifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TracebilityArtifact__DiagonosticModel_TracebilityArtifact", None)
        self.__DiagonosticModel_TracebilityArtifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestCase32"):
                opp_val = getattr(old_value, "DiagonosticModel_TestCase32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestCase32"):
                opp_val = getattr(value, "DiagonosticModel_TestCase32", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_TestCase32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DiagonosticModel_ImportArtifact:

    def __init__(self, path: str, DiagonosticModel_ImportArtifact: "DiagonosticModel_TestSpecification" = None, DiagonosticModel_ImportArtifact46: set["DiagonosticModel_SignalType"] = None):
        self.path = path
        self.DiagonosticModel_ImportArtifact = DiagonosticModel_ImportArtifact
        self.DiagonosticModel_ImportArtifact46 = DiagonosticModel_ImportArtifact46 if DiagonosticModel_ImportArtifact46 is not None else set()
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def DiagonosticModel_ImportArtifact46(self):
        return self.__DiagonosticModel_ImportArtifact46

    @DiagonosticModel_ImportArtifact46.setter
    def DiagonosticModel_ImportArtifact46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_ImportArtifact__DiagonosticModel_ImportArtifact46", None)
        self.__DiagonosticModel_ImportArtifact46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_SignalType47"):
                    opp_val = getattr(item, "DiagonosticModel_SignalType47", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_SignalType47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_SignalType47"):
                    opp_val = getattr(item, "DiagonosticModel_SignalType47", None)
                    
                    setattr(item, "DiagonosticModel_SignalType47", self)
                    

    @property
    def DiagonosticModel_ImportArtifact(self):
        return self.__DiagonosticModel_ImportArtifact

    @DiagonosticModel_ImportArtifact.setter
    def DiagonosticModel_ImportArtifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_ImportArtifact__DiagonosticModel_ImportArtifact", None)
        self.__DiagonosticModel_ImportArtifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestSpecification6"):
                opp_val = getattr(old_value, "DiagonosticModel_TestSpecification6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestSpecification6"):
                opp_val = getattr(value, "DiagonosticModel_TestSpecification6", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_TestSpecification6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DiagonosticModel_Variant:

    def __init__(self, name: str, description: str, DiagonosticModel_Variant: "DiagonosticModel_TestSpecification" = None, DiagonosticModel_Variant21: "DiagonosticModel_TestCase" = None):
        self.name = name
        self.description = description
        self.DiagonosticModel_Variant = DiagonosticModel_Variant
        self.DiagonosticModel_Variant21 = DiagonosticModel_Variant21
        
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
    def DiagonosticModel_Variant(self):
        return self.__DiagonosticModel_Variant

    @DiagonosticModel_Variant.setter
    def DiagonosticModel_Variant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_Variant__DiagonosticModel_Variant", None)
        self.__DiagonosticModel_Variant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestSpecification4"):
                opp_val = getattr(old_value, "DiagonosticModel_TestSpecification4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestSpecification4"):
                opp_val = getattr(value, "DiagonosticModel_TestSpecification4", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_TestSpecification4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagonosticModel_Variant21(self):
        return self.__DiagonosticModel_Variant21

    @DiagonosticModel_Variant21.setter
    def DiagonosticModel_Variant21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_Variant__DiagonosticModel_Variant21", None)
        self.__DiagonosticModel_Variant21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestCase20"):
                opp_val = getattr(old_value, "DiagonosticModel_TestCase20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestCase20"):
                opp_val = getattr(value, "DiagonosticModel_TestCase20", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_TestCase20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DiagonosticModel_CAPLTestCase:

    def __init__(self, name: str, DiagonosticModel_CAPLTestCase16: "DiagonosticModel_TestGroup" = None, DiagonosticModel_CAPLTestCase: "DiagonosticModel_TestSpecification" = None, DiagonosticModel_CAPLTestCase42: set["DiagonosticModel_CAPLParam"] = None):
        self.name = name
        self.DiagonosticModel_CAPLTestCase16 = DiagonosticModel_CAPLTestCase16
        self.DiagonosticModel_CAPLTestCase = DiagonosticModel_CAPLTestCase
        self.DiagonosticModel_CAPLTestCase42 = DiagonosticModel_CAPLTestCase42 if DiagonosticModel_CAPLTestCase42 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DiagonosticModel_CAPLTestCase16(self):
        return self.__DiagonosticModel_CAPLTestCase16

    @DiagonosticModel_CAPLTestCase16.setter
    def DiagonosticModel_CAPLTestCase16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_CAPLTestCase__DiagonosticModel_CAPLTestCase16", None)
        self.__DiagonosticModel_CAPLTestCase16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestGroup15"):
                opp_val = getattr(old_value, "DiagonosticModel_TestGroup15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestGroup15"):
                opp_val = getattr(value, "DiagonosticModel_TestGroup15", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_TestGroup15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagonosticModel_CAPLTestCase(self):
        return self.__DiagonosticModel_CAPLTestCase

    @DiagonosticModel_CAPLTestCase.setter
    def DiagonosticModel_CAPLTestCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_CAPLTestCase__DiagonosticModel_CAPLTestCase", None)
        self.__DiagonosticModel_CAPLTestCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestSpecification2"):
                opp_val = getattr(old_value, "DiagonosticModel_TestSpecification2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestSpecification2"):
                opp_val = getattr(value, "DiagonosticModel_TestSpecification2", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_TestSpecification2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagonosticModel_CAPLTestCase42(self):
        return self.__DiagonosticModel_CAPLTestCase42

    @DiagonosticModel_CAPLTestCase42.setter
    def DiagonosticModel_CAPLTestCase42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_CAPLTestCase__DiagonosticModel_CAPLTestCase42", None)
        self.__DiagonosticModel_CAPLTestCase42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_CAPLParam"):
                    opp_val = getattr(item, "DiagonosticModel_CAPLParam", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_CAPLParam", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_CAPLParam"):
                    opp_val = getattr(item, "DiagonosticModel_CAPLParam", None)
                    
                    setattr(item, "DiagonosticModel_CAPLParam", self)
                    

class DiagonosticModel_ExternalReference:

    def __init__(self, title: str, url: str, owner: str, type: str, DiagonosticModel_ExternalReference: "DiagonosticModel_TestGroup" = None, DiagonosticModel_ExternalReference30: "DiagonosticModel_TestCase" = None):
        self.title = title
        self.url = url
        self.owner = owner
        self.type = type
        self.DiagonosticModel_ExternalReference = DiagonosticModel_ExternalReference
        self.DiagonosticModel_ExternalReference30 = DiagonosticModel_ExternalReference30
        
    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def DiagonosticModel_ExternalReference(self):
        return self.__DiagonosticModel_ExternalReference

    @DiagonosticModel_ExternalReference.setter
    def DiagonosticModel_ExternalReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_ExternalReference__DiagonosticModel_ExternalReference", None)
        self.__DiagonosticModel_ExternalReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestGroup10"):
                opp_val = getattr(old_value, "DiagonosticModel_TestGroup10", None)
                if opp_val == self:
                    setattr(old_value, "DiagonosticModel_TestGroup10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestGroup10"):
                opp_val = getattr(value, "DiagonosticModel_TestGroup10", None)
                setattr(value, "DiagonosticModel_TestGroup10", self)

    @property
    def DiagonosticModel_ExternalReference30(self):
        return self.__DiagonosticModel_ExternalReference30

    @DiagonosticModel_ExternalReference30.setter
    def DiagonosticModel_ExternalReference30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_ExternalReference__DiagonosticModel_ExternalReference30", None)
        self.__DiagonosticModel_ExternalReference30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestCase29"):
                opp_val = getattr(old_value, "DiagonosticModel_TestCase29", None)
                if opp_val == self:
                    setattr(old_value, "DiagonosticModel_TestCase29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestCase29"):
                opp_val = getattr(value, "DiagonosticModel_TestCase29", None)
                setattr(value, "DiagonosticModel_TestCase29", self)

class DiagonosticModel_TestCase:

    def __init__(self, requirementID: str, executionStatus: str, skip: bool, name: str, id: str, description: str, DiagonosticModel_TestCase: "DiagonosticModel_TestGroup" = None, DiagonosticModel_TestCase26: set["DiagonosticModel_TestStep"] = None, DiagonosticModel_TestCase29: "DiagonosticModel_ExternalReference" = None, DiagonosticModel_TestCase32: set["DiagonosticModel_TracebilityArtifact"] = None, DiagonosticModel_TestCase18: set["DiagonosticModel_TestStep"] = None, DiagonosticModel_TestCase20: set["DiagonosticModel_Variant"] = None, DiagonosticModel_TestCase23: set["DiagonosticModel_TestStep"] = None):
        self.requirementID = requirementID
        self.executionStatus = executionStatus
        self.skip = skip
        self.name = name
        self.id = id
        self.description = description
        self.DiagonosticModel_TestCase = DiagonosticModel_TestCase
        self.DiagonosticModel_TestCase26 = DiagonosticModel_TestCase26 if DiagonosticModel_TestCase26 is not None else set()
        self.DiagonosticModel_TestCase29 = DiagonosticModel_TestCase29
        self.DiagonosticModel_TestCase32 = DiagonosticModel_TestCase32 if DiagonosticModel_TestCase32 is not None else set()
        self.DiagonosticModel_TestCase18 = DiagonosticModel_TestCase18 if DiagonosticModel_TestCase18 is not None else set()
        self.DiagonosticModel_TestCase20 = DiagonosticModel_TestCase20 if DiagonosticModel_TestCase20 is not None else set()
        self.DiagonosticModel_TestCase23 = DiagonosticModel_TestCase23 if DiagonosticModel_TestCase23 is not None else set()
        
    @property
    def skip(self) -> bool:
        return self.__skip

    @skip.setter
    def skip(self, skip: bool):
        self.__skip = skip

    @property
    def requirementID(self) -> str:
        return self.__requirementID

    @requirementID.setter
    def requirementID(self, requirementID: str):
        self.__requirementID = requirementID

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
    def executionStatus(self) -> str:
        return self.__executionStatus

    @executionStatus.setter
    def executionStatus(self, executionStatus: str):
        self.__executionStatus = executionStatus

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def DiagonosticModel_TestCase26(self):
        return self.__DiagonosticModel_TestCase26

    @DiagonosticModel_TestCase26.setter
    def DiagonosticModel_TestCase26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestCase__DiagonosticModel_TestCase26", None)
        self.__DiagonosticModel_TestCase26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_TestStep27"):
                    opp_val = getattr(item, "DiagonosticModel_TestStep27", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_TestStep27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_TestStep27"):
                    opp_val = getattr(item, "DiagonosticModel_TestStep27", None)
                    
                    setattr(item, "DiagonosticModel_TestStep27", self)
                    

    @property
    def DiagonosticModel_TestCase(self):
        return self.__DiagonosticModel_TestCase

    @DiagonosticModel_TestCase.setter
    def DiagonosticModel_TestCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestCase__DiagonosticModel_TestCase", None)
        self.__DiagonosticModel_TestCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestGroup8"):
                opp_val = getattr(old_value, "DiagonosticModel_TestGroup8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestGroup8"):
                opp_val = getattr(value, "DiagonosticModel_TestGroup8", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_TestGroup8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagonosticModel_TestCase23(self):
        return self.__DiagonosticModel_TestCase23

    @DiagonosticModel_TestCase23.setter
    def DiagonosticModel_TestCase23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestCase__DiagonosticModel_TestCase23", None)
        self.__DiagonosticModel_TestCase23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_TestStep24"):
                    opp_val = getattr(item, "DiagonosticModel_TestStep24", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_TestStep24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_TestStep24"):
                    opp_val = getattr(item, "DiagonosticModel_TestStep24", None)
                    
                    setattr(item, "DiagonosticModel_TestStep24", self)
                    

    @property
    def DiagonosticModel_TestCase18(self):
        return self.__DiagonosticModel_TestCase18

    @DiagonosticModel_TestCase18.setter
    def DiagonosticModel_TestCase18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestCase__DiagonosticModel_TestCase18", None)
        self.__DiagonosticModel_TestCase18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_TestStep"):
                    opp_val = getattr(item, "DiagonosticModel_TestStep", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_TestStep", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_TestStep"):
                    opp_val = getattr(item, "DiagonosticModel_TestStep", None)
                    
                    setattr(item, "DiagonosticModel_TestStep", self)
                    

    @property
    def DiagonosticModel_TestCase32(self):
        return self.__DiagonosticModel_TestCase32

    @DiagonosticModel_TestCase32.setter
    def DiagonosticModel_TestCase32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestCase__DiagonosticModel_TestCase32", None)
        self.__DiagonosticModel_TestCase32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_TracebilityArtifact"):
                    opp_val = getattr(item, "DiagonosticModel_TracebilityArtifact", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_TracebilityArtifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_TracebilityArtifact"):
                    opp_val = getattr(item, "DiagonosticModel_TracebilityArtifact", None)
                    
                    setattr(item, "DiagonosticModel_TracebilityArtifact", self)
                    

    @property
    def DiagonosticModel_TestCase20(self):
        return self.__DiagonosticModel_TestCase20

    @DiagonosticModel_TestCase20.setter
    def DiagonosticModel_TestCase20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestCase__DiagonosticModel_TestCase20", None)
        self.__DiagonosticModel_TestCase20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_Variant21"):
                    opp_val = getattr(item, "DiagonosticModel_Variant21", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_Variant21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_Variant21"):
                    opp_val = getattr(item, "DiagonosticModel_Variant21", None)
                    
                    setattr(item, "DiagonosticModel_Variant21", self)
                    

    @property
    def DiagonosticModel_TestCase29(self):
        return self.__DiagonosticModel_TestCase29

    @DiagonosticModel_TestCase29.setter
    def DiagonosticModel_TestCase29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestCase__DiagonosticModel_TestCase29", None)
        self.__DiagonosticModel_TestCase29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_ExternalReference30"):
                opp_val = getattr(old_value, "DiagonosticModel_ExternalReference30", None)
                if opp_val == self:
                    setattr(old_value, "DiagonosticModel_ExternalReference30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_ExternalReference30"):
                opp_val = getattr(value, "DiagonosticModel_ExternalReference30", None)
                setattr(value, "DiagonosticModel_ExternalReference30", self)

class DiagonosticModel_TestSpecification:

    def __init__(self, name: str, version: str, description: str, functionName: str, functionVersion: str, author: str, DiagonosticModel_TestSpecification: set["DiagonosticModel_TestGroup"] = None, DiagonosticModel_TestSpecification2: set["DiagonosticModel_CAPLTestCase"] = None, DiagonosticModel_TestSpecification4: set["DiagonosticModel_Variant"] = None, DiagonosticModel_TestSpecification6: set["DiagonosticModel_ImportArtifact"] = None):
        self.name = name
        self.version = version
        self.description = description
        self.functionName = functionName
        self.functionVersion = functionVersion
        self.author = author
        self.DiagonosticModel_TestSpecification = DiagonosticModel_TestSpecification if DiagonosticModel_TestSpecification is not None else set()
        self.DiagonosticModel_TestSpecification2 = DiagonosticModel_TestSpecification2 if DiagonosticModel_TestSpecification2 is not None else set()
        self.DiagonosticModel_TestSpecification4 = DiagonosticModel_TestSpecification4 if DiagonosticModel_TestSpecification4 is not None else set()
        self.DiagonosticModel_TestSpecification6 = DiagonosticModel_TestSpecification6 if DiagonosticModel_TestSpecification6 is not None else set()
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

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
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def functionVersion(self) -> str:
        return self.__functionVersion

    @functionVersion.setter
    def functionVersion(self, functionVersion: str):
        self.__functionVersion = functionVersion

    @property
    def DiagonosticModel_TestSpecification(self):
        return self.__DiagonosticModel_TestSpecification

    @DiagonosticModel_TestSpecification.setter
    def DiagonosticModel_TestSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestSpecification__DiagonosticModel_TestSpecification", None)
        self.__DiagonosticModel_TestSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_TestGroup"):
                    opp_val = getattr(item, "DiagonosticModel_TestGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_TestGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_TestGroup"):
                    opp_val = getattr(item, "DiagonosticModel_TestGroup", None)
                    
                    setattr(item, "DiagonosticModel_TestGroup", self)
                    

    @property
    def DiagonosticModel_TestSpecification6(self):
        return self.__DiagonosticModel_TestSpecification6

    @DiagonosticModel_TestSpecification6.setter
    def DiagonosticModel_TestSpecification6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestSpecification__DiagonosticModel_TestSpecification6", None)
        self.__DiagonosticModel_TestSpecification6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_ImportArtifact"):
                    opp_val = getattr(item, "DiagonosticModel_ImportArtifact", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_ImportArtifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_ImportArtifact"):
                    opp_val = getattr(item, "DiagonosticModel_ImportArtifact", None)
                    
                    setattr(item, "DiagonosticModel_ImportArtifact", self)
                    

    @property
    def DiagonosticModel_TestSpecification2(self):
        return self.__DiagonosticModel_TestSpecification2

    @DiagonosticModel_TestSpecification2.setter
    def DiagonosticModel_TestSpecification2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestSpecification__DiagonosticModel_TestSpecification2", None)
        self.__DiagonosticModel_TestSpecification2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_CAPLTestCase"):
                    opp_val = getattr(item, "DiagonosticModel_CAPLTestCase", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_CAPLTestCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_CAPLTestCase"):
                    opp_val = getattr(item, "DiagonosticModel_CAPLTestCase", None)
                    
                    setattr(item, "DiagonosticModel_CAPLTestCase", self)
                    

    @property
    def DiagonosticModel_TestSpecification4(self):
        return self.__DiagonosticModel_TestSpecification4

    @DiagonosticModel_TestSpecification4.setter
    def DiagonosticModel_TestSpecification4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestSpecification__DiagonosticModel_TestSpecification4", None)
        self.__DiagonosticModel_TestSpecification4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_Variant"):
                    opp_val = getattr(item, "DiagonosticModel_Variant", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_Variant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_Variant"):
                    opp_val = getattr(item, "DiagonosticModel_Variant", None)
                    
                    setattr(item, "DiagonosticModel_Variant", self)
                    

    def getSignals(self) -> str:
        # TODO: Implement getSignals method
        pass

class DiagonosticModel_TestGroup:

    def __init__(self, name: str, description: str, DiagonosticModel_TestGroup: "DiagonosticModel_TestSpecification" = None, DiagonosticModel_TestGroup8: set["DiagonosticModel_TestCase"] = None, DiagonosticModel_TestGroup10: "DiagonosticModel_ExternalReference" = None, DiagonosticModel_TestGroup13: "DiagonosticModel_TestGroup" = None, DiagonosticModel_TestGroup11: set["DiagonosticModel_TestGroup"] = None, DiagonosticModel_TestGroup15: set["DiagonosticModel_CAPLTestCase"] = None):
        self.name = name
        self.description = description
        self.DiagonosticModel_TestGroup = DiagonosticModel_TestGroup
        self.DiagonosticModel_TestGroup8 = DiagonosticModel_TestGroup8 if DiagonosticModel_TestGroup8 is not None else set()
        self.DiagonosticModel_TestGroup10 = DiagonosticModel_TestGroup10
        self.DiagonosticModel_TestGroup13 = DiagonosticModel_TestGroup13
        self.DiagonosticModel_TestGroup11 = DiagonosticModel_TestGroup11 if DiagonosticModel_TestGroup11 is not None else set()
        self.DiagonosticModel_TestGroup15 = DiagonosticModel_TestGroup15 if DiagonosticModel_TestGroup15 is not None else set()
        
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
    def DiagonosticModel_TestGroup11(self):
        return self.__DiagonosticModel_TestGroup11

    @DiagonosticModel_TestGroup11.setter
    def DiagonosticModel_TestGroup11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestGroup__DiagonosticModel_TestGroup11", None)
        self.__DiagonosticModel_TestGroup11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_TestGroup13"):
                    opp_val = getattr(item, "DiagonosticModel_TestGroup13", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_TestGroup13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_TestGroup13"):
                    opp_val = getattr(item, "DiagonosticModel_TestGroup13", None)
                    
                    setattr(item, "DiagonosticModel_TestGroup13", self)
                    

    @property
    def DiagonosticModel_TestGroup(self):
        return self.__DiagonosticModel_TestGroup

    @DiagonosticModel_TestGroup.setter
    def DiagonosticModel_TestGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestGroup__DiagonosticModel_TestGroup", None)
        self.__DiagonosticModel_TestGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestSpecification"):
                opp_val = getattr(old_value, "DiagonosticModel_TestSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestSpecification"):
                opp_val = getattr(value, "DiagonosticModel_TestSpecification", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_TestSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagonosticModel_TestGroup10(self):
        return self.__DiagonosticModel_TestGroup10

    @DiagonosticModel_TestGroup10.setter
    def DiagonosticModel_TestGroup10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestGroup__DiagonosticModel_TestGroup10", None)
        self.__DiagonosticModel_TestGroup10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_ExternalReference"):
                opp_val = getattr(old_value, "DiagonosticModel_ExternalReference", None)
                if opp_val == self:
                    setattr(old_value, "DiagonosticModel_ExternalReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_ExternalReference"):
                opp_val = getattr(value, "DiagonosticModel_ExternalReference", None)
                setattr(value, "DiagonosticModel_ExternalReference", self)

    @property
    def DiagonosticModel_TestGroup15(self):
        return self.__DiagonosticModel_TestGroup15

    @DiagonosticModel_TestGroup15.setter
    def DiagonosticModel_TestGroup15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestGroup__DiagonosticModel_TestGroup15", None)
        self.__DiagonosticModel_TestGroup15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_CAPLTestCase16"):
                    opp_val = getattr(item, "DiagonosticModel_CAPLTestCase16", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_CAPLTestCase16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_CAPLTestCase16"):
                    opp_val = getattr(item, "DiagonosticModel_CAPLTestCase16", None)
                    
                    setattr(item, "DiagonosticModel_CAPLTestCase16", self)
                    

    @property
    def DiagonosticModel_TestGroup13(self):
        return self.__DiagonosticModel_TestGroup13

    @DiagonosticModel_TestGroup13.setter
    def DiagonosticModel_TestGroup13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestGroup__DiagonosticModel_TestGroup13", None)
        self.__DiagonosticModel_TestGroup13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagonosticModel_TestGroup11"):
                opp_val = getattr(old_value, "DiagonosticModel_TestGroup11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagonosticModel_TestGroup11"):
                opp_val = getattr(value, "DiagonosticModel_TestGroup11", None)
                if opp_val is None:
                    setattr(value, "DiagonosticModel_TestGroup11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagonosticModel_TestGroup8(self):
        return self.__DiagonosticModel_TestGroup8

    @DiagonosticModel_TestGroup8.setter
    def DiagonosticModel_TestGroup8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiagonosticModel_TestGroup__DiagonosticModel_TestGroup8", None)
        self.__DiagonosticModel_TestGroup8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagonosticModel_TestCase"):
                    opp_val = getattr(item, "DiagonosticModel_TestCase", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagonosticModel_TestCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagonosticModel_TestCase"):
                    opp_val = getattr(item, "DiagonosticModel_TestCase", None)
                    
                    setattr(item, "DiagonosticModel_TestCase", self)
                    
