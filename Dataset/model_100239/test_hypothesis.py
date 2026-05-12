import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    XYABElt,
    DatadiagramMLTextFormat_XYABCDElt,
    DatadiagramMLTextFormat_InfiniteLine,
    XYAElt,
    DatadiagramMLTextFormat_XYABElt,
    DatadiagramMLTextFormat_PolylineTo,
    DatadiagramMLTextFormat_SplineKnot,
    DatadiagramMLTextFormat_ArcTo,
    Geom,
    XYElt,
    DatadiagramMLTextFormat_XYAElt,
    DatadiagramMLTextFormat_MoveTo,
    DatadiagramMLTextFormat_LineTo,
    SplineKnot,
    ArcTo,
    NURBSTo,
    SplineStart,
    EllipticalArcTo,
    Ellipse,
    InfiniteLine,
    PolylineTo,
    DatadiagramMLTextFormat_DelElt,
    DatadiagramMLTextFormat_IXElt,
    MoveTo,
    LineTo,
    CellType,
    DelElt,
    IXElt,
    DatadiagramMLTextFormat_XYElt,
    DatadiagramMLTextFormat_NamedElt,
    PageElt,
    MasterElt,
    DatadiagramMLTextFormat_SolutionXML,
    DatadiagramMLTextFormat_HeaderFooter,
    DatadiagramMLTextFormat_EventList,
    DatadiagramMLTextFormat_WindowsInfo,
    DatadiagramMLTextFormat_DocumentSettingsElt,
    DatadiagramMLTextFormat_PageElt,
    DatadiagramMLTextFormat_PrintSetup,
    DatadiagramMLTextFormat_PagesCollection,
    DatadiagramMLTextFormat_MasterElt,
    ConnectsCollection,
    DatadiagramMLTextFormat_Connect,
    Connect,
    DatadiagramMLTextFormat_ConnectsCollection,
    Page,
    DatadiagramMLTextFormat_ShapesCollection,
    DatadiagramMLTextFormat_Icon,
    Icon,
    MasterShortCut,
    Master,
    DatadiagramMLTextFormat_MastersCollection,
    TabsCollection,
    DatadiagramMLTextFormat_Tab,
    Tab,
    DatadiagramMLTextFormat_IXrequiredElt,
    Text,
    DatadiagramMLTextFormat_TextElt,
    XYABCDElt,
    DatadiagramMLTextFormat_SplineStart,
    DatadiagramMLTextFormat_EllipticalArcTo,
    DatadiagramMLTextFormat_Ellipse,
    TextElt,
    DatadiagramMLTextFormat_StringElt,
    XYABCDEElt,
    DatadiagramMLTextFormat_NURBSTo,
    DatadiagramMLTextFormat_XYABCDEElt,
    UniqueIdElt,
    DatadiagramMLTextFormat_ShapeElt,
    ShapeElt,
    DatadiagramMLTextFormat_Geom,
    DatadiagramMLTextFormat_Field,
    DatadiagramMLTextFormat_Text,
    DatadiagramMLTextFormat_TabsCollection,
    DatadiagramMLTextFormat_Char,
    DatadiagramMLTextFormat_Para,
    ShapesCollection,
    DatadiagramMLTextFormat_Shape,
    DatadiagramMLTextFormat_UniqueIdElt,
    DatadiagramMLTextFormat_IdentifiedElt,
    DatadiagramMLTextFormat_VBProjectData,
    PageSheet,
    NamedElt,
    DatadiagramMLTextFormat_DocumentSheet,
    Shape,
    DatadiagramMLTextFormat_PageSheet,
    StyleSheet,
    DatadiagramMLTextFormat_StyleSheetsCollection,
    DatadiagramMLTextFormat_EmailRoutingData,
    FontEntry,
    DatadiagramMLTextFormat_FontsTable,
    FaceName,
    DatadiagramMLTextFormat_FaceNamesTable,
    IdentifiedElt,
    DatadiagramMLTextFormat_StyleSheet,
    DatadiagramMLTextFormat_Page,
    DatadiagramMLTextFormat_MasterShortCut,
    DatadiagramMLTextFormat_FaceName,
    DatadiagramMLTextFormat_Master,
    CustomProperty,
    DatadiagramMLTextFormat_FontEntry,
    DatadiagramMLTextFormat_CustomPropertiesCollection,
    IXrequiredElt,
    DatadiagramMLTextFormat_Fld,
    DatadiagramMLTextFormat_Tp,
    DatadiagramMLTextFormat_Pp,
    DatadiagramMLTextFormat_Cp,
    DatadiagramMLTextFormat_ColorEntry,
    ColorEntry,
    DatadiagramMLTextFormat_ColorsTable,
    DatadiagramMLTextFormat_CustomProperty,
    DateTimeType,
    CustomPropertiesCollection,
    StyleSheetsCollection,
    FaceNamesTable,
    FontsTable,
    PrintSetup,
    ColorsTable,
    VisioDocument,
    DatadiagramMLTextFormat_DocumentPropertiesCollection,
    SolutionXML,
    EmailRoutingData,
    VBProjectData,
    HeaderFooter,
    EventList,
    WindowsInfo,
    PagesCollection,
    MastersCollection,
    DocumentSheet,
    DatadiagramMLTextFormat_DateTimeType,
    DocumentSettingsElt,
    DocumentPropertiesCollection,
    DatadiagramMLTextFormat_VisioDocument,
    DatadiagramMLTextFormat_CellType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xyabelt_is_not_abstract():
    assert not inspect.isabstract(XYABElt)


def test_xyabelt_constructor_exists():
    assert callable(XYABElt.__init__)


def test_xyabelt_constructor_args():
    sig = inspect.signature(XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_XYABCDElt)


def test_datadiagrammltextformat_xyabcdelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_XYABCDElt.__init__)


def test_datadiagrammltextformat_xyabcdelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_infiniteline_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_InfiniteLine)


def test_datadiagrammltextformat_infiniteline_constructor_exists():
    assert callable(DatadiagramMLTextFormat_InfiniteLine.__init__)


def test_datadiagrammltextformat_infiniteline_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_InfiniteLine.__init__)
    params = list(sig.parameters.keys())



def test_xyaelt_is_not_abstract():
    assert not inspect.isabstract(XYAElt)


def test_xyaelt_constructor_exists():
    assert callable(XYAElt.__init__)


def test_xyaelt_constructor_args():
    sig = inspect.signature(XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_xyabelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_XYABElt)


def test_datadiagrammltextformat_xyabelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_XYABElt.__init__)


def test_datadiagrammltextformat_xyabelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_polylineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_PolylineTo)


def test_datadiagrammltextformat_polylineto_constructor_exists():
    assert callable(DatadiagramMLTextFormat_PolylineTo.__init__)


def test_datadiagrammltextformat_polylineto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_PolylineTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_splineknot_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_SplineKnot)


def test_datadiagrammltextformat_splineknot_constructor_exists():
    assert callable(DatadiagramMLTextFormat_SplineKnot.__init__)


def test_datadiagrammltextformat_splineknot_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_SplineKnot.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_arcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_ArcTo)


def test_datadiagrammltextformat_arcto_constructor_exists():
    assert callable(DatadiagramMLTextFormat_ArcTo.__init__)


def test_datadiagrammltextformat_arcto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_ArcTo.__init__)
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



def test_datadiagrammltextformat_xyaelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_XYAElt)


def test_datadiagrammltextformat_xyaelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_XYAElt.__init__)


def test_datadiagrammltextformat_xyaelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_moveto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_MoveTo)


def test_datadiagrammltextformat_moveto_constructor_exists():
    assert callable(DatadiagramMLTextFormat_MoveTo.__init__)


def test_datadiagrammltextformat_moveto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_lineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_LineTo)


def test_datadiagrammltextformat_lineto_constructor_exists():
    assert callable(DatadiagramMLTextFormat_LineTo.__init__)


def test_datadiagrammltextformat_lineto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_LineTo.__init__)
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



def test_datadiagrammltextformat_delelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_DelElt)


def test_datadiagrammltextformat_delelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_DelElt.__init__)


def test_datadiagrammltextformat_delelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_DelElt.__init__)
    params = list(sig.parameters.keys())
    assert "del_" in params, "Missing parameter 'del_'"

def test_datadiagrammltextformat_delelt_has_del_():
    assert hasattr(DatadiagramMLTextFormat_DelElt, "del_")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DelElt.__mro__:
        if "del_" in klass.__dict__:
            descriptor = klass.__dict__["del_"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat_ixelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_IXElt)


def test_datadiagrammltextformat_ixelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_IXElt.__init__)


def test_datadiagrammltextformat_ixelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_IXElt.__init__)
    params = list(sig.parameters.keys())
    assert "iX" in params, "Missing parameter 'iX'"

def test_datadiagrammltextformat_ixelt_has_iX():
    assert hasattr(DatadiagramMLTextFormat_IXElt, "iX")
    descriptor = None
    for klass in DatadiagramMLTextFormat_IXElt.__mro__:
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



def test_datadiagrammltextformat_xyelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_XYElt)


def test_datadiagrammltextformat_xyelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_XYElt.__init__)


def test_datadiagrammltextformat_xyelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_XYElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_namedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_NamedElt)


def test_datadiagrammltextformat_namedelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_NamedElt.__init__)


def test_datadiagrammltextformat_namedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "nameU" in params, "Missing parameter 'nameU'"

def test_datadiagrammltextformat_namedelt_has_name():
    assert hasattr(DatadiagramMLTextFormat_NamedElt, "name")
    descriptor = None
    for klass in DatadiagramMLTextFormat_NamedElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_namedelt_has_nameU():
    assert hasattr(DatadiagramMLTextFormat_NamedElt, "nameU")
    descriptor = None
    for klass in DatadiagramMLTextFormat_NamedElt.__mro__:
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



def test_datadiagrammltextformat_solutionxml_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_SolutionXML)


def test_datadiagrammltextformat_solutionxml_constructor_exists():
    assert callable(DatadiagramMLTextFormat_SolutionXML.__init__)


def test_datadiagrammltextformat_solutionxml_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_SolutionXML.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_headerfooter_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_HeaderFooter)


def test_datadiagrammltextformat_headerfooter_constructor_exists():
    assert callable(DatadiagramMLTextFormat_HeaderFooter.__init__)


def test_datadiagrammltextformat_headerfooter_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_HeaderFooter.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_eventlist_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_EventList)


def test_datadiagrammltextformat_eventlist_constructor_exists():
    assert callable(DatadiagramMLTextFormat_EventList.__init__)


def test_datadiagrammltextformat_eventlist_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_EventList.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_windowsinfo_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_WindowsInfo)


def test_datadiagrammltextformat_windowsinfo_constructor_exists():
    assert callable(DatadiagramMLTextFormat_WindowsInfo.__init__)


def test_datadiagrammltextformat_windowsinfo_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_WindowsInfo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_documentsettingselt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_DocumentSettingsElt)


def test_datadiagrammltextformat_documentsettingselt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_DocumentSettingsElt.__init__)


def test_datadiagrammltextformat_documentsettingselt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_DocumentSettingsElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_pageelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_PageElt)


def test_datadiagrammltextformat_pageelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_PageElt.__init__)


def test_datadiagrammltextformat_pageelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_PageElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_printsetup_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_PrintSetup)


def test_datadiagrammltextformat_printsetup_constructor_exists():
    assert callable(DatadiagramMLTextFormat_PrintSetup.__init__)


def test_datadiagrammltextformat_printsetup_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_PrintSetup.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_pagescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_PagesCollection)


def test_datadiagrammltextformat_pagescollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_PagesCollection.__init__)


def test_datadiagrammltextformat_pagescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_PagesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_masterelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_MasterElt)


def test_datadiagrammltextformat_masterelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_MasterElt.__init__)


def test_datadiagrammltextformat_masterelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_MasterElt.__init__)
    params = list(sig.parameters.keys())



def test_connectscollection_is_not_abstract():
    assert not inspect.isabstract(ConnectsCollection)


def test_connectscollection_constructor_exists():
    assert callable(ConnectsCollection.__init__)


def test_connectscollection_constructor_args():
    sig = inspect.signature(ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_connect_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Connect)


def test_datadiagrammltextformat_connect_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Connect.__init__)


def test_datadiagrammltextformat_connect_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Connect.__init__)
    params = list(sig.parameters.keys())
    assert "fromCell" in params, "Missing parameter 'fromCell'"
    assert "toCell" in params, "Missing parameter 'toCell'"
    assert "fromSheet" in params, "Missing parameter 'fromSheet'"
    assert "toPart" in params, "Missing parameter 'toPart'"
    assert "toSheet" in params, "Missing parameter 'toSheet'"
    assert "fromPart" in params, "Missing parameter 'fromPart'"

def test_datadiagrammltextformat_connect_has_fromCell():
    assert hasattr(DatadiagramMLTextFormat_Connect, "fromCell")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Connect.__mro__:
        if "fromCell" in klass.__dict__:
            descriptor = klass.__dict__["fromCell"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_connect_has_toCell():
    assert hasattr(DatadiagramMLTextFormat_Connect, "toCell")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Connect.__mro__:
        if "toCell" in klass.__dict__:
            descriptor = klass.__dict__["toCell"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_connect_has_fromSheet():
    assert hasattr(DatadiagramMLTextFormat_Connect, "fromSheet")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Connect.__mro__:
        if "fromSheet" in klass.__dict__:
            descriptor = klass.__dict__["fromSheet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_connect_has_toPart():
    assert hasattr(DatadiagramMLTextFormat_Connect, "toPart")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Connect.__mro__:
        if "toPart" in klass.__dict__:
            descriptor = klass.__dict__["toPart"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_connect_has_toSheet():
    assert hasattr(DatadiagramMLTextFormat_Connect, "toSheet")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Connect.__mro__:
        if "toSheet" in klass.__dict__:
            descriptor = klass.__dict__["toSheet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_connect_has_fromPart():
    assert hasattr(DatadiagramMLTextFormat_Connect, "fromPart")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Connect.__mro__:
        if "fromPart" in klass.__dict__:
            descriptor = klass.__dict__["fromPart"]
            break
    assert isinstance(descriptor, property)



def test_connect_is_not_abstract():
    assert not inspect.isabstract(Connect)


def test_connect_constructor_exists():
    assert callable(Connect.__init__)


def test_connect_constructor_args():
    sig = inspect.signature(Connect.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_connectscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_ConnectsCollection)


def test_datadiagrammltextformat_connectscollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_ConnectsCollection.__init__)


def test_datadiagrammltextformat_connectscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_shapescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_ShapesCollection)


def test_datadiagrammltextformat_shapescollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_ShapesCollection.__init__)


def test_datadiagrammltextformat_shapescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_icon_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Icon)


def test_datadiagrammltextformat_icon_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Icon.__init__)


def test_datadiagrammltextformat_icon_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Icon.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammltextformat_icon_has_value():
    assert hasattr(DatadiagramMLTextFormat_Icon, "value")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Icon.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



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



def test_datadiagrammltextformat_masterscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_MastersCollection)


def test_datadiagrammltextformat_masterscollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_MastersCollection.__init__)


def test_datadiagrammltextformat_masterscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_MastersCollection.__init__)
    params = list(sig.parameters.keys())



def test_tabscollection_is_not_abstract():
    assert not inspect.isabstract(TabsCollection)


def test_tabscollection_constructor_exists():
    assert callable(TabsCollection.__init__)


def test_tabscollection_constructor_args():
    sig = inspect.signature(TabsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_tab_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Tab)


def test_datadiagrammltextformat_tab_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Tab.__init__)


def test_datadiagrammltextformat_tab_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Tab.__init__)
    params = list(sig.parameters.keys())



def test_tab_is_not_abstract():
    assert not inspect.isabstract(Tab)


def test_tab_constructor_exists():
    assert callable(Tab.__init__)


def test_tab_constructor_args():
    sig = inspect.signature(Tab.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_ixrequiredelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_IXrequiredElt)


def test_datadiagrammltextformat_ixrequiredelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_IXrequiredElt.__init__)


def test_datadiagrammltextformat_ixrequiredelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_IXrequiredElt.__init__)
    params = list(sig.parameters.keys())
    assert "iX" in params, "Missing parameter 'iX'"

def test_datadiagrammltextformat_ixrequiredelt_has_iX():
    assert hasattr(DatadiagramMLTextFormat_IXrequiredElt, "iX")
    descriptor = None
    for klass in DatadiagramMLTextFormat_IXrequiredElt.__mro__:
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



def test_datadiagrammltextformat_textelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_TextElt)


def test_datadiagrammltextformat_textelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_TextElt.__init__)


def test_datadiagrammltextformat_textelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_TextElt.__init__)
    params = list(sig.parameters.keys())



def test_xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(XYABCDElt)


def test_xyabcdelt_constructor_exists():
    assert callable(XYABCDElt.__init__)


def test_xyabcdelt_constructor_args():
    sig = inspect.signature(XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_splinestart_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_SplineStart)


def test_datadiagrammltextformat_splinestart_constructor_exists():
    assert callable(DatadiagramMLTextFormat_SplineStart.__init__)


def test_datadiagrammltextformat_splinestart_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_SplineStart.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_ellipticalarcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_EllipticalArcTo)


def test_datadiagrammltextformat_ellipticalarcto_constructor_exists():
    assert callable(DatadiagramMLTextFormat_EllipticalArcTo.__init__)


def test_datadiagrammltextformat_ellipticalarcto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_EllipticalArcTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_ellipse_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Ellipse)


def test_datadiagrammltextformat_ellipse_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Ellipse.__init__)


def test_datadiagrammltextformat_ellipse_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_textelt_is_not_abstract():
    assert not inspect.isabstract(TextElt)


def test_textelt_constructor_exists():
    assert callable(TextElt.__init__)


def test_textelt_constructor_args():
    sig = inspect.signature(TextElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_stringelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_StringElt)


def test_datadiagrammltextformat_stringelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_StringElt.__init__)


def test_datadiagrammltextformat_stringelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_StringElt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammltextformat_stringelt_has_value():
    assert hasattr(DatadiagramMLTextFormat_StringElt, "value")
    descriptor = None
    for klass in DatadiagramMLTextFormat_StringElt.__mro__:
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



def test_datadiagrammltextformat_nurbsto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_NURBSTo)


def test_datadiagrammltextformat_nurbsto_constructor_exists():
    assert callable(DatadiagramMLTextFormat_NURBSTo.__init__)


def test_datadiagrammltextformat_nurbsto_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_NURBSTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_xyabcdeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_XYABCDEElt)


def test_datadiagrammltextformat_xyabcdeelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_XYABCDEElt.__init__)


def test_datadiagrammltextformat_xyabcdeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_XYABCDEElt.__init__)
    params = list(sig.parameters.keys())



def test_uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(UniqueIdElt)


def test_uniqueidelt_constructor_exists():
    assert callable(UniqueIdElt.__init__)


def test_uniqueidelt_constructor_args():
    sig = inspect.signature(UniqueIdElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_shapeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_ShapeElt)


def test_datadiagrammltextformat_shapeelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_ShapeElt.__init__)


def test_datadiagrammltextformat_shapeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_shapeelt_is_not_abstract():
    assert not inspect.isabstract(ShapeElt)


def test_shapeelt_constructor_exists():
    assert callable(ShapeElt.__init__)


def test_shapeelt_constructor_args():
    sig = inspect.signature(ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_geom_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Geom)


def test_datadiagrammltextformat_geom_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Geom.__init__)


def test_datadiagrammltextformat_geom_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Geom.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_field_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Field)


def test_datadiagrammltextformat_field_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Field.__init__)


def test_datadiagrammltextformat_field_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Field.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_text_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Text)


def test_datadiagrammltextformat_text_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Text.__init__)


def test_datadiagrammltextformat_text_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Text.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_tabscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_TabsCollection)


def test_datadiagrammltextformat_tabscollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_TabsCollection.__init__)


def test_datadiagrammltextformat_tabscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_TabsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_char_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Char)


def test_datadiagrammltextformat_char_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Char.__init__)


def test_datadiagrammltextformat_char_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Char.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_para_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Para)


def test_datadiagrammltextformat_para_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Para.__init__)


def test_datadiagrammltextformat_para_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Para.__init__)
    params = list(sig.parameters.keys())



def test_shapescollection_is_not_abstract():
    assert not inspect.isabstract(ShapesCollection)


def test_shapescollection_constructor_exists():
    assert callable(ShapesCollection.__init__)


def test_shapescollection_constructor_args():
    sig = inspect.signature(ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_shape_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Shape)


def test_datadiagrammltextformat_shape_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Shape.__init__)


def test_datadiagrammltextformat_shape_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "fillStyle" in params, "Missing parameter 'fillStyle'"
    assert "textStyle" in params, "Missing parameter 'textStyle'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"

def test_datadiagrammltextformat_shape_has_fillStyle():
    assert hasattr(DatadiagramMLTextFormat_Shape, "fillStyle")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Shape.__mro__:
        if "fillStyle" in klass.__dict__:
            descriptor = klass.__dict__["fillStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_shape_has_textStyle():
    assert hasattr(DatadiagramMLTextFormat_Shape, "textStyle")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Shape.__mro__:
        if "textStyle" in klass.__dict__:
            descriptor = klass.__dict__["textStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_shape_has_lineStyle():
    assert hasattr(DatadiagramMLTextFormat_Shape, "lineStyle")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Shape.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat_uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_UniqueIdElt)


def test_datadiagrammltextformat_uniqueidelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_UniqueIdElt.__init__)


def test_datadiagrammltextformat_uniqueidelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_UniqueIdElt.__init__)
    params = list(sig.parameters.keys())
    assert "UniqueID" in params, "Missing parameter 'UniqueID'"

def test_datadiagrammltextformat_uniqueidelt_has_UniqueID():
    assert hasattr(DatadiagramMLTextFormat_UniqueIdElt, "UniqueID")
    descriptor = None
    for klass in DatadiagramMLTextFormat_UniqueIdElt.__mro__:
        if "UniqueID" in klass.__dict__:
            descriptor = klass.__dict__["UniqueID"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat_identifiedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_IdentifiedElt)


def test_datadiagrammltextformat_identifiedelt_constructor_exists():
    assert callable(DatadiagramMLTextFormat_IdentifiedElt.__init__)


def test_datadiagrammltextformat_identifiedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_IdentifiedElt.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_datadiagrammltextformat_identifiedelt_has_ID():
    assert hasattr(DatadiagramMLTextFormat_IdentifiedElt, "ID")
    descriptor = None
    for klass in DatadiagramMLTextFormat_IdentifiedElt.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat_vbprojectdata_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_VBProjectData)


def test_datadiagrammltextformat_vbprojectdata_constructor_exists():
    assert callable(DatadiagramMLTextFormat_VBProjectData.__init__)


def test_datadiagrammltextformat_vbprojectdata_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_VBProjectData.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_datadiagrammltextformat_vbprojectdata_has_data():
    assert hasattr(DatadiagramMLTextFormat_VBProjectData, "data")
    descriptor = None
    for klass in DatadiagramMLTextFormat_VBProjectData.__mro__:
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



def test_datadiagrammltextformat_documentsheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_DocumentSheet)


def test_datadiagrammltextformat_documentsheet_constructor_exists():
    assert callable(DatadiagramMLTextFormat_DocumentSheet.__init__)


def test_datadiagrammltextformat_documentsheet_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_DocumentSheet.__init__)
    params = list(sig.parameters.keys())



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_pagesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_PageSheet)


def test_datadiagrammltextformat_pagesheet_constructor_exists():
    assert callable(DatadiagramMLTextFormat_PageSheet.__init__)


def test_datadiagrammltextformat_pagesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_PageSheet.__init__)
    params = list(sig.parameters.keys())



def test_stylesheet_is_not_abstract():
    assert not inspect.isabstract(StyleSheet)


def test_stylesheet_constructor_exists():
    assert callable(StyleSheet.__init__)


def test_stylesheet_constructor_args():
    sig = inspect.signature(StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_stylesheetscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_StyleSheetsCollection)


def test_datadiagrammltextformat_stylesheetscollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_StyleSheetsCollection.__init__)


def test_datadiagrammltextformat_stylesheetscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_StyleSheetsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_emailroutingdata_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_EmailRoutingData)


def test_datadiagrammltextformat_emailroutingdata_constructor_exists():
    assert callable(DatadiagramMLTextFormat_EmailRoutingData.__init__)


def test_datadiagrammltextformat_emailroutingdata_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_EmailRoutingData.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "data" in params, "Missing parameter 'data'"

def test_datadiagrammltextformat_emailroutingdata_has_size():
    assert hasattr(DatadiagramMLTextFormat_EmailRoutingData, "size")
    descriptor = None
    for klass in DatadiagramMLTextFormat_EmailRoutingData.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_emailroutingdata_has_data():
    assert hasattr(DatadiagramMLTextFormat_EmailRoutingData, "data")
    descriptor = None
    for klass in DatadiagramMLTextFormat_EmailRoutingData.__mro__:
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



def test_datadiagrammltextformat_fontstable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_FontsTable)


def test_datadiagrammltextformat_fontstable_constructor_exists():
    assert callable(DatadiagramMLTextFormat_FontsTable.__init__)


def test_datadiagrammltextformat_fontstable_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_FontsTable.__init__)
    params = list(sig.parameters.keys())



def test_facename_is_not_abstract():
    assert not inspect.isabstract(FaceName)


def test_facename_constructor_exists():
    assert callable(FaceName.__init__)


def test_facename_constructor_args():
    sig = inspect.signature(FaceName.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_facenamestable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_FaceNamesTable)


def test_datadiagrammltextformat_facenamestable_constructor_exists():
    assert callable(DatadiagramMLTextFormat_FaceNamesTable.__init__)


def test_datadiagrammltextformat_facenamestable_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_FaceNamesTable.__init__)
    params = list(sig.parameters.keys())



def test_identifiedelt_is_not_abstract():
    assert not inspect.isabstract(IdentifiedElt)


def test_identifiedelt_constructor_exists():
    assert callable(IdentifiedElt.__init__)


def test_identifiedelt_constructor_args():
    sig = inspect.signature(IdentifiedElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_stylesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_StyleSheet)


def test_datadiagrammltextformat_stylesheet_constructor_exists():
    assert callable(DatadiagramMLTextFormat_StyleSheet.__init__)


def test_datadiagrammltextformat_stylesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_page_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Page)


def test_datadiagrammltextformat_page_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Page.__init__)


def test_datadiagrammltextformat_page_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Page.__init__)
    params = list(sig.parameters.keys())
    assert "viewCenterX" in params, "Missing parameter 'viewCenterX'"
    assert "background" in params, "Missing parameter 'background'"
    assert "ViewCenterY" in params, "Missing parameter 'ViewCenterY'"
    assert "backPage" in params, "Missing parameter 'backPage'"
    assert "associatedPage" in params, "Missing parameter 'associatedPage'"
    assert "reviewerID" in params, "Missing parameter 'reviewerID'"
    assert "viewScale" in params, "Missing parameter 'viewScale'"

def test_datadiagrammltextformat_page_has_viewCenterX():
    assert hasattr(DatadiagramMLTextFormat_Page, "viewCenterX")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Page.__mro__:
        if "viewCenterX" in klass.__dict__:
            descriptor = klass.__dict__["viewCenterX"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_page_has_background():
    assert hasattr(DatadiagramMLTextFormat_Page, "background")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Page.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_page_has_ViewCenterY():
    assert hasattr(DatadiagramMLTextFormat_Page, "ViewCenterY")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Page.__mro__:
        if "ViewCenterY" in klass.__dict__:
            descriptor = klass.__dict__["ViewCenterY"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_page_has_backPage():
    assert hasattr(DatadiagramMLTextFormat_Page, "backPage")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Page.__mro__:
        if "backPage" in klass.__dict__:
            descriptor = klass.__dict__["backPage"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_page_has_associatedPage():
    assert hasattr(DatadiagramMLTextFormat_Page, "associatedPage")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Page.__mro__:
        if "associatedPage" in klass.__dict__:
            descriptor = klass.__dict__["associatedPage"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_page_has_reviewerID():
    assert hasattr(DatadiagramMLTextFormat_Page, "reviewerID")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Page.__mro__:
        if "reviewerID" in klass.__dict__:
            descriptor = klass.__dict__["reviewerID"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_page_has_viewScale():
    assert hasattr(DatadiagramMLTextFormat_Page, "viewScale")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Page.__mro__:
        if "viewScale" in klass.__dict__:
            descriptor = klass.__dict__["viewScale"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat_mastershortcut_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_MasterShortCut)


def test_datadiagrammltextformat_mastershortcut_constructor_exists():
    assert callable(DatadiagramMLTextFormat_MasterShortCut.__init__)


def test_datadiagrammltextformat_mastershortcut_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_MasterShortCut.__init__)
    params = list(sig.parameters.keys())
    assert "shortcutURL" in params, "Missing parameter 'shortcutURL'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "shortcutHelp" in params, "Missing parameter 'shortcutHelp'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"

def test_datadiagrammltextformat_mastershortcut_has_shortcutURL():
    assert hasattr(DatadiagramMLTextFormat_MasterShortCut, "shortcutURL")
    descriptor = None
    for klass in DatadiagramMLTextFormat_MasterShortCut.__mro__:
        if "shortcutURL" in klass.__dict__:
            descriptor = klass.__dict__["shortcutURL"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_mastershortcut_has_patternFlags():
    assert hasattr(DatadiagramMLTextFormat_MasterShortCut, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLTextFormat_MasterShortCut.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_mastershortcut_has_shortcutHelp():
    assert hasattr(DatadiagramMLTextFormat_MasterShortCut, "shortcutHelp")
    descriptor = None
    for klass in DatadiagramMLTextFormat_MasterShortCut.__mro__:
        if "shortcutHelp" in klass.__dict__:
            descriptor = klass.__dict__["shortcutHelp"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_mastershortcut_has_alignName():
    assert hasattr(DatadiagramMLTextFormat_MasterShortCut, "alignName")
    descriptor = None
    for klass in DatadiagramMLTextFormat_MasterShortCut.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_mastershortcut_has_prompt():
    assert hasattr(DatadiagramMLTextFormat_MasterShortCut, "prompt")
    descriptor = None
    for klass in DatadiagramMLTextFormat_MasterShortCut.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_mastershortcut_has_iconSize():
    assert hasattr(DatadiagramMLTextFormat_MasterShortCut, "iconSize")
    descriptor = None
    for klass in DatadiagramMLTextFormat_MasterShortCut.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat_facename_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_FaceName)


def test_datadiagrammltextformat_facename_constructor_exists():
    assert callable(DatadiagramMLTextFormat_FaceName.__init__)


def test_datadiagrammltextformat_facename_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_FaceName.__init__)
    params = list(sig.parameters.keys())
    assert "charSet" in params, "Missing parameter 'charSet'"
    assert "unicodeRanges" in params, "Missing parameter 'unicodeRanges'"
    assert "flags" in params, "Missing parameter 'flags'"
    assert "name" in params, "Missing parameter 'name'"
    assert "panos" in params, "Missing parameter 'panos'"

def test_datadiagrammltextformat_facename_has_charSet():
    assert hasattr(DatadiagramMLTextFormat_FaceName, "charSet")
    descriptor = None
    for klass in DatadiagramMLTextFormat_FaceName.__mro__:
        if "charSet" in klass.__dict__:
            descriptor = klass.__dict__["charSet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_facename_has_unicodeRanges():
    assert hasattr(DatadiagramMLTextFormat_FaceName, "unicodeRanges")
    descriptor = None
    for klass in DatadiagramMLTextFormat_FaceName.__mro__:
        if "unicodeRanges" in klass.__dict__:
            descriptor = klass.__dict__["unicodeRanges"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_facename_has_flags():
    assert hasattr(DatadiagramMLTextFormat_FaceName, "flags")
    descriptor = None
    for klass in DatadiagramMLTextFormat_FaceName.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_facename_has_name():
    assert hasattr(DatadiagramMLTextFormat_FaceName, "name")
    descriptor = None
    for klass in DatadiagramMLTextFormat_FaceName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_facename_has_panos():
    assert hasattr(DatadiagramMLTextFormat_FaceName, "panos")
    descriptor = None
    for klass in DatadiagramMLTextFormat_FaceName.__mro__:
        if "panos" in klass.__dict__:
            descriptor = klass.__dict__["panos"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat_master_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Master)


def test_datadiagrammltextformat_master_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Master.__init__)


def test_datadiagrammltextformat_master_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Master.__init__)
    params = list(sig.parameters.keys())
    assert "baseID" in params, "Missing parameter 'baseID'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"
    assert "matchByName" in params, "Missing parameter 'matchByName'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "iconUpdate" in params, "Missing parameter 'iconUpdate'"
    assert "prompt" in params, "Missing parameter 'prompt'"

def test_datadiagrammltextformat_master_has_baseID():
    assert hasattr(DatadiagramMLTextFormat_Master, "baseID")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Master.__mro__:
        if "baseID" in klass.__dict__:
            descriptor = klass.__dict__["baseID"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_master_has_alignName():
    assert hasattr(DatadiagramMLTextFormat_Master, "alignName")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Master.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_master_has_iconSize():
    assert hasattr(DatadiagramMLTextFormat_Master, "iconSize")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Master.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_master_has_matchByName():
    assert hasattr(DatadiagramMLTextFormat_Master, "matchByName")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Master.__mro__:
        if "matchByName" in klass.__dict__:
            descriptor = klass.__dict__["matchByName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_master_has_patternFlags():
    assert hasattr(DatadiagramMLTextFormat_Master, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Master.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_master_has_hidden():
    assert hasattr(DatadiagramMLTextFormat_Master, "hidden")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Master.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_master_has_iconUpdate():
    assert hasattr(DatadiagramMLTextFormat_Master, "iconUpdate")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Master.__mro__:
        if "iconUpdate" in klass.__dict__:
            descriptor = klass.__dict__["iconUpdate"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_master_has_prompt():
    assert hasattr(DatadiagramMLTextFormat_Master, "prompt")
    descriptor = None
    for klass in DatadiagramMLTextFormat_Master.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)



def test_customproperty_is_not_abstract():
    assert not inspect.isabstract(CustomProperty)


def test_customproperty_constructor_exists():
    assert callable(CustomProperty.__init__)


def test_customproperty_constructor_args():
    sig = inspect.signature(CustomProperty.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_fontentry_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_FontEntry)


def test_datadiagrammltextformat_fontentry_constructor_exists():
    assert callable(DatadiagramMLTextFormat_FontEntry.__init__)


def test_datadiagrammltextformat_fontentry_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_FontEntry.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "charSet" in params, "Missing parameter 'charSet'"
    assert "pitchAndFamily" in params, "Missing parameter 'pitchAndFamily'"
    assert "name" in params, "Missing parameter 'name'"
    assert "unicode" in params, "Missing parameter 'unicode'"
    assert "attributes" in params, "Missing parameter 'attributes'"

def test_datadiagrammltextformat_fontentry_has_weight():
    assert hasattr(DatadiagramMLTextFormat_FontEntry, "weight")
    descriptor = None
    for klass in DatadiagramMLTextFormat_FontEntry.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_fontentry_has_charSet():
    assert hasattr(DatadiagramMLTextFormat_FontEntry, "charSet")
    descriptor = None
    for klass in DatadiagramMLTextFormat_FontEntry.__mro__:
        if "charSet" in klass.__dict__:
            descriptor = klass.__dict__["charSet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_fontentry_has_pitchAndFamily():
    assert hasattr(DatadiagramMLTextFormat_FontEntry, "pitchAndFamily")
    descriptor = None
    for klass in DatadiagramMLTextFormat_FontEntry.__mro__:
        if "pitchAndFamily" in klass.__dict__:
            descriptor = klass.__dict__["pitchAndFamily"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_fontentry_has_name():
    assert hasattr(DatadiagramMLTextFormat_FontEntry, "name")
    descriptor = None
    for klass in DatadiagramMLTextFormat_FontEntry.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_fontentry_has_unicode():
    assert hasattr(DatadiagramMLTextFormat_FontEntry, "unicode")
    descriptor = None
    for klass in DatadiagramMLTextFormat_FontEntry.__mro__:
        if "unicode" in klass.__dict__:
            descriptor = klass.__dict__["unicode"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_fontentry_has_attributes():
    assert hasattr(DatadiagramMLTextFormat_FontEntry, "attributes")
    descriptor = None
    for klass in DatadiagramMLTextFormat_FontEntry.__mro__:
        if "attributes" in klass.__dict__:
            descriptor = klass.__dict__["attributes"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat_custompropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_CustomPropertiesCollection)


def test_datadiagrammltextformat_custompropertiescollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_CustomPropertiesCollection.__init__)


def test_datadiagrammltextformat_custompropertiescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_CustomPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_ixrequiredelt_is_not_abstract():
    assert not inspect.isabstract(IXrequiredElt)


def test_ixrequiredelt_constructor_exists():
    assert callable(IXrequiredElt.__init__)


def test_ixrequiredelt_constructor_args():
    sig = inspect.signature(IXrequiredElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_fld_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Fld)


def test_datadiagrammltextformat_fld_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Fld.__init__)


def test_datadiagrammltextformat_fld_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Fld.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_tp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Tp)


def test_datadiagrammltextformat_tp_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Tp.__init__)


def test_datadiagrammltextformat_tp_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Tp.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_pp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Pp)


def test_datadiagrammltextformat_pp_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Pp.__init__)


def test_datadiagrammltextformat_pp_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Pp.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_cp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_Cp)


def test_datadiagrammltextformat_cp_constructor_exists():
    assert callable(DatadiagramMLTextFormat_Cp.__init__)


def test_datadiagrammltextformat_cp_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_Cp.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_colorentry_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_ColorEntry)


def test_datadiagrammltextformat_colorentry_constructor_exists():
    assert callable(DatadiagramMLTextFormat_ColorEntry.__init__)


def test_datadiagrammltextformat_colorentry_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_ColorEntry.__init__)
    params = list(sig.parameters.keys())
    assert "rgb" in params, "Missing parameter 'rgb'"

def test_datadiagrammltextformat_colorentry_has_rgb():
    assert hasattr(DatadiagramMLTextFormat_ColorEntry, "rgb")
    descriptor = None
    for klass in DatadiagramMLTextFormat_ColorEntry.__mro__:
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



def test_datadiagrammltextformat_colorstable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_ColorsTable)


def test_datadiagrammltextformat_colorstable_constructor_exists():
    assert callable(DatadiagramMLTextFormat_ColorsTable.__init__)


def test_datadiagrammltextformat_colorstable_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_ColorsTable.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammltextformat_customproperty_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_CustomProperty)


def test_datadiagrammltextformat_customproperty_constructor_exists():
    assert callable(DatadiagramMLTextFormat_CustomProperty.__init__)


def test_datadiagrammltextformat_customproperty_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_CustomProperty.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "name" in params, "Missing parameter 'name'"

def test_datadiagrammltextformat_customproperty_has_dataType():
    assert hasattr(DatadiagramMLTextFormat_CustomProperty, "dataType")
    descriptor = None
    for klass in DatadiagramMLTextFormat_CustomProperty.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_customproperty_has_name():
    assert hasattr(DatadiagramMLTextFormat_CustomProperty, "name")
    descriptor = None
    for klass in DatadiagramMLTextFormat_CustomProperty.__mro__:
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



def test_datadiagrammltextformat_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_DocumentPropertiesCollection)


def test_datadiagrammltextformat_documentpropertiescollection_constructor_exists():
    assert callable(DatadiagramMLTextFormat_DocumentPropertiesCollection.__init__)


def test_datadiagrammltextformat_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "company" in params, "Missing parameter 'company'"
    assert "template" in params, "Missing parameter 'template'"
    assert "buildNumberCreated" in params, "Missing parameter 'buildNumberCreated'"
    assert "hyperlinkBase_href" in params, "Missing parameter 'hyperlinkBase_href'"
    assert "description" in params, "Missing parameter 'description'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "title" in params, "Missing parameter 'title'"
    assert "creator" in params, "Missing parameter 'creator'"
    assert "category" in params, "Missing parameter 'category'"
    assert "alternateNames" in params, "Missing parameter 'alternateNames'"
    assert "buildNumberEdited" in params, "Missing parameter 'buildNumberEdited'"

def test_datadiagrammltextformat_documentpropertiescollection_has_subject():
    assert hasattr(DatadiagramMLTextFormat_DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_documentpropertiescollection_has_manager():
    assert hasattr(DatadiagramMLTextFormat_DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_documentpropertiescollection_has_company():
    assert hasattr(DatadiagramMLTextFormat_DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_documentpropertiescollection_has_template():
    assert hasattr(DatadiagramMLTextFormat_DocumentPropertiesCollection, "template")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DocumentPropertiesCollection.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_documentpropertiescollection_has_buildNumberCreated():
    assert hasattr(DatadiagramMLTextFormat_DocumentPropertiesCollection, "buildNumberCreated")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DocumentPropertiesCollection.__mro__:
        if "buildNumberCreated" in klass.__dict__:
            descriptor = klass.__dict__["buildNumberCreated"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_documentpropertiescollection_has_hyperlinkBase_href():
    assert hasattr(DatadiagramMLTextFormat_DocumentPropertiesCollection, "hyperlinkBase_href")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase_href" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase_href"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_documentpropertiescollection_has_description():
    assert hasattr(DatadiagramMLTextFormat_DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_documentpropertiescollection_has_keywords():
    assert hasattr(DatadiagramMLTextFormat_DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_documentpropertiescollection_has_title():
    assert hasattr(DatadiagramMLTextFormat_DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_documentpropertiescollection_has_creator():
    assert hasattr(DatadiagramMLTextFormat_DocumentPropertiesCollection, "creator")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DocumentPropertiesCollection.__mro__:
        if "creator" in klass.__dict__:
            descriptor = klass.__dict__["creator"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_documentpropertiescollection_has_category():
    assert hasattr(DatadiagramMLTextFormat_DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_documentpropertiescollection_has_alternateNames():
    assert hasattr(DatadiagramMLTextFormat_DocumentPropertiesCollection, "alternateNames")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DocumentPropertiesCollection.__mro__:
        if "alternateNames" in klass.__dict__:
            descriptor = klass.__dict__["alternateNames"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_documentpropertiescollection_has_buildNumberEdited():
    assert hasattr(DatadiagramMLTextFormat_DocumentPropertiesCollection, "buildNumberEdited")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DocumentPropertiesCollection.__mro__:
        if "buildNumberEdited" in klass.__dict__:
            descriptor = klass.__dict__["buildNumberEdited"]
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



def test_datadiagrammltextformat_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_DateTimeType)


def test_datadiagrammltextformat_datetimetype_constructor_exists():
    assert callable(DatadiagramMLTextFormat_DateTimeType.__init__)


def test_datadiagrammltextformat_datetimetype_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "day" in params, "Missing parameter 'day'"
    assert "second" in params, "Missing parameter 'second'"
    assert "year" in params, "Missing parameter 'year'"
    assert "minute" in params, "Missing parameter 'minute'"

def test_datadiagrammltextformat_datetimetype_has_month():
    assert hasattr(DatadiagramMLTextFormat_DateTimeType, "month")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_datetimetype_has_hour():
    assert hasattr(DatadiagramMLTextFormat_DateTimeType, "hour")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_datetimetype_has_day():
    assert hasattr(DatadiagramMLTextFormat_DateTimeType, "day")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_datetimetype_has_second():
    assert hasattr(DatadiagramMLTextFormat_DateTimeType, "second")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_datetimetype_has_year():
    assert hasattr(DatadiagramMLTextFormat_DateTimeType, "year")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_datetimetype_has_minute():
    assert hasattr(DatadiagramMLTextFormat_DateTimeType, "minute")
    descriptor = None
    for klass in DatadiagramMLTextFormat_DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
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



def test_datadiagrammltextformat_visiodocument_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_VisioDocument)


def test_datadiagrammltextformat_visiodocument_constructor_exists():
    assert callable(DatadiagramMLTextFormat_VisioDocument.__init__)


def test_datadiagrammltextformat_visiodocument_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_VisioDocument.__init__)
    params = list(sig.parameters.keys())
    assert "docLangId" in params, "Missing parameter 'docLangId'"
    assert "version" in params, "Missing parameter 'version'"
    assert "start" in params, "Missing parameter 'start'"
    assert "metric" in params, "Missing parameter 'metric'"
    assert "key" in params, "Missing parameter 'key'"
    assert "buildnum" in params, "Missing parameter 'buildnum'"

def test_datadiagrammltextformat_visiodocument_has_docLangId():
    assert hasattr(DatadiagramMLTextFormat_VisioDocument, "docLangId")
    descriptor = None
    for klass in DatadiagramMLTextFormat_VisioDocument.__mro__:
        if "docLangId" in klass.__dict__:
            descriptor = klass.__dict__["docLangId"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_visiodocument_has_version():
    assert hasattr(DatadiagramMLTextFormat_VisioDocument, "version")
    descriptor = None
    for klass in DatadiagramMLTextFormat_VisioDocument.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_visiodocument_has_start():
    assert hasattr(DatadiagramMLTextFormat_VisioDocument, "start")
    descriptor = None
    for klass in DatadiagramMLTextFormat_VisioDocument.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_visiodocument_has_metric():
    assert hasattr(DatadiagramMLTextFormat_VisioDocument, "metric")
    descriptor = None
    for klass in DatadiagramMLTextFormat_VisioDocument.__mro__:
        if "metric" in klass.__dict__:
            descriptor = klass.__dict__["metric"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_visiodocument_has_key():
    assert hasattr(DatadiagramMLTextFormat_VisioDocument, "key")
    descriptor = None
    for klass in DatadiagramMLTextFormat_VisioDocument.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_visiodocument_has_buildnum():
    assert hasattr(DatadiagramMLTextFormat_VisioDocument, "buildnum")
    descriptor = None
    for klass in DatadiagramMLTextFormat_VisioDocument.__mro__:
        if "buildnum" in klass.__dict__:
            descriptor = klass.__dict__["buildnum"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammltextformat_celltype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLTextFormat_CellType)


def test_datadiagrammltextformat_celltype_constructor_exists():
    assert callable(DatadiagramMLTextFormat_CellType.__init__)


def test_datadiagrammltextformat_celltype_constructor_args():
    sig = inspect.signature(DatadiagramMLTextFormat_CellType.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "err" in params, "Missing parameter 'err'"
    assert "formula" in params, "Missing parameter 'formula'"
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammltextformat_celltype_has_unit():
    assert hasattr(DatadiagramMLTextFormat_CellType, "unit")
    descriptor = None
    for klass in DatadiagramMLTextFormat_CellType.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_celltype_has_err():
    assert hasattr(DatadiagramMLTextFormat_CellType, "err")
    descriptor = None
    for klass in DatadiagramMLTextFormat_CellType.__mro__:
        if "err" in klass.__dict__:
            descriptor = klass.__dict__["err"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_celltype_has_formula():
    assert hasattr(DatadiagramMLTextFormat_CellType, "formula")
    descriptor = None
    for klass in DatadiagramMLTextFormat_CellType.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammltextformat_celltype_has_value():
    assert hasattr(DatadiagramMLTextFormat_CellType, "value")
    descriptor = None
    for klass in DatadiagramMLTextFormat_CellType.__mro__:
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
XYABElt_strategy = st.builds(
    XYABElt,
)
DatadiagramMLTextFormat_XYABCDElt_strategy = st.builds(
    DatadiagramMLTextFormat_XYABCDElt,
)
DatadiagramMLTextFormat_InfiniteLine_strategy = st.builds(
    DatadiagramMLTextFormat_InfiniteLine,
)
XYAElt_strategy = st.builds(
    XYAElt,
)
DatadiagramMLTextFormat_XYABElt_strategy = st.builds(
    DatadiagramMLTextFormat_XYABElt,
)
DatadiagramMLTextFormat_PolylineTo_strategy = st.builds(
    DatadiagramMLTextFormat_PolylineTo,
)
DatadiagramMLTextFormat_SplineKnot_strategy = st.builds(
    DatadiagramMLTextFormat_SplineKnot,
)
DatadiagramMLTextFormat_ArcTo_strategy = st.builds(
    DatadiagramMLTextFormat_ArcTo,
)
Geom_strategy = st.builds(
    Geom,
)
XYElt_strategy = st.builds(
    XYElt,
)
DatadiagramMLTextFormat_XYAElt_strategy = st.builds(
    DatadiagramMLTextFormat_XYAElt,
)
DatadiagramMLTextFormat_MoveTo_strategy = st.builds(
    DatadiagramMLTextFormat_MoveTo,
)
DatadiagramMLTextFormat_LineTo_strategy = st.builds(
    DatadiagramMLTextFormat_LineTo,
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
DatadiagramMLTextFormat_DelElt_strategy = st.builds(
    DatadiagramMLTextFormat_DelElt,
    del_=
        safe_text
)
DatadiagramMLTextFormat_IXElt_strategy = st.builds(
    DatadiagramMLTextFormat_IXElt,
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
DatadiagramMLTextFormat_XYElt_strategy = st.builds(
    DatadiagramMLTextFormat_XYElt,
)
DatadiagramMLTextFormat_NamedElt_strategy = st.builds(
    DatadiagramMLTextFormat_NamedElt,
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
DatadiagramMLTextFormat_SolutionXML_strategy = st.builds(
    DatadiagramMLTextFormat_SolutionXML,
)
DatadiagramMLTextFormat_HeaderFooter_strategy = st.builds(
    DatadiagramMLTextFormat_HeaderFooter,
)
DatadiagramMLTextFormat_EventList_strategy = st.builds(
    DatadiagramMLTextFormat_EventList,
)
DatadiagramMLTextFormat_WindowsInfo_strategy = st.builds(
    DatadiagramMLTextFormat_WindowsInfo,
)
DatadiagramMLTextFormat_DocumentSettingsElt_strategy = st.builds(
    DatadiagramMLTextFormat_DocumentSettingsElt,
)
DatadiagramMLTextFormat_PageElt_strategy = st.builds(
    DatadiagramMLTextFormat_PageElt,
)
DatadiagramMLTextFormat_PrintSetup_strategy = st.builds(
    DatadiagramMLTextFormat_PrintSetup,
)
DatadiagramMLTextFormat_PagesCollection_strategy = st.builds(
    DatadiagramMLTextFormat_PagesCollection,
)
DatadiagramMLTextFormat_MasterElt_strategy = st.builds(
    DatadiagramMLTextFormat_MasterElt,
)
ConnectsCollection_strategy = st.builds(
    ConnectsCollection,
)
DatadiagramMLTextFormat_Connect_strategy = st.builds(
    DatadiagramMLTextFormat_Connect,
    fromCell=
        safe_text,
    toCell=
        safe_text,
    fromSheet=
        safe_text,
    toPart=
        safe_text,
    toSheet=
        safe_text,
    fromPart=
        safe_text
)
Connect_strategy = st.builds(
    Connect,
)
DatadiagramMLTextFormat_ConnectsCollection_strategy = st.builds(
    DatadiagramMLTextFormat_ConnectsCollection,
)
Page_strategy = st.builds(
    Page,
)
DatadiagramMLTextFormat_ShapesCollection_strategy = st.builds(
    DatadiagramMLTextFormat_ShapesCollection,
)
DatadiagramMLTextFormat_Icon_strategy = st.builds(
    DatadiagramMLTextFormat_Icon,
    value=
        safe_text
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
DatadiagramMLTextFormat_MastersCollection_strategy = st.builds(
    DatadiagramMLTextFormat_MastersCollection,
)
TabsCollection_strategy = st.builds(
    TabsCollection,
)
DatadiagramMLTextFormat_Tab_strategy = st.builds(
    DatadiagramMLTextFormat_Tab,
)
Tab_strategy = st.builds(
    Tab,
)
DatadiagramMLTextFormat_IXrequiredElt_strategy = st.builds(
    DatadiagramMLTextFormat_IXrequiredElt,
    iX=
        safe_text
)
Text_strategy = st.builds(
    Text,
)
DatadiagramMLTextFormat_TextElt_strategy = st.builds(
    DatadiagramMLTextFormat_TextElt,
)
XYABCDElt_strategy = st.builds(
    XYABCDElt,
)
DatadiagramMLTextFormat_SplineStart_strategy = st.builds(
    DatadiagramMLTextFormat_SplineStart,
)
DatadiagramMLTextFormat_EllipticalArcTo_strategy = st.builds(
    DatadiagramMLTextFormat_EllipticalArcTo,
)
DatadiagramMLTextFormat_Ellipse_strategy = st.builds(
    DatadiagramMLTextFormat_Ellipse,
)
TextElt_strategy = st.builds(
    TextElt,
)
DatadiagramMLTextFormat_StringElt_strategy = st.builds(
    DatadiagramMLTextFormat_StringElt,
    value=
        safe_text
)
XYABCDEElt_strategy = st.builds(
    XYABCDEElt,
)
DatadiagramMLTextFormat_NURBSTo_strategy = st.builds(
    DatadiagramMLTextFormat_NURBSTo,
)
DatadiagramMLTextFormat_XYABCDEElt_strategy = st.builds(
    DatadiagramMLTextFormat_XYABCDEElt,
)
UniqueIdElt_strategy = st.builds(
    UniqueIdElt,
)
DatadiagramMLTextFormat_ShapeElt_strategy = st.builds(
    DatadiagramMLTextFormat_ShapeElt,
)
ShapeElt_strategy = st.builds(
    ShapeElt,
)
DatadiagramMLTextFormat_Geom_strategy = st.builds(
    DatadiagramMLTextFormat_Geom,
)
DatadiagramMLTextFormat_Field_strategy = st.builds(
    DatadiagramMLTextFormat_Field,
)
DatadiagramMLTextFormat_Text_strategy = st.builds(
    DatadiagramMLTextFormat_Text,
)
DatadiagramMLTextFormat_TabsCollection_strategy = st.builds(
    DatadiagramMLTextFormat_TabsCollection,
)
DatadiagramMLTextFormat_Char_strategy = st.builds(
    DatadiagramMLTextFormat_Char,
)
DatadiagramMLTextFormat_Para_strategy = st.builds(
    DatadiagramMLTextFormat_Para,
)
ShapesCollection_strategy = st.builds(
    ShapesCollection,
)
DatadiagramMLTextFormat_Shape_strategy = st.builds(
    DatadiagramMLTextFormat_Shape,
    fillStyle=
        safe_text,
    textStyle=
        safe_text,
    lineStyle=
        safe_text
)
DatadiagramMLTextFormat_UniqueIdElt_strategy = st.builds(
    DatadiagramMLTextFormat_UniqueIdElt,
    UniqueID=
        safe_text
)
DatadiagramMLTextFormat_IdentifiedElt_strategy = st.builds(
    DatadiagramMLTextFormat_IdentifiedElt,
    ID=
        safe_text
)
DatadiagramMLTextFormat_VBProjectData_strategy = st.builds(
    DatadiagramMLTextFormat_VBProjectData,
    data=
        safe_text
)
PageSheet_strategy = st.builds(
    PageSheet,
)
NamedElt_strategy = st.builds(
    NamedElt,
)
DatadiagramMLTextFormat_DocumentSheet_strategy = st.builds(
    DatadiagramMLTextFormat_DocumentSheet,
)
Shape_strategy = st.builds(
    Shape,
)
DatadiagramMLTextFormat_PageSheet_strategy = st.builds(
    DatadiagramMLTextFormat_PageSheet,
)
StyleSheet_strategy = st.builds(
    StyleSheet,
)
DatadiagramMLTextFormat_StyleSheetsCollection_strategy = st.builds(
    DatadiagramMLTextFormat_StyleSheetsCollection,
)
DatadiagramMLTextFormat_EmailRoutingData_strategy = st.builds(
    DatadiagramMLTextFormat_EmailRoutingData,
    size=
        safe_text,
    data=
        safe_text
)
FontEntry_strategy = st.builds(
    FontEntry,
)
DatadiagramMLTextFormat_FontsTable_strategy = st.builds(
    DatadiagramMLTextFormat_FontsTable,
)
FaceName_strategy = st.builds(
    FaceName,
)
DatadiagramMLTextFormat_FaceNamesTable_strategy = st.builds(
    DatadiagramMLTextFormat_FaceNamesTable,
)
IdentifiedElt_strategy = st.builds(
    IdentifiedElt,
)
DatadiagramMLTextFormat_StyleSheet_strategy = st.builds(
    DatadiagramMLTextFormat_StyleSheet,
)
DatadiagramMLTextFormat_Page_strategy = st.builds(
    DatadiagramMLTextFormat_Page,
    viewCenterX=
        safe_text,
    background=
        safe_text,
    ViewCenterY=
        safe_text,
    backPage=
        safe_text,
    associatedPage=
        safe_text,
    reviewerID=
        safe_text,
    viewScale=
        safe_text
)
DatadiagramMLTextFormat_MasterShortCut_strategy = st.builds(
    DatadiagramMLTextFormat_MasterShortCut,
    shortcutURL=
        safe_text,
    patternFlags=
        safe_text,
    shortcutHelp=
        safe_text,
    alignName=
        safe_text,
    prompt=
        safe_text,
    iconSize=
        safe_text
)
DatadiagramMLTextFormat_FaceName_strategy = st.builds(
    DatadiagramMLTextFormat_FaceName,
    charSet=
        safe_text,
    unicodeRanges=
        safe_text,
    flags=
        safe_text,
    name=
        safe_text,
    panos=
        safe_text
)
DatadiagramMLTextFormat_Master_strategy = st.builds(
    DatadiagramMLTextFormat_Master,
    baseID=
        safe_text,
    alignName=
        safe_text,
    iconSize=
        safe_text,
    matchByName=
        safe_text,
    patternFlags=
        safe_text,
    hidden=
        safe_text,
    iconUpdate=
        safe_text,
    prompt=
        safe_text
)
CustomProperty_strategy = st.builds(
    CustomProperty,
)
DatadiagramMLTextFormat_FontEntry_strategy = st.builds(
    DatadiagramMLTextFormat_FontEntry,
    weight=
        safe_text,
    charSet=
        safe_text,
    pitchAndFamily=
        safe_text,
    name=
        safe_text,
    unicode=
        safe_text,
    attributes=
        safe_text
)
DatadiagramMLTextFormat_CustomPropertiesCollection_strategy = st.builds(
    DatadiagramMLTextFormat_CustomPropertiesCollection,
)
IXrequiredElt_strategy = st.builds(
    IXrequiredElt,
)
DatadiagramMLTextFormat_Fld_strategy = st.builds(
    DatadiagramMLTextFormat_Fld,
)
DatadiagramMLTextFormat_Tp_strategy = st.builds(
    DatadiagramMLTextFormat_Tp,
)
DatadiagramMLTextFormat_Pp_strategy = st.builds(
    DatadiagramMLTextFormat_Pp,
)
DatadiagramMLTextFormat_Cp_strategy = st.builds(
    DatadiagramMLTextFormat_Cp,
)
DatadiagramMLTextFormat_ColorEntry_strategy = st.builds(
    DatadiagramMLTextFormat_ColorEntry,
    rgb=
        safe_text
)
ColorEntry_strategy = st.builds(
    ColorEntry,
)
DatadiagramMLTextFormat_ColorsTable_strategy = st.builds(
    DatadiagramMLTextFormat_ColorsTable,
)
DatadiagramMLTextFormat_CustomProperty_strategy = st.builds(
    DatadiagramMLTextFormat_CustomProperty,
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
DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy = st.builds(
    DatadiagramMLTextFormat_DocumentPropertiesCollection,
    subject=
        safe_text,
    manager=
        safe_text,
    company=
        safe_text,
    template=
        safe_text,
    buildNumberCreated=
        safe_text,
    hyperlinkBase_href=
        safe_text,
    description=
        safe_text,
    keywords=
        safe_text,
    title=
        safe_text,
    creator=
        safe_text,
    category=
        safe_text,
    alternateNames=
        safe_text,
    buildNumberEdited=
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
PagesCollection_strategy = st.builds(
    PagesCollection,
)
MastersCollection_strategy = st.builds(
    MastersCollection,
)
DocumentSheet_strategy = st.builds(
    DocumentSheet,
)
DatadiagramMLTextFormat_DateTimeType_strategy = st.builds(
    DatadiagramMLTextFormat_DateTimeType,
    month=
        safe_text,
    hour=
        safe_text,
    day=
        safe_text,
    second=
        safe_text,
    year=
        safe_text,
    minute=
        safe_text
)
DocumentSettingsElt_strategy = st.builds(
    DocumentSettingsElt,
)
DocumentPropertiesCollection_strategy = st.builds(
    DocumentPropertiesCollection,
)
DatadiagramMLTextFormat_VisioDocument_strategy = st.builds(
    DatadiagramMLTextFormat_VisioDocument,
    docLangId=
        safe_text,
    version=
        safe_text,
    start=
        safe_text,
    metric=
        safe_text,
    key=
        safe_text,
    buildnum=
        safe_text
)
DatadiagramMLTextFormat_CellType_strategy = st.builds(
    DatadiagramMLTextFormat_CellType,
    unit=
        safe_text,
    err=
        safe_text,
    formula=
        safe_text,
    value=
        safe_text
)

@given(instance=XYABElt_strategy)
@settings(max_examples=50)
def test_xyabelt_instantiation(instance):
    assert isinstance(instance, XYABElt)

@given(instance=DatadiagramMLTextFormat_XYABCDElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_xyabcdelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_XYABCDElt)

@given(instance=DatadiagramMLTextFormat_InfiniteLine_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_infiniteline_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_InfiniteLine)

@given(instance=XYAElt_strategy)
@settings(max_examples=50)
def test_xyaelt_instantiation(instance):
    assert isinstance(instance, XYAElt)

@given(instance=DatadiagramMLTextFormat_XYABElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_xyabelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_XYABElt)

@given(instance=DatadiagramMLTextFormat_PolylineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_polylineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_PolylineTo)

@given(instance=DatadiagramMLTextFormat_SplineKnot_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_splineknot_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_SplineKnot)

@given(instance=DatadiagramMLTextFormat_ArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_arcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_ArcTo)

@given(instance=Geom_strategy)
@settings(max_examples=50)
def test_geom_instantiation(instance):
    assert isinstance(instance, Geom)

@given(instance=XYElt_strategy)
@settings(max_examples=50)
def test_xyelt_instantiation(instance):
    assert isinstance(instance, XYElt)

@given(instance=DatadiagramMLTextFormat_XYAElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_xyaelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_XYAElt)

@given(instance=DatadiagramMLTextFormat_MoveTo_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_moveto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_MoveTo)

@given(instance=DatadiagramMLTextFormat_LineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_lineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_LineTo)

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

@given(instance=DatadiagramMLTextFormat_DelElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_delelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_DelElt)



@given(instance=DatadiagramMLTextFormat_DelElt_strategy)
def test_datadiagrammltextformat_delelt_del__setter(instance):
    original = instance.del_
    instance.del_ = original
    assert instance.del_ == original

@given(instance=DatadiagramMLTextFormat_IXElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_ixelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_IXElt)



@given(instance=DatadiagramMLTextFormat_IXElt_strategy)
def test_datadiagrammltextformat_ixelt_iX_setter(instance):
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

@given(instance=DatadiagramMLTextFormat_XYElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_xyelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_XYElt)

@given(instance=DatadiagramMLTextFormat_NamedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_namedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_NamedElt)



@given(instance=DatadiagramMLTextFormat_NamedElt_strategy)
def test_datadiagrammltextformat_namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=DatadiagramMLTextFormat_NamedElt_strategy)
def test_datadiagrammltextformat_namedelt_nameU_setter(instance):
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

@given(instance=DatadiagramMLTextFormat_SolutionXML_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_solutionxml_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_SolutionXML)

@given(instance=DatadiagramMLTextFormat_HeaderFooter_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_headerfooter_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_HeaderFooter)

@given(instance=DatadiagramMLTextFormat_EventList_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_eventlist_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_EventList)

@given(instance=DatadiagramMLTextFormat_WindowsInfo_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_windowsinfo_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_WindowsInfo)

@given(instance=DatadiagramMLTextFormat_DocumentSettingsElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_documentsettingselt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_DocumentSettingsElt)

@given(instance=DatadiagramMLTextFormat_PageElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_pageelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_PageElt)

@given(instance=DatadiagramMLTextFormat_PrintSetup_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_printsetup_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_PrintSetup)

@given(instance=DatadiagramMLTextFormat_PagesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_pagescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_PagesCollection)

@given(instance=DatadiagramMLTextFormat_MasterElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_masterelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_MasterElt)

@given(instance=ConnectsCollection_strategy)
@settings(max_examples=50)
def test_connectscollection_instantiation(instance):
    assert isinstance(instance, ConnectsCollection)

@given(instance=DatadiagramMLTextFormat_Connect_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_connect_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Connect)



@given(instance=DatadiagramMLTextFormat_Connect_strategy)
def test_datadiagrammltextformat_connect_fromCell_setter(instance):
    original = instance.fromCell
    instance.fromCell = original
    assert instance.fromCell == original



@given(instance=DatadiagramMLTextFormat_Connect_strategy)
def test_datadiagrammltextformat_connect_toCell_setter(instance):
    original = instance.toCell
    instance.toCell = original
    assert instance.toCell == original



@given(instance=DatadiagramMLTextFormat_Connect_strategy)
def test_datadiagrammltextformat_connect_fromSheet_setter(instance):
    original = instance.fromSheet
    instance.fromSheet = original
    assert instance.fromSheet == original



@given(instance=DatadiagramMLTextFormat_Connect_strategy)
def test_datadiagrammltextformat_connect_toPart_setter(instance):
    original = instance.toPart
    instance.toPart = original
    assert instance.toPart == original



@given(instance=DatadiagramMLTextFormat_Connect_strategy)
def test_datadiagrammltextformat_connect_toSheet_setter(instance):
    original = instance.toSheet
    instance.toSheet = original
    assert instance.toSheet == original



@given(instance=DatadiagramMLTextFormat_Connect_strategy)
def test_datadiagrammltextformat_connect_fromPart_setter(instance):
    original = instance.fromPart
    instance.fromPart = original
    assert instance.fromPart == original

@given(instance=Connect_strategy)
@settings(max_examples=50)
def test_connect_instantiation(instance):
    assert isinstance(instance, Connect)

@given(instance=DatadiagramMLTextFormat_ConnectsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_connectscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_ConnectsCollection)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=DatadiagramMLTextFormat_ShapesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_shapescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_ShapesCollection)

@given(instance=DatadiagramMLTextFormat_Icon_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_icon_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Icon)



@given(instance=DatadiagramMLTextFormat_Icon_strategy)
def test_datadiagrammltextformat_icon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

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

@given(instance=DatadiagramMLTextFormat_MastersCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_masterscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_MastersCollection)

@given(instance=TabsCollection_strategy)
@settings(max_examples=50)
def test_tabscollection_instantiation(instance):
    assert isinstance(instance, TabsCollection)

@given(instance=DatadiagramMLTextFormat_Tab_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_tab_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Tab)

@given(instance=Tab_strategy)
@settings(max_examples=50)
def test_tab_instantiation(instance):
    assert isinstance(instance, Tab)

@given(instance=DatadiagramMLTextFormat_IXrequiredElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_ixrequiredelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_IXrequiredElt)



@given(instance=DatadiagramMLTextFormat_IXrequiredElt_strategy)
def test_datadiagrammltextformat_ixrequiredelt_iX_setter(instance):
    original = instance.iX
    instance.iX = original
    assert instance.iX == original

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=DatadiagramMLTextFormat_TextElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_textelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_TextElt)

@given(instance=XYABCDElt_strategy)
@settings(max_examples=50)
def test_xyabcdelt_instantiation(instance):
    assert isinstance(instance, XYABCDElt)

@given(instance=DatadiagramMLTextFormat_SplineStart_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_splinestart_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_SplineStart)

@given(instance=DatadiagramMLTextFormat_EllipticalArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_ellipticalarcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_EllipticalArcTo)

@given(instance=DatadiagramMLTextFormat_Ellipse_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_ellipse_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Ellipse)

@given(instance=TextElt_strategy)
@settings(max_examples=50)
def test_textelt_instantiation(instance):
    assert isinstance(instance, TextElt)

@given(instance=DatadiagramMLTextFormat_StringElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_stringelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_StringElt)



@given(instance=DatadiagramMLTextFormat_StringElt_strategy)
def test_datadiagrammltextformat_stringelt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=XYABCDEElt_strategy)
@settings(max_examples=50)
def test_xyabcdeelt_instantiation(instance):
    assert isinstance(instance, XYABCDEElt)

@given(instance=DatadiagramMLTextFormat_NURBSTo_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_nurbsto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_NURBSTo)

@given(instance=DatadiagramMLTextFormat_XYABCDEElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_xyabcdeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_XYABCDEElt)

@given(instance=UniqueIdElt_strategy)
@settings(max_examples=50)
def test_uniqueidelt_instantiation(instance):
    assert isinstance(instance, UniqueIdElt)

@given(instance=DatadiagramMLTextFormat_ShapeElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_shapeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_ShapeElt)

@given(instance=ShapeElt_strategy)
@settings(max_examples=50)
def test_shapeelt_instantiation(instance):
    assert isinstance(instance, ShapeElt)

@given(instance=DatadiagramMLTextFormat_Geom_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_geom_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Geom)

@given(instance=DatadiagramMLTextFormat_Field_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_field_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Field)

@given(instance=DatadiagramMLTextFormat_Text_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_text_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Text)

@given(instance=DatadiagramMLTextFormat_TabsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_tabscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_TabsCollection)

@given(instance=DatadiagramMLTextFormat_Char_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_char_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Char)

@given(instance=DatadiagramMLTextFormat_Para_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_para_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Para)

@given(instance=ShapesCollection_strategy)
@settings(max_examples=50)
def test_shapescollection_instantiation(instance):
    assert isinstance(instance, ShapesCollection)

@given(instance=DatadiagramMLTextFormat_Shape_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_shape_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Shape)



@given(instance=DatadiagramMLTextFormat_Shape_strategy)
def test_datadiagrammltextformat_shape_fillStyle_setter(instance):
    original = instance.fillStyle
    instance.fillStyle = original
    assert instance.fillStyle == original



@given(instance=DatadiagramMLTextFormat_Shape_strategy)
def test_datadiagrammltextformat_shape_textStyle_setter(instance):
    original = instance.textStyle
    instance.textStyle = original
    assert instance.textStyle == original



@given(instance=DatadiagramMLTextFormat_Shape_strategy)
def test_datadiagrammltextformat_shape_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=DatadiagramMLTextFormat_UniqueIdElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_uniqueidelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_UniqueIdElt)



@given(instance=DatadiagramMLTextFormat_UniqueIdElt_strategy)
def test_datadiagrammltextformat_uniqueidelt_UniqueID_setter(instance):
    original = instance.UniqueID
    instance.UniqueID = original
    assert instance.UniqueID == original

@given(instance=DatadiagramMLTextFormat_IdentifiedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_identifiedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_IdentifiedElt)



@given(instance=DatadiagramMLTextFormat_IdentifiedElt_strategy)
def test_datadiagrammltextformat_identifiedelt_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=DatadiagramMLTextFormat_VBProjectData_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_vbprojectdata_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_VBProjectData)



@given(instance=DatadiagramMLTextFormat_VBProjectData_strategy)
def test_datadiagrammltextformat_vbprojectdata_data_setter(instance):
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

@given(instance=DatadiagramMLTextFormat_DocumentSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_documentsheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_DocumentSheet)

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=DatadiagramMLTextFormat_PageSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_pagesheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_PageSheet)

@given(instance=StyleSheet_strategy)
@settings(max_examples=50)
def test_stylesheet_instantiation(instance):
    assert isinstance(instance, StyleSheet)

@given(instance=DatadiagramMLTextFormat_StyleSheetsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_stylesheetscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_StyleSheetsCollection)

@given(instance=DatadiagramMLTextFormat_EmailRoutingData_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_emailroutingdata_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_EmailRoutingData)



@given(instance=DatadiagramMLTextFormat_EmailRoutingData_strategy)
def test_datadiagrammltextformat_emailroutingdata_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=DatadiagramMLTextFormat_EmailRoutingData_strategy)
def test_datadiagrammltextformat_emailroutingdata_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=FontEntry_strategy)
@settings(max_examples=50)
def test_fontentry_instantiation(instance):
    assert isinstance(instance, FontEntry)

@given(instance=DatadiagramMLTextFormat_FontsTable_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_fontstable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_FontsTable)

@given(instance=FaceName_strategy)
@settings(max_examples=50)
def test_facename_instantiation(instance):
    assert isinstance(instance, FaceName)

@given(instance=DatadiagramMLTextFormat_FaceNamesTable_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_facenamestable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_FaceNamesTable)

@given(instance=IdentifiedElt_strategy)
@settings(max_examples=50)
def test_identifiedelt_instantiation(instance):
    assert isinstance(instance, IdentifiedElt)

@given(instance=DatadiagramMLTextFormat_StyleSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_stylesheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_StyleSheet)

@given(instance=DatadiagramMLTextFormat_Page_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_page_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Page)



@given(instance=DatadiagramMLTextFormat_Page_strategy)
def test_datadiagrammltextformat_page_viewCenterX_setter(instance):
    original = instance.viewCenterX
    instance.viewCenterX = original
    assert instance.viewCenterX == original



@given(instance=DatadiagramMLTextFormat_Page_strategy)
def test_datadiagrammltextformat_page_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=DatadiagramMLTextFormat_Page_strategy)
def test_datadiagrammltextformat_page_ViewCenterY_setter(instance):
    original = instance.ViewCenterY
    instance.ViewCenterY = original
    assert instance.ViewCenterY == original



@given(instance=DatadiagramMLTextFormat_Page_strategy)
def test_datadiagrammltextformat_page_backPage_setter(instance):
    original = instance.backPage
    instance.backPage = original
    assert instance.backPage == original



@given(instance=DatadiagramMLTextFormat_Page_strategy)
def test_datadiagrammltextformat_page_associatedPage_setter(instance):
    original = instance.associatedPage
    instance.associatedPage = original
    assert instance.associatedPage == original



@given(instance=DatadiagramMLTextFormat_Page_strategy)
def test_datadiagrammltextformat_page_reviewerID_setter(instance):
    original = instance.reviewerID
    instance.reviewerID = original
    assert instance.reviewerID == original



@given(instance=DatadiagramMLTextFormat_Page_strategy)
def test_datadiagrammltextformat_page_viewScale_setter(instance):
    original = instance.viewScale
    instance.viewScale = original
    assert instance.viewScale == original

@given(instance=DatadiagramMLTextFormat_MasterShortCut_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_mastershortcut_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_MasterShortCut)



@given(instance=DatadiagramMLTextFormat_MasterShortCut_strategy)
def test_datadiagrammltextformat_mastershortcut_shortcutURL_setter(instance):
    original = instance.shortcutURL
    instance.shortcutURL = original
    assert instance.shortcutURL == original



@given(instance=DatadiagramMLTextFormat_MasterShortCut_strategy)
def test_datadiagrammltextformat_mastershortcut_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original



@given(instance=DatadiagramMLTextFormat_MasterShortCut_strategy)
def test_datadiagrammltextformat_mastershortcut_shortcutHelp_setter(instance):
    original = instance.shortcutHelp
    instance.shortcutHelp = original
    assert instance.shortcutHelp == original



@given(instance=DatadiagramMLTextFormat_MasterShortCut_strategy)
def test_datadiagrammltextformat_mastershortcut_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original



@given(instance=DatadiagramMLTextFormat_MasterShortCut_strategy)
def test_datadiagrammltextformat_mastershortcut_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original



@given(instance=DatadiagramMLTextFormat_MasterShortCut_strategy)
def test_datadiagrammltextformat_mastershortcut_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original

@given(instance=DatadiagramMLTextFormat_FaceName_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_facename_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_FaceName)



@given(instance=DatadiagramMLTextFormat_FaceName_strategy)
def test_datadiagrammltextformat_facename_charSet_setter(instance):
    original = instance.charSet
    instance.charSet = original
    assert instance.charSet == original



@given(instance=DatadiagramMLTextFormat_FaceName_strategy)
def test_datadiagrammltextformat_facename_unicodeRanges_setter(instance):
    original = instance.unicodeRanges
    instance.unicodeRanges = original
    assert instance.unicodeRanges == original



@given(instance=DatadiagramMLTextFormat_FaceName_strategy)
def test_datadiagrammltextformat_facename_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original



@given(instance=DatadiagramMLTextFormat_FaceName_strategy)
def test_datadiagrammltextformat_facename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=DatadiagramMLTextFormat_FaceName_strategy)
def test_datadiagrammltextformat_facename_panos_setter(instance):
    original = instance.panos
    instance.panos = original
    assert instance.panos == original

@given(instance=DatadiagramMLTextFormat_Master_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_master_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Master)



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_datadiagrammltextformat_master_baseID_setter(instance):
    original = instance.baseID
    instance.baseID = original
    assert instance.baseID == original



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_datadiagrammltextformat_master_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_datadiagrammltextformat_master_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_datadiagrammltextformat_master_matchByName_setter(instance):
    original = instance.matchByName
    instance.matchByName = original
    assert instance.matchByName == original



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_datadiagrammltextformat_master_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_datadiagrammltextformat_master_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_datadiagrammltextformat_master_iconUpdate_setter(instance):
    original = instance.iconUpdate
    instance.iconUpdate = original
    assert instance.iconUpdate == original



@given(instance=DatadiagramMLTextFormat_Master_strategy)
def test_datadiagrammltextformat_master_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original

@given(instance=CustomProperty_strategy)
@settings(max_examples=50)
def test_customproperty_instantiation(instance):
    assert isinstance(instance, CustomProperty)

@given(instance=DatadiagramMLTextFormat_FontEntry_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_fontentry_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_FontEntry)



@given(instance=DatadiagramMLTextFormat_FontEntry_strategy)
def test_datadiagrammltextformat_fontentry_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=DatadiagramMLTextFormat_FontEntry_strategy)
def test_datadiagrammltextformat_fontentry_charSet_setter(instance):
    original = instance.charSet
    instance.charSet = original
    assert instance.charSet == original



@given(instance=DatadiagramMLTextFormat_FontEntry_strategy)
def test_datadiagrammltextformat_fontentry_pitchAndFamily_setter(instance):
    original = instance.pitchAndFamily
    instance.pitchAndFamily = original
    assert instance.pitchAndFamily == original



@given(instance=DatadiagramMLTextFormat_FontEntry_strategy)
def test_datadiagrammltextformat_fontentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=DatadiagramMLTextFormat_FontEntry_strategy)
def test_datadiagrammltextformat_fontentry_unicode_setter(instance):
    original = instance.unicode
    instance.unicode = original
    assert instance.unicode == original



@given(instance=DatadiagramMLTextFormat_FontEntry_strategy)
def test_datadiagrammltextformat_fontentry_attributes_setter(instance):
    original = instance.attributes
    instance.attributes = original
    assert instance.attributes == original

@given(instance=DatadiagramMLTextFormat_CustomPropertiesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_custompropertiescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_CustomPropertiesCollection)

@given(instance=IXrequiredElt_strategy)
@settings(max_examples=50)
def test_ixrequiredelt_instantiation(instance):
    assert isinstance(instance, IXrequiredElt)

@given(instance=DatadiagramMLTextFormat_Fld_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_fld_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Fld)

@given(instance=DatadiagramMLTextFormat_Tp_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_tp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Tp)

@given(instance=DatadiagramMLTextFormat_Pp_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_pp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Pp)

@given(instance=DatadiagramMLTextFormat_Cp_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_cp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_Cp)

@given(instance=DatadiagramMLTextFormat_ColorEntry_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_colorentry_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_ColorEntry)



@given(instance=DatadiagramMLTextFormat_ColorEntry_strategy)
def test_datadiagrammltextformat_colorentry_rgb_setter(instance):
    original = instance.rgb
    instance.rgb = original
    assert instance.rgb == original

@given(instance=ColorEntry_strategy)
@settings(max_examples=50)
def test_colorentry_instantiation(instance):
    assert isinstance(instance, ColorEntry)

@given(instance=DatadiagramMLTextFormat_ColorsTable_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_colorstable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_ColorsTable)

@given(instance=DatadiagramMLTextFormat_CustomProperty_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_customproperty_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_CustomProperty)



@given(instance=DatadiagramMLTextFormat_CustomProperty_strategy)
def test_datadiagrammltextformat_customproperty_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original



@given(instance=DatadiagramMLTextFormat_CustomProperty_strategy)
def test_datadiagrammltextformat_customproperty_name_setter(instance):
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

@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_DocumentPropertiesCollection)



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat_documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat_documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat_documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat_documentpropertiescollection_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat_documentpropertiescollection_buildNumberCreated_setter(instance):
    original = instance.buildNumberCreated
    instance.buildNumberCreated = original
    assert instance.buildNumberCreated == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat_documentpropertiescollection_hyperlinkBase_href_setter(instance):
    original = instance.hyperlinkBase_href
    instance.hyperlinkBase_href = original
    assert instance.hyperlinkBase_href == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat_documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat_documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat_documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat_documentpropertiescollection_creator_setter(instance):
    original = instance.creator
    instance.creator = original
    assert instance.creator == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat_documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat_documentpropertiescollection_alternateNames_setter(instance):
    original = instance.alternateNames
    instance.alternateNames = original
    assert instance.alternateNames == original



@given(instance=DatadiagramMLTextFormat_DocumentPropertiesCollection_strategy)
def test_datadiagrammltextformat_documentpropertiescollection_buildNumberEdited_setter(instance):
    original = instance.buildNumberEdited
    instance.buildNumberEdited = original
    assert instance.buildNumberEdited == original

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

@given(instance=MastersCollection_strategy)
@settings(max_examples=50)
def test_masterscollection_instantiation(instance):
    assert isinstance(instance, MastersCollection)

@given(instance=DocumentSheet_strategy)
@settings(max_examples=50)
def test_documentsheet_instantiation(instance):
    assert isinstance(instance, DocumentSheet)

@given(instance=DatadiagramMLTextFormat_DateTimeType_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_datetimetype_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_DateTimeType)



@given(instance=DatadiagramMLTextFormat_DateTimeType_strategy)
def test_datadiagrammltextformat_datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=DatadiagramMLTextFormat_DateTimeType_strategy)
def test_datadiagrammltextformat_datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original



@given(instance=DatadiagramMLTextFormat_DateTimeType_strategy)
def test_datadiagrammltextformat_datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=DatadiagramMLTextFormat_DateTimeType_strategy)
def test_datadiagrammltextformat_datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original



@given(instance=DatadiagramMLTextFormat_DateTimeType_strategy)
def test_datadiagrammltextformat_datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=DatadiagramMLTextFormat_DateTimeType_strategy)
def test_datadiagrammltextformat_datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original

@given(instance=DocumentSettingsElt_strategy)
@settings(max_examples=50)
def test_documentsettingselt_instantiation(instance):
    assert isinstance(instance, DocumentSettingsElt)

@given(instance=DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DocumentPropertiesCollection)

@given(instance=DatadiagramMLTextFormat_VisioDocument_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_visiodocument_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_VisioDocument)



@given(instance=DatadiagramMLTextFormat_VisioDocument_strategy)
def test_datadiagrammltextformat_visiodocument_docLangId_setter(instance):
    original = instance.docLangId
    instance.docLangId = original
    assert instance.docLangId == original



@given(instance=DatadiagramMLTextFormat_VisioDocument_strategy)
def test_datadiagrammltextformat_visiodocument_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=DatadiagramMLTextFormat_VisioDocument_strategy)
def test_datadiagrammltextformat_visiodocument_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=DatadiagramMLTextFormat_VisioDocument_strategy)
def test_datadiagrammltextformat_visiodocument_metric_setter(instance):
    original = instance.metric
    instance.metric = original
    assert instance.metric == original



@given(instance=DatadiagramMLTextFormat_VisioDocument_strategy)
def test_datadiagrammltextformat_visiodocument_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=DatadiagramMLTextFormat_VisioDocument_strategy)
def test_datadiagrammltextformat_visiodocument_buildnum_setter(instance):
    original = instance.buildnum
    instance.buildnum = original
    assert instance.buildnum == original

@given(instance=DatadiagramMLTextFormat_CellType_strategy)
@settings(max_examples=50)
def test_datadiagrammltextformat_celltype_instantiation(instance):
    assert isinstance(instance, DatadiagramMLTextFormat_CellType)



@given(instance=DatadiagramMLTextFormat_CellType_strategy)
def test_datadiagrammltextformat_celltype_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=DatadiagramMLTextFormat_CellType_strategy)
def test_datadiagrammltextformat_celltype_err_setter(instance):
    original = instance.err
    instance.err = original
    assert instance.err == original



@given(instance=DatadiagramMLTextFormat_CellType_strategy)
def test_datadiagrammltextformat_celltype_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original



@given(instance=DatadiagramMLTextFormat_CellType_strategy)
def test_datadiagrammltextformat_celltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
