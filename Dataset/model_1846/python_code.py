from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ChargeApplies(Enum):
    ONSTART = "ONSTART"
    ONEND = "ONEND"
    PERHOUR = "PERHOUR"
    PERDAY = "PERDAY"
    PERWEEK = "PERWEEK"
class CriterionDirection(Enum):
    UP = "UP"
    DOWN = "DOWN"
class ListTypeValues(Enum):
    BULLETS = "BULLETS"
    COMMA = "COMMA"
    NUMBERED = "NUMBERED"
class JournalModeValue(Enum):
    JOURNAL = "JOURNAL"
    JOURNAL_SUB = "JOURNAL_SUB"
    STATUS_DOWN = "STATUS_DOWN"
    STATUS_UP = "STATUS_UP"
    ALERTS_DOWN = "ALERTS_DOWN"
class PurgeTaskAttribute(Enum):
    BOOKING = "BOOKING"
    CHARGE = "CHARGE"
    CHARGESET = "CHARGESET"
    DEPENDS = "DEPENDS"
    FAIL = "FAIL"
    FLAGS = "FLAGS"
    PRECEDES = "PRECEDES"
    WARN = "WARN"
class ColumnId(Enum):
    ALERT = "ALERT"
    ALERTMESSAGE = "ALERTMESSAGE"
    ALERTSUMMARY = "ALERTSUMMARY"
    ALERTTREND = "ALERTTREND"
    CHART = "CHART"
    EFFICIENCY = "EFFICIENCY"
    EFFORT = "EFFORT"
    EFFORTDONE = "EFFORTDONE"
    EFFORTLEFT = "EFFORTLEFT"
    EMAIL = "EMAIL"
    END = "END"
    FLAGS = "FLAGS"
    FOLLOWERS = "FOLLOWERS"
    FREETIME = "FREETIME"
    FREEWORK = "FREEWORK"
    FTE = "FTE"
    HEADCOUNT = "HEADCOUNT"
    HIERARCHINDEX = "HIERARCHINDEX"
    HOURLY = "HOURLY"
    ID = "ID"
    INDEX = "INDEX"
    JOURNAL = "JOURNAL"
    LINE = "LINE"
    MAXEND = "MAXEND"
    MAXSTART = "MAXSTART"
    MINEND = "MINEND"
    COMPLETE = "COMPLETE"
    COMPLETED = "COMPLETED"
    CRITICALNESS = "CRITICALNESS"
    COST = "COST"
    DAILY = "DAILY"
    DURATION = "DURATION"
    DUTIES = "DUTIES"
    PRECURSOR = "PRECURSOR"
    PRIORITY = "PRIORITY"
    QUARTERLY = "QUARTERLY"
    RATE = "RATE"
    RESOURCES = "RESOURCES"
    RESPONSIBLE = "RESPONSIBLE"
    REVENUE = "REVENUE"
    SCENARIO = "SCENARIO"
    SEQNO = "SEQNO"
    START = "START"
    STATUS = "STATUS"
    TARGETS = "TARGETS"
    WBS = "WBS"
    WEEKLY = "WEEKLY"
    YEARLY = "YEARLY"
    MINSTART = "MINSTART"
    MONTHLY = "MONTHLY"
    NO = "NO"
    NAME = "NAME"
    NOTE = "NOTE"
    PATHCRITICALNESS = "PATHCRITICALNESS"
class ScaleResolution(Enum):
    WEEK = "WEEK"
    MONTH = "MONTH"
    QUARTER = "QUARTER"
    YEAR = "YEAR"
    HOUR = "HOUR"
    DAY = "DAY"
class YesNo(Enum):
    YES = "YES"
    NO = "NO"
class TimeUnit(Enum):
    MINUTE = "MINUTE"
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"
class SelectArgument(Enum):
    MAXLOADED = "MAXLOADED"
    MINLOADED = "MINLOADED"
    MINALLOCATED = "MINALLOCATED"
    ORDER = "ORDER"
    RANDOM = "RANDOM"
class AlertLevel(Enum):
    RED = "RED"
    YELLOW = "YELLOW"
    GREEN = "GREEN"
class Justification(Enum):
    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"
class Weekday(Enum):
    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THR = "THR"
    FRI = "FRI"
    SAT = "SAT"
    SUN = "SUN"
class PurgeReportAttribute(Enum):
    COLUMNS = "COLUMNS"
    DEFINITIONS = "DEFINITIONS"
    SORTTASKS = "SORTTASKS"
    FLAGS = "FLAGS"
    FORMATS = "FORMATS"
    JOURNALATTRIBUTES = "JOURNALATTRIBUTES"
    SCENARIOS = "SCENARIOS"
    SORTACCOUNTS = "SORTACCOUNTS"
    SORTJOURNALENTRIES = "SORTJOURNALENTRIES"
    SORTRESOURCES = "SORTRESOURCES"
class PurgeResourceAttribute(Enum):
    FAIL = "FAIL"
    FLAGS = "FLAGS"
    MANAGERS = "MANAGERS"
    REPORTS = "REPORTS"
    VACATIONS = "VACATIONS"
    WARN = "WARN"
class ReportFormat(Enum):
    CSV = "CSV"
    HTML = "HTML"
    NIKU = "NIKU"
class SchedulingPolicy(Enum):
    ALAP = "ALAP"
    ASAP = "ASAP"
class WorkQuantityUnit(Enum):
    PERCENT = "PERCENT"
    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"
class JournalEntrySortCriterion(Enum):
    DATE_UP = "DATE_UP"
    ALERT_DOWN = "ALERT_DOWN"
    ALERT_UP = "ALERT_UP"
    PROPERTY_UP = "PROPERTY_UP"
    DATE_DOWN = "DATE_DOWN"
class LoadDisplayUnit(Enum):
    DAYS = "DAYS"
    HOURS = "HOURS"
    LONGAUTO = "LONGAUTO"
    MINUTES = "MINUTES"
    MONTHS = "MONTHS"
    SHORTAUTO = "SHORTAUTO"
    WEEKS = "WEEKS"
    YEARS = "YEARS"
class DependsPolicy(Enum):
    ONEND = "ONEND"
    ONSTART = "ONSTART"


############################################
# Definition of Classes
############################################

class project_JvmIdentifiableElement:

    pass
class LogicalExpression:

    pass
class project_LogicalFunctionExpression(LogicalExpression):

    pass
class project_LogicalDateLiteral(LogicalExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class project_LogicalAbsoluteIdExression(LogicalExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class project_LogicalNumeralLiteral(LogicalExpression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class project_LogicalBooleanLiteral(LogicalExpression):

    def __init__(self, isTrue: bool):
        self.isTrue = isTrue
        
    @property
    def isTrue(self) -> bool:
        return self.__isTrue

    @isTrue.setter
    def isTrue(self, isTrue: bool):
        self.__isTrue = isTrue

class project_LogicalStringLiteral(LogicalExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class project_XBinaryOperation(LogicalExpression):

    pass
class Definitions:

    pass
class project_Defintions(Definitions):

    def __init__(self, flags: bool, resources: bool, tasks: bool, project: bool, projectids: bool):
        self.flags = flags
        self.resources = resources
        self.tasks = tasks
        self.project = project
        self.projectids = projectids
        
    @property
    def tasks(self) -> bool:
        return self.__tasks

    @tasks.setter
    def tasks(self, tasks: bool):
        self.__tasks = tasks

    @property
    def project(self) -> bool:
        return self.__project

    @project.setter
    def project(self, project: bool):
        self.__project = project

    @property
    def projectids(self) -> bool:
        return self.__projectids

    @projectids.setter
    def projectids(self, projectids: bool):
        self.__projectids = projectids

    @property
    def flags(self) -> bool:
        return self.__flags

    @flags.setter
    def flags(self, flags: bool):
        self.__flags = flags

    @property
    def resources(self) -> bool:
        return self.__resources

    @resources.setter
    def resources(self, resources: bool):
        self.__resources = resources

class Summary:

    pass
class Right:

    pass
class Prolog:

    pass
class ListItem:

    pass
class Left:

    pass
class Headline:

    pass
class Header:

    pass
class Footer:

    pass
class Epilog:

    pass
class Details:

    pass
class Center:

    pass
class Caption:

    pass
class project_RichText(Header, Caption, Epilog, Center, Right, ListItem, Prolog, Left, Footer, Details, Summary, Headline):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class Precedes:

    pass
class Depends:

    pass
class project_TaskDependency(Depends, Precedes):

    def __init__(self, policy: str, project_TaskDependency: "project_Task" = None, project_TaskDependency242: "project_GapDuration" = None, project_TaskDependency244: "project_GapLength" = None):
        self.policy = policy
        self.project_TaskDependency = project_TaskDependency
        self.project_TaskDependency242 = project_TaskDependency242
        self.project_TaskDependency244 = project_TaskDependency244
        
    @property
    def policy(self) -> str:
        return self.__policy

    @policy.setter
    def policy(self, policy: str):
        self.__policy = policy

    @property
    def project_TaskDependency242(self):
        return self.__project_TaskDependency242

    @project_TaskDependency242.setter
    def project_TaskDependency242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_TaskDependency__project_TaskDependency242", None)
        self.__project_TaskDependency242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_GapDuration"):
                opp_val = getattr(old_value, "project_GapDuration", None)
                if opp_val == self:
                    setattr(old_value, "project_GapDuration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_GapDuration"):
                opp_val = getattr(value, "project_GapDuration", None)
                setattr(value, "project_GapDuration", self)

    @property
    def project_TaskDependency244(self):
        return self.__project_TaskDependency244

    @project_TaskDependency244.setter
    def project_TaskDependency244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_TaskDependency__project_TaskDependency244", None)
        self.__project_TaskDependency244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_GapLength"):
                opp_val = getattr(old_value, "project_GapLength", None)
                if opp_val == self:
                    setattr(old_value, "project_GapLength", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_GapLength"):
                opp_val = getattr(value, "project_GapLength", None)
                setattr(value, "project_GapLength", self)

    @property
    def project_TaskDependency(self):
        return self.__project_TaskDependency

    @project_TaskDependency.setter
    def project_TaskDependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_TaskDependency__project_TaskDependency", None)
        self.__project_TaskDependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Task240"):
                opp_val = getattr(old_value, "project_Task240", None)
                if opp_val == self:
                    setattr(old_value, "project_Task240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Task240"):
                opp_val = getattr(value, "project_Task240", None)
                setattr(value, "project_Task240", self)

class NumberFormat:

    pass
class CurrencyFormat:

    pass
class project_RealFormat(CurrencyFormat, NumberFormat):

    def __init__(self, thousandsSeparator: str, fractionSeparator: str, fractionDigits: int, negativePrefix: str, negativeSuffix: str):
        self.thousandsSeparator = thousandsSeparator
        self.fractionSeparator = fractionSeparator
        self.fractionDigits = fractionDigits
        self.negativePrefix = negativePrefix
        self.negativeSuffix = negativeSuffix
        
    @property
    def fractionDigits(self) -> int:
        return self.__fractionDigits

    @fractionDigits.setter
    def fractionDigits(self, fractionDigits: int):
        self.__fractionDigits = fractionDigits

    @property
    def negativePrefix(self) -> str:
        return self.__negativePrefix

    @negativePrefix.setter
    def negativePrefix(self, negativePrefix: str):
        self.__negativePrefix = negativePrefix

    @property
    def negativeSuffix(self) -> str:
        return self.__negativeSuffix

    @negativeSuffix.setter
    def negativeSuffix(self, negativeSuffix: str):
        self.__negativeSuffix = negativeSuffix

    @property
    def thousandsSeparator(self) -> str:
        return self.__thousandsSeparator

    @thousandsSeparator.setter
    def thousandsSeparator(self, thousandsSeparator: str):
        self.__thousandsSeparator = thousandsSeparator

    @property
    def fractionSeparator(self) -> str:
        return self.__fractionSeparator

    @fractionSeparator.setter
    def fractionSeparator(self, fractionSeparator: str):
        self.__fractionSeparator = fractionSeparator

class project_LimitAttribute:

    def __init__(self, end: str, start: str, project_LimitAttribute: "project_Limit" = None, project_LimitAttribute234: "project_Interval1" = None, project_LimitAttribute237: set["project_Resource"] = None):
        self.end = end
        self.start = start
        self.project_LimitAttribute = project_LimitAttribute
        self.project_LimitAttribute234 = project_LimitAttribute234
        self.project_LimitAttribute237 = project_LimitAttribute237 if project_LimitAttribute237 is not None else set()
        
    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

    @property
    def project_LimitAttribute234(self):
        return self.__project_LimitAttribute234

    @project_LimitAttribute234.setter
    def project_LimitAttribute234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_LimitAttribute__project_LimitAttribute234", None)
        self.__project_LimitAttribute234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Interval1235"):
                opp_val = getattr(old_value, "project_Interval1235", None)
                if opp_val == self:
                    setattr(old_value, "project_Interval1235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Interval1235"):
                opp_val = getattr(value, "project_Interval1235", None)
                setattr(value, "project_Interval1235", self)

    @property
    def project_LimitAttribute(self):
        return self.__project_LimitAttribute

    @project_LimitAttribute.setter
    def project_LimitAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_LimitAttribute__project_LimitAttribute", None)
        self.__project_LimitAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Limit232"):
                opp_val = getattr(old_value, "project_Limit232", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Limit232"):
                opp_val = getattr(value, "project_Limit232", None)
                if opp_val is None:
                    setattr(value, "project_Limit232", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def project_LimitAttribute237(self):
        return self.__project_LimitAttribute237

    @project_LimitAttribute237.setter
    def project_LimitAttribute237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_LimitAttribute__project_LimitAttribute237", None)
        self.__project_LimitAttribute237 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_Resource238"):
                    opp_val = getattr(item, "project_Resource238", None)
                    
                    if opp_val == self:
                        setattr(item, "project_Resource238", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_Resource238"):
                    opp_val = getattr(item, "project_Resource238", None)
                    
                    setattr(item, "project_Resource238", self)
                    

class WeeklyMin:

    pass
class WeeklyMax:

    pass
class MonthlyMin:

    pass
class MonthlyMax:

    pass
class Minimum:

    pass
class Maximum:

    pass
class DailyMin:

    pass
class DailyMax:

    pass
class project_Limit(WeeklyMin, Minimum, Maximum, DailyMin, MonthlyMin, DailyMax, WeeklyMax, MonthlyMax):

    pass
class GapLength:

    pass
class GapDuration:

    pass
class project_ColumnAttribute:

    pass
class project_WorkHours:

    def __init__(self, start: str, stop: str, project_WorkHours: "project_WorkingHours" = None):
        self.start = start
        self.stop = stop
        self.project_WorkHours = project_WorkHours
        
    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def stop(self) -> str:
        return self.__stop

    @stop.setter
    def stop(self, stop: str):
        self.__stop = stop

    @property
    def project_WorkHours(self):
        return self.__project_WorkHours

    @project_WorkHours.setter
    def project_WorkHours(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_WorkHours__project_WorkHours", None)
        self.__project_WorkHours = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_WorkingHours223"):
                opp_val = getattr(old_value, "project_WorkingHours223", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_WorkingHours223"):
                opp_val = getattr(value, "project_WorkingHours223", None)
                if opp_val is None:
                    setattr(value, "project_WorkingHours223", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class project_Weekdays:

    def __init__(self, first: str, last: str, project_Weekdays: "project_WorkingHours" = None):
        self.first = first
        self.last = last
        self.project_Weekdays = project_Weekdays
        
    @property
    def first(self) -> str:
        return self.__first

    @first.setter
    def first(self, first: str):
        self.__first = first

    @property
    def last(self) -> str:
        return self.__last

    @last.setter
    def last(self, last: str):
        self.__last = last

    @property
    def project_Weekdays(self):
        return self.__project_Weekdays

    @project_Weekdays.setter
    def project_Weekdays(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Weekdays__project_Weekdays", None)
        self.__project_Weekdays = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_WorkingHours221"):
                opp_val = getattr(old_value, "project_WorkingHours221", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_WorkingHours221"):
                opp_val = getattr(value, "project_WorkingHours221", None)
                if opp_val is None:
                    setattr(value, "project_WorkingHours221", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class project_TreeLevel:

    def __init__(self, level: str):
        self.level = level
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

class project_TimesheetReportAttribute:

    pass
class project_TimesheetAttribute:

    pass
class project_TaskTimesheetAttribute:

    pass
class project_TaskStatusSheetAttribute:

    pass
class StatusSheetAttribute:

    pass
class project_StatusSheetReportAttribute:

    pass
class project_StatusSheetAttribute:

    pass
class TaskStatusSheetAttribute:

    pass
class project_TaskStatusSheet(StatusSheetAttribute, TaskStatusSheetAttribute):

    pass
class project_StatusStatusSheet(TaskStatusSheetAttribute):

    def __init__(self, level: str, text: str, project_StatusStatusSheet: set["project_StatusStatusSheetAttribute"] = None):
        self.level = level
        self.text = text
        self.project_StatusStatusSheet = project_StatusStatusSheet if project_StatusStatusSheet is not None else set()
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def project_StatusStatusSheet(self):
        return self.__project_StatusStatusSheet

    @project_StatusStatusSheet.setter
    def project_StatusStatusSheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_StatusStatusSheet__project_StatusStatusSheet", None)
        self.__project_StatusStatusSheet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_StatusStatusSheetAttribute"):
                    opp_val = getattr(item, "project_StatusStatusSheetAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_StatusStatusSheetAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_StatusStatusSheetAttribute"):
                    opp_val = getattr(item, "project_StatusStatusSheetAttribute", None)
                    
                    setattr(item, "project_StatusStatusSheetAttribute", self)
                    

class project_StatusTimesheetAttribute:

    pass
class project_StatusStatusSheetAttribute:

    pass
class project_Criterion:

    def __init__(self, columnId: str, direction: str, project_Criterion: "project_Sort" = None):
        self.columnId = columnId
        self.direction = direction
        self.project_Criterion = project_Criterion
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def columnId(self) -> str:
        return self.__columnId

    @columnId.setter
    def columnId(self, columnId: str):
        self.__columnId = columnId

    @property
    def project_Criterion(self):
        return self.__project_Criterion

    @project_Criterion.setter
    def project_Criterion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Criterion__project_Criterion", None)
        self.__project_Criterion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Sort"):
                opp_val = getattr(old_value, "project_Sort", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Sort"):
                opp_val = getattr(value, "project_Sort", None)
                if opp_val is None:
                    setattr(value, "project_Sort", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SortTasks:

    pass
class SortResources:

    pass
class SortJournalEntries:

    pass
class SortAccounts:

    pass
class project_Sort(SortTasks, SortAccounts, SortJournalEntries, SortResources):

    def __init__(self, tree: bool, project_Sort: set["project_Criterion"] = None):
        self.tree = tree
        self.project_Sort = project_Sort if project_Sort is not None else set()
        
    @property
    def tree(self) -> bool:
        return self.__tree

    @tree.setter
    def tree(self, tree: bool):
        self.__tree = tree

    @property
    def project_Sort(self):
        return self.__project_Sort

    @project_Sort.setter
    def project_Sort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Sort__project_Sort", None)
        self.__project_Sort = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_Criterion"):
                    opp_val = getattr(item, "project_Criterion", None)
                    
                    if opp_val == self:
                        setattr(item, "project_Criterion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_Criterion"):
                    opp_val = getattr(item, "project_Criterion", None)
                    
                    setattr(item, "project_Criterion", self)
                    

class project_ShiftsLimit:

    pass
class ShiftsTask:

    pass
class ShiftsResource:

    pass
class project_Shifts(ShiftsResource, ShiftsTask):

    pass
class project_LimitsAttribute:

    pass
class project_Interval3:

    def __init__(self, start: str, end: str, project_Interval3: "project_DurationQuantity" = None, project_Interval3148: "project_ShiftsAllocate" = None, project_Interval3217: "project_Vacation" = None):
        self.start = start
        self.end = end
        self.project_Interval3 = project_Interval3
        self.project_Interval3148 = project_Interval3148
        self.project_Interval3217 = project_Interval3217
        
    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

    @property
    def project_Interval3(self):
        return self.__project_Interval3

    @project_Interval3.setter
    def project_Interval3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Interval3__project_Interval3", None)
        self.__project_Interval3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_DurationQuantity87"):
                opp_val = getattr(old_value, "project_DurationQuantity87", None)
                if opp_val == self:
                    setattr(old_value, "project_DurationQuantity87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_DurationQuantity87"):
                opp_val = getattr(value, "project_DurationQuantity87", None)
                setattr(value, "project_DurationQuantity87", self)

    @property
    def project_Interval3148(self):
        return self.__project_Interval3148

    @project_Interval3148.setter
    def project_Interval3148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Interval3__project_Interval3148", None)
        self.__project_Interval3148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ShiftsAllocate147"):
                opp_val = getattr(old_value, "project_ShiftsAllocate147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ShiftsAllocate147"):
                opp_val = getattr(value, "project_ShiftsAllocate147", None)
                if opp_val is None:
                    setattr(value, "project_ShiftsAllocate147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def project_Interval3217(self):
        return self.__project_Interval3217

    @project_Interval3217.setter
    def project_Interval3217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Interval3__project_Interval3217", None)
        self.__project_Interval3217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Vacation216"):
                opp_val = getattr(old_value, "project_Vacation216", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Vacation216"):
                opp_val = getattr(value, "project_Vacation216", None)
                if opp_val is None:
                    setattr(value, "project_Vacation216", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class project_Interval1:

    def __init__(self, start: str, end: str, project_Interval1: "project_DurationQuantity" = None, project_Interval1235: "project_LimitAttribute" = None):
        self.start = start
        self.end = end
        self.project_Interval1 = project_Interval1
        self.project_Interval1235 = project_Interval1235
        
    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

    @property
    def project_Interval1235(self):
        return self.__project_Interval1235

    @project_Interval1235.setter
    def project_Interval1235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Interval1__project_Interval1235", None)
        self.__project_Interval1235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_LimitAttribute234"):
                opp_val = getattr(old_value, "project_LimitAttribute234", None)
                if opp_val == self:
                    setattr(old_value, "project_LimitAttribute234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_LimitAttribute234"):
                opp_val = getattr(value, "project_LimitAttribute234", None)
                setattr(value, "project_LimitAttribute234", self)

    @property
    def project_Interval1(self):
        return self.__project_Interval1

    @project_Interval1.setter
    def project_Interval1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Interval1__project_Interval1", None)
        self.__project_Interval1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_DurationQuantity82"):
                opp_val = getattr(old_value, "project_DurationQuantity82", None)
                if opp_val == self:
                    setattr(old_value, "project_DurationQuantity82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_DurationQuantity82"):
                opp_val = getattr(value, "project_DurationQuantity82", None)
                setattr(value, "project_DurationQuantity82", self)

class project_IncludePropertiesAttribute:

    pass
class NavigatorAttribute:

    pass
class project_HideReport(NavigatorAttribute):

    pass
class project_GapLength:

    pass
class project_GapDuration:

    pass
class project_Function:

    def __init__(self, level: int, date: str, parentId: str, distance: int, project_Function: "project_Scenario" = None, project_Function67: "project_Task" = None, project_Function70: "project_Resource" = None, project_Function253: "project_LogicalFunctionExpression" = None):
        self.level = level
        self.date = date
        self.parentId = parentId
        self.distance = distance
        self.project_Function = project_Function
        self.project_Function67 = project_Function67
        self.project_Function70 = project_Function70
        self.project_Function253 = project_Function253
        
    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

    @property
    def parentId(self) -> str:
        return self.__parentId

    @parentId.setter
    def parentId(self, parentId: str):
        self.__parentId = parentId

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def project_Function70(self):
        return self.__project_Function70

    @project_Function70.setter
    def project_Function70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Function__project_Function70", None)
        self.__project_Function70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Resource71"):
                opp_val = getattr(old_value, "project_Resource71", None)
                if opp_val == self:
                    setattr(old_value, "project_Resource71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Resource71"):
                opp_val = getattr(value, "project_Resource71", None)
                setattr(value, "project_Resource71", self)

    @property
    def project_Function253(self):
        return self.__project_Function253

    @project_Function253.setter
    def project_Function253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Function__project_Function253", None)
        self.__project_Function253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_LogicalFunctionExpression"):
                opp_val = getattr(old_value, "project_LogicalFunctionExpression", None)
                if opp_val == self:
                    setattr(old_value, "project_LogicalFunctionExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_LogicalFunctionExpression"):
                opp_val = getattr(value, "project_LogicalFunctionExpression", None)
                setattr(value, "project_LogicalFunctionExpression", self)

    @property
    def project_Function(self):
        return self.__project_Function

    @project_Function.setter
    def project_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Function__project_Function", None)
        self.__project_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Scenario"):
                opp_val = getattr(old_value, "project_Scenario", None)
                if opp_val == self:
                    setattr(old_value, "project_Scenario", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Scenario"):
                opp_val = getattr(value, "project_Scenario", None)
                setattr(value, "project_Scenario", self)

    @property
    def project_Function67(self):
        return self.__project_Function67

    @project_Function67.setter
    def project_Function67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Function__project_Function67", None)
        self.__project_Function67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Task68"):
                opp_val = getattr(old_value, "project_Task68", None)
                if opp_val == self:
                    setattr(old_value, "project_Task68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Task68"):
                opp_val = getattr(value, "project_Task68", None)
                setattr(value, "project_Task68", self)

class ExportAttribute:

    pass
class project_ResourceAttributes(ExportAttribute):

    def __init__(self, all: bool, none: bool, vacation: bool, booking: bool, workingHours: bool):
        self.all = all
        self.none = none
        self.vacation = vacation
        self.booking = booking
        self.workingHours = workingHours
        
    @property
    def booking(self) -> bool:
        return self.__booking

    @booking.setter
    def booking(self, booking: bool):
        self.__booking = booking

    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def vacation(self) -> bool:
        return self.__vacation

    @vacation.setter
    def vacation(self, vacation: bool):
        self.__vacation = vacation

    @property
    def none(self) -> bool:
        return self.__none

    @none.setter
    def none(self, none: bool):
        self.__none = none

    @property
    def workingHours(self) -> bool:
        return self.__workingHours

    @workingHours.setter
    def workingHours(self, workingHours: bool):
        self.__workingHours = workingHours

class project_TaskAttributes(ExportAttribute):

    def __init__(self, all: bool, none: bool, responsible: bool, flags: bool, maxstart: bool, maxend: bool, priority: bool, booking: bool, note: bool, minstart: bool, minend: bool, complete: bool, depends: bool):
        self.all = all
        self.none = none
        self.responsible = responsible
        self.flags = flags
        self.maxstart = maxstart
        self.maxend = maxend
        self.priority = priority
        self.booking = booking
        self.note = note
        self.minstart = minstart
        self.minend = minend
        self.complete = complete
        self.depends = depends
        
    @property
    def depends(self) -> bool:
        return self.__depends

    @depends.setter
    def depends(self, depends: bool):
        self.__depends = depends

    @property
    def priority(self) -> bool:
        return self.__priority

    @priority.setter
    def priority(self, priority: bool):
        self.__priority = priority

    @property
    def note(self) -> bool:
        return self.__note

    @note.setter
    def note(self, note: bool):
        self.__note = note

    @property
    def minend(self) -> bool:
        return self.__minend

    @minend.setter
    def minend(self, minend: bool):
        self.__minend = minend

    @property
    def complete(self) -> bool:
        return self.__complete

    @complete.setter
    def complete(self, complete: bool):
        self.__complete = complete

    @property
    def maxstart(self) -> bool:
        return self.__maxstart

    @maxstart.setter
    def maxstart(self, maxstart: bool):
        self.__maxstart = maxstart

    @property
    def none(self) -> bool:
        return self.__none

    @none.setter
    def none(self, none: bool):
        self.__none = none

    @property
    def booking(self) -> bool:
        return self.__booking

    @booking.setter
    def booking(self, booking: bool):
        self.__booking = booking

    @property
    def minstart(self) -> bool:
        return self.__minstart

    @minstart.setter
    def minstart(self, minstart: bool):
        self.__minstart = minstart

    @property
    def responsible(self) -> bool:
        return self.__responsible

    @responsible.setter
    def responsible(self, responsible: bool):
        self.__responsible = responsible

    @property
    def flags(self) -> bool:
        return self.__flags

    @flags.setter
    def flags(self, flags: bool):
        self.__flags = flags

    @property
    def maxend(self) -> bool:
        return self.__maxend

    @maxend.setter
    def maxend(self, maxend: bool):
        self.__maxend = maxend

    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

class project_Definitions(ExportAttribute):

    def __init__(self, all: bool, none: bool):
        self.all = all
        self.none = none
        
    @property
    def none(self) -> bool:
        return self.__none

    @none.setter
    def none(self, none: bool):
        self.__none = none

    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

class project_Extend:

    def __init__(self, id: str, name: str, inherit: bool, scenariospecific: bool, project_Extend: "project_ExtendResource" = None, project_Extend62: "project_ExtendedTaskAttribute" = None, project_Extend58: "project_ExtendedResourceAttribute" = None, project_Extend60: "project_ExtendTask" = None):
        self.id = id
        self.name = name
        self.inherit = inherit
        self.scenariospecific = scenariospecific
        self.project_Extend = project_Extend
        self.project_Extend62 = project_Extend62
        self.project_Extend58 = project_Extend58
        self.project_Extend60 = project_Extend60
        
    @property
    def inherit(self) -> bool:
        return self.__inherit

    @inherit.setter
    def inherit(self, inherit: bool):
        self.__inherit = inherit

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def scenariospecific(self) -> bool:
        return self.__scenariospecific

    @scenariospecific.setter
    def scenariospecific(self, scenariospecific: bool):
        self.__scenariospecific = scenariospecific

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def project_Extend58(self):
        return self.__project_Extend58

    @project_Extend58.setter
    def project_Extend58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Extend__project_Extend58", None)
        self.__project_Extend58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ExtendedResourceAttribute"):
                opp_val = getattr(old_value, "project_ExtendedResourceAttribute", None)
                if opp_val == self:
                    setattr(old_value, "project_ExtendedResourceAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ExtendedResourceAttribute"):
                opp_val = getattr(value, "project_ExtendedResourceAttribute", None)
                setattr(value, "project_ExtendedResourceAttribute", self)

    @property
    def project_Extend(self):
        return self.__project_Extend

    @project_Extend.setter
    def project_Extend(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Extend__project_Extend", None)
        self.__project_Extend = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ExtendResource"):
                opp_val = getattr(old_value, "project_ExtendResource", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ExtendResource"):
                opp_val = getattr(value, "project_ExtendResource", None)
                if opp_val is None:
                    setattr(value, "project_ExtendResource", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def project_Extend60(self):
        return self.__project_Extend60

    @project_Extend60.setter
    def project_Extend60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Extend__project_Extend60", None)
        self.__project_Extend60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ExtendTask"):
                opp_val = getattr(old_value, "project_ExtendTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ExtendTask"):
                opp_val = getattr(value, "project_ExtendTask", None)
                if opp_val is None:
                    setattr(value, "project_ExtendTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def project_Extend62(self):
        return self.__project_Extend62

    @project_Extend62.setter
    def project_Extend62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Extend__project_Extend62", None)
        self.__project_Extend62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ExtendedTaskAttribute"):
                opp_val = getattr(old_value, "project_ExtendedTaskAttribute", None)
                if opp_val == self:
                    setattr(old_value, "project_ExtendedTaskAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ExtendedTaskAttribute"):
                opp_val = getattr(value, "project_ExtendedTaskAttribute", None)
                setattr(value, "project_ExtendedTaskAttribute", self)

class TimesheetReportAttribute:

    pass
class TaskTimesheetAttribute:

    pass
class StatusSheetReportAttribute:

    pass
class NikuReportAttribute:

    pass
class project_Timeoff(NikuReportAttribute):

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NewTaskAttribute:

    pass
class project_Work(NewTaskAttribute, TaskTimesheetAttribute):

    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class project_Remaining(NewTaskAttribute, TaskTimesheetAttribute):

    pass
class IcalReportAttribute:

    pass
class project_ScenarioIcal(IcalReportAttribute):

    pass
class project_DurationQuantity(GapDuration, GapLength):

    def __init__(self, value: float, unit: str, project_DurationQuantity: "project_Duration" = None, project_DurationQuantity55: "project_Effort" = None, project_DurationQuantity82: "project_Interval1" = None, project_DurationQuantity85: "project_Interval2" = None, project_DurationQuantity90: "project_Interval4" = None, project_DurationQuantity87: "project_Interval3" = None, project_DurationQuantity100: "project_Length" = None, project_DurationQuantity107: "project_Remaining" = None, project_DurationQuantity230: "project_Limit" = None):
        self.value = value
        self.unit = unit
        self.project_DurationQuantity = project_DurationQuantity
        self.project_DurationQuantity55 = project_DurationQuantity55
        self.project_DurationQuantity82 = project_DurationQuantity82
        self.project_DurationQuantity85 = project_DurationQuantity85
        self.project_DurationQuantity90 = project_DurationQuantity90
        self.project_DurationQuantity87 = project_DurationQuantity87
        self.project_DurationQuantity100 = project_DurationQuantity100
        self.project_DurationQuantity107 = project_DurationQuantity107
        self.project_DurationQuantity230 = project_DurationQuantity230
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def project_DurationQuantity90(self):
        return self.__project_DurationQuantity90

    @project_DurationQuantity90.setter
    def project_DurationQuantity90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_DurationQuantity__project_DurationQuantity90", None)
        self.__project_DurationQuantity90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Interval489"):
                opp_val = getattr(old_value, "project_Interval489", None)
                if opp_val == self:
                    setattr(old_value, "project_Interval489", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Interval489"):
                opp_val = getattr(value, "project_Interval489", None)
                setattr(value, "project_Interval489", self)

    @property
    def project_DurationQuantity(self):
        return self.__project_DurationQuantity

    @project_DurationQuantity.setter
    def project_DurationQuantity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_DurationQuantity__project_DurationQuantity", None)
        self.__project_DurationQuantity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Duration"):
                opp_val = getattr(old_value, "project_Duration", None)
                if opp_val == self:
                    setattr(old_value, "project_Duration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Duration"):
                opp_val = getattr(value, "project_Duration", None)
                setattr(value, "project_Duration", self)

    @property
    def project_DurationQuantity87(self):
        return self.__project_DurationQuantity87

    @project_DurationQuantity87.setter
    def project_DurationQuantity87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_DurationQuantity__project_DurationQuantity87", None)
        self.__project_DurationQuantity87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Interval3"):
                opp_val = getattr(old_value, "project_Interval3", None)
                if opp_val == self:
                    setattr(old_value, "project_Interval3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Interval3"):
                opp_val = getattr(value, "project_Interval3", None)
                setattr(value, "project_Interval3", self)

    @property
    def project_DurationQuantity85(self):
        return self.__project_DurationQuantity85

    @project_DurationQuantity85.setter
    def project_DurationQuantity85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_DurationQuantity__project_DurationQuantity85", None)
        self.__project_DurationQuantity85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Interval284"):
                opp_val = getattr(old_value, "project_Interval284", None)
                if opp_val == self:
                    setattr(old_value, "project_Interval284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Interval284"):
                opp_val = getattr(value, "project_Interval284", None)
                setattr(value, "project_Interval284", self)

    @property
    def project_DurationQuantity82(self):
        return self.__project_DurationQuantity82

    @project_DurationQuantity82.setter
    def project_DurationQuantity82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_DurationQuantity__project_DurationQuantity82", None)
        self.__project_DurationQuantity82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Interval1"):
                opp_val = getattr(old_value, "project_Interval1", None)
                if opp_val == self:
                    setattr(old_value, "project_Interval1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Interval1"):
                opp_val = getattr(value, "project_Interval1", None)
                setattr(value, "project_Interval1", self)

    @property
    def project_DurationQuantity100(self):
        return self.__project_DurationQuantity100

    @project_DurationQuantity100.setter
    def project_DurationQuantity100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_DurationQuantity__project_DurationQuantity100", None)
        self.__project_DurationQuantity100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Length"):
                opp_val = getattr(old_value, "project_Length", None)
                if opp_val == self:
                    setattr(old_value, "project_Length", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Length"):
                opp_val = getattr(value, "project_Length", None)
                setattr(value, "project_Length", self)

    @property
    def project_DurationQuantity55(self):
        return self.__project_DurationQuantity55

    @project_DurationQuantity55.setter
    def project_DurationQuantity55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_DurationQuantity__project_DurationQuantity55", None)
        self.__project_DurationQuantity55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Effort"):
                opp_val = getattr(old_value, "project_Effort", None)
                if opp_val == self:
                    setattr(old_value, "project_Effort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Effort"):
                opp_val = getattr(value, "project_Effort", None)
                setattr(value, "project_Effort", self)

    @property
    def project_DurationQuantity107(self):
        return self.__project_DurationQuantity107

    @project_DurationQuantity107.setter
    def project_DurationQuantity107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_DurationQuantity__project_DurationQuantity107", None)
        self.__project_DurationQuantity107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Remaining"):
                opp_val = getattr(old_value, "project_Remaining", None)
                if opp_val == self:
                    setattr(old_value, "project_Remaining", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Remaining"):
                opp_val = getattr(value, "project_Remaining", None)
                setattr(value, "project_Remaining", self)

    @property
    def project_DurationQuantity230(self):
        return self.__project_DurationQuantity230

    @project_DurationQuantity230.setter
    def project_DurationQuantity230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_DurationQuantity__project_DurationQuantity230", None)
        self.__project_DurationQuantity230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Limit"):
                opp_val = getattr(old_value, "project_Limit", None)
                if opp_val == self:
                    setattr(old_value, "project_Limit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Limit"):
                opp_val = getattr(value, "project_Limit", None)
                setattr(value, "project_Limit", self)

class StatusTimesheetAttribute:

    pass
class project_RGB:

    def __init__(self, value: str, project_RGB: "project_CellColor" = None):
        self.value = value
        self.project_RGB = project_RGB
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def project_RGB(self):
        return self.__project_RGB

    @project_RGB.setter
    def project_RGB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_RGB__project_RGB", None)
        self.__project_RGB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_CellColor48"):
                opp_val = getattr(old_value, "project_CellColor48", None)
                if opp_val == self:
                    setattr(old_value, "project_CellColor48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_CellColor48"):
                opp_val = getattr(value, "project_CellColor48", None)
                setattr(value, "project_CellColor48", self)

class project_LogicalExpression:

    pass
class ColumnAttribute:

    pass
class project_FontColor(ColumnAttribute):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class project_Scale(ColumnAttribute):

    def __init__(self, scale: str):
        self.scale = scale
        
    @property
    def scale(self) -> str:
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale

class project_ListItem(ColumnAttribute):

    pass
class project_ToolTip(ColumnAttribute):

    def __init__(self, tip: str, project_ToolTip: "project_LogicalExpression" = None):
        self.tip = tip
        self.project_ToolTip = project_ToolTip
        
    @property
    def tip(self) -> str:
        return self.__tip

    @tip.setter
    def tip(self, tip: str):
        self.__tip = tip

    @property
    def project_ToolTip(self):
        return self.__project_ToolTip

    @project_ToolTip.setter
    def project_ToolTip(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_ToolTip__project_ToolTip", None)
        self.__project_ToolTip = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_LogicalExpression212"):
                opp_val = getattr(old_value, "project_LogicalExpression212", None)
                if opp_val == self:
                    setattr(old_value, "project_LogicalExpression212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_LogicalExpression212"):
                opp_val = getattr(value, "project_LogicalExpression212", None)
                setattr(value, "project_LogicalExpression212", self)

class project_HAlign(ColumnAttribute):

    def __init__(self, justification: str, project_HAlign: "project_LogicalExpression" = None):
        self.justification = justification
        self.project_HAlign = project_HAlign
        
    @property
    def justification(self) -> str:
        return self.__justification

    @justification.setter
    def justification(self, justification: str):
        self.__justification = justification

    @property
    def project_HAlign(self):
        return self.__project_HAlign

    @project_HAlign.setter
    def project_HAlign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_HAlign__project_HAlign", None)
        self.__project_HAlign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_LogicalExpression73"):
                opp_val = getattr(old_value, "project_LogicalExpression73", None)
                if opp_val == self:
                    setattr(old_value, "project_LogicalExpression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_LogicalExpression73"):
                opp_val = getattr(value, "project_LogicalExpression73", None)
                setattr(value, "project_LogicalExpression73", self)

class project_Width(ColumnAttribute):

    def __init__(self, width: float):
        self.width = width
        
    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

class project_ListType(ColumnAttribute):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class project_CellColor(ColumnAttribute):

    pass
class LimitsAttribute:

    pass
class project_Maximum(LimitsAttribute):

    pass
class project_MonthlyMax(LimitsAttribute):

    pass
class project_MonthlyMin(LimitsAttribute):

    pass
class project_DailyMin(LimitsAttribute):

    pass
class project_WeeklyMin(LimitsAttribute):

    pass
class project_Minimum(LimitsAttribute):

    pass
class project_WeeklyMax(LimitsAttribute):

    pass
class project_DailyMax(LimitsAttribute):

    pass
class ProjectAttribute:

    pass
class project_Include(ProjectAttribute):

    def __init__(self, importURI: str):
        self.importURI = importURI
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

class project_ShortTimeFormat(ProjectAttribute):

    def __init__(self, shortTimeFormat: str):
        self.shortTimeFormat = shortTimeFormat
        
    @property
    def shortTimeFormat(self) -> str:
        return self.__shortTimeFormat

    @shortTimeFormat.setter
    def shortTimeFormat(self, shortTimeFormat: str):
        self.__shortTimeFormat = shortTimeFormat

class project_Now(ProjectAttribute):

    def __init__(self, now: str):
        self.now = now
        
    @property
    def now(self) -> str:
        return self.__now

    @now.setter
    def now(self, now: str):
        self.__now = now

class project_ExtendResource(ProjectAttribute):

    pass
class project_YearlyWorkingDays(ProjectAttribute):

    def __init__(self, yearlyWorkingDays: int):
        self.yearlyWorkingDays = yearlyWorkingDays
        
    @property
    def yearlyWorkingDays(self) -> int:
        return self.__yearlyWorkingDays

    @yearlyWorkingDays.setter
    def yearlyWorkingDays(self, yearlyWorkingDays: int):
        self.__yearlyWorkingDays = yearlyWorkingDays

class project_TimingResolution(ProjectAttribute):

    def __init__(self, timingResolution: int):
        self.timingResolution = timingResolution
        
    @property
    def timingResolution(self) -> int:
        return self.__timingResolution

    @timingResolution.setter
    def timingResolution(self, timingResolution: int):
        self.__timingResolution = timingResolution

class project_ExtendTask(ProjectAttribute):

    pass
class project_WeekStarts(ProjectAttribute):

    def __init__(self, sunday: bool, monday: bool):
        self.sunday = sunday
        self.monday = monday
        
    @property
    def monday(self) -> bool:
        return self.__monday

    @monday.setter
    def monday(self, monday: bool):
        self.__monday = monday

    @property
    def sunday(self) -> bool:
        return self.__sunday

    @sunday.setter
    def sunday(self, sunday: bool):
        self.__sunday = sunday

class project_TrackingScenario(ProjectAttribute):

    pass
class project_DailyWorkingHours(ProjectAttribute):

    def __init__(self, dailyWorkingHours: float):
        self.dailyWorkingHours = dailyWorkingHours
        
    @property
    def dailyWorkingHours(self) -> float:
        return self.__dailyWorkingHours

    @dailyWorkingHours.setter
    def dailyWorkingHours(self, dailyWorkingHours: float):
        self.__dailyWorkingHours = dailyWorkingHours

class project_Scenario(ProjectAttribute):

    def __init__(self, id: str, name: str, active: str, project_Scenario: "project_Function" = None, project_Scenario124: "project_Scenario" = None, project_Scenario122: "project_Scenario" = None, project_Scenario126: "project_ScenarioIcal" = None, project_Scenario128: "project_Scenarios" = None, project_Scenario214: "project_TrackingScenario" = None):
        self.id = id
        self.name = name
        self.active = active
        self.project_Scenario = project_Scenario
        self.project_Scenario124 = project_Scenario124
        self.project_Scenario122 = project_Scenario122
        self.project_Scenario126 = project_Scenario126
        self.project_Scenario128 = project_Scenario128
        self.project_Scenario214 = project_Scenario214
        
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
    def active(self) -> str:
        return self.__active

    @active.setter
    def active(self, active: str):
        self.__active = active

    @property
    def project_Scenario126(self):
        return self.__project_Scenario126

    @project_Scenario126.setter
    def project_Scenario126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Scenario__project_Scenario126", None)
        self.__project_Scenario126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ScenarioIcal"):
                opp_val = getattr(old_value, "project_ScenarioIcal", None)
                if opp_val == self:
                    setattr(old_value, "project_ScenarioIcal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ScenarioIcal"):
                opp_val = getattr(value, "project_ScenarioIcal", None)
                setattr(value, "project_ScenarioIcal", self)

    @property
    def project_Scenario214(self):
        return self.__project_Scenario214

    @project_Scenario214.setter
    def project_Scenario214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Scenario__project_Scenario214", None)
        self.__project_Scenario214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_TrackingScenario"):
                opp_val = getattr(old_value, "project_TrackingScenario", None)
                if opp_val == self:
                    setattr(old_value, "project_TrackingScenario", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_TrackingScenario"):
                opp_val = getattr(value, "project_TrackingScenario", None)
                setattr(value, "project_TrackingScenario", self)

    @property
    def project_Scenario124(self):
        return self.__project_Scenario124

    @project_Scenario124.setter
    def project_Scenario124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Scenario__project_Scenario124", None)
        self.__project_Scenario124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Scenario122"):
                opp_val = getattr(old_value, "project_Scenario122", None)
                if opp_val == self:
                    setattr(old_value, "project_Scenario122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Scenario122"):
                opp_val = getattr(value, "project_Scenario122", None)
                setattr(value, "project_Scenario122", self)

    @property
    def project_Scenario(self):
        return self.__project_Scenario

    @project_Scenario.setter
    def project_Scenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Scenario__project_Scenario", None)
        self.__project_Scenario = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Function"):
                opp_val = getattr(old_value, "project_Function", None)
                if opp_val == self:
                    setattr(old_value, "project_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Function"):
                opp_val = getattr(value, "project_Function", None)
                setattr(value, "project_Function", self)

    @property
    def project_Scenario122(self):
        return self.__project_Scenario122

    @project_Scenario122.setter
    def project_Scenario122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Scenario__project_Scenario122", None)
        self.__project_Scenario122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Scenario124"):
                opp_val = getattr(old_value, "project_Scenario124", None)
                if opp_val == self:
                    setattr(old_value, "project_Scenario124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Scenario124"):
                opp_val = getattr(value, "project_Scenario124", None)
                setattr(value, "project_Scenario124", self)

    @property
    def project_Scenario128(self):
        return self.__project_Scenario128

    @project_Scenario128.setter
    def project_Scenario128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Scenario__project_Scenario128", None)
        self.__project_Scenario128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Scenarios"):
                opp_val = getattr(old_value, "project_Scenarios", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Scenarios"):
                opp_val = getattr(value, "project_Scenarios", None)
                if opp_val is None:
                    setattr(value, "project_Scenarios", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class project_Currency(ProjectAttribute):

    def __init__(self, currency: str):
        self.currency = currency
        
    @property
    def currency(self) -> str:
        return self.__currency

    @currency.setter
    def currency(self, currency: str):
        self.__currency = currency

class project_Column:

    def __init__(self, id: str, project_Column: "project_Columns" = None, project_Column228: "project_ColumnAttribute" = None):
        self.id = id
        self.project_Column = project_Column
        self.project_Column228 = project_Column228
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def project_Column228(self):
        return self.__project_Column228

    @project_Column228.setter
    def project_Column228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Column__project_Column228", None)
        self.__project_Column228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ColumnAttribute"):
                opp_val = getattr(old_value, "project_ColumnAttribute", None)
                if opp_val == self:
                    setattr(old_value, "project_ColumnAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ColumnAttribute"):
                opp_val = getattr(value, "project_ColumnAttribute", None)
                setattr(value, "project_ColumnAttribute", self)

    @property
    def project_Column(self):
        return self.__project_Column

    @project_Column.setter
    def project_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Column__project_Column", None)
        self.__project_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Columns"):
                opp_val = getattr(old_value, "project_Columns", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Columns"):
                opp_val = getattr(value, "project_Columns", None)
                if opp_val is None:
                    setattr(value, "project_Columns", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class project_AccountShare:

    def __init__(self, share: float, project_AccountShare: "project_ChargeSet" = None, project_AccountShare225: "project_Account" = None):
        self.share = share
        self.project_AccountShare = project_AccountShare
        self.project_AccountShare225 = project_AccountShare225
        
    @property
    def share(self) -> float:
        return self.__share

    @share.setter
    def share(self, share: float):
        self.__share = share

    @property
    def project_AccountShare(self):
        return self.__project_AccountShare

    @project_AccountShare.setter
    def project_AccountShare(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_AccountShare__project_AccountShare", None)
        self.__project_AccountShare = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ChargeSet"):
                opp_val = getattr(old_value, "project_ChargeSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ChargeSet"):
                opp_val = getattr(value, "project_ChargeSet", None)
                if opp_val is None:
                    setattr(value, "project_ChargeSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def project_AccountShare225(self):
        return self.__project_AccountShare225

    @project_AccountShare225.setter
    def project_AccountShare225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_AccountShare__project_AccountShare225", None)
        self.__project_AccountShare225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Account226"):
                opp_val = getattr(old_value, "project_Account226", None)
                if opp_val == self:
                    setattr(old_value, "project_Account226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Account226"):
                opp_val = getattr(value, "project_Account226", None)
                setattr(value, "project_Account226", self)

class project_CellText(ColumnAttribute):

    def __init__(self, text: str, project_CellText: "project_LogicalExpression" = None):
        self.text = text
        self.project_CellText = project_CellText
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def project_CellText(self):
        return self.__project_CellText

    @project_CellText.setter
    def project_CellText(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_CellText__project_CellText", None)
        self.__project_CellText = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_LogicalExpression50"):
                opp_val = getattr(old_value, "project_LogicalExpression50", None)
                if opp_val == self:
                    setattr(old_value, "project_LogicalExpression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_LogicalExpression50"):
                opp_val = getattr(value, "project_LogicalExpression50", None)
                setattr(value, "project_LogicalExpression50", self)

class project_Interval4:

    def __init__(self, start: str, end: str, project_Interval4: "project_Booking" = None, project_Interval489: "project_DurationQuantity" = None, project_Interval4156: "project_StatusSheet" = None, project_Interval4207: "project_Timesheet" = None):
        self.start = start
        self.end = end
        self.project_Interval4 = project_Interval4
        self.project_Interval489 = project_Interval489
        self.project_Interval4156 = project_Interval4156
        self.project_Interval4207 = project_Interval4207
        
    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def project_Interval4(self):
        return self.__project_Interval4

    @project_Interval4.setter
    def project_Interval4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Interval4__project_Interval4", None)
        self.__project_Interval4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Booking"):
                opp_val = getattr(old_value, "project_Booking", None)
                if opp_val == self:
                    setattr(old_value, "project_Booking", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Booking"):
                opp_val = getattr(value, "project_Booking", None)
                setattr(value, "project_Booking", self)

    @property
    def project_Interval4207(self):
        return self.__project_Interval4207

    @project_Interval4207.setter
    def project_Interval4207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Interval4__project_Interval4207", None)
        self.__project_Interval4207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Timesheet206"):
                opp_val = getattr(old_value, "project_Timesheet206", None)
                if opp_val == self:
                    setattr(old_value, "project_Timesheet206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Timesheet206"):
                opp_val = getattr(value, "project_Timesheet206", None)
                setattr(value, "project_Timesheet206", self)

    @property
    def project_Interval489(self):
        return self.__project_Interval489

    @project_Interval489.setter
    def project_Interval489(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Interval4__project_Interval489", None)
        self.__project_Interval489 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_DurationQuantity90"):
                opp_val = getattr(old_value, "project_DurationQuantity90", None)
                if opp_val == self:
                    setattr(old_value, "project_DurationQuantity90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_DurationQuantity90"):
                opp_val = getattr(value, "project_DurationQuantity90", None)
                setattr(value, "project_DurationQuantity90", self)

    @property
    def project_Interval4156(self):
        return self.__project_Interval4156

    @project_Interval4156.setter
    def project_Interval4156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Interval4__project_Interval4156", None)
        self.__project_Interval4156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_StatusSheet155"):
                opp_val = getattr(old_value, "project_StatusSheet155", None)
                if opp_val == self:
                    setattr(old_value, "project_StatusSheet155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_StatusSheet155"):
                opp_val = getattr(value, "project_StatusSheet155", None)
                setattr(value, "project_StatusSheet155", self)

class project_Booking:

    def __init__(self, overtime: int, sloppy: int, project_Booking: "project_Interval4" = None, project_Booking40: "project_BookingTask" = None, project_Booking45: "project_BookingResource" = None):
        self.overtime = overtime
        self.sloppy = sloppy
        self.project_Booking = project_Booking
        self.project_Booking40 = project_Booking40
        self.project_Booking45 = project_Booking45
        
    @property
    def overtime(self) -> int:
        return self.__overtime

    @overtime.setter
    def overtime(self, overtime: int):
        self.__overtime = overtime

    @property
    def sloppy(self) -> int:
        return self.__sloppy

    @sloppy.setter
    def sloppy(self, sloppy: int):
        self.__sloppy = sloppy

    @property
    def project_Booking45(self):
        return self.__project_Booking45

    @project_Booking45.setter
    def project_Booking45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Booking__project_Booking45", None)
        self.__project_Booking45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_BookingResource44"):
                opp_val = getattr(old_value, "project_BookingResource44", None)
                if opp_val == self:
                    setattr(old_value, "project_BookingResource44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_BookingResource44"):
                opp_val = getattr(value, "project_BookingResource44", None)
                setattr(value, "project_BookingResource44", self)

    @property
    def project_Booking(self):
        return self.__project_Booking

    @project_Booking.setter
    def project_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Booking__project_Booking", None)
        self.__project_Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Interval4"):
                opp_val = getattr(old_value, "project_Interval4", None)
                if opp_val == self:
                    setattr(old_value, "project_Interval4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Interval4"):
                opp_val = getattr(value, "project_Interval4", None)
                setattr(value, "project_Interval4", self)

    @property
    def project_Booking40(self):
        return self.__project_Booking40

    @project_Booking40.setter
    def project_Booking40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Booking__project_Booking40", None)
        self.__project_Booking40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_BookingTask39"):
                opp_val = getattr(old_value, "project_BookingTask39", None)
                if opp_val == self:
                    setattr(old_value, "project_BookingTask39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_BookingTask39"):
                opp_val = getattr(value, "project_BookingTask39", None)
                setattr(value, "project_BookingTask39", self)

class project_NewTaskAttribute:

    pass
class StatusStatusSheetAttribute:

    pass
class project_Details(StatusTimesheetAttribute, StatusStatusSheetAttribute):

    pass
class project_Summary(StatusTimesheetAttribute, StatusStatusSheetAttribute):

    pass
class project_Author(StatusStatusSheetAttribute):

    pass
class AllocateResourceAttribute:

    pass
class project_Persistent(AllocateResourceAttribute):

    def __init__(self, persistent: bool):
        self.persistent = persistent
        
    @property
    def persistent(self) -> bool:
        return self.__persistent

    @persistent.setter
    def persistent(self, persistent: bool):
        self.__persistent = persistent

class project_Select(AllocateResourceAttribute):

    def __init__(self, argument: str):
        self.argument = argument
        
    @property
    def argument(self) -> str:
        return self.__argument

    @argument.setter
    def argument(self, argument: str):
        self.__argument = argument

class project_Mandatory(AllocateResourceAttribute):

    def __init__(self, mandatory: bool):
        self.mandatory = mandatory
        
    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

class project_ShiftsAllocate(AllocateResourceAttribute):

    pass
class project_Alternative(AllocateResourceAttribute):

    pass
class project_Alert:

    def __init__(self, level: str, project_Alert: "project_JournalEntry" = None):
        self.level = level
        self.project_Alert = project_Alert
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def project_Alert(self):
        return self.__project_Alert

    @project_Alert.setter
    def project_Alert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Alert__project_Alert", None)
        self.__project_Alert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_JournalEntry"):
                opp_val = getattr(old_value, "project_JournalEntry", None)
                if opp_val == self:
                    setattr(old_value, "project_JournalEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_JournalEntry"):
                opp_val = getattr(value, "project_JournalEntry", None)
                setattr(value, "project_JournalEntry", self)

class project_NikuReportAttribute:

    pass
class project_ResourceAttribute:

    pass
class TimesheetAttribute:

    pass
class project_StatusTimesheet(TaskTimesheetAttribute, TimesheetAttribute):

    def __init__(self, level: str, text: str, project_StatusTimesheet: set["project_StatusTimesheetAttribute"] = None):
        self.level = level
        self.text = text
        self.project_StatusTimesheet = project_StatusTimesheet if project_StatusTimesheet is not None else set()
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def project_StatusTimesheet(self):
        return self.__project_StatusTimesheet

    @project_StatusTimesheet.setter
    def project_StatusTimesheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_StatusTimesheet__project_StatusTimesheet", None)
        self.__project_StatusTimesheet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_StatusTimesheetAttribute"):
                    opp_val = getattr(item, "project_StatusTimesheetAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_StatusTimesheetAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_StatusTimesheetAttribute"):
                    opp_val = getattr(item, "project_StatusTimesheetAttribute", None)
                    
                    setattr(item, "project_StatusTimesheetAttribute", self)
                    

class project_TaskTimesheet(TimesheetAttribute):

    pass
class project_ShiftTimesheet(TimesheetAttribute):

    pass
class project_NewTask(TimesheetAttribute):

    def __init__(self, id: str, text: str, project_NewTask: set["project_NewTaskAttribute"] = None):
        self.id = id
        self.text = text
        self.project_NewTask = project_NewTask if project_NewTask is not None else set()
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def project_NewTask(self):
        return self.__project_NewTask

    @project_NewTask.setter
    def project_NewTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_NewTask__project_NewTask", None)
        self.__project_NewTask = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_NewTaskAttribute"):
                    opp_val = getattr(item, "project_NewTaskAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_NewTaskAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_NewTaskAttribute"):
                    opp_val = getattr(item, "project_NewTaskAttribute", None)
                    
                    setattr(item, "project_NewTaskAttribute", self)
                    

class project_NavigatorAttribute:

    pass
class project_AllocateResourceAttribute:

    pass
class project_AllocateResource:

    pass
class TextReport:

    pass
class ResourceAttribute:

    pass
class project_Managers(ResourceAttribute):

    pass
class project_BookingResource(ResourceAttribute):

    pass
class project_Email(ResourceAttribute):

    def __init__(self, address: str):
        self.address = address
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

class project_Efficiency(ResourceAttribute):

    def __init__(self, efficiency: float):
        self.efficiency = efficiency
        
    @property
    def efficiency(self) -> float:
        return self.__efficiency

    @efficiency.setter
    def efficiency(self, efficiency: float):
        self.__efficiency = efficiency

class project_ExtendedResourceAttribute(ResourceAttribute):

    def __init__(self, value: str, project_ExtendedResourceAttribute: "project_Extend" = None):
        self.value = value
        self.project_ExtendedResourceAttribute = project_ExtendedResourceAttribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def project_ExtendedResourceAttribute(self):
        return self.__project_ExtendedResourceAttribute

    @project_ExtendedResourceAttribute.setter
    def project_ExtendedResourceAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_ExtendedResourceAttribute__project_ExtendedResourceAttribute", None)
        self.__project_ExtendedResourceAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Extend58"):
                opp_val = getattr(old_value, "project_Extend58", None)
                if opp_val == self:
                    setattr(old_value, "project_Extend58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Extend58"):
                opp_val = getattr(value, "project_Extend58", None)
                setattr(value, "project_Extend58", self)

class project_ShiftsResource(ResourceAttribute):

    pass
class project_WorkingHours(ProjectAttribute, ResourceAttribute):

    def __init__(self, off: bool, project_WorkingHours: "project_Shift" = None, project_WorkingHours221: set["project_Weekdays"] = None, project_WorkingHours223: set["project_WorkHours"] = None):
        self.off = off
        self.project_WorkingHours = project_WorkingHours
        self.project_WorkingHours221 = project_WorkingHours221 if project_WorkingHours221 is not None else set()
        self.project_WorkingHours223 = project_WorkingHours223 if project_WorkingHours223 is not None else set()
        
    @property
    def off(self) -> bool:
        return self.__off

    @off.setter
    def off(self, off: bool):
        self.__off = off

    @property
    def project_WorkingHours223(self):
        return self.__project_WorkingHours223

    @project_WorkingHours223.setter
    def project_WorkingHours223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_WorkingHours__project_WorkingHours223", None)
        self.__project_WorkingHours223 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_WorkHours"):
                    opp_val = getattr(item, "project_WorkHours", None)
                    
                    if opp_val == self:
                        setattr(item, "project_WorkHours", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_WorkHours"):
                    opp_val = getattr(item, "project_WorkHours", None)
                    
                    setattr(item, "project_WorkHours", self)
                    

    @property
    def project_WorkingHours(self):
        return self.__project_WorkingHours

    @project_WorkingHours.setter
    def project_WorkingHours(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_WorkingHours__project_WorkingHours", None)
        self.__project_WorkingHours = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Shift134"):
                opp_val = getattr(old_value, "project_Shift134", None)
                if opp_val == self:
                    setattr(old_value, "project_Shift134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Shift134"):
                opp_val = getattr(value, "project_Shift134", None)
                setattr(value, "project_Shift134", self)

    @property
    def project_WorkingHours221(self):
        return self.__project_WorkingHours221

    @project_WorkingHours221.setter
    def project_WorkingHours221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_WorkingHours__project_WorkingHours221", None)
        self.__project_WorkingHours221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_Weekdays"):
                    opp_val = getattr(item, "project_Weekdays", None)
                    
                    if opp_val == self:
                        setattr(item, "project_Weekdays", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_Weekdays"):
                    opp_val = getattr(item, "project_Weekdays", None)
                    
                    setattr(item, "project_Weekdays", self)
                    

class project_PurgeResource(ResourceAttribute):

    def __init__(self, listAttribute: str):
        self.listAttribute = listAttribute
        
    @property
    def listAttribute(self) -> str:
        return self.__listAttribute

    @listAttribute.setter
    def listAttribute(self, listAttribute: str):
        self.__listAttribute = listAttribute

class project_ExportAttribute:

    pass
class project_IcalReportAttribute:

    pass
class project_ReportAttribute:

    pass
class TaskReport:

    pass
class ResourceReport:

    pass
class AccountReport:

    pass
class project_Report(ResourceReport, AccountReport, TaskReport, TextReport):

    def __init__(self, id: str, name: str, project_Report: set["project_ReportAttribute"] = None, project_Report109: "project_ReportPrefix" = None, project_Report166: "project_SupplementReport" = None):
        self.id = id
        self.name = name
        self.project_Report = project_Report if project_Report is not None else set()
        self.project_Report109 = project_Report109
        self.project_Report166 = project_Report166
        
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
    def project_Report109(self):
        return self.__project_Report109

    @project_Report109.setter
    def project_Report109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Report__project_Report109", None)
        self.__project_Report109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ReportPrefix"):
                opp_val = getattr(old_value, "project_ReportPrefix", None)
                if opp_val == self:
                    setattr(old_value, "project_ReportPrefix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ReportPrefix"):
                opp_val = getattr(value, "project_ReportPrefix", None)
                setattr(value, "project_ReportPrefix", self)

    @property
    def project_Report(self):
        return self.__project_Report

    @project_Report.setter
    def project_Report(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Report__project_Report", None)
        self.__project_Report = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_ReportAttribute"):
                    opp_val = getattr(item, "project_ReportAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_ReportAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_ReportAttribute"):
                    opp_val = getattr(item, "project_ReportAttribute", None)
                    
                    setattr(item, "project_ReportAttribute", self)
                    

    @property
    def project_Report166(self):
        return self.__project_Report166

    @project_Report166.setter
    def project_Report166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Report__project_Report166", None)
        self.__project_Report166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_SupplementReport"):
                opp_val = getattr(old_value, "project_SupplementReport", None)
                if opp_val == self:
                    setattr(old_value, "project_SupplementReport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_SupplementReport"):
                opp_val = getattr(value, "project_SupplementReport", None)
                setattr(value, "project_SupplementReport", self)

class project_TaskAttribute:

    pass
class TaskAttribute:

    pass
class project_ChargeSet(TaskAttribute):

    pass
class project_Fail(TaskAttribute, ResourceAttribute):

    pass
class project_EndCredit(TaskAttribute):

    def __init__(self, credit: float):
        self.credit = credit
        
    @property
    def credit(self) -> float:
        return self.__credit

    @credit.setter
    def credit(self, credit: float):
        self.__credit = credit

class project_ExtendedTaskAttribute(TaskAttribute):

    def __init__(self, value: str, project_ExtendedTaskAttribute: "project_Extend" = None):
        self.value = value
        self.project_ExtendedTaskAttribute = project_ExtendedTaskAttribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def project_ExtendedTaskAttribute(self):
        return self.__project_ExtendedTaskAttribute

    @project_ExtendedTaskAttribute.setter
    def project_ExtendedTaskAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_ExtendedTaskAttribute__project_ExtendedTaskAttribute", None)
        self.__project_ExtendedTaskAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Extend62"):
                opp_val = getattr(old_value, "project_Extend62", None)
                if opp_val == self:
                    setattr(old_value, "project_Extend62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Extend62"):
                opp_val = getattr(value, "project_Extend62", None)
                setattr(value, "project_Extend62", self)

class project_Responsible(TaskAttribute):

    pass
class project_Charge(TaskAttribute):

    def __init__(self, amount: float, applies: str):
        self.amount = amount
        self.applies = applies
        
    @property
    def applies(self) -> str:
        return self.__applies

    @applies.setter
    def applies(self, applies: str):
        self.__applies = applies

    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

class project_MinStart(TaskAttribute):

    def __init__(self, minStart: str):
        self.minStart = minStart
        
    @property
    def minStart(self) -> str:
        return self.__minStart

    @minStart.setter
    def minStart(self, minStart: str):
        self.__minStart = minStart

class project_Note(TaskAttribute):

    def __init__(self, note: str):
        self.note = note
        
    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

class project_Warn(TaskAttribute, ResourceAttribute):

    pass
class project_Scheduled(TaskAttribute):

    def __init__(self, scheduled: bool):
        self.scheduled = scheduled
        
    @property
    def scheduled(self) -> bool:
        return self.__scheduled

    @scheduled.setter
    def scheduled(self, scheduled: bool):
        self.__scheduled = scheduled

class project_Depends(TaskAttribute):

    pass
class project_Scheduling(TaskAttribute):

    def __init__(self, scheduling: str):
        self.scheduling = scheduling
        
    @property
    def scheduling(self) -> str:
        return self.__scheduling

    @scheduling.setter
    def scheduling(self, scheduling: str):
        self.__scheduling = scheduling

class project_MaxStart(TaskAttribute):

    def __init__(self, maxStart: str):
        self.maxStart = maxStart
        
    @property
    def maxStart(self) -> str:
        return self.__maxStart

    @maxStart.setter
    def maxStart(self, maxStart: str):
        self.__maxStart = maxStart

class project_Milestone(TaskAttribute):

    def __init__(self, milestone: bool):
        self.milestone = milestone
        
    @property
    def milestone(self) -> bool:
        return self.__milestone

    @milestone.setter
    def milestone(self, milestone: bool):
        self.__milestone = milestone

class project_JournalEntry(TaskAttribute, ProjectAttribute, ResourceAttribute):

    def __init__(self, date: str, headline: str, project_JournalEntry98: "project_Summary" = None, project_JournalEntry: "project_Alert" = None, project_JournalEntry93: "project_Author" = None, project_JournalEntry96: "project_Details" = None):
        self.date = date
        self.headline = headline
        self.project_JournalEntry98 = project_JournalEntry98
        self.project_JournalEntry = project_JournalEntry
        self.project_JournalEntry93 = project_JournalEntry93
        self.project_JournalEntry96 = project_JournalEntry96
        
    @property
    def headline(self) -> str:
        return self.__headline

    @headline.setter
    def headline(self, headline: str):
        self.__headline = headline

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def project_JournalEntry96(self):
        return self.__project_JournalEntry96

    @project_JournalEntry96.setter
    def project_JournalEntry96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_JournalEntry__project_JournalEntry96", None)
        self.__project_JournalEntry96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Details"):
                opp_val = getattr(old_value, "project_Details", None)
                if opp_val == self:
                    setattr(old_value, "project_Details", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Details"):
                opp_val = getattr(value, "project_Details", None)
                setattr(value, "project_Details", self)

    @property
    def project_JournalEntry93(self):
        return self.__project_JournalEntry93

    @project_JournalEntry93.setter
    def project_JournalEntry93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_JournalEntry__project_JournalEntry93", None)
        self.__project_JournalEntry93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Author94"):
                opp_val = getattr(old_value, "project_Author94", None)
                if opp_val == self:
                    setattr(old_value, "project_Author94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Author94"):
                opp_val = getattr(value, "project_Author94", None)
                setattr(value, "project_Author94", self)

    @property
    def project_JournalEntry(self):
        return self.__project_JournalEntry

    @project_JournalEntry.setter
    def project_JournalEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_JournalEntry__project_JournalEntry", None)
        self.__project_JournalEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Alert"):
                opp_val = getattr(old_value, "project_Alert", None)
                if opp_val == self:
                    setattr(old_value, "project_Alert", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Alert"):
                opp_val = getattr(value, "project_Alert", None)
                setattr(value, "project_Alert", self)

    @property
    def project_JournalEntry98(self):
        return self.__project_JournalEntry98

    @project_JournalEntry98.setter
    def project_JournalEntry98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_JournalEntry__project_JournalEntry98", None)
        self.__project_JournalEntry98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Summary"):
                opp_val = getattr(old_value, "project_Summary", None)
                if opp_val == self:
                    setattr(old_value, "project_Summary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Summary"):
                opp_val = getattr(value, "project_Summary", None)
                setattr(value, "project_Summary", self)

class project_ProjectId(TaskAttribute):

    def __init__(self, projectId: str):
        self.projectId = projectId
        
    @property
    def projectId(self) -> str:
        return self.__projectId

    @projectId.setter
    def projectId(self, projectId: str):
        self.__projectId = projectId

class project_MaxEnd(TaskAttribute):

    def __init__(self, maxEnd: str):
        self.maxEnd = maxEnd
        
    @property
    def maxEnd(self) -> str:
        return self.__maxEnd

    @maxEnd.setter
    def maxEnd(self, maxEnd: str):
        self.__maxEnd = maxEnd

class project_ShiftsTask(TaskAttribute):

    pass
class project_Allocate(TaskAttribute):

    pass
class project_PurgeTask(TaskAttribute):

    def __init__(self, listAttribute: str):
        self.listAttribute = listAttribute
        
    @property
    def listAttribute(self) -> str:
        return self.__listAttribute

    @listAttribute.setter
    def listAttribute(self, listAttribute: str):
        self.__listAttribute = listAttribute

class project_Priority(TaskAttribute, NewTaskAttribute, TaskTimesheetAttribute):

    def __init__(self, priority: int):
        self.priority = priority
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

class project_BookingTask(TaskAttribute):

    pass
class project_Duration(TaskAttribute):

    pass
class project_Complete(TaskAttribute):

    def __init__(self, complete: float):
        self.complete = complete
        
    @property
    def complete(self) -> float:
        return self.__complete

    @complete.setter
    def complete(self, complete: float):
        self.__complete = complete

class project_MinEnd(TaskAttribute):

    def __init__(self, minEnd: str):
        self.minEnd = minEnd
        
    @property
    def minEnd(self) -> str:
        return self.__minEnd

    @minEnd.setter
    def minEnd(self, minEnd: str):
        self.__minEnd = minEnd

class project_Length(TaskAttribute):

    pass
class project_Precedes(TaskAttribute):

    pass
class project_Effort(TaskAttribute):

    pass
class project_ProjectAttribute:

    pass
class project_Interval2:

    def __init__(self, start: str, end: str, project_Interval2: "project_Project" = None, project_Interval284: "project_DurationQuantity" = None, project_Interval2105: "project_Period" = None, project_Interval2143: "project_ShiftsLimit" = None):
        self.start = start
        self.end = end
        self.project_Interval2 = project_Interval2
        self.project_Interval284 = project_Interval284
        self.project_Interval2105 = project_Interval2105
        self.project_Interval2143 = project_Interval2143
        
    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def project_Interval2143(self):
        return self.__project_Interval2143

    @project_Interval2143.setter
    def project_Interval2143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Interval2__project_Interval2143", None)
        self.__project_Interval2143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ShiftsLimit142"):
                opp_val = getattr(old_value, "project_ShiftsLimit142", None)
                if opp_val == self:
                    setattr(old_value, "project_ShiftsLimit142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ShiftsLimit142"):
                opp_val = getattr(value, "project_ShiftsLimit142", None)
                setattr(value, "project_ShiftsLimit142", self)

    @property
    def project_Interval284(self):
        return self.__project_Interval284

    @project_Interval284.setter
    def project_Interval284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Interval2__project_Interval284", None)
        self.__project_Interval284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_DurationQuantity85"):
                opp_val = getattr(old_value, "project_DurationQuantity85", None)
                if opp_val == self:
                    setattr(old_value, "project_DurationQuantity85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_DurationQuantity85"):
                opp_val = getattr(value, "project_DurationQuantity85", None)
                setattr(value, "project_DurationQuantity85", self)

    @property
    def project_Interval2(self):
        return self.__project_Interval2

    @project_Interval2.setter
    def project_Interval2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Interval2__project_Interval2", None)
        self.__project_Interval2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Project9"):
                opp_val = getattr(old_value, "project_Project9", None)
                if opp_val == self:
                    setattr(old_value, "project_Project9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Project9"):
                opp_val = getattr(value, "project_Project9", None)
                setattr(value, "project_Project9", self)

    @property
    def project_Interval2105(self):
        return self.__project_Interval2105

    @project_Interval2105.setter
    def project_Interval2105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Interval2__project_Interval2105", None)
        self.__project_Interval2105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Period"):
                opp_val = getattr(old_value, "project_Period", None)
                if opp_val == self:
                    setattr(old_value, "project_Period", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Period"):
                opp_val = getattr(value, "project_Period", None)
                setattr(value, "project_Period", self)

class project_Global:

    pass
class ReportAttribute:

    pass
class project_RollupTask(ReportAttribute, ExportAttribute, IcalReportAttribute):

    pass
class project_Footer(ReportAttribute):

    pass
class project_Timezone(ReportAttribute, ProjectAttribute, ExportAttribute):

    def __init__(self, timezone: str):
        self.timezone = timezone
        
    @property
    def timezone(self) -> str:
        return self.__timezone

    @timezone.setter
    def timezone(self, timezone: str):
        self.__timezone = timezone

class project_SortJournalEntries(ReportAttribute):

    pass
class project_Header(ReportAttribute):

    pass
class project_JournalMode(ReportAttribute):

    def __init__(self, mode: str):
        self.mode = mode
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

class project_End(ColumnAttribute, TimesheetReportAttribute, ReportAttribute, ExportAttribute, IcalReportAttribute, TaskAttribute, NewTaskAttribute, StatusSheetReportAttribute, TaskTimesheetAttribute, NikuReportAttribute):

    def __init__(self, end: str):
        self.end = end
        
    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

class project_TimeFormat(ReportAttribute, ProjectAttribute):

    def __init__(self, timeformat: str):
        self.timeformat = timeformat
        
    @property
    def timeformat(self) -> str:
        return self.__timeformat

    @timeformat.setter
    def timeformat(self, timeformat: str):
        self.__timeformat = timeformat

class project_AccountRoot(ReportAttribute):

    pass
class project_NumberFormat(ReportAttribute, ProjectAttribute, NikuReportAttribute):

    pass
class project_LoadUnit(ReportAttribute):

    def __init__(self, unit: str):
        self.unit = unit
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

class project_Scenarios(ReportAttribute, ExportAttribute):

    pass
class project_Right(ReportAttribute):

    pass
class project_SortTasks(ReportAttribute, StatusSheetReportAttribute):

    pass
class project_HideResource(TimesheetReportAttribute, ReportAttribute, ExportAttribute, IcalReportAttribute, StatusSheetReportAttribute, NikuReportAttribute):

    pass
class project_Formats(ReportAttribute, NikuReportAttribute):

    def __init__(self, formats: str):
        self.formats = formats
        
    @property
    def formats(self) -> str:
        return self.__formats

    @formats.setter
    def formats(self, formats: str):
        self.__formats = formats

class project_SortAccounts(ReportAttribute):

    pass
class project_Columns(ReportAttribute):

    pass
class project_Epilog(ReportAttribute):

    pass
class project_SortResources(ReportAttribute, StatusSheetReportAttribute):

    pass
class project_PurgeReport(ReportAttribute):

    def __init__(self, listAttribute: str):
        self.listAttribute = listAttribute
        
    @property
    def listAttribute(self) -> str:
        return self.__listAttribute

    @listAttribute.setter
    def listAttribute(self, listAttribute: str):
        self.__listAttribute = listAttribute

class project_ResourceRoot(ReportAttribute):

    pass
class project_HideAccount(ReportAttribute):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class project_Title(ReportAttribute, NikuReportAttribute, ColumnAttribute):

    def __init__(self, title: str):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class project_RollupResource(ReportAttribute, ExportAttribute, IcalReportAttribute):

    pass
class project_JournalAttributes(ReportAttribute):

    def __init__(self, property: bool, details: bool, author: bool, headline: bool, date: bool, timesheet: bool, propertyid: bool, summary: bool, all: bool, none: bool, flags: bool):
        self.property = property
        self.details = details
        self.author = author
        self.headline = headline
        self.date = date
        self.timesheet = timesheet
        self.propertyid = propertyid
        self.summary = summary
        self.all = all
        self.none = none
        self.flags = flags
        
    @property
    def property(self) -> bool:
        return self.__property

    @property.setter
    def property(self, property: bool):
        self.__property = property

    @property
    def flags(self) -> bool:
        return self.__flags

    @flags.setter
    def flags(self, flags: bool):
        self.__flags = flags

    @property
    def author(self) -> bool:
        return self.__author

    @author.setter
    def author(self, author: bool):
        self.__author = author

    @property
    def date(self) -> bool:
        return self.__date

    @date.setter
    def date(self, date: bool):
        self.__date = date

    @property
    def propertyid(self) -> bool:
        return self.__propertyid

    @propertyid.setter
    def propertyid(self, propertyid: bool):
        self.__propertyid = propertyid

    @property
    def details(self) -> bool:
        return self.__details

    @details.setter
    def details(self, details: bool):
        self.__details = details

    @property
    def none(self) -> bool:
        return self.__none

    @none.setter
    def none(self, none: bool):
        self.__none = none

    @property
    def timesheet(self) -> bool:
        return self.__timesheet

    @timesheet.setter
    def timesheet(self, timesheet: bool):
        self.__timesheet = timesheet

    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def headline(self) -> bool:
        return self.__headline

    @headline.setter
    def headline(self, headline: bool):
        self.__headline = headline

    @property
    def summary(self) -> bool:
        return self.__summary

    @summary.setter
    def summary(self, summary: bool):
        self.__summary = summary

class project_Prolog(ReportAttribute):

    pass
class project_Headline(ReportAttribute, NikuReportAttribute):

    pass
class project_Center(ReportAttribute):

    pass
class project_TaskRoot(ReportAttribute):

    pass
class project_HideJournalEntry(ReportAttribute, IcalReportAttribute):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class project_CurrencyFormat(ReportAttribute, ProjectAttribute):

    pass
class project_SelfContained(ReportAttribute):

    def __init__(self, selfcontained: str):
        self.selfcontained = selfcontained
        
    @property
    def selfcontained(self) -> str:
        return self.__selfcontained

    @selfcontained.setter
    def selfcontained(self, selfcontained: str):
        self.__selfcontained = selfcontained

class project_Period(ColumnAttribute, TimesheetReportAttribute, ReportAttribute, ExportAttribute, IcalReportAttribute, TaskAttribute, StatusSheetReportAttribute, NikuReportAttribute):

    pass
class project_HideTask(ReportAttribute, ExportAttribute, IcalReportAttribute, StatusSheetReportAttribute, NikuReportAttribute):

    pass
class project_Start(ColumnAttribute, TimesheetReportAttribute, ReportAttribute, ExportAttribute, IcalReportAttribute, TaskAttribute, StatusSheetReportAttribute, NikuReportAttribute):

    def __init__(self, start: str):
        self.start = start
        
    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

class project_Caption(ReportAttribute):

    pass
class project_RollupAccount(ReportAttribute):

    pass
class project_Left(ReportAttribute):

    pass
class IncludePropertiesAttribute:

    pass
class project_ReportPrefix(IncludePropertiesAttribute):

    pass
class project_ResourcePrefix(IncludePropertiesAttribute):

    pass
class project_TaskPrefix(IncludePropertiesAttribute):

    pass
class project_AccountPrefix(IncludePropertiesAttribute):

    pass
class project_AccountAttribute:

    pass
class AccountAttribute:

    pass
class project_Credit(AccountAttribute):

    def __init__(self, date: str, description: str, amount: float):
        self.date = date
        self.description = description
        self.amount = amount
        
    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class Property:

    pass
class project_Task(TaskAttribute, Property):

    def __init__(self, id: str, name: str, project_Task: set["project_TaskAttribute"] = None, project_Task42: "project_BookingResource" = None, project_Task68: "project_Function" = None, project_Task176: "project_SupplementTask" = None, project_Task192: "project_TaskStatusSheet" = None, project_Task200: "project_TaskPrefix" = None, project_Task196: "project_TaskTimesheet" = None, project_Task202: "project_TaskRoot" = None, project_Task240: "project_TaskDependency" = None):
        self.id = id
        self.name = name
        self.project_Task = project_Task if project_Task is not None else set()
        self.project_Task42 = project_Task42
        self.project_Task68 = project_Task68
        self.project_Task176 = project_Task176
        self.project_Task192 = project_Task192
        self.project_Task200 = project_Task200
        self.project_Task196 = project_Task196
        self.project_Task202 = project_Task202
        self.project_Task240 = project_Task240
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def project_Task192(self):
        return self.__project_Task192

    @project_Task192.setter
    def project_Task192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Task__project_Task192", None)
        self.__project_Task192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_TaskStatusSheet"):
                opp_val = getattr(old_value, "project_TaskStatusSheet", None)
                if opp_val == self:
                    setattr(old_value, "project_TaskStatusSheet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_TaskStatusSheet"):
                opp_val = getattr(value, "project_TaskStatusSheet", None)
                setattr(value, "project_TaskStatusSheet", self)

    @property
    def project_Task176(self):
        return self.__project_Task176

    @project_Task176.setter
    def project_Task176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Task__project_Task176", None)
        self.__project_Task176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_SupplementTask"):
                opp_val = getattr(old_value, "project_SupplementTask", None)
                if opp_val == self:
                    setattr(old_value, "project_SupplementTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_SupplementTask"):
                opp_val = getattr(value, "project_SupplementTask", None)
                setattr(value, "project_SupplementTask", self)

    @property
    def project_Task240(self):
        return self.__project_Task240

    @project_Task240.setter
    def project_Task240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Task__project_Task240", None)
        self.__project_Task240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_TaskDependency"):
                opp_val = getattr(old_value, "project_TaskDependency", None)
                if opp_val == self:
                    setattr(old_value, "project_TaskDependency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_TaskDependency"):
                opp_val = getattr(value, "project_TaskDependency", None)
                setattr(value, "project_TaskDependency", self)

    @property
    def project_Task(self):
        return self.__project_Task

    @project_Task.setter
    def project_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Task__project_Task", None)
        self.__project_Task = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_TaskAttribute"):
                    opp_val = getattr(item, "project_TaskAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_TaskAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_TaskAttribute"):
                    opp_val = getattr(item, "project_TaskAttribute", None)
                    
                    setattr(item, "project_TaskAttribute", self)
                    

    @property
    def project_Task196(self):
        return self.__project_Task196

    @project_Task196.setter
    def project_Task196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Task__project_Task196", None)
        self.__project_Task196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_TaskTimesheet"):
                opp_val = getattr(old_value, "project_TaskTimesheet", None)
                if opp_val == self:
                    setattr(old_value, "project_TaskTimesheet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_TaskTimesheet"):
                opp_val = getattr(value, "project_TaskTimesheet", None)
                setattr(value, "project_TaskTimesheet", self)

    @property
    def project_Task42(self):
        return self.__project_Task42

    @project_Task42.setter
    def project_Task42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Task__project_Task42", None)
        self.__project_Task42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_BookingResource"):
                opp_val = getattr(old_value, "project_BookingResource", None)
                if opp_val == self:
                    setattr(old_value, "project_BookingResource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_BookingResource"):
                opp_val = getattr(value, "project_BookingResource", None)
                setattr(value, "project_BookingResource", self)

    @property
    def project_Task68(self):
        return self.__project_Task68

    @project_Task68.setter
    def project_Task68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Task__project_Task68", None)
        self.__project_Task68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Function67"):
                opp_val = getattr(old_value, "project_Function67", None)
                if opp_val == self:
                    setattr(old_value, "project_Function67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Function67"):
                opp_val = getattr(value, "project_Function67", None)
                setattr(value, "project_Function67", self)

    @property
    def project_Task202(self):
        return self.__project_Task202

    @project_Task202.setter
    def project_Task202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Task__project_Task202", None)
        self.__project_Task202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_TaskRoot"):
                opp_val = getattr(old_value, "project_TaskRoot", None)
                if opp_val == self:
                    setattr(old_value, "project_TaskRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_TaskRoot"):
                opp_val = getattr(value, "project_TaskRoot", None)
                setattr(value, "project_TaskRoot", self)

    @property
    def project_Task200(self):
        return self.__project_Task200

    @project_Task200.setter
    def project_Task200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Task__project_Task200", None)
        self.__project_Task200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_TaskPrefix"):
                opp_val = getattr(old_value, "project_TaskPrefix", None)
                if opp_val == self:
                    setattr(old_value, "project_TaskPrefix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_TaskPrefix"):
                opp_val = getattr(value, "project_TaskPrefix", None)
                setattr(value, "project_TaskPrefix", self)

class project_AccountReport(ReportAttribute, Property):

    pass
class project_TimesheetReport(Property):

    def __init__(self, filename: str, project_TimesheetReport: set["project_TimesheetReportAttribute"] = None):
        self.filename = filename
        self.project_TimesheetReport = project_TimesheetReport if project_TimesheetReport is not None else set()
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def project_TimesheetReport(self):
        return self.__project_TimesheetReport

    @project_TimesheetReport.setter
    def project_TimesheetReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_TimesheetReport__project_TimesheetReport", None)
        self.__project_TimesheetReport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_TimesheetReportAttribute"):
                    opp_val = getattr(item, "project_TimesheetReportAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_TimesheetReportAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_TimesheetReportAttribute"):
                    opp_val = getattr(item, "project_TimesheetReportAttribute", None)
                    
                    setattr(item, "project_TimesheetReportAttribute", self)
                    

class project_SupplementTask(TaskAttribute, Property):

    pass
class project_SupplementReport(Property):

    pass
class project_IcalReport(Property):

    def __init__(self, filename: str, project_IcalReport: set["project_IcalReportAttribute"] = None):
        self.filename = filename
        self.project_IcalReport = project_IcalReport if project_IcalReport is not None else set()
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def project_IcalReport(self):
        return self.__project_IcalReport

    @project_IcalReport.setter
    def project_IcalReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_IcalReport__project_IcalReport", None)
        self.__project_IcalReport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_IcalReportAttribute"):
                    opp_val = getattr(item, "project_IcalReportAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_IcalReportAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_IcalReportAttribute"):
                    opp_val = getattr(item, "project_IcalReportAttribute", None)
                    
                    setattr(item, "project_IcalReportAttribute", self)
                    

class project_Resource(Property, ResourceAttribute):

    def __init__(self, id: str, name: str, project_Resource20: "project_AllocateResource" = None, project_Resource: set["project_ResourceAttribute"] = None, project_Resource27: "project_Alternative" = None, project_Resource29: "project_Author" = None, project_Resource37: "project_BookingTask" = None, project_Resource71: "project_Function" = None, project_Resource103: "project_Managers" = None, project_Resource111: "project_ResourcePrefix" = None, project_Resource115: "project_Responsible" = None, project_Resource113: "project_ResourceRoot" = None, project_Resource153: "project_StatusSheet" = None, project_Resource171: "project_SupplementResource" = None, project_Resource204: "project_Timesheet" = None, project_Resource238: "project_LimitAttribute" = None):
        self.id = id
        self.name = name
        self.project_Resource20 = project_Resource20
        self.project_Resource = project_Resource if project_Resource is not None else set()
        self.project_Resource27 = project_Resource27
        self.project_Resource29 = project_Resource29
        self.project_Resource37 = project_Resource37
        self.project_Resource71 = project_Resource71
        self.project_Resource103 = project_Resource103
        self.project_Resource111 = project_Resource111
        self.project_Resource115 = project_Resource115
        self.project_Resource113 = project_Resource113
        self.project_Resource153 = project_Resource153
        self.project_Resource171 = project_Resource171
        self.project_Resource204 = project_Resource204
        self.project_Resource238 = project_Resource238
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def project_Resource27(self):
        return self.__project_Resource27

    @project_Resource27.setter
    def project_Resource27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Resource__project_Resource27", None)
        self.__project_Resource27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Alternative"):
                opp_val = getattr(old_value, "project_Alternative", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Alternative"):
                opp_val = getattr(value, "project_Alternative", None)
                if opp_val is None:
                    setattr(value, "project_Alternative", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def project_Resource103(self):
        return self.__project_Resource103

    @project_Resource103.setter
    def project_Resource103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Resource__project_Resource103", None)
        self.__project_Resource103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Managers"):
                opp_val = getattr(old_value, "project_Managers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Managers"):
                opp_val = getattr(value, "project_Managers", None)
                if opp_val is None:
                    setattr(value, "project_Managers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def project_Resource153(self):
        return self.__project_Resource153

    @project_Resource153.setter
    def project_Resource153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Resource__project_Resource153", None)
        self.__project_Resource153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_StatusSheet"):
                opp_val = getattr(old_value, "project_StatusSheet", None)
                if opp_val == self:
                    setattr(old_value, "project_StatusSheet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_StatusSheet"):
                opp_val = getattr(value, "project_StatusSheet", None)
                setattr(value, "project_StatusSheet", self)

    @property
    def project_Resource(self):
        return self.__project_Resource

    @project_Resource.setter
    def project_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Resource__project_Resource", None)
        self.__project_Resource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_ResourceAttribute"):
                    opp_val = getattr(item, "project_ResourceAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_ResourceAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_ResourceAttribute"):
                    opp_val = getattr(item, "project_ResourceAttribute", None)
                    
                    setattr(item, "project_ResourceAttribute", self)
                    

    @property
    def project_Resource37(self):
        return self.__project_Resource37

    @project_Resource37.setter
    def project_Resource37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Resource__project_Resource37", None)
        self.__project_Resource37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_BookingTask"):
                opp_val = getattr(old_value, "project_BookingTask", None)
                if opp_val == self:
                    setattr(old_value, "project_BookingTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_BookingTask"):
                opp_val = getattr(value, "project_BookingTask", None)
                setattr(value, "project_BookingTask", self)

    @property
    def project_Resource115(self):
        return self.__project_Resource115

    @project_Resource115.setter
    def project_Resource115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Resource__project_Resource115", None)
        self.__project_Resource115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Responsible"):
                opp_val = getattr(old_value, "project_Responsible", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Responsible"):
                opp_val = getattr(value, "project_Responsible", None)
                if opp_val is None:
                    setattr(value, "project_Responsible", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def project_Resource171(self):
        return self.__project_Resource171

    @project_Resource171.setter
    def project_Resource171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Resource__project_Resource171", None)
        self.__project_Resource171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_SupplementResource"):
                opp_val = getattr(old_value, "project_SupplementResource", None)
                if opp_val == self:
                    setattr(old_value, "project_SupplementResource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_SupplementResource"):
                opp_val = getattr(value, "project_SupplementResource", None)
                setattr(value, "project_SupplementResource", self)

    @property
    def project_Resource111(self):
        return self.__project_Resource111

    @project_Resource111.setter
    def project_Resource111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Resource__project_Resource111", None)
        self.__project_Resource111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ResourcePrefix"):
                opp_val = getattr(old_value, "project_ResourcePrefix", None)
                if opp_val == self:
                    setattr(old_value, "project_ResourcePrefix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ResourcePrefix"):
                opp_val = getattr(value, "project_ResourcePrefix", None)
                setattr(value, "project_ResourcePrefix", self)

    @property
    def project_Resource71(self):
        return self.__project_Resource71

    @project_Resource71.setter
    def project_Resource71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Resource__project_Resource71", None)
        self.__project_Resource71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Function70"):
                opp_val = getattr(old_value, "project_Function70", None)
                if opp_val == self:
                    setattr(old_value, "project_Function70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Function70"):
                opp_val = getattr(value, "project_Function70", None)
                setattr(value, "project_Function70", self)

    @property
    def project_Resource113(self):
        return self.__project_Resource113

    @project_Resource113.setter
    def project_Resource113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Resource__project_Resource113", None)
        self.__project_Resource113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ResourceRoot"):
                opp_val = getattr(old_value, "project_ResourceRoot", None)
                if opp_val == self:
                    setattr(old_value, "project_ResourceRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ResourceRoot"):
                opp_val = getattr(value, "project_ResourceRoot", None)
                setattr(value, "project_ResourceRoot", self)

    @property
    def project_Resource20(self):
        return self.__project_Resource20

    @project_Resource20.setter
    def project_Resource20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Resource__project_Resource20", None)
        self.__project_Resource20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_AllocateResource19"):
                opp_val = getattr(old_value, "project_AllocateResource19", None)
                if opp_val == self:
                    setattr(old_value, "project_AllocateResource19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_AllocateResource19"):
                opp_val = getattr(value, "project_AllocateResource19", None)
                setattr(value, "project_AllocateResource19", self)

    @property
    def project_Resource29(self):
        return self.__project_Resource29

    @project_Resource29.setter
    def project_Resource29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Resource__project_Resource29", None)
        self.__project_Resource29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Author"):
                opp_val = getattr(old_value, "project_Author", None)
                if opp_val == self:
                    setattr(old_value, "project_Author", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Author"):
                opp_val = getattr(value, "project_Author", None)
                setattr(value, "project_Author", self)

    @property
    def project_Resource238(self):
        return self.__project_Resource238

    @project_Resource238.setter
    def project_Resource238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Resource__project_Resource238", None)
        self.__project_Resource238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_LimitAttribute237"):
                opp_val = getattr(old_value, "project_LimitAttribute237", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_LimitAttribute237"):
                opp_val = getattr(value, "project_LimitAttribute237", None)
                if opp_val is None:
                    setattr(value, "project_LimitAttribute237", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def project_Resource204(self):
        return self.__project_Resource204

    @project_Resource204.setter
    def project_Resource204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Resource__project_Resource204", None)
        self.__project_Resource204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Timesheet"):
                opp_val = getattr(old_value, "project_Timesheet", None)
                if opp_val == self:
                    setattr(old_value, "project_Timesheet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Timesheet"):
                opp_val = getattr(value, "project_Timesheet", None)
                setattr(value, "project_Timesheet", self)

class project_TaskReport(ReportAttribute, Property):

    pass
class project_Limits(TaskAttribute, Property, ResourceAttribute):

    pass
class project_TextReport(ReportAttribute, Property):

    pass
class project_StatusSheet(Property):

    pass
class project_Export(Property):

    def __init__(self, id: str, filename: str, project_Export: set["project_ExportAttribute"] = None):
        self.id = id
        self.filename = filename
        self.project_Export = project_Export if project_Export is not None else set()
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def project_Export(self):
        return self.__project_Export

    @project_Export.setter
    def project_Export(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Export__project_Export", None)
        self.__project_Export = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_ExportAttribute"):
                    opp_val = getattr(item, "project_ExportAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_ExportAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_ExportAttribute"):
                    opp_val = getattr(item, "project_ExportAttribute", None)
                    
                    setattr(item, "project_ExportAttribute", self)
                    

class project_Timesheet(Property):

    pass
class project_Vacation(Property, ResourceAttribute):

    def __init__(self, name: str, project_Vacation: "project_Shift" = None, project_Vacation216: set["project_Interval3"] = None):
        self.name = name
        self.project_Vacation = project_Vacation
        self.project_Vacation216 = project_Vacation216 if project_Vacation216 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def project_Vacation216(self):
        return self.__project_Vacation216

    @project_Vacation216.setter
    def project_Vacation216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Vacation__project_Vacation216", None)
        self.__project_Vacation216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_Interval3217"):
                    opp_val = getattr(item, "project_Interval3217", None)
                    
                    if opp_val == self:
                        setattr(item, "project_Interval3217", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_Interval3217"):
                    opp_val = getattr(item, "project_Interval3217", None)
                    
                    setattr(item, "project_Interval3217", self)
                    

    @property
    def project_Vacation(self):
        return self.__project_Vacation

    @project_Vacation.setter
    def project_Vacation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Vacation__project_Vacation", None)
        self.__project_Vacation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Shift"):
                opp_val = getattr(old_value, "project_Shift", None)
                if opp_val == self:
                    setattr(old_value, "project_Shift", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Shift"):
                opp_val = getattr(value, "project_Shift", None)
                setattr(value, "project_Shift", self)

class project_Navigator(Property):

    def __init__(self, id: str, project_Navigator: set["project_NavigatorAttribute"] = None):
        self.id = id
        self.project_Navigator = project_Navigator if project_Navigator is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def project_Navigator(self):
        return self.__project_Navigator

    @project_Navigator.setter
    def project_Navigator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Navigator__project_Navigator", None)
        self.__project_Navigator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_NavigatorAttribute"):
                    opp_val = getattr(item, "project_NavigatorAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_NavigatorAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_NavigatorAttribute"):
                    opp_val = getattr(item, "project_NavigatorAttribute", None)
                    
                    setattr(item, "project_NavigatorAttribute", self)
                    

class project_TagFile(Property):

    def __init__(self, id: str, filename: str, project_TagFile: "project_HideResource" = None, project_TagFile186: "project_RollupResource" = None, project_TagFile189: "project_RollupTask" = None, project_TagFile183: "project_HideTask" = None):
        self.id = id
        self.filename = filename
        self.project_TagFile = project_TagFile
        self.project_TagFile186 = project_TagFile186
        self.project_TagFile189 = project_TagFile189
        self.project_TagFile183 = project_TagFile183
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def project_TagFile183(self):
        return self.__project_TagFile183

    @project_TagFile183.setter
    def project_TagFile183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_TagFile__project_TagFile183", None)
        self.__project_TagFile183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_HideTask184"):
                opp_val = getattr(old_value, "project_HideTask184", None)
                if opp_val == self:
                    setattr(old_value, "project_HideTask184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_HideTask184"):
                opp_val = getattr(value, "project_HideTask184", None)
                setattr(value, "project_HideTask184", self)

    @property
    def project_TagFile189(self):
        return self.__project_TagFile189

    @project_TagFile189.setter
    def project_TagFile189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_TagFile__project_TagFile189", None)
        self.__project_TagFile189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_RollupTask190"):
                opp_val = getattr(old_value, "project_RollupTask190", None)
                if opp_val == self:
                    setattr(old_value, "project_RollupTask190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_RollupTask190"):
                opp_val = getattr(value, "project_RollupTask190", None)
                setattr(value, "project_RollupTask190", self)

    @property
    def project_TagFile186(self):
        return self.__project_TagFile186

    @project_TagFile186.setter
    def project_TagFile186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_TagFile__project_TagFile186", None)
        self.__project_TagFile186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_RollupResource187"):
                opp_val = getattr(old_value, "project_RollupResource187", None)
                if opp_val == self:
                    setattr(old_value, "project_RollupResource187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_RollupResource187"):
                opp_val = getattr(value, "project_RollupResource187", None)
                setattr(value, "project_RollupResource187", self)

    @property
    def project_TagFile(self):
        return self.__project_TagFile

    @project_TagFile.setter
    def project_TagFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_TagFile__project_TagFile", None)
        self.__project_TagFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_HideResource181"):
                opp_val = getattr(old_value, "project_HideResource181", None)
                if opp_val == self:
                    setattr(old_value, "project_HideResource181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_HideResource181"):
                opp_val = getattr(value, "project_HideResource181", None)
                setattr(value, "project_HideResource181", self)

class project_SupplementResource(Property, ResourceAttribute):

    pass
class project_Shift(Property):

    def __init__(self, id: str, name: str, replace: str, timezone: str, project_Shift: "project_Vacation" = None, project_Shift136: "project_ShiftTimesheet" = None, project_Shift140: "project_ShiftsLimit" = None, project_Shift145: "project_ShiftsAllocate" = None, project_Shift132: "project_Shift" = None, project_Shift130: "project_Shift" = None, project_Shift134: "project_WorkingHours" = None):
        self.id = id
        self.name = name
        self.replace = replace
        self.timezone = timezone
        self.project_Shift = project_Shift
        self.project_Shift136 = project_Shift136
        self.project_Shift140 = project_Shift140
        self.project_Shift145 = project_Shift145
        self.project_Shift132 = project_Shift132
        self.project_Shift130 = project_Shift130
        self.project_Shift134 = project_Shift134
        
    @property
    def replace(self) -> str:
        return self.__replace

    @replace.setter
    def replace(self, replace: str):
        self.__replace = replace

    @property
    def timezone(self) -> str:
        return self.__timezone

    @timezone.setter
    def timezone(self, timezone: str):
        self.__timezone = timezone

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def project_Shift132(self):
        return self.__project_Shift132

    @project_Shift132.setter
    def project_Shift132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Shift__project_Shift132", None)
        self.__project_Shift132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Shift130"):
                opp_val = getattr(old_value, "project_Shift130", None)
                if opp_val == self:
                    setattr(old_value, "project_Shift130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Shift130"):
                opp_val = getattr(value, "project_Shift130", None)
                setattr(value, "project_Shift130", self)

    @property
    def project_Shift130(self):
        return self.__project_Shift130

    @project_Shift130.setter
    def project_Shift130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Shift__project_Shift130", None)
        self.__project_Shift130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Shift132"):
                opp_val = getattr(old_value, "project_Shift132", None)
                if opp_val == self:
                    setattr(old_value, "project_Shift132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Shift132"):
                opp_val = getattr(value, "project_Shift132", None)
                setattr(value, "project_Shift132", self)

    @property
    def project_Shift136(self):
        return self.__project_Shift136

    @project_Shift136.setter
    def project_Shift136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Shift__project_Shift136", None)
        self.__project_Shift136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ShiftTimesheet"):
                opp_val = getattr(old_value, "project_ShiftTimesheet", None)
                if opp_val == self:
                    setattr(old_value, "project_ShiftTimesheet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ShiftTimesheet"):
                opp_val = getattr(value, "project_ShiftTimesheet", None)
                setattr(value, "project_ShiftTimesheet", self)

    @property
    def project_Shift134(self):
        return self.__project_Shift134

    @project_Shift134.setter
    def project_Shift134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Shift__project_Shift134", None)
        self.__project_Shift134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_WorkingHours"):
                opp_val = getattr(old_value, "project_WorkingHours", None)
                if opp_val == self:
                    setattr(old_value, "project_WorkingHours", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_WorkingHours"):
                opp_val = getattr(value, "project_WorkingHours", None)
                setattr(value, "project_WorkingHours", self)

    @property
    def project_Shift(self):
        return self.__project_Shift

    @project_Shift.setter
    def project_Shift(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Shift__project_Shift", None)
        self.__project_Shift = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Vacation"):
                opp_val = getattr(old_value, "project_Vacation", None)
                if opp_val == self:
                    setattr(old_value, "project_Vacation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Vacation"):
                opp_val = getattr(value, "project_Vacation", None)
                setattr(value, "project_Vacation", self)

    @property
    def project_Shift145(self):
        return self.__project_Shift145

    @project_Shift145.setter
    def project_Shift145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Shift__project_Shift145", None)
        self.__project_Shift145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ShiftsAllocate"):
                opp_val = getattr(old_value, "project_ShiftsAllocate", None)
                if opp_val == self:
                    setattr(old_value, "project_ShiftsAllocate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ShiftsAllocate"):
                opp_val = getattr(value, "project_ShiftsAllocate", None)
                setattr(value, "project_ShiftsAllocate", self)

    @property
    def project_Shift140(self):
        return self.__project_Shift140

    @project_Shift140.setter
    def project_Shift140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Shift__project_Shift140", None)
        self.__project_Shift140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_ShiftsLimit139"):
                opp_val = getattr(old_value, "project_ShiftsLimit139", None)
                if opp_val == self:
                    setattr(old_value, "project_ShiftsLimit139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_ShiftsLimit139"):
                opp_val = getattr(value, "project_ShiftsLimit139", None)
                setattr(value, "project_ShiftsLimit139", self)

class project_StatusSheetReport(Property):

    def __init__(self, filename: str, project_StatusSheetReport: set["project_StatusSheetReportAttribute"] = None):
        self.filename = filename
        self.project_StatusSheetReport = project_StatusSheetReport if project_StatusSheetReport is not None else set()
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def project_StatusSheetReport(self):
        return self.__project_StatusSheetReport

    @project_StatusSheetReport.setter
    def project_StatusSheetReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_StatusSheetReport__project_StatusSheetReport", None)
        self.__project_StatusSheetReport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_StatusSheetReportAttribute"):
                    opp_val = getattr(item, "project_StatusSheetReportAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_StatusSheetReportAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_StatusSheetReportAttribute"):
                    opp_val = getattr(item, "project_StatusSheetReportAttribute", None)
                    
                    setattr(item, "project_StatusSheetReportAttribute", self)
                    

class project_SupplementAccount(Property):

    pass
class project_Rate(Property, ResourceAttribute):

    def __init__(self, rate: float):
        self.rate = rate
        
    @property
    def rate(self) -> float:
        return self.__rate

    @rate.setter
    def rate(self, rate: float):
        self.__rate = rate

class project_ProjectIds(Property):

    def __init__(self, ids: str):
        self.ids = ids
        
    @property
    def ids(self) -> str:
        return self.__ids

    @ids.setter
    def ids(self, ids: str):
        self.__ids = ids

class project_IncludeProperties(Property):

    def __init__(self, importURI: str, project_IncludeProperties: set["project_IncludePropertiesAttribute"] = None):
        self.importURI = importURI
        self.project_IncludeProperties = project_IncludeProperties if project_IncludeProperties is not None else set()
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def project_IncludeProperties(self):
        return self.__project_IncludeProperties

    @project_IncludeProperties.setter
    def project_IncludeProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_IncludeProperties__project_IncludeProperties", None)
        self.__project_IncludeProperties = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_IncludePropertiesAttribute"):
                    opp_val = getattr(item, "project_IncludePropertiesAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_IncludePropertiesAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_IncludePropertiesAttribute"):
                    opp_val = getattr(item, "project_IncludePropertiesAttribute", None)
                    
                    setattr(item, "project_IncludePropertiesAttribute", self)
                    

class project_Macro(Property):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class project_Copyright(Property):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class project_Flags(Property, ReportAttribute, StatusStatusSheetAttribute, TaskAttribute, AccountAttribute, StatusTimesheetAttribute, ResourceAttribute):

    def __init__(self, flags: str):
        self.flags = flags
        
    @property
    def flags(self) -> str:
        return self.__flags

    @flags.setter
    def flags(self, flags: str):
        self.__flags = flags

class project_ResourceReport(ReportAttribute, Property):

    pass
class project_Balance(ReportAttribute, Property):

    pass
class project_NikuReport(Property):

    def __init__(self, filename: str, project_NikuReport: set["project_NikuReportAttribute"] = None):
        self.filename = filename
        self.project_NikuReport = project_NikuReport if project_NikuReport is not None else set()
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def project_NikuReport(self):
        return self.__project_NikuReport

    @project_NikuReport.setter
    def project_NikuReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_NikuReport__project_NikuReport", None)
        self.__project_NikuReport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_NikuReportAttribute"):
                    opp_val = getattr(item, "project_NikuReportAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_NikuReportAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_NikuReportAttribute"):
                    opp_val = getattr(item, "project_NikuReportAttribute", None)
                    
                    setattr(item, "project_NikuReportAttribute", self)
                    

class project_Account(AccountAttribute, Property):

    def __init__(self, id: str, name: str, project_Account: set["project_AccountAttribute"] = None, project_Account5: "project_AccountPrefix" = None, project_Account7: "project_AccountRoot" = None, project_Account31: "project_Balance" = None, project_Account34: "project_Balance" = None, project_Account161: "project_SupplementAccount" = None, project_Account226: "project_AccountShare" = None):
        self.id = id
        self.name = name
        self.project_Account = project_Account if project_Account is not None else set()
        self.project_Account5 = project_Account5
        self.project_Account7 = project_Account7
        self.project_Account31 = project_Account31
        self.project_Account34 = project_Account34
        self.project_Account161 = project_Account161
        self.project_Account226 = project_Account226
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def project_Account34(self):
        return self.__project_Account34

    @project_Account34.setter
    def project_Account34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Account__project_Account34", None)
        self.__project_Account34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Balance33"):
                opp_val = getattr(old_value, "project_Balance33", None)
                if opp_val == self:
                    setattr(old_value, "project_Balance33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Balance33"):
                opp_val = getattr(value, "project_Balance33", None)
                setattr(value, "project_Balance33", self)

    @property
    def project_Account5(self):
        return self.__project_Account5

    @project_Account5.setter
    def project_Account5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Account__project_Account5", None)
        self.__project_Account5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_AccountPrefix"):
                opp_val = getattr(old_value, "project_AccountPrefix", None)
                if opp_val == self:
                    setattr(old_value, "project_AccountPrefix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_AccountPrefix"):
                opp_val = getattr(value, "project_AccountPrefix", None)
                setattr(value, "project_AccountPrefix", self)

    @property
    def project_Account7(self):
        return self.__project_Account7

    @project_Account7.setter
    def project_Account7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Account__project_Account7", None)
        self.__project_Account7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_AccountRoot"):
                opp_val = getattr(old_value, "project_AccountRoot", None)
                if opp_val == self:
                    setattr(old_value, "project_AccountRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_AccountRoot"):
                opp_val = getattr(value, "project_AccountRoot", None)
                setattr(value, "project_AccountRoot", self)

    @property
    def project_Account(self):
        return self.__project_Account

    @project_Account.setter
    def project_Account(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Account__project_Account", None)
        self.__project_Account = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_AccountAttribute"):
                    opp_val = getattr(item, "project_AccountAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_AccountAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_AccountAttribute"):
                    opp_val = getattr(item, "project_AccountAttribute", None)
                    
                    setattr(item, "project_AccountAttribute", self)
                    

    @property
    def project_Account226(self):
        return self.__project_Account226

    @project_Account226.setter
    def project_Account226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Account__project_Account226", None)
        self.__project_Account226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_AccountShare225"):
                opp_val = getattr(old_value, "project_AccountShare225", None)
                if opp_val == self:
                    setattr(old_value, "project_AccountShare225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_AccountShare225"):
                opp_val = getattr(value, "project_AccountShare225", None)
                setattr(value, "project_AccountShare225", self)

    @property
    def project_Account161(self):
        return self.__project_Account161

    @project_Account161.setter
    def project_Account161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Account__project_Account161", None)
        self.__project_Account161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_SupplementAccount"):
                opp_val = getattr(old_value, "project_SupplementAccount", None)
                if opp_val == self:
                    setattr(old_value, "project_SupplementAccount", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_SupplementAccount"):
                opp_val = getattr(value, "project_SupplementAccount", None)
                setattr(value, "project_SupplementAccount", self)

    @property
    def project_Account31(self):
        return self.__project_Account31

    @project_Account31.setter
    def project_Account31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Account__project_Account31", None)
        self.__project_Account31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Balance"):
                opp_val = getattr(old_value, "project_Balance", None)
                if opp_val == self:
                    setattr(old_value, "project_Balance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Balance"):
                opp_val = getattr(value, "project_Balance", None)
                setattr(value, "project_Balance", self)

class project_Property:

    pass
class project_Project:

    def __init__(self, id: str, name: str, version: str, project_Project: "project_Global" = None, project_Project9: "project_Interval2" = None, project_Project11: set["project_ProjectAttribute"] = None):
        self.id = id
        self.name = name
        self.version = version
        self.project_Project = project_Project
        self.project_Project9 = project_Project9
        self.project_Project11 = project_Project11 if project_Project11 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def project_Project9(self):
        return self.__project_Project9

    @project_Project9.setter
    def project_Project9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Project__project_Project9", None)
        self.__project_Project9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Interval2"):
                opp_val = getattr(old_value, "project_Interval2", None)
                if opp_val == self:
                    setattr(old_value, "project_Interval2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Interval2"):
                opp_val = getattr(value, "project_Interval2", None)
                setattr(value, "project_Interval2", self)

    @property
    def project_Project(self):
        return self.__project_Project

    @project_Project.setter
    def project_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Project__project_Project", None)
        self.__project_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Global"):
                opp_val = getattr(old_value, "project_Global", None)
                if opp_val == self:
                    setattr(old_value, "project_Global", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Global"):
                opp_val = getattr(value, "project_Global", None)
                setattr(value, "project_Global", self)

    @property
    def project_Project11(self):
        return self.__project_Project11

    @project_Project11.setter
    def project_Project11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Project__project_Project11", None)
        self.__project_Project11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_ProjectAttribute"):
                    opp_val = getattr(item, "project_ProjectAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "project_ProjectAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_ProjectAttribute"):
                    opp_val = getattr(item, "project_ProjectAttribute", None)
                    
                    setattr(item, "project_ProjectAttribute", self)
                    
