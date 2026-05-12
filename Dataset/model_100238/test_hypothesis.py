import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DatadiagramMLSimplified::PageElt,
    Page,
    DatadiagramMLSimplified::PagesCollection,
    DatadiagramMLSimplified::MasterElt,
    ConnectsCollection,
    DatadiagramMLSimplified::Connect,
    Connect,
    NamedElt,
    IdentifiedElt,
    DatadiagramMLSimplified::Page,
    DatadiagramMLSimplified::MasterShortCut,
    MasterShortCut,
    Master,
    VisioDocument,
    DatadiagramMLSimplified::MastersCollection,
    Text,
    DatadiagramMLSimplified::TextElt,
    Icon,
    XYABCDElt,
    DatadiagramMLSimplified::Ellipse,
    XYABElt,
    DatadiagramMLSimplified::XYABCDElt,
    DatadiagramMLSimplified::InfiniteLine,
    TextElt,
    DatadiagramMLSimplified::StringElt,
    XYABCDEElt,
    DatadiagramMLSimplified::NURBSTo,
    DatadiagramMLSimplified::XYABCDEElt,
    DatadiagramMLSimplified::SplineStart,
    DatadiagramMLSimplified::EllipticalArcTo,
    Geom,
    XYElt,
    DatadiagramMLSimplified::XYAElt,
    DatadiagramMLSimplified::MoveTo,
    DatadiagramMLSimplified::LineTo,
    XYAElt,
    DatadiagramMLSimplified::XYABElt,
    DatadiagramMLSimplified::SplineKnot,
    DatadiagramMLSimplified::PolylineTo,
    DatadiagramMLSimplified::ArcTo,
    PolylineTo,
    SplineKnot,
    ArcTo,
    MoveTo,
    LineTo,
    NURBSTo,
    SplineStart,
    EllipticalArcTo,
    Ellipse,
    InfiniteLine,
    DatadiagramMLSimplified::ShapeElt,
    ShapeElt,
    DatadiagramMLSimplified::Text,
    CellType,
    DelElt,
    IXElt,
    DatadiagramMLSimplified::XYElt,
    DatadiagramMLSimplified::Geom,
    DatadiagramMLSimplified::DelElt,
    DatadiagramMLSimplified::IXElt,
    DatadiagramMLSimplified::IdentifiedElt,
    DatadiagramMLSimplified::NamedElt,
    PageElt,
    MasterElt,
    DatadiagramMLSimplified::Icon,
    DatadiagramMLSimplified::ConnectsCollection,
    DatadiagramMLSimplified::ShapesCollection,
    UniqueIdElt,
    DatadiagramMLSimplified::Master,
    Shape,
    DatadiagramMLSimplified::PageSheet,
    ShapesCollection,
    DatadiagramMLSimplified::Shape,
    DatadiagramMLSimplified::UniqueIdElt,
    PagesCollection,
    MastersCollection,
    DatadiagramMLSimplified::VisioDocument,
    DatadiagramMLSimplified::CellType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datadiagrammlsimplified::pageelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::PageElt)


def test_datadiagrammlsimplified::pageelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::PageElt.__init__)


def test_datadiagrammlsimplified::pageelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::PageElt.__init__)
    params = list(sig.parameters.keys())



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::pagescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::PagesCollection)


def test_datadiagrammlsimplified::pagescollection_constructor_exists():
    assert callable(DatadiagramMLSimplified::PagesCollection.__init__)


def test_datadiagrammlsimplified::pagescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::PagesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::masterelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::MasterElt)


def test_datadiagrammlsimplified::masterelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::MasterElt.__init__)


def test_datadiagrammlsimplified::masterelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::MasterElt.__init__)
    params = list(sig.parameters.keys())



def test_connectscollection_is_not_abstract():
    assert not inspect.isabstract(ConnectsCollection)


def test_connectscollection_constructor_exists():
    assert callable(ConnectsCollection.__init__)


def test_connectscollection_constructor_args():
    sig = inspect.signature(ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::connect_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::Connect)


def test_datadiagrammlsimplified::connect_constructor_exists():
    assert callable(DatadiagramMLSimplified::Connect.__init__)


def test_datadiagrammlsimplified::connect_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::Connect.__init__)
    params = list(sig.parameters.keys())
    assert "fromPart" in params, "Missing parameter 'fromPart'"
    assert "fromSheet" in params, "Missing parameter 'fromSheet'"
    assert "toPart" in params, "Missing parameter 'toPart'"
    assert "toSheet" in params, "Missing parameter 'toSheet'"
    assert "toCell" in params, "Missing parameter 'toCell'"
    assert "fromCell" in params, "Missing parameter 'fromCell'"

def test_datadiagrammlsimplified::connect_has_fromPart():
    assert hasattr(DatadiagramMLSimplified::Connect, "fromPart")
    descriptor = None
    for klass in DatadiagramMLSimplified::Connect.__mro__:
        if "fromPart" in klass.__dict__:
            descriptor = klass.__dict__["fromPart"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::connect_has_fromSheet():
    assert hasattr(DatadiagramMLSimplified::Connect, "fromSheet")
    descriptor = None
    for klass in DatadiagramMLSimplified::Connect.__mro__:
        if "fromSheet" in klass.__dict__:
            descriptor = klass.__dict__["fromSheet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::connect_has_toPart():
    assert hasattr(DatadiagramMLSimplified::Connect, "toPart")
    descriptor = None
    for klass in DatadiagramMLSimplified::Connect.__mro__:
        if "toPart" in klass.__dict__:
            descriptor = klass.__dict__["toPart"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::connect_has_toSheet():
    assert hasattr(DatadiagramMLSimplified::Connect, "toSheet")
    descriptor = None
    for klass in DatadiagramMLSimplified::Connect.__mro__:
        if "toSheet" in klass.__dict__:
            descriptor = klass.__dict__["toSheet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::connect_has_toCell():
    assert hasattr(DatadiagramMLSimplified::Connect, "toCell")
    descriptor = None
    for klass in DatadiagramMLSimplified::Connect.__mro__:
        if "toCell" in klass.__dict__:
            descriptor = klass.__dict__["toCell"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::connect_has_fromCell():
    assert hasattr(DatadiagramMLSimplified::Connect, "fromCell")
    descriptor = None
    for klass in DatadiagramMLSimplified::Connect.__mro__:
        if "fromCell" in klass.__dict__:
            descriptor = klass.__dict__["fromCell"]
            break
    assert isinstance(descriptor, property)



def test_connect_is_not_abstract():
    assert not inspect.isabstract(Connect)


def test_connect_constructor_exists():
    assert callable(Connect.__init__)


def test_connect_constructor_args():
    sig = inspect.signature(Connect.__init__)
    params = list(sig.parameters.keys())



def test_namedelt_is_not_abstract():
    assert not inspect.isabstract(NamedElt)


def test_namedelt_constructor_exists():
    assert callable(NamedElt.__init__)


def test_namedelt_constructor_args():
    sig = inspect.signature(NamedElt.__init__)
    params = list(sig.parameters.keys())



def test_identifiedelt_is_not_abstract():
    assert not inspect.isabstract(IdentifiedElt)


def test_identifiedelt_constructor_exists():
    assert callable(IdentifiedElt.__init__)


def test_identifiedelt_constructor_args():
    sig = inspect.signature(IdentifiedElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::page_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::Page)


def test_datadiagrammlsimplified::page_constructor_exists():
    assert callable(DatadiagramMLSimplified::Page.__init__)


def test_datadiagrammlsimplified::page_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::Page.__init__)
    params = list(sig.parameters.keys())
    assert "ViewCenterY" in params, "Missing parameter 'ViewCenterY'"
    assert "viewCenterX" in params, "Missing parameter 'viewCenterX'"
    assert "backPage" in params, "Missing parameter 'backPage'"
    assert "reviewerID" in params, "Missing parameter 'reviewerID'"
    assert "background" in params, "Missing parameter 'background'"
    assert "viewScale" in params, "Missing parameter 'viewScale'"
    assert "associatedPage" in params, "Missing parameter 'associatedPage'"

def test_datadiagrammlsimplified::page_has_ViewCenterY():
    assert hasattr(DatadiagramMLSimplified::Page, "ViewCenterY")
    descriptor = None
    for klass in DatadiagramMLSimplified::Page.__mro__:
        if "ViewCenterY" in klass.__dict__:
            descriptor = klass.__dict__["ViewCenterY"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::page_has_viewCenterX():
    assert hasattr(DatadiagramMLSimplified::Page, "viewCenterX")
    descriptor = None
    for klass in DatadiagramMLSimplified::Page.__mro__:
        if "viewCenterX" in klass.__dict__:
            descriptor = klass.__dict__["viewCenterX"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::page_has_backPage():
    assert hasattr(DatadiagramMLSimplified::Page, "backPage")
    descriptor = None
    for klass in DatadiagramMLSimplified::Page.__mro__:
        if "backPage" in klass.__dict__:
            descriptor = klass.__dict__["backPage"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::page_has_reviewerID():
    assert hasattr(DatadiagramMLSimplified::Page, "reviewerID")
    descriptor = None
    for klass in DatadiagramMLSimplified::Page.__mro__:
        if "reviewerID" in klass.__dict__:
            descriptor = klass.__dict__["reviewerID"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::page_has_background():
    assert hasattr(DatadiagramMLSimplified::Page, "background")
    descriptor = None
    for klass in DatadiagramMLSimplified::Page.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::page_has_viewScale():
    assert hasattr(DatadiagramMLSimplified::Page, "viewScale")
    descriptor = None
    for klass in DatadiagramMLSimplified::Page.__mro__:
        if "viewScale" in klass.__dict__:
            descriptor = klass.__dict__["viewScale"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::page_has_associatedPage():
    assert hasattr(DatadiagramMLSimplified::Page, "associatedPage")
    descriptor = None
    for klass in DatadiagramMLSimplified::Page.__mro__:
        if "associatedPage" in klass.__dict__:
            descriptor = klass.__dict__["associatedPage"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlsimplified::mastershortcut_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::MasterShortCut)


def test_datadiagrammlsimplified::mastershortcut_constructor_exists():
    assert callable(DatadiagramMLSimplified::MasterShortCut.__init__)


def test_datadiagrammlsimplified::mastershortcut_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::MasterShortCut.__init__)
    params = list(sig.parameters.keys())
    assert "shortcutURL" in params, "Missing parameter 'shortcutURL'"
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "shortcutHelp" in params, "Missing parameter 'shortcutHelp'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"

def test_datadiagrammlsimplified::mastershortcut_has_shortcutURL():
    assert hasattr(DatadiagramMLSimplified::MasterShortCut, "shortcutURL")
    descriptor = None
    for klass in DatadiagramMLSimplified::MasterShortCut.__mro__:
        if "shortcutURL" in klass.__dict__:
            descriptor = klass.__dict__["shortcutURL"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::mastershortcut_has_prompt():
    assert hasattr(DatadiagramMLSimplified::MasterShortCut, "prompt")
    descriptor = None
    for klass in DatadiagramMLSimplified::MasterShortCut.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::mastershortcut_has_alignName():
    assert hasattr(DatadiagramMLSimplified::MasterShortCut, "alignName")
    descriptor = None
    for klass in DatadiagramMLSimplified::MasterShortCut.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::mastershortcut_has_patternFlags():
    assert hasattr(DatadiagramMLSimplified::MasterShortCut, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLSimplified::MasterShortCut.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::mastershortcut_has_shortcutHelp():
    assert hasattr(DatadiagramMLSimplified::MasterShortCut, "shortcutHelp")
    descriptor = None
    for klass in DatadiagramMLSimplified::MasterShortCut.__mro__:
        if "shortcutHelp" in klass.__dict__:
            descriptor = klass.__dict__["shortcutHelp"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::mastershortcut_has_iconSize():
    assert hasattr(DatadiagramMLSimplified::MasterShortCut, "iconSize")
    descriptor = None
    for klass in DatadiagramMLSimplified::MasterShortCut.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)



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



def test_visiodocument_is_not_abstract():
    assert not inspect.isabstract(VisioDocument)


def test_visiodocument_constructor_exists():
    assert callable(VisioDocument.__init__)


def test_visiodocument_constructor_args():
    sig = inspect.signature(VisioDocument.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::masterscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::MastersCollection)


def test_datadiagrammlsimplified::masterscollection_constructor_exists():
    assert callable(DatadiagramMLSimplified::MastersCollection.__init__)


def test_datadiagrammlsimplified::masterscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::MastersCollection.__init__)
    params = list(sig.parameters.keys())



def test_text_is_not_abstract():
    assert not inspect.isabstract(Text)


def test_text_constructor_exists():
    assert callable(Text.__init__)


def test_text_constructor_args():
    sig = inspect.signature(Text.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::textelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::TextElt)


def test_datadiagrammlsimplified::textelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::TextElt.__init__)


def test_datadiagrammlsimplified::textelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::TextElt.__init__)
    params = list(sig.parameters.keys())



def test_icon_is_not_abstract():
    assert not inspect.isabstract(Icon)


def test_icon_constructor_exists():
    assert callable(Icon.__init__)


def test_icon_constructor_args():
    sig = inspect.signature(Icon.__init__)
    params = list(sig.parameters.keys())



def test_xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(XYABCDElt)


def test_xyabcdelt_constructor_exists():
    assert callable(XYABCDElt.__init__)


def test_xyabcdelt_constructor_args():
    sig = inspect.signature(XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::ellipse_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::Ellipse)


def test_datadiagrammlsimplified::ellipse_constructor_exists():
    assert callable(DatadiagramMLSimplified::Ellipse.__init__)


def test_datadiagrammlsimplified::ellipse_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_xyabelt_is_not_abstract():
    assert not inspect.isabstract(XYABElt)


def test_xyabelt_constructor_exists():
    assert callable(XYABElt.__init__)


def test_xyabelt_constructor_args():
    sig = inspect.signature(XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::XYABCDElt)


def test_datadiagrammlsimplified::xyabcdelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::XYABCDElt.__init__)


def test_datadiagrammlsimplified::xyabcdelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::infiniteline_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::InfiniteLine)


def test_datadiagrammlsimplified::infiniteline_constructor_exists():
    assert callable(DatadiagramMLSimplified::InfiniteLine.__init__)


def test_datadiagrammlsimplified::infiniteline_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::InfiniteLine.__init__)
    params = list(sig.parameters.keys())



def test_textelt_is_not_abstract():
    assert not inspect.isabstract(TextElt)


def test_textelt_constructor_exists():
    assert callable(TextElt.__init__)


def test_textelt_constructor_args():
    sig = inspect.signature(TextElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::stringelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::StringElt)


def test_datadiagrammlsimplified::stringelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::StringElt.__init__)


def test_datadiagrammlsimplified::stringelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::StringElt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammlsimplified::stringelt_has_value():
    assert hasattr(DatadiagramMLSimplified::StringElt, "value")
    descriptor = None
    for klass in DatadiagramMLSimplified::StringElt.__mro__:
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



def test_datadiagrammlsimplified::nurbsto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::NURBSTo)


def test_datadiagrammlsimplified::nurbsto_constructor_exists():
    assert callable(DatadiagramMLSimplified::NURBSTo.__init__)


def test_datadiagrammlsimplified::nurbsto_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::NURBSTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::xyabcdeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::XYABCDEElt)


def test_datadiagrammlsimplified::xyabcdeelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::XYABCDEElt.__init__)


def test_datadiagrammlsimplified::xyabcdeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::XYABCDEElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::splinestart_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::SplineStart)


def test_datadiagrammlsimplified::splinestart_constructor_exists():
    assert callable(DatadiagramMLSimplified::SplineStart.__init__)


def test_datadiagrammlsimplified::splinestart_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::SplineStart.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::ellipticalarcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::EllipticalArcTo)


def test_datadiagrammlsimplified::ellipticalarcto_constructor_exists():
    assert callable(DatadiagramMLSimplified::EllipticalArcTo.__init__)


def test_datadiagrammlsimplified::ellipticalarcto_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::EllipticalArcTo.__init__)
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



def test_datadiagrammlsimplified::xyaelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::XYAElt)


def test_datadiagrammlsimplified::xyaelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::XYAElt.__init__)


def test_datadiagrammlsimplified::xyaelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::moveto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::MoveTo)


def test_datadiagrammlsimplified::moveto_constructor_exists():
    assert callable(DatadiagramMLSimplified::MoveTo.__init__)


def test_datadiagrammlsimplified::moveto_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::lineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::LineTo)


def test_datadiagrammlsimplified::lineto_constructor_exists():
    assert callable(DatadiagramMLSimplified::LineTo.__init__)


def test_datadiagrammlsimplified::lineto_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::LineTo.__init__)
    params = list(sig.parameters.keys())



def test_xyaelt_is_not_abstract():
    assert not inspect.isabstract(XYAElt)


def test_xyaelt_constructor_exists():
    assert callable(XYAElt.__init__)


def test_xyaelt_constructor_args():
    sig = inspect.signature(XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::xyabelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::XYABElt)


def test_datadiagrammlsimplified::xyabelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::XYABElt.__init__)


def test_datadiagrammlsimplified::xyabelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::splineknot_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::SplineKnot)


def test_datadiagrammlsimplified::splineknot_constructor_exists():
    assert callable(DatadiagramMLSimplified::SplineKnot.__init__)


def test_datadiagrammlsimplified::splineknot_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::SplineKnot.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::polylineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::PolylineTo)


def test_datadiagrammlsimplified::polylineto_constructor_exists():
    assert callable(DatadiagramMLSimplified::PolylineTo.__init__)


def test_datadiagrammlsimplified::polylineto_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::PolylineTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::arcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::ArcTo)


def test_datadiagrammlsimplified::arcto_constructor_exists():
    assert callable(DatadiagramMLSimplified::ArcTo.__init__)


def test_datadiagrammlsimplified::arcto_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::ArcTo.__init__)
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



def test_lineto_is_not_abstract():
    assert not inspect.isabstract(LineTo)


def test_lineto_constructor_exists():
    assert callable(LineTo.__init__)


def test_lineto_constructor_args():
    sig = inspect.signature(LineTo.__init__)
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



def test_datadiagrammlsimplified::shapeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::ShapeElt)


def test_datadiagrammlsimplified::shapeelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::ShapeElt.__init__)


def test_datadiagrammlsimplified::shapeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_shapeelt_is_not_abstract():
    assert not inspect.isabstract(ShapeElt)


def test_shapeelt_constructor_exists():
    assert callable(ShapeElt.__init__)


def test_shapeelt_constructor_args():
    sig = inspect.signature(ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::text_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::Text)


def test_datadiagrammlsimplified::text_constructor_exists():
    assert callable(DatadiagramMLSimplified::Text.__init__)


def test_datadiagrammlsimplified::text_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::Text.__init__)
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



def test_datadiagrammlsimplified::xyelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::XYElt)


def test_datadiagrammlsimplified::xyelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::XYElt.__init__)


def test_datadiagrammlsimplified::xyelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::XYElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::geom_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::Geom)


def test_datadiagrammlsimplified::geom_constructor_exists():
    assert callable(DatadiagramMLSimplified::Geom.__init__)


def test_datadiagrammlsimplified::geom_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::Geom.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::delelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::DelElt)


def test_datadiagrammlsimplified::delelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::DelElt.__init__)


def test_datadiagrammlsimplified::delelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::DelElt.__init__)
    params = list(sig.parameters.keys())
    assert "del_" in params, "Missing parameter 'del_'"

def test_datadiagrammlsimplified::delelt_has_del_():
    assert hasattr(DatadiagramMLSimplified::DelElt, "del_")
    descriptor = None
    for klass in DatadiagramMLSimplified::DelElt.__mro__:
        if "del_" in klass.__dict__:
            descriptor = klass.__dict__["del_"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlsimplified::ixelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::IXElt)


def test_datadiagrammlsimplified::ixelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::IXElt.__init__)


def test_datadiagrammlsimplified::ixelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::IXElt.__init__)
    params = list(sig.parameters.keys())
    assert "iX" in params, "Missing parameter 'iX'"

def test_datadiagrammlsimplified::ixelt_has_iX():
    assert hasattr(DatadiagramMLSimplified::IXElt, "iX")
    descriptor = None
    for klass in DatadiagramMLSimplified::IXElt.__mro__:
        if "iX" in klass.__dict__:
            descriptor = klass.__dict__["iX"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlsimplified::identifiedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::IdentifiedElt)


def test_datadiagrammlsimplified::identifiedelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::IdentifiedElt.__init__)


def test_datadiagrammlsimplified::identifiedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::IdentifiedElt.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_datadiagrammlsimplified::identifiedelt_has_ID():
    assert hasattr(DatadiagramMLSimplified::IdentifiedElt, "ID")
    descriptor = None
    for klass in DatadiagramMLSimplified::IdentifiedElt.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlsimplified::namedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::NamedElt)


def test_datadiagrammlsimplified::namedelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::NamedElt.__init__)


def test_datadiagrammlsimplified::namedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "nameU" in params, "Missing parameter 'nameU'"

def test_datadiagrammlsimplified::namedelt_has_name():
    assert hasattr(DatadiagramMLSimplified::NamedElt, "name")
    descriptor = None
    for klass in DatadiagramMLSimplified::NamedElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::namedelt_has_nameU():
    assert hasattr(DatadiagramMLSimplified::NamedElt, "nameU")
    descriptor = None
    for klass in DatadiagramMLSimplified::NamedElt.__mro__:
        if "nameU" in klass.__dict__:
            descriptor = klass.__dict__["nameU"]
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



def test_datadiagrammlsimplified::icon_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::Icon)


def test_datadiagrammlsimplified::icon_constructor_exists():
    assert callable(DatadiagramMLSimplified::Icon.__init__)


def test_datadiagrammlsimplified::icon_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::Icon.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammlsimplified::icon_has_value():
    assert hasattr(DatadiagramMLSimplified::Icon, "value")
    descriptor = None
    for klass in DatadiagramMLSimplified::Icon.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlsimplified::connectscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::ConnectsCollection)


def test_datadiagrammlsimplified::connectscollection_constructor_exists():
    assert callable(DatadiagramMLSimplified::ConnectsCollection.__init__)


def test_datadiagrammlsimplified::connectscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::shapescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::ShapesCollection)


def test_datadiagrammlsimplified::shapescollection_constructor_exists():
    assert callable(DatadiagramMLSimplified::ShapesCollection.__init__)


def test_datadiagrammlsimplified::shapescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(UniqueIdElt)


def test_uniqueidelt_constructor_exists():
    assert callable(UniqueIdElt.__init__)


def test_uniqueidelt_constructor_args():
    sig = inspect.signature(UniqueIdElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::master_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::Master)


def test_datadiagrammlsimplified::master_constructor_exists():
    assert callable(DatadiagramMLSimplified::Master.__init__)


def test_datadiagrammlsimplified::master_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::Master.__init__)
    params = list(sig.parameters.keys())
    assert "iconSize" in params, "Missing parameter 'iconSize'"
    assert "matchByName" in params, "Missing parameter 'matchByName'"
    assert "iconUpdate" in params, "Missing parameter 'iconUpdate'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "baseID" in params, "Missing parameter 'baseID'"
    assert "prompt" in params, "Missing parameter 'prompt'"

def test_datadiagrammlsimplified::master_has_iconSize():
    assert hasattr(DatadiagramMLSimplified::Master, "iconSize")
    descriptor = None
    for klass in DatadiagramMLSimplified::Master.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::master_has_matchByName():
    assert hasattr(DatadiagramMLSimplified::Master, "matchByName")
    descriptor = None
    for klass in DatadiagramMLSimplified::Master.__mro__:
        if "matchByName" in klass.__dict__:
            descriptor = klass.__dict__["matchByName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::master_has_iconUpdate():
    assert hasattr(DatadiagramMLSimplified::Master, "iconUpdate")
    descriptor = None
    for klass in DatadiagramMLSimplified::Master.__mro__:
        if "iconUpdate" in klass.__dict__:
            descriptor = klass.__dict__["iconUpdate"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::master_has_hidden():
    assert hasattr(DatadiagramMLSimplified::Master, "hidden")
    descriptor = None
    for klass in DatadiagramMLSimplified::Master.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::master_has_alignName():
    assert hasattr(DatadiagramMLSimplified::Master, "alignName")
    descriptor = None
    for klass in DatadiagramMLSimplified::Master.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::master_has_patternFlags():
    assert hasattr(DatadiagramMLSimplified::Master, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLSimplified::Master.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::master_has_baseID():
    assert hasattr(DatadiagramMLSimplified::Master, "baseID")
    descriptor = None
    for klass in DatadiagramMLSimplified::Master.__mro__:
        if "baseID" in klass.__dict__:
            descriptor = klass.__dict__["baseID"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::master_has_prompt():
    assert hasattr(DatadiagramMLSimplified::Master, "prompt")
    descriptor = None
    for klass in DatadiagramMLSimplified::Master.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::pagesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::PageSheet)


def test_datadiagrammlsimplified::pagesheet_constructor_exists():
    assert callable(DatadiagramMLSimplified::PageSheet.__init__)


def test_datadiagrammlsimplified::pagesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::PageSheet.__init__)
    params = list(sig.parameters.keys())



def test_shapescollection_is_not_abstract():
    assert not inspect.isabstract(ShapesCollection)


def test_shapescollection_constructor_exists():
    assert callable(ShapesCollection.__init__)


def test_shapescollection_constructor_args():
    sig = inspect.signature(ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::shape_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::Shape)


def test_datadiagrammlsimplified::shape_constructor_exists():
    assert callable(DatadiagramMLSimplified::Shape.__init__)


def test_datadiagrammlsimplified::shape_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::Shape.__init__)
    params = list(sig.parameters.keys())
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "textStyle" in params, "Missing parameter 'textStyle'"
    assert "fillStyle" in params, "Missing parameter 'fillStyle'"

def test_datadiagrammlsimplified::shape_has_lineStyle():
    assert hasattr(DatadiagramMLSimplified::Shape, "lineStyle")
    descriptor = None
    for klass in DatadiagramMLSimplified::Shape.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::shape_has_textStyle():
    assert hasattr(DatadiagramMLSimplified::Shape, "textStyle")
    descriptor = None
    for klass in DatadiagramMLSimplified::Shape.__mro__:
        if "textStyle" in klass.__dict__:
            descriptor = klass.__dict__["textStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::shape_has_fillStyle():
    assert hasattr(DatadiagramMLSimplified::Shape, "fillStyle")
    descriptor = None
    for klass in DatadiagramMLSimplified::Shape.__mro__:
        if "fillStyle" in klass.__dict__:
            descriptor = klass.__dict__["fillStyle"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlsimplified::uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::UniqueIdElt)


def test_datadiagrammlsimplified::uniqueidelt_constructor_exists():
    assert callable(DatadiagramMLSimplified::UniqueIdElt.__init__)


def test_datadiagrammlsimplified::uniqueidelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::UniqueIdElt.__init__)
    params = list(sig.parameters.keys())
    assert "UniqueID" in params, "Missing parameter 'UniqueID'"

def test_datadiagrammlsimplified::uniqueidelt_has_UniqueID():
    assert hasattr(DatadiagramMLSimplified::UniqueIdElt, "UniqueID")
    descriptor = None
    for klass in DatadiagramMLSimplified::UniqueIdElt.__mro__:
        if "UniqueID" in klass.__dict__:
            descriptor = klass.__dict__["UniqueID"]
            break
    assert isinstance(descriptor, property)



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



def test_datadiagrammlsimplified::visiodocument_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::VisioDocument)


def test_datadiagrammlsimplified::visiodocument_constructor_exists():
    assert callable(DatadiagramMLSimplified::VisioDocument.__init__)


def test_datadiagrammlsimplified::visiodocument_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::VisioDocument.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified::celltype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified::CellType)


def test_datadiagrammlsimplified::celltype_constructor_exists():
    assert callable(DatadiagramMLSimplified::CellType.__init__)


def test_datadiagrammlsimplified::celltype_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified::CellType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "formula" in params, "Missing parameter 'formula'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "err" in params, "Missing parameter 'err'"

def test_datadiagrammlsimplified::celltype_has_value():
    assert hasattr(DatadiagramMLSimplified::CellType, "value")
    descriptor = None
    for klass in DatadiagramMLSimplified::CellType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::celltype_has_formula():
    assert hasattr(DatadiagramMLSimplified::CellType, "formula")
    descriptor = None
    for klass in DatadiagramMLSimplified::CellType.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::celltype_has_unit():
    assert hasattr(DatadiagramMLSimplified::CellType, "unit")
    descriptor = None
    for klass in DatadiagramMLSimplified::CellType.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified::celltype_has_err():
    assert hasattr(DatadiagramMLSimplified::CellType, "err")
    descriptor = None
    for klass in DatadiagramMLSimplified::CellType.__mro__:
        if "err" in klass.__dict__:
            descriptor = klass.__dict__["err"]
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
DatadiagramMLSimplified::PageElt_strategy = st.builds(
    DatadiagramMLSimplified::PageElt,
)
Page_strategy = st.builds(
    Page,
)
DatadiagramMLSimplified::PagesCollection_strategy = st.builds(
    DatadiagramMLSimplified::PagesCollection,
)
DatadiagramMLSimplified::MasterElt_strategy = st.builds(
    DatadiagramMLSimplified::MasterElt,
)
ConnectsCollection_strategy = st.builds(
    ConnectsCollection,
)
DatadiagramMLSimplified::Connect_strategy = st.builds(
    DatadiagramMLSimplified::Connect,
    fromPart=
        safe_text,
    fromSheet=
        safe_text,
    toPart=
        safe_text,
    toSheet=
        safe_text,
    toCell=
        safe_text,
    fromCell=
        safe_text
)
Connect_strategy = st.builds(
    Connect,
)
NamedElt_strategy = st.builds(
    NamedElt,
)
IdentifiedElt_strategy = st.builds(
    IdentifiedElt,
)
DatadiagramMLSimplified::Page_strategy = st.builds(
    DatadiagramMLSimplified::Page,
    ViewCenterY=
        safe_text,
    viewCenterX=
        safe_text,
    backPage=
        safe_text,
    reviewerID=
        safe_text,
    background=
        safe_text,
    viewScale=
        safe_text,
    associatedPage=
        safe_text
)
DatadiagramMLSimplified::MasterShortCut_strategy = st.builds(
    DatadiagramMLSimplified::MasterShortCut,
    shortcutURL=
        safe_text,
    prompt=
        safe_text,
    alignName=
        safe_text,
    patternFlags=
        safe_text,
    shortcutHelp=
        safe_text,
    iconSize=
        safe_text
)
MasterShortCut_strategy = st.builds(
    MasterShortCut,
)
Master_strategy = st.builds(
    Master,
)
VisioDocument_strategy = st.builds(
    VisioDocument,
)
DatadiagramMLSimplified::MastersCollection_strategy = st.builds(
    DatadiagramMLSimplified::MastersCollection,
)
Text_strategy = st.builds(
    Text,
)
DatadiagramMLSimplified::TextElt_strategy = st.builds(
    DatadiagramMLSimplified::TextElt,
)
Icon_strategy = st.builds(
    Icon,
)
XYABCDElt_strategy = st.builds(
    XYABCDElt,
)
DatadiagramMLSimplified::Ellipse_strategy = st.builds(
    DatadiagramMLSimplified::Ellipse,
)
XYABElt_strategy = st.builds(
    XYABElt,
)
DatadiagramMLSimplified::XYABCDElt_strategy = st.builds(
    DatadiagramMLSimplified::XYABCDElt,
)
DatadiagramMLSimplified::InfiniteLine_strategy = st.builds(
    DatadiagramMLSimplified::InfiniteLine,
)
TextElt_strategy = st.builds(
    TextElt,
)
DatadiagramMLSimplified::StringElt_strategy = st.builds(
    DatadiagramMLSimplified::StringElt,
    value=
        safe_text
)
XYABCDEElt_strategy = st.builds(
    XYABCDEElt,
)
DatadiagramMLSimplified::NURBSTo_strategy = st.builds(
    DatadiagramMLSimplified::NURBSTo,
)
DatadiagramMLSimplified::XYABCDEElt_strategy = st.builds(
    DatadiagramMLSimplified::XYABCDEElt,
)
DatadiagramMLSimplified::SplineStart_strategy = st.builds(
    DatadiagramMLSimplified::SplineStart,
)
DatadiagramMLSimplified::EllipticalArcTo_strategy = st.builds(
    DatadiagramMLSimplified::EllipticalArcTo,
)
Geom_strategy = st.builds(
    Geom,
)
XYElt_strategy = st.builds(
    XYElt,
)
DatadiagramMLSimplified::XYAElt_strategy = st.builds(
    DatadiagramMLSimplified::XYAElt,
)
DatadiagramMLSimplified::MoveTo_strategy = st.builds(
    DatadiagramMLSimplified::MoveTo,
)
DatadiagramMLSimplified::LineTo_strategy = st.builds(
    DatadiagramMLSimplified::LineTo,
)
XYAElt_strategy = st.builds(
    XYAElt,
)
DatadiagramMLSimplified::XYABElt_strategy = st.builds(
    DatadiagramMLSimplified::XYABElt,
)
DatadiagramMLSimplified::SplineKnot_strategy = st.builds(
    DatadiagramMLSimplified::SplineKnot,
)
DatadiagramMLSimplified::PolylineTo_strategy = st.builds(
    DatadiagramMLSimplified::PolylineTo,
)
DatadiagramMLSimplified::ArcTo_strategy = st.builds(
    DatadiagramMLSimplified::ArcTo,
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
LineTo_strategy = st.builds(
    LineTo,
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
DatadiagramMLSimplified::ShapeElt_strategy = st.builds(
    DatadiagramMLSimplified::ShapeElt,
)
ShapeElt_strategy = st.builds(
    ShapeElt,
)
DatadiagramMLSimplified::Text_strategy = st.builds(
    DatadiagramMLSimplified::Text,
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
DatadiagramMLSimplified::XYElt_strategy = st.builds(
    DatadiagramMLSimplified::XYElt,
)
DatadiagramMLSimplified::Geom_strategy = st.builds(
    DatadiagramMLSimplified::Geom,
)
DatadiagramMLSimplified::DelElt_strategy = st.builds(
    DatadiagramMLSimplified::DelElt,
    del_=
        safe_text
)
DatadiagramMLSimplified::IXElt_strategy = st.builds(
    DatadiagramMLSimplified::IXElt,
    iX=
        safe_text
)
DatadiagramMLSimplified::IdentifiedElt_strategy = st.builds(
    DatadiagramMLSimplified::IdentifiedElt,
    ID=
        safe_text
)
DatadiagramMLSimplified::NamedElt_strategy = st.builds(
    DatadiagramMLSimplified::NamedElt,
    name=
        safe_text,
    nameU=
        safe_text
)
PageElt_strategy = st.builds(
    PageElt,
)
MasterElt_strategy = st.builds(
    MasterElt,
)
DatadiagramMLSimplified::Icon_strategy = st.builds(
    DatadiagramMLSimplified::Icon,
    value=
        safe_text
)
DatadiagramMLSimplified::ConnectsCollection_strategy = st.builds(
    DatadiagramMLSimplified::ConnectsCollection,
)
DatadiagramMLSimplified::ShapesCollection_strategy = st.builds(
    DatadiagramMLSimplified::ShapesCollection,
)
UniqueIdElt_strategy = st.builds(
    UniqueIdElt,
)
DatadiagramMLSimplified::Master_strategy = st.builds(
    DatadiagramMLSimplified::Master,
    iconSize=
        safe_text,
    matchByName=
        safe_text,
    iconUpdate=
        safe_text,
    hidden=
        safe_text,
    alignName=
        safe_text,
    patternFlags=
        safe_text,
    baseID=
        safe_text,
    prompt=
        safe_text
)
Shape_strategy = st.builds(
    Shape,
)
DatadiagramMLSimplified::PageSheet_strategy = st.builds(
    DatadiagramMLSimplified::PageSheet,
)
ShapesCollection_strategy = st.builds(
    ShapesCollection,
)
DatadiagramMLSimplified::Shape_strategy = st.builds(
    DatadiagramMLSimplified::Shape,
    lineStyle=
        safe_text,
    textStyle=
        safe_text,
    fillStyle=
        safe_text
)
DatadiagramMLSimplified::UniqueIdElt_strategy = st.builds(
    DatadiagramMLSimplified::UniqueIdElt,
    UniqueID=
        safe_text
)
PagesCollection_strategy = st.builds(
    PagesCollection,
)
MastersCollection_strategy = st.builds(
    MastersCollection,
)
DatadiagramMLSimplified::VisioDocument_strategy = st.builds(
    DatadiagramMLSimplified::VisioDocument,
)
DatadiagramMLSimplified::CellType_strategy = st.builds(
    DatadiagramMLSimplified::CellType,
    value=
        safe_text,
    formula=
        safe_text,
    unit=
        safe_text,
    err=
        safe_text
)

@given(instance=DatadiagramMLSimplified::PageElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::pageelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::PageElt)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=DatadiagramMLSimplified::PagesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::pagescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::PagesCollection)

@given(instance=DatadiagramMLSimplified::MasterElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::masterelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::MasterElt)

@given(instance=ConnectsCollection_strategy)
@settings(max_examples=50)
def test_connectscollection_instantiation(instance):
    assert isinstance(instance, ConnectsCollection)

@given(instance=DatadiagramMLSimplified::Connect_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::connect_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::Connect)

@given(instance=DatadiagramMLSimplified::Connect_strategy)
def test_datadiagrammlsimplified::connect_fromPart_type(instance):
    assert isinstance(instance.fromPart, str)


@given(instance=DatadiagramMLSimplified::Connect_strategy)
def test_datadiagrammlsimplified::connect_fromPart_setter(instance):
    original = instance.fromPart
    instance.fromPart = original
    assert instance.fromPart == original

@given(instance=DatadiagramMLSimplified::Connect_strategy)
def test_datadiagrammlsimplified::connect_fromSheet_type(instance):
    assert isinstance(instance.fromSheet, str)


@given(instance=DatadiagramMLSimplified::Connect_strategy)
def test_datadiagrammlsimplified::connect_fromSheet_setter(instance):
    original = instance.fromSheet
    instance.fromSheet = original
    assert instance.fromSheet == original

@given(instance=DatadiagramMLSimplified::Connect_strategy)
def test_datadiagrammlsimplified::connect_toPart_type(instance):
    assert isinstance(instance.toPart, str)


@given(instance=DatadiagramMLSimplified::Connect_strategy)
def test_datadiagrammlsimplified::connect_toPart_setter(instance):
    original = instance.toPart
    instance.toPart = original
    assert instance.toPart == original

@given(instance=DatadiagramMLSimplified::Connect_strategy)
def test_datadiagrammlsimplified::connect_toSheet_type(instance):
    assert isinstance(instance.toSheet, str)


@given(instance=DatadiagramMLSimplified::Connect_strategy)
def test_datadiagrammlsimplified::connect_toSheet_setter(instance):
    original = instance.toSheet
    instance.toSheet = original
    assert instance.toSheet == original

@given(instance=DatadiagramMLSimplified::Connect_strategy)
def test_datadiagrammlsimplified::connect_toCell_type(instance):
    assert isinstance(instance.toCell, str)


@given(instance=DatadiagramMLSimplified::Connect_strategy)
def test_datadiagrammlsimplified::connect_toCell_setter(instance):
    original = instance.toCell
    instance.toCell = original
    assert instance.toCell == original

@given(instance=DatadiagramMLSimplified::Connect_strategy)
def test_datadiagrammlsimplified::connect_fromCell_type(instance):
    assert isinstance(instance.fromCell, str)


@given(instance=DatadiagramMLSimplified::Connect_strategy)
def test_datadiagrammlsimplified::connect_fromCell_setter(instance):
    original = instance.fromCell
    instance.fromCell = original
    assert instance.fromCell == original

@given(instance=Connect_strategy)
@settings(max_examples=50)
def test_connect_instantiation(instance):
    assert isinstance(instance, Connect)

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=IdentifiedElt_strategy)
@settings(max_examples=50)
def test_identifiedelt_instantiation(instance):
    assert isinstance(instance, IdentifiedElt)

@given(instance=DatadiagramMLSimplified::Page_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::page_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::Page)

@given(instance=DatadiagramMLSimplified::Page_strategy)
def test_datadiagrammlsimplified::page_ViewCenterY_type(instance):
    assert isinstance(instance.ViewCenterY, str)


@given(instance=DatadiagramMLSimplified::Page_strategy)
def test_datadiagrammlsimplified::page_ViewCenterY_setter(instance):
    original = instance.ViewCenterY
    instance.ViewCenterY = original
    assert instance.ViewCenterY == original

@given(instance=DatadiagramMLSimplified::Page_strategy)
def test_datadiagrammlsimplified::page_viewCenterX_type(instance):
    assert isinstance(instance.viewCenterX, str)


@given(instance=DatadiagramMLSimplified::Page_strategy)
def test_datadiagrammlsimplified::page_viewCenterX_setter(instance):
    original = instance.viewCenterX
    instance.viewCenterX = original
    assert instance.viewCenterX == original

@given(instance=DatadiagramMLSimplified::Page_strategy)
def test_datadiagrammlsimplified::page_backPage_type(instance):
    assert isinstance(instance.backPage, str)


@given(instance=DatadiagramMLSimplified::Page_strategy)
def test_datadiagrammlsimplified::page_backPage_setter(instance):
    original = instance.backPage
    instance.backPage = original
    assert instance.backPage == original

@given(instance=DatadiagramMLSimplified::Page_strategy)
def test_datadiagrammlsimplified::page_reviewerID_type(instance):
    assert isinstance(instance.reviewerID, str)


@given(instance=DatadiagramMLSimplified::Page_strategy)
def test_datadiagrammlsimplified::page_reviewerID_setter(instance):
    original = instance.reviewerID
    instance.reviewerID = original
    assert instance.reviewerID == original

@given(instance=DatadiagramMLSimplified::Page_strategy)
def test_datadiagrammlsimplified::page_background_type(instance):
    assert isinstance(instance.background, str)


@given(instance=DatadiagramMLSimplified::Page_strategy)
def test_datadiagrammlsimplified::page_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original

@given(instance=DatadiagramMLSimplified::Page_strategy)
def test_datadiagrammlsimplified::page_viewScale_type(instance):
    assert isinstance(instance.viewScale, str)


@given(instance=DatadiagramMLSimplified::Page_strategy)
def test_datadiagrammlsimplified::page_viewScale_setter(instance):
    original = instance.viewScale
    instance.viewScale = original
    assert instance.viewScale == original

@given(instance=DatadiagramMLSimplified::Page_strategy)
def test_datadiagrammlsimplified::page_associatedPage_type(instance):
    assert isinstance(instance.associatedPage, str)


@given(instance=DatadiagramMLSimplified::Page_strategy)
def test_datadiagrammlsimplified::page_associatedPage_setter(instance):
    original = instance.associatedPage
    instance.associatedPage = original
    assert instance.associatedPage == original

@given(instance=DatadiagramMLSimplified::MasterShortCut_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::mastershortcut_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::MasterShortCut)

@given(instance=DatadiagramMLSimplified::MasterShortCut_strategy)
def test_datadiagrammlsimplified::mastershortcut_shortcutURL_type(instance):
    assert isinstance(instance.shortcutURL, str)


@given(instance=DatadiagramMLSimplified::MasterShortCut_strategy)
def test_datadiagrammlsimplified::mastershortcut_shortcutURL_setter(instance):
    original = instance.shortcutURL
    instance.shortcutURL = original
    assert instance.shortcutURL == original

@given(instance=DatadiagramMLSimplified::MasterShortCut_strategy)
def test_datadiagrammlsimplified::mastershortcut_prompt_type(instance):
    assert isinstance(instance.prompt, str)


@given(instance=DatadiagramMLSimplified::MasterShortCut_strategy)
def test_datadiagrammlsimplified::mastershortcut_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original

@given(instance=DatadiagramMLSimplified::MasterShortCut_strategy)
def test_datadiagrammlsimplified::mastershortcut_alignName_type(instance):
    assert isinstance(instance.alignName, str)


@given(instance=DatadiagramMLSimplified::MasterShortCut_strategy)
def test_datadiagrammlsimplified::mastershortcut_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original

@given(instance=DatadiagramMLSimplified::MasterShortCut_strategy)
def test_datadiagrammlsimplified::mastershortcut_patternFlags_type(instance):
    assert isinstance(instance.patternFlags, str)


@given(instance=DatadiagramMLSimplified::MasterShortCut_strategy)
def test_datadiagrammlsimplified::mastershortcut_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original

@given(instance=DatadiagramMLSimplified::MasterShortCut_strategy)
def test_datadiagrammlsimplified::mastershortcut_shortcutHelp_type(instance):
    assert isinstance(instance.shortcutHelp, str)


@given(instance=DatadiagramMLSimplified::MasterShortCut_strategy)
def test_datadiagrammlsimplified::mastershortcut_shortcutHelp_setter(instance):
    original = instance.shortcutHelp
    instance.shortcutHelp = original
    assert instance.shortcutHelp == original

@given(instance=DatadiagramMLSimplified::MasterShortCut_strategy)
def test_datadiagrammlsimplified::mastershortcut_iconSize_type(instance):
    assert isinstance(instance.iconSize, str)


@given(instance=DatadiagramMLSimplified::MasterShortCut_strategy)
def test_datadiagrammlsimplified::mastershortcut_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original

@given(instance=MasterShortCut_strategy)
@settings(max_examples=50)
def test_mastershortcut_instantiation(instance):
    assert isinstance(instance, MasterShortCut)

@given(instance=Master_strategy)
@settings(max_examples=50)
def test_master_instantiation(instance):
    assert isinstance(instance, Master)

@given(instance=VisioDocument_strategy)
@settings(max_examples=50)
def test_visiodocument_instantiation(instance):
    assert isinstance(instance, VisioDocument)

@given(instance=DatadiagramMLSimplified::MastersCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::masterscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::MastersCollection)

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=DatadiagramMLSimplified::TextElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::textelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::TextElt)

@given(instance=Icon_strategy)
@settings(max_examples=50)
def test_icon_instantiation(instance):
    assert isinstance(instance, Icon)

@given(instance=XYABCDElt_strategy)
@settings(max_examples=50)
def test_xyabcdelt_instantiation(instance):
    assert isinstance(instance, XYABCDElt)

@given(instance=DatadiagramMLSimplified::Ellipse_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::ellipse_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::Ellipse)

@given(instance=XYABElt_strategy)
@settings(max_examples=50)
def test_xyabelt_instantiation(instance):
    assert isinstance(instance, XYABElt)

@given(instance=DatadiagramMLSimplified::XYABCDElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::xyabcdelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::XYABCDElt)

@given(instance=DatadiagramMLSimplified::InfiniteLine_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::infiniteline_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::InfiniteLine)

@given(instance=TextElt_strategy)
@settings(max_examples=50)
def test_textelt_instantiation(instance):
    assert isinstance(instance, TextElt)

@given(instance=DatadiagramMLSimplified::StringElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::stringelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::StringElt)

@given(instance=DatadiagramMLSimplified::StringElt_strategy)
def test_datadiagrammlsimplified::stringelt_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DatadiagramMLSimplified::StringElt_strategy)
def test_datadiagrammlsimplified::stringelt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=XYABCDEElt_strategy)
@settings(max_examples=50)
def test_xyabcdeelt_instantiation(instance):
    assert isinstance(instance, XYABCDEElt)

@given(instance=DatadiagramMLSimplified::NURBSTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::nurbsto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::NURBSTo)

@given(instance=DatadiagramMLSimplified::XYABCDEElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::xyabcdeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::XYABCDEElt)

@given(instance=DatadiagramMLSimplified::SplineStart_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::splinestart_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::SplineStart)

@given(instance=DatadiagramMLSimplified::EllipticalArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::ellipticalarcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::EllipticalArcTo)

@given(instance=Geom_strategy)
@settings(max_examples=50)
def test_geom_instantiation(instance):
    assert isinstance(instance, Geom)

@given(instance=XYElt_strategy)
@settings(max_examples=50)
def test_xyelt_instantiation(instance):
    assert isinstance(instance, XYElt)

@given(instance=DatadiagramMLSimplified::XYAElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::xyaelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::XYAElt)

@given(instance=DatadiagramMLSimplified::MoveTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::moveto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::MoveTo)

@given(instance=DatadiagramMLSimplified::LineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::lineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::LineTo)

@given(instance=XYAElt_strategy)
@settings(max_examples=50)
def test_xyaelt_instantiation(instance):
    assert isinstance(instance, XYAElt)

@given(instance=DatadiagramMLSimplified::XYABElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::xyabelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::XYABElt)

@given(instance=DatadiagramMLSimplified::SplineKnot_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::splineknot_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::SplineKnot)

@given(instance=DatadiagramMLSimplified::PolylineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::polylineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::PolylineTo)

@given(instance=DatadiagramMLSimplified::ArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::arcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::ArcTo)

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

@given(instance=LineTo_strategy)
@settings(max_examples=50)
def test_lineto_instantiation(instance):
    assert isinstance(instance, LineTo)

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

@given(instance=DatadiagramMLSimplified::ShapeElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::shapeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::ShapeElt)

@given(instance=ShapeElt_strategy)
@settings(max_examples=50)
def test_shapeelt_instantiation(instance):
    assert isinstance(instance, ShapeElt)

@given(instance=DatadiagramMLSimplified::Text_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::text_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::Text)

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

@given(instance=DatadiagramMLSimplified::XYElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::xyelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::XYElt)

@given(instance=DatadiagramMLSimplified::Geom_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::geom_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::Geom)

@given(instance=DatadiagramMLSimplified::DelElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::delelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::DelElt)

@given(instance=DatadiagramMLSimplified::DelElt_strategy)
def test_datadiagrammlsimplified::delelt_del__type(instance):
    assert isinstance(instance.del_, str)


@given(instance=DatadiagramMLSimplified::DelElt_strategy)
def test_datadiagrammlsimplified::delelt_del__setter(instance):
    original = instance.del_
    instance.del_ = original
    assert instance.del_ == original

@given(instance=DatadiagramMLSimplified::IXElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::ixelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::IXElt)

@given(instance=DatadiagramMLSimplified::IXElt_strategy)
def test_datadiagrammlsimplified::ixelt_iX_type(instance):
    assert isinstance(instance.iX, str)


@given(instance=DatadiagramMLSimplified::IXElt_strategy)
def test_datadiagrammlsimplified::ixelt_iX_setter(instance):
    original = instance.iX
    instance.iX = original
    assert instance.iX == original

@given(instance=DatadiagramMLSimplified::IdentifiedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::identifiedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::IdentifiedElt)

@given(instance=DatadiagramMLSimplified::IdentifiedElt_strategy)
def test_datadiagrammlsimplified::identifiedelt_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=DatadiagramMLSimplified::IdentifiedElt_strategy)
def test_datadiagrammlsimplified::identifiedelt_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=DatadiagramMLSimplified::NamedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::namedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::NamedElt)

@given(instance=DatadiagramMLSimplified::NamedElt_strategy)
def test_datadiagrammlsimplified::namedelt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DatadiagramMLSimplified::NamedElt_strategy)
def test_datadiagrammlsimplified::namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DatadiagramMLSimplified::NamedElt_strategy)
def test_datadiagrammlsimplified::namedelt_nameU_type(instance):
    assert isinstance(instance.nameU, str)


@given(instance=DatadiagramMLSimplified::NamedElt_strategy)
def test_datadiagrammlsimplified::namedelt_nameU_setter(instance):
    original = instance.nameU
    instance.nameU = original
    assert instance.nameU == original

@given(instance=PageElt_strategy)
@settings(max_examples=50)
def test_pageelt_instantiation(instance):
    assert isinstance(instance, PageElt)

@given(instance=MasterElt_strategy)
@settings(max_examples=50)
def test_masterelt_instantiation(instance):
    assert isinstance(instance, MasterElt)

@given(instance=DatadiagramMLSimplified::Icon_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::icon_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::Icon)

@given(instance=DatadiagramMLSimplified::Icon_strategy)
def test_datadiagrammlsimplified::icon_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DatadiagramMLSimplified::Icon_strategy)
def test_datadiagrammlsimplified::icon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DatadiagramMLSimplified::ConnectsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::connectscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::ConnectsCollection)

@given(instance=DatadiagramMLSimplified::ShapesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::shapescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::ShapesCollection)

@given(instance=UniqueIdElt_strategy)
@settings(max_examples=50)
def test_uniqueidelt_instantiation(instance):
    assert isinstance(instance, UniqueIdElt)

@given(instance=DatadiagramMLSimplified::Master_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::master_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::Master)

@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_iconSize_type(instance):
    assert isinstance(instance.iconSize, str)


@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original

@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_matchByName_type(instance):
    assert isinstance(instance.matchByName, str)


@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_matchByName_setter(instance):
    original = instance.matchByName
    instance.matchByName = original
    assert instance.matchByName == original

@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_iconUpdate_type(instance):
    assert isinstance(instance.iconUpdate, str)


@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_iconUpdate_setter(instance):
    original = instance.iconUpdate
    instance.iconUpdate = original
    assert instance.iconUpdate == original

@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_hidden_type(instance):
    assert isinstance(instance.hidden, str)


@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_alignName_type(instance):
    assert isinstance(instance.alignName, str)


@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original

@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_patternFlags_type(instance):
    assert isinstance(instance.patternFlags, str)


@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original

@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_baseID_type(instance):
    assert isinstance(instance.baseID, str)


@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_baseID_setter(instance):
    original = instance.baseID
    instance.baseID = original
    assert instance.baseID == original

@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_prompt_type(instance):
    assert isinstance(instance.prompt, str)


@given(instance=DatadiagramMLSimplified::Master_strategy)
def test_datadiagrammlsimplified::master_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=DatadiagramMLSimplified::PageSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::pagesheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::PageSheet)

@given(instance=ShapesCollection_strategy)
@settings(max_examples=50)
def test_shapescollection_instantiation(instance):
    assert isinstance(instance, ShapesCollection)

@given(instance=DatadiagramMLSimplified::Shape_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::shape_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::Shape)

@given(instance=DatadiagramMLSimplified::Shape_strategy)
def test_datadiagrammlsimplified::shape_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=DatadiagramMLSimplified::Shape_strategy)
def test_datadiagrammlsimplified::shape_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=DatadiagramMLSimplified::Shape_strategy)
def test_datadiagrammlsimplified::shape_textStyle_type(instance):
    assert isinstance(instance.textStyle, str)


@given(instance=DatadiagramMLSimplified::Shape_strategy)
def test_datadiagrammlsimplified::shape_textStyle_setter(instance):
    original = instance.textStyle
    instance.textStyle = original
    assert instance.textStyle == original

@given(instance=DatadiagramMLSimplified::Shape_strategy)
def test_datadiagrammlsimplified::shape_fillStyle_type(instance):
    assert isinstance(instance.fillStyle, str)


@given(instance=DatadiagramMLSimplified::Shape_strategy)
def test_datadiagrammlsimplified::shape_fillStyle_setter(instance):
    original = instance.fillStyle
    instance.fillStyle = original
    assert instance.fillStyle == original

@given(instance=DatadiagramMLSimplified::UniqueIdElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::uniqueidelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::UniqueIdElt)

@given(instance=DatadiagramMLSimplified::UniqueIdElt_strategy)
def test_datadiagrammlsimplified::uniqueidelt_UniqueID_type(instance):
    assert isinstance(instance.UniqueID, str)


@given(instance=DatadiagramMLSimplified::UniqueIdElt_strategy)
def test_datadiagrammlsimplified::uniqueidelt_UniqueID_setter(instance):
    original = instance.UniqueID
    instance.UniqueID = original
    assert instance.UniqueID == original

@given(instance=PagesCollection_strategy)
@settings(max_examples=50)
def test_pagescollection_instantiation(instance):
    assert isinstance(instance, PagesCollection)

@given(instance=MastersCollection_strategy)
@settings(max_examples=50)
def test_masterscollection_instantiation(instance):
    assert isinstance(instance, MastersCollection)

@given(instance=DatadiagramMLSimplified::VisioDocument_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::visiodocument_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::VisioDocument)

@given(instance=DatadiagramMLSimplified::CellType_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified::celltype_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified::CellType)

@given(instance=DatadiagramMLSimplified::CellType_strategy)
def test_datadiagrammlsimplified::celltype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=DatadiagramMLSimplified::CellType_strategy)
def test_datadiagrammlsimplified::celltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DatadiagramMLSimplified::CellType_strategy)
def test_datadiagrammlsimplified::celltype_formula_type(instance):
    assert isinstance(instance.formula, str)


@given(instance=DatadiagramMLSimplified::CellType_strategy)
def test_datadiagrammlsimplified::celltype_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=DatadiagramMLSimplified::CellType_strategy)
def test_datadiagrammlsimplified::celltype_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=DatadiagramMLSimplified::CellType_strategy)
def test_datadiagrammlsimplified::celltype_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=DatadiagramMLSimplified::CellType_strategy)
def test_datadiagrammlsimplified::celltype_err_type(instance):
    assert isinstance(instance.err, str)


@given(instance=DatadiagramMLSimplified::CellType_strategy)
def test_datadiagrammlsimplified::celltype_err_setter(instance):
    original = instance.err
    instance.err = original
    assert instance.err == original
