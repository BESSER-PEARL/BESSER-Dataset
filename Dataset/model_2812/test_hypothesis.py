import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    xygraph_EObject,
    xygraph_FontDescriptor,
    xygraph_TraceDescriptor,
    xygraph_AxisDescriptor,
    xygraph_ColorDescriptor,
    xygraph_XYGraphDescriptor,
    Trace_BaseLine,
    Trace_TraceType,
    ZoomType,
    LinearScale_Orientation,
    Trace_ErrorBarType,
    Trace_PointStyle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xygraph_eobject_is_not_abstract():
    assert not inspect.isabstract(xygraph_EObject)


def test_xygraph_eobject_constructor_exists():
    assert callable(xygraph_EObject.__init__)


def test_xygraph_eobject_constructor_args():
    sig = inspect.signature(xygraph_EObject.__init__)
    params = list(sig.parameters.keys())



def test_xygraph_fontdescriptor_is_not_abstract():
    assert not inspect.isabstract(xygraph_FontDescriptor)


def test_xygraph_fontdescriptor_constructor_exists():
    assert callable(xygraph_FontDescriptor.__init__)


def test_xygraph_fontdescriptor_constructor_args():
    sig = inspect.signature(xygraph_FontDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "size" in params, "Missing parameter 'size'"
    assert "name" in params, "Missing parameter 'name'"

def test_xygraph_fontdescriptor_has_style():
    assert hasattr(xygraph_FontDescriptor, "style")
    descriptor = None
    for klass in xygraph_FontDescriptor.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_fontdescriptor_has_size():
    assert hasattr(xygraph_FontDescriptor, "size")
    descriptor = None
    for klass in xygraph_FontDescriptor.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_fontdescriptor_has_name():
    assert hasattr(xygraph_FontDescriptor, "name")
    descriptor = None
    for klass in xygraph_FontDescriptor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xygraph_tracedescriptor_is_not_abstract():
    assert not inspect.isabstract(xygraph_TraceDescriptor)


def test_xygraph_tracedescriptor_constructor_exists():
    assert callable(xygraph_TraceDescriptor.__init__)


def test_xygraph_tracedescriptor_constructor_args():
    sig = inspect.signature(xygraph_TraceDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "yErrorBarType" in params, "Missing parameter 'yErrorBarType'"
    assert "traceType" in params, "Missing parameter 'traceType'"
    assert "areaAlpha" in params, "Missing parameter 'areaAlpha'"
    assert "xErrorBarType" in params, "Missing parameter 'xErrorBarType'"
    assert "baseLine" in params, "Missing parameter 'baseLine'"
    assert "errorBarEnabled" in params, "Missing parameter 'errorBarEnabled'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "errorBarCapWidth" in params, "Missing parameter 'errorBarCapWidth'"
    assert "name" in params, "Missing parameter 'name'"
    assert "drawYErrorInArea" in params, "Missing parameter 'drawYErrorInArea'"
    assert "pointSize" in params, "Missing parameter 'pointSize'"
    assert "pointStyle" in params, "Missing parameter 'pointStyle'"
    assert "antiAliasing" in params, "Missing parameter 'antiAliasing'"

def test_xygraph_tracedescriptor_has_yErrorBarType():
    assert hasattr(xygraph_TraceDescriptor, "yErrorBarType")
    descriptor = None
    for klass in xygraph_TraceDescriptor.__mro__:
        if "yErrorBarType" in klass.__dict__:
            descriptor = klass.__dict__["yErrorBarType"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_tracedescriptor_has_traceType():
    assert hasattr(xygraph_TraceDescriptor, "traceType")
    descriptor = None
    for klass in xygraph_TraceDescriptor.__mro__:
        if "traceType" in klass.__dict__:
            descriptor = klass.__dict__["traceType"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_tracedescriptor_has_areaAlpha():
    assert hasattr(xygraph_TraceDescriptor, "areaAlpha")
    descriptor = None
    for klass in xygraph_TraceDescriptor.__mro__:
        if "areaAlpha" in klass.__dict__:
            descriptor = klass.__dict__["areaAlpha"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_tracedescriptor_has_xErrorBarType():
    assert hasattr(xygraph_TraceDescriptor, "xErrorBarType")
    descriptor = None
    for klass in xygraph_TraceDescriptor.__mro__:
        if "xErrorBarType" in klass.__dict__:
            descriptor = klass.__dict__["xErrorBarType"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_tracedescriptor_has_baseLine():
    assert hasattr(xygraph_TraceDescriptor, "baseLine")
    descriptor = None
    for klass in xygraph_TraceDescriptor.__mro__:
        if "baseLine" in klass.__dict__:
            descriptor = klass.__dict__["baseLine"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_tracedescriptor_has_errorBarEnabled():
    assert hasattr(xygraph_TraceDescriptor, "errorBarEnabled")
    descriptor = None
    for klass in xygraph_TraceDescriptor.__mro__:
        if "errorBarEnabled" in klass.__dict__:
            descriptor = klass.__dict__["errorBarEnabled"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_tracedescriptor_has_lineWidth():
    assert hasattr(xygraph_TraceDescriptor, "lineWidth")
    descriptor = None
    for klass in xygraph_TraceDescriptor.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_tracedescriptor_has_errorBarCapWidth():
    assert hasattr(xygraph_TraceDescriptor, "errorBarCapWidth")
    descriptor = None
    for klass in xygraph_TraceDescriptor.__mro__:
        if "errorBarCapWidth" in klass.__dict__:
            descriptor = klass.__dict__["errorBarCapWidth"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_tracedescriptor_has_name():
    assert hasattr(xygraph_TraceDescriptor, "name")
    descriptor = None
    for klass in xygraph_TraceDescriptor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_tracedescriptor_has_drawYErrorInArea():
    assert hasattr(xygraph_TraceDescriptor, "drawYErrorInArea")
    descriptor = None
    for klass in xygraph_TraceDescriptor.__mro__:
        if "drawYErrorInArea" in klass.__dict__:
            descriptor = klass.__dict__["drawYErrorInArea"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_tracedescriptor_has_pointSize():
    assert hasattr(xygraph_TraceDescriptor, "pointSize")
    descriptor = None
    for klass in xygraph_TraceDescriptor.__mro__:
        if "pointSize" in klass.__dict__:
            descriptor = klass.__dict__["pointSize"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_tracedescriptor_has_pointStyle():
    assert hasattr(xygraph_TraceDescriptor, "pointStyle")
    descriptor = None
    for klass in xygraph_TraceDescriptor.__mro__:
        if "pointStyle" in klass.__dict__:
            descriptor = klass.__dict__["pointStyle"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_tracedescriptor_has_antiAliasing():
    assert hasattr(xygraph_TraceDescriptor, "antiAliasing")
    descriptor = None
    for klass in xygraph_TraceDescriptor.__mro__:
        if "antiAliasing" in klass.__dict__:
            descriptor = klass.__dict__["antiAliasing"]
            break
    assert isinstance(descriptor, property)



def test_xygraph_axisdescriptor_is_not_abstract():
    assert not inspect.isabstract(xygraph_AxisDescriptor)


def test_xygraph_axisdescriptor_constructor_exists():
    assert callable(xygraph_AxisDescriptor.__init__)


def test_xygraph_axisdescriptor_constructor_args():
    sig = inspect.signature(xygraph_AxisDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "showMinorGrid" in params, "Missing parameter 'showMinorGrid'"
    assert "showMajorGrid" in params, "Missing parameter 'showMajorGrid'"
    assert "dashGridLine" in params, "Missing parameter 'dashGridLine'"
    assert "dateEnabled" in params, "Missing parameter 'dateEnabled'"
    assert "autoScaleThreshold" in params, "Missing parameter 'autoScaleThreshold'"
    assert "logScale" in params, "Missing parameter 'logScale'"
    assert "title" in params, "Missing parameter 'title'"
    assert "zoomType" in params, "Missing parameter 'zoomType'"
    assert "autoFormat" in params, "Missing parameter 'autoFormat'"
    assert "formatPattern" in params, "Missing parameter 'formatPattern'"
    assert "minorTicksVisible" in params, "Missing parameter 'minorTicksVisible'"
    assert "autoScale" in params, "Missing parameter 'autoScale'"
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "primarySide" in params, "Missing parameter 'primarySide'"
    assert "rangeLower" in params, "Missing parameter 'rangeLower'"
    assert "rangeUpper" in params, "Missing parameter 'rangeUpper'"

def test_xygraph_axisdescriptor_has_showMinorGrid():
    assert hasattr(xygraph_AxisDescriptor, "showMinorGrid")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "showMinorGrid" in klass.__dict__:
            descriptor = klass.__dict__["showMinorGrid"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_showMajorGrid():
    assert hasattr(xygraph_AxisDescriptor, "showMajorGrid")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "showMajorGrid" in klass.__dict__:
            descriptor = klass.__dict__["showMajorGrid"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_dashGridLine():
    assert hasattr(xygraph_AxisDescriptor, "dashGridLine")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "dashGridLine" in klass.__dict__:
            descriptor = klass.__dict__["dashGridLine"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_dateEnabled():
    assert hasattr(xygraph_AxisDescriptor, "dateEnabled")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "dateEnabled" in klass.__dict__:
            descriptor = klass.__dict__["dateEnabled"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_autoScaleThreshold():
    assert hasattr(xygraph_AxisDescriptor, "autoScaleThreshold")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "autoScaleThreshold" in klass.__dict__:
            descriptor = klass.__dict__["autoScaleThreshold"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_logScale():
    assert hasattr(xygraph_AxisDescriptor, "logScale")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "logScale" in klass.__dict__:
            descriptor = klass.__dict__["logScale"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_title():
    assert hasattr(xygraph_AxisDescriptor, "title")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_zoomType():
    assert hasattr(xygraph_AxisDescriptor, "zoomType")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "zoomType" in klass.__dict__:
            descriptor = klass.__dict__["zoomType"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_autoFormat():
    assert hasattr(xygraph_AxisDescriptor, "autoFormat")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "autoFormat" in klass.__dict__:
            descriptor = klass.__dict__["autoFormat"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_formatPattern():
    assert hasattr(xygraph_AxisDescriptor, "formatPattern")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "formatPattern" in klass.__dict__:
            descriptor = klass.__dict__["formatPattern"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_minorTicksVisible():
    assert hasattr(xygraph_AxisDescriptor, "minorTicksVisible")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "minorTicksVisible" in klass.__dict__:
            descriptor = klass.__dict__["minorTicksVisible"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_autoScale():
    assert hasattr(xygraph_AxisDescriptor, "autoScale")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "autoScale" in klass.__dict__:
            descriptor = klass.__dict__["autoScale"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_orientation():
    assert hasattr(xygraph_AxisDescriptor, "orientation")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_primarySide():
    assert hasattr(xygraph_AxisDescriptor, "primarySide")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "primarySide" in klass.__dict__:
            descriptor = klass.__dict__["primarySide"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_rangeLower():
    assert hasattr(xygraph_AxisDescriptor, "rangeLower")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "rangeLower" in klass.__dict__:
            descriptor = klass.__dict__["rangeLower"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_axisdescriptor_has_rangeUpper():
    assert hasattr(xygraph_AxisDescriptor, "rangeUpper")
    descriptor = None
    for klass in xygraph_AxisDescriptor.__mro__:
        if "rangeUpper" in klass.__dict__:
            descriptor = klass.__dict__["rangeUpper"]
            break
    assert isinstance(descriptor, property)



def test_xygraph_colordescriptor_is_not_abstract():
    assert not inspect.isabstract(xygraph_ColorDescriptor)


def test_xygraph_colordescriptor_constructor_exists():
    assert callable(xygraph_ColorDescriptor.__init__)


def test_xygraph_colordescriptor_constructor_args():
    sig = inspect.signature(xygraph_ColorDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "g" in params, "Missing parameter 'g'"
    assert "b" in params, "Missing parameter 'b'"
    assert "r" in params, "Missing parameter 'r'"

def test_xygraph_colordescriptor_has_g():
    assert hasattr(xygraph_ColorDescriptor, "g")
    descriptor = None
    for klass in xygraph_ColorDescriptor.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_colordescriptor_has_b():
    assert hasattr(xygraph_ColorDescriptor, "b")
    descriptor = None
    for klass in xygraph_ColorDescriptor.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_colordescriptor_has_r():
    assert hasattr(xygraph_ColorDescriptor, "r")
    descriptor = None
    for klass in xygraph_ColorDescriptor.__mro__:
        if "r" in klass.__dict__:
            descriptor = klass.__dict__["r"]
            break
    assert isinstance(descriptor, property)



def test_xygraph_xygraphdescriptor_is_not_abstract():
    assert not inspect.isabstract(xygraph_XYGraphDescriptor)


def test_xygraph_xygraphdescriptor_constructor_exists():
    assert callable(xygraph_XYGraphDescriptor.__init__)


def test_xygraph_xygraphdescriptor_constructor_args():
    sig = inspect.signature(xygraph_XYGraphDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "zoomType" in params, "Missing parameter 'zoomType'"
    assert "showPlotAreaBorder" in params, "Missing parameter 'showPlotAreaBorder'"
    assert "showLegend" in params, "Missing parameter 'showLegend'"
    assert "showTitle" in params, "Missing parameter 'showTitle'"
    assert "transparent" in params, "Missing parameter 'transparent'"
    assert "title" in params, "Missing parameter 'title'"

def test_xygraph_xygraphdescriptor_has_zoomType():
    assert hasattr(xygraph_XYGraphDescriptor, "zoomType")
    descriptor = None
    for klass in xygraph_XYGraphDescriptor.__mro__:
        if "zoomType" in klass.__dict__:
            descriptor = klass.__dict__["zoomType"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_xygraphdescriptor_has_showPlotAreaBorder():
    assert hasattr(xygraph_XYGraphDescriptor, "showPlotAreaBorder")
    descriptor = None
    for klass in xygraph_XYGraphDescriptor.__mro__:
        if "showPlotAreaBorder" in klass.__dict__:
            descriptor = klass.__dict__["showPlotAreaBorder"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_xygraphdescriptor_has_showLegend():
    assert hasattr(xygraph_XYGraphDescriptor, "showLegend")
    descriptor = None
    for klass in xygraph_XYGraphDescriptor.__mro__:
        if "showLegend" in klass.__dict__:
            descriptor = klass.__dict__["showLegend"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_xygraphdescriptor_has_showTitle():
    assert hasattr(xygraph_XYGraphDescriptor, "showTitle")
    descriptor = None
    for klass in xygraph_XYGraphDescriptor.__mro__:
        if "showTitle" in klass.__dict__:
            descriptor = klass.__dict__["showTitle"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_xygraphdescriptor_has_transparent():
    assert hasattr(xygraph_XYGraphDescriptor, "transparent")
    descriptor = None
    for klass in xygraph_XYGraphDescriptor.__mro__:
        if "transparent" in klass.__dict__:
            descriptor = klass.__dict__["transparent"]
            break
    assert isinstance(descriptor, property)

def test_xygraph_xygraphdescriptor_has_title():
    assert hasattr(xygraph_XYGraphDescriptor, "title")
    descriptor = None
    for klass in xygraph_XYGraphDescriptor.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_trace_baseline_exists():
    # Check that the Enumeration exists
    assert Trace_BaseLine is not None

def test_trace_baseline_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Trace_BaseLine]
    expected_literals = [
        "NEGATIVE_INFINITY",
        "POSITIVE_INFINITY",
        "ZERO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Trace_BaseLine"

def test_trace_tracetype_exists():
    # Check that the Enumeration exists
    assert Trace_TraceType is not None

def test_trace_tracetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Trace_TraceType]
    expected_literals = [
        "DASHDOT_LINE",
        "SOLID_LINE",
        "AREA",
        "POINT",
        "BAR",
        "DASH_LINE",
        "DOT_LINE",
        "LINE_AREA",
        "STEP_VERTICALLY",
        "DASHDOTDOT_LINE",
        "STEP_HORIZONTALLY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Trace_TraceType"

def test_zoomtype_exists():
    # Check that the Enumeration exists
    assert ZoomType is not None

def test_zoomtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ZoomType]
    expected_literals = [
        "VERTICAL_ZOOM",
        "ZOOM_IN_HORIZONTALLY",
        "ZOOM_OUT_VERTICALLY",
        "PANNING",
        "DYNAMIC_ZOOM",
        "RUBBERBAND_ZOOM",
        "ZOOM_OUT",
        "ZOOM_IN",
        "ZOOM_OUT_HORIZONTALLY",
        "HORIZONTAL_ZOOM",
        "ZOOM_IN_VERTICALLY",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ZoomType"

def test_linearscale_orientation_exists():
    # Check that the Enumeration exists
    assert LinearScale_Orientation is not None

def test_linearscale_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinearScale_Orientation]
    expected_literals = [
        "HORIZONTAL",
        "VERTICAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinearScale_Orientation"

def test_trace_errorbartype_exists():
    # Check that the Enumeration exists
    assert Trace_ErrorBarType is not None

def test_trace_errorbartype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Trace_ErrorBarType]
    expected_literals = [
        "PLUS",
        "NONE",
        "MINUS",
        "BOTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Trace_ErrorBarType"

def test_trace_pointstyle_exists():
    # Check that the Enumeration exists
    assert Trace_PointStyle is not None

def test_trace_pointstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Trace_PointStyle]
    expected_literals = [
        "NONE",
        "FILLED_SQUARE",
        "CIRCLE",
        "BAR",
        "SQUARE",
        "TRIANGLE",
        "POINT",
        "FILLED_TRIANGLE",
        "FILLED_DIAMOND",
        "XCROSS",
        "DIAMOND",
        "CROSS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Trace_PointStyle"


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
xygraph_EObject_strategy = st.builds(
    xygraph_EObject,
)
xygraph_FontDescriptor_strategy = st.builds(
    xygraph_FontDescriptor,
    style=
        st.integers(),
    size=
        st.integers(),
    name=
        safe_text
)
xygraph_TraceDescriptor_strategy = st.builds(
    xygraph_TraceDescriptor,
    yErrorBarType=
        safe_text,
    traceType=
        safe_text,
    areaAlpha=
        st.integers(),
    xErrorBarType=
        safe_text,
    baseLine=
        safe_text,
    errorBarEnabled=
        st.booleans(),
    lineWidth=
        st.integers(),
    errorBarCapWidth=
        st.integers(),
    name=
        safe_text,
    drawYErrorInArea=
        st.booleans(),
    pointSize=
        st.integers(),
    pointStyle=
        safe_text,
    antiAliasing=
        st.booleans()
)
xygraph_AxisDescriptor_strategy = st.builds(
    xygraph_AxisDescriptor,
    showMinorGrid=
        st.booleans(),
    showMajorGrid=
        st.booleans(),
    dashGridLine=
        st.booleans(),
    dateEnabled=
        st.booleans(),
    autoScaleThreshold=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    logScale=
        st.booleans(),
    title=
        safe_text,
    zoomType=
        safe_text,
    autoFormat=
        st.booleans(),
    formatPattern=
        safe_text,
    minorTicksVisible=
        st.booleans(),
    autoScale=
        st.booleans(),
    orientation=
        safe_text,
    primarySide=
        st.booleans(),
    rangeLower=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    rangeUpper=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
xygraph_ColorDescriptor_strategy = st.builds(
    xygraph_ColorDescriptor,
    g=
        st.integers(),
    b=
        st.integers(),
    r=
        st.integers()
)
xygraph_XYGraphDescriptor_strategy = st.builds(
    xygraph_XYGraphDescriptor,
    zoomType=
        safe_text,
    showPlotAreaBorder=
        st.booleans(),
    showLegend=
        st.booleans(),
    showTitle=
        st.booleans(),
    transparent=
        st.booleans(),
    title=
        safe_text
)

@given(instance=xygraph_EObject_strategy)
@settings(max_examples=50)
def test_xygraph_eobject_instantiation(instance):
    assert isinstance(instance, xygraph_EObject)

@given(instance=xygraph_FontDescriptor_strategy)
@settings(max_examples=50)
def test_xygraph_fontdescriptor_instantiation(instance):
    assert isinstance(instance, xygraph_FontDescriptor)



@given(instance=xygraph_FontDescriptor_strategy)
def test_xygraph_fontdescriptor_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xygraph_FontDescriptor_strategy)
def test_xygraph_fontdescriptor_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=xygraph_FontDescriptor_strategy)
def test_xygraph_fontdescriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xygraph_TraceDescriptor_strategy)
@settings(max_examples=50)
def test_xygraph_tracedescriptor_instantiation(instance):
    assert isinstance(instance, xygraph_TraceDescriptor)



@given(instance=xygraph_TraceDescriptor_strategy)
def test_xygraph_tracedescriptor_yErrorBarType_setter(instance):
    original = instance.yErrorBarType
    instance.yErrorBarType = original
    assert instance.yErrorBarType == original



@given(instance=xygraph_TraceDescriptor_strategy)
def test_xygraph_tracedescriptor_traceType_setter(instance):
    original = instance.traceType
    instance.traceType = original
    assert instance.traceType == original



@given(instance=xygraph_TraceDescriptor_strategy)
def test_xygraph_tracedescriptor_areaAlpha_setter(instance):
    original = instance.areaAlpha
    instance.areaAlpha = original
    assert instance.areaAlpha == original



@given(instance=xygraph_TraceDescriptor_strategy)
def test_xygraph_tracedescriptor_xErrorBarType_setter(instance):
    original = instance.xErrorBarType
    instance.xErrorBarType = original
    assert instance.xErrorBarType == original



@given(instance=xygraph_TraceDescriptor_strategy)
def test_xygraph_tracedescriptor_baseLine_setter(instance):
    original = instance.baseLine
    instance.baseLine = original
    assert instance.baseLine == original



@given(instance=xygraph_TraceDescriptor_strategy)
def test_xygraph_tracedescriptor_errorBarEnabled_setter(instance):
    original = instance.errorBarEnabled
    instance.errorBarEnabled = original
    assert instance.errorBarEnabled == original



@given(instance=xygraph_TraceDescriptor_strategy)
def test_xygraph_tracedescriptor_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original



@given(instance=xygraph_TraceDescriptor_strategy)
def test_xygraph_tracedescriptor_errorBarCapWidth_setter(instance):
    original = instance.errorBarCapWidth
    instance.errorBarCapWidth = original
    assert instance.errorBarCapWidth == original



@given(instance=xygraph_TraceDescriptor_strategy)
def test_xygraph_tracedescriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xygraph_TraceDescriptor_strategy)
def test_xygraph_tracedescriptor_drawYErrorInArea_setter(instance):
    original = instance.drawYErrorInArea
    instance.drawYErrorInArea = original
    assert instance.drawYErrorInArea == original



@given(instance=xygraph_TraceDescriptor_strategy)
def test_xygraph_tracedescriptor_pointSize_setter(instance):
    original = instance.pointSize
    instance.pointSize = original
    assert instance.pointSize == original



@given(instance=xygraph_TraceDescriptor_strategy)
def test_xygraph_tracedescriptor_pointStyle_setter(instance):
    original = instance.pointStyle
    instance.pointStyle = original
    assert instance.pointStyle == original



@given(instance=xygraph_TraceDescriptor_strategy)
def test_xygraph_tracedescriptor_antiAliasing_setter(instance):
    original = instance.antiAliasing
    instance.antiAliasing = original
    assert instance.antiAliasing == original

@given(instance=xygraph_AxisDescriptor_strategy)
@settings(max_examples=50)
def test_xygraph_axisdescriptor_instantiation(instance):
    assert isinstance(instance, xygraph_AxisDescriptor)



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_showMinorGrid_setter(instance):
    original = instance.showMinorGrid
    instance.showMinorGrid = original
    assert instance.showMinorGrid == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_showMajorGrid_setter(instance):
    original = instance.showMajorGrid
    instance.showMajorGrid = original
    assert instance.showMajorGrid == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_dashGridLine_setter(instance):
    original = instance.dashGridLine
    instance.dashGridLine = original
    assert instance.dashGridLine == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_dateEnabled_setter(instance):
    original = instance.dateEnabled
    instance.dateEnabled = original
    assert instance.dateEnabled == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_autoScaleThreshold_setter(instance):
    original = instance.autoScaleThreshold
    instance.autoScaleThreshold = original
    assert instance.autoScaleThreshold == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_logScale_setter(instance):
    original = instance.logScale
    instance.logScale = original
    assert instance.logScale == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_zoomType_setter(instance):
    original = instance.zoomType
    instance.zoomType = original
    assert instance.zoomType == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_autoFormat_setter(instance):
    original = instance.autoFormat
    instance.autoFormat = original
    assert instance.autoFormat == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_formatPattern_setter(instance):
    original = instance.formatPattern
    instance.formatPattern = original
    assert instance.formatPattern == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_minorTicksVisible_setter(instance):
    original = instance.minorTicksVisible
    instance.minorTicksVisible = original
    assert instance.minorTicksVisible == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_autoScale_setter(instance):
    original = instance.autoScale
    instance.autoScale = original
    assert instance.autoScale == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_primarySide_setter(instance):
    original = instance.primarySide
    instance.primarySide = original
    assert instance.primarySide == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_rangeLower_setter(instance):
    original = instance.rangeLower
    instance.rangeLower = original
    assert instance.rangeLower == original



@given(instance=xygraph_AxisDescriptor_strategy)
def test_xygraph_axisdescriptor_rangeUpper_setter(instance):
    original = instance.rangeUpper
    instance.rangeUpper = original
    assert instance.rangeUpper == original

@given(instance=xygraph_ColorDescriptor_strategy)
@settings(max_examples=50)
def test_xygraph_colordescriptor_instantiation(instance):
    assert isinstance(instance, xygraph_ColorDescriptor)



@given(instance=xygraph_ColorDescriptor_strategy)
def test_xygraph_colordescriptor_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original



@given(instance=xygraph_ColorDescriptor_strategy)
def test_xygraph_colordescriptor_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=xygraph_ColorDescriptor_strategy)
def test_xygraph_colordescriptor_r_setter(instance):
    original = instance.r
    instance.r = original
    assert instance.r == original

@given(instance=xygraph_XYGraphDescriptor_strategy)
@settings(max_examples=50)
def test_xygraph_xygraphdescriptor_instantiation(instance):
    assert isinstance(instance, xygraph_XYGraphDescriptor)



@given(instance=xygraph_XYGraphDescriptor_strategy)
def test_xygraph_xygraphdescriptor_zoomType_setter(instance):
    original = instance.zoomType
    instance.zoomType = original
    assert instance.zoomType == original



@given(instance=xygraph_XYGraphDescriptor_strategy)
def test_xygraph_xygraphdescriptor_showPlotAreaBorder_setter(instance):
    original = instance.showPlotAreaBorder
    instance.showPlotAreaBorder = original
    assert instance.showPlotAreaBorder == original



@given(instance=xygraph_XYGraphDescriptor_strategy)
def test_xygraph_xygraphdescriptor_showLegend_setter(instance):
    original = instance.showLegend
    instance.showLegend = original
    assert instance.showLegend == original



@given(instance=xygraph_XYGraphDescriptor_strategy)
def test_xygraph_xygraphdescriptor_showTitle_setter(instance):
    original = instance.showTitle
    instance.showTitle = original
    assert instance.showTitle == original



@given(instance=xygraph_XYGraphDescriptor_strategy)
def test_xygraph_xygraphdescriptor_transparent_setter(instance):
    original = instance.transparent
    instance.transparent = original
    assert instance.transparent == original



@given(instance=xygraph_XYGraphDescriptor_strategy)
def test_xygraph_xygraphdescriptor_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
