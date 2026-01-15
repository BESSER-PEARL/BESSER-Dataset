from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class testing_TestCoverage:

    pass
class testing_TestSuite:

    def __init__(self, sutName: str, testing_TestSuite2: "testing_Adapter" = None, testing_TestSuite: set["testing_TestCoverage"] = None):
        self.sutName = sutName
        self.testing_TestSuite2 = testing_TestSuite2
        self.testing_TestSuite = testing_TestSuite if testing_TestSuite is not None else set()
        
    @property
    def sutName(self) -> str:
        return self.__sutName

    @sutName.setter
    def sutName(self, sutName: str):
        self.__sutName = sutName

    @property
    def testing_TestSuite(self):
        return self.__testing_TestSuite

    @testing_TestSuite.setter
    def testing_TestSuite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testing_TestSuite__testing_TestSuite", None)
        self.__testing_TestSuite = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testing_TestCoverage"):
                    opp_val = getattr(item, "testing_TestCoverage", None)
                    
                    if opp_val == self:
                        setattr(item, "testing_TestCoverage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testing_TestCoverage"):
                    opp_val = getattr(item, "testing_TestCoverage", None)
                    
                    setattr(item, "testing_TestCoverage", self)
                    

    @property
    def testing_TestSuite2(self):
        return self.__testing_TestSuite2

    @testing_TestSuite2.setter
    def testing_TestSuite2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testing_TestSuite__testing_TestSuite2", None)
        self.__testing_TestSuite2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testing_Adapter"):
                opp_val = getattr(old_value, "testing_Adapter", None)
                if opp_val == self:
                    setattr(old_value, "testing_Adapter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testing_Adapter"):
                opp_val = getattr(value, "testing_Adapter", None)
                setattr(value, "testing_Adapter", self)

class testing_TestCase:

    def __init__(self, input: str, output: str, testing_TestCase: "testing_TestCoverage" = None):
        self.input = input
        self.output = output
        self.testing_TestCase = testing_TestCase
        
    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def testing_TestCase(self):
        return self.__testing_TestCase

    @testing_TestCase.setter
    def testing_TestCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testing_TestCase__testing_TestCase", None)
        self.__testing_TestCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testing_TestCoverage6"):
                opp_val = getattr(old_value, "testing_TestCoverage6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testing_TestCoverage6"):
                opp_val = getattr(value, "testing_TestCoverage6", None)
                if opp_val is None:
                    setattr(value, "testing_TestCoverage6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class testing_Transition:

    def __init__(self, name: str, type: str, testing_Transition: "testing_Adapter" = None):
        self.name = name
        self.type = type
        self.testing_Transition = testing_Transition
        
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
    def testing_Transition(self):
        return self.__testing_Transition

    @testing_Transition.setter
    def testing_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testing_Transition__testing_Transition", None)
        self.__testing_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testing_Adapter4"):
                opp_val = getattr(old_value, "testing_Adapter4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testing_Adapter4"):
                opp_val = getattr(value, "testing_Adapter4", None)
                if opp_val is None:
                    setattr(value, "testing_Adapter4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class testing_Adapter:

    pass