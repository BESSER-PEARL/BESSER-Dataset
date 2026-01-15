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
VersionSwitchType: Enumeration = Enumeration(
    name="VersionSwitchType",
    literals={
            EnumerationLiteral(name="L1"),
			EnumerationLiteral(name="L2"),
			EnumerationLiteral(name="Both")
    }
)

Language: Enumeration = Enumeration(
    name="Language",
    literals={
            EnumerationLiteral(name="L1"),
			EnumerationLiteral(name="L2")
    }
)

BreakType: Enumeration = Enumeration(
    name="BreakType",
    literals={
            EnumerationLiteral(name="line"),
			EnumerationLiteral(name="page")
    }
)

BookTypes: Enumeration = Enumeration(
    name="BookTypes",
    literals={
            EnumerationLiteral(name="Octochechos"),
			EnumerationLiteral(name="Menaion"),
			EnumerationLiteral(name="Euchologion"),
			EnumerationLiteral(name="Pentecostarion"),
			EnumerationLiteral(name="Triodion"),
			EnumerationLiteral(name="Horologion"),
			EnumerationLiteral(name="Eothina"),
			EnumerationLiteral(name="Heirmologion"),
			EnumerationLiteral(name="Katavasias"),
			EnumerationLiteral(name="Psalter"),
			EnumerationLiteral(name="Lectionary"),
			EnumerationLiteral(name="Other")
    }
)

Seasons: Enumeration = Enumeration(
    name="Seasons",
    literals={
            EnumerationLiteral(name="Triodion"),
			EnumerationLiteral(name="Pentecostarion"),
			EnumerationLiteral(name="Nativity_Fast"),
			EnumerationLiteral(name="Apostles_Fast"),
			EnumerationLiteral(name="Dormition_Fast")
    }
)

DayOfMonthTypes: Enumeration = Enumeration(
    name="DayOfMonthTypes",
    literals={
            EnumerationLiteral(name="D01"),
			EnumerationLiteral(name="D02"),
			EnumerationLiteral(name="D22"),
			EnumerationLiteral(name="D23"),
			EnumerationLiteral(name="D24"),
			EnumerationLiteral(name="D25"),
			EnumerationLiteral(name="D26"),
			EnumerationLiteral(name="D27"),
			EnumerationLiteral(name="D28"),
			EnumerationLiteral(name="D29"),
			EnumerationLiteral(name="D30"),
			EnumerationLiteral(name="D31"),
			EnumerationLiteral(name="D03"),
			EnumerationLiteral(name="D04"),
			EnumerationLiteral(name="D05"),
			EnumerationLiteral(name="D06"),
			EnumerationLiteral(name="D07"),
			EnumerationLiteral(name="D08"),
			EnumerationLiteral(name="D09"),
			EnumerationLiteral(name="D10"),
			EnumerationLiteral(name="D11"),
			EnumerationLiteral(name="D12"),
			EnumerationLiteral(name="D13"),
			EnumerationLiteral(name="D14"),
			EnumerationLiteral(name="D15"),
			EnumerationLiteral(name="D16"),
			EnumerationLiteral(name="D17"),
			EnumerationLiteral(name="D18"),
			EnumerationLiteral(name="D19"),
			EnumerationLiteral(name="D20"),
			EnumerationLiteral(name="D21")
    }
)

TemplateStatuses: Enumeration = Enumeration(
    name="TemplateStatuses",
    literals={
            EnumerationLiteral(name="NA"),
			EnumerationLiteral(name="Draft"),
			EnumerationLiteral(name="Review"),
			EnumerationLiteral(name="Final")
    }
)

Null: Enumeration = Enumeration(
    name="Null",
    literals={
            EnumerationLiteral(name="null")
    }
)

ModeTypes: Enumeration = Enumeration(
    name="ModeTypes",
    literals={
            EnumerationLiteral(name="M1"),
			EnumerationLiteral(name="M2"),
			EnumerationLiteral(name="M3"),
			EnumerationLiteral(name="M4"),
			EnumerationLiteral(name="M5"),
			EnumerationLiteral(name="M6"),
			EnumerationLiteral(name="M7"),
			EnumerationLiteral(name="M8")
    }
)

DowTypes: Enumeration = Enumeration(
    name="DowTypes",
    literals={
            EnumerationLiteral(name="D3"),
			EnumerationLiteral(name="D4"),
			EnumerationLiteral(name="D5"),
			EnumerationLiteral(name="D6"),
			EnumerationLiteral(name="D7"),
			EnumerationLiteral(name="D1"),
			EnumerationLiteral(name="D2")
    }
)

PeriodType: Enumeration = Enumeration(
    name="PeriodType",
    literals={
            EnumerationLiteral(name="pascha"),
			EnumerationLiteral(name="pentecostarion"),
			EnumerationLiteral(name="triodion")
    }
)

DayOfWeek: Enumeration = Enumeration(
    name="DayOfWeek",
    literals={
            EnumerationLiteral(name="Sunday"),
			EnumerationLiteral(name="Monday"),
			EnumerationLiteral(name="Tuesday"),
			EnumerationLiteral(name="Wednesday"),
			EnumerationLiteral(name="Thursday"),
			EnumerationLiteral(name="Friday"),
			EnumerationLiteral(name="Saturday")
    }
)

MonthName: Enumeration = Enumeration(
    name="MonthName",
    literals={
            EnumerationLiteral(name="Jan"),
			EnumerationLiteral(name="Feb"),
			EnumerationLiteral(name="Mar"),
			EnumerationLiteral(name="Apr"),
			EnumerationLiteral(name="May"),
			EnumerationLiteral(name="Jun"),
			EnumerationLiteral(name="Jul"),
			EnumerationLiteral(name="Aug"),
			EnumerationLiteral(name="Sep"),
			EnumerationLiteral(name="Oct"),
			EnumerationLiteral(name="Nov"),
			EnumerationLiteral(name="Dec")
    }
)

# Classes
atem_Head = Class(name="atem::Head")
atem_Preface = Class(name="atem::Preface")
atem_AbstractComponent = Class(name="atem::AbstractComponent")
atem_HeadComponent = Class(name="atem::HeadComponent")
atem_TemplateTitle = Class(name="atem::TemplateTitle")
HeadComponent = Class(name="HeadComponent")
atem_HeaderFooterFragment = Class(name="atem::HeaderFooterFragment")
atem_PageKeepWithNext = Class(name="atem::PageKeepWithNext")
atem_AtemModel = Class(name="atem::AtemModel")
atem_TemplateStatus = Class(name="atem::TemplateStatus")
atem_Import = Class(name="atem::Import")
atem_Driver = Class(name="atem::Driver")
atem_HeaderFooterColumnCenter = Class(name="atem::HeaderFooterColumnCenter")
atem_HeaderFooterColumnRight = Class(name="atem::HeaderFooterColumnRight")
atem_HeaderFooterText = Class(name="atem::HeaderFooterText")
HeaderFooterFragment = Class(name="HeaderFooterFragment")
atem_HeaderFooterDate = Class(name="atem::HeaderFooterDate")
atem_HeaderFooterPageNumber = Class(name="atem::HeaderFooterPageNumber")
atem_HeaderFooterLookup = Class(name="atem::HeaderFooterLookup")
atem_ElementType = Class(name="atem::ElementType")
atem_HeaderFooterTitle = Class(name="atem::HeaderFooterTitle")
atem_HeaderFooterCommemoration = Class(name="atem::HeaderFooterCommemoration")
atem_Commemoration = Class(name="atem::Commemoration")
atem_PageHeaderEven = Class(name="atem::PageHeaderEven")
atem_HeaderFooterColumn = Class(name="atem::HeaderFooterColumn")
atem_PageHeaderOdd = Class(name="atem::PageHeaderOdd")
atem_PageFooterEven = Class(name="atem::PageFooterEven")
atem_PageFooterOdd = Class(name="atem::PageFooterOdd")
atem_HeaderFooterColumnLeft = Class(name="atem::HeaderFooterColumnLeft")
HeaderFooterColumn = Class(name="HeaderFooterColumn")
atem_Lookup = Class(name="atem::Lookup")
atem_LDP = Class(name="atem::LDP")
atem_LdpType = Class(name="atem::LdpType")
atem_TaggedText = Class(name="atem::TaggedText")
atem_Info = Class(name="atem::Info")
atem_InfoElementType = Class(name="atem::InfoElementType")
atem_VersionSwitch = Class(name="atem::VersionSwitch")
AbstractComponent = Class(name="AbstractComponent")
InfoElementType = Class(name="InfoElementType")
PrefaceElementType = Class(name="PrefaceElementType")
atem_ResourceText = Class(name="atem::ResourceText")
ElementType = Class(name="ElementType")
atem_Definition = Class(name="atem::Definition")
atem_GenDate = Class(name="atem::GenDate")
atem_GenYear = Class(name="atem::GenYear")
atem_MCD = Class(name="atem::MCD")
atem_MOW = Class(name="atem::MOW")
atem_NOP = Class(name="atem::NOP")
atem_DOM = Class(name="atem::DOM")
atem_DOP = Class(name="atem::DOP")
atem_DOWN = Class(name="atem::DOWN")
atem_DOWT = Class(name="atem::DOWT")
atem_Date = Class(name="atem::Date")
SectionElementType = Class(name="SectionElementType")
atem_PrefaceElementType = Class(name="atem::PrefaceElementType")
atem_Section = Class(name="atem::Section")
atem_SectionElementType = Class(name="atem::SectionElementType")
atem_All = Class(name="atem::All")
LdpType = Class(name="LdpType")
atem_PrefaceFragment = Class(name="atem::PrefaceFragment")
atem_SectionFragment = Class(name="atem::SectionFragment")
atem_Break = Class(name="atem::Break")
atem_PageNumber = Class(name="atem::PageNumber")
atem_PassThroughHtml = Class(name="atem::PassThroughHtml")
atem_PassThroughPdf = Class(name="atem::PassThroughPdf")
atem_Title = Class(name="atem::Title")
atem_EOW = Class(name="atem::EOW")
atem_SAEC = Class(name="atem::SAEC")
atem_SOL = Class(name="atem::SOL")
atem_DOL = Class(name="atem::DOL")
atem_WOLC = Class(name="atem::WOLC")
atem_WDOLC = Class(name="atem::WDOLC")
atem_SBT = Class(name="atem::SBT")
atem_TemplateFragment = Class(name="atem::TemplateFragment")
atem_Block = Class(name="atem::Block")
atem_Hymn = Class(name="atem::Hymn")
atem_Media = Class(name="atem::Media")
atem_Verse = Class(name="atem::Verse")
atem_SubTitle = Class(name="atem::SubTitle")
atem_Paragraph = Class(name="atem::Paragraph")
atem_Heading2 = Class(name="atem::Heading2")
atem_Heading3 = Class(name="atem::Heading3")
atem_Aid = Class(name="atem::Aid")
atem_Version = Class(name="atem::Version")
atem_LitBook = Class(name="atem::LitBook")
atem_SetLocale = Class(name="atem::SetLocale")
atem_Actor = Class(name="atem::Actor")
atem_Rubric = Class(name="atem::Rubric")
atem_Dialog = Class(name="atem::Dialog")
atem_Reading = Class(name="atem::Reading")
atem_Heading1 = Class(name="atem::Heading1")
atem_RestoreLocale = Class(name="atem::RestoreLocale")
atem_WhenDate = Class(name="atem::WhenDate")
atem_WhenDateCase = Class(name="atem::WhenDateCase")
atem_WhenOther = Class(name="atem::WhenOther")
atem_AbstractDateCase = Class(name="atem::AbstractDateCase")
atem_DayNameRange = Class(name="atem::DayNameRange")
AbstractDayNameCase = Class(name="AbstractDayNameCase")
atem_DayNameSet = Class(name="atem::DayNameSet")
atem_WhenPentecostarionDay = Class(name="atem::WhenPentecostarionDay")
atem_WhenPeriodCase = Class(name="atem::WhenPeriodCase")
atem_WhenTriodionDay = Class(name="atem::WhenTriodionDay")
atem_DateRange = Class(name="atem::DateRange")
AbstractDateCase = Class(name="AbstractDateCase")
atem_DateSet = Class(name="atem::DateSet")
atem_WhenDayName = Class(name="atem::WhenDayName")
atem_WhenDayNameCase = Class(name="atem::WhenDayNameCase")
atem_AbstractDayNameCase = Class(name="atem::AbstractDayNameCase")
atem_WhenLukanCycleDay = Class(name="atem::WhenLukanCycleDay")
atem_WhenPascha = Class(name="atem::WhenPascha")
atem_AbstractDayCase = Class(name="atem::AbstractDayCase")
atem_WhenMovableCycleDay = Class(name="atem::WhenMovableCycleDay")
atem_WhenSundayAfterElevationOfCrossDay = Class(name="atem::WhenSundayAfterElevationOfCrossDay")
atem_WhenSundaysBeforeTriodion = Class(name="atem::WhenSundaysBeforeTriodion")
atem_SundaysBeforeTriodionCase = Class(name="atem::SundaysBeforeTriodionCase")
atem_DayRange = Class(name="atem::DayRange")
AbstractDayCase = Class(name="AbstractDayCase")
atem_DaySet = Class(name="atem::DaySet")
atem_WhenModeOfWeek = Class(name="atem::WhenModeOfWeek")
atem_WhenModeOfWeekCase = Class(name="atem::WhenModeOfWeekCase")
atem_ModeOfWeekSet = Class(name="atem::ModeOfWeekSet")
atem_WhenExists = Class(name="atem::WhenExists")
atem_WhenExistsCase = Class(name="atem::WhenExistsCase")

# atem_Head class attributes and methods

# atem_Preface class attributes and methods
atem_Preface_name: Property = Property(name="name", type=StringType)
atem_Preface.attributes={atem_Preface_name}

# atem_AbstractComponent class attributes and methods

# atem_HeadComponent class attributes and methods

# atem_TemplateTitle class attributes and methods

# HeadComponent class attributes and methods

# atem_HeaderFooterFragment class attributes and methods

# atem_PageKeepWithNext class attributes and methods
atem_PageKeepWithNext_dsl_PageKeepWithNext_value: Property = Property(name="dsl_PageKeepWithNext_value", type=StringType)
atem_PageKeepWithNext.attributes={atem_PageKeepWithNext_dsl_PageKeepWithNext_value}

# atem_AtemModel class attributes and methods
atem_AtemModel_name: Property = Property(name="name", type=StringType)
atem_AtemModel.attributes={atem_AtemModel_name}

# atem_TemplateStatus class attributes and methods
atem_TemplateStatus_dsl_TemplateStatus: Property = Property(name="dsl_TemplateStatus", type=StringType)
atem_TemplateStatus.attributes={atem_TemplateStatus_dsl_TemplateStatus}

# atem_Import class attributes and methods
atem_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
atem_Import.attributes={atem_Import_importedNamespace}

# atem_Driver class attributes and methods
atem_Driver_dsl_Driver_RegEx: Property = Property(name="dsl_Driver_RegEx", type=StringType)
atem_Driver_dsl_Driver_Status: Property = Property(name="dsl_Driver_Status", type=StringType)
atem_Driver.attributes={atem_Driver_dsl_Driver_RegEx, atem_Driver_dsl_Driver_Status}

# atem_HeaderFooterColumnCenter class attributes and methods

# atem_HeaderFooterColumnRight class attributes and methods

# atem_HeaderFooterText class attributes and methods
atem_HeaderFooterText_dsl_HeaderFooterText: Property = Property(name="dsl_HeaderFooterText", type=StringType)
atem_HeaderFooterText.attributes={atem_HeaderFooterText_dsl_HeaderFooterText}

# HeaderFooterFragment class attributes and methods

# atem_HeaderFooterDate class attributes and methods
atem_HeaderFooterDate_dsl_HeaderFooterDate: Property = Property(name="dsl_HeaderFooterDate", type=BooleanType)
atem_HeaderFooterDate_dsl_HeaderFooterDate_Language: Property = Property(name="dsl_HeaderFooterDate_Language", type=StringType)
atem_HeaderFooterDate.attributes={atem_HeaderFooterDate_dsl_HeaderFooterDate, atem_HeaderFooterDate_dsl_HeaderFooterDate_Language}

# atem_HeaderFooterPageNumber class attributes and methods
atem_HeaderFooterPageNumber_dsl_HeaderFooterPageNumber: Property = Property(name="dsl_HeaderFooterPageNumber", type=BooleanType)
atem_HeaderFooterPageNumber.attributes={atem_HeaderFooterPageNumber_dsl_HeaderFooterPageNumber}

# atem_HeaderFooterLookup class attributes and methods
atem_HeaderFooterLookup_dsl_HeaderFooterLookup_Language: Property = Property(name="dsl_HeaderFooterLookup_Language", type=StringType)
atem_HeaderFooterLookup.attributes={atem_HeaderFooterLookup_dsl_HeaderFooterLookup_Language}

# atem_ElementType class attributes and methods

# atem_HeaderFooterTitle class attributes and methods
atem_HeaderFooterTitle_dsl_HeaderFooterTitle: Property = Property(name="dsl_HeaderFooterTitle", type=BooleanType)
atem_HeaderFooterTitle.attributes={atem_HeaderFooterTitle_dsl_HeaderFooterTitle}

# atem_HeaderFooterCommemoration class attributes and methods
atem_HeaderFooterCommemoration_dsl_HeaderFooterCommemoration: Property = Property(name="dsl_HeaderFooterCommemoration", type=BooleanType)
atem_HeaderFooterCommemoration.attributes={atem_HeaderFooterCommemoration_dsl_HeaderFooterCommemoration}

# atem_Commemoration class attributes and methods

# atem_PageHeaderEven class attributes and methods

# atem_HeaderFooterColumn class attributes and methods

# atem_PageHeaderOdd class attributes and methods

# atem_PageFooterEven class attributes and methods

# atem_PageFooterOdd class attributes and methods

# atem_HeaderFooterColumnLeft class attributes and methods

# HeaderFooterColumn class attributes and methods

# atem_Lookup class attributes and methods
atem_Lookup_dsl_Lookup_Media_Off: Property = Property(name="dsl_Lookup_Media_Off", type=BooleanType)
atem_Lookup_dsl_Lookup_Override_Mode_Set: Property = Property(name="dsl_Lookup_Override_Mode_Set", type=BooleanType)
atem_Lookup_dsl_Lookup_OverrideMode: Property = Property(name="dsl_Lookup_OverrideMode", type=StringType)
atem_Lookup_dsl_Lookup_Override__Day_Set: Property = Property(name="dsl_Lookup_Override__Day_Set", type=BooleanType)
atem_Lookup_dsl_Lookup_OverrideDay: Property = Property(name="dsl_Lookup_OverrideDay", type=StringType)
atem_Lookup.attributes={atem_Lookup_dsl_Lookup_OverrideDay, atem_Lookup_dsl_Lookup_Override_Mode_Set, atem_Lookup_dsl_Lookup_OverrideMode, atem_Lookup_dsl_Lookup_Override__Day_Set, atem_Lookup_dsl_Lookup_Media_Off}

# atem_LDP class attributes and methods

# atem_LdpType class attributes and methods

# atem_TaggedText class attributes and methods

# atem_Info class attributes and methods
atem_Info_name: Property = Property(name="name", type=StringType)
atem_Info.attributes={atem_Info_name}

# atem_InfoElementType class attributes and methods

# atem_VersionSwitch class attributes and methods
atem_VersionSwitch_dsl_VersionSwitch_flag: Property = Property(name="dsl_VersionSwitch_flag", type=StringType)
atem_VersionSwitch.attributes={atem_VersionSwitch_dsl_VersionSwitch_flag}

# AbstractComponent class attributes and methods

# InfoElementType class attributes and methods

# PrefaceElementType class attributes and methods

# atem_ResourceText class attributes and methods
atem_ResourceText_dsl_ResourceText_Media_Off: Property = Property(name="dsl_ResourceText_Media_Off", type=BooleanType)
atem_ResourceText.attributes={atem_ResourceText_dsl_ResourceText_Media_Off}

# ElementType class attributes and methods

# atem_Definition class attributes and methods

# atem_GenDate class attributes and methods
atem_GenDate_dsl_Display_Date: Property = Property(name="dsl_Display_Date", type=BooleanType)
atem_GenDate.attributes={atem_GenDate_dsl_Display_Date}

# atem_GenYear class attributes and methods
atem_GenYear_dsl_Display_Year: Property = Property(name="dsl_Display_Year", type=BooleanType)
atem_GenYear.attributes={atem_GenYear_dsl_Display_Year}

# atem_MCD class attributes and methods
atem_MCD_dsl_MCD_value: Property = Property(name="dsl_MCD_value", type=BooleanType)
atem_MCD.attributes={atem_MCD_dsl_MCD_value}

# atem_MOW class attributes and methods
atem_MOW_dsl_Display_Mode: Property = Property(name="dsl_Display_Mode", type=BooleanType)
atem_MOW.attributes={atem_MOW_dsl_Display_Mode}

# atem_NOP class attributes and methods
atem_NOP_dsl_Display_Mode: Property = Property(name="dsl_Display_Mode", type=BooleanType)
atem_NOP.attributes={atem_NOP_dsl_Display_Mode}

# atem_DOM class attributes and methods
atem_DOM_dsl_Display_Mode: Property = Property(name="dsl_Display_Mode", type=BooleanType)
atem_DOM.attributes={atem_DOM_dsl_Display_Mode}

# atem_DOP class attributes and methods
atem_DOP_dsl_Display_Mode: Property = Property(name="dsl_Display_Mode", type=BooleanType)
atem_DOP.attributes={atem_DOP_dsl_Display_Mode}

# atem_DOWN class attributes and methods
atem_DOWN_dsl_Display_Mode: Property = Property(name="dsl_Display_Mode", type=BooleanType)
atem_DOWN.attributes={atem_DOWN_dsl_Display_Mode}

# atem_DOWT class attributes and methods
atem_DOWT_dsl_Display_Mode: Property = Property(name="dsl_Display_Mode", type=BooleanType)
atem_DOWT.attributes={atem_DOWT_dsl_Display_Mode}

# atem_Date class attributes and methods
atem_Date_dsl_Date_month: Property = Property(name="dsl_Date_month", type=IntegerType)
atem_Date_dsl_Date_day: Property = Property(name="dsl_Date_day", type=IntegerType)
atem_Date_dsl_Date_year: Property = Property(name="dsl_Date_year", type=IntegerType)
atem_Date.attributes={atem_Date_dsl_Date_month, atem_Date_dsl_Date_year, atem_Date_dsl_Date_day}

# SectionElementType class attributes and methods

# atem_PrefaceElementType class attributes and methods

# atem_Section class attributes and methods
atem_Section_name: Property = Property(name="name", type=StringType)
atem_Section.attributes={atem_Section_name}

# atem_SectionElementType class attributes and methods

# atem_All class attributes and methods
atem_All_dsl_Display_LiturgicalDayProperties: Property = Property(name="dsl_Display_LiturgicalDayProperties", type=BooleanType)
atem_All.attributes={atem_All_dsl_Display_LiturgicalDayProperties}

# LdpType class attributes and methods

# atem_PrefaceFragment class attributes and methods

# atem_SectionFragment class attributes and methods

# atem_Break class attributes and methods
atem_Break_dsl_break_type: Property = Property(name="dsl_break_type", type=StringType)
atem_Break.attributes={atem_Break_dsl_break_type}

# atem_PageNumber class attributes and methods
atem_PageNumber_dsl_PageNumber_value: Property = Property(name="dsl_PageNumber_value", type=IntegerType)
atem_PageNumber.attributes={atem_PageNumber_dsl_PageNumber_value}

# atem_PassThroughHtml class attributes and methods
atem_PassThroughHtml_dsl_Passthrough_html_text: Property = Property(name="dsl_Passthrough_html_text", type=StringType)
atem_PassThroughHtml.attributes={atem_PassThroughHtml_dsl_Passthrough_html_text}

# atem_PassThroughPdf class attributes and methods
atem_PassThroughPdf_dsl_Passthrough_pdf_text: Property = Property(name="dsl_Passthrough_pdf_text", type=StringType)
atem_PassThroughPdf.attributes={atem_PassThroughPdf_dsl_Passthrough_pdf_text}

# atem_Title class attributes and methods

# atem_EOW class attributes and methods
atem_EOW_dsl_Display_Eothinon: Property = Property(name="dsl_Display_Eothinon", type=BooleanType)
atem_EOW.attributes={atem_EOW_dsl_Display_Eothinon}

# atem_SAEC class attributes and methods
atem_SAEC_dsl_Display_SundayAfterElevationCross: Property = Property(name="dsl_Display_SundayAfterElevationCross", type=BooleanType)
atem_SAEC.attributes={atem_SAEC_dsl_Display_SundayAfterElevationCross}

# atem_SOL class attributes and methods
atem_SOL_dsl_Display_StartLukan: Property = Property(name="dsl_Display_StartLukan", type=BooleanType)
atem_SOL.attributes={atem_SOL_dsl_Display_StartLukan}

# atem_DOL class attributes and methods
atem_DOL_dsl_Display_DayLukan: Property = Property(name="dsl_Display_DayLukan", type=BooleanType)
atem_DOL.attributes={atem_DOL_dsl_Display_DayLukan}

# atem_WOLC class attributes and methods
atem_WOLC_dsl_Display_DayLukan: Property = Property(name="dsl_Display_DayLukan", type=BooleanType)
atem_WOLC.attributes={atem_WOLC_dsl_Display_DayLukan}

# atem_WDOLC class attributes and methods
atem_WDOLC_dsl_Display_DayLukan: Property = Property(name="dsl_Display_DayLukan", type=BooleanType)
atem_WDOLC.attributes={atem_WDOLC_dsl_Display_DayLukan}

# atem_SBT class attributes and methods
atem_SBT_dsl_Display_SundaysBeforeTriodion: Property = Property(name="dsl_Display_SundaysBeforeTriodion", type=BooleanType)
atem_SBT.attributes={atem_SBT_dsl_Display_SundaysBeforeTriodion}

# atem_TemplateFragment class attributes and methods

# atem_Block class attributes and methods

# atem_Hymn class attributes and methods

# atem_Media class attributes and methods

# atem_Verse class attributes and methods

# atem_SubTitle class attributes and methods

# atem_Paragraph class attributes and methods

# atem_Heading2 class attributes and methods

# atem_Heading3 class attributes and methods

# atem_Aid class attributes and methods
atem_Aid_name: Property = Property(name="name", type=StringType)
atem_Aid.attributes={atem_Aid_name}

# atem_Version class attributes and methods
atem_Version_name: Property = Property(name="name", type=StringType)
atem_Version.attributes={atem_Version_name}

# atem_LitBook class attributes and methods
atem_LitBook_name: Property = Property(name="name", type=StringType)
atem_LitBook.attributes={atem_LitBook_name}

# atem_SetLocale class attributes and methods
atem_SetLocale_dsl_SetLocale_V1: Property = Property(name="dsl_SetLocale_V1", type=StringType)
atem_SetLocale_dsl_SetLocale_V2: Property = Property(name="dsl_SetLocale_V2", type=StringType)
atem_SetLocale.attributes={atem_SetLocale_dsl_SetLocale_V2, atem_SetLocale_dsl_SetLocale_V1}

# atem_Actor class attributes and methods

# atem_Rubric class attributes and methods

# atem_Dialog class attributes and methods

# atem_Reading class attributes and methods

# atem_Heading1 class attributes and methods

# atem_RestoreLocale class attributes and methods
atem_RestoreLocale_dsl_RestoreLocale: Property = Property(name="dsl_RestoreLocale", type=BooleanType)
atem_RestoreLocale.attributes={atem_RestoreLocale_dsl_RestoreLocale}

# atem_WhenDate class attributes and methods

# atem_WhenDateCase class attributes and methods
atem_WhenDateCase_dsl_WhenDate_Case_Month: Property = Property(name="dsl_WhenDate_Case_Month", type=StringType)
atem_WhenDateCase.attributes={atem_WhenDateCase_dsl_WhenDate_Case_Month}

# atem_WhenOther class attributes and methods

# atem_AbstractDateCase class attributes and methods

# atem_DayNameRange class attributes and methods
atem_DayNameRange_dsl_DayNameRange_from: Property = Property(name="dsl_DayNameRange_from", type=StringType)
atem_DayNameRange_dsl_DayNameRange_To: Property = Property(name="dsl_DayNameRange_To", type=StringType)
atem_DayNameRange.attributes={atem_DayNameRange_dsl_DayNameRange_from, atem_DayNameRange_dsl_DayNameRange_To}

# AbstractDayNameCase class attributes and methods

# atem_DayNameSet class attributes and methods
atem_DayNameSet_dslDayNameSet_Values: Property = Property(name="dslDayNameSet_Values", type=StringType)
atem_DayNameSet.attributes={atem_DayNameSet_dslDayNameSet_Values}

# atem_WhenPentecostarionDay class attributes and methods

# atem_WhenPeriodCase class attributes and methods

# atem_WhenTriodionDay class attributes and methods

# atem_DateRange class attributes and methods
atem_DateRange_dsl_DateRange_from: Property = Property(name="dsl_DateRange_from", type=IntegerType)
atem_DateRange_dsl_DateRange_To: Property = Property(name="dsl_DateRange_To", type=IntegerType)
atem_DateRange.attributes={atem_DateRange_dsl_DateRange_To, atem_DateRange_dsl_DateRange_from}

# AbstractDateCase class attributes and methods

# atem_DateSet class attributes and methods
atem_DateSet_dslDateSet_Values: Property = Property(name="dslDateSet_Values", type=IntegerType)
atem_DateSet.attributes={atem_DateSet_dslDateSet_Values}

# atem_WhenDayName class attributes and methods

# atem_WhenDayNameCase class attributes and methods

# atem_AbstractDayNameCase class attributes and methods

# atem_WhenLukanCycleDay class attributes and methods

# atem_WhenPascha class attributes and methods

# atem_AbstractDayCase class attributes and methods

# atem_WhenMovableCycleDay class attributes and methods

# atem_WhenSundayAfterElevationOfCrossDay class attributes and methods

# atem_WhenSundaysBeforeTriodion class attributes and methods

# atem_SundaysBeforeTriodionCase class attributes and methods
atem_SundaysBeforeTriodionCase_dsl_SundaysBeforeTriodionCase_Days: Property = Property(name="dsl_SundaysBeforeTriodionCase_Days", type=IntegerType)
atem_SundaysBeforeTriodionCase.attributes={atem_SundaysBeforeTriodionCase_dsl_SundaysBeforeTriodionCase_Days}

# atem_DayRange class attributes and methods
atem_DayRange_dsl_DayRange_from: Property = Property(name="dsl_DayRange_from", type=IntegerType)
atem_DayRange_dsl_Range_To: Property = Property(name="dsl_Range_To", type=IntegerType)
atem_DayRange.attributes={atem_DayRange_dsl_Range_To, atem_DayRange_dsl_DayRange_from}

# AbstractDayCase class attributes and methods

# atem_DaySet class attributes and methods
atem_DaySet_dslSetValue_Days: Property = Property(name="dslSetValue_Days", type=IntegerType)
atem_DaySet.attributes={atem_DaySet_dslSetValue_Days}

# atem_WhenModeOfWeek class attributes and methods

# atem_WhenModeOfWeekCase class attributes and methods

# atem_ModeOfWeekSet class attributes and methods
atem_ModeOfWeekSet_dsl_ModeOfWeekSet_MOWs: Property = Property(name="dsl_ModeOfWeekSet_MOWs", type=StringType)
atem_ModeOfWeekSet.attributes={atem_ModeOfWeekSet_dsl_ModeOfWeekSet_MOWs}

# atem_WhenExists class attributes and methods

# atem_WhenExistsCase class attributes and methods

# Relationships
dsl_Template_Driver3: BinaryAssociation = BinaryAssociation(
    name="dsl_Template_Driver3",
    ends={
        Property(name="atem_AtemModel4", type=atem_Driver, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="atem_Driver", type=atem_AtemModel, multiplicity=Multiplicity(1, 1))
    }
)
dsl_Template_head5: BinaryAssociation = BinaryAssociation(
    name="dsl_Template_head5",
    ends={
        Property(name="atem_Head", type=atem_AtemModel, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_AtemModel6", type=atem_Head, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_Template_preface7: BinaryAssociation = BinaryAssociation(
    name="dsl_Template_preface7",
    ends={
        Property(name="atem_Preface", type=atem_AtemModel, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_AtemModel8", type=atem_Preface, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_Template_components9: BinaryAssociation = BinaryAssociation(
    name="dsl_Template_components9",
    ends={
        Property(name="atem_AbstractComponent", type=atem_AtemModel, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_AtemModel10", type=atem_AbstractComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Head_components11: BinaryAssociation = BinaryAssociation(
    name="dsl_Head_components11",
    ends={
        Property(name="atem_HeadComponent", type=atem_Head, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Head12", type=atem_HeadComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_TemplateTitle_Elements13: BinaryAssociation = BinaryAssociation(
    name="dsl_TemplateTitle_Elements13",
    ends={
        Property(name="atem_HeaderFooterFragment", type=atem_TemplateTitle, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_TemplateTitle", type=atem_HeaderFooterFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Template_Status0: BinaryAssociation = BinaryAssociation(
    name="dsl_Template_Status0",
    ends={
        Property(name="atem_TemplateStatus", type=atem_AtemModel, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_AtemModel", type=atem_TemplateStatus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="atem_Import", type=atem_AtemModel, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_AtemModel2", type=atem_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_HeaderFooterLookup_Elements24: BinaryAssociation = BinaryAssociation(
    name="dsl_HeaderFooterLookup_Elements24",
    ends={
        Property(name="atem_ElementType", type=atem_HeaderFooterLookup, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_HeaderFooterLookup", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_PageHeader_columns14: BinaryAssociation = BinaryAssociation(
    name="dsl_PageHeader_columns14",
    ends={
        Property(name="atem_HeaderFooterColumn", type=atem_PageHeaderEven, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_PageHeaderEven", type=atem_HeaderFooterColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_PageHeader_columns15: BinaryAssociation = BinaryAssociation(
    name="dsl_PageHeader_columns15",
    ends={
        Property(name="atem_HeaderFooterColumn16", type=atem_PageHeaderOdd, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_PageHeaderOdd", type=atem_HeaderFooterColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_PageHeader_columns17: BinaryAssociation = BinaryAssociation(
    name="dsl_PageHeader_columns17",
    ends={
        Property(name="atem_HeaderFooterColumn18", type=atem_PageFooterEven, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_PageFooterEven", type=atem_HeaderFooterColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_PageHeader_columns19: BinaryAssociation = BinaryAssociation(
    name="dsl_PageHeader_columns19",
    ends={
        Property(name="atem_HeaderFooterColumn20", type=atem_PageFooterOdd, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_PageFooterOdd", type=atem_HeaderFooterColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_HeaderFooterColumn_fragments21: BinaryAssociation = BinaryAssociation(
    name="dsl_HeaderFooterColumn_fragments21",
    ends={
        Property(name="atem_HeaderFooterFragment23", type=atem_HeaderFooterColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_HeaderFooterColumn22", type=atem_HeaderFooterFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_ResourceTextRef28: BinaryAssociation = BinaryAssociation(
    name="dsl_ResourceTextRef28",
    ends={
        Property(name="atem_Definition29", type=atem_Lookup, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Lookup", type=atem_Definition, multiplicity=Multiplicity(0, 1))
    }
)
dsl_LDP30: BinaryAssociation = BinaryAssociation(
    name="dsl_LDP30",
    ends={
        Property(name="atem_LdpType", type=atem_LDP, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_LDP", type=atem_LdpType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_TaggedText_tag31: BinaryAssociation = BinaryAssociation(
    name="dsl_TaggedText_tag31",
    ends={
        Property(name="atem_Definition32", type=atem_TaggedText, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_TaggedText", type=atem_Definition, multiplicity=Multiplicity(0, 1))
    }
)
dsl_TaggedText33: BinaryAssociation = BinaryAssociation(
    name="dsl_TaggedText33",
    ends={
        Property(name="atem_ElementType35", type=atem_TaggedText, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_TaggedText34", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Info_Elements36: BinaryAssociation = BinaryAssociation(
    name="dsl_Info_Elements36",
    ends={
        Property(name="atem_InfoElementType", type=atem_Info, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Info", type=atem_InfoElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Commemoration_Elements25: BinaryAssociation = BinaryAssociation(
    name="dsl_Commemoration_Elements25",
    ends={
        Property(name="atem_HeaderFooterFragment26", type=atem_Commemoration, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Commemoration", type=atem_HeaderFooterFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_ResourceTextRef27: BinaryAssociation = BinaryAssociation(
    name="dsl_ResourceTextRef27",
    ends={
        Property(name="atem_Definition", type=atem_ResourceText, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_ResourceText", type=atem_Definition, multiplicity=Multiplicity(0, 1))
    }
)
dsl_Preface_Elements37: BinaryAssociation = BinaryAssociation(
    name="dsl_Preface_Elements37",
    ends={
        Property(name="atem_PrefaceElementType", type=atem_Preface, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Preface38", type=atem_PrefaceElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Section_Role39: BinaryAssociation = BinaryAssociation(
    name="dsl_Section_Role39",
    ends={
        Property(name="atem_Definition40", type=atem_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Section", type=atem_Definition, multiplicity=Multiplicity(0, 1))
    }
)
dsl_Section_Elements41: BinaryAssociation = BinaryAssociation(
    name="dsl_Section_Elements41",
    ends={
        Property(name="atem_SectionElementType", type=atem_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Section42", type=atem_SectionElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name45: BinaryAssociation = BinaryAssociation(
    name="name45",
    ends={
        Property(name="atem_Preface46", type=atem_PrefaceFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_PrefaceFragment", type=atem_Preface, multiplicity=Multiplicity(0, 1))
    }
)
name47: BinaryAssociation = BinaryAssociation(
    name="name47",
    ends={
        Property(name="atem_Section48", type=atem_SectionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_SectionFragment", type=atem_Section, multiplicity=Multiplicity(0, 1))
    }
)
name43: BinaryAssociation = BinaryAssociation(
    name="name43",
    ends={
        Property(name="atem_AtemModel44", type=atem_TemplateFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_TemplateFragment", type=atem_AtemModel, multiplicity=Multiplicity(0, 1))
    }
)
dsl_Block_Role64: BinaryAssociation = BinaryAssociation(
    name="dsl_Block_Role64",
    ends={
        Property(name="atem_Definition65", type=atem_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Block", type=atem_Definition, multiplicity=Multiplicity(0, 1))
    }
)
dsl_Elements66: BinaryAssociation = BinaryAssociation(
    name="dsl_Elements66",
    ends={
        Property(name="atem_ElementType68", type=atem_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Block67", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Elements69: BinaryAssociation = BinaryAssociation(
    name="dsl_Elements69",
    ends={
        Property(name="atem_ElementType70", type=atem_Hymn, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Hymn", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Elements71: BinaryAssociation = BinaryAssociation(
    name="dsl_Elements71",
    ends={
        Property(name="atem_ElementType72", type=atem_Media, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Media", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Elements73: BinaryAssociation = BinaryAssociation(
    name="dsl_Elements73",
    ends={
        Property(name="atem_ElementType74", type=atem_Verse, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Verse", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Title_Role49: BinaryAssociation = BinaryAssociation(
    name="dsl_Title_Role49",
    ends={
        Property(name="atem_Definition50", type=atem_Title, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Title", type=atem_Definition, multiplicity=Multiplicity(0, 1))
    }
)
dsl_Elements51: BinaryAssociation = BinaryAssociation(
    name="dsl_Elements51",
    ends={
        Property(name="atem_ElementType53", type=atem_Title, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Title52", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_SubTitle_Role54: BinaryAssociation = BinaryAssociation(
    name="dsl_SubTitle_Role54",
    ends={
        Property(name="atem_Definition55", type=atem_SubTitle, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_SubTitle", type=atem_Definition, multiplicity=Multiplicity(0, 1))
    }
)
dsl_Elements56: BinaryAssociation = BinaryAssociation(
    name="dsl_Elements56",
    ends={
        Property(name="atem_ElementType58", type=atem_SubTitle, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_SubTitle57", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Para_Role59: BinaryAssociation = BinaryAssociation(
    name="dsl_Para_Role59",
    ends={
        Property(name="atem_Definition60", type=atem_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Paragraph", type=atem_Definition, multiplicity=Multiplicity(0, 1))
    }
)
dsl_Elements61: BinaryAssociation = BinaryAssociation(
    name="dsl_Elements61",
    ends={
        Property(name="atem_ElementType63", type=atem_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Paragraph62", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Elements83: BinaryAssociation = BinaryAssociation(
    name="dsl_Elements83",
    ends={
        Property(name="atem_ElementType84", type=atem_Heading1, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Heading1", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Elements85: BinaryAssociation = BinaryAssociation(
    name="dsl_Elements85",
    ends={
        Property(name="atem_ElementType86", type=atem_Heading2, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Heading2", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Elements87: BinaryAssociation = BinaryAssociation(
    name="dsl_Elements87",
    ends={
        Property(name="atem_ElementType88", type=atem_Heading3, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Heading3", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Elements75: BinaryAssociation = BinaryAssociation(
    name="dsl_Elements75",
    ends={
        Property(name="atem_ElementType76", type=atem_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Actor", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Elements77: BinaryAssociation = BinaryAssociation(
    name="dsl_Elements77",
    ends={
        Property(name="atem_ElementType78", type=atem_Rubric, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Rubric", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Elements79: BinaryAssociation = BinaryAssociation(
    name="dsl_Elements79",
    ends={
        Property(name="atem_ElementType80", type=atem_Dialog, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Dialog", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_Elements81: BinaryAssociation = BinaryAssociation(
    name="dsl_Elements81",
    ends={
        Property(name="atem_ElementType82", type=atem_Reading, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_Reading", type=atem_ElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenDate_Cases89: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenDate_Cases89",
    ends={
        Property(name="atem_WhenDateCase", type=atem_WhenDate, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenDate", type=atem_WhenDateCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenDate_Other90: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenDate_Other90",
    ends={
        Property(name="atem_WhenOther", type=atem_WhenDate, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenDate91", type=atem_WhenOther, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_WhenDateCase_Days92: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenDateCase_Days92",
    ends={
        Property(name="atem_AbstractDateCase", type=atem_WhenDateCase, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenDateCase93", type=atem_AbstractDateCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_WhenPentecostarionDay_Cases106: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenPentecostarionDay_Cases106",
    ends={
        Property(name="atem_WhenPeriodCase", type=atem_WhenPentecostarionDay, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenPentecostarionDay", type=atem_WhenPeriodCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenPentecostarionDay_Other107: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenPentecostarionDay_Other107",
    ends={
        Property(name="atem_WhenOther109", type=atem_WhenPentecostarionDay, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenPentecostarionDay108", type=atem_WhenOther, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_WhenDateCase_True_actions94: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenDateCase_True_actions94",
    ends={
        Property(name="atem_AbstractComponent96", type=atem_WhenDateCase, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenDateCase95", type=atem_AbstractComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenDayName_Cases97: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenDayName_Cases97",
    ends={
        Property(name="atem_WhenDayNameCase", type=atem_WhenDayName, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenDayName", type=atem_WhenDayNameCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenDayName_Other98: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenDayName_Other98",
    ends={
        Property(name="atem_WhenOther100", type=atem_WhenDayName, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenDayName99", type=atem_WhenOther, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_WhenDayNameCase_Days101: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenDayNameCase_Days101",
    ends={
        Property(name="atem_AbstractDayNameCase", type=atem_WhenDayNameCase, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenDayNameCase102", type=atem_AbstractDayNameCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_WhenDayNameCase_True_actions103: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenDayNameCase_True_actions103",
    ends={
        Property(name="atem_AbstractComponent105", type=atem_WhenDayNameCase, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenDayNameCase104", type=atem_AbstractComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenLukanCycleDay_Cases125: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenLukanCycleDay_Cases125",
    ends={
        Property(name="atem_WhenPeriodCase126", type=atem_WhenLukanCycleDay, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenLukanCycleDay", type=atem_WhenPeriodCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenLukanCycleDay_Other127: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenLukanCycleDay_Other127",
    ends={
        Property(name="atem_WhenOther129", type=atem_WhenLukanCycleDay, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenLukanCycleDay128", type=atem_WhenOther, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_WhenPascha_true_actions130: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenPascha_true_actions130",
    ends={
        Property(name="atem_AbstractComponent131", type=atem_WhenPascha, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenPascha", type=atem_AbstractComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenPascha_Other_actions132: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenPascha_Other_actions132",
    ends={
        Property(name="atem_AbstractComponent134", type=atem_WhenPascha, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenPascha133", type=atem_AbstractComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenCase_Other_actions135: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenCase_Other_actions135",
    ends={
        Property(name="atem_AbstractComponent137", type=atem_WhenOther, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenOther136", type=atem_AbstractComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenPeriodCase_Days138: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenPeriodCase_Days138",
    ends={
        Property(name="atem_AbstractDayCase", type=atem_WhenPeriodCase, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenPeriodCase139", type=atem_AbstractDayCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_WhenTriodionDay_Cases110: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenTriodionDay_Cases110",
    ends={
        Property(name="atem_WhenPeriodCase111", type=atem_WhenTriodionDay, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenTriodionDay", type=atem_WhenPeriodCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenTriodionDay_Other112: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenTriodionDay_Other112",
    ends={
        Property(name="atem_WhenOther114", type=atem_WhenTriodionDay, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenTriodionDay113", type=atem_WhenOther, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_WhenMovableCycleDay_Cases115: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenMovableCycleDay_Cases115",
    ends={
        Property(name="atem_WhenPeriodCase116", type=atem_WhenMovableCycleDay, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenMovableCycleDay", type=atem_WhenPeriodCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenMovableCycleDay_Other117: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenMovableCycleDay_Other117",
    ends={
        Property(name="atem_WhenOther119", type=atem_WhenMovableCycleDay, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenMovableCycleDay118", type=atem_WhenOther, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_WhenSundayAfterElevationOfCrossDay_Cases120: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenSundayAfterElevationOfCrossDay_Cases120",
    ends={
        Property(name="atem_WhenDateCase121", type=atem_WhenSundayAfterElevationOfCrossDay, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenSundayAfterElevationOfCrossDay", type=atem_WhenDateCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenSundayAfterElevationOfCrossDay_Other122: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenSundayAfterElevationOfCrossDay_Other122",
    ends={
        Property(name="atem_WhenOther124", type=atem_WhenSundayAfterElevationOfCrossDay, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenSundayAfterElevationOfCrossDay123", type=atem_WhenOther, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_WhenModeOfWeekCase_True_actions149: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenModeOfWeekCase_True_actions149",
    ends={
        Property(name="atem_AbstractComponent151", type=atem_WhenModeOfWeekCase, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenModeOfWeekCase150", type=atem_AbstractComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenSundaysBeforeTriodion_Cases152: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenSundaysBeforeTriodion_Cases152",
    ends={
        Property(name="atem_SundaysBeforeTriodionCase", type=atem_WhenSundaysBeforeTriodion, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenSundaysBeforeTriodion", type=atem_SundaysBeforeTriodionCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_SundaysBeforeTriodion_Other153: BinaryAssociation = BinaryAssociation(
    name="dsl_SundaysBeforeTriodion_Other153",
    ends={
        Property(name="atem_WhenOther155", type=atem_WhenSundaysBeforeTriodion, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenSundaysBeforeTriodion154", type=atem_WhenOther, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_SundaysBeforeTriodionCase_True_actions156: BinaryAssociation = BinaryAssociation(
    name="dsl_SundaysBeforeTriodionCase_True_actions156",
    ends={
        Property(name="atem_AbstractComponent158", type=atem_SundaysBeforeTriodionCase, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_SundaysBeforeTriodionCase157", type=atem_AbstractComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenPeriodCase_True_actions140: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenPeriodCase_True_actions140",
    ends={
        Property(name="atem_AbstractComponent142", type=atem_WhenPeriodCase, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenPeriodCase141", type=atem_AbstractComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenModeOfWeek_Cases143: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenModeOfWeek_Cases143",
    ends={
        Property(name="atem_WhenModeOfWeekCase", type=atem_WhenModeOfWeek, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenModeOfWeek", type=atem_WhenModeOfWeekCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenModeOfWeek_Other144: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenModeOfWeek_Other144",
    ends={
        Property(name="atem_WhenOther146", type=atem_WhenModeOfWeek, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenModeOfWeek145", type=atem_WhenOther, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_WhenModeOfWeekCase_Days147: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenModeOfWeekCase_Days147",
    ends={
        Property(name="atem_ModeOfWeekSet", type=atem_WhenModeOfWeekCase, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenModeOfWeekCase148", type=atem_ModeOfWeekSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dsl_WhenExistsCase_Ref163: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenExistsCase_Ref163",
    ends={
        Property(name="atem_Definition165", type=atem_WhenExistsCase, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenExistsCase164", type=atem_Definition, multiplicity=Multiplicity(0, 1))
    }
)
dsl_WhenExistsCase_True_actions166: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenExistsCase_True_actions166",
    ends={
        Property(name="atem_AbstractComponent168", type=atem_WhenExistsCase, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenExistsCase167", type=atem_AbstractComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenExists_Cases159: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenExists_Cases159",
    ends={
        Property(name="atem_WhenExistsCase", type=atem_WhenExists, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenExists", type=atem_WhenExistsCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dsl_WhenExists_Other160: BinaryAssociation = BinaryAssociation(
    name="dsl_WhenExists_Other160",
    ends={
        Property(name="atem_WhenOther162", type=atem_WhenExists, multiplicity=Multiplicity(1, 1)),
        Property(name="atem_WhenExists161", type=atem_WhenOther, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_atem_TemplateTitle_HeadComponent = Generalization(general=HeadComponent, specific=atem_TemplateTitle)
gen_atem_PageKeepWithNext_HeadComponent = Generalization(general=HeadComponent, specific=atem_PageKeepWithNext)
gen_atem_HeaderFooterColumnCenter_HeaderFooterColumn = Generalization(general=HeaderFooterColumn, specific=atem_HeaderFooterColumnCenter)
gen_atem_HeaderFooterColumnRight_HeaderFooterColumn = Generalization(general=HeaderFooterColumn, specific=atem_HeaderFooterColumnRight)
gen_atem_HeaderFooterText_HeaderFooterFragment = Generalization(general=HeaderFooterFragment, specific=atem_HeaderFooterText)
gen_atem_HeaderFooterDate_HeaderFooterFragment = Generalization(general=HeaderFooterFragment, specific=atem_HeaderFooterDate)
gen_atem_HeaderFooterPageNumber_HeaderFooterFragment = Generalization(general=HeaderFooterFragment, specific=atem_HeaderFooterPageNumber)
gen_atem_HeaderFooterLookup_HeaderFooterFragment = Generalization(general=HeaderFooterFragment, specific=atem_HeaderFooterLookup)
gen_atem_HeaderFooterTitle_HeaderFooterFragment = Generalization(general=HeaderFooterFragment, specific=atem_HeaderFooterTitle)
gen_atem_HeaderFooterCommemoration_HeaderFooterFragment = Generalization(general=HeaderFooterFragment, specific=atem_HeaderFooterCommemoration)
gen_atem_Commemoration_HeadComponent = Generalization(general=HeadComponent, specific=atem_Commemoration)
gen_atem_PageHeaderEven_HeadComponent = Generalization(general=HeadComponent, specific=atem_PageHeaderEven)
gen_atem_PageHeaderOdd_HeadComponent = Generalization(general=HeadComponent, specific=atem_PageHeaderOdd)
gen_atem_PageFooterEven_HeadComponent = Generalization(general=HeadComponent, specific=atem_PageFooterEven)
gen_atem_PageFooterOdd_HeadComponent = Generalization(general=HeadComponent, specific=atem_PageFooterOdd)
gen_atem_HeaderFooterColumnLeft_HeaderFooterColumn = Generalization(general=HeaderFooterColumn, specific=atem_HeaderFooterColumnLeft)
gen_atem_Lookup_ElementType = Generalization(general=ElementType, specific=atem_Lookup)
gen_atem_LDP_ElementType = Generalization(general=ElementType, specific=atem_LDP)
gen_atem_TaggedText_ElementType = Generalization(general=ElementType, specific=atem_TaggedText)
gen_atem_Info_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Info)
gen_atem_VersionSwitch_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_VersionSwitch)
gen_atem_VersionSwitch_InfoElementType = Generalization(general=InfoElementType, specific=atem_VersionSwitch)
gen_atem_VersionSwitch_PrefaceElementType = Generalization(general=PrefaceElementType, specific=atem_VersionSwitch)
gen_atem_ResourceText_ElementType = Generalization(general=ElementType, specific=atem_ResourceText)
gen_atem_GenDate_LdpType = Generalization(general=LdpType, specific=atem_GenDate)
gen_atem_GenYear_LdpType = Generalization(general=LdpType, specific=atem_GenYear)
gen_atem_MCD_LdpType = Generalization(general=LdpType, specific=atem_MCD)
gen_atem_MOW_LdpType = Generalization(general=LdpType, specific=atem_MOW)
gen_atem_NOP_LdpType = Generalization(general=LdpType, specific=atem_NOP)
gen_atem_DOM_LdpType = Generalization(general=LdpType, specific=atem_DOM)
gen_atem_DOP_LdpType = Generalization(general=LdpType, specific=atem_DOP)
gen_atem_DOWN_LdpType = Generalization(general=LdpType, specific=atem_DOWN)
gen_atem_DOWT_LdpType = Generalization(general=LdpType, specific=atem_DOWT)
gen_atem_Date_HeadComponent = Generalization(general=HeadComponent, specific=atem_Date)
gen_atem_Date_SectionElementType = Generalization(general=SectionElementType, specific=atem_Date)
gen_atem_Section_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Section)
gen_atem_Section_PrefaceElementType = Generalization(general=PrefaceElementType, specific=atem_Section)
gen_atem_Section_SectionElementType = Generalization(general=SectionElementType, specific=atem_Section)
gen_atem_All_LdpType = Generalization(general=LdpType, specific=atem_All)
gen_atem_SectionFragment_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_SectionFragment)
gen_atem_SectionFragment_PrefaceElementType = Generalization(general=PrefaceElementType, specific=atem_SectionFragment)
gen_atem_SectionFragment_SectionElementType = Generalization(general=SectionElementType, specific=atem_SectionFragment)
gen_atem_Break_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Break)
gen_atem_Break_SectionElementType = Generalization(general=SectionElementType, specific=atem_Break)
gen_atem_PageNumber_HeadComponent = Generalization(general=HeadComponent, specific=atem_PageNumber)
gen_atem_PassThroughHtml_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_PassThroughHtml)
gen_atem_PassThroughHtml_SectionElementType = Generalization(general=SectionElementType, specific=atem_PassThroughHtml)
gen_atem_PassThroughPdf_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_PassThroughPdf)
gen_atem_PassThroughPdf_SectionElementType = Generalization(general=SectionElementType, specific=atem_PassThroughPdf)
gen_atem_EOW_LdpType = Generalization(general=LdpType, specific=atem_EOW)
gen_atem_SAEC_LdpType = Generalization(general=LdpType, specific=atem_SAEC)
gen_atem_SOL_LdpType = Generalization(general=LdpType, specific=atem_SOL)
gen_atem_DOL_LdpType = Generalization(general=LdpType, specific=atem_DOL)
gen_atem_WOLC_LdpType = Generalization(general=LdpType, specific=atem_WOLC)
gen_atem_WDOLC_LdpType = Generalization(general=LdpType, specific=atem_WDOLC)
gen_atem_SBT_LdpType = Generalization(general=LdpType, specific=atem_SBT)
gen_atem_TemplateFragment_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_TemplateFragment)
gen_atem_TemplateFragment_PrefaceElementType = Generalization(general=PrefaceElementType, specific=atem_TemplateFragment)
gen_atem_TemplateFragment_SectionElementType = Generalization(general=SectionElementType, specific=atem_TemplateFragment)
gen_atem_Block_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Block)
gen_atem_Block_InfoElementType = Generalization(general=InfoElementType, specific=atem_Block)
gen_atem_Block_PrefaceElementType = Generalization(general=PrefaceElementType, specific=atem_Block)
gen_atem_Block_SectionElementType = Generalization(general=SectionElementType, specific=atem_Block)
gen_atem_Hymn_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Hymn)
gen_atem_Hymn_SectionElementType = Generalization(general=SectionElementType, specific=atem_Hymn)
gen_atem_Media_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Media)
gen_atem_Media_SectionElementType = Generalization(general=SectionElementType, specific=atem_Media)
gen_atem_Verse_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Verse)
gen_atem_Verse_SectionElementType = Generalization(general=SectionElementType, specific=atem_Verse)
gen_atem_Title_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Title)
gen_atem_Title_InfoElementType = Generalization(general=InfoElementType, specific=atem_Title)
gen_atem_Title_PrefaceElementType = Generalization(general=PrefaceElementType, specific=atem_Title)
gen_atem_Title_SectionElementType = Generalization(general=SectionElementType, specific=atem_Title)
gen_atem_SubTitle_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_SubTitle)
gen_atem_SubTitle_InfoElementType = Generalization(general=InfoElementType, specific=atem_SubTitle)
gen_atem_SubTitle_PrefaceElementType = Generalization(general=PrefaceElementType, specific=atem_SubTitle)
gen_atem_SubTitle_SectionElementType = Generalization(general=SectionElementType, specific=atem_SubTitle)
gen_atem_Paragraph_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Paragraph)
gen_atem_Paragraph_InfoElementType = Generalization(general=InfoElementType, specific=atem_Paragraph)
gen_atem_Paragraph_PrefaceElementType = Generalization(general=PrefaceElementType, specific=atem_Paragraph)
gen_atem_Paragraph_SectionElementType = Generalization(general=SectionElementType, specific=atem_Paragraph)
gen_atem_Heading2_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Heading2)
gen_atem_Heading2_SectionElementType = Generalization(general=SectionElementType, specific=atem_Heading2)
gen_atem_Heading3_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Heading3)
gen_atem_Heading3_SectionElementType = Generalization(general=SectionElementType, specific=atem_Heading3)
gen_atem_Aid_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Aid)
gen_atem_Version_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Version)
gen_atem_LitBook_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_LitBook)
gen_atem_SetLocale_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_SetLocale)
gen_atem_SetLocale_SectionElementType = Generalization(general=SectionElementType, specific=atem_SetLocale)
gen_atem_Actor_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Actor)
gen_atem_Actor_SectionElementType = Generalization(general=SectionElementType, specific=atem_Actor)
gen_atem_Rubric_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Rubric)
gen_atem_Rubric_SectionElementType = Generalization(general=SectionElementType, specific=atem_Rubric)
gen_atem_Dialog_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Dialog)
gen_atem_Dialog_SectionElementType = Generalization(general=SectionElementType, specific=atem_Dialog)
gen_atem_Reading_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Reading)
gen_atem_Reading_SectionElementType = Generalization(general=SectionElementType, specific=atem_Reading)
gen_atem_Heading1_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_Heading1)
gen_atem_Heading1_SectionElementType = Generalization(general=SectionElementType, specific=atem_Heading1)
gen_atem_RestoreLocale_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_RestoreLocale)
gen_atem_RestoreLocale_SectionElementType = Generalization(general=SectionElementType, specific=atem_RestoreLocale)
gen_atem_WhenDate_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_WhenDate)
gen_atem_WhenDate_SectionElementType = Generalization(general=SectionElementType, specific=atem_WhenDate)
gen_atem_DayNameRange_AbstractDayNameCase = Generalization(general=AbstractDayNameCase, specific=atem_DayNameRange)
gen_atem_DayNameSet_AbstractDayNameCase = Generalization(general=AbstractDayNameCase, specific=atem_DayNameSet)
gen_atem_WhenPentecostarionDay_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_WhenPentecostarionDay)
gen_atem_WhenPentecostarionDay_SectionElementType = Generalization(general=SectionElementType, specific=atem_WhenPentecostarionDay)
gen_atem_WhenTriodionDay_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_WhenTriodionDay)
gen_atem_DateRange_AbstractDateCase = Generalization(general=AbstractDateCase, specific=atem_DateRange)
gen_atem_DateSet_AbstractDateCase = Generalization(general=AbstractDateCase, specific=atem_DateSet)
gen_atem_WhenDayName_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_WhenDayName)
gen_atem_WhenDayName_SectionElementType = Generalization(general=SectionElementType, specific=atem_WhenDayName)
gen_atem_WhenLukanCycleDay_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_WhenLukanCycleDay)
gen_atem_WhenLukanCycleDay_SectionElementType = Generalization(general=SectionElementType, specific=atem_WhenLukanCycleDay)
gen_atem_WhenPascha_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_WhenPascha)
gen_atem_WhenPascha_SectionElementType = Generalization(general=SectionElementType, specific=atem_WhenPascha)
gen_atem_WhenTriodionDay_SectionElementType = Generalization(general=SectionElementType, specific=atem_WhenTriodionDay)
gen_atem_WhenMovableCycleDay_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_WhenMovableCycleDay)
gen_atem_WhenMovableCycleDay_SectionElementType = Generalization(general=SectionElementType, specific=atem_WhenMovableCycleDay)
gen_atem_WhenSundayAfterElevationOfCrossDay_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_WhenSundayAfterElevationOfCrossDay)
gen_atem_WhenSundayAfterElevationOfCrossDay_SectionElementType = Generalization(general=SectionElementType, specific=atem_WhenSundayAfterElevationOfCrossDay)
gen_atem_WhenSundaysBeforeTriodion_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_WhenSundaysBeforeTriodion)
gen_atem_WhenSundaysBeforeTriodion_SectionElementType = Generalization(general=SectionElementType, specific=atem_WhenSundaysBeforeTriodion)
gen_atem_DayRange_AbstractDayCase = Generalization(general=AbstractDayCase, specific=atem_DayRange)
gen_atem_DaySet_AbstractDayCase = Generalization(general=AbstractDayCase, specific=atem_DaySet)
gen_atem_WhenModeOfWeek_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_WhenModeOfWeek)
gen_atem_WhenModeOfWeek_SectionElementType = Generalization(general=SectionElementType, specific=atem_WhenModeOfWeek)
gen_atem_WhenExists_AbstractComponent = Generalization(general=AbstractComponent, specific=atem_WhenExists)
gen_atem_WhenExists_SectionElementType = Generalization(general=SectionElementType, specific=atem_WhenExists)

# Domain Model
domain_model = DomainModel(
    name="atem",
    types={atem_Head, atem_Preface, atem_AbstractComponent, atem_HeadComponent, atem_TemplateTitle, HeadComponent, atem_HeaderFooterFragment, atem_PageKeepWithNext, atem_AtemModel, atem_TemplateStatus, atem_Import, atem_Driver, atem_HeaderFooterColumnCenter, atem_HeaderFooterColumnRight, atem_HeaderFooterText, HeaderFooterFragment, atem_HeaderFooterDate, atem_HeaderFooterPageNumber, atem_HeaderFooterLookup, atem_ElementType, atem_HeaderFooterTitle, atem_HeaderFooterCommemoration, atem_Commemoration, atem_PageHeaderEven, atem_HeaderFooterColumn, atem_PageHeaderOdd, atem_PageFooterEven, atem_PageFooterOdd, atem_HeaderFooterColumnLeft, HeaderFooterColumn, atem_Lookup, atem_LDP, atem_LdpType, atem_TaggedText, atem_Info, atem_InfoElementType, atem_VersionSwitch, AbstractComponent, InfoElementType, PrefaceElementType, atem_ResourceText, ElementType, atem_Definition, atem_GenDate, atem_GenYear, atem_MCD, atem_MOW, atem_NOP, atem_DOM, atem_DOP, atem_DOWN, atem_DOWT, atem_Date, SectionElementType, atem_PrefaceElementType, atem_Section, atem_SectionElementType, atem_All, LdpType, atem_PrefaceFragment, atem_SectionFragment, atem_Break, atem_PageNumber, atem_PassThroughHtml, atem_PassThroughPdf, atem_Title, atem_EOW, atem_SAEC, atem_SOL, atem_DOL, atem_WOLC, atem_WDOLC, atem_SBT, atem_TemplateFragment, atem_Block, atem_Hymn, atem_Media, atem_Verse, atem_SubTitle, atem_Paragraph, atem_Heading2, atem_Heading3, atem_Aid, atem_Version, atem_LitBook, atem_SetLocale, atem_Actor, atem_Rubric, atem_Dialog, atem_Reading, atem_Heading1, atem_RestoreLocale, atem_WhenDate, atem_WhenDateCase, atem_WhenOther, atem_AbstractDateCase, atem_DayNameRange, AbstractDayNameCase, atem_DayNameSet, atem_WhenPentecostarionDay, atem_WhenPeriodCase, atem_WhenTriodionDay, atem_DateRange, AbstractDateCase, atem_DateSet, atem_WhenDayName, atem_WhenDayNameCase, atem_AbstractDayNameCase, atem_WhenLukanCycleDay, atem_WhenPascha, atem_AbstractDayCase, atem_WhenMovableCycleDay, atem_WhenSundayAfterElevationOfCrossDay, atem_WhenSundaysBeforeTriodion, atem_SundaysBeforeTriodionCase, atem_DayRange, AbstractDayCase, atem_DaySet, atem_WhenModeOfWeek, atem_WhenModeOfWeekCase, atem_ModeOfWeekSet, atem_WhenExists, atem_WhenExistsCase, VersionSwitchType, Language, BreakType, BookTypes, Seasons, DayOfMonthTypes, TemplateStatuses, Null, ModeTypes, DowTypes, PeriodType, DayOfWeek, MonthName},
    associations={dsl_Template_Driver3, dsl_Template_head5, dsl_Template_preface7, dsl_Template_components9, dsl_Head_components11, dsl_TemplateTitle_Elements13, dsl_Template_Status0, imports1, dsl_HeaderFooterLookup_Elements24, dsl_PageHeader_columns14, dsl_PageHeader_columns15, dsl_PageHeader_columns17, dsl_PageHeader_columns19, dsl_HeaderFooterColumn_fragments21, dsl_ResourceTextRef28, dsl_LDP30, dsl_TaggedText_tag31, dsl_TaggedText33, dsl_Info_Elements36, dsl_Commemoration_Elements25, dsl_ResourceTextRef27, dsl_Preface_Elements37, dsl_Section_Role39, dsl_Section_Elements41, name45, name47, name43, dsl_Block_Role64, dsl_Elements66, dsl_Elements69, dsl_Elements71, dsl_Elements73, dsl_Title_Role49, dsl_Elements51, dsl_SubTitle_Role54, dsl_Elements56, dsl_Para_Role59, dsl_Elements61, dsl_Elements83, dsl_Elements85, dsl_Elements87, dsl_Elements75, dsl_Elements77, dsl_Elements79, dsl_Elements81, dsl_WhenDate_Cases89, dsl_WhenDate_Other90, dsl_WhenDateCase_Days92, dsl_WhenPentecostarionDay_Cases106, dsl_WhenPentecostarionDay_Other107, dsl_WhenDateCase_True_actions94, dsl_WhenDayName_Cases97, dsl_WhenDayName_Other98, dsl_WhenDayNameCase_Days101, dsl_WhenDayNameCase_True_actions103, dsl_WhenLukanCycleDay_Cases125, dsl_WhenLukanCycleDay_Other127, dsl_WhenPascha_true_actions130, dsl_WhenPascha_Other_actions132, dsl_WhenCase_Other_actions135, dsl_WhenPeriodCase_Days138, dsl_WhenTriodionDay_Cases110, dsl_WhenTriodionDay_Other112, dsl_WhenMovableCycleDay_Cases115, dsl_WhenMovableCycleDay_Other117, dsl_WhenSundayAfterElevationOfCrossDay_Cases120, dsl_WhenSundayAfterElevationOfCrossDay_Other122, dsl_WhenModeOfWeekCase_True_actions149, dsl_WhenSundaysBeforeTriodion_Cases152, dsl_SundaysBeforeTriodion_Other153, dsl_SundaysBeforeTriodionCase_True_actions156, dsl_WhenPeriodCase_True_actions140, dsl_WhenModeOfWeek_Cases143, dsl_WhenModeOfWeek_Other144, dsl_WhenModeOfWeekCase_Days147, dsl_WhenExistsCase_Ref163, dsl_WhenExistsCase_True_actions166, dsl_WhenExists_Cases159, dsl_WhenExists_Other160},
    generalizations={gen_atem_TemplateTitle_HeadComponent, gen_atem_PageKeepWithNext_HeadComponent, gen_atem_HeaderFooterColumnCenter_HeaderFooterColumn, gen_atem_HeaderFooterColumnRight_HeaderFooterColumn, gen_atem_HeaderFooterText_HeaderFooterFragment, gen_atem_HeaderFooterDate_HeaderFooterFragment, gen_atem_HeaderFooterPageNumber_HeaderFooterFragment, gen_atem_HeaderFooterLookup_HeaderFooterFragment, gen_atem_HeaderFooterTitle_HeaderFooterFragment, gen_atem_HeaderFooterCommemoration_HeaderFooterFragment, gen_atem_Commemoration_HeadComponent, gen_atem_PageHeaderEven_HeadComponent, gen_atem_PageHeaderOdd_HeadComponent, gen_atem_PageFooterEven_HeadComponent, gen_atem_PageFooterOdd_HeadComponent, gen_atem_HeaderFooterColumnLeft_HeaderFooterColumn, gen_atem_Lookup_ElementType, gen_atem_LDP_ElementType, gen_atem_TaggedText_ElementType, gen_atem_Info_AbstractComponent, gen_atem_VersionSwitch_AbstractComponent, gen_atem_VersionSwitch_InfoElementType, gen_atem_VersionSwitch_PrefaceElementType, gen_atem_ResourceText_ElementType, gen_atem_GenDate_LdpType, gen_atem_GenYear_LdpType, gen_atem_MCD_LdpType, gen_atem_MOW_LdpType, gen_atem_NOP_LdpType, gen_atem_DOM_LdpType, gen_atem_DOP_LdpType, gen_atem_DOWN_LdpType, gen_atem_DOWT_LdpType, gen_atem_Date_HeadComponent, gen_atem_Date_SectionElementType, gen_atem_Section_AbstractComponent, gen_atem_Section_PrefaceElementType, gen_atem_Section_SectionElementType, gen_atem_All_LdpType, gen_atem_SectionFragment_AbstractComponent, gen_atem_SectionFragment_PrefaceElementType, gen_atem_SectionFragment_SectionElementType, gen_atem_Break_AbstractComponent, gen_atem_Break_SectionElementType, gen_atem_PageNumber_HeadComponent, gen_atem_PassThroughHtml_AbstractComponent, gen_atem_PassThroughHtml_SectionElementType, gen_atem_PassThroughPdf_AbstractComponent, gen_atem_PassThroughPdf_SectionElementType, gen_atem_EOW_LdpType, gen_atem_SAEC_LdpType, gen_atem_SOL_LdpType, gen_atem_DOL_LdpType, gen_atem_WOLC_LdpType, gen_atem_WDOLC_LdpType, gen_atem_SBT_LdpType, gen_atem_TemplateFragment_AbstractComponent, gen_atem_TemplateFragment_PrefaceElementType, gen_atem_TemplateFragment_SectionElementType, gen_atem_Block_AbstractComponent, gen_atem_Block_InfoElementType, gen_atem_Block_PrefaceElementType, gen_atem_Block_SectionElementType, gen_atem_Hymn_AbstractComponent, gen_atem_Hymn_SectionElementType, gen_atem_Media_AbstractComponent, gen_atem_Media_SectionElementType, gen_atem_Verse_AbstractComponent, gen_atem_Verse_SectionElementType, gen_atem_Title_AbstractComponent, gen_atem_Title_InfoElementType, gen_atem_Title_PrefaceElementType, gen_atem_Title_SectionElementType, gen_atem_SubTitle_AbstractComponent, gen_atem_SubTitle_InfoElementType, gen_atem_SubTitle_PrefaceElementType, gen_atem_SubTitle_SectionElementType, gen_atem_Paragraph_AbstractComponent, gen_atem_Paragraph_InfoElementType, gen_atem_Paragraph_PrefaceElementType, gen_atem_Paragraph_SectionElementType, gen_atem_Heading2_AbstractComponent, gen_atem_Heading2_SectionElementType, gen_atem_Heading3_AbstractComponent, gen_atem_Heading3_SectionElementType, gen_atem_Aid_AbstractComponent, gen_atem_Version_AbstractComponent, gen_atem_LitBook_AbstractComponent, gen_atem_SetLocale_AbstractComponent, gen_atem_SetLocale_SectionElementType, gen_atem_Actor_AbstractComponent, gen_atem_Actor_SectionElementType, gen_atem_Rubric_AbstractComponent, gen_atem_Rubric_SectionElementType, gen_atem_Dialog_AbstractComponent, gen_atem_Dialog_SectionElementType, gen_atem_Reading_AbstractComponent, gen_atem_Reading_SectionElementType, gen_atem_Heading1_AbstractComponent, gen_atem_Heading1_SectionElementType, gen_atem_RestoreLocale_AbstractComponent, gen_atem_RestoreLocale_SectionElementType, gen_atem_WhenDate_AbstractComponent, gen_atem_WhenDate_SectionElementType, gen_atem_DayNameRange_AbstractDayNameCase, gen_atem_DayNameSet_AbstractDayNameCase, gen_atem_WhenPentecostarionDay_AbstractComponent, gen_atem_WhenPentecostarionDay_SectionElementType, gen_atem_WhenTriodionDay_AbstractComponent, gen_atem_DateRange_AbstractDateCase, gen_atem_DateSet_AbstractDateCase, gen_atem_WhenDayName_AbstractComponent, gen_atem_WhenDayName_SectionElementType, gen_atem_WhenLukanCycleDay_AbstractComponent, gen_atem_WhenLukanCycleDay_SectionElementType, gen_atem_WhenPascha_AbstractComponent, gen_atem_WhenPascha_SectionElementType, gen_atem_WhenTriodionDay_SectionElementType, gen_atem_WhenMovableCycleDay_AbstractComponent, gen_atem_WhenMovableCycleDay_SectionElementType, gen_atem_WhenSundayAfterElevationOfCrossDay_AbstractComponent, gen_atem_WhenSundayAfterElevationOfCrossDay_SectionElementType, gen_atem_WhenSundaysBeforeTriodion_AbstractComponent, gen_atem_WhenSundaysBeforeTriodion_SectionElementType, gen_atem_DayRange_AbstractDayCase, gen_atem_DaySet_AbstractDayCase, gen_atem_WhenModeOfWeek_AbstractComponent, gen_atem_WhenModeOfWeek_SectionElementType, gen_atem_WhenExists_AbstractComponent, gen_atem_WhenExists_SectionElementType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)