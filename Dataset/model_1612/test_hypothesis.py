import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    hlcorestructure_Declarations,
    hlcorestructure_Term,
    hlcorestructure_Sort,
    HLCoreAnnotation,
    Label,
    hlcorestructure_Attribute,
    hlcorestructure_Condition,
    TransitionNode,
    hlcorestructure_Transition,
    hlcorestructure_HLMarking,
    hlcorestructure_Type,
    PlaceNode,
    hlcorestructure_Place,
    hlcorestructure_RefTransition,
    hlcorestructure_RefPlace,
    Node,
    hlcorestructure_TransitionNode,
    hlcorestructure_PlaceNode,
    hlcorestructure_HLAnnotation,
    hlcorestructure_Annotation,
    hlcorestructure_Font,
    hlcorestructure_AnyObject,
    hlcorestructure_Label,
    Coordinate,
    hlcorestructure_Offset,
    hlcorestructure_Coordinate,
    hlcorestructure_Graphics,
    hlcorestructure_Line,
    hlcorestructure_Fill,
    hlcorestructure_Dimension,
    hlcorestructure_Position,
    Graphics,
    hlcorestructure_AnnotationGraphics,
    hlcorestructure_ArcGraphics,
    hlcorestructure_PnObject,
    PnObject,
    hlcorestructure_Node,
    hlcorestructure_Arc,
    Annotation,
    hlcorestructure_HLCoreAnnotation,
    hlcorestructure_NodeGraphics,
    hlcorestructure_Declaration,
    hlcorestructure_ToolInfo,
    hlcorestructure_Name,
    hlcorestructure_Page,
    hlcorestructure_PetriNet,
    hlcorestructure_PetriNetDoc,
    PNType,
    CSS2FontStyle,
    CSS2FontWeight,
    FontAlign,
    LineShape,
    FontDecoration,
    Gradient,
    LineStyle,
    CSS2Color,
    CSS2FontSize,
    CSS2FontFamily,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hlcorestructure_declarations_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Declarations)


def test_hlcorestructure_declarations_constructor_exists():
    assert callable(hlcorestructure_Declarations.__init__)


def test_hlcorestructure_declarations_constructor_args():
    sig = inspect.signature(hlcorestructure_Declarations.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_term_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Term)


def test_hlcorestructure_term_constructor_exists():
    assert callable(hlcorestructure_Term.__init__)


def test_hlcorestructure_term_constructor_args():
    sig = inspect.signature(hlcorestructure_Term.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_sort_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Sort)


def test_hlcorestructure_sort_constructor_exists():
    assert callable(hlcorestructure_Sort.__init__)


def test_hlcorestructure_sort_constructor_args():
    sig = inspect.signature(hlcorestructure_Sort.__init__)
    params = list(sig.parameters.keys())



def test_hlcoreannotation_is_not_abstract():
    assert not inspect.isabstract(HLCoreAnnotation)


def test_hlcoreannotation_constructor_exists():
    assert callable(HLCoreAnnotation.__init__)


def test_hlcoreannotation_constructor_args():
    sig = inspect.signature(HLCoreAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_attribute_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Attribute)


def test_hlcorestructure_attribute_constructor_exists():
    assert callable(hlcorestructure_Attribute.__init__)


def test_hlcorestructure_attribute_constructor_args():
    sig = inspect.signature(hlcorestructure_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_condition_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Condition)


def test_hlcorestructure_condition_constructor_exists():
    assert callable(hlcorestructure_Condition.__init__)


def test_hlcorestructure_condition_constructor_args():
    sig = inspect.signature(hlcorestructure_Condition.__init__)
    params = list(sig.parameters.keys())



def test_transitionnode_is_not_abstract():
    assert not inspect.isabstract(TransitionNode)


def test_transitionnode_constructor_exists():
    assert callable(TransitionNode.__init__)


def test_transitionnode_constructor_args():
    sig = inspect.signature(TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_transition_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Transition)


def test_hlcorestructure_transition_constructor_exists():
    assert callable(hlcorestructure_Transition.__init__)


def test_hlcorestructure_transition_constructor_args():
    sig = inspect.signature(hlcorestructure_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_hlmarking_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_HLMarking)


def test_hlcorestructure_hlmarking_constructor_exists():
    assert callable(hlcorestructure_HLMarking.__init__)


def test_hlcorestructure_hlmarking_constructor_args():
    sig = inspect.signature(hlcorestructure_HLMarking.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_type_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Type)


def test_hlcorestructure_type_constructor_exists():
    assert callable(hlcorestructure_Type.__init__)


def test_hlcorestructure_type_constructor_args():
    sig = inspect.signature(hlcorestructure_Type.__init__)
    params = list(sig.parameters.keys())



def test_placenode_is_not_abstract():
    assert not inspect.isabstract(PlaceNode)


def test_placenode_constructor_exists():
    assert callable(PlaceNode.__init__)


def test_placenode_constructor_args():
    sig = inspect.signature(PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_place_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Place)


def test_hlcorestructure_place_constructor_exists():
    assert callable(hlcorestructure_Place.__init__)


def test_hlcorestructure_place_constructor_args():
    sig = inspect.signature(hlcorestructure_Place.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_reftransition_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_RefTransition)


def test_hlcorestructure_reftransition_constructor_exists():
    assert callable(hlcorestructure_RefTransition.__init__)


def test_hlcorestructure_reftransition_constructor_args():
    sig = inspect.signature(hlcorestructure_RefTransition.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_refplace_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_RefPlace)


def test_hlcorestructure_refplace_constructor_exists():
    assert callable(hlcorestructure_RefPlace.__init__)


def test_hlcorestructure_refplace_constructor_args():
    sig = inspect.signature(hlcorestructure_RefPlace.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_transitionnode_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_TransitionNode)


def test_hlcorestructure_transitionnode_constructor_exists():
    assert callable(hlcorestructure_TransitionNode.__init__)


def test_hlcorestructure_transitionnode_constructor_args():
    sig = inspect.signature(hlcorestructure_TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_placenode_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_PlaceNode)


def test_hlcorestructure_placenode_constructor_exists():
    assert callable(hlcorestructure_PlaceNode.__init__)


def test_hlcorestructure_placenode_constructor_args():
    sig = inspect.signature(hlcorestructure_PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_hlannotation_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_HLAnnotation)


def test_hlcorestructure_hlannotation_constructor_exists():
    assert callable(hlcorestructure_HLAnnotation.__init__)


def test_hlcorestructure_hlannotation_constructor_args():
    sig = inspect.signature(hlcorestructure_HLAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_annotation_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Annotation)


def test_hlcorestructure_annotation_constructor_exists():
    assert callable(hlcorestructure_Annotation.__init__)


def test_hlcorestructure_annotation_constructor_args():
    sig = inspect.signature(hlcorestructure_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_font_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Font)


def test_hlcorestructure_font_constructor_exists():
    assert callable(hlcorestructure_Font.__init__)


def test_hlcorestructure_font_constructor_args():
    sig = inspect.signature(hlcorestructure_Font.__init__)
    params = list(sig.parameters.keys())
    assert "decoration" in params, "Missing parameter 'decoration'"
    assert "align" in params, "Missing parameter 'align'"
    assert "size" in params, "Missing parameter 'size'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "family" in params, "Missing parameter 'family'"
    assert "style" in params, "Missing parameter 'style'"

def test_hlcorestructure_font_has_decoration():
    assert hasattr(hlcorestructure_Font, "decoration")
    descriptor = None
    for klass in hlcorestructure_Font.__mro__:
        if "decoration" in klass.__dict__:
            descriptor = klass.__dict__["decoration"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_font_has_align():
    assert hasattr(hlcorestructure_Font, "align")
    descriptor = None
    for klass in hlcorestructure_Font.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_font_has_size():
    assert hasattr(hlcorestructure_Font, "size")
    descriptor = None
    for klass in hlcorestructure_Font.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_font_has_rotation():
    assert hasattr(hlcorestructure_Font, "rotation")
    descriptor = None
    for klass in hlcorestructure_Font.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_font_has_weight():
    assert hasattr(hlcorestructure_Font, "weight")
    descriptor = None
    for klass in hlcorestructure_Font.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_font_has_family():
    assert hasattr(hlcorestructure_Font, "family")
    descriptor = None
    for klass in hlcorestructure_Font.__mro__:
        if "family" in klass.__dict__:
            descriptor = klass.__dict__["family"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_font_has_style():
    assert hasattr(hlcorestructure_Font, "style")
    descriptor = None
    for klass in hlcorestructure_Font.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure_anyobject_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_AnyObject)


def test_hlcorestructure_anyobject_constructor_exists():
    assert callable(hlcorestructure_AnyObject.__init__)


def test_hlcorestructure_anyobject_constructor_args():
    sig = inspect.signature(hlcorestructure_AnyObject.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_label_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Label)


def test_hlcorestructure_label_constructor_exists():
    assert callable(hlcorestructure_Label.__init__)


def test_hlcorestructure_label_constructor_args():
    sig = inspect.signature(hlcorestructure_Label.__init__)
    params = list(sig.parameters.keys())



def test_coordinate_is_not_abstract():
    assert not inspect.isabstract(Coordinate)


def test_coordinate_constructor_exists():
    assert callable(Coordinate.__init__)


def test_coordinate_constructor_args():
    sig = inspect.signature(Coordinate.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_offset_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Offset)


def test_hlcorestructure_offset_constructor_exists():
    assert callable(hlcorestructure_Offset.__init__)


def test_hlcorestructure_offset_constructor_args():
    sig = inspect.signature(hlcorestructure_Offset.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_coordinate_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Coordinate)


def test_hlcorestructure_coordinate_constructor_exists():
    assert callable(hlcorestructure_Coordinate.__init__)


def test_hlcorestructure_coordinate_constructor_args():
    sig = inspect.signature(hlcorestructure_Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_hlcorestructure_coordinate_has_x():
    assert hasattr(hlcorestructure_Coordinate, "x")
    descriptor = None
    for klass in hlcorestructure_Coordinate.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_coordinate_has_y():
    assert hasattr(hlcorestructure_Coordinate, "y")
    descriptor = None
    for klass in hlcorestructure_Coordinate.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure_graphics_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Graphics)


def test_hlcorestructure_graphics_constructor_exists():
    assert callable(hlcorestructure_Graphics.__init__)


def test_hlcorestructure_graphics_constructor_args():
    sig = inspect.signature(hlcorestructure_Graphics.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_line_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Line)


def test_hlcorestructure_line_constructor_exists():
    assert callable(hlcorestructure_Line.__init__)


def test_hlcorestructure_line_constructor_args():
    sig = inspect.signature(hlcorestructure_Line.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "style" in params, "Missing parameter 'style'"
    assert "color" in params, "Missing parameter 'color'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_hlcorestructure_line_has_width():
    assert hasattr(hlcorestructure_Line, "width")
    descriptor = None
    for klass in hlcorestructure_Line.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_line_has_style():
    assert hasattr(hlcorestructure_Line, "style")
    descriptor = None
    for klass in hlcorestructure_Line.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_line_has_color():
    assert hasattr(hlcorestructure_Line, "color")
    descriptor = None
    for klass in hlcorestructure_Line.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_line_has_shape():
    assert hasattr(hlcorestructure_Line, "shape")
    descriptor = None
    for klass in hlcorestructure_Line.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure_fill_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Fill)


def test_hlcorestructure_fill_constructor_exists():
    assert callable(hlcorestructure_Fill.__init__)


def test_hlcorestructure_fill_constructor_args():
    sig = inspect.signature(hlcorestructure_Fill.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "gradientrotation" in params, "Missing parameter 'gradientrotation'"
    assert "image" in params, "Missing parameter 'image'"
    assert "gradientcolor" in params, "Missing parameter 'gradientcolor'"

def test_hlcorestructure_fill_has_color():
    assert hasattr(hlcorestructure_Fill, "color")
    descriptor = None
    for klass in hlcorestructure_Fill.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_fill_has_gradientrotation():
    assert hasattr(hlcorestructure_Fill, "gradientrotation")
    descriptor = None
    for klass in hlcorestructure_Fill.__mro__:
        if "gradientrotation" in klass.__dict__:
            descriptor = klass.__dict__["gradientrotation"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_fill_has_image():
    assert hasattr(hlcorestructure_Fill, "image")
    descriptor = None
    for klass in hlcorestructure_Fill.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_fill_has_gradientcolor():
    assert hasattr(hlcorestructure_Fill, "gradientcolor")
    descriptor = None
    for klass in hlcorestructure_Fill.__mro__:
        if "gradientcolor" in klass.__dict__:
            descriptor = klass.__dict__["gradientcolor"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure_dimension_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Dimension)


def test_hlcorestructure_dimension_constructor_exists():
    assert callable(hlcorestructure_Dimension.__init__)


def test_hlcorestructure_dimension_constructor_args():
    sig = inspect.signature(hlcorestructure_Dimension.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_position_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Position)


def test_hlcorestructure_position_constructor_exists():
    assert callable(hlcorestructure_Position.__init__)


def test_hlcorestructure_position_constructor_args():
    sig = inspect.signature(hlcorestructure_Position.__init__)
    params = list(sig.parameters.keys())



def test_graphics_is_not_abstract():
    assert not inspect.isabstract(Graphics)


def test_graphics_constructor_exists():
    assert callable(Graphics.__init__)


def test_graphics_constructor_args():
    sig = inspect.signature(Graphics.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_annotationgraphics_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_AnnotationGraphics)


def test_hlcorestructure_annotationgraphics_constructor_exists():
    assert callable(hlcorestructure_AnnotationGraphics.__init__)


def test_hlcorestructure_annotationgraphics_constructor_args():
    sig = inspect.signature(hlcorestructure_AnnotationGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_arcgraphics_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_ArcGraphics)


def test_hlcorestructure_arcgraphics_constructor_exists():
    assert callable(hlcorestructure_ArcGraphics.__init__)


def test_hlcorestructure_arcgraphics_constructor_args():
    sig = inspect.signature(hlcorestructure_ArcGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_pnobject_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_PnObject)


def test_hlcorestructure_pnobject_constructor_exists():
    assert callable(hlcorestructure_PnObject.__init__)


def test_hlcorestructure_pnobject_constructor_args():
    sig = inspect.signature(hlcorestructure_PnObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_hlcorestructure_pnobject_has_id():
    assert hasattr(hlcorestructure_PnObject, "id")
    descriptor = None
    for klass in hlcorestructure_PnObject.__mro__:
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



def test_hlcorestructure_node_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Node)


def test_hlcorestructure_node_constructor_exists():
    assert callable(hlcorestructure_Node.__init__)


def test_hlcorestructure_node_constructor_args():
    sig = inspect.signature(hlcorestructure_Node.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_arc_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Arc)


def test_hlcorestructure_arc_constructor_exists():
    assert callable(hlcorestructure_Arc.__init__)


def test_hlcorestructure_arc_constructor_args():
    sig = inspect.signature(hlcorestructure_Arc.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_hlcoreannotation_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_HLCoreAnnotation)


def test_hlcorestructure_hlcoreannotation_constructor_exists():
    assert callable(hlcorestructure_HLCoreAnnotation.__init__)


def test_hlcorestructure_hlcoreannotation_constructor_args():
    sig = inspect.signature(hlcorestructure_HLCoreAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_hlcorestructure_hlcoreannotation_has_text():
    assert hasattr(hlcorestructure_HLCoreAnnotation, "text")
    descriptor = None
    for klass in hlcorestructure_HLCoreAnnotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure_nodegraphics_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_NodeGraphics)


def test_hlcorestructure_nodegraphics_constructor_exists():
    assert callable(hlcorestructure_NodeGraphics.__init__)


def test_hlcorestructure_nodegraphics_constructor_args():
    sig = inspect.signature(hlcorestructure_NodeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_declaration_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Declaration)


def test_hlcorestructure_declaration_constructor_exists():
    assert callable(hlcorestructure_Declaration.__init__)


def test_hlcorestructure_declaration_constructor_args():
    sig = inspect.signature(hlcorestructure_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_toolinfo_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_ToolInfo)


def test_hlcorestructure_toolinfo_constructor_exists():
    assert callable(hlcorestructure_ToolInfo.__init__)


def test_hlcorestructure_toolinfo_constructor_args():
    sig = inspect.signature(hlcorestructure_ToolInfo.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "toolInfoGrammarURI" in params, "Missing parameter 'toolInfoGrammarURI'"
    assert "formattedXMLBuffer" in params, "Missing parameter 'formattedXMLBuffer'"
    assert "tool" in params, "Missing parameter 'tool'"

def test_hlcorestructure_toolinfo_has_version():
    assert hasattr(hlcorestructure_ToolInfo, "version")
    descriptor = None
    for klass in hlcorestructure_ToolInfo.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_toolinfo_has_toolInfoGrammarURI():
    assert hasattr(hlcorestructure_ToolInfo, "toolInfoGrammarURI")
    descriptor = None
    for klass in hlcorestructure_ToolInfo.__mro__:
        if "toolInfoGrammarURI" in klass.__dict__:
            descriptor = klass.__dict__["toolInfoGrammarURI"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_toolinfo_has_formattedXMLBuffer():
    assert hasattr(hlcorestructure_ToolInfo, "formattedXMLBuffer")
    descriptor = None
    for klass in hlcorestructure_ToolInfo.__mro__:
        if "formattedXMLBuffer" in klass.__dict__:
            descriptor = klass.__dict__["formattedXMLBuffer"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_toolinfo_has_tool():
    assert hasattr(hlcorestructure_ToolInfo, "tool")
    descriptor = None
    for klass in hlcorestructure_ToolInfo.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure_name_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Name)


def test_hlcorestructure_name_constructor_exists():
    assert callable(hlcorestructure_Name.__init__)


def test_hlcorestructure_name_constructor_args():
    sig = inspect.signature(hlcorestructure_Name.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_hlcorestructure_name_has_text():
    assert hasattr(hlcorestructure_Name, "text")
    descriptor = None
    for klass in hlcorestructure_Name.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure_page_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_Page)


def test_hlcorestructure_page_constructor_exists():
    assert callable(hlcorestructure_Page.__init__)


def test_hlcorestructure_page_constructor_args():
    sig = inspect.signature(hlcorestructure_Page.__init__)
    params = list(sig.parameters.keys())



def test_hlcorestructure_petrinet_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_PetriNet)


def test_hlcorestructure_petrinet_constructor_exists():
    assert callable(hlcorestructure_PetriNet.__init__)


def test_hlcorestructure_petrinet_constructor_args():
    sig = inspect.signature(hlcorestructure_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

def test_hlcorestructure_petrinet_has_type():
    assert hasattr(hlcorestructure_PetriNet, "type")
    descriptor = None
    for klass in hlcorestructure_PetriNet.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hlcorestructure_petrinet_has_id():
    assert hasattr(hlcorestructure_PetriNet, "id")
    descriptor = None
    for klass in hlcorestructure_PetriNet.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_hlcorestructure_petrinetdoc_is_not_abstract():
    assert not inspect.isabstract(hlcorestructure_PetriNetDoc)


def test_hlcorestructure_petrinetdoc_constructor_exists():
    assert callable(hlcorestructure_PetriNetDoc.__init__)


def test_hlcorestructure_petrinetdoc_constructor_args():
    sig = inspect.signature(hlcorestructure_PetriNetDoc.__init__)
    params = list(sig.parameters.keys())
    assert "xmlns" in params, "Missing parameter 'xmlns'"

def test_hlcorestructure_petrinetdoc_has_xmlns():
    assert hasattr(hlcorestructure_PetriNetDoc, "xmlns")
    descriptor = None
    for klass in hlcorestructure_PetriNetDoc.__mro__:
        if "xmlns" in klass.__dict__:
            descriptor = klass.__dict__["xmlns"]
            break
    assert isinstance(descriptor, property)

def test_pntype_exists():
    # Check that the Enumeration exists
    assert PNType is not None

def test_pntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PNType]
    expected_literals = [
        "HLPN",
        "COREMODEL",
        "PTNET",
        "SYMNET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PNType"

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

def test_css2fontweight_exists():
    # Check that the Enumeration exists
    assert CSS2FontWeight is not None

def test_css2fontweight_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontWeight]
    expected_literals = [
        "BOLDER",
        "BOLD",
        "LIGHTER",
        "NORMAL",
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
        "LINE",
        "CURVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineShape"

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
        "VERTICAL",
        "DIAGONAL",
        "HORIZONTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gradient"

def test_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "SOLID",
        "DASH",
        "DOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"

def test_css2color_exists():
    # Check that the Enumeration exists
    assert CSS2Color is not None

def test_css2color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2Color]
    expected_literals = [
        "AQUA",
        "TEAL",
        "BLUE",
        "OLIVE",
        "MAROON",
        "FUCHSIA",
        "GRAY",
        "YELLOW",
        "GREEN",
        "NAVY",
        "ORANGE",
        "RED",
        "BLACK",
        "SILVER",
        "PURPLE",
        "LIME",
        "WHITE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2Color"

def test_css2fontsize_exists():
    # Check that the Enumeration exists
    assert CSS2FontSize is not None

def test_css2fontsize_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontSize]
    expected_literals = [
        "XXLARGE",
        "MEDIUM",
        "LARGE",
        "XSMALL",
        "XXSMALL",
        "SMALL",
        "XLARGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontSize"

def test_css2fontfamily_exists():
    # Check that the Enumeration exists
    assert CSS2FontFamily is not None

def test_css2fontfamily_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontFamily]
    expected_literals = [
        "ARIAL",
        "TREBUCHET",
        "TIMES",
        "VERDANA",
        "GEORGIA",
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
hlcorestructure_Declarations_strategy = st.builds(
    hlcorestructure_Declarations,
)
hlcorestructure_Term_strategy = st.builds(
    hlcorestructure_Term,
)
hlcorestructure_Sort_strategy = st.builds(
    hlcorestructure_Sort,
)
HLCoreAnnotation_strategy = st.builds(
    HLCoreAnnotation,
)
Label_strategy = st.builds(
    Label,
)
hlcorestructure_Attribute_strategy = st.builds(
    hlcorestructure_Attribute,
)
hlcorestructure_Condition_strategy = st.builds(
    hlcorestructure_Condition,
)
TransitionNode_strategy = st.builds(
    TransitionNode,
)
hlcorestructure_Transition_strategy = st.builds(
    hlcorestructure_Transition,
)
hlcorestructure_HLMarking_strategy = st.builds(
    hlcorestructure_HLMarking,
)
hlcorestructure_Type_strategy = st.builds(
    hlcorestructure_Type,
)
PlaceNode_strategy = st.builds(
    PlaceNode,
)
hlcorestructure_Place_strategy = st.builds(
    hlcorestructure_Place,
)
hlcorestructure_RefTransition_strategy = st.builds(
    hlcorestructure_RefTransition,
)
hlcorestructure_RefPlace_strategy = st.builds(
    hlcorestructure_RefPlace,
)
Node_strategy = st.builds(
    Node,
)
hlcorestructure_TransitionNode_strategy = st.builds(
    hlcorestructure_TransitionNode,
)
hlcorestructure_PlaceNode_strategy = st.builds(
    hlcorestructure_PlaceNode,
)
hlcorestructure_HLAnnotation_strategy = st.builds(
    hlcorestructure_HLAnnotation,
)
hlcorestructure_Annotation_strategy = st.builds(
    hlcorestructure_Annotation,
)
hlcorestructure_Font_strategy = st.builds(
    hlcorestructure_Font,
    decoration=
        safe_text,
    align=
        safe_text,
    size=
        safe_text,
    rotation=
        safe_text,
    weight=
        safe_text,
    family=
        safe_text,
    style=
        safe_text
)
hlcorestructure_AnyObject_strategy = st.builds(
    hlcorestructure_AnyObject,
)
hlcorestructure_Label_strategy = st.builds(
    hlcorestructure_Label,
)
Coordinate_strategy = st.builds(
    Coordinate,
)
hlcorestructure_Offset_strategy = st.builds(
    hlcorestructure_Offset,
)
hlcorestructure_Coordinate_strategy = st.builds(
    hlcorestructure_Coordinate,
    x=
        safe_text,
    y=
        safe_text
)
hlcorestructure_Graphics_strategy = st.builds(
    hlcorestructure_Graphics,
)
hlcorestructure_Line_strategy = st.builds(
    hlcorestructure_Line,
    width=
        safe_text,
    style=
        safe_text,
    color=
        safe_text,
    shape=
        safe_text
)
hlcorestructure_Fill_strategy = st.builds(
    hlcorestructure_Fill,
    color=
        safe_text,
    gradientrotation=
        safe_text,
    image=
        safe_text,
    gradientcolor=
        safe_text
)
hlcorestructure_Dimension_strategy = st.builds(
    hlcorestructure_Dimension,
)
hlcorestructure_Position_strategy = st.builds(
    hlcorestructure_Position,
)
Graphics_strategy = st.builds(
    Graphics,
)
hlcorestructure_AnnotationGraphics_strategy = st.builds(
    hlcorestructure_AnnotationGraphics,
)
hlcorestructure_ArcGraphics_strategy = st.builds(
    hlcorestructure_ArcGraphics,
)
hlcorestructure_PnObject_strategy = st.builds(
    hlcorestructure_PnObject,
    id=
        safe_text
)
PnObject_strategy = st.builds(
    PnObject,
)
hlcorestructure_Node_strategy = st.builds(
    hlcorestructure_Node,
)
hlcorestructure_Arc_strategy = st.builds(
    hlcorestructure_Arc,
)
Annotation_strategy = st.builds(
    Annotation,
)
hlcorestructure_HLCoreAnnotation_strategy = st.builds(
    hlcorestructure_HLCoreAnnotation,
    text=
        safe_text
)
hlcorestructure_NodeGraphics_strategy = st.builds(
    hlcorestructure_NodeGraphics,
)
hlcorestructure_Declaration_strategy = st.builds(
    hlcorestructure_Declaration,
)
hlcorestructure_ToolInfo_strategy = st.builds(
    hlcorestructure_ToolInfo,
    version=
        safe_text,
    toolInfoGrammarURI=
        safe_text,
    formattedXMLBuffer=
        safe_text,
    tool=
        safe_text
)
hlcorestructure_Name_strategy = st.builds(
    hlcorestructure_Name,
    text=
        safe_text
)
hlcorestructure_Page_strategy = st.builds(
    hlcorestructure_Page,
)
hlcorestructure_PetriNet_strategy = st.builds(
    hlcorestructure_PetriNet,
    type=
        safe_text,
    id=
        safe_text
)
hlcorestructure_PetriNetDoc_strategy = st.builds(
    hlcorestructure_PetriNetDoc,
    xmlns=
        safe_text
)

@given(instance=hlcorestructure_Declarations_strategy)
@settings(max_examples=50)
def test_hlcorestructure_declarations_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Declarations)

@given(instance=hlcorestructure_Term_strategy)
@settings(max_examples=50)
def test_hlcorestructure_term_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Term)

@given(instance=hlcorestructure_Sort_strategy)
@settings(max_examples=50)
def test_hlcorestructure_sort_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Sort)

@given(instance=HLCoreAnnotation_strategy)
@settings(max_examples=50)
def test_hlcoreannotation_instantiation(instance):
    assert isinstance(instance, HLCoreAnnotation)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=hlcorestructure_Attribute_strategy)
@settings(max_examples=50)
def test_hlcorestructure_attribute_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Attribute)

@given(instance=hlcorestructure_Condition_strategy)
@settings(max_examples=50)
def test_hlcorestructure_condition_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Condition)

@given(instance=TransitionNode_strategy)
@settings(max_examples=50)
def test_transitionnode_instantiation(instance):
    assert isinstance(instance, TransitionNode)

@given(instance=hlcorestructure_Transition_strategy)
@settings(max_examples=50)
def test_hlcorestructure_transition_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Transition)

@given(instance=hlcorestructure_HLMarking_strategy)
@settings(max_examples=50)
def test_hlcorestructure_hlmarking_instantiation(instance):
    assert isinstance(instance, hlcorestructure_HLMarking)

@given(instance=hlcorestructure_Type_strategy)
@settings(max_examples=50)
def test_hlcorestructure_type_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Type)

@given(instance=PlaceNode_strategy)
@settings(max_examples=50)
def test_placenode_instantiation(instance):
    assert isinstance(instance, PlaceNode)

@given(instance=hlcorestructure_Place_strategy)
@settings(max_examples=50)
def test_hlcorestructure_place_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Place)

@given(instance=hlcorestructure_RefTransition_strategy)
@settings(max_examples=50)
def test_hlcorestructure_reftransition_instantiation(instance):
    assert isinstance(instance, hlcorestructure_RefTransition)

@given(instance=hlcorestructure_RefPlace_strategy)
@settings(max_examples=50)
def test_hlcorestructure_refplace_instantiation(instance):
    assert isinstance(instance, hlcorestructure_RefPlace)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=hlcorestructure_TransitionNode_strategy)
@settings(max_examples=50)
def test_hlcorestructure_transitionnode_instantiation(instance):
    assert isinstance(instance, hlcorestructure_TransitionNode)

@given(instance=hlcorestructure_PlaceNode_strategy)
@settings(max_examples=50)
def test_hlcorestructure_placenode_instantiation(instance):
    assert isinstance(instance, hlcorestructure_PlaceNode)

@given(instance=hlcorestructure_HLAnnotation_strategy)
@settings(max_examples=50)
def test_hlcorestructure_hlannotation_instantiation(instance):
    assert isinstance(instance, hlcorestructure_HLAnnotation)

@given(instance=hlcorestructure_Annotation_strategy)
@settings(max_examples=50)
def test_hlcorestructure_annotation_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Annotation)

@given(instance=hlcorestructure_Font_strategy)
@settings(max_examples=50)
def test_hlcorestructure_font_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Font)



@given(instance=hlcorestructure_Font_strategy)
def test_hlcorestructure_font_decoration_setter(instance):
    original = instance.decoration
    instance.decoration = original
    assert instance.decoration == original



@given(instance=hlcorestructure_Font_strategy)
def test_hlcorestructure_font_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=hlcorestructure_Font_strategy)
def test_hlcorestructure_font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=hlcorestructure_Font_strategy)
def test_hlcorestructure_font_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=hlcorestructure_Font_strategy)
def test_hlcorestructure_font_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=hlcorestructure_Font_strategy)
def test_hlcorestructure_font_family_setter(instance):
    original = instance.family
    instance.family = original
    assert instance.family == original



@given(instance=hlcorestructure_Font_strategy)
def test_hlcorestructure_font_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=hlcorestructure_AnyObject_strategy)
@settings(max_examples=50)
def test_hlcorestructure_anyobject_instantiation(instance):
    assert isinstance(instance, hlcorestructure_AnyObject)

@given(instance=hlcorestructure_Label_strategy)
@settings(max_examples=50)
def test_hlcorestructure_label_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Label)

@given(instance=Coordinate_strategy)
@settings(max_examples=50)
def test_coordinate_instantiation(instance):
    assert isinstance(instance, Coordinate)

@given(instance=hlcorestructure_Offset_strategy)
@settings(max_examples=50)
def test_hlcorestructure_offset_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Offset)

@given(instance=hlcorestructure_Coordinate_strategy)
@settings(max_examples=50)
def test_hlcorestructure_coordinate_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Coordinate)



@given(instance=hlcorestructure_Coordinate_strategy)
def test_hlcorestructure_coordinate_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=hlcorestructure_Coordinate_strategy)
def test_hlcorestructure_coordinate_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=hlcorestructure_Graphics_strategy)
@settings(max_examples=50)
def test_hlcorestructure_graphics_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Graphics)

@given(instance=hlcorestructure_Line_strategy)
@settings(max_examples=50)
def test_hlcorestructure_line_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Line)



@given(instance=hlcorestructure_Line_strategy)
def test_hlcorestructure_line_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=hlcorestructure_Line_strategy)
def test_hlcorestructure_line_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=hlcorestructure_Line_strategy)
def test_hlcorestructure_line_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=hlcorestructure_Line_strategy)
def test_hlcorestructure_line_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=hlcorestructure_Fill_strategy)
@settings(max_examples=50)
def test_hlcorestructure_fill_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Fill)



@given(instance=hlcorestructure_Fill_strategy)
def test_hlcorestructure_fill_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=hlcorestructure_Fill_strategy)
def test_hlcorestructure_fill_gradientrotation_setter(instance):
    original = instance.gradientrotation
    instance.gradientrotation = original
    assert instance.gradientrotation == original



@given(instance=hlcorestructure_Fill_strategy)
def test_hlcorestructure_fill_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=hlcorestructure_Fill_strategy)
def test_hlcorestructure_fill_gradientcolor_setter(instance):
    original = instance.gradientcolor
    instance.gradientcolor = original
    assert instance.gradientcolor == original

@given(instance=hlcorestructure_Dimension_strategy)
@settings(max_examples=50)
def test_hlcorestructure_dimension_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Dimension)

@given(instance=hlcorestructure_Position_strategy)
@settings(max_examples=50)
def test_hlcorestructure_position_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Position)

@given(instance=Graphics_strategy)
@settings(max_examples=50)
def test_graphics_instantiation(instance):
    assert isinstance(instance, Graphics)

@given(instance=hlcorestructure_AnnotationGraphics_strategy)
@settings(max_examples=50)
def test_hlcorestructure_annotationgraphics_instantiation(instance):
    assert isinstance(instance, hlcorestructure_AnnotationGraphics)

@given(instance=hlcorestructure_ArcGraphics_strategy)
@settings(max_examples=50)
def test_hlcorestructure_arcgraphics_instantiation(instance):
    assert isinstance(instance, hlcorestructure_ArcGraphics)

@given(instance=hlcorestructure_PnObject_strategy)
@settings(max_examples=50)
def test_hlcorestructure_pnobject_instantiation(instance):
    assert isinstance(instance, hlcorestructure_PnObject)



@given(instance=hlcorestructure_PnObject_strategy)
def test_hlcorestructure_pnobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=PnObject_strategy)
@settings(max_examples=50)
def test_pnobject_instantiation(instance):
    assert isinstance(instance, PnObject)

@given(instance=hlcorestructure_Node_strategy)
@settings(max_examples=50)
def test_hlcorestructure_node_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Node)

@given(instance=hlcorestructure_Arc_strategy)
@settings(max_examples=50)
def test_hlcorestructure_arc_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Arc)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=hlcorestructure_HLCoreAnnotation_strategy)
@settings(max_examples=50)
def test_hlcorestructure_hlcoreannotation_instantiation(instance):
    assert isinstance(instance, hlcorestructure_HLCoreAnnotation)



@given(instance=hlcorestructure_HLCoreAnnotation_strategy)
def test_hlcorestructure_hlcoreannotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=hlcorestructure_NodeGraphics_strategy)
@settings(max_examples=50)
def test_hlcorestructure_nodegraphics_instantiation(instance):
    assert isinstance(instance, hlcorestructure_NodeGraphics)

@given(instance=hlcorestructure_Declaration_strategy)
@settings(max_examples=50)
def test_hlcorestructure_declaration_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Declaration)

@given(instance=hlcorestructure_ToolInfo_strategy)
@settings(max_examples=50)
def test_hlcorestructure_toolinfo_instantiation(instance):
    assert isinstance(instance, hlcorestructure_ToolInfo)



@given(instance=hlcorestructure_ToolInfo_strategy)
def test_hlcorestructure_toolinfo_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=hlcorestructure_ToolInfo_strategy)
def test_hlcorestructure_toolinfo_toolInfoGrammarURI_setter(instance):
    original = instance.toolInfoGrammarURI
    instance.toolInfoGrammarURI = original
    assert instance.toolInfoGrammarURI == original



@given(instance=hlcorestructure_ToolInfo_strategy)
def test_hlcorestructure_toolinfo_formattedXMLBuffer_setter(instance):
    original = instance.formattedXMLBuffer
    instance.formattedXMLBuffer = original
    assert instance.formattedXMLBuffer == original



@given(instance=hlcorestructure_ToolInfo_strategy)
def test_hlcorestructure_toolinfo_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=hlcorestructure_Name_strategy)
@settings(max_examples=50)
def test_hlcorestructure_name_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Name)



@given(instance=hlcorestructure_Name_strategy)
def test_hlcorestructure_name_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=hlcorestructure_Page_strategy)
@settings(max_examples=50)
def test_hlcorestructure_page_instantiation(instance):
    assert isinstance(instance, hlcorestructure_Page)

@given(instance=hlcorestructure_PetriNet_strategy)
@settings(max_examples=50)
def test_hlcorestructure_petrinet_instantiation(instance):
    assert isinstance(instance, hlcorestructure_PetriNet)



@given(instance=hlcorestructure_PetriNet_strategy)
def test_hlcorestructure_petrinet_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=hlcorestructure_PetriNet_strategy)
def test_hlcorestructure_petrinet_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=hlcorestructure_PetriNetDoc_strategy)
@settings(max_examples=50)
def test_hlcorestructure_petrinetdoc_instantiation(instance):
    assert isinstance(instance, hlcorestructure_PetriNetDoc)



@given(instance=hlcorestructure_PetriNetDoc_strategy)
def test_hlcorestructure_petrinetdoc_xmlns_setter(instance):
    original = instance.xmlns
    instance.xmlns = original
    assert instance.xmlns == original
