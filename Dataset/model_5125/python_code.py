from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class junitresult_JunitResult(ABC):

    pass
class JunitResult:

    pass
class junitresult_AbstractAggregatedTest(JunitResult):

    def __init__(self, name: str, tests: int, failures: int, errors: int, junitresult_AbstractAggregatedTest: set["junitresult_Testsuite"] = None):
        self.name = name
        self.tests = tests
        self.failures = failures
        self.errors = errors
        self.junitresult_AbstractAggregatedTest = junitresult_AbstractAggregatedTest if junitresult_AbstractAggregatedTest is not None else set()
        
    @property
    def errors(self) -> int:
        return self.__errors

    @errors.setter
    def errors(self, errors: int):
        self.__errors = errors

    @property
    def failures(self) -> int:
        return self.__failures

    @failures.setter
    def failures(self, failures: int):
        self.__failures = failures

    @property
    def tests(self) -> int:
        return self.__tests

    @tests.setter
    def tests(self, tests: int):
        self.__tests = tests

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def junitresult_AbstractAggregatedTest(self):
        return self.__junitresult_AbstractAggregatedTest

    @junitresult_AbstractAggregatedTest.setter
    def junitresult_AbstractAggregatedTest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_junitresult_AbstractAggregatedTest__junitresult_AbstractAggregatedTest", None)
        self.__junitresult_AbstractAggregatedTest = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "junitresult_Testsuite10"):
                    opp_val = getattr(item, "junitresult_Testsuite10", None)
                    
                    if opp_val == self:
                        setattr(item, "junitresult_Testsuite10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "junitresult_Testsuite10"):
                    opp_val = getattr(item, "junitresult_Testsuite10", None)
                    
                    setattr(item, "junitresult_Testsuite10", self)
                    

class junitresult_Testcase:

    def __init__(self, name: str, classname: str, time: float, system_out: str, system_err: str, status: str, assertions: str, junitresult_Testcase4: "junitresult_Skipped" = None, junitresult_Testcase6: set["junitresult_Failure"] = None, junitresult_Testcase8: set["junitresult_Error"] = None, junitresult_Testcase: "junitresult_Testsuite" = None):
        self.name = name
        self.classname = classname
        self.time = time
        self.system_out = system_out
        self.system_err = system_err
        self.status = status
        self.assertions = assertions
        self.junitresult_Testcase4 = junitresult_Testcase4
        self.junitresult_Testcase6 = junitresult_Testcase6 if junitresult_Testcase6 is not None else set()
        self.junitresult_Testcase8 = junitresult_Testcase8 if junitresult_Testcase8 is not None else set()
        self.junitresult_Testcase = junitresult_Testcase
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def system_out(self) -> str:
        return self.__system_out

    @system_out.setter
    def system_out(self, system_out: str):
        self.__system_out = system_out

    @property
    def assertions(self) -> str:
        return self.__assertions

    @assertions.setter
    def assertions(self, assertions: str):
        self.__assertions = assertions

    @property
    def system_err(self) -> str:
        return self.__system_err

    @system_err.setter
    def system_err(self, system_err: str):
        self.__system_err = system_err

    @property
    def time(self) -> float:
        return self.__time

    @time.setter
    def time(self, time: float):
        self.__time = time

    @property
    def classname(self) -> str:
        return self.__classname

    @classname.setter
    def classname(self, classname: str):
        self.__classname = classname

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def junitresult_Testcase(self):
        return self.__junitresult_Testcase

    @junitresult_Testcase.setter
    def junitresult_Testcase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_junitresult_Testcase__junitresult_Testcase", None)
        self.__junitresult_Testcase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "junitresult_Testsuite2"):
                opp_val = getattr(old_value, "junitresult_Testsuite2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "junitresult_Testsuite2"):
                opp_val = getattr(value, "junitresult_Testsuite2", None)
                if opp_val is None:
                    setattr(value, "junitresult_Testsuite2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def junitresult_Testcase4(self):
        return self.__junitresult_Testcase4

    @junitresult_Testcase4.setter
    def junitresult_Testcase4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_junitresult_Testcase__junitresult_Testcase4", None)
        self.__junitresult_Testcase4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "junitresult_Skipped"):
                opp_val = getattr(old_value, "junitresult_Skipped", None)
                if opp_val == self:
                    setattr(old_value, "junitresult_Skipped", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "junitresult_Skipped"):
                opp_val = getattr(value, "junitresult_Skipped", None)
                setattr(value, "junitresult_Skipped", self)

    @property
    def junitresult_Testcase6(self):
        return self.__junitresult_Testcase6

    @junitresult_Testcase6.setter
    def junitresult_Testcase6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_junitresult_Testcase__junitresult_Testcase6", None)
        self.__junitresult_Testcase6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "junitresult_Failure"):
                    opp_val = getattr(item, "junitresult_Failure", None)
                    
                    if opp_val == self:
                        setattr(item, "junitresult_Failure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "junitresult_Failure"):
                    opp_val = getattr(item, "junitresult_Failure", None)
                    
                    setattr(item, "junitresult_Failure", self)
                    

    @property
    def junitresult_Testcase8(self):
        return self.__junitresult_Testcase8

    @junitresult_Testcase8.setter
    def junitresult_Testcase8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_junitresult_Testcase__junitresult_Testcase8", None)
        self.__junitresult_Testcase8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "junitresult_Error"):
                    opp_val = getattr(item, "junitresult_Error", None)
                    
                    if opp_val == self:
                        setattr(item, "junitresult_Error", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "junitresult_Error"):
                    opp_val = getattr(item, "junitresult_Error", None)
                    
                    setattr(item, "junitresult_Error", self)
                    

class junitresult_Property:

    def __init__(self, name: str, value: str, junitresult_Property: "junitresult_Testsuite" = None):
        self.name = name
        self.value = value
        self.junitresult_Property = junitresult_Property
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def junitresult_Property(self):
        return self.__junitresult_Property

    @junitresult_Property.setter
    def junitresult_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_junitresult_Property__junitresult_Property", None)
        self.__junitresult_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "junitresult_Testsuite"):
                opp_val = getattr(old_value, "junitresult_Testsuite", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "junitresult_Testsuite"):
                opp_val = getattr(value, "junitresult_Testsuite", None)
                if opp_val is None:
                    setattr(value, "junitresult_Testsuite", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractAggregatedTest:

    pass
class junitresult_Testsuites(AbstractAggregatedTest):

    def __init__(self, time: float, disabled: int):
        self.time = time
        self.disabled = disabled
        
    @property
    def disabled(self) -> int:
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: int):
        self.__disabled = disabled

    @property
    def time(self) -> float:
        return self.__time

    @time.setter
    def time(self, time: float):
        self.__time = time

class junitresult_Testrun(AbstractAggregatedTest):

    def __init__(self, project: str, started: int, ignored: int):
        self.project = project
        self.started = started
        self.ignored = ignored
        
    @property
    def project(self) -> str:
        return self.__project

    @project.setter
    def project(self, project: str):
        self.__project = project

    @property
    def ignored(self) -> int:
        return self.__ignored

    @ignored.setter
    def ignored(self, ignored: int):
        self.__ignored = ignored

    @property
    def started(self) -> int:
        return self.__started

    @started.setter
    def started(self, started: int):
        self.__started = started

class junitresult_NegativeResult(ABC):

    def __init__(self, message: str, type: str, value: str):
        self.message = message
        self.type = type
        self.value = value
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

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

class NegativeResult:

    pass
class junitresult_Error(NegativeResult):

    pass
class junitresult_Failure(NegativeResult):

    pass
class junitresult_Skipped(NegativeResult):

    pass
class junitresult_Testsuite(AbstractAggregatedTest):

    def __init__(self, disabled: int, skipped: int, system_out: str, system_err: str, hostname: str, timestamp: date, time: float, id: int, package: str, junitresult_Testsuite: set["junitresult_Property"] = None, junitresult_Testsuite2: set["junitresult_Testcase"] = None, junitresult_Testsuite10: "junitresult_AbstractAggregatedTest" = None):
        self.disabled = disabled
        self.skipped = skipped
        self.system_out = system_out
        self.system_err = system_err
        self.hostname = hostname
        self.timestamp = timestamp
        self.time = time
        self.id = id
        self.package = package
        self.junitresult_Testsuite = junitresult_Testsuite if junitresult_Testsuite is not None else set()
        self.junitresult_Testsuite2 = junitresult_Testsuite2 if junitresult_Testsuite2 is not None else set()
        self.junitresult_Testsuite10 = junitresult_Testsuite10
        
    @property
    def system_out(self) -> str:
        return self.__system_out

    @system_out.setter
    def system_out(self, system_out: str):
        self.__system_out = system_out

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def hostname(self) -> str:
        return self.__hostname

    @hostname.setter
    def hostname(self, hostname: str):
        self.__hostname = hostname

    @property
    def timestamp(self) -> date:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: date):
        self.__timestamp = timestamp

    @property
    def system_err(self) -> str:
        return self.__system_err

    @system_err.setter
    def system_err(self, system_err: str):
        self.__system_err = system_err

    @property
    def disabled(self) -> int:
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: int):
        self.__disabled = disabled

    @property
    def time(self) -> float:
        return self.__time

    @time.setter
    def time(self, time: float):
        self.__time = time

    @property
    def skipped(self) -> int:
        return self.__skipped

    @skipped.setter
    def skipped(self, skipped: int):
        self.__skipped = skipped

    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def junitresult_Testsuite10(self):
        return self.__junitresult_Testsuite10

    @junitresult_Testsuite10.setter
    def junitresult_Testsuite10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_junitresult_Testsuite__junitresult_Testsuite10", None)
        self.__junitresult_Testsuite10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "junitresult_AbstractAggregatedTest"):
                opp_val = getattr(old_value, "junitresult_AbstractAggregatedTest", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "junitresult_AbstractAggregatedTest"):
                opp_val = getattr(value, "junitresult_AbstractAggregatedTest", None)
                if opp_val is None:
                    setattr(value, "junitresult_AbstractAggregatedTest", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def junitresult_Testsuite2(self):
        return self.__junitresult_Testsuite2

    @junitresult_Testsuite2.setter
    def junitresult_Testsuite2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_junitresult_Testsuite__junitresult_Testsuite2", None)
        self.__junitresult_Testsuite2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "junitresult_Testcase"):
                    opp_val = getattr(item, "junitresult_Testcase", None)
                    
                    if opp_val == self:
                        setattr(item, "junitresult_Testcase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "junitresult_Testcase"):
                    opp_val = getattr(item, "junitresult_Testcase", None)
                    
                    setattr(item, "junitresult_Testcase", self)
                    

    @property
    def junitresult_Testsuite(self):
        return self.__junitresult_Testsuite

    @junitresult_Testsuite.setter
    def junitresult_Testsuite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_junitresult_Testsuite__junitresult_Testsuite", None)
        self.__junitresult_Testsuite = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "junitresult_Property"):
                    opp_val = getattr(item, "junitresult_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "junitresult_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "junitresult_Property"):
                    opp_val = getattr(item, "junitresult_Property", None)
                    
                    setattr(item, "junitresult_Property", self)
                    
