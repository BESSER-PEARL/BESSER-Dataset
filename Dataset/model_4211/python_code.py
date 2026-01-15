from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class testFramework_Model:

    pass
class testFramework_LABEL:

    def __init__(self, labelvalue: str, testFramework_LABEL: "testFramework_TABLEACTION" = None):
        self.labelvalue = labelvalue
        self.testFramework_LABEL = testFramework_LABEL
        
    @property
    def labelvalue(self) -> str:
        return self.__labelvalue

    @labelvalue.setter
    def labelvalue(self, labelvalue: str):
        self.__labelvalue = labelvalue

    @property
    def testFramework_LABEL(self):
        return self.__testFramework_LABEL

    @testFramework_LABEL.setter
    def testFramework_LABEL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testFramework_LABEL__testFramework_LABEL", None)
        self.__testFramework_LABEL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testFramework_TABLEACTION8"):
                opp_val = getattr(old_value, "testFramework_TABLEACTION8", None)
                if opp_val == self:
                    setattr(old_value, "testFramework_TABLEACTION8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testFramework_TABLEACTION8"):
                opp_val = getattr(value, "testFramework_TABLEACTION8", None)
                setattr(value, "testFramework_TABLEACTION8", self)

class testFramework_IDENTIFIER:

    def __init__(self, identifiervalue: str, testFramework_IDENTIFIER: "testFramework_TABLEACTION" = None):
        self.identifiervalue = identifiervalue
        self.testFramework_IDENTIFIER = testFramework_IDENTIFIER
        
    @property
    def identifiervalue(self) -> str:
        return self.__identifiervalue

    @identifiervalue.setter
    def identifiervalue(self, identifiervalue: str):
        self.__identifiervalue = identifiervalue

    @property
    def testFramework_IDENTIFIER(self):
        return self.__testFramework_IDENTIFIER

    @testFramework_IDENTIFIER.setter
    def testFramework_IDENTIFIER(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testFramework_IDENTIFIER__testFramework_IDENTIFIER", None)
        self.__testFramework_IDENTIFIER = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testFramework_TABLEACTION6"):
                opp_val = getattr(old_value, "testFramework_TABLEACTION6", None)
                if opp_val == self:
                    setattr(old_value, "testFramework_TABLEACTION6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testFramework_TABLEACTION6"):
                opp_val = getattr(value, "testFramework_TABLEACTION6", None)
                setattr(value, "testFramework_TABLEACTION6", self)

class testFramework_TABLEACTION:

    pass
class testFramework_FIRSTACTION:

    def __init__(self, checktableAction: str, testFramework_FIRSTACTION: "testFramework_Greeting" = None, testFramework_FIRSTACTION4: "testFramework_TABLEACTION" = None):
        self.checktableAction = checktableAction
        self.testFramework_FIRSTACTION = testFramework_FIRSTACTION
        self.testFramework_FIRSTACTION4 = testFramework_FIRSTACTION4
        
    @property
    def checktableAction(self) -> str:
        return self.__checktableAction

    @checktableAction.setter
    def checktableAction(self, checktableAction: str):
        self.__checktableAction = checktableAction

    @property
    def testFramework_FIRSTACTION(self):
        return self.__testFramework_FIRSTACTION

    @testFramework_FIRSTACTION.setter
    def testFramework_FIRSTACTION(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testFramework_FIRSTACTION__testFramework_FIRSTACTION", None)
        self.__testFramework_FIRSTACTION = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testFramework_Greeting2"):
                opp_val = getattr(old_value, "testFramework_Greeting2", None)
                if opp_val == self:
                    setattr(old_value, "testFramework_Greeting2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testFramework_Greeting2"):
                opp_val = getattr(value, "testFramework_Greeting2", None)
                setattr(value, "testFramework_Greeting2", self)

    @property
    def testFramework_FIRSTACTION4(self):
        return self.__testFramework_FIRSTACTION4

    @testFramework_FIRSTACTION4.setter
    def testFramework_FIRSTACTION4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testFramework_FIRSTACTION__testFramework_FIRSTACTION4", None)
        self.__testFramework_FIRSTACTION4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testFramework_TABLEACTION"):
                opp_val = getattr(old_value, "testFramework_TABLEACTION", None)
                if opp_val == self:
                    setattr(old_value, "testFramework_TABLEACTION", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testFramework_TABLEACTION"):
                opp_val = getattr(value, "testFramework_TABLEACTION", None)
                setattr(value, "testFramework_TABLEACTION", self)

class testFramework_Greeting:

    def __init__(self, testcaseValue: int, summaryDetails: str, testFramework_Greeting: "testFramework_Model" = None, testFramework_Greeting2: "testFramework_FIRSTACTION" = None):
        self.testcaseValue = testcaseValue
        self.summaryDetails = summaryDetails
        self.testFramework_Greeting = testFramework_Greeting
        self.testFramework_Greeting2 = testFramework_Greeting2
        
    @property
    def summaryDetails(self) -> str:
        return self.__summaryDetails

    @summaryDetails.setter
    def summaryDetails(self, summaryDetails: str):
        self.__summaryDetails = summaryDetails

    @property
    def testcaseValue(self) -> int:
        return self.__testcaseValue

    @testcaseValue.setter
    def testcaseValue(self, testcaseValue: int):
        self.__testcaseValue = testcaseValue

    @property
    def testFramework_Greeting(self):
        return self.__testFramework_Greeting

    @testFramework_Greeting.setter
    def testFramework_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testFramework_Greeting__testFramework_Greeting", None)
        self.__testFramework_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testFramework_Model"):
                opp_val = getattr(old_value, "testFramework_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testFramework_Model"):
                opp_val = getattr(value, "testFramework_Model", None)
                if opp_val is None:
                    setattr(value, "testFramework_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def testFramework_Greeting2(self):
        return self.__testFramework_Greeting2

    @testFramework_Greeting2.setter
    def testFramework_Greeting2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testFramework_Greeting__testFramework_Greeting2", None)
        self.__testFramework_Greeting2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testFramework_FIRSTACTION"):
                opp_val = getattr(old_value, "testFramework_FIRSTACTION", None)
                if opp_val == self:
                    setattr(old_value, "testFramework_FIRSTACTION", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testFramework_FIRSTACTION"):
                opp_val = getattr(value, "testFramework_FIRSTACTION", None)
                setattr(value, "testFramework_FIRSTACTION", self)
