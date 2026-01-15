from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TestCaseResult(Enum):
    PASSED = "PASSED"
    SKIPPED = "SKIPPED"
    FAILED = "FAILED"
    FIXED = "FIXED"
    REGRESSION = "REGRESSION"


############################################
# Definition of Classes
############################################

class TestElement:

    pass
class builds_TestCase(TestElement):

    def __init__(self, status: str, message: str, stackTrace: str, className: str, skipped: bool, TestCase: "builds_TestSuite" = None, cases: "builds_TestSuite" = None):
        self.status = status
        self.message = message
        self.stackTrace = stackTrace
        self.className = className
        self.skipped = skipped
        self.TestCase = TestCase
        self.cases = cases
        
    @property
    def stackTrace(self) -> str:
        return self.__stackTrace

    @stackTrace.setter
    def stackTrace(self, stackTrace: str):
        self.__stackTrace = stackTrace

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def skipped(self) -> bool:
        return self.__skipped

    @skipped.setter
    def skipped(self, skipped: bool):
        self.__skipped = skipped

    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def cases(self):
        return self.__cases

    @cases.setter
    def cases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_TestCase__cases", None)
        self.__cases = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestSuite57"):
                opp_val = getattr(old_value, "TestSuite57", None)
                if opp_val == self:
                    setattr(old_value, "TestSuite57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestSuite57"):
                opp_val = getattr(value, "TestSuite57", None)
                setattr(value, "TestSuite57", self)

    @property
    def TestCase(self):
        return self.__TestCase

    @TestCase.setter
    def TestCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_TestCase__TestCase", None)
        self.__TestCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "suite"):
                opp_val = getattr(old_value, "suite", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "suite"):
                opp_val = getattr(value, "suite", None)
                if opp_val is None:
                    setattr(value, "suite", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class builds_TestElement:

    def __init__(self, label: str, duration: str, errorOutput: str, output: str):
        self.label = label
        self.duration = duration
        self.errorOutput = errorOutput
        self.output = output
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def errorOutput(self) -> str:
        return self.__errorOutput

    @errorOutput.setter
    def errorOutput(self, errorOutput: str):
        self.__errorOutput = errorOutput

    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

class builds_TestSuite(TestElement):

    pass
class ParameterDefinition:

    pass
class builds_BuildParameterDefinition(ParameterDefinition):

    def __init__(self, buildPlanId: str, builds_BuildParameterDefinition: "builds_BuildPlan" = None):
        self.buildPlanId = buildPlanId
        self.builds_BuildParameterDefinition = builds_BuildParameterDefinition
        
    @property
    def buildPlanId(self) -> str:
        return self.__buildPlanId

    @buildPlanId.setter
    def buildPlanId(self, buildPlanId: str):
        self.__buildPlanId = buildPlanId

    @property
    def builds_BuildParameterDefinition(self):
        return self.__builds_BuildParameterDefinition

    @builds_BuildParameterDefinition.setter
    def builds_BuildParameterDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildParameterDefinition__builds_BuildParameterDefinition", None)
        self.__builds_BuildParameterDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildPlan50"):
                opp_val = getattr(old_value, "builds_BuildPlan50", None)
                if opp_val == self:
                    setattr(old_value, "builds_BuildPlan50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildPlan50"):
                opp_val = getattr(value, "builds_BuildPlan50", None)
                setattr(value, "builds_BuildPlan50", self)

class builds_StringParameterDefinition(ParameterDefinition):

    def __init__(self, defaultValue: str):
        self.defaultValue = defaultValue
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

class builds_ChoiceParameterDefinition(ParameterDefinition):

    def __init__(self, options: str, defaultValue: str):
        self.options = options
        self.defaultValue = defaultValue
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def options(self) -> str:
        return self.__options

    @options.setter
    def options(self, options: str):
        self.__options = options

class builds_ChangeArtifact:

    def __init__(self, file: str, relativePath: str, prevRevision: str, revision: str, dead: bool, editType: str, builds_ChangeArtifact: "builds_Change" = None):
        self.file = file
        self.relativePath = relativePath
        self.prevRevision = prevRevision
        self.revision = revision
        self.dead = dead
        self.editType = editType
        self.builds_ChangeArtifact = builds_ChangeArtifact
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def dead(self) -> bool:
        return self.__dead

    @dead.setter
    def dead(self, dead: bool):
        self.__dead = dead

    @property
    def relativePath(self) -> str:
        return self.__relativePath

    @relativePath.setter
    def relativePath(self, relativePath: str):
        self.__relativePath = relativePath

    @property
    def editType(self) -> str:
        return self.__editType

    @editType.setter
    def editType(self, editType: str):
        self.__editType = editType

    @property
    def prevRevision(self) -> str:
        return self.__prevRevision

    @prevRevision.setter
    def prevRevision(self, prevRevision: str):
        self.__prevRevision = prevRevision

    @property
    def revision(self) -> str:
        return self.__revision

    @revision.setter
    def revision(self, revision: str):
        self.__revision = revision

    @property
    def builds_ChangeArtifact(self):
        return self.__builds_ChangeArtifact

    @builds_ChangeArtifact.setter
    def builds_ChangeArtifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_ChangeArtifact__builds_ChangeArtifact", None)
        self.__builds_ChangeArtifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_Change"):
                opp_val = getattr(old_value, "builds_Change", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_Change"):
                opp_val = getattr(value, "builds_Change", None)
                if opp_val is None:
                    setattr(value, "builds_Change", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class builds_Change:

    def __init__(self, message: str, date: str, revision: str, builds_Change: set["builds_ChangeArtifact"] = None, builds_Change42: "builds_User" = None, builds_Change46: "builds_ChangeSet" = None):
        self.message = message
        self.date = date
        self.revision = revision
        self.builds_Change = builds_Change if builds_Change is not None else set()
        self.builds_Change42 = builds_Change42
        self.builds_Change46 = builds_Change46
        
    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def revision(self) -> str:
        return self.__revision

    @revision.setter
    def revision(self, revision: str):
        self.__revision = revision

    @property
    def builds_Change(self):
        return self.__builds_Change

    @builds_Change.setter
    def builds_Change(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_Change__builds_Change", None)
        self.__builds_Change = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "builds_ChangeArtifact"):
                    opp_val = getattr(item, "builds_ChangeArtifact", None)
                    
                    if opp_val == self:
                        setattr(item, "builds_ChangeArtifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "builds_ChangeArtifact"):
                    opp_val = getattr(item, "builds_ChangeArtifact", None)
                    
                    setattr(item, "builds_ChangeArtifact", self)
                    

    @property
    def builds_Change42(self):
        return self.__builds_Change42

    @builds_Change42.setter
    def builds_Change42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_Change__builds_Change42", None)
        self.__builds_Change42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_User43"):
                opp_val = getattr(old_value, "builds_User43", None)
                if opp_val == self:
                    setattr(old_value, "builds_User43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_User43"):
                opp_val = getattr(value, "builds_User43", None)
                setattr(value, "builds_User43", self)

    @property
    def builds_Change46(self):
        return self.__builds_Change46

    @builds_Change46.setter
    def builds_Change46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_Change__builds_Change46", None)
        self.__builds_Change46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_ChangeSet45"):
                opp_val = getattr(old_value, "builds_ChangeSet45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_ChangeSet45"):
                opp_val = getattr(value, "builds_ChangeSet45", None)
                if opp_val is None:
                    setattr(value, "builds_ChangeSet45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class builds_BuildModel:

    pass
class builds_PasswordParameterDefinition(ParameterDefinition):

    def __init__(self, defaultValue: str):
        self.defaultValue = defaultValue
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

class builds_PlanParameterDefinition(ParameterDefinition):

    pass
class builds_FileParameterDefinition(ParameterDefinition):

    pass
class builds_BooleanParameterDefinition(ParameterDefinition):

    def __init__(self, defaultValue: bool):
        self.defaultValue = defaultValue
        
    @property
    def defaultValue(self) -> bool:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: bool):
        self.__defaultValue = defaultValue

class builds_BuildElement(ABC):

    def __init__(self, url: str, name: str, operations: str, elementStatus: str, refreshDate: date, builds_BuildElement: set["builds_StringToStringMap"] = None):
        self.url = url
        self.name = name
        self.operations = operations
        self.elementStatus = elementStatus
        self.refreshDate = refreshDate
        self.builds_BuildElement = builds_BuildElement if builds_BuildElement is not None else set()
        
    @property
    def refreshDate(self) -> date:
        return self.__refreshDate

    @refreshDate.setter
    def refreshDate(self, refreshDate: date):
        self.__refreshDate = refreshDate

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def operations(self) -> str:
        return self.__operations

    @operations.setter
    def operations(self, operations: str):
        self.__operations = operations

    @property
    def elementStatus(self) -> str:
        return self.__elementStatus

    @elementStatus.setter
    def elementStatus(self, elementStatus: str):
        self.__elementStatus = elementStatus

    @property
    def builds_BuildElement(self):
        return self.__builds_BuildElement

    @builds_BuildElement.setter
    def builds_BuildElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildElement__builds_BuildElement", None)
        self.__builds_BuildElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "builds_StringToStringMap"):
                    opp_val = getattr(item, "builds_StringToStringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "builds_StringToStringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "builds_StringToStringMap"):
                    opp_val = getattr(item, "builds_StringToStringMap", None)
                    
                    setattr(item, "builds_StringToStringMap", self)
                    

    def getServer(self) -> str:
        # TODO: Implement getServer method
        pass

    def getLabel(self) -> str:
        # TODO: Implement getLabel method
        pass

class builds_BuildReference:

    def __init__(self, plan: str, build: str, builds_BuildReference: "builds_BuildCause" = None):
        self.plan = plan
        self.build = build
        self.builds_BuildReference = builds_BuildReference
        
    @property
    def plan(self) -> str:
        return self.__plan

    @plan.setter
    def plan(self, plan: str):
        self.__plan = plan

    @property
    def build(self) -> str:
        return self.__build

    @build.setter
    def build(self, build: str):
        self.__build = build

    @property
    def builds_BuildReference(self):
        return self.__builds_BuildReference

    @builds_BuildReference.setter
    def builds_BuildReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildReference__builds_BuildReference", None)
        self.__builds_BuildReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildCause13"):
                opp_val = getattr(old_value, "builds_BuildCause13", None)
                if opp_val == self:
                    setattr(old_value, "builds_BuildCause13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildCause13"):
                opp_val = getattr(value, "builds_BuildCause13", None)
                setattr(value, "builds_BuildCause13", self)

class builds_BuildCause:

    def __init__(self, description: str, builds_BuildCause: "builds_Build" = None, builds_BuildCause13: "builds_BuildReference" = None, builds_BuildCause15: "builds_User" = None):
        self.description = description
        self.builds_BuildCause = builds_BuildCause
        self.builds_BuildCause13 = builds_BuildCause13
        self.builds_BuildCause15 = builds_BuildCause15
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def builds_BuildCause13(self):
        return self.__builds_BuildCause13

    @builds_BuildCause13.setter
    def builds_BuildCause13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildCause__builds_BuildCause13", None)
        self.__builds_BuildCause13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildReference"):
                opp_val = getattr(old_value, "builds_BuildReference", None)
                if opp_val == self:
                    setattr(old_value, "builds_BuildReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildReference"):
                opp_val = getattr(value, "builds_BuildReference", None)
                setattr(value, "builds_BuildReference", self)

    @property
    def builds_BuildCause15(self):
        return self.__builds_BuildCause15

    @builds_BuildCause15.setter
    def builds_BuildCause15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildCause__builds_BuildCause15", None)
        self.__builds_BuildCause15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_User16"):
                opp_val = getattr(old_value, "builds_User16", None)
                if opp_val == self:
                    setattr(old_value, "builds_User16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_User16"):
                opp_val = getattr(value, "builds_User16", None)
                setattr(value, "builds_User16", self)

    @property
    def builds_BuildCause(self):
        return self.__builds_BuildCause

    @builds_BuildCause.setter
    def builds_BuildCause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildCause__builds_BuildCause", None)
        self.__builds_BuildCause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_Build11"):
                opp_val = getattr(old_value, "builds_Build11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_Build11"):
                opp_val = getattr(value, "builds_Build11", None)
                if opp_val is None:
                    setattr(value, "builds_Build11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class builds_HealthReport:

    def __init__(self, health: int, description: str, builds_HealthReport: "builds_BuildPlan" = None):
        self.health = health
        self.description = description
        self.builds_HealthReport = builds_HealthReport
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, health: int):
        self.__health = health

    @property
    def builds_HealthReport(self):
        return self.__builds_HealthReport

    @builds_HealthReport.setter
    def builds_HealthReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_HealthReport__builds_HealthReport", None)
        self.__builds_HealthReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildPlan31"):
                opp_val = getattr(old_value, "builds_BuildPlan31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildPlan31"):
                opp_val = getattr(value, "builds_BuildPlan31", None)
                if opp_val is None:
                    setattr(value, "builds_BuildPlan31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class builds_ParameterDefinition(ABC):

    def __init__(self, name: str, description: str, ParameterDefinition: "builds_BuildPlan" = None, parameterDefinitions: "builds_BuildPlan" = None):
        self.name = name
        self.description = description
        self.ParameterDefinition = ParameterDefinition
        self.parameterDefinitions = parameterDefinitions
        
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
    def parameterDefinitions(self):
        return self.__parameterDefinitions

    @parameterDefinitions.setter
    def parameterDefinitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_ParameterDefinition__parameterDefinitions", None)
        self.__parameterDefinitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BuildPlan48"):
                opp_val = getattr(old_value, "BuildPlan48", None)
                if opp_val == self:
                    setattr(old_value, "BuildPlan48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BuildPlan48"):
                opp_val = getattr(value, "BuildPlan48", None)
                setattr(value, "BuildPlan48", self)

    @property
    def ParameterDefinition(self):
        return self.__ParameterDefinition

    @ParameterDefinition.setter
    def ParameterDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_ParameterDefinition__ParameterDefinition", None)
        self.__ParameterDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containingBuildPlan"):
                opp_val = getattr(old_value, "containingBuildPlan", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containingBuildPlan"):
                opp_val = getattr(value, "containingBuildPlan", None)
                if opp_val is None:
                    setattr(value, "containingBuildPlan", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class builds_ChangeSet:

    def __init__(self, kind: str, builds_ChangeSet: "builds_Build" = None, builds_ChangeSet45: set["builds_Change"] = None):
        self.kind = kind
        self.builds_ChangeSet = builds_ChangeSet
        self.builds_ChangeSet45 = builds_ChangeSet45 if builds_ChangeSet45 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def builds_ChangeSet(self):
        return self.__builds_ChangeSet

    @builds_ChangeSet.setter
    def builds_ChangeSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_ChangeSet__builds_ChangeSet", None)
        self.__builds_ChangeSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_Build2"):
                opp_val = getattr(old_value, "builds_Build2", None)
                if opp_val == self:
                    setattr(old_value, "builds_Build2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_Build2"):
                opp_val = getattr(value, "builds_Build2", None)
                setattr(value, "builds_Build2", self)

    @property
    def builds_ChangeSet45(self):
        return self.__builds_ChangeSet45

    @builds_ChangeSet45.setter
    def builds_ChangeSet45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_ChangeSet__builds_ChangeSet45", None)
        self.__builds_ChangeSet45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "builds_Change46"):
                    opp_val = getattr(item, "builds_Change46", None)
                    
                    if opp_val == self:
                        setattr(item, "builds_Change46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "builds_Change46"):
                    opp_val = getattr(item, "builds_Change46", None)
                    
                    setattr(item, "builds_Change46", self)
                    

class BuildElement:

    pass
class builds_BuildPlan(BuildElement):

    def __init__(self, flags: str, health: int, id: str, info: str, selected: bool, summary: str, state: str, status: str, description: str, builds_BuildPlan: "builds_Build" = None, containingBuildPlan: set["builds_ParameterDefinition"] = None, builds_BuildPlan31: set["builds_HealthReport"] = None, builds_BuildPlan19: "builds_BuildServer" = None, BuildPlan: "builds_BuildPlan" = None, parent: set["builds_BuildPlan"] = None, BuildPlan25: "builds_BuildPlan" = None, children: "builds_BuildPlan" = None, builds_BuildPlan27: "builds_Build" = None, builds_BuildPlan36: "builds_BuildModel" = None, BuildPlan48: "builds_ParameterDefinition" = None, builds_BuildPlan50: "builds_BuildParameterDefinition" = None):
        self.flags = flags
        self.health = health
        self.id = id
        self.info = info
        self.selected = selected
        self.summary = summary
        self.state = state
        self.status = status
        self.description = description
        self.builds_BuildPlan = builds_BuildPlan
        self.containingBuildPlan = containingBuildPlan if containingBuildPlan is not None else set()
        self.builds_BuildPlan31 = builds_BuildPlan31 if builds_BuildPlan31 is not None else set()
        self.builds_BuildPlan19 = builds_BuildPlan19
        self.BuildPlan = BuildPlan
        self.parent = parent if parent is not None else set()
        self.BuildPlan25 = BuildPlan25
        self.children = children
        self.builds_BuildPlan27 = builds_BuildPlan27
        self.builds_BuildPlan36 = builds_BuildPlan36
        self.BuildPlan48 = BuildPlan48
        self.builds_BuildPlan50 = builds_BuildPlan50
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def flags(self) -> str:
        return self.__flags

    @flags.setter
    def flags(self, flags: str):
        self.__flags = flags

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

    @property
    def summary(self) -> str:
        return self.__summary

    @summary.setter
    def summary(self, summary: str):
        self.__summary = summary

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, health: int):
        self.__health = health

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def info(self) -> str:
        return self.__info

    @info.setter
    def info(self, info: str):
        self.__info = info

    @property
    def builds_BuildPlan27(self):
        return self.__builds_BuildPlan27

    @builds_BuildPlan27.setter
    def builds_BuildPlan27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildPlan__builds_BuildPlan27", None)
        self.__builds_BuildPlan27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_Build28"):
                opp_val = getattr(old_value, "builds_Build28", None)
                if opp_val == self:
                    setattr(old_value, "builds_Build28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_Build28"):
                opp_val = getattr(value, "builds_Build28", None)
                setattr(value, "builds_Build28", self)

    @property
    def builds_BuildPlan50(self):
        return self.__builds_BuildPlan50

    @builds_BuildPlan50.setter
    def builds_BuildPlan50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildPlan__builds_BuildPlan50", None)
        self.__builds_BuildPlan50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildParameterDefinition"):
                opp_val = getattr(old_value, "builds_BuildParameterDefinition", None)
                if opp_val == self:
                    setattr(old_value, "builds_BuildParameterDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildParameterDefinition"):
                opp_val = getattr(value, "builds_BuildParameterDefinition", None)
                setattr(value, "builds_BuildParameterDefinition", self)

    @property
    def BuildPlan(self):
        return self.__BuildPlan

    @BuildPlan.setter
    def BuildPlan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildPlan__BuildPlan", None)
        self.__BuildPlan = value
        
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
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildPlan__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BuildPlan"):
                    opp_val = getattr(item, "BuildPlan", None)
                    
                    if opp_val == self:
                        setattr(item, "BuildPlan", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BuildPlan"):
                    opp_val = getattr(item, "BuildPlan", None)
                    
                    setattr(item, "BuildPlan", self)
                    

    @property
    def builds_BuildPlan(self):
        return self.__builds_BuildPlan

    @builds_BuildPlan.setter
    def builds_BuildPlan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildPlan__builds_BuildPlan", None)
        self.__builds_BuildPlan = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_Build4"):
                opp_val = getattr(old_value, "builds_Build4", None)
                if opp_val == self:
                    setattr(old_value, "builds_Build4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_Build4"):
                opp_val = getattr(value, "builds_Build4", None)
                setattr(value, "builds_Build4", self)

    @property
    def BuildPlan48(self):
        return self.__BuildPlan48

    @BuildPlan48.setter
    def BuildPlan48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildPlan__BuildPlan48", None)
        self.__BuildPlan48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterDefinitions"):
                opp_val = getattr(old_value, "parameterDefinitions", None)
                if opp_val == self:
                    setattr(old_value, "parameterDefinitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterDefinitions"):
                opp_val = getattr(value, "parameterDefinitions", None)
                setattr(value, "parameterDefinitions", self)

    @property
    def BuildPlan25(self):
        return self.__BuildPlan25

    @BuildPlan25.setter
    def BuildPlan25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildPlan__BuildPlan25", None)
        self.__BuildPlan25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def builds_BuildPlan31(self):
        return self.__builds_BuildPlan31

    @builds_BuildPlan31.setter
    def builds_BuildPlan31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildPlan__builds_BuildPlan31", None)
        self.__builds_BuildPlan31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "builds_HealthReport"):
                    opp_val = getattr(item, "builds_HealthReport", None)
                    
                    if opp_val == self:
                        setattr(item, "builds_HealthReport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "builds_HealthReport"):
                    opp_val = getattr(item, "builds_HealthReport", None)
                    
                    setattr(item, "builds_HealthReport", self)
                    

    @property
    def builds_BuildPlan19(self):
        return self.__builds_BuildPlan19

    @builds_BuildPlan19.setter
    def builds_BuildPlan19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildPlan__builds_BuildPlan19", None)
        self.__builds_BuildPlan19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildServer20"):
                opp_val = getattr(old_value, "builds_BuildServer20", None)
                if opp_val == self:
                    setattr(old_value, "builds_BuildServer20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildServer20"):
                opp_val = getattr(value, "builds_BuildServer20", None)
                setattr(value, "builds_BuildServer20", self)

    @property
    def containingBuildPlan(self):
        return self.__containingBuildPlan

    @containingBuildPlan.setter
    def containingBuildPlan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildPlan__containingBuildPlan", None)
        self.__containingBuildPlan = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ParameterDefinition"):
                    opp_val = getattr(item, "ParameterDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "ParameterDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ParameterDefinition"):
                    opp_val = getattr(item, "ParameterDefinition", None)
                    
                    setattr(item, "ParameterDefinition", self)
                    

    @property
    def builds_BuildPlan36(self):
        return self.__builds_BuildPlan36

    @builds_BuildPlan36.setter
    def builds_BuildPlan36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildPlan__builds_BuildPlan36", None)
        self.__builds_BuildPlan36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildModel35"):
                opp_val = getattr(old_value, "builds_BuildModel35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildModel35"):
                opp_val = getattr(value, "builds_BuildModel35", None)
                if opp_val is None:
                    setattr(value, "builds_BuildModel35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildPlan__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BuildPlan25"):
                opp_val = getattr(old_value, "BuildPlan25", None)
                if opp_val == self:
                    setattr(old_value, "BuildPlan25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BuildPlan25"):
                opp_val = getattr(value, "BuildPlan25", None)
                setattr(value, "BuildPlan25", self)

class builds_Build(BuildElement):

    def __init__(self, label: str, id: str, buildNumber: int, timestamp: str, duration: str, displayName: str, state: str, status: str, summary: str, builds_Build4: "builds_BuildPlan" = None, builds_Build6: "builds_BuildServer" = None, build: "builds_TestResult" = None, builds_Build: set["builds_Artifact"] = None, builds_Build2: "builds_ChangeSet" = None, builds_Build9: set["builds_User"] = None, builds_Build11: set["builds_BuildCause"] = None, builds_Build28: "builds_BuildPlan" = None, builds_Build39: "builds_BuildModel" = None, Build: "builds_TestResult" = None):
        self.label = label
        self.id = id
        self.buildNumber = buildNumber
        self.timestamp = timestamp
        self.duration = duration
        self.displayName = displayName
        self.state = state
        self.status = status
        self.summary = summary
        self.builds_Build4 = builds_Build4
        self.builds_Build6 = builds_Build6
        self.build = build
        self.builds_Build = builds_Build if builds_Build is not None else set()
        self.builds_Build2 = builds_Build2
        self.builds_Build9 = builds_Build9 if builds_Build9 is not None else set()
        self.builds_Build11 = builds_Build11 if builds_Build11 is not None else set()
        self.builds_Build28 = builds_Build28
        self.builds_Build39 = builds_Build39
        self.Build = Build
        
    @property
    def displayName(self) -> str:
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

    @property
    def summary(self) -> str:
        return self.__summary

    @summary.setter
    def summary(self, summary: str):
        self.__summary = summary

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def buildNumber(self) -> int:
        return self.__buildNumber

    @buildNumber.setter
    def buildNumber(self, buildNumber: int):
        self.__buildNumber = buildNumber

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def timestamp(self) -> str:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp

    @property
    def builds_Build39(self):
        return self.__builds_Build39

    @builds_Build39.setter
    def builds_Build39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_Build__builds_Build39", None)
        self.__builds_Build39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildModel38"):
                opp_val = getattr(old_value, "builds_BuildModel38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildModel38"):
                opp_val = getattr(value, "builds_BuildModel38", None)
                if opp_val is None:
                    setattr(value, "builds_BuildModel38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def builds_Build11(self):
        return self.__builds_Build11

    @builds_Build11.setter
    def builds_Build11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_Build__builds_Build11", None)
        self.__builds_Build11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "builds_BuildCause"):
                    opp_val = getattr(item, "builds_BuildCause", None)
                    
                    if opp_val == self:
                        setattr(item, "builds_BuildCause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "builds_BuildCause"):
                    opp_val = getattr(item, "builds_BuildCause", None)
                    
                    setattr(item, "builds_BuildCause", self)
                    

    @property
    def builds_Build9(self):
        return self.__builds_Build9

    @builds_Build9.setter
    def builds_Build9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_Build__builds_Build9", None)
        self.__builds_Build9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "builds_User"):
                    opp_val = getattr(item, "builds_User", None)
                    
                    if opp_val == self:
                        setattr(item, "builds_User", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "builds_User"):
                    opp_val = getattr(item, "builds_User", None)
                    
                    setattr(item, "builds_User", self)
                    

    @property
    def build(self):
        return self.__build

    @build.setter
    def build(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_Build__build", None)
        self.__build = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestResult"):
                opp_val = getattr(old_value, "TestResult", None)
                if opp_val == self:
                    setattr(old_value, "TestResult", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestResult"):
                opp_val = getattr(value, "TestResult", None)
                setattr(value, "TestResult", self)

    @property
    def builds_Build28(self):
        return self.__builds_Build28

    @builds_Build28.setter
    def builds_Build28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_Build__builds_Build28", None)
        self.__builds_Build28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildPlan27"):
                opp_val = getattr(old_value, "builds_BuildPlan27", None)
                if opp_val == self:
                    setattr(old_value, "builds_BuildPlan27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildPlan27"):
                opp_val = getattr(value, "builds_BuildPlan27", None)
                setattr(value, "builds_BuildPlan27", self)

    @property
    def Build(self):
        return self.__Build

    @Build.setter
    def Build(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_Build__Build", None)
        self.__Build = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testResult"):
                opp_val = getattr(old_value, "testResult", None)
                if opp_val == self:
                    setattr(old_value, "testResult", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testResult"):
                opp_val = getattr(value, "testResult", None)
                setattr(value, "testResult", self)

    @property
    def builds_Build4(self):
        return self.__builds_Build4

    @builds_Build4.setter
    def builds_Build4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_Build__builds_Build4", None)
        self.__builds_Build4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildPlan"):
                opp_val = getattr(old_value, "builds_BuildPlan", None)
                if opp_val == self:
                    setattr(old_value, "builds_BuildPlan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildPlan"):
                opp_val = getattr(value, "builds_BuildPlan", None)
                setattr(value, "builds_BuildPlan", self)

    @property
    def builds_Build6(self):
        return self.__builds_Build6

    @builds_Build6.setter
    def builds_Build6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_Build__builds_Build6", None)
        self.__builds_Build6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildServer"):
                opp_val = getattr(old_value, "builds_BuildServer", None)
                if opp_val == self:
                    setattr(old_value, "builds_BuildServer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildServer"):
                opp_val = getattr(value, "builds_BuildServer", None)
                setattr(value, "builds_BuildServer", self)

    @property
    def builds_Build2(self):
        return self.__builds_Build2

    @builds_Build2.setter
    def builds_Build2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_Build__builds_Build2", None)
        self.__builds_Build2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_ChangeSet"):
                opp_val = getattr(old_value, "builds_ChangeSet", None)
                if opp_val == self:
                    setattr(old_value, "builds_ChangeSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_ChangeSet"):
                opp_val = getattr(value, "builds_ChangeSet", None)
                setattr(value, "builds_ChangeSet", self)

    @property
    def builds_Build(self):
        return self.__builds_Build

    @builds_Build.setter
    def builds_Build(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_Build__builds_Build", None)
        self.__builds_Build = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "builds_Artifact"):
                    opp_val = getattr(item, "builds_Artifact", None)
                    
                    if opp_val == self:
                        setattr(item, "builds_Artifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "builds_Artifact"):
                    opp_val = getattr(item, "builds_Artifact", None)
                    
                    setattr(item, "builds_Artifact", self)
                    

class builds_Artifact(BuildElement):

    def __init__(self, relativePath: str, builds_Artifact: "builds_Build" = None):
        self.relativePath = relativePath
        self.builds_Artifact = builds_Artifact
        
    @property
    def relativePath(self) -> str:
        return self.__relativePath

    @relativePath.setter
    def relativePath(self, relativePath: str):
        self.__relativePath = relativePath

    @property
    def builds_Artifact(self):
        return self.__builds_Artifact

    @builds_Artifact.setter
    def builds_Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_Artifact__builds_Artifact", None)
        self.__builds_Artifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_Build"):
                opp_val = getattr(old_value, "builds_Build", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_Build"):
                opp_val = getattr(value, "builds_Build", None)
                if opp_val is None:
                    setattr(value, "builds_Build", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class builds_StringToStringMap:

    def __init__(self, key: str, value: str, builds_StringToStringMap: "builds_BuildElement" = None):
        self.key = key
        self.value = value
        self.builds_StringToStringMap = builds_StringToStringMap
        
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
    def builds_StringToStringMap(self):
        return self.__builds_StringToStringMap

    @builds_StringToStringMap.setter
    def builds_StringToStringMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_StringToStringMap__builds_StringToStringMap", None)
        self.__builds_StringToStringMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildElement"):
                opp_val = getattr(old_value, "builds_BuildElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildElement"):
                opp_val = getattr(value, "builds_BuildElement", None)
                if opp_val is None:
                    setattr(value, "builds_BuildElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class builds_User(BuildElement):

    def __init__(self, id: str, email: str, builds_User: "builds_Build" = None, builds_User16: "builds_BuildCause" = None, builds_User43: "builds_Change" = None):
        self.id = id
        self.email = email
        self.builds_User = builds_User
        self.builds_User16 = builds_User16
        self.builds_User43 = builds_User43
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def builds_User(self):
        return self.__builds_User

    @builds_User.setter
    def builds_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_User__builds_User", None)
        self.__builds_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_Build9"):
                opp_val = getattr(old_value, "builds_Build9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_Build9"):
                opp_val = getattr(value, "builds_Build9", None)
                if opp_val is None:
                    setattr(value, "builds_Build9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def builds_User43(self):
        return self.__builds_User43

    @builds_User43.setter
    def builds_User43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_User__builds_User43", None)
        self.__builds_User43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_Change42"):
                opp_val = getattr(old_value, "builds_Change42", None)
                if opp_val == self:
                    setattr(old_value, "builds_Change42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_Change42"):
                opp_val = getattr(value, "builds_Change42", None)
                setattr(value, "builds_Change42", self)

    @property
    def builds_User16(self):
        return self.__builds_User16

    @builds_User16.setter
    def builds_User16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_User__builds_User16", None)
        self.__builds_User16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildCause15"):
                opp_val = getattr(old_value, "builds_BuildCause15", None)
                if opp_val == self:
                    setattr(old_value, "builds_BuildCause15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildCause15"):
                opp_val = getattr(value, "builds_BuildCause15", None)
                setattr(value, "builds_BuildCause15", self)

class builds_TestResult:

    def __init__(self, duration: str, failCount: int, passCount: int, ignoredCount: int, errorCount: int, TestResult: "builds_Build" = None, testResult: "builds_Build" = None, result: set["builds_TestSuite"] = None, TestResult55: "builds_TestSuite" = None):
        self.duration = duration
        self.failCount = failCount
        self.passCount = passCount
        self.ignoredCount = ignoredCount
        self.errorCount = errorCount
        self.TestResult = TestResult
        self.testResult = testResult
        self.result = result if result is not None else set()
        self.TestResult55 = TestResult55
        
    @property
    def ignoredCount(self) -> int:
        return self.__ignoredCount

    @ignoredCount.setter
    def ignoredCount(self, ignoredCount: int):
        self.__ignoredCount = ignoredCount

    @property
    def failCount(self) -> int:
        return self.__failCount

    @failCount.setter
    def failCount(self, failCount: int):
        self.__failCount = failCount

    @property
    def errorCount(self) -> int:
        return self.__errorCount

    @errorCount.setter
    def errorCount(self, errorCount: int):
        self.__errorCount = errorCount

    @property
    def passCount(self) -> int:
        return self.__passCount

    @passCount.setter
    def passCount(self, passCount: int):
        self.__passCount = passCount

    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def testResult(self):
        return self.__testResult

    @testResult.setter
    def testResult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_TestResult__testResult", None)
        self.__testResult = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Build"):
                opp_val = getattr(old_value, "Build", None)
                if opp_val == self:
                    setattr(old_value, "Build", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Build"):
                opp_val = getattr(value, "Build", None)
                setattr(value, "Build", self)

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_TestResult__result", None)
        self.__result = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TestSuite"):
                    opp_val = getattr(item, "TestSuite", None)
                    
                    if opp_val == self:
                        setattr(item, "TestSuite", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TestSuite"):
                    opp_val = getattr(item, "TestSuite", None)
                    
                    setattr(item, "TestSuite", self)
                    

    @property
    def TestResult55(self):
        return self.__TestResult55

    @TestResult55.setter
    def TestResult55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_TestResult__TestResult55", None)
        self.__TestResult55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "suites"):
                opp_val = getattr(old_value, "suites", None)
                if opp_val == self:
                    setattr(old_value, "suites", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "suites"):
                opp_val = getattr(value, "suites", None)
                setattr(value, "suites", self)

    @property
    def TestResult(self):
        return self.__TestResult

    @TestResult.setter
    def TestResult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_TestResult__TestResult", None)
        self.__TestResult = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build"):
                opp_val = getattr(old_value, "build", None)
                if opp_val == self:
                    setattr(old_value, "build", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build"):
                opp_val = getattr(value, "build", None)
                setattr(value, "build", self)

class builds_BuildServer(BuildElement):

    def __init__(self, location: str, connectorKind: str, repositoryUrl: str, builds_BuildServer: "builds_Build" = None, builds_BuildServer20: "builds_BuildPlan" = None, builds_BuildServer33: "builds_BuildModel" = None):
        self.location = location
        self.connectorKind = connectorKind
        self.repositoryUrl = repositoryUrl
        self.builds_BuildServer = builds_BuildServer
        self.builds_BuildServer20 = builds_BuildServer20
        self.builds_BuildServer33 = builds_BuildServer33
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def connectorKind(self) -> str:
        return self.__connectorKind

    @connectorKind.setter
    def connectorKind(self, connectorKind: str):
        self.__connectorKind = connectorKind

    @property
    def repositoryUrl(self) -> str:
        return self.__repositoryUrl

    @repositoryUrl.setter
    def repositoryUrl(self, repositoryUrl: str):
        self.__repositoryUrl = repositoryUrl

    @property
    def builds_BuildServer20(self):
        return self.__builds_BuildServer20

    @builds_BuildServer20.setter
    def builds_BuildServer20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildServer__builds_BuildServer20", None)
        self.__builds_BuildServer20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildPlan19"):
                opp_val = getattr(old_value, "builds_BuildPlan19", None)
                if opp_val == self:
                    setattr(old_value, "builds_BuildPlan19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildPlan19"):
                opp_val = getattr(value, "builds_BuildPlan19", None)
                setattr(value, "builds_BuildPlan19", self)

    @property
    def builds_BuildServer33(self):
        return self.__builds_BuildServer33

    @builds_BuildServer33.setter
    def builds_BuildServer33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildServer__builds_BuildServer33", None)
        self.__builds_BuildServer33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_BuildModel"):
                opp_val = getattr(old_value, "builds_BuildModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_BuildModel"):
                opp_val = getattr(value, "builds_BuildModel", None)
                if opp_val is None:
                    setattr(value, "builds_BuildModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def builds_BuildServer(self):
        return self.__builds_BuildServer

    @builds_BuildServer.setter
    def builds_BuildServer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builds_BuildServer__builds_BuildServer", None)
        self.__builds_BuildServer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builds_Build6"):
                opp_val = getattr(old_value, "builds_Build6", None)
                if opp_val == self:
                    setattr(old_value, "builds_Build6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builds_Build6"):
                opp_val = getattr(value, "builds_Build6", None)
                setattr(value, "builds_Build6", self)
