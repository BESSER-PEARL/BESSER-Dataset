from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tests_Test:

    def __init__(self, id: str, version: str, tests_Test: "tests_TestsModel" = None):
        self.id = id
        self.version = version
        self.tests_Test = tests_Test
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def tests_Test(self):
        return self.__tests_Test

    @tests_Test.setter
    def tests_Test(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tests_Test__tests_Test", None)
        self.__tests_Test = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tests_TestsModel"):
                opp_val = getattr(old_value, "tests_TestsModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tests_TestsModel"):
                opp_val = getattr(value, "tests_TestsModel", None)
                if opp_val is None:
                    setattr(value, "tests_TestsModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tests_TestsModel:

    pass