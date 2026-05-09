import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    LogicalExpression,
    eTJ::LogicalAbsoluteIdExression,
    eTJ::LogicalNumeralLiteral,
    eTJ::LogicalBooleanLiteral,
    eTJ::LogicalDateLiteral,
    eTJ::LogicalFlagExpression,
    eTJ::LogicalStringLiteral,
    eTJ::LogicalFunctionExpression,
    Definitions,
    eTJ::Defintions,
    eTJ::ExtDate,
    NumberFormat,
    CurrencyFormat,
    eTJ::RealFormat,
    eTJ::LimitAttribute,
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
    eTJ::RichText,
    Precedes,
    eTJ::ColumnAttribute,
    eTJ::WorkHours,
    eTJ::Weekdays,
    WeeklyMin,
    WeeklyMax,
    MonthlyMin,
    MonthlyMax,
    Minimum,
    Maximum,
    DailyMin,
    DailyMax,
    eTJ::Limit,
    GapLength,
    GapDuration,
    eTJ::TreeLevel,
    eTJ::TimesheetReportAttribute,
    eTJ::TimesheetAttribute,
    eTJ::TaskTimesheetAttribute,
    eTJ::TaskStatusSheetAttribute,
    StatusSheetAttribute,
    eTJ::StatusSheetReportAttribute,
    eTJ::StatusSheetAttribute,
    eTJ::Criterion,
    SortTasks,
    SortResources,
    SortJournalEntries,
    SortAccounts,
    eTJ::Sort,
    eTJ::ShiftsTask,
    eTJ::StatusTimesheetAttribute,
    eTJ::StatusStatusSheetAttribute,
    TaskStatusSheetAttribute,
    eTJ::TaskStatusSheet,
    eTJ::StatusStatusSheet,
    eTJ::Scheduling,
    eTJ::Scheduled,
    eTJ::ShiftsLimit,
    ShiftsTask,
    ShiftsResource,
    eTJ::Shifts,
    eTJ::Responsible,
    eTJ::PurgeTask,
    eTJ::AccountAttribute,
    AccountAttribute,
    eTJ::Interval2,
    ReportAttribute,
    eTJ::SortAccounts,
    eTJ::SortJournalEntries,
    eTJ::SelfContained,
    eTJ::AccountRoot,
    eTJ::RollupAccount,
    eTJ::ResourceRoot,
    eTJ::Right,
    eTJ::TaskRoot,
    IncludePropertiesAttribute,
    eTJ::ReportPrefix,
    eTJ::TaskPrefix,
    eTJ::ResourcePrefix,
    eTJ::AccountPrefix,
    eTJ::Property,
    eTJ::Project,
    eTJ::Global,
    eTJ::Interval3,
    eTJ::LeaveDetails,
    ResourceAttribute,
    eTJ::PurgeResource,
    eTJ::ShiftsResource,
    eTJ::Warn,
    Property,
    eTJ::Shift,
    eTJ::TagFile,
    eTJ::Macro,
    eTJ::TextReport,
    eTJ::SupplementTask,
    eTJ::ResourceReport,
    eTJ::SupplementReport,
    eTJ::TimesheetReport,
    eTJ::StatusSheetReport,
    eTJ::AccountReport,
    eTJ::Rate,
    eTJ::TaskReport,
    eTJ::Vacation,
    eTJ::Timesheet,
    eTJ::SupplementAccount,
    eTJ::Account,
    eTJ::StatusSheet,
    eTJ::SupplementResource,
    eTJ::Leaves,
    eTJ::Note,
    eTJ::PurgeReport,
    eTJ::Prolog,
    eTJ::ProjectIds,
    eTJ::ProjectId,
    eTJ::Precedes,
    eTJ::LoadUnit,
    eTJ::LimitsAttribute,
    eTJ::Limits,
    eTJ::MinStart,
    eTJ::MinEnd,
    eTJ::Milestone,
    eTJ::MaxStart,
    eTJ::MaxEnd,
    eTJ::Managers,
    eTJ::JournalAttributes,
    eTJ::Length,
    eTJ::Left,
    eTJ::JournalMode,
    NavigatorAttribute,
    eTJ::HideReport,
    eTJ::Interval1,
    eTJ::IncludePropertiesAttribute,
    eTJ::IncludeProperties,
    eTJ::Footer,
    eTJ::Fail,
    eTJ::ExtendedTaskAttribute,
    eTJ::HideAccount,
    eTJ::Header,
    eTJ::GapLength,
    eTJ::GapDuration,
    eTJ::Function,
    NewTaskAttribute,
    IcalReportAttribute,
    eTJ::ScenarioIcal,
    eTJ::HideJournalEntry,
    eTJ::Email,
    eTJ::Effort,
    eTJ::Efficiency,
    eTJ::DurationQuantity,
    eTJ::Duration,
    StatusTimesheetAttribute,
    eTJ::TaskDependency,
    eTJ::Depends,
    eTJ::ExtendedResourceAttribute,
    eTJ::Extend,
    eTJ::Epilog,
    eTJ::EndCredit,
    TimesheetReportAttribute,
    TaskTimesheetAttribute,
    eTJ::Remaining,
    eTJ::Work,
    eTJ::Priority,
    StatusSheetReportAttribute,
    eTJ::SortResources,
    eTJ::SortTasks,
    NikuReportAttribute,
    eTJ::Timeoff,
    eTJ::Headline,
    eTJ::Formats,
    eTJ::AccountShare,
    eTJ::ChargeSet,
    eTJ::Charge,
    eTJ::Center,
    eTJ::RGB,
    eTJ::LogicalExpression,
    ColumnAttribute,
    eTJ::ExtendedResourceAttributeColumn,
    eTJ::ListType,
    eTJ::HAlign,
    eTJ::FontColor,
    eTJ::CellText,
    eTJ::ToolTip,
    eTJ::Title,
    eTJ::ListItem,
    eTJ::Width,
    eTJ::Scale,
    eTJ::CellColor,
    eTJ::Caption,
    ExportAttribute,
    eTJ::RollupTask,
    eTJ::TaskAttributes,
    eTJ::Period,
    eTJ::Start,
    eTJ::Scenarios,
    eTJ::RollupResource,
    eTJ::ResourceAttributes,
    eTJ::HideTask,
    eTJ::HideResource,
    eTJ::End,
    eTJ::Definitions,
    LimitsAttribute,
    eTJ::MonthlyMin,
    eTJ::DailyMin,
    eTJ::MonthlyMax,
    eTJ::Maximum,
    eTJ::WeeklyMax,
    eTJ::Minimum,
    eTJ::WeeklyMin,
    eTJ::DailyMax,
    ProjectAttribute,
    eTJ::ShortTimeFormat,
    eTJ::WorkingHours,
    eTJ::Include,
    eTJ::TimingResolution,
    eTJ::TrackingScenario,
    eTJ::WeekStarts,
    eTJ::ExtendResource,
    eTJ::TimeFormat,
    eTJ::DailyWorkingHours,
    eTJ::Now,
    eTJ::JournalEntry,
    eTJ::ExtendTask,
    eTJ::NumberFormat,
    eTJ::Timezone,
    eTJ::YearlyWorkingDays,
    eTJ::CurrencyFormat,
    eTJ::Currency,
    eTJ::ISODATE,
    eTJ::Credit,
    eTJ::Copyright,
    eTJ::Complete,
    eTJ::Column,
    eTJ::Columns,
    eTJ::Interval4,
    eTJ::Booking,
    eTJ::BookingResource,
    eTJ::BookingTask,
    eTJ::NavigatorAttribute,
    eTJ::Navigator,
    eTJ::AllocateResourceAttribute,
    eTJ::AllocateResource,
    eTJ::Allocate,
    eTJ::ResourceAttribute,
    eTJ::Resource,
    eTJ::Balance,
    StatusStatusSheetAttribute,
    eTJ::Flags,
    eTJ::Summary,
    eTJ::Details,
    eTJ::Author,
    AllocateResourceAttribute,
    eTJ::ShiftsAllocate,
    eTJ::Persistent,
    eTJ::Select,
    eTJ::Mandatory,
    eTJ::Alternative,
    eTJ::Alert,
    eTJ::NikuReportAttribute,
    eTJ::NikuReport,
    eTJ::NewTaskAttribute,
    TimesheetAttribute,
    eTJ::ShiftTimesheet,
    eTJ::TaskTimesheet,
    eTJ::StatusTimesheet,
    eTJ::NewTask,
    ExtDate,
    Start,
    End,
    eTJ::MacroCall,
    eTJ::EObject,
    eTJ::Scenario,
    eTJ::TaskAttribute,
    eTJ::Task,
    eTJ::ProjectAttribute,
    eTJ::ExportAttribute,
    eTJ::Export,
    eTJ::IcalReportAttribute,
    eTJ::IcalReport,
    eTJ::ReportAttribute,
    TextReport,
    TaskReport,
    ResourceReport,
    AccountReport,
    eTJ::Report,
    PurgeReportAttribute,
    Justification,
    ScaleResolution,
    ListTypeValues,
    WorkQuantityUnit,
    YesNo,
    LoadDisplayUnit,
    JournalAttributeValues,
    TimeUnit,
    SchedulingPolicy,
    ReportFormat,
    PurgeTaskAttribute,
    CriterionDirection,
    JournalEntrySortCriterion,
    LeaveType,
    ColumnId,
    AlertLevel,
    SelectArgument,
    DependsPolicy,
    ChargeApplies,
    PurgeResourceAttribute,
    BuildInMacro,
    Weekday,
    JournalModeValue,
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



def test_etj::logicalabsoluteidexression_is_not_abstract():
    assert not inspect.isabstract(eTJ::LogicalAbsoluteIdExression)


def test_etj::logicalabsoluteidexression_constructor_exists():
    assert callable(eTJ::LogicalAbsoluteIdExression.__init__)


def test_etj::logicalabsoluteidexression_constructor_args():
    sig = inspect.signature(eTJ::LogicalAbsoluteIdExression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_etj::logicalabsoluteidexression_has_value():
    assert hasattr(eTJ::LogicalAbsoluteIdExression, "value")
    descriptor = None
    for klass in eTJ::LogicalAbsoluteIdExression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj::logicalnumeralliteral_is_not_abstract():
    assert not inspect.isabstract(eTJ::LogicalNumeralLiteral)


def test_etj::logicalnumeralliteral_constructor_exists():
    assert callable(eTJ::LogicalNumeralLiteral.__init__)


def test_etj::logicalnumeralliteral_constructor_args():
    sig = inspect.signature(eTJ::LogicalNumeralLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_etj::logicalnumeralliteral_has_value():
    assert hasattr(eTJ::LogicalNumeralLiteral, "value")
    descriptor = None
    for klass in eTJ::LogicalNumeralLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj::logicalbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(eTJ::LogicalBooleanLiteral)


def test_etj::logicalbooleanliteral_constructor_exists():
    assert callable(eTJ::LogicalBooleanLiteral.__init__)


def test_etj::logicalbooleanliteral_constructor_args():
    sig = inspect.signature(eTJ::LogicalBooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "isTrue" in params, "Missing parameter 'isTrue'"

def test_etj::logicalbooleanliteral_has_isTrue():
    assert hasattr(eTJ::LogicalBooleanLiteral, "isTrue")
    descriptor = None
    for klass in eTJ::LogicalBooleanLiteral.__mro__:
        if "isTrue" in klass.__dict__:
            descriptor = klass.__dict__["isTrue"]
            break
    assert isinstance(descriptor, property)



def test_etj::logicaldateliteral_is_not_abstract():
    assert not inspect.isabstract(eTJ::LogicalDateLiteral)


def test_etj::logicaldateliteral_constructor_exists():
    assert callable(eTJ::LogicalDateLiteral.__init__)


def test_etj::logicaldateliteral_constructor_args():
    sig = inspect.signature(eTJ::LogicalDateLiteral.__init__)
    params = list(sig.parameters.keys())



def test_etj::logicalflagexpression_is_not_abstract():
    assert not inspect.isabstract(eTJ::LogicalFlagExpression)


def test_etj::logicalflagexpression_constructor_exists():
    assert callable(eTJ::LogicalFlagExpression.__init__)


def test_etj::logicalflagexpression_constructor_args():
    sig = inspect.signature(eTJ::LogicalFlagExpression.__init__)
    params = list(sig.parameters.keys())
    assert "columId" in params, "Missing parameter 'columId'"

def test_etj::logicalflagexpression_has_columId():
    assert hasattr(eTJ::LogicalFlagExpression, "columId")
    descriptor = None
    for klass in eTJ::LogicalFlagExpression.__mro__:
        if "columId" in klass.__dict__:
            descriptor = klass.__dict__["columId"]
            break
    assert isinstance(descriptor, property)



def test_etj::logicalstringliteral_is_not_abstract():
    assert not inspect.isabstract(eTJ::LogicalStringLiteral)


def test_etj::logicalstringliteral_constructor_exists():
    assert callable(eTJ::LogicalStringLiteral.__init__)


def test_etj::logicalstringliteral_constructor_args():
    sig = inspect.signature(eTJ::LogicalStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_etj::logicalstringliteral_has_value():
    assert hasattr(eTJ::LogicalStringLiteral, "value")
    descriptor = None
    for klass in eTJ::LogicalStringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj::logicalfunctionexpression_is_not_abstract():
    assert not inspect.isabstract(eTJ::LogicalFunctionExpression)


def test_etj::logicalfunctionexpression_constructor_exists():
    assert callable(eTJ::LogicalFunctionExpression.__init__)


def test_etj::logicalfunctionexpression_constructor_args():
    sig = inspect.signature(eTJ::LogicalFunctionExpression.__init__)
    params = list(sig.parameters.keys())



def test_definitions_is_not_abstract():
    assert not inspect.isabstract(Definitions)


def test_definitions_constructor_exists():
    assert callable(Definitions.__init__)


def test_definitions_constructor_args():
    sig = inspect.signature(Definitions.__init__)
    params = list(sig.parameters.keys())



def test_etj::defintions_is_not_abstract():
    assert not inspect.isabstract(eTJ::Defintions)


def test_etj::defintions_constructor_exists():
    assert callable(eTJ::Defintions.__init__)


def test_etj::defintions_constructor_args():
    sig = inspect.signature(eTJ::Defintions.__init__)
    params = list(sig.parameters.keys())
    assert "tasks" in params, "Missing parameter 'tasks'"
    assert "projectids" in params, "Missing parameter 'projectids'"
    assert "resources" in params, "Missing parameter 'resources'"
    assert "project" in params, "Missing parameter 'project'"
    assert "flags" in params, "Missing parameter 'flags'"

def test_etj::defintions_has_tasks():
    assert hasattr(eTJ::Defintions, "tasks")
    descriptor = None
    for klass in eTJ::Defintions.__mro__:
        if "tasks" in klass.__dict__:
            descriptor = klass.__dict__["tasks"]
            break
    assert isinstance(descriptor, property)

def test_etj::defintions_has_projectids():
    assert hasattr(eTJ::Defintions, "projectids")
    descriptor = None
    for klass in eTJ::Defintions.__mro__:
        if "projectids" in klass.__dict__:
            descriptor = klass.__dict__["projectids"]
            break
    assert isinstance(descriptor, property)

def test_etj::defintions_has_resources():
    assert hasattr(eTJ::Defintions, "resources")
    descriptor = None
    for klass in eTJ::Defintions.__mro__:
        if "resources" in klass.__dict__:
            descriptor = klass.__dict__["resources"]
            break
    assert isinstance(descriptor, property)

def test_etj::defintions_has_project():
    assert hasattr(eTJ::Defintions, "project")
    descriptor = None
    for klass in eTJ::Defintions.__mro__:
        if "project" in klass.__dict__:
            descriptor = klass.__dict__["project"]
            break
    assert isinstance(descriptor, property)

def test_etj::defintions_has_flags():
    assert hasattr(eTJ::Defintions, "flags")
    descriptor = None
    for klass in eTJ::Defintions.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)



def test_etj::extdate_is_not_abstract():
    assert not inspect.isabstract(eTJ::ExtDate)


def test_etj::extdate_constructor_exists():
    assert callable(eTJ::ExtDate.__init__)


def test_etj::extdate_constructor_args():
    sig = inspect.signature(eTJ::ExtDate.__init__)
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



def test_etj::realformat_is_not_abstract():
    assert not inspect.isabstract(eTJ::RealFormat)


def test_etj::realformat_constructor_exists():
    assert callable(eTJ::RealFormat.__init__)


def test_etj::realformat_constructor_args():
    sig = inspect.signature(eTJ::RealFormat.__init__)
    params = list(sig.parameters.keys())
    assert "thousandsSeparator" in params, "Missing parameter 'thousandsSeparator'"
    assert "fractionDigits" in params, "Missing parameter 'fractionDigits'"
    assert "negativeSuffix" in params, "Missing parameter 'negativeSuffix'"
    assert "negativePrefix" in params, "Missing parameter 'negativePrefix'"
    assert "fractionSeparator" in params, "Missing parameter 'fractionSeparator'"

def test_etj::realformat_has_thousandsSeparator():
    assert hasattr(eTJ::RealFormat, "thousandsSeparator")
    descriptor = None
    for klass in eTJ::RealFormat.__mro__:
        if "thousandsSeparator" in klass.__dict__:
            descriptor = klass.__dict__["thousandsSeparator"]
            break
    assert isinstance(descriptor, property)

def test_etj::realformat_has_fractionDigits():
    assert hasattr(eTJ::RealFormat, "fractionDigits")
    descriptor = None
    for klass in eTJ::RealFormat.__mro__:
        if "fractionDigits" in klass.__dict__:
            descriptor = klass.__dict__["fractionDigits"]
            break
    assert isinstance(descriptor, property)

def test_etj::realformat_has_negativeSuffix():
    assert hasattr(eTJ::RealFormat, "negativeSuffix")
    descriptor = None
    for klass in eTJ::RealFormat.__mro__:
        if "negativeSuffix" in klass.__dict__:
            descriptor = klass.__dict__["negativeSuffix"]
            break
    assert isinstance(descriptor, property)

def test_etj::realformat_has_negativePrefix():
    assert hasattr(eTJ::RealFormat, "negativePrefix")
    descriptor = None
    for klass in eTJ::RealFormat.__mro__:
        if "negativePrefix" in klass.__dict__:
            descriptor = klass.__dict__["negativePrefix"]
            break
    assert isinstance(descriptor, property)

def test_etj::realformat_has_fractionSeparator():
    assert hasattr(eTJ::RealFormat, "fractionSeparator")
    descriptor = None
    for klass in eTJ::RealFormat.__mro__:
        if "fractionSeparator" in klass.__dict__:
            descriptor = klass.__dict__["fractionSeparator"]
            break
    assert isinstance(descriptor, property)



def test_etj::limitattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::LimitAttribute)


def test_etj::limitattribute_constructor_exists():
    assert callable(eTJ::LimitAttribute.__init__)


def test_etj::limitattribute_constructor_args():
    sig = inspect.signature(eTJ::LimitAttribute.__init__)
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



def test_etj::richtext_is_not_abstract():
    assert not inspect.isabstract(eTJ::RichText)


def test_etj::richtext_constructor_exists():
    assert callable(eTJ::RichText.__init__)


def test_etj::richtext_constructor_args():
    sig = inspect.signature(eTJ::RichText.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_etj::richtext_has_text():
    assert hasattr(eTJ::RichText, "text")
    descriptor = None
    for klass in eTJ::RichText.__mro__:
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



def test_etj::columnattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::ColumnAttribute)


def test_etj::columnattribute_constructor_exists():
    assert callable(eTJ::ColumnAttribute.__init__)


def test_etj::columnattribute_constructor_args():
    sig = inspect.signature(eTJ::ColumnAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::workhours_is_not_abstract():
    assert not inspect.isabstract(eTJ::WorkHours)


def test_etj::workhours_constructor_exists():
    assert callable(eTJ::WorkHours.__init__)


def test_etj::workhours_constructor_args():
    sig = inspect.signature(eTJ::WorkHours.__init__)
    params = list(sig.parameters.keys())
    assert "stop" in params, "Missing parameter 'stop'"
    assert "start" in params, "Missing parameter 'start'"

def test_etj::workhours_has_stop():
    assert hasattr(eTJ::WorkHours, "stop")
    descriptor = None
    for klass in eTJ::WorkHours.__mro__:
        if "stop" in klass.__dict__:
            descriptor = klass.__dict__["stop"]
            break
    assert isinstance(descriptor, property)

def test_etj::workhours_has_start():
    assert hasattr(eTJ::WorkHours, "start")
    descriptor = None
    for klass in eTJ::WorkHours.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_etj::weekdays_is_not_abstract():
    assert not inspect.isabstract(eTJ::Weekdays)


def test_etj::weekdays_constructor_exists():
    assert callable(eTJ::Weekdays.__init__)


def test_etj::weekdays_constructor_args():
    sig = inspect.signature(eTJ::Weekdays.__init__)
    params = list(sig.parameters.keys())
    assert "first" in params, "Missing parameter 'first'"
    assert "last" in params, "Missing parameter 'last'"

def test_etj::weekdays_has_first():
    assert hasattr(eTJ::Weekdays, "first")
    descriptor = None
    for klass in eTJ::Weekdays.__mro__:
        if "first" in klass.__dict__:
            descriptor = klass.__dict__["first"]
            break
    assert isinstance(descriptor, property)

def test_etj::weekdays_has_last():
    assert hasattr(eTJ::Weekdays, "last")
    descriptor = None
    for klass in eTJ::Weekdays.__mro__:
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



def test_etj::limit_is_not_abstract():
    assert not inspect.isabstract(eTJ::Limit)


def test_etj::limit_constructor_exists():
    assert callable(eTJ::Limit.__init__)


def test_etj::limit_constructor_args():
    sig = inspect.signature(eTJ::Limit.__init__)
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



def test_etj::treelevel_is_not_abstract():
    assert not inspect.isabstract(eTJ::TreeLevel)


def test_etj::treelevel_constructor_exists():
    assert callable(eTJ::TreeLevel.__init__)


def test_etj::treelevel_constructor_args():
    sig = inspect.signature(eTJ::TreeLevel.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_etj::treelevel_has_level():
    assert hasattr(eTJ::TreeLevel, "level")
    descriptor = None
    for klass in eTJ::TreeLevel.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_etj::timesheetreportattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::TimesheetReportAttribute)


def test_etj::timesheetreportattribute_constructor_exists():
    assert callable(eTJ::TimesheetReportAttribute.__init__)


def test_etj::timesheetreportattribute_constructor_args():
    sig = inspect.signature(eTJ::TimesheetReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::timesheetattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::TimesheetAttribute)


def test_etj::timesheetattribute_constructor_exists():
    assert callable(eTJ::TimesheetAttribute.__init__)


def test_etj::timesheetattribute_constructor_args():
    sig = inspect.signature(eTJ::TimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::tasktimesheetattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::TaskTimesheetAttribute)


def test_etj::tasktimesheetattribute_constructor_exists():
    assert callable(eTJ::TaskTimesheetAttribute.__init__)


def test_etj::tasktimesheetattribute_constructor_args():
    sig = inspect.signature(eTJ::TaskTimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::taskstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::TaskStatusSheetAttribute)


def test_etj::taskstatussheetattribute_constructor_exists():
    assert callable(eTJ::TaskStatusSheetAttribute.__init__)


def test_etj::taskstatussheetattribute_constructor_args():
    sig = inspect.signature(eTJ::TaskStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_statussheetattribute_is_not_abstract():
    assert not inspect.isabstract(StatusSheetAttribute)


def test_statussheetattribute_constructor_exists():
    assert callable(StatusSheetAttribute.__init__)


def test_statussheetattribute_constructor_args():
    sig = inspect.signature(StatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::statussheetreportattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::StatusSheetReportAttribute)


def test_etj::statussheetreportattribute_constructor_exists():
    assert callable(eTJ::StatusSheetReportAttribute.__init__)


def test_etj::statussheetreportattribute_constructor_args():
    sig = inspect.signature(eTJ::StatusSheetReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::statussheetattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::StatusSheetAttribute)


def test_etj::statussheetattribute_constructor_exists():
    assert callable(eTJ::StatusSheetAttribute.__init__)


def test_etj::statussheetattribute_constructor_args():
    sig = inspect.signature(eTJ::StatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::criterion_is_not_abstract():
    assert not inspect.isabstract(eTJ::Criterion)


def test_etj::criterion_constructor_exists():
    assert callable(eTJ::Criterion.__init__)


def test_etj::criterion_constructor_args():
    sig = inspect.signature(eTJ::Criterion.__init__)
    params = list(sig.parameters.keys())
    assert "columnId" in params, "Missing parameter 'columnId'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_etj::criterion_has_columnId():
    assert hasattr(eTJ::Criterion, "columnId")
    descriptor = None
    for klass in eTJ::Criterion.__mro__:
        if "columnId" in klass.__dict__:
            descriptor = klass.__dict__["columnId"]
            break
    assert isinstance(descriptor, property)

def test_etj::criterion_has_direction():
    assert hasattr(eTJ::Criterion, "direction")
    descriptor = None
    for klass in eTJ::Criterion.__mro__:
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



def test_etj::sort_is_not_abstract():
    assert not inspect.isabstract(eTJ::Sort)


def test_etj::sort_constructor_exists():
    assert callable(eTJ::Sort.__init__)


def test_etj::sort_constructor_args():
    sig = inspect.signature(eTJ::Sort.__init__)
    params = list(sig.parameters.keys())
    assert "tree" in params, "Missing parameter 'tree'"

def test_etj::sort_has_tree():
    assert hasattr(eTJ::Sort, "tree")
    descriptor = None
    for klass in eTJ::Sort.__mro__:
        if "tree" in klass.__dict__:
            descriptor = klass.__dict__["tree"]
            break
    assert isinstance(descriptor, property)



def test_etj::shiftstask_is_not_abstract():
    assert not inspect.isabstract(eTJ::ShiftsTask)


def test_etj::shiftstask_constructor_exists():
    assert callable(eTJ::ShiftsTask.__init__)


def test_etj::shiftstask_constructor_args():
    sig = inspect.signature(eTJ::ShiftsTask.__init__)
    params = list(sig.parameters.keys())



def test_etj::statustimesheetattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::StatusTimesheetAttribute)


def test_etj::statustimesheetattribute_constructor_exists():
    assert callable(eTJ::StatusTimesheetAttribute.__init__)


def test_etj::statustimesheetattribute_constructor_args():
    sig = inspect.signature(eTJ::StatusTimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::statusstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::StatusStatusSheetAttribute)


def test_etj::statusstatussheetattribute_constructor_exists():
    assert callable(eTJ::StatusStatusSheetAttribute.__init__)


def test_etj::statusstatussheetattribute_constructor_args():
    sig = inspect.signature(eTJ::StatusStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_taskstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(TaskStatusSheetAttribute)


def test_taskstatussheetattribute_constructor_exists():
    assert callable(TaskStatusSheetAttribute.__init__)


def test_taskstatussheetattribute_constructor_args():
    sig = inspect.signature(TaskStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::taskstatussheet_is_not_abstract():
    assert not inspect.isabstract(eTJ::TaskStatusSheet)


def test_etj::taskstatussheet_constructor_exists():
    assert callable(eTJ::TaskStatusSheet.__init__)


def test_etj::taskstatussheet_constructor_args():
    sig = inspect.signature(eTJ::TaskStatusSheet.__init__)
    params = list(sig.parameters.keys())



def test_etj::statusstatussheet_is_not_abstract():
    assert not inspect.isabstract(eTJ::StatusStatusSheet)


def test_etj::statusstatussheet_constructor_exists():
    assert callable(eTJ::StatusStatusSheet.__init__)


def test_etj::statusstatussheet_constructor_args():
    sig = inspect.signature(eTJ::StatusStatusSheet.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "text" in params, "Missing parameter 'text'"

def test_etj::statusstatussheet_has_level():
    assert hasattr(eTJ::StatusStatusSheet, "level")
    descriptor = None
    for klass in eTJ::StatusStatusSheet.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_etj::statusstatussheet_has_text():
    assert hasattr(eTJ::StatusStatusSheet, "text")
    descriptor = None
    for klass in eTJ::StatusStatusSheet.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_etj::scheduling_is_not_abstract():
    assert not inspect.isabstract(eTJ::Scheduling)


def test_etj::scheduling_constructor_exists():
    assert callable(eTJ::Scheduling.__init__)


def test_etj::scheduling_constructor_args():
    sig = inspect.signature(eTJ::Scheduling.__init__)
    params = list(sig.parameters.keys())
    assert "scheduling" in params, "Missing parameter 'scheduling'"

def test_etj::scheduling_has_scheduling():
    assert hasattr(eTJ::Scheduling, "scheduling")
    descriptor = None
    for klass in eTJ::Scheduling.__mro__:
        if "scheduling" in klass.__dict__:
            descriptor = klass.__dict__["scheduling"]
            break
    assert isinstance(descriptor, property)



def test_etj::scheduled_is_not_abstract():
    assert not inspect.isabstract(eTJ::Scheduled)


def test_etj::scheduled_constructor_exists():
    assert callable(eTJ::Scheduled.__init__)


def test_etj::scheduled_constructor_args():
    sig = inspect.signature(eTJ::Scheduled.__init__)
    params = list(sig.parameters.keys())
    assert "scheduled" in params, "Missing parameter 'scheduled'"

def test_etj::scheduled_has_scheduled():
    assert hasattr(eTJ::Scheduled, "scheduled")
    descriptor = None
    for klass in eTJ::Scheduled.__mro__:
        if "scheduled" in klass.__dict__:
            descriptor = klass.__dict__["scheduled"]
            break
    assert isinstance(descriptor, property)



def test_etj::shiftslimit_is_not_abstract():
    assert not inspect.isabstract(eTJ::ShiftsLimit)


def test_etj::shiftslimit_constructor_exists():
    assert callable(eTJ::ShiftsLimit.__init__)


def test_etj::shiftslimit_constructor_args():
    sig = inspect.signature(eTJ::ShiftsLimit.__init__)
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



def test_etj::shifts_is_not_abstract():
    assert not inspect.isabstract(eTJ::Shifts)


def test_etj::shifts_constructor_exists():
    assert callable(eTJ::Shifts.__init__)


def test_etj::shifts_constructor_args():
    sig = inspect.signature(eTJ::Shifts.__init__)
    params = list(sig.parameters.keys())



def test_etj::responsible_is_not_abstract():
    assert not inspect.isabstract(eTJ::Responsible)


def test_etj::responsible_constructor_exists():
    assert callable(eTJ::Responsible.__init__)


def test_etj::responsible_constructor_args():
    sig = inspect.signature(eTJ::Responsible.__init__)
    params = list(sig.parameters.keys())



def test_etj::purgetask_is_not_abstract():
    assert not inspect.isabstract(eTJ::PurgeTask)


def test_etj::purgetask_constructor_exists():
    assert callable(eTJ::PurgeTask.__init__)


def test_etj::purgetask_constructor_args():
    sig = inspect.signature(eTJ::PurgeTask.__init__)
    params = list(sig.parameters.keys())
    assert "listAttribute" in params, "Missing parameter 'listAttribute'"

def test_etj::purgetask_has_listAttribute():
    assert hasattr(eTJ::PurgeTask, "listAttribute")
    descriptor = None
    for klass in eTJ::PurgeTask.__mro__:
        if "listAttribute" in klass.__dict__:
            descriptor = klass.__dict__["listAttribute"]
            break
    assert isinstance(descriptor, property)



def test_etj::accountattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::AccountAttribute)


def test_etj::accountattribute_constructor_exists():
    assert callable(eTJ::AccountAttribute.__init__)


def test_etj::accountattribute_constructor_args():
    sig = inspect.signature(eTJ::AccountAttribute.__init__)
    params = list(sig.parameters.keys())



def test_accountattribute_is_not_abstract():
    assert not inspect.isabstract(AccountAttribute)


def test_accountattribute_constructor_exists():
    assert callable(AccountAttribute.__init__)


def test_accountattribute_constructor_args():
    sig = inspect.signature(AccountAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::interval2_is_not_abstract():
    assert not inspect.isabstract(eTJ::Interval2)


def test_etj::interval2_constructor_exists():
    assert callable(eTJ::Interval2.__init__)


def test_etj::interval2_constructor_args():
    sig = inspect.signature(eTJ::Interval2.__init__)
    params = list(sig.parameters.keys())



def test_reportattribute_is_not_abstract():
    assert not inspect.isabstract(ReportAttribute)


def test_reportattribute_constructor_exists():
    assert callable(ReportAttribute.__init__)


def test_reportattribute_constructor_args():
    sig = inspect.signature(ReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::sortaccounts_is_not_abstract():
    assert not inspect.isabstract(eTJ::SortAccounts)


def test_etj::sortaccounts_constructor_exists():
    assert callable(eTJ::SortAccounts.__init__)


def test_etj::sortaccounts_constructor_args():
    sig = inspect.signature(eTJ::SortAccounts.__init__)
    params = list(sig.parameters.keys())



def test_etj::sortjournalentries_is_not_abstract():
    assert not inspect.isabstract(eTJ::SortJournalEntries)


def test_etj::sortjournalentries_constructor_exists():
    assert callable(eTJ::SortJournalEntries.__init__)


def test_etj::sortjournalentries_constructor_args():
    sig = inspect.signature(eTJ::SortJournalEntries.__init__)
    params = list(sig.parameters.keys())



def test_etj::selfcontained_is_not_abstract():
    assert not inspect.isabstract(eTJ::SelfContained)


def test_etj::selfcontained_constructor_exists():
    assert callable(eTJ::SelfContained.__init__)


def test_etj::selfcontained_constructor_args():
    sig = inspect.signature(eTJ::SelfContained.__init__)
    params = list(sig.parameters.keys())
    assert "selfcontained" in params, "Missing parameter 'selfcontained'"

def test_etj::selfcontained_has_selfcontained():
    assert hasattr(eTJ::SelfContained, "selfcontained")
    descriptor = None
    for klass in eTJ::SelfContained.__mro__:
        if "selfcontained" in klass.__dict__:
            descriptor = klass.__dict__["selfcontained"]
            break
    assert isinstance(descriptor, property)



def test_etj::accountroot_is_not_abstract():
    assert not inspect.isabstract(eTJ::AccountRoot)


def test_etj::accountroot_constructor_exists():
    assert callable(eTJ::AccountRoot.__init__)


def test_etj::accountroot_constructor_args():
    sig = inspect.signature(eTJ::AccountRoot.__init__)
    params = list(sig.parameters.keys())



def test_etj::rollupaccount_is_not_abstract():
    assert not inspect.isabstract(eTJ::RollupAccount)


def test_etj::rollupaccount_constructor_exists():
    assert callable(eTJ::RollupAccount.__init__)


def test_etj::rollupaccount_constructor_args():
    sig = inspect.signature(eTJ::RollupAccount.__init__)
    params = list(sig.parameters.keys())



def test_etj::resourceroot_is_not_abstract():
    assert not inspect.isabstract(eTJ::ResourceRoot)


def test_etj::resourceroot_constructor_exists():
    assert callable(eTJ::ResourceRoot.__init__)


def test_etj::resourceroot_constructor_args():
    sig = inspect.signature(eTJ::ResourceRoot.__init__)
    params = list(sig.parameters.keys())



def test_etj::right_is_not_abstract():
    assert not inspect.isabstract(eTJ::Right)


def test_etj::right_constructor_exists():
    assert callable(eTJ::Right.__init__)


def test_etj::right_constructor_args():
    sig = inspect.signature(eTJ::Right.__init__)
    params = list(sig.parameters.keys())



def test_etj::taskroot_is_not_abstract():
    assert not inspect.isabstract(eTJ::TaskRoot)


def test_etj::taskroot_constructor_exists():
    assert callable(eTJ::TaskRoot.__init__)


def test_etj::taskroot_constructor_args():
    sig = inspect.signature(eTJ::TaskRoot.__init__)
    params = list(sig.parameters.keys())



def test_includepropertiesattribute_is_not_abstract():
    assert not inspect.isabstract(IncludePropertiesAttribute)


def test_includepropertiesattribute_constructor_exists():
    assert callable(IncludePropertiesAttribute.__init__)


def test_includepropertiesattribute_constructor_args():
    sig = inspect.signature(IncludePropertiesAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::reportprefix_is_not_abstract():
    assert not inspect.isabstract(eTJ::ReportPrefix)


def test_etj::reportprefix_constructor_exists():
    assert callable(eTJ::ReportPrefix.__init__)


def test_etj::reportprefix_constructor_args():
    sig = inspect.signature(eTJ::ReportPrefix.__init__)
    params = list(sig.parameters.keys())



def test_etj::taskprefix_is_not_abstract():
    assert not inspect.isabstract(eTJ::TaskPrefix)


def test_etj::taskprefix_constructor_exists():
    assert callable(eTJ::TaskPrefix.__init__)


def test_etj::taskprefix_constructor_args():
    sig = inspect.signature(eTJ::TaskPrefix.__init__)
    params = list(sig.parameters.keys())



def test_etj::resourceprefix_is_not_abstract():
    assert not inspect.isabstract(eTJ::ResourcePrefix)


def test_etj::resourceprefix_constructor_exists():
    assert callable(eTJ::ResourcePrefix.__init__)


def test_etj::resourceprefix_constructor_args():
    sig = inspect.signature(eTJ::ResourcePrefix.__init__)
    params = list(sig.parameters.keys())



def test_etj::accountprefix_is_not_abstract():
    assert not inspect.isabstract(eTJ::AccountPrefix)


def test_etj::accountprefix_constructor_exists():
    assert callable(eTJ::AccountPrefix.__init__)


def test_etj::accountprefix_constructor_args():
    sig = inspect.signature(eTJ::AccountPrefix.__init__)
    params = list(sig.parameters.keys())



def test_etj::property_is_not_abstract():
    assert not inspect.isabstract(eTJ::Property)


def test_etj::property_constructor_exists():
    assert callable(eTJ::Property.__init__)


def test_etj::property_constructor_args():
    sig = inspect.signature(eTJ::Property.__init__)
    params = list(sig.parameters.keys())



def test_etj::project_is_not_abstract():
    assert not inspect.isabstract(eTJ::Project)


def test_etj::project_constructor_exists():
    assert callable(eTJ::Project.__init__)


def test_etj::project_constructor_args():
    sig = inspect.signature(eTJ::Project.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_etj::project_has_id():
    assert hasattr(eTJ::Project, "id")
    descriptor = None
    for klass in eTJ::Project.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_etj::project_has_version():
    assert hasattr(eTJ::Project, "version")
    descriptor = None
    for klass in eTJ::Project.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_etj::project_has_name():
    assert hasattr(eTJ::Project, "name")
    descriptor = None
    for klass in eTJ::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_etj::global_is_not_abstract():
    assert not inspect.isabstract(eTJ::Global)


def test_etj::global_constructor_exists():
    assert callable(eTJ::Global.__init__)


def test_etj::global_constructor_args():
    sig = inspect.signature(eTJ::Global.__init__)
    params = list(sig.parameters.keys())



def test_etj::interval3_is_not_abstract():
    assert not inspect.isabstract(eTJ::Interval3)


def test_etj::interval3_constructor_exists():
    assert callable(eTJ::Interval3.__init__)


def test_etj::interval3_constructor_args():
    sig = inspect.signature(eTJ::Interval3.__init__)
    params = list(sig.parameters.keys())



def test_etj::leavedetails_is_not_abstract():
    assert not inspect.isabstract(eTJ::LeaveDetails)


def test_etj::leavedetails_constructor_exists():
    assert callable(eTJ::LeaveDetails.__init__)


def test_etj::leavedetails_constructor_args():
    sig = inspect.signature(eTJ::LeaveDetails.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_etj::leavedetails_has_type():
    assert hasattr(eTJ::LeaveDetails, "type")
    descriptor = None
    for klass in eTJ::LeaveDetails.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_etj::leavedetails_has_name():
    assert hasattr(eTJ::LeaveDetails, "name")
    descriptor = None
    for klass in eTJ::LeaveDetails.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_resourceattribute_is_not_abstract():
    assert not inspect.isabstract(ResourceAttribute)


def test_resourceattribute_constructor_exists():
    assert callable(ResourceAttribute.__init__)


def test_resourceattribute_constructor_args():
    sig = inspect.signature(ResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::purgeresource_is_not_abstract():
    assert not inspect.isabstract(eTJ::PurgeResource)


def test_etj::purgeresource_constructor_exists():
    assert callable(eTJ::PurgeResource.__init__)


def test_etj::purgeresource_constructor_args():
    sig = inspect.signature(eTJ::PurgeResource.__init__)
    params = list(sig.parameters.keys())
    assert "listAttribute" in params, "Missing parameter 'listAttribute'"

def test_etj::purgeresource_has_listAttribute():
    assert hasattr(eTJ::PurgeResource, "listAttribute")
    descriptor = None
    for klass in eTJ::PurgeResource.__mro__:
        if "listAttribute" in klass.__dict__:
            descriptor = klass.__dict__["listAttribute"]
            break
    assert isinstance(descriptor, property)



def test_etj::shiftsresource_is_not_abstract():
    assert not inspect.isabstract(eTJ::ShiftsResource)


def test_etj::shiftsresource_constructor_exists():
    assert callable(eTJ::ShiftsResource.__init__)


def test_etj::shiftsresource_constructor_args():
    sig = inspect.signature(eTJ::ShiftsResource.__init__)
    params = list(sig.parameters.keys())



def test_etj::warn_is_not_abstract():
    assert not inspect.isabstract(eTJ::Warn)


def test_etj::warn_constructor_exists():
    assert callable(eTJ::Warn.__init__)


def test_etj::warn_constructor_args():
    sig = inspect.signature(eTJ::Warn.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_etj::shift_is_not_abstract():
    assert not inspect.isabstract(eTJ::Shift)


def test_etj::shift_constructor_exists():
    assert callable(eTJ::Shift.__init__)


def test_etj::shift_constructor_args():
    sig = inspect.signature(eTJ::Shift.__init__)
    params = list(sig.parameters.keys())
    assert "replace" in params, "Missing parameter 'replace'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "timezone" in params, "Missing parameter 'timezone'"

def test_etj::shift_has_replace():
    assert hasattr(eTJ::Shift, "replace")
    descriptor = None
    for klass in eTJ::Shift.__mro__:
        if "replace" in klass.__dict__:
            descriptor = klass.__dict__["replace"]
            break
    assert isinstance(descriptor, property)

def test_etj::shift_has_name():
    assert hasattr(eTJ::Shift, "name")
    descriptor = None
    for klass in eTJ::Shift.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_etj::shift_has_id():
    assert hasattr(eTJ::Shift, "id")
    descriptor = None
    for klass in eTJ::Shift.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_etj::shift_has_timezone():
    assert hasattr(eTJ::Shift, "timezone")
    descriptor = None
    for klass in eTJ::Shift.__mro__:
        if "timezone" in klass.__dict__:
            descriptor = klass.__dict__["timezone"]
            break
    assert isinstance(descriptor, property)



def test_etj::tagfile_is_not_abstract():
    assert not inspect.isabstract(eTJ::TagFile)


def test_etj::tagfile_constructor_exists():
    assert callable(eTJ::TagFile.__init__)


def test_etj::tagfile_constructor_args():
    sig = inspect.signature(eTJ::TagFile.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "filename" in params, "Missing parameter 'filename'"

def test_etj::tagfile_has_id():
    assert hasattr(eTJ::TagFile, "id")
    descriptor = None
    for klass in eTJ::TagFile.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_etj::tagfile_has_filename():
    assert hasattr(eTJ::TagFile, "filename")
    descriptor = None
    for klass in eTJ::TagFile.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_etj::macro_is_not_abstract():
    assert not inspect.isabstract(eTJ::Macro)


def test_etj::macro_constructor_exists():
    assert callable(eTJ::Macro.__init__)


def test_etj::macro_constructor_args():
    sig = inspect.signature(eTJ::Macro.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "id" in params, "Missing parameter 'id'"

def test_etj::macro_has_value():
    assert hasattr(eTJ::Macro, "value")
    descriptor = None
    for klass in eTJ::Macro.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_etj::macro_has_id():
    assert hasattr(eTJ::Macro, "id")
    descriptor = None
    for klass in eTJ::Macro.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_etj::textreport_is_not_abstract():
    assert not inspect.isabstract(eTJ::TextReport)


def test_etj::textreport_constructor_exists():
    assert callable(eTJ::TextReport.__init__)


def test_etj::textreport_constructor_args():
    sig = inspect.signature(eTJ::TextReport.__init__)
    params = list(sig.parameters.keys())



def test_etj::supplementtask_is_not_abstract():
    assert not inspect.isabstract(eTJ::SupplementTask)


def test_etj::supplementtask_constructor_exists():
    assert callable(eTJ::SupplementTask.__init__)


def test_etj::supplementtask_constructor_args():
    sig = inspect.signature(eTJ::SupplementTask.__init__)
    params = list(sig.parameters.keys())



def test_etj::resourcereport_is_not_abstract():
    assert not inspect.isabstract(eTJ::ResourceReport)


def test_etj::resourcereport_constructor_exists():
    assert callable(eTJ::ResourceReport.__init__)


def test_etj::resourcereport_constructor_args():
    sig = inspect.signature(eTJ::ResourceReport.__init__)
    params = list(sig.parameters.keys())



def test_etj::supplementreport_is_not_abstract():
    assert not inspect.isabstract(eTJ::SupplementReport)


def test_etj::supplementreport_constructor_exists():
    assert callable(eTJ::SupplementReport.__init__)


def test_etj::supplementreport_constructor_args():
    sig = inspect.signature(eTJ::SupplementReport.__init__)
    params = list(sig.parameters.keys())



def test_etj::timesheetreport_is_not_abstract():
    assert not inspect.isabstract(eTJ::TimesheetReport)


def test_etj::timesheetreport_constructor_exists():
    assert callable(eTJ::TimesheetReport.__init__)


def test_etj::timesheetreport_constructor_args():
    sig = inspect.signature(eTJ::TimesheetReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_etj::timesheetreport_has_filename():
    assert hasattr(eTJ::TimesheetReport, "filename")
    descriptor = None
    for klass in eTJ::TimesheetReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_etj::statussheetreport_is_not_abstract():
    assert not inspect.isabstract(eTJ::StatusSheetReport)


def test_etj::statussheetreport_constructor_exists():
    assert callable(eTJ::StatusSheetReport.__init__)


def test_etj::statussheetreport_constructor_args():
    sig = inspect.signature(eTJ::StatusSheetReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_etj::statussheetreport_has_filename():
    assert hasattr(eTJ::StatusSheetReport, "filename")
    descriptor = None
    for klass in eTJ::StatusSheetReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_etj::accountreport_is_not_abstract():
    assert not inspect.isabstract(eTJ::AccountReport)


def test_etj::accountreport_constructor_exists():
    assert callable(eTJ::AccountReport.__init__)


def test_etj::accountreport_constructor_args():
    sig = inspect.signature(eTJ::AccountReport.__init__)
    params = list(sig.parameters.keys())



def test_etj::rate_is_not_abstract():
    assert not inspect.isabstract(eTJ::Rate)


def test_etj::rate_constructor_exists():
    assert callable(eTJ::Rate.__init__)


def test_etj::rate_constructor_args():
    sig = inspect.signature(eTJ::Rate.__init__)
    params = list(sig.parameters.keys())
    assert "rate" in params, "Missing parameter 'rate'"

def test_etj::rate_has_rate():
    assert hasattr(eTJ::Rate, "rate")
    descriptor = None
    for klass in eTJ::Rate.__mro__:
        if "rate" in klass.__dict__:
            descriptor = klass.__dict__["rate"]
            break
    assert isinstance(descriptor, property)



def test_etj::taskreport_is_not_abstract():
    assert not inspect.isabstract(eTJ::TaskReport)


def test_etj::taskreport_constructor_exists():
    assert callable(eTJ::TaskReport.__init__)


def test_etj::taskreport_constructor_args():
    sig = inspect.signature(eTJ::TaskReport.__init__)
    params = list(sig.parameters.keys())



def test_etj::vacation_is_not_abstract():
    assert not inspect.isabstract(eTJ::Vacation)


def test_etj::vacation_constructor_exists():
    assert callable(eTJ::Vacation.__init__)


def test_etj::vacation_constructor_args():
    sig = inspect.signature(eTJ::Vacation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_etj::vacation_has_name():
    assert hasattr(eTJ::Vacation, "name")
    descriptor = None
    for klass in eTJ::Vacation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_etj::timesheet_is_not_abstract():
    assert not inspect.isabstract(eTJ::Timesheet)


def test_etj::timesheet_constructor_exists():
    assert callable(eTJ::Timesheet.__init__)


def test_etj::timesheet_constructor_args():
    sig = inspect.signature(eTJ::Timesheet.__init__)
    params = list(sig.parameters.keys())



def test_etj::supplementaccount_is_not_abstract():
    assert not inspect.isabstract(eTJ::SupplementAccount)


def test_etj::supplementaccount_constructor_exists():
    assert callable(eTJ::SupplementAccount.__init__)


def test_etj::supplementaccount_constructor_args():
    sig = inspect.signature(eTJ::SupplementAccount.__init__)
    params = list(sig.parameters.keys())



def test_etj::account_is_not_abstract():
    assert not inspect.isabstract(eTJ::Account)


def test_etj::account_constructor_exists():
    assert callable(eTJ::Account.__init__)


def test_etj::account_constructor_args():
    sig = inspect.signature(eTJ::Account.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_etj::account_has_name():
    assert hasattr(eTJ::Account, "name")
    descriptor = None
    for klass in eTJ::Account.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_etj::account_has_id():
    assert hasattr(eTJ::Account, "id")
    descriptor = None
    for klass in eTJ::Account.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_etj::statussheet_is_not_abstract():
    assert not inspect.isabstract(eTJ::StatusSheet)


def test_etj::statussheet_constructor_exists():
    assert callable(eTJ::StatusSheet.__init__)


def test_etj::statussheet_constructor_args():
    sig = inspect.signature(eTJ::StatusSheet.__init__)
    params = list(sig.parameters.keys())



def test_etj::supplementresource_is_not_abstract():
    assert not inspect.isabstract(eTJ::SupplementResource)


def test_etj::supplementresource_constructor_exists():
    assert callable(eTJ::SupplementResource.__init__)


def test_etj::supplementresource_constructor_args():
    sig = inspect.signature(eTJ::SupplementResource.__init__)
    params = list(sig.parameters.keys())



def test_etj::leaves_is_not_abstract():
    assert not inspect.isabstract(eTJ::Leaves)


def test_etj::leaves_constructor_exists():
    assert callable(eTJ::Leaves.__init__)


def test_etj::leaves_constructor_args():
    sig = inspect.signature(eTJ::Leaves.__init__)
    params = list(sig.parameters.keys())



def test_etj::note_is_not_abstract():
    assert not inspect.isabstract(eTJ::Note)


def test_etj::note_constructor_exists():
    assert callable(eTJ::Note.__init__)


def test_etj::note_constructor_args():
    sig = inspect.signature(eTJ::Note.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"

def test_etj::note_has_note():
    assert hasattr(eTJ::Note, "note")
    descriptor = None
    for klass in eTJ::Note.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_etj::purgereport_is_not_abstract():
    assert not inspect.isabstract(eTJ::PurgeReport)


def test_etj::purgereport_constructor_exists():
    assert callable(eTJ::PurgeReport.__init__)


def test_etj::purgereport_constructor_args():
    sig = inspect.signature(eTJ::PurgeReport.__init__)
    params = list(sig.parameters.keys())
    assert "listAttribute" in params, "Missing parameter 'listAttribute'"

def test_etj::purgereport_has_listAttribute():
    assert hasattr(eTJ::PurgeReport, "listAttribute")
    descriptor = None
    for klass in eTJ::PurgeReport.__mro__:
        if "listAttribute" in klass.__dict__:
            descriptor = klass.__dict__["listAttribute"]
            break
    assert isinstance(descriptor, property)



def test_etj::prolog_is_not_abstract():
    assert not inspect.isabstract(eTJ::Prolog)


def test_etj::prolog_constructor_exists():
    assert callable(eTJ::Prolog.__init__)


def test_etj::prolog_constructor_args():
    sig = inspect.signature(eTJ::Prolog.__init__)
    params = list(sig.parameters.keys())



def test_etj::projectids_is_not_abstract():
    assert not inspect.isabstract(eTJ::ProjectIds)


def test_etj::projectids_constructor_exists():
    assert callable(eTJ::ProjectIds.__init__)


def test_etj::projectids_constructor_args():
    sig = inspect.signature(eTJ::ProjectIds.__init__)
    params = list(sig.parameters.keys())
    assert "ids" in params, "Missing parameter 'ids'"

def test_etj::projectids_has_ids():
    assert hasattr(eTJ::ProjectIds, "ids")
    descriptor = None
    for klass in eTJ::ProjectIds.__mro__:
        if "ids" in klass.__dict__:
            descriptor = klass.__dict__["ids"]
            break
    assert isinstance(descriptor, property)



def test_etj::projectid_is_not_abstract():
    assert not inspect.isabstract(eTJ::ProjectId)


def test_etj::projectid_constructor_exists():
    assert callable(eTJ::ProjectId.__init__)


def test_etj::projectid_constructor_args():
    sig = inspect.signature(eTJ::ProjectId.__init__)
    params = list(sig.parameters.keys())
    assert "projectId" in params, "Missing parameter 'projectId'"

def test_etj::projectid_has_projectId():
    assert hasattr(eTJ::ProjectId, "projectId")
    descriptor = None
    for klass in eTJ::ProjectId.__mro__:
        if "projectId" in klass.__dict__:
            descriptor = klass.__dict__["projectId"]
            break
    assert isinstance(descriptor, property)



def test_etj::precedes_is_not_abstract():
    assert not inspect.isabstract(eTJ::Precedes)


def test_etj::precedes_constructor_exists():
    assert callable(eTJ::Precedes.__init__)


def test_etj::precedes_constructor_args():
    sig = inspect.signature(eTJ::Precedes.__init__)
    params = list(sig.parameters.keys())



def test_etj::loadunit_is_not_abstract():
    assert not inspect.isabstract(eTJ::LoadUnit)


def test_etj::loadunit_constructor_exists():
    assert callable(eTJ::LoadUnit.__init__)


def test_etj::loadunit_constructor_args():
    sig = inspect.signature(eTJ::LoadUnit.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_etj::loadunit_has_unit():
    assert hasattr(eTJ::LoadUnit, "unit")
    descriptor = None
    for klass in eTJ::LoadUnit.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_etj::limitsattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::LimitsAttribute)


def test_etj::limitsattribute_constructor_exists():
    assert callable(eTJ::LimitsAttribute.__init__)


def test_etj::limitsattribute_constructor_args():
    sig = inspect.signature(eTJ::LimitsAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::limits_is_not_abstract():
    assert not inspect.isabstract(eTJ::Limits)


def test_etj::limits_constructor_exists():
    assert callable(eTJ::Limits.__init__)


def test_etj::limits_constructor_args():
    sig = inspect.signature(eTJ::Limits.__init__)
    params = list(sig.parameters.keys())



def test_etj::minstart_is_not_abstract():
    assert not inspect.isabstract(eTJ::MinStart)


def test_etj::minstart_constructor_exists():
    assert callable(eTJ::MinStart.__init__)


def test_etj::minstart_constructor_args():
    sig = inspect.signature(eTJ::MinStart.__init__)
    params = list(sig.parameters.keys())



def test_etj::minend_is_not_abstract():
    assert not inspect.isabstract(eTJ::MinEnd)


def test_etj::minend_constructor_exists():
    assert callable(eTJ::MinEnd.__init__)


def test_etj::minend_constructor_args():
    sig = inspect.signature(eTJ::MinEnd.__init__)
    params = list(sig.parameters.keys())



def test_etj::milestone_is_not_abstract():
    assert not inspect.isabstract(eTJ::Milestone)


def test_etj::milestone_constructor_exists():
    assert callable(eTJ::Milestone.__init__)


def test_etj::milestone_constructor_args():
    sig = inspect.signature(eTJ::Milestone.__init__)
    params = list(sig.parameters.keys())
    assert "milestone" in params, "Missing parameter 'milestone'"

def test_etj::milestone_has_milestone():
    assert hasattr(eTJ::Milestone, "milestone")
    descriptor = None
    for klass in eTJ::Milestone.__mro__:
        if "milestone" in klass.__dict__:
            descriptor = klass.__dict__["milestone"]
            break
    assert isinstance(descriptor, property)



def test_etj::maxstart_is_not_abstract():
    assert not inspect.isabstract(eTJ::MaxStart)


def test_etj::maxstart_constructor_exists():
    assert callable(eTJ::MaxStart.__init__)


def test_etj::maxstart_constructor_args():
    sig = inspect.signature(eTJ::MaxStart.__init__)
    params = list(sig.parameters.keys())



def test_etj::maxend_is_not_abstract():
    assert not inspect.isabstract(eTJ::MaxEnd)


def test_etj::maxend_constructor_exists():
    assert callable(eTJ::MaxEnd.__init__)


def test_etj::maxend_constructor_args():
    sig = inspect.signature(eTJ::MaxEnd.__init__)
    params = list(sig.parameters.keys())



def test_etj::managers_is_not_abstract():
    assert not inspect.isabstract(eTJ::Managers)


def test_etj::managers_constructor_exists():
    assert callable(eTJ::Managers.__init__)


def test_etj::managers_constructor_args():
    sig = inspect.signature(eTJ::Managers.__init__)
    params = list(sig.parameters.keys())



def test_etj::journalattributes_is_not_abstract():
    assert not inspect.isabstract(eTJ::JournalAttributes)


def test_etj::journalattributes_constructor_exists():
    assert callable(eTJ::JournalAttributes.__init__)


def test_etj::journalattributes_constructor_args():
    sig = inspect.signature(eTJ::JournalAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "args" in params, "Missing parameter 'args'"

def test_etj::journalattributes_has_args():
    assert hasattr(eTJ::JournalAttributes, "args")
    descriptor = None
    for klass in eTJ::JournalAttributes.__mro__:
        if "args" in klass.__dict__:
            descriptor = klass.__dict__["args"]
            break
    assert isinstance(descriptor, property)



def test_etj::length_is_not_abstract():
    assert not inspect.isabstract(eTJ::Length)


def test_etj::length_constructor_exists():
    assert callable(eTJ::Length.__init__)


def test_etj::length_constructor_args():
    sig = inspect.signature(eTJ::Length.__init__)
    params = list(sig.parameters.keys())



def test_etj::left_is_not_abstract():
    assert not inspect.isabstract(eTJ::Left)


def test_etj::left_constructor_exists():
    assert callable(eTJ::Left.__init__)


def test_etj::left_constructor_args():
    sig = inspect.signature(eTJ::Left.__init__)
    params = list(sig.parameters.keys())



def test_etj::journalmode_is_not_abstract():
    assert not inspect.isabstract(eTJ::JournalMode)


def test_etj::journalmode_constructor_exists():
    assert callable(eTJ::JournalMode.__init__)


def test_etj::journalmode_constructor_args():
    sig = inspect.signature(eTJ::JournalMode.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_etj::journalmode_has_mode():
    assert hasattr(eTJ::JournalMode, "mode")
    descriptor = None
    for klass in eTJ::JournalMode.__mro__:
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



def test_etj::hidereport_is_not_abstract():
    assert not inspect.isabstract(eTJ::HideReport)


def test_etj::hidereport_constructor_exists():
    assert callable(eTJ::HideReport.__init__)


def test_etj::hidereport_constructor_args():
    sig = inspect.signature(eTJ::HideReport.__init__)
    params = list(sig.parameters.keys())



def test_etj::interval1_is_not_abstract():
    assert not inspect.isabstract(eTJ::Interval1)


def test_etj::interval1_constructor_exists():
    assert callable(eTJ::Interval1.__init__)


def test_etj::interval1_constructor_args():
    sig = inspect.signature(eTJ::Interval1.__init__)
    params = list(sig.parameters.keys())



def test_etj::includepropertiesattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::IncludePropertiesAttribute)


def test_etj::includepropertiesattribute_constructor_exists():
    assert callable(eTJ::IncludePropertiesAttribute.__init__)


def test_etj::includepropertiesattribute_constructor_args():
    sig = inspect.signature(eTJ::IncludePropertiesAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::includeproperties_is_not_abstract():
    assert not inspect.isabstract(eTJ::IncludeProperties)


def test_etj::includeproperties_constructor_exists():
    assert callable(eTJ::IncludeProperties.__init__)


def test_etj::includeproperties_constructor_args():
    sig = inspect.signature(eTJ::IncludeProperties.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_etj::includeproperties_has_importURI():
    assert hasattr(eTJ::IncludeProperties, "importURI")
    descriptor = None
    for klass in eTJ::IncludeProperties.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_etj::footer_is_not_abstract():
    assert not inspect.isabstract(eTJ::Footer)


def test_etj::footer_constructor_exists():
    assert callable(eTJ::Footer.__init__)


def test_etj::footer_constructor_args():
    sig = inspect.signature(eTJ::Footer.__init__)
    params = list(sig.parameters.keys())



def test_etj::fail_is_not_abstract():
    assert not inspect.isabstract(eTJ::Fail)


def test_etj::fail_constructor_exists():
    assert callable(eTJ::Fail.__init__)


def test_etj::fail_constructor_args():
    sig = inspect.signature(eTJ::Fail.__init__)
    params = list(sig.parameters.keys())



def test_etj::extendedtaskattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::ExtendedTaskAttribute)


def test_etj::extendedtaskattribute_constructor_exists():
    assert callable(eTJ::ExtendedTaskAttribute.__init__)


def test_etj::extendedtaskattribute_constructor_args():
    sig = inspect.signature(eTJ::ExtendedTaskAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_etj::extendedtaskattribute_has_value():
    assert hasattr(eTJ::ExtendedTaskAttribute, "value")
    descriptor = None
    for klass in eTJ::ExtendedTaskAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj::hideaccount_is_not_abstract():
    assert not inspect.isabstract(eTJ::HideAccount)


def test_etj::hideaccount_constructor_exists():
    assert callable(eTJ::HideAccount.__init__)


def test_etj::hideaccount_constructor_args():
    sig = inspect.signature(eTJ::HideAccount.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_etj::hideaccount_has_expression():
    assert hasattr(eTJ::HideAccount, "expression")
    descriptor = None
    for klass in eTJ::HideAccount.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_etj::header_is_not_abstract():
    assert not inspect.isabstract(eTJ::Header)


def test_etj::header_constructor_exists():
    assert callable(eTJ::Header.__init__)


def test_etj::header_constructor_args():
    sig = inspect.signature(eTJ::Header.__init__)
    params = list(sig.parameters.keys())



def test_etj::gaplength_is_not_abstract():
    assert not inspect.isabstract(eTJ::GapLength)


def test_etj::gaplength_constructor_exists():
    assert callable(eTJ::GapLength.__init__)


def test_etj::gaplength_constructor_args():
    sig = inspect.signature(eTJ::GapLength.__init__)
    params = list(sig.parameters.keys())



def test_etj::gapduration_is_not_abstract():
    assert not inspect.isabstract(eTJ::GapDuration)


def test_etj::gapduration_constructor_exists():
    assert callable(eTJ::GapDuration.__init__)


def test_etj::gapduration_constructor_args():
    sig = inspect.signature(eTJ::GapDuration.__init__)
    params = list(sig.parameters.keys())



def test_etj::function_is_not_abstract():
    assert not inspect.isabstract(eTJ::Function)


def test_etj::function_constructor_exists():
    assert callable(eTJ::Function.__init__)


def test_etj::function_constructor_args():
    sig = inspect.signature(eTJ::Function.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "parentId" in params, "Missing parameter 'parentId'"
    assert "distance" in params, "Missing parameter 'distance'"

def test_etj::function_has_level():
    assert hasattr(eTJ::Function, "level")
    descriptor = None
    for klass in eTJ::Function.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_etj::function_has_parentId():
    assert hasattr(eTJ::Function, "parentId")
    descriptor = None
    for klass in eTJ::Function.__mro__:
        if "parentId" in klass.__dict__:
            descriptor = klass.__dict__["parentId"]
            break
    assert isinstance(descriptor, property)

def test_etj::function_has_distance():
    assert hasattr(eTJ::Function, "distance")
    descriptor = None
    for klass in eTJ::Function.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
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



def test_etj::scenarioical_is_not_abstract():
    assert not inspect.isabstract(eTJ::ScenarioIcal)


def test_etj::scenarioical_constructor_exists():
    assert callable(eTJ::ScenarioIcal.__init__)


def test_etj::scenarioical_constructor_args():
    sig = inspect.signature(eTJ::ScenarioIcal.__init__)
    params = list(sig.parameters.keys())



def test_etj::hidejournalentry_is_not_abstract():
    assert not inspect.isabstract(eTJ::HideJournalEntry)


def test_etj::hidejournalentry_constructor_exists():
    assert callable(eTJ::HideJournalEntry.__init__)


def test_etj::hidejournalentry_constructor_args():
    sig = inspect.signature(eTJ::HideJournalEntry.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_etj::hidejournalentry_has_expression():
    assert hasattr(eTJ::HideJournalEntry, "expression")
    descriptor = None
    for klass in eTJ::HideJournalEntry.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_etj::email_is_not_abstract():
    assert not inspect.isabstract(eTJ::Email)


def test_etj::email_constructor_exists():
    assert callable(eTJ::Email.__init__)


def test_etj::email_constructor_args():
    sig = inspect.signature(eTJ::Email.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_etj::email_has_address():
    assert hasattr(eTJ::Email, "address")
    descriptor = None
    for klass in eTJ::Email.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_etj::effort_is_not_abstract():
    assert not inspect.isabstract(eTJ::Effort)


def test_etj::effort_constructor_exists():
    assert callable(eTJ::Effort.__init__)


def test_etj::effort_constructor_args():
    sig = inspect.signature(eTJ::Effort.__init__)
    params = list(sig.parameters.keys())



def test_etj::efficiency_is_not_abstract():
    assert not inspect.isabstract(eTJ::Efficiency)


def test_etj::efficiency_constructor_exists():
    assert callable(eTJ::Efficiency.__init__)


def test_etj::efficiency_constructor_args():
    sig = inspect.signature(eTJ::Efficiency.__init__)
    params = list(sig.parameters.keys())
    assert "efficiency" in params, "Missing parameter 'efficiency'"

def test_etj::efficiency_has_efficiency():
    assert hasattr(eTJ::Efficiency, "efficiency")
    descriptor = None
    for klass in eTJ::Efficiency.__mro__:
        if "efficiency" in klass.__dict__:
            descriptor = klass.__dict__["efficiency"]
            break
    assert isinstance(descriptor, property)



def test_etj::durationquantity_is_not_abstract():
    assert not inspect.isabstract(eTJ::DurationQuantity)


def test_etj::durationquantity_constructor_exists():
    assert callable(eTJ::DurationQuantity.__init__)


def test_etj::durationquantity_constructor_args():
    sig = inspect.signature(eTJ::DurationQuantity.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_etj::durationquantity_has_value():
    assert hasattr(eTJ::DurationQuantity, "value")
    descriptor = None
    for klass in eTJ::DurationQuantity.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_etj::durationquantity_has_unit():
    assert hasattr(eTJ::DurationQuantity, "unit")
    descriptor = None
    for klass in eTJ::DurationQuantity.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_etj::duration_is_not_abstract():
    assert not inspect.isabstract(eTJ::Duration)


def test_etj::duration_constructor_exists():
    assert callable(eTJ::Duration.__init__)


def test_etj::duration_constructor_args():
    sig = inspect.signature(eTJ::Duration.__init__)
    params = list(sig.parameters.keys())



def test_statustimesheetattribute_is_not_abstract():
    assert not inspect.isabstract(StatusTimesheetAttribute)


def test_statustimesheetattribute_constructor_exists():
    assert callable(StatusTimesheetAttribute.__init__)


def test_statustimesheetattribute_constructor_args():
    sig = inspect.signature(StatusTimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::taskdependency_is_not_abstract():
    assert not inspect.isabstract(eTJ::TaskDependency)


def test_etj::taskdependency_constructor_exists():
    assert callable(eTJ::TaskDependency.__init__)


def test_etj::taskdependency_constructor_args():
    sig = inspect.signature(eTJ::TaskDependency.__init__)
    params = list(sig.parameters.keys())
    assert "policy" in params, "Missing parameter 'policy'"

def test_etj::taskdependency_has_policy():
    assert hasattr(eTJ::TaskDependency, "policy")
    descriptor = None
    for klass in eTJ::TaskDependency.__mro__:
        if "policy" in klass.__dict__:
            descriptor = klass.__dict__["policy"]
            break
    assert isinstance(descriptor, property)



def test_etj::depends_is_not_abstract():
    assert not inspect.isabstract(eTJ::Depends)


def test_etj::depends_constructor_exists():
    assert callable(eTJ::Depends.__init__)


def test_etj::depends_constructor_args():
    sig = inspect.signature(eTJ::Depends.__init__)
    params = list(sig.parameters.keys())



def test_etj::extendedresourceattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::ExtendedResourceAttribute)


def test_etj::extendedresourceattribute_constructor_exists():
    assert callable(eTJ::ExtendedResourceAttribute.__init__)


def test_etj::extendedresourceattribute_constructor_args():
    sig = inspect.signature(eTJ::ExtendedResourceAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_etj::extendedresourceattribute_has_value():
    assert hasattr(eTJ::ExtendedResourceAttribute, "value")
    descriptor = None
    for klass in eTJ::ExtendedResourceAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj::extend_is_not_abstract():
    assert not inspect.isabstract(eTJ::Extend)


def test_etj::extend_constructor_exists():
    assert callable(eTJ::Extend.__init__)


def test_etj::extend_constructor_args():
    sig = inspect.signature(eTJ::Extend.__init__)
    params = list(sig.parameters.keys())
    assert "inherit" in params, "Missing parameter 'inherit'"
    assert "description" in params, "Missing parameter 'description'"
    assert "scenariospecific" in params, "Missing parameter 'scenariospecific'"
    assert "name" in params, "Missing parameter 'name'"

def test_etj::extend_has_inherit():
    assert hasattr(eTJ::Extend, "inherit")
    descriptor = None
    for klass in eTJ::Extend.__mro__:
        if "inherit" in klass.__dict__:
            descriptor = klass.__dict__["inherit"]
            break
    assert isinstance(descriptor, property)

def test_etj::extend_has_description():
    assert hasattr(eTJ::Extend, "description")
    descriptor = None
    for klass in eTJ::Extend.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_etj::extend_has_scenariospecific():
    assert hasattr(eTJ::Extend, "scenariospecific")
    descriptor = None
    for klass in eTJ::Extend.__mro__:
        if "scenariospecific" in klass.__dict__:
            descriptor = klass.__dict__["scenariospecific"]
            break
    assert isinstance(descriptor, property)

def test_etj::extend_has_name():
    assert hasattr(eTJ::Extend, "name")
    descriptor = None
    for klass in eTJ::Extend.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_etj::epilog_is_not_abstract():
    assert not inspect.isabstract(eTJ::Epilog)


def test_etj::epilog_constructor_exists():
    assert callable(eTJ::Epilog.__init__)


def test_etj::epilog_constructor_args():
    sig = inspect.signature(eTJ::Epilog.__init__)
    params = list(sig.parameters.keys())



def test_etj::endcredit_is_not_abstract():
    assert not inspect.isabstract(eTJ::EndCredit)


def test_etj::endcredit_constructor_exists():
    assert callable(eTJ::EndCredit.__init__)


def test_etj::endcredit_constructor_args():
    sig = inspect.signature(eTJ::EndCredit.__init__)
    params = list(sig.parameters.keys())
    assert "credit" in params, "Missing parameter 'credit'"

def test_etj::endcredit_has_credit():
    assert hasattr(eTJ::EndCredit, "credit")
    descriptor = None
    for klass in eTJ::EndCredit.__mro__:
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



def test_etj::remaining_is_not_abstract():
    assert not inspect.isabstract(eTJ::Remaining)


def test_etj::remaining_constructor_exists():
    assert callable(eTJ::Remaining.__init__)


def test_etj::remaining_constructor_args():
    sig = inspect.signature(eTJ::Remaining.__init__)
    params = list(sig.parameters.keys())



def test_etj::work_is_not_abstract():
    assert not inspect.isabstract(eTJ::Work)


def test_etj::work_constructor_exists():
    assert callable(eTJ::Work.__init__)


def test_etj::work_constructor_args():
    sig = inspect.signature(eTJ::Work.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "value" in params, "Missing parameter 'value'"

def test_etj::work_has_unit():
    assert hasattr(eTJ::Work, "unit")
    descriptor = None
    for klass in eTJ::Work.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_etj::work_has_value():
    assert hasattr(eTJ::Work, "value")
    descriptor = None
    for klass in eTJ::Work.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj::priority_is_not_abstract():
    assert not inspect.isabstract(eTJ::Priority)


def test_etj::priority_constructor_exists():
    assert callable(eTJ::Priority.__init__)


def test_etj::priority_constructor_args():
    sig = inspect.signature(eTJ::Priority.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_etj::priority_has_priority():
    assert hasattr(eTJ::Priority, "priority")
    descriptor = None
    for klass in eTJ::Priority.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_statussheetreportattribute_is_not_abstract():
    assert not inspect.isabstract(StatusSheetReportAttribute)


def test_statussheetreportattribute_constructor_exists():
    assert callable(StatusSheetReportAttribute.__init__)


def test_statussheetreportattribute_constructor_args():
    sig = inspect.signature(StatusSheetReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::sortresources_is_not_abstract():
    assert not inspect.isabstract(eTJ::SortResources)


def test_etj::sortresources_constructor_exists():
    assert callable(eTJ::SortResources.__init__)


def test_etj::sortresources_constructor_args():
    sig = inspect.signature(eTJ::SortResources.__init__)
    params = list(sig.parameters.keys())



def test_etj::sorttasks_is_not_abstract():
    assert not inspect.isabstract(eTJ::SortTasks)


def test_etj::sorttasks_constructor_exists():
    assert callable(eTJ::SortTasks.__init__)


def test_etj::sorttasks_constructor_args():
    sig = inspect.signature(eTJ::SortTasks.__init__)
    params = list(sig.parameters.keys())



def test_nikureportattribute_is_not_abstract():
    assert not inspect.isabstract(NikuReportAttribute)


def test_nikureportattribute_constructor_exists():
    assert callable(NikuReportAttribute.__init__)


def test_nikureportattribute_constructor_args():
    sig = inspect.signature(NikuReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::timeoff_is_not_abstract():
    assert not inspect.isabstract(eTJ::Timeoff)


def test_etj::timeoff_constructor_exists():
    assert callable(eTJ::Timeoff.__init__)


def test_etj::timeoff_constructor_args():
    sig = inspect.signature(eTJ::Timeoff.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_etj::timeoff_has_name():
    assert hasattr(eTJ::Timeoff, "name")
    descriptor = None
    for klass in eTJ::Timeoff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_etj::timeoff_has_id():
    assert hasattr(eTJ::Timeoff, "id")
    descriptor = None
    for klass in eTJ::Timeoff.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_etj::headline_is_not_abstract():
    assert not inspect.isabstract(eTJ::Headline)


def test_etj::headline_constructor_exists():
    assert callable(eTJ::Headline.__init__)


def test_etj::headline_constructor_args():
    sig = inspect.signature(eTJ::Headline.__init__)
    params = list(sig.parameters.keys())



def test_etj::formats_is_not_abstract():
    assert not inspect.isabstract(eTJ::Formats)


def test_etj::formats_constructor_exists():
    assert callable(eTJ::Formats.__init__)


def test_etj::formats_constructor_args():
    sig = inspect.signature(eTJ::Formats.__init__)
    params = list(sig.parameters.keys())
    assert "formats" in params, "Missing parameter 'formats'"

def test_etj::formats_has_formats():
    assert hasattr(eTJ::Formats, "formats")
    descriptor = None
    for klass in eTJ::Formats.__mro__:
        if "formats" in klass.__dict__:
            descriptor = klass.__dict__["formats"]
            break
    assert isinstance(descriptor, property)



def test_etj::accountshare_is_not_abstract():
    assert not inspect.isabstract(eTJ::AccountShare)


def test_etj::accountshare_constructor_exists():
    assert callable(eTJ::AccountShare.__init__)


def test_etj::accountshare_constructor_args():
    sig = inspect.signature(eTJ::AccountShare.__init__)
    params = list(sig.parameters.keys())
    assert "share" in params, "Missing parameter 'share'"

def test_etj::accountshare_has_share():
    assert hasattr(eTJ::AccountShare, "share")
    descriptor = None
    for klass in eTJ::AccountShare.__mro__:
        if "share" in klass.__dict__:
            descriptor = klass.__dict__["share"]
            break
    assert isinstance(descriptor, property)



def test_etj::chargeset_is_not_abstract():
    assert not inspect.isabstract(eTJ::ChargeSet)


def test_etj::chargeset_constructor_exists():
    assert callable(eTJ::ChargeSet.__init__)


def test_etj::chargeset_constructor_args():
    sig = inspect.signature(eTJ::ChargeSet.__init__)
    params = list(sig.parameters.keys())



def test_etj::charge_is_not_abstract():
    assert not inspect.isabstract(eTJ::Charge)


def test_etj::charge_constructor_exists():
    assert callable(eTJ::Charge.__init__)


def test_etj::charge_constructor_args():
    sig = inspect.signature(eTJ::Charge.__init__)
    params = list(sig.parameters.keys())
    assert "applies" in params, "Missing parameter 'applies'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_etj::charge_has_applies():
    assert hasattr(eTJ::Charge, "applies")
    descriptor = None
    for klass in eTJ::Charge.__mro__:
        if "applies" in klass.__dict__:
            descriptor = klass.__dict__["applies"]
            break
    assert isinstance(descriptor, property)

def test_etj::charge_has_amount():
    assert hasattr(eTJ::Charge, "amount")
    descriptor = None
    for klass in eTJ::Charge.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_etj::center_is_not_abstract():
    assert not inspect.isabstract(eTJ::Center)


def test_etj::center_constructor_exists():
    assert callable(eTJ::Center.__init__)


def test_etj::center_constructor_args():
    sig = inspect.signature(eTJ::Center.__init__)
    params = list(sig.parameters.keys())



def test_etj::rgb_is_not_abstract():
    assert not inspect.isabstract(eTJ::RGB)


def test_etj::rgb_constructor_exists():
    assert callable(eTJ::RGB.__init__)


def test_etj::rgb_constructor_args():
    sig = inspect.signature(eTJ::RGB.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_etj::rgb_has_value():
    assert hasattr(eTJ::RGB, "value")
    descriptor = None
    for klass in eTJ::RGB.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_etj::logicalexpression_is_not_abstract():
    assert not inspect.isabstract(eTJ::LogicalExpression)


def test_etj::logicalexpression_constructor_exists():
    assert callable(eTJ::LogicalExpression.__init__)


def test_etj::logicalexpression_constructor_args():
    sig = inspect.signature(eTJ::LogicalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_etj::logicalexpression_has_op():
    assert hasattr(eTJ::LogicalExpression, "op")
    descriptor = None
    for klass in eTJ::LogicalExpression.__mro__:
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



def test_etj::extendedresourceattributecolumn_is_not_abstract():
    assert not inspect.isabstract(eTJ::ExtendedResourceAttributeColumn)


def test_etj::extendedresourceattributecolumn_constructor_exists():
    assert callable(eTJ::ExtendedResourceAttributeColumn.__init__)


def test_etj::extendedresourceattributecolumn_constructor_args():
    sig = inspect.signature(eTJ::ExtendedResourceAttributeColumn.__init__)
    params = list(sig.parameters.keys())



def test_etj::listtype_is_not_abstract():
    assert not inspect.isabstract(eTJ::ListType)


def test_etj::listtype_constructor_exists():
    assert callable(eTJ::ListType.__init__)


def test_etj::listtype_constructor_args():
    sig = inspect.signature(eTJ::ListType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_etj::listtype_has_type():
    assert hasattr(eTJ::ListType, "type")
    descriptor = None
    for klass in eTJ::ListType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_etj::halign_is_not_abstract():
    assert not inspect.isabstract(eTJ::HAlign)


def test_etj::halign_constructor_exists():
    assert callable(eTJ::HAlign.__init__)


def test_etj::halign_constructor_args():
    sig = inspect.signature(eTJ::HAlign.__init__)
    params = list(sig.parameters.keys())
    assert "justification" in params, "Missing parameter 'justification'"

def test_etj::halign_has_justification():
    assert hasattr(eTJ::HAlign, "justification")
    descriptor = None
    for klass in eTJ::HAlign.__mro__:
        if "justification" in klass.__dict__:
            descriptor = klass.__dict__["justification"]
            break
    assert isinstance(descriptor, property)



def test_etj::fontcolor_is_not_abstract():
    assert not inspect.isabstract(eTJ::FontColor)


def test_etj::fontcolor_constructor_exists():
    assert callable(eTJ::FontColor.__init__)


def test_etj::fontcolor_constructor_args():
    sig = inspect.signature(eTJ::FontColor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_etj::fontcolor_has_color():
    assert hasattr(eTJ::FontColor, "color")
    descriptor = None
    for klass in eTJ::FontColor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_etj::celltext_is_not_abstract():
    assert not inspect.isabstract(eTJ::CellText)


def test_etj::celltext_constructor_exists():
    assert callable(eTJ::CellText.__init__)


def test_etj::celltext_constructor_args():
    sig = inspect.signature(eTJ::CellText.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_etj::celltext_has_text():
    assert hasattr(eTJ::CellText, "text")
    descriptor = None
    for klass in eTJ::CellText.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_etj::tooltip_is_not_abstract():
    assert not inspect.isabstract(eTJ::ToolTip)


def test_etj::tooltip_constructor_exists():
    assert callable(eTJ::ToolTip.__init__)


def test_etj::tooltip_constructor_args():
    sig = inspect.signature(eTJ::ToolTip.__init__)
    params = list(sig.parameters.keys())
    assert "tip" in params, "Missing parameter 'tip'"

def test_etj::tooltip_has_tip():
    assert hasattr(eTJ::ToolTip, "tip")
    descriptor = None
    for klass in eTJ::ToolTip.__mro__:
        if "tip" in klass.__dict__:
            descriptor = klass.__dict__["tip"]
            break
    assert isinstance(descriptor, property)



def test_etj::title_is_not_abstract():
    assert not inspect.isabstract(eTJ::Title)


def test_etj::title_constructor_exists():
    assert callable(eTJ::Title.__init__)


def test_etj::title_constructor_args():
    sig = inspect.signature(eTJ::Title.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_etj::title_has_title():
    assert hasattr(eTJ::Title, "title")
    descriptor = None
    for klass in eTJ::Title.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_etj::listitem_is_not_abstract():
    assert not inspect.isabstract(eTJ::ListItem)


def test_etj::listitem_constructor_exists():
    assert callable(eTJ::ListItem.__init__)


def test_etj::listitem_constructor_args():
    sig = inspect.signature(eTJ::ListItem.__init__)
    params = list(sig.parameters.keys())



def test_etj::width_is_not_abstract():
    assert not inspect.isabstract(eTJ::Width)


def test_etj::width_constructor_exists():
    assert callable(eTJ::Width.__init__)


def test_etj::width_constructor_args():
    sig = inspect.signature(eTJ::Width.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"

def test_etj::width_has_width():
    assert hasattr(eTJ::Width, "width")
    descriptor = None
    for klass in eTJ::Width.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_etj::scale_is_not_abstract():
    assert not inspect.isabstract(eTJ::Scale)


def test_etj::scale_constructor_exists():
    assert callable(eTJ::Scale.__init__)


def test_etj::scale_constructor_args():
    sig = inspect.signature(eTJ::Scale.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"

def test_etj::scale_has_scale():
    assert hasattr(eTJ::Scale, "scale")
    descriptor = None
    for klass in eTJ::Scale.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_etj::cellcolor_is_not_abstract():
    assert not inspect.isabstract(eTJ::CellColor)


def test_etj::cellcolor_constructor_exists():
    assert callable(eTJ::CellColor.__init__)


def test_etj::cellcolor_constructor_args():
    sig = inspect.signature(eTJ::CellColor.__init__)
    params = list(sig.parameters.keys())



def test_etj::caption_is_not_abstract():
    assert not inspect.isabstract(eTJ::Caption)


def test_etj::caption_constructor_exists():
    assert callable(eTJ::Caption.__init__)


def test_etj::caption_constructor_args():
    sig = inspect.signature(eTJ::Caption.__init__)
    params = list(sig.parameters.keys())



def test_exportattribute_is_not_abstract():
    assert not inspect.isabstract(ExportAttribute)


def test_exportattribute_constructor_exists():
    assert callable(ExportAttribute.__init__)


def test_exportattribute_constructor_args():
    sig = inspect.signature(ExportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::rolluptask_is_not_abstract():
    assert not inspect.isabstract(eTJ::RollupTask)


def test_etj::rolluptask_constructor_exists():
    assert callable(eTJ::RollupTask.__init__)


def test_etj::rolluptask_constructor_args():
    sig = inspect.signature(eTJ::RollupTask.__init__)
    params = list(sig.parameters.keys())



def test_etj::taskattributes_is_not_abstract():
    assert not inspect.isabstract(eTJ::TaskAttributes)


def test_etj::taskattributes_constructor_exists():
    assert callable(eTJ::TaskAttributes.__init__)


def test_etj::taskattributes_constructor_args():
    sig = inspect.signature(eTJ::TaskAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "minend" in params, "Missing parameter 'minend'"
    assert "all" in params, "Missing parameter 'all'"
    assert "responsible" in params, "Missing parameter 'responsible'"
    assert "note" in params, "Missing parameter 'note'"
    assert "maxend" in params, "Missing parameter 'maxend'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "minstart" in params, "Missing parameter 'minstart'"
    assert "complete" in params, "Missing parameter 'complete'"
    assert "depends" in params, "Missing parameter 'depends'"
    assert "flags" in params, "Missing parameter 'flags'"
    assert "maxstart" in params, "Missing parameter 'maxstart'"
    assert "booking" in params, "Missing parameter 'booking'"
    assert "none" in params, "Missing parameter 'none'"

def test_etj::taskattributes_has_minend():
    assert hasattr(eTJ::TaskAttributes, "minend")
    descriptor = None
    for klass in eTJ::TaskAttributes.__mro__:
        if "minend" in klass.__dict__:
            descriptor = klass.__dict__["minend"]
            break
    assert isinstance(descriptor, property)

def test_etj::taskattributes_has_all():
    assert hasattr(eTJ::TaskAttributes, "all")
    descriptor = None
    for klass in eTJ::TaskAttributes.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_etj::taskattributes_has_responsible():
    assert hasattr(eTJ::TaskAttributes, "responsible")
    descriptor = None
    for klass in eTJ::TaskAttributes.__mro__:
        if "responsible" in klass.__dict__:
            descriptor = klass.__dict__["responsible"]
            break
    assert isinstance(descriptor, property)

def test_etj::taskattributes_has_note():
    assert hasattr(eTJ::TaskAttributes, "note")
    descriptor = None
    for klass in eTJ::TaskAttributes.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_etj::taskattributes_has_maxend():
    assert hasattr(eTJ::TaskAttributes, "maxend")
    descriptor = None
    for klass in eTJ::TaskAttributes.__mro__:
        if "maxend" in klass.__dict__:
            descriptor = klass.__dict__["maxend"]
            break
    assert isinstance(descriptor, property)

def test_etj::taskattributes_has_priority():
    assert hasattr(eTJ::TaskAttributes, "priority")
    descriptor = None
    for klass in eTJ::TaskAttributes.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_etj::taskattributes_has_minstart():
    assert hasattr(eTJ::TaskAttributes, "minstart")
    descriptor = None
    for klass in eTJ::TaskAttributes.__mro__:
        if "minstart" in klass.__dict__:
            descriptor = klass.__dict__["minstart"]
            break
    assert isinstance(descriptor, property)

def test_etj::taskattributes_has_complete():
    assert hasattr(eTJ::TaskAttributes, "complete")
    descriptor = None
    for klass in eTJ::TaskAttributes.__mro__:
        if "complete" in klass.__dict__:
            descriptor = klass.__dict__["complete"]
            break
    assert isinstance(descriptor, property)

def test_etj::taskattributes_has_depends():
    assert hasattr(eTJ::TaskAttributes, "depends")
    descriptor = None
    for klass in eTJ::TaskAttributes.__mro__:
        if "depends" in klass.__dict__:
            descriptor = klass.__dict__["depends"]
            break
    assert isinstance(descriptor, property)

def test_etj::taskattributes_has_flags():
    assert hasattr(eTJ::TaskAttributes, "flags")
    descriptor = None
    for klass in eTJ::TaskAttributes.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)

def test_etj::taskattributes_has_maxstart():
    assert hasattr(eTJ::TaskAttributes, "maxstart")
    descriptor = None
    for klass in eTJ::TaskAttributes.__mro__:
        if "maxstart" in klass.__dict__:
            descriptor = klass.__dict__["maxstart"]
            break
    assert isinstance(descriptor, property)

def test_etj::taskattributes_has_booking():
    assert hasattr(eTJ::TaskAttributes, "booking")
    descriptor = None
    for klass in eTJ::TaskAttributes.__mro__:
        if "booking" in klass.__dict__:
            descriptor = klass.__dict__["booking"]
            break
    assert isinstance(descriptor, property)

def test_etj::taskattributes_has_none():
    assert hasattr(eTJ::TaskAttributes, "none")
    descriptor = None
    for klass in eTJ::TaskAttributes.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)



def test_etj::period_is_not_abstract():
    assert not inspect.isabstract(eTJ::Period)


def test_etj::period_constructor_exists():
    assert callable(eTJ::Period.__init__)


def test_etj::period_constructor_args():
    sig = inspect.signature(eTJ::Period.__init__)
    params = list(sig.parameters.keys())



def test_etj::start_is_not_abstract():
    assert not inspect.isabstract(eTJ::Start)


def test_etj::start_constructor_exists():
    assert callable(eTJ::Start.__init__)


def test_etj::start_constructor_args():
    sig = inspect.signature(eTJ::Start.__init__)
    params = list(sig.parameters.keys())



def test_etj::scenarios_is_not_abstract():
    assert not inspect.isabstract(eTJ::Scenarios)


def test_etj::scenarios_constructor_exists():
    assert callable(eTJ::Scenarios.__init__)


def test_etj::scenarios_constructor_args():
    sig = inspect.signature(eTJ::Scenarios.__init__)
    params = list(sig.parameters.keys())



def test_etj::rollupresource_is_not_abstract():
    assert not inspect.isabstract(eTJ::RollupResource)


def test_etj::rollupresource_constructor_exists():
    assert callable(eTJ::RollupResource.__init__)


def test_etj::rollupresource_constructor_args():
    sig = inspect.signature(eTJ::RollupResource.__init__)
    params = list(sig.parameters.keys())



def test_etj::resourceattributes_is_not_abstract():
    assert not inspect.isabstract(eTJ::ResourceAttributes)


def test_etj::resourceattributes_constructor_exists():
    assert callable(eTJ::ResourceAttributes.__init__)


def test_etj::resourceattributes_constructor_args():
    sig = inspect.signature(eTJ::ResourceAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"
    assert "workingHours" in params, "Missing parameter 'workingHours'"
    assert "booking" in params, "Missing parameter 'booking'"
    assert "none" in params, "Missing parameter 'none'"
    assert "vacation" in params, "Missing parameter 'vacation'"

def test_etj::resourceattributes_has_all():
    assert hasattr(eTJ::ResourceAttributes, "all")
    descriptor = None
    for klass in eTJ::ResourceAttributes.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_etj::resourceattributes_has_workingHours():
    assert hasattr(eTJ::ResourceAttributes, "workingHours")
    descriptor = None
    for klass in eTJ::ResourceAttributes.__mro__:
        if "workingHours" in klass.__dict__:
            descriptor = klass.__dict__["workingHours"]
            break
    assert isinstance(descriptor, property)

def test_etj::resourceattributes_has_booking():
    assert hasattr(eTJ::ResourceAttributes, "booking")
    descriptor = None
    for klass in eTJ::ResourceAttributes.__mro__:
        if "booking" in klass.__dict__:
            descriptor = klass.__dict__["booking"]
            break
    assert isinstance(descriptor, property)

def test_etj::resourceattributes_has_none():
    assert hasattr(eTJ::ResourceAttributes, "none")
    descriptor = None
    for klass in eTJ::ResourceAttributes.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_etj::resourceattributes_has_vacation():
    assert hasattr(eTJ::ResourceAttributes, "vacation")
    descriptor = None
    for klass in eTJ::ResourceAttributes.__mro__:
        if "vacation" in klass.__dict__:
            descriptor = klass.__dict__["vacation"]
            break
    assert isinstance(descriptor, property)



def test_etj::hidetask_is_not_abstract():
    assert not inspect.isabstract(eTJ::HideTask)


def test_etj::hidetask_constructor_exists():
    assert callable(eTJ::HideTask.__init__)


def test_etj::hidetask_constructor_args():
    sig = inspect.signature(eTJ::HideTask.__init__)
    params = list(sig.parameters.keys())



def test_etj::hideresource_is_not_abstract():
    assert not inspect.isabstract(eTJ::HideResource)


def test_etj::hideresource_constructor_exists():
    assert callable(eTJ::HideResource.__init__)


def test_etj::hideresource_constructor_args():
    sig = inspect.signature(eTJ::HideResource.__init__)
    params = list(sig.parameters.keys())



def test_etj::end_is_not_abstract():
    assert not inspect.isabstract(eTJ::End)


def test_etj::end_constructor_exists():
    assert callable(eTJ::End.__init__)


def test_etj::end_constructor_args():
    sig = inspect.signature(eTJ::End.__init__)
    params = list(sig.parameters.keys())



def test_etj::definitions_is_not_abstract():
    assert not inspect.isabstract(eTJ::Definitions)


def test_etj::definitions_constructor_exists():
    assert callable(eTJ::Definitions.__init__)


def test_etj::definitions_constructor_args():
    sig = inspect.signature(eTJ::Definitions.__init__)
    params = list(sig.parameters.keys())
    assert "none" in params, "Missing parameter 'none'"
    assert "all" in params, "Missing parameter 'all'"

def test_etj::definitions_has_none():
    assert hasattr(eTJ::Definitions, "none")
    descriptor = None
    for klass in eTJ::Definitions.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_etj::definitions_has_all():
    assert hasattr(eTJ::Definitions, "all")
    descriptor = None
    for klass in eTJ::Definitions.__mro__:
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



def test_etj::monthlymin_is_not_abstract():
    assert not inspect.isabstract(eTJ::MonthlyMin)


def test_etj::monthlymin_constructor_exists():
    assert callable(eTJ::MonthlyMin.__init__)


def test_etj::monthlymin_constructor_args():
    sig = inspect.signature(eTJ::MonthlyMin.__init__)
    params = list(sig.parameters.keys())



def test_etj::dailymin_is_not_abstract():
    assert not inspect.isabstract(eTJ::DailyMin)


def test_etj::dailymin_constructor_exists():
    assert callable(eTJ::DailyMin.__init__)


def test_etj::dailymin_constructor_args():
    sig = inspect.signature(eTJ::DailyMin.__init__)
    params = list(sig.parameters.keys())



def test_etj::monthlymax_is_not_abstract():
    assert not inspect.isabstract(eTJ::MonthlyMax)


def test_etj::monthlymax_constructor_exists():
    assert callable(eTJ::MonthlyMax.__init__)


def test_etj::monthlymax_constructor_args():
    sig = inspect.signature(eTJ::MonthlyMax.__init__)
    params = list(sig.parameters.keys())



def test_etj::maximum_is_not_abstract():
    assert not inspect.isabstract(eTJ::Maximum)


def test_etj::maximum_constructor_exists():
    assert callable(eTJ::Maximum.__init__)


def test_etj::maximum_constructor_args():
    sig = inspect.signature(eTJ::Maximum.__init__)
    params = list(sig.parameters.keys())



def test_etj::weeklymax_is_not_abstract():
    assert not inspect.isabstract(eTJ::WeeklyMax)


def test_etj::weeklymax_constructor_exists():
    assert callable(eTJ::WeeklyMax.__init__)


def test_etj::weeklymax_constructor_args():
    sig = inspect.signature(eTJ::WeeklyMax.__init__)
    params = list(sig.parameters.keys())



def test_etj::minimum_is_not_abstract():
    assert not inspect.isabstract(eTJ::Minimum)


def test_etj::minimum_constructor_exists():
    assert callable(eTJ::Minimum.__init__)


def test_etj::minimum_constructor_args():
    sig = inspect.signature(eTJ::Minimum.__init__)
    params = list(sig.parameters.keys())



def test_etj::weeklymin_is_not_abstract():
    assert not inspect.isabstract(eTJ::WeeklyMin)


def test_etj::weeklymin_constructor_exists():
    assert callable(eTJ::WeeklyMin.__init__)


def test_etj::weeklymin_constructor_args():
    sig = inspect.signature(eTJ::WeeklyMin.__init__)
    params = list(sig.parameters.keys())



def test_etj::dailymax_is_not_abstract():
    assert not inspect.isabstract(eTJ::DailyMax)


def test_etj::dailymax_constructor_exists():
    assert callable(eTJ::DailyMax.__init__)


def test_etj::dailymax_constructor_args():
    sig = inspect.signature(eTJ::DailyMax.__init__)
    params = list(sig.parameters.keys())



def test_projectattribute_is_not_abstract():
    assert not inspect.isabstract(ProjectAttribute)


def test_projectattribute_constructor_exists():
    assert callable(ProjectAttribute.__init__)


def test_projectattribute_constructor_args():
    sig = inspect.signature(ProjectAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::shorttimeformat_is_not_abstract():
    assert not inspect.isabstract(eTJ::ShortTimeFormat)


def test_etj::shorttimeformat_constructor_exists():
    assert callable(eTJ::ShortTimeFormat.__init__)


def test_etj::shorttimeformat_constructor_args():
    sig = inspect.signature(eTJ::ShortTimeFormat.__init__)
    params = list(sig.parameters.keys())
    assert "shortTimeFormat" in params, "Missing parameter 'shortTimeFormat'"

def test_etj::shorttimeformat_has_shortTimeFormat():
    assert hasattr(eTJ::ShortTimeFormat, "shortTimeFormat")
    descriptor = None
    for klass in eTJ::ShortTimeFormat.__mro__:
        if "shortTimeFormat" in klass.__dict__:
            descriptor = klass.__dict__["shortTimeFormat"]
            break
    assert isinstance(descriptor, property)



def test_etj::workinghours_is_not_abstract():
    assert not inspect.isabstract(eTJ::WorkingHours)


def test_etj::workinghours_constructor_exists():
    assert callable(eTJ::WorkingHours.__init__)


def test_etj::workinghours_constructor_args():
    sig = inspect.signature(eTJ::WorkingHours.__init__)
    params = list(sig.parameters.keys())
    assert "off" in params, "Missing parameter 'off'"

def test_etj::workinghours_has_off():
    assert hasattr(eTJ::WorkingHours, "off")
    descriptor = None
    for klass in eTJ::WorkingHours.__mro__:
        if "off" in klass.__dict__:
            descriptor = klass.__dict__["off"]
            break
    assert isinstance(descriptor, property)



def test_etj::include_is_not_abstract():
    assert not inspect.isabstract(eTJ::Include)


def test_etj::include_constructor_exists():
    assert callable(eTJ::Include.__init__)


def test_etj::include_constructor_args():
    sig = inspect.signature(eTJ::Include.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_etj::include_has_importURI():
    assert hasattr(eTJ::Include, "importURI")
    descriptor = None
    for klass in eTJ::Include.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_etj::timingresolution_is_not_abstract():
    assert not inspect.isabstract(eTJ::TimingResolution)


def test_etj::timingresolution_constructor_exists():
    assert callable(eTJ::TimingResolution.__init__)


def test_etj::timingresolution_constructor_args():
    sig = inspect.signature(eTJ::TimingResolution.__init__)
    params = list(sig.parameters.keys())
    assert "timingResolution" in params, "Missing parameter 'timingResolution'"

def test_etj::timingresolution_has_timingResolution():
    assert hasattr(eTJ::TimingResolution, "timingResolution")
    descriptor = None
    for klass in eTJ::TimingResolution.__mro__:
        if "timingResolution" in klass.__dict__:
            descriptor = klass.__dict__["timingResolution"]
            break
    assert isinstance(descriptor, property)



def test_etj::trackingscenario_is_not_abstract():
    assert not inspect.isabstract(eTJ::TrackingScenario)


def test_etj::trackingscenario_constructor_exists():
    assert callable(eTJ::TrackingScenario.__init__)


def test_etj::trackingscenario_constructor_args():
    sig = inspect.signature(eTJ::TrackingScenario.__init__)
    params = list(sig.parameters.keys())



def test_etj::weekstarts_is_not_abstract():
    assert not inspect.isabstract(eTJ::WeekStarts)


def test_etj::weekstarts_constructor_exists():
    assert callable(eTJ::WeekStarts.__init__)


def test_etj::weekstarts_constructor_args():
    sig = inspect.signature(eTJ::WeekStarts.__init__)
    params = list(sig.parameters.keys())
    assert "sunday" in params, "Missing parameter 'sunday'"
    assert "monday" in params, "Missing parameter 'monday'"

def test_etj::weekstarts_has_sunday():
    assert hasattr(eTJ::WeekStarts, "sunday")
    descriptor = None
    for klass in eTJ::WeekStarts.__mro__:
        if "sunday" in klass.__dict__:
            descriptor = klass.__dict__["sunday"]
            break
    assert isinstance(descriptor, property)

def test_etj::weekstarts_has_monday():
    assert hasattr(eTJ::WeekStarts, "monday")
    descriptor = None
    for klass in eTJ::WeekStarts.__mro__:
        if "monday" in klass.__dict__:
            descriptor = klass.__dict__["monday"]
            break
    assert isinstance(descriptor, property)



def test_etj::extendresource_is_not_abstract():
    assert not inspect.isabstract(eTJ::ExtendResource)


def test_etj::extendresource_constructor_exists():
    assert callable(eTJ::ExtendResource.__init__)


def test_etj::extendresource_constructor_args():
    sig = inspect.signature(eTJ::ExtendResource.__init__)
    params = list(sig.parameters.keys())



def test_etj::timeformat_is_not_abstract():
    assert not inspect.isabstract(eTJ::TimeFormat)


def test_etj::timeformat_constructor_exists():
    assert callable(eTJ::TimeFormat.__init__)


def test_etj::timeformat_constructor_args():
    sig = inspect.signature(eTJ::TimeFormat.__init__)
    params = list(sig.parameters.keys())
    assert "timeformat" in params, "Missing parameter 'timeformat'"

def test_etj::timeformat_has_timeformat():
    assert hasattr(eTJ::TimeFormat, "timeformat")
    descriptor = None
    for klass in eTJ::TimeFormat.__mro__:
        if "timeformat" in klass.__dict__:
            descriptor = klass.__dict__["timeformat"]
            break
    assert isinstance(descriptor, property)



def test_etj::dailyworkinghours_is_not_abstract():
    assert not inspect.isabstract(eTJ::DailyWorkingHours)


def test_etj::dailyworkinghours_constructor_exists():
    assert callable(eTJ::DailyWorkingHours.__init__)


def test_etj::dailyworkinghours_constructor_args():
    sig = inspect.signature(eTJ::DailyWorkingHours.__init__)
    params = list(sig.parameters.keys())
    assert "dailyWorkingHours" in params, "Missing parameter 'dailyWorkingHours'"

def test_etj::dailyworkinghours_has_dailyWorkingHours():
    assert hasattr(eTJ::DailyWorkingHours, "dailyWorkingHours")
    descriptor = None
    for klass in eTJ::DailyWorkingHours.__mro__:
        if "dailyWorkingHours" in klass.__dict__:
            descriptor = klass.__dict__["dailyWorkingHours"]
            break
    assert isinstance(descriptor, property)



def test_etj::now_is_not_abstract():
    assert not inspect.isabstract(eTJ::Now)


def test_etj::now_constructor_exists():
    assert callable(eTJ::Now.__init__)


def test_etj::now_constructor_args():
    sig = inspect.signature(eTJ::Now.__init__)
    params = list(sig.parameters.keys())



def test_etj::journalentry_is_not_abstract():
    assert not inspect.isabstract(eTJ::JournalEntry)


def test_etj::journalentry_constructor_exists():
    assert callable(eTJ::JournalEntry.__init__)


def test_etj::journalentry_constructor_args():
    sig = inspect.signature(eTJ::JournalEntry.__init__)
    params = list(sig.parameters.keys())
    assert "headline" in params, "Missing parameter 'headline'"

def test_etj::journalentry_has_headline():
    assert hasattr(eTJ::JournalEntry, "headline")
    descriptor = None
    for klass in eTJ::JournalEntry.__mro__:
        if "headline" in klass.__dict__:
            descriptor = klass.__dict__["headline"]
            break
    assert isinstance(descriptor, property)



def test_etj::extendtask_is_not_abstract():
    assert not inspect.isabstract(eTJ::ExtendTask)


def test_etj::extendtask_constructor_exists():
    assert callable(eTJ::ExtendTask.__init__)


def test_etj::extendtask_constructor_args():
    sig = inspect.signature(eTJ::ExtendTask.__init__)
    params = list(sig.parameters.keys())



def test_etj::numberformat_is_not_abstract():
    assert not inspect.isabstract(eTJ::NumberFormat)


def test_etj::numberformat_constructor_exists():
    assert callable(eTJ::NumberFormat.__init__)


def test_etj::numberformat_constructor_args():
    sig = inspect.signature(eTJ::NumberFormat.__init__)
    params = list(sig.parameters.keys())



def test_etj::timezone_is_not_abstract():
    assert not inspect.isabstract(eTJ::Timezone)


def test_etj::timezone_constructor_exists():
    assert callable(eTJ::Timezone.__init__)


def test_etj::timezone_constructor_args():
    sig = inspect.signature(eTJ::Timezone.__init__)
    params = list(sig.parameters.keys())
    assert "timezone" in params, "Missing parameter 'timezone'"

def test_etj::timezone_has_timezone():
    assert hasattr(eTJ::Timezone, "timezone")
    descriptor = None
    for klass in eTJ::Timezone.__mro__:
        if "timezone" in klass.__dict__:
            descriptor = klass.__dict__["timezone"]
            break
    assert isinstance(descriptor, property)



def test_etj::yearlyworkingdays_is_not_abstract():
    assert not inspect.isabstract(eTJ::YearlyWorkingDays)


def test_etj::yearlyworkingdays_constructor_exists():
    assert callable(eTJ::YearlyWorkingDays.__init__)


def test_etj::yearlyworkingdays_constructor_args():
    sig = inspect.signature(eTJ::YearlyWorkingDays.__init__)
    params = list(sig.parameters.keys())
    assert "yearlyWorkingDays" in params, "Missing parameter 'yearlyWorkingDays'"

def test_etj::yearlyworkingdays_has_yearlyWorkingDays():
    assert hasattr(eTJ::YearlyWorkingDays, "yearlyWorkingDays")
    descriptor = None
    for klass in eTJ::YearlyWorkingDays.__mro__:
        if "yearlyWorkingDays" in klass.__dict__:
            descriptor = klass.__dict__["yearlyWorkingDays"]
            break
    assert isinstance(descriptor, property)



def test_etj::currencyformat_is_not_abstract():
    assert not inspect.isabstract(eTJ::CurrencyFormat)


def test_etj::currencyformat_constructor_exists():
    assert callable(eTJ::CurrencyFormat.__init__)


def test_etj::currencyformat_constructor_args():
    sig = inspect.signature(eTJ::CurrencyFormat.__init__)
    params = list(sig.parameters.keys())



def test_etj::currency_is_not_abstract():
    assert not inspect.isabstract(eTJ::Currency)


def test_etj::currency_constructor_exists():
    assert callable(eTJ::Currency.__init__)


def test_etj::currency_constructor_args():
    sig = inspect.signature(eTJ::Currency.__init__)
    params = list(sig.parameters.keys())
    assert "currency" in params, "Missing parameter 'currency'"

def test_etj::currency_has_currency():
    assert hasattr(eTJ::Currency, "currency")
    descriptor = None
    for klass in eTJ::Currency.__mro__:
        if "currency" in klass.__dict__:
            descriptor = klass.__dict__["currency"]
            break
    assert isinstance(descriptor, property)



def test_etj::isodate_is_not_abstract():
    assert not inspect.isabstract(eTJ::ISODATE)


def test_etj::isodate_constructor_exists():
    assert callable(eTJ::ISODATE.__init__)


def test_etj::isodate_constructor_args():
    sig = inspect.signature(eTJ::ISODATE.__init__)
    params = list(sig.parameters.keys())



def test_etj::credit_is_not_abstract():
    assert not inspect.isabstract(eTJ::Credit)


def test_etj::credit_constructor_exists():
    assert callable(eTJ::Credit.__init__)


def test_etj::credit_constructor_args():
    sig = inspect.signature(eTJ::Credit.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "description" in params, "Missing parameter 'description'"

def test_etj::credit_has_amount():
    assert hasattr(eTJ::Credit, "amount")
    descriptor = None
    for klass in eTJ::Credit.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_etj::credit_has_description():
    assert hasattr(eTJ::Credit, "description")
    descriptor = None
    for klass in eTJ::Credit.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_etj::copyright_is_not_abstract():
    assert not inspect.isabstract(eTJ::Copyright)


def test_etj::copyright_constructor_exists():
    assert callable(eTJ::Copyright.__init__)


def test_etj::copyright_constructor_args():
    sig = inspect.signature(eTJ::Copyright.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_etj::copyright_has_text():
    assert hasattr(eTJ::Copyright, "text")
    descriptor = None
    for klass in eTJ::Copyright.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_etj::complete_is_not_abstract():
    assert not inspect.isabstract(eTJ::Complete)


def test_etj::complete_constructor_exists():
    assert callable(eTJ::Complete.__init__)


def test_etj::complete_constructor_args():
    sig = inspect.signature(eTJ::Complete.__init__)
    params = list(sig.parameters.keys())
    assert "complete" in params, "Missing parameter 'complete'"

def test_etj::complete_has_complete():
    assert hasattr(eTJ::Complete, "complete")
    descriptor = None
    for klass in eTJ::Complete.__mro__:
        if "complete" in klass.__dict__:
            descriptor = klass.__dict__["complete"]
            break
    assert isinstance(descriptor, property)



def test_etj::column_is_not_abstract():
    assert not inspect.isabstract(eTJ::Column)


def test_etj::column_constructor_exists():
    assert callable(eTJ::Column.__init__)


def test_etj::column_constructor_args():
    sig = inspect.signature(eTJ::Column.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_etj::column_has_id():
    assert hasattr(eTJ::Column, "id")
    descriptor = None
    for klass in eTJ::Column.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_etj::columns_is_not_abstract():
    assert not inspect.isabstract(eTJ::Columns)


def test_etj::columns_constructor_exists():
    assert callable(eTJ::Columns.__init__)


def test_etj::columns_constructor_args():
    sig = inspect.signature(eTJ::Columns.__init__)
    params = list(sig.parameters.keys())



def test_etj::interval4_is_not_abstract():
    assert not inspect.isabstract(eTJ::Interval4)


def test_etj::interval4_constructor_exists():
    assert callable(eTJ::Interval4.__init__)


def test_etj::interval4_constructor_args():
    sig = inspect.signature(eTJ::Interval4.__init__)
    params = list(sig.parameters.keys())



def test_etj::booking_is_not_abstract():
    assert not inspect.isabstract(eTJ::Booking)


def test_etj::booking_constructor_exists():
    assert callable(eTJ::Booking.__init__)


def test_etj::booking_constructor_args():
    sig = inspect.signature(eTJ::Booking.__init__)
    params = list(sig.parameters.keys())
    assert "overtime" in params, "Missing parameter 'overtime'"
    assert "sloppy" in params, "Missing parameter 'sloppy'"

def test_etj::booking_has_overtime():
    assert hasattr(eTJ::Booking, "overtime")
    descriptor = None
    for klass in eTJ::Booking.__mro__:
        if "overtime" in klass.__dict__:
            descriptor = klass.__dict__["overtime"]
            break
    assert isinstance(descriptor, property)

def test_etj::booking_has_sloppy():
    assert hasattr(eTJ::Booking, "sloppy")
    descriptor = None
    for klass in eTJ::Booking.__mro__:
        if "sloppy" in klass.__dict__:
            descriptor = klass.__dict__["sloppy"]
            break
    assert isinstance(descriptor, property)



def test_etj::bookingresource_is_not_abstract():
    assert not inspect.isabstract(eTJ::BookingResource)


def test_etj::bookingresource_constructor_exists():
    assert callable(eTJ::BookingResource.__init__)


def test_etj::bookingresource_constructor_args():
    sig = inspect.signature(eTJ::BookingResource.__init__)
    params = list(sig.parameters.keys())



def test_etj::bookingtask_is_not_abstract():
    assert not inspect.isabstract(eTJ::BookingTask)


def test_etj::bookingtask_constructor_exists():
    assert callable(eTJ::BookingTask.__init__)


def test_etj::bookingtask_constructor_args():
    sig = inspect.signature(eTJ::BookingTask.__init__)
    params = list(sig.parameters.keys())



def test_etj::navigatorattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::NavigatorAttribute)


def test_etj::navigatorattribute_constructor_exists():
    assert callable(eTJ::NavigatorAttribute.__init__)


def test_etj::navigatorattribute_constructor_args():
    sig = inspect.signature(eTJ::NavigatorAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::navigator_is_not_abstract():
    assert not inspect.isabstract(eTJ::Navigator)


def test_etj::navigator_constructor_exists():
    assert callable(eTJ::Navigator.__init__)


def test_etj::navigator_constructor_args():
    sig = inspect.signature(eTJ::Navigator.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_etj::navigator_has_id():
    assert hasattr(eTJ::Navigator, "id")
    descriptor = None
    for klass in eTJ::Navigator.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_etj::allocateresourceattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::AllocateResourceAttribute)


def test_etj::allocateresourceattribute_constructor_exists():
    assert callable(eTJ::AllocateResourceAttribute.__init__)


def test_etj::allocateresourceattribute_constructor_args():
    sig = inspect.signature(eTJ::AllocateResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::allocateresource_is_not_abstract():
    assert not inspect.isabstract(eTJ::AllocateResource)


def test_etj::allocateresource_constructor_exists():
    assert callable(eTJ::AllocateResource.__init__)


def test_etj::allocateresource_constructor_args():
    sig = inspect.signature(eTJ::AllocateResource.__init__)
    params = list(sig.parameters.keys())



def test_etj::allocate_is_not_abstract():
    assert not inspect.isabstract(eTJ::Allocate)


def test_etj::allocate_constructor_exists():
    assert callable(eTJ::Allocate.__init__)


def test_etj::allocate_constructor_args():
    sig = inspect.signature(eTJ::Allocate.__init__)
    params = list(sig.parameters.keys())



def test_etj::resourceattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::ResourceAttribute)


def test_etj::resourceattribute_constructor_exists():
    assert callable(eTJ::ResourceAttribute.__init__)


def test_etj::resourceattribute_constructor_args():
    sig = inspect.signature(eTJ::ResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::resource_is_not_abstract():
    assert not inspect.isabstract(eTJ::Resource)


def test_etj::resource_constructor_exists():
    assert callable(eTJ::Resource.__init__)


def test_etj::resource_constructor_args():
    sig = inspect.signature(eTJ::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_etj::resource_has_name():
    assert hasattr(eTJ::Resource, "name")
    descriptor = None
    for klass in eTJ::Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_etj::resource_has_id():
    assert hasattr(eTJ::Resource, "id")
    descriptor = None
    for klass in eTJ::Resource.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_etj::balance_is_not_abstract():
    assert not inspect.isabstract(eTJ::Balance)


def test_etj::balance_constructor_exists():
    assert callable(eTJ::Balance.__init__)


def test_etj::balance_constructor_args():
    sig = inspect.signature(eTJ::Balance.__init__)
    params = list(sig.parameters.keys())



def test_statusstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(StatusStatusSheetAttribute)


def test_statusstatussheetattribute_constructor_exists():
    assert callable(StatusStatusSheetAttribute.__init__)


def test_statusstatussheetattribute_constructor_args():
    sig = inspect.signature(StatusStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::flags_is_not_abstract():
    assert not inspect.isabstract(eTJ::Flags)


def test_etj::flags_constructor_exists():
    assert callable(eTJ::Flags.__init__)


def test_etj::flags_constructor_args():
    sig = inspect.signature(eTJ::Flags.__init__)
    params = list(sig.parameters.keys())
    assert "flags" in params, "Missing parameter 'flags'"

def test_etj::flags_has_flags():
    assert hasattr(eTJ::Flags, "flags")
    descriptor = None
    for klass in eTJ::Flags.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)



def test_etj::summary_is_not_abstract():
    assert not inspect.isabstract(eTJ::Summary)


def test_etj::summary_constructor_exists():
    assert callable(eTJ::Summary.__init__)


def test_etj::summary_constructor_args():
    sig = inspect.signature(eTJ::Summary.__init__)
    params = list(sig.parameters.keys())



def test_etj::details_is_not_abstract():
    assert not inspect.isabstract(eTJ::Details)


def test_etj::details_constructor_exists():
    assert callable(eTJ::Details.__init__)


def test_etj::details_constructor_args():
    sig = inspect.signature(eTJ::Details.__init__)
    params = list(sig.parameters.keys())



def test_etj::author_is_not_abstract():
    assert not inspect.isabstract(eTJ::Author)


def test_etj::author_constructor_exists():
    assert callable(eTJ::Author.__init__)


def test_etj::author_constructor_args():
    sig = inspect.signature(eTJ::Author.__init__)
    params = list(sig.parameters.keys())



def test_allocateresourceattribute_is_not_abstract():
    assert not inspect.isabstract(AllocateResourceAttribute)


def test_allocateresourceattribute_constructor_exists():
    assert callable(AllocateResourceAttribute.__init__)


def test_allocateresourceattribute_constructor_args():
    sig = inspect.signature(AllocateResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::shiftsallocate_is_not_abstract():
    assert not inspect.isabstract(eTJ::ShiftsAllocate)


def test_etj::shiftsallocate_constructor_exists():
    assert callable(eTJ::ShiftsAllocate.__init__)


def test_etj::shiftsallocate_constructor_args():
    sig = inspect.signature(eTJ::ShiftsAllocate.__init__)
    params = list(sig.parameters.keys())



def test_etj::persistent_is_not_abstract():
    assert not inspect.isabstract(eTJ::Persistent)


def test_etj::persistent_constructor_exists():
    assert callable(eTJ::Persistent.__init__)


def test_etj::persistent_constructor_args():
    sig = inspect.signature(eTJ::Persistent.__init__)
    params = list(sig.parameters.keys())
    assert "persistent" in params, "Missing parameter 'persistent'"

def test_etj::persistent_has_persistent():
    assert hasattr(eTJ::Persistent, "persistent")
    descriptor = None
    for klass in eTJ::Persistent.__mro__:
        if "persistent" in klass.__dict__:
            descriptor = klass.__dict__["persistent"]
            break
    assert isinstance(descriptor, property)



def test_etj::select_is_not_abstract():
    assert not inspect.isabstract(eTJ::Select)


def test_etj::select_constructor_exists():
    assert callable(eTJ::Select.__init__)


def test_etj::select_constructor_args():
    sig = inspect.signature(eTJ::Select.__init__)
    params = list(sig.parameters.keys())
    assert "argument" in params, "Missing parameter 'argument'"

def test_etj::select_has_argument():
    assert hasattr(eTJ::Select, "argument")
    descriptor = None
    for klass in eTJ::Select.__mro__:
        if "argument" in klass.__dict__:
            descriptor = klass.__dict__["argument"]
            break
    assert isinstance(descriptor, property)



def test_etj::mandatory_is_not_abstract():
    assert not inspect.isabstract(eTJ::Mandatory)


def test_etj::mandatory_constructor_exists():
    assert callable(eTJ::Mandatory.__init__)


def test_etj::mandatory_constructor_args():
    sig = inspect.signature(eTJ::Mandatory.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_etj::mandatory_has_mandatory():
    assert hasattr(eTJ::Mandatory, "mandatory")
    descriptor = None
    for klass in eTJ::Mandatory.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_etj::alternative_is_not_abstract():
    assert not inspect.isabstract(eTJ::Alternative)


def test_etj::alternative_constructor_exists():
    assert callable(eTJ::Alternative.__init__)


def test_etj::alternative_constructor_args():
    sig = inspect.signature(eTJ::Alternative.__init__)
    params = list(sig.parameters.keys())



def test_etj::alert_is_not_abstract():
    assert not inspect.isabstract(eTJ::Alert)


def test_etj::alert_constructor_exists():
    assert callable(eTJ::Alert.__init__)


def test_etj::alert_constructor_args():
    sig = inspect.signature(eTJ::Alert.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_etj::alert_has_level():
    assert hasattr(eTJ::Alert, "level")
    descriptor = None
    for klass in eTJ::Alert.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_etj::nikureportattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::NikuReportAttribute)


def test_etj::nikureportattribute_constructor_exists():
    assert callable(eTJ::NikuReportAttribute.__init__)


def test_etj::nikureportattribute_constructor_args():
    sig = inspect.signature(eTJ::NikuReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::nikureport_is_not_abstract():
    assert not inspect.isabstract(eTJ::NikuReport)


def test_etj::nikureport_constructor_exists():
    assert callable(eTJ::NikuReport.__init__)


def test_etj::nikureport_constructor_args():
    sig = inspect.signature(eTJ::NikuReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_etj::nikureport_has_filename():
    assert hasattr(eTJ::NikuReport, "filename")
    descriptor = None
    for klass in eTJ::NikuReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_etj::newtaskattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::NewTaskAttribute)


def test_etj::newtaskattribute_constructor_exists():
    assert callable(eTJ::NewTaskAttribute.__init__)


def test_etj::newtaskattribute_constructor_args():
    sig = inspect.signature(eTJ::NewTaskAttribute.__init__)
    params = list(sig.parameters.keys())



def test_timesheetattribute_is_not_abstract():
    assert not inspect.isabstract(TimesheetAttribute)


def test_timesheetattribute_constructor_exists():
    assert callable(TimesheetAttribute.__init__)


def test_timesheetattribute_constructor_args():
    sig = inspect.signature(TimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::shifttimesheet_is_not_abstract():
    assert not inspect.isabstract(eTJ::ShiftTimesheet)


def test_etj::shifttimesheet_constructor_exists():
    assert callable(eTJ::ShiftTimesheet.__init__)


def test_etj::shifttimesheet_constructor_args():
    sig = inspect.signature(eTJ::ShiftTimesheet.__init__)
    params = list(sig.parameters.keys())



def test_etj::tasktimesheet_is_not_abstract():
    assert not inspect.isabstract(eTJ::TaskTimesheet)


def test_etj::tasktimesheet_constructor_exists():
    assert callable(eTJ::TaskTimesheet.__init__)


def test_etj::tasktimesheet_constructor_args():
    sig = inspect.signature(eTJ::TaskTimesheet.__init__)
    params = list(sig.parameters.keys())



def test_etj::statustimesheet_is_not_abstract():
    assert not inspect.isabstract(eTJ::StatusTimesheet)


def test_etj::statustimesheet_constructor_exists():
    assert callable(eTJ::StatusTimesheet.__init__)


def test_etj::statustimesheet_constructor_args():
    sig = inspect.signature(eTJ::StatusTimesheet.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "level" in params, "Missing parameter 'level'"

def test_etj::statustimesheet_has_text():
    assert hasattr(eTJ::StatusTimesheet, "text")
    descriptor = None
    for klass in eTJ::StatusTimesheet.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_etj::statustimesheet_has_level():
    assert hasattr(eTJ::StatusTimesheet, "level")
    descriptor = None
    for klass in eTJ::StatusTimesheet.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_etj::newtask_is_not_abstract():
    assert not inspect.isabstract(eTJ::NewTask)


def test_etj::newtask_constructor_exists():
    assert callable(eTJ::NewTask.__init__)


def test_etj::newtask_constructor_args():
    sig = inspect.signature(eTJ::NewTask.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "id" in params, "Missing parameter 'id'"

def test_etj::newtask_has_text():
    assert hasattr(eTJ::NewTask, "text")
    descriptor = None
    for klass in eTJ::NewTask.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_etj::newtask_has_id():
    assert hasattr(eTJ::NewTask, "id")
    descriptor = None
    for klass in eTJ::NewTask.__mro__:
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



def test_etj::macrocall_is_not_abstract():
    assert not inspect.isabstract(eTJ::MacroCall)


def test_etj::macrocall_constructor_exists():
    assert callable(eTJ::MacroCall.__init__)


def test_etj::macrocall_constructor_args():
    sig = inspect.signature(eTJ::MacroCall.__init__)
    params = list(sig.parameters.keys())
    assert "buildin" in params, "Missing parameter 'buildin'"

def test_etj::macrocall_has_buildin():
    assert hasattr(eTJ::MacroCall, "buildin")
    descriptor = None
    for klass in eTJ::MacroCall.__mro__:
        if "buildin" in klass.__dict__:
            descriptor = klass.__dict__["buildin"]
            break
    assert isinstance(descriptor, property)



def test_etj::eobject_is_not_abstract():
    assert not inspect.isabstract(eTJ::EObject)


def test_etj::eobject_constructor_exists():
    assert callable(eTJ::EObject.__init__)


def test_etj::eobject_constructor_args():
    sig = inspect.signature(eTJ::EObject.__init__)
    params = list(sig.parameters.keys())



def test_etj::scenario_is_not_abstract():
    assert not inspect.isabstract(eTJ::Scenario)


def test_etj::scenario_constructor_exists():
    assert callable(eTJ::Scenario.__init__)


def test_etj::scenario_constructor_args():
    sig = inspect.signature(eTJ::Scenario.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "active" in params, "Missing parameter 'active'"

def test_etj::scenario_has_name():
    assert hasattr(eTJ::Scenario, "name")
    descriptor = None
    for klass in eTJ::Scenario.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_etj::scenario_has_id():
    assert hasattr(eTJ::Scenario, "id")
    descriptor = None
    for klass in eTJ::Scenario.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_etj::scenario_has_active():
    assert hasattr(eTJ::Scenario, "active")
    descriptor = None
    for klass in eTJ::Scenario.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_etj::taskattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::TaskAttribute)


def test_etj::taskattribute_constructor_exists():
    assert callable(eTJ::TaskAttribute.__init__)


def test_etj::taskattribute_constructor_args():
    sig = inspect.signature(eTJ::TaskAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::task_is_not_abstract():
    assert not inspect.isabstract(eTJ::Task)


def test_etj::task_constructor_exists():
    assert callable(eTJ::Task.__init__)


def test_etj::task_constructor_args():
    sig = inspect.signature(eTJ::Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_etj::task_has_name():
    assert hasattr(eTJ::Task, "name")
    descriptor = None
    for klass in eTJ::Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_etj::task_has_id():
    assert hasattr(eTJ::Task, "id")
    descriptor = None
    for klass in eTJ::Task.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_etj::projectattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::ProjectAttribute)


def test_etj::projectattribute_constructor_exists():
    assert callable(eTJ::ProjectAttribute.__init__)


def test_etj::projectattribute_constructor_args():
    sig = inspect.signature(eTJ::ProjectAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::exportattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::ExportAttribute)


def test_etj::exportattribute_constructor_exists():
    assert callable(eTJ::ExportAttribute.__init__)


def test_etj::exportattribute_constructor_args():
    sig = inspect.signature(eTJ::ExportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::export_is_not_abstract():
    assert not inspect.isabstract(eTJ::Export)


def test_etj::export_constructor_exists():
    assert callable(eTJ::Export.__init__)


def test_etj::export_constructor_args():
    sig = inspect.signature(eTJ::Export.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"
    assert "id" in params, "Missing parameter 'id'"

def test_etj::export_has_filename():
    assert hasattr(eTJ::Export, "filename")
    descriptor = None
    for klass in eTJ::Export.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_etj::export_has_id():
    assert hasattr(eTJ::Export, "id")
    descriptor = None
    for klass in eTJ::Export.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_etj::icalreportattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::IcalReportAttribute)


def test_etj::icalreportattribute_constructor_exists():
    assert callable(eTJ::IcalReportAttribute.__init__)


def test_etj::icalreportattribute_constructor_args():
    sig = inspect.signature(eTJ::IcalReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_etj::icalreport_is_not_abstract():
    assert not inspect.isabstract(eTJ::IcalReport)


def test_etj::icalreport_constructor_exists():
    assert callable(eTJ::IcalReport.__init__)


def test_etj::icalreport_constructor_args():
    sig = inspect.signature(eTJ::IcalReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_etj::icalreport_has_filename():
    assert hasattr(eTJ::IcalReport, "filename")
    descriptor = None
    for klass in eTJ::IcalReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_etj::reportattribute_is_not_abstract():
    assert not inspect.isabstract(eTJ::ReportAttribute)


def test_etj::reportattribute_constructor_exists():
    assert callable(eTJ::ReportAttribute.__init__)


def test_etj::reportattribute_constructor_args():
    sig = inspect.signature(eTJ::ReportAttribute.__init__)
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



def test_etj::report_is_not_abstract():
    assert not inspect.isabstract(eTJ::Report)


def test_etj::report_constructor_exists():
    assert callable(eTJ::Report.__init__)


def test_etj::report_constructor_args():
    sig = inspect.signature(eTJ::Report.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_etj::report_has_name():
    assert hasattr(eTJ::Report, "name")
    descriptor = None
    for klass in eTJ::Report.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_etj::report_has_id():
    assert hasattr(eTJ::Report, "id")
    descriptor = None
    for klass in eTJ::Report.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_purgereportattribute_exists():
    # Check that the Enumeration exists
    assert PurgeReportAttribute is not None

def test_purgereportattribute_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PurgeReportAttribute]
    expected_literals = [
        "FLAGS",
        "JOURNALATTRIBUTES",
        "DEFINITIONS",
        "SORTACCOUNTS",
        "FORMATS",
        "SORTRESOURCES",
        "SORTJOURNALENTRIES",
        "SORTTASKS",
        "SCENARIOS",
        "COLUMNS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PurgeReportAttribute"

def test_justification_exists():
    # Check that the Enumeration exists
    assert Justification is not None

def test_justification_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Justification]
    expected_literals = [
        "CENTER",
        "LEFT",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Justification"

def test_scaleresolution_exists():
    # Check that the Enumeration exists
    assert ScaleResolution is not None

def test_scaleresolution_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScaleResolution]
    expected_literals = [
        "HOUR",
        "YEAR",
        "MONTH",
        "QUARTER",
        "WEEK",
        "DAY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScaleResolution"

def test_listtypevalues_exists():
    # Check that the Enumeration exists
    assert ListTypeValues is not None

def test_listtypevalues_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ListTypeValues]
    expected_literals = [
        "NUMBERED",
        "COMMA",
        "BULLETS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ListTypeValues"

def test_workquantityunit_exists():
    # Check that the Enumeration exists
    assert WorkQuantityUnit is not None

def test_workquantityunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkQuantityUnit]
    expected_literals = [
        "DAYS",
        "HOURS",
        "MINUTES",
        "PERCENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkQuantityUnit"

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

def test_loaddisplayunit_exists():
    # Check that the Enumeration exists
    assert LoadDisplayUnit is not None

def test_loaddisplayunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LoadDisplayUnit]
    expected_literals = [
        "WEEKS",
        "MONTHS",
        "SHORTAUTO",
        "MINUTES",
        "HOURS",
        "YEARS",
        "DAYS",
        "LONGAUTO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LoadDisplayUnit"

def test_journalattributevalues_exists():
    # Check that the Enumeration exists
    assert JournalAttributeValues is not None

def test_journalattributevalues_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JournalAttributeValues]
    expected_literals = [
        "summary",
        "details",
        "flags",
        "NONE",
        "author",
        "alert",
        "propertyid",
        "ALL",
        "property",
        "timesheet",
        "headline",
        "date",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JournalAttributeValues"

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "MINUTE",
        "MONTH",
        "YEAR",
        "HOUR",
        "WEEK",
        "DAY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnit"

def test_schedulingpolicy_exists():
    # Check that the Enumeration exists
    assert SchedulingPolicy is not None

def test_schedulingpolicy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SchedulingPolicy]
    expected_literals = [
        "ALAP",
        "ASAP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SchedulingPolicy"

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

def test_purgetaskattribute_exists():
    # Check that the Enumeration exists
    assert PurgeTaskAttribute is not None

def test_purgetaskattribute_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PurgeTaskAttribute]
    expected_literals = [
        "BOOKING",
        "DEPENDS",
        "CHARGESET",
        "FAIL",
        "CHARGE",
        "WARN",
        "PRECEDES",
        "FLAGS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PurgeTaskAttribute"

def test_criteriondirection_exists():
    # Check that the Enumeration exists
    assert CriterionDirection is not None

def test_criteriondirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CriterionDirection]
    expected_literals = [
        "UP",
        "DOWN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CriterionDirection"

def test_journalentrysortcriterion_exists():
    # Check that the Enumeration exists
    assert JournalEntrySortCriterion is not None

def test_journalentrysortcriterion_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JournalEntrySortCriterion]
    expected_literals = [
        "DATE_DOWN",
        "ALERT_DOWN",
        "ALERT_UP",
        "PROPERTY_UP",
        "DATE_UP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JournalEntrySortCriterion"

def test_leavetype_exists():
    # Check that the Enumeration exists
    assert LeaveType is not None

def test_leavetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LeaveType]
    expected_literals = [
        "sick",
        "unemployed",
        "annual",
        "unpaid",
        "project",
        "special",
        "holiday",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LeaveType"

def test_columnid_exists():
    # Check that the Enumeration exists
    assert ColumnId is not None

def test_columnid_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColumnId]
    expected_literals = [
        "duties",
        "flags",
        "managers",
        "id",
        "hourly",
        "alert",
        "followers",
        "reports",
        "sickleave",
        "maxend",
        "annualleavebalance",
        "effort",
        "freetime",
        "priority",
        "activetasks",
        "responsible",
        "daily",
        "alertmessages",
        "status",
        "journal_sub",
        "name",
        "balance",
        "alerttrend",
        "journalmessages",
        "duration",
        "competitorcount",
        "weekly",
        "line",
        "effortdone",
        "turnover",
        "directreports",
        "minstart",
        "cost",
        "children",
        "fte",
        "pathcriticalness",
        "journalsummaries",
        "hierarchindex",
        "maxstart",
        "criticalness",
        "closedtasks",
        "bsi",
        "revenue",
        "resources",
        "end",
        "start",
        "opentasks",
        "wbs",
        "efficiency",
        "inputs",
        "freework",
        "chart",
        "email",
        "effortleft",
        "rate",
        "alertsummaries",
        "specialleave",
        "yearly",
        "unpaidleave",
        "headcount",
        "scenario",
        "note",
        "no",
        "scheduling",
        "competitors",
        "index",
        "precursors",
        "gauge",
        "annualleave",
        "seqno",
        "quarterly",
        "targets",
        "complete",
        "monthly",
        "journal",
        "minend",
        "completed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColumnId"

def test_alertlevel_exists():
    # Check that the Enumeration exists
    assert AlertLevel is not None

def test_alertlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlertLevel]
    expected_literals = [
        "GREEN",
        "YELLOW",
        "RED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlertLevel"

def test_selectargument_exists():
    # Check that the Enumeration exists
    assert SelectArgument is not None

def test_selectargument_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SelectArgument]
    expected_literals = [
        "RANDOM",
        "MAXLOADED",
        "MINALLOCATED",
        "ORDER",
        "MINLOADED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SelectArgument"

def test_dependspolicy_exists():
    # Check that the Enumeration exists
    assert DependsPolicy is not None

def test_dependspolicy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DependsPolicy]
    expected_literals = [
        "ONEND",
        "ONSTART",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DependsPolicy"

def test_chargeapplies_exists():
    # Check that the Enumeration exists
    assert ChargeApplies is not None

def test_chargeapplies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ChargeApplies]
    expected_literals = [
        "PERDAY",
        "PERHOUR",
        "PERWEEK",
        "ONSTART",
        "ONEND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ChargeApplies"

def test_purgeresourceattribute_exists():
    # Check that the Enumeration exists
    assert PurgeResourceAttribute is not None

def test_purgeresourceattribute_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PurgeResourceAttribute]
    expected_literals = [
        "FAIL",
        "VACATIONS",
        "FLAGS",
        "MANAGERS",
        "WARN",
        "REPORTS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PurgeResourceAttribute"

def test_buildinmacro_exists():
    # Check that the Enumeration exists
    assert BuildInMacro is not None

def test_buildinmacro_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuildInMacro]
    expected_literals = [
        "projectstart",
        "now",
        "projectend",
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
        "SUN",
        "FRI",
        "TUE",
        "SAT",
        "THR",
        "MON",
        "WED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Weekday"

def test_journalmodevalue_exists():
    # Check that the Enumeration exists
    assert JournalModeValue is not None

def test_journalmodevalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JournalModeValue]
    expected_literals = [
        "STATUS_UP",
        "JOURNAL",
        "JOURNAL_SUB",
        "STATUS_DOWN",
        "ALERTS_DOWN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JournalModeValue"


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
eTJ::LogicalAbsoluteIdExression_strategy = st.builds(
    eTJ::LogicalAbsoluteIdExression,
    value=
        safe_text
)
eTJ::LogicalNumeralLiteral_strategy = st.builds(
    eTJ::LogicalNumeralLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ::LogicalBooleanLiteral_strategy = st.builds(
    eTJ::LogicalBooleanLiteral,
    isTrue=
        st.booleans()
)
eTJ::LogicalDateLiteral_strategy = st.builds(
    eTJ::LogicalDateLiteral,
)
eTJ::LogicalFlagExpression_strategy = st.builds(
    eTJ::LogicalFlagExpression,
    columId=
        safe_text
)
eTJ::LogicalStringLiteral_strategy = st.builds(
    eTJ::LogicalStringLiteral,
    value=
        safe_text
)
eTJ::LogicalFunctionExpression_strategy = st.builds(
    eTJ::LogicalFunctionExpression,
)
Definitions_strategy = st.builds(
    Definitions,
)
eTJ::Defintions_strategy = st.builds(
    eTJ::Defintions,
    tasks=
        st.booleans(),
    projectids=
        st.booleans(),
    resources=
        st.booleans(),
    project=
        st.booleans(),
    flags=
        st.booleans()
)
eTJ::ExtDate_strategy = st.builds(
    eTJ::ExtDate,
)
NumberFormat_strategy = st.builds(
    NumberFormat,
)
CurrencyFormat_strategy = st.builds(
    CurrencyFormat,
)
eTJ::RealFormat_strategy = st.builds(
    eTJ::RealFormat,
    thousandsSeparator=
        safe_text,
    fractionDigits=
        st.integers(),
    negativeSuffix=
        safe_text,
    negativePrefix=
        safe_text,
    fractionSeparator=
        safe_text
)
eTJ::LimitAttribute_strategy = st.builds(
    eTJ::LimitAttribute,
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
eTJ::RichText_strategy = st.builds(
    eTJ::RichText,
    text=
        safe_text
)
Precedes_strategy = st.builds(
    Precedes,
)
eTJ::ColumnAttribute_strategy = st.builds(
    eTJ::ColumnAttribute,
)
eTJ::WorkHours_strategy = st.builds(
    eTJ::WorkHours,
    stop=
        safe_text,
    start=
        safe_text
)
eTJ::Weekdays_strategy = st.builds(
    eTJ::Weekdays,
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
eTJ::Limit_strategy = st.builds(
    eTJ::Limit,
)
GapLength_strategy = st.builds(
    GapLength,
)
GapDuration_strategy = st.builds(
    GapDuration,
)
eTJ::TreeLevel_strategy = st.builds(
    eTJ::TreeLevel,
    level=
        safe_text
)
eTJ::TimesheetReportAttribute_strategy = st.builds(
    eTJ::TimesheetReportAttribute,
)
eTJ::TimesheetAttribute_strategy = st.builds(
    eTJ::TimesheetAttribute,
)
eTJ::TaskTimesheetAttribute_strategy = st.builds(
    eTJ::TaskTimesheetAttribute,
)
eTJ::TaskStatusSheetAttribute_strategy = st.builds(
    eTJ::TaskStatusSheetAttribute,
)
StatusSheetAttribute_strategy = st.builds(
    StatusSheetAttribute,
)
eTJ::StatusSheetReportAttribute_strategy = st.builds(
    eTJ::StatusSheetReportAttribute,
)
eTJ::StatusSheetAttribute_strategy = st.builds(
    eTJ::StatusSheetAttribute,
)
eTJ::Criterion_strategy = st.builds(
    eTJ::Criterion,
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
eTJ::Sort_strategy = st.builds(
    eTJ::Sort,
    tree=
        st.booleans()
)
eTJ::ShiftsTask_strategy = st.builds(
    eTJ::ShiftsTask,
)
eTJ::StatusTimesheetAttribute_strategy = st.builds(
    eTJ::StatusTimesheetAttribute,
)
eTJ::StatusStatusSheetAttribute_strategy = st.builds(
    eTJ::StatusStatusSheetAttribute,
)
TaskStatusSheetAttribute_strategy = st.builds(
    TaskStatusSheetAttribute,
)
eTJ::TaskStatusSheet_strategy = st.builds(
    eTJ::TaskStatusSheet,
)
eTJ::StatusStatusSheet_strategy = st.builds(
    eTJ::StatusStatusSheet,
    level=
        safe_text,
    text=
        safe_text
)
eTJ::Scheduling_strategy = st.builds(
    eTJ::Scheduling,
    scheduling=
        safe_text
)
eTJ::Scheduled_strategy = st.builds(
    eTJ::Scheduled,
    scheduled=
        st.booleans()
)
eTJ::ShiftsLimit_strategy = st.builds(
    eTJ::ShiftsLimit,
)
ShiftsTask_strategy = st.builds(
    ShiftsTask,
)
ShiftsResource_strategy = st.builds(
    ShiftsResource,
)
eTJ::Shifts_strategy = st.builds(
    eTJ::Shifts,
)
eTJ::Responsible_strategy = st.builds(
    eTJ::Responsible,
)
eTJ::PurgeTask_strategy = st.builds(
    eTJ::PurgeTask,
    listAttribute=
        safe_text
)
eTJ::AccountAttribute_strategy = st.builds(
    eTJ::AccountAttribute,
)
AccountAttribute_strategy = st.builds(
    AccountAttribute,
)
eTJ::Interval2_strategy = st.builds(
    eTJ::Interval2,
)
ReportAttribute_strategy = st.builds(
    ReportAttribute,
)
eTJ::SortAccounts_strategy = st.builds(
    eTJ::SortAccounts,
)
eTJ::SortJournalEntries_strategy = st.builds(
    eTJ::SortJournalEntries,
)
eTJ::SelfContained_strategy = st.builds(
    eTJ::SelfContained,
    selfcontained=
        safe_text
)
eTJ::AccountRoot_strategy = st.builds(
    eTJ::AccountRoot,
)
eTJ::RollupAccount_strategy = st.builds(
    eTJ::RollupAccount,
)
eTJ::ResourceRoot_strategy = st.builds(
    eTJ::ResourceRoot,
)
eTJ::Right_strategy = st.builds(
    eTJ::Right,
)
eTJ::TaskRoot_strategy = st.builds(
    eTJ::TaskRoot,
)
IncludePropertiesAttribute_strategy = st.builds(
    IncludePropertiesAttribute,
)
eTJ::ReportPrefix_strategy = st.builds(
    eTJ::ReportPrefix,
)
eTJ::TaskPrefix_strategy = st.builds(
    eTJ::TaskPrefix,
)
eTJ::ResourcePrefix_strategy = st.builds(
    eTJ::ResourcePrefix,
)
eTJ::AccountPrefix_strategy = st.builds(
    eTJ::AccountPrefix,
)
eTJ::Property_strategy = st.builds(
    eTJ::Property,
)
eTJ::Project_strategy = st.builds(
    eTJ::Project,
    id=
        safe_text,
    version=
        safe_text,
    name=
        safe_text
)
eTJ::Global_strategy = st.builds(
    eTJ::Global,
)
eTJ::Interval3_strategy = st.builds(
    eTJ::Interval3,
)
eTJ::LeaveDetails_strategy = st.builds(
    eTJ::LeaveDetails,
    type=
        safe_text,
    name=
        safe_text
)
ResourceAttribute_strategy = st.builds(
    ResourceAttribute,
)
eTJ::PurgeResource_strategy = st.builds(
    eTJ::PurgeResource,
    listAttribute=
        safe_text
)
eTJ::ShiftsResource_strategy = st.builds(
    eTJ::ShiftsResource,
)
eTJ::Warn_strategy = st.builds(
    eTJ::Warn,
)
Property_strategy = st.builds(
    Property,
)
eTJ::Shift_strategy = st.builds(
    eTJ::Shift,
    replace=
        safe_text,
    name=
        safe_text,
    id=
        safe_text,
    timezone=
        safe_text
)
eTJ::TagFile_strategy = st.builds(
    eTJ::TagFile,
    id=
        safe_text,
    filename=
        safe_text
)
eTJ::Macro_strategy = st.builds(
    eTJ::Macro,
    value=
        safe_text,
    id=
        safe_text
)
eTJ::TextReport_strategy = st.builds(
    eTJ::TextReport,
)
eTJ::SupplementTask_strategy = st.builds(
    eTJ::SupplementTask,
)
eTJ::ResourceReport_strategy = st.builds(
    eTJ::ResourceReport,
)
eTJ::SupplementReport_strategy = st.builds(
    eTJ::SupplementReport,
)
eTJ::TimesheetReport_strategy = st.builds(
    eTJ::TimesheetReport,
    filename=
        safe_text
)
eTJ::StatusSheetReport_strategy = st.builds(
    eTJ::StatusSheetReport,
    filename=
        safe_text
)
eTJ::AccountReport_strategy = st.builds(
    eTJ::AccountReport,
)
eTJ::Rate_strategy = st.builds(
    eTJ::Rate,
    rate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ::TaskReport_strategy = st.builds(
    eTJ::TaskReport,
)
eTJ::Vacation_strategy = st.builds(
    eTJ::Vacation,
    name=
        safe_text
)
eTJ::Timesheet_strategy = st.builds(
    eTJ::Timesheet,
)
eTJ::SupplementAccount_strategy = st.builds(
    eTJ::SupplementAccount,
)
eTJ::Account_strategy = st.builds(
    eTJ::Account,
    name=
        safe_text,
    id=
        safe_text
)
eTJ::StatusSheet_strategy = st.builds(
    eTJ::StatusSheet,
)
eTJ::SupplementResource_strategy = st.builds(
    eTJ::SupplementResource,
)
eTJ::Leaves_strategy = st.builds(
    eTJ::Leaves,
)
eTJ::Note_strategy = st.builds(
    eTJ::Note,
    note=
        safe_text
)
eTJ::PurgeReport_strategy = st.builds(
    eTJ::PurgeReport,
    listAttribute=
        safe_text
)
eTJ::Prolog_strategy = st.builds(
    eTJ::Prolog,
)
eTJ::ProjectIds_strategy = st.builds(
    eTJ::ProjectIds,
    ids=
        safe_text
)
eTJ::ProjectId_strategy = st.builds(
    eTJ::ProjectId,
    projectId=
        safe_text
)
eTJ::Precedes_strategy = st.builds(
    eTJ::Precedes,
)
eTJ::LoadUnit_strategy = st.builds(
    eTJ::LoadUnit,
    unit=
        safe_text
)
eTJ::LimitsAttribute_strategy = st.builds(
    eTJ::LimitsAttribute,
)
eTJ::Limits_strategy = st.builds(
    eTJ::Limits,
)
eTJ::MinStart_strategy = st.builds(
    eTJ::MinStart,
)
eTJ::MinEnd_strategy = st.builds(
    eTJ::MinEnd,
)
eTJ::Milestone_strategy = st.builds(
    eTJ::Milestone,
    milestone=
        st.booleans()
)
eTJ::MaxStart_strategy = st.builds(
    eTJ::MaxStart,
)
eTJ::MaxEnd_strategy = st.builds(
    eTJ::MaxEnd,
)
eTJ::Managers_strategy = st.builds(
    eTJ::Managers,
)
eTJ::JournalAttributes_strategy = st.builds(
    eTJ::JournalAttributes,
    args=
        safe_text
)
eTJ::Length_strategy = st.builds(
    eTJ::Length,
)
eTJ::Left_strategy = st.builds(
    eTJ::Left,
)
eTJ::JournalMode_strategy = st.builds(
    eTJ::JournalMode,
    mode=
        safe_text
)
NavigatorAttribute_strategy = st.builds(
    NavigatorAttribute,
)
eTJ::HideReport_strategy = st.builds(
    eTJ::HideReport,
)
eTJ::Interval1_strategy = st.builds(
    eTJ::Interval1,
)
eTJ::IncludePropertiesAttribute_strategy = st.builds(
    eTJ::IncludePropertiesAttribute,
)
eTJ::IncludeProperties_strategy = st.builds(
    eTJ::IncludeProperties,
    importURI=
        safe_text
)
eTJ::Footer_strategy = st.builds(
    eTJ::Footer,
)
eTJ::Fail_strategy = st.builds(
    eTJ::Fail,
)
eTJ::ExtendedTaskAttribute_strategy = st.builds(
    eTJ::ExtendedTaskAttribute,
    value=
        safe_text
)
eTJ::HideAccount_strategy = st.builds(
    eTJ::HideAccount,
    expression=
        safe_text
)
eTJ::Header_strategy = st.builds(
    eTJ::Header,
)
eTJ::GapLength_strategy = st.builds(
    eTJ::GapLength,
)
eTJ::GapDuration_strategy = st.builds(
    eTJ::GapDuration,
)
eTJ::Function_strategy = st.builds(
    eTJ::Function,
    level=
        st.integers(),
    parentId=
        safe_text,
    distance=
        st.integers()
)
NewTaskAttribute_strategy = st.builds(
    NewTaskAttribute,
)
IcalReportAttribute_strategy = st.builds(
    IcalReportAttribute,
)
eTJ::ScenarioIcal_strategy = st.builds(
    eTJ::ScenarioIcal,
)
eTJ::HideJournalEntry_strategy = st.builds(
    eTJ::HideJournalEntry,
    expression=
        safe_text
)
eTJ::Email_strategy = st.builds(
    eTJ::Email,
    address=
        safe_text
)
eTJ::Effort_strategy = st.builds(
    eTJ::Effort,
)
eTJ::Efficiency_strategy = st.builds(
    eTJ::Efficiency,
    efficiency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ::DurationQuantity_strategy = st.builds(
    eTJ::DurationQuantity,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    unit=
        safe_text
)
eTJ::Duration_strategy = st.builds(
    eTJ::Duration,
)
StatusTimesheetAttribute_strategy = st.builds(
    StatusTimesheetAttribute,
)
eTJ::TaskDependency_strategy = st.builds(
    eTJ::TaskDependency,
    policy=
        safe_text
)
eTJ::Depends_strategy = st.builds(
    eTJ::Depends,
)
eTJ::ExtendedResourceAttribute_strategy = st.builds(
    eTJ::ExtendedResourceAttribute,
    value=
        safe_text
)
eTJ::Extend_strategy = st.builds(
    eTJ::Extend,
    inherit=
        st.booleans(),
    description=
        safe_text,
    scenariospecific=
        st.booleans(),
    name=
        safe_text
)
eTJ::Epilog_strategy = st.builds(
    eTJ::Epilog,
)
eTJ::EndCredit_strategy = st.builds(
    eTJ::EndCredit,
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
TimesheetReportAttribute_strategy = st.builds(
    TimesheetReportAttribute,
)
TaskTimesheetAttribute_strategy = st.builds(
    TaskTimesheetAttribute,
)
eTJ::Remaining_strategy = st.builds(
    eTJ::Remaining,
)
eTJ::Work_strategy = st.builds(
    eTJ::Work,
    unit=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ::Priority_strategy = st.builds(
    eTJ::Priority,
    priority=
        st.integers()
)
StatusSheetReportAttribute_strategy = st.builds(
    StatusSheetReportAttribute,
)
eTJ::SortResources_strategy = st.builds(
    eTJ::SortResources,
)
eTJ::SortTasks_strategy = st.builds(
    eTJ::SortTasks,
)
NikuReportAttribute_strategy = st.builds(
    NikuReportAttribute,
)
eTJ::Timeoff_strategy = st.builds(
    eTJ::Timeoff,
    name=
        safe_text,
    id=
        safe_text
)
eTJ::Headline_strategy = st.builds(
    eTJ::Headline,
)
eTJ::Formats_strategy = st.builds(
    eTJ::Formats,
    formats=
        safe_text
)
eTJ::AccountShare_strategy = st.builds(
    eTJ::AccountShare,
    share=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ::ChargeSet_strategy = st.builds(
    eTJ::ChargeSet,
)
eTJ::Charge_strategy = st.builds(
    eTJ::Charge,
    applies=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ::Center_strategy = st.builds(
    eTJ::Center,
)
eTJ::RGB_strategy = st.builds(
    eTJ::RGB,
    value=
        safe_text
)
eTJ::LogicalExpression_strategy = st.builds(
    eTJ::LogicalExpression,
    op=
        safe_text
)
ColumnAttribute_strategy = st.builds(
    ColumnAttribute,
)
eTJ::ExtendedResourceAttributeColumn_strategy = st.builds(
    eTJ::ExtendedResourceAttributeColumn,
)
eTJ::ListType_strategy = st.builds(
    eTJ::ListType,
    type=
        safe_text
)
eTJ::HAlign_strategy = st.builds(
    eTJ::HAlign,
    justification=
        safe_text
)
eTJ::FontColor_strategy = st.builds(
    eTJ::FontColor,
    color=
        safe_text
)
eTJ::CellText_strategy = st.builds(
    eTJ::CellText,
    text=
        safe_text
)
eTJ::ToolTip_strategy = st.builds(
    eTJ::ToolTip,
    tip=
        safe_text
)
eTJ::Title_strategy = st.builds(
    eTJ::Title,
    title=
        safe_text
)
eTJ::ListItem_strategy = st.builds(
    eTJ::ListItem,
)
eTJ::Width_strategy = st.builds(
    eTJ::Width,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ::Scale_strategy = st.builds(
    eTJ::Scale,
    scale=
        safe_text
)
eTJ::CellColor_strategy = st.builds(
    eTJ::CellColor,
)
eTJ::Caption_strategy = st.builds(
    eTJ::Caption,
)
ExportAttribute_strategy = st.builds(
    ExportAttribute,
)
eTJ::RollupTask_strategy = st.builds(
    eTJ::RollupTask,
)
eTJ::TaskAttributes_strategy = st.builds(
    eTJ::TaskAttributes,
    minend=
        st.booleans(),
    all=
        st.booleans(),
    responsible=
        st.booleans(),
    note=
        st.booleans(),
    maxend=
        st.booleans(),
    priority=
        st.booleans(),
    minstart=
        st.booleans(),
    complete=
        st.booleans(),
    depends=
        st.booleans(),
    flags=
        st.booleans(),
    maxstart=
        st.booleans(),
    booking=
        st.booleans(),
    none=
        st.booleans()
)
eTJ::Period_strategy = st.builds(
    eTJ::Period,
)
eTJ::Start_strategy = st.builds(
    eTJ::Start,
)
eTJ::Scenarios_strategy = st.builds(
    eTJ::Scenarios,
)
eTJ::RollupResource_strategy = st.builds(
    eTJ::RollupResource,
)
eTJ::ResourceAttributes_strategy = st.builds(
    eTJ::ResourceAttributes,
    all=
        st.booleans(),
    workingHours=
        st.booleans(),
    booking=
        st.booleans(),
    none=
        st.booleans(),
    vacation=
        st.booleans()
)
eTJ::HideTask_strategy = st.builds(
    eTJ::HideTask,
)
eTJ::HideResource_strategy = st.builds(
    eTJ::HideResource,
)
eTJ::End_strategy = st.builds(
    eTJ::End,
)
eTJ::Definitions_strategy = st.builds(
    eTJ::Definitions,
    none=
        st.booleans(),
    all=
        st.booleans()
)
LimitsAttribute_strategy = st.builds(
    LimitsAttribute,
)
eTJ::MonthlyMin_strategy = st.builds(
    eTJ::MonthlyMin,
)
eTJ::DailyMin_strategy = st.builds(
    eTJ::DailyMin,
)
eTJ::MonthlyMax_strategy = st.builds(
    eTJ::MonthlyMax,
)
eTJ::Maximum_strategy = st.builds(
    eTJ::Maximum,
)
eTJ::WeeklyMax_strategy = st.builds(
    eTJ::WeeklyMax,
)
eTJ::Minimum_strategy = st.builds(
    eTJ::Minimum,
)
eTJ::WeeklyMin_strategy = st.builds(
    eTJ::WeeklyMin,
)
eTJ::DailyMax_strategy = st.builds(
    eTJ::DailyMax,
)
ProjectAttribute_strategy = st.builds(
    ProjectAttribute,
)
eTJ::ShortTimeFormat_strategy = st.builds(
    eTJ::ShortTimeFormat,
    shortTimeFormat=
        safe_text
)
eTJ::WorkingHours_strategy = st.builds(
    eTJ::WorkingHours,
    off=
        st.booleans()
)
eTJ::Include_strategy = st.builds(
    eTJ::Include,
    importURI=
        safe_text
)
eTJ::TimingResolution_strategy = st.builds(
    eTJ::TimingResolution,
    timingResolution=
        st.integers()
)
eTJ::TrackingScenario_strategy = st.builds(
    eTJ::TrackingScenario,
)
eTJ::WeekStarts_strategy = st.builds(
    eTJ::WeekStarts,
    sunday=
        st.booleans(),
    monday=
        st.booleans()
)
eTJ::ExtendResource_strategy = st.builds(
    eTJ::ExtendResource,
)
eTJ::TimeFormat_strategy = st.builds(
    eTJ::TimeFormat,
    timeformat=
        safe_text
)
eTJ::DailyWorkingHours_strategy = st.builds(
    eTJ::DailyWorkingHours,
    dailyWorkingHours=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ::Now_strategy = st.builds(
    eTJ::Now,
)
eTJ::JournalEntry_strategy = st.builds(
    eTJ::JournalEntry,
    headline=
        safe_text
)
eTJ::ExtendTask_strategy = st.builds(
    eTJ::ExtendTask,
)
eTJ::NumberFormat_strategy = st.builds(
    eTJ::NumberFormat,
)
eTJ::Timezone_strategy = st.builds(
    eTJ::Timezone,
    timezone=
        safe_text
)
eTJ::YearlyWorkingDays_strategy = st.builds(
    eTJ::YearlyWorkingDays,
    yearlyWorkingDays=
        st.integers()
)
eTJ::CurrencyFormat_strategy = st.builds(
    eTJ::CurrencyFormat,
)
eTJ::Currency_strategy = st.builds(
    eTJ::Currency,
    currency=
        safe_text
)
eTJ::ISODATE_strategy = st.builds(
    eTJ::ISODATE,
)
eTJ::Credit_strategy = st.builds(
    eTJ::Credit,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    description=
        safe_text
)
eTJ::Copyright_strategy = st.builds(
    eTJ::Copyright,
    text=
        safe_text
)
eTJ::Complete_strategy = st.builds(
    eTJ::Complete,
    complete=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eTJ::Column_strategy = st.builds(
    eTJ::Column,
    id=
        safe_text
)
eTJ::Columns_strategy = st.builds(
    eTJ::Columns,
)
eTJ::Interval4_strategy = st.builds(
    eTJ::Interval4,
)
eTJ::Booking_strategy = st.builds(
    eTJ::Booking,
    overtime=
        st.integers(),
    sloppy=
        st.integers()
)
eTJ::BookingResource_strategy = st.builds(
    eTJ::BookingResource,
)
eTJ::BookingTask_strategy = st.builds(
    eTJ::BookingTask,
)
eTJ::NavigatorAttribute_strategy = st.builds(
    eTJ::NavigatorAttribute,
)
eTJ::Navigator_strategy = st.builds(
    eTJ::Navigator,
    id=
        safe_text
)
eTJ::AllocateResourceAttribute_strategy = st.builds(
    eTJ::AllocateResourceAttribute,
)
eTJ::AllocateResource_strategy = st.builds(
    eTJ::AllocateResource,
)
eTJ::Allocate_strategy = st.builds(
    eTJ::Allocate,
)
eTJ::ResourceAttribute_strategy = st.builds(
    eTJ::ResourceAttribute,
)
eTJ::Resource_strategy = st.builds(
    eTJ::Resource,
    name=
        safe_text,
    id=
        safe_text
)
eTJ::Balance_strategy = st.builds(
    eTJ::Balance,
)
StatusStatusSheetAttribute_strategy = st.builds(
    StatusStatusSheetAttribute,
)
eTJ::Flags_strategy = st.builds(
    eTJ::Flags,
    flags=
        safe_text
)
eTJ::Summary_strategy = st.builds(
    eTJ::Summary,
)
eTJ::Details_strategy = st.builds(
    eTJ::Details,
)
eTJ::Author_strategy = st.builds(
    eTJ::Author,
)
AllocateResourceAttribute_strategy = st.builds(
    AllocateResourceAttribute,
)
eTJ::ShiftsAllocate_strategy = st.builds(
    eTJ::ShiftsAllocate,
)
eTJ::Persistent_strategy = st.builds(
    eTJ::Persistent,
    persistent=
        st.booleans()
)
eTJ::Select_strategy = st.builds(
    eTJ::Select,
    argument=
        safe_text
)
eTJ::Mandatory_strategy = st.builds(
    eTJ::Mandatory,
    mandatory=
        st.booleans()
)
eTJ::Alternative_strategy = st.builds(
    eTJ::Alternative,
)
eTJ::Alert_strategy = st.builds(
    eTJ::Alert,
    level=
        safe_text
)
eTJ::NikuReportAttribute_strategy = st.builds(
    eTJ::NikuReportAttribute,
)
eTJ::NikuReport_strategy = st.builds(
    eTJ::NikuReport,
    filename=
        safe_text
)
eTJ::NewTaskAttribute_strategy = st.builds(
    eTJ::NewTaskAttribute,
)
TimesheetAttribute_strategy = st.builds(
    TimesheetAttribute,
)
eTJ::ShiftTimesheet_strategy = st.builds(
    eTJ::ShiftTimesheet,
)
eTJ::TaskTimesheet_strategy = st.builds(
    eTJ::TaskTimesheet,
)
eTJ::StatusTimesheet_strategy = st.builds(
    eTJ::StatusTimesheet,
    text=
        safe_text,
    level=
        safe_text
)
eTJ::NewTask_strategy = st.builds(
    eTJ::NewTask,
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
eTJ::MacroCall_strategy = st.builds(
    eTJ::MacroCall,
    buildin=
        safe_text
)
eTJ::EObject_strategy = st.builds(
    eTJ::EObject,
)
eTJ::Scenario_strategy = st.builds(
    eTJ::Scenario,
    name=
        safe_text,
    id=
        safe_text,
    active=
        safe_text
)
eTJ::TaskAttribute_strategy = st.builds(
    eTJ::TaskAttribute,
)
eTJ::Task_strategy = st.builds(
    eTJ::Task,
    name=
        safe_text,
    id=
        safe_text
)
eTJ::ProjectAttribute_strategy = st.builds(
    eTJ::ProjectAttribute,
)
eTJ::ExportAttribute_strategy = st.builds(
    eTJ::ExportAttribute,
)
eTJ::Export_strategy = st.builds(
    eTJ::Export,
    filename=
        safe_text,
    id=
        safe_text
)
eTJ::IcalReportAttribute_strategy = st.builds(
    eTJ::IcalReportAttribute,
)
eTJ::IcalReport_strategy = st.builds(
    eTJ::IcalReport,
    filename=
        safe_text
)
eTJ::ReportAttribute_strategy = st.builds(
    eTJ::ReportAttribute,
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
eTJ::Report_strategy = st.builds(
    eTJ::Report,
    name=
        safe_text,
    id=
        safe_text
)

@given(instance=LogicalExpression_strategy)
@settings(max_examples=50)
def test_logicalexpression_instantiation(instance):
    assert isinstance(instance, LogicalExpression)

@given(instance=eTJ::LogicalAbsoluteIdExression_strategy)
@settings(max_examples=50)
def test_etj::logicalabsoluteidexression_instantiation(instance):
    assert isinstance(instance, eTJ::LogicalAbsoluteIdExression)

@given(instance=eTJ::LogicalAbsoluteIdExression_strategy)
def test_etj::logicalabsoluteidexression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=eTJ::LogicalAbsoluteIdExression_strategy)
def test_etj::logicalabsoluteidexression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ::LogicalNumeralLiteral_strategy)
@settings(max_examples=50)
def test_etj::logicalnumeralliteral_instantiation(instance):
    assert isinstance(instance, eTJ::LogicalNumeralLiteral)

@given(instance=eTJ::LogicalNumeralLiteral_strategy)
def test_etj::logicalnumeralliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=eTJ::LogicalNumeralLiteral_strategy)
def test_etj::logicalnumeralliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ::LogicalBooleanLiteral_strategy)
@settings(max_examples=50)
def test_etj::logicalbooleanliteral_instantiation(instance):
    assert isinstance(instance, eTJ::LogicalBooleanLiteral)

@given(instance=eTJ::LogicalBooleanLiteral_strategy)
def test_etj::logicalbooleanliteral_isTrue_type(instance):
    assert isinstance(instance.isTrue, bool)


@given(instance=eTJ::LogicalBooleanLiteral_strategy)
def test_etj::logicalbooleanliteral_isTrue_setter(instance):
    original = instance.isTrue
    instance.isTrue = original
    assert instance.isTrue == original

@given(instance=eTJ::LogicalDateLiteral_strategy)
@settings(max_examples=50)
def test_etj::logicaldateliteral_instantiation(instance):
    assert isinstance(instance, eTJ::LogicalDateLiteral)

@given(instance=eTJ::LogicalFlagExpression_strategy)
@settings(max_examples=50)
def test_etj::logicalflagexpression_instantiation(instance):
    assert isinstance(instance, eTJ::LogicalFlagExpression)

@given(instance=eTJ::LogicalFlagExpression_strategy)
def test_etj::logicalflagexpression_columId_type(instance):
    assert isinstance(instance.columId, str)


@given(instance=eTJ::LogicalFlagExpression_strategy)
def test_etj::logicalflagexpression_columId_setter(instance):
    original = instance.columId
    instance.columId = original
    assert instance.columId == original

@given(instance=eTJ::LogicalStringLiteral_strategy)
@settings(max_examples=50)
def test_etj::logicalstringliteral_instantiation(instance):
    assert isinstance(instance, eTJ::LogicalStringLiteral)

@given(instance=eTJ::LogicalStringLiteral_strategy)
def test_etj::logicalstringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=eTJ::LogicalStringLiteral_strategy)
def test_etj::logicalstringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ::LogicalFunctionExpression_strategy)
@settings(max_examples=50)
def test_etj::logicalfunctionexpression_instantiation(instance):
    assert isinstance(instance, eTJ::LogicalFunctionExpression)

@given(instance=Definitions_strategy)
@settings(max_examples=50)
def test_definitions_instantiation(instance):
    assert isinstance(instance, Definitions)

@given(instance=eTJ::Defintions_strategy)
@settings(max_examples=50)
def test_etj::defintions_instantiation(instance):
    assert isinstance(instance, eTJ::Defintions)

@given(instance=eTJ::Defintions_strategy)
def test_etj::defintions_tasks_type(instance):
    assert isinstance(instance.tasks, bool)


@given(instance=eTJ::Defintions_strategy)
def test_etj::defintions_tasks_setter(instance):
    original = instance.tasks
    instance.tasks = original
    assert instance.tasks == original

@given(instance=eTJ::Defintions_strategy)
def test_etj::defintions_projectids_type(instance):
    assert isinstance(instance.projectids, bool)


@given(instance=eTJ::Defintions_strategy)
def test_etj::defintions_projectids_setter(instance):
    original = instance.projectids
    instance.projectids = original
    assert instance.projectids == original

@given(instance=eTJ::Defintions_strategy)
def test_etj::defintions_resources_type(instance):
    assert isinstance(instance.resources, bool)


@given(instance=eTJ::Defintions_strategy)
def test_etj::defintions_resources_setter(instance):
    original = instance.resources
    instance.resources = original
    assert instance.resources == original

@given(instance=eTJ::Defintions_strategy)
def test_etj::defintions_project_type(instance):
    assert isinstance(instance.project, bool)


@given(instance=eTJ::Defintions_strategy)
def test_etj::defintions_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original

@given(instance=eTJ::Defintions_strategy)
def test_etj::defintions_flags_type(instance):
    assert isinstance(instance.flags, bool)


@given(instance=eTJ::Defintions_strategy)
def test_etj::defintions_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original

@given(instance=eTJ::ExtDate_strategy)
@settings(max_examples=50)
def test_etj::extdate_instantiation(instance):
    assert isinstance(instance, eTJ::ExtDate)

@given(instance=NumberFormat_strategy)
@settings(max_examples=50)
def test_numberformat_instantiation(instance):
    assert isinstance(instance, NumberFormat)

@given(instance=CurrencyFormat_strategy)
@settings(max_examples=50)
def test_currencyformat_instantiation(instance):
    assert isinstance(instance, CurrencyFormat)

@given(instance=eTJ::RealFormat_strategy)
@settings(max_examples=50)
def test_etj::realformat_instantiation(instance):
    assert isinstance(instance, eTJ::RealFormat)

@given(instance=eTJ::RealFormat_strategy)
def test_etj::realformat_thousandsSeparator_type(instance):
    assert isinstance(instance.thousandsSeparator, str)


@given(instance=eTJ::RealFormat_strategy)
def test_etj::realformat_thousandsSeparator_setter(instance):
    original = instance.thousandsSeparator
    instance.thousandsSeparator = original
    assert instance.thousandsSeparator == original

@given(instance=eTJ::RealFormat_strategy)
def test_etj::realformat_fractionDigits_type(instance):
    assert isinstance(instance.fractionDigits, int)


@given(instance=eTJ::RealFormat_strategy)
def test_etj::realformat_fractionDigits_setter(instance):
    original = instance.fractionDigits
    instance.fractionDigits = original
    assert instance.fractionDigits == original

@given(instance=eTJ::RealFormat_strategy)
def test_etj::realformat_negativeSuffix_type(instance):
    assert isinstance(instance.negativeSuffix, str)


@given(instance=eTJ::RealFormat_strategy)
def test_etj::realformat_negativeSuffix_setter(instance):
    original = instance.negativeSuffix
    instance.negativeSuffix = original
    assert instance.negativeSuffix == original

@given(instance=eTJ::RealFormat_strategy)
def test_etj::realformat_negativePrefix_type(instance):
    assert isinstance(instance.negativePrefix, str)


@given(instance=eTJ::RealFormat_strategy)
def test_etj::realformat_negativePrefix_setter(instance):
    original = instance.negativePrefix
    instance.negativePrefix = original
    assert instance.negativePrefix == original

@given(instance=eTJ::RealFormat_strategy)
def test_etj::realformat_fractionSeparator_type(instance):
    assert isinstance(instance.fractionSeparator, str)


@given(instance=eTJ::RealFormat_strategy)
def test_etj::realformat_fractionSeparator_setter(instance):
    original = instance.fractionSeparator
    instance.fractionSeparator = original
    assert instance.fractionSeparator == original

@given(instance=eTJ::LimitAttribute_strategy)
@settings(max_examples=50)
def test_etj::limitattribute_instantiation(instance):
    assert isinstance(instance, eTJ::LimitAttribute)

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

@given(instance=eTJ::RichText_strategy)
@settings(max_examples=50)
def test_etj::richtext_instantiation(instance):
    assert isinstance(instance, eTJ::RichText)

@given(instance=eTJ::RichText_strategy)
def test_etj::richtext_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=eTJ::RichText_strategy)
def test_etj::richtext_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Precedes_strategy)
@settings(max_examples=50)
def test_precedes_instantiation(instance):
    assert isinstance(instance, Precedes)

@given(instance=eTJ::ColumnAttribute_strategy)
@settings(max_examples=50)
def test_etj::columnattribute_instantiation(instance):
    assert isinstance(instance, eTJ::ColumnAttribute)

@given(instance=eTJ::WorkHours_strategy)
@settings(max_examples=50)
def test_etj::workhours_instantiation(instance):
    assert isinstance(instance, eTJ::WorkHours)

@given(instance=eTJ::WorkHours_strategy)
def test_etj::workhours_stop_type(instance):
    assert isinstance(instance.stop, str)


@given(instance=eTJ::WorkHours_strategy)
def test_etj::workhours_stop_setter(instance):
    original = instance.stop
    instance.stop = original
    assert instance.stop == original

@given(instance=eTJ::WorkHours_strategy)
def test_etj::workhours_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=eTJ::WorkHours_strategy)
def test_etj::workhours_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=eTJ::Weekdays_strategy)
@settings(max_examples=50)
def test_etj::weekdays_instantiation(instance):
    assert isinstance(instance, eTJ::Weekdays)

@given(instance=eTJ::Weekdays_strategy)
def test_etj::weekdays_first_type(instance):
    assert isinstance(instance.first, str)


@given(instance=eTJ::Weekdays_strategy)
def test_etj::weekdays_first_setter(instance):
    original = instance.first
    instance.first = original
    assert instance.first == original

@given(instance=eTJ::Weekdays_strategy)
def test_etj::weekdays_last_type(instance):
    assert isinstance(instance.last, str)


@given(instance=eTJ::Weekdays_strategy)
def test_etj::weekdays_last_setter(instance):
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

@given(instance=eTJ::Limit_strategy)
@settings(max_examples=50)
def test_etj::limit_instantiation(instance):
    assert isinstance(instance, eTJ::Limit)

@given(instance=GapLength_strategy)
@settings(max_examples=50)
def test_gaplength_instantiation(instance):
    assert isinstance(instance, GapLength)

@given(instance=GapDuration_strategy)
@settings(max_examples=50)
def test_gapduration_instantiation(instance):
    assert isinstance(instance, GapDuration)

@given(instance=eTJ::TreeLevel_strategy)
@settings(max_examples=50)
def test_etj::treelevel_instantiation(instance):
    assert isinstance(instance, eTJ::TreeLevel)

@given(instance=eTJ::TreeLevel_strategy)
def test_etj::treelevel_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=eTJ::TreeLevel_strategy)
def test_etj::treelevel_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=eTJ::TimesheetReportAttribute_strategy)
@settings(max_examples=50)
def test_etj::timesheetreportattribute_instantiation(instance):
    assert isinstance(instance, eTJ::TimesheetReportAttribute)

@given(instance=eTJ::TimesheetAttribute_strategy)
@settings(max_examples=50)
def test_etj::timesheetattribute_instantiation(instance):
    assert isinstance(instance, eTJ::TimesheetAttribute)

@given(instance=eTJ::TaskTimesheetAttribute_strategy)
@settings(max_examples=50)
def test_etj::tasktimesheetattribute_instantiation(instance):
    assert isinstance(instance, eTJ::TaskTimesheetAttribute)

@given(instance=eTJ::TaskStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_etj::taskstatussheetattribute_instantiation(instance):
    assert isinstance(instance, eTJ::TaskStatusSheetAttribute)

@given(instance=StatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_statussheetattribute_instantiation(instance):
    assert isinstance(instance, StatusSheetAttribute)

@given(instance=eTJ::StatusSheetReportAttribute_strategy)
@settings(max_examples=50)
def test_etj::statussheetreportattribute_instantiation(instance):
    assert isinstance(instance, eTJ::StatusSheetReportAttribute)

@given(instance=eTJ::StatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_etj::statussheetattribute_instantiation(instance):
    assert isinstance(instance, eTJ::StatusSheetAttribute)

@given(instance=eTJ::Criterion_strategy)
@settings(max_examples=50)
def test_etj::criterion_instantiation(instance):
    assert isinstance(instance, eTJ::Criterion)

@given(instance=eTJ::Criterion_strategy)
def test_etj::criterion_columnId_type(instance):
    assert isinstance(instance.columnId, str)


@given(instance=eTJ::Criterion_strategy)
def test_etj::criterion_columnId_setter(instance):
    original = instance.columnId
    instance.columnId = original
    assert instance.columnId == original

@given(instance=eTJ::Criterion_strategy)
def test_etj::criterion_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=eTJ::Criterion_strategy)
def test_etj::criterion_direction_setter(instance):
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

@given(instance=eTJ::Sort_strategy)
@settings(max_examples=50)
def test_etj::sort_instantiation(instance):
    assert isinstance(instance, eTJ::Sort)

@given(instance=eTJ::Sort_strategy)
def test_etj::sort_tree_type(instance):
    assert isinstance(instance.tree, bool)


@given(instance=eTJ::Sort_strategy)
def test_etj::sort_tree_setter(instance):
    original = instance.tree
    instance.tree = original
    assert instance.tree == original

@given(instance=eTJ::ShiftsTask_strategy)
@settings(max_examples=50)
def test_etj::shiftstask_instantiation(instance):
    assert isinstance(instance, eTJ::ShiftsTask)

@given(instance=eTJ::StatusTimesheetAttribute_strategy)
@settings(max_examples=50)
def test_etj::statustimesheetattribute_instantiation(instance):
    assert isinstance(instance, eTJ::StatusTimesheetAttribute)

@given(instance=eTJ::StatusStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_etj::statusstatussheetattribute_instantiation(instance):
    assert isinstance(instance, eTJ::StatusStatusSheetAttribute)

@given(instance=TaskStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_taskstatussheetattribute_instantiation(instance):
    assert isinstance(instance, TaskStatusSheetAttribute)

@given(instance=eTJ::TaskStatusSheet_strategy)
@settings(max_examples=50)
def test_etj::taskstatussheet_instantiation(instance):
    assert isinstance(instance, eTJ::TaskStatusSheet)

@given(instance=eTJ::StatusStatusSheet_strategy)
@settings(max_examples=50)
def test_etj::statusstatussheet_instantiation(instance):
    assert isinstance(instance, eTJ::StatusStatusSheet)

@given(instance=eTJ::StatusStatusSheet_strategy)
def test_etj::statusstatussheet_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=eTJ::StatusStatusSheet_strategy)
def test_etj::statusstatussheet_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=eTJ::StatusStatusSheet_strategy)
def test_etj::statusstatussheet_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=eTJ::StatusStatusSheet_strategy)
def test_etj::statusstatussheet_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=eTJ::Scheduling_strategy)
@settings(max_examples=50)
def test_etj::scheduling_instantiation(instance):
    assert isinstance(instance, eTJ::Scheduling)

@given(instance=eTJ::Scheduling_strategy)
def test_etj::scheduling_scheduling_type(instance):
    assert isinstance(instance.scheduling, str)


@given(instance=eTJ::Scheduling_strategy)
def test_etj::scheduling_scheduling_setter(instance):
    original = instance.scheduling
    instance.scheduling = original
    assert instance.scheduling == original

@given(instance=eTJ::Scheduled_strategy)
@settings(max_examples=50)
def test_etj::scheduled_instantiation(instance):
    assert isinstance(instance, eTJ::Scheduled)

@given(instance=eTJ::Scheduled_strategy)
def test_etj::scheduled_scheduled_type(instance):
    assert isinstance(instance.scheduled, bool)


@given(instance=eTJ::Scheduled_strategy)
def test_etj::scheduled_scheduled_setter(instance):
    original = instance.scheduled
    instance.scheduled = original
    assert instance.scheduled == original

@given(instance=eTJ::ShiftsLimit_strategy)
@settings(max_examples=50)
def test_etj::shiftslimit_instantiation(instance):
    assert isinstance(instance, eTJ::ShiftsLimit)

@given(instance=ShiftsTask_strategy)
@settings(max_examples=50)
def test_shiftstask_instantiation(instance):
    assert isinstance(instance, ShiftsTask)

@given(instance=ShiftsResource_strategy)
@settings(max_examples=50)
def test_shiftsresource_instantiation(instance):
    assert isinstance(instance, ShiftsResource)

@given(instance=eTJ::Shifts_strategy)
@settings(max_examples=50)
def test_etj::shifts_instantiation(instance):
    assert isinstance(instance, eTJ::Shifts)

@given(instance=eTJ::Responsible_strategy)
@settings(max_examples=50)
def test_etj::responsible_instantiation(instance):
    assert isinstance(instance, eTJ::Responsible)

@given(instance=eTJ::PurgeTask_strategy)
@settings(max_examples=50)
def test_etj::purgetask_instantiation(instance):
    assert isinstance(instance, eTJ::PurgeTask)

@given(instance=eTJ::PurgeTask_strategy)
def test_etj::purgetask_listAttribute_type(instance):
    assert isinstance(instance.listAttribute, str)


@given(instance=eTJ::PurgeTask_strategy)
def test_etj::purgetask_listAttribute_setter(instance):
    original = instance.listAttribute
    instance.listAttribute = original
    assert instance.listAttribute == original

@given(instance=eTJ::AccountAttribute_strategy)
@settings(max_examples=50)
def test_etj::accountattribute_instantiation(instance):
    assert isinstance(instance, eTJ::AccountAttribute)

@given(instance=AccountAttribute_strategy)
@settings(max_examples=50)
def test_accountattribute_instantiation(instance):
    assert isinstance(instance, AccountAttribute)

@given(instance=eTJ::Interval2_strategy)
@settings(max_examples=50)
def test_etj::interval2_instantiation(instance):
    assert isinstance(instance, eTJ::Interval2)

@given(instance=ReportAttribute_strategy)
@settings(max_examples=50)
def test_reportattribute_instantiation(instance):
    assert isinstance(instance, ReportAttribute)

@given(instance=eTJ::SortAccounts_strategy)
@settings(max_examples=50)
def test_etj::sortaccounts_instantiation(instance):
    assert isinstance(instance, eTJ::SortAccounts)

@given(instance=eTJ::SortJournalEntries_strategy)
@settings(max_examples=50)
def test_etj::sortjournalentries_instantiation(instance):
    assert isinstance(instance, eTJ::SortJournalEntries)

@given(instance=eTJ::SelfContained_strategy)
@settings(max_examples=50)
def test_etj::selfcontained_instantiation(instance):
    assert isinstance(instance, eTJ::SelfContained)

@given(instance=eTJ::SelfContained_strategy)
def test_etj::selfcontained_selfcontained_type(instance):
    assert isinstance(instance.selfcontained, str)


@given(instance=eTJ::SelfContained_strategy)
def test_etj::selfcontained_selfcontained_setter(instance):
    original = instance.selfcontained
    instance.selfcontained = original
    assert instance.selfcontained == original

@given(instance=eTJ::AccountRoot_strategy)
@settings(max_examples=50)
def test_etj::accountroot_instantiation(instance):
    assert isinstance(instance, eTJ::AccountRoot)

@given(instance=eTJ::RollupAccount_strategy)
@settings(max_examples=50)
def test_etj::rollupaccount_instantiation(instance):
    assert isinstance(instance, eTJ::RollupAccount)

@given(instance=eTJ::ResourceRoot_strategy)
@settings(max_examples=50)
def test_etj::resourceroot_instantiation(instance):
    assert isinstance(instance, eTJ::ResourceRoot)

@given(instance=eTJ::Right_strategy)
@settings(max_examples=50)
def test_etj::right_instantiation(instance):
    assert isinstance(instance, eTJ::Right)

@given(instance=eTJ::TaskRoot_strategy)
@settings(max_examples=50)
def test_etj::taskroot_instantiation(instance):
    assert isinstance(instance, eTJ::TaskRoot)

@given(instance=IncludePropertiesAttribute_strategy)
@settings(max_examples=50)
def test_includepropertiesattribute_instantiation(instance):
    assert isinstance(instance, IncludePropertiesAttribute)

@given(instance=eTJ::ReportPrefix_strategy)
@settings(max_examples=50)
def test_etj::reportprefix_instantiation(instance):
    assert isinstance(instance, eTJ::ReportPrefix)

@given(instance=eTJ::TaskPrefix_strategy)
@settings(max_examples=50)
def test_etj::taskprefix_instantiation(instance):
    assert isinstance(instance, eTJ::TaskPrefix)

@given(instance=eTJ::ResourcePrefix_strategy)
@settings(max_examples=50)
def test_etj::resourceprefix_instantiation(instance):
    assert isinstance(instance, eTJ::ResourcePrefix)

@given(instance=eTJ::AccountPrefix_strategy)
@settings(max_examples=50)
def test_etj::accountprefix_instantiation(instance):
    assert isinstance(instance, eTJ::AccountPrefix)

@given(instance=eTJ::Property_strategy)
@settings(max_examples=50)
def test_etj::property_instantiation(instance):
    assert isinstance(instance, eTJ::Property)

@given(instance=eTJ::Project_strategy)
@settings(max_examples=50)
def test_etj::project_instantiation(instance):
    assert isinstance(instance, eTJ::Project)

@given(instance=eTJ::Project_strategy)
def test_etj::project_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=eTJ::Project_strategy)
def test_etj::project_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ::Project_strategy)
def test_etj::project_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=eTJ::Project_strategy)
def test_etj::project_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=eTJ::Project_strategy)
def test_etj::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eTJ::Project_strategy)
def test_etj::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ::Global_strategy)
@settings(max_examples=50)
def test_etj::global_instantiation(instance):
    assert isinstance(instance, eTJ::Global)

@given(instance=eTJ::Interval3_strategy)
@settings(max_examples=50)
def test_etj::interval3_instantiation(instance):
    assert isinstance(instance, eTJ::Interval3)

@given(instance=eTJ::LeaveDetails_strategy)
@settings(max_examples=50)
def test_etj::leavedetails_instantiation(instance):
    assert isinstance(instance, eTJ::LeaveDetails)

@given(instance=eTJ::LeaveDetails_strategy)
def test_etj::leavedetails_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=eTJ::LeaveDetails_strategy)
def test_etj::leavedetails_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=eTJ::LeaveDetails_strategy)
def test_etj::leavedetails_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eTJ::LeaveDetails_strategy)
def test_etj::leavedetails_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ResourceAttribute_strategy)
@settings(max_examples=50)
def test_resourceattribute_instantiation(instance):
    assert isinstance(instance, ResourceAttribute)

@given(instance=eTJ::PurgeResource_strategy)
@settings(max_examples=50)
def test_etj::purgeresource_instantiation(instance):
    assert isinstance(instance, eTJ::PurgeResource)

@given(instance=eTJ::PurgeResource_strategy)
def test_etj::purgeresource_listAttribute_type(instance):
    assert isinstance(instance.listAttribute, str)


@given(instance=eTJ::PurgeResource_strategy)
def test_etj::purgeresource_listAttribute_setter(instance):
    original = instance.listAttribute
    instance.listAttribute = original
    assert instance.listAttribute == original

@given(instance=eTJ::ShiftsResource_strategy)
@settings(max_examples=50)
def test_etj::shiftsresource_instantiation(instance):
    assert isinstance(instance, eTJ::ShiftsResource)

@given(instance=eTJ::Warn_strategy)
@settings(max_examples=50)
def test_etj::warn_instantiation(instance):
    assert isinstance(instance, eTJ::Warn)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=eTJ::Shift_strategy)
@settings(max_examples=50)
def test_etj::shift_instantiation(instance):
    assert isinstance(instance, eTJ::Shift)

@given(instance=eTJ::Shift_strategy)
def test_etj::shift_replace_type(instance):
    assert isinstance(instance.replace, str)


@given(instance=eTJ::Shift_strategy)
def test_etj::shift_replace_setter(instance):
    original = instance.replace
    instance.replace = original
    assert instance.replace == original

@given(instance=eTJ::Shift_strategy)
def test_etj::shift_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eTJ::Shift_strategy)
def test_etj::shift_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ::Shift_strategy)
def test_etj::shift_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=eTJ::Shift_strategy)
def test_etj::shift_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ::Shift_strategy)
def test_etj::shift_timezone_type(instance):
    assert isinstance(instance.timezone, str)


@given(instance=eTJ::Shift_strategy)
def test_etj::shift_timezone_setter(instance):
    original = instance.timezone
    instance.timezone = original
    assert instance.timezone == original

@given(instance=eTJ::TagFile_strategy)
@settings(max_examples=50)
def test_etj::tagfile_instantiation(instance):
    assert isinstance(instance, eTJ::TagFile)

@given(instance=eTJ::TagFile_strategy)
def test_etj::tagfile_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=eTJ::TagFile_strategy)
def test_etj::tagfile_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ::TagFile_strategy)
def test_etj::tagfile_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=eTJ::TagFile_strategy)
def test_etj::tagfile_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=eTJ::Macro_strategy)
@settings(max_examples=50)
def test_etj::macro_instantiation(instance):
    assert isinstance(instance, eTJ::Macro)

@given(instance=eTJ::Macro_strategy)
def test_etj::macro_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=eTJ::Macro_strategy)
def test_etj::macro_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ::Macro_strategy)
def test_etj::macro_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=eTJ::Macro_strategy)
def test_etj::macro_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ::TextReport_strategy)
@settings(max_examples=50)
def test_etj::textreport_instantiation(instance):
    assert isinstance(instance, eTJ::TextReport)

@given(instance=eTJ::SupplementTask_strategy)
@settings(max_examples=50)
def test_etj::supplementtask_instantiation(instance):
    assert isinstance(instance, eTJ::SupplementTask)

@given(instance=eTJ::ResourceReport_strategy)
@settings(max_examples=50)
def test_etj::resourcereport_instantiation(instance):
    assert isinstance(instance, eTJ::ResourceReport)

@given(instance=eTJ::SupplementReport_strategy)
@settings(max_examples=50)
def test_etj::supplementreport_instantiation(instance):
    assert isinstance(instance, eTJ::SupplementReport)

@given(instance=eTJ::TimesheetReport_strategy)
@settings(max_examples=50)
def test_etj::timesheetreport_instantiation(instance):
    assert isinstance(instance, eTJ::TimesheetReport)

@given(instance=eTJ::TimesheetReport_strategy)
def test_etj::timesheetreport_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=eTJ::TimesheetReport_strategy)
def test_etj::timesheetreport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=eTJ::StatusSheetReport_strategy)
@settings(max_examples=50)
def test_etj::statussheetreport_instantiation(instance):
    assert isinstance(instance, eTJ::StatusSheetReport)

@given(instance=eTJ::StatusSheetReport_strategy)
def test_etj::statussheetreport_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=eTJ::StatusSheetReport_strategy)
def test_etj::statussheetreport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=eTJ::AccountReport_strategy)
@settings(max_examples=50)
def test_etj::accountreport_instantiation(instance):
    assert isinstance(instance, eTJ::AccountReport)

@given(instance=eTJ::Rate_strategy)
@settings(max_examples=50)
def test_etj::rate_instantiation(instance):
    assert isinstance(instance, eTJ::Rate)

@given(instance=eTJ::Rate_strategy)
def test_etj::rate_rate_type(instance):
    assert isinstance(instance.rate, float)


@given(instance=eTJ::Rate_strategy)
def test_etj::rate_rate_setter(instance):
    original = instance.rate
    instance.rate = original
    assert instance.rate == original

@given(instance=eTJ::TaskReport_strategy)
@settings(max_examples=50)
def test_etj::taskreport_instantiation(instance):
    assert isinstance(instance, eTJ::TaskReport)

@given(instance=eTJ::Vacation_strategy)
@settings(max_examples=50)
def test_etj::vacation_instantiation(instance):
    assert isinstance(instance, eTJ::Vacation)

@given(instance=eTJ::Vacation_strategy)
def test_etj::vacation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eTJ::Vacation_strategy)
def test_etj::vacation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ::Timesheet_strategy)
@settings(max_examples=50)
def test_etj::timesheet_instantiation(instance):
    assert isinstance(instance, eTJ::Timesheet)

@given(instance=eTJ::SupplementAccount_strategy)
@settings(max_examples=50)
def test_etj::supplementaccount_instantiation(instance):
    assert isinstance(instance, eTJ::SupplementAccount)

@given(instance=eTJ::Account_strategy)
@settings(max_examples=50)
def test_etj::account_instantiation(instance):
    assert isinstance(instance, eTJ::Account)

@given(instance=eTJ::Account_strategy)
def test_etj::account_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eTJ::Account_strategy)
def test_etj::account_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ::Account_strategy)
def test_etj::account_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=eTJ::Account_strategy)
def test_etj::account_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ::StatusSheet_strategy)
@settings(max_examples=50)
def test_etj::statussheet_instantiation(instance):
    assert isinstance(instance, eTJ::StatusSheet)

@given(instance=eTJ::SupplementResource_strategy)
@settings(max_examples=50)
def test_etj::supplementresource_instantiation(instance):
    assert isinstance(instance, eTJ::SupplementResource)

@given(instance=eTJ::Leaves_strategy)
@settings(max_examples=50)
def test_etj::leaves_instantiation(instance):
    assert isinstance(instance, eTJ::Leaves)

@given(instance=eTJ::Note_strategy)
@settings(max_examples=50)
def test_etj::note_instantiation(instance):
    assert isinstance(instance, eTJ::Note)

@given(instance=eTJ::Note_strategy)
def test_etj::note_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=eTJ::Note_strategy)
def test_etj::note_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=eTJ::PurgeReport_strategy)
@settings(max_examples=50)
def test_etj::purgereport_instantiation(instance):
    assert isinstance(instance, eTJ::PurgeReport)

@given(instance=eTJ::PurgeReport_strategy)
def test_etj::purgereport_listAttribute_type(instance):
    assert isinstance(instance.listAttribute, str)


@given(instance=eTJ::PurgeReport_strategy)
def test_etj::purgereport_listAttribute_setter(instance):
    original = instance.listAttribute
    instance.listAttribute = original
    assert instance.listAttribute == original

@given(instance=eTJ::Prolog_strategy)
@settings(max_examples=50)
def test_etj::prolog_instantiation(instance):
    assert isinstance(instance, eTJ::Prolog)

@given(instance=eTJ::ProjectIds_strategy)
@settings(max_examples=50)
def test_etj::projectids_instantiation(instance):
    assert isinstance(instance, eTJ::ProjectIds)

@given(instance=eTJ::ProjectIds_strategy)
def test_etj::projectids_ids_type(instance):
    assert isinstance(instance.ids, str)


@given(instance=eTJ::ProjectIds_strategy)
def test_etj::projectids_ids_setter(instance):
    original = instance.ids
    instance.ids = original
    assert instance.ids == original

@given(instance=eTJ::ProjectId_strategy)
@settings(max_examples=50)
def test_etj::projectid_instantiation(instance):
    assert isinstance(instance, eTJ::ProjectId)

@given(instance=eTJ::ProjectId_strategy)
def test_etj::projectid_projectId_type(instance):
    assert isinstance(instance.projectId, str)


@given(instance=eTJ::ProjectId_strategy)
def test_etj::projectid_projectId_setter(instance):
    original = instance.projectId
    instance.projectId = original
    assert instance.projectId == original

@given(instance=eTJ::Precedes_strategy)
@settings(max_examples=50)
def test_etj::precedes_instantiation(instance):
    assert isinstance(instance, eTJ::Precedes)

@given(instance=eTJ::LoadUnit_strategy)
@settings(max_examples=50)
def test_etj::loadunit_instantiation(instance):
    assert isinstance(instance, eTJ::LoadUnit)

@given(instance=eTJ::LoadUnit_strategy)
def test_etj::loadunit_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=eTJ::LoadUnit_strategy)
def test_etj::loadunit_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=eTJ::LimitsAttribute_strategy)
@settings(max_examples=50)
def test_etj::limitsattribute_instantiation(instance):
    assert isinstance(instance, eTJ::LimitsAttribute)

@given(instance=eTJ::Limits_strategy)
@settings(max_examples=50)
def test_etj::limits_instantiation(instance):
    assert isinstance(instance, eTJ::Limits)

@given(instance=eTJ::MinStart_strategy)
@settings(max_examples=50)
def test_etj::minstart_instantiation(instance):
    assert isinstance(instance, eTJ::MinStart)

@given(instance=eTJ::MinEnd_strategy)
@settings(max_examples=50)
def test_etj::minend_instantiation(instance):
    assert isinstance(instance, eTJ::MinEnd)

@given(instance=eTJ::Milestone_strategy)
@settings(max_examples=50)
def test_etj::milestone_instantiation(instance):
    assert isinstance(instance, eTJ::Milestone)

@given(instance=eTJ::Milestone_strategy)
def test_etj::milestone_milestone_type(instance):
    assert isinstance(instance.milestone, bool)


@given(instance=eTJ::Milestone_strategy)
def test_etj::milestone_milestone_setter(instance):
    original = instance.milestone
    instance.milestone = original
    assert instance.milestone == original

@given(instance=eTJ::MaxStart_strategy)
@settings(max_examples=50)
def test_etj::maxstart_instantiation(instance):
    assert isinstance(instance, eTJ::MaxStart)

@given(instance=eTJ::MaxEnd_strategy)
@settings(max_examples=50)
def test_etj::maxend_instantiation(instance):
    assert isinstance(instance, eTJ::MaxEnd)

@given(instance=eTJ::Managers_strategy)
@settings(max_examples=50)
def test_etj::managers_instantiation(instance):
    assert isinstance(instance, eTJ::Managers)

@given(instance=eTJ::JournalAttributes_strategy)
@settings(max_examples=50)
def test_etj::journalattributes_instantiation(instance):
    assert isinstance(instance, eTJ::JournalAttributes)

@given(instance=eTJ::JournalAttributes_strategy)
def test_etj::journalattributes_args_type(instance):
    assert isinstance(instance.args, str)


@given(instance=eTJ::JournalAttributes_strategy)
def test_etj::journalattributes_args_setter(instance):
    original = instance.args
    instance.args = original
    assert instance.args == original

@given(instance=eTJ::Length_strategy)
@settings(max_examples=50)
def test_etj::length_instantiation(instance):
    assert isinstance(instance, eTJ::Length)

@given(instance=eTJ::Left_strategy)
@settings(max_examples=50)
def test_etj::left_instantiation(instance):
    assert isinstance(instance, eTJ::Left)

@given(instance=eTJ::JournalMode_strategy)
@settings(max_examples=50)
def test_etj::journalmode_instantiation(instance):
    assert isinstance(instance, eTJ::JournalMode)

@given(instance=eTJ::JournalMode_strategy)
def test_etj::journalmode_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=eTJ::JournalMode_strategy)
def test_etj::journalmode_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=NavigatorAttribute_strategy)
@settings(max_examples=50)
def test_navigatorattribute_instantiation(instance):
    assert isinstance(instance, NavigatorAttribute)

@given(instance=eTJ::HideReport_strategy)
@settings(max_examples=50)
def test_etj::hidereport_instantiation(instance):
    assert isinstance(instance, eTJ::HideReport)

@given(instance=eTJ::Interval1_strategy)
@settings(max_examples=50)
def test_etj::interval1_instantiation(instance):
    assert isinstance(instance, eTJ::Interval1)

@given(instance=eTJ::IncludePropertiesAttribute_strategy)
@settings(max_examples=50)
def test_etj::includepropertiesattribute_instantiation(instance):
    assert isinstance(instance, eTJ::IncludePropertiesAttribute)

@given(instance=eTJ::IncludeProperties_strategy)
@settings(max_examples=50)
def test_etj::includeproperties_instantiation(instance):
    assert isinstance(instance, eTJ::IncludeProperties)

@given(instance=eTJ::IncludeProperties_strategy)
def test_etj::includeproperties_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=eTJ::IncludeProperties_strategy)
def test_etj::includeproperties_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=eTJ::Footer_strategy)
@settings(max_examples=50)
def test_etj::footer_instantiation(instance):
    assert isinstance(instance, eTJ::Footer)

@given(instance=eTJ::Fail_strategy)
@settings(max_examples=50)
def test_etj::fail_instantiation(instance):
    assert isinstance(instance, eTJ::Fail)

@given(instance=eTJ::ExtendedTaskAttribute_strategy)
@settings(max_examples=50)
def test_etj::extendedtaskattribute_instantiation(instance):
    assert isinstance(instance, eTJ::ExtendedTaskAttribute)

@given(instance=eTJ::ExtendedTaskAttribute_strategy)
def test_etj::extendedtaskattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=eTJ::ExtendedTaskAttribute_strategy)
def test_etj::extendedtaskattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ::HideAccount_strategy)
@settings(max_examples=50)
def test_etj::hideaccount_instantiation(instance):
    assert isinstance(instance, eTJ::HideAccount)

@given(instance=eTJ::HideAccount_strategy)
def test_etj::hideaccount_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=eTJ::HideAccount_strategy)
def test_etj::hideaccount_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=eTJ::Header_strategy)
@settings(max_examples=50)
def test_etj::header_instantiation(instance):
    assert isinstance(instance, eTJ::Header)

@given(instance=eTJ::GapLength_strategy)
@settings(max_examples=50)
def test_etj::gaplength_instantiation(instance):
    assert isinstance(instance, eTJ::GapLength)

@given(instance=eTJ::GapDuration_strategy)
@settings(max_examples=50)
def test_etj::gapduration_instantiation(instance):
    assert isinstance(instance, eTJ::GapDuration)

@given(instance=eTJ::Function_strategy)
@settings(max_examples=50)
def test_etj::function_instantiation(instance):
    assert isinstance(instance, eTJ::Function)

@given(instance=eTJ::Function_strategy)
def test_etj::function_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=eTJ::Function_strategy)
def test_etj::function_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=eTJ::Function_strategy)
def test_etj::function_parentId_type(instance):
    assert isinstance(instance.parentId, str)


@given(instance=eTJ::Function_strategy)
def test_etj::function_parentId_setter(instance):
    original = instance.parentId
    instance.parentId = original
    assert instance.parentId == original

@given(instance=eTJ::Function_strategy)
def test_etj::function_distance_type(instance):
    assert isinstance(instance.distance, int)


@given(instance=eTJ::Function_strategy)
def test_etj::function_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=NewTaskAttribute_strategy)
@settings(max_examples=50)
def test_newtaskattribute_instantiation(instance):
    assert isinstance(instance, NewTaskAttribute)

@given(instance=IcalReportAttribute_strategy)
@settings(max_examples=50)
def test_icalreportattribute_instantiation(instance):
    assert isinstance(instance, IcalReportAttribute)

@given(instance=eTJ::ScenarioIcal_strategy)
@settings(max_examples=50)
def test_etj::scenarioical_instantiation(instance):
    assert isinstance(instance, eTJ::ScenarioIcal)

@given(instance=eTJ::HideJournalEntry_strategy)
@settings(max_examples=50)
def test_etj::hidejournalentry_instantiation(instance):
    assert isinstance(instance, eTJ::HideJournalEntry)

@given(instance=eTJ::HideJournalEntry_strategy)
def test_etj::hidejournalentry_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=eTJ::HideJournalEntry_strategy)
def test_etj::hidejournalentry_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=eTJ::Email_strategy)
@settings(max_examples=50)
def test_etj::email_instantiation(instance):
    assert isinstance(instance, eTJ::Email)

@given(instance=eTJ::Email_strategy)
def test_etj::email_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=eTJ::Email_strategy)
def test_etj::email_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=eTJ::Effort_strategy)
@settings(max_examples=50)
def test_etj::effort_instantiation(instance):
    assert isinstance(instance, eTJ::Effort)

@given(instance=eTJ::Efficiency_strategy)
@settings(max_examples=50)
def test_etj::efficiency_instantiation(instance):
    assert isinstance(instance, eTJ::Efficiency)

@given(instance=eTJ::Efficiency_strategy)
def test_etj::efficiency_efficiency_type(instance):
    assert isinstance(instance.efficiency, float)


@given(instance=eTJ::Efficiency_strategy)
def test_etj::efficiency_efficiency_setter(instance):
    original = instance.efficiency
    instance.efficiency = original
    assert instance.efficiency == original

@given(instance=eTJ::DurationQuantity_strategy)
@settings(max_examples=50)
def test_etj::durationquantity_instantiation(instance):
    assert isinstance(instance, eTJ::DurationQuantity)

@given(instance=eTJ::DurationQuantity_strategy)
def test_etj::durationquantity_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=eTJ::DurationQuantity_strategy)
def test_etj::durationquantity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ::DurationQuantity_strategy)
def test_etj::durationquantity_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=eTJ::DurationQuantity_strategy)
def test_etj::durationquantity_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=eTJ::Duration_strategy)
@settings(max_examples=50)
def test_etj::duration_instantiation(instance):
    assert isinstance(instance, eTJ::Duration)

@given(instance=StatusTimesheetAttribute_strategy)
@settings(max_examples=50)
def test_statustimesheetattribute_instantiation(instance):
    assert isinstance(instance, StatusTimesheetAttribute)

@given(instance=eTJ::TaskDependency_strategy)
@settings(max_examples=50)
def test_etj::taskdependency_instantiation(instance):
    assert isinstance(instance, eTJ::TaskDependency)

@given(instance=eTJ::TaskDependency_strategy)
def test_etj::taskdependency_policy_type(instance):
    assert isinstance(instance.policy, str)


@given(instance=eTJ::TaskDependency_strategy)
def test_etj::taskdependency_policy_setter(instance):
    original = instance.policy
    instance.policy = original
    assert instance.policy == original

@given(instance=eTJ::Depends_strategy)
@settings(max_examples=50)
def test_etj::depends_instantiation(instance):
    assert isinstance(instance, eTJ::Depends)

@given(instance=eTJ::ExtendedResourceAttribute_strategy)
@settings(max_examples=50)
def test_etj::extendedresourceattribute_instantiation(instance):
    assert isinstance(instance, eTJ::ExtendedResourceAttribute)

@given(instance=eTJ::ExtendedResourceAttribute_strategy)
def test_etj::extendedresourceattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=eTJ::ExtendedResourceAttribute_strategy)
def test_etj::extendedresourceattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ::Extend_strategy)
@settings(max_examples=50)
def test_etj::extend_instantiation(instance):
    assert isinstance(instance, eTJ::Extend)

@given(instance=eTJ::Extend_strategy)
def test_etj::extend_inherit_type(instance):
    assert isinstance(instance.inherit, bool)


@given(instance=eTJ::Extend_strategy)
def test_etj::extend_inherit_setter(instance):
    original = instance.inherit
    instance.inherit = original
    assert instance.inherit == original

@given(instance=eTJ::Extend_strategy)
def test_etj::extend_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=eTJ::Extend_strategy)
def test_etj::extend_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=eTJ::Extend_strategy)
def test_etj::extend_scenariospecific_type(instance):
    assert isinstance(instance.scenariospecific, bool)


@given(instance=eTJ::Extend_strategy)
def test_etj::extend_scenariospecific_setter(instance):
    original = instance.scenariospecific
    instance.scenariospecific = original
    assert instance.scenariospecific == original

@given(instance=eTJ::Extend_strategy)
def test_etj::extend_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eTJ::Extend_strategy)
def test_etj::extend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ::Epilog_strategy)
@settings(max_examples=50)
def test_etj::epilog_instantiation(instance):
    assert isinstance(instance, eTJ::Epilog)

@given(instance=eTJ::EndCredit_strategy)
@settings(max_examples=50)
def test_etj::endcredit_instantiation(instance):
    assert isinstance(instance, eTJ::EndCredit)

@given(instance=eTJ::EndCredit_strategy)
def test_etj::endcredit_credit_type(instance):
    assert isinstance(instance.credit, float)


@given(instance=eTJ::EndCredit_strategy)
def test_etj::endcredit_credit_setter(instance):
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

@given(instance=eTJ::Remaining_strategy)
@settings(max_examples=50)
def test_etj::remaining_instantiation(instance):
    assert isinstance(instance, eTJ::Remaining)

@given(instance=eTJ::Work_strategy)
@settings(max_examples=50)
def test_etj::work_instantiation(instance):
    assert isinstance(instance, eTJ::Work)

@given(instance=eTJ::Work_strategy)
def test_etj::work_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=eTJ::Work_strategy)
def test_etj::work_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=eTJ::Work_strategy)
def test_etj::work_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=eTJ::Work_strategy)
def test_etj::work_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ::Priority_strategy)
@settings(max_examples=50)
def test_etj::priority_instantiation(instance):
    assert isinstance(instance, eTJ::Priority)

@given(instance=eTJ::Priority_strategy)
def test_etj::priority_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=eTJ::Priority_strategy)
def test_etj::priority_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=StatusSheetReportAttribute_strategy)
@settings(max_examples=50)
def test_statussheetreportattribute_instantiation(instance):
    assert isinstance(instance, StatusSheetReportAttribute)

@given(instance=eTJ::SortResources_strategy)
@settings(max_examples=50)
def test_etj::sortresources_instantiation(instance):
    assert isinstance(instance, eTJ::SortResources)

@given(instance=eTJ::SortTasks_strategy)
@settings(max_examples=50)
def test_etj::sorttasks_instantiation(instance):
    assert isinstance(instance, eTJ::SortTasks)

@given(instance=NikuReportAttribute_strategy)
@settings(max_examples=50)
def test_nikureportattribute_instantiation(instance):
    assert isinstance(instance, NikuReportAttribute)

@given(instance=eTJ::Timeoff_strategy)
@settings(max_examples=50)
def test_etj::timeoff_instantiation(instance):
    assert isinstance(instance, eTJ::Timeoff)

@given(instance=eTJ::Timeoff_strategy)
def test_etj::timeoff_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eTJ::Timeoff_strategy)
def test_etj::timeoff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ::Timeoff_strategy)
def test_etj::timeoff_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=eTJ::Timeoff_strategy)
def test_etj::timeoff_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ::Headline_strategy)
@settings(max_examples=50)
def test_etj::headline_instantiation(instance):
    assert isinstance(instance, eTJ::Headline)

@given(instance=eTJ::Formats_strategy)
@settings(max_examples=50)
def test_etj::formats_instantiation(instance):
    assert isinstance(instance, eTJ::Formats)

@given(instance=eTJ::Formats_strategy)
def test_etj::formats_formats_type(instance):
    assert isinstance(instance.formats, str)


@given(instance=eTJ::Formats_strategy)
def test_etj::formats_formats_setter(instance):
    original = instance.formats
    instance.formats = original
    assert instance.formats == original

@given(instance=eTJ::AccountShare_strategy)
@settings(max_examples=50)
def test_etj::accountshare_instantiation(instance):
    assert isinstance(instance, eTJ::AccountShare)

@given(instance=eTJ::AccountShare_strategy)
def test_etj::accountshare_share_type(instance):
    assert isinstance(instance.share, float)


@given(instance=eTJ::AccountShare_strategy)
def test_etj::accountshare_share_setter(instance):
    original = instance.share
    instance.share = original
    assert instance.share == original

@given(instance=eTJ::ChargeSet_strategy)
@settings(max_examples=50)
def test_etj::chargeset_instantiation(instance):
    assert isinstance(instance, eTJ::ChargeSet)

@given(instance=eTJ::Charge_strategy)
@settings(max_examples=50)
def test_etj::charge_instantiation(instance):
    assert isinstance(instance, eTJ::Charge)

@given(instance=eTJ::Charge_strategy)
def test_etj::charge_applies_type(instance):
    assert isinstance(instance.applies, str)


@given(instance=eTJ::Charge_strategy)
def test_etj::charge_applies_setter(instance):
    original = instance.applies
    instance.applies = original
    assert instance.applies == original

@given(instance=eTJ::Charge_strategy)
def test_etj::charge_amount_type(instance):
    assert isinstance(instance.amount, float)


@given(instance=eTJ::Charge_strategy)
def test_etj::charge_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=eTJ::Center_strategy)
@settings(max_examples=50)
def test_etj::center_instantiation(instance):
    assert isinstance(instance, eTJ::Center)

@given(instance=eTJ::RGB_strategy)
@settings(max_examples=50)
def test_etj::rgb_instantiation(instance):
    assert isinstance(instance, eTJ::RGB)

@given(instance=eTJ::RGB_strategy)
def test_etj::rgb_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=eTJ::RGB_strategy)
def test_etj::rgb_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eTJ::LogicalExpression_strategy)
@settings(max_examples=50)
def test_etj::logicalexpression_instantiation(instance):
    assert isinstance(instance, eTJ::LogicalExpression)

@given(instance=eTJ::LogicalExpression_strategy)
def test_etj::logicalexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=eTJ::LogicalExpression_strategy)
def test_etj::logicalexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ColumnAttribute_strategy)
@settings(max_examples=50)
def test_columnattribute_instantiation(instance):
    assert isinstance(instance, ColumnAttribute)

@given(instance=eTJ::ExtendedResourceAttributeColumn_strategy)
@settings(max_examples=50)
def test_etj::extendedresourceattributecolumn_instantiation(instance):
    assert isinstance(instance, eTJ::ExtendedResourceAttributeColumn)

@given(instance=eTJ::ListType_strategy)
@settings(max_examples=50)
def test_etj::listtype_instantiation(instance):
    assert isinstance(instance, eTJ::ListType)

@given(instance=eTJ::ListType_strategy)
def test_etj::listtype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=eTJ::ListType_strategy)
def test_etj::listtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=eTJ::HAlign_strategy)
@settings(max_examples=50)
def test_etj::halign_instantiation(instance):
    assert isinstance(instance, eTJ::HAlign)

@given(instance=eTJ::HAlign_strategy)
def test_etj::halign_justification_type(instance):
    assert isinstance(instance.justification, str)


@given(instance=eTJ::HAlign_strategy)
def test_etj::halign_justification_setter(instance):
    original = instance.justification
    instance.justification = original
    assert instance.justification == original

@given(instance=eTJ::FontColor_strategy)
@settings(max_examples=50)
def test_etj::fontcolor_instantiation(instance):
    assert isinstance(instance, eTJ::FontColor)

@given(instance=eTJ::FontColor_strategy)
def test_etj::fontcolor_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=eTJ::FontColor_strategy)
def test_etj::fontcolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=eTJ::CellText_strategy)
@settings(max_examples=50)
def test_etj::celltext_instantiation(instance):
    assert isinstance(instance, eTJ::CellText)

@given(instance=eTJ::CellText_strategy)
def test_etj::celltext_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=eTJ::CellText_strategy)
def test_etj::celltext_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=eTJ::ToolTip_strategy)
@settings(max_examples=50)
def test_etj::tooltip_instantiation(instance):
    assert isinstance(instance, eTJ::ToolTip)

@given(instance=eTJ::ToolTip_strategy)
def test_etj::tooltip_tip_type(instance):
    assert isinstance(instance.tip, str)


@given(instance=eTJ::ToolTip_strategy)
def test_etj::tooltip_tip_setter(instance):
    original = instance.tip
    instance.tip = original
    assert instance.tip == original

@given(instance=eTJ::Title_strategy)
@settings(max_examples=50)
def test_etj::title_instantiation(instance):
    assert isinstance(instance, eTJ::Title)

@given(instance=eTJ::Title_strategy)
def test_etj::title_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=eTJ::Title_strategy)
def test_etj::title_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=eTJ::ListItem_strategy)
@settings(max_examples=50)
def test_etj::listitem_instantiation(instance):
    assert isinstance(instance, eTJ::ListItem)

@given(instance=eTJ::Width_strategy)
@settings(max_examples=50)
def test_etj::width_instantiation(instance):
    assert isinstance(instance, eTJ::Width)

@given(instance=eTJ::Width_strategy)
def test_etj::width_width_type(instance):
    assert isinstance(instance.width, float)


@given(instance=eTJ::Width_strategy)
def test_etj::width_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=eTJ::Scale_strategy)
@settings(max_examples=50)
def test_etj::scale_instantiation(instance):
    assert isinstance(instance, eTJ::Scale)

@given(instance=eTJ::Scale_strategy)
def test_etj::scale_scale_type(instance):
    assert isinstance(instance.scale, str)


@given(instance=eTJ::Scale_strategy)
def test_etj::scale_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=eTJ::CellColor_strategy)
@settings(max_examples=50)
def test_etj::cellcolor_instantiation(instance):
    assert isinstance(instance, eTJ::CellColor)

@given(instance=eTJ::Caption_strategy)
@settings(max_examples=50)
def test_etj::caption_instantiation(instance):
    assert isinstance(instance, eTJ::Caption)

@given(instance=ExportAttribute_strategy)
@settings(max_examples=50)
def test_exportattribute_instantiation(instance):
    assert isinstance(instance, ExportAttribute)

@given(instance=eTJ::RollupTask_strategy)
@settings(max_examples=50)
def test_etj::rolluptask_instantiation(instance):
    assert isinstance(instance, eTJ::RollupTask)

@given(instance=eTJ::TaskAttributes_strategy)
@settings(max_examples=50)
def test_etj::taskattributes_instantiation(instance):
    assert isinstance(instance, eTJ::TaskAttributes)

@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_minend_type(instance):
    assert isinstance(instance.minend, bool)


@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_minend_setter(instance):
    original = instance.minend
    instance.minend = original
    assert instance.minend == original

@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_responsible_type(instance):
    assert isinstance(instance.responsible, bool)


@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_responsible_setter(instance):
    original = instance.responsible
    instance.responsible = original
    assert instance.responsible == original

@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_note_type(instance):
    assert isinstance(instance.note, bool)


@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_maxend_type(instance):
    assert isinstance(instance.maxend, bool)


@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_maxend_setter(instance):
    original = instance.maxend
    instance.maxend = original
    assert instance.maxend == original

@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_priority_type(instance):
    assert isinstance(instance.priority, bool)


@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_minstart_type(instance):
    assert isinstance(instance.minstart, bool)


@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_minstart_setter(instance):
    original = instance.minstart
    instance.minstart = original
    assert instance.minstart == original

@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_complete_type(instance):
    assert isinstance(instance.complete, bool)


@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_complete_setter(instance):
    original = instance.complete
    instance.complete = original
    assert instance.complete == original

@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_depends_type(instance):
    assert isinstance(instance.depends, bool)


@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_depends_setter(instance):
    original = instance.depends
    instance.depends = original
    assert instance.depends == original

@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_flags_type(instance):
    assert isinstance(instance.flags, bool)


@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original

@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_maxstart_type(instance):
    assert isinstance(instance.maxstart, bool)


@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_maxstart_setter(instance):
    original = instance.maxstart
    instance.maxstart = original
    assert instance.maxstart == original

@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_booking_type(instance):
    assert isinstance(instance.booking, bool)


@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_booking_setter(instance):
    original = instance.booking
    instance.booking = original
    assert instance.booking == original

@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_none_type(instance):
    assert isinstance(instance.none, bool)


@given(instance=eTJ::TaskAttributes_strategy)
def test_etj::taskattributes_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=eTJ::Period_strategy)
@settings(max_examples=50)
def test_etj::period_instantiation(instance):
    assert isinstance(instance, eTJ::Period)

@given(instance=eTJ::Start_strategy)
@settings(max_examples=50)
def test_etj::start_instantiation(instance):
    assert isinstance(instance, eTJ::Start)

@given(instance=eTJ::Scenarios_strategy)
@settings(max_examples=50)
def test_etj::scenarios_instantiation(instance):
    assert isinstance(instance, eTJ::Scenarios)

@given(instance=eTJ::RollupResource_strategy)
@settings(max_examples=50)
def test_etj::rollupresource_instantiation(instance):
    assert isinstance(instance, eTJ::RollupResource)

@given(instance=eTJ::ResourceAttributes_strategy)
@settings(max_examples=50)
def test_etj::resourceattributes_instantiation(instance):
    assert isinstance(instance, eTJ::ResourceAttributes)

@given(instance=eTJ::ResourceAttributes_strategy)
def test_etj::resourceattributes_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=eTJ::ResourceAttributes_strategy)
def test_etj::resourceattributes_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=eTJ::ResourceAttributes_strategy)
def test_etj::resourceattributes_workingHours_type(instance):
    assert isinstance(instance.workingHours, bool)


@given(instance=eTJ::ResourceAttributes_strategy)
def test_etj::resourceattributes_workingHours_setter(instance):
    original = instance.workingHours
    instance.workingHours = original
    assert instance.workingHours == original

@given(instance=eTJ::ResourceAttributes_strategy)
def test_etj::resourceattributes_booking_type(instance):
    assert isinstance(instance.booking, bool)


@given(instance=eTJ::ResourceAttributes_strategy)
def test_etj::resourceattributes_booking_setter(instance):
    original = instance.booking
    instance.booking = original
    assert instance.booking == original

@given(instance=eTJ::ResourceAttributes_strategy)
def test_etj::resourceattributes_none_type(instance):
    assert isinstance(instance.none, bool)


@given(instance=eTJ::ResourceAttributes_strategy)
def test_etj::resourceattributes_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=eTJ::ResourceAttributes_strategy)
def test_etj::resourceattributes_vacation_type(instance):
    assert isinstance(instance.vacation, bool)


@given(instance=eTJ::ResourceAttributes_strategy)
def test_etj::resourceattributes_vacation_setter(instance):
    original = instance.vacation
    instance.vacation = original
    assert instance.vacation == original

@given(instance=eTJ::HideTask_strategy)
@settings(max_examples=50)
def test_etj::hidetask_instantiation(instance):
    assert isinstance(instance, eTJ::HideTask)

@given(instance=eTJ::HideResource_strategy)
@settings(max_examples=50)
def test_etj::hideresource_instantiation(instance):
    assert isinstance(instance, eTJ::HideResource)

@given(instance=eTJ::End_strategy)
@settings(max_examples=50)
def test_etj::end_instantiation(instance):
    assert isinstance(instance, eTJ::End)

@given(instance=eTJ::Definitions_strategy)
@settings(max_examples=50)
def test_etj::definitions_instantiation(instance):
    assert isinstance(instance, eTJ::Definitions)

@given(instance=eTJ::Definitions_strategy)
def test_etj::definitions_none_type(instance):
    assert isinstance(instance.none, bool)


@given(instance=eTJ::Definitions_strategy)
def test_etj::definitions_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=eTJ::Definitions_strategy)
def test_etj::definitions_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=eTJ::Definitions_strategy)
def test_etj::definitions_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=LimitsAttribute_strategy)
@settings(max_examples=50)
def test_limitsattribute_instantiation(instance):
    assert isinstance(instance, LimitsAttribute)

@given(instance=eTJ::MonthlyMin_strategy)
@settings(max_examples=50)
def test_etj::monthlymin_instantiation(instance):
    assert isinstance(instance, eTJ::MonthlyMin)

@given(instance=eTJ::DailyMin_strategy)
@settings(max_examples=50)
def test_etj::dailymin_instantiation(instance):
    assert isinstance(instance, eTJ::DailyMin)

@given(instance=eTJ::MonthlyMax_strategy)
@settings(max_examples=50)
def test_etj::monthlymax_instantiation(instance):
    assert isinstance(instance, eTJ::MonthlyMax)

@given(instance=eTJ::Maximum_strategy)
@settings(max_examples=50)
def test_etj::maximum_instantiation(instance):
    assert isinstance(instance, eTJ::Maximum)

@given(instance=eTJ::WeeklyMax_strategy)
@settings(max_examples=50)
def test_etj::weeklymax_instantiation(instance):
    assert isinstance(instance, eTJ::WeeklyMax)

@given(instance=eTJ::Minimum_strategy)
@settings(max_examples=50)
def test_etj::minimum_instantiation(instance):
    assert isinstance(instance, eTJ::Minimum)

@given(instance=eTJ::WeeklyMin_strategy)
@settings(max_examples=50)
def test_etj::weeklymin_instantiation(instance):
    assert isinstance(instance, eTJ::WeeklyMin)

@given(instance=eTJ::DailyMax_strategy)
@settings(max_examples=50)
def test_etj::dailymax_instantiation(instance):
    assert isinstance(instance, eTJ::DailyMax)

@given(instance=ProjectAttribute_strategy)
@settings(max_examples=50)
def test_projectattribute_instantiation(instance):
    assert isinstance(instance, ProjectAttribute)

@given(instance=eTJ::ShortTimeFormat_strategy)
@settings(max_examples=50)
def test_etj::shorttimeformat_instantiation(instance):
    assert isinstance(instance, eTJ::ShortTimeFormat)

@given(instance=eTJ::ShortTimeFormat_strategy)
def test_etj::shorttimeformat_shortTimeFormat_type(instance):
    assert isinstance(instance.shortTimeFormat, str)


@given(instance=eTJ::ShortTimeFormat_strategy)
def test_etj::shorttimeformat_shortTimeFormat_setter(instance):
    original = instance.shortTimeFormat
    instance.shortTimeFormat = original
    assert instance.shortTimeFormat == original

@given(instance=eTJ::WorkingHours_strategy)
@settings(max_examples=50)
def test_etj::workinghours_instantiation(instance):
    assert isinstance(instance, eTJ::WorkingHours)

@given(instance=eTJ::WorkingHours_strategy)
def test_etj::workinghours_off_type(instance):
    assert isinstance(instance.off, bool)


@given(instance=eTJ::WorkingHours_strategy)
def test_etj::workinghours_off_setter(instance):
    original = instance.off
    instance.off = original
    assert instance.off == original

@given(instance=eTJ::Include_strategy)
@settings(max_examples=50)
def test_etj::include_instantiation(instance):
    assert isinstance(instance, eTJ::Include)

@given(instance=eTJ::Include_strategy)
def test_etj::include_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=eTJ::Include_strategy)
def test_etj::include_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=eTJ::TimingResolution_strategy)
@settings(max_examples=50)
def test_etj::timingresolution_instantiation(instance):
    assert isinstance(instance, eTJ::TimingResolution)

@given(instance=eTJ::TimingResolution_strategy)
def test_etj::timingresolution_timingResolution_type(instance):
    assert isinstance(instance.timingResolution, int)


@given(instance=eTJ::TimingResolution_strategy)
def test_etj::timingresolution_timingResolution_setter(instance):
    original = instance.timingResolution
    instance.timingResolution = original
    assert instance.timingResolution == original

@given(instance=eTJ::TrackingScenario_strategy)
@settings(max_examples=50)
def test_etj::trackingscenario_instantiation(instance):
    assert isinstance(instance, eTJ::TrackingScenario)

@given(instance=eTJ::WeekStarts_strategy)
@settings(max_examples=50)
def test_etj::weekstarts_instantiation(instance):
    assert isinstance(instance, eTJ::WeekStarts)

@given(instance=eTJ::WeekStarts_strategy)
def test_etj::weekstarts_sunday_type(instance):
    assert isinstance(instance.sunday, bool)


@given(instance=eTJ::WeekStarts_strategy)
def test_etj::weekstarts_sunday_setter(instance):
    original = instance.sunday
    instance.sunday = original
    assert instance.sunday == original

@given(instance=eTJ::WeekStarts_strategy)
def test_etj::weekstarts_monday_type(instance):
    assert isinstance(instance.monday, bool)


@given(instance=eTJ::WeekStarts_strategy)
def test_etj::weekstarts_monday_setter(instance):
    original = instance.monday
    instance.monday = original
    assert instance.monday == original

@given(instance=eTJ::ExtendResource_strategy)
@settings(max_examples=50)
def test_etj::extendresource_instantiation(instance):
    assert isinstance(instance, eTJ::ExtendResource)

@given(instance=eTJ::TimeFormat_strategy)
@settings(max_examples=50)
def test_etj::timeformat_instantiation(instance):
    assert isinstance(instance, eTJ::TimeFormat)

@given(instance=eTJ::TimeFormat_strategy)
def test_etj::timeformat_timeformat_type(instance):
    assert isinstance(instance.timeformat, str)


@given(instance=eTJ::TimeFormat_strategy)
def test_etj::timeformat_timeformat_setter(instance):
    original = instance.timeformat
    instance.timeformat = original
    assert instance.timeformat == original

@given(instance=eTJ::DailyWorkingHours_strategy)
@settings(max_examples=50)
def test_etj::dailyworkinghours_instantiation(instance):
    assert isinstance(instance, eTJ::DailyWorkingHours)

@given(instance=eTJ::DailyWorkingHours_strategy)
def test_etj::dailyworkinghours_dailyWorkingHours_type(instance):
    assert isinstance(instance.dailyWorkingHours, float)


@given(instance=eTJ::DailyWorkingHours_strategy)
def test_etj::dailyworkinghours_dailyWorkingHours_setter(instance):
    original = instance.dailyWorkingHours
    instance.dailyWorkingHours = original
    assert instance.dailyWorkingHours == original

@given(instance=eTJ::Now_strategy)
@settings(max_examples=50)
def test_etj::now_instantiation(instance):
    assert isinstance(instance, eTJ::Now)

@given(instance=eTJ::JournalEntry_strategy)
@settings(max_examples=50)
def test_etj::journalentry_instantiation(instance):
    assert isinstance(instance, eTJ::JournalEntry)

@given(instance=eTJ::JournalEntry_strategy)
def test_etj::journalentry_headline_type(instance):
    assert isinstance(instance.headline, str)


@given(instance=eTJ::JournalEntry_strategy)
def test_etj::journalentry_headline_setter(instance):
    original = instance.headline
    instance.headline = original
    assert instance.headline == original

@given(instance=eTJ::ExtendTask_strategy)
@settings(max_examples=50)
def test_etj::extendtask_instantiation(instance):
    assert isinstance(instance, eTJ::ExtendTask)

@given(instance=eTJ::NumberFormat_strategy)
@settings(max_examples=50)
def test_etj::numberformat_instantiation(instance):
    assert isinstance(instance, eTJ::NumberFormat)

@given(instance=eTJ::Timezone_strategy)
@settings(max_examples=50)
def test_etj::timezone_instantiation(instance):
    assert isinstance(instance, eTJ::Timezone)

@given(instance=eTJ::Timezone_strategy)
def test_etj::timezone_timezone_type(instance):
    assert isinstance(instance.timezone, str)


@given(instance=eTJ::Timezone_strategy)
def test_etj::timezone_timezone_setter(instance):
    original = instance.timezone
    instance.timezone = original
    assert instance.timezone == original

@given(instance=eTJ::YearlyWorkingDays_strategy)
@settings(max_examples=50)
def test_etj::yearlyworkingdays_instantiation(instance):
    assert isinstance(instance, eTJ::YearlyWorkingDays)

@given(instance=eTJ::YearlyWorkingDays_strategy)
def test_etj::yearlyworkingdays_yearlyWorkingDays_type(instance):
    assert isinstance(instance.yearlyWorkingDays, int)


@given(instance=eTJ::YearlyWorkingDays_strategy)
def test_etj::yearlyworkingdays_yearlyWorkingDays_setter(instance):
    original = instance.yearlyWorkingDays
    instance.yearlyWorkingDays = original
    assert instance.yearlyWorkingDays == original

@given(instance=eTJ::CurrencyFormat_strategy)
@settings(max_examples=50)
def test_etj::currencyformat_instantiation(instance):
    assert isinstance(instance, eTJ::CurrencyFormat)

@given(instance=eTJ::Currency_strategy)
@settings(max_examples=50)
def test_etj::currency_instantiation(instance):
    assert isinstance(instance, eTJ::Currency)

@given(instance=eTJ::Currency_strategy)
def test_etj::currency_currency_type(instance):
    assert isinstance(instance.currency, str)


@given(instance=eTJ::Currency_strategy)
def test_etj::currency_currency_setter(instance):
    original = instance.currency
    instance.currency = original
    assert instance.currency == original

@given(instance=eTJ::ISODATE_strategy)
@settings(max_examples=50)
def test_etj::isodate_instantiation(instance):
    assert isinstance(instance, eTJ::ISODATE)

@given(instance=eTJ::Credit_strategy)
@settings(max_examples=50)
def test_etj::credit_instantiation(instance):
    assert isinstance(instance, eTJ::Credit)

@given(instance=eTJ::Credit_strategy)
def test_etj::credit_amount_type(instance):
    assert isinstance(instance.amount, float)


@given(instance=eTJ::Credit_strategy)
def test_etj::credit_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=eTJ::Credit_strategy)
def test_etj::credit_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=eTJ::Credit_strategy)
def test_etj::credit_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=eTJ::Copyright_strategy)
@settings(max_examples=50)
def test_etj::copyright_instantiation(instance):
    assert isinstance(instance, eTJ::Copyright)

@given(instance=eTJ::Copyright_strategy)
def test_etj::copyright_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=eTJ::Copyright_strategy)
def test_etj::copyright_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=eTJ::Complete_strategy)
@settings(max_examples=50)
def test_etj::complete_instantiation(instance):
    assert isinstance(instance, eTJ::Complete)

@given(instance=eTJ::Complete_strategy)
def test_etj::complete_complete_type(instance):
    assert isinstance(instance.complete, float)


@given(instance=eTJ::Complete_strategy)
def test_etj::complete_complete_setter(instance):
    original = instance.complete
    instance.complete = original
    assert instance.complete == original

@given(instance=eTJ::Column_strategy)
@settings(max_examples=50)
def test_etj::column_instantiation(instance):
    assert isinstance(instance, eTJ::Column)

@given(instance=eTJ::Column_strategy)
def test_etj::column_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=eTJ::Column_strategy)
def test_etj::column_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ::Columns_strategy)
@settings(max_examples=50)
def test_etj::columns_instantiation(instance):
    assert isinstance(instance, eTJ::Columns)

@given(instance=eTJ::Interval4_strategy)
@settings(max_examples=50)
def test_etj::interval4_instantiation(instance):
    assert isinstance(instance, eTJ::Interval4)

@given(instance=eTJ::Booking_strategy)
@settings(max_examples=50)
def test_etj::booking_instantiation(instance):
    assert isinstance(instance, eTJ::Booking)

@given(instance=eTJ::Booking_strategy)
def test_etj::booking_overtime_type(instance):
    assert isinstance(instance.overtime, int)


@given(instance=eTJ::Booking_strategy)
def test_etj::booking_overtime_setter(instance):
    original = instance.overtime
    instance.overtime = original
    assert instance.overtime == original

@given(instance=eTJ::Booking_strategy)
def test_etj::booking_sloppy_type(instance):
    assert isinstance(instance.sloppy, int)


@given(instance=eTJ::Booking_strategy)
def test_etj::booking_sloppy_setter(instance):
    original = instance.sloppy
    instance.sloppy = original
    assert instance.sloppy == original

@given(instance=eTJ::BookingResource_strategy)
@settings(max_examples=50)
def test_etj::bookingresource_instantiation(instance):
    assert isinstance(instance, eTJ::BookingResource)

@given(instance=eTJ::BookingTask_strategy)
@settings(max_examples=50)
def test_etj::bookingtask_instantiation(instance):
    assert isinstance(instance, eTJ::BookingTask)

@given(instance=eTJ::NavigatorAttribute_strategy)
@settings(max_examples=50)
def test_etj::navigatorattribute_instantiation(instance):
    assert isinstance(instance, eTJ::NavigatorAttribute)

@given(instance=eTJ::Navigator_strategy)
@settings(max_examples=50)
def test_etj::navigator_instantiation(instance):
    assert isinstance(instance, eTJ::Navigator)

@given(instance=eTJ::Navigator_strategy)
def test_etj::navigator_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=eTJ::Navigator_strategy)
def test_etj::navigator_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ::AllocateResourceAttribute_strategy)
@settings(max_examples=50)
def test_etj::allocateresourceattribute_instantiation(instance):
    assert isinstance(instance, eTJ::AllocateResourceAttribute)

@given(instance=eTJ::AllocateResource_strategy)
@settings(max_examples=50)
def test_etj::allocateresource_instantiation(instance):
    assert isinstance(instance, eTJ::AllocateResource)

@given(instance=eTJ::Allocate_strategy)
@settings(max_examples=50)
def test_etj::allocate_instantiation(instance):
    assert isinstance(instance, eTJ::Allocate)

@given(instance=eTJ::ResourceAttribute_strategy)
@settings(max_examples=50)
def test_etj::resourceattribute_instantiation(instance):
    assert isinstance(instance, eTJ::ResourceAttribute)

@given(instance=eTJ::Resource_strategy)
@settings(max_examples=50)
def test_etj::resource_instantiation(instance):
    assert isinstance(instance, eTJ::Resource)

@given(instance=eTJ::Resource_strategy)
def test_etj::resource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eTJ::Resource_strategy)
def test_etj::resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ::Resource_strategy)
def test_etj::resource_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=eTJ::Resource_strategy)
def test_etj::resource_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ::Balance_strategy)
@settings(max_examples=50)
def test_etj::balance_instantiation(instance):
    assert isinstance(instance, eTJ::Balance)

@given(instance=StatusStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_statusstatussheetattribute_instantiation(instance):
    assert isinstance(instance, StatusStatusSheetAttribute)

@given(instance=eTJ::Flags_strategy)
@settings(max_examples=50)
def test_etj::flags_instantiation(instance):
    assert isinstance(instance, eTJ::Flags)

@given(instance=eTJ::Flags_strategy)
def test_etj::flags_flags_type(instance):
    assert isinstance(instance.flags, str)


@given(instance=eTJ::Flags_strategy)
def test_etj::flags_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original

@given(instance=eTJ::Summary_strategy)
@settings(max_examples=50)
def test_etj::summary_instantiation(instance):
    assert isinstance(instance, eTJ::Summary)

@given(instance=eTJ::Details_strategy)
@settings(max_examples=50)
def test_etj::details_instantiation(instance):
    assert isinstance(instance, eTJ::Details)

@given(instance=eTJ::Author_strategy)
@settings(max_examples=50)
def test_etj::author_instantiation(instance):
    assert isinstance(instance, eTJ::Author)

@given(instance=AllocateResourceAttribute_strategy)
@settings(max_examples=50)
def test_allocateresourceattribute_instantiation(instance):
    assert isinstance(instance, AllocateResourceAttribute)

@given(instance=eTJ::ShiftsAllocate_strategy)
@settings(max_examples=50)
def test_etj::shiftsallocate_instantiation(instance):
    assert isinstance(instance, eTJ::ShiftsAllocate)

@given(instance=eTJ::Persistent_strategy)
@settings(max_examples=50)
def test_etj::persistent_instantiation(instance):
    assert isinstance(instance, eTJ::Persistent)

@given(instance=eTJ::Persistent_strategy)
def test_etj::persistent_persistent_type(instance):
    assert isinstance(instance.persistent, bool)


@given(instance=eTJ::Persistent_strategy)
def test_etj::persistent_persistent_setter(instance):
    original = instance.persistent
    instance.persistent = original
    assert instance.persistent == original

@given(instance=eTJ::Select_strategy)
@settings(max_examples=50)
def test_etj::select_instantiation(instance):
    assert isinstance(instance, eTJ::Select)

@given(instance=eTJ::Select_strategy)
def test_etj::select_argument_type(instance):
    assert isinstance(instance.argument, str)


@given(instance=eTJ::Select_strategy)
def test_etj::select_argument_setter(instance):
    original = instance.argument
    instance.argument = original
    assert instance.argument == original

@given(instance=eTJ::Mandatory_strategy)
@settings(max_examples=50)
def test_etj::mandatory_instantiation(instance):
    assert isinstance(instance, eTJ::Mandatory)

@given(instance=eTJ::Mandatory_strategy)
def test_etj::mandatory_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=eTJ::Mandatory_strategy)
def test_etj::mandatory_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=eTJ::Alternative_strategy)
@settings(max_examples=50)
def test_etj::alternative_instantiation(instance):
    assert isinstance(instance, eTJ::Alternative)

@given(instance=eTJ::Alert_strategy)
@settings(max_examples=50)
def test_etj::alert_instantiation(instance):
    assert isinstance(instance, eTJ::Alert)

@given(instance=eTJ::Alert_strategy)
def test_etj::alert_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=eTJ::Alert_strategy)
def test_etj::alert_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=eTJ::NikuReportAttribute_strategy)
@settings(max_examples=50)
def test_etj::nikureportattribute_instantiation(instance):
    assert isinstance(instance, eTJ::NikuReportAttribute)

@given(instance=eTJ::NikuReport_strategy)
@settings(max_examples=50)
def test_etj::nikureport_instantiation(instance):
    assert isinstance(instance, eTJ::NikuReport)

@given(instance=eTJ::NikuReport_strategy)
def test_etj::nikureport_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=eTJ::NikuReport_strategy)
def test_etj::nikureport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=eTJ::NewTaskAttribute_strategy)
@settings(max_examples=50)
def test_etj::newtaskattribute_instantiation(instance):
    assert isinstance(instance, eTJ::NewTaskAttribute)

@given(instance=TimesheetAttribute_strategy)
@settings(max_examples=50)
def test_timesheetattribute_instantiation(instance):
    assert isinstance(instance, TimesheetAttribute)

@given(instance=eTJ::ShiftTimesheet_strategy)
@settings(max_examples=50)
def test_etj::shifttimesheet_instantiation(instance):
    assert isinstance(instance, eTJ::ShiftTimesheet)

@given(instance=eTJ::TaskTimesheet_strategy)
@settings(max_examples=50)
def test_etj::tasktimesheet_instantiation(instance):
    assert isinstance(instance, eTJ::TaskTimesheet)

@given(instance=eTJ::StatusTimesheet_strategy)
@settings(max_examples=50)
def test_etj::statustimesheet_instantiation(instance):
    assert isinstance(instance, eTJ::StatusTimesheet)

@given(instance=eTJ::StatusTimesheet_strategy)
def test_etj::statustimesheet_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=eTJ::StatusTimesheet_strategy)
def test_etj::statustimesheet_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=eTJ::StatusTimesheet_strategy)
def test_etj::statustimesheet_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=eTJ::StatusTimesheet_strategy)
def test_etj::statustimesheet_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=eTJ::NewTask_strategy)
@settings(max_examples=50)
def test_etj::newtask_instantiation(instance):
    assert isinstance(instance, eTJ::NewTask)

@given(instance=eTJ::NewTask_strategy)
def test_etj::newtask_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=eTJ::NewTask_strategy)
def test_etj::newtask_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=eTJ::NewTask_strategy)
def test_etj::newtask_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=eTJ::NewTask_strategy)
def test_etj::newtask_id_setter(instance):
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

@given(instance=eTJ::MacroCall_strategy)
@settings(max_examples=50)
def test_etj::macrocall_instantiation(instance):
    assert isinstance(instance, eTJ::MacroCall)

@given(instance=eTJ::MacroCall_strategy)
def test_etj::macrocall_buildin_type(instance):
    assert isinstance(instance.buildin, str)


@given(instance=eTJ::MacroCall_strategy)
def test_etj::macrocall_buildin_setter(instance):
    original = instance.buildin
    instance.buildin = original
    assert instance.buildin == original

@given(instance=eTJ::EObject_strategy)
@settings(max_examples=50)
def test_etj::eobject_instantiation(instance):
    assert isinstance(instance, eTJ::EObject)

@given(instance=eTJ::Scenario_strategy)
@settings(max_examples=50)
def test_etj::scenario_instantiation(instance):
    assert isinstance(instance, eTJ::Scenario)

@given(instance=eTJ::Scenario_strategy)
def test_etj::scenario_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eTJ::Scenario_strategy)
def test_etj::scenario_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ::Scenario_strategy)
def test_etj::scenario_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=eTJ::Scenario_strategy)
def test_etj::scenario_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ::Scenario_strategy)
def test_etj::scenario_active_type(instance):
    assert isinstance(instance.active, str)


@given(instance=eTJ::Scenario_strategy)
def test_etj::scenario_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=eTJ::TaskAttribute_strategy)
@settings(max_examples=50)
def test_etj::taskattribute_instantiation(instance):
    assert isinstance(instance, eTJ::TaskAttribute)

@given(instance=eTJ::Task_strategy)
@settings(max_examples=50)
def test_etj::task_instantiation(instance):
    assert isinstance(instance, eTJ::Task)

@given(instance=eTJ::Task_strategy)
def test_etj::task_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eTJ::Task_strategy)
def test_etj::task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ::Task_strategy)
def test_etj::task_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=eTJ::Task_strategy)
def test_etj::task_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ::ProjectAttribute_strategy)
@settings(max_examples=50)
def test_etj::projectattribute_instantiation(instance):
    assert isinstance(instance, eTJ::ProjectAttribute)

@given(instance=eTJ::ExportAttribute_strategy)
@settings(max_examples=50)
def test_etj::exportattribute_instantiation(instance):
    assert isinstance(instance, eTJ::ExportAttribute)

@given(instance=eTJ::Export_strategy)
@settings(max_examples=50)
def test_etj::export_instantiation(instance):
    assert isinstance(instance, eTJ::Export)

@given(instance=eTJ::Export_strategy)
def test_etj::export_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=eTJ::Export_strategy)
def test_etj::export_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=eTJ::Export_strategy)
def test_etj::export_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=eTJ::Export_strategy)
def test_etj::export_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eTJ::IcalReportAttribute_strategy)
@settings(max_examples=50)
def test_etj::icalreportattribute_instantiation(instance):
    assert isinstance(instance, eTJ::IcalReportAttribute)

@given(instance=eTJ::IcalReport_strategy)
@settings(max_examples=50)
def test_etj::icalreport_instantiation(instance):
    assert isinstance(instance, eTJ::IcalReport)

@given(instance=eTJ::IcalReport_strategy)
def test_etj::icalreport_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=eTJ::IcalReport_strategy)
def test_etj::icalreport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=eTJ::ReportAttribute_strategy)
@settings(max_examples=50)
def test_etj::reportattribute_instantiation(instance):
    assert isinstance(instance, eTJ::ReportAttribute)

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

@given(instance=eTJ::Report_strategy)
@settings(max_examples=50)
def test_etj::report_instantiation(instance):
    assert isinstance(instance, eTJ::Report)

@given(instance=eTJ::Report_strategy)
def test_etj::report_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eTJ::Report_strategy)
def test_etj::report_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eTJ::Report_strategy)
def test_etj::report_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=eTJ::Report_strategy)
def test_etj::report_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
