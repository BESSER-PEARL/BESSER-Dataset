import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    GapDuration,
    project_LimitAttribute,
    WeeklyMin,
    project_ColumnAttribute,
    project_WorkHours,
    project_Weekdays,
    project_TreeLevel,
    project_TimesheetReportAttribute,
    project_TimesheetAttribute,
    StatusSheetAttribute,
    project_TaskTimesheetAttribute,
    project_TaskStatusSheetAttribute,
    project_StatusSheetReportAttribute,
    project_StatusSheetAttribute,
    project_StatusTimesheetAttribute,
    project_Criterion,
    SortTasks,
    SortResources,
    SortJournalEntries,
    SortAccounts,
    project_Sort,
    project_StatusStatusSheetAttribute,
    TaskStatusSheetAttribute,
    project_TaskStatusSheet,
    project_StatusStatusSheet,
    project_ShiftsLimit,
    ShiftsTask,
    ShiftsResource,
    project_Shifts,
    project_JvmIdentifiableElement,
    LogicalExpression,
    project_LogicalDateLiteral,
    project_LogicalStringLiteral,
    project_LogicalBooleanLiteral,
    project_LogicalNumeralLiteral,
    project_LogicalFunctionExpression,
    project_LogicalAbsoluteIdExression,
    project_XBinaryOperation,
    Definitions,
    project_Defintions,
    Header,
    Footer,
    Epilog,
    Details,
    Center,
    Caption,
    Summary,
    Right,
    Prolog,
    ListItem,
    Left,
    Headline,
    project_RichText,
    Precedes,
    Depends,
    project_TaskDependency,
    NumberFormat,
    CurrencyFormat,
    project_RealFormat,
    WeeklyMax,
    MonthlyMin,
    MonthlyMax,
    Minimum,
    Maximum,
    DailyMin,
    DailyMax,
    project_Limit,
    GapLength,
    project_LimitsAttribute,
    project_Interval3,
    project_Interval1,
    project_IncludePropertiesAttribute,
    project_Function,
    NavigatorAttribute,
    project_HideReport,
    project_GapLength,
    project_GapDuration,
    project_Extend,
    ExportAttribute,
    project_ResourceAttributes,
    project_TaskAttributes,
    project_Definitions,
    LimitsAttribute,
    project_DailyMin,
    project_WeeklyMax,
    project_Minimum,
    project_Maximum,
    project_MonthlyMin,
    project_MonthlyMax,
    project_WeeklyMin,
    project_DailyMax,
    ProjectAttribute,
    project_TrackingScenario,
    project_TimingResolution,
    project_DailyWorkingHours,
    project_WeekStarts,
    project_Scenario,
    project_ExtendResource,
    project_ExtendTask,
    project_ShortTimeFormat,
    project_YearlyWorkingDays,
    project_Include,
    project_Now,
    project_Currency,
    TimesheetReportAttribute,
    TaskTimesheetAttribute,
    StatusSheetReportAttribute,
    NikuReportAttribute,
    project_Timeoff,
    NewTaskAttribute,
    project_Work,
    project_Remaining,
    IcalReportAttribute,
    project_ScenarioIcal,
    project_DurationQuantity,
    StatusTimesheetAttribute,
    project_RGB,
    project_LogicalExpression,
    ColumnAttribute,
    project_CellText,
    project_Width,
    project_FontColor,
    project_ToolTip,
    project_ListType,
    project_ListItem,
    project_HAlign,
    project_Scale,
    project_CellColor,
    project_Column,
    project_AccountShare,
    StatusStatusSheetAttribute,
    project_Summary,
    project_Details,
    project_Author,
    AllocateResourceAttribute,
    project_ShiftsAllocate,
    project_Mandatory,
    project_Select,
    project_Persistent,
    project_Alternative,
    project_Alert,
    project_NikuReportAttribute,
    project_Interval4,
    project_Booking,
    project_AllocateResourceAttribute,
    project_AllocateResource,
    project_NewTaskAttribute,
    TimesheetAttribute,
    project_ShiftTimesheet,
    project_TaskTimesheet,
    project_StatusTimesheet,
    project_NewTask,
    project_NavigatorAttribute,
    project_ReportAttribute,
    project_ResourceAttribute,
    ResourceAttribute,
    project_Email,
    project_ShiftsResource,
    project_WorkingHours,
    project_ExtendedResourceAttribute,
    project_PurgeResource,
    project_Managers,
    project_Efficiency,
    project_BookingResource,
    project_ExportAttribute,
    project_IcalReportAttribute,
    ReportAttribute,
    project_HideTask,
    project_Formats,
    project_Left,
    project_HideAccount,
    project_SortJournalEntries,
    project_Title,
    project_Right,
    project_Prolog,
    project_SelfContained,
    project_RollupAccount,
    project_AccountRoot,
    project_Epilog,
    project_RollupResource,
    project_HideJournalEntry,
    project_HideResource,
    project_Headline,
    project_Footer,
    project_Timezone,
    project_TaskRoot,
    project_SortResources,
    project_NumberFormat,
    project_PurgeReport,
    project_Scenarios,
    project_CurrencyFormat,
    project_TimeFormat,
    project_SortAccounts,
    project_JournalAttributes,
    project_Center,
    project_ResourceRoot,
    project_RollupTask,
    project_LoadUnit,
    project_Columns,
    project_Caption,
    project_Header,
    project_JournalMode,
    project_SortTasks,
    TextReport,
    TaskReport,
    ResourceReport,
    AccountReport,
    project_Report,
    project_TaskAttribute,
    TaskAttribute,
    project_Note,
    project_ShiftsTask,
    project_Period,
    project_Priority,
    project_Warn,
    project_Charge,
    project_Scheduled,
    project_Start,
    project_End,
    project_MinEnd,
    project_Allocate,
    project_Length,
    project_MinStart,
    project_Duration,
    project_Complete,
    project_EndCredit,
    project_Effort,
    project_JournalEntry,
    project_PurgeTask,
    project_BookingTask,
    project_ChargeSet,
    project_MaxEnd,
    project_Milestone,
    project_Scheduling,
    project_Precedes,
    project_Depends,
    project_Fail,
    project_ProjectId,
    project_ExtendedTaskAttribute,
    project_MaxStart,
    project_Responsible,
    project_ProjectAttribute,
    project_Interval2,
    project_Global,
    IncludePropertiesAttribute,
    project_TaskPrefix,
    project_ReportPrefix,
    project_ResourcePrefix,
    project_AccountPrefix,
    project_AccountAttribute,
    AccountAttribute,
    project_Credit,
    Property,
    project_AccountReport,
    project_SupplementAccount,
    project_StatusSheet,
    project_Flags,
    project_Navigator,
    project_TimesheetReport,
    project_StatusSheetReport,
    project_Vacation,
    project_Rate,
    project_Macro,
    project_NikuReport,
    project_TextReport,
    project_Resource,
    project_Limits,
    project_IcalReport,
    project_Export,
    project_Timesheet,
    project_SupplementReport,
    project_SupplementResource,
    project_Copyright,
    project_Shift,
    project_IncludeProperties,
    project_Task,
    project_ProjectIds,
    project_ResourceReport,
    project_TaskReport,
    project_SupplementTask,
    project_Balance,
    project_TagFile,
    project_Account,
    project_Property,
    project_Project,
    CriterionDirection,
    ColumnId,
    Weekday,
    LoadDisplayUnit,
    SelectArgument,
    TimeUnit,
    ListTypeValues,
    YesNo,
    Justification,
    PurgeResourceAttribute,
    ScaleResolution,
    ReportFormat,
    SchedulingPolicy,
    WorkQuantityUnit,
    JournalEntrySortCriterion,
    AlertLevel,
    PurgeReportAttribute,
    ChargeApplies,
    PurgeTaskAttribute,
    JournalModeValue,
    DependsPolicy,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gapduration_is_not_abstract():
    assert not inspect.isabstract(GapDuration)


def test_gapduration_constructor_exists():
    assert callable(GapDuration.__init__)


def test_gapduration_constructor_args():
    sig = inspect.signature(GapDuration.__init__)
    params = list(sig.parameters.keys())



def test_project_limitattribute_is_not_abstract():
    assert not inspect.isabstract(project_LimitAttribute)


def test_project_limitattribute_constructor_exists():
    assert callable(project_LimitAttribute.__init__)


def test_project_limitattribute_constructor_args():
    sig = inspect.signature(project_LimitAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"

def test_project_limitattribute_has_end():
    assert hasattr(project_LimitAttribute, "end")
    descriptor = None
    for klass in project_LimitAttribute.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_project_limitattribute_has_start():
    assert hasattr(project_LimitAttribute, "start")
    descriptor = None
    for klass in project_LimitAttribute.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_weeklymin_is_not_abstract():
    assert not inspect.isabstract(WeeklyMin)


def test_weeklymin_constructor_exists():
    assert callable(WeeklyMin.__init__)


def test_weeklymin_constructor_args():
    sig = inspect.signature(WeeklyMin.__init__)
    params = list(sig.parameters.keys())



def test_project_columnattribute_is_not_abstract():
    assert not inspect.isabstract(project_ColumnAttribute)


def test_project_columnattribute_constructor_exists():
    assert callable(project_ColumnAttribute.__init__)


def test_project_columnattribute_constructor_args():
    sig = inspect.signature(project_ColumnAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_workhours_is_not_abstract():
    assert not inspect.isabstract(project_WorkHours)


def test_project_workhours_constructor_exists():
    assert callable(project_WorkHours.__init__)


def test_project_workhours_constructor_args():
    sig = inspect.signature(project_WorkHours.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "stop" in params, "Missing parameter 'stop'"

def test_project_workhours_has_start():
    assert hasattr(project_WorkHours, "start")
    descriptor = None
    for klass in project_WorkHours.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_project_workhours_has_stop():
    assert hasattr(project_WorkHours, "stop")
    descriptor = None
    for klass in project_WorkHours.__mro__:
        if "stop" in klass.__dict__:
            descriptor = klass.__dict__["stop"]
            break
    assert isinstance(descriptor, property)



def test_project_weekdays_is_not_abstract():
    assert not inspect.isabstract(project_Weekdays)


def test_project_weekdays_constructor_exists():
    assert callable(project_Weekdays.__init__)


def test_project_weekdays_constructor_args():
    sig = inspect.signature(project_Weekdays.__init__)
    params = list(sig.parameters.keys())
    assert "first" in params, "Missing parameter 'first'"
    assert "last" in params, "Missing parameter 'last'"

def test_project_weekdays_has_first():
    assert hasattr(project_Weekdays, "first")
    descriptor = None
    for klass in project_Weekdays.__mro__:
        if "first" in klass.__dict__:
            descriptor = klass.__dict__["first"]
            break
    assert isinstance(descriptor, property)

def test_project_weekdays_has_last():
    assert hasattr(project_Weekdays, "last")
    descriptor = None
    for klass in project_Weekdays.__mro__:
        if "last" in klass.__dict__:
            descriptor = klass.__dict__["last"]
            break
    assert isinstance(descriptor, property)



def test_project_treelevel_is_not_abstract():
    assert not inspect.isabstract(project_TreeLevel)


def test_project_treelevel_constructor_exists():
    assert callable(project_TreeLevel.__init__)


def test_project_treelevel_constructor_args():
    sig = inspect.signature(project_TreeLevel.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_project_treelevel_has_level():
    assert hasattr(project_TreeLevel, "level")
    descriptor = None
    for klass in project_TreeLevel.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_project_timesheetreportattribute_is_not_abstract():
    assert not inspect.isabstract(project_TimesheetReportAttribute)


def test_project_timesheetreportattribute_constructor_exists():
    assert callable(project_TimesheetReportAttribute.__init__)


def test_project_timesheetreportattribute_constructor_args():
    sig = inspect.signature(project_TimesheetReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_timesheetattribute_is_not_abstract():
    assert not inspect.isabstract(project_TimesheetAttribute)


def test_project_timesheetattribute_constructor_exists():
    assert callable(project_TimesheetAttribute.__init__)


def test_project_timesheetattribute_constructor_args():
    sig = inspect.signature(project_TimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_statussheetattribute_is_not_abstract():
    assert not inspect.isabstract(StatusSheetAttribute)


def test_statussheetattribute_constructor_exists():
    assert callable(StatusSheetAttribute.__init__)


def test_statussheetattribute_constructor_args():
    sig = inspect.signature(StatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_tasktimesheetattribute_is_not_abstract():
    assert not inspect.isabstract(project_TaskTimesheetAttribute)


def test_project_tasktimesheetattribute_constructor_exists():
    assert callable(project_TaskTimesheetAttribute.__init__)


def test_project_tasktimesheetattribute_constructor_args():
    sig = inspect.signature(project_TaskTimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_taskstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(project_TaskStatusSheetAttribute)


def test_project_taskstatussheetattribute_constructor_exists():
    assert callable(project_TaskStatusSheetAttribute.__init__)


def test_project_taskstatussheetattribute_constructor_args():
    sig = inspect.signature(project_TaskStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_statussheetreportattribute_is_not_abstract():
    assert not inspect.isabstract(project_StatusSheetReportAttribute)


def test_project_statussheetreportattribute_constructor_exists():
    assert callable(project_StatusSheetReportAttribute.__init__)


def test_project_statussheetreportattribute_constructor_args():
    sig = inspect.signature(project_StatusSheetReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_statussheetattribute_is_not_abstract():
    assert not inspect.isabstract(project_StatusSheetAttribute)


def test_project_statussheetattribute_constructor_exists():
    assert callable(project_StatusSheetAttribute.__init__)


def test_project_statussheetattribute_constructor_args():
    sig = inspect.signature(project_StatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_statustimesheetattribute_is_not_abstract():
    assert not inspect.isabstract(project_StatusTimesheetAttribute)


def test_project_statustimesheetattribute_constructor_exists():
    assert callable(project_StatusTimesheetAttribute.__init__)


def test_project_statustimesheetattribute_constructor_args():
    sig = inspect.signature(project_StatusTimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_criterion_is_not_abstract():
    assert not inspect.isabstract(project_Criterion)


def test_project_criterion_constructor_exists():
    assert callable(project_Criterion.__init__)


def test_project_criterion_constructor_args():
    sig = inspect.signature(project_Criterion.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "columnId" in params, "Missing parameter 'columnId'"

def test_project_criterion_has_direction():
    assert hasattr(project_Criterion, "direction")
    descriptor = None
    for klass in project_Criterion.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_project_criterion_has_columnId():
    assert hasattr(project_Criterion, "columnId")
    descriptor = None
    for klass in project_Criterion.__mro__:
        if "columnId" in klass.__dict__:
            descriptor = klass.__dict__["columnId"]
            break
    assert isinstance(descriptor, property)



def test_sorttasks_is_not_abstract():
    assert not inspect.isabstract(SortTasks)


def test_sorttasks_constructor_exists():
    assert callable(SortTasks.__init__)


def test_sorttasks_constructor_args():
    sig = inspect.signature(SortTasks.__init__)
    params = list(sig.parameters.keys())



def test_sortresources_is_not_abstract():
    assert not inspect.isabstract(SortResources)


def test_sortresources_constructor_exists():
    assert callable(SortResources.__init__)


def test_sortresources_constructor_args():
    sig = inspect.signature(SortResources.__init__)
    params = list(sig.parameters.keys())



def test_sortjournalentries_is_not_abstract():
    assert not inspect.isabstract(SortJournalEntries)


def test_sortjournalentries_constructor_exists():
    assert callable(SortJournalEntries.__init__)


def test_sortjournalentries_constructor_args():
    sig = inspect.signature(SortJournalEntries.__init__)
    params = list(sig.parameters.keys())



def test_sortaccounts_is_not_abstract():
    assert not inspect.isabstract(SortAccounts)


def test_sortaccounts_constructor_exists():
    assert callable(SortAccounts.__init__)


def test_sortaccounts_constructor_args():
    sig = inspect.signature(SortAccounts.__init__)
    params = list(sig.parameters.keys())



def test_project_sort_is_not_abstract():
    assert not inspect.isabstract(project_Sort)


def test_project_sort_constructor_exists():
    assert callable(project_Sort.__init__)


def test_project_sort_constructor_args():
    sig = inspect.signature(project_Sort.__init__)
    params = list(sig.parameters.keys())
    assert "tree" in params, "Missing parameter 'tree'"

def test_project_sort_has_tree():
    assert hasattr(project_Sort, "tree")
    descriptor = None
    for klass in project_Sort.__mro__:
        if "tree" in klass.__dict__:
            descriptor = klass.__dict__["tree"]
            break
    assert isinstance(descriptor, property)



def test_project_statusstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(project_StatusStatusSheetAttribute)


def test_project_statusstatussheetattribute_constructor_exists():
    assert callable(project_StatusStatusSheetAttribute.__init__)


def test_project_statusstatussheetattribute_constructor_args():
    sig = inspect.signature(project_StatusStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_taskstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(TaskStatusSheetAttribute)


def test_taskstatussheetattribute_constructor_exists():
    assert callable(TaskStatusSheetAttribute.__init__)


def test_taskstatussheetattribute_constructor_args():
    sig = inspect.signature(TaskStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_taskstatussheet_is_not_abstract():
    assert not inspect.isabstract(project_TaskStatusSheet)


def test_project_taskstatussheet_constructor_exists():
    assert callable(project_TaskStatusSheet.__init__)


def test_project_taskstatussheet_constructor_args():
    sig = inspect.signature(project_TaskStatusSheet.__init__)
    params = list(sig.parameters.keys())



def test_project_statusstatussheet_is_not_abstract():
    assert not inspect.isabstract(project_StatusStatusSheet)


def test_project_statusstatussheet_constructor_exists():
    assert callable(project_StatusStatusSheet.__init__)


def test_project_statusstatussheet_constructor_args():
    sig = inspect.signature(project_StatusStatusSheet.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "text" in params, "Missing parameter 'text'"

def test_project_statusstatussheet_has_level():
    assert hasattr(project_StatusStatusSheet, "level")
    descriptor = None
    for klass in project_StatusStatusSheet.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_project_statusstatussheet_has_text():
    assert hasattr(project_StatusStatusSheet, "text")
    descriptor = None
    for klass in project_StatusStatusSheet.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_project_shiftslimit_is_not_abstract():
    assert not inspect.isabstract(project_ShiftsLimit)


def test_project_shiftslimit_constructor_exists():
    assert callable(project_ShiftsLimit.__init__)


def test_project_shiftslimit_constructor_args():
    sig = inspect.signature(project_ShiftsLimit.__init__)
    params = list(sig.parameters.keys())



def test_shiftstask_is_not_abstract():
    assert not inspect.isabstract(ShiftsTask)


def test_shiftstask_constructor_exists():
    assert callable(ShiftsTask.__init__)


def test_shiftstask_constructor_args():
    sig = inspect.signature(ShiftsTask.__init__)
    params = list(sig.parameters.keys())



def test_shiftsresource_is_not_abstract():
    assert not inspect.isabstract(ShiftsResource)


def test_shiftsresource_constructor_exists():
    assert callable(ShiftsResource.__init__)


def test_shiftsresource_constructor_args():
    sig = inspect.signature(ShiftsResource.__init__)
    params = list(sig.parameters.keys())



def test_project_shifts_is_not_abstract():
    assert not inspect.isabstract(project_Shifts)


def test_project_shifts_constructor_exists():
    assert callable(project_Shifts.__init__)


def test_project_shifts_constructor_args():
    sig = inspect.signature(project_Shifts.__init__)
    params = list(sig.parameters.keys())



def test_project_jvmidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(project_JvmIdentifiableElement)


def test_project_jvmidentifiableelement_constructor_exists():
    assert callable(project_JvmIdentifiableElement.__init__)


def test_project_jvmidentifiableelement_constructor_args():
    sig = inspect.signature(project_JvmIdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(LogicalExpression)


def test_logicalexpression_constructor_exists():
    assert callable(LogicalExpression.__init__)


def test_logicalexpression_constructor_args():
    sig = inspect.signature(LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_project_logicaldateliteral_is_not_abstract():
    assert not inspect.isabstract(project_LogicalDateLiteral)


def test_project_logicaldateliteral_constructor_exists():
    assert callable(project_LogicalDateLiteral.__init__)


def test_project_logicaldateliteral_constructor_args():
    sig = inspect.signature(project_LogicalDateLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project_logicaldateliteral_has_value():
    assert hasattr(project_LogicalDateLiteral, "value")
    descriptor = None
    for klass in project_LogicalDateLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project_logicalstringliteral_is_not_abstract():
    assert not inspect.isabstract(project_LogicalStringLiteral)


def test_project_logicalstringliteral_constructor_exists():
    assert callable(project_LogicalStringLiteral.__init__)


def test_project_logicalstringliteral_constructor_args():
    sig = inspect.signature(project_LogicalStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project_logicalstringliteral_has_value():
    assert hasattr(project_LogicalStringLiteral, "value")
    descriptor = None
    for klass in project_LogicalStringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project_logicalbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(project_LogicalBooleanLiteral)


def test_project_logicalbooleanliteral_constructor_exists():
    assert callable(project_LogicalBooleanLiteral.__init__)


def test_project_logicalbooleanliteral_constructor_args():
    sig = inspect.signature(project_LogicalBooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "isTrue" in params, "Missing parameter 'isTrue'"

def test_project_logicalbooleanliteral_has_isTrue():
    assert hasattr(project_LogicalBooleanLiteral, "isTrue")
    descriptor = None
    for klass in project_LogicalBooleanLiteral.__mro__:
        if "isTrue" in klass.__dict__:
            descriptor = klass.__dict__["isTrue"]
            break
    assert isinstance(descriptor, property)



def test_project_logicalnumeralliteral_is_not_abstract():
    assert not inspect.isabstract(project_LogicalNumeralLiteral)


def test_project_logicalnumeralliteral_constructor_exists():
    assert callable(project_LogicalNumeralLiteral.__init__)


def test_project_logicalnumeralliteral_constructor_args():
    sig = inspect.signature(project_LogicalNumeralLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project_logicalnumeralliteral_has_value():
    assert hasattr(project_LogicalNumeralLiteral, "value")
    descriptor = None
    for klass in project_LogicalNumeralLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project_logicalfunctionexpression_is_not_abstract():
    assert not inspect.isabstract(project_LogicalFunctionExpression)


def test_project_logicalfunctionexpression_constructor_exists():
    assert callable(project_LogicalFunctionExpression.__init__)


def test_project_logicalfunctionexpression_constructor_args():
    sig = inspect.signature(project_LogicalFunctionExpression.__init__)
    params = list(sig.parameters.keys())



def test_project_logicalabsoluteidexression_is_not_abstract():
    assert not inspect.isabstract(project_LogicalAbsoluteIdExression)


def test_project_logicalabsoluteidexression_constructor_exists():
    assert callable(project_LogicalAbsoluteIdExression.__init__)


def test_project_logicalabsoluteidexression_constructor_args():
    sig = inspect.signature(project_LogicalAbsoluteIdExression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project_logicalabsoluteidexression_has_value():
    assert hasattr(project_LogicalAbsoluteIdExression, "value")
    descriptor = None
    for klass in project_LogicalAbsoluteIdExression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project_xbinaryoperation_is_not_abstract():
    assert not inspect.isabstract(project_XBinaryOperation)


def test_project_xbinaryoperation_constructor_exists():
    assert callable(project_XBinaryOperation.__init__)


def test_project_xbinaryoperation_constructor_args():
    sig = inspect.signature(project_XBinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_definitions_is_not_abstract():
    assert not inspect.isabstract(Definitions)


def test_definitions_constructor_exists():
    assert callable(Definitions.__init__)


def test_definitions_constructor_args():
    sig = inspect.signature(Definitions.__init__)
    params = list(sig.parameters.keys())



def test_project_defintions_is_not_abstract():
    assert not inspect.isabstract(project_Defintions)


def test_project_defintions_constructor_exists():
    assert callable(project_Defintions.__init__)


def test_project_defintions_constructor_args():
    sig = inspect.signature(project_Defintions.__init__)
    params = list(sig.parameters.keys())
    assert "projectids" in params, "Missing parameter 'projectids'"
    assert "project" in params, "Missing parameter 'project'"
    assert "tasks" in params, "Missing parameter 'tasks'"
    assert "resources" in params, "Missing parameter 'resources'"
    assert "flags" in params, "Missing parameter 'flags'"

def test_project_defintions_has_projectids():
    assert hasattr(project_Defintions, "projectids")
    descriptor = None
    for klass in project_Defintions.__mro__:
        if "projectids" in klass.__dict__:
            descriptor = klass.__dict__["projectids"]
            break
    assert isinstance(descriptor, property)

def test_project_defintions_has_project():
    assert hasattr(project_Defintions, "project")
    descriptor = None
    for klass in project_Defintions.__mro__:
        if "project" in klass.__dict__:
            descriptor = klass.__dict__["project"]
            break
    assert isinstance(descriptor, property)

def test_project_defintions_has_tasks():
    assert hasattr(project_Defintions, "tasks")
    descriptor = None
    for klass in project_Defintions.__mro__:
        if "tasks" in klass.__dict__:
            descriptor = klass.__dict__["tasks"]
            break
    assert isinstance(descriptor, property)

def test_project_defintions_has_resources():
    assert hasattr(project_Defintions, "resources")
    descriptor = None
    for klass in project_Defintions.__mro__:
        if "resources" in klass.__dict__:
            descriptor = klass.__dict__["resources"]
            break
    assert isinstance(descriptor, property)

def test_project_defintions_has_flags():
    assert hasattr(project_Defintions, "flags")
    descriptor = None
    for klass in project_Defintions.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)



def test_header_is_not_abstract():
    assert not inspect.isabstract(Header)


def test_header_constructor_exists():
    assert callable(Header.__init__)


def test_header_constructor_args():
    sig = inspect.signature(Header.__init__)
    params = list(sig.parameters.keys())



def test_footer_is_not_abstract():
    assert not inspect.isabstract(Footer)


def test_footer_constructor_exists():
    assert callable(Footer.__init__)


def test_footer_constructor_args():
    sig = inspect.signature(Footer.__init__)
    params = list(sig.parameters.keys())



def test_epilog_is_not_abstract():
    assert not inspect.isabstract(Epilog)


def test_epilog_constructor_exists():
    assert callable(Epilog.__init__)


def test_epilog_constructor_args():
    sig = inspect.signature(Epilog.__init__)
    params = list(sig.parameters.keys())



def test_details_is_not_abstract():
    assert not inspect.isabstract(Details)


def test_details_constructor_exists():
    assert callable(Details.__init__)


def test_details_constructor_args():
    sig = inspect.signature(Details.__init__)
    params = list(sig.parameters.keys())



def test_center_is_not_abstract():
    assert not inspect.isabstract(Center)


def test_center_constructor_exists():
    assert callable(Center.__init__)


def test_center_constructor_args():
    sig = inspect.signature(Center.__init__)
    params = list(sig.parameters.keys())



def test_caption_is_not_abstract():
    assert not inspect.isabstract(Caption)


def test_caption_constructor_exists():
    assert callable(Caption.__init__)


def test_caption_constructor_args():
    sig = inspect.signature(Caption.__init__)
    params = list(sig.parameters.keys())



def test_summary_is_not_abstract():
    assert not inspect.isabstract(Summary)


def test_summary_constructor_exists():
    assert callable(Summary.__init__)


def test_summary_constructor_args():
    sig = inspect.signature(Summary.__init__)
    params = list(sig.parameters.keys())



def test_right_is_not_abstract():
    assert not inspect.isabstract(Right)


def test_right_constructor_exists():
    assert callable(Right.__init__)


def test_right_constructor_args():
    sig = inspect.signature(Right.__init__)
    params = list(sig.parameters.keys())



def test_prolog_is_not_abstract():
    assert not inspect.isabstract(Prolog)


def test_prolog_constructor_exists():
    assert callable(Prolog.__init__)


def test_prolog_constructor_args():
    sig = inspect.signature(Prolog.__init__)
    params = list(sig.parameters.keys())



def test_listitem_is_not_abstract():
    assert not inspect.isabstract(ListItem)


def test_listitem_constructor_exists():
    assert callable(ListItem.__init__)


def test_listitem_constructor_args():
    sig = inspect.signature(ListItem.__init__)
    params = list(sig.parameters.keys())



def test_left_is_not_abstract():
    assert not inspect.isabstract(Left)


def test_left_constructor_exists():
    assert callable(Left.__init__)


def test_left_constructor_args():
    sig = inspect.signature(Left.__init__)
    params = list(sig.parameters.keys())



def test_headline_is_not_abstract():
    assert not inspect.isabstract(Headline)


def test_headline_constructor_exists():
    assert callable(Headline.__init__)


def test_headline_constructor_args():
    sig = inspect.signature(Headline.__init__)
    params = list(sig.parameters.keys())



def test_project_richtext_is_not_abstract():
    assert not inspect.isabstract(project_RichText)


def test_project_richtext_constructor_exists():
    assert callable(project_RichText.__init__)


def test_project_richtext_constructor_args():
    sig = inspect.signature(project_RichText.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_project_richtext_has_text():
    assert hasattr(project_RichText, "text")
    descriptor = None
    for klass in project_RichText.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_precedes_is_not_abstract():
    assert not inspect.isabstract(Precedes)


def test_precedes_constructor_exists():
    assert callable(Precedes.__init__)


def test_precedes_constructor_args():
    sig = inspect.signature(Precedes.__init__)
    params = list(sig.parameters.keys())



def test_depends_is_not_abstract():
    assert not inspect.isabstract(Depends)


def test_depends_constructor_exists():
    assert callable(Depends.__init__)


def test_depends_constructor_args():
    sig = inspect.signature(Depends.__init__)
    params = list(sig.parameters.keys())



def test_project_taskdependency_is_not_abstract():
    assert not inspect.isabstract(project_TaskDependency)


def test_project_taskdependency_constructor_exists():
    assert callable(project_TaskDependency.__init__)


def test_project_taskdependency_constructor_args():
    sig = inspect.signature(project_TaskDependency.__init__)
    params = list(sig.parameters.keys())
    assert "policy" in params, "Missing parameter 'policy'"

def test_project_taskdependency_has_policy():
    assert hasattr(project_TaskDependency, "policy")
    descriptor = None
    for klass in project_TaskDependency.__mro__:
        if "policy" in klass.__dict__:
            descriptor = klass.__dict__["policy"]
            break
    assert isinstance(descriptor, property)



def test_numberformat_is_not_abstract():
    assert not inspect.isabstract(NumberFormat)


def test_numberformat_constructor_exists():
    assert callable(NumberFormat.__init__)


def test_numberformat_constructor_args():
    sig = inspect.signature(NumberFormat.__init__)
    params = list(sig.parameters.keys())



def test_currencyformat_is_not_abstract():
    assert not inspect.isabstract(CurrencyFormat)


def test_currencyformat_constructor_exists():
    assert callable(CurrencyFormat.__init__)


def test_currencyformat_constructor_args():
    sig = inspect.signature(CurrencyFormat.__init__)
    params = list(sig.parameters.keys())



def test_project_realformat_is_not_abstract():
    assert not inspect.isabstract(project_RealFormat)


def test_project_realformat_constructor_exists():
    assert callable(project_RealFormat.__init__)


def test_project_realformat_constructor_args():
    sig = inspect.signature(project_RealFormat.__init__)
    params = list(sig.parameters.keys())
    assert "fractionSeparator" in params, "Missing parameter 'fractionSeparator'"
    assert "negativePrefix" in params, "Missing parameter 'negativePrefix'"
    assert "thousandsSeparator" in params, "Missing parameter 'thousandsSeparator'"
    assert "negativeSuffix" in params, "Missing parameter 'negativeSuffix'"
    assert "fractionDigits" in params, "Missing parameter 'fractionDigits'"

def test_project_realformat_has_fractionSeparator():
    assert hasattr(project_RealFormat, "fractionSeparator")
    descriptor = None
    for klass in project_RealFormat.__mro__:
        if "fractionSeparator" in klass.__dict__:
            descriptor = klass.__dict__["fractionSeparator"]
            break
    assert isinstance(descriptor, property)

def test_project_realformat_has_negativePrefix():
    assert hasattr(project_RealFormat, "negativePrefix")
    descriptor = None
    for klass in project_RealFormat.__mro__:
        if "negativePrefix" in klass.__dict__:
            descriptor = klass.__dict__["negativePrefix"]
            break
    assert isinstance(descriptor, property)

def test_project_realformat_has_thousandsSeparator():
    assert hasattr(project_RealFormat, "thousandsSeparator")
    descriptor = None
    for klass in project_RealFormat.__mro__:
        if "thousandsSeparator" in klass.__dict__:
            descriptor = klass.__dict__["thousandsSeparator"]
            break
    assert isinstance(descriptor, property)

def test_project_realformat_has_negativeSuffix():
    assert hasattr(project_RealFormat, "negativeSuffix")
    descriptor = None
    for klass in project_RealFormat.__mro__:
        if "negativeSuffix" in klass.__dict__:
            descriptor = klass.__dict__["negativeSuffix"]
            break
    assert isinstance(descriptor, property)

def test_project_realformat_has_fractionDigits():
    assert hasattr(project_RealFormat, "fractionDigits")
    descriptor = None
    for klass in project_RealFormat.__mro__:
        if "fractionDigits" in klass.__dict__:
            descriptor = klass.__dict__["fractionDigits"]
            break
    assert isinstance(descriptor, property)



def test_weeklymax_is_not_abstract():
    assert not inspect.isabstract(WeeklyMax)


def test_weeklymax_constructor_exists():
    assert callable(WeeklyMax.__init__)


def test_weeklymax_constructor_args():
    sig = inspect.signature(WeeklyMax.__init__)
    params = list(sig.parameters.keys())



def test_monthlymin_is_not_abstract():
    assert not inspect.isabstract(MonthlyMin)


def test_monthlymin_constructor_exists():
    assert callable(MonthlyMin.__init__)


def test_monthlymin_constructor_args():
    sig = inspect.signature(MonthlyMin.__init__)
    params = list(sig.parameters.keys())



def test_monthlymax_is_not_abstract():
    assert not inspect.isabstract(MonthlyMax)


def test_monthlymax_constructor_exists():
    assert callable(MonthlyMax.__init__)


def test_monthlymax_constructor_args():
    sig = inspect.signature(MonthlyMax.__init__)
    params = list(sig.parameters.keys())



def test_minimum_is_not_abstract():
    assert not inspect.isabstract(Minimum)


def test_minimum_constructor_exists():
    assert callable(Minimum.__init__)


def test_minimum_constructor_args():
    sig = inspect.signature(Minimum.__init__)
    params = list(sig.parameters.keys())



def test_maximum_is_not_abstract():
    assert not inspect.isabstract(Maximum)


def test_maximum_constructor_exists():
    assert callable(Maximum.__init__)


def test_maximum_constructor_args():
    sig = inspect.signature(Maximum.__init__)
    params = list(sig.parameters.keys())



def test_dailymin_is_not_abstract():
    assert not inspect.isabstract(DailyMin)


def test_dailymin_constructor_exists():
    assert callable(DailyMin.__init__)


def test_dailymin_constructor_args():
    sig = inspect.signature(DailyMin.__init__)
    params = list(sig.parameters.keys())



def test_dailymax_is_not_abstract():
    assert not inspect.isabstract(DailyMax)


def test_dailymax_constructor_exists():
    assert callable(DailyMax.__init__)


def test_dailymax_constructor_args():
    sig = inspect.signature(DailyMax.__init__)
    params = list(sig.parameters.keys())



def test_project_limit_is_not_abstract():
    assert not inspect.isabstract(project_Limit)


def test_project_limit_constructor_exists():
    assert callable(project_Limit.__init__)


def test_project_limit_constructor_args():
    sig = inspect.signature(project_Limit.__init__)
    params = list(sig.parameters.keys())



def test_gaplength_is_not_abstract():
    assert not inspect.isabstract(GapLength)


def test_gaplength_constructor_exists():
    assert callable(GapLength.__init__)


def test_gaplength_constructor_args():
    sig = inspect.signature(GapLength.__init__)
    params = list(sig.parameters.keys())



def test_project_limitsattribute_is_not_abstract():
    assert not inspect.isabstract(project_LimitsAttribute)


def test_project_limitsattribute_constructor_exists():
    assert callable(project_LimitsAttribute.__init__)


def test_project_limitsattribute_constructor_args():
    sig = inspect.signature(project_LimitsAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_interval3_is_not_abstract():
    assert not inspect.isabstract(project_Interval3)


def test_project_interval3_constructor_exists():
    assert callable(project_Interval3.__init__)


def test_project_interval3_constructor_args():
    sig = inspect.signature(project_Interval3.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"

def test_project_interval3_has_end():
    assert hasattr(project_Interval3, "end")
    descriptor = None
    for klass in project_Interval3.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_project_interval3_has_start():
    assert hasattr(project_Interval3, "start")
    descriptor = None
    for klass in project_Interval3.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_project_interval1_is_not_abstract():
    assert not inspect.isabstract(project_Interval1)


def test_project_interval1_constructor_exists():
    assert callable(project_Interval1.__init__)


def test_project_interval1_constructor_args():
    sig = inspect.signature(project_Interval1.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"

def test_project_interval1_has_end():
    assert hasattr(project_Interval1, "end")
    descriptor = None
    for klass in project_Interval1.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_project_interval1_has_start():
    assert hasattr(project_Interval1, "start")
    descriptor = None
    for klass in project_Interval1.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_project_includepropertiesattribute_is_not_abstract():
    assert not inspect.isabstract(project_IncludePropertiesAttribute)


def test_project_includepropertiesattribute_constructor_exists():
    assert callable(project_IncludePropertiesAttribute.__init__)


def test_project_includepropertiesattribute_constructor_args():
    sig = inspect.signature(project_IncludePropertiesAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_function_is_not_abstract():
    assert not inspect.isabstract(project_Function)


def test_project_function_constructor_exists():
    assert callable(project_Function.__init__)


def test_project_function_constructor_args():
    sig = inspect.signature(project_Function.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"
    assert "level" in params, "Missing parameter 'level'"
    assert "parentId" in params, "Missing parameter 'parentId'"
    assert "date" in params, "Missing parameter 'date'"

def test_project_function_has_distance():
    assert hasattr(project_Function, "distance")
    descriptor = None
    for klass in project_Function.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_project_function_has_level():
    assert hasattr(project_Function, "level")
    descriptor = None
    for klass in project_Function.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_project_function_has_parentId():
    assert hasattr(project_Function, "parentId")
    descriptor = None
    for klass in project_Function.__mro__:
        if "parentId" in klass.__dict__:
            descriptor = klass.__dict__["parentId"]
            break
    assert isinstance(descriptor, property)

def test_project_function_has_date():
    assert hasattr(project_Function, "date")
    descriptor = None
    for klass in project_Function.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_navigatorattribute_is_not_abstract():
    assert not inspect.isabstract(NavigatorAttribute)


def test_navigatorattribute_constructor_exists():
    assert callable(NavigatorAttribute.__init__)


def test_navigatorattribute_constructor_args():
    sig = inspect.signature(NavigatorAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_hidereport_is_not_abstract():
    assert not inspect.isabstract(project_HideReport)


def test_project_hidereport_constructor_exists():
    assert callable(project_HideReport.__init__)


def test_project_hidereport_constructor_args():
    sig = inspect.signature(project_HideReport.__init__)
    params = list(sig.parameters.keys())



def test_project_gaplength_is_not_abstract():
    assert not inspect.isabstract(project_GapLength)


def test_project_gaplength_constructor_exists():
    assert callable(project_GapLength.__init__)


def test_project_gaplength_constructor_args():
    sig = inspect.signature(project_GapLength.__init__)
    params = list(sig.parameters.keys())



def test_project_gapduration_is_not_abstract():
    assert not inspect.isabstract(project_GapDuration)


def test_project_gapduration_constructor_exists():
    assert callable(project_GapDuration.__init__)


def test_project_gapduration_constructor_args():
    sig = inspect.signature(project_GapDuration.__init__)
    params = list(sig.parameters.keys())



def test_project_extend_is_not_abstract():
    assert not inspect.isabstract(project_Extend)


def test_project_extend_constructor_exists():
    assert callable(project_Extend.__init__)


def test_project_extend_constructor_args():
    sig = inspect.signature(project_Extend.__init__)
    params = list(sig.parameters.keys())
    assert "scenariospecific" in params, "Missing parameter 'scenariospecific'"
    assert "name" in params, "Missing parameter 'name'"
    assert "inherit" in params, "Missing parameter 'inherit'"
    assert "id" in params, "Missing parameter 'id'"

def test_project_extend_has_scenariospecific():
    assert hasattr(project_Extend, "scenariospecific")
    descriptor = None
    for klass in project_Extend.__mro__:
        if "scenariospecific" in klass.__dict__:
            descriptor = klass.__dict__["scenariospecific"]
            break
    assert isinstance(descriptor, property)

def test_project_extend_has_name():
    assert hasattr(project_Extend, "name")
    descriptor = None
    for klass in project_Extend.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project_extend_has_inherit():
    assert hasattr(project_Extend, "inherit")
    descriptor = None
    for klass in project_Extend.__mro__:
        if "inherit" in klass.__dict__:
            descriptor = klass.__dict__["inherit"]
            break
    assert isinstance(descriptor, property)

def test_project_extend_has_id():
    assert hasattr(project_Extend, "id")
    descriptor = None
    for klass in project_Extend.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_exportattribute_is_not_abstract():
    assert not inspect.isabstract(ExportAttribute)


def test_exportattribute_constructor_exists():
    assert callable(ExportAttribute.__init__)


def test_exportattribute_constructor_args():
    sig = inspect.signature(ExportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_resourceattributes_is_not_abstract():
    assert not inspect.isabstract(project_ResourceAttributes)


def test_project_resourceattributes_constructor_exists():
    assert callable(project_ResourceAttributes.__init__)


def test_project_resourceattributes_constructor_args():
    sig = inspect.signature(project_ResourceAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "none" in params, "Missing parameter 'none'"
    assert "vacation" in params, "Missing parameter 'vacation'"
    assert "workingHours" in params, "Missing parameter 'workingHours'"
    assert "all" in params, "Missing parameter 'all'"
    assert "booking" in params, "Missing parameter 'booking'"

def test_project_resourceattributes_has_none():
    assert hasattr(project_ResourceAttributes, "none")
    descriptor = None
    for klass in project_ResourceAttributes.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_project_resourceattributes_has_vacation():
    assert hasattr(project_ResourceAttributes, "vacation")
    descriptor = None
    for klass in project_ResourceAttributes.__mro__:
        if "vacation" in klass.__dict__:
            descriptor = klass.__dict__["vacation"]
            break
    assert isinstance(descriptor, property)

def test_project_resourceattributes_has_workingHours():
    assert hasattr(project_ResourceAttributes, "workingHours")
    descriptor = None
    for klass in project_ResourceAttributes.__mro__:
        if "workingHours" in klass.__dict__:
            descriptor = klass.__dict__["workingHours"]
            break
    assert isinstance(descriptor, property)

def test_project_resourceattributes_has_all():
    assert hasattr(project_ResourceAttributes, "all")
    descriptor = None
    for klass in project_ResourceAttributes.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_project_resourceattributes_has_booking():
    assert hasattr(project_ResourceAttributes, "booking")
    descriptor = None
    for klass in project_ResourceAttributes.__mro__:
        if "booking" in klass.__dict__:
            descriptor = klass.__dict__["booking"]
            break
    assert isinstance(descriptor, property)



def test_project_taskattributes_is_not_abstract():
    assert not inspect.isabstract(project_TaskAttributes)


def test_project_taskattributes_constructor_exists():
    assert callable(project_TaskAttributes.__init__)


def test_project_taskattributes_constructor_args():
    sig = inspect.signature(project_TaskAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "minstart" in params, "Missing parameter 'minstart'"
    assert "booking" in params, "Missing parameter 'booking'"
    assert "complete" in params, "Missing parameter 'complete'"
    assert "minend" in params, "Missing parameter 'minend'"
    assert "none" in params, "Missing parameter 'none'"
    assert "flags" in params, "Missing parameter 'flags'"
    assert "depends" in params, "Missing parameter 'depends'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "all" in params, "Missing parameter 'all'"
    assert "responsible" in params, "Missing parameter 'responsible'"
    assert "maxend" in params, "Missing parameter 'maxend'"
    assert "maxstart" in params, "Missing parameter 'maxstart'"
    assert "note" in params, "Missing parameter 'note'"

def test_project_taskattributes_has_minstart():
    assert hasattr(project_TaskAttributes, "minstart")
    descriptor = None
    for klass in project_TaskAttributes.__mro__:
        if "minstart" in klass.__dict__:
            descriptor = klass.__dict__["minstart"]
            break
    assert isinstance(descriptor, property)

def test_project_taskattributes_has_booking():
    assert hasattr(project_TaskAttributes, "booking")
    descriptor = None
    for klass in project_TaskAttributes.__mro__:
        if "booking" in klass.__dict__:
            descriptor = klass.__dict__["booking"]
            break
    assert isinstance(descriptor, property)

def test_project_taskattributes_has_complete():
    assert hasattr(project_TaskAttributes, "complete")
    descriptor = None
    for klass in project_TaskAttributes.__mro__:
        if "complete" in klass.__dict__:
            descriptor = klass.__dict__["complete"]
            break
    assert isinstance(descriptor, property)

def test_project_taskattributes_has_minend():
    assert hasattr(project_TaskAttributes, "minend")
    descriptor = None
    for klass in project_TaskAttributes.__mro__:
        if "minend" in klass.__dict__:
            descriptor = klass.__dict__["minend"]
            break
    assert isinstance(descriptor, property)

def test_project_taskattributes_has_none():
    assert hasattr(project_TaskAttributes, "none")
    descriptor = None
    for klass in project_TaskAttributes.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_project_taskattributes_has_flags():
    assert hasattr(project_TaskAttributes, "flags")
    descriptor = None
    for klass in project_TaskAttributes.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)

def test_project_taskattributes_has_depends():
    assert hasattr(project_TaskAttributes, "depends")
    descriptor = None
    for klass in project_TaskAttributes.__mro__:
        if "depends" in klass.__dict__:
            descriptor = klass.__dict__["depends"]
            break
    assert isinstance(descriptor, property)

def test_project_taskattributes_has_priority():
    assert hasattr(project_TaskAttributes, "priority")
    descriptor = None
    for klass in project_TaskAttributes.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_project_taskattributes_has_all():
    assert hasattr(project_TaskAttributes, "all")
    descriptor = None
    for klass in project_TaskAttributes.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_project_taskattributes_has_responsible():
    assert hasattr(project_TaskAttributes, "responsible")
    descriptor = None
    for klass in project_TaskAttributes.__mro__:
        if "responsible" in klass.__dict__:
            descriptor = klass.__dict__["responsible"]
            break
    assert isinstance(descriptor, property)

def test_project_taskattributes_has_maxend():
    assert hasattr(project_TaskAttributes, "maxend")
    descriptor = None
    for klass in project_TaskAttributes.__mro__:
        if "maxend" in klass.__dict__:
            descriptor = klass.__dict__["maxend"]
            break
    assert isinstance(descriptor, property)

def test_project_taskattributes_has_maxstart():
    assert hasattr(project_TaskAttributes, "maxstart")
    descriptor = None
    for klass in project_TaskAttributes.__mro__:
        if "maxstart" in klass.__dict__:
            descriptor = klass.__dict__["maxstart"]
            break
    assert isinstance(descriptor, property)

def test_project_taskattributes_has_note():
    assert hasattr(project_TaskAttributes, "note")
    descriptor = None
    for klass in project_TaskAttributes.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_project_definitions_is_not_abstract():
    assert not inspect.isabstract(project_Definitions)


def test_project_definitions_constructor_exists():
    assert callable(project_Definitions.__init__)


def test_project_definitions_constructor_args():
    sig = inspect.signature(project_Definitions.__init__)
    params = list(sig.parameters.keys())
    assert "none" in params, "Missing parameter 'none'"
    assert "all" in params, "Missing parameter 'all'"

def test_project_definitions_has_none():
    assert hasattr(project_Definitions, "none")
    descriptor = None
    for klass in project_Definitions.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_project_definitions_has_all():
    assert hasattr(project_Definitions, "all")
    descriptor = None
    for klass in project_Definitions.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_limitsattribute_is_not_abstract():
    assert not inspect.isabstract(LimitsAttribute)


def test_limitsattribute_constructor_exists():
    assert callable(LimitsAttribute.__init__)


def test_limitsattribute_constructor_args():
    sig = inspect.signature(LimitsAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_dailymin_is_not_abstract():
    assert not inspect.isabstract(project_DailyMin)


def test_project_dailymin_constructor_exists():
    assert callable(project_DailyMin.__init__)


def test_project_dailymin_constructor_args():
    sig = inspect.signature(project_DailyMin.__init__)
    params = list(sig.parameters.keys())



def test_project_weeklymax_is_not_abstract():
    assert not inspect.isabstract(project_WeeklyMax)


def test_project_weeklymax_constructor_exists():
    assert callable(project_WeeklyMax.__init__)


def test_project_weeklymax_constructor_args():
    sig = inspect.signature(project_WeeklyMax.__init__)
    params = list(sig.parameters.keys())



def test_project_minimum_is_not_abstract():
    assert not inspect.isabstract(project_Minimum)


def test_project_minimum_constructor_exists():
    assert callable(project_Minimum.__init__)


def test_project_minimum_constructor_args():
    sig = inspect.signature(project_Minimum.__init__)
    params = list(sig.parameters.keys())



def test_project_maximum_is_not_abstract():
    assert not inspect.isabstract(project_Maximum)


def test_project_maximum_constructor_exists():
    assert callable(project_Maximum.__init__)


def test_project_maximum_constructor_args():
    sig = inspect.signature(project_Maximum.__init__)
    params = list(sig.parameters.keys())



def test_project_monthlymin_is_not_abstract():
    assert not inspect.isabstract(project_MonthlyMin)


def test_project_monthlymin_constructor_exists():
    assert callable(project_MonthlyMin.__init__)


def test_project_monthlymin_constructor_args():
    sig = inspect.signature(project_MonthlyMin.__init__)
    params = list(sig.parameters.keys())



def test_project_monthlymax_is_not_abstract():
    assert not inspect.isabstract(project_MonthlyMax)


def test_project_monthlymax_constructor_exists():
    assert callable(project_MonthlyMax.__init__)


def test_project_monthlymax_constructor_args():
    sig = inspect.signature(project_MonthlyMax.__init__)
    params = list(sig.parameters.keys())



def test_project_weeklymin_is_not_abstract():
    assert not inspect.isabstract(project_WeeklyMin)


def test_project_weeklymin_constructor_exists():
    assert callable(project_WeeklyMin.__init__)


def test_project_weeklymin_constructor_args():
    sig = inspect.signature(project_WeeklyMin.__init__)
    params = list(sig.parameters.keys())



def test_project_dailymax_is_not_abstract():
    assert not inspect.isabstract(project_DailyMax)


def test_project_dailymax_constructor_exists():
    assert callable(project_DailyMax.__init__)


def test_project_dailymax_constructor_args():
    sig = inspect.signature(project_DailyMax.__init__)
    params = list(sig.parameters.keys())



def test_projectattribute_is_not_abstract():
    assert not inspect.isabstract(ProjectAttribute)


def test_projectattribute_constructor_exists():
    assert callable(ProjectAttribute.__init__)


def test_projectattribute_constructor_args():
    sig = inspect.signature(ProjectAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_trackingscenario_is_not_abstract():
    assert not inspect.isabstract(project_TrackingScenario)


def test_project_trackingscenario_constructor_exists():
    assert callable(project_TrackingScenario.__init__)


def test_project_trackingscenario_constructor_args():
    sig = inspect.signature(project_TrackingScenario.__init__)
    params = list(sig.parameters.keys())



def test_project_timingresolution_is_not_abstract():
    assert not inspect.isabstract(project_TimingResolution)


def test_project_timingresolution_constructor_exists():
    assert callable(project_TimingResolution.__init__)


def test_project_timingresolution_constructor_args():
    sig = inspect.signature(project_TimingResolution.__init__)
    params = list(sig.parameters.keys())
    assert "timingResolution" in params, "Missing parameter 'timingResolution'"

def test_project_timingresolution_has_timingResolution():
    assert hasattr(project_TimingResolution, "timingResolution")
    descriptor = None
    for klass in project_TimingResolution.__mro__:
        if "timingResolution" in klass.__dict__:
            descriptor = klass.__dict__["timingResolution"]
            break
    assert isinstance(descriptor, property)



def test_project_dailyworkinghours_is_not_abstract():
    assert not inspect.isabstract(project_DailyWorkingHours)


def test_project_dailyworkinghours_constructor_exists():
    assert callable(project_DailyWorkingHours.__init__)


def test_project_dailyworkinghours_constructor_args():
    sig = inspect.signature(project_DailyWorkingHours.__init__)
    params = list(sig.parameters.keys())
    assert "dailyWorkingHours" in params, "Missing parameter 'dailyWorkingHours'"

def test_project_dailyworkinghours_has_dailyWorkingHours():
    assert hasattr(project_DailyWorkingHours, "dailyWorkingHours")
    descriptor = None
    for klass in project_DailyWorkingHours.__mro__:
        if "dailyWorkingHours" in klass.__dict__:
            descriptor = klass.__dict__["dailyWorkingHours"]
            break
    assert isinstance(descriptor, property)



def test_project_weekstarts_is_not_abstract():
    assert not inspect.isabstract(project_WeekStarts)


def test_project_weekstarts_constructor_exists():
    assert callable(project_WeekStarts.__init__)


def test_project_weekstarts_constructor_args():
    sig = inspect.signature(project_WeekStarts.__init__)
    params = list(sig.parameters.keys())
    assert "monday" in params, "Missing parameter 'monday'"
    assert "sunday" in params, "Missing parameter 'sunday'"

def test_project_weekstarts_has_monday():
    assert hasattr(project_WeekStarts, "monday")
    descriptor = None
    for klass in project_WeekStarts.__mro__:
        if "monday" in klass.__dict__:
            descriptor = klass.__dict__["monday"]
            break
    assert isinstance(descriptor, property)

def test_project_weekstarts_has_sunday():
    assert hasattr(project_WeekStarts, "sunday")
    descriptor = None
    for klass in project_WeekStarts.__mro__:
        if "sunday" in klass.__dict__:
            descriptor = klass.__dict__["sunday"]
            break
    assert isinstance(descriptor, property)



def test_project_scenario_is_not_abstract():
    assert not inspect.isabstract(project_Scenario)


def test_project_scenario_constructor_exists():
    assert callable(project_Scenario.__init__)


def test_project_scenario_constructor_args():
    sig = inspect.signature(project_Scenario.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_project_scenario_has_active():
    assert hasattr(project_Scenario, "active")
    descriptor = None
    for klass in project_Scenario.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_project_scenario_has_name():
    assert hasattr(project_Scenario, "name")
    descriptor = None
    for klass in project_Scenario.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project_scenario_has_id():
    assert hasattr(project_Scenario, "id")
    descriptor = None
    for klass in project_Scenario.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_project_extendresource_is_not_abstract():
    assert not inspect.isabstract(project_ExtendResource)


def test_project_extendresource_constructor_exists():
    assert callable(project_ExtendResource.__init__)


def test_project_extendresource_constructor_args():
    sig = inspect.signature(project_ExtendResource.__init__)
    params = list(sig.parameters.keys())



def test_project_extendtask_is_not_abstract():
    assert not inspect.isabstract(project_ExtendTask)


def test_project_extendtask_constructor_exists():
    assert callable(project_ExtendTask.__init__)


def test_project_extendtask_constructor_args():
    sig = inspect.signature(project_ExtendTask.__init__)
    params = list(sig.parameters.keys())



def test_project_shorttimeformat_is_not_abstract():
    assert not inspect.isabstract(project_ShortTimeFormat)


def test_project_shorttimeformat_constructor_exists():
    assert callable(project_ShortTimeFormat.__init__)


def test_project_shorttimeformat_constructor_args():
    sig = inspect.signature(project_ShortTimeFormat.__init__)
    params = list(sig.parameters.keys())
    assert "shortTimeFormat" in params, "Missing parameter 'shortTimeFormat'"

def test_project_shorttimeformat_has_shortTimeFormat():
    assert hasattr(project_ShortTimeFormat, "shortTimeFormat")
    descriptor = None
    for klass in project_ShortTimeFormat.__mro__:
        if "shortTimeFormat" in klass.__dict__:
            descriptor = klass.__dict__["shortTimeFormat"]
            break
    assert isinstance(descriptor, property)



def test_project_yearlyworkingdays_is_not_abstract():
    assert not inspect.isabstract(project_YearlyWorkingDays)


def test_project_yearlyworkingdays_constructor_exists():
    assert callable(project_YearlyWorkingDays.__init__)


def test_project_yearlyworkingdays_constructor_args():
    sig = inspect.signature(project_YearlyWorkingDays.__init__)
    params = list(sig.parameters.keys())
    assert "yearlyWorkingDays" in params, "Missing parameter 'yearlyWorkingDays'"

def test_project_yearlyworkingdays_has_yearlyWorkingDays():
    assert hasattr(project_YearlyWorkingDays, "yearlyWorkingDays")
    descriptor = None
    for klass in project_YearlyWorkingDays.__mro__:
        if "yearlyWorkingDays" in klass.__dict__:
            descriptor = klass.__dict__["yearlyWorkingDays"]
            break
    assert isinstance(descriptor, property)



def test_project_include_is_not_abstract():
    assert not inspect.isabstract(project_Include)


def test_project_include_constructor_exists():
    assert callable(project_Include.__init__)


def test_project_include_constructor_args():
    sig = inspect.signature(project_Include.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_project_include_has_importURI():
    assert hasattr(project_Include, "importURI")
    descriptor = None
    for klass in project_Include.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_project_now_is_not_abstract():
    assert not inspect.isabstract(project_Now)


def test_project_now_constructor_exists():
    assert callable(project_Now.__init__)


def test_project_now_constructor_args():
    sig = inspect.signature(project_Now.__init__)
    params = list(sig.parameters.keys())
    assert "now" in params, "Missing parameter 'now'"

def test_project_now_has_now():
    assert hasattr(project_Now, "now")
    descriptor = None
    for klass in project_Now.__mro__:
        if "now" in klass.__dict__:
            descriptor = klass.__dict__["now"]
            break
    assert isinstance(descriptor, property)



def test_project_currency_is_not_abstract():
    assert not inspect.isabstract(project_Currency)


def test_project_currency_constructor_exists():
    assert callable(project_Currency.__init__)


def test_project_currency_constructor_args():
    sig = inspect.signature(project_Currency.__init__)
    params = list(sig.parameters.keys())
    assert "currency" in params, "Missing parameter 'currency'"

def test_project_currency_has_currency():
    assert hasattr(project_Currency, "currency")
    descriptor = None
    for klass in project_Currency.__mro__:
        if "currency" in klass.__dict__:
            descriptor = klass.__dict__["currency"]
            break
    assert isinstance(descriptor, property)



def test_timesheetreportattribute_is_not_abstract():
    assert not inspect.isabstract(TimesheetReportAttribute)


def test_timesheetreportattribute_constructor_exists():
    assert callable(TimesheetReportAttribute.__init__)


def test_timesheetreportattribute_constructor_args():
    sig = inspect.signature(TimesheetReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_tasktimesheetattribute_is_not_abstract():
    assert not inspect.isabstract(TaskTimesheetAttribute)


def test_tasktimesheetattribute_constructor_exists():
    assert callable(TaskTimesheetAttribute.__init__)


def test_tasktimesheetattribute_constructor_args():
    sig = inspect.signature(TaskTimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_statussheetreportattribute_is_not_abstract():
    assert not inspect.isabstract(StatusSheetReportAttribute)


def test_statussheetreportattribute_constructor_exists():
    assert callable(StatusSheetReportAttribute.__init__)


def test_statussheetreportattribute_constructor_args():
    sig = inspect.signature(StatusSheetReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_nikureportattribute_is_not_abstract():
    assert not inspect.isabstract(NikuReportAttribute)


def test_nikureportattribute_constructor_exists():
    assert callable(NikuReportAttribute.__init__)


def test_nikureportattribute_constructor_args():
    sig = inspect.signature(NikuReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_timeoff_is_not_abstract():
    assert not inspect.isabstract(project_Timeoff)


def test_project_timeoff_constructor_exists():
    assert callable(project_Timeoff.__init__)


def test_project_timeoff_constructor_args():
    sig = inspect.signature(project_Timeoff.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_project_timeoff_has_name():
    assert hasattr(project_Timeoff, "name")
    descriptor = None
    for klass in project_Timeoff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project_timeoff_has_id():
    assert hasattr(project_Timeoff, "id")
    descriptor = None
    for klass in project_Timeoff.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_newtaskattribute_is_not_abstract():
    assert not inspect.isabstract(NewTaskAttribute)


def test_newtaskattribute_constructor_exists():
    assert callable(NewTaskAttribute.__init__)


def test_newtaskattribute_constructor_args():
    sig = inspect.signature(NewTaskAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_work_is_not_abstract():
    assert not inspect.isabstract(project_Work)


def test_project_work_constructor_exists():
    assert callable(project_Work.__init__)


def test_project_work_constructor_args():
    sig = inspect.signature(project_Work.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_project_work_has_value():
    assert hasattr(project_Work, "value")
    descriptor = None
    for klass in project_Work.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_project_work_has_unit():
    assert hasattr(project_Work, "unit")
    descriptor = None
    for klass in project_Work.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_project_remaining_is_not_abstract():
    assert not inspect.isabstract(project_Remaining)


def test_project_remaining_constructor_exists():
    assert callable(project_Remaining.__init__)


def test_project_remaining_constructor_args():
    sig = inspect.signature(project_Remaining.__init__)
    params = list(sig.parameters.keys())



def test_icalreportattribute_is_not_abstract():
    assert not inspect.isabstract(IcalReportAttribute)


def test_icalreportattribute_constructor_exists():
    assert callable(IcalReportAttribute.__init__)


def test_icalreportattribute_constructor_args():
    sig = inspect.signature(IcalReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_scenarioical_is_not_abstract():
    assert not inspect.isabstract(project_ScenarioIcal)


def test_project_scenarioical_constructor_exists():
    assert callable(project_ScenarioIcal.__init__)


def test_project_scenarioical_constructor_args():
    sig = inspect.signature(project_ScenarioIcal.__init__)
    params = list(sig.parameters.keys())



def test_project_durationquantity_is_not_abstract():
    assert not inspect.isabstract(project_DurationQuantity)


def test_project_durationquantity_constructor_exists():
    assert callable(project_DurationQuantity.__init__)


def test_project_durationquantity_constructor_args():
    sig = inspect.signature(project_DurationQuantity.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "value" in params, "Missing parameter 'value'"

def test_project_durationquantity_has_unit():
    assert hasattr(project_DurationQuantity, "unit")
    descriptor = None
    for klass in project_DurationQuantity.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_project_durationquantity_has_value():
    assert hasattr(project_DurationQuantity, "value")
    descriptor = None
    for klass in project_DurationQuantity.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statustimesheetattribute_is_not_abstract():
    assert not inspect.isabstract(StatusTimesheetAttribute)


def test_statustimesheetattribute_constructor_exists():
    assert callable(StatusTimesheetAttribute.__init__)


def test_statustimesheetattribute_constructor_args():
    sig = inspect.signature(StatusTimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_rgb_is_not_abstract():
    assert not inspect.isabstract(project_RGB)


def test_project_rgb_constructor_exists():
    assert callable(project_RGB.__init__)


def test_project_rgb_constructor_args():
    sig = inspect.signature(project_RGB.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project_rgb_has_value():
    assert hasattr(project_RGB, "value")
    descriptor = None
    for klass in project_RGB.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(project_LogicalExpression)


def test_project_logicalexpression_constructor_exists():
    assert callable(project_LogicalExpression.__init__)


def test_project_logicalexpression_constructor_args():
    sig = inspect.signature(project_LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_columnattribute_is_not_abstract():
    assert not inspect.isabstract(ColumnAttribute)


def test_columnattribute_constructor_exists():
    assert callable(ColumnAttribute.__init__)


def test_columnattribute_constructor_args():
    sig = inspect.signature(ColumnAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_celltext_is_not_abstract():
    assert not inspect.isabstract(project_CellText)


def test_project_celltext_constructor_exists():
    assert callable(project_CellText.__init__)


def test_project_celltext_constructor_args():
    sig = inspect.signature(project_CellText.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_project_celltext_has_text():
    assert hasattr(project_CellText, "text")
    descriptor = None
    for klass in project_CellText.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_project_width_is_not_abstract():
    assert not inspect.isabstract(project_Width)


def test_project_width_constructor_exists():
    assert callable(project_Width.__init__)


def test_project_width_constructor_args():
    sig = inspect.signature(project_Width.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"

def test_project_width_has_width():
    assert hasattr(project_Width, "width")
    descriptor = None
    for klass in project_Width.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_project_fontcolor_is_not_abstract():
    assert not inspect.isabstract(project_FontColor)


def test_project_fontcolor_constructor_exists():
    assert callable(project_FontColor.__init__)


def test_project_fontcolor_constructor_args():
    sig = inspect.signature(project_FontColor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_project_fontcolor_has_color():
    assert hasattr(project_FontColor, "color")
    descriptor = None
    for klass in project_FontColor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_project_tooltip_is_not_abstract():
    assert not inspect.isabstract(project_ToolTip)


def test_project_tooltip_constructor_exists():
    assert callable(project_ToolTip.__init__)


def test_project_tooltip_constructor_args():
    sig = inspect.signature(project_ToolTip.__init__)
    params = list(sig.parameters.keys())
    assert "tip" in params, "Missing parameter 'tip'"

def test_project_tooltip_has_tip():
    assert hasattr(project_ToolTip, "tip")
    descriptor = None
    for klass in project_ToolTip.__mro__:
        if "tip" in klass.__dict__:
            descriptor = klass.__dict__["tip"]
            break
    assert isinstance(descriptor, property)



def test_project_listtype_is_not_abstract():
    assert not inspect.isabstract(project_ListType)


def test_project_listtype_constructor_exists():
    assert callable(project_ListType.__init__)


def test_project_listtype_constructor_args():
    sig = inspect.signature(project_ListType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_project_listtype_has_type():
    assert hasattr(project_ListType, "type")
    descriptor = None
    for klass in project_ListType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_project_listitem_is_not_abstract():
    assert not inspect.isabstract(project_ListItem)


def test_project_listitem_constructor_exists():
    assert callable(project_ListItem.__init__)


def test_project_listitem_constructor_args():
    sig = inspect.signature(project_ListItem.__init__)
    params = list(sig.parameters.keys())



def test_project_halign_is_not_abstract():
    assert not inspect.isabstract(project_HAlign)


def test_project_halign_constructor_exists():
    assert callable(project_HAlign.__init__)


def test_project_halign_constructor_args():
    sig = inspect.signature(project_HAlign.__init__)
    params = list(sig.parameters.keys())
    assert "justification" in params, "Missing parameter 'justification'"

def test_project_halign_has_justification():
    assert hasattr(project_HAlign, "justification")
    descriptor = None
    for klass in project_HAlign.__mro__:
        if "justification" in klass.__dict__:
            descriptor = klass.__dict__["justification"]
            break
    assert isinstance(descriptor, property)



def test_project_scale_is_not_abstract():
    assert not inspect.isabstract(project_Scale)


def test_project_scale_constructor_exists():
    assert callable(project_Scale.__init__)


def test_project_scale_constructor_args():
    sig = inspect.signature(project_Scale.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"

def test_project_scale_has_scale():
    assert hasattr(project_Scale, "scale")
    descriptor = None
    for klass in project_Scale.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_project_cellcolor_is_not_abstract():
    assert not inspect.isabstract(project_CellColor)


def test_project_cellcolor_constructor_exists():
    assert callable(project_CellColor.__init__)


def test_project_cellcolor_constructor_args():
    sig = inspect.signature(project_CellColor.__init__)
    params = list(sig.parameters.keys())



def test_project_column_is_not_abstract():
    assert not inspect.isabstract(project_Column)


def test_project_column_constructor_exists():
    assert callable(project_Column.__init__)


def test_project_column_constructor_args():
    sig = inspect.signature(project_Column.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_project_column_has_id():
    assert hasattr(project_Column, "id")
    descriptor = None
    for klass in project_Column.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_project_accountshare_is_not_abstract():
    assert not inspect.isabstract(project_AccountShare)


def test_project_accountshare_constructor_exists():
    assert callable(project_AccountShare.__init__)


def test_project_accountshare_constructor_args():
    sig = inspect.signature(project_AccountShare.__init__)
    params = list(sig.parameters.keys())
    assert "share" in params, "Missing parameter 'share'"

def test_project_accountshare_has_share():
    assert hasattr(project_AccountShare, "share")
    descriptor = None
    for klass in project_AccountShare.__mro__:
        if "share" in klass.__dict__:
            descriptor = klass.__dict__["share"]
            break
    assert isinstance(descriptor, property)



def test_statusstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(StatusStatusSheetAttribute)


def test_statusstatussheetattribute_constructor_exists():
    assert callable(StatusStatusSheetAttribute.__init__)


def test_statusstatussheetattribute_constructor_args():
    sig = inspect.signature(StatusStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_summary_is_not_abstract():
    assert not inspect.isabstract(project_Summary)


def test_project_summary_constructor_exists():
    assert callable(project_Summary.__init__)


def test_project_summary_constructor_args():
    sig = inspect.signature(project_Summary.__init__)
    params = list(sig.parameters.keys())



def test_project_details_is_not_abstract():
    assert not inspect.isabstract(project_Details)


def test_project_details_constructor_exists():
    assert callable(project_Details.__init__)


def test_project_details_constructor_args():
    sig = inspect.signature(project_Details.__init__)
    params = list(sig.parameters.keys())



def test_project_author_is_not_abstract():
    assert not inspect.isabstract(project_Author)


def test_project_author_constructor_exists():
    assert callable(project_Author.__init__)


def test_project_author_constructor_args():
    sig = inspect.signature(project_Author.__init__)
    params = list(sig.parameters.keys())



def test_allocateresourceattribute_is_not_abstract():
    assert not inspect.isabstract(AllocateResourceAttribute)


def test_allocateresourceattribute_constructor_exists():
    assert callable(AllocateResourceAttribute.__init__)


def test_allocateresourceattribute_constructor_args():
    sig = inspect.signature(AllocateResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_shiftsallocate_is_not_abstract():
    assert not inspect.isabstract(project_ShiftsAllocate)


def test_project_shiftsallocate_constructor_exists():
    assert callable(project_ShiftsAllocate.__init__)


def test_project_shiftsallocate_constructor_args():
    sig = inspect.signature(project_ShiftsAllocate.__init__)
    params = list(sig.parameters.keys())



def test_project_mandatory_is_not_abstract():
    assert not inspect.isabstract(project_Mandatory)


def test_project_mandatory_constructor_exists():
    assert callable(project_Mandatory.__init__)


def test_project_mandatory_constructor_args():
    sig = inspect.signature(project_Mandatory.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_project_mandatory_has_mandatory():
    assert hasattr(project_Mandatory, "mandatory")
    descriptor = None
    for klass in project_Mandatory.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_project_select_is_not_abstract():
    assert not inspect.isabstract(project_Select)


def test_project_select_constructor_exists():
    assert callable(project_Select.__init__)


def test_project_select_constructor_args():
    sig = inspect.signature(project_Select.__init__)
    params = list(sig.parameters.keys())
    assert "argument" in params, "Missing parameter 'argument'"

def test_project_select_has_argument():
    assert hasattr(project_Select, "argument")
    descriptor = None
    for klass in project_Select.__mro__:
        if "argument" in klass.__dict__:
            descriptor = klass.__dict__["argument"]
            break
    assert isinstance(descriptor, property)



def test_project_persistent_is_not_abstract():
    assert not inspect.isabstract(project_Persistent)


def test_project_persistent_constructor_exists():
    assert callable(project_Persistent.__init__)


def test_project_persistent_constructor_args():
    sig = inspect.signature(project_Persistent.__init__)
    params = list(sig.parameters.keys())
    assert "persistent" in params, "Missing parameter 'persistent'"

def test_project_persistent_has_persistent():
    assert hasattr(project_Persistent, "persistent")
    descriptor = None
    for klass in project_Persistent.__mro__:
        if "persistent" in klass.__dict__:
            descriptor = klass.__dict__["persistent"]
            break
    assert isinstance(descriptor, property)



def test_project_alternative_is_not_abstract():
    assert not inspect.isabstract(project_Alternative)


def test_project_alternative_constructor_exists():
    assert callable(project_Alternative.__init__)


def test_project_alternative_constructor_args():
    sig = inspect.signature(project_Alternative.__init__)
    params = list(sig.parameters.keys())



def test_project_alert_is_not_abstract():
    assert not inspect.isabstract(project_Alert)


def test_project_alert_constructor_exists():
    assert callable(project_Alert.__init__)


def test_project_alert_constructor_args():
    sig = inspect.signature(project_Alert.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_project_alert_has_level():
    assert hasattr(project_Alert, "level")
    descriptor = None
    for klass in project_Alert.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_project_nikureportattribute_is_not_abstract():
    assert not inspect.isabstract(project_NikuReportAttribute)


def test_project_nikureportattribute_constructor_exists():
    assert callable(project_NikuReportAttribute.__init__)


def test_project_nikureportattribute_constructor_args():
    sig = inspect.signature(project_NikuReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_interval4_is_not_abstract():
    assert not inspect.isabstract(project_Interval4)


def test_project_interval4_constructor_exists():
    assert callable(project_Interval4.__init__)


def test_project_interval4_constructor_args():
    sig = inspect.signature(project_Interval4.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_project_interval4_has_start():
    assert hasattr(project_Interval4, "start")
    descriptor = None
    for klass in project_Interval4.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_project_interval4_has_end():
    assert hasattr(project_Interval4, "end")
    descriptor = None
    for klass in project_Interval4.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_project_booking_is_not_abstract():
    assert not inspect.isabstract(project_Booking)


def test_project_booking_constructor_exists():
    assert callable(project_Booking.__init__)


def test_project_booking_constructor_args():
    sig = inspect.signature(project_Booking.__init__)
    params = list(sig.parameters.keys())
    assert "sloppy" in params, "Missing parameter 'sloppy'"
    assert "overtime" in params, "Missing parameter 'overtime'"

def test_project_booking_has_sloppy():
    assert hasattr(project_Booking, "sloppy")
    descriptor = None
    for klass in project_Booking.__mro__:
        if "sloppy" in klass.__dict__:
            descriptor = klass.__dict__["sloppy"]
            break
    assert isinstance(descriptor, property)

def test_project_booking_has_overtime():
    assert hasattr(project_Booking, "overtime")
    descriptor = None
    for klass in project_Booking.__mro__:
        if "overtime" in klass.__dict__:
            descriptor = klass.__dict__["overtime"]
            break
    assert isinstance(descriptor, property)



def test_project_allocateresourceattribute_is_not_abstract():
    assert not inspect.isabstract(project_AllocateResourceAttribute)


def test_project_allocateresourceattribute_constructor_exists():
    assert callable(project_AllocateResourceAttribute.__init__)


def test_project_allocateresourceattribute_constructor_args():
    sig = inspect.signature(project_AllocateResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_allocateresource_is_not_abstract():
    assert not inspect.isabstract(project_AllocateResource)


def test_project_allocateresource_constructor_exists():
    assert callable(project_AllocateResource.__init__)


def test_project_allocateresource_constructor_args():
    sig = inspect.signature(project_AllocateResource.__init__)
    params = list(sig.parameters.keys())



def test_project_newtaskattribute_is_not_abstract():
    assert not inspect.isabstract(project_NewTaskAttribute)


def test_project_newtaskattribute_constructor_exists():
    assert callable(project_NewTaskAttribute.__init__)


def test_project_newtaskattribute_constructor_args():
    sig = inspect.signature(project_NewTaskAttribute.__init__)
    params = list(sig.parameters.keys())



def test_timesheetattribute_is_not_abstract():
    assert not inspect.isabstract(TimesheetAttribute)


def test_timesheetattribute_constructor_exists():
    assert callable(TimesheetAttribute.__init__)


def test_timesheetattribute_constructor_args():
    sig = inspect.signature(TimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_shifttimesheet_is_not_abstract():
    assert not inspect.isabstract(project_ShiftTimesheet)


def test_project_shifttimesheet_constructor_exists():
    assert callable(project_ShiftTimesheet.__init__)


def test_project_shifttimesheet_constructor_args():
    sig = inspect.signature(project_ShiftTimesheet.__init__)
    params = list(sig.parameters.keys())



def test_project_tasktimesheet_is_not_abstract():
    assert not inspect.isabstract(project_TaskTimesheet)


def test_project_tasktimesheet_constructor_exists():
    assert callable(project_TaskTimesheet.__init__)


def test_project_tasktimesheet_constructor_args():
    sig = inspect.signature(project_TaskTimesheet.__init__)
    params = list(sig.parameters.keys())



def test_project_statustimesheet_is_not_abstract():
    assert not inspect.isabstract(project_StatusTimesheet)


def test_project_statustimesheet_constructor_exists():
    assert callable(project_StatusTimesheet.__init__)


def test_project_statustimesheet_constructor_args():
    sig = inspect.signature(project_StatusTimesheet.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "level" in params, "Missing parameter 'level'"

def test_project_statustimesheet_has_text():
    assert hasattr(project_StatusTimesheet, "text")
    descriptor = None
    for klass in project_StatusTimesheet.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_project_statustimesheet_has_level():
    assert hasattr(project_StatusTimesheet, "level")
    descriptor = None
    for klass in project_StatusTimesheet.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_project_newtask_is_not_abstract():
    assert not inspect.isabstract(project_NewTask)


def test_project_newtask_constructor_exists():
    assert callable(project_NewTask.__init__)


def test_project_newtask_constructor_args():
    sig = inspect.signature(project_NewTask.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "id" in params, "Missing parameter 'id'"

def test_project_newtask_has_text():
    assert hasattr(project_NewTask, "text")
    descriptor = None
    for klass in project_NewTask.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_project_newtask_has_id():
    assert hasattr(project_NewTask, "id")
    descriptor = None
    for klass in project_NewTask.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_project_navigatorattribute_is_not_abstract():
    assert not inspect.isabstract(project_NavigatorAttribute)


def test_project_navigatorattribute_constructor_exists():
    assert callable(project_NavigatorAttribute.__init__)


def test_project_navigatorattribute_constructor_args():
    sig = inspect.signature(project_NavigatorAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_reportattribute_is_not_abstract():
    assert not inspect.isabstract(project_ReportAttribute)


def test_project_reportattribute_constructor_exists():
    assert callable(project_ReportAttribute.__init__)


def test_project_reportattribute_constructor_args():
    sig = inspect.signature(project_ReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_resourceattribute_is_not_abstract():
    assert not inspect.isabstract(project_ResourceAttribute)


def test_project_resourceattribute_constructor_exists():
    assert callable(project_ResourceAttribute.__init__)


def test_project_resourceattribute_constructor_args():
    sig = inspect.signature(project_ResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_resourceattribute_is_not_abstract():
    assert not inspect.isabstract(ResourceAttribute)


def test_resourceattribute_constructor_exists():
    assert callable(ResourceAttribute.__init__)


def test_resourceattribute_constructor_args():
    sig = inspect.signature(ResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_email_is_not_abstract():
    assert not inspect.isabstract(project_Email)


def test_project_email_constructor_exists():
    assert callable(project_Email.__init__)


def test_project_email_constructor_args():
    sig = inspect.signature(project_Email.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_project_email_has_address():
    assert hasattr(project_Email, "address")
    descriptor = None
    for klass in project_Email.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_project_shiftsresource_is_not_abstract():
    assert not inspect.isabstract(project_ShiftsResource)


def test_project_shiftsresource_constructor_exists():
    assert callable(project_ShiftsResource.__init__)


def test_project_shiftsresource_constructor_args():
    sig = inspect.signature(project_ShiftsResource.__init__)
    params = list(sig.parameters.keys())



def test_project_workinghours_is_not_abstract():
    assert not inspect.isabstract(project_WorkingHours)


def test_project_workinghours_constructor_exists():
    assert callable(project_WorkingHours.__init__)


def test_project_workinghours_constructor_args():
    sig = inspect.signature(project_WorkingHours.__init__)
    params = list(sig.parameters.keys())
    assert "off" in params, "Missing parameter 'off'"

def test_project_workinghours_has_off():
    assert hasattr(project_WorkingHours, "off")
    descriptor = None
    for klass in project_WorkingHours.__mro__:
        if "off" in klass.__dict__:
            descriptor = klass.__dict__["off"]
            break
    assert isinstance(descriptor, property)



def test_project_extendedresourceattribute_is_not_abstract():
    assert not inspect.isabstract(project_ExtendedResourceAttribute)


def test_project_extendedresourceattribute_constructor_exists():
    assert callable(project_ExtendedResourceAttribute.__init__)


def test_project_extendedresourceattribute_constructor_args():
    sig = inspect.signature(project_ExtendedResourceAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project_extendedresourceattribute_has_value():
    assert hasattr(project_ExtendedResourceAttribute, "value")
    descriptor = None
    for klass in project_ExtendedResourceAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project_purgeresource_is_not_abstract():
    assert not inspect.isabstract(project_PurgeResource)


def test_project_purgeresource_constructor_exists():
    assert callable(project_PurgeResource.__init__)


def test_project_purgeresource_constructor_args():
    sig = inspect.signature(project_PurgeResource.__init__)
    params = list(sig.parameters.keys())
    assert "listAttribute" in params, "Missing parameter 'listAttribute'"

def test_project_purgeresource_has_listAttribute():
    assert hasattr(project_PurgeResource, "listAttribute")
    descriptor = None
    for klass in project_PurgeResource.__mro__:
        if "listAttribute" in klass.__dict__:
            descriptor = klass.__dict__["listAttribute"]
            break
    assert isinstance(descriptor, property)



def test_project_managers_is_not_abstract():
    assert not inspect.isabstract(project_Managers)


def test_project_managers_constructor_exists():
    assert callable(project_Managers.__init__)


def test_project_managers_constructor_args():
    sig = inspect.signature(project_Managers.__init__)
    params = list(sig.parameters.keys())



def test_project_efficiency_is_not_abstract():
    assert not inspect.isabstract(project_Efficiency)


def test_project_efficiency_constructor_exists():
    assert callable(project_Efficiency.__init__)


def test_project_efficiency_constructor_args():
    sig = inspect.signature(project_Efficiency.__init__)
    params = list(sig.parameters.keys())
    assert "efficiency" in params, "Missing parameter 'efficiency'"

def test_project_efficiency_has_efficiency():
    assert hasattr(project_Efficiency, "efficiency")
    descriptor = None
    for klass in project_Efficiency.__mro__:
        if "efficiency" in klass.__dict__:
            descriptor = klass.__dict__["efficiency"]
            break
    assert isinstance(descriptor, property)



def test_project_bookingresource_is_not_abstract():
    assert not inspect.isabstract(project_BookingResource)


def test_project_bookingresource_constructor_exists():
    assert callable(project_BookingResource.__init__)


def test_project_bookingresource_constructor_args():
    sig = inspect.signature(project_BookingResource.__init__)
    params = list(sig.parameters.keys())



def test_project_exportattribute_is_not_abstract():
    assert not inspect.isabstract(project_ExportAttribute)


def test_project_exportattribute_constructor_exists():
    assert callable(project_ExportAttribute.__init__)


def test_project_exportattribute_constructor_args():
    sig = inspect.signature(project_ExportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_icalreportattribute_is_not_abstract():
    assert not inspect.isabstract(project_IcalReportAttribute)


def test_project_icalreportattribute_constructor_exists():
    assert callable(project_IcalReportAttribute.__init__)


def test_project_icalreportattribute_constructor_args():
    sig = inspect.signature(project_IcalReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_reportattribute_is_not_abstract():
    assert not inspect.isabstract(ReportAttribute)


def test_reportattribute_constructor_exists():
    assert callable(ReportAttribute.__init__)


def test_reportattribute_constructor_args():
    sig = inspect.signature(ReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_hidetask_is_not_abstract():
    assert not inspect.isabstract(project_HideTask)


def test_project_hidetask_constructor_exists():
    assert callable(project_HideTask.__init__)


def test_project_hidetask_constructor_args():
    sig = inspect.signature(project_HideTask.__init__)
    params = list(sig.parameters.keys())



def test_project_formats_is_not_abstract():
    assert not inspect.isabstract(project_Formats)


def test_project_formats_constructor_exists():
    assert callable(project_Formats.__init__)


def test_project_formats_constructor_args():
    sig = inspect.signature(project_Formats.__init__)
    params = list(sig.parameters.keys())
    assert "formats" in params, "Missing parameter 'formats'"

def test_project_formats_has_formats():
    assert hasattr(project_Formats, "formats")
    descriptor = None
    for klass in project_Formats.__mro__:
        if "formats" in klass.__dict__:
            descriptor = klass.__dict__["formats"]
            break
    assert isinstance(descriptor, property)



def test_project_left_is_not_abstract():
    assert not inspect.isabstract(project_Left)


def test_project_left_constructor_exists():
    assert callable(project_Left.__init__)


def test_project_left_constructor_args():
    sig = inspect.signature(project_Left.__init__)
    params = list(sig.parameters.keys())



def test_project_hideaccount_is_not_abstract():
    assert not inspect.isabstract(project_HideAccount)


def test_project_hideaccount_constructor_exists():
    assert callable(project_HideAccount.__init__)


def test_project_hideaccount_constructor_args():
    sig = inspect.signature(project_HideAccount.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_project_hideaccount_has_expression():
    assert hasattr(project_HideAccount, "expression")
    descriptor = None
    for klass in project_HideAccount.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_project_sortjournalentries_is_not_abstract():
    assert not inspect.isabstract(project_SortJournalEntries)


def test_project_sortjournalentries_constructor_exists():
    assert callable(project_SortJournalEntries.__init__)


def test_project_sortjournalentries_constructor_args():
    sig = inspect.signature(project_SortJournalEntries.__init__)
    params = list(sig.parameters.keys())



def test_project_title_is_not_abstract():
    assert not inspect.isabstract(project_Title)


def test_project_title_constructor_exists():
    assert callable(project_Title.__init__)


def test_project_title_constructor_args():
    sig = inspect.signature(project_Title.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_project_title_has_title():
    assert hasattr(project_Title, "title")
    descriptor = None
    for klass in project_Title.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_project_right_is_not_abstract():
    assert not inspect.isabstract(project_Right)


def test_project_right_constructor_exists():
    assert callable(project_Right.__init__)


def test_project_right_constructor_args():
    sig = inspect.signature(project_Right.__init__)
    params = list(sig.parameters.keys())



def test_project_prolog_is_not_abstract():
    assert not inspect.isabstract(project_Prolog)


def test_project_prolog_constructor_exists():
    assert callable(project_Prolog.__init__)


def test_project_prolog_constructor_args():
    sig = inspect.signature(project_Prolog.__init__)
    params = list(sig.parameters.keys())



def test_project_selfcontained_is_not_abstract():
    assert not inspect.isabstract(project_SelfContained)


def test_project_selfcontained_constructor_exists():
    assert callable(project_SelfContained.__init__)


def test_project_selfcontained_constructor_args():
    sig = inspect.signature(project_SelfContained.__init__)
    params = list(sig.parameters.keys())
    assert "selfcontained" in params, "Missing parameter 'selfcontained'"

def test_project_selfcontained_has_selfcontained():
    assert hasattr(project_SelfContained, "selfcontained")
    descriptor = None
    for klass in project_SelfContained.__mro__:
        if "selfcontained" in klass.__dict__:
            descriptor = klass.__dict__["selfcontained"]
            break
    assert isinstance(descriptor, property)



def test_project_rollupaccount_is_not_abstract():
    assert not inspect.isabstract(project_RollupAccount)


def test_project_rollupaccount_constructor_exists():
    assert callable(project_RollupAccount.__init__)


def test_project_rollupaccount_constructor_args():
    sig = inspect.signature(project_RollupAccount.__init__)
    params = list(sig.parameters.keys())



def test_project_accountroot_is_not_abstract():
    assert not inspect.isabstract(project_AccountRoot)


def test_project_accountroot_constructor_exists():
    assert callable(project_AccountRoot.__init__)


def test_project_accountroot_constructor_args():
    sig = inspect.signature(project_AccountRoot.__init__)
    params = list(sig.parameters.keys())



def test_project_epilog_is_not_abstract():
    assert not inspect.isabstract(project_Epilog)


def test_project_epilog_constructor_exists():
    assert callable(project_Epilog.__init__)


def test_project_epilog_constructor_args():
    sig = inspect.signature(project_Epilog.__init__)
    params = list(sig.parameters.keys())



def test_project_rollupresource_is_not_abstract():
    assert not inspect.isabstract(project_RollupResource)


def test_project_rollupresource_constructor_exists():
    assert callable(project_RollupResource.__init__)


def test_project_rollupresource_constructor_args():
    sig = inspect.signature(project_RollupResource.__init__)
    params = list(sig.parameters.keys())



def test_project_hidejournalentry_is_not_abstract():
    assert not inspect.isabstract(project_HideJournalEntry)


def test_project_hidejournalentry_constructor_exists():
    assert callable(project_HideJournalEntry.__init__)


def test_project_hidejournalentry_constructor_args():
    sig = inspect.signature(project_HideJournalEntry.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_project_hidejournalentry_has_expression():
    assert hasattr(project_HideJournalEntry, "expression")
    descriptor = None
    for klass in project_HideJournalEntry.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_project_hideresource_is_not_abstract():
    assert not inspect.isabstract(project_HideResource)


def test_project_hideresource_constructor_exists():
    assert callable(project_HideResource.__init__)


def test_project_hideresource_constructor_args():
    sig = inspect.signature(project_HideResource.__init__)
    params = list(sig.parameters.keys())



def test_project_headline_is_not_abstract():
    assert not inspect.isabstract(project_Headline)


def test_project_headline_constructor_exists():
    assert callable(project_Headline.__init__)


def test_project_headline_constructor_args():
    sig = inspect.signature(project_Headline.__init__)
    params = list(sig.parameters.keys())



def test_project_footer_is_not_abstract():
    assert not inspect.isabstract(project_Footer)


def test_project_footer_constructor_exists():
    assert callable(project_Footer.__init__)


def test_project_footer_constructor_args():
    sig = inspect.signature(project_Footer.__init__)
    params = list(sig.parameters.keys())



def test_project_timezone_is_not_abstract():
    assert not inspect.isabstract(project_Timezone)


def test_project_timezone_constructor_exists():
    assert callable(project_Timezone.__init__)


def test_project_timezone_constructor_args():
    sig = inspect.signature(project_Timezone.__init__)
    params = list(sig.parameters.keys())
    assert "timezone" in params, "Missing parameter 'timezone'"

def test_project_timezone_has_timezone():
    assert hasattr(project_Timezone, "timezone")
    descriptor = None
    for klass in project_Timezone.__mro__:
        if "timezone" in klass.__dict__:
            descriptor = klass.__dict__["timezone"]
            break
    assert isinstance(descriptor, property)



def test_project_taskroot_is_not_abstract():
    assert not inspect.isabstract(project_TaskRoot)


def test_project_taskroot_constructor_exists():
    assert callable(project_TaskRoot.__init__)


def test_project_taskroot_constructor_args():
    sig = inspect.signature(project_TaskRoot.__init__)
    params = list(sig.parameters.keys())



def test_project_sortresources_is_not_abstract():
    assert not inspect.isabstract(project_SortResources)


def test_project_sortresources_constructor_exists():
    assert callable(project_SortResources.__init__)


def test_project_sortresources_constructor_args():
    sig = inspect.signature(project_SortResources.__init__)
    params = list(sig.parameters.keys())



def test_project_numberformat_is_not_abstract():
    assert not inspect.isabstract(project_NumberFormat)


def test_project_numberformat_constructor_exists():
    assert callable(project_NumberFormat.__init__)


def test_project_numberformat_constructor_args():
    sig = inspect.signature(project_NumberFormat.__init__)
    params = list(sig.parameters.keys())



def test_project_purgereport_is_not_abstract():
    assert not inspect.isabstract(project_PurgeReport)


def test_project_purgereport_constructor_exists():
    assert callable(project_PurgeReport.__init__)


def test_project_purgereport_constructor_args():
    sig = inspect.signature(project_PurgeReport.__init__)
    params = list(sig.parameters.keys())
    assert "listAttribute" in params, "Missing parameter 'listAttribute'"

def test_project_purgereport_has_listAttribute():
    assert hasattr(project_PurgeReport, "listAttribute")
    descriptor = None
    for klass in project_PurgeReport.__mro__:
        if "listAttribute" in klass.__dict__:
            descriptor = klass.__dict__["listAttribute"]
            break
    assert isinstance(descriptor, property)



def test_project_scenarios_is_not_abstract():
    assert not inspect.isabstract(project_Scenarios)


def test_project_scenarios_constructor_exists():
    assert callable(project_Scenarios.__init__)


def test_project_scenarios_constructor_args():
    sig = inspect.signature(project_Scenarios.__init__)
    params = list(sig.parameters.keys())



def test_project_currencyformat_is_not_abstract():
    assert not inspect.isabstract(project_CurrencyFormat)


def test_project_currencyformat_constructor_exists():
    assert callable(project_CurrencyFormat.__init__)


def test_project_currencyformat_constructor_args():
    sig = inspect.signature(project_CurrencyFormat.__init__)
    params = list(sig.parameters.keys())



def test_project_timeformat_is_not_abstract():
    assert not inspect.isabstract(project_TimeFormat)


def test_project_timeformat_constructor_exists():
    assert callable(project_TimeFormat.__init__)


def test_project_timeformat_constructor_args():
    sig = inspect.signature(project_TimeFormat.__init__)
    params = list(sig.parameters.keys())
    assert "timeformat" in params, "Missing parameter 'timeformat'"

def test_project_timeformat_has_timeformat():
    assert hasattr(project_TimeFormat, "timeformat")
    descriptor = None
    for klass in project_TimeFormat.__mro__:
        if "timeformat" in klass.__dict__:
            descriptor = klass.__dict__["timeformat"]
            break
    assert isinstance(descriptor, property)



def test_project_sortaccounts_is_not_abstract():
    assert not inspect.isabstract(project_SortAccounts)


def test_project_sortaccounts_constructor_exists():
    assert callable(project_SortAccounts.__init__)


def test_project_sortaccounts_constructor_args():
    sig = inspect.signature(project_SortAccounts.__init__)
    params = list(sig.parameters.keys())



def test_project_journalattributes_is_not_abstract():
    assert not inspect.isabstract(project_JournalAttributes)


def test_project_journalattributes_constructor_exists():
    assert callable(project_JournalAttributes.__init__)


def test_project_journalattributes_constructor_args():
    sig = inspect.signature(project_JournalAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "propertyid" in params, "Missing parameter 'propertyid'"
    assert "all" in params, "Missing parameter 'all'"
    assert "none" in params, "Missing parameter 'none'"
    assert "summary" in params, "Missing parameter 'summary'"
    assert "author" in params, "Missing parameter 'author'"
    assert "_property" in params, "Missing parameter '_property'"
    assert "details" in params, "Missing parameter 'details'"
    assert "flags" in params, "Missing parameter 'flags'"
    assert "date" in params, "Missing parameter 'date'"
    assert "headline" in params, "Missing parameter 'headline'"
    assert "timesheet" in params, "Missing parameter 'timesheet'"

def test_project_journalattributes_has_propertyid():
    assert hasattr(project_JournalAttributes, "propertyid")
    descriptor = None
    for klass in project_JournalAttributes.__mro__:
        if "propertyid" in klass.__dict__:
            descriptor = klass.__dict__["propertyid"]
            break
    assert isinstance(descriptor, property)

def test_project_journalattributes_has_all():
    assert hasattr(project_JournalAttributes, "all")
    descriptor = None
    for klass in project_JournalAttributes.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_project_journalattributes_has_none():
    assert hasattr(project_JournalAttributes, "none")
    descriptor = None
    for klass in project_JournalAttributes.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_project_journalattributes_has_summary():
    assert hasattr(project_JournalAttributes, "summary")
    descriptor = None
    for klass in project_JournalAttributes.__mro__:
        if "summary" in klass.__dict__:
            descriptor = klass.__dict__["summary"]
            break
    assert isinstance(descriptor, property)

def test_project_journalattributes_has_author():
    assert hasattr(project_JournalAttributes, "author")
    descriptor = None
    for klass in project_JournalAttributes.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_project_journalattributes_has__property():
    assert hasattr(project_JournalAttributes, "_property")
    descriptor = None
    for klass in project_JournalAttributes.__mro__:
        if "_property" in klass.__dict__:
            descriptor = klass.__dict__["_property"]
            break
    assert isinstance(descriptor, property)

def test_project_journalattributes_has_details():
    assert hasattr(project_JournalAttributes, "details")
    descriptor = None
    for klass in project_JournalAttributes.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)

def test_project_journalattributes_has_flags():
    assert hasattr(project_JournalAttributes, "flags")
    descriptor = None
    for klass in project_JournalAttributes.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)

def test_project_journalattributes_has_date():
    assert hasattr(project_JournalAttributes, "date")
    descriptor = None
    for klass in project_JournalAttributes.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_project_journalattributes_has_headline():
    assert hasattr(project_JournalAttributes, "headline")
    descriptor = None
    for klass in project_JournalAttributes.__mro__:
        if "headline" in klass.__dict__:
            descriptor = klass.__dict__["headline"]
            break
    assert isinstance(descriptor, property)

def test_project_journalattributes_has_timesheet():
    assert hasattr(project_JournalAttributes, "timesheet")
    descriptor = None
    for klass in project_JournalAttributes.__mro__:
        if "timesheet" in klass.__dict__:
            descriptor = klass.__dict__["timesheet"]
            break
    assert isinstance(descriptor, property)



def test_project_center_is_not_abstract():
    assert not inspect.isabstract(project_Center)


def test_project_center_constructor_exists():
    assert callable(project_Center.__init__)


def test_project_center_constructor_args():
    sig = inspect.signature(project_Center.__init__)
    params = list(sig.parameters.keys())



def test_project_resourceroot_is_not_abstract():
    assert not inspect.isabstract(project_ResourceRoot)


def test_project_resourceroot_constructor_exists():
    assert callable(project_ResourceRoot.__init__)


def test_project_resourceroot_constructor_args():
    sig = inspect.signature(project_ResourceRoot.__init__)
    params = list(sig.parameters.keys())



def test_project_rolluptask_is_not_abstract():
    assert not inspect.isabstract(project_RollupTask)


def test_project_rolluptask_constructor_exists():
    assert callable(project_RollupTask.__init__)


def test_project_rolluptask_constructor_args():
    sig = inspect.signature(project_RollupTask.__init__)
    params = list(sig.parameters.keys())



def test_project_loadunit_is_not_abstract():
    assert not inspect.isabstract(project_LoadUnit)


def test_project_loadunit_constructor_exists():
    assert callable(project_LoadUnit.__init__)


def test_project_loadunit_constructor_args():
    sig = inspect.signature(project_LoadUnit.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_project_loadunit_has_unit():
    assert hasattr(project_LoadUnit, "unit")
    descriptor = None
    for klass in project_LoadUnit.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_project_columns_is_not_abstract():
    assert not inspect.isabstract(project_Columns)


def test_project_columns_constructor_exists():
    assert callable(project_Columns.__init__)


def test_project_columns_constructor_args():
    sig = inspect.signature(project_Columns.__init__)
    params = list(sig.parameters.keys())



def test_project_caption_is_not_abstract():
    assert not inspect.isabstract(project_Caption)


def test_project_caption_constructor_exists():
    assert callable(project_Caption.__init__)


def test_project_caption_constructor_args():
    sig = inspect.signature(project_Caption.__init__)
    params = list(sig.parameters.keys())



def test_project_header_is_not_abstract():
    assert not inspect.isabstract(project_Header)


def test_project_header_constructor_exists():
    assert callable(project_Header.__init__)


def test_project_header_constructor_args():
    sig = inspect.signature(project_Header.__init__)
    params = list(sig.parameters.keys())



def test_project_journalmode_is_not_abstract():
    assert not inspect.isabstract(project_JournalMode)


def test_project_journalmode_constructor_exists():
    assert callable(project_JournalMode.__init__)


def test_project_journalmode_constructor_args():
    sig = inspect.signature(project_JournalMode.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_project_journalmode_has_mode():
    assert hasattr(project_JournalMode, "mode")
    descriptor = None
    for klass in project_JournalMode.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_project_sorttasks_is_not_abstract():
    assert not inspect.isabstract(project_SortTasks)


def test_project_sorttasks_constructor_exists():
    assert callable(project_SortTasks.__init__)


def test_project_sorttasks_constructor_args():
    sig = inspect.signature(project_SortTasks.__init__)
    params = list(sig.parameters.keys())



def test_textreport_is_not_abstract():
    assert not inspect.isabstract(TextReport)


def test_textreport_constructor_exists():
    assert callable(TextReport.__init__)


def test_textreport_constructor_args():
    sig = inspect.signature(TextReport.__init__)
    params = list(sig.parameters.keys())



def test_taskreport_is_not_abstract():
    assert not inspect.isabstract(TaskReport)


def test_taskreport_constructor_exists():
    assert callable(TaskReport.__init__)


def test_taskreport_constructor_args():
    sig = inspect.signature(TaskReport.__init__)
    params = list(sig.parameters.keys())



def test_resourcereport_is_not_abstract():
    assert not inspect.isabstract(ResourceReport)


def test_resourcereport_constructor_exists():
    assert callable(ResourceReport.__init__)


def test_resourcereport_constructor_args():
    sig = inspect.signature(ResourceReport.__init__)
    params = list(sig.parameters.keys())



def test_accountreport_is_not_abstract():
    assert not inspect.isabstract(AccountReport)


def test_accountreport_constructor_exists():
    assert callable(AccountReport.__init__)


def test_accountreport_constructor_args():
    sig = inspect.signature(AccountReport.__init__)
    params = list(sig.parameters.keys())



def test_project_report_is_not_abstract():
    assert not inspect.isabstract(project_Report)


def test_project_report_constructor_exists():
    assert callable(project_Report.__init__)


def test_project_report_constructor_args():
    sig = inspect.signature(project_Report.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_project_report_has_id():
    assert hasattr(project_Report, "id")
    descriptor = None
    for klass in project_Report.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_project_report_has_name():
    assert hasattr(project_Report, "name")
    descriptor = None
    for klass in project_Report.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_project_taskattribute_is_not_abstract():
    assert not inspect.isabstract(project_TaskAttribute)


def test_project_taskattribute_constructor_exists():
    assert callable(project_TaskAttribute.__init__)


def test_project_taskattribute_constructor_args():
    sig = inspect.signature(project_TaskAttribute.__init__)
    params = list(sig.parameters.keys())



def test_taskattribute_is_not_abstract():
    assert not inspect.isabstract(TaskAttribute)


def test_taskattribute_constructor_exists():
    assert callable(TaskAttribute.__init__)


def test_taskattribute_constructor_args():
    sig = inspect.signature(TaskAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_note_is_not_abstract():
    assert not inspect.isabstract(project_Note)


def test_project_note_constructor_exists():
    assert callable(project_Note.__init__)


def test_project_note_constructor_args():
    sig = inspect.signature(project_Note.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"

def test_project_note_has_note():
    assert hasattr(project_Note, "note")
    descriptor = None
    for klass in project_Note.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_project_shiftstask_is_not_abstract():
    assert not inspect.isabstract(project_ShiftsTask)


def test_project_shiftstask_constructor_exists():
    assert callable(project_ShiftsTask.__init__)


def test_project_shiftstask_constructor_args():
    sig = inspect.signature(project_ShiftsTask.__init__)
    params = list(sig.parameters.keys())



def test_project_period_is_not_abstract():
    assert not inspect.isabstract(project_Period)


def test_project_period_constructor_exists():
    assert callable(project_Period.__init__)


def test_project_period_constructor_args():
    sig = inspect.signature(project_Period.__init__)
    params = list(sig.parameters.keys())



def test_project_priority_is_not_abstract():
    assert not inspect.isabstract(project_Priority)


def test_project_priority_constructor_exists():
    assert callable(project_Priority.__init__)


def test_project_priority_constructor_args():
    sig = inspect.signature(project_Priority.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_project_priority_has_priority():
    assert hasattr(project_Priority, "priority")
    descriptor = None
    for klass in project_Priority.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_project_warn_is_not_abstract():
    assert not inspect.isabstract(project_Warn)


def test_project_warn_constructor_exists():
    assert callable(project_Warn.__init__)


def test_project_warn_constructor_args():
    sig = inspect.signature(project_Warn.__init__)
    params = list(sig.parameters.keys())



def test_project_charge_is_not_abstract():
    assert not inspect.isabstract(project_Charge)


def test_project_charge_constructor_exists():
    assert callable(project_Charge.__init__)


def test_project_charge_constructor_args():
    sig = inspect.signature(project_Charge.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "applies" in params, "Missing parameter 'applies'"

def test_project_charge_has_amount():
    assert hasattr(project_Charge, "amount")
    descriptor = None
    for klass in project_Charge.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_project_charge_has_applies():
    assert hasattr(project_Charge, "applies")
    descriptor = None
    for klass in project_Charge.__mro__:
        if "applies" in klass.__dict__:
            descriptor = klass.__dict__["applies"]
            break
    assert isinstance(descriptor, property)



def test_project_scheduled_is_not_abstract():
    assert not inspect.isabstract(project_Scheduled)


def test_project_scheduled_constructor_exists():
    assert callable(project_Scheduled.__init__)


def test_project_scheduled_constructor_args():
    sig = inspect.signature(project_Scheduled.__init__)
    params = list(sig.parameters.keys())
    assert "scheduled" in params, "Missing parameter 'scheduled'"

def test_project_scheduled_has_scheduled():
    assert hasattr(project_Scheduled, "scheduled")
    descriptor = None
    for klass in project_Scheduled.__mro__:
        if "scheduled" in klass.__dict__:
            descriptor = klass.__dict__["scheduled"]
            break
    assert isinstance(descriptor, property)



def test_project_start_is_not_abstract():
    assert not inspect.isabstract(project_Start)


def test_project_start_constructor_exists():
    assert callable(project_Start.__init__)


def test_project_start_constructor_args():
    sig = inspect.signature(project_Start.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"

def test_project_start_has_start():
    assert hasattr(project_Start, "start")
    descriptor = None
    for klass in project_Start.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_project_end_is_not_abstract():
    assert not inspect.isabstract(project_End)


def test_project_end_constructor_exists():
    assert callable(project_End.__init__)


def test_project_end_constructor_args():
    sig = inspect.signature(project_End.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"

def test_project_end_has_end():
    assert hasattr(project_End, "end")
    descriptor = None
    for klass in project_End.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_project_minend_is_not_abstract():
    assert not inspect.isabstract(project_MinEnd)


def test_project_minend_constructor_exists():
    assert callable(project_MinEnd.__init__)


def test_project_minend_constructor_args():
    sig = inspect.signature(project_MinEnd.__init__)
    params = list(sig.parameters.keys())
    assert "minEnd" in params, "Missing parameter 'minEnd'"

def test_project_minend_has_minEnd():
    assert hasattr(project_MinEnd, "minEnd")
    descriptor = None
    for klass in project_MinEnd.__mro__:
        if "minEnd" in klass.__dict__:
            descriptor = klass.__dict__["minEnd"]
            break
    assert isinstance(descriptor, property)



def test_project_allocate_is_not_abstract():
    assert not inspect.isabstract(project_Allocate)


def test_project_allocate_constructor_exists():
    assert callable(project_Allocate.__init__)


def test_project_allocate_constructor_args():
    sig = inspect.signature(project_Allocate.__init__)
    params = list(sig.parameters.keys())



def test_project_length_is_not_abstract():
    assert not inspect.isabstract(project_Length)


def test_project_length_constructor_exists():
    assert callable(project_Length.__init__)


def test_project_length_constructor_args():
    sig = inspect.signature(project_Length.__init__)
    params = list(sig.parameters.keys())



def test_project_minstart_is_not_abstract():
    assert not inspect.isabstract(project_MinStart)


def test_project_minstart_constructor_exists():
    assert callable(project_MinStart.__init__)


def test_project_minstart_constructor_args():
    sig = inspect.signature(project_MinStart.__init__)
    params = list(sig.parameters.keys())
    assert "minStart" in params, "Missing parameter 'minStart'"

def test_project_minstart_has_minStart():
    assert hasattr(project_MinStart, "minStart")
    descriptor = None
    for klass in project_MinStart.__mro__:
        if "minStart" in klass.__dict__:
            descriptor = klass.__dict__["minStart"]
            break
    assert isinstance(descriptor, property)



def test_project_duration_is_not_abstract():
    assert not inspect.isabstract(project_Duration)


def test_project_duration_constructor_exists():
    assert callable(project_Duration.__init__)


def test_project_duration_constructor_args():
    sig = inspect.signature(project_Duration.__init__)
    params = list(sig.parameters.keys())



def test_project_complete_is_not_abstract():
    assert not inspect.isabstract(project_Complete)


def test_project_complete_constructor_exists():
    assert callable(project_Complete.__init__)


def test_project_complete_constructor_args():
    sig = inspect.signature(project_Complete.__init__)
    params = list(sig.parameters.keys())
    assert "complete" in params, "Missing parameter 'complete'"

def test_project_complete_has_complete():
    assert hasattr(project_Complete, "complete")
    descriptor = None
    for klass in project_Complete.__mro__:
        if "complete" in klass.__dict__:
            descriptor = klass.__dict__["complete"]
            break
    assert isinstance(descriptor, property)



def test_project_endcredit_is_not_abstract():
    assert not inspect.isabstract(project_EndCredit)


def test_project_endcredit_constructor_exists():
    assert callable(project_EndCredit.__init__)


def test_project_endcredit_constructor_args():
    sig = inspect.signature(project_EndCredit.__init__)
    params = list(sig.parameters.keys())
    assert "credit" in params, "Missing parameter 'credit'"

def test_project_endcredit_has_credit():
    assert hasattr(project_EndCredit, "credit")
    descriptor = None
    for klass in project_EndCredit.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
            break
    assert isinstance(descriptor, property)



def test_project_effort_is_not_abstract():
    assert not inspect.isabstract(project_Effort)


def test_project_effort_constructor_exists():
    assert callable(project_Effort.__init__)


def test_project_effort_constructor_args():
    sig = inspect.signature(project_Effort.__init__)
    params = list(sig.parameters.keys())



def test_project_journalentry_is_not_abstract():
    assert not inspect.isabstract(project_JournalEntry)


def test_project_journalentry_constructor_exists():
    assert callable(project_JournalEntry.__init__)


def test_project_journalentry_constructor_args():
    sig = inspect.signature(project_JournalEntry.__init__)
    params = list(sig.parameters.keys())
    assert "headline" in params, "Missing parameter 'headline'"
    assert "date" in params, "Missing parameter 'date'"

def test_project_journalentry_has_headline():
    assert hasattr(project_JournalEntry, "headline")
    descriptor = None
    for klass in project_JournalEntry.__mro__:
        if "headline" in klass.__dict__:
            descriptor = klass.__dict__["headline"]
            break
    assert isinstance(descriptor, property)

def test_project_journalentry_has_date():
    assert hasattr(project_JournalEntry, "date")
    descriptor = None
    for klass in project_JournalEntry.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_project_purgetask_is_not_abstract():
    assert not inspect.isabstract(project_PurgeTask)


def test_project_purgetask_constructor_exists():
    assert callable(project_PurgeTask.__init__)


def test_project_purgetask_constructor_args():
    sig = inspect.signature(project_PurgeTask.__init__)
    params = list(sig.parameters.keys())
    assert "listAttribute" in params, "Missing parameter 'listAttribute'"

def test_project_purgetask_has_listAttribute():
    assert hasattr(project_PurgeTask, "listAttribute")
    descriptor = None
    for klass in project_PurgeTask.__mro__:
        if "listAttribute" in klass.__dict__:
            descriptor = klass.__dict__["listAttribute"]
            break
    assert isinstance(descriptor, property)



def test_project_bookingtask_is_not_abstract():
    assert not inspect.isabstract(project_BookingTask)


def test_project_bookingtask_constructor_exists():
    assert callable(project_BookingTask.__init__)


def test_project_bookingtask_constructor_args():
    sig = inspect.signature(project_BookingTask.__init__)
    params = list(sig.parameters.keys())



def test_project_chargeset_is_not_abstract():
    assert not inspect.isabstract(project_ChargeSet)


def test_project_chargeset_constructor_exists():
    assert callable(project_ChargeSet.__init__)


def test_project_chargeset_constructor_args():
    sig = inspect.signature(project_ChargeSet.__init__)
    params = list(sig.parameters.keys())



def test_project_maxend_is_not_abstract():
    assert not inspect.isabstract(project_MaxEnd)


def test_project_maxend_constructor_exists():
    assert callable(project_MaxEnd.__init__)


def test_project_maxend_constructor_args():
    sig = inspect.signature(project_MaxEnd.__init__)
    params = list(sig.parameters.keys())
    assert "maxEnd" in params, "Missing parameter 'maxEnd'"

def test_project_maxend_has_maxEnd():
    assert hasattr(project_MaxEnd, "maxEnd")
    descriptor = None
    for klass in project_MaxEnd.__mro__:
        if "maxEnd" in klass.__dict__:
            descriptor = klass.__dict__["maxEnd"]
            break
    assert isinstance(descriptor, property)



def test_project_milestone_is_not_abstract():
    assert not inspect.isabstract(project_Milestone)


def test_project_milestone_constructor_exists():
    assert callable(project_Milestone.__init__)


def test_project_milestone_constructor_args():
    sig = inspect.signature(project_Milestone.__init__)
    params = list(sig.parameters.keys())
    assert "milestone" in params, "Missing parameter 'milestone'"

def test_project_milestone_has_milestone():
    assert hasattr(project_Milestone, "milestone")
    descriptor = None
    for klass in project_Milestone.__mro__:
        if "milestone" in klass.__dict__:
            descriptor = klass.__dict__["milestone"]
            break
    assert isinstance(descriptor, property)



def test_project_scheduling_is_not_abstract():
    assert not inspect.isabstract(project_Scheduling)


def test_project_scheduling_constructor_exists():
    assert callable(project_Scheduling.__init__)


def test_project_scheduling_constructor_args():
    sig = inspect.signature(project_Scheduling.__init__)
    params = list(sig.parameters.keys())
    assert "scheduling" in params, "Missing parameter 'scheduling'"

def test_project_scheduling_has_scheduling():
    assert hasattr(project_Scheduling, "scheduling")
    descriptor = None
    for klass in project_Scheduling.__mro__:
        if "scheduling" in klass.__dict__:
            descriptor = klass.__dict__["scheduling"]
            break
    assert isinstance(descriptor, property)



def test_project_precedes_is_not_abstract():
    assert not inspect.isabstract(project_Precedes)


def test_project_precedes_constructor_exists():
    assert callable(project_Precedes.__init__)


def test_project_precedes_constructor_args():
    sig = inspect.signature(project_Precedes.__init__)
    params = list(sig.parameters.keys())



def test_project_depends_is_not_abstract():
    assert not inspect.isabstract(project_Depends)


def test_project_depends_constructor_exists():
    assert callable(project_Depends.__init__)


def test_project_depends_constructor_args():
    sig = inspect.signature(project_Depends.__init__)
    params = list(sig.parameters.keys())



def test_project_fail_is_not_abstract():
    assert not inspect.isabstract(project_Fail)


def test_project_fail_constructor_exists():
    assert callable(project_Fail.__init__)


def test_project_fail_constructor_args():
    sig = inspect.signature(project_Fail.__init__)
    params = list(sig.parameters.keys())



def test_project_projectid_is_not_abstract():
    assert not inspect.isabstract(project_ProjectId)


def test_project_projectid_constructor_exists():
    assert callable(project_ProjectId.__init__)


def test_project_projectid_constructor_args():
    sig = inspect.signature(project_ProjectId.__init__)
    params = list(sig.parameters.keys())
    assert "projectId" in params, "Missing parameter 'projectId'"

def test_project_projectid_has_projectId():
    assert hasattr(project_ProjectId, "projectId")
    descriptor = None
    for klass in project_ProjectId.__mro__:
        if "projectId" in klass.__dict__:
            descriptor = klass.__dict__["projectId"]
            break
    assert isinstance(descriptor, property)



def test_project_extendedtaskattribute_is_not_abstract():
    assert not inspect.isabstract(project_ExtendedTaskAttribute)


def test_project_extendedtaskattribute_constructor_exists():
    assert callable(project_ExtendedTaskAttribute.__init__)


def test_project_extendedtaskattribute_constructor_args():
    sig = inspect.signature(project_ExtendedTaskAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project_extendedtaskattribute_has_value():
    assert hasattr(project_ExtendedTaskAttribute, "value")
    descriptor = None
    for klass in project_ExtendedTaskAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project_maxstart_is_not_abstract():
    assert not inspect.isabstract(project_MaxStart)


def test_project_maxstart_constructor_exists():
    assert callable(project_MaxStart.__init__)


def test_project_maxstart_constructor_args():
    sig = inspect.signature(project_MaxStart.__init__)
    params = list(sig.parameters.keys())
    assert "maxStart" in params, "Missing parameter 'maxStart'"

def test_project_maxstart_has_maxStart():
    assert hasattr(project_MaxStart, "maxStart")
    descriptor = None
    for klass in project_MaxStart.__mro__:
        if "maxStart" in klass.__dict__:
            descriptor = klass.__dict__["maxStart"]
            break
    assert isinstance(descriptor, property)



def test_project_responsible_is_not_abstract():
    assert not inspect.isabstract(project_Responsible)


def test_project_responsible_constructor_exists():
    assert callable(project_Responsible.__init__)


def test_project_responsible_constructor_args():
    sig = inspect.signature(project_Responsible.__init__)
    params = list(sig.parameters.keys())



def test_project_projectattribute_is_not_abstract():
    assert not inspect.isabstract(project_ProjectAttribute)


def test_project_projectattribute_constructor_exists():
    assert callable(project_ProjectAttribute.__init__)


def test_project_projectattribute_constructor_args():
    sig = inspect.signature(project_ProjectAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_interval2_is_not_abstract():
    assert not inspect.isabstract(project_Interval2)


def test_project_interval2_constructor_exists():
    assert callable(project_Interval2.__init__)


def test_project_interval2_constructor_args():
    sig = inspect.signature(project_Interval2.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"

def test_project_interval2_has_end():
    assert hasattr(project_Interval2, "end")
    descriptor = None
    for klass in project_Interval2.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_project_interval2_has_start():
    assert hasattr(project_Interval2, "start")
    descriptor = None
    for klass in project_Interval2.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_project_global_is_not_abstract():
    assert not inspect.isabstract(project_Global)


def test_project_global_constructor_exists():
    assert callable(project_Global.__init__)


def test_project_global_constructor_args():
    sig = inspect.signature(project_Global.__init__)
    params = list(sig.parameters.keys())



def test_includepropertiesattribute_is_not_abstract():
    assert not inspect.isabstract(IncludePropertiesAttribute)


def test_includepropertiesattribute_constructor_exists():
    assert callable(IncludePropertiesAttribute.__init__)


def test_includepropertiesattribute_constructor_args():
    sig = inspect.signature(IncludePropertiesAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_taskprefix_is_not_abstract():
    assert not inspect.isabstract(project_TaskPrefix)


def test_project_taskprefix_constructor_exists():
    assert callable(project_TaskPrefix.__init__)


def test_project_taskprefix_constructor_args():
    sig = inspect.signature(project_TaskPrefix.__init__)
    params = list(sig.parameters.keys())



def test_project_reportprefix_is_not_abstract():
    assert not inspect.isabstract(project_ReportPrefix)


def test_project_reportprefix_constructor_exists():
    assert callable(project_ReportPrefix.__init__)


def test_project_reportprefix_constructor_args():
    sig = inspect.signature(project_ReportPrefix.__init__)
    params = list(sig.parameters.keys())



def test_project_resourceprefix_is_not_abstract():
    assert not inspect.isabstract(project_ResourcePrefix)


def test_project_resourceprefix_constructor_exists():
    assert callable(project_ResourcePrefix.__init__)


def test_project_resourceprefix_constructor_args():
    sig = inspect.signature(project_ResourcePrefix.__init__)
    params = list(sig.parameters.keys())



def test_project_accountprefix_is_not_abstract():
    assert not inspect.isabstract(project_AccountPrefix)


def test_project_accountprefix_constructor_exists():
    assert callable(project_AccountPrefix.__init__)


def test_project_accountprefix_constructor_args():
    sig = inspect.signature(project_AccountPrefix.__init__)
    params = list(sig.parameters.keys())



def test_project_accountattribute_is_not_abstract():
    assert not inspect.isabstract(project_AccountAttribute)


def test_project_accountattribute_constructor_exists():
    assert callable(project_AccountAttribute.__init__)


def test_project_accountattribute_constructor_args():
    sig = inspect.signature(project_AccountAttribute.__init__)
    params = list(sig.parameters.keys())



def test_accountattribute_is_not_abstract():
    assert not inspect.isabstract(AccountAttribute)


def test_accountattribute_constructor_exists():
    assert callable(AccountAttribute.__init__)


def test_accountattribute_constructor_args():
    sig = inspect.signature(AccountAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project_credit_is_not_abstract():
    assert not inspect.isabstract(project_Credit)


def test_project_credit_constructor_exists():
    assert callable(project_Credit.__init__)


def test_project_credit_constructor_args():
    sig = inspect.signature(project_Credit.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "date" in params, "Missing parameter 'date'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_project_credit_has_description():
    assert hasattr(project_Credit, "description")
    descriptor = None
    for klass in project_Credit.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_project_credit_has_date():
    assert hasattr(project_Credit, "date")
    descriptor = None
    for klass in project_Credit.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_project_credit_has_amount():
    assert hasattr(project_Credit, "amount")
    descriptor = None
    for klass in project_Credit.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_project_accountreport_is_not_abstract():
    assert not inspect.isabstract(project_AccountReport)


def test_project_accountreport_constructor_exists():
    assert callable(project_AccountReport.__init__)


def test_project_accountreport_constructor_args():
    sig = inspect.signature(project_AccountReport.__init__)
    params = list(sig.parameters.keys())



def test_project_supplementaccount_is_not_abstract():
    assert not inspect.isabstract(project_SupplementAccount)


def test_project_supplementaccount_constructor_exists():
    assert callable(project_SupplementAccount.__init__)


def test_project_supplementaccount_constructor_args():
    sig = inspect.signature(project_SupplementAccount.__init__)
    params = list(sig.parameters.keys())



def test_project_statussheet_is_not_abstract():
    assert not inspect.isabstract(project_StatusSheet)


def test_project_statussheet_constructor_exists():
    assert callable(project_StatusSheet.__init__)


def test_project_statussheet_constructor_args():
    sig = inspect.signature(project_StatusSheet.__init__)
    params = list(sig.parameters.keys())



def test_project_flags_is_not_abstract():
    assert not inspect.isabstract(project_Flags)


def test_project_flags_constructor_exists():
    assert callable(project_Flags.__init__)


def test_project_flags_constructor_args():
    sig = inspect.signature(project_Flags.__init__)
    params = list(sig.parameters.keys())
    assert "flags" in params, "Missing parameter 'flags'"

def test_project_flags_has_flags():
    assert hasattr(project_Flags, "flags")
    descriptor = None
    for klass in project_Flags.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)



def test_project_navigator_is_not_abstract():
    assert not inspect.isabstract(project_Navigator)


def test_project_navigator_constructor_exists():
    assert callable(project_Navigator.__init__)


def test_project_navigator_constructor_args():
    sig = inspect.signature(project_Navigator.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_project_navigator_has_id():
    assert hasattr(project_Navigator, "id")
    descriptor = None
    for klass in project_Navigator.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_project_timesheetreport_is_not_abstract():
    assert not inspect.isabstract(project_TimesheetReport)


def test_project_timesheetreport_constructor_exists():
    assert callable(project_TimesheetReport.__init__)


def test_project_timesheetreport_constructor_args():
    sig = inspect.signature(project_TimesheetReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_project_timesheetreport_has_filename():
    assert hasattr(project_TimesheetReport, "filename")
    descriptor = None
    for klass in project_TimesheetReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_project_statussheetreport_is_not_abstract():
    assert not inspect.isabstract(project_StatusSheetReport)


def test_project_statussheetreport_constructor_exists():
    assert callable(project_StatusSheetReport.__init__)


def test_project_statussheetreport_constructor_args():
    sig = inspect.signature(project_StatusSheetReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_project_statussheetreport_has_filename():
    assert hasattr(project_StatusSheetReport, "filename")
    descriptor = None
    for klass in project_StatusSheetReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_project_vacation_is_not_abstract():
    assert not inspect.isabstract(project_Vacation)


def test_project_vacation_constructor_exists():
    assert callable(project_Vacation.__init__)


def test_project_vacation_constructor_args():
    sig = inspect.signature(project_Vacation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_project_vacation_has_name():
    assert hasattr(project_Vacation, "name")
    descriptor = None
    for klass in project_Vacation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_project_rate_is_not_abstract():
    assert not inspect.isabstract(project_Rate)


def test_project_rate_constructor_exists():
    assert callable(project_Rate.__init__)


def test_project_rate_constructor_args():
    sig = inspect.signature(project_Rate.__init__)
    params = list(sig.parameters.keys())
    assert "rate" in params, "Missing parameter 'rate'"

def test_project_rate_has_rate():
    assert hasattr(project_Rate, "rate")
    descriptor = None
    for klass in project_Rate.__mro__:
        if "rate" in klass.__dict__:
            descriptor = klass.__dict__["rate"]
            break
    assert isinstance(descriptor, property)



def test_project_macro_is_not_abstract():
    assert not inspect.isabstract(project_Macro)


def test_project_macro_constructor_exists():
    assert callable(project_Macro.__init__)


def test_project_macro_constructor_args():
    sig = inspect.signature(project_Macro.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project_macro_has_value():
    assert hasattr(project_Macro, "value")
    descriptor = None
    for klass in project_Macro.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project_nikureport_is_not_abstract():
    assert not inspect.isabstract(project_NikuReport)


def test_project_nikureport_constructor_exists():
    assert callable(project_NikuReport.__init__)


def test_project_nikureport_constructor_args():
    sig = inspect.signature(project_NikuReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_project_nikureport_has_filename():
    assert hasattr(project_NikuReport, "filename")
    descriptor = None
    for klass in project_NikuReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_project_textreport_is_not_abstract():
    assert not inspect.isabstract(project_TextReport)


def test_project_textreport_constructor_exists():
    assert callable(project_TextReport.__init__)


def test_project_textreport_constructor_args():
    sig = inspect.signature(project_TextReport.__init__)
    params = list(sig.parameters.keys())



def test_project_resource_is_not_abstract():
    assert not inspect.isabstract(project_Resource)


def test_project_resource_constructor_exists():
    assert callable(project_Resource.__init__)


def test_project_resource_constructor_args():
    sig = inspect.signature(project_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_project_resource_has_id():
    assert hasattr(project_Resource, "id")
    descriptor = None
    for klass in project_Resource.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_project_resource_has_name():
    assert hasattr(project_Resource, "name")
    descriptor = None
    for klass in project_Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_project_limits_is_not_abstract():
    assert not inspect.isabstract(project_Limits)


def test_project_limits_constructor_exists():
    assert callable(project_Limits.__init__)


def test_project_limits_constructor_args():
    sig = inspect.signature(project_Limits.__init__)
    params = list(sig.parameters.keys())



def test_project_icalreport_is_not_abstract():
    assert not inspect.isabstract(project_IcalReport)


def test_project_icalreport_constructor_exists():
    assert callable(project_IcalReport.__init__)


def test_project_icalreport_constructor_args():
    sig = inspect.signature(project_IcalReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_project_icalreport_has_filename():
    assert hasattr(project_IcalReport, "filename")
    descriptor = None
    for klass in project_IcalReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_project_export_is_not_abstract():
    assert not inspect.isabstract(project_Export)


def test_project_export_constructor_exists():
    assert callable(project_Export.__init__)


def test_project_export_constructor_args():
    sig = inspect.signature(project_Export.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "filename" in params, "Missing parameter 'filename'"

def test_project_export_has_id():
    assert hasattr(project_Export, "id")
    descriptor = None
    for klass in project_Export.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_project_export_has_filename():
    assert hasattr(project_Export, "filename")
    descriptor = None
    for klass in project_Export.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_project_timesheet_is_not_abstract():
    assert not inspect.isabstract(project_Timesheet)


def test_project_timesheet_constructor_exists():
    assert callable(project_Timesheet.__init__)


def test_project_timesheet_constructor_args():
    sig = inspect.signature(project_Timesheet.__init__)
    params = list(sig.parameters.keys())



def test_project_supplementreport_is_not_abstract():
    assert not inspect.isabstract(project_SupplementReport)


def test_project_supplementreport_constructor_exists():
    assert callable(project_SupplementReport.__init__)


def test_project_supplementreport_constructor_args():
    sig = inspect.signature(project_SupplementReport.__init__)
    params = list(sig.parameters.keys())



def test_project_supplementresource_is_not_abstract():
    assert not inspect.isabstract(project_SupplementResource)


def test_project_supplementresource_constructor_exists():
    assert callable(project_SupplementResource.__init__)


def test_project_supplementresource_constructor_args():
    sig = inspect.signature(project_SupplementResource.__init__)
    params = list(sig.parameters.keys())



def test_project_copyright_is_not_abstract():
    assert not inspect.isabstract(project_Copyright)


def test_project_copyright_constructor_exists():
    assert callable(project_Copyright.__init__)


def test_project_copyright_constructor_args():
    sig = inspect.signature(project_Copyright.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_project_copyright_has_text():
    assert hasattr(project_Copyright, "text")
    descriptor = None
    for klass in project_Copyright.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_project_shift_is_not_abstract():
    assert not inspect.isabstract(project_Shift)


def test_project_shift_constructor_exists():
    assert callable(project_Shift.__init__)


def test_project_shift_constructor_args():
    sig = inspect.signature(project_Shift.__init__)
    params = list(sig.parameters.keys())
    assert "replace" in params, "Missing parameter 'replace'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "timezone" in params, "Missing parameter 'timezone'"

def test_project_shift_has_replace():
    assert hasattr(project_Shift, "replace")
    descriptor = None
    for klass in project_Shift.__mro__:
        if "replace" in klass.__dict__:
            descriptor = klass.__dict__["replace"]
            break
    assert isinstance(descriptor, property)

def test_project_shift_has_id():
    assert hasattr(project_Shift, "id")
    descriptor = None
    for klass in project_Shift.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_project_shift_has_name():
    assert hasattr(project_Shift, "name")
    descriptor = None
    for klass in project_Shift.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project_shift_has_timezone():
    assert hasattr(project_Shift, "timezone")
    descriptor = None
    for klass in project_Shift.__mro__:
        if "timezone" in klass.__dict__:
            descriptor = klass.__dict__["timezone"]
            break
    assert isinstance(descriptor, property)



def test_project_includeproperties_is_not_abstract():
    assert not inspect.isabstract(project_IncludeProperties)


def test_project_includeproperties_constructor_exists():
    assert callable(project_IncludeProperties.__init__)


def test_project_includeproperties_constructor_args():
    sig = inspect.signature(project_IncludeProperties.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_project_includeproperties_has_importURI():
    assert hasattr(project_IncludeProperties, "importURI")
    descriptor = None
    for klass in project_IncludeProperties.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_project_task_is_not_abstract():
    assert not inspect.isabstract(project_Task)


def test_project_task_constructor_exists():
    assert callable(project_Task.__init__)


def test_project_task_constructor_args():
    sig = inspect.signature(project_Task.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_project_task_has_id():
    assert hasattr(project_Task, "id")
    descriptor = None
    for klass in project_Task.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_project_task_has_name():
    assert hasattr(project_Task, "name")
    descriptor = None
    for klass in project_Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_project_projectids_is_not_abstract():
    assert not inspect.isabstract(project_ProjectIds)


def test_project_projectids_constructor_exists():
    assert callable(project_ProjectIds.__init__)


def test_project_projectids_constructor_args():
    sig = inspect.signature(project_ProjectIds.__init__)
    params = list(sig.parameters.keys())
    assert "ids" in params, "Missing parameter 'ids'"

def test_project_projectids_has_ids():
    assert hasattr(project_ProjectIds, "ids")
    descriptor = None
    for klass in project_ProjectIds.__mro__:
        if "ids" in klass.__dict__:
            descriptor = klass.__dict__["ids"]
            break
    assert isinstance(descriptor, property)



def test_project_resourcereport_is_not_abstract():
    assert not inspect.isabstract(project_ResourceReport)


def test_project_resourcereport_constructor_exists():
    assert callable(project_ResourceReport.__init__)


def test_project_resourcereport_constructor_args():
    sig = inspect.signature(project_ResourceReport.__init__)
    params = list(sig.parameters.keys())



def test_project_taskreport_is_not_abstract():
    assert not inspect.isabstract(project_TaskReport)


def test_project_taskreport_constructor_exists():
    assert callable(project_TaskReport.__init__)


def test_project_taskreport_constructor_args():
    sig = inspect.signature(project_TaskReport.__init__)
    params = list(sig.parameters.keys())



def test_project_supplementtask_is_not_abstract():
    assert not inspect.isabstract(project_SupplementTask)


def test_project_supplementtask_constructor_exists():
    assert callable(project_SupplementTask.__init__)


def test_project_supplementtask_constructor_args():
    sig = inspect.signature(project_SupplementTask.__init__)
    params = list(sig.parameters.keys())



def test_project_balance_is_not_abstract():
    assert not inspect.isabstract(project_Balance)


def test_project_balance_constructor_exists():
    assert callable(project_Balance.__init__)


def test_project_balance_constructor_args():
    sig = inspect.signature(project_Balance.__init__)
    params = list(sig.parameters.keys())



def test_project_tagfile_is_not_abstract():
    assert not inspect.isabstract(project_TagFile)


def test_project_tagfile_constructor_exists():
    assert callable(project_TagFile.__init__)


def test_project_tagfile_constructor_args():
    sig = inspect.signature(project_TagFile.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"
    assert "id" in params, "Missing parameter 'id'"

def test_project_tagfile_has_filename():
    assert hasattr(project_TagFile, "filename")
    descriptor = None
    for klass in project_TagFile.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_project_tagfile_has_id():
    assert hasattr(project_TagFile, "id")
    descriptor = None
    for klass in project_TagFile.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_project_account_is_not_abstract():
    assert not inspect.isabstract(project_Account)


def test_project_account_constructor_exists():
    assert callable(project_Account.__init__)


def test_project_account_constructor_args():
    sig = inspect.signature(project_Account.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_project_account_has_name():
    assert hasattr(project_Account, "name")
    descriptor = None
    for klass in project_Account.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project_account_has_id():
    assert hasattr(project_Account, "id")
    descriptor = None
    for klass in project_Account.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_project_property_is_not_abstract():
    assert not inspect.isabstract(project_Property)


def test_project_property_constructor_exists():
    assert callable(project_Property.__init__)


def test_project_property_constructor_args():
    sig = inspect.signature(project_Property.__init__)
    params = list(sig.parameters.keys())



def test_project_project_is_not_abstract():
    assert not inspect.isabstract(project_Project)


def test_project_project_constructor_exists():
    assert callable(project_Project.__init__)


def test_project_project_constructor_args():
    sig = inspect.signature(project_Project.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"

def test_project_project_has_id():
    assert hasattr(project_Project, "id")
    descriptor = None
    for klass in project_Project.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_project_project_has_name():
    assert hasattr(project_Project, "name")
    descriptor = None
    for klass in project_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project_project_has_version():
    assert hasattr(project_Project, "version")
    descriptor = None
    for klass in project_Project.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_criteriondirection_exists():
    # Check that the Enumeration exists
    assert CriterionDirection is not None

def test_criteriondirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CriterionDirection]
    expected_literals = [
        "DOWN",
        "UP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CriterionDirection"

def test_columnid_exists():
    # Check that the Enumeration exists
    assert ColumnId is not None

def test_columnid_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColumnId]
    expected_literals = [
        "RESOURCES",
        "ALERT",
        "FREEWORK",
        "MAXEND",
        "HIERARCHINDEX",
        "YEARLY",
        "REVENUE",
        "LINE",
        "NAME",
        "PATHCRITICALNESS",
        "DUTIES",
        "SEQNO",
        "PRIORITY",
        "WEEKLY",
        "EFFICIENCY",
        "STATUS",
        "CRITICALNESS",
        "INDEX",
        "COMPLETE",
        "CHART",
        "JOURNAL",
        "NO",
        "NOTE",
        "MINEND",
        "WBS",
        "EFFORT",
        "FREETIME",
        "MONTHLY",
        "FLAGS",
        "EMAIL",
        "EFFORTDONE",
        "HEADCOUNT",
        "FOLLOWERS",
        "HOURLY",
        "FTE",
        "END",
        "MINSTART",
        "ALERTTREND",
        "QUARTERLY",
        "START",
        "PRECURSOR",
        "RESPONSIBLE",
        "RATE",
        "SCENARIO",
        "DURATION",
        "TARGETS",
        "DAILY",
        "EFFORTLEFT",
        "ID",
        "MAXSTART",
        "COMPLETED",
        "ALERTSUMMARY",
        "COST",
        "ALERTMESSAGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColumnId"

def test_weekday_exists():
    # Check that the Enumeration exists
    assert Weekday is not None

def test_weekday_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Weekday]
    expected_literals = [
        "MON",
        "SAT",
        "TUE",
        "THR",
        "WED",
        "FRI",
        "SUN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Weekday"

def test_loaddisplayunit_exists():
    # Check that the Enumeration exists
    assert LoadDisplayUnit is not None

def test_loaddisplayunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LoadDisplayUnit]
    expected_literals = [
        "SHORTAUTO",
        "MINUTES",
        "LONGAUTO",
        "WEEKS",
        "MONTHS",
        "YEARS",
        "DAYS",
        "HOURS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LoadDisplayUnit"

def test_selectargument_exists():
    # Check that the Enumeration exists
    assert SelectArgument is not None

def test_selectargument_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SelectArgument]
    expected_literals = [
        "MINALLOCATED",
        "MINLOADED",
        "RANDOM",
        "ORDER",
        "MAXLOADED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SelectArgument"

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "YEAR",
        "MONTH",
        "DAY",
        "WEEK",
        "HOUR",
        "MINUTE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnit"

def test_listtypevalues_exists():
    # Check that the Enumeration exists
    assert ListTypeValues is not None

def test_listtypevalues_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ListTypeValues]
    expected_literals = [
        "COMMA",
        "NUMBERED",
        "BULLETS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ListTypeValues"

def test_yesno_exists():
    # Check that the Enumeration exists
    assert YesNo is not None

def test_yesno_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in YesNo]
    expected_literals = [
        "YES",
        "NO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in YesNo"

def test_justification_exists():
    # Check that the Enumeration exists
    assert Justification is not None

def test_justification_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Justification]
    expected_literals = [
        "LEFT",
        "CENTER",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Justification"

def test_purgeresourceattribute_exists():
    # Check that the Enumeration exists
    assert PurgeResourceAttribute is not None

def test_purgeresourceattribute_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PurgeResourceAttribute]
    expected_literals = [
        "REPORTS",
        "FAIL",
        "MANAGERS",
        "VACATIONS",
        "WARN",
        "FLAGS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PurgeResourceAttribute"

def test_scaleresolution_exists():
    # Check that the Enumeration exists
    assert ScaleResolution is not None

def test_scaleresolution_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScaleResolution]
    expected_literals = [
        "HOUR",
        "WEEK",
        "DAY",
        "YEAR",
        "QUARTER",
        "MONTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScaleResolution"

def test_reportformat_exists():
    # Check that the Enumeration exists
    assert ReportFormat is not None

def test_reportformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReportFormat]
    expected_literals = [
        "HTML",
        "NIKU",
        "CSV",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReportFormat"

def test_schedulingpolicy_exists():
    # Check that the Enumeration exists
    assert SchedulingPolicy is not None

def test_schedulingpolicy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SchedulingPolicy]
    expected_literals = [
        "ASAP",
        "ALAP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SchedulingPolicy"

def test_workquantityunit_exists():
    # Check that the Enumeration exists
    assert WorkQuantityUnit is not None

def test_workquantityunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkQuantityUnit]
    expected_literals = [
        "HOURS",
        "DAYS",
        "PERCENT",
        "MINUTES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkQuantityUnit"

def test_journalentrysortcriterion_exists():
    # Check that the Enumeration exists
    assert JournalEntrySortCriterion is not None

def test_journalentrysortcriterion_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JournalEntrySortCriterion]
    expected_literals = [
        "DATE_UP",
        "ALERT_DOWN",
        "PROPERTY_UP",
        "DATE_DOWN",
        "ALERT_UP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JournalEntrySortCriterion"

def test_alertlevel_exists():
    # Check that the Enumeration exists
    assert AlertLevel is not None

def test_alertlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlertLevel]
    expected_literals = [
        "RED",
        "GREEN",
        "YELLOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlertLevel"

def test_purgereportattribute_exists():
    # Check that the Enumeration exists
    assert PurgeReportAttribute is not None

def test_purgereportattribute_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PurgeReportAttribute]
    expected_literals = [
        "SORTJOURNALENTRIES",
        "DEFINITIONS",
        "SORTRESOURCES",
        "SORTACCOUNTS",
        "JOURNALATTRIBUTES",
        "FLAGS",
        "FORMATS",
        "COLUMNS",
        "SCENARIOS",
        "SORTTASKS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PurgeReportAttribute"

def test_chargeapplies_exists():
    # Check that the Enumeration exists
    assert ChargeApplies is not None

def test_chargeapplies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ChargeApplies]
    expected_literals = [
        "PERHOUR",
        "PERDAY",
        "PERWEEK",
        "ONEND",
        "ONSTART",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ChargeApplies"

def test_purgetaskattribute_exists():
    # Check that the Enumeration exists
    assert PurgeTaskAttribute is not None

def test_purgetaskattribute_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PurgeTaskAttribute]
    expected_literals = [
        "CHARGESET",
        "BOOKING",
        "FAIL",
        "CHARGE",
        "PRECEDES",
        "WARN",
        "DEPENDS",
        "FLAGS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PurgeTaskAttribute"

def test_journalmodevalue_exists():
    # Check that the Enumeration exists
    assert JournalModeValue is not None

def test_journalmodevalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JournalModeValue]
    expected_literals = [
        "JOURNAL",
        "STATUS_UP",
        "ALERTS_DOWN",
        "STATUS_DOWN",
        "JOURNAL_SUB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JournalModeValue"

def test_dependspolicy_exists():
    # Check that the Enumeration exists
    assert DependsPolicy is not None

def test_dependspolicy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DependsPolicy]
    expected_literals = [
        "ONSTART",
        "ONEND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DependsPolicy"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
GapDuration_strategy = st.builds(
    GapDuration,
)
project_LimitAttribute_strategy = st.builds(
    project_LimitAttribute,
    end=
        safe_text,
    start=
        safe_text
)
WeeklyMin_strategy = st.builds(
    WeeklyMin,
)
project_ColumnAttribute_strategy = st.builds(
    project_ColumnAttribute,
)
project_WorkHours_strategy = st.builds(
    project_WorkHours,
    start=
        safe_text,
    stop=
        safe_text
)
project_Weekdays_strategy = st.builds(
    project_Weekdays,
    first=
        safe_text,
    last=
        safe_text
)
project_TreeLevel_strategy = st.builds(
    project_TreeLevel,
    level=
        safe_text
)
project_TimesheetReportAttribute_strategy = st.builds(
    project_TimesheetReportAttribute,
)
project_TimesheetAttribute_strategy = st.builds(
    project_TimesheetAttribute,
)
StatusSheetAttribute_strategy = st.builds(
    StatusSheetAttribute,
)
project_TaskTimesheetAttribute_strategy = st.builds(
    project_TaskTimesheetAttribute,
)
project_TaskStatusSheetAttribute_strategy = st.builds(
    project_TaskStatusSheetAttribute,
)
project_StatusSheetReportAttribute_strategy = st.builds(
    project_StatusSheetReportAttribute,
)
project_StatusSheetAttribute_strategy = st.builds(
    project_StatusSheetAttribute,
)
project_StatusTimesheetAttribute_strategy = st.builds(
    project_StatusTimesheetAttribute,
)
project_Criterion_strategy = st.builds(
    project_Criterion,
    direction=
        safe_text,
    columnId=
        safe_text
)
SortTasks_strategy = st.builds(
    SortTasks,
)
SortResources_strategy = st.builds(
    SortResources,
)
SortJournalEntries_strategy = st.builds(
    SortJournalEntries,
)
SortAccounts_strategy = st.builds(
    SortAccounts,
)
project_Sort_strategy = st.builds(
    project_Sort,
    tree=
        st.booleans()
)
project_StatusStatusSheetAttribute_strategy = st.builds(
    project_StatusStatusSheetAttribute,
)
TaskStatusSheetAttribute_strategy = st.builds(
    TaskStatusSheetAttribute,
)
project_TaskStatusSheet_strategy = st.builds(
    project_TaskStatusSheet,
)
project_StatusStatusSheet_strategy = st.builds(
    project_StatusStatusSheet,
    level=
        safe_text,
    text=
        safe_text
)
project_ShiftsLimit_strategy = st.builds(
    project_ShiftsLimit,
)
ShiftsTask_strategy = st.builds(
    ShiftsTask,
)
ShiftsResource_strategy = st.builds(
    ShiftsResource,
)
project_Shifts_strategy = st.builds(
    project_Shifts,
)
project_JvmIdentifiableElement_strategy = st.builds(
    project_JvmIdentifiableElement,
)
LogicalExpression_strategy = st.builds(
    LogicalExpression,
)
project_LogicalDateLiteral_strategy = st.builds(
    project_LogicalDateLiteral,
    value=
        safe_text
)
project_LogicalStringLiteral_strategy = st.builds(
    project_LogicalStringLiteral,
    value=
        safe_text
)
project_LogicalBooleanLiteral_strategy = st.builds(
    project_LogicalBooleanLiteral,
    isTrue=
        st.booleans()
)
project_LogicalNumeralLiteral_strategy = st.builds(
    project_LogicalNumeralLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project_LogicalFunctionExpression_strategy = st.builds(
    project_LogicalFunctionExpression,
)
project_LogicalAbsoluteIdExression_strategy = st.builds(
    project_LogicalAbsoluteIdExression,
    value=
        safe_text
)
project_XBinaryOperation_strategy = st.builds(
    project_XBinaryOperation,
)
Definitions_strategy = st.builds(
    Definitions,
)
project_Defintions_strategy = st.builds(
    project_Defintions,
    projectids=
        st.booleans(),
    project=
        st.booleans(),
    tasks=
        st.booleans(),
    resources=
        st.booleans(),
    flags=
        st.booleans()
)
Header_strategy = st.builds(
    Header,
)
Footer_strategy = st.builds(
    Footer,
)
Epilog_strategy = st.builds(
    Epilog,
)
Details_strategy = st.builds(
    Details,
)
Center_strategy = st.builds(
    Center,
)
Caption_strategy = st.builds(
    Caption,
)
Summary_strategy = st.builds(
    Summary,
)
Right_strategy = st.builds(
    Right,
)
Prolog_strategy = st.builds(
    Prolog,
)
ListItem_strategy = st.builds(
    ListItem,
)
Left_strategy = st.builds(
    Left,
)
Headline_strategy = st.builds(
    Headline,
)
project_RichText_strategy = st.builds(
    project_RichText,
    text=
        safe_text
)
Precedes_strategy = st.builds(
    Precedes,
)
Depends_strategy = st.builds(
    Depends,
)
project_TaskDependency_strategy = st.builds(
    project_TaskDependency,
    policy=
        safe_text
)
NumberFormat_strategy = st.builds(
    NumberFormat,
)
CurrencyFormat_strategy = st.builds(
    CurrencyFormat,
)
project_RealFormat_strategy = st.builds(
    project_RealFormat,
    fractionSeparator=
        safe_text,
    negativePrefix=
        safe_text,
    thousandsSeparator=
        safe_text,
    negativeSuffix=
        safe_text,
    fractionDigits=
        st.integers()
)
WeeklyMax_strategy = st.builds(
    WeeklyMax,
)
MonthlyMin_strategy = st.builds(
    MonthlyMin,
)
MonthlyMax_strategy = st.builds(
    MonthlyMax,
)
Minimum_strategy = st.builds(
    Minimum,
)
Maximum_strategy = st.builds(
    Maximum,
)
DailyMin_strategy = st.builds(
    DailyMin,
)
DailyMax_strategy = st.builds(
    DailyMax,
)
project_Limit_strategy = st.builds(
    project_Limit,
)
GapLength_strategy = st.builds(
    GapLength,
)
project_LimitsAttribute_strategy = st.builds(
    project_LimitsAttribute,
)
project_Interval3_strategy = st.builds(
    project_Interval3,
    end=
        safe_text,
    start=
        safe_text
)
project_Interval1_strategy = st.builds(
    project_Interval1,
    end=
        safe_text,
    start=
        safe_text
)
project_IncludePropertiesAttribute_strategy = st.builds(
    project_IncludePropertiesAttribute,
)
project_Function_strategy = st.builds(
    project_Function,
    distance=
        st.integers(),
    level=
        st.integers(),
    parentId=
        safe_text,
    date=
        safe_text
)
NavigatorAttribute_strategy = st.builds(
    NavigatorAttribute,
)
project_HideReport_strategy = st.builds(
    project_HideReport,
)
project_GapLength_strategy = st.builds(
    project_GapLength,
)
project_GapDuration_strategy = st.builds(
    project_GapDuration,
)
project_Extend_strategy = st.builds(
    project_Extend,
    scenariospecific=
        st.booleans(),
    name=
        safe_text,
    inherit=
        st.booleans(),
    id=
        safe_text
)
ExportAttribute_strategy = st.builds(
    ExportAttribute,
)
project_ResourceAttributes_strategy = st.builds(
    project_ResourceAttributes,
    none=
        st.booleans(),
    vacation=
        st.booleans(),
    workingHours=
        st.booleans(),
    all=
        st.booleans(),
    booking=
        st.booleans()
)
project_TaskAttributes_strategy = st.builds(
    project_TaskAttributes,
    minstart=
        st.booleans(),
    booking=
        st.booleans(),
    complete=
        st.booleans(),
    minend=
        st.booleans(),
    none=
        st.booleans(),
    flags=
        st.booleans(),
    depends=
        st.booleans(),
    priority=
        st.booleans(),
    all=
        st.booleans(),
    responsible=
        st.booleans(),
    maxend=
        st.booleans(),
    maxstart=
        st.booleans(),
    note=
        st.booleans()
)
project_Definitions_strategy = st.builds(
    project_Definitions,
    none=
        st.booleans(),
    all=
        st.booleans()
)
LimitsAttribute_strategy = st.builds(
    LimitsAttribute,
)
project_DailyMin_strategy = st.builds(
    project_DailyMin,
)
project_WeeklyMax_strategy = st.builds(
    project_WeeklyMax,
)
project_Minimum_strategy = st.builds(
    project_Minimum,
)
project_Maximum_strategy = st.builds(
    project_Maximum,
)
project_MonthlyMin_strategy = st.builds(
    project_MonthlyMin,
)
project_MonthlyMax_strategy = st.builds(
    project_MonthlyMax,
)
project_WeeklyMin_strategy = st.builds(
    project_WeeklyMin,
)
project_DailyMax_strategy = st.builds(
    project_DailyMax,
)
ProjectAttribute_strategy = st.builds(
    ProjectAttribute,
)
project_TrackingScenario_strategy = st.builds(
    project_TrackingScenario,
)
project_TimingResolution_strategy = st.builds(
    project_TimingResolution,
    timingResolution=
        st.integers()
)
project_DailyWorkingHours_strategy = st.builds(
    project_DailyWorkingHours,
    dailyWorkingHours=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project_WeekStarts_strategy = st.builds(
    project_WeekStarts,
    monday=
        st.booleans(),
    sunday=
        st.booleans()
)
project_Scenario_strategy = st.builds(
    project_Scenario,
    active=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
project_ExtendResource_strategy = st.builds(
    project_ExtendResource,
)
project_ExtendTask_strategy = st.builds(
    project_ExtendTask,
)
project_ShortTimeFormat_strategy = st.builds(
    project_ShortTimeFormat,
    shortTimeFormat=
        safe_text
)
project_YearlyWorkingDays_strategy = st.builds(
    project_YearlyWorkingDays,
    yearlyWorkingDays=
        st.integers()
)
project_Include_strategy = st.builds(
    project_Include,
    importURI=
        safe_text
)
project_Now_strategy = st.builds(
    project_Now,
    now=
        safe_text
)
project_Currency_strategy = st.builds(
    project_Currency,
    currency=
        safe_text
)
TimesheetReportAttribute_strategy = st.builds(
    TimesheetReportAttribute,
)
TaskTimesheetAttribute_strategy = st.builds(
    TaskTimesheetAttribute,
)
StatusSheetReportAttribute_strategy = st.builds(
    StatusSheetReportAttribute,
)
NikuReportAttribute_strategy = st.builds(
    NikuReportAttribute,
)
project_Timeoff_strategy = st.builds(
    project_Timeoff,
    name=
        safe_text,
    id=
        safe_text
)
NewTaskAttribute_strategy = st.builds(
    NewTaskAttribute,
)
project_Work_strategy = st.builds(
    project_Work,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    unit=
        safe_text
)
project_Remaining_strategy = st.builds(
    project_Remaining,
)
IcalReportAttribute_strategy = st.builds(
    IcalReportAttribute,
)
project_ScenarioIcal_strategy = st.builds(
    project_ScenarioIcal,
)
project_DurationQuantity_strategy = st.builds(
    project_DurationQuantity,
    unit=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
StatusTimesheetAttribute_strategy = st.builds(
    StatusTimesheetAttribute,
)
project_RGB_strategy = st.builds(
    project_RGB,
    value=
        safe_text
)
project_LogicalExpression_strategy = st.builds(
    project_LogicalExpression,
)
ColumnAttribute_strategy = st.builds(
    ColumnAttribute,
)
project_CellText_strategy = st.builds(
    project_CellText,
    text=
        safe_text
)
project_Width_strategy = st.builds(
    project_Width,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project_FontColor_strategy = st.builds(
    project_FontColor,
    color=
        safe_text
)
project_ToolTip_strategy = st.builds(
    project_ToolTip,
    tip=
        safe_text
)
project_ListType_strategy = st.builds(
    project_ListType,
    type=
        safe_text
)
project_ListItem_strategy = st.builds(
    project_ListItem,
)
project_HAlign_strategy = st.builds(
    project_HAlign,
    justification=
        safe_text
)
project_Scale_strategy = st.builds(
    project_Scale,
    scale=
        safe_text
)
project_CellColor_strategy = st.builds(
    project_CellColor,
)
project_Column_strategy = st.builds(
    project_Column,
    id=
        safe_text
)
project_AccountShare_strategy = st.builds(
    project_AccountShare,
    share=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
StatusStatusSheetAttribute_strategy = st.builds(
    StatusStatusSheetAttribute,
)
project_Summary_strategy = st.builds(
    project_Summary,
)
project_Details_strategy = st.builds(
    project_Details,
)
project_Author_strategy = st.builds(
    project_Author,
)
AllocateResourceAttribute_strategy = st.builds(
    AllocateResourceAttribute,
)
project_ShiftsAllocate_strategy = st.builds(
    project_ShiftsAllocate,
)
project_Mandatory_strategy = st.builds(
    project_Mandatory,
    mandatory=
        st.booleans()
)
project_Select_strategy = st.builds(
    project_Select,
    argument=
        safe_text
)
project_Persistent_strategy = st.builds(
    project_Persistent,
    persistent=
        st.booleans()
)
project_Alternative_strategy = st.builds(
    project_Alternative,
)
project_Alert_strategy = st.builds(
    project_Alert,
    level=
        safe_text
)
project_NikuReportAttribute_strategy = st.builds(
    project_NikuReportAttribute,
)
project_Interval4_strategy = st.builds(
    project_Interval4,
    start=
        safe_text,
    end=
        safe_text
)
project_Booking_strategy = st.builds(
    project_Booking,
    sloppy=
        st.integers(),
    overtime=
        st.integers()
)
project_AllocateResourceAttribute_strategy = st.builds(
    project_AllocateResourceAttribute,
)
project_AllocateResource_strategy = st.builds(
    project_AllocateResource,
)
project_NewTaskAttribute_strategy = st.builds(
    project_NewTaskAttribute,
)
TimesheetAttribute_strategy = st.builds(
    TimesheetAttribute,
)
project_ShiftTimesheet_strategy = st.builds(
    project_ShiftTimesheet,
)
project_TaskTimesheet_strategy = st.builds(
    project_TaskTimesheet,
)
project_StatusTimesheet_strategy = st.builds(
    project_StatusTimesheet,
    text=
        safe_text,
    level=
        safe_text
)
project_NewTask_strategy = st.builds(
    project_NewTask,
    text=
        safe_text,
    id=
        safe_text
)
project_NavigatorAttribute_strategy = st.builds(
    project_NavigatorAttribute,
)
project_ReportAttribute_strategy = st.builds(
    project_ReportAttribute,
)
project_ResourceAttribute_strategy = st.builds(
    project_ResourceAttribute,
)
ResourceAttribute_strategy = st.builds(
    ResourceAttribute,
)
project_Email_strategy = st.builds(
    project_Email,
    address=
        safe_text
)
project_ShiftsResource_strategy = st.builds(
    project_ShiftsResource,
)
project_WorkingHours_strategy = st.builds(
    project_WorkingHours,
    off=
        st.booleans()
)
project_ExtendedResourceAttribute_strategy = st.builds(
    project_ExtendedResourceAttribute,
    value=
        safe_text
)
project_PurgeResource_strategy = st.builds(
    project_PurgeResource,
    listAttribute=
        safe_text
)
project_Managers_strategy = st.builds(
    project_Managers,
)
project_Efficiency_strategy = st.builds(
    project_Efficiency,
    efficiency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project_BookingResource_strategy = st.builds(
    project_BookingResource,
)
project_ExportAttribute_strategy = st.builds(
    project_ExportAttribute,
)
project_IcalReportAttribute_strategy = st.builds(
    project_IcalReportAttribute,
)
ReportAttribute_strategy = st.builds(
    ReportAttribute,
)
project_HideTask_strategy = st.builds(
    project_HideTask,
)
project_Formats_strategy = st.builds(
    project_Formats,
    formats=
        safe_text
)
project_Left_strategy = st.builds(
    project_Left,
)
project_HideAccount_strategy = st.builds(
    project_HideAccount,
    expression=
        safe_text
)
project_SortJournalEntries_strategy = st.builds(
    project_SortJournalEntries,
)
project_Title_strategy = st.builds(
    project_Title,
    title=
        safe_text
)
project_Right_strategy = st.builds(
    project_Right,
)
project_Prolog_strategy = st.builds(
    project_Prolog,
)
project_SelfContained_strategy = st.builds(
    project_SelfContained,
    selfcontained=
        safe_text
)
project_RollupAccount_strategy = st.builds(
    project_RollupAccount,
)
project_AccountRoot_strategy = st.builds(
    project_AccountRoot,
)
project_Epilog_strategy = st.builds(
    project_Epilog,
)
project_RollupResource_strategy = st.builds(
    project_RollupResource,
)
project_HideJournalEntry_strategy = st.builds(
    project_HideJournalEntry,
    expression=
        safe_text
)
project_HideResource_strategy = st.builds(
    project_HideResource,
)
project_Headline_strategy = st.builds(
    project_Headline,
)
project_Footer_strategy = st.builds(
    project_Footer,
)
project_Timezone_strategy = st.builds(
    project_Timezone,
    timezone=
        safe_text
)
project_TaskRoot_strategy = st.builds(
    project_TaskRoot,
)
project_SortResources_strategy = st.builds(
    project_SortResources,
)
project_NumberFormat_strategy = st.builds(
    project_NumberFormat,
)
project_PurgeReport_strategy = st.builds(
    project_PurgeReport,
    listAttribute=
        safe_text
)
project_Scenarios_strategy = st.builds(
    project_Scenarios,
)
project_CurrencyFormat_strategy = st.builds(
    project_CurrencyFormat,
)
project_TimeFormat_strategy = st.builds(
    project_TimeFormat,
    timeformat=
        safe_text
)
project_SortAccounts_strategy = st.builds(
    project_SortAccounts,
)
project_JournalAttributes_strategy = st.builds(
    project_JournalAttributes,
    propertyid=
        st.booleans(),
    all=
        st.booleans(),
    none=
        st.booleans(),
    summary=
        st.booleans(),
    author=
        st.booleans(),
    _property=
        st.booleans(),
    details=
        st.booleans(),
    flags=
        st.booleans(),
    date=
        st.booleans(),
    headline=
        st.booleans(),
    timesheet=
        st.booleans()
)
project_Center_strategy = st.builds(
    project_Center,
)
project_ResourceRoot_strategy = st.builds(
    project_ResourceRoot,
)
project_RollupTask_strategy = st.builds(
    project_RollupTask,
)
project_LoadUnit_strategy = st.builds(
    project_LoadUnit,
    unit=
        safe_text
)
project_Columns_strategy = st.builds(
    project_Columns,
)
project_Caption_strategy = st.builds(
    project_Caption,
)
project_Header_strategy = st.builds(
    project_Header,
)
project_JournalMode_strategy = st.builds(
    project_JournalMode,
    mode=
        safe_text
)
project_SortTasks_strategy = st.builds(
    project_SortTasks,
)
TextReport_strategy = st.builds(
    TextReport,
)
TaskReport_strategy = st.builds(
    TaskReport,
)
ResourceReport_strategy = st.builds(
    ResourceReport,
)
AccountReport_strategy = st.builds(
    AccountReport,
)
project_Report_strategy = st.builds(
    project_Report,
    id=
        safe_text,
    name=
        safe_text
)
project_TaskAttribute_strategy = st.builds(
    project_TaskAttribute,
)
TaskAttribute_strategy = st.builds(
    TaskAttribute,
)
project_Note_strategy = st.builds(
    project_Note,
    note=
        safe_text
)
project_ShiftsTask_strategy = st.builds(
    project_ShiftsTask,
)
project_Period_strategy = st.builds(
    project_Period,
)
project_Priority_strategy = st.builds(
    project_Priority,
    priority=
        st.integers()
)
project_Warn_strategy = st.builds(
    project_Warn,
)
project_Charge_strategy = st.builds(
    project_Charge,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    applies=
        safe_text
)
project_Scheduled_strategy = st.builds(
    project_Scheduled,
    scheduled=
        st.booleans()
)
project_Start_strategy = st.builds(
    project_Start,
    start=
        safe_text
)
project_End_strategy = st.builds(
    project_End,
    end=
        safe_text
)
project_MinEnd_strategy = st.builds(
    project_MinEnd,
    minEnd=
        safe_text
)
project_Allocate_strategy = st.builds(
    project_Allocate,
)
project_Length_strategy = st.builds(
    project_Length,
)
project_MinStart_strategy = st.builds(
    project_MinStart,
    minStart=
        safe_text
)
project_Duration_strategy = st.builds(
    project_Duration,
)
project_Complete_strategy = st.builds(
    project_Complete,
    complete=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project_EndCredit_strategy = st.builds(
    project_EndCredit,
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project_Effort_strategy = st.builds(
    project_Effort,
)
project_JournalEntry_strategy = st.builds(
    project_JournalEntry,
    headline=
        safe_text,
    date=
        safe_text
)
project_PurgeTask_strategy = st.builds(
    project_PurgeTask,
    listAttribute=
        safe_text
)
project_BookingTask_strategy = st.builds(
    project_BookingTask,
)
project_ChargeSet_strategy = st.builds(
    project_ChargeSet,
)
project_MaxEnd_strategy = st.builds(
    project_MaxEnd,
    maxEnd=
        safe_text
)
project_Milestone_strategy = st.builds(
    project_Milestone,
    milestone=
        st.booleans()
)
project_Scheduling_strategy = st.builds(
    project_Scheduling,
    scheduling=
        safe_text
)
project_Precedes_strategy = st.builds(
    project_Precedes,
)
project_Depends_strategy = st.builds(
    project_Depends,
)
project_Fail_strategy = st.builds(
    project_Fail,
)
project_ProjectId_strategy = st.builds(
    project_ProjectId,
    projectId=
        safe_text
)
project_ExtendedTaskAttribute_strategy = st.builds(
    project_ExtendedTaskAttribute,
    value=
        safe_text
)
project_MaxStart_strategy = st.builds(
    project_MaxStart,
    maxStart=
        safe_text
)
project_Responsible_strategy = st.builds(
    project_Responsible,
)
project_ProjectAttribute_strategy = st.builds(
    project_ProjectAttribute,
)
project_Interval2_strategy = st.builds(
    project_Interval2,
    end=
        safe_text,
    start=
        safe_text
)
project_Global_strategy = st.builds(
    project_Global,
)
IncludePropertiesAttribute_strategy = st.builds(
    IncludePropertiesAttribute,
)
project_TaskPrefix_strategy = st.builds(
    project_TaskPrefix,
)
project_ReportPrefix_strategy = st.builds(
    project_ReportPrefix,
)
project_ResourcePrefix_strategy = st.builds(
    project_ResourcePrefix,
)
project_AccountPrefix_strategy = st.builds(
    project_AccountPrefix,
)
project_AccountAttribute_strategy = st.builds(
    project_AccountAttribute,
)
AccountAttribute_strategy = st.builds(
    AccountAttribute,
)
project_Credit_strategy = st.builds(
    project_Credit,
    description=
        safe_text,
    date=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Property_strategy = st.builds(
    Property,
)
project_AccountReport_strategy = st.builds(
    project_AccountReport,
)
project_SupplementAccount_strategy = st.builds(
    project_SupplementAccount,
)
project_StatusSheet_strategy = st.builds(
    project_StatusSheet,
)
project_Flags_strategy = st.builds(
    project_Flags,
    flags=
        safe_text
)
project_Navigator_strategy = st.builds(
    project_Navigator,
    id=
        safe_text
)
project_TimesheetReport_strategy = st.builds(
    project_TimesheetReport,
    filename=
        safe_text
)
project_StatusSheetReport_strategy = st.builds(
    project_StatusSheetReport,
    filename=
        safe_text
)
project_Vacation_strategy = st.builds(
    project_Vacation,
    name=
        safe_text
)
project_Rate_strategy = st.builds(
    project_Rate,
    rate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project_Macro_strategy = st.builds(
    project_Macro,
    value=
        safe_text
)
project_NikuReport_strategy = st.builds(
    project_NikuReport,
    filename=
        safe_text
)
project_TextReport_strategy = st.builds(
    project_TextReport,
)
project_Resource_strategy = st.builds(
    project_Resource,
    id=
        safe_text,
    name=
        safe_text
)
project_Limits_strategy = st.builds(
    project_Limits,
)
project_IcalReport_strategy = st.builds(
    project_IcalReport,
    filename=
        safe_text
)
project_Export_strategy = st.builds(
    project_Export,
    id=
        safe_text,
    filename=
        safe_text
)
project_Timesheet_strategy = st.builds(
    project_Timesheet,
)
project_SupplementReport_strategy = st.builds(
    project_SupplementReport,
)
project_SupplementResource_strategy = st.builds(
    project_SupplementResource,
)
project_Copyright_strategy = st.builds(
    project_Copyright,
    text=
        safe_text
)
project_Shift_strategy = st.builds(
    project_Shift,
    replace=
        safe_text,
    id=
        safe_text,
    name=
        safe_text,
    timezone=
        safe_text
)
project_IncludeProperties_strategy = st.builds(
    project_IncludeProperties,
    importURI=
        safe_text
)
project_Task_strategy = st.builds(
    project_Task,
    id=
        safe_text,
    name=
        safe_text
)
project_ProjectIds_strategy = st.builds(
    project_ProjectIds,
    ids=
        safe_text
)
project_ResourceReport_strategy = st.builds(
    project_ResourceReport,
)
project_TaskReport_strategy = st.builds(
    project_TaskReport,
)
project_SupplementTask_strategy = st.builds(
    project_SupplementTask,
)
project_Balance_strategy = st.builds(
    project_Balance,
)
project_TagFile_strategy = st.builds(
    project_TagFile,
    filename=
        safe_text,
    id=
        safe_text
)
project_Account_strategy = st.builds(
    project_Account,
    name=
        safe_text,
    id=
        safe_text
)
project_Property_strategy = st.builds(
    project_Property,
)
project_Project_strategy = st.builds(
    project_Project,
    id=
        safe_text,
    name=
        safe_text,
    version=
        safe_text
)

@given(instance=GapDuration_strategy)
@settings(max_examples=50)
def test_gapduration_instantiation(instance):
    assert isinstance(instance, GapDuration)

@given(instance=project_LimitAttribute_strategy)
@settings(max_examples=50)
def test_project_limitattribute_instantiation(instance):
    assert isinstance(instance, project_LimitAttribute)



@given(instance=project_LimitAttribute_strategy)
def test_project_limitattribute_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=project_LimitAttribute_strategy)
def test_project_limitattribute_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=WeeklyMin_strategy)
@settings(max_examples=50)
def test_weeklymin_instantiation(instance):
    assert isinstance(instance, WeeklyMin)

@given(instance=project_ColumnAttribute_strategy)
@settings(max_examples=50)
def test_project_columnattribute_instantiation(instance):
    assert isinstance(instance, project_ColumnAttribute)

@given(instance=project_WorkHours_strategy)
@settings(max_examples=50)
def test_project_workhours_instantiation(instance):
    assert isinstance(instance, project_WorkHours)



@given(instance=project_WorkHours_strategy)
def test_project_workhours_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=project_WorkHours_strategy)
def test_project_workhours_stop_setter(instance):
    original = instance.stop
    instance.stop = original
    assert instance.stop == original

@given(instance=project_Weekdays_strategy)
@settings(max_examples=50)
def test_project_weekdays_instantiation(instance):
    assert isinstance(instance, project_Weekdays)



@given(instance=project_Weekdays_strategy)
def test_project_weekdays_first_setter(instance):
    original = instance.first
    instance.first = original
    assert instance.first == original



@given(instance=project_Weekdays_strategy)
def test_project_weekdays_last_setter(instance):
    original = instance.last
    instance.last = original
    assert instance.last == original

@given(instance=project_TreeLevel_strategy)
@settings(max_examples=50)
def test_project_treelevel_instantiation(instance):
    assert isinstance(instance, project_TreeLevel)



@given(instance=project_TreeLevel_strategy)
def test_project_treelevel_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=project_TimesheetReportAttribute_strategy)
@settings(max_examples=50)
def test_project_timesheetreportattribute_instantiation(instance):
    assert isinstance(instance, project_TimesheetReportAttribute)

@given(instance=project_TimesheetAttribute_strategy)
@settings(max_examples=50)
def test_project_timesheetattribute_instantiation(instance):
    assert isinstance(instance, project_TimesheetAttribute)

@given(instance=StatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_statussheetattribute_instantiation(instance):
    assert isinstance(instance, StatusSheetAttribute)

@given(instance=project_TaskTimesheetAttribute_strategy)
@settings(max_examples=50)
def test_project_tasktimesheetattribute_instantiation(instance):
    assert isinstance(instance, project_TaskTimesheetAttribute)

@given(instance=project_TaskStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_project_taskstatussheetattribute_instantiation(instance):
    assert isinstance(instance, project_TaskStatusSheetAttribute)

@given(instance=project_StatusSheetReportAttribute_strategy)
@settings(max_examples=50)
def test_project_statussheetreportattribute_instantiation(instance):
    assert isinstance(instance, project_StatusSheetReportAttribute)

@given(instance=project_StatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_project_statussheetattribute_instantiation(instance):
    assert isinstance(instance, project_StatusSheetAttribute)

@given(instance=project_StatusTimesheetAttribute_strategy)
@settings(max_examples=50)
def test_project_statustimesheetattribute_instantiation(instance):
    assert isinstance(instance, project_StatusTimesheetAttribute)

@given(instance=project_Criterion_strategy)
@settings(max_examples=50)
def test_project_criterion_instantiation(instance):
    assert isinstance(instance, project_Criterion)



@given(instance=project_Criterion_strategy)
def test_project_criterion_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=project_Criterion_strategy)
def test_project_criterion_columnId_setter(instance):
    original = instance.columnId
    instance.columnId = original
    assert instance.columnId == original

@given(instance=SortTasks_strategy)
@settings(max_examples=50)
def test_sorttasks_instantiation(instance):
    assert isinstance(instance, SortTasks)

@given(instance=SortResources_strategy)
@settings(max_examples=50)
def test_sortresources_instantiation(instance):
    assert isinstance(instance, SortResources)

@given(instance=SortJournalEntries_strategy)
@settings(max_examples=50)
def test_sortjournalentries_instantiation(instance):
    assert isinstance(instance, SortJournalEntries)

@given(instance=SortAccounts_strategy)
@settings(max_examples=50)
def test_sortaccounts_instantiation(instance):
    assert isinstance(instance, SortAccounts)

@given(instance=project_Sort_strategy)
@settings(max_examples=50)
def test_project_sort_instantiation(instance):
    assert isinstance(instance, project_Sort)



@given(instance=project_Sort_strategy)
def test_project_sort_tree_setter(instance):
    original = instance.tree
    instance.tree = original
    assert instance.tree == original

@given(instance=project_StatusStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_project_statusstatussheetattribute_instantiation(instance):
    assert isinstance(instance, project_StatusStatusSheetAttribute)

@given(instance=TaskStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_taskstatussheetattribute_instantiation(instance):
    assert isinstance(instance, TaskStatusSheetAttribute)

@given(instance=project_TaskStatusSheet_strategy)
@settings(max_examples=50)
def test_project_taskstatussheet_instantiation(instance):
    assert isinstance(instance, project_TaskStatusSheet)

@given(instance=project_StatusStatusSheet_strategy)
@settings(max_examples=50)
def test_project_statusstatussheet_instantiation(instance):
    assert isinstance(instance, project_StatusStatusSheet)



@given(instance=project_StatusStatusSheet_strategy)
def test_project_statusstatussheet_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=project_StatusStatusSheet_strategy)
def test_project_statusstatussheet_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=project_ShiftsLimit_strategy)
@settings(max_examples=50)
def test_project_shiftslimit_instantiation(instance):
    assert isinstance(instance, project_ShiftsLimit)

@given(instance=ShiftsTask_strategy)
@settings(max_examples=50)
def test_shiftstask_instantiation(instance):
    assert isinstance(instance, ShiftsTask)

@given(instance=ShiftsResource_strategy)
@settings(max_examples=50)
def test_shiftsresource_instantiation(instance):
    assert isinstance(instance, ShiftsResource)

@given(instance=project_Shifts_strategy)
@settings(max_examples=50)
def test_project_shifts_instantiation(instance):
    assert isinstance(instance, project_Shifts)

@given(instance=project_JvmIdentifiableElement_strategy)
@settings(max_examples=50)
def test_project_jvmidentifiableelement_instantiation(instance):
    assert isinstance(instance, project_JvmIdentifiableElement)

@given(instance=LogicalExpression_strategy)
@settings(max_examples=50)
def test_logicalexpression_instantiation(instance):
    assert isinstance(instance, LogicalExpression)

@given(instance=project_LogicalDateLiteral_strategy)
@settings(max_examples=50)
def test_project_logicaldateliteral_instantiation(instance):
    assert isinstance(instance, project_LogicalDateLiteral)



@given(instance=project_LogicalDateLiteral_strategy)
def test_project_logicaldateliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project_LogicalStringLiteral_strategy)
@settings(max_examples=50)
def test_project_logicalstringliteral_instantiation(instance):
    assert isinstance(instance, project_LogicalStringLiteral)



@given(instance=project_LogicalStringLiteral_strategy)
def test_project_logicalstringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project_LogicalBooleanLiteral_strategy)
@settings(max_examples=50)
def test_project_logicalbooleanliteral_instantiation(instance):
    assert isinstance(instance, project_LogicalBooleanLiteral)



@given(instance=project_LogicalBooleanLiteral_strategy)
def test_project_logicalbooleanliteral_isTrue_setter(instance):
    original = instance.isTrue
    instance.isTrue = original
    assert instance.isTrue == original

@given(instance=project_LogicalNumeralLiteral_strategy)
@settings(max_examples=50)
def test_project_logicalnumeralliteral_instantiation(instance):
    assert isinstance(instance, project_LogicalNumeralLiteral)



@given(instance=project_LogicalNumeralLiteral_strategy)
def test_project_logicalnumeralliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project_LogicalFunctionExpression_strategy)
@settings(max_examples=50)
def test_project_logicalfunctionexpression_instantiation(instance):
    assert isinstance(instance, project_LogicalFunctionExpression)

@given(instance=project_LogicalAbsoluteIdExression_strategy)
@settings(max_examples=50)
def test_project_logicalabsoluteidexression_instantiation(instance):
    assert isinstance(instance, project_LogicalAbsoluteIdExression)



@given(instance=project_LogicalAbsoluteIdExression_strategy)
def test_project_logicalabsoluteidexression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project_XBinaryOperation_strategy)
@settings(max_examples=50)
def test_project_xbinaryoperation_instantiation(instance):
    assert isinstance(instance, project_XBinaryOperation)

@given(instance=Definitions_strategy)
@settings(max_examples=50)
def test_definitions_instantiation(instance):
    assert isinstance(instance, Definitions)

@given(instance=project_Defintions_strategy)
@settings(max_examples=50)
def test_project_defintions_instantiation(instance):
    assert isinstance(instance, project_Defintions)



@given(instance=project_Defintions_strategy)
def test_project_defintions_projectids_setter(instance):
    original = instance.projectids
    instance.projectids = original
    assert instance.projectids == original



@given(instance=project_Defintions_strategy)
def test_project_defintions_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original



@given(instance=project_Defintions_strategy)
def test_project_defintions_tasks_setter(instance):
    original = instance.tasks
    instance.tasks = original
    assert instance.tasks == original



@given(instance=project_Defintions_strategy)
def test_project_defintions_resources_setter(instance):
    original = instance.resources
    instance.resources = original
    assert instance.resources == original



@given(instance=project_Defintions_strategy)
def test_project_defintions_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original

@given(instance=Header_strategy)
@settings(max_examples=50)
def test_header_instantiation(instance):
    assert isinstance(instance, Header)

@given(instance=Footer_strategy)
@settings(max_examples=50)
def test_footer_instantiation(instance):
    assert isinstance(instance, Footer)

@given(instance=Epilog_strategy)
@settings(max_examples=50)
def test_epilog_instantiation(instance):
    assert isinstance(instance, Epilog)

@given(instance=Details_strategy)
@settings(max_examples=50)
def test_details_instantiation(instance):
    assert isinstance(instance, Details)

@given(instance=Center_strategy)
@settings(max_examples=50)
def test_center_instantiation(instance):
    assert isinstance(instance, Center)

@given(instance=Caption_strategy)
@settings(max_examples=50)
def test_caption_instantiation(instance):
    assert isinstance(instance, Caption)

@given(instance=Summary_strategy)
@settings(max_examples=50)
def test_summary_instantiation(instance):
    assert isinstance(instance, Summary)

@given(instance=Right_strategy)
@settings(max_examples=50)
def test_right_instantiation(instance):
    assert isinstance(instance, Right)

@given(instance=Prolog_strategy)
@settings(max_examples=50)
def test_prolog_instantiation(instance):
    assert isinstance(instance, Prolog)

@given(instance=ListItem_strategy)
@settings(max_examples=50)
def test_listitem_instantiation(instance):
    assert isinstance(instance, ListItem)

@given(instance=Left_strategy)
@settings(max_examples=50)
def test_left_instantiation(instance):
    assert isinstance(instance, Left)

@given(instance=Headline_strategy)
@settings(max_examples=50)
def test_headline_instantiation(instance):
    assert isinstance(instance, Headline)

@given(instance=project_RichText_strategy)
@settings(max_examples=50)
def test_project_richtext_instantiation(instance):
    assert isinstance(instance, project_RichText)



@given(instance=project_RichText_strategy)
def test_project_richtext_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Precedes_strategy)
@settings(max_examples=50)
def test_precedes_instantiation(instance):
    assert isinstance(instance, Precedes)

@given(instance=Depends_strategy)
@settings(max_examples=50)
def test_depends_instantiation(instance):
    assert isinstance(instance, Depends)

@given(instance=project_TaskDependency_strategy)
@settings(max_examples=50)
def test_project_taskdependency_instantiation(instance):
    assert isinstance(instance, project_TaskDependency)



@given(instance=project_TaskDependency_strategy)
def test_project_taskdependency_policy_setter(instance):
    original = instance.policy
    instance.policy = original
    assert instance.policy == original

@given(instance=NumberFormat_strategy)
@settings(max_examples=50)
def test_numberformat_instantiation(instance):
    assert isinstance(instance, NumberFormat)

@given(instance=CurrencyFormat_strategy)
@settings(max_examples=50)
def test_currencyformat_instantiation(instance):
    assert isinstance(instance, CurrencyFormat)

@given(instance=project_RealFormat_strategy)
@settings(max_examples=50)
def test_project_realformat_instantiation(instance):
    assert isinstance(instance, project_RealFormat)



@given(instance=project_RealFormat_strategy)
def test_project_realformat_fractionSeparator_setter(instance):
    original = instance.fractionSeparator
    instance.fractionSeparator = original
    assert instance.fractionSeparator == original



@given(instance=project_RealFormat_strategy)
def test_project_realformat_negativePrefix_setter(instance):
    original = instance.negativePrefix
    instance.negativePrefix = original
    assert instance.negativePrefix == original



@given(instance=project_RealFormat_strategy)
def test_project_realformat_thousandsSeparator_setter(instance):
    original = instance.thousandsSeparator
    instance.thousandsSeparator = original
    assert instance.thousandsSeparator == original



@given(instance=project_RealFormat_strategy)
def test_project_realformat_negativeSuffix_setter(instance):
    original = instance.negativeSuffix
    instance.negativeSuffix = original
    assert instance.negativeSuffix == original



@given(instance=project_RealFormat_strategy)
def test_project_realformat_fractionDigits_setter(instance):
    original = instance.fractionDigits
    instance.fractionDigits = original
    assert instance.fractionDigits == original

@given(instance=WeeklyMax_strategy)
@settings(max_examples=50)
def test_weeklymax_instantiation(instance):
    assert isinstance(instance, WeeklyMax)

@given(instance=MonthlyMin_strategy)
@settings(max_examples=50)
def test_monthlymin_instantiation(instance):
    assert isinstance(instance, MonthlyMin)

@given(instance=MonthlyMax_strategy)
@settings(max_examples=50)
def test_monthlymax_instantiation(instance):
    assert isinstance(instance, MonthlyMax)

@given(instance=Minimum_strategy)
@settings(max_examples=50)
def test_minimum_instantiation(instance):
    assert isinstance(instance, Minimum)

@given(instance=Maximum_strategy)
@settings(max_examples=50)
def test_maximum_instantiation(instance):
    assert isinstance(instance, Maximum)

@given(instance=DailyMin_strategy)
@settings(max_examples=50)
def test_dailymin_instantiation(instance):
    assert isinstance(instance, DailyMin)

@given(instance=DailyMax_strategy)
@settings(max_examples=50)
def test_dailymax_instantiation(instance):
    assert isinstance(instance, DailyMax)

@given(instance=project_Limit_strategy)
@settings(max_examples=50)
def test_project_limit_instantiation(instance):
    assert isinstance(instance, project_Limit)

@given(instance=GapLength_strategy)
@settings(max_examples=50)
def test_gaplength_instantiation(instance):
    assert isinstance(instance, GapLength)

@given(instance=project_LimitsAttribute_strategy)
@settings(max_examples=50)
def test_project_limitsattribute_instantiation(instance):
    assert isinstance(instance, project_LimitsAttribute)

@given(instance=project_Interval3_strategy)
@settings(max_examples=50)
def test_project_interval3_instantiation(instance):
    assert isinstance(instance, project_Interval3)



@given(instance=project_Interval3_strategy)
def test_project_interval3_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=project_Interval3_strategy)
def test_project_interval3_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=project_Interval1_strategy)
@settings(max_examples=50)
def test_project_interval1_instantiation(instance):
    assert isinstance(instance, project_Interval1)



@given(instance=project_Interval1_strategy)
def test_project_interval1_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=project_Interval1_strategy)
def test_project_interval1_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=project_IncludePropertiesAttribute_strategy)
@settings(max_examples=50)
def test_project_includepropertiesattribute_instantiation(instance):
    assert isinstance(instance, project_IncludePropertiesAttribute)

@given(instance=project_Function_strategy)
@settings(max_examples=50)
def test_project_function_instantiation(instance):
    assert isinstance(instance, project_Function)



@given(instance=project_Function_strategy)
def test_project_function_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original



@given(instance=project_Function_strategy)
def test_project_function_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=project_Function_strategy)
def test_project_function_parentId_setter(instance):
    original = instance.parentId
    instance.parentId = original
    assert instance.parentId == original



@given(instance=project_Function_strategy)
def test_project_function_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=NavigatorAttribute_strategy)
@settings(max_examples=50)
def test_navigatorattribute_instantiation(instance):
    assert isinstance(instance, NavigatorAttribute)

@given(instance=project_HideReport_strategy)
@settings(max_examples=50)
def test_project_hidereport_instantiation(instance):
    assert isinstance(instance, project_HideReport)

@given(instance=project_GapLength_strategy)
@settings(max_examples=50)
def test_project_gaplength_instantiation(instance):
    assert isinstance(instance, project_GapLength)

@given(instance=project_GapDuration_strategy)
@settings(max_examples=50)
def test_project_gapduration_instantiation(instance):
    assert isinstance(instance, project_GapDuration)

@given(instance=project_Extend_strategy)
@settings(max_examples=50)
def test_project_extend_instantiation(instance):
    assert isinstance(instance, project_Extend)



@given(instance=project_Extend_strategy)
def test_project_extend_scenariospecific_setter(instance):
    original = instance.scenariospecific
    instance.scenariospecific = original
    assert instance.scenariospecific == original



@given(instance=project_Extend_strategy)
def test_project_extend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=project_Extend_strategy)
def test_project_extend_inherit_setter(instance):
    original = instance.inherit
    instance.inherit = original
    assert instance.inherit == original



@given(instance=project_Extend_strategy)
def test_project_extend_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ExportAttribute_strategy)
@settings(max_examples=50)
def test_exportattribute_instantiation(instance):
    assert isinstance(instance, ExportAttribute)

@given(instance=project_ResourceAttributes_strategy)
@settings(max_examples=50)
def test_project_resourceattributes_instantiation(instance):
    assert isinstance(instance, project_ResourceAttributes)



@given(instance=project_ResourceAttributes_strategy)
def test_project_resourceattributes_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original



@given(instance=project_ResourceAttributes_strategy)
def test_project_resourceattributes_vacation_setter(instance):
    original = instance.vacation
    instance.vacation = original
    assert instance.vacation == original



@given(instance=project_ResourceAttributes_strategy)
def test_project_resourceattributes_workingHours_setter(instance):
    original = instance.workingHours
    instance.workingHours = original
    assert instance.workingHours == original



@given(instance=project_ResourceAttributes_strategy)
def test_project_resourceattributes_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original



@given(instance=project_ResourceAttributes_strategy)
def test_project_resourceattributes_booking_setter(instance):
    original = instance.booking
    instance.booking = original
    assert instance.booking == original

@given(instance=project_TaskAttributes_strategy)
@settings(max_examples=50)
def test_project_taskattributes_instantiation(instance):
    assert isinstance(instance, project_TaskAttributes)



@given(instance=project_TaskAttributes_strategy)
def test_project_taskattributes_minstart_setter(instance):
    original = instance.minstart
    instance.minstart = original
    assert instance.minstart == original



@given(instance=project_TaskAttributes_strategy)
def test_project_taskattributes_booking_setter(instance):
    original = instance.booking
    instance.booking = original
    assert instance.booking == original



@given(instance=project_TaskAttributes_strategy)
def test_project_taskattributes_complete_setter(instance):
    original = instance.complete
    instance.complete = original
    assert instance.complete == original



@given(instance=project_TaskAttributes_strategy)
def test_project_taskattributes_minend_setter(instance):
    original = instance.minend
    instance.minend = original
    assert instance.minend == original



@given(instance=project_TaskAttributes_strategy)
def test_project_taskattributes_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original



@given(instance=project_TaskAttributes_strategy)
def test_project_taskattributes_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original



@given(instance=project_TaskAttributes_strategy)
def test_project_taskattributes_depends_setter(instance):
    original = instance.depends
    instance.depends = original
    assert instance.depends == original



@given(instance=project_TaskAttributes_strategy)
def test_project_taskattributes_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=project_TaskAttributes_strategy)
def test_project_taskattributes_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original



@given(instance=project_TaskAttributes_strategy)
def test_project_taskattributes_responsible_setter(instance):
    original = instance.responsible
    instance.responsible = original
    assert instance.responsible == original



@given(instance=project_TaskAttributes_strategy)
def test_project_taskattributes_maxend_setter(instance):
    original = instance.maxend
    instance.maxend = original
    assert instance.maxend == original



@given(instance=project_TaskAttributes_strategy)
def test_project_taskattributes_maxstart_setter(instance):
    original = instance.maxstart
    instance.maxstart = original
    assert instance.maxstart == original



@given(instance=project_TaskAttributes_strategy)
def test_project_taskattributes_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=project_Definitions_strategy)
@settings(max_examples=50)
def test_project_definitions_instantiation(instance):
    assert isinstance(instance, project_Definitions)



@given(instance=project_Definitions_strategy)
def test_project_definitions_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original



@given(instance=project_Definitions_strategy)
def test_project_definitions_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=LimitsAttribute_strategy)
@settings(max_examples=50)
def test_limitsattribute_instantiation(instance):
    assert isinstance(instance, LimitsAttribute)

@given(instance=project_DailyMin_strategy)
@settings(max_examples=50)
def test_project_dailymin_instantiation(instance):
    assert isinstance(instance, project_DailyMin)

@given(instance=project_WeeklyMax_strategy)
@settings(max_examples=50)
def test_project_weeklymax_instantiation(instance):
    assert isinstance(instance, project_WeeklyMax)

@given(instance=project_Minimum_strategy)
@settings(max_examples=50)
def test_project_minimum_instantiation(instance):
    assert isinstance(instance, project_Minimum)

@given(instance=project_Maximum_strategy)
@settings(max_examples=50)
def test_project_maximum_instantiation(instance):
    assert isinstance(instance, project_Maximum)

@given(instance=project_MonthlyMin_strategy)
@settings(max_examples=50)
def test_project_monthlymin_instantiation(instance):
    assert isinstance(instance, project_MonthlyMin)

@given(instance=project_MonthlyMax_strategy)
@settings(max_examples=50)
def test_project_monthlymax_instantiation(instance):
    assert isinstance(instance, project_MonthlyMax)

@given(instance=project_WeeklyMin_strategy)
@settings(max_examples=50)
def test_project_weeklymin_instantiation(instance):
    assert isinstance(instance, project_WeeklyMin)

@given(instance=project_DailyMax_strategy)
@settings(max_examples=50)
def test_project_dailymax_instantiation(instance):
    assert isinstance(instance, project_DailyMax)

@given(instance=ProjectAttribute_strategy)
@settings(max_examples=50)
def test_projectattribute_instantiation(instance):
    assert isinstance(instance, ProjectAttribute)

@given(instance=project_TrackingScenario_strategy)
@settings(max_examples=50)
def test_project_trackingscenario_instantiation(instance):
    assert isinstance(instance, project_TrackingScenario)

@given(instance=project_TimingResolution_strategy)
@settings(max_examples=50)
def test_project_timingresolution_instantiation(instance):
    assert isinstance(instance, project_TimingResolution)



@given(instance=project_TimingResolution_strategy)
def test_project_timingresolution_timingResolution_setter(instance):
    original = instance.timingResolution
    instance.timingResolution = original
    assert instance.timingResolution == original

@given(instance=project_DailyWorkingHours_strategy)
@settings(max_examples=50)
def test_project_dailyworkinghours_instantiation(instance):
    assert isinstance(instance, project_DailyWorkingHours)



@given(instance=project_DailyWorkingHours_strategy)
def test_project_dailyworkinghours_dailyWorkingHours_setter(instance):
    original = instance.dailyWorkingHours
    instance.dailyWorkingHours = original
    assert instance.dailyWorkingHours == original

@given(instance=project_WeekStarts_strategy)
@settings(max_examples=50)
def test_project_weekstarts_instantiation(instance):
    assert isinstance(instance, project_WeekStarts)



@given(instance=project_WeekStarts_strategy)
def test_project_weekstarts_monday_setter(instance):
    original = instance.monday
    instance.monday = original
    assert instance.monday == original



@given(instance=project_WeekStarts_strategy)
def test_project_weekstarts_sunday_setter(instance):
    original = instance.sunday
    instance.sunday = original
    assert instance.sunday == original

@given(instance=project_Scenario_strategy)
@settings(max_examples=50)
def test_project_scenario_instantiation(instance):
    assert isinstance(instance, project_Scenario)



@given(instance=project_Scenario_strategy)
def test_project_scenario_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original



@given(instance=project_Scenario_strategy)
def test_project_scenario_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=project_Scenario_strategy)
def test_project_scenario_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project_ExtendResource_strategy)
@settings(max_examples=50)
def test_project_extendresource_instantiation(instance):
    assert isinstance(instance, project_ExtendResource)

@given(instance=project_ExtendTask_strategy)
@settings(max_examples=50)
def test_project_extendtask_instantiation(instance):
    assert isinstance(instance, project_ExtendTask)

@given(instance=project_ShortTimeFormat_strategy)
@settings(max_examples=50)
def test_project_shorttimeformat_instantiation(instance):
    assert isinstance(instance, project_ShortTimeFormat)



@given(instance=project_ShortTimeFormat_strategy)
def test_project_shorttimeformat_shortTimeFormat_setter(instance):
    original = instance.shortTimeFormat
    instance.shortTimeFormat = original
    assert instance.shortTimeFormat == original

@given(instance=project_YearlyWorkingDays_strategy)
@settings(max_examples=50)
def test_project_yearlyworkingdays_instantiation(instance):
    assert isinstance(instance, project_YearlyWorkingDays)



@given(instance=project_YearlyWorkingDays_strategy)
def test_project_yearlyworkingdays_yearlyWorkingDays_setter(instance):
    original = instance.yearlyWorkingDays
    instance.yearlyWorkingDays = original
    assert instance.yearlyWorkingDays == original

@given(instance=project_Include_strategy)
@settings(max_examples=50)
def test_project_include_instantiation(instance):
    assert isinstance(instance, project_Include)



@given(instance=project_Include_strategy)
def test_project_include_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=project_Now_strategy)
@settings(max_examples=50)
def test_project_now_instantiation(instance):
    assert isinstance(instance, project_Now)



@given(instance=project_Now_strategy)
def test_project_now_now_setter(instance):
    original = instance.now
    instance.now = original
    assert instance.now == original

@given(instance=project_Currency_strategy)
@settings(max_examples=50)
def test_project_currency_instantiation(instance):
    assert isinstance(instance, project_Currency)



@given(instance=project_Currency_strategy)
def test_project_currency_currency_setter(instance):
    original = instance.currency
    instance.currency = original
    assert instance.currency == original

@given(instance=TimesheetReportAttribute_strategy)
@settings(max_examples=50)
def test_timesheetreportattribute_instantiation(instance):
    assert isinstance(instance, TimesheetReportAttribute)

@given(instance=TaskTimesheetAttribute_strategy)
@settings(max_examples=50)
def test_tasktimesheetattribute_instantiation(instance):
    assert isinstance(instance, TaskTimesheetAttribute)

@given(instance=StatusSheetReportAttribute_strategy)
@settings(max_examples=50)
def test_statussheetreportattribute_instantiation(instance):
    assert isinstance(instance, StatusSheetReportAttribute)

@given(instance=NikuReportAttribute_strategy)
@settings(max_examples=50)
def test_nikureportattribute_instantiation(instance):
    assert isinstance(instance, NikuReportAttribute)

@given(instance=project_Timeoff_strategy)
@settings(max_examples=50)
def test_project_timeoff_instantiation(instance):
    assert isinstance(instance, project_Timeoff)



@given(instance=project_Timeoff_strategy)
def test_project_timeoff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=project_Timeoff_strategy)
def test_project_timeoff_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=NewTaskAttribute_strategy)
@settings(max_examples=50)
def test_newtaskattribute_instantiation(instance):
    assert isinstance(instance, NewTaskAttribute)

@given(instance=project_Work_strategy)
@settings(max_examples=50)
def test_project_work_instantiation(instance):
    assert isinstance(instance, project_Work)



@given(instance=project_Work_strategy)
def test_project_work_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=project_Work_strategy)
def test_project_work_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=project_Remaining_strategy)
@settings(max_examples=50)
def test_project_remaining_instantiation(instance):
    assert isinstance(instance, project_Remaining)

@given(instance=IcalReportAttribute_strategy)
@settings(max_examples=50)
def test_icalreportattribute_instantiation(instance):
    assert isinstance(instance, IcalReportAttribute)

@given(instance=project_ScenarioIcal_strategy)
@settings(max_examples=50)
def test_project_scenarioical_instantiation(instance):
    assert isinstance(instance, project_ScenarioIcal)

@given(instance=project_DurationQuantity_strategy)
@settings(max_examples=50)
def test_project_durationquantity_instantiation(instance):
    assert isinstance(instance, project_DurationQuantity)



@given(instance=project_DurationQuantity_strategy)
def test_project_durationquantity_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=project_DurationQuantity_strategy)
def test_project_durationquantity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=StatusTimesheetAttribute_strategy)
@settings(max_examples=50)
def test_statustimesheetattribute_instantiation(instance):
    assert isinstance(instance, StatusTimesheetAttribute)

@given(instance=project_RGB_strategy)
@settings(max_examples=50)
def test_project_rgb_instantiation(instance):
    assert isinstance(instance, project_RGB)



@given(instance=project_RGB_strategy)
def test_project_rgb_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project_LogicalExpression_strategy)
@settings(max_examples=50)
def test_project_logicalexpression_instantiation(instance):
    assert isinstance(instance, project_LogicalExpression)

@given(instance=ColumnAttribute_strategy)
@settings(max_examples=50)
def test_columnattribute_instantiation(instance):
    assert isinstance(instance, ColumnAttribute)

@given(instance=project_CellText_strategy)
@settings(max_examples=50)
def test_project_celltext_instantiation(instance):
    assert isinstance(instance, project_CellText)



@given(instance=project_CellText_strategy)
def test_project_celltext_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=project_Width_strategy)
@settings(max_examples=50)
def test_project_width_instantiation(instance):
    assert isinstance(instance, project_Width)



@given(instance=project_Width_strategy)
def test_project_width_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=project_FontColor_strategy)
@settings(max_examples=50)
def test_project_fontcolor_instantiation(instance):
    assert isinstance(instance, project_FontColor)



@given(instance=project_FontColor_strategy)
def test_project_fontcolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=project_ToolTip_strategy)
@settings(max_examples=50)
def test_project_tooltip_instantiation(instance):
    assert isinstance(instance, project_ToolTip)



@given(instance=project_ToolTip_strategy)
def test_project_tooltip_tip_setter(instance):
    original = instance.tip
    instance.tip = original
    assert instance.tip == original

@given(instance=project_ListType_strategy)
@settings(max_examples=50)
def test_project_listtype_instantiation(instance):
    assert isinstance(instance, project_ListType)



@given(instance=project_ListType_strategy)
def test_project_listtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=project_ListItem_strategy)
@settings(max_examples=50)
def test_project_listitem_instantiation(instance):
    assert isinstance(instance, project_ListItem)

@given(instance=project_HAlign_strategy)
@settings(max_examples=50)
def test_project_halign_instantiation(instance):
    assert isinstance(instance, project_HAlign)



@given(instance=project_HAlign_strategy)
def test_project_halign_justification_setter(instance):
    original = instance.justification
    instance.justification = original
    assert instance.justification == original

@given(instance=project_Scale_strategy)
@settings(max_examples=50)
def test_project_scale_instantiation(instance):
    assert isinstance(instance, project_Scale)



@given(instance=project_Scale_strategy)
def test_project_scale_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=project_CellColor_strategy)
@settings(max_examples=50)
def test_project_cellcolor_instantiation(instance):
    assert isinstance(instance, project_CellColor)

@given(instance=project_Column_strategy)
@settings(max_examples=50)
def test_project_column_instantiation(instance):
    assert isinstance(instance, project_Column)



@given(instance=project_Column_strategy)
def test_project_column_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project_AccountShare_strategy)
@settings(max_examples=50)
def test_project_accountshare_instantiation(instance):
    assert isinstance(instance, project_AccountShare)



@given(instance=project_AccountShare_strategy)
def test_project_accountshare_share_setter(instance):
    original = instance.share
    instance.share = original
    assert instance.share == original

@given(instance=StatusStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_statusstatussheetattribute_instantiation(instance):
    assert isinstance(instance, StatusStatusSheetAttribute)

@given(instance=project_Summary_strategy)
@settings(max_examples=50)
def test_project_summary_instantiation(instance):
    assert isinstance(instance, project_Summary)

@given(instance=project_Details_strategy)
@settings(max_examples=50)
def test_project_details_instantiation(instance):
    assert isinstance(instance, project_Details)

@given(instance=project_Author_strategy)
@settings(max_examples=50)
def test_project_author_instantiation(instance):
    assert isinstance(instance, project_Author)

@given(instance=AllocateResourceAttribute_strategy)
@settings(max_examples=50)
def test_allocateresourceattribute_instantiation(instance):
    assert isinstance(instance, AllocateResourceAttribute)

@given(instance=project_ShiftsAllocate_strategy)
@settings(max_examples=50)
def test_project_shiftsallocate_instantiation(instance):
    assert isinstance(instance, project_ShiftsAllocate)

@given(instance=project_Mandatory_strategy)
@settings(max_examples=50)
def test_project_mandatory_instantiation(instance):
    assert isinstance(instance, project_Mandatory)



@given(instance=project_Mandatory_strategy)
def test_project_mandatory_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=project_Select_strategy)
@settings(max_examples=50)
def test_project_select_instantiation(instance):
    assert isinstance(instance, project_Select)



@given(instance=project_Select_strategy)
def test_project_select_argument_setter(instance):
    original = instance.argument
    instance.argument = original
    assert instance.argument == original

@given(instance=project_Persistent_strategy)
@settings(max_examples=50)
def test_project_persistent_instantiation(instance):
    assert isinstance(instance, project_Persistent)



@given(instance=project_Persistent_strategy)
def test_project_persistent_persistent_setter(instance):
    original = instance.persistent
    instance.persistent = original
    assert instance.persistent == original

@given(instance=project_Alternative_strategy)
@settings(max_examples=50)
def test_project_alternative_instantiation(instance):
    assert isinstance(instance, project_Alternative)

@given(instance=project_Alert_strategy)
@settings(max_examples=50)
def test_project_alert_instantiation(instance):
    assert isinstance(instance, project_Alert)



@given(instance=project_Alert_strategy)
def test_project_alert_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=project_NikuReportAttribute_strategy)
@settings(max_examples=50)
def test_project_nikureportattribute_instantiation(instance):
    assert isinstance(instance, project_NikuReportAttribute)

@given(instance=project_Interval4_strategy)
@settings(max_examples=50)
def test_project_interval4_instantiation(instance):
    assert isinstance(instance, project_Interval4)



@given(instance=project_Interval4_strategy)
def test_project_interval4_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=project_Interval4_strategy)
def test_project_interval4_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=project_Booking_strategy)
@settings(max_examples=50)
def test_project_booking_instantiation(instance):
    assert isinstance(instance, project_Booking)



@given(instance=project_Booking_strategy)
def test_project_booking_sloppy_setter(instance):
    original = instance.sloppy
    instance.sloppy = original
    assert instance.sloppy == original



@given(instance=project_Booking_strategy)
def test_project_booking_overtime_setter(instance):
    original = instance.overtime
    instance.overtime = original
    assert instance.overtime == original

@given(instance=project_AllocateResourceAttribute_strategy)
@settings(max_examples=50)
def test_project_allocateresourceattribute_instantiation(instance):
    assert isinstance(instance, project_AllocateResourceAttribute)

@given(instance=project_AllocateResource_strategy)
@settings(max_examples=50)
def test_project_allocateresource_instantiation(instance):
    assert isinstance(instance, project_AllocateResource)

@given(instance=project_NewTaskAttribute_strategy)
@settings(max_examples=50)
def test_project_newtaskattribute_instantiation(instance):
    assert isinstance(instance, project_NewTaskAttribute)

@given(instance=TimesheetAttribute_strategy)
@settings(max_examples=50)
def test_timesheetattribute_instantiation(instance):
    assert isinstance(instance, TimesheetAttribute)

@given(instance=project_ShiftTimesheet_strategy)
@settings(max_examples=50)
def test_project_shifttimesheet_instantiation(instance):
    assert isinstance(instance, project_ShiftTimesheet)

@given(instance=project_TaskTimesheet_strategy)
@settings(max_examples=50)
def test_project_tasktimesheet_instantiation(instance):
    assert isinstance(instance, project_TaskTimesheet)

@given(instance=project_StatusTimesheet_strategy)
@settings(max_examples=50)
def test_project_statustimesheet_instantiation(instance):
    assert isinstance(instance, project_StatusTimesheet)



@given(instance=project_StatusTimesheet_strategy)
def test_project_statustimesheet_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=project_StatusTimesheet_strategy)
def test_project_statustimesheet_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=project_NewTask_strategy)
@settings(max_examples=50)
def test_project_newtask_instantiation(instance):
    assert isinstance(instance, project_NewTask)



@given(instance=project_NewTask_strategy)
def test_project_newtask_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=project_NewTask_strategy)
def test_project_newtask_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project_NavigatorAttribute_strategy)
@settings(max_examples=50)
def test_project_navigatorattribute_instantiation(instance):
    assert isinstance(instance, project_NavigatorAttribute)

@given(instance=project_ReportAttribute_strategy)
@settings(max_examples=50)
def test_project_reportattribute_instantiation(instance):
    assert isinstance(instance, project_ReportAttribute)

@given(instance=project_ResourceAttribute_strategy)
@settings(max_examples=50)
def test_project_resourceattribute_instantiation(instance):
    assert isinstance(instance, project_ResourceAttribute)

@given(instance=ResourceAttribute_strategy)
@settings(max_examples=50)
def test_resourceattribute_instantiation(instance):
    assert isinstance(instance, ResourceAttribute)

@given(instance=project_Email_strategy)
@settings(max_examples=50)
def test_project_email_instantiation(instance):
    assert isinstance(instance, project_Email)



@given(instance=project_Email_strategy)
def test_project_email_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=project_ShiftsResource_strategy)
@settings(max_examples=50)
def test_project_shiftsresource_instantiation(instance):
    assert isinstance(instance, project_ShiftsResource)

@given(instance=project_WorkingHours_strategy)
@settings(max_examples=50)
def test_project_workinghours_instantiation(instance):
    assert isinstance(instance, project_WorkingHours)



@given(instance=project_WorkingHours_strategy)
def test_project_workinghours_off_setter(instance):
    original = instance.off
    instance.off = original
    assert instance.off == original

@given(instance=project_ExtendedResourceAttribute_strategy)
@settings(max_examples=50)
def test_project_extendedresourceattribute_instantiation(instance):
    assert isinstance(instance, project_ExtendedResourceAttribute)



@given(instance=project_ExtendedResourceAttribute_strategy)
def test_project_extendedresourceattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project_PurgeResource_strategy)
@settings(max_examples=50)
def test_project_purgeresource_instantiation(instance):
    assert isinstance(instance, project_PurgeResource)



@given(instance=project_PurgeResource_strategy)
def test_project_purgeresource_listAttribute_setter(instance):
    original = instance.listAttribute
    instance.listAttribute = original
    assert instance.listAttribute == original

@given(instance=project_Managers_strategy)
@settings(max_examples=50)
def test_project_managers_instantiation(instance):
    assert isinstance(instance, project_Managers)

@given(instance=project_Efficiency_strategy)
@settings(max_examples=50)
def test_project_efficiency_instantiation(instance):
    assert isinstance(instance, project_Efficiency)



@given(instance=project_Efficiency_strategy)
def test_project_efficiency_efficiency_setter(instance):
    original = instance.efficiency
    instance.efficiency = original
    assert instance.efficiency == original

@given(instance=project_BookingResource_strategy)
@settings(max_examples=50)
def test_project_bookingresource_instantiation(instance):
    assert isinstance(instance, project_BookingResource)

@given(instance=project_ExportAttribute_strategy)
@settings(max_examples=50)
def test_project_exportattribute_instantiation(instance):
    assert isinstance(instance, project_ExportAttribute)

@given(instance=project_IcalReportAttribute_strategy)
@settings(max_examples=50)
def test_project_icalreportattribute_instantiation(instance):
    assert isinstance(instance, project_IcalReportAttribute)

@given(instance=ReportAttribute_strategy)
@settings(max_examples=50)
def test_reportattribute_instantiation(instance):
    assert isinstance(instance, ReportAttribute)

@given(instance=project_HideTask_strategy)
@settings(max_examples=50)
def test_project_hidetask_instantiation(instance):
    assert isinstance(instance, project_HideTask)

@given(instance=project_Formats_strategy)
@settings(max_examples=50)
def test_project_formats_instantiation(instance):
    assert isinstance(instance, project_Formats)



@given(instance=project_Formats_strategy)
def test_project_formats_formats_setter(instance):
    original = instance.formats
    instance.formats = original
    assert instance.formats == original

@given(instance=project_Left_strategy)
@settings(max_examples=50)
def test_project_left_instantiation(instance):
    assert isinstance(instance, project_Left)

@given(instance=project_HideAccount_strategy)
@settings(max_examples=50)
def test_project_hideaccount_instantiation(instance):
    assert isinstance(instance, project_HideAccount)



@given(instance=project_HideAccount_strategy)
def test_project_hideaccount_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=project_SortJournalEntries_strategy)
@settings(max_examples=50)
def test_project_sortjournalentries_instantiation(instance):
    assert isinstance(instance, project_SortJournalEntries)

@given(instance=project_Title_strategy)
@settings(max_examples=50)
def test_project_title_instantiation(instance):
    assert isinstance(instance, project_Title)



@given(instance=project_Title_strategy)
def test_project_title_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=project_Right_strategy)
@settings(max_examples=50)
def test_project_right_instantiation(instance):
    assert isinstance(instance, project_Right)

@given(instance=project_Prolog_strategy)
@settings(max_examples=50)
def test_project_prolog_instantiation(instance):
    assert isinstance(instance, project_Prolog)

@given(instance=project_SelfContained_strategy)
@settings(max_examples=50)
def test_project_selfcontained_instantiation(instance):
    assert isinstance(instance, project_SelfContained)



@given(instance=project_SelfContained_strategy)
def test_project_selfcontained_selfcontained_setter(instance):
    original = instance.selfcontained
    instance.selfcontained = original
    assert instance.selfcontained == original

@given(instance=project_RollupAccount_strategy)
@settings(max_examples=50)
def test_project_rollupaccount_instantiation(instance):
    assert isinstance(instance, project_RollupAccount)

@given(instance=project_AccountRoot_strategy)
@settings(max_examples=50)
def test_project_accountroot_instantiation(instance):
    assert isinstance(instance, project_AccountRoot)

@given(instance=project_Epilog_strategy)
@settings(max_examples=50)
def test_project_epilog_instantiation(instance):
    assert isinstance(instance, project_Epilog)

@given(instance=project_RollupResource_strategy)
@settings(max_examples=50)
def test_project_rollupresource_instantiation(instance):
    assert isinstance(instance, project_RollupResource)

@given(instance=project_HideJournalEntry_strategy)
@settings(max_examples=50)
def test_project_hidejournalentry_instantiation(instance):
    assert isinstance(instance, project_HideJournalEntry)



@given(instance=project_HideJournalEntry_strategy)
def test_project_hidejournalentry_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=project_HideResource_strategy)
@settings(max_examples=50)
def test_project_hideresource_instantiation(instance):
    assert isinstance(instance, project_HideResource)

@given(instance=project_Headline_strategy)
@settings(max_examples=50)
def test_project_headline_instantiation(instance):
    assert isinstance(instance, project_Headline)

@given(instance=project_Footer_strategy)
@settings(max_examples=50)
def test_project_footer_instantiation(instance):
    assert isinstance(instance, project_Footer)

@given(instance=project_Timezone_strategy)
@settings(max_examples=50)
def test_project_timezone_instantiation(instance):
    assert isinstance(instance, project_Timezone)



@given(instance=project_Timezone_strategy)
def test_project_timezone_timezone_setter(instance):
    original = instance.timezone
    instance.timezone = original
    assert instance.timezone == original

@given(instance=project_TaskRoot_strategy)
@settings(max_examples=50)
def test_project_taskroot_instantiation(instance):
    assert isinstance(instance, project_TaskRoot)

@given(instance=project_SortResources_strategy)
@settings(max_examples=50)
def test_project_sortresources_instantiation(instance):
    assert isinstance(instance, project_SortResources)

@given(instance=project_NumberFormat_strategy)
@settings(max_examples=50)
def test_project_numberformat_instantiation(instance):
    assert isinstance(instance, project_NumberFormat)

@given(instance=project_PurgeReport_strategy)
@settings(max_examples=50)
def test_project_purgereport_instantiation(instance):
    assert isinstance(instance, project_PurgeReport)



@given(instance=project_PurgeReport_strategy)
def test_project_purgereport_listAttribute_setter(instance):
    original = instance.listAttribute
    instance.listAttribute = original
    assert instance.listAttribute == original

@given(instance=project_Scenarios_strategy)
@settings(max_examples=50)
def test_project_scenarios_instantiation(instance):
    assert isinstance(instance, project_Scenarios)

@given(instance=project_CurrencyFormat_strategy)
@settings(max_examples=50)
def test_project_currencyformat_instantiation(instance):
    assert isinstance(instance, project_CurrencyFormat)

@given(instance=project_TimeFormat_strategy)
@settings(max_examples=50)
def test_project_timeformat_instantiation(instance):
    assert isinstance(instance, project_TimeFormat)



@given(instance=project_TimeFormat_strategy)
def test_project_timeformat_timeformat_setter(instance):
    original = instance.timeformat
    instance.timeformat = original
    assert instance.timeformat == original

@given(instance=project_SortAccounts_strategy)
@settings(max_examples=50)
def test_project_sortaccounts_instantiation(instance):
    assert isinstance(instance, project_SortAccounts)

@given(instance=project_JournalAttributes_strategy)
@settings(max_examples=50)
def test_project_journalattributes_instantiation(instance):
    assert isinstance(instance, project_JournalAttributes)



@given(instance=project_JournalAttributes_strategy)
def test_project_journalattributes_propertyid_setter(instance):
    original = instance.propertyid
    instance.propertyid = original
    assert instance.propertyid == original



@given(instance=project_JournalAttributes_strategy)
def test_project_journalattributes_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original



@given(instance=project_JournalAttributes_strategy)
def test_project_journalattributes_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original



@given(instance=project_JournalAttributes_strategy)
def test_project_journalattributes_summary_setter(instance):
    original = instance.summary
    instance.summary = original
    assert instance.summary == original



@given(instance=project_JournalAttributes_strategy)
def test_project_journalattributes_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=project_JournalAttributes_strategy)
def test_project_journalattributes__property_setter(instance):
    original = instance._property
    instance._property = original
    assert instance._property == original



@given(instance=project_JournalAttributes_strategy)
def test_project_journalattributes_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original



@given(instance=project_JournalAttributes_strategy)
def test_project_journalattributes_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original



@given(instance=project_JournalAttributes_strategy)
def test_project_journalattributes_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=project_JournalAttributes_strategy)
def test_project_journalattributes_headline_setter(instance):
    original = instance.headline
    instance.headline = original
    assert instance.headline == original



@given(instance=project_JournalAttributes_strategy)
def test_project_journalattributes_timesheet_setter(instance):
    original = instance.timesheet
    instance.timesheet = original
    assert instance.timesheet == original

@given(instance=project_Center_strategy)
@settings(max_examples=50)
def test_project_center_instantiation(instance):
    assert isinstance(instance, project_Center)

@given(instance=project_ResourceRoot_strategy)
@settings(max_examples=50)
def test_project_resourceroot_instantiation(instance):
    assert isinstance(instance, project_ResourceRoot)

@given(instance=project_RollupTask_strategy)
@settings(max_examples=50)
def test_project_rolluptask_instantiation(instance):
    assert isinstance(instance, project_RollupTask)

@given(instance=project_LoadUnit_strategy)
@settings(max_examples=50)
def test_project_loadunit_instantiation(instance):
    assert isinstance(instance, project_LoadUnit)



@given(instance=project_LoadUnit_strategy)
def test_project_loadunit_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=project_Columns_strategy)
@settings(max_examples=50)
def test_project_columns_instantiation(instance):
    assert isinstance(instance, project_Columns)

@given(instance=project_Caption_strategy)
@settings(max_examples=50)
def test_project_caption_instantiation(instance):
    assert isinstance(instance, project_Caption)

@given(instance=project_Header_strategy)
@settings(max_examples=50)
def test_project_header_instantiation(instance):
    assert isinstance(instance, project_Header)

@given(instance=project_JournalMode_strategy)
@settings(max_examples=50)
def test_project_journalmode_instantiation(instance):
    assert isinstance(instance, project_JournalMode)



@given(instance=project_JournalMode_strategy)
def test_project_journalmode_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=project_SortTasks_strategy)
@settings(max_examples=50)
def test_project_sorttasks_instantiation(instance):
    assert isinstance(instance, project_SortTasks)

@given(instance=TextReport_strategy)
@settings(max_examples=50)
def test_textreport_instantiation(instance):
    assert isinstance(instance, TextReport)

@given(instance=TaskReport_strategy)
@settings(max_examples=50)
def test_taskreport_instantiation(instance):
    assert isinstance(instance, TaskReport)

@given(instance=ResourceReport_strategy)
@settings(max_examples=50)
def test_resourcereport_instantiation(instance):
    assert isinstance(instance, ResourceReport)

@given(instance=AccountReport_strategy)
@settings(max_examples=50)
def test_accountreport_instantiation(instance):
    assert isinstance(instance, AccountReport)

@given(instance=project_Report_strategy)
@settings(max_examples=50)
def test_project_report_instantiation(instance):
    assert isinstance(instance, project_Report)



@given(instance=project_Report_strategy)
def test_project_report_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=project_Report_strategy)
def test_project_report_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=project_TaskAttribute_strategy)
@settings(max_examples=50)
def test_project_taskattribute_instantiation(instance):
    assert isinstance(instance, project_TaskAttribute)

@given(instance=TaskAttribute_strategy)
@settings(max_examples=50)
def test_taskattribute_instantiation(instance):
    assert isinstance(instance, TaskAttribute)

@given(instance=project_Note_strategy)
@settings(max_examples=50)
def test_project_note_instantiation(instance):
    assert isinstance(instance, project_Note)



@given(instance=project_Note_strategy)
def test_project_note_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=project_ShiftsTask_strategy)
@settings(max_examples=50)
def test_project_shiftstask_instantiation(instance):
    assert isinstance(instance, project_ShiftsTask)

@given(instance=project_Period_strategy)
@settings(max_examples=50)
def test_project_period_instantiation(instance):
    assert isinstance(instance, project_Period)

@given(instance=project_Priority_strategy)
@settings(max_examples=50)
def test_project_priority_instantiation(instance):
    assert isinstance(instance, project_Priority)



@given(instance=project_Priority_strategy)
def test_project_priority_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=project_Warn_strategy)
@settings(max_examples=50)
def test_project_warn_instantiation(instance):
    assert isinstance(instance, project_Warn)

@given(instance=project_Charge_strategy)
@settings(max_examples=50)
def test_project_charge_instantiation(instance):
    assert isinstance(instance, project_Charge)



@given(instance=project_Charge_strategy)
def test_project_charge_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=project_Charge_strategy)
def test_project_charge_applies_setter(instance):
    original = instance.applies
    instance.applies = original
    assert instance.applies == original

@given(instance=project_Scheduled_strategy)
@settings(max_examples=50)
def test_project_scheduled_instantiation(instance):
    assert isinstance(instance, project_Scheduled)



@given(instance=project_Scheduled_strategy)
def test_project_scheduled_scheduled_setter(instance):
    original = instance.scheduled
    instance.scheduled = original
    assert instance.scheduled == original

@given(instance=project_Start_strategy)
@settings(max_examples=50)
def test_project_start_instantiation(instance):
    assert isinstance(instance, project_Start)



@given(instance=project_Start_strategy)
def test_project_start_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=project_End_strategy)
@settings(max_examples=50)
def test_project_end_instantiation(instance):
    assert isinstance(instance, project_End)



@given(instance=project_End_strategy)
def test_project_end_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=project_MinEnd_strategy)
@settings(max_examples=50)
def test_project_minend_instantiation(instance):
    assert isinstance(instance, project_MinEnd)



@given(instance=project_MinEnd_strategy)
def test_project_minend_minEnd_setter(instance):
    original = instance.minEnd
    instance.minEnd = original
    assert instance.minEnd == original

@given(instance=project_Allocate_strategy)
@settings(max_examples=50)
def test_project_allocate_instantiation(instance):
    assert isinstance(instance, project_Allocate)

@given(instance=project_Length_strategy)
@settings(max_examples=50)
def test_project_length_instantiation(instance):
    assert isinstance(instance, project_Length)

@given(instance=project_MinStart_strategy)
@settings(max_examples=50)
def test_project_minstart_instantiation(instance):
    assert isinstance(instance, project_MinStart)



@given(instance=project_MinStart_strategy)
def test_project_minstart_minStart_setter(instance):
    original = instance.minStart
    instance.minStart = original
    assert instance.minStart == original

@given(instance=project_Duration_strategy)
@settings(max_examples=50)
def test_project_duration_instantiation(instance):
    assert isinstance(instance, project_Duration)

@given(instance=project_Complete_strategy)
@settings(max_examples=50)
def test_project_complete_instantiation(instance):
    assert isinstance(instance, project_Complete)



@given(instance=project_Complete_strategy)
def test_project_complete_complete_setter(instance):
    original = instance.complete
    instance.complete = original
    assert instance.complete == original

@given(instance=project_EndCredit_strategy)
@settings(max_examples=50)
def test_project_endcredit_instantiation(instance):
    assert isinstance(instance, project_EndCredit)



@given(instance=project_EndCredit_strategy)
def test_project_endcredit_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original

@given(instance=project_Effort_strategy)
@settings(max_examples=50)
def test_project_effort_instantiation(instance):
    assert isinstance(instance, project_Effort)

@given(instance=project_JournalEntry_strategy)
@settings(max_examples=50)
def test_project_journalentry_instantiation(instance):
    assert isinstance(instance, project_JournalEntry)



@given(instance=project_JournalEntry_strategy)
def test_project_journalentry_headline_setter(instance):
    original = instance.headline
    instance.headline = original
    assert instance.headline == original



@given(instance=project_JournalEntry_strategy)
def test_project_journalentry_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=project_PurgeTask_strategy)
@settings(max_examples=50)
def test_project_purgetask_instantiation(instance):
    assert isinstance(instance, project_PurgeTask)



@given(instance=project_PurgeTask_strategy)
def test_project_purgetask_listAttribute_setter(instance):
    original = instance.listAttribute
    instance.listAttribute = original
    assert instance.listAttribute == original

@given(instance=project_BookingTask_strategy)
@settings(max_examples=50)
def test_project_bookingtask_instantiation(instance):
    assert isinstance(instance, project_BookingTask)

@given(instance=project_ChargeSet_strategy)
@settings(max_examples=50)
def test_project_chargeset_instantiation(instance):
    assert isinstance(instance, project_ChargeSet)

@given(instance=project_MaxEnd_strategy)
@settings(max_examples=50)
def test_project_maxend_instantiation(instance):
    assert isinstance(instance, project_MaxEnd)



@given(instance=project_MaxEnd_strategy)
def test_project_maxend_maxEnd_setter(instance):
    original = instance.maxEnd
    instance.maxEnd = original
    assert instance.maxEnd == original

@given(instance=project_Milestone_strategy)
@settings(max_examples=50)
def test_project_milestone_instantiation(instance):
    assert isinstance(instance, project_Milestone)



@given(instance=project_Milestone_strategy)
def test_project_milestone_milestone_setter(instance):
    original = instance.milestone
    instance.milestone = original
    assert instance.milestone == original

@given(instance=project_Scheduling_strategy)
@settings(max_examples=50)
def test_project_scheduling_instantiation(instance):
    assert isinstance(instance, project_Scheduling)



@given(instance=project_Scheduling_strategy)
def test_project_scheduling_scheduling_setter(instance):
    original = instance.scheduling
    instance.scheduling = original
    assert instance.scheduling == original

@given(instance=project_Precedes_strategy)
@settings(max_examples=50)
def test_project_precedes_instantiation(instance):
    assert isinstance(instance, project_Precedes)

@given(instance=project_Depends_strategy)
@settings(max_examples=50)
def test_project_depends_instantiation(instance):
    assert isinstance(instance, project_Depends)

@given(instance=project_Fail_strategy)
@settings(max_examples=50)
def test_project_fail_instantiation(instance):
    assert isinstance(instance, project_Fail)

@given(instance=project_ProjectId_strategy)
@settings(max_examples=50)
def test_project_projectid_instantiation(instance):
    assert isinstance(instance, project_ProjectId)



@given(instance=project_ProjectId_strategy)
def test_project_projectid_projectId_setter(instance):
    original = instance.projectId
    instance.projectId = original
    assert instance.projectId == original

@given(instance=project_ExtendedTaskAttribute_strategy)
@settings(max_examples=50)
def test_project_extendedtaskattribute_instantiation(instance):
    assert isinstance(instance, project_ExtendedTaskAttribute)



@given(instance=project_ExtendedTaskAttribute_strategy)
def test_project_extendedtaskattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project_MaxStart_strategy)
@settings(max_examples=50)
def test_project_maxstart_instantiation(instance):
    assert isinstance(instance, project_MaxStart)



@given(instance=project_MaxStart_strategy)
def test_project_maxstart_maxStart_setter(instance):
    original = instance.maxStart
    instance.maxStart = original
    assert instance.maxStart == original

@given(instance=project_Responsible_strategy)
@settings(max_examples=50)
def test_project_responsible_instantiation(instance):
    assert isinstance(instance, project_Responsible)

@given(instance=project_ProjectAttribute_strategy)
@settings(max_examples=50)
def test_project_projectattribute_instantiation(instance):
    assert isinstance(instance, project_ProjectAttribute)

@given(instance=project_Interval2_strategy)
@settings(max_examples=50)
def test_project_interval2_instantiation(instance):
    assert isinstance(instance, project_Interval2)



@given(instance=project_Interval2_strategy)
def test_project_interval2_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=project_Interval2_strategy)
def test_project_interval2_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=project_Global_strategy)
@settings(max_examples=50)
def test_project_global_instantiation(instance):
    assert isinstance(instance, project_Global)

@given(instance=IncludePropertiesAttribute_strategy)
@settings(max_examples=50)
def test_includepropertiesattribute_instantiation(instance):
    assert isinstance(instance, IncludePropertiesAttribute)

@given(instance=project_TaskPrefix_strategy)
@settings(max_examples=50)
def test_project_taskprefix_instantiation(instance):
    assert isinstance(instance, project_TaskPrefix)

@given(instance=project_ReportPrefix_strategy)
@settings(max_examples=50)
def test_project_reportprefix_instantiation(instance):
    assert isinstance(instance, project_ReportPrefix)

@given(instance=project_ResourcePrefix_strategy)
@settings(max_examples=50)
def test_project_resourceprefix_instantiation(instance):
    assert isinstance(instance, project_ResourcePrefix)

@given(instance=project_AccountPrefix_strategy)
@settings(max_examples=50)
def test_project_accountprefix_instantiation(instance):
    assert isinstance(instance, project_AccountPrefix)

@given(instance=project_AccountAttribute_strategy)
@settings(max_examples=50)
def test_project_accountattribute_instantiation(instance):
    assert isinstance(instance, project_AccountAttribute)

@given(instance=AccountAttribute_strategy)
@settings(max_examples=50)
def test_accountattribute_instantiation(instance):
    assert isinstance(instance, AccountAttribute)

@given(instance=project_Credit_strategy)
@settings(max_examples=50)
def test_project_credit_instantiation(instance):
    assert isinstance(instance, project_Credit)



@given(instance=project_Credit_strategy)
def test_project_credit_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=project_Credit_strategy)
def test_project_credit_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=project_Credit_strategy)
def test_project_credit_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=project_AccountReport_strategy)
@settings(max_examples=50)
def test_project_accountreport_instantiation(instance):
    assert isinstance(instance, project_AccountReport)

@given(instance=project_SupplementAccount_strategy)
@settings(max_examples=50)
def test_project_supplementaccount_instantiation(instance):
    assert isinstance(instance, project_SupplementAccount)

@given(instance=project_StatusSheet_strategy)
@settings(max_examples=50)
def test_project_statussheet_instantiation(instance):
    assert isinstance(instance, project_StatusSheet)

@given(instance=project_Flags_strategy)
@settings(max_examples=50)
def test_project_flags_instantiation(instance):
    assert isinstance(instance, project_Flags)



@given(instance=project_Flags_strategy)
def test_project_flags_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original

@given(instance=project_Navigator_strategy)
@settings(max_examples=50)
def test_project_navigator_instantiation(instance):
    assert isinstance(instance, project_Navigator)



@given(instance=project_Navigator_strategy)
def test_project_navigator_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project_TimesheetReport_strategy)
@settings(max_examples=50)
def test_project_timesheetreport_instantiation(instance):
    assert isinstance(instance, project_TimesheetReport)



@given(instance=project_TimesheetReport_strategy)
def test_project_timesheetreport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=project_StatusSheetReport_strategy)
@settings(max_examples=50)
def test_project_statussheetreport_instantiation(instance):
    assert isinstance(instance, project_StatusSheetReport)



@given(instance=project_StatusSheetReport_strategy)
def test_project_statussheetreport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=project_Vacation_strategy)
@settings(max_examples=50)
def test_project_vacation_instantiation(instance):
    assert isinstance(instance, project_Vacation)



@given(instance=project_Vacation_strategy)
def test_project_vacation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=project_Rate_strategy)
@settings(max_examples=50)
def test_project_rate_instantiation(instance):
    assert isinstance(instance, project_Rate)



@given(instance=project_Rate_strategy)
def test_project_rate_rate_setter(instance):
    original = instance.rate
    instance.rate = original
    assert instance.rate == original

@given(instance=project_Macro_strategy)
@settings(max_examples=50)
def test_project_macro_instantiation(instance):
    assert isinstance(instance, project_Macro)



@given(instance=project_Macro_strategy)
def test_project_macro_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project_NikuReport_strategy)
@settings(max_examples=50)
def test_project_nikureport_instantiation(instance):
    assert isinstance(instance, project_NikuReport)



@given(instance=project_NikuReport_strategy)
def test_project_nikureport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=project_TextReport_strategy)
@settings(max_examples=50)
def test_project_textreport_instantiation(instance):
    assert isinstance(instance, project_TextReport)

@given(instance=project_Resource_strategy)
@settings(max_examples=50)
def test_project_resource_instantiation(instance):
    assert isinstance(instance, project_Resource)



@given(instance=project_Resource_strategy)
def test_project_resource_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=project_Resource_strategy)
def test_project_resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=project_Limits_strategy)
@settings(max_examples=50)
def test_project_limits_instantiation(instance):
    assert isinstance(instance, project_Limits)

@given(instance=project_IcalReport_strategy)
@settings(max_examples=50)
def test_project_icalreport_instantiation(instance):
    assert isinstance(instance, project_IcalReport)



@given(instance=project_IcalReport_strategy)
def test_project_icalreport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=project_Export_strategy)
@settings(max_examples=50)
def test_project_export_instantiation(instance):
    assert isinstance(instance, project_Export)



@given(instance=project_Export_strategy)
def test_project_export_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=project_Export_strategy)
def test_project_export_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=project_Timesheet_strategy)
@settings(max_examples=50)
def test_project_timesheet_instantiation(instance):
    assert isinstance(instance, project_Timesheet)

@given(instance=project_SupplementReport_strategy)
@settings(max_examples=50)
def test_project_supplementreport_instantiation(instance):
    assert isinstance(instance, project_SupplementReport)

@given(instance=project_SupplementResource_strategy)
@settings(max_examples=50)
def test_project_supplementresource_instantiation(instance):
    assert isinstance(instance, project_SupplementResource)

@given(instance=project_Copyright_strategy)
@settings(max_examples=50)
def test_project_copyright_instantiation(instance):
    assert isinstance(instance, project_Copyright)



@given(instance=project_Copyright_strategy)
def test_project_copyright_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=project_Shift_strategy)
@settings(max_examples=50)
def test_project_shift_instantiation(instance):
    assert isinstance(instance, project_Shift)



@given(instance=project_Shift_strategy)
def test_project_shift_replace_setter(instance):
    original = instance.replace
    instance.replace = original
    assert instance.replace == original



@given(instance=project_Shift_strategy)
def test_project_shift_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=project_Shift_strategy)
def test_project_shift_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=project_Shift_strategy)
def test_project_shift_timezone_setter(instance):
    original = instance.timezone
    instance.timezone = original
    assert instance.timezone == original

@given(instance=project_IncludeProperties_strategy)
@settings(max_examples=50)
def test_project_includeproperties_instantiation(instance):
    assert isinstance(instance, project_IncludeProperties)



@given(instance=project_IncludeProperties_strategy)
def test_project_includeproperties_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=project_Task_strategy)
@settings(max_examples=50)
def test_project_task_instantiation(instance):
    assert isinstance(instance, project_Task)



@given(instance=project_Task_strategy)
def test_project_task_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=project_Task_strategy)
def test_project_task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=project_ProjectIds_strategy)
@settings(max_examples=50)
def test_project_projectids_instantiation(instance):
    assert isinstance(instance, project_ProjectIds)



@given(instance=project_ProjectIds_strategy)
def test_project_projectids_ids_setter(instance):
    original = instance.ids
    instance.ids = original
    assert instance.ids == original

@given(instance=project_ResourceReport_strategy)
@settings(max_examples=50)
def test_project_resourcereport_instantiation(instance):
    assert isinstance(instance, project_ResourceReport)

@given(instance=project_TaskReport_strategy)
@settings(max_examples=50)
def test_project_taskreport_instantiation(instance):
    assert isinstance(instance, project_TaskReport)

@given(instance=project_SupplementTask_strategy)
@settings(max_examples=50)
def test_project_supplementtask_instantiation(instance):
    assert isinstance(instance, project_SupplementTask)

@given(instance=project_Balance_strategy)
@settings(max_examples=50)
def test_project_balance_instantiation(instance):
    assert isinstance(instance, project_Balance)

@given(instance=project_TagFile_strategy)
@settings(max_examples=50)
def test_project_tagfile_instantiation(instance):
    assert isinstance(instance, project_TagFile)



@given(instance=project_TagFile_strategy)
def test_project_tagfile_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original



@given(instance=project_TagFile_strategy)
def test_project_tagfile_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project_Account_strategy)
@settings(max_examples=50)
def test_project_account_instantiation(instance):
    assert isinstance(instance, project_Account)



@given(instance=project_Account_strategy)
def test_project_account_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=project_Account_strategy)
def test_project_account_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project_Property_strategy)
@settings(max_examples=50)
def test_project_property_instantiation(instance):
    assert isinstance(instance, project_Property)

@given(instance=project_Project_strategy)
@settings(max_examples=50)
def test_project_project_instantiation(instance):
    assert isinstance(instance, project_Project)



@given(instance=project_Project_strategy)
def test_project_project_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=project_Project_strategy)
def test_project_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=project_Project_strategy)
def test_project_project_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original
