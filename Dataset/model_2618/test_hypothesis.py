import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DNodeEdgeStyle,
    diastyle_DEdgeStyle,
    diastyle_DNodeStyle,
    diastyle_DGraphElement,
    diastyle_DStyleBridge,
    diastyle_DGraph,
    diastyle_DBaseStyle,
    DBaseStyle,
    diastyle_DNestingEdgeStyle,
    EModelElement,
    diastyle_DStyle,
    diastyle_DNodeEdgeStyle,
    DDirection,
    DColor,
    DLayout,
    DLine,
    DShape,
    DFontStyle,
    DFontName,
    DAlignment,
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



def test_diastyle_dedgestyle_is_not_abstract():
    assert not inspect.isabstract(diastyle_DEdgeStyle)


def test_diastyle_dedgestyle_constructor_exists():
    assert callable(diastyle_DEdgeStyle.__init__)


def test_diastyle_dedgestyle_constructor_args():
    sig = inspect.signature(diastyle_DEdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "arrowDirection" in params, "Missing parameter 'arrowDirection'"
    assert "shape" in params, "Missing parameter 'shape'"
    assert "arrowSize" in params, "Missing parameter 'arrowSize'"

def test_diastyle_dedgestyle_has_arrowDirection():
    assert hasattr(diastyle_DEdgeStyle, "arrowDirection")
    descriptor = None
    for klass in diastyle_DEdgeStyle.__mro__:
        if "arrowDirection" in klass.__dict__:
            descriptor = klass.__dict__["arrowDirection"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dedgestyle_has_shape():
    assert hasattr(diastyle_DEdgeStyle, "shape")
    descriptor = None
    for klass in diastyle_DEdgeStyle.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dedgestyle_has_arrowSize():
    assert hasattr(diastyle_DEdgeStyle, "arrowSize")
    descriptor = None
    for klass in diastyle_DEdgeStyle.__mro__:
        if "arrowSize" in klass.__dict__:
            descriptor = klass.__dict__["arrowSize"]
            break
    assert isinstance(descriptor, property)



def test_diastyle_dnodestyle_is_not_abstract():
    assert not inspect.isabstract(diastyle_DNodeStyle)


def test_diastyle_dnodestyle_constructor_exists():
    assert callable(diastyle_DNodeStyle.__init__)


def test_diastyle_dnodestyle_constructor_args():
    sig = inspect.signature(diastyle_DNodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "radius" in params, "Missing parameter 'radius'"
    assert "shapeData" in params, "Missing parameter 'shapeData'"
    assert "sizeX" in params, "Missing parameter 'sizeX'"
    assert "figure" in params, "Missing parameter 'figure'"
    assert "layout" in params, "Missing parameter 'layout'"
    assert "sizeY" in params, "Missing parameter 'sizeY'"

def test_diastyle_dnodestyle_has_shape():
    assert hasattr(diastyle_DNodeStyle, "shape")
    descriptor = None
    for klass in diastyle_DNodeStyle.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dnodestyle_has_radius():
    assert hasattr(diastyle_DNodeStyle, "radius")
    descriptor = None
    for klass in diastyle_DNodeStyle.__mro__:
        if "radius" in klass.__dict__:
            descriptor = klass.__dict__["radius"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dnodestyle_has_shapeData():
    assert hasattr(diastyle_DNodeStyle, "shapeData")
    descriptor = None
    for klass in diastyle_DNodeStyle.__mro__:
        if "shapeData" in klass.__dict__:
            descriptor = klass.__dict__["shapeData"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dnodestyle_has_sizeX():
    assert hasattr(diastyle_DNodeStyle, "sizeX")
    descriptor = None
    for klass in diastyle_DNodeStyle.__mro__:
        if "sizeX" in klass.__dict__:
            descriptor = klass.__dict__["sizeX"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dnodestyle_has_figure():
    assert hasattr(diastyle_DNodeStyle, "figure")
    descriptor = None
    for klass in diastyle_DNodeStyle.__mro__:
        if "figure" in klass.__dict__:
            descriptor = klass.__dict__["figure"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dnodestyle_has_layout():
    assert hasattr(diastyle_DNodeStyle, "layout")
    descriptor = None
    for klass in diastyle_DNodeStyle.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dnodestyle_has_sizeY():
    assert hasattr(diastyle_DNodeStyle, "sizeY")
    descriptor = None
    for klass in diastyle_DNodeStyle.__mro__:
        if "sizeY" in klass.__dict__:
            descriptor = klass.__dict__["sizeY"]
            break
    assert isinstance(descriptor, property)



def test_diastyle_dgraphelement_is_not_abstract():
    assert not inspect.isabstract(diastyle_DGraphElement)


def test_diastyle_dgraphelement_constructor_exists():
    assert callable(diastyle_DGraphElement.__init__)


def test_diastyle_dgraphelement_constructor_args():
    sig = inspect.signature(diastyle_DGraphElement.__init__)
    params = list(sig.parameters.keys())



def test_diastyle_dstylebridge_is_not_abstract():
    assert not inspect.isabstract(diastyle_DStyleBridge)


def test_diastyle_dstylebridge_constructor_exists():
    assert callable(diastyle_DStyleBridge.__init__)


def test_diastyle_dstylebridge_constructor_args():
    sig = inspect.signature(diastyle_DStyleBridge.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_diastyle_dstylebridge_has_name():
    assert hasattr(diastyle_DStyleBridge, "name")
    descriptor = None
    for klass in diastyle_DStyleBridge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_diastyle_dgraph_is_not_abstract():
    assert not inspect.isabstract(diastyle_DGraph)


def test_diastyle_dgraph_constructor_exists():
    assert callable(diastyle_DGraph.__init__)


def test_diastyle_dgraph_constructor_args():
    sig = inspect.signature(diastyle_DGraph.__init__)
    params = list(sig.parameters.keys())



def test_diastyle_dbasestyle_is_not_abstract():
    assert not inspect.isabstract(diastyle_DBaseStyle)


def test_diastyle_dbasestyle_constructor_exists():
    assert callable(diastyle_DBaseStyle.__init__)


def test_diastyle_dbasestyle_constructor_args():
    sig = inspect.signature(diastyle_DBaseStyle.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "color" in params, "Missing parameter 'color'"
    assert "parentName" in params, "Missing parameter 'parentName'"

def test_diastyle_dbasestyle_has_name():
    assert hasattr(diastyle_DBaseStyle, "name")
    descriptor = None
    for klass in diastyle_DBaseStyle.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dbasestyle_has_color():
    assert hasattr(diastyle_DBaseStyle, "color")
    descriptor = None
    for klass in diastyle_DBaseStyle.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dbasestyle_has_parentName():
    assert hasattr(diastyle_DBaseStyle, "parentName")
    descriptor = None
    for klass in diastyle_DBaseStyle.__mro__:
        if "parentName" in klass.__dict__:
            descriptor = klass.__dict__["parentName"]
            break
    assert isinstance(descriptor, property)



def test_dbasestyle_is_not_abstract():
    assert not inspect.isabstract(DBaseStyle)


def test_dbasestyle_constructor_exists():
    assert callable(DBaseStyle.__init__)


def test_dbasestyle_constructor_args():
    sig = inspect.signature(DBaseStyle.__init__)
    params = list(sig.parameters.keys())



def test_diastyle_dnestingedgestyle_is_not_abstract():
    assert not inspect.isabstract(diastyle_DNestingEdgeStyle)


def test_diastyle_dnestingedgestyle_constructor_exists():
    assert callable(diastyle_DNestingEdgeStyle.__init__)


def test_diastyle_dnestingedgestyle_constructor_args():
    sig = inspect.signature(diastyle_DNestingEdgeStyle.__init__)
    params = list(sig.parameters.keys())



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_diastyle_dstyle_is_not_abstract():
    assert not inspect.isabstract(diastyle_DStyle)


def test_diastyle_dstyle_constructor_exists():
    assert callable(diastyle_DStyle.__init__)


def test_diastyle_dstyle_constructor_args():
    sig = inspect.signature(diastyle_DStyle.__init__)
    params = list(sig.parameters.keys())
    assert "styleHandler" in params, "Missing parameter 'styleHandler'"

def test_diastyle_dstyle_has_styleHandler():
    assert hasattr(diastyle_DStyle, "styleHandler")
    descriptor = None
    for klass in diastyle_DStyle.__mro__:
        if "styleHandler" in klass.__dict__:
            descriptor = klass.__dict__["styleHandler"]
            break
    assert isinstance(descriptor, property)



def test_diastyle_dnodeedgestyle_is_not_abstract():
    assert not inspect.isabstract(diastyle_DNodeEdgeStyle)


def test_diastyle_dnodeedgestyle_constructor_exists():
    assert callable(diastyle_DNodeEdgeStyle.__init__)


def test_diastyle_dnodeedgestyle_constructor_args():
    sig = inspect.signature(diastyle_DNodeEdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "fontStyle" in params, "Missing parameter 'fontStyle'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "textAlignment" in params, "Missing parameter 'textAlignment'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "fontColor" in params, "Missing parameter 'fontColor'"
    assert "fontName" in params, "Missing parameter 'fontName'"
    assert "fontSize" in params, "Missing parameter 'fontSize'"
    assert "line" in params, "Missing parameter 'line'"

def test_diastyle_dnodeedgestyle_has_fontStyle():
    assert hasattr(diastyle_DNodeEdgeStyle, "fontStyle")
    descriptor = None
    for klass in diastyle_DNodeEdgeStyle.__mro__:
        if "fontStyle" in klass.__dict__:
            descriptor = klass.__dict__["fontStyle"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dnodeedgestyle_has_lineWidth():
    assert hasattr(diastyle_DNodeEdgeStyle, "lineWidth")
    descriptor = None
    for klass in diastyle_DNodeEdgeStyle.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dnodeedgestyle_has_textAlignment():
    assert hasattr(diastyle_DNodeEdgeStyle, "textAlignment")
    descriptor = None
    for klass in diastyle_DNodeEdgeStyle.__mro__:
        if "textAlignment" in klass.__dict__:
            descriptor = klass.__dict__["textAlignment"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dnodeedgestyle_has_icon():
    assert hasattr(diastyle_DNodeEdgeStyle, "icon")
    descriptor = None
    for klass in diastyle_DNodeEdgeStyle.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dnodeedgestyle_has_fontColor():
    assert hasattr(diastyle_DNodeEdgeStyle, "fontColor")
    descriptor = None
    for klass in diastyle_DNodeEdgeStyle.__mro__:
        if "fontColor" in klass.__dict__:
            descriptor = klass.__dict__["fontColor"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dnodeedgestyle_has_fontName():
    assert hasattr(diastyle_DNodeEdgeStyle, "fontName")
    descriptor = None
    for klass in diastyle_DNodeEdgeStyle.__mro__:
        if "fontName" in klass.__dict__:
            descriptor = klass.__dict__["fontName"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dnodeedgestyle_has_fontSize():
    assert hasattr(diastyle_DNodeEdgeStyle, "fontSize")
    descriptor = None
    for klass in diastyle_DNodeEdgeStyle.__mro__:
        if "fontSize" in klass.__dict__:
            descriptor = klass.__dict__["fontSize"]
            break
    assert isinstance(descriptor, property)

def test_diastyle_dnodeedgestyle_has_line():
    assert hasattr(diastyle_DNodeEdgeStyle, "line")
    descriptor = None
    for klass in diastyle_DNodeEdgeStyle.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
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
        "bidirectional",
        "none",
        "left",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DDirection"

def test_dcolor_exists():
    # Check that the Enumeration exists
    assert DColor is not None

def test_dcolor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DColor]
    expected_literals = [
        "lightGreen",
        "gray",
        "darkBlue",
        "darkGreen",
        "darkGray",
        "green",
        "white",
        "black",
        "cyan",
        "orange",
        "lightBlue",
        "blue",
        "red",
        "yellow",
        "lightGray",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DColor"

def test_dlayout_exists():
    # Check that the Enumeration exists
    assert DLayout is not None

def test_dlayout_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DLayout]
    expected_literals = [
        "free",
        "none",
        "vertical",
        "horizontal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DLayout"

def test_dline_exists():
    # Check that the Enumeration exists
    assert DLine is not None

def test_dline_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DLine]
    expected_literals = [
        "solid",
        "dashdot",
        "custom",
        "dot",
        "dash",
        "dashdotdot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DLine"

def test_dshape_exists():
    # Check that the Enumeration exists
    assert DShape is not None

def test_dshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DShape]
    expected_literals = [
        "rectangle",
        "roundedRectangle",
        "custom",
        "dot",
        "triangle",
        "ellipse",
        "arrow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DShape"

def test_dfontstyle_exists():
    # Check that the Enumeration exists
    assert DFontStyle is not None

def test_dfontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DFontStyle]
    expected_literals = [
        "italic",
        "bold",
        "normal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DFontStyle"

def test_dfontname_exists():
    # Check that the Enumeration exists
    assert DFontName is not None

def test_dfontname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DFontName]
    expected_literals = [
        "times",
        "arial",
        "courier",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DFontName"

def test_dalignment_exists():
    # Check that the Enumeration exists
    assert DAlignment is not None

def test_dalignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DAlignment]
    expected_literals = [
        "beginning",
        "center",
        "fill",
        "end",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DAlignment"


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
diastyle_DEdgeStyle_strategy = st.builds(
    diastyle_DEdgeStyle,
    arrowDirection=
        safe_text,
    shape=
        safe_text,
    arrowSize=
        st.integers()
)
diastyle_DNodeStyle_strategy = st.builds(
    diastyle_DNodeStyle,
    shape=
        safe_text,
    radius=
        st.integers(),
    shapeData=
        safe_text,
    sizeX=
        st.integers(),
    figure=
        safe_text,
    layout=
        safe_text,
    sizeY=
        st.integers()
)
diastyle_DGraphElement_strategy = st.builds(
    diastyle_DGraphElement,
)
diastyle_DStyleBridge_strategy = st.builds(
    diastyle_DStyleBridge,
    name=
        safe_text
)
diastyle_DGraph_strategy = st.builds(
    diastyle_DGraph,
)
diastyle_DBaseStyle_strategy = st.builds(
    diastyle_DBaseStyle,
    name=
        safe_text,
    color=
        safe_text,
    parentName=
        safe_text
)
DBaseStyle_strategy = st.builds(
    DBaseStyle,
)
diastyle_DNestingEdgeStyle_strategy = st.builds(
    diastyle_DNestingEdgeStyle,
)
EModelElement_strategy = st.builds(
    EModelElement,
)
diastyle_DStyle_strategy = st.builds(
    diastyle_DStyle,
    styleHandler=
        safe_text
)
diastyle_DNodeEdgeStyle_strategy = st.builds(
    diastyle_DNodeEdgeStyle,
    fontStyle=
        safe_text,
    lineWidth=
        st.integers(),
    textAlignment=
        safe_text,
    icon=
        safe_text,
    fontColor=
        safe_text,
    fontName=
        safe_text,
    fontSize=
        st.integers(),
    line=
        safe_text
)

@given(instance=DNodeEdgeStyle_strategy)
@settings(max_examples=50)
def test_dnodeedgestyle_instantiation(instance):
    assert isinstance(instance, DNodeEdgeStyle)

@given(instance=diastyle_DEdgeStyle_strategy)
@settings(max_examples=50)
def test_diastyle_dedgestyle_instantiation(instance):
    assert isinstance(instance, diastyle_DEdgeStyle)



@given(instance=diastyle_DEdgeStyle_strategy)
def test_diastyle_dedgestyle_arrowDirection_setter(instance):
    original = instance.arrowDirection
    instance.arrowDirection = original
    assert instance.arrowDirection == original



@given(instance=diastyle_DEdgeStyle_strategy)
def test_diastyle_dedgestyle_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=diastyle_DEdgeStyle_strategy)
def test_diastyle_dedgestyle_arrowSize_setter(instance):
    original = instance.arrowSize
    instance.arrowSize = original
    assert instance.arrowSize == original

@given(instance=diastyle_DNodeStyle_strategy)
@settings(max_examples=50)
def test_diastyle_dnodestyle_instantiation(instance):
    assert isinstance(instance, diastyle_DNodeStyle)



@given(instance=diastyle_DNodeStyle_strategy)
def test_diastyle_dnodestyle_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=diastyle_DNodeStyle_strategy)
def test_diastyle_dnodestyle_radius_setter(instance):
    original = instance.radius
    instance.radius = original
    assert instance.radius == original



@given(instance=diastyle_DNodeStyle_strategy)
def test_diastyle_dnodestyle_shapeData_setter(instance):
    original = instance.shapeData
    instance.shapeData = original
    assert instance.shapeData == original



@given(instance=diastyle_DNodeStyle_strategy)
def test_diastyle_dnodestyle_sizeX_setter(instance):
    original = instance.sizeX
    instance.sizeX = original
    assert instance.sizeX == original



@given(instance=diastyle_DNodeStyle_strategy)
def test_diastyle_dnodestyle_figure_setter(instance):
    original = instance.figure
    instance.figure = original
    assert instance.figure == original



@given(instance=diastyle_DNodeStyle_strategy)
def test_diastyle_dnodestyle_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original



@given(instance=diastyle_DNodeStyle_strategy)
def test_diastyle_dnodestyle_sizeY_setter(instance):
    original = instance.sizeY
    instance.sizeY = original
    assert instance.sizeY == original

@given(instance=diastyle_DGraphElement_strategy)
@settings(max_examples=50)
def test_diastyle_dgraphelement_instantiation(instance):
    assert isinstance(instance, diastyle_DGraphElement)

@given(instance=diastyle_DStyleBridge_strategy)
@settings(max_examples=50)
def test_diastyle_dstylebridge_instantiation(instance):
    assert isinstance(instance, diastyle_DStyleBridge)



@given(instance=diastyle_DStyleBridge_strategy)
def test_diastyle_dstylebridge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=diastyle_DGraph_strategy)
@settings(max_examples=50)
def test_diastyle_dgraph_instantiation(instance):
    assert isinstance(instance, diastyle_DGraph)

@given(instance=diastyle_DBaseStyle_strategy)
@settings(max_examples=50)
def test_diastyle_dbasestyle_instantiation(instance):
    assert isinstance(instance, diastyle_DBaseStyle)



@given(instance=diastyle_DBaseStyle_strategy)
def test_diastyle_dbasestyle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=diastyle_DBaseStyle_strategy)
def test_diastyle_dbasestyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=diastyle_DBaseStyle_strategy)
def test_diastyle_dbasestyle_parentName_setter(instance):
    original = instance.parentName
    instance.parentName = original
    assert instance.parentName == original

@given(instance=DBaseStyle_strategy)
@settings(max_examples=50)
def test_dbasestyle_instantiation(instance):
    assert isinstance(instance, DBaseStyle)

@given(instance=diastyle_DNestingEdgeStyle_strategy)
@settings(max_examples=50)
def test_diastyle_dnestingedgestyle_instantiation(instance):
    assert isinstance(instance, diastyle_DNestingEdgeStyle)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=diastyle_DStyle_strategy)
@settings(max_examples=50)
def test_diastyle_dstyle_instantiation(instance):
    assert isinstance(instance, diastyle_DStyle)



@given(instance=diastyle_DStyle_strategy)
def test_diastyle_dstyle_styleHandler_setter(instance):
    original = instance.styleHandler
    instance.styleHandler = original
    assert instance.styleHandler == original

@given(instance=diastyle_DNodeEdgeStyle_strategy)
@settings(max_examples=50)
def test_diastyle_dnodeedgestyle_instantiation(instance):
    assert isinstance(instance, diastyle_DNodeEdgeStyle)



@given(instance=diastyle_DNodeEdgeStyle_strategy)
def test_diastyle_dnodeedgestyle_fontStyle_setter(instance):
    original = instance.fontStyle
    instance.fontStyle = original
    assert instance.fontStyle == original



@given(instance=diastyle_DNodeEdgeStyle_strategy)
def test_diastyle_dnodeedgestyle_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original



@given(instance=diastyle_DNodeEdgeStyle_strategy)
def test_diastyle_dnodeedgestyle_textAlignment_setter(instance):
    original = instance.textAlignment
    instance.textAlignment = original
    assert instance.textAlignment == original



@given(instance=diastyle_DNodeEdgeStyle_strategy)
def test_diastyle_dnodeedgestyle_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=diastyle_DNodeEdgeStyle_strategy)
def test_diastyle_dnodeedgestyle_fontColor_setter(instance):
    original = instance.fontColor
    instance.fontColor = original
    assert instance.fontColor == original



@given(instance=diastyle_DNodeEdgeStyle_strategy)
def test_diastyle_dnodeedgestyle_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original



@given(instance=diastyle_DNodeEdgeStyle_strategy)
def test_diastyle_dnodeedgestyle_fontSize_setter(instance):
    original = instance.fontSize
    instance.fontSize = original
    assert instance.fontSize == original



@given(instance=diastyle_DNodeEdgeStyle_strategy)
def test_diastyle_dnodeedgestyle_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original
