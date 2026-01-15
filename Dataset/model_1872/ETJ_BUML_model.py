####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
LeaveType: Enumeration = Enumeration(
    name="LeaveType",
    literals={
            EnumerationLiteral(name="project"),
			EnumerationLiteral(name="annual"),
			EnumerationLiteral(name="special"),
			EnumerationLiteral(name="sick"),
			EnumerationLiteral(name="unpaid"),
			EnumerationLiteral(name="holiday"),
			EnumerationLiteral(name="unemployed")
    }
)

BuildInMacro: Enumeration = Enumeration(
    name="BuildInMacro",
    literals={
            EnumerationLiteral(name="projectstart"),
			EnumerationLiteral(name="projectend"),
			EnumerationLiteral(name="now")
    }
)

JournalAttributeValues: Enumeration = Enumeration(
    name="JournalAttributeValues",
    literals={
            EnumerationLiteral(name="ALL"),
			EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="alert"),
			EnumerationLiteral(name="author"),
			EnumerationLiteral(name="date"),
			EnumerationLiteral(name="details"),
			EnumerationLiteral(name="flags"),
			EnumerationLiteral(name="headline"),
			EnumerationLiteral(name="property"),
			EnumerationLiteral(name="propertyid"),
			EnumerationLiteral(name="summary"),
			EnumerationLiteral(name="timesheet")
    }
)

PurgeReportAttribute: Enumeration = Enumeration(
    name="PurgeReportAttribute",
    literals={
            EnumerationLiteral(name="SORTRESOURCES"),
			EnumerationLiteral(name="SORTTASKS"),
			EnumerationLiteral(name="COLUMNS"),
			EnumerationLiteral(name="DEFINITIONS"),
			EnumerationLiteral(name="FLAGS"),
			EnumerationLiteral(name="FORMATS"),
			EnumerationLiteral(name="JOURNALATTRIBUTES"),
			EnumerationLiteral(name="SCENARIOS"),
			EnumerationLiteral(name="SORTACCOUNTS"),
			EnumerationLiteral(name="SORTJOURNALENTRIES")
    }
)

PurgeResourceAttribute: Enumeration = Enumeration(
    name="PurgeResourceAttribute",
    literals={
            EnumerationLiteral(name="FAIL"),
			EnumerationLiteral(name="FLAGS"),
			EnumerationLiteral(name="MANAGERS"),
			EnumerationLiteral(name="REPORTS"),
			EnumerationLiteral(name="VACATIONS"),
			EnumerationLiteral(name="WARN")
    }
)

PurgeTaskAttribute: Enumeration = Enumeration(
    name="PurgeTaskAttribute",
    literals={
            EnumerationLiteral(name="BOOKING"),
			EnumerationLiteral(name="CHARGE"),
			EnumerationLiteral(name="CHARGESET"),
			EnumerationLiteral(name="DEPENDS"),
			EnumerationLiteral(name="FAIL"),
			EnumerationLiteral(name="FLAGS"),
			EnumerationLiteral(name="PRECEDES"),
			EnumerationLiteral(name="WARN")
    }
)

ChargeApplies: Enumeration = Enumeration(
    name="ChargeApplies",
    literals={
            EnumerationLiteral(name="ONSTART"),
			EnumerationLiteral(name="ONEND"),
			EnumerationLiteral(name="PERHOUR"),
			EnumerationLiteral(name="PERDAY"),
			EnumerationLiteral(name="PERWEEK")
    }
)

JournalModeValue: Enumeration = Enumeration(
    name="JournalModeValue",
    literals={
            EnumerationLiteral(name="JOURNAL"),
			EnumerationLiteral(name="JOURNAL_SUB"),
			EnumerationLiteral(name="STATUS_DOWN"),
			EnumerationLiteral(name="STATUS_UP"),
			EnumerationLiteral(name="ALERTS_DOWN")
    }
)

JournalEntrySortCriterion: Enumeration = Enumeration(
    name="JournalEntrySortCriterion",
    literals={
            EnumerationLiteral(name="DATE_DOWN"),
			EnumerationLiteral(name="DATE_UP"),
			EnumerationLiteral(name="ALERT_DOWN"),
			EnumerationLiteral(name="ALERT_UP"),
			EnumerationLiteral(name="PROPERTY_UP")
    }
)

ListTypeValues: Enumeration = Enumeration(
    name="ListTypeValues",
    literals={
            EnumerationLiteral(name="BULLETS"),
			EnumerationLiteral(name="COMMA"),
			EnumerationLiteral(name="NUMBERED")
    }
)

Justification: Enumeration = Enumeration(
    name="Justification",
    literals={
            EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="RIGHT"),
			EnumerationLiteral(name="LEFT")
    }
)

ReportFormat: Enumeration = Enumeration(
    name="ReportFormat",
    literals={
            EnumerationLiteral(name="CSV"),
			EnumerationLiteral(name="HTML"),
			EnumerationLiteral(name="NIKU")
    }
)

LoadDisplayUnit: Enumeration = Enumeration(
    name="LoadDisplayUnit",
    literals={
            EnumerationLiteral(name="DAYS"),
			EnumerationLiteral(name="HOURS"),
			EnumerationLiteral(name="LONGAUTO"),
			EnumerationLiteral(name="MINUTES"),
			EnumerationLiteral(name="MONTHS"),
			EnumerationLiteral(name="SHORTAUTO"),
			EnumerationLiteral(name="WEEKS"),
			EnumerationLiteral(name="YEARS")
    }
)

ScaleResolution: Enumeration = Enumeration(
    name="ScaleResolution",
    literals={
            EnumerationLiteral(name="HOUR"),
			EnumerationLiteral(name="DAY"),
			EnumerationLiteral(name="WEEK"),
			EnumerationLiteral(name="MONTH"),
			EnumerationLiteral(name="QUARTER"),
			EnumerationLiteral(name="YEAR")
    }
)

CriterionDirection: Enumeration = Enumeration(
    name="CriterionDirection",
    literals={
            EnumerationLiteral(name="UP"),
			EnumerationLiteral(name="DOWN")
    }
)

YesNo: Enumeration = Enumeration(
    name="YesNo",
    literals={
            EnumerationLiteral(name="NO"),
			EnumerationLiteral(name="YES")
    }
)

ColumnId: Enumeration = Enumeration(
    name="ColumnId",
    literals={
            EnumerationLiteral(name="activetasks"),
			EnumerationLiteral(name="annualleave"),
			EnumerationLiteral(name="annualleavebalance"),
			EnumerationLiteral(name="alert"),
			EnumerationLiteral(name="alertmessages"),
			EnumerationLiteral(name="alertsummaries"),
			EnumerationLiteral(name="alerttrend"),
			EnumerationLiteral(name="balance"),
			EnumerationLiteral(name="bsi"),
			EnumerationLiteral(name="chart"),
			EnumerationLiteral(name="children"),
			EnumerationLiteral(name="daily"),
			EnumerationLiteral(name="directreports"),
			EnumerationLiteral(name="duration"),
			EnumerationLiteral(name="duties"),
			EnumerationLiteral(name="efficiency"),
			EnumerationLiteral(name="effort"),
			EnumerationLiteral(name="effortdone"),
			EnumerationLiteral(name="effortleft"),
			EnumerationLiteral(name="email"),
			EnumerationLiteral(name="end"),
			EnumerationLiteral(name="flags"),
			EnumerationLiteral(name="followers"),
			EnumerationLiteral(name="freetime"),
			EnumerationLiteral(name="freework"),
			EnumerationLiteral(name="fte"),
			EnumerationLiteral(name="closedtasks"),
			EnumerationLiteral(name="competitorcount"),
			EnumerationLiteral(name="competitors"),
			EnumerationLiteral(name="complete"),
			EnumerationLiteral(name="completed"),
			EnumerationLiteral(name="criticalness"),
			EnumerationLiteral(name="cost"),
			EnumerationLiteral(name="journalmessages"),
			EnumerationLiteral(name="journalsummaries"),
			EnumerationLiteral(name="line"),
			EnumerationLiteral(name="managers"),
			EnumerationLiteral(name="maxend"),
			EnumerationLiteral(name="maxstart"),
			EnumerationLiteral(name="minend"),
			EnumerationLiteral(name="minstart"),
			EnumerationLiteral(name="monthly"),
			EnumerationLiteral(name="no"),
			EnumerationLiteral(name="name"),
			EnumerationLiteral(name="note"),
			EnumerationLiteral(name="opentasks"),
			EnumerationLiteral(name="pathcriticalness"),
			EnumerationLiteral(name="precursors"),
			EnumerationLiteral(name="priority"),
			EnumerationLiteral(name="quarterly"),
			EnumerationLiteral(name="gauge"),
			EnumerationLiteral(name="rate"),
			EnumerationLiteral(name="headcount"),
			EnumerationLiteral(name="reports"),
			EnumerationLiteral(name="hierarchindex"),
			EnumerationLiteral(name="hourly"),
			EnumerationLiteral(name="id"),
			EnumerationLiteral(name="index"),
			EnumerationLiteral(name="inputs"),
			EnumerationLiteral(name="journal"),
			EnumerationLiteral(name="journal_sub"),
			EnumerationLiteral(name="specialleave"),
			EnumerationLiteral(name="start"),
			EnumerationLiteral(name="status"),
			EnumerationLiteral(name="targets"),
			EnumerationLiteral(name="turnover"),
			EnumerationLiteral(name="wbs"),
			EnumerationLiteral(name="unpaidleave"),
			EnumerationLiteral(name="weekly"),
			EnumerationLiteral(name="yearly"),
			EnumerationLiteral(name="resources"),
			EnumerationLiteral(name="responsible"),
			EnumerationLiteral(name="revenue"),
			EnumerationLiteral(name="scenario"),
			EnumerationLiteral(name="scheduling"),
			EnumerationLiteral(name="seqno"),
			EnumerationLiteral(name="sickleave")
    }
)

SelectArgument: Enumeration = Enumeration(
    name="SelectArgument",
    literals={
            EnumerationLiteral(name="MINALLOCATED"),
			EnumerationLiteral(name="ORDER"),
			EnumerationLiteral(name="RANDOM"),
			EnumerationLiteral(name="MAXLOADED"),
			EnumerationLiteral(name="MINLOADED")
    }
)

AlertLevel: Enumeration = Enumeration(
    name="AlertLevel",
    literals={
            EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="YELLOW"),
			EnumerationLiteral(name="GREEN")
    }
)

DependsPolicy: Enumeration = Enumeration(
    name="DependsPolicy",
    literals={
            EnumerationLiteral(name="ONEND"),
			EnumerationLiteral(name="ONSTART")
    }
)

SchedulingPolicy: Enumeration = Enumeration(
    name="SchedulingPolicy",
    literals={
            EnumerationLiteral(name="ALAP"),
			EnumerationLiteral(name="ASAP")
    }
)

TimeUnit: Enumeration = Enumeration(
    name="TimeUnit",
    literals={
            EnumerationLiteral(name="MINUTE"),
			EnumerationLiteral(name="HOUR"),
			EnumerationLiteral(name="DAY"),
			EnumerationLiteral(name="WEEK"),
			EnumerationLiteral(name="MONTH"),
			EnumerationLiteral(name="YEAR")
    }
)

WorkQuantityUnit: Enumeration = Enumeration(
    name="WorkQuantityUnit",
    literals={
            EnumerationLiteral(name="PERCENT"),
			EnumerationLiteral(name="MINUTES"),
			EnumerationLiteral(name="HOURS"),
			EnumerationLiteral(name="DAYS")
    }
)

Weekday: Enumeration = Enumeration(
    name="Weekday",
    literals={
            EnumerationLiteral(name="WED"),
			EnumerationLiteral(name="THR"),
			EnumerationLiteral(name="FRI"),
			EnumerationLiteral(name="SAT"),
			EnumerationLiteral(name="SUN"),
			EnumerationLiteral(name="MON"),
			EnumerationLiteral(name="TUE")
    }
)

# Classes
eTJ_Global = Class(name="eTJ::Global")
eTJ_Project = Class(name="eTJ::Project")
eTJ_Property = Class(name="eTJ::Property")
eTJ_Leaves = Class(name="eTJ::Leaves")
Property_ = Class(name="Property")
ResourceAttribute = Class(name="ResourceAttribute")
eTJ_LeaveDetails = Class(name="eTJ::LeaveDetails")
eTJ_Interval3 = Class(name="eTJ::Interval3")
eTJ_Account = Class(name="eTJ::Account")
AccountAttribute = Class(name="AccountAttribute")
eTJ_AccountAttribute = Class(name="eTJ::AccountAttribute")
eTJ_AccountPrefix = Class(name="eTJ::AccountPrefix")
IncludePropertiesAttribute = Class(name="IncludePropertiesAttribute")
eTJ_AccountReport = Class(name="eTJ::AccountReport")
ReportAttribute = Class(name="ReportAttribute")
eTJ_AccountRoot = Class(name="eTJ::AccountRoot")
eTJ_Interval2 = Class(name="eTJ::Interval2")
eTJ_ProjectAttribute = Class(name="eTJ::ProjectAttribute")
eTJ_Task = Class(name="eTJ::Task")
eTJ_TaskAttribute = Class(name="eTJ::TaskAttribute")
eTJ_ReportAttribute = Class(name="eTJ::ReportAttribute")
eTJ_Scenario = Class(name="eTJ::Scenario")
eTJ_EObject = Class(name="eTJ::EObject")
eTJ_MacroCall = Class(name="eTJ::MacroCall")
End = Class(name="End")
Start = Class(name="Start")
ExtDate = Class(name="ExtDate")
eTJ_Macro = Class(name="eTJ::Macro")
eTJ_Report = Class(name="eTJ::Report")
AccountReport = Class(name="AccountReport")
ResourceReport = Class(name="ResourceReport")
TaskReport = Class(name="TaskReport")
TextReport = Class(name="TextReport")
eTJ_ResourceAttribute = Class(name="eTJ::ResourceAttribute")
eTJ_IcalReport = Class(name="eTJ::IcalReport")
eTJ_IcalReportAttribute = Class(name="eTJ::IcalReportAttribute")
eTJ_Export = Class(name="eTJ::Export")
eTJ_ExportAttribute = Class(name="eTJ::ExportAttribute")
eTJ_Resource = Class(name="eTJ::Resource")
eTJ_Allocate = Class(name="eTJ::Allocate")
eTJ_AllocateResource = Class(name="eTJ::AllocateResource")
eTJ_AllocateResourceAttribute = Class(name="eTJ::AllocateResourceAttribute")
eTJ_Navigator = Class(name="eTJ::Navigator")
eTJ_NavigatorAttribute = Class(name="eTJ::NavigatorAttribute")
eTJ_NewTask = Class(name="eTJ::NewTask")
TimesheetAttribute = Class(name="TimesheetAttribute")
eTJ_Balance = Class(name="eTJ::Balance")
eTJ_NewTaskAttribute = Class(name="eTJ::NewTaskAttribute")
eTJ_NikuReport = Class(name="eTJ::NikuReport")
eTJ_NikuReportAttribute = Class(name="eTJ::NikuReportAttribute")
eTJ_Alert = Class(name="eTJ::Alert")
eTJ_Alternative = Class(name="eTJ::Alternative")
AllocateResourceAttribute = Class(name="AllocateResourceAttribute")
eTJ_Author = Class(name="eTJ::Author")
StatusStatusSheetAttribute = Class(name="StatusStatusSheetAttribute")
eTJ_Caption = Class(name="eTJ::Caption")
eTJ_Booking = Class(name="eTJ::Booking")
eTJ_Interval4 = Class(name="eTJ::Interval4")
eTJ_BookingTask = Class(name="eTJ::BookingTask")
eTJ_BookingResource = Class(name="eTJ::BookingResource")
eTJ_Columns = Class(name="eTJ::Columns")
eTJ_Column = Class(name="eTJ::Column")
eTJ_CellColor = Class(name="eTJ::CellColor")
ColumnAttribute = Class(name="ColumnAttribute")
eTJ_LogicalExpression = Class(name="eTJ::LogicalExpression")
eTJ_RGB = Class(name="eTJ::RGB")
eTJ_CellText = Class(name="eTJ::CellText")
eTJ_Center = Class(name="eTJ::Center")
eTJ_Charge = Class(name="eTJ::Charge")
eTJ_ChargeSet = Class(name="eTJ::ChargeSet")
eTJ_AccountShare = Class(name="eTJ::AccountShare")
eTJ_DailyMin = Class(name="eTJ::DailyMin")
eTJ_Complete = Class(name="eTJ::Complete")
eTJ_Copyright = Class(name="eTJ::Copyright")
eTJ_Credit = Class(name="eTJ::Credit")
eTJ_ISODATE = Class(name="eTJ::ISODATE")
eTJ_Currency = Class(name="eTJ::Currency")
ProjectAttribute = Class(name="ProjectAttribute")
eTJ_CurrencyFormat = Class(name="eTJ::CurrencyFormat")
eTJ_DailyMax = Class(name="eTJ::DailyMax")
LimitsAttribute = Class(name="LimitsAttribute")
eTJ_DailyWorkingHours = Class(name="eTJ::DailyWorkingHours")
eTJ_Email = Class(name="eTJ::Email")
eTJ_Definitions = Class(name="eTJ::Definitions")
ExportAttribute = Class(name="ExportAttribute")
eTJ_Depends = Class(name="eTJ::Depends")
eTJ_TaskDependency = Class(name="eTJ::TaskDependency")
eTJ_Details = Class(name="eTJ::Details")
StatusTimesheetAttribute = Class(name="StatusTimesheetAttribute")
eTJ_Duration = Class(name="eTJ::Duration")
eTJ_DurationQuantity = Class(name="eTJ::DurationQuantity")
eTJ_Efficiency = Class(name="eTJ::Efficiency")
eTJ_Effort = Class(name="eTJ::Effort")
eTJ_ExtendResource = Class(name="eTJ::ExtendResource")
eTJ_End = Class(name="eTJ::End")
IcalReportAttribute = Class(name="IcalReportAttribute")
NewTaskAttribute = Class(name="NewTaskAttribute")
NikuReportAttribute = Class(name="NikuReportAttribute")
StatusSheetReportAttribute = Class(name="StatusSheetReportAttribute")
TaskTimesheetAttribute = Class(name="TaskTimesheetAttribute")
TimesheetReportAttribute = Class(name="TimesheetReportAttribute")
eTJ_EndCredit = Class(name="eTJ::EndCredit")
eTJ_Epilog = Class(name="eTJ::Epilog")
eTJ_Extend = Class(name="eTJ::Extend")
eTJ_ExtendedResourceAttribute = Class(name="eTJ::ExtendedResourceAttribute")
eTJ_ExtendTask = Class(name="eTJ::ExtendTask")
eTJ_ExtendedTaskAttribute = Class(name="eTJ::ExtendedTaskAttribute")
eTJ_Fail = Class(name="eTJ::Fail")
eTJ_Flags = Class(name="eTJ::Flags")
eTJ_FontColor = Class(name="eTJ::FontColor")
eTJ_Footer = Class(name="eTJ::Footer")
eTJ_Formats = Class(name="eTJ::Formats")
eTJ_Function = Class(name="eTJ::Function")
eTJ_GapDuration = Class(name="eTJ::GapDuration")
eTJ_GapLength = Class(name="eTJ::GapLength")
eTJ_HAlign = Class(name="eTJ::HAlign")
eTJ_Header = Class(name="eTJ::Header")
eTJ_Headline = Class(name="eTJ::Headline")
eTJ_HideAccount = Class(name="eTJ::HideAccount")
eTJ_HideJournalEntry = Class(name="eTJ::HideJournalEntry")
eTJ_HideReport = Class(name="eTJ::HideReport")
NavigatorAttribute = Class(name="NavigatorAttribute")
eTJ_HideResource = Class(name="eTJ::HideResource")
eTJ_HideTask = Class(name="eTJ::HideTask")
eTJ_Include = Class(name="eTJ::Include")
eTJ_IncludeProperties = Class(name="eTJ::IncludeProperties")
eTJ_IncludePropertiesAttribute = Class(name="eTJ::IncludePropertiesAttribute")
eTJ_Interval1 = Class(name="eTJ::Interval1")
eTJ_JournalAttributes = Class(name="eTJ::JournalAttributes")
eTJ_JournalEntry = Class(name="eTJ::JournalEntry")
eTJ_Summary = Class(name="eTJ::Summary")
eTJ_JournalMode = Class(name="eTJ::JournalMode")
eTJ_Left = Class(name="eTJ::Left")
eTJ_Length = Class(name="eTJ::Length")
eTJ_Limits = Class(name="eTJ::Limits")
eTJ_LimitsAttribute = Class(name="eTJ::LimitsAttribute")
eTJ_ListItem = Class(name="eTJ::ListItem")
eTJ_ListType = Class(name="eTJ::ListType")
eTJ_Mandatory = Class(name="eTJ::Mandatory")
eTJ_LoadUnit = Class(name="eTJ::LoadUnit")
eTJ_Managers = Class(name="eTJ::Managers")
eTJ_MonthlyMin = Class(name="eTJ::MonthlyMin")
eTJ_MaxEnd = Class(name="eTJ::MaxEnd")
eTJ_Maximum = Class(name="eTJ::Maximum")
eTJ_MaxStart = Class(name="eTJ::MaxStart")
eTJ_Milestone = Class(name="eTJ::Milestone")
eTJ_Minimum = Class(name="eTJ::Minimum")
eTJ_MinEnd = Class(name="eTJ::MinEnd")
eTJ_MinStart = Class(name="eTJ::MinStart")
eTJ_MonthlyMax = Class(name="eTJ::MonthlyMax")
eTJ_Precedes = Class(name="eTJ::Precedes")
eTJ_Priority = Class(name="eTJ::Priority")
eTJ_Note = Class(name="eTJ::Note")
eTJ_Now = Class(name="eTJ::Now")
eTJ_NumberFormat = Class(name="eTJ::NumberFormat")
eTJ_Period = Class(name="eTJ::Period")
eTJ_Persistent = Class(name="eTJ::Persistent")
eTJ_PurgeResource = Class(name="eTJ::PurgeResource")
eTJ_ProjectId = Class(name="eTJ::ProjectId")
eTJ_ProjectIds = Class(name="eTJ::ProjectIds")
eTJ_Prolog = Class(name="eTJ::Prolog")
eTJ_PurgeReport = Class(name="eTJ::PurgeReport")
eTJ_Rate = Class(name="eTJ::Rate")
eTJ_Remaining = Class(name="eTJ::Remaining")
eTJ_PurgeTask = Class(name="eTJ::PurgeTask")
eTJ_ResourceReport = Class(name="eTJ::ResourceReport")
eTJ_ResourceRoot = Class(name="eTJ::ResourceRoot")
eTJ_ReportPrefix = Class(name="eTJ::ReportPrefix")
eTJ_ResourceAttributes = Class(name="eTJ::ResourceAttributes")
eTJ_ResourcePrefix = Class(name="eTJ::ResourcePrefix")
eTJ_Responsible = Class(name="eTJ::Responsible")
eTJ_Right = Class(name="eTJ::Right")
eTJ_RollupAccount = Class(name="eTJ::RollupAccount")
eTJ_RollupResource = Class(name="eTJ::RollupResource")
eTJ_ScenarioIcal = Class(name="eTJ::ScenarioIcal")
eTJ_RollupTask = Class(name="eTJ::RollupTask")
eTJ_Scale = Class(name="eTJ::Scale")
eTJ_Scenarios = Class(name="eTJ::Scenarios")
eTJ_Scheduled = Class(name="eTJ::Scheduled")
eTJ_Scheduling = Class(name="eTJ::Scheduling")
eTJ_Select = Class(name="eTJ::Select")
eTJ_SelfContained = Class(name="eTJ::SelfContained")
eTJ_Shift = Class(name="eTJ::Shift")
eTJ_Vacation = Class(name="eTJ::Vacation")
eTJ_WorkingHours = Class(name="eTJ::WorkingHours")
eTJ_ShiftTimesheet = Class(name="eTJ::ShiftTimesheet")
eTJ_Shifts = Class(name="eTJ::Shifts")
ShiftsResource = Class(name="ShiftsResource")
ShiftsTask = Class(name="ShiftsTask")
eTJ_ShiftsLimit = Class(name="eTJ::ShiftsLimit")
eTJ_Criterion = Class(name="eTJ::Criterion")
eTJ_ShiftsAllocate = Class(name="eTJ::ShiftsAllocate")
eTJ_ShiftsResource = Class(name="eTJ::ShiftsResource")
eTJ_ShiftsTask = Class(name="eTJ::ShiftsTask")
eTJ_ShortTimeFormat = Class(name="eTJ::ShortTimeFormat")
eTJ_Sort = Class(name="eTJ::Sort")
SortAccounts = Class(name="SortAccounts")
SortJournalEntries = Class(name="SortJournalEntries")
SortResources = Class(name="SortResources")
eTJ_StatusStatusSheet = Class(name="eTJ::StatusStatusSheet")
TaskStatusSheetAttribute = Class(name="TaskStatusSheetAttribute")
SortTasks = Class(name="SortTasks")
eTJ_SortAccounts = Class(name="eTJ::SortAccounts")
eTJ_SortJournalEntries = Class(name="eTJ::SortJournalEntries")
eTJ_SortResources = Class(name="eTJ::SortResources")
eTJ_SortTasks = Class(name="eTJ::SortTasks")
eTJ_Start = Class(name="eTJ::Start")
eTJ_StatusSheetAttribute = Class(name="eTJ::StatusSheetAttribute")
eTJ_StatusStatusSheetAttribute = Class(name="eTJ::StatusStatusSheetAttribute")
eTJ_StatusTimesheet = Class(name="eTJ::StatusTimesheet")
eTJ_StatusTimesheetAttribute = Class(name="eTJ::StatusTimesheetAttribute")
eTJ_StatusSheet = Class(name="eTJ::StatusSheet")
eTJ_SupplementResource = Class(name="eTJ::SupplementResource")
eTJ_StatusSheetReport = Class(name="eTJ::StatusSheetReport")
eTJ_StatusSheetReportAttribute = Class(name="eTJ::StatusSheetReportAttribute")
eTJ_SupplementAccount = Class(name="eTJ::SupplementAccount")
eTJ_SupplementReport = Class(name="eTJ::SupplementReport")
eTJ_SupplementTask = Class(name="eTJ::SupplementTask")
eTJ_TagFile = Class(name="eTJ::TagFile")
eTJ_TaskStatusSheet = Class(name="eTJ::TaskStatusSheet")
StatusSheetAttribute = Class(name="StatusSheetAttribute")
eTJ_TaskStatusSheetAttribute = Class(name="eTJ::TaskStatusSheetAttribute")
eTJ_TaskTimesheet = Class(name="eTJ::TaskTimesheet")
eTJ_TaskTimesheetAttribute = Class(name="eTJ::TaskTimesheetAttribute")
eTJ_TaskAttributes = Class(name="eTJ::TaskAttributes")
eTJ_Timesheet = Class(name="eTJ::Timesheet")
eTJ_TaskPrefix = Class(name="eTJ::TaskPrefix")
eTJ_TaskReport = Class(name="eTJ::TaskReport")
eTJ_TaskRoot = Class(name="eTJ::TaskRoot")
eTJ_TextReport = Class(name="eTJ::TextReport")
eTJ_TimeFormat = Class(name="eTJ::TimeFormat")
eTJ_Timeoff = Class(name="eTJ::Timeoff")
eTJ_TimingResolution = Class(name="eTJ::TimingResolution")
eTJ_TimesheetAttribute = Class(name="eTJ::TimesheetAttribute")
eTJ_TimesheetReport = Class(name="eTJ::TimesheetReport")
eTJ_TimesheetReportAttribute = Class(name="eTJ::TimesheetReportAttribute")
eTJ_Timezone = Class(name="eTJ::Timezone")
eTJ_Title = Class(name="eTJ::Title")
eTJ_Warn = Class(name="eTJ::Warn")
eTJ_ToolTip = Class(name="eTJ::ToolTip")
eTJ_WeekStarts = Class(name="eTJ::WeekStarts")
eTJ_WeeklyMax = Class(name="eTJ::WeeklyMax")
eTJ_TrackingScenario = Class(name="eTJ::TrackingScenario")
eTJ_TreeLevel = Class(name="eTJ::TreeLevel")
eTJ_Weekdays = Class(name="eTJ::Weekdays")
eTJ_WorkHours = Class(name="eTJ::WorkHours")
eTJ_YearlyWorkingDays = Class(name="eTJ::YearlyWorkingDays")
eTJ_WeeklyMin = Class(name="eTJ::WeeklyMin")
eTJ_Width = Class(name="eTJ::Width")
eTJ_Work = Class(name="eTJ::Work")
GapDuration = Class(name="GapDuration")
GapLength = Class(name="GapLength")
eTJ_ColumnAttribute = Class(name="eTJ::ColumnAttribute")
eTJ_ExtendedResourceAttributeColumn = Class(name="eTJ::ExtendedResourceAttributeColumn")
eTJ_LimitAttribute = Class(name="eTJ::LimitAttribute")
eTJ_Limit = Class(name="eTJ::Limit")
DailyMax = Class(name="DailyMax")
DailyMin = Class(name="DailyMin")
Maximum = Class(name="Maximum")
Minimum = Class(name="Minimum")
MonthlyMax = Class(name="MonthlyMax")
MonthlyMin = Class(name="MonthlyMin")
WeeklyMax = Class(name="WeeklyMax")
WeeklyMin = Class(name="WeeklyMin")
Precedes = Class(name="Precedes")
eTJ_RealFormat = Class(name="eTJ::RealFormat")
CurrencyFormat = Class(name="CurrencyFormat")
NumberFormat = Class(name="NumberFormat")
ListItem = Class(name="ListItem")
Prolog = Class(name="Prolog")
Right = Class(name="Right")
Summary = Class(name="Summary")
eTJ_RichText = Class(name="eTJ::RichText")
Caption = Class(name="Caption")
Center = Class(name="Center")
Details = Class(name="Details")
Epilog = Class(name="Epilog")
Footer = Class(name="Footer")
Header = Class(name="Header")
Headline = Class(name="Headline")
Left = Class(name="Left")
eTJ_ExtDate = Class(name="eTJ::ExtDate")
eTJ_LogicalAbsoluteIdExression = Class(name="eTJ::LogicalAbsoluteIdExression")
eTJ_LogicalBooleanLiteral = Class(name="eTJ::LogicalBooleanLiteral")
eTJ_LogicalNumeralLiteral = Class(name="eTJ::LogicalNumeralLiteral")
eTJ_LogicalStringLiteral = Class(name="eTJ::LogicalStringLiteral")
eTJ_Defintions = Class(name="eTJ::Defintions")
Definitions = Class(name="Definitions")
eTJ_LogicalFunctionExpression = Class(name="eTJ::LogicalFunctionExpression")
LogicalExpression = Class(name="LogicalExpression")
eTJ_LogicalDateLiteral = Class(name="eTJ::LogicalDateLiteral")
eTJ_LogicalFlagExpression = Class(name="eTJ::LogicalFlagExpression")

# eTJ_Global class attributes and methods

# eTJ_Project class attributes and methods
eTJ_Project_id: Property = Property(name="id", type=StringType)
eTJ_Project_name: Property = Property(name="name", type=StringType)
eTJ_Project_version: Property = Property(name="version", type=StringType)
eTJ_Project.attributes={eTJ_Project_id, eTJ_Project_version, eTJ_Project_name}

# eTJ_Property class attributes and methods

# eTJ_Leaves class attributes and methods

# Property class attributes and methods

# ResourceAttribute class attributes and methods

# eTJ_LeaveDetails class attributes and methods
eTJ_LeaveDetails_type: Property = Property(name="type", type=StringType)
eTJ_LeaveDetails_name: Property = Property(name="name", type=StringType)
eTJ_LeaveDetails.attributes={eTJ_LeaveDetails_name, eTJ_LeaveDetails_type}

# eTJ_Interval3 class attributes and methods

# eTJ_Account class attributes and methods
eTJ_Account_id: Property = Property(name="id", type=StringType)
eTJ_Account_name: Property = Property(name="name", type=StringType)
eTJ_Account.attributes={eTJ_Account_name, eTJ_Account_id}

# AccountAttribute class attributes and methods

# eTJ_AccountAttribute class attributes and methods

# eTJ_AccountPrefix class attributes and methods

# IncludePropertiesAttribute class attributes and methods

# eTJ_AccountReport class attributes and methods

# ReportAttribute class attributes and methods

# eTJ_AccountRoot class attributes and methods

# eTJ_Interval2 class attributes and methods

# eTJ_ProjectAttribute class attributes and methods

# eTJ_Task class attributes and methods
eTJ_Task_id: Property = Property(name="id", type=StringType)
eTJ_Task_name: Property = Property(name="name", type=StringType)
eTJ_Task.attributes={eTJ_Task_name, eTJ_Task_id}

# eTJ_TaskAttribute class attributes and methods

# eTJ_ReportAttribute class attributes and methods

# eTJ_Scenario class attributes and methods
eTJ_Scenario_id: Property = Property(name="id", type=StringType)
eTJ_Scenario_name: Property = Property(name="name", type=StringType)
eTJ_Scenario_active: Property = Property(name="active", type=StringType)
eTJ_Scenario.attributes={eTJ_Scenario_active, eTJ_Scenario_name, eTJ_Scenario_id}

# eTJ_EObject class attributes and methods

# eTJ_MacroCall class attributes and methods
eTJ_MacroCall_buildin: Property = Property(name="buildin", type=StringType)
eTJ_MacroCall.attributes={eTJ_MacroCall_buildin}

# End class attributes and methods

# Start class attributes and methods

# ExtDate class attributes and methods

# eTJ_Macro class attributes and methods
eTJ_Macro_id: Property = Property(name="id", type=StringType)
eTJ_Macro_value: Property = Property(name="value", type=StringType)
eTJ_Macro.attributes={eTJ_Macro_id, eTJ_Macro_value}

# eTJ_Report class attributes and methods
eTJ_Report_name: Property = Property(name="name", type=StringType)
eTJ_Report_id: Property = Property(name="id", type=StringType)
eTJ_Report.attributes={eTJ_Report_name, eTJ_Report_id}

# AccountReport class attributes and methods

# ResourceReport class attributes and methods

# TaskReport class attributes and methods

# TextReport class attributes and methods

# eTJ_ResourceAttribute class attributes and methods

# eTJ_IcalReport class attributes and methods
eTJ_IcalReport_filename: Property = Property(name="filename", type=StringType)
eTJ_IcalReport.attributes={eTJ_IcalReport_filename}

# eTJ_IcalReportAttribute class attributes and methods

# eTJ_Export class attributes and methods
eTJ_Export_id: Property = Property(name="id", type=StringType)
eTJ_Export_filename: Property = Property(name="filename", type=StringType)
eTJ_Export.attributes={eTJ_Export_filename, eTJ_Export_id}

# eTJ_ExportAttribute class attributes and methods

# eTJ_Resource class attributes and methods
eTJ_Resource_id: Property = Property(name="id", type=StringType)
eTJ_Resource_name: Property = Property(name="name", type=StringType)
eTJ_Resource.attributes={eTJ_Resource_id, eTJ_Resource_name}

# eTJ_Allocate class attributes and methods

# eTJ_AllocateResource class attributes and methods

# eTJ_AllocateResourceAttribute class attributes and methods

# eTJ_Navigator class attributes and methods
eTJ_Navigator_id: Property = Property(name="id", type=StringType)
eTJ_Navigator.attributes={eTJ_Navigator_id}

# eTJ_NavigatorAttribute class attributes and methods

# eTJ_NewTask class attributes and methods
eTJ_NewTask_id: Property = Property(name="id", type=StringType)
eTJ_NewTask_text: Property = Property(name="text", type=StringType)
eTJ_NewTask.attributes={eTJ_NewTask_id, eTJ_NewTask_text}

# TimesheetAttribute class attributes and methods

# eTJ_Balance class attributes and methods

# eTJ_NewTaskAttribute class attributes and methods

# eTJ_NikuReport class attributes and methods
eTJ_NikuReport_filename: Property = Property(name="filename", type=StringType)
eTJ_NikuReport.attributes={eTJ_NikuReport_filename}

# eTJ_NikuReportAttribute class attributes and methods

# eTJ_Alert class attributes and methods
eTJ_Alert_level: Property = Property(name="level", type=StringType)
eTJ_Alert.attributes={eTJ_Alert_level}

# eTJ_Alternative class attributes and methods

# AllocateResourceAttribute class attributes and methods

# eTJ_Author class attributes and methods

# StatusStatusSheetAttribute class attributes and methods

# eTJ_Caption class attributes and methods

# eTJ_Booking class attributes and methods
eTJ_Booking_overtime: Property = Property(name="overtime", type=IntegerType)
eTJ_Booking_sloppy: Property = Property(name="sloppy", type=IntegerType)
eTJ_Booking.attributes={eTJ_Booking_sloppy, eTJ_Booking_overtime}

# eTJ_Interval4 class attributes and methods

# eTJ_BookingTask class attributes and methods

# eTJ_BookingResource class attributes and methods

# eTJ_Columns class attributes and methods

# eTJ_Column class attributes and methods
eTJ_Column_id: Property = Property(name="id", type=StringType)
eTJ_Column.attributes={eTJ_Column_id}

# eTJ_CellColor class attributes and methods

# ColumnAttribute class attributes and methods

# eTJ_LogicalExpression class attributes and methods
eTJ_LogicalExpression_op: Property = Property(name="op", type=StringType)
eTJ_LogicalExpression.attributes={eTJ_LogicalExpression_op}

# eTJ_RGB class attributes and methods
eTJ_RGB_value: Property = Property(name="value", type=StringType)
eTJ_RGB.attributes={eTJ_RGB_value}

# eTJ_CellText class attributes and methods
eTJ_CellText_text: Property = Property(name="text", type=StringType)
eTJ_CellText.attributes={eTJ_CellText_text}

# eTJ_Center class attributes and methods

# eTJ_Charge class attributes and methods
eTJ_Charge_amount: Property = Property(name="amount", type=FloatType)
eTJ_Charge_applies: Property = Property(name="applies", type=StringType)
eTJ_Charge.attributes={eTJ_Charge_applies, eTJ_Charge_amount}

# eTJ_ChargeSet class attributes and methods

# eTJ_AccountShare class attributes and methods
eTJ_AccountShare_share: Property = Property(name="share", type=FloatType)
eTJ_AccountShare.attributes={eTJ_AccountShare_share}

# eTJ_DailyMin class attributes and methods

# eTJ_Complete class attributes and methods
eTJ_Complete_complete: Property = Property(name="complete", type=FloatType)
eTJ_Complete.attributes={eTJ_Complete_complete}

# eTJ_Copyright class attributes and methods
eTJ_Copyright_text: Property = Property(name="text", type=StringType)
eTJ_Copyright.attributes={eTJ_Copyright_text}

# eTJ_Credit class attributes and methods
eTJ_Credit_description: Property = Property(name="description", type=StringType)
eTJ_Credit_amount: Property = Property(name="amount", type=FloatType)
eTJ_Credit.attributes={eTJ_Credit_amount, eTJ_Credit_description}

# eTJ_ISODATE class attributes and methods

# eTJ_Currency class attributes and methods
eTJ_Currency_currency: Property = Property(name="currency", type=StringType)
eTJ_Currency.attributes={eTJ_Currency_currency}

# ProjectAttribute class attributes and methods

# eTJ_CurrencyFormat class attributes and methods

# eTJ_DailyMax class attributes and methods

# LimitsAttribute class attributes and methods

# eTJ_DailyWorkingHours class attributes and methods
eTJ_DailyWorkingHours_dailyWorkingHours: Property = Property(name="dailyWorkingHours", type=FloatType)
eTJ_DailyWorkingHours.attributes={eTJ_DailyWorkingHours_dailyWorkingHours}

# eTJ_Email class attributes and methods
eTJ_Email_address: Property = Property(name="address", type=StringType)
eTJ_Email.attributes={eTJ_Email_address}

# eTJ_Definitions class attributes and methods
eTJ_Definitions_all: Property = Property(name="all", type=BooleanType)
eTJ_Definitions_none: Property = Property(name="none", type=BooleanType)
eTJ_Definitions.attributes={eTJ_Definitions_all, eTJ_Definitions_none}

# ExportAttribute class attributes and methods

# eTJ_Depends class attributes and methods

# eTJ_TaskDependency class attributes and methods
eTJ_TaskDependency_policy: Property = Property(name="policy", type=StringType)
eTJ_TaskDependency.attributes={eTJ_TaskDependency_policy}

# eTJ_Details class attributes and methods

# StatusTimesheetAttribute class attributes and methods

# eTJ_Duration class attributes and methods

# eTJ_DurationQuantity class attributes and methods
eTJ_DurationQuantity_value: Property = Property(name="value", type=FloatType)
eTJ_DurationQuantity_unit: Property = Property(name="unit", type=StringType)
eTJ_DurationQuantity.attributes={eTJ_DurationQuantity_value, eTJ_DurationQuantity_unit}

# eTJ_Efficiency class attributes and methods
eTJ_Efficiency_efficiency: Property = Property(name="efficiency", type=FloatType)
eTJ_Efficiency.attributes={eTJ_Efficiency_efficiency}

# eTJ_Effort class attributes and methods

# eTJ_ExtendResource class attributes and methods

# eTJ_End class attributes and methods

# IcalReportAttribute class attributes and methods

# NewTaskAttribute class attributes and methods

# NikuReportAttribute class attributes and methods

# StatusSheetReportAttribute class attributes and methods

# TaskTimesheetAttribute class attributes and methods

# TimesheetReportAttribute class attributes and methods

# eTJ_EndCredit class attributes and methods
eTJ_EndCredit_credit: Property = Property(name="credit", type=FloatType)
eTJ_EndCredit.attributes={eTJ_EndCredit_credit}

# eTJ_Epilog class attributes and methods

# eTJ_Extend class attributes and methods
eTJ_Extend_scenariospecific: Property = Property(name="scenariospecific", type=BooleanType)
eTJ_Extend_name: Property = Property(name="name", type=StringType)
eTJ_Extend_description: Property = Property(name="description", type=StringType)
eTJ_Extend_inherit: Property = Property(name="inherit", type=BooleanType)
eTJ_Extend.attributes={eTJ_Extend_scenariospecific, eTJ_Extend_name, eTJ_Extend_inherit, eTJ_Extend_description}

# eTJ_ExtendedResourceAttribute class attributes and methods
eTJ_ExtendedResourceAttribute_value: Property = Property(name="value", type=StringType)
eTJ_ExtendedResourceAttribute.attributes={eTJ_ExtendedResourceAttribute_value}

# eTJ_ExtendTask class attributes and methods

# eTJ_ExtendedTaskAttribute class attributes and methods
eTJ_ExtendedTaskAttribute_value: Property = Property(name="value", type=StringType)
eTJ_ExtendedTaskAttribute.attributes={eTJ_ExtendedTaskAttribute_value}

# eTJ_Fail class attributes and methods

# eTJ_Flags class attributes and methods
eTJ_Flags_flags: Property = Property(name="flags", type=StringType)
eTJ_Flags.attributes={eTJ_Flags_flags}

# eTJ_FontColor class attributes and methods
eTJ_FontColor_color: Property = Property(name="color", type=StringType)
eTJ_FontColor.attributes={eTJ_FontColor_color}

# eTJ_Footer class attributes and methods

# eTJ_Formats class attributes and methods
eTJ_Formats_formats: Property = Property(name="formats", type=StringType)
eTJ_Formats.attributes={eTJ_Formats_formats}

# eTJ_Function class attributes and methods
eTJ_Function_level: Property = Property(name="level", type=IntegerType)
eTJ_Function_parentId: Property = Property(name="parentId", type=StringType)
eTJ_Function_distance: Property = Property(name="distance", type=IntegerType)
eTJ_Function.attributes={eTJ_Function_level, eTJ_Function_distance, eTJ_Function_parentId}

# eTJ_GapDuration class attributes and methods

# eTJ_GapLength class attributes and methods

# eTJ_HAlign class attributes and methods
eTJ_HAlign_justification: Property = Property(name="justification", type=StringType)
eTJ_HAlign.attributes={eTJ_HAlign_justification}

# eTJ_Header class attributes and methods

# eTJ_Headline class attributes and methods

# eTJ_HideAccount class attributes and methods
eTJ_HideAccount_expression: Property = Property(name="expression", type=StringType)
eTJ_HideAccount.attributes={eTJ_HideAccount_expression}

# eTJ_HideJournalEntry class attributes and methods
eTJ_HideJournalEntry_expression: Property = Property(name="expression", type=StringType)
eTJ_HideJournalEntry.attributes={eTJ_HideJournalEntry_expression}

# eTJ_HideReport class attributes and methods

# NavigatorAttribute class attributes and methods

# eTJ_HideResource class attributes and methods

# eTJ_HideTask class attributes and methods

# eTJ_Include class attributes and methods
eTJ_Include_importURI: Property = Property(name="importURI", type=StringType)
eTJ_Include.attributes={eTJ_Include_importURI}

# eTJ_IncludeProperties class attributes and methods
eTJ_IncludeProperties_importURI: Property = Property(name="importURI", type=StringType)
eTJ_IncludeProperties.attributes={eTJ_IncludeProperties_importURI}

# eTJ_IncludePropertiesAttribute class attributes and methods

# eTJ_Interval1 class attributes and methods

# eTJ_JournalAttributes class attributes and methods
eTJ_JournalAttributes_args: Property = Property(name="args", type=StringType)
eTJ_JournalAttributes.attributes={eTJ_JournalAttributes_args}

# eTJ_JournalEntry class attributes and methods
eTJ_JournalEntry_headline: Property = Property(name="headline", type=StringType)
eTJ_JournalEntry.attributes={eTJ_JournalEntry_headline}

# eTJ_Summary class attributes and methods

# eTJ_JournalMode class attributes and methods
eTJ_JournalMode_mode: Property = Property(name="mode", type=StringType)
eTJ_JournalMode.attributes={eTJ_JournalMode_mode}

# eTJ_Left class attributes and methods

# eTJ_Length class attributes and methods

# eTJ_Limits class attributes and methods

# eTJ_LimitsAttribute class attributes and methods

# eTJ_ListItem class attributes and methods

# eTJ_ListType class attributes and methods
eTJ_ListType_type: Property = Property(name="type", type=StringType)
eTJ_ListType.attributes={eTJ_ListType_type}

# eTJ_Mandatory class attributes and methods
eTJ_Mandatory_mandatory: Property = Property(name="mandatory", type=BooleanType)
eTJ_Mandatory.attributes={eTJ_Mandatory_mandatory}

# eTJ_LoadUnit class attributes and methods
eTJ_LoadUnit_unit: Property = Property(name="unit", type=StringType)
eTJ_LoadUnit.attributes={eTJ_LoadUnit_unit}

# eTJ_Managers class attributes and methods

# eTJ_MonthlyMin class attributes and methods

# eTJ_MaxEnd class attributes and methods

# eTJ_Maximum class attributes and methods

# eTJ_MaxStart class attributes and methods

# eTJ_Milestone class attributes and methods
eTJ_Milestone_milestone: Property = Property(name="milestone", type=BooleanType)
eTJ_Milestone.attributes={eTJ_Milestone_milestone}

# eTJ_Minimum class attributes and methods

# eTJ_MinEnd class attributes and methods

# eTJ_MinStart class attributes and methods

# eTJ_MonthlyMax class attributes and methods

# eTJ_Precedes class attributes and methods

# eTJ_Priority class attributes and methods
eTJ_Priority_priority: Property = Property(name="priority", type=IntegerType)
eTJ_Priority.attributes={eTJ_Priority_priority}

# eTJ_Note class attributes and methods
eTJ_Note_note: Property = Property(name="note", type=StringType)
eTJ_Note.attributes={eTJ_Note_note}

# eTJ_Now class attributes and methods

# eTJ_NumberFormat class attributes and methods

# eTJ_Period class attributes and methods

# eTJ_Persistent class attributes and methods
eTJ_Persistent_persistent: Property = Property(name="persistent", type=BooleanType)
eTJ_Persistent.attributes={eTJ_Persistent_persistent}

# eTJ_PurgeResource class attributes and methods
eTJ_PurgeResource_listAttribute: Property = Property(name="listAttribute", type=StringType)
eTJ_PurgeResource.attributes={eTJ_PurgeResource_listAttribute}

# eTJ_ProjectId class attributes and methods
eTJ_ProjectId_projectId: Property = Property(name="projectId", type=StringType)
eTJ_ProjectId.attributes={eTJ_ProjectId_projectId}

# eTJ_ProjectIds class attributes and methods
eTJ_ProjectIds_ids: Property = Property(name="ids", type=StringType)
eTJ_ProjectIds.attributes={eTJ_ProjectIds_ids}

# eTJ_Prolog class attributes and methods

# eTJ_PurgeReport class attributes and methods
eTJ_PurgeReport_listAttribute: Property = Property(name="listAttribute", type=StringType)
eTJ_PurgeReport.attributes={eTJ_PurgeReport_listAttribute}

# eTJ_Rate class attributes and methods
eTJ_Rate_rate: Property = Property(name="rate", type=FloatType)
eTJ_Rate.attributes={eTJ_Rate_rate}

# eTJ_Remaining class attributes and methods

# eTJ_PurgeTask class attributes and methods
eTJ_PurgeTask_listAttribute: Property = Property(name="listAttribute", type=StringType)
eTJ_PurgeTask.attributes={eTJ_PurgeTask_listAttribute}

# eTJ_ResourceReport class attributes and methods

# eTJ_ResourceRoot class attributes and methods

# eTJ_ReportPrefix class attributes and methods

# eTJ_ResourceAttributes class attributes and methods
eTJ_ResourceAttributes_all: Property = Property(name="all", type=BooleanType)
eTJ_ResourceAttributes_none: Property = Property(name="none", type=BooleanType)
eTJ_ResourceAttributes_vacation: Property = Property(name="vacation", type=BooleanType)
eTJ_ResourceAttributes_booking: Property = Property(name="booking", type=BooleanType)
eTJ_ResourceAttributes_workingHours: Property = Property(name="workingHours", type=BooleanType)
eTJ_ResourceAttributes.attributes={eTJ_ResourceAttributes_all, eTJ_ResourceAttributes_none, eTJ_ResourceAttributes_vacation, eTJ_ResourceAttributes_workingHours, eTJ_ResourceAttributes_booking}

# eTJ_ResourcePrefix class attributes and methods

# eTJ_Responsible class attributes and methods

# eTJ_Right class attributes and methods

# eTJ_RollupAccount class attributes and methods

# eTJ_RollupResource class attributes and methods

# eTJ_ScenarioIcal class attributes and methods

# eTJ_RollupTask class attributes and methods

# eTJ_Scale class attributes and methods
eTJ_Scale_scale: Property = Property(name="scale", type=StringType)
eTJ_Scale.attributes={eTJ_Scale_scale}

# eTJ_Scenarios class attributes and methods

# eTJ_Scheduled class attributes and methods
eTJ_Scheduled_scheduled: Property = Property(name="scheduled", type=BooleanType)
eTJ_Scheduled.attributes={eTJ_Scheduled_scheduled}

# eTJ_Scheduling class attributes and methods
eTJ_Scheduling_scheduling: Property = Property(name="scheduling", type=StringType)
eTJ_Scheduling.attributes={eTJ_Scheduling_scheduling}

# eTJ_Select class attributes and methods
eTJ_Select_argument: Property = Property(name="argument", type=StringType)
eTJ_Select.attributes={eTJ_Select_argument}

# eTJ_SelfContained class attributes and methods
eTJ_SelfContained_selfcontained: Property = Property(name="selfcontained", type=StringType)
eTJ_SelfContained.attributes={eTJ_SelfContained_selfcontained}

# eTJ_Shift class attributes and methods
eTJ_Shift_id: Property = Property(name="id", type=StringType)
eTJ_Shift_name: Property = Property(name="name", type=StringType)
eTJ_Shift_replace: Property = Property(name="replace", type=StringType)
eTJ_Shift_timezone: Property = Property(name="timezone", type=StringType)
eTJ_Shift.attributes={eTJ_Shift_timezone, eTJ_Shift_id, eTJ_Shift_replace, eTJ_Shift_name}

# eTJ_Vacation class attributes and methods
eTJ_Vacation_name: Property = Property(name="name", type=StringType)
eTJ_Vacation.attributes={eTJ_Vacation_name}

# eTJ_WorkingHours class attributes and methods
eTJ_WorkingHours_off: Property = Property(name="off", type=BooleanType)
eTJ_WorkingHours.attributes={eTJ_WorkingHours_off}

# eTJ_ShiftTimesheet class attributes and methods

# eTJ_Shifts class attributes and methods

# ShiftsResource class attributes and methods

# ShiftsTask class attributes and methods

# eTJ_ShiftsLimit class attributes and methods

# eTJ_Criterion class attributes and methods
eTJ_Criterion_columnId: Property = Property(name="columnId", type=StringType)
eTJ_Criterion_direction: Property = Property(name="direction", type=StringType)
eTJ_Criterion.attributes={eTJ_Criterion_direction, eTJ_Criterion_columnId}

# eTJ_ShiftsAllocate class attributes and methods

# eTJ_ShiftsResource class attributes and methods

# eTJ_ShiftsTask class attributes and methods

# eTJ_ShortTimeFormat class attributes and methods
eTJ_ShortTimeFormat_shortTimeFormat: Property = Property(name="shortTimeFormat", type=StringType)
eTJ_ShortTimeFormat.attributes={eTJ_ShortTimeFormat_shortTimeFormat}

# eTJ_Sort class attributes and methods
eTJ_Sort_tree: Property = Property(name="tree", type=BooleanType)
eTJ_Sort.attributes={eTJ_Sort_tree}

# SortAccounts class attributes and methods

# SortJournalEntries class attributes and methods

# SortResources class attributes and methods

# eTJ_StatusStatusSheet class attributes and methods
eTJ_StatusStatusSheet_level: Property = Property(name="level", type=StringType)
eTJ_StatusStatusSheet_text: Property = Property(name="text", type=StringType)
eTJ_StatusStatusSheet.attributes={eTJ_StatusStatusSheet_level, eTJ_StatusStatusSheet_text}

# TaskStatusSheetAttribute class attributes and methods

# SortTasks class attributes and methods

# eTJ_SortAccounts class attributes and methods

# eTJ_SortJournalEntries class attributes and methods

# eTJ_SortResources class attributes and methods

# eTJ_SortTasks class attributes and methods

# eTJ_Start class attributes and methods

# eTJ_StatusSheetAttribute class attributes and methods

# eTJ_StatusStatusSheetAttribute class attributes and methods

# eTJ_StatusTimesheet class attributes and methods
eTJ_StatusTimesheet_level: Property = Property(name="level", type=StringType)
eTJ_StatusTimesheet_text: Property = Property(name="text", type=StringType)
eTJ_StatusTimesheet.attributes={eTJ_StatusTimesheet_text, eTJ_StatusTimesheet_level}

# eTJ_StatusTimesheetAttribute class attributes and methods

# eTJ_StatusSheet class attributes and methods

# eTJ_SupplementResource class attributes and methods

# eTJ_StatusSheetReport class attributes and methods
eTJ_StatusSheetReport_filename: Property = Property(name="filename", type=StringType)
eTJ_StatusSheetReport.attributes={eTJ_StatusSheetReport_filename}

# eTJ_StatusSheetReportAttribute class attributes and methods

# eTJ_SupplementAccount class attributes and methods

# eTJ_SupplementReport class attributes and methods

# eTJ_SupplementTask class attributes and methods

# eTJ_TagFile class attributes and methods
eTJ_TagFile_id: Property = Property(name="id", type=StringType)
eTJ_TagFile_filename: Property = Property(name="filename", type=StringType)
eTJ_TagFile.attributes={eTJ_TagFile_filename, eTJ_TagFile_id}

# eTJ_TaskStatusSheet class attributes and methods

# StatusSheetAttribute class attributes and methods

# eTJ_TaskStatusSheetAttribute class attributes and methods

# eTJ_TaskTimesheet class attributes and methods

# eTJ_TaskTimesheetAttribute class attributes and methods

# eTJ_TaskAttributes class attributes and methods
eTJ_TaskAttributes_note: Property = Property(name="note", type=BooleanType)
eTJ_TaskAttributes_minstart: Property = Property(name="minstart", type=BooleanType)
eTJ_TaskAttributes_minend: Property = Property(name="minend", type=BooleanType)
eTJ_TaskAttributes_all: Property = Property(name="all", type=BooleanType)
eTJ_TaskAttributes_none: Property = Property(name="none", type=BooleanType)
eTJ_TaskAttributes_responsible: Property = Property(name="responsible", type=BooleanType)
eTJ_TaskAttributes_flags: Property = Property(name="flags", type=BooleanType)
eTJ_TaskAttributes_maxstart: Property = Property(name="maxstart", type=BooleanType)
eTJ_TaskAttributes_maxend: Property = Property(name="maxend", type=BooleanType)
eTJ_TaskAttributes_priority: Property = Property(name="priority", type=BooleanType)
eTJ_TaskAttributes_booking: Property = Property(name="booking", type=BooleanType)
eTJ_TaskAttributes_complete: Property = Property(name="complete", type=BooleanType)
eTJ_TaskAttributes_depends: Property = Property(name="depends", type=BooleanType)
eTJ_TaskAttributes.attributes={eTJ_TaskAttributes_flags, eTJ_TaskAttributes_minend, eTJ_TaskAttributes_depends, eTJ_TaskAttributes_maxend, eTJ_TaskAttributes_responsible, eTJ_TaskAttributes_minstart, eTJ_TaskAttributes_priority, eTJ_TaskAttributes_all, eTJ_TaskAttributes_none, eTJ_TaskAttributes_complete, eTJ_TaskAttributes_maxstart, eTJ_TaskAttributes_booking, eTJ_TaskAttributes_note}

# eTJ_Timesheet class attributes and methods

# eTJ_TaskPrefix class attributes and methods

# eTJ_TaskReport class attributes and methods

# eTJ_TaskRoot class attributes and methods

# eTJ_TextReport class attributes and methods

# eTJ_TimeFormat class attributes and methods
eTJ_TimeFormat_timeformat: Property = Property(name="timeformat", type=StringType)
eTJ_TimeFormat.attributes={eTJ_TimeFormat_timeformat}

# eTJ_Timeoff class attributes and methods
eTJ_Timeoff_name: Property = Property(name="name", type=StringType)
eTJ_Timeoff_id: Property = Property(name="id", type=StringType)
eTJ_Timeoff.attributes={eTJ_Timeoff_id, eTJ_Timeoff_name}

# eTJ_TimingResolution class attributes and methods
eTJ_TimingResolution_timingResolution: Property = Property(name="timingResolution", type=IntegerType)
eTJ_TimingResolution.attributes={eTJ_TimingResolution_timingResolution}

# eTJ_TimesheetAttribute class attributes and methods

# eTJ_TimesheetReport class attributes and methods
eTJ_TimesheetReport_filename: Property = Property(name="filename", type=StringType)
eTJ_TimesheetReport.attributes={eTJ_TimesheetReport_filename}

# eTJ_TimesheetReportAttribute class attributes and methods

# eTJ_Timezone class attributes and methods
eTJ_Timezone_timezone: Property = Property(name="timezone", type=StringType)
eTJ_Timezone.attributes={eTJ_Timezone_timezone}

# eTJ_Title class attributes and methods
eTJ_Title_title: Property = Property(name="title", type=StringType)
eTJ_Title.attributes={eTJ_Title_title}

# eTJ_Warn class attributes and methods

# eTJ_ToolTip class attributes and methods
eTJ_ToolTip_tip: Property = Property(name="tip", type=StringType)
eTJ_ToolTip.attributes={eTJ_ToolTip_tip}

# eTJ_WeekStarts class attributes and methods
eTJ_WeekStarts_sunday: Property = Property(name="sunday", type=BooleanType)
eTJ_WeekStarts_monday: Property = Property(name="monday", type=BooleanType)
eTJ_WeekStarts.attributes={eTJ_WeekStarts_monday, eTJ_WeekStarts_sunday}

# eTJ_WeeklyMax class attributes and methods

# eTJ_TrackingScenario class attributes and methods

# eTJ_TreeLevel class attributes and methods
eTJ_TreeLevel_level: Property = Property(name="level", type=StringType)
eTJ_TreeLevel.attributes={eTJ_TreeLevel_level}

# eTJ_Weekdays class attributes and methods
eTJ_Weekdays_first: Property = Property(name="first", type=StringType)
eTJ_Weekdays_last: Property = Property(name="last", type=StringType)
eTJ_Weekdays.attributes={eTJ_Weekdays_first, eTJ_Weekdays_last}

# eTJ_WorkHours class attributes and methods
eTJ_WorkHours_start: Property = Property(name="start", type=StringType)
eTJ_WorkHours_stop: Property = Property(name="stop", type=StringType)
eTJ_WorkHours.attributes={eTJ_WorkHours_start, eTJ_WorkHours_stop}

# eTJ_YearlyWorkingDays class attributes and methods
eTJ_YearlyWorkingDays_yearlyWorkingDays: Property = Property(name="yearlyWorkingDays", type=IntegerType)
eTJ_YearlyWorkingDays.attributes={eTJ_YearlyWorkingDays_yearlyWorkingDays}

# eTJ_WeeklyMin class attributes and methods

# eTJ_Width class attributes and methods
eTJ_Width_width: Property = Property(name="width", type=FloatType)
eTJ_Width.attributes={eTJ_Width_width}

# eTJ_Work class attributes and methods
eTJ_Work_value: Property = Property(name="value", type=FloatType)
eTJ_Work_unit: Property = Property(name="unit", type=StringType)
eTJ_Work.attributes={eTJ_Work_unit, eTJ_Work_value}

# GapDuration class attributes and methods

# GapLength class attributes and methods

# eTJ_ColumnAttribute class attributes and methods

# eTJ_ExtendedResourceAttributeColumn class attributes and methods

# eTJ_LimitAttribute class attributes and methods

# eTJ_Limit class attributes and methods

# DailyMax class attributes and methods

# DailyMin class attributes and methods

# Maximum class attributes and methods

# Minimum class attributes and methods

# MonthlyMax class attributes and methods

# MonthlyMin class attributes and methods

# WeeklyMax class attributes and methods

# WeeklyMin class attributes and methods

# Precedes class attributes and methods

# eTJ_RealFormat class attributes and methods
eTJ_RealFormat_thousandsSeparator: Property = Property(name="thousandsSeparator", type=StringType)
eTJ_RealFormat_fractionSeparator: Property = Property(name="fractionSeparator", type=StringType)
eTJ_RealFormat_fractionDigits: Property = Property(name="fractionDigits", type=IntegerType)
eTJ_RealFormat_negativePrefix: Property = Property(name="negativePrefix", type=StringType)
eTJ_RealFormat_negativeSuffix: Property = Property(name="negativeSuffix", type=StringType)
eTJ_RealFormat.attributes={eTJ_RealFormat_negativePrefix, eTJ_RealFormat_thousandsSeparator, eTJ_RealFormat_fractionSeparator, eTJ_RealFormat_negativeSuffix, eTJ_RealFormat_fractionDigits}

# CurrencyFormat class attributes and methods

# NumberFormat class attributes and methods

# ListItem class attributes and methods

# Prolog class attributes and methods

# Right class attributes and methods

# Summary class attributes and methods

# eTJ_RichText class attributes and methods
eTJ_RichText_text: Property = Property(name="text", type=StringType)
eTJ_RichText.attributes={eTJ_RichText_text}

# Caption class attributes and methods

# Center class attributes and methods

# Details class attributes and methods

# Epilog class attributes and methods

# Footer class attributes and methods

# Header class attributes and methods

# Headline class attributes and methods

# Left class attributes and methods

# eTJ_ExtDate class attributes and methods

# eTJ_LogicalAbsoluteIdExression class attributes and methods
eTJ_LogicalAbsoluteIdExression_value: Property = Property(name="value", type=StringType)
eTJ_LogicalAbsoluteIdExression.attributes={eTJ_LogicalAbsoluteIdExression_value}

# eTJ_LogicalBooleanLiteral class attributes and methods
eTJ_LogicalBooleanLiteral_isTrue: Property = Property(name="isTrue", type=BooleanType)
eTJ_LogicalBooleanLiteral.attributes={eTJ_LogicalBooleanLiteral_isTrue}

# eTJ_LogicalNumeralLiteral class attributes and methods
eTJ_LogicalNumeralLiteral_value: Property = Property(name="value", type=FloatType)
eTJ_LogicalNumeralLiteral.attributes={eTJ_LogicalNumeralLiteral_value}

# eTJ_LogicalStringLiteral class attributes and methods
eTJ_LogicalStringLiteral_value: Property = Property(name="value", type=StringType)
eTJ_LogicalStringLiteral.attributes={eTJ_LogicalStringLiteral_value}

# eTJ_Defintions class attributes and methods
eTJ_Defintions_flags: Property = Property(name="flags", type=BooleanType)
eTJ_Defintions_resources: Property = Property(name="resources", type=BooleanType)
eTJ_Defintions_tasks: Property = Property(name="tasks", type=BooleanType)
eTJ_Defintions_project: Property = Property(name="project", type=BooleanType)
eTJ_Defintions_projectids: Property = Property(name="projectids", type=BooleanType)
eTJ_Defintions.attributes={eTJ_Defintions_flags, eTJ_Defintions_resources, eTJ_Defintions_tasks, eTJ_Defintions_project, eTJ_Defintions_projectids}

# Definitions class attributes and methods

# eTJ_LogicalFunctionExpression class attributes and methods

# LogicalExpression class attributes and methods

# eTJ_LogicalDateLiteral class attributes and methods

# eTJ_LogicalFlagExpression class attributes and methods
eTJ_LogicalFlagExpression_columId: Property = Property(name="columId", type=StringType)
eTJ_LogicalFlagExpression.attributes={eTJ_LogicalFlagExpression_columId}

# Relationships
project0: BinaryAssociation = BinaryAssociation(
    name="project0",
    ends={
        Property(name="eTJ_Project", type=eTJ_Global, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Global", type=eTJ_Project, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties1: BinaryAssociation = BinaryAssociation(
    name="properties1",
    ends={
        Property(name="eTJ_Property", type=eTJ_Global, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Global2", type=eTJ_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
details3: BinaryAssociation = BinaryAssociation(
    name="details3",
    ends={
        Property(name="eTJ_LeaveDetails", type=eTJ_Leaves, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Leaves", type=eTJ_LeaveDetails, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
account7: BinaryAssociation = BinaryAssociation(
    name="account7",
    ends={
        Property(name="eTJ_AccountPrefix", type=eTJ_Account, multiplicity=Multiplicity(0, 1)),
        Property(name="eTJ_Account8", type=eTJ_AccountPrefix, multiplicity=Multiplicity(1, 1))
    }
)
interval4: BinaryAssociation = BinaryAssociation(
    name="interval4",
    ends={
        Property(name="eTJ_Interval3", type=eTJ_LeaveDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_LeaveDetails5", type=eTJ_Interval3, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes6: BinaryAssociation = BinaryAssociation(
    name="attributes6",
    ends={
        Property(name="eTJ_AccountAttribute", type=eTJ_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Account", type=eTJ_AccountAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes15: BinaryAssociation = BinaryAssociation(
    name="attributes15",
    ends={
        Property(name="eTJ_Task", type=eTJ_TaskAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="eTJ_TaskAttribute", type=eTJ_Task, multiplicity=Multiplicity(1, 1))
    }
)
account9: BinaryAssociation = BinaryAssociation(
    name="account9",
    ends={
        Property(name="eTJ_Account10", type=eTJ_AccountRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_AccountRoot", type=eTJ_Account, multiplicity=Multiplicity(0, 1))
    }
)
interval11: BinaryAssociation = BinaryAssociation(
    name="interval11",
    ends={
        Property(name="eTJ_Interval2", type=eTJ_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Project12", type=eTJ_Interval2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes13: BinaryAssociation = BinaryAssociation(
    name="attributes13",
    ends={
        Property(name="eTJ_ProjectAttribute", type=eTJ_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Project14", type=eTJ_ProjectAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenario16: BinaryAssociation = BinaryAssociation(
    name="scenario16",
    ends={
        Property(name="eTJ_Scenario", type=eTJ_TaskAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TaskAttribute17", type=eTJ_Scenario, multiplicity=Multiplicity(0, 1))
    }
)
attr18: BinaryAssociation = BinaryAssociation(
    name="attr18",
    ends={
        Property(name="eTJ_EObject", type=eTJ_TaskAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TaskAttribute19", type=eTJ_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
macro20: BinaryAssociation = BinaryAssociation(
    name="macro20",
    ends={
        Property(name="eTJ_Macro", type=eTJ_MacroCall, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_MacroCall", type=eTJ_Macro, multiplicity=Multiplicity(0, 1))
    }
)
attributes24: BinaryAssociation = BinaryAssociation(
    name="attributes24",
    ends={
        Property(name="eTJ_ResourceAttribute", type=eTJ_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Resource", type=eTJ_ResourceAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes21: BinaryAssociation = BinaryAssociation(
    name="attributes21",
    ends={
        Property(name="eTJ_ReportAttribute", type=eTJ_Report, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Report", type=eTJ_ReportAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes22: BinaryAssociation = BinaryAssociation(
    name="attributes22",
    ends={
        Property(name="eTJ_IcalReportAttribute", type=eTJ_IcalReport, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_IcalReport", type=eTJ_IcalReportAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes23: BinaryAssociation = BinaryAssociation(
    name="attributes23",
    ends={
        Property(name="eTJ_ExportAttribute", type=eTJ_Export, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Export", type=eTJ_ExportAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources25: BinaryAssociation = BinaryAssociation(
    name="resources25",
    ends={
        Property(name="eTJ_AllocateResource", type=eTJ_Allocate, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Allocate", type=eTJ_AllocateResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resource26: BinaryAssociation = BinaryAssociation(
    name="resource26",
    ends={
        Property(name="eTJ_Resource28", type=eTJ_AllocateResource, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_AllocateResource27", type=eTJ_Resource, multiplicity=Multiplicity(0, 1))
    }
)
attributes29: BinaryAssociation = BinaryAssociation(
    name="attributes29",
    ends={
        Property(name="eTJ_AllocateResourceAttribute", type=eTJ_AllocateResource, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_AllocateResource30", type=eTJ_AllocateResourceAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes31: BinaryAssociation = BinaryAssociation(
    name="attributes31",
    ends={
        Property(name="eTJ_NavigatorAttribute", type=eTJ_Navigator, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Navigator", type=eTJ_NavigatorAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes32: BinaryAssociation = BinaryAssociation(
    name="attributes32",
    ends={
        Property(name="eTJ_NewTaskAttribute", type=eTJ_NewTask, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_NewTask", type=eTJ_NewTaskAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes33: BinaryAssociation = BinaryAssociation(
    name="attributes33",
    ends={
        Property(name="eTJ_NikuReportAttribute", type=eTJ_NikuReport, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_NikuReport", type=eTJ_NikuReportAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources34: BinaryAssociation = BinaryAssociation(
    name="resources34",
    ends={
        Property(name="eTJ_Resource35", type=eTJ_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Alternative", type=eTJ_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
resource36: BinaryAssociation = BinaryAssociation(
    name="resource36",
    ends={
        Property(name="eTJ_Resource37", type=eTJ_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Author", type=eTJ_Resource, multiplicity=Multiplicity(0, 1))
    }
)
cost38: BinaryAssociation = BinaryAssociation(
    name="cost38",
    ends={
        Property(name="eTJ_Account39", type=eTJ_Balance, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Balance", type=eTJ_Account, multiplicity=Multiplicity(0, 1))
    }
)
revenue40: BinaryAssociation = BinaryAssociation(
    name="revenue40",
    ends={
        Property(name="eTJ_Account42", type=eTJ_Balance, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Balance41", type=eTJ_Account, multiplicity=Multiplicity(0, 1))
    }
)
interval43: BinaryAssociation = BinaryAssociation(
    name="interval43",
    ends={
        Property(name="eTJ_Interval4", type=eTJ_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Booking", type=eTJ_Interval4, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resource44: BinaryAssociation = BinaryAssociation(
    name="resource44",
    ends={
        Property(name="eTJ_Resource45", type=eTJ_BookingTask, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_BookingTask", type=eTJ_Resource, multiplicity=Multiplicity(0, 1))
    }
)
booking46: BinaryAssociation = BinaryAssociation(
    name="booking46",
    ends={
        Property(name="eTJ_Booking48", type=eTJ_BookingTask, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_BookingTask47", type=eTJ_Booking, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
task49: BinaryAssociation = BinaryAssociation(
    name="task49",
    ends={
        Property(name="eTJ_Task50", type=eTJ_BookingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_BookingResource", type=eTJ_Task, multiplicity=Multiplicity(0, 1))
    }
)
booking51: BinaryAssociation = BinaryAssociation(
    name="booking51",
    ends={
        Property(name="eTJ_Booking53", type=eTJ_BookingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_BookingResource52", type=eTJ_Booking, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression54: BinaryAssociation = BinaryAssociation(
    name="expression54",
    ends={
        Property(name="eTJ_LogicalExpression", type=eTJ_CellColor, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_CellColor", type=eTJ_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color55: BinaryAssociation = BinaryAssociation(
    name="color55",
    ends={
        Property(name="eTJ_RGB", type=eTJ_CellColor, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_CellColor56", type=eTJ_RGB, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expresssion57: BinaryAssociation = BinaryAssociation(
    name="expresssion57",
    ends={
        Property(name="eTJ_LogicalExpression58", type=eTJ_CellText, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_CellText", type=eTJ_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accountShares59: BinaryAssociation = BinaryAssociation(
    name="accountShares59",
    ends={
        Property(name="eTJ_AccountShare", type=eTJ_ChargeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ChargeSet", type=eTJ_AccountShare, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns60: BinaryAssociation = BinaryAssociation(
    name="columns60",
    ends={
        Property(name="eTJ_Column", type=eTJ_Columns, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Columns", type=eTJ_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
date61: BinaryAssociation = BinaryAssociation(
    name="date61",
    ends={
        Property(name="eTJ_ISODATE", type=eTJ_Credit, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Credit", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effort64: BinaryAssociation = BinaryAssociation(
    name="effort64",
    ends={
        Property(name="eTJ_Effort", type=eTJ_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="eTJ_DurationQuantity65", type=eTJ_Effort, multiplicity=Multiplicity(1, 1))
    }
)
dependency62: BinaryAssociation = BinaryAssociation(
    name="dependency62",
    ends={
        Property(name="eTJ_TaskDependency", type=eTJ_Depends, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Depends", type=eTJ_TaskDependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
duration63: BinaryAssociation = BinaryAssociation(
    name="duration63",
    ends={
        Property(name="eTJ_DurationQuantity", type=eTJ_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Duration", type=eTJ_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end66: BinaryAssociation = BinaryAssociation(
    name="end66",
    ends={
        Property(name="eTJ_ISODATE67", type=eTJ_End, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_End", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends68: BinaryAssociation = BinaryAssociation(
    name="extends68",
    ends={
        Property(name="eTJ_Extend", type=eTJ_ExtendResource, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ExtendResource", type=eTJ_Extend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extend69: BinaryAssociation = BinaryAssociation(
    name="extend69",
    ends={
        Property(name="eTJ_Extend70", type=eTJ_ExtendedResourceAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ExtendedResourceAttribute", type=eTJ_Extend, multiplicity=Multiplicity(0, 1))
    }
)
extends71: BinaryAssociation = BinaryAssociation(
    name="extends71",
    ends={
        Property(name="eTJ_Extend72", type=eTJ_ExtendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ExtendTask", type=eTJ_Extend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extend73: BinaryAssociation = BinaryAssociation(
    name="extend73",
    ends={
        Property(name="eTJ_Extend74", type=eTJ_ExtendedTaskAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ExtendedTaskAttribute", type=eTJ_Extend, multiplicity=Multiplicity(0, 1))
    }
)
expression75: BinaryAssociation = BinaryAssociation(
    name="expression75",
    ends={
        Property(name="eTJ_LogicalExpression76", type=eTJ_Fail, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Fail", type=eTJ_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
date77: BinaryAssociation = BinaryAssociation(
    name="date77",
    ends={
        Property(name="eTJ_ISODATE78", type=eTJ_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Function", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scenario79: BinaryAssociation = BinaryAssociation(
    name="scenario79",
    ends={
        Property(name="eTJ_Scenario81", type=eTJ_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Function80", type=eTJ_Scenario, multiplicity=Multiplicity(0, 1))
    }
)
task82: BinaryAssociation = BinaryAssociation(
    name="task82",
    ends={
        Property(name="eTJ_Task84", type=eTJ_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Function83", type=eTJ_Task, multiplicity=Multiplicity(0, 1))
    }
)
resource85: BinaryAssociation = BinaryAssociation(
    name="resource85",
    ends={
        Property(name="eTJ_Resource87", type=eTJ_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Function86", type=eTJ_Resource, multiplicity=Multiplicity(0, 1))
    }
)
expression88: BinaryAssociation = BinaryAssociation(
    name="expression88",
    ends={
        Property(name="eTJ_LogicalExpression89", type=eTJ_HAlign, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_HAlign", type=eTJ_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression94: BinaryAssociation = BinaryAssociation(
    name="expression94",
    ends={
        Property(name="eTJ_LogicalExpression95", type=eTJ_HideTask, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_HideTask", type=eTJ_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression90: BinaryAssociation = BinaryAssociation(
    name="expression90",
    ends={
        Property(name="eTJ_LogicalExpression91", type=eTJ_HideReport, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_HideReport", type=eTJ_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression92: BinaryAssociation = BinaryAssociation(
    name="expression92",
    ends={
        Property(name="eTJ_LogicalExpression93", type=eTJ_HideResource, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_HideResource", type=eTJ_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes96: BinaryAssociation = BinaryAssociation(
    name="attributes96",
    ends={
        Property(name="eTJ_IncludePropertiesAttribute", type=eTJ_IncludeProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_IncludeProperties", type=eTJ_IncludePropertiesAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start97: BinaryAssociation = BinaryAssociation(
    name="start97",
    ends={
        Property(name="eTJ_ISODATE98", type=eTJ_Interval1, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Interval1", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end99: BinaryAssociation = BinaryAssociation(
    name="end99",
    ends={
        Property(name="eTJ_ISODATE101", type=eTJ_Interval1, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Interval1100", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration102: BinaryAssociation = BinaryAssociation(
    name="duration102",
    ends={
        Property(name="eTJ_DurationQuantity104", type=eTJ_Interval1, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Interval1103", type=eTJ_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start105: BinaryAssociation = BinaryAssociation(
    name="start105",
    ends={
        Property(name="eTJ_ISODATE107", type=eTJ_Interval2, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Interval2106", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration111: BinaryAssociation = BinaryAssociation(
    name="duration111",
    ends={
        Property(name="eTJ_DurationQuantity113", type=eTJ_Interval2, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Interval2112", type=eTJ_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end108: BinaryAssociation = BinaryAssociation(
    name="end108",
    ends={
        Property(name="eTJ_ISODATE110", type=eTJ_Interval2, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Interval2109", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start114: BinaryAssociation = BinaryAssociation(
    name="start114",
    ends={
        Property(name="eTJ_ISODATE116", type=eTJ_Interval3, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Interval3115", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end117: BinaryAssociation = BinaryAssociation(
    name="end117",
    ends={
        Property(name="eTJ_ISODATE119", type=eTJ_Interval3, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Interval3118", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration120: BinaryAssociation = BinaryAssociation(
    name="duration120",
    ends={
        Property(name="eTJ_DurationQuantity122", type=eTJ_Interval3, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Interval3121", type=eTJ_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start123: BinaryAssociation = BinaryAssociation(
    name="start123",
    ends={
        Property(name="eTJ_ISODATE125", type=eTJ_Interval4, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Interval4124", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end126: BinaryAssociation = BinaryAssociation(
    name="end126",
    ends={
        Property(name="eTJ_ISODATE128", type=eTJ_Interval4, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Interval4127", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration129: BinaryAssociation = BinaryAssociation(
    name="duration129",
    ends={
        Property(name="eTJ_DurationQuantity131", type=eTJ_Interval4, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Interval4130", type=eTJ_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
details139: BinaryAssociation = BinaryAssociation(
    name="details139",
    ends={
        Property(name="eTJ_Details", type=eTJ_JournalEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_JournalEntry140", type=eTJ_Details, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
date132: BinaryAssociation = BinaryAssociation(
    name="date132",
    ends={
        Property(name="eTJ_ISODATE133", type=eTJ_JournalEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_JournalEntry", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alert134: BinaryAssociation = BinaryAssociation(
    name="alert134",
    ends={
        Property(name="eTJ_Alert", type=eTJ_JournalEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_JournalEntry135", type=eTJ_Alert, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author136: BinaryAssociation = BinaryAssociation(
    name="author136",
    ends={
        Property(name="eTJ_Author138", type=eTJ_JournalEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_JournalEntry137", type=eTJ_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
summary141: BinaryAssociation = BinaryAssociation(
    name="summary141",
    ends={
        Property(name="eTJ_Summary", type=eTJ_JournalEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_JournalEntry142", type=eTJ_Summary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
length143: BinaryAssociation = BinaryAssociation(
    name="length143",
    ends={
        Property(name="eTJ_DurationQuantity144", type=eTJ_Length, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Length", type=eTJ_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes145: BinaryAssociation = BinaryAssociation(
    name="attributes145",
    ends={
        Property(name="eTJ_LimitsAttribute", type=eTJ_Limits, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Limits", type=eTJ_LimitsAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftOperant147: BinaryAssociation = BinaryAssociation(
    name="leftOperant147",
    ends={
        Property(name="eTJ_LogicalExpression148", type=eTJ_LogicalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_LogicalExpression146", type=eTJ_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand150: BinaryAssociation = BinaryAssociation(
    name="rightOperand150",
    ends={
        Property(name="eTJ_LogicalExpression151", type=eTJ_LogicalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_LogicalExpression149", type=eTJ_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties152: BinaryAssociation = BinaryAssociation(
    name="properties152",
    ends={
        Property(name="eTJ_Property154", type=eTJ_Macro, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Macro153", type=eTJ_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources155: BinaryAssociation = BinaryAssociation(
    name="resources155",
    ends={
        Property(name="eTJ_Resource156", type=eTJ_Managers, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Managers", type=eTJ_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
maxEnd157: BinaryAssociation = BinaryAssociation(
    name="maxEnd157",
    ends={
        Property(name="eTJ_ISODATE158", type=eTJ_MaxEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_MaxEnd", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxStart159: BinaryAssociation = BinaryAssociation(
    name="maxStart159",
    ends={
        Property(name="eTJ_ISODATE160", type=eTJ_MaxStart, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_MaxStart", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minEnd161: BinaryAssociation = BinaryAssociation(
    name="minEnd161",
    ends={
        Property(name="eTJ_ISODATE162", type=eTJ_MinEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_MinEnd", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minStart163: BinaryAssociation = BinaryAssociation(
    name="minStart163",
    ends={
        Property(name="eTJ_ISODATE164", type=eTJ_MinStart, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_MinStart", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
now165: BinaryAssociation = BinaryAssociation(
    name="now165",
    ends={
        Property(name="eTJ_ISODATE166", type=eTJ_Now, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Now", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
period167: BinaryAssociation = BinaryAssociation(
    name="period167",
    ends={
        Property(name="eTJ_Interval2168", type=eTJ_Period, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Period", type=eTJ_Interval2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
remaining169: BinaryAssociation = BinaryAssociation(
    name="remaining169",
    ends={
        Property(name="eTJ_DurationQuantity170", type=eTJ_Remaining, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Remaining", type=eTJ_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
report171: BinaryAssociation = BinaryAssociation(
    name="report171",
    ends={
        Property(name="eTJ_Report172", type=eTJ_ReportPrefix, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ReportPrefix", type=eTJ_Report, multiplicity=Multiplicity(0, 1))
    }
)
resource173: BinaryAssociation = BinaryAssociation(
    name="resource173",
    ends={
        Property(name="eTJ_Resource174", type=eTJ_ResourcePrefix, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ResourcePrefix", type=eTJ_Resource, multiplicity=Multiplicity(0, 1))
    }
)
expression181: BinaryAssociation = BinaryAssociation(
    name="expression181",
    ends={
        Property(name="eTJ_LogicalExpression182", type=eTJ_RollupResource, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_RollupResource", type=eTJ_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resource175: BinaryAssociation = BinaryAssociation(
    name="resource175",
    ends={
        Property(name="eTJ_Resource176", type=eTJ_ResourceRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ResourceRoot", type=eTJ_Resource, multiplicity=Multiplicity(0, 1))
    }
)
resources177: BinaryAssociation = BinaryAssociation(
    name="resources177",
    ends={
        Property(name="eTJ_Resource178", type=eTJ_Responsible, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Responsible", type=eTJ_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
expression179: BinaryAssociation = BinaryAssociation(
    name="expression179",
    ends={
        Property(name="eTJ_LogicalExpression180", type=eTJ_RollupAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_RollupAccount", type=eTJ_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scenario188: BinaryAssociation = BinaryAssociation(
    name="scenario188",
    ends={
        Property(name="eTJ_Scenario189", type=eTJ_ScenarioIcal, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ScenarioIcal", type=eTJ_Scenario, multiplicity=Multiplicity(0, 1))
    }
)
expression183: BinaryAssociation = BinaryAssociation(
    name="expression183",
    ends={
        Property(name="eTJ_LogicalExpression184", type=eTJ_RollupTask, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_RollupTask", type=eTJ_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scenario186: BinaryAssociation = BinaryAssociation(
    name="scenario186",
    ends={
        Property(name="eTJ_Scenario187", type=eTJ_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Scenario185", type=eTJ_Scenario, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scenarios190: BinaryAssociation = BinaryAssociation(
    name="scenarios190",
    ends={
        Property(name="eTJ_Scenario191", type=eTJ_Scenarios, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Scenarios", type=eTJ_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
shift201: BinaryAssociation = BinaryAssociation(
    name="shift201",
    ends={
        Property(name="eTJ_Shift203", type=eTJ_ShiftsLimit, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ShiftsLimit202", type=eTJ_Shift, multiplicity=Multiplicity(0, 1))
    }
)
limit204: BinaryAssociation = BinaryAssociation(
    name="limit204",
    ends={
        Property(name="eTJ_Interval2206", type=eTJ_ShiftsLimit, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ShiftsLimit205", type=eTJ_Interval2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vacation192: BinaryAssociation = BinaryAssociation(
    name="vacation192",
    ends={
        Property(name="eTJ_Vacation", type=eTJ_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Shift", type=eTJ_Vacation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift194: BinaryAssociation = BinaryAssociation(
    name="shift194",
    ends={
        Property(name="eTJ_Shift195", type=eTJ_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Shift193", type=eTJ_Shift, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workingHours196: BinaryAssociation = BinaryAssociation(
    name="workingHours196",
    ends={
        Property(name="eTJ_WorkingHours", type=eTJ_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Shift197", type=eTJ_WorkingHours, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift198: BinaryAssociation = BinaryAssociation(
    name="shift198",
    ends={
        Property(name="eTJ_Shift199", type=eTJ_ShiftTimesheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ShiftTimesheet", type=eTJ_Shift, multiplicity=Multiplicity(0, 1))
    }
)
limits200: BinaryAssociation = BinaryAssociation(
    name="limits200",
    ends={
        Property(name="eTJ_ShiftsLimit", type=eTJ_Shifts, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Shifts", type=eTJ_ShiftsLimit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shift207: BinaryAssociation = BinaryAssociation(
    name="shift207",
    ends={
        Property(name="eTJ_Shift208", type=eTJ_ShiftsAllocate, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ShiftsAllocate", type=eTJ_Shift, multiplicity=Multiplicity(0, 1))
    }
)
intervals209: BinaryAssociation = BinaryAssociation(
    name="intervals209",
    ends={
        Property(name="eTJ_Interval3211", type=eTJ_ShiftsAllocate, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ShiftsAllocate210", type=eTJ_Interval3, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
criteria212: BinaryAssociation = BinaryAssociation(
    name="criteria212",
    ends={
        Property(name="eTJ_Criterion", type=eTJ_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Sort", type=eTJ_Criterion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start213: BinaryAssociation = BinaryAssociation(
    name="start213",
    ends={
        Property(name="eTJ_ISODATE214", type=eTJ_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Start", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes222: BinaryAssociation = BinaryAssociation(
    name="attributes222",
    ends={
        Property(name="eTJ_StatusSheetAttribute", type=eTJ_StatusSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_StatusSheet223", type=eTJ_StatusSheetAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes215: BinaryAssociation = BinaryAssociation(
    name="attributes215",
    ends={
        Property(name="eTJ_StatusStatusSheetAttribute", type=eTJ_StatusStatusSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_StatusStatusSheet", type=eTJ_StatusStatusSheetAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes216: BinaryAssociation = BinaryAssociation(
    name="attributes216",
    ends={
        Property(name="eTJ_StatusTimesheetAttribute", type=eTJ_StatusTimesheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_StatusTimesheet", type=eTJ_StatusTimesheetAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resource217: BinaryAssociation = BinaryAssociation(
    name="resource217",
    ends={
        Property(name="eTJ_Resource218", type=eTJ_StatusSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_StatusSheet", type=eTJ_Resource, multiplicity=Multiplicity(0, 1))
    }
)
interval219: BinaryAssociation = BinaryAssociation(
    name="interval219",
    ends={
        Property(name="eTJ_Interval4221", type=eTJ_StatusSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_StatusSheet220", type=eTJ_Interval4, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes224: BinaryAssociation = BinaryAssociation(
    name="attributes224",
    ends={
        Property(name="eTJ_StatusSheetReportAttribute", type=eTJ_StatusSheetReport, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_StatusSheetReport", type=eTJ_StatusSheetReportAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
account225: BinaryAssociation = BinaryAssociation(
    name="account225",
    ends={
        Property(name="eTJ_Account226", type=eTJ_SupplementAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_SupplementAccount", type=eTJ_Account, multiplicity=Multiplicity(0, 1))
    }
)
attributes227: BinaryAssociation = BinaryAssociation(
    name="attributes227",
    ends={
        Property(name="eTJ_AccountAttribute229", type=eTJ_SupplementAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_SupplementAccount228", type=eTJ_AccountAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
report230: BinaryAssociation = BinaryAssociation(
    name="report230",
    ends={
        Property(name="eTJ_Report231", type=eTJ_SupplementReport, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_SupplementReport", type=eTJ_Report, multiplicity=Multiplicity(0, 1))
    }
)
attributes232: BinaryAssociation = BinaryAssociation(
    name="attributes232",
    ends={
        Property(name="eTJ_ReportAttribute234", type=eTJ_SupplementReport, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_SupplementReport233", type=eTJ_ReportAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rollupTask253: BinaryAssociation = BinaryAssociation(
    name="rollupTask253",
    ends={
        Property(name="eTJ_RollupTask255", type=eTJ_TagFile, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TagFile254", type=eTJ_RollupTask, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resource235: BinaryAssociation = BinaryAssociation(
    name="resource235",
    ends={
        Property(name="eTJ_Resource236", type=eTJ_SupplementResource, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_SupplementResource", type=eTJ_Resource, multiplicity=Multiplicity(0, 1))
    }
)
attributes237: BinaryAssociation = BinaryAssociation(
    name="attributes237",
    ends={
        Property(name="eTJ_ResourceAttribute239", type=eTJ_SupplementResource, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_SupplementResource238", type=eTJ_ResourceAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task240: BinaryAssociation = BinaryAssociation(
    name="task240",
    ends={
        Property(name="eTJ_Task241", type=eTJ_SupplementTask, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_SupplementTask", type=eTJ_Task, multiplicity=Multiplicity(0, 1))
    }
)
attributes242: BinaryAssociation = BinaryAssociation(
    name="attributes242",
    ends={
        Property(name="eTJ_TaskAttribute244", type=eTJ_SupplementTask, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_SupplementTask243", type=eTJ_TaskAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hideResource245: BinaryAssociation = BinaryAssociation(
    name="hideResource245",
    ends={
        Property(name="eTJ_HideResource246", type=eTJ_TagFile, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TagFile", type=eTJ_HideResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hideTask247: BinaryAssociation = BinaryAssociation(
    name="hideTask247",
    ends={
        Property(name="eTJ_HideTask249", type=eTJ_TagFile, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TagFile248", type=eTJ_HideTask, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rollupResource250: BinaryAssociation = BinaryAssociation(
    name="rollupResource250",
    ends={
        Property(name="eTJ_RollupResource252", type=eTJ_TagFile, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TagFile251", type=eTJ_RollupResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
task256: BinaryAssociation = BinaryAssociation(
    name="task256",
    ends={
        Property(name="eTJ_Task257", type=eTJ_TaskStatusSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TaskStatusSheet", type=eTJ_Task, multiplicity=Multiplicity(0, 1))
    }
)
attributes258: BinaryAssociation = BinaryAssociation(
    name="attributes258",
    ends={
        Property(name="eTJ_TaskStatusSheetAttribute", type=eTJ_TaskStatusSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TaskStatusSheet259", type=eTJ_TaskStatusSheetAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task260: BinaryAssociation = BinaryAssociation(
    name="task260",
    ends={
        Property(name="eTJ_Task261", type=eTJ_TaskTimesheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TaskTimesheet", type=eTJ_Task, multiplicity=Multiplicity(0, 1))
    }
)
attributes262: BinaryAssociation = BinaryAssociation(
    name="attributes262",
    ends={
        Property(name="eTJ_TaskTimesheetAttribute", type=eTJ_TaskTimesheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TaskTimesheet263", type=eTJ_TaskTimesheetAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task264: BinaryAssociation = BinaryAssociation(
    name="task264",
    ends={
        Property(name="eTJ_Task265", type=eTJ_TaskPrefix, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TaskPrefix", type=eTJ_Task, multiplicity=Multiplicity(0, 1))
    }
)
task266: BinaryAssociation = BinaryAssociation(
    name="task266",
    ends={
        Property(name="eTJ_Task267", type=eTJ_TaskRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TaskRoot", type=eTJ_Task, multiplicity=Multiplicity(0, 1))
    }
)
resource268: BinaryAssociation = BinaryAssociation(
    name="resource268",
    ends={
        Property(name="eTJ_Resource269", type=eTJ_Timesheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Timesheet", type=eTJ_Resource, multiplicity=Multiplicity(0, 1))
    }
)
interval270: BinaryAssociation = BinaryAssociation(
    name="interval270",
    ends={
        Property(name="eTJ_Interval4272", type=eTJ_Timesheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Timesheet271", type=eTJ_Interval4, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes273: BinaryAssociation = BinaryAssociation(
    name="attributes273",
    ends={
        Property(name="eTJ_TimesheetAttribute", type=eTJ_Timesheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Timesheet274", type=eTJ_TimesheetAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes275: BinaryAssociation = BinaryAssociation(
    name="attributes275",
    ends={
        Property(name="eTJ_TimesheetReportAttribute", type=eTJ_TimesheetReport, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TimesheetReport", type=eTJ_TimesheetReportAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intervals280: BinaryAssociation = BinaryAssociation(
    name="intervals280",
    ends={
        Property(name="eTJ_Interval3282", type=eTJ_Vacation, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Vacation281", type=eTJ_Interval3, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression283: BinaryAssociation = BinaryAssociation(
    name="expression283",
    ends={
        Property(name="eTJ_LogicalExpression284", type=eTJ_Warn, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Warn", type=eTJ_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression276: BinaryAssociation = BinaryAssociation(
    name="expression276",
    ends={
        Property(name="eTJ_LogicalExpression277", type=eTJ_ToolTip, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ToolTip", type=eTJ_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scenario278: BinaryAssociation = BinaryAssociation(
    name="scenario278",
    ends={
        Property(name="eTJ_Scenario279", type=eTJ_TrackingScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TrackingScenario", type=eTJ_Scenario, multiplicity=Multiplicity(0, 1))
    }
)
weekdays285: BinaryAssociation = BinaryAssociation(
    name="weekdays285",
    ends={
        Property(name="eTJ_Weekdays", type=eTJ_WorkingHours, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_WorkingHours286", type=eTJ_Weekdays, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hours287: BinaryAssociation = BinaryAssociation(
    name="hours287",
    ends={
        Property(name="eTJ_WorkHours", type=eTJ_WorkingHours, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_WorkingHours288", type=eTJ_WorkHours, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
account289: BinaryAssociation = BinaryAssociation(
    name="account289",
    ends={
        Property(name="eTJ_Account291", type=eTJ_AccountShare, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_AccountShare290", type=eTJ_Account, multiplicity=Multiplicity(0, 1))
    }
)
ext294: BinaryAssociation = BinaryAssociation(
    name="ext294",
    ends={
        Property(name="eTJ_ExtendedResourceAttributeColumn296", type=eTJ_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Column295", type=eTJ_ExtendedResourceAttributeColumn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes297: BinaryAssociation = BinaryAssociation(
    name="attributes297",
    ends={
        Property(name="eTJ_ColumnAttribute", type=eTJ_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Column298", type=eTJ_ColumnAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenario299: BinaryAssociation = BinaryAssociation(
    name="scenario299",
    ends={
        Property(name="eTJ_Scenario301", type=eTJ_Criterion, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Criterion300", type=eTJ_Scenario, multiplicity=Multiplicity(0, 1))
    }
)
extension292: BinaryAssociation = BinaryAssociation(
    name="extension292",
    ends={
        Property(name="eTJ_Extend293", type=eTJ_ExtendedResourceAttributeColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ExtendedResourceAttributeColumn", type=eTJ_Extend, multiplicity=Multiplicity(0, 1))
    }
)
duration302: BinaryAssociation = BinaryAssociation(
    name="duration302",
    ends={
        Property(name="eTJ_Limit", type=eTJ_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="eTJ_DurationQuantity303", type=eTJ_Limit, multiplicity=Multiplicity(1, 1))
    }
)
attributes304: BinaryAssociation = BinaryAssociation(
    name="attributes304",
    ends={
        Property(name="eTJ_LimitAttribute", type=eTJ_Limit, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_Limit305", type=eTJ_LimitAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
end306: BinaryAssociation = BinaryAssociation(
    name="end306",
    ends={
        Property(name="eTJ_ISODATE308", type=eTJ_LimitAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_LimitAttribute307", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
period309: BinaryAssociation = BinaryAssociation(
    name="period309",
    ends={
        Property(name="eTJ_Interval1311", type=eTJ_LimitAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_LimitAttribute310", type=eTJ_Interval1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resources312: BinaryAssociation = BinaryAssociation(
    name="resources312",
    ends={
        Property(name="eTJ_Resource314", type=eTJ_LimitAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_LimitAttribute313", type=eTJ_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
task318: BinaryAssociation = BinaryAssociation(
    name="task318",
    ends={
        Property(name="eTJ_Task320", type=eTJ_TaskDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TaskDependency319", type=eTJ_Task, multiplicity=Multiplicity(0, 1))
    }
)
gapDuration321: BinaryAssociation = BinaryAssociation(
    name="gapDuration321",
    ends={
        Property(name="eTJ_GapDuration", type=eTJ_TaskDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TaskDependency322", type=eTJ_GapDuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gapLength323: BinaryAssociation = BinaryAssociation(
    name="gapLength323",
    ends={
        Property(name="eTJ_GapLength", type=eTJ_TaskDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_TaskDependency324", type=eTJ_GapLength, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start315: BinaryAssociation = BinaryAssociation(
    name="start315",
    ends={
        Property(name="eTJ_ISODATE317", type=eTJ_LimitAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_LimitAttribute316", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
date325: BinaryAssociation = BinaryAssociation(
    name="date325",
    ends={
        Property(name="eTJ_ExtDate", type=eTJ_ISODATE, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ISODATE326", type=eTJ_ExtDate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration327: BinaryAssociation = BinaryAssociation(
    name="duration327",
    ends={
        Property(name="eTJ_DurationQuantity329", type=eTJ_ISODATE, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_ISODATE328", type=eTJ_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function330: BinaryAssociation = BinaryAssociation(
    name="function330",
    ends={
        Property(name="eTJ_Function331", type=eTJ_LogicalFunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_LogicalFunctionExpression", type=eTJ_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
macro332: BinaryAssociation = BinaryAssociation(
    name="macro332",
    ends={
        Property(name="eTJ_MacroCall333", type=eTJ_LogicalStringLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_LogicalStringLiteral", type=eTJ_MacroCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value334: BinaryAssociation = BinaryAssociation(
    name="value334",
    ends={
        Property(name="eTJ_ISODATE335", type=eTJ_LogicalDateLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_LogicalDateLiteral", type=eTJ_ISODATE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scenario336: BinaryAssociation = BinaryAssociation(
    name="scenario336",
    ends={
        Property(name="eTJ_Scenario337", type=eTJ_LogicalFlagExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eTJ_LogicalFlagExpression", type=eTJ_Scenario, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_eTJ_Leaves_Property = Generalization(general=Property_, specific=eTJ_Leaves)
gen_eTJ_Leaves_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_Leaves)
gen_eTJ_Account_Property = Generalization(general=Property_, specific=eTJ_Account)
gen_eTJ_Account_AccountAttribute = Generalization(general=AccountAttribute, specific=eTJ_Account)
gen_eTJ_AccountPrefix_IncludePropertiesAttribute = Generalization(general=IncludePropertiesAttribute, specific=eTJ_AccountPrefix)
gen_eTJ_AccountReport_Property = Generalization(general=Property_, specific=eTJ_AccountReport)
gen_eTJ_AccountReport_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_AccountReport)
gen_eTJ_AccountRoot_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_AccountRoot)
gen_eTJ_Task_Property = Generalization(general=Property_, specific=eTJ_Task)
gen_eTJ_MacroCall_End = Generalization(general=End, specific=eTJ_MacroCall)
gen_eTJ_MacroCall_Start = Generalization(general=Start, specific=eTJ_MacroCall)
gen_eTJ_MacroCall_ExtDate = Generalization(general=ExtDate, specific=eTJ_MacroCall)
gen_eTJ_Report_AccountReport = Generalization(general=AccountReport, specific=eTJ_Report)
gen_eTJ_Report_ResourceReport = Generalization(general=ResourceReport, specific=eTJ_Report)
gen_eTJ_Report_TaskReport = Generalization(general=TaskReport, specific=eTJ_Report)
gen_eTJ_Report_TextReport = Generalization(general=TextReport, specific=eTJ_Report)
gen_eTJ_IcalReport_Property = Generalization(general=Property_, specific=eTJ_IcalReport)
gen_eTJ_Export_Property = Generalization(general=Property_, specific=eTJ_Export)
gen_eTJ_Resource_Property = Generalization(general=Property_, specific=eTJ_Resource)
gen_eTJ_Resource_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_Resource)
gen_eTJ_Allocate_Property = Generalization(general=Property_, specific=eTJ_Allocate)
gen_eTJ_Navigator_Property = Generalization(general=Property_, specific=eTJ_Navigator)
gen_eTJ_NewTask_TimesheetAttribute = Generalization(general=TimesheetAttribute, specific=eTJ_NewTask)
gen_eTJ_Balance_Property = Generalization(general=Property_, specific=eTJ_Balance)
gen_eTJ_Balance_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Balance)
gen_eTJ_NikuReport_Property = Generalization(general=Property_, specific=eTJ_NikuReport)
gen_eTJ_Alternative_AllocateResourceAttribute = Generalization(general=AllocateResourceAttribute, specific=eTJ_Alternative)
gen_eTJ_Author_StatusStatusSheetAttribute = Generalization(general=StatusStatusSheetAttribute, specific=eTJ_Author)
gen_eTJ_Caption_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Caption)
gen_eTJ_BookingResource_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_BookingResource)
gen_eTJ_Columns_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Columns)
gen_eTJ_CellColor_Property = Generalization(general=Property_, specific=eTJ_CellColor)
gen_eTJ_CellColor_ColumnAttribute = Generalization(general=ColumnAttribute, specific=eTJ_CellColor)
gen_eTJ_CellText_ColumnAttribute = Generalization(general=ColumnAttribute, specific=eTJ_CellText)
gen_eTJ_Center_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Center)
gen_eTJ_DailyMin_LimitsAttribute = Generalization(general=LimitsAttribute, specific=eTJ_DailyMin)
gen_eTJ_Copyright_Property = Generalization(general=Property_, specific=eTJ_Copyright)
gen_eTJ_Credit_AccountAttribute = Generalization(general=AccountAttribute, specific=eTJ_Credit)
gen_eTJ_Currency_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_Currency)
gen_eTJ_CurrencyFormat_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_CurrencyFormat)
gen_eTJ_CurrencyFormat_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_CurrencyFormat)
gen_eTJ_DailyMax_LimitsAttribute = Generalization(general=LimitsAttribute, specific=eTJ_DailyMax)
gen_eTJ_DailyWorkingHours_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_DailyWorkingHours)
gen_eTJ_Email_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_Email)
gen_eTJ_Definitions_ExportAttribute = Generalization(general=ExportAttribute, specific=eTJ_Definitions)
gen_eTJ_Details_StatusStatusSheetAttribute = Generalization(general=StatusStatusSheetAttribute, specific=eTJ_Details)
gen_eTJ_Details_StatusTimesheetAttribute = Generalization(general=StatusTimesheetAttribute, specific=eTJ_Details)
gen_eTJ_Efficiency_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_Efficiency)
gen_eTJ_End_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_End)
gen_eTJ_End_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=eTJ_End)
gen_eTJ_End_ExportAttribute = Generalization(general=ExportAttribute, specific=eTJ_End)
gen_eTJ_End_NewTaskAttribute = Generalization(general=NewTaskAttribute, specific=eTJ_End)
gen_eTJ_End_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=eTJ_End)
gen_eTJ_End_StatusSheetReportAttribute = Generalization(general=StatusSheetReportAttribute, specific=eTJ_End)
gen_eTJ_End_TaskTimesheetAttribute = Generalization(general=TaskTimesheetAttribute, specific=eTJ_End)
gen_eTJ_End_TimesheetReportAttribute = Generalization(general=TimesheetReportAttribute, specific=eTJ_End)
gen_eTJ_End_ColumnAttribute = Generalization(general=ColumnAttribute, specific=eTJ_End)
gen_eTJ_Epilog_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Epilog)
gen_eTJ_ExtendResource_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_ExtendResource)
gen_eTJ_ExtendedResourceAttribute_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_ExtendedResourceAttribute)
gen_eTJ_ExtendTask_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_ExtendTask)
gen_eTJ_Fail_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_Fail)
gen_eTJ_Flags_Property = Generalization(general=Property_, specific=eTJ_Flags)
gen_eTJ_Flags_AccountAttribute = Generalization(general=AccountAttribute, specific=eTJ_Flags)
gen_eTJ_Flags_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Flags)
gen_eTJ_Flags_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_Flags)
gen_eTJ_Flags_StatusStatusSheetAttribute = Generalization(general=StatusStatusSheetAttribute, specific=eTJ_Flags)
gen_eTJ_Flags_StatusTimesheetAttribute = Generalization(general=StatusTimesheetAttribute, specific=eTJ_Flags)
gen_eTJ_FontColor_ColumnAttribute = Generalization(general=ColumnAttribute, specific=eTJ_FontColor)
gen_eTJ_Footer_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Footer)
gen_eTJ_Formats_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Formats)
gen_eTJ_Formats_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=eTJ_Formats)
gen_eTJ_HAlign_ColumnAttribute = Generalization(general=ColumnAttribute, specific=eTJ_HAlign)
gen_eTJ_Header_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Header)
gen_eTJ_Headline_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Headline)
gen_eTJ_Headline_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=eTJ_Headline)
gen_eTJ_HideAccount_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_HideAccount)
gen_eTJ_HideJournalEntry_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_HideJournalEntry)
gen_eTJ_HideJournalEntry_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=eTJ_HideJournalEntry)
gen_eTJ_HideReport_NavigatorAttribute = Generalization(general=NavigatorAttribute, specific=eTJ_HideReport)
gen_eTJ_HideResource_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_HideResource)
gen_eTJ_HideResource_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=eTJ_HideResource)
gen_eTJ_HideResource_ExportAttribute = Generalization(general=ExportAttribute, specific=eTJ_HideResource)
gen_eTJ_HideResource_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=eTJ_HideResource)
gen_eTJ_HideResource_StatusSheetReportAttribute = Generalization(general=StatusSheetReportAttribute, specific=eTJ_HideResource)
gen_eTJ_HideResource_TimesheetReportAttribute = Generalization(general=TimesheetReportAttribute, specific=eTJ_HideResource)
gen_eTJ_HideTask_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_HideTask)
gen_eTJ_HideTask_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=eTJ_HideTask)
gen_eTJ_HideTask_ExportAttribute = Generalization(general=ExportAttribute, specific=eTJ_HideTask)
gen_eTJ_HideTask_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=eTJ_HideTask)
gen_eTJ_HideTask_StatusSheetReportAttribute = Generalization(general=StatusSheetReportAttribute, specific=eTJ_HideTask)
gen_eTJ_Include_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_Include)
gen_eTJ_IncludeProperties_Property = Generalization(general=Property_, specific=eTJ_IncludeProperties)
gen_eTJ_JournalAttributes_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_JournalAttributes)
gen_eTJ_JournalEntry_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_JournalEntry)
gen_eTJ_JournalEntry_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_JournalEntry)
gen_eTJ_ListType_ColumnAttribute = Generalization(general=ColumnAttribute, specific=eTJ_ListType)
gen_eTJ_JournalMode_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_JournalMode)
gen_eTJ_Left_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Left)
gen_eTJ_Limits_Property = Generalization(general=Property_, specific=eTJ_Limits)
gen_eTJ_Limits_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_Limits)
gen_eTJ_ListItem_ColumnAttribute = Generalization(general=ColumnAttribute, specific=eTJ_ListItem)
gen_eTJ_Mandatory_AllocateResourceAttribute = Generalization(general=AllocateResourceAttribute, specific=eTJ_Mandatory)
gen_eTJ_LoadUnit_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_LoadUnit)
gen_eTJ_Macro_Property = Generalization(general=Property_, specific=eTJ_Macro)
gen_eTJ_Managers_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_Managers)
gen_eTJ_MonthlyMax_LimitsAttribute = Generalization(general=LimitsAttribute, specific=eTJ_MonthlyMax)
gen_eTJ_MonthlyMin_LimitsAttribute = Generalization(general=LimitsAttribute, specific=eTJ_MonthlyMin)
gen_eTJ_Maximum_LimitsAttribute = Generalization(general=LimitsAttribute, specific=eTJ_Maximum)
gen_eTJ_Minimum_LimitsAttribute = Generalization(general=LimitsAttribute, specific=eTJ_Minimum)
gen_eTJ_Priority_NewTaskAttribute = Generalization(general=NewTaskAttribute, specific=eTJ_Priority)
gen_eTJ_Now_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_Now)
gen_eTJ_NumberFormat_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_NumberFormat)
gen_eTJ_NumberFormat_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_NumberFormat)
gen_eTJ_NumberFormat_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=eTJ_NumberFormat)
gen_eTJ_Period_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Period)
gen_eTJ_Period_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=eTJ_Period)
gen_eTJ_Period_ExportAttribute = Generalization(general=ExportAttribute, specific=eTJ_Period)
gen_eTJ_Period_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=eTJ_Period)
gen_eTJ_Period_StatusSheetReportAttribute = Generalization(general=StatusSheetReportAttribute, specific=eTJ_Period)
gen_eTJ_Period_TimesheetReportAttribute = Generalization(general=TimesheetReportAttribute, specific=eTJ_Period)
gen_eTJ_Period_ColumnAttribute = Generalization(general=ColumnAttribute, specific=eTJ_Period)
gen_eTJ_Persistent_AllocateResourceAttribute = Generalization(general=AllocateResourceAttribute, specific=eTJ_Persistent)
gen_eTJ_Priority_TaskTimesheetAttribute = Generalization(general=TaskTimesheetAttribute, specific=eTJ_Priority)
gen_eTJ_ProjectIds_Property = Generalization(general=Property_, specific=eTJ_ProjectIds)
gen_eTJ_Prolog_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Prolog)
gen_eTJ_PurgeReport_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_PurgeReport)
gen_eTJ_Rate_Property = Generalization(general=Property_, specific=eTJ_Rate)
gen_eTJ_Rate_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_Rate)
gen_eTJ_PurgeResource_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_PurgeResource)
gen_eTJ_Remaining_NewTaskAttribute = Generalization(general=NewTaskAttribute, specific=eTJ_Remaining)
gen_eTJ_Remaining_TaskTimesheetAttribute = Generalization(general=TaskTimesheetAttribute, specific=eTJ_Remaining)
gen_eTJ_ResourceReport_Property = Generalization(general=Property_, specific=eTJ_ResourceReport)
gen_eTJ_ResourceReport_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_ResourceReport)
gen_eTJ_ResourceRoot_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_ResourceRoot)
gen_eTJ_ReportPrefix_IncludePropertiesAttribute = Generalization(general=IncludePropertiesAttribute, specific=eTJ_ReportPrefix)
gen_eTJ_ResourceAttributes_ExportAttribute = Generalization(general=ExportAttribute, specific=eTJ_ResourceAttributes)
gen_eTJ_ResourcePrefix_IncludePropertiesAttribute = Generalization(general=IncludePropertiesAttribute, specific=eTJ_ResourcePrefix)
gen_eTJ_Right_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Right)
gen_eTJ_RollupAccount_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_RollupAccount)
gen_eTJ_RollupResource_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_RollupResource)
gen_eTJ_RollupResource_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=eTJ_RollupResource)
gen_eTJ_RollupResource_ExportAttribute = Generalization(general=ExportAttribute, specific=eTJ_RollupResource)
gen_eTJ_ScenarioIcal_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=eTJ_ScenarioIcal)
gen_eTJ_RollupTask_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_RollupTask)
gen_eTJ_RollupTask_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=eTJ_RollupTask)
gen_eTJ_RollupTask_ExportAttribute = Generalization(general=ExportAttribute, specific=eTJ_RollupTask)
gen_eTJ_Scale_ColumnAttribute = Generalization(general=ColumnAttribute, specific=eTJ_Scale)
gen_eTJ_Scenario_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_Scenario)
gen_eTJ_Scenarios_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Scenarios)
gen_eTJ_Scenarios_ExportAttribute = Generalization(general=ExportAttribute, specific=eTJ_Scenarios)
gen_eTJ_Select_AllocateResourceAttribute = Generalization(general=AllocateResourceAttribute, specific=eTJ_Select)
gen_eTJ_SelfContained_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_SelfContained)
gen_eTJ_Shift_Property = Generalization(general=Property_, specific=eTJ_Shift)
gen_eTJ_ShiftTimesheet_TimesheetAttribute = Generalization(general=TimesheetAttribute, specific=eTJ_ShiftTimesheet)
gen_eTJ_Shifts_ShiftsResource = Generalization(general=ShiftsResource, specific=eTJ_Shifts)
gen_eTJ_Shifts_ShiftsTask = Generalization(general=ShiftsTask, specific=eTJ_Shifts)
gen_eTJ_ShiftsAllocate_AllocateResourceAttribute = Generalization(general=AllocateResourceAttribute, specific=eTJ_ShiftsAllocate)
gen_eTJ_ShiftsResource_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_ShiftsResource)
gen_eTJ_ShortTimeFormat_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_ShortTimeFormat)
gen_eTJ_Sort_SortAccounts = Generalization(general=SortAccounts, specific=eTJ_Sort)
gen_eTJ_Sort_SortJournalEntries = Generalization(general=SortJournalEntries, specific=eTJ_Sort)
gen_eTJ_Sort_SortResources = Generalization(general=SortResources, specific=eTJ_Sort)
gen_eTJ_StatusStatusSheet_TaskStatusSheetAttribute = Generalization(general=TaskStatusSheetAttribute, specific=eTJ_StatusStatusSheet)
gen_eTJ_Sort_SortTasks = Generalization(general=SortTasks, specific=eTJ_Sort)
gen_eTJ_SortAccounts_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_SortAccounts)
gen_eTJ_SortJournalEntries_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_SortJournalEntries)
gen_eTJ_SortResources_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_SortResources)
gen_eTJ_SortResources_StatusSheetReportAttribute = Generalization(general=StatusSheetReportAttribute, specific=eTJ_SortResources)
gen_eTJ_SortTasks_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_SortTasks)
gen_eTJ_SortTasks_StatusSheetReportAttribute = Generalization(general=StatusSheetReportAttribute, specific=eTJ_SortTasks)
gen_eTJ_Start_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Start)
gen_eTJ_Start_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=eTJ_Start)
gen_eTJ_Start_ExportAttribute = Generalization(general=ExportAttribute, specific=eTJ_Start)
gen_eTJ_Start_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=eTJ_Start)
gen_eTJ_Start_StatusSheetReportAttribute = Generalization(general=StatusSheetReportAttribute, specific=eTJ_Start)
gen_eTJ_Start_TimesheetReportAttribute = Generalization(general=TimesheetReportAttribute, specific=eTJ_Start)
gen_eTJ_Start_ColumnAttribute = Generalization(general=ColumnAttribute, specific=eTJ_Start)
gen_eTJ_StatusTimesheet_TaskTimesheetAttribute = Generalization(general=TaskTimesheetAttribute, specific=eTJ_StatusTimesheet)
gen_eTJ_StatusTimesheet_TimesheetAttribute = Generalization(general=TimesheetAttribute, specific=eTJ_StatusTimesheet)
gen_eTJ_StatusSheet_Property = Generalization(general=Property_, specific=eTJ_StatusSheet)
gen_eTJ_SupplementResource_Property = Generalization(general=Property_, specific=eTJ_SupplementResource)
gen_eTJ_SupplementResource_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_SupplementResource)
gen_eTJ_StatusSheetReport_Property = Generalization(general=Property_, specific=eTJ_StatusSheetReport)
gen_eTJ_Summary_StatusStatusSheetAttribute = Generalization(general=StatusStatusSheetAttribute, specific=eTJ_Summary)
gen_eTJ_Summary_StatusTimesheetAttribute = Generalization(general=StatusTimesheetAttribute, specific=eTJ_Summary)
gen_eTJ_SupplementAccount_Property = Generalization(general=Property_, specific=eTJ_SupplementAccount)
gen_eTJ_SupplementReport_Property = Generalization(general=Property_, specific=eTJ_SupplementReport)
gen_eTJ_SupplementTask_Property = Generalization(general=Property_, specific=eTJ_SupplementTask)
gen_eTJ_TagFile_Property = Generalization(general=Property_, specific=eTJ_TagFile)
gen_eTJ_TaskStatusSheet_StatusSheetAttribute = Generalization(general=StatusSheetAttribute, specific=eTJ_TaskStatusSheet)
gen_eTJ_TaskStatusSheet_TaskStatusSheetAttribute = Generalization(general=TaskStatusSheetAttribute, specific=eTJ_TaskStatusSheet)
gen_eTJ_TaskTimesheet_TimesheetAttribute = Generalization(general=TimesheetAttribute, specific=eTJ_TaskTimesheet)
gen_eTJ_TaskAttributes_ExportAttribute = Generalization(general=ExportAttribute, specific=eTJ_TaskAttributes)
gen_eTJ_Timesheet_Property = Generalization(general=Property_, specific=eTJ_Timesheet)
gen_eTJ_TaskPrefix_IncludePropertiesAttribute = Generalization(general=IncludePropertiesAttribute, specific=eTJ_TaskPrefix)
gen_eTJ_TaskReport_Property = Generalization(general=Property_, specific=eTJ_TaskReport)
gen_eTJ_TaskReport_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_TaskReport)
gen_eTJ_TaskRoot_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_TaskRoot)
gen_eTJ_TextReport_Property = Generalization(general=Property_, specific=eTJ_TextReport)
gen_eTJ_TextReport_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_TextReport)
gen_eTJ_TimeFormat_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_TimeFormat)
gen_eTJ_TimeFormat_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_TimeFormat)
gen_eTJ_Timeoff_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=eTJ_Timeoff)
gen_eTJ_TimingResolution_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_TimingResolution)
gen_eTJ_TimesheetReport_Property = Generalization(general=Property_, specific=eTJ_TimesheetReport)
gen_eTJ_Timezone_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_Timezone)
gen_eTJ_Timezone_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Timezone)
gen_eTJ_Timezone_ExportAttribute = Generalization(general=ExportAttribute, specific=eTJ_Timezone)
gen_eTJ_Title_ReportAttribute = Generalization(general=ReportAttribute, specific=eTJ_Title)
gen_eTJ_Title_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=eTJ_Title)
gen_eTJ_Warn_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_Warn)
gen_eTJ_Title_ColumnAttribute = Generalization(general=ColumnAttribute, specific=eTJ_Title)
gen_eTJ_ToolTip_Property = Generalization(general=Property_, specific=eTJ_ToolTip)
gen_eTJ_WeekStarts_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_WeekStarts)
gen_eTJ_ToolTip_ColumnAttribute = Generalization(general=ColumnAttribute, specific=eTJ_ToolTip)
gen_eTJ_WeeklyMax_LimitsAttribute = Generalization(general=LimitsAttribute, specific=eTJ_WeeklyMax)
gen_eTJ_TrackingScenario_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_TrackingScenario)
gen_eTJ_Vacation_Property = Generalization(general=Property_, specific=eTJ_Vacation)
gen_eTJ_Vacation_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_Vacation)
gen_eTJ_WorkingHours_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_WorkingHours)
gen_eTJ_WorkingHours_ResourceAttribute = Generalization(general=ResourceAttribute, specific=eTJ_WorkingHours)
gen_eTJ_YearlyWorkingDays_ProjectAttribute = Generalization(general=ProjectAttribute, specific=eTJ_YearlyWorkingDays)
gen_eTJ_WeeklyMin_LimitsAttribute = Generalization(general=LimitsAttribute, specific=eTJ_WeeklyMin)
gen_eTJ_Width_ColumnAttribute = Generalization(general=ColumnAttribute, specific=eTJ_Width)
gen_eTJ_Work_NewTaskAttribute = Generalization(general=NewTaskAttribute, specific=eTJ_Work)
gen_eTJ_Work_TaskTimesheetAttribute = Generalization(general=TaskTimesheetAttribute, specific=eTJ_Work)
gen_eTJ_DurationQuantity_GapDuration = Generalization(general=GapDuration, specific=eTJ_DurationQuantity)
gen_eTJ_DurationQuantity_GapLength = Generalization(general=GapLength, specific=eTJ_DurationQuantity)
gen_eTJ_ExtendedResourceAttributeColumn_ColumnAttribute = Generalization(general=ColumnAttribute, specific=eTJ_ExtendedResourceAttributeColumn)
gen_eTJ_Limit_DailyMax = Generalization(general=DailyMax, specific=eTJ_Limit)
gen_eTJ_Limit_DailyMin = Generalization(general=DailyMin, specific=eTJ_Limit)
gen_eTJ_Limit_Maximum = Generalization(general=Maximum, specific=eTJ_Limit)
gen_eTJ_Limit_Minimum = Generalization(general=Minimum, specific=eTJ_Limit)
gen_eTJ_Limit_MonthlyMax = Generalization(general=MonthlyMax, specific=eTJ_Limit)
gen_eTJ_Limit_MonthlyMin = Generalization(general=MonthlyMin, specific=eTJ_Limit)
gen_eTJ_Limit_WeeklyMax = Generalization(general=WeeklyMax, specific=eTJ_Limit)
gen_eTJ_Limit_WeeklyMin = Generalization(general=WeeklyMin, specific=eTJ_Limit)
gen_eTJ_TaskDependency_Precedes = Generalization(general=Precedes, specific=eTJ_TaskDependency)
gen_eTJ_RealFormat_CurrencyFormat = Generalization(general=CurrencyFormat, specific=eTJ_RealFormat)
gen_eTJ_RealFormat_NumberFormat = Generalization(general=NumberFormat, specific=eTJ_RealFormat)
gen_eTJ_RichText_ListItem = Generalization(general=ListItem, specific=eTJ_RichText)
gen_eTJ_RichText_Prolog = Generalization(general=Prolog, specific=eTJ_RichText)
gen_eTJ_RichText_Right = Generalization(general=Right, specific=eTJ_RichText)
gen_eTJ_RichText_Summary = Generalization(general=Summary, specific=eTJ_RichText)
gen_eTJ_RichText_Caption = Generalization(general=Caption, specific=eTJ_RichText)
gen_eTJ_RichText_Center = Generalization(general=Center, specific=eTJ_RichText)
gen_eTJ_RichText_Details = Generalization(general=Details, specific=eTJ_RichText)
gen_eTJ_RichText_Epilog = Generalization(general=Epilog, specific=eTJ_RichText)
gen_eTJ_RichText_Footer = Generalization(general=Footer, specific=eTJ_RichText)
gen_eTJ_RichText_Header = Generalization(general=Header, specific=eTJ_RichText)
gen_eTJ_RichText_Headline = Generalization(general=Headline, specific=eTJ_RichText)
gen_eTJ_RichText_Left = Generalization(general=Left, specific=eTJ_RichText)
gen_eTJ_LogicalAbsoluteIdExression_LogicalExpression = Generalization(general=LogicalExpression, specific=eTJ_LogicalAbsoluteIdExression)
gen_eTJ_LogicalBooleanLiteral_LogicalExpression = Generalization(general=LogicalExpression, specific=eTJ_LogicalBooleanLiteral)
gen_eTJ_LogicalNumeralLiteral_LogicalExpression = Generalization(general=LogicalExpression, specific=eTJ_LogicalNumeralLiteral)
gen_eTJ_LogicalStringLiteral_LogicalExpression = Generalization(general=LogicalExpression, specific=eTJ_LogicalStringLiteral)
gen_eTJ_Defintions_Definitions = Generalization(general=Definitions, specific=eTJ_Defintions)
gen_eTJ_LogicalFunctionExpression_LogicalExpression = Generalization(general=LogicalExpression, specific=eTJ_LogicalFunctionExpression)
gen_eTJ_LogicalDateLiteral_LogicalExpression = Generalization(general=LogicalExpression, specific=eTJ_LogicalDateLiteral)
gen_eTJ_LogicalFlagExpression_LogicalExpression = Generalization(general=LogicalExpression, specific=eTJ_LogicalFlagExpression)

# Domain Model
domain_model = DomainModel(
    name="eTJ",
    types={eTJ_Global, eTJ_Project, eTJ_Property, eTJ_Leaves, Property_, ResourceAttribute, eTJ_LeaveDetails, eTJ_Interval3, eTJ_Account, AccountAttribute, eTJ_AccountAttribute, eTJ_AccountPrefix, IncludePropertiesAttribute, eTJ_AccountReport, ReportAttribute, eTJ_AccountRoot, eTJ_Interval2, eTJ_ProjectAttribute, eTJ_Task, eTJ_TaskAttribute, eTJ_ReportAttribute, eTJ_Scenario, eTJ_EObject, eTJ_MacroCall, End, Start, ExtDate, eTJ_Macro, eTJ_Report, AccountReport, ResourceReport, TaskReport, TextReport, eTJ_ResourceAttribute, eTJ_IcalReport, eTJ_IcalReportAttribute, eTJ_Export, eTJ_ExportAttribute, eTJ_Resource, eTJ_Allocate, eTJ_AllocateResource, eTJ_AllocateResourceAttribute, eTJ_Navigator, eTJ_NavigatorAttribute, eTJ_NewTask, TimesheetAttribute, eTJ_Balance, eTJ_NewTaskAttribute, eTJ_NikuReport, eTJ_NikuReportAttribute, eTJ_Alert, eTJ_Alternative, AllocateResourceAttribute, eTJ_Author, StatusStatusSheetAttribute, eTJ_Caption, eTJ_Booking, eTJ_Interval4, eTJ_BookingTask, eTJ_BookingResource, eTJ_Columns, eTJ_Column, eTJ_CellColor, ColumnAttribute, eTJ_LogicalExpression, eTJ_RGB, eTJ_CellText, eTJ_Center, eTJ_Charge, eTJ_ChargeSet, eTJ_AccountShare, eTJ_DailyMin, eTJ_Complete, eTJ_Copyright, eTJ_Credit, eTJ_ISODATE, eTJ_Currency, ProjectAttribute, eTJ_CurrencyFormat, eTJ_DailyMax, LimitsAttribute, eTJ_DailyWorkingHours, eTJ_Email, eTJ_Definitions, ExportAttribute, eTJ_Depends, eTJ_TaskDependency, eTJ_Details, StatusTimesheetAttribute, eTJ_Duration, eTJ_DurationQuantity, eTJ_Efficiency, eTJ_Effort, eTJ_ExtendResource, eTJ_End, IcalReportAttribute, NewTaskAttribute, NikuReportAttribute, StatusSheetReportAttribute, TaskTimesheetAttribute, TimesheetReportAttribute, eTJ_EndCredit, eTJ_Epilog, eTJ_Extend, eTJ_ExtendedResourceAttribute, eTJ_ExtendTask, eTJ_ExtendedTaskAttribute, eTJ_Fail, eTJ_Flags, eTJ_FontColor, eTJ_Footer, eTJ_Formats, eTJ_Function, eTJ_GapDuration, eTJ_GapLength, eTJ_HAlign, eTJ_Header, eTJ_Headline, eTJ_HideAccount, eTJ_HideJournalEntry, eTJ_HideReport, NavigatorAttribute, eTJ_HideResource, eTJ_HideTask, eTJ_Include, eTJ_IncludeProperties, eTJ_IncludePropertiesAttribute, eTJ_Interval1, eTJ_JournalAttributes, eTJ_JournalEntry, eTJ_Summary, eTJ_JournalMode, eTJ_Left, eTJ_Length, eTJ_Limits, eTJ_LimitsAttribute, eTJ_ListItem, eTJ_ListType, eTJ_Mandatory, eTJ_LoadUnit, eTJ_Managers, eTJ_MonthlyMin, eTJ_MaxEnd, eTJ_Maximum, eTJ_MaxStart, eTJ_Milestone, eTJ_Minimum, eTJ_MinEnd, eTJ_MinStart, eTJ_MonthlyMax, eTJ_Precedes, eTJ_Priority, eTJ_Note, eTJ_Now, eTJ_NumberFormat, eTJ_Period, eTJ_Persistent, eTJ_PurgeResource, eTJ_ProjectId, eTJ_ProjectIds, eTJ_Prolog, eTJ_PurgeReport, eTJ_Rate, eTJ_Remaining, eTJ_PurgeTask, eTJ_ResourceReport, eTJ_ResourceRoot, eTJ_ReportPrefix, eTJ_ResourceAttributes, eTJ_ResourcePrefix, eTJ_Responsible, eTJ_Right, eTJ_RollupAccount, eTJ_RollupResource, eTJ_ScenarioIcal, eTJ_RollupTask, eTJ_Scale, eTJ_Scenarios, eTJ_Scheduled, eTJ_Scheduling, eTJ_Select, eTJ_SelfContained, eTJ_Shift, eTJ_Vacation, eTJ_WorkingHours, eTJ_ShiftTimesheet, eTJ_Shifts, ShiftsResource, ShiftsTask, eTJ_ShiftsLimit, eTJ_Criterion, eTJ_ShiftsAllocate, eTJ_ShiftsResource, eTJ_ShiftsTask, eTJ_ShortTimeFormat, eTJ_Sort, SortAccounts, SortJournalEntries, SortResources, eTJ_StatusStatusSheet, TaskStatusSheetAttribute, SortTasks, eTJ_SortAccounts, eTJ_SortJournalEntries, eTJ_SortResources, eTJ_SortTasks, eTJ_Start, eTJ_StatusSheetAttribute, eTJ_StatusStatusSheetAttribute, eTJ_StatusTimesheet, eTJ_StatusTimesheetAttribute, eTJ_StatusSheet, eTJ_SupplementResource, eTJ_StatusSheetReport, eTJ_StatusSheetReportAttribute, eTJ_SupplementAccount, eTJ_SupplementReport, eTJ_SupplementTask, eTJ_TagFile, eTJ_TaskStatusSheet, StatusSheetAttribute, eTJ_TaskStatusSheetAttribute, eTJ_TaskTimesheet, eTJ_TaskTimesheetAttribute, eTJ_TaskAttributes, eTJ_Timesheet, eTJ_TaskPrefix, eTJ_TaskReport, eTJ_TaskRoot, eTJ_TextReport, eTJ_TimeFormat, eTJ_Timeoff, eTJ_TimingResolution, eTJ_TimesheetAttribute, eTJ_TimesheetReport, eTJ_TimesheetReportAttribute, eTJ_Timezone, eTJ_Title, eTJ_Warn, eTJ_ToolTip, eTJ_WeekStarts, eTJ_WeeklyMax, eTJ_TrackingScenario, eTJ_TreeLevel, eTJ_Weekdays, eTJ_WorkHours, eTJ_YearlyWorkingDays, eTJ_WeeklyMin, eTJ_Width, eTJ_Work, GapDuration, GapLength, eTJ_ColumnAttribute, eTJ_ExtendedResourceAttributeColumn, eTJ_LimitAttribute, eTJ_Limit, DailyMax, DailyMin, Maximum, Minimum, MonthlyMax, MonthlyMin, WeeklyMax, WeeklyMin, Precedes, eTJ_RealFormat, CurrencyFormat, NumberFormat, ListItem, Prolog, Right, Summary, eTJ_RichText, Caption, Center, Details, Epilog, Footer, Header, Headline, Left, eTJ_ExtDate, eTJ_LogicalAbsoluteIdExression, eTJ_LogicalBooleanLiteral, eTJ_LogicalNumeralLiteral, eTJ_LogicalStringLiteral, eTJ_Defintions, Definitions, eTJ_LogicalFunctionExpression, LogicalExpression, eTJ_LogicalDateLiteral, eTJ_LogicalFlagExpression, LeaveType, BuildInMacro, JournalAttributeValues, PurgeReportAttribute, PurgeResourceAttribute, PurgeTaskAttribute, ChargeApplies, JournalModeValue, JournalEntrySortCriterion, ListTypeValues, Justification, ReportFormat, LoadDisplayUnit, ScaleResolution, CriterionDirection, YesNo, ColumnId, SelectArgument, AlertLevel, DependsPolicy, SchedulingPolicy, TimeUnit, WorkQuantityUnit, Weekday},
    associations={project0, properties1, details3, account7, interval4, attributes6, attributes15, account9, interval11, attributes13, scenario16, attr18, macro20, attributes24, attributes21, attributes22, attributes23, resources25, resource26, attributes29, attributes31, attributes32, attributes33, resources34, resource36, cost38, revenue40, interval43, resource44, booking46, task49, booking51, expression54, color55, expresssion57, accountShares59, columns60, date61, effort64, dependency62, duration63, end66, extends68, extend69, extends71, extend73, expression75, date77, scenario79, task82, resource85, expression88, expression94, expression90, expression92, attributes96, start97, end99, duration102, start105, duration111, end108, start114, end117, duration120, start123, end126, duration129, details139, date132, alert134, author136, summary141, length143, attributes145, leftOperant147, rightOperand150, properties152, resources155, maxEnd157, maxStart159, minEnd161, minStart163, now165, period167, remaining169, report171, resource173, expression181, resource175, resources177, expression179, scenario188, expression183, scenario186, scenarios190, shift201, limit204, vacation192, shift194, workingHours196, shift198, limits200, shift207, intervals209, criteria212, start213, attributes222, attributes215, attributes216, resource217, interval219, attributes224, account225, attributes227, report230, attributes232, rollupTask253, resource235, attributes237, task240, attributes242, hideResource245, hideTask247, rollupResource250, task256, attributes258, task260, attributes262, task264, task266, resource268, interval270, attributes273, attributes275, intervals280, expression283, expression276, scenario278, weekdays285, hours287, account289, ext294, attributes297, scenario299, extension292, duration302, attributes304, end306, period309, resources312, task318, gapDuration321, gapLength323, start315, date325, duration327, function330, macro332, value334, scenario336},
    generalizations={gen_eTJ_Leaves_Property, gen_eTJ_Leaves_ResourceAttribute, gen_eTJ_Account_Property, gen_eTJ_Account_AccountAttribute, gen_eTJ_AccountPrefix_IncludePropertiesAttribute, gen_eTJ_AccountReport_Property, gen_eTJ_AccountReport_ReportAttribute, gen_eTJ_AccountRoot_ReportAttribute, gen_eTJ_Task_Property, gen_eTJ_MacroCall_End, gen_eTJ_MacroCall_Start, gen_eTJ_MacroCall_ExtDate, gen_eTJ_Report_AccountReport, gen_eTJ_Report_ResourceReport, gen_eTJ_Report_TaskReport, gen_eTJ_Report_TextReport, gen_eTJ_IcalReport_Property, gen_eTJ_Export_Property, gen_eTJ_Resource_Property, gen_eTJ_Resource_ResourceAttribute, gen_eTJ_Allocate_Property, gen_eTJ_Navigator_Property, gen_eTJ_NewTask_TimesheetAttribute, gen_eTJ_Balance_Property, gen_eTJ_Balance_ReportAttribute, gen_eTJ_NikuReport_Property, gen_eTJ_Alternative_AllocateResourceAttribute, gen_eTJ_Author_StatusStatusSheetAttribute, gen_eTJ_Caption_ReportAttribute, gen_eTJ_BookingResource_ResourceAttribute, gen_eTJ_Columns_ReportAttribute, gen_eTJ_CellColor_Property, gen_eTJ_CellColor_ColumnAttribute, gen_eTJ_CellText_ColumnAttribute, gen_eTJ_Center_ReportAttribute, gen_eTJ_DailyMin_LimitsAttribute, gen_eTJ_Copyright_Property, gen_eTJ_Credit_AccountAttribute, gen_eTJ_Currency_ProjectAttribute, gen_eTJ_CurrencyFormat_ProjectAttribute, gen_eTJ_CurrencyFormat_ReportAttribute, gen_eTJ_DailyMax_LimitsAttribute, gen_eTJ_DailyWorkingHours_ProjectAttribute, gen_eTJ_Email_ResourceAttribute, gen_eTJ_Definitions_ExportAttribute, gen_eTJ_Details_StatusStatusSheetAttribute, gen_eTJ_Details_StatusTimesheetAttribute, gen_eTJ_Efficiency_ResourceAttribute, gen_eTJ_End_ReportAttribute, gen_eTJ_End_IcalReportAttribute, gen_eTJ_End_ExportAttribute, gen_eTJ_End_NewTaskAttribute, gen_eTJ_End_NikuReportAttribute, gen_eTJ_End_StatusSheetReportAttribute, gen_eTJ_End_TaskTimesheetAttribute, gen_eTJ_End_TimesheetReportAttribute, gen_eTJ_End_ColumnAttribute, gen_eTJ_Epilog_ReportAttribute, gen_eTJ_ExtendResource_ProjectAttribute, gen_eTJ_ExtendedResourceAttribute_ResourceAttribute, gen_eTJ_ExtendTask_ProjectAttribute, gen_eTJ_Fail_ResourceAttribute, gen_eTJ_Flags_Property, gen_eTJ_Flags_AccountAttribute, gen_eTJ_Flags_ReportAttribute, gen_eTJ_Flags_ResourceAttribute, gen_eTJ_Flags_StatusStatusSheetAttribute, gen_eTJ_Flags_StatusTimesheetAttribute, gen_eTJ_FontColor_ColumnAttribute, gen_eTJ_Footer_ReportAttribute, gen_eTJ_Formats_ReportAttribute, gen_eTJ_Formats_NikuReportAttribute, gen_eTJ_HAlign_ColumnAttribute, gen_eTJ_Header_ReportAttribute, gen_eTJ_Headline_ReportAttribute, gen_eTJ_Headline_NikuReportAttribute, gen_eTJ_HideAccount_ReportAttribute, gen_eTJ_HideJournalEntry_ReportAttribute, gen_eTJ_HideJournalEntry_IcalReportAttribute, gen_eTJ_HideReport_NavigatorAttribute, gen_eTJ_HideResource_ReportAttribute, gen_eTJ_HideResource_IcalReportAttribute, gen_eTJ_HideResource_ExportAttribute, gen_eTJ_HideResource_NikuReportAttribute, gen_eTJ_HideResource_StatusSheetReportAttribute, gen_eTJ_HideResource_TimesheetReportAttribute, gen_eTJ_HideTask_ReportAttribute, gen_eTJ_HideTask_IcalReportAttribute, gen_eTJ_HideTask_ExportAttribute, gen_eTJ_HideTask_NikuReportAttribute, gen_eTJ_HideTask_StatusSheetReportAttribute, gen_eTJ_Include_ProjectAttribute, gen_eTJ_IncludeProperties_Property, gen_eTJ_JournalAttributes_ReportAttribute, gen_eTJ_JournalEntry_ProjectAttribute, gen_eTJ_JournalEntry_ResourceAttribute, gen_eTJ_ListType_ColumnAttribute, gen_eTJ_JournalMode_ReportAttribute, gen_eTJ_Left_ReportAttribute, gen_eTJ_Limits_Property, gen_eTJ_Limits_ResourceAttribute, gen_eTJ_ListItem_ColumnAttribute, gen_eTJ_Mandatory_AllocateResourceAttribute, gen_eTJ_LoadUnit_ReportAttribute, gen_eTJ_Macro_Property, gen_eTJ_Managers_ResourceAttribute, gen_eTJ_MonthlyMax_LimitsAttribute, gen_eTJ_MonthlyMin_LimitsAttribute, gen_eTJ_Maximum_LimitsAttribute, gen_eTJ_Minimum_LimitsAttribute, gen_eTJ_Priority_NewTaskAttribute, gen_eTJ_Now_ProjectAttribute, gen_eTJ_NumberFormat_ProjectAttribute, gen_eTJ_NumberFormat_ReportAttribute, gen_eTJ_NumberFormat_NikuReportAttribute, gen_eTJ_Period_ReportAttribute, gen_eTJ_Period_IcalReportAttribute, gen_eTJ_Period_ExportAttribute, gen_eTJ_Period_NikuReportAttribute, gen_eTJ_Period_StatusSheetReportAttribute, gen_eTJ_Period_TimesheetReportAttribute, gen_eTJ_Period_ColumnAttribute, gen_eTJ_Persistent_AllocateResourceAttribute, gen_eTJ_Priority_TaskTimesheetAttribute, gen_eTJ_ProjectIds_Property, gen_eTJ_Prolog_ReportAttribute, gen_eTJ_PurgeReport_ReportAttribute, gen_eTJ_Rate_Property, gen_eTJ_Rate_ResourceAttribute, gen_eTJ_PurgeResource_ResourceAttribute, gen_eTJ_Remaining_NewTaskAttribute, gen_eTJ_Remaining_TaskTimesheetAttribute, gen_eTJ_ResourceReport_Property, gen_eTJ_ResourceReport_ReportAttribute, gen_eTJ_ResourceRoot_ReportAttribute, gen_eTJ_ReportPrefix_IncludePropertiesAttribute, gen_eTJ_ResourceAttributes_ExportAttribute, gen_eTJ_ResourcePrefix_IncludePropertiesAttribute, gen_eTJ_Right_ReportAttribute, gen_eTJ_RollupAccount_ReportAttribute, gen_eTJ_RollupResource_ReportAttribute, gen_eTJ_RollupResource_IcalReportAttribute, gen_eTJ_RollupResource_ExportAttribute, gen_eTJ_ScenarioIcal_IcalReportAttribute, gen_eTJ_RollupTask_ReportAttribute, gen_eTJ_RollupTask_IcalReportAttribute, gen_eTJ_RollupTask_ExportAttribute, gen_eTJ_Scale_ColumnAttribute, gen_eTJ_Scenario_ProjectAttribute, gen_eTJ_Scenarios_ReportAttribute, gen_eTJ_Scenarios_ExportAttribute, gen_eTJ_Select_AllocateResourceAttribute, gen_eTJ_SelfContained_ReportAttribute, gen_eTJ_Shift_Property, gen_eTJ_ShiftTimesheet_TimesheetAttribute, gen_eTJ_Shifts_ShiftsResource, gen_eTJ_Shifts_ShiftsTask, gen_eTJ_ShiftsAllocate_AllocateResourceAttribute, gen_eTJ_ShiftsResource_ResourceAttribute, gen_eTJ_ShortTimeFormat_ProjectAttribute, gen_eTJ_Sort_SortAccounts, gen_eTJ_Sort_SortJournalEntries, gen_eTJ_Sort_SortResources, gen_eTJ_StatusStatusSheet_TaskStatusSheetAttribute, gen_eTJ_Sort_SortTasks, gen_eTJ_SortAccounts_ReportAttribute, gen_eTJ_SortJournalEntries_ReportAttribute, gen_eTJ_SortResources_ReportAttribute, gen_eTJ_SortResources_StatusSheetReportAttribute, gen_eTJ_SortTasks_ReportAttribute, gen_eTJ_SortTasks_StatusSheetReportAttribute, gen_eTJ_Start_ReportAttribute, gen_eTJ_Start_IcalReportAttribute, gen_eTJ_Start_ExportAttribute, gen_eTJ_Start_NikuReportAttribute, gen_eTJ_Start_StatusSheetReportAttribute, gen_eTJ_Start_TimesheetReportAttribute, gen_eTJ_Start_ColumnAttribute, gen_eTJ_StatusTimesheet_TaskTimesheetAttribute, gen_eTJ_StatusTimesheet_TimesheetAttribute, gen_eTJ_StatusSheet_Property, gen_eTJ_SupplementResource_Property, gen_eTJ_SupplementResource_ResourceAttribute, gen_eTJ_StatusSheetReport_Property, gen_eTJ_Summary_StatusStatusSheetAttribute, gen_eTJ_Summary_StatusTimesheetAttribute, gen_eTJ_SupplementAccount_Property, gen_eTJ_SupplementReport_Property, gen_eTJ_SupplementTask_Property, gen_eTJ_TagFile_Property, gen_eTJ_TaskStatusSheet_StatusSheetAttribute, gen_eTJ_TaskStatusSheet_TaskStatusSheetAttribute, gen_eTJ_TaskTimesheet_TimesheetAttribute, gen_eTJ_TaskAttributes_ExportAttribute, gen_eTJ_Timesheet_Property, gen_eTJ_TaskPrefix_IncludePropertiesAttribute, gen_eTJ_TaskReport_Property, gen_eTJ_TaskReport_ReportAttribute, gen_eTJ_TaskRoot_ReportAttribute, gen_eTJ_TextReport_Property, gen_eTJ_TextReport_ReportAttribute, gen_eTJ_TimeFormat_ProjectAttribute, gen_eTJ_TimeFormat_ReportAttribute, gen_eTJ_Timeoff_NikuReportAttribute, gen_eTJ_TimingResolution_ProjectAttribute, gen_eTJ_TimesheetReport_Property, gen_eTJ_Timezone_ProjectAttribute, gen_eTJ_Timezone_ReportAttribute, gen_eTJ_Timezone_ExportAttribute, gen_eTJ_Title_ReportAttribute, gen_eTJ_Title_NikuReportAttribute, gen_eTJ_Warn_ResourceAttribute, gen_eTJ_Title_ColumnAttribute, gen_eTJ_ToolTip_Property, gen_eTJ_WeekStarts_ProjectAttribute, gen_eTJ_ToolTip_ColumnAttribute, gen_eTJ_WeeklyMax_LimitsAttribute, gen_eTJ_TrackingScenario_ProjectAttribute, gen_eTJ_Vacation_Property, gen_eTJ_Vacation_ResourceAttribute, gen_eTJ_WorkingHours_ProjectAttribute, gen_eTJ_WorkingHours_ResourceAttribute, gen_eTJ_YearlyWorkingDays_ProjectAttribute, gen_eTJ_WeeklyMin_LimitsAttribute, gen_eTJ_Width_ColumnAttribute, gen_eTJ_Work_NewTaskAttribute, gen_eTJ_Work_TaskTimesheetAttribute, gen_eTJ_DurationQuantity_GapDuration, gen_eTJ_DurationQuantity_GapLength, gen_eTJ_ExtendedResourceAttributeColumn_ColumnAttribute, gen_eTJ_Limit_DailyMax, gen_eTJ_Limit_DailyMin, gen_eTJ_Limit_Maximum, gen_eTJ_Limit_Minimum, gen_eTJ_Limit_MonthlyMax, gen_eTJ_Limit_MonthlyMin, gen_eTJ_Limit_WeeklyMax, gen_eTJ_Limit_WeeklyMin, gen_eTJ_TaskDependency_Precedes, gen_eTJ_RealFormat_CurrencyFormat, gen_eTJ_RealFormat_NumberFormat, gen_eTJ_RichText_ListItem, gen_eTJ_RichText_Prolog, gen_eTJ_RichText_Right, gen_eTJ_RichText_Summary, gen_eTJ_RichText_Caption, gen_eTJ_RichText_Center, gen_eTJ_RichText_Details, gen_eTJ_RichText_Epilog, gen_eTJ_RichText_Footer, gen_eTJ_RichText_Header, gen_eTJ_RichText_Headline, gen_eTJ_RichText_Left, gen_eTJ_LogicalAbsoluteIdExression_LogicalExpression, gen_eTJ_LogicalBooleanLiteral_LogicalExpression, gen_eTJ_LogicalNumeralLiteral_LogicalExpression, gen_eTJ_LogicalStringLiteral_LogicalExpression, gen_eTJ_Defintions_Definitions, gen_eTJ_LogicalFunctionExpression_LogicalExpression, gen_eTJ_LogicalDateLiteral_LogicalExpression, gen_eTJ_LogicalFlagExpression_LogicalExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)