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
class LeaveType(Enum):
    project = "project"
    annual = "annual"
    special = "special"
    sick = "sick"
    unpaid = "unpaid"
    holiday = "holiday"
    unemployed = "unemployed"
class BuildInMacro(Enum):
    projectstart = "projectstart"
    projectend = "projectend"
    now = "now"
class PurgeReportAttribute(Enum):
    SORTRESOURCES = "SORTRESOURCES"
    SORTTASKS = "SORTTASKS"
    COLUMNS = "COLUMNS"
    DEFINITIONS = "DEFINITIONS"
    FLAGS = "FLAGS"
    FORMATS = "FORMATS"
    JOURNALATTRIBUTES = "JOURNALATTRIBUTES"
    SCENARIOS = "SCENARIOS"
    SORTACCOUNTS = "SORTACCOUNTS"
    SORTJOURNALENTRIES = "SORTJOURNALENTRIES"
class AlertLevel(Enum):
    RED = "RED"
    YELLOW = "YELLOW"
    GREEN = "GREEN"
class JournalModeValue(Enum):
    JOURNAL = "JOURNAL"
    JOURNAL_SUB = "JOURNAL_SUB"
    STATUS_DOWN = "STATUS_DOWN"
    STATUS_UP = "STATUS_UP"
    ALERTS_DOWN = "ALERTS_DOWN"
class SelectArgument(Enum):
    MINALLOCATED = "MINALLOCATED"
    ORDER = "ORDER"
    RANDOM = "RANDOM"
    MAXLOADED = "MAXLOADED"
    MINLOADED = "MINLOADED"
class LoadDisplayUnit(Enum):
    DAYS = "DAYS"
    HOURS = "HOURS"
    LONGAUTO = "LONGAUTO"
    MINUTES = "MINUTES"
    MONTHS = "MONTHS"
    SHORTAUTO = "SHORTAUTO"
    WEEKS = "WEEKS"
    YEARS = "YEARS"
class ListTypeValues(Enum):
    BULLETS = "BULLETS"
    COMMA = "COMMA"
    NUMBERED = "NUMBERED"
class DependsPolicy(Enum):
    ONEND = "ONEND"
    ONSTART = "ONSTART"
class Justification(Enum):
    CENTER = "CENTER"
    RIGHT = "RIGHT"
    LEFT = "LEFT"
class WorkQuantityUnit(Enum):
    PERCENT = "PERCENT"
    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"
class ColumnId(Enum):
    activetasks = "activetasks"
    annualleave = "annualleave"
    annualleavebalance = "annualleavebalance"
    alert = "alert"
    alertmessages = "alertmessages"
    alertsummaries = "alertsummaries"
    alerttrend = "alerttrend"
    balance = "balance"
    bsi = "bsi"
    chart = "chart"
    children = "children"
    daily = "daily"
    directreports = "directreports"
    duration = "duration"
    duties = "duties"
    efficiency = "efficiency"
    effort = "effort"
    effortdone = "effortdone"
    effortleft = "effortleft"
    email = "email"
    end = "end"
    flags = "flags"
    followers = "followers"
    freetime = "freetime"
    freework = "freework"
    fte = "fte"
    closedtasks = "closedtasks"
    competitorcount = "competitorcount"
    competitors = "competitors"
    complete = "complete"
    completed = "completed"
    criticalness = "criticalness"
    cost = "cost"
    journalmessages = "journalmessages"
    journalsummaries = "journalsummaries"
    line = "line"
    managers = "managers"
    maxend = "maxend"
    maxstart = "maxstart"
    minend = "minend"
    minstart = "minstart"
    monthly = "monthly"
    no = "no"
    name = "name"
    note = "note"
    opentasks = "opentasks"
    pathcriticalness = "pathcriticalness"
    precursors = "precursors"
    priority = "priority"
    quarterly = "quarterly"
    gauge = "gauge"
    rate = "rate"
    headcount = "headcount"
    reports = "reports"
    hierarchindex = "hierarchindex"
    hourly = "hourly"
    id = "id"
    index = "index"
    inputs = "inputs"
    journal = "journal"
    journal_sub = "journal_sub"
    specialleave = "specialleave"
    start = "start"
    status = "status"
    targets = "targets"
    turnover = "turnover"
    wbs = "wbs"
    unpaidleave = "unpaidleave"
    weekly = "weekly"
    yearly = "yearly"
    resources = "resources"
    responsible = "responsible"
    revenue = "revenue"
    scenario = "scenario"
    scheduling = "scheduling"
    seqno = "seqno"
    sickleave = "sickleave"
class YesNo(Enum):
    NO = "NO"
    YES = "YES"
class JournalAttributeValues(Enum):
    ALL = "ALL"
    NONE = "NONE"
    alert = "alert"
    author = "author"
    date = "date"
    details = "details"
    flags = "flags"
    headline = "headline"
    property = "property"
    propertyid = "propertyid"
    summary = "summary"
    timesheet = "timesheet"
class ReportFormat(Enum):
    CSV = "CSV"
    HTML = "HTML"
    NIKU = "NIKU"
class PurgeResourceAttribute(Enum):
    FAIL = "FAIL"
    FLAGS = "FLAGS"
    MANAGERS = "MANAGERS"
    REPORTS = "REPORTS"
    VACATIONS = "VACATIONS"
    WARN = "WARN"
class CriterionDirection(Enum):
    UP = "UP"
    DOWN = "DOWN"
class SchedulingPolicy(Enum):
    ALAP = "ALAP"
    ASAP = "ASAP"
class Weekday(Enum):
    WED = "WED"
    THR = "THR"
    FRI = "FRI"
    SAT = "SAT"
    SUN = "SUN"
    MON = "MON"
    TUE = "TUE"
class JournalEntrySortCriterion(Enum):
    DATE_DOWN = "DATE_DOWN"
    DATE_UP = "DATE_UP"
    ALERT_DOWN = "ALERT_DOWN"
    ALERT_UP = "ALERT_UP"
    PROPERTY_UP = "PROPERTY_UP"
class PurgeTaskAttribute(Enum):
    BOOKING = "BOOKING"
    CHARGE = "CHARGE"
    CHARGESET = "CHARGESET"
    DEPENDS = "DEPENDS"
    FAIL = "FAIL"
    FLAGS = "FLAGS"
    PRECEDES = "PRECEDES"
    WARN = "WARN"
class ScaleResolution(Enum):
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    QUARTER = "QUARTER"
    YEAR = "YEAR"
class TimeUnit(Enum):
    MINUTE = "MINUTE"
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"


############################################
# Definition of Classes
############################################

class LogicalExpression:

    pass
class eTJ_LogicalDateLiteral(LogicalExpression):

    pass
class eTJ_LogicalFlagExpression(LogicalExpression):

    def __init__(self, columId: str, eTJ_LogicalFlagExpression: "eTJ_Scenario" = None):
        self.columId = columId
        self.eTJ_LogicalFlagExpression = eTJ_LogicalFlagExpression
        
    @property
    def columId(self) -> str:
        return self.__columId

    @columId.setter
    def columId(self, columId: str):
        self.__columId = columId

    @property
    def eTJ_LogicalFlagExpression(self):
        return self.__eTJ_LogicalFlagExpression

    @eTJ_LogicalFlagExpression.setter
    def eTJ_LogicalFlagExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalFlagExpression__eTJ_LogicalFlagExpression", None)
        self.__eTJ_LogicalFlagExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Scenario337"):
                opp_val = getattr(old_value, "eTJ_Scenario337", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Scenario337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Scenario337"):
                opp_val = getattr(value, "eTJ_Scenario337", None)
                setattr(value, "eTJ_Scenario337", self)

class eTJ_LogicalFunctionExpression(LogicalExpression):

    pass
class Definitions:

    pass
class eTJ_Defintions(Definitions):

    def __init__(self, flags: bool, resources: bool, tasks: bool, project: bool, projectids: bool):
        self.flags = flags
        self.resources = resources
        self.tasks = tasks
        self.project = project
        self.projectids = projectids
        
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

class eTJ_LogicalStringLiteral(LogicalExpression):

    def __init__(self, value: str, eTJ_LogicalStringLiteral: "eTJ_MacroCall" = None):
        self.value = value
        self.eTJ_LogicalStringLiteral = eTJ_LogicalStringLiteral
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def eTJ_LogicalStringLiteral(self):
        return self.__eTJ_LogicalStringLiteral

    @eTJ_LogicalStringLiteral.setter
    def eTJ_LogicalStringLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalStringLiteral__eTJ_LogicalStringLiteral", None)
        self.__eTJ_LogicalStringLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_MacroCall333"):
                opp_val = getattr(old_value, "eTJ_MacroCall333", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_MacroCall333", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_MacroCall333"):
                opp_val = getattr(value, "eTJ_MacroCall333", None)
                setattr(value, "eTJ_MacroCall333", self)

class eTJ_LogicalNumeralLiteral(LogicalExpression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class eTJ_LogicalBooleanLiteral(LogicalExpression):

    def __init__(self, isTrue: bool):
        self.isTrue = isTrue
        
    @property
    def isTrue(self) -> bool:
        return self.__isTrue

    @isTrue.setter
    def isTrue(self, isTrue: bool):
        self.__isTrue = isTrue

class eTJ_LogicalAbsoluteIdExression(LogicalExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class eTJ_ExtDate:

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
class Summary:

    pass
class Right:

    pass
class Prolog:

    pass
class ListItem:

    pass
class eTJ_RichText(Summary, Left, Right, Footer, Caption, Details, Header, Prolog, Center, Headline, Epilog, ListItem):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class NumberFormat:

    pass
class CurrencyFormat:

    pass
class eTJ_RealFormat(CurrencyFormat, NumberFormat):

    def __init__(self, thousandsSeparator: str, fractionSeparator: str, fractionDigits: int, negativePrefix: str, negativeSuffix: str):
        self.thousandsSeparator = thousandsSeparator
        self.fractionSeparator = fractionSeparator
        self.fractionDigits = fractionDigits
        self.negativePrefix = negativePrefix
        self.negativeSuffix = negativeSuffix
        
    @property
    def negativePrefix(self) -> str:
        return self.__negativePrefix

    @negativePrefix.setter
    def negativePrefix(self, negativePrefix: str):
        self.__negativePrefix = negativePrefix

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

    @property
    def negativeSuffix(self) -> str:
        return self.__negativeSuffix

    @negativeSuffix.setter
    def negativeSuffix(self, negativeSuffix: str):
        self.__negativeSuffix = negativeSuffix

    @property
    def fractionDigits(self) -> int:
        return self.__fractionDigits

    @fractionDigits.setter
    def fractionDigits(self, fractionDigits: int):
        self.__fractionDigits = fractionDigits

class Precedes:

    pass
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
class eTJ_Limit(WeeklyMax, MonthlyMin, Minimum, MonthlyMax, Maximum, DailyMin, DailyMax, WeeklyMin):

    pass
class eTJ_LimitAttribute:

    pass
class eTJ_ColumnAttribute:

    pass
class GapLength:

    pass
class GapDuration:

    pass
class eTJ_WorkHours:

    def __init__(self, start: str, stop: str, eTJ_WorkHours: "eTJ_WorkingHours" = None):
        self.start = start
        self.stop = stop
        self.eTJ_WorkHours = eTJ_WorkHours
        
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
    def eTJ_WorkHours(self):
        return self.__eTJ_WorkHours

    @eTJ_WorkHours.setter
    def eTJ_WorkHours(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_WorkHours__eTJ_WorkHours", None)
        self.__eTJ_WorkHours = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_WorkingHours288"):
                opp_val = getattr(old_value, "eTJ_WorkingHours288", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_WorkingHours288"):
                opp_val = getattr(value, "eTJ_WorkingHours288", None)
                if opp_val is None:
                    setattr(value, "eTJ_WorkingHours288", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eTJ_Weekdays:

    def __init__(self, first: str, last: str, eTJ_Weekdays: "eTJ_WorkingHours" = None):
        self.first = first
        self.last = last
        self.eTJ_Weekdays = eTJ_Weekdays
        
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
    def eTJ_Weekdays(self):
        return self.__eTJ_Weekdays

    @eTJ_Weekdays.setter
    def eTJ_Weekdays(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Weekdays__eTJ_Weekdays", None)
        self.__eTJ_Weekdays = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_WorkingHours286"):
                opp_val = getattr(old_value, "eTJ_WorkingHours286", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_WorkingHours286"):
                opp_val = getattr(value, "eTJ_WorkingHours286", None)
                if opp_val is None:
                    setattr(value, "eTJ_WorkingHours286", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eTJ_TreeLevel:

    def __init__(self, level: str):
        self.level = level
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

class eTJ_TimesheetReportAttribute:

    pass
class eTJ_TimesheetAttribute:

    pass
class eTJ_TaskTimesheetAttribute:

    pass
class eTJ_TaskStatusSheetAttribute:

    pass
class StatusSheetAttribute:

    pass
class eTJ_StatusSheetReportAttribute:

    pass
class eTJ_StatusTimesheetAttribute:

    pass
class eTJ_StatusStatusSheetAttribute:

    pass
class eTJ_StatusSheetAttribute:

    pass
class SortTasks:

    pass
class TaskStatusSheetAttribute:

    pass
class eTJ_TaskStatusSheet(StatusSheetAttribute, TaskStatusSheetAttribute):

    pass
class eTJ_StatusStatusSheet(TaskStatusSheetAttribute):

    def __init__(self, level: str, text: str, eTJ_StatusStatusSheet: set["eTJ_StatusStatusSheetAttribute"] = None):
        self.level = level
        self.text = text
        self.eTJ_StatusStatusSheet = eTJ_StatusStatusSheet if eTJ_StatusStatusSheet is not None else set()
        
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
    def eTJ_StatusStatusSheet(self):
        return self.__eTJ_StatusStatusSheet

    @eTJ_StatusStatusSheet.setter
    def eTJ_StatusStatusSheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_StatusStatusSheet__eTJ_StatusStatusSheet", None)
        self.__eTJ_StatusStatusSheet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_StatusStatusSheetAttribute"):
                    opp_val = getattr(item, "eTJ_StatusStatusSheetAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_StatusStatusSheetAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_StatusStatusSheetAttribute"):
                    opp_val = getattr(item, "eTJ_StatusStatusSheetAttribute", None)
                    
                    setattr(item, "eTJ_StatusStatusSheetAttribute", self)
                    

class SortResources:

    pass
class SortJournalEntries:

    pass
class SortAccounts:

    pass
class eTJ_Sort(SortResources, SortJournalEntries, SortAccounts, SortTasks):

    def __init__(self, tree: bool, eTJ_Sort: set["eTJ_Criterion"] = None):
        self.tree = tree
        self.eTJ_Sort = eTJ_Sort if eTJ_Sort is not None else set()
        
    @property
    def tree(self) -> bool:
        return self.__tree

    @tree.setter
    def tree(self, tree: bool):
        self.__tree = tree

    @property
    def eTJ_Sort(self):
        return self.__eTJ_Sort

    @eTJ_Sort.setter
    def eTJ_Sort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Sort__eTJ_Sort", None)
        self.__eTJ_Sort = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_Criterion"):
                    opp_val = getattr(item, "eTJ_Criterion", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_Criterion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_Criterion"):
                    opp_val = getattr(item, "eTJ_Criterion", None)
                    
                    setattr(item, "eTJ_Criterion", self)
                    

class eTJ_ShiftsTask:

    pass
class eTJ_Criterion:

    def __init__(self, columnId: str, direction: str, eTJ_Criterion: "eTJ_Sort" = None, eTJ_Criterion300: "eTJ_Scenario" = None):
        self.columnId = columnId
        self.direction = direction
        self.eTJ_Criterion = eTJ_Criterion
        self.eTJ_Criterion300 = eTJ_Criterion300
        
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
    def eTJ_Criterion300(self):
        return self.__eTJ_Criterion300

    @eTJ_Criterion300.setter
    def eTJ_Criterion300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Criterion__eTJ_Criterion300", None)
        self.__eTJ_Criterion300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Scenario301"):
                opp_val = getattr(old_value, "eTJ_Scenario301", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Scenario301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Scenario301"):
                opp_val = getattr(value, "eTJ_Scenario301", None)
                setattr(value, "eTJ_Scenario301", self)

    @property
    def eTJ_Criterion(self):
        return self.__eTJ_Criterion

    @eTJ_Criterion.setter
    def eTJ_Criterion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Criterion__eTJ_Criterion", None)
        self.__eTJ_Criterion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Sort"):
                opp_val = getattr(old_value, "eTJ_Sort", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Sort"):
                opp_val = getattr(value, "eTJ_Sort", None)
                if opp_val is None:
                    setattr(value, "eTJ_Sort", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eTJ_ShiftsLimit:

    pass
class ShiftsTask:

    pass
class ShiftsResource:

    pass
class eTJ_Shifts(ShiftsResource, ShiftsTask):

    pass
class eTJ_Scheduling:

    def __init__(self, scheduling: str):
        self.scheduling = scheduling
        
    @property
    def scheduling(self) -> str:
        return self.__scheduling

    @scheduling.setter
    def scheduling(self, scheduling: str):
        self.__scheduling = scheduling

class eTJ_Scheduled:

    def __init__(self, scheduled: bool):
        self.scheduled = scheduled
        
    @property
    def scheduled(self) -> bool:
        return self.__scheduled

    @scheduled.setter
    def scheduled(self, scheduled: bool):
        self.__scheduled = scheduled

class eTJ_Responsible:

    pass
class eTJ_PurgeTask:

    def __init__(self, listAttribute: str):
        self.listAttribute = listAttribute
        
    @property
    def listAttribute(self) -> str:
        return self.__listAttribute

    @listAttribute.setter
    def listAttribute(self, listAttribute: str):
        self.__listAttribute = listAttribute

class eTJ_ProjectId:

    def __init__(self, projectId: str):
        self.projectId = projectId
        
    @property
    def projectId(self) -> str:
        return self.__projectId

    @projectId.setter
    def projectId(self, projectId: str):
        self.__projectId = projectId

class eTJ_Note:

    def __init__(self, note: str):
        self.note = note
        
    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

class eTJ_Precedes:

    pass
class eTJ_MinStart:

    pass
class eTJ_MinEnd:

    pass
class eTJ_Milestone:

    def __init__(self, milestone: bool):
        self.milestone = milestone
        
    @property
    def milestone(self) -> bool:
        return self.__milestone

    @milestone.setter
    def milestone(self, milestone: bool):
        self.__milestone = milestone

class eTJ_MaxStart:

    pass
class eTJ_MaxEnd:

    pass
class eTJ_LimitsAttribute:

    pass
class eTJ_Length:

    pass
class eTJ_Interval1:

    pass
class eTJ_IncludePropertiesAttribute:

    pass
class NavigatorAttribute:

    pass
class eTJ_HideReport(NavigatorAttribute):

    pass
class eTJ_GapLength:

    pass
class eTJ_GapDuration:

    pass
class eTJ_Function:

    def __init__(self, level: int, parentId: str, distance: int, eTJ_Function: "eTJ_ISODATE" = None, eTJ_Function80: "eTJ_Scenario" = None, eTJ_Function83: "eTJ_Task" = None, eTJ_Function86: "eTJ_Resource" = None, eTJ_Function331: "eTJ_LogicalFunctionExpression" = None):
        self.level = level
        self.parentId = parentId
        self.distance = distance
        self.eTJ_Function = eTJ_Function
        self.eTJ_Function80 = eTJ_Function80
        self.eTJ_Function83 = eTJ_Function83
        self.eTJ_Function86 = eTJ_Function86
        self.eTJ_Function331 = eTJ_Function331
        
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

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
    def eTJ_Function80(self):
        return self.__eTJ_Function80

    @eTJ_Function80.setter
    def eTJ_Function80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Function__eTJ_Function80", None)
        self.__eTJ_Function80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Scenario81"):
                opp_val = getattr(old_value, "eTJ_Scenario81", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Scenario81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Scenario81"):
                opp_val = getattr(value, "eTJ_Scenario81", None)
                setattr(value, "eTJ_Scenario81", self)

    @property
    def eTJ_Function86(self):
        return self.__eTJ_Function86

    @eTJ_Function86.setter
    def eTJ_Function86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Function__eTJ_Function86", None)
        self.__eTJ_Function86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Resource87"):
                opp_val = getattr(old_value, "eTJ_Resource87", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Resource87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Resource87"):
                opp_val = getattr(value, "eTJ_Resource87", None)
                setattr(value, "eTJ_Resource87", self)

    @property
    def eTJ_Function331(self):
        return self.__eTJ_Function331

    @eTJ_Function331.setter
    def eTJ_Function331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Function__eTJ_Function331", None)
        self.__eTJ_Function331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_LogicalFunctionExpression"):
                opp_val = getattr(old_value, "eTJ_LogicalFunctionExpression", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_LogicalFunctionExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_LogicalFunctionExpression"):
                opp_val = getattr(value, "eTJ_LogicalFunctionExpression", None)
                setattr(value, "eTJ_LogicalFunctionExpression", self)

    @property
    def eTJ_Function(self):
        return self.__eTJ_Function

    @eTJ_Function.setter
    def eTJ_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Function__eTJ_Function", None)
        self.__eTJ_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ISODATE78"):
                opp_val = getattr(old_value, "eTJ_ISODATE78", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ISODATE78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ISODATE78"):
                opp_val = getattr(value, "eTJ_ISODATE78", None)
                setattr(value, "eTJ_ISODATE78", self)

    @property
    def eTJ_Function83(self):
        return self.__eTJ_Function83

    @eTJ_Function83.setter
    def eTJ_Function83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Function__eTJ_Function83", None)
        self.__eTJ_Function83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Task84"):
                opp_val = getattr(old_value, "eTJ_Task84", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Task84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Task84"):
                opp_val = getattr(value, "eTJ_Task84", None)
                setattr(value, "eTJ_Task84", self)

class eTJ_ExtendedTaskAttribute:

    def __init__(self, value: str, eTJ_ExtendedTaskAttribute: "eTJ_Extend" = None):
        self.value = value
        self.eTJ_ExtendedTaskAttribute = eTJ_ExtendedTaskAttribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def eTJ_ExtendedTaskAttribute(self):
        return self.__eTJ_ExtendedTaskAttribute

    @eTJ_ExtendedTaskAttribute.setter
    def eTJ_ExtendedTaskAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_ExtendedTaskAttribute__eTJ_ExtendedTaskAttribute", None)
        self.__eTJ_ExtendedTaskAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Extend74"):
                opp_val = getattr(old_value, "eTJ_Extend74", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Extend74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Extend74"):
                opp_val = getattr(value, "eTJ_Extend74", None)
                setattr(value, "eTJ_Extend74", self)

class eTJ_Extend:

    def __init__(self, scenariospecific: bool, name: str, description: str, inherit: bool, eTJ_Extend: "eTJ_ExtendResource" = None, eTJ_Extend70: "eTJ_ExtendedResourceAttribute" = None, eTJ_Extend72: "eTJ_ExtendTask" = None, eTJ_Extend74: "eTJ_ExtendedTaskAttribute" = None, eTJ_Extend293: "eTJ_ExtendedResourceAttributeColumn" = None):
        self.scenariospecific = scenariospecific
        self.name = name
        self.description = description
        self.inherit = inherit
        self.eTJ_Extend = eTJ_Extend
        self.eTJ_Extend70 = eTJ_Extend70
        self.eTJ_Extend72 = eTJ_Extend72
        self.eTJ_Extend74 = eTJ_Extend74
        self.eTJ_Extend293 = eTJ_Extend293
        
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
    def inherit(self) -> bool:
        return self.__inherit

    @inherit.setter
    def inherit(self, inherit: bool):
        self.__inherit = inherit

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def eTJ_Extend70(self):
        return self.__eTJ_Extend70

    @eTJ_Extend70.setter
    def eTJ_Extend70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Extend__eTJ_Extend70", None)
        self.__eTJ_Extend70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ExtendedResourceAttribute"):
                opp_val = getattr(old_value, "eTJ_ExtendedResourceAttribute", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ExtendedResourceAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ExtendedResourceAttribute"):
                opp_val = getattr(value, "eTJ_ExtendedResourceAttribute", None)
                setattr(value, "eTJ_ExtendedResourceAttribute", self)

    @property
    def eTJ_Extend74(self):
        return self.__eTJ_Extend74

    @eTJ_Extend74.setter
    def eTJ_Extend74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Extend__eTJ_Extend74", None)
        self.__eTJ_Extend74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ExtendedTaskAttribute"):
                opp_val = getattr(old_value, "eTJ_ExtendedTaskAttribute", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ExtendedTaskAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ExtendedTaskAttribute"):
                opp_val = getattr(value, "eTJ_ExtendedTaskAttribute", None)
                setattr(value, "eTJ_ExtendedTaskAttribute", self)

    @property
    def eTJ_Extend72(self):
        return self.__eTJ_Extend72

    @eTJ_Extend72.setter
    def eTJ_Extend72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Extend__eTJ_Extend72", None)
        self.__eTJ_Extend72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ExtendTask"):
                opp_val = getattr(old_value, "eTJ_ExtendTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ExtendTask"):
                opp_val = getattr(value, "eTJ_ExtendTask", None)
                if opp_val is None:
                    setattr(value, "eTJ_ExtendTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eTJ_Extend(self):
        return self.__eTJ_Extend

    @eTJ_Extend.setter
    def eTJ_Extend(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Extend__eTJ_Extend", None)
        self.__eTJ_Extend = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ExtendResource"):
                opp_val = getattr(old_value, "eTJ_ExtendResource", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ExtendResource"):
                opp_val = getattr(value, "eTJ_ExtendResource", None)
                if opp_val is None:
                    setattr(value, "eTJ_ExtendResource", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eTJ_Extend293(self):
        return self.__eTJ_Extend293

    @eTJ_Extend293.setter
    def eTJ_Extend293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Extend__eTJ_Extend293", None)
        self.__eTJ_Extend293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ExtendedResourceAttributeColumn"):
                opp_val = getattr(old_value, "eTJ_ExtendedResourceAttributeColumn", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ExtendedResourceAttributeColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ExtendedResourceAttributeColumn"):
                opp_val = getattr(value, "eTJ_ExtendedResourceAttributeColumn", None)
                setattr(value, "eTJ_ExtendedResourceAttributeColumn", self)

class eTJ_EndCredit:

    def __init__(self, credit: float):
        self.credit = credit
        
    @property
    def credit(self) -> float:
        return self.__credit

    @credit.setter
    def credit(self, credit: float):
        self.__credit = credit

class TimesheetReportAttribute:

    pass
class TaskTimesheetAttribute:

    pass
class StatusSheetReportAttribute:

    pass
class NikuReportAttribute:

    pass
class eTJ_Timeoff(NikuReportAttribute):

    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id
        
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
class eTJ_Priority(TaskTimesheetAttribute, NewTaskAttribute):

    def __init__(self, priority: int):
        self.priority = priority
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

class eTJ_Remaining(TaskTimesheetAttribute, NewTaskAttribute):

    pass
class eTJ_Work(TaskTimesheetAttribute, NewTaskAttribute):

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

class IcalReportAttribute:

    pass
class eTJ_ScenarioIcal(IcalReportAttribute):

    pass
class eTJ_Effort:

    pass
class eTJ_DurationQuantity(GapDuration, GapLength):

    def __init__(self, value: float, unit: str, eTJ_DurationQuantity: "eTJ_Duration" = None, eTJ_DurationQuantity65: "eTJ_Effort" = None, eTJ_DurationQuantity104: "eTJ_Interval1" = None, eTJ_DurationQuantity113: "eTJ_Interval2" = None, eTJ_DurationQuantity122: "eTJ_Interval3" = None, eTJ_DurationQuantity131: "eTJ_Interval4" = None, eTJ_DurationQuantity144: "eTJ_Length" = None, eTJ_DurationQuantity170: "eTJ_Remaining" = None, eTJ_DurationQuantity303: "eTJ_Limit" = None, eTJ_DurationQuantity329: "eTJ_ISODATE" = None):
        self.value = value
        self.unit = unit
        self.eTJ_DurationQuantity = eTJ_DurationQuantity
        self.eTJ_DurationQuantity65 = eTJ_DurationQuantity65
        self.eTJ_DurationQuantity104 = eTJ_DurationQuantity104
        self.eTJ_DurationQuantity113 = eTJ_DurationQuantity113
        self.eTJ_DurationQuantity122 = eTJ_DurationQuantity122
        self.eTJ_DurationQuantity131 = eTJ_DurationQuantity131
        self.eTJ_DurationQuantity144 = eTJ_DurationQuantity144
        self.eTJ_DurationQuantity170 = eTJ_DurationQuantity170
        self.eTJ_DurationQuantity303 = eTJ_DurationQuantity303
        self.eTJ_DurationQuantity329 = eTJ_DurationQuantity329
        
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
    def eTJ_DurationQuantity104(self):
        return self.__eTJ_DurationQuantity104

    @eTJ_DurationQuantity104.setter
    def eTJ_DurationQuantity104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_DurationQuantity__eTJ_DurationQuantity104", None)
        self.__eTJ_DurationQuantity104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Interval1103"):
                opp_val = getattr(old_value, "eTJ_Interval1103", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Interval1103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Interval1103"):
                opp_val = getattr(value, "eTJ_Interval1103", None)
                setattr(value, "eTJ_Interval1103", self)

    @property
    def eTJ_DurationQuantity122(self):
        return self.__eTJ_DurationQuantity122

    @eTJ_DurationQuantity122.setter
    def eTJ_DurationQuantity122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_DurationQuantity__eTJ_DurationQuantity122", None)
        self.__eTJ_DurationQuantity122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Interval3121"):
                opp_val = getattr(old_value, "eTJ_Interval3121", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Interval3121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Interval3121"):
                opp_val = getattr(value, "eTJ_Interval3121", None)
                setattr(value, "eTJ_Interval3121", self)

    @property
    def eTJ_DurationQuantity113(self):
        return self.__eTJ_DurationQuantity113

    @eTJ_DurationQuantity113.setter
    def eTJ_DurationQuantity113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_DurationQuantity__eTJ_DurationQuantity113", None)
        self.__eTJ_DurationQuantity113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Interval2112"):
                opp_val = getattr(old_value, "eTJ_Interval2112", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Interval2112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Interval2112"):
                opp_val = getattr(value, "eTJ_Interval2112", None)
                setattr(value, "eTJ_Interval2112", self)

    @property
    def eTJ_DurationQuantity131(self):
        return self.__eTJ_DurationQuantity131

    @eTJ_DurationQuantity131.setter
    def eTJ_DurationQuantity131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_DurationQuantity__eTJ_DurationQuantity131", None)
        self.__eTJ_DurationQuantity131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Interval4130"):
                opp_val = getattr(old_value, "eTJ_Interval4130", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Interval4130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Interval4130"):
                opp_val = getattr(value, "eTJ_Interval4130", None)
                setattr(value, "eTJ_Interval4130", self)

    @property
    def eTJ_DurationQuantity(self):
        return self.__eTJ_DurationQuantity

    @eTJ_DurationQuantity.setter
    def eTJ_DurationQuantity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_DurationQuantity__eTJ_DurationQuantity", None)
        self.__eTJ_DurationQuantity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Duration"):
                opp_val = getattr(old_value, "eTJ_Duration", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Duration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Duration"):
                opp_val = getattr(value, "eTJ_Duration", None)
                setattr(value, "eTJ_Duration", self)

    @property
    def eTJ_DurationQuantity144(self):
        return self.__eTJ_DurationQuantity144

    @eTJ_DurationQuantity144.setter
    def eTJ_DurationQuantity144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_DurationQuantity__eTJ_DurationQuantity144", None)
        self.__eTJ_DurationQuantity144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Length"):
                opp_val = getattr(old_value, "eTJ_Length", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Length", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Length"):
                opp_val = getattr(value, "eTJ_Length", None)
                setattr(value, "eTJ_Length", self)

    @property
    def eTJ_DurationQuantity303(self):
        return self.__eTJ_DurationQuantity303

    @eTJ_DurationQuantity303.setter
    def eTJ_DurationQuantity303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_DurationQuantity__eTJ_DurationQuantity303", None)
        self.__eTJ_DurationQuantity303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Limit"):
                opp_val = getattr(old_value, "eTJ_Limit", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Limit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Limit"):
                opp_val = getattr(value, "eTJ_Limit", None)
                setattr(value, "eTJ_Limit", self)

    @property
    def eTJ_DurationQuantity65(self):
        return self.__eTJ_DurationQuantity65

    @eTJ_DurationQuantity65.setter
    def eTJ_DurationQuantity65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_DurationQuantity__eTJ_DurationQuantity65", None)
        self.__eTJ_DurationQuantity65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Effort"):
                opp_val = getattr(old_value, "eTJ_Effort", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Effort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Effort"):
                opp_val = getattr(value, "eTJ_Effort", None)
                setattr(value, "eTJ_Effort", self)

    @property
    def eTJ_DurationQuantity170(self):
        return self.__eTJ_DurationQuantity170

    @eTJ_DurationQuantity170.setter
    def eTJ_DurationQuantity170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_DurationQuantity__eTJ_DurationQuantity170", None)
        self.__eTJ_DurationQuantity170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Remaining"):
                opp_val = getattr(old_value, "eTJ_Remaining", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Remaining", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Remaining"):
                opp_val = getattr(value, "eTJ_Remaining", None)
                setattr(value, "eTJ_Remaining", self)

    @property
    def eTJ_DurationQuantity329(self):
        return self.__eTJ_DurationQuantity329

    @eTJ_DurationQuantity329.setter
    def eTJ_DurationQuantity329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_DurationQuantity__eTJ_DurationQuantity329", None)
        self.__eTJ_DurationQuantity329 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ISODATE328"):
                opp_val = getattr(old_value, "eTJ_ISODATE328", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ISODATE328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ISODATE328"):
                opp_val = getattr(value, "eTJ_ISODATE328", None)
                setattr(value, "eTJ_ISODATE328", self)

class eTJ_Duration:

    pass
class StatusTimesheetAttribute:

    pass
class eTJ_TaskDependency(Precedes):

    def __init__(self, policy: str, eTJ_TaskDependency: "eTJ_Depends" = None, eTJ_TaskDependency319: "eTJ_Task" = None, eTJ_TaskDependency322: "eTJ_GapDuration" = None, eTJ_TaskDependency324: "eTJ_GapLength" = None):
        self.policy = policy
        self.eTJ_TaskDependency = eTJ_TaskDependency
        self.eTJ_TaskDependency319 = eTJ_TaskDependency319
        self.eTJ_TaskDependency322 = eTJ_TaskDependency322
        self.eTJ_TaskDependency324 = eTJ_TaskDependency324
        
    @property
    def policy(self) -> str:
        return self.__policy

    @policy.setter
    def policy(self, policy: str):
        self.__policy = policy

    @property
    def eTJ_TaskDependency319(self):
        return self.__eTJ_TaskDependency319

    @eTJ_TaskDependency319.setter
    def eTJ_TaskDependency319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_TaskDependency__eTJ_TaskDependency319", None)
        self.__eTJ_TaskDependency319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Task320"):
                opp_val = getattr(old_value, "eTJ_Task320", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Task320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Task320"):
                opp_val = getattr(value, "eTJ_Task320", None)
                setattr(value, "eTJ_Task320", self)

    @property
    def eTJ_TaskDependency322(self):
        return self.__eTJ_TaskDependency322

    @eTJ_TaskDependency322.setter
    def eTJ_TaskDependency322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_TaskDependency__eTJ_TaskDependency322", None)
        self.__eTJ_TaskDependency322 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_GapDuration"):
                opp_val = getattr(old_value, "eTJ_GapDuration", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_GapDuration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_GapDuration"):
                opp_val = getattr(value, "eTJ_GapDuration", None)
                setattr(value, "eTJ_GapDuration", self)

    @property
    def eTJ_TaskDependency324(self):
        return self.__eTJ_TaskDependency324

    @eTJ_TaskDependency324.setter
    def eTJ_TaskDependency324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_TaskDependency__eTJ_TaskDependency324", None)
        self.__eTJ_TaskDependency324 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_GapLength"):
                opp_val = getattr(old_value, "eTJ_GapLength", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_GapLength", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_GapLength"):
                opp_val = getattr(value, "eTJ_GapLength", None)
                setattr(value, "eTJ_GapLength", self)

    @property
    def eTJ_TaskDependency(self):
        return self.__eTJ_TaskDependency

    @eTJ_TaskDependency.setter
    def eTJ_TaskDependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_TaskDependency__eTJ_TaskDependency", None)
        self.__eTJ_TaskDependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Depends"):
                opp_val = getattr(old_value, "eTJ_Depends", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Depends"):
                opp_val = getattr(value, "eTJ_Depends", None)
                if opp_val is None:
                    setattr(value, "eTJ_Depends", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eTJ_Depends:

    pass
class ExportAttribute:

    pass
class eTJ_TaskAttributes(ExportAttribute):

    def __init__(self, note: bool, minstart: bool, minend: bool, all: bool, none: bool, responsible: bool, flags: bool, maxstart: bool, maxend: bool, priority: bool, booking: bool, complete: bool, depends: bool):
        self.note = note
        self.minstart = minstart
        self.minend = minend
        self.all = all
        self.none = none
        self.responsible = responsible
        self.flags = flags
        self.maxstart = maxstart
        self.maxend = maxend
        self.priority = priority
        self.booking = booking
        self.complete = complete
        self.depends = depends
        
    @property
    def flags(self) -> bool:
        return self.__flags

    @flags.setter
    def flags(self, flags: bool):
        self.__flags = flags

    @property
    def minend(self) -> bool:
        return self.__minend

    @minend.setter
    def minend(self, minend: bool):
        self.__minend = minend

    @property
    def depends(self) -> bool:
        return self.__depends

    @depends.setter
    def depends(self, depends: bool):
        self.__depends = depends

    @property
    def maxend(self) -> bool:
        return self.__maxend

    @maxend.setter
    def maxend(self, maxend: bool):
        self.__maxend = maxend

    @property
    def responsible(self) -> bool:
        return self.__responsible

    @responsible.setter
    def responsible(self, responsible: bool):
        self.__responsible = responsible

    @property
    def minstart(self) -> bool:
        return self.__minstart

    @minstart.setter
    def minstart(self, minstart: bool):
        self.__minstart = minstart

    @property
    def priority(self) -> bool:
        return self.__priority

    @priority.setter
    def priority(self, priority: bool):
        self.__priority = priority

    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def none(self) -> bool:
        return self.__none

    @none.setter
    def none(self, none: bool):
        self.__none = none

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
    def booking(self) -> bool:
        return self.__booking

    @booking.setter
    def booking(self, booking: bool):
        self.__booking = booking

    @property
    def note(self) -> bool:
        return self.__note

    @note.setter
    def note(self, note: bool):
        self.__note = note

class eTJ_ResourceAttributes(ExportAttribute):

    def __init__(self, all: bool, none: bool, vacation: bool, booking: bool, workingHours: bool):
        self.all = all
        self.none = none
        self.vacation = vacation
        self.booking = booking
        self.workingHours = workingHours
        
    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def none(self) -> bool:
        return self.__none

    @none.setter
    def none(self, none: bool):
        self.__none = none

    @property
    def vacation(self) -> bool:
        return self.__vacation

    @vacation.setter
    def vacation(self, vacation: bool):
        self.__vacation = vacation

    @property
    def workingHours(self) -> bool:
        return self.__workingHours

    @workingHours.setter
    def workingHours(self, workingHours: bool):
        self.__workingHours = workingHours

    @property
    def booking(self) -> bool:
        return self.__booking

    @booking.setter
    def booking(self, booking: bool):
        self.__booking = booking

class eTJ_Definitions(ExportAttribute):

    def __init__(self, all: bool, none: bool):
        self.all = all
        self.none = none
        
    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def none(self) -> bool:
        return self.__none

    @none.setter
    def none(self, none: bool):
        self.__none = none

class LimitsAttribute:

    pass
class eTJ_MonthlyMax(LimitsAttribute):

    pass
class eTJ_WeeklyMin(LimitsAttribute):

    pass
class eTJ_MonthlyMin(LimitsAttribute):

    pass
class eTJ_WeeklyMax(LimitsAttribute):

    pass
class eTJ_Minimum(LimitsAttribute):

    pass
class eTJ_Maximum(LimitsAttribute):

    pass
class eTJ_DailyMax(LimitsAttribute):

    pass
class ProjectAttribute:

    pass
class eTJ_ExtendResource(ProjectAttribute):

    pass
class eTJ_YearlyWorkingDays(ProjectAttribute):

    def __init__(self, yearlyWorkingDays: int):
        self.yearlyWorkingDays = yearlyWorkingDays
        
    @property
    def yearlyWorkingDays(self) -> int:
        return self.__yearlyWorkingDays

    @yearlyWorkingDays.setter
    def yearlyWorkingDays(self, yearlyWorkingDays: int):
        self.__yearlyWorkingDays = yearlyWorkingDays

class eTJ_DailyWorkingHours(ProjectAttribute):

    def __init__(self, dailyWorkingHours: float):
        self.dailyWorkingHours = dailyWorkingHours
        
    @property
    def dailyWorkingHours(self) -> float:
        return self.__dailyWorkingHours

    @dailyWorkingHours.setter
    def dailyWorkingHours(self, dailyWorkingHours: float):
        self.__dailyWorkingHours = dailyWorkingHours

class eTJ_Now(ProjectAttribute):

    pass
class eTJ_TimingResolution(ProjectAttribute):

    def __init__(self, timingResolution: int):
        self.timingResolution = timingResolution
        
    @property
    def timingResolution(self) -> int:
        return self.__timingResolution

    @timingResolution.setter
    def timingResolution(self, timingResolution: int):
        self.__timingResolution = timingResolution

class eTJ_ShortTimeFormat(ProjectAttribute):

    def __init__(self, shortTimeFormat: str):
        self.shortTimeFormat = shortTimeFormat
        
    @property
    def shortTimeFormat(self) -> str:
        return self.__shortTimeFormat

    @shortTimeFormat.setter
    def shortTimeFormat(self, shortTimeFormat: str):
        self.__shortTimeFormat = shortTimeFormat

class eTJ_Include(ProjectAttribute):

    def __init__(self, importURI: str):
        self.importURI = importURI
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

class eTJ_TrackingScenario(ProjectAttribute):

    pass
class eTJ_ExtendTask(ProjectAttribute):

    pass
class eTJ_WeekStarts(ProjectAttribute):

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

class eTJ_Currency(ProjectAttribute):

    def __init__(self, currency: str):
        self.currency = currency
        
    @property
    def currency(self) -> str:
        return self.__currency

    @currency.setter
    def currency(self, currency: str):
        self.__currency = currency

class eTJ_ISODATE:

    pass
class eTJ_Complete:

    def __init__(self, complete: float):
        self.complete = complete
        
    @property
    def complete(self) -> float:
        return self.__complete

    @complete.setter
    def complete(self, complete: float):
        self.__complete = complete

class eTJ_DailyMin(LimitsAttribute):

    pass
class eTJ_AccountShare:

    def __init__(self, share: float, eTJ_AccountShare: "eTJ_ChargeSet" = None, eTJ_AccountShare290: "eTJ_Account" = None):
        self.share = share
        self.eTJ_AccountShare = eTJ_AccountShare
        self.eTJ_AccountShare290 = eTJ_AccountShare290
        
    @property
    def share(self) -> float:
        return self.__share

    @share.setter
    def share(self, share: float):
        self.__share = share

    @property
    def eTJ_AccountShare290(self):
        return self.__eTJ_AccountShare290

    @eTJ_AccountShare290.setter
    def eTJ_AccountShare290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_AccountShare__eTJ_AccountShare290", None)
        self.__eTJ_AccountShare290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Account291"):
                opp_val = getattr(old_value, "eTJ_Account291", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Account291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Account291"):
                opp_val = getattr(value, "eTJ_Account291", None)
                setattr(value, "eTJ_Account291", self)

    @property
    def eTJ_AccountShare(self):
        return self.__eTJ_AccountShare

    @eTJ_AccountShare.setter
    def eTJ_AccountShare(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_AccountShare__eTJ_AccountShare", None)
        self.__eTJ_AccountShare = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ChargeSet"):
                opp_val = getattr(old_value, "eTJ_ChargeSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ChargeSet"):
                opp_val = getattr(value, "eTJ_ChargeSet", None)
                if opp_val is None:
                    setattr(value, "eTJ_ChargeSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eTJ_ChargeSet:

    pass
class eTJ_Charge:

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

class eTJ_RGB:

    def __init__(self, value: str, eTJ_RGB: "eTJ_CellColor" = None):
        self.value = value
        self.eTJ_RGB = eTJ_RGB
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def eTJ_RGB(self):
        return self.__eTJ_RGB

    @eTJ_RGB.setter
    def eTJ_RGB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_RGB__eTJ_RGB", None)
        self.__eTJ_RGB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_CellColor56"):
                opp_val = getattr(old_value, "eTJ_CellColor56", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_CellColor56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_CellColor56"):
                opp_val = getattr(value, "eTJ_CellColor56", None)
                setattr(value, "eTJ_CellColor56", self)

class eTJ_LogicalExpression:

    def __init__(self, op: str, eTJ_LogicalExpression: "eTJ_CellColor" = None, eTJ_LogicalExpression58: "eTJ_CellText" = None, eTJ_LogicalExpression76: "eTJ_Fail" = None, eTJ_LogicalExpression89: "eTJ_HAlign" = None, eTJ_LogicalExpression95: "eTJ_HideTask" = None, eTJ_LogicalExpression91: "eTJ_HideReport" = None, eTJ_LogicalExpression93: "eTJ_HideResource" = None, eTJ_LogicalExpression148: "eTJ_LogicalExpression" = None, eTJ_LogicalExpression146: "eTJ_LogicalExpression" = None, eTJ_LogicalExpression151: "eTJ_LogicalExpression" = None, eTJ_LogicalExpression149: "eTJ_LogicalExpression" = None, eTJ_LogicalExpression182: "eTJ_RollupResource" = None, eTJ_LogicalExpression180: "eTJ_RollupAccount" = None, eTJ_LogicalExpression184: "eTJ_RollupTask" = None, eTJ_LogicalExpression284: "eTJ_Warn" = None, eTJ_LogicalExpression277: "eTJ_ToolTip" = None):
        self.op = op
        self.eTJ_LogicalExpression = eTJ_LogicalExpression
        self.eTJ_LogicalExpression58 = eTJ_LogicalExpression58
        self.eTJ_LogicalExpression76 = eTJ_LogicalExpression76
        self.eTJ_LogicalExpression89 = eTJ_LogicalExpression89
        self.eTJ_LogicalExpression95 = eTJ_LogicalExpression95
        self.eTJ_LogicalExpression91 = eTJ_LogicalExpression91
        self.eTJ_LogicalExpression93 = eTJ_LogicalExpression93
        self.eTJ_LogicalExpression148 = eTJ_LogicalExpression148
        self.eTJ_LogicalExpression146 = eTJ_LogicalExpression146
        self.eTJ_LogicalExpression151 = eTJ_LogicalExpression151
        self.eTJ_LogicalExpression149 = eTJ_LogicalExpression149
        self.eTJ_LogicalExpression182 = eTJ_LogicalExpression182
        self.eTJ_LogicalExpression180 = eTJ_LogicalExpression180
        self.eTJ_LogicalExpression184 = eTJ_LogicalExpression184
        self.eTJ_LogicalExpression284 = eTJ_LogicalExpression284
        self.eTJ_LogicalExpression277 = eTJ_LogicalExpression277
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def eTJ_LogicalExpression284(self):
        return self.__eTJ_LogicalExpression284

    @eTJ_LogicalExpression284.setter
    def eTJ_LogicalExpression284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression284", None)
        self.__eTJ_LogicalExpression284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Warn"):
                opp_val = getattr(old_value, "eTJ_Warn", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Warn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Warn"):
                opp_val = getattr(value, "eTJ_Warn", None)
                setattr(value, "eTJ_Warn", self)

    @property
    def eTJ_LogicalExpression180(self):
        return self.__eTJ_LogicalExpression180

    @eTJ_LogicalExpression180.setter
    def eTJ_LogicalExpression180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression180", None)
        self.__eTJ_LogicalExpression180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_RollupAccount"):
                opp_val = getattr(old_value, "eTJ_RollupAccount", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_RollupAccount", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_RollupAccount"):
                opp_val = getattr(value, "eTJ_RollupAccount", None)
                setattr(value, "eTJ_RollupAccount", self)

    @property
    def eTJ_LogicalExpression184(self):
        return self.__eTJ_LogicalExpression184

    @eTJ_LogicalExpression184.setter
    def eTJ_LogicalExpression184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression184", None)
        self.__eTJ_LogicalExpression184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_RollupTask"):
                opp_val = getattr(old_value, "eTJ_RollupTask", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_RollupTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_RollupTask"):
                opp_val = getattr(value, "eTJ_RollupTask", None)
                setattr(value, "eTJ_RollupTask", self)

    @property
    def eTJ_LogicalExpression58(self):
        return self.__eTJ_LogicalExpression58

    @eTJ_LogicalExpression58.setter
    def eTJ_LogicalExpression58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression58", None)
        self.__eTJ_LogicalExpression58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_CellText"):
                opp_val = getattr(old_value, "eTJ_CellText", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_CellText", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_CellText"):
                opp_val = getattr(value, "eTJ_CellText", None)
                setattr(value, "eTJ_CellText", self)

    @property
    def eTJ_LogicalExpression146(self):
        return self.__eTJ_LogicalExpression146

    @eTJ_LogicalExpression146.setter
    def eTJ_LogicalExpression146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression146", None)
        self.__eTJ_LogicalExpression146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_LogicalExpression148"):
                opp_val = getattr(old_value, "eTJ_LogicalExpression148", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_LogicalExpression148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_LogicalExpression148"):
                opp_val = getattr(value, "eTJ_LogicalExpression148", None)
                setattr(value, "eTJ_LogicalExpression148", self)

    @property
    def eTJ_LogicalExpression148(self):
        return self.__eTJ_LogicalExpression148

    @eTJ_LogicalExpression148.setter
    def eTJ_LogicalExpression148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression148", None)
        self.__eTJ_LogicalExpression148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_LogicalExpression146"):
                opp_val = getattr(old_value, "eTJ_LogicalExpression146", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_LogicalExpression146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_LogicalExpression146"):
                opp_val = getattr(value, "eTJ_LogicalExpression146", None)
                setattr(value, "eTJ_LogicalExpression146", self)

    @property
    def eTJ_LogicalExpression149(self):
        return self.__eTJ_LogicalExpression149

    @eTJ_LogicalExpression149.setter
    def eTJ_LogicalExpression149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression149", None)
        self.__eTJ_LogicalExpression149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_LogicalExpression151"):
                opp_val = getattr(old_value, "eTJ_LogicalExpression151", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_LogicalExpression151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_LogicalExpression151"):
                opp_val = getattr(value, "eTJ_LogicalExpression151", None)
                setattr(value, "eTJ_LogicalExpression151", self)

    @property
    def eTJ_LogicalExpression93(self):
        return self.__eTJ_LogicalExpression93

    @eTJ_LogicalExpression93.setter
    def eTJ_LogicalExpression93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression93", None)
        self.__eTJ_LogicalExpression93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_HideResource"):
                opp_val = getattr(old_value, "eTJ_HideResource", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_HideResource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_HideResource"):
                opp_val = getattr(value, "eTJ_HideResource", None)
                setattr(value, "eTJ_HideResource", self)

    @property
    def eTJ_LogicalExpression89(self):
        return self.__eTJ_LogicalExpression89

    @eTJ_LogicalExpression89.setter
    def eTJ_LogicalExpression89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression89", None)
        self.__eTJ_LogicalExpression89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_HAlign"):
                opp_val = getattr(old_value, "eTJ_HAlign", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_HAlign", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_HAlign"):
                opp_val = getattr(value, "eTJ_HAlign", None)
                setattr(value, "eTJ_HAlign", self)

    @property
    def eTJ_LogicalExpression76(self):
        return self.__eTJ_LogicalExpression76

    @eTJ_LogicalExpression76.setter
    def eTJ_LogicalExpression76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression76", None)
        self.__eTJ_LogicalExpression76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Fail"):
                opp_val = getattr(old_value, "eTJ_Fail", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Fail", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Fail"):
                opp_val = getattr(value, "eTJ_Fail", None)
                setattr(value, "eTJ_Fail", self)

    @property
    def eTJ_LogicalExpression277(self):
        return self.__eTJ_LogicalExpression277

    @eTJ_LogicalExpression277.setter
    def eTJ_LogicalExpression277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression277", None)
        self.__eTJ_LogicalExpression277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ToolTip"):
                opp_val = getattr(old_value, "eTJ_ToolTip", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ToolTip", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ToolTip"):
                opp_val = getattr(value, "eTJ_ToolTip", None)
                setattr(value, "eTJ_ToolTip", self)

    @property
    def eTJ_LogicalExpression151(self):
        return self.__eTJ_LogicalExpression151

    @eTJ_LogicalExpression151.setter
    def eTJ_LogicalExpression151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression151", None)
        self.__eTJ_LogicalExpression151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_LogicalExpression149"):
                opp_val = getattr(old_value, "eTJ_LogicalExpression149", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_LogicalExpression149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_LogicalExpression149"):
                opp_val = getattr(value, "eTJ_LogicalExpression149", None)
                setattr(value, "eTJ_LogicalExpression149", self)

    @property
    def eTJ_LogicalExpression95(self):
        return self.__eTJ_LogicalExpression95

    @eTJ_LogicalExpression95.setter
    def eTJ_LogicalExpression95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression95", None)
        self.__eTJ_LogicalExpression95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_HideTask"):
                opp_val = getattr(old_value, "eTJ_HideTask", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_HideTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_HideTask"):
                opp_val = getattr(value, "eTJ_HideTask", None)
                setattr(value, "eTJ_HideTask", self)

    @property
    def eTJ_LogicalExpression91(self):
        return self.__eTJ_LogicalExpression91

    @eTJ_LogicalExpression91.setter
    def eTJ_LogicalExpression91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression91", None)
        self.__eTJ_LogicalExpression91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_HideReport"):
                opp_val = getattr(old_value, "eTJ_HideReport", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_HideReport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_HideReport"):
                opp_val = getattr(value, "eTJ_HideReport", None)
                setattr(value, "eTJ_HideReport", self)

    @property
    def eTJ_LogicalExpression182(self):
        return self.__eTJ_LogicalExpression182

    @eTJ_LogicalExpression182.setter
    def eTJ_LogicalExpression182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression182", None)
        self.__eTJ_LogicalExpression182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_RollupResource"):
                opp_val = getattr(old_value, "eTJ_RollupResource", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_RollupResource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_RollupResource"):
                opp_val = getattr(value, "eTJ_RollupResource", None)
                setattr(value, "eTJ_RollupResource", self)

    @property
    def eTJ_LogicalExpression(self):
        return self.__eTJ_LogicalExpression

    @eTJ_LogicalExpression.setter
    def eTJ_LogicalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LogicalExpression__eTJ_LogicalExpression", None)
        self.__eTJ_LogicalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_CellColor"):
                opp_val = getattr(old_value, "eTJ_CellColor", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_CellColor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_CellColor"):
                opp_val = getattr(value, "eTJ_CellColor", None)
                setattr(value, "eTJ_CellColor", self)

class ColumnAttribute:

    pass
class eTJ_FontColor(ColumnAttribute):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class eTJ_ExtendedResourceAttributeColumn(ColumnAttribute):

    pass
class eTJ_Scale(ColumnAttribute):

    def __init__(self, scale: str):
        self.scale = scale
        
    @property
    def scale(self) -> str:
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale

class eTJ_HAlign(ColumnAttribute):

    def __init__(self, justification: str, eTJ_HAlign: "eTJ_LogicalExpression" = None):
        self.justification = justification
        self.eTJ_HAlign = eTJ_HAlign
        
    @property
    def justification(self) -> str:
        return self.__justification

    @justification.setter
    def justification(self, justification: str):
        self.__justification = justification

    @property
    def eTJ_HAlign(self):
        return self.__eTJ_HAlign

    @eTJ_HAlign.setter
    def eTJ_HAlign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_HAlign__eTJ_HAlign", None)
        self.__eTJ_HAlign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_LogicalExpression89"):
                opp_val = getattr(old_value, "eTJ_LogicalExpression89", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_LogicalExpression89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_LogicalExpression89"):
                opp_val = getattr(value, "eTJ_LogicalExpression89", None)
                setattr(value, "eTJ_LogicalExpression89", self)

class eTJ_ListType(ColumnAttribute):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class eTJ_Width(ColumnAttribute):

    def __init__(self, width: float):
        self.width = width
        
    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

class eTJ_ListItem(ColumnAttribute):

    pass
class eTJ_CellText(ColumnAttribute):

    def __init__(self, text: str, eTJ_CellText: "eTJ_LogicalExpression" = None):
        self.text = text
        self.eTJ_CellText = eTJ_CellText
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def eTJ_CellText(self):
        return self.__eTJ_CellText

    @eTJ_CellText.setter
    def eTJ_CellText(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_CellText__eTJ_CellText", None)
        self.__eTJ_CellText = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_LogicalExpression58"):
                opp_val = getattr(old_value, "eTJ_LogicalExpression58", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_LogicalExpression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_LogicalExpression58"):
                opp_val = getattr(value, "eTJ_LogicalExpression58", None)
                setattr(value, "eTJ_LogicalExpression58", self)

class eTJ_Column:

    def __init__(self, id: str, eTJ_Column: "eTJ_Columns" = None, eTJ_Column295: "eTJ_ExtendedResourceAttributeColumn" = None, eTJ_Column298: set["eTJ_ColumnAttribute"] = None):
        self.id = id
        self.eTJ_Column = eTJ_Column
        self.eTJ_Column295 = eTJ_Column295
        self.eTJ_Column298 = eTJ_Column298 if eTJ_Column298 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def eTJ_Column295(self):
        return self.__eTJ_Column295

    @eTJ_Column295.setter
    def eTJ_Column295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Column__eTJ_Column295", None)
        self.__eTJ_Column295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ExtendedResourceAttributeColumn296"):
                opp_val = getattr(old_value, "eTJ_ExtendedResourceAttributeColumn296", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ExtendedResourceAttributeColumn296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ExtendedResourceAttributeColumn296"):
                opp_val = getattr(value, "eTJ_ExtendedResourceAttributeColumn296", None)
                setattr(value, "eTJ_ExtendedResourceAttributeColumn296", self)

    @property
    def eTJ_Column(self):
        return self.__eTJ_Column

    @eTJ_Column.setter
    def eTJ_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Column__eTJ_Column", None)
        self.__eTJ_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Columns"):
                opp_val = getattr(old_value, "eTJ_Columns", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Columns"):
                opp_val = getattr(value, "eTJ_Columns", None)
                if opp_val is None:
                    setattr(value, "eTJ_Columns", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eTJ_Column298(self):
        return self.__eTJ_Column298

    @eTJ_Column298.setter
    def eTJ_Column298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Column__eTJ_Column298", None)
        self.__eTJ_Column298 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_ColumnAttribute"):
                    opp_val = getattr(item, "eTJ_ColumnAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_ColumnAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_ColumnAttribute"):
                    opp_val = getattr(item, "eTJ_ColumnAttribute", None)
                    
                    setattr(item, "eTJ_ColumnAttribute", self)
                    

class eTJ_BookingTask:

    pass
class eTJ_Interval4:

    pass
class eTJ_Booking:

    def __init__(self, overtime: int, sloppy: int, eTJ_Booking: "eTJ_Interval4" = None, eTJ_Booking48: "eTJ_BookingTask" = None, eTJ_Booking53: "eTJ_BookingResource" = None):
        self.overtime = overtime
        self.sloppy = sloppy
        self.eTJ_Booking = eTJ_Booking
        self.eTJ_Booking48 = eTJ_Booking48
        self.eTJ_Booking53 = eTJ_Booking53
        
    @property
    def sloppy(self) -> int:
        return self.__sloppy

    @sloppy.setter
    def sloppy(self, sloppy: int):
        self.__sloppy = sloppy

    @property
    def overtime(self) -> int:
        return self.__overtime

    @overtime.setter
    def overtime(self, overtime: int):
        self.__overtime = overtime

    @property
    def eTJ_Booking53(self):
        return self.__eTJ_Booking53

    @eTJ_Booking53.setter
    def eTJ_Booking53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Booking__eTJ_Booking53", None)
        self.__eTJ_Booking53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_BookingResource52"):
                opp_val = getattr(old_value, "eTJ_BookingResource52", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_BookingResource52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_BookingResource52"):
                opp_val = getattr(value, "eTJ_BookingResource52", None)
                setattr(value, "eTJ_BookingResource52", self)

    @property
    def eTJ_Booking48(self):
        return self.__eTJ_Booking48

    @eTJ_Booking48.setter
    def eTJ_Booking48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Booking__eTJ_Booking48", None)
        self.__eTJ_Booking48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_BookingTask47"):
                opp_val = getattr(old_value, "eTJ_BookingTask47", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_BookingTask47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_BookingTask47"):
                opp_val = getattr(value, "eTJ_BookingTask47", None)
                setattr(value, "eTJ_BookingTask47", self)

    @property
    def eTJ_Booking(self):
        return self.__eTJ_Booking

    @eTJ_Booking.setter
    def eTJ_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Booking__eTJ_Booking", None)
        self.__eTJ_Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Interval4"):
                opp_val = getattr(old_value, "eTJ_Interval4", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Interval4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Interval4"):
                opp_val = getattr(value, "eTJ_Interval4", None)
                setattr(value, "eTJ_Interval4", self)

class StatusStatusSheetAttribute:

    pass
class eTJ_Summary(StatusStatusSheetAttribute, StatusTimesheetAttribute):

    pass
class eTJ_Details(StatusStatusSheetAttribute, StatusTimesheetAttribute):

    pass
class eTJ_Author(StatusStatusSheetAttribute):

    pass
class AllocateResourceAttribute:

    pass
class eTJ_Persistent(AllocateResourceAttribute):

    def __init__(self, persistent: bool):
        self.persistent = persistent
        
    @property
    def persistent(self) -> bool:
        return self.__persistent

    @persistent.setter
    def persistent(self, persistent: bool):
        self.__persistent = persistent

class eTJ_Select(AllocateResourceAttribute):

    def __init__(self, argument: str):
        self.argument = argument
        
    @property
    def argument(self) -> str:
        return self.__argument

    @argument.setter
    def argument(self, argument: str):
        self.__argument = argument

class eTJ_ShiftsAllocate(AllocateResourceAttribute):

    pass
class eTJ_Mandatory(AllocateResourceAttribute):

    def __init__(self, mandatory: bool):
        self.mandatory = mandatory
        
    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

class eTJ_Alternative(AllocateResourceAttribute):

    pass
class eTJ_Alert:

    def __init__(self, level: str, eTJ_Alert: "eTJ_JournalEntry" = None):
        self.level = level
        self.eTJ_Alert = eTJ_Alert
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def eTJ_Alert(self):
        return self.__eTJ_Alert

    @eTJ_Alert.setter
    def eTJ_Alert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Alert__eTJ_Alert", None)
        self.__eTJ_Alert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_JournalEntry135"):
                opp_val = getattr(old_value, "eTJ_JournalEntry135", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_JournalEntry135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_JournalEntry135"):
                opp_val = getattr(value, "eTJ_JournalEntry135", None)
                setattr(value, "eTJ_JournalEntry135", self)

class eTJ_NikuReportAttribute:

    pass
class eTJ_NewTaskAttribute:

    pass
class TimesheetAttribute:

    pass
class eTJ_ShiftTimesheet(TimesheetAttribute):

    pass
class eTJ_StatusTimesheet(TimesheetAttribute, TaskTimesheetAttribute):

    def __init__(self, level: str, text: str, eTJ_StatusTimesheet: set["eTJ_StatusTimesheetAttribute"] = None):
        self.level = level
        self.text = text
        self.eTJ_StatusTimesheet = eTJ_StatusTimesheet if eTJ_StatusTimesheet is not None else set()
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def eTJ_StatusTimesheet(self):
        return self.__eTJ_StatusTimesheet

    @eTJ_StatusTimesheet.setter
    def eTJ_StatusTimesheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_StatusTimesheet__eTJ_StatusTimesheet", None)
        self.__eTJ_StatusTimesheet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_StatusTimesheetAttribute"):
                    opp_val = getattr(item, "eTJ_StatusTimesheetAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_StatusTimesheetAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_StatusTimesheetAttribute"):
                    opp_val = getattr(item, "eTJ_StatusTimesheetAttribute", None)
                    
                    setattr(item, "eTJ_StatusTimesheetAttribute", self)
                    

class eTJ_TaskTimesheet(TimesheetAttribute):

    pass
class eTJ_NewTask(TimesheetAttribute):

    def __init__(self, id: str, text: str, eTJ_NewTask: set["eTJ_NewTaskAttribute"] = None):
        self.id = id
        self.text = text
        self.eTJ_NewTask = eTJ_NewTask if eTJ_NewTask is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def eTJ_NewTask(self):
        return self.__eTJ_NewTask

    @eTJ_NewTask.setter
    def eTJ_NewTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_NewTask__eTJ_NewTask", None)
        self.__eTJ_NewTask = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_NewTaskAttribute"):
                    opp_val = getattr(item, "eTJ_NewTaskAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_NewTaskAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_NewTaskAttribute"):
                    opp_val = getattr(item, "eTJ_NewTaskAttribute", None)
                    
                    setattr(item, "eTJ_NewTaskAttribute", self)
                    

class eTJ_NavigatorAttribute:

    pass
class eTJ_AllocateResourceAttribute:

    pass
class eTJ_AllocateResource:

    pass
class eTJ_ExportAttribute:

    pass
class eTJ_IcalReportAttribute:

    pass
class eTJ_ResourceAttribute:

    pass
class TextReport:

    pass
class TaskReport:

    pass
class ResourceReport:

    pass
class AccountReport:

    pass
class eTJ_Report(ResourceReport, TaskReport, TextReport, AccountReport):

    def __init__(self, name: str, id: str, eTJ_Report: set["eTJ_ReportAttribute"] = None, eTJ_Report172: "eTJ_ReportPrefix" = None, eTJ_Report231: "eTJ_SupplementReport" = None):
        self.name = name
        self.id = id
        self.eTJ_Report = eTJ_Report if eTJ_Report is not None else set()
        self.eTJ_Report172 = eTJ_Report172
        self.eTJ_Report231 = eTJ_Report231
        
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
    def eTJ_Report172(self):
        return self.__eTJ_Report172

    @eTJ_Report172.setter
    def eTJ_Report172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Report__eTJ_Report172", None)
        self.__eTJ_Report172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ReportPrefix"):
                opp_val = getattr(old_value, "eTJ_ReportPrefix", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ReportPrefix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ReportPrefix"):
                opp_val = getattr(value, "eTJ_ReportPrefix", None)
                setattr(value, "eTJ_ReportPrefix", self)

    @property
    def eTJ_Report231(self):
        return self.__eTJ_Report231

    @eTJ_Report231.setter
    def eTJ_Report231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Report__eTJ_Report231", None)
        self.__eTJ_Report231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_SupplementReport"):
                opp_val = getattr(old_value, "eTJ_SupplementReport", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_SupplementReport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_SupplementReport"):
                opp_val = getattr(value, "eTJ_SupplementReport", None)
                setattr(value, "eTJ_SupplementReport", self)

    @property
    def eTJ_Report(self):
        return self.__eTJ_Report

    @eTJ_Report.setter
    def eTJ_Report(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Report__eTJ_Report", None)
        self.__eTJ_Report = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_ReportAttribute"):
                    opp_val = getattr(item, "eTJ_ReportAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_ReportAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_ReportAttribute"):
                    opp_val = getattr(item, "eTJ_ReportAttribute", None)
                    
                    setattr(item, "eTJ_ReportAttribute", self)
                    

class ExtDate:

    pass
class Start:

    pass
class End:

    pass
class eTJ_MacroCall(Start, End, ExtDate):

    def __init__(self, buildin: str, eTJ_MacroCall: "eTJ_Macro" = None, eTJ_MacroCall333: "eTJ_LogicalStringLiteral" = None):
        self.buildin = buildin
        self.eTJ_MacroCall = eTJ_MacroCall
        self.eTJ_MacroCall333 = eTJ_MacroCall333
        
    @property
    def buildin(self) -> str:
        return self.__buildin

    @buildin.setter
    def buildin(self, buildin: str):
        self.__buildin = buildin

    @property
    def eTJ_MacroCall(self):
        return self.__eTJ_MacroCall

    @eTJ_MacroCall.setter
    def eTJ_MacroCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_MacroCall__eTJ_MacroCall", None)
        self.__eTJ_MacroCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Macro"):
                opp_val = getattr(old_value, "eTJ_Macro", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Macro", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Macro"):
                opp_val = getattr(value, "eTJ_Macro", None)
                setattr(value, "eTJ_Macro", self)

    @property
    def eTJ_MacroCall333(self):
        return self.__eTJ_MacroCall333

    @eTJ_MacroCall333.setter
    def eTJ_MacroCall333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_MacroCall__eTJ_MacroCall333", None)
        self.__eTJ_MacroCall333 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_LogicalStringLiteral"):
                opp_val = getattr(old_value, "eTJ_LogicalStringLiteral", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_LogicalStringLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_LogicalStringLiteral"):
                opp_val = getattr(value, "eTJ_LogicalStringLiteral", None)
                setattr(value, "eTJ_LogicalStringLiteral", self)

class eTJ_EObject:

    pass
class eTJ_Scenario(ProjectAttribute):

    def __init__(self, id: str, name: str, active: str, eTJ_Scenario: "eTJ_TaskAttribute" = None, eTJ_Scenario81: "eTJ_Function" = None, eTJ_Scenario189: "eTJ_ScenarioIcal" = None, eTJ_Scenario187: "eTJ_Scenario" = None, eTJ_Scenario185: "eTJ_Scenario" = None, eTJ_Scenario191: "eTJ_Scenarios" = None, eTJ_Scenario279: "eTJ_TrackingScenario" = None, eTJ_Scenario301: "eTJ_Criterion" = None, eTJ_Scenario337: "eTJ_LogicalFlagExpression" = None):
        self.id = id
        self.name = name
        self.active = active
        self.eTJ_Scenario = eTJ_Scenario
        self.eTJ_Scenario81 = eTJ_Scenario81
        self.eTJ_Scenario189 = eTJ_Scenario189
        self.eTJ_Scenario187 = eTJ_Scenario187
        self.eTJ_Scenario185 = eTJ_Scenario185
        self.eTJ_Scenario191 = eTJ_Scenario191
        self.eTJ_Scenario279 = eTJ_Scenario279
        self.eTJ_Scenario301 = eTJ_Scenario301
        self.eTJ_Scenario337 = eTJ_Scenario337
        
    @property
    def active(self) -> str:
        return self.__active

    @active.setter
    def active(self, active: str):
        self.__active = active

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
    def eTJ_Scenario(self):
        return self.__eTJ_Scenario

    @eTJ_Scenario.setter
    def eTJ_Scenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Scenario__eTJ_Scenario", None)
        self.__eTJ_Scenario = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_TaskAttribute17"):
                opp_val = getattr(old_value, "eTJ_TaskAttribute17", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_TaskAttribute17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_TaskAttribute17"):
                opp_val = getattr(value, "eTJ_TaskAttribute17", None)
                setattr(value, "eTJ_TaskAttribute17", self)

    @property
    def eTJ_Scenario187(self):
        return self.__eTJ_Scenario187

    @eTJ_Scenario187.setter
    def eTJ_Scenario187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Scenario__eTJ_Scenario187", None)
        self.__eTJ_Scenario187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Scenario185"):
                opp_val = getattr(old_value, "eTJ_Scenario185", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Scenario185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Scenario185"):
                opp_val = getattr(value, "eTJ_Scenario185", None)
                setattr(value, "eTJ_Scenario185", self)

    @property
    def eTJ_Scenario301(self):
        return self.__eTJ_Scenario301

    @eTJ_Scenario301.setter
    def eTJ_Scenario301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Scenario__eTJ_Scenario301", None)
        self.__eTJ_Scenario301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Criterion300"):
                opp_val = getattr(old_value, "eTJ_Criterion300", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Criterion300", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Criterion300"):
                opp_val = getattr(value, "eTJ_Criterion300", None)
                setattr(value, "eTJ_Criterion300", self)

    @property
    def eTJ_Scenario185(self):
        return self.__eTJ_Scenario185

    @eTJ_Scenario185.setter
    def eTJ_Scenario185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Scenario__eTJ_Scenario185", None)
        self.__eTJ_Scenario185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Scenario187"):
                opp_val = getattr(old_value, "eTJ_Scenario187", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Scenario187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Scenario187"):
                opp_val = getattr(value, "eTJ_Scenario187", None)
                setattr(value, "eTJ_Scenario187", self)

    @property
    def eTJ_Scenario189(self):
        return self.__eTJ_Scenario189

    @eTJ_Scenario189.setter
    def eTJ_Scenario189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Scenario__eTJ_Scenario189", None)
        self.__eTJ_Scenario189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ScenarioIcal"):
                opp_val = getattr(old_value, "eTJ_ScenarioIcal", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ScenarioIcal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ScenarioIcal"):
                opp_val = getattr(value, "eTJ_ScenarioIcal", None)
                setattr(value, "eTJ_ScenarioIcal", self)

    @property
    def eTJ_Scenario279(self):
        return self.__eTJ_Scenario279

    @eTJ_Scenario279.setter
    def eTJ_Scenario279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Scenario__eTJ_Scenario279", None)
        self.__eTJ_Scenario279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_TrackingScenario"):
                opp_val = getattr(old_value, "eTJ_TrackingScenario", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_TrackingScenario", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_TrackingScenario"):
                opp_val = getattr(value, "eTJ_TrackingScenario", None)
                setattr(value, "eTJ_TrackingScenario", self)

    @property
    def eTJ_Scenario337(self):
        return self.__eTJ_Scenario337

    @eTJ_Scenario337.setter
    def eTJ_Scenario337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Scenario__eTJ_Scenario337", None)
        self.__eTJ_Scenario337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_LogicalFlagExpression"):
                opp_val = getattr(old_value, "eTJ_LogicalFlagExpression", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_LogicalFlagExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_LogicalFlagExpression"):
                opp_val = getattr(value, "eTJ_LogicalFlagExpression", None)
                setattr(value, "eTJ_LogicalFlagExpression", self)

    @property
    def eTJ_Scenario191(self):
        return self.__eTJ_Scenario191

    @eTJ_Scenario191.setter
    def eTJ_Scenario191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Scenario__eTJ_Scenario191", None)
        self.__eTJ_Scenario191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Scenarios"):
                opp_val = getattr(old_value, "eTJ_Scenarios", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Scenarios"):
                opp_val = getattr(value, "eTJ_Scenarios", None)
                if opp_val is None:
                    setattr(value, "eTJ_Scenarios", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eTJ_Scenario81(self):
        return self.__eTJ_Scenario81

    @eTJ_Scenario81.setter
    def eTJ_Scenario81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Scenario__eTJ_Scenario81", None)
        self.__eTJ_Scenario81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Function80"):
                opp_val = getattr(old_value, "eTJ_Function80", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Function80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Function80"):
                opp_val = getattr(value, "eTJ_Function80", None)
                setattr(value, "eTJ_Function80", self)

class eTJ_ReportAttribute:

    pass
class eTJ_TaskAttribute:

    pass
class eTJ_ProjectAttribute:

    pass
class eTJ_Interval2:

    pass
class ReportAttribute:

    pass
class eTJ_Scenarios(ExportAttribute, ReportAttribute):

    pass
class eTJ_SortResources(StatusSheetReportAttribute, ReportAttribute):

    pass
class eTJ_SortJournalEntries(ReportAttribute):

    pass
class eTJ_SortAccounts(ReportAttribute):

    pass
class eTJ_Footer(ReportAttribute):

    pass
class eTJ_Start(ExportAttribute, TimesheetReportAttribute, StatusSheetReportAttribute, ReportAttribute, ColumnAttribute, IcalReportAttribute, NikuReportAttribute):

    pass
class eTJ_Right(ReportAttribute):

    pass
class eTJ_Period(ExportAttribute, TimesheetReportAttribute, StatusSheetReportAttribute, ReportAttribute, ColumnAttribute, IcalReportAttribute, NikuReportAttribute):

    pass
class eTJ_Epilog(ReportAttribute):

    pass
class eTJ_TaskRoot(ReportAttribute):

    pass
class eTJ_RollupResource(ExportAttribute, ReportAttribute, IcalReportAttribute):

    pass
class eTJ_Formats(ReportAttribute, NikuReportAttribute):

    def __init__(self, formats: str):
        self.formats = formats
        
    @property
    def formats(self) -> str:
        return self.__formats

    @formats.setter
    def formats(self, formats: str):
        self.__formats = formats

class eTJ_Timezone(ExportAttribute, ReportAttribute, ProjectAttribute):

    def __init__(self, timezone: str):
        self.timezone = timezone
        
    @property
    def timezone(self) -> str:
        return self.__timezone

    @timezone.setter
    def timezone(self, timezone: str):
        self.__timezone = timezone

class eTJ_ResourceRoot(ReportAttribute):

    pass
class eTJ_Center(ReportAttribute):

    pass
class eTJ_RollupAccount(ReportAttribute):

    pass
class eTJ_HideAccount(ReportAttribute):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class eTJ_Caption(ReportAttribute):

    pass
class eTJ_End(ExportAttribute, TimesheetReportAttribute, NewTaskAttribute, StatusSheetReportAttribute, TaskTimesheetAttribute, ReportAttribute, ColumnAttribute, IcalReportAttribute, NikuReportAttribute):

    pass
class eTJ_JournalMode(ReportAttribute):

    def __init__(self, mode: str):
        self.mode = mode
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

class eTJ_Columns(ReportAttribute):

    pass
class eTJ_SortTasks(StatusSheetReportAttribute, ReportAttribute):

    pass
class eTJ_Headline(ReportAttribute, NikuReportAttribute):

    pass
class eTJ_RollupTask(ExportAttribute, ReportAttribute, IcalReportAttribute):

    pass
class eTJ_HideJournalEntry(ReportAttribute, IcalReportAttribute):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class eTJ_Left(ReportAttribute):

    pass
class eTJ_HideResource(ExportAttribute, TimesheetReportAttribute, StatusSheetReportAttribute, ReportAttribute, IcalReportAttribute, NikuReportAttribute):

    pass
class eTJ_JournalAttributes(ReportAttribute):

    def __init__(self, args: str):
        self.args = args
        
    @property
    def args(self) -> str:
        return self.__args

    @args.setter
    def args(self, args: str):
        self.__args = args

class eTJ_NumberFormat(ProjectAttribute, ReportAttribute, NikuReportAttribute):

    pass
class eTJ_AccountRoot(ReportAttribute):

    pass
class eTJ_CurrencyFormat(ReportAttribute, ProjectAttribute):

    pass
class eTJ_HideTask(ExportAttribute, StatusSheetReportAttribute, ReportAttribute, IcalReportAttribute, NikuReportAttribute):

    pass
class eTJ_Title(ReportAttribute, ColumnAttribute, NikuReportAttribute):

    def __init__(self, title: str):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class eTJ_LoadUnit(ReportAttribute):

    def __init__(self, unit: str):
        self.unit = unit
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

class eTJ_SelfContained(ReportAttribute):

    def __init__(self, selfcontained: str):
        self.selfcontained = selfcontained
        
    @property
    def selfcontained(self) -> str:
        return self.__selfcontained

    @selfcontained.setter
    def selfcontained(self, selfcontained: str):
        self.__selfcontained = selfcontained

class eTJ_PurgeReport(ReportAttribute):

    def __init__(self, listAttribute: str):
        self.listAttribute = listAttribute
        
    @property
    def listAttribute(self) -> str:
        return self.__listAttribute

    @listAttribute.setter
    def listAttribute(self, listAttribute: str):
        self.__listAttribute = listAttribute

class eTJ_Prolog(ReportAttribute):

    pass
class eTJ_Header(ReportAttribute):

    pass
class eTJ_TimeFormat(ReportAttribute, ProjectAttribute):

    def __init__(self, timeformat: str):
        self.timeformat = timeformat
        
    @property
    def timeformat(self) -> str:
        return self.__timeformat

    @timeformat.setter
    def timeformat(self, timeformat: str):
        self.__timeformat = timeformat

class IncludePropertiesAttribute:

    pass
class eTJ_TaskPrefix(IncludePropertiesAttribute):

    pass
class eTJ_ReportPrefix(IncludePropertiesAttribute):

    pass
class eTJ_ResourcePrefix(IncludePropertiesAttribute):

    pass
class eTJ_AccountPrefix(IncludePropertiesAttribute):

    pass
class eTJ_AccountAttribute:

    pass
class AccountAttribute:

    pass
class eTJ_Credit(AccountAttribute):

    def __init__(self, description: str, amount: float, eTJ_Credit: "eTJ_ISODATE" = None):
        self.description = description
        self.amount = amount
        self.eTJ_Credit = eTJ_Credit
        
    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def eTJ_Credit(self):
        return self.__eTJ_Credit

    @eTJ_Credit.setter
    def eTJ_Credit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Credit__eTJ_Credit", None)
        self.__eTJ_Credit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ISODATE"):
                opp_val = getattr(old_value, "eTJ_ISODATE", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ISODATE", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ISODATE"):
                opp_val = getattr(value, "eTJ_ISODATE", None)
                setattr(value, "eTJ_ISODATE", self)

class eTJ_Interval3:

    pass
class eTJ_LeaveDetails:

    def __init__(self, type: str, name: str, eTJ_LeaveDetails: "eTJ_Leaves" = None, eTJ_LeaveDetails5: "eTJ_Interval3" = None):
        self.type = type
        self.name = name
        self.eTJ_LeaveDetails = eTJ_LeaveDetails
        self.eTJ_LeaveDetails5 = eTJ_LeaveDetails5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def eTJ_LeaveDetails(self):
        return self.__eTJ_LeaveDetails

    @eTJ_LeaveDetails.setter
    def eTJ_LeaveDetails(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LeaveDetails__eTJ_LeaveDetails", None)
        self.__eTJ_LeaveDetails = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Leaves"):
                opp_val = getattr(old_value, "eTJ_Leaves", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Leaves"):
                opp_val = getattr(value, "eTJ_Leaves", None)
                if opp_val is None:
                    setattr(value, "eTJ_Leaves", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eTJ_LeaveDetails5(self):
        return self.__eTJ_LeaveDetails5

    @eTJ_LeaveDetails5.setter
    def eTJ_LeaveDetails5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_LeaveDetails__eTJ_LeaveDetails5", None)
        self.__eTJ_LeaveDetails5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Interval3"):
                opp_val = getattr(old_value, "eTJ_Interval3", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Interval3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Interval3"):
                opp_val = getattr(value, "eTJ_Interval3", None)
                setattr(value, "eTJ_Interval3", self)

class ResourceAttribute:

    pass
class eTJ_JournalEntry(ResourceAttribute, ProjectAttribute):

    def __init__(self, headline: str, eTJ_JournalEntry140: "eTJ_Details" = None, eTJ_JournalEntry: "eTJ_ISODATE" = None, eTJ_JournalEntry135: "eTJ_Alert" = None, eTJ_JournalEntry137: "eTJ_Author" = None, eTJ_JournalEntry142: "eTJ_Summary" = None):
        self.headline = headline
        self.eTJ_JournalEntry140 = eTJ_JournalEntry140
        self.eTJ_JournalEntry = eTJ_JournalEntry
        self.eTJ_JournalEntry135 = eTJ_JournalEntry135
        self.eTJ_JournalEntry137 = eTJ_JournalEntry137
        self.eTJ_JournalEntry142 = eTJ_JournalEntry142
        
    @property
    def headline(self) -> str:
        return self.__headline

    @headline.setter
    def headline(self, headline: str):
        self.__headline = headline

    @property
    def eTJ_JournalEntry140(self):
        return self.__eTJ_JournalEntry140

    @eTJ_JournalEntry140.setter
    def eTJ_JournalEntry140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_JournalEntry__eTJ_JournalEntry140", None)
        self.__eTJ_JournalEntry140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Details"):
                opp_val = getattr(old_value, "eTJ_Details", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Details", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Details"):
                opp_val = getattr(value, "eTJ_Details", None)
                setattr(value, "eTJ_Details", self)

    @property
    def eTJ_JournalEntry(self):
        return self.__eTJ_JournalEntry

    @eTJ_JournalEntry.setter
    def eTJ_JournalEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_JournalEntry__eTJ_JournalEntry", None)
        self.__eTJ_JournalEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ISODATE133"):
                opp_val = getattr(old_value, "eTJ_ISODATE133", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ISODATE133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ISODATE133"):
                opp_val = getattr(value, "eTJ_ISODATE133", None)
                setattr(value, "eTJ_ISODATE133", self)

    @property
    def eTJ_JournalEntry137(self):
        return self.__eTJ_JournalEntry137

    @eTJ_JournalEntry137.setter
    def eTJ_JournalEntry137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_JournalEntry__eTJ_JournalEntry137", None)
        self.__eTJ_JournalEntry137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Author138"):
                opp_val = getattr(old_value, "eTJ_Author138", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Author138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Author138"):
                opp_val = getattr(value, "eTJ_Author138", None)
                setattr(value, "eTJ_Author138", self)

    @property
    def eTJ_JournalEntry142(self):
        return self.__eTJ_JournalEntry142

    @eTJ_JournalEntry142.setter
    def eTJ_JournalEntry142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_JournalEntry__eTJ_JournalEntry142", None)
        self.__eTJ_JournalEntry142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Summary"):
                opp_val = getattr(old_value, "eTJ_Summary", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Summary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Summary"):
                opp_val = getattr(value, "eTJ_Summary", None)
                setattr(value, "eTJ_Summary", self)

    @property
    def eTJ_JournalEntry135(self):
        return self.__eTJ_JournalEntry135

    @eTJ_JournalEntry135.setter
    def eTJ_JournalEntry135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_JournalEntry__eTJ_JournalEntry135", None)
        self.__eTJ_JournalEntry135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Alert"):
                opp_val = getattr(old_value, "eTJ_Alert", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Alert", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Alert"):
                opp_val = getattr(value, "eTJ_Alert", None)
                setattr(value, "eTJ_Alert", self)

class eTJ_Managers(ResourceAttribute):

    pass
class eTJ_BookingResource(ResourceAttribute):

    pass
class eTJ_Fail(ResourceAttribute):

    pass
class eTJ_WorkingHours(ResourceAttribute, ProjectAttribute):

    def __init__(self, off: bool, eTJ_WorkingHours: "eTJ_Shift" = None, eTJ_WorkingHours286: set["eTJ_Weekdays"] = None, eTJ_WorkingHours288: set["eTJ_WorkHours"] = None):
        self.off = off
        self.eTJ_WorkingHours = eTJ_WorkingHours
        self.eTJ_WorkingHours286 = eTJ_WorkingHours286 if eTJ_WorkingHours286 is not None else set()
        self.eTJ_WorkingHours288 = eTJ_WorkingHours288 if eTJ_WorkingHours288 is not None else set()
        
    @property
    def off(self) -> bool:
        return self.__off

    @off.setter
    def off(self, off: bool):
        self.__off = off

    @property
    def eTJ_WorkingHours288(self):
        return self.__eTJ_WorkingHours288

    @eTJ_WorkingHours288.setter
    def eTJ_WorkingHours288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_WorkingHours__eTJ_WorkingHours288", None)
        self.__eTJ_WorkingHours288 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_WorkHours"):
                    opp_val = getattr(item, "eTJ_WorkHours", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_WorkHours", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_WorkHours"):
                    opp_val = getattr(item, "eTJ_WorkHours", None)
                    
                    setattr(item, "eTJ_WorkHours", self)
                    

    @property
    def eTJ_WorkingHours286(self):
        return self.__eTJ_WorkingHours286

    @eTJ_WorkingHours286.setter
    def eTJ_WorkingHours286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_WorkingHours__eTJ_WorkingHours286", None)
        self.__eTJ_WorkingHours286 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_Weekdays"):
                    opp_val = getattr(item, "eTJ_Weekdays", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_Weekdays", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_Weekdays"):
                    opp_val = getattr(item, "eTJ_Weekdays", None)
                    
                    setattr(item, "eTJ_Weekdays", self)
                    

    @property
    def eTJ_WorkingHours(self):
        return self.__eTJ_WorkingHours

    @eTJ_WorkingHours.setter
    def eTJ_WorkingHours(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_WorkingHours__eTJ_WorkingHours", None)
        self.__eTJ_WorkingHours = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Shift197"):
                opp_val = getattr(old_value, "eTJ_Shift197", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Shift197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Shift197"):
                opp_val = getattr(value, "eTJ_Shift197", None)
                setattr(value, "eTJ_Shift197", self)

class eTJ_ShiftsResource(ResourceAttribute):

    pass
class eTJ_PurgeResource(ResourceAttribute):

    def __init__(self, listAttribute: str):
        self.listAttribute = listAttribute
        
    @property
    def listAttribute(self) -> str:
        return self.__listAttribute

    @listAttribute.setter
    def listAttribute(self, listAttribute: str):
        self.__listAttribute = listAttribute

class eTJ_ExtendedResourceAttribute(ResourceAttribute):

    def __init__(self, value: str, eTJ_ExtendedResourceAttribute: "eTJ_Extend" = None):
        self.value = value
        self.eTJ_ExtendedResourceAttribute = eTJ_ExtendedResourceAttribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def eTJ_ExtendedResourceAttribute(self):
        return self.__eTJ_ExtendedResourceAttribute

    @eTJ_ExtendedResourceAttribute.setter
    def eTJ_ExtendedResourceAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_ExtendedResourceAttribute__eTJ_ExtendedResourceAttribute", None)
        self.__eTJ_ExtendedResourceAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Extend70"):
                opp_val = getattr(old_value, "eTJ_Extend70", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Extend70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Extend70"):
                opp_val = getattr(value, "eTJ_Extend70", None)
                setattr(value, "eTJ_Extend70", self)

class eTJ_Warn(ResourceAttribute):

    pass
class eTJ_Efficiency(ResourceAttribute):

    def __init__(self, efficiency: float):
        self.efficiency = efficiency
        
    @property
    def efficiency(self) -> float:
        return self.__efficiency

    @efficiency.setter
    def efficiency(self, efficiency: float):
        self.__efficiency = efficiency

class eTJ_Email(ResourceAttribute):

    def __init__(self, address: str):
        self.address = address
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

class Property:

    pass
class eTJ_Copyright(Property):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class eTJ_Rate(ResourceAttribute, Property):

    def __init__(self, rate: float):
        self.rate = rate
        
    @property
    def rate(self) -> float:
        return self.__rate

    @rate.setter
    def rate(self, rate: float):
        self.__rate = rate

class eTJ_CellColor(Property, ColumnAttribute):

    pass
class eTJ_ProjectIds(Property):

    def __init__(self, ids: str):
        self.ids = ids
        
    @property
    def ids(self) -> str:
        return self.__ids

    @ids.setter
    def ids(self, ids: str):
        self.__ids = ids

class eTJ_Vacation(ResourceAttribute, Property):

    def __init__(self, name: str, eTJ_Vacation: "eTJ_Shift" = None, eTJ_Vacation281: set["eTJ_Interval3"] = None):
        self.name = name
        self.eTJ_Vacation = eTJ_Vacation
        self.eTJ_Vacation281 = eTJ_Vacation281 if eTJ_Vacation281 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eTJ_Vacation(self):
        return self.__eTJ_Vacation

    @eTJ_Vacation.setter
    def eTJ_Vacation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Vacation__eTJ_Vacation", None)
        self.__eTJ_Vacation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Shift"):
                opp_val = getattr(old_value, "eTJ_Shift", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Shift", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Shift"):
                opp_val = getattr(value, "eTJ_Shift", None)
                setattr(value, "eTJ_Shift", self)

    @property
    def eTJ_Vacation281(self):
        return self.__eTJ_Vacation281

    @eTJ_Vacation281.setter
    def eTJ_Vacation281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Vacation__eTJ_Vacation281", None)
        self.__eTJ_Vacation281 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_Interval3282"):
                    opp_val = getattr(item, "eTJ_Interval3282", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_Interval3282", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_Interval3282"):
                    opp_val = getattr(item, "eTJ_Interval3282", None)
                    
                    setattr(item, "eTJ_Interval3282", self)
                    

class eTJ_ToolTip(Property, ColumnAttribute):

    def __init__(self, tip: str, eTJ_ToolTip: "eTJ_LogicalExpression" = None):
        self.tip = tip
        self.eTJ_ToolTip = eTJ_ToolTip
        
    @property
    def tip(self) -> str:
        return self.__tip

    @tip.setter
    def tip(self, tip: str):
        self.__tip = tip

    @property
    def eTJ_ToolTip(self):
        return self.__eTJ_ToolTip

    @eTJ_ToolTip.setter
    def eTJ_ToolTip(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_ToolTip__eTJ_ToolTip", None)
        self.__eTJ_ToolTip = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_LogicalExpression277"):
                opp_val = getattr(old_value, "eTJ_LogicalExpression277", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_LogicalExpression277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_LogicalExpression277"):
                opp_val = getattr(value, "eTJ_LogicalExpression277", None)
                setattr(value, "eTJ_LogicalExpression277", self)

class eTJ_Allocate(Property):

    pass
class eTJ_IncludeProperties(Property):

    def __init__(self, importURI: str, eTJ_IncludeProperties: set["eTJ_IncludePropertiesAttribute"] = None):
        self.importURI = importURI
        self.eTJ_IncludeProperties = eTJ_IncludeProperties if eTJ_IncludeProperties is not None else set()
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def eTJ_IncludeProperties(self):
        return self.__eTJ_IncludeProperties

    @eTJ_IncludeProperties.setter
    def eTJ_IncludeProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_IncludeProperties__eTJ_IncludeProperties", None)
        self.__eTJ_IncludeProperties = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_IncludePropertiesAttribute"):
                    opp_val = getattr(item, "eTJ_IncludePropertiesAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_IncludePropertiesAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_IncludePropertiesAttribute"):
                    opp_val = getattr(item, "eTJ_IncludePropertiesAttribute", None)
                    
                    setattr(item, "eTJ_IncludePropertiesAttribute", self)
                    

class eTJ_SupplementResource(Property, ResourceAttribute):

    pass
class eTJ_Flags(Property, ResourceAttribute, StatusStatusSheetAttribute, AccountAttribute, StatusTimesheetAttribute, ReportAttribute):

    def __init__(self, flags: str):
        self.flags = flags
        
    @property
    def flags(self) -> str:
        return self.__flags

    @flags.setter
    def flags(self, flags: str):
        self.__flags = flags

class eTJ_Task(Property):

    def __init__(self, id: str, name: str, eTJ_Task: set["eTJ_TaskAttribute"] = None, eTJ_Task50: "eTJ_BookingResource" = None, eTJ_Task84: "eTJ_Function" = None, eTJ_Task241: "eTJ_SupplementTask" = None, eTJ_Task257: "eTJ_TaskStatusSheet" = None, eTJ_Task261: "eTJ_TaskTimesheet" = None, eTJ_Task265: "eTJ_TaskPrefix" = None, eTJ_Task267: "eTJ_TaskRoot" = None, eTJ_Task320: "eTJ_TaskDependency" = None):
        self.id = id
        self.name = name
        self.eTJ_Task = eTJ_Task if eTJ_Task is not None else set()
        self.eTJ_Task50 = eTJ_Task50
        self.eTJ_Task84 = eTJ_Task84
        self.eTJ_Task241 = eTJ_Task241
        self.eTJ_Task257 = eTJ_Task257
        self.eTJ_Task261 = eTJ_Task261
        self.eTJ_Task265 = eTJ_Task265
        self.eTJ_Task267 = eTJ_Task267
        self.eTJ_Task320 = eTJ_Task320
        
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
    def eTJ_Task267(self):
        return self.__eTJ_Task267

    @eTJ_Task267.setter
    def eTJ_Task267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Task__eTJ_Task267", None)
        self.__eTJ_Task267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_TaskRoot"):
                opp_val = getattr(old_value, "eTJ_TaskRoot", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_TaskRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_TaskRoot"):
                opp_val = getattr(value, "eTJ_TaskRoot", None)
                setattr(value, "eTJ_TaskRoot", self)

    @property
    def eTJ_Task(self):
        return self.__eTJ_Task

    @eTJ_Task.setter
    def eTJ_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Task__eTJ_Task", None)
        self.__eTJ_Task = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_TaskAttribute"):
                    opp_val = getattr(item, "eTJ_TaskAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_TaskAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_TaskAttribute"):
                    opp_val = getattr(item, "eTJ_TaskAttribute", None)
                    
                    setattr(item, "eTJ_TaskAttribute", self)
                    

    @property
    def eTJ_Task261(self):
        return self.__eTJ_Task261

    @eTJ_Task261.setter
    def eTJ_Task261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Task__eTJ_Task261", None)
        self.__eTJ_Task261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_TaskTimesheet"):
                opp_val = getattr(old_value, "eTJ_TaskTimesheet", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_TaskTimesheet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_TaskTimesheet"):
                opp_val = getattr(value, "eTJ_TaskTimesheet", None)
                setattr(value, "eTJ_TaskTimesheet", self)

    @property
    def eTJ_Task241(self):
        return self.__eTJ_Task241

    @eTJ_Task241.setter
    def eTJ_Task241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Task__eTJ_Task241", None)
        self.__eTJ_Task241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_SupplementTask"):
                opp_val = getattr(old_value, "eTJ_SupplementTask", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_SupplementTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_SupplementTask"):
                opp_val = getattr(value, "eTJ_SupplementTask", None)
                setattr(value, "eTJ_SupplementTask", self)

    @property
    def eTJ_Task320(self):
        return self.__eTJ_Task320

    @eTJ_Task320.setter
    def eTJ_Task320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Task__eTJ_Task320", None)
        self.__eTJ_Task320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_TaskDependency319"):
                opp_val = getattr(old_value, "eTJ_TaskDependency319", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_TaskDependency319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_TaskDependency319"):
                opp_val = getattr(value, "eTJ_TaskDependency319", None)
                setattr(value, "eTJ_TaskDependency319", self)

    @property
    def eTJ_Task50(self):
        return self.__eTJ_Task50

    @eTJ_Task50.setter
    def eTJ_Task50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Task__eTJ_Task50", None)
        self.__eTJ_Task50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_BookingResource"):
                opp_val = getattr(old_value, "eTJ_BookingResource", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_BookingResource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_BookingResource"):
                opp_val = getattr(value, "eTJ_BookingResource", None)
                setattr(value, "eTJ_BookingResource", self)

    @property
    def eTJ_Task257(self):
        return self.__eTJ_Task257

    @eTJ_Task257.setter
    def eTJ_Task257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Task__eTJ_Task257", None)
        self.__eTJ_Task257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_TaskStatusSheet"):
                opp_val = getattr(old_value, "eTJ_TaskStatusSheet", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_TaskStatusSheet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_TaskStatusSheet"):
                opp_val = getattr(value, "eTJ_TaskStatusSheet", None)
                setattr(value, "eTJ_TaskStatusSheet", self)

    @property
    def eTJ_Task84(self):
        return self.__eTJ_Task84

    @eTJ_Task84.setter
    def eTJ_Task84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Task__eTJ_Task84", None)
        self.__eTJ_Task84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Function83"):
                opp_val = getattr(old_value, "eTJ_Function83", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Function83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Function83"):
                opp_val = getattr(value, "eTJ_Function83", None)
                setattr(value, "eTJ_Function83", self)

    @property
    def eTJ_Task265(self):
        return self.__eTJ_Task265

    @eTJ_Task265.setter
    def eTJ_Task265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Task__eTJ_Task265", None)
        self.__eTJ_Task265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_TaskPrefix"):
                opp_val = getattr(old_value, "eTJ_TaskPrefix", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_TaskPrefix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_TaskPrefix"):
                opp_val = getattr(value, "eTJ_TaskPrefix", None)
                setattr(value, "eTJ_TaskPrefix", self)

class eTJ_Account(Property, AccountAttribute):

    def __init__(self, id: str, name: str, eTJ_Account: set["eTJ_AccountAttribute"] = None, eTJ_Account8: "eTJ_AccountPrefix" = None, eTJ_Account10: "eTJ_AccountRoot" = None, eTJ_Account39: "eTJ_Balance" = None, eTJ_Account42: "eTJ_Balance" = None, eTJ_Account226: "eTJ_SupplementAccount" = None, eTJ_Account291: "eTJ_AccountShare" = None):
        self.id = id
        self.name = name
        self.eTJ_Account = eTJ_Account if eTJ_Account is not None else set()
        self.eTJ_Account8 = eTJ_Account8
        self.eTJ_Account10 = eTJ_Account10
        self.eTJ_Account39 = eTJ_Account39
        self.eTJ_Account42 = eTJ_Account42
        self.eTJ_Account226 = eTJ_Account226
        self.eTJ_Account291 = eTJ_Account291
        
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
    def eTJ_Account226(self):
        return self.__eTJ_Account226

    @eTJ_Account226.setter
    def eTJ_Account226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Account__eTJ_Account226", None)
        self.__eTJ_Account226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_SupplementAccount"):
                opp_val = getattr(old_value, "eTJ_SupplementAccount", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_SupplementAccount", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_SupplementAccount"):
                opp_val = getattr(value, "eTJ_SupplementAccount", None)
                setattr(value, "eTJ_SupplementAccount", self)

    @property
    def eTJ_Account42(self):
        return self.__eTJ_Account42

    @eTJ_Account42.setter
    def eTJ_Account42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Account__eTJ_Account42", None)
        self.__eTJ_Account42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Balance41"):
                opp_val = getattr(old_value, "eTJ_Balance41", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Balance41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Balance41"):
                opp_val = getattr(value, "eTJ_Balance41", None)
                setattr(value, "eTJ_Balance41", self)

    @property
    def eTJ_Account10(self):
        return self.__eTJ_Account10

    @eTJ_Account10.setter
    def eTJ_Account10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Account__eTJ_Account10", None)
        self.__eTJ_Account10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_AccountRoot"):
                opp_val = getattr(old_value, "eTJ_AccountRoot", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_AccountRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_AccountRoot"):
                opp_val = getattr(value, "eTJ_AccountRoot", None)
                setattr(value, "eTJ_AccountRoot", self)

    @property
    def eTJ_Account8(self):
        return self.__eTJ_Account8

    @eTJ_Account8.setter
    def eTJ_Account8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Account__eTJ_Account8", None)
        self.__eTJ_Account8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_AccountPrefix"):
                opp_val = getattr(old_value, "eTJ_AccountPrefix", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_AccountPrefix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_AccountPrefix"):
                opp_val = getattr(value, "eTJ_AccountPrefix", None)
                setattr(value, "eTJ_AccountPrefix", self)

    @property
    def eTJ_Account39(self):
        return self.__eTJ_Account39

    @eTJ_Account39.setter
    def eTJ_Account39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Account__eTJ_Account39", None)
        self.__eTJ_Account39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Balance"):
                opp_val = getattr(old_value, "eTJ_Balance", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Balance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Balance"):
                opp_val = getattr(value, "eTJ_Balance", None)
                setattr(value, "eTJ_Balance", self)

    @property
    def eTJ_Account(self):
        return self.__eTJ_Account

    @eTJ_Account.setter
    def eTJ_Account(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Account__eTJ_Account", None)
        self.__eTJ_Account = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_AccountAttribute"):
                    opp_val = getattr(item, "eTJ_AccountAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_AccountAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_AccountAttribute"):
                    opp_val = getattr(item, "eTJ_AccountAttribute", None)
                    
                    setattr(item, "eTJ_AccountAttribute", self)
                    

    @property
    def eTJ_Account291(self):
        return self.__eTJ_Account291

    @eTJ_Account291.setter
    def eTJ_Account291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Account__eTJ_Account291", None)
        self.__eTJ_Account291 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_AccountShare290"):
                opp_val = getattr(old_value, "eTJ_AccountShare290", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_AccountShare290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_AccountShare290"):
                opp_val = getattr(value, "eTJ_AccountShare290", None)
                setattr(value, "eTJ_AccountShare290", self)

class eTJ_TaskReport(Property, ReportAttribute):

    pass
class eTJ_AccountReport(Property, ReportAttribute):

    pass
class eTJ_TextReport(Property, ReportAttribute):

    pass
class eTJ_Balance(Property, ReportAttribute):

    pass
class eTJ_TagFile(Property):

    def __init__(self, id: str, filename: str, eTJ_TagFile254: "eTJ_RollupTask" = None, eTJ_TagFile: "eTJ_HideResource" = None, eTJ_TagFile248: "eTJ_HideTask" = None, eTJ_TagFile251: "eTJ_RollupResource" = None):
        self.id = id
        self.filename = filename
        self.eTJ_TagFile254 = eTJ_TagFile254
        self.eTJ_TagFile = eTJ_TagFile
        self.eTJ_TagFile248 = eTJ_TagFile248
        self.eTJ_TagFile251 = eTJ_TagFile251
        
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
    def eTJ_TagFile254(self):
        return self.__eTJ_TagFile254

    @eTJ_TagFile254.setter
    def eTJ_TagFile254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_TagFile__eTJ_TagFile254", None)
        self.__eTJ_TagFile254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_RollupTask255"):
                opp_val = getattr(old_value, "eTJ_RollupTask255", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_RollupTask255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_RollupTask255"):
                opp_val = getattr(value, "eTJ_RollupTask255", None)
                setattr(value, "eTJ_RollupTask255", self)

    @property
    def eTJ_TagFile251(self):
        return self.__eTJ_TagFile251

    @eTJ_TagFile251.setter
    def eTJ_TagFile251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_TagFile__eTJ_TagFile251", None)
        self.__eTJ_TagFile251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_RollupResource252"):
                opp_val = getattr(old_value, "eTJ_RollupResource252", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_RollupResource252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_RollupResource252"):
                opp_val = getattr(value, "eTJ_RollupResource252", None)
                setattr(value, "eTJ_RollupResource252", self)

    @property
    def eTJ_TagFile248(self):
        return self.__eTJ_TagFile248

    @eTJ_TagFile248.setter
    def eTJ_TagFile248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_TagFile__eTJ_TagFile248", None)
        self.__eTJ_TagFile248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_HideTask249"):
                opp_val = getattr(old_value, "eTJ_HideTask249", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_HideTask249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_HideTask249"):
                opp_val = getattr(value, "eTJ_HideTask249", None)
                setattr(value, "eTJ_HideTask249", self)

    @property
    def eTJ_TagFile(self):
        return self.__eTJ_TagFile

    @eTJ_TagFile.setter
    def eTJ_TagFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_TagFile__eTJ_TagFile", None)
        self.__eTJ_TagFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_HideResource246"):
                opp_val = getattr(old_value, "eTJ_HideResource246", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_HideResource246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_HideResource246"):
                opp_val = getattr(value, "eTJ_HideResource246", None)
                setattr(value, "eTJ_HideResource246", self)

class eTJ_SupplementTask(Property):

    pass
class eTJ_Shift(Property):

    def __init__(self, id: str, name: str, replace: str, timezone: str, eTJ_Shift203: "eTJ_ShiftsLimit" = None, eTJ_Shift: "eTJ_Vacation" = None, eTJ_Shift195: "eTJ_Shift" = None, eTJ_Shift193: "eTJ_Shift" = None, eTJ_Shift197: "eTJ_WorkingHours" = None, eTJ_Shift199: "eTJ_ShiftTimesheet" = None, eTJ_Shift208: "eTJ_ShiftsAllocate" = None):
        self.id = id
        self.name = name
        self.replace = replace
        self.timezone = timezone
        self.eTJ_Shift203 = eTJ_Shift203
        self.eTJ_Shift = eTJ_Shift
        self.eTJ_Shift195 = eTJ_Shift195
        self.eTJ_Shift193 = eTJ_Shift193
        self.eTJ_Shift197 = eTJ_Shift197
        self.eTJ_Shift199 = eTJ_Shift199
        self.eTJ_Shift208 = eTJ_Shift208
        
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
    def replace(self) -> str:
        return self.__replace

    @replace.setter
    def replace(self, replace: str):
        self.__replace = replace

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eTJ_Shift199(self):
        return self.__eTJ_Shift199

    @eTJ_Shift199.setter
    def eTJ_Shift199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Shift__eTJ_Shift199", None)
        self.__eTJ_Shift199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ShiftTimesheet"):
                opp_val = getattr(old_value, "eTJ_ShiftTimesheet", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ShiftTimesheet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ShiftTimesheet"):
                opp_val = getattr(value, "eTJ_ShiftTimesheet", None)
                setattr(value, "eTJ_ShiftTimesheet", self)

    @property
    def eTJ_Shift195(self):
        return self.__eTJ_Shift195

    @eTJ_Shift195.setter
    def eTJ_Shift195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Shift__eTJ_Shift195", None)
        self.__eTJ_Shift195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Shift193"):
                opp_val = getattr(old_value, "eTJ_Shift193", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Shift193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Shift193"):
                opp_val = getattr(value, "eTJ_Shift193", None)
                setattr(value, "eTJ_Shift193", self)

    @property
    def eTJ_Shift197(self):
        return self.__eTJ_Shift197

    @eTJ_Shift197.setter
    def eTJ_Shift197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Shift__eTJ_Shift197", None)
        self.__eTJ_Shift197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_WorkingHours"):
                opp_val = getattr(old_value, "eTJ_WorkingHours", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_WorkingHours", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_WorkingHours"):
                opp_val = getattr(value, "eTJ_WorkingHours", None)
                setattr(value, "eTJ_WorkingHours", self)

    @property
    def eTJ_Shift203(self):
        return self.__eTJ_Shift203

    @eTJ_Shift203.setter
    def eTJ_Shift203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Shift__eTJ_Shift203", None)
        self.__eTJ_Shift203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ShiftsLimit202"):
                opp_val = getattr(old_value, "eTJ_ShiftsLimit202", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ShiftsLimit202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ShiftsLimit202"):
                opp_val = getattr(value, "eTJ_ShiftsLimit202", None)
                setattr(value, "eTJ_ShiftsLimit202", self)

    @property
    def eTJ_Shift193(self):
        return self.__eTJ_Shift193

    @eTJ_Shift193.setter
    def eTJ_Shift193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Shift__eTJ_Shift193", None)
        self.__eTJ_Shift193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Shift195"):
                opp_val = getattr(old_value, "eTJ_Shift195", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Shift195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Shift195"):
                opp_val = getattr(value, "eTJ_Shift195", None)
                setattr(value, "eTJ_Shift195", self)

    @property
    def eTJ_Shift(self):
        return self.__eTJ_Shift

    @eTJ_Shift.setter
    def eTJ_Shift(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Shift__eTJ_Shift", None)
        self.__eTJ_Shift = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Vacation"):
                opp_val = getattr(old_value, "eTJ_Vacation", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Vacation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Vacation"):
                opp_val = getattr(value, "eTJ_Vacation", None)
                setattr(value, "eTJ_Vacation", self)

    @property
    def eTJ_Shift208(self):
        return self.__eTJ_Shift208

    @eTJ_Shift208.setter
    def eTJ_Shift208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Shift__eTJ_Shift208", None)
        self.__eTJ_Shift208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ShiftsAllocate"):
                opp_val = getattr(old_value, "eTJ_ShiftsAllocate", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ShiftsAllocate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ShiftsAllocate"):
                opp_val = getattr(value, "eTJ_ShiftsAllocate", None)
                setattr(value, "eTJ_ShiftsAllocate", self)

class eTJ_SupplementReport(Property):

    pass
class eTJ_StatusSheet(Property):

    pass
class eTJ_Limits(ResourceAttribute, Property):

    pass
class eTJ_TimesheetReport(Property):

    def __init__(self, filename: str, eTJ_TimesheetReport: set["eTJ_TimesheetReportAttribute"] = None):
        self.filename = filename
        self.eTJ_TimesheetReport = eTJ_TimesheetReport if eTJ_TimesheetReport is not None else set()
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def eTJ_TimesheetReport(self):
        return self.__eTJ_TimesheetReport

    @eTJ_TimesheetReport.setter
    def eTJ_TimesheetReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_TimesheetReport__eTJ_TimesheetReport", None)
        self.__eTJ_TimesheetReport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_TimesheetReportAttribute"):
                    opp_val = getattr(item, "eTJ_TimesheetReportAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_TimesheetReportAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_TimesheetReportAttribute"):
                    opp_val = getattr(item, "eTJ_TimesheetReportAttribute", None)
                    
                    setattr(item, "eTJ_TimesheetReportAttribute", self)
                    

class eTJ_ResourceReport(Property, ReportAttribute):

    pass
class eTJ_Timesheet(Property):

    pass
class eTJ_Macro(Property):

    def __init__(self, id: str, value: str, eTJ_Macro: "eTJ_MacroCall" = None, eTJ_Macro153: set["eTJ_Property"] = None):
        self.id = id
        self.value = value
        self.eTJ_Macro = eTJ_Macro
        self.eTJ_Macro153 = eTJ_Macro153 if eTJ_Macro153 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def eTJ_Macro(self):
        return self.__eTJ_Macro

    @eTJ_Macro.setter
    def eTJ_Macro(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Macro__eTJ_Macro", None)
        self.__eTJ_Macro = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_MacroCall"):
                opp_val = getattr(old_value, "eTJ_MacroCall", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_MacroCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_MacroCall"):
                opp_val = getattr(value, "eTJ_MacroCall", None)
                setattr(value, "eTJ_MacroCall", self)

    @property
    def eTJ_Macro153(self):
        return self.__eTJ_Macro153

    @eTJ_Macro153.setter
    def eTJ_Macro153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Macro__eTJ_Macro153", None)
        self.__eTJ_Macro153 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_Property154"):
                    opp_val = getattr(item, "eTJ_Property154", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_Property154", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_Property154"):
                    opp_val = getattr(item, "eTJ_Property154", None)
                    
                    setattr(item, "eTJ_Property154", self)
                    

class eTJ_NikuReport(Property):

    def __init__(self, filename: str, eTJ_NikuReport: set["eTJ_NikuReportAttribute"] = None):
        self.filename = filename
        self.eTJ_NikuReport = eTJ_NikuReport if eTJ_NikuReport is not None else set()
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def eTJ_NikuReport(self):
        return self.__eTJ_NikuReport

    @eTJ_NikuReport.setter
    def eTJ_NikuReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_NikuReport__eTJ_NikuReport", None)
        self.__eTJ_NikuReport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_NikuReportAttribute"):
                    opp_val = getattr(item, "eTJ_NikuReportAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_NikuReportAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_NikuReportAttribute"):
                    opp_val = getattr(item, "eTJ_NikuReportAttribute", None)
                    
                    setattr(item, "eTJ_NikuReportAttribute", self)
                    

class eTJ_SupplementAccount(Property):

    pass
class eTJ_Export(Property):

    def __init__(self, id: str, filename: str, eTJ_Export: set["eTJ_ExportAttribute"] = None):
        self.id = id
        self.filename = filename
        self.eTJ_Export = eTJ_Export if eTJ_Export is not None else set()
        
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
    def eTJ_Export(self):
        return self.__eTJ_Export

    @eTJ_Export.setter
    def eTJ_Export(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Export__eTJ_Export", None)
        self.__eTJ_Export = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_ExportAttribute"):
                    opp_val = getattr(item, "eTJ_ExportAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_ExportAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_ExportAttribute"):
                    opp_val = getattr(item, "eTJ_ExportAttribute", None)
                    
                    setattr(item, "eTJ_ExportAttribute", self)
                    

class eTJ_IcalReport(Property):

    def __init__(self, filename: str, eTJ_IcalReport: set["eTJ_IcalReportAttribute"] = None):
        self.filename = filename
        self.eTJ_IcalReport = eTJ_IcalReport if eTJ_IcalReport is not None else set()
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def eTJ_IcalReport(self):
        return self.__eTJ_IcalReport

    @eTJ_IcalReport.setter
    def eTJ_IcalReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_IcalReport__eTJ_IcalReport", None)
        self.__eTJ_IcalReport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_IcalReportAttribute"):
                    opp_val = getattr(item, "eTJ_IcalReportAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_IcalReportAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_IcalReportAttribute"):
                    opp_val = getattr(item, "eTJ_IcalReportAttribute", None)
                    
                    setattr(item, "eTJ_IcalReportAttribute", self)
                    

class eTJ_Resource(Property, ResourceAttribute):

    def __init__(self, id: str, name: str, eTJ_Resource: set["eTJ_ResourceAttribute"] = None, eTJ_Resource28: "eTJ_AllocateResource" = None, eTJ_Resource35: "eTJ_Alternative" = None, eTJ_Resource37: "eTJ_Author" = None, eTJ_Resource45: "eTJ_BookingTask" = None, eTJ_Resource87: "eTJ_Function" = None, eTJ_Resource156: "eTJ_Managers" = None, eTJ_Resource174: "eTJ_ResourcePrefix" = None, eTJ_Resource176: "eTJ_ResourceRoot" = None, eTJ_Resource178: "eTJ_Responsible" = None, eTJ_Resource218: "eTJ_StatusSheet" = None, eTJ_Resource236: "eTJ_SupplementResource" = None, eTJ_Resource269: "eTJ_Timesheet" = None, eTJ_Resource314: "eTJ_LimitAttribute" = None):
        self.id = id
        self.name = name
        self.eTJ_Resource = eTJ_Resource if eTJ_Resource is not None else set()
        self.eTJ_Resource28 = eTJ_Resource28
        self.eTJ_Resource35 = eTJ_Resource35
        self.eTJ_Resource37 = eTJ_Resource37
        self.eTJ_Resource45 = eTJ_Resource45
        self.eTJ_Resource87 = eTJ_Resource87
        self.eTJ_Resource156 = eTJ_Resource156
        self.eTJ_Resource174 = eTJ_Resource174
        self.eTJ_Resource176 = eTJ_Resource176
        self.eTJ_Resource178 = eTJ_Resource178
        self.eTJ_Resource218 = eTJ_Resource218
        self.eTJ_Resource236 = eTJ_Resource236
        self.eTJ_Resource269 = eTJ_Resource269
        self.eTJ_Resource314 = eTJ_Resource314
        
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
    def eTJ_Resource28(self):
        return self.__eTJ_Resource28

    @eTJ_Resource28.setter
    def eTJ_Resource28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Resource__eTJ_Resource28", None)
        self.__eTJ_Resource28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_AllocateResource27"):
                opp_val = getattr(old_value, "eTJ_AllocateResource27", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_AllocateResource27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_AllocateResource27"):
                opp_val = getattr(value, "eTJ_AllocateResource27", None)
                setattr(value, "eTJ_AllocateResource27", self)

    @property
    def eTJ_Resource314(self):
        return self.__eTJ_Resource314

    @eTJ_Resource314.setter
    def eTJ_Resource314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Resource__eTJ_Resource314", None)
        self.__eTJ_Resource314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_LimitAttribute313"):
                opp_val = getattr(old_value, "eTJ_LimitAttribute313", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_LimitAttribute313"):
                opp_val = getattr(value, "eTJ_LimitAttribute313", None)
                if opp_val is None:
                    setattr(value, "eTJ_LimitAttribute313", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eTJ_Resource236(self):
        return self.__eTJ_Resource236

    @eTJ_Resource236.setter
    def eTJ_Resource236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Resource__eTJ_Resource236", None)
        self.__eTJ_Resource236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_SupplementResource"):
                opp_val = getattr(old_value, "eTJ_SupplementResource", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_SupplementResource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_SupplementResource"):
                opp_val = getattr(value, "eTJ_SupplementResource", None)
                setattr(value, "eTJ_SupplementResource", self)

    @property
    def eTJ_Resource269(self):
        return self.__eTJ_Resource269

    @eTJ_Resource269.setter
    def eTJ_Resource269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Resource__eTJ_Resource269", None)
        self.__eTJ_Resource269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Timesheet"):
                opp_val = getattr(old_value, "eTJ_Timesheet", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Timesheet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Timesheet"):
                opp_val = getattr(value, "eTJ_Timesheet", None)
                setattr(value, "eTJ_Timesheet", self)

    @property
    def eTJ_Resource156(self):
        return self.__eTJ_Resource156

    @eTJ_Resource156.setter
    def eTJ_Resource156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Resource__eTJ_Resource156", None)
        self.__eTJ_Resource156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Managers"):
                opp_val = getattr(old_value, "eTJ_Managers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Managers"):
                opp_val = getattr(value, "eTJ_Managers", None)
                if opp_val is None:
                    setattr(value, "eTJ_Managers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eTJ_Resource35(self):
        return self.__eTJ_Resource35

    @eTJ_Resource35.setter
    def eTJ_Resource35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Resource__eTJ_Resource35", None)
        self.__eTJ_Resource35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Alternative"):
                opp_val = getattr(old_value, "eTJ_Alternative", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Alternative"):
                opp_val = getattr(value, "eTJ_Alternative", None)
                if opp_val is None:
                    setattr(value, "eTJ_Alternative", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eTJ_Resource37(self):
        return self.__eTJ_Resource37

    @eTJ_Resource37.setter
    def eTJ_Resource37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Resource__eTJ_Resource37", None)
        self.__eTJ_Resource37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Author"):
                opp_val = getattr(old_value, "eTJ_Author", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Author", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Author"):
                opp_val = getattr(value, "eTJ_Author", None)
                setattr(value, "eTJ_Author", self)

    @property
    def eTJ_Resource218(self):
        return self.__eTJ_Resource218

    @eTJ_Resource218.setter
    def eTJ_Resource218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Resource__eTJ_Resource218", None)
        self.__eTJ_Resource218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_StatusSheet"):
                opp_val = getattr(old_value, "eTJ_StatusSheet", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_StatusSheet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_StatusSheet"):
                opp_val = getattr(value, "eTJ_StatusSheet", None)
                setattr(value, "eTJ_StatusSheet", self)

    @property
    def eTJ_Resource176(self):
        return self.__eTJ_Resource176

    @eTJ_Resource176.setter
    def eTJ_Resource176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Resource__eTJ_Resource176", None)
        self.__eTJ_Resource176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ResourceRoot"):
                opp_val = getattr(old_value, "eTJ_ResourceRoot", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ResourceRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ResourceRoot"):
                opp_val = getattr(value, "eTJ_ResourceRoot", None)
                setattr(value, "eTJ_ResourceRoot", self)

    @property
    def eTJ_Resource45(self):
        return self.__eTJ_Resource45

    @eTJ_Resource45.setter
    def eTJ_Resource45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Resource__eTJ_Resource45", None)
        self.__eTJ_Resource45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_BookingTask"):
                opp_val = getattr(old_value, "eTJ_BookingTask", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_BookingTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_BookingTask"):
                opp_val = getattr(value, "eTJ_BookingTask", None)
                setattr(value, "eTJ_BookingTask", self)

    @property
    def eTJ_Resource178(self):
        return self.__eTJ_Resource178

    @eTJ_Resource178.setter
    def eTJ_Resource178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Resource__eTJ_Resource178", None)
        self.__eTJ_Resource178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Responsible"):
                opp_val = getattr(old_value, "eTJ_Responsible", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Responsible"):
                opp_val = getattr(value, "eTJ_Responsible", None)
                if opp_val is None:
                    setattr(value, "eTJ_Responsible", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eTJ_Resource(self):
        return self.__eTJ_Resource

    @eTJ_Resource.setter
    def eTJ_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Resource__eTJ_Resource", None)
        self.__eTJ_Resource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_ResourceAttribute"):
                    opp_val = getattr(item, "eTJ_ResourceAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_ResourceAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_ResourceAttribute"):
                    opp_val = getattr(item, "eTJ_ResourceAttribute", None)
                    
                    setattr(item, "eTJ_ResourceAttribute", self)
                    

    @property
    def eTJ_Resource87(self):
        return self.__eTJ_Resource87

    @eTJ_Resource87.setter
    def eTJ_Resource87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Resource__eTJ_Resource87", None)
        self.__eTJ_Resource87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Function86"):
                opp_val = getattr(old_value, "eTJ_Function86", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Function86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Function86"):
                opp_val = getattr(value, "eTJ_Function86", None)
                setattr(value, "eTJ_Function86", self)

    @property
    def eTJ_Resource174(self):
        return self.__eTJ_Resource174

    @eTJ_Resource174.setter
    def eTJ_Resource174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Resource__eTJ_Resource174", None)
        self.__eTJ_Resource174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_ResourcePrefix"):
                opp_val = getattr(old_value, "eTJ_ResourcePrefix", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_ResourcePrefix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_ResourcePrefix"):
                opp_val = getattr(value, "eTJ_ResourcePrefix", None)
                setattr(value, "eTJ_ResourcePrefix", self)

class eTJ_Navigator(Property):

    def __init__(self, id: str, eTJ_Navigator: set["eTJ_NavigatorAttribute"] = None):
        self.id = id
        self.eTJ_Navigator = eTJ_Navigator if eTJ_Navigator is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def eTJ_Navigator(self):
        return self.__eTJ_Navigator

    @eTJ_Navigator.setter
    def eTJ_Navigator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Navigator__eTJ_Navigator", None)
        self.__eTJ_Navigator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_NavigatorAttribute"):
                    opp_val = getattr(item, "eTJ_NavigatorAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_NavigatorAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_NavigatorAttribute"):
                    opp_val = getattr(item, "eTJ_NavigatorAttribute", None)
                    
                    setattr(item, "eTJ_NavigatorAttribute", self)
                    

class eTJ_StatusSheetReport(Property):

    def __init__(self, filename: str, eTJ_StatusSheetReport: set["eTJ_StatusSheetReportAttribute"] = None):
        self.filename = filename
        self.eTJ_StatusSheetReport = eTJ_StatusSheetReport if eTJ_StatusSheetReport is not None else set()
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def eTJ_StatusSheetReport(self):
        return self.__eTJ_StatusSheetReport

    @eTJ_StatusSheetReport.setter
    def eTJ_StatusSheetReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_StatusSheetReport__eTJ_StatusSheetReport", None)
        self.__eTJ_StatusSheetReport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_StatusSheetReportAttribute"):
                    opp_val = getattr(item, "eTJ_StatusSheetReportAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_StatusSheetReportAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_StatusSheetReportAttribute"):
                    opp_val = getattr(item, "eTJ_StatusSheetReportAttribute", None)
                    
                    setattr(item, "eTJ_StatusSheetReportAttribute", self)
                    

class eTJ_Leaves(Property, ResourceAttribute):

    pass
class eTJ_Property:

    pass
class eTJ_Project:

    def __init__(self, id: str, name: str, version: str, eTJ_Project: "eTJ_Global" = None, eTJ_Project12: "eTJ_Interval2" = None, eTJ_Project14: set["eTJ_ProjectAttribute"] = None):
        self.id = id
        self.name = name
        self.version = version
        self.eTJ_Project = eTJ_Project
        self.eTJ_Project12 = eTJ_Project12
        self.eTJ_Project14 = eTJ_Project14 if eTJ_Project14 is not None else set()
        
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
    def eTJ_Project14(self):
        return self.__eTJ_Project14

    @eTJ_Project14.setter
    def eTJ_Project14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Project__eTJ_Project14", None)
        self.__eTJ_Project14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eTJ_ProjectAttribute"):
                    opp_val = getattr(item, "eTJ_ProjectAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eTJ_ProjectAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eTJ_ProjectAttribute"):
                    opp_val = getattr(item, "eTJ_ProjectAttribute", None)
                    
                    setattr(item, "eTJ_ProjectAttribute", self)
                    

    @property
    def eTJ_Project(self):
        return self.__eTJ_Project

    @eTJ_Project.setter
    def eTJ_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Project__eTJ_Project", None)
        self.__eTJ_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Global"):
                opp_val = getattr(old_value, "eTJ_Global", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Global", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Global"):
                opp_val = getattr(value, "eTJ_Global", None)
                setattr(value, "eTJ_Global", self)

    @property
    def eTJ_Project12(self):
        return self.__eTJ_Project12

    @eTJ_Project12.setter
    def eTJ_Project12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eTJ_Project__eTJ_Project12", None)
        self.__eTJ_Project12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTJ_Interval2"):
                opp_val = getattr(old_value, "eTJ_Interval2", None)
                if opp_val == self:
                    setattr(old_value, "eTJ_Interval2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTJ_Interval2"):
                opp_val = getattr(value, "eTJ_Interval2", None)
                setattr(value, "eTJ_Interval2", self)

class eTJ_Global:

    pass