from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Testsuite:

    pass
class Etunit_TestsuiteType(Testsuite):

    pass
class Etunit_TestcaseType:

    def __init__(self, classname: str, name: str, time: str, Etunit_TestcaseType: "Etunit_ErrorType" = None, Etunit_TestcaseType10: "Etunit_FailureType" = None, Etunit_TestcaseType13: "Etunit_Testsuite" = None):
        self.classname = classname
        self.name = name
        self.time = time
        self.Etunit_TestcaseType = Etunit_TestcaseType
        self.Etunit_TestcaseType10 = Etunit_TestcaseType10
        self.Etunit_TestcaseType13 = Etunit_TestcaseType13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def classname(self) -> str:
        return self.__classname

    @classname.setter
    def classname(self, classname: str):
        self.__classname = classname

    @property
    def Etunit_TestcaseType(self):
        return self.__Etunit_TestcaseType

    @Etunit_TestcaseType.setter
    def Etunit_TestcaseType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_TestcaseType__Etunit_TestcaseType", None)
        self.__Etunit_TestcaseType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_ErrorType"):
                opp_val = getattr(old_value, "Etunit_ErrorType", None)
                if opp_val == self:
                    setattr(old_value, "Etunit_ErrorType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_ErrorType"):
                opp_val = getattr(value, "Etunit_ErrorType", None)
                setattr(value, "Etunit_ErrorType", self)

    @property
    def Etunit_TestcaseType13(self):
        return self.__Etunit_TestcaseType13

    @Etunit_TestcaseType13.setter
    def Etunit_TestcaseType13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_TestcaseType__Etunit_TestcaseType13", None)
        self.__Etunit_TestcaseType13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_Testsuite12"):
                opp_val = getattr(old_value, "Etunit_Testsuite12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_Testsuite12"):
                opp_val = getattr(value, "Etunit_Testsuite12", None)
                if opp_val is None:
                    setattr(value, "Etunit_Testsuite12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Etunit_TestcaseType10(self):
        return self.__Etunit_TestcaseType10

    @Etunit_TestcaseType10.setter
    def Etunit_TestcaseType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_TestcaseType__Etunit_TestcaseType10", None)
        self.__Etunit_TestcaseType10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_FailureType"):
                opp_val = getattr(old_value, "Etunit_FailureType", None)
                if opp_val == self:
                    setattr(old_value, "Etunit_FailureType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_FailureType"):
                opp_val = getattr(value, "Etunit_FailureType", None)
                setattr(value, "Etunit_FailureType", self)

class Etunit_FailureType:

    def __init__(self, mixed: str, expected: str, actual: str, Etunit_FailureType: "Etunit_TestcaseType" = None):
        self.mixed = mixed
        self.expected = expected
        self.actual = actual
        self.Etunit_FailureType = Etunit_FailureType
        
    @property
    def expected(self) -> str:
        return self.__expected

    @expected.setter
    def expected(self, expected: str):
        self.__expected = expected

    @property
    def actual(self) -> str:
        return self.__actual

    @actual.setter
    def actual(self, actual: str):
        self.__actual = actual

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Etunit_FailureType(self):
        return self.__Etunit_FailureType

    @Etunit_FailureType.setter
    def Etunit_FailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_FailureType__Etunit_FailureType", None)
        self.__Etunit_FailureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_TestcaseType10"):
                opp_val = getattr(old_value, "Etunit_TestcaseType10", None)
                if opp_val == self:
                    setattr(old_value, "Etunit_TestcaseType10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_TestcaseType10"):
                opp_val = getattr(value, "Etunit_TestcaseType10", None)
                setattr(value, "Etunit_TestcaseType10", self)

class Etunit_ErrorType:

    def __init__(self, mixed: str, expected: str, actual: str, Etunit_ErrorType: "Etunit_TestcaseType" = None):
        self.mixed = mixed
        self.expected = expected
        self.actual = actual
        self.Etunit_ErrorType = Etunit_ErrorType
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def expected(self) -> str:
        return self.__expected

    @expected.setter
    def expected(self, expected: str):
        self.__expected = expected

    @property
    def actual(self) -> str:
        return self.__actual

    @actual.setter
    def actual(self, actual: str):
        self.__actual = actual

    @property
    def Etunit_ErrorType(self):
        return self.__Etunit_ErrorType

    @Etunit_ErrorType.setter
    def Etunit_ErrorType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_ErrorType__Etunit_ErrorType", None)
        self.__Etunit_ErrorType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_TestcaseType"):
                opp_val = getattr(old_value, "Etunit_TestcaseType", None)
                if opp_val == self:
                    setattr(old_value, "Etunit_TestcaseType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_TestcaseType"):
                opp_val = getattr(value, "Etunit_TestcaseType", None)
                setattr(value, "Etunit_TestcaseType", self)

class Etunit_TestsuitesType:

    pass
class Etunit_Testsuite:

    def __init__(self, errors: str, failures: str, name: str, skipped: str, tests: str, time: str, timestamp: str, Etunit_Testsuite: "Etunit_DocumentRoot" = None, Etunit_Testsuite12: set["Etunit_TestcaseType"] = None):
        self.errors = errors
        self.failures = failures
        self.name = name
        self.skipped = skipped
        self.tests = tests
        self.time = time
        self.timestamp = timestamp
        self.Etunit_Testsuite = Etunit_Testsuite
        self.Etunit_Testsuite12 = Etunit_Testsuite12 if Etunit_Testsuite12 is not None else set()
        
    @property
    def skipped(self) -> str:
        return self.__skipped

    @skipped.setter
    def skipped(self, skipped: str):
        self.__skipped = skipped

    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def errors(self) -> str:
        return self.__errors

    @errors.setter
    def errors(self, errors: str):
        self.__errors = errors

    @property
    def failures(self) -> str:
        return self.__failures

    @failures.setter
    def failures(self, failures: str):
        self.__failures = failures

    @property
    def timestamp(self) -> str:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp

    @property
    def tests(self) -> str:
        return self.__tests

    @tests.setter
    def tests(self, tests: str):
        self.__tests = tests

    @property
    def Etunit_Testsuite(self):
        return self.__Etunit_Testsuite

    @Etunit_Testsuite.setter
    def Etunit_Testsuite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_Testsuite__Etunit_Testsuite", None)
        self.__Etunit_Testsuite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_DocumentRoot5"):
                opp_val = getattr(old_value, "Etunit_DocumentRoot5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_DocumentRoot5"):
                opp_val = getattr(value, "Etunit_DocumentRoot5", None)
                if opp_val is None:
                    setattr(value, "Etunit_DocumentRoot5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Etunit_Testsuite12(self):
        return self.__Etunit_Testsuite12

    @Etunit_Testsuite12.setter
    def Etunit_Testsuite12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_Testsuite__Etunit_Testsuite12", None)
        self.__Etunit_Testsuite12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Etunit_TestcaseType13"):
                    opp_val = getattr(item, "Etunit_TestcaseType13", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_TestcaseType13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_TestcaseType13"):
                    opp_val = getattr(item, "Etunit_TestcaseType13", None)
                    
                    setattr(item, "Etunit_TestcaseType13", self)
                    

class Etunit_EStringToStringMapEntry:

    pass
class Etunit_DocumentRoot:

    def __init__(self, mixed: str, Etunit_DocumentRoot: set["Etunit_EStringToStringMapEntry"] = None, Etunit_DocumentRoot2: set["Etunit_EStringToStringMapEntry"] = None, Etunit_DocumentRoot5: set["Etunit_Testsuite"] = None, Etunit_DocumentRoot7: set["Etunit_TestsuitesType"] = None):
        self.mixed = mixed
        self.Etunit_DocumentRoot = Etunit_DocumentRoot if Etunit_DocumentRoot is not None else set()
        self.Etunit_DocumentRoot2 = Etunit_DocumentRoot2 if Etunit_DocumentRoot2 is not None else set()
        self.Etunit_DocumentRoot5 = Etunit_DocumentRoot5 if Etunit_DocumentRoot5 is not None else set()
        self.Etunit_DocumentRoot7 = Etunit_DocumentRoot7 if Etunit_DocumentRoot7 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Etunit_DocumentRoot(self):
        return self.__Etunit_DocumentRoot

    @Etunit_DocumentRoot.setter
    def Etunit_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_DocumentRoot__Etunit_DocumentRoot", None)
        self.__Etunit_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Etunit_EStringToStringMapEntry"):
                    opp_val = getattr(item, "Etunit_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_EStringToStringMapEntry"):
                    opp_val = getattr(item, "Etunit_EStringToStringMapEntry", None)
                    
                    setattr(item, "Etunit_EStringToStringMapEntry", self)
                    

    @property
    def Etunit_DocumentRoot2(self):
        return self.__Etunit_DocumentRoot2

    @Etunit_DocumentRoot2.setter
    def Etunit_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_DocumentRoot__Etunit_DocumentRoot2", None)
        self.__Etunit_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Etunit_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "Etunit_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "Etunit_EStringToStringMapEntry3", None)
                    
                    setattr(item, "Etunit_EStringToStringMapEntry3", self)
                    

    @property
    def Etunit_DocumentRoot7(self):
        return self.__Etunit_DocumentRoot7

    @Etunit_DocumentRoot7.setter
    def Etunit_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_DocumentRoot__Etunit_DocumentRoot7", None)
        self.__Etunit_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Etunit_TestsuitesType"):
                    opp_val = getattr(item, "Etunit_TestsuitesType", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_TestsuitesType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_TestsuitesType"):
                    opp_val = getattr(item, "Etunit_TestsuitesType", None)
                    
                    setattr(item, "Etunit_TestsuitesType", self)
                    

    @property
    def Etunit_DocumentRoot5(self):
        return self.__Etunit_DocumentRoot5

    @Etunit_DocumentRoot5.setter
    def Etunit_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_DocumentRoot__Etunit_DocumentRoot5", None)
        self.__Etunit_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Etunit_Testsuite"):
                    opp_val = getattr(item, "Etunit_Testsuite", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_Testsuite", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_Testsuite"):
                    opp_val = getattr(item, "Etunit_Testsuite", None)
                    
                    setattr(item, "Etunit_Testsuite", self)
                    
