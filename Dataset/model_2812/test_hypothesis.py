import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    xygraph::EObject,
    xygraph::FontDescriptor,
    xygraph::TraceDescriptor,
    xygraph::AxisDescriptor,
    xygraph::ColorDescriptor,
    xygraph::XYGraphDescriptor,
    Trace_ErrorBarType,
    ZoomType,
    Trace_TraceType,
    Trace_BaseLine,
    Trace_PointStyle,
    LinearScale_Orientation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xygraph::eobject_is_not_abstract():
    assert not inspect.isabstract(xygraph::EObject)


def test_xygraph::eobject_constructor_exists():
    assert callable(xygraph::EObject.__init__)


def test_xygraph::eobject_constructor_args():
    sig = inspect.signature(xygraph::EObject.__init__)
    params = list(sig.parameters.keys())



def test_xygraph::fontdescriptor_is_not_abstract():
    assert not inspect.isabstract(xygraph::FontDescriptor)


def test_xygraph::fontdescriptor_constructor_exists():
    assert callable(xygraph::FontDescriptor.__init__)


def test_xygraph::fontdescriptor_constructor_args():
    sig = inspect.signature(xygraph::FontDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "size" in params, "Missing parameter 'size'"
    assert "style" in params, "Missing parameter 'style'"

def test_xygraph::fontdescriptor_has_name():
    assert hasattr(xygraph::FontDescriptor, "name")
    descriptor = None
    for klass in xygraph::FontDescriptor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::fontdescriptor_has_size():
    assert hasattr(xygraph::FontDescriptor, "size")
    descriptor = None
    for klass in xygraph::FontDescriptor.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::fontdescriptor_has_style():
    assert hasattr(xygraph::FontDescriptor, "style")
    descriptor = None
    for klass in xygraph::FontDescriptor.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xygraph::tracedescriptor_is_not_abstract():
    assert not inspect.isabstract(xygraph::TraceDescriptor)


def test_xygraph::tracedescriptor_constructor_exists():
    assert callable(xygraph::TraceDescriptor.__init__)


def test_xygraph::tracedescriptor_constructor_args():
    sig = inspect.signature(xygraph::TraceDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "errorBarEnabled" in params, "Missing parameter 'errorBarEnabled'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "name" in params, "Missing parameter 'name'"
    assert "errorBarCapWidth" in params, "Missing parameter 'errorBarCapWidth'"
    assert "baseLine" in params, "Missing parameter 'baseLine'"
    assert "pointSize" in params, "Missing parameter 'pointSize'"
    assert "areaAlpha" in params, "Missing parameter 'areaAlpha'"
    assert "traceType" in params, "Missing parameter 'traceType'"
    assert "antiAliasing" in params, "Missing parameter 'antiAliasing'"
    assert "drawYErrorInArea" in params, "Missing parameter 'drawYErrorInArea'"
    assert "yErrorBarType" in params, "Missing parameter 'yErrorBarType'"
    assert "xErrorBarType" in params, "Missing parameter 'xErrorBarType'"
    assert "pointStyle" in params, "Missing parameter 'pointStyle'"

def test_xygraph::tracedescriptor_has_errorBarEnabled():
    assert hasattr(xygraph::TraceDescriptor, "errorBarEnabled")
    descriptor = None
    for klass in xygraph::TraceDescriptor.__mro__:
        if "errorBarEnabled" in klass.__dict__:
            descriptor = klass.__dict__["errorBarEnabled"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::tracedescriptor_has_lineWidth():
    assert hasattr(xygraph::TraceDescriptor, "lineWidth")
    descriptor = None
    for klass in xygraph::TraceDescriptor.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::tracedescriptor_has_name():
    assert hasattr(xygraph::TraceDescriptor, "name")
    descriptor = None
    for klass in xygraph::TraceDescriptor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::tracedescriptor_has_errorBarCapWidth():
    assert hasattr(xygraph::TraceDescriptor, "errorBarCapWidth")
    descriptor = None
    for klass in xygraph::TraceDescriptor.__mro__:
        if "errorBarCapWidth" in klass.__dict__:
            descriptor = klass.__dict__["errorBarCapWidth"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::tracedescriptor_has_baseLine():
    assert hasattr(xygraph::TraceDescriptor, "baseLine")
    descriptor = None
    for klass in xygraph::TraceDescriptor.__mro__:
        if "baseLine" in klass.__dict__:
            descriptor = klass.__dict__["baseLine"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::tracedescriptor_has_pointSize():
    assert hasattr(xygraph::TraceDescriptor, "pointSize")
    descriptor = None
    for klass in xygraph::TraceDescriptor.__mro__:
        if "pointSize" in klass.__dict__:
            descriptor = klass.__dict__["pointSize"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::tracedescriptor_has_areaAlpha():
    assert hasattr(xygraph::TraceDescriptor, "areaAlpha")
    descriptor = None
    for klass in xygraph::TraceDescriptor.__mro__:
        if "areaAlpha" in klass.__dict__:
            descriptor = klass.__dict__["areaAlpha"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::tracedescriptor_has_traceType():
    assert hasattr(xygraph::TraceDescriptor, "traceType")
    descriptor = None
    for klass in xygraph::TraceDescriptor.__mro__:
        if "traceType" in klass.__dict__:
            descriptor = klass.__dict__["traceType"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::tracedescriptor_has_antiAliasing():
    assert hasattr(xygraph::TraceDescriptor, "antiAliasing")
    descriptor = None
    for klass in xygraph::TraceDescriptor.__mro__:
        if "antiAliasing" in klass.__dict__:
            descriptor = klass.__dict__["antiAliasing"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::tracedescriptor_has_drawYErrorInArea():
    assert hasattr(xygraph::TraceDescriptor, "drawYErrorInArea")
    descriptor = None
    for klass in xygraph::TraceDescriptor.__mro__:
        if "drawYErrorInArea" in klass.__dict__:
            descriptor = klass.__dict__["drawYErrorInArea"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::tracedescriptor_has_yErrorBarType():
    assert hasattr(xygraph::TraceDescriptor, "yErrorBarType")
    descriptor = None
    for klass in xygraph::TraceDescriptor.__mro__:
        if "yErrorBarType" in klass.__dict__:
            descriptor = klass.__dict__["yErrorBarType"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::tracedescriptor_has_xErrorBarType():
    assert hasattr(xygraph::TraceDescriptor, "xErrorBarType")
    descriptor = None
    for klass in xygraph::TraceDescriptor.__mro__:
        if "xErrorBarType" in klass.__dict__:
            descriptor = klass.__dict__["xErrorBarType"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::tracedescriptor_has_pointStyle():
    assert hasattr(xygraph::TraceDescriptor, "pointStyle")
    descriptor = None
    for klass in xygraph::TraceDescriptor.__mro__:
        if "pointStyle" in klass.__dict__:
            descriptor = klass.__dict__["pointStyle"]
            break
    assert isinstance(descriptor, property)



def test_xygraph::axisdescriptor_is_not_abstract():
    assert not inspect.isabstract(xygraph::AxisDescriptor)


def test_xygraph::axisdescriptor_constructor_exists():
    assert callable(xygraph::AxisDescriptor.__init__)


def test_xygraph::axisdescriptor_constructor_args():
    sig = inspect.signature(xygraph::AxisDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "formatPattern" in params, "Missing parameter 'formatPattern'"
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "title" in params, "Missing parameter 'title'"
    assert "showMinorGrid" in params, "Missing parameter 'showMinorGrid'"
    assert "autoFormat" in params, "Missing parameter 'autoFormat'"
    assert "rangeLower" in params, "Missing parameter 'rangeLower'"
    assert "dashGridLine" in params, "Missing parameter 'dashGridLine'"
    assert "minorTicksVisible" in params, "Missing parameter 'minorTicksVisible'"
    assert "zoomType" in params, "Missing parameter 'zoomType'"
    assert "autoScale" in params, "Missing parameter 'autoScale'"
    assert "autoScaleThreshold" in params, "Missing parameter 'autoScaleThreshold'"
    assert "rangeUpper" in params, "Missing parameter 'rangeUpper'"
    assert "showMajorGrid" in params, "Missing parameter 'showMajorGrid'"
    assert "dateEnabled" in params, "Missing parameter 'dateEnabled'"
    assert "primarySide" in params, "Missing parameter 'primarySide'"
    assert "logScale" in params, "Missing parameter 'logScale'"

def test_xygraph::axisdescriptor_has_formatPattern():
    assert hasattr(xygraph::AxisDescriptor, "formatPattern")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "formatPattern" in klass.__dict__:
            descriptor = klass.__dict__["formatPattern"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_orientation():
    assert hasattr(xygraph::AxisDescriptor, "orientation")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_title():
    assert hasattr(xygraph::AxisDescriptor, "title")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_showMinorGrid():
    assert hasattr(xygraph::AxisDescriptor, "showMinorGrid")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "showMinorGrid" in klass.__dict__:
            descriptor = klass.__dict__["showMinorGrid"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_autoFormat():
    assert hasattr(xygraph::AxisDescriptor, "autoFormat")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "autoFormat" in klass.__dict__:
            descriptor = klass.__dict__["autoFormat"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_rangeLower():
    assert hasattr(xygraph::AxisDescriptor, "rangeLower")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "rangeLower" in klass.__dict__:
            descriptor = klass.__dict__["rangeLower"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_dashGridLine():
    assert hasattr(xygraph::AxisDescriptor, "dashGridLine")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "dashGridLine" in klass.__dict__:
            descriptor = klass.__dict__["dashGridLine"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_minorTicksVisible():
    assert hasattr(xygraph::AxisDescriptor, "minorTicksVisible")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "minorTicksVisible" in klass.__dict__:
            descriptor = klass.__dict__["minorTicksVisible"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_zoomType():
    assert hasattr(xygraph::AxisDescriptor, "zoomType")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "zoomType" in klass.__dict__:
            descriptor = klass.__dict__["zoomType"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_autoScale():
    assert hasattr(xygraph::AxisDescriptor, "autoScale")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "autoScale" in klass.__dict__:
            descriptor = klass.__dict__["autoScale"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_autoScaleThreshold():
    assert hasattr(xygraph::AxisDescriptor, "autoScaleThreshold")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "autoScaleThreshold" in klass.__dict__:
            descriptor = klass.__dict__["autoScaleThreshold"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_rangeUpper():
    assert hasattr(xygraph::AxisDescriptor, "rangeUpper")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "rangeUpper" in klass.__dict__:
            descriptor = klass.__dict__["rangeUpper"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_showMajorGrid():
    assert hasattr(xygraph::AxisDescriptor, "showMajorGrid")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "showMajorGrid" in klass.__dict__:
            descriptor = klass.__dict__["showMajorGrid"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_dateEnabled():
    assert hasattr(xygraph::AxisDescriptor, "dateEnabled")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "dateEnabled" in klass.__dict__:
            descriptor = klass.__dict__["dateEnabled"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_primarySide():
    assert hasattr(xygraph::AxisDescriptor, "primarySide")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "primarySide" in klass.__dict__:
            descriptor = klass.__dict__["primarySide"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::axisdescriptor_has_logScale():
    assert hasattr(xygraph::AxisDescriptor, "logScale")
    descriptor = None
    for klass in xygraph::AxisDescriptor.__mro__:
        if "logScale" in klass.__dict__:
            descriptor = klass.__dict__["logScale"]
            break
    assert isinstance(descriptor, property)



def test_xygraph::colordescriptor_is_not_abstract():
    assert not inspect.isabstract(xygraph::ColorDescriptor)


def test_xygraph::colordescriptor_constructor_exists():
    assert callable(xygraph::ColorDescriptor.__init__)


def test_xygraph::colordescriptor_constructor_args():
    sig = inspect.signature(xygraph::ColorDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "r" in params, "Missing parameter 'r'"
    assert "g" in params, "Missing parameter 'g'"
    assert "b" in params, "Missing parameter 'b'"

def test_xygraph::colordescriptor_has_r():
    assert hasattr(xygraph::ColorDescriptor, "r")
    descriptor = None
    for klass in xygraph::ColorDescriptor.__mro__:
        if "r" in klass.__dict__:
            descriptor = klass.__dict__["r"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::colordescriptor_has_g():
    assert hasattr(xygraph::ColorDescriptor, "g")
    descriptor = None
    for klass in xygraph::ColorDescriptor.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::colordescriptor_has_b():
    assert hasattr(xygraph::ColorDescriptor, "b")
    descriptor = None
    for klass in xygraph::ColorDescriptor.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_xygraph::xygraphdescriptor_is_not_abstract():
    assert not inspect.isabstract(xygraph::XYGraphDescriptor)


def test_xygraph::xygraphdescriptor_constructor_exists():
    assert callable(xygraph::XYGraphDescriptor.__init__)


def test_xygraph::xygraphdescriptor_constructor_args():
    sig = inspect.signature(xygraph::XYGraphDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "showPlotAreaBorder" in params, "Missing parameter 'showPlotAreaBorder'"
    assert "zoomType" in params, "Missing parameter 'zoomType'"
    assert "transparent" in params, "Missing parameter 'transparent'"
    assert "title" in params, "Missing parameter 'title'"
    assert "showTitle" in params, "Missing parameter 'showTitle'"
    assert "showLegend" in params, "Missing parameter 'showLegend'"

def test_xygraph::xygraphdescriptor_has_showPlotAreaBorder():
    assert hasattr(xygraph::XYGraphDescriptor, "showPlotAreaBorder")
    descriptor = None
    for klass in xygraph::XYGraphDescriptor.__mro__:
        if "showPlotAreaBorder" in klass.__dict__:
            descriptor = klass.__dict__["showPlotAreaBorder"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::xygraphdescriptor_has_zoomType():
    assert hasattr(xygraph::XYGraphDescriptor, "zoomType")
    descriptor = None
    for klass in xygraph::XYGraphDescriptor.__mro__:
        if "zoomType" in klass.__dict__:
            descriptor = klass.__dict__["zoomType"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::xygraphdescriptor_has_transparent():
    assert hasattr(xygraph::XYGraphDescriptor, "transparent")
    descriptor = None
    for klass in xygraph::XYGraphDescriptor.__mro__:
        if "transparent" in klass.__dict__:
            descriptor = klass.__dict__["transparent"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::xygraphdescriptor_has_title():
    assert hasattr(xygraph::XYGraphDescriptor, "title")
    descriptor = None
    for klass in xygraph::XYGraphDescriptor.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::xygraphdescriptor_has_showTitle():
    assert hasattr(xygraph::XYGraphDescriptor, "showTitle")
    descriptor = None
    for klass in xygraph::XYGraphDescriptor.__mro__:
        if "showTitle" in klass.__dict__:
            descriptor = klass.__dict__["showTitle"]
            break
    assert isinstance(descriptor, property)

def test_xygraph::xygraphdescriptor_has_showLegend():
    assert hasattr(xygraph::XYGraphDescriptor, "showLegend")
    descriptor = None
    for klass in xygraph::XYGraphDescriptor.__mro__:
        if "showLegend" in klass.__dict__:
            descriptor = klass.__dict__["showLegend"]
            break
    assert isinstance(descriptor, property)

def test_trace_errorbartype_exists():
    # Check that the Enumeration exists
    assert Trace_ErrorBarType is not None

def test_trace_errorbartype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Trace_ErrorBarType]
    expected_literals = [
        "NONE",
        "MINUS",
        "BOTH",
        "PLUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Trace_ErrorBarType"

def test_zoomtype_exists():
    # Check that the Enumeration exists
    assert ZoomType is not None

def test_zoomtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ZoomType]
    expected_literals = [
        "NONE",
        "DYNAMIC_ZOOM",
        "ZOOM_IN_VERTICALLY",
        "ZOOM_OUT_HORIZONTALLY",
        "RUBBERBAND_ZOOM",
        "ZOOM_IN",
        "PANNING",
        "HORIZONTAL_ZOOM",
        "ZOOM_OUT",
        "ZOOM_OUT_VERTICALLY",
        "VERTICAL_ZOOM",
        "ZOOM_IN_HORIZONTALLY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ZoomType"

def test_trace_tracetype_exists():
    # Check that the Enumeration exists
    assert Trace_TraceType is not None

def test_trace_tracetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Trace_TraceType]
    expected_literals = [
        "STEP_HORIZONTALLY",
        "DASH_LINE",
        "STEP_VERTICALLY",
        "DOT_LINE",
        "SOLID_LINE",
        "DASHDOT_LINE",
        "POINT",
        "AREA",
        "LINE_AREA",
        "DASHDOTDOT_LINE",
        "BAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Trace_TraceType"

def test_trace_baseline_exists():
    # Check that the Enumeration exists
    assert Trace_BaseLine is not None

def test_trace_baseline_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Trace_BaseLine]
    expected_literals = [
        "ZERO",
        "POSITIVE_INFINITY",
        "NEGATIVE_INFINITY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Trace_BaseLine"

def test_trace_pointstyle_exists():
    # Check that the Enumeration exists
    assert Trace_PointStyle is not None

def test_trace_pointstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Trace_PointStyle]
    expected_literals = [
        "POINT",
        "DIAMOND",
        "FILLED_SQUARE",
        "XCROSS",
        "CIRCLE",
        "TRIANGLE",
        "CROSS",
        "FILLED_TRIANGLE",
        "BAR",
        "SQUARE",
        "FILLED_DIAMOND",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Trace_PointStyle"

def test_linearscale_orientation_exists():
    # Check that the Enumeration exists
    assert LinearScale_Orientation is not None

def test_linearscale_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinearScale_Orientation]
    expected_literals = [
        "VERTICAL",
        "HORIZONTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinearScale_Orientation"


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
xygraph::EObject_strategy = st.builds(
    xygraph::EObject,
)
xygraph::FontDescriptor_strategy = st.builds(
    xygraph::FontDescriptor,
    name=
        safe_text,
    size=
        st.integers(),
    style=
        st.integers()
)
xygraph::TraceDescriptor_strategy = st.builds(
    xygraph::TraceDescriptor,
    errorBarEnabled=
        st.booleans(),
    lineWidth=
        st.integers(),
    name=
        safe_text,
    errorBarCapWidth=
        st.integers(),
    baseLine=
        safe_text,
    pointSize=
        st.integers(),
    areaAlpha=
        st.integers(),
    traceType=
        safe_text,
    antiAliasing=
        st.booleans(),
    drawYErrorInArea=
        st.booleans(),
    yErrorBarType=
        safe_text,
    xErrorBarType=
        safe_text,
    pointStyle=
        safe_text
)
xygraph::AxisDescriptor_strategy = st.builds(
    xygraph::AxisDescriptor,
    formatPattern=
        safe_text,
    orientation=
        safe_text,
    title=
        safe_text,
    showMinorGrid=
        st.booleans(),
    autoFormat=
        st.booleans(),
    rangeLower=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    dashGridLine=
        st.booleans(),
    minorTicksVisible=
        st.booleans(),
    zoomType=
        safe_text,
    autoScale=
        st.booleans(),
    autoScaleThreshold=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    rangeUpper=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    showMajorGrid=
        st.booleans(),
    dateEnabled=
        st.booleans(),
    primarySide=
        st.booleans(),
    logScale=
        st.booleans()
)
xygraph::ColorDescriptor_strategy = st.builds(
    xygraph::ColorDescriptor,
    r=
        st.integers(),
    g=
        st.integers(),
    b=
        st.integers()
)
xygraph::XYGraphDescriptor_strategy = st.builds(
    xygraph::XYGraphDescriptor,
    showPlotAreaBorder=
        st.booleans(),
    zoomType=
        safe_text,
    transparent=
        st.booleans(),
    title=
        safe_text,
    showTitle=
        st.booleans(),
    showLegend=
        st.booleans()
)

@given(instance=xygraph::EObject_strategy)
@settings(max_examples=50)
def test_xygraph::eobject_instantiation(instance):
    assert isinstance(instance, xygraph::EObject)

@given(instance=xygraph::FontDescriptor_strategy)
@settings(max_examples=50)
def test_xygraph::fontdescriptor_instantiation(instance):
    assert isinstance(instance, xygraph::FontDescriptor)

@given(instance=xygraph::FontDescriptor_strategy)
def test_xygraph::fontdescriptor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xygraph::FontDescriptor_strategy)
def test_xygraph::fontdescriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xygraph::FontDescriptor_strategy)
def test_xygraph::fontdescriptor_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=xygraph::FontDescriptor_strategy)
def test_xygraph::fontdescriptor_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=xygraph::FontDescriptor_strategy)
def test_xygraph::fontdescriptor_style_type(instance):
    assert isinstance(instance.style, int)


@given(instance=xygraph::FontDescriptor_strategy)
def test_xygraph::fontdescriptor_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xygraph::TraceDescriptor_strategy)
@settings(max_examples=50)
def test_xygraph::tracedescriptor_instantiation(instance):
    assert isinstance(instance, xygraph::TraceDescriptor)

@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_errorBarEnabled_type(instance):
    assert isinstance(instance.errorBarEnabled, bool)


@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_errorBarEnabled_setter(instance):
    original = instance.errorBarEnabled
    instance.errorBarEnabled = original
    assert instance.errorBarEnabled == original

@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_lineWidth_type(instance):
    assert isinstance(instance.lineWidth, int)


@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_errorBarCapWidth_type(instance):
    assert isinstance(instance.errorBarCapWidth, int)


@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_errorBarCapWidth_setter(instance):
    original = instance.errorBarCapWidth
    instance.errorBarCapWidth = original
    assert instance.errorBarCapWidth == original

@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_baseLine_type(instance):
    assert isinstance(instance.baseLine, str)


@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_baseLine_setter(instance):
    original = instance.baseLine
    instance.baseLine = original
    assert instance.baseLine == original

@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_pointSize_type(instance):
    assert isinstance(instance.pointSize, int)


@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_pointSize_setter(instance):
    original = instance.pointSize
    instance.pointSize = original
    assert instance.pointSize == original

@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_areaAlpha_type(instance):
    assert isinstance(instance.areaAlpha, int)


@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_areaAlpha_setter(instance):
    original = instance.areaAlpha
    instance.areaAlpha = original
    assert instance.areaAlpha == original

@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_traceType_type(instance):
    assert isinstance(instance.traceType, str)


@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_traceType_setter(instance):
    original = instance.traceType
    instance.traceType = original
    assert instance.traceType == original

@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_antiAliasing_type(instance):
    assert isinstance(instance.antiAliasing, bool)


@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_antiAliasing_setter(instance):
    original = instance.antiAliasing
    instance.antiAliasing = original
    assert instance.antiAliasing == original

@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_drawYErrorInArea_type(instance):
    assert isinstance(instance.drawYErrorInArea, bool)


@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_drawYErrorInArea_setter(instance):
    original = instance.drawYErrorInArea
    instance.drawYErrorInArea = original
    assert instance.drawYErrorInArea == original

@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_yErrorBarType_type(instance):
    assert isinstance(instance.yErrorBarType, str)


@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_yErrorBarType_setter(instance):
    original = instance.yErrorBarType
    instance.yErrorBarType = original
    assert instance.yErrorBarType == original

@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_xErrorBarType_type(instance):
    assert isinstance(instance.xErrorBarType, str)


@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_xErrorBarType_setter(instance):
    original = instance.xErrorBarType
    instance.xErrorBarType = original
    assert instance.xErrorBarType == original

@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_pointStyle_type(instance):
    assert isinstance(instance.pointStyle, str)


@given(instance=xygraph::TraceDescriptor_strategy)
def test_xygraph::tracedescriptor_pointStyle_setter(instance):
    original = instance.pointStyle
    instance.pointStyle = original
    assert instance.pointStyle == original

@given(instance=xygraph::AxisDescriptor_strategy)
@settings(max_examples=50)
def test_xygraph::axisdescriptor_instantiation(instance):
    assert isinstance(instance, xygraph::AxisDescriptor)

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_formatPattern_type(instance):
    assert isinstance(instance.formatPattern, str)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_formatPattern_setter(instance):
    original = instance.formatPattern
    instance.formatPattern = original
    assert instance.formatPattern == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_showMinorGrid_type(instance):
    assert isinstance(instance.showMinorGrid, bool)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_showMinorGrid_setter(instance):
    original = instance.showMinorGrid
    instance.showMinorGrid = original
    assert instance.showMinorGrid == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_autoFormat_type(instance):
    assert isinstance(instance.autoFormat, bool)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_autoFormat_setter(instance):
    original = instance.autoFormat
    instance.autoFormat = original
    assert instance.autoFormat == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_rangeLower_type(instance):
    assert isinstance(instance.rangeLower, float)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_rangeLower_setter(instance):
    original = instance.rangeLower
    instance.rangeLower = original
    assert instance.rangeLower == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_dashGridLine_type(instance):
    assert isinstance(instance.dashGridLine, bool)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_dashGridLine_setter(instance):
    original = instance.dashGridLine
    instance.dashGridLine = original
    assert instance.dashGridLine == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_minorTicksVisible_type(instance):
    assert isinstance(instance.minorTicksVisible, bool)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_minorTicksVisible_setter(instance):
    original = instance.minorTicksVisible
    instance.minorTicksVisible = original
    assert instance.minorTicksVisible == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_zoomType_type(instance):
    assert isinstance(instance.zoomType, str)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_zoomType_setter(instance):
    original = instance.zoomType
    instance.zoomType = original
    assert instance.zoomType == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_autoScale_type(instance):
    assert isinstance(instance.autoScale, bool)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_autoScale_setter(instance):
    original = instance.autoScale
    instance.autoScale = original
    assert instance.autoScale == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_autoScaleThreshold_type(instance):
    assert isinstance(instance.autoScaleThreshold, float)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_autoScaleThreshold_setter(instance):
    original = instance.autoScaleThreshold
    instance.autoScaleThreshold = original
    assert instance.autoScaleThreshold == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_rangeUpper_type(instance):
    assert isinstance(instance.rangeUpper, float)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_rangeUpper_setter(instance):
    original = instance.rangeUpper
    instance.rangeUpper = original
    assert instance.rangeUpper == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_showMajorGrid_type(instance):
    assert isinstance(instance.showMajorGrid, bool)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_showMajorGrid_setter(instance):
    original = instance.showMajorGrid
    instance.showMajorGrid = original
    assert instance.showMajorGrid == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_dateEnabled_type(instance):
    assert isinstance(instance.dateEnabled, bool)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_dateEnabled_setter(instance):
    original = instance.dateEnabled
    instance.dateEnabled = original
    assert instance.dateEnabled == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_primarySide_type(instance):
    assert isinstance(instance.primarySide, bool)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_primarySide_setter(instance):
    original = instance.primarySide
    instance.primarySide = original
    assert instance.primarySide == original

@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_logScale_type(instance):
    assert isinstance(instance.logScale, bool)


@given(instance=xygraph::AxisDescriptor_strategy)
def test_xygraph::axisdescriptor_logScale_setter(instance):
    original = instance.logScale
    instance.logScale = original
    assert instance.logScale == original

@given(instance=xygraph::ColorDescriptor_strategy)
@settings(max_examples=50)
def test_xygraph::colordescriptor_instantiation(instance):
    assert isinstance(instance, xygraph::ColorDescriptor)

@given(instance=xygraph::ColorDescriptor_strategy)
def test_xygraph::colordescriptor_r_type(instance):
    assert isinstance(instance.r, int)


@given(instance=xygraph::ColorDescriptor_strategy)
def test_xygraph::colordescriptor_r_setter(instance):
    original = instance.r
    instance.r = original
    assert instance.r == original

@given(instance=xygraph::ColorDescriptor_strategy)
def test_xygraph::colordescriptor_g_type(instance):
    assert isinstance(instance.g, int)


@given(instance=xygraph::ColorDescriptor_strategy)
def test_xygraph::colordescriptor_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original

@given(instance=xygraph::ColorDescriptor_strategy)
def test_xygraph::colordescriptor_b_type(instance):
    assert isinstance(instance.b, int)


@given(instance=xygraph::ColorDescriptor_strategy)
def test_xygraph::colordescriptor_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=xygraph::XYGraphDescriptor_strategy)
@settings(max_examples=50)
def test_xygraph::xygraphdescriptor_instantiation(instance):
    assert isinstance(instance, xygraph::XYGraphDescriptor)

@given(instance=xygraph::XYGraphDescriptor_strategy)
def test_xygraph::xygraphdescriptor_showPlotAreaBorder_type(instance):
    assert isinstance(instance.showPlotAreaBorder, bool)


@given(instance=xygraph::XYGraphDescriptor_strategy)
def test_xygraph::xygraphdescriptor_showPlotAreaBorder_setter(instance):
    original = instance.showPlotAreaBorder
    instance.showPlotAreaBorder = original
    assert instance.showPlotAreaBorder == original

@given(instance=xygraph::XYGraphDescriptor_strategy)
def test_xygraph::xygraphdescriptor_zoomType_type(instance):
    assert isinstance(instance.zoomType, str)


@given(instance=xygraph::XYGraphDescriptor_strategy)
def test_xygraph::xygraphdescriptor_zoomType_setter(instance):
    original = instance.zoomType
    instance.zoomType = original
    assert instance.zoomType == original

@given(instance=xygraph::XYGraphDescriptor_strategy)
def test_xygraph::xygraphdescriptor_transparent_type(instance):
    assert isinstance(instance.transparent, bool)


@given(instance=xygraph::XYGraphDescriptor_strategy)
def test_xygraph::xygraphdescriptor_transparent_setter(instance):
    original = instance.transparent
    instance.transparent = original
    assert instance.transparent == original

@given(instance=xygraph::XYGraphDescriptor_strategy)
def test_xygraph::xygraphdescriptor_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xygraph::XYGraphDescriptor_strategy)
def test_xygraph::xygraphdescriptor_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xygraph::XYGraphDescriptor_strategy)
def test_xygraph::xygraphdescriptor_showTitle_type(instance):
    assert isinstance(instance.showTitle, bool)


@given(instance=xygraph::XYGraphDescriptor_strategy)
def test_xygraph::xygraphdescriptor_showTitle_setter(instance):
    original = instance.showTitle
    instance.showTitle = original
    assert instance.showTitle == original

@given(instance=xygraph::XYGraphDescriptor_strategy)
def test_xygraph::xygraphdescriptor_showLegend_type(instance):
    assert isinstance(instance.showLegend, bool)


@given(instance=xygraph::XYGraphDescriptor_strategy)
def test_xygraph::xygraphdescriptor_showLegend_setter(instance):
    original = instance.showLegend
    instance.showLegend = original
    assert instance.showLegend == original
