from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ProgressState(Enum):
    NOT_STARTED = "NOT_STARTED"
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
    COMPLETED = "COMPLETED"
class ProblemType(Enum):
    ERROR = "ERROR"
    ASSERTION = "ASSERTION"
    ASSUMPTION = "ASSUMPTION"
class TestState(Enum):
    NOT_RUN = "NOT_RUN"
    IGNORED = "IGNORED"
    PASS = "PASS"
    FAILURE = "FAILURE"
    ERROR = "ERROR"


############################################
# Definition of Classes
############################################

class TraceElement:

    pass
class model_TraceException(TraceElement):

    pass
class model_TraceStackframe(TraceElement):

    pass
class model_Metadata:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
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

class TestProblem:

    pass
class model_ComparisonProblem(TestProblem):

    def __init__(self, expected: str, actual: str):
        self.expected = expected
        self.actual = actual
        
    @property
    def actual(self) -> str:
        return self.__actual

    @actual.setter
    def actual(self, actual: str):
        self.__actual = actual

    @property
    def expected(self) -> str:
        return self.__expected

    @expected.setter
    def expected(self, expected: str):
        self.__expected = expected

class model_TraceElement(ABC):

    def __init__(self, message: str, model_TraceElement: "model_TestProblem" = None):
        self.message = message
        self.model_TraceElement = model_TraceElement
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def model_TraceElement(self):
        return self.__model_TraceElement

    @model_TraceElement.setter
    def model_TraceElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TraceElement__model_TraceElement", None)
        self.__model_TraceElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TestProblem4"):
                opp_val = getattr(old_value, "model_TestProblem4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TestProblem4"):
                opp_val = getattr(value, "model_TestProblem4", None)
                if opp_val is None:
                    setattr(value, "model_TestProblem4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def open(self):
        # TODO: Implement open method
        pass

    def getProblem(self) -> TestProblem:
        # TODO: Implement getProblem method
        pass

    def getImageDescriptor(self) -> str:
        # TODO: Implement getImageDescriptor method
        pass

class model_TestProblem:

    def __init__(self, message: str, problemType: str, model_TestProblem: "model_TestElement" = None, model_TestProblem4: set["model_TraceElement"] = None):
        self.message = message
        self.problemType = problemType
        self.model_TestProblem = model_TestProblem
        self.model_TestProblem4 = model_TestProblem4 if model_TestProblem4 is not None else set()
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def problemType(self) -> str:
        return self.__problemType

    @problemType.setter
    def problemType(self, problemType: str):
        self.__problemType = problemType

    @property
    def model_TestProblem4(self):
        return self.__model_TestProblem4

    @model_TestProblem4.setter
    def model_TestProblem4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TestProblem__model_TestProblem4", None)
        self.__model_TestProblem4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TraceElement"):
                    opp_val = getattr(item, "model_TraceElement", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TraceElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TraceElement"):
                    opp_val = getattr(item, "model_TraceElement", None)
                    
                    setattr(item, "model_TraceElement", self)
                    

    @property
    def model_TestProblem(self):
        return self.__model_TestProblem

    @model_TestProblem.setter
    def model_TestProblem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TestProblem__model_TestProblem", None)
        self.__model_TestProblem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TestElement"):
                opp_val = getattr(old_value, "model_TestElement", None)
                if opp_val == self:
                    setattr(old_value, "model_TestElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TestElement"):
                opp_val = getattr(value, "model_TestElement", None)
                setattr(value, "model_TestElement", self)

    def getTestElement(self) -> TestElement:
        # TODO: Implement getTestElement method
        pass

class TestContainer:

    pass
class model_TestRoot(TestContainer):

    def __init__(self, testRunner: str):
        self.testRunner = testRunner
        
    @property
    def testRunner(self) -> str:
        return self.__testRunner

    @testRunner.setter
    def testRunner(self, testRunner: str):
        self.__testRunner = testRunner

class TestElement:

    pass
class model_TestCaseElement(TestElement):

    pass
class model_TestContainer(TestElement):

    def __init__(self, parent: set["model_TestElement"] = None, TestContainer: "model_TestElement" = None):
        self.parent = parent if parent is not None else set()
        self.TestContainer = TestContainer
        
    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TestContainer__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TestElement"):
                    opp_val = getattr(item, "TestElement", None)
                    
                    if opp_val == self:
                        setattr(item, "TestElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TestElement"):
                    opp_val = getattr(item, "TestElement", None)
                    
                    setattr(item, "TestElement", self)
                    

    @property
    def TestContainer(self):
        return self.__TestContainer

    @TestContainer.setter
    def TestContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TestContainer__TestContainer", None)
        self.__TestContainer = value
        
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

    def getErrorCount(self) -> int:
        # TODO: Implement getErrorCount method
        pass

    def updateProgressState(self):
        # TODO: Implement updateProgressState method
        pass

    def getIgnoredCount(self) -> int:
        # TODO: Implement getIgnoredCount method
        pass

    def getCompletedCount(self) -> int:
        # TODO: Implement getCompletedCount method
        pass

    def getTestCaseCount(self) -> int:
        # TODO: Implement getTestCaseCount method
        pass

    def getFailureCount(self) -> int:
        # TODO: Implement getFailureCount method
        pass

    def getAssumptionMismatchCount(self) -> int:
        # TODO: Implement getAssumptionMismatchCount method
        pass

    def getMergedTestState(self) -> str:
        # TODO: Implement getMergedTestState method
        pass

class model_TestElement(ABC):

    def __init__(self, name: str, description: str, testState: str, elementUnderTest: str, progressState: str, startTimestamp: str, endTimestamp: str, target: str, TestElement: "model_TestContainer" = None, children: "model_TestContainer" = None, model_TestElement: "model_TestProblem" = None):
        self.name = name
        self.description = description
        self.testState = testState
        self.elementUnderTest = elementUnderTest
        self.progressState = progressState
        self.startTimestamp = startTimestamp
        self.endTimestamp = endTimestamp
        self.target = target
        self.TestElement = TestElement
        self.children = children
        self.model_TestElement = model_TestElement
        
    @property
    def progressState(self) -> str:
        return self.__progressState

    @progressState.setter
    def progressState(self, progressState: str):
        self.__progressState = progressState

    @property
    def endTimestamp(self) -> str:
        return self.__endTimestamp

    @endTimestamp.setter
    def endTimestamp(self, endTimestamp: str):
        self.__endTimestamp = endTimestamp

    @property
    def testState(self) -> str:
        return self.__testState

    @testState.setter
    def testState(self, testState: str):
        self.__testState = testState

    @property
    def elementUnderTest(self) -> str:
        return self.__elementUnderTest

    @elementUnderTest.setter
    def elementUnderTest(self, elementUnderTest: str):
        self.__elementUnderTest = elementUnderTest

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def startTimestamp(self) -> str:
        return self.__startTimestamp

    @startTimestamp.setter
    def startTimestamp(self, startTimestamp: str):
        self.__startTimestamp = startTimestamp

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def TestElement(self):
        return self.__TestElement

    @TestElement.setter
    def TestElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TestElement__TestElement", None)
        self.__TestElement = value
        
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
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TestElement__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestContainer"):
                opp_val = getattr(old_value, "TestContainer", None)
                if opp_val == self:
                    setattr(old_value, "TestContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestContainer"):
                opp_val = getattr(value, "TestContainer", None)
                setattr(value, "TestContainer", self)

    @property
    def model_TestElement(self):
        return self.__model_TestElement

    @model_TestElement.setter
    def model_TestElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TestElement__model_TestElement", None)
        self.__model_TestElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TestProblem"):
                opp_val = getattr(old_value, "model_TestProblem", None)
                if opp_val == self:
                    setattr(old_value, "model_TestProblem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TestProblem"):
                opp_val = getattr(value, "model_TestProblem", None)
                setattr(value, "model_TestProblem", self)

    def getRoot(self) -> str:
        # TODO: Implement getRoot method
        pass

    def isErrorOrFailure(self) -> bool:
        # TODO: Implement isErrorOrFailure method
        pass

    def getDuration(self) -> str:
        # TODO: Implement getDuration method
        pass

    def getImageDescriptor(self) -> str:
        # TODO: Implement getImageDescriptor method
        pass

    def isRunning(self) -> bool:
        # TODO: Implement isRunning method
        pass

    def open(self):
        # TODO: Implement open method
        pass

    def hasWrongAssumption(self) -> bool:
        # TODO: Implement hasWrongAssumption method
        pass
