import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DatadiagramMLBasicDef::HeaderFooter,
    DatadiagramMLBasicDef::EventList,
    DatadiagramMLBasicDef::WindowsInfo,
    DatadiagramMLBasicDef::FaceNamesTable,
    DatadiagramMLBasicDef::FontsTable,
    DatadiagramMLBasicDef::PrintSetup,
    DatadiagramMLBasicDef::SolutionXML,
    Page,
    DatadiagramMLBasicDef::ColorsTable,
    DatadiagramMLBasicDef::DocumentSettingsElt,
    DatadiagramMLBasicDef::PageElt,
    ConnectsCollection,
    DatadiagramMLBasicDef::Connect,
    Connect,
    DatadiagramMLBasicDef::PagesCollection,
    DatadiagramMLBasicDef::MasterElt,
    Icon,
    DatadiagramMLBasicDef::MastersCollection,
    Text,
    DatadiagramMLBasicDef::TextElt,
    MasterShortCut,
    Master,
    XYABCDElt,
    DatadiagramMLBasicDef::SplineStart,
    DatadiagramMLBasicDef::EllipticalArcTo,
    DatadiagramMLBasicDef::Ellipse,
    TextElt,
    DatadiagramMLBasicDef::StringElt,
    XYABCDEElt,
    DatadiagramMLBasicDef::NURBSTo,
    DatadiagramMLBasicDef::XYABCDEElt,
    XYAElt,
    DatadiagramMLBasicDef::SplineKnot,
    DatadiagramMLBasicDef::PolylineTo,
    DatadiagramMLBasicDef::ArcTo,
    XYABElt,
    DatadiagramMLBasicDef::XYABCDElt,
    DatadiagramMLBasicDef::InfiniteLine,
    DatadiagramMLBasicDef::XYABElt,
    NURBSTo,
    SplineStart,
    EllipticalArcTo,
    Ellipse,
    Geom,
    XYElt,
    DatadiagramMLBasicDef::XYAElt,
    DatadiagramMLBasicDef::MoveTo,
    DatadiagramMLBasicDef::LineTo,
    LineTo,
    CellType,
    DelElt,
    IXElt,
    DatadiagramMLBasicDef::XYElt,
    DatadiagramMLBasicDef::DelElt,
    DatadiagramMLBasicDef::IXElt,
    InfiniteLine,
    PolylineTo,
    SplineKnot,
    ArcTo,
    MoveTo,
    DatadiagramMLBasicDef::UniqueIdElt,
    DatadiagramMLBasicDef::IdentifiedElt,
    DatadiagramMLBasicDef::NamedElt,
    PageElt,
    MasterElt,
    DatadiagramMLBasicDef::ConnectsCollection,
    DatadiagramMLBasicDef::Icon,
    DatadiagramMLBasicDef::ShapesCollection,
    UniqueIdElt,
    PageSheet,
    NamedElt,
    DatadiagramMLBasicDef::DocumentSheet,
    DatadiagramMLBasicDef::ShapeElt,
    ShapeElt,
    DatadiagramMLBasicDef::Text,
    DatadiagramMLBasicDef::Geom,
    ShapesCollection,
    DatadiagramMLBasicDef::Shape,
    DatadiagramMLBasicDef::EmailRoutingData,
    DatadiagramMLBasicDef::VBProjectData,
    DatadiagramMLBasicDef::CustomProperty,
    CustomProperty,
    DatadiagramMLBasicDef::CustomPropertiesCollection,
    IdentifiedElt,
    DatadiagramMLBasicDef::MasterShortCut,
    DatadiagramMLBasicDef::Master,
    DatadiagramMLBasicDef::Page,
    Shape,
    DatadiagramMLBasicDef::PageSheet,
    DatadiagramMLBasicDef::StyleSheet,
    StyleSheet,
    DatadiagramMLBasicDef::StyleSheetsCollection,
    VisioDocument,
    DatadiagramMLBasicDef::DocumentPropertiesCollection,
    DateTimeType,
    CustomPropertiesCollection,
    MastersCollection,
    DocumentSheet,
    StyleSheetsCollection,
    FaceNamesTable,
    FontsTable,
    PrintSetup,
    ColorsTable,
    DocumentSettingsElt,
    DocumentPropertiesCollection,
    SolutionXML,
    EmailRoutingData,
    VBProjectData,
    HeaderFooter,
    EventList,
    WindowsInfo,
    PagesCollection,
    DatadiagramMLBasicDef::DateTimeType,
    DatadiagramMLBasicDef::VisioDocument,
    DatadiagramMLBasicDef::CellType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datadiagrammlbasicdef::headerfooter_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::HeaderFooter)


def test_datadiagrammlbasicdef::headerfooter_constructor_exists():
    assert callable(DatadiagramMLBasicDef::HeaderFooter.__init__)


def test_datadiagrammlbasicdef::headerfooter_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::HeaderFooter.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::eventlist_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::EventList)


def test_datadiagrammlbasicdef::eventlist_constructor_exists():
    assert callable(DatadiagramMLBasicDef::EventList.__init__)


def test_datadiagrammlbasicdef::eventlist_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::EventList.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::windowsinfo_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::WindowsInfo)


def test_datadiagrammlbasicdef::windowsinfo_constructor_exists():
    assert callable(DatadiagramMLBasicDef::WindowsInfo.__init__)


def test_datadiagrammlbasicdef::windowsinfo_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::WindowsInfo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::facenamestable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::FaceNamesTable)


def test_datadiagrammlbasicdef::facenamestable_constructor_exists():
    assert callable(DatadiagramMLBasicDef::FaceNamesTable.__init__)


def test_datadiagrammlbasicdef::facenamestable_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::FaceNamesTable.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::fontstable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::FontsTable)


def test_datadiagrammlbasicdef::fontstable_constructor_exists():
    assert callable(DatadiagramMLBasicDef::FontsTable.__init__)


def test_datadiagrammlbasicdef::fontstable_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::FontsTable.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::printsetup_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::PrintSetup)


def test_datadiagrammlbasicdef::printsetup_constructor_exists():
    assert callable(DatadiagramMLBasicDef::PrintSetup.__init__)


def test_datadiagrammlbasicdef::printsetup_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::PrintSetup.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::solutionxml_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::SolutionXML)


def test_datadiagrammlbasicdef::solutionxml_constructor_exists():
    assert callable(DatadiagramMLBasicDef::SolutionXML.__init__)


def test_datadiagrammlbasicdef::solutionxml_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::SolutionXML.__init__)
    params = list(sig.parameters.keys())



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::colorstable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::ColorsTable)


def test_datadiagrammlbasicdef::colorstable_constructor_exists():
    assert callable(DatadiagramMLBasicDef::ColorsTable.__init__)


def test_datadiagrammlbasicdef::colorstable_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::ColorsTable.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::documentsettingselt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::DocumentSettingsElt)


def test_datadiagrammlbasicdef::documentsettingselt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::DocumentSettingsElt.__init__)


def test_datadiagrammlbasicdef::documentsettingselt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::DocumentSettingsElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::pageelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::PageElt)


def test_datadiagrammlbasicdef::pageelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::PageElt.__init__)


def test_datadiagrammlbasicdef::pageelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::PageElt.__init__)
    params = list(sig.parameters.keys())



def test_connectscollection_is_not_abstract():
    assert not inspect.isabstract(ConnectsCollection)


def test_connectscollection_constructor_exists():
    assert callable(ConnectsCollection.__init__)


def test_connectscollection_constructor_args():
    sig = inspect.signature(ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::connect_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::Connect)


def test_datadiagrammlbasicdef::connect_constructor_exists():
    assert callable(DatadiagramMLBasicDef::Connect.__init__)


def test_datadiagrammlbasicdef::connect_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::Connect.__init__)
    params = list(sig.parameters.keys())
    assert "fromCell" in params, "Missing parameter 'fromCell'"
    assert "fromSheet" in params, "Missing parameter 'fromSheet'"
    assert "toSheet" in params, "Missing parameter 'toSheet'"
    assert "fromPart" in params, "Missing parameter 'fromPart'"
    assert "toPart" in params, "Missing parameter 'toPart'"
    assert "toCell" in params, "Missing parameter 'toCell'"

def test_datadiagrammlbasicdef::connect_has_fromCell():
    assert hasattr(DatadiagramMLBasicDef::Connect, "fromCell")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Connect.__mro__:
        if "fromCell" in klass.__dict__:
            descriptor = klass.__dict__["fromCell"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::connect_has_fromSheet():
    assert hasattr(DatadiagramMLBasicDef::Connect, "fromSheet")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Connect.__mro__:
        if "fromSheet" in klass.__dict__:
            descriptor = klass.__dict__["fromSheet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::connect_has_toSheet():
    assert hasattr(DatadiagramMLBasicDef::Connect, "toSheet")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Connect.__mro__:
        if "toSheet" in klass.__dict__:
            descriptor = klass.__dict__["toSheet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::connect_has_fromPart():
    assert hasattr(DatadiagramMLBasicDef::Connect, "fromPart")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Connect.__mro__:
        if "fromPart" in klass.__dict__:
            descriptor = klass.__dict__["fromPart"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::connect_has_toPart():
    assert hasattr(DatadiagramMLBasicDef::Connect, "toPart")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Connect.__mro__:
        if "toPart" in klass.__dict__:
            descriptor = klass.__dict__["toPart"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::connect_has_toCell():
    assert hasattr(DatadiagramMLBasicDef::Connect, "toCell")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Connect.__mro__:
        if "toCell" in klass.__dict__:
            descriptor = klass.__dict__["toCell"]
            break
    assert isinstance(descriptor, property)



def test_connect_is_not_abstract():
    assert not inspect.isabstract(Connect)


def test_connect_constructor_exists():
    assert callable(Connect.__init__)


def test_connect_constructor_args():
    sig = inspect.signature(Connect.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::pagescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::PagesCollection)


def test_datadiagrammlbasicdef::pagescollection_constructor_exists():
    assert callable(DatadiagramMLBasicDef::PagesCollection.__init__)


def test_datadiagrammlbasicdef::pagescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::PagesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::masterelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::MasterElt)


def test_datadiagrammlbasicdef::masterelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::MasterElt.__init__)


def test_datadiagrammlbasicdef::masterelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::MasterElt.__init__)
    params = list(sig.parameters.keys())



def test_icon_is_not_abstract():
    assert not inspect.isabstract(Icon)


def test_icon_constructor_exists():
    assert callable(Icon.__init__)


def test_icon_constructor_args():
    sig = inspect.signature(Icon.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::masterscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::MastersCollection)


def test_datadiagrammlbasicdef::masterscollection_constructor_exists():
    assert callable(DatadiagramMLBasicDef::MastersCollection.__init__)


def test_datadiagrammlbasicdef::masterscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::MastersCollection.__init__)
    params = list(sig.parameters.keys())



def test_text_is_not_abstract():
    assert not inspect.isabstract(Text)


def test_text_constructor_exists():
    assert callable(Text.__init__)


def test_text_constructor_args():
    sig = inspect.signature(Text.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::textelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::TextElt)


def test_datadiagrammlbasicdef::textelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::TextElt.__init__)


def test_datadiagrammlbasicdef::textelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::TextElt.__init__)
    params = list(sig.parameters.keys())



def test_mastershortcut_is_not_abstract():
    assert not inspect.isabstract(MasterShortCut)


def test_mastershortcut_constructor_exists():
    assert callable(MasterShortCut.__init__)


def test_mastershortcut_constructor_args():
    sig = inspect.signature(MasterShortCut.__init__)
    params = list(sig.parameters.keys())



def test_master_is_not_abstract():
    assert not inspect.isabstract(Master)


def test_master_constructor_exists():
    assert callable(Master.__init__)


def test_master_constructor_args():
    sig = inspect.signature(Master.__init__)
    params = list(sig.parameters.keys())



def test_xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(XYABCDElt)


def test_xyabcdelt_constructor_exists():
    assert callable(XYABCDElt.__init__)


def test_xyabcdelt_constructor_args():
    sig = inspect.signature(XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::splinestart_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::SplineStart)


def test_datadiagrammlbasicdef::splinestart_constructor_exists():
    assert callable(DatadiagramMLBasicDef::SplineStart.__init__)


def test_datadiagrammlbasicdef::splinestart_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::SplineStart.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::ellipticalarcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::EllipticalArcTo)


def test_datadiagrammlbasicdef::ellipticalarcto_constructor_exists():
    assert callable(DatadiagramMLBasicDef::EllipticalArcTo.__init__)


def test_datadiagrammlbasicdef::ellipticalarcto_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::EllipticalArcTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::ellipse_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::Ellipse)


def test_datadiagrammlbasicdef::ellipse_constructor_exists():
    assert callable(DatadiagramMLBasicDef::Ellipse.__init__)


def test_datadiagrammlbasicdef::ellipse_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_textelt_is_not_abstract():
    assert not inspect.isabstract(TextElt)


def test_textelt_constructor_exists():
    assert callable(TextElt.__init__)


def test_textelt_constructor_args():
    sig = inspect.signature(TextElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::stringelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::StringElt)


def test_datadiagrammlbasicdef::stringelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::StringElt.__init__)


def test_datadiagrammlbasicdef::stringelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::StringElt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammlbasicdef::stringelt_has_value():
    assert hasattr(DatadiagramMLBasicDef::StringElt, "value")
    descriptor = None
    for klass in DatadiagramMLBasicDef::StringElt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xyabcdeelt_is_not_abstract():
    assert not inspect.isabstract(XYABCDEElt)


def test_xyabcdeelt_constructor_exists():
    assert callable(XYABCDEElt.__init__)


def test_xyabcdeelt_constructor_args():
    sig = inspect.signature(XYABCDEElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::nurbsto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::NURBSTo)


def test_datadiagrammlbasicdef::nurbsto_constructor_exists():
    assert callable(DatadiagramMLBasicDef::NURBSTo.__init__)


def test_datadiagrammlbasicdef::nurbsto_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::NURBSTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::xyabcdeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::XYABCDEElt)


def test_datadiagrammlbasicdef::xyabcdeelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::XYABCDEElt.__init__)


def test_datadiagrammlbasicdef::xyabcdeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::XYABCDEElt.__init__)
    params = list(sig.parameters.keys())



def test_xyaelt_is_not_abstract():
    assert not inspect.isabstract(XYAElt)


def test_xyaelt_constructor_exists():
    assert callable(XYAElt.__init__)


def test_xyaelt_constructor_args():
    sig = inspect.signature(XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::splineknot_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::SplineKnot)


def test_datadiagrammlbasicdef::splineknot_constructor_exists():
    assert callable(DatadiagramMLBasicDef::SplineKnot.__init__)


def test_datadiagrammlbasicdef::splineknot_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::SplineKnot.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::polylineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::PolylineTo)


def test_datadiagrammlbasicdef::polylineto_constructor_exists():
    assert callable(DatadiagramMLBasicDef::PolylineTo.__init__)


def test_datadiagrammlbasicdef::polylineto_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::PolylineTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::arcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::ArcTo)


def test_datadiagrammlbasicdef::arcto_constructor_exists():
    assert callable(DatadiagramMLBasicDef::ArcTo.__init__)


def test_datadiagrammlbasicdef::arcto_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::ArcTo.__init__)
    params = list(sig.parameters.keys())



def test_xyabelt_is_not_abstract():
    assert not inspect.isabstract(XYABElt)


def test_xyabelt_constructor_exists():
    assert callable(XYABElt.__init__)


def test_xyabelt_constructor_args():
    sig = inspect.signature(XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::XYABCDElt)


def test_datadiagrammlbasicdef::xyabcdelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::XYABCDElt.__init__)


def test_datadiagrammlbasicdef::xyabcdelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::infiniteline_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::InfiniteLine)


def test_datadiagrammlbasicdef::infiniteline_constructor_exists():
    assert callable(DatadiagramMLBasicDef::InfiniteLine.__init__)


def test_datadiagrammlbasicdef::infiniteline_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::InfiniteLine.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::xyabelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::XYABElt)


def test_datadiagrammlbasicdef::xyabelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::XYABElt.__init__)


def test_datadiagrammlbasicdef::xyabelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_nurbsto_is_not_abstract():
    assert not inspect.isabstract(NURBSTo)


def test_nurbsto_constructor_exists():
    assert callable(NURBSTo.__init__)


def test_nurbsto_constructor_args():
    sig = inspect.signature(NURBSTo.__init__)
    params = list(sig.parameters.keys())



def test_splinestart_is_not_abstract():
    assert not inspect.isabstract(SplineStart)


def test_splinestart_constructor_exists():
    assert callable(SplineStart.__init__)


def test_splinestart_constructor_args():
    sig = inspect.signature(SplineStart.__init__)
    params = list(sig.parameters.keys())



def test_ellipticalarcto_is_not_abstract():
    assert not inspect.isabstract(EllipticalArcTo)


def test_ellipticalarcto_constructor_exists():
    assert callable(EllipticalArcTo.__init__)


def test_ellipticalarcto_constructor_args():
    sig = inspect.signature(EllipticalArcTo.__init__)
    params = list(sig.parameters.keys())



def test_ellipse_is_not_abstract():
    assert not inspect.isabstract(Ellipse)


def test_ellipse_constructor_exists():
    assert callable(Ellipse.__init__)


def test_ellipse_constructor_args():
    sig = inspect.signature(Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_geom_is_not_abstract():
    assert not inspect.isabstract(Geom)


def test_geom_constructor_exists():
    assert callable(Geom.__init__)


def test_geom_constructor_args():
    sig = inspect.signature(Geom.__init__)
    params = list(sig.parameters.keys())



def test_xyelt_is_not_abstract():
    assert not inspect.isabstract(XYElt)


def test_xyelt_constructor_exists():
    assert callable(XYElt.__init__)


def test_xyelt_constructor_args():
    sig = inspect.signature(XYElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::xyaelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::XYAElt)


def test_datadiagrammlbasicdef::xyaelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::XYAElt.__init__)


def test_datadiagrammlbasicdef::xyaelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::moveto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::MoveTo)


def test_datadiagrammlbasicdef::moveto_constructor_exists():
    assert callable(DatadiagramMLBasicDef::MoveTo.__init__)


def test_datadiagrammlbasicdef::moveto_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::lineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::LineTo)


def test_datadiagrammlbasicdef::lineto_constructor_exists():
    assert callable(DatadiagramMLBasicDef::LineTo.__init__)


def test_datadiagrammlbasicdef::lineto_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::LineTo.__init__)
    params = list(sig.parameters.keys())



def test_lineto_is_not_abstract():
    assert not inspect.isabstract(LineTo)


def test_lineto_constructor_exists():
    assert callable(LineTo.__init__)


def test_lineto_constructor_args():
    sig = inspect.signature(LineTo.__init__)
    params = list(sig.parameters.keys())



def test_celltype_is_not_abstract():
    assert not inspect.isabstract(CellType)


def test_celltype_constructor_exists():
    assert callable(CellType.__init__)


def test_celltype_constructor_args():
    sig = inspect.signature(CellType.__init__)
    params = list(sig.parameters.keys())



def test_delelt_is_not_abstract():
    assert not inspect.isabstract(DelElt)


def test_delelt_constructor_exists():
    assert callable(DelElt.__init__)


def test_delelt_constructor_args():
    sig = inspect.signature(DelElt.__init__)
    params = list(sig.parameters.keys())



def test_ixelt_is_not_abstract():
    assert not inspect.isabstract(IXElt)


def test_ixelt_constructor_exists():
    assert callable(IXElt.__init__)


def test_ixelt_constructor_args():
    sig = inspect.signature(IXElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::xyelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::XYElt)


def test_datadiagrammlbasicdef::xyelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::XYElt.__init__)


def test_datadiagrammlbasicdef::xyelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::XYElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::delelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::DelElt)


def test_datadiagrammlbasicdef::delelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::DelElt.__init__)


def test_datadiagrammlbasicdef::delelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::DelElt.__init__)
    params = list(sig.parameters.keys())
    assert "del_" in params, "Missing parameter 'del_'"

def test_datadiagrammlbasicdef::delelt_has_del_():
    assert hasattr(DatadiagramMLBasicDef::DelElt, "del_")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DelElt.__mro__:
        if "del_" in klass.__dict__:
            descriptor = klass.__dict__["del_"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef::ixelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::IXElt)


def test_datadiagrammlbasicdef::ixelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::IXElt.__init__)


def test_datadiagrammlbasicdef::ixelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::IXElt.__init__)
    params = list(sig.parameters.keys())
    assert "iX" in params, "Missing parameter 'iX'"

def test_datadiagrammlbasicdef::ixelt_has_iX():
    assert hasattr(DatadiagramMLBasicDef::IXElt, "iX")
    descriptor = None
    for klass in DatadiagramMLBasicDef::IXElt.__mro__:
        if "iX" in klass.__dict__:
            descriptor = klass.__dict__["iX"]
            break
    assert isinstance(descriptor, property)



def test_infiniteline_is_not_abstract():
    assert not inspect.isabstract(InfiniteLine)


def test_infiniteline_constructor_exists():
    assert callable(InfiniteLine.__init__)


def test_infiniteline_constructor_args():
    sig = inspect.signature(InfiniteLine.__init__)
    params = list(sig.parameters.keys())



def test_polylineto_is_not_abstract():
    assert not inspect.isabstract(PolylineTo)


def test_polylineto_constructor_exists():
    assert callable(PolylineTo.__init__)


def test_polylineto_constructor_args():
    sig = inspect.signature(PolylineTo.__init__)
    params = list(sig.parameters.keys())



def test_splineknot_is_not_abstract():
    assert not inspect.isabstract(SplineKnot)


def test_splineknot_constructor_exists():
    assert callable(SplineKnot.__init__)


def test_splineknot_constructor_args():
    sig = inspect.signature(SplineKnot.__init__)
    params = list(sig.parameters.keys())



def test_arcto_is_not_abstract():
    assert not inspect.isabstract(ArcTo)


def test_arcto_constructor_exists():
    assert callable(ArcTo.__init__)


def test_arcto_constructor_args():
    sig = inspect.signature(ArcTo.__init__)
    params = list(sig.parameters.keys())



def test_moveto_is_not_abstract():
    assert not inspect.isabstract(MoveTo)


def test_moveto_constructor_exists():
    assert callable(MoveTo.__init__)


def test_moveto_constructor_args():
    sig = inspect.signature(MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::UniqueIdElt)


def test_datadiagrammlbasicdef::uniqueidelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::UniqueIdElt.__init__)


def test_datadiagrammlbasicdef::uniqueidelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::UniqueIdElt.__init__)
    params = list(sig.parameters.keys())
    assert "UniqueID" in params, "Missing parameter 'UniqueID'"

def test_datadiagrammlbasicdef::uniqueidelt_has_UniqueID():
    assert hasattr(DatadiagramMLBasicDef::UniqueIdElt, "UniqueID")
    descriptor = None
    for klass in DatadiagramMLBasicDef::UniqueIdElt.__mro__:
        if "UniqueID" in klass.__dict__:
            descriptor = klass.__dict__["UniqueID"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef::identifiedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::IdentifiedElt)


def test_datadiagrammlbasicdef::identifiedelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::IdentifiedElt.__init__)


def test_datadiagrammlbasicdef::identifiedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::IdentifiedElt.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_datadiagrammlbasicdef::identifiedelt_has_ID():
    assert hasattr(DatadiagramMLBasicDef::IdentifiedElt, "ID")
    descriptor = None
    for klass in DatadiagramMLBasicDef::IdentifiedElt.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef::namedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::NamedElt)


def test_datadiagrammlbasicdef::namedelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::NamedElt.__init__)


def test_datadiagrammlbasicdef::namedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "nameU" in params, "Missing parameter 'nameU'"
    assert "name" in params, "Missing parameter 'name'"

def test_datadiagrammlbasicdef::namedelt_has_nameU():
    assert hasattr(DatadiagramMLBasicDef::NamedElt, "nameU")
    descriptor = None
    for klass in DatadiagramMLBasicDef::NamedElt.__mro__:
        if "nameU" in klass.__dict__:
            descriptor = klass.__dict__["nameU"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::namedelt_has_name():
    assert hasattr(DatadiagramMLBasicDef::NamedElt, "name")
    descriptor = None
    for klass in DatadiagramMLBasicDef::NamedElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pageelt_is_not_abstract():
    assert not inspect.isabstract(PageElt)


def test_pageelt_constructor_exists():
    assert callable(PageElt.__init__)


def test_pageelt_constructor_args():
    sig = inspect.signature(PageElt.__init__)
    params = list(sig.parameters.keys())



def test_masterelt_is_not_abstract():
    assert not inspect.isabstract(MasterElt)


def test_masterelt_constructor_exists():
    assert callable(MasterElt.__init__)


def test_masterelt_constructor_args():
    sig = inspect.signature(MasterElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::connectscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::ConnectsCollection)


def test_datadiagrammlbasicdef::connectscollection_constructor_exists():
    assert callable(DatadiagramMLBasicDef::ConnectsCollection.__init__)


def test_datadiagrammlbasicdef::connectscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::icon_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::Icon)


def test_datadiagrammlbasicdef::icon_constructor_exists():
    assert callable(DatadiagramMLBasicDef::Icon.__init__)


def test_datadiagrammlbasicdef::icon_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::Icon.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammlbasicdef::icon_has_value():
    assert hasattr(DatadiagramMLBasicDef::Icon, "value")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Icon.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef::shapescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::ShapesCollection)


def test_datadiagrammlbasicdef::shapescollection_constructor_exists():
    assert callable(DatadiagramMLBasicDef::ShapesCollection.__init__)


def test_datadiagrammlbasicdef::shapescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(UniqueIdElt)


def test_uniqueidelt_constructor_exists():
    assert callable(UniqueIdElt.__init__)


def test_uniqueidelt_constructor_args():
    sig = inspect.signature(UniqueIdElt.__init__)
    params = list(sig.parameters.keys())



def test_pagesheet_is_not_abstract():
    assert not inspect.isabstract(PageSheet)


def test_pagesheet_constructor_exists():
    assert callable(PageSheet.__init__)


def test_pagesheet_constructor_args():
    sig = inspect.signature(PageSheet.__init__)
    params = list(sig.parameters.keys())



def test_namedelt_is_not_abstract():
    assert not inspect.isabstract(NamedElt)


def test_namedelt_constructor_exists():
    assert callable(NamedElt.__init__)


def test_namedelt_constructor_args():
    sig = inspect.signature(NamedElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::documentsheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::DocumentSheet)


def test_datadiagrammlbasicdef::documentsheet_constructor_exists():
    assert callable(DatadiagramMLBasicDef::DocumentSheet.__init__)


def test_datadiagrammlbasicdef::documentsheet_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::DocumentSheet.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::shapeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::ShapeElt)


def test_datadiagrammlbasicdef::shapeelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef::ShapeElt.__init__)


def test_datadiagrammlbasicdef::shapeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_shapeelt_is_not_abstract():
    assert not inspect.isabstract(ShapeElt)


def test_shapeelt_constructor_exists():
    assert callable(ShapeElt.__init__)


def test_shapeelt_constructor_args():
    sig = inspect.signature(ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::text_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::Text)


def test_datadiagrammlbasicdef::text_constructor_exists():
    assert callable(DatadiagramMLBasicDef::Text.__init__)


def test_datadiagrammlbasicdef::text_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::Text.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::geom_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::Geom)


def test_datadiagrammlbasicdef::geom_constructor_exists():
    assert callable(DatadiagramMLBasicDef::Geom.__init__)


def test_datadiagrammlbasicdef::geom_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::Geom.__init__)
    params = list(sig.parameters.keys())



def test_shapescollection_is_not_abstract():
    assert not inspect.isabstract(ShapesCollection)


def test_shapescollection_constructor_exists():
    assert callable(ShapesCollection.__init__)


def test_shapescollection_constructor_args():
    sig = inspect.signature(ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::shape_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::Shape)


def test_datadiagrammlbasicdef::shape_constructor_exists():
    assert callable(DatadiagramMLBasicDef::Shape.__init__)


def test_datadiagrammlbasicdef::shape_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::Shape.__init__)
    params = list(sig.parameters.keys())
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "textStyle" in params, "Missing parameter 'textStyle'"
    assert "fillStyle" in params, "Missing parameter 'fillStyle'"

def test_datadiagrammlbasicdef::shape_has_lineStyle():
    assert hasattr(DatadiagramMLBasicDef::Shape, "lineStyle")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Shape.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::shape_has_textStyle():
    assert hasattr(DatadiagramMLBasicDef::Shape, "textStyle")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Shape.__mro__:
        if "textStyle" in klass.__dict__:
            descriptor = klass.__dict__["textStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::shape_has_fillStyle():
    assert hasattr(DatadiagramMLBasicDef::Shape, "fillStyle")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Shape.__mro__:
        if "fillStyle" in klass.__dict__:
            descriptor = klass.__dict__["fillStyle"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef::emailroutingdata_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::EmailRoutingData)


def test_datadiagrammlbasicdef::emailroutingdata_constructor_exists():
    assert callable(DatadiagramMLBasicDef::EmailRoutingData.__init__)


def test_datadiagrammlbasicdef::emailroutingdata_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::EmailRoutingData.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "data" in params, "Missing parameter 'data'"

def test_datadiagrammlbasicdef::emailroutingdata_has_size():
    assert hasattr(DatadiagramMLBasicDef::EmailRoutingData, "size")
    descriptor = None
    for klass in DatadiagramMLBasicDef::EmailRoutingData.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::emailroutingdata_has_data():
    assert hasattr(DatadiagramMLBasicDef::EmailRoutingData, "data")
    descriptor = None
    for klass in DatadiagramMLBasicDef::EmailRoutingData.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef::vbprojectdata_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::VBProjectData)


def test_datadiagrammlbasicdef::vbprojectdata_constructor_exists():
    assert callable(DatadiagramMLBasicDef::VBProjectData.__init__)


def test_datadiagrammlbasicdef::vbprojectdata_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::VBProjectData.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_datadiagrammlbasicdef::vbprojectdata_has_data():
    assert hasattr(DatadiagramMLBasicDef::VBProjectData, "data")
    descriptor = None
    for klass in DatadiagramMLBasicDef::VBProjectData.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef::customproperty_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::CustomProperty)


def test_datadiagrammlbasicdef::customproperty_constructor_exists():
    assert callable(DatadiagramMLBasicDef::CustomProperty.__init__)


def test_datadiagrammlbasicdef::customproperty_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::CustomProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_datadiagrammlbasicdef::customproperty_has_name():
    assert hasattr(DatadiagramMLBasicDef::CustomProperty, "name")
    descriptor = None
    for klass in DatadiagramMLBasicDef::CustomProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::customproperty_has_dataType():
    assert hasattr(DatadiagramMLBasicDef::CustomProperty, "dataType")
    descriptor = None
    for klass in DatadiagramMLBasicDef::CustomProperty.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_customproperty_is_not_abstract():
    assert not inspect.isabstract(CustomProperty)


def test_customproperty_constructor_exists():
    assert callable(CustomProperty.__init__)


def test_customproperty_constructor_args():
    sig = inspect.signature(CustomProperty.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::custompropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::CustomPropertiesCollection)


def test_datadiagrammlbasicdef::custompropertiescollection_constructor_exists():
    assert callable(DatadiagramMLBasicDef::CustomPropertiesCollection.__init__)


def test_datadiagrammlbasicdef::custompropertiescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::CustomPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_identifiedelt_is_not_abstract():
    assert not inspect.isabstract(IdentifiedElt)


def test_identifiedelt_constructor_exists():
    assert callable(IdentifiedElt.__init__)


def test_identifiedelt_constructor_args():
    sig = inspect.signature(IdentifiedElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::mastershortcut_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::MasterShortCut)


def test_datadiagrammlbasicdef::mastershortcut_constructor_exists():
    assert callable(DatadiagramMLBasicDef::MasterShortCut.__init__)


def test_datadiagrammlbasicdef::mastershortcut_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::MasterShortCut.__init__)
    params = list(sig.parameters.keys())
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "shortcutURL" in params, "Missing parameter 'shortcutURL'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"
    assert "shortcutHelp" in params, "Missing parameter 'shortcutHelp'"

def test_datadiagrammlbasicdef::mastershortcut_has_prompt():
    assert hasattr(DatadiagramMLBasicDef::MasterShortCut, "prompt")
    descriptor = None
    for klass in DatadiagramMLBasicDef::MasterShortCut.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::mastershortcut_has_alignName():
    assert hasattr(DatadiagramMLBasicDef::MasterShortCut, "alignName")
    descriptor = None
    for klass in DatadiagramMLBasicDef::MasterShortCut.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::mastershortcut_has_patternFlags():
    assert hasattr(DatadiagramMLBasicDef::MasterShortCut, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLBasicDef::MasterShortCut.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::mastershortcut_has_shortcutURL():
    assert hasattr(DatadiagramMLBasicDef::MasterShortCut, "shortcutURL")
    descriptor = None
    for klass in DatadiagramMLBasicDef::MasterShortCut.__mro__:
        if "shortcutURL" in klass.__dict__:
            descriptor = klass.__dict__["shortcutURL"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::mastershortcut_has_iconSize():
    assert hasattr(DatadiagramMLBasicDef::MasterShortCut, "iconSize")
    descriptor = None
    for klass in DatadiagramMLBasicDef::MasterShortCut.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::mastershortcut_has_shortcutHelp():
    assert hasattr(DatadiagramMLBasicDef::MasterShortCut, "shortcutHelp")
    descriptor = None
    for klass in DatadiagramMLBasicDef::MasterShortCut.__mro__:
        if "shortcutHelp" in klass.__dict__:
            descriptor = klass.__dict__["shortcutHelp"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef::master_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::Master)


def test_datadiagrammlbasicdef::master_constructor_exists():
    assert callable(DatadiagramMLBasicDef::Master.__init__)


def test_datadiagrammlbasicdef::master_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::Master.__init__)
    params = list(sig.parameters.keys())
    assert "iconUpdate" in params, "Missing parameter 'iconUpdate'"
    assert "baseID" in params, "Missing parameter 'baseID'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"
    assert "matchByName" in params, "Missing parameter 'matchByName'"

def test_datadiagrammlbasicdef::master_has_iconUpdate():
    assert hasattr(DatadiagramMLBasicDef::Master, "iconUpdate")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Master.__mro__:
        if "iconUpdate" in klass.__dict__:
            descriptor = klass.__dict__["iconUpdate"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::master_has_baseID():
    assert hasattr(DatadiagramMLBasicDef::Master, "baseID")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Master.__mro__:
        if "baseID" in klass.__dict__:
            descriptor = klass.__dict__["baseID"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::master_has_hidden():
    assert hasattr(DatadiagramMLBasicDef::Master, "hidden")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Master.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::master_has_alignName():
    assert hasattr(DatadiagramMLBasicDef::Master, "alignName")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Master.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::master_has_prompt():
    assert hasattr(DatadiagramMLBasicDef::Master, "prompt")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Master.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::master_has_patternFlags():
    assert hasattr(DatadiagramMLBasicDef::Master, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Master.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::master_has_iconSize():
    assert hasattr(DatadiagramMLBasicDef::Master, "iconSize")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Master.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::master_has_matchByName():
    assert hasattr(DatadiagramMLBasicDef::Master, "matchByName")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Master.__mro__:
        if "matchByName" in klass.__dict__:
            descriptor = klass.__dict__["matchByName"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef::page_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::Page)


def test_datadiagrammlbasicdef::page_constructor_exists():
    assert callable(DatadiagramMLBasicDef::Page.__init__)


def test_datadiagrammlbasicdef::page_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::Page.__init__)
    params = list(sig.parameters.keys())
    assert "associatedPage" in params, "Missing parameter 'associatedPage'"
    assert "viewScale" in params, "Missing parameter 'viewScale'"
    assert "reviewerID" in params, "Missing parameter 'reviewerID'"
    assert "backPage" in params, "Missing parameter 'backPage'"
    assert "viewCenterX" in params, "Missing parameter 'viewCenterX'"
    assert "background" in params, "Missing parameter 'background'"
    assert "ViewCenterY" in params, "Missing parameter 'ViewCenterY'"

def test_datadiagrammlbasicdef::page_has_associatedPage():
    assert hasattr(DatadiagramMLBasicDef::Page, "associatedPage")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Page.__mro__:
        if "associatedPage" in klass.__dict__:
            descriptor = klass.__dict__["associatedPage"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::page_has_viewScale():
    assert hasattr(DatadiagramMLBasicDef::Page, "viewScale")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Page.__mro__:
        if "viewScale" in klass.__dict__:
            descriptor = klass.__dict__["viewScale"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::page_has_reviewerID():
    assert hasattr(DatadiagramMLBasicDef::Page, "reviewerID")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Page.__mro__:
        if "reviewerID" in klass.__dict__:
            descriptor = klass.__dict__["reviewerID"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::page_has_backPage():
    assert hasattr(DatadiagramMLBasicDef::Page, "backPage")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Page.__mro__:
        if "backPage" in klass.__dict__:
            descriptor = klass.__dict__["backPage"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::page_has_viewCenterX():
    assert hasattr(DatadiagramMLBasicDef::Page, "viewCenterX")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Page.__mro__:
        if "viewCenterX" in klass.__dict__:
            descriptor = klass.__dict__["viewCenterX"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::page_has_background():
    assert hasattr(DatadiagramMLBasicDef::Page, "background")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Page.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::page_has_ViewCenterY():
    assert hasattr(DatadiagramMLBasicDef::Page, "ViewCenterY")
    descriptor = None
    for klass in DatadiagramMLBasicDef::Page.__mro__:
        if "ViewCenterY" in klass.__dict__:
            descriptor = klass.__dict__["ViewCenterY"]
            break
    assert isinstance(descriptor, property)



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::pagesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::PageSheet)


def test_datadiagrammlbasicdef::pagesheet_constructor_exists():
    assert callable(DatadiagramMLBasicDef::PageSheet.__init__)


def test_datadiagrammlbasicdef::pagesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::PageSheet.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::stylesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::StyleSheet)


def test_datadiagrammlbasicdef::stylesheet_constructor_exists():
    assert callable(DatadiagramMLBasicDef::StyleSheet.__init__)


def test_datadiagrammlbasicdef::stylesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_stylesheet_is_not_abstract():
    assert not inspect.isabstract(StyleSheet)


def test_stylesheet_constructor_exists():
    assert callable(StyleSheet.__init__)


def test_stylesheet_constructor_args():
    sig = inspect.signature(StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::stylesheetscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::StyleSheetsCollection)


def test_datadiagrammlbasicdef::stylesheetscollection_constructor_exists():
    assert callable(DatadiagramMLBasicDef::StyleSheetsCollection.__init__)


def test_datadiagrammlbasicdef::stylesheetscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::StyleSheetsCollection.__init__)
    params = list(sig.parameters.keys())



def test_visiodocument_is_not_abstract():
    assert not inspect.isabstract(VisioDocument)


def test_visiodocument_constructor_exists():
    assert callable(VisioDocument.__init__)


def test_visiodocument_constructor_args():
    sig = inspect.signature(VisioDocument.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::DocumentPropertiesCollection)


def test_datadiagrammlbasicdef::documentpropertiescollection_constructor_exists():
    assert callable(DatadiagramMLBasicDef::DocumentPropertiesCollection.__init__)


def test_datadiagrammlbasicdef::documentpropertiescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "creator" in params, "Missing parameter 'creator'"
    assert "template" in params, "Missing parameter 'template'"
    assert "company" in params, "Missing parameter 'company'"
    assert "title" in params, "Missing parameter 'title'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "description" in params, "Missing parameter 'description'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "alternateNames" in params, "Missing parameter 'alternateNames'"
    assert "buildNumberCreated" in params, "Missing parameter 'buildNumberCreated'"
    assert "buildNumberEdited" in params, "Missing parameter 'buildNumberEdited'"
    assert "hyperlinkBase_href" in params, "Missing parameter 'hyperlinkBase_href'"

def test_datadiagrammlbasicdef::documentpropertiescollection_has_category():
    assert hasattr(DatadiagramMLBasicDef::DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::documentpropertiescollection_has_creator():
    assert hasattr(DatadiagramMLBasicDef::DocumentPropertiesCollection, "creator")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "creator" in klass.__dict__:
            descriptor = klass.__dict__["creator"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::documentpropertiescollection_has_template():
    assert hasattr(DatadiagramMLBasicDef::DocumentPropertiesCollection, "template")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::documentpropertiescollection_has_company():
    assert hasattr(DatadiagramMLBasicDef::DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::documentpropertiescollection_has_title():
    assert hasattr(DatadiagramMLBasicDef::DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::documentpropertiescollection_has_manager():
    assert hasattr(DatadiagramMLBasicDef::DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::documentpropertiescollection_has_description():
    assert hasattr(DatadiagramMLBasicDef::DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::documentpropertiescollection_has_keywords():
    assert hasattr(DatadiagramMLBasicDef::DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::documentpropertiescollection_has_subject():
    assert hasattr(DatadiagramMLBasicDef::DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::documentpropertiescollection_has_alternateNames():
    assert hasattr(DatadiagramMLBasicDef::DocumentPropertiesCollection, "alternateNames")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "alternateNames" in klass.__dict__:
            descriptor = klass.__dict__["alternateNames"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::documentpropertiescollection_has_buildNumberCreated():
    assert hasattr(DatadiagramMLBasicDef::DocumentPropertiesCollection, "buildNumberCreated")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "buildNumberCreated" in klass.__dict__:
            descriptor = klass.__dict__["buildNumberCreated"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::documentpropertiescollection_has_buildNumberEdited():
    assert hasattr(DatadiagramMLBasicDef::DocumentPropertiesCollection, "buildNumberEdited")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "buildNumberEdited" in klass.__dict__:
            descriptor = klass.__dict__["buildNumberEdited"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::documentpropertiescollection_has_hyperlinkBase_href():
    assert hasattr(DatadiagramMLBasicDef::DocumentPropertiesCollection, "hyperlinkBase_href")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase_href" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase_href"]
            break
    assert isinstance(descriptor, property)



def test_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DateTimeType)


def test_datetimetype_constructor_exists():
    assert callable(DateTimeType.__init__)


def test_datetimetype_constructor_args():
    sig = inspect.signature(DateTimeType.__init__)
    params = list(sig.parameters.keys())



def test_custompropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomPropertiesCollection)


def test_custompropertiescollection_constructor_exists():
    assert callable(CustomPropertiesCollection.__init__)


def test_custompropertiescollection_constructor_args():
    sig = inspect.signature(CustomPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_masterscollection_is_not_abstract():
    assert not inspect.isabstract(MastersCollection)


def test_masterscollection_constructor_exists():
    assert callable(MastersCollection.__init__)


def test_masterscollection_constructor_args():
    sig = inspect.signature(MastersCollection.__init__)
    params = list(sig.parameters.keys())



def test_documentsheet_is_not_abstract():
    assert not inspect.isabstract(DocumentSheet)


def test_documentsheet_constructor_exists():
    assert callable(DocumentSheet.__init__)


def test_documentsheet_constructor_args():
    sig = inspect.signature(DocumentSheet.__init__)
    params = list(sig.parameters.keys())



def test_stylesheetscollection_is_not_abstract():
    assert not inspect.isabstract(StyleSheetsCollection)


def test_stylesheetscollection_constructor_exists():
    assert callable(StyleSheetsCollection.__init__)


def test_stylesheetscollection_constructor_args():
    sig = inspect.signature(StyleSheetsCollection.__init__)
    params = list(sig.parameters.keys())



def test_facenamestable_is_not_abstract():
    assert not inspect.isabstract(FaceNamesTable)


def test_facenamestable_constructor_exists():
    assert callable(FaceNamesTable.__init__)


def test_facenamestable_constructor_args():
    sig = inspect.signature(FaceNamesTable.__init__)
    params = list(sig.parameters.keys())



def test_fontstable_is_not_abstract():
    assert not inspect.isabstract(FontsTable)


def test_fontstable_constructor_exists():
    assert callable(FontsTable.__init__)


def test_fontstable_constructor_args():
    sig = inspect.signature(FontsTable.__init__)
    params = list(sig.parameters.keys())



def test_printsetup_is_not_abstract():
    assert not inspect.isabstract(PrintSetup)


def test_printsetup_constructor_exists():
    assert callable(PrintSetup.__init__)


def test_printsetup_constructor_args():
    sig = inspect.signature(PrintSetup.__init__)
    params = list(sig.parameters.keys())



def test_colorstable_is_not_abstract():
    assert not inspect.isabstract(ColorsTable)


def test_colorstable_constructor_exists():
    assert callable(ColorsTable.__init__)


def test_colorstable_constructor_args():
    sig = inspect.signature(ColorsTable.__init__)
    params = list(sig.parameters.keys())



def test_documentsettingselt_is_not_abstract():
    assert not inspect.isabstract(DocumentSettingsElt)


def test_documentsettingselt_constructor_exists():
    assert callable(DocumentSettingsElt.__init__)


def test_documentsettingselt_constructor_args():
    sig = inspect.signature(DocumentSettingsElt.__init__)
    params = list(sig.parameters.keys())



def test_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DocumentPropertiesCollection)


def test_documentpropertiescollection_constructor_exists():
    assert callable(DocumentPropertiesCollection.__init__)


def test_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_solutionxml_is_not_abstract():
    assert not inspect.isabstract(SolutionXML)


def test_solutionxml_constructor_exists():
    assert callable(SolutionXML.__init__)


def test_solutionxml_constructor_args():
    sig = inspect.signature(SolutionXML.__init__)
    params = list(sig.parameters.keys())



def test_emailroutingdata_is_not_abstract():
    assert not inspect.isabstract(EmailRoutingData)


def test_emailroutingdata_constructor_exists():
    assert callable(EmailRoutingData.__init__)


def test_emailroutingdata_constructor_args():
    sig = inspect.signature(EmailRoutingData.__init__)
    params = list(sig.parameters.keys())



def test_vbprojectdata_is_not_abstract():
    assert not inspect.isabstract(VBProjectData)


def test_vbprojectdata_constructor_exists():
    assert callable(VBProjectData.__init__)


def test_vbprojectdata_constructor_args():
    sig = inspect.signature(VBProjectData.__init__)
    params = list(sig.parameters.keys())



def test_headerfooter_is_not_abstract():
    assert not inspect.isabstract(HeaderFooter)


def test_headerfooter_constructor_exists():
    assert callable(HeaderFooter.__init__)


def test_headerfooter_constructor_args():
    sig = inspect.signature(HeaderFooter.__init__)
    params = list(sig.parameters.keys())



def test_eventlist_is_not_abstract():
    assert not inspect.isabstract(EventList)


def test_eventlist_constructor_exists():
    assert callable(EventList.__init__)


def test_eventlist_constructor_args():
    sig = inspect.signature(EventList.__init__)
    params = list(sig.parameters.keys())



def test_windowsinfo_is_not_abstract():
    assert not inspect.isabstract(WindowsInfo)


def test_windowsinfo_constructor_exists():
    assert callable(WindowsInfo.__init__)


def test_windowsinfo_constructor_args():
    sig = inspect.signature(WindowsInfo.__init__)
    params = list(sig.parameters.keys())



def test_pagescollection_is_not_abstract():
    assert not inspect.isabstract(PagesCollection)


def test_pagescollection_constructor_exists():
    assert callable(PagesCollection.__init__)


def test_pagescollection_constructor_args():
    sig = inspect.signature(PagesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef::datetimetype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::DateTimeType)


def test_datadiagrammlbasicdef::datetimetype_constructor_exists():
    assert callable(DatadiagramMLBasicDef::DateTimeType.__init__)


def test_datadiagrammlbasicdef::datetimetype_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "month" in params, "Missing parameter 'month'"
    assert "second" in params, "Missing parameter 'second'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "day" in params, "Missing parameter 'day'"
    assert "minute" in params, "Missing parameter 'minute'"

def test_datadiagrammlbasicdef::datetimetype_has_year():
    assert hasattr(DatadiagramMLBasicDef::DateTimeType, "year")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::datetimetype_has_month():
    assert hasattr(DatadiagramMLBasicDef::DateTimeType, "month")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::datetimetype_has_second():
    assert hasattr(DatadiagramMLBasicDef::DateTimeType, "second")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::datetimetype_has_hour():
    assert hasattr(DatadiagramMLBasicDef::DateTimeType, "hour")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::datetimetype_has_day():
    assert hasattr(DatadiagramMLBasicDef::DateTimeType, "day")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::datetimetype_has_minute():
    assert hasattr(DatadiagramMLBasicDef::DateTimeType, "minute")
    descriptor = None
    for klass in DatadiagramMLBasicDef::DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef::visiodocument_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::VisioDocument)


def test_datadiagrammlbasicdef::visiodocument_constructor_exists():
    assert callable(DatadiagramMLBasicDef::VisioDocument.__init__)


def test_datadiagrammlbasicdef::visiodocument_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::VisioDocument.__init__)
    params = list(sig.parameters.keys())
    assert "metric" in params, "Missing parameter 'metric'"
    assert "buildnum" in params, "Missing parameter 'buildnum'"
    assert "docLangId" in params, "Missing parameter 'docLangId'"
    assert "key" in params, "Missing parameter 'key'"
    assert "start" in params, "Missing parameter 'start'"
    assert "version" in params, "Missing parameter 'version'"

def test_datadiagrammlbasicdef::visiodocument_has_metric():
    assert hasattr(DatadiagramMLBasicDef::VisioDocument, "metric")
    descriptor = None
    for klass in DatadiagramMLBasicDef::VisioDocument.__mro__:
        if "metric" in klass.__dict__:
            descriptor = klass.__dict__["metric"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::visiodocument_has_buildnum():
    assert hasattr(DatadiagramMLBasicDef::VisioDocument, "buildnum")
    descriptor = None
    for klass in DatadiagramMLBasicDef::VisioDocument.__mro__:
        if "buildnum" in klass.__dict__:
            descriptor = klass.__dict__["buildnum"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::visiodocument_has_docLangId():
    assert hasattr(DatadiagramMLBasicDef::VisioDocument, "docLangId")
    descriptor = None
    for klass in DatadiagramMLBasicDef::VisioDocument.__mro__:
        if "docLangId" in klass.__dict__:
            descriptor = klass.__dict__["docLangId"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::visiodocument_has_key():
    assert hasattr(DatadiagramMLBasicDef::VisioDocument, "key")
    descriptor = None
    for klass in DatadiagramMLBasicDef::VisioDocument.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::visiodocument_has_start():
    assert hasattr(DatadiagramMLBasicDef::VisioDocument, "start")
    descriptor = None
    for klass in DatadiagramMLBasicDef::VisioDocument.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::visiodocument_has_version():
    assert hasattr(DatadiagramMLBasicDef::VisioDocument, "version")
    descriptor = None
    for klass in DatadiagramMLBasicDef::VisioDocument.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef::celltype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef::CellType)


def test_datadiagrammlbasicdef::celltype_constructor_exists():
    assert callable(DatadiagramMLBasicDef::CellType.__init__)


def test_datadiagrammlbasicdef::celltype_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef::CellType.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "formula" in params, "Missing parameter 'formula'"
    assert "err" in params, "Missing parameter 'err'"
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammlbasicdef::celltype_has_unit():
    assert hasattr(DatadiagramMLBasicDef::CellType, "unit")
    descriptor = None
    for klass in DatadiagramMLBasicDef::CellType.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::celltype_has_formula():
    assert hasattr(DatadiagramMLBasicDef::CellType, "formula")
    descriptor = None
    for klass in DatadiagramMLBasicDef::CellType.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::celltype_has_err():
    assert hasattr(DatadiagramMLBasicDef::CellType, "err")
    descriptor = None
    for klass in DatadiagramMLBasicDef::CellType.__mro__:
        if "err" in klass.__dict__:
            descriptor = klass.__dict__["err"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef::celltype_has_value():
    assert hasattr(DatadiagramMLBasicDef::CellType, "value")
    descriptor = None
    for klass in DatadiagramMLBasicDef::CellType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)


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
DatadiagramMLBasicDef::HeaderFooter_strategy = st.builds(
    DatadiagramMLBasicDef::HeaderFooter,
)
DatadiagramMLBasicDef::EventList_strategy = st.builds(
    DatadiagramMLBasicDef::EventList,
)
DatadiagramMLBasicDef::WindowsInfo_strategy = st.builds(
    DatadiagramMLBasicDef::WindowsInfo,
)
DatadiagramMLBasicDef::FaceNamesTable_strategy = st.builds(
    DatadiagramMLBasicDef::FaceNamesTable,
)
DatadiagramMLBasicDef::FontsTable_strategy = st.builds(
    DatadiagramMLBasicDef::FontsTable,
)
DatadiagramMLBasicDef::PrintSetup_strategy = st.builds(
    DatadiagramMLBasicDef::PrintSetup,
)
DatadiagramMLBasicDef::SolutionXML_strategy = st.builds(
    DatadiagramMLBasicDef::SolutionXML,
)
Page_strategy = st.builds(
    Page,
)
DatadiagramMLBasicDef::ColorsTable_strategy = st.builds(
    DatadiagramMLBasicDef::ColorsTable,
)
DatadiagramMLBasicDef::DocumentSettingsElt_strategy = st.builds(
    DatadiagramMLBasicDef::DocumentSettingsElt,
)
DatadiagramMLBasicDef::PageElt_strategy = st.builds(
    DatadiagramMLBasicDef::PageElt,
)
ConnectsCollection_strategy = st.builds(
    ConnectsCollection,
)
DatadiagramMLBasicDef::Connect_strategy = st.builds(
    DatadiagramMLBasicDef::Connect,
    fromCell=
        safe_text,
    fromSheet=
        safe_text,
    toSheet=
        safe_text,
    fromPart=
        safe_text,
    toPart=
        safe_text,
    toCell=
        safe_text
)
Connect_strategy = st.builds(
    Connect,
)
DatadiagramMLBasicDef::PagesCollection_strategy = st.builds(
    DatadiagramMLBasicDef::PagesCollection,
)
DatadiagramMLBasicDef::MasterElt_strategy = st.builds(
    DatadiagramMLBasicDef::MasterElt,
)
Icon_strategy = st.builds(
    Icon,
)
DatadiagramMLBasicDef::MastersCollection_strategy = st.builds(
    DatadiagramMLBasicDef::MastersCollection,
)
Text_strategy = st.builds(
    Text,
)
DatadiagramMLBasicDef::TextElt_strategy = st.builds(
    DatadiagramMLBasicDef::TextElt,
)
MasterShortCut_strategy = st.builds(
    MasterShortCut,
)
Master_strategy = st.builds(
    Master,
)
XYABCDElt_strategy = st.builds(
    XYABCDElt,
)
DatadiagramMLBasicDef::SplineStart_strategy = st.builds(
    DatadiagramMLBasicDef::SplineStart,
)
DatadiagramMLBasicDef::EllipticalArcTo_strategy = st.builds(
    DatadiagramMLBasicDef::EllipticalArcTo,
)
DatadiagramMLBasicDef::Ellipse_strategy = st.builds(
    DatadiagramMLBasicDef::Ellipse,
)
TextElt_strategy = st.builds(
    TextElt,
)
DatadiagramMLBasicDef::StringElt_strategy = st.builds(
    DatadiagramMLBasicDef::StringElt,
    value=
        safe_text
)
XYABCDEElt_strategy = st.builds(
    XYABCDEElt,
)
DatadiagramMLBasicDef::NURBSTo_strategy = st.builds(
    DatadiagramMLBasicDef::NURBSTo,
)
DatadiagramMLBasicDef::XYABCDEElt_strategy = st.builds(
    DatadiagramMLBasicDef::XYABCDEElt,
)
XYAElt_strategy = st.builds(
    XYAElt,
)
DatadiagramMLBasicDef::SplineKnot_strategy = st.builds(
    DatadiagramMLBasicDef::SplineKnot,
)
DatadiagramMLBasicDef::PolylineTo_strategy = st.builds(
    DatadiagramMLBasicDef::PolylineTo,
)
DatadiagramMLBasicDef::ArcTo_strategy = st.builds(
    DatadiagramMLBasicDef::ArcTo,
)
XYABElt_strategy = st.builds(
    XYABElt,
)
DatadiagramMLBasicDef::XYABCDElt_strategy = st.builds(
    DatadiagramMLBasicDef::XYABCDElt,
)
DatadiagramMLBasicDef::InfiniteLine_strategy = st.builds(
    DatadiagramMLBasicDef::InfiniteLine,
)
DatadiagramMLBasicDef::XYABElt_strategy = st.builds(
    DatadiagramMLBasicDef::XYABElt,
)
NURBSTo_strategy = st.builds(
    NURBSTo,
)
SplineStart_strategy = st.builds(
    SplineStart,
)
EllipticalArcTo_strategy = st.builds(
    EllipticalArcTo,
)
Ellipse_strategy = st.builds(
    Ellipse,
)
Geom_strategy = st.builds(
    Geom,
)
XYElt_strategy = st.builds(
    XYElt,
)
DatadiagramMLBasicDef::XYAElt_strategy = st.builds(
    DatadiagramMLBasicDef::XYAElt,
)
DatadiagramMLBasicDef::MoveTo_strategy = st.builds(
    DatadiagramMLBasicDef::MoveTo,
)
DatadiagramMLBasicDef::LineTo_strategy = st.builds(
    DatadiagramMLBasicDef::LineTo,
)
LineTo_strategy = st.builds(
    LineTo,
)
CellType_strategy = st.builds(
    CellType,
)
DelElt_strategy = st.builds(
    DelElt,
)
IXElt_strategy = st.builds(
    IXElt,
)
DatadiagramMLBasicDef::XYElt_strategy = st.builds(
    DatadiagramMLBasicDef::XYElt,
)
DatadiagramMLBasicDef::DelElt_strategy = st.builds(
    DatadiagramMLBasicDef::DelElt,
    del_=
        safe_text
)
DatadiagramMLBasicDef::IXElt_strategy = st.builds(
    DatadiagramMLBasicDef::IXElt,
    iX=
        safe_text
)
InfiniteLine_strategy = st.builds(
    InfiniteLine,
)
PolylineTo_strategy = st.builds(
    PolylineTo,
)
SplineKnot_strategy = st.builds(
    SplineKnot,
)
ArcTo_strategy = st.builds(
    ArcTo,
)
MoveTo_strategy = st.builds(
    MoveTo,
)
DatadiagramMLBasicDef::UniqueIdElt_strategy = st.builds(
    DatadiagramMLBasicDef::UniqueIdElt,
    UniqueID=
        safe_text
)
DatadiagramMLBasicDef::IdentifiedElt_strategy = st.builds(
    DatadiagramMLBasicDef::IdentifiedElt,
    ID=
        safe_text
)
DatadiagramMLBasicDef::NamedElt_strategy = st.builds(
    DatadiagramMLBasicDef::NamedElt,
    nameU=
        safe_text,
    name=
        safe_text
)
PageElt_strategy = st.builds(
    PageElt,
)
MasterElt_strategy = st.builds(
    MasterElt,
)
DatadiagramMLBasicDef::ConnectsCollection_strategy = st.builds(
    DatadiagramMLBasicDef::ConnectsCollection,
)
DatadiagramMLBasicDef::Icon_strategy = st.builds(
    DatadiagramMLBasicDef::Icon,
    value=
        safe_text
)
DatadiagramMLBasicDef::ShapesCollection_strategy = st.builds(
    DatadiagramMLBasicDef::ShapesCollection,
)
UniqueIdElt_strategy = st.builds(
    UniqueIdElt,
)
PageSheet_strategy = st.builds(
    PageSheet,
)
NamedElt_strategy = st.builds(
    NamedElt,
)
DatadiagramMLBasicDef::DocumentSheet_strategy = st.builds(
    DatadiagramMLBasicDef::DocumentSheet,
)
DatadiagramMLBasicDef::ShapeElt_strategy = st.builds(
    DatadiagramMLBasicDef::ShapeElt,
)
ShapeElt_strategy = st.builds(
    ShapeElt,
)
DatadiagramMLBasicDef::Text_strategy = st.builds(
    DatadiagramMLBasicDef::Text,
)
DatadiagramMLBasicDef::Geom_strategy = st.builds(
    DatadiagramMLBasicDef::Geom,
)
ShapesCollection_strategy = st.builds(
    ShapesCollection,
)
DatadiagramMLBasicDef::Shape_strategy = st.builds(
    DatadiagramMLBasicDef::Shape,
    lineStyle=
        safe_text,
    textStyle=
        safe_text,
    fillStyle=
        safe_text
)
DatadiagramMLBasicDef::EmailRoutingData_strategy = st.builds(
    DatadiagramMLBasicDef::EmailRoutingData,
    size=
        safe_text,
    data=
        safe_text
)
DatadiagramMLBasicDef::VBProjectData_strategy = st.builds(
    DatadiagramMLBasicDef::VBProjectData,
    data=
        safe_text
)
DatadiagramMLBasicDef::CustomProperty_strategy = st.builds(
    DatadiagramMLBasicDef::CustomProperty,
    name=
        safe_text,
    dataType=
        safe_text
)
CustomProperty_strategy = st.builds(
    CustomProperty,
)
DatadiagramMLBasicDef::CustomPropertiesCollection_strategy = st.builds(
    DatadiagramMLBasicDef::CustomPropertiesCollection,
)
IdentifiedElt_strategy = st.builds(
    IdentifiedElt,
)
DatadiagramMLBasicDef::MasterShortCut_strategy = st.builds(
    DatadiagramMLBasicDef::MasterShortCut,
    prompt=
        safe_text,
    alignName=
        safe_text,
    patternFlags=
        safe_text,
    shortcutURL=
        safe_text,
    iconSize=
        safe_text,
    shortcutHelp=
        safe_text
)
DatadiagramMLBasicDef::Master_strategy = st.builds(
    DatadiagramMLBasicDef::Master,
    iconUpdate=
        safe_text,
    baseID=
        safe_text,
    hidden=
        safe_text,
    alignName=
        safe_text,
    prompt=
        safe_text,
    patternFlags=
        safe_text,
    iconSize=
        safe_text,
    matchByName=
        safe_text
)
DatadiagramMLBasicDef::Page_strategy = st.builds(
    DatadiagramMLBasicDef::Page,
    associatedPage=
        safe_text,
    viewScale=
        safe_text,
    reviewerID=
        safe_text,
    backPage=
        safe_text,
    viewCenterX=
        safe_text,
    background=
        safe_text,
    ViewCenterY=
        safe_text
)
Shape_strategy = st.builds(
    Shape,
)
DatadiagramMLBasicDef::PageSheet_strategy = st.builds(
    DatadiagramMLBasicDef::PageSheet,
)
DatadiagramMLBasicDef::StyleSheet_strategy = st.builds(
    DatadiagramMLBasicDef::StyleSheet,
)
StyleSheet_strategy = st.builds(
    StyleSheet,
)
DatadiagramMLBasicDef::StyleSheetsCollection_strategy = st.builds(
    DatadiagramMLBasicDef::StyleSheetsCollection,
)
VisioDocument_strategy = st.builds(
    VisioDocument,
)
DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy = st.builds(
    DatadiagramMLBasicDef::DocumentPropertiesCollection,
    category=
        safe_text,
    creator=
        safe_text,
    template=
        safe_text,
    company=
        safe_text,
    title=
        safe_text,
    manager=
        safe_text,
    description=
        safe_text,
    keywords=
        safe_text,
    subject=
        safe_text,
    alternateNames=
        safe_text,
    buildNumberCreated=
        safe_text,
    buildNumberEdited=
        safe_text,
    hyperlinkBase_href=
        safe_text
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
CustomPropertiesCollection_strategy = st.builds(
    CustomPropertiesCollection,
)
MastersCollection_strategy = st.builds(
    MastersCollection,
)
DocumentSheet_strategy = st.builds(
    DocumentSheet,
)
StyleSheetsCollection_strategy = st.builds(
    StyleSheetsCollection,
)
FaceNamesTable_strategy = st.builds(
    FaceNamesTable,
)
FontsTable_strategy = st.builds(
    FontsTable,
)
PrintSetup_strategy = st.builds(
    PrintSetup,
)
ColorsTable_strategy = st.builds(
    ColorsTable,
)
DocumentSettingsElt_strategy = st.builds(
    DocumentSettingsElt,
)
DocumentPropertiesCollection_strategy = st.builds(
    DocumentPropertiesCollection,
)
SolutionXML_strategy = st.builds(
    SolutionXML,
)
EmailRoutingData_strategy = st.builds(
    EmailRoutingData,
)
VBProjectData_strategy = st.builds(
    VBProjectData,
)
HeaderFooter_strategy = st.builds(
    HeaderFooter,
)
EventList_strategy = st.builds(
    EventList,
)
WindowsInfo_strategy = st.builds(
    WindowsInfo,
)
PagesCollection_strategy = st.builds(
    PagesCollection,
)
DatadiagramMLBasicDef::DateTimeType_strategy = st.builds(
    DatadiagramMLBasicDef::DateTimeType,
    year=
        safe_text,
    month=
        safe_text,
    second=
        safe_text,
    hour=
        safe_text,
    day=
        safe_text,
    minute=
        safe_text
)
DatadiagramMLBasicDef::VisioDocument_strategy = st.builds(
    DatadiagramMLBasicDef::VisioDocument,
    metric=
        safe_text,
    buildnum=
        safe_text,
    docLangId=
        safe_text,
    key=
        safe_text,
    start=
        safe_text,
    version=
        safe_text
)
DatadiagramMLBasicDef::CellType_strategy = st.builds(
    DatadiagramMLBasicDef::CellType,
    unit=
        safe_text,
    formula=
        safe_text,
    err=
        safe_text,
    value=
        safe_text
)

@given(instance=DatadiagramMLBasicDef::HeaderFooter_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::headerfooter_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::HeaderFooter)

@given(instance=DatadiagramMLBasicDef::EventList_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::eventlist_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::EventList)

@given(instance=DatadiagramMLBasicDef::WindowsInfo_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::windowsinfo_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::WindowsInfo)

@given(instance=DatadiagramMLBasicDef::FaceNamesTable_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::facenamestable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::FaceNamesTable)

@given(instance=DatadiagramMLBasicDef::FontsTable_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::fontstable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::FontsTable)

@given(instance=DatadiagramMLBasicDef::PrintSetup_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::printsetup_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::PrintSetup)

@given(instance=DatadiagramMLBasicDef::SolutionXML_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::solutionxml_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::SolutionXML)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=DatadiagramMLBasicDef::ColorsTable_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::colorstable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::ColorsTable)

@given(instance=DatadiagramMLBasicDef::DocumentSettingsElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::documentsettingselt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::DocumentSettingsElt)

@given(instance=DatadiagramMLBasicDef::PageElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::pageelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::PageElt)

@given(instance=ConnectsCollection_strategy)
@settings(max_examples=50)
def test_connectscollection_instantiation(instance):
    assert isinstance(instance, ConnectsCollection)

@given(instance=DatadiagramMLBasicDef::Connect_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::connect_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::Connect)

@given(instance=DatadiagramMLBasicDef::Connect_strategy)
def test_datadiagrammlbasicdef::connect_fromCell_type(instance):
    assert isinstance(instance.fromCell, str)


@given(instance=DatadiagramMLBasicDef::Connect_strategy)
def test_datadiagrammlbasicdef::connect_fromCell_setter(instance):
    original = instance.fromCell
    instance.fromCell = original
    assert instance.fromCell == original

@given(instance=DatadiagramMLBasicDef::Connect_strategy)
def test_datadiagrammlbasicdef::connect_fromSheet_type(instance):
    assert isinstance(instance.fromSheet, str)


@given(instance=DatadiagramMLBasicDef::Connect_strategy)
def test_datadiagrammlbasicdef::connect_fromSheet_setter(instance):
    original = instance.fromSheet
    instance.fromSheet = original
    assert instance.fromSheet == original

@given(instance=DatadiagramMLBasicDef::Connect_strategy)
def test_datadiagrammlbasicdef::connect_toSheet_type(instance):
    assert isinstance(instance.toSheet, str)


@given(instance=DatadiagramMLBasicDef::Connect_strategy)
def test_datadiagrammlbasicdef::connect_toSheet_setter(instance):
    original = instance.toSheet
    instance.toSheet = original
    assert instance.toSheet == original

@given(instance=DatadiagramMLBasicDef::Connect_strategy)
def test_datadiagrammlbasicdef::connect_fromPart_type(instance):
    assert isinstance(instance.fromPart, str)


@given(instance=DatadiagramMLBasicDef::Connect_strategy)
def test_datadiagrammlbasicdef::connect_fromPart_setter(instance):
    original = instance.fromPart
    instance.fromPart = original
    assert instance.fromPart == original

@given(instance=DatadiagramMLBasicDef::Connect_strategy)
def test_datadiagrammlbasicdef::connect_toPart_type(instance):
    assert isinstance(instance.toPart, str)


@given(instance=DatadiagramMLBasicDef::Connect_strategy)
def test_datadiagrammlbasicdef::connect_toPart_setter(instance):
    original = instance.toPart
    instance.toPart = original
    assert instance.toPart == original

@given(instance=DatadiagramMLBasicDef::Connect_strategy)
def test_datadiagrammlbasicdef::connect_toCell_type(instance):
    assert isinstance(instance.toCell, str)


@given(instance=DatadiagramMLBasicDef::Connect_strategy)
def test_datadiagrammlbasicdef::connect_toCell_setter(instance):
    original = instance.toCell
    instance.toCell = original
    assert instance.toCell == original

@given(instance=Connect_strategy)
@settings(max_examples=50)
def test_connect_instantiation(instance):
    assert isinstance(instance, Connect)

@given(instance=DatadiagramMLBasicDef::PagesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::pagescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::PagesCollection)

@given(instance=DatadiagramMLBasicDef::MasterElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::masterelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::MasterElt)

@given(instance=Icon_strategy)
@settings(max_examples=50)
def test_icon_instantiation(instance):
    assert isinstance(instance, Icon)

@given(instance=DatadiagramMLBasicDef::MastersCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::masterscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::MastersCollection)

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=DatadiagramMLBasicDef::TextElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::textelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::TextElt)

@given(instance=MasterShortCut_strategy)
@settings(max_examples=50)
def test_mastershortcut_instantiation(instance):
    assert isinstance(instance, MasterShortCut)

@given(instance=Master_strategy)
@settings(max_examples=50)
def test_master_instantiation(instance):
    assert isinstance(instance, Master)

@given(instance=XYABCDElt_strategy)
@settings(max_examples=50)
def test_xyabcdelt_instantiation(instance):
    assert isinstance(instance, XYABCDElt)

@given(instance=DatadiagramMLBasicDef::SplineStart_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::splinestart_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::SplineStart)

@given(instance=DatadiagramMLBasicDef::EllipticalArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::ellipticalarcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::EllipticalArcTo)

@given(instance=DatadiagramMLBasicDef::Ellipse_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::ellipse_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::Ellipse)

@given(instance=TextElt_strategy)
@settings(max_examples=50)
def test_textelt_instantiation(instance):
    assert isinstance(instance, TextElt)

@given(instance=DatadiagramMLBasicDef::StringElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::stringelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::StringElt)

@given(instance=DatadiagramMLBasicDef::StringElt_strategy)
def test_datadiagrammlbasicdef::stringelt_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DatadiagramMLBasicDef::StringElt_strategy)
def test_datadiagrammlbasicdef::stringelt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=XYABCDEElt_strategy)
@settings(max_examples=50)
def test_xyabcdeelt_instantiation(instance):
    assert isinstance(instance, XYABCDEElt)

@given(instance=DatadiagramMLBasicDef::NURBSTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::nurbsto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::NURBSTo)

@given(instance=DatadiagramMLBasicDef::XYABCDEElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::xyabcdeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::XYABCDEElt)

@given(instance=XYAElt_strategy)
@settings(max_examples=50)
def test_xyaelt_instantiation(instance):
    assert isinstance(instance, XYAElt)

@given(instance=DatadiagramMLBasicDef::SplineKnot_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::splineknot_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::SplineKnot)

@given(instance=DatadiagramMLBasicDef::PolylineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::polylineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::PolylineTo)

@given(instance=DatadiagramMLBasicDef::ArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::arcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::ArcTo)

@given(instance=XYABElt_strategy)
@settings(max_examples=50)
def test_xyabelt_instantiation(instance):
    assert isinstance(instance, XYABElt)

@given(instance=DatadiagramMLBasicDef::XYABCDElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::xyabcdelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::XYABCDElt)

@given(instance=DatadiagramMLBasicDef::InfiniteLine_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::infiniteline_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::InfiniteLine)

@given(instance=DatadiagramMLBasicDef::XYABElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::xyabelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::XYABElt)

@given(instance=NURBSTo_strategy)
@settings(max_examples=50)
def test_nurbsto_instantiation(instance):
    assert isinstance(instance, NURBSTo)

@given(instance=SplineStart_strategy)
@settings(max_examples=50)
def test_splinestart_instantiation(instance):
    assert isinstance(instance, SplineStart)

@given(instance=EllipticalArcTo_strategy)
@settings(max_examples=50)
def test_ellipticalarcto_instantiation(instance):
    assert isinstance(instance, EllipticalArcTo)

@given(instance=Ellipse_strategy)
@settings(max_examples=50)
def test_ellipse_instantiation(instance):
    assert isinstance(instance, Ellipse)

@given(instance=Geom_strategy)
@settings(max_examples=50)
def test_geom_instantiation(instance):
    assert isinstance(instance, Geom)

@given(instance=XYElt_strategy)
@settings(max_examples=50)
def test_xyelt_instantiation(instance):
    assert isinstance(instance, XYElt)

@given(instance=DatadiagramMLBasicDef::XYAElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::xyaelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::XYAElt)

@given(instance=DatadiagramMLBasicDef::MoveTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::moveto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::MoveTo)

@given(instance=DatadiagramMLBasicDef::LineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::lineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::LineTo)

@given(instance=LineTo_strategy)
@settings(max_examples=50)
def test_lineto_instantiation(instance):
    assert isinstance(instance, LineTo)

@given(instance=CellType_strategy)
@settings(max_examples=50)
def test_celltype_instantiation(instance):
    assert isinstance(instance, CellType)

@given(instance=DelElt_strategy)
@settings(max_examples=50)
def test_delelt_instantiation(instance):
    assert isinstance(instance, DelElt)

@given(instance=IXElt_strategy)
@settings(max_examples=50)
def test_ixelt_instantiation(instance):
    assert isinstance(instance, IXElt)

@given(instance=DatadiagramMLBasicDef::XYElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::xyelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::XYElt)

@given(instance=DatadiagramMLBasicDef::DelElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::delelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::DelElt)

@given(instance=DatadiagramMLBasicDef::DelElt_strategy)
def test_datadiagrammlbasicdef::delelt_del__type(instance):
    assert isinstance(instance.del_, str)


@given(instance=DatadiagramMLBasicDef::DelElt_strategy)
def test_datadiagrammlbasicdef::delelt_del__setter(instance):
    original = instance.del_
    instance.del_ = original
    assert instance.del_ == original

@given(instance=DatadiagramMLBasicDef::IXElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::ixelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::IXElt)

@given(instance=DatadiagramMLBasicDef::IXElt_strategy)
def test_datadiagrammlbasicdef::ixelt_iX_type(instance):
    assert isinstance(instance.iX, str)


@given(instance=DatadiagramMLBasicDef::IXElt_strategy)
def test_datadiagrammlbasicdef::ixelt_iX_setter(instance):
    original = instance.iX
    instance.iX = original
    assert instance.iX == original

@given(instance=InfiniteLine_strategy)
@settings(max_examples=50)
def test_infiniteline_instantiation(instance):
    assert isinstance(instance, InfiniteLine)

@given(instance=PolylineTo_strategy)
@settings(max_examples=50)
def test_polylineto_instantiation(instance):
    assert isinstance(instance, PolylineTo)

@given(instance=SplineKnot_strategy)
@settings(max_examples=50)
def test_splineknot_instantiation(instance):
    assert isinstance(instance, SplineKnot)

@given(instance=ArcTo_strategy)
@settings(max_examples=50)
def test_arcto_instantiation(instance):
    assert isinstance(instance, ArcTo)

@given(instance=MoveTo_strategy)
@settings(max_examples=50)
def test_moveto_instantiation(instance):
    assert isinstance(instance, MoveTo)

@given(instance=DatadiagramMLBasicDef::UniqueIdElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::uniqueidelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::UniqueIdElt)

@given(instance=DatadiagramMLBasicDef::UniqueIdElt_strategy)
def test_datadiagrammlbasicdef::uniqueidelt_UniqueID_type(instance):
    assert isinstance(instance.UniqueID, str)


@given(instance=DatadiagramMLBasicDef::UniqueIdElt_strategy)
def test_datadiagrammlbasicdef::uniqueidelt_UniqueID_setter(instance):
    original = instance.UniqueID
    instance.UniqueID = original
    assert instance.UniqueID == original

@given(instance=DatadiagramMLBasicDef::IdentifiedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::identifiedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::IdentifiedElt)

@given(instance=DatadiagramMLBasicDef::IdentifiedElt_strategy)
def test_datadiagrammlbasicdef::identifiedelt_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=DatadiagramMLBasicDef::IdentifiedElt_strategy)
def test_datadiagrammlbasicdef::identifiedelt_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=DatadiagramMLBasicDef::NamedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::namedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::NamedElt)

@given(instance=DatadiagramMLBasicDef::NamedElt_strategy)
def test_datadiagrammlbasicdef::namedelt_nameU_type(instance):
    assert isinstance(instance.nameU, str)


@given(instance=DatadiagramMLBasicDef::NamedElt_strategy)
def test_datadiagrammlbasicdef::namedelt_nameU_setter(instance):
    original = instance.nameU
    instance.nameU = original
    assert instance.nameU == original

@given(instance=DatadiagramMLBasicDef::NamedElt_strategy)
def test_datadiagrammlbasicdef::namedelt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DatadiagramMLBasicDef::NamedElt_strategy)
def test_datadiagrammlbasicdef::namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PageElt_strategy)
@settings(max_examples=50)
def test_pageelt_instantiation(instance):
    assert isinstance(instance, PageElt)

@given(instance=MasterElt_strategy)
@settings(max_examples=50)
def test_masterelt_instantiation(instance):
    assert isinstance(instance, MasterElt)

@given(instance=DatadiagramMLBasicDef::ConnectsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::connectscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::ConnectsCollection)

@given(instance=DatadiagramMLBasicDef::Icon_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::icon_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::Icon)

@given(instance=DatadiagramMLBasicDef::Icon_strategy)
def test_datadiagrammlbasicdef::icon_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DatadiagramMLBasicDef::Icon_strategy)
def test_datadiagrammlbasicdef::icon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DatadiagramMLBasicDef::ShapesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::shapescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::ShapesCollection)

@given(instance=UniqueIdElt_strategy)
@settings(max_examples=50)
def test_uniqueidelt_instantiation(instance):
    assert isinstance(instance, UniqueIdElt)

@given(instance=PageSheet_strategy)
@settings(max_examples=50)
def test_pagesheet_instantiation(instance):
    assert isinstance(instance, PageSheet)

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=DatadiagramMLBasicDef::DocumentSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::documentsheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::DocumentSheet)

@given(instance=DatadiagramMLBasicDef::ShapeElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::shapeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::ShapeElt)

@given(instance=ShapeElt_strategy)
@settings(max_examples=50)
def test_shapeelt_instantiation(instance):
    assert isinstance(instance, ShapeElt)

@given(instance=DatadiagramMLBasicDef::Text_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::text_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::Text)

@given(instance=DatadiagramMLBasicDef::Geom_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::geom_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::Geom)

@given(instance=ShapesCollection_strategy)
@settings(max_examples=50)
def test_shapescollection_instantiation(instance):
    assert isinstance(instance, ShapesCollection)

@given(instance=DatadiagramMLBasicDef::Shape_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::shape_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::Shape)

@given(instance=DatadiagramMLBasicDef::Shape_strategy)
def test_datadiagrammlbasicdef::shape_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=DatadiagramMLBasicDef::Shape_strategy)
def test_datadiagrammlbasicdef::shape_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=DatadiagramMLBasicDef::Shape_strategy)
def test_datadiagrammlbasicdef::shape_textStyle_type(instance):
    assert isinstance(instance.textStyle, str)


@given(instance=DatadiagramMLBasicDef::Shape_strategy)
def test_datadiagrammlbasicdef::shape_textStyle_setter(instance):
    original = instance.textStyle
    instance.textStyle = original
    assert instance.textStyle == original

@given(instance=DatadiagramMLBasicDef::Shape_strategy)
def test_datadiagrammlbasicdef::shape_fillStyle_type(instance):
    assert isinstance(instance.fillStyle, str)


@given(instance=DatadiagramMLBasicDef::Shape_strategy)
def test_datadiagrammlbasicdef::shape_fillStyle_setter(instance):
    original = instance.fillStyle
    instance.fillStyle = original
    assert instance.fillStyle == original

@given(instance=DatadiagramMLBasicDef::EmailRoutingData_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::emailroutingdata_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::EmailRoutingData)

@given(instance=DatadiagramMLBasicDef::EmailRoutingData_strategy)
def test_datadiagrammlbasicdef::emailroutingdata_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=DatadiagramMLBasicDef::EmailRoutingData_strategy)
def test_datadiagrammlbasicdef::emailroutingdata_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=DatadiagramMLBasicDef::EmailRoutingData_strategy)
def test_datadiagrammlbasicdef::emailroutingdata_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=DatadiagramMLBasicDef::EmailRoutingData_strategy)
def test_datadiagrammlbasicdef::emailroutingdata_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=DatadiagramMLBasicDef::VBProjectData_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::vbprojectdata_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::VBProjectData)

@given(instance=DatadiagramMLBasicDef::VBProjectData_strategy)
def test_datadiagrammlbasicdef::vbprojectdata_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=DatadiagramMLBasicDef::VBProjectData_strategy)
def test_datadiagrammlbasicdef::vbprojectdata_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=DatadiagramMLBasicDef::CustomProperty_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::customproperty_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::CustomProperty)

@given(instance=DatadiagramMLBasicDef::CustomProperty_strategy)
def test_datadiagrammlbasicdef::customproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DatadiagramMLBasicDef::CustomProperty_strategy)
def test_datadiagrammlbasicdef::customproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DatadiagramMLBasicDef::CustomProperty_strategy)
def test_datadiagrammlbasicdef::customproperty_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=DatadiagramMLBasicDef::CustomProperty_strategy)
def test_datadiagrammlbasicdef::customproperty_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=CustomProperty_strategy)
@settings(max_examples=50)
def test_customproperty_instantiation(instance):
    assert isinstance(instance, CustomProperty)

@given(instance=DatadiagramMLBasicDef::CustomPropertiesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::custompropertiescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::CustomPropertiesCollection)

@given(instance=IdentifiedElt_strategy)
@settings(max_examples=50)
def test_identifiedelt_instantiation(instance):
    assert isinstance(instance, IdentifiedElt)

@given(instance=DatadiagramMLBasicDef::MasterShortCut_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::mastershortcut_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::MasterShortCut)

@given(instance=DatadiagramMLBasicDef::MasterShortCut_strategy)
def test_datadiagrammlbasicdef::mastershortcut_prompt_type(instance):
    assert isinstance(instance.prompt, str)


@given(instance=DatadiagramMLBasicDef::MasterShortCut_strategy)
def test_datadiagrammlbasicdef::mastershortcut_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original

@given(instance=DatadiagramMLBasicDef::MasterShortCut_strategy)
def test_datadiagrammlbasicdef::mastershortcut_alignName_type(instance):
    assert isinstance(instance.alignName, str)


@given(instance=DatadiagramMLBasicDef::MasterShortCut_strategy)
def test_datadiagrammlbasicdef::mastershortcut_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original

@given(instance=DatadiagramMLBasicDef::MasterShortCut_strategy)
def test_datadiagrammlbasicdef::mastershortcut_patternFlags_type(instance):
    assert isinstance(instance.patternFlags, str)


@given(instance=DatadiagramMLBasicDef::MasterShortCut_strategy)
def test_datadiagrammlbasicdef::mastershortcut_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original

@given(instance=DatadiagramMLBasicDef::MasterShortCut_strategy)
def test_datadiagrammlbasicdef::mastershortcut_shortcutURL_type(instance):
    assert isinstance(instance.shortcutURL, str)


@given(instance=DatadiagramMLBasicDef::MasterShortCut_strategy)
def test_datadiagrammlbasicdef::mastershortcut_shortcutURL_setter(instance):
    original = instance.shortcutURL
    instance.shortcutURL = original
    assert instance.shortcutURL == original

@given(instance=DatadiagramMLBasicDef::MasterShortCut_strategy)
def test_datadiagrammlbasicdef::mastershortcut_iconSize_type(instance):
    assert isinstance(instance.iconSize, str)


@given(instance=DatadiagramMLBasicDef::MasterShortCut_strategy)
def test_datadiagrammlbasicdef::mastershortcut_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original

@given(instance=DatadiagramMLBasicDef::MasterShortCut_strategy)
def test_datadiagrammlbasicdef::mastershortcut_shortcutHelp_type(instance):
    assert isinstance(instance.shortcutHelp, str)


@given(instance=DatadiagramMLBasicDef::MasterShortCut_strategy)
def test_datadiagrammlbasicdef::mastershortcut_shortcutHelp_setter(instance):
    original = instance.shortcutHelp
    instance.shortcutHelp = original
    assert instance.shortcutHelp == original

@given(instance=DatadiagramMLBasicDef::Master_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::master_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::Master)

@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_iconUpdate_type(instance):
    assert isinstance(instance.iconUpdate, str)


@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_iconUpdate_setter(instance):
    original = instance.iconUpdate
    instance.iconUpdate = original
    assert instance.iconUpdate == original

@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_baseID_type(instance):
    assert isinstance(instance.baseID, str)


@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_baseID_setter(instance):
    original = instance.baseID
    instance.baseID = original
    assert instance.baseID == original

@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_hidden_type(instance):
    assert isinstance(instance.hidden, str)


@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_alignName_type(instance):
    assert isinstance(instance.alignName, str)


@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original

@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_prompt_type(instance):
    assert isinstance(instance.prompt, str)


@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original

@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_patternFlags_type(instance):
    assert isinstance(instance.patternFlags, str)


@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original

@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_iconSize_type(instance):
    assert isinstance(instance.iconSize, str)


@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original

@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_matchByName_type(instance):
    assert isinstance(instance.matchByName, str)


@given(instance=DatadiagramMLBasicDef::Master_strategy)
def test_datadiagrammlbasicdef::master_matchByName_setter(instance):
    original = instance.matchByName
    instance.matchByName = original
    assert instance.matchByName == original

@given(instance=DatadiagramMLBasicDef::Page_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::page_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::Page)

@given(instance=DatadiagramMLBasicDef::Page_strategy)
def test_datadiagrammlbasicdef::page_associatedPage_type(instance):
    assert isinstance(instance.associatedPage, str)


@given(instance=DatadiagramMLBasicDef::Page_strategy)
def test_datadiagrammlbasicdef::page_associatedPage_setter(instance):
    original = instance.associatedPage
    instance.associatedPage = original
    assert instance.associatedPage == original

@given(instance=DatadiagramMLBasicDef::Page_strategy)
def test_datadiagrammlbasicdef::page_viewScale_type(instance):
    assert isinstance(instance.viewScale, str)


@given(instance=DatadiagramMLBasicDef::Page_strategy)
def test_datadiagrammlbasicdef::page_viewScale_setter(instance):
    original = instance.viewScale
    instance.viewScale = original
    assert instance.viewScale == original

@given(instance=DatadiagramMLBasicDef::Page_strategy)
def test_datadiagrammlbasicdef::page_reviewerID_type(instance):
    assert isinstance(instance.reviewerID, str)


@given(instance=DatadiagramMLBasicDef::Page_strategy)
def test_datadiagrammlbasicdef::page_reviewerID_setter(instance):
    original = instance.reviewerID
    instance.reviewerID = original
    assert instance.reviewerID == original

@given(instance=DatadiagramMLBasicDef::Page_strategy)
def test_datadiagrammlbasicdef::page_backPage_type(instance):
    assert isinstance(instance.backPage, str)


@given(instance=DatadiagramMLBasicDef::Page_strategy)
def test_datadiagrammlbasicdef::page_backPage_setter(instance):
    original = instance.backPage
    instance.backPage = original
    assert instance.backPage == original

@given(instance=DatadiagramMLBasicDef::Page_strategy)
def test_datadiagrammlbasicdef::page_viewCenterX_type(instance):
    assert isinstance(instance.viewCenterX, str)


@given(instance=DatadiagramMLBasicDef::Page_strategy)
def test_datadiagrammlbasicdef::page_viewCenterX_setter(instance):
    original = instance.viewCenterX
    instance.viewCenterX = original
    assert instance.viewCenterX == original

@given(instance=DatadiagramMLBasicDef::Page_strategy)
def test_datadiagrammlbasicdef::page_background_type(instance):
    assert isinstance(instance.background, str)


@given(instance=DatadiagramMLBasicDef::Page_strategy)
def test_datadiagrammlbasicdef::page_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original

@given(instance=DatadiagramMLBasicDef::Page_strategy)
def test_datadiagrammlbasicdef::page_ViewCenterY_type(instance):
    assert isinstance(instance.ViewCenterY, str)


@given(instance=DatadiagramMLBasicDef::Page_strategy)
def test_datadiagrammlbasicdef::page_ViewCenterY_setter(instance):
    original = instance.ViewCenterY
    instance.ViewCenterY = original
    assert instance.ViewCenterY == original

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=DatadiagramMLBasicDef::PageSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::pagesheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::PageSheet)

@given(instance=DatadiagramMLBasicDef::StyleSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::stylesheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::StyleSheet)

@given(instance=StyleSheet_strategy)
@settings(max_examples=50)
def test_stylesheet_instantiation(instance):
    assert isinstance(instance, StyleSheet)

@given(instance=DatadiagramMLBasicDef::StyleSheetsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::stylesheetscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::StyleSheetsCollection)

@given(instance=VisioDocument_strategy)
@settings(max_examples=50)
def test_visiodocument_instantiation(instance):
    assert isinstance(instance, VisioDocument)

@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::DocumentPropertiesCollection)

@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_creator_type(instance):
    assert isinstance(instance.creator, str)


@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_creator_setter(instance):
    original = instance.creator
    instance.creator = original
    assert instance.creator == original

@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_template_type(instance):
    assert isinstance(instance.template, str)


@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_company_type(instance):
    assert isinstance(instance.company, str)


@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original

@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_manager_type(instance):
    assert isinstance(instance.manager, str)


@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original

@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_keywords_type(instance):
    assert isinstance(instance.keywords, str)


@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_alternateNames_type(instance):
    assert isinstance(instance.alternateNames, str)


@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_alternateNames_setter(instance):
    original = instance.alternateNames
    instance.alternateNames = original
    assert instance.alternateNames == original

@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_buildNumberCreated_type(instance):
    assert isinstance(instance.buildNumberCreated, str)


@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_buildNumberCreated_setter(instance):
    original = instance.buildNumberCreated
    instance.buildNumberCreated = original
    assert instance.buildNumberCreated == original

@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_buildNumberEdited_type(instance):
    assert isinstance(instance.buildNumberEdited, str)


@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_buildNumberEdited_setter(instance):
    original = instance.buildNumberEdited
    instance.buildNumberEdited = original
    assert instance.buildNumberEdited == original

@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_hyperlinkBase_href_type(instance):
    assert isinstance(instance.hyperlinkBase_href, str)


@given(instance=DatadiagramMLBasicDef::DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef::documentpropertiescollection_hyperlinkBase_href_setter(instance):
    original = instance.hyperlinkBase_href
    instance.hyperlinkBase_href = original
    assert instance.hyperlinkBase_href == original

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=CustomPropertiesCollection_strategy)
@settings(max_examples=50)
def test_custompropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomPropertiesCollection)

@given(instance=MastersCollection_strategy)
@settings(max_examples=50)
def test_masterscollection_instantiation(instance):
    assert isinstance(instance, MastersCollection)

@given(instance=DocumentSheet_strategy)
@settings(max_examples=50)
def test_documentsheet_instantiation(instance):
    assert isinstance(instance, DocumentSheet)

@given(instance=StyleSheetsCollection_strategy)
@settings(max_examples=50)
def test_stylesheetscollection_instantiation(instance):
    assert isinstance(instance, StyleSheetsCollection)

@given(instance=FaceNamesTable_strategy)
@settings(max_examples=50)
def test_facenamestable_instantiation(instance):
    assert isinstance(instance, FaceNamesTable)

@given(instance=FontsTable_strategy)
@settings(max_examples=50)
def test_fontstable_instantiation(instance):
    assert isinstance(instance, FontsTable)

@given(instance=PrintSetup_strategy)
@settings(max_examples=50)
def test_printsetup_instantiation(instance):
    assert isinstance(instance, PrintSetup)

@given(instance=ColorsTable_strategy)
@settings(max_examples=50)
def test_colorstable_instantiation(instance):
    assert isinstance(instance, ColorsTable)

@given(instance=DocumentSettingsElt_strategy)
@settings(max_examples=50)
def test_documentsettingselt_instantiation(instance):
    assert isinstance(instance, DocumentSettingsElt)

@given(instance=DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DocumentPropertiesCollection)

@given(instance=SolutionXML_strategy)
@settings(max_examples=50)
def test_solutionxml_instantiation(instance):
    assert isinstance(instance, SolutionXML)

@given(instance=EmailRoutingData_strategy)
@settings(max_examples=50)
def test_emailroutingdata_instantiation(instance):
    assert isinstance(instance, EmailRoutingData)

@given(instance=VBProjectData_strategy)
@settings(max_examples=50)
def test_vbprojectdata_instantiation(instance):
    assert isinstance(instance, VBProjectData)

@given(instance=HeaderFooter_strategy)
@settings(max_examples=50)
def test_headerfooter_instantiation(instance):
    assert isinstance(instance, HeaderFooter)

@given(instance=EventList_strategy)
@settings(max_examples=50)
def test_eventlist_instantiation(instance):
    assert isinstance(instance, EventList)

@given(instance=WindowsInfo_strategy)
@settings(max_examples=50)
def test_windowsinfo_instantiation(instance):
    assert isinstance(instance, WindowsInfo)

@given(instance=PagesCollection_strategy)
@settings(max_examples=50)
def test_pagescollection_instantiation(instance):
    assert isinstance(instance, PagesCollection)

@given(instance=DatadiagramMLBasicDef::DateTimeType_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::datetimetype_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::DateTimeType)

@given(instance=DatadiagramMLBasicDef::DateTimeType_strategy)
def test_datadiagrammlbasicdef::datetimetype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=DatadiagramMLBasicDef::DateTimeType_strategy)
def test_datadiagrammlbasicdef::datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=DatadiagramMLBasicDef::DateTimeType_strategy)
def test_datadiagrammlbasicdef::datetimetype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=DatadiagramMLBasicDef::DateTimeType_strategy)
def test_datadiagrammlbasicdef::datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=DatadiagramMLBasicDef::DateTimeType_strategy)
def test_datadiagrammlbasicdef::datetimetype_second_type(instance):
    assert isinstance(instance.second, str)


@given(instance=DatadiagramMLBasicDef::DateTimeType_strategy)
def test_datadiagrammlbasicdef::datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=DatadiagramMLBasicDef::DateTimeType_strategy)
def test_datadiagrammlbasicdef::datetimetype_hour_type(instance):
    assert isinstance(instance.hour, str)


@given(instance=DatadiagramMLBasicDef::DateTimeType_strategy)
def test_datadiagrammlbasicdef::datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=DatadiagramMLBasicDef::DateTimeType_strategy)
def test_datadiagrammlbasicdef::datetimetype_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=DatadiagramMLBasicDef::DateTimeType_strategy)
def test_datadiagrammlbasicdef::datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=DatadiagramMLBasicDef::DateTimeType_strategy)
def test_datadiagrammlbasicdef::datetimetype_minute_type(instance):
    assert isinstance(instance.minute, str)


@given(instance=DatadiagramMLBasicDef::DateTimeType_strategy)
def test_datadiagrammlbasicdef::datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original

@given(instance=DatadiagramMLBasicDef::VisioDocument_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::visiodocument_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::VisioDocument)

@given(instance=DatadiagramMLBasicDef::VisioDocument_strategy)
def test_datadiagrammlbasicdef::visiodocument_metric_type(instance):
    assert isinstance(instance.metric, str)


@given(instance=DatadiagramMLBasicDef::VisioDocument_strategy)
def test_datadiagrammlbasicdef::visiodocument_metric_setter(instance):
    original = instance.metric
    instance.metric = original
    assert instance.metric == original

@given(instance=DatadiagramMLBasicDef::VisioDocument_strategy)
def test_datadiagrammlbasicdef::visiodocument_buildnum_type(instance):
    assert isinstance(instance.buildnum, str)


@given(instance=DatadiagramMLBasicDef::VisioDocument_strategy)
def test_datadiagrammlbasicdef::visiodocument_buildnum_setter(instance):
    original = instance.buildnum
    instance.buildnum = original
    assert instance.buildnum == original

@given(instance=DatadiagramMLBasicDef::VisioDocument_strategy)
def test_datadiagrammlbasicdef::visiodocument_docLangId_type(instance):
    assert isinstance(instance.docLangId, str)


@given(instance=DatadiagramMLBasicDef::VisioDocument_strategy)
def test_datadiagrammlbasicdef::visiodocument_docLangId_setter(instance):
    original = instance.docLangId
    instance.docLangId = original
    assert instance.docLangId == original

@given(instance=DatadiagramMLBasicDef::VisioDocument_strategy)
def test_datadiagrammlbasicdef::visiodocument_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=DatadiagramMLBasicDef::VisioDocument_strategy)
def test_datadiagrammlbasicdef::visiodocument_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=DatadiagramMLBasicDef::VisioDocument_strategy)
def test_datadiagrammlbasicdef::visiodocument_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=DatadiagramMLBasicDef::VisioDocument_strategy)
def test_datadiagrammlbasicdef::visiodocument_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=DatadiagramMLBasicDef::VisioDocument_strategy)
def test_datadiagrammlbasicdef::visiodocument_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=DatadiagramMLBasicDef::VisioDocument_strategy)
def test_datadiagrammlbasicdef::visiodocument_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=DatadiagramMLBasicDef::CellType_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef::celltype_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef::CellType)

@given(instance=DatadiagramMLBasicDef::CellType_strategy)
def test_datadiagrammlbasicdef::celltype_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=DatadiagramMLBasicDef::CellType_strategy)
def test_datadiagrammlbasicdef::celltype_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=DatadiagramMLBasicDef::CellType_strategy)
def test_datadiagrammlbasicdef::celltype_formula_type(instance):
    assert isinstance(instance.formula, str)


@given(instance=DatadiagramMLBasicDef::CellType_strategy)
def test_datadiagrammlbasicdef::celltype_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=DatadiagramMLBasicDef::CellType_strategy)
def test_datadiagrammlbasicdef::celltype_err_type(instance):
    assert isinstance(instance.err, str)


@given(instance=DatadiagramMLBasicDef::CellType_strategy)
def test_datadiagrammlbasicdef::celltype_err_setter(instance):
    original = instance.err
    instance.err = original
    assert instance.err == original

@given(instance=DatadiagramMLBasicDef::CellType_strategy)
def test_datadiagrammlbasicdef::celltype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DatadiagramMLBasicDef::CellType_strategy)
def test_datadiagrammlbasicdef::celltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
