import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DatadiagramMLXForm_IXrequiredElt,
    Text,
    DatadiagramMLXForm_TextElt,
    Geom,
    XYElt,
    DatadiagramMLXForm_LineTo,
    XYABElt,
    DatadiagramMLXForm_XYABCDElt,
    DatadiagramMLXForm_InfiniteLine,
    XYAElt,
    DatadiagramMLXForm_SplineKnot,
    DatadiagramMLXForm_XYABElt,
    DatadiagramMLXForm_PolylineTo,
    DatadiagramMLXForm_ArcTo,
    DatadiagramMLXForm_XYAElt,
    DatadiagramMLXForm_MoveTo,
    CellType,
    NURBSTo,
    SplineStart,
    EllipticalArcTo,
    Ellipse,
    InfiniteLine,
    PolylineTo,
    SplineKnot,
    ArcTo,
    MoveTo,
    LineTo,
    DatadiagramMLXForm_IdentifiedElt,
    DatadiagramMLXForm_NamedElt,
    PageElt,
    MasterElt,
    UniqueIdElt,
    DelElt,
    IXElt,
    DatadiagramMLXForm_XYElt,
    DatadiagramMLXForm_DelElt,
    DatadiagramMLXForm_IXElt,
    DatadiagramMLXForm_ShapeElt,
    ShapeElt,
    DatadiagramMLXForm_Geom,
    ShapesCollection,
    DatadiagramMLXForm_Shape,
    DatadiagramMLXForm_UniqueIdElt,
    PageSheet,
    NamedElt,
    DatadiagramMLXForm_DocumentSheet,
    Shape,
    DatadiagramMLXForm_PageSheet,
    FaceName,
    DatadiagramMLXForm_FaceNamesTable,
    DatadiagramMLXForm_StyleSheetsCollection,
    DatadiagramMLXForm_EmailRoutingData,
    DatadiagramMLXForm_VBProjectData,
    IdentifiedElt,
    DatadiagramMLXForm_FaceName,
    DatadiagramMLXForm_StyleSheet,
    DatadiagramMLXForm_FontEntry,
    FontEntry,
    DatadiagramMLXForm_FontsTable,
    DatadiagramMLXForm_PrintSetup,
    SnapAnglesCollection,
    IXrequiredElt,
    DatadiagramMLXForm_ColorEntry,
    ColorEntry,
    StyleSheet,
    DatadiagramMLXForm_ColorsTable,
    Page,
    DatadiagramMLXForm_SnapAngle,
    SnapAngle,
    DatadiagramMLXForm_SnapAnglesCollection,
    DateTimeType,
    CustomPropertiesCollection,
    DatadiagramMLXForm_DocumentSettingsElt,
    DatadiagramMLXForm_CustomProperty,
    CustomProperty,
    DatadiagramMLXForm_CustomPropertiesCollection,
    VBProjectData,
    HeaderFooter,
    EventList,
    WindowsInfo,
    PagesCollection,
    MastersCollection,
    DocumentSheet,
    StyleSheetsCollection,
    VisioDocument,
    DatadiagramMLXForm_DocumentPropertiesCollection,
    SolutionXML,
    EmailRoutingData,
    DocumentPropertiesCollection,
    DatadiagramMLXForm_VisioDocument,
    FaceNamesTable,
    FontsTable,
    PrintSetup,
    DatadiagramMLXForm_CellType,
    ColorsTable,
    DocumentSettingsElt,
    DatadiagramMLXForm_DateTimeType,
    DatadiagramMLXForm_SolutionXML,
    DatadiagramMLXForm_HeaderFooter,
    DatadiagramMLXForm_EventList,
    DatadiagramMLXForm_WindowsInfo,
    DatadiagramMLXForm_PageElt,
    DatadiagramMLXForm_Page,
    DatadiagramMLXForm_PagesCollection,
    DatadiagramMLXForm_MasterElt,
    Connect,
    DatadiagramMLXForm_ConnectsCollection,
    DatadiagramMLXForm_ShapesCollection,
    ConnectsCollection,
    DatadiagramMLXForm_Connect,
    DatadiagramMLXForm_MasterShortCut,
    MasterShortCut,
    DatadiagramMLXForm_Master,
    Master,
    DatadiagramMLXForm_Icon,
    Icon,
    DatadiagramMLXForm_XForm,
    DatadiagramMLXForm_MastersCollection,
    DatadiagramMLXForm_Field,
    TabsCollection,
    DatadiagramMLXForm_Tab,
    Tab,
    DatadiagramMLXForm_TabsCollection,
    DatadiagramMLXForm_Para,
    DatadiagramMLXForm_Char,
    TextElt,
    DatadiagramMLXForm_Pp,
    DatadiagramMLXForm_Fld,
    DatadiagramMLXForm_Cp,
    DatadiagramMLXForm_StringElt,
    DatadiagramMLXForm_Tp,
    DatadiagramMLXForm_Text,
    XYABCDEElt,
    DatadiagramMLXForm_NURBSTo,
    XYABCDElt,
    DatadiagramMLXForm_XYABCDEElt,
    DatadiagramMLXForm_EllipticalArcTo,
    DatadiagramMLXForm_SplineStart,
    DatadiagramMLXForm_Ellipse,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datadiagrammlxform_ixrequiredelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_IXrequiredElt)


def test_datadiagrammlxform_ixrequiredelt_constructor_exists():
    assert callable(DatadiagramMLXForm_IXrequiredElt.__init__)


def test_datadiagrammlxform_ixrequiredelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_IXrequiredElt.__init__)
    params = list(sig.parameters.keys())
    assert "iX" in params, "Missing parameter 'iX'"

def test_datadiagrammlxform_ixrequiredelt_has_iX():
    assert hasattr(DatadiagramMLXForm_IXrequiredElt, "iX")
    descriptor = None
    for klass in DatadiagramMLXForm_IXrequiredElt.__mro__:
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



def test_datadiagrammlxform_textelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_TextElt)


def test_datadiagrammlxform_textelt_constructor_exists():
    assert callable(DatadiagramMLXForm_TextElt.__init__)


def test_datadiagrammlxform_textelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_TextElt.__init__)
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



def test_datadiagrammlxform_lineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_LineTo)


def test_datadiagrammlxform_lineto_constructor_exists():
    assert callable(DatadiagramMLXForm_LineTo.__init__)


def test_datadiagrammlxform_lineto_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_LineTo.__init__)
    params = list(sig.parameters.keys())



def test_xyabelt_is_not_abstract():
    assert not inspect.isabstract(XYABElt)


def test_xyabelt_constructor_exists():
    assert callable(XYABElt.__init__)


def test_xyabelt_constructor_args():
    sig = inspect.signature(XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_XYABCDElt)


def test_datadiagrammlxform_xyabcdelt_constructor_exists():
    assert callable(DatadiagramMLXForm_XYABCDElt.__init__)


def test_datadiagrammlxform_xyabcdelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_infiniteline_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_InfiniteLine)


def test_datadiagrammlxform_infiniteline_constructor_exists():
    assert callable(DatadiagramMLXForm_InfiniteLine.__init__)


def test_datadiagrammlxform_infiniteline_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_InfiniteLine.__init__)
    params = list(sig.parameters.keys())



def test_xyaelt_is_not_abstract():
    assert not inspect.isabstract(XYAElt)


def test_xyaelt_constructor_exists():
    assert callable(XYAElt.__init__)


def test_xyaelt_constructor_args():
    sig = inspect.signature(XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_splineknot_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_SplineKnot)


def test_datadiagrammlxform_splineknot_constructor_exists():
    assert callable(DatadiagramMLXForm_SplineKnot.__init__)


def test_datadiagrammlxform_splineknot_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_SplineKnot.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_xyabelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_XYABElt)


def test_datadiagrammlxform_xyabelt_constructor_exists():
    assert callable(DatadiagramMLXForm_XYABElt.__init__)


def test_datadiagrammlxform_xyabelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_XYABElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_polylineto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_PolylineTo)


def test_datadiagrammlxform_polylineto_constructor_exists():
    assert callable(DatadiagramMLXForm_PolylineTo.__init__)


def test_datadiagrammlxform_polylineto_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_PolylineTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_arcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_ArcTo)


def test_datadiagrammlxform_arcto_constructor_exists():
    assert callable(DatadiagramMLXForm_ArcTo.__init__)


def test_datadiagrammlxform_arcto_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_ArcTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_xyaelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_XYAElt)


def test_datadiagrammlxform_xyaelt_constructor_exists():
    assert callable(DatadiagramMLXForm_XYAElt.__init__)


def test_datadiagrammlxform_xyaelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_XYAElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_moveto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_MoveTo)


def test_datadiagrammlxform_moveto_constructor_exists():
    assert callable(DatadiagramMLXForm_MoveTo.__init__)


def test_datadiagrammlxform_moveto_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_celltype_is_not_abstract():
    assert not inspect.isabstract(CellType)


def test_celltype_constructor_exists():
    assert callable(CellType.__init__)


def test_celltype_constructor_args():
    sig = inspect.signature(CellType.__init__)
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



def test_datadiagrammlxform_identifiedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_IdentifiedElt)


def test_datadiagrammlxform_identifiedelt_constructor_exists():
    assert callable(DatadiagramMLXForm_IdentifiedElt.__init__)


def test_datadiagrammlxform_identifiedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_IdentifiedElt.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_datadiagrammlxform_identifiedelt_has_ID():
    assert hasattr(DatadiagramMLXForm_IdentifiedElt, "ID")
    descriptor = None
    for klass in DatadiagramMLXForm_IdentifiedElt.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform_namedelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_NamedElt)


def test_datadiagrammlxform_namedelt_constructor_exists():
    assert callable(DatadiagramMLXForm_NamedElt.__init__)


def test_datadiagrammlxform_namedelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "nameU" in params, "Missing parameter 'nameU'"
    assert "name" in params, "Missing parameter 'name'"

def test_datadiagrammlxform_namedelt_has_nameU():
    assert hasattr(DatadiagramMLXForm_NamedElt, "nameU")
    descriptor = None
    for klass in DatadiagramMLXForm_NamedElt.__mro__:
        if "nameU" in klass.__dict__:
            descriptor = klass.__dict__["nameU"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_namedelt_has_name():
    assert hasattr(DatadiagramMLXForm_NamedElt, "name")
    descriptor = None
    for klass in DatadiagramMLXForm_NamedElt.__mro__:
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



def test_uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(UniqueIdElt)


def test_uniqueidelt_constructor_exists():
    assert callable(UniqueIdElt.__init__)


def test_uniqueidelt_constructor_args():
    sig = inspect.signature(UniqueIdElt.__init__)
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



def test_datadiagrammlxform_xyelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_XYElt)


def test_datadiagrammlxform_xyelt_constructor_exists():
    assert callable(DatadiagramMLXForm_XYElt.__init__)


def test_datadiagrammlxform_xyelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_XYElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_delelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_DelElt)


def test_datadiagrammlxform_delelt_constructor_exists():
    assert callable(DatadiagramMLXForm_DelElt.__init__)


def test_datadiagrammlxform_delelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_DelElt.__init__)
    params = list(sig.parameters.keys())
    assert "del_" in params, "Missing parameter 'del_'"

def test_datadiagrammlxform_delelt_has_del_():
    assert hasattr(DatadiagramMLXForm_DelElt, "del_")
    descriptor = None
    for klass in DatadiagramMLXForm_DelElt.__mro__:
        if "del_" in klass.__dict__:
            descriptor = klass.__dict__["del_"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform_ixelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_IXElt)


def test_datadiagrammlxform_ixelt_constructor_exists():
    assert callable(DatadiagramMLXForm_IXElt.__init__)


def test_datadiagrammlxform_ixelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_IXElt.__init__)
    params = list(sig.parameters.keys())
    assert "iX" in params, "Missing parameter 'iX'"

def test_datadiagrammlxform_ixelt_has_iX():
    assert hasattr(DatadiagramMLXForm_IXElt, "iX")
    descriptor = None
    for klass in DatadiagramMLXForm_IXElt.__mro__:
        if "iX" in klass.__dict__:
            descriptor = klass.__dict__["iX"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform_shapeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_ShapeElt)


def test_datadiagrammlxform_shapeelt_constructor_exists():
    assert callable(DatadiagramMLXForm_ShapeElt.__init__)


def test_datadiagrammlxform_shapeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_shapeelt_is_not_abstract():
    assert not inspect.isabstract(ShapeElt)


def test_shapeelt_constructor_exists():
    assert callable(ShapeElt.__init__)


def test_shapeelt_constructor_args():
    sig = inspect.signature(ShapeElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_geom_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Geom)


def test_datadiagrammlxform_geom_constructor_exists():
    assert callable(DatadiagramMLXForm_Geom.__init__)


def test_datadiagrammlxform_geom_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Geom.__init__)
    params = list(sig.parameters.keys())



def test_shapescollection_is_not_abstract():
    assert not inspect.isabstract(ShapesCollection)


def test_shapescollection_constructor_exists():
    assert callable(ShapesCollection.__init__)


def test_shapescollection_constructor_args():
    sig = inspect.signature(ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_shape_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Shape)


def test_datadiagrammlxform_shape_constructor_exists():
    assert callable(DatadiagramMLXForm_Shape.__init__)


def test_datadiagrammlxform_shape_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "textStyle" in params, "Missing parameter 'textStyle'"
    assert "fillStyle" in params, "Missing parameter 'fillStyle'"

def test_datadiagrammlxform_shape_has_lineStyle():
    assert hasattr(DatadiagramMLXForm_Shape, "lineStyle")
    descriptor = None
    for klass in DatadiagramMLXForm_Shape.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_shape_has_textStyle():
    assert hasattr(DatadiagramMLXForm_Shape, "textStyle")
    descriptor = None
    for klass in DatadiagramMLXForm_Shape.__mro__:
        if "textStyle" in klass.__dict__:
            descriptor = klass.__dict__["textStyle"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_shape_has_fillStyle():
    assert hasattr(DatadiagramMLXForm_Shape, "fillStyle")
    descriptor = None
    for klass in DatadiagramMLXForm_Shape.__mro__:
        if "fillStyle" in klass.__dict__:
            descriptor = klass.__dict__["fillStyle"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform_uniqueidelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_UniqueIdElt)


def test_datadiagrammlxform_uniqueidelt_constructor_exists():
    assert callable(DatadiagramMLXForm_UniqueIdElt.__init__)


def test_datadiagrammlxform_uniqueidelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_UniqueIdElt.__init__)
    params = list(sig.parameters.keys())
    assert "UniqueID" in params, "Missing parameter 'UniqueID'"

def test_datadiagrammlxform_uniqueidelt_has_UniqueID():
    assert hasattr(DatadiagramMLXForm_UniqueIdElt, "UniqueID")
    descriptor = None
    for klass in DatadiagramMLXForm_UniqueIdElt.__mro__:
        if "UniqueID" in klass.__dict__:
            descriptor = klass.__dict__["UniqueID"]
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



def test_datadiagrammlxform_documentsheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_DocumentSheet)


def test_datadiagrammlxform_documentsheet_constructor_exists():
    assert callable(DatadiagramMLXForm_DocumentSheet.__init__)


def test_datadiagrammlxform_documentsheet_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_DocumentSheet.__init__)
    params = list(sig.parameters.keys())



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_pagesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_PageSheet)


def test_datadiagrammlxform_pagesheet_constructor_exists():
    assert callable(DatadiagramMLXForm_PageSheet.__init__)


def test_datadiagrammlxform_pagesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_PageSheet.__init__)
    params = list(sig.parameters.keys())



def test_facename_is_not_abstract():
    assert not inspect.isabstract(FaceName)


def test_facename_constructor_exists():
    assert callable(FaceName.__init__)


def test_facename_constructor_args():
    sig = inspect.signature(FaceName.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_facenamestable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_FaceNamesTable)


def test_datadiagrammlxform_facenamestable_constructor_exists():
    assert callable(DatadiagramMLXForm_FaceNamesTable.__init__)


def test_datadiagrammlxform_facenamestable_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_FaceNamesTable.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_stylesheetscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_StyleSheetsCollection)


def test_datadiagrammlxform_stylesheetscollection_constructor_exists():
    assert callable(DatadiagramMLXForm_StyleSheetsCollection.__init__)


def test_datadiagrammlxform_stylesheetscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_StyleSheetsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_emailroutingdata_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_EmailRoutingData)


def test_datadiagrammlxform_emailroutingdata_constructor_exists():
    assert callable(DatadiagramMLXForm_EmailRoutingData.__init__)


def test_datadiagrammlxform_emailroutingdata_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_EmailRoutingData.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "size" in params, "Missing parameter 'size'"

def test_datadiagrammlxform_emailroutingdata_has_data():
    assert hasattr(DatadiagramMLXForm_EmailRoutingData, "data")
    descriptor = None
    for klass in DatadiagramMLXForm_EmailRoutingData.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_emailroutingdata_has_size():
    assert hasattr(DatadiagramMLXForm_EmailRoutingData, "size")
    descriptor = None
    for klass in DatadiagramMLXForm_EmailRoutingData.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform_vbprojectdata_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_VBProjectData)


def test_datadiagrammlxform_vbprojectdata_constructor_exists():
    assert callable(DatadiagramMLXForm_VBProjectData.__init__)


def test_datadiagrammlxform_vbprojectdata_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_VBProjectData.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_datadiagrammlxform_vbprojectdata_has_data():
    assert hasattr(DatadiagramMLXForm_VBProjectData, "data")
    descriptor = None
    for klass in DatadiagramMLXForm_VBProjectData.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_identifiedelt_is_not_abstract():
    assert not inspect.isabstract(IdentifiedElt)


def test_identifiedelt_constructor_exists():
    assert callable(IdentifiedElt.__init__)


def test_identifiedelt_constructor_args():
    sig = inspect.signature(IdentifiedElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_facename_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_FaceName)


def test_datadiagrammlxform_facename_constructor_exists():
    assert callable(DatadiagramMLXForm_FaceName.__init__)


def test_datadiagrammlxform_facename_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_FaceName.__init__)
    params = list(sig.parameters.keys())
    assert "panos" in params, "Missing parameter 'panos'"
    assert "unicodeRanges" in params, "Missing parameter 'unicodeRanges'"
    assert "flags" in params, "Missing parameter 'flags'"
    assert "charSet" in params, "Missing parameter 'charSet'"
    assert "name" in params, "Missing parameter 'name'"

def test_datadiagrammlxform_facename_has_panos():
    assert hasattr(DatadiagramMLXForm_FaceName, "panos")
    descriptor = None
    for klass in DatadiagramMLXForm_FaceName.__mro__:
        if "panos" in klass.__dict__:
            descriptor = klass.__dict__["panos"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_facename_has_unicodeRanges():
    assert hasattr(DatadiagramMLXForm_FaceName, "unicodeRanges")
    descriptor = None
    for klass in DatadiagramMLXForm_FaceName.__mro__:
        if "unicodeRanges" in klass.__dict__:
            descriptor = klass.__dict__["unicodeRanges"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_facename_has_flags():
    assert hasattr(DatadiagramMLXForm_FaceName, "flags")
    descriptor = None
    for klass in DatadiagramMLXForm_FaceName.__mro__:
        if "flags" in klass.__dict__:
            descriptor = klass.__dict__["flags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_facename_has_charSet():
    assert hasattr(DatadiagramMLXForm_FaceName, "charSet")
    descriptor = None
    for klass in DatadiagramMLXForm_FaceName.__mro__:
        if "charSet" in klass.__dict__:
            descriptor = klass.__dict__["charSet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_facename_has_name():
    assert hasattr(DatadiagramMLXForm_FaceName, "name")
    descriptor = None
    for klass in DatadiagramMLXForm_FaceName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform_stylesheet_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_StyleSheet)


def test_datadiagrammlxform_stylesheet_constructor_exists():
    assert callable(DatadiagramMLXForm_StyleSheet.__init__)


def test_datadiagrammlxform_stylesheet_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_fontentry_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_FontEntry)


def test_datadiagrammlxform_fontentry_constructor_exists():
    assert callable(DatadiagramMLXForm_FontEntry.__init__)


def test_datadiagrammlxform_fontentry_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_FontEntry.__init__)
    params = list(sig.parameters.keys())
    assert "charSet" in params, "Missing parameter 'charSet'"
    assert "name" in params, "Missing parameter 'name'"
    assert "unicode" in params, "Missing parameter 'unicode'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "attributes" in params, "Missing parameter 'attributes'"
    assert "pitchAndFamily" in params, "Missing parameter 'pitchAndFamily'"

def test_datadiagrammlxform_fontentry_has_charSet():
    assert hasattr(DatadiagramMLXForm_FontEntry, "charSet")
    descriptor = None
    for klass in DatadiagramMLXForm_FontEntry.__mro__:
        if "charSet" in klass.__dict__:
            descriptor = klass.__dict__["charSet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_fontentry_has_name():
    assert hasattr(DatadiagramMLXForm_FontEntry, "name")
    descriptor = None
    for klass in DatadiagramMLXForm_FontEntry.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_fontentry_has_unicode():
    assert hasattr(DatadiagramMLXForm_FontEntry, "unicode")
    descriptor = None
    for klass in DatadiagramMLXForm_FontEntry.__mro__:
        if "unicode" in klass.__dict__:
            descriptor = klass.__dict__["unicode"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_fontentry_has_weight():
    assert hasattr(DatadiagramMLXForm_FontEntry, "weight")
    descriptor = None
    for klass in DatadiagramMLXForm_FontEntry.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_fontentry_has_attributes():
    assert hasattr(DatadiagramMLXForm_FontEntry, "attributes")
    descriptor = None
    for klass in DatadiagramMLXForm_FontEntry.__mro__:
        if "attributes" in klass.__dict__:
            descriptor = klass.__dict__["attributes"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_fontentry_has_pitchAndFamily():
    assert hasattr(DatadiagramMLXForm_FontEntry, "pitchAndFamily")
    descriptor = None
    for klass in DatadiagramMLXForm_FontEntry.__mro__:
        if "pitchAndFamily" in klass.__dict__:
            descriptor = klass.__dict__["pitchAndFamily"]
            break
    assert isinstance(descriptor, property)



def test_fontentry_is_not_abstract():
    assert not inspect.isabstract(FontEntry)


def test_fontentry_constructor_exists():
    assert callable(FontEntry.__init__)


def test_fontentry_constructor_args():
    sig = inspect.signature(FontEntry.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_fontstable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_FontsTable)


def test_datadiagrammlxform_fontstable_constructor_exists():
    assert callable(DatadiagramMLXForm_FontsTable.__init__)


def test_datadiagrammlxform_fontstable_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_FontsTable.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_printsetup_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_PrintSetup)


def test_datadiagrammlxform_printsetup_constructor_exists():
    assert callable(DatadiagramMLXForm_PrintSetup.__init__)


def test_datadiagrammlxform_printsetup_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_PrintSetup.__init__)
    params = list(sig.parameters.keys())



def test_snapanglescollection_is_not_abstract():
    assert not inspect.isabstract(SnapAnglesCollection)


def test_snapanglescollection_constructor_exists():
    assert callable(SnapAnglesCollection.__init__)


def test_snapanglescollection_constructor_args():
    sig = inspect.signature(SnapAnglesCollection.__init__)
    params = list(sig.parameters.keys())



def test_ixrequiredelt_is_not_abstract():
    assert not inspect.isabstract(IXrequiredElt)


def test_ixrequiredelt_constructor_exists():
    assert callable(IXrequiredElt.__init__)


def test_ixrequiredelt_constructor_args():
    sig = inspect.signature(IXrequiredElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_colorentry_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_ColorEntry)


def test_datadiagrammlxform_colorentry_constructor_exists():
    assert callable(DatadiagramMLXForm_ColorEntry.__init__)


def test_datadiagrammlxform_colorentry_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_ColorEntry.__init__)
    params = list(sig.parameters.keys())
    assert "rgb" in params, "Missing parameter 'rgb'"

def test_datadiagrammlxform_colorentry_has_rgb():
    assert hasattr(DatadiagramMLXForm_ColorEntry, "rgb")
    descriptor = None
    for klass in DatadiagramMLXForm_ColorEntry.__mro__:
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



def test_stylesheet_is_not_abstract():
    assert not inspect.isabstract(StyleSheet)


def test_stylesheet_constructor_exists():
    assert callable(StyleSheet.__init__)


def test_stylesheet_constructor_args():
    sig = inspect.signature(StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_colorstable_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_ColorsTable)


def test_datadiagrammlxform_colorstable_constructor_exists():
    assert callable(DatadiagramMLXForm_ColorsTable.__init__)


def test_datadiagrammlxform_colorstable_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_ColorsTable.__init__)
    params = list(sig.parameters.keys())



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_snapangle_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_SnapAngle)


def test_datadiagrammlxform_snapangle_constructor_exists():
    assert callable(DatadiagramMLXForm_SnapAngle.__init__)


def test_datadiagrammlxform_snapangle_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_SnapAngle.__init__)
    params = list(sig.parameters.keys())
    assert "angleValue" in params, "Missing parameter 'angleValue'"

def test_datadiagrammlxform_snapangle_has_angleValue():
    assert hasattr(DatadiagramMLXForm_SnapAngle, "angleValue")
    descriptor = None
    for klass in DatadiagramMLXForm_SnapAngle.__mro__:
        if "angleValue" in klass.__dict__:
            descriptor = klass.__dict__["angleValue"]
            break
    assert isinstance(descriptor, property)



def test_snapangle_is_not_abstract():
    assert not inspect.isabstract(SnapAngle)


def test_snapangle_constructor_exists():
    assert callable(SnapAngle.__init__)


def test_snapangle_constructor_args():
    sig = inspect.signature(SnapAngle.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_snapanglescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_SnapAnglesCollection)


def test_datadiagrammlxform_snapanglescollection_constructor_exists():
    assert callable(DatadiagramMLXForm_SnapAnglesCollection.__init__)


def test_datadiagrammlxform_snapanglescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_SnapAnglesCollection.__init__)
    params = list(sig.parameters.keys())



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



def test_datadiagrammlxform_documentsettingselt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_DocumentSettingsElt)


def test_datadiagrammlxform_documentsettingselt_constructor_exists():
    assert callable(DatadiagramMLXForm_DocumentSettingsElt.__init__)


def test_datadiagrammlxform_documentsettingselt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_DocumentSettingsElt.__init__)
    params = list(sig.parameters.keys())
    assert "snapExtensions" in params, "Missing parameter 'snapExtensions'"
    assert "customToolbarsFile" in params, "Missing parameter 'customToolbarsFile'"
    assert "protectMasters" in params, "Missing parameter 'protectMasters'"
    assert "glueSettings" in params, "Missing parameter 'glueSettings'"
    assert "protectShapes" in params, "Missing parameter 'protectShapes'"
    assert "protectBkgnds" in params, "Missing parameter 'protectBkgnds'"
    assert "attachedToolbars" in params, "Missing parameter 'attachedToolbars'"
    assert "dynamicGridEnabled" in params, "Missing parameter 'dynamicGridEnabled'"
    assert "customMenusFile" in params, "Missing parameter 'customMenusFile'"
    assert "snapSettings" in params, "Missing parameter 'snapSettings'"
    assert "protectStyles" in params, "Missing parameter 'protectStyles'"

def test_datadiagrammlxform_documentsettingselt_has_snapExtensions():
    assert hasattr(DatadiagramMLXForm_DocumentSettingsElt, "snapExtensions")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentSettingsElt.__mro__:
        if "snapExtensions" in klass.__dict__:
            descriptor = klass.__dict__["snapExtensions"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentsettingselt_has_customToolbarsFile():
    assert hasattr(DatadiagramMLXForm_DocumentSettingsElt, "customToolbarsFile")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentSettingsElt.__mro__:
        if "customToolbarsFile" in klass.__dict__:
            descriptor = klass.__dict__["customToolbarsFile"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentsettingselt_has_protectMasters():
    assert hasattr(DatadiagramMLXForm_DocumentSettingsElt, "protectMasters")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentSettingsElt.__mro__:
        if "protectMasters" in klass.__dict__:
            descriptor = klass.__dict__["protectMasters"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentsettingselt_has_glueSettings():
    assert hasattr(DatadiagramMLXForm_DocumentSettingsElt, "glueSettings")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentSettingsElt.__mro__:
        if "glueSettings" in klass.__dict__:
            descriptor = klass.__dict__["glueSettings"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentsettingselt_has_protectShapes():
    assert hasattr(DatadiagramMLXForm_DocumentSettingsElt, "protectShapes")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentSettingsElt.__mro__:
        if "protectShapes" in klass.__dict__:
            descriptor = klass.__dict__["protectShapes"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentsettingselt_has_protectBkgnds():
    assert hasattr(DatadiagramMLXForm_DocumentSettingsElt, "protectBkgnds")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentSettingsElt.__mro__:
        if "protectBkgnds" in klass.__dict__:
            descriptor = klass.__dict__["protectBkgnds"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentsettingselt_has_attachedToolbars():
    assert hasattr(DatadiagramMLXForm_DocumentSettingsElt, "attachedToolbars")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentSettingsElt.__mro__:
        if "attachedToolbars" in klass.__dict__:
            descriptor = klass.__dict__["attachedToolbars"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentsettingselt_has_dynamicGridEnabled():
    assert hasattr(DatadiagramMLXForm_DocumentSettingsElt, "dynamicGridEnabled")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentSettingsElt.__mro__:
        if "dynamicGridEnabled" in klass.__dict__:
            descriptor = klass.__dict__["dynamicGridEnabled"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentsettingselt_has_customMenusFile():
    assert hasattr(DatadiagramMLXForm_DocumentSettingsElt, "customMenusFile")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentSettingsElt.__mro__:
        if "customMenusFile" in klass.__dict__:
            descriptor = klass.__dict__["customMenusFile"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentsettingselt_has_snapSettings():
    assert hasattr(DatadiagramMLXForm_DocumentSettingsElt, "snapSettings")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentSettingsElt.__mro__:
        if "snapSettings" in klass.__dict__:
            descriptor = klass.__dict__["snapSettings"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentsettingselt_has_protectStyles():
    assert hasattr(DatadiagramMLXForm_DocumentSettingsElt, "protectStyles")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentSettingsElt.__mro__:
        if "protectStyles" in klass.__dict__:
            descriptor = klass.__dict__["protectStyles"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform_customproperty_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_CustomProperty)


def test_datadiagrammlxform_customproperty_constructor_exists():
    assert callable(DatadiagramMLXForm_CustomProperty.__init__)


def test_datadiagrammlxform_customproperty_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_CustomProperty.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "name" in params, "Missing parameter 'name'"

def test_datadiagrammlxform_customproperty_has_dataType():
    assert hasattr(DatadiagramMLXForm_CustomProperty, "dataType")
    descriptor = None
    for klass in DatadiagramMLXForm_CustomProperty.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_customproperty_has_name():
    assert hasattr(DatadiagramMLXForm_CustomProperty, "name")
    descriptor = None
    for klass in DatadiagramMLXForm_CustomProperty.__mro__:
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



def test_datadiagrammlxform_custompropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_CustomPropertiesCollection)


def test_datadiagrammlxform_custompropertiescollection_constructor_exists():
    assert callable(DatadiagramMLXForm_CustomPropertiesCollection.__init__)


def test_datadiagrammlxform_custompropertiescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_CustomPropertiesCollection.__init__)
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



def test_stylesheetscollection_is_not_abstract():
    assert not inspect.isabstract(StyleSheetsCollection)


def test_stylesheetscollection_constructor_exists():
    assert callable(StyleSheetsCollection.__init__)


def test_stylesheetscollection_constructor_args():
    sig = inspect.signature(StyleSheetsCollection.__init__)
    params = list(sig.parameters.keys())



def test_visiodocument_is_not_abstract():
    assert not inspect.isabstract(VisioDocument)


def test_visiodocument_constructor_exists():
    assert callable(VisioDocument.__init__)


def test_visiodocument_constructor_args():
    sig = inspect.signature(VisioDocument.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_DocumentPropertiesCollection)


def test_datadiagrammlxform_documentpropertiescollection_constructor_exists():
    assert callable(DatadiagramMLXForm_DocumentPropertiesCollection.__init__)


def test_datadiagrammlxform_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"
    assert "company" in params, "Missing parameter 'company'"
    assert "category" in params, "Missing parameter 'category'"
    assert "title" in params, "Missing parameter 'title'"
    assert "creator" in params, "Missing parameter 'creator'"
    assert "description" in params, "Missing parameter 'description'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "hyperlinkBase_href" in params, "Missing parameter 'hyperlinkBase_href'"
    assert "buildNumberCreated" in params, "Missing parameter 'buildNumberCreated'"
    assert "buildNumberEdited" in params, "Missing parameter 'buildNumberEdited'"
    assert "alternateNames" in params, "Missing parameter 'alternateNames'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "template" in params, "Missing parameter 'template'"

def test_datadiagrammlxform_documentpropertiescollection_has_subject():
    assert hasattr(DatadiagramMLXForm_DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentpropertiescollection_has_company():
    assert hasattr(DatadiagramMLXForm_DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentpropertiescollection_has_category():
    assert hasattr(DatadiagramMLXForm_DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentpropertiescollection_has_title():
    assert hasattr(DatadiagramMLXForm_DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentpropertiescollection_has_creator():
    assert hasattr(DatadiagramMLXForm_DocumentPropertiesCollection, "creator")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentPropertiesCollection.__mro__:
        if "creator" in klass.__dict__:
            descriptor = klass.__dict__["creator"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentpropertiescollection_has_description():
    assert hasattr(DatadiagramMLXForm_DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentpropertiescollection_has_manager():
    assert hasattr(DatadiagramMLXForm_DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentpropertiescollection_has_hyperlinkBase_href():
    assert hasattr(DatadiagramMLXForm_DocumentPropertiesCollection, "hyperlinkBase_href")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase_href" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase_href"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentpropertiescollection_has_buildNumberCreated():
    assert hasattr(DatadiagramMLXForm_DocumentPropertiesCollection, "buildNumberCreated")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentPropertiesCollection.__mro__:
        if "buildNumberCreated" in klass.__dict__:
            descriptor = klass.__dict__["buildNumberCreated"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentpropertiescollection_has_buildNumberEdited():
    assert hasattr(DatadiagramMLXForm_DocumentPropertiesCollection, "buildNumberEdited")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentPropertiesCollection.__mro__:
        if "buildNumberEdited" in klass.__dict__:
            descriptor = klass.__dict__["buildNumberEdited"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentpropertiescollection_has_alternateNames():
    assert hasattr(DatadiagramMLXForm_DocumentPropertiesCollection, "alternateNames")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentPropertiesCollection.__mro__:
        if "alternateNames" in klass.__dict__:
            descriptor = klass.__dict__["alternateNames"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentpropertiescollection_has_keywords():
    assert hasattr(DatadiagramMLXForm_DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_documentpropertiescollection_has_template():
    assert hasattr(DatadiagramMLXForm_DocumentPropertiesCollection, "template")
    descriptor = None
    for klass in DatadiagramMLXForm_DocumentPropertiesCollection.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
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



def test_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DocumentPropertiesCollection)


def test_documentpropertiescollection_constructor_exists():
    assert callable(DocumentPropertiesCollection.__init__)


def test_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_visiodocument_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_VisioDocument)


def test_datadiagrammlxform_visiodocument_constructor_exists():
    assert callable(DatadiagramMLXForm_VisioDocument.__init__)


def test_datadiagrammlxform_visiodocument_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_VisioDocument.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "buildnum" in params, "Missing parameter 'buildnum'"
    assert "version" in params, "Missing parameter 'version'"
    assert "docLangId" in params, "Missing parameter 'docLangId'"
    assert "key" in params, "Missing parameter 'key'"
    assert "metric" in params, "Missing parameter 'metric'"

def test_datadiagrammlxform_visiodocument_has_start():
    assert hasattr(DatadiagramMLXForm_VisioDocument, "start")
    descriptor = None
    for klass in DatadiagramMLXForm_VisioDocument.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_visiodocument_has_buildnum():
    assert hasattr(DatadiagramMLXForm_VisioDocument, "buildnum")
    descriptor = None
    for klass in DatadiagramMLXForm_VisioDocument.__mro__:
        if "buildnum" in klass.__dict__:
            descriptor = klass.__dict__["buildnum"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_visiodocument_has_version():
    assert hasattr(DatadiagramMLXForm_VisioDocument, "version")
    descriptor = None
    for klass in DatadiagramMLXForm_VisioDocument.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_visiodocument_has_docLangId():
    assert hasattr(DatadiagramMLXForm_VisioDocument, "docLangId")
    descriptor = None
    for klass in DatadiagramMLXForm_VisioDocument.__mro__:
        if "docLangId" in klass.__dict__:
            descriptor = klass.__dict__["docLangId"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_visiodocument_has_key():
    assert hasattr(DatadiagramMLXForm_VisioDocument, "key")
    descriptor = None
    for klass in DatadiagramMLXForm_VisioDocument.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_visiodocument_has_metric():
    assert hasattr(DatadiagramMLXForm_VisioDocument, "metric")
    descriptor = None
    for klass in DatadiagramMLXForm_VisioDocument.__mro__:
        if "metric" in klass.__dict__:
            descriptor = klass.__dict__["metric"]
            break
    assert isinstance(descriptor, property)



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



def test_datadiagrammlxform_celltype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_CellType)


def test_datadiagrammlxform_celltype_constructor_exists():
    assert callable(DatadiagramMLXForm_CellType.__init__)


def test_datadiagrammlxform_celltype_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_CellType.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "formula" in params, "Missing parameter 'formula'"
    assert "value" in params, "Missing parameter 'value'"
    assert "err" in params, "Missing parameter 'err'"

def test_datadiagrammlxform_celltype_has_unit():
    assert hasattr(DatadiagramMLXForm_CellType, "unit")
    descriptor = None
    for klass in DatadiagramMLXForm_CellType.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_celltype_has_formula():
    assert hasattr(DatadiagramMLXForm_CellType, "formula")
    descriptor = None
    for klass in DatadiagramMLXForm_CellType.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_celltype_has_value():
    assert hasattr(DatadiagramMLXForm_CellType, "value")
    descriptor = None
    for klass in DatadiagramMLXForm_CellType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_celltype_has_err():
    assert hasattr(DatadiagramMLXForm_CellType, "err")
    descriptor = None
    for klass in DatadiagramMLXForm_CellType.__mro__:
        if "err" in klass.__dict__:
            descriptor = klass.__dict__["err"]
            break
    assert isinstance(descriptor, property)



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



def test_datadiagrammlxform_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_DateTimeType)


def test_datadiagrammlxform_datetimetype_constructor_exists():
    assert callable(DatadiagramMLXForm_DateTimeType.__init__)


def test_datadiagrammlxform_datetimetype_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "hour" in params, "Missing parameter 'hour'"
    assert "second" in params, "Missing parameter 'second'"
    assert "year" in params, "Missing parameter 'year'"
    assert "day" in params, "Missing parameter 'day'"
    assert "month" in params, "Missing parameter 'month'"
    assert "minute" in params, "Missing parameter 'minute'"

def test_datadiagrammlxform_datetimetype_has_hour():
    assert hasattr(DatadiagramMLXForm_DateTimeType, "hour")
    descriptor = None
    for klass in DatadiagramMLXForm_DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_datetimetype_has_second():
    assert hasattr(DatadiagramMLXForm_DateTimeType, "second")
    descriptor = None
    for klass in DatadiagramMLXForm_DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_datetimetype_has_year():
    assert hasattr(DatadiagramMLXForm_DateTimeType, "year")
    descriptor = None
    for klass in DatadiagramMLXForm_DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_datetimetype_has_day():
    assert hasattr(DatadiagramMLXForm_DateTimeType, "day")
    descriptor = None
    for klass in DatadiagramMLXForm_DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_datetimetype_has_month():
    assert hasattr(DatadiagramMLXForm_DateTimeType, "month")
    descriptor = None
    for klass in DatadiagramMLXForm_DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_datetimetype_has_minute():
    assert hasattr(DatadiagramMLXForm_DateTimeType, "minute")
    descriptor = None
    for klass in DatadiagramMLXForm_DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform_solutionxml_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_SolutionXML)


def test_datadiagrammlxform_solutionxml_constructor_exists():
    assert callable(DatadiagramMLXForm_SolutionXML.__init__)


def test_datadiagrammlxform_solutionxml_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_SolutionXML.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_headerfooter_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_HeaderFooter)


def test_datadiagrammlxform_headerfooter_constructor_exists():
    assert callable(DatadiagramMLXForm_HeaderFooter.__init__)


def test_datadiagrammlxform_headerfooter_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_HeaderFooter.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_eventlist_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_EventList)


def test_datadiagrammlxform_eventlist_constructor_exists():
    assert callable(DatadiagramMLXForm_EventList.__init__)


def test_datadiagrammlxform_eventlist_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_EventList.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_windowsinfo_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_WindowsInfo)


def test_datadiagrammlxform_windowsinfo_constructor_exists():
    assert callable(DatadiagramMLXForm_WindowsInfo.__init__)


def test_datadiagrammlxform_windowsinfo_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_WindowsInfo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_pageelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_PageElt)


def test_datadiagrammlxform_pageelt_constructor_exists():
    assert callable(DatadiagramMLXForm_PageElt.__init__)


def test_datadiagrammlxform_pageelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_PageElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_page_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Page)


def test_datadiagrammlxform_page_constructor_exists():
    assert callable(DatadiagramMLXForm_Page.__init__)


def test_datadiagrammlxform_page_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Page.__init__)
    params = list(sig.parameters.keys())
    assert "viewCenterX" in params, "Missing parameter 'viewCenterX'"
    assert "background" in params, "Missing parameter 'background'"
    assert "viewScale" in params, "Missing parameter 'viewScale'"
    assert "associatedPage" in params, "Missing parameter 'associatedPage'"
    assert "backPage" in params, "Missing parameter 'backPage'"
    assert "ViewCenterY" in params, "Missing parameter 'ViewCenterY'"
    assert "reviewerID" in params, "Missing parameter 'reviewerID'"

def test_datadiagrammlxform_page_has_viewCenterX():
    assert hasattr(DatadiagramMLXForm_Page, "viewCenterX")
    descriptor = None
    for klass in DatadiagramMLXForm_Page.__mro__:
        if "viewCenterX" in klass.__dict__:
            descriptor = klass.__dict__["viewCenterX"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_page_has_background():
    assert hasattr(DatadiagramMLXForm_Page, "background")
    descriptor = None
    for klass in DatadiagramMLXForm_Page.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_page_has_viewScale():
    assert hasattr(DatadiagramMLXForm_Page, "viewScale")
    descriptor = None
    for klass in DatadiagramMLXForm_Page.__mro__:
        if "viewScale" in klass.__dict__:
            descriptor = klass.__dict__["viewScale"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_page_has_associatedPage():
    assert hasattr(DatadiagramMLXForm_Page, "associatedPage")
    descriptor = None
    for klass in DatadiagramMLXForm_Page.__mro__:
        if "associatedPage" in klass.__dict__:
            descriptor = klass.__dict__["associatedPage"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_page_has_backPage():
    assert hasattr(DatadiagramMLXForm_Page, "backPage")
    descriptor = None
    for klass in DatadiagramMLXForm_Page.__mro__:
        if "backPage" in klass.__dict__:
            descriptor = klass.__dict__["backPage"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_page_has_ViewCenterY():
    assert hasattr(DatadiagramMLXForm_Page, "ViewCenterY")
    descriptor = None
    for klass in DatadiagramMLXForm_Page.__mro__:
        if "ViewCenterY" in klass.__dict__:
            descriptor = klass.__dict__["ViewCenterY"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_page_has_reviewerID():
    assert hasattr(DatadiagramMLXForm_Page, "reviewerID")
    descriptor = None
    for klass in DatadiagramMLXForm_Page.__mro__:
        if "reviewerID" in klass.__dict__:
            descriptor = klass.__dict__["reviewerID"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform_pagescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_PagesCollection)


def test_datadiagrammlxform_pagescollection_constructor_exists():
    assert callable(DatadiagramMLXForm_PagesCollection.__init__)


def test_datadiagrammlxform_pagescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_PagesCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_masterelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_MasterElt)


def test_datadiagrammlxform_masterelt_constructor_exists():
    assert callable(DatadiagramMLXForm_MasterElt.__init__)


def test_datadiagrammlxform_masterelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_MasterElt.__init__)
    params = list(sig.parameters.keys())



def test_connect_is_not_abstract():
    assert not inspect.isabstract(Connect)


def test_connect_constructor_exists():
    assert callable(Connect.__init__)


def test_connect_constructor_args():
    sig = inspect.signature(Connect.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_connectscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_ConnectsCollection)


def test_datadiagrammlxform_connectscollection_constructor_exists():
    assert callable(DatadiagramMLXForm_ConnectsCollection.__init__)


def test_datadiagrammlxform_connectscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_shapescollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_ShapesCollection)


def test_datadiagrammlxform_shapescollection_constructor_exists():
    assert callable(DatadiagramMLXForm_ShapesCollection.__init__)


def test_datadiagrammlxform_shapescollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_ShapesCollection.__init__)
    params = list(sig.parameters.keys())



def test_connectscollection_is_not_abstract():
    assert not inspect.isabstract(ConnectsCollection)


def test_connectscollection_constructor_exists():
    assert callable(ConnectsCollection.__init__)


def test_connectscollection_constructor_args():
    sig = inspect.signature(ConnectsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_connect_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Connect)


def test_datadiagrammlxform_connect_constructor_exists():
    assert callable(DatadiagramMLXForm_Connect.__init__)


def test_datadiagrammlxform_connect_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Connect.__init__)
    params = list(sig.parameters.keys())
    assert "fromPart" in params, "Missing parameter 'fromPart'"
    assert "toPart" in params, "Missing parameter 'toPart'"
    assert "toCell" in params, "Missing parameter 'toCell'"
    assert "toSheet" in params, "Missing parameter 'toSheet'"
    assert "fromSheet" in params, "Missing parameter 'fromSheet'"
    assert "fromCell" in params, "Missing parameter 'fromCell'"

def test_datadiagrammlxform_connect_has_fromPart():
    assert hasattr(DatadiagramMLXForm_Connect, "fromPart")
    descriptor = None
    for klass in DatadiagramMLXForm_Connect.__mro__:
        if "fromPart" in klass.__dict__:
            descriptor = klass.__dict__["fromPart"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_connect_has_toPart():
    assert hasattr(DatadiagramMLXForm_Connect, "toPart")
    descriptor = None
    for klass in DatadiagramMLXForm_Connect.__mro__:
        if "toPart" in klass.__dict__:
            descriptor = klass.__dict__["toPart"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_connect_has_toCell():
    assert hasattr(DatadiagramMLXForm_Connect, "toCell")
    descriptor = None
    for klass in DatadiagramMLXForm_Connect.__mro__:
        if "toCell" in klass.__dict__:
            descriptor = klass.__dict__["toCell"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_connect_has_toSheet():
    assert hasattr(DatadiagramMLXForm_Connect, "toSheet")
    descriptor = None
    for klass in DatadiagramMLXForm_Connect.__mro__:
        if "toSheet" in klass.__dict__:
            descriptor = klass.__dict__["toSheet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_connect_has_fromSheet():
    assert hasattr(DatadiagramMLXForm_Connect, "fromSheet")
    descriptor = None
    for klass in DatadiagramMLXForm_Connect.__mro__:
        if "fromSheet" in klass.__dict__:
            descriptor = klass.__dict__["fromSheet"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_connect_has_fromCell():
    assert hasattr(DatadiagramMLXForm_Connect, "fromCell")
    descriptor = None
    for klass in DatadiagramMLXForm_Connect.__mro__:
        if "fromCell" in klass.__dict__:
            descriptor = klass.__dict__["fromCell"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform_mastershortcut_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_MasterShortCut)


def test_datadiagrammlxform_mastershortcut_constructor_exists():
    assert callable(DatadiagramMLXForm_MasterShortCut.__init__)


def test_datadiagrammlxform_mastershortcut_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_MasterShortCut.__init__)
    params = list(sig.parameters.keys())
    assert "iconSize" in params, "Missing parameter 'iconSize'"
    assert "shortcutHelp" in params, "Missing parameter 'shortcutHelp'"
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "shortcutURL" in params, "Missing parameter 'shortcutURL'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"

def test_datadiagrammlxform_mastershortcut_has_iconSize():
    assert hasattr(DatadiagramMLXForm_MasterShortCut, "iconSize")
    descriptor = None
    for klass in DatadiagramMLXForm_MasterShortCut.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_mastershortcut_has_shortcutHelp():
    assert hasattr(DatadiagramMLXForm_MasterShortCut, "shortcutHelp")
    descriptor = None
    for klass in DatadiagramMLXForm_MasterShortCut.__mro__:
        if "shortcutHelp" in klass.__dict__:
            descriptor = klass.__dict__["shortcutHelp"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_mastershortcut_has_prompt():
    assert hasattr(DatadiagramMLXForm_MasterShortCut, "prompt")
    descriptor = None
    for klass in DatadiagramMLXForm_MasterShortCut.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_mastershortcut_has_shortcutURL():
    assert hasattr(DatadiagramMLXForm_MasterShortCut, "shortcutURL")
    descriptor = None
    for klass in DatadiagramMLXForm_MasterShortCut.__mro__:
        if "shortcutURL" in klass.__dict__:
            descriptor = klass.__dict__["shortcutURL"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_mastershortcut_has_alignName():
    assert hasattr(DatadiagramMLXForm_MasterShortCut, "alignName")
    descriptor = None
    for klass in DatadiagramMLXForm_MasterShortCut.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_mastershortcut_has_patternFlags():
    assert hasattr(DatadiagramMLXForm_MasterShortCut, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLXForm_MasterShortCut.__mro__:
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



def test_datadiagrammlxform_master_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Master)


def test_datadiagrammlxform_master_constructor_exists():
    assert callable(DatadiagramMLXForm_Master.__init__)


def test_datadiagrammlxform_master_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Master.__init__)
    params = list(sig.parameters.keys())
    assert "matchByName" in params, "Missing parameter 'matchByName'"
    assert "iconSize" in params, "Missing parameter 'iconSize'"
    assert "alignName" in params, "Missing parameter 'alignName'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "iconUpdate" in params, "Missing parameter 'iconUpdate'"
    assert "patternFlags" in params, "Missing parameter 'patternFlags'"
    assert "prompt" in params, "Missing parameter 'prompt'"
    assert "baseID" in params, "Missing parameter 'baseID'"

def test_datadiagrammlxform_master_has_matchByName():
    assert hasattr(DatadiagramMLXForm_Master, "matchByName")
    descriptor = None
    for klass in DatadiagramMLXForm_Master.__mro__:
        if "matchByName" in klass.__dict__:
            descriptor = klass.__dict__["matchByName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_master_has_iconSize():
    assert hasattr(DatadiagramMLXForm_Master, "iconSize")
    descriptor = None
    for klass in DatadiagramMLXForm_Master.__mro__:
        if "iconSize" in klass.__dict__:
            descriptor = klass.__dict__["iconSize"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_master_has_alignName():
    assert hasattr(DatadiagramMLXForm_Master, "alignName")
    descriptor = None
    for klass in DatadiagramMLXForm_Master.__mro__:
        if "alignName" in klass.__dict__:
            descriptor = klass.__dict__["alignName"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_master_has_hidden():
    assert hasattr(DatadiagramMLXForm_Master, "hidden")
    descriptor = None
    for klass in DatadiagramMLXForm_Master.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_master_has_iconUpdate():
    assert hasattr(DatadiagramMLXForm_Master, "iconUpdate")
    descriptor = None
    for klass in DatadiagramMLXForm_Master.__mro__:
        if "iconUpdate" in klass.__dict__:
            descriptor = klass.__dict__["iconUpdate"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_master_has_patternFlags():
    assert hasattr(DatadiagramMLXForm_Master, "patternFlags")
    descriptor = None
    for klass in DatadiagramMLXForm_Master.__mro__:
        if "patternFlags" in klass.__dict__:
            descriptor = klass.__dict__["patternFlags"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_master_has_prompt():
    assert hasattr(DatadiagramMLXForm_Master, "prompt")
    descriptor = None
    for klass in DatadiagramMLXForm_Master.__mro__:
        if "prompt" in klass.__dict__:
            descriptor = klass.__dict__["prompt"]
            break
    assert isinstance(descriptor, property)

def test_datadiagrammlxform_master_has_baseID():
    assert hasattr(DatadiagramMLXForm_Master, "baseID")
    descriptor = None
    for klass in DatadiagramMLXForm_Master.__mro__:
        if "baseID" in klass.__dict__:
            descriptor = klass.__dict__["baseID"]
            break
    assert isinstance(descriptor, property)



def test_master_is_not_abstract():
    assert not inspect.isabstract(Master)


def test_master_constructor_exists():
    assert callable(Master.__init__)


def test_master_constructor_args():
    sig = inspect.signature(Master.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_icon_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Icon)


def test_datadiagrammlxform_icon_constructor_exists():
    assert callable(DatadiagramMLXForm_Icon.__init__)


def test_datadiagrammlxform_icon_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Icon.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammlxform_icon_has_value():
    assert hasattr(DatadiagramMLXForm_Icon, "value")
    descriptor = None
    for klass in DatadiagramMLXForm_Icon.__mro__:
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



def test_datadiagrammlxform_xform_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_XForm)


def test_datadiagrammlxform_xform_constructor_exists():
    assert callable(DatadiagramMLXForm_XForm.__init__)


def test_datadiagrammlxform_xform_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_XForm.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_masterscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_MastersCollection)


def test_datadiagrammlxform_masterscollection_constructor_exists():
    assert callable(DatadiagramMLXForm_MastersCollection.__init__)


def test_datadiagrammlxform_masterscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_MastersCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_field_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Field)


def test_datadiagrammlxform_field_constructor_exists():
    assert callable(DatadiagramMLXForm_Field.__init__)


def test_datadiagrammlxform_field_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Field.__init__)
    params = list(sig.parameters.keys())



def test_tabscollection_is_not_abstract():
    assert not inspect.isabstract(TabsCollection)


def test_tabscollection_constructor_exists():
    assert callable(TabsCollection.__init__)


def test_tabscollection_constructor_args():
    sig = inspect.signature(TabsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_tab_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Tab)


def test_datadiagrammlxform_tab_constructor_exists():
    assert callable(DatadiagramMLXForm_Tab.__init__)


def test_datadiagrammlxform_tab_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Tab.__init__)
    params = list(sig.parameters.keys())



def test_tab_is_not_abstract():
    assert not inspect.isabstract(Tab)


def test_tab_constructor_exists():
    assert callable(Tab.__init__)


def test_tab_constructor_args():
    sig = inspect.signature(Tab.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_tabscollection_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_TabsCollection)


def test_datadiagrammlxform_tabscollection_constructor_exists():
    assert callable(DatadiagramMLXForm_TabsCollection.__init__)


def test_datadiagrammlxform_tabscollection_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_TabsCollection.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_para_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Para)


def test_datadiagrammlxform_para_constructor_exists():
    assert callable(DatadiagramMLXForm_Para.__init__)


def test_datadiagrammlxform_para_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Para.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_char_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Char)


def test_datadiagrammlxform_char_constructor_exists():
    assert callable(DatadiagramMLXForm_Char.__init__)


def test_datadiagrammlxform_char_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Char.__init__)
    params = list(sig.parameters.keys())



def test_textelt_is_not_abstract():
    assert not inspect.isabstract(TextElt)


def test_textelt_constructor_exists():
    assert callable(TextElt.__init__)


def test_textelt_constructor_args():
    sig = inspect.signature(TextElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_pp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Pp)


def test_datadiagrammlxform_pp_constructor_exists():
    assert callable(DatadiagramMLXForm_Pp.__init__)


def test_datadiagrammlxform_pp_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Pp.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_fld_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Fld)


def test_datadiagrammlxform_fld_constructor_exists():
    assert callable(DatadiagramMLXForm_Fld.__init__)


def test_datadiagrammlxform_fld_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Fld.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_cp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Cp)


def test_datadiagrammlxform_cp_constructor_exists():
    assert callable(DatadiagramMLXForm_Cp.__init__)


def test_datadiagrammlxform_cp_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Cp.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_stringelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_StringElt)


def test_datadiagrammlxform_stringelt_constructor_exists():
    assert callable(DatadiagramMLXForm_StringElt.__init__)


def test_datadiagrammlxform_stringelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_StringElt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_datadiagrammlxform_stringelt_has_value():
    assert hasattr(DatadiagramMLXForm_StringElt, "value")
    descriptor = None
    for klass in DatadiagramMLXForm_StringElt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_datadiagrammlxform_tp_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Tp)


def test_datadiagrammlxform_tp_constructor_exists():
    assert callable(DatadiagramMLXForm_Tp.__init__)


def test_datadiagrammlxform_tp_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Tp.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_text_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Text)


def test_datadiagrammlxform_text_constructor_exists():
    assert callable(DatadiagramMLXForm_Text.__init__)


def test_datadiagrammlxform_text_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Text.__init__)
    params = list(sig.parameters.keys())



def test_xyabcdeelt_is_not_abstract():
    assert not inspect.isabstract(XYABCDEElt)


def test_xyabcdeelt_constructor_exists():
    assert callable(XYABCDEElt.__init__)


def test_xyabcdeelt_constructor_args():
    sig = inspect.signature(XYABCDEElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_nurbsto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_NURBSTo)


def test_datadiagrammlxform_nurbsto_constructor_exists():
    assert callable(DatadiagramMLXForm_NURBSTo.__init__)


def test_datadiagrammlxform_nurbsto_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_NURBSTo.__init__)
    params = list(sig.parameters.keys())



def test_xyabcdelt_is_not_abstract():
    assert not inspect.isabstract(XYABCDElt)


def test_xyabcdelt_constructor_exists():
    assert callable(XYABCDElt.__init__)


def test_xyabcdelt_constructor_args():
    sig = inspect.signature(XYABCDElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_xyabcdeelt_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_XYABCDEElt)


def test_datadiagrammlxform_xyabcdeelt_constructor_exists():
    assert callable(DatadiagramMLXForm_XYABCDEElt.__init__)


def test_datadiagrammlxform_xyabcdeelt_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_XYABCDEElt.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_ellipticalarcto_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_EllipticalArcTo)


def test_datadiagrammlxform_ellipticalarcto_constructor_exists():
    assert callable(DatadiagramMLXForm_EllipticalArcTo.__init__)


def test_datadiagrammlxform_ellipticalarcto_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_EllipticalArcTo.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_splinestart_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_SplineStart)


def test_datadiagrammlxform_splinestart_constructor_exists():
    assert callable(DatadiagramMLXForm_SplineStart.__init__)


def test_datadiagrammlxform_splinestart_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_SplineStart.__init__)
    params = list(sig.parameters.keys())



def test_datadiagrammlxform_ellipse_is_not_abstract():
    assert not inspect.isabstract(DatadiagramMLXForm_Ellipse)


def test_datadiagrammlxform_ellipse_constructor_exists():
    assert callable(DatadiagramMLXForm_Ellipse.__init__)


def test_datadiagrammlxform_ellipse_constructor_args():
    sig = inspect.signature(DatadiagramMLXForm_Ellipse.__init__)
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
DatadiagramMLXForm_IXrequiredElt_strategy = st.builds(
    DatadiagramMLXForm_IXrequiredElt,
    iX=
        safe_text
)
Text_strategy = st.builds(
    Text,
)
DatadiagramMLXForm_TextElt_strategy = st.builds(
    DatadiagramMLXForm_TextElt,
)
Geom_strategy = st.builds(
    Geom,
)
XYElt_strategy = st.builds(
    XYElt,
)
DatadiagramMLXForm_LineTo_strategy = st.builds(
    DatadiagramMLXForm_LineTo,
)
XYABElt_strategy = st.builds(
    XYABElt,
)
DatadiagramMLXForm_XYABCDElt_strategy = st.builds(
    DatadiagramMLXForm_XYABCDElt,
)
DatadiagramMLXForm_InfiniteLine_strategy = st.builds(
    DatadiagramMLXForm_InfiniteLine,
)
XYAElt_strategy = st.builds(
    XYAElt,
)
DatadiagramMLXForm_SplineKnot_strategy = st.builds(
    DatadiagramMLXForm_SplineKnot,
)
DatadiagramMLXForm_XYABElt_strategy = st.builds(
    DatadiagramMLXForm_XYABElt,
)
DatadiagramMLXForm_PolylineTo_strategy = st.builds(
    DatadiagramMLXForm_PolylineTo,
)
DatadiagramMLXForm_ArcTo_strategy = st.builds(
    DatadiagramMLXForm_ArcTo,
)
DatadiagramMLXForm_XYAElt_strategy = st.builds(
    DatadiagramMLXForm_XYAElt,
)
DatadiagramMLXForm_MoveTo_strategy = st.builds(
    DatadiagramMLXForm_MoveTo,
)
CellType_strategy = st.builds(
    CellType,
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
DatadiagramMLXForm_IdentifiedElt_strategy = st.builds(
    DatadiagramMLXForm_IdentifiedElt,
    ID=
        safe_text
)
DatadiagramMLXForm_NamedElt_strategy = st.builds(
    DatadiagramMLXForm_NamedElt,
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
UniqueIdElt_strategy = st.builds(
    UniqueIdElt,
)
DelElt_strategy = st.builds(
    DelElt,
)
IXElt_strategy = st.builds(
    IXElt,
)
DatadiagramMLXForm_XYElt_strategy = st.builds(
    DatadiagramMLXForm_XYElt,
)
DatadiagramMLXForm_DelElt_strategy = st.builds(
    DatadiagramMLXForm_DelElt,
    del_=
        safe_text
)
DatadiagramMLXForm_IXElt_strategy = st.builds(
    DatadiagramMLXForm_IXElt,
    iX=
        safe_text
)
DatadiagramMLXForm_ShapeElt_strategy = st.builds(
    DatadiagramMLXForm_ShapeElt,
)
ShapeElt_strategy = st.builds(
    ShapeElt,
)
DatadiagramMLXForm_Geom_strategy = st.builds(
    DatadiagramMLXForm_Geom,
)
ShapesCollection_strategy = st.builds(
    ShapesCollection,
)
DatadiagramMLXForm_Shape_strategy = st.builds(
    DatadiagramMLXForm_Shape,
    lineStyle=
        safe_text,
    textStyle=
        safe_text,
    fillStyle=
        safe_text
)
DatadiagramMLXForm_UniqueIdElt_strategy = st.builds(
    DatadiagramMLXForm_UniqueIdElt,
    UniqueID=
        safe_text
)
PageSheet_strategy = st.builds(
    PageSheet,
)
NamedElt_strategy = st.builds(
    NamedElt,
)
DatadiagramMLXForm_DocumentSheet_strategy = st.builds(
    DatadiagramMLXForm_DocumentSheet,
)
Shape_strategy = st.builds(
    Shape,
)
DatadiagramMLXForm_PageSheet_strategy = st.builds(
    DatadiagramMLXForm_PageSheet,
)
FaceName_strategy = st.builds(
    FaceName,
)
DatadiagramMLXForm_FaceNamesTable_strategy = st.builds(
    DatadiagramMLXForm_FaceNamesTable,
)
DatadiagramMLXForm_StyleSheetsCollection_strategy = st.builds(
    DatadiagramMLXForm_StyleSheetsCollection,
)
DatadiagramMLXForm_EmailRoutingData_strategy = st.builds(
    DatadiagramMLXForm_EmailRoutingData,
    data=
        safe_text,
    size=
        safe_text
)
DatadiagramMLXForm_VBProjectData_strategy = st.builds(
    DatadiagramMLXForm_VBProjectData,
    data=
        safe_text
)
IdentifiedElt_strategy = st.builds(
    IdentifiedElt,
)
DatadiagramMLXForm_FaceName_strategy = st.builds(
    DatadiagramMLXForm_FaceName,
    panos=
        safe_text,
    unicodeRanges=
        safe_text,
    flags=
        safe_text,
    charSet=
        safe_text,
    name=
        safe_text
)
DatadiagramMLXForm_StyleSheet_strategy = st.builds(
    DatadiagramMLXForm_StyleSheet,
)
DatadiagramMLXForm_FontEntry_strategy = st.builds(
    DatadiagramMLXForm_FontEntry,
    charSet=
        safe_text,
    name=
        safe_text,
    unicode=
        safe_text,
    weight=
        safe_text,
    attributes=
        safe_text,
    pitchAndFamily=
        safe_text
)
FontEntry_strategy = st.builds(
    FontEntry,
)
DatadiagramMLXForm_FontsTable_strategy = st.builds(
    DatadiagramMLXForm_FontsTable,
)
DatadiagramMLXForm_PrintSetup_strategy = st.builds(
    DatadiagramMLXForm_PrintSetup,
)
SnapAnglesCollection_strategy = st.builds(
    SnapAnglesCollection,
)
IXrequiredElt_strategy = st.builds(
    IXrequiredElt,
)
DatadiagramMLXForm_ColorEntry_strategy = st.builds(
    DatadiagramMLXForm_ColorEntry,
    rgb=
        safe_text
)
ColorEntry_strategy = st.builds(
    ColorEntry,
)
StyleSheet_strategy = st.builds(
    StyleSheet,
)
DatadiagramMLXForm_ColorsTable_strategy = st.builds(
    DatadiagramMLXForm_ColorsTable,
)
Page_strategy = st.builds(
    Page,
)
DatadiagramMLXForm_SnapAngle_strategy = st.builds(
    DatadiagramMLXForm_SnapAngle,
    angleValue=
        safe_text
)
SnapAngle_strategy = st.builds(
    SnapAngle,
)
DatadiagramMLXForm_SnapAnglesCollection_strategy = st.builds(
    DatadiagramMLXForm_SnapAnglesCollection,
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
CustomPropertiesCollection_strategy = st.builds(
    CustomPropertiesCollection,
)
DatadiagramMLXForm_DocumentSettingsElt_strategy = st.builds(
    DatadiagramMLXForm_DocumentSettingsElt,
    snapExtensions=
        safe_text,
    customToolbarsFile=
        safe_text,
    protectMasters=
        safe_text,
    glueSettings=
        safe_text,
    protectShapes=
        safe_text,
    protectBkgnds=
        safe_text,
    attachedToolbars=
        safe_text,
    dynamicGridEnabled=
        safe_text,
    customMenusFile=
        safe_text,
    snapSettings=
        safe_text,
    protectStyles=
        safe_text
)
DatadiagramMLXForm_CustomProperty_strategy = st.builds(
    DatadiagramMLXForm_CustomProperty,
    dataType=
        safe_text,
    name=
        safe_text
)
CustomProperty_strategy = st.builds(
    CustomProperty,
)
DatadiagramMLXForm_CustomPropertiesCollection_strategy = st.builds(
    DatadiagramMLXForm_CustomPropertiesCollection,
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
StyleSheetsCollection_strategy = st.builds(
    StyleSheetsCollection,
)
VisioDocument_strategy = st.builds(
    VisioDocument,
)
DatadiagramMLXForm_DocumentPropertiesCollection_strategy = st.builds(
    DatadiagramMLXForm_DocumentPropertiesCollection,
    subject=
        safe_text,
    company=
        safe_text,
    category=
        safe_text,
    title=
        safe_text,
    creator=
        safe_text,
    description=
        safe_text,
    manager=
        safe_text,
    hyperlinkBase_href=
        safe_text,
    buildNumberCreated=
        safe_text,
    buildNumberEdited=
        safe_text,
    alternateNames=
        safe_text,
    keywords=
        safe_text,
    template=
        safe_text
)
SolutionXML_strategy = st.builds(
    SolutionXML,
)
EmailRoutingData_strategy = st.builds(
    EmailRoutingData,
)
DocumentPropertiesCollection_strategy = st.builds(
    DocumentPropertiesCollection,
)
DatadiagramMLXForm_VisioDocument_strategy = st.builds(
    DatadiagramMLXForm_VisioDocument,
    start=
        safe_text,
    buildnum=
        safe_text,
    version=
        safe_text,
    docLangId=
        safe_text,
    key=
        safe_text,
    metric=
        safe_text
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
DatadiagramMLXForm_CellType_strategy = st.builds(
    DatadiagramMLXForm_CellType,
    unit=
        safe_text,
    formula=
        safe_text,
    value=
        safe_text,
    err=
        safe_text
)
ColorsTable_strategy = st.builds(
    ColorsTable,
)
DocumentSettingsElt_strategy = st.builds(
    DocumentSettingsElt,
)
DatadiagramMLXForm_DateTimeType_strategy = st.builds(
    DatadiagramMLXForm_DateTimeType,
    hour=
        safe_text,
    second=
        safe_text,
    year=
        safe_text,
    day=
        safe_text,
    month=
        safe_text,
    minute=
        safe_text
)
DatadiagramMLXForm_SolutionXML_strategy = st.builds(
    DatadiagramMLXForm_SolutionXML,
)
DatadiagramMLXForm_HeaderFooter_strategy = st.builds(
    DatadiagramMLXForm_HeaderFooter,
)
DatadiagramMLXForm_EventList_strategy = st.builds(
    DatadiagramMLXForm_EventList,
)
DatadiagramMLXForm_WindowsInfo_strategy = st.builds(
    DatadiagramMLXForm_WindowsInfo,
)
DatadiagramMLXForm_PageElt_strategy = st.builds(
    DatadiagramMLXForm_PageElt,
)
DatadiagramMLXForm_Page_strategy = st.builds(
    DatadiagramMLXForm_Page,
    viewCenterX=
        safe_text,
    background=
        safe_text,
    viewScale=
        safe_text,
    associatedPage=
        safe_text,
    backPage=
        safe_text,
    ViewCenterY=
        safe_text,
    reviewerID=
        safe_text
)
DatadiagramMLXForm_PagesCollection_strategy = st.builds(
    DatadiagramMLXForm_PagesCollection,
)
DatadiagramMLXForm_MasterElt_strategy = st.builds(
    DatadiagramMLXForm_MasterElt,
)
Connect_strategy = st.builds(
    Connect,
)
DatadiagramMLXForm_ConnectsCollection_strategy = st.builds(
    DatadiagramMLXForm_ConnectsCollection,
)
DatadiagramMLXForm_ShapesCollection_strategy = st.builds(
    DatadiagramMLXForm_ShapesCollection,
)
ConnectsCollection_strategy = st.builds(
    ConnectsCollection,
)
DatadiagramMLXForm_Connect_strategy = st.builds(
    DatadiagramMLXForm_Connect,
    fromPart=
        safe_text,
    toPart=
        safe_text,
    toCell=
        safe_text,
    toSheet=
        safe_text,
    fromSheet=
        safe_text,
    fromCell=
        safe_text
)
DatadiagramMLXForm_MasterShortCut_strategy = st.builds(
    DatadiagramMLXForm_MasterShortCut,
    iconSize=
        safe_text,
    shortcutHelp=
        safe_text,
    prompt=
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
DatadiagramMLXForm_Master_strategy = st.builds(
    DatadiagramMLXForm_Master,
    matchByName=
        safe_text,
    iconSize=
        safe_text,
    alignName=
        safe_text,
    hidden=
        safe_text,
    iconUpdate=
        safe_text,
    patternFlags=
        safe_text,
    prompt=
        safe_text,
    baseID=
        safe_text
)
Master_strategy = st.builds(
    Master,
)
DatadiagramMLXForm_Icon_strategy = st.builds(
    DatadiagramMLXForm_Icon,
    value=
        safe_text
)
Icon_strategy = st.builds(
    Icon,
)
DatadiagramMLXForm_XForm_strategy = st.builds(
    DatadiagramMLXForm_XForm,
)
DatadiagramMLXForm_MastersCollection_strategy = st.builds(
    DatadiagramMLXForm_MastersCollection,
)
DatadiagramMLXForm_Field_strategy = st.builds(
    DatadiagramMLXForm_Field,
)
TabsCollection_strategy = st.builds(
    TabsCollection,
)
DatadiagramMLXForm_Tab_strategy = st.builds(
    DatadiagramMLXForm_Tab,
)
Tab_strategy = st.builds(
    Tab,
)
DatadiagramMLXForm_TabsCollection_strategy = st.builds(
    DatadiagramMLXForm_TabsCollection,
)
DatadiagramMLXForm_Para_strategy = st.builds(
    DatadiagramMLXForm_Para,
)
DatadiagramMLXForm_Char_strategy = st.builds(
    DatadiagramMLXForm_Char,
)
TextElt_strategy = st.builds(
    TextElt,
)
DatadiagramMLXForm_Pp_strategy = st.builds(
    DatadiagramMLXForm_Pp,
)
DatadiagramMLXForm_Fld_strategy = st.builds(
    DatadiagramMLXForm_Fld,
)
DatadiagramMLXForm_Cp_strategy = st.builds(
    DatadiagramMLXForm_Cp,
)
DatadiagramMLXForm_StringElt_strategy = st.builds(
    DatadiagramMLXForm_StringElt,
    value=
        safe_text
)
DatadiagramMLXForm_Tp_strategy = st.builds(
    DatadiagramMLXForm_Tp,
)
DatadiagramMLXForm_Text_strategy = st.builds(
    DatadiagramMLXForm_Text,
)
XYABCDEElt_strategy = st.builds(
    XYABCDEElt,
)
DatadiagramMLXForm_NURBSTo_strategy = st.builds(
    DatadiagramMLXForm_NURBSTo,
)
XYABCDElt_strategy = st.builds(
    XYABCDElt,
)
DatadiagramMLXForm_XYABCDEElt_strategy = st.builds(
    DatadiagramMLXForm_XYABCDEElt,
)
DatadiagramMLXForm_EllipticalArcTo_strategy = st.builds(
    DatadiagramMLXForm_EllipticalArcTo,
)
DatadiagramMLXForm_SplineStart_strategy = st.builds(
    DatadiagramMLXForm_SplineStart,
)
DatadiagramMLXForm_Ellipse_strategy = st.builds(
    DatadiagramMLXForm_Ellipse,
)

@given(instance=DatadiagramMLXForm_IXrequiredElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_ixrequiredelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_IXrequiredElt)



@given(instance=DatadiagramMLXForm_IXrequiredElt_strategy)
def test_datadiagrammlxform_ixrequiredelt_iX_setter(instance):
    original = instance.iX
    instance.iX = original
    assert instance.iX == original

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=DatadiagramMLXForm_TextElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_textelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_TextElt)

@given(instance=Geom_strategy)
@settings(max_examples=50)
def test_geom_instantiation(instance):
    assert isinstance(instance, Geom)

@given(instance=XYElt_strategy)
@settings(max_examples=50)
def test_xyelt_instantiation(instance):
    assert isinstance(instance, XYElt)

@given(instance=DatadiagramMLXForm_LineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_lineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_LineTo)

@given(instance=XYABElt_strategy)
@settings(max_examples=50)
def test_xyabelt_instantiation(instance):
    assert isinstance(instance, XYABElt)

@given(instance=DatadiagramMLXForm_XYABCDElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_xyabcdelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_XYABCDElt)

@given(instance=DatadiagramMLXForm_InfiniteLine_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_infiniteline_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_InfiniteLine)

@given(instance=XYAElt_strategy)
@settings(max_examples=50)
def test_xyaelt_instantiation(instance):
    assert isinstance(instance, XYAElt)

@given(instance=DatadiagramMLXForm_SplineKnot_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_splineknot_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_SplineKnot)

@given(instance=DatadiagramMLXForm_XYABElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_xyabelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_XYABElt)

@given(instance=DatadiagramMLXForm_PolylineTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_polylineto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_PolylineTo)

@given(instance=DatadiagramMLXForm_ArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_arcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_ArcTo)

@given(instance=DatadiagramMLXForm_XYAElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_xyaelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_XYAElt)

@given(instance=DatadiagramMLXForm_MoveTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_moveto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_MoveTo)

@given(instance=CellType_strategy)
@settings(max_examples=50)
def test_celltype_instantiation(instance):
    assert isinstance(instance, CellType)

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

@given(instance=DatadiagramMLXForm_IdentifiedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_identifiedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_IdentifiedElt)



@given(instance=DatadiagramMLXForm_IdentifiedElt_strategy)
def test_datadiagrammlxform_identifiedelt_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=DatadiagramMLXForm_NamedElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_namedelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_NamedElt)



@given(instance=DatadiagramMLXForm_NamedElt_strategy)
def test_datadiagrammlxform_namedelt_nameU_setter(instance):
    original = instance.nameU
    instance.nameU = original
    assert instance.nameU == original



@given(instance=DatadiagramMLXForm_NamedElt_strategy)
def test_datadiagrammlxform_namedelt_name_setter(instance):
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

@given(instance=UniqueIdElt_strategy)
@settings(max_examples=50)
def test_uniqueidelt_instantiation(instance):
    assert isinstance(instance, UniqueIdElt)

@given(instance=DelElt_strategy)
@settings(max_examples=50)
def test_delelt_instantiation(instance):
    assert isinstance(instance, DelElt)

@given(instance=IXElt_strategy)
@settings(max_examples=50)
def test_ixelt_instantiation(instance):
    assert isinstance(instance, IXElt)

@given(instance=DatadiagramMLXForm_XYElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_xyelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_XYElt)

@given(instance=DatadiagramMLXForm_DelElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_delelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_DelElt)



@given(instance=DatadiagramMLXForm_DelElt_strategy)
def test_datadiagrammlxform_delelt_del__setter(instance):
    original = instance.del_
    instance.del_ = original
    assert instance.del_ == original

@given(instance=DatadiagramMLXForm_IXElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_ixelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_IXElt)



@given(instance=DatadiagramMLXForm_IXElt_strategy)
def test_datadiagrammlxform_ixelt_iX_setter(instance):
    original = instance.iX
    instance.iX = original
    assert instance.iX == original

@given(instance=DatadiagramMLXForm_ShapeElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_shapeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_ShapeElt)

@given(instance=ShapeElt_strategy)
@settings(max_examples=50)
def test_shapeelt_instantiation(instance):
    assert isinstance(instance, ShapeElt)

@given(instance=DatadiagramMLXForm_Geom_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_geom_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Geom)

@given(instance=ShapesCollection_strategy)
@settings(max_examples=50)
def test_shapescollection_instantiation(instance):
    assert isinstance(instance, ShapesCollection)

@given(instance=DatadiagramMLXForm_Shape_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_shape_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Shape)



@given(instance=DatadiagramMLXForm_Shape_strategy)
def test_datadiagrammlxform_shape_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original



@given(instance=DatadiagramMLXForm_Shape_strategy)
def test_datadiagrammlxform_shape_textStyle_setter(instance):
    original = instance.textStyle
    instance.textStyle = original
    assert instance.textStyle == original



@given(instance=DatadiagramMLXForm_Shape_strategy)
def test_datadiagrammlxform_shape_fillStyle_setter(instance):
    original = instance.fillStyle
    instance.fillStyle = original
    assert instance.fillStyle == original

@given(instance=DatadiagramMLXForm_UniqueIdElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_uniqueidelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_UniqueIdElt)



@given(instance=DatadiagramMLXForm_UniqueIdElt_strategy)
def test_datadiagrammlxform_uniqueidelt_UniqueID_setter(instance):
    original = instance.UniqueID
    instance.UniqueID = original
    assert instance.UniqueID == original

@given(instance=PageSheet_strategy)
@settings(max_examples=50)
def test_pagesheet_instantiation(instance):
    assert isinstance(instance, PageSheet)

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=DatadiagramMLXForm_DocumentSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_documentsheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_DocumentSheet)

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=DatadiagramMLXForm_PageSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_pagesheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_PageSheet)

@given(instance=FaceName_strategy)
@settings(max_examples=50)
def test_facename_instantiation(instance):
    assert isinstance(instance, FaceName)

@given(instance=DatadiagramMLXForm_FaceNamesTable_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_facenamestable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_FaceNamesTable)

@given(instance=DatadiagramMLXForm_StyleSheetsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_stylesheetscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_StyleSheetsCollection)

@given(instance=DatadiagramMLXForm_EmailRoutingData_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_emailroutingdata_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_EmailRoutingData)



@given(instance=DatadiagramMLXForm_EmailRoutingData_strategy)
def test_datadiagrammlxform_emailroutingdata_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=DatadiagramMLXForm_EmailRoutingData_strategy)
def test_datadiagrammlxform_emailroutingdata_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=DatadiagramMLXForm_VBProjectData_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_vbprojectdata_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_VBProjectData)



@given(instance=DatadiagramMLXForm_VBProjectData_strategy)
def test_datadiagrammlxform_vbprojectdata_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=IdentifiedElt_strategy)
@settings(max_examples=50)
def test_identifiedelt_instantiation(instance):
    assert isinstance(instance, IdentifiedElt)

@given(instance=DatadiagramMLXForm_FaceName_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_facename_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_FaceName)



@given(instance=DatadiagramMLXForm_FaceName_strategy)
def test_datadiagrammlxform_facename_panos_setter(instance):
    original = instance.panos
    instance.panos = original
    assert instance.panos == original



@given(instance=DatadiagramMLXForm_FaceName_strategy)
def test_datadiagrammlxform_facename_unicodeRanges_setter(instance):
    original = instance.unicodeRanges
    instance.unicodeRanges = original
    assert instance.unicodeRanges == original



@given(instance=DatadiagramMLXForm_FaceName_strategy)
def test_datadiagrammlxform_facename_flags_setter(instance):
    original = instance.flags
    instance.flags = original
    assert instance.flags == original



@given(instance=DatadiagramMLXForm_FaceName_strategy)
def test_datadiagrammlxform_facename_charSet_setter(instance):
    original = instance.charSet
    instance.charSet = original
    assert instance.charSet == original



@given(instance=DatadiagramMLXForm_FaceName_strategy)
def test_datadiagrammlxform_facename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DatadiagramMLXForm_StyleSheet_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_stylesheet_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_StyleSheet)

@given(instance=DatadiagramMLXForm_FontEntry_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_fontentry_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_FontEntry)



@given(instance=DatadiagramMLXForm_FontEntry_strategy)
def test_datadiagrammlxform_fontentry_charSet_setter(instance):
    original = instance.charSet
    instance.charSet = original
    assert instance.charSet == original



@given(instance=DatadiagramMLXForm_FontEntry_strategy)
def test_datadiagrammlxform_fontentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=DatadiagramMLXForm_FontEntry_strategy)
def test_datadiagrammlxform_fontentry_unicode_setter(instance):
    original = instance.unicode
    instance.unicode = original
    assert instance.unicode == original



@given(instance=DatadiagramMLXForm_FontEntry_strategy)
def test_datadiagrammlxform_fontentry_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=DatadiagramMLXForm_FontEntry_strategy)
def test_datadiagrammlxform_fontentry_attributes_setter(instance):
    original = instance.attributes
    instance.attributes = original
    assert instance.attributes == original



@given(instance=DatadiagramMLXForm_FontEntry_strategy)
def test_datadiagrammlxform_fontentry_pitchAndFamily_setter(instance):
    original = instance.pitchAndFamily
    instance.pitchAndFamily = original
    assert instance.pitchAndFamily == original

@given(instance=FontEntry_strategy)
@settings(max_examples=50)
def test_fontentry_instantiation(instance):
    assert isinstance(instance, FontEntry)

@given(instance=DatadiagramMLXForm_FontsTable_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_fontstable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_FontsTable)

@given(instance=DatadiagramMLXForm_PrintSetup_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_printsetup_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_PrintSetup)

@given(instance=SnapAnglesCollection_strategy)
@settings(max_examples=50)
def test_snapanglescollection_instantiation(instance):
    assert isinstance(instance, SnapAnglesCollection)

@given(instance=IXrequiredElt_strategy)
@settings(max_examples=50)
def test_ixrequiredelt_instantiation(instance):
    assert isinstance(instance, IXrequiredElt)

@given(instance=DatadiagramMLXForm_ColorEntry_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_colorentry_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_ColorEntry)



@given(instance=DatadiagramMLXForm_ColorEntry_strategy)
def test_datadiagrammlxform_colorentry_rgb_setter(instance):
    original = instance.rgb
    instance.rgb = original
    assert instance.rgb == original

@given(instance=ColorEntry_strategy)
@settings(max_examples=50)
def test_colorentry_instantiation(instance):
    assert isinstance(instance, ColorEntry)

@given(instance=StyleSheet_strategy)
@settings(max_examples=50)
def test_stylesheet_instantiation(instance):
    assert isinstance(instance, StyleSheet)

@given(instance=DatadiagramMLXForm_ColorsTable_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_colorstable_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_ColorsTable)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=DatadiagramMLXForm_SnapAngle_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_snapangle_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_SnapAngle)



@given(instance=DatadiagramMLXForm_SnapAngle_strategy)
def test_datadiagrammlxform_snapangle_angleValue_setter(instance):
    original = instance.angleValue
    instance.angleValue = original
    assert instance.angleValue == original

@given(instance=SnapAngle_strategy)
@settings(max_examples=50)
def test_snapangle_instantiation(instance):
    assert isinstance(instance, SnapAngle)

@given(instance=DatadiagramMLXForm_SnapAnglesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_snapanglescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_SnapAnglesCollection)

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=CustomPropertiesCollection_strategy)
@settings(max_examples=50)
def test_custompropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomPropertiesCollection)

@given(instance=DatadiagramMLXForm_DocumentSettingsElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_documentsettingselt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_DocumentSettingsElt)



@given(instance=DatadiagramMLXForm_DocumentSettingsElt_strategy)
def test_datadiagrammlxform_documentsettingselt_snapExtensions_setter(instance):
    original = instance.snapExtensions
    instance.snapExtensions = original
    assert instance.snapExtensions == original



@given(instance=DatadiagramMLXForm_DocumentSettingsElt_strategy)
def test_datadiagrammlxform_documentsettingselt_customToolbarsFile_setter(instance):
    original = instance.customToolbarsFile
    instance.customToolbarsFile = original
    assert instance.customToolbarsFile == original



@given(instance=DatadiagramMLXForm_DocumentSettingsElt_strategy)
def test_datadiagrammlxform_documentsettingselt_protectMasters_setter(instance):
    original = instance.protectMasters
    instance.protectMasters = original
    assert instance.protectMasters == original



@given(instance=DatadiagramMLXForm_DocumentSettingsElt_strategy)
def test_datadiagrammlxform_documentsettingselt_glueSettings_setter(instance):
    original = instance.glueSettings
    instance.glueSettings = original
    assert instance.glueSettings == original



@given(instance=DatadiagramMLXForm_DocumentSettingsElt_strategy)
def test_datadiagrammlxform_documentsettingselt_protectShapes_setter(instance):
    original = instance.protectShapes
    instance.protectShapes = original
    assert instance.protectShapes == original



@given(instance=DatadiagramMLXForm_DocumentSettingsElt_strategy)
def test_datadiagrammlxform_documentsettingselt_protectBkgnds_setter(instance):
    original = instance.protectBkgnds
    instance.protectBkgnds = original
    assert instance.protectBkgnds == original



@given(instance=DatadiagramMLXForm_DocumentSettingsElt_strategy)
def test_datadiagrammlxform_documentsettingselt_attachedToolbars_setter(instance):
    original = instance.attachedToolbars
    instance.attachedToolbars = original
    assert instance.attachedToolbars == original



@given(instance=DatadiagramMLXForm_DocumentSettingsElt_strategy)
def test_datadiagrammlxform_documentsettingselt_dynamicGridEnabled_setter(instance):
    original = instance.dynamicGridEnabled
    instance.dynamicGridEnabled = original
    assert instance.dynamicGridEnabled == original



@given(instance=DatadiagramMLXForm_DocumentSettingsElt_strategy)
def test_datadiagrammlxform_documentsettingselt_customMenusFile_setter(instance):
    original = instance.customMenusFile
    instance.customMenusFile = original
    assert instance.customMenusFile == original



@given(instance=DatadiagramMLXForm_DocumentSettingsElt_strategy)
def test_datadiagrammlxform_documentsettingselt_snapSettings_setter(instance):
    original = instance.snapSettings
    instance.snapSettings = original
    assert instance.snapSettings == original



@given(instance=DatadiagramMLXForm_DocumentSettingsElt_strategy)
def test_datadiagrammlxform_documentsettingselt_protectStyles_setter(instance):
    original = instance.protectStyles
    instance.protectStyles = original
    assert instance.protectStyles == original

@given(instance=DatadiagramMLXForm_CustomProperty_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_customproperty_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_CustomProperty)



@given(instance=DatadiagramMLXForm_CustomProperty_strategy)
def test_datadiagrammlxform_customproperty_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original



@given(instance=DatadiagramMLXForm_CustomProperty_strategy)
def test_datadiagrammlxform_customproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CustomProperty_strategy)
@settings(max_examples=50)
def test_customproperty_instantiation(instance):
    assert isinstance(instance, CustomProperty)

@given(instance=DatadiagramMLXForm_CustomPropertiesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_custompropertiescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_CustomPropertiesCollection)

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

@given(instance=StyleSheetsCollection_strategy)
@settings(max_examples=50)
def test_stylesheetscollection_instantiation(instance):
    assert isinstance(instance, StyleSheetsCollection)

@given(instance=VisioDocument_strategy)
@settings(max_examples=50)
def test_visiodocument_instantiation(instance):
    assert isinstance(instance, VisioDocument)

@given(instance=DatadiagramMLXForm_DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_DocumentPropertiesCollection)



@given(instance=DatadiagramMLXForm_DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform_documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=DatadiagramMLXForm_DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform_documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=DatadiagramMLXForm_DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform_documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=DatadiagramMLXForm_DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform_documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=DatadiagramMLXForm_DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform_documentpropertiescollection_creator_setter(instance):
    original = instance.creator
    instance.creator = original
    assert instance.creator == original



@given(instance=DatadiagramMLXForm_DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform_documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=DatadiagramMLXForm_DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform_documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original



@given(instance=DatadiagramMLXForm_DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform_documentpropertiescollection_hyperlinkBase_href_setter(instance):
    original = instance.hyperlinkBase_href
    instance.hyperlinkBase_href = original
    assert instance.hyperlinkBase_href == original



@given(instance=DatadiagramMLXForm_DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform_documentpropertiescollection_buildNumberCreated_setter(instance):
    original = instance.buildNumberCreated
    instance.buildNumberCreated = original
    assert instance.buildNumberCreated == original



@given(instance=DatadiagramMLXForm_DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform_documentpropertiescollection_buildNumberEdited_setter(instance):
    original = instance.buildNumberEdited
    instance.buildNumberEdited = original
    assert instance.buildNumberEdited == original



@given(instance=DatadiagramMLXForm_DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform_documentpropertiescollection_alternateNames_setter(instance):
    original = instance.alternateNames
    instance.alternateNames = original
    assert instance.alternateNames == original



@given(instance=DatadiagramMLXForm_DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform_documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=DatadiagramMLXForm_DocumentPropertiesCollection_strategy)
def test_datadiagrammlxform_documentpropertiescollection_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=SolutionXML_strategy)
@settings(max_examples=50)
def test_solutionxml_instantiation(instance):
    assert isinstance(instance, SolutionXML)

@given(instance=EmailRoutingData_strategy)
@settings(max_examples=50)
def test_emailroutingdata_instantiation(instance):
    assert isinstance(instance, EmailRoutingData)

@given(instance=DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DocumentPropertiesCollection)

@given(instance=DatadiagramMLXForm_VisioDocument_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_visiodocument_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_VisioDocument)



@given(instance=DatadiagramMLXForm_VisioDocument_strategy)
def test_datadiagrammlxform_visiodocument_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=DatadiagramMLXForm_VisioDocument_strategy)
def test_datadiagrammlxform_visiodocument_buildnum_setter(instance):
    original = instance.buildnum
    instance.buildnum = original
    assert instance.buildnum == original



@given(instance=DatadiagramMLXForm_VisioDocument_strategy)
def test_datadiagrammlxform_visiodocument_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=DatadiagramMLXForm_VisioDocument_strategy)
def test_datadiagrammlxform_visiodocument_docLangId_setter(instance):
    original = instance.docLangId
    instance.docLangId = original
    assert instance.docLangId == original



@given(instance=DatadiagramMLXForm_VisioDocument_strategy)
def test_datadiagrammlxform_visiodocument_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=DatadiagramMLXForm_VisioDocument_strategy)
def test_datadiagrammlxform_visiodocument_metric_setter(instance):
    original = instance.metric
    instance.metric = original
    assert instance.metric == original

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

@given(instance=DatadiagramMLXForm_CellType_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_celltype_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_CellType)



@given(instance=DatadiagramMLXForm_CellType_strategy)
def test_datadiagrammlxform_celltype_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=DatadiagramMLXForm_CellType_strategy)
def test_datadiagrammlxform_celltype_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original



@given(instance=DatadiagramMLXForm_CellType_strategy)
def test_datadiagrammlxform_celltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=DatadiagramMLXForm_CellType_strategy)
def test_datadiagrammlxform_celltype_err_setter(instance):
    original = instance.err
    instance.err = original
    assert instance.err == original

@given(instance=ColorsTable_strategy)
@settings(max_examples=50)
def test_colorstable_instantiation(instance):
    assert isinstance(instance, ColorsTable)

@given(instance=DocumentSettingsElt_strategy)
@settings(max_examples=50)
def test_documentsettingselt_instantiation(instance):
    assert isinstance(instance, DocumentSettingsElt)

@given(instance=DatadiagramMLXForm_DateTimeType_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_datetimetype_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_DateTimeType)



@given(instance=DatadiagramMLXForm_DateTimeType_strategy)
def test_datadiagrammlxform_datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original



@given(instance=DatadiagramMLXForm_DateTimeType_strategy)
def test_datadiagrammlxform_datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original



@given(instance=DatadiagramMLXForm_DateTimeType_strategy)
def test_datadiagrammlxform_datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=DatadiagramMLXForm_DateTimeType_strategy)
def test_datadiagrammlxform_datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=DatadiagramMLXForm_DateTimeType_strategy)
def test_datadiagrammlxform_datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=DatadiagramMLXForm_DateTimeType_strategy)
def test_datadiagrammlxform_datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original

@given(instance=DatadiagramMLXForm_SolutionXML_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_solutionxml_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_SolutionXML)

@given(instance=DatadiagramMLXForm_HeaderFooter_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_headerfooter_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_HeaderFooter)

@given(instance=DatadiagramMLXForm_EventList_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_eventlist_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_EventList)

@given(instance=DatadiagramMLXForm_WindowsInfo_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_windowsinfo_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_WindowsInfo)

@given(instance=DatadiagramMLXForm_PageElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_pageelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_PageElt)

@given(instance=DatadiagramMLXForm_Page_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_page_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Page)



@given(instance=DatadiagramMLXForm_Page_strategy)
def test_datadiagrammlxform_page_viewCenterX_setter(instance):
    original = instance.viewCenterX
    instance.viewCenterX = original
    assert instance.viewCenterX == original



@given(instance=DatadiagramMLXForm_Page_strategy)
def test_datadiagrammlxform_page_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=DatadiagramMLXForm_Page_strategy)
def test_datadiagrammlxform_page_viewScale_setter(instance):
    original = instance.viewScale
    instance.viewScale = original
    assert instance.viewScale == original



@given(instance=DatadiagramMLXForm_Page_strategy)
def test_datadiagrammlxform_page_associatedPage_setter(instance):
    original = instance.associatedPage
    instance.associatedPage = original
    assert instance.associatedPage == original



@given(instance=DatadiagramMLXForm_Page_strategy)
def test_datadiagrammlxform_page_backPage_setter(instance):
    original = instance.backPage
    instance.backPage = original
    assert instance.backPage == original



@given(instance=DatadiagramMLXForm_Page_strategy)
def test_datadiagrammlxform_page_ViewCenterY_setter(instance):
    original = instance.ViewCenterY
    instance.ViewCenterY = original
    assert instance.ViewCenterY == original



@given(instance=DatadiagramMLXForm_Page_strategy)
def test_datadiagrammlxform_page_reviewerID_setter(instance):
    original = instance.reviewerID
    instance.reviewerID = original
    assert instance.reviewerID == original

@given(instance=DatadiagramMLXForm_PagesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_pagescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_PagesCollection)

@given(instance=DatadiagramMLXForm_MasterElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_masterelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_MasterElt)

@given(instance=Connect_strategy)
@settings(max_examples=50)
def test_connect_instantiation(instance):
    assert isinstance(instance, Connect)

@given(instance=DatadiagramMLXForm_ConnectsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_connectscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_ConnectsCollection)

@given(instance=DatadiagramMLXForm_ShapesCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_shapescollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_ShapesCollection)

@given(instance=ConnectsCollection_strategy)
@settings(max_examples=50)
def test_connectscollection_instantiation(instance):
    assert isinstance(instance, ConnectsCollection)

@given(instance=DatadiagramMLXForm_Connect_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_connect_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Connect)



@given(instance=DatadiagramMLXForm_Connect_strategy)
def test_datadiagrammlxform_connect_fromPart_setter(instance):
    original = instance.fromPart
    instance.fromPart = original
    assert instance.fromPart == original



@given(instance=DatadiagramMLXForm_Connect_strategy)
def test_datadiagrammlxform_connect_toPart_setter(instance):
    original = instance.toPart
    instance.toPart = original
    assert instance.toPart == original



@given(instance=DatadiagramMLXForm_Connect_strategy)
def test_datadiagrammlxform_connect_toCell_setter(instance):
    original = instance.toCell
    instance.toCell = original
    assert instance.toCell == original



@given(instance=DatadiagramMLXForm_Connect_strategy)
def test_datadiagrammlxform_connect_toSheet_setter(instance):
    original = instance.toSheet
    instance.toSheet = original
    assert instance.toSheet == original



@given(instance=DatadiagramMLXForm_Connect_strategy)
def test_datadiagrammlxform_connect_fromSheet_setter(instance):
    original = instance.fromSheet
    instance.fromSheet = original
    assert instance.fromSheet == original



@given(instance=DatadiagramMLXForm_Connect_strategy)
def test_datadiagrammlxform_connect_fromCell_setter(instance):
    original = instance.fromCell
    instance.fromCell = original
    assert instance.fromCell == original

@given(instance=DatadiagramMLXForm_MasterShortCut_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_mastershortcut_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_MasterShortCut)



@given(instance=DatadiagramMLXForm_MasterShortCut_strategy)
def test_datadiagrammlxform_mastershortcut_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original



@given(instance=DatadiagramMLXForm_MasterShortCut_strategy)
def test_datadiagrammlxform_mastershortcut_shortcutHelp_setter(instance):
    original = instance.shortcutHelp
    instance.shortcutHelp = original
    assert instance.shortcutHelp == original



@given(instance=DatadiagramMLXForm_MasterShortCut_strategy)
def test_datadiagrammlxform_mastershortcut_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original



@given(instance=DatadiagramMLXForm_MasterShortCut_strategy)
def test_datadiagrammlxform_mastershortcut_shortcutURL_setter(instance):
    original = instance.shortcutURL
    instance.shortcutURL = original
    assert instance.shortcutURL == original



@given(instance=DatadiagramMLXForm_MasterShortCut_strategy)
def test_datadiagrammlxform_mastershortcut_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original



@given(instance=DatadiagramMLXForm_MasterShortCut_strategy)
def test_datadiagrammlxform_mastershortcut_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original

@given(instance=MasterShortCut_strategy)
@settings(max_examples=50)
def test_mastershortcut_instantiation(instance):
    assert isinstance(instance, MasterShortCut)

@given(instance=DatadiagramMLXForm_Master_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_master_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Master)



@given(instance=DatadiagramMLXForm_Master_strategy)
def test_datadiagrammlxform_master_matchByName_setter(instance):
    original = instance.matchByName
    instance.matchByName = original
    assert instance.matchByName == original



@given(instance=DatadiagramMLXForm_Master_strategy)
def test_datadiagrammlxform_master_iconSize_setter(instance):
    original = instance.iconSize
    instance.iconSize = original
    assert instance.iconSize == original



@given(instance=DatadiagramMLXForm_Master_strategy)
def test_datadiagrammlxform_master_alignName_setter(instance):
    original = instance.alignName
    instance.alignName = original
    assert instance.alignName == original



@given(instance=DatadiagramMLXForm_Master_strategy)
def test_datadiagrammlxform_master_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original



@given(instance=DatadiagramMLXForm_Master_strategy)
def test_datadiagrammlxform_master_iconUpdate_setter(instance):
    original = instance.iconUpdate
    instance.iconUpdate = original
    assert instance.iconUpdate == original



@given(instance=DatadiagramMLXForm_Master_strategy)
def test_datadiagrammlxform_master_patternFlags_setter(instance):
    original = instance.patternFlags
    instance.patternFlags = original
    assert instance.patternFlags == original



@given(instance=DatadiagramMLXForm_Master_strategy)
def test_datadiagrammlxform_master_prompt_setter(instance):
    original = instance.prompt
    instance.prompt = original
    assert instance.prompt == original



@given(instance=DatadiagramMLXForm_Master_strategy)
def test_datadiagrammlxform_master_baseID_setter(instance):
    original = instance.baseID
    instance.baseID = original
    assert instance.baseID == original

@given(instance=Master_strategy)
@settings(max_examples=50)
def test_master_instantiation(instance):
    assert isinstance(instance, Master)

@given(instance=DatadiagramMLXForm_Icon_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_icon_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Icon)



@given(instance=DatadiagramMLXForm_Icon_strategy)
def test_datadiagrammlxform_icon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Icon_strategy)
@settings(max_examples=50)
def test_icon_instantiation(instance):
    assert isinstance(instance, Icon)

@given(instance=DatadiagramMLXForm_XForm_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_xform_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_XForm)

@given(instance=DatadiagramMLXForm_MastersCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_masterscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_MastersCollection)

@given(instance=DatadiagramMLXForm_Field_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_field_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Field)

@given(instance=TabsCollection_strategy)
@settings(max_examples=50)
def test_tabscollection_instantiation(instance):
    assert isinstance(instance, TabsCollection)

@given(instance=DatadiagramMLXForm_Tab_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_tab_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Tab)

@given(instance=Tab_strategy)
@settings(max_examples=50)
def test_tab_instantiation(instance):
    assert isinstance(instance, Tab)

@given(instance=DatadiagramMLXForm_TabsCollection_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_tabscollection_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_TabsCollection)

@given(instance=DatadiagramMLXForm_Para_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_para_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Para)

@given(instance=DatadiagramMLXForm_Char_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_char_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Char)

@given(instance=TextElt_strategy)
@settings(max_examples=50)
def test_textelt_instantiation(instance):
    assert isinstance(instance, TextElt)

@given(instance=DatadiagramMLXForm_Pp_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_pp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Pp)

@given(instance=DatadiagramMLXForm_Fld_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_fld_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Fld)

@given(instance=DatadiagramMLXForm_Cp_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_cp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Cp)

@given(instance=DatadiagramMLXForm_StringElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_stringelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_StringElt)



@given(instance=DatadiagramMLXForm_StringElt_strategy)
def test_datadiagrammlxform_stringelt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DatadiagramMLXForm_Tp_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_tp_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Tp)

@given(instance=DatadiagramMLXForm_Text_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_text_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Text)

@given(instance=XYABCDEElt_strategy)
@settings(max_examples=50)
def test_xyabcdeelt_instantiation(instance):
    assert isinstance(instance, XYABCDEElt)

@given(instance=DatadiagramMLXForm_NURBSTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_nurbsto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_NURBSTo)

@given(instance=XYABCDElt_strategy)
@settings(max_examples=50)
def test_xyabcdelt_instantiation(instance):
    assert isinstance(instance, XYABCDElt)

@given(instance=DatadiagramMLXForm_XYABCDEElt_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_xyabcdeelt_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_XYABCDEElt)

@given(instance=DatadiagramMLXForm_EllipticalArcTo_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_ellipticalarcto_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_EllipticalArcTo)

@given(instance=DatadiagramMLXForm_SplineStart_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_splinestart_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_SplineStart)

@given(instance=DatadiagramMLXForm_Ellipse_strategy)
@settings(max_examples=50)
def test_datadiagrammlxform_ellipse_instantiation(instance):
    assert isinstance(instance, DatadiagramMLXForm_Ellipse)
