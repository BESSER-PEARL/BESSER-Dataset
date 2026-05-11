from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TraceStackframe:

    pass
class junitmodel_JUnitTraceStackframe(TraceStackframe):

    pass
class ComparisonProblem:

    pass
class JUnitProblem:

    pass
class junitmodel_JUnitComparisonProblem(ComparisonProblem, JUnitProblem):

    pass
class TestProblem:

    pass
class junitmodel_JUnitProblem(TestProblem):

    def __init__(self, lastTraceWasFiltered: bool):
        self.lastTraceWasFiltered = lastTraceWasFiltered
        
        pass
    @property
    def lastTraceWasFiltered(self):
        return self.__lastTraceWasFiltered

    @lastTraceWasFiltered.setter
    def lastTraceWasFiltered(self, lastTraceWasFiltered: bool):
        self.__lastTraceWasFiltered = lastTraceWasFiltered


class TestRoot:

    pass
class junitmodel_JUnitRoot(TestRoot):

    pass
class TestContainer:

    pass
class junitmodel_JUnitTestSuite(TestContainer):

    pass
class TestCaseElement:

    pass
class junitmodel_JUnitTestCase(TestCaseElement):

    pass