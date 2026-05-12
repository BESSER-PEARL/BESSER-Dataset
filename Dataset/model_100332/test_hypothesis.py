import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Label,
    pnmlcoremodel_Attribute,
    TransitionNode,
    pnmlcoremodel_Transition,
    PlaceNode,
    pnmlcoremodel_Place,
    pnmlcoremodel_RefTransition,
    pnmlcoremodel_RefPlace,
    Node,
    pnmlcoremodel_PlaceNode,
    pnmlcoremodel_TransitionNode,
    pnmlcoremodel_Annotation,
    pnmlcoremodel_Font,
    Coordinate,
    pnmlcoremodel_Offset,
    pnmlcoremodel_Coordinate,
    pnmlcoremodel_Graphics,
    pnmlcoremodel_Line,
    pnmlcoremodel_Fill,
    pnmlcoremodel_Dimension,
    pnmlcoremodel_Position,
    Graphics,
    pnmlcoremodel_ArcGraphics,
    pnmlcoremodel_AnnotationGraphics,
    pnmlcoremodel_AnyObject,
    pnmlcoremodel_Label,
    Annotation,
    pnmlcoremodel_NodeGraphics,
    pnmlcoremodel_PnObject,
    PnObject,
    pnmlcoremodel_Arc,
    pnmlcoremodel_Node,
    pnmlcoremodel_ToolInfo,
    pnmlcoremodel_Name,
    pnmlcoremodel_Page,
    pnmlcoremodel_PetriNet,
    pnmlcoremodel_PetriNetDoc,
    FontAlign,
    LineShape,
    CSS2FontStyle,
    CSS2FontFamily,
    FontDecoration,
    CSS2FontWeight,
    Gradient,
    CSS2Color,
    PNType,
    CSS2FontSize,
    LineStyle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_attribute_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Attribute)


def test_pnmlcoremodel_attribute_constructor_exists():
    assert callable(pnmlcoremodel_Attribute.__init__)


def test_pnmlcoremodel_attribute_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_transitionnode_is_not_abstract():
    assert not inspect.isabstract(TransitionNode)


def test_transitionnode_constructor_exists():
    assert callable(TransitionNode.__init__)


def test_transitionnode_constructor_args():
    sig = inspect.signature(TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_transition_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Transition)


def test_pnmlcoremodel_transition_constructor_exists():
    assert callable(pnmlcoremodel_Transition.__init__)


def test_pnmlcoremodel_transition_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Transition.__init__)
    params = list(sig.parameters.keys())



def test_placenode_is_not_abstract():
    assert not inspect.isabstract(PlaceNode)


def test_placenode_constructor_exists():
    assert callable(PlaceNode.__init__)


def test_placenode_constructor_args():
    sig = inspect.signature(PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_place_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Place)


def test_pnmlcoremodel_place_constructor_exists():
    assert callable(pnmlcoremodel_Place.__init__)


def test_pnmlcoremodel_place_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Place.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_reftransition_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_RefTransition)


def test_pnmlcoremodel_reftransition_constructor_exists():
    assert callable(pnmlcoremodel_RefTransition.__init__)


def test_pnmlcoremodel_reftransition_constructor_args():
    sig = inspect.signature(pnmlcoremodel_RefTransition.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_refplace_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_RefPlace)


def test_pnmlcoremodel_refplace_constructor_exists():
    assert callable(pnmlcoremodel_RefPlace.__init__)


def test_pnmlcoremodel_refplace_constructor_args():
    sig = inspect.signature(pnmlcoremodel_RefPlace.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_placenode_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_PlaceNode)


def test_pnmlcoremodel_placenode_constructor_exists():
    assert callable(pnmlcoremodel_PlaceNode.__init__)


def test_pnmlcoremodel_placenode_constructor_args():
    sig = inspect.signature(pnmlcoremodel_PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_transitionnode_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_TransitionNode)


def test_pnmlcoremodel_transitionnode_constructor_exists():
    assert callable(pnmlcoremodel_TransitionNode.__init__)


def test_pnmlcoremodel_transitionnode_constructor_args():
    sig = inspect.signature(pnmlcoremodel_TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_annotation_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Annotation)


def test_pnmlcoremodel_annotation_constructor_exists():
    assert callable(pnmlcoremodel_Annotation.__init__)


def test_pnmlcoremodel_annotation_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_font_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Font)


def test_pnmlcoremodel_font_constructor_exists():
    assert callable(pnmlcoremodel_Font.__init__)


def test_pnmlcoremodel_font_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Font.__init__)
    params = list(sig.parameters.keys())
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "decoration" in params, "Missing parameter 'decoration'"
    assert "family" in params, "Missing parameter 'family'"
    assert "style" in params, "Missing parameter 'style'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "size" in params, "Missing parameter 'size'"
    assert "align" in params, "Missing parameter 'align'"

def test_pnmlcoremodel_font_has_rotation():
    assert hasattr(pnmlcoremodel_Font, "rotation")
    descriptor = None
    for klass in pnmlcoremodel_Font.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_font_has_decoration():
    assert hasattr(pnmlcoremodel_Font, "decoration")
    descriptor = None
    for klass in pnmlcoremodel_Font.__mro__:
        if "decoration" in klass.__dict__:
            descriptor = klass.__dict__["decoration"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_font_has_family():
    assert hasattr(pnmlcoremodel_Font, "family")
    descriptor = None
    for klass in pnmlcoremodel_Font.__mro__:
        if "family" in klass.__dict__:
            descriptor = klass.__dict__["family"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_font_has_style():
    assert hasattr(pnmlcoremodel_Font, "style")
    descriptor = None
    for klass in pnmlcoremodel_Font.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_font_has_weight():
    assert hasattr(pnmlcoremodel_Font, "weight")
    descriptor = None
    for klass in pnmlcoremodel_Font.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_font_has_size():
    assert hasattr(pnmlcoremodel_Font, "size")
    descriptor = None
    for klass in pnmlcoremodel_Font.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_font_has_align():
    assert hasattr(pnmlcoremodel_Font, "align")
    descriptor = None
    for klass in pnmlcoremodel_Font.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_coordinate_is_not_abstract():
    assert not inspect.isabstract(Coordinate)


def test_coordinate_constructor_exists():
    assert callable(Coordinate.__init__)


def test_coordinate_constructor_args():
    sig = inspect.signature(Coordinate.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_offset_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Offset)


def test_pnmlcoremodel_offset_constructor_exists():
    assert callable(pnmlcoremodel_Offset.__init__)


def test_pnmlcoremodel_offset_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Offset.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_coordinate_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Coordinate)


def test_pnmlcoremodel_coordinate_constructor_exists():
    assert callable(pnmlcoremodel_Coordinate.__init__)


def test_pnmlcoremodel_coordinate_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_pnmlcoremodel_coordinate_has_x():
    assert hasattr(pnmlcoremodel_Coordinate, "x")
    descriptor = None
    for klass in pnmlcoremodel_Coordinate.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_coordinate_has_y():
    assert hasattr(pnmlcoremodel_Coordinate, "y")
    descriptor = None
    for klass in pnmlcoremodel_Coordinate.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_pnmlcoremodel_graphics_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Graphics)


def test_pnmlcoremodel_graphics_constructor_exists():
    assert callable(pnmlcoremodel_Graphics.__init__)


def test_pnmlcoremodel_graphics_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Graphics.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_line_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Line)


def test_pnmlcoremodel_line_constructor_exists():
    assert callable(pnmlcoremodel_Line.__init__)


def test_pnmlcoremodel_line_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Line.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "style" in params, "Missing parameter 'style'"
    assert "color" in params, "Missing parameter 'color'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_pnmlcoremodel_line_has_width():
    assert hasattr(pnmlcoremodel_Line, "width")
    descriptor = None
    for klass in pnmlcoremodel_Line.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_line_has_style():
    assert hasattr(pnmlcoremodel_Line, "style")
    descriptor = None
    for klass in pnmlcoremodel_Line.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_line_has_color():
    assert hasattr(pnmlcoremodel_Line, "color")
    descriptor = None
    for klass in pnmlcoremodel_Line.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_line_has_shape():
    assert hasattr(pnmlcoremodel_Line, "shape")
    descriptor = None
    for klass in pnmlcoremodel_Line.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_pnmlcoremodel_fill_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Fill)


def test_pnmlcoremodel_fill_constructor_exists():
    assert callable(pnmlcoremodel_Fill.__init__)


def test_pnmlcoremodel_fill_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Fill.__init__)
    params = list(sig.parameters.keys())
    assert "gradientcolor" in params, "Missing parameter 'gradientcolor'"
    assert "image" in params, "Missing parameter 'image'"
    assert "gradientrotation" in params, "Missing parameter 'gradientrotation'"
    assert "color" in params, "Missing parameter 'color'"

def test_pnmlcoremodel_fill_has_gradientcolor():
    assert hasattr(pnmlcoremodel_Fill, "gradientcolor")
    descriptor = None
    for klass in pnmlcoremodel_Fill.__mro__:
        if "gradientcolor" in klass.__dict__:
            descriptor = klass.__dict__["gradientcolor"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_fill_has_image():
    assert hasattr(pnmlcoremodel_Fill, "image")
    descriptor = None
    for klass in pnmlcoremodel_Fill.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_fill_has_gradientrotation():
    assert hasattr(pnmlcoremodel_Fill, "gradientrotation")
    descriptor = None
    for klass in pnmlcoremodel_Fill.__mro__:
        if "gradientrotation" in klass.__dict__:
            descriptor = klass.__dict__["gradientrotation"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_fill_has_color():
    assert hasattr(pnmlcoremodel_Fill, "color")
    descriptor = None
    for klass in pnmlcoremodel_Fill.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_pnmlcoremodel_dimension_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Dimension)


def test_pnmlcoremodel_dimension_constructor_exists():
    assert callable(pnmlcoremodel_Dimension.__init__)


def test_pnmlcoremodel_dimension_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Dimension.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_position_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Position)


def test_pnmlcoremodel_position_constructor_exists():
    assert callable(pnmlcoremodel_Position.__init__)


def test_pnmlcoremodel_position_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Position.__init__)
    params = list(sig.parameters.keys())



def test_graphics_is_not_abstract():
    assert not inspect.isabstract(Graphics)


def test_graphics_constructor_exists():
    assert callable(Graphics.__init__)


def test_graphics_constructor_args():
    sig = inspect.signature(Graphics.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_arcgraphics_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_ArcGraphics)


def test_pnmlcoremodel_arcgraphics_constructor_exists():
    assert callable(pnmlcoremodel_ArcGraphics.__init__)


def test_pnmlcoremodel_arcgraphics_constructor_args():
    sig = inspect.signature(pnmlcoremodel_ArcGraphics.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_annotationgraphics_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_AnnotationGraphics)


def test_pnmlcoremodel_annotationgraphics_constructor_exists():
    assert callable(pnmlcoremodel_AnnotationGraphics.__init__)


def test_pnmlcoremodel_annotationgraphics_constructor_args():
    sig = inspect.signature(pnmlcoremodel_AnnotationGraphics.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_anyobject_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_AnyObject)


def test_pnmlcoremodel_anyobject_constructor_exists():
    assert callable(pnmlcoremodel_AnyObject.__init__)


def test_pnmlcoremodel_anyobject_constructor_args():
    sig = inspect.signature(pnmlcoremodel_AnyObject.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_label_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Label)


def test_pnmlcoremodel_label_constructor_exists():
    assert callable(pnmlcoremodel_Label.__init__)


def test_pnmlcoremodel_label_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Label.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_nodegraphics_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_NodeGraphics)


def test_pnmlcoremodel_nodegraphics_constructor_exists():
    assert callable(pnmlcoremodel_NodeGraphics.__init__)


def test_pnmlcoremodel_nodegraphics_constructor_args():
    sig = inspect.signature(pnmlcoremodel_NodeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_pnobject_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_PnObject)


def test_pnmlcoremodel_pnobject_constructor_exists():
    assert callable(pnmlcoremodel_PnObject.__init__)


def test_pnmlcoremodel_pnobject_constructor_args():
    sig = inspect.signature(pnmlcoremodel_PnObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_pnmlcoremodel_pnobject_has_id():
    assert hasattr(pnmlcoremodel_PnObject, "id")
    descriptor = None
    for klass in pnmlcoremodel_PnObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_pnobject_is_not_abstract():
    assert not inspect.isabstract(PnObject)


def test_pnobject_constructor_exists():
    assert callable(PnObject.__init__)


def test_pnobject_constructor_args():
    sig = inspect.signature(PnObject.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_arc_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Arc)


def test_pnmlcoremodel_arc_constructor_exists():
    assert callable(pnmlcoremodel_Arc.__init__)


def test_pnmlcoremodel_arc_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Arc.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_node_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Node)


def test_pnmlcoremodel_node_constructor_exists():
    assert callable(pnmlcoremodel_Node.__init__)


def test_pnmlcoremodel_node_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Node.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_toolinfo_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_ToolInfo)


def test_pnmlcoremodel_toolinfo_constructor_exists():
    assert callable(pnmlcoremodel_ToolInfo.__init__)


def test_pnmlcoremodel_toolinfo_constructor_args():
    sig = inspect.signature(pnmlcoremodel_ToolInfo.__init__)
    params = list(sig.parameters.keys())
    assert "formattedXMLBuffer" in params, "Missing parameter 'formattedXMLBuffer'"
    assert "tool" in params, "Missing parameter 'tool'"
    assert "toolInfoGrammarURI" in params, "Missing parameter 'toolInfoGrammarURI'"
    assert "version" in params, "Missing parameter 'version'"

def test_pnmlcoremodel_toolinfo_has_formattedXMLBuffer():
    assert hasattr(pnmlcoremodel_ToolInfo, "formattedXMLBuffer")
    descriptor = None
    for klass in pnmlcoremodel_ToolInfo.__mro__:
        if "formattedXMLBuffer" in klass.__dict__:
            descriptor = klass.__dict__["formattedXMLBuffer"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_toolinfo_has_tool():
    assert hasattr(pnmlcoremodel_ToolInfo, "tool")
    descriptor = None
    for klass in pnmlcoremodel_ToolInfo.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_toolinfo_has_toolInfoGrammarURI():
    assert hasattr(pnmlcoremodel_ToolInfo, "toolInfoGrammarURI")
    descriptor = None
    for klass in pnmlcoremodel_ToolInfo.__mro__:
        if "toolInfoGrammarURI" in klass.__dict__:
            descriptor = klass.__dict__["toolInfoGrammarURI"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_toolinfo_has_version():
    assert hasattr(pnmlcoremodel_ToolInfo, "version")
    descriptor = None
    for klass in pnmlcoremodel_ToolInfo.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_pnmlcoremodel_name_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Name)


def test_pnmlcoremodel_name_constructor_exists():
    assert callable(pnmlcoremodel_Name.__init__)


def test_pnmlcoremodel_name_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Name.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_pnmlcoremodel_name_has_text():
    assert hasattr(pnmlcoremodel_Name, "text")
    descriptor = None
    for klass in pnmlcoremodel_Name.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_pnmlcoremodel_page_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Page)


def test_pnmlcoremodel_page_constructor_exists():
    assert callable(pnmlcoremodel_Page.__init__)


def test_pnmlcoremodel_page_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Page.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel_petrinet_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_PetriNet)


def test_pnmlcoremodel_petrinet_constructor_exists():
    assert callable(pnmlcoremodel_PetriNet.__init__)


def test_pnmlcoremodel_petrinet_constructor_args():
    sig = inspect.signature(pnmlcoremodel_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

def test_pnmlcoremodel_petrinet_has_type():
    assert hasattr(pnmlcoremodel_PetriNet, "type")
    descriptor = None
    for klass in pnmlcoremodel_PetriNet.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel_petrinet_has_id():
    assert hasattr(pnmlcoremodel_PetriNet, "id")
    descriptor = None
    for klass in pnmlcoremodel_PetriNet.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_pnmlcoremodel_petrinetdoc_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_PetriNetDoc)


def test_pnmlcoremodel_petrinetdoc_constructor_exists():
    assert callable(pnmlcoremodel_PetriNetDoc.__init__)


def test_pnmlcoremodel_petrinetdoc_constructor_args():
    sig = inspect.signature(pnmlcoremodel_PetriNetDoc.__init__)
    params = list(sig.parameters.keys())
    assert "xmlns" in params, "Missing parameter 'xmlns'"

def test_pnmlcoremodel_petrinetdoc_has_xmlns():
    assert hasattr(pnmlcoremodel_PetriNetDoc, "xmlns")
    descriptor = None
    for klass in pnmlcoremodel_PetriNetDoc.__mro__:
        if "xmlns" in klass.__dict__:
            descriptor = klass.__dict__["xmlns"]
            break
    assert isinstance(descriptor, property)

def test_fontalign_exists():
    # Check that the Enumeration exists
    assert FontAlign is not None

def test_fontalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontAlign]
    expected_literals = [
        "LEFT",
        "CENTER",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontAlign"

def test_lineshape_exists():
    # Check that the Enumeration exists
    assert LineShape is not None

def test_lineshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineShape]
    expected_literals = [
        "CURVE",
        "LINE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineShape"

def test_css2fontstyle_exists():
    # Check that the Enumeration exists
    assert CSS2FontStyle is not None

def test_css2fontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontStyle]
    expected_literals = [
        "OBLIQUE",
        "NORMAL",
        "ITALIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontStyle"

def test_css2fontfamily_exists():
    # Check that the Enumeration exists
    assert CSS2FontFamily is not None

def test_css2fontfamily_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontFamily]
    expected_literals = [
        "GEORGIA",
        "TIMES",
        "ARIAL",
        "VERDANA",
        "TREBUCHET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontFamily"

def test_fontdecoration_exists():
    # Check that the Enumeration exists
    assert FontDecoration is not None

def test_fontdecoration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontDecoration]
    expected_literals = [
        "LINETHROUGH",
        "OVERLINE",
        "UNDERLINE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontDecoration"

def test_css2fontweight_exists():
    # Check that the Enumeration exists
    assert CSS2FontWeight is not None

def test_css2fontweight_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontWeight]
    expected_literals = [
        "BOLD",
        "LIGHTER",
        "BOLDER",
        "NORMAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontWeight"

def test_gradient_exists():
    # Check that the Enumeration exists
    assert Gradient is not None

def test_gradient_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gradient]
    expected_literals = [
        "DIAGONAL",
        "VERTICAL",
        "HORIZONTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gradient"

def test_css2color_exists():
    # Check that the Enumeration exists
    assert CSS2Color is not None

def test_css2color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2Color]
    expected_literals = [
        "BLUE",
        "FUCHSIA",
        "NAVY",
        "PURPLE",
        "MAROON",
        "SILVER",
        "TEAL",
        "GREEN",
        "YELLOW",
        "LIME",
        "GRAY",
        "ORANGE",
        "RED",
        "BLACK",
        "OLIVE",
        "WHITE",
        "AQUA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2Color"

def test_pntype_exists():
    # Check that the Enumeration exists
    assert PNType is not None

def test_pntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PNType]
    expected_literals = [
        "COREMODEL",
        "SYMNET",
        "HLPN",
        "PTNET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PNType"

def test_css2fontsize_exists():
    # Check that the Enumeration exists
    assert CSS2FontSize is not None

def test_css2fontsize_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontSize]
    expected_literals = [
        "XSMALL",
        "LARGE",
        "XXLARGE",
        "MEDIUM",
        "SMALL",
        "XLARGE",
        "XXSMALL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontSize"

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
Label_strategy = st.builds(
    Label,
)
pnmlcoremodel_Attribute_strategy = st.builds(
    pnmlcoremodel_Attribute,
)
TransitionNode_strategy = st.builds(
    TransitionNode,
)
pnmlcoremodel_Transition_strategy = st.builds(
    pnmlcoremodel_Transition,
)
PlaceNode_strategy = st.builds(
    PlaceNode,
)
pnmlcoremodel_Place_strategy = st.builds(
    pnmlcoremodel_Place,
)
pnmlcoremodel_RefTransition_strategy = st.builds(
    pnmlcoremodel_RefTransition,
)
pnmlcoremodel_RefPlace_strategy = st.builds(
    pnmlcoremodel_RefPlace,
)
Node_strategy = st.builds(
    Node,
)
pnmlcoremodel_PlaceNode_strategy = st.builds(
    pnmlcoremodel_PlaceNode,
)
pnmlcoremodel_TransitionNode_strategy = st.builds(
    pnmlcoremodel_TransitionNode,
)
pnmlcoremodel_Annotation_strategy = st.builds(
    pnmlcoremodel_Annotation,
)
pnmlcoremodel_Font_strategy = st.builds(
    pnmlcoremodel_Font,
    rotation=
        safe_text,
    decoration=
        safe_text,
    family=
        safe_text,
    style=
        safe_text,
    weight=
        safe_text,
    size=
        safe_text,
    align=
        safe_text
)
Coordinate_strategy = st.builds(
    Coordinate,
)
pnmlcoremodel_Offset_strategy = st.builds(
    pnmlcoremodel_Offset,
)
pnmlcoremodel_Coordinate_strategy = st.builds(
    pnmlcoremodel_Coordinate,
    x=
        safe_text,
    y=
        safe_text
)
pnmlcoremodel_Graphics_strategy = st.builds(
    pnmlcoremodel_Graphics,
)
pnmlcoremodel_Line_strategy = st.builds(
    pnmlcoremodel_Line,
    width=
        safe_text,
    style=
        safe_text,
    color=
        safe_text,
    shape=
        safe_text
)
pnmlcoremodel_Fill_strategy = st.builds(
    pnmlcoremodel_Fill,
    gradientcolor=
        safe_text,
    image=
        safe_text,
    gradientrotation=
        safe_text,
    color=
        safe_text
)
pnmlcoremodel_Dimension_strategy = st.builds(
    pnmlcoremodel_Dimension,
)
pnmlcoremodel_Position_strategy = st.builds(
    pnmlcoremodel_Position,
)
Graphics_strategy = st.builds(
    Graphics,
)
pnmlcoremodel_ArcGraphics_strategy = st.builds(
    pnmlcoremodel_ArcGraphics,
)
pnmlcoremodel_AnnotationGraphics_strategy = st.builds(
    pnmlcoremodel_AnnotationGraphics,
)
pnmlcoremodel_AnyObject_strategy = st.builds(
    pnmlcoremodel_AnyObject,
)
pnmlcoremodel_Label_strategy = st.builds(
    pnmlcoremodel_Label,
)
Annotation_strategy = st.builds(
    Annotation,
)
pnmlcoremodel_NodeGraphics_strategy = st.builds(
    pnmlcoremodel_NodeGraphics,
)
pnmlcoremodel_PnObject_strategy = st.builds(
    pnmlcoremodel_PnObject,
    id=
        safe_text
)
PnObject_strategy = st.builds(
    PnObject,
)
pnmlcoremodel_Arc_strategy = st.builds(
    pnmlcoremodel_Arc,
)
pnmlcoremodel_Node_strategy = st.builds(
    pnmlcoremodel_Node,
)
pnmlcoremodel_ToolInfo_strategy = st.builds(
    pnmlcoremodel_ToolInfo,
    formattedXMLBuffer=
        safe_text,
    tool=
        safe_text,
    toolInfoGrammarURI=
        safe_text,
    version=
        safe_text
)
pnmlcoremodel_Name_strategy = st.builds(
    pnmlcoremodel_Name,
    text=
        safe_text
)
pnmlcoremodel_Page_strategy = st.builds(
    pnmlcoremodel_Page,
)
pnmlcoremodel_PetriNet_strategy = st.builds(
    pnmlcoremodel_PetriNet,
    type=
        safe_text,
    id=
        safe_text
)
pnmlcoremodel_PetriNetDoc_strategy = st.builds(
    pnmlcoremodel_PetriNetDoc,
    xmlns=
        safe_text
)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=pnmlcoremodel_Attribute_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_attribute_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Attribute)

@given(instance=TransitionNode_strategy)
@settings(max_examples=50)
def test_transitionnode_instantiation(instance):
    assert isinstance(instance, TransitionNode)

@given(instance=pnmlcoremodel_Transition_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_transition_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Transition)

@given(instance=PlaceNode_strategy)
@settings(max_examples=50)
def test_placenode_instantiation(instance):
    assert isinstance(instance, PlaceNode)

@given(instance=pnmlcoremodel_Place_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_place_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Place)

@given(instance=pnmlcoremodel_RefTransition_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_reftransition_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_RefTransition)

@given(instance=pnmlcoremodel_RefPlace_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_refplace_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_RefPlace)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=pnmlcoremodel_PlaceNode_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_placenode_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_PlaceNode)

@given(instance=pnmlcoremodel_TransitionNode_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_transitionnode_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_TransitionNode)

@given(instance=pnmlcoremodel_Annotation_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_annotation_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Annotation)

@given(instance=pnmlcoremodel_Font_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_font_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Font)



@given(instance=pnmlcoremodel_Font_strategy)
def test_pnmlcoremodel_font_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=pnmlcoremodel_Font_strategy)
def test_pnmlcoremodel_font_decoration_setter(instance):
    original = instance.decoration
    instance.decoration = original
    assert instance.decoration == original



@given(instance=pnmlcoremodel_Font_strategy)
def test_pnmlcoremodel_font_family_setter(instance):
    original = instance.family
    instance.family = original
    assert instance.family == original



@given(instance=pnmlcoremodel_Font_strategy)
def test_pnmlcoremodel_font_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=pnmlcoremodel_Font_strategy)
def test_pnmlcoremodel_font_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=pnmlcoremodel_Font_strategy)
def test_pnmlcoremodel_font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=pnmlcoremodel_Font_strategy)
def test_pnmlcoremodel_font_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=Coordinate_strategy)
@settings(max_examples=50)
def test_coordinate_instantiation(instance):
    assert isinstance(instance, Coordinate)

@given(instance=pnmlcoremodel_Offset_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_offset_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Offset)

@given(instance=pnmlcoremodel_Coordinate_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_coordinate_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Coordinate)



@given(instance=pnmlcoremodel_Coordinate_strategy)
def test_pnmlcoremodel_coordinate_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=pnmlcoremodel_Coordinate_strategy)
def test_pnmlcoremodel_coordinate_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=pnmlcoremodel_Graphics_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_graphics_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Graphics)

@given(instance=pnmlcoremodel_Line_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_line_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Line)



@given(instance=pnmlcoremodel_Line_strategy)
def test_pnmlcoremodel_line_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=pnmlcoremodel_Line_strategy)
def test_pnmlcoremodel_line_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=pnmlcoremodel_Line_strategy)
def test_pnmlcoremodel_line_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=pnmlcoremodel_Line_strategy)
def test_pnmlcoremodel_line_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=pnmlcoremodel_Fill_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_fill_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Fill)



@given(instance=pnmlcoremodel_Fill_strategy)
def test_pnmlcoremodel_fill_gradientcolor_setter(instance):
    original = instance.gradientcolor
    instance.gradientcolor = original
    assert instance.gradientcolor == original



@given(instance=pnmlcoremodel_Fill_strategy)
def test_pnmlcoremodel_fill_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=pnmlcoremodel_Fill_strategy)
def test_pnmlcoremodel_fill_gradientrotation_setter(instance):
    original = instance.gradientrotation
    instance.gradientrotation = original
    assert instance.gradientrotation == original



@given(instance=pnmlcoremodel_Fill_strategy)
def test_pnmlcoremodel_fill_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=pnmlcoremodel_Dimension_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_dimension_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Dimension)

@given(instance=pnmlcoremodel_Position_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_position_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Position)

@given(instance=Graphics_strategy)
@settings(max_examples=50)
def test_graphics_instantiation(instance):
    assert isinstance(instance, Graphics)

@given(instance=pnmlcoremodel_ArcGraphics_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_arcgraphics_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_ArcGraphics)

@given(instance=pnmlcoremodel_AnnotationGraphics_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_annotationgraphics_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_AnnotationGraphics)

@given(instance=pnmlcoremodel_AnyObject_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_anyobject_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_AnyObject)

@given(instance=pnmlcoremodel_Label_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_label_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Label)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=pnmlcoremodel_NodeGraphics_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_nodegraphics_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_NodeGraphics)

@given(instance=pnmlcoremodel_PnObject_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_pnobject_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_PnObject)



@given(instance=pnmlcoremodel_PnObject_strategy)
def test_pnmlcoremodel_pnobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=PnObject_strategy)
@settings(max_examples=50)
def test_pnobject_instantiation(instance):
    assert isinstance(instance, PnObject)

@given(instance=pnmlcoremodel_Arc_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_arc_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Arc)

@given(instance=pnmlcoremodel_Node_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_node_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Node)

@given(instance=pnmlcoremodel_ToolInfo_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_toolinfo_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_ToolInfo)



@given(instance=pnmlcoremodel_ToolInfo_strategy)
def test_pnmlcoremodel_toolinfo_formattedXMLBuffer_setter(instance):
    original = instance.formattedXMLBuffer
    instance.formattedXMLBuffer = original
    assert instance.formattedXMLBuffer == original



@given(instance=pnmlcoremodel_ToolInfo_strategy)
def test_pnmlcoremodel_toolinfo_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original



@given(instance=pnmlcoremodel_ToolInfo_strategy)
def test_pnmlcoremodel_toolinfo_toolInfoGrammarURI_setter(instance):
    original = instance.toolInfoGrammarURI
    instance.toolInfoGrammarURI = original
    assert instance.toolInfoGrammarURI == original



@given(instance=pnmlcoremodel_ToolInfo_strategy)
def test_pnmlcoremodel_toolinfo_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=pnmlcoremodel_Name_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_name_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Name)



@given(instance=pnmlcoremodel_Name_strategy)
def test_pnmlcoremodel_name_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=pnmlcoremodel_Page_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_page_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Page)

@given(instance=pnmlcoremodel_PetriNet_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_petrinet_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_PetriNet)



@given(instance=pnmlcoremodel_PetriNet_strategy)
def test_pnmlcoremodel_petrinet_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=pnmlcoremodel_PetriNet_strategy)
def test_pnmlcoremodel_petrinet_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=pnmlcoremodel_PetriNetDoc_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel_petrinetdoc_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_PetriNetDoc)



@given(instance=pnmlcoremodel_PetriNetDoc_strategy)
def test_pnmlcoremodel_petrinetdoc_xmlns_setter(instance):
    original = instance.xmlns
    instance.xmlns = original
    assert instance.xmlns == original
