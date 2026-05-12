import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    atem_WhenExistsCase,
    atem_WhenModeOfWeekCase,
    atem_SundaysBeforeTriodionCase,
    atem_ModeOfWeekSet,
    AbstractDayCase,
    atem_DaySet,
    atem_DayRange,
    atem_AbstractDayCase,
    AbstractDateCase,
    atem_DateSet,
    atem_DateRange,
    atem_WhenPeriodCase,
    AbstractDayNameCase,
    atem_DayNameSet,
    atem_DayNameRange,
    atem_AbstractDayNameCase,
    atem_WhenDayNameCase,
    atem_AbstractDateCase,
    atem_WhenOther,
    atem_WhenDateCase,
    atem_PrefaceFragment,
    LdpType,
    atem_DOM,
    atem_NOP,
    atem_SBT,
    atem_WOLC,
    atem_WDOLC,
    atem_DOL,
    atem_MOW,
    atem_MCD,
    atem_GenDate,
    atem_GenYear,
    atem_All,
    atem_SectionElementType,
    atem_PrefaceElementType,
    atem_SOL,
    atem_SAEC,
    atem_EOW,
    atem_DOWT,
    atem_DOWN,
    atem_DOP,
    atem_LdpType,
    atem_Definition,
    ElementType,
    atem_TaggedText,
    atem_LDP,
    atem_Lookup,
    atem_ResourceText,
    SectionElementType,
    atem_InfoElementType,
    atem_ElementType,
    HeaderFooterFragment,
    atem_HeaderFooterTitle,
    atem_HeaderFooterCommemoration,
    atem_HeaderFooterLookup,
    atem_HeaderFooterPageNumber,
    atem_HeaderFooterDate,
    atem_HeaderFooterText,
    HeaderFooterColumn,
    atem_HeaderFooterColumnRight,
    atem_HeaderFooterColumnCenter,
    atem_HeaderFooterColumnLeft,
    PrefaceElementType,
    InfoElementType,
    AbstractComponent,
    atem_Actor,
    atem_TemplateFragment,
    atem_Hymn,
    atem_LitBook,
    atem_SubTitle,
    atem_Paragraph,
    atem_SetLocale,
    atem_WhenTriodionDay,
    atem_WhenMovableCycleDay,
    atem_Aid,
    atem_WhenLukanCycleDay,
    atem_Break,
    atem_Media,
    atem_PassThroughPdf,
    atem_Dialog,
    atem_SectionFragment,
    atem_Title,
    atem_WhenDayName,
    atem_RestoreLocale,
    atem_Heading3,
    atem_Rubric,
    atem_Info,
    atem_Block,
    atem_Heading1,
    atem_Reading,
    atem_WhenDate,
    atem_WhenModeOfWeek,
    atem_WhenExists,
    atem_WhenPascha,
    atem_WhenPentecostarionDay,
    atem_WhenSundaysBeforeTriodion,
    atem_Section,
    atem_WhenSundayAfterElevationOfCrossDay,
    atem_Heading2,
    atem_Verse,
    atem_PassThroughHtml,
    atem_Version,
    atem_VersionSwitch,
    HeadComponent,
    atem_Commemoration,
    atem_PageNumber,
    atem_PageFooterOdd,
    atem_Date,
    atem_TemplateTitle,
    atem_PageFooterEven,
    atem_PageHeaderOdd,
    atem_HeaderFooterColumn,
    atem_PageHeaderEven,
    atem_PageKeepWithNext,
    atem_HeaderFooterFragment,
    atem_Preface,
    atem_Head,
    atem_Driver,
    atem_Import,
    atem_TemplateStatus,
    atem_AtemModel,
    atem_HeadComponent,
    atem_AbstractComponent,
    TemplateStatuses,
    DowTypes,
    ModeTypes,
    PeriodType,
    BreakType,
    MonthName,
    DayOfMonthTypes,
    Null,
    Language,
    BookTypes,
    Seasons,
    DayOfWeek,
    VersionSwitchType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_atem_whenexistscase_is_not_abstract():
    assert not inspect.isabstract(atem_WhenExistsCase)


def test_atem_whenexistscase_constructor_exists():
    assert callable(atem_WhenExistsCase.__init__)


def test_atem_whenexistscase_constructor_args():
    sig = inspect.signature(atem_WhenExistsCase.__init__)
    params = list(sig.parameters.keys())



def test_atem_whenmodeofweekcase_is_not_abstract():
    assert not inspect.isabstract(atem_WhenModeOfWeekCase)


def test_atem_whenmodeofweekcase_constructor_exists():
    assert callable(atem_WhenModeOfWeekCase.__init__)


def test_atem_whenmodeofweekcase_constructor_args():
    sig = inspect.signature(atem_WhenModeOfWeekCase.__init__)
    params = list(sig.parameters.keys())



def test_atem_sundaysbeforetriodioncase_is_not_abstract():
    assert not inspect.isabstract(atem_SundaysBeforeTriodionCase)


def test_atem_sundaysbeforetriodioncase_constructor_exists():
    assert callable(atem_SundaysBeforeTriodionCase.__init__)


def test_atem_sundaysbeforetriodioncase_constructor_args():
    sig = inspect.signature(atem_SundaysBeforeTriodionCase.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_SundaysBeforeTriodionCase_Days" in params, "Missing parameter 'dsl_SundaysBeforeTriodionCase_Days'"

def test_atem_sundaysbeforetriodioncase_has_dsl_SundaysBeforeTriodionCase_Days():
    assert hasattr(atem_SundaysBeforeTriodionCase, "dsl_SundaysBeforeTriodionCase_Days")
    descriptor = None
    for klass in atem_SundaysBeforeTriodionCase.__mro__:
        if "dsl_SundaysBeforeTriodionCase_Days" in klass.__dict__:
            descriptor = klass.__dict__["dsl_SundaysBeforeTriodionCase_Days"]
            break
    assert isinstance(descriptor, property)



def test_atem_modeofweekset_is_not_abstract():
    assert not inspect.isabstract(atem_ModeOfWeekSet)


def test_atem_modeofweekset_constructor_exists():
    assert callable(atem_ModeOfWeekSet.__init__)


def test_atem_modeofweekset_constructor_args():
    sig = inspect.signature(atem_ModeOfWeekSet.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_ModeOfWeekSet_MOWs" in params, "Missing parameter 'dsl_ModeOfWeekSet_MOWs'"

def test_atem_modeofweekset_has_dsl_ModeOfWeekSet_MOWs():
    assert hasattr(atem_ModeOfWeekSet, "dsl_ModeOfWeekSet_MOWs")
    descriptor = None
    for klass in atem_ModeOfWeekSet.__mro__:
        if "dsl_ModeOfWeekSet_MOWs" in klass.__dict__:
            descriptor = klass.__dict__["dsl_ModeOfWeekSet_MOWs"]
            break
    assert isinstance(descriptor, property)



def test_abstractdaycase_is_not_abstract():
    assert not inspect.isabstract(AbstractDayCase)


def test_abstractdaycase_constructor_exists():
    assert callable(AbstractDayCase.__init__)


def test_abstractdaycase_constructor_args():
    sig = inspect.signature(AbstractDayCase.__init__)
    params = list(sig.parameters.keys())



def test_atem_dayset_is_not_abstract():
    assert not inspect.isabstract(atem_DaySet)


def test_atem_dayset_constructor_exists():
    assert callable(atem_DaySet.__init__)


def test_atem_dayset_constructor_args():
    sig = inspect.signature(atem_DaySet.__init__)
    params = list(sig.parameters.keys())
    assert "dslSetValue_Days" in params, "Missing parameter 'dslSetValue_Days'"

def test_atem_dayset_has_dslSetValue_Days():
    assert hasattr(atem_DaySet, "dslSetValue_Days")
    descriptor = None
    for klass in atem_DaySet.__mro__:
        if "dslSetValue_Days" in klass.__dict__:
            descriptor = klass.__dict__["dslSetValue_Days"]
            break
    assert isinstance(descriptor, property)



def test_atem_dayrange_is_not_abstract():
    assert not inspect.isabstract(atem_DayRange)


def test_atem_dayrange_constructor_exists():
    assert callable(atem_DayRange.__init__)


def test_atem_dayrange_constructor_args():
    sig = inspect.signature(atem_DayRange.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Range_To" in params, "Missing parameter 'dsl_Range_To'"
    assert "dsl_DayRange_from" in params, "Missing parameter 'dsl_DayRange_from'"

def test_atem_dayrange_has_dsl_Range_To():
    assert hasattr(atem_DayRange, "dsl_Range_To")
    descriptor = None
    for klass in atem_DayRange.__mro__:
        if "dsl_Range_To" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Range_To"]
            break
    assert isinstance(descriptor, property)

def test_atem_dayrange_has_dsl_DayRange_from():
    assert hasattr(atem_DayRange, "dsl_DayRange_from")
    descriptor = None
    for klass in atem_DayRange.__mro__:
        if "dsl_DayRange_from" in klass.__dict__:
            descriptor = klass.__dict__["dsl_DayRange_from"]
            break
    assert isinstance(descriptor, property)



def test_atem_abstractdaycase_is_not_abstract():
    assert not inspect.isabstract(atem_AbstractDayCase)


def test_atem_abstractdaycase_constructor_exists():
    assert callable(atem_AbstractDayCase.__init__)


def test_atem_abstractdaycase_constructor_args():
    sig = inspect.signature(atem_AbstractDayCase.__init__)
    params = list(sig.parameters.keys())



def test_abstractdatecase_is_not_abstract():
    assert not inspect.isabstract(AbstractDateCase)


def test_abstractdatecase_constructor_exists():
    assert callable(AbstractDateCase.__init__)


def test_abstractdatecase_constructor_args():
    sig = inspect.signature(AbstractDateCase.__init__)
    params = list(sig.parameters.keys())



def test_atem_dateset_is_not_abstract():
    assert not inspect.isabstract(atem_DateSet)


def test_atem_dateset_constructor_exists():
    assert callable(atem_DateSet.__init__)


def test_atem_dateset_constructor_args():
    sig = inspect.signature(atem_DateSet.__init__)
    params = list(sig.parameters.keys())
    assert "dslDateSet_Values" in params, "Missing parameter 'dslDateSet_Values'"

def test_atem_dateset_has_dslDateSet_Values():
    assert hasattr(atem_DateSet, "dslDateSet_Values")
    descriptor = None
    for klass in atem_DateSet.__mro__:
        if "dslDateSet_Values" in klass.__dict__:
            descriptor = klass.__dict__["dslDateSet_Values"]
            break
    assert isinstance(descriptor, property)



def test_atem_daterange_is_not_abstract():
    assert not inspect.isabstract(atem_DateRange)


def test_atem_daterange_constructor_exists():
    assert callable(atem_DateRange.__init__)


def test_atem_daterange_constructor_args():
    sig = inspect.signature(atem_DateRange.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_DateRange_To" in params, "Missing parameter 'dsl_DateRange_To'"
    assert "dsl_DateRange_from" in params, "Missing parameter 'dsl_DateRange_from'"

def test_atem_daterange_has_dsl_DateRange_To():
    assert hasattr(atem_DateRange, "dsl_DateRange_To")
    descriptor = None
    for klass in atem_DateRange.__mro__:
        if "dsl_DateRange_To" in klass.__dict__:
            descriptor = klass.__dict__["dsl_DateRange_To"]
            break
    assert isinstance(descriptor, property)

def test_atem_daterange_has_dsl_DateRange_from():
    assert hasattr(atem_DateRange, "dsl_DateRange_from")
    descriptor = None
    for klass in atem_DateRange.__mro__:
        if "dsl_DateRange_from" in klass.__dict__:
            descriptor = klass.__dict__["dsl_DateRange_from"]
            break
    assert isinstance(descriptor, property)



def test_atem_whenperiodcase_is_not_abstract():
    assert not inspect.isabstract(atem_WhenPeriodCase)


def test_atem_whenperiodcase_constructor_exists():
    assert callable(atem_WhenPeriodCase.__init__)


def test_atem_whenperiodcase_constructor_args():
    sig = inspect.signature(atem_WhenPeriodCase.__init__)
    params = list(sig.parameters.keys())



def test_abstractdaynamecase_is_not_abstract():
    assert not inspect.isabstract(AbstractDayNameCase)


def test_abstractdaynamecase_constructor_exists():
    assert callable(AbstractDayNameCase.__init__)


def test_abstractdaynamecase_constructor_args():
    sig = inspect.signature(AbstractDayNameCase.__init__)
    params = list(sig.parameters.keys())



def test_atem_daynameset_is_not_abstract():
    assert not inspect.isabstract(atem_DayNameSet)


def test_atem_daynameset_constructor_exists():
    assert callable(atem_DayNameSet.__init__)


def test_atem_daynameset_constructor_args():
    sig = inspect.signature(atem_DayNameSet.__init__)
    params = list(sig.parameters.keys())
    assert "dslDayNameSet_Values" in params, "Missing parameter 'dslDayNameSet_Values'"

def test_atem_daynameset_has_dslDayNameSet_Values():
    assert hasattr(atem_DayNameSet, "dslDayNameSet_Values")
    descriptor = None
    for klass in atem_DayNameSet.__mro__:
        if "dslDayNameSet_Values" in klass.__dict__:
            descriptor = klass.__dict__["dslDayNameSet_Values"]
            break
    assert isinstance(descriptor, property)



def test_atem_daynamerange_is_not_abstract():
    assert not inspect.isabstract(atem_DayNameRange)


def test_atem_daynamerange_constructor_exists():
    assert callable(atem_DayNameRange.__init__)


def test_atem_daynamerange_constructor_args():
    sig = inspect.signature(atem_DayNameRange.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_DayNameRange_from" in params, "Missing parameter 'dsl_DayNameRange_from'"
    assert "dsl_DayNameRange_To" in params, "Missing parameter 'dsl_DayNameRange_To'"

def test_atem_daynamerange_has_dsl_DayNameRange_from():
    assert hasattr(atem_DayNameRange, "dsl_DayNameRange_from")
    descriptor = None
    for klass in atem_DayNameRange.__mro__:
        if "dsl_DayNameRange_from" in klass.__dict__:
            descriptor = klass.__dict__["dsl_DayNameRange_from"]
            break
    assert isinstance(descriptor, property)

def test_atem_daynamerange_has_dsl_DayNameRange_To():
    assert hasattr(atem_DayNameRange, "dsl_DayNameRange_To")
    descriptor = None
    for klass in atem_DayNameRange.__mro__:
        if "dsl_DayNameRange_To" in klass.__dict__:
            descriptor = klass.__dict__["dsl_DayNameRange_To"]
            break
    assert isinstance(descriptor, property)



def test_atem_abstractdaynamecase_is_not_abstract():
    assert not inspect.isabstract(atem_AbstractDayNameCase)


def test_atem_abstractdaynamecase_constructor_exists():
    assert callable(atem_AbstractDayNameCase.__init__)


def test_atem_abstractdaynamecase_constructor_args():
    sig = inspect.signature(atem_AbstractDayNameCase.__init__)
    params = list(sig.parameters.keys())



def test_atem_whendaynamecase_is_not_abstract():
    assert not inspect.isabstract(atem_WhenDayNameCase)


def test_atem_whendaynamecase_constructor_exists():
    assert callable(atem_WhenDayNameCase.__init__)


def test_atem_whendaynamecase_constructor_args():
    sig = inspect.signature(atem_WhenDayNameCase.__init__)
    params = list(sig.parameters.keys())



def test_atem_abstractdatecase_is_not_abstract():
    assert not inspect.isabstract(atem_AbstractDateCase)


def test_atem_abstractdatecase_constructor_exists():
    assert callable(atem_AbstractDateCase.__init__)


def test_atem_abstractdatecase_constructor_args():
    sig = inspect.signature(atem_AbstractDateCase.__init__)
    params = list(sig.parameters.keys())



def test_atem_whenother_is_not_abstract():
    assert not inspect.isabstract(atem_WhenOther)


def test_atem_whenother_constructor_exists():
    assert callable(atem_WhenOther.__init__)


def test_atem_whenother_constructor_args():
    sig = inspect.signature(atem_WhenOther.__init__)
    params = list(sig.parameters.keys())



def test_atem_whendatecase_is_not_abstract():
    assert not inspect.isabstract(atem_WhenDateCase)


def test_atem_whendatecase_constructor_exists():
    assert callable(atem_WhenDateCase.__init__)


def test_atem_whendatecase_constructor_args():
    sig = inspect.signature(atem_WhenDateCase.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_WhenDate_Case_Month" in params, "Missing parameter 'dsl_WhenDate_Case_Month'"

def test_atem_whendatecase_has_dsl_WhenDate_Case_Month():
    assert hasattr(atem_WhenDateCase, "dsl_WhenDate_Case_Month")
    descriptor = None
    for klass in atem_WhenDateCase.__mro__:
        if "dsl_WhenDate_Case_Month" in klass.__dict__:
            descriptor = klass.__dict__["dsl_WhenDate_Case_Month"]
            break
    assert isinstance(descriptor, property)



def test_atem_prefacefragment_is_not_abstract():
    assert not inspect.isabstract(atem_PrefaceFragment)


def test_atem_prefacefragment_constructor_exists():
    assert callable(atem_PrefaceFragment.__init__)


def test_atem_prefacefragment_constructor_args():
    sig = inspect.signature(atem_PrefaceFragment.__init__)
    params = list(sig.parameters.keys())



def test_ldptype_is_not_abstract():
    assert not inspect.isabstract(LdpType)


def test_ldptype_constructor_exists():
    assert callable(LdpType.__init__)


def test_ldptype_constructor_args():
    sig = inspect.signature(LdpType.__init__)
    params = list(sig.parameters.keys())



def test_atem_dom_is_not_abstract():
    assert not inspect.isabstract(atem_DOM)


def test_atem_dom_constructor_exists():
    assert callable(atem_DOM.__init__)


def test_atem_dom_constructor_args():
    sig = inspect.signature(atem_DOM.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Mode" in params, "Missing parameter 'dsl_Display_Mode'"

def test_atem_dom_has_dsl_Display_Mode():
    assert hasattr(atem_DOM, "dsl_Display_Mode")
    descriptor = None
    for klass in atem_DOM.__mro__:
        if "dsl_Display_Mode" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Mode"]
            break
    assert isinstance(descriptor, property)



def test_atem_nop_is_not_abstract():
    assert not inspect.isabstract(atem_NOP)


def test_atem_nop_constructor_exists():
    assert callable(atem_NOP.__init__)


def test_atem_nop_constructor_args():
    sig = inspect.signature(atem_NOP.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Mode" in params, "Missing parameter 'dsl_Display_Mode'"

def test_atem_nop_has_dsl_Display_Mode():
    assert hasattr(atem_NOP, "dsl_Display_Mode")
    descriptor = None
    for klass in atem_NOP.__mro__:
        if "dsl_Display_Mode" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Mode"]
            break
    assert isinstance(descriptor, property)



def test_atem_sbt_is_not_abstract():
    assert not inspect.isabstract(atem_SBT)


def test_atem_sbt_constructor_exists():
    assert callable(atem_SBT.__init__)


def test_atem_sbt_constructor_args():
    sig = inspect.signature(atem_SBT.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_SundaysBeforeTriodion" in params, "Missing parameter 'dsl_Display_SundaysBeforeTriodion'"

def test_atem_sbt_has_dsl_Display_SundaysBeforeTriodion():
    assert hasattr(atem_SBT, "dsl_Display_SundaysBeforeTriodion")
    descriptor = None
    for klass in atem_SBT.__mro__:
        if "dsl_Display_SundaysBeforeTriodion" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_SundaysBeforeTriodion"]
            break
    assert isinstance(descriptor, property)



def test_atem_wolc_is_not_abstract():
    assert not inspect.isabstract(atem_WOLC)


def test_atem_wolc_constructor_exists():
    assert callable(atem_WOLC.__init__)


def test_atem_wolc_constructor_args():
    sig = inspect.signature(atem_WOLC.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_DayLukan" in params, "Missing parameter 'dsl_Display_DayLukan'"

def test_atem_wolc_has_dsl_Display_DayLukan():
    assert hasattr(atem_WOLC, "dsl_Display_DayLukan")
    descriptor = None
    for klass in atem_WOLC.__mro__:
        if "dsl_Display_DayLukan" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_DayLukan"]
            break
    assert isinstance(descriptor, property)



def test_atem_wdolc_is_not_abstract():
    assert not inspect.isabstract(atem_WDOLC)


def test_atem_wdolc_constructor_exists():
    assert callable(atem_WDOLC.__init__)


def test_atem_wdolc_constructor_args():
    sig = inspect.signature(atem_WDOLC.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_DayLukan" in params, "Missing parameter 'dsl_Display_DayLukan'"

def test_atem_wdolc_has_dsl_Display_DayLukan():
    assert hasattr(atem_WDOLC, "dsl_Display_DayLukan")
    descriptor = None
    for klass in atem_WDOLC.__mro__:
        if "dsl_Display_DayLukan" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_DayLukan"]
            break
    assert isinstance(descriptor, property)



def test_atem_dol_is_not_abstract():
    assert not inspect.isabstract(atem_DOL)


def test_atem_dol_constructor_exists():
    assert callable(atem_DOL.__init__)


def test_atem_dol_constructor_args():
    sig = inspect.signature(atem_DOL.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_DayLukan" in params, "Missing parameter 'dsl_Display_DayLukan'"

def test_atem_dol_has_dsl_Display_DayLukan():
    assert hasattr(atem_DOL, "dsl_Display_DayLukan")
    descriptor = None
    for klass in atem_DOL.__mro__:
        if "dsl_Display_DayLukan" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_DayLukan"]
            break
    assert isinstance(descriptor, property)



def test_atem_mow_is_not_abstract():
    assert not inspect.isabstract(atem_MOW)


def test_atem_mow_constructor_exists():
    assert callable(atem_MOW.__init__)


def test_atem_mow_constructor_args():
    sig = inspect.signature(atem_MOW.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Mode" in params, "Missing parameter 'dsl_Display_Mode'"

def test_atem_mow_has_dsl_Display_Mode():
    assert hasattr(atem_MOW, "dsl_Display_Mode")
    descriptor = None
    for klass in atem_MOW.__mro__:
        if "dsl_Display_Mode" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Mode"]
            break
    assert isinstance(descriptor, property)



def test_atem_mcd_is_not_abstract():
    assert not inspect.isabstract(atem_MCD)


def test_atem_mcd_constructor_exists():
    assert callable(atem_MCD.__init__)


def test_atem_mcd_constructor_args():
    sig = inspect.signature(atem_MCD.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_MCD_value" in params, "Missing parameter 'dsl_MCD_value'"

def test_atem_mcd_has_dsl_MCD_value():
    assert hasattr(atem_MCD, "dsl_MCD_value")
    descriptor = None
    for klass in atem_MCD.__mro__:
        if "dsl_MCD_value" in klass.__dict__:
            descriptor = klass.__dict__["dsl_MCD_value"]
            break
    assert isinstance(descriptor, property)



def test_atem_gendate_is_not_abstract():
    assert not inspect.isabstract(atem_GenDate)


def test_atem_gendate_constructor_exists():
    assert callable(atem_GenDate.__init__)


def test_atem_gendate_constructor_args():
    sig = inspect.signature(atem_GenDate.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Date" in params, "Missing parameter 'dsl_Display_Date'"

def test_atem_gendate_has_dsl_Display_Date():
    assert hasattr(atem_GenDate, "dsl_Display_Date")
    descriptor = None
    for klass in atem_GenDate.__mro__:
        if "dsl_Display_Date" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Date"]
            break
    assert isinstance(descriptor, property)



def test_atem_genyear_is_not_abstract():
    assert not inspect.isabstract(atem_GenYear)


def test_atem_genyear_constructor_exists():
    assert callable(atem_GenYear.__init__)


def test_atem_genyear_constructor_args():
    sig = inspect.signature(atem_GenYear.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Year" in params, "Missing parameter 'dsl_Display_Year'"

def test_atem_genyear_has_dsl_Display_Year():
    assert hasattr(atem_GenYear, "dsl_Display_Year")
    descriptor = None
    for klass in atem_GenYear.__mro__:
        if "dsl_Display_Year" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Year"]
            break
    assert isinstance(descriptor, property)



def test_atem_all_is_not_abstract():
    assert not inspect.isabstract(atem_All)


def test_atem_all_constructor_exists():
    assert callable(atem_All.__init__)


def test_atem_all_constructor_args():
    sig = inspect.signature(atem_All.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_LiturgicalDayProperties" in params, "Missing parameter 'dsl_Display_LiturgicalDayProperties'"

def test_atem_all_has_dsl_Display_LiturgicalDayProperties():
    assert hasattr(atem_All, "dsl_Display_LiturgicalDayProperties")
    descriptor = None
    for klass in atem_All.__mro__:
        if "dsl_Display_LiturgicalDayProperties" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_LiturgicalDayProperties"]
            break
    assert isinstance(descriptor, property)



def test_atem_sectionelementtype_is_not_abstract():
    assert not inspect.isabstract(atem_SectionElementType)


def test_atem_sectionelementtype_constructor_exists():
    assert callable(atem_SectionElementType.__init__)


def test_atem_sectionelementtype_constructor_args():
    sig = inspect.signature(atem_SectionElementType.__init__)
    params = list(sig.parameters.keys())



def test_atem_prefaceelementtype_is_not_abstract():
    assert not inspect.isabstract(atem_PrefaceElementType)


def test_atem_prefaceelementtype_constructor_exists():
    assert callable(atem_PrefaceElementType.__init__)


def test_atem_prefaceelementtype_constructor_args():
    sig = inspect.signature(atem_PrefaceElementType.__init__)
    params = list(sig.parameters.keys())



def test_atem_sol_is_not_abstract():
    assert not inspect.isabstract(atem_SOL)


def test_atem_sol_constructor_exists():
    assert callable(atem_SOL.__init__)


def test_atem_sol_constructor_args():
    sig = inspect.signature(atem_SOL.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_StartLukan" in params, "Missing parameter 'dsl_Display_StartLukan'"

def test_atem_sol_has_dsl_Display_StartLukan():
    assert hasattr(atem_SOL, "dsl_Display_StartLukan")
    descriptor = None
    for klass in atem_SOL.__mro__:
        if "dsl_Display_StartLukan" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_StartLukan"]
            break
    assert isinstance(descriptor, property)



def test_atem_saec_is_not_abstract():
    assert not inspect.isabstract(atem_SAEC)


def test_atem_saec_constructor_exists():
    assert callable(atem_SAEC.__init__)


def test_atem_saec_constructor_args():
    sig = inspect.signature(atem_SAEC.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_SundayAfterElevationCross" in params, "Missing parameter 'dsl_Display_SundayAfterElevationCross'"

def test_atem_saec_has_dsl_Display_SundayAfterElevationCross():
    assert hasattr(atem_SAEC, "dsl_Display_SundayAfterElevationCross")
    descriptor = None
    for klass in atem_SAEC.__mro__:
        if "dsl_Display_SundayAfterElevationCross" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_SundayAfterElevationCross"]
            break
    assert isinstance(descriptor, property)



def test_atem_eow_is_not_abstract():
    assert not inspect.isabstract(atem_EOW)


def test_atem_eow_constructor_exists():
    assert callable(atem_EOW.__init__)


def test_atem_eow_constructor_args():
    sig = inspect.signature(atem_EOW.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Eothinon" in params, "Missing parameter 'dsl_Display_Eothinon'"

def test_atem_eow_has_dsl_Display_Eothinon():
    assert hasattr(atem_EOW, "dsl_Display_Eothinon")
    descriptor = None
    for klass in atem_EOW.__mro__:
        if "dsl_Display_Eothinon" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Eothinon"]
            break
    assert isinstance(descriptor, property)



def test_atem_dowt_is_not_abstract():
    assert not inspect.isabstract(atem_DOWT)


def test_atem_dowt_constructor_exists():
    assert callable(atem_DOWT.__init__)


def test_atem_dowt_constructor_args():
    sig = inspect.signature(atem_DOWT.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Mode" in params, "Missing parameter 'dsl_Display_Mode'"

def test_atem_dowt_has_dsl_Display_Mode():
    assert hasattr(atem_DOWT, "dsl_Display_Mode")
    descriptor = None
    for klass in atem_DOWT.__mro__:
        if "dsl_Display_Mode" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Mode"]
            break
    assert isinstance(descriptor, property)



def test_atem_down_is_not_abstract():
    assert not inspect.isabstract(atem_DOWN)


def test_atem_down_constructor_exists():
    assert callable(atem_DOWN.__init__)


def test_atem_down_constructor_args():
    sig = inspect.signature(atem_DOWN.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Mode" in params, "Missing parameter 'dsl_Display_Mode'"

def test_atem_down_has_dsl_Display_Mode():
    assert hasattr(atem_DOWN, "dsl_Display_Mode")
    descriptor = None
    for klass in atem_DOWN.__mro__:
        if "dsl_Display_Mode" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Mode"]
            break
    assert isinstance(descriptor, property)



def test_atem_dop_is_not_abstract():
    assert not inspect.isabstract(atem_DOP)


def test_atem_dop_constructor_exists():
    assert callable(atem_DOP.__init__)


def test_atem_dop_constructor_args():
    sig = inspect.signature(atem_DOP.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Display_Mode" in params, "Missing parameter 'dsl_Display_Mode'"

def test_atem_dop_has_dsl_Display_Mode():
    assert hasattr(atem_DOP, "dsl_Display_Mode")
    descriptor = None
    for klass in atem_DOP.__mro__:
        if "dsl_Display_Mode" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Display_Mode"]
            break
    assert isinstance(descriptor, property)



def test_atem_ldptype_is_not_abstract():
    assert not inspect.isabstract(atem_LdpType)


def test_atem_ldptype_constructor_exists():
    assert callable(atem_LdpType.__init__)


def test_atem_ldptype_constructor_args():
    sig = inspect.signature(atem_LdpType.__init__)
    params = list(sig.parameters.keys())



def test_atem_definition_is_not_abstract():
    assert not inspect.isabstract(atem_Definition)


def test_atem_definition_constructor_exists():
    assert callable(atem_Definition.__init__)


def test_atem_definition_constructor_args():
    sig = inspect.signature(atem_Definition.__init__)
    params = list(sig.parameters.keys())



def test_elementtype_is_not_abstract():
    assert not inspect.isabstract(ElementType)


def test_elementtype_constructor_exists():
    assert callable(ElementType.__init__)


def test_elementtype_constructor_args():
    sig = inspect.signature(ElementType.__init__)
    params = list(sig.parameters.keys())



def test_atem_taggedtext_is_not_abstract():
    assert not inspect.isabstract(atem_TaggedText)


def test_atem_taggedtext_constructor_exists():
    assert callable(atem_TaggedText.__init__)


def test_atem_taggedtext_constructor_args():
    sig = inspect.signature(atem_TaggedText.__init__)
    params = list(sig.parameters.keys())



def test_atem_ldp_is_not_abstract():
    assert not inspect.isabstract(atem_LDP)


def test_atem_ldp_constructor_exists():
    assert callable(atem_LDP.__init__)


def test_atem_ldp_constructor_args():
    sig = inspect.signature(atem_LDP.__init__)
    params = list(sig.parameters.keys())



def test_atem_lookup_is_not_abstract():
    assert not inspect.isabstract(atem_Lookup)


def test_atem_lookup_constructor_exists():
    assert callable(atem_Lookup.__init__)


def test_atem_lookup_constructor_args():
    sig = inspect.signature(atem_Lookup.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Lookup_Media_Off" in params, "Missing parameter 'dsl_Lookup_Media_Off'"
    assert "dsl_Lookup_Override__Day_Set" in params, "Missing parameter 'dsl_Lookup_Override__Day_Set'"
    assert "dsl_Lookup_OverrideMode" in params, "Missing parameter 'dsl_Lookup_OverrideMode'"
    assert "dsl_Lookup_OverrideDay" in params, "Missing parameter 'dsl_Lookup_OverrideDay'"
    assert "dsl_Lookup_Override_Mode_Set" in params, "Missing parameter 'dsl_Lookup_Override_Mode_Set'"

def test_atem_lookup_has_dsl_Lookup_Media_Off():
    assert hasattr(atem_Lookup, "dsl_Lookup_Media_Off")
    descriptor = None
    for klass in atem_Lookup.__mro__:
        if "dsl_Lookup_Media_Off" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Lookup_Media_Off"]
            break
    assert isinstance(descriptor, property)

def test_atem_lookup_has_dsl_Lookup_Override__Day_Set():
    assert hasattr(atem_Lookup, "dsl_Lookup_Override__Day_Set")
    descriptor = None
    for klass in atem_Lookup.__mro__:
        if "dsl_Lookup_Override__Day_Set" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Lookup_Override__Day_Set"]
            break
    assert isinstance(descriptor, property)

def test_atem_lookup_has_dsl_Lookup_OverrideMode():
    assert hasattr(atem_Lookup, "dsl_Lookup_OverrideMode")
    descriptor = None
    for klass in atem_Lookup.__mro__:
        if "dsl_Lookup_OverrideMode" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Lookup_OverrideMode"]
            break
    assert isinstance(descriptor, property)

def test_atem_lookup_has_dsl_Lookup_OverrideDay():
    assert hasattr(atem_Lookup, "dsl_Lookup_OverrideDay")
    descriptor = None
    for klass in atem_Lookup.__mro__:
        if "dsl_Lookup_OverrideDay" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Lookup_OverrideDay"]
            break
    assert isinstance(descriptor, property)

def test_atem_lookup_has_dsl_Lookup_Override_Mode_Set():
    assert hasattr(atem_Lookup, "dsl_Lookup_Override_Mode_Set")
    descriptor = None
    for klass in atem_Lookup.__mro__:
        if "dsl_Lookup_Override_Mode_Set" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Lookup_Override_Mode_Set"]
            break
    assert isinstance(descriptor, property)



def test_atem_resourcetext_is_not_abstract():
    assert not inspect.isabstract(atem_ResourceText)


def test_atem_resourcetext_constructor_exists():
    assert callable(atem_ResourceText.__init__)


def test_atem_resourcetext_constructor_args():
    sig = inspect.signature(atem_ResourceText.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_ResourceText_Media_Off" in params, "Missing parameter 'dsl_ResourceText_Media_Off'"

def test_atem_resourcetext_has_dsl_ResourceText_Media_Off():
    assert hasattr(atem_ResourceText, "dsl_ResourceText_Media_Off")
    descriptor = None
    for klass in atem_ResourceText.__mro__:
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



def test_atem_infoelementtype_is_not_abstract():
    assert not inspect.isabstract(atem_InfoElementType)


def test_atem_infoelementtype_constructor_exists():
    assert callable(atem_InfoElementType.__init__)


def test_atem_infoelementtype_constructor_args():
    sig = inspect.signature(atem_InfoElementType.__init__)
    params = list(sig.parameters.keys())



def test_atem_elementtype_is_not_abstract():
    assert not inspect.isabstract(atem_ElementType)


def test_atem_elementtype_constructor_exists():
    assert callable(atem_ElementType.__init__)


def test_atem_elementtype_constructor_args():
    sig = inspect.signature(atem_ElementType.__init__)
    params = list(sig.parameters.keys())



def test_headerfooterfragment_is_not_abstract():
    assert not inspect.isabstract(HeaderFooterFragment)


def test_headerfooterfragment_constructor_exists():
    assert callable(HeaderFooterFragment.__init__)


def test_headerfooterfragment_constructor_args():
    sig = inspect.signature(HeaderFooterFragment.__init__)
    params = list(sig.parameters.keys())



def test_atem_headerfootertitle_is_not_abstract():
    assert not inspect.isabstract(atem_HeaderFooterTitle)


def test_atem_headerfootertitle_constructor_exists():
    assert callable(atem_HeaderFooterTitle.__init__)


def test_atem_headerfootertitle_constructor_args():
    sig = inspect.signature(atem_HeaderFooterTitle.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_HeaderFooterTitle" in params, "Missing parameter 'dsl_HeaderFooterTitle'"

def test_atem_headerfootertitle_has_dsl_HeaderFooterTitle():
    assert hasattr(atem_HeaderFooterTitle, "dsl_HeaderFooterTitle")
    descriptor = None
    for klass in atem_HeaderFooterTitle.__mro__:
        if "dsl_HeaderFooterTitle" in klass.__dict__:
            descriptor = klass.__dict__["dsl_HeaderFooterTitle"]
            break
    assert isinstance(descriptor, property)



def test_atem_headerfootercommemoration_is_not_abstract():
    assert not inspect.isabstract(atem_HeaderFooterCommemoration)


def test_atem_headerfootercommemoration_constructor_exists():
    assert callable(atem_HeaderFooterCommemoration.__init__)


def test_atem_headerfootercommemoration_constructor_args():
    sig = inspect.signature(atem_HeaderFooterCommemoration.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_HeaderFooterCommemoration" in params, "Missing parameter 'dsl_HeaderFooterCommemoration'"

def test_atem_headerfootercommemoration_has_dsl_HeaderFooterCommemoration():
    assert hasattr(atem_HeaderFooterCommemoration, "dsl_HeaderFooterCommemoration")
    descriptor = None
    for klass in atem_HeaderFooterCommemoration.__mro__:
        if "dsl_HeaderFooterCommemoration" in klass.__dict__:
            descriptor = klass.__dict__["dsl_HeaderFooterCommemoration"]
            break
    assert isinstance(descriptor, property)



def test_atem_headerfooterlookup_is_not_abstract():
    assert not inspect.isabstract(atem_HeaderFooterLookup)


def test_atem_headerfooterlookup_constructor_exists():
    assert callable(atem_HeaderFooterLookup.__init__)


def test_atem_headerfooterlookup_constructor_args():
    sig = inspect.signature(atem_HeaderFooterLookup.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_HeaderFooterLookup_Language" in params, "Missing parameter 'dsl_HeaderFooterLookup_Language'"

def test_atem_headerfooterlookup_has_dsl_HeaderFooterLookup_Language():
    assert hasattr(atem_HeaderFooterLookup, "dsl_HeaderFooterLookup_Language")
    descriptor = None
    for klass in atem_HeaderFooterLookup.__mro__:
        if "dsl_HeaderFooterLookup_Language" in klass.__dict__:
            descriptor = klass.__dict__["dsl_HeaderFooterLookup_Language"]
            break
    assert isinstance(descriptor, property)



def test_atem_headerfooterpagenumber_is_not_abstract():
    assert not inspect.isabstract(atem_HeaderFooterPageNumber)


def test_atem_headerfooterpagenumber_constructor_exists():
    assert callable(atem_HeaderFooterPageNumber.__init__)


def test_atem_headerfooterpagenumber_constructor_args():
    sig = inspect.signature(atem_HeaderFooterPageNumber.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_HeaderFooterPageNumber" in params, "Missing parameter 'dsl_HeaderFooterPageNumber'"

def test_atem_headerfooterpagenumber_has_dsl_HeaderFooterPageNumber():
    assert hasattr(atem_HeaderFooterPageNumber, "dsl_HeaderFooterPageNumber")
    descriptor = None
    for klass in atem_HeaderFooterPageNumber.__mro__:
        if "dsl_HeaderFooterPageNumber" in klass.__dict__:
            descriptor = klass.__dict__["dsl_HeaderFooterPageNumber"]
            break
    assert isinstance(descriptor, property)



def test_atem_headerfooterdate_is_not_abstract():
    assert not inspect.isabstract(atem_HeaderFooterDate)


def test_atem_headerfooterdate_constructor_exists():
    assert callable(atem_HeaderFooterDate.__init__)


def test_atem_headerfooterdate_constructor_args():
    sig = inspect.signature(atem_HeaderFooterDate.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_HeaderFooterDate" in params, "Missing parameter 'dsl_HeaderFooterDate'"
    assert "dsl_HeaderFooterDate_Language" in params, "Missing parameter 'dsl_HeaderFooterDate_Language'"

def test_atem_headerfooterdate_has_dsl_HeaderFooterDate():
    assert hasattr(atem_HeaderFooterDate, "dsl_HeaderFooterDate")
    descriptor = None
    for klass in atem_HeaderFooterDate.__mro__:
        if "dsl_HeaderFooterDate" in klass.__dict__:
            descriptor = klass.__dict__["dsl_HeaderFooterDate"]
            break
    assert isinstance(descriptor, property)

def test_atem_headerfooterdate_has_dsl_HeaderFooterDate_Language():
    assert hasattr(atem_HeaderFooterDate, "dsl_HeaderFooterDate_Language")
    descriptor = None
    for klass in atem_HeaderFooterDate.__mro__:
        if "dsl_HeaderFooterDate_Language" in klass.__dict__:
            descriptor = klass.__dict__["dsl_HeaderFooterDate_Language"]
            break
    assert isinstance(descriptor, property)



def test_atem_headerfootertext_is_not_abstract():
    assert not inspect.isabstract(atem_HeaderFooterText)


def test_atem_headerfootertext_constructor_exists():
    assert callable(atem_HeaderFooterText.__init__)


def test_atem_headerfootertext_constructor_args():
    sig = inspect.signature(atem_HeaderFooterText.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_HeaderFooterText" in params, "Missing parameter 'dsl_HeaderFooterText'"

def test_atem_headerfootertext_has_dsl_HeaderFooterText():
    assert hasattr(atem_HeaderFooterText, "dsl_HeaderFooterText")
    descriptor = None
    for klass in atem_HeaderFooterText.__mro__:
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



def test_atem_headerfootercolumnright_is_not_abstract():
    assert not inspect.isabstract(atem_HeaderFooterColumnRight)


def test_atem_headerfootercolumnright_constructor_exists():
    assert callable(atem_HeaderFooterColumnRight.__init__)


def test_atem_headerfootercolumnright_constructor_args():
    sig = inspect.signature(atem_HeaderFooterColumnRight.__init__)
    params = list(sig.parameters.keys())



def test_atem_headerfootercolumncenter_is_not_abstract():
    assert not inspect.isabstract(atem_HeaderFooterColumnCenter)


def test_atem_headerfootercolumncenter_constructor_exists():
    assert callable(atem_HeaderFooterColumnCenter.__init__)


def test_atem_headerfootercolumncenter_constructor_args():
    sig = inspect.signature(atem_HeaderFooterColumnCenter.__init__)
    params = list(sig.parameters.keys())



def test_atem_headerfootercolumnleft_is_not_abstract():
    assert not inspect.isabstract(atem_HeaderFooterColumnLeft)


def test_atem_headerfootercolumnleft_constructor_exists():
    assert callable(atem_HeaderFooterColumnLeft.__init__)


def test_atem_headerfootercolumnleft_constructor_args():
    sig = inspect.signature(atem_HeaderFooterColumnLeft.__init__)
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



def test_atem_actor_is_not_abstract():
    assert not inspect.isabstract(atem_Actor)


def test_atem_actor_constructor_exists():
    assert callable(atem_Actor.__init__)


def test_atem_actor_constructor_args():
    sig = inspect.signature(atem_Actor.__init__)
    params = list(sig.parameters.keys())



def test_atem_templatefragment_is_not_abstract():
    assert not inspect.isabstract(atem_TemplateFragment)


def test_atem_templatefragment_constructor_exists():
    assert callable(atem_TemplateFragment.__init__)


def test_atem_templatefragment_constructor_args():
    sig = inspect.signature(atem_TemplateFragment.__init__)
    params = list(sig.parameters.keys())



def test_atem_hymn_is_not_abstract():
    assert not inspect.isabstract(atem_Hymn)


def test_atem_hymn_constructor_exists():
    assert callable(atem_Hymn.__init__)


def test_atem_hymn_constructor_args():
    sig = inspect.signature(atem_Hymn.__init__)
    params = list(sig.parameters.keys())



def test_atem_litbook_is_not_abstract():
    assert not inspect.isabstract(atem_LitBook)


def test_atem_litbook_constructor_exists():
    assert callable(atem_LitBook.__init__)


def test_atem_litbook_constructor_args():
    sig = inspect.signature(atem_LitBook.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atem_litbook_has_name():
    assert hasattr(atem_LitBook, "name")
    descriptor = None
    for klass in atem_LitBook.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atem_subtitle_is_not_abstract():
    assert not inspect.isabstract(atem_SubTitle)


def test_atem_subtitle_constructor_exists():
    assert callable(atem_SubTitle.__init__)


def test_atem_subtitle_constructor_args():
    sig = inspect.signature(atem_SubTitle.__init__)
    params = list(sig.parameters.keys())



def test_atem_paragraph_is_not_abstract():
    assert not inspect.isabstract(atem_Paragraph)


def test_atem_paragraph_constructor_exists():
    assert callable(atem_Paragraph.__init__)


def test_atem_paragraph_constructor_args():
    sig = inspect.signature(atem_Paragraph.__init__)
    params = list(sig.parameters.keys())



def test_atem_setlocale_is_not_abstract():
    assert not inspect.isabstract(atem_SetLocale)


def test_atem_setlocale_constructor_exists():
    assert callable(atem_SetLocale.__init__)


def test_atem_setlocale_constructor_args():
    sig = inspect.signature(atem_SetLocale.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_SetLocale_V1" in params, "Missing parameter 'dsl_SetLocale_V1'"
    assert "dsl_SetLocale_V2" in params, "Missing parameter 'dsl_SetLocale_V2'"

def test_atem_setlocale_has_dsl_SetLocale_V1():
    assert hasattr(atem_SetLocale, "dsl_SetLocale_V1")
    descriptor = None
    for klass in atem_SetLocale.__mro__:
        if "dsl_SetLocale_V1" in klass.__dict__:
            descriptor = klass.__dict__["dsl_SetLocale_V1"]
            break
    assert isinstance(descriptor, property)

def test_atem_setlocale_has_dsl_SetLocale_V2():
    assert hasattr(atem_SetLocale, "dsl_SetLocale_V2")
    descriptor = None
    for klass in atem_SetLocale.__mro__:
        if "dsl_SetLocale_V2" in klass.__dict__:
            descriptor = klass.__dict__["dsl_SetLocale_V2"]
            break
    assert isinstance(descriptor, property)



def test_atem_whentriodionday_is_not_abstract():
    assert not inspect.isabstract(atem_WhenTriodionDay)


def test_atem_whentriodionday_constructor_exists():
    assert callable(atem_WhenTriodionDay.__init__)


def test_atem_whentriodionday_constructor_args():
    sig = inspect.signature(atem_WhenTriodionDay.__init__)
    params = list(sig.parameters.keys())



def test_atem_whenmovablecycleday_is_not_abstract():
    assert not inspect.isabstract(atem_WhenMovableCycleDay)


def test_atem_whenmovablecycleday_constructor_exists():
    assert callable(atem_WhenMovableCycleDay.__init__)


def test_atem_whenmovablecycleday_constructor_args():
    sig = inspect.signature(atem_WhenMovableCycleDay.__init__)
    params = list(sig.parameters.keys())



def test_atem_aid_is_not_abstract():
    assert not inspect.isabstract(atem_Aid)


def test_atem_aid_constructor_exists():
    assert callable(atem_Aid.__init__)


def test_atem_aid_constructor_args():
    sig = inspect.signature(atem_Aid.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atem_aid_has_name():
    assert hasattr(atem_Aid, "name")
    descriptor = None
    for klass in atem_Aid.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atem_whenlukancycleday_is_not_abstract():
    assert not inspect.isabstract(atem_WhenLukanCycleDay)


def test_atem_whenlukancycleday_constructor_exists():
    assert callable(atem_WhenLukanCycleDay.__init__)


def test_atem_whenlukancycleday_constructor_args():
    sig = inspect.signature(atem_WhenLukanCycleDay.__init__)
    params = list(sig.parameters.keys())



def test_atem_break_is_not_abstract():
    assert not inspect.isabstract(atem_Break)


def test_atem_break_constructor_exists():
    assert callable(atem_Break.__init__)


def test_atem_break_constructor_args():
    sig = inspect.signature(atem_Break.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_break_type" in params, "Missing parameter 'dsl_break_type'"

def test_atem_break_has_dsl_break_type():
    assert hasattr(atem_Break, "dsl_break_type")
    descriptor = None
    for klass in atem_Break.__mro__:
        if "dsl_break_type" in klass.__dict__:
            descriptor = klass.__dict__["dsl_break_type"]
            break
    assert isinstance(descriptor, property)



def test_atem_media_is_not_abstract():
    assert not inspect.isabstract(atem_Media)


def test_atem_media_constructor_exists():
    assert callable(atem_Media.__init__)


def test_atem_media_constructor_args():
    sig = inspect.signature(atem_Media.__init__)
    params = list(sig.parameters.keys())



def test_atem_passthroughpdf_is_not_abstract():
    assert not inspect.isabstract(atem_PassThroughPdf)


def test_atem_passthroughpdf_constructor_exists():
    assert callable(atem_PassThroughPdf.__init__)


def test_atem_passthroughpdf_constructor_args():
    sig = inspect.signature(atem_PassThroughPdf.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Passthrough_pdf_text" in params, "Missing parameter 'dsl_Passthrough_pdf_text'"

def test_atem_passthroughpdf_has_dsl_Passthrough_pdf_text():
    assert hasattr(atem_PassThroughPdf, "dsl_Passthrough_pdf_text")
    descriptor = None
    for klass in atem_PassThroughPdf.__mro__:
        if "dsl_Passthrough_pdf_text" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Passthrough_pdf_text"]
            break
    assert isinstance(descriptor, property)



def test_atem_dialog_is_not_abstract():
    assert not inspect.isabstract(atem_Dialog)


def test_atem_dialog_constructor_exists():
    assert callable(atem_Dialog.__init__)


def test_atem_dialog_constructor_args():
    sig = inspect.signature(atem_Dialog.__init__)
    params = list(sig.parameters.keys())



def test_atem_sectionfragment_is_not_abstract():
    assert not inspect.isabstract(atem_SectionFragment)


def test_atem_sectionfragment_constructor_exists():
    assert callable(atem_SectionFragment.__init__)


def test_atem_sectionfragment_constructor_args():
    sig = inspect.signature(atem_SectionFragment.__init__)
    params = list(sig.parameters.keys())



def test_atem_title_is_not_abstract():
    assert not inspect.isabstract(atem_Title)


def test_atem_title_constructor_exists():
    assert callable(atem_Title.__init__)


def test_atem_title_constructor_args():
    sig = inspect.signature(atem_Title.__init__)
    params = list(sig.parameters.keys())



def test_atem_whendayname_is_not_abstract():
    assert not inspect.isabstract(atem_WhenDayName)


def test_atem_whendayname_constructor_exists():
    assert callable(atem_WhenDayName.__init__)


def test_atem_whendayname_constructor_args():
    sig = inspect.signature(atem_WhenDayName.__init__)
    params = list(sig.parameters.keys())



def test_atem_restorelocale_is_not_abstract():
    assert not inspect.isabstract(atem_RestoreLocale)


def test_atem_restorelocale_constructor_exists():
    assert callable(atem_RestoreLocale.__init__)


def test_atem_restorelocale_constructor_args():
    sig = inspect.signature(atem_RestoreLocale.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_RestoreLocale" in params, "Missing parameter 'dsl_RestoreLocale'"

def test_atem_restorelocale_has_dsl_RestoreLocale():
    assert hasattr(atem_RestoreLocale, "dsl_RestoreLocale")
    descriptor = None
    for klass in atem_RestoreLocale.__mro__:
        if "dsl_RestoreLocale" in klass.__dict__:
            descriptor = klass.__dict__["dsl_RestoreLocale"]
            break
    assert isinstance(descriptor, property)



def test_atem_heading3_is_not_abstract():
    assert not inspect.isabstract(atem_Heading3)


def test_atem_heading3_constructor_exists():
    assert callable(atem_Heading3.__init__)


def test_atem_heading3_constructor_args():
    sig = inspect.signature(atem_Heading3.__init__)
    params = list(sig.parameters.keys())



def test_atem_rubric_is_not_abstract():
    assert not inspect.isabstract(atem_Rubric)


def test_atem_rubric_constructor_exists():
    assert callable(atem_Rubric.__init__)


def test_atem_rubric_constructor_args():
    sig = inspect.signature(atem_Rubric.__init__)
    params = list(sig.parameters.keys())



def test_atem_info_is_not_abstract():
    assert not inspect.isabstract(atem_Info)


def test_atem_info_constructor_exists():
    assert callable(atem_Info.__init__)


def test_atem_info_constructor_args():
    sig = inspect.signature(atem_Info.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atem_info_has_name():
    assert hasattr(atem_Info, "name")
    descriptor = None
    for klass in atem_Info.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atem_block_is_not_abstract():
    assert not inspect.isabstract(atem_Block)


def test_atem_block_constructor_exists():
    assert callable(atem_Block.__init__)


def test_atem_block_constructor_args():
    sig = inspect.signature(atem_Block.__init__)
    params = list(sig.parameters.keys())



def test_atem_heading1_is_not_abstract():
    assert not inspect.isabstract(atem_Heading1)


def test_atem_heading1_constructor_exists():
    assert callable(atem_Heading1.__init__)


def test_atem_heading1_constructor_args():
    sig = inspect.signature(atem_Heading1.__init__)
    params = list(sig.parameters.keys())



def test_atem_reading_is_not_abstract():
    assert not inspect.isabstract(atem_Reading)


def test_atem_reading_constructor_exists():
    assert callable(atem_Reading.__init__)


def test_atem_reading_constructor_args():
    sig = inspect.signature(atem_Reading.__init__)
    params = list(sig.parameters.keys())



def test_atem_whendate_is_not_abstract():
    assert not inspect.isabstract(atem_WhenDate)


def test_atem_whendate_constructor_exists():
    assert callable(atem_WhenDate.__init__)


def test_atem_whendate_constructor_args():
    sig = inspect.signature(atem_WhenDate.__init__)
    params = list(sig.parameters.keys())



def test_atem_whenmodeofweek_is_not_abstract():
    assert not inspect.isabstract(atem_WhenModeOfWeek)


def test_atem_whenmodeofweek_constructor_exists():
    assert callable(atem_WhenModeOfWeek.__init__)


def test_atem_whenmodeofweek_constructor_args():
    sig = inspect.signature(atem_WhenModeOfWeek.__init__)
    params = list(sig.parameters.keys())



def test_atem_whenexists_is_not_abstract():
    assert not inspect.isabstract(atem_WhenExists)


def test_atem_whenexists_constructor_exists():
    assert callable(atem_WhenExists.__init__)


def test_atem_whenexists_constructor_args():
    sig = inspect.signature(atem_WhenExists.__init__)
    params = list(sig.parameters.keys())



def test_atem_whenpascha_is_not_abstract():
    assert not inspect.isabstract(atem_WhenPascha)


def test_atem_whenpascha_constructor_exists():
    assert callable(atem_WhenPascha.__init__)


def test_atem_whenpascha_constructor_args():
    sig = inspect.signature(atem_WhenPascha.__init__)
    params = list(sig.parameters.keys())



def test_atem_whenpentecostarionday_is_not_abstract():
    assert not inspect.isabstract(atem_WhenPentecostarionDay)


def test_atem_whenpentecostarionday_constructor_exists():
    assert callable(atem_WhenPentecostarionDay.__init__)


def test_atem_whenpentecostarionday_constructor_args():
    sig = inspect.signature(atem_WhenPentecostarionDay.__init__)
    params = list(sig.parameters.keys())



def test_atem_whensundaysbeforetriodion_is_not_abstract():
    assert not inspect.isabstract(atem_WhenSundaysBeforeTriodion)


def test_atem_whensundaysbeforetriodion_constructor_exists():
    assert callable(atem_WhenSundaysBeforeTriodion.__init__)


def test_atem_whensundaysbeforetriodion_constructor_args():
    sig = inspect.signature(atem_WhenSundaysBeforeTriodion.__init__)
    params = list(sig.parameters.keys())



def test_atem_section_is_not_abstract():
    assert not inspect.isabstract(atem_Section)


def test_atem_section_constructor_exists():
    assert callable(atem_Section.__init__)


def test_atem_section_constructor_args():
    sig = inspect.signature(atem_Section.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atem_section_has_name():
    assert hasattr(atem_Section, "name")
    descriptor = None
    for klass in atem_Section.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atem_whensundayafterelevationofcrossday_is_not_abstract():
    assert not inspect.isabstract(atem_WhenSundayAfterElevationOfCrossDay)


def test_atem_whensundayafterelevationofcrossday_constructor_exists():
    assert callable(atem_WhenSundayAfterElevationOfCrossDay.__init__)


def test_atem_whensundayafterelevationofcrossday_constructor_args():
    sig = inspect.signature(atem_WhenSundayAfterElevationOfCrossDay.__init__)
    params = list(sig.parameters.keys())



def test_atem_heading2_is_not_abstract():
    assert not inspect.isabstract(atem_Heading2)


def test_atem_heading2_constructor_exists():
    assert callable(atem_Heading2.__init__)


def test_atem_heading2_constructor_args():
    sig = inspect.signature(atem_Heading2.__init__)
    params = list(sig.parameters.keys())



def test_atem_verse_is_not_abstract():
    assert not inspect.isabstract(atem_Verse)


def test_atem_verse_constructor_exists():
    assert callable(atem_Verse.__init__)


def test_atem_verse_constructor_args():
    sig = inspect.signature(atem_Verse.__init__)
    params = list(sig.parameters.keys())



def test_atem_passthroughhtml_is_not_abstract():
    assert not inspect.isabstract(atem_PassThroughHtml)


def test_atem_passthroughhtml_constructor_exists():
    assert callable(atem_PassThroughHtml.__init__)


def test_atem_passthroughhtml_constructor_args():
    sig = inspect.signature(atem_PassThroughHtml.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Passthrough_html_text" in params, "Missing parameter 'dsl_Passthrough_html_text'"

def test_atem_passthroughhtml_has_dsl_Passthrough_html_text():
    assert hasattr(atem_PassThroughHtml, "dsl_Passthrough_html_text")
    descriptor = None
    for klass in atem_PassThroughHtml.__mro__:
        if "dsl_Passthrough_html_text" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Passthrough_html_text"]
            break
    assert isinstance(descriptor, property)



def test_atem_version_is_not_abstract():
    assert not inspect.isabstract(atem_Version)


def test_atem_version_constructor_exists():
    assert callable(atem_Version.__init__)


def test_atem_version_constructor_args():
    sig = inspect.signature(atem_Version.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atem_version_has_name():
    assert hasattr(atem_Version, "name")
    descriptor = None
    for klass in atem_Version.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atem_versionswitch_is_not_abstract():
    assert not inspect.isabstract(atem_VersionSwitch)


def test_atem_versionswitch_constructor_exists():
    assert callable(atem_VersionSwitch.__init__)


def test_atem_versionswitch_constructor_args():
    sig = inspect.signature(atem_VersionSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_VersionSwitch_flag" in params, "Missing parameter 'dsl_VersionSwitch_flag'"

def test_atem_versionswitch_has_dsl_VersionSwitch_flag():
    assert hasattr(atem_VersionSwitch, "dsl_VersionSwitch_flag")
    descriptor = None
    for klass in atem_VersionSwitch.__mro__:
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



def test_atem_commemoration_is_not_abstract():
    assert not inspect.isabstract(atem_Commemoration)


def test_atem_commemoration_constructor_exists():
    assert callable(atem_Commemoration.__init__)


def test_atem_commemoration_constructor_args():
    sig = inspect.signature(atem_Commemoration.__init__)
    params = list(sig.parameters.keys())



def test_atem_pagenumber_is_not_abstract():
    assert not inspect.isabstract(atem_PageNumber)


def test_atem_pagenumber_constructor_exists():
    assert callable(atem_PageNumber.__init__)


def test_atem_pagenumber_constructor_args():
    sig = inspect.signature(atem_PageNumber.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_PageNumber_value" in params, "Missing parameter 'dsl_PageNumber_value'"

def test_atem_pagenumber_has_dsl_PageNumber_value():
    assert hasattr(atem_PageNumber, "dsl_PageNumber_value")
    descriptor = None
    for klass in atem_PageNumber.__mro__:
        if "dsl_PageNumber_value" in klass.__dict__:
            descriptor = klass.__dict__["dsl_PageNumber_value"]
            break
    assert isinstance(descriptor, property)



def test_atem_pagefooterodd_is_not_abstract():
    assert not inspect.isabstract(atem_PageFooterOdd)


def test_atem_pagefooterodd_constructor_exists():
    assert callable(atem_PageFooterOdd.__init__)


def test_atem_pagefooterodd_constructor_args():
    sig = inspect.signature(atem_PageFooterOdd.__init__)
    params = list(sig.parameters.keys())



def test_atem_date_is_not_abstract():
    assert not inspect.isabstract(atem_Date)


def test_atem_date_constructor_exists():
    assert callable(atem_Date.__init__)


def test_atem_date_constructor_args():
    sig = inspect.signature(atem_Date.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Date_month" in params, "Missing parameter 'dsl_Date_month'"
    assert "dsl_Date_day" in params, "Missing parameter 'dsl_Date_day'"
    assert "dsl_Date_year" in params, "Missing parameter 'dsl_Date_year'"

def test_atem_date_has_dsl_Date_month():
    assert hasattr(atem_Date, "dsl_Date_month")
    descriptor = None
    for klass in atem_Date.__mro__:
        if "dsl_Date_month" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Date_month"]
            break
    assert isinstance(descriptor, property)

def test_atem_date_has_dsl_Date_day():
    assert hasattr(atem_Date, "dsl_Date_day")
    descriptor = None
    for klass in atem_Date.__mro__:
        if "dsl_Date_day" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Date_day"]
            break
    assert isinstance(descriptor, property)

def test_atem_date_has_dsl_Date_year():
    assert hasattr(atem_Date, "dsl_Date_year")
    descriptor = None
    for klass in atem_Date.__mro__:
        if "dsl_Date_year" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Date_year"]
            break
    assert isinstance(descriptor, property)



def test_atem_templatetitle_is_not_abstract():
    assert not inspect.isabstract(atem_TemplateTitle)


def test_atem_templatetitle_constructor_exists():
    assert callable(atem_TemplateTitle.__init__)


def test_atem_templatetitle_constructor_args():
    sig = inspect.signature(atem_TemplateTitle.__init__)
    params = list(sig.parameters.keys())



def test_atem_pagefootereven_is_not_abstract():
    assert not inspect.isabstract(atem_PageFooterEven)


def test_atem_pagefootereven_constructor_exists():
    assert callable(atem_PageFooterEven.__init__)


def test_atem_pagefootereven_constructor_args():
    sig = inspect.signature(atem_PageFooterEven.__init__)
    params = list(sig.parameters.keys())



def test_atem_pageheaderodd_is_not_abstract():
    assert not inspect.isabstract(atem_PageHeaderOdd)


def test_atem_pageheaderodd_constructor_exists():
    assert callable(atem_PageHeaderOdd.__init__)


def test_atem_pageheaderodd_constructor_args():
    sig = inspect.signature(atem_PageHeaderOdd.__init__)
    params = list(sig.parameters.keys())



def test_atem_headerfootercolumn_is_not_abstract():
    assert not inspect.isabstract(atem_HeaderFooterColumn)


def test_atem_headerfootercolumn_constructor_exists():
    assert callable(atem_HeaderFooterColumn.__init__)


def test_atem_headerfootercolumn_constructor_args():
    sig = inspect.signature(atem_HeaderFooterColumn.__init__)
    params = list(sig.parameters.keys())



def test_atem_pageheadereven_is_not_abstract():
    assert not inspect.isabstract(atem_PageHeaderEven)


def test_atem_pageheadereven_constructor_exists():
    assert callable(atem_PageHeaderEven.__init__)


def test_atem_pageheadereven_constructor_args():
    sig = inspect.signature(atem_PageHeaderEven.__init__)
    params = list(sig.parameters.keys())



def test_atem_pagekeepwithnext_is_not_abstract():
    assert not inspect.isabstract(atem_PageKeepWithNext)


def test_atem_pagekeepwithnext_constructor_exists():
    assert callable(atem_PageKeepWithNext.__init__)


def test_atem_pagekeepwithnext_constructor_args():
    sig = inspect.signature(atem_PageKeepWithNext.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_PageKeepWithNext_value" in params, "Missing parameter 'dsl_PageKeepWithNext_value'"

def test_atem_pagekeepwithnext_has_dsl_PageKeepWithNext_value():
    assert hasattr(atem_PageKeepWithNext, "dsl_PageKeepWithNext_value")
    descriptor = None
    for klass in atem_PageKeepWithNext.__mro__:
        if "dsl_PageKeepWithNext_value" in klass.__dict__:
            descriptor = klass.__dict__["dsl_PageKeepWithNext_value"]
            break
    assert isinstance(descriptor, property)



def test_atem_headerfooterfragment_is_not_abstract():
    assert not inspect.isabstract(atem_HeaderFooterFragment)


def test_atem_headerfooterfragment_constructor_exists():
    assert callable(atem_HeaderFooterFragment.__init__)


def test_atem_headerfooterfragment_constructor_args():
    sig = inspect.signature(atem_HeaderFooterFragment.__init__)
    params = list(sig.parameters.keys())



def test_atem_preface_is_not_abstract():
    assert not inspect.isabstract(atem_Preface)


def test_atem_preface_constructor_exists():
    assert callable(atem_Preface.__init__)


def test_atem_preface_constructor_args():
    sig = inspect.signature(atem_Preface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atem_preface_has_name():
    assert hasattr(atem_Preface, "name")
    descriptor = None
    for klass in atem_Preface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atem_head_is_not_abstract():
    assert not inspect.isabstract(atem_Head)


def test_atem_head_constructor_exists():
    assert callable(atem_Head.__init__)


def test_atem_head_constructor_args():
    sig = inspect.signature(atem_Head.__init__)
    params = list(sig.parameters.keys())



def test_atem_driver_is_not_abstract():
    assert not inspect.isabstract(atem_Driver)


def test_atem_driver_constructor_exists():
    assert callable(atem_Driver.__init__)


def test_atem_driver_constructor_args():
    sig = inspect.signature(atem_Driver.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_Driver_RegEx" in params, "Missing parameter 'dsl_Driver_RegEx'"
    assert "dsl_Driver_Status" in params, "Missing parameter 'dsl_Driver_Status'"

def test_atem_driver_has_dsl_Driver_RegEx():
    assert hasattr(atem_Driver, "dsl_Driver_RegEx")
    descriptor = None
    for klass in atem_Driver.__mro__:
        if "dsl_Driver_RegEx" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Driver_RegEx"]
            break
    assert isinstance(descriptor, property)

def test_atem_driver_has_dsl_Driver_Status():
    assert hasattr(atem_Driver, "dsl_Driver_Status")
    descriptor = None
    for klass in atem_Driver.__mro__:
        if "dsl_Driver_Status" in klass.__dict__:
            descriptor = klass.__dict__["dsl_Driver_Status"]
            break
    assert isinstance(descriptor, property)



def test_atem_import_is_not_abstract():
    assert not inspect.isabstract(atem_Import)


def test_atem_import_constructor_exists():
    assert callable(atem_Import.__init__)


def test_atem_import_constructor_args():
    sig = inspect.signature(atem_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_atem_import_has_importedNamespace():
    assert hasattr(atem_Import, "importedNamespace")
    descriptor = None
    for klass in atem_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_atem_templatestatus_is_not_abstract():
    assert not inspect.isabstract(atem_TemplateStatus)


def test_atem_templatestatus_constructor_exists():
    assert callable(atem_TemplateStatus.__init__)


def test_atem_templatestatus_constructor_args():
    sig = inspect.signature(atem_TemplateStatus.__init__)
    params = list(sig.parameters.keys())
    assert "dsl_TemplateStatus" in params, "Missing parameter 'dsl_TemplateStatus'"

def test_atem_templatestatus_has_dsl_TemplateStatus():
    assert hasattr(atem_TemplateStatus, "dsl_TemplateStatus")
    descriptor = None
    for klass in atem_TemplateStatus.__mro__:
        if "dsl_TemplateStatus" in klass.__dict__:
            descriptor = klass.__dict__["dsl_TemplateStatus"]
            break
    assert isinstance(descriptor, property)



def test_atem_atemmodel_is_not_abstract():
    assert not inspect.isabstract(atem_AtemModel)


def test_atem_atemmodel_constructor_exists():
    assert callable(atem_AtemModel.__init__)


def test_atem_atemmodel_constructor_args():
    sig = inspect.signature(atem_AtemModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atem_atemmodel_has_name():
    assert hasattr(atem_AtemModel, "name")
    descriptor = None
    for klass in atem_AtemModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atem_headcomponent_is_not_abstract():
    assert not inspect.isabstract(atem_HeadComponent)


def test_atem_headcomponent_constructor_exists():
    assert callable(atem_HeadComponent.__init__)


def test_atem_headcomponent_constructor_args():
    sig = inspect.signature(atem_HeadComponent.__init__)
    params = list(sig.parameters.keys())



def test_atem_abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(atem_AbstractComponent)


def test_atem_abstractcomponent_constructor_exists():
    assert callable(atem_AbstractComponent.__init__)


def test_atem_abstractcomponent_constructor_args():
    sig = inspect.signature(atem_AbstractComponent.__init__)
    params = list(sig.parameters.keys())

def test_templatestatuses_exists():
    # Check that the Enumeration exists
    assert TemplateStatuses is not None

def test_templatestatuses_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TemplateStatuses]
    expected_literals = [
        "NA",
        "Review",
        "Draft",
        "Final",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TemplateStatuses"

def test_dowtypes_exists():
    # Check that the Enumeration exists
    assert DowTypes is not None

def test_dowtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DowTypes]
    expected_literals = [
        "D3",
        "D1",
        "D7",
        "D4",
        "D6",
        "D2",
        "D5",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DowTypes"

def test_modetypes_exists():
    # Check that the Enumeration exists
    assert ModeTypes is not None

def test_modetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModeTypes]
    expected_literals = [
        "M6",
        "M4",
        "M8",
        "M2",
        "M3",
        "M7",
        "M5",
        "M1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModeTypes"

def test_periodtype_exists():
    # Check that the Enumeration exists
    assert PeriodType is not None

def test_periodtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PeriodType]
    expected_literals = [
        "pascha",
        "triodion",
        "pentecostarion",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PeriodType"

def test_breaktype_exists():
    # Check that the Enumeration exists
    assert BreakType is not None

def test_breaktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BreakType]
    expected_literals = [
        "line",
        "page",
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
        "Jan",
        "Feb",
        "Mar",
        "Dec",
        "Aug",
        "Oct",
        "May",
        "Jun",
        "Sep",
        "Jul",
        "Nov",
        "Apr",
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
        "D07",
        "D08",
        "D14",
        "D30",
        "D06",
        "D20",
        "D26",
        "D03",
        "D05",
        "D15",
        "D04",
        "D28",
        "D23",
        "D01",
        "D31",
        "D19",
        "D09",
        "D25",
        "D21",
        "D02",
        "D17",
        "D24",
        "D22",
        "D29",
        "D18",
        "D27",
        "D10",
        "D11",
        "D13",
        "D12",
        "D16",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DayOfMonthTypes"

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
        "Horologion",
        "Katavasias",
        "Menaion",
        "Heirmologion",
        "Euchologion",
        "Octochechos",
        "Triodion",
        "Other",
        "Pentecostarion",
        "Psalter",
        "Lectionary",
        "Eothina",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BookTypes"

def test_seasons_exists():
    # Check that the Enumeration exists
    assert Seasons is not None

def test_seasons_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Seasons]
    expected_literals = [
        "Triodion",
        "Pentecostarion",
        "Apostles_Fast",
        "Nativity_Fast",
        "Dormition_Fast",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Seasons"

def test_dayofweek_exists():
    # Check that the Enumeration exists
    assert DayOfWeek is not None

def test_dayofweek_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DayOfWeek]
    expected_literals = [
        "Wednesday",
        "Tuesday",
        "Monday",
        "Sunday",
        "Thursday",
        "Saturday",
        "Friday",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DayOfWeek"

def test_versionswitchtype_exists():
    # Check that the Enumeration exists
    assert VersionSwitchType is not None

def test_versionswitchtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VersionSwitchType]
    expected_literals = [
        "Both",
        "L2",
        "L1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VersionSwitchType"


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
atem_WhenExistsCase_strategy = st.builds(
    atem_WhenExistsCase,
)
atem_WhenModeOfWeekCase_strategy = st.builds(
    atem_WhenModeOfWeekCase,
)
atem_SundaysBeforeTriodionCase_strategy = st.builds(
    atem_SundaysBeforeTriodionCase,
    dsl_SundaysBeforeTriodionCase_Days=
        st.integers()
)
atem_ModeOfWeekSet_strategy = st.builds(
    atem_ModeOfWeekSet,
    dsl_ModeOfWeekSet_MOWs=
        safe_text
)
AbstractDayCase_strategy = st.builds(
    AbstractDayCase,
)
atem_DaySet_strategy = st.builds(
    atem_DaySet,
    dslSetValue_Days=
        st.integers()
)
atem_DayRange_strategy = st.builds(
    atem_DayRange,
    dsl_Range_To=
        st.integers(),
    dsl_DayRange_from=
        st.integers()
)
atem_AbstractDayCase_strategy = st.builds(
    atem_AbstractDayCase,
)
AbstractDateCase_strategy = st.builds(
    AbstractDateCase,
)
atem_DateSet_strategy = st.builds(
    atem_DateSet,
    dslDateSet_Values=
        st.integers()
)
atem_DateRange_strategy = st.builds(
    atem_DateRange,
    dsl_DateRange_To=
        st.integers(),
    dsl_DateRange_from=
        st.integers()
)
atem_WhenPeriodCase_strategy = st.builds(
    atem_WhenPeriodCase,
)
AbstractDayNameCase_strategy = st.builds(
    AbstractDayNameCase,
)
atem_DayNameSet_strategy = st.builds(
    atem_DayNameSet,
    dslDayNameSet_Values=
        safe_text
)
atem_DayNameRange_strategy = st.builds(
    atem_DayNameRange,
    dsl_DayNameRange_from=
        safe_text,
    dsl_DayNameRange_To=
        safe_text
)
atem_AbstractDayNameCase_strategy = st.builds(
    atem_AbstractDayNameCase,
)
atem_WhenDayNameCase_strategy = st.builds(
    atem_WhenDayNameCase,
)
atem_AbstractDateCase_strategy = st.builds(
    atem_AbstractDateCase,
)
atem_WhenOther_strategy = st.builds(
    atem_WhenOther,
)
atem_WhenDateCase_strategy = st.builds(
    atem_WhenDateCase,
    dsl_WhenDate_Case_Month=
        safe_text
)
atem_PrefaceFragment_strategy = st.builds(
    atem_PrefaceFragment,
)
LdpType_strategy = st.builds(
    LdpType,
)
atem_DOM_strategy = st.builds(
    atem_DOM,
    dsl_Display_Mode=
        st.booleans()
)
atem_NOP_strategy = st.builds(
    atem_NOP,
    dsl_Display_Mode=
        st.booleans()
)
atem_SBT_strategy = st.builds(
    atem_SBT,
    dsl_Display_SundaysBeforeTriodion=
        st.booleans()
)
atem_WOLC_strategy = st.builds(
    atem_WOLC,
    dsl_Display_DayLukan=
        st.booleans()
)
atem_WDOLC_strategy = st.builds(
    atem_WDOLC,
    dsl_Display_DayLukan=
        st.booleans()
)
atem_DOL_strategy = st.builds(
    atem_DOL,
    dsl_Display_DayLukan=
        st.booleans()
)
atem_MOW_strategy = st.builds(
    atem_MOW,
    dsl_Display_Mode=
        st.booleans()
)
atem_MCD_strategy = st.builds(
    atem_MCD,
    dsl_MCD_value=
        st.booleans()
)
atem_GenDate_strategy = st.builds(
    atem_GenDate,
    dsl_Display_Date=
        st.booleans()
)
atem_GenYear_strategy = st.builds(
    atem_GenYear,
    dsl_Display_Year=
        st.booleans()
)
atem_All_strategy = st.builds(
    atem_All,
    dsl_Display_LiturgicalDayProperties=
        st.booleans()
)
atem_SectionElementType_strategy = st.builds(
    atem_SectionElementType,
)
atem_PrefaceElementType_strategy = st.builds(
    atem_PrefaceElementType,
)
atem_SOL_strategy = st.builds(
    atem_SOL,
    dsl_Display_StartLukan=
        st.booleans()
)
atem_SAEC_strategy = st.builds(
    atem_SAEC,
    dsl_Display_SundayAfterElevationCross=
        st.booleans()
)
atem_EOW_strategy = st.builds(
    atem_EOW,
    dsl_Display_Eothinon=
        st.booleans()
)
atem_DOWT_strategy = st.builds(
    atem_DOWT,
    dsl_Display_Mode=
        st.booleans()
)
atem_DOWN_strategy = st.builds(
    atem_DOWN,
    dsl_Display_Mode=
        st.booleans()
)
atem_DOP_strategy = st.builds(
    atem_DOP,
    dsl_Display_Mode=
        st.booleans()
)
atem_LdpType_strategy = st.builds(
    atem_LdpType,
)
atem_Definition_strategy = st.builds(
    atem_Definition,
)
ElementType_strategy = st.builds(
    ElementType,
)
atem_TaggedText_strategy = st.builds(
    atem_TaggedText,
)
atem_LDP_strategy = st.builds(
    atem_LDP,
)
atem_Lookup_strategy = st.builds(
    atem_Lookup,
    dsl_Lookup_Media_Off=
        st.booleans(),
    dsl_Lookup_Override__Day_Set=
        st.booleans(),
    dsl_Lookup_OverrideMode=
        safe_text,
    dsl_Lookup_OverrideDay=
        safe_text,
    dsl_Lookup_Override_Mode_Set=
        st.booleans()
)
atem_ResourceText_strategy = st.builds(
    atem_ResourceText,
    dsl_ResourceText_Media_Off=
        st.booleans()
)
SectionElementType_strategy = st.builds(
    SectionElementType,
)
atem_InfoElementType_strategy = st.builds(
    atem_InfoElementType,
)
atem_ElementType_strategy = st.builds(
    atem_ElementType,
)
HeaderFooterFragment_strategy = st.builds(
    HeaderFooterFragment,
)
atem_HeaderFooterTitle_strategy = st.builds(
    atem_HeaderFooterTitle,
    dsl_HeaderFooterTitle=
        st.booleans()
)
atem_HeaderFooterCommemoration_strategy = st.builds(
    atem_HeaderFooterCommemoration,
    dsl_HeaderFooterCommemoration=
        st.booleans()
)
atem_HeaderFooterLookup_strategy = st.builds(
    atem_HeaderFooterLookup,
    dsl_HeaderFooterLookup_Language=
        safe_text
)
atem_HeaderFooterPageNumber_strategy = st.builds(
    atem_HeaderFooterPageNumber,
    dsl_HeaderFooterPageNumber=
        st.booleans()
)
atem_HeaderFooterDate_strategy = st.builds(
    atem_HeaderFooterDate,
    dsl_HeaderFooterDate=
        st.booleans(),
    dsl_HeaderFooterDate_Language=
        safe_text
)
atem_HeaderFooterText_strategy = st.builds(
    atem_HeaderFooterText,
    dsl_HeaderFooterText=
        safe_text
)
HeaderFooterColumn_strategy = st.builds(
    HeaderFooterColumn,
)
atem_HeaderFooterColumnRight_strategy = st.builds(
    atem_HeaderFooterColumnRight,
)
atem_HeaderFooterColumnCenter_strategy = st.builds(
    atem_HeaderFooterColumnCenter,
)
atem_HeaderFooterColumnLeft_strategy = st.builds(
    atem_HeaderFooterColumnLeft,
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
atem_Actor_strategy = st.builds(
    atem_Actor,
)
atem_TemplateFragment_strategy = st.builds(
    atem_TemplateFragment,
)
atem_Hymn_strategy = st.builds(
    atem_Hymn,
)
atem_LitBook_strategy = st.builds(
    atem_LitBook,
    name=
        safe_text
)
atem_SubTitle_strategy = st.builds(
    atem_SubTitle,
)
atem_Paragraph_strategy = st.builds(
    atem_Paragraph,
)
atem_SetLocale_strategy = st.builds(
    atem_SetLocale,
    dsl_SetLocale_V1=
        safe_text,
    dsl_SetLocale_V2=
        safe_text
)
atem_WhenTriodionDay_strategy = st.builds(
    atem_WhenTriodionDay,
)
atem_WhenMovableCycleDay_strategy = st.builds(
    atem_WhenMovableCycleDay,
)
atem_Aid_strategy = st.builds(
    atem_Aid,
    name=
        safe_text
)
atem_WhenLukanCycleDay_strategy = st.builds(
    atem_WhenLukanCycleDay,
)
atem_Break_strategy = st.builds(
    atem_Break,
    dsl_break_type=
        safe_text
)
atem_Media_strategy = st.builds(
    atem_Media,
)
atem_PassThroughPdf_strategy = st.builds(
    atem_PassThroughPdf,
    dsl_Passthrough_pdf_text=
        safe_text
)
atem_Dialog_strategy = st.builds(
    atem_Dialog,
)
atem_SectionFragment_strategy = st.builds(
    atem_SectionFragment,
)
atem_Title_strategy = st.builds(
    atem_Title,
)
atem_WhenDayName_strategy = st.builds(
    atem_WhenDayName,
)
atem_RestoreLocale_strategy = st.builds(
    atem_RestoreLocale,
    dsl_RestoreLocale=
        st.booleans()
)
atem_Heading3_strategy = st.builds(
    atem_Heading3,
)
atem_Rubric_strategy = st.builds(
    atem_Rubric,
)
atem_Info_strategy = st.builds(
    atem_Info,
    name=
        safe_text
)
atem_Block_strategy = st.builds(
    atem_Block,
)
atem_Heading1_strategy = st.builds(
    atem_Heading1,
)
atem_Reading_strategy = st.builds(
    atem_Reading,
)
atem_WhenDate_strategy = st.builds(
    atem_WhenDate,
)
atem_WhenModeOfWeek_strategy = st.builds(
    atem_WhenModeOfWeek,
)
atem_WhenExists_strategy = st.builds(
    atem_WhenExists,
)
atem_WhenPascha_strategy = st.builds(
    atem_WhenPascha,
)
atem_WhenPentecostarionDay_strategy = st.builds(
    atem_WhenPentecostarionDay,
)
atem_WhenSundaysBeforeTriodion_strategy = st.builds(
    atem_WhenSundaysBeforeTriodion,
)
atem_Section_strategy = st.builds(
    atem_Section,
    name=
        safe_text
)
atem_WhenSundayAfterElevationOfCrossDay_strategy = st.builds(
    atem_WhenSundayAfterElevationOfCrossDay,
)
atem_Heading2_strategy = st.builds(
    atem_Heading2,
)
atem_Verse_strategy = st.builds(
    atem_Verse,
)
atem_PassThroughHtml_strategy = st.builds(
    atem_PassThroughHtml,
    dsl_Passthrough_html_text=
        safe_text
)
atem_Version_strategy = st.builds(
    atem_Version,
    name=
        safe_text
)
atem_VersionSwitch_strategy = st.builds(
    atem_VersionSwitch,
    dsl_VersionSwitch_flag=
        safe_text
)
HeadComponent_strategy = st.builds(
    HeadComponent,
)
atem_Commemoration_strategy = st.builds(
    atem_Commemoration,
)
atem_PageNumber_strategy = st.builds(
    atem_PageNumber,
    dsl_PageNumber_value=
        st.integers()
)
atem_PageFooterOdd_strategy = st.builds(
    atem_PageFooterOdd,
)
atem_Date_strategy = st.builds(
    atem_Date,
    dsl_Date_month=
        st.integers(),
    dsl_Date_day=
        st.integers(),
    dsl_Date_year=
        st.integers()
)
atem_TemplateTitle_strategy = st.builds(
    atem_TemplateTitle,
)
atem_PageFooterEven_strategy = st.builds(
    atem_PageFooterEven,
)
atem_PageHeaderOdd_strategy = st.builds(
    atem_PageHeaderOdd,
)
atem_HeaderFooterColumn_strategy = st.builds(
    atem_HeaderFooterColumn,
)
atem_PageHeaderEven_strategy = st.builds(
    atem_PageHeaderEven,
)
atem_PageKeepWithNext_strategy = st.builds(
    atem_PageKeepWithNext,
    dsl_PageKeepWithNext_value=
        safe_text
)
atem_HeaderFooterFragment_strategy = st.builds(
    atem_HeaderFooterFragment,
)
atem_Preface_strategy = st.builds(
    atem_Preface,
    name=
        safe_text
)
atem_Head_strategy = st.builds(
    atem_Head,
)
atem_Driver_strategy = st.builds(
    atem_Driver,
    dsl_Driver_RegEx=
        safe_text,
    dsl_Driver_Status=
        safe_text
)
atem_Import_strategy = st.builds(
    atem_Import,
    importedNamespace=
        safe_text
)
atem_TemplateStatus_strategy = st.builds(
    atem_TemplateStatus,
    dsl_TemplateStatus=
        safe_text
)
atem_AtemModel_strategy = st.builds(
    atem_AtemModel,
    name=
        safe_text
)
atem_HeadComponent_strategy = st.builds(
    atem_HeadComponent,
)
atem_AbstractComponent_strategy = st.builds(
    atem_AbstractComponent,
)

@given(instance=atem_WhenExistsCase_strategy)
@settings(max_examples=50)
def test_atem_whenexistscase_instantiation(instance):
    assert isinstance(instance, atem_WhenExistsCase)

@given(instance=atem_WhenModeOfWeekCase_strategy)
@settings(max_examples=50)
def test_atem_whenmodeofweekcase_instantiation(instance):
    assert isinstance(instance, atem_WhenModeOfWeekCase)

@given(instance=atem_SundaysBeforeTriodionCase_strategy)
@settings(max_examples=50)
def test_atem_sundaysbeforetriodioncase_instantiation(instance):
    assert isinstance(instance, atem_SundaysBeforeTriodionCase)



@given(instance=atem_SundaysBeforeTriodionCase_strategy)
def test_atem_sundaysbeforetriodioncase_dsl_SundaysBeforeTriodionCase_Days_setter(instance):
    original = instance.dsl_SundaysBeforeTriodionCase_Days
    instance.dsl_SundaysBeforeTriodionCase_Days = original
    assert instance.dsl_SundaysBeforeTriodionCase_Days == original

@given(instance=atem_ModeOfWeekSet_strategy)
@settings(max_examples=50)
def test_atem_modeofweekset_instantiation(instance):
    assert isinstance(instance, atem_ModeOfWeekSet)



@given(instance=atem_ModeOfWeekSet_strategy)
def test_atem_modeofweekset_dsl_ModeOfWeekSet_MOWs_setter(instance):
    original = instance.dsl_ModeOfWeekSet_MOWs
    instance.dsl_ModeOfWeekSet_MOWs = original
    assert instance.dsl_ModeOfWeekSet_MOWs == original

@given(instance=AbstractDayCase_strategy)
@settings(max_examples=50)
def test_abstractdaycase_instantiation(instance):
    assert isinstance(instance, AbstractDayCase)

@given(instance=atem_DaySet_strategy)
@settings(max_examples=50)
def test_atem_dayset_instantiation(instance):
    assert isinstance(instance, atem_DaySet)



@given(instance=atem_DaySet_strategy)
def test_atem_dayset_dslSetValue_Days_setter(instance):
    original = instance.dslSetValue_Days
    instance.dslSetValue_Days = original
    assert instance.dslSetValue_Days == original

@given(instance=atem_DayRange_strategy)
@settings(max_examples=50)
def test_atem_dayrange_instantiation(instance):
    assert isinstance(instance, atem_DayRange)



@given(instance=atem_DayRange_strategy)
def test_atem_dayrange_dsl_Range_To_setter(instance):
    original = instance.dsl_Range_To
    instance.dsl_Range_To = original
    assert instance.dsl_Range_To == original



@given(instance=atem_DayRange_strategy)
def test_atem_dayrange_dsl_DayRange_from_setter(instance):
    original = instance.dsl_DayRange_from
    instance.dsl_DayRange_from = original
    assert instance.dsl_DayRange_from == original

@given(instance=atem_AbstractDayCase_strategy)
@settings(max_examples=50)
def test_atem_abstractdaycase_instantiation(instance):
    assert isinstance(instance, atem_AbstractDayCase)

@given(instance=AbstractDateCase_strategy)
@settings(max_examples=50)
def test_abstractdatecase_instantiation(instance):
    assert isinstance(instance, AbstractDateCase)

@given(instance=atem_DateSet_strategy)
@settings(max_examples=50)
def test_atem_dateset_instantiation(instance):
    assert isinstance(instance, atem_DateSet)



@given(instance=atem_DateSet_strategy)
def test_atem_dateset_dslDateSet_Values_setter(instance):
    original = instance.dslDateSet_Values
    instance.dslDateSet_Values = original
    assert instance.dslDateSet_Values == original

@given(instance=atem_DateRange_strategy)
@settings(max_examples=50)
def test_atem_daterange_instantiation(instance):
    assert isinstance(instance, atem_DateRange)



@given(instance=atem_DateRange_strategy)
def test_atem_daterange_dsl_DateRange_To_setter(instance):
    original = instance.dsl_DateRange_To
    instance.dsl_DateRange_To = original
    assert instance.dsl_DateRange_To == original



@given(instance=atem_DateRange_strategy)
def test_atem_daterange_dsl_DateRange_from_setter(instance):
    original = instance.dsl_DateRange_from
    instance.dsl_DateRange_from = original
    assert instance.dsl_DateRange_from == original

@given(instance=atem_WhenPeriodCase_strategy)
@settings(max_examples=50)
def test_atem_whenperiodcase_instantiation(instance):
    assert isinstance(instance, atem_WhenPeriodCase)

@given(instance=AbstractDayNameCase_strategy)
@settings(max_examples=50)
def test_abstractdaynamecase_instantiation(instance):
    assert isinstance(instance, AbstractDayNameCase)

@given(instance=atem_DayNameSet_strategy)
@settings(max_examples=50)
def test_atem_daynameset_instantiation(instance):
    assert isinstance(instance, atem_DayNameSet)



@given(instance=atem_DayNameSet_strategy)
def test_atem_daynameset_dslDayNameSet_Values_setter(instance):
    original = instance.dslDayNameSet_Values
    instance.dslDayNameSet_Values = original
    assert instance.dslDayNameSet_Values == original

@given(instance=atem_DayNameRange_strategy)
@settings(max_examples=50)
def test_atem_daynamerange_instantiation(instance):
    assert isinstance(instance, atem_DayNameRange)



@given(instance=atem_DayNameRange_strategy)
def test_atem_daynamerange_dsl_DayNameRange_from_setter(instance):
    original = instance.dsl_DayNameRange_from
    instance.dsl_DayNameRange_from = original
    assert instance.dsl_DayNameRange_from == original



@given(instance=atem_DayNameRange_strategy)
def test_atem_daynamerange_dsl_DayNameRange_To_setter(instance):
    original = instance.dsl_DayNameRange_To
    instance.dsl_DayNameRange_To = original
    assert instance.dsl_DayNameRange_To == original

@given(instance=atem_AbstractDayNameCase_strategy)
@settings(max_examples=50)
def test_atem_abstractdaynamecase_instantiation(instance):
    assert isinstance(instance, atem_AbstractDayNameCase)

@given(instance=atem_WhenDayNameCase_strategy)
@settings(max_examples=50)
def test_atem_whendaynamecase_instantiation(instance):
    assert isinstance(instance, atem_WhenDayNameCase)

@given(instance=atem_AbstractDateCase_strategy)
@settings(max_examples=50)
def test_atem_abstractdatecase_instantiation(instance):
    assert isinstance(instance, atem_AbstractDateCase)

@given(instance=atem_WhenOther_strategy)
@settings(max_examples=50)
def test_atem_whenother_instantiation(instance):
    assert isinstance(instance, atem_WhenOther)

@given(instance=atem_WhenDateCase_strategy)
@settings(max_examples=50)
def test_atem_whendatecase_instantiation(instance):
    assert isinstance(instance, atem_WhenDateCase)



@given(instance=atem_WhenDateCase_strategy)
def test_atem_whendatecase_dsl_WhenDate_Case_Month_setter(instance):
    original = instance.dsl_WhenDate_Case_Month
    instance.dsl_WhenDate_Case_Month = original
    assert instance.dsl_WhenDate_Case_Month == original

@given(instance=atem_PrefaceFragment_strategy)
@settings(max_examples=50)
def test_atem_prefacefragment_instantiation(instance):
    assert isinstance(instance, atem_PrefaceFragment)

@given(instance=LdpType_strategy)
@settings(max_examples=50)
def test_ldptype_instantiation(instance):
    assert isinstance(instance, LdpType)

@given(instance=atem_DOM_strategy)
@settings(max_examples=50)
def test_atem_dom_instantiation(instance):
    assert isinstance(instance, atem_DOM)



@given(instance=atem_DOM_strategy)
def test_atem_dom_dsl_Display_Mode_setter(instance):
    original = instance.dsl_Display_Mode
    instance.dsl_Display_Mode = original
    assert instance.dsl_Display_Mode == original

@given(instance=atem_NOP_strategy)
@settings(max_examples=50)
def test_atem_nop_instantiation(instance):
    assert isinstance(instance, atem_NOP)



@given(instance=atem_NOP_strategy)
def test_atem_nop_dsl_Display_Mode_setter(instance):
    original = instance.dsl_Display_Mode
    instance.dsl_Display_Mode = original
    assert instance.dsl_Display_Mode == original

@given(instance=atem_SBT_strategy)
@settings(max_examples=50)
def test_atem_sbt_instantiation(instance):
    assert isinstance(instance, atem_SBT)



@given(instance=atem_SBT_strategy)
def test_atem_sbt_dsl_Display_SundaysBeforeTriodion_setter(instance):
    original = instance.dsl_Display_SundaysBeforeTriodion
    instance.dsl_Display_SundaysBeforeTriodion = original
    assert instance.dsl_Display_SundaysBeforeTriodion == original

@given(instance=atem_WOLC_strategy)
@settings(max_examples=50)
def test_atem_wolc_instantiation(instance):
    assert isinstance(instance, atem_WOLC)



@given(instance=atem_WOLC_strategy)
def test_atem_wolc_dsl_Display_DayLukan_setter(instance):
    original = instance.dsl_Display_DayLukan
    instance.dsl_Display_DayLukan = original
    assert instance.dsl_Display_DayLukan == original

@given(instance=atem_WDOLC_strategy)
@settings(max_examples=50)
def test_atem_wdolc_instantiation(instance):
    assert isinstance(instance, atem_WDOLC)



@given(instance=atem_WDOLC_strategy)
def test_atem_wdolc_dsl_Display_DayLukan_setter(instance):
    original = instance.dsl_Display_DayLukan
    instance.dsl_Display_DayLukan = original
    assert instance.dsl_Display_DayLukan == original

@given(instance=atem_DOL_strategy)
@settings(max_examples=50)
def test_atem_dol_instantiation(instance):
    assert isinstance(instance, atem_DOL)



@given(instance=atem_DOL_strategy)
def test_atem_dol_dsl_Display_DayLukan_setter(instance):
    original = instance.dsl_Display_DayLukan
    instance.dsl_Display_DayLukan = original
    assert instance.dsl_Display_DayLukan == original

@given(instance=atem_MOW_strategy)
@settings(max_examples=50)
def test_atem_mow_instantiation(instance):
    assert isinstance(instance, atem_MOW)



@given(instance=atem_MOW_strategy)
def test_atem_mow_dsl_Display_Mode_setter(instance):
    original = instance.dsl_Display_Mode
    instance.dsl_Display_Mode = original
    assert instance.dsl_Display_Mode == original

@given(instance=atem_MCD_strategy)
@settings(max_examples=50)
def test_atem_mcd_instantiation(instance):
    assert isinstance(instance, atem_MCD)



@given(instance=atem_MCD_strategy)
def test_atem_mcd_dsl_MCD_value_setter(instance):
    original = instance.dsl_MCD_value
    instance.dsl_MCD_value = original
    assert instance.dsl_MCD_value == original

@given(instance=atem_GenDate_strategy)
@settings(max_examples=50)
def test_atem_gendate_instantiation(instance):
    assert isinstance(instance, atem_GenDate)



@given(instance=atem_GenDate_strategy)
def test_atem_gendate_dsl_Display_Date_setter(instance):
    original = instance.dsl_Display_Date
    instance.dsl_Display_Date = original
    assert instance.dsl_Display_Date == original

@given(instance=atem_GenYear_strategy)
@settings(max_examples=50)
def test_atem_genyear_instantiation(instance):
    assert isinstance(instance, atem_GenYear)



@given(instance=atem_GenYear_strategy)
def test_atem_genyear_dsl_Display_Year_setter(instance):
    original = instance.dsl_Display_Year
    instance.dsl_Display_Year = original
    assert instance.dsl_Display_Year == original

@given(instance=atem_All_strategy)
@settings(max_examples=50)
def test_atem_all_instantiation(instance):
    assert isinstance(instance, atem_All)



@given(instance=atem_All_strategy)
def test_atem_all_dsl_Display_LiturgicalDayProperties_setter(instance):
    original = instance.dsl_Display_LiturgicalDayProperties
    instance.dsl_Display_LiturgicalDayProperties = original
    assert instance.dsl_Display_LiturgicalDayProperties == original

@given(instance=atem_SectionElementType_strategy)
@settings(max_examples=50)
def test_atem_sectionelementtype_instantiation(instance):
    assert isinstance(instance, atem_SectionElementType)

@given(instance=atem_PrefaceElementType_strategy)
@settings(max_examples=50)
def test_atem_prefaceelementtype_instantiation(instance):
    assert isinstance(instance, atem_PrefaceElementType)

@given(instance=atem_SOL_strategy)
@settings(max_examples=50)
def test_atem_sol_instantiation(instance):
    assert isinstance(instance, atem_SOL)



@given(instance=atem_SOL_strategy)
def test_atem_sol_dsl_Display_StartLukan_setter(instance):
    original = instance.dsl_Display_StartLukan
    instance.dsl_Display_StartLukan = original
    assert instance.dsl_Display_StartLukan == original

@given(instance=atem_SAEC_strategy)
@settings(max_examples=50)
def test_atem_saec_instantiation(instance):
    assert isinstance(instance, atem_SAEC)



@given(instance=atem_SAEC_strategy)
def test_atem_saec_dsl_Display_SundayAfterElevationCross_setter(instance):
    original = instance.dsl_Display_SundayAfterElevationCross
    instance.dsl_Display_SundayAfterElevationCross = original
    assert instance.dsl_Display_SundayAfterElevationCross == original

@given(instance=atem_EOW_strategy)
@settings(max_examples=50)
def test_atem_eow_instantiation(instance):
    assert isinstance(instance, atem_EOW)



@given(instance=atem_EOW_strategy)
def test_atem_eow_dsl_Display_Eothinon_setter(instance):
    original = instance.dsl_Display_Eothinon
    instance.dsl_Display_Eothinon = original
    assert instance.dsl_Display_Eothinon == original

@given(instance=atem_DOWT_strategy)
@settings(max_examples=50)
def test_atem_dowt_instantiation(instance):
    assert isinstance(instance, atem_DOWT)



@given(instance=atem_DOWT_strategy)
def test_atem_dowt_dsl_Display_Mode_setter(instance):
    original = instance.dsl_Display_Mode
    instance.dsl_Display_Mode = original
    assert instance.dsl_Display_Mode == original

@given(instance=atem_DOWN_strategy)
@settings(max_examples=50)
def test_atem_down_instantiation(instance):
    assert isinstance(instance, atem_DOWN)



@given(instance=atem_DOWN_strategy)
def test_atem_down_dsl_Display_Mode_setter(instance):
    original = instance.dsl_Display_Mode
    instance.dsl_Display_Mode = original
    assert instance.dsl_Display_Mode == original

@given(instance=atem_DOP_strategy)
@settings(max_examples=50)
def test_atem_dop_instantiation(instance):
    assert isinstance(instance, atem_DOP)



@given(instance=atem_DOP_strategy)
def test_atem_dop_dsl_Display_Mode_setter(instance):
    original = instance.dsl_Display_Mode
    instance.dsl_Display_Mode = original
    assert instance.dsl_Display_Mode == original

@given(instance=atem_LdpType_strategy)
@settings(max_examples=50)
def test_atem_ldptype_instantiation(instance):
    assert isinstance(instance, atem_LdpType)

@given(instance=atem_Definition_strategy)
@settings(max_examples=50)
def test_atem_definition_instantiation(instance):
    assert isinstance(instance, atem_Definition)

@given(instance=ElementType_strategy)
@settings(max_examples=50)
def test_elementtype_instantiation(instance):
    assert isinstance(instance, ElementType)

@given(instance=atem_TaggedText_strategy)
@settings(max_examples=50)
def test_atem_taggedtext_instantiation(instance):
    assert isinstance(instance, atem_TaggedText)

@given(instance=atem_LDP_strategy)
@settings(max_examples=50)
def test_atem_ldp_instantiation(instance):
    assert isinstance(instance, atem_LDP)

@given(instance=atem_Lookup_strategy)
@settings(max_examples=50)
def test_atem_lookup_instantiation(instance):
    assert isinstance(instance, atem_Lookup)



@given(instance=atem_Lookup_strategy)
def test_atem_lookup_dsl_Lookup_Media_Off_setter(instance):
    original = instance.dsl_Lookup_Media_Off
    instance.dsl_Lookup_Media_Off = original
    assert instance.dsl_Lookup_Media_Off == original



@given(instance=atem_Lookup_strategy)
def test_atem_lookup_dsl_Lookup_Override__Day_Set_setter(instance):
    original = instance.dsl_Lookup_Override__Day_Set
    instance.dsl_Lookup_Override__Day_Set = original
    assert instance.dsl_Lookup_Override__Day_Set == original



@given(instance=atem_Lookup_strategy)
def test_atem_lookup_dsl_Lookup_OverrideMode_setter(instance):
    original = instance.dsl_Lookup_OverrideMode
    instance.dsl_Lookup_OverrideMode = original
    assert instance.dsl_Lookup_OverrideMode == original



@given(instance=atem_Lookup_strategy)
def test_atem_lookup_dsl_Lookup_OverrideDay_setter(instance):
    original = instance.dsl_Lookup_OverrideDay
    instance.dsl_Lookup_OverrideDay = original
    assert instance.dsl_Lookup_OverrideDay == original



@given(instance=atem_Lookup_strategy)
def test_atem_lookup_dsl_Lookup_Override_Mode_Set_setter(instance):
    original = instance.dsl_Lookup_Override_Mode_Set
    instance.dsl_Lookup_Override_Mode_Set = original
    assert instance.dsl_Lookup_Override_Mode_Set == original

@given(instance=atem_ResourceText_strategy)
@settings(max_examples=50)
def test_atem_resourcetext_instantiation(instance):
    assert isinstance(instance, atem_ResourceText)



@given(instance=atem_ResourceText_strategy)
def test_atem_resourcetext_dsl_ResourceText_Media_Off_setter(instance):
    original = instance.dsl_ResourceText_Media_Off
    instance.dsl_ResourceText_Media_Off = original
    assert instance.dsl_ResourceText_Media_Off == original

@given(instance=SectionElementType_strategy)
@settings(max_examples=50)
def test_sectionelementtype_instantiation(instance):
    assert isinstance(instance, SectionElementType)

@given(instance=atem_InfoElementType_strategy)
@settings(max_examples=50)
def test_atem_infoelementtype_instantiation(instance):
    assert isinstance(instance, atem_InfoElementType)

@given(instance=atem_ElementType_strategy)
@settings(max_examples=50)
def test_atem_elementtype_instantiation(instance):
    assert isinstance(instance, atem_ElementType)

@given(instance=HeaderFooterFragment_strategy)
@settings(max_examples=50)
def test_headerfooterfragment_instantiation(instance):
    assert isinstance(instance, HeaderFooterFragment)

@given(instance=atem_HeaderFooterTitle_strategy)
@settings(max_examples=50)
def test_atem_headerfootertitle_instantiation(instance):
    assert isinstance(instance, atem_HeaderFooterTitle)



@given(instance=atem_HeaderFooterTitle_strategy)
def test_atem_headerfootertitle_dsl_HeaderFooterTitle_setter(instance):
    original = instance.dsl_HeaderFooterTitle
    instance.dsl_HeaderFooterTitle = original
    assert instance.dsl_HeaderFooterTitle == original

@given(instance=atem_HeaderFooterCommemoration_strategy)
@settings(max_examples=50)
def test_atem_headerfootercommemoration_instantiation(instance):
    assert isinstance(instance, atem_HeaderFooterCommemoration)



@given(instance=atem_HeaderFooterCommemoration_strategy)
def test_atem_headerfootercommemoration_dsl_HeaderFooterCommemoration_setter(instance):
    original = instance.dsl_HeaderFooterCommemoration
    instance.dsl_HeaderFooterCommemoration = original
    assert instance.dsl_HeaderFooterCommemoration == original

@given(instance=atem_HeaderFooterLookup_strategy)
@settings(max_examples=50)
def test_atem_headerfooterlookup_instantiation(instance):
    assert isinstance(instance, atem_HeaderFooterLookup)



@given(instance=atem_HeaderFooterLookup_strategy)
def test_atem_headerfooterlookup_dsl_HeaderFooterLookup_Language_setter(instance):
    original = instance.dsl_HeaderFooterLookup_Language
    instance.dsl_HeaderFooterLookup_Language = original
    assert instance.dsl_HeaderFooterLookup_Language == original

@given(instance=atem_HeaderFooterPageNumber_strategy)
@settings(max_examples=50)
def test_atem_headerfooterpagenumber_instantiation(instance):
    assert isinstance(instance, atem_HeaderFooterPageNumber)



@given(instance=atem_HeaderFooterPageNumber_strategy)
def test_atem_headerfooterpagenumber_dsl_HeaderFooterPageNumber_setter(instance):
    original = instance.dsl_HeaderFooterPageNumber
    instance.dsl_HeaderFooterPageNumber = original
    assert instance.dsl_HeaderFooterPageNumber == original

@given(instance=atem_HeaderFooterDate_strategy)
@settings(max_examples=50)
def test_atem_headerfooterdate_instantiation(instance):
    assert isinstance(instance, atem_HeaderFooterDate)



@given(instance=atem_HeaderFooterDate_strategy)
def test_atem_headerfooterdate_dsl_HeaderFooterDate_setter(instance):
    original = instance.dsl_HeaderFooterDate
    instance.dsl_HeaderFooterDate = original
    assert instance.dsl_HeaderFooterDate == original



@given(instance=atem_HeaderFooterDate_strategy)
def test_atem_headerfooterdate_dsl_HeaderFooterDate_Language_setter(instance):
    original = instance.dsl_HeaderFooterDate_Language
    instance.dsl_HeaderFooterDate_Language = original
    assert instance.dsl_HeaderFooterDate_Language == original

@given(instance=atem_HeaderFooterText_strategy)
@settings(max_examples=50)
def test_atem_headerfootertext_instantiation(instance):
    assert isinstance(instance, atem_HeaderFooterText)



@given(instance=atem_HeaderFooterText_strategy)
def test_atem_headerfootertext_dsl_HeaderFooterText_setter(instance):
    original = instance.dsl_HeaderFooterText
    instance.dsl_HeaderFooterText = original
    assert instance.dsl_HeaderFooterText == original

@given(instance=HeaderFooterColumn_strategy)
@settings(max_examples=50)
def test_headerfootercolumn_instantiation(instance):
    assert isinstance(instance, HeaderFooterColumn)

@given(instance=atem_HeaderFooterColumnRight_strategy)
@settings(max_examples=50)
def test_atem_headerfootercolumnright_instantiation(instance):
    assert isinstance(instance, atem_HeaderFooterColumnRight)

@given(instance=atem_HeaderFooterColumnCenter_strategy)
@settings(max_examples=50)
def test_atem_headerfootercolumncenter_instantiation(instance):
    assert isinstance(instance, atem_HeaderFooterColumnCenter)

@given(instance=atem_HeaderFooterColumnLeft_strategy)
@settings(max_examples=50)
def test_atem_headerfootercolumnleft_instantiation(instance):
    assert isinstance(instance, atem_HeaderFooterColumnLeft)

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

@given(instance=atem_Actor_strategy)
@settings(max_examples=50)
def test_atem_actor_instantiation(instance):
    assert isinstance(instance, atem_Actor)

@given(instance=atem_TemplateFragment_strategy)
@settings(max_examples=50)
def test_atem_templatefragment_instantiation(instance):
    assert isinstance(instance, atem_TemplateFragment)

@given(instance=atem_Hymn_strategy)
@settings(max_examples=50)
def test_atem_hymn_instantiation(instance):
    assert isinstance(instance, atem_Hymn)

@given(instance=atem_LitBook_strategy)
@settings(max_examples=50)
def test_atem_litbook_instantiation(instance):
    assert isinstance(instance, atem_LitBook)



@given(instance=atem_LitBook_strategy)
def test_atem_litbook_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atem_SubTitle_strategy)
@settings(max_examples=50)
def test_atem_subtitle_instantiation(instance):
    assert isinstance(instance, atem_SubTitle)

@given(instance=atem_Paragraph_strategy)
@settings(max_examples=50)
def test_atem_paragraph_instantiation(instance):
    assert isinstance(instance, atem_Paragraph)

@given(instance=atem_SetLocale_strategy)
@settings(max_examples=50)
def test_atem_setlocale_instantiation(instance):
    assert isinstance(instance, atem_SetLocale)



@given(instance=atem_SetLocale_strategy)
def test_atem_setlocale_dsl_SetLocale_V1_setter(instance):
    original = instance.dsl_SetLocale_V1
    instance.dsl_SetLocale_V1 = original
    assert instance.dsl_SetLocale_V1 == original



@given(instance=atem_SetLocale_strategy)
def test_atem_setlocale_dsl_SetLocale_V2_setter(instance):
    original = instance.dsl_SetLocale_V2
    instance.dsl_SetLocale_V2 = original
    assert instance.dsl_SetLocale_V2 == original

@given(instance=atem_WhenTriodionDay_strategy)
@settings(max_examples=50)
def test_atem_whentriodionday_instantiation(instance):
    assert isinstance(instance, atem_WhenTriodionDay)

@given(instance=atem_WhenMovableCycleDay_strategy)
@settings(max_examples=50)
def test_atem_whenmovablecycleday_instantiation(instance):
    assert isinstance(instance, atem_WhenMovableCycleDay)

@given(instance=atem_Aid_strategy)
@settings(max_examples=50)
def test_atem_aid_instantiation(instance):
    assert isinstance(instance, atem_Aid)



@given(instance=atem_Aid_strategy)
def test_atem_aid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atem_WhenLukanCycleDay_strategy)
@settings(max_examples=50)
def test_atem_whenlukancycleday_instantiation(instance):
    assert isinstance(instance, atem_WhenLukanCycleDay)

@given(instance=atem_Break_strategy)
@settings(max_examples=50)
def test_atem_break_instantiation(instance):
    assert isinstance(instance, atem_Break)



@given(instance=atem_Break_strategy)
def test_atem_break_dsl_break_type_setter(instance):
    original = instance.dsl_break_type
    instance.dsl_break_type = original
    assert instance.dsl_break_type == original

@given(instance=atem_Media_strategy)
@settings(max_examples=50)
def test_atem_media_instantiation(instance):
    assert isinstance(instance, atem_Media)

@given(instance=atem_PassThroughPdf_strategy)
@settings(max_examples=50)
def test_atem_passthroughpdf_instantiation(instance):
    assert isinstance(instance, atem_PassThroughPdf)



@given(instance=atem_PassThroughPdf_strategy)
def test_atem_passthroughpdf_dsl_Passthrough_pdf_text_setter(instance):
    original = instance.dsl_Passthrough_pdf_text
    instance.dsl_Passthrough_pdf_text = original
    assert instance.dsl_Passthrough_pdf_text == original

@given(instance=atem_Dialog_strategy)
@settings(max_examples=50)
def test_atem_dialog_instantiation(instance):
    assert isinstance(instance, atem_Dialog)

@given(instance=atem_SectionFragment_strategy)
@settings(max_examples=50)
def test_atem_sectionfragment_instantiation(instance):
    assert isinstance(instance, atem_SectionFragment)

@given(instance=atem_Title_strategy)
@settings(max_examples=50)
def test_atem_title_instantiation(instance):
    assert isinstance(instance, atem_Title)

@given(instance=atem_WhenDayName_strategy)
@settings(max_examples=50)
def test_atem_whendayname_instantiation(instance):
    assert isinstance(instance, atem_WhenDayName)

@given(instance=atem_RestoreLocale_strategy)
@settings(max_examples=50)
def test_atem_restorelocale_instantiation(instance):
    assert isinstance(instance, atem_RestoreLocale)



@given(instance=atem_RestoreLocale_strategy)
def test_atem_restorelocale_dsl_RestoreLocale_setter(instance):
    original = instance.dsl_RestoreLocale
    instance.dsl_RestoreLocale = original
    assert instance.dsl_RestoreLocale == original

@given(instance=atem_Heading3_strategy)
@settings(max_examples=50)
def test_atem_heading3_instantiation(instance):
    assert isinstance(instance, atem_Heading3)

@given(instance=atem_Rubric_strategy)
@settings(max_examples=50)
def test_atem_rubric_instantiation(instance):
    assert isinstance(instance, atem_Rubric)

@given(instance=atem_Info_strategy)
@settings(max_examples=50)
def test_atem_info_instantiation(instance):
    assert isinstance(instance, atem_Info)



@given(instance=atem_Info_strategy)
def test_atem_info_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atem_Block_strategy)
@settings(max_examples=50)
def test_atem_block_instantiation(instance):
    assert isinstance(instance, atem_Block)

@given(instance=atem_Heading1_strategy)
@settings(max_examples=50)
def test_atem_heading1_instantiation(instance):
    assert isinstance(instance, atem_Heading1)

@given(instance=atem_Reading_strategy)
@settings(max_examples=50)
def test_atem_reading_instantiation(instance):
    assert isinstance(instance, atem_Reading)

@given(instance=atem_WhenDate_strategy)
@settings(max_examples=50)
def test_atem_whendate_instantiation(instance):
    assert isinstance(instance, atem_WhenDate)

@given(instance=atem_WhenModeOfWeek_strategy)
@settings(max_examples=50)
def test_atem_whenmodeofweek_instantiation(instance):
    assert isinstance(instance, atem_WhenModeOfWeek)

@given(instance=atem_WhenExists_strategy)
@settings(max_examples=50)
def test_atem_whenexists_instantiation(instance):
    assert isinstance(instance, atem_WhenExists)

@given(instance=atem_WhenPascha_strategy)
@settings(max_examples=50)
def test_atem_whenpascha_instantiation(instance):
    assert isinstance(instance, atem_WhenPascha)

@given(instance=atem_WhenPentecostarionDay_strategy)
@settings(max_examples=50)
def test_atem_whenpentecostarionday_instantiation(instance):
    assert isinstance(instance, atem_WhenPentecostarionDay)

@given(instance=atem_WhenSundaysBeforeTriodion_strategy)
@settings(max_examples=50)
def test_atem_whensundaysbeforetriodion_instantiation(instance):
    assert isinstance(instance, atem_WhenSundaysBeforeTriodion)

@given(instance=atem_Section_strategy)
@settings(max_examples=50)
def test_atem_section_instantiation(instance):
    assert isinstance(instance, atem_Section)



@given(instance=atem_Section_strategy)
def test_atem_section_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atem_WhenSundayAfterElevationOfCrossDay_strategy)
@settings(max_examples=50)
def test_atem_whensundayafterelevationofcrossday_instantiation(instance):
    assert isinstance(instance, atem_WhenSundayAfterElevationOfCrossDay)

@given(instance=atem_Heading2_strategy)
@settings(max_examples=50)
def test_atem_heading2_instantiation(instance):
    assert isinstance(instance, atem_Heading2)

@given(instance=atem_Verse_strategy)
@settings(max_examples=50)
def test_atem_verse_instantiation(instance):
    assert isinstance(instance, atem_Verse)

@given(instance=atem_PassThroughHtml_strategy)
@settings(max_examples=50)
def test_atem_passthroughhtml_instantiation(instance):
    assert isinstance(instance, atem_PassThroughHtml)



@given(instance=atem_PassThroughHtml_strategy)
def test_atem_passthroughhtml_dsl_Passthrough_html_text_setter(instance):
    original = instance.dsl_Passthrough_html_text
    instance.dsl_Passthrough_html_text = original
    assert instance.dsl_Passthrough_html_text == original

@given(instance=atem_Version_strategy)
@settings(max_examples=50)
def test_atem_version_instantiation(instance):
    assert isinstance(instance, atem_Version)



@given(instance=atem_Version_strategy)
def test_atem_version_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atem_VersionSwitch_strategy)
@settings(max_examples=50)
def test_atem_versionswitch_instantiation(instance):
    assert isinstance(instance, atem_VersionSwitch)



@given(instance=atem_VersionSwitch_strategy)
def test_atem_versionswitch_dsl_VersionSwitch_flag_setter(instance):
    original = instance.dsl_VersionSwitch_flag
    instance.dsl_VersionSwitch_flag = original
    assert instance.dsl_VersionSwitch_flag == original

@given(instance=HeadComponent_strategy)
@settings(max_examples=50)
def test_headcomponent_instantiation(instance):
    assert isinstance(instance, HeadComponent)

@given(instance=atem_Commemoration_strategy)
@settings(max_examples=50)
def test_atem_commemoration_instantiation(instance):
    assert isinstance(instance, atem_Commemoration)

@given(instance=atem_PageNumber_strategy)
@settings(max_examples=50)
def test_atem_pagenumber_instantiation(instance):
    assert isinstance(instance, atem_PageNumber)



@given(instance=atem_PageNumber_strategy)
def test_atem_pagenumber_dsl_PageNumber_value_setter(instance):
    original = instance.dsl_PageNumber_value
    instance.dsl_PageNumber_value = original
    assert instance.dsl_PageNumber_value == original

@given(instance=atem_PageFooterOdd_strategy)
@settings(max_examples=50)
def test_atem_pagefooterodd_instantiation(instance):
    assert isinstance(instance, atem_PageFooterOdd)

@given(instance=atem_Date_strategy)
@settings(max_examples=50)
def test_atem_date_instantiation(instance):
    assert isinstance(instance, atem_Date)



@given(instance=atem_Date_strategy)
def test_atem_date_dsl_Date_month_setter(instance):
    original = instance.dsl_Date_month
    instance.dsl_Date_month = original
    assert instance.dsl_Date_month == original



@given(instance=atem_Date_strategy)
def test_atem_date_dsl_Date_day_setter(instance):
    original = instance.dsl_Date_day
    instance.dsl_Date_day = original
    assert instance.dsl_Date_day == original



@given(instance=atem_Date_strategy)
def test_atem_date_dsl_Date_year_setter(instance):
    original = instance.dsl_Date_year
    instance.dsl_Date_year = original
    assert instance.dsl_Date_year == original

@given(instance=atem_TemplateTitle_strategy)
@settings(max_examples=50)
def test_atem_templatetitle_instantiation(instance):
    assert isinstance(instance, atem_TemplateTitle)

@given(instance=atem_PageFooterEven_strategy)
@settings(max_examples=50)
def test_atem_pagefootereven_instantiation(instance):
    assert isinstance(instance, atem_PageFooterEven)

@given(instance=atem_PageHeaderOdd_strategy)
@settings(max_examples=50)
def test_atem_pageheaderodd_instantiation(instance):
    assert isinstance(instance, atem_PageHeaderOdd)

@given(instance=atem_HeaderFooterColumn_strategy)
@settings(max_examples=50)
def test_atem_headerfootercolumn_instantiation(instance):
    assert isinstance(instance, atem_HeaderFooterColumn)

@given(instance=atem_PageHeaderEven_strategy)
@settings(max_examples=50)
def test_atem_pageheadereven_instantiation(instance):
    assert isinstance(instance, atem_PageHeaderEven)

@given(instance=atem_PageKeepWithNext_strategy)
@settings(max_examples=50)
def test_atem_pagekeepwithnext_instantiation(instance):
    assert isinstance(instance, atem_PageKeepWithNext)



@given(instance=atem_PageKeepWithNext_strategy)
def test_atem_pagekeepwithnext_dsl_PageKeepWithNext_value_setter(instance):
    original = instance.dsl_PageKeepWithNext_value
    instance.dsl_PageKeepWithNext_value = original
    assert instance.dsl_PageKeepWithNext_value == original

@given(instance=atem_HeaderFooterFragment_strategy)
@settings(max_examples=50)
def test_atem_headerfooterfragment_instantiation(instance):
    assert isinstance(instance, atem_HeaderFooterFragment)

@given(instance=atem_Preface_strategy)
@settings(max_examples=50)
def test_atem_preface_instantiation(instance):
    assert isinstance(instance, atem_Preface)



@given(instance=atem_Preface_strategy)
def test_atem_preface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atem_Head_strategy)
@settings(max_examples=50)
def test_atem_head_instantiation(instance):
    assert isinstance(instance, atem_Head)

@given(instance=atem_Driver_strategy)
@settings(max_examples=50)
def test_atem_driver_instantiation(instance):
    assert isinstance(instance, atem_Driver)



@given(instance=atem_Driver_strategy)
def test_atem_driver_dsl_Driver_RegEx_setter(instance):
    original = instance.dsl_Driver_RegEx
    instance.dsl_Driver_RegEx = original
    assert instance.dsl_Driver_RegEx == original



@given(instance=atem_Driver_strategy)
def test_atem_driver_dsl_Driver_Status_setter(instance):
    original = instance.dsl_Driver_Status
    instance.dsl_Driver_Status = original
    assert instance.dsl_Driver_Status == original

@given(instance=atem_Import_strategy)
@settings(max_examples=50)
def test_atem_import_instantiation(instance):
    assert isinstance(instance, atem_Import)



@given(instance=atem_Import_strategy)
def test_atem_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=atem_TemplateStatus_strategy)
@settings(max_examples=50)
def test_atem_templatestatus_instantiation(instance):
    assert isinstance(instance, atem_TemplateStatus)



@given(instance=atem_TemplateStatus_strategy)
def test_atem_templatestatus_dsl_TemplateStatus_setter(instance):
    original = instance.dsl_TemplateStatus
    instance.dsl_TemplateStatus = original
    assert instance.dsl_TemplateStatus == original

@given(instance=atem_AtemModel_strategy)
@settings(max_examples=50)
def test_atem_atemmodel_instantiation(instance):
    assert isinstance(instance, atem_AtemModel)



@given(instance=atem_AtemModel_strategy)
def test_atem_atemmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atem_HeadComponent_strategy)
@settings(max_examples=50)
def test_atem_headcomponent_instantiation(instance):
    assert isinstance(instance, atem_HeadComponent)

@given(instance=atem_AbstractComponent_strategy)
@settings(max_examples=50)
def test_atem_abstractcomponent_instantiation(instance):
    assert isinstance(instance, atem_AbstractComponent)
