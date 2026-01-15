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
PurgeReportAttribute: Enumeration = Enumeration(
    name="PurgeReportAttribute",
    literals={
            EnumerationLiteral(name="COLUMNS"),
			EnumerationLiteral(name="DEFINITIONS"),
			EnumerationLiteral(name="SORTTASKS"),
			EnumerationLiteral(name="FLAGS"),
			EnumerationLiteral(name="FORMATS"),
			EnumerationLiteral(name="JOURNALATTRIBUTES"),
			EnumerationLiteral(name="SCENARIOS"),
			EnumerationLiteral(name="SORTACCOUNTS"),
			EnumerationLiteral(name="SORTJOURNALENTRIES"),
			EnumerationLiteral(name="SORTRESOURCES")
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

Justification: Enumeration = Enumeration(
    name="Justification",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="RIGHT")
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

ListTypeValues: Enumeration = Enumeration(
    name="ListTypeValues",
    literals={
            EnumerationLiteral(name="BULLETS"),
			EnumerationLiteral(name="COMMA"),
			EnumerationLiteral(name="NUMBERED")
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
            EnumerationLiteral(name="YES"),
			EnumerationLiteral(name="NO")
    }
)

JournalEntrySortCriterion: Enumeration = Enumeration(
    name="JournalEntrySortCriterion",
    literals={
            EnumerationLiteral(name="DATE_UP"),
			EnumerationLiteral(name="ALERT_DOWN"),
			EnumerationLiteral(name="ALERT_UP"),
			EnumerationLiteral(name="PROPERTY_UP"),
			EnumerationLiteral(name="DATE_DOWN")
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

ReportFormat: Enumeration = Enumeration(
    name="ReportFormat",
    literals={
            EnumerationLiteral(name="CSV"),
			EnumerationLiteral(name="HTML"),
			EnumerationLiteral(name="NIKU")
    }
)

SelectArgument: Enumeration = Enumeration(
    name="SelectArgument",
    literals={
            EnumerationLiteral(name="MAXLOADED"),
			EnumerationLiteral(name="MINLOADED"),
			EnumerationLiteral(name="MINALLOCATED"),
			EnumerationLiteral(name="ORDER"),
			EnumerationLiteral(name="RANDOM")
    }
)

ColumnId: Enumeration = Enumeration(
    name="ColumnId",
    literals={
            EnumerationLiteral(name="ALERT"),
			EnumerationLiteral(name="ALERTMESSAGE"),
			EnumerationLiteral(name="ALERTSUMMARY"),
			EnumerationLiteral(name="ALERTTREND"),
			EnumerationLiteral(name="CHART"),
			EnumerationLiteral(name="EFFICIENCY"),
			EnumerationLiteral(name="EFFORT"),
			EnumerationLiteral(name="EFFORTDONE"),
			EnumerationLiteral(name="EFFORTLEFT"),
			EnumerationLiteral(name="EMAIL"),
			EnumerationLiteral(name="END"),
			EnumerationLiteral(name="FLAGS"),
			EnumerationLiteral(name="FOLLOWERS"),
			EnumerationLiteral(name="FREETIME"),
			EnumerationLiteral(name="FREEWORK"),
			EnumerationLiteral(name="FTE"),
			EnumerationLiteral(name="HEADCOUNT"),
			EnumerationLiteral(name="HIERARCHINDEX"),
			EnumerationLiteral(name="HOURLY"),
			EnumerationLiteral(name="ID"),
			EnumerationLiteral(name="INDEX"),
			EnumerationLiteral(name="JOURNAL"),
			EnumerationLiteral(name="LINE"),
			EnumerationLiteral(name="MAXEND"),
			EnumerationLiteral(name="MAXSTART"),
			EnumerationLiteral(name="MINEND"),
			EnumerationLiteral(name="COMPLETE"),
			EnumerationLiteral(name="COMPLETED"),
			EnumerationLiteral(name="CRITICALNESS"),
			EnumerationLiteral(name="COST"),
			EnumerationLiteral(name="DAILY"),
			EnumerationLiteral(name="DURATION"),
			EnumerationLiteral(name="DUTIES"),
			EnumerationLiteral(name="PRECURSOR"),
			EnumerationLiteral(name="PRIORITY"),
			EnumerationLiteral(name="QUARTERLY"),
			EnumerationLiteral(name="RATE"),
			EnumerationLiteral(name="RESOURCES"),
			EnumerationLiteral(name="RESPONSIBLE"),
			EnumerationLiteral(name="REVENUE"),
			EnumerationLiteral(name="SCENARIO"),
			EnumerationLiteral(name="SEQNO"),
			EnumerationLiteral(name="START"),
			EnumerationLiteral(name="STATUS"),
			EnumerationLiteral(name="TARGETS"),
			EnumerationLiteral(name="WBS"),
			EnumerationLiteral(name="WEEKLY"),
			EnumerationLiteral(name="YEARLY"),
			EnumerationLiteral(name="MINSTART"),
			EnumerationLiteral(name="MONTHLY"),
			EnumerationLiteral(name="NO"),
			EnumerationLiteral(name="NAME"),
			EnumerationLiteral(name="NOTE"),
			EnumerationLiteral(name="PATHCRITICALNESS")
    }
)

ScaleResolution: Enumeration = Enumeration(
    name="ScaleResolution",
    literals={
            EnumerationLiteral(name="WEEK"),
			EnumerationLiteral(name="MONTH"),
			EnumerationLiteral(name="QUARTER"),
			EnumerationLiteral(name="YEAR"),
			EnumerationLiteral(name="HOUR"),
			EnumerationLiteral(name="DAY")
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

Weekday: Enumeration = Enumeration(
    name="Weekday",
    literals={
            EnumerationLiteral(name="MON"),
			EnumerationLiteral(name="TUE"),
			EnumerationLiteral(name="WED"),
			EnumerationLiteral(name="THR"),
			EnumerationLiteral(name="FRI"),
			EnumerationLiteral(name="SAT"),
			EnumerationLiteral(name="SUN")
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

SchedulingPolicy: Enumeration = Enumeration(
    name="SchedulingPolicy",
    literals={
            EnumerationLiteral(name="ALAP"),
			EnumerationLiteral(name="ASAP")
    }
)

# Classes
project_Project = Class(name="project::Project")
project_Property = Class(name="project::Property")
project_Account = Class(name="project::Account")
Property_ = Class(name="Property")
AccountAttribute = Class(name="AccountAttribute")
project_AccountAttribute = Class(name="project::AccountAttribute")
project_AccountPrefix = Class(name="project::AccountPrefix")
IncludePropertiesAttribute = Class(name="IncludePropertiesAttribute")
project_AccountReport = Class(name="project::AccountReport")
ReportAttribute = Class(name="ReportAttribute")
project_Global = Class(name="project::Global")
project_Interval2 = Class(name="project::Interval2")
project_ProjectAttribute = Class(name="project::ProjectAttribute")
project_Task = Class(name="project::Task")
TaskAttribute = Class(name="TaskAttribute")
project_TaskAttribute = Class(name="project::TaskAttribute")
project_Report = Class(name="project::Report")
AccountReport = Class(name="AccountReport")
ResourceReport = Class(name="ResourceReport")
TaskReport = Class(name="TaskReport")
project_AccountRoot = Class(name="project::AccountRoot")
project_ReportAttribute = Class(name="project::ReportAttribute")
project_IcalReport = Class(name="project::IcalReport")
project_IcalReportAttribute = Class(name="project::IcalReportAttribute")
project_Export = Class(name="project::Export")
project_ExportAttribute = Class(name="project::ExportAttribute")
project_Resource = Class(name="project::Resource")
ResourceAttribute = Class(name="ResourceAttribute")
TextReport = Class(name="TextReport")
project_Allocate = Class(name="project::Allocate")
project_AllocateResource = Class(name="project::AllocateResource")
project_AllocateResourceAttribute = Class(name="project::AllocateResourceAttribute")
project_Navigator = Class(name="project::Navigator")
project_NavigatorAttribute = Class(name="project::NavigatorAttribute")
project_NewTask = Class(name="project::NewTask")
TimesheetAttribute = Class(name="TimesheetAttribute")
project_ResourceAttribute = Class(name="project::ResourceAttribute")
project_NikuReport = Class(name="project::NikuReport")
project_NikuReportAttribute = Class(name="project::NikuReportAttribute")
project_Alert = Class(name="project::Alert")
project_Alternative = Class(name="project::Alternative")
AllocateResourceAttribute = Class(name="AllocateResourceAttribute")
project_Author = Class(name="project::Author")
StatusStatusSheetAttribute = Class(name="StatusStatusSheetAttribute")
project_Balance = Class(name="project::Balance")
project_NewTaskAttribute = Class(name="project::NewTaskAttribute")
project_Booking = Class(name="project::Booking")
project_Interval4 = Class(name="project::Interval4")
project_BookingTask = Class(name="project::BookingTask")
project_BookingResource = Class(name="project::BookingResource")
project_CellText = Class(name="project::CellText")
project_Center = Class(name="project::Center")
project_Charge = Class(name="project::Charge")
project_ChargeSet = Class(name="project::ChargeSet")
project_AccountShare = Class(name="project::AccountShare")
project_Columns = Class(name="project::Columns")
project_Column = Class(name="project::Column")
project_Complete = Class(name="project::Complete")
project_Copyright = Class(name="project::Copyright")
project_Credit = Class(name="project::Credit")
project_Currency = Class(name="project::Currency")
ProjectAttribute = Class(name="ProjectAttribute")
project_CurrencyFormat = Class(name="project::CurrencyFormat")
project_DailyMax = Class(name="project::DailyMax")
LimitsAttribute = Class(name="LimitsAttribute")
project_Caption = Class(name="project::Caption")
project_CellColor = Class(name="project::CellColor")
ColumnAttribute = Class(name="ColumnAttribute")
project_LogicalExpression = Class(name="project::LogicalExpression")
project_RGB = Class(name="project::RGB")
StatusTimesheetAttribute = Class(name="StatusTimesheetAttribute")
project_Duration = Class(name="project::Duration")
project_DurationQuantity = Class(name="project::DurationQuantity")
project_Efficiency = Class(name="project::Efficiency")
project_Effort = Class(name="project::Effort")
project_Email = Class(name="project::Email")
project_End = Class(name="project::End")
IcalReportAttribute = Class(name="IcalReportAttribute")
NewTaskAttribute = Class(name="NewTaskAttribute")
NikuReportAttribute = Class(name="NikuReportAttribute")
StatusSheetReportAttribute = Class(name="StatusSheetReportAttribute")
TaskTimesheetAttribute = Class(name="TaskTimesheetAttribute")
TimesheetReportAttribute = Class(name="TimesheetReportAttribute")
project_EndCredit = Class(name="project::EndCredit")
project_Epilog = Class(name="project::Epilog")
project_Extend = Class(name="project::Extend")
project_ExtendResource = Class(name="project::ExtendResource")
project_DailyMin = Class(name="project::DailyMin")
project_DailyWorkingHours = Class(name="project::DailyWorkingHours")
project_Definitions = Class(name="project::Definitions")
ExportAttribute = Class(name="ExportAttribute")
project_Depends = Class(name="project::Depends")
project_Details = Class(name="project::Details")
project_ExtendedTaskAttribute = Class(name="project::ExtendedTaskAttribute")
project_Fail = Class(name="project::Fail")
project_ExtendedResourceAttribute = Class(name="project::ExtendedResourceAttribute")
project_ExtendTask = Class(name="project::ExtendTask")
project_Footer = Class(name="project::Footer")
project_Formats = Class(name="project::Formats")
project_Function = Class(name="project::Function")
project_Scenario = Class(name="project::Scenario")
project_GapDuration = Class(name="project::GapDuration")
project_GapLength = Class(name="project::GapLength")
project_HAlign = Class(name="project::HAlign")
project_Header = Class(name="project::Header")
project_Headline = Class(name="project::Headline")
project_HideAccount = Class(name="project::HideAccount")
project_HideJournalEntry = Class(name="project::HideJournalEntry")
project_HideReport = Class(name="project::HideReport")
NavigatorAttribute = Class(name="NavigatorAttribute")
project_Flags = Class(name="project::Flags")
project_FontColor = Class(name="project::FontColor")
project_Include = Class(name="project::Include")
project_IncludeProperties = Class(name="project::IncludeProperties")
project_IncludePropertiesAttribute = Class(name="project::IncludePropertiesAttribute")
project_Interval1 = Class(name="project::Interval1")
project_Interval3 = Class(name="project::Interval3")
project_HideResource = Class(name="project::HideResource")
project_HideTask = Class(name="project::HideTask")
project_JournalAttributes = Class(name="project::JournalAttributes")
project_JournalEntry = Class(name="project::JournalEntry")
project_Summary = Class(name="project::Summary")
project_JournalMode = Class(name="project::JournalMode")
project_Left = Class(name="project::Left")
project_Length = Class(name="project::Length")
project_Limits = Class(name="project::Limits")
project_LimitsAttribute = Class(name="project::LimitsAttribute")
project_Macro = Class(name="project::Macro")
project_Managers = Class(name="project::Managers")
project_Mandatory = Class(name="project::Mandatory")
project_MaxEnd = Class(name="project::MaxEnd")
project_Maximum = Class(name="project::Maximum")
project_MaxStart = Class(name="project::MaxStart")
project_ListItem = Class(name="project::ListItem")
project_ListType = Class(name="project::ListType")
project_LoadUnit = Class(name="project::LoadUnit")
project_MinStart = Class(name="project::MinStart")
project_MonthlyMax = Class(name="project::MonthlyMax")
project_MonthlyMin = Class(name="project::MonthlyMin")
project_Note = Class(name="project::Note")
project_Now = Class(name="project::Now")
project_NumberFormat = Class(name="project::NumberFormat")
project_Period = Class(name="project::Period")
project_Milestone = Class(name="project::Milestone")
project_Minimum = Class(name="project::Minimum")
project_MinEnd = Class(name="project::MinEnd")
project_Precedes = Class(name="project::Precedes")
project_Priority = Class(name="project::Priority")
project_ProjectId = Class(name="project::ProjectId")
project_ProjectIds = Class(name="project::ProjectIds")
project_Prolog = Class(name="project::Prolog")
project_PurgeReport = Class(name="project::PurgeReport")
project_Persistent = Class(name="project::Persistent")
project_PurgeResource = Class(name="project::PurgeResource")
project_PurgeTask = Class(name="project::PurgeTask")
project_ReportPrefix = Class(name="project::ReportPrefix")
project_ResourceAttributes = Class(name="project::ResourceAttributes")
project_ResourcePrefix = Class(name="project::ResourcePrefix")
project_ResourceReport = Class(name="project::ResourceReport")
project_Rate = Class(name="project::Rate")
project_Remaining = Class(name="project::Remaining")
project_Responsible = Class(name="project::Responsible")
project_Right = Class(name="project::Right")
project_RollupAccount = Class(name="project::RollupAccount")
project_RollupResource = Class(name="project::RollupResource")
project_ResourceRoot = Class(name="project::ResourceRoot")
project_Scale = Class(name="project::Scale")
project_ScenarioIcal = Class(name="project::ScenarioIcal")
project_Scenarios = Class(name="project::Scenarios")
project_Scheduled = Class(name="project::Scheduled")
project_RollupTask = Class(name="project::RollupTask")
project_Scheduling = Class(name="project::Scheduling")
project_Select = Class(name="project::Select")
project_SelfContained = Class(name="project::SelfContained")
project_Shift = Class(name="project::Shift")
project_Vacation = Class(name="project::Vacation")
project_Shifts = Class(name="project::Shifts")
ShiftsResource = Class(name="ShiftsResource")
ShiftsTask = Class(name="ShiftsTask")
project_ShiftsLimit = Class(name="project::ShiftsLimit")
project_ShiftsAllocate = Class(name="project::ShiftsAllocate")
project_WorkingHours = Class(name="project::WorkingHours")
project_ShiftTimesheet = Class(name="project::ShiftTimesheet")
SortAccounts = Class(name="SortAccounts")
SortJournalEntries = Class(name="SortJournalEntries")
SortResources = Class(name="SortResources")
SortTasks = Class(name="SortTasks")
project_Criterion = Class(name="project::Criterion")
project_SortAccounts = Class(name="project::SortAccounts")
project_SortJournalEntries = Class(name="project::SortJournalEntries")
project_SortResources = Class(name="project::SortResources")
project_SortTasks = Class(name="project::SortTasks")
project_Start = Class(name="project::Start")
project_ShiftsResource = Class(name="project::ShiftsResource")
project_ShiftsTask = Class(name="project::ShiftsTask")
project_ShortTimeFormat = Class(name="project::ShortTimeFormat")
project_Sort = Class(name="project::Sort")
project_StatusStatusSheetAttribute = Class(name="project::StatusStatusSheetAttribute")
project_StatusTimesheet = Class(name="project::StatusTimesheet")
project_StatusTimesheetAttribute = Class(name="project::StatusTimesheetAttribute")
project_StatusSheet = Class(name="project::StatusSheet")
project_StatusStatusSheet = Class(name="project::StatusStatusSheet")
TaskStatusSheetAttribute = Class(name="TaskStatusSheetAttribute")
project_StatusSheetAttribute = Class(name="project::StatusSheetAttribute")
project_StatusSheetReport = Class(name="project::StatusSheetReport")
project_StatusSheetReportAttribute = Class(name="project::StatusSheetReportAttribute")
project_SupplementReport = Class(name="project::SupplementReport")
project_SupplementAccount = Class(name="project::SupplementAccount")
project_SupplementTask = Class(name="project::SupplementTask")
project_SupplementResource = Class(name="project::SupplementResource")
project_TagFile = Class(name="project::TagFile")
project_TaskStatusSheet = Class(name="project::TaskStatusSheet")
StatusSheetAttribute = Class(name="StatusSheetAttribute")
project_TaskStatusSheetAttribute = Class(name="project::TaskStatusSheetAttribute")
project_TaskTimesheet = Class(name="project::TaskTimesheet")
project_TaskAttributes = Class(name="project::TaskAttributes")
project_TaskPrefix = Class(name="project::TaskPrefix")
project_TaskTimesheetAttribute = Class(name="project::TaskTimesheetAttribute")
project_TextReport = Class(name="project::TextReport")
project_TimeFormat = Class(name="project::TimeFormat")
project_Timeoff = Class(name="project::Timeoff")
project_Timesheet = Class(name="project::Timesheet")
project_TaskReport = Class(name="project::TaskReport")
project_TaskRoot = Class(name="project::TaskRoot")
project_TimesheetAttribute = Class(name="project::TimesheetAttribute")
project_TimesheetReport = Class(name="project::TimesheetReport")
project_TimesheetReportAttribute = Class(name="project::TimesheetReportAttribute")
project_Timezone = Class(name="project::Timezone")
project_TimingResolution = Class(name="project::TimingResolution")
project_Title = Class(name="project::Title")
project_ToolTip = Class(name="project::ToolTip")
project_TrackingScenario = Class(name="project::TrackingScenario")
project_TreeLevel = Class(name="project::TreeLevel")
project_Warn = Class(name="project::Warn")
project_WeekStarts = Class(name="project::WeekStarts")
project_WeeklyMax = Class(name="project::WeeklyMax")
project_Work = Class(name="project::Work")
project_Weekdays = Class(name="project::Weekdays")
project_WeeklyMin = Class(name="project::WeeklyMin")
project_Width = Class(name="project::Width")
project_YearlyWorkingDays = Class(name="project::YearlyWorkingDays")
project_WorkHours = Class(name="project::WorkHours")
project_ColumnAttribute = Class(name="project::ColumnAttribute")
GapDuration = Class(name="GapDuration")
GapLength = Class(name="GapLength")
project_Limit = Class(name="project::Limit")
DailyMax = Class(name="DailyMax")
DailyMin = Class(name="DailyMin")
Maximum = Class(name="Maximum")
Minimum = Class(name="Minimum")
MonthlyMax = Class(name="MonthlyMax")
MonthlyMin = Class(name="MonthlyMin")
WeeklyMax = Class(name="WeeklyMax")
WeeklyMin = Class(name="WeeklyMin")
project_LimitAttribute = Class(name="project::LimitAttribute")
project_RealFormat = Class(name="project::RealFormat")
CurrencyFormat = Class(name="CurrencyFormat")
NumberFormat = Class(name="NumberFormat")
project_TaskDependency = Class(name="project::TaskDependency")
Depends = Class(name="Depends")
Precedes = Class(name="Precedes")
project_RichText = Class(name="project::RichText")
Caption = Class(name="Caption")
Center = Class(name="Center")
Details = Class(name="Details")
Epilog = Class(name="Epilog")
Footer = Class(name="Footer")
Header = Class(name="Header")
Headline = Class(name="Headline")
Left = Class(name="Left")
ListItem = Class(name="ListItem")
Prolog = Class(name="Prolog")
Right = Class(name="Right")
Summary = Class(name="Summary")
project_Defintions = Class(name="project::Defintions")
Definitions = Class(name="Definitions")
project_XBinaryOperation = Class(name="project::XBinaryOperation")
LogicalExpression = Class(name="LogicalExpression")
project_JvmIdentifiableElement = Class(name="project::JvmIdentifiableElement")
project_LogicalFunctionExpression = Class(name="project::LogicalFunctionExpression")
project_LogicalAbsoluteIdExression = Class(name="project::LogicalAbsoluteIdExression")
project_LogicalBooleanLiteral = Class(name="project::LogicalBooleanLiteral")
project_LogicalStringLiteral = Class(name="project::LogicalStringLiteral")
project_LogicalDateLiteral = Class(name="project::LogicalDateLiteral")
project_LogicalNumeralLiteral = Class(name="project::LogicalNumeralLiteral")

# project_Project class attributes and methods
project_Project_id: Property = Property(name="id", type=StringType)
project_Project_name: Property = Property(name="name", type=StringType)
project_Project_version: Property = Property(name="version", type=StringType)
project_Project.attributes={project_Project_id, project_Project_version, project_Project_name}

# project_Property class attributes and methods

# project_Account class attributes and methods
project_Account_id: Property = Property(name="id", type=StringType)
project_Account_name: Property = Property(name="name", type=StringType)
project_Account.attributes={project_Account_id, project_Account_name}

# Property class attributes and methods

# AccountAttribute class attributes and methods

# project_AccountAttribute class attributes and methods

# project_AccountPrefix class attributes and methods

# IncludePropertiesAttribute class attributes and methods

# project_AccountReport class attributes and methods

# ReportAttribute class attributes and methods

# project_Global class attributes and methods

# project_Interval2 class attributes and methods
project_Interval2_start: Property = Property(name="start", type=StringType)
project_Interval2_end: Property = Property(name="end", type=StringType)
project_Interval2.attributes={project_Interval2_end, project_Interval2_start}

# project_ProjectAttribute class attributes and methods

# project_Task class attributes and methods
project_Task_id: Property = Property(name="id", type=StringType)
project_Task_name: Property = Property(name="name", type=StringType)
project_Task.attributes={project_Task_id, project_Task_name}

# TaskAttribute class attributes and methods

# project_TaskAttribute class attributes and methods

# project_Report class attributes and methods
project_Report_id: Property = Property(name="id", type=StringType)
project_Report_name: Property = Property(name="name", type=StringType)
project_Report.attributes={project_Report_name, project_Report_id}

# AccountReport class attributes and methods

# ResourceReport class attributes and methods

# TaskReport class attributes and methods

# project_AccountRoot class attributes and methods

# project_ReportAttribute class attributes and methods

# project_IcalReport class attributes and methods
project_IcalReport_filename: Property = Property(name="filename", type=StringType)
project_IcalReport.attributes={project_IcalReport_filename}

# project_IcalReportAttribute class attributes and methods

# project_Export class attributes and methods
project_Export_id: Property = Property(name="id", type=StringType)
project_Export_filename: Property = Property(name="filename", type=StringType)
project_Export.attributes={project_Export_filename, project_Export_id}

# project_ExportAttribute class attributes and methods

# project_Resource class attributes and methods
project_Resource_id: Property = Property(name="id", type=StringType)
project_Resource_name: Property = Property(name="name", type=StringType)
project_Resource.attributes={project_Resource_id, project_Resource_name}

# ResourceAttribute class attributes and methods

# TextReport class attributes and methods

# project_Allocate class attributes and methods

# project_AllocateResource class attributes and methods

# project_AllocateResourceAttribute class attributes and methods

# project_Navigator class attributes and methods
project_Navigator_id: Property = Property(name="id", type=StringType)
project_Navigator.attributes={project_Navigator_id}

# project_NavigatorAttribute class attributes and methods

# project_NewTask class attributes and methods
project_NewTask_id: Property = Property(name="id", type=StringType)
project_NewTask_text: Property = Property(name="text", type=StringType)
project_NewTask.attributes={project_NewTask_text, project_NewTask_id}

# TimesheetAttribute class attributes and methods

# project_ResourceAttribute class attributes and methods

# project_NikuReport class attributes and methods
project_NikuReport_filename: Property = Property(name="filename", type=StringType)
project_NikuReport.attributes={project_NikuReport_filename}

# project_NikuReportAttribute class attributes and methods

# project_Alert class attributes and methods
project_Alert_level: Property = Property(name="level", type=StringType)
project_Alert.attributes={project_Alert_level}

# project_Alternative class attributes and methods

# AllocateResourceAttribute class attributes and methods

# project_Author class attributes and methods

# StatusStatusSheetAttribute class attributes and methods

# project_Balance class attributes and methods

# project_NewTaskAttribute class attributes and methods

# project_Booking class attributes and methods
project_Booking_overtime: Property = Property(name="overtime", type=IntegerType)
project_Booking_sloppy: Property = Property(name="sloppy", type=IntegerType)
project_Booking.attributes={project_Booking_overtime, project_Booking_sloppy}

# project_Interval4 class attributes and methods
project_Interval4_start: Property = Property(name="start", type=StringType)
project_Interval4_end: Property = Property(name="end", type=StringType)
project_Interval4.attributes={project_Interval4_end, project_Interval4_start}

# project_BookingTask class attributes and methods

# project_BookingResource class attributes and methods

# project_CellText class attributes and methods
project_CellText_text: Property = Property(name="text", type=StringType)
project_CellText.attributes={project_CellText_text}

# project_Center class attributes and methods

# project_Charge class attributes and methods
project_Charge_amount: Property = Property(name="amount", type=FloatType)
project_Charge_applies: Property = Property(name="applies", type=StringType)
project_Charge.attributes={project_Charge_applies, project_Charge_amount}

# project_ChargeSet class attributes and methods

# project_AccountShare class attributes and methods
project_AccountShare_share: Property = Property(name="share", type=FloatType)
project_AccountShare.attributes={project_AccountShare_share}

# project_Columns class attributes and methods

# project_Column class attributes and methods
project_Column_id: Property = Property(name="id", type=StringType)
project_Column.attributes={project_Column_id}

# project_Complete class attributes and methods
project_Complete_complete: Property = Property(name="complete", type=FloatType)
project_Complete.attributes={project_Complete_complete}

# project_Copyright class attributes and methods
project_Copyright_text: Property = Property(name="text", type=StringType)
project_Copyright.attributes={project_Copyright_text}

# project_Credit class attributes and methods
project_Credit_date: Property = Property(name="date", type=StringType)
project_Credit_description: Property = Property(name="description", type=StringType)
project_Credit_amount: Property = Property(name="amount", type=FloatType)
project_Credit.attributes={project_Credit_amount, project_Credit_date, project_Credit_description}

# project_Currency class attributes and methods
project_Currency_currency: Property = Property(name="currency", type=StringType)
project_Currency.attributes={project_Currency_currency}

# ProjectAttribute class attributes and methods

# project_CurrencyFormat class attributes and methods

# project_DailyMax class attributes and methods

# LimitsAttribute class attributes and methods

# project_Caption class attributes and methods

# project_CellColor class attributes and methods

# ColumnAttribute class attributes and methods

# project_LogicalExpression class attributes and methods

# project_RGB class attributes and methods
project_RGB_value: Property = Property(name="value", type=StringType)
project_RGB.attributes={project_RGB_value}

# StatusTimesheetAttribute class attributes and methods

# project_Duration class attributes and methods

# project_DurationQuantity class attributes and methods
project_DurationQuantity_value: Property = Property(name="value", type=FloatType)
project_DurationQuantity_unit: Property = Property(name="unit", type=StringType)
project_DurationQuantity.attributes={project_DurationQuantity_value, project_DurationQuantity_unit}

# project_Efficiency class attributes and methods
project_Efficiency_efficiency: Property = Property(name="efficiency", type=FloatType)
project_Efficiency.attributes={project_Efficiency_efficiency}

# project_Effort class attributes and methods

# project_Email class attributes and methods
project_Email_address: Property = Property(name="address", type=StringType)
project_Email.attributes={project_Email_address}

# project_End class attributes and methods
project_End_end: Property = Property(name="end", type=StringType)
project_End.attributes={project_End_end}

# IcalReportAttribute class attributes and methods

# NewTaskAttribute class attributes and methods

# NikuReportAttribute class attributes and methods

# StatusSheetReportAttribute class attributes and methods

# TaskTimesheetAttribute class attributes and methods

# TimesheetReportAttribute class attributes and methods

# project_EndCredit class attributes and methods
project_EndCredit_credit: Property = Property(name="credit", type=FloatType)
project_EndCredit.attributes={project_EndCredit_credit}

# project_Epilog class attributes and methods

# project_Extend class attributes and methods
project_Extend_id: Property = Property(name="id", type=StringType)
project_Extend_name: Property = Property(name="name", type=StringType)
project_Extend_inherit: Property = Property(name="inherit", type=BooleanType)
project_Extend_scenariospecific: Property = Property(name="scenariospecific", type=BooleanType)
project_Extend.attributes={project_Extend_inherit, project_Extend_id, project_Extend_scenariospecific, project_Extend_name}

# project_ExtendResource class attributes and methods

# project_DailyMin class attributes and methods

# project_DailyWorkingHours class attributes and methods
project_DailyWorkingHours_dailyWorkingHours: Property = Property(name="dailyWorkingHours", type=FloatType)
project_DailyWorkingHours.attributes={project_DailyWorkingHours_dailyWorkingHours}

# project_Definitions class attributes and methods
project_Definitions_all: Property = Property(name="all", type=BooleanType)
project_Definitions_none: Property = Property(name="none", type=BooleanType)
project_Definitions.attributes={project_Definitions_none, project_Definitions_all}

# ExportAttribute class attributes and methods

# project_Depends class attributes and methods

# project_Details class attributes and methods

# project_ExtendedTaskAttribute class attributes and methods
project_ExtendedTaskAttribute_value: Property = Property(name="value", type=StringType)
project_ExtendedTaskAttribute.attributes={project_ExtendedTaskAttribute_value}

# project_Fail class attributes and methods

# project_ExtendedResourceAttribute class attributes and methods
project_ExtendedResourceAttribute_value: Property = Property(name="value", type=StringType)
project_ExtendedResourceAttribute.attributes={project_ExtendedResourceAttribute_value}

# project_ExtendTask class attributes and methods

# project_Footer class attributes and methods

# project_Formats class attributes and methods
project_Formats_formats: Property = Property(name="formats", type=StringType)
project_Formats.attributes={project_Formats_formats}

# project_Function class attributes and methods
project_Function_level: Property = Property(name="level", type=IntegerType)
project_Function_date: Property = Property(name="date", type=StringType)
project_Function_parentId: Property = Property(name="parentId", type=StringType)
project_Function_distance: Property = Property(name="distance", type=IntegerType)
project_Function.attributes={project_Function_distance, project_Function_parentId, project_Function_date, project_Function_level}

# project_Scenario class attributes and methods
project_Scenario_id: Property = Property(name="id", type=StringType)
project_Scenario_name: Property = Property(name="name", type=StringType)
project_Scenario_active: Property = Property(name="active", type=StringType)
project_Scenario.attributes={project_Scenario_name, project_Scenario_id, project_Scenario_active}

# project_GapDuration class attributes and methods

# project_GapLength class attributes and methods

# project_HAlign class attributes and methods
project_HAlign_justification: Property = Property(name="justification", type=StringType)
project_HAlign.attributes={project_HAlign_justification}

# project_Header class attributes and methods

# project_Headline class attributes and methods

# project_HideAccount class attributes and methods
project_HideAccount_expression: Property = Property(name="expression", type=StringType)
project_HideAccount.attributes={project_HideAccount_expression}

# project_HideJournalEntry class attributes and methods
project_HideJournalEntry_expression: Property = Property(name="expression", type=StringType)
project_HideJournalEntry.attributes={project_HideJournalEntry_expression}

# project_HideReport class attributes and methods

# NavigatorAttribute class attributes and methods

# project_Flags class attributes and methods
project_Flags_flags: Property = Property(name="flags", type=StringType)
project_Flags.attributes={project_Flags_flags}

# project_FontColor class attributes and methods
project_FontColor_color: Property = Property(name="color", type=StringType)
project_FontColor.attributes={project_FontColor_color}

# project_Include class attributes and methods
project_Include_importURI: Property = Property(name="importURI", type=StringType)
project_Include.attributes={project_Include_importURI}

# project_IncludeProperties class attributes and methods
project_IncludeProperties_importURI: Property = Property(name="importURI", type=StringType)
project_IncludeProperties.attributes={project_IncludeProperties_importURI}

# project_IncludePropertiesAttribute class attributes and methods

# project_Interval1 class attributes and methods
project_Interval1_start: Property = Property(name="start", type=StringType)
project_Interval1_end: Property = Property(name="end", type=StringType)
project_Interval1.attributes={project_Interval1_start, project_Interval1_end}

# project_Interval3 class attributes and methods
project_Interval3_start: Property = Property(name="start", type=StringType)
project_Interval3_end: Property = Property(name="end", type=StringType)
project_Interval3.attributes={project_Interval3_start, project_Interval3_end}

# project_HideResource class attributes and methods

# project_HideTask class attributes and methods

# project_JournalAttributes class attributes and methods
project_JournalAttributes_property: Property = Property(name="property", type=BooleanType)
project_JournalAttributes_details: Property = Property(name="details", type=BooleanType)
project_JournalAttributes_author: Property = Property(name="author", type=BooleanType)
project_JournalAttributes_headline: Property = Property(name="headline", type=BooleanType)
project_JournalAttributes_date: Property = Property(name="date", type=BooleanType)
project_JournalAttributes_timesheet: Property = Property(name="timesheet", type=BooleanType)
project_JournalAttributes_propertyid: Property = Property(name="propertyid", type=BooleanType)
project_JournalAttributes_summary: Property = Property(name="summary", type=BooleanType)
project_JournalAttributes_all: Property = Property(name="all", type=BooleanType)
project_JournalAttributes_none: Property = Property(name="none", type=BooleanType)
project_JournalAttributes_flags: Property = Property(name="flags", type=BooleanType)
project_JournalAttributes.attributes={project_JournalAttributes_property, project_JournalAttributes_flags, project_JournalAttributes_author, project_JournalAttributes_date, project_JournalAttributes_propertyid, project_JournalAttributes_details, project_JournalAttributes_none, project_JournalAttributes_timesheet, project_JournalAttributes_all, project_JournalAttributes_headline, project_JournalAttributes_summary}

# project_JournalEntry class attributes and methods
project_JournalEntry_date: Property = Property(name="date", type=StringType)
project_JournalEntry_headline: Property = Property(name="headline", type=StringType)
project_JournalEntry.attributes={project_JournalEntry_headline, project_JournalEntry_date}

# project_Summary class attributes and methods

# project_JournalMode class attributes and methods
project_JournalMode_mode: Property = Property(name="mode", type=StringType)
project_JournalMode.attributes={project_JournalMode_mode}

# project_Left class attributes and methods

# project_Length class attributes and methods

# project_Limits class attributes and methods

# project_LimitsAttribute class attributes and methods

# project_Macro class attributes and methods
project_Macro_value: Property = Property(name="value", type=StringType)
project_Macro.attributes={project_Macro_value}

# project_Managers class attributes and methods

# project_Mandatory class attributes and methods
project_Mandatory_mandatory: Property = Property(name="mandatory", type=BooleanType)
project_Mandatory.attributes={project_Mandatory_mandatory}

# project_MaxEnd class attributes and methods
project_MaxEnd_maxEnd: Property = Property(name="maxEnd", type=StringType)
project_MaxEnd.attributes={project_MaxEnd_maxEnd}

# project_Maximum class attributes and methods

# project_MaxStart class attributes and methods
project_MaxStart_maxStart: Property = Property(name="maxStart", type=StringType)
project_MaxStart.attributes={project_MaxStart_maxStart}

# project_ListItem class attributes and methods

# project_ListType class attributes and methods
project_ListType_type: Property = Property(name="type", type=StringType)
project_ListType.attributes={project_ListType_type}

# project_LoadUnit class attributes and methods
project_LoadUnit_unit: Property = Property(name="unit", type=StringType)
project_LoadUnit.attributes={project_LoadUnit_unit}

# project_MinStart class attributes and methods
project_MinStart_minStart: Property = Property(name="minStart", type=StringType)
project_MinStart.attributes={project_MinStart_minStart}

# project_MonthlyMax class attributes and methods

# project_MonthlyMin class attributes and methods

# project_Note class attributes and methods
project_Note_note: Property = Property(name="note", type=StringType)
project_Note.attributes={project_Note_note}

# project_Now class attributes and methods
project_Now_now: Property = Property(name="now", type=StringType)
project_Now.attributes={project_Now_now}

# project_NumberFormat class attributes and methods

# project_Period class attributes and methods

# project_Milestone class attributes and methods
project_Milestone_milestone: Property = Property(name="milestone", type=BooleanType)
project_Milestone.attributes={project_Milestone_milestone}

# project_Minimum class attributes and methods

# project_MinEnd class attributes and methods
project_MinEnd_minEnd: Property = Property(name="minEnd", type=StringType)
project_MinEnd.attributes={project_MinEnd_minEnd}

# project_Precedes class attributes and methods

# project_Priority class attributes and methods
project_Priority_priority: Property = Property(name="priority", type=IntegerType)
project_Priority.attributes={project_Priority_priority}

# project_ProjectId class attributes and methods
project_ProjectId_projectId: Property = Property(name="projectId", type=StringType)
project_ProjectId.attributes={project_ProjectId_projectId}

# project_ProjectIds class attributes and methods
project_ProjectIds_ids: Property = Property(name="ids", type=StringType)
project_ProjectIds.attributes={project_ProjectIds_ids}

# project_Prolog class attributes and methods

# project_PurgeReport class attributes and methods
project_PurgeReport_listAttribute: Property = Property(name="listAttribute", type=StringType)
project_PurgeReport.attributes={project_PurgeReport_listAttribute}

# project_Persistent class attributes and methods
project_Persistent_persistent: Property = Property(name="persistent", type=BooleanType)
project_Persistent.attributes={project_Persistent_persistent}

# project_PurgeResource class attributes and methods
project_PurgeResource_listAttribute: Property = Property(name="listAttribute", type=StringType)
project_PurgeResource.attributes={project_PurgeResource_listAttribute}

# project_PurgeTask class attributes and methods
project_PurgeTask_listAttribute: Property = Property(name="listAttribute", type=StringType)
project_PurgeTask.attributes={project_PurgeTask_listAttribute}

# project_ReportPrefix class attributes and methods

# project_ResourceAttributes class attributes and methods
project_ResourceAttributes_all: Property = Property(name="all", type=BooleanType)
project_ResourceAttributes_none: Property = Property(name="none", type=BooleanType)
project_ResourceAttributes_vacation: Property = Property(name="vacation", type=BooleanType)
project_ResourceAttributes_booking: Property = Property(name="booking", type=BooleanType)
project_ResourceAttributes_workingHours: Property = Property(name="workingHours", type=BooleanType)
project_ResourceAttributes.attributes={project_ResourceAttributes_booking, project_ResourceAttributes_all, project_ResourceAttributes_vacation, project_ResourceAttributes_none, project_ResourceAttributes_workingHours}

# project_ResourcePrefix class attributes and methods

# project_ResourceReport class attributes and methods

# project_Rate class attributes and methods
project_Rate_rate: Property = Property(name="rate", type=FloatType)
project_Rate.attributes={project_Rate_rate}

# project_Remaining class attributes and methods

# project_Responsible class attributes and methods

# project_Right class attributes and methods

# project_RollupAccount class attributes and methods

# project_RollupResource class attributes and methods

# project_ResourceRoot class attributes and methods

# project_Scale class attributes and methods
project_Scale_scale: Property = Property(name="scale", type=StringType)
project_Scale.attributes={project_Scale_scale}

# project_ScenarioIcal class attributes and methods

# project_Scenarios class attributes and methods

# project_Scheduled class attributes and methods
project_Scheduled_scheduled: Property = Property(name="scheduled", type=BooleanType)
project_Scheduled.attributes={project_Scheduled_scheduled}

# project_RollupTask class attributes and methods

# project_Scheduling class attributes and methods
project_Scheduling_scheduling: Property = Property(name="scheduling", type=StringType)
project_Scheduling.attributes={project_Scheduling_scheduling}

# project_Select class attributes and methods
project_Select_argument: Property = Property(name="argument", type=StringType)
project_Select.attributes={project_Select_argument}

# project_SelfContained class attributes and methods
project_SelfContained_selfcontained: Property = Property(name="selfcontained", type=StringType)
project_SelfContained.attributes={project_SelfContained_selfcontained}

# project_Shift class attributes and methods
project_Shift_id: Property = Property(name="id", type=StringType)
project_Shift_name: Property = Property(name="name", type=StringType)
project_Shift_replace: Property = Property(name="replace", type=StringType)
project_Shift_timezone: Property = Property(name="timezone", type=StringType)
project_Shift.attributes={project_Shift_replace, project_Shift_timezone, project_Shift_id, project_Shift_name}

# project_Vacation class attributes and methods
project_Vacation_name: Property = Property(name="name", type=StringType)
project_Vacation.attributes={project_Vacation_name}

# project_Shifts class attributes and methods

# ShiftsResource class attributes and methods

# ShiftsTask class attributes and methods

# project_ShiftsLimit class attributes and methods

# project_ShiftsAllocate class attributes and methods

# project_WorkingHours class attributes and methods
project_WorkingHours_off: Property = Property(name="off", type=BooleanType)
project_WorkingHours.attributes={project_WorkingHours_off}

# project_ShiftTimesheet class attributes and methods

# SortAccounts class attributes and methods

# SortJournalEntries class attributes and methods

# SortResources class attributes and methods

# SortTasks class attributes and methods

# project_Criterion class attributes and methods
project_Criterion_columnId: Property = Property(name="columnId", type=StringType)
project_Criterion_direction: Property = Property(name="direction", type=StringType)
project_Criterion.attributes={project_Criterion_direction, project_Criterion_columnId}

# project_SortAccounts class attributes and methods

# project_SortJournalEntries class attributes and methods

# project_SortResources class attributes and methods

# project_SortTasks class attributes and methods

# project_Start class attributes and methods
project_Start_start: Property = Property(name="start", type=StringType)
project_Start.attributes={project_Start_start}

# project_ShiftsResource class attributes and methods

# project_ShiftsTask class attributes and methods

# project_ShortTimeFormat class attributes and methods
project_ShortTimeFormat_shortTimeFormat: Property = Property(name="shortTimeFormat", type=StringType)
project_ShortTimeFormat.attributes={project_ShortTimeFormat_shortTimeFormat}

# project_Sort class attributes and methods
project_Sort_tree: Property = Property(name="tree", type=BooleanType)
project_Sort.attributes={project_Sort_tree}

# project_StatusStatusSheetAttribute class attributes and methods

# project_StatusTimesheet class attributes and methods
project_StatusTimesheet_level: Property = Property(name="level", type=StringType)
project_StatusTimesheet_text: Property = Property(name="text", type=StringType)
project_StatusTimesheet.attributes={project_StatusTimesheet_level, project_StatusTimesheet_text}

# project_StatusTimesheetAttribute class attributes and methods

# project_StatusSheet class attributes and methods

# project_StatusStatusSheet class attributes and methods
project_StatusStatusSheet_level: Property = Property(name="level", type=StringType)
project_StatusStatusSheet_text: Property = Property(name="text", type=StringType)
project_StatusStatusSheet.attributes={project_StatusStatusSheet_level, project_StatusStatusSheet_text}

# TaskStatusSheetAttribute class attributes and methods

# project_StatusSheetAttribute class attributes and methods

# project_StatusSheetReport class attributes and methods
project_StatusSheetReport_filename: Property = Property(name="filename", type=StringType)
project_StatusSheetReport.attributes={project_StatusSheetReport_filename}

# project_StatusSheetReportAttribute class attributes and methods

# project_SupplementReport class attributes and methods

# project_SupplementAccount class attributes and methods

# project_SupplementTask class attributes and methods

# project_SupplementResource class attributes and methods

# project_TagFile class attributes and methods
project_TagFile_id: Property = Property(name="id", type=StringType)
project_TagFile_filename: Property = Property(name="filename", type=StringType)
project_TagFile.attributes={project_TagFile_filename, project_TagFile_id}

# project_TaskStatusSheet class attributes and methods

# StatusSheetAttribute class attributes and methods

# project_TaskStatusSheetAttribute class attributes and methods

# project_TaskTimesheet class attributes and methods

# project_TaskAttributes class attributes and methods
project_TaskAttributes_all: Property = Property(name="all", type=BooleanType)
project_TaskAttributes_none: Property = Property(name="none", type=BooleanType)
project_TaskAttributes_responsible: Property = Property(name="responsible", type=BooleanType)
project_TaskAttributes_flags: Property = Property(name="flags", type=BooleanType)
project_TaskAttributes_maxstart: Property = Property(name="maxstart", type=BooleanType)
project_TaskAttributes_maxend: Property = Property(name="maxend", type=BooleanType)
project_TaskAttributes_priority: Property = Property(name="priority", type=BooleanType)
project_TaskAttributes_booking: Property = Property(name="booking", type=BooleanType)
project_TaskAttributes_note: Property = Property(name="note", type=BooleanType)
project_TaskAttributes_minstart: Property = Property(name="minstart", type=BooleanType)
project_TaskAttributes_minend: Property = Property(name="minend", type=BooleanType)
project_TaskAttributes_complete: Property = Property(name="complete", type=BooleanType)
project_TaskAttributes_depends: Property = Property(name="depends", type=BooleanType)
project_TaskAttributes.attributes={project_TaskAttributes_depends, project_TaskAttributes_priority, project_TaskAttributes_note, project_TaskAttributes_minend, project_TaskAttributes_complete, project_TaskAttributes_maxstart, project_TaskAttributes_none, project_TaskAttributes_booking, project_TaskAttributes_minstart, project_TaskAttributes_responsible, project_TaskAttributes_flags, project_TaskAttributes_maxend, project_TaskAttributes_all}

# project_TaskPrefix class attributes and methods

# project_TaskTimesheetAttribute class attributes and methods

# project_TextReport class attributes and methods

# project_TimeFormat class attributes and methods
project_TimeFormat_timeformat: Property = Property(name="timeformat", type=StringType)
project_TimeFormat.attributes={project_TimeFormat_timeformat}

# project_Timeoff class attributes and methods
project_Timeoff_id: Property = Property(name="id", type=StringType)
project_Timeoff_name: Property = Property(name="name", type=StringType)
project_Timeoff.attributes={project_Timeoff_id, project_Timeoff_name}

# project_Timesheet class attributes and methods

# project_TaskReport class attributes and methods

# project_TaskRoot class attributes and methods

# project_TimesheetAttribute class attributes and methods

# project_TimesheetReport class attributes and methods
project_TimesheetReport_filename: Property = Property(name="filename", type=StringType)
project_TimesheetReport.attributes={project_TimesheetReport_filename}

# project_TimesheetReportAttribute class attributes and methods

# project_Timezone class attributes and methods
project_Timezone_timezone: Property = Property(name="timezone", type=StringType)
project_Timezone.attributes={project_Timezone_timezone}

# project_TimingResolution class attributes and methods
project_TimingResolution_timingResolution: Property = Property(name="timingResolution", type=IntegerType)
project_TimingResolution.attributes={project_TimingResolution_timingResolution}

# project_Title class attributes and methods
project_Title_title: Property = Property(name="title", type=StringType)
project_Title.attributes={project_Title_title}

# project_ToolTip class attributes and methods
project_ToolTip_tip: Property = Property(name="tip", type=StringType)
project_ToolTip.attributes={project_ToolTip_tip}

# project_TrackingScenario class attributes and methods

# project_TreeLevel class attributes and methods
project_TreeLevel_level: Property = Property(name="level", type=StringType)
project_TreeLevel.attributes={project_TreeLevel_level}

# project_Warn class attributes and methods

# project_WeekStarts class attributes and methods
project_WeekStarts_sunday: Property = Property(name="sunday", type=BooleanType)
project_WeekStarts_monday: Property = Property(name="monday", type=BooleanType)
project_WeekStarts.attributes={project_WeekStarts_monday, project_WeekStarts_sunday}

# project_WeeklyMax class attributes and methods

# project_Work class attributes and methods
project_Work_value: Property = Property(name="value", type=FloatType)
project_Work_unit: Property = Property(name="unit", type=StringType)
project_Work.attributes={project_Work_unit, project_Work_value}

# project_Weekdays class attributes and methods
project_Weekdays_first: Property = Property(name="first", type=StringType)
project_Weekdays_last: Property = Property(name="last", type=StringType)
project_Weekdays.attributes={project_Weekdays_first, project_Weekdays_last}

# project_WeeklyMin class attributes and methods

# project_Width class attributes and methods
project_Width_width: Property = Property(name="width", type=FloatType)
project_Width.attributes={project_Width_width}

# project_YearlyWorkingDays class attributes and methods
project_YearlyWorkingDays_yearlyWorkingDays: Property = Property(name="yearlyWorkingDays", type=IntegerType)
project_YearlyWorkingDays.attributes={project_YearlyWorkingDays_yearlyWorkingDays}

# project_WorkHours class attributes and methods
project_WorkHours_start: Property = Property(name="start", type=StringType)
project_WorkHours_stop: Property = Property(name="stop", type=StringType)
project_WorkHours.attributes={project_WorkHours_start, project_WorkHours_stop}

# project_ColumnAttribute class attributes and methods

# GapDuration class attributes and methods

# GapLength class attributes and methods

# project_Limit class attributes and methods

# DailyMax class attributes and methods

# DailyMin class attributes and methods

# Maximum class attributes and methods

# Minimum class attributes and methods

# MonthlyMax class attributes and methods

# MonthlyMin class attributes and methods

# WeeklyMax class attributes and methods

# WeeklyMin class attributes and methods

# project_LimitAttribute class attributes and methods
project_LimitAttribute_end: Property = Property(name="end", type=StringType)
project_LimitAttribute_start: Property = Property(name="start", type=StringType)
project_LimitAttribute.attributes={project_LimitAttribute_start, project_LimitAttribute_end}

# project_RealFormat class attributes and methods
project_RealFormat_thousandsSeparator: Property = Property(name="thousandsSeparator", type=StringType)
project_RealFormat_fractionSeparator: Property = Property(name="fractionSeparator", type=StringType)
project_RealFormat_fractionDigits: Property = Property(name="fractionDigits", type=IntegerType)
project_RealFormat_negativePrefix: Property = Property(name="negativePrefix", type=StringType)
project_RealFormat_negativeSuffix: Property = Property(name="negativeSuffix", type=StringType)
project_RealFormat.attributes={project_RealFormat_fractionDigits, project_RealFormat_negativePrefix, project_RealFormat_negativeSuffix, project_RealFormat_thousandsSeparator, project_RealFormat_fractionSeparator}

# CurrencyFormat class attributes and methods

# NumberFormat class attributes and methods

# project_TaskDependency class attributes and methods
project_TaskDependency_policy: Property = Property(name="policy", type=StringType)
project_TaskDependency.attributes={project_TaskDependency_policy}

# Depends class attributes and methods

# Precedes class attributes and methods

# project_RichText class attributes and methods
project_RichText_text: Property = Property(name="text", type=StringType)
project_RichText.attributes={project_RichText_text}

# Caption class attributes and methods

# Center class attributes and methods

# Details class attributes and methods

# Epilog class attributes and methods

# Footer class attributes and methods

# Header class attributes and methods

# Headline class attributes and methods

# Left class attributes and methods

# ListItem class attributes and methods

# Prolog class attributes and methods

# Right class attributes and methods

# Summary class attributes and methods

# project_Defintions class attributes and methods
project_Defintions_flags: Property = Property(name="flags", type=BooleanType)
project_Defintions_resources: Property = Property(name="resources", type=BooleanType)
project_Defintions_tasks: Property = Property(name="tasks", type=BooleanType)
project_Defintions_project: Property = Property(name="project", type=BooleanType)
project_Defintions_projectids: Property = Property(name="projectids", type=BooleanType)
project_Defintions.attributes={project_Defintions_tasks, project_Defintions_project, project_Defintions_projectids, project_Defintions_flags, project_Defintions_resources}

# Definitions class attributes and methods

# project_XBinaryOperation class attributes and methods

# LogicalExpression class attributes and methods

# project_JvmIdentifiableElement class attributes and methods

# project_LogicalFunctionExpression class attributes and methods

# project_LogicalAbsoluteIdExression class attributes and methods
project_LogicalAbsoluteIdExression_value: Property = Property(name="value", type=StringType)
project_LogicalAbsoluteIdExression.attributes={project_LogicalAbsoluteIdExression_value}

# project_LogicalBooleanLiteral class attributes and methods
project_LogicalBooleanLiteral_isTrue: Property = Property(name="isTrue", type=BooleanType)
project_LogicalBooleanLiteral.attributes={project_LogicalBooleanLiteral_isTrue}

# project_LogicalStringLiteral class attributes and methods
project_LogicalStringLiteral_value: Property = Property(name="value", type=StringType)
project_LogicalStringLiteral.attributes={project_LogicalStringLiteral_value}

# project_LogicalDateLiteral class attributes and methods
project_LogicalDateLiteral_value: Property = Property(name="value", type=StringType)
project_LogicalDateLiteral.attributes={project_LogicalDateLiteral_value}

# project_LogicalNumeralLiteral class attributes and methods
project_LogicalNumeralLiteral_value: Property = Property(name="value", type=FloatType)
project_LogicalNumeralLiteral.attributes={project_LogicalNumeralLiteral_value}

# Relationships
project0: BinaryAssociation = BinaryAssociation(
    name="project0",
    ends={
        Property(name="project_Project", type=project_Global, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Global", type=project_Project, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties1: BinaryAssociation = BinaryAssociation(
    name="properties1",
    ends={
        Property(name="project_Property", type=project_Global, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Global2", type=project_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="project_AccountAttribute", type=project_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Account", type=project_AccountAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
account4: BinaryAssociation = BinaryAssociation(
    name="account4",
    ends={
        Property(name="project_Account5", type=project_AccountPrefix, multiplicity=Multiplicity(1, 1)),
        Property(name="project_AccountPrefix", type=project_Account, multiplicity=Multiplicity(0, 1))
    }
)
account6: BinaryAssociation = BinaryAssociation(
    name="account6",
    ends={
        Property(name="project_Account7", type=project_AccountRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="project_AccountRoot", type=project_Account, multiplicity=Multiplicity(0, 1))
    }
)
interval8: BinaryAssociation = BinaryAssociation(
    name="interval8",
    ends={
        Property(name="project_Interval2", type=project_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Project9", type=project_Interval2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes10: BinaryAssociation = BinaryAssociation(
    name="attributes10",
    ends={
        Property(name="project_ProjectAttribute", type=project_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Project11", type=project_ProjectAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes12: BinaryAssociation = BinaryAssociation(
    name="attributes12",
    ends={
        Property(name="project_TaskAttribute", type=project_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Task", type=project_TaskAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes13: BinaryAssociation = BinaryAssociation(
    name="attributes13",
    ends={
        Property(name="project_ReportAttribute", type=project_Report, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Report", type=project_ReportAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes14: BinaryAssociation = BinaryAssociation(
    name="attributes14",
    ends={
        Property(name="project_IcalReportAttribute", type=project_IcalReport, multiplicity=Multiplicity(1, 1)),
        Property(name="project_IcalReport", type=project_IcalReportAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes15: BinaryAssociation = BinaryAssociation(
    name="attributes15",
    ends={
        Property(name="project_ExportAttribute", type=project_Export, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Export", type=project_ExportAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes16: BinaryAssociation = BinaryAssociation(
    name="attributes16",
    ends={
        Property(name="project_ResourceAttribute", type=project_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Resource", type=project_ResourceAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources17: BinaryAssociation = BinaryAssociation(
    name="resources17",
    ends={
        Property(name="project_AllocateResource", type=project_Allocate, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Allocate", type=project_AllocateResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resource18: BinaryAssociation = BinaryAssociation(
    name="resource18",
    ends={
        Property(name="project_Resource20", type=project_AllocateResource, multiplicity=Multiplicity(1, 1)),
        Property(name="project_AllocateResource19", type=project_Resource, multiplicity=Multiplicity(0, 1))
    }
)
attributes21: BinaryAssociation = BinaryAssociation(
    name="attributes21",
    ends={
        Property(name="project_AllocateResourceAttribute", type=project_AllocateResource, multiplicity=Multiplicity(1, 1)),
        Property(name="project_AllocateResource22", type=project_AllocateResourceAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes23: BinaryAssociation = BinaryAssociation(
    name="attributes23",
    ends={
        Property(name="project_NavigatorAttribute", type=project_Navigator, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Navigator", type=project_NavigatorAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes25: BinaryAssociation = BinaryAssociation(
    name="attributes25",
    ends={
        Property(name="project_NikuReportAttribute", type=project_NikuReport, multiplicity=Multiplicity(1, 1)),
        Property(name="project_NikuReport", type=project_NikuReportAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources26: BinaryAssociation = BinaryAssociation(
    name="resources26",
    ends={
        Property(name="project_Resource27", type=project_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Alternative", type=project_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
resource28: BinaryAssociation = BinaryAssociation(
    name="resource28",
    ends={
        Property(name="project_Resource29", type=project_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Author", type=project_Resource, multiplicity=Multiplicity(0, 1))
    }
)
cost30: BinaryAssociation = BinaryAssociation(
    name="cost30",
    ends={
        Property(name="project_Account31", type=project_Balance, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Balance", type=project_Account, multiplicity=Multiplicity(0, 1))
    }
)
attributes24: BinaryAssociation = BinaryAssociation(
    name="attributes24",
    ends={
        Property(name="project_NewTaskAttribute", type=project_NewTask, multiplicity=Multiplicity(1, 1)),
        Property(name="project_NewTask", type=project_NewTaskAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
revenue32: BinaryAssociation = BinaryAssociation(
    name="revenue32",
    ends={
        Property(name="project_Account34", type=project_Balance, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Balance33", type=project_Account, multiplicity=Multiplicity(0, 1))
    }
)
interval35: BinaryAssociation = BinaryAssociation(
    name="interval35",
    ends={
        Property(name="project_Interval4", type=project_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Booking", type=project_Interval4, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resource36: BinaryAssociation = BinaryAssociation(
    name="resource36",
    ends={
        Property(name="project_Resource37", type=project_BookingTask, multiplicity=Multiplicity(1, 1)),
        Property(name="project_BookingTask", type=project_Resource, multiplicity=Multiplicity(0, 1))
    }
)
booking38: BinaryAssociation = BinaryAssociation(
    name="booking38",
    ends={
        Property(name="project_Booking40", type=project_BookingTask, multiplicity=Multiplicity(1, 1)),
        Property(name="project_BookingTask39", type=project_Booking, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
task41: BinaryAssociation = BinaryAssociation(
    name="task41",
    ends={
        Property(name="project_Task42", type=project_BookingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="project_BookingResource", type=project_Task, multiplicity=Multiplicity(0, 1))
    }
)
expresssion49: BinaryAssociation = BinaryAssociation(
    name="expresssion49",
    ends={
        Property(name="project_LogicalExpression50", type=project_CellText, multiplicity=Multiplicity(1, 1)),
        Property(name="project_CellText", type=project_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accountShares51: BinaryAssociation = BinaryAssociation(
    name="accountShares51",
    ends={
        Property(name="project_AccountShare", type=project_ChargeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="project_ChargeSet", type=project_AccountShare, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns52: BinaryAssociation = BinaryAssociation(
    name="columns52",
    ends={
        Property(name="project_Column", type=project_Columns, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Columns", type=project_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
booking43: BinaryAssociation = BinaryAssociation(
    name="booking43",
    ends={
        Property(name="project_Booking45", type=project_BookingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="project_BookingResource44", type=project_Booking, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression46: BinaryAssociation = BinaryAssociation(
    name="expression46",
    ends={
        Property(name="project_LogicalExpression", type=project_CellColor, multiplicity=Multiplicity(1, 1)),
        Property(name="project_CellColor", type=project_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color47: BinaryAssociation = BinaryAssociation(
    name="color47",
    ends={
        Property(name="project_RGB", type=project_CellColor, multiplicity=Multiplicity(1, 1)),
        Property(name="project_CellColor48", type=project_RGB, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration53: BinaryAssociation = BinaryAssociation(
    name="duration53",
    ends={
        Property(name="project_DurationQuantity", type=project_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Duration", type=project_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effort54: BinaryAssociation = BinaryAssociation(
    name="effort54",
    ends={
        Property(name="project_DurationQuantity55", type=project_Effort, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Effort", type=project_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends56: BinaryAssociation = BinaryAssociation(
    name="extends56",
    ends={
        Property(name="project_Extend", type=project_ExtendResource, multiplicity=Multiplicity(1, 1)),
        Property(name="project_ExtendResource", type=project_Extend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extend61: BinaryAssociation = BinaryAssociation(
    name="extend61",
    ends={
        Property(name="project_Extend62", type=project_ExtendedTaskAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="project_ExtendedTaskAttribute", type=project_Extend, multiplicity=Multiplicity(0, 1))
    }
)
extend57: BinaryAssociation = BinaryAssociation(
    name="extend57",
    ends={
        Property(name="project_Extend58", type=project_ExtendedResourceAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="project_ExtendedResourceAttribute", type=project_Extend, multiplicity=Multiplicity(0, 1))
    }
)
extends59: BinaryAssociation = BinaryAssociation(
    name="extends59",
    ends={
        Property(name="project_Extend60", type=project_ExtendTask, multiplicity=Multiplicity(1, 1)),
        Property(name="project_ExtendTask", type=project_Extend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenario65: BinaryAssociation = BinaryAssociation(
    name="scenario65",
    ends={
        Property(name="project_Scenario", type=project_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Function", type=project_Scenario, multiplicity=Multiplicity(0, 1))
    }
)
task66: BinaryAssociation = BinaryAssociation(
    name="task66",
    ends={
        Property(name="project_Task68", type=project_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Function67", type=project_Task, multiplicity=Multiplicity(0, 1))
    }
)
resource69: BinaryAssociation = BinaryAssociation(
    name="resource69",
    ends={
        Property(name="project_Resource71", type=project_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Function70", type=project_Resource, multiplicity=Multiplicity(0, 1))
    }
)
expression72: BinaryAssociation = BinaryAssociation(
    name="expression72",
    ends={
        Property(name="project_LogicalExpression73", type=project_HAlign, multiplicity=Multiplicity(1, 1)),
        Property(name="project_HAlign", type=project_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression63: BinaryAssociation = BinaryAssociation(
    name="expression63",
    ends={
        Property(name="project_LogicalExpression64", type=project_Fail, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Fail", type=project_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression78: BinaryAssociation = BinaryAssociation(
    name="expression78",
    ends={
        Property(name="project_LogicalExpression79", type=project_HideTask, multiplicity=Multiplicity(1, 1)),
        Property(name="project_HideTask", type=project_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes80: BinaryAssociation = BinaryAssociation(
    name="attributes80",
    ends={
        Property(name="project_IncludePropertiesAttribute", type=project_IncludeProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="project_IncludeProperties", type=project_IncludePropertiesAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
duration81: BinaryAssociation = BinaryAssociation(
    name="duration81",
    ends={
        Property(name="project_DurationQuantity82", type=project_Interval1, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Interval1", type=project_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration83: BinaryAssociation = BinaryAssociation(
    name="duration83",
    ends={
        Property(name="project_DurationQuantity85", type=project_Interval2, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Interval284", type=project_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression74: BinaryAssociation = BinaryAssociation(
    name="expression74",
    ends={
        Property(name="project_LogicalExpression75", type=project_HideReport, multiplicity=Multiplicity(1, 1)),
        Property(name="project_HideReport", type=project_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression76: BinaryAssociation = BinaryAssociation(
    name="expression76",
    ends={
        Property(name="project_LogicalExpression77", type=project_HideResource, multiplicity=Multiplicity(1, 1)),
        Property(name="project_HideResource", type=project_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration88: BinaryAssociation = BinaryAssociation(
    name="duration88",
    ends={
        Property(name="project_DurationQuantity90", type=project_Interval4, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Interval489", type=project_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration86: BinaryAssociation = BinaryAssociation(
    name="duration86",
    ends={
        Property(name="project_DurationQuantity87", type=project_Interval3, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Interval3", type=project_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
summary97: BinaryAssociation = BinaryAssociation(
    name="summary97",
    ends={
        Property(name="project_Summary", type=project_JournalEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="project_JournalEntry98", type=project_Summary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
length99: BinaryAssociation = BinaryAssociation(
    name="length99",
    ends={
        Property(name="project_DurationQuantity100", type=project_Length, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Length", type=project_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes101: BinaryAssociation = BinaryAssociation(
    name="attributes101",
    ends={
        Property(name="project_LimitsAttribute", type=project_Limits, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Limits", type=project_LimitsAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alert91: BinaryAssociation = BinaryAssociation(
    name="alert91",
    ends={
        Property(name="project_Alert", type=project_JournalEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="project_JournalEntry", type=project_Alert, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author92: BinaryAssociation = BinaryAssociation(
    name="author92",
    ends={
        Property(name="project_Author94", type=project_JournalEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="project_JournalEntry93", type=project_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
details95: BinaryAssociation = BinaryAssociation(
    name="details95",
    ends={
        Property(name="project_Details", type=project_JournalEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="project_JournalEntry96", type=project_Details, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resources102: BinaryAssociation = BinaryAssociation(
    name="resources102",
    ends={
        Property(name="project_Resource103", type=project_Managers, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Managers", type=project_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
period104: BinaryAssociation = BinaryAssociation(
    name="period104",
    ends={
        Property(name="project_Interval2105", type=project_Period, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Period", type=project_Interval2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
remaining106: BinaryAssociation = BinaryAssociation(
    name="remaining106",
    ends={
        Property(name="project_DurationQuantity107", type=project_Remaining, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Remaining", type=project_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
report108: BinaryAssociation = BinaryAssociation(
    name="report108",
    ends={
        Property(name="project_Report109", type=project_ReportPrefix, multiplicity=Multiplicity(1, 1)),
        Property(name="project_ReportPrefix", type=project_Report, multiplicity=Multiplicity(0, 1))
    }
)
resource110: BinaryAssociation = BinaryAssociation(
    name="resource110",
    ends={
        Property(name="project_Resource111", type=project_ResourcePrefix, multiplicity=Multiplicity(1, 1)),
        Property(name="project_ResourcePrefix", type=project_Resource, multiplicity=Multiplicity(0, 1))
    }
)
resource112: BinaryAssociation = BinaryAssociation(
    name="resource112",
    ends={
        Property(name="project_ResourceRoot", type=project_Resource, multiplicity=Multiplicity(0, 1)),
        Property(name="project_Resource113", type=project_ResourceRoot, multiplicity=Multiplicity(1, 1))
    }
)
resources114: BinaryAssociation = BinaryAssociation(
    name="resources114",
    ends={
        Property(name="project_Resource115", type=project_Responsible, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Responsible", type=project_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
expression116: BinaryAssociation = BinaryAssociation(
    name="expression116",
    ends={
        Property(name="project_LogicalExpression117", type=project_RollupAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="project_RollupAccount", type=project_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression118: BinaryAssociation = BinaryAssociation(
    name="expression118",
    ends={
        Property(name="project_LogicalExpression119", type=project_RollupResource, multiplicity=Multiplicity(1, 1)),
        Property(name="project_RollupResource", type=project_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scenario123: BinaryAssociation = BinaryAssociation(
    name="scenario123",
    ends={
        Property(name="project_Scenario124", type=project_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Scenario122", type=project_Scenario, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scenario125: BinaryAssociation = BinaryAssociation(
    name="scenario125",
    ends={
        Property(name="project_Scenario126", type=project_ScenarioIcal, multiplicity=Multiplicity(1, 1)),
        Property(name="project_ScenarioIcal", type=project_Scenario, multiplicity=Multiplicity(0, 1))
    }
)
scenarios127: BinaryAssociation = BinaryAssociation(
    name="scenarios127",
    ends={
        Property(name="project_Scenario128", type=project_Scenarios, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Scenarios", type=project_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
expression120: BinaryAssociation = BinaryAssociation(
    name="expression120",
    ends={
        Property(name="project_LogicalExpression121", type=project_RollupTask, multiplicity=Multiplicity(1, 1)),
        Property(name="project_RollupTask", type=project_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vacation129: BinaryAssociation = BinaryAssociation(
    name="vacation129",
    ends={
        Property(name="project_Vacation", type=project_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Shift", type=project_Vacation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift135: BinaryAssociation = BinaryAssociation(
    name="shift135",
    ends={
        Property(name="project_Shift136", type=project_ShiftTimesheet, multiplicity=Multiplicity(1, 1)),
        Property(name="project_ShiftTimesheet", type=project_Shift, multiplicity=Multiplicity(0, 1))
    }
)
limits137: BinaryAssociation = BinaryAssociation(
    name="limits137",
    ends={
        Property(name="project_ShiftsLimit", type=project_Shifts, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Shifts", type=project_ShiftsLimit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shift138: BinaryAssociation = BinaryAssociation(
    name="shift138",
    ends={
        Property(name="project_Shift140", type=project_ShiftsLimit, multiplicity=Multiplicity(1, 1)),
        Property(name="project_ShiftsLimit139", type=project_Shift, multiplicity=Multiplicity(0, 1))
    }
)
limit141: BinaryAssociation = BinaryAssociation(
    name="limit141",
    ends={
        Property(name="project_Interval2143", type=project_ShiftsLimit, multiplicity=Multiplicity(1, 1)),
        Property(name="project_ShiftsLimit142", type=project_Interval2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift144: BinaryAssociation = BinaryAssociation(
    name="shift144",
    ends={
        Property(name="project_Shift145", type=project_ShiftsAllocate, multiplicity=Multiplicity(1, 1)),
        Property(name="project_ShiftsAllocate", type=project_Shift, multiplicity=Multiplicity(0, 1))
    }
)
intervals146: BinaryAssociation = BinaryAssociation(
    name="intervals146",
    ends={
        Property(name="project_Interval3148", type=project_ShiftsAllocate, multiplicity=Multiplicity(1, 1)),
        Property(name="project_ShiftsAllocate147", type=project_Interval3, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shift131: BinaryAssociation = BinaryAssociation(
    name="shift131",
    ends={
        Property(name="project_Shift132", type=project_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Shift130", type=project_Shift, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workingHours133: BinaryAssociation = BinaryAssociation(
    name="workingHours133",
    ends={
        Property(name="project_WorkingHours", type=project_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Shift134", type=project_WorkingHours, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
criteria149: BinaryAssociation = BinaryAssociation(
    name="criteria149",
    ends={
        Property(name="project_Criterion", type=project_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Sort", type=project_Criterion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes150: BinaryAssociation = BinaryAssociation(
    name="attributes150",
    ends={
        Property(name="project_StatusStatusSheetAttribute", type=project_StatusStatusSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="project_StatusStatusSheet", type=project_StatusStatusSheetAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes151: BinaryAssociation = BinaryAssociation(
    name="attributes151",
    ends={
        Property(name="project_StatusTimesheetAttribute", type=project_StatusTimesheet, multiplicity=Multiplicity(1, 1)),
        Property(name="project_StatusTimesheet", type=project_StatusTimesheetAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resource152: BinaryAssociation = BinaryAssociation(
    name="resource152",
    ends={
        Property(name="project_Resource153", type=project_StatusSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="project_StatusSheet", type=project_Resource, multiplicity=Multiplicity(0, 1))
    }
)
attributes157: BinaryAssociation = BinaryAssociation(
    name="attributes157",
    ends={
        Property(name="project_StatusSheetAttribute", type=project_StatusSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="project_StatusSheet158", type=project_StatusSheetAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes159: BinaryAssociation = BinaryAssociation(
    name="attributes159",
    ends={
        Property(name="project_StatusSheetReportAttribute", type=project_StatusSheetReport, multiplicity=Multiplicity(1, 1)),
        Property(name="project_StatusSheetReport", type=project_StatusSheetReportAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interval154: BinaryAssociation = BinaryAssociation(
    name="interval154",
    ends={
        Property(name="project_Interval4156", type=project_StatusSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="project_StatusSheet155", type=project_Interval4, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
account160: BinaryAssociation = BinaryAssociation(
    name="account160",
    ends={
        Property(name="project_Account161", type=project_SupplementAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="project_SupplementAccount", type=project_Account, multiplicity=Multiplicity(0, 1))
    }
)
attributes162: BinaryAssociation = BinaryAssociation(
    name="attributes162",
    ends={
        Property(name="project_AccountAttribute164", type=project_SupplementAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="project_SupplementAccount163", type=project_AccountAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
report165: BinaryAssociation = BinaryAssociation(
    name="report165",
    ends={
        Property(name="project_Report166", type=project_SupplementReport, multiplicity=Multiplicity(1, 1)),
        Property(name="project_SupplementReport", type=project_Report, multiplicity=Multiplicity(0, 1))
    }
)
attributes167: BinaryAssociation = BinaryAssociation(
    name="attributes167",
    ends={
        Property(name="project_ReportAttribute169", type=project_SupplementReport, multiplicity=Multiplicity(1, 1)),
        Property(name="project_SupplementReport168", type=project_ReportAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resource170: BinaryAssociation = BinaryAssociation(
    name="resource170",
    ends={
        Property(name="project_Resource171", type=project_SupplementResource, multiplicity=Multiplicity(1, 1)),
        Property(name="project_SupplementResource", type=project_Resource, multiplicity=Multiplicity(0, 1))
    }
)
attributes172: BinaryAssociation = BinaryAssociation(
    name="attributes172",
    ends={
        Property(name="project_ResourceAttribute174", type=project_SupplementResource, multiplicity=Multiplicity(1, 1)),
        Property(name="project_SupplementResource173", type=project_ResourceAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task175: BinaryAssociation = BinaryAssociation(
    name="task175",
    ends={
        Property(name="project_Task176", type=project_SupplementTask, multiplicity=Multiplicity(1, 1)),
        Property(name="project_SupplementTask", type=project_Task, multiplicity=Multiplicity(0, 1))
    }
)
attributes177: BinaryAssociation = BinaryAssociation(
    name="attributes177",
    ends={
        Property(name="project_TaskAttribute179", type=project_SupplementTask, multiplicity=Multiplicity(1, 1)),
        Property(name="project_SupplementTask178", type=project_TaskAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hideResource180: BinaryAssociation = BinaryAssociation(
    name="hideResource180",
    ends={
        Property(name="project_HideResource181", type=project_TagFile, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TagFile", type=project_HideResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rollupResource185: BinaryAssociation = BinaryAssociation(
    name="rollupResource185",
    ends={
        Property(name="project_RollupResource187", type=project_TagFile, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TagFile186", type=project_RollupResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rollupTask188: BinaryAssociation = BinaryAssociation(
    name="rollupTask188",
    ends={
        Property(name="project_RollupTask190", type=project_TagFile, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TagFile189", type=project_RollupTask, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
task191: BinaryAssociation = BinaryAssociation(
    name="task191",
    ends={
        Property(name="project_Task192", type=project_TaskStatusSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TaskStatusSheet", type=project_Task, multiplicity=Multiplicity(0, 1))
    }
)
attributes193: BinaryAssociation = BinaryAssociation(
    name="attributes193",
    ends={
        Property(name="project_TaskStatusSheetAttribute", type=project_TaskStatusSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TaskStatusSheet194", type=project_TaskStatusSheetAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hideTask182: BinaryAssociation = BinaryAssociation(
    name="hideTask182",
    ends={
        Property(name="project_HideTask184", type=project_TagFile, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TagFile183", type=project_HideTask, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes197: BinaryAssociation = BinaryAssociation(
    name="attributes197",
    ends={
        Property(name="project_TaskTimesheetAttribute", type=project_TaskTimesheet, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TaskTimesheet198", type=project_TaskTimesheetAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task199: BinaryAssociation = BinaryAssociation(
    name="task199",
    ends={
        Property(name="project_Task200", type=project_TaskPrefix, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TaskPrefix", type=project_Task, multiplicity=Multiplicity(0, 1))
    }
)
task195: BinaryAssociation = BinaryAssociation(
    name="task195",
    ends={
        Property(name="project_Task196", type=project_TaskTimesheet, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TaskTimesheet", type=project_Task, multiplicity=Multiplicity(0, 1))
    }
)
task201: BinaryAssociation = BinaryAssociation(
    name="task201",
    ends={
        Property(name="project_Task202", type=project_TaskRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TaskRoot", type=project_Task, multiplicity=Multiplicity(0, 1))
    }
)
interval205: BinaryAssociation = BinaryAssociation(
    name="interval205",
    ends={
        Property(name="project_Interval4207", type=project_Timesheet, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Timesheet206", type=project_Interval4, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes208: BinaryAssociation = BinaryAssociation(
    name="attributes208",
    ends={
        Property(name="project_TimesheetAttribute", type=project_Timesheet, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Timesheet209", type=project_TimesheetAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes210: BinaryAssociation = BinaryAssociation(
    name="attributes210",
    ends={
        Property(name="project_TimesheetReportAttribute", type=project_TimesheetReport, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TimesheetReport", type=project_TimesheetReportAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resource203: BinaryAssociation = BinaryAssociation(
    name="resource203",
    ends={
        Property(name="project_Resource204", type=project_Timesheet, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Timesheet", type=project_Resource, multiplicity=Multiplicity(0, 1))
    }
)
expression211: BinaryAssociation = BinaryAssociation(
    name="expression211",
    ends={
        Property(name="project_ToolTip", type=project_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="project_LogicalExpression212", type=project_ToolTip, multiplicity=Multiplicity(1, 1))
    }
)
scenario213: BinaryAssociation = BinaryAssociation(
    name="scenario213",
    ends={
        Property(name="project_Scenario214", type=project_TrackingScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TrackingScenario", type=project_Scenario, multiplicity=Multiplicity(0, 1))
    }
)
expression218: BinaryAssociation = BinaryAssociation(
    name="expression218",
    ends={
        Property(name="project_LogicalExpression219", type=project_Warn, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Warn", type=project_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
intervals215: BinaryAssociation = BinaryAssociation(
    name="intervals215",
    ends={
        Property(name="project_Interval3217", type=project_Vacation, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Vacation216", type=project_Interval3, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
weekdays220: BinaryAssociation = BinaryAssociation(
    name="weekdays220",
    ends={
        Property(name="project_Weekdays", type=project_WorkingHours, multiplicity=Multiplicity(1, 1)),
        Property(name="project_WorkingHours221", type=project_Weekdays, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hours222: BinaryAssociation = BinaryAssociation(
    name="hours222",
    ends={
        Property(name="project_WorkHours", type=project_WorkingHours, multiplicity=Multiplicity(1, 1)),
        Property(name="project_WorkingHours223", type=project_WorkHours, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute227: BinaryAssociation = BinaryAssociation(
    name="attribute227",
    ends={
        Property(name="project_ColumnAttribute", type=project_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Column228", type=project_ColumnAttribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
account224: BinaryAssociation = BinaryAssociation(
    name="account224",
    ends={
        Property(name="project_Account226", type=project_AccountShare, multiplicity=Multiplicity(1, 1)),
        Property(name="project_AccountShare225", type=project_Account, multiplicity=Multiplicity(0, 1))
    }
)
duration229: BinaryAssociation = BinaryAssociation(
    name="duration229",
    ends={
        Property(name="project_DurationQuantity230", type=project_Limit, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Limit", type=project_DurationQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes231: BinaryAssociation = BinaryAssociation(
    name="attributes231",
    ends={
        Property(name="project_LimitAttribute", type=project_Limit, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Limit232", type=project_LimitAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
period233: BinaryAssociation = BinaryAssociation(
    name="period233",
    ends={
        Property(name="project_Interval1235", type=project_LimitAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="project_LimitAttribute234", type=project_Interval1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resources236: BinaryAssociation = BinaryAssociation(
    name="resources236",
    ends={
        Property(name="project_Resource238", type=project_LimitAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="project_LimitAttribute237", type=project_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
task239: BinaryAssociation = BinaryAssociation(
    name="task239",
    ends={
        Property(name="project_Task240", type=project_TaskDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TaskDependency", type=project_Task, multiplicity=Multiplicity(0, 1))
    }
)
gapDuration241: BinaryAssociation = BinaryAssociation(
    name="gapDuration241",
    ends={
        Property(name="project_GapDuration", type=project_TaskDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TaskDependency242", type=project_GapDuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gapLength243: BinaryAssociation = BinaryAssociation(
    name="gapLength243",
    ends={
        Property(name="project_GapLength", type=project_TaskDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="project_TaskDependency244", type=project_GapLength, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand245: BinaryAssociation = BinaryAssociation(
    name="leftOperand245",
    ends={
        Property(name="project_LogicalExpression246", type=project_XBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="project_XBinaryOperation", type=project_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature247: BinaryAssociation = BinaryAssociation(
    name="feature247",
    ends={
        Property(name="project_JvmIdentifiableElement", type=project_XBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="project_XBinaryOperation248", type=project_JvmIdentifiableElement, multiplicity=Multiplicity(0, 1))
    }
)
rightOperand249: BinaryAssociation = BinaryAssociation(
    name="rightOperand249",
    ends={
        Property(name="project_LogicalExpression251", type=project_XBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="project_XBinaryOperation250", type=project_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function252: BinaryAssociation = BinaryAssociation(
    name="function252",
    ends={
        Property(name="project_Function253", type=project_LogicalFunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="project_LogicalFunctionExpression", type=project_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_project_Account_Property = Generalization(general=Property_, specific=project_Account)
gen_project_Account_AccountAttribute = Generalization(general=AccountAttribute, specific=project_Account)
gen_project_AccountPrefix_IncludePropertiesAttribute = Generalization(general=IncludePropertiesAttribute, specific=project_AccountPrefix)
gen_project_AccountReport_Property = Generalization(general=Property_, specific=project_AccountReport)
gen_project_AccountReport_ReportAttribute = Generalization(general=ReportAttribute, specific=project_AccountReport)
gen_project_Task_Property = Generalization(general=Property_, specific=project_Task)
gen_project_Task_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Task)
gen_project_Report_AccountReport = Generalization(general=AccountReport, specific=project_Report)
gen_project_Report_ResourceReport = Generalization(general=ResourceReport, specific=project_Report)
gen_project_Report_TaskReport = Generalization(general=TaskReport, specific=project_Report)
gen_project_AccountRoot_ReportAttribute = Generalization(general=ReportAttribute, specific=project_AccountRoot)
gen_project_IcalReport_Property = Generalization(general=Property_, specific=project_IcalReport)
gen_project_Export_Property = Generalization(general=Property_, specific=project_Export)
gen_project_Resource_Property = Generalization(general=Property_, specific=project_Resource)
gen_project_Resource_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_Resource)
gen_project_Report_TextReport = Generalization(general=TextReport, specific=project_Report)
gen_project_Allocate_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Allocate)
gen_project_Navigator_Property = Generalization(general=Property_, specific=project_Navigator)
gen_project_NewTask_TimesheetAttribute = Generalization(general=TimesheetAttribute, specific=project_NewTask)
gen_project_NikuReport_Property = Generalization(general=Property_, specific=project_NikuReport)
gen_project_Alternative_AllocateResourceAttribute = Generalization(general=AllocateResourceAttribute, specific=project_Alternative)
gen_project_Author_StatusStatusSheetAttribute = Generalization(general=StatusStatusSheetAttribute, specific=project_Author)
gen_project_Balance_Property = Generalization(general=Property_, specific=project_Balance)
gen_project_Balance_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Balance)
gen_project_BookingTask_TaskAttribute = Generalization(general=TaskAttribute, specific=project_BookingTask)
gen_project_BookingResource_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_BookingResource)
gen_project_CellText_ColumnAttribute = Generalization(general=ColumnAttribute, specific=project_CellText)
gen_project_Center_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Center)
gen_project_Charge_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Charge)
gen_project_ChargeSet_TaskAttribute = Generalization(general=TaskAttribute, specific=project_ChargeSet)
gen_project_Columns_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Columns)
gen_project_Complete_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Complete)
gen_project_Copyright_Property = Generalization(general=Property_, specific=project_Copyright)
gen_project_Credit_AccountAttribute = Generalization(general=AccountAttribute, specific=project_Credit)
gen_project_Currency_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_Currency)
gen_project_CurrencyFormat_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_CurrencyFormat)
gen_project_CurrencyFormat_ReportAttribute = Generalization(general=ReportAttribute, specific=project_CurrencyFormat)
gen_project_DailyMax_LimitsAttribute = Generalization(general=LimitsAttribute, specific=project_DailyMax)
gen_project_Caption_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Caption)
gen_project_CellColor_ColumnAttribute = Generalization(general=ColumnAttribute, specific=project_CellColor)
gen_project_Details_StatusTimesheetAttribute = Generalization(general=StatusTimesheetAttribute, specific=project_Details)
gen_project_Duration_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Duration)
gen_project_Efficiency_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_Efficiency)
gen_project_Effort_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Effort)
gen_project_Email_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_Email)
gen_project_End_TaskAttribute = Generalization(general=TaskAttribute, specific=project_End)
gen_project_End_ReportAttribute = Generalization(general=ReportAttribute, specific=project_End)
gen_project_End_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=project_End)
gen_project_End_ExportAttribute = Generalization(general=ExportAttribute, specific=project_End)
gen_project_End_NewTaskAttribute = Generalization(general=NewTaskAttribute, specific=project_End)
gen_project_End_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=project_End)
gen_project_End_StatusSheetReportAttribute = Generalization(general=StatusSheetReportAttribute, specific=project_End)
gen_project_End_TaskTimesheetAttribute = Generalization(general=TaskTimesheetAttribute, specific=project_End)
gen_project_End_TimesheetReportAttribute = Generalization(general=TimesheetReportAttribute, specific=project_End)
gen_project_End_ColumnAttribute = Generalization(general=ColumnAttribute, specific=project_End)
gen_project_EndCredit_TaskAttribute = Generalization(general=TaskAttribute, specific=project_EndCredit)
gen_project_Epilog_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Epilog)
gen_project_ExtendResource_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_ExtendResource)
gen_project_DailyMin_LimitsAttribute = Generalization(general=LimitsAttribute, specific=project_DailyMin)
gen_project_DailyWorkingHours_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_DailyWorkingHours)
gen_project_Definitions_ExportAttribute = Generalization(general=ExportAttribute, specific=project_Definitions)
gen_project_Depends_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Depends)
gen_project_Details_StatusStatusSheetAttribute = Generalization(general=StatusStatusSheetAttribute, specific=project_Details)
gen_project_ExtendedTaskAttribute_TaskAttribute = Generalization(general=TaskAttribute, specific=project_ExtendedTaskAttribute)
gen_project_Fail_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Fail)
gen_project_Fail_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_Fail)
gen_project_ExtendedResourceAttribute_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_ExtendedResourceAttribute)
gen_project_ExtendTask_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_ExtendTask)
gen_project_Footer_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Footer)
gen_project_Formats_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Formats)
gen_project_Formats_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=project_Formats)
gen_project_HAlign_ColumnAttribute = Generalization(general=ColumnAttribute, specific=project_HAlign)
gen_project_Header_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Header)
gen_project_Headline_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Headline)
gen_project_Headline_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=project_Headline)
gen_project_HideAccount_ReportAttribute = Generalization(general=ReportAttribute, specific=project_HideAccount)
gen_project_HideJournalEntry_ReportAttribute = Generalization(general=ReportAttribute, specific=project_HideJournalEntry)
gen_project_HideJournalEntry_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=project_HideJournalEntry)
gen_project_HideReport_NavigatorAttribute = Generalization(general=NavigatorAttribute, specific=project_HideReport)
gen_project_Flags_Property = Generalization(general=Property_, specific=project_Flags)
gen_project_Flags_AccountAttribute = Generalization(general=AccountAttribute, specific=project_Flags)
gen_project_Flags_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Flags)
gen_project_Flags_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Flags)
gen_project_Flags_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_Flags)
gen_project_Flags_StatusStatusSheetAttribute = Generalization(general=StatusStatusSheetAttribute, specific=project_Flags)
gen_project_Flags_StatusTimesheetAttribute = Generalization(general=StatusTimesheetAttribute, specific=project_Flags)
gen_project_HideTask_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=project_HideTask)
gen_project_FontColor_ColumnAttribute = Generalization(general=ColumnAttribute, specific=project_FontColor)
gen_project_HideTask_ExportAttribute = Generalization(general=ExportAttribute, specific=project_HideTask)
gen_project_HideTask_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=project_HideTask)
gen_project_HideTask_StatusSheetReportAttribute = Generalization(general=StatusSheetReportAttribute, specific=project_HideTask)
gen_project_Include_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_Include)
gen_project_IncludeProperties_Property = Generalization(general=Property_, specific=project_IncludeProperties)
gen_project_HideResource_ReportAttribute = Generalization(general=ReportAttribute, specific=project_HideResource)
gen_project_HideResource_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=project_HideResource)
gen_project_HideResource_ExportAttribute = Generalization(general=ExportAttribute, specific=project_HideResource)
gen_project_HideResource_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=project_HideResource)
gen_project_HideResource_StatusSheetReportAttribute = Generalization(general=StatusSheetReportAttribute, specific=project_HideResource)
gen_project_HideResource_TimesheetReportAttribute = Generalization(general=TimesheetReportAttribute, specific=project_HideResource)
gen_project_HideTask_ReportAttribute = Generalization(general=ReportAttribute, specific=project_HideTask)
gen_project_JournalAttributes_ReportAttribute = Generalization(general=ReportAttribute, specific=project_JournalAttributes)
gen_project_JournalEntry_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_JournalEntry)
gen_project_JournalEntry_TaskAttribute = Generalization(general=TaskAttribute, specific=project_JournalEntry)
gen_project_JournalEntry_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_JournalEntry)
gen_project_JournalMode_ReportAttribute = Generalization(general=ReportAttribute, specific=project_JournalMode)
gen_project_Left_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Left)
gen_project_Length_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Length)
gen_project_Limits_Property = Generalization(general=Property_, specific=project_Limits)
gen_project_Limits_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Limits)
gen_project_Limits_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_Limits)
gen_project_Macro_Property = Generalization(general=Property_, specific=project_Macro)
gen_project_Managers_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_Managers)
gen_project_Mandatory_AllocateResourceAttribute = Generalization(general=AllocateResourceAttribute, specific=project_Mandatory)
gen_project_MaxEnd_TaskAttribute = Generalization(general=TaskAttribute, specific=project_MaxEnd)
gen_project_Maximum_LimitsAttribute = Generalization(general=LimitsAttribute, specific=project_Maximum)
gen_project_MaxStart_TaskAttribute = Generalization(general=TaskAttribute, specific=project_MaxStart)
gen_project_ListItem_ColumnAttribute = Generalization(general=ColumnAttribute, specific=project_ListItem)
gen_project_ListType_ColumnAttribute = Generalization(general=ColumnAttribute, specific=project_ListType)
gen_project_LoadUnit_ReportAttribute = Generalization(general=ReportAttribute, specific=project_LoadUnit)
gen_project_MinStart_TaskAttribute = Generalization(general=TaskAttribute, specific=project_MinStart)
gen_project_MonthlyMax_LimitsAttribute = Generalization(general=LimitsAttribute, specific=project_MonthlyMax)
gen_project_MonthlyMin_LimitsAttribute = Generalization(general=LimitsAttribute, specific=project_MonthlyMin)
gen_project_Note_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Note)
gen_project_Now_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_Now)
gen_project_NumberFormat_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_NumberFormat)
gen_project_NumberFormat_ReportAttribute = Generalization(general=ReportAttribute, specific=project_NumberFormat)
gen_project_NumberFormat_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=project_NumberFormat)
gen_project_Period_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Period)
gen_project_Period_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Period)
gen_project_Period_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=project_Period)
gen_project_Period_ExportAttribute = Generalization(general=ExportAttribute, specific=project_Period)
gen_project_Period_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=project_Period)
gen_project_Period_StatusSheetReportAttribute = Generalization(general=StatusSheetReportAttribute, specific=project_Period)
gen_project_Period_TimesheetReportAttribute = Generalization(general=TimesheetReportAttribute, specific=project_Period)
gen_project_Milestone_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Milestone)
gen_project_Minimum_LimitsAttribute = Generalization(general=LimitsAttribute, specific=project_Minimum)
gen_project_MinEnd_TaskAttribute = Generalization(general=TaskAttribute, specific=project_MinEnd)
gen_project_Precedes_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Precedes)
gen_project_Priority_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Priority)
gen_project_Priority_NewTaskAttribute = Generalization(general=NewTaskAttribute, specific=project_Priority)
gen_project_Priority_TaskTimesheetAttribute = Generalization(general=TaskTimesheetAttribute, specific=project_Priority)
gen_project_ProjectId_TaskAttribute = Generalization(general=TaskAttribute, specific=project_ProjectId)
gen_project_ProjectIds_Property = Generalization(general=Property_, specific=project_ProjectIds)
gen_project_Prolog_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Prolog)
gen_project_PurgeReport_ReportAttribute = Generalization(general=ReportAttribute, specific=project_PurgeReport)
gen_project_Period_ColumnAttribute = Generalization(general=ColumnAttribute, specific=project_Period)
gen_project_Persistent_AllocateResourceAttribute = Generalization(general=AllocateResourceAttribute, specific=project_Persistent)
gen_project_PurgeResource_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_PurgeResource)
gen_project_PurgeTask_TaskAttribute = Generalization(general=TaskAttribute, specific=project_PurgeTask)
gen_project_Remaining_NewTaskAttribute = Generalization(general=NewTaskAttribute, specific=project_Remaining)
gen_project_Remaining_TaskTimesheetAttribute = Generalization(general=TaskTimesheetAttribute, specific=project_Remaining)
gen_project_ReportPrefix_IncludePropertiesAttribute = Generalization(general=IncludePropertiesAttribute, specific=project_ReportPrefix)
gen_project_ResourceAttributes_ExportAttribute = Generalization(general=ExportAttribute, specific=project_ResourceAttributes)
gen_project_ResourcePrefix_IncludePropertiesAttribute = Generalization(general=IncludePropertiesAttribute, specific=project_ResourcePrefix)
gen_project_Rate_Property = Generalization(general=Property_, specific=project_Rate)
gen_project_Rate_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_Rate)
gen_project_Responsible_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Responsible)
gen_project_Right_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Right)
gen_project_RollupAccount_ReportAttribute = Generalization(general=ReportAttribute, specific=project_RollupAccount)
gen_project_RollupResource_ReportAttribute = Generalization(general=ReportAttribute, specific=project_RollupResource)
gen_project_RollupResource_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=project_RollupResource)
gen_project_RollupResource_ExportAttribute = Generalization(general=ExportAttribute, specific=project_RollupResource)
gen_project_ResourceReport_Property = Generalization(general=Property_, specific=project_ResourceReport)
gen_project_ResourceReport_ReportAttribute = Generalization(general=ReportAttribute, specific=project_ResourceReport)
gen_project_ResourceRoot_ReportAttribute = Generalization(general=ReportAttribute, specific=project_ResourceRoot)
gen_project_Scale_ColumnAttribute = Generalization(general=ColumnAttribute, specific=project_Scale)
gen_project_Scenario_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_Scenario)
gen_project_ScenarioIcal_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=project_ScenarioIcal)
gen_project_Scenarios_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Scenarios)
gen_project_Scenarios_ExportAttribute = Generalization(general=ExportAttribute, specific=project_Scenarios)
gen_project_RollupTask_ReportAttribute = Generalization(general=ReportAttribute, specific=project_RollupTask)
gen_project_RollupTask_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=project_RollupTask)
gen_project_RollupTask_ExportAttribute = Generalization(general=ExportAttribute, specific=project_RollupTask)
gen_project_Scheduling_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Scheduling)
gen_project_Select_AllocateResourceAttribute = Generalization(general=AllocateResourceAttribute, specific=project_Select)
gen_project_SelfContained_ReportAttribute = Generalization(general=ReportAttribute, specific=project_SelfContained)
gen_project_Shift_Property = Generalization(general=Property_, specific=project_Shift)
gen_project_Scheduled_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Scheduled)
gen_project_Shifts_ShiftsResource = Generalization(general=ShiftsResource, specific=project_Shifts)
gen_project_Shifts_ShiftsTask = Generalization(general=ShiftsTask, specific=project_Shifts)
gen_project_ShiftsAllocate_AllocateResourceAttribute = Generalization(general=AllocateResourceAttribute, specific=project_ShiftsAllocate)
gen_project_ShiftTimesheet_TimesheetAttribute = Generalization(general=TimesheetAttribute, specific=project_ShiftTimesheet)
gen_project_Sort_SortAccounts = Generalization(general=SortAccounts, specific=project_Sort)
gen_project_Sort_SortJournalEntries = Generalization(general=SortJournalEntries, specific=project_Sort)
gen_project_Sort_SortResources = Generalization(general=SortResources, specific=project_Sort)
gen_project_Sort_SortTasks = Generalization(general=SortTasks, specific=project_Sort)
gen_project_SortAccounts_ReportAttribute = Generalization(general=ReportAttribute, specific=project_SortAccounts)
gen_project_SortJournalEntries_ReportAttribute = Generalization(general=ReportAttribute, specific=project_SortJournalEntries)
gen_project_SortResources_ReportAttribute = Generalization(general=ReportAttribute, specific=project_SortResources)
gen_project_SortResources_StatusSheetReportAttribute = Generalization(general=StatusSheetReportAttribute, specific=project_SortResources)
gen_project_SortTasks_ReportAttribute = Generalization(general=ReportAttribute, specific=project_SortTasks)
gen_project_SortTasks_StatusSheetReportAttribute = Generalization(general=StatusSheetReportAttribute, specific=project_SortTasks)
gen_project_Start_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Start)
gen_project_Start_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Start)
gen_project_Start_IcalReportAttribute = Generalization(general=IcalReportAttribute, specific=project_Start)
gen_project_Start_ExportAttribute = Generalization(general=ExportAttribute, specific=project_Start)
gen_project_Start_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=project_Start)
gen_project_Start_StatusSheetReportAttribute = Generalization(general=StatusSheetReportAttribute, specific=project_Start)
gen_project_ShiftsResource_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_ShiftsResource)
gen_project_ShiftsTask_TaskAttribute = Generalization(general=TaskAttribute, specific=project_ShiftsTask)
gen_project_ShortTimeFormat_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_ShortTimeFormat)
gen_project_StatusTimesheet_TaskTimesheetAttribute = Generalization(general=TaskTimesheetAttribute, specific=project_StatusTimesheet)
gen_project_StatusTimesheet_TimesheetAttribute = Generalization(general=TimesheetAttribute, specific=project_StatusTimesheet)
gen_project_StatusSheet_Property = Generalization(general=Property_, specific=project_StatusSheet)
gen_project_Start_TimesheetReportAttribute = Generalization(general=TimesheetReportAttribute, specific=project_Start)
gen_project_Start_ColumnAttribute = Generalization(general=ColumnAttribute, specific=project_Start)
gen_project_StatusStatusSheet_TaskStatusSheetAttribute = Generalization(general=TaskStatusSheetAttribute, specific=project_StatusStatusSheet)
gen_project_StatusSheetReport_Property = Generalization(general=Property_, specific=project_StatusSheetReport)
gen_project_SupplementReport_Property = Generalization(general=Property_, specific=project_SupplementReport)
gen_project_Summary_StatusStatusSheetAttribute = Generalization(general=StatusStatusSheetAttribute, specific=project_Summary)
gen_project_Summary_StatusTimesheetAttribute = Generalization(general=StatusTimesheetAttribute, specific=project_Summary)
gen_project_SupplementAccount_Property = Generalization(general=Property_, specific=project_SupplementAccount)
gen_project_SupplementTask_Property = Generalization(general=Property_, specific=project_SupplementTask)
gen_project_SupplementTask_TaskAttribute = Generalization(general=TaskAttribute, specific=project_SupplementTask)
gen_project_SupplementResource_Property = Generalization(general=Property_, specific=project_SupplementResource)
gen_project_SupplementResource_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_SupplementResource)
gen_project_TagFile_Property = Generalization(general=Property_, specific=project_TagFile)
gen_project_TaskStatusSheet_StatusSheetAttribute = Generalization(general=StatusSheetAttribute, specific=project_TaskStatusSheet)
gen_project_TaskStatusSheet_TaskStatusSheetAttribute = Generalization(general=TaskStatusSheetAttribute, specific=project_TaskStatusSheet)
gen_project_TaskTimesheet_TimesheetAttribute = Generalization(general=TimesheetAttribute, specific=project_TaskTimesheet)
gen_project_TaskAttributes_ExportAttribute = Generalization(general=ExportAttribute, specific=project_TaskAttributes)
gen_project_TaskPrefix_IncludePropertiesAttribute = Generalization(general=IncludePropertiesAttribute, specific=project_TaskPrefix)
gen_project_TextReport_Property = Generalization(general=Property_, specific=project_TextReport)
gen_project_TextReport_ReportAttribute = Generalization(general=ReportAttribute, specific=project_TextReport)
gen_project_TimeFormat_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_TimeFormat)
gen_project_TimeFormat_ReportAttribute = Generalization(general=ReportAttribute, specific=project_TimeFormat)
gen_project_Timeoff_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=project_Timeoff)
gen_project_Timesheet_Property = Generalization(general=Property_, specific=project_Timesheet)
gen_project_TaskReport_Property = Generalization(general=Property_, specific=project_TaskReport)
gen_project_TaskReport_ReportAttribute = Generalization(general=ReportAttribute, specific=project_TaskReport)
gen_project_TaskRoot_ReportAttribute = Generalization(general=ReportAttribute, specific=project_TaskRoot)
gen_project_TimesheetReport_Property = Generalization(general=Property_, specific=project_TimesheetReport)
gen_project_Timezone_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_Timezone)
gen_project_Timezone_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Timezone)
gen_project_Timezone_ExportAttribute = Generalization(general=ExportAttribute, specific=project_Timezone)
gen_project_TimingResolution_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_TimingResolution)
gen_project_Title_ReportAttribute = Generalization(general=ReportAttribute, specific=project_Title)
gen_project_Title_NikuReportAttribute = Generalization(general=NikuReportAttribute, specific=project_Title)
gen_project_Title_ColumnAttribute = Generalization(general=ColumnAttribute, specific=project_Title)
gen_project_TrackingScenario_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_TrackingScenario)
gen_project_Vacation_Property = Generalization(general=Property_, specific=project_Vacation)
gen_project_Vacation_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_Vacation)
gen_project_ToolTip_ColumnAttribute = Generalization(general=ColumnAttribute, specific=project_ToolTip)
gen_project_Warn_TaskAttribute = Generalization(general=TaskAttribute, specific=project_Warn)
gen_project_Warn_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_Warn)
gen_project_WeekStarts_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_WeekStarts)
gen_project_WeeklyMax_LimitsAttribute = Generalization(general=LimitsAttribute, specific=project_WeeklyMax)
gen_project_Width_ColumnAttribute = Generalization(general=ColumnAttribute, specific=project_Width)
gen_project_Work_NewTaskAttribute = Generalization(general=NewTaskAttribute, specific=project_Work)
gen_project_Work_TaskTimesheetAttribute = Generalization(general=TaskTimesheetAttribute, specific=project_Work)
gen_project_WorkingHours_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_WorkingHours)
gen_project_WorkingHours_ResourceAttribute = Generalization(general=ResourceAttribute, specific=project_WorkingHours)
gen_project_WeeklyMin_LimitsAttribute = Generalization(general=LimitsAttribute, specific=project_WeeklyMin)
gen_project_YearlyWorkingDays_ProjectAttribute = Generalization(general=ProjectAttribute, specific=project_YearlyWorkingDays)
gen_project_DurationQuantity_GapDuration = Generalization(general=GapDuration, specific=project_DurationQuantity)
gen_project_DurationQuantity_GapLength = Generalization(general=GapLength, specific=project_DurationQuantity)
gen_project_Limit_DailyMax = Generalization(general=DailyMax, specific=project_Limit)
gen_project_Limit_DailyMin = Generalization(general=DailyMin, specific=project_Limit)
gen_project_Limit_Maximum = Generalization(general=Maximum, specific=project_Limit)
gen_project_Limit_Minimum = Generalization(general=Minimum, specific=project_Limit)
gen_project_Limit_MonthlyMax = Generalization(general=MonthlyMax, specific=project_Limit)
gen_project_Limit_MonthlyMin = Generalization(general=MonthlyMin, specific=project_Limit)
gen_project_Limit_WeeklyMax = Generalization(general=WeeklyMax, specific=project_Limit)
gen_project_Limit_WeeklyMin = Generalization(general=WeeklyMin, specific=project_Limit)
gen_project_RealFormat_CurrencyFormat = Generalization(general=CurrencyFormat, specific=project_RealFormat)
gen_project_RealFormat_NumberFormat = Generalization(general=NumberFormat, specific=project_RealFormat)
gen_project_TaskDependency_Depends = Generalization(general=Depends, specific=project_TaskDependency)
gen_project_TaskDependency_Precedes = Generalization(general=Precedes, specific=project_TaskDependency)
gen_project_RichText_Caption = Generalization(general=Caption, specific=project_RichText)
gen_project_RichText_Center = Generalization(general=Center, specific=project_RichText)
gen_project_RichText_Details = Generalization(general=Details, specific=project_RichText)
gen_project_RichText_Epilog = Generalization(general=Epilog, specific=project_RichText)
gen_project_RichText_Footer = Generalization(general=Footer, specific=project_RichText)
gen_project_RichText_Header = Generalization(general=Header, specific=project_RichText)
gen_project_RichText_Headline = Generalization(general=Headline, specific=project_RichText)
gen_project_RichText_Left = Generalization(general=Left, specific=project_RichText)
gen_project_RichText_ListItem = Generalization(general=ListItem, specific=project_RichText)
gen_project_RichText_Prolog = Generalization(general=Prolog, specific=project_RichText)
gen_project_RichText_Right = Generalization(general=Right, specific=project_RichText)
gen_project_RichText_Summary = Generalization(general=Summary, specific=project_RichText)
gen_project_Defintions_Definitions = Generalization(general=Definitions, specific=project_Defintions)
gen_project_XBinaryOperation_LogicalExpression = Generalization(general=LogicalExpression, specific=project_XBinaryOperation)
gen_project_LogicalFunctionExpression_LogicalExpression = Generalization(general=LogicalExpression, specific=project_LogicalFunctionExpression)
gen_project_LogicalAbsoluteIdExression_LogicalExpression = Generalization(general=LogicalExpression, specific=project_LogicalAbsoluteIdExression)
gen_project_LogicalBooleanLiteral_LogicalExpression = Generalization(general=LogicalExpression, specific=project_LogicalBooleanLiteral)
gen_project_LogicalStringLiteral_LogicalExpression = Generalization(general=LogicalExpression, specific=project_LogicalStringLiteral)
gen_project_LogicalDateLiteral_LogicalExpression = Generalization(general=LogicalExpression, specific=project_LogicalDateLiteral)
gen_project_LogicalNumeralLiteral_LogicalExpression = Generalization(general=LogicalExpression, specific=project_LogicalNumeralLiteral)

# Domain Model
domain_model = DomainModel(
    name="project",
    types={project_Project, project_Property, project_Account, Property_, AccountAttribute, project_AccountAttribute, project_AccountPrefix, IncludePropertiesAttribute, project_AccountReport, ReportAttribute, project_Global, project_Interval2, project_ProjectAttribute, project_Task, TaskAttribute, project_TaskAttribute, project_Report, AccountReport, ResourceReport, TaskReport, project_AccountRoot, project_ReportAttribute, project_IcalReport, project_IcalReportAttribute, project_Export, project_ExportAttribute, project_Resource, ResourceAttribute, TextReport, project_Allocate, project_AllocateResource, project_AllocateResourceAttribute, project_Navigator, project_NavigatorAttribute, project_NewTask, TimesheetAttribute, project_ResourceAttribute, project_NikuReport, project_NikuReportAttribute, project_Alert, project_Alternative, AllocateResourceAttribute, project_Author, StatusStatusSheetAttribute, project_Balance, project_NewTaskAttribute, project_Booking, project_Interval4, project_BookingTask, project_BookingResource, project_CellText, project_Center, project_Charge, project_ChargeSet, project_AccountShare, project_Columns, project_Column, project_Complete, project_Copyright, project_Credit, project_Currency, ProjectAttribute, project_CurrencyFormat, project_DailyMax, LimitsAttribute, project_Caption, project_CellColor, ColumnAttribute, project_LogicalExpression, project_RGB, StatusTimesheetAttribute, project_Duration, project_DurationQuantity, project_Efficiency, project_Effort, project_Email, project_End, IcalReportAttribute, NewTaskAttribute, NikuReportAttribute, StatusSheetReportAttribute, TaskTimesheetAttribute, TimesheetReportAttribute, project_EndCredit, project_Epilog, project_Extend, project_ExtendResource, project_DailyMin, project_DailyWorkingHours, project_Definitions, ExportAttribute, project_Depends, project_Details, project_ExtendedTaskAttribute, project_Fail, project_ExtendedResourceAttribute, project_ExtendTask, project_Footer, project_Formats, project_Function, project_Scenario, project_GapDuration, project_GapLength, project_HAlign, project_Header, project_Headline, project_HideAccount, project_HideJournalEntry, project_HideReport, NavigatorAttribute, project_Flags, project_FontColor, project_Include, project_IncludeProperties, project_IncludePropertiesAttribute, project_Interval1, project_Interval3, project_HideResource, project_HideTask, project_JournalAttributes, project_JournalEntry, project_Summary, project_JournalMode, project_Left, project_Length, project_Limits, project_LimitsAttribute, project_Macro, project_Managers, project_Mandatory, project_MaxEnd, project_Maximum, project_MaxStart, project_ListItem, project_ListType, project_LoadUnit, project_MinStart, project_MonthlyMax, project_MonthlyMin, project_Note, project_Now, project_NumberFormat, project_Period, project_Milestone, project_Minimum, project_MinEnd, project_Precedes, project_Priority, project_ProjectId, project_ProjectIds, project_Prolog, project_PurgeReport, project_Persistent, project_PurgeResource, project_PurgeTask, project_ReportPrefix, project_ResourceAttributes, project_ResourcePrefix, project_ResourceReport, project_Rate, project_Remaining, project_Responsible, project_Right, project_RollupAccount, project_RollupResource, project_ResourceRoot, project_Scale, project_ScenarioIcal, project_Scenarios, project_Scheduled, project_RollupTask, project_Scheduling, project_Select, project_SelfContained, project_Shift, project_Vacation, project_Shifts, ShiftsResource, ShiftsTask, project_ShiftsLimit, project_ShiftsAllocate, project_WorkingHours, project_ShiftTimesheet, SortAccounts, SortJournalEntries, SortResources, SortTasks, project_Criterion, project_SortAccounts, project_SortJournalEntries, project_SortResources, project_SortTasks, project_Start, project_ShiftsResource, project_ShiftsTask, project_ShortTimeFormat, project_Sort, project_StatusStatusSheetAttribute, project_StatusTimesheet, project_StatusTimesheetAttribute, project_StatusSheet, project_StatusStatusSheet, TaskStatusSheetAttribute, project_StatusSheetAttribute, project_StatusSheetReport, project_StatusSheetReportAttribute, project_SupplementReport, project_SupplementAccount, project_SupplementTask, project_SupplementResource, project_TagFile, project_TaskStatusSheet, StatusSheetAttribute, project_TaskStatusSheetAttribute, project_TaskTimesheet, project_TaskAttributes, project_TaskPrefix, project_TaskTimesheetAttribute, project_TextReport, project_TimeFormat, project_Timeoff, project_Timesheet, project_TaskReport, project_TaskRoot, project_TimesheetAttribute, project_TimesheetReport, project_TimesheetReportAttribute, project_Timezone, project_TimingResolution, project_Title, project_ToolTip, project_TrackingScenario, project_TreeLevel, project_Warn, project_WeekStarts, project_WeeklyMax, project_Work, project_Weekdays, project_WeeklyMin, project_Width, project_YearlyWorkingDays, project_WorkHours, project_ColumnAttribute, GapDuration, GapLength, project_Limit, DailyMax, DailyMin, Maximum, Minimum, MonthlyMax, MonthlyMin, WeeklyMax, WeeklyMin, project_LimitAttribute, project_RealFormat, CurrencyFormat, NumberFormat, project_TaskDependency, Depends, Precedes, project_RichText, Caption, Center, Details, Epilog, Footer, Header, Headline, Left, ListItem, Prolog, Right, Summary, project_Defintions, Definitions, project_XBinaryOperation, LogicalExpression, project_JvmIdentifiableElement, project_LogicalFunctionExpression, project_LogicalAbsoluteIdExression, project_LogicalBooleanLiteral, project_LogicalStringLiteral, project_LogicalDateLiteral, project_LogicalNumeralLiteral, PurgeReportAttribute, PurgeResourceAttribute, PurgeTaskAttribute, ChargeApplies, Justification, JournalModeValue, ListTypeValues, CriterionDirection, YesNo, JournalEntrySortCriterion, LoadDisplayUnit, ReportFormat, SelectArgument, ColumnId, ScaleResolution, AlertLevel, DependsPolicy, TimeUnit, Weekday, WorkQuantityUnit, SchedulingPolicy},
    associations={project0, properties1, attributes3, account4, account6, interval8, attributes10, attributes12, attributes13, attributes14, attributes15, attributes16, resources17, resource18, attributes21, attributes23, attributes25, resources26, resource28, cost30, attributes24, revenue32, interval35, resource36, booking38, task41, expresssion49, accountShares51, columns52, booking43, expression46, color47, duration53, effort54, extends56, extend61, extend57, extends59, scenario65, task66, resource69, expression72, expression63, expression78, attributes80, duration81, duration83, expression74, expression76, duration88, duration86, summary97, length99, attributes101, alert91, author92, details95, resources102, period104, remaining106, report108, resource110, resource112, resources114, expression116, expression118, scenario123, scenario125, scenarios127, expression120, vacation129, shift135, limits137, shift138, limit141, shift144, intervals146, shift131, workingHours133, criteria149, attributes150, attributes151, resource152, attributes157, attributes159, interval154, account160, attributes162, report165, attributes167, resource170, attributes172, task175, attributes177, hideResource180, rollupResource185, rollupTask188, task191, attributes193, hideTask182, attributes197, task199, task195, task201, interval205, attributes208, attributes210, resource203, expression211, scenario213, expression218, intervals215, weekdays220, hours222, attribute227, account224, duration229, attributes231, period233, resources236, task239, gapDuration241, gapLength243, leftOperand245, feature247, rightOperand249, function252},
    generalizations={gen_project_Account_Property, gen_project_Account_AccountAttribute, gen_project_AccountPrefix_IncludePropertiesAttribute, gen_project_AccountReport_Property, gen_project_AccountReport_ReportAttribute, gen_project_Task_Property, gen_project_Task_TaskAttribute, gen_project_Report_AccountReport, gen_project_Report_ResourceReport, gen_project_Report_TaskReport, gen_project_AccountRoot_ReportAttribute, gen_project_IcalReport_Property, gen_project_Export_Property, gen_project_Resource_Property, gen_project_Resource_ResourceAttribute, gen_project_Report_TextReport, gen_project_Allocate_TaskAttribute, gen_project_Navigator_Property, gen_project_NewTask_TimesheetAttribute, gen_project_NikuReport_Property, gen_project_Alternative_AllocateResourceAttribute, gen_project_Author_StatusStatusSheetAttribute, gen_project_Balance_Property, gen_project_Balance_ReportAttribute, gen_project_BookingTask_TaskAttribute, gen_project_BookingResource_ResourceAttribute, gen_project_CellText_ColumnAttribute, gen_project_Center_ReportAttribute, gen_project_Charge_TaskAttribute, gen_project_ChargeSet_TaskAttribute, gen_project_Columns_ReportAttribute, gen_project_Complete_TaskAttribute, gen_project_Copyright_Property, gen_project_Credit_AccountAttribute, gen_project_Currency_ProjectAttribute, gen_project_CurrencyFormat_ProjectAttribute, gen_project_CurrencyFormat_ReportAttribute, gen_project_DailyMax_LimitsAttribute, gen_project_Caption_ReportAttribute, gen_project_CellColor_ColumnAttribute, gen_project_Details_StatusTimesheetAttribute, gen_project_Duration_TaskAttribute, gen_project_Efficiency_ResourceAttribute, gen_project_Effort_TaskAttribute, gen_project_Email_ResourceAttribute, gen_project_End_TaskAttribute, gen_project_End_ReportAttribute, gen_project_End_IcalReportAttribute, gen_project_End_ExportAttribute, gen_project_End_NewTaskAttribute, gen_project_End_NikuReportAttribute, gen_project_End_StatusSheetReportAttribute, gen_project_End_TaskTimesheetAttribute, gen_project_End_TimesheetReportAttribute, gen_project_End_ColumnAttribute, gen_project_EndCredit_TaskAttribute, gen_project_Epilog_ReportAttribute, gen_project_ExtendResource_ProjectAttribute, gen_project_DailyMin_LimitsAttribute, gen_project_DailyWorkingHours_ProjectAttribute, gen_project_Definitions_ExportAttribute, gen_project_Depends_TaskAttribute, gen_project_Details_StatusStatusSheetAttribute, gen_project_ExtendedTaskAttribute_TaskAttribute, gen_project_Fail_TaskAttribute, gen_project_Fail_ResourceAttribute, gen_project_ExtendedResourceAttribute_ResourceAttribute, gen_project_ExtendTask_ProjectAttribute, gen_project_Footer_ReportAttribute, gen_project_Formats_ReportAttribute, gen_project_Formats_NikuReportAttribute, gen_project_HAlign_ColumnAttribute, gen_project_Header_ReportAttribute, gen_project_Headline_ReportAttribute, gen_project_Headline_NikuReportAttribute, gen_project_HideAccount_ReportAttribute, gen_project_HideJournalEntry_ReportAttribute, gen_project_HideJournalEntry_IcalReportAttribute, gen_project_HideReport_NavigatorAttribute, gen_project_Flags_Property, gen_project_Flags_AccountAttribute, gen_project_Flags_TaskAttribute, gen_project_Flags_ReportAttribute, gen_project_Flags_ResourceAttribute, gen_project_Flags_StatusStatusSheetAttribute, gen_project_Flags_StatusTimesheetAttribute, gen_project_HideTask_IcalReportAttribute, gen_project_FontColor_ColumnAttribute, gen_project_HideTask_ExportAttribute, gen_project_HideTask_NikuReportAttribute, gen_project_HideTask_StatusSheetReportAttribute, gen_project_Include_ProjectAttribute, gen_project_IncludeProperties_Property, gen_project_HideResource_ReportAttribute, gen_project_HideResource_IcalReportAttribute, gen_project_HideResource_ExportAttribute, gen_project_HideResource_NikuReportAttribute, gen_project_HideResource_StatusSheetReportAttribute, gen_project_HideResource_TimesheetReportAttribute, gen_project_HideTask_ReportAttribute, gen_project_JournalAttributes_ReportAttribute, gen_project_JournalEntry_ProjectAttribute, gen_project_JournalEntry_TaskAttribute, gen_project_JournalEntry_ResourceAttribute, gen_project_JournalMode_ReportAttribute, gen_project_Left_ReportAttribute, gen_project_Length_TaskAttribute, gen_project_Limits_Property, gen_project_Limits_TaskAttribute, gen_project_Limits_ResourceAttribute, gen_project_Macro_Property, gen_project_Managers_ResourceAttribute, gen_project_Mandatory_AllocateResourceAttribute, gen_project_MaxEnd_TaskAttribute, gen_project_Maximum_LimitsAttribute, gen_project_MaxStart_TaskAttribute, gen_project_ListItem_ColumnAttribute, gen_project_ListType_ColumnAttribute, gen_project_LoadUnit_ReportAttribute, gen_project_MinStart_TaskAttribute, gen_project_MonthlyMax_LimitsAttribute, gen_project_MonthlyMin_LimitsAttribute, gen_project_Note_TaskAttribute, gen_project_Now_ProjectAttribute, gen_project_NumberFormat_ProjectAttribute, gen_project_NumberFormat_ReportAttribute, gen_project_NumberFormat_NikuReportAttribute, gen_project_Period_TaskAttribute, gen_project_Period_ReportAttribute, gen_project_Period_IcalReportAttribute, gen_project_Period_ExportAttribute, gen_project_Period_NikuReportAttribute, gen_project_Period_StatusSheetReportAttribute, gen_project_Period_TimesheetReportAttribute, gen_project_Milestone_TaskAttribute, gen_project_Minimum_LimitsAttribute, gen_project_MinEnd_TaskAttribute, gen_project_Precedes_TaskAttribute, gen_project_Priority_TaskAttribute, gen_project_Priority_NewTaskAttribute, gen_project_Priority_TaskTimesheetAttribute, gen_project_ProjectId_TaskAttribute, gen_project_ProjectIds_Property, gen_project_Prolog_ReportAttribute, gen_project_PurgeReport_ReportAttribute, gen_project_Period_ColumnAttribute, gen_project_Persistent_AllocateResourceAttribute, gen_project_PurgeResource_ResourceAttribute, gen_project_PurgeTask_TaskAttribute, gen_project_Remaining_NewTaskAttribute, gen_project_Remaining_TaskTimesheetAttribute, gen_project_ReportPrefix_IncludePropertiesAttribute, gen_project_ResourceAttributes_ExportAttribute, gen_project_ResourcePrefix_IncludePropertiesAttribute, gen_project_Rate_Property, gen_project_Rate_ResourceAttribute, gen_project_Responsible_TaskAttribute, gen_project_Right_ReportAttribute, gen_project_RollupAccount_ReportAttribute, gen_project_RollupResource_ReportAttribute, gen_project_RollupResource_IcalReportAttribute, gen_project_RollupResource_ExportAttribute, gen_project_ResourceReport_Property, gen_project_ResourceReport_ReportAttribute, gen_project_ResourceRoot_ReportAttribute, gen_project_Scale_ColumnAttribute, gen_project_Scenario_ProjectAttribute, gen_project_ScenarioIcal_IcalReportAttribute, gen_project_Scenarios_ReportAttribute, gen_project_Scenarios_ExportAttribute, gen_project_RollupTask_ReportAttribute, gen_project_RollupTask_IcalReportAttribute, gen_project_RollupTask_ExportAttribute, gen_project_Scheduling_TaskAttribute, gen_project_Select_AllocateResourceAttribute, gen_project_SelfContained_ReportAttribute, gen_project_Shift_Property, gen_project_Scheduled_TaskAttribute, gen_project_Shifts_ShiftsResource, gen_project_Shifts_ShiftsTask, gen_project_ShiftsAllocate_AllocateResourceAttribute, gen_project_ShiftTimesheet_TimesheetAttribute, gen_project_Sort_SortAccounts, gen_project_Sort_SortJournalEntries, gen_project_Sort_SortResources, gen_project_Sort_SortTasks, gen_project_SortAccounts_ReportAttribute, gen_project_SortJournalEntries_ReportAttribute, gen_project_SortResources_ReportAttribute, gen_project_SortResources_StatusSheetReportAttribute, gen_project_SortTasks_ReportAttribute, gen_project_SortTasks_StatusSheetReportAttribute, gen_project_Start_TaskAttribute, gen_project_Start_ReportAttribute, gen_project_Start_IcalReportAttribute, gen_project_Start_ExportAttribute, gen_project_Start_NikuReportAttribute, gen_project_Start_StatusSheetReportAttribute, gen_project_ShiftsResource_ResourceAttribute, gen_project_ShiftsTask_TaskAttribute, gen_project_ShortTimeFormat_ProjectAttribute, gen_project_StatusTimesheet_TaskTimesheetAttribute, gen_project_StatusTimesheet_TimesheetAttribute, gen_project_StatusSheet_Property, gen_project_Start_TimesheetReportAttribute, gen_project_Start_ColumnAttribute, gen_project_StatusStatusSheet_TaskStatusSheetAttribute, gen_project_StatusSheetReport_Property, gen_project_SupplementReport_Property, gen_project_Summary_StatusStatusSheetAttribute, gen_project_Summary_StatusTimesheetAttribute, gen_project_SupplementAccount_Property, gen_project_SupplementTask_Property, gen_project_SupplementTask_TaskAttribute, gen_project_SupplementResource_Property, gen_project_SupplementResource_ResourceAttribute, gen_project_TagFile_Property, gen_project_TaskStatusSheet_StatusSheetAttribute, gen_project_TaskStatusSheet_TaskStatusSheetAttribute, gen_project_TaskTimesheet_TimesheetAttribute, gen_project_TaskAttributes_ExportAttribute, gen_project_TaskPrefix_IncludePropertiesAttribute, gen_project_TextReport_Property, gen_project_TextReport_ReportAttribute, gen_project_TimeFormat_ProjectAttribute, gen_project_TimeFormat_ReportAttribute, gen_project_Timeoff_NikuReportAttribute, gen_project_Timesheet_Property, gen_project_TaskReport_Property, gen_project_TaskReport_ReportAttribute, gen_project_TaskRoot_ReportAttribute, gen_project_TimesheetReport_Property, gen_project_Timezone_ProjectAttribute, gen_project_Timezone_ReportAttribute, gen_project_Timezone_ExportAttribute, gen_project_TimingResolution_ProjectAttribute, gen_project_Title_ReportAttribute, gen_project_Title_NikuReportAttribute, gen_project_Title_ColumnAttribute, gen_project_TrackingScenario_ProjectAttribute, gen_project_Vacation_Property, gen_project_Vacation_ResourceAttribute, gen_project_ToolTip_ColumnAttribute, gen_project_Warn_TaskAttribute, gen_project_Warn_ResourceAttribute, gen_project_WeekStarts_ProjectAttribute, gen_project_WeeklyMax_LimitsAttribute, gen_project_Width_ColumnAttribute, gen_project_Work_NewTaskAttribute, gen_project_Work_TaskTimesheetAttribute, gen_project_WorkingHours_ProjectAttribute, gen_project_WorkingHours_ResourceAttribute, gen_project_WeeklyMin_LimitsAttribute, gen_project_YearlyWorkingDays_ProjectAttribute, gen_project_DurationQuantity_GapDuration, gen_project_DurationQuantity_GapLength, gen_project_Limit_DailyMax, gen_project_Limit_DailyMin, gen_project_Limit_Maximum, gen_project_Limit_Minimum, gen_project_Limit_MonthlyMax, gen_project_Limit_MonthlyMin, gen_project_Limit_WeeklyMax, gen_project_Limit_WeeklyMin, gen_project_RealFormat_CurrencyFormat, gen_project_RealFormat_NumberFormat, gen_project_TaskDependency_Depends, gen_project_TaskDependency_Precedes, gen_project_RichText_Caption, gen_project_RichText_Center, gen_project_RichText_Details, gen_project_RichText_Epilog, gen_project_RichText_Footer, gen_project_RichText_Header, gen_project_RichText_Headline, gen_project_RichText_Left, gen_project_RichText_ListItem, gen_project_RichText_Prolog, gen_project_RichText_Right, gen_project_RichText_Summary, gen_project_Defintions_Definitions, gen_project_XBinaryOperation_LogicalExpression, gen_project_LogicalFunctionExpression_LogicalExpression, gen_project_LogicalAbsoluteIdExression_LogicalExpression, gen_project_LogicalBooleanLiteral_LogicalExpression, gen_project_LogicalStringLiteral_LogicalExpression, gen_project_LogicalDateLiteral_LogicalExpression, gen_project_LogicalNumeralLiteral_LogicalExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)