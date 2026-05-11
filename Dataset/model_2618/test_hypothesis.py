import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DNodeEdgeStyle,
    diastyle::DEdgeStyle,
    diastyle::DNodeStyle,
    diastyle::DGraphElement,
    diastyle::DStyleBridge,
    diastyle::DGraph,
    diastyle::DBaseStyle,
    DBaseStyle,
    diastyle::DNestingEdgeStyle,
    EModelElement,
    diastyle::DStyle,
    diastyle::DNodeEdgeStyle,
    DDirection,
    DShape,
    DAlignment,
    DLayout,
    DColor,
    DFontStyle,
    DLine,
    DFontName,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dnodeedgestyle_is_not_abstract():
    assert not inspect.isabstract(DNodeEdgeStyle)


def test_dnodeedgestyle_constructor_exists():
    assert callable(DNodeEdgeStyle.__init__)


def test_dnodeedgestyle_constructor_args():
    sig = inspect.signature(DNodeEdgeStyle.__init__)
    params = list(sig.parameters.keys())



def test_diastyle::dedgestyle_is_not_abstract():
    assert not inspect.isabstract(diastyle::DEdgeStyle)


def test_diastyle::dedgestyle_constructor_exists():
    assert callable(diastyle::DEdgeStyle.__init__)


def test_diastyle::dedgestyle_constructor_args():
    sig = inspect.signature(diastyle::DEdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "arrowDirection" in params, "Missing parameter 'arrowDirection'"
    assert "arrowSize" in params, "Missing parameter 'arrowSize'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_diastyle::dedgestyle_has_arrowDirection():
    assert hasattr(diastyle::DEdgeStyle, "arrowDirection")
    descriptor = None
    for klass in diastyle::DEdgeStyle.__mro__:
        if "arrowDirection" in klass.__dict__:
            descriptor = klass.__dict__["arrowDirection"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dedgestyle_has_arrowSize():
    assert hasattr(diastyle::DEdgeStyle, "arrowSize")
    descriptor = None
    for klass in diastyle::DEdgeStyle.__mro__:
        if "arrowSize" in klass.__dict__:
            descriptor = klass.__dict__["arrowSize"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dedgestyle_has_shape():
    assert hasattr(diastyle::DEdgeStyle, "shape")
    descriptor = None
    for klass in diastyle::DEdgeStyle.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_diastyle::dnodestyle_is_not_abstract():
    assert not inspect.isabstract(diastyle::DNodeStyle)


def test_diastyle::dnodestyle_constructor_exists():
    assert callable(diastyle::DNodeStyle.__init__)


def test_diastyle::dnodestyle_constructor_args():
    sig = inspect.signature(diastyle::DNodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "figure" in params, "Missing parameter 'figure'"
    assert "layout" in params, "Missing parameter 'layout'"
    assert "shape" in params, "Missing parameter 'shape'"
    assert "shapeData" in params, "Missing parameter 'shapeData'"
    assert "sizeX" in params, "Missing parameter 'sizeX'"
    assert "radius" in params, "Missing parameter 'radius'"
    assert "sizeY" in params, "Missing parameter 'sizeY'"

def test_diastyle::dnodestyle_has_figure():
    assert hasattr(diastyle::DNodeStyle, "figure")
    descriptor = None
    for klass in diastyle::DNodeStyle.__mro__:
        if "figure" in klass.__dict__:
            descriptor = klass.__dict__["figure"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dnodestyle_has_layout():
    assert hasattr(diastyle::DNodeStyle, "layout")
    descriptor = None
    for klass in diastyle::DNodeStyle.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dnodestyle_has_shape():
    assert hasattr(diastyle::DNodeStyle, "shape")
    descriptor = None
    for klass in diastyle::DNodeStyle.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dnodestyle_has_shapeData():
    assert hasattr(diastyle::DNodeStyle, "shapeData")
    descriptor = None
    for klass in diastyle::DNodeStyle.__mro__:
        if "shapeData" in klass.__dict__:
            descriptor = klass.__dict__["shapeData"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dnodestyle_has_sizeX():
    assert hasattr(diastyle::DNodeStyle, "sizeX")
    descriptor = None
    for klass in diastyle::DNodeStyle.__mro__:
        if "sizeX" in klass.__dict__:
            descriptor = klass.__dict__["sizeX"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dnodestyle_has_radius():
    assert hasattr(diastyle::DNodeStyle, "radius")
    descriptor = None
    for klass in diastyle::DNodeStyle.__mro__:
        if "radius" in klass.__dict__:
            descriptor = klass.__dict__["radius"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dnodestyle_has_sizeY():
    assert hasattr(diastyle::DNodeStyle, "sizeY")
    descriptor = None
    for klass in diastyle::DNodeStyle.__mro__:
        if "sizeY" in klass.__dict__:
            descriptor = klass.__dict__["sizeY"]
            break
    assert isinstance(descriptor, property)



def test_diastyle::dgraphelement_is_not_abstract():
    assert not inspect.isabstract(diastyle::DGraphElement)


def test_diastyle::dgraphelement_constructor_exists():
    assert callable(diastyle::DGraphElement.__init__)


def test_diastyle::dgraphelement_constructor_args():
    sig = inspect.signature(diastyle::DGraphElement.__init__)
    params = list(sig.parameters.keys())



def test_diastyle::dstylebridge_is_not_abstract():
    assert not inspect.isabstract(diastyle::DStyleBridge)


def test_diastyle::dstylebridge_constructor_exists():
    assert callable(diastyle::DStyleBridge.__init__)


def test_diastyle::dstylebridge_constructor_args():
    sig = inspect.signature(diastyle::DStyleBridge.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_diastyle::dstylebridge_has_name():
    assert hasattr(diastyle::DStyleBridge, "name")
    descriptor = None
    for klass in diastyle::DStyleBridge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_diastyle::dgraph_is_not_abstract():
    assert not inspect.isabstract(diastyle::DGraph)


def test_diastyle::dgraph_constructor_exists():
    assert callable(diastyle::DGraph.__init__)


def test_diastyle::dgraph_constructor_args():
    sig = inspect.signature(diastyle::DGraph.__init__)
    params = list(sig.parameters.keys())



def test_diastyle::dbasestyle_is_not_abstract():
    assert not inspect.isabstract(diastyle::DBaseStyle)


def test_diastyle::dbasestyle_constructor_exists():
    assert callable(diastyle::DBaseStyle.__init__)


def test_diastyle::dbasestyle_constructor_args():
    sig = inspect.signature(diastyle::DBaseStyle.__init__)
    params = list(sig.parameters.keys())
    assert "parentName" in params, "Missing parameter 'parentName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "color" in params, "Missing parameter 'color'"

def test_diastyle::dbasestyle_has_parentName():
    assert hasattr(diastyle::DBaseStyle, "parentName")
    descriptor = None
    for klass in diastyle::DBaseStyle.__mro__:
        if "parentName" in klass.__dict__:
            descriptor = klass.__dict__["parentName"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dbasestyle_has_name():
    assert hasattr(diastyle::DBaseStyle, "name")
    descriptor = None
    for klass in diastyle::DBaseStyle.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dbasestyle_has_color():
    assert hasattr(diastyle::DBaseStyle, "color")
    descriptor = None
    for klass in diastyle::DBaseStyle.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_dbasestyle_is_not_abstract():
    assert not inspect.isabstract(DBaseStyle)


def test_dbasestyle_constructor_exists():
    assert callable(DBaseStyle.__init__)


def test_dbasestyle_constructor_args():
    sig = inspect.signature(DBaseStyle.__init__)
    params = list(sig.parameters.keys())



def test_diastyle::dnestingedgestyle_is_not_abstract():
    assert not inspect.isabstract(diastyle::DNestingEdgeStyle)


def test_diastyle::dnestingedgestyle_constructor_exists():
    assert callable(diastyle::DNestingEdgeStyle.__init__)


def test_diastyle::dnestingedgestyle_constructor_args():
    sig = inspect.signature(diastyle::DNestingEdgeStyle.__init__)
    params = list(sig.parameters.keys())



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_diastyle::dstyle_is_not_abstract():
    assert not inspect.isabstract(diastyle::DStyle)


def test_diastyle::dstyle_constructor_exists():
    assert callable(diastyle::DStyle.__init__)


def test_diastyle::dstyle_constructor_args():
    sig = inspect.signature(diastyle::DStyle.__init__)
    params = list(sig.parameters.keys())
    assert "styleHandler" in params, "Missing parameter 'styleHandler'"

def test_diastyle::dstyle_has_styleHandler():
    assert hasattr(diastyle::DStyle, "styleHandler")
    descriptor = None
    for klass in diastyle::DStyle.__mro__:
        if "styleHandler" in klass.__dict__:
            descriptor = klass.__dict__["styleHandler"]
            break
    assert isinstance(descriptor, property)



def test_diastyle::dnodeedgestyle_is_not_abstract():
    assert not inspect.isabstract(diastyle::DNodeEdgeStyle)


def test_diastyle::dnodeedgestyle_constructor_exists():
    assert callable(diastyle::DNodeEdgeStyle.__init__)


def test_diastyle::dnodeedgestyle_constructor_args():
    sig = inspect.signature(diastyle::DNodeEdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "line" in params, "Missing parameter 'line'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "fontColor" in params, "Missing parameter 'fontColor'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "fontName" in params, "Missing parameter 'fontName'"
    assert "textAlignment" in params, "Missing parameter 'textAlignment'"
    assert "fontStyle" in params, "Missing parameter 'fontStyle'"
    assert "fontSize" in params, "Missing parameter 'fontSize'"

def test_diastyle::dnodeedgestyle_has_line():
    assert hasattr(diastyle::DNodeEdgeStyle, "line")
    descriptor = None
    for klass in diastyle::DNodeEdgeStyle.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dnodeedgestyle_has_icon():
    assert hasattr(diastyle::DNodeEdgeStyle, "icon")
    descriptor = None
    for klass in diastyle::DNodeEdgeStyle.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dnodeedgestyle_has_fontColor():
    assert hasattr(diastyle::DNodeEdgeStyle, "fontColor")
    descriptor = None
    for klass in diastyle::DNodeEdgeStyle.__mro__:
        if "fontColor" in klass.__dict__:
            descriptor = klass.__dict__["fontColor"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dnodeedgestyle_has_lineWidth():
    assert hasattr(diastyle::DNodeEdgeStyle, "lineWidth")
    descriptor = None
    for klass in diastyle::DNodeEdgeStyle.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dnodeedgestyle_has_fontName():
    assert hasattr(diastyle::DNodeEdgeStyle, "fontName")
    descriptor = None
    for klass in diastyle::DNodeEdgeStyle.__mro__:
        if "fontName" in klass.__dict__:
            descriptor = klass.__dict__["fontName"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dnodeedgestyle_has_textAlignment():
    assert hasattr(diastyle::DNodeEdgeStyle, "textAlignment")
    descriptor = None
    for klass in diastyle::DNodeEdgeStyle.__mro__:
        if "textAlignment" in klass.__dict__:
            descriptor = klass.__dict__["textAlignment"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dnodeedgestyle_has_fontStyle():
    assert hasattr(diastyle::DNodeEdgeStyle, "fontStyle")
    descriptor = None
    for klass in diastyle::DNodeEdgeStyle.__mro__:
        if "fontStyle" in klass.__dict__:
            descriptor = klass.__dict__["fontStyle"]
            break
    assert isinstance(descriptor, property)

def test_diastyle::dnodeedgestyle_has_fontSize():
    assert hasattr(diastyle::DNodeEdgeStyle, "fontSize")
    descriptor = None
    for klass in diastyle::DNodeEdgeStyle.__mro__:
        if "fontSize" in klass.__dict__:
            descriptor = klass.__dict__["fontSize"]
            break
    assert isinstance(descriptor, property)

def test_ddirection_exists():
    # Check that the Enumeration exists
    assert DDirection is not None

def test_ddirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DDirection]
    expected_literals = [
        "right",
        "left",
        "none",
        "bidirectional",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DDirection"

def test_dshape_exists():
    # Check that the Enumeration exists
    assert DShape is not None

def test_dshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DShape]
    expected_literals = [
        "rectangle",
        "ellipse",
        "arrow",
        "dot",
        "triangle",
        "custom",
        "roundedRectangle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DShape"

def test_dalignment_exists():
    # Check that the Enumeration exists
    assert DAlignment is not None

def test_dalignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DAlignment]
    expected_literals = [
        "fill",
        "end",
        "center",
        "beginning",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DAlignment"

def test_dlayout_exists():
    # Check that the Enumeration exists
    assert DLayout is not None

def test_dlayout_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DLayout]
    expected_literals = [
        "vertical",
        "none",
        "free",
        "horizontal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DLayout"

def test_dcolor_exists():
    # Check that the Enumeration exists
    assert DColor is not None

def test_dcolor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DColor]
    expected_literals = [
        "black",
        "darkBlue",
        "blue",
        "red",
        "lightBlue",
        "lightGray",
        "yellow",
        "gray",
        "cyan",
        "orange",
        "white",
        "darkGreen",
        "lightGreen",
        "darkGray",
        "green",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DColor"

def test_dfontstyle_exists():
    # Check that the Enumeration exists
    assert DFontStyle is not None

def test_dfontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DFontStyle]
    expected_literals = [
        "bold",
        "normal",
        "italic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DFontStyle"

def test_dline_exists():
    # Check that the Enumeration exists
    assert DLine is not None

def test_dline_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DLine]
    expected_literals = [
        "dashdotdot",
        "dashdot",
        "solid",
        "dash",
        "custom",
        "dot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DLine"

def test_dfontname_exists():
    # Check that the Enumeration exists
    assert DFontName is not None

def test_dfontname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DFontName]
    expected_literals = [
        "courier",
        "times",
        "arial",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DFontName"


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
DNodeEdgeStyle_strategy = st.builds(
    DNodeEdgeStyle,
)
diastyle::DEdgeStyle_strategy = st.builds(
    diastyle::DEdgeStyle,
    arrowDirection=
        safe_text,
    arrowSize=
        st.integers(),
    shape=
        safe_text
)
diastyle::DNodeStyle_strategy = st.builds(
    diastyle::DNodeStyle,
    figure=
        safe_text,
    layout=
        safe_text,
    shape=
        safe_text,
    shapeData=
        safe_text,
    sizeX=
        st.integers(),
    radius=
        st.integers(),
    sizeY=
        st.integers()
)
diastyle::DGraphElement_strategy = st.builds(
    diastyle::DGraphElement,
)
diastyle::DStyleBridge_strategy = st.builds(
    diastyle::DStyleBridge,
    name=
        safe_text
)
diastyle::DGraph_strategy = st.builds(
    diastyle::DGraph,
)
diastyle::DBaseStyle_strategy = st.builds(
    diastyle::DBaseStyle,
    parentName=
        safe_text,
    name=
        safe_text,
    color=
        safe_text
)
DBaseStyle_strategy = st.builds(
    DBaseStyle,
)
diastyle::DNestingEdgeStyle_strategy = st.builds(
    diastyle::DNestingEdgeStyle,
)
EModelElement_strategy = st.builds(
    EModelElement,
)
diastyle::DStyle_strategy = st.builds(
    diastyle::DStyle,
    styleHandler=
        safe_text
)
diastyle::DNodeEdgeStyle_strategy = st.builds(
    diastyle::DNodeEdgeStyle,
    line=
        safe_text,
    icon=
        safe_text,
    fontColor=
        safe_text,
    lineWidth=
        st.integers(),
    fontName=
        safe_text,
    textAlignment=
        safe_text,
    fontStyle=
        safe_text,
    fontSize=
        st.integers()
)

@given(instance=DNodeEdgeStyle_strategy)
@settings(max_examples=50)
def test_dnodeedgestyle_instantiation(instance):
    assert isinstance(instance, DNodeEdgeStyle)

@given(instance=diastyle::DEdgeStyle_strategy)
@settings(max_examples=50)
def test_diastyle::dedgestyle_instantiation(instance):
    assert isinstance(instance, diastyle::DEdgeStyle)

@given(instance=diastyle::DEdgeStyle_strategy)
def test_diastyle::dedgestyle_arrowDirection_type(instance):
    assert isinstance(instance.arrowDirection, str)


@given(instance=diastyle::DEdgeStyle_strategy)
def test_diastyle::dedgestyle_arrowDirection_setter(instance):
    original = instance.arrowDirection
    instance.arrowDirection = original
    assert instance.arrowDirection == original

@given(instance=diastyle::DEdgeStyle_strategy)
def test_diastyle::dedgestyle_arrowSize_type(instance):
    assert isinstance(instance.arrowSize, int)


@given(instance=diastyle::DEdgeStyle_strategy)
def test_diastyle::dedgestyle_arrowSize_setter(instance):
    original = instance.arrowSize
    instance.arrowSize = original
    assert instance.arrowSize == original

@given(instance=diastyle::DEdgeStyle_strategy)
def test_diastyle::dedgestyle_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=diastyle::DEdgeStyle_strategy)
def test_diastyle::dedgestyle_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=diastyle::DNodeStyle_strategy)
@settings(max_examples=50)
def test_diastyle::dnodestyle_instantiation(instance):
    assert isinstance(instance, diastyle::DNodeStyle)

@given(instance=diastyle::DNodeStyle_strategy)
def test_diastyle::dnodestyle_figure_type(instance):
    assert isinstance(instance.figure, str)


@given(instance=diastyle::DNodeStyle_strategy)
def test_diastyle::dnodestyle_figure_setter(instance):
    original = instance.figure
    instance.figure = original
    assert instance.figure == original

@given(instance=diastyle::DNodeStyle_strategy)
def test_diastyle::dnodestyle_layout_type(instance):
    assert isinstance(instance.layout, str)


@given(instance=diastyle::DNodeStyle_strategy)
def test_diastyle::dnodestyle_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original

@given(instance=diastyle::DNodeStyle_strategy)
def test_diastyle::dnodestyle_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=diastyle::DNodeStyle_strategy)
def test_diastyle::dnodestyle_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=diastyle::DNodeStyle_strategy)
def test_diastyle::dnodestyle_shapeData_type(instance):
    assert isinstance(instance.shapeData, str)


@given(instance=diastyle::DNodeStyle_strategy)
def test_diastyle::dnodestyle_shapeData_setter(instance):
    original = instance.shapeData
    instance.shapeData = original
    assert instance.shapeData == original

@given(instance=diastyle::DNodeStyle_strategy)
def test_diastyle::dnodestyle_sizeX_type(instance):
    assert isinstance(instance.sizeX, int)


@given(instance=diastyle::DNodeStyle_strategy)
def test_diastyle::dnodestyle_sizeX_setter(instance):
    original = instance.sizeX
    instance.sizeX = original
    assert instance.sizeX == original

@given(instance=diastyle::DNodeStyle_strategy)
def test_diastyle::dnodestyle_radius_type(instance):
    assert isinstance(instance.radius, int)


@given(instance=diastyle::DNodeStyle_strategy)
def test_diastyle::dnodestyle_radius_setter(instance):
    original = instance.radius
    instance.radius = original
    assert instance.radius == original

@given(instance=diastyle::DNodeStyle_strategy)
def test_diastyle::dnodestyle_sizeY_type(instance):
    assert isinstance(instance.sizeY, int)


@given(instance=diastyle::DNodeStyle_strategy)
def test_diastyle::dnodestyle_sizeY_setter(instance):
    original = instance.sizeY
    instance.sizeY = original
    assert instance.sizeY == original

@given(instance=diastyle::DGraphElement_strategy)
@settings(max_examples=50)
def test_diastyle::dgraphelement_instantiation(instance):
    assert isinstance(instance, diastyle::DGraphElement)

@given(instance=diastyle::DStyleBridge_strategy)
@settings(max_examples=50)
def test_diastyle::dstylebridge_instantiation(instance):
    assert isinstance(instance, diastyle::DStyleBridge)

@given(instance=diastyle::DStyleBridge_strategy)
def test_diastyle::dstylebridge_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=diastyle::DStyleBridge_strategy)
def test_diastyle::dstylebridge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=diastyle::DGraph_strategy)
@settings(max_examples=50)
def test_diastyle::dgraph_instantiation(instance):
    assert isinstance(instance, diastyle::DGraph)

@given(instance=diastyle::DBaseStyle_strategy)
@settings(max_examples=50)
def test_diastyle::dbasestyle_instantiation(instance):
    assert isinstance(instance, diastyle::DBaseStyle)

@given(instance=diastyle::DBaseStyle_strategy)
def test_diastyle::dbasestyle_parentName_type(instance):
    assert isinstance(instance.parentName, str)


@given(instance=diastyle::DBaseStyle_strategy)
def test_diastyle::dbasestyle_parentName_setter(instance):
    original = instance.parentName
    instance.parentName = original
    assert instance.parentName == original

@given(instance=diastyle::DBaseStyle_strategy)
def test_diastyle::dbasestyle_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=diastyle::DBaseStyle_strategy)
def test_diastyle::dbasestyle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=diastyle::DBaseStyle_strategy)
def test_diastyle::dbasestyle_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=diastyle::DBaseStyle_strategy)
def test_diastyle::dbasestyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=DBaseStyle_strategy)
@settings(max_examples=50)
def test_dbasestyle_instantiation(instance):
    assert isinstance(instance, DBaseStyle)

@given(instance=diastyle::DNestingEdgeStyle_strategy)
@settings(max_examples=50)
def test_diastyle::dnestingedgestyle_instantiation(instance):
    assert isinstance(instance, diastyle::DNestingEdgeStyle)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=diastyle::DStyle_strategy)
@settings(max_examples=50)
def test_diastyle::dstyle_instantiation(instance):
    assert isinstance(instance, diastyle::DStyle)

@given(instance=diastyle::DStyle_strategy)
def test_diastyle::dstyle_styleHandler_type(instance):
    assert isinstance(instance.styleHandler, str)


@given(instance=diastyle::DStyle_strategy)
def test_diastyle::dstyle_styleHandler_setter(instance):
    original = instance.styleHandler
    instance.styleHandler = original
    assert instance.styleHandler == original

@given(instance=diastyle::DNodeEdgeStyle_strategy)
@settings(max_examples=50)
def test_diastyle::dnodeedgestyle_instantiation(instance):
    assert isinstance(instance, diastyle::DNodeEdgeStyle)

@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_line_type(instance):
    assert isinstance(instance.line, str)


@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_fontColor_type(instance):
    assert isinstance(instance.fontColor, str)


@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_fontColor_setter(instance):
    original = instance.fontColor
    instance.fontColor = original
    assert instance.fontColor == original

@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_lineWidth_type(instance):
    assert isinstance(instance.lineWidth, int)


@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_fontName_type(instance):
    assert isinstance(instance.fontName, str)


@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original

@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_textAlignment_type(instance):
    assert isinstance(instance.textAlignment, str)


@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_textAlignment_setter(instance):
    original = instance.textAlignment
    instance.textAlignment = original
    assert instance.textAlignment == original

@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_fontStyle_type(instance):
    assert isinstance(instance.fontStyle, str)


@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_fontStyle_setter(instance):
    original = instance.fontStyle
    instance.fontStyle = original
    assert instance.fontStyle == original

@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_fontSize_type(instance):
    assert isinstance(instance.fontSize, int)


@given(instance=diastyle::DNodeEdgeStyle_strategy)
def test_diastyle::dnodeedgestyle_fontSize_setter(instance):
    original = instance.fontSize
    instance.fontSize = original
    assert instance.fontSize == original
