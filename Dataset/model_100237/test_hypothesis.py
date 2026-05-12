import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ConnectsCollection,
    DatadiagramMLBasicDef_Connect,
    Connect,
    DatadiagramMLBasicDef_PagesCollection,
    DatadiagramMLBasicDef_MasterElt,
    Icon,
    DatadiagramMLBasicDef_MastersCollection,
    Text,
    DatadiagramMLBasicDef_TextElt,
    DatadiagramMLBasicDef_HeaderFooter,
    DatadiagramMLBasicDef_EventList,
    DatadiagramMLBasicDef_WindowsInfo,
    DatadiagramMLBasicDef_FaceNamesTable,
    DatadiagramMLBasicDef_FontsTable,
    DatadiagramMLBasicDef_PrintSetup,
    DatadiagramMLBasicDef_SolutionXML,
    Page,
    DatadiagramMLBasicDef_ColorsTable,
    DatadiagramMLBasicDef_DocumentSettingsElt,
    DatadiagramMLBasicDef_PageElt,
    MasterShortCut,
    Master,
    XYABCDElt,
    DatadiagramMLBasicDef_SplineStart,
    DatadiagramMLBasicDef_EllipticalArcTo,
    DatadiagramMLBasicDef_Ellipse,
    TextElt,
    DatadiagramMLBasicDef_StringElt,
    XYABCDEElt,
    DatadiagramMLBasicDef_NURBSTo,
    DatadiagramMLBasicDef_XYABCDEElt,
    XYAElt,
    DatadiagramMLBasicDef_SplineKnot,
    DatadiagramMLBasicDef_PolylineTo,
    DatadiagramMLBasicDef_ArcTo,
    XYABElt,
    DatadiagramMLBasicDef_XYABCDElt,
    DatadiagramMLBasicDef_InfiniteLine,
    DatadiagramMLBasicDef_XYABElt,
    NURBSTo,
    SplineStart,
    EllipticalArcTo,
    Ellipse,
    Geom,
    XYElt,
    DatadiagramMLBasicDef_MoveTo,
    DatadiagramMLBasicDef_XYAElt,
    DatadiagramMLBasicDef_LineTo,
    LineTo,
    CellType,
    DelElt,
    IXElt,
    DatadiagramMLBasicDef_XYElt,
    DatadiagramMLBasicDef_DelElt,
    DatadiagramMLBasicDef_IXElt,
    InfiniteLine,
    PolylineTo,
    SplineKnot,
    ArcTo,
    MoveTo,
    DatadiagramMLBasicDef_UniqueIdElt,
    DatadiagramMLBasicDef_IdentifiedElt,
    DatadiagramMLBasicDef_NamedElt,
    PageElt,
    MasterElt,
    DatadiagramMLBasicDef_ConnectsCollection,
    DatadiagramMLBasicDef_ShapesCollection,
    DatadiagramMLBasicDef_Icon,
    UniqueIdElt,
    PageSheet,
    NamedElt,
    DatadiagramMLBasicDef_DocumentSheet,
    DatadiagramMLBasicDef_ShapeElt,
    ShapeElt,
    DatadiagramMLBasicDef_Text,
    DatadiagramMLBasicDef_Geom,
    ShapesCollection,
    DatadiagramMLBasicDef_Shape,
    DatadiagramMLBasicDef_EmailRoutingData,
    DatadiagramMLBasicDef_VBProjectData,
    DatadiagramMLBasicDef_CustomProperty,
    CustomProperty,
    DatadiagramMLBasicDef_CustomPropertiesCollection,
    IdentifiedElt,
    DatadiagramMLBasicDef_Page,
    DatadiagramMLBasicDef_MasterShortCut,
    DatadiagramMLBasicDef_Master,
    Shape,
    DatadiagramMLBasicDef_PageSheet,
    DatadiagramMLBasicDef_StyleSheet,
    StyleSheet,
    DatadiagramMLBasicDef_StyleSheetsCollection,
    VisioDocument,
    DatadiagramMLBasicDef_DocumentPropertiesCollection,
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
    DatadiagramMLBasicDef_DateTimeType,
    DatadiagramMLBasicDef_VisioDocument,
    DatadiagramMLBasicDef_CellType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_connectscollection_is_not_abstract():
    assert not inspect.isabstract(ConnectsCollection)


def test_connectscollection_constructor_exists():
    assert callable(ConnectsCollection.__init__)


def test_connectscollection_constructor_args():
    sig = inspect.signature(ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_connect_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_Connect)


def test_datadiagrammlbasicdef_connect_constructor_exists():
    assert callable(DatadiagramMLBasicDef_Connect.__init__)


def test_datadiagrammlbasicdef_connect_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_Connect.__init__)
    params = list(sig.parameters.keys())
    assert "fromPart" in params, "Missing parameter 'fromPart'"
    assert "toSheet" in params, "Missing parameter 'toSheet'"
    assert "fromCell" in params, "Missing parameter 'fromCell'"
    assert "toPart" in params, "Missing parameter 'toPart'"
    assert "toCell" in params, "Missing parameter 'toCell'"
    assert "fromSheet" in params, "Missing parameter 'fromSheet'"

def test_datadiagrammlbasicdef_connect_has_fromPart():
    assert hasattr(DatadiagramMLBasicDef_Connect, "fromPart")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Connect.__mro__:
        if "fromPart" in klass.__dict__:
            descriptor = klass.__dict__["fromPart"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_connect_has_toSheet():
    assert hasattr(DatadiagramMLBasicDef_Connect, "toSheet")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Connect.__mro__:
        if "toSheet" in klass.__dict__:
            descriptor = klass.__dict__["toSheet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_connect_has_fromCell():
    assert hasattr(DatadiagramMLBasicDef_Connect, "fromCell")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Connect.__mro__:
        if "fromCell" in klass.__dict__:
            descriptor = klass.__dict__["fromCell"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_connect_has_toPart():
    assert hasattr(DatadiagramMLBasicDef_Connect, "toPart")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Connect.__mro__:
        if "toPart" in klass.__dict__:
            descriptor = klass.__dict__["toPart"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_connect_has_toCell():
    assert hasattr(DatadiagramMLBasicDef_Connect, "toCell")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Connect.__mro__:
        if "toCell" in klass.__dict__:
            descriptor = klass.__dict__["toCell"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_connect_has_fromSheet():
    assert hasattr(DatadiagramMLBasicDef_Connect, "fromSheet")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Connect.__mro__:
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



def test_datadiagrammlbasicdef_pagescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_PagesCollection)


def test_datadiagrammlbasicdef_pagescollection_constructor_exists():
    assert callable(DatadiagramMLBasicDef_PagesCollection.__init__)


def test_datadiagrammlbasicdef_pagescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_PagesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_masterelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_MasterElt)


def test_datadiagrammlbasicdef_masterelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_MasterElt.__init__)


def test_datadiagrammlbasicdef_masterelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_MasterElt.__init__)
    params = list(sig.parameters.keys())



def test_icon_is_not_abstract():
    assert not inspect.isabstract(Icon)


def test_icon_constructor_exists():
    assert callable(Icon.__init__)


def test_icon_constructor_args():
    sig = inspect.signature(Icon.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_masterscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_MastersCollection)


def test_datadiagrammlbasicdef_masterscollection_constructor_exists():
    assert callable(DatadiagramMLBasicDef_MastersCollection.__init__)


def test_datadiagrammlbasicdef_masterscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_MastersCollection.__init__)
    params = list(sig.parameters.keys())



def test_text_is_not_abstract():
    assert not inspect.isabstract(Text)


def test_text_constructor_exists():
    assert callable(Text.__init__)


def test_text_constructor_args():
    sig = inspect.signature(Text.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_textelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_TextElt)


def test_datadiagrammlbasicdef_textelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_TextElt.__init__)


def test_datadiagrammlbasicdef_textelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_TextElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_headerfooter_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_HeaderFooter)


def test_datadiagrammlbasicdef_headerfooter_constructor_exists():
    assert callable(DatadiagramMLBasicDef_HeaderFooter.__init__)


def test_datadiagrammlbasicdef_headerfooter_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_HeaderFooter.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_eventlist_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_EventList)


def test_datadiagrammlbasicdef_eventlist_constructor_exists():
    assert callable(DatadiagramMLBasicDef_EventList.__init__)


def test_datadiagrammlbasicdef_eventlist_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_EventList.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_windowsinfo_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_WindowsInfo)


def test_datadiagrammlbasicdef_windowsinfo_constructor_exists():
    assert callable(DatadiagramMLBasicDef_WindowsInfo.__init__)


def test_datadiagrammlbasicdef_windowsinfo_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_WindowsInfo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_facenamestable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_FaceNamesTable)


def test_datadiagrammlbasicdef_facenamestable_constructor_exists():
    assert callable(DatadiagramMLBasicDef_FaceNamesTable.__init__)


def test_datadiagrammlbasicdef_facenamestable_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_FaceNamesTable.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_fontstable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_FontsTable)


def test_datadiagrammlbasicdef_fontstable_constructor_exists():
    assert callable(DatadiagramMLBasicDef_FontsTable.__init__)


def test_datadiagrammlbasicdef_fontstable_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_FontsTable.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_printsetup_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_PrintSetup)


def test_datadiagrammlbasicdef_printsetup_constructor_exists():
    assert callable(DatadiagramMLBasicDef_PrintSetup.__init__)


def test_datadiagrammlbasicdef_printsetup_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_PrintSetup.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_solutionxml_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_SolutionXML)


def test_datadiagrammlbasicdef_solutionxml_constructor_exists():
    assert callable(DatadiagramMLBasicDef_SolutionXML.__init__)


def test_datadiagrammlbasicdef_solutionxml_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_SolutionXML.__init__)
    params = list(sig.parameters.keys())



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_colorstable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_ColorsTable)


def test_datadiagrammlbasicdef_colorstable_constructor_exists():
    assert callable(DatadiagramMLBasicDef_ColorsTable.__init__)


def test_datadiagrammlbasicdef_colorstable_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_ColorsTable.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_documentsettingselt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_DocumentSettingsElt)


def test_datadiagrammlbasicdef_documentsettingselt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_DocumentSettingsElt.__init__)


def test_datadiagrammlbasicdef_documentsettingselt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_DocumentSettingsElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_pageelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_PageElt)


def test_datadiagrammlbasicdef_pageelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_PageElt.__init__)


def test_datadiagrammlbasicdef_pageelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_PageElt.__init__)
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



def test_datadiagrammlbasicdef_splinestart_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_SplineStart)


def test_datadiagrammlbasicdef_splinestart_constructor_exists():
    assert callable(DatadiagramMLBasicDef_SplineStart.__init__)


def test_datadiagrammlbasicdef_splinestart_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_SplineStart.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_ellipticalarcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_EllipticalArcTo)


def test_datadiagrammlbasicdef_ellipticalarcto_constructor_exists():
    assert callable(DatadiagramMLBasicDef_EllipticalArcTo.__init__)


def test_datadiagrammlbasicdef_ellipticalarcto_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_EllipticalArcTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_ellipse_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_Ellipse)


def test_datadiagrammlbasicdef_ellipse_constructor_exists():
    assert callable(DatadiagramMLBasicDef_Ellipse.__init__)


def test_datadiagrammlbasicdef_ellipse_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_textelt_is_not_abstract():
    assert not inspect.isabstract(TextElt)


def test_textelt_constructor_exists():
    assert callable(TextElt.__init__)


def test_textelt_constructor_args():
    sig = inspect.signature(TextElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_stringelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_StringElt)


def test_datadiagrammlbasicdef_stringelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_StringElt.__init__)


def test_datadiagrammlbasicdef_stringelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_StringElt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammlbasicdef_stringelt_has_value():
    assert hasattr(DatadiagramMLBasicDef_StringElt, "value")
    descriptor = None
    for klass in DatadiagramMLBasicDef_StringElt.__mro__:
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



def test_datadiagrammlbasicdef_nurbsto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_NURBSTo)


def test_datadiagrammlbasicdef_nurbsto_constructor_exists():
    assert callable(DatadiagramMLBasicDef_NURBSTo.__init__)


def test_datadiagrammlbasicdef_nurbsto_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_NURBSTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_xyabcdeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_XYABCDEElt)


def test_datadiagrammlbasicdef_xyabcdeelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_XYABCDEElt.__init__)


def test_datadiagrammlbasicdef_xyabcdeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_XYABCDEElt.__init__)
    params = list(sig.parameters.keys())



def test_xyaelt_is_not_abstract():
    assert not inspect.isabstract(XYAElt)


def test_xyaelt_constructor_exists():
    assert callable(XYAElt.__init__)


def test_xyaelt_constructor_args():
    sig = inspect.signature(XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_splineknot_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_SplineKnot)


def test_datadiagrammlbasicdef_splineknot_constructor_exists():
    assert callable(DatadiagramMLBasicDef_SplineKnot.__init__)


def test_datadiagrammlbasicdef_splineknot_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_SplineKnot.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_polylineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_PolylineTo)


def test_datadiagrammlbasicdef_polylineto_constructor_exists():
    assert callable(DatadiagramMLBasicDef_PolylineTo.__init__)


def test_datadiagrammlbasicdef_polylineto_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_PolylineTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_arcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_ArcTo)


def test_datadiagrammlbasicdef_arcto_constructor_exists():
    assert callable(DatadiagramMLBasicDef_ArcTo.__init__)


def test_datadiagrammlbasicdef_arcto_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_ArcTo.__init__)
    params = list(sig.parameters.keys())



def test_xyabelt_is_not_abstract():
    assert not inspect.isabstract(XYABElt)


def test_xyabelt_constructor_exists():
    assert callable(XYABElt.__init__)


def test_xyabelt_constructor_args():
    sig = inspect.signature(XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_XYABCDElt)


def test_datadiagrammlbasicdef_xyabcdelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_XYABCDElt.__init__)


def test_datadiagrammlbasicdef_xyabcdelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_infiniteline_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_InfiniteLine)


def test_datadiagrammlbasicdef_infiniteline_constructor_exists():
    assert callable(DatadiagramMLBasicDef_InfiniteLine.__init__)


def test_datadiagrammlbasicdef_infiniteline_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_InfiniteLine.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_xyabelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_XYABElt)


def test_datadiagrammlbasicdef_xyabelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_XYABElt.__init__)


def test_datadiagrammlbasicdef_xyabelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_XYABElt.__init__)
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



def test_datadiagrammlbasicdef_moveto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_MoveTo)


def test_datadiagrammlbasicdef_moveto_constructor_exists():
    assert callable(DatadiagramMLBasicDef_MoveTo.__init__)


def test_datadiagrammlbasicdef_moveto_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_xyaelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_XYAElt)


def test_datadiagrammlbasicdef_xyaelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_XYAElt.__init__)


def test_datadiagrammlbasicdef_xyaelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_lineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_LineTo)


def test_datadiagrammlbasicdef_lineto_constructor_exists():
    assert callable(DatadiagramMLBasicDef_LineTo.__init__)


def test_datadiagrammlbasicdef_lineto_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_LineTo.__init__)
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



def test_datadiagrammlbasicdef_xyelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_XYElt)


def test_datadiagrammlbasicdef_xyelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_XYElt.__init__)


def test_datadiagrammlbasicdef_xyelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_XYElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_delelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_DelElt)


def test_datadiagrammlbasicdef_delelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_DelElt.__init__)


def test_datadiagrammlbasicdef_delelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_DelElt.__init__)
    params = list(sig.parameters.keys())
    assert "del_" in params, "Missing parameter 'del_'"

def test_datadiagrammlbasicdef_delelt_has_del_():
    assert hasattr(DatadiagramMLBasicDef_DelElt, "del_")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DelElt.__mro__:
        if "del_" in klass.__dict__:
            descriptor = klass.__dict__["del_"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef_ixelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_IXElt)


def test_datadiagrammlbasicdef_ixelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_IXElt.__init__)


def test_datadiagrammlbasicdef_ixelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_IXElt.__init__)
    params = list(sig.parameters.keys())
    assert "iX" in params, "Missing parameter 'iX'"

def test_datadiagrammlbasicdef_ixelt_has_iX():
    assert hasattr(DatadiagramMLBasicDef_IXElt, "iX")
    descriptor = None
    for klass in DatadiagramMLBasicDef_IXElt.__mro__:
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



def test_datadiagrammlbasicdef_uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_UniqueIdElt)


def test_datadiagrammlbasicdef_uniqueidelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_UniqueIdElt.__init__)


def test_datadiagrammlbasicdef_uniqueidelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_UniqueIdElt.__init__)
    params = list(sig.parameters.keys())
    assert "UniqueID" in params, "Missing parameter 'UniqueID'"

def test_datadiagrammlbasicdef_uniqueidelt_has_UniqueID():
    assert hasattr(DatadiagramMLBasicDef_UniqueIdElt, "UniqueID")
    descriptor = None
    for klass in DatadiagramMLBasicDef_UniqueIdElt.__mro__:
        if "UniqueID" in klass.__dict__:
            descriptor = klass.__dict__["UniqueID"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef_identifiedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_IdentifiedElt)


def test_datadiagrammlbasicdef_identifiedelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_IdentifiedElt.__init__)


def test_datadiagrammlbasicdef_identifiedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_IdentifiedElt.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_datadiagrammlbasicdef_identifiedelt_has_ID():
    assert hasattr(DatadiagramMLBasicDef_IdentifiedElt, "ID")
    descriptor = None
    for klass in DatadiagramMLBasicDef_IdentifiedElt.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef_namedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_NamedElt)


def test_datadiagrammlbasicdef_namedelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_NamedElt.__init__)


def test_datadiagrammlbasicdef_namedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "nameU" in params, "Missing parameter 'nameU'"

def test_datadiagrammlbasicdef_namedelt_has_name():
    assert hasattr(DatadiagramMLBasicDef_NamedElt, "name")
    descriptor = None
    for klass in DatadiagramMLBasicDef_NamedElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_namedelt_has_nameU():
    assert hasattr(DatadiagramMLBasicDef_NamedElt, "nameU")
    descriptor = None
    for klass in DatadiagramMLBasicDef_NamedElt.__mro__:
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



def test_datadiagrammlbasicdef_connectscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_ConnectsCollection)


def test_datadiagrammlbasicdef_connectscollection_constructor_exists():
    assert callable(DatadiagramMLBasicDef_ConnectsCollection.__init__)


def test_datadiagrammlbasicdef_connectscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_shapescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_ShapesCollection)


def test_datadiagrammlbasicdef_shapescollection_constructor_exists():
    assert callable(DatadiagramMLBasicDef_ShapesCollection.__init__)


def test_datadiagrammlbasicdef_shapescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_icon_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_Icon)


def test_datadiagrammlbasicdef_icon_constructor_exists():
    assert callable(DatadiagramMLBasicDef_Icon.__init__)


def test_datadiagrammlbasicdef_icon_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_Icon.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammlbasicdef_icon_has_value():
    assert hasattr(DatadiagramMLBasicDef_Icon, "value")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Icon.__mro__:
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



def test_datadiagrammlbasicdef_documentsheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_DocumentSheet)


def test_datadiagrammlbasicdef_documentsheet_constructor_exists():
    assert callable(DatadiagramMLBasicDef_DocumentSheet.__init__)


def test_datadiagrammlbasicdef_documentsheet_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_DocumentSheet.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_shapeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_ShapeElt)


def test_datadiagrammlbasicdef_shapeelt_constructor_exists():
    assert callable(DatadiagramMLBasicDef_ShapeElt.__init__)


def test_datadiagrammlbasicdef_shapeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_shapeelt_is_not_abstract():
    assert not inspect.isabstract(ShapeElt)


def test_shapeelt_constructor_exists():
    assert callable(ShapeElt.__init__)


def test_shapeelt_constructor_args():
    sig = inspect.signature(ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_text_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_Text)


def test_datadiagrammlbasicdef_text_constructor_exists():
    assert callable(DatadiagramMLBasicDef_Text.__init__)


def test_datadiagrammlbasicdef_text_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_Text.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_geom_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_Geom)


def test_datadiagrammlbasicdef_geom_constructor_exists():
    assert callable(DatadiagramMLBasicDef_Geom.__init__)


def test_datadiagrammlbasicdef_geom_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_Geom.__init__)
    params = list(sig.parameters.keys())



def test_shapescollection_is_not_abstract():
    assert not inspect.isabstract(ShapesCollection)


def test_shapescollection_constructor_exists():
    assert callable(ShapesCollection.__init__)


def test_shapescollection_constructor_args():
    sig = inspect.signature(ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_shape_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_Shape)


def test_datadiagrammlbasicdef_shape_constructor_exists():
    assert callable(DatadiagramMLBasicDef_Shape.__init__)


def test_datadiagrammlbasicdef_shape_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "textStyle" in params, "Missing parameter 'textStyle'"
    assert "fillStyle" in params, "Missing parameter 'fillStyle'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"

def test_datadiagrammlbasicdef_shape_has_textStyle():
    assert hasattr(DatadiagramMLBasicDef_Shape, "textStyle")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Shape.__mro__:
        if "textStyle" in klass.__dict__:
            descriptor = klass.__dict__["textStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_shape_has_fillStyle():
    assert hasattr(DatadiagramMLBasicDef_Shape, "fillStyle")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Shape.__mro__:
        if "fillStyle" in klass.__dict__:
            descriptor = klass.__dict__["fillStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_shape_has_lineStyle():
    assert hasattr(DatadiagramMLBasicDef_Shape, "lineStyle")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Shape.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef_emailroutingdata_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_EmailRoutingData)


def test_datadiagrammlbasicdef_emailroutingdata_constructor_exists():
    assert callable(DatadiagramMLBasicDef_EmailRoutingData.__init__)


def test_datadiagrammlbasicdef_emailroutingdata_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_EmailRoutingData.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "data" in params, "Missing parameter 'data'"

def test_datadiagrammlbasicdef_emailroutingdata_has_size():
    assert hasattr(DatadiagramMLBasicDef_EmailRoutingData, "size")
    descriptor = None
    for klass in DatadiagramMLBasicDef_EmailRoutingData.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_emailroutingdata_has_data():
    assert hasattr(DatadiagramMLBasicDef_EmailRoutingData, "data")
    descriptor = None
    for klass in DatadiagramMLBasicDef_EmailRoutingData.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef_vbprojectdata_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_VBProjectData)


def test_datadiagrammlbasicdef_vbprojectdata_constructor_exists():
    assert callable(DatadiagramMLBasicDef_VBProjectData.__init__)


def test_datadiagrammlbasicdef_vbprojectdata_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_VBProjectData.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_datadiagrammlbasicdef_vbprojectdata_has_data():
    assert hasattr(DatadiagramMLBasicDef_VBProjectData, "data")
    descriptor = None
    for klass in DatadiagramMLBasicDef_VBProjectData.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef_customproperty_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_CustomProperty)


def test_datadiagrammlbasicdef_customproperty_constructor_exists():
    assert callable(DatadiagramMLBasicDef_CustomProperty.__init__)


def test_datadiagrammlbasicdef_customproperty_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_CustomProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_datadiagrammlbasicdef_customproperty_has_name():
    assert hasattr(DatadiagramMLBasicDef_CustomProperty, "name")
    descriptor = None
    for klass in DatadiagramMLBasicDef_CustomProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_customproperty_has_dataType():
    assert hasattr(DatadiagramMLBasicDef_CustomProperty, "dataType")
    descriptor = None
    for klass in DatadiagramMLBasicDef_CustomProperty.__mro__:
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



def test_datadiagrammlbasicdef_custompropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_CustomPropertiesCollection)


def test_datadiagrammlbasicdef_custompropertiescollection_constructor_exists():
    assert callable(DatadiagramMLBasicDef_CustomPropertiesCollection.__init__)


def test_datadiagrammlbasicdef_custompropertiescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_CustomPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_identifiedelt_is_not_abstract():
    assert not inspect.isabstract(IdentifiedElt)


def test_identifiedelt_constructor_exists():
    assert callable(IdentifiedElt.__init__)


def test_identifiedelt_constructor_args():
    sig = inspect.signature(IdentifiedElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_page_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_Page)


def test_datadiagrammlbasicdef_page_constructor_exists():
    assert callable(DatadiagramMLBasicDef_Page.__init__)


def test_datadiagrammlbasicdef_page_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_Page.__init__)
    params = list(sig.parameters.keys())
    assert "reviewerID" in params, "Missing parameter 'reviewerID'"
    assert "viewScale" in params, "Missing parameter 'viewScale'"
    assert "backPage" in params, "Missing parameter 'backPage'"
    assert "viewCenterX" in params, "Missing parameter 'viewCenterX'"
    assert "background" in params, "Missing parameter 'background'"
    assert "associatedPage" in params, "Missing parameter 'associatedPage'"
    assert "ViewCenterY" in params, "Missing parameter 'ViewCenterY'"

def test_datadiagrammlbasicdef_page_has_reviewerID():
    assert hasattr(DatadiagramMLBasicDef_Page, "reviewerID")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Page.__mro__:
        if "reviewerID" in klass.__dict__:
            descriptor = klass.__dict__["reviewerID"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_page_has_viewScale():
    assert hasattr(DatadiagramMLBasicDef_Page, "viewScale")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Page.__mro__:
        if "viewScale" in klass.__dict__:
            descriptor = klass.__dict__["viewScale"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_page_has_backPage():
    assert hasattr(DatadiagramMLBasicDef_Page, "backPage")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Page.__mro__:
        if "backPage" in klass.__dict__:
            descriptor = klass.__dict__["backPage"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_page_has_viewCenterX():
    assert hasattr(DatadiagramMLBasicDef_Page, "viewCenterX")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Page.__mro__:
        if "viewCenterX" in klass.__dict__:
            descriptor = klass.__dict__["viewCenterX"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_page_has_background():
    assert hasattr(DatadiagramMLBasicDef_Page, "background")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Page.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_page_has_associatedPage():
    assert hasattr(DatadiagramMLBasicDef_Page, "associatedPage")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Page.__mro__:
        if "associatedPage" in klass.__dict__:
            descriptor = klass.__dict__["associatedPage"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_page_has_ViewCenterY():
    assert hasattr(DatadiagramMLBasicDef_Page, "ViewCenterY")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Page.__mro__:
        if "ViewCenterY" in klass.__dict__:
            descriptor = klass.__dict__["ViewCenterY"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef_mastershortcut_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_MasterShortCut)


def test_datadiagrammlbasicdef_mastershortcut_constructor_exists():
    assert callable(DatadiagramMLBasicDef_MasterShortCut.__init__)


def test_datadiagrammlbasicdef_mastershortcut_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_MasterShortCut.__init__)
    params = list(sig.parameters.keys())
    assert "shortcutURL" in params, "Missing parameter 'shortcutURL'"
    assert "shortcutHelp" in params, "Missing parameter 'shortcutHelp'"
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"

def test_datadiagrammlbasicdef_mastershortcut_has_shortcutURL():
    assert hasattr(DatadiagramMLBasicDef_MasterShortCut, "shortcutURL")
    descriptor = None
    for klass in DatadiagramMLBasicDef_MasterShortCut.__mro__:
        if "shortcutURL" in klass.__dict__:
            descriptor = klass.__dict__["shortcutURL"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_mastershortcut_has_shortcutHelp():
    assert hasattr(DatadiagramMLBasicDef_MasterShortCut, "shortcutHelp")
    descriptor = None
    for klass in DatadiagramMLBasicDef_MasterShortCut.__mro__:
        if "shortcutHelp" in klass.__dict__:
            descriptor = klass.__dict__["shortcutHelp"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_mastershortcut_has_prompt():
    assert hasattr(DatadiagramMLBasicDef_MasterShortCut, "prompt")
    descriptor = None
    for klass in DatadiagramMLBasicDef_MasterShortCut.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_mastershortcut_has_patternFlags():
    assert hasattr(DatadiagramMLBasicDef_MasterShortCut, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLBasicDef_MasterShortCut.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_mastershortcut_has_alignName():
    assert hasattr(DatadiagramMLBasicDef_MasterShortCut, "alignName")
    descriptor = None
    for klass in DatadiagramMLBasicDef_MasterShortCut.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_mastershortcut_has_iconSize():
    assert hasattr(DatadiagramMLBasicDef_MasterShortCut, "iconSize")
    descriptor = None
    for klass in DatadiagramMLBasicDef_MasterShortCut.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef_master_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_Master)


def test_datadiagrammlbasicdef_master_constructor_exists():
    assert callable(DatadiagramMLBasicDef_Master.__init__)


def test_datadiagrammlbasicdef_master_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_Master.__init__)
    params = list(sig.parameters.keys())
    assert "iconUpdate" in params, "Missing parameter 'iconUpdate'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"
    assert "baseID" in params, "Missing parameter 'baseID'"
    assert "matchByName" in params, "Missing parameter 'matchByName'"
    assert "hidden" in params, "Missing parameter 'hidden'"

def test_datadiagrammlbasicdef_master_has_iconUpdate():
    assert hasattr(DatadiagramMLBasicDef_Master, "iconUpdate")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Master.__mro__:
        if "iconUpdate" in klass.__dict__:
            descriptor = klass.__dict__["iconUpdate"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_master_has_alignName():
    assert hasattr(DatadiagramMLBasicDef_Master, "alignName")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Master.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_master_has_patternFlags():
    assert hasattr(DatadiagramMLBasicDef_Master, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Master.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_master_has_prompt():
    assert hasattr(DatadiagramMLBasicDef_Master, "prompt")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Master.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_master_has_iconSize():
    assert hasattr(DatadiagramMLBasicDef_Master, "iconSize")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Master.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_master_has_baseID():
    assert hasattr(DatadiagramMLBasicDef_Master, "baseID")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Master.__mro__:
        if "baseID" in klass.__dict__:
            descriptor = klass.__dict__["baseID"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_master_has_matchByName():
    assert hasattr(DatadiagramMLBasicDef_Master, "matchByName")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Master.__mro__:
        if "matchByName" in klass.__dict__:
            descriptor = klass.__dict__["matchByName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_master_has_hidden():
    assert hasattr(DatadiagramMLBasicDef_Master, "hidden")
    descriptor = None
    for klass in DatadiagramMLBasicDef_Master.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_pagesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_PageSheet)


def test_datadiagrammlbasicdef_pagesheet_constructor_exists():
    assert callable(DatadiagramMLBasicDef_PageSheet.__init__)


def test_datadiagrammlbasicdef_pagesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_PageSheet.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_stylesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_StyleSheet)


def test_datadiagrammlbasicdef_stylesheet_constructor_exists():
    assert callable(DatadiagramMLBasicDef_StyleSheet.__init__)


def test_datadiagrammlbasicdef_stylesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_stylesheet_is_not_abstract():
    assert not inspect.isabstract(StyleSheet)


def test_stylesheet_constructor_exists():
    assert callable(StyleSheet.__init__)


def test_stylesheet_constructor_args():
    sig = inspect.signature(StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_stylesheetscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_StyleSheetsCollection)


def test_datadiagrammlbasicdef_stylesheetscollection_constructor_exists():
    assert callable(DatadiagramMLBasicDef_StyleSheetsCollection.__init__)


def test_datadiagrammlbasicdef_stylesheetscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_StyleSheetsCollection.__init__)
    params = list(sig.parameters.keys())



def test_visiodocument_is_not_abstract():
    assert not inspect.isabstract(VisioDocument)


def test_visiodocument_constructor_exists():
    assert callable(VisioDocument.__init__)


def test_visiodocument_constructor_args():
    sig = inspect.signature(VisioDocument.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlbasicdef_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_DocumentPropertiesCollection)


def test_datadiagrammlbasicdef_documentpropertiescollection_constructor_exists():
    assert callable(DatadiagramMLBasicDef_DocumentPropertiesCollection.__init__)


def test_datadiagrammlbasicdef_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "company" in params, "Missing parameter 'company'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "title" in params, "Missing parameter 'title'"
    assert "alternateNames" in params, "Missing parameter 'alternateNames'"
    assert "description" in params, "Missing parameter 'description'"
    assert "buildNumberCreated" in params, "Missing parameter 'buildNumberCreated'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "creator" in params, "Missing parameter 'creator'"
    assert "buildNumberEdited" in params, "Missing parameter 'buildNumberEdited'"
    assert "hyperlinkBase_href" in params, "Missing parameter 'hyperlinkBase_href'"
    assert "template" in params, "Missing parameter 'template'"
    assert "category" in params, "Missing parameter 'category'"
    assert "subject" in params, "Missing parameter 'subject'"

def test_datadiagrammlbasicdef_documentpropertiescollection_has_company():
    assert hasattr(DatadiagramMLBasicDef_DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_documentpropertiescollection_has_manager():
    assert hasattr(DatadiagramMLBasicDef_DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_documentpropertiescollection_has_title():
    assert hasattr(DatadiagramMLBasicDef_DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_documentpropertiescollection_has_alternateNames():
    assert hasattr(DatadiagramMLBasicDef_DocumentPropertiesCollection, "alternateNames")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "alternateNames" in klass.__dict__:
            descriptor = klass.__dict__["alternateNames"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_documentpropertiescollection_has_description():
    assert hasattr(DatadiagramMLBasicDef_DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_documentpropertiescollection_has_buildNumberCreated():
    assert hasattr(DatadiagramMLBasicDef_DocumentPropertiesCollection, "buildNumberCreated")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "buildNumberCreated" in klass.__dict__:
            descriptor = klass.__dict__["buildNumberCreated"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_documentpropertiescollection_has_keywords():
    assert hasattr(DatadiagramMLBasicDef_DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_documentpropertiescollection_has_creator():
    assert hasattr(DatadiagramMLBasicDef_DocumentPropertiesCollection, "creator")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "creator" in klass.__dict__:
            descriptor = klass.__dict__["creator"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_documentpropertiescollection_has_buildNumberEdited():
    assert hasattr(DatadiagramMLBasicDef_DocumentPropertiesCollection, "buildNumberEdited")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "buildNumberEdited" in klass.__dict__:
            descriptor = klass.__dict__["buildNumberEdited"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_documentpropertiescollection_has_hyperlinkBase_href():
    assert hasattr(DatadiagramMLBasicDef_DocumentPropertiesCollection, "hyperlinkBase_href")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase_href" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase_href"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_documentpropertiescollection_has_template():
    assert hasattr(DatadiagramMLBasicDef_DocumentPropertiesCollection, "template")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_documentpropertiescollection_has_category():
    assert hasattr(DatadiagramMLBasicDef_DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_documentpropertiescollection_has_subject():
    assert hasattr(DatadiagramMLBasicDef_DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
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



def test_datadiagrammlbasicdef_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_DateTimeType)


def test_datadiagrammlbasicdef_datetimetype_constructor_exists():
    assert callable(DatadiagramMLBasicDef_DateTimeType.__init__)


def test_datadiagrammlbasicdef_datetimetype_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "second" in params, "Missing parameter 'second'"
    assert "day" in params, "Missing parameter 'day'"
    assert "month" in params, "Missing parameter 'month'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "year" in params, "Missing parameter 'year'"

def test_datadiagrammlbasicdef_datetimetype_has_second():
    assert hasattr(DatadiagramMLBasicDef_DateTimeType, "second")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_datetimetype_has_day():
    assert hasattr(DatadiagramMLBasicDef_DateTimeType, "day")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_datetimetype_has_month():
    assert hasattr(DatadiagramMLBasicDef_DateTimeType, "month")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_datetimetype_has_hour():
    assert hasattr(DatadiagramMLBasicDef_DateTimeType, "hour")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_datetimetype_has_minute():
    assert hasattr(DatadiagramMLBasicDef_DateTimeType, "minute")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_datetimetype_has_year():
    assert hasattr(DatadiagramMLBasicDef_DateTimeType, "year")
    descriptor = None
    for klass in DatadiagramMLBasicDef_DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef_visiodocument_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_VisioDocument)


def test_datadiagrammlbasicdef_visiodocument_constructor_exists():
    assert callable(DatadiagramMLBasicDef_VisioDocument.__init__)


def test_datadiagrammlbasicdef_visiodocument_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_VisioDocument.__init__)
    params = list(sig.parameters.keys())
    assert "docLangId" in params, "Missing parameter 'docLangId'"
    assert "key" in params, "Missing parameter 'key'"
    assert "metric" in params, "Missing parameter 'metric'"
    assert "buildnum" in params, "Missing parameter 'buildnum'"
    assert "version" in params, "Missing parameter 'version'"
    assert "start" in params, "Missing parameter 'start'"

def test_datadiagrammlbasicdef_visiodocument_has_docLangId():
    assert hasattr(DatadiagramMLBasicDef_VisioDocument, "docLangId")
    descriptor = None
    for klass in DatadiagramMLBasicDef_VisioDocument.__mro__:
        if "docLangId" in klass.__dict__:
            descriptor = klass.__dict__["docLangId"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_visiodocument_has_key():
    assert hasattr(DatadiagramMLBasicDef_VisioDocument, "key")
    descriptor = None
    for klass in DatadiagramMLBasicDef_VisioDocument.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_visiodocument_has_metric():
    assert hasattr(DatadiagramMLBasicDef_VisioDocument, "metric")
    descriptor = None
    for klass in DatadiagramMLBasicDef_VisioDocument.__mro__:
        if "metric" in klass.__dict__:
            descriptor = klass.__dict__["metric"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_visiodocument_has_buildnum():
    assert hasattr(DatadiagramMLBasicDef_VisioDocument, "buildnum")
    descriptor = None
    for klass in DatadiagramMLBasicDef_VisioDocument.__mro__:
        if "buildnum" in klass.__dict__:
            descriptor = klass.__dict__["buildnum"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_visiodocument_has_version():
    assert hasattr(DatadiagramMLBasicDef_VisioDocument, "version")
    descriptor = None
    for klass in DatadiagramMLBasicDef_VisioDocument.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_visiodocument_has_start():
    assert hasattr(DatadiagramMLBasicDef_VisioDocument, "start")
    descriptor = None
    for klass in DatadiagramMLBasicDef_VisioDocument.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlbasicdef_celltype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLBasicDef_CellType)


def test_datadiagrammlbasicdef_celltype_constructor_exists():
    assert callable(DatadiagramMLBasicDef_CellType.__init__)


def test_datadiagrammlbasicdef_celltype_constructor_args():
    sig = inspect.signature(DatadiagramMLBasicDef_CellType.__init__)
    params = list(sig.parameters.keys())
    assert "formula" in params, "Missing parameter 'formula'"
    assert "err" in params, "Missing parameter 'err'"
    assert "value" in params, "Missing parameter 'value'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_datadiagrammlbasicdef_celltype_has_formula():
    assert hasattr(DatadiagramMLBasicDef_CellType, "formula")
    descriptor = None
    for klass in DatadiagramMLBasicDef_CellType.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_celltype_has_err():
    assert hasattr(DatadiagramMLBasicDef_CellType, "err")
    descriptor = None
    for klass in DatadiagramMLBasicDef_CellType.__mro__:
        if "err" in klass.__dict__:
            descriptor = klass.__dict__["err"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_celltype_has_value():
    assert hasattr(DatadiagramMLBasicDef_CellType, "value")
    descriptor = None
    for klass in DatadiagramMLBasicDef_CellType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlbasicdef_celltype_has_unit():
    assert hasattr(DatadiagramMLBasicDef_CellType, "unit")
    descriptor = None
    for klass in DatadiagramMLBasicDef_CellType.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
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
ConnectsCollection_strategy = st.builds(
    ConnectsCollection,
)
DatadiagramMLBasicDef_Connect_strategy = st.builds(
    DatadiagramMLBasicDef_Connect,
    fromPart=
        safe_text,
    toSheet=
        safe_text,
    fromCell=
        safe_text,
    toPart=
        safe_text,
    toCell=
        safe_text,
    fromSheet=
        safe_text
)
Connect_strategy = st.builds(
    Connect,
)
DatadiagramMLBasicDef_PagesCollection_strategy = st.builds(
    DatadiagramMLBasicDef_PagesCollection,
)
DatadiagramMLBasicDef_MasterElt_strategy = st.builds(
    DatadiagramMLBasicDef_MasterElt,
)
Icon_strategy = st.builds(
    Icon,
)
DatadiagramMLBasicDef_MastersCollection_strategy = st.builds(
    DatadiagramMLBasicDef_MastersCollection,
)
Text_strategy = st.builds(
    Text,
)
DatadiagramMLBasicDef_TextElt_strategy = st.builds(
    DatadiagramMLBasicDef_TextElt,
)
DatadiagramMLBasicDef_HeaderFooter_strategy = st.builds(
    DatadiagramMLBasicDef_HeaderFooter,
)
DatadiagramMLBasicDef_EventList_strategy = st.builds(
    DatadiagramMLBasicDef_EventList,
)
DatadiagramMLBasicDef_WindowsInfo_strategy = st.builds(
    DatadiagramMLBasicDef_WindowsInfo,
)
DatadiagramMLBasicDef_FaceNamesTable_strategy = st.builds(
    DatadiagramMLBasicDef_FaceNamesTable,
)
DatadiagramMLBasicDef_FontsTable_strategy = st.builds(
    DatadiagramMLBasicDef_FontsTable,
)
DatadiagramMLBasicDef_PrintSetup_strategy = st.builds(
    DatadiagramMLBasicDef_PrintSetup,
)
DatadiagramMLBasicDef_SolutionXML_strategy = st.builds(
    DatadiagramMLBasicDef_SolutionXML,
)
Page_strategy = st.builds(
    Page,
)
DatadiagramMLBasicDef_ColorsTable_strategy = st.builds(
    DatadiagramMLBasicDef_ColorsTable,
)
DatadiagramMLBasicDef_DocumentSettingsElt_strategy = st.builds(
    DatadiagramMLBasicDef_DocumentSettingsElt,
)
DatadiagramMLBasicDef_PageElt_strategy = st.builds(
    DatadiagramMLBasicDef_PageElt,
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
DatadiagramMLBasicDef_SplineStart_strategy = st.builds(
    DatadiagramMLBasicDef_SplineStart,
)
DatadiagramMLBasicDef_EllipticalArcTo_strategy = st.builds(
    DatadiagramMLBasicDef_EllipticalArcTo,
)
DatadiagramMLBasicDef_Ellipse_strategy = st.builds(
    DatadiagramMLBasicDef_Ellipse,
)
TextElt_strategy = st.builds(
    TextElt,
)
DatadiagramMLBasicDef_StringElt_strategy = st.builds(
    DatadiagramMLBasicDef_StringElt,
    value=
        safe_text
)
XYABCDEElt_strategy = st.builds(
    XYABCDEElt,
)
DatadiagramMLBasicDef_NURBSTo_strategy = st.builds(
    DatadiagramMLBasicDef_NURBSTo,
)
DatadiagramMLBasicDef_XYABCDEElt_strategy = st.builds(
    DatadiagramMLBasicDef_XYABCDEElt,
)
XYAElt_strategy = st.builds(
    XYAElt,
)
DatadiagramMLBasicDef_SplineKnot_strategy = st.builds(
    DatadiagramMLBasicDef_SplineKnot,
)
DatadiagramMLBasicDef_PolylineTo_strategy = st.builds(
    DatadiagramMLBasicDef_PolylineTo,
)
DatadiagramMLBasicDef_ArcTo_strategy = st.builds(
    DatadiagramMLBasicDef_ArcTo,
)
XYABElt_strategy = st.builds(
    XYABElt,
)
DatadiagramMLBasicDef_XYABCDElt_strategy = st.builds(
    DatadiagramMLBasicDef_XYABCDElt,
)
DatadiagramMLBasicDef_InfiniteLine_strategy = st.builds(
    DatadiagramMLBasicDef_InfiniteLine,
)
DatadiagramMLBasicDef_XYABElt_strategy = st.builds(
    DatadiagramMLBasicDef_XYABElt,
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
DatadiagramMLBasicDef_MoveTo_strategy = st.builds(
    DatadiagramMLBasicDef_MoveTo,
)
DatadiagramMLBasicDef_XYAElt_strategy = st.builds(
    DatadiagramMLBasicDef_XYAElt,
)
DatadiagramMLBasicDef_LineTo_strategy = st.builds(
    DatadiagramMLBasicDef_LineTo,
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
DatadiagramMLBasicDef_XYElt_strategy = st.builds(
    DatadiagramMLBasicDef_XYElt,
)
DatadiagramMLBasicDef_DelElt_strategy = st.builds(
    DatadiagramMLBasicDef_DelElt,
    del_=
        safe_text
)
DatadiagramMLBasicDef_IXElt_strategy = st.builds(
    DatadiagramMLBasicDef_IXElt,
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
DatadiagramMLBasicDef_UniqueIdElt_strategy = st.builds(
    DatadiagramMLBasicDef_UniqueIdElt,
    UniqueID=
        safe_text
)
DatadiagramMLBasicDef_IdentifiedElt_strategy = st.builds(
    DatadiagramMLBasicDef_IdentifiedElt,
    ID=
        safe_text
)
DatadiagramMLBasicDef_NamedElt_strategy = st.builds(
    DatadiagramMLBasicDef_NamedElt,
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
DatadiagramMLBasicDef_ConnectsCollection_strategy = st.builds(
    DatadiagramMLBasicDef_ConnectsCollection,
)
DatadiagramMLBasicDef_ShapesCollection_strategy = st.builds(
    DatadiagramMLBasicDef_ShapesCollection,
)
DatadiagramMLBasicDef_Icon_strategy = st.builds(
    DatadiagramMLBasicDef_Icon,
    value=
        safe_text
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
DatadiagramMLBasicDef_DocumentSheet_strategy = st.builds(
    DatadiagramMLBasicDef_DocumentSheet,
)
DatadiagramMLBasicDef_ShapeElt_strategy = st.builds(
    DatadiagramMLBasicDef_ShapeElt,
)
ShapeElt_strategy = st.builds(
    ShapeElt,
)
DatadiagramMLBasicDef_Text_strategy = st.builds(
    DatadiagramMLBasicDef_Text,
)
DatadiagramMLBasicDef_Geom_strategy = st.builds(
    DatadiagramMLBasicDef_Geom,
)
ShapesCollection_strategy = st.builds(
    ShapesCollection,
)
DatadiagramMLBasicDef_Shape_strategy = st.builds(
    DatadiagramMLBasicDef_Shape,
    textStyle=
        safe_text,
    fillStyle=
        safe_text,
    lineStyle=
        safe_text
)
DatadiagramMLBasicDef_EmailRoutingData_strategy = st.builds(
    DatadiagramMLBasicDef_EmailRoutingData,
    size=
        safe_text,
    data=
        safe_text
)
DatadiagramMLBasicDef_VBProjectData_strategy = st.builds(
    DatadiagramMLBasicDef_VBProjectData,
    data=
        safe_text
)
DatadiagramMLBasicDef_CustomProperty_strategy = st.builds(
    DatadiagramMLBasicDef_CustomProperty,
    name=
        safe_text,
    dataType=
        safe_text
)
CustomProperty_strategy = st.builds(
    CustomProperty,
)
DatadiagramMLBasicDef_CustomPropertiesCollection_strategy = st.builds(
    DatadiagramMLBasicDef_CustomPropertiesCollection,
)
IdentifiedElt_strategy = st.builds(
    IdentifiedElt,
)
DatadiagramMLBasicDef_Page_strategy = st.builds(
    DatadiagramMLBasicDef_Page,
    reviewerID=
        safe_text,
    viewScale=
        safe_text,
    backPage=
        safe_text,
    viewCenterX=
        safe_text,
    background=
        safe_text,
    associatedPage=
        safe_text,
    ViewCenterY=
        safe_text
)
DatadiagramMLBasicDef_MasterShortCut_strategy = st.builds(
    DatadiagramMLBasicDef_MasterShortCut,
    shortcutURL=
        safe_text,
    shortcutHelp=
        safe_text,
    prompt=
        safe_text,
    patternFlags=
        safe_text,
    alignName=
        safe_text,
    iconSize=
        safe_text
)
DatadiagramMLBasicDef_Master_strategy = st.builds(
    DatadiagramMLBasicDef_Master,
    iconUpdate=
        safe_text,
    alignName=
        safe_text,
    patternFlags=
        safe_text,
    prompt=
        safe_text,
    iconSize=
        safe_text,
    baseID=
        safe_text,
    matchByName=
        safe_text,
    hidden=
        safe_text
)
Shape_strategy = st.builds(
    Shape,
)
DatadiagramMLBasicDef_PageSheet_strategy = st.builds(
    DatadiagramMLBasicDef_PageSheet,
)
DatadiagramMLBasicDef_StyleSheet_strategy = st.builds(
    DatadiagramMLBasicDef_StyleSheet,
)
StyleSheet_strategy = st.builds(
    StyleSheet,
)
DatadiagramMLBasicDef_StyleSheetsCollection_strategy = st.builds(
    DatadiagramMLBasicDef_StyleSheetsCollection,
)
VisioDocument_strategy = st.builds(
    VisioDocument,
)
DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy = st.builds(
    DatadiagramMLBasicDef_DocumentPropertiesCollection,
    company=
        safe_text,
    manager=
        safe_text,
    title=
        safe_text,
    alternateNames=
        safe_text,
    description=
        safe_text,
    buildNumberCreated=
        safe_text,
    keywords=
        safe_text,
    creator=
        safe_text,
    buildNumberEdited=
        safe_text,
    hyperlinkBase_href=
        safe_text,
    template=
        safe_text,
    category=
        safe_text,
    subject=
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
DatadiagramMLBasicDef_DateTimeType_strategy = st.builds(
    DatadiagramMLBasicDef_DateTimeType,
    second=
        safe_text,
    day=
        safe_text,
    month=
        safe_text,
    hour=
        safe_text,
    minute=
        safe_text,
    year=
        safe_text
)
DatadiagramMLBasicDef_VisioDocument_strategy = st.builds(
    DatadiagramMLBasicDef_VisioDocument,
    docLangId=
        safe_text,
    key=
        safe_text,
    metric=
        safe_text,
    buildnum=
        safe_text,
    version=
        safe_text,
    start=
        safe_text
)
DatadiagramMLBasicDef_CellType_strategy = st.builds(
    DatadiagramMLBasicDef_CellType,
    formula=
        safe_text,
    err=
        safe_text,
    value=
        safe_text,
    unit=
        safe_text
)

@given(instance=ConnectsCollection_strategy)
@settings(max_examples=50)
def test_connectscollection_instantiation(instance):
    assert isinstance(instance, ConnectsCollection)

@given(instance=DatadiagramMLBasicDef_Connect_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_connect_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_Connect)



@given(instance=DatadiagramMLBasicDef_Connect_strategy)
def test_datadiagrammlbasicdef_connect_fromPart_setter(instance):
    original = instance.fromPart
    instance.fromPart = original
    assert instance.fromPart == original



@given(instance=DatadiagramMLBasicDef_Connect_strategy)
def test_datadiagrammlbasicdef_connect_toSheet_setter(instance):
    original = instance.toSheet
    instance.toSheet = original
    assert instance.toSheet == original



@given(instance=DatadiagramMLBasicDef_Connect_strategy)
def test_datadiagrammlbasicdef_connect_fromCell_setter(instance):
    original = instance.fromCell
    instance.fromCell = original
    assert instance.fromCell == original



@given(instance=DatadiagramMLBasicDef_Connect_strategy)
def test_datadiagrammlbasicdef_connect_toPart_setter(instance):
    original = instance.toPart
    instance.toPart = original
    assert instance.toPart == original



@given(instance=DatadiagramMLBasicDef_Connect_strategy)
def test_datadiagrammlbasicdef_connect_toCell_setter(instance):
    original = instance.toCell
    instance.toCell = original
    assert instance.toCell == original



@given(instance=DatadiagramMLBasicDef_Connect_strategy)
def test_datadiagrammlbasicdef_connect_fromSheet_setter(instance):
    original = instance.fromSheet
    instance.fromSheet = original
    assert instance.fromSheet == original

@given(instance=Connect_strategy)
@settings(max_examples=50)
def test_connect_instantiation(instance):
    assert isinstance(instance, Connect)

@given(instance=DatadiagramMLBasicDef_PagesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_pagescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_PagesCollection)

@given(instance=DatadiagramMLBasicDef_MasterElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_masterelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_MasterElt)

@given(instance=Icon_strategy)
@settings(max_examples=50)
def test_icon_instantiation(instance):
    assert isinstance(instance, Icon)

@given(instance=DatadiagramMLBasicDef_MastersCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_masterscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_MastersCollection)

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=DatadiagramMLBasicDef_TextElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_textelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_TextElt)

@given(instance=DatadiagramMLBasicDef_HeaderFooter_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_headerfooter_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_HeaderFooter)

@given(instance=DatadiagramMLBasicDef_EventList_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_eventlist_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_EventList)

@given(instance=DatadiagramMLBasicDef_WindowsInfo_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_windowsinfo_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_WindowsInfo)

@given(instance=DatadiagramMLBasicDef_FaceNamesTable_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_facenamestable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_FaceNamesTable)

@given(instance=DatadiagramMLBasicDef_FontsTable_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_fontstable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_FontsTable)

@given(instance=DatadiagramMLBasicDef_PrintSetup_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_printsetup_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_PrintSetup)

@given(instance=DatadiagramMLBasicDef_SolutionXML_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_solutionxml_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_SolutionXML)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=DatadiagramMLBasicDef_ColorsTable_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_colorstable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_ColorsTable)

@given(instance=DatadiagramMLBasicDef_DocumentSettingsElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_documentsettingselt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_DocumentSettingsElt)

@given(instance=DatadiagramMLBasicDef_PageElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_pageelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_PageElt)

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

@given(instance=DatadiagramMLBasicDef_SplineStart_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_splinestart_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_SplineStart)

@given(instance=DatadiagramMLBasicDef_EllipticalArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_ellipticalarcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_EllipticalArcTo)

@given(instance=DatadiagramMLBasicDef_Ellipse_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_ellipse_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_Ellipse)

@given(instance=TextElt_strategy)
@settings(max_examples=50)
def test_textelt_instantiation(instance):
    assert isinstance(instance, TextElt)

@given(instance=DatadiagramMLBasicDef_StringElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_stringelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_StringElt)



@given(instance=DatadiagramMLBasicDef_StringElt_strategy)
def test_datadiagrammlbasicdef_stringelt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=XYABCDEElt_strategy)
@settings(max_examples=50)
def test_xyabcdeelt_instantiation(instance):
    assert isinstance(instance, XYABCDEElt)

@given(instance=DatadiagramMLBasicDef_NURBSTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_nurbsto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_NURBSTo)

@given(instance=DatadiagramMLBasicDef_XYABCDEElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_xyabcdeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_XYABCDEElt)

@given(instance=XYAElt_strategy)
@settings(max_examples=50)
def test_xyaelt_instantiation(instance):
    assert isinstance(instance, XYAElt)

@given(instance=DatadiagramMLBasicDef_SplineKnot_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_splineknot_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_SplineKnot)

@given(instance=DatadiagramMLBasicDef_PolylineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_polylineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_PolylineTo)

@given(instance=DatadiagramMLBasicDef_ArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_arcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_ArcTo)

@given(instance=XYABElt_strategy)
@settings(max_examples=50)
def test_xyabelt_instantiation(instance):
    assert isinstance(instance, XYABElt)

@given(instance=DatadiagramMLBasicDef_XYABCDElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_xyabcdelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_XYABCDElt)

@given(instance=DatadiagramMLBasicDef_InfiniteLine_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_infiniteline_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_InfiniteLine)

@given(instance=DatadiagramMLBasicDef_XYABElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_xyabelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_XYABElt)

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

@given(instance=DatadiagramMLBasicDef_MoveTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_moveto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_MoveTo)

@given(instance=DatadiagramMLBasicDef_XYAElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_xyaelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_XYAElt)

@given(instance=DatadiagramMLBasicDef_LineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_lineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_LineTo)

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

@given(instance=DatadiagramMLBasicDef_XYElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_xyelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_XYElt)

@given(instance=DatadiagramMLBasicDef_DelElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_delelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_DelElt)



@given(instance=DatadiagramMLBasicDef_DelElt_strategy)
def test_datadiagrammlbasicdef_delelt_del__setter(instance):
    original = instance.del_
    instance.del_ = original
    assert instance.del_ == original

@given(instance=DatadiagramMLBasicDef_IXElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_ixelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_IXElt)



@given(instance=DatadiagramMLBasicDef_IXElt_strategy)
def test_datadiagrammlbasicdef_ixelt_iX_setter(instance):
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

@given(instance=DatadiagramMLBasicDef_UniqueIdElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_uniqueidelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_UniqueIdElt)



@given(instance=DatadiagramMLBasicDef_UniqueIdElt_strategy)
def test_datadiagrammlbasicdef_uniqueidelt_UniqueID_setter(instance):
    original = instance.UniqueID
    instance.UniqueID = original
    assert instance.UniqueID == original

@given(instance=DatadiagramMLBasicDef_IdentifiedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_identifiedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_IdentifiedElt)



@given(instance=DatadiagramMLBasicDef_IdentifiedElt_strategy)
def test_datadiagrammlbasicdef_identifiedelt_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=DatadiagramMLBasicDef_NamedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_namedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_NamedElt)



@given(instance=DatadiagramMLBasicDef_NamedElt_strategy)
def test_datadiagrammlbasicdef_namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=DatadiagramMLBasicDef_NamedElt_strategy)
def test_datadiagrammlbasicdef_namedelt_nameU_setter(instance):
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

@given(instance=DatadiagramMLBasicDef_ConnectsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_connectscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_ConnectsCollection)

@given(instance=DatadiagramMLBasicDef_ShapesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_shapescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_ShapesCollection)

@given(instance=DatadiagramMLBasicDef_Icon_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_icon_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_Icon)



@given(instance=DatadiagramMLBasicDef_Icon_strategy)
def test_datadiagrammlbasicdef_icon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

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

@given(instance=DatadiagramMLBasicDef_DocumentSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_documentsheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_DocumentSheet)

@given(instance=DatadiagramMLBasicDef_ShapeElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_shapeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_ShapeElt)

@given(instance=ShapeElt_strategy)
@settings(max_examples=50)
def test_shapeelt_instantiation(instance):
    assert isinstance(instance, ShapeElt)

@given(instance=DatadiagramMLBasicDef_Text_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_text_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_Text)

@given(instance=DatadiagramMLBasicDef_Geom_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_geom_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_Geom)

@given(instance=ShapesCollection_strategy)
@settings(max_examples=50)
def test_shapescollection_instantiation(instance):
    assert isinstance(instance, ShapesCollection)

@given(instance=DatadiagramMLBasicDef_Shape_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_shape_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_Shape)



@given(instance=DatadiagramMLBasicDef_Shape_strategy)
def test_datadiagrammlbasicdef_shape_textStyle_setter(instance):
    original = instance.textStyle
    instance.textStyle = original
    assert instance.textStyle == original



@given(instance=DatadiagramMLBasicDef_Shape_strategy)
def test_datadiagrammlbasicdef_shape_fillStyle_setter(instance):
    original = instance.fillStyle
    instance.fillStyle = original
    assert instance.fillStyle == original



@given(instance=DatadiagramMLBasicDef_Shape_strategy)
def test_datadiagrammlbasicdef_shape_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=DatadiagramMLBasicDef_EmailRoutingData_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_emailroutingdata_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_EmailRoutingData)



@given(instance=DatadiagramMLBasicDef_EmailRoutingData_strategy)
def test_datadiagrammlbasicdef_emailroutingdata_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=DatadiagramMLBasicDef_EmailRoutingData_strategy)
def test_datadiagrammlbasicdef_emailroutingdata_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=DatadiagramMLBasicDef_VBProjectData_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_vbprojectdata_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_VBProjectData)



@given(instance=DatadiagramMLBasicDef_VBProjectData_strategy)
def test_datadiagrammlbasicdef_vbprojectdata_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=DatadiagramMLBasicDef_CustomProperty_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_customproperty_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_CustomProperty)



@given(instance=DatadiagramMLBasicDef_CustomProperty_strategy)
def test_datadiagrammlbasicdef_customproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=DatadiagramMLBasicDef_CustomProperty_strategy)
def test_datadiagrammlbasicdef_customproperty_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=CustomProperty_strategy)
@settings(max_examples=50)
def test_customproperty_instantiation(instance):
    assert isinstance(instance, CustomProperty)

@given(instance=DatadiagramMLBasicDef_CustomPropertiesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_custompropertiescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_CustomPropertiesCollection)

@given(instance=IdentifiedElt_strategy)
@settings(max_examples=50)
def test_identifiedelt_instantiation(instance):
    assert isinstance(instance, IdentifiedElt)

@given(instance=DatadiagramMLBasicDef_Page_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_page_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_Page)



@given(instance=DatadiagramMLBasicDef_Page_strategy)
def test_datadiagrammlbasicdef_page_reviewerID_setter(instance):
    original = instance.reviewerID
    instance.reviewerID = original
    assert instance.reviewerID == original



@given(instance=DatadiagramMLBasicDef_Page_strategy)
def test_datadiagrammlbasicdef_page_viewScale_setter(instance):
    original = instance.viewScale
    instance.viewScale = original
    assert instance.viewScale == original



@given(instance=DatadiagramMLBasicDef_Page_strategy)
def test_datadiagrammlbasicdef_page_backPage_setter(instance):
    original = instance.backPage
    instance.backPage = original
    assert instance.backPage == original



@given(instance=DatadiagramMLBasicDef_Page_strategy)
def test_datadiagrammlbasicdef_page_viewCenterX_setter(instance):
    original = instance.viewCenterX
    instance.viewCenterX = original
    assert instance.viewCenterX == original



@given(instance=DatadiagramMLBasicDef_Page_strategy)
def test_datadiagrammlbasicdef_page_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=DatadiagramMLBasicDef_Page_strategy)
def test_datadiagrammlbasicdef_page_associatedPage_setter(instance):
    original = instance.associatedPage
    instance.associatedPage = original
    assert instance.associatedPage == original



@given(instance=DatadiagramMLBasicDef_Page_strategy)
def test_datadiagrammlbasicdef_page_ViewCenterY_setter(instance):
    original = instance.ViewCenterY
    instance.ViewCenterY = original
    assert instance.ViewCenterY == original

@given(instance=DatadiagramMLBasicDef_MasterShortCut_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_mastershortcut_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_MasterShortCut)



@given(instance=DatadiagramMLBasicDef_MasterShortCut_strategy)
def test_datadiagrammlbasicdef_mastershortcut_shortcutURL_setter(instance):
    original = instance.shortcutURL
    instance.shortcutURL = original
    assert instance.shortcutURL == original



@given(instance=DatadiagramMLBasicDef_MasterShortCut_strategy)
def test_datadiagrammlbasicdef_mastershortcut_shortcutHelp_setter(instance):
    original = instance.shortcutHelp
    instance.shortcutHelp = original
    assert instance.shortcutHelp == original



@given(instance=DatadiagramMLBasicDef_MasterShortCut_strategy)
def test_datadiagrammlbasicdef_mastershortcut_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original



@given(instance=DatadiagramMLBasicDef_MasterShortCut_strategy)
def test_datadiagrammlbasicdef_mastershortcut_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original



@given(instance=DatadiagramMLBasicDef_MasterShortCut_strategy)
def test_datadiagrammlbasicdef_mastershortcut_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original



@given(instance=DatadiagramMLBasicDef_MasterShortCut_strategy)
def test_datadiagrammlbasicdef_mastershortcut_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original

@given(instance=DatadiagramMLBasicDef_Master_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_master_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_Master)



@given(instance=DatadiagramMLBasicDef_Master_strategy)
def test_datadiagrammlbasicdef_master_iconUpdate_setter(instance):
    original = instance.iconUpdate
    instance.iconUpdate = original
    assert instance.iconUpdate == original



@given(instance=DatadiagramMLBasicDef_Master_strategy)
def test_datadiagrammlbasicdef_master_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original



@given(instance=DatadiagramMLBasicDef_Master_strategy)
def test_datadiagrammlbasicdef_master_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original



@given(instance=DatadiagramMLBasicDef_Master_strategy)
def test_datadiagrammlbasicdef_master_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original



@given(instance=DatadiagramMLBasicDef_Master_strategy)
def test_datadiagrammlbasicdef_master_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original



@given(instance=DatadiagramMLBasicDef_Master_strategy)
def test_datadiagrammlbasicdef_master_baseID_setter(instance):
    original = instance.baseID
    instance.baseID = original
    assert instance.baseID == original



@given(instance=DatadiagramMLBasicDef_Master_strategy)
def test_datadiagrammlbasicdef_master_matchByName_setter(instance):
    original = instance.matchByName
    instance.matchByName = original
    assert instance.matchByName == original



@given(instance=DatadiagramMLBasicDef_Master_strategy)
def test_datadiagrammlbasicdef_master_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=DatadiagramMLBasicDef_PageSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_pagesheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_PageSheet)

@given(instance=DatadiagramMLBasicDef_StyleSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_stylesheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_StyleSheet)

@given(instance=StyleSheet_strategy)
@settings(max_examples=50)
def test_stylesheet_instantiation(instance):
    assert isinstance(instance, StyleSheet)

@given(instance=DatadiagramMLBasicDef_StyleSheetsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_stylesheetscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_StyleSheetsCollection)

@given(instance=VisioDocument_strategy)
@settings(max_examples=50)
def test_visiodocument_instantiation(instance):
    assert isinstance(instance, VisioDocument)

@given(instance=DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_DocumentPropertiesCollection)



@given(instance=DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef_documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef_documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original



@given(instance=DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef_documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef_documentpropertiescollection_alternateNames_setter(instance):
    original = instance.alternateNames
    instance.alternateNames = original
    assert instance.alternateNames == original



@given(instance=DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef_documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef_documentpropertiescollection_buildNumberCreated_setter(instance):
    original = instance.buildNumberCreated
    instance.buildNumberCreated = original
    assert instance.buildNumberCreated == original



@given(instance=DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef_documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef_documentpropertiescollection_creator_setter(instance):
    original = instance.creator
    instance.creator = original
    assert instance.creator == original



@given(instance=DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef_documentpropertiescollection_buildNumberEdited_setter(instance):
    original = instance.buildNumberEdited
    instance.buildNumberEdited = original
    assert instance.buildNumberEdited == original



@given(instance=DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef_documentpropertiescollection_hyperlinkBase_href_setter(instance):
    original = instance.hyperlinkBase_href
    instance.hyperlinkBase_href = original
    assert instance.hyperlinkBase_href == original



@given(instance=DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef_documentpropertiescollection_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original



@given(instance=DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef_documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=DatadiagramMLBasicDef_DocumentPropertiesCollection_strategy)
def test_datadiagrammlbasicdef_documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

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

@given(instance=DatadiagramMLBasicDef_DateTimeType_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_datetimetype_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_DateTimeType)



@given(instance=DatadiagramMLBasicDef_DateTimeType_strategy)
def test_datadiagrammlbasicdef_datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original



@given(instance=DatadiagramMLBasicDef_DateTimeType_strategy)
def test_datadiagrammlbasicdef_datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=DatadiagramMLBasicDef_DateTimeType_strategy)
def test_datadiagrammlbasicdef_datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=DatadiagramMLBasicDef_DateTimeType_strategy)
def test_datadiagrammlbasicdef_datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original



@given(instance=DatadiagramMLBasicDef_DateTimeType_strategy)
def test_datadiagrammlbasicdef_datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original



@given(instance=DatadiagramMLBasicDef_DateTimeType_strategy)
def test_datadiagrammlbasicdef_datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=DatadiagramMLBasicDef_VisioDocument_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_visiodocument_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_VisioDocument)



@given(instance=DatadiagramMLBasicDef_VisioDocument_strategy)
def test_datadiagrammlbasicdef_visiodocument_docLangId_setter(instance):
    original = instance.docLangId
    instance.docLangId = original
    assert instance.docLangId == original



@given(instance=DatadiagramMLBasicDef_VisioDocument_strategy)
def test_datadiagrammlbasicdef_visiodocument_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=DatadiagramMLBasicDef_VisioDocument_strategy)
def test_datadiagrammlbasicdef_visiodocument_metric_setter(instance):
    original = instance.metric
    instance.metric = original
    assert instance.metric == original



@given(instance=DatadiagramMLBasicDef_VisioDocument_strategy)
def test_datadiagrammlbasicdef_visiodocument_buildnum_setter(instance):
    original = instance.buildnum
    instance.buildnum = original
    assert instance.buildnum == original



@given(instance=DatadiagramMLBasicDef_VisioDocument_strategy)
def test_datadiagrammlbasicdef_visiodocument_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=DatadiagramMLBasicDef_VisioDocument_strategy)
def test_datadiagrammlbasicdef_visiodocument_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=DatadiagramMLBasicDef_CellType_strategy)
@settings(max_examples=50)
def test_datadiagrammlbasicdef_celltype_instantiation(instance):
    assert isinstance(instance, DatadiagramMLBasicDef_CellType)



@given(instance=DatadiagramMLBasicDef_CellType_strategy)
def test_datadiagrammlbasicdef_celltype_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original



@given(instance=DatadiagramMLBasicDef_CellType_strategy)
def test_datadiagrammlbasicdef_celltype_err_setter(instance):
    original = instance.err
    instance.err = original
    assert instance.err == original



@given(instance=DatadiagramMLBasicDef_CellType_strategy)
def test_datadiagrammlbasicdef_celltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=DatadiagramMLBasicDef_CellType_strategy)
def test_datadiagrammlbasicdef_celltype_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original
