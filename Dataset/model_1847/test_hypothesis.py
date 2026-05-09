import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    project::JvmIdentifiableElement,
    LogicalExpression,
    project::LogicalNumeralLiteral,
    project::LogicalFunctionExpression,
    project::LogicalAbsoluteIdExression,
    project::LogicalDateLiteral,
    project::LogicalBooleanLiteral,
    project::LogicalStringLiteral,
    project::XBinaryOperation,
    Definitions,
    project::Defintions,
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
    project::RichText,
    Precedes,
    Depends,
    project::TaskDependency,
    NumberFormat,
    CurrencyFormat,
    project::RealFormat,
    WeeklyMax,
    MonthlyMin,
    MonthlyMax,
    Minimum,
    Maximum,
    DailyMin,
    DailyMax,
    GapLength,
    GapDuration,
    project::LimitAttribute,
    WeeklyMin,
    project::Limit,
    project::ColumnAttribute,
    project::WorkHours,
    project::Weekdays,
    project::TreeLevel,
    project::TimesheetReportAttribute,
    project::TimesheetAttribute,
    StatusSheetAttribute,
    project::TaskTimesheetAttribute,
    project::TaskStatusSheetAttribute,
    project::StatusSheetReportAttribute,
    project::StatusSheetAttribute,
    project::StatusTimesheetAttribute,
    project::Criterion,
    SortTasks,
    SortResources,
    SortJournalEntries,
    SortAccounts,
    project::Sort,
    project::StatusStatusSheetAttribute,
    TaskStatusSheetAttribute,
    project::TaskStatusSheet,
    project::StatusStatusSheet,
    project::ShiftsLimit,
    ShiftsTask,
    ShiftsResource,
    project::Shifts,
    project::LimitsAttribute,
    project::Interval3,
    project::Interval1,
    project::IncludePropertiesAttribute,
    project::Function,
    NavigatorAttribute,
    project::HideReport,
    project::GapLength,
    project::GapDuration,
    project::Extend,
    ExportAttribute,
    project::TaskAttributes,
    project::ResourceAttributes,
    project::Definitions,
    LimitsAttribute,
    project::WeeklyMin,
    project::Maximum,
    project::MonthlyMax,
    project::WeeklyMax,
    project::Minimum,
    project::DailyMin,
    project::MonthlyMin,
    project::DailyMax,
    ProjectAttribute,
    project::TimingResolution,
    project::ExtendResource,
    project::ExtendTask,
    project::DailyWorkingHours,
    project::ShortTimeFormat,
    project::WeekStarts,
    project::Scenario,
    project::Include,
    project::TrackingScenario,
    project::Now,
    project::YearlyWorkingDays,
    project::Currency,
    TimesheetReportAttribute,
    TaskTimesheetAttribute,
    StatusSheetReportAttribute,
    NikuReportAttribute,
    project::Timeoff,
    NewTaskAttribute,
    project::Remaining,
    project::Work,
    IcalReportAttribute,
    project::ScenarioIcal,
    project::DurationQuantity,
    StatusTimesheetAttribute,
    project::RGB,
    project::LogicalExpression,
    ColumnAttribute,
    project::ToolTip,
    project::ListItem,
    project::FontColor,
    project::Scale,
    project::HAlign,
    project::ListType,
    project::Width,
    project::CellText,
    project::CellColor,
    project::Column,
    project::AccountShare,
    StatusStatusSheetAttribute,
    project::Details,
    project::Summary,
    project::Author,
    AllocateResourceAttribute,
    project::Select,
    project::ShiftsAllocate,
    project::Persistent,
    project::Mandatory,
    project::Alternative,
    project::Alert,
    project::NikuReportAttribute,
    project::Interval4,
    project::Booking,
    project::AllocateResourceAttribute,
    project::AllocateResource,
    project::NewTaskAttribute,
    TimesheetAttribute,
    project::TaskTimesheet,
    project::ShiftTimesheet,
    project::StatusTimesheet,
    project::NewTask,
    project::NavigatorAttribute,
    project::ReportAttribute,
    project::ResourceAttribute,
    ResourceAttribute,
    project::Efficiency,
    project::PurgeResource,
    project::WorkingHours,
    project::ShiftsResource,
    project::ExtendedResourceAttribute,
    project::BookingResource,
    project::Email,
    project::Managers,
    project::ExportAttribute,
    project::IcalReportAttribute,
    ReportAttribute,
    project::RollupTask,
    project::RollupResource,
    project::PurgeReport,
    project::SelfContained,
    project::Scenarios,
    project::Right,
    project::JournalMode,
    project::Center,
    project::SortResources,
    project::HideAccount,
    project::CurrencyFormat,
    project::LoadUnit,
    project::Epilog,
    project::Left,
    project::HideJournalEntry,
    project::ResourceRoot,
    project::Timezone,
    project::Caption,
    project::SortJournalEntries,
    project::HideResource,
    project::Formats,
    project::JournalAttributes,
    project::SortTasks,
    project::Title,
    project::NumberFormat,
    project::AccountRoot,
    project::RollupAccount,
    project::HideTask,
    project::Header,
    project::TimeFormat,
    project::Footer,
    project::TaskRoot,
    project::Headline,
    project::Columns,
    project::SortAccounts,
    project::Prolog,
    TextReport,
    TaskReport,
    ResourceReport,
    AccountReport,
    project::Report,
    project::TaskAttribute,
    TaskAttribute,
    project::Note,
    project::Milestone,
    project::BookingTask,
    project::Duration,
    project::Depends,
    project::Warn,
    project::Scheduling,
    project::Start,
    project::ProjectId,
    project::MinStart,
    project::Allocate,
    project::Complete,
    project::MinEnd,
    project::MaxEnd,
    project::Length,
    project::Charge,
    project::JournalEntry,
    project::Precedes,
    project::PurgeTask,
    project::Priority,
    project::Responsible,
    project::End,
    project::ShiftsTask,
    project::ChargeSet,
    project::Fail,
    project::Scheduled,
    project::Effort,
    project::ExtendedTaskAttribute,
    project::MaxStart,
    project::EndCredit,
    project::Period,
    project::ProjectAttribute,
    project::Interval2,
    project::Global,
    IncludePropertiesAttribute,
    project::ReportPrefix,
    project::ResourcePrefix,
    project::TaskPrefix,
    project::AccountPrefix,
    project::AccountAttribute,
    AccountAttribute,
    project::Credit,
    Property,
    project::IncludeProperties,
    project::Export,
    project::TimesheetReport,
    project::Resource,
    project::TaskReport,
    project::Rate,
    project::SupplementAccount,
    project::NikuReport,
    project::Macro,
    project::TagFile,
    project::StatusSheetReport,
    project::AccountReport,
    project::TextReport,
    project::StatusSheet,
    project::Balance,
    project::Navigator,
    project::Timesheet,
    project::Shift,
    project::SupplementTask,
    project::SupplementResource,
    project::ResourceReport,
    project::Copyright,
    project::Task,
    project::IcalReport,
    project::Flags,
    project::Vacation,
    project::ProjectIds,
    project::SupplementReport,
    project::Limits,
    project::Account,
    project::Property,
    project::Project,
    SchedulingPolicy,
    JournalEntrySortCriterion,
    JournalModeValue,
    PurgeResourceAttribute,
    Weekday,
    ScaleResolution,
    DependsPolicy,
    ListTypeValues,
    ReportFormat,
    WorkQuantityUnit,
    AlertLevel,
    LoadDisplayUnit,
    CriterionDirection,
    ColumnId,
    SelectArgument,
    PurgeTaskAttribute,
    PurgeReportAttribute,
    YesNo,
    Justification,
    ChargeApplies,
    TimeUnit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_project::jvmidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(project::JvmIdentifiableElement)


def test_project::jvmidentifiableelement_constructor_exists():
    assert callable(project::JvmIdentifiableElement.__init__)


def test_project::jvmidentifiableelement_constructor_args():
    sig = inspect.signature(project::JvmIdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(LogicalExpression)


def test_logicalexpression_constructor_exists():
    assert callable(LogicalExpression.__init__)


def test_logicalexpression_constructor_args():
    sig = inspect.signature(LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_project::logicalnumeralliteral_is_not_abstract():
    assert not inspect.isabstract(project::LogicalNumeralLiteral)


def test_project::logicalnumeralliteral_constructor_exists():
    assert callable(project::LogicalNumeralLiteral.__init__)


def test_project::logicalnumeralliteral_constructor_args():
    sig = inspect.signature(project::LogicalNumeralLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project::logicalnumeralliteral_has_value():
    assert hasattr(project::LogicalNumeralLiteral, "value")
    descriptor = None
    for klass in project::LogicalNumeralLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project::logicalfunctionexpression_is_not_abstract():
    assert not inspect.isabstract(project::LogicalFunctionExpression)


def test_project::logicalfunctionexpression_constructor_exists():
    assert callable(project::LogicalFunctionExpression.__init__)


def test_project::logicalfunctionexpression_constructor_args():
    sig = inspect.signature(project::LogicalFunctionExpression.__init__)
    params = list(sig.parameters.keys())



def test_project::logicalabsoluteidexression_is_not_abstract():
    assert not inspect.isabstract(project::LogicalAbsoluteIdExression)


def test_project::logicalabsoluteidexression_constructor_exists():
    assert callable(project::LogicalAbsoluteIdExression.__init__)


def test_project::logicalabsoluteidexression_constructor_args():
    sig = inspect.signature(project::LogicalAbsoluteIdExression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project::logicalabsoluteidexression_has_value():
    assert hasattr(project::LogicalAbsoluteIdExression, "value")
    descriptor = None
    for klass in project::LogicalAbsoluteIdExression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project::logicaldateliteral_is_not_abstract():
    assert not inspect.isabstract(project::LogicalDateLiteral)


def test_project::logicaldateliteral_constructor_exists():
    assert callable(project::LogicalDateLiteral.__init__)


def test_project::logicaldateliteral_constructor_args():
    sig = inspect.signature(project::LogicalDateLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project::logicaldateliteral_has_value():
    assert hasattr(project::LogicalDateLiteral, "value")
    descriptor = None
    for klass in project::LogicalDateLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project::logicalbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(project::LogicalBooleanLiteral)


def test_project::logicalbooleanliteral_constructor_exists():
    assert callable(project::LogicalBooleanLiteral.__init__)


def test_project::logicalbooleanliteral_constructor_args():
    sig = inspect.signature(project::LogicalBooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "isTrue" in params, "Missing parameter 'isTrue'"

def test_project::logicalbooleanliteral_has_isTrue():
    assert hasattr(project::LogicalBooleanLiteral, "isTrue")
    descriptor = None
    for klass in project::LogicalBooleanLiteral.__mro__:
        if "isTrue" in klass.__dict__:
            descriptor = klass.__dict__["isTrue"]
            break
    assert isinstance(descriptor, property)



def test_project::logicalstringliteral_is_not_abstract():
    assert not inspect.isabstract(project::LogicalStringLiteral)


def test_project::logicalstringliteral_constructor_exists():
    assert callable(project::LogicalStringLiteral.__init__)


def test_project::logicalstringliteral_constructor_args():
    sig = inspect.signature(project::LogicalStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project::logicalstringliteral_has_value():
    assert hasattr(project::LogicalStringLiteral, "value")
    descriptor = None
    for klass in project::LogicalStringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project::xbinaryoperation_is_not_abstract():
    assert not inspect.isabstract(project::XBinaryOperation)


def test_project::xbinaryoperation_constructor_exists():
    assert callable(project::XBinaryOperation.__init__)


def test_project::xbinaryoperation_constructor_args():
    sig = inspect.signature(project::XBinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_definitions_is_not_abstract():
    assert not inspect.isabstract(Definitions)


def test_definitions_constructor_exists():
    assert callable(Definitions.__init__)


def test_definitions_constructor_args():
    sig = inspect.signature(Definitions.__init__)
    params = list(sig.parameters.keys())



def test_project::defintions_is_not_abstract():
    assert not inspect.isabstract(project::Defintions)


def test_project::defintions_constructor_exists():
    assert callable(project::Defintions.__init__)


def test_project::defintions_constructor_args():
    sig = inspect.signature(project::Defintions.__init__)
    params = list(sig.parameters.keys())
    assert "flags" in params, "Missing parameter 'flags'"
    assert "project" in params, "Missing parameter 'project'"
    assert "tasks" in params, "Missing parameter 'tasks'"
    assert "projectids" in params, "Missing parameter 'projectids'"
    assert "resources" in params, "Missing parameter 'resources'"

def test_project::defintions_has_flags():
    assert hasattr(project::Defintions, "flags")
    descriptor = None
    for klass in project::Defintions.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)

def test_project::defintions_has_project():
    assert hasattr(project::Defintions, "project")
    descriptor = None
    for klass in project::Defintions.__mro__:
        if "project" in klass.__dict__:
            descriptor = klass.__dict__["project"]
            break
    assert isinstance(descriptor, property)

def test_project::defintions_has_tasks():
    assert hasattr(project::Defintions, "tasks")
    descriptor = None
    for klass in project::Defintions.__mro__:
        if "tasks" in klass.__dict__:
            descriptor = klass.__dict__["tasks"]
            break
    assert isinstance(descriptor, property)

def test_project::defintions_has_projectids():
    assert hasattr(project::Defintions, "projectids")
    descriptor = None
    for klass in project::Defintions.__mro__:
        if "projectids" in klass.__dict__:
            descriptor = klass.__dict__["projectids"]
            break
    assert isinstance(descriptor, property)

def test_project::defintions_has_resources():
    assert hasattr(project::Defintions, "resources")
    descriptor = None
    for klass in project::Defintions.__mro__:
        if "resources" in klass.__dict__:
            descriptor = klass.__dict__["resources"]
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



def test_project::richtext_is_not_abstract():
    assert not inspect.isabstract(project::RichText)


def test_project::richtext_constructor_exists():
    assert callable(project::RichText.__init__)


def test_project::richtext_constructor_args():
    sig = inspect.signature(project::RichText.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_project::richtext_has_text():
    assert hasattr(project::RichText, "text")
    descriptor = None
    for klass in project::RichText.__mro__:
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



def test_project::taskdependency_is_not_abstract():
    assert not inspect.isabstract(project::TaskDependency)


def test_project::taskdependency_constructor_exists():
    assert callable(project::TaskDependency.__init__)


def test_project::taskdependency_constructor_args():
    sig = inspect.signature(project::TaskDependency.__init__)
    params = list(sig.parameters.keys())
    assert "policy" in params, "Missing parameter 'policy'"

def test_project::taskdependency_has_policy():
    assert hasattr(project::TaskDependency, "policy")
    descriptor = None
    for klass in project::TaskDependency.__mro__:
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



def test_project::realformat_is_not_abstract():
    assert not inspect.isabstract(project::RealFormat)


def test_project::realformat_constructor_exists():
    assert callable(project::RealFormat.__init__)


def test_project::realformat_constructor_args():
    sig = inspect.signature(project::RealFormat.__init__)
    params = list(sig.parameters.keys())
    assert "negativeSuffix" in params, "Missing parameter 'negativeSuffix'"
    assert "fractionSeparator" in params, "Missing parameter 'fractionSeparator'"
    assert "negativePrefix" in params, "Missing parameter 'negativePrefix'"
    assert "fractionDigits" in params, "Missing parameter 'fractionDigits'"
    assert "thousandsSeparator" in params, "Missing parameter 'thousandsSeparator'"

def test_project::realformat_has_negativeSuffix():
    assert hasattr(project::RealFormat, "negativeSuffix")
    descriptor = None
    for klass in project::RealFormat.__mro__:
        if "negativeSuffix" in klass.__dict__:
            descriptor = klass.__dict__["negativeSuffix"]
            break
    assert isinstance(descriptor, property)

def test_project::realformat_has_fractionSeparator():
    assert hasattr(project::RealFormat, "fractionSeparator")
    descriptor = None
    for klass in project::RealFormat.__mro__:
        if "fractionSeparator" in klass.__dict__:
            descriptor = klass.__dict__["fractionSeparator"]
            break
    assert isinstance(descriptor, property)

def test_project::realformat_has_negativePrefix():
    assert hasattr(project::RealFormat, "negativePrefix")
    descriptor = None
    for klass in project::RealFormat.__mro__:
        if "negativePrefix" in klass.__dict__:
            descriptor = klass.__dict__["negativePrefix"]
            break
    assert isinstance(descriptor, property)

def test_project::realformat_has_fractionDigits():
    assert hasattr(project::RealFormat, "fractionDigits")
    descriptor = None
    for klass in project::RealFormat.__mro__:
        if "fractionDigits" in klass.__dict__:
            descriptor = klass.__dict__["fractionDigits"]
            break
    assert isinstance(descriptor, property)

def test_project::realformat_has_thousandsSeparator():
    assert hasattr(project::RealFormat, "thousandsSeparator")
    descriptor = None
    for klass in project::RealFormat.__mro__:
        if "thousandsSeparator" in klass.__dict__:
            descriptor = klass.__dict__["thousandsSeparator"]
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



def test_project::limitattribute_is_not_abstract():
    assert not inspect.isabstract(project::LimitAttribute)


def test_project::limitattribute_constructor_exists():
    assert callable(project::LimitAttribute.__init__)


def test_project::limitattribute_constructor_args():
    sig = inspect.signature(project::LimitAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"

def test_project::limitattribute_has_end():
    assert hasattr(project::LimitAttribute, "end")
    descriptor = None
    for klass in project::LimitAttribute.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_project::limitattribute_has_start():
    assert hasattr(project::LimitAttribute, "start")
    descriptor = None
    for klass in project::LimitAttribute.__mro__:
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



def test_project::limit_is_not_abstract():
    assert not inspect.isabstract(project::Limit)


def test_project::limit_constructor_exists():
    assert callable(project::Limit.__init__)


def test_project::limit_constructor_args():
    sig = inspect.signature(project::Limit.__init__)
    params = list(sig.parameters.keys())



def test_project::columnattribute_is_not_abstract():
    assert not inspect.isabstract(project::ColumnAttribute)


def test_project::columnattribute_constructor_exists():
    assert callable(project::ColumnAttribute.__init__)


def test_project::columnattribute_constructor_args():
    sig = inspect.signature(project::ColumnAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::workhours_is_not_abstract():
    assert not inspect.isabstract(project::WorkHours)


def test_project::workhours_constructor_exists():
    assert callable(project::WorkHours.__init__)


def test_project::workhours_constructor_args():
    sig = inspect.signature(project::WorkHours.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "stop" in params, "Missing parameter 'stop'"

def test_project::workhours_has_start():
    assert hasattr(project::WorkHours, "start")
    descriptor = None
    for klass in project::WorkHours.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_project::workhours_has_stop():
    assert hasattr(project::WorkHours, "stop")
    descriptor = None
    for klass in project::WorkHours.__mro__:
        if "stop" in klass.__dict__:
            descriptor = klass.__dict__["stop"]
            break
    assert isinstance(descriptor, property)



def test_project::weekdays_is_not_abstract():
    assert not inspect.isabstract(project::Weekdays)


def test_project::weekdays_constructor_exists():
    assert callable(project::Weekdays.__init__)


def test_project::weekdays_constructor_args():
    sig = inspect.signature(project::Weekdays.__init__)
    params = list(sig.parameters.keys())
    assert "first" in params, "Missing parameter 'first'"
    assert "last" in params, "Missing parameter 'last'"

def test_project::weekdays_has_first():
    assert hasattr(project::Weekdays, "first")
    descriptor = None
    for klass in project::Weekdays.__mro__:
        if "first" in klass.__dict__:
            descriptor = klass.__dict__["first"]
            break
    assert isinstance(descriptor, property)

def test_project::weekdays_has_last():
    assert hasattr(project::Weekdays, "last")
    descriptor = None
    for klass in project::Weekdays.__mro__:
        if "last" in klass.__dict__:
            descriptor = klass.__dict__["last"]
            break
    assert isinstance(descriptor, property)



def test_project::treelevel_is_not_abstract():
    assert not inspect.isabstract(project::TreeLevel)


def test_project::treelevel_constructor_exists():
    assert callable(project::TreeLevel.__init__)


def test_project::treelevel_constructor_args():
    sig = inspect.signature(project::TreeLevel.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_project::treelevel_has_level():
    assert hasattr(project::TreeLevel, "level")
    descriptor = None
    for klass in project::TreeLevel.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_project::timesheetreportattribute_is_not_abstract():
    assert not inspect.isabstract(project::TimesheetReportAttribute)


def test_project::timesheetreportattribute_constructor_exists():
    assert callable(project::TimesheetReportAttribute.__init__)


def test_project::timesheetreportattribute_constructor_args():
    sig = inspect.signature(project::TimesheetReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::timesheetattribute_is_not_abstract():
    assert not inspect.isabstract(project::TimesheetAttribute)


def test_project::timesheetattribute_constructor_exists():
    assert callable(project::TimesheetAttribute.__init__)


def test_project::timesheetattribute_constructor_args():
    sig = inspect.signature(project::TimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_statussheetattribute_is_not_abstract():
    assert not inspect.isabstract(StatusSheetAttribute)


def test_statussheetattribute_constructor_exists():
    assert callable(StatusSheetAttribute.__init__)


def test_statussheetattribute_constructor_args():
    sig = inspect.signature(StatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::tasktimesheetattribute_is_not_abstract():
    assert not inspect.isabstract(project::TaskTimesheetAttribute)


def test_project::tasktimesheetattribute_constructor_exists():
    assert callable(project::TaskTimesheetAttribute.__init__)


def test_project::tasktimesheetattribute_constructor_args():
    sig = inspect.signature(project::TaskTimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::taskstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(project::TaskStatusSheetAttribute)


def test_project::taskstatussheetattribute_constructor_exists():
    assert callable(project::TaskStatusSheetAttribute.__init__)


def test_project::taskstatussheetattribute_constructor_args():
    sig = inspect.signature(project::TaskStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::statussheetreportattribute_is_not_abstract():
    assert not inspect.isabstract(project::StatusSheetReportAttribute)


def test_project::statussheetreportattribute_constructor_exists():
    assert callable(project::StatusSheetReportAttribute.__init__)


def test_project::statussheetreportattribute_constructor_args():
    sig = inspect.signature(project::StatusSheetReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::statussheetattribute_is_not_abstract():
    assert not inspect.isabstract(project::StatusSheetAttribute)


def test_project::statussheetattribute_constructor_exists():
    assert callable(project::StatusSheetAttribute.__init__)


def test_project::statussheetattribute_constructor_args():
    sig = inspect.signature(project::StatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::statustimesheetattribute_is_not_abstract():
    assert not inspect.isabstract(project::StatusTimesheetAttribute)


def test_project::statustimesheetattribute_constructor_exists():
    assert callable(project::StatusTimesheetAttribute.__init__)


def test_project::statustimesheetattribute_constructor_args():
    sig = inspect.signature(project::StatusTimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::criterion_is_not_abstract():
    assert not inspect.isabstract(project::Criterion)


def test_project::criterion_constructor_exists():
    assert callable(project::Criterion.__init__)


def test_project::criterion_constructor_args():
    sig = inspect.signature(project::Criterion.__init__)
    params = list(sig.parameters.keys())
    assert "columnId" in params, "Missing parameter 'columnId'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_project::criterion_has_columnId():
    assert hasattr(project::Criterion, "columnId")
    descriptor = None
    for klass in project::Criterion.__mro__:
        if "columnId" in klass.__dict__:
            descriptor = klass.__dict__["columnId"]
            break
    assert isinstance(descriptor, property)

def test_project::criterion_has_direction():
    assert hasattr(project::Criterion, "direction")
    descriptor = None
    for klass in project::Criterion.__mro__:
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



def test_project::sort_is_not_abstract():
    assert not inspect.isabstract(project::Sort)


def test_project::sort_constructor_exists():
    assert callable(project::Sort.__init__)


def test_project::sort_constructor_args():
    sig = inspect.signature(project::Sort.__init__)
    params = list(sig.parameters.keys())
    assert "tree" in params, "Missing parameter 'tree'"

def test_project::sort_has_tree():
    assert hasattr(project::Sort, "tree")
    descriptor = None
    for klass in project::Sort.__mro__:
        if "tree" in klass.__dict__:
            descriptor = klass.__dict__["tree"]
            break
    assert isinstance(descriptor, property)



def test_project::statusstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(project::StatusStatusSheetAttribute)


def test_project::statusstatussheetattribute_constructor_exists():
    assert callable(project::StatusStatusSheetAttribute.__init__)


def test_project::statusstatussheetattribute_constructor_args():
    sig = inspect.signature(project::StatusStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_taskstatussheetattribute_is_not_abstract():
    assert not inspect.isabstract(TaskStatusSheetAttribute)


def test_taskstatussheetattribute_constructor_exists():
    assert callable(TaskStatusSheetAttribute.__init__)


def test_taskstatussheetattribute_constructor_args():
    sig = inspect.signature(TaskStatusSheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::taskstatussheet_is_not_abstract():
    assert not inspect.isabstract(project::TaskStatusSheet)


def test_project::taskstatussheet_constructor_exists():
    assert callable(project::TaskStatusSheet.__init__)


def test_project::taskstatussheet_constructor_args():
    sig = inspect.signature(project::TaskStatusSheet.__init__)
    params = list(sig.parameters.keys())



def test_project::statusstatussheet_is_not_abstract():
    assert not inspect.isabstract(project::StatusStatusSheet)


def test_project::statusstatussheet_constructor_exists():
    assert callable(project::StatusStatusSheet.__init__)


def test_project::statusstatussheet_constructor_args():
    sig = inspect.signature(project::StatusStatusSheet.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "level" in params, "Missing parameter 'level'"

def test_project::statusstatussheet_has_text():
    assert hasattr(project::StatusStatusSheet, "text")
    descriptor = None
    for klass in project::StatusStatusSheet.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_project::statusstatussheet_has_level():
    assert hasattr(project::StatusStatusSheet, "level")
    descriptor = None
    for klass in project::StatusStatusSheet.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_project::shiftslimit_is_not_abstract():
    assert not inspect.isabstract(project::ShiftsLimit)


def test_project::shiftslimit_constructor_exists():
    assert callable(project::ShiftsLimit.__init__)


def test_project::shiftslimit_constructor_args():
    sig = inspect.signature(project::ShiftsLimit.__init__)
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



def test_project::shifts_is_not_abstract():
    assert not inspect.isabstract(project::Shifts)


def test_project::shifts_constructor_exists():
    assert callable(project::Shifts.__init__)


def test_project::shifts_constructor_args():
    sig = inspect.signature(project::Shifts.__init__)
    params = list(sig.parameters.keys())



def test_project::limitsattribute_is_not_abstract():
    assert not inspect.isabstract(project::LimitsAttribute)


def test_project::limitsattribute_constructor_exists():
    assert callable(project::LimitsAttribute.__init__)


def test_project::limitsattribute_constructor_args():
    sig = inspect.signature(project::LimitsAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::interval3_is_not_abstract():
    assert not inspect.isabstract(project::Interval3)


def test_project::interval3_constructor_exists():
    assert callable(project::Interval3.__init__)


def test_project::interval3_constructor_args():
    sig = inspect.signature(project::Interval3.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_project::interval3_has_start():
    assert hasattr(project::Interval3, "start")
    descriptor = None
    for klass in project::Interval3.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_project::interval3_has_end():
    assert hasattr(project::Interval3, "end")
    descriptor = None
    for klass in project::Interval3.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_project::interval1_is_not_abstract():
    assert not inspect.isabstract(project::Interval1)


def test_project::interval1_constructor_exists():
    assert callable(project::Interval1.__init__)


def test_project::interval1_constructor_args():
    sig = inspect.signature(project::Interval1.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_project::interval1_has_start():
    assert hasattr(project::Interval1, "start")
    descriptor = None
    for klass in project::Interval1.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_project::interval1_has_end():
    assert hasattr(project::Interval1, "end")
    descriptor = None
    for klass in project::Interval1.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_project::includepropertiesattribute_is_not_abstract():
    assert not inspect.isabstract(project::IncludePropertiesAttribute)


def test_project::includepropertiesattribute_constructor_exists():
    assert callable(project::IncludePropertiesAttribute.__init__)


def test_project::includepropertiesattribute_constructor_args():
    sig = inspect.signature(project::IncludePropertiesAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::function_is_not_abstract():
    assert not inspect.isabstract(project::Function)


def test_project::function_constructor_exists():
    assert callable(project::Function.__init__)


def test_project::function_constructor_args():
    sig = inspect.signature(project::Function.__init__)
    params = list(sig.parameters.keys())
    assert "parentId" in params, "Missing parameter 'parentId'"
    assert "level" in params, "Missing parameter 'level'"
    assert "date" in params, "Missing parameter 'date'"
    assert "distance" in params, "Missing parameter 'distance'"

def test_project::function_has_parentId():
    assert hasattr(project::Function, "parentId")
    descriptor = None
    for klass in project::Function.__mro__:
        if "parentId" in klass.__dict__:
            descriptor = klass.__dict__["parentId"]
            break
    assert isinstance(descriptor, property)

def test_project::function_has_level():
    assert hasattr(project::Function, "level")
    descriptor = None
    for klass in project::Function.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_project::function_has_date():
    assert hasattr(project::Function, "date")
    descriptor = None
    for klass in project::Function.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_project::function_has_distance():
    assert hasattr(project::Function, "distance")
    descriptor = None
    for klass in project::Function.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_navigatorattribute_is_not_abstract():
    assert not inspect.isabstract(NavigatorAttribute)


def test_navigatorattribute_constructor_exists():
    assert callable(NavigatorAttribute.__init__)


def test_navigatorattribute_constructor_args():
    sig = inspect.signature(NavigatorAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::hidereport_is_not_abstract():
    assert not inspect.isabstract(project::HideReport)


def test_project::hidereport_constructor_exists():
    assert callable(project::HideReport.__init__)


def test_project::hidereport_constructor_args():
    sig = inspect.signature(project::HideReport.__init__)
    params = list(sig.parameters.keys())



def test_project::gaplength_is_not_abstract():
    assert not inspect.isabstract(project::GapLength)


def test_project::gaplength_constructor_exists():
    assert callable(project::GapLength.__init__)


def test_project::gaplength_constructor_args():
    sig = inspect.signature(project::GapLength.__init__)
    params = list(sig.parameters.keys())



def test_project::gapduration_is_not_abstract():
    assert not inspect.isabstract(project::GapDuration)


def test_project::gapduration_constructor_exists():
    assert callable(project::GapDuration.__init__)


def test_project::gapduration_constructor_args():
    sig = inspect.signature(project::GapDuration.__init__)
    params = list(sig.parameters.keys())



def test_project::extend_is_not_abstract():
    assert not inspect.isabstract(project::Extend)


def test_project::extend_constructor_exists():
    assert callable(project::Extend.__init__)


def test_project::extend_constructor_args():
    sig = inspect.signature(project::Extend.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "scenariospecific" in params, "Missing parameter 'scenariospecific'"
    assert "id" in params, "Missing parameter 'id'"
    assert "inherit" in params, "Missing parameter 'inherit'"

def test_project::extend_has_name():
    assert hasattr(project::Extend, "name")
    descriptor = None
    for klass in project::Extend.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project::extend_has_scenariospecific():
    assert hasattr(project::Extend, "scenariospecific")
    descriptor = None
    for klass in project::Extend.__mro__:
        if "scenariospecific" in klass.__dict__:
            descriptor = klass.__dict__["scenariospecific"]
            break
    assert isinstance(descriptor, property)

def test_project::extend_has_id():
    assert hasattr(project::Extend, "id")
    descriptor = None
    for klass in project::Extend.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_project::extend_has_inherit():
    assert hasattr(project::Extend, "inherit")
    descriptor = None
    for klass in project::Extend.__mro__:
        if "inherit" in klass.__dict__:
            descriptor = klass.__dict__["inherit"]
            break
    assert isinstance(descriptor, property)



def test_exportattribute_is_not_abstract():
    assert not inspect.isabstract(ExportAttribute)


def test_exportattribute_constructor_exists():
    assert callable(ExportAttribute.__init__)


def test_exportattribute_constructor_args():
    sig = inspect.signature(ExportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::taskattributes_is_not_abstract():
    assert not inspect.isabstract(project::TaskAttributes)


def test_project::taskattributes_constructor_exists():
    assert callable(project::TaskAttributes.__init__)


def test_project::taskattributes_constructor_args():
    sig = inspect.signature(project::TaskAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "flags" in params, "Missing parameter 'flags'"
    assert "maxstart" in params, "Missing parameter 'maxstart'"
    assert "booking" in params, "Missing parameter 'booking'"
    assert "note" in params, "Missing parameter 'note'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "complete" in params, "Missing parameter 'complete'"
    assert "none" in params, "Missing parameter 'none'"
    assert "maxend" in params, "Missing parameter 'maxend'"
    assert "minstart" in params, "Missing parameter 'minstart'"
    assert "all" in params, "Missing parameter 'all'"
    assert "minend" in params, "Missing parameter 'minend'"
    assert "depends" in params, "Missing parameter 'depends'"
    assert "responsible" in params, "Missing parameter 'responsible'"

def test_project::taskattributes_has_flags():
    assert hasattr(project::TaskAttributes, "flags")
    descriptor = None
    for klass in project::TaskAttributes.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)

def test_project::taskattributes_has_maxstart():
    assert hasattr(project::TaskAttributes, "maxstart")
    descriptor = None
    for klass in project::TaskAttributes.__mro__:
        if "maxstart" in klass.__dict__:
            descriptor = klass.__dict__["maxstart"]
            break
    assert isinstance(descriptor, property)

def test_project::taskattributes_has_booking():
    assert hasattr(project::TaskAttributes, "booking")
    descriptor = None
    for klass in project::TaskAttributes.__mro__:
        if "booking" in klass.__dict__:
            descriptor = klass.__dict__["booking"]
            break
    assert isinstance(descriptor, property)

def test_project::taskattributes_has_note():
    assert hasattr(project::TaskAttributes, "note")
    descriptor = None
    for klass in project::TaskAttributes.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_project::taskattributes_has_priority():
    assert hasattr(project::TaskAttributes, "priority")
    descriptor = None
    for klass in project::TaskAttributes.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_project::taskattributes_has_complete():
    assert hasattr(project::TaskAttributes, "complete")
    descriptor = None
    for klass in project::TaskAttributes.__mro__:
        if "complete" in klass.__dict__:
            descriptor = klass.__dict__["complete"]
            break
    assert isinstance(descriptor, property)

def test_project::taskattributes_has_none():
    assert hasattr(project::TaskAttributes, "none")
    descriptor = None
    for klass in project::TaskAttributes.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_project::taskattributes_has_maxend():
    assert hasattr(project::TaskAttributes, "maxend")
    descriptor = None
    for klass in project::TaskAttributes.__mro__:
        if "maxend" in klass.__dict__:
            descriptor = klass.__dict__["maxend"]
            break
    assert isinstance(descriptor, property)

def test_project::taskattributes_has_minstart():
    assert hasattr(project::TaskAttributes, "minstart")
    descriptor = None
    for klass in project::TaskAttributes.__mro__:
        if "minstart" in klass.__dict__:
            descriptor = klass.__dict__["minstart"]
            break
    assert isinstance(descriptor, property)

def test_project::taskattributes_has_all():
    assert hasattr(project::TaskAttributes, "all")
    descriptor = None
    for klass in project::TaskAttributes.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_project::taskattributes_has_minend():
    assert hasattr(project::TaskAttributes, "minend")
    descriptor = None
    for klass in project::TaskAttributes.__mro__:
        if "minend" in klass.__dict__:
            descriptor = klass.__dict__["minend"]
            break
    assert isinstance(descriptor, property)

def test_project::taskattributes_has_depends():
    assert hasattr(project::TaskAttributes, "depends")
    descriptor = None
    for klass in project::TaskAttributes.__mro__:
        if "depends" in klass.__dict__:
            descriptor = klass.__dict__["depends"]
            break
    assert isinstance(descriptor, property)

def test_project::taskattributes_has_responsible():
    assert hasattr(project::TaskAttributes, "responsible")
    descriptor = None
    for klass in project::TaskAttributes.__mro__:
        if "responsible" in klass.__dict__:
            descriptor = klass.__dict__["responsible"]
            break
    assert isinstance(descriptor, property)



def test_project::resourceattributes_is_not_abstract():
    assert not inspect.isabstract(project::ResourceAttributes)


def test_project::resourceattributes_constructor_exists():
    assert callable(project::ResourceAttributes.__init__)


def test_project::resourceattributes_constructor_args():
    sig = inspect.signature(project::ResourceAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "none" in params, "Missing parameter 'none'"
    assert "booking" in params, "Missing parameter 'booking'"
    assert "workingHours" in params, "Missing parameter 'workingHours'"
    assert "vacation" in params, "Missing parameter 'vacation'"
    assert "all" in params, "Missing parameter 'all'"

def test_project::resourceattributes_has_none():
    assert hasattr(project::ResourceAttributes, "none")
    descriptor = None
    for klass in project::ResourceAttributes.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_project::resourceattributes_has_booking():
    assert hasattr(project::ResourceAttributes, "booking")
    descriptor = None
    for klass in project::ResourceAttributes.__mro__:
        if "booking" in klass.__dict__:
            descriptor = klass.__dict__["booking"]
            break
    assert isinstance(descriptor, property)

def test_project::resourceattributes_has_workingHours():
    assert hasattr(project::ResourceAttributes, "workingHours")
    descriptor = None
    for klass in project::ResourceAttributes.__mro__:
        if "workingHours" in klass.__dict__:
            descriptor = klass.__dict__["workingHours"]
            break
    assert isinstance(descriptor, property)

def test_project::resourceattributes_has_vacation():
    assert hasattr(project::ResourceAttributes, "vacation")
    descriptor = None
    for klass in project::ResourceAttributes.__mro__:
        if "vacation" in klass.__dict__:
            descriptor = klass.__dict__["vacation"]
            break
    assert isinstance(descriptor, property)

def test_project::resourceattributes_has_all():
    assert hasattr(project::ResourceAttributes, "all")
    descriptor = None
    for klass in project::ResourceAttributes.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_project::definitions_is_not_abstract():
    assert not inspect.isabstract(project::Definitions)


def test_project::definitions_constructor_exists():
    assert callable(project::Definitions.__init__)


def test_project::definitions_constructor_args():
    sig = inspect.signature(project::Definitions.__init__)
    params = list(sig.parameters.keys())
    assert "none" in params, "Missing parameter 'none'"
    assert "all" in params, "Missing parameter 'all'"

def test_project::definitions_has_none():
    assert hasattr(project::Definitions, "none")
    descriptor = None
    for klass in project::Definitions.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_project::definitions_has_all():
    assert hasattr(project::Definitions, "all")
    descriptor = None
    for klass in project::Definitions.__mro__:
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



def test_project::weeklymin_is_not_abstract():
    assert not inspect.isabstract(project::WeeklyMin)


def test_project::weeklymin_constructor_exists():
    assert callable(project::WeeklyMin.__init__)


def test_project::weeklymin_constructor_args():
    sig = inspect.signature(project::WeeklyMin.__init__)
    params = list(sig.parameters.keys())



def test_project::maximum_is_not_abstract():
    assert not inspect.isabstract(project::Maximum)


def test_project::maximum_constructor_exists():
    assert callable(project::Maximum.__init__)


def test_project::maximum_constructor_args():
    sig = inspect.signature(project::Maximum.__init__)
    params = list(sig.parameters.keys())



def test_project::monthlymax_is_not_abstract():
    assert not inspect.isabstract(project::MonthlyMax)


def test_project::monthlymax_constructor_exists():
    assert callable(project::MonthlyMax.__init__)


def test_project::monthlymax_constructor_args():
    sig = inspect.signature(project::MonthlyMax.__init__)
    params = list(sig.parameters.keys())



def test_project::weeklymax_is_not_abstract():
    assert not inspect.isabstract(project::WeeklyMax)


def test_project::weeklymax_constructor_exists():
    assert callable(project::WeeklyMax.__init__)


def test_project::weeklymax_constructor_args():
    sig = inspect.signature(project::WeeklyMax.__init__)
    params = list(sig.parameters.keys())



def test_project::minimum_is_not_abstract():
    assert not inspect.isabstract(project::Minimum)


def test_project::minimum_constructor_exists():
    assert callable(project::Minimum.__init__)


def test_project::minimum_constructor_args():
    sig = inspect.signature(project::Minimum.__init__)
    params = list(sig.parameters.keys())



def test_project::dailymin_is_not_abstract():
    assert not inspect.isabstract(project::DailyMin)


def test_project::dailymin_constructor_exists():
    assert callable(project::DailyMin.__init__)


def test_project::dailymin_constructor_args():
    sig = inspect.signature(project::DailyMin.__init__)
    params = list(sig.parameters.keys())



def test_project::monthlymin_is_not_abstract():
    assert not inspect.isabstract(project::MonthlyMin)


def test_project::monthlymin_constructor_exists():
    assert callable(project::MonthlyMin.__init__)


def test_project::monthlymin_constructor_args():
    sig = inspect.signature(project::MonthlyMin.__init__)
    params = list(sig.parameters.keys())



def test_project::dailymax_is_not_abstract():
    assert not inspect.isabstract(project::DailyMax)


def test_project::dailymax_constructor_exists():
    assert callable(project::DailyMax.__init__)


def test_project::dailymax_constructor_args():
    sig = inspect.signature(project::DailyMax.__init__)
    params = list(sig.parameters.keys())



def test_projectattribute_is_not_abstract():
    assert not inspect.isabstract(ProjectAttribute)


def test_projectattribute_constructor_exists():
    assert callable(ProjectAttribute.__init__)


def test_projectattribute_constructor_args():
    sig = inspect.signature(ProjectAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::timingresolution_is_not_abstract():
    assert not inspect.isabstract(project::TimingResolution)


def test_project::timingresolution_constructor_exists():
    assert callable(project::TimingResolution.__init__)


def test_project::timingresolution_constructor_args():
    sig = inspect.signature(project::TimingResolution.__init__)
    params = list(sig.parameters.keys())
    assert "timingResolution" in params, "Missing parameter 'timingResolution'"

def test_project::timingresolution_has_timingResolution():
    assert hasattr(project::TimingResolution, "timingResolution")
    descriptor = None
    for klass in project::TimingResolution.__mro__:
        if "timingResolution" in klass.__dict__:
            descriptor = klass.__dict__["timingResolution"]
            break
    assert isinstance(descriptor, property)



def test_project::extendresource_is_not_abstract():
    assert not inspect.isabstract(project::ExtendResource)


def test_project::extendresource_constructor_exists():
    assert callable(project::ExtendResource.__init__)


def test_project::extendresource_constructor_args():
    sig = inspect.signature(project::ExtendResource.__init__)
    params = list(sig.parameters.keys())



def test_project::extendtask_is_not_abstract():
    assert not inspect.isabstract(project::ExtendTask)


def test_project::extendtask_constructor_exists():
    assert callable(project::ExtendTask.__init__)


def test_project::extendtask_constructor_args():
    sig = inspect.signature(project::ExtendTask.__init__)
    params = list(sig.parameters.keys())



def test_project::dailyworkinghours_is_not_abstract():
    assert not inspect.isabstract(project::DailyWorkingHours)


def test_project::dailyworkinghours_constructor_exists():
    assert callable(project::DailyWorkingHours.__init__)


def test_project::dailyworkinghours_constructor_args():
    sig = inspect.signature(project::DailyWorkingHours.__init__)
    params = list(sig.parameters.keys())
    assert "dailyWorkingHours" in params, "Missing parameter 'dailyWorkingHours'"

def test_project::dailyworkinghours_has_dailyWorkingHours():
    assert hasattr(project::DailyWorkingHours, "dailyWorkingHours")
    descriptor = None
    for klass in project::DailyWorkingHours.__mro__:
        if "dailyWorkingHours" in klass.__dict__:
            descriptor = klass.__dict__["dailyWorkingHours"]
            break
    assert isinstance(descriptor, property)



def test_project::shorttimeformat_is_not_abstract():
    assert not inspect.isabstract(project::ShortTimeFormat)


def test_project::shorttimeformat_constructor_exists():
    assert callable(project::ShortTimeFormat.__init__)


def test_project::shorttimeformat_constructor_args():
    sig = inspect.signature(project::ShortTimeFormat.__init__)
    params = list(sig.parameters.keys())
    assert "shortTimeFormat" in params, "Missing parameter 'shortTimeFormat'"

def test_project::shorttimeformat_has_shortTimeFormat():
    assert hasattr(project::ShortTimeFormat, "shortTimeFormat")
    descriptor = None
    for klass in project::ShortTimeFormat.__mro__:
        if "shortTimeFormat" in klass.__dict__:
            descriptor = klass.__dict__["shortTimeFormat"]
            break
    assert isinstance(descriptor, property)



def test_project::weekstarts_is_not_abstract():
    assert not inspect.isabstract(project::WeekStarts)


def test_project::weekstarts_constructor_exists():
    assert callable(project::WeekStarts.__init__)


def test_project::weekstarts_constructor_args():
    sig = inspect.signature(project::WeekStarts.__init__)
    params = list(sig.parameters.keys())
    assert "sunday" in params, "Missing parameter 'sunday'"
    assert "monday" in params, "Missing parameter 'monday'"

def test_project::weekstarts_has_sunday():
    assert hasattr(project::WeekStarts, "sunday")
    descriptor = None
    for klass in project::WeekStarts.__mro__:
        if "sunday" in klass.__dict__:
            descriptor = klass.__dict__["sunday"]
            break
    assert isinstance(descriptor, property)

def test_project::weekstarts_has_monday():
    assert hasattr(project::WeekStarts, "monday")
    descriptor = None
    for klass in project::WeekStarts.__mro__:
        if "monday" in klass.__dict__:
            descriptor = klass.__dict__["monday"]
            break
    assert isinstance(descriptor, property)



def test_project::scenario_is_not_abstract():
    assert not inspect.isabstract(project::Scenario)


def test_project::scenario_constructor_exists():
    assert callable(project::Scenario.__init__)


def test_project::scenario_constructor_args():
    sig = inspect.signature(project::Scenario.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "active" in params, "Missing parameter 'active'"
    assert "id" in params, "Missing parameter 'id'"

def test_project::scenario_has_name():
    assert hasattr(project::Scenario, "name")
    descriptor = None
    for klass in project::Scenario.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project::scenario_has_active():
    assert hasattr(project::Scenario, "active")
    descriptor = None
    for klass in project::Scenario.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_project::scenario_has_id():
    assert hasattr(project::Scenario, "id")
    descriptor = None
    for klass in project::Scenario.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_project::include_is_not_abstract():
    assert not inspect.isabstract(project::Include)


def test_project::include_constructor_exists():
    assert callable(project::Include.__init__)


def test_project::include_constructor_args():
    sig = inspect.signature(project::Include.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_project::include_has_importURI():
    assert hasattr(project::Include, "importURI")
    descriptor = None
    for klass in project::Include.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_project::trackingscenario_is_not_abstract():
    assert not inspect.isabstract(project::TrackingScenario)


def test_project::trackingscenario_constructor_exists():
    assert callable(project::TrackingScenario.__init__)


def test_project::trackingscenario_constructor_args():
    sig = inspect.signature(project::TrackingScenario.__init__)
    params = list(sig.parameters.keys())



def test_project::now_is_not_abstract():
    assert not inspect.isabstract(project::Now)


def test_project::now_constructor_exists():
    assert callable(project::Now.__init__)


def test_project::now_constructor_args():
    sig = inspect.signature(project::Now.__init__)
    params = list(sig.parameters.keys())
    assert "now" in params, "Missing parameter 'now'"

def test_project::now_has_now():
    assert hasattr(project::Now, "now")
    descriptor = None
    for klass in project::Now.__mro__:
        if "now" in klass.__dict__:
            descriptor = klass.__dict__["now"]
            break
    assert isinstance(descriptor, property)



def test_project::yearlyworkingdays_is_not_abstract():
    assert not inspect.isabstract(project::YearlyWorkingDays)


def test_project::yearlyworkingdays_constructor_exists():
    assert callable(project::YearlyWorkingDays.__init__)


def test_project::yearlyworkingdays_constructor_args():
    sig = inspect.signature(project::YearlyWorkingDays.__init__)
    params = list(sig.parameters.keys())
    assert "yearlyWorkingDays" in params, "Missing parameter 'yearlyWorkingDays'"

def test_project::yearlyworkingdays_has_yearlyWorkingDays():
    assert hasattr(project::YearlyWorkingDays, "yearlyWorkingDays")
    descriptor = None
    for klass in project::YearlyWorkingDays.__mro__:
        if "yearlyWorkingDays" in klass.__dict__:
            descriptor = klass.__dict__["yearlyWorkingDays"]
            break
    assert isinstance(descriptor, property)



def test_project::currency_is_not_abstract():
    assert not inspect.isabstract(project::Currency)


def test_project::currency_constructor_exists():
    assert callable(project::Currency.__init__)


def test_project::currency_constructor_args():
    sig = inspect.signature(project::Currency.__init__)
    params = list(sig.parameters.keys())
    assert "currency" in params, "Missing parameter 'currency'"

def test_project::currency_has_currency():
    assert hasattr(project::Currency, "currency")
    descriptor = None
    for klass in project::Currency.__mro__:
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



def test_project::timeoff_is_not_abstract():
    assert not inspect.isabstract(project::Timeoff)


def test_project::timeoff_constructor_exists():
    assert callable(project::Timeoff.__init__)


def test_project::timeoff_constructor_args():
    sig = inspect.signature(project::Timeoff.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_project::timeoff_has_name():
    assert hasattr(project::Timeoff, "name")
    descriptor = None
    for klass in project::Timeoff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project::timeoff_has_id():
    assert hasattr(project::Timeoff, "id")
    descriptor = None
    for klass in project::Timeoff.__mro__:
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



def test_project::remaining_is_not_abstract():
    assert not inspect.isabstract(project::Remaining)


def test_project::remaining_constructor_exists():
    assert callable(project::Remaining.__init__)


def test_project::remaining_constructor_args():
    sig = inspect.signature(project::Remaining.__init__)
    params = list(sig.parameters.keys())



def test_project::work_is_not_abstract():
    assert not inspect.isabstract(project::Work)


def test_project::work_constructor_exists():
    assert callable(project::Work.__init__)


def test_project::work_constructor_args():
    sig = inspect.signature(project::Work.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "value" in params, "Missing parameter 'value'"

def test_project::work_has_unit():
    assert hasattr(project::Work, "unit")
    descriptor = None
    for klass in project::Work.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_project::work_has_value():
    assert hasattr(project::Work, "value")
    descriptor = None
    for klass in project::Work.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_icalreportattribute_is_not_abstract():
    assert not inspect.isabstract(IcalReportAttribute)


def test_icalreportattribute_constructor_exists():
    assert callable(IcalReportAttribute.__init__)


def test_icalreportattribute_constructor_args():
    sig = inspect.signature(IcalReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::scenarioical_is_not_abstract():
    assert not inspect.isabstract(project::ScenarioIcal)


def test_project::scenarioical_constructor_exists():
    assert callable(project::ScenarioIcal.__init__)


def test_project::scenarioical_constructor_args():
    sig = inspect.signature(project::ScenarioIcal.__init__)
    params = list(sig.parameters.keys())



def test_project::durationquantity_is_not_abstract():
    assert not inspect.isabstract(project::DurationQuantity)


def test_project::durationquantity_constructor_exists():
    assert callable(project::DurationQuantity.__init__)


def test_project::durationquantity_constructor_args():
    sig = inspect.signature(project::DurationQuantity.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "value" in params, "Missing parameter 'value'"

def test_project::durationquantity_has_unit():
    assert hasattr(project::DurationQuantity, "unit")
    descriptor = None
    for klass in project::DurationQuantity.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_project::durationquantity_has_value():
    assert hasattr(project::DurationQuantity, "value")
    descriptor = None
    for klass in project::DurationQuantity.__mro__:
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



def test_project::rgb_is_not_abstract():
    assert not inspect.isabstract(project::RGB)


def test_project::rgb_constructor_exists():
    assert callable(project::RGB.__init__)


def test_project::rgb_constructor_args():
    sig = inspect.signature(project::RGB.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project::rgb_has_value():
    assert hasattr(project::RGB, "value")
    descriptor = None
    for klass in project::RGB.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project::logicalexpression_is_not_abstract():
    assert not inspect.isabstract(project::LogicalExpression)


def test_project::logicalexpression_constructor_exists():
    assert callable(project::LogicalExpression.__init__)


def test_project::logicalexpression_constructor_args():
    sig = inspect.signature(project::LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_columnattribute_is_not_abstract():
    assert not inspect.isabstract(ColumnAttribute)


def test_columnattribute_constructor_exists():
    assert callable(ColumnAttribute.__init__)


def test_columnattribute_constructor_args():
    sig = inspect.signature(ColumnAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::tooltip_is_not_abstract():
    assert not inspect.isabstract(project::ToolTip)


def test_project::tooltip_constructor_exists():
    assert callable(project::ToolTip.__init__)


def test_project::tooltip_constructor_args():
    sig = inspect.signature(project::ToolTip.__init__)
    params = list(sig.parameters.keys())
    assert "tip" in params, "Missing parameter 'tip'"

def test_project::tooltip_has_tip():
    assert hasattr(project::ToolTip, "tip")
    descriptor = None
    for klass in project::ToolTip.__mro__:
        if "tip" in klass.__dict__:
            descriptor = klass.__dict__["tip"]
            break
    assert isinstance(descriptor, property)



def test_project::listitem_is_not_abstract():
    assert not inspect.isabstract(project::ListItem)


def test_project::listitem_constructor_exists():
    assert callable(project::ListItem.__init__)


def test_project::listitem_constructor_args():
    sig = inspect.signature(project::ListItem.__init__)
    params = list(sig.parameters.keys())



def test_project::fontcolor_is_not_abstract():
    assert not inspect.isabstract(project::FontColor)


def test_project::fontcolor_constructor_exists():
    assert callable(project::FontColor.__init__)


def test_project::fontcolor_constructor_args():
    sig = inspect.signature(project::FontColor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_project::fontcolor_has_color():
    assert hasattr(project::FontColor, "color")
    descriptor = None
    for klass in project::FontColor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_project::scale_is_not_abstract():
    assert not inspect.isabstract(project::Scale)


def test_project::scale_constructor_exists():
    assert callable(project::Scale.__init__)


def test_project::scale_constructor_args():
    sig = inspect.signature(project::Scale.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"

def test_project::scale_has_scale():
    assert hasattr(project::Scale, "scale")
    descriptor = None
    for klass in project::Scale.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_project::halign_is_not_abstract():
    assert not inspect.isabstract(project::HAlign)


def test_project::halign_constructor_exists():
    assert callable(project::HAlign.__init__)


def test_project::halign_constructor_args():
    sig = inspect.signature(project::HAlign.__init__)
    params = list(sig.parameters.keys())
    assert "justification" in params, "Missing parameter 'justification'"

def test_project::halign_has_justification():
    assert hasattr(project::HAlign, "justification")
    descriptor = None
    for klass in project::HAlign.__mro__:
        if "justification" in klass.__dict__:
            descriptor = klass.__dict__["justification"]
            break
    assert isinstance(descriptor, property)



def test_project::listtype_is_not_abstract():
    assert not inspect.isabstract(project::ListType)


def test_project::listtype_constructor_exists():
    assert callable(project::ListType.__init__)


def test_project::listtype_constructor_args():
    sig = inspect.signature(project::ListType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_project::listtype_has_type():
    assert hasattr(project::ListType, "type")
    descriptor = None
    for klass in project::ListType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_project::width_is_not_abstract():
    assert not inspect.isabstract(project::Width)


def test_project::width_constructor_exists():
    assert callable(project::Width.__init__)


def test_project::width_constructor_args():
    sig = inspect.signature(project::Width.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"

def test_project::width_has_width():
    assert hasattr(project::Width, "width")
    descriptor = None
    for klass in project::Width.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_project::celltext_is_not_abstract():
    assert not inspect.isabstract(project::CellText)


def test_project::celltext_constructor_exists():
    assert callable(project::CellText.__init__)


def test_project::celltext_constructor_args():
    sig = inspect.signature(project::CellText.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_project::celltext_has_text():
    assert hasattr(project::CellText, "text")
    descriptor = None
    for klass in project::CellText.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_project::cellcolor_is_not_abstract():
    assert not inspect.isabstract(project::CellColor)


def test_project::cellcolor_constructor_exists():
    assert callable(project::CellColor.__init__)


def test_project::cellcolor_constructor_args():
    sig = inspect.signature(project::CellColor.__init__)
    params = list(sig.parameters.keys())



def test_project::column_is_not_abstract():
    assert not inspect.isabstract(project::Column)


def test_project::column_constructor_exists():
    assert callable(project::Column.__init__)


def test_project::column_constructor_args():
    sig = inspect.signature(project::Column.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_project::column_has_id():
    assert hasattr(project::Column, "id")
    descriptor = None
    for klass in project::Column.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_project::accountshare_is_not_abstract():
    assert not inspect.isabstract(project::AccountShare)


def test_project::accountshare_constructor_exists():
    assert callable(project::AccountShare.__init__)


def test_project::accountshare_constructor_args():
    sig = inspect.signature(project::AccountShare.__init__)
    params = list(sig.parameters.keys())
    assert "share" in params, "Missing parameter 'share'"

def test_project::accountshare_has_share():
    assert hasattr(project::AccountShare, "share")
    descriptor = None
    for klass in project::AccountShare.__mro__:
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



def test_project::details_is_not_abstract():
    assert not inspect.isabstract(project::Details)


def test_project::details_constructor_exists():
    assert callable(project::Details.__init__)


def test_project::details_constructor_args():
    sig = inspect.signature(project::Details.__init__)
    params = list(sig.parameters.keys())



def test_project::summary_is_not_abstract():
    assert not inspect.isabstract(project::Summary)


def test_project::summary_constructor_exists():
    assert callable(project::Summary.__init__)


def test_project::summary_constructor_args():
    sig = inspect.signature(project::Summary.__init__)
    params = list(sig.parameters.keys())



def test_project::author_is_not_abstract():
    assert not inspect.isabstract(project::Author)


def test_project::author_constructor_exists():
    assert callable(project::Author.__init__)


def test_project::author_constructor_args():
    sig = inspect.signature(project::Author.__init__)
    params = list(sig.parameters.keys())



def test_allocateresourceattribute_is_not_abstract():
    assert not inspect.isabstract(AllocateResourceAttribute)


def test_allocateresourceattribute_constructor_exists():
    assert callable(AllocateResourceAttribute.__init__)


def test_allocateresourceattribute_constructor_args():
    sig = inspect.signature(AllocateResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::select_is_not_abstract():
    assert not inspect.isabstract(project::Select)


def test_project::select_constructor_exists():
    assert callable(project::Select.__init__)


def test_project::select_constructor_args():
    sig = inspect.signature(project::Select.__init__)
    params = list(sig.parameters.keys())
    assert "argument" in params, "Missing parameter 'argument'"

def test_project::select_has_argument():
    assert hasattr(project::Select, "argument")
    descriptor = None
    for klass in project::Select.__mro__:
        if "argument" in klass.__dict__:
            descriptor = klass.__dict__["argument"]
            break
    assert isinstance(descriptor, property)



def test_project::shiftsallocate_is_not_abstract():
    assert not inspect.isabstract(project::ShiftsAllocate)


def test_project::shiftsallocate_constructor_exists():
    assert callable(project::ShiftsAllocate.__init__)


def test_project::shiftsallocate_constructor_args():
    sig = inspect.signature(project::ShiftsAllocate.__init__)
    params = list(sig.parameters.keys())



def test_project::persistent_is_not_abstract():
    assert not inspect.isabstract(project::Persistent)


def test_project::persistent_constructor_exists():
    assert callable(project::Persistent.__init__)


def test_project::persistent_constructor_args():
    sig = inspect.signature(project::Persistent.__init__)
    params = list(sig.parameters.keys())
    assert "persistent" in params, "Missing parameter 'persistent'"

def test_project::persistent_has_persistent():
    assert hasattr(project::Persistent, "persistent")
    descriptor = None
    for klass in project::Persistent.__mro__:
        if "persistent" in klass.__dict__:
            descriptor = klass.__dict__["persistent"]
            break
    assert isinstance(descriptor, property)



def test_project::mandatory_is_not_abstract():
    assert not inspect.isabstract(project::Mandatory)


def test_project::mandatory_constructor_exists():
    assert callable(project::Mandatory.__init__)


def test_project::mandatory_constructor_args():
    sig = inspect.signature(project::Mandatory.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_project::mandatory_has_mandatory():
    assert hasattr(project::Mandatory, "mandatory")
    descriptor = None
    for klass in project::Mandatory.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_project::alternative_is_not_abstract():
    assert not inspect.isabstract(project::Alternative)


def test_project::alternative_constructor_exists():
    assert callable(project::Alternative.__init__)


def test_project::alternative_constructor_args():
    sig = inspect.signature(project::Alternative.__init__)
    params = list(sig.parameters.keys())



def test_project::alert_is_not_abstract():
    assert not inspect.isabstract(project::Alert)


def test_project::alert_constructor_exists():
    assert callable(project::Alert.__init__)


def test_project::alert_constructor_args():
    sig = inspect.signature(project::Alert.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_project::alert_has_level():
    assert hasattr(project::Alert, "level")
    descriptor = None
    for klass in project::Alert.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_project::nikureportattribute_is_not_abstract():
    assert not inspect.isabstract(project::NikuReportAttribute)


def test_project::nikureportattribute_constructor_exists():
    assert callable(project::NikuReportAttribute.__init__)


def test_project::nikureportattribute_constructor_args():
    sig = inspect.signature(project::NikuReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::interval4_is_not_abstract():
    assert not inspect.isabstract(project::Interval4)


def test_project::interval4_constructor_exists():
    assert callable(project::Interval4.__init__)


def test_project::interval4_constructor_args():
    sig = inspect.signature(project::Interval4.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"

def test_project::interval4_has_end():
    assert hasattr(project::Interval4, "end")
    descriptor = None
    for klass in project::Interval4.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_project::interval4_has_start():
    assert hasattr(project::Interval4, "start")
    descriptor = None
    for klass in project::Interval4.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_project::booking_is_not_abstract():
    assert not inspect.isabstract(project::Booking)


def test_project::booking_constructor_exists():
    assert callable(project::Booking.__init__)


def test_project::booking_constructor_args():
    sig = inspect.signature(project::Booking.__init__)
    params = list(sig.parameters.keys())
    assert "sloppy" in params, "Missing parameter 'sloppy'"
    assert "overtime" in params, "Missing parameter 'overtime'"

def test_project::booking_has_sloppy():
    assert hasattr(project::Booking, "sloppy")
    descriptor = None
    for klass in project::Booking.__mro__:
        if "sloppy" in klass.__dict__:
            descriptor = klass.__dict__["sloppy"]
            break
    assert isinstance(descriptor, property)

def test_project::booking_has_overtime():
    assert hasattr(project::Booking, "overtime")
    descriptor = None
    for klass in project::Booking.__mro__:
        if "overtime" in klass.__dict__:
            descriptor = klass.__dict__["overtime"]
            break
    assert isinstance(descriptor, property)



def test_project::allocateresourceattribute_is_not_abstract():
    assert not inspect.isabstract(project::AllocateResourceAttribute)


def test_project::allocateresourceattribute_constructor_exists():
    assert callable(project::AllocateResourceAttribute.__init__)


def test_project::allocateresourceattribute_constructor_args():
    sig = inspect.signature(project::AllocateResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::allocateresource_is_not_abstract():
    assert not inspect.isabstract(project::AllocateResource)


def test_project::allocateresource_constructor_exists():
    assert callable(project::AllocateResource.__init__)


def test_project::allocateresource_constructor_args():
    sig = inspect.signature(project::AllocateResource.__init__)
    params = list(sig.parameters.keys())



def test_project::newtaskattribute_is_not_abstract():
    assert not inspect.isabstract(project::NewTaskAttribute)


def test_project::newtaskattribute_constructor_exists():
    assert callable(project::NewTaskAttribute.__init__)


def test_project::newtaskattribute_constructor_args():
    sig = inspect.signature(project::NewTaskAttribute.__init__)
    params = list(sig.parameters.keys())



def test_timesheetattribute_is_not_abstract():
    assert not inspect.isabstract(TimesheetAttribute)


def test_timesheetattribute_constructor_exists():
    assert callable(TimesheetAttribute.__init__)


def test_timesheetattribute_constructor_args():
    sig = inspect.signature(TimesheetAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::tasktimesheet_is_not_abstract():
    assert not inspect.isabstract(project::TaskTimesheet)


def test_project::tasktimesheet_constructor_exists():
    assert callable(project::TaskTimesheet.__init__)


def test_project::tasktimesheet_constructor_args():
    sig = inspect.signature(project::TaskTimesheet.__init__)
    params = list(sig.parameters.keys())



def test_project::shifttimesheet_is_not_abstract():
    assert not inspect.isabstract(project::ShiftTimesheet)


def test_project::shifttimesheet_constructor_exists():
    assert callable(project::ShiftTimesheet.__init__)


def test_project::shifttimesheet_constructor_args():
    sig = inspect.signature(project::ShiftTimesheet.__init__)
    params = list(sig.parameters.keys())



def test_project::statustimesheet_is_not_abstract():
    assert not inspect.isabstract(project::StatusTimesheet)


def test_project::statustimesheet_constructor_exists():
    assert callable(project::StatusTimesheet.__init__)


def test_project::statustimesheet_constructor_args():
    sig = inspect.signature(project::StatusTimesheet.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "level" in params, "Missing parameter 'level'"

def test_project::statustimesheet_has_text():
    assert hasattr(project::StatusTimesheet, "text")
    descriptor = None
    for klass in project::StatusTimesheet.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_project::statustimesheet_has_level():
    assert hasattr(project::StatusTimesheet, "level")
    descriptor = None
    for klass in project::StatusTimesheet.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_project::newtask_is_not_abstract():
    assert not inspect.isabstract(project::NewTask)


def test_project::newtask_constructor_exists():
    assert callable(project::NewTask.__init__)


def test_project::newtask_constructor_args():
    sig = inspect.signature(project::NewTask.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "id" in params, "Missing parameter 'id'"

def test_project::newtask_has_text():
    assert hasattr(project::NewTask, "text")
    descriptor = None
    for klass in project::NewTask.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_project::newtask_has_id():
    assert hasattr(project::NewTask, "id")
    descriptor = None
    for klass in project::NewTask.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_project::navigatorattribute_is_not_abstract():
    assert not inspect.isabstract(project::NavigatorAttribute)


def test_project::navigatorattribute_constructor_exists():
    assert callable(project::NavigatorAttribute.__init__)


def test_project::navigatorattribute_constructor_args():
    sig = inspect.signature(project::NavigatorAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::reportattribute_is_not_abstract():
    assert not inspect.isabstract(project::ReportAttribute)


def test_project::reportattribute_constructor_exists():
    assert callable(project::ReportAttribute.__init__)


def test_project::reportattribute_constructor_args():
    sig = inspect.signature(project::ReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::resourceattribute_is_not_abstract():
    assert not inspect.isabstract(project::ResourceAttribute)


def test_project::resourceattribute_constructor_exists():
    assert callable(project::ResourceAttribute.__init__)


def test_project::resourceattribute_constructor_args():
    sig = inspect.signature(project::ResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_resourceattribute_is_not_abstract():
    assert not inspect.isabstract(ResourceAttribute)


def test_resourceattribute_constructor_exists():
    assert callable(ResourceAttribute.__init__)


def test_resourceattribute_constructor_args():
    sig = inspect.signature(ResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::efficiency_is_not_abstract():
    assert not inspect.isabstract(project::Efficiency)


def test_project::efficiency_constructor_exists():
    assert callable(project::Efficiency.__init__)


def test_project::efficiency_constructor_args():
    sig = inspect.signature(project::Efficiency.__init__)
    params = list(sig.parameters.keys())
    assert "efficiency" in params, "Missing parameter 'efficiency'"

def test_project::efficiency_has_efficiency():
    assert hasattr(project::Efficiency, "efficiency")
    descriptor = None
    for klass in project::Efficiency.__mro__:
        if "efficiency" in klass.__dict__:
            descriptor = klass.__dict__["efficiency"]
            break
    assert isinstance(descriptor, property)



def test_project::purgeresource_is_not_abstract():
    assert not inspect.isabstract(project::PurgeResource)


def test_project::purgeresource_constructor_exists():
    assert callable(project::PurgeResource.__init__)


def test_project::purgeresource_constructor_args():
    sig = inspect.signature(project::PurgeResource.__init__)
    params = list(sig.parameters.keys())
    assert "listAttribute" in params, "Missing parameter 'listAttribute'"

def test_project::purgeresource_has_listAttribute():
    assert hasattr(project::PurgeResource, "listAttribute")
    descriptor = None
    for klass in project::PurgeResource.__mro__:
        if "listAttribute" in klass.__dict__:
            descriptor = klass.__dict__["listAttribute"]
            break
    assert isinstance(descriptor, property)



def test_project::workinghours_is_not_abstract():
    assert not inspect.isabstract(project::WorkingHours)


def test_project::workinghours_constructor_exists():
    assert callable(project::WorkingHours.__init__)


def test_project::workinghours_constructor_args():
    sig = inspect.signature(project::WorkingHours.__init__)
    params = list(sig.parameters.keys())
    assert "off" in params, "Missing parameter 'off'"

def test_project::workinghours_has_off():
    assert hasattr(project::WorkingHours, "off")
    descriptor = None
    for klass in project::WorkingHours.__mro__:
        if "off" in klass.__dict__:
            descriptor = klass.__dict__["off"]
            break
    assert isinstance(descriptor, property)



def test_project::shiftsresource_is_not_abstract():
    assert not inspect.isabstract(project::ShiftsResource)


def test_project::shiftsresource_constructor_exists():
    assert callable(project::ShiftsResource.__init__)


def test_project::shiftsresource_constructor_args():
    sig = inspect.signature(project::ShiftsResource.__init__)
    params = list(sig.parameters.keys())



def test_project::extendedresourceattribute_is_not_abstract():
    assert not inspect.isabstract(project::ExtendedResourceAttribute)


def test_project::extendedresourceattribute_constructor_exists():
    assert callable(project::ExtendedResourceAttribute.__init__)


def test_project::extendedresourceattribute_constructor_args():
    sig = inspect.signature(project::ExtendedResourceAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project::extendedresourceattribute_has_value():
    assert hasattr(project::ExtendedResourceAttribute, "value")
    descriptor = None
    for klass in project::ExtendedResourceAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project::bookingresource_is_not_abstract():
    assert not inspect.isabstract(project::BookingResource)


def test_project::bookingresource_constructor_exists():
    assert callable(project::BookingResource.__init__)


def test_project::bookingresource_constructor_args():
    sig = inspect.signature(project::BookingResource.__init__)
    params = list(sig.parameters.keys())



def test_project::email_is_not_abstract():
    assert not inspect.isabstract(project::Email)


def test_project::email_constructor_exists():
    assert callable(project::Email.__init__)


def test_project::email_constructor_args():
    sig = inspect.signature(project::Email.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_project::email_has_address():
    assert hasattr(project::Email, "address")
    descriptor = None
    for klass in project::Email.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_project::managers_is_not_abstract():
    assert not inspect.isabstract(project::Managers)


def test_project::managers_constructor_exists():
    assert callable(project::Managers.__init__)


def test_project::managers_constructor_args():
    sig = inspect.signature(project::Managers.__init__)
    params = list(sig.parameters.keys())



def test_project::exportattribute_is_not_abstract():
    assert not inspect.isabstract(project::ExportAttribute)


def test_project::exportattribute_constructor_exists():
    assert callable(project::ExportAttribute.__init__)


def test_project::exportattribute_constructor_args():
    sig = inspect.signature(project::ExportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::icalreportattribute_is_not_abstract():
    assert not inspect.isabstract(project::IcalReportAttribute)


def test_project::icalreportattribute_constructor_exists():
    assert callable(project::IcalReportAttribute.__init__)


def test_project::icalreportattribute_constructor_args():
    sig = inspect.signature(project::IcalReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_reportattribute_is_not_abstract():
    assert not inspect.isabstract(ReportAttribute)


def test_reportattribute_constructor_exists():
    assert callable(ReportAttribute.__init__)


def test_reportattribute_constructor_args():
    sig = inspect.signature(ReportAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::rolluptask_is_not_abstract():
    assert not inspect.isabstract(project::RollupTask)


def test_project::rolluptask_constructor_exists():
    assert callable(project::RollupTask.__init__)


def test_project::rolluptask_constructor_args():
    sig = inspect.signature(project::RollupTask.__init__)
    params = list(sig.parameters.keys())



def test_project::rollupresource_is_not_abstract():
    assert not inspect.isabstract(project::RollupResource)


def test_project::rollupresource_constructor_exists():
    assert callable(project::RollupResource.__init__)


def test_project::rollupresource_constructor_args():
    sig = inspect.signature(project::RollupResource.__init__)
    params = list(sig.parameters.keys())



def test_project::purgereport_is_not_abstract():
    assert not inspect.isabstract(project::PurgeReport)


def test_project::purgereport_constructor_exists():
    assert callable(project::PurgeReport.__init__)


def test_project::purgereport_constructor_args():
    sig = inspect.signature(project::PurgeReport.__init__)
    params = list(sig.parameters.keys())
    assert "listAttribute" in params, "Missing parameter 'listAttribute'"

def test_project::purgereport_has_listAttribute():
    assert hasattr(project::PurgeReport, "listAttribute")
    descriptor = None
    for klass in project::PurgeReport.__mro__:
        if "listAttribute" in klass.__dict__:
            descriptor = klass.__dict__["listAttribute"]
            break
    assert isinstance(descriptor, property)



def test_project::selfcontained_is_not_abstract():
    assert not inspect.isabstract(project::SelfContained)


def test_project::selfcontained_constructor_exists():
    assert callable(project::SelfContained.__init__)


def test_project::selfcontained_constructor_args():
    sig = inspect.signature(project::SelfContained.__init__)
    params = list(sig.parameters.keys())
    assert "selfcontained" in params, "Missing parameter 'selfcontained'"

def test_project::selfcontained_has_selfcontained():
    assert hasattr(project::SelfContained, "selfcontained")
    descriptor = None
    for klass in project::SelfContained.__mro__:
        if "selfcontained" in klass.__dict__:
            descriptor = klass.__dict__["selfcontained"]
            break
    assert isinstance(descriptor, property)



def test_project::scenarios_is_not_abstract():
    assert not inspect.isabstract(project::Scenarios)


def test_project::scenarios_constructor_exists():
    assert callable(project::Scenarios.__init__)


def test_project::scenarios_constructor_args():
    sig = inspect.signature(project::Scenarios.__init__)
    params = list(sig.parameters.keys())



def test_project::right_is_not_abstract():
    assert not inspect.isabstract(project::Right)


def test_project::right_constructor_exists():
    assert callable(project::Right.__init__)


def test_project::right_constructor_args():
    sig = inspect.signature(project::Right.__init__)
    params = list(sig.parameters.keys())



def test_project::journalmode_is_not_abstract():
    assert not inspect.isabstract(project::JournalMode)


def test_project::journalmode_constructor_exists():
    assert callable(project::JournalMode.__init__)


def test_project::journalmode_constructor_args():
    sig = inspect.signature(project::JournalMode.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_project::journalmode_has_mode():
    assert hasattr(project::JournalMode, "mode")
    descriptor = None
    for klass in project::JournalMode.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_project::center_is_not_abstract():
    assert not inspect.isabstract(project::Center)


def test_project::center_constructor_exists():
    assert callable(project::Center.__init__)


def test_project::center_constructor_args():
    sig = inspect.signature(project::Center.__init__)
    params = list(sig.parameters.keys())



def test_project::sortresources_is_not_abstract():
    assert not inspect.isabstract(project::SortResources)


def test_project::sortresources_constructor_exists():
    assert callable(project::SortResources.__init__)


def test_project::sortresources_constructor_args():
    sig = inspect.signature(project::SortResources.__init__)
    params = list(sig.parameters.keys())



def test_project::hideaccount_is_not_abstract():
    assert not inspect.isabstract(project::HideAccount)


def test_project::hideaccount_constructor_exists():
    assert callable(project::HideAccount.__init__)


def test_project::hideaccount_constructor_args():
    sig = inspect.signature(project::HideAccount.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_project::hideaccount_has_expression():
    assert hasattr(project::HideAccount, "expression")
    descriptor = None
    for klass in project::HideAccount.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_project::currencyformat_is_not_abstract():
    assert not inspect.isabstract(project::CurrencyFormat)


def test_project::currencyformat_constructor_exists():
    assert callable(project::CurrencyFormat.__init__)


def test_project::currencyformat_constructor_args():
    sig = inspect.signature(project::CurrencyFormat.__init__)
    params = list(sig.parameters.keys())



def test_project::loadunit_is_not_abstract():
    assert not inspect.isabstract(project::LoadUnit)


def test_project::loadunit_constructor_exists():
    assert callable(project::LoadUnit.__init__)


def test_project::loadunit_constructor_args():
    sig = inspect.signature(project::LoadUnit.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_project::loadunit_has_unit():
    assert hasattr(project::LoadUnit, "unit")
    descriptor = None
    for klass in project::LoadUnit.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_project::epilog_is_not_abstract():
    assert not inspect.isabstract(project::Epilog)


def test_project::epilog_constructor_exists():
    assert callable(project::Epilog.__init__)


def test_project::epilog_constructor_args():
    sig = inspect.signature(project::Epilog.__init__)
    params = list(sig.parameters.keys())



def test_project::left_is_not_abstract():
    assert not inspect.isabstract(project::Left)


def test_project::left_constructor_exists():
    assert callable(project::Left.__init__)


def test_project::left_constructor_args():
    sig = inspect.signature(project::Left.__init__)
    params = list(sig.parameters.keys())



def test_project::hidejournalentry_is_not_abstract():
    assert not inspect.isabstract(project::HideJournalEntry)


def test_project::hidejournalentry_constructor_exists():
    assert callable(project::HideJournalEntry.__init__)


def test_project::hidejournalentry_constructor_args():
    sig = inspect.signature(project::HideJournalEntry.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_project::hidejournalentry_has_expression():
    assert hasattr(project::HideJournalEntry, "expression")
    descriptor = None
    for klass in project::HideJournalEntry.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_project::resourceroot_is_not_abstract():
    assert not inspect.isabstract(project::ResourceRoot)


def test_project::resourceroot_constructor_exists():
    assert callable(project::ResourceRoot.__init__)


def test_project::resourceroot_constructor_args():
    sig = inspect.signature(project::ResourceRoot.__init__)
    params = list(sig.parameters.keys())



def test_project::timezone_is_not_abstract():
    assert not inspect.isabstract(project::Timezone)


def test_project::timezone_constructor_exists():
    assert callable(project::Timezone.__init__)


def test_project::timezone_constructor_args():
    sig = inspect.signature(project::Timezone.__init__)
    params = list(sig.parameters.keys())
    assert "timezone" in params, "Missing parameter 'timezone'"

def test_project::timezone_has_timezone():
    assert hasattr(project::Timezone, "timezone")
    descriptor = None
    for klass in project::Timezone.__mro__:
        if "timezone" in klass.__dict__:
            descriptor = klass.__dict__["timezone"]
            break
    assert isinstance(descriptor, property)



def test_project::caption_is_not_abstract():
    assert not inspect.isabstract(project::Caption)


def test_project::caption_constructor_exists():
    assert callable(project::Caption.__init__)


def test_project::caption_constructor_args():
    sig = inspect.signature(project::Caption.__init__)
    params = list(sig.parameters.keys())



def test_project::sortjournalentries_is_not_abstract():
    assert not inspect.isabstract(project::SortJournalEntries)


def test_project::sortjournalentries_constructor_exists():
    assert callable(project::SortJournalEntries.__init__)


def test_project::sortjournalentries_constructor_args():
    sig = inspect.signature(project::SortJournalEntries.__init__)
    params = list(sig.parameters.keys())



def test_project::hideresource_is_not_abstract():
    assert not inspect.isabstract(project::HideResource)


def test_project::hideresource_constructor_exists():
    assert callable(project::HideResource.__init__)


def test_project::hideresource_constructor_args():
    sig = inspect.signature(project::HideResource.__init__)
    params = list(sig.parameters.keys())



def test_project::formats_is_not_abstract():
    assert not inspect.isabstract(project::Formats)


def test_project::formats_constructor_exists():
    assert callable(project::Formats.__init__)


def test_project::formats_constructor_args():
    sig = inspect.signature(project::Formats.__init__)
    params = list(sig.parameters.keys())
    assert "formats" in params, "Missing parameter 'formats'"

def test_project::formats_has_formats():
    assert hasattr(project::Formats, "formats")
    descriptor = None
    for klass in project::Formats.__mro__:
        if "formats" in klass.__dict__:
            descriptor = klass.__dict__["formats"]
            break
    assert isinstance(descriptor, property)



def test_project::journalattributes_is_not_abstract():
    assert not inspect.isabstract(project::JournalAttributes)


def test_project::journalattributes_constructor_exists():
    assert callable(project::JournalAttributes.__init__)


def test_project::journalattributes_constructor_args():
    sig = inspect.signature(project::JournalAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "propertyid" in params, "Missing parameter 'propertyid'"
    assert "all" in params, "Missing parameter 'all'"
    assert "none" in params, "Missing parameter 'none'"
    assert "_property" in params, "Missing parameter '_property'"
    assert "summary" in params, "Missing parameter 'summary'"
    assert "details" in params, "Missing parameter 'details'"
    assert "author" in params, "Missing parameter 'author'"
    assert "headline" in params, "Missing parameter 'headline'"
    assert "timesheet" in params, "Missing parameter 'timesheet'"
    assert "date" in params, "Missing parameter 'date'"
    assert "flags" in params, "Missing parameter 'flags'"

def test_project::journalattributes_has_propertyid():
    assert hasattr(project::JournalAttributes, "propertyid")
    descriptor = None
    for klass in project::JournalAttributes.__mro__:
        if "propertyid" in klass.__dict__:
            descriptor = klass.__dict__["propertyid"]
            break
    assert isinstance(descriptor, property)

def test_project::journalattributes_has_all():
    assert hasattr(project::JournalAttributes, "all")
    descriptor = None
    for klass in project::JournalAttributes.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_project::journalattributes_has_none():
    assert hasattr(project::JournalAttributes, "none")
    descriptor = None
    for klass in project::JournalAttributes.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)

def test_project::journalattributes_has__property():
    assert hasattr(project::JournalAttributes, "_property")
    descriptor = None
    for klass in project::JournalAttributes.__mro__:
        if "_property" in klass.__dict__:
            descriptor = klass.__dict__["_property"]
            break
    assert isinstance(descriptor, property)

def test_project::journalattributes_has_summary():
    assert hasattr(project::JournalAttributes, "summary")
    descriptor = None
    for klass in project::JournalAttributes.__mro__:
        if "summary" in klass.__dict__:
            descriptor = klass.__dict__["summary"]
            break
    assert isinstance(descriptor, property)

def test_project::journalattributes_has_details():
    assert hasattr(project::JournalAttributes, "details")
    descriptor = None
    for klass in project::JournalAttributes.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)

def test_project::journalattributes_has_author():
    assert hasattr(project::JournalAttributes, "author")
    descriptor = None
    for klass in project::JournalAttributes.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_project::journalattributes_has_headline():
    assert hasattr(project::JournalAttributes, "headline")
    descriptor = None
    for klass in project::JournalAttributes.__mro__:
        if "headline" in klass.__dict__:
            descriptor = klass.__dict__["headline"]
            break
    assert isinstance(descriptor, property)

def test_project::journalattributes_has_timesheet():
    assert hasattr(project::JournalAttributes, "timesheet")
    descriptor = None
    for klass in project::JournalAttributes.__mro__:
        if "timesheet" in klass.__dict__:
            descriptor = klass.__dict__["timesheet"]
            break
    assert isinstance(descriptor, property)

def test_project::journalattributes_has_date():
    assert hasattr(project::JournalAttributes, "date")
    descriptor = None
    for klass in project::JournalAttributes.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_project::journalattributes_has_flags():
    assert hasattr(project::JournalAttributes, "flags")
    descriptor = None
    for klass in project::JournalAttributes.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)



def test_project::sorttasks_is_not_abstract():
    assert not inspect.isabstract(project::SortTasks)


def test_project::sorttasks_constructor_exists():
    assert callable(project::SortTasks.__init__)


def test_project::sorttasks_constructor_args():
    sig = inspect.signature(project::SortTasks.__init__)
    params = list(sig.parameters.keys())



def test_project::title_is_not_abstract():
    assert not inspect.isabstract(project::Title)


def test_project::title_constructor_exists():
    assert callable(project::Title.__init__)


def test_project::title_constructor_args():
    sig = inspect.signature(project::Title.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_project::title_has_title():
    assert hasattr(project::Title, "title")
    descriptor = None
    for klass in project::Title.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_project::numberformat_is_not_abstract():
    assert not inspect.isabstract(project::NumberFormat)


def test_project::numberformat_constructor_exists():
    assert callable(project::NumberFormat.__init__)


def test_project::numberformat_constructor_args():
    sig = inspect.signature(project::NumberFormat.__init__)
    params = list(sig.parameters.keys())



def test_project::accountroot_is_not_abstract():
    assert not inspect.isabstract(project::AccountRoot)


def test_project::accountroot_constructor_exists():
    assert callable(project::AccountRoot.__init__)


def test_project::accountroot_constructor_args():
    sig = inspect.signature(project::AccountRoot.__init__)
    params = list(sig.parameters.keys())



def test_project::rollupaccount_is_not_abstract():
    assert not inspect.isabstract(project::RollupAccount)


def test_project::rollupaccount_constructor_exists():
    assert callable(project::RollupAccount.__init__)


def test_project::rollupaccount_constructor_args():
    sig = inspect.signature(project::RollupAccount.__init__)
    params = list(sig.parameters.keys())



def test_project::hidetask_is_not_abstract():
    assert not inspect.isabstract(project::HideTask)


def test_project::hidetask_constructor_exists():
    assert callable(project::HideTask.__init__)


def test_project::hidetask_constructor_args():
    sig = inspect.signature(project::HideTask.__init__)
    params = list(sig.parameters.keys())



def test_project::header_is_not_abstract():
    assert not inspect.isabstract(project::Header)


def test_project::header_constructor_exists():
    assert callable(project::Header.__init__)


def test_project::header_constructor_args():
    sig = inspect.signature(project::Header.__init__)
    params = list(sig.parameters.keys())



def test_project::timeformat_is_not_abstract():
    assert not inspect.isabstract(project::TimeFormat)


def test_project::timeformat_constructor_exists():
    assert callable(project::TimeFormat.__init__)


def test_project::timeformat_constructor_args():
    sig = inspect.signature(project::TimeFormat.__init__)
    params = list(sig.parameters.keys())
    assert "timeformat" in params, "Missing parameter 'timeformat'"

def test_project::timeformat_has_timeformat():
    assert hasattr(project::TimeFormat, "timeformat")
    descriptor = None
    for klass in project::TimeFormat.__mro__:
        if "timeformat" in klass.__dict__:
            descriptor = klass.__dict__["timeformat"]
            break
    assert isinstance(descriptor, property)



def test_project::footer_is_not_abstract():
    assert not inspect.isabstract(project::Footer)


def test_project::footer_constructor_exists():
    assert callable(project::Footer.__init__)


def test_project::footer_constructor_args():
    sig = inspect.signature(project::Footer.__init__)
    params = list(sig.parameters.keys())



def test_project::taskroot_is_not_abstract():
    assert not inspect.isabstract(project::TaskRoot)


def test_project::taskroot_constructor_exists():
    assert callable(project::TaskRoot.__init__)


def test_project::taskroot_constructor_args():
    sig = inspect.signature(project::TaskRoot.__init__)
    params = list(sig.parameters.keys())



def test_project::headline_is_not_abstract():
    assert not inspect.isabstract(project::Headline)


def test_project::headline_constructor_exists():
    assert callable(project::Headline.__init__)


def test_project::headline_constructor_args():
    sig = inspect.signature(project::Headline.__init__)
    params = list(sig.parameters.keys())



def test_project::columns_is_not_abstract():
    assert not inspect.isabstract(project::Columns)


def test_project::columns_constructor_exists():
    assert callable(project::Columns.__init__)


def test_project::columns_constructor_args():
    sig = inspect.signature(project::Columns.__init__)
    params = list(sig.parameters.keys())



def test_project::sortaccounts_is_not_abstract():
    assert not inspect.isabstract(project::SortAccounts)


def test_project::sortaccounts_constructor_exists():
    assert callable(project::SortAccounts.__init__)


def test_project::sortaccounts_constructor_args():
    sig = inspect.signature(project::SortAccounts.__init__)
    params = list(sig.parameters.keys())



def test_project::prolog_is_not_abstract():
    assert not inspect.isabstract(project::Prolog)


def test_project::prolog_constructor_exists():
    assert callable(project::Prolog.__init__)


def test_project::prolog_constructor_args():
    sig = inspect.signature(project::Prolog.__init__)
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



def test_project::report_is_not_abstract():
    assert not inspect.isabstract(project::Report)


def test_project::report_constructor_exists():
    assert callable(project::Report.__init__)


def test_project::report_constructor_args():
    sig = inspect.signature(project::Report.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_project::report_has_id():
    assert hasattr(project::Report, "id")
    descriptor = None
    for klass in project::Report.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_project::report_has_name():
    assert hasattr(project::Report, "name")
    descriptor = None
    for klass in project::Report.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_project::taskattribute_is_not_abstract():
    assert not inspect.isabstract(project::TaskAttribute)


def test_project::taskattribute_constructor_exists():
    assert callable(project::TaskAttribute.__init__)


def test_project::taskattribute_constructor_args():
    sig = inspect.signature(project::TaskAttribute.__init__)
    params = list(sig.parameters.keys())



def test_taskattribute_is_not_abstract():
    assert not inspect.isabstract(TaskAttribute)


def test_taskattribute_constructor_exists():
    assert callable(TaskAttribute.__init__)


def test_taskattribute_constructor_args():
    sig = inspect.signature(TaskAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::note_is_not_abstract():
    assert not inspect.isabstract(project::Note)


def test_project::note_constructor_exists():
    assert callable(project::Note.__init__)


def test_project::note_constructor_args():
    sig = inspect.signature(project::Note.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"

def test_project::note_has_note():
    assert hasattr(project::Note, "note")
    descriptor = None
    for klass in project::Note.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_project::milestone_is_not_abstract():
    assert not inspect.isabstract(project::Milestone)


def test_project::milestone_constructor_exists():
    assert callable(project::Milestone.__init__)


def test_project::milestone_constructor_args():
    sig = inspect.signature(project::Milestone.__init__)
    params = list(sig.parameters.keys())
    assert "milestone" in params, "Missing parameter 'milestone'"

def test_project::milestone_has_milestone():
    assert hasattr(project::Milestone, "milestone")
    descriptor = None
    for klass in project::Milestone.__mro__:
        if "milestone" in klass.__dict__:
            descriptor = klass.__dict__["milestone"]
            break
    assert isinstance(descriptor, property)



def test_project::bookingtask_is_not_abstract():
    assert not inspect.isabstract(project::BookingTask)


def test_project::bookingtask_constructor_exists():
    assert callable(project::BookingTask.__init__)


def test_project::bookingtask_constructor_args():
    sig = inspect.signature(project::BookingTask.__init__)
    params = list(sig.parameters.keys())



def test_project::duration_is_not_abstract():
    assert not inspect.isabstract(project::Duration)


def test_project::duration_constructor_exists():
    assert callable(project::Duration.__init__)


def test_project::duration_constructor_args():
    sig = inspect.signature(project::Duration.__init__)
    params = list(sig.parameters.keys())



def test_project::depends_is_not_abstract():
    assert not inspect.isabstract(project::Depends)


def test_project::depends_constructor_exists():
    assert callable(project::Depends.__init__)


def test_project::depends_constructor_args():
    sig = inspect.signature(project::Depends.__init__)
    params = list(sig.parameters.keys())



def test_project::warn_is_not_abstract():
    assert not inspect.isabstract(project::Warn)


def test_project::warn_constructor_exists():
    assert callable(project::Warn.__init__)


def test_project::warn_constructor_args():
    sig = inspect.signature(project::Warn.__init__)
    params = list(sig.parameters.keys())



def test_project::scheduling_is_not_abstract():
    assert not inspect.isabstract(project::Scheduling)


def test_project::scheduling_constructor_exists():
    assert callable(project::Scheduling.__init__)


def test_project::scheduling_constructor_args():
    sig = inspect.signature(project::Scheduling.__init__)
    params = list(sig.parameters.keys())
    assert "scheduling" in params, "Missing parameter 'scheduling'"

def test_project::scheduling_has_scheduling():
    assert hasattr(project::Scheduling, "scheduling")
    descriptor = None
    for klass in project::Scheduling.__mro__:
        if "scheduling" in klass.__dict__:
            descriptor = klass.__dict__["scheduling"]
            break
    assert isinstance(descriptor, property)



def test_project::start_is_not_abstract():
    assert not inspect.isabstract(project::Start)


def test_project::start_constructor_exists():
    assert callable(project::Start.__init__)


def test_project::start_constructor_args():
    sig = inspect.signature(project::Start.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"

def test_project::start_has_start():
    assert hasattr(project::Start, "start")
    descriptor = None
    for klass in project::Start.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_project::projectid_is_not_abstract():
    assert not inspect.isabstract(project::ProjectId)


def test_project::projectid_constructor_exists():
    assert callable(project::ProjectId.__init__)


def test_project::projectid_constructor_args():
    sig = inspect.signature(project::ProjectId.__init__)
    params = list(sig.parameters.keys())
    assert "projectId" in params, "Missing parameter 'projectId'"

def test_project::projectid_has_projectId():
    assert hasattr(project::ProjectId, "projectId")
    descriptor = None
    for klass in project::ProjectId.__mro__:
        if "projectId" in klass.__dict__:
            descriptor = klass.__dict__["projectId"]
            break
    assert isinstance(descriptor, property)



def test_project::minstart_is_not_abstract():
    assert not inspect.isabstract(project::MinStart)


def test_project::minstart_constructor_exists():
    assert callable(project::MinStart.__init__)


def test_project::minstart_constructor_args():
    sig = inspect.signature(project::MinStart.__init__)
    params = list(sig.parameters.keys())
    assert "minStart" in params, "Missing parameter 'minStart'"

def test_project::minstart_has_minStart():
    assert hasattr(project::MinStart, "minStart")
    descriptor = None
    for klass in project::MinStart.__mro__:
        if "minStart" in klass.__dict__:
            descriptor = klass.__dict__["minStart"]
            break
    assert isinstance(descriptor, property)



def test_project::allocate_is_not_abstract():
    assert not inspect.isabstract(project::Allocate)


def test_project::allocate_constructor_exists():
    assert callable(project::Allocate.__init__)


def test_project::allocate_constructor_args():
    sig = inspect.signature(project::Allocate.__init__)
    params = list(sig.parameters.keys())



def test_project::complete_is_not_abstract():
    assert not inspect.isabstract(project::Complete)


def test_project::complete_constructor_exists():
    assert callable(project::Complete.__init__)


def test_project::complete_constructor_args():
    sig = inspect.signature(project::Complete.__init__)
    params = list(sig.parameters.keys())
    assert "complete" in params, "Missing parameter 'complete'"

def test_project::complete_has_complete():
    assert hasattr(project::Complete, "complete")
    descriptor = None
    for klass in project::Complete.__mro__:
        if "complete" in klass.__dict__:
            descriptor = klass.__dict__["complete"]
            break
    assert isinstance(descriptor, property)



def test_project::minend_is_not_abstract():
    assert not inspect.isabstract(project::MinEnd)


def test_project::minend_constructor_exists():
    assert callable(project::MinEnd.__init__)


def test_project::minend_constructor_args():
    sig = inspect.signature(project::MinEnd.__init__)
    params = list(sig.parameters.keys())
    assert "minEnd" in params, "Missing parameter 'minEnd'"

def test_project::minend_has_minEnd():
    assert hasattr(project::MinEnd, "minEnd")
    descriptor = None
    for klass in project::MinEnd.__mro__:
        if "minEnd" in klass.__dict__:
            descriptor = klass.__dict__["minEnd"]
            break
    assert isinstance(descriptor, property)



def test_project::maxend_is_not_abstract():
    assert not inspect.isabstract(project::MaxEnd)


def test_project::maxend_constructor_exists():
    assert callable(project::MaxEnd.__init__)


def test_project::maxend_constructor_args():
    sig = inspect.signature(project::MaxEnd.__init__)
    params = list(sig.parameters.keys())
    assert "maxEnd" in params, "Missing parameter 'maxEnd'"

def test_project::maxend_has_maxEnd():
    assert hasattr(project::MaxEnd, "maxEnd")
    descriptor = None
    for klass in project::MaxEnd.__mro__:
        if "maxEnd" in klass.__dict__:
            descriptor = klass.__dict__["maxEnd"]
            break
    assert isinstance(descriptor, property)



def test_project::length_is_not_abstract():
    assert not inspect.isabstract(project::Length)


def test_project::length_constructor_exists():
    assert callable(project::Length.__init__)


def test_project::length_constructor_args():
    sig = inspect.signature(project::Length.__init__)
    params = list(sig.parameters.keys())



def test_project::charge_is_not_abstract():
    assert not inspect.isabstract(project::Charge)


def test_project::charge_constructor_exists():
    assert callable(project::Charge.__init__)


def test_project::charge_constructor_args():
    sig = inspect.signature(project::Charge.__init__)
    params = list(sig.parameters.keys())
    assert "applies" in params, "Missing parameter 'applies'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_project::charge_has_applies():
    assert hasattr(project::Charge, "applies")
    descriptor = None
    for klass in project::Charge.__mro__:
        if "applies" in klass.__dict__:
            descriptor = klass.__dict__["applies"]
            break
    assert isinstance(descriptor, property)

def test_project::charge_has_amount():
    assert hasattr(project::Charge, "amount")
    descriptor = None
    for klass in project::Charge.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_project::journalentry_is_not_abstract():
    assert not inspect.isabstract(project::JournalEntry)


def test_project::journalentry_constructor_exists():
    assert callable(project::JournalEntry.__init__)


def test_project::journalentry_constructor_args():
    sig = inspect.signature(project::JournalEntry.__init__)
    params = list(sig.parameters.keys())
    assert "headline" in params, "Missing parameter 'headline'"
    assert "date" in params, "Missing parameter 'date'"

def test_project::journalentry_has_headline():
    assert hasattr(project::JournalEntry, "headline")
    descriptor = None
    for klass in project::JournalEntry.__mro__:
        if "headline" in klass.__dict__:
            descriptor = klass.__dict__["headline"]
            break
    assert isinstance(descriptor, property)

def test_project::journalentry_has_date():
    assert hasattr(project::JournalEntry, "date")
    descriptor = None
    for klass in project::JournalEntry.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_project::precedes_is_not_abstract():
    assert not inspect.isabstract(project::Precedes)


def test_project::precedes_constructor_exists():
    assert callable(project::Precedes.__init__)


def test_project::precedes_constructor_args():
    sig = inspect.signature(project::Precedes.__init__)
    params = list(sig.parameters.keys())



def test_project::purgetask_is_not_abstract():
    assert not inspect.isabstract(project::PurgeTask)


def test_project::purgetask_constructor_exists():
    assert callable(project::PurgeTask.__init__)


def test_project::purgetask_constructor_args():
    sig = inspect.signature(project::PurgeTask.__init__)
    params = list(sig.parameters.keys())
    assert "listAttribute" in params, "Missing parameter 'listAttribute'"

def test_project::purgetask_has_listAttribute():
    assert hasattr(project::PurgeTask, "listAttribute")
    descriptor = None
    for klass in project::PurgeTask.__mro__:
        if "listAttribute" in klass.__dict__:
            descriptor = klass.__dict__["listAttribute"]
            break
    assert isinstance(descriptor, property)



def test_project::priority_is_not_abstract():
    assert not inspect.isabstract(project::Priority)


def test_project::priority_constructor_exists():
    assert callable(project::Priority.__init__)


def test_project::priority_constructor_args():
    sig = inspect.signature(project::Priority.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_project::priority_has_priority():
    assert hasattr(project::Priority, "priority")
    descriptor = None
    for klass in project::Priority.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_project::responsible_is_not_abstract():
    assert not inspect.isabstract(project::Responsible)


def test_project::responsible_constructor_exists():
    assert callable(project::Responsible.__init__)


def test_project::responsible_constructor_args():
    sig = inspect.signature(project::Responsible.__init__)
    params = list(sig.parameters.keys())



def test_project::end_is_not_abstract():
    assert not inspect.isabstract(project::End)


def test_project::end_constructor_exists():
    assert callable(project::End.__init__)


def test_project::end_constructor_args():
    sig = inspect.signature(project::End.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"

def test_project::end_has_end():
    assert hasattr(project::End, "end")
    descriptor = None
    for klass in project::End.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_project::shiftstask_is_not_abstract():
    assert not inspect.isabstract(project::ShiftsTask)


def test_project::shiftstask_constructor_exists():
    assert callable(project::ShiftsTask.__init__)


def test_project::shiftstask_constructor_args():
    sig = inspect.signature(project::ShiftsTask.__init__)
    params = list(sig.parameters.keys())



def test_project::chargeset_is_not_abstract():
    assert not inspect.isabstract(project::ChargeSet)


def test_project::chargeset_constructor_exists():
    assert callable(project::ChargeSet.__init__)


def test_project::chargeset_constructor_args():
    sig = inspect.signature(project::ChargeSet.__init__)
    params = list(sig.parameters.keys())



def test_project::fail_is_not_abstract():
    assert not inspect.isabstract(project::Fail)


def test_project::fail_constructor_exists():
    assert callable(project::Fail.__init__)


def test_project::fail_constructor_args():
    sig = inspect.signature(project::Fail.__init__)
    params = list(sig.parameters.keys())



def test_project::scheduled_is_not_abstract():
    assert not inspect.isabstract(project::Scheduled)


def test_project::scheduled_constructor_exists():
    assert callable(project::Scheduled.__init__)


def test_project::scheduled_constructor_args():
    sig = inspect.signature(project::Scheduled.__init__)
    params = list(sig.parameters.keys())
    assert "scheduled" in params, "Missing parameter 'scheduled'"

def test_project::scheduled_has_scheduled():
    assert hasattr(project::Scheduled, "scheduled")
    descriptor = None
    for klass in project::Scheduled.__mro__:
        if "scheduled" in klass.__dict__:
            descriptor = klass.__dict__["scheduled"]
            break
    assert isinstance(descriptor, property)



def test_project::effort_is_not_abstract():
    assert not inspect.isabstract(project::Effort)


def test_project::effort_constructor_exists():
    assert callable(project::Effort.__init__)


def test_project::effort_constructor_args():
    sig = inspect.signature(project::Effort.__init__)
    params = list(sig.parameters.keys())



def test_project::extendedtaskattribute_is_not_abstract():
    assert not inspect.isabstract(project::ExtendedTaskAttribute)


def test_project::extendedtaskattribute_constructor_exists():
    assert callable(project::ExtendedTaskAttribute.__init__)


def test_project::extendedtaskattribute_constructor_args():
    sig = inspect.signature(project::ExtendedTaskAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project::extendedtaskattribute_has_value():
    assert hasattr(project::ExtendedTaskAttribute, "value")
    descriptor = None
    for klass in project::ExtendedTaskAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project::maxstart_is_not_abstract():
    assert not inspect.isabstract(project::MaxStart)


def test_project::maxstart_constructor_exists():
    assert callable(project::MaxStart.__init__)


def test_project::maxstart_constructor_args():
    sig = inspect.signature(project::MaxStart.__init__)
    params = list(sig.parameters.keys())
    assert "maxStart" in params, "Missing parameter 'maxStart'"

def test_project::maxstart_has_maxStart():
    assert hasattr(project::MaxStart, "maxStart")
    descriptor = None
    for klass in project::MaxStart.__mro__:
        if "maxStart" in klass.__dict__:
            descriptor = klass.__dict__["maxStart"]
            break
    assert isinstance(descriptor, property)



def test_project::endcredit_is_not_abstract():
    assert not inspect.isabstract(project::EndCredit)


def test_project::endcredit_constructor_exists():
    assert callable(project::EndCredit.__init__)


def test_project::endcredit_constructor_args():
    sig = inspect.signature(project::EndCredit.__init__)
    params = list(sig.parameters.keys())
    assert "credit" in params, "Missing parameter 'credit'"

def test_project::endcredit_has_credit():
    assert hasattr(project::EndCredit, "credit")
    descriptor = None
    for klass in project::EndCredit.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
            break
    assert isinstance(descriptor, property)



def test_project::period_is_not_abstract():
    assert not inspect.isabstract(project::Period)


def test_project::period_constructor_exists():
    assert callable(project::Period.__init__)


def test_project::period_constructor_args():
    sig = inspect.signature(project::Period.__init__)
    params = list(sig.parameters.keys())



def test_project::projectattribute_is_not_abstract():
    assert not inspect.isabstract(project::ProjectAttribute)


def test_project::projectattribute_constructor_exists():
    assert callable(project::ProjectAttribute.__init__)


def test_project::projectattribute_constructor_args():
    sig = inspect.signature(project::ProjectAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::interval2_is_not_abstract():
    assert not inspect.isabstract(project::Interval2)


def test_project::interval2_constructor_exists():
    assert callable(project::Interval2.__init__)


def test_project::interval2_constructor_args():
    sig = inspect.signature(project::Interval2.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"

def test_project::interval2_has_end():
    assert hasattr(project::Interval2, "end")
    descriptor = None
    for klass in project::Interval2.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_project::interval2_has_start():
    assert hasattr(project::Interval2, "start")
    descriptor = None
    for klass in project::Interval2.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_project::global_is_not_abstract():
    assert not inspect.isabstract(project::Global)


def test_project::global_constructor_exists():
    assert callable(project::Global.__init__)


def test_project::global_constructor_args():
    sig = inspect.signature(project::Global.__init__)
    params = list(sig.parameters.keys())



def test_includepropertiesattribute_is_not_abstract():
    assert not inspect.isabstract(IncludePropertiesAttribute)


def test_includepropertiesattribute_constructor_exists():
    assert callable(IncludePropertiesAttribute.__init__)


def test_includepropertiesattribute_constructor_args():
    sig = inspect.signature(IncludePropertiesAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::reportprefix_is_not_abstract():
    assert not inspect.isabstract(project::ReportPrefix)


def test_project::reportprefix_constructor_exists():
    assert callable(project::ReportPrefix.__init__)


def test_project::reportprefix_constructor_args():
    sig = inspect.signature(project::ReportPrefix.__init__)
    params = list(sig.parameters.keys())



def test_project::resourceprefix_is_not_abstract():
    assert not inspect.isabstract(project::ResourcePrefix)


def test_project::resourceprefix_constructor_exists():
    assert callable(project::ResourcePrefix.__init__)


def test_project::resourceprefix_constructor_args():
    sig = inspect.signature(project::ResourcePrefix.__init__)
    params = list(sig.parameters.keys())



def test_project::taskprefix_is_not_abstract():
    assert not inspect.isabstract(project::TaskPrefix)


def test_project::taskprefix_constructor_exists():
    assert callable(project::TaskPrefix.__init__)


def test_project::taskprefix_constructor_args():
    sig = inspect.signature(project::TaskPrefix.__init__)
    params = list(sig.parameters.keys())



def test_project::accountprefix_is_not_abstract():
    assert not inspect.isabstract(project::AccountPrefix)


def test_project::accountprefix_constructor_exists():
    assert callable(project::AccountPrefix.__init__)


def test_project::accountprefix_constructor_args():
    sig = inspect.signature(project::AccountPrefix.__init__)
    params = list(sig.parameters.keys())



def test_project::accountattribute_is_not_abstract():
    assert not inspect.isabstract(project::AccountAttribute)


def test_project::accountattribute_constructor_exists():
    assert callable(project::AccountAttribute.__init__)


def test_project::accountattribute_constructor_args():
    sig = inspect.signature(project::AccountAttribute.__init__)
    params = list(sig.parameters.keys())



def test_accountattribute_is_not_abstract():
    assert not inspect.isabstract(AccountAttribute)


def test_accountattribute_constructor_exists():
    assert callable(AccountAttribute.__init__)


def test_accountattribute_constructor_args():
    sig = inspect.signature(AccountAttribute.__init__)
    params = list(sig.parameters.keys())



def test_project::credit_is_not_abstract():
    assert not inspect.isabstract(project::Credit)


def test_project::credit_constructor_exists():
    assert callable(project::Credit.__init__)


def test_project::credit_constructor_args():
    sig = inspect.signature(project::Credit.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "description" in params, "Missing parameter 'description'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_project::credit_has_date():
    assert hasattr(project::Credit, "date")
    descriptor = None
    for klass in project::Credit.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_project::credit_has_description():
    assert hasattr(project::Credit, "description")
    descriptor = None
    for klass in project::Credit.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_project::credit_has_amount():
    assert hasattr(project::Credit, "amount")
    descriptor = None
    for klass in project::Credit.__mro__:
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



def test_project::includeproperties_is_not_abstract():
    assert not inspect.isabstract(project::IncludeProperties)


def test_project::includeproperties_constructor_exists():
    assert callable(project::IncludeProperties.__init__)


def test_project::includeproperties_constructor_args():
    sig = inspect.signature(project::IncludeProperties.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_project::includeproperties_has_importURI():
    assert hasattr(project::IncludeProperties, "importURI")
    descriptor = None
    for klass in project::IncludeProperties.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_project::export_is_not_abstract():
    assert not inspect.isabstract(project::Export)


def test_project::export_constructor_exists():
    assert callable(project::Export.__init__)


def test_project::export_constructor_args():
    sig = inspect.signature(project::Export.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"
    assert "id" in params, "Missing parameter 'id'"

def test_project::export_has_filename():
    assert hasattr(project::Export, "filename")
    descriptor = None
    for klass in project::Export.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_project::export_has_id():
    assert hasattr(project::Export, "id")
    descriptor = None
    for klass in project::Export.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_project::timesheetreport_is_not_abstract():
    assert not inspect.isabstract(project::TimesheetReport)


def test_project::timesheetreport_constructor_exists():
    assert callable(project::TimesheetReport.__init__)


def test_project::timesheetreport_constructor_args():
    sig = inspect.signature(project::TimesheetReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_project::timesheetreport_has_filename():
    assert hasattr(project::TimesheetReport, "filename")
    descriptor = None
    for klass in project::TimesheetReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_project::resource_is_not_abstract():
    assert not inspect.isabstract(project::Resource)


def test_project::resource_constructor_exists():
    assert callable(project::Resource.__init__)


def test_project::resource_constructor_args():
    sig = inspect.signature(project::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_project::resource_has_id():
    assert hasattr(project::Resource, "id")
    descriptor = None
    for klass in project::Resource.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_project::resource_has_name():
    assert hasattr(project::Resource, "name")
    descriptor = None
    for klass in project::Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_project::taskreport_is_not_abstract():
    assert not inspect.isabstract(project::TaskReport)


def test_project::taskreport_constructor_exists():
    assert callable(project::TaskReport.__init__)


def test_project::taskreport_constructor_args():
    sig = inspect.signature(project::TaskReport.__init__)
    params = list(sig.parameters.keys())



def test_project::rate_is_not_abstract():
    assert not inspect.isabstract(project::Rate)


def test_project::rate_constructor_exists():
    assert callable(project::Rate.__init__)


def test_project::rate_constructor_args():
    sig = inspect.signature(project::Rate.__init__)
    params = list(sig.parameters.keys())
    assert "rate" in params, "Missing parameter 'rate'"

def test_project::rate_has_rate():
    assert hasattr(project::Rate, "rate")
    descriptor = None
    for klass in project::Rate.__mro__:
        if "rate" in klass.__dict__:
            descriptor = klass.__dict__["rate"]
            break
    assert isinstance(descriptor, property)



def test_project::supplementaccount_is_not_abstract():
    assert not inspect.isabstract(project::SupplementAccount)


def test_project::supplementaccount_constructor_exists():
    assert callable(project::SupplementAccount.__init__)


def test_project::supplementaccount_constructor_args():
    sig = inspect.signature(project::SupplementAccount.__init__)
    params = list(sig.parameters.keys())



def test_project::nikureport_is_not_abstract():
    assert not inspect.isabstract(project::NikuReport)


def test_project::nikureport_constructor_exists():
    assert callable(project::NikuReport.__init__)


def test_project::nikureport_constructor_args():
    sig = inspect.signature(project::NikuReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_project::nikureport_has_filename():
    assert hasattr(project::NikuReport, "filename")
    descriptor = None
    for klass in project::NikuReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_project::macro_is_not_abstract():
    assert not inspect.isabstract(project::Macro)


def test_project::macro_constructor_exists():
    assert callable(project::Macro.__init__)


def test_project::macro_constructor_args():
    sig = inspect.signature(project::Macro.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_project::macro_has_value():
    assert hasattr(project::Macro, "value")
    descriptor = None
    for klass in project::Macro.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_project::tagfile_is_not_abstract():
    assert not inspect.isabstract(project::TagFile)


def test_project::tagfile_constructor_exists():
    assert callable(project::TagFile.__init__)


def test_project::tagfile_constructor_args():
    sig = inspect.signature(project::TagFile.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"
    assert "id" in params, "Missing parameter 'id'"

def test_project::tagfile_has_filename():
    assert hasattr(project::TagFile, "filename")
    descriptor = None
    for klass in project::TagFile.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_project::tagfile_has_id():
    assert hasattr(project::TagFile, "id")
    descriptor = None
    for klass in project::TagFile.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_project::statussheetreport_is_not_abstract():
    assert not inspect.isabstract(project::StatusSheetReport)


def test_project::statussheetreport_constructor_exists():
    assert callable(project::StatusSheetReport.__init__)


def test_project::statussheetreport_constructor_args():
    sig = inspect.signature(project::StatusSheetReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_project::statussheetreport_has_filename():
    assert hasattr(project::StatusSheetReport, "filename")
    descriptor = None
    for klass in project::StatusSheetReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_project::accountreport_is_not_abstract():
    assert not inspect.isabstract(project::AccountReport)


def test_project::accountreport_constructor_exists():
    assert callable(project::AccountReport.__init__)


def test_project::accountreport_constructor_args():
    sig = inspect.signature(project::AccountReport.__init__)
    params = list(sig.parameters.keys())



def test_project::textreport_is_not_abstract():
    assert not inspect.isabstract(project::TextReport)


def test_project::textreport_constructor_exists():
    assert callable(project::TextReport.__init__)


def test_project::textreport_constructor_args():
    sig = inspect.signature(project::TextReport.__init__)
    params = list(sig.parameters.keys())



def test_project::statussheet_is_not_abstract():
    assert not inspect.isabstract(project::StatusSheet)


def test_project::statussheet_constructor_exists():
    assert callable(project::StatusSheet.__init__)


def test_project::statussheet_constructor_args():
    sig = inspect.signature(project::StatusSheet.__init__)
    params = list(sig.parameters.keys())



def test_project::balance_is_not_abstract():
    assert not inspect.isabstract(project::Balance)


def test_project::balance_constructor_exists():
    assert callable(project::Balance.__init__)


def test_project::balance_constructor_args():
    sig = inspect.signature(project::Balance.__init__)
    params = list(sig.parameters.keys())



def test_project::navigator_is_not_abstract():
    assert not inspect.isabstract(project::Navigator)


def test_project::navigator_constructor_exists():
    assert callable(project::Navigator.__init__)


def test_project::navigator_constructor_args():
    sig = inspect.signature(project::Navigator.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_project::navigator_has_id():
    assert hasattr(project::Navigator, "id")
    descriptor = None
    for klass in project::Navigator.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_project::timesheet_is_not_abstract():
    assert not inspect.isabstract(project::Timesheet)


def test_project::timesheet_constructor_exists():
    assert callable(project::Timesheet.__init__)


def test_project::timesheet_constructor_args():
    sig = inspect.signature(project::Timesheet.__init__)
    params = list(sig.parameters.keys())



def test_project::shift_is_not_abstract():
    assert not inspect.isabstract(project::Shift)


def test_project::shift_constructor_exists():
    assert callable(project::Shift.__init__)


def test_project::shift_constructor_args():
    sig = inspect.signature(project::Shift.__init__)
    params = list(sig.parameters.keys())
    assert "timezone" in params, "Missing parameter 'timezone'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "replace" in params, "Missing parameter 'replace'"

def test_project::shift_has_timezone():
    assert hasattr(project::Shift, "timezone")
    descriptor = None
    for klass in project::Shift.__mro__:
        if "timezone" in klass.__dict__:
            descriptor = klass.__dict__["timezone"]
            break
    assert isinstance(descriptor, property)

def test_project::shift_has_id():
    assert hasattr(project::Shift, "id")
    descriptor = None
    for klass in project::Shift.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_project::shift_has_name():
    assert hasattr(project::Shift, "name")
    descriptor = None
    for klass in project::Shift.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project::shift_has_replace():
    assert hasattr(project::Shift, "replace")
    descriptor = None
    for klass in project::Shift.__mro__:
        if "replace" in klass.__dict__:
            descriptor = klass.__dict__["replace"]
            break
    assert isinstance(descriptor, property)



def test_project::supplementtask_is_not_abstract():
    assert not inspect.isabstract(project::SupplementTask)


def test_project::supplementtask_constructor_exists():
    assert callable(project::SupplementTask.__init__)


def test_project::supplementtask_constructor_args():
    sig = inspect.signature(project::SupplementTask.__init__)
    params = list(sig.parameters.keys())



def test_project::supplementresource_is_not_abstract():
    assert not inspect.isabstract(project::SupplementResource)


def test_project::supplementresource_constructor_exists():
    assert callable(project::SupplementResource.__init__)


def test_project::supplementresource_constructor_args():
    sig = inspect.signature(project::SupplementResource.__init__)
    params = list(sig.parameters.keys())



def test_project::resourcereport_is_not_abstract():
    assert not inspect.isabstract(project::ResourceReport)


def test_project::resourcereport_constructor_exists():
    assert callable(project::ResourceReport.__init__)


def test_project::resourcereport_constructor_args():
    sig = inspect.signature(project::ResourceReport.__init__)
    params = list(sig.parameters.keys())



def test_project::copyright_is_not_abstract():
    assert not inspect.isabstract(project::Copyright)


def test_project::copyright_constructor_exists():
    assert callable(project::Copyright.__init__)


def test_project::copyright_constructor_args():
    sig = inspect.signature(project::Copyright.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_project::copyright_has_text():
    assert hasattr(project::Copyright, "text")
    descriptor = None
    for klass in project::Copyright.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_project::task_is_not_abstract():
    assert not inspect.isabstract(project::Task)


def test_project::task_constructor_exists():
    assert callable(project::Task.__init__)


def test_project::task_constructor_args():
    sig = inspect.signature(project::Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_project::task_has_name():
    assert hasattr(project::Task, "name")
    descriptor = None
    for klass in project::Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project::task_has_id():
    assert hasattr(project::Task, "id")
    descriptor = None
    for klass in project::Task.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_project::icalreport_is_not_abstract():
    assert not inspect.isabstract(project::IcalReport)


def test_project::icalreport_constructor_exists():
    assert callable(project::IcalReport.__init__)


def test_project::icalreport_constructor_args():
    sig = inspect.signature(project::IcalReport.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_project::icalreport_has_filename():
    assert hasattr(project::IcalReport, "filename")
    descriptor = None
    for klass in project::IcalReport.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_project::flags_is_not_abstract():
    assert not inspect.isabstract(project::Flags)


def test_project::flags_constructor_exists():
    assert callable(project::Flags.__init__)


def test_project::flags_constructor_args():
    sig = inspect.signature(project::Flags.__init__)
    params = list(sig.parameters.keys())
    assert "flags" in params, "Missing parameter 'flags'"

def test_project::flags_has_flags():
    assert hasattr(project::Flags, "flags")
    descriptor = None
    for klass in project::Flags.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)



def test_project::vacation_is_not_abstract():
    assert not inspect.isabstract(project::Vacation)


def test_project::vacation_constructor_exists():
    assert callable(project::Vacation.__init__)


def test_project::vacation_constructor_args():
    sig = inspect.signature(project::Vacation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_project::vacation_has_name():
    assert hasattr(project::Vacation, "name")
    descriptor = None
    for klass in project::Vacation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_project::projectids_is_not_abstract():
    assert not inspect.isabstract(project::ProjectIds)


def test_project::projectids_constructor_exists():
    assert callable(project::ProjectIds.__init__)


def test_project::projectids_constructor_args():
    sig = inspect.signature(project::ProjectIds.__init__)
    params = list(sig.parameters.keys())
    assert "ids" in params, "Missing parameter 'ids'"

def test_project::projectids_has_ids():
    assert hasattr(project::ProjectIds, "ids")
    descriptor = None
    for klass in project::ProjectIds.__mro__:
        if "ids" in klass.__dict__:
            descriptor = klass.__dict__["ids"]
            break
    assert isinstance(descriptor, property)



def test_project::supplementreport_is_not_abstract():
    assert not inspect.isabstract(project::SupplementReport)


def test_project::supplementreport_constructor_exists():
    assert callable(project::SupplementReport.__init__)


def test_project::supplementreport_constructor_args():
    sig = inspect.signature(project::SupplementReport.__init__)
    params = list(sig.parameters.keys())



def test_project::limits_is_not_abstract():
    assert not inspect.isabstract(project::Limits)


def test_project::limits_constructor_exists():
    assert callable(project::Limits.__init__)


def test_project::limits_constructor_args():
    sig = inspect.signature(project::Limits.__init__)
    params = list(sig.parameters.keys())



def test_project::account_is_not_abstract():
    assert not inspect.isabstract(project::Account)


def test_project::account_constructor_exists():
    assert callable(project::Account.__init__)


def test_project::account_constructor_args():
    sig = inspect.signature(project::Account.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_project::account_has_name():
    assert hasattr(project::Account, "name")
    descriptor = None
    for klass in project::Account.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project::account_has_id():
    assert hasattr(project::Account, "id")
    descriptor = None
    for klass in project::Account.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_project::property_is_not_abstract():
    assert not inspect.isabstract(project::Property)


def test_project::property_constructor_exists():
    assert callable(project::Property.__init__)


def test_project::property_constructor_args():
    sig = inspect.signature(project::Property.__init__)
    params = list(sig.parameters.keys())



def test_project::project_is_not_abstract():
    assert not inspect.isabstract(project::Project)


def test_project::project_constructor_exists():
    assert callable(project::Project.__init__)


def test_project::project_constructor_args():
    sig = inspect.signature(project::Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "version" in params, "Missing parameter 'version'"

def test_project::project_has_name():
    assert hasattr(project::Project, "name")
    descriptor = None
    for klass in project::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_project::project_has_id():
    assert hasattr(project::Project, "id")
    descriptor = None
    for klass in project::Project.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_project::project_has_version():
    assert hasattr(project::Project, "version")
    descriptor = None
    for klass in project::Project.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

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

def test_journalentrysortcriterion_exists():
    # Check that the Enumeration exists
    assert JournalEntrySortCriterion is not None

def test_journalentrysortcriterion_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JournalEntrySortCriterion]
    expected_literals = [
        "ALERT_UP",
        "PROPERTY_UP",
        "DATE_DOWN",
        "DATE_UP",
        "ALERT_DOWN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JournalEntrySortCriterion"

def test_journalmodevalue_exists():
    # Check that the Enumeration exists
    assert JournalModeValue is not None

def test_journalmodevalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JournalModeValue]
    expected_literals = [
        "ALERTS_DOWN",
        "JOURNAL_SUB",
        "STATUS_DOWN",
        "STATUS_UP",
        "JOURNAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JournalModeValue"

def test_purgeresourceattribute_exists():
    # Check that the Enumeration exists
    assert PurgeResourceAttribute is not None

def test_purgeresourceattribute_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PurgeResourceAttribute]
    expected_literals = [
        "FAIL",
        "REPORTS",
        "WARN",
        "FLAGS",
        "VACATIONS",
        "MANAGERS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PurgeResourceAttribute"

def test_weekday_exists():
    # Check that the Enumeration exists
    assert Weekday is not None

def test_weekday_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Weekday]
    expected_literals = [
        "MON",
        "THR",
        "FRI",
        "SAT",
        "SUN",
        "WED",
        "TUE",
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
        "MONTH",
        "WEEK",
        "QUARTER",
        "HOUR",
        "DAY",
        "YEAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScaleResolution"

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

def test_reportformat_exists():
    # Check that the Enumeration exists
    assert ReportFormat is not None

def test_reportformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReportFormat]
    expected_literals = [
        "NIKU",
        "CSV",
        "HTML",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReportFormat"

def test_workquantityunit_exists():
    # Check that the Enumeration exists
    assert WorkQuantityUnit is not None

def test_workquantityunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkQuantityUnit]
    expected_literals = [
        "DAYS",
        "PERCENT",
        "HOURS",
        "MINUTES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkQuantityUnit"

def test_alertlevel_exists():
    # Check that the Enumeration exists
    assert AlertLevel is not None

def test_alertlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlertLevel]
    expected_literals = [
        "YELLOW",
        "RED",
        "GREEN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlertLevel"

def test_loaddisplayunit_exists():
    # Check that the Enumeration exists
    assert LoadDisplayUnit is not None

def test_loaddisplayunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LoadDisplayUnit]
    expected_literals = [
        "LONGAUTO",
        "MONTHS",
        "YEARS",
        "SHORTAUTO",
        "WEEKS",
        "DAYS",
        "MINUTES",
        "HOURS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LoadDisplayUnit"

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
        "RESPONSIBLE",
        "HIERARCHINDEX",
        "CHART",
        "HEADCOUNT",
        "FREEWORK",
        "REVENUE",
        "MINSTART",
        "END",
        "SCENARIO",
        "TARGETS",
        "EFFORTLEFT",
        "EFFICIENCY",
        "EFFORTDONE",
        "START",
        "FREETIME",
        "HOURLY",
        "ALERTSUMMARY",
        "MONTHLY",
        "QUARTERLY",
        "INDEX",
        "RATE",
        "RESOURCES",
        "FLAGS",
        "DAILY",
        "SEQNO",
        "EMAIL",
        "DURATION",
        "NOTE",
        "WBS",
        "FOLLOWERS",
        "PRIORITY",
        "WEEKLY",
        "PATHCRITICALNESS",
        "MINEND",
        "STATUS",
        "LINE",
        "COST",
        "COMPLETE",
        "ALERTTREND",
        "FTE",
        "DUTIES",
        "COMPLETED",
        "YEARLY",
        "ALERTMESSAGE",
        "EFFORT",
        "NAME",
        "MAXEND",
        "ALERT",
        "ID",
        "JOURNAL",
        "CRITICALNESS",
        "NO",
        "PRECURSOR",
        "MAXSTART",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColumnId"

def test_selectargument_exists():
    # Check that the Enumeration exists
    assert SelectArgument is not None

def test_selectargument_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SelectArgument]
    expected_literals = [
        "ORDER",
        "MINLOADED",
        "MAXLOADED",
        "MINALLOCATED",
        "RANDOM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SelectArgument"

def test_purgetaskattribute_exists():
    # Check that the Enumeration exists
    assert PurgeTaskAttribute is not None

def test_purgetaskattribute_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PurgeTaskAttribute]
    expected_literals = [
        "WARN",
        "DEPENDS",
        "CHARGESET",
        "BOOKING",
        "PRECEDES",
        "CHARGE",
        "FAIL",
        "FLAGS",
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
        "JOURNALATTRIBUTES",
        "DEFINITIONS",
        "FORMATS",
        "SORTRESOURCES",
        "SCENARIOS",
        "SORTTASKS",
        "COLUMNS",
        "FLAGS",
        "SORTACCOUNTS",
        "SORTJOURNALENTRIES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PurgeReportAttribute"

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

def test_justification_exists():
    # Check that the Enumeration exists
    assert Justification is not None

def test_justification_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Justification]
    expected_literals = [
        "LEFT",
        "RIGHT",
        "CENTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Justification"

def test_chargeapplies_exists():
    # Check that the Enumeration exists
    assert ChargeApplies is not None

def test_chargeapplies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ChargeApplies]
    expected_literals = [
        "ONEND",
        "ONSTART",
        "PERHOUR",
        "PERWEEK",
        "PERDAY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ChargeApplies"

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "MINUTE",
        "HOUR",
        "DAY",
        "YEAR",
        "MONTH",
        "WEEK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnit"


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
project::JvmIdentifiableElement_strategy = st.builds(
    project::JvmIdentifiableElement,
)
LogicalExpression_strategy = st.builds(
    LogicalExpression,
)
project::LogicalNumeralLiteral_strategy = st.builds(
    project::LogicalNumeralLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project::LogicalFunctionExpression_strategy = st.builds(
    project::LogicalFunctionExpression,
)
project::LogicalAbsoluteIdExression_strategy = st.builds(
    project::LogicalAbsoluteIdExression,
    value=
        safe_text
)
project::LogicalDateLiteral_strategy = st.builds(
    project::LogicalDateLiteral,
    value=
        safe_text
)
project::LogicalBooleanLiteral_strategy = st.builds(
    project::LogicalBooleanLiteral,
    isTrue=
        st.booleans()
)
project::LogicalStringLiteral_strategy = st.builds(
    project::LogicalStringLiteral,
    value=
        safe_text
)
project::XBinaryOperation_strategy = st.builds(
    project::XBinaryOperation,
)
Definitions_strategy = st.builds(
    Definitions,
)
project::Defintions_strategy = st.builds(
    project::Defintions,
    flags=
        st.booleans(),
    project=
        st.booleans(),
    tasks=
        st.booleans(),
    projectids=
        st.booleans(),
    resources=
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
project::RichText_strategy = st.builds(
    project::RichText,
    text=
        safe_text
)
Precedes_strategy = st.builds(
    Precedes,
)
Depends_strategy = st.builds(
    Depends,
)
project::TaskDependency_strategy = st.builds(
    project::TaskDependency,
    policy=
        safe_text
)
NumberFormat_strategy = st.builds(
    NumberFormat,
)
CurrencyFormat_strategy = st.builds(
    CurrencyFormat,
)
project::RealFormat_strategy = st.builds(
    project::RealFormat,
    negativeSuffix=
        safe_text,
    fractionSeparator=
        safe_text,
    negativePrefix=
        safe_text,
    fractionDigits=
        st.integers(),
    thousandsSeparator=
        safe_text
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
GapLength_strategy = st.builds(
    GapLength,
)
GapDuration_strategy = st.builds(
    GapDuration,
)
project::LimitAttribute_strategy = st.builds(
    project::LimitAttribute,
    end=
        safe_text,
    start=
        safe_text
)
WeeklyMin_strategy = st.builds(
    WeeklyMin,
)
project::Limit_strategy = st.builds(
    project::Limit,
)
project::ColumnAttribute_strategy = st.builds(
    project::ColumnAttribute,
)
project::WorkHours_strategy = st.builds(
    project::WorkHours,
    start=
        safe_text,
    stop=
        safe_text
)
project::Weekdays_strategy = st.builds(
    project::Weekdays,
    first=
        safe_text,
    last=
        safe_text
)
project::TreeLevel_strategy = st.builds(
    project::TreeLevel,
    level=
        safe_text
)
project::TimesheetReportAttribute_strategy = st.builds(
    project::TimesheetReportAttribute,
)
project::TimesheetAttribute_strategy = st.builds(
    project::TimesheetAttribute,
)
StatusSheetAttribute_strategy = st.builds(
    StatusSheetAttribute,
)
project::TaskTimesheetAttribute_strategy = st.builds(
    project::TaskTimesheetAttribute,
)
project::TaskStatusSheetAttribute_strategy = st.builds(
    project::TaskStatusSheetAttribute,
)
project::StatusSheetReportAttribute_strategy = st.builds(
    project::StatusSheetReportAttribute,
)
project::StatusSheetAttribute_strategy = st.builds(
    project::StatusSheetAttribute,
)
project::StatusTimesheetAttribute_strategy = st.builds(
    project::StatusTimesheetAttribute,
)
project::Criterion_strategy = st.builds(
    project::Criterion,
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
project::Sort_strategy = st.builds(
    project::Sort,
    tree=
        st.booleans()
)
project::StatusStatusSheetAttribute_strategy = st.builds(
    project::StatusStatusSheetAttribute,
)
TaskStatusSheetAttribute_strategy = st.builds(
    TaskStatusSheetAttribute,
)
project::TaskStatusSheet_strategy = st.builds(
    project::TaskStatusSheet,
)
project::StatusStatusSheet_strategy = st.builds(
    project::StatusStatusSheet,
    text=
        safe_text,
    level=
        safe_text
)
project::ShiftsLimit_strategy = st.builds(
    project::ShiftsLimit,
)
ShiftsTask_strategy = st.builds(
    ShiftsTask,
)
ShiftsResource_strategy = st.builds(
    ShiftsResource,
)
project::Shifts_strategy = st.builds(
    project::Shifts,
)
project::LimitsAttribute_strategy = st.builds(
    project::LimitsAttribute,
)
project::Interval3_strategy = st.builds(
    project::Interval3,
    start=
        safe_text,
    end=
        safe_text
)
project::Interval1_strategy = st.builds(
    project::Interval1,
    start=
        safe_text,
    end=
        safe_text
)
project::IncludePropertiesAttribute_strategy = st.builds(
    project::IncludePropertiesAttribute,
)
project::Function_strategy = st.builds(
    project::Function,
    parentId=
        safe_text,
    level=
        st.integers(),
    date=
        safe_text,
    distance=
        st.integers()
)
NavigatorAttribute_strategy = st.builds(
    NavigatorAttribute,
)
project::HideReport_strategy = st.builds(
    project::HideReport,
)
project::GapLength_strategy = st.builds(
    project::GapLength,
)
project::GapDuration_strategy = st.builds(
    project::GapDuration,
)
project::Extend_strategy = st.builds(
    project::Extend,
    name=
        safe_text,
    scenariospecific=
        st.booleans(),
    id=
        safe_text,
    inherit=
        st.booleans()
)
ExportAttribute_strategy = st.builds(
    ExportAttribute,
)
project::TaskAttributes_strategy = st.builds(
    project::TaskAttributes,
    flags=
        st.booleans(),
    maxstart=
        st.booleans(),
    booking=
        st.booleans(),
    note=
        st.booleans(),
    priority=
        st.booleans(),
    complete=
        st.booleans(),
    none=
        st.booleans(),
    maxend=
        st.booleans(),
    minstart=
        st.booleans(),
    all=
        st.booleans(),
    minend=
        st.booleans(),
    depends=
        st.booleans(),
    responsible=
        st.booleans()
)
project::ResourceAttributes_strategy = st.builds(
    project::ResourceAttributes,
    none=
        st.booleans(),
    booking=
        st.booleans(),
    workingHours=
        st.booleans(),
    vacation=
        st.booleans(),
    all=
        st.booleans()
)
project::Definitions_strategy = st.builds(
    project::Definitions,
    none=
        st.booleans(),
    all=
        st.booleans()
)
LimitsAttribute_strategy = st.builds(
    LimitsAttribute,
)
project::WeeklyMin_strategy = st.builds(
    project::WeeklyMin,
)
project::Maximum_strategy = st.builds(
    project::Maximum,
)
project::MonthlyMax_strategy = st.builds(
    project::MonthlyMax,
)
project::WeeklyMax_strategy = st.builds(
    project::WeeklyMax,
)
project::Minimum_strategy = st.builds(
    project::Minimum,
)
project::DailyMin_strategy = st.builds(
    project::DailyMin,
)
project::MonthlyMin_strategy = st.builds(
    project::MonthlyMin,
)
project::DailyMax_strategy = st.builds(
    project::DailyMax,
)
ProjectAttribute_strategy = st.builds(
    ProjectAttribute,
)
project::TimingResolution_strategy = st.builds(
    project::TimingResolution,
    timingResolution=
        st.integers()
)
project::ExtendResource_strategy = st.builds(
    project::ExtendResource,
)
project::ExtendTask_strategy = st.builds(
    project::ExtendTask,
)
project::DailyWorkingHours_strategy = st.builds(
    project::DailyWorkingHours,
    dailyWorkingHours=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project::ShortTimeFormat_strategy = st.builds(
    project::ShortTimeFormat,
    shortTimeFormat=
        safe_text
)
project::WeekStarts_strategy = st.builds(
    project::WeekStarts,
    sunday=
        st.booleans(),
    monday=
        st.booleans()
)
project::Scenario_strategy = st.builds(
    project::Scenario,
    name=
        safe_text,
    active=
        safe_text,
    id=
        safe_text
)
project::Include_strategy = st.builds(
    project::Include,
    importURI=
        safe_text
)
project::TrackingScenario_strategy = st.builds(
    project::TrackingScenario,
)
project::Now_strategy = st.builds(
    project::Now,
    now=
        safe_text
)
project::YearlyWorkingDays_strategy = st.builds(
    project::YearlyWorkingDays,
    yearlyWorkingDays=
        st.integers()
)
project::Currency_strategy = st.builds(
    project::Currency,
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
project::Timeoff_strategy = st.builds(
    project::Timeoff,
    name=
        safe_text,
    id=
        safe_text
)
NewTaskAttribute_strategy = st.builds(
    NewTaskAttribute,
)
project::Remaining_strategy = st.builds(
    project::Remaining,
)
project::Work_strategy = st.builds(
    project::Work,
    unit=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
IcalReportAttribute_strategy = st.builds(
    IcalReportAttribute,
)
project::ScenarioIcal_strategy = st.builds(
    project::ScenarioIcal,
)
project::DurationQuantity_strategy = st.builds(
    project::DurationQuantity,
    unit=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
StatusTimesheetAttribute_strategy = st.builds(
    StatusTimesheetAttribute,
)
project::RGB_strategy = st.builds(
    project::RGB,
    value=
        safe_text
)
project::LogicalExpression_strategy = st.builds(
    project::LogicalExpression,
)
ColumnAttribute_strategy = st.builds(
    ColumnAttribute,
)
project::ToolTip_strategy = st.builds(
    project::ToolTip,
    tip=
        safe_text
)
project::ListItem_strategy = st.builds(
    project::ListItem,
)
project::FontColor_strategy = st.builds(
    project::FontColor,
    color=
        safe_text
)
project::Scale_strategy = st.builds(
    project::Scale,
    scale=
        safe_text
)
project::HAlign_strategy = st.builds(
    project::HAlign,
    justification=
        safe_text
)
project::ListType_strategy = st.builds(
    project::ListType,
    type=
        safe_text
)
project::Width_strategy = st.builds(
    project::Width,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project::CellText_strategy = st.builds(
    project::CellText,
    text=
        safe_text
)
project::CellColor_strategy = st.builds(
    project::CellColor,
)
project::Column_strategy = st.builds(
    project::Column,
    id=
        safe_text
)
project::AccountShare_strategy = st.builds(
    project::AccountShare,
    share=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
StatusStatusSheetAttribute_strategy = st.builds(
    StatusStatusSheetAttribute,
)
project::Details_strategy = st.builds(
    project::Details,
)
project::Summary_strategy = st.builds(
    project::Summary,
)
project::Author_strategy = st.builds(
    project::Author,
)
AllocateResourceAttribute_strategy = st.builds(
    AllocateResourceAttribute,
)
project::Select_strategy = st.builds(
    project::Select,
    argument=
        safe_text
)
project::ShiftsAllocate_strategy = st.builds(
    project::ShiftsAllocate,
)
project::Persistent_strategy = st.builds(
    project::Persistent,
    persistent=
        st.booleans()
)
project::Mandatory_strategy = st.builds(
    project::Mandatory,
    mandatory=
        st.booleans()
)
project::Alternative_strategy = st.builds(
    project::Alternative,
)
project::Alert_strategy = st.builds(
    project::Alert,
    level=
        safe_text
)
project::NikuReportAttribute_strategy = st.builds(
    project::NikuReportAttribute,
)
project::Interval4_strategy = st.builds(
    project::Interval4,
    end=
        safe_text,
    start=
        safe_text
)
project::Booking_strategy = st.builds(
    project::Booking,
    sloppy=
        st.integers(),
    overtime=
        st.integers()
)
project::AllocateResourceAttribute_strategy = st.builds(
    project::AllocateResourceAttribute,
)
project::AllocateResource_strategy = st.builds(
    project::AllocateResource,
)
project::NewTaskAttribute_strategy = st.builds(
    project::NewTaskAttribute,
)
TimesheetAttribute_strategy = st.builds(
    TimesheetAttribute,
)
project::TaskTimesheet_strategy = st.builds(
    project::TaskTimesheet,
)
project::ShiftTimesheet_strategy = st.builds(
    project::ShiftTimesheet,
)
project::StatusTimesheet_strategy = st.builds(
    project::StatusTimesheet,
    text=
        safe_text,
    level=
        safe_text
)
project::NewTask_strategy = st.builds(
    project::NewTask,
    text=
        safe_text,
    id=
        safe_text
)
project::NavigatorAttribute_strategy = st.builds(
    project::NavigatorAttribute,
)
project::ReportAttribute_strategy = st.builds(
    project::ReportAttribute,
)
project::ResourceAttribute_strategy = st.builds(
    project::ResourceAttribute,
)
ResourceAttribute_strategy = st.builds(
    ResourceAttribute,
)
project::Efficiency_strategy = st.builds(
    project::Efficiency,
    efficiency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project::PurgeResource_strategy = st.builds(
    project::PurgeResource,
    listAttribute=
        safe_text
)
project::WorkingHours_strategy = st.builds(
    project::WorkingHours,
    off=
        st.booleans()
)
project::ShiftsResource_strategy = st.builds(
    project::ShiftsResource,
)
project::ExtendedResourceAttribute_strategy = st.builds(
    project::ExtendedResourceAttribute,
    value=
        safe_text
)
project::BookingResource_strategy = st.builds(
    project::BookingResource,
)
project::Email_strategy = st.builds(
    project::Email,
    address=
        safe_text
)
project::Managers_strategy = st.builds(
    project::Managers,
)
project::ExportAttribute_strategy = st.builds(
    project::ExportAttribute,
)
project::IcalReportAttribute_strategy = st.builds(
    project::IcalReportAttribute,
)
ReportAttribute_strategy = st.builds(
    ReportAttribute,
)
project::RollupTask_strategy = st.builds(
    project::RollupTask,
)
project::RollupResource_strategy = st.builds(
    project::RollupResource,
)
project::PurgeReport_strategy = st.builds(
    project::PurgeReport,
    listAttribute=
        safe_text
)
project::SelfContained_strategy = st.builds(
    project::SelfContained,
    selfcontained=
        safe_text
)
project::Scenarios_strategy = st.builds(
    project::Scenarios,
)
project::Right_strategy = st.builds(
    project::Right,
)
project::JournalMode_strategy = st.builds(
    project::JournalMode,
    mode=
        safe_text
)
project::Center_strategy = st.builds(
    project::Center,
)
project::SortResources_strategy = st.builds(
    project::SortResources,
)
project::HideAccount_strategy = st.builds(
    project::HideAccount,
    expression=
        safe_text
)
project::CurrencyFormat_strategy = st.builds(
    project::CurrencyFormat,
)
project::LoadUnit_strategy = st.builds(
    project::LoadUnit,
    unit=
        safe_text
)
project::Epilog_strategy = st.builds(
    project::Epilog,
)
project::Left_strategy = st.builds(
    project::Left,
)
project::HideJournalEntry_strategy = st.builds(
    project::HideJournalEntry,
    expression=
        safe_text
)
project::ResourceRoot_strategy = st.builds(
    project::ResourceRoot,
)
project::Timezone_strategy = st.builds(
    project::Timezone,
    timezone=
        safe_text
)
project::Caption_strategy = st.builds(
    project::Caption,
)
project::SortJournalEntries_strategy = st.builds(
    project::SortJournalEntries,
)
project::HideResource_strategy = st.builds(
    project::HideResource,
)
project::Formats_strategy = st.builds(
    project::Formats,
    formats=
        safe_text
)
project::JournalAttributes_strategy = st.builds(
    project::JournalAttributes,
    propertyid=
        st.booleans(),
    all=
        st.booleans(),
    none=
        st.booleans(),
    _property=
        st.booleans(),
    summary=
        st.booleans(),
    details=
        st.booleans(),
    author=
        st.booleans(),
    headline=
        st.booleans(),
    timesheet=
        st.booleans(),
    date=
        st.booleans(),
    flags=
        st.booleans()
)
project::SortTasks_strategy = st.builds(
    project::SortTasks,
)
project::Title_strategy = st.builds(
    project::Title,
    title=
        safe_text
)
project::NumberFormat_strategy = st.builds(
    project::NumberFormat,
)
project::AccountRoot_strategy = st.builds(
    project::AccountRoot,
)
project::RollupAccount_strategy = st.builds(
    project::RollupAccount,
)
project::HideTask_strategy = st.builds(
    project::HideTask,
)
project::Header_strategy = st.builds(
    project::Header,
)
project::TimeFormat_strategy = st.builds(
    project::TimeFormat,
    timeformat=
        safe_text
)
project::Footer_strategy = st.builds(
    project::Footer,
)
project::TaskRoot_strategy = st.builds(
    project::TaskRoot,
)
project::Headline_strategy = st.builds(
    project::Headline,
)
project::Columns_strategy = st.builds(
    project::Columns,
)
project::SortAccounts_strategy = st.builds(
    project::SortAccounts,
)
project::Prolog_strategy = st.builds(
    project::Prolog,
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
project::Report_strategy = st.builds(
    project::Report,
    id=
        safe_text,
    name=
        safe_text
)
project::TaskAttribute_strategy = st.builds(
    project::TaskAttribute,
)
TaskAttribute_strategy = st.builds(
    TaskAttribute,
)
project::Note_strategy = st.builds(
    project::Note,
    note=
        safe_text
)
project::Milestone_strategy = st.builds(
    project::Milestone,
    milestone=
        st.booleans()
)
project::BookingTask_strategy = st.builds(
    project::BookingTask,
)
project::Duration_strategy = st.builds(
    project::Duration,
)
project::Depends_strategy = st.builds(
    project::Depends,
)
project::Warn_strategy = st.builds(
    project::Warn,
)
project::Scheduling_strategy = st.builds(
    project::Scheduling,
    scheduling=
        safe_text
)
project::Start_strategy = st.builds(
    project::Start,
    start=
        safe_text
)
project::ProjectId_strategy = st.builds(
    project::ProjectId,
    projectId=
        safe_text
)
project::MinStart_strategy = st.builds(
    project::MinStart,
    minStart=
        safe_text
)
project::Allocate_strategy = st.builds(
    project::Allocate,
)
project::Complete_strategy = st.builds(
    project::Complete,
    complete=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project::MinEnd_strategy = st.builds(
    project::MinEnd,
    minEnd=
        safe_text
)
project::MaxEnd_strategy = st.builds(
    project::MaxEnd,
    maxEnd=
        safe_text
)
project::Length_strategy = st.builds(
    project::Length,
)
project::Charge_strategy = st.builds(
    project::Charge,
    applies=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project::JournalEntry_strategy = st.builds(
    project::JournalEntry,
    headline=
        safe_text,
    date=
        safe_text
)
project::Precedes_strategy = st.builds(
    project::Precedes,
)
project::PurgeTask_strategy = st.builds(
    project::PurgeTask,
    listAttribute=
        safe_text
)
project::Priority_strategy = st.builds(
    project::Priority,
    priority=
        st.integers()
)
project::Responsible_strategy = st.builds(
    project::Responsible,
)
project::End_strategy = st.builds(
    project::End,
    end=
        safe_text
)
project::ShiftsTask_strategy = st.builds(
    project::ShiftsTask,
)
project::ChargeSet_strategy = st.builds(
    project::ChargeSet,
)
project::Fail_strategy = st.builds(
    project::Fail,
)
project::Scheduled_strategy = st.builds(
    project::Scheduled,
    scheduled=
        st.booleans()
)
project::Effort_strategy = st.builds(
    project::Effort,
)
project::ExtendedTaskAttribute_strategy = st.builds(
    project::ExtendedTaskAttribute,
    value=
        safe_text
)
project::MaxStart_strategy = st.builds(
    project::MaxStart,
    maxStart=
        safe_text
)
project::EndCredit_strategy = st.builds(
    project::EndCredit,
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project::Period_strategy = st.builds(
    project::Period,
)
project::ProjectAttribute_strategy = st.builds(
    project::ProjectAttribute,
)
project::Interval2_strategy = st.builds(
    project::Interval2,
    end=
        safe_text,
    start=
        safe_text
)
project::Global_strategy = st.builds(
    project::Global,
)
IncludePropertiesAttribute_strategy = st.builds(
    IncludePropertiesAttribute,
)
project::ReportPrefix_strategy = st.builds(
    project::ReportPrefix,
)
project::ResourcePrefix_strategy = st.builds(
    project::ResourcePrefix,
)
project::TaskPrefix_strategy = st.builds(
    project::TaskPrefix,
)
project::AccountPrefix_strategy = st.builds(
    project::AccountPrefix,
)
project::AccountAttribute_strategy = st.builds(
    project::AccountAttribute,
)
AccountAttribute_strategy = st.builds(
    AccountAttribute,
)
project::Credit_strategy = st.builds(
    project::Credit,
    date=
        safe_text,
    description=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Property_strategy = st.builds(
    Property,
)
project::IncludeProperties_strategy = st.builds(
    project::IncludeProperties,
    importURI=
        safe_text
)
project::Export_strategy = st.builds(
    project::Export,
    filename=
        safe_text,
    id=
        safe_text
)
project::TimesheetReport_strategy = st.builds(
    project::TimesheetReport,
    filename=
        safe_text
)
project::Resource_strategy = st.builds(
    project::Resource,
    id=
        safe_text,
    name=
        safe_text
)
project::TaskReport_strategy = st.builds(
    project::TaskReport,
)
project::Rate_strategy = st.builds(
    project::Rate,
    rate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
project::SupplementAccount_strategy = st.builds(
    project::SupplementAccount,
)
project::NikuReport_strategy = st.builds(
    project::NikuReport,
    filename=
        safe_text
)
project::Macro_strategy = st.builds(
    project::Macro,
    value=
        safe_text
)
project::TagFile_strategy = st.builds(
    project::TagFile,
    filename=
        safe_text,
    id=
        safe_text
)
project::StatusSheetReport_strategy = st.builds(
    project::StatusSheetReport,
    filename=
        safe_text
)
project::AccountReport_strategy = st.builds(
    project::AccountReport,
)
project::TextReport_strategy = st.builds(
    project::TextReport,
)
project::StatusSheet_strategy = st.builds(
    project::StatusSheet,
)
project::Balance_strategy = st.builds(
    project::Balance,
)
project::Navigator_strategy = st.builds(
    project::Navigator,
    id=
        safe_text
)
project::Timesheet_strategy = st.builds(
    project::Timesheet,
)
project::Shift_strategy = st.builds(
    project::Shift,
    timezone=
        safe_text,
    id=
        safe_text,
    name=
        safe_text,
    replace=
        safe_text
)
project::SupplementTask_strategy = st.builds(
    project::SupplementTask,
)
project::SupplementResource_strategy = st.builds(
    project::SupplementResource,
)
project::ResourceReport_strategy = st.builds(
    project::ResourceReport,
)
project::Copyright_strategy = st.builds(
    project::Copyright,
    text=
        safe_text
)
project::Task_strategy = st.builds(
    project::Task,
    name=
        safe_text,
    id=
        safe_text
)
project::IcalReport_strategy = st.builds(
    project::IcalReport,
    filename=
        safe_text
)
project::Flags_strategy = st.builds(
    project::Flags,
    flags=
        safe_text
)
project::Vacation_strategy = st.builds(
    project::Vacation,
    name=
        safe_text
)
project::ProjectIds_strategy = st.builds(
    project::ProjectIds,
    ids=
        safe_text
)
project::SupplementReport_strategy = st.builds(
    project::SupplementReport,
)
project::Limits_strategy = st.builds(
    project::Limits,
)
project::Account_strategy = st.builds(
    project::Account,
    name=
        safe_text,
    id=
        safe_text
)
project::Property_strategy = st.builds(
    project::Property,
)
project::Project_strategy = st.builds(
    project::Project,
    name=
        safe_text,
    id=
        safe_text,
    version=
        safe_text
)

@given(instance=project::JvmIdentifiableElement_strategy)
@settings(max_examples=50)
def test_project::jvmidentifiableelement_instantiation(instance):
    assert isinstance(instance, project::JvmIdentifiableElement)

@given(instance=LogicalExpression_strategy)
@settings(max_examples=50)
def test_logicalexpression_instantiation(instance):
    assert isinstance(instance, LogicalExpression)

@given(instance=project::LogicalNumeralLiteral_strategy)
@settings(max_examples=50)
def test_project::logicalnumeralliteral_instantiation(instance):
    assert isinstance(instance, project::LogicalNumeralLiteral)

@given(instance=project::LogicalNumeralLiteral_strategy)
def test_project::logicalnumeralliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=project::LogicalNumeralLiteral_strategy)
def test_project::logicalnumeralliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project::LogicalFunctionExpression_strategy)
@settings(max_examples=50)
def test_project::logicalfunctionexpression_instantiation(instance):
    assert isinstance(instance, project::LogicalFunctionExpression)

@given(instance=project::LogicalAbsoluteIdExression_strategy)
@settings(max_examples=50)
def test_project::logicalabsoluteidexression_instantiation(instance):
    assert isinstance(instance, project::LogicalAbsoluteIdExression)

@given(instance=project::LogicalAbsoluteIdExression_strategy)
def test_project::logicalabsoluteidexression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=project::LogicalAbsoluteIdExression_strategy)
def test_project::logicalabsoluteidexression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project::LogicalDateLiteral_strategy)
@settings(max_examples=50)
def test_project::logicaldateliteral_instantiation(instance):
    assert isinstance(instance, project::LogicalDateLiteral)

@given(instance=project::LogicalDateLiteral_strategy)
def test_project::logicaldateliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=project::LogicalDateLiteral_strategy)
def test_project::logicaldateliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project::LogicalBooleanLiteral_strategy)
@settings(max_examples=50)
def test_project::logicalbooleanliteral_instantiation(instance):
    assert isinstance(instance, project::LogicalBooleanLiteral)

@given(instance=project::LogicalBooleanLiteral_strategy)
def test_project::logicalbooleanliteral_isTrue_type(instance):
    assert isinstance(instance.isTrue, bool)


@given(instance=project::LogicalBooleanLiteral_strategy)
def test_project::logicalbooleanliteral_isTrue_setter(instance):
    original = instance.isTrue
    instance.isTrue = original
    assert instance.isTrue == original

@given(instance=project::LogicalStringLiteral_strategy)
@settings(max_examples=50)
def test_project::logicalstringliteral_instantiation(instance):
    assert isinstance(instance, project::LogicalStringLiteral)

@given(instance=project::LogicalStringLiteral_strategy)
def test_project::logicalstringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=project::LogicalStringLiteral_strategy)
def test_project::logicalstringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project::XBinaryOperation_strategy)
@settings(max_examples=50)
def test_project::xbinaryoperation_instantiation(instance):
    assert isinstance(instance, project::XBinaryOperation)

@given(instance=Definitions_strategy)
@settings(max_examples=50)
def test_definitions_instantiation(instance):
    assert isinstance(instance, Definitions)

@given(instance=project::Defintions_strategy)
@settings(max_examples=50)
def test_project::defintions_instantiation(instance):
    assert isinstance(instance, project::Defintions)

@given(instance=project::Defintions_strategy)
def test_project::defintions_flags_type(instance):
    assert isinstance(instance.flags, bool)


@given(instance=project::Defintions_strategy)
def test_project::defintions_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original

@given(instance=project::Defintions_strategy)
def test_project::defintions_project_type(instance):
    assert isinstance(instance.project, bool)


@given(instance=project::Defintions_strategy)
def test_project::defintions_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original

@given(instance=project::Defintions_strategy)
def test_project::defintions_tasks_type(instance):
    assert isinstance(instance.tasks, bool)


@given(instance=project::Defintions_strategy)
def test_project::defintions_tasks_setter(instance):
    original = instance.tasks
    instance.tasks = original
    assert instance.tasks == original

@given(instance=project::Defintions_strategy)
def test_project::defintions_projectids_type(instance):
    assert isinstance(instance.projectids, bool)


@given(instance=project::Defintions_strategy)
def test_project::defintions_projectids_setter(instance):
    original = instance.projectids
    instance.projectids = original
    assert instance.projectids == original

@given(instance=project::Defintions_strategy)
def test_project::defintions_resources_type(instance):
    assert isinstance(instance.resources, bool)


@given(instance=project::Defintions_strategy)
def test_project::defintions_resources_setter(instance):
    original = instance.resources
    instance.resources = original
    assert instance.resources == original

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

@given(instance=project::RichText_strategy)
@settings(max_examples=50)
def test_project::richtext_instantiation(instance):
    assert isinstance(instance, project::RichText)

@given(instance=project::RichText_strategy)
def test_project::richtext_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=project::RichText_strategy)
def test_project::richtext_text_setter(instance):
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

@given(instance=project::TaskDependency_strategy)
@settings(max_examples=50)
def test_project::taskdependency_instantiation(instance):
    assert isinstance(instance, project::TaskDependency)

@given(instance=project::TaskDependency_strategy)
def test_project::taskdependency_policy_type(instance):
    assert isinstance(instance.policy, str)


@given(instance=project::TaskDependency_strategy)
def test_project::taskdependency_policy_setter(instance):
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

@given(instance=project::RealFormat_strategy)
@settings(max_examples=50)
def test_project::realformat_instantiation(instance):
    assert isinstance(instance, project::RealFormat)

@given(instance=project::RealFormat_strategy)
def test_project::realformat_negativeSuffix_type(instance):
    assert isinstance(instance.negativeSuffix, str)


@given(instance=project::RealFormat_strategy)
def test_project::realformat_negativeSuffix_setter(instance):
    original = instance.negativeSuffix
    instance.negativeSuffix = original
    assert instance.negativeSuffix == original

@given(instance=project::RealFormat_strategy)
def test_project::realformat_fractionSeparator_type(instance):
    assert isinstance(instance.fractionSeparator, str)


@given(instance=project::RealFormat_strategy)
def test_project::realformat_fractionSeparator_setter(instance):
    original = instance.fractionSeparator
    instance.fractionSeparator = original
    assert instance.fractionSeparator == original

@given(instance=project::RealFormat_strategy)
def test_project::realformat_negativePrefix_type(instance):
    assert isinstance(instance.negativePrefix, str)


@given(instance=project::RealFormat_strategy)
def test_project::realformat_negativePrefix_setter(instance):
    original = instance.negativePrefix
    instance.negativePrefix = original
    assert instance.negativePrefix == original

@given(instance=project::RealFormat_strategy)
def test_project::realformat_fractionDigits_type(instance):
    assert isinstance(instance.fractionDigits, int)


@given(instance=project::RealFormat_strategy)
def test_project::realformat_fractionDigits_setter(instance):
    original = instance.fractionDigits
    instance.fractionDigits = original
    assert instance.fractionDigits == original

@given(instance=project::RealFormat_strategy)
def test_project::realformat_thousandsSeparator_type(instance):
    assert isinstance(instance.thousandsSeparator, str)


@given(instance=project::RealFormat_strategy)
def test_project::realformat_thousandsSeparator_setter(instance):
    original = instance.thousandsSeparator
    instance.thousandsSeparator = original
    assert instance.thousandsSeparator == original

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

@given(instance=GapLength_strategy)
@settings(max_examples=50)
def test_gaplength_instantiation(instance):
    assert isinstance(instance, GapLength)

@given(instance=GapDuration_strategy)
@settings(max_examples=50)
def test_gapduration_instantiation(instance):
    assert isinstance(instance, GapDuration)

@given(instance=project::LimitAttribute_strategy)
@settings(max_examples=50)
def test_project::limitattribute_instantiation(instance):
    assert isinstance(instance, project::LimitAttribute)

@given(instance=project::LimitAttribute_strategy)
def test_project::limitattribute_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=project::LimitAttribute_strategy)
def test_project::limitattribute_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=project::LimitAttribute_strategy)
def test_project::limitattribute_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=project::LimitAttribute_strategy)
def test_project::limitattribute_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=WeeklyMin_strategy)
@settings(max_examples=50)
def test_weeklymin_instantiation(instance):
    assert isinstance(instance, WeeklyMin)

@given(instance=project::Limit_strategy)
@settings(max_examples=50)
def test_project::limit_instantiation(instance):
    assert isinstance(instance, project::Limit)

@given(instance=project::ColumnAttribute_strategy)
@settings(max_examples=50)
def test_project::columnattribute_instantiation(instance):
    assert isinstance(instance, project::ColumnAttribute)

@given(instance=project::WorkHours_strategy)
@settings(max_examples=50)
def test_project::workhours_instantiation(instance):
    assert isinstance(instance, project::WorkHours)

@given(instance=project::WorkHours_strategy)
def test_project::workhours_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=project::WorkHours_strategy)
def test_project::workhours_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=project::WorkHours_strategy)
def test_project::workhours_stop_type(instance):
    assert isinstance(instance.stop, str)


@given(instance=project::WorkHours_strategy)
def test_project::workhours_stop_setter(instance):
    original = instance.stop
    instance.stop = original
    assert instance.stop == original

@given(instance=project::Weekdays_strategy)
@settings(max_examples=50)
def test_project::weekdays_instantiation(instance):
    assert isinstance(instance, project::Weekdays)

@given(instance=project::Weekdays_strategy)
def test_project::weekdays_first_type(instance):
    assert isinstance(instance.first, str)


@given(instance=project::Weekdays_strategy)
def test_project::weekdays_first_setter(instance):
    original = instance.first
    instance.first = original
    assert instance.first == original

@given(instance=project::Weekdays_strategy)
def test_project::weekdays_last_type(instance):
    assert isinstance(instance.last, str)


@given(instance=project::Weekdays_strategy)
def test_project::weekdays_last_setter(instance):
    original = instance.last
    instance.last = original
    assert instance.last == original

@given(instance=project::TreeLevel_strategy)
@settings(max_examples=50)
def test_project::treelevel_instantiation(instance):
    assert isinstance(instance, project::TreeLevel)

@given(instance=project::TreeLevel_strategy)
def test_project::treelevel_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=project::TreeLevel_strategy)
def test_project::treelevel_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=project::TimesheetReportAttribute_strategy)
@settings(max_examples=50)
def test_project::timesheetreportattribute_instantiation(instance):
    assert isinstance(instance, project::TimesheetReportAttribute)

@given(instance=project::TimesheetAttribute_strategy)
@settings(max_examples=50)
def test_project::timesheetattribute_instantiation(instance):
    assert isinstance(instance, project::TimesheetAttribute)

@given(instance=StatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_statussheetattribute_instantiation(instance):
    assert isinstance(instance, StatusSheetAttribute)

@given(instance=project::TaskTimesheetAttribute_strategy)
@settings(max_examples=50)
def test_project::tasktimesheetattribute_instantiation(instance):
    assert isinstance(instance, project::TaskTimesheetAttribute)

@given(instance=project::TaskStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_project::taskstatussheetattribute_instantiation(instance):
    assert isinstance(instance, project::TaskStatusSheetAttribute)

@given(instance=project::StatusSheetReportAttribute_strategy)
@settings(max_examples=50)
def test_project::statussheetreportattribute_instantiation(instance):
    assert isinstance(instance, project::StatusSheetReportAttribute)

@given(instance=project::StatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_project::statussheetattribute_instantiation(instance):
    assert isinstance(instance, project::StatusSheetAttribute)

@given(instance=project::StatusTimesheetAttribute_strategy)
@settings(max_examples=50)
def test_project::statustimesheetattribute_instantiation(instance):
    assert isinstance(instance, project::StatusTimesheetAttribute)

@given(instance=project::Criterion_strategy)
@settings(max_examples=50)
def test_project::criterion_instantiation(instance):
    assert isinstance(instance, project::Criterion)

@given(instance=project::Criterion_strategy)
def test_project::criterion_columnId_type(instance):
    assert isinstance(instance.columnId, str)


@given(instance=project::Criterion_strategy)
def test_project::criterion_columnId_setter(instance):
    original = instance.columnId
    instance.columnId = original
    assert instance.columnId == original

@given(instance=project::Criterion_strategy)
def test_project::criterion_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=project::Criterion_strategy)
def test_project::criterion_direction_setter(instance):
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

@given(instance=project::Sort_strategy)
@settings(max_examples=50)
def test_project::sort_instantiation(instance):
    assert isinstance(instance, project::Sort)

@given(instance=project::Sort_strategy)
def test_project::sort_tree_type(instance):
    assert isinstance(instance.tree, bool)


@given(instance=project::Sort_strategy)
def test_project::sort_tree_setter(instance):
    original = instance.tree
    instance.tree = original
    assert instance.tree == original

@given(instance=project::StatusStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_project::statusstatussheetattribute_instantiation(instance):
    assert isinstance(instance, project::StatusStatusSheetAttribute)

@given(instance=TaskStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_taskstatussheetattribute_instantiation(instance):
    assert isinstance(instance, TaskStatusSheetAttribute)

@given(instance=project::TaskStatusSheet_strategy)
@settings(max_examples=50)
def test_project::taskstatussheet_instantiation(instance):
    assert isinstance(instance, project::TaskStatusSheet)

@given(instance=project::StatusStatusSheet_strategy)
@settings(max_examples=50)
def test_project::statusstatussheet_instantiation(instance):
    assert isinstance(instance, project::StatusStatusSheet)

@given(instance=project::StatusStatusSheet_strategy)
def test_project::statusstatussheet_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=project::StatusStatusSheet_strategy)
def test_project::statusstatussheet_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=project::StatusStatusSheet_strategy)
def test_project::statusstatussheet_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=project::StatusStatusSheet_strategy)
def test_project::statusstatussheet_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=project::ShiftsLimit_strategy)
@settings(max_examples=50)
def test_project::shiftslimit_instantiation(instance):
    assert isinstance(instance, project::ShiftsLimit)

@given(instance=ShiftsTask_strategy)
@settings(max_examples=50)
def test_shiftstask_instantiation(instance):
    assert isinstance(instance, ShiftsTask)

@given(instance=ShiftsResource_strategy)
@settings(max_examples=50)
def test_shiftsresource_instantiation(instance):
    assert isinstance(instance, ShiftsResource)

@given(instance=project::Shifts_strategy)
@settings(max_examples=50)
def test_project::shifts_instantiation(instance):
    assert isinstance(instance, project::Shifts)

@given(instance=project::LimitsAttribute_strategy)
@settings(max_examples=50)
def test_project::limitsattribute_instantiation(instance):
    assert isinstance(instance, project::LimitsAttribute)

@given(instance=project::Interval3_strategy)
@settings(max_examples=50)
def test_project::interval3_instantiation(instance):
    assert isinstance(instance, project::Interval3)

@given(instance=project::Interval3_strategy)
def test_project::interval3_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=project::Interval3_strategy)
def test_project::interval3_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=project::Interval3_strategy)
def test_project::interval3_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=project::Interval3_strategy)
def test_project::interval3_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=project::Interval1_strategy)
@settings(max_examples=50)
def test_project::interval1_instantiation(instance):
    assert isinstance(instance, project::Interval1)

@given(instance=project::Interval1_strategy)
def test_project::interval1_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=project::Interval1_strategy)
def test_project::interval1_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=project::Interval1_strategy)
def test_project::interval1_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=project::Interval1_strategy)
def test_project::interval1_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=project::IncludePropertiesAttribute_strategy)
@settings(max_examples=50)
def test_project::includepropertiesattribute_instantiation(instance):
    assert isinstance(instance, project::IncludePropertiesAttribute)

@given(instance=project::Function_strategy)
@settings(max_examples=50)
def test_project::function_instantiation(instance):
    assert isinstance(instance, project::Function)

@given(instance=project::Function_strategy)
def test_project::function_parentId_type(instance):
    assert isinstance(instance.parentId, str)


@given(instance=project::Function_strategy)
def test_project::function_parentId_setter(instance):
    original = instance.parentId
    instance.parentId = original
    assert instance.parentId == original

@given(instance=project::Function_strategy)
def test_project::function_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=project::Function_strategy)
def test_project::function_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=project::Function_strategy)
def test_project::function_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=project::Function_strategy)
def test_project::function_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=project::Function_strategy)
def test_project::function_distance_type(instance):
    assert isinstance(instance.distance, int)


@given(instance=project::Function_strategy)
def test_project::function_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=NavigatorAttribute_strategy)
@settings(max_examples=50)
def test_navigatorattribute_instantiation(instance):
    assert isinstance(instance, NavigatorAttribute)

@given(instance=project::HideReport_strategy)
@settings(max_examples=50)
def test_project::hidereport_instantiation(instance):
    assert isinstance(instance, project::HideReport)

@given(instance=project::GapLength_strategy)
@settings(max_examples=50)
def test_project::gaplength_instantiation(instance):
    assert isinstance(instance, project::GapLength)

@given(instance=project::GapDuration_strategy)
@settings(max_examples=50)
def test_project::gapduration_instantiation(instance):
    assert isinstance(instance, project::GapDuration)

@given(instance=project::Extend_strategy)
@settings(max_examples=50)
def test_project::extend_instantiation(instance):
    assert isinstance(instance, project::Extend)

@given(instance=project::Extend_strategy)
def test_project::extend_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=project::Extend_strategy)
def test_project::extend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=project::Extend_strategy)
def test_project::extend_scenariospecific_type(instance):
    assert isinstance(instance.scenariospecific, bool)


@given(instance=project::Extend_strategy)
def test_project::extend_scenariospecific_setter(instance):
    original = instance.scenariospecific
    instance.scenariospecific = original
    assert instance.scenariospecific == original

@given(instance=project::Extend_strategy)
def test_project::extend_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=project::Extend_strategy)
def test_project::extend_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project::Extend_strategy)
def test_project::extend_inherit_type(instance):
    assert isinstance(instance.inherit, bool)


@given(instance=project::Extend_strategy)
def test_project::extend_inherit_setter(instance):
    original = instance.inherit
    instance.inherit = original
    assert instance.inherit == original

@given(instance=ExportAttribute_strategy)
@settings(max_examples=50)
def test_exportattribute_instantiation(instance):
    assert isinstance(instance, ExportAttribute)

@given(instance=project::TaskAttributes_strategy)
@settings(max_examples=50)
def test_project::taskattributes_instantiation(instance):
    assert isinstance(instance, project::TaskAttributes)

@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_flags_type(instance):
    assert isinstance(instance.flags, bool)


@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original

@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_maxstart_type(instance):
    assert isinstance(instance.maxstart, bool)


@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_maxstart_setter(instance):
    original = instance.maxstart
    instance.maxstart = original
    assert instance.maxstart == original

@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_booking_type(instance):
    assert isinstance(instance.booking, bool)


@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_booking_setter(instance):
    original = instance.booking
    instance.booking = original
    assert instance.booking == original

@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_note_type(instance):
    assert isinstance(instance.note, bool)


@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_priority_type(instance):
    assert isinstance(instance.priority, bool)


@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_complete_type(instance):
    assert isinstance(instance.complete, bool)


@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_complete_setter(instance):
    original = instance.complete
    instance.complete = original
    assert instance.complete == original

@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_none_type(instance):
    assert isinstance(instance.none, bool)


@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_maxend_type(instance):
    assert isinstance(instance.maxend, bool)


@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_maxend_setter(instance):
    original = instance.maxend
    instance.maxend = original
    assert instance.maxend == original

@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_minstart_type(instance):
    assert isinstance(instance.minstart, bool)


@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_minstart_setter(instance):
    original = instance.minstart
    instance.minstart = original
    assert instance.minstart == original

@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_minend_type(instance):
    assert isinstance(instance.minend, bool)


@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_minend_setter(instance):
    original = instance.minend
    instance.minend = original
    assert instance.minend == original

@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_depends_type(instance):
    assert isinstance(instance.depends, bool)


@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_depends_setter(instance):
    original = instance.depends
    instance.depends = original
    assert instance.depends == original

@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_responsible_type(instance):
    assert isinstance(instance.responsible, bool)


@given(instance=project::TaskAttributes_strategy)
def test_project::taskattributes_responsible_setter(instance):
    original = instance.responsible
    instance.responsible = original
    assert instance.responsible == original

@given(instance=project::ResourceAttributes_strategy)
@settings(max_examples=50)
def test_project::resourceattributes_instantiation(instance):
    assert isinstance(instance, project::ResourceAttributes)

@given(instance=project::ResourceAttributes_strategy)
def test_project::resourceattributes_none_type(instance):
    assert isinstance(instance.none, bool)


@given(instance=project::ResourceAttributes_strategy)
def test_project::resourceattributes_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=project::ResourceAttributes_strategy)
def test_project::resourceattributes_booking_type(instance):
    assert isinstance(instance.booking, bool)


@given(instance=project::ResourceAttributes_strategy)
def test_project::resourceattributes_booking_setter(instance):
    original = instance.booking
    instance.booking = original
    assert instance.booking == original

@given(instance=project::ResourceAttributes_strategy)
def test_project::resourceattributes_workingHours_type(instance):
    assert isinstance(instance.workingHours, bool)


@given(instance=project::ResourceAttributes_strategy)
def test_project::resourceattributes_workingHours_setter(instance):
    original = instance.workingHours
    instance.workingHours = original
    assert instance.workingHours == original

@given(instance=project::ResourceAttributes_strategy)
def test_project::resourceattributes_vacation_type(instance):
    assert isinstance(instance.vacation, bool)


@given(instance=project::ResourceAttributes_strategy)
def test_project::resourceattributes_vacation_setter(instance):
    original = instance.vacation
    instance.vacation = original
    assert instance.vacation == original

@given(instance=project::ResourceAttributes_strategy)
def test_project::resourceattributes_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=project::ResourceAttributes_strategy)
def test_project::resourceattributes_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=project::Definitions_strategy)
@settings(max_examples=50)
def test_project::definitions_instantiation(instance):
    assert isinstance(instance, project::Definitions)

@given(instance=project::Definitions_strategy)
def test_project::definitions_none_type(instance):
    assert isinstance(instance.none, bool)


@given(instance=project::Definitions_strategy)
def test_project::definitions_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=project::Definitions_strategy)
def test_project::definitions_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=project::Definitions_strategy)
def test_project::definitions_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=LimitsAttribute_strategy)
@settings(max_examples=50)
def test_limitsattribute_instantiation(instance):
    assert isinstance(instance, LimitsAttribute)

@given(instance=project::WeeklyMin_strategy)
@settings(max_examples=50)
def test_project::weeklymin_instantiation(instance):
    assert isinstance(instance, project::WeeklyMin)

@given(instance=project::Maximum_strategy)
@settings(max_examples=50)
def test_project::maximum_instantiation(instance):
    assert isinstance(instance, project::Maximum)

@given(instance=project::MonthlyMax_strategy)
@settings(max_examples=50)
def test_project::monthlymax_instantiation(instance):
    assert isinstance(instance, project::MonthlyMax)

@given(instance=project::WeeklyMax_strategy)
@settings(max_examples=50)
def test_project::weeklymax_instantiation(instance):
    assert isinstance(instance, project::WeeklyMax)

@given(instance=project::Minimum_strategy)
@settings(max_examples=50)
def test_project::minimum_instantiation(instance):
    assert isinstance(instance, project::Minimum)

@given(instance=project::DailyMin_strategy)
@settings(max_examples=50)
def test_project::dailymin_instantiation(instance):
    assert isinstance(instance, project::DailyMin)

@given(instance=project::MonthlyMin_strategy)
@settings(max_examples=50)
def test_project::monthlymin_instantiation(instance):
    assert isinstance(instance, project::MonthlyMin)

@given(instance=project::DailyMax_strategy)
@settings(max_examples=50)
def test_project::dailymax_instantiation(instance):
    assert isinstance(instance, project::DailyMax)

@given(instance=ProjectAttribute_strategy)
@settings(max_examples=50)
def test_projectattribute_instantiation(instance):
    assert isinstance(instance, ProjectAttribute)

@given(instance=project::TimingResolution_strategy)
@settings(max_examples=50)
def test_project::timingresolution_instantiation(instance):
    assert isinstance(instance, project::TimingResolution)

@given(instance=project::TimingResolution_strategy)
def test_project::timingresolution_timingResolution_type(instance):
    assert isinstance(instance.timingResolution, int)


@given(instance=project::TimingResolution_strategy)
def test_project::timingresolution_timingResolution_setter(instance):
    original = instance.timingResolution
    instance.timingResolution = original
    assert instance.timingResolution == original

@given(instance=project::ExtendResource_strategy)
@settings(max_examples=50)
def test_project::extendresource_instantiation(instance):
    assert isinstance(instance, project::ExtendResource)

@given(instance=project::ExtendTask_strategy)
@settings(max_examples=50)
def test_project::extendtask_instantiation(instance):
    assert isinstance(instance, project::ExtendTask)

@given(instance=project::DailyWorkingHours_strategy)
@settings(max_examples=50)
def test_project::dailyworkinghours_instantiation(instance):
    assert isinstance(instance, project::DailyWorkingHours)

@given(instance=project::DailyWorkingHours_strategy)
def test_project::dailyworkinghours_dailyWorkingHours_type(instance):
    assert isinstance(instance.dailyWorkingHours, float)


@given(instance=project::DailyWorkingHours_strategy)
def test_project::dailyworkinghours_dailyWorkingHours_setter(instance):
    original = instance.dailyWorkingHours
    instance.dailyWorkingHours = original
    assert instance.dailyWorkingHours == original

@given(instance=project::ShortTimeFormat_strategy)
@settings(max_examples=50)
def test_project::shorttimeformat_instantiation(instance):
    assert isinstance(instance, project::ShortTimeFormat)

@given(instance=project::ShortTimeFormat_strategy)
def test_project::shorttimeformat_shortTimeFormat_type(instance):
    assert isinstance(instance.shortTimeFormat, str)


@given(instance=project::ShortTimeFormat_strategy)
def test_project::shorttimeformat_shortTimeFormat_setter(instance):
    original = instance.shortTimeFormat
    instance.shortTimeFormat = original
    assert instance.shortTimeFormat == original

@given(instance=project::WeekStarts_strategy)
@settings(max_examples=50)
def test_project::weekstarts_instantiation(instance):
    assert isinstance(instance, project::WeekStarts)

@given(instance=project::WeekStarts_strategy)
def test_project::weekstarts_sunday_type(instance):
    assert isinstance(instance.sunday, bool)


@given(instance=project::WeekStarts_strategy)
def test_project::weekstarts_sunday_setter(instance):
    original = instance.sunday
    instance.sunday = original
    assert instance.sunday == original

@given(instance=project::WeekStarts_strategy)
def test_project::weekstarts_monday_type(instance):
    assert isinstance(instance.monday, bool)


@given(instance=project::WeekStarts_strategy)
def test_project::weekstarts_monday_setter(instance):
    original = instance.monday
    instance.monday = original
    assert instance.monday == original

@given(instance=project::Scenario_strategy)
@settings(max_examples=50)
def test_project::scenario_instantiation(instance):
    assert isinstance(instance, project::Scenario)

@given(instance=project::Scenario_strategy)
def test_project::scenario_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=project::Scenario_strategy)
def test_project::scenario_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=project::Scenario_strategy)
def test_project::scenario_active_type(instance):
    assert isinstance(instance.active, str)


@given(instance=project::Scenario_strategy)
def test_project::scenario_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=project::Scenario_strategy)
def test_project::scenario_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=project::Scenario_strategy)
def test_project::scenario_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project::Include_strategy)
@settings(max_examples=50)
def test_project::include_instantiation(instance):
    assert isinstance(instance, project::Include)

@given(instance=project::Include_strategy)
def test_project::include_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=project::Include_strategy)
def test_project::include_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=project::TrackingScenario_strategy)
@settings(max_examples=50)
def test_project::trackingscenario_instantiation(instance):
    assert isinstance(instance, project::TrackingScenario)

@given(instance=project::Now_strategy)
@settings(max_examples=50)
def test_project::now_instantiation(instance):
    assert isinstance(instance, project::Now)

@given(instance=project::Now_strategy)
def test_project::now_now_type(instance):
    assert isinstance(instance.now, str)


@given(instance=project::Now_strategy)
def test_project::now_now_setter(instance):
    original = instance.now
    instance.now = original
    assert instance.now == original

@given(instance=project::YearlyWorkingDays_strategy)
@settings(max_examples=50)
def test_project::yearlyworkingdays_instantiation(instance):
    assert isinstance(instance, project::YearlyWorkingDays)

@given(instance=project::YearlyWorkingDays_strategy)
def test_project::yearlyworkingdays_yearlyWorkingDays_type(instance):
    assert isinstance(instance.yearlyWorkingDays, int)


@given(instance=project::YearlyWorkingDays_strategy)
def test_project::yearlyworkingdays_yearlyWorkingDays_setter(instance):
    original = instance.yearlyWorkingDays
    instance.yearlyWorkingDays = original
    assert instance.yearlyWorkingDays == original

@given(instance=project::Currency_strategy)
@settings(max_examples=50)
def test_project::currency_instantiation(instance):
    assert isinstance(instance, project::Currency)

@given(instance=project::Currency_strategy)
def test_project::currency_currency_type(instance):
    assert isinstance(instance.currency, str)


@given(instance=project::Currency_strategy)
def test_project::currency_currency_setter(instance):
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

@given(instance=project::Timeoff_strategy)
@settings(max_examples=50)
def test_project::timeoff_instantiation(instance):
    assert isinstance(instance, project::Timeoff)

@given(instance=project::Timeoff_strategy)
def test_project::timeoff_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=project::Timeoff_strategy)
def test_project::timeoff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=project::Timeoff_strategy)
def test_project::timeoff_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=project::Timeoff_strategy)
def test_project::timeoff_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=NewTaskAttribute_strategy)
@settings(max_examples=50)
def test_newtaskattribute_instantiation(instance):
    assert isinstance(instance, NewTaskAttribute)

@given(instance=project::Remaining_strategy)
@settings(max_examples=50)
def test_project::remaining_instantiation(instance):
    assert isinstance(instance, project::Remaining)

@given(instance=project::Work_strategy)
@settings(max_examples=50)
def test_project::work_instantiation(instance):
    assert isinstance(instance, project::Work)

@given(instance=project::Work_strategy)
def test_project::work_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=project::Work_strategy)
def test_project::work_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=project::Work_strategy)
def test_project::work_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=project::Work_strategy)
def test_project::work_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=IcalReportAttribute_strategy)
@settings(max_examples=50)
def test_icalreportattribute_instantiation(instance):
    assert isinstance(instance, IcalReportAttribute)

@given(instance=project::ScenarioIcal_strategy)
@settings(max_examples=50)
def test_project::scenarioical_instantiation(instance):
    assert isinstance(instance, project::ScenarioIcal)

@given(instance=project::DurationQuantity_strategy)
@settings(max_examples=50)
def test_project::durationquantity_instantiation(instance):
    assert isinstance(instance, project::DurationQuantity)

@given(instance=project::DurationQuantity_strategy)
def test_project::durationquantity_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=project::DurationQuantity_strategy)
def test_project::durationquantity_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=project::DurationQuantity_strategy)
def test_project::durationquantity_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=project::DurationQuantity_strategy)
def test_project::durationquantity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=StatusTimesheetAttribute_strategy)
@settings(max_examples=50)
def test_statustimesheetattribute_instantiation(instance):
    assert isinstance(instance, StatusTimesheetAttribute)

@given(instance=project::RGB_strategy)
@settings(max_examples=50)
def test_project::rgb_instantiation(instance):
    assert isinstance(instance, project::RGB)

@given(instance=project::RGB_strategy)
def test_project::rgb_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=project::RGB_strategy)
def test_project::rgb_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project::LogicalExpression_strategy)
@settings(max_examples=50)
def test_project::logicalexpression_instantiation(instance):
    assert isinstance(instance, project::LogicalExpression)

@given(instance=ColumnAttribute_strategy)
@settings(max_examples=50)
def test_columnattribute_instantiation(instance):
    assert isinstance(instance, ColumnAttribute)

@given(instance=project::ToolTip_strategy)
@settings(max_examples=50)
def test_project::tooltip_instantiation(instance):
    assert isinstance(instance, project::ToolTip)

@given(instance=project::ToolTip_strategy)
def test_project::tooltip_tip_type(instance):
    assert isinstance(instance.tip, str)


@given(instance=project::ToolTip_strategy)
def test_project::tooltip_tip_setter(instance):
    original = instance.tip
    instance.tip = original
    assert instance.tip == original

@given(instance=project::ListItem_strategy)
@settings(max_examples=50)
def test_project::listitem_instantiation(instance):
    assert isinstance(instance, project::ListItem)

@given(instance=project::FontColor_strategy)
@settings(max_examples=50)
def test_project::fontcolor_instantiation(instance):
    assert isinstance(instance, project::FontColor)

@given(instance=project::FontColor_strategy)
def test_project::fontcolor_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=project::FontColor_strategy)
def test_project::fontcolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=project::Scale_strategy)
@settings(max_examples=50)
def test_project::scale_instantiation(instance):
    assert isinstance(instance, project::Scale)

@given(instance=project::Scale_strategy)
def test_project::scale_scale_type(instance):
    assert isinstance(instance.scale, str)


@given(instance=project::Scale_strategy)
def test_project::scale_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=project::HAlign_strategy)
@settings(max_examples=50)
def test_project::halign_instantiation(instance):
    assert isinstance(instance, project::HAlign)

@given(instance=project::HAlign_strategy)
def test_project::halign_justification_type(instance):
    assert isinstance(instance.justification, str)


@given(instance=project::HAlign_strategy)
def test_project::halign_justification_setter(instance):
    original = instance.justification
    instance.justification = original
    assert instance.justification == original

@given(instance=project::ListType_strategy)
@settings(max_examples=50)
def test_project::listtype_instantiation(instance):
    assert isinstance(instance, project::ListType)

@given(instance=project::ListType_strategy)
def test_project::listtype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=project::ListType_strategy)
def test_project::listtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=project::Width_strategy)
@settings(max_examples=50)
def test_project::width_instantiation(instance):
    assert isinstance(instance, project::Width)

@given(instance=project::Width_strategy)
def test_project::width_width_type(instance):
    assert isinstance(instance.width, float)


@given(instance=project::Width_strategy)
def test_project::width_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=project::CellText_strategy)
@settings(max_examples=50)
def test_project::celltext_instantiation(instance):
    assert isinstance(instance, project::CellText)

@given(instance=project::CellText_strategy)
def test_project::celltext_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=project::CellText_strategy)
def test_project::celltext_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=project::CellColor_strategy)
@settings(max_examples=50)
def test_project::cellcolor_instantiation(instance):
    assert isinstance(instance, project::CellColor)

@given(instance=project::Column_strategy)
@settings(max_examples=50)
def test_project::column_instantiation(instance):
    assert isinstance(instance, project::Column)

@given(instance=project::Column_strategy)
def test_project::column_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=project::Column_strategy)
def test_project::column_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project::AccountShare_strategy)
@settings(max_examples=50)
def test_project::accountshare_instantiation(instance):
    assert isinstance(instance, project::AccountShare)

@given(instance=project::AccountShare_strategy)
def test_project::accountshare_share_type(instance):
    assert isinstance(instance.share, float)


@given(instance=project::AccountShare_strategy)
def test_project::accountshare_share_setter(instance):
    original = instance.share
    instance.share = original
    assert instance.share == original

@given(instance=StatusStatusSheetAttribute_strategy)
@settings(max_examples=50)
def test_statusstatussheetattribute_instantiation(instance):
    assert isinstance(instance, StatusStatusSheetAttribute)

@given(instance=project::Details_strategy)
@settings(max_examples=50)
def test_project::details_instantiation(instance):
    assert isinstance(instance, project::Details)

@given(instance=project::Summary_strategy)
@settings(max_examples=50)
def test_project::summary_instantiation(instance):
    assert isinstance(instance, project::Summary)

@given(instance=project::Author_strategy)
@settings(max_examples=50)
def test_project::author_instantiation(instance):
    assert isinstance(instance, project::Author)

@given(instance=AllocateResourceAttribute_strategy)
@settings(max_examples=50)
def test_allocateresourceattribute_instantiation(instance):
    assert isinstance(instance, AllocateResourceAttribute)

@given(instance=project::Select_strategy)
@settings(max_examples=50)
def test_project::select_instantiation(instance):
    assert isinstance(instance, project::Select)

@given(instance=project::Select_strategy)
def test_project::select_argument_type(instance):
    assert isinstance(instance.argument, str)


@given(instance=project::Select_strategy)
def test_project::select_argument_setter(instance):
    original = instance.argument
    instance.argument = original
    assert instance.argument == original

@given(instance=project::ShiftsAllocate_strategy)
@settings(max_examples=50)
def test_project::shiftsallocate_instantiation(instance):
    assert isinstance(instance, project::ShiftsAllocate)

@given(instance=project::Persistent_strategy)
@settings(max_examples=50)
def test_project::persistent_instantiation(instance):
    assert isinstance(instance, project::Persistent)

@given(instance=project::Persistent_strategy)
def test_project::persistent_persistent_type(instance):
    assert isinstance(instance.persistent, bool)


@given(instance=project::Persistent_strategy)
def test_project::persistent_persistent_setter(instance):
    original = instance.persistent
    instance.persistent = original
    assert instance.persistent == original

@given(instance=project::Mandatory_strategy)
@settings(max_examples=50)
def test_project::mandatory_instantiation(instance):
    assert isinstance(instance, project::Mandatory)

@given(instance=project::Mandatory_strategy)
def test_project::mandatory_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=project::Mandatory_strategy)
def test_project::mandatory_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=project::Alternative_strategy)
@settings(max_examples=50)
def test_project::alternative_instantiation(instance):
    assert isinstance(instance, project::Alternative)

@given(instance=project::Alert_strategy)
@settings(max_examples=50)
def test_project::alert_instantiation(instance):
    assert isinstance(instance, project::Alert)

@given(instance=project::Alert_strategy)
def test_project::alert_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=project::Alert_strategy)
def test_project::alert_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=project::NikuReportAttribute_strategy)
@settings(max_examples=50)
def test_project::nikureportattribute_instantiation(instance):
    assert isinstance(instance, project::NikuReportAttribute)

@given(instance=project::Interval4_strategy)
@settings(max_examples=50)
def test_project::interval4_instantiation(instance):
    assert isinstance(instance, project::Interval4)

@given(instance=project::Interval4_strategy)
def test_project::interval4_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=project::Interval4_strategy)
def test_project::interval4_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=project::Interval4_strategy)
def test_project::interval4_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=project::Interval4_strategy)
def test_project::interval4_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=project::Booking_strategy)
@settings(max_examples=50)
def test_project::booking_instantiation(instance):
    assert isinstance(instance, project::Booking)

@given(instance=project::Booking_strategy)
def test_project::booking_sloppy_type(instance):
    assert isinstance(instance.sloppy, int)


@given(instance=project::Booking_strategy)
def test_project::booking_sloppy_setter(instance):
    original = instance.sloppy
    instance.sloppy = original
    assert instance.sloppy == original

@given(instance=project::Booking_strategy)
def test_project::booking_overtime_type(instance):
    assert isinstance(instance.overtime, int)


@given(instance=project::Booking_strategy)
def test_project::booking_overtime_setter(instance):
    original = instance.overtime
    instance.overtime = original
    assert instance.overtime == original

@given(instance=project::AllocateResourceAttribute_strategy)
@settings(max_examples=50)
def test_project::allocateresourceattribute_instantiation(instance):
    assert isinstance(instance, project::AllocateResourceAttribute)

@given(instance=project::AllocateResource_strategy)
@settings(max_examples=50)
def test_project::allocateresource_instantiation(instance):
    assert isinstance(instance, project::AllocateResource)

@given(instance=project::NewTaskAttribute_strategy)
@settings(max_examples=50)
def test_project::newtaskattribute_instantiation(instance):
    assert isinstance(instance, project::NewTaskAttribute)

@given(instance=TimesheetAttribute_strategy)
@settings(max_examples=50)
def test_timesheetattribute_instantiation(instance):
    assert isinstance(instance, TimesheetAttribute)

@given(instance=project::TaskTimesheet_strategy)
@settings(max_examples=50)
def test_project::tasktimesheet_instantiation(instance):
    assert isinstance(instance, project::TaskTimesheet)

@given(instance=project::ShiftTimesheet_strategy)
@settings(max_examples=50)
def test_project::shifttimesheet_instantiation(instance):
    assert isinstance(instance, project::ShiftTimesheet)

@given(instance=project::StatusTimesheet_strategy)
@settings(max_examples=50)
def test_project::statustimesheet_instantiation(instance):
    assert isinstance(instance, project::StatusTimesheet)

@given(instance=project::StatusTimesheet_strategy)
def test_project::statustimesheet_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=project::StatusTimesheet_strategy)
def test_project::statustimesheet_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=project::StatusTimesheet_strategy)
def test_project::statustimesheet_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=project::StatusTimesheet_strategy)
def test_project::statustimesheet_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=project::NewTask_strategy)
@settings(max_examples=50)
def test_project::newtask_instantiation(instance):
    assert isinstance(instance, project::NewTask)

@given(instance=project::NewTask_strategy)
def test_project::newtask_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=project::NewTask_strategy)
def test_project::newtask_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=project::NewTask_strategy)
def test_project::newtask_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=project::NewTask_strategy)
def test_project::newtask_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project::NavigatorAttribute_strategy)
@settings(max_examples=50)
def test_project::navigatorattribute_instantiation(instance):
    assert isinstance(instance, project::NavigatorAttribute)

@given(instance=project::ReportAttribute_strategy)
@settings(max_examples=50)
def test_project::reportattribute_instantiation(instance):
    assert isinstance(instance, project::ReportAttribute)

@given(instance=project::ResourceAttribute_strategy)
@settings(max_examples=50)
def test_project::resourceattribute_instantiation(instance):
    assert isinstance(instance, project::ResourceAttribute)

@given(instance=ResourceAttribute_strategy)
@settings(max_examples=50)
def test_resourceattribute_instantiation(instance):
    assert isinstance(instance, ResourceAttribute)

@given(instance=project::Efficiency_strategy)
@settings(max_examples=50)
def test_project::efficiency_instantiation(instance):
    assert isinstance(instance, project::Efficiency)

@given(instance=project::Efficiency_strategy)
def test_project::efficiency_efficiency_type(instance):
    assert isinstance(instance.efficiency, float)


@given(instance=project::Efficiency_strategy)
def test_project::efficiency_efficiency_setter(instance):
    original = instance.efficiency
    instance.efficiency = original
    assert instance.efficiency == original

@given(instance=project::PurgeResource_strategy)
@settings(max_examples=50)
def test_project::purgeresource_instantiation(instance):
    assert isinstance(instance, project::PurgeResource)

@given(instance=project::PurgeResource_strategy)
def test_project::purgeresource_listAttribute_type(instance):
    assert isinstance(instance.listAttribute, str)


@given(instance=project::PurgeResource_strategy)
def test_project::purgeresource_listAttribute_setter(instance):
    original = instance.listAttribute
    instance.listAttribute = original
    assert instance.listAttribute == original

@given(instance=project::WorkingHours_strategy)
@settings(max_examples=50)
def test_project::workinghours_instantiation(instance):
    assert isinstance(instance, project::WorkingHours)

@given(instance=project::WorkingHours_strategy)
def test_project::workinghours_off_type(instance):
    assert isinstance(instance.off, bool)


@given(instance=project::WorkingHours_strategy)
def test_project::workinghours_off_setter(instance):
    original = instance.off
    instance.off = original
    assert instance.off == original

@given(instance=project::ShiftsResource_strategy)
@settings(max_examples=50)
def test_project::shiftsresource_instantiation(instance):
    assert isinstance(instance, project::ShiftsResource)

@given(instance=project::ExtendedResourceAttribute_strategy)
@settings(max_examples=50)
def test_project::extendedresourceattribute_instantiation(instance):
    assert isinstance(instance, project::ExtendedResourceAttribute)

@given(instance=project::ExtendedResourceAttribute_strategy)
def test_project::extendedresourceattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=project::ExtendedResourceAttribute_strategy)
def test_project::extendedresourceattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project::BookingResource_strategy)
@settings(max_examples=50)
def test_project::bookingresource_instantiation(instance):
    assert isinstance(instance, project::BookingResource)

@given(instance=project::Email_strategy)
@settings(max_examples=50)
def test_project::email_instantiation(instance):
    assert isinstance(instance, project::Email)

@given(instance=project::Email_strategy)
def test_project::email_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=project::Email_strategy)
def test_project::email_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=project::Managers_strategy)
@settings(max_examples=50)
def test_project::managers_instantiation(instance):
    assert isinstance(instance, project::Managers)

@given(instance=project::ExportAttribute_strategy)
@settings(max_examples=50)
def test_project::exportattribute_instantiation(instance):
    assert isinstance(instance, project::ExportAttribute)

@given(instance=project::IcalReportAttribute_strategy)
@settings(max_examples=50)
def test_project::icalreportattribute_instantiation(instance):
    assert isinstance(instance, project::IcalReportAttribute)

@given(instance=ReportAttribute_strategy)
@settings(max_examples=50)
def test_reportattribute_instantiation(instance):
    assert isinstance(instance, ReportAttribute)

@given(instance=project::RollupTask_strategy)
@settings(max_examples=50)
def test_project::rolluptask_instantiation(instance):
    assert isinstance(instance, project::RollupTask)

@given(instance=project::RollupResource_strategy)
@settings(max_examples=50)
def test_project::rollupresource_instantiation(instance):
    assert isinstance(instance, project::RollupResource)

@given(instance=project::PurgeReport_strategy)
@settings(max_examples=50)
def test_project::purgereport_instantiation(instance):
    assert isinstance(instance, project::PurgeReport)

@given(instance=project::PurgeReport_strategy)
def test_project::purgereport_listAttribute_type(instance):
    assert isinstance(instance.listAttribute, str)


@given(instance=project::PurgeReport_strategy)
def test_project::purgereport_listAttribute_setter(instance):
    original = instance.listAttribute
    instance.listAttribute = original
    assert instance.listAttribute == original

@given(instance=project::SelfContained_strategy)
@settings(max_examples=50)
def test_project::selfcontained_instantiation(instance):
    assert isinstance(instance, project::SelfContained)

@given(instance=project::SelfContained_strategy)
def test_project::selfcontained_selfcontained_type(instance):
    assert isinstance(instance.selfcontained, str)


@given(instance=project::SelfContained_strategy)
def test_project::selfcontained_selfcontained_setter(instance):
    original = instance.selfcontained
    instance.selfcontained = original
    assert instance.selfcontained == original

@given(instance=project::Scenarios_strategy)
@settings(max_examples=50)
def test_project::scenarios_instantiation(instance):
    assert isinstance(instance, project::Scenarios)

@given(instance=project::Right_strategy)
@settings(max_examples=50)
def test_project::right_instantiation(instance):
    assert isinstance(instance, project::Right)

@given(instance=project::JournalMode_strategy)
@settings(max_examples=50)
def test_project::journalmode_instantiation(instance):
    assert isinstance(instance, project::JournalMode)

@given(instance=project::JournalMode_strategy)
def test_project::journalmode_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=project::JournalMode_strategy)
def test_project::journalmode_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=project::Center_strategy)
@settings(max_examples=50)
def test_project::center_instantiation(instance):
    assert isinstance(instance, project::Center)

@given(instance=project::SortResources_strategy)
@settings(max_examples=50)
def test_project::sortresources_instantiation(instance):
    assert isinstance(instance, project::SortResources)

@given(instance=project::HideAccount_strategy)
@settings(max_examples=50)
def test_project::hideaccount_instantiation(instance):
    assert isinstance(instance, project::HideAccount)

@given(instance=project::HideAccount_strategy)
def test_project::hideaccount_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=project::HideAccount_strategy)
def test_project::hideaccount_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=project::CurrencyFormat_strategy)
@settings(max_examples=50)
def test_project::currencyformat_instantiation(instance):
    assert isinstance(instance, project::CurrencyFormat)

@given(instance=project::LoadUnit_strategy)
@settings(max_examples=50)
def test_project::loadunit_instantiation(instance):
    assert isinstance(instance, project::LoadUnit)

@given(instance=project::LoadUnit_strategy)
def test_project::loadunit_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=project::LoadUnit_strategy)
def test_project::loadunit_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=project::Epilog_strategy)
@settings(max_examples=50)
def test_project::epilog_instantiation(instance):
    assert isinstance(instance, project::Epilog)

@given(instance=project::Left_strategy)
@settings(max_examples=50)
def test_project::left_instantiation(instance):
    assert isinstance(instance, project::Left)

@given(instance=project::HideJournalEntry_strategy)
@settings(max_examples=50)
def test_project::hidejournalentry_instantiation(instance):
    assert isinstance(instance, project::HideJournalEntry)

@given(instance=project::HideJournalEntry_strategy)
def test_project::hidejournalentry_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=project::HideJournalEntry_strategy)
def test_project::hidejournalentry_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=project::ResourceRoot_strategy)
@settings(max_examples=50)
def test_project::resourceroot_instantiation(instance):
    assert isinstance(instance, project::ResourceRoot)

@given(instance=project::Timezone_strategy)
@settings(max_examples=50)
def test_project::timezone_instantiation(instance):
    assert isinstance(instance, project::Timezone)

@given(instance=project::Timezone_strategy)
def test_project::timezone_timezone_type(instance):
    assert isinstance(instance.timezone, str)


@given(instance=project::Timezone_strategy)
def test_project::timezone_timezone_setter(instance):
    original = instance.timezone
    instance.timezone = original
    assert instance.timezone == original

@given(instance=project::Caption_strategy)
@settings(max_examples=50)
def test_project::caption_instantiation(instance):
    assert isinstance(instance, project::Caption)

@given(instance=project::SortJournalEntries_strategy)
@settings(max_examples=50)
def test_project::sortjournalentries_instantiation(instance):
    assert isinstance(instance, project::SortJournalEntries)

@given(instance=project::HideResource_strategy)
@settings(max_examples=50)
def test_project::hideresource_instantiation(instance):
    assert isinstance(instance, project::HideResource)

@given(instance=project::Formats_strategy)
@settings(max_examples=50)
def test_project::formats_instantiation(instance):
    assert isinstance(instance, project::Formats)

@given(instance=project::Formats_strategy)
def test_project::formats_formats_type(instance):
    assert isinstance(instance.formats, str)


@given(instance=project::Formats_strategy)
def test_project::formats_formats_setter(instance):
    original = instance.formats
    instance.formats = original
    assert instance.formats == original

@given(instance=project::JournalAttributes_strategy)
@settings(max_examples=50)
def test_project::journalattributes_instantiation(instance):
    assert isinstance(instance, project::JournalAttributes)

@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_propertyid_type(instance):
    assert isinstance(instance.propertyid, bool)


@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_propertyid_setter(instance):
    original = instance.propertyid
    instance.propertyid = original
    assert instance.propertyid == original

@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_none_type(instance):
    assert isinstance(instance.none, bool)


@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes__property_type(instance):
    assert isinstance(instance._property, bool)


@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes__property_setter(instance):
    original = instance._property
    instance._property = original
    assert instance._property == original

@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_summary_type(instance):
    assert isinstance(instance.summary, bool)


@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_summary_setter(instance):
    original = instance.summary
    instance.summary = original
    assert instance.summary == original

@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_details_type(instance):
    assert isinstance(instance.details, bool)


@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_author_type(instance):
    assert isinstance(instance.author, bool)


@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_headline_type(instance):
    assert isinstance(instance.headline, bool)


@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_headline_setter(instance):
    original = instance.headline
    instance.headline = original
    assert instance.headline == original

@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_timesheet_type(instance):
    assert isinstance(instance.timesheet, bool)


@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_timesheet_setter(instance):
    original = instance.timesheet
    instance.timesheet = original
    assert instance.timesheet == original

@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_date_type(instance):
    assert isinstance(instance.date, bool)


@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_flags_type(instance):
    assert isinstance(instance.flags, bool)


@given(instance=project::JournalAttributes_strategy)
def test_project::journalattributes_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original

@given(instance=project::SortTasks_strategy)
@settings(max_examples=50)
def test_project::sorttasks_instantiation(instance):
    assert isinstance(instance, project::SortTasks)

@given(instance=project::Title_strategy)
@settings(max_examples=50)
def test_project::title_instantiation(instance):
    assert isinstance(instance, project::Title)

@given(instance=project::Title_strategy)
def test_project::title_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=project::Title_strategy)
def test_project::title_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=project::NumberFormat_strategy)
@settings(max_examples=50)
def test_project::numberformat_instantiation(instance):
    assert isinstance(instance, project::NumberFormat)

@given(instance=project::AccountRoot_strategy)
@settings(max_examples=50)
def test_project::accountroot_instantiation(instance):
    assert isinstance(instance, project::AccountRoot)

@given(instance=project::RollupAccount_strategy)
@settings(max_examples=50)
def test_project::rollupaccount_instantiation(instance):
    assert isinstance(instance, project::RollupAccount)

@given(instance=project::HideTask_strategy)
@settings(max_examples=50)
def test_project::hidetask_instantiation(instance):
    assert isinstance(instance, project::HideTask)

@given(instance=project::Header_strategy)
@settings(max_examples=50)
def test_project::header_instantiation(instance):
    assert isinstance(instance, project::Header)

@given(instance=project::TimeFormat_strategy)
@settings(max_examples=50)
def test_project::timeformat_instantiation(instance):
    assert isinstance(instance, project::TimeFormat)

@given(instance=project::TimeFormat_strategy)
def test_project::timeformat_timeformat_type(instance):
    assert isinstance(instance.timeformat, str)


@given(instance=project::TimeFormat_strategy)
def test_project::timeformat_timeformat_setter(instance):
    original = instance.timeformat
    instance.timeformat = original
    assert instance.timeformat == original

@given(instance=project::Footer_strategy)
@settings(max_examples=50)
def test_project::footer_instantiation(instance):
    assert isinstance(instance, project::Footer)

@given(instance=project::TaskRoot_strategy)
@settings(max_examples=50)
def test_project::taskroot_instantiation(instance):
    assert isinstance(instance, project::TaskRoot)

@given(instance=project::Headline_strategy)
@settings(max_examples=50)
def test_project::headline_instantiation(instance):
    assert isinstance(instance, project::Headline)

@given(instance=project::Columns_strategy)
@settings(max_examples=50)
def test_project::columns_instantiation(instance):
    assert isinstance(instance, project::Columns)

@given(instance=project::SortAccounts_strategy)
@settings(max_examples=50)
def test_project::sortaccounts_instantiation(instance):
    assert isinstance(instance, project::SortAccounts)

@given(instance=project::Prolog_strategy)
@settings(max_examples=50)
def test_project::prolog_instantiation(instance):
    assert isinstance(instance, project::Prolog)

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

@given(instance=project::Report_strategy)
@settings(max_examples=50)
def test_project::report_instantiation(instance):
    assert isinstance(instance, project::Report)

@given(instance=project::Report_strategy)
def test_project::report_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=project::Report_strategy)
def test_project::report_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project::Report_strategy)
def test_project::report_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=project::Report_strategy)
def test_project::report_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=project::TaskAttribute_strategy)
@settings(max_examples=50)
def test_project::taskattribute_instantiation(instance):
    assert isinstance(instance, project::TaskAttribute)

@given(instance=TaskAttribute_strategy)
@settings(max_examples=50)
def test_taskattribute_instantiation(instance):
    assert isinstance(instance, TaskAttribute)

@given(instance=project::Note_strategy)
@settings(max_examples=50)
def test_project::note_instantiation(instance):
    assert isinstance(instance, project::Note)

@given(instance=project::Note_strategy)
def test_project::note_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=project::Note_strategy)
def test_project::note_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=project::Milestone_strategy)
@settings(max_examples=50)
def test_project::milestone_instantiation(instance):
    assert isinstance(instance, project::Milestone)

@given(instance=project::Milestone_strategy)
def test_project::milestone_milestone_type(instance):
    assert isinstance(instance.milestone, bool)


@given(instance=project::Milestone_strategy)
def test_project::milestone_milestone_setter(instance):
    original = instance.milestone
    instance.milestone = original
    assert instance.milestone == original

@given(instance=project::BookingTask_strategy)
@settings(max_examples=50)
def test_project::bookingtask_instantiation(instance):
    assert isinstance(instance, project::BookingTask)

@given(instance=project::Duration_strategy)
@settings(max_examples=50)
def test_project::duration_instantiation(instance):
    assert isinstance(instance, project::Duration)

@given(instance=project::Depends_strategy)
@settings(max_examples=50)
def test_project::depends_instantiation(instance):
    assert isinstance(instance, project::Depends)

@given(instance=project::Warn_strategy)
@settings(max_examples=50)
def test_project::warn_instantiation(instance):
    assert isinstance(instance, project::Warn)

@given(instance=project::Scheduling_strategy)
@settings(max_examples=50)
def test_project::scheduling_instantiation(instance):
    assert isinstance(instance, project::Scheduling)

@given(instance=project::Scheduling_strategy)
def test_project::scheduling_scheduling_type(instance):
    assert isinstance(instance.scheduling, str)


@given(instance=project::Scheduling_strategy)
def test_project::scheduling_scheduling_setter(instance):
    original = instance.scheduling
    instance.scheduling = original
    assert instance.scheduling == original

@given(instance=project::Start_strategy)
@settings(max_examples=50)
def test_project::start_instantiation(instance):
    assert isinstance(instance, project::Start)

@given(instance=project::Start_strategy)
def test_project::start_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=project::Start_strategy)
def test_project::start_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=project::ProjectId_strategy)
@settings(max_examples=50)
def test_project::projectid_instantiation(instance):
    assert isinstance(instance, project::ProjectId)

@given(instance=project::ProjectId_strategy)
def test_project::projectid_projectId_type(instance):
    assert isinstance(instance.projectId, str)


@given(instance=project::ProjectId_strategy)
def test_project::projectid_projectId_setter(instance):
    original = instance.projectId
    instance.projectId = original
    assert instance.projectId == original

@given(instance=project::MinStart_strategy)
@settings(max_examples=50)
def test_project::minstart_instantiation(instance):
    assert isinstance(instance, project::MinStart)

@given(instance=project::MinStart_strategy)
def test_project::minstart_minStart_type(instance):
    assert isinstance(instance.minStart, str)


@given(instance=project::MinStart_strategy)
def test_project::minstart_minStart_setter(instance):
    original = instance.minStart
    instance.minStart = original
    assert instance.minStart == original

@given(instance=project::Allocate_strategy)
@settings(max_examples=50)
def test_project::allocate_instantiation(instance):
    assert isinstance(instance, project::Allocate)

@given(instance=project::Complete_strategy)
@settings(max_examples=50)
def test_project::complete_instantiation(instance):
    assert isinstance(instance, project::Complete)

@given(instance=project::Complete_strategy)
def test_project::complete_complete_type(instance):
    assert isinstance(instance.complete, float)


@given(instance=project::Complete_strategy)
def test_project::complete_complete_setter(instance):
    original = instance.complete
    instance.complete = original
    assert instance.complete == original

@given(instance=project::MinEnd_strategy)
@settings(max_examples=50)
def test_project::minend_instantiation(instance):
    assert isinstance(instance, project::MinEnd)

@given(instance=project::MinEnd_strategy)
def test_project::minend_minEnd_type(instance):
    assert isinstance(instance.minEnd, str)


@given(instance=project::MinEnd_strategy)
def test_project::minend_minEnd_setter(instance):
    original = instance.minEnd
    instance.minEnd = original
    assert instance.minEnd == original

@given(instance=project::MaxEnd_strategy)
@settings(max_examples=50)
def test_project::maxend_instantiation(instance):
    assert isinstance(instance, project::MaxEnd)

@given(instance=project::MaxEnd_strategy)
def test_project::maxend_maxEnd_type(instance):
    assert isinstance(instance.maxEnd, str)


@given(instance=project::MaxEnd_strategy)
def test_project::maxend_maxEnd_setter(instance):
    original = instance.maxEnd
    instance.maxEnd = original
    assert instance.maxEnd == original

@given(instance=project::Length_strategy)
@settings(max_examples=50)
def test_project::length_instantiation(instance):
    assert isinstance(instance, project::Length)

@given(instance=project::Charge_strategy)
@settings(max_examples=50)
def test_project::charge_instantiation(instance):
    assert isinstance(instance, project::Charge)

@given(instance=project::Charge_strategy)
def test_project::charge_applies_type(instance):
    assert isinstance(instance.applies, str)


@given(instance=project::Charge_strategy)
def test_project::charge_applies_setter(instance):
    original = instance.applies
    instance.applies = original
    assert instance.applies == original

@given(instance=project::Charge_strategy)
def test_project::charge_amount_type(instance):
    assert isinstance(instance.amount, float)


@given(instance=project::Charge_strategy)
def test_project::charge_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=project::JournalEntry_strategy)
@settings(max_examples=50)
def test_project::journalentry_instantiation(instance):
    assert isinstance(instance, project::JournalEntry)

@given(instance=project::JournalEntry_strategy)
def test_project::journalentry_headline_type(instance):
    assert isinstance(instance.headline, str)


@given(instance=project::JournalEntry_strategy)
def test_project::journalentry_headline_setter(instance):
    original = instance.headline
    instance.headline = original
    assert instance.headline == original

@given(instance=project::JournalEntry_strategy)
def test_project::journalentry_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=project::JournalEntry_strategy)
def test_project::journalentry_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=project::Precedes_strategy)
@settings(max_examples=50)
def test_project::precedes_instantiation(instance):
    assert isinstance(instance, project::Precedes)

@given(instance=project::PurgeTask_strategy)
@settings(max_examples=50)
def test_project::purgetask_instantiation(instance):
    assert isinstance(instance, project::PurgeTask)

@given(instance=project::PurgeTask_strategy)
def test_project::purgetask_listAttribute_type(instance):
    assert isinstance(instance.listAttribute, str)


@given(instance=project::PurgeTask_strategy)
def test_project::purgetask_listAttribute_setter(instance):
    original = instance.listAttribute
    instance.listAttribute = original
    assert instance.listAttribute == original

@given(instance=project::Priority_strategy)
@settings(max_examples=50)
def test_project::priority_instantiation(instance):
    assert isinstance(instance, project::Priority)

@given(instance=project::Priority_strategy)
def test_project::priority_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=project::Priority_strategy)
def test_project::priority_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=project::Responsible_strategy)
@settings(max_examples=50)
def test_project::responsible_instantiation(instance):
    assert isinstance(instance, project::Responsible)

@given(instance=project::End_strategy)
@settings(max_examples=50)
def test_project::end_instantiation(instance):
    assert isinstance(instance, project::End)

@given(instance=project::End_strategy)
def test_project::end_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=project::End_strategy)
def test_project::end_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=project::ShiftsTask_strategy)
@settings(max_examples=50)
def test_project::shiftstask_instantiation(instance):
    assert isinstance(instance, project::ShiftsTask)

@given(instance=project::ChargeSet_strategy)
@settings(max_examples=50)
def test_project::chargeset_instantiation(instance):
    assert isinstance(instance, project::ChargeSet)

@given(instance=project::Fail_strategy)
@settings(max_examples=50)
def test_project::fail_instantiation(instance):
    assert isinstance(instance, project::Fail)

@given(instance=project::Scheduled_strategy)
@settings(max_examples=50)
def test_project::scheduled_instantiation(instance):
    assert isinstance(instance, project::Scheduled)

@given(instance=project::Scheduled_strategy)
def test_project::scheduled_scheduled_type(instance):
    assert isinstance(instance.scheduled, bool)


@given(instance=project::Scheduled_strategy)
def test_project::scheduled_scheduled_setter(instance):
    original = instance.scheduled
    instance.scheduled = original
    assert instance.scheduled == original

@given(instance=project::Effort_strategy)
@settings(max_examples=50)
def test_project::effort_instantiation(instance):
    assert isinstance(instance, project::Effort)

@given(instance=project::ExtendedTaskAttribute_strategy)
@settings(max_examples=50)
def test_project::extendedtaskattribute_instantiation(instance):
    assert isinstance(instance, project::ExtendedTaskAttribute)

@given(instance=project::ExtendedTaskAttribute_strategy)
def test_project::extendedtaskattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=project::ExtendedTaskAttribute_strategy)
def test_project::extendedtaskattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project::MaxStart_strategy)
@settings(max_examples=50)
def test_project::maxstart_instantiation(instance):
    assert isinstance(instance, project::MaxStart)

@given(instance=project::MaxStart_strategy)
def test_project::maxstart_maxStart_type(instance):
    assert isinstance(instance.maxStart, str)


@given(instance=project::MaxStart_strategy)
def test_project::maxstart_maxStart_setter(instance):
    original = instance.maxStart
    instance.maxStart = original
    assert instance.maxStart == original

@given(instance=project::EndCredit_strategy)
@settings(max_examples=50)
def test_project::endcredit_instantiation(instance):
    assert isinstance(instance, project::EndCredit)

@given(instance=project::EndCredit_strategy)
def test_project::endcredit_credit_type(instance):
    assert isinstance(instance.credit, float)


@given(instance=project::EndCredit_strategy)
def test_project::endcredit_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original

@given(instance=project::Period_strategy)
@settings(max_examples=50)
def test_project::period_instantiation(instance):
    assert isinstance(instance, project::Period)

@given(instance=project::ProjectAttribute_strategy)
@settings(max_examples=50)
def test_project::projectattribute_instantiation(instance):
    assert isinstance(instance, project::ProjectAttribute)

@given(instance=project::Interval2_strategy)
@settings(max_examples=50)
def test_project::interval2_instantiation(instance):
    assert isinstance(instance, project::Interval2)

@given(instance=project::Interval2_strategy)
def test_project::interval2_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=project::Interval2_strategy)
def test_project::interval2_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=project::Interval2_strategy)
def test_project::interval2_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=project::Interval2_strategy)
def test_project::interval2_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=project::Global_strategy)
@settings(max_examples=50)
def test_project::global_instantiation(instance):
    assert isinstance(instance, project::Global)

@given(instance=IncludePropertiesAttribute_strategy)
@settings(max_examples=50)
def test_includepropertiesattribute_instantiation(instance):
    assert isinstance(instance, IncludePropertiesAttribute)

@given(instance=project::ReportPrefix_strategy)
@settings(max_examples=50)
def test_project::reportprefix_instantiation(instance):
    assert isinstance(instance, project::ReportPrefix)

@given(instance=project::ResourcePrefix_strategy)
@settings(max_examples=50)
def test_project::resourceprefix_instantiation(instance):
    assert isinstance(instance, project::ResourcePrefix)

@given(instance=project::TaskPrefix_strategy)
@settings(max_examples=50)
def test_project::taskprefix_instantiation(instance):
    assert isinstance(instance, project::TaskPrefix)

@given(instance=project::AccountPrefix_strategy)
@settings(max_examples=50)
def test_project::accountprefix_instantiation(instance):
    assert isinstance(instance, project::AccountPrefix)

@given(instance=project::AccountAttribute_strategy)
@settings(max_examples=50)
def test_project::accountattribute_instantiation(instance):
    assert isinstance(instance, project::AccountAttribute)

@given(instance=AccountAttribute_strategy)
@settings(max_examples=50)
def test_accountattribute_instantiation(instance):
    assert isinstance(instance, AccountAttribute)

@given(instance=project::Credit_strategy)
@settings(max_examples=50)
def test_project::credit_instantiation(instance):
    assert isinstance(instance, project::Credit)

@given(instance=project::Credit_strategy)
def test_project::credit_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=project::Credit_strategy)
def test_project::credit_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=project::Credit_strategy)
def test_project::credit_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=project::Credit_strategy)
def test_project::credit_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=project::Credit_strategy)
def test_project::credit_amount_type(instance):
    assert isinstance(instance.amount, float)


@given(instance=project::Credit_strategy)
def test_project::credit_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=project::IncludeProperties_strategy)
@settings(max_examples=50)
def test_project::includeproperties_instantiation(instance):
    assert isinstance(instance, project::IncludeProperties)

@given(instance=project::IncludeProperties_strategy)
def test_project::includeproperties_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=project::IncludeProperties_strategy)
def test_project::includeproperties_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=project::Export_strategy)
@settings(max_examples=50)
def test_project::export_instantiation(instance):
    assert isinstance(instance, project::Export)

@given(instance=project::Export_strategy)
def test_project::export_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=project::Export_strategy)
def test_project::export_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=project::Export_strategy)
def test_project::export_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=project::Export_strategy)
def test_project::export_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project::TimesheetReport_strategy)
@settings(max_examples=50)
def test_project::timesheetreport_instantiation(instance):
    assert isinstance(instance, project::TimesheetReport)

@given(instance=project::TimesheetReport_strategy)
def test_project::timesheetreport_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=project::TimesheetReport_strategy)
def test_project::timesheetreport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=project::Resource_strategy)
@settings(max_examples=50)
def test_project::resource_instantiation(instance):
    assert isinstance(instance, project::Resource)

@given(instance=project::Resource_strategy)
def test_project::resource_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=project::Resource_strategy)
def test_project::resource_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project::Resource_strategy)
def test_project::resource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=project::Resource_strategy)
def test_project::resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=project::TaskReport_strategy)
@settings(max_examples=50)
def test_project::taskreport_instantiation(instance):
    assert isinstance(instance, project::TaskReport)

@given(instance=project::Rate_strategy)
@settings(max_examples=50)
def test_project::rate_instantiation(instance):
    assert isinstance(instance, project::Rate)

@given(instance=project::Rate_strategy)
def test_project::rate_rate_type(instance):
    assert isinstance(instance.rate, float)


@given(instance=project::Rate_strategy)
def test_project::rate_rate_setter(instance):
    original = instance.rate
    instance.rate = original
    assert instance.rate == original

@given(instance=project::SupplementAccount_strategy)
@settings(max_examples=50)
def test_project::supplementaccount_instantiation(instance):
    assert isinstance(instance, project::SupplementAccount)

@given(instance=project::NikuReport_strategy)
@settings(max_examples=50)
def test_project::nikureport_instantiation(instance):
    assert isinstance(instance, project::NikuReport)

@given(instance=project::NikuReport_strategy)
def test_project::nikureport_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=project::NikuReport_strategy)
def test_project::nikureport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=project::Macro_strategy)
@settings(max_examples=50)
def test_project::macro_instantiation(instance):
    assert isinstance(instance, project::Macro)

@given(instance=project::Macro_strategy)
def test_project::macro_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=project::Macro_strategy)
def test_project::macro_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=project::TagFile_strategy)
@settings(max_examples=50)
def test_project::tagfile_instantiation(instance):
    assert isinstance(instance, project::TagFile)

@given(instance=project::TagFile_strategy)
def test_project::tagfile_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=project::TagFile_strategy)
def test_project::tagfile_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=project::TagFile_strategy)
def test_project::tagfile_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=project::TagFile_strategy)
def test_project::tagfile_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project::StatusSheetReport_strategy)
@settings(max_examples=50)
def test_project::statussheetreport_instantiation(instance):
    assert isinstance(instance, project::StatusSheetReport)

@given(instance=project::StatusSheetReport_strategy)
def test_project::statussheetreport_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=project::StatusSheetReport_strategy)
def test_project::statussheetreport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=project::AccountReport_strategy)
@settings(max_examples=50)
def test_project::accountreport_instantiation(instance):
    assert isinstance(instance, project::AccountReport)

@given(instance=project::TextReport_strategy)
@settings(max_examples=50)
def test_project::textreport_instantiation(instance):
    assert isinstance(instance, project::TextReport)

@given(instance=project::StatusSheet_strategy)
@settings(max_examples=50)
def test_project::statussheet_instantiation(instance):
    assert isinstance(instance, project::StatusSheet)

@given(instance=project::Balance_strategy)
@settings(max_examples=50)
def test_project::balance_instantiation(instance):
    assert isinstance(instance, project::Balance)

@given(instance=project::Navigator_strategy)
@settings(max_examples=50)
def test_project::navigator_instantiation(instance):
    assert isinstance(instance, project::Navigator)

@given(instance=project::Navigator_strategy)
def test_project::navigator_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=project::Navigator_strategy)
def test_project::navigator_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project::Timesheet_strategy)
@settings(max_examples=50)
def test_project::timesheet_instantiation(instance):
    assert isinstance(instance, project::Timesheet)

@given(instance=project::Shift_strategy)
@settings(max_examples=50)
def test_project::shift_instantiation(instance):
    assert isinstance(instance, project::Shift)

@given(instance=project::Shift_strategy)
def test_project::shift_timezone_type(instance):
    assert isinstance(instance.timezone, str)


@given(instance=project::Shift_strategy)
def test_project::shift_timezone_setter(instance):
    original = instance.timezone
    instance.timezone = original
    assert instance.timezone == original

@given(instance=project::Shift_strategy)
def test_project::shift_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=project::Shift_strategy)
def test_project::shift_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project::Shift_strategy)
def test_project::shift_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=project::Shift_strategy)
def test_project::shift_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=project::Shift_strategy)
def test_project::shift_replace_type(instance):
    assert isinstance(instance.replace, str)


@given(instance=project::Shift_strategy)
def test_project::shift_replace_setter(instance):
    original = instance.replace
    instance.replace = original
    assert instance.replace == original

@given(instance=project::SupplementTask_strategy)
@settings(max_examples=50)
def test_project::supplementtask_instantiation(instance):
    assert isinstance(instance, project::SupplementTask)

@given(instance=project::SupplementResource_strategy)
@settings(max_examples=50)
def test_project::supplementresource_instantiation(instance):
    assert isinstance(instance, project::SupplementResource)

@given(instance=project::ResourceReport_strategy)
@settings(max_examples=50)
def test_project::resourcereport_instantiation(instance):
    assert isinstance(instance, project::ResourceReport)

@given(instance=project::Copyright_strategy)
@settings(max_examples=50)
def test_project::copyright_instantiation(instance):
    assert isinstance(instance, project::Copyright)

@given(instance=project::Copyright_strategy)
def test_project::copyright_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=project::Copyright_strategy)
def test_project::copyright_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=project::Task_strategy)
@settings(max_examples=50)
def test_project::task_instantiation(instance):
    assert isinstance(instance, project::Task)

@given(instance=project::Task_strategy)
def test_project::task_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=project::Task_strategy)
def test_project::task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=project::Task_strategy)
def test_project::task_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=project::Task_strategy)
def test_project::task_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project::IcalReport_strategy)
@settings(max_examples=50)
def test_project::icalreport_instantiation(instance):
    assert isinstance(instance, project::IcalReport)

@given(instance=project::IcalReport_strategy)
def test_project::icalreport_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=project::IcalReport_strategy)
def test_project::icalreport_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=project::Flags_strategy)
@settings(max_examples=50)
def test_project::flags_instantiation(instance):
    assert isinstance(instance, project::Flags)

@given(instance=project::Flags_strategy)
def test_project::flags_flags_type(instance):
    assert isinstance(instance.flags, str)


@given(instance=project::Flags_strategy)
def test_project::flags_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original

@given(instance=project::Vacation_strategy)
@settings(max_examples=50)
def test_project::vacation_instantiation(instance):
    assert isinstance(instance, project::Vacation)

@given(instance=project::Vacation_strategy)
def test_project::vacation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=project::Vacation_strategy)
def test_project::vacation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=project::ProjectIds_strategy)
@settings(max_examples=50)
def test_project::projectids_instantiation(instance):
    assert isinstance(instance, project::ProjectIds)

@given(instance=project::ProjectIds_strategy)
def test_project::projectids_ids_type(instance):
    assert isinstance(instance.ids, str)


@given(instance=project::ProjectIds_strategy)
def test_project::projectids_ids_setter(instance):
    original = instance.ids
    instance.ids = original
    assert instance.ids == original

@given(instance=project::SupplementReport_strategy)
@settings(max_examples=50)
def test_project::supplementreport_instantiation(instance):
    assert isinstance(instance, project::SupplementReport)

@given(instance=project::Limits_strategy)
@settings(max_examples=50)
def test_project::limits_instantiation(instance):
    assert isinstance(instance, project::Limits)

@given(instance=project::Account_strategy)
@settings(max_examples=50)
def test_project::account_instantiation(instance):
    assert isinstance(instance, project::Account)

@given(instance=project::Account_strategy)
def test_project::account_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=project::Account_strategy)
def test_project::account_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=project::Account_strategy)
def test_project::account_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=project::Account_strategy)
def test_project::account_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project::Property_strategy)
@settings(max_examples=50)
def test_project::property_instantiation(instance):
    assert isinstance(instance, project::Property)

@given(instance=project::Project_strategy)
@settings(max_examples=50)
def test_project::project_instantiation(instance):
    assert isinstance(instance, project::Project)

@given(instance=project::Project_strategy)
def test_project::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=project::Project_strategy)
def test_project::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=project::Project_strategy)
def test_project::project_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=project::Project_strategy)
def test_project::project_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=project::Project_strategy)
def test_project::project_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=project::Project_strategy)
def test_project::project_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original
