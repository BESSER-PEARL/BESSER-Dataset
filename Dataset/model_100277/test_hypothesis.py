import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    hlcorestructure::Declarations,
    hlcorestructure::Term,
    hlcorestructure::Sort,
    HLCoreAnnotation,
    hlcorestructure::ArbitrarySort,
    hlcorestructure::AnySort,
    hlcorestructure::Unparsed,
    Label,
    hlcorestructure::Attribute,
    hlcorestructure::Condition,
    TransitionNode,
    hlcorestructure::Transition,
    hlcorestructure::Type,
    PlaceNode,
    hlcorestructure::Place,
    hlcorestructure::RefTransition,
    hlcorestructure::RefPlace,
    Node,
    hlcorestructure::TransitionNode,
    hlcorestructure::PlaceNode,
    hlcorestructure::HLMarking,
    hlcorestructure::HLAnnotation,
    hlcorestructure::Annotation,
    hlcorestructure::Font,
    hlcorestructure::Coordinate,
    Coordinate,
    hlcorestructure::Offset,
    hlcorestructure::AnyObject,
    hlcorestructure::Label,
    hlcorestructure::Graphics,
    hlcorestructure::Line,
    hlcorestructure::Fill,
    hlcorestructure::Dimension,
    hlcorestructure::Position,
    Graphics,
    hlcorestructure::AnnotationGraphics,
    hlcorestructure::ArcGraphics,
    Annotation,
    hlcorestructure::HLCoreAnnotation,
    hlcorestructure::ToolInfo,
    hlcorestructure::Name,
    hlcorestructure::NodeGraphics,
    hlcorestructure::PnObject,
    PnObject,
    hlcorestructure::Node,
    hlcorestructure::Arc,
    hlcorestructure::Page,
    hlcorestructure::Declaration,
    hlcorestructure::PetriNet,
    hlcorestructure::PetriNetDoc,
    CSS2FontFamily,
    LineStyle,
    CSS2FontWeight,
    FontAlign,
    CSS2Color,
    Gradient,
    FontDecoration,
    LineShape,
    CSS2FontStyle,
    CSS2FontSize,
    PNType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hlcorestructure::declarations_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Declarations)


def test_hlcorestructure::declarations_constructor_exists():
    assert callable(hlcorestructure::Declarations.__init__)


def test_hlcorestructure::declarations_constructor_args():
    sig = inspect.signature(hlcorestructure::Declarations.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::term_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Term)


def test_hlcorestructure::term_constructor_exists():
    assert callable(hlcorestructure::Term.__init__)


def test_hlcorestructure::term_constructor_args():
    sig = inspect.signature(hlcorestructure::Term.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::sort_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Sort)


def test_hlcorestructure::sort_constructor_exists():
    assert callable(hlcorestructure::Sort.__init__)


def test_hlcorestructure::sort_constructor_args():
    sig = inspect.signature(hlcorestructure::Sort.__init__)
    params = list(sig.parameters.keys())



def test_hlcoreannotation_is_not_abstract():
    assert not inspect.isabstract(HLCoreAnnotation)


def test_hlcoreannotation_constructor_exists():
    assert callable(HLCoreAnnotation.__init__)


def test_hlcoreannotation_constructor_args():
    sig = inspect.signature(HLCoreAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::arbitrarysort_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::ArbitrarySort)


def test_hlcorestructure::arbitrarysort_constructor_exists():
    assert callable(hlcorestructure::ArbitrarySort.__init__)


def test_hlcorestructure::arbitrarysort_constructor_args():
    sig = inspect.signature(hlcorestructure::ArbitrarySort.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::anysort_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::AnySort)


def test_hlcorestructure::anysort_constructor_exists():
    assert callable(hlcorestructure::AnySort.__init__)


def test_hlcorestructure::anysort_constructor_args():
    sig = inspect.signature(hlcorestructure::AnySort.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::unparsed_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Unparsed)


def test_hlcorestructure::unparsed_constructor_exists():
    assert callable(hlcorestructure::Unparsed.__init__)


def test_hlcorestructure::unparsed_constructor_args():
    sig = inspect.signature(hlcorestructure::Unparsed.__init__)
    params = list(sig.parameters.keys())



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::attribute_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Attribute)


def test_hlcorestructure::attribute_constructor_exists():
    assert callable(hlcorestructure::Attribute.__init__)


def test_hlcorestructure::attribute_constructor_args():
    sig = inspect.signature(hlcorestructure::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::condition_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Condition)


def test_hlcorestructure::condition_constructor_exists():
    assert callable(hlcorestructure::Condition.__init__)


def test_hlcorestructure::condition_constructor_args():
    sig = inspect.signature(hlcorestructure::Condition.__init__)
    params = list(sig.parameters.keys())



def test_transitionnode_is_not_abstract():
    assert not inspect.isabstract(TransitionNode)


def test_transitionnode_constructor_exists():
    assert callable(TransitionNode.__init__)


def test_transitionnode_constructor_args():
    sig = inspect.signature(TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::transition_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Transition)


def test_hlcorestructure::transition_constructor_exists():
    assert callable(hlcorestructure::Transition.__init__)


def test_hlcorestructure::transition_constructor_args():
    sig = inspect.signature(hlcorestructure::Transition.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::type_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Type)


def test_hlcorestructure::type_constructor_exists():
    assert callable(hlcorestructure::Type.__init__)


def test_hlcorestructure::type_constructor_args():
    sig = inspect.signature(hlcorestructure::Type.__init__)
    params = list(sig.parameters.keys())



def test_placenode_is_not_abstract():
    assert not inspect.isabstract(PlaceNode)


def test_placenode_constructor_exists():
    assert callable(PlaceNode.__init__)


def test_placenode_constructor_args():
    sig = inspect.signature(PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::place_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Place)


def test_hlcorestructure::place_constructor_exists():
    assert callable(hlcorestructure::Place.__init__)


def test_hlcorestructure::place_constructor_args():
    sig = inspect.signature(hlcorestructure::Place.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::reftransition_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::RefTransition)


def test_hlcorestructure::reftransition_constructor_exists():
    assert callable(hlcorestructure::RefTransition.__init__)


def test_hlcorestructure::reftransition_constructor_args():
    sig = inspect.signature(hlcorestructure::RefTransition.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::refplace_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::RefPlace)


def test_hlcorestructure::refplace_constructor_exists():
    assert callable(hlcorestructure::RefPlace.__init__)


def test_hlcorestructure::refplace_constructor_args():
    sig = inspect.signature(hlcorestructure::RefPlace.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::transitionnode_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::TransitionNode)


def test_hlcorestructure::transitionnode_constructor_exists():
    assert callable(hlcorestructure::TransitionNode.__init__)


def test_hlcorestructure::transitionnode_constructor_args():
    sig = inspect.signature(hlcorestructure::TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::placenode_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::PlaceNode)


def test_hlcorestructure::placenode_constructor_exists():
    assert callable(hlcorestructure::PlaceNode.__init__)


def test_hlcorestructure::placenode_constructor_args():
    sig = inspect.signature(hlcorestructure::PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::hlmarking_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::HLMarking)


def test_hlcorestructure::hlmarking_constructor_exists():
    assert callable(hlcorestructure::HLMarking.__init__)


def test_hlcorestructure::hlmarking_constructor_args():
    sig = inspect.signature(hlcorestructure::HLMarking.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::hlannotation_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::HLAnnotation)


def test_hlcorestructure::hlannotation_constructor_exists():
    assert callable(hlcorestructure::HLAnnotation.__init__)


def test_hlcorestructure::hlannotation_constructor_args():
    sig = inspect.signature(hlcorestructure::HLAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::annotation_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Annotation)


def test_hlcorestructure::annotation_constructor_exists():
    assert callable(hlcorestructure::Annotation.__init__)


def test_hlcorestructure::annotation_constructor_args():
    sig = inspect.signature(hlcorestructure::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::font_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Font)


def test_hlcorestructure::font_constructor_exists():
    assert callable(hlcorestructure::Font.__init__)


def test_hlcorestructure::font_constructor_args():
    sig = inspect.signature(hlcorestructure::Font.__init__)
    params = list(sig.parameters.keys())
    assert "decoration" in params, "Missing parameter 'decoration'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "align" in params, "Missing parameter 'align'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "style" in params, "Missing parameter 'style'"
    assert "size" in params, "Missing parameter 'size'"
    assert "family" in params, "Missing parameter 'family'"

def test_hlcorestructure::font_has_decoration():
    assert hasattr(hlcorestructure::Font, "decoration")
    descriptor = None
    for klass in hlcorestructure::Font.__mro__:
        if "decoration" in klass.__dict__:
            descriptor = klass.__dict__["decoration"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::font_has_weight():
    assert hasattr(hlcorestructure::Font, "weight")
    descriptor = None
    for klass in hlcorestructure::Font.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::font_has_align():
    assert hasattr(hlcorestructure::Font, "align")
    descriptor = None
    for klass in hlcorestructure::Font.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::font_has_rotation():
    assert hasattr(hlcorestructure::Font, "rotation")
    descriptor = None
    for klass in hlcorestructure::Font.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::font_has_style():
    assert hasattr(hlcorestructure::Font, "style")
    descriptor = None
    for klass in hlcorestructure::Font.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::font_has_size():
    assert hasattr(hlcorestructure::Font, "size")
    descriptor = None
    for klass in hlcorestructure::Font.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::font_has_family():
    assert hasattr(hlcorestructure::Font, "family")
    descriptor = None
    for klass in hlcorestructure::Font.__mro__:
        if "family" in klass.__dict__:
            descriptor = klass.__dict__["family"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure::coordinate_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Coordinate)


def test_hlcorestructure::coordinate_constructor_exists():
    assert callable(hlcorestructure::Coordinate.__init__)


def test_hlcorestructure::coordinate_constructor_args():
    sig = inspect.signature(hlcorestructure::Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_hlcorestructure::coordinate_has_y():
    assert hasattr(hlcorestructure::Coordinate, "y")
    descriptor = None
    for klass in hlcorestructure::Coordinate.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::coordinate_has_x():
    assert hasattr(hlcorestructure::Coordinate, "x")
    descriptor = None
    for klass in hlcorestructure::Coordinate.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_coordinate_is_not_abstract():
    assert not inspect.isabstract(Coordinate)


def test_coordinate_constructor_exists():
    assert callable(Coordinate.__init__)


def test_coordinate_constructor_args():
    sig = inspect.signature(Coordinate.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::offset_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Offset)


def test_hlcorestructure::offset_constructor_exists():
    assert callable(hlcorestructure::Offset.__init__)


def test_hlcorestructure::offset_constructor_args():
    sig = inspect.signature(hlcorestructure::Offset.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::anyobject_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::AnyObject)


def test_hlcorestructure::anyobject_constructor_exists():
    assert callable(hlcorestructure::AnyObject.__init__)


def test_hlcorestructure::anyobject_constructor_args():
    sig = inspect.signature(hlcorestructure::AnyObject.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::label_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Label)


def test_hlcorestructure::label_constructor_exists():
    assert callable(hlcorestructure::Label.__init__)


def test_hlcorestructure::label_constructor_args():
    sig = inspect.signature(hlcorestructure::Label.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::graphics_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Graphics)


def test_hlcorestructure::graphics_constructor_exists():
    assert callable(hlcorestructure::Graphics.__init__)


def test_hlcorestructure::graphics_constructor_args():
    sig = inspect.signature(hlcorestructure::Graphics.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::line_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Line)


def test_hlcorestructure::line_constructor_exists():
    assert callable(hlcorestructure::Line.__init__)


def test_hlcorestructure::line_constructor_args():
    sig = inspect.signature(hlcorestructure::Line.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "shape" in params, "Missing parameter 'shape'"
    assert "style" in params, "Missing parameter 'style'"
    assert "width" in params, "Missing parameter 'width'"

def test_hlcorestructure::line_has_color():
    assert hasattr(hlcorestructure::Line, "color")
    descriptor = None
    for klass in hlcorestructure::Line.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::line_has_shape():
    assert hasattr(hlcorestructure::Line, "shape")
    descriptor = None
    for klass in hlcorestructure::Line.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::line_has_style():
    assert hasattr(hlcorestructure::Line, "style")
    descriptor = None
    for klass in hlcorestructure::Line.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::line_has_width():
    assert hasattr(hlcorestructure::Line, "width")
    descriptor = None
    for klass in hlcorestructure::Line.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure::fill_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Fill)


def test_hlcorestructure::fill_constructor_exists():
    assert callable(hlcorestructure::Fill.__init__)


def test_hlcorestructure::fill_constructor_args():
    sig = inspect.signature(hlcorestructure::Fill.__init__)
    params = list(sig.parameters.keys())
    assert "gradientrotation" in params, "Missing parameter 'gradientrotation'"
    assert "color" in params, "Missing parameter 'color'"
    assert "gradientcolor" in params, "Missing parameter 'gradientcolor'"
    assert "image" in params, "Missing parameter 'image'"

def test_hlcorestructure::fill_has_gradientrotation():
    assert hasattr(hlcorestructure::Fill, "gradientrotation")
    descriptor = None
    for klass in hlcorestructure::Fill.__mro__:
        if "gradientrotation" in klass.__dict__:
            descriptor = klass.__dict__["gradientrotation"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::fill_has_color():
    assert hasattr(hlcorestructure::Fill, "color")
    descriptor = None
    for klass in hlcorestructure::Fill.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::fill_has_gradientcolor():
    assert hasattr(hlcorestructure::Fill, "gradientcolor")
    descriptor = None
    for klass in hlcorestructure::Fill.__mro__:
        if "gradientcolor" in klass.__dict__:
            descriptor = klass.__dict__["gradientcolor"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::fill_has_image():
    assert hasattr(hlcorestructure::Fill, "image")
    descriptor = None
    for klass in hlcorestructure::Fill.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure::dimension_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Dimension)


def test_hlcorestructure::dimension_constructor_exists():
    assert callable(hlcorestructure::Dimension.__init__)


def test_hlcorestructure::dimension_constructor_args():
    sig = inspect.signature(hlcorestructure::Dimension.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::position_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Position)


def test_hlcorestructure::position_constructor_exists():
    assert callable(hlcorestructure::Position.__init__)


def test_hlcorestructure::position_constructor_args():
    sig = inspect.signature(hlcorestructure::Position.__init__)
    params = list(sig.parameters.keys())



def test_graphics_is_not_abstract():
    assert not inspect.isabstract(Graphics)


def test_graphics_constructor_exists():
    assert callable(Graphics.__init__)


def test_graphics_constructor_args():
    sig = inspect.signature(Graphics.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::annotationgraphics_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::AnnotationGraphics)


def test_hlcorestructure::annotationgraphics_constructor_exists():
    assert callable(hlcorestructure::AnnotationGraphics.__init__)


def test_hlcorestructure::annotationgraphics_constructor_args():
    sig = inspect.signature(hlcorestructure::AnnotationGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::arcgraphics_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::ArcGraphics)


def test_hlcorestructure::arcgraphics_constructor_exists():
    assert callable(hlcorestructure::ArcGraphics.__init__)


def test_hlcorestructure::arcgraphics_constructor_args():
    sig = inspect.signature(hlcorestructure::ArcGraphics.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::hlcoreannotation_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::HLCoreAnnotation)


def test_hlcorestructure::hlcoreannotation_constructor_exists():
    assert callable(hlcorestructure::HLCoreAnnotation.__init__)


def test_hlcorestructure::hlcoreannotation_constructor_args():
    sig = inspect.signature(hlcorestructure::HLCoreAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_hlcorestructure::hlcoreannotation_has_text():
    assert hasattr(hlcorestructure::HLCoreAnnotation, "text")
    descriptor = None
    for klass in hlcorestructure::HLCoreAnnotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure::toolinfo_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::ToolInfo)


def test_hlcorestructure::toolinfo_constructor_exists():
    assert callable(hlcorestructure::ToolInfo.__init__)


def test_hlcorestructure::toolinfo_constructor_args():
    sig = inspect.signature(hlcorestructure::ToolInfo.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "toolInfoGrammarURI" in params, "Missing parameter 'toolInfoGrammarURI'"
    assert "formattedXMLBuffer" in params, "Missing parameter 'formattedXMLBuffer'"
    assert "tool" in params, "Missing parameter 'tool'"

def test_hlcorestructure::toolinfo_has_version():
    assert hasattr(hlcorestructure::ToolInfo, "version")
    descriptor = None
    for klass in hlcorestructure::ToolInfo.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::toolinfo_has_toolInfoGrammarURI():
    assert hasattr(hlcorestructure::ToolInfo, "toolInfoGrammarURI")
    descriptor = None
    for klass in hlcorestructure::ToolInfo.__mro__:
        if "toolInfoGrammarURI" in klass.__dict__:
            descriptor = klass.__dict__["toolInfoGrammarURI"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::toolinfo_has_formattedXMLBuffer():
    assert hasattr(hlcorestructure::ToolInfo, "formattedXMLBuffer")
    descriptor = None
    for klass in hlcorestructure::ToolInfo.__mro__:
        if "formattedXMLBuffer" in klass.__dict__:
            descriptor = klass.__dict__["formattedXMLBuffer"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::toolinfo_has_tool():
    assert hasattr(hlcorestructure::ToolInfo, "tool")
    descriptor = None
    for klass in hlcorestructure::ToolInfo.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure::name_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Name)


def test_hlcorestructure::name_constructor_exists():
    assert callable(hlcorestructure::Name.__init__)


def test_hlcorestructure::name_constructor_args():
    sig = inspect.signature(hlcorestructure::Name.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_hlcorestructure::name_has_text():
    assert hasattr(hlcorestructure::Name, "text")
    descriptor = None
    for klass in hlcorestructure::Name.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure::nodegraphics_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::NodeGraphics)


def test_hlcorestructure::nodegraphics_constructor_exists():
    assert callable(hlcorestructure::NodeGraphics.__init__)


def test_hlcorestructure::nodegraphics_constructor_args():
    sig = inspect.signature(hlcorestructure::NodeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::pnobject_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::PnObject)


def test_hlcorestructure::pnobject_constructor_exists():
    assert callable(hlcorestructure::PnObject.__init__)


def test_hlcorestructure::pnobject_constructor_args():
    sig = inspect.signature(hlcorestructure::PnObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_hlcorestructure::pnobject_has_id():
    assert hasattr(hlcorestructure::PnObject, "id")
    descriptor = None
    for klass in hlcorestructure::PnObject.__mro__:
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



def test_hlcorestructure::node_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Node)


def test_hlcorestructure::node_constructor_exists():
    assert callable(hlcorestructure::Node.__init__)


def test_hlcorestructure::node_constructor_args():
    sig = inspect.signature(hlcorestructure::Node.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::arc_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Arc)


def test_hlcorestructure::arc_constructor_exists():
    assert callable(hlcorestructure::Arc.__init__)


def test_hlcorestructure::arc_constructor_args():
    sig = inspect.signature(hlcorestructure::Arc.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::page_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Page)


def test_hlcorestructure::page_constructor_exists():
    assert callable(hlcorestructure::Page.__init__)


def test_hlcorestructure::page_constructor_args():
    sig = inspect.signature(hlcorestructure::Page.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::declaration_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::Declaration)


def test_hlcorestructure::declaration_constructor_exists():
    assert callable(hlcorestructure::Declaration.__init__)


def test_hlcorestructure::declaration_constructor_args():
    sig = inspect.signature(hlcorestructure::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure::petrinet_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::PetriNet)


def test_hlcorestructure::petrinet_constructor_exists():
    assert callable(hlcorestructure::PetriNet.__init__)


def test_hlcorestructure::petrinet_constructor_args():
    sig = inspect.signature(hlcorestructure::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

def test_hlcorestructure::petrinet_has_type():
    assert hasattr(hlcorestructure::PetriNet, "type")
    descriptor = None
    for klass in hlcorestructure::PetriNet.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure::petrinet_has_id():
    assert hasattr(hlcorestructure::PetriNet, "id")
    descriptor = None
    for klass in hlcorestructure::PetriNet.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure::petrinetdoc_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure::PetriNetDoc)


def test_hlcorestructure::petrinetdoc_constructor_exists():
    assert callable(hlcorestructure::PetriNetDoc.__init__)


def test_hlcorestructure::petrinetdoc_constructor_args():
    sig = inspect.signature(hlcorestructure::PetriNetDoc.__init__)
    params = list(sig.parameters.keys())
    assert "xmlns" in params, "Missing parameter 'xmlns'"

def test_hlcorestructure::petrinetdoc_has_xmlns():
    assert hasattr(hlcorestructure::PetriNetDoc, "xmlns")
    descriptor = None
    for klass in hlcorestructure::PetriNetDoc.__mro__:
        if "xmlns" in klass.__dict__:
            descriptor = klass.__dict__["xmlns"]
            break
    assert isinstance(descriptor, property)

def test_css2fontfamily_exists():
    # Check that the Enumeration exists
    assert CSS2FontFamily is not None

def test_css2fontfamily_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontFamily]
    expected_literals = [
        "VERDANA",
        "ARIAL",
        "GEORGIA",
        "TIMES",
        "TREBUCHET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontFamily"

def test_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "DOT",
        "DASH",
        "SOLID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"

def test_css2fontweight_exists():
    # Check that the Enumeration exists
    assert CSS2FontWeight is not None

def test_css2fontweight_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontWeight]
    expected_literals = [
        "NORMAL",
        "LIGHTER",
        "BOLDER",
        "BOLD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontWeight"

def test_fontalign_exists():
    # Check that the Enumeration exists
    assert FontAlign is not None

def test_fontalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontAlign]
    expected_literals = [
        "RIGHT",
        "CENTER",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontAlign"

def test_css2color_exists():
    # Check that the Enumeration exists
    assert CSS2Color is not None

def test_css2color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2Color]
    expected_literals = [
        "GRAY",
        "LIME",
        "MAROON",
        "OLIVE",
        "RED",
        "BLUE",
        "AQUA",
        "PURPLE",
        "YELLOW",
        "SILVER",
        "TEAL",
        "FUCHSIA",
        "NAVY",
        "WHITE",
        "BLACK",
        "GREEN",
        "ORANGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2Color"

def test_gradient_exists():
    # Check that the Enumeration exists
    assert Gradient is not None

def test_gradient_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gradient]
    expected_literals = [
        "HORIZONTAL",
        "DIAGONAL",
        "VERTICAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gradient"

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
        "NORMAL",
        "OBLIQUE",
        "ITALIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontStyle"

def test_css2fontsize_exists():
    # Check that the Enumeration exists
    assert CSS2FontSize is not None

def test_css2fontsize_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontSize]
    expected_literals = [
        "LARGE",
        "MEDIUM",
        "XLARGE",
        "SMALL",
        "XSMALL",
        "XXLARGE",
        "XXSMALL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontSize"

def test_pntype_exists():
    # Check that the Enumeration exists
    assert PNType is not None

def test_pntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PNType]
    expected_literals = [
        "COREMODEL",
        "PTNET",
        "SYMNET",
        "HLPN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PNType"


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
hlcorestructure::Declarations_strategy = st.builds(
    hlcorestructure::Declarations,
)
hlcorestructure::Term_strategy = st.builds(
    hlcorestructure::Term,
)
hlcorestructure::Sort_strategy = st.builds(
    hlcorestructure::Sort,
)
HLCoreAnnotation_strategy = st.builds(
    HLCoreAnnotation,
)
hlcorestructure::ArbitrarySort_strategy = st.builds(
    hlcorestructure::ArbitrarySort,
)
hlcorestructure::AnySort_strategy = st.builds(
    hlcorestructure::AnySort,
)
hlcorestructure::Unparsed_strategy = st.builds(
    hlcorestructure::Unparsed,
)
Label_strategy = st.builds(
    Label,
)
hlcorestructure::Attribute_strategy = st.builds(
    hlcorestructure::Attribute,
)
hlcorestructure::Condition_strategy = st.builds(
    hlcorestructure::Condition,
)
TransitionNode_strategy = st.builds(
    TransitionNode,
)
hlcorestructure::Transition_strategy = st.builds(
    hlcorestructure::Transition,
)
hlcorestructure::Type_strategy = st.builds(
    hlcorestructure::Type,
)
PlaceNode_strategy = st.builds(
    PlaceNode,
)
hlcorestructure::Place_strategy = st.builds(
    hlcorestructure::Place,
)
hlcorestructure::RefTransition_strategy = st.builds(
    hlcorestructure::RefTransition,
)
hlcorestructure::RefPlace_strategy = st.builds(
    hlcorestructure::RefPlace,
)
Node_strategy = st.builds(
    Node,
)
hlcorestructure::TransitionNode_strategy = st.builds(
    hlcorestructure::TransitionNode,
)
hlcorestructure::PlaceNode_strategy = st.builds(
    hlcorestructure::PlaceNode,
)
hlcorestructure::HLMarking_strategy = st.builds(
    hlcorestructure::HLMarking,
)
hlcorestructure::HLAnnotation_strategy = st.builds(
    hlcorestructure::HLAnnotation,
)
hlcorestructure::Annotation_strategy = st.builds(
    hlcorestructure::Annotation,
)
hlcorestructure::Font_strategy = st.builds(
    hlcorestructure::Font,
    decoration=
        safe_text,
    weight=
        safe_text,
    align=
        safe_text,
    rotation=
        safe_text,
    style=
        safe_text,
    size=
        safe_text,
    family=
        safe_text
)
hlcorestructure::Coordinate_strategy = st.builds(
    hlcorestructure::Coordinate,
    y=
        safe_text,
    x=
        safe_text
)
Coordinate_strategy = st.builds(
    Coordinate,
)
hlcorestructure::Offset_strategy = st.builds(
    hlcorestructure::Offset,
)
hlcorestructure::AnyObject_strategy = st.builds(
    hlcorestructure::AnyObject,
)
hlcorestructure::Label_strategy = st.builds(
    hlcorestructure::Label,
)
hlcorestructure::Graphics_strategy = st.builds(
    hlcorestructure::Graphics,
)
hlcorestructure::Line_strategy = st.builds(
    hlcorestructure::Line,
    color=
        safe_text,
    shape=
        safe_text,
    style=
        safe_text,
    width=
        safe_text
)
hlcorestructure::Fill_strategy = st.builds(
    hlcorestructure::Fill,
    gradientrotation=
        safe_text,
    color=
        safe_text,
    gradientcolor=
        safe_text,
    image=
        safe_text
)
hlcorestructure::Dimension_strategy = st.builds(
    hlcorestructure::Dimension,
)
hlcorestructure::Position_strategy = st.builds(
    hlcorestructure::Position,
)
Graphics_strategy = st.builds(
    Graphics,
)
hlcorestructure::AnnotationGraphics_strategy = st.builds(
    hlcorestructure::AnnotationGraphics,
)
hlcorestructure::ArcGraphics_strategy = st.builds(
    hlcorestructure::ArcGraphics,
)
Annotation_strategy = st.builds(
    Annotation,
)
hlcorestructure::HLCoreAnnotation_strategy = st.builds(
    hlcorestructure::HLCoreAnnotation,
    text=
        safe_text
)
hlcorestructure::ToolInfo_strategy = st.builds(
    hlcorestructure::ToolInfo,
    version=
        safe_text,
    toolInfoGrammarURI=
        safe_text,
    formattedXMLBuffer=
        safe_text,
    tool=
        safe_text
)
hlcorestructure::Name_strategy = st.builds(
    hlcorestructure::Name,
    text=
        safe_text
)
hlcorestructure::NodeGraphics_strategy = st.builds(
    hlcorestructure::NodeGraphics,
)
hlcorestructure::PnObject_strategy = st.builds(
    hlcorestructure::PnObject,
    id=
        safe_text
)
PnObject_strategy = st.builds(
    PnObject,
)
hlcorestructure::Node_strategy = st.builds(
    hlcorestructure::Node,
)
hlcorestructure::Arc_strategy = st.builds(
    hlcorestructure::Arc,
)
hlcorestructure::Page_strategy = st.builds(
    hlcorestructure::Page,
)
hlcorestructure::Declaration_strategy = st.builds(
    hlcorestructure::Declaration,
)
hlcorestructure::PetriNet_strategy = st.builds(
    hlcorestructure::PetriNet,
    type=
        safe_text,
    id=
        safe_text
)
hlcorestructure::PetriNetDoc_strategy = st.builds(
    hlcorestructure::PetriNetDoc,
    xmlns=
        safe_text
)

@given(instance=hlcorestructure::Declarations_strategy)
@settings(max_examples=50)
def test_hlcorestructure::declarations_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Declarations)

@given(instance=hlcorestructure::Term_strategy)
@settings(max_examples=50)
def test_hlcorestructure::term_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Term)

@given(instance=hlcorestructure::Sort_strategy)
@settings(max_examples=50)
def test_hlcorestructure::sort_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Sort)

@given(instance=HLCoreAnnotation_strategy)
@settings(max_examples=50)
def test_hlcoreannotation_instantiation(instance):
    assert isinstance(instance, HLCoreAnnotation)

@given(instance=hlcorestructure::ArbitrarySort_strategy)
@settings(max_examples=50)
def test_hlcorestructure::arbitrarysort_instantiation(instance):
    assert isinstance(instance, hlcorestructure::ArbitrarySort)

@given(instance=hlcorestructure::AnySort_strategy)
@settings(max_examples=50)
def test_hlcorestructure::anysort_instantiation(instance):
    assert isinstance(instance, hlcorestructure::AnySort)

@given(instance=hlcorestructure::Unparsed_strategy)
@settings(max_examples=50)
def test_hlcorestructure::unparsed_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Unparsed)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=hlcorestructure::Attribute_strategy)
@settings(max_examples=50)
def test_hlcorestructure::attribute_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Attribute)

@given(instance=hlcorestructure::Condition_strategy)
@settings(max_examples=50)
def test_hlcorestructure::condition_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Condition)

@given(instance=TransitionNode_strategy)
@settings(max_examples=50)
def test_transitionnode_instantiation(instance):
    assert isinstance(instance, TransitionNode)

@given(instance=hlcorestructure::Transition_strategy)
@settings(max_examples=50)
def test_hlcorestructure::transition_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Transition)

@given(instance=hlcorestructure::Type_strategy)
@settings(max_examples=50)
def test_hlcorestructure::type_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Type)

@given(instance=PlaceNode_strategy)
@settings(max_examples=50)
def test_placenode_instantiation(instance):
    assert isinstance(instance, PlaceNode)

@given(instance=hlcorestructure::Place_strategy)
@settings(max_examples=50)
def test_hlcorestructure::place_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Place)

@given(instance=hlcorestructure::RefTransition_strategy)
@settings(max_examples=50)
def test_hlcorestructure::reftransition_instantiation(instance):
    assert isinstance(instance, hlcorestructure::RefTransition)

@given(instance=hlcorestructure::RefPlace_strategy)
@settings(max_examples=50)
def test_hlcorestructure::refplace_instantiation(instance):
    assert isinstance(instance, hlcorestructure::RefPlace)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=hlcorestructure::TransitionNode_strategy)
@settings(max_examples=50)
def test_hlcorestructure::transitionnode_instantiation(instance):
    assert isinstance(instance, hlcorestructure::TransitionNode)

@given(instance=hlcorestructure::PlaceNode_strategy)
@settings(max_examples=50)
def test_hlcorestructure::placenode_instantiation(instance):
    assert isinstance(instance, hlcorestructure::PlaceNode)

@given(instance=hlcorestructure::HLMarking_strategy)
@settings(max_examples=50)
def test_hlcorestructure::hlmarking_instantiation(instance):
    assert isinstance(instance, hlcorestructure::HLMarking)

@given(instance=hlcorestructure::HLAnnotation_strategy)
@settings(max_examples=50)
def test_hlcorestructure::hlannotation_instantiation(instance):
    assert isinstance(instance, hlcorestructure::HLAnnotation)

@given(instance=hlcorestructure::Annotation_strategy)
@settings(max_examples=50)
def test_hlcorestructure::annotation_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Annotation)

@given(instance=hlcorestructure::Font_strategy)
@settings(max_examples=50)
def test_hlcorestructure::font_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Font)

@given(instance=hlcorestructure::Font_strategy)
def test_hlcorestructure::font_decoration_type(instance):
    assert isinstance(instance.decoration, str)


@given(instance=hlcorestructure::Font_strategy)
def test_hlcorestructure::font_decoration_setter(instance):
    original = instance.decoration
    instance.decoration = original
    assert instance.decoration == original

@given(instance=hlcorestructure::Font_strategy)
def test_hlcorestructure::font_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=hlcorestructure::Font_strategy)
def test_hlcorestructure::font_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=hlcorestructure::Font_strategy)
def test_hlcorestructure::font_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=hlcorestructure::Font_strategy)
def test_hlcorestructure::font_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=hlcorestructure::Font_strategy)
def test_hlcorestructure::font_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=hlcorestructure::Font_strategy)
def test_hlcorestructure::font_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=hlcorestructure::Font_strategy)
def test_hlcorestructure::font_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=hlcorestructure::Font_strategy)
def test_hlcorestructure::font_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=hlcorestructure::Font_strategy)
def test_hlcorestructure::font_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=hlcorestructure::Font_strategy)
def test_hlcorestructure::font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=hlcorestructure::Font_strategy)
def test_hlcorestructure::font_family_type(instance):
    assert isinstance(instance.family, str)


@given(instance=hlcorestructure::Font_strategy)
def test_hlcorestructure::font_family_setter(instance):
    original = instance.family
    instance.family = original
    assert instance.family == original

@given(instance=hlcorestructure::Coordinate_strategy)
@settings(max_examples=50)
def test_hlcorestructure::coordinate_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Coordinate)

@given(instance=hlcorestructure::Coordinate_strategy)
def test_hlcorestructure::coordinate_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=hlcorestructure::Coordinate_strategy)
def test_hlcorestructure::coordinate_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=hlcorestructure::Coordinate_strategy)
def test_hlcorestructure::coordinate_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=hlcorestructure::Coordinate_strategy)
def test_hlcorestructure::coordinate_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=Coordinate_strategy)
@settings(max_examples=50)
def test_coordinate_instantiation(instance):
    assert isinstance(instance, Coordinate)

@given(instance=hlcorestructure::Offset_strategy)
@settings(max_examples=50)
def test_hlcorestructure::offset_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Offset)

@given(instance=hlcorestructure::AnyObject_strategy)
@settings(max_examples=50)
def test_hlcorestructure::anyobject_instantiation(instance):
    assert isinstance(instance, hlcorestructure::AnyObject)

@given(instance=hlcorestructure::Label_strategy)
@settings(max_examples=50)
def test_hlcorestructure::label_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Label)

@given(instance=hlcorestructure::Graphics_strategy)
@settings(max_examples=50)
def test_hlcorestructure::graphics_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Graphics)

@given(instance=hlcorestructure::Line_strategy)
@settings(max_examples=50)
def test_hlcorestructure::line_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Line)

@given(instance=hlcorestructure::Line_strategy)
def test_hlcorestructure::line_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=hlcorestructure::Line_strategy)
def test_hlcorestructure::line_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=hlcorestructure::Line_strategy)
def test_hlcorestructure::line_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=hlcorestructure::Line_strategy)
def test_hlcorestructure::line_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=hlcorestructure::Line_strategy)
def test_hlcorestructure::line_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=hlcorestructure::Line_strategy)
def test_hlcorestructure::line_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=hlcorestructure::Line_strategy)
def test_hlcorestructure::line_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=hlcorestructure::Line_strategy)
def test_hlcorestructure::line_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=hlcorestructure::Fill_strategy)
@settings(max_examples=50)
def test_hlcorestructure::fill_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Fill)

@given(instance=hlcorestructure::Fill_strategy)
def test_hlcorestructure::fill_gradientrotation_type(instance):
    assert isinstance(instance.gradientrotation, str)


@given(instance=hlcorestructure::Fill_strategy)
def test_hlcorestructure::fill_gradientrotation_setter(instance):
    original = instance.gradientrotation
    instance.gradientrotation = original
    assert instance.gradientrotation == original

@given(instance=hlcorestructure::Fill_strategy)
def test_hlcorestructure::fill_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=hlcorestructure::Fill_strategy)
def test_hlcorestructure::fill_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=hlcorestructure::Fill_strategy)
def test_hlcorestructure::fill_gradientcolor_type(instance):
    assert isinstance(instance.gradientcolor, str)


@given(instance=hlcorestructure::Fill_strategy)
def test_hlcorestructure::fill_gradientcolor_setter(instance):
    original = instance.gradientcolor
    instance.gradientcolor = original
    assert instance.gradientcolor == original

@given(instance=hlcorestructure::Fill_strategy)
def test_hlcorestructure::fill_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=hlcorestructure::Fill_strategy)
def test_hlcorestructure::fill_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=hlcorestructure::Dimension_strategy)
@settings(max_examples=50)
def test_hlcorestructure::dimension_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Dimension)

@given(instance=hlcorestructure::Position_strategy)
@settings(max_examples=50)
def test_hlcorestructure::position_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Position)

@given(instance=Graphics_strategy)
@settings(max_examples=50)
def test_graphics_instantiation(instance):
    assert isinstance(instance, Graphics)

@given(instance=hlcorestructure::AnnotationGraphics_strategy)
@settings(max_examples=50)
def test_hlcorestructure::annotationgraphics_instantiation(instance):
    assert isinstance(instance, hlcorestructure::AnnotationGraphics)

@given(instance=hlcorestructure::ArcGraphics_strategy)
@settings(max_examples=50)
def test_hlcorestructure::arcgraphics_instantiation(instance):
    assert isinstance(instance, hlcorestructure::ArcGraphics)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=hlcorestructure::HLCoreAnnotation_strategy)
@settings(max_examples=50)
def test_hlcorestructure::hlcoreannotation_instantiation(instance):
    assert isinstance(instance, hlcorestructure::HLCoreAnnotation)

@given(instance=hlcorestructure::HLCoreAnnotation_strategy)
def test_hlcorestructure::hlcoreannotation_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=hlcorestructure::HLCoreAnnotation_strategy)
def test_hlcorestructure::hlcoreannotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=hlcorestructure::ToolInfo_strategy)
@settings(max_examples=50)
def test_hlcorestructure::toolinfo_instantiation(instance):
    assert isinstance(instance, hlcorestructure::ToolInfo)

@given(instance=hlcorestructure::ToolInfo_strategy)
def test_hlcorestructure::toolinfo_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=hlcorestructure::ToolInfo_strategy)
def test_hlcorestructure::toolinfo_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=hlcorestructure::ToolInfo_strategy)
def test_hlcorestructure::toolinfo_toolInfoGrammarURI_type(instance):
    assert isinstance(instance.toolInfoGrammarURI, str)


@given(instance=hlcorestructure::ToolInfo_strategy)
def test_hlcorestructure::toolinfo_toolInfoGrammarURI_setter(instance):
    original = instance.toolInfoGrammarURI
    instance.toolInfoGrammarURI = original
    assert instance.toolInfoGrammarURI == original

@given(instance=hlcorestructure::ToolInfo_strategy)
def test_hlcorestructure::toolinfo_formattedXMLBuffer_type(instance):
    assert isinstance(instance.formattedXMLBuffer, str)


@given(instance=hlcorestructure::ToolInfo_strategy)
def test_hlcorestructure::toolinfo_formattedXMLBuffer_setter(instance):
    original = instance.formattedXMLBuffer
    instance.formattedXMLBuffer = original
    assert instance.formattedXMLBuffer == original

@given(instance=hlcorestructure::ToolInfo_strategy)
def test_hlcorestructure::toolinfo_tool_type(instance):
    assert isinstance(instance.tool, str)


@given(instance=hlcorestructure::ToolInfo_strategy)
def test_hlcorestructure::toolinfo_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=hlcorestructure::Name_strategy)
@settings(max_examples=50)
def test_hlcorestructure::name_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Name)

@given(instance=hlcorestructure::Name_strategy)
def test_hlcorestructure::name_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=hlcorestructure::Name_strategy)
def test_hlcorestructure::name_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=hlcorestructure::NodeGraphics_strategy)
@settings(max_examples=50)
def test_hlcorestructure::nodegraphics_instantiation(instance):
    assert isinstance(instance, hlcorestructure::NodeGraphics)

@given(instance=hlcorestructure::PnObject_strategy)
@settings(max_examples=50)
def test_hlcorestructure::pnobject_instantiation(instance):
    assert isinstance(instance, hlcorestructure::PnObject)

@given(instance=hlcorestructure::PnObject_strategy)
def test_hlcorestructure::pnobject_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=hlcorestructure::PnObject_strategy)
def test_hlcorestructure::pnobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=PnObject_strategy)
@settings(max_examples=50)
def test_pnobject_instantiation(instance):
    assert isinstance(instance, PnObject)

@given(instance=hlcorestructure::Node_strategy)
@settings(max_examples=50)
def test_hlcorestructure::node_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Node)

@given(instance=hlcorestructure::Arc_strategy)
@settings(max_examples=50)
def test_hlcorestructure::arc_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Arc)

@given(instance=hlcorestructure::Page_strategy)
@settings(max_examples=50)
def test_hlcorestructure::page_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Page)

@given(instance=hlcorestructure::Declaration_strategy)
@settings(max_examples=50)
def test_hlcorestructure::declaration_instantiation(instance):
    assert isinstance(instance, hlcorestructure::Declaration)

@given(instance=hlcorestructure::PetriNet_strategy)
@settings(max_examples=50)
def test_hlcorestructure::petrinet_instantiation(instance):
    assert isinstance(instance, hlcorestructure::PetriNet)

@given(instance=hlcorestructure::PetriNet_strategy)
def test_hlcorestructure::petrinet_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=hlcorestructure::PetriNet_strategy)
def test_hlcorestructure::petrinet_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=hlcorestructure::PetriNet_strategy)
def test_hlcorestructure::petrinet_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=hlcorestructure::PetriNet_strategy)
def test_hlcorestructure::petrinet_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=hlcorestructure::PetriNetDoc_strategy)
@settings(max_examples=50)
def test_hlcorestructure::petrinetdoc_instantiation(instance):
    assert isinstance(instance, hlcorestructure::PetriNetDoc)

@given(instance=hlcorestructure::PetriNetDoc_strategy)
def test_hlcorestructure::petrinetdoc_xmlns_type(instance):
    assert isinstance(instance.xmlns, str)


@given(instance=hlcorestructure::PetriNetDoc_strategy)
def test_hlcorestructure::petrinetdoc_xmlns_setter(instance):
    original = instance.xmlns
    instance.xmlns = original
    assert instance.xmlns == original
