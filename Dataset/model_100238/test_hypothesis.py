import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DatadiagramMLSimplified_PageElt,
    Page,
    DatadiagramMLSimplified_PagesCollection,
    DatadiagramMLSimplified_MasterElt,
    ConnectsCollection,
    DatadiagramMLSimplified_Connect,
    Connect,
    NamedElt,
    IdentifiedElt,
    DatadiagramMLSimplified_Page,
    DatadiagramMLSimplified_MasterShortCut,
    MasterShortCut,
    Master,
    VisioDocument,
    DatadiagramMLSimplified_MastersCollection,
    Text,
    DatadiagramMLSimplified_TextElt,
    Icon,
    XYABCDElt,
    DatadiagramMLSimplified_Ellipse,
    XYABElt,
    DatadiagramMLSimplified_XYABCDElt,
    DatadiagramMLSimplified_InfiniteLine,
    TextElt,
    DatadiagramMLSimplified_StringElt,
    XYABCDEElt,
    DatadiagramMLSimplified_NURBSTo,
    DatadiagramMLSimplified_XYABCDEElt,
    DatadiagramMLSimplified_SplineStart,
    DatadiagramMLSimplified_EllipticalArcTo,
    Geom,
    XYElt,
    DatadiagramMLSimplified_MoveTo,
    DatadiagramMLSimplified_XYAElt,
    DatadiagramMLSimplified_LineTo,
    XYAElt,
    DatadiagramMLSimplified_SplineKnot,
    DatadiagramMLSimplified_XYABElt,
    DatadiagramMLSimplified_PolylineTo,
    DatadiagramMLSimplified_ArcTo,
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
    DatadiagramMLSimplified_ShapeElt,
    ShapeElt,
    DatadiagramMLSimplified_Text,
    CellType,
    DelElt,
    IXElt,
    DatadiagramMLSimplified_XYElt,
    DatadiagramMLSimplified_Geom,
    DatadiagramMLSimplified_DelElt,
    DatadiagramMLSimplified_IXElt,
    DatadiagramMLSimplified_IdentifiedElt,
    DatadiagramMLSimplified_NamedElt,
    PageElt,
    MasterElt,
    DatadiagramMLSimplified_ConnectsCollection,
    DatadiagramMLSimplified_Icon,
    DatadiagramMLSimplified_ShapesCollection,
    UniqueIdElt,
    DatadiagramMLSimplified_Master,
    Shape,
    DatadiagramMLSimplified_PageSheet,
    ShapesCollection,
    DatadiagramMLSimplified_Shape,
    DatadiagramMLSimplified_UniqueIdElt,
    PagesCollection,
    MastersCollection,
    DatadiagramMLSimplified_VisioDocument,
    DatadiagramMLSimplified_CellType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datadiagrammlsimplified_pageelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_PageElt)


def test_datadiagrammlsimplified_pageelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_PageElt.__init__)


def test_datadiagrammlsimplified_pageelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_PageElt.__init__)
    params = list(sig.parameters.keys())



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_pagescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_PagesCollection)


def test_datadiagrammlsimplified_pagescollection_constructor_exists():
    assert callable(DatadiagramMLSimplified_PagesCollection.__init__)


def test_datadiagrammlsimplified_pagescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_PagesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_masterelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_MasterElt)


def test_datadiagrammlsimplified_masterelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_MasterElt.__init__)


def test_datadiagrammlsimplified_masterelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_MasterElt.__init__)
    params = list(sig.parameters.keys())



def test_connectscollection_is_not_abstract():
    assert not inspect.isabstract(ConnectsCollection)


def test_connectscollection_constructor_exists():
    assert callable(ConnectsCollection.__init__)


def test_connectscollection_constructor_args():
    sig = inspect.signature(ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_connect_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_Connect)


def test_datadiagrammlsimplified_connect_constructor_exists():
    assert callable(DatadiagramMLSimplified_Connect.__init__)


def test_datadiagrammlsimplified_connect_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_Connect.__init__)
    params = list(sig.parameters.keys())
    assert "fromPart" in params, "Missing parameter 'fromPart'"
    assert "toSheet" in params, "Missing parameter 'toSheet'"
    assert "toCell" in params, "Missing parameter 'toCell'"
    assert "fromSheet" in params, "Missing parameter 'fromSheet'"
    assert "fromCell" in params, "Missing parameter 'fromCell'"
    assert "toPart" in params, "Missing parameter 'toPart'"

def test_datadiagrammlsimplified_connect_has_fromPart():
    assert hasattr(DatadiagramMLSimplified_Connect, "fromPart")
    descriptor = None
    for klass in DatadiagramMLSimplified_Connect.__mro__:
        if "fromPart" in klass.__dict__:
            descriptor = klass.__dict__["fromPart"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_connect_has_toSheet():
    assert hasattr(DatadiagramMLSimplified_Connect, "toSheet")
    descriptor = None
    for klass in DatadiagramMLSimplified_Connect.__mro__:
        if "toSheet" in klass.__dict__:
            descriptor = klass.__dict__["toSheet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_connect_has_toCell():
    assert hasattr(DatadiagramMLSimplified_Connect, "toCell")
    descriptor = None
    for klass in DatadiagramMLSimplified_Connect.__mro__:
        if "toCell" in klass.__dict__:
            descriptor = klass.__dict__["toCell"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_connect_has_fromSheet():
    assert hasattr(DatadiagramMLSimplified_Connect, "fromSheet")
    descriptor = None
    for klass in DatadiagramMLSimplified_Connect.__mro__:
        if "fromSheet" in klass.__dict__:
            descriptor = klass.__dict__["fromSheet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_connect_has_fromCell():
    assert hasattr(DatadiagramMLSimplified_Connect, "fromCell")
    descriptor = None
    for klass in DatadiagramMLSimplified_Connect.__mro__:
        if "fromCell" in klass.__dict__:
            descriptor = klass.__dict__["fromCell"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_connect_has_toPart():
    assert hasattr(DatadiagramMLSimplified_Connect, "toPart")
    descriptor = None
    for klass in DatadiagramMLSimplified_Connect.__mro__:
        if "toPart" in klass.__dict__:
            descriptor = klass.__dict__["toPart"]
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



def test_datadiagrammlsimplified_page_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_Page)


def test_datadiagrammlsimplified_page_constructor_exists():
    assert callable(DatadiagramMLSimplified_Page.__init__)


def test_datadiagrammlsimplified_page_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_Page.__init__)
    params = list(sig.parameters.keys())
    assert "backPage" in params, "Missing parameter 'backPage'"
    assert "reviewerID" in params, "Missing parameter 'reviewerID'"
    assert "background" in params, "Missing parameter 'background'"
    assert "viewScale" in params, "Missing parameter 'viewScale'"
    assert "ViewCenterY" in params, "Missing parameter 'ViewCenterY'"
    assert "viewCenterX" in params, "Missing parameter 'viewCenterX'"
    assert "associatedPage" in params, "Missing parameter 'associatedPage'"

def test_datadiagrammlsimplified_page_has_backPage():
    assert hasattr(DatadiagramMLSimplified_Page, "backPage")
    descriptor = None
    for klass in DatadiagramMLSimplified_Page.__mro__:
        if "backPage" in klass.__dict__:
            descriptor = klass.__dict__["backPage"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_page_has_reviewerID():
    assert hasattr(DatadiagramMLSimplified_Page, "reviewerID")
    descriptor = None
    for klass in DatadiagramMLSimplified_Page.__mro__:
        if "reviewerID" in klass.__dict__:
            descriptor = klass.__dict__["reviewerID"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_page_has_background():
    assert hasattr(DatadiagramMLSimplified_Page, "background")
    descriptor = None
    for klass in DatadiagramMLSimplified_Page.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_page_has_viewScale():
    assert hasattr(DatadiagramMLSimplified_Page, "viewScale")
    descriptor = None
    for klass in DatadiagramMLSimplified_Page.__mro__:
        if "viewScale" in klass.__dict__:
            descriptor = klass.__dict__["viewScale"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_page_has_ViewCenterY():
    assert hasattr(DatadiagramMLSimplified_Page, "ViewCenterY")
    descriptor = None
    for klass in DatadiagramMLSimplified_Page.__mro__:
        if "ViewCenterY" in klass.__dict__:
            descriptor = klass.__dict__["ViewCenterY"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_page_has_viewCenterX():
    assert hasattr(DatadiagramMLSimplified_Page, "viewCenterX")
    descriptor = None
    for klass in DatadiagramMLSimplified_Page.__mro__:
        if "viewCenterX" in klass.__dict__:
            descriptor = klass.__dict__["viewCenterX"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_page_has_associatedPage():
    assert hasattr(DatadiagramMLSimplified_Page, "associatedPage")
    descriptor = None
    for klass in DatadiagramMLSimplified_Page.__mro__:
        if "associatedPage" in klass.__dict__:
            descriptor = klass.__dict__["associatedPage"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlsimplified_mastershortcut_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_MasterShortCut)


def test_datadiagrammlsimplified_mastershortcut_constructor_exists():
    assert callable(DatadiagramMLSimplified_MasterShortCut.__init__)


def test_datadiagrammlsimplified_mastershortcut_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_MasterShortCut.__init__)
    params = list(sig.parameters.keys())
    assert "iconSize" in params, "Missing parameter 'iconSize'"
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "shortcutHelp" in params, "Missing parameter 'shortcutHelp'"
    assert "shortcutURL" in params, "Missing parameter 'shortcutURL'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"

def test_datadiagrammlsimplified_mastershortcut_has_iconSize():
    assert hasattr(DatadiagramMLSimplified_MasterShortCut, "iconSize")
    descriptor = None
    for klass in DatadiagramMLSimplified_MasterShortCut.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_mastershortcut_has_prompt():
    assert hasattr(DatadiagramMLSimplified_MasterShortCut, "prompt")
    descriptor = None
    for klass in DatadiagramMLSimplified_MasterShortCut.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_mastershortcut_has_shortcutHelp():
    assert hasattr(DatadiagramMLSimplified_MasterShortCut, "shortcutHelp")
    descriptor = None
    for klass in DatadiagramMLSimplified_MasterShortCut.__mro__:
        if "shortcutHelp" in klass.__dict__:
            descriptor = klass.__dict__["shortcutHelp"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_mastershortcut_has_shortcutURL():
    assert hasattr(DatadiagramMLSimplified_MasterShortCut, "shortcutURL")
    descriptor = None
    for klass in DatadiagramMLSimplified_MasterShortCut.__mro__:
        if "shortcutURL" in klass.__dict__:
            descriptor = klass.__dict__["shortcutURL"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_mastershortcut_has_alignName():
    assert hasattr(DatadiagramMLSimplified_MasterShortCut, "alignName")
    descriptor = None
    for klass in DatadiagramMLSimplified_MasterShortCut.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_mastershortcut_has_patternFlags():
    assert hasattr(DatadiagramMLSimplified_MasterShortCut, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLSimplified_MasterShortCut.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
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



def test_datadiagrammlsimplified_masterscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_MastersCollection)


def test_datadiagrammlsimplified_masterscollection_constructor_exists():
    assert callable(DatadiagramMLSimplified_MastersCollection.__init__)


def test_datadiagrammlsimplified_masterscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_MastersCollection.__init__)
    params = list(sig.parameters.keys())



def test_text_is_not_abstract():
    assert not inspect.isabstract(Text)


def test_text_constructor_exists():
    assert callable(Text.__init__)


def test_text_constructor_args():
    sig = inspect.signature(Text.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_textelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_TextElt)


def test_datadiagrammlsimplified_textelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_TextElt.__init__)


def test_datadiagrammlsimplified_textelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_TextElt.__init__)
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



def test_datadiagrammlsimplified_ellipse_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_Ellipse)


def test_datadiagrammlsimplified_ellipse_constructor_exists():
    assert callable(DatadiagramMLSimplified_Ellipse.__init__)


def test_datadiagrammlsimplified_ellipse_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_xyabelt_is_not_abstract():
    assert not inspect.isabstract(XYABElt)


def test_xyabelt_constructor_exists():
    assert callable(XYABElt.__init__)


def test_xyabelt_constructor_args():
    sig = inspect.signature(XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_XYABCDElt)


def test_datadiagrammlsimplified_xyabcdelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_XYABCDElt.__init__)


def test_datadiagrammlsimplified_xyabcdelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_infiniteline_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_InfiniteLine)


def test_datadiagrammlsimplified_infiniteline_constructor_exists():
    assert callable(DatadiagramMLSimplified_InfiniteLine.__init__)


def test_datadiagrammlsimplified_infiniteline_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_InfiniteLine.__init__)
    params = list(sig.parameters.keys())



def test_textelt_is_not_abstract():
    assert not inspect.isabstract(TextElt)


def test_textelt_constructor_exists():
    assert callable(TextElt.__init__)


def test_textelt_constructor_args():
    sig = inspect.signature(TextElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_stringelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_StringElt)


def test_datadiagrammlsimplified_stringelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_StringElt.__init__)


def test_datadiagrammlsimplified_stringelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_StringElt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammlsimplified_stringelt_has_value():
    assert hasattr(DatadiagramMLSimplified_StringElt, "value")
    descriptor = None
    for klass in DatadiagramMLSimplified_StringElt.__mro__:
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



def test_datadiagrammlsimplified_nurbsto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_NURBSTo)


def test_datadiagrammlsimplified_nurbsto_constructor_exists():
    assert callable(DatadiagramMLSimplified_NURBSTo.__init__)


def test_datadiagrammlsimplified_nurbsto_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_NURBSTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_xyabcdeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_XYABCDEElt)


def test_datadiagrammlsimplified_xyabcdeelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_XYABCDEElt.__init__)


def test_datadiagrammlsimplified_xyabcdeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_XYABCDEElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_splinestart_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_SplineStart)


def test_datadiagrammlsimplified_splinestart_constructor_exists():
    assert callable(DatadiagramMLSimplified_SplineStart.__init__)


def test_datadiagrammlsimplified_splinestart_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_SplineStart.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_ellipticalarcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_EllipticalArcTo)


def test_datadiagrammlsimplified_ellipticalarcto_constructor_exists():
    assert callable(DatadiagramMLSimplified_EllipticalArcTo.__init__)


def test_datadiagrammlsimplified_ellipticalarcto_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_EllipticalArcTo.__init__)
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



def test_datadiagrammlsimplified_moveto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_MoveTo)


def test_datadiagrammlsimplified_moveto_constructor_exists():
    assert callable(DatadiagramMLSimplified_MoveTo.__init__)


def test_datadiagrammlsimplified_moveto_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_xyaelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_XYAElt)


def test_datadiagrammlsimplified_xyaelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_XYAElt.__init__)


def test_datadiagrammlsimplified_xyaelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_lineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_LineTo)


def test_datadiagrammlsimplified_lineto_constructor_exists():
    assert callable(DatadiagramMLSimplified_LineTo.__init__)


def test_datadiagrammlsimplified_lineto_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_LineTo.__init__)
    params = list(sig.parameters.keys())



def test_xyaelt_is_not_abstract():
    assert not inspect.isabstract(XYAElt)


def test_xyaelt_constructor_exists():
    assert callable(XYAElt.__init__)


def test_xyaelt_constructor_args():
    sig = inspect.signature(XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_splineknot_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_SplineKnot)


def test_datadiagrammlsimplified_splineknot_constructor_exists():
    assert callable(DatadiagramMLSimplified_SplineKnot.__init__)


def test_datadiagrammlsimplified_splineknot_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_SplineKnot.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_xyabelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_XYABElt)


def test_datadiagrammlsimplified_xyabelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_XYABElt.__init__)


def test_datadiagrammlsimplified_xyabelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_polylineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_PolylineTo)


def test_datadiagrammlsimplified_polylineto_constructor_exists():
    assert callable(DatadiagramMLSimplified_PolylineTo.__init__)


def test_datadiagrammlsimplified_polylineto_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_PolylineTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_arcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_ArcTo)


def test_datadiagrammlsimplified_arcto_constructor_exists():
    assert callable(DatadiagramMLSimplified_ArcTo.__init__)


def test_datadiagrammlsimplified_arcto_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_ArcTo.__init__)
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



def test_datadiagrammlsimplified_shapeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_ShapeElt)


def test_datadiagrammlsimplified_shapeelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_ShapeElt.__init__)


def test_datadiagrammlsimplified_shapeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_shapeelt_is_not_abstract():
    assert not inspect.isabstract(ShapeElt)


def test_shapeelt_constructor_exists():
    assert callable(ShapeElt.__init__)


def test_shapeelt_constructor_args():
    sig = inspect.signature(ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_text_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_Text)


def test_datadiagrammlsimplified_text_constructor_exists():
    assert callable(DatadiagramMLSimplified_Text.__init__)


def test_datadiagrammlsimplified_text_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_Text.__init__)
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



def test_datadiagrammlsimplified_xyelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_XYElt)


def test_datadiagrammlsimplified_xyelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_XYElt.__init__)


def test_datadiagrammlsimplified_xyelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_XYElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_geom_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_Geom)


def test_datadiagrammlsimplified_geom_constructor_exists():
    assert callable(DatadiagramMLSimplified_Geom.__init__)


def test_datadiagrammlsimplified_geom_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_Geom.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_delelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_DelElt)


def test_datadiagrammlsimplified_delelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_DelElt.__init__)


def test_datadiagrammlsimplified_delelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_DelElt.__init__)
    params = list(sig.parameters.keys())
    assert "del_" in params, "Missing parameter 'del_'"

def test_datadiagrammlsimplified_delelt_has_del_():
    assert hasattr(DatadiagramMLSimplified_DelElt, "del_")
    descriptor = None
    for klass in DatadiagramMLSimplified_DelElt.__mro__:
        if "del_" in klass.__dict__:
            descriptor = klass.__dict__["del_"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlsimplified_ixelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_IXElt)


def test_datadiagrammlsimplified_ixelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_IXElt.__init__)


def test_datadiagrammlsimplified_ixelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_IXElt.__init__)
    params = list(sig.parameters.keys())
    assert "iX" in params, "Missing parameter 'iX'"

def test_datadiagrammlsimplified_ixelt_has_iX():
    assert hasattr(DatadiagramMLSimplified_IXElt, "iX")
    descriptor = None
    for klass in DatadiagramMLSimplified_IXElt.__mro__:
        if "iX" in klass.__dict__:
            descriptor = klass.__dict__["iX"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlsimplified_identifiedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_IdentifiedElt)


def test_datadiagrammlsimplified_identifiedelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_IdentifiedElt.__init__)


def test_datadiagrammlsimplified_identifiedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_IdentifiedElt.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_datadiagrammlsimplified_identifiedelt_has_ID():
    assert hasattr(DatadiagramMLSimplified_IdentifiedElt, "ID")
    descriptor = None
    for klass in DatadiagramMLSimplified_IdentifiedElt.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlsimplified_namedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_NamedElt)


def test_datadiagrammlsimplified_namedelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_NamedElt.__init__)


def test_datadiagrammlsimplified_namedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "nameU" in params, "Missing parameter 'nameU'"
    assert "name" in params, "Missing parameter 'name'"

def test_datadiagrammlsimplified_namedelt_has_nameU():
    assert hasattr(DatadiagramMLSimplified_NamedElt, "nameU")
    descriptor = None
    for klass in DatadiagramMLSimplified_NamedElt.__mro__:
        if "nameU" in klass.__dict__:
            descriptor = klass.__dict__["nameU"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_namedelt_has_name():
    assert hasattr(DatadiagramMLSimplified_NamedElt, "name")
    descriptor = None
    for klass in DatadiagramMLSimplified_NamedElt.__mro__:
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



def test_datadiagrammlsimplified_connectscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_ConnectsCollection)


def test_datadiagrammlsimplified_connectscollection_constructor_exists():
    assert callable(DatadiagramMLSimplified_ConnectsCollection.__init__)


def test_datadiagrammlsimplified_connectscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_icon_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_Icon)


def test_datadiagrammlsimplified_icon_constructor_exists():
    assert callable(DatadiagramMLSimplified_Icon.__init__)


def test_datadiagrammlsimplified_icon_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_Icon.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammlsimplified_icon_has_value():
    assert hasattr(DatadiagramMLSimplified_Icon, "value")
    descriptor = None
    for klass in DatadiagramMLSimplified_Icon.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlsimplified_shapescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_ShapesCollection)


def test_datadiagrammlsimplified_shapescollection_constructor_exists():
    assert callable(DatadiagramMLSimplified_ShapesCollection.__init__)


def test_datadiagrammlsimplified_shapescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(UniqueIdElt)


def test_uniqueidelt_constructor_exists():
    assert callable(UniqueIdElt.__init__)


def test_uniqueidelt_constructor_args():
    sig = inspect.signature(UniqueIdElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_master_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_Master)


def test_datadiagrammlsimplified_master_constructor_exists():
    assert callable(DatadiagramMLSimplified_Master.__init__)


def test_datadiagrammlsimplified_master_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_Master.__init__)
    params = list(sig.parameters.keys())
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "matchByName" in params, "Missing parameter 'matchByName'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "baseID" in params, "Missing parameter 'baseID'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"
    assert "iconUpdate" in params, "Missing parameter 'iconUpdate'"
    assert "alignName" in params, "Missing parameter 'alignName'"

def test_datadiagrammlsimplified_master_has_prompt():
    assert hasattr(DatadiagramMLSimplified_Master, "prompt")
    descriptor = None
    for klass in DatadiagramMLSimplified_Master.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_master_has_matchByName():
    assert hasattr(DatadiagramMLSimplified_Master, "matchByName")
    descriptor = None
    for klass in DatadiagramMLSimplified_Master.__mro__:
        if "matchByName" in klass.__dict__:
            descriptor = klass.__dict__["matchByName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_master_has_hidden():
    assert hasattr(DatadiagramMLSimplified_Master, "hidden")
    descriptor = None
    for klass in DatadiagramMLSimplified_Master.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_master_has_baseID():
    assert hasattr(DatadiagramMLSimplified_Master, "baseID")
    descriptor = None
    for klass in DatadiagramMLSimplified_Master.__mro__:
        if "baseID" in klass.__dict__:
            descriptor = klass.__dict__["baseID"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_master_has_patternFlags():
    assert hasattr(DatadiagramMLSimplified_Master, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLSimplified_Master.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_master_has_iconSize():
    assert hasattr(DatadiagramMLSimplified_Master, "iconSize")
    descriptor = None
    for klass in DatadiagramMLSimplified_Master.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_master_has_iconUpdate():
    assert hasattr(DatadiagramMLSimplified_Master, "iconUpdate")
    descriptor = None
    for klass in DatadiagramMLSimplified_Master.__mro__:
        if "iconUpdate" in klass.__dict__:
            descriptor = klass.__dict__["iconUpdate"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_master_has_alignName():
    assert hasattr(DatadiagramMLSimplified_Master, "alignName")
    descriptor = None
    for klass in DatadiagramMLSimplified_Master.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_pagesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_PageSheet)


def test_datadiagrammlsimplified_pagesheet_constructor_exists():
    assert callable(DatadiagramMLSimplified_PageSheet.__init__)


def test_datadiagrammlsimplified_pagesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_PageSheet.__init__)
    params = list(sig.parameters.keys())



def test_shapescollection_is_not_abstract():
    assert not inspect.isabstract(ShapesCollection)


def test_shapescollection_constructor_exists():
    assert callable(ShapesCollection.__init__)


def test_shapescollection_constructor_args():
    sig = inspect.signature(ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_shape_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_Shape)


def test_datadiagrammlsimplified_shape_constructor_exists():
    assert callable(DatadiagramMLSimplified_Shape.__init__)


def test_datadiagrammlsimplified_shape_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "textStyle" in params, "Missing parameter 'textStyle'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "fillStyle" in params, "Missing parameter 'fillStyle'"

def test_datadiagrammlsimplified_shape_has_textStyle():
    assert hasattr(DatadiagramMLSimplified_Shape, "textStyle")
    descriptor = None
    for klass in DatadiagramMLSimplified_Shape.__mro__:
        if "textStyle" in klass.__dict__:
            descriptor = klass.__dict__["textStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_shape_has_lineStyle():
    assert hasattr(DatadiagramMLSimplified_Shape, "lineStyle")
    descriptor = None
    for klass in DatadiagramMLSimplified_Shape.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_shape_has_fillStyle():
    assert hasattr(DatadiagramMLSimplified_Shape, "fillStyle")
    descriptor = None
    for klass in DatadiagramMLSimplified_Shape.__mro__:
        if "fillStyle" in klass.__dict__:
            descriptor = klass.__dict__["fillStyle"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlsimplified_uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_UniqueIdElt)


def test_datadiagrammlsimplified_uniqueidelt_constructor_exists():
    assert callable(DatadiagramMLSimplified_UniqueIdElt.__init__)


def test_datadiagrammlsimplified_uniqueidelt_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_UniqueIdElt.__init__)
    params = list(sig.parameters.keys())
    assert "UniqueID" in params, "Missing parameter 'UniqueID'"

def test_datadiagrammlsimplified_uniqueidelt_has_UniqueID():
    assert hasattr(DatadiagramMLSimplified_UniqueIdElt, "UniqueID")
    descriptor = None
    for klass in DatadiagramMLSimplified_UniqueIdElt.__mro__:
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



def test_datadiagrammlsimplified_visiodocument_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_VisioDocument)


def test_datadiagrammlsimplified_visiodocument_constructor_exists():
    assert callable(DatadiagramMLSimplified_VisioDocument.__init__)


def test_datadiagrammlsimplified_visiodocument_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_VisioDocument.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlsimplified_celltype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLSimplified_CellType)


def test_datadiagrammlsimplified_celltype_constructor_exists():
    assert callable(DatadiagramMLSimplified_CellType.__init__)


def test_datadiagrammlsimplified_celltype_constructor_args():
    sig = inspect.signature(DatadiagramMLSimplified_CellType.__init__)
    params = list(sig.parameters.keys())
    assert "formula" in params, "Missing parameter 'formula'"
    assert "value" in params, "Missing parameter 'value'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "err" in params, "Missing parameter 'err'"

def test_datadiagrammlsimplified_celltype_has_formula():
    assert hasattr(DatadiagramMLSimplified_CellType, "formula")
    descriptor = None
    for klass in DatadiagramMLSimplified_CellType.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_celltype_has_value():
    assert hasattr(DatadiagramMLSimplified_CellType, "value")
    descriptor = None
    for klass in DatadiagramMLSimplified_CellType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_celltype_has_unit():
    assert hasattr(DatadiagramMLSimplified_CellType, "unit")
    descriptor = None
    for klass in DatadiagramMLSimplified_CellType.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlsimplified_celltype_has_err():
    assert hasattr(DatadiagramMLSimplified_CellType, "err")
    descriptor = None
    for klass in DatadiagramMLSimplified_CellType.__mro__:
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
DatadiagramMLSimplified_PageElt_strategy = st.builds(
    DatadiagramMLSimplified_PageElt,
)
Page_strategy = st.builds(
    Page,
)
DatadiagramMLSimplified_PagesCollection_strategy = st.builds(
    DatadiagramMLSimplified_PagesCollection,
)
DatadiagramMLSimplified_MasterElt_strategy = st.builds(
    DatadiagramMLSimplified_MasterElt,
)
ConnectsCollection_strategy = st.builds(
    ConnectsCollection,
)
DatadiagramMLSimplified_Connect_strategy = st.builds(
    DatadiagramMLSimplified_Connect,
    fromPart=
        safe_text,
    toSheet=
        safe_text,
    toCell=
        safe_text,
    fromSheet=
        safe_text,
    fromCell=
        safe_text,
    toPart=
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
DatadiagramMLSimplified_Page_strategy = st.builds(
    DatadiagramMLSimplified_Page,
    backPage=
        safe_text,
    reviewerID=
        safe_text,
    background=
        safe_text,
    viewScale=
        safe_text,
    ViewCenterY=
        safe_text,
    viewCenterX=
        safe_text,
    associatedPage=
        safe_text
)
DatadiagramMLSimplified_MasterShortCut_strategy = st.builds(
    DatadiagramMLSimplified_MasterShortCut,
    iconSize=
        safe_text,
    prompt=
        safe_text,
    shortcutHelp=
        safe_text,
    shortcutURL=
        safe_text,
    alignName=
        safe_text,
    patternFlags=
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
DatadiagramMLSimplified_MastersCollection_strategy = st.builds(
    DatadiagramMLSimplified_MastersCollection,
)
Text_strategy = st.builds(
    Text,
)
DatadiagramMLSimplified_TextElt_strategy = st.builds(
    DatadiagramMLSimplified_TextElt,
)
Icon_strategy = st.builds(
    Icon,
)
XYABCDElt_strategy = st.builds(
    XYABCDElt,
)
DatadiagramMLSimplified_Ellipse_strategy = st.builds(
    DatadiagramMLSimplified_Ellipse,
)
XYABElt_strategy = st.builds(
    XYABElt,
)
DatadiagramMLSimplified_XYABCDElt_strategy = st.builds(
    DatadiagramMLSimplified_XYABCDElt,
)
DatadiagramMLSimplified_InfiniteLine_strategy = st.builds(
    DatadiagramMLSimplified_InfiniteLine,
)
TextElt_strategy = st.builds(
    TextElt,
)
DatadiagramMLSimplified_StringElt_strategy = st.builds(
    DatadiagramMLSimplified_StringElt,
    value=
        safe_text
)
XYABCDEElt_strategy = st.builds(
    XYABCDEElt,
)
DatadiagramMLSimplified_NURBSTo_strategy = st.builds(
    DatadiagramMLSimplified_NURBSTo,
)
DatadiagramMLSimplified_XYABCDEElt_strategy = st.builds(
    DatadiagramMLSimplified_XYABCDEElt,
)
DatadiagramMLSimplified_SplineStart_strategy = st.builds(
    DatadiagramMLSimplified_SplineStart,
)
DatadiagramMLSimplified_EllipticalArcTo_strategy = st.builds(
    DatadiagramMLSimplified_EllipticalArcTo,
)
Geom_strategy = st.builds(
    Geom,
)
XYElt_strategy = st.builds(
    XYElt,
)
DatadiagramMLSimplified_MoveTo_strategy = st.builds(
    DatadiagramMLSimplified_MoveTo,
)
DatadiagramMLSimplified_XYAElt_strategy = st.builds(
    DatadiagramMLSimplified_XYAElt,
)
DatadiagramMLSimplified_LineTo_strategy = st.builds(
    DatadiagramMLSimplified_LineTo,
)
XYAElt_strategy = st.builds(
    XYAElt,
)
DatadiagramMLSimplified_SplineKnot_strategy = st.builds(
    DatadiagramMLSimplified_SplineKnot,
)
DatadiagramMLSimplified_XYABElt_strategy = st.builds(
    DatadiagramMLSimplified_XYABElt,
)
DatadiagramMLSimplified_PolylineTo_strategy = st.builds(
    DatadiagramMLSimplified_PolylineTo,
)
DatadiagramMLSimplified_ArcTo_strategy = st.builds(
    DatadiagramMLSimplified_ArcTo,
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
DatadiagramMLSimplified_ShapeElt_strategy = st.builds(
    DatadiagramMLSimplified_ShapeElt,
)
ShapeElt_strategy = st.builds(
    ShapeElt,
)
DatadiagramMLSimplified_Text_strategy = st.builds(
    DatadiagramMLSimplified_Text,
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
DatadiagramMLSimplified_XYElt_strategy = st.builds(
    DatadiagramMLSimplified_XYElt,
)
DatadiagramMLSimplified_Geom_strategy = st.builds(
    DatadiagramMLSimplified_Geom,
)
DatadiagramMLSimplified_DelElt_strategy = st.builds(
    DatadiagramMLSimplified_DelElt,
    del_=
        safe_text
)
DatadiagramMLSimplified_IXElt_strategy = st.builds(
    DatadiagramMLSimplified_IXElt,
    iX=
        safe_text
)
DatadiagramMLSimplified_IdentifiedElt_strategy = st.builds(
    DatadiagramMLSimplified_IdentifiedElt,
    ID=
        safe_text
)
DatadiagramMLSimplified_NamedElt_strategy = st.builds(
    DatadiagramMLSimplified_NamedElt,
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
DatadiagramMLSimplified_ConnectsCollection_strategy = st.builds(
    DatadiagramMLSimplified_ConnectsCollection,
)
DatadiagramMLSimplified_Icon_strategy = st.builds(
    DatadiagramMLSimplified_Icon,
    value=
        safe_text
)
DatadiagramMLSimplified_ShapesCollection_strategy = st.builds(
    DatadiagramMLSimplified_ShapesCollection,
)
UniqueIdElt_strategy = st.builds(
    UniqueIdElt,
)
DatadiagramMLSimplified_Master_strategy = st.builds(
    DatadiagramMLSimplified_Master,
    prompt=
        safe_text,
    matchByName=
        safe_text,
    hidden=
        safe_text,
    baseID=
        safe_text,
    patternFlags=
        safe_text,
    iconSize=
        safe_text,
    iconUpdate=
        safe_text,
    alignName=
        safe_text
)
Shape_strategy = st.builds(
    Shape,
)
DatadiagramMLSimplified_PageSheet_strategy = st.builds(
    DatadiagramMLSimplified_PageSheet,
)
ShapesCollection_strategy = st.builds(
    ShapesCollection,
)
DatadiagramMLSimplified_Shape_strategy = st.builds(
    DatadiagramMLSimplified_Shape,
    textStyle=
        safe_text,
    lineStyle=
        safe_text,
    fillStyle=
        safe_text
)
DatadiagramMLSimplified_UniqueIdElt_strategy = st.builds(
    DatadiagramMLSimplified_UniqueIdElt,
    UniqueID=
        safe_text
)
PagesCollection_strategy = st.builds(
    PagesCollection,
)
MastersCollection_strategy = st.builds(
    MastersCollection,
)
DatadiagramMLSimplified_VisioDocument_strategy = st.builds(
    DatadiagramMLSimplified_VisioDocument,
)
DatadiagramMLSimplified_CellType_strategy = st.builds(
    DatadiagramMLSimplified_CellType,
    formula=
        safe_text,
    value=
        safe_text,
    unit=
        safe_text,
    err=
        safe_text
)

@given(instance=DatadiagramMLSimplified_PageElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_pageelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_PageElt)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=DatadiagramMLSimplified_PagesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_pagescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_PagesCollection)

@given(instance=DatadiagramMLSimplified_MasterElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_masterelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_MasterElt)

@given(instance=ConnectsCollection_strategy)
@settings(max_examples=50)
def test_connectscollection_instantiation(instance):
    assert isinstance(instance, ConnectsCollection)

@given(instance=DatadiagramMLSimplified_Connect_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_connect_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_Connect)



@given(instance=DatadiagramMLSimplified_Connect_strategy)
def test_datadiagrammlsimplified_connect_fromPart_setter(instance):
    original = instance.fromPart
    instance.fromPart = original
    assert instance.fromPart == original



@given(instance=DatadiagramMLSimplified_Connect_strategy)
def test_datadiagrammlsimplified_connect_toSheet_setter(instance):
    original = instance.toSheet
    instance.toSheet = original
    assert instance.toSheet == original



@given(instance=DatadiagramMLSimplified_Connect_strategy)
def test_datadiagrammlsimplified_connect_toCell_setter(instance):
    original = instance.toCell
    instance.toCell = original
    assert instance.toCell == original



@given(instance=DatadiagramMLSimplified_Connect_strategy)
def test_datadiagrammlsimplified_connect_fromSheet_setter(instance):
    original = instance.fromSheet
    instance.fromSheet = original
    assert instance.fromSheet == original



@given(instance=DatadiagramMLSimplified_Connect_strategy)
def test_datadiagrammlsimplified_connect_fromCell_setter(instance):
    original = instance.fromCell
    instance.fromCell = original
    assert instance.fromCell == original



@given(instance=DatadiagramMLSimplified_Connect_strategy)
def test_datadiagrammlsimplified_connect_toPart_setter(instance):
    original = instance.toPart
    instance.toPart = original
    assert instance.toPart == original

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

@given(instance=DatadiagramMLSimplified_Page_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_page_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_Page)



@given(instance=DatadiagramMLSimplified_Page_strategy)
def test_datadiagrammlsimplified_page_backPage_setter(instance):
    original = instance.backPage
    instance.backPage = original
    assert instance.backPage == original



@given(instance=DatadiagramMLSimplified_Page_strategy)
def test_datadiagrammlsimplified_page_reviewerID_setter(instance):
    original = instance.reviewerID
    instance.reviewerID = original
    assert instance.reviewerID == original



@given(instance=DatadiagramMLSimplified_Page_strategy)
def test_datadiagrammlsimplified_page_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=DatadiagramMLSimplified_Page_strategy)
def test_datadiagrammlsimplified_page_viewScale_setter(instance):
    original = instance.viewScale
    instance.viewScale = original
    assert instance.viewScale == original



@given(instance=DatadiagramMLSimplified_Page_strategy)
def test_datadiagrammlsimplified_page_ViewCenterY_setter(instance):
    original = instance.ViewCenterY
    instance.ViewCenterY = original
    assert instance.ViewCenterY == original



@given(instance=DatadiagramMLSimplified_Page_strategy)
def test_datadiagrammlsimplified_page_viewCenterX_setter(instance):
    original = instance.viewCenterX
    instance.viewCenterX = original
    assert instance.viewCenterX == original



@given(instance=DatadiagramMLSimplified_Page_strategy)
def test_datadiagrammlsimplified_page_associatedPage_setter(instance):
    original = instance.associatedPage
    instance.associatedPage = original
    assert instance.associatedPage == original

@given(instance=DatadiagramMLSimplified_MasterShortCut_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_mastershortcut_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_MasterShortCut)



@given(instance=DatadiagramMLSimplified_MasterShortCut_strategy)
def test_datadiagrammlsimplified_mastershortcut_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original



@given(instance=DatadiagramMLSimplified_MasterShortCut_strategy)
def test_datadiagrammlsimplified_mastershortcut_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original



@given(instance=DatadiagramMLSimplified_MasterShortCut_strategy)
def test_datadiagrammlsimplified_mastershortcut_shortcutHelp_setter(instance):
    original = instance.shortcutHelp
    instance.shortcutHelp = original
    assert instance.shortcutHelp == original



@given(instance=DatadiagramMLSimplified_MasterShortCut_strategy)
def test_datadiagrammlsimplified_mastershortcut_shortcutURL_setter(instance):
    original = instance.shortcutURL
    instance.shortcutURL = original
    assert instance.shortcutURL == original



@given(instance=DatadiagramMLSimplified_MasterShortCut_strategy)
def test_datadiagrammlsimplified_mastershortcut_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original



@given(instance=DatadiagramMLSimplified_MasterShortCut_strategy)
def test_datadiagrammlsimplified_mastershortcut_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original

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

@given(instance=DatadiagramMLSimplified_MastersCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_masterscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_MastersCollection)

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=DatadiagramMLSimplified_TextElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_textelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_TextElt)

@given(instance=Icon_strategy)
@settings(max_examples=50)
def test_icon_instantiation(instance):
    assert isinstance(instance, Icon)

@given(instance=XYABCDElt_strategy)
@settings(max_examples=50)
def test_xyabcdelt_instantiation(instance):
    assert isinstance(instance, XYABCDElt)

@given(instance=DatadiagramMLSimplified_Ellipse_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_ellipse_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_Ellipse)

@given(instance=XYABElt_strategy)
@settings(max_examples=50)
def test_xyabelt_instantiation(instance):
    assert isinstance(instance, XYABElt)

@given(instance=DatadiagramMLSimplified_XYABCDElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_xyabcdelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_XYABCDElt)

@given(instance=DatadiagramMLSimplified_InfiniteLine_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_infiniteline_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_InfiniteLine)

@given(instance=TextElt_strategy)
@settings(max_examples=50)
def test_textelt_instantiation(instance):
    assert isinstance(instance, TextElt)

@given(instance=DatadiagramMLSimplified_StringElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_stringelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_StringElt)



@given(instance=DatadiagramMLSimplified_StringElt_strategy)
def test_datadiagrammlsimplified_stringelt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=XYABCDEElt_strategy)
@settings(max_examples=50)
def test_xyabcdeelt_instantiation(instance):
    assert isinstance(instance, XYABCDEElt)

@given(instance=DatadiagramMLSimplified_NURBSTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_nurbsto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_NURBSTo)

@given(instance=DatadiagramMLSimplified_XYABCDEElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_xyabcdeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_XYABCDEElt)

@given(instance=DatadiagramMLSimplified_SplineStart_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_splinestart_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_SplineStart)

@given(instance=DatadiagramMLSimplified_EllipticalArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_ellipticalarcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_EllipticalArcTo)

@given(instance=Geom_strategy)
@settings(max_examples=50)
def test_geom_instantiation(instance):
    assert isinstance(instance, Geom)

@given(instance=XYElt_strategy)
@settings(max_examples=50)
def test_xyelt_instantiation(instance):
    assert isinstance(instance, XYElt)

@given(instance=DatadiagramMLSimplified_MoveTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_moveto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_MoveTo)

@given(instance=DatadiagramMLSimplified_XYAElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_xyaelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_XYAElt)

@given(instance=DatadiagramMLSimplified_LineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_lineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_LineTo)

@given(instance=XYAElt_strategy)
@settings(max_examples=50)
def test_xyaelt_instantiation(instance):
    assert isinstance(instance, XYAElt)

@given(instance=DatadiagramMLSimplified_SplineKnot_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_splineknot_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_SplineKnot)

@given(instance=DatadiagramMLSimplified_XYABElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_xyabelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_XYABElt)

@given(instance=DatadiagramMLSimplified_PolylineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_polylineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_PolylineTo)

@given(instance=DatadiagramMLSimplified_ArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_arcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_ArcTo)

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

@given(instance=DatadiagramMLSimplified_ShapeElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_shapeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_ShapeElt)

@given(instance=ShapeElt_strategy)
@settings(max_examples=50)
def test_shapeelt_instantiation(instance):
    assert isinstance(instance, ShapeElt)

@given(instance=DatadiagramMLSimplified_Text_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_text_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_Text)

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

@given(instance=DatadiagramMLSimplified_XYElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_xyelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_XYElt)

@given(instance=DatadiagramMLSimplified_Geom_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_geom_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_Geom)

@given(instance=DatadiagramMLSimplified_DelElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_delelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_DelElt)



@given(instance=DatadiagramMLSimplified_DelElt_strategy)
def test_datadiagrammlsimplified_delelt_del__setter(instance):
    original = instance.del_
    instance.del_ = original
    assert instance.del_ == original

@given(instance=DatadiagramMLSimplified_IXElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_ixelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_IXElt)



@given(instance=DatadiagramMLSimplified_IXElt_strategy)
def test_datadiagrammlsimplified_ixelt_iX_setter(instance):
    original = instance.iX
    instance.iX = original
    assert instance.iX == original

@given(instance=DatadiagramMLSimplified_IdentifiedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_identifiedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_IdentifiedElt)



@given(instance=DatadiagramMLSimplified_IdentifiedElt_strategy)
def test_datadiagrammlsimplified_identifiedelt_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=DatadiagramMLSimplified_NamedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_namedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_NamedElt)



@given(instance=DatadiagramMLSimplified_NamedElt_strategy)
def test_datadiagrammlsimplified_namedelt_nameU_setter(instance):
    original = instance.nameU
    instance.nameU = original
    assert instance.nameU == original



@given(instance=DatadiagramMLSimplified_NamedElt_strategy)
def test_datadiagrammlsimplified_namedelt_name_setter(instance):
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

@given(instance=DatadiagramMLSimplified_ConnectsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_connectscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_ConnectsCollection)

@given(instance=DatadiagramMLSimplified_Icon_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_icon_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_Icon)



@given(instance=DatadiagramMLSimplified_Icon_strategy)
def test_datadiagrammlsimplified_icon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DatadiagramMLSimplified_ShapesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_shapescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_ShapesCollection)

@given(instance=UniqueIdElt_strategy)
@settings(max_examples=50)
def test_uniqueidelt_instantiation(instance):
    assert isinstance(instance, UniqueIdElt)

@given(instance=DatadiagramMLSimplified_Master_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_master_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_Master)



@given(instance=DatadiagramMLSimplified_Master_strategy)
def test_datadiagrammlsimplified_master_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original



@given(instance=DatadiagramMLSimplified_Master_strategy)
def test_datadiagrammlsimplified_master_matchByName_setter(instance):
    original = instance.matchByName
    instance.matchByName = original
    assert instance.matchByName == original



@given(instance=DatadiagramMLSimplified_Master_strategy)
def test_datadiagrammlsimplified_master_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original



@given(instance=DatadiagramMLSimplified_Master_strategy)
def test_datadiagrammlsimplified_master_baseID_setter(instance):
    original = instance.baseID
    instance.baseID = original
    assert instance.baseID == original



@given(instance=DatadiagramMLSimplified_Master_strategy)
def test_datadiagrammlsimplified_master_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original



@given(instance=DatadiagramMLSimplified_Master_strategy)
def test_datadiagrammlsimplified_master_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original



@given(instance=DatadiagramMLSimplified_Master_strategy)
def test_datadiagrammlsimplified_master_iconUpdate_setter(instance):
    original = instance.iconUpdate
    instance.iconUpdate = original
    assert instance.iconUpdate == original



@given(instance=DatadiagramMLSimplified_Master_strategy)
def test_datadiagrammlsimplified_master_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=DatadiagramMLSimplified_PageSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_pagesheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_PageSheet)

@given(instance=ShapesCollection_strategy)
@settings(max_examples=50)
def test_shapescollection_instantiation(instance):
    assert isinstance(instance, ShapesCollection)

@given(instance=DatadiagramMLSimplified_Shape_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_shape_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_Shape)



@given(instance=DatadiagramMLSimplified_Shape_strategy)
def test_datadiagrammlsimplified_shape_textStyle_setter(instance):
    original = instance.textStyle
    instance.textStyle = original
    assert instance.textStyle == original



@given(instance=DatadiagramMLSimplified_Shape_strategy)
def test_datadiagrammlsimplified_shape_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original



@given(instance=DatadiagramMLSimplified_Shape_strategy)
def test_datadiagrammlsimplified_shape_fillStyle_setter(instance):
    original = instance.fillStyle
    instance.fillStyle = original
    assert instance.fillStyle == original

@given(instance=DatadiagramMLSimplified_UniqueIdElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_uniqueidelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_UniqueIdElt)



@given(instance=DatadiagramMLSimplified_UniqueIdElt_strategy)
def test_datadiagrammlsimplified_uniqueidelt_UniqueID_setter(instance):
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

@given(instance=DatadiagramMLSimplified_VisioDocument_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_visiodocument_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_VisioDocument)

@given(instance=DatadiagramMLSimplified_CellType_strategy)
@settings(max_examples=50)
def test_datadiagrammlsimplified_celltype_instantiation(instance):
    assert isinstance(instance, DatadiagramMLSimplified_CellType)



@given(instance=DatadiagramMLSimplified_CellType_strategy)
def test_datadiagrammlsimplified_celltype_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original



@given(instance=DatadiagramMLSimplified_CellType_strategy)
def test_datadiagrammlsimplified_celltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=DatadiagramMLSimplified_CellType_strategy)
def test_datadiagrammlsimplified_celltype_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=DatadiagramMLSimplified_CellType_strategy)
def test_datadiagrammlsimplified_celltype_err_setter(instance):
    original = instance.err
    instance.err = original
    assert instance.err == original
