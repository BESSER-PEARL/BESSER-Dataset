import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    LogicalExpression,
    eTJ_LogicalDateLiteral,
    eTJ_LogicalNumeralLiteral,
    eTJ_LogicalAbsoluteIdExression,
    eTJ_LogicalFlagExpression,
    eTJ_LogicalBooleanLiteral,
    eTJ_LogicalStringLiteral,
    eTJ_LogicalFunctionExpression,
    Definitions,
    eTJ_Defintions,
    eTJ_ExtDate,
    NumberFormat,
    CurrencyFormat,
    eTJ_RealFormat,
    eTJ_LimitAttribute,
    Summary,
    Right,
    Prolog,
    ListItem,
    Left,
    Headline,
    Header,
    Footer,
    Epilog,
    Details,
    Center,
    Caption,
    eTJ_RichText,
    Precedes,
    eTJ_ColumnAttribute,
    eTJ_WorkHours,
    eTJ_Weekdays,
    WeeklyMin,
    WeeklyMax,
    MonthlyMin,
    MonthlyMax,
    Minimum,
    Maximum,
    DailyMin,
    DailyMax,
    eTJ_Limit,
    GapLength,
    GapDuration,
    eTJ_TreeLevel,
    eTJ_TimesheetReportAttribute,
    eTJ_TimesheetAttribute,
    eTJ_TaskTimesheetAttribute,
    eTJ_TaskStatusSheetAttribute,
    StatusSheetAttribute,
    AllocateResourceAttribute,
    eTJ_Alternative,
    eTJ_Alert,
    eTJ_NikuReportAttribute,
    eTJ_NewTaskAttribute,
    TimesheetAttribute,
    eTJ_TaskTimesheet,
    eTJ_NewTask,
    ExtDate,
    Start,
    End,
    eTJ_MacroCall,
    eTJ_EObject,
    eTJ_TaskAttribute,
    eTJ_ProjectAttribute,
    eTJ_ExportAttribute,
    eTJ_IcalReportAttribute,
    eTJ_ReportAttribute,
    TextReport,
    TaskReport,
    ResourceReport,
    AccountReport,
    eTJ_Report,
    eTJ_AccountAttribute,
    AccountAttribute,
    eTJ_Interval2,
    ReportAttribute,
    eTJ_TaskRoot,
    eTJ_AccountRoot,
    IncludePropertiesAttribute,
    eTJ_TaskPrefix,
    eTJ_AccountPrefix,
    eTJ_Property,
    eTJ_Project,
    eTJ_Global,
    eTJ_Interval3,
    eTJ_LeaveDetails,
    ResourceAttribute,
    eTJ_Warn,
    Property,
    eTJ_IcalReport,
    eTJ_Macro,
    eTJ_NikuReport,
    eTJ_TextReport,
    eTJ_TimesheetReport,
    eTJ_Account,
    eTJ_Timesheet,
    eTJ_TaskReport,
    eTJ_Task,
    eTJ_AccountReport,
    eTJ_Export,
    eTJ_Leaves,
    eTJ_SupplementAccount,
    eTJ_StatusSheetReportAttribute,
    eTJ_StatusSheetReport,
    eTJ_StatusSheetAttribute,
    eTJ_StatusSheet,
    eTJ_TagFile,
    eTJ_SupplementTask,
    eTJ_SupplementResource,
    eTJ_SupplementReport,
    eTJ_SortJournalEntries,
    eTJ_SortAccounts,
    eTJ_Criterion,
    SortTasks,
    SortResources,
    SortJournalEntries,
    SortAccounts,
    eTJ_Sort,
    eTJ_ShiftsTask,
    eTJ_ShiftsResource,
    eTJ_StatusTimesheetAttribute,
    eTJ_StatusStatusSheetAttribute,
    TaskStatusSheetAttribute,
    eTJ_TaskStatusSheet,
    eTJ_StatusStatusSheet,
    eTJ_Shift,
    eTJ_SelfContained,
    eTJ_Select,
    eTJ_Scheduling,
    eTJ_Scheduled,
    eTJ_ShiftsAllocate,
    eTJ_ShiftsLimit,
    ShiftsTask,
    ShiftsResource,
    eTJ_Shifts,
    eTJ_ShiftTimesheet,
    eTJ_Vacation,
    eTJ_RollupAccount,
    eTJ_Right,
    eTJ_Responsible,
    eTJ_ResourceRoot,
    eTJ_ResourceReport,
    eTJ_PurgeTask,
    eTJ_PurgeResource,
    eTJ_ResourcePrefix,
    eTJ_ReportPrefix,
    eTJ_Rate,
    eTJ_Note,
    eTJ_PurgeReport,
    eTJ_Prolog,
    eTJ_ProjectIds,
    eTJ_ProjectId,
    eTJ_Precedes,
    eTJ_Persistent,
    eTJ_LoadUnit,
    eTJ_LimitsAttribute,
    eTJ_Limits,
    eTJ_MinStart,
    eTJ_MinEnd,
    eTJ_Milestone,
    eTJ_MaxStart,
    eTJ_MaxEnd,
    eTJ_Mandatory,
    eTJ_Managers,
    eTJ_JournalAttributes,
    eTJ_Length,
    eTJ_Left,
    eTJ_JournalMode,
    NavigatorAttribute,
    eTJ_HideReport,
    eTJ_Interval1,
    eTJ_IncludePropertiesAttribute,
    eTJ_IncludeProperties,
    eTJ_Footer,
    eTJ_Fail,
    eTJ_ExtendedTaskAttribute,
    eTJ_HideAccount,
    eTJ_Header,
    eTJ_GapLength,
    eTJ_GapDuration,
    eTJ_Function,
    NewTaskAttribute,
    IcalReportAttribute,
    eTJ_HideJournalEntry,
    eTJ_ScenarioIcal,
    eTJ_Email,
    eTJ_Effort,
    eTJ_Efficiency,
    eTJ_DurationQuantity,
    eTJ_Duration,
    StatusTimesheetAttribute,
    eTJ_TaskDependency,
    eTJ_Depends,
    eTJ_ExtendedResourceAttribute,
    eTJ_Extend,
    eTJ_Epilog,
    eTJ_EndCredit,
    TimesheetReportAttribute,
    TaskTimesheetAttribute,
    eTJ_Remaining,
    eTJ_StatusTimesheet,
    eTJ_Priority,
    eTJ_Work,
    StatusSheetReportAttribute,
    eTJ_SortTasks,
    eTJ_SortResources,
    NikuReportAttribute,
    eTJ_Formats,
    eTJ_Headline,
    eTJ_Timeoff,
    eTJ_AccountShare,
    eTJ_ChargeSet,
    eTJ_Charge,
    eTJ_Center,
    eTJ_RGB,
    eTJ_LogicalExpression,
    ColumnAttribute,
    eTJ_FontColor,
    eTJ_CellText,
    eTJ_HAlign,
    eTJ_Scale,
    eTJ_Title,
    eTJ_ExtendedResourceAttributeColumn,
    eTJ_ListType,
    eTJ_ToolTip,
    eTJ_ListItem,
    eTJ_Width,
    eTJ_CellColor,
    eTJ_Caption,
    ExportAttribute,
    eTJ_ResourceAttributes,
    eTJ_HideTask,
    eTJ_HideResource,
    eTJ_End,
    eTJ_Scenarios,
    eTJ_TaskAttributes,
    eTJ_Start,
    eTJ_Period,
    eTJ_RollupTask,
    eTJ_RollupResource,
    eTJ_Definitions,
    LimitsAttribute,
    eTJ_WeeklyMax,
    eTJ_Minimum,
    eTJ_MonthlyMin,
    eTJ_WeeklyMin,
    eTJ_DailyMin,
    eTJ_Maximum,
    eTJ_MonthlyMax,
    eTJ_DailyMax,
    ProjectAttribute,
    eTJ_YearlyWorkingDays,
    eTJ_ExtendResource,
    eTJ_ShortTimeFormat,
    eTJ_TrackingScenario,
    eTJ_JournalEntry,
    eTJ_WeekStarts,
    eTJ_WorkingHours,
    eTJ_Now,
    eTJ_Scenario,
    eTJ_Include,
    eTJ_Timezone,
    eTJ_TimeFormat,
    eTJ_NumberFormat,
    eTJ_ExtendTask,
    eTJ_CurrencyFormat,
    eTJ_DailyWorkingHours,
    eTJ_TimingResolution,
    eTJ_Currency,
    eTJ_ISODATE,
    eTJ_Credit,
    eTJ_Copyright,
    eTJ_Complete,
    eTJ_Column,
    eTJ_Columns,
    eTJ_Interval4,
    eTJ_Booking,
    eTJ_BookingResource,
    eTJ_BookingTask,
    eTJ_NavigatorAttribute,
    eTJ_Navigator,
    eTJ_AllocateResourceAttribute,
    eTJ_AllocateResource,
    eTJ_Allocate,
    eTJ_ResourceAttribute,
    eTJ_Resource,
    eTJ_Balance,
    StatusStatusSheetAttribute,
    eTJ_Summary,
    eTJ_Flags,
    eTJ_Details,
    eTJ_Author,
    JournalAttributeValues,
    ChargeApplies,
    CriterionDirection,
    LeaveType,
    JournalEntrySortCriterion,
    PurgeTaskAttribute,
    PurgeReportAttribute,
    SelectArgument,
    PurgeResourceAttribute,
    AlertLevel,
    JournalModeValue,
    YesNo,
    TimeUnit,
    Justification,
    LoadDisplayUnit,
    BuildInMacro,
    Weekday,
    ScaleResolution,
    SchedulingPolicy,
    WorkQuantityUnit,
    ReportFormat,
    ColumnId,
    DependsPolicy,
    ListTypeValues,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(LogicalExpression)


def test_logicalexpression_constructor_exists():
    assert callable(LogicalExpression.__init__)


def test_logicalexpression_constructor_args():
    sig = inspect.signature(LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_etj_logicaldateliteral_is_not_abstract():
    assert not inspect.isabstract(eTJ_LogicalDateLiteral)


def test_etj_logicaldateliteral_constructor_exists():
    assert callable(eTJ_LogicalDateLiteral.__init__)


def test_etj_logicaldateliteral_constructor_args():
    sig = inspect.signature(eTJ_LogicalDateLiteral.__init__)
    params = list(sig.parameters.keys())



def test_etj_logicalnumeralliteral_is_not_abstract():
    assert not inspect.isabstract(eTJ_LogicalNumeralLiteral)


def test_etj_logicalnumeralliteral_constructor_exists():
    assert callable(eTJ_LogicalNumeralLiteral.__init__)


def test_etj_logicalnumeralliteral_constructor_args():
    sig = inspect.signature(eTJ_LogicalNumeralLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_etj_logicalnumeralliteral_has_value():
    assert hasattr(eTJ_LogicalNumeralLiteral, "value")
    descriptor = None
    for klass in eTJ_LogicalNumeralLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj_logicalabsoluteidexression_is_not_abstract():
    assert not inspect.isabstract(eTJ_LogicalAbsoluteIdExression)


def test_etj_logicalabsoluteidexression_constructor_exists():
    assert callable(eTJ_LogicalAbsoluteIdExression.__init__)


def test_etj_logicalabsoluteidexression_constructor_args():
    sig = inspect.signature(eTJ_LogicalAbsoluteIdExression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_etj_logicalabsoluteidexression_has_value():
    assert hasattr(eTJ_LogicalAbsoluteIdExression, "value")
    descriptor = None
    for klass in eTJ_LogicalAbsoluteIdExression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj_logicalflagexpression_is_not_abstract():
    assert not inspect.isabstract(eTJ_LogicalFlagExpression)


def test_etj_logicalflagexpression_constructor_exists():
    assert callable(eTJ_LogicalFlagExpression.__init__)


def test_etj_logicalflagexpression_constructor_args():
    sig = inspect.signature(eTJ_LogicalFlagExpression.__init__)
    params = list(sig.parameters.keys())
    assert "columId" in params, "Missing parameter 'columId'"

def test_etj_logicalflagexpression_has_columId():
    assert hasattr(eTJ_LogicalFlagExpression, "columId")
    descriptor = None
    for klass in eTJ_LogicalFlagExpression.__mro__:
        if "columId" in klass.__dict__:
            descriptor = klass.__dict__["columId"]
            break
    assert isinstance(descriptor, property)



def test_etj_logicalbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(eTJ_LogicalBooleanLiteral)


def test_etj_logicalbooleanliteral_constructor_exists():
    assert callable(eTJ_LogicalBooleanLiteral.__init__)


def test_etj_logicalbooleanliteral_constructor_args():
    sig = inspect.signature(eTJ_LogicalBooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "isTrue" in params, "Missing parameter 'isTrue'"

def test_etj_logicalbooleanliteral_has_isTrue():
    assert hasattr(eTJ_LogicalBooleanLiteral, "isTrue")
    descriptor = None
    for klass in eTJ_LogicalBooleanLiteral.__mro__:
        if "isTrue" in klass.__dict__:
            descriptor = klass.__dict__["isTrue"]
            break
    assert isinstance(descriptor, property)



def test_etj_logicalstringliteral_is_not_abstract():
    assert not inspect.isabstract(eTJ_LogicalStringLiteral)


def test_etj_logicalstringliteral_constructor_exists():
    assert callable(eTJ_LogicalStringLiteral.__init__)


def test_etj_logicalstringliteral_constructor_args():
    sig = inspect.signature(eTJ_LogicalStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_etj_logicalstringliteral_has_value():
    assert hasattr(eTJ_LogicalStringLiteral, "value")
    descriptor = None
    for klass in eTJ_LogicalStringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj_logicalfunctionexpression_is_not_abstract():
    assert not inspect.isabstract(eTJ_LogicalFunctionExpression)


def test_etj_logicalfunctionexpression_constructor_exists():
    assert callable(eTJ_LogicalFunctionExpression.__init__)


def test_etj_logicalfunctionexpression_constructor_args():
    sig = inspect.signature(eTJ_LogicalFunctionExpression.__init__)
    params = list(sig.parameters.keys())



def test_definitions_is_not_abstract():
    assert not inspect.isabstract(Definitions)


def test_definitions_constructor_exists():
    assert callable(Definitions.__init__)


def test_definitions_constructor_args():
    sig = inspect.signature(Definitions.__init__)
    params = list(sig.parameters.keys())



def test_etj_defintions_is_not_abstract():
    assert not inspect.isabstract(eTJ_Defintions)


def test_etj_defintions_constructor_exists():
    assert callable(eTJ_Defintions.__init__)


def test_etj_defintions_constructor_args():
    sig = inspect.signature(eTJ_Defintions.__init__)
    params = list(sig.parameters.keys())
    assert "project" in params, "Missing parameter 'project'"
    assert "flags" in params, "Missing parameter 'flags'"
    assert "tasks" in params, "Missing parameter 'tasks'"
    assert "resources" in params, "Missing parameter 'resources'"
    assert "projectids" in params, "Missing parameter 'projectids'"

def test_etj_defintions_has_project():
    assert hasattr(eTJ_Defintions, "project")
    descriptor = None
    for klass in eTJ_Defintions.__mro__:
        if "project" in klass.__dict__:
            descriptor = klass.__dict__["project"]
            break
    assert isinstance(descriptor, property)

def test_etj_defintions_has_flags():
    assert hasattr(eTJ_Defintions, "flags")
    descriptor = None
    for klass in eTJ_Defintions.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)

def test_etj_defintions_has_tasks():
    assert hasattr(eTJ_Defintions, "tasks")
    descriptor = None
    for klass in eTJ_Defintions.__mro__:
        if "tasks" in klass.__dict__:
            descriptor = klass.__dict__["tasks"]
            break
    assert isinstance(descriptor, property)

def test_etj_defintions_has_resources():
    assert hasattr(eTJ_Defintions, "resources")
    descriptor = None
    for klass in eTJ_Defintions.__mro__:
        if "resources" in klass.__dict__:
            descriptor = klass.__dict__["resources"]
            break
    assert isinstance(descriptor, property)

def test_etj_defintions_has_projectids():
    assert hasattr(eTJ_Defintions, "projectids")
    descriptor = None
    for klass in eTJ_Defintions.__mro__:
        if "projectids" in klass.__dict__:
            descriptor = klass.__dict__["projectids"]
            break
    assert isinstance(descriptor, property)



def test_etj_extdate_is_not_abstract():
    assert not inspect.isabstract(eTJ_ExtDate)


def test_etj_extdate_constructor_exists():
    assert callable(eTJ_ExtDate.__init__)


def test_etj_extdate_constructor_args():
    sig = inspect.signature(eTJ_ExtDate.__init__)
    params = list(sig.parameters.keys())



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



def test_etj_realformat_is_not_abstract():
    assert not inspect.isabstract(eTJ_RealFormat)


def test_etj_realformat_constructor_exists():
    assert callable(eTJ_RealFormat.__init__)


def test_etj_realformat_constructor_args():
    sig = inspect.signature(eTJ_RealFormat.__init__)
    params = list(sig.parameters.keys())
    assert "fractionSeparator" in params, "Missing parameter 'fractionSeparator'"
    assert "thousandsSeparator" in params, "Missing parameter 'thousandsSeparator'"
    assert "fractionDigits" in params, "Missing parameter 'fractionDigits'"
    assert "negativeSuffix" in params, "Missing parameter 'negativeSuffix'"
    assert "negativePrefix" in params, "Missing parameter 'negativePrefix'"

def test_etj_realformat_has_fractionSeparator():
    assert hasattr(eTJ_RealFormat, "fractionSeparator")
    descriptor = None
    for klass in eTJ_RealFormat.__mro__:
        if "fractionSeparator" in klass.__dict__:
            descriptor = klass.__dict__["fractionSeparator"]
            break
    assert isinstance(descriptor, property)

def test_etj_realformat_has_thousandsSeparator():
    assert hasattr(eTJ_RealFormat, "thousandsSeparator")
    descriptor = None
    for klass in eTJ_RealFormat.__mro__:
        if "thousandsSeparator" in klass.__dict__:
            descriptor = klass.__dict__["thousandsSeparator"]
            break
    assert isinstance(descriptor, property)

def test_etj_realformat_has_fractionDigits():
    assert hasattr(eTJ_RealFormat, "fractionDigits")
    descriptor = None
    for klass in eTJ_RealFormat.__mro__:
        if "fractionDigits" in klass.__dict__:
            descriptor = klass.__dict__["fractionDigits"]
            break
    assert isinstance(descriptor, property)

def test_etj_realformat_has_negativeSuffix():
    assert hasattr(eTJ_RealFormat, "negativeSuffix")
    descriptor = None
    for klass in eTJ_RealFormat.__mro__:
        if "negativeSuffix" in klass.__dict__:
            descriptor = klass.__dict__["negativeSuffix"]
            break
    assert isinstance(descriptor, property)

def test_etj_realformat_has_negativePrefix():
    assert hasattr(eTJ_RealFormat, "negativePrefix")
    descriptor = None
    for klass in eTJ_RealFormat.__mro__:
        if "negativePrefix" in klass.__dict__:
            descriptor = klass.__dict__["negativePrefix"]
            break
    assert isinstance(descriptor, property)



def test_etj_limitattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_LimitAttribute)


def test_etj_limitattribute_constructor_exists():
    assert callable(eTJ_LimitAttribute.__init__)


def test_etj_limitattribute_constructor_args():
    sig = inspect.signature(eTJ_LimitAttribute.__init__)
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



def test_etj_richtext_is_not_abstract():
    assert not inspect.isabstract(eTJ_RichText)


def test_etj_richtext_constructor_exists():
    assert callable(eTJ_RichText.__init__)


def test_etj_richtext_constructor_args():
    sig = inspect.signature(eTJ_RichText.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_etj_richtext_has_text():
    assert hasattr(eTJ_RichText, "text")
    descriptor = None
    for klass in eTJ_RichText.__mro__:
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



def test_etj_columnattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_ColumnAttribute)


def test_etj_columnattribute_constructor_exists():
    assert callable(eTJ_ColumnAttribute.__init__)


def test_etj_columnattribute_constructor_args():
    sig = inspect.signature(eTJ_ColumnAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_workhours_is_not_abstract():
    assert not inspect.isabstract(eTJ_WorkHours)


def test_etj_workhours_constructor_exists():
    assert callable(eTJ_WorkHours.__init__)


def test_etj_workhours_constructor_args():
    sig = inspect.signature(eTJ_WorkHours.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "stop" in params, "Missing parameter 'stop'"

def test_etj_workhours_has_start():
    assert hasattr(eTJ_WorkHours, "start")
    descriptor = None
    for klass in eTJ_WorkHours.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_etj_workhours_has_stop():
    assert hasattr(eTJ_WorkHours, "stop")
    descriptor = None
    for klass in eTJ_WorkHours.__mro__:
        if "stop" in klass.__dict__:
            descriptor = klass.__dict__["stop"]
            break
    assert isinstance(descriptor, property)



def test_etj_weekdays_is_not_abstract():
    assert not inspect.isabstract(eTJ_Weekdays)


def test_etj_weekdays_constructor_exists():
    assert callable(eTJ_Weekdays.__init__)


def test_etj_weekdays_constructor_args():
    sig = inspect.signature(eTJ_Weekdays.__init__)
    params = list(sig.parameters.keys())
    assert "first" in params, "Missing parameter 'first'"
    assert "last" in params, "Missing parameter 'last'"

def test_etj_weekdays_has_first():
    assert hasattr(eTJ_Weekdays, "first")
    descriptor = None
    for klass in eTJ_Weekdays.__mro__:
        if "first" in klass.__dict__:
            descriptor = klass.__dict__["first"]
            break
    assert isinstance(descriptor, property)

def test_etj_weekdays_has_last():
    assert hasattr(eTJ_Weekdays, "last")
    descriptor = None
    for klass in eTJ_Weekdays.__mro__:
        if "last" in klass.__dict__:
            descriptor = klass.__dict__["last"]
            break
    assert isinstance(descriptor, property)



def test_weeklymin_is_not_abstract():
    assert not inspect.isabstract(WeeklyMin)


def test_weeklymin_constructor_exists():
    assert callable(WeeklyMin.__init__)


def test_weeklymin_constructor_args():
    sig = inspect.signature(WeeklyMin.__init__)
    params = list(sig.parameters.keys())



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



def test_etj_limit_is_not_abstract():
    assert not inspect.isabstract(eTJ_Limit)


def test_etj_limit_constructor_exists():
    assert callable(eTJ_Limit.__init__)


def test_etj_limit_constructor_args():
    sig = inspect.signature(eTJ_Limit.__init__)
    params = list(sig.parameters.keys())



def test_gaplength_is_not_abstract():
    assert not inspect.isabstract(GapLength)


def test_gaplength_constructor_exists():
    assert callable(GapLength.__init__)


def test_gaplength_constructor_args():
    sig = inspect.signature(GapLength.__init__)
    params = list(sig.parameters.keys())



def test_gapduration_is_not_abstract():
    assert not inspect.isabstract(GapDuration)


def test_gapduration_constructor_exists():
    assert callable(GapDuration.__init__)


def test_gapduration_constructor_args():
    sig = inspect.signature(GapDuration.__init__)
    params = list(sig.parameters.keys())



def test_etj_treelevel_is_not_abstract():
    assert not inspect.isabstract(eTJ_TreeLevel)


def test_etj_treelevel_constructor_exists():
    assert callable(eTJ_TreeLevel.__init__)


def test_etj_treelevel_constructor_args():
    sig = inspect.signature(eTJ_TreeLevel.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_etj_treelevel_has_level():
    assert hasattr(eTJ_TreeLevel, "level")
    descriptor = None
    for klass in eTJ_TreeLevel.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_etj_timesheetreportattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_TimesheetReportAttribute)


def test_etj_timesheetreportattribute_constructor_exists():
    assert callable(eTJ_TimesheetReportAttribute.__init__)


def test_etj_timesheetreportattribute_constructor_args():
    sig = inspect.signature(eTJ_TimesheetReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_timesheetattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_TimesheetAttribute)


def test_etj_timesheetattribute_constructor_exists():
    assert callable(eTJ_TimesheetAttribute.__init__)


def test_etj_timesheetattribute_constructor_args():
    sig = inspect.signature(eTJ_TimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_tasktimesheetattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_TaskTimesheetAttribute)


def test_etj_tasktimesheetattribute_constructor_exists():
    assert callable(eTJ_TaskTimesheetAttribute.__init__)


def test_etj_tasktimesheetattribute_constructor_args():
    sig = inspect.signature(eTJ_TaskTimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_taskstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_TaskStatusSheetAttribute)


def test_etj_taskstatussheetattribute_constructor_exists():
    assert callable(eTJ_TaskStatusSheetAttribute.__init__)


def test_etj_taskstatussheetattribute_constructor_args():
    sig = inspect.signature(eTJ_TaskStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_statussheetattribute_is_not_abstract():
    assert not inspect.isabstract(StatusSheetAttribute)


def test_statussheetattribute_constructor_exists():
    assert callable(StatusSheetAttribute.__init__)


def test_statussheetattribute_constructor_args():
    sig = inspect.signature(StatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_allocateresourceattribute_is_not_abstract():
    assert not inspect.isabstract(AllocateResourceAttribute)


def test_allocateresourceattribute_constructor_exists():
    assert callable(AllocateResourceAttribute.__init__)


def test_allocateresourceattribute_constructor_args():
    sig = inspect.signature(AllocateResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_alternative_is_not_abstract():
    assert not inspect.isabstract(eTJ_Alternative)


def test_etj_alternative_constructor_exists():
    assert callable(eTJ_Alternative.__init__)


def test_etj_alternative_constructor_args():
    sig = inspect.signature(eTJ_Alternative.__init__)
    params = list(sig.parameters.keys())



def test_etj_alert_is_not_abstract():
    assert not inspect.isabstract(eTJ_Alert)


def test_etj_alert_constructor_exists():
    assert callable(eTJ_Alert.__init__)


def test_etj_alert_constructor_args():
    sig = inspect.signature(eTJ_Alert.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_etj_alert_has_level():
    assert hasattr(eTJ_Alert, "level")
    descriptor = None
    for klass in eTJ_Alert.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_etj_nikureportattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_NikuReportAttribute)


def test_etj_nikureportattribute_constructor_exists():
    assert callable(eTJ_NikuReportAttribute.__init__)


def test_etj_nikureportattribute_constructor_args():
    sig = inspect.signature(eTJ_NikuReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_newtaskattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_NewTaskAttribute)


def test_etj_newtaskattribute_constructor_exists():
    assert callable(eTJ_NewTaskAttribute.__init__)


def test_etj_newtaskattribute_constructor_args():
    sig = inspect.signature(eTJ_NewTaskAttribute.__init__)
    params = list(sig.parameters.keys())



def test_timesheetattribute_is_not_abstract():
    assert not inspect.isabstract(TimesheetAttribute)


def test_timesheetattribute_constructor_exists():
    assert callable(TimesheetAttribute.__init__)


def test_timesheetattribute_constructor_args():
    sig = inspect.signature(TimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_tasktimesheet_is_not_abstract():
    assert not inspect.isabstract(eTJ_TaskTimesheet)


def test_etj_tasktimesheet_constructor_exists():
    assert callable(eTJ_TaskTimesheet.__init__)


def test_etj_tasktimesheet_constructor_args():
    sig = inspect.signature(eTJ_TaskTimesheet.__init__)
    params = list(sig.parameters.keys())



def test_etj_newtask_is_not_abstract():
    assert not inspect.isabstract(eTJ_NewTask)


def test_etj_newtask_constructor_exists():
    assert callable(eTJ_NewTask.__init__)


def test_etj_newtask_constructor_args():
    sig = inspect.signature(eTJ_NewTask.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "id" in params, "Missing parameter 'id'"

def test_etj_newtask_has_text():
    assert hasattr(eTJ_NewTask, "text")
    descriptor = None
    for klass in eTJ_NewTask.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_etj_newtask_has_id():
    assert hasattr(eTJ_NewTask, "id")
    descriptor = None
    for klass in eTJ_NewTask.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_extdate_is_not_abstract():
    assert not inspect.isabstract(ExtDate)


def test_extdate_constructor_exists():
    assert callable(ExtDate.__init__)


def test_extdate_constructor_args():
    sig = inspect.signature(ExtDate.__init__)
    params = list(sig.parameters.keys())



def test_start_is_not_abstract():
    assert not inspect.isabstract(Start)


def test_start_constructor_exists():
    assert callable(Start.__init__)


def test_start_constructor_args():
    sig = inspect.signature(Start.__init__)
    params = list(sig.parameters.keys())



def test_end_is_not_abstract():
    assert not inspect.isabstract(End)


def test_end_constructor_exists():
    assert callable(End.__init__)


def test_end_constructor_args():
    sig = inspect.signature(End.__init__)
    params = list(sig.parameters.keys())



def test_etj_macrocall_is_not_abstract():
    assert not inspect.isabstract(eTJ_MacroCall)


def test_etj_macrocall_constructor_exists():
    assert callable(eTJ_MacroCall.__init__)


def test_etj_macrocall_constructor_args():
    sig = inspect.signature(eTJ_MacroCall.__init__)
    params = list(sig.parameters.keys())
    assert "buildin" in params, "Missing parameter 'buildin'"

def test_etj_macrocall_has_buildin():
    assert hasattr(eTJ_MacroCall, "buildin")
    descriptor = None
    for klass in eTJ_MacroCall.__mro__:
        if "buildin" in klass.__dict__:
            descriptor = klass.__dict__["buildin"]
            break
    assert isinstance(descriptor, property)



def test_etj_eobject_is_not_abstract():
    assert not inspect.isabstract(eTJ_EObject)


def test_etj_eobject_constructor_exists():
    assert callable(eTJ_EObject.__init__)


def test_etj_eobject_constructor_args():
    sig = inspect.signature(eTJ_EObject.__init__)
    params = list(sig.parameters.keys())



def test_etj_taskattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_TaskAttribute)


def test_etj_taskattribute_constructor_exists():
    assert callable(eTJ_TaskAttribute.__init__)


def test_etj_taskattribute_constructor_args():
    sig = inspect.signature(eTJ_TaskAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_projectattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_ProjectAttribute)


def test_etj_projectattribute_constructor_exists():
    assert callable(eTJ_ProjectAttribute.__init__)


def test_etj_projectattribute_constructor_args():
    sig = inspect.signature(eTJ_ProjectAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_exportattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_ExportAttribute)


def test_etj_exportattribute_constructor_exists():
    assert callable(eTJ_ExportAttribute.__init__)


def test_etj_exportattribute_constructor_args():
    sig = inspect.signature(eTJ_ExportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_icalreportattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_IcalReportAttribute)


def test_etj_icalreportattribute_constructor_exists():
    assert callable(eTJ_IcalReportAttribute.__init__)


def test_etj_icalreportattribute_constructor_args():
    sig = inspect.signature(eTJ_IcalReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_reportattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_ReportAttribute)


def test_etj_reportattribute_constructor_exists():
    assert callable(eTJ_ReportAttribute.__init__)


def test_etj_reportattribute_constructor_args():
    sig = inspect.signature(eTJ_ReportAttribute.__init__)
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



def test_etj_report_is_not_abstract():
    assert not inspect.isabstract(eTJ_Report)


def test_etj_report_constructor_exists():
    assert callable(eTJ_Report.__init__)


def test_etj_report_constructor_args():
    sig = inspect.signature(eTJ_Report.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_etj_report_has_name():
    assert hasattr(eTJ_Report, "name")
    descriptor = None
    for klass in eTJ_Report.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_etj_report_has_id():
    assert hasattr(eTJ_Report, "id")
    descriptor = None
    for klass in eTJ_Report.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_etj_accountattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_AccountAttribute)


def test_etj_accountattribute_constructor_exists():
    assert callable(eTJ_AccountAttribute.__init__)


def test_etj_accountattribute_constructor_args():
    sig = inspect.signature(eTJ_AccountAttribute.__init__)
    params = list(sig.parameters.keys())



def test_accountattribute_is_not_abstract():
    assert not inspect.isabstract(AccountAttribute)


def test_accountattribute_constructor_exists():
    assert callable(AccountAttribute.__init__)


def test_accountattribute_constructor_args():
    sig = inspect.signature(AccountAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_interval2_is_not_abstract():
    assert not inspect.isabstract(eTJ_Interval2)


def test_etj_interval2_constructor_exists():
    assert callable(eTJ_Interval2.__init__)


def test_etj_interval2_constructor_args():
    sig = inspect.signature(eTJ_Interval2.__init__)
    params = list(sig.parameters.keys())



def test_reportattribute_is_not_abstract():
    assert not inspect.isabstract(ReportAttribute)


def test_reportattribute_constructor_exists():
    assert callable(ReportAttribute.__init__)


def test_reportattribute_constructor_args():
    sig = inspect.signature(ReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_taskroot_is_not_abstract():
    assert not inspect.isabstract(eTJ_TaskRoot)


def test_etj_taskroot_constructor_exists():
    assert callable(eTJ_TaskRoot.__init__)


def test_etj_taskroot_constructor_args():
    sig = inspect.signature(eTJ_TaskRoot.__init__)
    params = list(sig.parameters.keys())



def test_etj_accountroot_is_not_abstract():
    assert not inspect.isabstract(eTJ_AccountRoot)


def test_etj_accountroot_constructor_exists():
    assert callable(eTJ_AccountRoot.__init__)


def test_etj_accountroot_constructor_args():
    sig = inspect.signature(eTJ_AccountRoot.__init__)
    params = list(sig.parameters.keys())



def test_includepropertiesattribute_is_not_abstract():
    assert not inspect.isabstract(IncludePropertiesAttribute)


def test_includepropertiesattribute_constructor_exists():
    assert callable(IncludePropertiesAttribute.__init__)


def test_includepropertiesattribute_constructor_args():
    sig = inspect.signature(IncludePropertiesAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_taskprefix_is_not_abstract():
    assert not inspect.isabstract(eTJ_TaskPrefix)


def test_etj_taskprefix_constructor_exists():
    assert callable(eTJ_TaskPrefix.__init__)


def test_etj_taskprefix_constructor_args():
    sig = inspect.signature(eTJ_TaskPrefix.__init__)
    params = list(sig.parameters.keys())



def test_etj_accountprefix_is_not_abstract():
    assert not inspect.isabstract(eTJ_AccountPrefix)


def test_etj_accountprefix_constructor_exists():
    assert callable(eTJ_AccountPrefix.__init__)


def test_etj_accountprefix_constructor_args():
    sig = inspect.signature(eTJ_AccountPrefix.__init__)
    params = list(sig.parameters.keys())



def test_etj_property_is_not_abstract():
    assert not inspect.isabstract(eTJ_Property)


def test_etj_property_constructor_exists():
    assert callable(eTJ_Property.__init__)


def test_etj_property_constructor_args():
    sig = inspect.signature(eTJ_Property.__init__)
    params = list(sig.parameters.keys())



def test_etj_project_is_not_abstract():
    assert not inspect.isabstract(eTJ_Project)


def test_etj_project_constructor_exists():
    assert callable(eTJ_Project.__init__)


def test_etj_project_constructor_args():
    sig = inspect.signature(eTJ_Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"
    assert "id" in params, "Missing parameter 'id'"

def test_etj_project_has_name():
    assert hasattr(eTJ_Project, "name")
    descriptor = None
    for klass in eTJ_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_etj_project_has_version():
    assert hasattr(eTJ_Project, "version")
    descriptor = None
    for klass in eTJ_Project.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_etj_project_has_id():
    assert hasattr(eTJ_Project, "id")
    descriptor = None
    for klass in eTJ_Project.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_etj_global_is_not_abstract():
    assert not inspect.isabstract(eTJ_Global)


def test_etj_global_constructor_exists():
    assert callable(eTJ_Global.__init__)


def test_etj_global_constructor_args():
    sig = inspect.signature(eTJ_Global.__init__)
    params = list(sig.parameters.keys())



def test_etj_interval3_is_not_abstract():
    assert not inspect.isabstract(eTJ_Interval3)


def test_etj_interval3_constructor_exists():
    assert callable(eTJ_Interval3.__init__)


def test_etj_interval3_constructor_args():
    sig = inspect.signature(eTJ_Interval3.__init__)
    params = list(sig.parameters.keys())



def test_etj_leavedetails_is_not_abstract():
    assert not inspect.isabstract(eTJ_LeaveDetails)


def test_etj_leavedetails_constructor_exists():
    assert callable(eTJ_LeaveDetails.__init__)


def test_etj_leavedetails_constructor_args():
    sig = inspect.signature(eTJ_LeaveDetails.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_etj_leavedetails_has_name():
    assert hasattr(eTJ_LeaveDetails, "name")
    descriptor = None
    for klass in eTJ_LeaveDetails.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_etj_leavedetails_has_type():
    assert hasattr(eTJ_LeaveDetails, "type")
    descriptor = None
    for klass in eTJ_LeaveDetails.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_resourceattribute_is_not_abstract():
    assert not inspect.isabstract(ResourceAttribute)


def test_resourceattribute_constructor_exists():
    assert callable(ResourceAttribute.__init__)


def test_resourceattribute_constructor_args():
    sig = inspect.signature(ResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_warn_is_not_abstract():
    assert not inspect.isabstract(eTJ_Warn)


def test_etj_warn_constructor_exists():
    assert callable(eTJ_Warn.__init__)


def test_etj_warn_constructor_args():
    sig = inspect.signature(eTJ_Warn.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_etj_icalreport_is_not_abstract():
    assert not inspect.isabstract(eTJ_IcalReport)


def test_etj_icalreport_constructor_exists():
    assert callable(eTJ_IcalReport.__init__)


def test_etj_icalreport_constructor_args():
    sig = inspect.signature(eTJ_IcalReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_etj_icalreport_has_filename():
    assert hasattr(eTJ_IcalReport, "filename")
    descriptor = None
    for klass in eTJ_IcalReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_etj_macro_is_not_abstract():
    assert not inspect.isabstract(eTJ_Macro)


def test_etj_macro_constructor_exists():
    assert callable(eTJ_Macro.__init__)


def test_etj_macro_constructor_args():
    sig = inspect.signature(eTJ_Macro.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "value" in params, "Missing parameter 'value'"

def test_etj_macro_has_id():
    assert hasattr(eTJ_Macro, "id")
    descriptor = None
    for klass in eTJ_Macro.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_etj_macro_has_value():
    assert hasattr(eTJ_Macro, "value")
    descriptor = None
    for klass in eTJ_Macro.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj_nikureport_is_not_abstract():
    assert not inspect.isabstract(eTJ_NikuReport)


def test_etj_nikureport_constructor_exists():
    assert callable(eTJ_NikuReport.__init__)


def test_etj_nikureport_constructor_args():
    sig = inspect.signature(eTJ_NikuReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_etj_nikureport_has_filename():
    assert hasattr(eTJ_NikuReport, "filename")
    descriptor = None
    for klass in eTJ_NikuReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_etj_textreport_is_not_abstract():
    assert not inspect.isabstract(eTJ_TextReport)


def test_etj_textreport_constructor_exists():
    assert callable(eTJ_TextReport.__init__)


def test_etj_textreport_constructor_args():
    sig = inspect.signature(eTJ_TextReport.__init__)
    params = list(sig.parameters.keys())



def test_etj_timesheetreport_is_not_abstract():
    assert not inspect.isabstract(eTJ_TimesheetReport)


def test_etj_timesheetreport_constructor_exists():
    assert callable(eTJ_TimesheetReport.__init__)


def test_etj_timesheetreport_constructor_args():
    sig = inspect.signature(eTJ_TimesheetReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_etj_timesheetreport_has_filename():
    assert hasattr(eTJ_TimesheetReport, "filename")
    descriptor = None
    for klass in eTJ_TimesheetReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_etj_account_is_not_abstract():
    assert not inspect.isabstract(eTJ_Account)


def test_etj_account_constructor_exists():
    assert callable(eTJ_Account.__init__)


def test_etj_account_constructor_args():
    sig = inspect.signature(eTJ_Account.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_etj_account_has_id():
    assert hasattr(eTJ_Account, "id")
    descriptor = None
    for klass in eTJ_Account.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_etj_account_has_name():
    assert hasattr(eTJ_Account, "name")
    descriptor = None
    for klass in eTJ_Account.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_etj_timesheet_is_not_abstract():
    assert not inspect.isabstract(eTJ_Timesheet)


def test_etj_timesheet_constructor_exists():
    assert callable(eTJ_Timesheet.__init__)


def test_etj_timesheet_constructor_args():
    sig = inspect.signature(eTJ_Timesheet.__init__)
    params = list(sig.parameters.keys())



def test_etj_taskreport_is_not_abstract():
    assert not inspect.isabstract(eTJ_TaskReport)


def test_etj_taskreport_constructor_exists():
    assert callable(eTJ_TaskReport.__init__)


def test_etj_taskreport_constructor_args():
    sig = inspect.signature(eTJ_TaskReport.__init__)
    params = list(sig.parameters.keys())



def test_etj_task_is_not_abstract():
    assert not inspect.isabstract(eTJ_Task)


def test_etj_task_constructor_exists():
    assert callable(eTJ_Task.__init__)


def test_etj_task_constructor_args():
    sig = inspect.signature(eTJ_Task.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_etj_task_has_id():
    assert hasattr(eTJ_Task, "id")
    descriptor = None
    for klass in eTJ_Task.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_etj_task_has_name():
    assert hasattr(eTJ_Task, "name")
    descriptor = None
    for klass in eTJ_Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_etj_accountreport_is_not_abstract():
    assert not inspect.isabstract(eTJ_AccountReport)


def test_etj_accountreport_constructor_exists():
    assert callable(eTJ_AccountReport.__init__)


def test_etj_accountreport_constructor_args():
    sig = inspect.signature(eTJ_AccountReport.__init__)
    params = list(sig.parameters.keys())



def test_etj_export_is_not_abstract():
    assert not inspect.isabstract(eTJ_Export)


def test_etj_export_constructor_exists():
    assert callable(eTJ_Export.__init__)


def test_etj_export_constructor_args():
    sig = inspect.signature(eTJ_Export.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"
    assert "id" in params, "Missing parameter 'id'"

def test_etj_export_has_filename():
    assert hasattr(eTJ_Export, "filename")
    descriptor = None
    for klass in eTJ_Export.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_etj_export_has_id():
    assert hasattr(eTJ_Export, "id")
    descriptor = None
    for klass in eTJ_Export.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_etj_leaves_is_not_abstract():
    assert not inspect.isabstract(eTJ_Leaves)


def test_etj_leaves_constructor_exists():
    assert callable(eTJ_Leaves.__init__)


def test_etj_leaves_constructor_args():
    sig = inspect.signature(eTJ_Leaves.__init__)
    params = list(sig.parameters.keys())



def test_etj_supplementaccount_is_not_abstract():
    assert not inspect.isabstract(eTJ_SupplementAccount)


def test_etj_supplementaccount_constructor_exists():
    assert callable(eTJ_SupplementAccount.__init__)


def test_etj_supplementaccount_constructor_args():
    sig = inspect.signature(eTJ_SupplementAccount.__init__)
    params = list(sig.parameters.keys())



def test_etj_statussheetreportattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_StatusSheetReportAttribute)


def test_etj_statussheetreportattribute_constructor_exists():
    assert callable(eTJ_StatusSheetReportAttribute.__init__)


def test_etj_statussheetreportattribute_constructor_args():
    sig = inspect.signature(eTJ_StatusSheetReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_statussheetreport_is_not_abstract():
    assert not inspect.isabstract(eTJ_StatusSheetReport)


def test_etj_statussheetreport_constructor_exists():
    assert callable(eTJ_StatusSheetReport.__init__)


def test_etj_statussheetreport_constructor_args():
    sig = inspect.signature(eTJ_StatusSheetReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_etj_statussheetreport_has_filename():
    assert hasattr(eTJ_StatusSheetReport, "filename")
    descriptor = None
    for klass in eTJ_StatusSheetReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_etj_statussheetattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_StatusSheetAttribute)


def test_etj_statussheetattribute_constructor_exists():
    assert callable(eTJ_StatusSheetAttribute.__init__)


def test_etj_statussheetattribute_constructor_args():
    sig = inspect.signature(eTJ_StatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_statussheet_is_not_abstract():
    assert not inspect.isabstract(eTJ_StatusSheet)


def test_etj_statussheet_constructor_exists():
    assert callable(eTJ_StatusSheet.__init__)


def test_etj_statussheet_constructor_args():
    sig = inspect.signature(eTJ_StatusSheet.__init__)
    params = list(sig.parameters.keys())



def test_etj_tagfile_is_not_abstract():
    assert not inspect.isabstract(eTJ_TagFile)


def test_etj_tagfile_constructor_exists():
    assert callable(eTJ_TagFile.__init__)


def test_etj_tagfile_constructor_args():
    sig = inspect.signature(eTJ_TagFile.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "filename" in params, "Missing parameter 'filename'"

def test_etj_tagfile_has_id():
    assert hasattr(eTJ_TagFile, "id")
    descriptor = None
    for klass in eTJ_TagFile.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_etj_tagfile_has_filename():
    assert hasattr(eTJ_TagFile, "filename")
    descriptor = None
    for klass in eTJ_TagFile.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_etj_supplementtask_is_not_abstract():
    assert not inspect.isabstract(eTJ_SupplementTask)


def test_etj_supplementtask_constructor_exists():
    assert callable(eTJ_SupplementTask.__init__)


def test_etj_supplementtask_constructor_args():
    sig = inspect.signature(eTJ_SupplementTask.__init__)
    params = list(sig.parameters.keys())



def test_etj_supplementresource_is_not_abstract():
    assert not inspect.isabstract(eTJ_SupplementResource)


def test_etj_supplementresource_constructor_exists():
    assert callable(eTJ_SupplementResource.__init__)


def test_etj_supplementresource_constructor_args():
    sig = inspect.signature(eTJ_SupplementResource.__init__)
    params = list(sig.parameters.keys())



def test_etj_supplementreport_is_not_abstract():
    assert not inspect.isabstract(eTJ_SupplementReport)


def test_etj_supplementreport_constructor_exists():
    assert callable(eTJ_SupplementReport.__init__)


def test_etj_supplementreport_constructor_args():
    sig = inspect.signature(eTJ_SupplementReport.__init__)
    params = list(sig.parameters.keys())



def test_etj_sortjournalentries_is_not_abstract():
    assert not inspect.isabstract(eTJ_SortJournalEntries)


def test_etj_sortjournalentries_constructor_exists():
    assert callable(eTJ_SortJournalEntries.__init__)


def test_etj_sortjournalentries_constructor_args():
    sig = inspect.signature(eTJ_SortJournalEntries.__init__)
    params = list(sig.parameters.keys())



def test_etj_sortaccounts_is_not_abstract():
    assert not inspect.isabstract(eTJ_SortAccounts)


def test_etj_sortaccounts_constructor_exists():
    assert callable(eTJ_SortAccounts.__init__)


def test_etj_sortaccounts_constructor_args():
    sig = inspect.signature(eTJ_SortAccounts.__init__)
    params = list(sig.parameters.keys())



def test_etj_criterion_is_not_abstract():
    assert not inspect.isabstract(eTJ_Criterion)


def test_etj_criterion_constructor_exists():
    assert callable(eTJ_Criterion.__init__)


def test_etj_criterion_constructor_args():
    sig = inspect.signature(eTJ_Criterion.__init__)
    params = list(sig.parameters.keys())
    assert "columnId" in params, "Missing parameter 'columnId'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_etj_criterion_has_columnId():
    assert hasattr(eTJ_Criterion, "columnId")
    descriptor = None
    for klass in eTJ_Criterion.__mro__:
        if "columnId" in klass.__dict__:
            descriptor = klass.__dict__["columnId"]
            break
    assert isinstance(descriptor, property)

def test_etj_criterion_has_direction():
    assert hasattr(eTJ_Criterion, "direction")
    descriptor = None
    for klass in eTJ_Criterion.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
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



def test_etj_sort_is_not_abstract():
    assert not inspect.isabstract(eTJ_Sort)


def test_etj_sort_constructor_exists():
    assert callable(eTJ_Sort.__init__)


def test_etj_sort_constructor_args():
    sig = inspect.signature(eTJ_Sort.__init__)
    params = list(sig.parameters.keys())
    assert "tree" in params, "Missing parameter 'tree'"

def test_etj_sort_has_tree():
    assert hasattr(eTJ_Sort, "tree")
    descriptor = None
    for klass in eTJ_Sort.__mro__:
        if "tree" in klass.__dict__:
            descriptor = klass.__dict__["tree"]
            break
    assert isinstance(descriptor, property)



def test_etj_shiftstask_is_not_abstract():
    assert not inspect.isabstract(eTJ_ShiftsTask)


def test_etj_shiftstask_constructor_exists():
    assert callable(eTJ_ShiftsTask.__init__)


def test_etj_shiftstask_constructor_args():
    sig = inspect.signature(eTJ_ShiftsTask.__init__)
    params = list(sig.parameters.keys())



def test_etj_shiftsresource_is_not_abstract():
    assert not inspect.isabstract(eTJ_ShiftsResource)


def test_etj_shiftsresource_constructor_exists():
    assert callable(eTJ_ShiftsResource.__init__)


def test_etj_shiftsresource_constructor_args():
    sig = inspect.signature(eTJ_ShiftsResource.__init__)
    params = list(sig.parameters.keys())



def test_etj_statustimesheetattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_StatusTimesheetAttribute)


def test_etj_statustimesheetattribute_constructor_exists():
    assert callable(eTJ_StatusTimesheetAttribute.__init__)


def test_etj_statustimesheetattribute_constructor_args():
    sig = inspect.signature(eTJ_StatusTimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_statusstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_StatusStatusSheetAttribute)


def test_etj_statusstatussheetattribute_constructor_exists():
    assert callable(eTJ_StatusStatusSheetAttribute.__init__)


def test_etj_statusstatussheetattribute_constructor_args():
    sig = inspect.signature(eTJ_StatusStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_taskstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(TaskStatusSheetAttribute)


def test_taskstatussheetattribute_constructor_exists():
    assert callable(TaskStatusSheetAttribute.__init__)


def test_taskstatussheetattribute_constructor_args():
    sig = inspect.signature(TaskStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_taskstatussheet_is_not_abstract():
    assert not inspect.isabstract(eTJ_TaskStatusSheet)


def test_etj_taskstatussheet_constructor_exists():
    assert callable(eTJ_TaskStatusSheet.__init__)


def test_etj_taskstatussheet_constructor_args():
    sig = inspect.signature(eTJ_TaskStatusSheet.__init__)
    params = list(sig.parameters.keys())



def test_etj_statusstatussheet_is_not_abstract():
    assert not inspect.isabstract(eTJ_StatusStatusSheet)


def test_etj_statusstatussheet_constructor_exists():
    assert callable(eTJ_StatusStatusSheet.__init__)


def test_etj_statusstatussheet_constructor_args():
    sig = inspect.signature(eTJ_StatusStatusSheet.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "text" in params, "Missing parameter 'text'"

def test_etj_statusstatussheet_has_level():
    assert hasattr(eTJ_StatusStatusSheet, "level")
    descriptor = None
    for klass in eTJ_StatusStatusSheet.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_etj_statusstatussheet_has_text():
    assert hasattr(eTJ_StatusStatusSheet, "text")
    descriptor = None
    for klass in eTJ_StatusStatusSheet.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_etj_shift_is_not_abstract():
    assert not inspect.isabstract(eTJ_Shift)


def test_etj_shift_constructor_exists():
    assert callable(eTJ_Shift.__init__)


def test_etj_shift_constructor_args():
    sig = inspect.signature(eTJ_Shift.__init__)
    params = list(sig.parameters.keys())
    assert "replace" in params, "Missing parameter 'replace'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "timezone" in params, "Missing parameter 'timezone'"

def test_etj_shift_has_replace():
    assert hasattr(eTJ_Shift, "replace")
    descriptor = None
    for klass in eTJ_Shift.__mro__:
        if "replace" in klass.__dict__:
            descriptor = klass.__dict__["replace"]
            break
    assert isinstance(descriptor, property)

def test_etj_shift_has_name():
    assert hasattr(eTJ_Shift, "name")
    descriptor = None
    for klass in eTJ_Shift.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_etj_shift_has_id():
    assert hasattr(eTJ_Shift, "id")
    descriptor = None
    for klass in eTJ_Shift.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_etj_shift_has_timezone():
    assert hasattr(eTJ_Shift, "timezone")
    descriptor = None
    for klass in eTJ_Shift.__mro__:
        if "timezone" in klass.__dict__:
            descriptor = klass.__dict__["timezone"]
            break
    assert isinstance(descriptor, property)



def test_etj_selfcontained_is_not_abstract():
    assert not inspect.isabstract(eTJ_SelfContained)


def test_etj_selfcontained_constructor_exists():
    assert callable(eTJ_SelfContained.__init__)


def test_etj_selfcontained_constructor_args():
    sig = inspect.signature(eTJ_SelfContained.__init__)
    params = list(sig.parameters.keys())
    assert "selfcontained" in params, "Missing parameter 'selfcontained'"

def test_etj_selfcontained_has_selfcontained():
    assert hasattr(eTJ_SelfContained, "selfcontained")
    descriptor = None
    for klass in eTJ_SelfContained.__mro__:
        if "selfcontained" in klass.__dict__:
            descriptor = klass.__dict__["selfcontained"]
            break
    assert isinstance(descriptor, property)



def test_etj_select_is_not_abstract():
    assert not inspect.isabstract(eTJ_Select)


def test_etj_select_constructor_exists():
    assert callable(eTJ_Select.__init__)


def test_etj_select_constructor_args():
    sig = inspect.signature(eTJ_Select.__init__)
    params = list(sig.parameters.keys())
    assert "argument" in params, "Missing parameter 'argument'"

def test_etj_select_has_argument():
    assert hasattr(eTJ_Select, "argument")
    descriptor = None
    for klass in eTJ_Select.__mro__:
        if "argument" in klass.__dict__:
            descriptor = klass.__dict__["argument"]
            break
    assert isinstance(descriptor, property)



def test_etj_scheduling_is_not_abstract():
    assert not inspect.isabstract(eTJ_Scheduling)


def test_etj_scheduling_constructor_exists():
    assert callable(eTJ_Scheduling.__init__)


def test_etj_scheduling_constructor_args():
    sig = inspect.signature(eTJ_Scheduling.__init__)
    params = list(sig.parameters.keys())
    assert "scheduling" in params, "Missing parameter 'scheduling'"

def test_etj_scheduling_has_scheduling():
    assert hasattr(eTJ_Scheduling, "scheduling")
    descriptor = None
    for klass in eTJ_Scheduling.__mro__:
        if "scheduling" in klass.__dict__:
            descriptor = klass.__dict__["scheduling"]
            break
    assert isinstance(descriptor, property)



def test_etj_scheduled_is_not_abstract():
    assert not inspect.isabstract(eTJ_Scheduled)


def test_etj_scheduled_constructor_exists():
    assert callable(eTJ_Scheduled.__init__)


def test_etj_scheduled_constructor_args():
    sig = inspect.signature(eTJ_Scheduled.__init__)
    params = list(sig.parameters.keys())
    assert "scheduled" in params, "Missing parameter 'scheduled'"

def test_etj_scheduled_has_scheduled():
    assert hasattr(eTJ_Scheduled, "scheduled")
    descriptor = None
    for klass in eTJ_Scheduled.__mro__:
        if "scheduled" in klass.__dict__:
            descriptor = klass.__dict__["scheduled"]
            break
    assert isinstance(descriptor, property)



def test_etj_shiftsallocate_is_not_abstract():
    assert not inspect.isabstract(eTJ_ShiftsAllocate)


def test_etj_shiftsallocate_constructor_exists():
    assert callable(eTJ_ShiftsAllocate.__init__)


def test_etj_shiftsallocate_constructor_args():
    sig = inspect.signature(eTJ_ShiftsAllocate.__init__)
    params = list(sig.parameters.keys())



def test_etj_shiftslimit_is_not_abstract():
    assert not inspect.isabstract(eTJ_ShiftsLimit)


def test_etj_shiftslimit_constructor_exists():
    assert callable(eTJ_ShiftsLimit.__init__)


def test_etj_shiftslimit_constructor_args():
    sig = inspect.signature(eTJ_ShiftsLimit.__init__)
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



def test_etj_shifts_is_not_abstract():
    assert not inspect.isabstract(eTJ_Shifts)


def test_etj_shifts_constructor_exists():
    assert callable(eTJ_Shifts.__init__)


def test_etj_shifts_constructor_args():
    sig = inspect.signature(eTJ_Shifts.__init__)
    params = list(sig.parameters.keys())



def test_etj_shifttimesheet_is_not_abstract():
    assert not inspect.isabstract(eTJ_ShiftTimesheet)


def test_etj_shifttimesheet_constructor_exists():
    assert callable(eTJ_ShiftTimesheet.__init__)


def test_etj_shifttimesheet_constructor_args():
    sig = inspect.signature(eTJ_ShiftTimesheet.__init__)
    params = list(sig.parameters.keys())



def test_etj_vacation_is_not_abstract():
    assert not inspect.isabstract(eTJ_Vacation)


def test_etj_vacation_constructor_exists():
    assert callable(eTJ_Vacation.__init__)


def test_etj_vacation_constructor_args():
    sig = inspect.signature(eTJ_Vacation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_etj_vacation_has_name():
    assert hasattr(eTJ_Vacation, "name")
    descriptor = None
    for klass in eTJ_Vacation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_etj_rollupaccount_is_not_abstract():
    assert not inspect.isabstract(eTJ_RollupAccount)


def test_etj_rollupaccount_constructor_exists():
    assert callable(eTJ_RollupAccount.__init__)


def test_etj_rollupaccount_constructor_args():
    sig = inspect.signature(eTJ_RollupAccount.__init__)
    params = list(sig.parameters.keys())



def test_etj_right_is_not_abstract():
    assert not inspect.isabstract(eTJ_Right)


def test_etj_right_constructor_exists():
    assert callable(eTJ_Right.__init__)


def test_etj_right_constructor_args():
    sig = inspect.signature(eTJ_Right.__init__)
    params = list(sig.parameters.keys())



def test_etj_responsible_is_not_abstract():
    assert not inspect.isabstract(eTJ_Responsible)


def test_etj_responsible_constructor_exists():
    assert callable(eTJ_Responsible.__init__)


def test_etj_responsible_constructor_args():
    sig = inspect.signature(eTJ_Responsible.__init__)
    params = list(sig.parameters.keys())



def test_etj_resourceroot_is_not_abstract():
    assert not inspect.isabstract(eTJ_ResourceRoot)


def test_etj_resourceroot_constructor_exists():
    assert callable(eTJ_ResourceRoot.__init__)


def test_etj_resourceroot_constructor_args():
    sig = inspect.signature(eTJ_ResourceRoot.__init__)
    params = list(sig.parameters.keys())



def test_etj_resourcereport_is_not_abstract():
    assert not inspect.isabstract(eTJ_ResourceReport)


def test_etj_resourcereport_constructor_exists():
    assert callable(eTJ_ResourceReport.__init__)


def test_etj_resourcereport_constructor_args():
    sig = inspect.signature(eTJ_ResourceReport.__init__)
    params = list(sig.parameters.keys())



def test_etj_purgetask_is_not_abstract():
    assert not inspect.isabstract(eTJ_PurgeTask)


def test_etj_purgetask_constructor_exists():
    assert callable(eTJ_PurgeTask.__init__)


def test_etj_purgetask_constructor_args():
    sig = inspect.signature(eTJ_PurgeTask.__init__)
    params = list(sig.parameters.keys())
    assert "listAttribute" in params, "Missing parameter 'listAttribute'"

def test_etj_purgetask_has_listAttribute():
    assert hasattr(eTJ_PurgeTask, "listAttribute")
    descriptor = None
    for klass in eTJ_PurgeTask.__mro__:
        if "listAttribute" in klass.__dict__:
            descriptor = klass.__dict__["listAttribute"]
            break
    assert isinstance(descriptor, property)



def test_etj_purgeresource_is_not_abstract():
    assert not inspect.isabstract(eTJ_PurgeResource)


def test_etj_purgeresource_constructor_exists():
    assert callable(eTJ_PurgeResource.__init__)


def test_etj_purgeresource_constructor_args():
    sig = inspect.signature(eTJ_PurgeResource.__init__)
    params = list(sig.parameters.keys())
    assert "listAttribute" in params, "Missing parameter 'listAttribute'"

def test_etj_purgeresource_has_listAttribute():
    assert hasattr(eTJ_PurgeResource, "listAttribute")
    descriptor = None
    for klass in eTJ_PurgeResource.__mro__:
        if "listAttribute" in klass.__dict__:
            descriptor = klass.__dict__["listAttribute"]
            break
    assert isinstance(descriptor, property)



def test_etj_resourceprefix_is_not_abstract():
    assert not inspect.isabstract(eTJ_ResourcePrefix)


def test_etj_resourceprefix_constructor_exists():
    assert callable(eTJ_ResourcePrefix.__init__)


def test_etj_resourceprefix_constructor_args():
    sig = inspect.signature(eTJ_ResourcePrefix.__init__)
    params = list(sig.parameters.keys())



def test_etj_reportprefix_is_not_abstract():
    assert not inspect.isabstract(eTJ_ReportPrefix)


def test_etj_reportprefix_constructor_exists():
    assert callable(eTJ_ReportPrefix.__init__)


def test_etj_reportprefix_constructor_args():
    sig = inspect.signature(eTJ_ReportPrefix.__init__)
    params = list(sig.parameters.keys())



def test_etj_rate_is_not_abstract():
    assert not inspect.isabstract(eTJ_Rate)


def test_etj_rate_constructor_exists():
    assert callable(eTJ_Rate.__init__)


def test_etj_rate_constructor_args():
    sig = inspect.signature(eTJ_Rate.__init__)
    params = list(sig.parameters.keys())
    assert "rate" in params, "Missing parameter 'rate'"

def test_etj_rate_has_rate():
    assert hasattr(eTJ_Rate, "rate")
    descriptor = None
    for klass in eTJ_Rate.__mro__:
        if "rate" in klass.__dict__:
            descriptor = klass.__dict__["rate"]
            break
    assert isinstance(descriptor, property)



def test_etj_note_is_not_abstract():
    assert not inspect.isabstract(eTJ_Note)


def test_etj_note_constructor_exists():
    assert callable(eTJ_Note.__init__)


def test_etj_note_constructor_args():
    sig = inspect.signature(eTJ_Note.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"

def test_etj_note_has_note():
    assert hasattr(eTJ_Note, "note")
    descriptor = None
    for klass in eTJ_Note.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_etj_purgereport_is_not_abstract():
    assert not inspect.isabstract(eTJ_PurgeReport)


def test_etj_purgereport_constructor_exists():
    assert callable(eTJ_PurgeReport.__init__)


def test_etj_purgereport_constructor_args():
    sig = inspect.signature(eTJ_PurgeReport.__init__)
    params = list(sig.parameters.keys())
    assert "listAttribute" in params, "Missing parameter 'listAttribute'"

def test_etj_purgereport_has_listAttribute():
    assert hasattr(eTJ_PurgeReport, "listAttribute")
    descriptor = None
    for klass in eTJ_PurgeReport.__mro__:
        if "listAttribute" in klass.__dict__:
            descriptor = klass.__dict__["listAttribute"]
            break
    assert isinstance(descriptor, property)



def test_etj_prolog_is_not_abstract():
    assert not inspect.isabstract(eTJ_Prolog)


def test_etj_prolog_constructor_exists():
    assert callable(eTJ_Prolog.__init__)


def test_etj_prolog_constructor_args():
    sig = inspect.signature(eTJ_Prolog.__init__)
    params = list(sig.parameters.keys())



def test_etj_projectids_is_not_abstract():
    assert not inspect.isabstract(eTJ_ProjectIds)


def test_etj_projectids_constructor_exists():
    assert callable(eTJ_ProjectIds.__init__)


def test_etj_projectids_constructor_args():
    sig = inspect.signature(eTJ_ProjectIds.__init__)
    params = list(sig.parameters.keys())
    assert "ids" in params, "Missing parameter 'ids'"

def test_etj_projectids_has_ids():
    assert hasattr(eTJ_ProjectIds, "ids")
    descriptor = None
    for klass in eTJ_ProjectIds.__mro__:
        if "ids" in klass.__dict__:
            descriptor = klass.__dict__["ids"]
            break
    assert isinstance(descriptor, property)



def test_etj_projectid_is_not_abstract():
    assert not inspect.isabstract(eTJ_ProjectId)


def test_etj_projectid_constructor_exists():
    assert callable(eTJ_ProjectId.__init__)


def test_etj_projectid_constructor_args():
    sig = inspect.signature(eTJ_ProjectId.__init__)
    params = list(sig.parameters.keys())
    assert "projectId" in params, "Missing parameter 'projectId'"

def test_etj_projectid_has_projectId():
    assert hasattr(eTJ_ProjectId, "projectId")
    descriptor = None
    for klass in eTJ_ProjectId.__mro__:
        if "projectId" in klass.__dict__:
            descriptor = klass.__dict__["projectId"]
            break
    assert isinstance(descriptor, property)



def test_etj_precedes_is_not_abstract():
    assert not inspect.isabstract(eTJ_Precedes)


def test_etj_precedes_constructor_exists():
    assert callable(eTJ_Precedes.__init__)


def test_etj_precedes_constructor_args():
    sig = inspect.signature(eTJ_Precedes.__init__)
    params = list(sig.parameters.keys())



def test_etj_persistent_is_not_abstract():
    assert not inspect.isabstract(eTJ_Persistent)


def test_etj_persistent_constructor_exists():
    assert callable(eTJ_Persistent.__init__)


def test_etj_persistent_constructor_args():
    sig = inspect.signature(eTJ_Persistent.__init__)
    params = list(sig.parameters.keys())
    assert "persistent" in params, "Missing parameter 'persistent'"

def test_etj_persistent_has_persistent():
    assert hasattr(eTJ_Persistent, "persistent")
    descriptor = None
    for klass in eTJ_Persistent.__mro__:
        if "persistent" in klass.__dict__:
            descriptor = klass.__dict__["persistent"]
            break
    assert isinstance(descriptor, property)



def test_etj_loadunit_is_not_abstract():
    assert not inspect.isabstract(eTJ_LoadUnit)


def test_etj_loadunit_constructor_exists():
    assert callable(eTJ_LoadUnit.__init__)


def test_etj_loadunit_constructor_args():
    sig = inspect.signature(eTJ_LoadUnit.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_etj_loadunit_has_unit():
    assert hasattr(eTJ_LoadUnit, "unit")
    descriptor = None
    for klass in eTJ_LoadUnit.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_etj_limitsattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_LimitsAttribute)


def test_etj_limitsattribute_constructor_exists():
    assert callable(eTJ_LimitsAttribute.__init__)


def test_etj_limitsattribute_constructor_args():
    sig = inspect.signature(eTJ_LimitsAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_limits_is_not_abstract():
    assert not inspect.isabstract(eTJ_Limits)


def test_etj_limits_constructor_exists():
    assert callable(eTJ_Limits.__init__)


def test_etj_limits_constructor_args():
    sig = inspect.signature(eTJ_Limits.__init__)
    params = list(sig.parameters.keys())



def test_etj_minstart_is_not_abstract():
    assert not inspect.isabstract(eTJ_MinStart)


def test_etj_minstart_constructor_exists():
    assert callable(eTJ_MinStart.__init__)


def test_etj_minstart_constructor_args():
    sig = inspect.signature(eTJ_MinStart.__init__)
    params = list(sig.parameters.keys())



def test_etj_minend_is_not_abstract():
    assert not inspect.isabstract(eTJ_MinEnd)


def test_etj_minend_constructor_exists():
    assert callable(eTJ_MinEnd.__init__)


def test_etj_minend_constructor_args():
    sig = inspect.signature(eTJ_MinEnd.__init__)
    params = list(sig.parameters.keys())



def test_etj_milestone_is_not_abstract():
    assert not inspect.isabstract(eTJ_Milestone)


def test_etj_milestone_constructor_exists():
    assert callable(eTJ_Milestone.__init__)


def test_etj_milestone_constructor_args():
    sig = inspect.signature(eTJ_Milestone.__init__)
    params = list(sig.parameters.keys())
    assert "milestone" in params, "Missing parameter 'milestone'"

def test_etj_milestone_has_milestone():
    assert hasattr(eTJ_Milestone, "milestone")
    descriptor = None
    for klass in eTJ_Milestone.__mro__:
        if "milestone" in klass.__dict__:
            descriptor = klass.__dict__["milestone"]
            break
    assert isinstance(descriptor, property)



def test_etj_maxstart_is_not_abstract():
    assert not inspect.isabstract(eTJ_MaxStart)


def test_etj_maxstart_constructor_exists():
    assert callable(eTJ_MaxStart.__init__)


def test_etj_maxstart_constructor_args():
    sig = inspect.signature(eTJ_MaxStart.__init__)
    params = list(sig.parameters.keys())



def test_etj_maxend_is_not_abstract():
    assert not inspect.isabstract(eTJ_MaxEnd)


def test_etj_maxend_constructor_exists():
    assert callable(eTJ_MaxEnd.__init__)


def test_etj_maxend_constructor_args():
    sig = inspect.signature(eTJ_MaxEnd.__init__)
    params = list(sig.parameters.keys())



def test_etj_mandatory_is_not_abstract():
    assert not inspect.isabstract(eTJ_Mandatory)


def test_etj_mandatory_constructor_exists():
    assert callable(eTJ_Mandatory.__init__)


def test_etj_mandatory_constructor_args():
    sig = inspect.signature(eTJ_Mandatory.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_etj_mandatory_has_mandatory():
    assert hasattr(eTJ_Mandatory, "mandatory")
    descriptor = None
    for klass in eTJ_Mandatory.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_etj_managers_is_not_abstract():
    assert not inspect.isabstract(eTJ_Managers)


def test_etj_managers_constructor_exists():
    assert callable(eTJ_Managers.__init__)


def test_etj_managers_constructor_args():
    sig = inspect.signature(eTJ_Managers.__init__)
    params = list(sig.parameters.keys())



def test_etj_journalattributes_is_not_abstract():
    assert not inspect.isabstract(eTJ_JournalAttributes)


def test_etj_journalattributes_constructor_exists():
    assert callable(eTJ_JournalAttributes.__init__)


def test_etj_journalattributes_constructor_args():
    sig = inspect.signature(eTJ_JournalAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "args" in params, "Missing parameter 'args'"

def test_etj_journalattributes_has_args():
    assert hasattr(eTJ_JournalAttributes, "args")
    descriptor = None
    for klass in eTJ_JournalAttributes.__mro__:
        if "args" in klass.__dict__:
            descriptor = klass.__dict__["args"]
            break
    assert isinstance(descriptor, property)



def test_etj_length_is_not_abstract():
    assert not inspect.isabstract(eTJ_Length)


def test_etj_length_constructor_exists():
    assert callable(eTJ_Length.__init__)


def test_etj_length_constructor_args():
    sig = inspect.signature(eTJ_Length.__init__)
    params = list(sig.parameters.keys())



def test_etj_left_is_not_abstract():
    assert not inspect.isabstract(eTJ_Left)


def test_etj_left_constructor_exists():
    assert callable(eTJ_Left.__init__)


def test_etj_left_constructor_args():
    sig = inspect.signature(eTJ_Left.__init__)
    params = list(sig.parameters.keys())



def test_etj_journalmode_is_not_abstract():
    assert not inspect.isabstract(eTJ_JournalMode)


def test_etj_journalmode_constructor_exists():
    assert callable(eTJ_JournalMode.__init__)


def test_etj_journalmode_constructor_args():
    sig = inspect.signature(eTJ_JournalMode.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_etj_journalmode_has_mode():
    assert hasattr(eTJ_JournalMode, "mode")
    descriptor = None
    for klass in eTJ_JournalMode.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_navigatorattribute_is_not_abstract():
    assert not inspect.isabstract(NavigatorAttribute)


def test_navigatorattribute_constructor_exists():
    assert callable(NavigatorAttribute.__init__)


def test_navigatorattribute_constructor_args():
    sig = inspect.signature(NavigatorAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_hidereport_is_not_abstract():
    assert not inspect.isabstract(eTJ_HideReport)


def test_etj_hidereport_constructor_exists():
    assert callable(eTJ_HideReport.__init__)


def test_etj_hidereport_constructor_args():
    sig = inspect.signature(eTJ_HideReport.__init__)
    params = list(sig.parameters.keys())



def test_etj_interval1_is_not_abstract():
    assert not inspect.isabstract(eTJ_Interval1)


def test_etj_interval1_constructor_exists():
    assert callable(eTJ_Interval1.__init__)


def test_etj_interval1_constructor_args():
    sig = inspect.signature(eTJ_Interval1.__init__)
    params = list(sig.parameters.keys())



def test_etj_includepropertiesattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_IncludePropertiesAttribute)


def test_etj_includepropertiesattribute_constructor_exists():
    assert callable(eTJ_IncludePropertiesAttribute.__init__)


def test_etj_includepropertiesattribute_constructor_args():
    sig = inspect.signature(eTJ_IncludePropertiesAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_includeproperties_is_not_abstract():
    assert not inspect.isabstract(eTJ_IncludeProperties)


def test_etj_includeproperties_constructor_exists():
    assert callable(eTJ_IncludeProperties.__init__)


def test_etj_includeproperties_constructor_args():
    sig = inspect.signature(eTJ_IncludeProperties.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_etj_includeproperties_has_importURI():
    assert hasattr(eTJ_IncludeProperties, "importURI")
    descriptor = None
    for klass in eTJ_IncludeProperties.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_etj_footer_is_not_abstract():
    assert not inspect.isabstract(eTJ_Footer)


def test_etj_footer_constructor_exists():
    assert callable(eTJ_Footer.__init__)


def test_etj_footer_constructor_args():
    sig = inspect.signature(eTJ_Footer.__init__)
    params = list(sig.parameters.keys())



def test_etj_fail_is_not_abstract():
    assert not inspect.isabstract(eTJ_Fail)


def test_etj_fail_constructor_exists():
    assert callable(eTJ_Fail.__init__)


def test_etj_fail_constructor_args():
    sig = inspect.signature(eTJ_Fail.__init__)
    params = list(sig.parameters.keys())



def test_etj_extendedtaskattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_ExtendedTaskAttribute)


def test_etj_extendedtaskattribute_constructor_exists():
    assert callable(eTJ_ExtendedTaskAttribute.__init__)


def test_etj_extendedtaskattribute_constructor_args():
    sig = inspect.signature(eTJ_ExtendedTaskAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_etj_extendedtaskattribute_has_value():
    assert hasattr(eTJ_ExtendedTaskAttribute, "value")
    descriptor = None
    for klass in eTJ_ExtendedTaskAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj_hideaccount_is_not_abstract():
    assert not inspect.isabstract(eTJ_HideAccount)


def test_etj_hideaccount_constructor_exists():
    assert callable(eTJ_HideAccount.__init__)


def test_etj_hideaccount_constructor_args():
    sig = inspect.signature(eTJ_HideAccount.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_etj_hideaccount_has_expression():
    assert hasattr(eTJ_HideAccount, "expression")
    descriptor = None
    for klass in eTJ_HideAccount.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_etj_header_is_not_abstract():
    assert not inspect.isabstract(eTJ_Header)


def test_etj_header_constructor_exists():
    assert callable(eTJ_Header.__init__)


def test_etj_header_constructor_args():
    sig = inspect.signature(eTJ_Header.__init__)
    params = list(sig.parameters.keys())



def test_etj_gaplength_is_not_abstract():
    assert not inspect.isabstract(eTJ_GapLength)


def test_etj_gaplength_constructor_exists():
    assert callable(eTJ_GapLength.__init__)


def test_etj_gaplength_constructor_args():
    sig = inspect.signature(eTJ_GapLength.__init__)
    params = list(sig.parameters.keys())



def test_etj_gapduration_is_not_abstract():
    assert not inspect.isabstract(eTJ_GapDuration)


def test_etj_gapduration_constructor_exists():
    assert callable(eTJ_GapDuration.__init__)


def test_etj_gapduration_constructor_args():
    sig = inspect.signature(eTJ_GapDuration.__init__)
    params = list(sig.parameters.keys())



def test_etj_function_is_not_abstract():
    assert not inspect.isabstract(eTJ_Function)


def test_etj_function_constructor_exists():
    assert callable(eTJ_Function.__init__)


def test_etj_function_constructor_args():
    sig = inspect.signature(eTJ_Function.__init__)
    params = list(sig.parameters.keys())
    assert "parentId" in params, "Missing parameter 'parentId'"
    assert "distance" in params, "Missing parameter 'distance'"
    assert "level" in params, "Missing parameter 'level'"

def test_etj_function_has_parentId():
    assert hasattr(eTJ_Function, "parentId")
    descriptor = None
    for klass in eTJ_Function.__mro__:
        if "parentId" in klass.__dict__:
            descriptor = klass.__dict__["parentId"]
            break
    assert isinstance(descriptor, property)

def test_etj_function_has_distance():
    assert hasattr(eTJ_Function, "distance")
    descriptor = None
    for klass in eTJ_Function.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_etj_function_has_level():
    assert hasattr(eTJ_Function, "level")
    descriptor = None
    for klass in eTJ_Function.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_newtaskattribute_is_not_abstract():
    assert not inspect.isabstract(NewTaskAttribute)


def test_newtaskattribute_constructor_exists():
    assert callable(NewTaskAttribute.__init__)


def test_newtaskattribute_constructor_args():
    sig = inspect.signature(NewTaskAttribute.__init__)
    params = list(sig.parameters.keys())



def test_icalreportattribute_is_not_abstract():
    assert not inspect.isabstract(IcalReportAttribute)


def test_icalreportattribute_constructor_exists():
    assert callable(IcalReportAttribute.__init__)


def test_icalreportattribute_constructor_args():
    sig = inspect.signature(IcalReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_hidejournalentry_is_not_abstract():
    assert not inspect.isabstract(eTJ_HideJournalEntry)


def test_etj_hidejournalentry_constructor_exists():
    assert callable(eTJ_HideJournalEntry.__init__)


def test_etj_hidejournalentry_constructor_args():
    sig = inspect.signature(eTJ_HideJournalEntry.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_etj_hidejournalentry_has_expression():
    assert hasattr(eTJ_HideJournalEntry, "expression")
    descriptor = None
    for klass in eTJ_HideJournalEntry.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_etj_scenarioical_is_not_abstract():
    assert not inspect.isabstract(eTJ_ScenarioIcal)


def test_etj_scenarioical_constructor_exists():
    assert callable(eTJ_ScenarioIcal.__init__)


def test_etj_scenarioical_constructor_args():
    sig = inspect.signature(eTJ_ScenarioIcal.__init__)
    params = list(sig.parameters.keys())



def test_etj_email_is_not_abstract():
    assert not inspect.isabstract(eTJ_Email)


def test_etj_email_constructor_exists():
    assert callable(eTJ_Email.__init__)


def test_etj_email_constructor_args():
    sig = inspect.signature(eTJ_Email.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_etj_email_has_address():
    assert hasattr(eTJ_Email, "address")
    descriptor = None
    for klass in eTJ_Email.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_etj_effort_is_not_abstract():
    assert not inspect.isabstract(eTJ_Effort)


def test_etj_effort_constructor_exists():
    assert callable(eTJ_Effort.__init__)


def test_etj_effort_constructor_args():
    sig = inspect.signature(eTJ_Effort.__init__)
    params = list(sig.parameters.keys())



def test_etj_efficiency_is_not_abstract():
    assert not inspect.isabstract(eTJ_Efficiency)


def test_etj_efficiency_constructor_exists():
    assert callable(eTJ_Efficiency.__init__)


def test_etj_efficiency_constructor_args():
    sig = inspect.signature(eTJ_Efficiency.__init__)
    params = list(sig.parameters.keys())
    assert "efficiency" in params, "Missing parameter 'efficiency'"

def test_etj_efficiency_has_efficiency():
    assert hasattr(eTJ_Efficiency, "efficiency")
    descriptor = None
    for klass in eTJ_Efficiency.__mro__:
        if "efficiency" in klass.__dict__:
            descriptor = klass.__dict__["efficiency"]
            break
    assert isinstance(descriptor, property)



def test_etj_durationquantity_is_not_abstract():
    assert not inspect.isabstract(eTJ_DurationQuantity)


def test_etj_durationquantity_constructor_exists():
    assert callable(eTJ_DurationQuantity.__init__)


def test_etj_durationquantity_constructor_args():
    sig = inspect.signature(eTJ_DurationQuantity.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "value" in params, "Missing parameter 'value'"

def test_etj_durationquantity_has_unit():
    assert hasattr(eTJ_DurationQuantity, "unit")
    descriptor = None
    for klass in eTJ_DurationQuantity.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_etj_durationquantity_has_value():
    assert hasattr(eTJ_DurationQuantity, "value")
    descriptor = None
    for klass in eTJ_DurationQuantity.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj_duration_is_not_abstract():
    assert not inspect.isabstract(eTJ_Duration)


def test_etj_duration_constructor_exists():
    assert callable(eTJ_Duration.__init__)


def test_etj_duration_constructor_args():
    sig = inspect.signature(eTJ_Duration.__init__)
    params = list(sig.parameters.keys())



def test_statustimesheetattribute_is_not_abstract():
    assert not inspect.isabstract(StatusTimesheetAttribute)


def test_statustimesheetattribute_constructor_exists():
    assert callable(StatusTimesheetAttribute.__init__)


def test_statustimesheetattribute_constructor_args():
    sig = inspect.signature(StatusTimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_taskdependency_is_not_abstract():
    assert not inspect.isabstract(eTJ_TaskDependency)


def test_etj_taskdependency_constructor_exists():
    assert callable(eTJ_TaskDependency.__init__)


def test_etj_taskdependency_constructor_args():
    sig = inspect.signature(eTJ_TaskDependency.__init__)
    params = list(sig.parameters.keys())
    assert "policy" in params, "Missing parameter 'policy'"

def test_etj_taskdependency_has_policy():
    assert hasattr(eTJ_TaskDependency, "policy")
    descriptor = None
    for klass in eTJ_TaskDependency.__mro__:
        if "policy" in klass.__dict__:
            descriptor = klass.__dict__["policy"]
            break
    assert isinstance(descriptor, property)



def test_etj_depends_is_not_abstract():
    assert not inspect.isabstract(eTJ_Depends)


def test_etj_depends_constructor_exists():
    assert callable(eTJ_Depends.__init__)


def test_etj_depends_constructor_args():
    sig = inspect.signature(eTJ_Depends.__init__)
    params = list(sig.parameters.keys())



def test_etj_extendedresourceattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_ExtendedResourceAttribute)


def test_etj_extendedresourceattribute_constructor_exists():
    assert callable(eTJ_ExtendedResourceAttribute.__init__)


def test_etj_extendedresourceattribute_constructor_args():
    sig = inspect.signature(eTJ_ExtendedResourceAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_etj_extendedresourceattribute_has_value():
    assert hasattr(eTJ_ExtendedResourceAttribute, "value")
    descriptor = None
    for klass in eTJ_ExtendedResourceAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj_extend_is_not_abstract():
    assert not inspect.isabstract(eTJ_Extend)


def test_etj_extend_constructor_exists():
    assert callable(eTJ_Extend.__init__)


def test_etj_extend_constructor_args():
    sig = inspect.signature(eTJ_Extend.__init__)
    params = list(sig.parameters.keys())
    assert "inherit" in params, "Missing parameter 'inherit'"
    assert "description" in params, "Missing parameter 'description'"
    assert "scenariospecific" in params, "Missing parameter 'scenariospecific'"
    assert "name" in params, "Missing parameter 'name'"

def test_etj_extend_has_inherit():
    assert hasattr(eTJ_Extend, "inherit")
    descriptor = None
    for klass in eTJ_Extend.__mro__:
        if "inherit" in klass.__dict__:
            descriptor = klass.__dict__["inherit"]
            break
    assert isinstance(descriptor, property)

def test_etj_extend_has_description():
    assert hasattr(eTJ_Extend, "description")
    descriptor = None
    for klass in eTJ_Extend.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_etj_extend_has_scenariospecific():
    assert hasattr(eTJ_Extend, "scenariospecific")
    descriptor = None
    for klass in eTJ_Extend.__mro__:
        if "scenariospecific" in klass.__dict__:
            descriptor = klass.__dict__["scenariospecific"]
            break
    assert isinstance(descriptor, property)

def test_etj_extend_has_name():
    assert hasattr(eTJ_Extend, "name")
    descriptor = None
    for klass in eTJ_Extend.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_etj_epilog_is_not_abstract():
    assert not inspect.isabstract(eTJ_Epilog)


def test_etj_epilog_constructor_exists():
    assert callable(eTJ_Epilog.__init__)


def test_etj_epilog_constructor_args():
    sig = inspect.signature(eTJ_Epilog.__init__)
    params = list(sig.parameters.keys())



def test_etj_endcredit_is_not_abstract():
    assert not inspect.isabstract(eTJ_EndCredit)


def test_etj_endcredit_constructor_exists():
    assert callable(eTJ_EndCredit.__init__)


def test_etj_endcredit_constructor_args():
    sig = inspect.signature(eTJ_EndCredit.__init__)
    params = list(sig.parameters.keys())
    assert "credit" in params, "Missing parameter 'credit'"

def test_etj_endcredit_has_credit():
    assert hasattr(eTJ_EndCredit, "credit")
    descriptor = None
    for klass in eTJ_EndCredit.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
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



def test_etj_remaining_is_not_abstract():
    assert not inspect.isabstract(eTJ_Remaining)


def test_etj_remaining_constructor_exists():
    assert callable(eTJ_Remaining.__init__)


def test_etj_remaining_constructor_args():
    sig = inspect.signature(eTJ_Remaining.__init__)
    params = list(sig.parameters.keys())



def test_etj_statustimesheet_is_not_abstract():
    assert not inspect.isabstract(eTJ_StatusTimesheet)


def test_etj_statustimesheet_constructor_exists():
    assert callable(eTJ_StatusTimesheet.__init__)


def test_etj_statustimesheet_constructor_args():
    sig = inspect.signature(eTJ_StatusTimesheet.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "text" in params, "Missing parameter 'text'"

def test_etj_statustimesheet_has_level():
    assert hasattr(eTJ_StatusTimesheet, "level")
    descriptor = None
    for klass in eTJ_StatusTimesheet.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_etj_statustimesheet_has_text():
    assert hasattr(eTJ_StatusTimesheet, "text")
    descriptor = None
    for klass in eTJ_StatusTimesheet.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_etj_priority_is_not_abstract():
    assert not inspect.isabstract(eTJ_Priority)


def test_etj_priority_constructor_exists():
    assert callable(eTJ_Priority.__init__)


def test_etj_priority_constructor_args():
    sig = inspect.signature(eTJ_Priority.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_etj_priority_has_priority():
    assert hasattr(eTJ_Priority, "priority")
    descriptor = None
    for klass in eTJ_Priority.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_etj_work_is_not_abstract():
    assert not inspect.isabstract(eTJ_Work)


def test_etj_work_constructor_exists():
    assert callable(eTJ_Work.__init__)


def test_etj_work_constructor_args():
    sig = inspect.signature(eTJ_Work.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "value" in params, "Missing parameter 'value'"

def test_etj_work_has_unit():
    assert hasattr(eTJ_Work, "unit")
    descriptor = None
    for klass in eTJ_Work.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_etj_work_has_value():
    assert hasattr(eTJ_Work, "value")
    descriptor = None
    for klass in eTJ_Work.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statussheetreportattribute_is_not_abstract():
    assert not inspect.isabstract(StatusSheetReportAttribute)


def test_statussheetreportattribute_constructor_exists():
    assert callable(StatusSheetReportAttribute.__init__)


def test_statussheetreportattribute_constructor_args():
    sig = inspect.signature(StatusSheetReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_sorttasks_is_not_abstract():
    assert not inspect.isabstract(eTJ_SortTasks)


def test_etj_sorttasks_constructor_exists():
    assert callable(eTJ_SortTasks.__init__)


def test_etj_sorttasks_constructor_args():
    sig = inspect.signature(eTJ_SortTasks.__init__)
    params = list(sig.parameters.keys())



def test_etj_sortresources_is_not_abstract():
    assert not inspect.isabstract(eTJ_SortResources)


def test_etj_sortresources_constructor_exists():
    assert callable(eTJ_SortResources.__init__)


def test_etj_sortresources_constructor_args():
    sig = inspect.signature(eTJ_SortResources.__init__)
    params = list(sig.parameters.keys())



def test_nikureportattribute_is_not_abstract():
    assert not inspect.isabstract(NikuReportAttribute)


def test_nikureportattribute_constructor_exists():
    assert callable(NikuReportAttribute.__init__)


def test_nikureportattribute_constructor_args():
    sig = inspect.signature(NikuReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_formats_is_not_abstract():
    assert not inspect.isabstract(eTJ_Formats)


def test_etj_formats_constructor_exists():
    assert callable(eTJ_Formats.__init__)


def test_etj_formats_constructor_args():
    sig = inspect.signature(eTJ_Formats.__init__)
    params = list(sig.parameters.keys())
    assert "formats" in params, "Missing parameter 'formats'"

def test_etj_formats_has_formats():
    assert hasattr(eTJ_Formats, "formats")
    descriptor = None
    for klass in eTJ_Formats.__mro__:
        if "formats" in klass.__dict__:
            descriptor = klass.__dict__["formats"]
            break
    assert isinstance(descriptor, property)



def test_etj_headline_is_not_abstract():
    assert not inspect.isabstract(eTJ_Headline)


def test_etj_headline_constructor_exists():
    assert callable(eTJ_Headline.__init__)


def test_etj_headline_constructor_args():
    sig = inspect.signature(eTJ_Headline.__init__)
    params = list(sig.parameters.keys())



def test_etj_timeoff_is_not_abstract():
    assert not inspect.isabstract(eTJ_Timeoff)


def test_etj_timeoff_constructor_exists():
    assert callable(eTJ_Timeoff.__init__)


def test_etj_timeoff_constructor_args():
    sig = inspect.signature(eTJ_Timeoff.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_etj_timeoff_has_name():
    assert hasattr(eTJ_Timeoff, "name")
    descriptor = None
    for klass in eTJ_Timeoff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_etj_timeoff_has_id():
    assert hasattr(eTJ_Timeoff, "id")
    descriptor = None
    for klass in eTJ_Timeoff.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_etj_accountshare_is_not_abstract():
    assert not inspect.isabstract(eTJ_AccountShare)


def test_etj_accountshare_constructor_exists():
    assert callable(eTJ_AccountShare.__init__)


def test_etj_accountshare_constructor_args():
    sig = inspect.signature(eTJ_AccountShare.__init__)
    params = list(sig.parameters.keys())
    assert "share" in params, "Missing parameter 'share'"

def test_etj_accountshare_has_share():
    assert hasattr(eTJ_AccountShare, "share")
    descriptor = None
    for klass in eTJ_AccountShare.__mro__:
        if "share" in klass.__dict__:
            descriptor = klass.__dict__["share"]
            break
    assert isinstance(descriptor, property)



def test_etj_chargeset_is_not_abstract():
    assert not inspect.isabstract(eTJ_ChargeSet)


def test_etj_chargeset_constructor_exists():
    assert callable(eTJ_ChargeSet.__init__)


def test_etj_chargeset_constructor_args():
    sig = inspect.signature(eTJ_ChargeSet.__init__)
    params = list(sig.parameters.keys())



def test_etj_charge_is_not_abstract():
    assert not inspect.isabstract(eTJ_Charge)


def test_etj_charge_constructor_exists():
    assert callable(eTJ_Charge.__init__)


def test_etj_charge_constructor_args():
    sig = inspect.signature(eTJ_Charge.__init__)
    params = list(sig.parameters.keys())
    assert "applies" in params, "Missing parameter 'applies'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_etj_charge_has_applies():
    assert hasattr(eTJ_Charge, "applies")
    descriptor = None
    for klass in eTJ_Charge.__mro__:
        if "applies" in klass.__dict__:
            descriptor = klass.__dict__["applies"]
            break
    assert isinstance(descriptor, property)

def test_etj_charge_has_amount():
    assert hasattr(eTJ_Charge, "amount")
    descriptor = None
    for klass in eTJ_Charge.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_etj_center_is_not_abstract():
    assert not inspect.isabstract(eTJ_Center)


def test_etj_center_constructor_exists():
    assert callable(eTJ_Center.__init__)


def test_etj_center_constructor_args():
    sig = inspect.signature(eTJ_Center.__init__)
    params = list(sig.parameters.keys())



def test_etj_rgb_is_not_abstract():
    assert not inspect.isabstract(eTJ_RGB)


def test_etj_rgb_constructor_exists():
    assert callable(eTJ_RGB.__init__)


def test_etj_rgb_constructor_args():
    sig = inspect.signature(eTJ_RGB.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_etj_rgb_has_value():
    assert hasattr(eTJ_RGB, "value")
    descriptor = None
    for klass in eTJ_RGB.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(eTJ_LogicalExpression)


def test_etj_logicalexpression_constructor_exists():
    assert callable(eTJ_LogicalExpression.__init__)


def test_etj_logicalexpression_constructor_args():
    sig = inspect.signature(eTJ_LogicalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_etj_logicalexpression_has_op():
    assert hasattr(eTJ_LogicalExpression, "op")
    descriptor = None
    for klass in eTJ_LogicalExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_columnattribute_is_not_abstract():
    assert not inspect.isabstract(ColumnAttribute)


def test_columnattribute_constructor_exists():
    assert callable(ColumnAttribute.__init__)


def test_columnattribute_constructor_args():
    sig = inspect.signature(ColumnAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_fontcolor_is_not_abstract():
    assert not inspect.isabstract(eTJ_FontColor)


def test_etj_fontcolor_constructor_exists():
    assert callable(eTJ_FontColor.__init__)


def test_etj_fontcolor_constructor_args():
    sig = inspect.signature(eTJ_FontColor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_etj_fontcolor_has_color():
    assert hasattr(eTJ_FontColor, "color")
    descriptor = None
    for klass in eTJ_FontColor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_etj_celltext_is_not_abstract():
    assert not inspect.isabstract(eTJ_CellText)


def test_etj_celltext_constructor_exists():
    assert callable(eTJ_CellText.__init__)


def test_etj_celltext_constructor_args():
    sig = inspect.signature(eTJ_CellText.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_etj_celltext_has_text():
    assert hasattr(eTJ_CellText, "text")
    descriptor = None
    for klass in eTJ_CellText.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_etj_halign_is_not_abstract():
    assert not inspect.isabstract(eTJ_HAlign)


def test_etj_halign_constructor_exists():
    assert callable(eTJ_HAlign.__init__)


def test_etj_halign_constructor_args():
    sig = inspect.signature(eTJ_HAlign.__init__)
    params = list(sig.parameters.keys())
    assert "justification" in params, "Missing parameter 'justification'"

def test_etj_halign_has_justification():
    assert hasattr(eTJ_HAlign, "justification")
    descriptor = None
    for klass in eTJ_HAlign.__mro__:
        if "justification" in klass.__dict__:
            descriptor = klass.__dict__["justification"]
            break
    assert isinstance(descriptor, property)



def test_etj_scale_is_not_abstract():
    assert not inspect.isabstract(eTJ_Scale)


def test_etj_scale_constructor_exists():
    assert callable(eTJ_Scale.__init__)


def test_etj_scale_constructor_args():
    sig = inspect.signature(eTJ_Scale.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"

def test_etj_scale_has_scale():
    assert hasattr(eTJ_Scale, "scale")
    descriptor = None
    for klass in eTJ_Scale.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_etj_title_is_not_abstract():
    assert not inspect.isabstract(eTJ_Title)


def test_etj_title_constructor_exists():
    assert callable(eTJ_Title.__init__)


def test_etj_title_constructor_args():
    sig = inspect.signature(eTJ_Title.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_etj_title_has_title():
    assert hasattr(eTJ_Title, "title")
    descriptor = None
    for klass in eTJ_Title.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_etj_extendedresourceattributecolumn_is_not_abstract():
    assert not inspect.isabstract(eTJ_ExtendedResourceAttributeColumn)


def test_etj_extendedresourceattributecolumn_constructor_exists():
    assert callable(eTJ_ExtendedResourceAttributeColumn.__init__)


def test_etj_extendedresourceattributecolumn_constructor_args():
    sig = inspect.signature(eTJ_ExtendedResourceAttributeColumn.__init__)
    params = list(sig.parameters.keys())



def test_etj_listtype_is_not_abstract():
    assert not inspect.isabstract(eTJ_ListType)


def test_etj_listtype_constructor_exists():
    assert callable(eTJ_ListType.__init__)


def test_etj_listtype_constructor_args():
    sig = inspect.signature(eTJ_ListType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_etj_listtype_has_type():
    assert hasattr(eTJ_ListType, "type")
    descriptor = None
    for klass in eTJ_ListType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_etj_tooltip_is_not_abstract():
    assert not inspect.isabstract(eTJ_ToolTip)


def test_etj_tooltip_constructor_exists():
    assert callable(eTJ_ToolTip.__init__)


def test_etj_tooltip_constructor_args():
    sig = inspect.signature(eTJ_ToolTip.__init__)
    params = list(sig.parameters.keys())
    assert "tip" in params, "Missing parameter 'tip'"

def test_etj_tooltip_has_tip():
    assert hasattr(eTJ_ToolTip, "tip")
    descriptor = None
    for klass in eTJ_ToolTip.__mro__:
        if "tip" in klass.__dict__:
            descriptor = klass.__dict__["tip"]
            break
    assert isinstance(descriptor, property)



def test_etj_listitem_is_not_abstract():
    assert not inspect.isabstract(eTJ_ListItem)


def test_etj_listitem_constructor_exists():
    assert callable(eTJ_ListItem.__init__)


def test_etj_listitem_constructor_args():
    sig = inspect.signature(eTJ_ListItem.__init__)
    params = list(sig.parameters.keys())



def test_etj_width_is_not_abstract():
    assert not inspect.isabstract(eTJ_Width)


def test_etj_width_constructor_exists():
    assert callable(eTJ_Width.__init__)


def test_etj_width_constructor_args():
    sig = inspect.signature(eTJ_Width.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"

def test_etj_width_has_width():
    assert hasattr(eTJ_Width, "width")
    descriptor = None
    for klass in eTJ_Width.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_etj_cellcolor_is_not_abstract():
    assert not inspect.isabstract(eTJ_CellColor)


def test_etj_cellcolor_constructor_exists():
    assert callable(eTJ_CellColor.__init__)


def test_etj_cellcolor_constructor_args():
    sig = inspect.signature(eTJ_CellColor.__init__)
    params = list(sig.parameters.keys())



def test_etj_caption_is_not_abstract():
    assert not inspect.isabstract(eTJ_Caption)


def test_etj_caption_constructor_exists():
    assert callable(eTJ_Caption.__init__)


def test_etj_caption_constructor_args():
    sig = inspect.signature(eTJ_Caption.__init__)
    params = list(sig.parameters.keys())



def test_exportattribute_is_not_abstract():
    assert not inspect.isabstract(ExportAttribute)


def test_exportattribute_constructor_exists():
    assert callable(ExportAttribute.__init__)


def test_exportattribute_constructor_args():
    sig = inspect.signature(ExportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_resourceattributes_is_not_abstract():
    assert not inspect.isabstract(eTJ_ResourceAttributes)


def test_etj_resourceattributes_constructor_exists():
    assert callable(eTJ_ResourceAttributes.__init__)


def test_etj_resourceattributes_constructor_args():
    sig = inspect.signature(eTJ_ResourceAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "none" in params, "Missing parameter 'none'"
    assert "vacation" in params, "Missing parameter 'vacation'"
    assert "workingHours" in params, "Missing parameter 'workingHours'"
    assert "all" in params, "Missing parameter 'all'"
    assert "booking" in params, "Missing parameter 'booking'"

def test_etj_resourceattributes_has_none():
    assert hasattr(eTJ_ResourceAttributes, "none")
    descriptor = None
    for klass in eTJ_ResourceAttributes.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_etj_resourceattributes_has_vacation():
    assert hasattr(eTJ_ResourceAttributes, "vacation")
    descriptor = None
    for klass in eTJ_ResourceAttributes.__mro__:
        if "vacation" in klass.__dict__:
            descriptor = klass.__dict__["vacation"]
            break
    assert isinstance(descriptor, property)

def test_etj_resourceattributes_has_workingHours():
    assert hasattr(eTJ_ResourceAttributes, "workingHours")
    descriptor = None
    for klass in eTJ_ResourceAttributes.__mro__:
        if "workingHours" in klass.__dict__:
            descriptor = klass.__dict__["workingHours"]
            break
    assert isinstance(descriptor, property)

def test_etj_resourceattributes_has_all():
    assert hasattr(eTJ_ResourceAttributes, "all")
    descriptor = None
    for klass in eTJ_ResourceAttributes.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_etj_resourceattributes_has_booking():
    assert hasattr(eTJ_ResourceAttributes, "booking")
    descriptor = None
    for klass in eTJ_ResourceAttributes.__mro__:
        if "booking" in klass.__dict__:
            descriptor = klass.__dict__["booking"]
            break
    assert isinstance(descriptor, property)



def test_etj_hidetask_is_not_abstract():
    assert not inspect.isabstract(eTJ_HideTask)


def test_etj_hidetask_constructor_exists():
    assert callable(eTJ_HideTask.__init__)


def test_etj_hidetask_constructor_args():
    sig = inspect.signature(eTJ_HideTask.__init__)
    params = list(sig.parameters.keys())



def test_etj_hideresource_is_not_abstract():
    assert not inspect.isabstract(eTJ_HideResource)


def test_etj_hideresource_constructor_exists():
    assert callable(eTJ_HideResource.__init__)


def test_etj_hideresource_constructor_args():
    sig = inspect.signature(eTJ_HideResource.__init__)
    params = list(sig.parameters.keys())



def test_etj_end_is_not_abstract():
    assert not inspect.isabstract(eTJ_End)


def test_etj_end_constructor_exists():
    assert callable(eTJ_End.__init__)


def test_etj_end_constructor_args():
    sig = inspect.signature(eTJ_End.__init__)
    params = list(sig.parameters.keys())



def test_etj_scenarios_is_not_abstract():
    assert not inspect.isabstract(eTJ_Scenarios)


def test_etj_scenarios_constructor_exists():
    assert callable(eTJ_Scenarios.__init__)


def test_etj_scenarios_constructor_args():
    sig = inspect.signature(eTJ_Scenarios.__init__)
    params = list(sig.parameters.keys())



def test_etj_taskattributes_is_not_abstract():
    assert not inspect.isabstract(eTJ_TaskAttributes)


def test_etj_taskattributes_constructor_exists():
    assert callable(eTJ_TaskAttributes.__init__)


def test_etj_taskattributes_constructor_args():
    sig = inspect.signature(eTJ_TaskAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "flags" in params, "Missing parameter 'flags'"
    assert "maxstart" in params, "Missing parameter 'maxstart'"
    assert "none" in params, "Missing parameter 'none'"
    assert "note" in params, "Missing parameter 'note'"
    assert "all" in params, "Missing parameter 'all'"
    assert "responsible" in params, "Missing parameter 'responsible'"
    assert "maxend" in params, "Missing parameter 'maxend'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "minstart" in params, "Missing parameter 'minstart'"
    assert "booking" in params, "Missing parameter 'booking'"
    assert "complete" in params, "Missing parameter 'complete'"
    assert "depends" in params, "Missing parameter 'depends'"
    assert "minend" in params, "Missing parameter 'minend'"

def test_etj_taskattributes_has_flags():
    assert hasattr(eTJ_TaskAttributes, "flags")
    descriptor = None
    for klass in eTJ_TaskAttributes.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)

def test_etj_taskattributes_has_maxstart():
    assert hasattr(eTJ_TaskAttributes, "maxstart")
    descriptor = None
    for klass in eTJ_TaskAttributes.__mro__:
        if "maxstart" in klass.__dict__:
            descriptor = klass.__dict__["maxstart"]
            break
    assert isinstance(descriptor, property)

def test_etj_taskattributes_has_none():
    assert hasattr(eTJ_TaskAttributes, "none")
    descriptor = None
    for klass in eTJ_TaskAttributes.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_etj_taskattributes_has_note():
    assert hasattr(eTJ_TaskAttributes, "note")
    descriptor = None
    for klass in eTJ_TaskAttributes.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_etj_taskattributes_has_all():
    assert hasattr(eTJ_TaskAttributes, "all")
    descriptor = None
    for klass in eTJ_TaskAttributes.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_etj_taskattributes_has_responsible():
    assert hasattr(eTJ_TaskAttributes, "responsible")
    descriptor = None
    for klass in eTJ_TaskAttributes.__mro__:
        if "responsible" in klass.__dict__:
            descriptor = klass.__dict__["responsible"]
            break
    assert isinstance(descriptor, property)

def test_etj_taskattributes_has_maxend():
    assert hasattr(eTJ_TaskAttributes, "maxend")
    descriptor = None
    for klass in eTJ_TaskAttributes.__mro__:
        if "maxend" in klass.__dict__:
            descriptor = klass.__dict__["maxend"]
            break
    assert isinstance(descriptor, property)

def test_etj_taskattributes_has_priority():
    assert hasattr(eTJ_TaskAttributes, "priority")
    descriptor = None
    for klass in eTJ_TaskAttributes.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_etj_taskattributes_has_minstart():
    assert hasattr(eTJ_TaskAttributes, "minstart")
    descriptor = None
    for klass in eTJ_TaskAttributes.__mro__:
        if "minstart" in klass.__dict__:
            descriptor = klass.__dict__["minstart"]
            break
    assert isinstance(descriptor, property)

def test_etj_taskattributes_has_booking():
    assert hasattr(eTJ_TaskAttributes, "booking")
    descriptor = None
    for klass in eTJ_TaskAttributes.__mro__:
        if "booking" in klass.__dict__:
            descriptor = klass.__dict__["booking"]
            break
    assert isinstance(descriptor, property)

def test_etj_taskattributes_has_complete():
    assert hasattr(eTJ_TaskAttributes, "complete")
    descriptor = None
    for klass in eTJ_TaskAttributes.__mro__:
        if "complete" in klass.__dict__:
            descriptor = klass.__dict__["complete"]
            break
    assert isinstance(descriptor, property)

def test_etj_taskattributes_has_depends():
    assert hasattr(eTJ_TaskAttributes, "depends")
    descriptor = None
    for klass in eTJ_TaskAttributes.__mro__:
        if "depends" in klass.__dict__:
            descriptor = klass.__dict__["depends"]
            break
    assert isinstance(descriptor, property)

def test_etj_taskattributes_has_minend():
    assert hasattr(eTJ_TaskAttributes, "minend")
    descriptor = None
    for klass in eTJ_TaskAttributes.__mro__:
        if "minend" in klass.__dict__:
            descriptor = klass.__dict__["minend"]
            break
    assert isinstance(descriptor, property)



def test_etj_start_is_not_abstract():
    assert not inspect.isabstract(eTJ_Start)


def test_etj_start_constructor_exists():
    assert callable(eTJ_Start.__init__)


def test_etj_start_constructor_args():
    sig = inspect.signature(eTJ_Start.__init__)
    params = list(sig.parameters.keys())



def test_etj_period_is_not_abstract():
    assert not inspect.isabstract(eTJ_Period)


def test_etj_period_constructor_exists():
    assert callable(eTJ_Period.__init__)


def test_etj_period_constructor_args():
    sig = inspect.signature(eTJ_Period.__init__)
    params = list(sig.parameters.keys())



def test_etj_rolluptask_is_not_abstract():
    assert not inspect.isabstract(eTJ_RollupTask)


def test_etj_rolluptask_constructor_exists():
    assert callable(eTJ_RollupTask.__init__)


def test_etj_rolluptask_constructor_args():
    sig = inspect.signature(eTJ_RollupTask.__init__)
    params = list(sig.parameters.keys())



def test_etj_rollupresource_is_not_abstract():
    assert not inspect.isabstract(eTJ_RollupResource)


def test_etj_rollupresource_constructor_exists():
    assert callable(eTJ_RollupResource.__init__)


def test_etj_rollupresource_constructor_args():
    sig = inspect.signature(eTJ_RollupResource.__init__)
    params = list(sig.parameters.keys())



def test_etj_definitions_is_not_abstract():
    assert not inspect.isabstract(eTJ_Definitions)


def test_etj_definitions_constructor_exists():
    assert callable(eTJ_Definitions.__init__)


def test_etj_definitions_constructor_args():
    sig = inspect.signature(eTJ_Definitions.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"
    assert "none" in params, "Missing parameter 'none'"

def test_etj_definitions_has_all():
    assert hasattr(eTJ_Definitions, "all")
    descriptor = None
    for klass in eTJ_Definitions.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_etj_definitions_has_none():
    assert hasattr(eTJ_Definitions, "none")
    descriptor = None
    for klass in eTJ_Definitions.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)



def test_limitsattribute_is_not_abstract():
    assert not inspect.isabstract(LimitsAttribute)


def test_limitsattribute_constructor_exists():
    assert callable(LimitsAttribute.__init__)


def test_limitsattribute_constructor_args():
    sig = inspect.signature(LimitsAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_weeklymax_is_not_abstract():
    assert not inspect.isabstract(eTJ_WeeklyMax)


def test_etj_weeklymax_constructor_exists():
    assert callable(eTJ_WeeklyMax.__init__)


def test_etj_weeklymax_constructor_args():
    sig = inspect.signature(eTJ_WeeklyMax.__init__)
    params = list(sig.parameters.keys())



def test_etj_minimum_is_not_abstract():
    assert not inspect.isabstract(eTJ_Minimum)


def test_etj_minimum_constructor_exists():
    assert callable(eTJ_Minimum.__init__)


def test_etj_minimum_constructor_args():
    sig = inspect.signature(eTJ_Minimum.__init__)
    params = list(sig.parameters.keys())



def test_etj_monthlymin_is_not_abstract():
    assert not inspect.isabstract(eTJ_MonthlyMin)


def test_etj_monthlymin_constructor_exists():
    assert callable(eTJ_MonthlyMin.__init__)


def test_etj_monthlymin_constructor_args():
    sig = inspect.signature(eTJ_MonthlyMin.__init__)
    params = list(sig.parameters.keys())



def test_etj_weeklymin_is_not_abstract():
    assert not inspect.isabstract(eTJ_WeeklyMin)


def test_etj_weeklymin_constructor_exists():
    assert callable(eTJ_WeeklyMin.__init__)


def test_etj_weeklymin_constructor_args():
    sig = inspect.signature(eTJ_WeeklyMin.__init__)
    params = list(sig.parameters.keys())



def test_etj_dailymin_is_not_abstract():
    assert not inspect.isabstract(eTJ_DailyMin)


def test_etj_dailymin_constructor_exists():
    assert callable(eTJ_DailyMin.__init__)


def test_etj_dailymin_constructor_args():
    sig = inspect.signature(eTJ_DailyMin.__init__)
    params = list(sig.parameters.keys())



def test_etj_maximum_is_not_abstract():
    assert not inspect.isabstract(eTJ_Maximum)


def test_etj_maximum_constructor_exists():
    assert callable(eTJ_Maximum.__init__)


def test_etj_maximum_constructor_args():
    sig = inspect.signature(eTJ_Maximum.__init__)
    params = list(sig.parameters.keys())



def test_etj_monthlymax_is_not_abstract():
    assert not inspect.isabstract(eTJ_MonthlyMax)


def test_etj_monthlymax_constructor_exists():
    assert callable(eTJ_MonthlyMax.__init__)


def test_etj_monthlymax_constructor_args():
    sig = inspect.signature(eTJ_MonthlyMax.__init__)
    params = list(sig.parameters.keys())



def test_etj_dailymax_is_not_abstract():
    assert not inspect.isabstract(eTJ_DailyMax)


def test_etj_dailymax_constructor_exists():
    assert callable(eTJ_DailyMax.__init__)


def test_etj_dailymax_constructor_args():
    sig = inspect.signature(eTJ_DailyMax.__init__)
    params = list(sig.parameters.keys())



def test_projectattribute_is_not_abstract():
    assert not inspect.isabstract(ProjectAttribute)


def test_projectattribute_constructor_exists():
    assert callable(ProjectAttribute.__init__)


def test_projectattribute_constructor_args():
    sig = inspect.signature(ProjectAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_yearlyworkingdays_is_not_abstract():
    assert not inspect.isabstract(eTJ_YearlyWorkingDays)


def test_etj_yearlyworkingdays_constructor_exists():
    assert callable(eTJ_YearlyWorkingDays.__init__)


def test_etj_yearlyworkingdays_constructor_args():
    sig = inspect.signature(eTJ_YearlyWorkingDays.__init__)
    params = list(sig.parameters.keys())
    assert "yearlyWorkingDays" in params, "Missing parameter 'yearlyWorkingDays'"

def test_etj_yearlyworkingdays_has_yearlyWorkingDays():
    assert hasattr(eTJ_YearlyWorkingDays, "yearlyWorkingDays")
    descriptor = None
    for klass in eTJ_YearlyWorkingDays.__mro__:
        if "yearlyWorkingDays" in klass.__dict__:
            descriptor = klass.__dict__["yearlyWorkingDays"]
            break
    assert isinstance(descriptor, property)



def test_etj_extendresource_is_not_abstract():
    assert not inspect.isabstract(eTJ_ExtendResource)


def test_etj_extendresource_constructor_exists():
    assert callable(eTJ_ExtendResource.__init__)


def test_etj_extendresource_constructor_args():
    sig = inspect.signature(eTJ_ExtendResource.__init__)
    params = list(sig.parameters.keys())



def test_etj_shorttimeformat_is_not_abstract():
    assert not inspect.isabstract(eTJ_ShortTimeFormat)


def test_etj_shorttimeformat_constructor_exists():
    assert callable(eTJ_ShortTimeFormat.__init__)


def test_etj_shorttimeformat_constructor_args():
    sig = inspect.signature(eTJ_ShortTimeFormat.__init__)
    params = list(sig.parameters.keys())
    assert "shortTimeFormat" in params, "Missing parameter 'shortTimeFormat'"

def test_etj_shorttimeformat_has_shortTimeFormat():
    assert hasattr(eTJ_ShortTimeFormat, "shortTimeFormat")
    descriptor = None
    for klass in eTJ_ShortTimeFormat.__mro__:
        if "shortTimeFormat" in klass.__dict__:
            descriptor = klass.__dict__["shortTimeFormat"]
            break
    assert isinstance(descriptor, property)



def test_etj_trackingscenario_is_not_abstract():
    assert not inspect.isabstract(eTJ_TrackingScenario)


def test_etj_trackingscenario_constructor_exists():
    assert callable(eTJ_TrackingScenario.__init__)


def test_etj_trackingscenario_constructor_args():
    sig = inspect.signature(eTJ_TrackingScenario.__init__)
    params = list(sig.parameters.keys())



def test_etj_journalentry_is_not_abstract():
    assert not inspect.isabstract(eTJ_JournalEntry)


def test_etj_journalentry_constructor_exists():
    assert callable(eTJ_JournalEntry.__init__)


def test_etj_journalentry_constructor_args():
    sig = inspect.signature(eTJ_JournalEntry.__init__)
    params = list(sig.parameters.keys())
    assert "headline" in params, "Missing parameter 'headline'"

def test_etj_journalentry_has_headline():
    assert hasattr(eTJ_JournalEntry, "headline")
    descriptor = None
    for klass in eTJ_JournalEntry.__mro__:
        if "headline" in klass.__dict__:
            descriptor = klass.__dict__["headline"]
            break
    assert isinstance(descriptor, property)



def test_etj_weekstarts_is_not_abstract():
    assert not inspect.isabstract(eTJ_WeekStarts)


def test_etj_weekstarts_constructor_exists():
    assert callable(eTJ_WeekStarts.__init__)


def test_etj_weekstarts_constructor_args():
    sig = inspect.signature(eTJ_WeekStarts.__init__)
    params = list(sig.parameters.keys())
    assert "monday" in params, "Missing parameter 'monday'"
    assert "sunday" in params, "Missing parameter 'sunday'"

def test_etj_weekstarts_has_monday():
    assert hasattr(eTJ_WeekStarts, "monday")
    descriptor = None
    for klass in eTJ_WeekStarts.__mro__:
        if "monday" in klass.__dict__:
            descriptor = klass.__dict__["monday"]
            break
    assert isinstance(descriptor, property)

def test_etj_weekstarts_has_sunday():
    assert hasattr(eTJ_WeekStarts, "sunday")
    descriptor = None
    for klass in eTJ_WeekStarts.__mro__:
        if "sunday" in klass.__dict__:
            descriptor = klass.__dict__["sunday"]
            break
    assert isinstance(descriptor, property)



def test_etj_workinghours_is_not_abstract():
    assert not inspect.isabstract(eTJ_WorkingHours)


def test_etj_workinghours_constructor_exists():
    assert callable(eTJ_WorkingHours.__init__)


def test_etj_workinghours_constructor_args():
    sig = inspect.signature(eTJ_WorkingHours.__init__)
    params = list(sig.parameters.keys())
    assert "off" in params, "Missing parameter 'off'"

def test_etj_workinghours_has_off():
    assert hasattr(eTJ_WorkingHours, "off")
    descriptor = None
    for klass in eTJ_WorkingHours.__mro__:
        if "off" in klass.__dict__:
            descriptor = klass.__dict__["off"]
            break
    assert isinstance(descriptor, property)



def test_etj_now_is_not_abstract():
    assert not inspect.isabstract(eTJ_Now)


def test_etj_now_constructor_exists():
    assert callable(eTJ_Now.__init__)


def test_etj_now_constructor_args():
    sig = inspect.signature(eTJ_Now.__init__)
    params = list(sig.parameters.keys())



def test_etj_scenario_is_not_abstract():
    assert not inspect.isabstract(eTJ_Scenario)


def test_etj_scenario_constructor_exists():
    assert callable(eTJ_Scenario.__init__)


def test_etj_scenario_constructor_args():
    sig = inspect.signature(eTJ_Scenario.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "active" in params, "Missing parameter 'active'"

def test_etj_scenario_has_name():
    assert hasattr(eTJ_Scenario, "name")
    descriptor = None
    for klass in eTJ_Scenario.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_etj_scenario_has_id():
    assert hasattr(eTJ_Scenario, "id")
    descriptor = None
    for klass in eTJ_Scenario.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_etj_scenario_has_active():
    assert hasattr(eTJ_Scenario, "active")
    descriptor = None
    for klass in eTJ_Scenario.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_etj_include_is_not_abstract():
    assert not inspect.isabstract(eTJ_Include)


def test_etj_include_constructor_exists():
    assert callable(eTJ_Include.__init__)


def test_etj_include_constructor_args():
    sig = inspect.signature(eTJ_Include.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_etj_include_has_importURI():
    assert hasattr(eTJ_Include, "importURI")
    descriptor = None
    for klass in eTJ_Include.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_etj_timezone_is_not_abstract():
    assert not inspect.isabstract(eTJ_Timezone)


def test_etj_timezone_constructor_exists():
    assert callable(eTJ_Timezone.__init__)


def test_etj_timezone_constructor_args():
    sig = inspect.signature(eTJ_Timezone.__init__)
    params = list(sig.parameters.keys())
    assert "timezone" in params, "Missing parameter 'timezone'"

def test_etj_timezone_has_timezone():
    assert hasattr(eTJ_Timezone, "timezone")
    descriptor = None
    for klass in eTJ_Timezone.__mro__:
        if "timezone" in klass.__dict__:
            descriptor = klass.__dict__["timezone"]
            break
    assert isinstance(descriptor, property)



def test_etj_timeformat_is_not_abstract():
    assert not inspect.isabstract(eTJ_TimeFormat)


def test_etj_timeformat_constructor_exists():
    assert callable(eTJ_TimeFormat.__init__)


def test_etj_timeformat_constructor_args():
    sig = inspect.signature(eTJ_TimeFormat.__init__)
    params = list(sig.parameters.keys())
    assert "timeformat" in params, "Missing parameter 'timeformat'"

def test_etj_timeformat_has_timeformat():
    assert hasattr(eTJ_TimeFormat, "timeformat")
    descriptor = None
    for klass in eTJ_TimeFormat.__mro__:
        if "timeformat" in klass.__dict__:
            descriptor = klass.__dict__["timeformat"]
            break
    assert isinstance(descriptor, property)



def test_etj_numberformat_is_not_abstract():
    assert not inspect.isabstract(eTJ_NumberFormat)


def test_etj_numberformat_constructor_exists():
    assert callable(eTJ_NumberFormat.__init__)


def test_etj_numberformat_constructor_args():
    sig = inspect.signature(eTJ_NumberFormat.__init__)
    params = list(sig.parameters.keys())



def test_etj_extendtask_is_not_abstract():
    assert not inspect.isabstract(eTJ_ExtendTask)


def test_etj_extendtask_constructor_exists():
    assert callable(eTJ_ExtendTask.__init__)


def test_etj_extendtask_constructor_args():
    sig = inspect.signature(eTJ_ExtendTask.__init__)
    params = list(sig.parameters.keys())



def test_etj_currencyformat_is_not_abstract():
    assert not inspect.isabstract(eTJ_CurrencyFormat)


def test_etj_currencyformat_constructor_exists():
    assert callable(eTJ_CurrencyFormat.__init__)


def test_etj_currencyformat_constructor_args():
    sig = inspect.signature(eTJ_CurrencyFormat.__init__)
    params = list(sig.parameters.keys())



def test_etj_dailyworkinghours_is_not_abstract():
    assert not inspect.isabstract(eTJ_DailyWorkingHours)


def test_etj_dailyworkinghours_constructor_exists():
    assert callable(eTJ_DailyWorkingHours.__init__)


def test_etj_dailyworkinghours_constructor_args():
    sig = inspect.signature(eTJ_DailyWorkingHours.__init__)
    params = list(sig.parameters.keys())
    assert "dailyWorkingHours" in params, "Missing parameter 'dailyWorkingHours'"

def test_etj_dailyworkinghours_has_dailyWorkingHours():
    assert hasattr(eTJ_DailyWorkingHours, "dailyWorkingHours")
    descriptor = None
    for klass in eTJ_DailyWorkingHours.__mro__:
        if "dailyWorkingHours" in klass.__dict__:
            descriptor = klass.__dict__["dailyWorkingHours"]
            break
    assert isinstance(descriptor, property)



def test_etj_timingresolution_is_not_abstract():
    assert not inspect.isabstract(eTJ_TimingResolution)


def test_etj_timingresolution_constructor_exists():
    assert callable(eTJ_TimingResolution.__init__)


def test_etj_timingresolution_constructor_args():
    sig = inspect.signature(eTJ_TimingResolution.__init__)
    params = list(sig.parameters.keys())
    assert "timingResolution" in params, "Missing parameter 'timingResolution'"

def test_etj_timingresolution_has_timingResolution():
    assert hasattr(eTJ_TimingResolution, "timingResolution")
    descriptor = None
    for klass in eTJ_TimingResolution.__mro__:
        if "timingResolution" in klass.__dict__:
            descriptor = klass.__dict__["timingResolution"]
            break
    assert isinstance(descriptor, property)



def test_etj_currency_is_not_abstract():
    assert not inspect.isabstract(eTJ_Currency)


def test_etj_currency_constructor_exists():
    assert callable(eTJ_Currency.__init__)


def test_etj_currency_constructor_args():
    sig = inspect.signature(eTJ_Currency.__init__)
    params = list(sig.parameters.keys())
    assert "currency" in params, "Missing parameter 'currency'"

def test_etj_currency_has_currency():
    assert hasattr(eTJ_Currency, "currency")
    descriptor = None
    for klass in eTJ_Currency.__mro__:
        if "currency" in klass.__dict__:
            descriptor = klass.__dict__["currency"]
            break
    assert isinstance(descriptor, property)



def test_etj_isodate_is_not_abstract():
    assert not inspect.isabstract(eTJ_ISODATE)


def test_etj_isodate_constructor_exists():
    assert callable(eTJ_ISODATE.__init__)


def test_etj_isodate_constructor_args():
    sig = inspect.signature(eTJ_ISODATE.__init__)
    params = list(sig.parameters.keys())



def test_etj_credit_is_not_abstract():
    assert not inspect.isabstract(eTJ_Credit)


def test_etj_credit_constructor_exists():
    assert callable(eTJ_Credit.__init__)


def test_etj_credit_constructor_args():
    sig = inspect.signature(eTJ_Credit.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_etj_credit_has_description():
    assert hasattr(eTJ_Credit, "description")
    descriptor = None
    for klass in eTJ_Credit.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_etj_credit_has_amount():
    assert hasattr(eTJ_Credit, "amount")
    descriptor = None
    for klass in eTJ_Credit.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_etj_copyright_is_not_abstract():
    assert not inspect.isabstract(eTJ_Copyright)


def test_etj_copyright_constructor_exists():
    assert callable(eTJ_Copyright.__init__)


def test_etj_copyright_constructor_args():
    sig = inspect.signature(eTJ_Copyright.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_etj_copyright_has_text():
    assert hasattr(eTJ_Copyright, "text")
    descriptor = None
    for klass in eTJ_Copyright.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_etj_complete_is_not_abstract():
    assert not inspect.isabstract(eTJ_Complete)


def test_etj_complete_constructor_exists():
    assert callable(eTJ_Complete.__init__)


def test_etj_complete_constructor_args():
    sig = inspect.signature(eTJ_Complete.__init__)
    params = list(sig.parameters.keys())
    assert "complete" in params, "Missing parameter 'complete'"

def test_etj_complete_has_complete():
    assert hasattr(eTJ_Complete, "complete")
    descriptor = None
    for klass in eTJ_Complete.__mro__:
        if "complete" in klass.__dict__:
            descriptor = klass.__dict__["complete"]
            break
    assert isinstance(descriptor, property)



def test_etj_column_is_not_abstract():
    assert not inspect.isabstract(eTJ_Column)


def test_etj_column_constructor_exists():
    assert callable(eTJ_Column.__init__)


def test_etj_column_constructor_args():
    sig = inspect.signature(eTJ_Column.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_etj_column_has_id():
    assert hasattr(eTJ_Column, "id")
    descriptor = None
    for klass in eTJ_Column.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_etj_columns_is_not_abstract():
    assert not inspect.isabstract(eTJ_Columns)


def test_etj_columns_constructor_exists():
    assert callable(eTJ_Columns.__init__)


def test_etj_columns_constructor_args():
    sig = inspect.signature(eTJ_Columns.__init__)
    params = list(sig.parameters.keys())



def test_etj_interval4_is_not_abstract():
    assert not inspect.isabstract(eTJ_Interval4)


def test_etj_interval4_constructor_exists():
    assert callable(eTJ_Interval4.__init__)


def test_etj_interval4_constructor_args():
    sig = inspect.signature(eTJ_Interval4.__init__)
    params = list(sig.parameters.keys())



def test_etj_booking_is_not_abstract():
    assert not inspect.isabstract(eTJ_Booking)


def test_etj_booking_constructor_exists():
    assert callable(eTJ_Booking.__init__)


def test_etj_booking_constructor_args():
    sig = inspect.signature(eTJ_Booking.__init__)
    params = list(sig.parameters.keys())
    assert "sloppy" in params, "Missing parameter 'sloppy'"
    assert "overtime" in params, "Missing parameter 'overtime'"

def test_etj_booking_has_sloppy():
    assert hasattr(eTJ_Booking, "sloppy")
    descriptor = None
    for klass in eTJ_Booking.__mro__:
        if "sloppy" in klass.__dict__:
            descriptor = klass.__dict__["sloppy"]
            break
    assert isinstance(descriptor, property)

def test_etj_booking_has_overtime():
    assert hasattr(eTJ_Booking, "overtime")
    descriptor = None
    for klass in eTJ_Booking.__mro__:
        if "overtime" in klass.__dict__:
            descriptor = klass.__dict__["overtime"]
            break
    assert isinstance(descriptor, property)



def test_etj_bookingresource_is_not_abstract():
    assert not inspect.isabstract(eTJ_BookingResource)


def test_etj_bookingresource_constructor_exists():
    assert callable(eTJ_BookingResource.__init__)


def test_etj_bookingresource_constructor_args():
    sig = inspect.signature(eTJ_BookingResource.__init__)
    params = list(sig.parameters.keys())



def test_etj_bookingtask_is_not_abstract():
    assert not inspect.isabstract(eTJ_BookingTask)


def test_etj_bookingtask_constructor_exists():
    assert callable(eTJ_BookingTask.__init__)


def test_etj_bookingtask_constructor_args():
    sig = inspect.signature(eTJ_BookingTask.__init__)
    params = list(sig.parameters.keys())



def test_etj_navigatorattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_NavigatorAttribute)


def test_etj_navigatorattribute_constructor_exists():
    assert callable(eTJ_NavigatorAttribute.__init__)


def test_etj_navigatorattribute_constructor_args():
    sig = inspect.signature(eTJ_NavigatorAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_navigator_is_not_abstract():
    assert not inspect.isabstract(eTJ_Navigator)


def test_etj_navigator_constructor_exists():
    assert callable(eTJ_Navigator.__init__)


def test_etj_navigator_constructor_args():
    sig = inspect.signature(eTJ_Navigator.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_etj_navigator_has_id():
    assert hasattr(eTJ_Navigator, "id")
    descriptor = None
    for klass in eTJ_Navigator.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_etj_allocateresourceattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_AllocateResourceAttribute)


def test_etj_allocateresourceattribute_constructor_exists():
    assert callable(eTJ_AllocateResourceAttribute.__init__)


def test_etj_allocateresourceattribute_constructor_args():
    sig = inspect.signature(eTJ_AllocateResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_allocateresource_is_not_abstract():
    assert not inspect.isabstract(eTJ_AllocateResource)


def test_etj_allocateresource_constructor_exists():
    assert callable(eTJ_AllocateResource.__init__)


def test_etj_allocateresource_constructor_args():
    sig = inspect.signature(eTJ_AllocateResource.__init__)
    params = list(sig.parameters.keys())



def test_etj_allocate_is_not_abstract():
    assert not inspect.isabstract(eTJ_Allocate)


def test_etj_allocate_constructor_exists():
    assert callable(eTJ_Allocate.__init__)


def test_etj_allocate_constructor_args():
    sig = inspect.signature(eTJ_Allocate.__init__)
    params = list(sig.parameters.keys())



def test_etj_resourceattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ_ResourceAttribute)


def test_etj_resourceattribute_constructor_exists():
    assert callable(eTJ_ResourceAttribute.__init__)


def test_etj_resourceattribute_constructor_args():
    sig = inspect.signature(eTJ_ResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_resource_is_not_abstract():
    assert not inspect.isabstract(eTJ_Resource)


def test_etj_resource_constructor_exists():
    assert callable(eTJ_Resource.__init__)


def test_etj_resource_constructor_args():
    sig = inspect.signature(eTJ_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_etj_resource_has_id():
    assert hasattr(eTJ_Resource, "id")
    descriptor = None
    for klass in eTJ_Resource.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_etj_resource_has_name():
    assert hasattr(eTJ_Resource, "name")
    descriptor = None
    for klass in eTJ_Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_etj_balance_is_not_abstract():
    assert not inspect.isabstract(eTJ_Balance)


def test_etj_balance_constructor_exists():
    assert callable(eTJ_Balance.__init__)


def test_etj_balance_constructor_args():
    sig = inspect.signature(eTJ_Balance.__init__)
    params = list(sig.parameters.keys())



def test_statusstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(StatusStatusSheetAttribute)


def test_statusstatussheetattribute_constructor_exists():
    assert callable(StatusStatusSheetAttribute.__init__)


def test_statusstatussheetattribute_constructor_args():
    sig = inspect.signature(StatusStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj_summary_is_not_abstract():
    assert not inspect.isabstract(eTJ_Summary)


def test_etj_summary_constructor_exists():
    assert callable(eTJ_Summary.__init__)


def test_etj_summary_constructor_args():
    sig = inspect.signature(eTJ_Summary.__init__)
    params = list(sig.parameters.keys())



def test_etj_flags_is_not_abstract():
    assert not inspect.isabstract(eTJ_Flags)


def test_etj_flags_constructor_exists():
    assert callable(eTJ_Flags.__init__)


def test_etj_flags_constructor_args():
    sig = inspect.signature(eTJ_Flags.__init__)
    params = list(sig.parameters.keys())
    assert "flags" in params, "Missing parameter 'flags'"

def test_etj_flags_has_flags():
    assert hasattr(eTJ_Flags, "flags")
    descriptor = None
    for klass in eTJ_Flags.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)



def test_etj_details_is_not_abstract():
    assert not inspect.isabstract(eTJ_Details)


def test_etj_details_constructor_exists():
    assert callable(eTJ_Details.__init__)


def test_etj_details_constructor_args():
    sig = inspect.signature(eTJ_Details.__init__)
    params = list(sig.parameters.keys())



def test_etj_author_is_not_abstract():
    assert not inspect.isabstract(eTJ_Author)


def test_etj_author_constructor_exists():
    assert callable(eTJ_Author.__init__)


def test_etj_author_constructor_args():
    sig = inspect.signature(eTJ_Author.__init__)
    params = list(sig.parameters.keys())

def test_journalattributevalues_exists():
    # Check that the Enumeration exists
    assert JournalAttributeValues is not None

def test_journalattributevalues_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JournalAttributeValues]
    expected_literals = [
        "NONE",
        "date",
        "ALL",
        "summary",
        "flags",
        "details",
        "alert",
        "headline",
        "property",
        "propertyid",
        "timesheet",
        "author",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JournalAttributeValues"

def test_chargeapplies_exists():
    # Check that the Enumeration exists
    assert ChargeApplies is not None

def test_chargeapplies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ChargeApplies]
    expected_literals = [
        "ONSTART",
        "PERWEEK",
        "PERHOUR",
        "ONEND",
        "PERDAY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ChargeApplies"

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

def test_leavetype_exists():
    # Check that the Enumeration exists
    assert LeaveType is not None

def test_leavetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LeaveType]
    expected_literals = [
        "project",
        "unpaid",
        "holiday",
        "annual",
        "unemployed",
        "sick",
        "special",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LeaveType"

def test_journalentrysortcriterion_exists():
    # Check that the Enumeration exists
    assert JournalEntrySortCriterion is not None

def test_journalentrysortcriterion_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JournalEntrySortCriterion]
    expected_literals = [
        "ALERT_UP",
        "DATE_DOWN",
        "PROPERTY_UP",
        "ALERT_DOWN",
        "DATE_UP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JournalEntrySortCriterion"

def test_purgetaskattribute_exists():
    # Check that the Enumeration exists
    assert PurgeTaskAttribute is not None

def test_purgetaskattribute_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PurgeTaskAttribute]
    expected_literals = [
        "CHARGE",
        "FAIL",
        "FLAGS",
        "BOOKING",
        "WARN",
        "DEPENDS",
        "CHARGESET",
        "PRECEDES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PurgeTaskAttribute"

def test_purgereportattribute_exists():
    # Check that the Enumeration exists
    assert PurgeReportAttribute is not None

def test_purgereportattribute_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PurgeReportAttribute]
    expected_literals = [
        "SORTRESOURCES",
        "SORTTASKS",
        "SCENARIOS",
        "FORMATS",
        "JOURNALATTRIBUTES",
        "COLUMNS",
        "DEFINITIONS",
        "FLAGS",
        "SORTJOURNALENTRIES",
        "SORTACCOUNTS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PurgeReportAttribute"

def test_selectargument_exists():
    # Check that the Enumeration exists
    assert SelectArgument is not None

def test_selectargument_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SelectArgument]
    expected_literals = [
        "MINLOADED",
        "MINALLOCATED",
        "RANDOM",
        "ORDER",
        "MAXLOADED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SelectArgument"

def test_purgeresourceattribute_exists():
    # Check that the Enumeration exists
    assert PurgeResourceAttribute is not None

def test_purgeresourceattribute_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PurgeResourceAttribute]
    expected_literals = [
        "FAIL",
        "VACATIONS",
        "MANAGERS",
        "REPORTS",
        "FLAGS",
        "WARN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PurgeResourceAttribute"

def test_alertlevel_exists():
    # Check that the Enumeration exists
    assert AlertLevel is not None

def test_alertlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlertLevel]
    expected_literals = [
        "GREEN",
        "RED",
        "YELLOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlertLevel"

def test_journalmodevalue_exists():
    # Check that the Enumeration exists
    assert JournalModeValue is not None

def test_journalmodevalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JournalModeValue]
    expected_literals = [
        "JOURNAL_SUB",
        "STATUS_UP",
        "STATUS_DOWN",
        "JOURNAL",
        "ALERTS_DOWN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JournalModeValue"

def test_yesno_exists():
    # Check that the Enumeration exists
    assert YesNo is not None

def test_yesno_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in YesNo]
    expected_literals = [
        "NO",
        "YES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in YesNo"

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "MONTH",
        "YEAR",
        "MINUTE",
        "WEEK",
        "HOUR",
        "DAY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnit"

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

def test_loaddisplayunit_exists():
    # Check that the Enumeration exists
    assert LoadDisplayUnit is not None

def test_loaddisplayunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LoadDisplayUnit]
    expected_literals = [
        "SHORTAUTO",
        "MINUTES",
        "DAYS",
        "LONGAUTO",
        "HOURS",
        "YEARS",
        "WEEKS",
        "MONTHS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LoadDisplayUnit"

def test_buildinmacro_exists():
    # Check that the Enumeration exists
    assert BuildInMacro is not None

def test_buildinmacro_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuildInMacro]
    expected_literals = [
        "projectend",
        "projectstart",
        "now",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuildInMacro"

def test_weekday_exists():
    # Check that the Enumeration exists
    assert Weekday is not None

def test_weekday_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Weekday]
    expected_literals = [
        "SAT",
        "THR",
        "FRI",
        "MON",
        "SUN",
        "TUE",
        "WED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Weekday"

def test_scaleresolution_exists():
    # Check that the Enumeration exists
    assert ScaleResolution is not None

def test_scaleresolution_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScaleResolution]
    expected_literals = [
        "WEEK",
        "YEAR",
        "MONTH",
        "QUARTER",
        "DAY",
        "HOUR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScaleResolution"

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
        "PERCENT",
        "DAYS",
        "MINUTES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkQuantityUnit"

def test_reportformat_exists():
    # Check that the Enumeration exists
    assert ReportFormat is not None

def test_reportformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReportFormat]
    expected_literals = [
        "HTML",
        "CSV",
        "NIKU",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReportFormat"

def test_columnid_exists():
    # Check that the Enumeration exists
    assert ColumnId is not None

def test_columnid_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColumnId]
    expected_literals = [
        "seqno",
        "closedtasks",
        "targets",
        "completed",
        "line",
        "monthly",
        "journalsummaries",
        "competitors",
        "email",
        "criticalness",
        "scenario",
        "children",
        "weekly",
        "daily",
        "reports",
        "freetime",
        "priority",
        "gauge",
        "minstart",
        "sickleave",
        "opentasks",
        "annualleavebalance",
        "index",
        "inputs",
        "yearly",
        "activetasks",
        "resources",
        "quarterly",
        "specialleave",
        "followers",
        "maxstart",
        "cost",
        "bsi",
        "rate",
        "id",
        "scheduling",
        "alertsummaries",
        "freework",
        "competitorcount",
        "note",
        "fte",
        "effortdone",
        "status",
        "headcount",
        "turnover",
        "start",
        "directreports",
        "journal_sub",
        "maxend",
        "complete",
        "duties",
        "revenue",
        "annualleave",
        "flags",
        "journal",
        "effortleft",
        "hierarchindex",
        "no",
        "hourly",
        "wbs",
        "alertmessages",
        "effort",
        "precursors",
        "end",
        "unpaidleave",
        "balance",
        "journalmessages",
        "minend",
        "chart",
        "alert",
        "duration",
        "managers",
        "pathcriticalness",
        "name",
        "responsible",
        "alerttrend",
        "efficiency",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColumnId"

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
LogicalExpression_strategy = st.builds(
    LogicalExpression,
)
eTJ_LogicalDateLiteral_strategy = st.builds(
    eTJ_LogicalDateLiteral,
)
eTJ_LogicalNumeralLiteral_strategy = st.builds(
    eTJ_LogicalNumeralLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ_LogicalAbsoluteIdExression_strategy = st.builds(
    eTJ_LogicalAbsoluteIdExression,
    value=
        safe_text
)
eTJ_LogicalFlagExpression_strategy = st.builds(
    eTJ_LogicalFlagExpression,
    columId=
        safe_text
)
eTJ_LogicalBooleanLiteral_strategy = st.builds(
    eTJ_LogicalBooleanLiteral,
    isTrue=
        st.booleans()
)
eTJ_LogicalStringLiteral_strategy = st.builds(
    eTJ_LogicalStringLiteral,
    value=
        safe_text
)
eTJ_LogicalFunctionExpression_strategy = st.builds(
    eTJ_LogicalFunctionExpression,
)
Definitions_strategy = st.builds(
    Definitions,
)
eTJ_Defintions_strategy = st.builds(
    eTJ_Defintions,
    project=
        st.booleans(),
    flags=
        st.booleans(),
    tasks=
        st.booleans(),
    resources=
        st.booleans(),
    projectids=
        st.booleans()
)
eTJ_ExtDate_strategy = st.builds(
    eTJ_ExtDate,
)
NumberFormat_strategy = st.builds(
    NumberFormat,
)
CurrencyFormat_strategy = st.builds(
    CurrencyFormat,
)
eTJ_RealFormat_strategy = st.builds(
    eTJ_RealFormat,
    fractionSeparator=
        safe_text,
    thousandsSeparator=
        safe_text,
    fractionDigits=
        st.integers(),
    negativeSuffix=
        safe_text,
    negativePrefix=
        safe_text
)
eTJ_LimitAttribute_strategy = st.builds(
    eTJ_LimitAttribute,
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
eTJ_RichText_strategy = st.builds(
    eTJ_RichText,
    text=
        safe_text
)
Precedes_strategy = st.builds(
    Precedes,
)
eTJ_ColumnAttribute_strategy = st.builds(
    eTJ_ColumnAttribute,
)
eTJ_WorkHours_strategy = st.builds(
    eTJ_WorkHours,
    start=
        safe_text,
    stop=
        safe_text
)
eTJ_Weekdays_strategy = st.builds(
    eTJ_Weekdays,
    first=
        safe_text,
    last=
        safe_text
)
WeeklyMin_strategy = st.builds(
    WeeklyMin,
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
eTJ_Limit_strategy = st.builds(
    eTJ_Limit,
)
GapLength_strategy = st.builds(
    GapLength,
)
GapDuration_strategy = st.builds(
    GapDuration,
)
eTJ_TreeLevel_strategy = st.builds(
    eTJ_TreeLevel,
    level=
        safe_text
)
eTJ_TimesheetReportAttribute_strategy = st.builds(
    eTJ_TimesheetReportAttribute,
)
eTJ_TimesheetAttribute_strategy = st.builds(
    eTJ_TimesheetAttribute,
)
eTJ_TaskTimesheetAttribute_strategy = st.builds(
    eTJ_TaskTimesheetAttribute,
)
eTJ_TaskStatusSheetAttribute_strategy = st.builds(
    eTJ_TaskStatusSheetAttribute,
)
StatusSheetAttribute_strategy = st.builds(
    StatusSheetAttribute,
)
AllocateResourceAttribute_strategy = st.builds(
    AllocateResourceAttribute,
)
eTJ_Alternative_strategy = st.builds(
    eTJ_Alternative,
)
eTJ_Alert_strategy = st.builds(
    eTJ_Alert,
    level=
        safe_text
)
eTJ_NikuReportAttribute_strategy = st.builds(
    eTJ_NikuReportAttribute,
)
eTJ_NewTaskAttribute_strategy = st.builds(
    eTJ_NewTaskAttribute,
)
TimesheetAttribute_strategy = st.builds(
    TimesheetAttribute,
)
eTJ_TaskTimesheet_strategy = st.builds(
    eTJ_TaskTimesheet,
)
eTJ_NewTask_strategy = st.builds(
    eTJ_NewTask,
    text=
        safe_text,
    id=
        safe_text
)
ExtDate_strategy = st.builds(
    ExtDate,
)
Start_strategy = st.builds(
    Start,
)
End_strategy = st.builds(
    End,
)
eTJ_MacroCall_strategy = st.builds(
    eTJ_MacroCall,
    buildin=
        safe_text
)
eTJ_EObject_strategy = st.builds(
    eTJ_EObject,
)
eTJ_TaskAttribute_strategy = st.builds(
    eTJ_TaskAttribute,
)
eTJ_ProjectAttribute_strategy = st.builds(
    eTJ_ProjectAttribute,
)
eTJ_ExportAttribute_strategy = st.builds(
    eTJ_ExportAttribute,
)
eTJ_IcalReportAttribute_strategy = st.builds(
    eTJ_IcalReportAttribute,
)
eTJ_ReportAttribute_strategy = st.builds(
    eTJ_ReportAttribute,
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
eTJ_Report_strategy = st.builds(
    eTJ_Report,
    name=
        safe_text,
    id=
        safe_text
)
eTJ_AccountAttribute_strategy = st.builds(
    eTJ_AccountAttribute,
)
AccountAttribute_strategy = st.builds(
    AccountAttribute,
)
eTJ_Interval2_strategy = st.builds(
    eTJ_Interval2,
)
ReportAttribute_strategy = st.builds(
    ReportAttribute,
)
eTJ_TaskRoot_strategy = st.builds(
    eTJ_TaskRoot,
)
eTJ_AccountRoot_strategy = st.builds(
    eTJ_AccountRoot,
)
IncludePropertiesAttribute_strategy = st.builds(
    IncludePropertiesAttribute,
)
eTJ_TaskPrefix_strategy = st.builds(
    eTJ_TaskPrefix,
)
eTJ_AccountPrefix_strategy = st.builds(
    eTJ_AccountPrefix,
)
eTJ_Property_strategy = st.builds(
    eTJ_Property,
)
eTJ_Project_strategy = st.builds(
    eTJ_Project,
    name=
        safe_text,
    version=
        safe_text,
    id=
        safe_text
)
eTJ_Global_strategy = st.builds(
    eTJ_Global,
)
eTJ_Interval3_strategy = st.builds(
    eTJ_Interval3,
)
eTJ_LeaveDetails_strategy = st.builds(
    eTJ_LeaveDetails,
    name=
        safe_text,
    type=
        safe_text
)
ResourceAttribute_strategy = st.builds(
    ResourceAttribute,
)
eTJ_Warn_strategy = st.builds(
    eTJ_Warn,
)
Property_strategy = st.builds(
    Property,
)
eTJ_IcalReport_strategy = st.builds(
    eTJ_IcalReport,
    filename=
        safe_text
)
eTJ_Macro_strategy = st.builds(
    eTJ_Macro,
    id=
        safe_text,
    value=
        safe_text
)
eTJ_NikuReport_strategy = st.builds(
    eTJ_NikuReport,
    filename=
        safe_text
)
eTJ_TextReport_strategy = st.builds(
    eTJ_TextReport,
)
eTJ_TimesheetReport_strategy = st.builds(
    eTJ_TimesheetReport,
    filename=
        safe_text
)
eTJ_Account_strategy = st.builds(
    eTJ_Account,
    id=
        safe_text,
    name=
        safe_text
)
eTJ_Timesheet_strategy = st.builds(
    eTJ_Timesheet,
)
eTJ_TaskReport_strategy = st.builds(
    eTJ_TaskReport,
)
eTJ_Task_strategy = st.builds(
    eTJ_Task,
    id=
        safe_text,
    name=
        safe_text
)
eTJ_AccountReport_strategy = st.builds(
    eTJ_AccountReport,
)
eTJ_Export_strategy = st.builds(
    eTJ_Export,
    filename=
        safe_text,
    id=
        safe_text
)
eTJ_Leaves_strategy = st.builds(
    eTJ_Leaves,
)
eTJ_SupplementAccount_strategy = st.builds(
    eTJ_SupplementAccount,
)
eTJ_StatusSheetReportAttribute_strategy = st.builds(
    eTJ_StatusSheetReportAttribute,
)
eTJ_StatusSheetReport_strategy = st.builds(
    eTJ_StatusSheetReport,
    filename=
        safe_text
)
eTJ_StatusSheetAttribute_strategy = st.builds(
    eTJ_StatusSheetAttribute,
)
eTJ_StatusSheet_strategy = st.builds(
    eTJ_StatusSheet,
)
eTJ_TagFile_strategy = st.builds(
    eTJ_TagFile,
    id=
        safe_text,
    filename=
        safe_text
)
eTJ_SupplementTask_strategy = st.builds(
    eTJ_SupplementTask,
)
eTJ_SupplementResource_strategy = st.builds(
    eTJ_SupplementResource,
)
eTJ_SupplementReport_strategy = st.builds(
    eTJ_SupplementReport,
)
eTJ_SortJournalEntries_strategy = st.builds(
    eTJ_SortJournalEntries,
)
eTJ_SortAccounts_strategy = st.builds(
    eTJ_SortAccounts,
)
eTJ_Criterion_strategy = st.builds(
    eTJ_Criterion,
    columnId=
        safe_text,
    direction=
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
eTJ_Sort_strategy = st.builds(
    eTJ_Sort,
    tree=
        st.booleans()
)
eTJ_ShiftsTask_strategy = st.builds(
    eTJ_ShiftsTask,
)
eTJ_ShiftsResource_strategy = st.builds(
    eTJ_ShiftsResource,
)
eTJ_StatusTimesheetAttribute_strategy = st.builds(
    eTJ_StatusTimesheetAttribute,
)
eTJ_StatusStatusSheetAttribute_strategy = st.builds(
    eTJ_StatusStatusSheetAttribute,
)
TaskStatusSheetAttribute_strategy = st.builds(
    TaskStatusSheetAttribute,
)
eTJ_TaskStatusSheet_strategy = st.builds(
    eTJ_TaskStatusSheet,
)
eTJ_StatusStatusSheet_strategy = st.builds(
    eTJ_StatusStatusSheet,
    level=
        safe_text,
    text=
        safe_text
)
eTJ_Shift_strategy = st.builds(
    eTJ_Shift,
    replace=
        safe_text,
    name=
        safe_text,
    id=
        safe_text,
    timezone=
        safe_text
)
eTJ_SelfContained_strategy = st.builds(
    eTJ_SelfContained,
    selfcontained=
        safe_text
)
eTJ_Select_strategy = st.builds(
    eTJ_Select,
    argument=
        safe_text
)
eTJ_Scheduling_strategy = st.builds(
    eTJ_Scheduling,
    scheduling=
        safe_text
)
eTJ_Scheduled_strategy = st.builds(
    eTJ_Scheduled,
    scheduled=
        st.booleans()
)
eTJ_ShiftsAllocate_strategy = st.builds(
    eTJ_ShiftsAllocate,
)
eTJ_ShiftsLimit_strategy = st.builds(
    eTJ_ShiftsLimit,
)
ShiftsTask_strategy = st.builds(
    ShiftsTask,
)
ShiftsResource_strategy = st.builds(
    ShiftsResource,
)
eTJ_Shifts_strategy = st.builds(
    eTJ_Shifts,
)
eTJ_ShiftTimesheet_strategy = st.builds(
    eTJ_ShiftTimesheet,
)
eTJ_Vacation_strategy = st.builds(
    eTJ_Vacation,
    name=
        safe_text
)
eTJ_RollupAccount_strategy = st.builds(
    eTJ_RollupAccount,
)
eTJ_Right_strategy = st.builds(
    eTJ_Right,
)
eTJ_Responsible_strategy = st.builds(
    eTJ_Responsible,
)
eTJ_ResourceRoot_strategy = st.builds(
    eTJ_ResourceRoot,
)
eTJ_ResourceReport_strategy = st.builds(
    eTJ_ResourceReport,
)
eTJ_PurgeTask_strategy = st.builds(
    eTJ_PurgeTask,
    listAttribute=
        safe_text
)
eTJ_PurgeResource_strategy = st.builds(
    eTJ_PurgeResource,
    listAttribute=
        safe_text
)
eTJ_ResourcePrefix_strategy = st.builds(
    eTJ_ResourcePrefix,
)
eTJ_ReportPrefix_strategy = st.builds(
    eTJ_ReportPrefix,
)
eTJ_Rate_strategy = st.builds(
    eTJ_Rate,
    rate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ_Note_strategy = st.builds(
    eTJ_Note,
    note=
        safe_text
)
eTJ_PurgeReport_strategy = st.builds(
    eTJ_PurgeReport,
    listAttribute=
        safe_text
)
eTJ_Prolog_strategy = st.builds(
    eTJ_Prolog,
)
eTJ_ProjectIds_strategy = st.builds(
    eTJ_ProjectIds,
    ids=
        safe_text
)
eTJ_ProjectId_strategy = st.builds(
    eTJ_ProjectId,
    projectId=
        safe_text
)
eTJ_Precedes_strategy = st.builds(
    eTJ_Precedes,
)
eTJ_Persistent_strategy = st.builds(
    eTJ_Persistent,
    persistent=
        st.booleans()
)
eTJ_LoadUnit_strategy = st.builds(
    eTJ_LoadUnit,
    unit=
        safe_text
)
eTJ_LimitsAttribute_strategy = st.builds(
    eTJ_LimitsAttribute,
)
eTJ_Limits_strategy = st.builds(
    eTJ_Limits,
)
eTJ_MinStart_strategy = st.builds(
    eTJ_MinStart,
)
eTJ_MinEnd_strategy = st.builds(
    eTJ_MinEnd,
)
eTJ_Milestone_strategy = st.builds(
    eTJ_Milestone,
    milestone=
        st.booleans()
)
eTJ_MaxStart_strategy = st.builds(
    eTJ_MaxStart,
)
eTJ_MaxEnd_strategy = st.builds(
    eTJ_MaxEnd,
)
eTJ_Mandatory_strategy = st.builds(
    eTJ_Mandatory,
    mandatory=
        st.booleans()
)
eTJ_Managers_strategy = st.builds(
    eTJ_Managers,
)
eTJ_JournalAttributes_strategy = st.builds(
    eTJ_JournalAttributes,
    args=
        safe_text
)
eTJ_Length_strategy = st.builds(
    eTJ_Length,
)
eTJ_Left_strategy = st.builds(
    eTJ_Left,
)
eTJ_JournalMode_strategy = st.builds(
    eTJ_JournalMode,
    mode=
        safe_text
)
NavigatorAttribute_strategy = st.builds(
    NavigatorAttribute,
)
eTJ_HideReport_strategy = st.builds(
    eTJ_HideReport,
)
eTJ_Interval1_strategy = st.builds(
    eTJ_Interval1,
)
eTJ_IncludePropertiesAttribute_strategy = st.builds(
    eTJ_IncludePropertiesAttribute,
)
eTJ_IncludeProperties_strategy = st.builds(
    eTJ_IncludeProperties,
    importURI=
        safe_text
)
eTJ_Footer_strategy = st.builds(
    eTJ_Footer,
)
eTJ_Fail_strategy = st.builds(
    eTJ_Fail,
)
eTJ_ExtendedTaskAttribute_strategy = st.builds(
    eTJ_ExtendedTaskAttribute,
    value=
        safe_text
)
eTJ_HideAccount_strategy = st.builds(
    eTJ_HideAccount,
    expression=
        safe_text
)
eTJ_Header_strategy = st.builds(
    eTJ_Header,
)
eTJ_GapLength_strategy = st.builds(
    eTJ_GapLength,
)
eTJ_GapDuration_strategy = st.builds(
    eTJ_GapDuration,
)
eTJ_Function_strategy = st.builds(
    eTJ_Function,
    parentId=
        safe_text,
    distance=
        st.integers(),
    level=
        st.integers()
)
NewTaskAttribute_strategy = st.builds(
    NewTaskAttribute,
)
IcalReportAttribute_strategy = st.builds(
    IcalReportAttribute,
)
eTJ_HideJournalEntry_strategy = st.builds(
    eTJ_HideJournalEntry,
    expression=
        safe_text
)
eTJ_ScenarioIcal_strategy = st.builds(
    eTJ_ScenarioIcal,
)
eTJ_Email_strategy = st.builds(
    eTJ_Email,
    address=
        safe_text
)
eTJ_Effort_strategy = st.builds(
    eTJ_Effort,
)
eTJ_Efficiency_strategy = st.builds(
    eTJ_Efficiency,
    efficiency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ_DurationQuantity_strategy = st.builds(
    eTJ_DurationQuantity,
    unit=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ_Duration_strategy = st.builds(
    eTJ_Duration,
)
StatusTimesheetAttribute_strategy = st.builds(
    StatusTimesheetAttribute,
)
eTJ_TaskDependency_strategy = st.builds(
    eTJ_TaskDependency,
    policy=
        safe_text
)
eTJ_Depends_strategy = st.builds(
    eTJ_Depends,
)
eTJ_ExtendedResourceAttribute_strategy = st.builds(
    eTJ_ExtendedResourceAttribute,
    value=
        safe_text
)
eTJ_Extend_strategy = st.builds(
    eTJ_Extend,
    inherit=
        st.booleans(),
    description=
        safe_text,
    scenariospecific=
        st.booleans(),
    name=
        safe_text
)
eTJ_Epilog_strategy = st.builds(
    eTJ_Epilog,
)
eTJ_EndCredit_strategy = st.builds(
    eTJ_EndCredit,
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
TimesheetReportAttribute_strategy = st.builds(
    TimesheetReportAttribute,
)
TaskTimesheetAttribute_strategy = st.builds(
    TaskTimesheetAttribute,
)
eTJ_Remaining_strategy = st.builds(
    eTJ_Remaining,
)
eTJ_StatusTimesheet_strategy = st.builds(
    eTJ_StatusTimesheet,
    level=
        safe_text,
    text=
        safe_text
)
eTJ_Priority_strategy = st.builds(
    eTJ_Priority,
    priority=
        st.integers()
)
eTJ_Work_strategy = st.builds(
    eTJ_Work,
    unit=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
StatusSheetReportAttribute_strategy = st.builds(
    StatusSheetReportAttribute,
)
eTJ_SortTasks_strategy = st.builds(
    eTJ_SortTasks,
)
eTJ_SortResources_strategy = st.builds(
    eTJ_SortResources,
)
NikuReportAttribute_strategy = st.builds(
    NikuReportAttribute,
)
eTJ_Formats_strategy = st.builds(
    eTJ_Formats,
    formats=
        safe_text
)
eTJ_Headline_strategy = st.builds(
    eTJ_Headline,
)
eTJ_Timeoff_strategy = st.builds(
    eTJ_Timeoff,
    name=
        safe_text,
    id=
        safe_text
)
eTJ_AccountShare_strategy = st.builds(
    eTJ_AccountShare,
    share=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ_ChargeSet_strategy = st.builds(
    eTJ_ChargeSet,
)
eTJ_Charge_strategy = st.builds(
    eTJ_Charge,
    applies=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ_Center_strategy = st.builds(
    eTJ_Center,
)
eTJ_RGB_strategy = st.builds(
    eTJ_RGB,
    value=
        safe_text
)
eTJ_LogicalExpression_strategy = st.builds(
    eTJ_LogicalExpression,
    op=
        safe_text
)
ColumnAttribute_strategy = st.builds(
    ColumnAttribute,
)
eTJ_FontColor_strategy = st.builds(
    eTJ_FontColor,
    color=
        safe_text
)
eTJ_CellText_strategy = st.builds(
    eTJ_CellText,
    text=
        safe_text
)
eTJ_HAlign_strategy = st.builds(
    eTJ_HAlign,
    justification=
        safe_text
)
eTJ_Scale_strategy = st.builds(
    eTJ_Scale,
    scale=
        safe_text
)
eTJ_Title_strategy = st.builds(
    eTJ_Title,
    title=
        safe_text
)
eTJ_ExtendedResourceAttributeColumn_strategy = st.builds(
    eTJ_ExtendedResourceAttributeColumn,
)
eTJ_ListType_strategy = st.builds(
    eTJ_ListType,
    type=
        safe_text
)
eTJ_ToolTip_strategy = st.builds(
    eTJ_ToolTip,
    tip=
        safe_text
)
eTJ_ListItem_strategy = st.builds(
    eTJ_ListItem,
)
eTJ_Width_strategy = st.builds(
    eTJ_Width,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ_CellColor_strategy = st.builds(
    eTJ_CellColor,
)
eTJ_Caption_strategy = st.builds(
    eTJ_Caption,
)
ExportAttribute_strategy = st.builds(
    ExportAttribute,
)
eTJ_ResourceAttributes_strategy = st.builds(
    eTJ_ResourceAttributes,
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
eTJ_HideTask_strategy = st.builds(
    eTJ_HideTask,
)
eTJ_HideResource_strategy = st.builds(
    eTJ_HideResource,
)
eTJ_End_strategy = st.builds(
    eTJ_End,
)
eTJ_Scenarios_strategy = st.builds(
    eTJ_Scenarios,
)
eTJ_TaskAttributes_strategy = st.builds(
    eTJ_TaskAttributes,
    flags=
        st.booleans(),
    maxstart=
        st.booleans(),
    none=
        st.booleans(),
    note=
        st.booleans(),
    all=
        st.booleans(),
    responsible=
        st.booleans(),
    maxend=
        st.booleans(),
    priority=
        st.booleans(),
    minstart=
        st.booleans(),
    booking=
        st.booleans(),
    complete=
        st.booleans(),
    depends=
        st.booleans(),
    minend=
        st.booleans()
)
eTJ_Start_strategy = st.builds(
    eTJ_Start,
)
eTJ_Period_strategy = st.builds(
    eTJ_Period,
)
eTJ_RollupTask_strategy = st.builds(
    eTJ_RollupTask,
)
eTJ_RollupResource_strategy = st.builds(
    eTJ_RollupResource,
)
eTJ_Definitions_strategy = st.builds(
    eTJ_Definitions,
    all=
        st.booleans(),
    none=
        st.booleans()
)
LimitsAttribute_strategy = st.builds(
    LimitsAttribute,
)
eTJ_WeeklyMax_strategy = st.builds(
    eTJ_WeeklyMax,
)
eTJ_Minimum_strategy = st.builds(
    eTJ_Minimum,
)
eTJ_MonthlyMin_strategy = st.builds(
    eTJ_MonthlyMin,
)
eTJ_WeeklyMin_strategy = st.builds(
    eTJ_WeeklyMin,
)
eTJ_DailyMin_strategy = st.builds(
    eTJ_DailyMin,
)
eTJ_Maximum_strategy = st.builds(
    eTJ_Maximum,
)
eTJ_MonthlyMax_strategy = st.builds(
    eTJ_MonthlyMax,
)
eTJ_DailyMax_strategy = st.builds(
    eTJ_DailyMax,
)
ProjectAttribute_strategy = st.builds(
    ProjectAttribute,
)
eTJ_YearlyWorkingDays_strategy = st.builds(
    eTJ_YearlyWorkingDays,
    yearlyWorkingDays=
        st.integers()
)
eTJ_ExtendResource_strategy = st.builds(
    eTJ_ExtendResource,
)
eTJ_ShortTimeFormat_strategy = st.builds(
    eTJ_ShortTimeFormat,
    shortTimeFormat=
        safe_text
)
eTJ_TrackingScenario_strategy = st.builds(
    eTJ_TrackingScenario,
)
eTJ_JournalEntry_strategy = st.builds(
    eTJ_JournalEntry,
    headline=
        safe_text
)
eTJ_WeekStarts_strategy = st.builds(
    eTJ_WeekStarts,
    monday=
        st.booleans(),
    sunday=
        st.booleans()
)
eTJ_WorkingHours_strategy = st.builds(
    eTJ_WorkingHours,
    off=
        st.booleans()
)
eTJ_Now_strategy = st.builds(
    eTJ_Now,
)
eTJ_Scenario_strategy = st.builds(
    eTJ_Scenario,
    name=
        safe_text,
    id=
        safe_text,
    active=
        safe_text
)
eTJ_Include_strategy = st.builds(
    eTJ_Include,
    importURI=
        safe_text
)
eTJ_Timezone_strategy = st.builds(
    eTJ_Timezone,
    timezone=
        safe_text
)
eTJ_TimeFormat_strategy = st.builds(
    eTJ_TimeFormat,
    timeformat=
        safe_text
)
eTJ_NumberFormat_strategy = st.builds(
    eTJ_NumberFormat,
)
eTJ_ExtendTask_strategy = st.builds(
    eTJ_ExtendTask,
)
eTJ_CurrencyFormat_strategy = st.builds(
    eTJ_CurrencyFormat,
)
eTJ_DailyWorkingHours_strategy = st.builds(
    eTJ_DailyWorkingHours,
    dailyWorkingHours=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ_TimingResolution_strategy = st.builds(
    eTJ_TimingResolution,
    timingResolution=
        st.integers()
)
eTJ_Currency_strategy = st.builds(
    eTJ_Currency,
    currency=
        safe_text
)
eTJ_ISODATE_strategy = st.builds(
    eTJ_ISODATE,
)
eTJ_Credit_strategy = st.builds(
    eTJ_Credit,
    description=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ_Copyright_strategy = st.builds(
    eTJ_Copyright,
    text=
        safe_text
)
eTJ_Complete_strategy = st.builds(
    eTJ_Complete,
    complete=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ_Column_strategy = st.builds(
    eTJ_Column,
    id=
        safe_text
)
eTJ_Columns_strategy = st.builds(
    eTJ_Columns,
)
eTJ_Interval4_strategy = st.builds(
    eTJ_Interval4,
)
eTJ_Booking_strategy = st.builds(
    eTJ_Booking,
    sloppy=
        st.integers(),
    overtime=
        st.integers()
)
eTJ_BookingResource_strategy = st.builds(
    eTJ_BookingResource,
)
eTJ_BookingTask_strategy = st.builds(
    eTJ_BookingTask,
)
eTJ_NavigatorAttribute_strategy = st.builds(
    eTJ_NavigatorAttribute,
)
eTJ_Navigator_strategy = st.builds(
    eTJ_Navigator,
    id=
        safe_text
)
eTJ_AllocateResourceAttribute_strategy = st.builds(
    eTJ_AllocateResourceAttribute,
)
eTJ_AllocateResource_strategy = st.builds(
    eTJ_AllocateResource,
)
eTJ_Allocate_strategy = st.builds(
    eTJ_Allocate,
)
eTJ_ResourceAttribute_strategy = st.builds(
    eTJ_ResourceAttribute,
)
eTJ_Resource_strategy = st.builds(
    eTJ_Resource,
    id=
        safe_text,
    name=
        safe_text
)
eTJ_Balance_strategy = st.builds(
    eTJ_Balance,
)
StatusStatusSheetAttribute_strategy = st.builds(
    StatusStatusSheetAttribute,
)
eTJ_Summary_strategy = st.builds(
    eTJ_Summary,
)
eTJ_Flags_strategy = st.builds(
    eTJ_Flags,
    flags=
        safe_text
)
eTJ_Details_strategy = st.builds(
    eTJ_Details,
)
eTJ_Author_strategy = st.builds(
    eTJ_Author,
)

@given(instance=LogicalExpression_strategy)
@settings(max_examples=50)
def test_logicalexpression_instantiation(instance):
    assert isinstance(instance, LogicalExpression)

@given(instance=eTJ_LogicalDateLiteral_strategy)
@settings(max_examples=50)
def test_etj_logicaldateliteral_instantiation(instance):
    assert isinstance(instance, eTJ_LogicalDateLiteral)

@given(instance=eTJ_LogicalNumeralLiteral_strategy)
@settings(max_examples=50)
def test_etj_logicalnumeralliteral_instantiation(instance):
    assert isinstance(instance, eTJ_LogicalNumeralLiteral)



@given(instance=eTJ_LogicalNumeralLiteral_strategy)
def test_etj_logicalnumeralliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ_LogicalAbsoluteIdExression_strategy)
@settings(max_examples=50)
def test_etj_logicalabsoluteidexression_instantiation(instance):
    assert isinstance(instance, eTJ_LogicalAbsoluteIdExression)



@given(instance=eTJ_LogicalAbsoluteIdExression_strategy)
def test_etj_logicalabsoluteidexression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ_LogicalFlagExpression_strategy)
@settings(max_examples=50)
def test_etj_logicalflagexpression_instantiation(instance):
    assert isinstance(instance, eTJ_LogicalFlagExpression)



@given(instance=eTJ_LogicalFlagExpression_strategy)
def test_etj_logicalflagexpression_columId_setter(instance):
    original = instance.columId
    instance.columId = original
    assert instance.columId == original

@given(instance=eTJ_LogicalBooleanLiteral_strategy)
@settings(max_examples=50)
def test_etj_logicalbooleanliteral_instantiation(instance):
    assert isinstance(instance, eTJ_LogicalBooleanLiteral)



@given(instance=eTJ_LogicalBooleanLiteral_strategy)
def test_etj_logicalbooleanliteral_isTrue_setter(instance):
    original = instance.isTrue
    instance.isTrue = original
    assert instance.isTrue == original

@given(instance=eTJ_LogicalStringLiteral_strategy)
@settings(max_examples=50)
def test_etj_logicalstringliteral_instantiation(instance):
    assert isinstance(instance, eTJ_LogicalStringLiteral)



@given(instance=eTJ_LogicalStringLiteral_strategy)
def test_etj_logicalstringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ_LogicalFunctionExpression_strategy)
@settings(max_examples=50)
def test_etj_logicalfunctionexpression_instantiation(instance):
    assert isinstance(instance, eTJ_LogicalFunctionExpression)

@given(instance=Definitions_strategy)
@settings(max_examples=50)
def test_definitions_instantiation(instance):
    assert isinstance(instance, Definitions)

@given(instance=eTJ_Defintions_strategy)
@settings(max_examples=50)
def test_etj_defintions_instantiation(instance):
    assert isinstance(instance, eTJ_Defintions)



@given(instance=eTJ_Defintions_strategy)
def test_etj_defintions_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original



@given(instance=eTJ_Defintions_strategy)
def test_etj_defintions_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original



@given(instance=eTJ_Defintions_strategy)
def test_etj_defintions_tasks_setter(instance):
    original = instance.tasks
    instance.tasks = original
    assert instance.tasks == original



@given(instance=eTJ_Defintions_strategy)
def test_etj_defintions_resources_setter(instance):
    original = instance.resources
    instance.resources = original
    assert instance.resources == original



@given(instance=eTJ_Defintions_strategy)
def test_etj_defintions_projectids_setter(instance):
    original = instance.projectids
    instance.projectids = original
    assert instance.projectids == original

@given(instance=eTJ_ExtDate_strategy)
@settings(max_examples=50)
def test_etj_extdate_instantiation(instance):
    assert isinstance(instance, eTJ_ExtDate)

@given(instance=NumberFormat_strategy)
@settings(max_examples=50)
def test_numberformat_instantiation(instance):
    assert isinstance(instance, NumberFormat)

@given(instance=CurrencyFormat_strategy)
@settings(max_examples=50)
def test_currencyformat_instantiation(instance):
    assert isinstance(instance, CurrencyFormat)

@given(instance=eTJ_RealFormat_strategy)
@settings(max_examples=50)
def test_etj_realformat_instantiation(instance):
    assert isinstance(instance, eTJ_RealFormat)



@given(instance=eTJ_RealFormat_strategy)
def test_etj_realformat_fractionSeparator_setter(instance):
    original = instance.fractionSeparator
    instance.fractionSeparator = original
    assert instance.fractionSeparator == original



@given(instance=eTJ_RealFormat_strategy)
def test_etj_realformat_thousandsSeparator_setter(instance):
    original = instance.thousandsSeparator
    instance.thousandsSeparator = original
    assert instance.thousandsSeparator == original



@given(instance=eTJ_RealFormat_strategy)
def test_etj_realformat_fractionDigits_setter(instance):
    original = instance.fractionDigits
    instance.fractionDigits = original
    assert instance.fractionDigits == original



@given(instance=eTJ_RealFormat_strategy)
def test_etj_realformat_negativeSuffix_setter(instance):
    original = instance.negativeSuffix
    instance.negativeSuffix = original
    assert instance.negativeSuffix == original



@given(instance=eTJ_RealFormat_strategy)
def test_etj_realformat_negativePrefix_setter(instance):
    original = instance.negativePrefix
    instance.negativePrefix = original
    assert instance.negativePrefix == original

@given(instance=eTJ_LimitAttribute_strategy)
@settings(max_examples=50)
def test_etj_limitattribute_instantiation(instance):
    assert isinstance(instance, eTJ_LimitAttribute)

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

@given(instance=eTJ_RichText_strategy)
@settings(max_examples=50)
def test_etj_richtext_instantiation(instance):
    assert isinstance(instance, eTJ_RichText)



@given(instance=eTJ_RichText_strategy)
def test_etj_richtext_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Precedes_strategy)
@settings(max_examples=50)
def test_precedes_instantiation(instance):
    assert isinstance(instance, Precedes)

@given(instance=eTJ_ColumnAttribute_strategy)
@settings(max_examples=50)
def test_etj_columnattribute_instantiation(instance):
    assert isinstance(instance, eTJ_ColumnAttribute)

@given(instance=eTJ_WorkHours_strategy)
@settings(max_examples=50)
def test_etj_workhours_instantiation(instance):
    assert isinstance(instance, eTJ_WorkHours)



@given(instance=eTJ_WorkHours_strategy)
def test_etj_workhours_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=eTJ_WorkHours_strategy)
def test_etj_workhours_stop_setter(instance):
    original = instance.stop
    instance.stop = original
    assert instance.stop == original

@given(instance=eTJ_Weekdays_strategy)
@settings(max_examples=50)
def test_etj_weekdays_instantiation(instance):
    assert isinstance(instance, eTJ_Weekdays)



@given(instance=eTJ_Weekdays_strategy)
def test_etj_weekdays_first_setter(instance):
    original = instance.first
    instance.first = original
    assert instance.first == original



@given(instance=eTJ_Weekdays_strategy)
def test_etj_weekdays_last_setter(instance):
    original = instance.last
    instance.last = original
    assert instance.last == original

@given(instance=WeeklyMin_strategy)
@settings(max_examples=50)
def test_weeklymin_instantiation(instance):
    assert isinstance(instance, WeeklyMin)

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

@given(instance=eTJ_Limit_strategy)
@settings(max_examples=50)
def test_etj_limit_instantiation(instance):
    assert isinstance(instance, eTJ_Limit)

@given(instance=GapLength_strategy)
@settings(max_examples=50)
def test_gaplength_instantiation(instance):
    assert isinstance(instance, GapLength)

@given(instance=GapDuration_strategy)
@settings(max_examples=50)
def test_gapduration_instantiation(instance):
    assert isinstance(instance, GapDuration)

@given(instance=eTJ_TreeLevel_strategy)
@settings(max_examples=50)
def test_etj_treelevel_instantiation(instance):
    assert isinstance(instance, eTJ_TreeLevel)



@given(instance=eTJ_TreeLevel_strategy)
def test_etj_treelevel_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=eTJ_TimesheetReportAttribute_strategy)
@settings(max_examples=50)
def test_etj_timesheetreportattribute_instantiation(instance):
    assert isinstance(instance, eTJ_TimesheetReportAttribute)

@given(instance=eTJ_TimesheetAttribute_strategy)
@settings(max_examples=50)
def test_etj_timesheetattribute_instantiation(instance):
    assert isinstance(instance, eTJ_TimesheetAttribute)

@given(instance=eTJ_TaskTimesheetAttribute_strategy)
@settings(max_examples=50)
def test_etj_tasktimesheetattribute_instantiation(instance):
    assert isinstance(instance, eTJ_TaskTimesheetAttribute)

@given(instance=eTJ_TaskStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_etj_taskstatussheetattribute_instantiation(instance):
    assert isinstance(instance, eTJ_TaskStatusSheetAttribute)

@given(instance=StatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_statussheetattribute_instantiation(instance):
    assert isinstance(instance, StatusSheetAttribute)

@given(instance=AllocateResourceAttribute_strategy)
@settings(max_examples=50)
def test_allocateresourceattribute_instantiation(instance):
    assert isinstance(instance, AllocateResourceAttribute)

@given(instance=eTJ_Alternative_strategy)
@settings(max_examples=50)
def test_etj_alternative_instantiation(instance):
    assert isinstance(instance, eTJ_Alternative)

@given(instance=eTJ_Alert_strategy)
@settings(max_examples=50)
def test_etj_alert_instantiation(instance):
    assert isinstance(instance, eTJ_Alert)



@given(instance=eTJ_Alert_strategy)
def test_etj_alert_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=eTJ_NikuReportAttribute_strategy)
@settings(max_examples=50)
def test_etj_nikureportattribute_instantiation(instance):
    assert isinstance(instance, eTJ_NikuReportAttribute)

@given(instance=eTJ_NewTaskAttribute_strategy)
@settings(max_examples=50)
def test_etj_newtaskattribute_instantiation(instance):
    assert isinstance(instance, eTJ_NewTaskAttribute)

@given(instance=TimesheetAttribute_strategy)
@settings(max_examples=50)
def test_timesheetattribute_instantiation(instance):
    assert isinstance(instance, TimesheetAttribute)

@given(instance=eTJ_TaskTimesheet_strategy)
@settings(max_examples=50)
def test_etj_tasktimesheet_instantiation(instance):
    assert isinstance(instance, eTJ_TaskTimesheet)

@given(instance=eTJ_NewTask_strategy)
@settings(max_examples=50)
def test_etj_newtask_instantiation(instance):
    assert isinstance(instance, eTJ_NewTask)



@given(instance=eTJ_NewTask_strategy)
def test_etj_newtask_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=eTJ_NewTask_strategy)
def test_etj_newtask_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ExtDate_strategy)
@settings(max_examples=50)
def test_extdate_instantiation(instance):
    assert isinstance(instance, ExtDate)

@given(instance=Start_strategy)
@settings(max_examples=50)
def test_start_instantiation(instance):
    assert isinstance(instance, Start)

@given(instance=End_strategy)
@settings(max_examples=50)
def test_end_instantiation(instance):
    assert isinstance(instance, End)

@given(instance=eTJ_MacroCall_strategy)
@settings(max_examples=50)
def test_etj_macrocall_instantiation(instance):
    assert isinstance(instance, eTJ_MacroCall)



@given(instance=eTJ_MacroCall_strategy)
def test_etj_macrocall_buildin_setter(instance):
    original = instance.buildin
    instance.buildin = original
    assert instance.buildin == original

@given(instance=eTJ_EObject_strategy)
@settings(max_examples=50)
def test_etj_eobject_instantiation(instance):
    assert isinstance(instance, eTJ_EObject)

@given(instance=eTJ_TaskAttribute_strategy)
@settings(max_examples=50)
def test_etj_taskattribute_instantiation(instance):
    assert isinstance(instance, eTJ_TaskAttribute)

@given(instance=eTJ_ProjectAttribute_strategy)
@settings(max_examples=50)
def test_etj_projectattribute_instantiation(instance):
    assert isinstance(instance, eTJ_ProjectAttribute)

@given(instance=eTJ_ExportAttribute_strategy)
@settings(max_examples=50)
def test_etj_exportattribute_instantiation(instance):
    assert isinstance(instance, eTJ_ExportAttribute)

@given(instance=eTJ_IcalReportAttribute_strategy)
@settings(max_examples=50)
def test_etj_icalreportattribute_instantiation(instance):
    assert isinstance(instance, eTJ_IcalReportAttribute)

@given(instance=eTJ_ReportAttribute_strategy)
@settings(max_examples=50)
def test_etj_reportattribute_instantiation(instance):
    assert isinstance(instance, eTJ_ReportAttribute)

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

@given(instance=eTJ_Report_strategy)
@settings(max_examples=50)
def test_etj_report_instantiation(instance):
    assert isinstance(instance, eTJ_Report)



@given(instance=eTJ_Report_strategy)
def test_etj_report_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=eTJ_Report_strategy)
def test_etj_report_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ_AccountAttribute_strategy)
@settings(max_examples=50)
def test_etj_accountattribute_instantiation(instance):
    assert isinstance(instance, eTJ_AccountAttribute)

@given(instance=AccountAttribute_strategy)
@settings(max_examples=50)
def test_accountattribute_instantiation(instance):
    assert isinstance(instance, AccountAttribute)

@given(instance=eTJ_Interval2_strategy)
@settings(max_examples=50)
def test_etj_interval2_instantiation(instance):
    assert isinstance(instance, eTJ_Interval2)

@given(instance=ReportAttribute_strategy)
@settings(max_examples=50)
def test_reportattribute_instantiation(instance):
    assert isinstance(instance, ReportAttribute)

@given(instance=eTJ_TaskRoot_strategy)
@settings(max_examples=50)
def test_etj_taskroot_instantiation(instance):
    assert isinstance(instance, eTJ_TaskRoot)

@given(instance=eTJ_AccountRoot_strategy)
@settings(max_examples=50)
def test_etj_accountroot_instantiation(instance):
    assert isinstance(instance, eTJ_AccountRoot)

@given(instance=IncludePropertiesAttribute_strategy)
@settings(max_examples=50)
def test_includepropertiesattribute_instantiation(instance):
    assert isinstance(instance, IncludePropertiesAttribute)

@given(instance=eTJ_TaskPrefix_strategy)
@settings(max_examples=50)
def test_etj_taskprefix_instantiation(instance):
    assert isinstance(instance, eTJ_TaskPrefix)

@given(instance=eTJ_AccountPrefix_strategy)
@settings(max_examples=50)
def test_etj_accountprefix_instantiation(instance):
    assert isinstance(instance, eTJ_AccountPrefix)

@given(instance=eTJ_Property_strategy)
@settings(max_examples=50)
def test_etj_property_instantiation(instance):
    assert isinstance(instance, eTJ_Property)

@given(instance=eTJ_Project_strategy)
@settings(max_examples=50)
def test_etj_project_instantiation(instance):
    assert isinstance(instance, eTJ_Project)



@given(instance=eTJ_Project_strategy)
def test_etj_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=eTJ_Project_strategy)
def test_etj_project_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=eTJ_Project_strategy)
def test_etj_project_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ_Global_strategy)
@settings(max_examples=50)
def test_etj_global_instantiation(instance):
    assert isinstance(instance, eTJ_Global)

@given(instance=eTJ_Interval3_strategy)
@settings(max_examples=50)
def test_etj_interval3_instantiation(instance):
    assert isinstance(instance, eTJ_Interval3)

@given(instance=eTJ_LeaveDetails_strategy)
@settings(max_examples=50)
def test_etj_leavedetails_instantiation(instance):
    assert isinstance(instance, eTJ_LeaveDetails)



@given(instance=eTJ_LeaveDetails_strategy)
def test_etj_leavedetails_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=eTJ_LeaveDetails_strategy)
def test_etj_leavedetails_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ResourceAttribute_strategy)
@settings(max_examples=50)
def test_resourceattribute_instantiation(instance):
    assert isinstance(instance, ResourceAttribute)

@given(instance=eTJ_Warn_strategy)
@settings(max_examples=50)
def test_etj_warn_instantiation(instance):
    assert isinstance(instance, eTJ_Warn)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=eTJ_IcalReport_strategy)
@settings(max_examples=50)
def test_etj_icalreport_instantiation(instance):
    assert isinstance(instance, eTJ_IcalReport)



@given(instance=eTJ_IcalReport_strategy)
def test_etj_icalreport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=eTJ_Macro_strategy)
@settings(max_examples=50)
def test_etj_macro_instantiation(instance):
    assert isinstance(instance, eTJ_Macro)



@given(instance=eTJ_Macro_strategy)
def test_etj_macro_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=eTJ_Macro_strategy)
def test_etj_macro_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ_NikuReport_strategy)
@settings(max_examples=50)
def test_etj_nikureport_instantiation(instance):
    assert isinstance(instance, eTJ_NikuReport)



@given(instance=eTJ_NikuReport_strategy)
def test_etj_nikureport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=eTJ_TextReport_strategy)
@settings(max_examples=50)
def test_etj_textreport_instantiation(instance):
    assert isinstance(instance, eTJ_TextReport)

@given(instance=eTJ_TimesheetReport_strategy)
@settings(max_examples=50)
def test_etj_timesheetreport_instantiation(instance):
    assert isinstance(instance, eTJ_TimesheetReport)



@given(instance=eTJ_TimesheetReport_strategy)
def test_etj_timesheetreport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=eTJ_Account_strategy)
@settings(max_examples=50)
def test_etj_account_instantiation(instance):
    assert isinstance(instance, eTJ_Account)



@given(instance=eTJ_Account_strategy)
def test_etj_account_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=eTJ_Account_strategy)
def test_etj_account_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ_Timesheet_strategy)
@settings(max_examples=50)
def test_etj_timesheet_instantiation(instance):
    assert isinstance(instance, eTJ_Timesheet)

@given(instance=eTJ_TaskReport_strategy)
@settings(max_examples=50)
def test_etj_taskreport_instantiation(instance):
    assert isinstance(instance, eTJ_TaskReport)

@given(instance=eTJ_Task_strategy)
@settings(max_examples=50)
def test_etj_task_instantiation(instance):
    assert isinstance(instance, eTJ_Task)



@given(instance=eTJ_Task_strategy)
def test_etj_task_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=eTJ_Task_strategy)
def test_etj_task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ_AccountReport_strategy)
@settings(max_examples=50)
def test_etj_accountreport_instantiation(instance):
    assert isinstance(instance, eTJ_AccountReport)

@given(instance=eTJ_Export_strategy)
@settings(max_examples=50)
def test_etj_export_instantiation(instance):
    assert isinstance(instance, eTJ_Export)



@given(instance=eTJ_Export_strategy)
def test_etj_export_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original



@given(instance=eTJ_Export_strategy)
def test_etj_export_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ_Leaves_strategy)
@settings(max_examples=50)
def test_etj_leaves_instantiation(instance):
    assert isinstance(instance, eTJ_Leaves)

@given(instance=eTJ_SupplementAccount_strategy)
@settings(max_examples=50)
def test_etj_supplementaccount_instantiation(instance):
    assert isinstance(instance, eTJ_SupplementAccount)

@given(instance=eTJ_StatusSheetReportAttribute_strategy)
@settings(max_examples=50)
def test_etj_statussheetreportattribute_instantiation(instance):
    assert isinstance(instance, eTJ_StatusSheetReportAttribute)

@given(instance=eTJ_StatusSheetReport_strategy)
@settings(max_examples=50)
def test_etj_statussheetreport_instantiation(instance):
    assert isinstance(instance, eTJ_StatusSheetReport)



@given(instance=eTJ_StatusSheetReport_strategy)
def test_etj_statussheetreport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=eTJ_StatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_etj_statussheetattribute_instantiation(instance):
    assert isinstance(instance, eTJ_StatusSheetAttribute)

@given(instance=eTJ_StatusSheet_strategy)
@settings(max_examples=50)
def test_etj_statussheet_instantiation(instance):
    assert isinstance(instance, eTJ_StatusSheet)

@given(instance=eTJ_TagFile_strategy)
@settings(max_examples=50)
def test_etj_tagfile_instantiation(instance):
    assert isinstance(instance, eTJ_TagFile)



@given(instance=eTJ_TagFile_strategy)
def test_etj_tagfile_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=eTJ_TagFile_strategy)
def test_etj_tagfile_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=eTJ_SupplementTask_strategy)
@settings(max_examples=50)
def test_etj_supplementtask_instantiation(instance):
    assert isinstance(instance, eTJ_SupplementTask)

@given(instance=eTJ_SupplementResource_strategy)
@settings(max_examples=50)
def test_etj_supplementresource_instantiation(instance):
    assert isinstance(instance, eTJ_SupplementResource)

@given(instance=eTJ_SupplementReport_strategy)
@settings(max_examples=50)
def test_etj_supplementreport_instantiation(instance):
    assert isinstance(instance, eTJ_SupplementReport)

@given(instance=eTJ_SortJournalEntries_strategy)
@settings(max_examples=50)
def test_etj_sortjournalentries_instantiation(instance):
    assert isinstance(instance, eTJ_SortJournalEntries)

@given(instance=eTJ_SortAccounts_strategy)
@settings(max_examples=50)
def test_etj_sortaccounts_instantiation(instance):
    assert isinstance(instance, eTJ_SortAccounts)

@given(instance=eTJ_Criterion_strategy)
@settings(max_examples=50)
def test_etj_criterion_instantiation(instance):
    assert isinstance(instance, eTJ_Criterion)



@given(instance=eTJ_Criterion_strategy)
def test_etj_criterion_columnId_setter(instance):
    original = instance.columnId
    instance.columnId = original
    assert instance.columnId == original



@given(instance=eTJ_Criterion_strategy)
def test_etj_criterion_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

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

@given(instance=eTJ_Sort_strategy)
@settings(max_examples=50)
def test_etj_sort_instantiation(instance):
    assert isinstance(instance, eTJ_Sort)



@given(instance=eTJ_Sort_strategy)
def test_etj_sort_tree_setter(instance):
    original = instance.tree
    instance.tree = original
    assert instance.tree == original

@given(instance=eTJ_ShiftsTask_strategy)
@settings(max_examples=50)
def test_etj_shiftstask_instantiation(instance):
    assert isinstance(instance, eTJ_ShiftsTask)

@given(instance=eTJ_ShiftsResource_strategy)
@settings(max_examples=50)
def test_etj_shiftsresource_instantiation(instance):
    assert isinstance(instance, eTJ_ShiftsResource)

@given(instance=eTJ_StatusTimesheetAttribute_strategy)
@settings(max_examples=50)
def test_etj_statustimesheetattribute_instantiation(instance):
    assert isinstance(instance, eTJ_StatusTimesheetAttribute)

@given(instance=eTJ_StatusStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_etj_statusstatussheetattribute_instantiation(instance):
    assert isinstance(instance, eTJ_StatusStatusSheetAttribute)

@given(instance=TaskStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_taskstatussheetattribute_instantiation(instance):
    assert isinstance(instance, TaskStatusSheetAttribute)

@given(instance=eTJ_TaskStatusSheet_strategy)
@settings(max_examples=50)
def test_etj_taskstatussheet_instantiation(instance):
    assert isinstance(instance, eTJ_TaskStatusSheet)

@given(instance=eTJ_StatusStatusSheet_strategy)
@settings(max_examples=50)
def test_etj_statusstatussheet_instantiation(instance):
    assert isinstance(instance, eTJ_StatusStatusSheet)



@given(instance=eTJ_StatusStatusSheet_strategy)
def test_etj_statusstatussheet_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=eTJ_StatusStatusSheet_strategy)
def test_etj_statusstatussheet_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=eTJ_Shift_strategy)
@settings(max_examples=50)
def test_etj_shift_instantiation(instance):
    assert isinstance(instance, eTJ_Shift)



@given(instance=eTJ_Shift_strategy)
def test_etj_shift_replace_setter(instance):
    original = instance.replace
    instance.replace = original
    assert instance.replace == original



@given(instance=eTJ_Shift_strategy)
def test_etj_shift_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=eTJ_Shift_strategy)
def test_etj_shift_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=eTJ_Shift_strategy)
def test_etj_shift_timezone_setter(instance):
    original = instance.timezone
    instance.timezone = original
    assert instance.timezone == original

@given(instance=eTJ_SelfContained_strategy)
@settings(max_examples=50)
def test_etj_selfcontained_instantiation(instance):
    assert isinstance(instance, eTJ_SelfContained)



@given(instance=eTJ_SelfContained_strategy)
def test_etj_selfcontained_selfcontained_setter(instance):
    original = instance.selfcontained
    instance.selfcontained = original
    assert instance.selfcontained == original

@given(instance=eTJ_Select_strategy)
@settings(max_examples=50)
def test_etj_select_instantiation(instance):
    assert isinstance(instance, eTJ_Select)



@given(instance=eTJ_Select_strategy)
def test_etj_select_argument_setter(instance):
    original = instance.argument
    instance.argument = original
    assert instance.argument == original

@given(instance=eTJ_Scheduling_strategy)
@settings(max_examples=50)
def test_etj_scheduling_instantiation(instance):
    assert isinstance(instance, eTJ_Scheduling)



@given(instance=eTJ_Scheduling_strategy)
def test_etj_scheduling_scheduling_setter(instance):
    original = instance.scheduling
    instance.scheduling = original
    assert instance.scheduling == original

@given(instance=eTJ_Scheduled_strategy)
@settings(max_examples=50)
def test_etj_scheduled_instantiation(instance):
    assert isinstance(instance, eTJ_Scheduled)



@given(instance=eTJ_Scheduled_strategy)
def test_etj_scheduled_scheduled_setter(instance):
    original = instance.scheduled
    instance.scheduled = original
    assert instance.scheduled == original

@given(instance=eTJ_ShiftsAllocate_strategy)
@settings(max_examples=50)
def test_etj_shiftsallocate_instantiation(instance):
    assert isinstance(instance, eTJ_ShiftsAllocate)

@given(instance=eTJ_ShiftsLimit_strategy)
@settings(max_examples=50)
def test_etj_shiftslimit_instantiation(instance):
    assert isinstance(instance, eTJ_ShiftsLimit)

@given(instance=ShiftsTask_strategy)
@settings(max_examples=50)
def test_shiftstask_instantiation(instance):
    assert isinstance(instance, ShiftsTask)

@given(instance=ShiftsResource_strategy)
@settings(max_examples=50)
def test_shiftsresource_instantiation(instance):
    assert isinstance(instance, ShiftsResource)

@given(instance=eTJ_Shifts_strategy)
@settings(max_examples=50)
def test_etj_shifts_instantiation(instance):
    assert isinstance(instance, eTJ_Shifts)

@given(instance=eTJ_ShiftTimesheet_strategy)
@settings(max_examples=50)
def test_etj_shifttimesheet_instantiation(instance):
    assert isinstance(instance, eTJ_ShiftTimesheet)

@given(instance=eTJ_Vacation_strategy)
@settings(max_examples=50)
def test_etj_vacation_instantiation(instance):
    assert isinstance(instance, eTJ_Vacation)



@given(instance=eTJ_Vacation_strategy)
def test_etj_vacation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ_RollupAccount_strategy)
@settings(max_examples=50)
def test_etj_rollupaccount_instantiation(instance):
    assert isinstance(instance, eTJ_RollupAccount)

@given(instance=eTJ_Right_strategy)
@settings(max_examples=50)
def test_etj_right_instantiation(instance):
    assert isinstance(instance, eTJ_Right)

@given(instance=eTJ_Responsible_strategy)
@settings(max_examples=50)
def test_etj_responsible_instantiation(instance):
    assert isinstance(instance, eTJ_Responsible)

@given(instance=eTJ_ResourceRoot_strategy)
@settings(max_examples=50)
def test_etj_resourceroot_instantiation(instance):
    assert isinstance(instance, eTJ_ResourceRoot)

@given(instance=eTJ_ResourceReport_strategy)
@settings(max_examples=50)
def test_etj_resourcereport_instantiation(instance):
    assert isinstance(instance, eTJ_ResourceReport)

@given(instance=eTJ_PurgeTask_strategy)
@settings(max_examples=50)
def test_etj_purgetask_instantiation(instance):
    assert isinstance(instance, eTJ_PurgeTask)



@given(instance=eTJ_PurgeTask_strategy)
def test_etj_purgetask_listAttribute_setter(instance):
    original = instance.listAttribute
    instance.listAttribute = original
    assert instance.listAttribute == original

@given(instance=eTJ_PurgeResource_strategy)
@settings(max_examples=50)
def test_etj_purgeresource_instantiation(instance):
    assert isinstance(instance, eTJ_PurgeResource)



@given(instance=eTJ_PurgeResource_strategy)
def test_etj_purgeresource_listAttribute_setter(instance):
    original = instance.listAttribute
    instance.listAttribute = original
    assert instance.listAttribute == original

@given(instance=eTJ_ResourcePrefix_strategy)
@settings(max_examples=50)
def test_etj_resourceprefix_instantiation(instance):
    assert isinstance(instance, eTJ_ResourcePrefix)

@given(instance=eTJ_ReportPrefix_strategy)
@settings(max_examples=50)
def test_etj_reportprefix_instantiation(instance):
    assert isinstance(instance, eTJ_ReportPrefix)

@given(instance=eTJ_Rate_strategy)
@settings(max_examples=50)
def test_etj_rate_instantiation(instance):
    assert isinstance(instance, eTJ_Rate)



@given(instance=eTJ_Rate_strategy)
def test_etj_rate_rate_setter(instance):
    original = instance.rate
    instance.rate = original
    assert instance.rate == original

@given(instance=eTJ_Note_strategy)
@settings(max_examples=50)
def test_etj_note_instantiation(instance):
    assert isinstance(instance, eTJ_Note)



@given(instance=eTJ_Note_strategy)
def test_etj_note_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=eTJ_PurgeReport_strategy)
@settings(max_examples=50)
def test_etj_purgereport_instantiation(instance):
    assert isinstance(instance, eTJ_PurgeReport)



@given(instance=eTJ_PurgeReport_strategy)
def test_etj_purgereport_listAttribute_setter(instance):
    original = instance.listAttribute
    instance.listAttribute = original
    assert instance.listAttribute == original

@given(instance=eTJ_Prolog_strategy)
@settings(max_examples=50)
def test_etj_prolog_instantiation(instance):
    assert isinstance(instance, eTJ_Prolog)

@given(instance=eTJ_ProjectIds_strategy)
@settings(max_examples=50)
def test_etj_projectids_instantiation(instance):
    assert isinstance(instance, eTJ_ProjectIds)



@given(instance=eTJ_ProjectIds_strategy)
def test_etj_projectids_ids_setter(instance):
    original = instance.ids
    instance.ids = original
    assert instance.ids == original

@given(instance=eTJ_ProjectId_strategy)
@settings(max_examples=50)
def test_etj_projectid_instantiation(instance):
    assert isinstance(instance, eTJ_ProjectId)



@given(instance=eTJ_ProjectId_strategy)
def test_etj_projectid_projectId_setter(instance):
    original = instance.projectId
    instance.projectId = original
    assert instance.projectId == original

@given(instance=eTJ_Precedes_strategy)
@settings(max_examples=50)
def test_etj_precedes_instantiation(instance):
    assert isinstance(instance, eTJ_Precedes)

@given(instance=eTJ_Persistent_strategy)
@settings(max_examples=50)
def test_etj_persistent_instantiation(instance):
    assert isinstance(instance, eTJ_Persistent)



@given(instance=eTJ_Persistent_strategy)
def test_etj_persistent_persistent_setter(instance):
    original = instance.persistent
    instance.persistent = original
    assert instance.persistent == original

@given(instance=eTJ_LoadUnit_strategy)
@settings(max_examples=50)
def test_etj_loadunit_instantiation(instance):
    assert isinstance(instance, eTJ_LoadUnit)



@given(instance=eTJ_LoadUnit_strategy)
def test_etj_loadunit_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=eTJ_LimitsAttribute_strategy)
@settings(max_examples=50)
def test_etj_limitsattribute_instantiation(instance):
    assert isinstance(instance, eTJ_LimitsAttribute)

@given(instance=eTJ_Limits_strategy)
@settings(max_examples=50)
def test_etj_limits_instantiation(instance):
    assert isinstance(instance, eTJ_Limits)

@given(instance=eTJ_MinStart_strategy)
@settings(max_examples=50)
def test_etj_minstart_instantiation(instance):
    assert isinstance(instance, eTJ_MinStart)

@given(instance=eTJ_MinEnd_strategy)
@settings(max_examples=50)
def test_etj_minend_instantiation(instance):
    assert isinstance(instance, eTJ_MinEnd)

@given(instance=eTJ_Milestone_strategy)
@settings(max_examples=50)
def test_etj_milestone_instantiation(instance):
    assert isinstance(instance, eTJ_Milestone)



@given(instance=eTJ_Milestone_strategy)
def test_etj_milestone_milestone_setter(instance):
    original = instance.milestone
    instance.milestone = original
    assert instance.milestone == original

@given(instance=eTJ_MaxStart_strategy)
@settings(max_examples=50)
def test_etj_maxstart_instantiation(instance):
    assert isinstance(instance, eTJ_MaxStart)

@given(instance=eTJ_MaxEnd_strategy)
@settings(max_examples=50)
def test_etj_maxend_instantiation(instance):
    assert isinstance(instance, eTJ_MaxEnd)

@given(instance=eTJ_Mandatory_strategy)
@settings(max_examples=50)
def test_etj_mandatory_instantiation(instance):
    assert isinstance(instance, eTJ_Mandatory)



@given(instance=eTJ_Mandatory_strategy)
def test_etj_mandatory_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=eTJ_Managers_strategy)
@settings(max_examples=50)
def test_etj_managers_instantiation(instance):
    assert isinstance(instance, eTJ_Managers)

@given(instance=eTJ_JournalAttributes_strategy)
@settings(max_examples=50)
def test_etj_journalattributes_instantiation(instance):
    assert isinstance(instance, eTJ_JournalAttributes)



@given(instance=eTJ_JournalAttributes_strategy)
def test_etj_journalattributes_args_setter(instance):
    original = instance.args
    instance.args = original
    assert instance.args == original

@given(instance=eTJ_Length_strategy)
@settings(max_examples=50)
def test_etj_length_instantiation(instance):
    assert isinstance(instance, eTJ_Length)

@given(instance=eTJ_Left_strategy)
@settings(max_examples=50)
def test_etj_left_instantiation(instance):
    assert isinstance(instance, eTJ_Left)

@given(instance=eTJ_JournalMode_strategy)
@settings(max_examples=50)
def test_etj_journalmode_instantiation(instance):
    assert isinstance(instance, eTJ_JournalMode)



@given(instance=eTJ_JournalMode_strategy)
def test_etj_journalmode_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=NavigatorAttribute_strategy)
@settings(max_examples=50)
def test_navigatorattribute_instantiation(instance):
    assert isinstance(instance, NavigatorAttribute)

@given(instance=eTJ_HideReport_strategy)
@settings(max_examples=50)
def test_etj_hidereport_instantiation(instance):
    assert isinstance(instance, eTJ_HideReport)

@given(instance=eTJ_Interval1_strategy)
@settings(max_examples=50)
def test_etj_interval1_instantiation(instance):
    assert isinstance(instance, eTJ_Interval1)

@given(instance=eTJ_IncludePropertiesAttribute_strategy)
@settings(max_examples=50)
def test_etj_includepropertiesattribute_instantiation(instance):
    assert isinstance(instance, eTJ_IncludePropertiesAttribute)

@given(instance=eTJ_IncludeProperties_strategy)
@settings(max_examples=50)
def test_etj_includeproperties_instantiation(instance):
    assert isinstance(instance, eTJ_IncludeProperties)



@given(instance=eTJ_IncludeProperties_strategy)
def test_etj_includeproperties_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=eTJ_Footer_strategy)
@settings(max_examples=50)
def test_etj_footer_instantiation(instance):
    assert isinstance(instance, eTJ_Footer)

@given(instance=eTJ_Fail_strategy)
@settings(max_examples=50)
def test_etj_fail_instantiation(instance):
    assert isinstance(instance, eTJ_Fail)

@given(instance=eTJ_ExtendedTaskAttribute_strategy)
@settings(max_examples=50)
def test_etj_extendedtaskattribute_instantiation(instance):
    assert isinstance(instance, eTJ_ExtendedTaskAttribute)



@given(instance=eTJ_ExtendedTaskAttribute_strategy)
def test_etj_extendedtaskattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ_HideAccount_strategy)
@settings(max_examples=50)
def test_etj_hideaccount_instantiation(instance):
    assert isinstance(instance, eTJ_HideAccount)



@given(instance=eTJ_HideAccount_strategy)
def test_etj_hideaccount_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=eTJ_Header_strategy)
@settings(max_examples=50)
def test_etj_header_instantiation(instance):
    assert isinstance(instance, eTJ_Header)

@given(instance=eTJ_GapLength_strategy)
@settings(max_examples=50)
def test_etj_gaplength_instantiation(instance):
    assert isinstance(instance, eTJ_GapLength)

@given(instance=eTJ_GapDuration_strategy)
@settings(max_examples=50)
def test_etj_gapduration_instantiation(instance):
    assert isinstance(instance, eTJ_GapDuration)

@given(instance=eTJ_Function_strategy)
@settings(max_examples=50)
def test_etj_function_instantiation(instance):
    assert isinstance(instance, eTJ_Function)



@given(instance=eTJ_Function_strategy)
def test_etj_function_parentId_setter(instance):
    original = instance.parentId
    instance.parentId = original
    assert instance.parentId == original



@given(instance=eTJ_Function_strategy)
def test_etj_function_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original



@given(instance=eTJ_Function_strategy)
def test_etj_function_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=NewTaskAttribute_strategy)
@settings(max_examples=50)
def test_newtaskattribute_instantiation(instance):
    assert isinstance(instance, NewTaskAttribute)

@given(instance=IcalReportAttribute_strategy)
@settings(max_examples=50)
def test_icalreportattribute_instantiation(instance):
    assert isinstance(instance, IcalReportAttribute)

@given(instance=eTJ_HideJournalEntry_strategy)
@settings(max_examples=50)
def test_etj_hidejournalentry_instantiation(instance):
    assert isinstance(instance, eTJ_HideJournalEntry)



@given(instance=eTJ_HideJournalEntry_strategy)
def test_etj_hidejournalentry_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=eTJ_ScenarioIcal_strategy)
@settings(max_examples=50)
def test_etj_scenarioical_instantiation(instance):
    assert isinstance(instance, eTJ_ScenarioIcal)

@given(instance=eTJ_Email_strategy)
@settings(max_examples=50)
def test_etj_email_instantiation(instance):
    assert isinstance(instance, eTJ_Email)



@given(instance=eTJ_Email_strategy)
def test_etj_email_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=eTJ_Effort_strategy)
@settings(max_examples=50)
def test_etj_effort_instantiation(instance):
    assert isinstance(instance, eTJ_Effort)

@given(instance=eTJ_Efficiency_strategy)
@settings(max_examples=50)
def test_etj_efficiency_instantiation(instance):
    assert isinstance(instance, eTJ_Efficiency)



@given(instance=eTJ_Efficiency_strategy)
def test_etj_efficiency_efficiency_setter(instance):
    original = instance.efficiency
    instance.efficiency = original
    assert instance.efficiency == original

@given(instance=eTJ_DurationQuantity_strategy)
@settings(max_examples=50)
def test_etj_durationquantity_instantiation(instance):
    assert isinstance(instance, eTJ_DurationQuantity)



@given(instance=eTJ_DurationQuantity_strategy)
def test_etj_durationquantity_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=eTJ_DurationQuantity_strategy)
def test_etj_durationquantity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ_Duration_strategy)
@settings(max_examples=50)
def test_etj_duration_instantiation(instance):
    assert isinstance(instance, eTJ_Duration)

@given(instance=StatusTimesheetAttribute_strategy)
@settings(max_examples=50)
def test_statustimesheetattribute_instantiation(instance):
    assert isinstance(instance, StatusTimesheetAttribute)

@given(instance=eTJ_TaskDependency_strategy)
@settings(max_examples=50)
def test_etj_taskdependency_instantiation(instance):
    assert isinstance(instance, eTJ_TaskDependency)



@given(instance=eTJ_TaskDependency_strategy)
def test_etj_taskdependency_policy_setter(instance):
    original = instance.policy
    instance.policy = original
    assert instance.policy == original

@given(instance=eTJ_Depends_strategy)
@settings(max_examples=50)
def test_etj_depends_instantiation(instance):
    assert isinstance(instance, eTJ_Depends)

@given(instance=eTJ_ExtendedResourceAttribute_strategy)
@settings(max_examples=50)
def test_etj_extendedresourceattribute_instantiation(instance):
    assert isinstance(instance, eTJ_ExtendedResourceAttribute)



@given(instance=eTJ_ExtendedResourceAttribute_strategy)
def test_etj_extendedresourceattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ_Extend_strategy)
@settings(max_examples=50)
def test_etj_extend_instantiation(instance):
    assert isinstance(instance, eTJ_Extend)



@given(instance=eTJ_Extend_strategy)
def test_etj_extend_inherit_setter(instance):
    original = instance.inherit
    instance.inherit = original
    assert instance.inherit == original



@given(instance=eTJ_Extend_strategy)
def test_etj_extend_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=eTJ_Extend_strategy)
def test_etj_extend_scenariospecific_setter(instance):
    original = instance.scenariospecific
    instance.scenariospecific = original
    assert instance.scenariospecific == original



@given(instance=eTJ_Extend_strategy)
def test_etj_extend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ_Epilog_strategy)
@settings(max_examples=50)
def test_etj_epilog_instantiation(instance):
    assert isinstance(instance, eTJ_Epilog)

@given(instance=eTJ_EndCredit_strategy)
@settings(max_examples=50)
def test_etj_endcredit_instantiation(instance):
    assert isinstance(instance, eTJ_EndCredit)



@given(instance=eTJ_EndCredit_strategy)
def test_etj_endcredit_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original

@given(instance=TimesheetReportAttribute_strategy)
@settings(max_examples=50)
def test_timesheetreportattribute_instantiation(instance):
    assert isinstance(instance, TimesheetReportAttribute)

@given(instance=TaskTimesheetAttribute_strategy)
@settings(max_examples=50)
def test_tasktimesheetattribute_instantiation(instance):
    assert isinstance(instance, TaskTimesheetAttribute)

@given(instance=eTJ_Remaining_strategy)
@settings(max_examples=50)
def test_etj_remaining_instantiation(instance):
    assert isinstance(instance, eTJ_Remaining)

@given(instance=eTJ_StatusTimesheet_strategy)
@settings(max_examples=50)
def test_etj_statustimesheet_instantiation(instance):
    assert isinstance(instance, eTJ_StatusTimesheet)



@given(instance=eTJ_StatusTimesheet_strategy)
def test_etj_statustimesheet_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=eTJ_StatusTimesheet_strategy)
def test_etj_statustimesheet_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=eTJ_Priority_strategy)
@settings(max_examples=50)
def test_etj_priority_instantiation(instance):
    assert isinstance(instance, eTJ_Priority)



@given(instance=eTJ_Priority_strategy)
def test_etj_priority_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=eTJ_Work_strategy)
@settings(max_examples=50)
def test_etj_work_instantiation(instance):
    assert isinstance(instance, eTJ_Work)



@given(instance=eTJ_Work_strategy)
def test_etj_work_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=eTJ_Work_strategy)
def test_etj_work_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=StatusSheetReportAttribute_strategy)
@settings(max_examples=50)
def test_statussheetreportattribute_instantiation(instance):
    assert isinstance(instance, StatusSheetReportAttribute)

@given(instance=eTJ_SortTasks_strategy)
@settings(max_examples=50)
def test_etj_sorttasks_instantiation(instance):
    assert isinstance(instance, eTJ_SortTasks)

@given(instance=eTJ_SortResources_strategy)
@settings(max_examples=50)
def test_etj_sortresources_instantiation(instance):
    assert isinstance(instance, eTJ_SortResources)

@given(instance=NikuReportAttribute_strategy)
@settings(max_examples=50)
def test_nikureportattribute_instantiation(instance):
    assert isinstance(instance, NikuReportAttribute)

@given(instance=eTJ_Formats_strategy)
@settings(max_examples=50)
def test_etj_formats_instantiation(instance):
    assert isinstance(instance, eTJ_Formats)



@given(instance=eTJ_Formats_strategy)
def test_etj_formats_formats_setter(instance):
    original = instance.formats
    instance.formats = original
    assert instance.formats == original

@given(instance=eTJ_Headline_strategy)
@settings(max_examples=50)
def test_etj_headline_instantiation(instance):
    assert isinstance(instance, eTJ_Headline)

@given(instance=eTJ_Timeoff_strategy)
@settings(max_examples=50)
def test_etj_timeoff_instantiation(instance):
    assert isinstance(instance, eTJ_Timeoff)



@given(instance=eTJ_Timeoff_strategy)
def test_etj_timeoff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=eTJ_Timeoff_strategy)
def test_etj_timeoff_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ_AccountShare_strategy)
@settings(max_examples=50)
def test_etj_accountshare_instantiation(instance):
    assert isinstance(instance, eTJ_AccountShare)



@given(instance=eTJ_AccountShare_strategy)
def test_etj_accountshare_share_setter(instance):
    original = instance.share
    instance.share = original
    assert instance.share == original

@given(instance=eTJ_ChargeSet_strategy)
@settings(max_examples=50)
def test_etj_chargeset_instantiation(instance):
    assert isinstance(instance, eTJ_ChargeSet)

@given(instance=eTJ_Charge_strategy)
@settings(max_examples=50)
def test_etj_charge_instantiation(instance):
    assert isinstance(instance, eTJ_Charge)



@given(instance=eTJ_Charge_strategy)
def test_etj_charge_applies_setter(instance):
    original = instance.applies
    instance.applies = original
    assert instance.applies == original



@given(instance=eTJ_Charge_strategy)
def test_etj_charge_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=eTJ_Center_strategy)
@settings(max_examples=50)
def test_etj_center_instantiation(instance):
    assert isinstance(instance, eTJ_Center)

@given(instance=eTJ_RGB_strategy)
@settings(max_examples=50)
def test_etj_rgb_instantiation(instance):
    assert isinstance(instance, eTJ_RGB)



@given(instance=eTJ_RGB_strategy)
def test_etj_rgb_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ_LogicalExpression_strategy)
@settings(max_examples=50)
def test_etj_logicalexpression_instantiation(instance):
    assert isinstance(instance, eTJ_LogicalExpression)



@given(instance=eTJ_LogicalExpression_strategy)
def test_etj_logicalexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ColumnAttribute_strategy)
@settings(max_examples=50)
def test_columnattribute_instantiation(instance):
    assert isinstance(instance, ColumnAttribute)

@given(instance=eTJ_FontColor_strategy)
@settings(max_examples=50)
def test_etj_fontcolor_instantiation(instance):
    assert isinstance(instance, eTJ_FontColor)



@given(instance=eTJ_FontColor_strategy)
def test_etj_fontcolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=eTJ_CellText_strategy)
@settings(max_examples=50)
def test_etj_celltext_instantiation(instance):
    assert isinstance(instance, eTJ_CellText)



@given(instance=eTJ_CellText_strategy)
def test_etj_celltext_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=eTJ_HAlign_strategy)
@settings(max_examples=50)
def test_etj_halign_instantiation(instance):
    assert isinstance(instance, eTJ_HAlign)



@given(instance=eTJ_HAlign_strategy)
def test_etj_halign_justification_setter(instance):
    original = instance.justification
    instance.justification = original
    assert instance.justification == original

@given(instance=eTJ_Scale_strategy)
@settings(max_examples=50)
def test_etj_scale_instantiation(instance):
    assert isinstance(instance, eTJ_Scale)



@given(instance=eTJ_Scale_strategy)
def test_etj_scale_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=eTJ_Title_strategy)
@settings(max_examples=50)
def test_etj_title_instantiation(instance):
    assert isinstance(instance, eTJ_Title)



@given(instance=eTJ_Title_strategy)
def test_etj_title_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=eTJ_ExtendedResourceAttributeColumn_strategy)
@settings(max_examples=50)
def test_etj_extendedresourceattributecolumn_instantiation(instance):
    assert isinstance(instance, eTJ_ExtendedResourceAttributeColumn)

@given(instance=eTJ_ListType_strategy)
@settings(max_examples=50)
def test_etj_listtype_instantiation(instance):
    assert isinstance(instance, eTJ_ListType)



@given(instance=eTJ_ListType_strategy)
def test_etj_listtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=eTJ_ToolTip_strategy)
@settings(max_examples=50)
def test_etj_tooltip_instantiation(instance):
    assert isinstance(instance, eTJ_ToolTip)



@given(instance=eTJ_ToolTip_strategy)
def test_etj_tooltip_tip_setter(instance):
    original = instance.tip
    instance.tip = original
    assert instance.tip == original

@given(instance=eTJ_ListItem_strategy)
@settings(max_examples=50)
def test_etj_listitem_instantiation(instance):
    assert isinstance(instance, eTJ_ListItem)

@given(instance=eTJ_Width_strategy)
@settings(max_examples=50)
def test_etj_width_instantiation(instance):
    assert isinstance(instance, eTJ_Width)



@given(instance=eTJ_Width_strategy)
def test_etj_width_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=eTJ_CellColor_strategy)
@settings(max_examples=50)
def test_etj_cellcolor_instantiation(instance):
    assert isinstance(instance, eTJ_CellColor)

@given(instance=eTJ_Caption_strategy)
@settings(max_examples=50)
def test_etj_caption_instantiation(instance):
    assert isinstance(instance, eTJ_Caption)

@given(instance=ExportAttribute_strategy)
@settings(max_examples=50)
def test_exportattribute_instantiation(instance):
    assert isinstance(instance, ExportAttribute)

@given(instance=eTJ_ResourceAttributes_strategy)
@settings(max_examples=50)
def test_etj_resourceattributes_instantiation(instance):
    assert isinstance(instance, eTJ_ResourceAttributes)



@given(instance=eTJ_ResourceAttributes_strategy)
def test_etj_resourceattributes_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original



@given(instance=eTJ_ResourceAttributes_strategy)
def test_etj_resourceattributes_vacation_setter(instance):
    original = instance.vacation
    instance.vacation = original
    assert instance.vacation == original



@given(instance=eTJ_ResourceAttributes_strategy)
def test_etj_resourceattributes_workingHours_setter(instance):
    original = instance.workingHours
    instance.workingHours = original
    assert instance.workingHours == original



@given(instance=eTJ_ResourceAttributes_strategy)
def test_etj_resourceattributes_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original



@given(instance=eTJ_ResourceAttributes_strategy)
def test_etj_resourceattributes_booking_setter(instance):
    original = instance.booking
    instance.booking = original
    assert instance.booking == original

@given(instance=eTJ_HideTask_strategy)
@settings(max_examples=50)
def test_etj_hidetask_instantiation(instance):
    assert isinstance(instance, eTJ_HideTask)

@given(instance=eTJ_HideResource_strategy)
@settings(max_examples=50)
def test_etj_hideresource_instantiation(instance):
    assert isinstance(instance, eTJ_HideResource)

@given(instance=eTJ_End_strategy)
@settings(max_examples=50)
def test_etj_end_instantiation(instance):
    assert isinstance(instance, eTJ_End)

@given(instance=eTJ_Scenarios_strategy)
@settings(max_examples=50)
def test_etj_scenarios_instantiation(instance):
    assert isinstance(instance, eTJ_Scenarios)

@given(instance=eTJ_TaskAttributes_strategy)
@settings(max_examples=50)
def test_etj_taskattributes_instantiation(instance):
    assert isinstance(instance, eTJ_TaskAttributes)



@given(instance=eTJ_TaskAttributes_strategy)
def test_etj_taskattributes_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original



@given(instance=eTJ_TaskAttributes_strategy)
def test_etj_taskattributes_maxstart_setter(instance):
    original = instance.maxstart
    instance.maxstart = original
    assert instance.maxstart == original



@given(instance=eTJ_TaskAttributes_strategy)
def test_etj_taskattributes_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original



@given(instance=eTJ_TaskAttributes_strategy)
def test_etj_taskattributes_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original



@given(instance=eTJ_TaskAttributes_strategy)
def test_etj_taskattributes_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original



@given(instance=eTJ_TaskAttributes_strategy)
def test_etj_taskattributes_responsible_setter(instance):
    original = instance.responsible
    instance.responsible = original
    assert instance.responsible == original



@given(instance=eTJ_TaskAttributes_strategy)
def test_etj_taskattributes_maxend_setter(instance):
    original = instance.maxend
    instance.maxend = original
    assert instance.maxend == original



@given(instance=eTJ_TaskAttributes_strategy)
def test_etj_taskattributes_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=eTJ_TaskAttributes_strategy)
def test_etj_taskattributes_minstart_setter(instance):
    original = instance.minstart
    instance.minstart = original
    assert instance.minstart == original



@given(instance=eTJ_TaskAttributes_strategy)
def test_etj_taskattributes_booking_setter(instance):
    original = instance.booking
    instance.booking = original
    assert instance.booking == original



@given(instance=eTJ_TaskAttributes_strategy)
def test_etj_taskattributes_complete_setter(instance):
    original = instance.complete
    instance.complete = original
    assert instance.complete == original



@given(instance=eTJ_TaskAttributes_strategy)
def test_etj_taskattributes_depends_setter(instance):
    original = instance.depends
    instance.depends = original
    assert instance.depends == original



@given(instance=eTJ_TaskAttributes_strategy)
def test_etj_taskattributes_minend_setter(instance):
    original = instance.minend
    instance.minend = original
    assert instance.minend == original

@given(instance=eTJ_Start_strategy)
@settings(max_examples=50)
def test_etj_start_instantiation(instance):
    assert isinstance(instance, eTJ_Start)

@given(instance=eTJ_Period_strategy)
@settings(max_examples=50)
def test_etj_period_instantiation(instance):
    assert isinstance(instance, eTJ_Period)

@given(instance=eTJ_RollupTask_strategy)
@settings(max_examples=50)
def test_etj_rolluptask_instantiation(instance):
    assert isinstance(instance, eTJ_RollupTask)

@given(instance=eTJ_RollupResource_strategy)
@settings(max_examples=50)
def test_etj_rollupresource_instantiation(instance):
    assert isinstance(instance, eTJ_RollupResource)

@given(instance=eTJ_Definitions_strategy)
@settings(max_examples=50)
def test_etj_definitions_instantiation(instance):
    assert isinstance(instance, eTJ_Definitions)



@given(instance=eTJ_Definitions_strategy)
def test_etj_definitions_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original



@given(instance=eTJ_Definitions_strategy)
def test_etj_definitions_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=LimitsAttribute_strategy)
@settings(max_examples=50)
def test_limitsattribute_instantiation(instance):
    assert isinstance(instance, LimitsAttribute)

@given(instance=eTJ_WeeklyMax_strategy)
@settings(max_examples=50)
def test_etj_weeklymax_instantiation(instance):
    assert isinstance(instance, eTJ_WeeklyMax)

@given(instance=eTJ_Minimum_strategy)
@settings(max_examples=50)
def test_etj_minimum_instantiation(instance):
    assert isinstance(instance, eTJ_Minimum)

@given(instance=eTJ_MonthlyMin_strategy)
@settings(max_examples=50)
def test_etj_monthlymin_instantiation(instance):
    assert isinstance(instance, eTJ_MonthlyMin)

@given(instance=eTJ_WeeklyMin_strategy)
@settings(max_examples=50)
def test_etj_weeklymin_instantiation(instance):
    assert isinstance(instance, eTJ_WeeklyMin)

@given(instance=eTJ_DailyMin_strategy)
@settings(max_examples=50)
def test_etj_dailymin_instantiation(instance):
    assert isinstance(instance, eTJ_DailyMin)

@given(instance=eTJ_Maximum_strategy)
@settings(max_examples=50)
def test_etj_maximum_instantiation(instance):
    assert isinstance(instance, eTJ_Maximum)

@given(instance=eTJ_MonthlyMax_strategy)
@settings(max_examples=50)
def test_etj_monthlymax_instantiation(instance):
    assert isinstance(instance, eTJ_MonthlyMax)

@given(instance=eTJ_DailyMax_strategy)
@settings(max_examples=50)
def test_etj_dailymax_instantiation(instance):
    assert isinstance(instance, eTJ_DailyMax)

@given(instance=ProjectAttribute_strategy)
@settings(max_examples=50)
def test_projectattribute_instantiation(instance):
    assert isinstance(instance, ProjectAttribute)

@given(instance=eTJ_YearlyWorkingDays_strategy)
@settings(max_examples=50)
def test_etj_yearlyworkingdays_instantiation(instance):
    assert isinstance(instance, eTJ_YearlyWorkingDays)



@given(instance=eTJ_YearlyWorkingDays_strategy)
def test_etj_yearlyworkingdays_yearlyWorkingDays_setter(instance):
    original = instance.yearlyWorkingDays
    instance.yearlyWorkingDays = original
    assert instance.yearlyWorkingDays == original

@given(instance=eTJ_ExtendResource_strategy)
@settings(max_examples=50)
def test_etj_extendresource_instantiation(instance):
    assert isinstance(instance, eTJ_ExtendResource)

@given(instance=eTJ_ShortTimeFormat_strategy)
@settings(max_examples=50)
def test_etj_shorttimeformat_instantiation(instance):
    assert isinstance(instance, eTJ_ShortTimeFormat)



@given(instance=eTJ_ShortTimeFormat_strategy)
def test_etj_shorttimeformat_shortTimeFormat_setter(instance):
    original = instance.shortTimeFormat
    instance.shortTimeFormat = original
    assert instance.shortTimeFormat == original

@given(instance=eTJ_TrackingScenario_strategy)
@settings(max_examples=50)
def test_etj_trackingscenario_instantiation(instance):
    assert isinstance(instance, eTJ_TrackingScenario)

@given(instance=eTJ_JournalEntry_strategy)
@settings(max_examples=50)
def test_etj_journalentry_instantiation(instance):
    assert isinstance(instance, eTJ_JournalEntry)



@given(instance=eTJ_JournalEntry_strategy)
def test_etj_journalentry_headline_setter(instance):
    original = instance.headline
    instance.headline = original
    assert instance.headline == original

@given(instance=eTJ_WeekStarts_strategy)
@settings(max_examples=50)
def test_etj_weekstarts_instantiation(instance):
    assert isinstance(instance, eTJ_WeekStarts)



@given(instance=eTJ_WeekStarts_strategy)
def test_etj_weekstarts_monday_setter(instance):
    original = instance.monday
    instance.monday = original
    assert instance.monday == original



@given(instance=eTJ_WeekStarts_strategy)
def test_etj_weekstarts_sunday_setter(instance):
    original = instance.sunday
    instance.sunday = original
    assert instance.sunday == original

@given(instance=eTJ_WorkingHours_strategy)
@settings(max_examples=50)
def test_etj_workinghours_instantiation(instance):
    assert isinstance(instance, eTJ_WorkingHours)



@given(instance=eTJ_WorkingHours_strategy)
def test_etj_workinghours_off_setter(instance):
    original = instance.off
    instance.off = original
    assert instance.off == original

@given(instance=eTJ_Now_strategy)
@settings(max_examples=50)
def test_etj_now_instantiation(instance):
    assert isinstance(instance, eTJ_Now)

@given(instance=eTJ_Scenario_strategy)
@settings(max_examples=50)
def test_etj_scenario_instantiation(instance):
    assert isinstance(instance, eTJ_Scenario)



@given(instance=eTJ_Scenario_strategy)
def test_etj_scenario_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=eTJ_Scenario_strategy)
def test_etj_scenario_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=eTJ_Scenario_strategy)
def test_etj_scenario_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=eTJ_Include_strategy)
@settings(max_examples=50)
def test_etj_include_instantiation(instance):
    assert isinstance(instance, eTJ_Include)



@given(instance=eTJ_Include_strategy)
def test_etj_include_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=eTJ_Timezone_strategy)
@settings(max_examples=50)
def test_etj_timezone_instantiation(instance):
    assert isinstance(instance, eTJ_Timezone)



@given(instance=eTJ_Timezone_strategy)
def test_etj_timezone_timezone_setter(instance):
    original = instance.timezone
    instance.timezone = original
    assert instance.timezone == original

@given(instance=eTJ_TimeFormat_strategy)
@settings(max_examples=50)
def test_etj_timeformat_instantiation(instance):
    assert isinstance(instance, eTJ_TimeFormat)



@given(instance=eTJ_TimeFormat_strategy)
def test_etj_timeformat_timeformat_setter(instance):
    original = instance.timeformat
    instance.timeformat = original
    assert instance.timeformat == original

@given(instance=eTJ_NumberFormat_strategy)
@settings(max_examples=50)
def test_etj_numberformat_instantiation(instance):
    assert isinstance(instance, eTJ_NumberFormat)

@given(instance=eTJ_ExtendTask_strategy)
@settings(max_examples=50)
def test_etj_extendtask_instantiation(instance):
    assert isinstance(instance, eTJ_ExtendTask)

@given(instance=eTJ_CurrencyFormat_strategy)
@settings(max_examples=50)
def test_etj_currencyformat_instantiation(instance):
    assert isinstance(instance, eTJ_CurrencyFormat)

@given(instance=eTJ_DailyWorkingHours_strategy)
@settings(max_examples=50)
def test_etj_dailyworkinghours_instantiation(instance):
    assert isinstance(instance, eTJ_DailyWorkingHours)



@given(instance=eTJ_DailyWorkingHours_strategy)
def test_etj_dailyworkinghours_dailyWorkingHours_setter(instance):
    original = instance.dailyWorkingHours
    instance.dailyWorkingHours = original
    assert instance.dailyWorkingHours == original

@given(instance=eTJ_TimingResolution_strategy)
@settings(max_examples=50)
def test_etj_timingresolution_instantiation(instance):
    assert isinstance(instance, eTJ_TimingResolution)



@given(instance=eTJ_TimingResolution_strategy)
def test_etj_timingresolution_timingResolution_setter(instance):
    original = instance.timingResolution
    instance.timingResolution = original
    assert instance.timingResolution == original

@given(instance=eTJ_Currency_strategy)
@settings(max_examples=50)
def test_etj_currency_instantiation(instance):
    assert isinstance(instance, eTJ_Currency)



@given(instance=eTJ_Currency_strategy)
def test_etj_currency_currency_setter(instance):
    original = instance.currency
    instance.currency = original
    assert instance.currency == original

@given(instance=eTJ_ISODATE_strategy)
@settings(max_examples=50)
def test_etj_isodate_instantiation(instance):
    assert isinstance(instance, eTJ_ISODATE)

@given(instance=eTJ_Credit_strategy)
@settings(max_examples=50)
def test_etj_credit_instantiation(instance):
    assert isinstance(instance, eTJ_Credit)



@given(instance=eTJ_Credit_strategy)
def test_etj_credit_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=eTJ_Credit_strategy)
def test_etj_credit_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=eTJ_Copyright_strategy)
@settings(max_examples=50)
def test_etj_copyright_instantiation(instance):
    assert isinstance(instance, eTJ_Copyright)



@given(instance=eTJ_Copyright_strategy)
def test_etj_copyright_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=eTJ_Complete_strategy)
@settings(max_examples=50)
def test_etj_complete_instantiation(instance):
    assert isinstance(instance, eTJ_Complete)



@given(instance=eTJ_Complete_strategy)
def test_etj_complete_complete_setter(instance):
    original = instance.complete
    instance.complete = original
    assert instance.complete == original

@given(instance=eTJ_Column_strategy)
@settings(max_examples=50)
def test_etj_column_instantiation(instance):
    assert isinstance(instance, eTJ_Column)



@given(instance=eTJ_Column_strategy)
def test_etj_column_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ_Columns_strategy)
@settings(max_examples=50)
def test_etj_columns_instantiation(instance):
    assert isinstance(instance, eTJ_Columns)

@given(instance=eTJ_Interval4_strategy)
@settings(max_examples=50)
def test_etj_interval4_instantiation(instance):
    assert isinstance(instance, eTJ_Interval4)

@given(instance=eTJ_Booking_strategy)
@settings(max_examples=50)
def test_etj_booking_instantiation(instance):
    assert isinstance(instance, eTJ_Booking)



@given(instance=eTJ_Booking_strategy)
def test_etj_booking_sloppy_setter(instance):
    original = instance.sloppy
    instance.sloppy = original
    assert instance.sloppy == original



@given(instance=eTJ_Booking_strategy)
def test_etj_booking_overtime_setter(instance):
    original = instance.overtime
    instance.overtime = original
    assert instance.overtime == original

@given(instance=eTJ_BookingResource_strategy)
@settings(max_examples=50)
def test_etj_bookingresource_instantiation(instance):
    assert isinstance(instance, eTJ_BookingResource)

@given(instance=eTJ_BookingTask_strategy)
@settings(max_examples=50)
def test_etj_bookingtask_instantiation(instance):
    assert isinstance(instance, eTJ_BookingTask)

@given(instance=eTJ_NavigatorAttribute_strategy)
@settings(max_examples=50)
def test_etj_navigatorattribute_instantiation(instance):
    assert isinstance(instance, eTJ_NavigatorAttribute)

@given(instance=eTJ_Navigator_strategy)
@settings(max_examples=50)
def test_etj_navigator_instantiation(instance):
    assert isinstance(instance, eTJ_Navigator)



@given(instance=eTJ_Navigator_strategy)
def test_etj_navigator_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ_AllocateResourceAttribute_strategy)
@settings(max_examples=50)
def test_etj_allocateresourceattribute_instantiation(instance):
    assert isinstance(instance, eTJ_AllocateResourceAttribute)

@given(instance=eTJ_AllocateResource_strategy)
@settings(max_examples=50)
def test_etj_allocateresource_instantiation(instance):
    assert isinstance(instance, eTJ_AllocateResource)

@given(instance=eTJ_Allocate_strategy)
@settings(max_examples=50)
def test_etj_allocate_instantiation(instance):
    assert isinstance(instance, eTJ_Allocate)

@given(instance=eTJ_ResourceAttribute_strategy)
@settings(max_examples=50)
def test_etj_resourceattribute_instantiation(instance):
    assert isinstance(instance, eTJ_ResourceAttribute)

@given(instance=eTJ_Resource_strategy)
@settings(max_examples=50)
def test_etj_resource_instantiation(instance):
    assert isinstance(instance, eTJ_Resource)



@given(instance=eTJ_Resource_strategy)
def test_etj_resource_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=eTJ_Resource_strategy)
def test_etj_resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ_Balance_strategy)
@settings(max_examples=50)
def test_etj_balance_instantiation(instance):
    assert isinstance(instance, eTJ_Balance)

@given(instance=StatusStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_statusstatussheetattribute_instantiation(instance):
    assert isinstance(instance, StatusStatusSheetAttribute)

@given(instance=eTJ_Summary_strategy)
@settings(max_examples=50)
def test_etj_summary_instantiation(instance):
    assert isinstance(instance, eTJ_Summary)

@given(instance=eTJ_Flags_strategy)
@settings(max_examples=50)
def test_etj_flags_instantiation(instance):
    assert isinstance(instance, eTJ_Flags)



@given(instance=eTJ_Flags_strategy)
def test_etj_flags_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original

@given(instance=eTJ_Details_strategy)
@settings(max_examples=50)
def test_etj_details_instantiation(instance):
    assert isinstance(instance, eTJ_Details)

@given(instance=eTJ_Author_strategy)
@settings(max_examples=50)
def test_etj_author_instantiation(instance):
    assert isinstance(instance, eTJ_Author)
