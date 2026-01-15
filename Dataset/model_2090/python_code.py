from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TimeStampedElement:

    pass
class ChangingOverTime_BindingKind(TimeStampedElement):

    pass
class ChangingOverTime_NodeKind(TimeStampedElement):

    pass
class ChangingOverTime_Tree:

    pass
class ChangingOverTime_LinkKind:

    pass
class ChangingOverTime_Entity(TimeStampedElement):

    pass
class ChangingOverTime_TimeStampedElement:

    def __init__(self, effectiveDate: date, expirationDate: date):
        self.effectiveDate = effectiveDate
        self.expirationDate = expirationDate
        
    @property
    def effectiveDate(self) -> date:
        return self.__effectiveDate

    @effectiveDate.setter
    def effectiveDate(self, effectiveDate: date):
        self.__effectiveDate = effectiveDate

    @property
    def expirationDate(self) -> date:
        return self.__expirationDate

    @expirationDate.setter
    def expirationDate(self, expirationDate: date):
        self.__expirationDate = expirationDate
