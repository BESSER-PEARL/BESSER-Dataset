import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    atem::PrefaceFragment,
    LdpType,
    atem::GenDate,
    atem::SBT,
    atem::NOP,
    atem::DOL,
    atem::MOW,
    atem::WDOLC,
    atem::WOLC,
    atem::MCD,
    atem::DOM,
    atem::GenYear,
    atem::All,
    atem::SectionElementType,
    atem::PrefaceElementType,
    atem::SOL,
    atem::SAEC,
    atem::EOW,
    atem::DOWT,
    atem::DOWN,
    atem::DOP,
    atem::LdpType,
    atem::Definition,
    ElementType,
    atem::TaggedText,
    atem::LDP,
    atem::Lookup,
    atem::ResourceText,
    SectionElementType,
    atem::InfoElementType,
    atem::ElementType,
    HeaderFooterFragment,
    atem::HeaderFooterCommemoration,
    atem::HeaderFooterDate,
    atem::HeaderFooterLookup,
    atem::HeaderFooterPageNumber,
    atem::HeaderFooterTitle,
    atem::HeaderFooterText,
    HeaderFooterColumn,
    atem::HeaderFooterColumnCenter,
    atem::HeaderFooterColumnRight,
    atem::HeaderFooterColumnLeft,
    PrefaceElementType,
    InfoElementType,
    AbstractComponent,
    atem::Section,
    atem::Info,
    atem::TemplateFragment,
    atem::Break,
    atem::Title,
    atem::SubTitle,
    atem::PassThroughPdf,
    atem::SectionFragment,
    atem::VersionSwitch,
    HeadComponent,
    atem::Date,
    atem::Commemoration,
    atem::PageFooterOdd,
    atem::TemplateTitle,
    atem::PageFooterEven,
    atem::PageHeaderOdd,
    atem::HeaderFooterColumn,
    atem::PageHeaderEven,
    atem::PageKeepWithNext,
    atem::HeaderFooterFragment,
    atem::Preface,
    atem::Head,
    atem::Driver,
    atem::Import,
    atem::TemplateStatus,
    atem::AtemModel,
    atem::HeadComponent,
    atem::AbstractComponent,
    atem::WhenExists,
    atem::WhenExistsCase,
    atem::WhenModeOfWeekCase,
    atem::WhenModeOfWeek,
    atem::SundaysBeforeTriodionCase,
    atem::WhenSundaysBeforeTriodion,
    atem::ModeOfWeekSet,
    atem::WhenMovableCycleDay,
    AbstractDayCase,
    atem::DaySet,
    atem::DayRange,
    atem::AbstractDayCase,
    atem::WhenPascha,
    atem::WhenLukanCycleDay,
    atem::WhenSundayAfterElevationOfCrossDay,
    AbstractDateCase,
    atem::DateSet,
    atem::DateRange,
    atem::WhenTriodionDay,
    atem::WhenPeriodCase,
    atem::WhenPentecostarionDay,
    AbstractDayNameCase,
    atem::DayNameSet,
    atem::DayNameRange,
    atem::AbstractDayNameCase,
    atem::WhenDayNameCase,
    atem::WhenDayName,
    atem::AbstractDateCase,
    atem::WhenOther,
    atem::WhenDateCase,
    atem::WhenDate,
    atem::RestoreLocale,
    atem::Dialog,
    atem::Rubric,
    atem::SetLocale,
    atem::LitBook,
    atem::Version,
    atem::Aid,
    atem::Heading3,
    atem::Heading2,
    atem::Heading1,
    atem::Reading,
    atem::Block,
    atem::Actor,
    atem::Paragraph,
    atem::Verse,
    atem::Media,
    atem::Hymn,
    atem::PassThroughHtml,
    atem::PageNumber,
    Language,
    BookTypes,
    DayOfWeek,
    Seasons,
    DowTypes,
    VersionSwitchType,
    BreakType,
    MonthName,
    DayOfMonthTypes,
    PeriodType,
    TemplateStatuses,
    Null,
    ModeTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_atem::prefacefragment_is_not_abstract():
    assert not inspect.isabstract(atem::PrefaceFragment)


def test_atem::prefacefragment_constructor_exists():
    assert callable(atem::PrefaceFragment.__init__)


def test_atem::prefacefragment_constructor_args():
    sig = inspect.signature(atem::PrefaceFragment.__init__)
    params = list(sig.parameters.keys())



def test_ldptype_is_not_abstract():
    assert not inspect.isabstract(LdpType)


def test_ldptype_constructor_exists():
    assert callable(LdpType.__init__)


def test_ldptype_constructor_args():
    sig = inspect.signature(LdpType.__init__)
    params = list(sig.parameters.keys())



def test_atem::gendate_is_not_abstract():
    assert not inspect.isabstract(atem::GenDate)


def test_atem::gendate_constructor_exists():
    assert callable(atem::GenDate.__init__)


def test_atem::gendate_constructor_args():
    sig = inspect.signature(atem::GenDate.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Date" in params, "Missing parameter 'dsl_Display_Date'"

def test_atem::gendate_has_dsl_Display_Date():
    assert hasattr(atem::GenDate, "dsl_Display_Date")
    descriptor = None
    for klass in atem::GenDate.__mro__:
        if "dsl_Display_Date" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Date"]
            break
    assert isinstance(descriptor, property)



def test_atem::sbt_is_not_abstract():
    assert not inspect.isabstract(atem::SBT)


def test_atem::sbt_constructor_exists():
    assert callable(atem::SBT.__init__)


def test_atem::sbt_constructor_args():
    sig = inspect.signature(atem::SBT.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_SundaysBeforeTriodion" in params, "Missing parameter 'dsl_Display_SundaysBeforeTriodion'"

def test_atem::sbt_has_dsl_Display_SundaysBeforeTriodion():
    assert hasattr(atem::SBT, "dsl_Display_SundaysBeforeTriodion")
    descriptor = None
    for klass in atem::SBT.__mro__:
        if "dsl_Display_SundaysBeforeTriodion" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_SundaysBeforeTriodion"]
            break
    assert isinstance(descriptor, property)



def test_atem::nop_is_not_abstract():
    assert not inspect.isabstract(atem::NOP)


def test_atem::nop_constructor_exists():
    assert callable(atem::NOP.__init__)


def test_atem::nop_constructor_args():
    sig = inspect.signature(atem::NOP.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Mode" in params, "Missing parameter 'dsl_Display_Mode'"

def test_atem::nop_has_dsl_Display_Mode():
    assert hasattr(atem::NOP, "dsl_Display_Mode")
    descriptor = None
    for klass in atem::NOP.__mro__:
        if "dsl_Display_Mode" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Mode"]
            break
    assert isinstance(descriptor, property)



def test_atem::dol_is_not_abstract():
    assert not inspect.isabstract(atem::DOL)


def test_atem::dol_constructor_exists():
    assert callable(atem::DOL.__init__)


def test_atem::dol_constructor_args():
    sig = inspect.signature(atem::DOL.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_DayLukan" in params, "Missing parameter 'dsl_Display_DayLukan'"

def test_atem::dol_has_dsl_Display_DayLukan():
    assert hasattr(atem::DOL, "dsl_Display_DayLukan")
    descriptor = None
    for klass in atem::DOL.__mro__:
        if "dsl_Display_DayLukan" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_DayLukan"]
            break
    assert isinstance(descriptor, property)



def test_atem::mow_is_not_abstract():
    assert not inspect.isabstract(atem::MOW)


def test_atem::mow_constructor_exists():
    assert callable(atem::MOW.__init__)


def test_atem::mow_constructor_args():
    sig = inspect.signature(atem::MOW.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Mode" in params, "Missing parameter 'dsl_Display_Mode'"

def test_atem::mow_has_dsl_Display_Mode():
    assert hasattr(atem::MOW, "dsl_Display_Mode")
    descriptor = None
    for klass in atem::MOW.__mro__:
        if "dsl_Display_Mode" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Mode"]
            break
    assert isinstance(descriptor, property)



def test_atem::wdolc_is_not_abstract():
    assert not inspect.isabstract(atem::WDOLC)


def test_atem::wdolc_constructor_exists():
    assert callable(atem::WDOLC.__init__)


def test_atem::wdolc_constructor_args():
    sig = inspect.signature(atem::WDOLC.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_DayLukan" in params, "Missing parameter 'dsl_Display_DayLukan'"

def test_atem::wdolc_has_dsl_Display_DayLukan():
    assert hasattr(atem::WDOLC, "dsl_Display_DayLukan")
    descriptor = None
    for klass in atem::WDOLC.__mro__:
        if "dsl_Display_DayLukan" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_DayLukan"]
            break
    assert isinstance(descriptor, property)



def test_atem::wolc_is_not_abstract():
    assert not inspect.isabstract(atem::WOLC)


def test_atem::wolc_constructor_exists():
    assert callable(atem::WOLC.__init__)


def test_atem::wolc_constructor_args():
    sig = inspect.signature(atem::WOLC.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_DayLukan" in params, "Missing parameter 'dsl_Display_DayLukan'"

def test_atem::wolc_has_dsl_Display_DayLukan():
    assert hasattr(atem::WOLC, "dsl_Display_DayLukan")
    descriptor = None
    for klass in atem::WOLC.__mro__:
        if "dsl_Display_DayLukan" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_DayLukan"]
            break
    assert isinstance(descriptor, property)



def test_atem::mcd_is_not_abstract():
    assert not inspect.isabstract(atem::MCD)


def test_atem::mcd_constructor_exists():
    assert callable(atem::MCD.__init__)


def test_atem::mcd_constructor_args():
    sig = inspect.signature(atem::MCD.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_MCD_value" in params, "Missing parameter 'dsl_MCD_value'"

def test_atem::mcd_has_dsl_MCD_value():
    assert hasattr(atem::MCD, "dsl_MCD_value")
    descriptor = None
    for klass in atem::MCD.__mro__:
        if "dsl_MCD_value" in klass.__dict__:
            descriptor = klass.__dict__["dsl_MCD_value"]
            break
    assert isinstance(descriptor, property)



def test_atem::dom_is_not_abstract():
    assert not inspect.isabstract(atem::DOM)


def test_atem::dom_constructor_exists():
    assert callable(atem::DOM.__init__)


def test_atem::dom_constructor_args():
    sig = inspect.signature(atem::DOM.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Mode" in params, "Missing parameter 'dsl_Display_Mode'"

def test_atem::dom_has_dsl_Display_Mode():
    assert hasattr(atem::DOM, "dsl_Display_Mode")
    descriptor = None
    for klass in atem::DOM.__mro__:
        if "dsl_Display_Mode" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Mode"]
            break
    assert isinstance(descriptor, property)



def test_atem::genyear_is_not_abstract():
    assert not inspect.isabstract(atem::GenYear)


def test_atem::genyear_constructor_exists():
    assert callable(atem::GenYear.__init__)


def test_atem::genyear_constructor_args():
    sig = inspect.signature(atem::GenYear.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Year" in params, "Missing parameter 'dsl_Display_Year'"

def test_atem::genyear_has_dsl_Display_Year():
    assert hasattr(atem::GenYear, "dsl_Display_Year")
    descriptor = None
    for klass in atem::GenYear.__mro__:
        if "dsl_Display_Year" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Year"]
            break
    assert isinstance(descriptor, property)



def test_atem::all_is_not_abstract():
    assert not inspect.isabstract(atem::All)


def test_atem::all_constructor_exists():
    assert callable(atem::All.__init__)


def test_atem::all_constructor_args():
    sig = inspect.signature(atem::All.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_LiturgicalDayProperties" in params, "Missing parameter 'dsl_Display_LiturgicalDayProperties'"

def test_atem::all_has_dsl_Display_LiturgicalDayProperties():
    assert hasattr(atem::All, "dsl_Display_LiturgicalDayProperties")
    descriptor = None
    for klass in atem::All.__mro__:
        if "dsl_Display_LiturgicalDayProperties" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_LiturgicalDayProperties"]
            break
    assert isinstance(descriptor, property)



def test_atem::sectionelementtype_is_not_abstract():
    assert not inspect.isabstract(atem::SectionElementType)


def test_atem::sectionelementtype_constructor_exists():
    assert callable(atem::SectionElementType.__init__)


def test_atem::sectionelementtype_constructor_args():
    sig = inspect.signature(atem::SectionElementType.__init__)
    params = list(sig.parameters.keys())



def test_atem::prefaceelementtype_is_not_abstract():
    assert not inspect.isabstract(atem::PrefaceElementType)


def test_atem::prefaceelementtype_constructor_exists():
    assert callable(atem::PrefaceElementType.__init__)


def test_atem::prefaceelementtype_constructor_args():
    sig = inspect.signature(atem::PrefaceElementType.__init__)
    params = list(sig.parameters.keys())



def test_atem::sol_is_not_abstract():
    assert not inspect.isabstract(atem::SOL)


def test_atem::sol_constructor_exists():
    assert callable(atem::SOL.__init__)


def test_atem::sol_constructor_args():
    sig = inspect.signature(atem::SOL.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_StartLukan" in params, "Missing parameter 'dsl_Display_StartLukan'"

def test_atem::sol_has_dsl_Display_StartLukan():
    assert hasattr(atem::SOL, "dsl_Display_StartLukan")
    descriptor = None
    for klass in atem::SOL.__mro__:
        if "dsl_Display_StartLukan" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_StartLukan"]
            break
    assert isinstance(descriptor, property)



def test_atem::saec_is_not_abstract():
    assert not inspect.isabstract(atem::SAEC)


def test_atem::saec_constructor_exists():
    assert callable(atem::SAEC.__init__)


def test_atem::saec_constructor_args():
    sig = inspect.signature(atem::SAEC.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_SundayAfterElevationCross" in params, "Missing parameter 'dsl_Display_SundayAfterElevationCross'"

def test_atem::saec_has_dsl_Display_SundayAfterElevationCross():
    assert hasattr(atem::SAEC, "dsl_Display_SundayAfterElevationCross")
    descriptor = None
    for klass in atem::SAEC.__mro__:
        if "dsl_Display_SundayAfterElevationCross" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_SundayAfterElevationCross"]
            break
    assert isinstance(descriptor, property)



def test_atem::eow_is_not_abstract():
    assert not inspect.isabstract(atem::EOW)


def test_atem::eow_constructor_exists():
    assert callable(atem::EOW.__init__)


def test_atem::eow_constructor_args():
    sig = inspect.signature(atem::EOW.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Eothinon" in params, "Missing parameter 'dsl_Display_Eothinon'"

def test_atem::eow_has_dsl_Display_Eothinon():
    assert hasattr(atem::EOW, "dsl_Display_Eothinon")
    descriptor = None
    for klass in atem::EOW.__mro__:
        if "dsl_Display_Eothinon" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Eothinon"]
            break
    assert isinstance(descriptor, property)



def test_atem::dowt_is_not_abstract():
    assert not inspect.isabstract(atem::DOWT)


def test_atem::dowt_constructor_exists():
    assert callable(atem::DOWT.__init__)


def test_atem::dowt_constructor_args():
    sig = inspect.signature(atem::DOWT.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Mode" in params, "Missing parameter 'dsl_Display_Mode'"

def test_atem::dowt_has_dsl_Display_Mode():
    assert hasattr(atem::DOWT, "dsl_Display_Mode")
    descriptor = None
    for klass in atem::DOWT.__mro__:
        if "dsl_Display_Mode" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Mode"]
            break
    assert isinstance(descriptor, property)



def test_atem::down_is_not_abstract():
    assert not inspect.isabstract(atem::DOWN)


def test_atem::down_constructor_exists():
    assert callable(atem::DOWN.__init__)


def test_atem::down_constructor_args():
    sig = inspect.signature(atem::DOWN.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Mode" in params, "Missing parameter 'dsl_Display_Mode'"

def test_atem::down_has_dsl_Display_Mode():
    assert hasattr(atem::DOWN, "dsl_Display_Mode")
    descriptor = None
    for klass in atem::DOWN.__mro__:
        if "dsl_Display_Mode" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Mode"]
            break
    assert isinstance(descriptor, property)



def test_atem::dop_is_not_abstract():
    assert not inspect.isabstract(atem::DOP)


def test_atem::dop_constructor_exists():
    assert callable(atem::DOP.__init__)


def test_atem::dop_constructor_args():
    sig = inspect.signature(atem::DOP.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Mode" in params, "Missing parameter 'dsl_Display_Mode'"

def test_atem::dop_has_dsl_Display_Mode():
    assert hasattr(atem::DOP, "dsl_Display_Mode")
    descriptor = None
    for klass in atem::DOP.__mro__:
        if "dsl_Display_Mode" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Mode"]
            break
    assert isinstance(descriptor, property)



def test_atem::ldptype_is_not_abstract():
    assert not inspect.isabstract(atem::LdpType)


def test_atem::ldptype_constructor_exists():
    assert callable(atem::LdpType.__init__)


def test_atem::ldptype_constructor_args():
    sig = inspect.signature(atem::LdpType.__init__)
    params = list(sig.parameters.keys())



def test_atem::definition_is_not_abstract():
    assert not inspect.isabstract(atem::Definition)


def test_atem::definition_constructor_exists():
    assert callable(atem::Definition.__init__)


def test_atem::definition_constructor_args():
    sig = inspect.signature(atem::Definition.__init__)
    params = list(sig.parameters.keys())



def test_elementtype_is_not_abstract():
    assert not inspect.isabstract(ElementType)


def test_elementtype_constructor_exists():
    assert callable(ElementType.__init__)


def test_elementtype_constructor_args():
    sig = inspect.signature(ElementType.__init__)
    params = list(sig.parameters.keys())



def test_atem::taggedtext_is_not_abstract():
    assert not inspect.isabstract(atem::TaggedText)


def test_atem::taggedtext_constructor_exists():
    assert callable(atem::TaggedText.__init__)


def test_atem::taggedtext_constructor_args():
    sig = inspect.signature(atem::TaggedText.__init__)
    params = list(sig.parameters.keys())



def test_atem::ldp_is_not_abstract():
    assert not inspect.isabstract(atem::LDP)


def test_atem::ldp_constructor_exists():
    assert callable(atem::LDP.__init__)


def test_atem::ldp_constructor_args():
    sig = inspect.signature(atem::LDP.__init__)
    params = list(sig.parameters.keys())



def test_atem::lookup_is_not_abstract():
    assert not inspect.isabstract(atem::Lookup)


def test_atem::lookup_constructor_exists():
    assert callable(atem::Lookup.__init__)


def test_atem::lookup_constructor_args():
    sig = inspect.signature(atem::Lookup.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Lookup_Override_Mode_Set" in params, "Missing parameter 'dsl_Lookup_Override_Mode_Set'"
    assert "dsl_Lookup_OverrideDay" in params, "Missing parameter 'dsl_Lookup_OverrideDay'"
    assert "dsl_Lookup_OverrideMode" in params, "Missing parameter 'dsl_Lookup_OverrideMode'"
    assert "dsl_Lookup_Override__Day_Set" in params, "Missing parameter 'dsl_Lookup_Override__Day_Set'"
    assert "dsl_Lookup_Media_Off" in params, "Missing parameter 'dsl_Lookup_Media_Off'"

def test_atem::lookup_has_dsl_Lookup_Override_Mode_Set():
    assert hasattr(atem::Lookup, "dsl_Lookup_Override_Mode_Set")
    descriptor = None
    for klass in atem::Lookup.__mro__:
        if "dsl_Lookup_Override_Mode_Set" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Lookup_Override_Mode_Set"]
            break
    assert isinstance(descriptor, property)

def test_atem::lookup_has_dsl_Lookup_OverrideDay():
    assert hasattr(atem::Lookup, "dsl_Lookup_OverrideDay")
    descriptor = None
    for klass in atem::Lookup.__mro__:
        if "dsl_Lookup_OverrideDay" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Lookup_OverrideDay"]
            break
    assert isinstance(descriptor, property)

def test_atem::lookup_has_dsl_Lookup_OverrideMode():
    assert hasattr(atem::Lookup, "dsl_Lookup_OverrideMode")
    descriptor = None
    for klass in atem::Lookup.__mro__:
        if "dsl_Lookup_OverrideMode" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Lookup_OverrideMode"]
            break
    assert isinstance(descriptor, property)

def test_atem::lookup_has_dsl_Lookup_Override__Day_Set():
    assert hasattr(atem::Lookup, "dsl_Lookup_Override__Day_Set")
    descriptor = None
    for klass in atem::Lookup.__mro__:
        if "dsl_Lookup_Override__Day_Set" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Lookup_Override__Day_Set"]
            break
    assert isinstance(descriptor, property)

def test_atem::lookup_has_dsl_Lookup_Media_Off():
    assert hasattr(atem::Lookup, "dsl_Lookup_Media_Off")
    descriptor = None
    for klass in atem::Lookup.__mro__:
        if "dsl_Lookup_Media_Off" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Lookup_Media_Off"]
            break
    assert isinstance(descriptor, property)



def test_atem::resourcetext_is_not_abstract():
    assert not inspect.isabstract(atem::ResourceText)


def test_atem::resourcetext_constructor_exists():
    assert callable(atem::ResourceText.__init__)


def test_atem::resourcetext_constructor_args():
    sig = inspect.signature(atem::ResourceText.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_ResourceText_Media_Off" in params, "Missing parameter 'dsl_ResourceText_Media_Off'"

def test_atem::resourcetext_has_dsl_ResourceText_Media_Off():
    assert hasattr(atem::ResourceText, "dsl_ResourceText_Media_Off")
    descriptor = None
    for klass in atem::ResourceText.__mro__:
        if "dsl_ResourceText_Media_Off" in klass.__dict__:
            descriptor = klass.__dict__["dsl_ResourceText_Media_Off"]
            break
    assert isinstance(descriptor, property)



def test_sectionelementtype_is_not_abstract():
    assert not inspect.isabstract(SectionElementType)


def test_sectionelementtype_constructor_exists():
    assert callable(SectionElementType.__init__)


def test_sectionelementtype_constructor_args():
    sig = inspect.signature(SectionElementType.__init__)
    params = list(sig.parameters.keys())



def test_atem::infoelementtype_is_not_abstract():
    assert not inspect.isabstract(atem::InfoElementType)


def test_atem::infoelementtype_constructor_exists():
    assert callable(atem::InfoElementType.__init__)


def test_atem::infoelementtype_constructor_args():
    sig = inspect.signature(atem::InfoElementType.__init__)
    params = list(sig.parameters.keys())



def test_atem::elementtype_is_not_abstract():
    assert not inspect.isabstract(atem::ElementType)


def test_atem::elementtype_constructor_exists():
    assert callable(atem::ElementType.__init__)


def test_atem::elementtype_constructor_args():
    sig = inspect.signature(atem::ElementType.__init__)
    params = list(sig.parameters.keys())



def test_headerfooterfragment_is_not_abstract():
    assert not inspect.isabstract(HeaderFooterFragment)


def test_headerfooterfragment_constructor_exists():
    assert callable(HeaderFooterFragment.__init__)


def test_headerfooterfragment_constructor_args():
    sig = inspect.signature(HeaderFooterFragment.__init__)
    params = list(sig.parameters.keys())



def test_atem::headerfootercommemoration_is_not_abstract():
    assert not inspect.isabstract(atem::HeaderFooterCommemoration)


def test_atem::headerfootercommemoration_constructor_exists():
    assert callable(atem::HeaderFooterCommemoration.__init__)


def test_atem::headerfootercommemoration_constructor_args():
    sig = inspect.signature(atem::HeaderFooterCommemoration.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_HeaderFooterCommemoration" in params, "Missing parameter 'dsl_HeaderFooterCommemoration'"

def test_atem::headerfootercommemoration_has_dsl_HeaderFooterCommemoration():
    assert hasattr(atem::HeaderFooterCommemoration, "dsl_HeaderFooterCommemoration")
    descriptor = None
    for klass in atem::HeaderFooterCommemoration.__mro__:
        if "dsl_HeaderFooterCommemoration" in klass.__dict__:
            descriptor = klass.__dict__["dsl_HeaderFooterCommemoration"]
            break
    assert isinstance(descriptor, property)



def test_atem::headerfooterdate_is_not_abstract():
    assert not inspect.isabstract(atem::HeaderFooterDate)


def test_atem::headerfooterdate_constructor_exists():
    assert callable(atem::HeaderFooterDate.__init__)


def test_atem::headerfooterdate_constructor_args():
    sig = inspect.signature(atem::HeaderFooterDate.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_HeaderFooterDate" in params, "Missing parameter 'dsl_HeaderFooterDate'"
    assert "dsl_HeaderFooterDate_Language" in params, "Missing parameter 'dsl_HeaderFooterDate_Language'"

def test_atem::headerfooterdate_has_dsl_HeaderFooterDate():
    assert hasattr(atem::HeaderFooterDate, "dsl_HeaderFooterDate")
    descriptor = None
    for klass in atem::HeaderFooterDate.__mro__:
        if "dsl_HeaderFooterDate" in klass.__dict__:
            descriptor = klass.__dict__["dsl_HeaderFooterDate"]
            break
    assert isinstance(descriptor, property)

def test_atem::headerfooterdate_has_dsl_HeaderFooterDate_Language():
    assert hasattr(atem::HeaderFooterDate, "dsl_HeaderFooterDate_Language")
    descriptor = None
    for klass in atem::HeaderFooterDate.__mro__:
        if "dsl_HeaderFooterDate_Language" in klass.__dict__:
            descriptor = klass.__dict__["dsl_HeaderFooterDate_Language"]
            break
    assert isinstance(descriptor, property)



def test_atem::headerfooterlookup_is_not_abstract():
    assert not inspect.isabstract(atem::HeaderFooterLookup)


def test_atem::headerfooterlookup_constructor_exists():
    assert callable(atem::HeaderFooterLookup.__init__)


def test_atem::headerfooterlookup_constructor_args():
    sig = inspect.signature(atem::HeaderFooterLookup.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_HeaderFooterLookup_Language" in params, "Missing parameter 'dsl_HeaderFooterLookup_Language'"

def test_atem::headerfooterlookup_has_dsl_HeaderFooterLookup_Language():
    assert hasattr(atem::HeaderFooterLookup, "dsl_HeaderFooterLookup_Language")
    descriptor = None
    for klass in atem::HeaderFooterLookup.__mro__:
        if "dsl_HeaderFooterLookup_Language" in klass.__dict__:
            descriptor = klass.__dict__["dsl_HeaderFooterLookup_Language"]
            break
    assert isinstance(descriptor, property)



def test_atem::headerfooterpagenumber_is_not_abstract():
    assert not inspect.isabstract(atem::HeaderFooterPageNumber)


def test_atem::headerfooterpagenumber_constructor_exists():
    assert callable(atem::HeaderFooterPageNumber.__init__)


def test_atem::headerfooterpagenumber_constructor_args():
    sig = inspect.signature(atem::HeaderFooterPageNumber.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_HeaderFooterPageNumber" in params, "Missing parameter 'dsl_HeaderFooterPageNumber'"

def test_atem::headerfooterpagenumber_has_dsl_HeaderFooterPageNumber():
    assert hasattr(atem::HeaderFooterPageNumber, "dsl_HeaderFooterPageNumber")
    descriptor = None
    for klass in atem::HeaderFooterPageNumber.__mro__:
        if "dsl_HeaderFooterPageNumber" in klass.__dict__:
            descriptor = klass.__dict__["dsl_HeaderFooterPageNumber"]
            break
    assert isinstance(descriptor, property)



def test_atem::headerfootertitle_is_not_abstract():
    assert not inspect.isabstract(atem::HeaderFooterTitle)


def test_atem::headerfootertitle_constructor_exists():
    assert callable(atem::HeaderFooterTitle.__init__)


def test_atem::headerfootertitle_constructor_args():
    sig = inspect.signature(atem::HeaderFooterTitle.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_HeaderFooterTitle" in params, "Missing parameter 'dsl_HeaderFooterTitle'"

def test_atem::headerfootertitle_has_dsl_HeaderFooterTitle():
    assert hasattr(atem::HeaderFooterTitle, "dsl_HeaderFooterTitle")
    descriptor = None
    for klass in atem::HeaderFooterTitle.__mro__:
        if "dsl_HeaderFooterTitle" in klass.__dict__:
            descriptor = klass.__dict__["dsl_HeaderFooterTitle"]
            break
    assert isinstance(descriptor, property)



def test_atem::headerfootertext_is_not_abstract():
    assert not inspect.isabstract(atem::HeaderFooterText)


def test_atem::headerfootertext_constructor_exists():
    assert callable(atem::HeaderFooterText.__init__)


def test_atem::headerfootertext_constructor_args():
    sig = inspect.signature(atem::HeaderFooterText.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_HeaderFooterText" in params, "Missing parameter 'dsl_HeaderFooterText'"

def test_atem::headerfootertext_has_dsl_HeaderFooterText():
    assert hasattr(atem::HeaderFooterText, "dsl_HeaderFooterText")
    descriptor = None
    for klass in atem::HeaderFooterText.__mro__:
        if "dsl_HeaderFooterText" in klass.__dict__:
            descriptor = klass.__dict__["dsl_HeaderFooterText"]
            break
    assert isinstance(descriptor, property)



def test_headerfootercolumn_is_not_abstract():
    assert not inspect.isabstract(HeaderFooterColumn)


def test_headerfootercolumn_constructor_exists():
    assert callable(HeaderFooterColumn.__init__)


def test_headerfootercolumn_constructor_args():
    sig = inspect.signature(HeaderFooterColumn.__init__)
    params = list(sig.parameters.keys())



def test_atem::headerfootercolumncenter_is_not_abstract():
    assert not inspect.isabstract(atem::HeaderFooterColumnCenter)


def test_atem::headerfootercolumncenter_constructor_exists():
    assert callable(atem::HeaderFooterColumnCenter.__init__)


def test_atem::headerfootercolumncenter_constructor_args():
    sig = inspect.signature(atem::HeaderFooterColumnCenter.__init__)
    params = list(sig.parameters.keys())



def test_atem::headerfootercolumnright_is_not_abstract():
    assert not inspect.isabstract(atem::HeaderFooterColumnRight)


def test_atem::headerfootercolumnright_constructor_exists():
    assert callable(atem::HeaderFooterColumnRight.__init__)


def test_atem::headerfootercolumnright_constructor_args():
    sig = inspect.signature(atem::HeaderFooterColumnRight.__init__)
    params = list(sig.parameters.keys())



def test_atem::headerfootercolumnleft_is_not_abstract():
    assert not inspect.isabstract(atem::HeaderFooterColumnLeft)


def test_atem::headerfootercolumnleft_constructor_exists():
    assert callable(atem::HeaderFooterColumnLeft.__init__)


def test_atem::headerfootercolumnleft_constructor_args():
    sig = inspect.signature(atem::HeaderFooterColumnLeft.__init__)
    params = list(sig.parameters.keys())



def test_prefaceelementtype_is_not_abstract():
    assert not inspect.isabstract(PrefaceElementType)


def test_prefaceelementtype_constructor_exists():
    assert callable(PrefaceElementType.__init__)


def test_prefaceelementtype_constructor_args():
    sig = inspect.signature(PrefaceElementType.__init__)
    params = list(sig.parameters.keys())



def test_infoelementtype_is_not_abstract():
    assert not inspect.isabstract(InfoElementType)


def test_infoelementtype_constructor_exists():
    assert callable(InfoElementType.__init__)


def test_infoelementtype_constructor_args():
    sig = inspect.signature(InfoElementType.__init__)
    params = list(sig.parameters.keys())



def test_abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(AbstractComponent)


def test_abstractcomponent_constructor_exists():
    assert callable(AbstractComponent.__init__)


def test_abstractcomponent_constructor_args():
    sig = inspect.signature(AbstractComponent.__init__)
    params = list(sig.parameters.keys())



def test_atem::section_is_not_abstract():
    assert not inspect.isabstract(atem::Section)


def test_atem::section_constructor_exists():
    assert callable(atem::Section.__init__)


def test_atem::section_constructor_args():
    sig = inspect.signature(atem::Section.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atem::section_has_name():
    assert hasattr(atem::Section, "name")
    descriptor = None
    for klass in atem::Section.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atem::info_is_not_abstract():
    assert not inspect.isabstract(atem::Info)


def test_atem::info_constructor_exists():
    assert callable(atem::Info.__init__)


def test_atem::info_constructor_args():
    sig = inspect.signature(atem::Info.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atem::info_has_name():
    assert hasattr(atem::Info, "name")
    descriptor = None
    for klass in atem::Info.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atem::templatefragment_is_not_abstract():
    assert not inspect.isabstract(atem::TemplateFragment)


def test_atem::templatefragment_constructor_exists():
    assert callable(atem::TemplateFragment.__init__)


def test_atem::templatefragment_constructor_args():
    sig = inspect.signature(atem::TemplateFragment.__init__)
    params = list(sig.parameters.keys())



def test_atem::break_is_not_abstract():
    assert not inspect.isabstract(atem::Break)


def test_atem::break_constructor_exists():
    assert callable(atem::Break.__init__)


def test_atem::break_constructor_args():
    sig = inspect.signature(atem::Break.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_break_type" in params, "Missing parameter 'dsl_break_type'"

def test_atem::break_has_dsl_break_type():
    assert hasattr(atem::Break, "dsl_break_type")
    descriptor = None
    for klass in atem::Break.__mro__:
        if "dsl_break_type" in klass.__dict__:
            descriptor = klass.__dict__["dsl_break_type"]
            break
    assert isinstance(descriptor, property)



def test_atem::title_is_not_abstract():
    assert not inspect.isabstract(atem::Title)


def test_atem::title_constructor_exists():
    assert callable(atem::Title.__init__)


def test_atem::title_constructor_args():
    sig = inspect.signature(atem::Title.__init__)
    params = list(sig.parameters.keys())



def test_atem::subtitle_is_not_abstract():
    assert not inspect.isabstract(atem::SubTitle)


def test_atem::subtitle_constructor_exists():
    assert callable(atem::SubTitle.__init__)


def test_atem::subtitle_constructor_args():
    sig = inspect.signature(atem::SubTitle.__init__)
    params = list(sig.parameters.keys())



def test_atem::passthroughpdf_is_not_abstract():
    assert not inspect.isabstract(atem::PassThroughPdf)


def test_atem::passthroughpdf_constructor_exists():
    assert callable(atem::PassThroughPdf.__init__)


def test_atem::passthroughpdf_constructor_args():
    sig = inspect.signature(atem::PassThroughPdf.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Passthrough_pdf_text" in params, "Missing parameter 'dsl_Passthrough_pdf_text'"

def test_atem::passthroughpdf_has_dsl_Passthrough_pdf_text():
    assert hasattr(atem::PassThroughPdf, "dsl_Passthrough_pdf_text")
    descriptor = None
    for klass in atem::PassThroughPdf.__mro__:
        if "dsl_Passthrough_pdf_text" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Passthrough_pdf_text"]
            break
    assert isinstance(descriptor, property)



def test_atem::sectionfragment_is_not_abstract():
    assert not inspect.isabstract(atem::SectionFragment)


def test_atem::sectionfragment_constructor_exists():
    assert callable(atem::SectionFragment.__init__)


def test_atem::sectionfragment_constructor_args():
    sig = inspect.signature(atem::SectionFragment.__init__)
    params = list(sig.parameters.keys())



def test_atem::versionswitch_is_not_abstract():
    assert not inspect.isabstract(atem::VersionSwitch)


def test_atem::versionswitch_constructor_exists():
    assert callable(atem::VersionSwitch.__init__)


def test_atem::versionswitch_constructor_args():
    sig = inspect.signature(atem::VersionSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_VersionSwitch_flag" in params, "Missing parameter 'dsl_VersionSwitch_flag'"

def test_atem::versionswitch_has_dsl_VersionSwitch_flag():
    assert hasattr(atem::VersionSwitch, "dsl_VersionSwitch_flag")
    descriptor = None
    for klass in atem::VersionSwitch.__mro__:
        if "dsl_VersionSwitch_flag" in klass.__dict__:
            descriptor = klass.__dict__["dsl_VersionSwitch_flag"]
            break
    assert isinstance(descriptor, property)



def test_headcomponent_is_not_abstract():
    assert not inspect.isabstract(HeadComponent)


def test_headcomponent_constructor_exists():
    assert callable(HeadComponent.__init__)


def test_headcomponent_constructor_args():
    sig = inspect.signature(HeadComponent.__init__)
    params = list(sig.parameters.keys())



def test_atem::date_is_not_abstract():
    assert not inspect.isabstract(atem::Date)


def test_atem::date_constructor_exists():
    assert callable(atem::Date.__init__)


def test_atem::date_constructor_args():
    sig = inspect.signature(atem::Date.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Date_month" in params, "Missing parameter 'dsl_Date_month'"
    assert "dsl_Date_day" in params, "Missing parameter 'dsl_Date_day'"
    assert "dsl_Date_year" in params, "Missing parameter 'dsl_Date_year'"

def test_atem::date_has_dsl_Date_month():
    assert hasattr(atem::Date, "dsl_Date_month")
    descriptor = None
    for klass in atem::Date.__mro__:
        if "dsl_Date_month" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Date_month"]
            break
    assert isinstance(descriptor, property)

def test_atem::date_has_dsl_Date_day():
    assert hasattr(atem::Date, "dsl_Date_day")
    descriptor = None
    for klass in atem::Date.__mro__:
        if "dsl_Date_day" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Date_day"]
            break
    assert isinstance(descriptor, property)

def test_atem::date_has_dsl_Date_year():
    assert hasattr(atem::Date, "dsl_Date_year")
    descriptor = None
    for klass in atem::Date.__mro__:
        if "dsl_Date_year" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Date_year"]
            break
    assert isinstance(descriptor, property)



def test_atem::commemoration_is_not_abstract():
    assert not inspect.isabstract(atem::Commemoration)


def test_atem::commemoration_constructor_exists():
    assert callable(atem::Commemoration.__init__)


def test_atem::commemoration_constructor_args():
    sig = inspect.signature(atem::Commemoration.__init__)
    params = list(sig.parameters.keys())



def test_atem::pagefooterodd_is_not_abstract():
    assert not inspect.isabstract(atem::PageFooterOdd)


def test_atem::pagefooterodd_constructor_exists():
    assert callable(atem::PageFooterOdd.__init__)


def test_atem::pagefooterodd_constructor_args():
    sig = inspect.signature(atem::PageFooterOdd.__init__)
    params = list(sig.parameters.keys())



def test_atem::templatetitle_is_not_abstract():
    assert not inspect.isabstract(atem::TemplateTitle)


def test_atem::templatetitle_constructor_exists():
    assert callable(atem::TemplateTitle.__init__)


def test_atem::templatetitle_constructor_args():
    sig = inspect.signature(atem::TemplateTitle.__init__)
    params = list(sig.parameters.keys())



def test_atem::pagefootereven_is_not_abstract():
    assert not inspect.isabstract(atem::PageFooterEven)


def test_atem::pagefootereven_constructor_exists():
    assert callable(atem::PageFooterEven.__init__)


def test_atem::pagefootereven_constructor_args():
    sig = inspect.signature(atem::PageFooterEven.__init__)
    params = list(sig.parameters.keys())



def test_atem::pageheaderodd_is_not_abstract():
    assert not inspect.isabstract(atem::PageHeaderOdd)


def test_atem::pageheaderodd_constructor_exists():
    assert callable(atem::PageHeaderOdd.__init__)


def test_atem::pageheaderodd_constructor_args():
    sig = inspect.signature(atem::PageHeaderOdd.__init__)
    params = list(sig.parameters.keys())



def test_atem::headerfootercolumn_is_not_abstract():
    assert not inspect.isabstract(atem::HeaderFooterColumn)


def test_atem::headerfootercolumn_constructor_exists():
    assert callable(atem::HeaderFooterColumn.__init__)


def test_atem::headerfootercolumn_constructor_args():
    sig = inspect.signature(atem::HeaderFooterColumn.__init__)
    params = list(sig.parameters.keys())



def test_atem::pageheadereven_is_not_abstract():
    assert not inspect.isabstract(atem::PageHeaderEven)


def test_atem::pageheadereven_constructor_exists():
    assert callable(atem::PageHeaderEven.__init__)


def test_atem::pageheadereven_constructor_args():
    sig = inspect.signature(atem::PageHeaderEven.__init__)
    params = list(sig.parameters.keys())



def test_atem::pagekeepwithnext_is_not_abstract():
    assert not inspect.isabstract(atem::PageKeepWithNext)


def test_atem::pagekeepwithnext_constructor_exists():
    assert callable(atem::PageKeepWithNext.__init__)


def test_atem::pagekeepwithnext_constructor_args():
    sig = inspect.signature(atem::PageKeepWithNext.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_PageKeepWithNext_value" in params, "Missing parameter 'dsl_PageKeepWithNext_value'"

def test_atem::pagekeepwithnext_has_dsl_PageKeepWithNext_value():
    assert hasattr(atem::PageKeepWithNext, "dsl_PageKeepWithNext_value")
    descriptor = None
    for klass in atem::PageKeepWithNext.__mro__:
        if "dsl_PageKeepWithNext_value" in klass.__dict__:
            descriptor = klass.__dict__["dsl_PageKeepWithNext_value"]
            break
    assert isinstance(descriptor, property)



def test_atem::headerfooterfragment_is_not_abstract():
    assert not inspect.isabstract(atem::HeaderFooterFragment)


def test_atem::headerfooterfragment_constructor_exists():
    assert callable(atem::HeaderFooterFragment.__init__)


def test_atem::headerfooterfragment_constructor_args():
    sig = inspect.signature(atem::HeaderFooterFragment.__init__)
    params = list(sig.parameters.keys())



def test_atem::preface_is_not_abstract():
    assert not inspect.isabstract(atem::Preface)


def test_atem::preface_constructor_exists():
    assert callable(atem::Preface.__init__)


def test_atem::preface_constructor_args():
    sig = inspect.signature(atem::Preface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atem::preface_has_name():
    assert hasattr(atem::Preface, "name")
    descriptor = None
    for klass in atem::Preface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atem::head_is_not_abstract():
    assert not inspect.isabstract(atem::Head)


def test_atem::head_constructor_exists():
    assert callable(atem::Head.__init__)


def test_atem::head_constructor_args():
    sig = inspect.signature(atem::Head.__init__)
    params = list(sig.parameters.keys())



def test_atem::driver_is_not_abstract():
    assert not inspect.isabstract(atem::Driver)


def test_atem::driver_constructor_exists():
    assert callable(atem::Driver.__init__)


def test_atem::driver_constructor_args():
    sig = inspect.signature(atem::Driver.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Driver_RegEx" in params, "Missing parameter 'dsl_Driver_RegEx'"
    assert "dsl_Driver_Status" in params, "Missing parameter 'dsl_Driver_Status'"

def test_atem::driver_has_dsl_Driver_RegEx():
    assert hasattr(atem::Driver, "dsl_Driver_RegEx")
    descriptor = None
    for klass in atem::Driver.__mro__:
        if "dsl_Driver_RegEx" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Driver_RegEx"]
            break
    assert isinstance(descriptor, property)

def test_atem::driver_has_dsl_Driver_Status():
    assert hasattr(atem::Driver, "dsl_Driver_Status")
    descriptor = None
    for klass in atem::Driver.__mro__:
        if "dsl_Driver_Status" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Driver_Status"]
            break
    assert isinstance(descriptor, property)



def test_atem::import_is_not_abstract():
    assert not inspect.isabstract(atem::Import)


def test_atem::import_constructor_exists():
    assert callable(atem::Import.__init__)


def test_atem::import_constructor_args():
    sig = inspect.signature(atem::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_atem::import_has_importedNamespace():
    assert hasattr(atem::Import, "importedNamespace")
    descriptor = None
    for klass in atem::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_atem::templatestatus_is_not_abstract():
    assert not inspect.isabstract(atem::TemplateStatus)


def test_atem::templatestatus_constructor_exists():
    assert callable(atem::TemplateStatus.__init__)


def test_atem::templatestatus_constructor_args():
    sig = inspect.signature(atem::TemplateStatus.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_TemplateStatus" in params, "Missing parameter 'dsl_TemplateStatus'"

def test_atem::templatestatus_has_dsl_TemplateStatus():
    assert hasattr(atem::TemplateStatus, "dsl_TemplateStatus")
    descriptor = None
    for klass in atem::TemplateStatus.__mro__:
        if "dsl_TemplateStatus" in klass.__dict__:
            descriptor = klass.__dict__["dsl_TemplateStatus"]
            break
    assert isinstance(descriptor, property)



def test_atem::atemmodel_is_not_abstract():
    assert not inspect.isabstract(atem::AtemModel)


def test_atem::atemmodel_constructor_exists():
    assert callable(atem::AtemModel.__init__)


def test_atem::atemmodel_constructor_args():
    sig = inspect.signature(atem::AtemModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atem::atemmodel_has_name():
    assert hasattr(atem::AtemModel, "name")
    descriptor = None
    for klass in atem::AtemModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atem::headcomponent_is_not_abstract():
    assert not inspect.isabstract(atem::HeadComponent)


def test_atem::headcomponent_constructor_exists():
    assert callable(atem::HeadComponent.__init__)


def test_atem::headcomponent_constructor_args():
    sig = inspect.signature(atem::HeadComponent.__init__)
    params = list(sig.parameters.keys())



def test_atem::abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(atem::AbstractComponent)


def test_atem::abstractcomponent_constructor_exists():
    assert callable(atem::AbstractComponent.__init__)


def test_atem::abstractcomponent_constructor_args():
    sig = inspect.signature(atem::AbstractComponent.__init__)
    params = list(sig.parameters.keys())



def test_atem::whenexists_is_not_abstract():
    assert not inspect.isabstract(atem::WhenExists)


def test_atem::whenexists_constructor_exists():
    assert callable(atem::WhenExists.__init__)


def test_atem::whenexists_constructor_args():
    sig = inspect.signature(atem::WhenExists.__init__)
    params = list(sig.parameters.keys())



def test_atem::whenexistscase_is_not_abstract():
    assert not inspect.isabstract(atem::WhenExistsCase)


def test_atem::whenexistscase_constructor_exists():
    assert callable(atem::WhenExistsCase.__init__)


def test_atem::whenexistscase_constructor_args():
    sig = inspect.signature(atem::WhenExistsCase.__init__)
    params = list(sig.parameters.keys())



def test_atem::whenmodeofweekcase_is_not_abstract():
    assert not inspect.isabstract(atem::WhenModeOfWeekCase)


def test_atem::whenmodeofweekcase_constructor_exists():
    assert callable(atem::WhenModeOfWeekCase.__init__)


def test_atem::whenmodeofweekcase_constructor_args():
    sig = inspect.signature(atem::WhenModeOfWeekCase.__init__)
    params = list(sig.parameters.keys())



def test_atem::whenmodeofweek_is_not_abstract():
    assert not inspect.isabstract(atem::WhenModeOfWeek)


def test_atem::whenmodeofweek_constructor_exists():
    assert callable(atem::WhenModeOfWeek.__init__)


def test_atem::whenmodeofweek_constructor_args():
    sig = inspect.signature(atem::WhenModeOfWeek.__init__)
    params = list(sig.parameters.keys())



def test_atem::sundaysbeforetriodioncase_is_not_abstract():
    assert not inspect.isabstract(atem::SundaysBeforeTriodionCase)


def test_atem::sundaysbeforetriodioncase_constructor_exists():
    assert callable(atem::SundaysBeforeTriodionCase.__init__)


def test_atem::sundaysbeforetriodioncase_constructor_args():
    sig = inspect.signature(atem::SundaysBeforeTriodionCase.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_SundaysBeforeTriodionCase_Days" in params, "Missing parameter 'dsl_SundaysBeforeTriodionCase_Days'"

def test_atem::sundaysbeforetriodioncase_has_dsl_SundaysBeforeTriodionCase_Days():
    assert hasattr(atem::SundaysBeforeTriodionCase, "dsl_SundaysBeforeTriodionCase_Days")
    descriptor = None
    for klass in atem::SundaysBeforeTriodionCase.__mro__:
        if "dsl_SundaysBeforeTriodionCase_Days" in klass.__dict__:
            descriptor = klass.__dict__["dsl_SundaysBeforeTriodionCase_Days"]
            break
    assert isinstance(descriptor, property)



def test_atem::whensundaysbeforetriodion_is_not_abstract():
    assert not inspect.isabstract(atem::WhenSundaysBeforeTriodion)


def test_atem::whensundaysbeforetriodion_constructor_exists():
    assert callable(atem::WhenSundaysBeforeTriodion.__init__)


def test_atem::whensundaysbeforetriodion_constructor_args():
    sig = inspect.signature(atem::WhenSundaysBeforeTriodion.__init__)
    params = list(sig.parameters.keys())



def test_atem::modeofweekset_is_not_abstract():
    assert not inspect.isabstract(atem::ModeOfWeekSet)


def test_atem::modeofweekset_constructor_exists():
    assert callable(atem::ModeOfWeekSet.__init__)


def test_atem::modeofweekset_constructor_args():
    sig = inspect.signature(atem::ModeOfWeekSet.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_ModeOfWeekSet_MOWs" in params, "Missing parameter 'dsl_ModeOfWeekSet_MOWs'"

def test_atem::modeofweekset_has_dsl_ModeOfWeekSet_MOWs():
    assert hasattr(atem::ModeOfWeekSet, "dsl_ModeOfWeekSet_MOWs")
    descriptor = None
    for klass in atem::ModeOfWeekSet.__mro__:
        if "dsl_ModeOfWeekSet_MOWs" in klass.__dict__:
            descriptor = klass.__dict__["dsl_ModeOfWeekSet_MOWs"]
            break
    assert isinstance(descriptor, property)



def test_atem::whenmovablecycleday_is_not_abstract():
    assert not inspect.isabstract(atem::WhenMovableCycleDay)


def test_atem::whenmovablecycleday_constructor_exists():
    assert callable(atem::WhenMovableCycleDay.__init__)


def test_atem::whenmovablecycleday_constructor_args():
    sig = inspect.signature(atem::WhenMovableCycleDay.__init__)
    params = list(sig.parameters.keys())



def test_abstractdaycase_is_not_abstract():
    assert not inspect.isabstract(AbstractDayCase)


def test_abstractdaycase_constructor_exists():
    assert callable(AbstractDayCase.__init__)


def test_abstractdaycase_constructor_args():
    sig = inspect.signature(AbstractDayCase.__init__)
    params = list(sig.parameters.keys())



def test_atem::dayset_is_not_abstract():
    assert not inspect.isabstract(atem::DaySet)


def test_atem::dayset_constructor_exists():
    assert callable(atem::DaySet.__init__)


def test_atem::dayset_constructor_args():
    sig = inspect.signature(atem::DaySet.__init__)
    params = list(sig.parameters.keys())
    assert "dslSetValue_Days" in params, "Missing parameter 'dslSetValue_Days'"

def test_atem::dayset_has_dslSetValue_Days():
    assert hasattr(atem::DaySet, "dslSetValue_Days")
    descriptor = None
    for klass in atem::DaySet.__mro__:
        if "dslSetValue_Days" in klass.__dict__:
            descriptor = klass.__dict__["dslSetValue_Days"]
            break
    assert isinstance(descriptor, property)



def test_atem::dayrange_is_not_abstract():
    assert not inspect.isabstract(atem::DayRange)


def test_atem::dayrange_constructor_exists():
    assert callable(atem::DayRange.__init__)


def test_atem::dayrange_constructor_args():
    sig = inspect.signature(atem::DayRange.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Range_To" in params, "Missing parameter 'dsl_Range_To'"
    assert "dsl_DayRange_from" in params, "Missing parameter 'dsl_DayRange_from'"

def test_atem::dayrange_has_dsl_Range_To():
    assert hasattr(atem::DayRange, "dsl_Range_To")
    descriptor = None
    for klass in atem::DayRange.__mro__:
        if "dsl_Range_To" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Range_To"]
            break
    assert isinstance(descriptor, property)

def test_atem::dayrange_has_dsl_DayRange_from():
    assert hasattr(atem::DayRange, "dsl_DayRange_from")
    descriptor = None
    for klass in atem::DayRange.__mro__:
        if "dsl_DayRange_from" in klass.__dict__:
            descriptor = klass.__dict__["dsl_DayRange_from"]
            break
    assert isinstance(descriptor, property)



def test_atem::abstractdaycase_is_not_abstract():
    assert not inspect.isabstract(atem::AbstractDayCase)


def test_atem::abstractdaycase_constructor_exists():
    assert callable(atem::AbstractDayCase.__init__)


def test_atem::abstractdaycase_constructor_args():
    sig = inspect.signature(atem::AbstractDayCase.__init__)
    params = list(sig.parameters.keys())



def test_atem::whenpascha_is_not_abstract():
    assert not inspect.isabstract(atem::WhenPascha)


def test_atem::whenpascha_constructor_exists():
    assert callable(atem::WhenPascha.__init__)


def test_atem::whenpascha_constructor_args():
    sig = inspect.signature(atem::WhenPascha.__init__)
    params = list(sig.parameters.keys())



def test_atem::whenlukancycleday_is_not_abstract():
    assert not inspect.isabstract(atem::WhenLukanCycleDay)


def test_atem::whenlukancycleday_constructor_exists():
    assert callable(atem::WhenLukanCycleDay.__init__)


def test_atem::whenlukancycleday_constructor_args():
    sig = inspect.signature(atem::WhenLukanCycleDay.__init__)
    params = list(sig.parameters.keys())



def test_atem::whensundayafterelevationofcrossday_is_not_abstract():
    assert not inspect.isabstract(atem::WhenSundayAfterElevationOfCrossDay)


def test_atem::whensundayafterelevationofcrossday_constructor_exists():
    assert callable(atem::WhenSundayAfterElevationOfCrossDay.__init__)


def test_atem::whensundayafterelevationofcrossday_constructor_args():
    sig = inspect.signature(atem::WhenSundayAfterElevationOfCrossDay.__init__)
    params = list(sig.parameters.keys())



def test_abstractdatecase_is_not_abstract():
    assert not inspect.isabstract(AbstractDateCase)


def test_abstractdatecase_constructor_exists():
    assert callable(AbstractDateCase.__init__)


def test_abstractdatecase_constructor_args():
    sig = inspect.signature(AbstractDateCase.__init__)
    params = list(sig.parameters.keys())



def test_atem::dateset_is_not_abstract():
    assert not inspect.isabstract(atem::DateSet)


def test_atem::dateset_constructor_exists():
    assert callable(atem::DateSet.__init__)


def test_atem::dateset_constructor_args():
    sig = inspect.signature(atem::DateSet.__init__)
    params = list(sig.parameters.keys())
    assert "dslDateSet_Values" in params, "Missing parameter 'dslDateSet_Values'"

def test_atem::dateset_has_dslDateSet_Values():
    assert hasattr(atem::DateSet, "dslDateSet_Values")
    descriptor = None
    for klass in atem::DateSet.__mro__:
        if "dslDateSet_Values" in klass.__dict__:
            descriptor = klass.__dict__["dslDateSet_Values"]
            break
    assert isinstance(descriptor, property)



def test_atem::daterange_is_not_abstract():
    assert not inspect.isabstract(atem::DateRange)


def test_atem::daterange_constructor_exists():
    assert callable(atem::DateRange.__init__)


def test_atem::daterange_constructor_args():
    sig = inspect.signature(atem::DateRange.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_DateRange_To" in params, "Missing parameter 'dsl_DateRange_To'"
    assert "dsl_DateRange_from" in params, "Missing parameter 'dsl_DateRange_from'"

def test_atem::daterange_has_dsl_DateRange_To():
    assert hasattr(atem::DateRange, "dsl_DateRange_To")
    descriptor = None
    for klass in atem::DateRange.__mro__:
        if "dsl_DateRange_To" in klass.__dict__:
            descriptor = klass.__dict__["dsl_DateRange_To"]
            break
    assert isinstance(descriptor, property)

def test_atem::daterange_has_dsl_DateRange_from():
    assert hasattr(atem::DateRange, "dsl_DateRange_from")
    descriptor = None
    for klass in atem::DateRange.__mro__:
        if "dsl_DateRange_from" in klass.__dict__:
            descriptor = klass.__dict__["dsl_DateRange_from"]
            break
    assert isinstance(descriptor, property)



def test_atem::whentriodionday_is_not_abstract():
    assert not inspect.isabstract(atem::WhenTriodionDay)


def test_atem::whentriodionday_constructor_exists():
    assert callable(atem::WhenTriodionDay.__init__)


def test_atem::whentriodionday_constructor_args():
    sig = inspect.signature(atem::WhenTriodionDay.__init__)
    params = list(sig.parameters.keys())



def test_atem::whenperiodcase_is_not_abstract():
    assert not inspect.isabstract(atem::WhenPeriodCase)


def test_atem::whenperiodcase_constructor_exists():
    assert callable(atem::WhenPeriodCase.__init__)


def test_atem::whenperiodcase_constructor_args():
    sig = inspect.signature(atem::WhenPeriodCase.__init__)
    params = list(sig.parameters.keys())



def test_atem::whenpentecostarionday_is_not_abstract():
    assert not inspect.isabstract(atem::WhenPentecostarionDay)


def test_atem::whenpentecostarionday_constructor_exists():
    assert callable(atem::WhenPentecostarionDay.__init__)


def test_atem::whenpentecostarionday_constructor_args():
    sig = inspect.signature(atem::WhenPentecostarionDay.__init__)
    params = list(sig.parameters.keys())



def test_abstractdaynamecase_is_not_abstract():
    assert not inspect.isabstract(AbstractDayNameCase)


def test_abstractdaynamecase_constructor_exists():
    assert callable(AbstractDayNameCase.__init__)


def test_abstractdaynamecase_constructor_args():
    sig = inspect.signature(AbstractDayNameCase.__init__)
    params = list(sig.parameters.keys())



def test_atem::daynameset_is_not_abstract():
    assert not inspect.isabstract(atem::DayNameSet)


def test_atem::daynameset_constructor_exists():
    assert callable(atem::DayNameSet.__init__)


def test_atem::daynameset_constructor_args():
    sig = inspect.signature(atem::DayNameSet.__init__)
    params = list(sig.parameters.keys())
    assert "dslDayNameSet_Values" in params, "Missing parameter 'dslDayNameSet_Values'"

def test_atem::daynameset_has_dslDayNameSet_Values():
    assert hasattr(atem::DayNameSet, "dslDayNameSet_Values")
    descriptor = None
    for klass in atem::DayNameSet.__mro__:
        if "dslDayNameSet_Values" in klass.__dict__:
            descriptor = klass.__dict__["dslDayNameSet_Values"]
            break
    assert isinstance(descriptor, property)



def test_atem::daynamerange_is_not_abstract():
    assert not inspect.isabstract(atem::DayNameRange)


def test_atem::daynamerange_constructor_exists():
    assert callable(atem::DayNameRange.__init__)


def test_atem::daynamerange_constructor_args():
    sig = inspect.signature(atem::DayNameRange.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_DayNameRange_To" in params, "Missing parameter 'dsl_DayNameRange_To'"
    assert "dsl_DayNameRange_from" in params, "Missing parameter 'dsl_DayNameRange_from'"

def test_atem::daynamerange_has_dsl_DayNameRange_To():
    assert hasattr(atem::DayNameRange, "dsl_DayNameRange_To")
    descriptor = None
    for klass in atem::DayNameRange.__mro__:
        if "dsl_DayNameRange_To" in klass.__dict__:
            descriptor = klass.__dict__["dsl_DayNameRange_To"]
            break
    assert isinstance(descriptor, property)

def test_atem::daynamerange_has_dsl_DayNameRange_from():
    assert hasattr(atem::DayNameRange, "dsl_DayNameRange_from")
    descriptor = None
    for klass in atem::DayNameRange.__mro__:
        if "dsl_DayNameRange_from" in klass.__dict__:
            descriptor = klass.__dict__["dsl_DayNameRange_from"]
            break
    assert isinstance(descriptor, property)



def test_atem::abstractdaynamecase_is_not_abstract():
    assert not inspect.isabstract(atem::AbstractDayNameCase)


def test_atem::abstractdaynamecase_constructor_exists():
    assert callable(atem::AbstractDayNameCase.__init__)


def test_atem::abstractdaynamecase_constructor_args():
    sig = inspect.signature(atem::AbstractDayNameCase.__init__)
    params = list(sig.parameters.keys())



def test_atem::whendaynamecase_is_not_abstract():
    assert not inspect.isabstract(atem::WhenDayNameCase)


def test_atem::whendaynamecase_constructor_exists():
    assert callable(atem::WhenDayNameCase.__init__)


def test_atem::whendaynamecase_constructor_args():
    sig = inspect.signature(atem::WhenDayNameCase.__init__)
    params = list(sig.parameters.keys())



def test_atem::whendayname_is_not_abstract():
    assert not inspect.isabstract(atem::WhenDayName)


def test_atem::whendayname_constructor_exists():
    assert callable(atem::WhenDayName.__init__)


def test_atem::whendayname_constructor_args():
    sig = inspect.signature(atem::WhenDayName.__init__)
    params = list(sig.parameters.keys())



def test_atem::abstractdatecase_is_not_abstract():
    assert not inspect.isabstract(atem::AbstractDateCase)


def test_atem::abstractdatecase_constructor_exists():
    assert callable(atem::AbstractDateCase.__init__)


def test_atem::abstractdatecase_constructor_args():
    sig = inspect.signature(atem::AbstractDateCase.__init__)
    params = list(sig.parameters.keys())



def test_atem::whenother_is_not_abstract():
    assert not inspect.isabstract(atem::WhenOther)


def test_atem::whenother_constructor_exists():
    assert callable(atem::WhenOther.__init__)


def test_atem::whenother_constructor_args():
    sig = inspect.signature(atem::WhenOther.__init__)
    params = list(sig.parameters.keys())



def test_atem::whendatecase_is_not_abstract():
    assert not inspect.isabstract(atem::WhenDateCase)


def test_atem::whendatecase_constructor_exists():
    assert callable(atem::WhenDateCase.__init__)


def test_atem::whendatecase_constructor_args():
    sig = inspect.signature(atem::WhenDateCase.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_WhenDate_Case_Month" in params, "Missing parameter 'dsl_WhenDate_Case_Month'"

def test_atem::whendatecase_has_dsl_WhenDate_Case_Month():
    assert hasattr(atem::WhenDateCase, "dsl_WhenDate_Case_Month")
    descriptor = None
    for klass in atem::WhenDateCase.__mro__:
        if "dsl_WhenDate_Case_Month" in klass.__dict__:
            descriptor = klass.__dict__["dsl_WhenDate_Case_Month"]
            break
    assert isinstance(descriptor, property)



def test_atem::whendate_is_not_abstract():
    assert not inspect.isabstract(atem::WhenDate)


def test_atem::whendate_constructor_exists():
    assert callable(atem::WhenDate.__init__)


def test_atem::whendate_constructor_args():
    sig = inspect.signature(atem::WhenDate.__init__)
    params = list(sig.parameters.keys())



def test_atem::restorelocale_is_not_abstract():
    assert not inspect.isabstract(atem::RestoreLocale)


def test_atem::restorelocale_constructor_exists():
    assert callable(atem::RestoreLocale.__init__)


def test_atem::restorelocale_constructor_args():
    sig = inspect.signature(atem::RestoreLocale.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_RestoreLocale" in params, "Missing parameter 'dsl_RestoreLocale'"

def test_atem::restorelocale_has_dsl_RestoreLocale():
    assert hasattr(atem::RestoreLocale, "dsl_RestoreLocale")
    descriptor = None
    for klass in atem::RestoreLocale.__mro__:
        if "dsl_RestoreLocale" in klass.__dict__:
            descriptor = klass.__dict__["dsl_RestoreLocale"]
            break
    assert isinstance(descriptor, property)



def test_atem::dialog_is_not_abstract():
    assert not inspect.isabstract(atem::Dialog)


def test_atem::dialog_constructor_exists():
    assert callable(atem::Dialog.__init__)


def test_atem::dialog_constructor_args():
    sig = inspect.signature(atem::Dialog.__init__)
    params = list(sig.parameters.keys())



def test_atem::rubric_is_not_abstract():
    assert not inspect.isabstract(atem::Rubric)


def test_atem::rubric_constructor_exists():
    assert callable(atem::Rubric.__init__)


def test_atem::rubric_constructor_args():
    sig = inspect.signature(atem::Rubric.__init__)
    params = list(sig.parameters.keys())



def test_atem::setlocale_is_not_abstract():
    assert not inspect.isabstract(atem::SetLocale)


def test_atem::setlocale_constructor_exists():
    assert callable(atem::SetLocale.__init__)


def test_atem::setlocale_constructor_args():
    sig = inspect.signature(atem::SetLocale.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_SetLocale_V1" in params, "Missing parameter 'dsl_SetLocale_V1'"
    assert "dsl_SetLocale_V2" in params, "Missing parameter 'dsl_SetLocale_V2'"

def test_atem::setlocale_has_dsl_SetLocale_V1():
    assert hasattr(atem::SetLocale, "dsl_SetLocale_V1")
    descriptor = None
    for klass in atem::SetLocale.__mro__:
        if "dsl_SetLocale_V1" in klass.__dict__:
            descriptor = klass.__dict__["dsl_SetLocale_V1"]
            break
    assert isinstance(descriptor, property)

def test_atem::setlocale_has_dsl_SetLocale_V2():
    assert hasattr(atem::SetLocale, "dsl_SetLocale_V2")
    descriptor = None
    for klass in atem::SetLocale.__mro__:
        if "dsl_SetLocale_V2" in klass.__dict__:
            descriptor = klass.__dict__["dsl_SetLocale_V2"]
            break
    assert isinstance(descriptor, property)



def test_atem::litbook_is_not_abstract():
    assert not inspect.isabstract(atem::LitBook)


def test_atem::litbook_constructor_exists():
    assert callable(atem::LitBook.__init__)


def test_atem::litbook_constructor_args():
    sig = inspect.signature(atem::LitBook.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atem::litbook_has_name():
    assert hasattr(atem::LitBook, "name")
    descriptor = None
    for klass in atem::LitBook.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atem::version_is_not_abstract():
    assert not inspect.isabstract(atem::Version)


def test_atem::version_constructor_exists():
    assert callable(atem::Version.__init__)


def test_atem::version_constructor_args():
    sig = inspect.signature(atem::Version.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atem::version_has_name():
    assert hasattr(atem::Version, "name")
    descriptor = None
    for klass in atem::Version.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atem::aid_is_not_abstract():
    assert not inspect.isabstract(atem::Aid)


def test_atem::aid_constructor_exists():
    assert callable(atem::Aid.__init__)


def test_atem::aid_constructor_args():
    sig = inspect.signature(atem::Aid.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atem::aid_has_name():
    assert hasattr(atem::Aid, "name")
    descriptor = None
    for klass in atem::Aid.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atem::heading3_is_not_abstract():
    assert not inspect.isabstract(atem::Heading3)


def test_atem::heading3_constructor_exists():
    assert callable(atem::Heading3.__init__)


def test_atem::heading3_constructor_args():
    sig = inspect.signature(atem::Heading3.__init__)
    params = list(sig.parameters.keys())



def test_atem::heading2_is_not_abstract():
    assert not inspect.isabstract(atem::Heading2)


def test_atem::heading2_constructor_exists():
    assert callable(atem::Heading2.__init__)


def test_atem::heading2_constructor_args():
    sig = inspect.signature(atem::Heading2.__init__)
    params = list(sig.parameters.keys())



def test_atem::heading1_is_not_abstract():
    assert not inspect.isabstract(atem::Heading1)


def test_atem::heading1_constructor_exists():
    assert callable(atem::Heading1.__init__)


def test_atem::heading1_constructor_args():
    sig = inspect.signature(atem::Heading1.__init__)
    params = list(sig.parameters.keys())



def test_atem::reading_is_not_abstract():
    assert not inspect.isabstract(atem::Reading)


def test_atem::reading_constructor_exists():
    assert callable(atem::Reading.__init__)


def test_atem::reading_constructor_args():
    sig = inspect.signature(atem::Reading.__init__)
    params = list(sig.parameters.keys())



def test_atem::block_is_not_abstract():
    assert not inspect.isabstract(atem::Block)


def test_atem::block_constructor_exists():
    assert callable(atem::Block.__init__)


def test_atem::block_constructor_args():
    sig = inspect.signature(atem::Block.__init__)
    params = list(sig.parameters.keys())



def test_atem::actor_is_not_abstract():
    assert not inspect.isabstract(atem::Actor)


def test_atem::actor_constructor_exists():
    assert callable(atem::Actor.__init__)


def test_atem::actor_constructor_args():
    sig = inspect.signature(atem::Actor.__init__)
    params = list(sig.parameters.keys())



def test_atem::paragraph_is_not_abstract():
    assert not inspect.isabstract(atem::Paragraph)


def test_atem::paragraph_constructor_exists():
    assert callable(atem::Paragraph.__init__)


def test_atem::paragraph_constructor_args():
    sig = inspect.signature(atem::Paragraph.__init__)
    params = list(sig.parameters.keys())



def test_atem::verse_is_not_abstract():
    assert not inspect.isabstract(atem::Verse)


def test_atem::verse_constructor_exists():
    assert callable(atem::Verse.__init__)


def test_atem::verse_constructor_args():
    sig = inspect.signature(atem::Verse.__init__)
    params = list(sig.parameters.keys())



def test_atem::media_is_not_abstract():
    assert not inspect.isabstract(atem::Media)


def test_atem::media_constructor_exists():
    assert callable(atem::Media.__init__)


def test_atem::media_constructor_args():
    sig = inspect.signature(atem::Media.__init__)
    params = list(sig.parameters.keys())



def test_atem::hymn_is_not_abstract():
    assert not inspect.isabstract(atem::Hymn)


def test_atem::hymn_constructor_exists():
    assert callable(atem::Hymn.__init__)


def test_atem::hymn_constructor_args():
    sig = inspect.signature(atem::Hymn.__init__)
    params = list(sig.parameters.keys())



def test_atem::passthroughhtml_is_not_abstract():
    assert not inspect.isabstract(atem::PassThroughHtml)


def test_atem::passthroughhtml_constructor_exists():
    assert callable(atem::PassThroughHtml.__init__)


def test_atem::passthroughhtml_constructor_args():
    sig = inspect.signature(atem::PassThroughHtml.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Passthrough_html_text" in params, "Missing parameter 'dsl_Passthrough_html_text'"

def test_atem::passthroughhtml_has_dsl_Passthrough_html_text():
    assert hasattr(atem::PassThroughHtml, "dsl_Passthrough_html_text")
    descriptor = None
    for klass in atem::PassThroughHtml.__mro__:
        if "dsl_Passthrough_html_text" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Passthrough_html_text"]
            break
    assert isinstance(descriptor, property)



def test_atem::pagenumber_is_not_abstract():
    assert not inspect.isabstract(atem::PageNumber)


def test_atem::pagenumber_constructor_exists():
    assert callable(atem::PageNumber.__init__)


def test_atem::pagenumber_constructor_args():
    sig = inspect.signature(atem::PageNumber.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_PageNumber_value" in params, "Missing parameter 'dsl_PageNumber_value'"

def test_atem::pagenumber_has_dsl_PageNumber_value():
    assert hasattr(atem::PageNumber, "dsl_PageNumber_value")
    descriptor = None
    for klass in atem::PageNumber.__mro__:
        if "dsl_PageNumber_value" in klass.__dict__:
            descriptor = klass.__dict__["dsl_PageNumber_value"]
            break
    assert isinstance(descriptor, property)

def test_language_exists():
    # Check that the Enumeration exists
    assert Language is not None

def test_language_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Language]
    expected_literals = [
        "L2",
        "L1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Language"

def test_booktypes_exists():
    # Check that the Enumeration exists
    assert BookTypes is not None

def test_booktypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookTypes]
    expected_literals = [
        "Heirmologion",
        "Lectionary",
        "Horologion",
        "Other",
        "Euchologion",
        "Katavasias",
        "Pentecostarion",
        "Triodion",
        "Psalter",
        "Menaion",
        "Eothina",
        "Octochechos",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BookTypes"

def test_dayofweek_exists():
    # Check that the Enumeration exists
    assert DayOfWeek is not None

def test_dayofweek_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DayOfWeek]
    expected_literals = [
        "Saturday",
        "Monday",
        "Wednesday",
        "Thursday",
        "Sunday",
        "Tuesday",
        "Friday",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DayOfWeek"

def test_seasons_exists():
    # Check that the Enumeration exists
    assert Seasons is not None

def test_seasons_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Seasons]
    expected_literals = [
        "Apostles_Fast",
        "Dormition_Fast",
        "Nativity_Fast",
        "Pentecostarion",
        "Triodion",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Seasons"

def test_dowtypes_exists():
    # Check that the Enumeration exists
    assert DowTypes is not None

def test_dowtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DowTypes]
    expected_literals = [
        "D4",
        "D7",
        "D5",
        "D6",
        "D1",
        "D3",
        "D2",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DowTypes"

def test_versionswitchtype_exists():
    # Check that the Enumeration exists
    assert VersionSwitchType is not None

def test_versionswitchtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VersionSwitchType]
    expected_literals = [
        "L1",
        "L2",
        "Both",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VersionSwitchType"

def test_breaktype_exists():
    # Check that the Enumeration exists
    assert BreakType is not None

def test_breaktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BreakType]
    expected_literals = [
        "page",
        "line",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BreakType"

def test_monthname_exists():
    # Check that the Enumeration exists
    assert MonthName is not None

def test_monthname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MonthName]
    expected_literals = [
        "Sep",
        "Apr",
        "Jun",
        "Nov",
        "Oct",
        "Dec",
        "Aug",
        "Jan",
        "Feb",
        "Jul",
        "Mar",
        "May",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MonthName"

def test_dayofmonthtypes_exists():
    # Check that the Enumeration exists
    assert DayOfMonthTypes is not None

def test_dayofmonthtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DayOfMonthTypes]
    expected_literals = [
        "D22",
        "D28",
        "D25",
        "D01",
        "D07",
        "D23",
        "D31",
        "D06",
        "D05",
        "D19",
        "D02",
        "D04",
        "D29",
        "D24",
        "D15",
        "D20",
        "D26",
        "D17",
        "D10",
        "D11",
        "D21",
        "D09",
        "D03",
        "D13",
        "D12",
        "D30",
        "D16",
        "D08",
        "D27",
        "D18",
        "D14",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DayOfMonthTypes"

def test_periodtype_exists():
    # Check that the Enumeration exists
    assert PeriodType is not None

def test_periodtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PeriodType]
    expected_literals = [
        "triodion",
        "pentecostarion",
        "pascha",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PeriodType"

def test_templatestatuses_exists():
    # Check that the Enumeration exists
    assert TemplateStatuses is not None

def test_templatestatuses_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TemplateStatuses]
    expected_literals = [
        "Final",
        "Review",
        "NA",
        "Draft",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TemplateStatuses"

def test_null_exists():
    # Check that the Enumeration exists
    assert Null is not None

def test_null_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Null]
    expected_literals = [
        "null",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Null"

def test_modetypes_exists():
    # Check that the Enumeration exists
    assert ModeTypes is not None

def test_modetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModeTypes]
    expected_literals = [
        "M2",
        "M4",
        "M3",
        "M6",
        "M5",
        "M1",
        "M7",
        "M8",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModeTypes"


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
atem::PrefaceFragment_strategy = st.builds(
    atem::PrefaceFragment,
)
LdpType_strategy = st.builds(
    LdpType,
)
atem::GenDate_strategy = st.builds(
    atem::GenDate,
    dsl_Display_Date=
        st.booleans()
)
atem::SBT_strategy = st.builds(
    atem::SBT,
    dsl_Display_SundaysBeforeTriodion=
        st.booleans()
)
atem::NOP_strategy = st.builds(
    atem::NOP,
    dsl_Display_Mode=
        st.booleans()
)
atem::DOL_strategy = st.builds(
    atem::DOL,
    dsl_Display_DayLukan=
        st.booleans()
)
atem::MOW_strategy = st.builds(
    atem::MOW,
    dsl_Display_Mode=
        st.booleans()
)
atem::WDOLC_strategy = st.builds(
    atem::WDOLC,
    dsl_Display_DayLukan=
        st.booleans()
)
atem::WOLC_strategy = st.builds(
    atem::WOLC,
    dsl_Display_DayLukan=
        st.booleans()
)
atem::MCD_strategy = st.builds(
    atem::MCD,
    dsl_MCD_value=
        st.booleans()
)
atem::DOM_strategy = st.builds(
    atem::DOM,
    dsl_Display_Mode=
        st.booleans()
)
atem::GenYear_strategy = st.builds(
    atem::GenYear,
    dsl_Display_Year=
        st.booleans()
)
atem::All_strategy = st.builds(
    atem::All,
    dsl_Display_LiturgicalDayProperties=
        st.booleans()
)
atem::SectionElementType_strategy = st.builds(
    atem::SectionElementType,
)
atem::PrefaceElementType_strategy = st.builds(
    atem::PrefaceElementType,
)
atem::SOL_strategy = st.builds(
    atem::SOL,
    dsl_Display_StartLukan=
        st.booleans()
)
atem::SAEC_strategy = st.builds(
    atem::SAEC,
    dsl_Display_SundayAfterElevationCross=
        st.booleans()
)
atem::EOW_strategy = st.builds(
    atem::EOW,
    dsl_Display_Eothinon=
        st.booleans()
)
atem::DOWT_strategy = st.builds(
    atem::DOWT,
    dsl_Display_Mode=
        st.booleans()
)
atem::DOWN_strategy = st.builds(
    atem::DOWN,
    dsl_Display_Mode=
        st.booleans()
)
atem::DOP_strategy = st.builds(
    atem::DOP,
    dsl_Display_Mode=
        st.booleans()
)
atem::LdpType_strategy = st.builds(
    atem::LdpType,
)
atem::Definition_strategy = st.builds(
    atem::Definition,
)
ElementType_strategy = st.builds(
    ElementType,
)
atem::TaggedText_strategy = st.builds(
    atem::TaggedText,
)
atem::LDP_strategy = st.builds(
    atem::LDP,
)
atem::Lookup_strategy = st.builds(
    atem::Lookup,
    dsl_Lookup_Override_Mode_Set=
        st.booleans(),
    dsl_Lookup_OverrideDay=
        safe_text,
    dsl_Lookup_OverrideMode=
        safe_text,
    dsl_Lookup_Override__Day_Set=
        st.booleans(),
    dsl_Lookup_Media_Off=
        st.booleans()
)
atem::ResourceText_strategy = st.builds(
    atem::ResourceText,
    dsl_ResourceText_Media_Off=
        st.booleans()
)
SectionElementType_strategy = st.builds(
    SectionElementType,
)
atem::InfoElementType_strategy = st.builds(
    atem::InfoElementType,
)
atem::ElementType_strategy = st.builds(
    atem::ElementType,
)
HeaderFooterFragment_strategy = st.builds(
    HeaderFooterFragment,
)
atem::HeaderFooterCommemoration_strategy = st.builds(
    atem::HeaderFooterCommemoration,
    dsl_HeaderFooterCommemoration=
        st.booleans()
)
atem::HeaderFooterDate_strategy = st.builds(
    atem::HeaderFooterDate,
    dsl_HeaderFooterDate=
        st.booleans(),
    dsl_HeaderFooterDate_Language=
        safe_text
)
atem::HeaderFooterLookup_strategy = st.builds(
    atem::HeaderFooterLookup,
    dsl_HeaderFooterLookup_Language=
        safe_text
)
atem::HeaderFooterPageNumber_strategy = st.builds(
    atem::HeaderFooterPageNumber,
    dsl_HeaderFooterPageNumber=
        st.booleans()
)
atem::HeaderFooterTitle_strategy = st.builds(
    atem::HeaderFooterTitle,
    dsl_HeaderFooterTitle=
        st.booleans()
)
atem::HeaderFooterText_strategy = st.builds(
    atem::HeaderFooterText,
    dsl_HeaderFooterText=
        safe_text
)
HeaderFooterColumn_strategy = st.builds(
    HeaderFooterColumn,
)
atem::HeaderFooterColumnCenter_strategy = st.builds(
    atem::HeaderFooterColumnCenter,
)
atem::HeaderFooterColumnRight_strategy = st.builds(
    atem::HeaderFooterColumnRight,
)
atem::HeaderFooterColumnLeft_strategy = st.builds(
    atem::HeaderFooterColumnLeft,
)
PrefaceElementType_strategy = st.builds(
    PrefaceElementType,
)
InfoElementType_strategy = st.builds(
    InfoElementType,
)
AbstractComponent_strategy = st.builds(
    AbstractComponent,
)
atem::Section_strategy = st.builds(
    atem::Section,
    name=
        safe_text
)
atem::Info_strategy = st.builds(
    atem::Info,
    name=
        safe_text
)
atem::TemplateFragment_strategy = st.builds(
    atem::TemplateFragment,
)
atem::Break_strategy = st.builds(
    atem::Break,
    dsl_break_type=
        safe_text
)
atem::Title_strategy = st.builds(
    atem::Title,
)
atem::SubTitle_strategy = st.builds(
    atem::SubTitle,
)
atem::PassThroughPdf_strategy = st.builds(
    atem::PassThroughPdf,
    dsl_Passthrough_pdf_text=
        safe_text
)
atem::SectionFragment_strategy = st.builds(
    atem::SectionFragment,
)
atem::VersionSwitch_strategy = st.builds(
    atem::VersionSwitch,
    dsl_VersionSwitch_flag=
        safe_text
)
HeadComponent_strategy = st.builds(
    HeadComponent,
)
atem::Date_strategy = st.builds(
    atem::Date,
    dsl_Date_month=
        st.integers(),
    dsl_Date_day=
        st.integers(),
    dsl_Date_year=
        st.integers()
)
atem::Commemoration_strategy = st.builds(
    atem::Commemoration,
)
atem::PageFooterOdd_strategy = st.builds(
    atem::PageFooterOdd,
)
atem::TemplateTitle_strategy = st.builds(
    atem::TemplateTitle,
)
atem::PageFooterEven_strategy = st.builds(
    atem::PageFooterEven,
)
atem::PageHeaderOdd_strategy = st.builds(
    atem::PageHeaderOdd,
)
atem::HeaderFooterColumn_strategy = st.builds(
    atem::HeaderFooterColumn,
)
atem::PageHeaderEven_strategy = st.builds(
    atem::PageHeaderEven,
)
atem::PageKeepWithNext_strategy = st.builds(
    atem::PageKeepWithNext,
    dsl_PageKeepWithNext_value=
        safe_text
)
atem::HeaderFooterFragment_strategy = st.builds(
    atem::HeaderFooterFragment,
)
atem::Preface_strategy = st.builds(
    atem::Preface,
    name=
        safe_text
)
atem::Head_strategy = st.builds(
    atem::Head,
)
atem::Driver_strategy = st.builds(
    atem::Driver,
    dsl_Driver_RegEx=
        safe_text,
    dsl_Driver_Status=
        safe_text
)
atem::Import_strategy = st.builds(
    atem::Import,
    importedNamespace=
        safe_text
)
atem::TemplateStatus_strategy = st.builds(
    atem::TemplateStatus,
    dsl_TemplateStatus=
        safe_text
)
atem::AtemModel_strategy = st.builds(
    atem::AtemModel,
    name=
        safe_text
)
atem::HeadComponent_strategy = st.builds(
    atem::HeadComponent,
)
atem::AbstractComponent_strategy = st.builds(
    atem::AbstractComponent,
)
atem::WhenExists_strategy = st.builds(
    atem::WhenExists,
)
atem::WhenExistsCase_strategy = st.builds(
    atem::WhenExistsCase,
)
atem::WhenModeOfWeekCase_strategy = st.builds(
    atem::WhenModeOfWeekCase,
)
atem::WhenModeOfWeek_strategy = st.builds(
    atem::WhenModeOfWeek,
)
atem::SundaysBeforeTriodionCase_strategy = st.builds(
    atem::SundaysBeforeTriodionCase,
    dsl_SundaysBeforeTriodionCase_Days=
        st.integers()
)
atem::WhenSundaysBeforeTriodion_strategy = st.builds(
    atem::WhenSundaysBeforeTriodion,
)
atem::ModeOfWeekSet_strategy = st.builds(
    atem::ModeOfWeekSet,
    dsl_ModeOfWeekSet_MOWs=
        safe_text
)
atem::WhenMovableCycleDay_strategy = st.builds(
    atem::WhenMovableCycleDay,
)
AbstractDayCase_strategy = st.builds(
    AbstractDayCase,
)
atem::DaySet_strategy = st.builds(
    atem::DaySet,
    dslSetValue_Days=
        st.integers()
)
atem::DayRange_strategy = st.builds(
    atem::DayRange,
    dsl_Range_To=
        st.integers(),
    dsl_DayRange_from=
        st.integers()
)
atem::AbstractDayCase_strategy = st.builds(
    atem::AbstractDayCase,
)
atem::WhenPascha_strategy = st.builds(
    atem::WhenPascha,
)
atem::WhenLukanCycleDay_strategy = st.builds(
    atem::WhenLukanCycleDay,
)
atem::WhenSundayAfterElevationOfCrossDay_strategy = st.builds(
    atem::WhenSundayAfterElevationOfCrossDay,
)
AbstractDateCase_strategy = st.builds(
    AbstractDateCase,
)
atem::DateSet_strategy = st.builds(
    atem::DateSet,
    dslDateSet_Values=
        st.integers()
)
atem::DateRange_strategy = st.builds(
    atem::DateRange,
    dsl_DateRange_To=
        st.integers(),
    dsl_DateRange_from=
        st.integers()
)
atem::WhenTriodionDay_strategy = st.builds(
    atem::WhenTriodionDay,
)
atem::WhenPeriodCase_strategy = st.builds(
    atem::WhenPeriodCase,
)
atem::WhenPentecostarionDay_strategy = st.builds(
    atem::WhenPentecostarionDay,
)
AbstractDayNameCase_strategy = st.builds(
    AbstractDayNameCase,
)
atem::DayNameSet_strategy = st.builds(
    atem::DayNameSet,
    dslDayNameSet_Values=
        safe_text
)
atem::DayNameRange_strategy = st.builds(
    atem::DayNameRange,
    dsl_DayNameRange_To=
        safe_text,
    dsl_DayNameRange_from=
        safe_text
)
atem::AbstractDayNameCase_strategy = st.builds(
    atem::AbstractDayNameCase,
)
atem::WhenDayNameCase_strategy = st.builds(
    atem::WhenDayNameCase,
)
atem::WhenDayName_strategy = st.builds(
    atem::WhenDayName,
)
atem::AbstractDateCase_strategy = st.builds(
    atem::AbstractDateCase,
)
atem::WhenOther_strategy = st.builds(
    atem::WhenOther,
)
atem::WhenDateCase_strategy = st.builds(
    atem::WhenDateCase,
    dsl_WhenDate_Case_Month=
        safe_text
)
atem::WhenDate_strategy = st.builds(
    atem::WhenDate,
)
atem::RestoreLocale_strategy = st.builds(
    atem::RestoreLocale,
    dsl_RestoreLocale=
        st.booleans()
)
atem::Dialog_strategy = st.builds(
    atem::Dialog,
)
atem::Rubric_strategy = st.builds(
    atem::Rubric,
)
atem::SetLocale_strategy = st.builds(
    atem::SetLocale,
    dsl_SetLocale_V1=
        safe_text,
    dsl_SetLocale_V2=
        safe_text
)
atem::LitBook_strategy = st.builds(
    atem::LitBook,
    name=
        safe_text
)
atem::Version_strategy = st.builds(
    atem::Version,
    name=
        safe_text
)
atem::Aid_strategy = st.builds(
    atem::Aid,
    name=
        safe_text
)
atem::Heading3_strategy = st.builds(
    atem::Heading3,
)
atem::Heading2_strategy = st.builds(
    atem::Heading2,
)
atem::Heading1_strategy = st.builds(
    atem::Heading1,
)
atem::Reading_strategy = st.builds(
    atem::Reading,
)
atem::Block_strategy = st.builds(
    atem::Block,
)
atem::Actor_strategy = st.builds(
    atem::Actor,
)
atem::Paragraph_strategy = st.builds(
    atem::Paragraph,
)
atem::Verse_strategy = st.builds(
    atem::Verse,
)
atem::Media_strategy = st.builds(
    atem::Media,
)
atem::Hymn_strategy = st.builds(
    atem::Hymn,
)
atem::PassThroughHtml_strategy = st.builds(
    atem::PassThroughHtml,
    dsl_Passthrough_html_text=
        safe_text
)
atem::PageNumber_strategy = st.builds(
    atem::PageNumber,
    dsl_PageNumber_value=
        st.integers()
)

@given(instance=atem::PrefaceFragment_strategy)
@settings(max_examples=50)
def test_atem::prefacefragment_instantiation(instance):
    assert isinstance(instance, atem::PrefaceFragment)

@given(instance=LdpType_strategy)
@settings(max_examples=50)
def test_ldptype_instantiation(instance):
    assert isinstance(instance, LdpType)

@given(instance=atem::GenDate_strategy)
@settings(max_examples=50)
def test_atem::gendate_instantiation(instance):
    assert isinstance(instance, atem::GenDate)

@given(instance=atem::GenDate_strategy)
def test_atem::gendate_dsl_Display_Date_type(instance):
    assert isinstance(instance.dsl_Display_Date, bool)


@given(instance=atem::GenDate_strategy)
def test_atem::gendate_dsl_Display_Date_setter(instance):
    original = instance.dsl_Display_Date
    instance.dsl_Display_Date = original
    assert instance.dsl_Display_Date == original

@given(instance=atem::SBT_strategy)
@settings(max_examples=50)
def test_atem::sbt_instantiation(instance):
    assert isinstance(instance, atem::SBT)

@given(instance=atem::SBT_strategy)
def test_atem::sbt_dsl_Display_SundaysBeforeTriodion_type(instance):
    assert isinstance(instance.dsl_Display_SundaysBeforeTriodion, bool)


@given(instance=atem::SBT_strategy)
def test_atem::sbt_dsl_Display_SundaysBeforeTriodion_setter(instance):
    original = instance.dsl_Display_SundaysBeforeTriodion
    instance.dsl_Display_SundaysBeforeTriodion = original
    assert instance.dsl_Display_SundaysBeforeTriodion == original

@given(instance=atem::NOP_strategy)
@settings(max_examples=50)
def test_atem::nop_instantiation(instance):
    assert isinstance(instance, atem::NOP)

@given(instance=atem::NOP_strategy)
def test_atem::nop_dsl_Display_Mode_type(instance):
    assert isinstance(instance.dsl_Display_Mode, bool)


@given(instance=atem::NOP_strategy)
def test_atem::nop_dsl_Display_Mode_setter(instance):
    original = instance.dsl_Display_Mode
    instance.dsl_Display_Mode = original
    assert instance.dsl_Display_Mode == original

@given(instance=atem::DOL_strategy)
@settings(max_examples=50)
def test_atem::dol_instantiation(instance):
    assert isinstance(instance, atem::DOL)

@given(instance=atem::DOL_strategy)
def test_atem::dol_dsl_Display_DayLukan_type(instance):
    assert isinstance(instance.dsl_Display_DayLukan, bool)


@given(instance=atem::DOL_strategy)
def test_atem::dol_dsl_Display_DayLukan_setter(instance):
    original = instance.dsl_Display_DayLukan
    instance.dsl_Display_DayLukan = original
    assert instance.dsl_Display_DayLukan == original

@given(instance=atem::MOW_strategy)
@settings(max_examples=50)
def test_atem::mow_instantiation(instance):
    assert isinstance(instance, atem::MOW)

@given(instance=atem::MOW_strategy)
def test_atem::mow_dsl_Display_Mode_type(instance):
    assert isinstance(instance.dsl_Display_Mode, bool)


@given(instance=atem::MOW_strategy)
def test_atem::mow_dsl_Display_Mode_setter(instance):
    original = instance.dsl_Display_Mode
    instance.dsl_Display_Mode = original
    assert instance.dsl_Display_Mode == original

@given(instance=atem::WDOLC_strategy)
@settings(max_examples=50)
def test_atem::wdolc_instantiation(instance):
    assert isinstance(instance, atem::WDOLC)

@given(instance=atem::WDOLC_strategy)
def test_atem::wdolc_dsl_Display_DayLukan_type(instance):
    assert isinstance(instance.dsl_Display_DayLukan, bool)


@given(instance=atem::WDOLC_strategy)
def test_atem::wdolc_dsl_Display_DayLukan_setter(instance):
    original = instance.dsl_Display_DayLukan
    instance.dsl_Display_DayLukan = original
    assert instance.dsl_Display_DayLukan == original

@given(instance=atem::WOLC_strategy)
@settings(max_examples=50)
def test_atem::wolc_instantiation(instance):
    assert isinstance(instance, atem::WOLC)

@given(instance=atem::WOLC_strategy)
def test_atem::wolc_dsl_Display_DayLukan_type(instance):
    assert isinstance(instance.dsl_Display_DayLukan, bool)


@given(instance=atem::WOLC_strategy)
def test_atem::wolc_dsl_Display_DayLukan_setter(instance):
    original = instance.dsl_Display_DayLukan
    instance.dsl_Display_DayLukan = original
    assert instance.dsl_Display_DayLukan == original

@given(instance=atem::MCD_strategy)
@settings(max_examples=50)
def test_atem::mcd_instantiation(instance):
    assert isinstance(instance, atem::MCD)

@given(instance=atem::MCD_strategy)
def test_atem::mcd_dsl_MCD_value_type(instance):
    assert isinstance(instance.dsl_MCD_value, bool)


@given(instance=atem::MCD_strategy)
def test_atem::mcd_dsl_MCD_value_setter(instance):
    original = instance.dsl_MCD_value
    instance.dsl_MCD_value = original
    assert instance.dsl_MCD_value == original

@given(instance=atem::DOM_strategy)
@settings(max_examples=50)
def test_atem::dom_instantiation(instance):
    assert isinstance(instance, atem::DOM)

@given(instance=atem::DOM_strategy)
def test_atem::dom_dsl_Display_Mode_type(instance):
    assert isinstance(instance.dsl_Display_Mode, bool)


@given(instance=atem::DOM_strategy)
def test_atem::dom_dsl_Display_Mode_setter(instance):
    original = instance.dsl_Display_Mode
    instance.dsl_Display_Mode = original
    assert instance.dsl_Display_Mode == original

@given(instance=atem::GenYear_strategy)
@settings(max_examples=50)
def test_atem::genyear_instantiation(instance):
    assert isinstance(instance, atem::GenYear)

@given(instance=atem::GenYear_strategy)
def test_atem::genyear_dsl_Display_Year_type(instance):
    assert isinstance(instance.dsl_Display_Year, bool)


@given(instance=atem::GenYear_strategy)
def test_atem::genyear_dsl_Display_Year_setter(instance):
    original = instance.dsl_Display_Year
    instance.dsl_Display_Year = original
    assert instance.dsl_Display_Year == original

@given(instance=atem::All_strategy)
@settings(max_examples=50)
def test_atem::all_instantiation(instance):
    assert isinstance(instance, atem::All)

@given(instance=atem::All_strategy)
def test_atem::all_dsl_Display_LiturgicalDayProperties_type(instance):
    assert isinstance(instance.dsl_Display_LiturgicalDayProperties, bool)


@given(instance=atem::All_strategy)
def test_atem::all_dsl_Display_LiturgicalDayProperties_setter(instance):
    original = instance.dsl_Display_LiturgicalDayProperties
    instance.dsl_Display_LiturgicalDayProperties = original
    assert instance.dsl_Display_LiturgicalDayProperties == original

@given(instance=atem::SectionElementType_strategy)
@settings(max_examples=50)
def test_atem::sectionelementtype_instantiation(instance):
    assert isinstance(instance, atem::SectionElementType)

@given(instance=atem::PrefaceElementType_strategy)
@settings(max_examples=50)
def test_atem::prefaceelementtype_instantiation(instance):
    assert isinstance(instance, atem::PrefaceElementType)

@given(instance=atem::SOL_strategy)
@settings(max_examples=50)
def test_atem::sol_instantiation(instance):
    assert isinstance(instance, atem::SOL)

@given(instance=atem::SOL_strategy)
def test_atem::sol_dsl_Display_StartLukan_type(instance):
    assert isinstance(instance.dsl_Display_StartLukan, bool)


@given(instance=atem::SOL_strategy)
def test_atem::sol_dsl_Display_StartLukan_setter(instance):
    original = instance.dsl_Display_StartLukan
    instance.dsl_Display_StartLukan = original
    assert instance.dsl_Display_StartLukan == original

@given(instance=atem::SAEC_strategy)
@settings(max_examples=50)
def test_atem::saec_instantiation(instance):
    assert isinstance(instance, atem::SAEC)

@given(instance=atem::SAEC_strategy)
def test_atem::saec_dsl_Display_SundayAfterElevationCross_type(instance):
    assert isinstance(instance.dsl_Display_SundayAfterElevationCross, bool)


@given(instance=atem::SAEC_strategy)
def test_atem::saec_dsl_Display_SundayAfterElevationCross_setter(instance):
    original = instance.dsl_Display_SundayAfterElevationCross
    instance.dsl_Display_SundayAfterElevationCross = original
    assert instance.dsl_Display_SundayAfterElevationCross == original

@given(instance=atem::EOW_strategy)
@settings(max_examples=50)
def test_atem::eow_instantiation(instance):
    assert isinstance(instance, atem::EOW)

@given(instance=atem::EOW_strategy)
def test_atem::eow_dsl_Display_Eothinon_type(instance):
    assert isinstance(instance.dsl_Display_Eothinon, bool)


@given(instance=atem::EOW_strategy)
def test_atem::eow_dsl_Display_Eothinon_setter(instance):
    original = instance.dsl_Display_Eothinon
    instance.dsl_Display_Eothinon = original
    assert instance.dsl_Display_Eothinon == original

@given(instance=atem::DOWT_strategy)
@settings(max_examples=50)
def test_atem::dowt_instantiation(instance):
    assert isinstance(instance, atem::DOWT)

@given(instance=atem::DOWT_strategy)
def test_atem::dowt_dsl_Display_Mode_type(instance):
    assert isinstance(instance.dsl_Display_Mode, bool)


@given(instance=atem::DOWT_strategy)
def test_atem::dowt_dsl_Display_Mode_setter(instance):
    original = instance.dsl_Display_Mode
    instance.dsl_Display_Mode = original
    assert instance.dsl_Display_Mode == original

@given(instance=atem::DOWN_strategy)
@settings(max_examples=50)
def test_atem::down_instantiation(instance):
    assert isinstance(instance, atem::DOWN)

@given(instance=atem::DOWN_strategy)
def test_atem::down_dsl_Display_Mode_type(instance):
    assert isinstance(instance.dsl_Display_Mode, bool)


@given(instance=atem::DOWN_strategy)
def test_atem::down_dsl_Display_Mode_setter(instance):
    original = instance.dsl_Display_Mode
    instance.dsl_Display_Mode = original
    assert instance.dsl_Display_Mode == original

@given(instance=atem::DOP_strategy)
@settings(max_examples=50)
def test_atem::dop_instantiation(instance):
    assert isinstance(instance, atem::DOP)

@given(instance=atem::DOP_strategy)
def test_atem::dop_dsl_Display_Mode_type(instance):
    assert isinstance(instance.dsl_Display_Mode, bool)


@given(instance=atem::DOP_strategy)
def test_atem::dop_dsl_Display_Mode_setter(instance):
    original = instance.dsl_Display_Mode
    instance.dsl_Display_Mode = original
    assert instance.dsl_Display_Mode == original

@given(instance=atem::LdpType_strategy)
@settings(max_examples=50)
def test_atem::ldptype_instantiation(instance):
    assert isinstance(instance, atem::LdpType)

@given(instance=atem::Definition_strategy)
@settings(max_examples=50)
def test_atem::definition_instantiation(instance):
    assert isinstance(instance, atem::Definition)

@given(instance=ElementType_strategy)
@settings(max_examples=50)
def test_elementtype_instantiation(instance):
    assert isinstance(instance, ElementType)

@given(instance=atem::TaggedText_strategy)
@settings(max_examples=50)
def test_atem::taggedtext_instantiation(instance):
    assert isinstance(instance, atem::TaggedText)

@given(instance=atem::LDP_strategy)
@settings(max_examples=50)
def test_atem::ldp_instantiation(instance):
    assert isinstance(instance, atem::LDP)

@given(instance=atem::Lookup_strategy)
@settings(max_examples=50)
def test_atem::lookup_instantiation(instance):
    assert isinstance(instance, atem::Lookup)

@given(instance=atem::Lookup_strategy)
def test_atem::lookup_dsl_Lookup_Override_Mode_Set_type(instance):
    assert isinstance(instance.dsl_Lookup_Override_Mode_Set, bool)


@given(instance=atem::Lookup_strategy)
def test_atem::lookup_dsl_Lookup_Override_Mode_Set_setter(instance):
    original = instance.dsl_Lookup_Override_Mode_Set
    instance.dsl_Lookup_Override_Mode_Set = original
    assert instance.dsl_Lookup_Override_Mode_Set == original

@given(instance=atem::Lookup_strategy)
def test_atem::lookup_dsl_Lookup_OverrideDay_type(instance):
    assert isinstance(instance.dsl_Lookup_OverrideDay, str)


@given(instance=atem::Lookup_strategy)
def test_atem::lookup_dsl_Lookup_OverrideDay_setter(instance):
    original = instance.dsl_Lookup_OverrideDay
    instance.dsl_Lookup_OverrideDay = original
    assert instance.dsl_Lookup_OverrideDay == original

@given(instance=atem::Lookup_strategy)
def test_atem::lookup_dsl_Lookup_OverrideMode_type(instance):
    assert isinstance(instance.dsl_Lookup_OverrideMode, str)


@given(instance=atem::Lookup_strategy)
def test_atem::lookup_dsl_Lookup_OverrideMode_setter(instance):
    original = instance.dsl_Lookup_OverrideMode
    instance.dsl_Lookup_OverrideMode = original
    assert instance.dsl_Lookup_OverrideMode == original

@given(instance=atem::Lookup_strategy)
def test_atem::lookup_dsl_Lookup_Override__Day_Set_type(instance):
    assert isinstance(instance.dsl_Lookup_Override__Day_Set, bool)


@given(instance=atem::Lookup_strategy)
def test_atem::lookup_dsl_Lookup_Override__Day_Set_setter(instance):
    original = instance.dsl_Lookup_Override__Day_Set
    instance.dsl_Lookup_Override__Day_Set = original
    assert instance.dsl_Lookup_Override__Day_Set == original

@given(instance=atem::Lookup_strategy)
def test_atem::lookup_dsl_Lookup_Media_Off_type(instance):
    assert isinstance(instance.dsl_Lookup_Media_Off, bool)


@given(instance=atem::Lookup_strategy)
def test_atem::lookup_dsl_Lookup_Media_Off_setter(instance):
    original = instance.dsl_Lookup_Media_Off
    instance.dsl_Lookup_Media_Off = original
    assert instance.dsl_Lookup_Media_Off == original

@given(instance=atem::ResourceText_strategy)
@settings(max_examples=50)
def test_atem::resourcetext_instantiation(instance):
    assert isinstance(instance, atem::ResourceText)

@given(instance=atem::ResourceText_strategy)
def test_atem::resourcetext_dsl_ResourceText_Media_Off_type(instance):
    assert isinstance(instance.dsl_ResourceText_Media_Off, bool)


@given(instance=atem::ResourceText_strategy)
def test_atem::resourcetext_dsl_ResourceText_Media_Off_setter(instance):
    original = instance.dsl_ResourceText_Media_Off
    instance.dsl_ResourceText_Media_Off = original
    assert instance.dsl_ResourceText_Media_Off == original

@given(instance=SectionElementType_strategy)
@settings(max_examples=50)
def test_sectionelementtype_instantiation(instance):
    assert isinstance(instance, SectionElementType)

@given(instance=atem::InfoElementType_strategy)
@settings(max_examples=50)
def test_atem::infoelementtype_instantiation(instance):
    assert isinstance(instance, atem::InfoElementType)

@given(instance=atem::ElementType_strategy)
@settings(max_examples=50)
def test_atem::elementtype_instantiation(instance):
    assert isinstance(instance, atem::ElementType)

@given(instance=HeaderFooterFragment_strategy)
@settings(max_examples=50)
def test_headerfooterfragment_instantiation(instance):
    assert isinstance(instance, HeaderFooterFragment)

@given(instance=atem::HeaderFooterCommemoration_strategy)
@settings(max_examples=50)
def test_atem::headerfootercommemoration_instantiation(instance):
    assert isinstance(instance, atem::HeaderFooterCommemoration)

@given(instance=atem::HeaderFooterCommemoration_strategy)
def test_atem::headerfootercommemoration_dsl_HeaderFooterCommemoration_type(instance):
    assert isinstance(instance.dsl_HeaderFooterCommemoration, bool)


@given(instance=atem::HeaderFooterCommemoration_strategy)
def test_atem::headerfootercommemoration_dsl_HeaderFooterCommemoration_setter(instance):
    original = instance.dsl_HeaderFooterCommemoration
    instance.dsl_HeaderFooterCommemoration = original
    assert instance.dsl_HeaderFooterCommemoration == original

@given(instance=atem::HeaderFooterDate_strategy)
@settings(max_examples=50)
def test_atem::headerfooterdate_instantiation(instance):
    assert isinstance(instance, atem::HeaderFooterDate)

@given(instance=atem::HeaderFooterDate_strategy)
def test_atem::headerfooterdate_dsl_HeaderFooterDate_type(instance):
    assert isinstance(instance.dsl_HeaderFooterDate, bool)


@given(instance=atem::HeaderFooterDate_strategy)
def test_atem::headerfooterdate_dsl_HeaderFooterDate_setter(instance):
    original = instance.dsl_HeaderFooterDate
    instance.dsl_HeaderFooterDate = original
    assert instance.dsl_HeaderFooterDate == original

@given(instance=atem::HeaderFooterDate_strategy)
def test_atem::headerfooterdate_dsl_HeaderFooterDate_Language_type(instance):
    assert isinstance(instance.dsl_HeaderFooterDate_Language, str)


@given(instance=atem::HeaderFooterDate_strategy)
def test_atem::headerfooterdate_dsl_HeaderFooterDate_Language_setter(instance):
    original = instance.dsl_HeaderFooterDate_Language
    instance.dsl_HeaderFooterDate_Language = original
    assert instance.dsl_HeaderFooterDate_Language == original

@given(instance=atem::HeaderFooterLookup_strategy)
@settings(max_examples=50)
def test_atem::headerfooterlookup_instantiation(instance):
    assert isinstance(instance, atem::HeaderFooterLookup)

@given(instance=atem::HeaderFooterLookup_strategy)
def test_atem::headerfooterlookup_dsl_HeaderFooterLookup_Language_type(instance):
    assert isinstance(instance.dsl_HeaderFooterLookup_Language, str)


@given(instance=atem::HeaderFooterLookup_strategy)
def test_atem::headerfooterlookup_dsl_HeaderFooterLookup_Language_setter(instance):
    original = instance.dsl_HeaderFooterLookup_Language
    instance.dsl_HeaderFooterLookup_Language = original
    assert instance.dsl_HeaderFooterLookup_Language == original

@given(instance=atem::HeaderFooterPageNumber_strategy)
@settings(max_examples=50)
def test_atem::headerfooterpagenumber_instantiation(instance):
    assert isinstance(instance, atem::HeaderFooterPageNumber)

@given(instance=atem::HeaderFooterPageNumber_strategy)
def test_atem::headerfooterpagenumber_dsl_HeaderFooterPageNumber_type(instance):
    assert isinstance(instance.dsl_HeaderFooterPageNumber, bool)


@given(instance=atem::HeaderFooterPageNumber_strategy)
def test_atem::headerfooterpagenumber_dsl_HeaderFooterPageNumber_setter(instance):
    original = instance.dsl_HeaderFooterPageNumber
    instance.dsl_HeaderFooterPageNumber = original
    assert instance.dsl_HeaderFooterPageNumber == original

@given(instance=atem::HeaderFooterTitle_strategy)
@settings(max_examples=50)
def test_atem::headerfootertitle_instantiation(instance):
    assert isinstance(instance, atem::HeaderFooterTitle)

@given(instance=atem::HeaderFooterTitle_strategy)
def test_atem::headerfootertitle_dsl_HeaderFooterTitle_type(instance):
    assert isinstance(instance.dsl_HeaderFooterTitle, bool)


@given(instance=atem::HeaderFooterTitle_strategy)
def test_atem::headerfootertitle_dsl_HeaderFooterTitle_setter(instance):
    original = instance.dsl_HeaderFooterTitle
    instance.dsl_HeaderFooterTitle = original
    assert instance.dsl_HeaderFooterTitle == original

@given(instance=atem::HeaderFooterText_strategy)
@settings(max_examples=50)
def test_atem::headerfootertext_instantiation(instance):
    assert isinstance(instance, atem::HeaderFooterText)

@given(instance=atem::HeaderFooterText_strategy)
def test_atem::headerfootertext_dsl_HeaderFooterText_type(instance):
    assert isinstance(instance.dsl_HeaderFooterText, str)


@given(instance=atem::HeaderFooterText_strategy)
def test_atem::headerfootertext_dsl_HeaderFooterText_setter(instance):
    original = instance.dsl_HeaderFooterText
    instance.dsl_HeaderFooterText = original
    assert instance.dsl_HeaderFooterText == original

@given(instance=HeaderFooterColumn_strategy)
@settings(max_examples=50)
def test_headerfootercolumn_instantiation(instance):
    assert isinstance(instance, HeaderFooterColumn)

@given(instance=atem::HeaderFooterColumnCenter_strategy)
@settings(max_examples=50)
def test_atem::headerfootercolumncenter_instantiation(instance):
    assert isinstance(instance, atem::HeaderFooterColumnCenter)

@given(instance=atem::HeaderFooterColumnRight_strategy)
@settings(max_examples=50)
def test_atem::headerfootercolumnright_instantiation(instance):
    assert isinstance(instance, atem::HeaderFooterColumnRight)

@given(instance=atem::HeaderFooterColumnLeft_strategy)
@settings(max_examples=50)
def test_atem::headerfootercolumnleft_instantiation(instance):
    assert isinstance(instance, atem::HeaderFooterColumnLeft)

@given(instance=PrefaceElementType_strategy)
@settings(max_examples=50)
def test_prefaceelementtype_instantiation(instance):
    assert isinstance(instance, PrefaceElementType)

@given(instance=InfoElementType_strategy)
@settings(max_examples=50)
def test_infoelementtype_instantiation(instance):
    assert isinstance(instance, InfoElementType)

@given(instance=AbstractComponent_strategy)
@settings(max_examples=50)
def test_abstractcomponent_instantiation(instance):
    assert isinstance(instance, AbstractComponent)

@given(instance=atem::Section_strategy)
@settings(max_examples=50)
def test_atem::section_instantiation(instance):
    assert isinstance(instance, atem::Section)

@given(instance=atem::Section_strategy)
def test_atem::section_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atem::Section_strategy)
def test_atem::section_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atem::Info_strategy)
@settings(max_examples=50)
def test_atem::info_instantiation(instance):
    assert isinstance(instance, atem::Info)

@given(instance=atem::Info_strategy)
def test_atem::info_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atem::Info_strategy)
def test_atem::info_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atem::TemplateFragment_strategy)
@settings(max_examples=50)
def test_atem::templatefragment_instantiation(instance):
    assert isinstance(instance, atem::TemplateFragment)

@given(instance=atem::Break_strategy)
@settings(max_examples=50)
def test_atem::break_instantiation(instance):
    assert isinstance(instance, atem::Break)

@given(instance=atem::Break_strategy)
def test_atem::break_dsl_break_type_type(instance):
    assert isinstance(instance.dsl_break_type, str)


@given(instance=atem::Break_strategy)
def test_atem::break_dsl_break_type_setter(instance):
    original = instance.dsl_break_type
    instance.dsl_break_type = original
    assert instance.dsl_break_type == original

@given(instance=atem::Title_strategy)
@settings(max_examples=50)
def test_atem::title_instantiation(instance):
    assert isinstance(instance, atem::Title)

@given(instance=atem::SubTitle_strategy)
@settings(max_examples=50)
def test_atem::subtitle_instantiation(instance):
    assert isinstance(instance, atem::SubTitle)

@given(instance=atem::PassThroughPdf_strategy)
@settings(max_examples=50)
def test_atem::passthroughpdf_instantiation(instance):
    assert isinstance(instance, atem::PassThroughPdf)

@given(instance=atem::PassThroughPdf_strategy)
def test_atem::passthroughpdf_dsl_Passthrough_pdf_text_type(instance):
    assert isinstance(instance.dsl_Passthrough_pdf_text, str)


@given(instance=atem::PassThroughPdf_strategy)
def test_atem::passthroughpdf_dsl_Passthrough_pdf_text_setter(instance):
    original = instance.dsl_Passthrough_pdf_text
    instance.dsl_Passthrough_pdf_text = original
    assert instance.dsl_Passthrough_pdf_text == original

@given(instance=atem::SectionFragment_strategy)
@settings(max_examples=50)
def test_atem::sectionfragment_instantiation(instance):
    assert isinstance(instance, atem::SectionFragment)

@given(instance=atem::VersionSwitch_strategy)
@settings(max_examples=50)
def test_atem::versionswitch_instantiation(instance):
    assert isinstance(instance, atem::VersionSwitch)

@given(instance=atem::VersionSwitch_strategy)
def test_atem::versionswitch_dsl_VersionSwitch_flag_type(instance):
    assert isinstance(instance.dsl_VersionSwitch_flag, str)


@given(instance=atem::VersionSwitch_strategy)
def test_atem::versionswitch_dsl_VersionSwitch_flag_setter(instance):
    original = instance.dsl_VersionSwitch_flag
    instance.dsl_VersionSwitch_flag = original
    assert instance.dsl_VersionSwitch_flag == original

@given(instance=HeadComponent_strategy)
@settings(max_examples=50)
def test_headcomponent_instantiation(instance):
    assert isinstance(instance, HeadComponent)

@given(instance=atem::Date_strategy)
@settings(max_examples=50)
def test_atem::date_instantiation(instance):
    assert isinstance(instance, atem::Date)

@given(instance=atem::Date_strategy)
def test_atem::date_dsl_Date_month_type(instance):
    assert isinstance(instance.dsl_Date_month, int)


@given(instance=atem::Date_strategy)
def test_atem::date_dsl_Date_month_setter(instance):
    original = instance.dsl_Date_month
    instance.dsl_Date_month = original
    assert instance.dsl_Date_month == original

@given(instance=atem::Date_strategy)
def test_atem::date_dsl_Date_day_type(instance):
    assert isinstance(instance.dsl_Date_day, int)


@given(instance=atem::Date_strategy)
def test_atem::date_dsl_Date_day_setter(instance):
    original = instance.dsl_Date_day
    instance.dsl_Date_day = original
    assert instance.dsl_Date_day == original

@given(instance=atem::Date_strategy)
def test_atem::date_dsl_Date_year_type(instance):
    assert isinstance(instance.dsl_Date_year, int)


@given(instance=atem::Date_strategy)
def test_atem::date_dsl_Date_year_setter(instance):
    original = instance.dsl_Date_year
    instance.dsl_Date_year = original
    assert instance.dsl_Date_year == original

@given(instance=atem::Commemoration_strategy)
@settings(max_examples=50)
def test_atem::commemoration_instantiation(instance):
    assert isinstance(instance, atem::Commemoration)

@given(instance=atem::PageFooterOdd_strategy)
@settings(max_examples=50)
def test_atem::pagefooterodd_instantiation(instance):
    assert isinstance(instance, atem::PageFooterOdd)

@given(instance=atem::TemplateTitle_strategy)
@settings(max_examples=50)
def test_atem::templatetitle_instantiation(instance):
    assert isinstance(instance, atem::TemplateTitle)

@given(instance=atem::PageFooterEven_strategy)
@settings(max_examples=50)
def test_atem::pagefootereven_instantiation(instance):
    assert isinstance(instance, atem::PageFooterEven)

@given(instance=atem::PageHeaderOdd_strategy)
@settings(max_examples=50)
def test_atem::pageheaderodd_instantiation(instance):
    assert isinstance(instance, atem::PageHeaderOdd)

@given(instance=atem::HeaderFooterColumn_strategy)
@settings(max_examples=50)
def test_atem::headerfootercolumn_instantiation(instance):
    assert isinstance(instance, atem::HeaderFooterColumn)

@given(instance=atem::PageHeaderEven_strategy)
@settings(max_examples=50)
def test_atem::pageheadereven_instantiation(instance):
    assert isinstance(instance, atem::PageHeaderEven)

@given(instance=atem::PageKeepWithNext_strategy)
@settings(max_examples=50)
def test_atem::pagekeepwithnext_instantiation(instance):
    assert isinstance(instance, atem::PageKeepWithNext)

@given(instance=atem::PageKeepWithNext_strategy)
def test_atem::pagekeepwithnext_dsl_PageKeepWithNext_value_type(instance):
    assert isinstance(instance.dsl_PageKeepWithNext_value, str)


@given(instance=atem::PageKeepWithNext_strategy)
def test_atem::pagekeepwithnext_dsl_PageKeepWithNext_value_setter(instance):
    original = instance.dsl_PageKeepWithNext_value
    instance.dsl_PageKeepWithNext_value = original
    assert instance.dsl_PageKeepWithNext_value == original

@given(instance=atem::HeaderFooterFragment_strategy)
@settings(max_examples=50)
def test_atem::headerfooterfragment_instantiation(instance):
    assert isinstance(instance, atem::HeaderFooterFragment)

@given(instance=atem::Preface_strategy)
@settings(max_examples=50)
def test_atem::preface_instantiation(instance):
    assert isinstance(instance, atem::Preface)

@given(instance=atem::Preface_strategy)
def test_atem::preface_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atem::Preface_strategy)
def test_atem::preface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atem::Head_strategy)
@settings(max_examples=50)
def test_atem::head_instantiation(instance):
    assert isinstance(instance, atem::Head)

@given(instance=atem::Driver_strategy)
@settings(max_examples=50)
def test_atem::driver_instantiation(instance):
    assert isinstance(instance, atem::Driver)

@given(instance=atem::Driver_strategy)
def test_atem::driver_dsl_Driver_RegEx_type(instance):
    assert isinstance(instance.dsl_Driver_RegEx, str)


@given(instance=atem::Driver_strategy)
def test_atem::driver_dsl_Driver_RegEx_setter(instance):
    original = instance.dsl_Driver_RegEx
    instance.dsl_Driver_RegEx = original
    assert instance.dsl_Driver_RegEx == original

@given(instance=atem::Driver_strategy)
def test_atem::driver_dsl_Driver_Status_type(instance):
    assert isinstance(instance.dsl_Driver_Status, str)


@given(instance=atem::Driver_strategy)
def test_atem::driver_dsl_Driver_Status_setter(instance):
    original = instance.dsl_Driver_Status
    instance.dsl_Driver_Status = original
    assert instance.dsl_Driver_Status == original

@given(instance=atem::Import_strategy)
@settings(max_examples=50)
def test_atem::import_instantiation(instance):
    assert isinstance(instance, atem::Import)

@given(instance=atem::Import_strategy)
def test_atem::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=atem::Import_strategy)
def test_atem::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=atem::TemplateStatus_strategy)
@settings(max_examples=50)
def test_atem::templatestatus_instantiation(instance):
    assert isinstance(instance, atem::TemplateStatus)

@given(instance=atem::TemplateStatus_strategy)
def test_atem::templatestatus_dsl_TemplateStatus_type(instance):
    assert isinstance(instance.dsl_TemplateStatus, str)


@given(instance=atem::TemplateStatus_strategy)
def test_atem::templatestatus_dsl_TemplateStatus_setter(instance):
    original = instance.dsl_TemplateStatus
    instance.dsl_TemplateStatus = original
    assert instance.dsl_TemplateStatus == original

@given(instance=atem::AtemModel_strategy)
@settings(max_examples=50)
def test_atem::atemmodel_instantiation(instance):
    assert isinstance(instance, atem::AtemModel)

@given(instance=atem::AtemModel_strategy)
def test_atem::atemmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atem::AtemModel_strategy)
def test_atem::atemmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atem::HeadComponent_strategy)
@settings(max_examples=50)
def test_atem::headcomponent_instantiation(instance):
    assert isinstance(instance, atem::HeadComponent)

@given(instance=atem::AbstractComponent_strategy)
@settings(max_examples=50)
def test_atem::abstractcomponent_instantiation(instance):
    assert isinstance(instance, atem::AbstractComponent)

@given(instance=atem::WhenExists_strategy)
@settings(max_examples=50)
def test_atem::whenexists_instantiation(instance):
    assert isinstance(instance, atem::WhenExists)

@given(instance=atem::WhenExistsCase_strategy)
@settings(max_examples=50)
def test_atem::whenexistscase_instantiation(instance):
    assert isinstance(instance, atem::WhenExistsCase)

@given(instance=atem::WhenModeOfWeekCase_strategy)
@settings(max_examples=50)
def test_atem::whenmodeofweekcase_instantiation(instance):
    assert isinstance(instance, atem::WhenModeOfWeekCase)

@given(instance=atem::WhenModeOfWeek_strategy)
@settings(max_examples=50)
def test_atem::whenmodeofweek_instantiation(instance):
    assert isinstance(instance, atem::WhenModeOfWeek)

@given(instance=atem::SundaysBeforeTriodionCase_strategy)
@settings(max_examples=50)
def test_atem::sundaysbeforetriodioncase_instantiation(instance):
    assert isinstance(instance, atem::SundaysBeforeTriodionCase)

@given(instance=atem::SundaysBeforeTriodionCase_strategy)
def test_atem::sundaysbeforetriodioncase_dsl_SundaysBeforeTriodionCase_Days_type(instance):
    assert isinstance(instance.dsl_SundaysBeforeTriodionCase_Days, int)


@given(instance=atem::SundaysBeforeTriodionCase_strategy)
def test_atem::sundaysbeforetriodioncase_dsl_SundaysBeforeTriodionCase_Days_setter(instance):
    original = instance.dsl_SundaysBeforeTriodionCase_Days
    instance.dsl_SundaysBeforeTriodionCase_Days = original
    assert instance.dsl_SundaysBeforeTriodionCase_Days == original

@given(instance=atem::WhenSundaysBeforeTriodion_strategy)
@settings(max_examples=50)
def test_atem::whensundaysbeforetriodion_instantiation(instance):
    assert isinstance(instance, atem::WhenSundaysBeforeTriodion)

@given(instance=atem::ModeOfWeekSet_strategy)
@settings(max_examples=50)
def test_atem::modeofweekset_instantiation(instance):
    assert isinstance(instance, atem::ModeOfWeekSet)

@given(instance=atem::ModeOfWeekSet_strategy)
def test_atem::modeofweekset_dsl_ModeOfWeekSet_MOWs_type(instance):
    assert isinstance(instance.dsl_ModeOfWeekSet_MOWs, str)


@given(instance=atem::ModeOfWeekSet_strategy)
def test_atem::modeofweekset_dsl_ModeOfWeekSet_MOWs_setter(instance):
    original = instance.dsl_ModeOfWeekSet_MOWs
    instance.dsl_ModeOfWeekSet_MOWs = original
    assert instance.dsl_ModeOfWeekSet_MOWs == original

@given(instance=atem::WhenMovableCycleDay_strategy)
@settings(max_examples=50)
def test_atem::whenmovablecycleday_instantiation(instance):
    assert isinstance(instance, atem::WhenMovableCycleDay)

@given(instance=AbstractDayCase_strategy)
@settings(max_examples=50)
def test_abstractdaycase_instantiation(instance):
    assert isinstance(instance, AbstractDayCase)

@given(instance=atem::DaySet_strategy)
@settings(max_examples=50)
def test_atem::dayset_instantiation(instance):
    assert isinstance(instance, atem::DaySet)

@given(instance=atem::DaySet_strategy)
def test_atem::dayset_dslSetValue_Days_type(instance):
    assert isinstance(instance.dslSetValue_Days, int)


@given(instance=atem::DaySet_strategy)
def test_atem::dayset_dslSetValue_Days_setter(instance):
    original = instance.dslSetValue_Days
    instance.dslSetValue_Days = original
    assert instance.dslSetValue_Days == original

@given(instance=atem::DayRange_strategy)
@settings(max_examples=50)
def test_atem::dayrange_instantiation(instance):
    assert isinstance(instance, atem::DayRange)

@given(instance=atem::DayRange_strategy)
def test_atem::dayrange_dsl_Range_To_type(instance):
    assert isinstance(instance.dsl_Range_To, int)


@given(instance=atem::DayRange_strategy)
def test_atem::dayrange_dsl_Range_To_setter(instance):
    original = instance.dsl_Range_To
    instance.dsl_Range_To = original
    assert instance.dsl_Range_To == original

@given(instance=atem::DayRange_strategy)
def test_atem::dayrange_dsl_DayRange_from_type(instance):
    assert isinstance(instance.dsl_DayRange_from, int)


@given(instance=atem::DayRange_strategy)
def test_atem::dayrange_dsl_DayRange_from_setter(instance):
    original = instance.dsl_DayRange_from
    instance.dsl_DayRange_from = original
    assert instance.dsl_DayRange_from == original

@given(instance=atem::AbstractDayCase_strategy)
@settings(max_examples=50)
def test_atem::abstractdaycase_instantiation(instance):
    assert isinstance(instance, atem::AbstractDayCase)

@given(instance=atem::WhenPascha_strategy)
@settings(max_examples=50)
def test_atem::whenpascha_instantiation(instance):
    assert isinstance(instance, atem::WhenPascha)

@given(instance=atem::WhenLukanCycleDay_strategy)
@settings(max_examples=50)
def test_atem::whenlukancycleday_instantiation(instance):
    assert isinstance(instance, atem::WhenLukanCycleDay)

@given(instance=atem::WhenSundayAfterElevationOfCrossDay_strategy)
@settings(max_examples=50)
def test_atem::whensundayafterelevationofcrossday_instantiation(instance):
    assert isinstance(instance, atem::WhenSundayAfterElevationOfCrossDay)

@given(instance=AbstractDateCase_strategy)
@settings(max_examples=50)
def test_abstractdatecase_instantiation(instance):
    assert isinstance(instance, AbstractDateCase)

@given(instance=atem::DateSet_strategy)
@settings(max_examples=50)
def test_atem::dateset_instantiation(instance):
    assert isinstance(instance, atem::DateSet)

@given(instance=atem::DateSet_strategy)
def test_atem::dateset_dslDateSet_Values_type(instance):
    assert isinstance(instance.dslDateSet_Values, int)


@given(instance=atem::DateSet_strategy)
def test_atem::dateset_dslDateSet_Values_setter(instance):
    original = instance.dslDateSet_Values
    instance.dslDateSet_Values = original
    assert instance.dslDateSet_Values == original

@given(instance=atem::DateRange_strategy)
@settings(max_examples=50)
def test_atem::daterange_instantiation(instance):
    assert isinstance(instance, atem::DateRange)

@given(instance=atem::DateRange_strategy)
def test_atem::daterange_dsl_DateRange_To_type(instance):
    assert isinstance(instance.dsl_DateRange_To, int)


@given(instance=atem::DateRange_strategy)
def test_atem::daterange_dsl_DateRange_To_setter(instance):
    original = instance.dsl_DateRange_To
    instance.dsl_DateRange_To = original
    assert instance.dsl_DateRange_To == original

@given(instance=atem::DateRange_strategy)
def test_atem::daterange_dsl_DateRange_from_type(instance):
    assert isinstance(instance.dsl_DateRange_from, int)


@given(instance=atem::DateRange_strategy)
def test_atem::daterange_dsl_DateRange_from_setter(instance):
    original = instance.dsl_DateRange_from
    instance.dsl_DateRange_from = original
    assert instance.dsl_DateRange_from == original

@given(instance=atem::WhenTriodionDay_strategy)
@settings(max_examples=50)
def test_atem::whentriodionday_instantiation(instance):
    assert isinstance(instance, atem::WhenTriodionDay)

@given(instance=atem::WhenPeriodCase_strategy)
@settings(max_examples=50)
def test_atem::whenperiodcase_instantiation(instance):
    assert isinstance(instance, atem::WhenPeriodCase)

@given(instance=atem::WhenPentecostarionDay_strategy)
@settings(max_examples=50)
def test_atem::whenpentecostarionday_instantiation(instance):
    assert isinstance(instance, atem::WhenPentecostarionDay)

@given(instance=AbstractDayNameCase_strategy)
@settings(max_examples=50)
def test_abstractdaynamecase_instantiation(instance):
    assert isinstance(instance, AbstractDayNameCase)

@given(instance=atem::DayNameSet_strategy)
@settings(max_examples=50)
def test_atem::daynameset_instantiation(instance):
    assert isinstance(instance, atem::DayNameSet)

@given(instance=atem::DayNameSet_strategy)
def test_atem::daynameset_dslDayNameSet_Values_type(instance):
    assert isinstance(instance.dslDayNameSet_Values, str)


@given(instance=atem::DayNameSet_strategy)
def test_atem::daynameset_dslDayNameSet_Values_setter(instance):
    original = instance.dslDayNameSet_Values
    instance.dslDayNameSet_Values = original
    assert instance.dslDayNameSet_Values == original

@given(instance=atem::DayNameRange_strategy)
@settings(max_examples=50)
def test_atem::daynamerange_instantiation(instance):
    assert isinstance(instance, atem::DayNameRange)

@given(instance=atem::DayNameRange_strategy)
def test_atem::daynamerange_dsl_DayNameRange_To_type(instance):
    assert isinstance(instance.dsl_DayNameRange_To, str)


@given(instance=atem::DayNameRange_strategy)
def test_atem::daynamerange_dsl_DayNameRange_To_setter(instance):
    original = instance.dsl_DayNameRange_To
    instance.dsl_DayNameRange_To = original
    assert instance.dsl_DayNameRange_To == original

@given(instance=atem::DayNameRange_strategy)
def test_atem::daynamerange_dsl_DayNameRange_from_type(instance):
    assert isinstance(instance.dsl_DayNameRange_from, str)


@given(instance=atem::DayNameRange_strategy)
def test_atem::daynamerange_dsl_DayNameRange_from_setter(instance):
    original = instance.dsl_DayNameRange_from
    instance.dsl_DayNameRange_from = original
    assert instance.dsl_DayNameRange_from == original

@given(instance=atem::AbstractDayNameCase_strategy)
@settings(max_examples=50)
def test_atem::abstractdaynamecase_instantiation(instance):
    assert isinstance(instance, atem::AbstractDayNameCase)

@given(instance=atem::WhenDayNameCase_strategy)
@settings(max_examples=50)
def test_atem::whendaynamecase_instantiation(instance):
    assert isinstance(instance, atem::WhenDayNameCase)

@given(instance=atem::WhenDayName_strategy)
@settings(max_examples=50)
def test_atem::whendayname_instantiation(instance):
    assert isinstance(instance, atem::WhenDayName)

@given(instance=atem::AbstractDateCase_strategy)
@settings(max_examples=50)
def test_atem::abstractdatecase_instantiation(instance):
    assert isinstance(instance, atem::AbstractDateCase)

@given(instance=atem::WhenOther_strategy)
@settings(max_examples=50)
def test_atem::whenother_instantiation(instance):
    assert isinstance(instance, atem::WhenOther)

@given(instance=atem::WhenDateCase_strategy)
@settings(max_examples=50)
def test_atem::whendatecase_instantiation(instance):
    assert isinstance(instance, atem::WhenDateCase)

@given(instance=atem::WhenDateCase_strategy)
def test_atem::whendatecase_dsl_WhenDate_Case_Month_type(instance):
    assert isinstance(instance.dsl_WhenDate_Case_Month, str)


@given(instance=atem::WhenDateCase_strategy)
def test_atem::whendatecase_dsl_WhenDate_Case_Month_setter(instance):
    original = instance.dsl_WhenDate_Case_Month
    instance.dsl_WhenDate_Case_Month = original
    assert instance.dsl_WhenDate_Case_Month == original

@given(instance=atem::WhenDate_strategy)
@settings(max_examples=50)
def test_atem::whendate_instantiation(instance):
    assert isinstance(instance, atem::WhenDate)

@given(instance=atem::RestoreLocale_strategy)
@settings(max_examples=50)
def test_atem::restorelocale_instantiation(instance):
    assert isinstance(instance, atem::RestoreLocale)

@given(instance=atem::RestoreLocale_strategy)
def test_atem::restorelocale_dsl_RestoreLocale_type(instance):
    assert isinstance(instance.dsl_RestoreLocale, bool)


@given(instance=atem::RestoreLocale_strategy)
def test_atem::restorelocale_dsl_RestoreLocale_setter(instance):
    original = instance.dsl_RestoreLocale
    instance.dsl_RestoreLocale = original
    assert instance.dsl_RestoreLocale == original

@given(instance=atem::Dialog_strategy)
@settings(max_examples=50)
def test_atem::dialog_instantiation(instance):
    assert isinstance(instance, atem::Dialog)

@given(instance=atem::Rubric_strategy)
@settings(max_examples=50)
def test_atem::rubric_instantiation(instance):
    assert isinstance(instance, atem::Rubric)

@given(instance=atem::SetLocale_strategy)
@settings(max_examples=50)
def test_atem::setlocale_instantiation(instance):
    assert isinstance(instance, atem::SetLocale)

@given(instance=atem::SetLocale_strategy)
def test_atem::setlocale_dsl_SetLocale_V1_type(instance):
    assert isinstance(instance.dsl_SetLocale_V1, str)


@given(instance=atem::SetLocale_strategy)
def test_atem::setlocale_dsl_SetLocale_V1_setter(instance):
    original = instance.dsl_SetLocale_V1
    instance.dsl_SetLocale_V1 = original
    assert instance.dsl_SetLocale_V1 == original

@given(instance=atem::SetLocale_strategy)
def test_atem::setlocale_dsl_SetLocale_V2_type(instance):
    assert isinstance(instance.dsl_SetLocale_V2, str)


@given(instance=atem::SetLocale_strategy)
def test_atem::setlocale_dsl_SetLocale_V2_setter(instance):
    original = instance.dsl_SetLocale_V2
    instance.dsl_SetLocale_V2 = original
    assert instance.dsl_SetLocale_V2 == original

@given(instance=atem::LitBook_strategy)
@settings(max_examples=50)
def test_atem::litbook_instantiation(instance):
    assert isinstance(instance, atem::LitBook)

@given(instance=atem::LitBook_strategy)
def test_atem::litbook_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atem::LitBook_strategy)
def test_atem::litbook_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atem::Version_strategy)
@settings(max_examples=50)
def test_atem::version_instantiation(instance):
    assert isinstance(instance, atem::Version)

@given(instance=atem::Version_strategy)
def test_atem::version_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atem::Version_strategy)
def test_atem::version_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atem::Aid_strategy)
@settings(max_examples=50)
def test_atem::aid_instantiation(instance):
    assert isinstance(instance, atem::Aid)

@given(instance=atem::Aid_strategy)
def test_atem::aid_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atem::Aid_strategy)
def test_atem::aid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atem::Heading3_strategy)
@settings(max_examples=50)
def test_atem::heading3_instantiation(instance):
    assert isinstance(instance, atem::Heading3)

@given(instance=atem::Heading2_strategy)
@settings(max_examples=50)
def test_atem::heading2_instantiation(instance):
    assert isinstance(instance, atem::Heading2)

@given(instance=atem::Heading1_strategy)
@settings(max_examples=50)
def test_atem::heading1_instantiation(instance):
    assert isinstance(instance, atem::Heading1)

@given(instance=atem::Reading_strategy)
@settings(max_examples=50)
def test_atem::reading_instantiation(instance):
    assert isinstance(instance, atem::Reading)

@given(instance=atem::Block_strategy)
@settings(max_examples=50)
def test_atem::block_instantiation(instance):
    assert isinstance(instance, atem::Block)

@given(instance=atem::Actor_strategy)
@settings(max_examples=50)
def test_atem::actor_instantiation(instance):
    assert isinstance(instance, atem::Actor)

@given(instance=atem::Paragraph_strategy)
@settings(max_examples=50)
def test_atem::paragraph_instantiation(instance):
    assert isinstance(instance, atem::Paragraph)

@given(instance=atem::Verse_strategy)
@settings(max_examples=50)
def test_atem::verse_instantiation(instance):
    assert isinstance(instance, atem::Verse)

@given(instance=atem::Media_strategy)
@settings(max_examples=50)
def test_atem::media_instantiation(instance):
    assert isinstance(instance, atem::Media)

@given(instance=atem::Hymn_strategy)
@settings(max_examples=50)
def test_atem::hymn_instantiation(instance):
    assert isinstance(instance, atem::Hymn)

@given(instance=atem::PassThroughHtml_strategy)
@settings(max_examples=50)
def test_atem::passthroughhtml_instantiation(instance):
    assert isinstance(instance, atem::PassThroughHtml)

@given(instance=atem::PassThroughHtml_strategy)
def test_atem::passthroughhtml_dsl_Passthrough_html_text_type(instance):
    assert isinstance(instance.dsl_Passthrough_html_text, str)


@given(instance=atem::PassThroughHtml_strategy)
def test_atem::passthroughhtml_dsl_Passthrough_html_text_setter(instance):
    original = instance.dsl_Passthrough_html_text
    instance.dsl_Passthrough_html_text = original
    assert instance.dsl_Passthrough_html_text == original

@given(instance=atem::PageNumber_strategy)
@settings(max_examples=50)
def test_atem::pagenumber_instantiation(instance):
    assert isinstance(instance, atem::PageNumber)

@given(instance=atem::PageNumber_strategy)
def test_atem::pagenumber_dsl_PageNumber_value_type(instance):
    assert isinstance(instance.dsl_PageNumber_value, int)


@given(instance=atem::PageNumber_strategy)
def test_atem::pagenumber_dsl_PageNumber_value_setter(instance):
    original = instance.dsl_PageNumber_value
    instance.dsl_PageNumber_value = original
    assert instance.dsl_PageNumber_value == original
