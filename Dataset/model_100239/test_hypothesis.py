import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DatadiagramMLTextFormat::SolutionXML,
    DatadiagramMLTextFormat::HeaderFooter,
    DatadiagramMLTextFormat::EventList,
    DatadiagramMLTextFormat::WindowsInfo,
    DatadiagramMLTextFormat::DocumentSettingsElt,
    DatadiagramMLTextFormat::PageElt,
    DatadiagramMLTextFormat::PrintSetup,
    DatadiagramMLTextFormat::PagesCollection,
    DatadiagramMLTextFormat::MasterElt,
    ConnectsCollection,
    DatadiagramMLTextFormat::Connect,
    Connect,
    Page,
    Icon,
    MasterShortCut,
    Master,
    DatadiagramMLTextFormat::MastersCollection,
    TabsCollection,
    Tab,
    DatadiagramMLTextFormat::IXrequiredElt,
    Text,
    DatadiagramMLTextFormat::TextElt,
    XYABCDElt,
    DatadiagramMLTextFormat::EllipticalArcTo,
    DatadiagramMLTextFormat::Ellipse,
    TextElt,
    DatadiagramMLTextFormat::StringElt,
    XYABCDEElt,
    DatadiagramMLTextFormat::NURBSTo,
    DatadiagramMLTextFormat::XYABCDEElt,
    DatadiagramMLTextFormat::SplineStart,
    XYABElt,
    DatadiagramMLTextFormat::XYABCDElt,
    DatadiagramMLTextFormat::InfiniteLine,
    XYAElt,
    DatadiagramMLTextFormat::SplineKnot,
    DatadiagramMLTextFormat::XYABElt,
    DatadiagramMLTextFormat::PolylineTo,
    DatadiagramMLTextFormat::ArcTo,
    Geom,
    XYElt,
    DatadiagramMLTextFormat::MoveTo,
    DatadiagramMLTextFormat::XYAElt,
    DatadiagramMLTextFormat::LineTo,
    SplineKnot,
    ArcTo,
    NURBSTo,
    SplineStart,
    EllipticalArcTo,
    Ellipse,
    InfiniteLine,
    PolylineTo,
    DatadiagramMLTextFormat::DelElt,
    DatadiagramMLTextFormat::IXElt,
    MoveTo,
    LineTo,
    CellType,
    DelElt,
    IXElt,
    DatadiagramMLTextFormat::XYElt,
    DatadiagramMLTextFormat::Tab,
    DatadiagramMLTextFormat::NamedElt,
    PageElt,
    MasterElt,
    DatadiagramMLTextFormat::ConnectsCollection,
    DatadiagramMLTextFormat::ShapesCollection,
    DatadiagramMLTextFormat::Icon,
    UniqueIdElt,
    DatadiagramMLTextFormat::ShapeElt,
    ShapeElt,
    DatadiagramMLTextFormat::Field,
    DatadiagramMLTextFormat::Para,
    DatadiagramMLTextFormat::Text,
    DatadiagramMLTextFormat::Geom,
    DatadiagramMLTextFormat::Char,
    DatadiagramMLTextFormat::TabsCollection,
    ShapesCollection,
    DatadiagramMLTextFormat::Shape,
    DatadiagramMLTextFormat::UniqueIdElt,
    DatadiagramMLTextFormat::IdentifiedElt,
    DatadiagramMLTextFormat::VBProjectData,
    PageSheet,
    NamedElt,
    DatadiagramMLTextFormat::DocumentSheet,
    Shape,
    DatadiagramMLTextFormat::PageSheet,
    PagesCollection,
    MastersCollection,
    DocumentSheet,
    DatadiagramMLTextFormat::DateTimeType,
    DocumentSettingsElt,
    DocumentPropertiesCollection,
    DatadiagramMLTextFormat::VisioDocument,
    DatadiagramMLTextFormat::CellType,
    StyleSheet,
    DatadiagramMLTextFormat::StyleSheetsCollection,
    DatadiagramMLTextFormat::EmailRoutingData,
    FontEntry,
    DatadiagramMLTextFormat::FontsTable,
    FaceName,
    DatadiagramMLTextFormat::FaceNamesTable,
    IdentifiedElt,
    DatadiagramMLTextFormat::Page,
    DatadiagramMLTextFormat::StyleSheet,
    DatadiagramMLTextFormat::MasterShortCut,
    DatadiagramMLTextFormat::Master,
    DatadiagramMLTextFormat::FaceName,
    CustomProperty,
    DatadiagramMLTextFormat::FontEntry,
    DatadiagramMLTextFormat::CustomPropertiesCollection,
    IXrequiredElt,
    DatadiagramMLTextFormat::Tp,
    DatadiagramMLTextFormat::Pp,
    DatadiagramMLTextFormat::Fld,
    DatadiagramMLTextFormat::Cp,
    DatadiagramMLTextFormat::ColorEntry,
    ColorEntry,
    DatadiagramMLTextFormat::ColorsTable,
    DatadiagramMLTextFormat::CustomProperty,
    DateTimeType,
    CustomPropertiesCollection,
    StyleSheetsCollection,
    FaceNamesTable,
    FontsTable,
    PrintSetup,
    ColorsTable,
    VisioDocument,
    DatadiagramMLTextFormat::DocumentPropertiesCollection,
    SolutionXML,
    EmailRoutingData,
    VBProjectData,
    HeaderFooter,
    EventList,
    WindowsInfo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datadiagrammltextformat::solutionxml_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::SolutionXML)


def test_datadiagrammltextformat::solutionxml_constructor_exists():
    assert callable(DatadiagramMLTextFormat::SolutionXML.__init__)


def test_datadiagrammltextformat::solutionxml_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::SolutionXML.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::headerfooter_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::HeaderFooter)


def test_datadiagrammltextformat::headerfooter_constructor_exists():
    assert callable(DatadiagramMLTextFormat::HeaderFooter.__init__)


def test_datadiagrammltextformat::headerfooter_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::HeaderFooter.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::eventlist_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::EventList)


def test_datadiagrammltextformat::eventlist_constructor_exists():
    assert callable(DatadiagramMLTextFormat::EventList.__init__)


def test_datadiagrammltextformat::eventlist_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::EventList.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::windowsinfo_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::WindowsInfo)


def test_datadiagrammltextformat::windowsinfo_constructor_exists():
    assert callable(DatadiagramMLTextFormat::WindowsInfo.__init__)


def test_datadiagrammltextformat::windowsinfo_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::WindowsInfo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::documentsettingselt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::DocumentSettingsElt)


def test_datadiagrammltextformat::documentsettingselt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::DocumentSettingsElt.__init__)


def test_datadiagrammltextformat::documentsettingselt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::DocumentSettingsElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::pageelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::PageElt)


def test_datadiagrammltextformat::pageelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::PageElt.__init__)


def test_datadiagrammltextformat::pageelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::PageElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::printsetup_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::PrintSetup)


def test_datadiagrammltextformat::printsetup_constructor_exists():
    assert callable(DatadiagramMLTextFormat::PrintSetup.__init__)


def test_datadiagrammltextformat::printsetup_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::PrintSetup.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::pagescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::PagesCollection)


def test_datadiagrammltextformat::pagescollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat::PagesCollection.__init__)


def test_datadiagrammltextformat::pagescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::PagesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::masterelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::MasterElt)


def test_datadiagrammltextformat::masterelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::MasterElt.__init__)


def test_datadiagrammltextformat::masterelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::MasterElt.__init__)
    params = list(sig.parameters.keys())



def test_connectscollection_is_not_abstract():
    assert not inspect.isabstract(ConnectsCollection)


def test_connectscollection_constructor_exists():
    assert callable(ConnectsCollection.__init__)


def test_connectscollection_constructor_args():
    sig = inspect.signature(ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::connect_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Connect)


def test_datadiagrammltextformat::connect_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Connect.__init__)


def test_datadiagrammltextformat::connect_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Connect.__init__)
    params = list(sig.parameters.keys())
    assert "toCell" in params, "Missing parameter 'toCell'"
    assert "fromPart" in params, "Missing parameter 'fromPart'"
    assert "toPart" in params, "Missing parameter 'toPart'"
    assert "toSheet" in params, "Missing parameter 'toSheet'"
    assert "fromCell" in params, "Missing parameter 'fromCell'"
    assert "fromSheet" in params, "Missing parameter 'fromSheet'"

def test_datadiagrammltextformat::connect_has_toCell():
    assert hasattr(DatadiagramMLTextFormat::Connect, "toCell")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Connect.__mro__:
        if "toCell" in klass.__dict__:
            descriptor = klass.__dict__["toCell"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::connect_has_fromPart():
    assert hasattr(DatadiagramMLTextFormat::Connect, "fromPart")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Connect.__mro__:
        if "fromPart" in klass.__dict__:
            descriptor = klass.__dict__["fromPart"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::connect_has_toPart():
    assert hasattr(DatadiagramMLTextFormat::Connect, "toPart")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Connect.__mro__:
        if "toPart" in klass.__dict__:
            descriptor = klass.__dict__["toPart"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::connect_has_toSheet():
    assert hasattr(DatadiagramMLTextFormat::Connect, "toSheet")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Connect.__mro__:
        if "toSheet" in klass.__dict__:
            descriptor = klass.__dict__["toSheet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::connect_has_fromCell():
    assert hasattr(DatadiagramMLTextFormat::Connect, "fromCell")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Connect.__mro__:
        if "fromCell" in klass.__dict__:
            descriptor = klass.__dict__["fromCell"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::connect_has_fromSheet():
    assert hasattr(DatadiagramMLTextFormat::Connect, "fromSheet")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Connect.__mro__:
        if "fromSheet" in klass.__dict__:
            descriptor = klass.__dict__["fromSheet"]
            break
    assert isinstance(descriptor, property)



def test_connect_is_not_abstract():
    assert not inspect.isabstract(Connect)


def test_connect_constructor_exists():
    assert callable(Connect.__init__)


def test_connect_constructor_args():
    sig = inspect.signature(Connect.__init__)
    params = list(sig.parameters.keys())



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_icon_is_not_abstract():
    assert not inspect.isabstract(Icon)


def test_icon_constructor_exists():
    assert callable(Icon.__init__)


def test_icon_constructor_args():
    sig = inspect.signature(Icon.__init__)
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



def test_datadiagrammltextformat::masterscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::MastersCollection)


def test_datadiagrammltextformat::masterscollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat::MastersCollection.__init__)


def test_datadiagrammltextformat::masterscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::MastersCollection.__init__)
    params = list(sig.parameters.keys())



def test_tabscollection_is_not_abstract():
    assert not inspect.isabstract(TabsCollection)


def test_tabscollection_constructor_exists():
    assert callable(TabsCollection.__init__)


def test_tabscollection_constructor_args():
    sig = inspect.signature(TabsCollection.__init__)
    params = list(sig.parameters.keys())



def test_tab_is_not_abstract():
    assert not inspect.isabstract(Tab)


def test_tab_constructor_exists():
    assert callable(Tab.__init__)


def test_tab_constructor_args():
    sig = inspect.signature(Tab.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::ixrequiredelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::IXrequiredElt)


def test_datadiagrammltextformat::ixrequiredelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::IXrequiredElt.__init__)


def test_datadiagrammltextformat::ixrequiredelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::IXrequiredElt.__init__)
    params = list(sig.parameters.keys())
    assert "iX" in params, "Missing parameter 'iX'"

def test_datadiagrammltextformat::ixrequiredelt_has_iX():
    assert hasattr(DatadiagramMLTextFormat::IXrequiredElt, "iX")
    descriptor = None
    for klass in DatadiagramMLTextFormat::IXrequiredElt.__mro__:
        if "iX" in klass.__dict__:
            descriptor = klass.__dict__["iX"]
            break
    assert isinstance(descriptor, property)



def test_text_is_not_abstract():
    assert not inspect.isabstract(Text)


def test_text_constructor_exists():
    assert callable(Text.__init__)


def test_text_constructor_args():
    sig = inspect.signature(Text.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::textelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::TextElt)


def test_datadiagrammltextformat::textelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::TextElt.__init__)


def test_datadiagrammltextformat::textelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::TextElt.__init__)
    params = list(sig.parameters.keys())



def test_xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(XYABCDElt)


def test_xyabcdelt_constructor_exists():
    assert callable(XYABCDElt.__init__)


def test_xyabcdelt_constructor_args():
    sig = inspect.signature(XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::ellipticalarcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::EllipticalArcTo)


def test_datadiagrammltextformat::ellipticalarcto_constructor_exists():
    assert callable(DatadiagramMLTextFormat::EllipticalArcTo.__init__)


def test_datadiagrammltextformat::ellipticalarcto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::EllipticalArcTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::ellipse_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Ellipse)


def test_datadiagrammltextformat::ellipse_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Ellipse.__init__)


def test_datadiagrammltextformat::ellipse_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_textelt_is_not_abstract():
    assert not inspect.isabstract(TextElt)


def test_textelt_constructor_exists():
    assert callable(TextElt.__init__)


def test_textelt_constructor_args():
    sig = inspect.signature(TextElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::stringelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::StringElt)


def test_datadiagrammltextformat::stringelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::StringElt.__init__)


def test_datadiagrammltextformat::stringelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::StringElt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammltextformat::stringelt_has_value():
    assert hasattr(DatadiagramMLTextFormat::StringElt, "value")
    descriptor = None
    for klass in DatadiagramMLTextFormat::StringElt.__mro__:
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



def test_datadiagrammltextformat::nurbsto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::NURBSTo)


def test_datadiagrammltextformat::nurbsto_constructor_exists():
    assert callable(DatadiagramMLTextFormat::NURBSTo.__init__)


def test_datadiagrammltextformat::nurbsto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::NURBSTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::xyabcdeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::XYABCDEElt)


def test_datadiagrammltextformat::xyabcdeelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::XYABCDEElt.__init__)


def test_datadiagrammltextformat::xyabcdeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::XYABCDEElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::splinestart_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::SplineStart)


def test_datadiagrammltextformat::splinestart_constructor_exists():
    assert callable(DatadiagramMLTextFormat::SplineStart.__init__)


def test_datadiagrammltextformat::splinestart_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::SplineStart.__init__)
    params = list(sig.parameters.keys())



def test_xyabelt_is_not_abstract():
    assert not inspect.isabstract(XYABElt)


def test_xyabelt_constructor_exists():
    assert callable(XYABElt.__init__)


def test_xyabelt_constructor_args():
    sig = inspect.signature(XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::XYABCDElt)


def test_datadiagrammltextformat::xyabcdelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::XYABCDElt.__init__)


def test_datadiagrammltextformat::xyabcdelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::infiniteline_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::InfiniteLine)


def test_datadiagrammltextformat::infiniteline_constructor_exists():
    assert callable(DatadiagramMLTextFormat::InfiniteLine.__init__)


def test_datadiagrammltextformat::infiniteline_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::InfiniteLine.__init__)
    params = list(sig.parameters.keys())



def test_xyaelt_is_not_abstract():
    assert not inspect.isabstract(XYAElt)


def test_xyaelt_constructor_exists():
    assert callable(XYAElt.__init__)


def test_xyaelt_constructor_args():
    sig = inspect.signature(XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::splineknot_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::SplineKnot)


def test_datadiagrammltextformat::splineknot_constructor_exists():
    assert callable(DatadiagramMLTextFormat::SplineKnot.__init__)


def test_datadiagrammltextformat::splineknot_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::SplineKnot.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::xyabelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::XYABElt)


def test_datadiagrammltextformat::xyabelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::XYABElt.__init__)


def test_datadiagrammltextformat::xyabelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::polylineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::PolylineTo)


def test_datadiagrammltextformat::polylineto_constructor_exists():
    assert callable(DatadiagramMLTextFormat::PolylineTo.__init__)


def test_datadiagrammltextformat::polylineto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::PolylineTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::arcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::ArcTo)


def test_datadiagrammltextformat::arcto_constructor_exists():
    assert callable(DatadiagramMLTextFormat::ArcTo.__init__)


def test_datadiagrammltextformat::arcto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::ArcTo.__init__)
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



def test_datadiagrammltextformat::moveto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::MoveTo)


def test_datadiagrammltextformat::moveto_constructor_exists():
    assert callable(DatadiagramMLTextFormat::MoveTo.__init__)


def test_datadiagrammltextformat::moveto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::xyaelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::XYAElt)


def test_datadiagrammltextformat::xyaelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::XYAElt.__init__)


def test_datadiagrammltextformat::xyaelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::lineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::LineTo)


def test_datadiagrammltextformat::lineto_constructor_exists():
    assert callable(DatadiagramMLTextFormat::LineTo.__init__)


def test_datadiagrammltextformat::lineto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::LineTo.__init__)
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



def test_datadiagrammltextformat::delelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::DelElt)


def test_datadiagrammltextformat::delelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::DelElt.__init__)


def test_datadiagrammltextformat::delelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::DelElt.__init__)
    params = list(sig.parameters.keys())
    assert "del_" in params, "Missing parameter 'del_'"

def test_datadiagrammltextformat::delelt_has_del_():
    assert hasattr(DatadiagramMLTextFormat::DelElt, "del_")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DelElt.__mro__:
        if "del_" in klass.__dict__:
            descriptor = klass.__dict__["del_"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat::ixelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::IXElt)


def test_datadiagrammltextformat::ixelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::IXElt.__init__)


def test_datadiagrammltextformat::ixelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::IXElt.__init__)
    params = list(sig.parameters.keys())
    assert "iX" in params, "Missing parameter 'iX'"

def test_datadiagrammltextformat::ixelt_has_iX():
    assert hasattr(DatadiagramMLTextFormat::IXElt, "iX")
    descriptor = None
    for klass in DatadiagramMLTextFormat::IXElt.__mro__:
        if "iX" in klass.__dict__:
            descriptor = klass.__dict__["iX"]
            break
    assert isinstance(descriptor, property)



def test_moveto_is_not_abstract():
    assert not inspect.isabstract(MoveTo)


def test_moveto_constructor_exists():
    assert callable(MoveTo.__init__)


def test_moveto_constructor_args():
    sig = inspect.signature(MoveTo.__init__)
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



def test_datadiagrammltextformat::xyelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::XYElt)


def test_datadiagrammltextformat::xyelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::XYElt.__init__)


def test_datadiagrammltextformat::xyelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::XYElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::tab_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Tab)


def test_datadiagrammltextformat::tab_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Tab.__init__)


def test_datadiagrammltextformat::tab_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Tab.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::namedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::NamedElt)


def test_datadiagrammltextformat::namedelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::NamedElt.__init__)


def test_datadiagrammltextformat::namedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "nameU" in params, "Missing parameter 'nameU'"
    assert "name" in params, "Missing parameter 'name'"

def test_datadiagrammltextformat::namedelt_has_nameU():
    assert hasattr(DatadiagramMLTextFormat::NamedElt, "nameU")
    descriptor = None
    for klass in DatadiagramMLTextFormat::NamedElt.__mro__:
        if "nameU" in klass.__dict__:
            descriptor = klass.__dict__["nameU"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::namedelt_has_name():
    assert hasattr(DatadiagramMLTextFormat::NamedElt, "name")
    descriptor = None
    for klass in DatadiagramMLTextFormat::NamedElt.__mro__:
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



def test_datadiagrammltextformat::connectscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::ConnectsCollection)


def test_datadiagrammltextformat::connectscollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat::ConnectsCollection.__init__)


def test_datadiagrammltextformat::connectscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::shapescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::ShapesCollection)


def test_datadiagrammltextformat::shapescollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat::ShapesCollection.__init__)


def test_datadiagrammltextformat::shapescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::icon_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Icon)


def test_datadiagrammltextformat::icon_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Icon.__init__)


def test_datadiagrammltextformat::icon_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Icon.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammltextformat::icon_has_value():
    assert hasattr(DatadiagramMLTextFormat::Icon, "value")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Icon.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(UniqueIdElt)


def test_uniqueidelt_constructor_exists():
    assert callable(UniqueIdElt.__init__)


def test_uniqueidelt_constructor_args():
    sig = inspect.signature(UniqueIdElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::shapeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::ShapeElt)


def test_datadiagrammltextformat::shapeelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::ShapeElt.__init__)


def test_datadiagrammltextformat::shapeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_shapeelt_is_not_abstract():
    assert not inspect.isabstract(ShapeElt)


def test_shapeelt_constructor_exists():
    assert callable(ShapeElt.__init__)


def test_shapeelt_constructor_args():
    sig = inspect.signature(ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::field_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Field)


def test_datadiagrammltextformat::field_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Field.__init__)


def test_datadiagrammltextformat::field_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Field.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::para_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Para)


def test_datadiagrammltextformat::para_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Para.__init__)


def test_datadiagrammltextformat::para_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Para.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::text_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Text)


def test_datadiagrammltextformat::text_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Text.__init__)


def test_datadiagrammltextformat::text_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Text.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::geom_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Geom)


def test_datadiagrammltextformat::geom_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Geom.__init__)


def test_datadiagrammltextformat::geom_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Geom.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::char_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Char)


def test_datadiagrammltextformat::char_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Char.__init__)


def test_datadiagrammltextformat::char_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Char.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::tabscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::TabsCollection)


def test_datadiagrammltextformat::tabscollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat::TabsCollection.__init__)


def test_datadiagrammltextformat::tabscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::TabsCollection.__init__)
    params = list(sig.parameters.keys())



def test_shapescollection_is_not_abstract():
    assert not inspect.isabstract(ShapesCollection)


def test_shapescollection_constructor_exists():
    assert callable(ShapesCollection.__init__)


def test_shapescollection_constructor_args():
    sig = inspect.signature(ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::shape_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Shape)


def test_datadiagrammltextformat::shape_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Shape.__init__)


def test_datadiagrammltextformat::shape_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Shape.__init__)
    params = list(sig.parameters.keys())
    assert "textStyle" in params, "Missing parameter 'textStyle'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "fillStyle" in params, "Missing parameter 'fillStyle'"

def test_datadiagrammltextformat::shape_has_textStyle():
    assert hasattr(DatadiagramMLTextFormat::Shape, "textStyle")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Shape.__mro__:
        if "textStyle" in klass.__dict__:
            descriptor = klass.__dict__["textStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::shape_has_lineStyle():
    assert hasattr(DatadiagramMLTextFormat::Shape, "lineStyle")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Shape.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::shape_has_fillStyle():
    assert hasattr(DatadiagramMLTextFormat::Shape, "fillStyle")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Shape.__mro__:
        if "fillStyle" in klass.__dict__:
            descriptor = klass.__dict__["fillStyle"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat::uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::UniqueIdElt)


def test_datadiagrammltextformat::uniqueidelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::UniqueIdElt.__init__)


def test_datadiagrammltextformat::uniqueidelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::UniqueIdElt.__init__)
    params = list(sig.parameters.keys())
    assert "UniqueID" in params, "Missing parameter 'UniqueID'"

def test_datadiagrammltextformat::uniqueidelt_has_UniqueID():
    assert hasattr(DatadiagramMLTextFormat::UniqueIdElt, "UniqueID")
    descriptor = None
    for klass in DatadiagramMLTextFormat::UniqueIdElt.__mro__:
        if "UniqueID" in klass.__dict__:
            descriptor = klass.__dict__["UniqueID"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat::identifiedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::IdentifiedElt)


def test_datadiagrammltextformat::identifiedelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat::IdentifiedElt.__init__)


def test_datadiagrammltextformat::identifiedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::IdentifiedElt.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_datadiagrammltextformat::identifiedelt_has_ID():
    assert hasattr(DatadiagramMLTextFormat::IdentifiedElt, "ID")
    descriptor = None
    for klass in DatadiagramMLTextFormat::IdentifiedElt.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat::vbprojectdata_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::VBProjectData)


def test_datadiagrammltextformat::vbprojectdata_constructor_exists():
    assert callable(DatadiagramMLTextFormat::VBProjectData.__init__)


def test_datadiagrammltextformat::vbprojectdata_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::VBProjectData.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_datadiagrammltextformat::vbprojectdata_has_data():
    assert hasattr(DatadiagramMLTextFormat::VBProjectData, "data")
    descriptor = None
    for klass in DatadiagramMLTextFormat::VBProjectData.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



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



def test_datadiagrammltextformat::documentsheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::DocumentSheet)


def test_datadiagrammltextformat::documentsheet_constructor_exists():
    assert callable(DatadiagramMLTextFormat::DocumentSheet.__init__)


def test_datadiagrammltextformat::documentsheet_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::DocumentSheet.__init__)
    params = list(sig.parameters.keys())



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::pagesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::PageSheet)


def test_datadiagrammltextformat::pagesheet_constructor_exists():
    assert callable(DatadiagramMLTextFormat::PageSheet.__init__)


def test_datadiagrammltextformat::pagesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::PageSheet.__init__)
    params = list(sig.parameters.keys())



def test_pagescollection_is_not_abstract():
    assert not inspect.isabstract(PagesCollection)


def test_pagescollection_constructor_exists():
    assert callable(PagesCollection.__init__)


def test_pagescollection_constructor_args():
    sig = inspect.signature(PagesCollection.__init__)
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



def test_datadiagrammltextformat::datetimetype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::DateTimeType)


def test_datadiagrammltextformat::datetimetype_constructor_exists():
    assert callable(DatadiagramMLTextFormat::DateTimeType.__init__)


def test_datadiagrammltextformat::datetimetype_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "hour" in params, "Missing parameter 'hour'"
    assert "year" in params, "Missing parameter 'year'"
    assert "second" in params, "Missing parameter 'second'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "day" in params, "Missing parameter 'day'"
    assert "month" in params, "Missing parameter 'month'"

def test_datadiagrammltextformat::datetimetype_has_hour():
    assert hasattr(DatadiagramMLTextFormat::DateTimeType, "hour")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::datetimetype_has_year():
    assert hasattr(DatadiagramMLTextFormat::DateTimeType, "year")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::datetimetype_has_second():
    assert hasattr(DatadiagramMLTextFormat::DateTimeType, "second")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::datetimetype_has_minute():
    assert hasattr(DatadiagramMLTextFormat::DateTimeType, "minute")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::datetimetype_has_day():
    assert hasattr(DatadiagramMLTextFormat::DateTimeType, "day")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::datetimetype_has_month():
    assert hasattr(DatadiagramMLTextFormat::DateTimeType, "month")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)



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



def test_datadiagrammltextformat::visiodocument_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::VisioDocument)


def test_datadiagrammltextformat::visiodocument_constructor_exists():
    assert callable(DatadiagramMLTextFormat::VisioDocument.__init__)


def test_datadiagrammltextformat::visiodocument_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::VisioDocument.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "key" in params, "Missing parameter 'key'"
    assert "version" in params, "Missing parameter 'version'"
    assert "buildnum" in params, "Missing parameter 'buildnum'"
    assert "docLangId" in params, "Missing parameter 'docLangId'"
    assert "metric" in params, "Missing parameter 'metric'"

def test_datadiagrammltextformat::visiodocument_has_start():
    assert hasattr(DatadiagramMLTextFormat::VisioDocument, "start")
    descriptor = None
    for klass in DatadiagramMLTextFormat::VisioDocument.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::visiodocument_has_key():
    assert hasattr(DatadiagramMLTextFormat::VisioDocument, "key")
    descriptor = None
    for klass in DatadiagramMLTextFormat::VisioDocument.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::visiodocument_has_version():
    assert hasattr(DatadiagramMLTextFormat::VisioDocument, "version")
    descriptor = None
    for klass in DatadiagramMLTextFormat::VisioDocument.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::visiodocument_has_buildnum():
    assert hasattr(DatadiagramMLTextFormat::VisioDocument, "buildnum")
    descriptor = None
    for klass in DatadiagramMLTextFormat::VisioDocument.__mro__:
        if "buildnum" in klass.__dict__:
            descriptor = klass.__dict__["buildnum"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::visiodocument_has_docLangId():
    assert hasattr(DatadiagramMLTextFormat::VisioDocument, "docLangId")
    descriptor = None
    for klass in DatadiagramMLTextFormat::VisioDocument.__mro__:
        if "docLangId" in klass.__dict__:
            descriptor = klass.__dict__["docLangId"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::visiodocument_has_metric():
    assert hasattr(DatadiagramMLTextFormat::VisioDocument, "metric")
    descriptor = None
    for klass in DatadiagramMLTextFormat::VisioDocument.__mro__:
        if "metric" in klass.__dict__:
            descriptor = klass.__dict__["metric"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat::celltype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::CellType)


def test_datadiagrammltextformat::celltype_constructor_exists():
    assert callable(DatadiagramMLTextFormat::CellType.__init__)


def test_datadiagrammltextformat::celltype_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::CellType.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "formula" in params, "Missing parameter 'formula'"
    assert "err" in params, "Missing parameter 'err'"
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammltextformat::celltype_has_unit():
    assert hasattr(DatadiagramMLTextFormat::CellType, "unit")
    descriptor = None
    for klass in DatadiagramMLTextFormat::CellType.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::celltype_has_formula():
    assert hasattr(DatadiagramMLTextFormat::CellType, "formula")
    descriptor = None
    for klass in DatadiagramMLTextFormat::CellType.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::celltype_has_err():
    assert hasattr(DatadiagramMLTextFormat::CellType, "err")
    descriptor = None
    for klass in DatadiagramMLTextFormat::CellType.__mro__:
        if "err" in klass.__dict__:
            descriptor = klass.__dict__["err"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::celltype_has_value():
    assert hasattr(DatadiagramMLTextFormat::CellType, "value")
    descriptor = None
    for klass in DatadiagramMLTextFormat::CellType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_stylesheet_is_not_abstract():
    assert not inspect.isabstract(StyleSheet)


def test_stylesheet_constructor_exists():
    assert callable(StyleSheet.__init__)


def test_stylesheet_constructor_args():
    sig = inspect.signature(StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::stylesheetscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::StyleSheetsCollection)


def test_datadiagrammltextformat::stylesheetscollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat::StyleSheetsCollection.__init__)


def test_datadiagrammltextformat::stylesheetscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::StyleSheetsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::emailroutingdata_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::EmailRoutingData)


def test_datadiagrammltextformat::emailroutingdata_constructor_exists():
    assert callable(DatadiagramMLTextFormat::EmailRoutingData.__init__)


def test_datadiagrammltextformat::emailroutingdata_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::EmailRoutingData.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "data" in params, "Missing parameter 'data'"

def test_datadiagrammltextformat::emailroutingdata_has_size():
    assert hasattr(DatadiagramMLTextFormat::EmailRoutingData, "size")
    descriptor = None
    for klass in DatadiagramMLTextFormat::EmailRoutingData.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::emailroutingdata_has_data():
    assert hasattr(DatadiagramMLTextFormat::EmailRoutingData, "data")
    descriptor = None
    for klass in DatadiagramMLTextFormat::EmailRoutingData.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_fontentry_is_not_abstract():
    assert not inspect.isabstract(FontEntry)


def test_fontentry_constructor_exists():
    assert callable(FontEntry.__init__)


def test_fontentry_constructor_args():
    sig = inspect.signature(FontEntry.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::fontstable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::FontsTable)


def test_datadiagrammltextformat::fontstable_constructor_exists():
    assert callable(DatadiagramMLTextFormat::FontsTable.__init__)


def test_datadiagrammltextformat::fontstable_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::FontsTable.__init__)
    params = list(sig.parameters.keys())



def test_facename_is_not_abstract():
    assert not inspect.isabstract(FaceName)


def test_facename_constructor_exists():
    assert callable(FaceName.__init__)


def test_facename_constructor_args():
    sig = inspect.signature(FaceName.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::facenamestable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::FaceNamesTable)


def test_datadiagrammltextformat::facenamestable_constructor_exists():
    assert callable(DatadiagramMLTextFormat::FaceNamesTable.__init__)


def test_datadiagrammltextformat::facenamestable_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::FaceNamesTable.__init__)
    params = list(sig.parameters.keys())



def test_identifiedelt_is_not_abstract():
    assert not inspect.isabstract(IdentifiedElt)


def test_identifiedelt_constructor_exists():
    assert callable(IdentifiedElt.__init__)


def test_identifiedelt_constructor_args():
    sig = inspect.signature(IdentifiedElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::page_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Page)


def test_datadiagrammltextformat::page_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Page.__init__)


def test_datadiagrammltextformat::page_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Page.__init__)
    params = list(sig.parameters.keys())
    assert "backPage" in params, "Missing parameter 'backPage'"
    assert "reviewerID" in params, "Missing parameter 'reviewerID'"
    assert "associatedPage" in params, "Missing parameter 'associatedPage'"
    assert "viewCenterX" in params, "Missing parameter 'viewCenterX'"
    assert "ViewCenterY" in params, "Missing parameter 'ViewCenterY'"
    assert "viewScale" in params, "Missing parameter 'viewScale'"
    assert "background" in params, "Missing parameter 'background'"

def test_datadiagrammltextformat::page_has_backPage():
    assert hasattr(DatadiagramMLTextFormat::Page, "backPage")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Page.__mro__:
        if "backPage" in klass.__dict__:
            descriptor = klass.__dict__["backPage"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::page_has_reviewerID():
    assert hasattr(DatadiagramMLTextFormat::Page, "reviewerID")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Page.__mro__:
        if "reviewerID" in klass.__dict__:
            descriptor = klass.__dict__["reviewerID"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::page_has_associatedPage():
    assert hasattr(DatadiagramMLTextFormat::Page, "associatedPage")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Page.__mro__:
        if "associatedPage" in klass.__dict__:
            descriptor = klass.__dict__["associatedPage"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::page_has_viewCenterX():
    assert hasattr(DatadiagramMLTextFormat::Page, "viewCenterX")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Page.__mro__:
        if "viewCenterX" in klass.__dict__:
            descriptor = klass.__dict__["viewCenterX"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::page_has_ViewCenterY():
    assert hasattr(DatadiagramMLTextFormat::Page, "ViewCenterY")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Page.__mro__:
        if "ViewCenterY" in klass.__dict__:
            descriptor = klass.__dict__["ViewCenterY"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::page_has_viewScale():
    assert hasattr(DatadiagramMLTextFormat::Page, "viewScale")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Page.__mro__:
        if "viewScale" in klass.__dict__:
            descriptor = klass.__dict__["viewScale"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::page_has_background():
    assert hasattr(DatadiagramMLTextFormat::Page, "background")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Page.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat::stylesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::StyleSheet)


def test_datadiagrammltextformat::stylesheet_constructor_exists():
    assert callable(DatadiagramMLTextFormat::StyleSheet.__init__)


def test_datadiagrammltextformat::stylesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::mastershortcut_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::MasterShortCut)


def test_datadiagrammltextformat::mastershortcut_constructor_exists():
    assert callable(DatadiagramMLTextFormat::MasterShortCut.__init__)


def test_datadiagrammltextformat::mastershortcut_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::MasterShortCut.__init__)
    params = list(sig.parameters.keys())
    assert "shortcutURL" in params, "Missing parameter 'shortcutURL'"
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "shortcutHelp" in params, "Missing parameter 'shortcutHelp'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"

def test_datadiagrammltextformat::mastershortcut_has_shortcutURL():
    assert hasattr(DatadiagramMLTextFormat::MasterShortCut, "shortcutURL")
    descriptor = None
    for klass in DatadiagramMLTextFormat::MasterShortCut.__mro__:
        if "shortcutURL" in klass.__dict__:
            descriptor = klass.__dict__["shortcutURL"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::mastershortcut_has_prompt():
    assert hasattr(DatadiagramMLTextFormat::MasterShortCut, "prompt")
    descriptor = None
    for klass in DatadiagramMLTextFormat::MasterShortCut.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::mastershortcut_has_shortcutHelp():
    assert hasattr(DatadiagramMLTextFormat::MasterShortCut, "shortcutHelp")
    descriptor = None
    for klass in DatadiagramMLTextFormat::MasterShortCut.__mro__:
        if "shortcutHelp" in klass.__dict__:
            descriptor = klass.__dict__["shortcutHelp"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::mastershortcut_has_patternFlags():
    assert hasattr(DatadiagramMLTextFormat::MasterShortCut, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLTextFormat::MasterShortCut.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::mastershortcut_has_alignName():
    assert hasattr(DatadiagramMLTextFormat::MasterShortCut, "alignName")
    descriptor = None
    for klass in DatadiagramMLTextFormat::MasterShortCut.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::mastershortcut_has_iconSize():
    assert hasattr(DatadiagramMLTextFormat::MasterShortCut, "iconSize")
    descriptor = None
    for klass in DatadiagramMLTextFormat::MasterShortCut.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat::master_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Master)


def test_datadiagrammltextformat::master_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Master.__init__)


def test_datadiagrammltextformat::master_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Master.__init__)
    params = list(sig.parameters.keys())
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "baseID" in params, "Missing parameter 'baseID'"
    assert "matchByName" in params, "Missing parameter 'matchByName'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "iconUpdate" in params, "Missing parameter 'iconUpdate'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"

def test_datadiagrammltextformat::master_has_hidden():
    assert hasattr(DatadiagramMLTextFormat::Master, "hidden")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Master.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::master_has_baseID():
    assert hasattr(DatadiagramMLTextFormat::Master, "baseID")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Master.__mro__:
        if "baseID" in klass.__dict__:
            descriptor = klass.__dict__["baseID"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::master_has_matchByName():
    assert hasattr(DatadiagramMLTextFormat::Master, "matchByName")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Master.__mro__:
        if "matchByName" in klass.__dict__:
            descriptor = klass.__dict__["matchByName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::master_has_alignName():
    assert hasattr(DatadiagramMLTextFormat::Master, "alignName")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Master.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::master_has_prompt():
    assert hasattr(DatadiagramMLTextFormat::Master, "prompt")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Master.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::master_has_iconUpdate():
    assert hasattr(DatadiagramMLTextFormat::Master, "iconUpdate")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Master.__mro__:
        if "iconUpdate" in klass.__dict__:
            descriptor = klass.__dict__["iconUpdate"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::master_has_iconSize():
    assert hasattr(DatadiagramMLTextFormat::Master, "iconSize")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Master.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::master_has_patternFlags():
    assert hasattr(DatadiagramMLTextFormat::Master, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLTextFormat::Master.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat::facename_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::FaceName)


def test_datadiagrammltextformat::facename_constructor_exists():
    assert callable(DatadiagramMLTextFormat::FaceName.__init__)


def test_datadiagrammltextformat::facename_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::FaceName.__init__)
    params = list(sig.parameters.keys())
    assert "panos" in params, "Missing parameter 'panos'"
    assert "unicodeRanges" in params, "Missing parameter 'unicodeRanges'"
    assert "charSet" in params, "Missing parameter 'charSet'"
    assert "flags" in params, "Missing parameter 'flags'"
    assert "name" in params, "Missing parameter 'name'"

def test_datadiagrammltextformat::facename_has_panos():
    assert hasattr(DatadiagramMLTextFormat::FaceName, "panos")
    descriptor = None
    for klass in DatadiagramMLTextFormat::FaceName.__mro__:
        if "panos" in klass.__dict__:
            descriptor = klass.__dict__["panos"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::facename_has_unicodeRanges():
    assert hasattr(DatadiagramMLTextFormat::FaceName, "unicodeRanges")
    descriptor = None
    for klass in DatadiagramMLTextFormat::FaceName.__mro__:
        if "unicodeRanges" in klass.__dict__:
            descriptor = klass.__dict__["unicodeRanges"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::facename_has_charSet():
    assert hasattr(DatadiagramMLTextFormat::FaceName, "charSet")
    descriptor = None
    for klass in DatadiagramMLTextFormat::FaceName.__mro__:
        if "charSet" in klass.__dict__:
            descriptor = klass.__dict__["charSet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::facename_has_flags():
    assert hasattr(DatadiagramMLTextFormat::FaceName, "flags")
    descriptor = None
    for klass in DatadiagramMLTextFormat::FaceName.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::facename_has_name():
    assert hasattr(DatadiagramMLTextFormat::FaceName, "name")
    descriptor = None
    for klass in DatadiagramMLTextFormat::FaceName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_customproperty_is_not_abstract():
    assert not inspect.isabstract(CustomProperty)


def test_customproperty_constructor_exists():
    assert callable(CustomProperty.__init__)


def test_customproperty_constructor_args():
    sig = inspect.signature(CustomProperty.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::fontentry_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::FontEntry)


def test_datadiagrammltextformat::fontentry_constructor_exists():
    assert callable(DatadiagramMLTextFormat::FontEntry.__init__)


def test_datadiagrammltextformat::fontentry_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::FontEntry.__init__)
    params = list(sig.parameters.keys())
    assert "charSet" in params, "Missing parameter 'charSet'"
    assert "attributes" in params, "Missing parameter 'attributes'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "name" in params, "Missing parameter 'name'"
    assert "unicode" in params, "Missing parameter 'unicode'"
    assert "pitchAndFamily" in params, "Missing parameter 'pitchAndFamily'"

def test_datadiagrammltextformat::fontentry_has_charSet():
    assert hasattr(DatadiagramMLTextFormat::FontEntry, "charSet")
    descriptor = None
    for klass in DatadiagramMLTextFormat::FontEntry.__mro__:
        if "charSet" in klass.__dict__:
            descriptor = klass.__dict__["charSet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::fontentry_has_attributes():
    assert hasattr(DatadiagramMLTextFormat::FontEntry, "attributes")
    descriptor = None
    for klass in DatadiagramMLTextFormat::FontEntry.__mro__:
        if "attributes" in klass.__dict__:
            descriptor = klass.__dict__["attributes"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::fontentry_has_weight():
    assert hasattr(DatadiagramMLTextFormat::FontEntry, "weight")
    descriptor = None
    for klass in DatadiagramMLTextFormat::FontEntry.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::fontentry_has_name():
    assert hasattr(DatadiagramMLTextFormat::FontEntry, "name")
    descriptor = None
    for klass in DatadiagramMLTextFormat::FontEntry.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::fontentry_has_unicode():
    assert hasattr(DatadiagramMLTextFormat::FontEntry, "unicode")
    descriptor = None
    for klass in DatadiagramMLTextFormat::FontEntry.__mro__:
        if "unicode" in klass.__dict__:
            descriptor = klass.__dict__["unicode"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::fontentry_has_pitchAndFamily():
    assert hasattr(DatadiagramMLTextFormat::FontEntry, "pitchAndFamily")
    descriptor = None
    for klass in DatadiagramMLTextFormat::FontEntry.__mro__:
        if "pitchAndFamily" in klass.__dict__:
            descriptor = klass.__dict__["pitchAndFamily"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat::custompropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::CustomPropertiesCollection)


def test_datadiagrammltextformat::custompropertiescollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat::CustomPropertiesCollection.__init__)


def test_datadiagrammltextformat::custompropertiescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::CustomPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_ixrequiredelt_is_not_abstract():
    assert not inspect.isabstract(IXrequiredElt)


def test_ixrequiredelt_constructor_exists():
    assert callable(IXrequiredElt.__init__)


def test_ixrequiredelt_constructor_args():
    sig = inspect.signature(IXrequiredElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::tp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Tp)


def test_datadiagrammltextformat::tp_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Tp.__init__)


def test_datadiagrammltextformat::tp_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Tp.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::pp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Pp)


def test_datadiagrammltextformat::pp_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Pp.__init__)


def test_datadiagrammltextformat::pp_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Pp.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::fld_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Fld)


def test_datadiagrammltextformat::fld_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Fld.__init__)


def test_datadiagrammltextformat::fld_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Fld.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::cp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::Cp)


def test_datadiagrammltextformat::cp_constructor_exists():
    assert callable(DatadiagramMLTextFormat::Cp.__init__)


def test_datadiagrammltextformat::cp_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::Cp.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::colorentry_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::ColorEntry)


def test_datadiagrammltextformat::colorentry_constructor_exists():
    assert callable(DatadiagramMLTextFormat::ColorEntry.__init__)


def test_datadiagrammltextformat::colorentry_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::ColorEntry.__init__)
    params = list(sig.parameters.keys())
    assert "rgb" in params, "Missing parameter 'rgb'"

def test_datadiagrammltextformat::colorentry_has_rgb():
    assert hasattr(DatadiagramMLTextFormat::ColorEntry, "rgb")
    descriptor = None
    for klass in DatadiagramMLTextFormat::ColorEntry.__mro__:
        if "rgb" in klass.__dict__:
            descriptor = klass.__dict__["rgb"]
            break
    assert isinstance(descriptor, property)



def test_colorentry_is_not_abstract():
    assert not inspect.isabstract(ColorEntry)


def test_colorentry_constructor_exists():
    assert callable(ColorEntry.__init__)


def test_colorentry_constructor_args():
    sig = inspect.signature(ColorEntry.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::colorstable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::ColorsTable)


def test_datadiagrammltextformat::colorstable_constructor_exists():
    assert callable(DatadiagramMLTextFormat::ColorsTable.__init__)


def test_datadiagrammltextformat::colorstable_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::ColorsTable.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::customproperty_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::CustomProperty)


def test_datadiagrammltextformat::customproperty_constructor_exists():
    assert callable(DatadiagramMLTextFormat::CustomProperty.__init__)


def test_datadiagrammltextformat::customproperty_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::CustomProperty.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "name" in params, "Missing parameter 'name'"

def test_datadiagrammltextformat::customproperty_has_dataType():
    assert hasattr(DatadiagramMLTextFormat::CustomProperty, "dataType")
    descriptor = None
    for klass in DatadiagramMLTextFormat::CustomProperty.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::customproperty_has_name():
    assert hasattr(DatadiagramMLTextFormat::CustomProperty, "name")
    descriptor = None
    for klass in DatadiagramMLTextFormat::CustomProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_visiodocument_is_not_abstract():
    assert not inspect.isabstract(VisioDocument)


def test_visiodocument_constructor_exists():
    assert callable(VisioDocument.__init__)


def test_visiodocument_constructor_args():
    sig = inspect.signature(VisioDocument.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat::documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat::DocumentPropertiesCollection)


def test_datadiagrammltextformat::documentpropertiescollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat::DocumentPropertiesCollection.__init__)


def test_datadiagrammltextformat::documentpropertiescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat::DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"
    assert "alternateNames" in params, "Missing parameter 'alternateNames'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "buildNumberCreated" in params, "Missing parameter 'buildNumberCreated'"
    assert "buildNumberEdited" in params, "Missing parameter 'buildNumberEdited'"
    assert "title" in params, "Missing parameter 'title'"
    assert "category" in params, "Missing parameter 'category'"
    assert "creator" in params, "Missing parameter 'creator'"
    assert "hyperlinkBase_href" in params, "Missing parameter 'hyperlinkBase_href'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "company" in params, "Missing parameter 'company'"
    assert "template" in params, "Missing parameter 'template'"
    assert "description" in params, "Missing parameter 'description'"

def test_datadiagrammltextformat::documentpropertiescollection_has_subject():
    assert hasattr(DatadiagramMLTextFormat::DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::documentpropertiescollection_has_alternateNames():
    assert hasattr(DatadiagramMLTextFormat::DocumentPropertiesCollection, "alternateNames")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DocumentPropertiesCollection.__mro__:
        if "alternateNames" in klass.__dict__:
            descriptor = klass.__dict__["alternateNames"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::documentpropertiescollection_has_keywords():
    assert hasattr(DatadiagramMLTextFormat::DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::documentpropertiescollection_has_buildNumberCreated():
    assert hasattr(DatadiagramMLTextFormat::DocumentPropertiesCollection, "buildNumberCreated")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DocumentPropertiesCollection.__mro__:
        if "buildNumberCreated" in klass.__dict__:
            descriptor = klass.__dict__["buildNumberCreated"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::documentpropertiescollection_has_buildNumberEdited():
    assert hasattr(DatadiagramMLTextFormat::DocumentPropertiesCollection, "buildNumberEdited")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DocumentPropertiesCollection.__mro__:
        if "buildNumberEdited" in klass.__dict__:
            descriptor = klass.__dict__["buildNumberEdited"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::documentpropertiescollection_has_title():
    assert hasattr(DatadiagramMLTextFormat::DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::documentpropertiescollection_has_category():
    assert hasattr(DatadiagramMLTextFormat::DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::documentpropertiescollection_has_creator():
    assert hasattr(DatadiagramMLTextFormat::DocumentPropertiesCollection, "creator")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DocumentPropertiesCollection.__mro__:
        if "creator" in klass.__dict__:
            descriptor = klass.__dict__["creator"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::documentpropertiescollection_has_hyperlinkBase_href():
    assert hasattr(DatadiagramMLTextFormat::DocumentPropertiesCollection, "hyperlinkBase_href")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase_href" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase_href"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::documentpropertiescollection_has_manager():
    assert hasattr(DatadiagramMLTextFormat::DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::documentpropertiescollection_has_company():
    assert hasattr(DatadiagramMLTextFormat::DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::documentpropertiescollection_has_template():
    assert hasattr(DatadiagramMLTextFormat::DocumentPropertiesCollection, "template")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DocumentPropertiesCollection.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat::documentpropertiescollection_has_description():
    assert hasattr(DatadiagramMLTextFormat::DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in DatadiagramMLTextFormat::DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



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
DatadiagramMLTextFormat::SolutionXML_strategy = st.builds(
    DatadiagramMLTextFormat::SolutionXML,
)
DatadiagramMLTextFormat::HeaderFooter_strategy = st.builds(
    DatadiagramMLTextFormat::HeaderFooter,
)
DatadiagramMLTextFormat::EventList_strategy = st.builds(
    DatadiagramMLTextFormat::EventList,
)
DatadiagramMLTextFormat::WindowsInfo_strategy = st.builds(
    DatadiagramMLTextFormat::WindowsInfo,
)
DatadiagramMLTextFormat::DocumentSettingsElt_strategy = st.builds(
    DatadiagramMLTextFormat::DocumentSettingsElt,
)
DatadiagramMLTextFormat::PageElt_strategy = st.builds(
    DatadiagramMLTextFormat::PageElt,
)
DatadiagramMLTextFormat::PrintSetup_strategy = st.builds(
    DatadiagramMLTextFormat::PrintSetup,
)
DatadiagramMLTextFormat::PagesCollection_strategy = st.builds(
    DatadiagramMLTextFormat::PagesCollection,
)
DatadiagramMLTextFormat::MasterElt_strategy = st.builds(
    DatadiagramMLTextFormat::MasterElt,
)
ConnectsCollection_strategy = st.builds(
    ConnectsCollection,
)
DatadiagramMLTextFormat::Connect_strategy = st.builds(
    DatadiagramMLTextFormat::Connect,
    toCell=
        safe_text,
    fromPart=
        safe_text,
    toPart=
        safe_text,
    toSheet=
        safe_text,
    fromCell=
        safe_text,
    fromSheet=
        safe_text
)
Connect_strategy = st.builds(
    Connect,
)
Page_strategy = st.builds(
    Page,
)
Icon_strategy = st.builds(
    Icon,
)
MasterShortCut_strategy = st.builds(
    MasterShortCut,
)
Master_strategy = st.builds(
    Master,
)
DatadiagramMLTextFormat::MastersCollection_strategy = st.builds(
    DatadiagramMLTextFormat::MastersCollection,
)
TabsCollection_strategy = st.builds(
    TabsCollection,
)
Tab_strategy = st.builds(
    Tab,
)
DatadiagramMLTextFormat::IXrequiredElt_strategy = st.builds(
    DatadiagramMLTextFormat::IXrequiredElt,
    iX=
        safe_text
)
Text_strategy = st.builds(
    Text,
)
DatadiagramMLTextFormat::TextElt_strategy = st.builds(
    DatadiagramMLTextFormat::TextElt,
)
XYABCDElt_strategy = st.builds(
    XYABCDElt,
)
DatadiagramMLTextFormat::EllipticalArcTo_strategy = st.builds(
    DatadiagramMLTextFormat::EllipticalArcTo,
)
DatadiagramMLTextFormat::Ellipse_strategy = st.builds(
    DatadiagramMLTextFormat::Ellipse,
)
TextElt_strategy = st.builds(
    TextElt,
)
DatadiagramMLTextFormat::StringElt_strategy = st.builds(
    DatadiagramMLTextFormat::StringElt,
    value=
        safe_text
)
XYABCDEElt_strategy = st.builds(
    XYABCDEElt,
)
DatadiagramMLTextFormat::NURBSTo_strategy = st.builds(
    DatadiagramMLTextFormat::NURBSTo,
)
DatadiagramMLTextFormat::XYABCDEElt_strategy = st.builds(
    DatadiagramMLTextFormat::XYABCDEElt,
)
DatadiagramMLTextFormat::SplineStart_strategy = st.builds(
    DatadiagramMLTextFormat::SplineStart,
)
XYABElt_strategy = st.builds(
    XYABElt,
)
DatadiagramMLTextFormat::XYABCDElt_strategy = st.builds(
    DatadiagramMLTextFormat::XYABCDElt,
)
DatadiagramMLTextFormat::InfiniteLine_strategy = st.builds(
    DatadiagramMLTextFormat::InfiniteLine,
)
XYAElt_strategy = st.builds(
    XYAElt,
)
DatadiagramMLTextFormat::SplineKnot_strategy = st.builds(
    DatadiagramMLTextFormat::SplineKnot,
)
DatadiagramMLTextFormat::XYABElt_strategy = st.builds(
    DatadiagramMLTextFormat::XYABElt,
)
DatadiagramMLTextFormat::PolylineTo_strategy = st.builds(
    DatadiagramMLTextFormat::PolylineTo,
)
DatadiagramMLTextFormat::ArcTo_strategy = st.builds(
    DatadiagramMLTextFormat::ArcTo,
)
Geom_strategy = st.builds(
    Geom,
)
XYElt_strategy = st.builds(
    XYElt,
)
DatadiagramMLTextFormat::MoveTo_strategy = st.builds(
    DatadiagramMLTextFormat::MoveTo,
)
DatadiagramMLTextFormat::XYAElt_strategy = st.builds(
    DatadiagramMLTextFormat::XYAElt,
)
DatadiagramMLTextFormat::LineTo_strategy = st.builds(
    DatadiagramMLTextFormat::LineTo,
)
SplineKnot_strategy = st.builds(
    SplineKnot,
)
ArcTo_strategy = st.builds(
    ArcTo,
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
InfiniteLine_strategy = st.builds(
    InfiniteLine,
)
PolylineTo_strategy = st.builds(
    PolylineTo,
)
DatadiagramMLTextFormat::DelElt_strategy = st.builds(
    DatadiagramMLTextFormat::DelElt,
    del_=
        safe_text
)
DatadiagramMLTextFormat::IXElt_strategy = st.builds(
    DatadiagramMLTextFormat::IXElt,
    iX=
        safe_text
)
MoveTo_strategy = st.builds(
    MoveTo,
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
DatadiagramMLTextFormat::XYElt_strategy = st.builds(
    DatadiagramMLTextFormat::XYElt,
)
DatadiagramMLTextFormat::Tab_strategy = st.builds(
    DatadiagramMLTextFormat::Tab,
)
DatadiagramMLTextFormat::NamedElt_strategy = st.builds(
    DatadiagramMLTextFormat::NamedElt,
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
DatadiagramMLTextFormat::ConnectsCollection_strategy = st.builds(
    DatadiagramMLTextFormat::ConnectsCollection,
)
DatadiagramMLTextFormat::ShapesCollection_strategy = st.builds(
    DatadiagramMLTextFormat::ShapesCollection,
)
DatadiagramMLTextFormat::Icon_strategy = st.builds(
    DatadiagramMLTextFormat::Icon,
    value=
        safe_text
)
UniqueIdElt_strategy = st.builds(
    UniqueIdElt,
)
DatadiagramMLTextFormat::ShapeElt_strategy = st.builds(
    DatadiagramMLTextFormat::ShapeElt,
)
ShapeElt_strategy = st.builds(
    ShapeElt,
)
DatadiagramMLTextFormat::Field_strategy = st.builds(
    DatadiagramMLTextFormat::Field,
)
DatadiagramMLTextFormat::Para_strategy = st.builds(
    DatadiagramMLTextFormat::Para,
)
DatadiagramMLTextFormat::Text_strategy = st.builds(
    DatadiagramMLTextFormat::Text,
)
DatadiagramMLTextFormat::Geom_strategy = st.builds(
    DatadiagramMLTextFormat::Geom,
)
DatadiagramMLTextFormat::Char_strategy = st.builds(
    DatadiagramMLTextFormat::Char,
)
DatadiagramMLTextFormat::TabsCollection_strategy = st.builds(
    DatadiagramMLTextFormat::TabsCollection,
)
ShapesCollection_strategy = st.builds(
    ShapesCollection,
)
DatadiagramMLTextFormat::Shape_strategy = st.builds(
    DatadiagramMLTextFormat::Shape,
    textStyle=
        safe_text,
    lineStyle=
        safe_text,
    fillStyle=
        safe_text
)
DatadiagramMLTextFormat::UniqueIdElt_strategy = st.builds(
    DatadiagramMLTextFormat::UniqueIdElt,
    UniqueID=
        safe_text
)
DatadiagramMLTextFormat::IdentifiedElt_strategy = st.builds(
    DatadiagramMLTextFormat::IdentifiedElt,
    ID=
        safe_text
)
DatadiagramMLTextFormat::VBProjectData_strategy = st.builds(
    DatadiagramMLTextFormat::VBProjectData,
    data=
        safe_text
)
PageSheet_strategy = st.builds(
    PageSheet,
)
NamedElt_strategy = st.builds(
    NamedElt,
)
DatadiagramMLTextFormat::DocumentSheet_strategy = st.builds(
    DatadiagramMLTextFormat::DocumentSheet,
)
Shape_strategy = st.builds(
    Shape,
)
DatadiagramMLTextFormat::PageSheet_strategy = st.builds(
    DatadiagramMLTextFormat::PageSheet,
)
PagesCollection_strategy = st.builds(
    PagesCollection,
)
MastersCollection_strategy = st.builds(
    MastersCollection,
)
DocumentSheet_strategy = st.builds(
    DocumentSheet,
)
DatadiagramMLTextFormat::DateTimeType_strategy = st.builds(
    DatadiagramMLTextFormat::DateTimeType,
    hour=
        safe_text,
    year=
        safe_text,
    second=
        safe_text,
    minute=
        safe_text,
    day=
        safe_text,
    month=
        safe_text
)
DocumentSettingsElt_strategy = st.builds(
    DocumentSettingsElt,
)
DocumentPropertiesCollection_strategy = st.builds(
    DocumentPropertiesCollection,
)
DatadiagramMLTextFormat::VisioDocument_strategy = st.builds(
    DatadiagramMLTextFormat::VisioDocument,
    start=
        safe_text,
    key=
        safe_text,
    version=
        safe_text,
    buildnum=
        safe_text,
    docLangId=
        safe_text,
    metric=
        safe_text
)
DatadiagramMLTextFormat::CellType_strategy = st.builds(
    DatadiagramMLTextFormat::CellType,
    unit=
        safe_text,
    formula=
        safe_text,
    err=
        safe_text,
    value=
        safe_text
)
StyleSheet_strategy = st.builds(
    StyleSheet,
)
DatadiagramMLTextFormat::StyleSheetsCollection_strategy = st.builds(
    DatadiagramMLTextFormat::StyleSheetsCollection,
)
DatadiagramMLTextFormat::EmailRoutingData_strategy = st.builds(
    DatadiagramMLTextFormat::EmailRoutingData,
    size=
        safe_text,
    data=
        safe_text
)
FontEntry_strategy = st.builds(
    FontEntry,
)
DatadiagramMLTextFormat::FontsTable_strategy = st.builds(
    DatadiagramMLTextFormat::FontsTable,
)
FaceName_strategy = st.builds(
    FaceName,
)
DatadiagramMLTextFormat::FaceNamesTable_strategy = st.builds(
    DatadiagramMLTextFormat::FaceNamesTable,
)
IdentifiedElt_strategy = st.builds(
    IdentifiedElt,
)
DatadiagramMLTextFormat::Page_strategy = st.builds(
    DatadiagramMLTextFormat::Page,
    backPage=
        safe_text,
    reviewerID=
        safe_text,
    associatedPage=
        safe_text,
    viewCenterX=
        safe_text,
    ViewCenterY=
        safe_text,
    viewScale=
        safe_text,
    background=
        safe_text
)
DatadiagramMLTextFormat::StyleSheet_strategy = st.builds(
    DatadiagramMLTextFormat::StyleSheet,
)
DatadiagramMLTextFormat::MasterShortCut_strategy = st.builds(
    DatadiagramMLTextFormat::MasterShortCut,
    shortcutURL=
        safe_text,
    prompt=
        safe_text,
    shortcutHelp=
        safe_text,
    patternFlags=
        safe_text,
    alignName=
        safe_text,
    iconSize=
        safe_text
)
DatadiagramMLTextFormat::Master_strategy = st.builds(
    DatadiagramMLTextFormat::Master,
    hidden=
        safe_text,
    baseID=
        safe_text,
    matchByName=
        safe_text,
    alignName=
        safe_text,
    prompt=
        safe_text,
    iconUpdate=
        safe_text,
    iconSize=
        safe_text,
    patternFlags=
        safe_text
)
DatadiagramMLTextFormat::FaceName_strategy = st.builds(
    DatadiagramMLTextFormat::FaceName,
    panos=
        safe_text,
    unicodeRanges=
        safe_text,
    charSet=
        safe_text,
    flags=
        safe_text,
    name=
        safe_text
)
CustomProperty_strategy = st.builds(
    CustomProperty,
)
DatadiagramMLTextFormat::FontEntry_strategy = st.builds(
    DatadiagramMLTextFormat::FontEntry,
    charSet=
        safe_text,
    attributes=
        safe_text,
    weight=
        safe_text,
    name=
        safe_text,
    unicode=
        safe_text,
    pitchAndFamily=
        safe_text
)
DatadiagramMLTextFormat::CustomPropertiesCollection_strategy = st.builds(
    DatadiagramMLTextFormat::CustomPropertiesCollection,
)
IXrequiredElt_strategy = st.builds(
    IXrequiredElt,
)
DatadiagramMLTextFormat::Tp_strategy = st.builds(
    DatadiagramMLTextFormat::Tp,
)
DatadiagramMLTextFormat::Pp_strategy = st.builds(
    DatadiagramMLTextFormat::Pp,
)
DatadiagramMLTextFormat::Fld_strategy = st.builds(
    DatadiagramMLTextFormat::Fld,
)
DatadiagramMLTextFormat::Cp_strategy = st.builds(
    DatadiagramMLTextFormat::Cp,
)
DatadiagramMLTextFormat::ColorEntry_strategy = st.builds(
    DatadiagramMLTextFormat::ColorEntry,
    rgb=
        safe_text
)
ColorEntry_strategy = st.builds(
    ColorEntry,
)
DatadiagramMLTextFormat::ColorsTable_strategy = st.builds(
    DatadiagramMLTextFormat::ColorsTable,
)
DatadiagramMLTextFormat::CustomProperty_strategy = st.builds(
    DatadiagramMLTextFormat::CustomProperty,
    dataType=
        safe_text,
    name=
        safe_text
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
CustomPropertiesCollection_strategy = st.builds(
    CustomPropertiesCollection,
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
VisioDocument_strategy = st.builds(
    VisioDocument,
)
DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy = st.builds(
    DatadiagramMLTextFormat::DocumentPropertiesCollection,
    subject=
        safe_text,
    alternateNames=
        safe_text,
    keywords=
        safe_text,
    buildNumberCreated=
        safe_text,
    buildNumberEdited=
        safe_text,
    title=
        safe_text,
    category=
        safe_text,
    creator=
        safe_text,
    hyperlinkBase_href=
        safe_text,
    manager=
        safe_text,
    company=
        safe_text,
    template=
        safe_text,
    description=
        safe_text
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

@given(instance=DatadiagramMLTextFormat::SolutionXML_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::solutionxml_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::SolutionXML)

@given(instance=DatadiagramMLTextFormat::HeaderFooter_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::headerfooter_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::HeaderFooter)

@given(instance=DatadiagramMLTextFormat::EventList_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::eventlist_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::EventList)

@given(instance=DatadiagramMLTextFormat::WindowsInfo_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::windowsinfo_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::WindowsInfo)

@given(instance=DatadiagramMLTextFormat::DocumentSettingsElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::documentsettingselt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::DocumentSettingsElt)

@given(instance=DatadiagramMLTextFormat::PageElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::pageelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::PageElt)

@given(instance=DatadiagramMLTextFormat::PrintSetup_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::printsetup_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::PrintSetup)

@given(instance=DatadiagramMLTextFormat::PagesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::pagescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::PagesCollection)

@given(instance=DatadiagramMLTextFormat::MasterElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::masterelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::MasterElt)

@given(instance=ConnectsCollection_strategy)
@settings(max_examples=50)
def test_connectscollection_instantiation(instance):
    assert isinstance(instance, ConnectsCollection)

@given(instance=DatadiagramMLTextFormat::Connect_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::connect_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Connect)

@given(instance=DatadiagramMLTextFormat::Connect_strategy)
def test_datadiagrammltextformat::connect_toCell_type(instance):
    assert isinstance(instance.toCell, str)


@given(instance=DatadiagramMLTextFormat::Connect_strategy)
def test_datadiagrammltextformat::connect_toCell_setter(instance):
    original = instance.toCell
    instance.toCell = original
    assert instance.toCell == original

@given(instance=DatadiagramMLTextFormat::Connect_strategy)
def test_datadiagrammltextformat::connect_fromPart_type(instance):
    assert isinstance(instance.fromPart, str)


@given(instance=DatadiagramMLTextFormat::Connect_strategy)
def test_datadiagrammltextformat::connect_fromPart_setter(instance):
    original = instance.fromPart
    instance.fromPart = original
    assert instance.fromPart == original

@given(instance=DatadiagramMLTextFormat::Connect_strategy)
def test_datadiagrammltextformat::connect_toPart_type(instance):
    assert isinstance(instance.toPart, str)


@given(instance=DatadiagramMLTextFormat::Connect_strategy)
def test_datadiagrammltextformat::connect_toPart_setter(instance):
    original = instance.toPart
    instance.toPart = original
    assert instance.toPart == original

@given(instance=DatadiagramMLTextFormat::Connect_strategy)
def test_datadiagrammltextformat::connect_toSheet_type(instance):
    assert isinstance(instance.toSheet, str)


@given(instance=DatadiagramMLTextFormat::Connect_strategy)
def test_datadiagrammltextformat::connect_toSheet_setter(instance):
    original = instance.toSheet
    instance.toSheet = original
    assert instance.toSheet == original

@given(instance=DatadiagramMLTextFormat::Connect_strategy)
def test_datadiagrammltextformat::connect_fromCell_type(instance):
    assert isinstance(instance.fromCell, str)


@given(instance=DatadiagramMLTextFormat::Connect_strategy)
def test_datadiagrammltextformat::connect_fromCell_setter(instance):
    original = instance.fromCell
    instance.fromCell = original
    assert instance.fromCell == original

@given(instance=DatadiagramMLTextFormat::Connect_strategy)
def test_datadiagrammltextformat::connect_fromSheet_type(instance):
    assert isinstance(instance.fromSheet, str)


@given(instance=DatadiagramMLTextFormat::Connect_strategy)
def test_datadiagrammltextformat::connect_fromSheet_setter(instance):
    original = instance.fromSheet
    instance.fromSheet = original
    assert instance.fromSheet == original

@given(instance=Connect_strategy)
@settings(max_examples=50)
def test_connect_instantiation(instance):
    assert isinstance(instance, Connect)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=Icon_strategy)
@settings(max_examples=50)
def test_icon_instantiation(instance):
    assert isinstance(instance, Icon)

@given(instance=MasterShortCut_strategy)
@settings(max_examples=50)
def test_mastershortcut_instantiation(instance):
    assert isinstance(instance, MasterShortCut)

@given(instance=Master_strategy)
@settings(max_examples=50)
def test_master_instantiation(instance):
    assert isinstance(instance, Master)

@given(instance=DatadiagramMLTextFormat::MastersCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::masterscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::MastersCollection)

@given(instance=TabsCollection_strategy)
@settings(max_examples=50)
def test_tabscollection_instantiation(instance):
    assert isinstance(instance, TabsCollection)

@given(instance=Tab_strategy)
@settings(max_examples=50)
def test_tab_instantiation(instance):
    assert isinstance(instance, Tab)

@given(instance=DatadiagramMLTextFormat::IXrequiredElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::ixrequiredelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::IXrequiredElt)

@given(instance=DatadiagramMLTextFormat::IXrequiredElt_strategy)
def test_datadiagrammltextformat::ixrequiredelt_iX_type(instance):
    assert isinstance(instance.iX, str)


@given(instance=DatadiagramMLTextFormat::IXrequiredElt_strategy)
def test_datadiagrammltextformat::ixrequiredelt_iX_setter(instance):
    original = instance.iX
    instance.iX = original
    assert instance.iX == original

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=DatadiagramMLTextFormat::TextElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::textelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::TextElt)

@given(instance=XYABCDElt_strategy)
@settings(max_examples=50)
def test_xyabcdelt_instantiation(instance):
    assert isinstance(instance, XYABCDElt)

@given(instance=DatadiagramMLTextFormat::EllipticalArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::ellipticalarcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::EllipticalArcTo)

@given(instance=DatadiagramMLTextFormat::Ellipse_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::ellipse_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Ellipse)

@given(instance=TextElt_strategy)
@settings(max_examples=50)
def test_textelt_instantiation(instance):
    assert isinstance(instance, TextElt)

@given(instance=DatadiagramMLTextFormat::StringElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::stringelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::StringElt)

@given(instance=DatadiagramMLTextFormat::StringElt_strategy)
def test_datadiagrammltextformat::stringelt_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DatadiagramMLTextFormat::StringElt_strategy)
def test_datadiagrammltextformat::stringelt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=XYABCDEElt_strategy)
@settings(max_examples=50)
def test_xyabcdeelt_instantiation(instance):
    assert isinstance(instance, XYABCDEElt)

@given(instance=DatadiagramMLTextFormat::NURBSTo_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::nurbsto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::NURBSTo)

@given(instance=DatadiagramMLTextFormat::XYABCDEElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::xyabcdeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::XYABCDEElt)

@given(instance=DatadiagramMLTextFormat::SplineStart_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::splinestart_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::SplineStart)

@given(instance=XYABElt_strategy)
@settings(max_examples=50)
def test_xyabelt_instantiation(instance):
    assert isinstance(instance, XYABElt)

@given(instance=DatadiagramMLTextFormat::XYABCDElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::xyabcdelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::XYABCDElt)

@given(instance=DatadiagramMLTextFormat::InfiniteLine_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::infiniteline_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::InfiniteLine)

@given(instance=XYAElt_strategy)
@settings(max_examples=50)
def test_xyaelt_instantiation(instance):
    assert isinstance(instance, XYAElt)

@given(instance=DatadiagramMLTextFormat::SplineKnot_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::splineknot_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::SplineKnot)

@given(instance=DatadiagramMLTextFormat::XYABElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::xyabelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::XYABElt)

@given(instance=DatadiagramMLTextFormat::PolylineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::polylineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::PolylineTo)

@given(instance=DatadiagramMLTextFormat::ArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::arcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::ArcTo)

@given(instance=Geom_strategy)
@settings(max_examples=50)
def test_geom_instantiation(instance):
    assert isinstance(instance, Geom)

@given(instance=XYElt_strategy)
@settings(max_examples=50)
def test_xyelt_instantiation(instance):
    assert isinstance(instance, XYElt)

@given(instance=DatadiagramMLTextFormat::MoveTo_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::moveto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::MoveTo)

@given(instance=DatadiagramMLTextFormat::XYAElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::xyaelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::XYAElt)

@given(instance=DatadiagramMLTextFormat::LineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::lineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::LineTo)

@given(instance=SplineKnot_strategy)
@settings(max_examples=50)
def test_splineknot_instantiation(instance):
    assert isinstance(instance, SplineKnot)

@given(instance=ArcTo_strategy)
@settings(max_examples=50)
def test_arcto_instantiation(instance):
    assert isinstance(instance, ArcTo)

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

@given(instance=InfiniteLine_strategy)
@settings(max_examples=50)
def test_infiniteline_instantiation(instance):
    assert isinstance(instance, InfiniteLine)

@given(instance=PolylineTo_strategy)
@settings(max_examples=50)
def test_polylineto_instantiation(instance):
    assert isinstance(instance, PolylineTo)

@given(instance=DatadiagramMLTextFormat::DelElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::delelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::DelElt)

@given(instance=DatadiagramMLTextFormat::DelElt_strategy)
def test_datadiagrammltextformat::delelt_del__type(instance):
    assert isinstance(instance.del_, str)


@given(instance=DatadiagramMLTextFormat::DelElt_strategy)
def test_datadiagrammltextformat::delelt_del__setter(instance):
    original = instance.del_
    instance.del_ = original
    assert instance.del_ == original

@given(instance=DatadiagramMLTextFormat::IXElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::ixelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::IXElt)

@given(instance=DatadiagramMLTextFormat::IXElt_strategy)
def test_datadiagrammltextformat::ixelt_iX_type(instance):
    assert isinstance(instance.iX, str)


@given(instance=DatadiagramMLTextFormat::IXElt_strategy)
def test_datadiagrammltextformat::ixelt_iX_setter(instance):
    original = instance.iX
    instance.iX = original
    assert instance.iX == original

@given(instance=MoveTo_strategy)
@settings(max_examples=50)
def test_moveto_instantiation(instance):
    assert isinstance(instance, MoveTo)

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

@given(instance=DatadiagramMLTextFormat::XYElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::xyelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::XYElt)

@given(instance=DatadiagramMLTextFormat::Tab_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::tab_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Tab)

@given(instance=DatadiagramMLTextFormat::NamedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::namedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::NamedElt)

@given(instance=DatadiagramMLTextFormat::NamedElt_strategy)
def test_datadiagrammltextformat::namedelt_nameU_type(instance):
    assert isinstance(instance.nameU, str)


@given(instance=DatadiagramMLTextFormat::NamedElt_strategy)
def test_datadiagrammltextformat::namedelt_nameU_setter(instance):
    original = instance.nameU
    instance.nameU = original
    assert instance.nameU == original

@given(instance=DatadiagramMLTextFormat::NamedElt_strategy)
def test_datadiagrammltextformat::namedelt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DatadiagramMLTextFormat::NamedElt_strategy)
def test_datadiagrammltextformat::namedelt_name_setter(instance):
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

@given(instance=DatadiagramMLTextFormat::ConnectsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::connectscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::ConnectsCollection)

@given(instance=DatadiagramMLTextFormat::ShapesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::shapescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::ShapesCollection)

@given(instance=DatadiagramMLTextFormat::Icon_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::icon_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Icon)

@given(instance=DatadiagramMLTextFormat::Icon_strategy)
def test_datadiagrammltextformat::icon_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DatadiagramMLTextFormat::Icon_strategy)
def test_datadiagrammltextformat::icon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UniqueIdElt_strategy)
@settings(max_examples=50)
def test_uniqueidelt_instantiation(instance):
    assert isinstance(instance, UniqueIdElt)

@given(instance=DatadiagramMLTextFormat::ShapeElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::shapeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::ShapeElt)

@given(instance=ShapeElt_strategy)
@settings(max_examples=50)
def test_shapeelt_instantiation(instance):
    assert isinstance(instance, ShapeElt)

@given(instance=DatadiagramMLTextFormat::Field_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::field_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Field)

@given(instance=DatadiagramMLTextFormat::Para_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::para_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Para)

@given(instance=DatadiagramMLTextFormat::Text_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::text_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Text)

@given(instance=DatadiagramMLTextFormat::Geom_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::geom_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Geom)

@given(instance=DatadiagramMLTextFormat::Char_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::char_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Char)

@given(instance=DatadiagramMLTextFormat::TabsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::tabscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::TabsCollection)

@given(instance=ShapesCollection_strategy)
@settings(max_examples=50)
def test_shapescollection_instantiation(instance):
    assert isinstance(instance, ShapesCollection)

@given(instance=DatadiagramMLTextFormat::Shape_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::shape_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Shape)

@given(instance=DatadiagramMLTextFormat::Shape_strategy)
def test_datadiagrammltextformat::shape_textStyle_type(instance):
    assert isinstance(instance.textStyle, str)


@given(instance=DatadiagramMLTextFormat::Shape_strategy)
def test_datadiagrammltextformat::shape_textStyle_setter(instance):
    original = instance.textStyle
    instance.textStyle = original
    assert instance.textStyle == original

@given(instance=DatadiagramMLTextFormat::Shape_strategy)
def test_datadiagrammltextformat::shape_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=DatadiagramMLTextFormat::Shape_strategy)
def test_datadiagrammltextformat::shape_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=DatadiagramMLTextFormat::Shape_strategy)
def test_datadiagrammltextformat::shape_fillStyle_type(instance):
    assert isinstance(instance.fillStyle, str)


@given(instance=DatadiagramMLTextFormat::Shape_strategy)
def test_datadiagrammltextformat::shape_fillStyle_setter(instance):
    original = instance.fillStyle
    instance.fillStyle = original
    assert instance.fillStyle == original

@given(instance=DatadiagramMLTextFormat::UniqueIdElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::uniqueidelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::UniqueIdElt)

@given(instance=DatadiagramMLTextFormat::UniqueIdElt_strategy)
def test_datadiagrammltextformat::uniqueidelt_UniqueID_type(instance):
    assert isinstance(instance.UniqueID, str)


@given(instance=DatadiagramMLTextFormat::UniqueIdElt_strategy)
def test_datadiagrammltextformat::uniqueidelt_UniqueID_setter(instance):
    original = instance.UniqueID
    instance.UniqueID = original
    assert instance.UniqueID == original

@given(instance=DatadiagramMLTextFormat::IdentifiedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::identifiedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::IdentifiedElt)

@given(instance=DatadiagramMLTextFormat::IdentifiedElt_strategy)
def test_datadiagrammltextformat::identifiedelt_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=DatadiagramMLTextFormat::IdentifiedElt_strategy)
def test_datadiagrammltextformat::identifiedelt_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=DatadiagramMLTextFormat::VBProjectData_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::vbprojectdata_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::VBProjectData)

@given(instance=DatadiagramMLTextFormat::VBProjectData_strategy)
def test_datadiagrammltextformat::vbprojectdata_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=DatadiagramMLTextFormat::VBProjectData_strategy)
def test_datadiagrammltextformat::vbprojectdata_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=PageSheet_strategy)
@settings(max_examples=50)
def test_pagesheet_instantiation(instance):
    assert isinstance(instance, PageSheet)

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=DatadiagramMLTextFormat::DocumentSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::documentsheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::DocumentSheet)

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=DatadiagramMLTextFormat::PageSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::pagesheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::PageSheet)

@given(instance=PagesCollection_strategy)
@settings(max_examples=50)
def test_pagescollection_instantiation(instance):
    assert isinstance(instance, PagesCollection)

@given(instance=MastersCollection_strategy)
@settings(max_examples=50)
def test_masterscollection_instantiation(instance):
    assert isinstance(instance, MastersCollection)

@given(instance=DocumentSheet_strategy)
@settings(max_examples=50)
def test_documentsheet_instantiation(instance):
    assert isinstance(instance, DocumentSheet)

@given(instance=DatadiagramMLTextFormat::DateTimeType_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::datetimetype_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::DateTimeType)

@given(instance=DatadiagramMLTextFormat::DateTimeType_strategy)
def test_datadiagrammltextformat::datetimetype_hour_type(instance):
    assert isinstance(instance.hour, str)


@given(instance=DatadiagramMLTextFormat::DateTimeType_strategy)
def test_datadiagrammltextformat::datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=DatadiagramMLTextFormat::DateTimeType_strategy)
def test_datadiagrammltextformat::datetimetype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=DatadiagramMLTextFormat::DateTimeType_strategy)
def test_datadiagrammltextformat::datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=DatadiagramMLTextFormat::DateTimeType_strategy)
def test_datadiagrammltextformat::datetimetype_second_type(instance):
    assert isinstance(instance.second, str)


@given(instance=DatadiagramMLTextFormat::DateTimeType_strategy)
def test_datadiagrammltextformat::datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=DatadiagramMLTextFormat::DateTimeType_strategy)
def test_datadiagrammltextformat::datetimetype_minute_type(instance):
    assert isinstance(instance.minute, str)


@given(instance=DatadiagramMLTextFormat::DateTimeType_strategy)
def test_datadiagrammltextformat::datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original

@given(instance=DatadiagramMLTextFormat::DateTimeType_strategy)
def test_datadiagrammltextformat::datetimetype_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=DatadiagramMLTextFormat::DateTimeType_strategy)
def test_datadiagrammltextformat::datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=DatadiagramMLTextFormat::DateTimeType_strategy)
def test_datadiagrammltextformat::datetimetype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=DatadiagramMLTextFormat::DateTimeType_strategy)
def test_datadiagrammltextformat::datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=DocumentSettingsElt_strategy)
@settings(max_examples=50)
def test_documentsettingselt_instantiation(instance):
    assert isinstance(instance, DocumentSettingsElt)

@given(instance=DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DocumentPropertiesCollection)

@given(instance=DatadiagramMLTextFormat::VisioDocument_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::visiodocument_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::VisioDocument)

@given(instance=DatadiagramMLTextFormat::VisioDocument_strategy)
def test_datadiagrammltextformat::visiodocument_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=DatadiagramMLTextFormat::VisioDocument_strategy)
def test_datadiagrammltextformat::visiodocument_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=DatadiagramMLTextFormat::VisioDocument_strategy)
def test_datadiagrammltextformat::visiodocument_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=DatadiagramMLTextFormat::VisioDocument_strategy)
def test_datadiagrammltextformat::visiodocument_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=DatadiagramMLTextFormat::VisioDocument_strategy)
def test_datadiagrammltextformat::visiodocument_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=DatadiagramMLTextFormat::VisioDocument_strategy)
def test_datadiagrammltextformat::visiodocument_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=DatadiagramMLTextFormat::VisioDocument_strategy)
def test_datadiagrammltextformat::visiodocument_buildnum_type(instance):
    assert isinstance(instance.buildnum, str)


@given(instance=DatadiagramMLTextFormat::VisioDocument_strategy)
def test_datadiagrammltextformat::visiodocument_buildnum_setter(instance):
    original = instance.buildnum
    instance.buildnum = original
    assert instance.buildnum == original

@given(instance=DatadiagramMLTextFormat::VisioDocument_strategy)
def test_datadiagrammltextformat::visiodocument_docLangId_type(instance):
    assert isinstance(instance.docLangId, str)


@given(instance=DatadiagramMLTextFormat::VisioDocument_strategy)
def test_datadiagrammltextformat::visiodocument_docLangId_setter(instance):
    original = instance.docLangId
    instance.docLangId = original
    assert instance.docLangId == original

@given(instance=DatadiagramMLTextFormat::VisioDocument_strategy)
def test_datadiagrammltextformat::visiodocument_metric_type(instance):
    assert isinstance(instance.metric, str)


@given(instance=DatadiagramMLTextFormat::VisioDocument_strategy)
def test_datadiagrammltextformat::visiodocument_metric_setter(instance):
    original = instance.metric
    instance.metric = original
    assert instance.metric == original

@given(instance=DatadiagramMLTextFormat::CellType_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::celltype_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::CellType)

@given(instance=DatadiagramMLTextFormat::CellType_strategy)
def test_datadiagrammltextformat::celltype_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=DatadiagramMLTextFormat::CellType_strategy)
def test_datadiagrammltextformat::celltype_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=DatadiagramMLTextFormat::CellType_strategy)
def test_datadiagrammltextformat::celltype_formula_type(instance):
    assert isinstance(instance.formula, str)


@given(instance=DatadiagramMLTextFormat::CellType_strategy)
def test_datadiagrammltextformat::celltype_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=DatadiagramMLTextFormat::CellType_strategy)
def test_datadiagrammltextformat::celltype_err_type(instance):
    assert isinstance(instance.err, str)


@given(instance=DatadiagramMLTextFormat::CellType_strategy)
def test_datadiagrammltextformat::celltype_err_setter(instance):
    original = instance.err
    instance.err = original
    assert instance.err == original

@given(instance=DatadiagramMLTextFormat::CellType_strategy)
def test_datadiagrammltextformat::celltype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DatadiagramMLTextFormat::CellType_strategy)
def test_datadiagrammltextformat::celltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=StyleSheet_strategy)
@settings(max_examples=50)
def test_stylesheet_instantiation(instance):
    assert isinstance(instance, StyleSheet)

@given(instance=DatadiagramMLTextFormat::StyleSheetsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::stylesheetscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::StyleSheetsCollection)

@given(instance=DatadiagramMLTextFormat::EmailRoutingData_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::emailroutingdata_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::EmailRoutingData)

@given(instance=DatadiagramMLTextFormat::EmailRoutingData_strategy)
def test_datadiagrammltextformat::emailroutingdata_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=DatadiagramMLTextFormat::EmailRoutingData_strategy)
def test_datadiagrammltextformat::emailroutingdata_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=DatadiagramMLTextFormat::EmailRoutingData_strategy)
def test_datadiagrammltextformat::emailroutingdata_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=DatadiagramMLTextFormat::EmailRoutingData_strategy)
def test_datadiagrammltextformat::emailroutingdata_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=FontEntry_strategy)
@settings(max_examples=50)
def test_fontentry_instantiation(instance):
    assert isinstance(instance, FontEntry)

@given(instance=DatadiagramMLTextFormat::FontsTable_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::fontstable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::FontsTable)

@given(instance=FaceName_strategy)
@settings(max_examples=50)
def test_facename_instantiation(instance):
    assert isinstance(instance, FaceName)

@given(instance=DatadiagramMLTextFormat::FaceNamesTable_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::facenamestable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::FaceNamesTable)

@given(instance=IdentifiedElt_strategy)
@settings(max_examples=50)
def test_identifiedelt_instantiation(instance):
    assert isinstance(instance, IdentifiedElt)

@given(instance=DatadiagramMLTextFormat::Page_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::page_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Page)

@given(instance=DatadiagramMLTextFormat::Page_strategy)
def test_datadiagrammltextformat::page_backPage_type(instance):
    assert isinstance(instance.backPage, str)


@given(instance=DatadiagramMLTextFormat::Page_strategy)
def test_datadiagrammltextformat::page_backPage_setter(instance):
    original = instance.backPage
    instance.backPage = original
    assert instance.backPage == original

@given(instance=DatadiagramMLTextFormat::Page_strategy)
def test_datadiagrammltextformat::page_reviewerID_type(instance):
    assert isinstance(instance.reviewerID, str)


@given(instance=DatadiagramMLTextFormat::Page_strategy)
def test_datadiagrammltextformat::page_reviewerID_setter(instance):
    original = instance.reviewerID
    instance.reviewerID = original
    assert instance.reviewerID == original

@given(instance=DatadiagramMLTextFormat::Page_strategy)
def test_datadiagrammltextformat::page_associatedPage_type(instance):
    assert isinstance(instance.associatedPage, str)


@given(instance=DatadiagramMLTextFormat::Page_strategy)
def test_datadiagrammltextformat::page_associatedPage_setter(instance):
    original = instance.associatedPage
    instance.associatedPage = original
    assert instance.associatedPage == original

@given(instance=DatadiagramMLTextFormat::Page_strategy)
def test_datadiagrammltextformat::page_viewCenterX_type(instance):
    assert isinstance(instance.viewCenterX, str)


@given(instance=DatadiagramMLTextFormat::Page_strategy)
def test_datadiagrammltextformat::page_viewCenterX_setter(instance):
    original = instance.viewCenterX
    instance.viewCenterX = original
    assert instance.viewCenterX == original

@given(instance=DatadiagramMLTextFormat::Page_strategy)
def test_datadiagrammltextformat::page_ViewCenterY_type(instance):
    assert isinstance(instance.ViewCenterY, str)


@given(instance=DatadiagramMLTextFormat::Page_strategy)
def test_datadiagrammltextformat::page_ViewCenterY_setter(instance):
    original = instance.ViewCenterY
    instance.ViewCenterY = original
    assert instance.ViewCenterY == original

@given(instance=DatadiagramMLTextFormat::Page_strategy)
def test_datadiagrammltextformat::page_viewScale_type(instance):
    assert isinstance(instance.viewScale, str)


@given(instance=DatadiagramMLTextFormat::Page_strategy)
def test_datadiagrammltextformat::page_viewScale_setter(instance):
    original = instance.viewScale
    instance.viewScale = original
    assert instance.viewScale == original

@given(instance=DatadiagramMLTextFormat::Page_strategy)
def test_datadiagrammltextformat::page_background_type(instance):
    assert isinstance(instance.background, str)


@given(instance=DatadiagramMLTextFormat::Page_strategy)
def test_datadiagrammltextformat::page_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original

@given(instance=DatadiagramMLTextFormat::StyleSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::stylesheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::StyleSheet)

@given(instance=DatadiagramMLTextFormat::MasterShortCut_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::mastershortcut_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::MasterShortCut)

@given(instance=DatadiagramMLTextFormat::MasterShortCut_strategy)
def test_datadiagrammltextformat::mastershortcut_shortcutURL_type(instance):
    assert isinstance(instance.shortcutURL, str)


@given(instance=DatadiagramMLTextFormat::MasterShortCut_strategy)
def test_datadiagrammltextformat::mastershortcut_shortcutURL_setter(instance):
    original = instance.shortcutURL
    instance.shortcutURL = original
    assert instance.shortcutURL == original

@given(instance=DatadiagramMLTextFormat::MasterShortCut_strategy)
def test_datadiagrammltextformat::mastershortcut_prompt_type(instance):
    assert isinstance(instance.prompt, str)


@given(instance=DatadiagramMLTextFormat::MasterShortCut_strategy)
def test_datadiagrammltextformat::mastershortcut_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original

@given(instance=DatadiagramMLTextFormat::MasterShortCut_strategy)
def test_datadiagrammltextformat::mastershortcut_shortcutHelp_type(instance):
    assert isinstance(instance.shortcutHelp, str)


@given(instance=DatadiagramMLTextFormat::MasterShortCut_strategy)
def test_datadiagrammltextformat::mastershortcut_shortcutHelp_setter(instance):
    original = instance.shortcutHelp
    instance.shortcutHelp = original
    assert instance.shortcutHelp == original

@given(instance=DatadiagramMLTextFormat::MasterShortCut_strategy)
def test_datadiagrammltextformat::mastershortcut_patternFlags_type(instance):
    assert isinstance(instance.patternFlags, str)


@given(instance=DatadiagramMLTextFormat::MasterShortCut_strategy)
def test_datadiagrammltextformat::mastershortcut_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original

@given(instance=DatadiagramMLTextFormat::MasterShortCut_strategy)
def test_datadiagrammltextformat::mastershortcut_alignName_type(instance):
    assert isinstance(instance.alignName, str)


@given(instance=DatadiagramMLTextFormat::MasterShortCut_strategy)
def test_datadiagrammltextformat::mastershortcut_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original

@given(instance=DatadiagramMLTextFormat::MasterShortCut_strategy)
def test_datadiagrammltextformat::mastershortcut_iconSize_type(instance):
    assert isinstance(instance.iconSize, str)


@given(instance=DatadiagramMLTextFormat::MasterShortCut_strategy)
def test_datadiagrammltextformat::mastershortcut_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original

@given(instance=DatadiagramMLTextFormat::Master_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::master_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Master)

@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_hidden_type(instance):
    assert isinstance(instance.hidden, str)


@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_baseID_type(instance):
    assert isinstance(instance.baseID, str)


@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_baseID_setter(instance):
    original = instance.baseID
    instance.baseID = original
    assert instance.baseID == original

@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_matchByName_type(instance):
    assert isinstance(instance.matchByName, str)


@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_matchByName_setter(instance):
    original = instance.matchByName
    instance.matchByName = original
    assert instance.matchByName == original

@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_alignName_type(instance):
    assert isinstance(instance.alignName, str)


@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original

@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_prompt_type(instance):
    assert isinstance(instance.prompt, str)


@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original

@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_iconUpdate_type(instance):
    assert isinstance(instance.iconUpdate, str)


@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_iconUpdate_setter(instance):
    original = instance.iconUpdate
    instance.iconUpdate = original
    assert instance.iconUpdate == original

@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_iconSize_type(instance):
    assert isinstance(instance.iconSize, str)


@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original

@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_patternFlags_type(instance):
    assert isinstance(instance.patternFlags, str)


@given(instance=DatadiagramMLTextFormat::Master_strategy)
def test_datadiagrammltextformat::master_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original

@given(instance=DatadiagramMLTextFormat::FaceName_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::facename_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::FaceName)

@given(instance=DatadiagramMLTextFormat::FaceName_strategy)
def test_datadiagrammltextformat::facename_panos_type(instance):
    assert isinstance(instance.panos, str)


@given(instance=DatadiagramMLTextFormat::FaceName_strategy)
def test_datadiagrammltextformat::facename_panos_setter(instance):
    original = instance.panos
    instance.panos = original
    assert instance.panos == original

@given(instance=DatadiagramMLTextFormat::FaceName_strategy)
def test_datadiagrammltextformat::facename_unicodeRanges_type(instance):
    assert isinstance(instance.unicodeRanges, str)


@given(instance=DatadiagramMLTextFormat::FaceName_strategy)
def test_datadiagrammltextformat::facename_unicodeRanges_setter(instance):
    original = instance.unicodeRanges
    instance.unicodeRanges = original
    assert instance.unicodeRanges == original

@given(instance=DatadiagramMLTextFormat::FaceName_strategy)
def test_datadiagrammltextformat::facename_charSet_type(instance):
    assert isinstance(instance.charSet, str)


@given(instance=DatadiagramMLTextFormat::FaceName_strategy)
def test_datadiagrammltextformat::facename_charSet_setter(instance):
    original = instance.charSet
    instance.charSet = original
    assert instance.charSet == original

@given(instance=DatadiagramMLTextFormat::FaceName_strategy)
def test_datadiagrammltextformat::facename_flags_type(instance):
    assert isinstance(instance.flags, str)


@given(instance=DatadiagramMLTextFormat::FaceName_strategy)
def test_datadiagrammltextformat::facename_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original

@given(instance=DatadiagramMLTextFormat::FaceName_strategy)
def test_datadiagrammltextformat::facename_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DatadiagramMLTextFormat::FaceName_strategy)
def test_datadiagrammltextformat::facename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CustomProperty_strategy)
@settings(max_examples=50)
def test_customproperty_instantiation(instance):
    assert isinstance(instance, CustomProperty)

@given(instance=DatadiagramMLTextFormat::FontEntry_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::fontentry_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::FontEntry)

@given(instance=DatadiagramMLTextFormat::FontEntry_strategy)
def test_datadiagrammltextformat::fontentry_charSet_type(instance):
    assert isinstance(instance.charSet, str)


@given(instance=DatadiagramMLTextFormat::FontEntry_strategy)
def test_datadiagrammltextformat::fontentry_charSet_setter(instance):
    original = instance.charSet
    instance.charSet = original
    assert instance.charSet == original

@given(instance=DatadiagramMLTextFormat::FontEntry_strategy)
def test_datadiagrammltextformat::fontentry_attributes_type(instance):
    assert isinstance(instance.attributes, str)


@given(instance=DatadiagramMLTextFormat::FontEntry_strategy)
def test_datadiagrammltextformat::fontentry_attributes_setter(instance):
    original = instance.attributes
    instance.attributes = original
    assert instance.attributes == original

@given(instance=DatadiagramMLTextFormat::FontEntry_strategy)
def test_datadiagrammltextformat::fontentry_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=DatadiagramMLTextFormat::FontEntry_strategy)
def test_datadiagrammltextformat::fontentry_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=DatadiagramMLTextFormat::FontEntry_strategy)
def test_datadiagrammltextformat::fontentry_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DatadiagramMLTextFormat::FontEntry_strategy)
def test_datadiagrammltextformat::fontentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DatadiagramMLTextFormat::FontEntry_strategy)
def test_datadiagrammltextformat::fontentry_unicode_type(instance):
    assert isinstance(instance.unicode, str)


@given(instance=DatadiagramMLTextFormat::FontEntry_strategy)
def test_datadiagrammltextformat::fontentry_unicode_setter(instance):
    original = instance.unicode
    instance.unicode = original
    assert instance.unicode == original

@given(instance=DatadiagramMLTextFormat::FontEntry_strategy)
def test_datadiagrammltextformat::fontentry_pitchAndFamily_type(instance):
    assert isinstance(instance.pitchAndFamily, str)


@given(instance=DatadiagramMLTextFormat::FontEntry_strategy)
def test_datadiagrammltextformat::fontentry_pitchAndFamily_setter(instance):
    original = instance.pitchAndFamily
    instance.pitchAndFamily = original
    assert instance.pitchAndFamily == original

@given(instance=DatadiagramMLTextFormat::CustomPropertiesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::custompropertiescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::CustomPropertiesCollection)

@given(instance=IXrequiredElt_strategy)
@settings(max_examples=50)
def test_ixrequiredelt_instantiation(instance):
    assert isinstance(instance, IXrequiredElt)

@given(instance=DatadiagramMLTextFormat::Tp_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::tp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Tp)

@given(instance=DatadiagramMLTextFormat::Pp_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::pp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Pp)

@given(instance=DatadiagramMLTextFormat::Fld_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::fld_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Fld)

@given(instance=DatadiagramMLTextFormat::Cp_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::cp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::Cp)

@given(instance=DatadiagramMLTextFormat::ColorEntry_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::colorentry_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::ColorEntry)

@given(instance=DatadiagramMLTextFormat::ColorEntry_strategy)
def test_datadiagrammltextformat::colorentry_rgb_type(instance):
    assert isinstance(instance.rgb, str)


@given(instance=DatadiagramMLTextFormat::ColorEntry_strategy)
def test_datadiagrammltextformat::colorentry_rgb_setter(instance):
    original = instance.rgb
    instance.rgb = original
    assert instance.rgb == original

@given(instance=ColorEntry_strategy)
@settings(max_examples=50)
def test_colorentry_instantiation(instance):
    assert isinstance(instance, ColorEntry)

@given(instance=DatadiagramMLTextFormat::ColorsTable_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::colorstable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::ColorsTable)

@given(instance=DatadiagramMLTextFormat::CustomProperty_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::customproperty_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::CustomProperty)

@given(instance=DatadiagramMLTextFormat::CustomProperty_strategy)
def test_datadiagrammltextformat::customproperty_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=DatadiagramMLTextFormat::CustomProperty_strategy)
def test_datadiagrammltextformat::customproperty_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=DatadiagramMLTextFormat::CustomProperty_strategy)
def test_datadiagrammltextformat::customproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DatadiagramMLTextFormat::CustomProperty_strategy)
def test_datadiagrammltextformat::customproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=CustomPropertiesCollection_strategy)
@settings(max_examples=50)
def test_custompropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomPropertiesCollection)

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

@given(instance=VisioDocument_strategy)
@settings(max_examples=50)
def test_visiodocument_instantiation(instance):
    assert isinstance(instance, VisioDocument)

@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat::documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat::DocumentPropertiesCollection)

@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_alternateNames_type(instance):
    assert isinstance(instance.alternateNames, str)


@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_alternateNames_setter(instance):
    original = instance.alternateNames
    instance.alternateNames = original
    assert instance.alternateNames == original

@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_keywords_type(instance):
    assert isinstance(instance.keywords, str)


@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_buildNumberCreated_type(instance):
    assert isinstance(instance.buildNumberCreated, str)


@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_buildNumberCreated_setter(instance):
    original = instance.buildNumberCreated
    instance.buildNumberCreated = original
    assert instance.buildNumberCreated == original

@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_buildNumberEdited_type(instance):
    assert isinstance(instance.buildNumberEdited, str)


@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_buildNumberEdited_setter(instance):
    original = instance.buildNumberEdited
    instance.buildNumberEdited = original
    assert instance.buildNumberEdited == original

@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_creator_type(instance):
    assert isinstance(instance.creator, str)


@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_creator_setter(instance):
    original = instance.creator
    instance.creator = original
    assert instance.creator == original

@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_hyperlinkBase_href_type(instance):
    assert isinstance(instance.hyperlinkBase_href, str)


@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_hyperlinkBase_href_setter(instance):
    original = instance.hyperlinkBase_href
    instance.hyperlinkBase_href = original
    assert instance.hyperlinkBase_href == original

@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_manager_type(instance):
    assert isinstance(instance.manager, str)


@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original

@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_company_type(instance):
    assert isinstance(instance.company, str)


@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original

@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_template_type(instance):
    assert isinstance(instance.template, str)


@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=DatadiagramMLTextFormat::DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat::documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

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
