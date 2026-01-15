from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Etunit_SkippedType:

    def __init__(self, mixed: str, message: str, Etunit_SkippedType: "Etunit_DocumentRoot" = None, Etunit_SkippedType25: "Etunit_TestcaseType" = None):
        self.mixed = mixed
        self.message = message
        self.Etunit_SkippedType = Etunit_SkippedType
        self.Etunit_SkippedType25 = Etunit_SkippedType25
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Etunit_SkippedType25(self):
        return self.__Etunit_SkippedType25

    @Etunit_SkippedType25.setter
    def Etunit_SkippedType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_SkippedType__Etunit_SkippedType25", None)
        self.__Etunit_SkippedType25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_TestcaseType24"):
                opp_val = getattr(old_value, "Etunit_TestcaseType24", None)
                if opp_val == self:
                    setattr(old_value, "Etunit_TestcaseType24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_TestcaseType24"):
                opp_val = getattr(value, "Etunit_TestcaseType24", None)
                setattr(value, "Etunit_TestcaseType24", self)

    @property
    def Etunit_SkippedType(self):
        return self.__Etunit_SkippedType

    @Etunit_SkippedType.setter
    def Etunit_SkippedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_SkippedType__Etunit_SkippedType", None)
        self.__Etunit_SkippedType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_DocumentRoot13"):
                opp_val = getattr(old_value, "Etunit_DocumentRoot13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_DocumentRoot13"):
                opp_val = getattr(value, "Etunit_DocumentRoot13", None)
                if opp_val is None:
                    setattr(value, "Etunit_DocumentRoot13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Etunit_PropertyType:

    def __init__(self, name: str, value: str, Etunit_PropertyType: "Etunit_DocumentRoot" = None, Etunit_PropertyType22: "Etunit_PropertiesType" = None):
        self.name = name
        self.value = value
        self.Etunit_PropertyType = Etunit_PropertyType
        self.Etunit_PropertyType22 = Etunit_PropertyType22
        
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
    def Etunit_PropertyType22(self):
        return self.__Etunit_PropertyType22

    @Etunit_PropertyType22.setter
    def Etunit_PropertyType22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_PropertyType__Etunit_PropertyType22", None)
        self.__Etunit_PropertyType22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_PropertiesType21"):
                opp_val = getattr(old_value, "Etunit_PropertiesType21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_PropertiesType21"):
                opp_val = getattr(value, "Etunit_PropertiesType21", None)
                if opp_val is None:
                    setattr(value, "Etunit_PropertiesType21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Etunit_PropertyType(self):
        return self.__Etunit_PropertyType

    @Etunit_PropertyType.setter
    def Etunit_PropertyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_PropertyType__Etunit_PropertyType", None)
        self.__Etunit_PropertyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_DocumentRoot11"):
                opp_val = getattr(old_value, "Etunit_DocumentRoot11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_DocumentRoot11"):
                opp_val = getattr(value, "Etunit_DocumentRoot11", None)
                if opp_val is None:
                    setattr(value, "Etunit_DocumentRoot11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Etunit_PropertiesType:

    pass
class Etunit_FailureType:

    def __init__(self, mixed: str, message: str, type: str, Etunit_FailureType: "Etunit_DocumentRoot" = None, Etunit_FailureType31: "Etunit_TestcaseType" = None):
        self.mixed = mixed
        self.message = message
        self.type = type
        self.Etunit_FailureType = Etunit_FailureType
        self.Etunit_FailureType31 = Etunit_FailureType31
        
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
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Etunit_FailureType31(self):
        return self.__Etunit_FailureType31

    @Etunit_FailureType31.setter
    def Etunit_FailureType31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_FailureType__Etunit_FailureType31", None)
        self.__Etunit_FailureType31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_TestcaseType30"):
                opp_val = getattr(old_value, "Etunit_TestcaseType30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_TestcaseType30"):
                opp_val = getattr(value, "Etunit_TestcaseType30", None)
                if opp_val is None:
                    setattr(value, "Etunit_TestcaseType30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Etunit_DocumentRoot7"):
                opp_val = getattr(old_value, "Etunit_DocumentRoot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_DocumentRoot7"):
                opp_val = getattr(value, "Etunit_DocumentRoot7", None)
                if opp_val is None:
                    setattr(value, "Etunit_DocumentRoot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Etunit_ErrorType:

    def __init__(self, mixed: str, message: str, type: str, Etunit_ErrorType: "Etunit_DocumentRoot" = None, Etunit_ErrorType28: "Etunit_TestcaseType" = None):
        self.mixed = mixed
        self.message = message
        self.type = type
        self.Etunit_ErrorType = Etunit_ErrorType
        self.Etunit_ErrorType28 = Etunit_ErrorType28
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

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
    def Etunit_ErrorType28(self):
        return self.__Etunit_ErrorType28

    @Etunit_ErrorType28.setter
    def Etunit_ErrorType28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_ErrorType__Etunit_ErrorType28", None)
        self.__Etunit_ErrorType28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_TestcaseType27"):
                opp_val = getattr(old_value, "Etunit_TestcaseType27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_TestcaseType27"):
                opp_val = getattr(value, "Etunit_TestcaseType27", None)
                if opp_val is None:
                    setattr(value, "Etunit_TestcaseType27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Etunit_TestsuitesType:

    def __init__(self, disabled: str, errors: str, failures: str, name: str, tests: str, time: str, Etunit_TestsuitesType: "Etunit_DocumentRoot" = None, Etunit_TestsuitesType33: set["Etunit_TestsuiteType"] = None):
        self.disabled = disabled
        self.errors = errors
        self.failures = failures
        self.name = name
        self.tests = tests
        self.time = time
        self.Etunit_TestsuitesType = Etunit_TestsuitesType
        self.Etunit_TestsuitesType33 = Etunit_TestsuitesType33 if Etunit_TestsuitesType33 is not None else set()
        
    @property
    def failures(self) -> str:
        return self.__failures

    @failures.setter
    def failures(self, failures: str):
        self.__failures = failures

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
    def errors(self) -> str:
        return self.__errors

    @errors.setter
    def errors(self, errors: str):
        self.__errors = errors

    @property
    def disabled(self) -> str:
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: str):
        self.__disabled = disabled

    @property
    def tests(self) -> str:
        return self.__tests

    @tests.setter
    def tests(self, tests: str):
        self.__tests = tests

    @property
    def Etunit_TestsuitesType33(self):
        return self.__Etunit_TestsuitesType33

    @Etunit_TestsuitesType33.setter
    def Etunit_TestsuitesType33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_TestsuitesType__Etunit_TestsuitesType33", None)
        self.__Etunit_TestsuitesType33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Etunit_TestsuiteType34"):
                    opp_val = getattr(item, "Etunit_TestsuiteType34", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_TestsuiteType34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_TestsuiteType34"):
                    opp_val = getattr(item, "Etunit_TestsuiteType34", None)
                    
                    setattr(item, "Etunit_TestsuiteType34", self)
                    

    @property
    def Etunit_TestsuitesType(self):
        return self.__Etunit_TestsuitesType

    @Etunit_TestsuitesType.setter
    def Etunit_TestsuitesType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_TestsuitesType__Etunit_TestsuitesType", None)
        self.__Etunit_TestsuitesType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_DocumentRoot19"):
                opp_val = getattr(old_value, "Etunit_DocumentRoot19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_DocumentRoot19"):
                opp_val = getattr(value, "Etunit_DocumentRoot19", None)
                if opp_val is None:
                    setattr(value, "Etunit_DocumentRoot19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Etunit_TestsuiteType:

    def __init__(self, systemOut: str, systemErr: str, disabled: str, errors: str, time: str, timestamp: str, failures: str, hostname: str, id: str, name: str, package: str, skipped: str, tests: str, Etunit_TestsuiteType: "Etunit_DocumentRoot" = None, Etunit_TestsuiteType36: "Etunit_PropertiesType" = None, Etunit_TestsuiteType39: set["Etunit_TestcaseType"] = None, Etunit_TestsuiteType34: "Etunit_TestsuitesType" = None):
        self.systemOut = systemOut
        self.systemErr = systemErr
        self.disabled = disabled
        self.errors = errors
        self.time = time
        self.timestamp = timestamp
        self.failures = failures
        self.hostname = hostname
        self.id = id
        self.name = name
        self.package = package
        self.skipped = skipped
        self.tests = tests
        self.Etunit_TestsuiteType = Etunit_TestsuiteType
        self.Etunit_TestsuiteType36 = Etunit_TestsuiteType36
        self.Etunit_TestsuiteType39 = Etunit_TestsuiteType39 if Etunit_TestsuiteType39 is not None else set()
        self.Etunit_TestsuiteType34 = Etunit_TestsuiteType34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hostname(self) -> str:
        return self.__hostname

    @hostname.setter
    def hostname(self, hostname: str):
        self.__hostname = hostname

    @property
    def skipped(self) -> str:
        return self.__skipped

    @skipped.setter
    def skipped(self, skipped: str):
        self.__skipped = skipped

    @property
    def errors(self) -> str:
        return self.__errors

    @errors.setter
    def errors(self, errors: str):
        self.__errors = errors

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def failures(self) -> str:
        return self.__failures

    @failures.setter
    def failures(self, failures: str):
        self.__failures = failures

    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def timestamp(self) -> str:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp

    @property
    def systemErr(self) -> str:
        return self.__systemErr

    @systemErr.setter
    def systemErr(self, systemErr: str):
        self.__systemErr = systemErr

    @property
    def disabled(self) -> str:
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: str):
        self.__disabled = disabled

    @property
    def tests(self) -> str:
        return self.__tests

    @tests.setter
    def tests(self, tests: str):
        self.__tests = tests

    @property
    def systemOut(self) -> str:
        return self.__systemOut

    @systemOut.setter
    def systemOut(self, systemOut: str):
        self.__systemOut = systemOut

    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def Etunit_TestsuiteType36(self):
        return self.__Etunit_TestsuiteType36

    @Etunit_TestsuiteType36.setter
    def Etunit_TestsuiteType36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_TestsuiteType__Etunit_TestsuiteType36", None)
        self.__Etunit_TestsuiteType36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_PropertiesType37"):
                opp_val = getattr(old_value, "Etunit_PropertiesType37", None)
                if opp_val == self:
                    setattr(old_value, "Etunit_PropertiesType37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_PropertiesType37"):
                opp_val = getattr(value, "Etunit_PropertiesType37", None)
                setattr(value, "Etunit_PropertiesType37", self)

    @property
    def Etunit_TestsuiteType39(self):
        return self.__Etunit_TestsuiteType39

    @Etunit_TestsuiteType39.setter
    def Etunit_TestsuiteType39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_TestsuiteType__Etunit_TestsuiteType39", None)
        self.__Etunit_TestsuiteType39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Etunit_TestcaseType40"):
                    opp_val = getattr(item, "Etunit_TestcaseType40", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_TestcaseType40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_TestcaseType40"):
                    opp_val = getattr(item, "Etunit_TestcaseType40", None)
                    
                    setattr(item, "Etunit_TestcaseType40", self)
                    

    @property
    def Etunit_TestsuiteType34(self):
        return self.__Etunit_TestsuiteType34

    @Etunit_TestsuiteType34.setter
    def Etunit_TestsuiteType34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_TestsuiteType__Etunit_TestsuiteType34", None)
        self.__Etunit_TestsuiteType34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_TestsuitesType33"):
                opp_val = getattr(old_value, "Etunit_TestsuitesType33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_TestsuitesType33"):
                opp_val = getattr(value, "Etunit_TestsuitesType33", None)
                if opp_val is None:
                    setattr(value, "Etunit_TestsuitesType33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Etunit_TestsuiteType(self):
        return self.__Etunit_TestsuiteType

    @Etunit_TestsuiteType.setter
    def Etunit_TestsuiteType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_TestsuiteType__Etunit_TestsuiteType", None)
        self.__Etunit_TestsuiteType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_DocumentRoot17"):
                opp_val = getattr(old_value, "Etunit_DocumentRoot17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_DocumentRoot17"):
                opp_val = getattr(value, "Etunit_DocumentRoot17", None)
                if opp_val is None:
                    setattr(value, "Etunit_DocumentRoot17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Etunit_TestcaseType:

    def __init__(self, systemErr: str, assertions: str, classname: str, name: str, status: str, time: str, systemOut: str, Etunit_TestcaseType: "Etunit_DocumentRoot" = None, Etunit_TestcaseType24: "Etunit_SkippedType" = None, Etunit_TestcaseType27: set["Etunit_ErrorType"] = None, Etunit_TestcaseType30: set["Etunit_FailureType"] = None, Etunit_TestcaseType40: "Etunit_TestsuiteType" = None):
        self.systemErr = systemErr
        self.assertions = assertions
        self.classname = classname
        self.name = name
        self.status = status
        self.time = time
        self.systemOut = systemOut
        self.Etunit_TestcaseType = Etunit_TestcaseType
        self.Etunit_TestcaseType24 = Etunit_TestcaseType24
        self.Etunit_TestcaseType27 = Etunit_TestcaseType27 if Etunit_TestcaseType27 is not None else set()
        self.Etunit_TestcaseType30 = Etunit_TestcaseType30 if Etunit_TestcaseType30 is not None else set()
        self.Etunit_TestcaseType40 = Etunit_TestcaseType40
        
    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def assertions(self) -> str:
        return self.__assertions

    @assertions.setter
    def assertions(self, assertions: str):
        self.__assertions = assertions

    @property
    def systemErr(self) -> str:
        return self.__systemErr

    @systemErr.setter
    def systemErr(self, systemErr: str):
        self.__systemErr = systemErr

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def systemOut(self) -> str:
        return self.__systemOut

    @systemOut.setter
    def systemOut(self, systemOut: str):
        self.__systemOut = systemOut

    @property
    def classname(self) -> str:
        return self.__classname

    @classname.setter
    def classname(self, classname: str):
        self.__classname = classname

    @property
    def Etunit_TestcaseType24(self):
        return self.__Etunit_TestcaseType24

    @Etunit_TestcaseType24.setter
    def Etunit_TestcaseType24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_TestcaseType__Etunit_TestcaseType24", None)
        self.__Etunit_TestcaseType24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_SkippedType25"):
                opp_val = getattr(old_value, "Etunit_SkippedType25", None)
                if opp_val == self:
                    setattr(old_value, "Etunit_SkippedType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_SkippedType25"):
                opp_val = getattr(value, "Etunit_SkippedType25", None)
                setattr(value, "Etunit_SkippedType25", self)

    @property
    def Etunit_TestcaseType30(self):
        return self.__Etunit_TestcaseType30

    @Etunit_TestcaseType30.setter
    def Etunit_TestcaseType30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_TestcaseType__Etunit_TestcaseType30", None)
        self.__Etunit_TestcaseType30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Etunit_FailureType31"):
                    opp_val = getattr(item, "Etunit_FailureType31", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_FailureType31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_FailureType31"):
                    opp_val = getattr(item, "Etunit_FailureType31", None)
                    
                    setattr(item, "Etunit_FailureType31", self)
                    

    @property
    def Etunit_TestcaseType27(self):
        return self.__Etunit_TestcaseType27

    @Etunit_TestcaseType27.setter
    def Etunit_TestcaseType27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_TestcaseType__Etunit_TestcaseType27", None)
        self.__Etunit_TestcaseType27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Etunit_ErrorType28"):
                    opp_val = getattr(item, "Etunit_ErrorType28", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_ErrorType28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_ErrorType28"):
                    opp_val = getattr(item, "Etunit_ErrorType28", None)
                    
                    setattr(item, "Etunit_ErrorType28", self)
                    

    @property
    def Etunit_TestcaseType40(self):
        return self.__Etunit_TestcaseType40

    @Etunit_TestcaseType40.setter
    def Etunit_TestcaseType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_TestcaseType__Etunit_TestcaseType40", None)
        self.__Etunit_TestcaseType40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etunit_TestsuiteType39"):
                opp_val = getattr(old_value, "Etunit_TestsuiteType39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_TestsuiteType39"):
                opp_val = getattr(value, "Etunit_TestsuiteType39", None)
                if opp_val is None:
                    setattr(value, "Etunit_TestsuiteType39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Etunit_DocumentRoot15"):
                opp_val = getattr(old_value, "Etunit_DocumentRoot15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etunit_DocumentRoot15"):
                opp_val = getattr(value, "Etunit_DocumentRoot15", None)
                if opp_val is None:
                    setattr(value, "Etunit_DocumentRoot15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Etunit_EStringToStringMapEntry:

    pass
class Etunit_DocumentRoot:

    def __init__(self, mixed: str, systemErr: str, systemOut: str, Etunit_DocumentRoot: set["Etunit_EStringToStringMapEntry"] = None, Etunit_DocumentRoot2: set["Etunit_EStringToStringMapEntry"] = None, Etunit_DocumentRoot15: set["Etunit_TestcaseType"] = None, Etunit_DocumentRoot17: set["Etunit_TestsuiteType"] = None, Etunit_DocumentRoot19: set["Etunit_TestsuitesType"] = None, Etunit_DocumentRoot5: set["Etunit_ErrorType"] = None, Etunit_DocumentRoot7: set["Etunit_FailureType"] = None, Etunit_DocumentRoot9: set["Etunit_PropertiesType"] = None, Etunit_DocumentRoot11: set["Etunit_PropertyType"] = None, Etunit_DocumentRoot13: set["Etunit_SkippedType"] = None):
        self.mixed = mixed
        self.systemErr = systemErr
        self.systemOut = systemOut
        self.Etunit_DocumentRoot = Etunit_DocumentRoot if Etunit_DocumentRoot is not None else set()
        self.Etunit_DocumentRoot2 = Etunit_DocumentRoot2 if Etunit_DocumentRoot2 is not None else set()
        self.Etunit_DocumentRoot15 = Etunit_DocumentRoot15 if Etunit_DocumentRoot15 is not None else set()
        self.Etunit_DocumentRoot17 = Etunit_DocumentRoot17 if Etunit_DocumentRoot17 is not None else set()
        self.Etunit_DocumentRoot19 = Etunit_DocumentRoot19 if Etunit_DocumentRoot19 is not None else set()
        self.Etunit_DocumentRoot5 = Etunit_DocumentRoot5 if Etunit_DocumentRoot5 is not None else set()
        self.Etunit_DocumentRoot7 = Etunit_DocumentRoot7 if Etunit_DocumentRoot7 is not None else set()
        self.Etunit_DocumentRoot9 = Etunit_DocumentRoot9 if Etunit_DocumentRoot9 is not None else set()
        self.Etunit_DocumentRoot11 = Etunit_DocumentRoot11 if Etunit_DocumentRoot11 is not None else set()
        self.Etunit_DocumentRoot13 = Etunit_DocumentRoot13 if Etunit_DocumentRoot13 is not None else set()
        
    @property
    def systemErr(self) -> str:
        return self.__systemErr

    @systemErr.setter
    def systemErr(self, systemErr: str):
        self.__systemErr = systemErr

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def systemOut(self) -> str:
        return self.__systemOut

    @systemOut.setter
    def systemOut(self, systemOut: str):
        self.__systemOut = systemOut

    @property
    def Etunit_DocumentRoot11(self):
        return self.__Etunit_DocumentRoot11

    @Etunit_DocumentRoot11.setter
    def Etunit_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_DocumentRoot__Etunit_DocumentRoot11", None)
        self.__Etunit_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Etunit_PropertyType"):
                    opp_val = getattr(item, "Etunit_PropertyType", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_PropertyType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_PropertyType"):
                    opp_val = getattr(item, "Etunit_PropertyType", None)
                    
                    setattr(item, "Etunit_PropertyType", self)
                    

    @property
    def Etunit_DocumentRoot9(self):
        return self.__Etunit_DocumentRoot9

    @Etunit_DocumentRoot9.setter
    def Etunit_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_DocumentRoot__Etunit_DocumentRoot9", None)
        self.__Etunit_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Etunit_PropertiesType"):
                    opp_val = getattr(item, "Etunit_PropertiesType", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_PropertiesType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_PropertiesType"):
                    opp_val = getattr(item, "Etunit_PropertiesType", None)
                    
                    setattr(item, "Etunit_PropertiesType", self)
                    

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
                if hasattr(item, "Etunit_ErrorType"):
                    opp_val = getattr(item, "Etunit_ErrorType", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_ErrorType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_ErrorType"):
                    opp_val = getattr(item, "Etunit_ErrorType", None)
                    
                    setattr(item, "Etunit_ErrorType", self)
                    

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
                if hasattr(item, "Etunit_FailureType"):
                    opp_val = getattr(item, "Etunit_FailureType", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_FailureType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_FailureType"):
                    opp_val = getattr(item, "Etunit_FailureType", None)
                    
                    setattr(item, "Etunit_FailureType", self)
                    

    @property
    def Etunit_DocumentRoot13(self):
        return self.__Etunit_DocumentRoot13

    @Etunit_DocumentRoot13.setter
    def Etunit_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_DocumentRoot__Etunit_DocumentRoot13", None)
        self.__Etunit_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Etunit_SkippedType"):
                    opp_val = getattr(item, "Etunit_SkippedType", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_SkippedType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_SkippedType"):
                    opp_val = getattr(item, "Etunit_SkippedType", None)
                    
                    setattr(item, "Etunit_SkippedType", self)
                    

    @property
    def Etunit_DocumentRoot17(self):
        return self.__Etunit_DocumentRoot17

    @Etunit_DocumentRoot17.setter
    def Etunit_DocumentRoot17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_DocumentRoot__Etunit_DocumentRoot17", None)
        self.__Etunit_DocumentRoot17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Etunit_TestsuiteType"):
                    opp_val = getattr(item, "Etunit_TestsuiteType", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_TestsuiteType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_TestsuiteType"):
                    opp_val = getattr(item, "Etunit_TestsuiteType", None)
                    
                    setattr(item, "Etunit_TestsuiteType", self)
                    

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
    def Etunit_DocumentRoot19(self):
        return self.__Etunit_DocumentRoot19

    @Etunit_DocumentRoot19.setter
    def Etunit_DocumentRoot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_DocumentRoot__Etunit_DocumentRoot19", None)
        self.__Etunit_DocumentRoot19 = value if value is not None else set()
        
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
    def Etunit_DocumentRoot15(self):
        return self.__Etunit_DocumentRoot15

    @Etunit_DocumentRoot15.setter
    def Etunit_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etunit_DocumentRoot__Etunit_DocumentRoot15", None)
        self.__Etunit_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Etunit_TestcaseType"):
                    opp_val = getattr(item, "Etunit_TestcaseType", None)
                    
                    if opp_val == self:
                        setattr(item, "Etunit_TestcaseType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Etunit_TestcaseType"):
                    opp_val = getattr(item, "Etunit_TestcaseType", None)
                    
                    setattr(item, "Etunit_TestcaseType", self)
                    
