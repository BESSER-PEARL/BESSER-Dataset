import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    pnmlcoremodel::PetriNetDoc,
    PlaceNode,
    pnmlcoremodel::Place,
    pnmlcoremodel::RefPlace,
    Node,
    pnmlcoremodel::TransitionNode,
    pnmlcoremodel::PlaceNode,
    Label,
    pnmlcoremodel::Attribute,
    TransitionNode,
    pnmlcoremodel::Transition,
    pnmlcoremodel::RefTransition,
    pnmlcoremodel::Annotation,
    pnmlcoremodel::Font,
    pnmlcoremodel::Fill,
    Graphics,
    pnmlcoremodel::AnyObject,
    pnmlcoremodel::Label,
    pnmlcoremodel::AnnotationGraphics,
    pnmlcoremodel::ArcGraphics,
    Coordinate,
    pnmlcoremodel::Offset,
    pnmlcoremodel::Dimension,
    pnmlcoremodel::Position,
    pnmlcoremodel::Coordinate,
    pnmlcoremodel::Graphics,
    pnmlcoremodel::Line,
    pnmlcoremodel::PnObject,
    PnObject,
    pnmlcoremodel::Node,
    pnmlcoremodel::Arc,
    pnmlcoremodel::ToolInfo,
    pnmlcoremodel::Page,
    Annotation,
    pnmlcoremodel::Name,
    pnmlcoremodel::NodeGraphics,
    pnmlcoremodel::PetriNet,
    LineShape,
    CSS2FontStyle,
    PNType,
    LineStyle,
    FontDecoration,
    Gradient,
    CSS2FontSize,
    CSS2Color,
    FontAlign,
    CSS2FontWeight,
    CSS2FontFamily,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pnmlcoremodel::petrinetdoc_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::PetriNetDoc)


def test_pnmlcoremodel::petrinetdoc_constructor_exists():
    assert callable(pnmlcoremodel::PetriNetDoc.__init__)


def test_pnmlcoremodel::petrinetdoc_constructor_args():
    sig = inspect.signature(pnmlcoremodel::PetriNetDoc.__init__)
    params = list(sig.parameters.keys())
    assert "xmlns" in params, "Missing parameter 'xmlns'"

def test_pnmlcoremodel::petrinetdoc_has_xmlns():
    assert hasattr(pnmlcoremodel::PetriNetDoc, "xmlns")
    descriptor = None
    for klass in pnmlcoremodel::PetriNetDoc.__mro__:
        if "xmlns" in klass.__dict__:
            descriptor = klass.__dict__["xmlns"]
            break
    assert isinstance(descriptor, property)



def test_placenode_is_not_abstract():
    assert not inspect.isabstract(PlaceNode)


def test_placenode_constructor_exists():
    assert callable(PlaceNode.__init__)


def test_placenode_constructor_args():
    sig = inspect.signature(PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::place_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Place)


def test_pnmlcoremodel::place_constructor_exists():
    assert callable(pnmlcoremodel::Place.__init__)


def test_pnmlcoremodel::place_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Place.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::refplace_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::RefPlace)


def test_pnmlcoremodel::refplace_constructor_exists():
    assert callable(pnmlcoremodel::RefPlace.__init__)


def test_pnmlcoremodel::refplace_constructor_args():
    sig = inspect.signature(pnmlcoremodel::RefPlace.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::transitionnode_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::TransitionNode)


def test_pnmlcoremodel::transitionnode_constructor_exists():
    assert callable(pnmlcoremodel::TransitionNode.__init__)


def test_pnmlcoremodel::transitionnode_constructor_args():
    sig = inspect.signature(pnmlcoremodel::TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::placenode_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::PlaceNode)


def test_pnmlcoremodel::placenode_constructor_exists():
    assert callable(pnmlcoremodel::PlaceNode.__init__)


def test_pnmlcoremodel::placenode_constructor_args():
    sig = inspect.signature(pnmlcoremodel::PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::attribute_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Attribute)


def test_pnmlcoremodel::attribute_constructor_exists():
    assert callable(pnmlcoremodel::Attribute.__init__)


def test_pnmlcoremodel::attribute_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_transitionnode_is_not_abstract():
    assert not inspect.isabstract(TransitionNode)


def test_transitionnode_constructor_exists():
    assert callable(TransitionNode.__init__)


def test_transitionnode_constructor_args():
    sig = inspect.signature(TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::transition_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Transition)


def test_pnmlcoremodel::transition_constructor_exists():
    assert callable(pnmlcoremodel::Transition.__init__)


def test_pnmlcoremodel::transition_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Transition.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::reftransition_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::RefTransition)


def test_pnmlcoremodel::reftransition_constructor_exists():
    assert callable(pnmlcoremodel::RefTransition.__init__)


def test_pnmlcoremodel::reftransition_constructor_args():
    sig = inspect.signature(pnmlcoremodel::RefTransition.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::annotation_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Annotation)


def test_pnmlcoremodel::annotation_constructor_exists():
    assert callable(pnmlcoremodel::Annotation.__init__)


def test_pnmlcoremodel::annotation_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::font_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Font)


def test_pnmlcoremodel::font_constructor_exists():
    assert callable(pnmlcoremodel::Font.__init__)


def test_pnmlcoremodel::font_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Font.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "align" in params, "Missing parameter 'align'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "size" in params, "Missing parameter 'size'"
    assert "decoration" in params, "Missing parameter 'decoration'"
    assert "family" in params, "Missing parameter 'family'"
    assert "rotation" in params, "Missing parameter 'rotation'"

def test_pnmlcoremodel::font_has_style():
    assert hasattr(pnmlcoremodel::Font, "style")
    descriptor = None
    for klass in pnmlcoremodel::Font.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::font_has_align():
    assert hasattr(pnmlcoremodel::Font, "align")
    descriptor = None
    for klass in pnmlcoremodel::Font.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::font_has_weight():
    assert hasattr(pnmlcoremodel::Font, "weight")
    descriptor = None
    for klass in pnmlcoremodel::Font.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::font_has_size():
    assert hasattr(pnmlcoremodel::Font, "size")
    descriptor = None
    for klass in pnmlcoremodel::Font.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::font_has_decoration():
    assert hasattr(pnmlcoremodel::Font, "decoration")
    descriptor = None
    for klass in pnmlcoremodel::Font.__mro__:
        if "decoration" in klass.__dict__:
            descriptor = klass.__dict__["decoration"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::font_has_family():
    assert hasattr(pnmlcoremodel::Font, "family")
    descriptor = None
    for klass in pnmlcoremodel::Font.__mro__:
        if "family" in klass.__dict__:
            descriptor = klass.__dict__["family"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::font_has_rotation():
    assert hasattr(pnmlcoremodel::Font, "rotation")
    descriptor = None
    for klass in pnmlcoremodel::Font.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)



def test_pnmlcoremodel::fill_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Fill)


def test_pnmlcoremodel::fill_constructor_exists():
    assert callable(pnmlcoremodel::Fill.__init__)


def test_pnmlcoremodel::fill_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Fill.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "gradientrotation" in params, "Missing parameter 'gradientrotation'"
    assert "image" in params, "Missing parameter 'image'"
    assert "gradientcolor" in params, "Missing parameter 'gradientcolor'"

def test_pnmlcoremodel::fill_has_color():
    assert hasattr(pnmlcoremodel::Fill, "color")
    descriptor = None
    for klass in pnmlcoremodel::Fill.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::fill_has_gradientrotation():
    assert hasattr(pnmlcoremodel::Fill, "gradientrotation")
    descriptor = None
    for klass in pnmlcoremodel::Fill.__mro__:
        if "gradientrotation" in klass.__dict__:
            descriptor = klass.__dict__["gradientrotation"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::fill_has_image():
    assert hasattr(pnmlcoremodel::Fill, "image")
    descriptor = None
    for klass in pnmlcoremodel::Fill.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::fill_has_gradientcolor():
    assert hasattr(pnmlcoremodel::Fill, "gradientcolor")
    descriptor = None
    for klass in pnmlcoremodel::Fill.__mro__:
        if "gradientcolor" in klass.__dict__:
            descriptor = klass.__dict__["gradientcolor"]
            break
    assert isinstance(descriptor, property)



def test_graphics_is_not_abstract():
    assert not inspect.isabstract(Graphics)


def test_graphics_constructor_exists():
    assert callable(Graphics.__init__)


def test_graphics_constructor_args():
    sig = inspect.signature(Graphics.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::anyobject_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::AnyObject)


def test_pnmlcoremodel::anyobject_constructor_exists():
    assert callable(pnmlcoremodel::AnyObject.__init__)


def test_pnmlcoremodel::anyobject_constructor_args():
    sig = inspect.signature(pnmlcoremodel::AnyObject.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::label_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Label)


def test_pnmlcoremodel::label_constructor_exists():
    assert callable(pnmlcoremodel::Label.__init__)


def test_pnmlcoremodel::label_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Label.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::annotationgraphics_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::AnnotationGraphics)


def test_pnmlcoremodel::annotationgraphics_constructor_exists():
    assert callable(pnmlcoremodel::AnnotationGraphics.__init__)


def test_pnmlcoremodel::annotationgraphics_constructor_args():
    sig = inspect.signature(pnmlcoremodel::AnnotationGraphics.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::arcgraphics_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::ArcGraphics)


def test_pnmlcoremodel::arcgraphics_constructor_exists():
    assert callable(pnmlcoremodel::ArcGraphics.__init__)


def test_pnmlcoremodel::arcgraphics_constructor_args():
    sig = inspect.signature(pnmlcoremodel::ArcGraphics.__init__)
    params = list(sig.parameters.keys())



def test_coordinate_is_not_abstract():
    assert not inspect.isabstract(Coordinate)


def test_coordinate_constructor_exists():
    assert callable(Coordinate.__init__)


def test_coordinate_constructor_args():
    sig = inspect.signature(Coordinate.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::offset_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Offset)


def test_pnmlcoremodel::offset_constructor_exists():
    assert callable(pnmlcoremodel::Offset.__init__)


def test_pnmlcoremodel::offset_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Offset.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::dimension_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Dimension)


def test_pnmlcoremodel::dimension_constructor_exists():
    assert callable(pnmlcoremodel::Dimension.__init__)


def test_pnmlcoremodel::dimension_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Dimension.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::position_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Position)


def test_pnmlcoremodel::position_constructor_exists():
    assert callable(pnmlcoremodel::Position.__init__)


def test_pnmlcoremodel::position_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Position.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::coordinate_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Coordinate)


def test_pnmlcoremodel::coordinate_constructor_exists():
    assert callable(pnmlcoremodel::Coordinate.__init__)


def test_pnmlcoremodel::coordinate_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_pnmlcoremodel::coordinate_has_x():
    assert hasattr(pnmlcoremodel::Coordinate, "x")
    descriptor = None
    for klass in pnmlcoremodel::Coordinate.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::coordinate_has_y():
    assert hasattr(pnmlcoremodel::Coordinate, "y")
    descriptor = None
    for klass in pnmlcoremodel::Coordinate.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_pnmlcoremodel::graphics_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Graphics)


def test_pnmlcoremodel::graphics_constructor_exists():
    assert callable(pnmlcoremodel::Graphics.__init__)


def test_pnmlcoremodel::graphics_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Graphics.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::line_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Line)


def test_pnmlcoremodel::line_constructor_exists():
    assert callable(pnmlcoremodel::Line.__init__)


def test_pnmlcoremodel::line_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Line.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "width" in params, "Missing parameter 'width'"
    assert "style" in params, "Missing parameter 'style'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_pnmlcoremodel::line_has_color():
    assert hasattr(pnmlcoremodel::Line, "color")
    descriptor = None
    for klass in pnmlcoremodel::Line.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::line_has_width():
    assert hasattr(pnmlcoremodel::Line, "width")
    descriptor = None
    for klass in pnmlcoremodel::Line.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::line_has_style():
    assert hasattr(pnmlcoremodel::Line, "style")
    descriptor = None
    for klass in pnmlcoremodel::Line.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::line_has_shape():
    assert hasattr(pnmlcoremodel::Line, "shape")
    descriptor = None
    for klass in pnmlcoremodel::Line.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_pnmlcoremodel::pnobject_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::PnObject)


def test_pnmlcoremodel::pnobject_constructor_exists():
    assert callable(pnmlcoremodel::PnObject.__init__)


def test_pnmlcoremodel::pnobject_constructor_args():
    sig = inspect.signature(pnmlcoremodel::PnObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_pnmlcoremodel::pnobject_has_id():
    assert hasattr(pnmlcoremodel::PnObject, "id")
    descriptor = None
    for klass in pnmlcoremodel::PnObject.__mro__:
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



def test_pnmlcoremodel::node_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Node)


def test_pnmlcoremodel::node_constructor_exists():
    assert callable(pnmlcoremodel::Node.__init__)


def test_pnmlcoremodel::node_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Node.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::arc_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Arc)


def test_pnmlcoremodel::arc_constructor_exists():
    assert callable(pnmlcoremodel::Arc.__init__)


def test_pnmlcoremodel::arc_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Arc.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::toolinfo_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::ToolInfo)


def test_pnmlcoremodel::toolinfo_constructor_exists():
    assert callable(pnmlcoremodel::ToolInfo.__init__)


def test_pnmlcoremodel::toolinfo_constructor_args():
    sig = inspect.signature(pnmlcoremodel::ToolInfo.__init__)
    params = list(sig.parameters.keys())
    assert "formattedXMLBuffer" in params, "Missing parameter 'formattedXMLBuffer'"
    assert "toolInfoGrammarURI" in params, "Missing parameter 'toolInfoGrammarURI'"
    assert "version" in params, "Missing parameter 'version'"
    assert "tool" in params, "Missing parameter 'tool'"

def test_pnmlcoremodel::toolinfo_has_formattedXMLBuffer():
    assert hasattr(pnmlcoremodel::ToolInfo, "formattedXMLBuffer")
    descriptor = None
    for klass in pnmlcoremodel::ToolInfo.__mro__:
        if "formattedXMLBuffer" in klass.__dict__:
            descriptor = klass.__dict__["formattedXMLBuffer"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::toolinfo_has_toolInfoGrammarURI():
    assert hasattr(pnmlcoremodel::ToolInfo, "toolInfoGrammarURI")
    descriptor = None
    for klass in pnmlcoremodel::ToolInfo.__mro__:
        if "toolInfoGrammarURI" in klass.__dict__:
            descriptor = klass.__dict__["toolInfoGrammarURI"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::toolinfo_has_version():
    assert hasattr(pnmlcoremodel::ToolInfo, "version")
    descriptor = None
    for klass in pnmlcoremodel::ToolInfo.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::toolinfo_has_tool():
    assert hasattr(pnmlcoremodel::ToolInfo, "tool")
    descriptor = None
    for klass in pnmlcoremodel::ToolInfo.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)



def test_pnmlcoremodel::page_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Page)


def test_pnmlcoremodel::page_constructor_exists():
    assert callable(pnmlcoremodel::Page.__init__)


def test_pnmlcoremodel::page_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Page.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::name_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::Name)


def test_pnmlcoremodel::name_constructor_exists():
    assert callable(pnmlcoremodel::Name.__init__)


def test_pnmlcoremodel::name_constructor_args():
    sig = inspect.signature(pnmlcoremodel::Name.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_pnmlcoremodel::name_has_text():
    assert hasattr(pnmlcoremodel::Name, "text")
    descriptor = None
    for klass in pnmlcoremodel::Name.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_pnmlcoremodel::nodegraphics_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::NodeGraphics)


def test_pnmlcoremodel::nodegraphics_constructor_exists():
    assert callable(pnmlcoremodel::NodeGraphics.__init__)


def test_pnmlcoremodel::nodegraphics_constructor_args():
    sig = inspect.signature(pnmlcoremodel::NodeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_pnmlcoremodel::petrinet_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel::PetriNet)


def test_pnmlcoremodel::petrinet_constructor_exists():
    assert callable(pnmlcoremodel::PetriNet.__init__)


def test_pnmlcoremodel::petrinet_constructor_args():
    sig = inspect.signature(pnmlcoremodel::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

def test_pnmlcoremodel::petrinet_has_type():
    assert hasattr(pnmlcoremodel::PetriNet, "type")
    descriptor = None
    for klass in pnmlcoremodel::PetriNet.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_pnmlcoremodel::petrinet_has_id():
    assert hasattr(pnmlcoremodel::PetriNet, "id")
    descriptor = None
    for klass in pnmlcoremodel::PetriNet.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

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
        "ITALIC",
        "NORMAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontStyle"

def test_pntype_exists():
    # Check that the Enumeration exists
    assert PNType is not None

def test_pntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PNType]
    expected_literals = [
        "HLPN",
        "COREMODEL",
        "SYMNET",
        "PTNET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PNType"

def test_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "DASH",
        "DOT",
        "SOLID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"

def test_fontdecoration_exists():
    # Check that the Enumeration exists
    assert FontDecoration is not None

def test_fontdecoration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontDecoration]
    expected_literals = [
        "LINETHROUGH",
        "UNDERLINE",
        "OVERLINE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontDecoration"

def test_gradient_exists():
    # Check that the Enumeration exists
    assert Gradient is not None

def test_gradient_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gradient]
    expected_literals = [
        "HORIZONTAL",
        "VERTICAL",
        "DIAGONAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gradient"

def test_css2fontsize_exists():
    # Check that the Enumeration exists
    assert CSS2FontSize is not None

def test_css2fontsize_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontSize]
    expected_literals = [
        "XSMALL",
        "XXSMALL",
        "XXLARGE",
        "LARGE",
        "XLARGE",
        "MEDIUM",
        "SMALL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontSize"

def test_css2color_exists():
    # Check that the Enumeration exists
    assert CSS2Color is not None

def test_css2color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2Color]
    expected_literals = [
        "FUCHSIA",
        "WHITE",
        "ORANGE",
        "PURPLE",
        "LIME",
        "AQUA",
        "TEAL",
        "GREEN",
        "YELLOW",
        "RED",
        "MAROON",
        "NAVY",
        "BLUE",
        "BLACK",
        "OLIVE",
        "SILVER",
        "GRAY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2Color"

def test_fontalign_exists():
    # Check that the Enumeration exists
    assert FontAlign is not None

def test_fontalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontAlign]
    expected_literals = [
        "CENTER",
        "LEFT",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontAlign"

def test_css2fontweight_exists():
    # Check that the Enumeration exists
    assert CSS2FontWeight is not None

def test_css2fontweight_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontWeight]
    expected_literals = [
        "LIGHTER",
        "BOLDER",
        "NORMAL",
        "BOLD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontWeight"

def test_css2fontfamily_exists():
    # Check that the Enumeration exists
    assert CSS2FontFamily is not None

def test_css2fontfamily_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontFamily]
    expected_literals = [
        "VERDANA",
        "ARIAL",
        "TIMES",
        "GEORGIA",
        "TREBUCHET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontFamily"


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
pnmlcoremodel::PetriNetDoc_strategy = st.builds(
    pnmlcoremodel::PetriNetDoc,
    xmlns=
        safe_text
)
PlaceNode_strategy = st.builds(
    PlaceNode,
)
pnmlcoremodel::Place_strategy = st.builds(
    pnmlcoremodel::Place,
)
pnmlcoremodel::RefPlace_strategy = st.builds(
    pnmlcoremodel::RefPlace,
)
Node_strategy = st.builds(
    Node,
)
pnmlcoremodel::TransitionNode_strategy = st.builds(
    pnmlcoremodel::TransitionNode,
)
pnmlcoremodel::PlaceNode_strategy = st.builds(
    pnmlcoremodel::PlaceNode,
)
Label_strategy = st.builds(
    Label,
)
pnmlcoremodel::Attribute_strategy = st.builds(
    pnmlcoremodel::Attribute,
)
TransitionNode_strategy = st.builds(
    TransitionNode,
)
pnmlcoremodel::Transition_strategy = st.builds(
    pnmlcoremodel::Transition,
)
pnmlcoremodel::RefTransition_strategy = st.builds(
    pnmlcoremodel::RefTransition,
)
pnmlcoremodel::Annotation_strategy = st.builds(
    pnmlcoremodel::Annotation,
)
pnmlcoremodel::Font_strategy = st.builds(
    pnmlcoremodel::Font,
    style=
        safe_text,
    align=
        safe_text,
    weight=
        safe_text,
    size=
        safe_text,
    decoration=
        safe_text,
    family=
        safe_text,
    rotation=
        safe_text
)
pnmlcoremodel::Fill_strategy = st.builds(
    pnmlcoremodel::Fill,
    color=
        safe_text,
    gradientrotation=
        safe_text,
    image=
        safe_text,
    gradientcolor=
        safe_text
)
Graphics_strategy = st.builds(
    Graphics,
)
pnmlcoremodel::AnyObject_strategy = st.builds(
    pnmlcoremodel::AnyObject,
)
pnmlcoremodel::Label_strategy = st.builds(
    pnmlcoremodel::Label,
)
pnmlcoremodel::AnnotationGraphics_strategy = st.builds(
    pnmlcoremodel::AnnotationGraphics,
)
pnmlcoremodel::ArcGraphics_strategy = st.builds(
    pnmlcoremodel::ArcGraphics,
)
Coordinate_strategy = st.builds(
    Coordinate,
)
pnmlcoremodel::Offset_strategy = st.builds(
    pnmlcoremodel::Offset,
)
pnmlcoremodel::Dimension_strategy = st.builds(
    pnmlcoremodel::Dimension,
)
pnmlcoremodel::Position_strategy = st.builds(
    pnmlcoremodel::Position,
)
pnmlcoremodel::Coordinate_strategy = st.builds(
    pnmlcoremodel::Coordinate,
    x=
        safe_text,
    y=
        safe_text
)
pnmlcoremodel::Graphics_strategy = st.builds(
    pnmlcoremodel::Graphics,
)
pnmlcoremodel::Line_strategy = st.builds(
    pnmlcoremodel::Line,
    color=
        safe_text,
    width=
        safe_text,
    style=
        safe_text,
    shape=
        safe_text
)
pnmlcoremodel::PnObject_strategy = st.builds(
    pnmlcoremodel::PnObject,
    id=
        safe_text
)
PnObject_strategy = st.builds(
    PnObject,
)
pnmlcoremodel::Node_strategy = st.builds(
    pnmlcoremodel::Node,
)
pnmlcoremodel::Arc_strategy = st.builds(
    pnmlcoremodel::Arc,
)
pnmlcoremodel::ToolInfo_strategy = st.builds(
    pnmlcoremodel::ToolInfo,
    formattedXMLBuffer=
        safe_text,
    toolInfoGrammarURI=
        safe_text,
    version=
        safe_text,
    tool=
        safe_text
)
pnmlcoremodel::Page_strategy = st.builds(
    pnmlcoremodel::Page,
)
Annotation_strategy = st.builds(
    Annotation,
)
pnmlcoremodel::Name_strategy = st.builds(
    pnmlcoremodel::Name,
    text=
        safe_text
)
pnmlcoremodel::NodeGraphics_strategy = st.builds(
    pnmlcoremodel::NodeGraphics,
)
pnmlcoremodel::PetriNet_strategy = st.builds(
    pnmlcoremodel::PetriNet,
    type=
        safe_text,
    id=
        safe_text
)

@given(instance=pnmlcoremodel::PetriNetDoc_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::petrinetdoc_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::PetriNetDoc)

@given(instance=pnmlcoremodel::PetriNetDoc_strategy)
def test_pnmlcoremodel::petrinetdoc_xmlns_type(instance):
    assert isinstance(instance.xmlns, str)


@given(instance=pnmlcoremodel::PetriNetDoc_strategy)
def test_pnmlcoremodel::petrinetdoc_xmlns_setter(instance):
    original = instance.xmlns
    instance.xmlns = original
    assert instance.xmlns == original

@given(instance=PlaceNode_strategy)
@settings(max_examples=50)
def test_placenode_instantiation(instance):
    assert isinstance(instance, PlaceNode)

@given(instance=pnmlcoremodel::Place_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::place_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Place)

@given(instance=pnmlcoremodel::RefPlace_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::refplace_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::RefPlace)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=pnmlcoremodel::TransitionNode_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::transitionnode_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::TransitionNode)

@given(instance=pnmlcoremodel::PlaceNode_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::placenode_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::PlaceNode)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=pnmlcoremodel::Attribute_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::attribute_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Attribute)

@given(instance=TransitionNode_strategy)
@settings(max_examples=50)
def test_transitionnode_instantiation(instance):
    assert isinstance(instance, TransitionNode)

@given(instance=pnmlcoremodel::Transition_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::transition_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Transition)

@given(instance=pnmlcoremodel::RefTransition_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::reftransition_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::RefTransition)

@given(instance=pnmlcoremodel::Annotation_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::annotation_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Annotation)

@given(instance=pnmlcoremodel::Font_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::font_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Font)

@given(instance=pnmlcoremodel::Font_strategy)
def test_pnmlcoremodel::font_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=pnmlcoremodel::Font_strategy)
def test_pnmlcoremodel::font_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=pnmlcoremodel::Font_strategy)
def test_pnmlcoremodel::font_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=pnmlcoremodel::Font_strategy)
def test_pnmlcoremodel::font_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=pnmlcoremodel::Font_strategy)
def test_pnmlcoremodel::font_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=pnmlcoremodel::Font_strategy)
def test_pnmlcoremodel::font_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=pnmlcoremodel::Font_strategy)
def test_pnmlcoremodel::font_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=pnmlcoremodel::Font_strategy)
def test_pnmlcoremodel::font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=pnmlcoremodel::Font_strategy)
def test_pnmlcoremodel::font_decoration_type(instance):
    assert isinstance(instance.decoration, str)


@given(instance=pnmlcoremodel::Font_strategy)
def test_pnmlcoremodel::font_decoration_setter(instance):
    original = instance.decoration
    instance.decoration = original
    assert instance.decoration == original

@given(instance=pnmlcoremodel::Font_strategy)
def test_pnmlcoremodel::font_family_type(instance):
    assert isinstance(instance.family, str)


@given(instance=pnmlcoremodel::Font_strategy)
def test_pnmlcoremodel::font_family_setter(instance):
    original = instance.family
    instance.family = original
    assert instance.family == original

@given(instance=pnmlcoremodel::Font_strategy)
def test_pnmlcoremodel::font_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=pnmlcoremodel::Font_strategy)
def test_pnmlcoremodel::font_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=pnmlcoremodel::Fill_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::fill_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Fill)

@given(instance=pnmlcoremodel::Fill_strategy)
def test_pnmlcoremodel::fill_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=pnmlcoremodel::Fill_strategy)
def test_pnmlcoremodel::fill_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=pnmlcoremodel::Fill_strategy)
def test_pnmlcoremodel::fill_gradientrotation_type(instance):
    assert isinstance(instance.gradientrotation, str)


@given(instance=pnmlcoremodel::Fill_strategy)
def test_pnmlcoremodel::fill_gradientrotation_setter(instance):
    original = instance.gradientrotation
    instance.gradientrotation = original
    assert instance.gradientrotation == original

@given(instance=pnmlcoremodel::Fill_strategy)
def test_pnmlcoremodel::fill_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=pnmlcoremodel::Fill_strategy)
def test_pnmlcoremodel::fill_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=pnmlcoremodel::Fill_strategy)
def test_pnmlcoremodel::fill_gradientcolor_type(instance):
    assert isinstance(instance.gradientcolor, str)


@given(instance=pnmlcoremodel::Fill_strategy)
def test_pnmlcoremodel::fill_gradientcolor_setter(instance):
    original = instance.gradientcolor
    instance.gradientcolor = original
    assert instance.gradientcolor == original

@given(instance=Graphics_strategy)
@settings(max_examples=50)
def test_graphics_instantiation(instance):
    assert isinstance(instance, Graphics)

@given(instance=pnmlcoremodel::AnyObject_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::anyobject_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::AnyObject)

@given(instance=pnmlcoremodel::Label_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::label_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Label)

@given(instance=pnmlcoremodel::AnnotationGraphics_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::annotationgraphics_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::AnnotationGraphics)

@given(instance=pnmlcoremodel::ArcGraphics_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::arcgraphics_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::ArcGraphics)

@given(instance=Coordinate_strategy)
@settings(max_examples=50)
def test_coordinate_instantiation(instance):
    assert isinstance(instance, Coordinate)

@given(instance=pnmlcoremodel::Offset_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::offset_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Offset)

@given(instance=pnmlcoremodel::Dimension_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::dimension_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Dimension)

@given(instance=pnmlcoremodel::Position_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::position_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Position)

@given(instance=pnmlcoremodel::Coordinate_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::coordinate_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Coordinate)

@given(instance=pnmlcoremodel::Coordinate_strategy)
def test_pnmlcoremodel::coordinate_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=pnmlcoremodel::Coordinate_strategy)
def test_pnmlcoremodel::coordinate_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=pnmlcoremodel::Coordinate_strategy)
def test_pnmlcoremodel::coordinate_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=pnmlcoremodel::Coordinate_strategy)
def test_pnmlcoremodel::coordinate_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=pnmlcoremodel::Graphics_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::graphics_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Graphics)

@given(instance=pnmlcoremodel::Line_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::line_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Line)

@given(instance=pnmlcoremodel::Line_strategy)
def test_pnmlcoremodel::line_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=pnmlcoremodel::Line_strategy)
def test_pnmlcoremodel::line_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=pnmlcoremodel::Line_strategy)
def test_pnmlcoremodel::line_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=pnmlcoremodel::Line_strategy)
def test_pnmlcoremodel::line_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=pnmlcoremodel::Line_strategy)
def test_pnmlcoremodel::line_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=pnmlcoremodel::Line_strategy)
def test_pnmlcoremodel::line_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=pnmlcoremodel::Line_strategy)
def test_pnmlcoremodel::line_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=pnmlcoremodel::Line_strategy)
def test_pnmlcoremodel::line_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=pnmlcoremodel::PnObject_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::pnobject_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::PnObject)

@given(instance=pnmlcoremodel::PnObject_strategy)
def test_pnmlcoremodel::pnobject_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=pnmlcoremodel::PnObject_strategy)
def test_pnmlcoremodel::pnobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=PnObject_strategy)
@settings(max_examples=50)
def test_pnobject_instantiation(instance):
    assert isinstance(instance, PnObject)

@given(instance=pnmlcoremodel::Node_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::node_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Node)

@given(instance=pnmlcoremodel::Arc_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::arc_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Arc)

@given(instance=pnmlcoremodel::ToolInfo_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::toolinfo_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::ToolInfo)

@given(instance=pnmlcoremodel::ToolInfo_strategy)
def test_pnmlcoremodel::toolinfo_formattedXMLBuffer_type(instance):
    assert isinstance(instance.formattedXMLBuffer, str)


@given(instance=pnmlcoremodel::ToolInfo_strategy)
def test_pnmlcoremodel::toolinfo_formattedXMLBuffer_setter(instance):
    original = instance.formattedXMLBuffer
    instance.formattedXMLBuffer = original
    assert instance.formattedXMLBuffer == original

@given(instance=pnmlcoremodel::ToolInfo_strategy)
def test_pnmlcoremodel::toolinfo_toolInfoGrammarURI_type(instance):
    assert isinstance(instance.toolInfoGrammarURI, str)


@given(instance=pnmlcoremodel::ToolInfo_strategy)
def test_pnmlcoremodel::toolinfo_toolInfoGrammarURI_setter(instance):
    original = instance.toolInfoGrammarURI
    instance.toolInfoGrammarURI = original
    assert instance.toolInfoGrammarURI == original

@given(instance=pnmlcoremodel::ToolInfo_strategy)
def test_pnmlcoremodel::toolinfo_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=pnmlcoremodel::ToolInfo_strategy)
def test_pnmlcoremodel::toolinfo_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=pnmlcoremodel::ToolInfo_strategy)
def test_pnmlcoremodel::toolinfo_tool_type(instance):
    assert isinstance(instance.tool, str)


@given(instance=pnmlcoremodel::ToolInfo_strategy)
def test_pnmlcoremodel::toolinfo_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=pnmlcoremodel::Page_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::page_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Page)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=pnmlcoremodel::Name_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::name_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::Name)

@given(instance=pnmlcoremodel::Name_strategy)
def test_pnmlcoremodel::name_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=pnmlcoremodel::Name_strategy)
def test_pnmlcoremodel::name_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=pnmlcoremodel::NodeGraphics_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::nodegraphics_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::NodeGraphics)

@given(instance=pnmlcoremodel::PetriNet_strategy)
@settings(max_examples=50)
def test_pnmlcoremodel::petrinet_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel::PetriNet)

@given(instance=pnmlcoremodel::PetriNet_strategy)
def test_pnmlcoremodel::petrinet_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=pnmlcoremodel::PetriNet_strategy)
def test_pnmlcoremodel::petrinet_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=pnmlcoremodel::PetriNet_strategy)
def test_pnmlcoremodel::petrinet_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=pnmlcoremodel::PetriNet_strategy)
def test_pnmlcoremodel::petrinet_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
