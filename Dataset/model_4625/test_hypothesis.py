import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Cursor,
    model_SystemCursor,
    Container,
    model_GridContainer,
    model_StackContainer,
    model_BorderContainer,
    model_XYContainer,
    model_Child,
    Shape,
    model_RoundedRectangle,
    model_Line,
    model_Polygon,
    model_Arc,
    model_Ellipse,
    model_Rectangle,
    Figure,
    model_FigureContainer,
    model_Image,
    model_Text,
    model_Shape,
    Primitive,
    model_SymbolReference,
    model_Figure,
    model_Container,
    model_TimeTrigger,
    model_Connection,
    model_Position,
    Child,
    model_GridChild,
    model_BorderChild,
    model_XYChild,
    model_StringToStringMap,
    model_Primitive,
    model_Symbol,
    model_Dimension,
    model_Cursor,
    Alignment,
    Orientation,
    GridAlignment,
    SystemCursorType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cursor_is_not_abstract():
    assert not inspect.isabstract(Cursor)


def test_cursor_constructor_exists():
    assert callable(Cursor.__init__)


def test_cursor_constructor_args():
    sig = inspect.signature(Cursor.__init__)
    params = list(sig.parameters.keys())



def test_model_systemcursor_is_not_abstract():
    assert not inspect.isabstract(model_SystemCursor)


def test_model_systemcursor_constructor_exists():
    assert callable(model_SystemCursor.__init__)


def test_model_systemcursor_constructor_args():
    sig = inspect.signature(model_SystemCursor.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model_systemcursor_has_type():
    assert hasattr(model_SystemCursor, "type")
    descriptor = None
    for klass in model_SystemCursor.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_container_is_not_abstract():
    assert not inspect.isabstract(Container)


def test_container_constructor_exists():
    assert callable(Container.__init__)


def test_container_constructor_args():
    sig = inspect.signature(Container.__init__)
    params = list(sig.parameters.keys())



def test_model_gridcontainer_is_not_abstract():
    assert not inspect.isabstract(model_GridContainer)


def test_model_gridcontainer_constructor_exists():
    assert callable(model_GridContainer.__init__)


def test_model_gridcontainer_constructor_args():
    sig = inspect.signature(model_GridContainer.__init__)
    params = list(sig.parameters.keys())
    assert "marginWidth" in params, "Missing parameter 'marginWidth'"
    assert "verticalSpacing" in params, "Missing parameter 'verticalSpacing'"
    assert "columns" in params, "Missing parameter 'columns'"
    assert "horizontalSpacing" in params, "Missing parameter 'horizontalSpacing'"
    assert "marginHeight" in params, "Missing parameter 'marginHeight'"
    assert "equalWidth" in params, "Missing parameter 'equalWidth'"

def test_model_gridcontainer_has_marginWidth():
    assert hasattr(model_GridContainer, "marginWidth")
    descriptor = None
    for klass in model_GridContainer.__mro__:
        if "marginWidth" in klass.__dict__:
            descriptor = klass.__dict__["marginWidth"]
            break
    assert isinstance(descriptor, property)

def test_model_gridcontainer_has_verticalSpacing():
    assert hasattr(model_GridContainer, "verticalSpacing")
    descriptor = None
    for klass in model_GridContainer.__mro__:
        if "verticalSpacing" in klass.__dict__:
            descriptor = klass.__dict__["verticalSpacing"]
            break
    assert isinstance(descriptor, property)

def test_model_gridcontainer_has_columns():
    assert hasattr(model_GridContainer, "columns")
    descriptor = None
    for klass in model_GridContainer.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)

def test_model_gridcontainer_has_horizontalSpacing():
    assert hasattr(model_GridContainer, "horizontalSpacing")
    descriptor = None
    for klass in model_GridContainer.__mro__:
        if "horizontalSpacing" in klass.__dict__:
            descriptor = klass.__dict__["horizontalSpacing"]
            break
    assert isinstance(descriptor, property)

def test_model_gridcontainer_has_marginHeight():
    assert hasattr(model_GridContainer, "marginHeight")
    descriptor = None
    for klass in model_GridContainer.__mro__:
        if "marginHeight" in klass.__dict__:
            descriptor = klass.__dict__["marginHeight"]
            break
    assert isinstance(descriptor, property)

def test_model_gridcontainer_has_equalWidth():
    assert hasattr(model_GridContainer, "equalWidth")
    descriptor = None
    for klass in model_GridContainer.__mro__:
        if "equalWidth" in klass.__dict__:
            descriptor = klass.__dict__["equalWidth"]
            break
    assert isinstance(descriptor, property)



def test_model_stackcontainer_is_not_abstract():
    assert not inspect.isabstract(model_StackContainer)


def test_model_stackcontainer_constructor_exists():
    assert callable(model_StackContainer.__init__)


def test_model_stackcontainer_constructor_args():
    sig = inspect.signature(model_StackContainer.__init__)
    params = list(sig.parameters.keys())



def test_model_bordercontainer_is_not_abstract():
    assert not inspect.isabstract(model_BorderContainer)


def test_model_bordercontainer_constructor_exists():
    assert callable(model_BorderContainer.__init__)


def test_model_bordercontainer_constructor_args():
    sig = inspect.signature(model_BorderContainer.__init__)
    params = list(sig.parameters.keys())
    assert "horizontalSpacing" in params, "Missing parameter 'horizontalSpacing'"
    assert "verticalSpacing" in params, "Missing parameter 'verticalSpacing'"

def test_model_bordercontainer_has_horizontalSpacing():
    assert hasattr(model_BorderContainer, "horizontalSpacing")
    descriptor = None
    for klass in model_BorderContainer.__mro__:
        if "horizontalSpacing" in klass.__dict__:
            descriptor = klass.__dict__["horizontalSpacing"]
            break
    assert isinstance(descriptor, property)

def test_model_bordercontainer_has_verticalSpacing():
    assert hasattr(model_BorderContainer, "verticalSpacing")
    descriptor = None
    for klass in model_BorderContainer.__mro__:
        if "verticalSpacing" in klass.__dict__:
            descriptor = klass.__dict__["verticalSpacing"]
            break
    assert isinstance(descriptor, property)



def test_model_xycontainer_is_not_abstract():
    assert not inspect.isabstract(model_XYContainer)


def test_model_xycontainer_constructor_exists():
    assert callable(model_XYContainer.__init__)


def test_model_xycontainer_constructor_args():
    sig = inspect.signature(model_XYContainer.__init__)
    params = list(sig.parameters.keys())



def test_model_child_is_not_abstract():
    assert not inspect.isabstract(model_Child)


def test_model_child_constructor_exists():
    assert callable(model_Child.__init__)


def test_model_child_constructor_args():
    sig = inspect.signature(model_Child.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_child_has_name():
    assert hasattr(model_Child, "name")
    descriptor = None
    for klass in model_Child.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_model_roundedrectangle_is_not_abstract():
    assert not inspect.isabstract(model_RoundedRectangle)


def test_model_roundedrectangle_constructor_exists():
    assert callable(model_RoundedRectangle.__init__)


def test_model_roundedrectangle_constructor_args():
    sig = inspect.signature(model_RoundedRectangle.__init__)
    params = list(sig.parameters.keys())



def test_model_line_is_not_abstract():
    assert not inspect.isabstract(model_Line)


def test_model_line_constructor_exists():
    assert callable(model_Line.__init__)


def test_model_line_constructor_args():
    sig = inspect.signature(model_Line.__init__)
    params = list(sig.parameters.keys())



def test_model_polygon_is_not_abstract():
    assert not inspect.isabstract(model_Polygon)


def test_model_polygon_constructor_exists():
    assert callable(model_Polygon.__init__)


def test_model_polygon_constructor_args():
    sig = inspect.signature(model_Polygon.__init__)
    params = list(sig.parameters.keys())



def test_model_arc_is_not_abstract():
    assert not inspect.isabstract(model_Arc)


def test_model_arc_constructor_exists():
    assert callable(model_Arc.__init__)


def test_model_arc_constructor_args():
    sig = inspect.signature(model_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "length" in params, "Missing parameter 'length'"

def test_model_arc_has_start():
    assert hasattr(model_Arc, "start")
    descriptor = None
    for klass in model_Arc.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_model_arc_has_length():
    assert hasattr(model_Arc, "length")
    descriptor = None
    for klass in model_Arc.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_model_ellipse_is_not_abstract():
    assert not inspect.isabstract(model_Ellipse)


def test_model_ellipse_constructor_exists():
    assert callable(model_Ellipse.__init__)


def test_model_ellipse_constructor_args():
    sig = inspect.signature(model_Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_model_rectangle_is_not_abstract():
    assert not inspect.isabstract(model_Rectangle)


def test_model_rectangle_constructor_exists():
    assert callable(model_Rectangle.__init__)


def test_model_rectangle_constructor_args():
    sig = inspect.signature(model_Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_model_figurecontainer_is_not_abstract():
    assert not inspect.isabstract(model_FigureContainer)


def test_model_figurecontainer_constructor_exists():
    assert callable(model_FigureContainer.__init__)


def test_model_figurecontainer_constructor_args():
    sig = inspect.signature(model_FigureContainer.__init__)
    params = list(sig.parameters.keys())



def test_model_image_is_not_abstract():
    assert not inspect.isabstract(model_Image)


def test_model_image_constructor_exists():
    assert callable(model_Image.__init__)


def test_model_image_constructor_args():
    sig = inspect.signature(model_Image.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"
    assert "imageAlignment" in params, "Missing parameter 'imageAlignment'"

def test_model_image_has_uri():
    assert hasattr(model_Image, "uri")
    descriptor = None
    for klass in model_Image.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)

def test_model_image_has_imageAlignment():
    assert hasattr(model_Image, "imageAlignment")
    descriptor = None
    for klass in model_Image.__mro__:
        if "imageAlignment" in klass.__dict__:
            descriptor = klass.__dict__["imageAlignment"]
            break
    assert isinstance(descriptor, property)



def test_model_text_is_not_abstract():
    assert not inspect.isabstract(model_Text)


def test_model_text_constructor_exists():
    assert callable(model_Text.__init__)


def test_model_text_constructor_args():
    sig = inspect.signature(model_Text.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "fontBold" in params, "Missing parameter 'fontBold'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "labelAlignment" in params, "Missing parameter 'labelAlignment'"
    assert "textAlignment" in params, "Missing parameter 'textAlignment'"
    assert "fontItalic" in params, "Missing parameter 'fontItalic'"
    assert "iconAlignment" in params, "Missing parameter 'iconAlignment'"
    assert "fontSize" in params, "Missing parameter 'fontSize'"
    assert "textPlacement" in params, "Missing parameter 'textPlacement'"
    assert "fontName" in params, "Missing parameter 'fontName'"

def test_model_text_has_text():
    assert hasattr(model_Text, "text")
    descriptor = None
    for klass in model_Text.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_model_text_has_fontBold():
    assert hasattr(model_Text, "fontBold")
    descriptor = None
    for klass in model_Text.__mro__:
        if "fontBold" in klass.__dict__:
            descriptor = klass.__dict__["fontBold"]
            break
    assert isinstance(descriptor, property)

def test_model_text_has_alpha():
    assert hasattr(model_Text, "alpha")
    descriptor = None
    for klass in model_Text.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_model_text_has_labelAlignment():
    assert hasattr(model_Text, "labelAlignment")
    descriptor = None
    for klass in model_Text.__mro__:
        if "labelAlignment" in klass.__dict__:
            descriptor = klass.__dict__["labelAlignment"]
            break
    assert isinstance(descriptor, property)

def test_model_text_has_textAlignment():
    assert hasattr(model_Text, "textAlignment")
    descriptor = None
    for klass in model_Text.__mro__:
        if "textAlignment" in klass.__dict__:
            descriptor = klass.__dict__["textAlignment"]
            break
    assert isinstance(descriptor, property)

def test_model_text_has_fontItalic():
    assert hasattr(model_Text, "fontItalic")
    descriptor = None
    for klass in model_Text.__mro__:
        if "fontItalic" in klass.__dict__:
            descriptor = klass.__dict__["fontItalic"]
            break
    assert isinstance(descriptor, property)

def test_model_text_has_iconAlignment():
    assert hasattr(model_Text, "iconAlignment")
    descriptor = None
    for klass in model_Text.__mro__:
        if "iconAlignment" in klass.__dict__:
            descriptor = klass.__dict__["iconAlignment"]
            break
    assert isinstance(descriptor, property)

def test_model_text_has_fontSize():
    assert hasattr(model_Text, "fontSize")
    descriptor = None
    for klass in model_Text.__mro__:
        if "fontSize" in klass.__dict__:
            descriptor = klass.__dict__["fontSize"]
            break
    assert isinstance(descriptor, property)

def test_model_text_has_textPlacement():
    assert hasattr(model_Text, "textPlacement")
    descriptor = None
    for klass in model_Text.__mro__:
        if "textPlacement" in klass.__dict__:
            descriptor = klass.__dict__["textPlacement"]
            break
    assert isinstance(descriptor, property)

def test_model_text_has_fontName():
    assert hasattr(model_Text, "fontName")
    descriptor = None
    for klass in model_Text.__mro__:
        if "fontName" in klass.__dict__:
            descriptor = klass.__dict__["fontName"]
            break
    assert isinstance(descriptor, property)



def test_model_shape_is_not_abstract():
    assert not inspect.isabstract(model_Shape)


def test_model_shape_constructor_exists():
    assert callable(model_Shape.__init__)


def test_model_shape_constructor_args():
    sig = inspect.signature(model_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "outline" in params, "Missing parameter 'outline'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "fill" in params, "Missing parameter 'fill'"
    assert "antialias" in params, "Missing parameter 'antialias'"

def test_model_shape_has_lineWidth():
    assert hasattr(model_Shape, "lineWidth")
    descriptor = None
    for klass in model_Shape.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_model_shape_has_outline():
    assert hasattr(model_Shape, "outline")
    descriptor = None
    for klass in model_Shape.__mro__:
        if "outline" in klass.__dict__:
            descriptor = klass.__dict__["outline"]
            break
    assert isinstance(descriptor, property)

def test_model_shape_has_alpha():
    assert hasattr(model_Shape, "alpha")
    descriptor = None
    for klass in model_Shape.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_model_shape_has_fill():
    assert hasattr(model_Shape, "fill")
    descriptor = None
    for klass in model_Shape.__mro__:
        if "fill" in klass.__dict__:
            descriptor = klass.__dict__["fill"]
            break
    assert isinstance(descriptor, property)

def test_model_shape_has_antialias():
    assert hasattr(model_Shape, "antialias")
    descriptor = None
    for klass in model_Shape.__mro__:
        if "antialias" in klass.__dict__:
            descriptor = klass.__dict__["antialias"]
            break
    assert isinstance(descriptor, property)



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_model_symbolreference_is_not_abstract():
    assert not inspect.isabstract(model_SymbolReference)


def test_model_symbolreference_constructor_exists():
    assert callable(model_SymbolReference.__init__)


def test_model_symbolreference_constructor_args():
    sig = inspect.signature(model_SymbolReference.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"
    assert "zoom" in params, "Missing parameter 'zoom'"
    assert "onCreateProperties" in params, "Missing parameter 'onCreateProperties'"

def test_model_symbolreference_has_uri():
    assert hasattr(model_SymbolReference, "uri")
    descriptor = None
    for klass in model_SymbolReference.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)

def test_model_symbolreference_has_zoom():
    assert hasattr(model_SymbolReference, "zoom")
    descriptor = None
    for klass in model_SymbolReference.__mro__:
        if "zoom" in klass.__dict__:
            descriptor = klass.__dict__["zoom"]
            break
    assert isinstance(descriptor, property)

def test_model_symbolreference_has_onCreateProperties():
    assert hasattr(model_SymbolReference, "onCreateProperties")
    descriptor = None
    for klass in model_SymbolReference.__mro__:
        if "onCreateProperties" in klass.__dict__:
            descriptor = klass.__dict__["onCreateProperties"]
            break
    assert isinstance(descriptor, property)



def test_model_figure_is_not_abstract():
    assert not inspect.isabstract(model_Figure)


def test_model_figure_constructor_exists():
    assert callable(model_Figure.__init__)


def test_model_figure_constructor_args():
    sig = inspect.signature(model_Figure.__init__)
    params = list(sig.parameters.keys())
    assert "onDoubleClick" in params, "Missing parameter 'onDoubleClick'"
    assert "onMouseMove" in params, "Missing parameter 'onMouseMove'"
    assert "toolTip" in params, "Missing parameter 'toolTip'"
    assert "opaque" in params, "Missing parameter 'opaque'"
    assert "onClick" in params, "Missing parameter 'onClick'"
    assert "border" in params, "Missing parameter 'border'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "onMouseOut" in params, "Missing parameter 'onMouseOut'"
    assert "onMouseDrag" in params, "Missing parameter 'onMouseDrag'"
    assert "onMouseIn" in params, "Missing parameter 'onMouseIn'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "onMouseHover" in params, "Missing parameter 'onMouseHover'"
    assert "foregroundColor" in params, "Missing parameter 'foregroundColor'"

def test_model_figure_has_onDoubleClick():
    assert hasattr(model_Figure, "onDoubleClick")
    descriptor = None
    for klass in model_Figure.__mro__:
        if "onDoubleClick" in klass.__dict__:
            descriptor = klass.__dict__["onDoubleClick"]
            break
    assert isinstance(descriptor, property)

def test_model_figure_has_onMouseMove():
    assert hasattr(model_Figure, "onMouseMove")
    descriptor = None
    for klass in model_Figure.__mro__:
        if "onMouseMove" in klass.__dict__:
            descriptor = klass.__dict__["onMouseMove"]
            break
    assert isinstance(descriptor, property)

def test_model_figure_has_toolTip():
    assert hasattr(model_Figure, "toolTip")
    descriptor = None
    for klass in model_Figure.__mro__:
        if "toolTip" in klass.__dict__:
            descriptor = klass.__dict__["toolTip"]
            break
    assert isinstance(descriptor, property)

def test_model_figure_has_opaque():
    assert hasattr(model_Figure, "opaque")
    descriptor = None
    for klass in model_Figure.__mro__:
        if "opaque" in klass.__dict__:
            descriptor = klass.__dict__["opaque"]
            break
    assert isinstance(descriptor, property)

def test_model_figure_has_onClick():
    assert hasattr(model_Figure, "onClick")
    descriptor = None
    for klass in model_Figure.__mro__:
        if "onClick" in klass.__dict__:
            descriptor = klass.__dict__["onClick"]
            break
    assert isinstance(descriptor, property)

def test_model_figure_has_border():
    assert hasattr(model_Figure, "border")
    descriptor = None
    for klass in model_Figure.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)

def test_model_figure_has_visible():
    assert hasattr(model_Figure, "visible")
    descriptor = None
    for klass in model_Figure.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_model_figure_has_onMouseOut():
    assert hasattr(model_Figure, "onMouseOut")
    descriptor = None
    for klass in model_Figure.__mro__:
        if "onMouseOut" in klass.__dict__:
            descriptor = klass.__dict__["onMouseOut"]
            break
    assert isinstance(descriptor, property)

def test_model_figure_has_onMouseDrag():
    assert hasattr(model_Figure, "onMouseDrag")
    descriptor = None
    for klass in model_Figure.__mro__:
        if "onMouseDrag" in klass.__dict__:
            descriptor = klass.__dict__["onMouseDrag"]
            break
    assert isinstance(descriptor, property)

def test_model_figure_has_onMouseIn():
    assert hasattr(model_Figure, "onMouseIn")
    descriptor = None
    for klass in model_Figure.__mro__:
        if "onMouseIn" in klass.__dict__:
            descriptor = klass.__dict__["onMouseIn"]
            break
    assert isinstance(descriptor, property)

def test_model_figure_has_backgroundColor():
    assert hasattr(model_Figure, "backgroundColor")
    descriptor = None
    for klass in model_Figure.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_model_figure_has_onMouseHover():
    assert hasattr(model_Figure, "onMouseHover")
    descriptor = None
    for klass in model_Figure.__mro__:
        if "onMouseHover" in klass.__dict__:
            descriptor = klass.__dict__["onMouseHover"]
            break
    assert isinstance(descriptor, property)

def test_model_figure_has_foregroundColor():
    assert hasattr(model_Figure, "foregroundColor")
    descriptor = None
    for klass in model_Figure.__mro__:
        if "foregroundColor" in klass.__dict__:
            descriptor = klass.__dict__["foregroundColor"]
            break
    assert isinstance(descriptor, property)



def test_model_container_is_not_abstract():
    assert not inspect.isabstract(model_Container)


def test_model_container_constructor_exists():
    assert callable(model_Container.__init__)


def test_model_container_constructor_args():
    sig = inspect.signature(model_Container.__init__)
    params = list(sig.parameters.keys())



def test_model_timetrigger_is_not_abstract():
    assert not inspect.isabstract(model_TimeTrigger)


def test_model_timetrigger_constructor_exists():
    assert callable(model_TimeTrigger.__init__)


def test_model_timetrigger_constructor_args():
    sig = inspect.signature(model_TimeTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "onTrigger" in params, "Missing parameter 'onTrigger'"
    assert "period" in params, "Missing parameter 'period'"

def test_model_timetrigger_has_onTrigger():
    assert hasattr(model_TimeTrigger, "onTrigger")
    descriptor = None
    for klass in model_TimeTrigger.__mro__:
        if "onTrigger" in klass.__dict__:
            descriptor = klass.__dict__["onTrigger"]
            break
    assert isinstance(descriptor, property)

def test_model_timetrigger_has_period():
    assert hasattr(model_TimeTrigger, "period")
    descriptor = None
    for klass in model_TimeTrigger.__mro__:
        if "period" in klass.__dict__:
            descriptor = klass.__dict__["period"]
            break
    assert isinstance(descriptor, property)



def test_model_connection_is_not_abstract():
    assert not inspect.isabstract(model_Connection)


def test_model_connection_constructor_exists():
    assert callable(model_Connection.__init__)


def test_model_connection_constructor_args():
    sig = inspect.signature(model_Connection.__init__)
    params = list(sig.parameters.keys())



def test_model_position_is_not_abstract():
    assert not inspect.isabstract(model_Position)


def test_model_position_constructor_exists():
    assert callable(model_Position.__init__)


def test_model_position_constructor_args():
    sig = inspect.signature(model_Position.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_model_position_has_x():
    assert hasattr(model_Position, "x")
    descriptor = None
    for klass in model_Position.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_model_position_has_y():
    assert hasattr(model_Position, "y")
    descriptor = None
    for klass in model_Position.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_child_is_not_abstract():
    assert not inspect.isabstract(Child)


def test_child_constructor_exists():
    assert callable(Child.__init__)


def test_child_constructor_args():
    sig = inspect.signature(Child.__init__)
    params = list(sig.parameters.keys())



def test_model_gridchild_is_not_abstract():
    assert not inspect.isabstract(model_GridChild)


def test_model_gridchild_constructor_exists():
    assert callable(model_GridChild.__init__)


def test_model_gridchild_constructor_args():
    sig = inspect.signature(model_GridChild.__init__)
    params = list(sig.parameters.keys())
    assert "grabHorizontalSpace" in params, "Missing parameter 'grabHorizontalSpace'"
    assert "grabVerticalSpace" in params, "Missing parameter 'grabVerticalSpace'"
    assert "widthHint" in params, "Missing parameter 'widthHint'"
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"
    assert "heightHint" in params, "Missing parameter 'heightHint'"
    assert "spanCols" in params, "Missing parameter 'spanCols'"
    assert "spanRows" in params, "Missing parameter 'spanRows'"

def test_model_gridchild_has_grabHorizontalSpace():
    assert hasattr(model_GridChild, "grabHorizontalSpace")
    descriptor = None
    for klass in model_GridChild.__mro__:
        if "grabHorizontalSpace" in klass.__dict__:
            descriptor = klass.__dict__["grabHorizontalSpace"]
            break
    assert isinstance(descriptor, property)

def test_model_gridchild_has_grabVerticalSpace():
    assert hasattr(model_GridChild, "grabVerticalSpace")
    descriptor = None
    for klass in model_GridChild.__mro__:
        if "grabVerticalSpace" in klass.__dict__:
            descriptor = klass.__dict__["grabVerticalSpace"]
            break
    assert isinstance(descriptor, property)

def test_model_gridchild_has_widthHint():
    assert hasattr(model_GridChild, "widthHint")
    descriptor = None
    for klass in model_GridChild.__mro__:
        if "widthHint" in klass.__dict__:
            descriptor = klass.__dict__["widthHint"]
            break
    assert isinstance(descriptor, property)

def test_model_gridchild_has_verticalAlignment():
    assert hasattr(model_GridChild, "verticalAlignment")
    descriptor = None
    for klass in model_GridChild.__mro__:
        if "verticalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_model_gridchild_has_horizontalAlignment():
    assert hasattr(model_GridChild, "horizontalAlignment")
    descriptor = None
    for klass in model_GridChild.__mro__:
        if "horizontalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["horizontalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_model_gridchild_has_heightHint():
    assert hasattr(model_GridChild, "heightHint")
    descriptor = None
    for klass in model_GridChild.__mro__:
        if "heightHint" in klass.__dict__:
            descriptor = klass.__dict__["heightHint"]
            break
    assert isinstance(descriptor, property)

def test_model_gridchild_has_spanCols():
    assert hasattr(model_GridChild, "spanCols")
    descriptor = None
    for klass in model_GridChild.__mro__:
        if "spanCols" in klass.__dict__:
            descriptor = klass.__dict__["spanCols"]
            break
    assert isinstance(descriptor, property)

def test_model_gridchild_has_spanRows():
    assert hasattr(model_GridChild, "spanRows")
    descriptor = None
    for klass in model_GridChild.__mro__:
        if "spanRows" in klass.__dict__:
            descriptor = klass.__dict__["spanRows"]
            break
    assert isinstance(descriptor, property)



def test_model_borderchild_is_not_abstract():
    assert not inspect.isabstract(model_BorderChild)


def test_model_borderchild_constructor_exists():
    assert callable(model_BorderChild.__init__)


def test_model_borderchild_constructor_args():
    sig = inspect.signature(model_BorderChild.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_model_borderchild_has_alignment():
    assert hasattr(model_BorderChild, "alignment")
    descriptor = None
    for klass in model_BorderChild.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_model_xychild_is_not_abstract():
    assert not inspect.isabstract(model_XYChild)


def test_model_xychild_constructor_exists():
    assert callable(model_XYChild.__init__)


def test_model_xychild_constructor_args():
    sig = inspect.signature(model_XYChild.__init__)
    params = list(sig.parameters.keys())



def test_model_stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(model_StringToStringMap)


def test_model_stringtostringmap_constructor_exists():
    assert callable(model_StringToStringMap.__init__)


def test_model_stringtostringmap_constructor_args():
    sig = inspect.signature(model_StringToStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_model_stringtostringmap_has_value():
    assert hasattr(model_StringToStringMap, "value")
    descriptor = None
    for klass in model_StringToStringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_model_stringtostringmap_has_key():
    assert hasattr(model_StringToStringMap, "key")
    descriptor = None
    for klass in model_StringToStringMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_model_primitive_is_not_abstract():
    assert not inspect.isabstract(model_Primitive)


def test_model_primitive_constructor_exists():
    assert callable(model_Primitive.__init__)


def test_model_primitive_constructor_args():
    sig = inspect.signature(model_Primitive.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_primitive_has_name():
    assert hasattr(model_Primitive, "name")
    descriptor = None
    for klass in model_Primitive.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_symbol_is_not_abstract():
    assert not inspect.isabstract(model_Symbol)


def test_model_symbol_constructor_exists():
    assert callable(model_Symbol.__init__)


def test_model_symbol_constructor_args():
    sig = inspect.signature(model_Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "onUpdate" in params, "Missing parameter 'onUpdate'"
    assert "scriptModules" in params, "Missing parameter 'scriptModules'"
    assert "backgroundImage" in params, "Missing parameter 'backgroundImage'"
    assert "onDispose" in params, "Missing parameter 'onDispose'"
    assert "onInit" in params, "Missing parameter 'onInit'"

def test_model_symbol_has_backgroundColor():
    assert hasattr(model_Symbol, "backgroundColor")
    descriptor = None
    for klass in model_Symbol.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_model_symbol_has_onUpdate():
    assert hasattr(model_Symbol, "onUpdate")
    descriptor = None
    for klass in model_Symbol.__mro__:
        if "onUpdate" in klass.__dict__:
            descriptor = klass.__dict__["onUpdate"]
            break
    assert isinstance(descriptor, property)

def test_model_symbol_has_scriptModules():
    assert hasattr(model_Symbol, "scriptModules")
    descriptor = None
    for klass in model_Symbol.__mro__:
        if "scriptModules" in klass.__dict__:
            descriptor = klass.__dict__["scriptModules"]
            break
    assert isinstance(descriptor, property)

def test_model_symbol_has_backgroundImage():
    assert hasattr(model_Symbol, "backgroundImage")
    descriptor = None
    for klass in model_Symbol.__mro__:
        if "backgroundImage" in klass.__dict__:
            descriptor = klass.__dict__["backgroundImage"]
            break
    assert isinstance(descriptor, property)

def test_model_symbol_has_onDispose():
    assert hasattr(model_Symbol, "onDispose")
    descriptor = None
    for klass in model_Symbol.__mro__:
        if "onDispose" in klass.__dict__:
            descriptor = klass.__dict__["onDispose"]
            break
    assert isinstance(descriptor, property)

def test_model_symbol_has_onInit():
    assert hasattr(model_Symbol, "onInit")
    descriptor = None
    for klass in model_Symbol.__mro__:
        if "onInit" in klass.__dict__:
            descriptor = klass.__dict__["onInit"]
            break
    assert isinstance(descriptor, property)



def test_model_dimension_is_not_abstract():
    assert not inspect.isabstract(model_Dimension)


def test_model_dimension_constructor_exists():
    assert callable(model_Dimension.__init__)


def test_model_dimension_constructor_args():
    sig = inspect.signature(model_Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_model_dimension_has_height():
    assert hasattr(model_Dimension, "height")
    descriptor = None
    for klass in model_Dimension.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_model_dimension_has_width():
    assert hasattr(model_Dimension, "width")
    descriptor = None
    for klass in model_Dimension.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_model_cursor_is_not_abstract():
    assert not inspect.isabstract(model_Cursor)


def test_model_cursor_constructor_exists():
    assert callable(model_Cursor.__init__)


def test_model_cursor_constructor_args():
    sig = inspect.signature(model_Cursor.__init__)
    params = list(sig.parameters.keys())

def test_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "LEFT",
        "CENTER",
        "TOP",
        "BOTTOM",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Alignment"

def test_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "SOUTH",
        "WEST",
        "EAST",
        "NORTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"

def test_gridalignment_exists():
    # Check that the Enumeration exists
    assert GridAlignment is not None

def test_gridalignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GridAlignment]
    expected_literals = [
        "END",
        "CENTER",
        "FILL",
        "BEGINNING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GridAlignment"

def test_systemcursortype_exists():
    # Check that the Enumeration exists
    assert SystemCursorType is not None

def test_systemcursortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SystemCursorType]
    expected_literals = [
        "ARROW",
        "HAND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SystemCursorType"


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
Cursor_strategy = st.builds(
    Cursor,
)
model_SystemCursor_strategy = st.builds(
    model_SystemCursor,
    type=
        safe_text
)
Container_strategy = st.builds(
    Container,
)
model_GridContainer_strategy = st.builds(
    model_GridContainer,
    marginWidth=
        st.integers(),
    verticalSpacing=
        st.integers(),
    columns=
        st.integers(),
    horizontalSpacing=
        st.integers(),
    marginHeight=
        st.integers(),
    equalWidth=
        st.booleans()
)
model_StackContainer_strategy = st.builds(
    model_StackContainer,
)
model_BorderContainer_strategy = st.builds(
    model_BorderContainer,
    horizontalSpacing=
        st.integers(),
    verticalSpacing=
        st.integers()
)
model_XYContainer_strategy = st.builds(
    model_XYContainer,
)
model_Child_strategy = st.builds(
    model_Child,
    name=
        safe_text
)
Shape_strategy = st.builds(
    Shape,
)
model_RoundedRectangle_strategy = st.builds(
    model_RoundedRectangle,
)
model_Line_strategy = st.builds(
    model_Line,
)
model_Polygon_strategy = st.builds(
    model_Polygon,
)
model_Arc_strategy = st.builds(
    model_Arc,
    start=
        st.integers(),
    length=
        st.integers()
)
model_Ellipse_strategy = st.builds(
    model_Ellipse,
)
model_Rectangle_strategy = st.builds(
    model_Rectangle,
)
Figure_strategy = st.builds(
    Figure,
)
model_FigureContainer_strategy = st.builds(
    model_FigureContainer,
)
model_Image_strategy = st.builds(
    model_Image,
    uri=
        safe_text,
    imageAlignment=
        safe_text
)
model_Text_strategy = st.builds(
    model_Text,
    text=
        safe_text,
    fontBold=
        st.booleans(),
    alpha=
        safe_text,
    labelAlignment=
        safe_text,
    textAlignment=
        safe_text,
    fontItalic=
        st.booleans(),
    iconAlignment=
        safe_text,
    fontSize=
        st.integers(),
    textPlacement=
        safe_text,
    fontName=
        safe_text
)
model_Shape_strategy = st.builds(
    model_Shape,
    lineWidth=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    outline=
        st.booleans(),
    alpha=
        safe_text,
    fill=
        st.booleans(),
    antialias=
        safe_text
)
Primitive_strategy = st.builds(
    Primitive,
)
model_SymbolReference_strategy = st.builds(
    model_SymbolReference,
    uri=
        safe_text,
    zoom=
        safe_text,
    onCreateProperties=
        safe_text
)
model_Figure_strategy = st.builds(
    model_Figure,
    onDoubleClick=
        safe_text,
    onMouseMove=
        safe_text,
    toolTip=
        safe_text,
    opaque=
        safe_text,
    onClick=
        safe_text,
    border=
        safe_text,
    visible=
        st.booleans(),
    onMouseOut=
        safe_text,
    onMouseDrag=
        safe_text,
    onMouseIn=
        safe_text,
    backgroundColor=
        safe_text,
    onMouseHover=
        safe_text,
    foregroundColor=
        safe_text
)
model_Container_strategy = st.builds(
    model_Container,
)
model_TimeTrigger_strategy = st.builds(
    model_TimeTrigger,
    onTrigger=
        safe_text,
    period=
        safe_text
)
model_Connection_strategy = st.builds(
    model_Connection,
)
model_Position_strategy = st.builds(
    model_Position,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Child_strategy = st.builds(
    Child,
)
model_GridChild_strategy = st.builds(
    model_GridChild,
    grabHorizontalSpace=
        st.booleans(),
    grabVerticalSpace=
        st.booleans(),
    widthHint=
        safe_text,
    verticalAlignment=
        safe_text,
    horizontalAlignment=
        safe_text,
    heightHint=
        safe_text,
    spanCols=
        st.integers(),
    spanRows=
        safe_text
)
model_BorderChild_strategy = st.builds(
    model_BorderChild,
    alignment=
        safe_text
)
model_XYChild_strategy = st.builds(
    model_XYChild,
)
model_StringToStringMap_strategy = st.builds(
    model_StringToStringMap,
    value=
        safe_text,
    key=
        safe_text
)
model_Primitive_strategy = st.builds(
    model_Primitive,
    name=
        safe_text
)
model_Symbol_strategy = st.builds(
    model_Symbol,
    backgroundColor=
        safe_text,
    onUpdate=
        safe_text,
    scriptModules=
        safe_text,
    backgroundImage=
        safe_text,
    onDispose=
        safe_text,
    onInit=
        safe_text
)
model_Dimension_strategy = st.builds(
    model_Dimension,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model_Cursor_strategy = st.builds(
    model_Cursor,
)

@given(instance=Cursor_strategy)
@settings(max_examples=50)
def test_cursor_instantiation(instance):
    assert isinstance(instance, Cursor)

@given(instance=model_SystemCursor_strategy)
@settings(max_examples=50)
def test_model_systemcursor_instantiation(instance):
    assert isinstance(instance, model_SystemCursor)



@given(instance=model_SystemCursor_strategy)
def test_model_systemcursor_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Container_strategy)
@settings(max_examples=50)
def test_container_instantiation(instance):
    assert isinstance(instance, Container)

@given(instance=model_GridContainer_strategy)
@settings(max_examples=50)
def test_model_gridcontainer_instantiation(instance):
    assert isinstance(instance, model_GridContainer)



@given(instance=model_GridContainer_strategy)
def test_model_gridcontainer_marginWidth_setter(instance):
    original = instance.marginWidth
    instance.marginWidth = original
    assert instance.marginWidth == original



@given(instance=model_GridContainer_strategy)
def test_model_gridcontainer_verticalSpacing_setter(instance):
    original = instance.verticalSpacing
    instance.verticalSpacing = original
    assert instance.verticalSpacing == original



@given(instance=model_GridContainer_strategy)
def test_model_gridcontainer_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original



@given(instance=model_GridContainer_strategy)
def test_model_gridcontainer_horizontalSpacing_setter(instance):
    original = instance.horizontalSpacing
    instance.horizontalSpacing = original
    assert instance.horizontalSpacing == original



@given(instance=model_GridContainer_strategy)
def test_model_gridcontainer_marginHeight_setter(instance):
    original = instance.marginHeight
    instance.marginHeight = original
    assert instance.marginHeight == original



@given(instance=model_GridContainer_strategy)
def test_model_gridcontainer_equalWidth_setter(instance):
    original = instance.equalWidth
    instance.equalWidth = original
    assert instance.equalWidth == original

@given(instance=model_StackContainer_strategy)
@settings(max_examples=50)
def test_model_stackcontainer_instantiation(instance):
    assert isinstance(instance, model_StackContainer)

@given(instance=model_BorderContainer_strategy)
@settings(max_examples=50)
def test_model_bordercontainer_instantiation(instance):
    assert isinstance(instance, model_BorderContainer)



@given(instance=model_BorderContainer_strategy)
def test_model_bordercontainer_horizontalSpacing_setter(instance):
    original = instance.horizontalSpacing
    instance.horizontalSpacing = original
    assert instance.horizontalSpacing == original



@given(instance=model_BorderContainer_strategy)
def test_model_bordercontainer_verticalSpacing_setter(instance):
    original = instance.verticalSpacing
    instance.verticalSpacing = original
    assert instance.verticalSpacing == original

@given(instance=model_XYContainer_strategy)
@settings(max_examples=50)
def test_model_xycontainer_instantiation(instance):
    assert isinstance(instance, model_XYContainer)

@given(instance=model_Child_strategy)
@settings(max_examples=50)
def test_model_child_instantiation(instance):
    assert isinstance(instance, model_Child)



@given(instance=model_Child_strategy)
def test_model_child_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=model_RoundedRectangle_strategy)
@settings(max_examples=50)
def test_model_roundedrectangle_instantiation(instance):
    assert isinstance(instance, model_RoundedRectangle)

@given(instance=model_Line_strategy)
@settings(max_examples=50)
def test_model_line_instantiation(instance):
    assert isinstance(instance, model_Line)

@given(instance=model_Polygon_strategy)
@settings(max_examples=50)
def test_model_polygon_instantiation(instance):
    assert isinstance(instance, model_Polygon)

@given(instance=model_Arc_strategy)
@settings(max_examples=50)
def test_model_arc_instantiation(instance):
    assert isinstance(instance, model_Arc)



@given(instance=model_Arc_strategy)
def test_model_arc_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=model_Arc_strategy)
def test_model_arc_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=model_Ellipse_strategy)
@settings(max_examples=50)
def test_model_ellipse_instantiation(instance):
    assert isinstance(instance, model_Ellipse)

@given(instance=model_Rectangle_strategy)
@settings(max_examples=50)
def test_model_rectangle_instantiation(instance):
    assert isinstance(instance, model_Rectangle)

@given(instance=Figure_strategy)
@settings(max_examples=50)
def test_figure_instantiation(instance):
    assert isinstance(instance, Figure)

@given(instance=model_FigureContainer_strategy)
@settings(max_examples=50)
def test_model_figurecontainer_instantiation(instance):
    assert isinstance(instance, model_FigureContainer)

@given(instance=model_Image_strategy)
@settings(max_examples=50)
def test_model_image_instantiation(instance):
    assert isinstance(instance, model_Image)



@given(instance=model_Image_strategy)
def test_model_image_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original



@given(instance=model_Image_strategy)
def test_model_image_imageAlignment_setter(instance):
    original = instance.imageAlignment
    instance.imageAlignment = original
    assert instance.imageAlignment == original

@given(instance=model_Text_strategy)
@settings(max_examples=50)
def test_model_text_instantiation(instance):
    assert isinstance(instance, model_Text)



@given(instance=model_Text_strategy)
def test_model_text_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=model_Text_strategy)
def test_model_text_fontBold_setter(instance):
    original = instance.fontBold
    instance.fontBold = original
    assert instance.fontBold == original



@given(instance=model_Text_strategy)
def test_model_text_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=model_Text_strategy)
def test_model_text_labelAlignment_setter(instance):
    original = instance.labelAlignment
    instance.labelAlignment = original
    assert instance.labelAlignment == original



@given(instance=model_Text_strategy)
def test_model_text_textAlignment_setter(instance):
    original = instance.textAlignment
    instance.textAlignment = original
    assert instance.textAlignment == original



@given(instance=model_Text_strategy)
def test_model_text_fontItalic_setter(instance):
    original = instance.fontItalic
    instance.fontItalic = original
    assert instance.fontItalic == original



@given(instance=model_Text_strategy)
def test_model_text_iconAlignment_setter(instance):
    original = instance.iconAlignment
    instance.iconAlignment = original
    assert instance.iconAlignment == original



@given(instance=model_Text_strategy)
def test_model_text_fontSize_setter(instance):
    original = instance.fontSize
    instance.fontSize = original
    assert instance.fontSize == original



@given(instance=model_Text_strategy)
def test_model_text_textPlacement_setter(instance):
    original = instance.textPlacement
    instance.textPlacement = original
    assert instance.textPlacement == original



@given(instance=model_Text_strategy)
def test_model_text_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original

@given(instance=model_Shape_strategy)
@settings(max_examples=50)
def test_model_shape_instantiation(instance):
    assert isinstance(instance, model_Shape)



@given(instance=model_Shape_strategy)
def test_model_shape_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original



@given(instance=model_Shape_strategy)
def test_model_shape_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original



@given(instance=model_Shape_strategy)
def test_model_shape_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original



@given(instance=model_Shape_strategy)
def test_model_shape_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original



@given(instance=model_Shape_strategy)
def test_model_shape_antialias_setter(instance):
    original = instance.antialias
    instance.antialias = original
    assert instance.antialias == original

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=model_SymbolReference_strategy)
@settings(max_examples=50)
def test_model_symbolreference_instantiation(instance):
    assert isinstance(instance, model_SymbolReference)



@given(instance=model_SymbolReference_strategy)
def test_model_symbolreference_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original



@given(instance=model_SymbolReference_strategy)
def test_model_symbolreference_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original



@given(instance=model_SymbolReference_strategy)
def test_model_symbolreference_onCreateProperties_setter(instance):
    original = instance.onCreateProperties
    instance.onCreateProperties = original
    assert instance.onCreateProperties == original

@given(instance=model_Figure_strategy)
@settings(max_examples=50)
def test_model_figure_instantiation(instance):
    assert isinstance(instance, model_Figure)



@given(instance=model_Figure_strategy)
def test_model_figure_onDoubleClick_setter(instance):
    original = instance.onDoubleClick
    instance.onDoubleClick = original
    assert instance.onDoubleClick == original



@given(instance=model_Figure_strategy)
def test_model_figure_onMouseMove_setter(instance):
    original = instance.onMouseMove
    instance.onMouseMove = original
    assert instance.onMouseMove == original



@given(instance=model_Figure_strategy)
def test_model_figure_toolTip_setter(instance):
    original = instance.toolTip
    instance.toolTip = original
    assert instance.toolTip == original



@given(instance=model_Figure_strategy)
def test_model_figure_opaque_setter(instance):
    original = instance.opaque
    instance.opaque = original
    assert instance.opaque == original



@given(instance=model_Figure_strategy)
def test_model_figure_onClick_setter(instance):
    original = instance.onClick
    instance.onClick = original
    assert instance.onClick == original



@given(instance=model_Figure_strategy)
def test_model_figure_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original



@given(instance=model_Figure_strategy)
def test_model_figure_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=model_Figure_strategy)
def test_model_figure_onMouseOut_setter(instance):
    original = instance.onMouseOut
    instance.onMouseOut = original
    assert instance.onMouseOut == original



@given(instance=model_Figure_strategy)
def test_model_figure_onMouseDrag_setter(instance):
    original = instance.onMouseDrag
    instance.onMouseDrag = original
    assert instance.onMouseDrag == original



@given(instance=model_Figure_strategy)
def test_model_figure_onMouseIn_setter(instance):
    original = instance.onMouseIn
    instance.onMouseIn = original
    assert instance.onMouseIn == original



@given(instance=model_Figure_strategy)
def test_model_figure_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=model_Figure_strategy)
def test_model_figure_onMouseHover_setter(instance):
    original = instance.onMouseHover
    instance.onMouseHover = original
    assert instance.onMouseHover == original



@given(instance=model_Figure_strategy)
def test_model_figure_foregroundColor_setter(instance):
    original = instance.foregroundColor
    instance.foregroundColor = original
    assert instance.foregroundColor == original

@given(instance=model_Container_strategy)
@settings(max_examples=50)
def test_model_container_instantiation(instance):
    assert isinstance(instance, model_Container)

@given(instance=model_TimeTrigger_strategy)
@settings(max_examples=50)
def test_model_timetrigger_instantiation(instance):
    assert isinstance(instance, model_TimeTrigger)



@given(instance=model_TimeTrigger_strategy)
def test_model_timetrigger_onTrigger_setter(instance):
    original = instance.onTrigger
    instance.onTrigger = original
    assert instance.onTrigger == original



@given(instance=model_TimeTrigger_strategy)
def test_model_timetrigger_period_setter(instance):
    original = instance.period
    instance.period = original
    assert instance.period == original

@given(instance=model_Connection_strategy)
@settings(max_examples=50)
def test_model_connection_instantiation(instance):
    assert isinstance(instance, model_Connection)

@given(instance=model_Position_strategy)
@settings(max_examples=50)
def test_model_position_instantiation(instance):
    assert isinstance(instance, model_Position)



@given(instance=model_Position_strategy)
def test_model_position_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=model_Position_strategy)
def test_model_position_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Child_strategy)
@settings(max_examples=50)
def test_child_instantiation(instance):
    assert isinstance(instance, Child)

@given(instance=model_GridChild_strategy)
@settings(max_examples=50)
def test_model_gridchild_instantiation(instance):
    assert isinstance(instance, model_GridChild)



@given(instance=model_GridChild_strategy)
def test_model_gridchild_grabHorizontalSpace_setter(instance):
    original = instance.grabHorizontalSpace
    instance.grabHorizontalSpace = original
    assert instance.grabHorizontalSpace == original



@given(instance=model_GridChild_strategy)
def test_model_gridchild_grabVerticalSpace_setter(instance):
    original = instance.grabVerticalSpace
    instance.grabVerticalSpace = original
    assert instance.grabVerticalSpace == original



@given(instance=model_GridChild_strategy)
def test_model_gridchild_widthHint_setter(instance):
    original = instance.widthHint
    instance.widthHint = original
    assert instance.widthHint == original



@given(instance=model_GridChild_strategy)
def test_model_gridchild_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original



@given(instance=model_GridChild_strategy)
def test_model_gridchild_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original



@given(instance=model_GridChild_strategy)
def test_model_gridchild_heightHint_setter(instance):
    original = instance.heightHint
    instance.heightHint = original
    assert instance.heightHint == original



@given(instance=model_GridChild_strategy)
def test_model_gridchild_spanCols_setter(instance):
    original = instance.spanCols
    instance.spanCols = original
    assert instance.spanCols == original



@given(instance=model_GridChild_strategy)
def test_model_gridchild_spanRows_setter(instance):
    original = instance.spanRows
    instance.spanRows = original
    assert instance.spanRows == original

@given(instance=model_BorderChild_strategy)
@settings(max_examples=50)
def test_model_borderchild_instantiation(instance):
    assert isinstance(instance, model_BorderChild)



@given(instance=model_BorderChild_strategy)
def test_model_borderchild_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=model_XYChild_strategy)
@settings(max_examples=50)
def test_model_xychild_instantiation(instance):
    assert isinstance(instance, model_XYChild)

@given(instance=model_StringToStringMap_strategy)
@settings(max_examples=50)
def test_model_stringtostringmap_instantiation(instance):
    assert isinstance(instance, model_StringToStringMap)



@given(instance=model_StringToStringMap_strategy)
def test_model_stringtostringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=model_StringToStringMap_strategy)
def test_model_stringtostringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=model_Primitive_strategy)
@settings(max_examples=50)
def test_model_primitive_instantiation(instance):
    assert isinstance(instance, model_Primitive)



@given(instance=model_Primitive_strategy)
def test_model_primitive_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_Symbol_strategy)
@settings(max_examples=50)
def test_model_symbol_instantiation(instance):
    assert isinstance(instance, model_Symbol)



@given(instance=model_Symbol_strategy)
def test_model_symbol_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=model_Symbol_strategy)
def test_model_symbol_onUpdate_setter(instance):
    original = instance.onUpdate
    instance.onUpdate = original
    assert instance.onUpdate == original



@given(instance=model_Symbol_strategy)
def test_model_symbol_scriptModules_setter(instance):
    original = instance.scriptModules
    instance.scriptModules = original
    assert instance.scriptModules == original



@given(instance=model_Symbol_strategy)
def test_model_symbol_backgroundImage_setter(instance):
    original = instance.backgroundImage
    instance.backgroundImage = original
    assert instance.backgroundImage == original



@given(instance=model_Symbol_strategy)
def test_model_symbol_onDispose_setter(instance):
    original = instance.onDispose
    instance.onDispose = original
    assert instance.onDispose == original



@given(instance=model_Symbol_strategy)
def test_model_symbol_onInit_setter(instance):
    original = instance.onInit
    instance.onInit = original
    assert instance.onInit == original

@given(instance=model_Dimension_strategy)
@settings(max_examples=50)
def test_model_dimension_instantiation(instance):
    assert isinstance(instance, model_Dimension)



@given(instance=model_Dimension_strategy)
def test_model_dimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=model_Dimension_strategy)
def test_model_dimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=model_Cursor_strategy)
@settings(max_examples=50)
def test_model_cursor_instantiation(instance):
    assert isinstance(instance, model_Cursor)
