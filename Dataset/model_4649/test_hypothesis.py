import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    di_ElementEntry,
    di_Guide,
    Line,
    Shape,
    di_GradientShape,
    di_Ruler,
    Node,
    di_Grid,
    di_Comment,
    Container,
    di_Diagram,
    di_Connector,
    di_Line,
    di_Shape,
    di_EObject,
    di_View,
    di_CommentLink,
    View,
    di_Container,
    di_Node,
    Alignment,
    RulerUnit,
    LineStyle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_di_elemententry_is_not_abstract():
    assert not inspect.isabstract(di_ElementEntry)


def test_di_elemententry_constructor_exists():
    assert callable(di_ElementEntry.__init__)


def test_di_elemententry_constructor_args():
    sig = inspect.signature(di_ElementEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_di_elemententry_has_value():
    assert hasattr(di_ElementEntry, "value")
    descriptor = None
    for klass in di_ElementEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_di_guide_is_not_abstract():
    assert not inspect.isabstract(di_Guide)


def test_di_guide_constructor_exists():
    assert callable(di_Guide.__init__)


def test_di_guide_constructor_args():
    sig = inspect.signature(di_Guide.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_di_guide_has_position():
    assert hasattr(di_Guide, "position")
    descriptor = None
    for klass in di_Guide.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_line_is_not_abstract():
    assert not inspect.isabstract(Line)


def test_line_constructor_exists():
    assert callable(Line.__init__)


def test_line_constructor_args():
    sig = inspect.signature(Line.__init__)
    params = list(sig.parameters.keys())



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_di_gradientshape_is_not_abstract():
    assert not inspect.isabstract(di_GradientShape)


def test_di_gradientshape_constructor_exists():
    assert callable(di_GradientShape.__init__)


def test_di_gradientshape_constructor_args():
    sig = inspect.signature(di_GradientShape.__init__)
    params = list(sig.parameters.keys())
    assert "usingGradient" in params, "Missing parameter 'usingGradient'"
    assert "verticalGradient" in params, "Missing parameter 'verticalGradient'"
    assert "gradientColor" in params, "Missing parameter 'gradientColor'"

def test_di_gradientshape_has_usingGradient():
    assert hasattr(di_GradientShape, "usingGradient")
    descriptor = None
    for klass in di_GradientShape.__mro__:
        if "usingGradient" in klass.__dict__:
            descriptor = klass.__dict__["usingGradient"]
            break
    assert isinstance(descriptor, property)

def test_di_gradientshape_has_verticalGradient():
    assert hasattr(di_GradientShape, "verticalGradient")
    descriptor = None
    for klass in di_GradientShape.__mro__:
        if "verticalGradient" in klass.__dict__:
            descriptor = klass.__dict__["verticalGradient"]
            break
    assert isinstance(descriptor, property)

def test_di_gradientshape_has_gradientColor():
    assert hasattr(di_GradientShape, "gradientColor")
    descriptor = None
    for klass in di_GradientShape.__mro__:
        if "gradientColor" in klass.__dict__:
            descriptor = klass.__dict__["gradientColor"]
            break
    assert isinstance(descriptor, property)



def test_di_ruler_is_not_abstract():
    assert not inspect.isabstract(di_Ruler)


def test_di_ruler_constructor_exists():
    assert callable(di_Ruler.__init__)


def test_di_ruler_constructor_args():
    sig = inspect.signature(di_Ruler.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_di_ruler_has_unit():
    assert hasattr(di_Ruler, "unit")
    descriptor = None
    for klass in di_Ruler.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_di_grid_is_not_abstract():
    assert not inspect.isabstract(di_Grid)


def test_di_grid_constructor_exists():
    assert callable(di_Grid.__init__)


def test_di_grid_constructor_args():
    sig = inspect.signature(di_Grid.__init__)
    params = list(sig.parameters.keys())
    assert "spacing" in params, "Missing parameter 'spacing'"
    assert "style" in params, "Missing parameter 'style'"
    assert "color" in params, "Missing parameter 'color'"

def test_di_grid_has_spacing():
    assert hasattr(di_Grid, "spacing")
    descriptor = None
    for klass in di_Grid.__mro__:
        if "spacing" in klass.__dict__:
            descriptor = klass.__dict__["spacing"]
            break
    assert isinstance(descriptor, property)

def test_di_grid_has_style():
    assert hasattr(di_Grid, "style")
    descriptor = None
    for klass in di_Grid.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_di_grid_has_color():
    assert hasattr(di_Grid, "color")
    descriptor = None
    for klass in di_Grid.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_di_comment_is_not_abstract():
    assert not inspect.isabstract(di_Comment)


def test_di_comment_constructor_exists():
    assert callable(di_Comment.__init__)


def test_di_comment_constructor_args():
    sig = inspect.signature(di_Comment.__init__)
    params = list(sig.parameters.keys())



def test_container_is_not_abstract():
    assert not inspect.isabstract(Container)


def test_container_constructor_exists():
    assert callable(Container.__init__)


def test_container_constructor_args():
    sig = inspect.signature(Container.__init__)
    params = list(sig.parameters.keys())



def test_di_diagram_is_not_abstract():
    assert not inspect.isabstract(di_Diagram)


def test_di_diagram_constructor_exists():
    assert callable(di_Diagram.__init__)


def test_di_diagram_constructor_args():
    sig = inspect.signature(di_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "snapToGeometry" in params, "Missing parameter 'snapToGeometry'"
    assert "rulers" in params, "Missing parameter 'rulers'"
    assert "snapToGrid" in params, "Missing parameter 'snapToGrid'"

def test_di_diagram_has_snapToGeometry():
    assert hasattr(di_Diagram, "snapToGeometry")
    descriptor = None
    for klass in di_Diagram.__mro__:
        if "snapToGeometry" in klass.__dict__:
            descriptor = klass.__dict__["snapToGeometry"]
            break
    assert isinstance(descriptor, property)

def test_di_diagram_has_rulers():
    assert hasattr(di_Diagram, "rulers")
    descriptor = None
    for klass in di_Diagram.__mro__:
        if "rulers" in klass.__dict__:
            descriptor = klass.__dict__["rulers"]
            break
    assert isinstance(descriptor, property)

def test_di_diagram_has_snapToGrid():
    assert hasattr(di_Diagram, "snapToGrid")
    descriptor = None
    for klass in di_Diagram.__mro__:
        if "snapToGrid" in klass.__dict__:
            descriptor = klass.__dict__["snapToGrid"]
            break
    assert isinstance(descriptor, property)



def test_di_connector_is_not_abstract():
    assert not inspect.isabstract(di_Connector)


def test_di_connector_constructor_exists():
    assert callable(di_Connector.__init__)


def test_di_connector_constructor_args():
    sig = inspect.signature(di_Connector.__init__)
    params = list(sig.parameters.keys())



def test_di_line_is_not_abstract():
    assert not inspect.isabstract(di_Line)


def test_di_line_constructor_exists():
    assert callable(di_Line.__init__)


def test_di_line_constructor_args():
    sig = inspect.signature(di_Line.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "width" in params, "Missing parameter 'width'"
    assert "sourceNode" in params, "Missing parameter 'sourceNode'"
    assert "targetAnchor" in params, "Missing parameter 'targetAnchor'"
    assert "lineDash" in params, "Missing parameter 'lineDash'"
    assert "targetNode" in params, "Missing parameter 'targetNode'"
    assert "sourceAnchor" in params, "Missing parameter 'sourceAnchor'"
    assert "color" in params, "Missing parameter 'color'"

def test_di_line_has_style():
    assert hasattr(di_Line, "style")
    descriptor = None
    for klass in di_Line.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_di_line_has_width():
    assert hasattr(di_Line, "width")
    descriptor = None
    for klass in di_Line.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_di_line_has_sourceNode():
    assert hasattr(di_Line, "sourceNode")
    descriptor = None
    for klass in di_Line.__mro__:
        if "sourceNode" in klass.__dict__:
            descriptor = klass.__dict__["sourceNode"]
            break
    assert isinstance(descriptor, property)

def test_di_line_has_targetAnchor():
    assert hasattr(di_Line, "targetAnchor")
    descriptor = None
    for klass in di_Line.__mro__:
        if "targetAnchor" in klass.__dict__:
            descriptor = klass.__dict__["targetAnchor"]
            break
    assert isinstance(descriptor, property)

def test_di_line_has_lineDash():
    assert hasattr(di_Line, "lineDash")
    descriptor = None
    for klass in di_Line.__mro__:
        if "lineDash" in klass.__dict__:
            descriptor = klass.__dict__["lineDash"]
            break
    assert isinstance(descriptor, property)

def test_di_line_has_targetNode():
    assert hasattr(di_Line, "targetNode")
    descriptor = None
    for klass in di_Line.__mro__:
        if "targetNode" in klass.__dict__:
            descriptor = klass.__dict__["targetNode"]
            break
    assert isinstance(descriptor, property)

def test_di_line_has_sourceAnchor():
    assert hasattr(di_Line, "sourceAnchor")
    descriptor = None
    for klass in di_Line.__mro__:
        if "sourceAnchor" in klass.__dict__:
            descriptor = klass.__dict__["sourceAnchor"]
            break
    assert isinstance(descriptor, property)

def test_di_line_has_color():
    assert hasattr(di_Line, "color")
    descriptor = None
    for klass in di_Line.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_di_shape_is_not_abstract():
    assert not inspect.isabstract(di_Shape)


def test_di_shape_constructor_exists():
    assert callable(di_Shape.__init__)


def test_di_shape_constructor_args():
    sig = inspect.signature(di_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "background" in params, "Missing parameter 'background'"
    assert "bounds" in params, "Missing parameter 'bounds'"
    assert "foreground" in params, "Missing parameter 'foreground'"

def test_di_shape_has_background():
    assert hasattr(di_Shape, "background")
    descriptor = None
    for klass in di_Shape.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_di_shape_has_bounds():
    assert hasattr(di_Shape, "bounds")
    descriptor = None
    for klass in di_Shape.__mro__:
        if "bounds" in klass.__dict__:
            descriptor = klass.__dict__["bounds"]
            break
    assert isinstance(descriptor, property)

def test_di_shape_has_foreground():
    assert hasattr(di_Shape, "foreground")
    descriptor = None
    for klass in di_Shape.__mro__:
        if "foreground" in klass.__dict__:
            descriptor = klass.__dict__["foreground"]
            break
    assert isinstance(descriptor, property)



def test_di_eobject_is_not_abstract():
    assert not inspect.isabstract(di_EObject)


def test_di_eobject_constructor_exists():
    assert callable(di_EObject.__init__)


def test_di_eobject_constructor_args():
    sig = inspect.signature(di_EObject.__init__)
    params = list(sig.parameters.keys())



def test_di_view_is_not_abstract():
    assert not inspect.isabstract(di_View)


def test_di_view_constructor_exists():
    assert callable(di_View.__init__)


def test_di_view_constructor_args():
    sig = inspect.signature(di_View.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "id" in params, "Missing parameter 'id'"

def test_di_view_has_label():
    assert hasattr(di_View, "label")
    descriptor = None
    for klass in di_View.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_di_view_has_id():
    assert hasattr(di_View, "id")
    descriptor = None
    for klass in di_View.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_di_commentlink_is_not_abstract():
    assert not inspect.isabstract(di_CommentLink)


def test_di_commentlink_constructor_exists():
    assert callable(di_CommentLink.__init__)


def test_di_commentlink_constructor_args():
    sig = inspect.signature(di_CommentLink.__init__)
    params = list(sig.parameters.keys())



def test_view_is_not_abstract():
    assert not inspect.isabstract(View)


def test_view_constructor_exists():
    assert callable(View.__init__)


def test_view_constructor_args():
    sig = inspect.signature(View.__init__)
    params = list(sig.parameters.keys())



def test_di_container_is_not_abstract():
    assert not inspect.isabstract(di_Container)


def test_di_container_constructor_exists():
    assert callable(di_Container.__init__)


def test_di_container_constructor_args():
    sig = inspect.signature(di_Container.__init__)
    params = list(sig.parameters.keys())
    assert "allLines" in params, "Missing parameter 'allLines'"
    assert "allShapes" in params, "Missing parameter 'allShapes'"

def test_di_container_has_allLines():
    assert hasattr(di_Container, "allLines")
    descriptor = None
    for klass in di_Container.__mro__:
        if "allLines" in klass.__dict__:
            descriptor = klass.__dict__["allLines"]
            break
    assert isinstance(descriptor, property)

def test_di_container_has_allShapes():
    assert hasattr(di_Container, "allShapes")
    descriptor = None
    for klass in di_Container.__mro__:
        if "allShapes" in klass.__dict__:
            descriptor = klass.__dict__["allShapes"]
            break
    assert isinstance(descriptor, property)



def test_di_node_is_not_abstract():
    assert not inspect.isabstract(di_Node)


def test_di_node_constructor_exists():
    assert callable(di_Node.__init__)


def test_di_node_constructor_args():
    sig = inspect.signature(di_Node.__init__)
    params = list(sig.parameters.keys())
    assert "allIncomingLines" in params, "Missing parameter 'allIncomingLines'"
    assert "allOutgoingLines" in params, "Missing parameter 'allOutgoingLines'"

def test_di_node_has_allIncomingLines():
    assert hasattr(di_Node, "allIncomingLines")
    descriptor = None
    for klass in di_Node.__mro__:
        if "allIncomingLines" in klass.__dict__:
            descriptor = klass.__dict__["allIncomingLines"]
            break
    assert isinstance(descriptor, property)

def test_di_node_has_allOutgoingLines():
    assert hasattr(di_Node, "allOutgoingLines")
    descriptor = None
    for klass in di_Node.__mro__:
        if "allOutgoingLines" in klass.__dict__:
            descriptor = klass.__dict__["allOutgoingLines"]
            break
    assert isinstance(descriptor, property)

def test_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "BOTTOM",
        "LEFT",
        "TOP",
        "CENTER",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Alignment"

def test_rulerunit_exists():
    # Check that the Enumeration exists
    assert RulerUnit is not None

def test_rulerunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RulerUnit]
    expected_literals = [
        "INCHES",
        "PIXELS",
        "CENTIMETERS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RulerUnit"

def test_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "DOT",
        "SOLID",
        "DASH",
        "LINE_CUSTOM",
        "DASHDOTDOT",
        "DASHDOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"


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
di_ElementEntry_strategy = st.builds(
    di_ElementEntry,
    value=
        safe_text
)
di_Guide_strategy = st.builds(
    di_Guide,
    position=
        st.integers()
)
Line_strategy = st.builds(
    Line,
)
Shape_strategy = st.builds(
    Shape,
)
di_GradientShape_strategy = st.builds(
    di_GradientShape,
    usingGradient=
        st.booleans(),
    verticalGradient=
        st.booleans(),
    gradientColor=
        st.integers()
)
di_Ruler_strategy = st.builds(
    di_Ruler,
    unit=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
di_Grid_strategy = st.builds(
    di_Grid,
    spacing=
        st.integers(),
    style=
        safe_text,
    color=
        st.integers()
)
di_Comment_strategy = st.builds(
    di_Comment,
)
Container_strategy = st.builds(
    Container,
)
di_Diagram_strategy = st.builds(
    di_Diagram,
    snapToGeometry=
        st.booleans(),
    rulers=
        safe_text,
    snapToGrid=
        st.booleans()
)
di_Connector_strategy = st.builds(
    di_Connector,
)
di_Line_strategy = st.builds(
    di_Line,
    style=
        safe_text,
    width=
        st.integers(),
    sourceNode=
        safe_text,
    targetAnchor=
        safe_text,
    lineDash=
        st.integers(),
    targetNode=
        safe_text,
    sourceAnchor=
        safe_text,
    color=
        st.integers()
)
di_Shape_strategy = st.builds(
    di_Shape,
    background=
        st.integers(),
    bounds=
        safe_text,
    foreground=
        st.integers()
)
di_EObject_strategy = st.builds(
    di_EObject,
)
di_View_strategy = st.builds(
    di_View,
    label=
        safe_text,
    id=
        safe_text
)
di_CommentLink_strategy = st.builds(
    di_CommentLink,
)
View_strategy = st.builds(
    View,
)
di_Container_strategy = st.builds(
    di_Container,
    allLines=
        safe_text,
    allShapes=
        safe_text
)
di_Node_strategy = st.builds(
    di_Node,
    allIncomingLines=
        safe_text,
    allOutgoingLines=
        safe_text
)

@given(instance=di_ElementEntry_strategy)
@settings(max_examples=50)
def test_di_elemententry_instantiation(instance):
    assert isinstance(instance, di_ElementEntry)



@given(instance=di_ElementEntry_strategy)
def test_di_elemententry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=di_Guide_strategy)
@settings(max_examples=50)
def test_di_guide_instantiation(instance):
    assert isinstance(instance, di_Guide)



@given(instance=di_Guide_strategy)
def test_di_guide_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=Line_strategy)
@settings(max_examples=50)
def test_line_instantiation(instance):
    assert isinstance(instance, Line)

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=di_GradientShape_strategy)
@settings(max_examples=50)
def test_di_gradientshape_instantiation(instance):
    assert isinstance(instance, di_GradientShape)



@given(instance=di_GradientShape_strategy)
def test_di_gradientshape_usingGradient_setter(instance):
    original = instance.usingGradient
    instance.usingGradient = original
    assert instance.usingGradient == original



@given(instance=di_GradientShape_strategy)
def test_di_gradientshape_verticalGradient_setter(instance):
    original = instance.verticalGradient
    instance.verticalGradient = original
    assert instance.verticalGradient == original



@given(instance=di_GradientShape_strategy)
def test_di_gradientshape_gradientColor_setter(instance):
    original = instance.gradientColor
    instance.gradientColor = original
    assert instance.gradientColor == original

@given(instance=di_Ruler_strategy)
@settings(max_examples=50)
def test_di_ruler_instantiation(instance):
    assert isinstance(instance, di_Ruler)



@given(instance=di_Ruler_strategy)
def test_di_ruler_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=di_Grid_strategy)
@settings(max_examples=50)
def test_di_grid_instantiation(instance):
    assert isinstance(instance, di_Grid)



@given(instance=di_Grid_strategy)
def test_di_grid_spacing_setter(instance):
    original = instance.spacing
    instance.spacing = original
    assert instance.spacing == original



@given(instance=di_Grid_strategy)
def test_di_grid_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=di_Grid_strategy)
def test_di_grid_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=di_Comment_strategy)
@settings(max_examples=50)
def test_di_comment_instantiation(instance):
    assert isinstance(instance, di_Comment)

@given(instance=Container_strategy)
@settings(max_examples=50)
def test_container_instantiation(instance):
    assert isinstance(instance, Container)

@given(instance=di_Diagram_strategy)
@settings(max_examples=50)
def test_di_diagram_instantiation(instance):
    assert isinstance(instance, di_Diagram)



@given(instance=di_Diagram_strategy)
def test_di_diagram_snapToGeometry_setter(instance):
    original = instance.snapToGeometry
    instance.snapToGeometry = original
    assert instance.snapToGeometry == original



@given(instance=di_Diagram_strategy)
def test_di_diagram_rulers_setter(instance):
    original = instance.rulers
    instance.rulers = original
    assert instance.rulers == original



@given(instance=di_Diagram_strategy)
def test_di_diagram_snapToGrid_setter(instance):
    original = instance.snapToGrid
    instance.snapToGrid = original
    assert instance.snapToGrid == original

@given(instance=di_Connector_strategy)
@settings(max_examples=50)
def test_di_connector_instantiation(instance):
    assert isinstance(instance, di_Connector)

@given(instance=di_Line_strategy)
@settings(max_examples=50)
def test_di_line_instantiation(instance):
    assert isinstance(instance, di_Line)



@given(instance=di_Line_strategy)
def test_di_line_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=di_Line_strategy)
def test_di_line_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=di_Line_strategy)
def test_di_line_sourceNode_setter(instance):
    original = instance.sourceNode
    instance.sourceNode = original
    assert instance.sourceNode == original



@given(instance=di_Line_strategy)
def test_di_line_targetAnchor_setter(instance):
    original = instance.targetAnchor
    instance.targetAnchor = original
    assert instance.targetAnchor == original



@given(instance=di_Line_strategy)
def test_di_line_lineDash_setter(instance):
    original = instance.lineDash
    instance.lineDash = original
    assert instance.lineDash == original



@given(instance=di_Line_strategy)
def test_di_line_targetNode_setter(instance):
    original = instance.targetNode
    instance.targetNode = original
    assert instance.targetNode == original



@given(instance=di_Line_strategy)
def test_di_line_sourceAnchor_setter(instance):
    original = instance.sourceAnchor
    instance.sourceAnchor = original
    assert instance.sourceAnchor == original



@given(instance=di_Line_strategy)
def test_di_line_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=di_Shape_strategy)
@settings(max_examples=50)
def test_di_shape_instantiation(instance):
    assert isinstance(instance, di_Shape)



@given(instance=di_Shape_strategy)
def test_di_shape_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=di_Shape_strategy)
def test_di_shape_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original



@given(instance=di_Shape_strategy)
def test_di_shape_foreground_setter(instance):
    original = instance.foreground
    instance.foreground = original
    assert instance.foreground == original

@given(instance=di_EObject_strategy)
@settings(max_examples=50)
def test_di_eobject_instantiation(instance):
    assert isinstance(instance, di_EObject)

@given(instance=di_View_strategy)
@settings(max_examples=50)
def test_di_view_instantiation(instance):
    assert isinstance(instance, di_View)



@given(instance=di_View_strategy)
def test_di_view_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=di_View_strategy)
def test_di_view_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=di_CommentLink_strategy)
@settings(max_examples=50)
def test_di_commentlink_instantiation(instance):
    assert isinstance(instance, di_CommentLink)

@given(instance=View_strategy)
@settings(max_examples=50)
def test_view_instantiation(instance):
    assert isinstance(instance, View)

@given(instance=di_Container_strategy)
@settings(max_examples=50)
def test_di_container_instantiation(instance):
    assert isinstance(instance, di_Container)



@given(instance=di_Container_strategy)
def test_di_container_allLines_setter(instance):
    original = instance.allLines
    instance.allLines = original
    assert instance.allLines == original



@given(instance=di_Container_strategy)
def test_di_container_allShapes_setter(instance):
    original = instance.allShapes
    instance.allShapes = original
    assert instance.allShapes == original

@given(instance=di_Node_strategy)
@settings(max_examples=50)
def test_di_node_instantiation(instance):
    assert isinstance(instance, di_Node)



@given(instance=di_Node_strategy)
def test_di_node_allIncomingLines_setter(instance):
    original = instance.allIncomingLines
    instance.allIncomingLines = original
    assert instance.allIncomingLines == original



@given(instance=di_Node_strategy)
def test_di_node_allOutgoingLines_setter(instance):
    original = instance.allOutgoingLines
    instance.allOutgoingLines = original
    assert instance.allOutgoingLines == original
