from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ValidationModel_TestContainer:

    pass
class ValidationModel_UnitTest:

    def __init__(self, name: str, id: str, isTested: bool, ValidationModel_UnitTest: "ValidationModel_TestContainer" = None):
        self.name = name
        self.id = id
        self.isTested = isTested
        self.ValidationModel_UnitTest = ValidationModel_UnitTest
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def isTested(self) -> bool:
        return self.__isTested

    @isTested.setter
    def isTested(self, isTested: bool):
        self.__isTested = isTested

    @property
    def ValidationModel_UnitTest(self):
        return self.__ValidationModel_UnitTest

    @ValidationModel_UnitTest.setter
    def ValidationModel_UnitTest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ValidationModel_UnitTest__ValidationModel_UnitTest", None)
        self.__ValidationModel_UnitTest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValidationModel_TestContainer"):
                opp_val = getattr(old_value, "ValidationModel_TestContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValidationModel_TestContainer"):
                opp_val = getattr(value, "ValidationModel_TestContainer", None)
                if opp_val is None:
                    setattr(value, "ValidationModel_TestContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
