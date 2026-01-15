from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Day(Enum):
    SUNDAY = "SUNDAY"
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
class OccursMode(Enum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
class DayOccurrence(Enum):
    FIRST = "FIRST"
    SECOND = "SECOND"
    THIRD = "THIRD"
    FOURTH = "FOURTH"
    LAST = "LAST"


############################################
# Definition of Classes
############################################

class OccursModel:

    pass
class timeBasedRouting_DailyOccursModel(OccursModel):

    def __init__(self, skipDays: int, startDate: date):
        self.skipDays = skipDays
        self.startDate = startDate
        
    @property
    def skipDays(self) -> int:
        return self.__skipDays

    @skipDays.setter
    def skipDays(self, skipDays: int):
        self.__skipDays = skipDays

    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

class timeBasedRouting_TimeRange:

    def __init__(self, endRange: date, name: str, startRange: date, timeBasedRouting_TimeRange: "timeBasedRouting_OccursModel" = None):
        self.endRange = endRange
        self.name = name
        self.startRange = startRange
        self.timeBasedRouting_TimeRange = timeBasedRouting_TimeRange
        
    @property
    def startRange(self) -> date:
        return self.__startRange

    @startRange.setter
    def startRange(self, startRange: date):
        self.__startRange = startRange

    @property
    def endRange(self) -> date:
        return self.__endRange

    @endRange.setter
    def endRange(self, endRange: date):
        self.__endRange = endRange

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def timeBasedRouting_TimeRange(self):
        return self.__timeBasedRouting_TimeRange

    @timeBasedRouting_TimeRange.setter
    def timeBasedRouting_TimeRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timeBasedRouting_TimeRange__timeBasedRouting_TimeRange", None)
        self.__timeBasedRouting_TimeRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timeBasedRouting_OccursModel"):
                opp_val = getattr(old_value, "timeBasedRouting_OccursModel", None)
                if opp_val == self:
                    setattr(old_value, "timeBasedRouting_OccursModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timeBasedRouting_OccursModel"):
                opp_val = getattr(value, "timeBasedRouting_OccursModel", None)
                setattr(value, "timeBasedRouting_OccursModel", self)

    def isMatch(self, date: date) -> bool:
        # TODO: Implement isMatch method
        pass

class timeBasedRouting_MonthlyOccursModel(OccursModel):

    def __init__(self, byIndex: bool, skipMonths: int, dayIndex: int, dayOccurence: str, day: str, startDate: date):
        self.byIndex = byIndex
        self.skipMonths = skipMonths
        self.dayIndex = dayIndex
        self.dayOccurence = dayOccurence
        self.day = day
        self.startDate = startDate
        
    @property
    def dayOccurence(self) -> str:
        return self.__dayOccurence

    @dayOccurence.setter
    def dayOccurence(self, dayOccurence: str):
        self.__dayOccurence = dayOccurence

    @property
    def dayIndex(self) -> int:
        return self.__dayIndex

    @dayIndex.setter
    def dayIndex(self, dayIndex: int):
        self.__dayIndex = dayIndex

    @property
    def skipMonths(self) -> int:
        return self.__skipMonths

    @skipMonths.setter
    def skipMonths(self, skipMonths: int):
        self.__skipMonths = skipMonths

    @property
    def byIndex(self) -> bool:
        return self.__byIndex

    @byIndex.setter
    def byIndex(self, byIndex: bool):
        self.__byIndex = byIndex

    @property
    def day(self) -> str:
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day

    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

class timeBasedRouting_WeeklyOccursModel(OccursModel):

    def __init__(self, skipWeeks: int, days: str, startDate: date):
        self.skipWeeks = skipWeeks
        self.days = days
        self.startDate = startDate
        
    @property
    def days(self) -> str:
        return self.__days

    @days.setter
    def days(self, days: str):
        self.__days = days

    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def skipWeeks(self) -> int:
        return self.__skipWeeks

    @skipWeeks.setter
    def skipWeeks(self, skipWeeks: int):
        self.__skipWeeks = skipWeeks

class timeBasedRouting_OccursModel:

    def __init__(self, mode: str, description: str, timeBasedRouting_OccursModel: "timeBasedRouting_TimeRange" = None):
        self.mode = mode
        self.description = description
        self.timeBasedRouting_OccursModel = timeBasedRouting_OccursModel
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def timeBasedRouting_OccursModel(self):
        return self.__timeBasedRouting_OccursModel

    @timeBasedRouting_OccursModel.setter
    def timeBasedRouting_OccursModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timeBasedRouting_OccursModel__timeBasedRouting_OccursModel", None)
        self.__timeBasedRouting_OccursModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timeBasedRouting_TimeRange"):
                opp_val = getattr(old_value, "timeBasedRouting_TimeRange", None)
                if opp_val == self:
                    setattr(old_value, "timeBasedRouting_TimeRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timeBasedRouting_TimeRange"):
                opp_val = getattr(value, "timeBasedRouting_TimeRange", None)
                setattr(value, "timeBasedRouting_TimeRange", self)

    def isMatch(self, date: date) -> bool:
        # TODO: Implement isMatch method
        pass

class CaseItem:

    pass
class timeBasedRouting_TimeItem(CaseItem):

    def __init__(self, description: str, timeBasedRouting_TimeItem: "timeBasedRouting_TimeBasedRouting" = None):
        self.description = description
        self.timeBasedRouting_TimeItem = timeBasedRouting_TimeItem
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def timeBasedRouting_TimeItem(self):
        return self.__timeBasedRouting_TimeItem

    @timeBasedRouting_TimeItem.setter
    def timeBasedRouting_TimeItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timeBasedRouting_TimeItem__timeBasedRouting_TimeItem", None)
        self.__timeBasedRouting_TimeItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timeBasedRouting_TimeBasedRouting2"):
                opp_val = getattr(old_value, "timeBasedRouting_TimeBasedRouting2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timeBasedRouting_TimeBasedRouting2"):
                opp_val = getattr(value, "timeBasedRouting_TimeBasedRouting2", None)
                if opp_val is None:
                    setattr(value, "timeBasedRouting_TimeBasedRouting2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DynamicValue:

    pass
class ActionStep:

    pass
class timeBasedRouting_TimeBasedRouting(ActionStep):

    pass