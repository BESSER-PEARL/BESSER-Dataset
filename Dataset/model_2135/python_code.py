from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterType(Enum):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"
class NodeType(Enum):
    AND = "AND"
    OR = "OR"
class ErrorCode(Enum):
    testgeneration = "testgeneration"
    trello = "trello"
    nlp = "nlp"
    noSuchService = "noSuchService"
    methodNotAllowed = "methodNotAllowed"
    inMaintenanceMode = "inMaintenanceMode"
    invalidData = "invalidData"
    validator = "validator"
    noAuthorization = "noAuthorization"
    internalProblem = "internalProblem"
    userSession = "userSession"
    configuration = "configuration"
    persistency = "persistency"
    migration = "migration"
    seralization = "seralization"
    restService = "restService"
    scheduler = "scheduler"
    hpProxy = "hpProxy"
    jira = "jira"
    metrics = "metrics"
    search = "search"
class OperationType(Enum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


############################################
# Definition of Classes
############################################

class INamed:

    pass
class model_export_Export(INamed):

    def __init__(self, type: str, content: str):
        self.type = type
        self.content = content
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

class model_administration_ProblemDetail:

    def __init__(self, ecode: str, status: int, detail: str, instance: str):
        self.ecode = ecode
        self.status = status
        self.detail = detail
        self.instance = instance
        
    @property
    def ecode(self) -> str:
        return self.__ecode

    @ecode.setter
    def ecode(self, ecode: str):
        self.__ecode = ecode

    @property
    def instance(self) -> str:
        return self.__instance

    @instance.setter
    def instance(self, instance: str):
        self.__instance = instance

    @property
    def status(self) -> int:
        return self.__status

    @status.setter
    def status(self, status: int):
        self.__status = status

    @property
    def detail(self) -> str:
        return self.__detail

    @detail.setter
    def detail(self, detail: str):
        self.__detail = detail

class model_administration_Status:

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class model_history_Change:

    def __init__(self, objectName: str, objectType: str, oldValue: str, newValue: str, feature: str, isCreate: bool, isDelete: bool):
        self.objectName = objectName
        self.objectType = objectType
        self.oldValue = oldValue
        self.newValue = newValue
        self.feature = feature
        self.isCreate = isCreate
        self.isDelete = isDelete
        
    @property
    def newValue(self) -> str:
        return self.__newValue

    @newValue.setter
    def newValue(self, newValue: str):
        self.__newValue = newValue

    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

    @property
    def oldValue(self) -> str:
        return self.__oldValue

    @oldValue.setter
    def oldValue(self, oldValue: str):
        self.__oldValue = oldValue

    @property
    def objectName(self) -> str:
        return self.__objectName

    @objectName.setter
    def objectName(self, objectName: str):
        self.__objectName = objectName

    @property
    def isCreate(self) -> bool:
        return self.__isCreate

    @isCreate.setter
    def isCreate(self, isCreate: bool):
        self.__isCreate = isCreate

    @property
    def objectType(self) -> str:
        return self.__objectType

    @objectType.setter
    def objectType(self, objectType: str):
        self.__objectType = objectType

    @property
    def isDelete(self) -> bool:
        return self.__isDelete

    @isDelete.setter
    def isDelete(self, isDelete: bool):
        self.__isDelete = isDelete

class Change:

    pass
class model_batch_Operation:

    def __init__(self, type: str, model_batch_Operation: "IContentElement" = None, model_batch_Operation26: "IContentElement" = None):
        self.type = type
        self.model_batch_Operation = model_batch_Operation
        self.model_batch_Operation26 = model_batch_Operation26
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def model_batch_Operation(self):
        return self.__model_batch_Operation

    @model_batch_Operation.setter
    def model_batch_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_batch_Operation__model_batch_Operation", None)
        self.__model_batch_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IContentElement24"):
                opp_val = getattr(old_value, "IContentElement24", None)
                if opp_val == self:
                    setattr(old_value, "IContentElement24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IContentElement24"):
                opp_val = getattr(value, "IContentElement24", None)
                setattr(value, "IContentElement24", self)

    @property
    def model_batch_Operation26(self):
        return self.__model_batch_Operation26

    @model_batch_Operation26.setter
    def model_batch_Operation26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_batch_Operation__model_batch_Operation26", None)
        self.__model_batch_Operation26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IContentElement27"):
                opp_val = getattr(old_value, "IContentElement27", None)
                if opp_val == self:
                    setattr(old_value, "IContentElement27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IContentElement27"):
                opp_val = getattr(value, "IContentElement27", None)
                setattr(value, "IContentElement27", self)

class Operation:

    pass
class model_batch_BatchOperation:

    pass
class ProcessNode:

    pass
class model_processes_ProcessDecision(ProcessNode):

    pass
class model_processes_ProcessStart(ProcessNode):

    pass
class model_processes_ProcessStep(ProcessNode):

    def __init__(self, expectedOutcome: str):
        self.expectedOutcome = expectedOutcome
        
    @property
    def expectedOutcome(self) -> str:
        return self.__expectedOutcome

    @expectedOutcome.setter
    def expectedOutcome(self, expectedOutcome: str):
        self.__expectedOutcome = expectedOutcome

class base_IContentElement:

    pass
class model_history_HistoryEntry:

    def __init__(self, timestamp: str, user: str, deletedObjects: str, comment: str, model_history_HistoryEntry: set["Change"] = None):
        self.timestamp = timestamp
        self.user = user
        self.deletedObjects = deletedObjects
        self.comment = comment
        self.model_history_HistoryEntry = model_history_HistoryEntry if model_history_HistoryEntry is not None else set()
        
    @property
    def user(self) -> str:
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def timestamp(self) -> str:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp

    @property
    def deletedObjects(self) -> str:
        return self.__deletedObjects

    @deletedObjects.setter
    def deletedObjects(self, deletedObjects: str):
        self.__deletedObjects = deletedObjects

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def model_history_HistoryEntry(self):
        return self.__model_history_HistoryEntry

    @model_history_HistoryEntry.setter
    def model_history_HistoryEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_history_HistoryEntry__model_history_HistoryEntry", None)
        self.__model_history_HistoryEntry = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Change"):
                    opp_val = getattr(item, "Change", None)
                    
                    if opp_val == self:
                        setattr(item, "Change", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Change"):
                    opp_val = getattr(item, "Change", None)
                    
                    setattr(item, "Change", self)
                    

class HistoryEntry:

    pass
class model_history_History:

    pass
class model_processes_ProcessEnd(ProcessNode):

    pass
class ParameterAssignment:

    pass
class IContainer:

    pass
class model_processes_Process(IContainer):

    pass
class model_testspecification_TestSpecification(IContainer):

    pass
class TestParameter:

    pass
class base_IPositionable:

    pass
class model_testspecification_TestStep(base_IPositionable, base_IContentElement):

    def __init__(self, expectedOutcome: str, model_testspecification_TestStep: set["TestParameter"] = None):
        self.expectedOutcome = expectedOutcome
        self.model_testspecification_TestStep = model_testspecification_TestStep if model_testspecification_TestStep is not None else set()
        
    @property
    def expectedOutcome(self) -> str:
        return self.__expectedOutcome

    @expectedOutcome.setter
    def expectedOutcome(self, expectedOutcome: str):
        self.__expectedOutcome = expectedOutcome

    @property
    def model_testspecification_TestStep(self):
        return self.__model_testspecification_TestStep

    @model_testspecification_TestStep.setter
    def model_testspecification_TestStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_testspecification_TestStep__model_testspecification_TestStep", None)
        self.__model_testspecification_TestStep = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TestParameter19"):
                    opp_val = getattr(item, "TestParameter19", None)
                    
                    if opp_val == self:
                        setattr(item, "TestParameter19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TestParameter19"):
                    opp_val = getattr(item, "TestParameter19", None)
                    
                    setattr(item, "TestParameter19", self)
                    

class base_IExternal:

    pass
class base_ISpecmateModelObject:

    pass
class model_requirements_Requirement(base_IExternal, base_ISpecmateModelObject):

    def __init__(self, implementingITTeam: str, plannedRelease: str, status: str, isRegressionRequirement: bool, platform: str, numberOfTests: int, tac: str, implementingUnit: str, implementingBOTeam: str):
        self.implementingITTeam = implementingITTeam
        self.plannedRelease = plannedRelease
        self.status = status
        self.isRegressionRequirement = isRegressionRequirement
        self.platform = platform
        self.numberOfTests = numberOfTests
        self.tac = tac
        self.implementingUnit = implementingUnit
        self.implementingBOTeam = implementingBOTeam
        
    @property
    def implementingBOTeam(self) -> str:
        return self.__implementingBOTeam

    @implementingBOTeam.setter
    def implementingBOTeam(self, implementingBOTeam: str):
        self.__implementingBOTeam = implementingBOTeam

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def implementingITTeam(self) -> str:
        return self.__implementingITTeam

    @implementingITTeam.setter
    def implementingITTeam(self, implementingITTeam: str):
        self.__implementingITTeam = implementingITTeam

    @property
    def plannedRelease(self) -> str:
        return self.__plannedRelease

    @plannedRelease.setter
    def plannedRelease(self, plannedRelease: str):
        self.__plannedRelease = plannedRelease

    @property
    def implementingUnit(self) -> str:
        return self.__implementingUnit

    @implementingUnit.setter
    def implementingUnit(self, implementingUnit: str):
        self.__implementingUnit = implementingUnit

    @property
    def platform(self) -> str:
        return self.__platform

    @platform.setter
    def platform(self, platform: str):
        self.__platform = platform

    @property
    def numberOfTests(self) -> int:
        return self.__numberOfTests

    @numberOfTests.setter
    def numberOfTests(self, numberOfTests: int):
        self.__numberOfTests = numberOfTests

    @property
    def isRegressionRequirement(self) -> bool:
        return self.__isRegressionRequirement

    @isRegressionRequirement.setter
    def isRegressionRequirement(self, isRegressionRequirement: bool):
        self.__isRegressionRequirement = isRegressionRequirement

    @property
    def tac(self) -> str:
        return self.__tac

    @tac.setter
    def tac(self, tac: str):
        self.__tac = tac

class model_base_IRecycled(ABC):

    def __init__(self, recycled: bool, hasRecycledChildren: bool):
        self.recycled = recycled
        self.hasRecycledChildren = hasRecycledChildren
        
    @property
    def hasRecycledChildren(self) -> bool:
        return self.__hasRecycledChildren

    @hasRecycledChildren.setter
    def hasRecycledChildren(self, hasRecycledChildren: bool):
        self.__hasRecycledChildren = hasRecycledChildren

    @property
    def recycled(self) -> bool:
        return self.__recycled

    @recycled.setter
    def recycled(self, recycled: bool):
        self.__recycled = recycled

class ITracingElement:

    pass
class model_base_ITracingElement:

    pass
class IModelConnection:

    pass
class model_requirements_CEGConnection(IModelConnection):

    def __init__(self, negate: bool, base9: "model_base_IModelNode", base6: "model_base_IModelNode"):
        self.negate = negate
        
    @property
    def negate(self) -> bool:
        return self.__negate

    @negate.setter
    def negate(self, negate: bool):
        self.__negate = negate

class model_processes_ProcessConnection(IModelConnection):

    def __init__(self, condition: str, labelX: float, labelY: float, base9: "model_base_IModelNode", base6: "model_base_IModelNode"):
        self.condition = condition
        self.labelX = labelX
        self.labelY = labelY
        
    @property
    def labelX(self) -> float:
        return self.__labelX

    @labelX.setter
    def labelX(self, labelX: float):
        self.__labelX = labelX

    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def labelY(self) -> float:
        return self.__labelY

    @labelY.setter
    def labelY(self, labelY: float):
        self.__labelY = labelY

class ISpecmatePositionableModelObject:

    pass
class model_base_IModelNode(ISpecmatePositionableModelObject):

    pass
class IModelNode:

    pass
class model_requirements_CEGNode(IModelNode):

    def __init__(self, type: str, variable: str, condition: str, base: "model_base_IModelConnection", base4: "model_base_IModelConnection"):
        self.type = type
        self.variable = variable
        self.condition = condition
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

class model_processes_ProcessNode(IModelNode):

    pass
class IContentElement:

    pass
class model_testspecification_ParameterAssignment(IContentElement):

    def __init__(self, value: str, condition: str, TestParameter: "TestParameter" = None, IContentElement24: "model_batch_Operation", IContentElement: "model_base_IContainer", IContentElement27: "model_batch_Operation"):
        self.value = value
        self.condition = condition
        self.TestParameter = TestParameter
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def TestParameter(self):
        return self.__TestParameter

    @TestParameter.setter
    def TestParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_testspecification_ParameterAssignment__TestParameter", None)
        self.__TestParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testspecification17"):
                opp_val = getattr(old_value, "testspecification17", None)
                if opp_val == self:
                    setattr(old_value, "testspecification17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testspecification17"):
                opp_val = getattr(value, "testspecification17", None)
                setattr(value, "testspecification17", self)

class model_testspecification_TestParameter(IContentElement):

    def __init__(self, type: str, ParameterAssignment: set["ParameterAssignment"] = None, IContentElement24: "model_batch_Operation", IContentElement: "model_base_IContainer", IContentElement27: "model_batch_Operation"):
        self.type = type
        self.ParameterAssignment = ParameterAssignment if ParameterAssignment is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ParameterAssignment(self):
        return self.__ParameterAssignment

    @ParameterAssignment.setter
    def ParameterAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_testspecification_TestParameter__ParameterAssignment", None)
        self.__ParameterAssignment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testspecification"):
                    opp_val = getattr(item, "testspecification", None)
                    
                    if opp_val == self:
                        setattr(item, "testspecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testspecification"):
                    opp_val = getattr(item, "testspecification", None)
                    
                    setattr(item, "testspecification", self)
                    

class model_base_IContainer(IContentElement):

    pass
class base_IRecycled:

    pass
class base_IDescribed:

    pass
class base_INamed:

    pass
class base_IID:

    pass
class model_base_IContentElement(base_INamed, base_IRecycled, base_IDescribed, base_IID):

    pass
class model_base_IID(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class model_base_IDescribed(ABC):

    def __init__(self, description: str):
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class model_base_INamed(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class model_base_IExternal:

    def __init__(self, extId: str, extId2: str, source: str, live: bool):
        self.extId = extId
        self.extId2 = extId2
        self.source = source
        self.live = live
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def live(self) -> bool:
        return self.__live

    @live.setter
    def live(self, live: bool):
        self.__live = live

    @property
    def extId(self) -> str:
        return self.__extId

    @extId.setter
    def extId(self, extId: str):
        self.__extId = extId

    @property
    def extId2(self) -> str:
        return self.__extId2

    @extId2.setter
    def extId2(self, extId2: str):
        self.__extId2 = extId2

class model_base_IPositionable(ABC):

    def __init__(self, position: int):
        self.position = position
        
    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

class ISpecmateModelObject:

    pass
class model_base_IModelConnection(ISpecmateModelObject):

    pass
class model_base_ISpecmatePositionableModelObject(ISpecmateModelObject):

    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

class model_requirements_CEGModel(ISpecmateModelObject):

    def __init__(self, modelRequirements: str):
        self.modelRequirements = modelRequirements
        
    @property
    def modelRequirements(self) -> str:
        return self.__modelRequirements

    @modelRequirements.setter
    def modelRequirements(self, modelRequirements: str):
        self.__modelRequirements = modelRequirements

class model_base_Folder(ISpecmateModelObject):

    def __init__(self, library: bool):
        self.library = library
        
    @property
    def library(self) -> bool:
        return self.__library

    @library.setter
    def library(self, library: bool):
        self.__library = library

class base_ITracingElement:

    pass
class base_IContainer:

    pass
class model_testspecification_TestProcedure(base_IExternal, base_IContainer):

    def __init__(self, isRegressionTest: bool):
        self.isRegressionTest = isRegressionTest
        
    @property
    def isRegressionTest(self) -> bool:
        return self.__isRegressionTest

    @isRegressionTest.setter
    def isRegressionTest(self, isRegressionTest: bool):
        self.__isRegressionTest = isRegressionTest

class model_testspecification_TestCase(base_IPositionable, base_IContainer):

    def __init__(self, consistent: bool):
        self.consistent = consistent
        
    @property
    def consistent(self) -> bool:
        return self.__consistent

    @consistent.setter
    def consistent(self, consistent: bool):
        self.__consistent = consistent

class model_base_ISpecmateModelObject(base_ITracingElement, base_IContainer):

    pass