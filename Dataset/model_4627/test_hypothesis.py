import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Cursor,
    VisualInterface_SystemCursor,
    Container,
    VisualInterface_StackContainer,
    VisualInterface_BorderContainer,
    VisualInterface_GridContainer,
    VisualInterface_XYContainer,
    VisualInterface_Position,
    Child,
    VisualInterface_GridChild,
    VisualInterface_BorderChild,
    VisualInterface_XYChild,
    VisualInterface_Child,
    Figure,
    VisualInterface_FigureContainer,
    VisualInterface_Image,
    VisualInterface_Shape,
    Primitive,
    VisualInterface_Figure,
    VisualInterface_SymbolReference,
    VisualInterface_Container,
    VisualInterface_Connection,
    VisualInterface_Dimension,
    VisualInterface_Cursor,
    VisualInterface_StringToStringMap,
    VisualInterface_Primitive,
    VisualInterface_Symbol,
    VisualInterface_Text,
    Shape,
    VisualInterface_Rectangle,
    VisualInterface_Line,
    VisualInterface_Arc,
    VisualInterface_Ellipse,
    SystemCursorType,
    Alignment,
    Orientation,
    GridAlignment,
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



def test_visualinterface_systemcursor_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_SystemCursor)


def test_visualinterface_systemcursor_constructor_exists():
    assert callable(VisualInterface_SystemCursor.__init__)


def test_visualinterface_systemcursor_constructor_args():
    sig = inspect.signature(VisualInterface_SystemCursor.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_visualinterface_systemcursor_has_type():
    assert hasattr(VisualInterface_SystemCursor, "type")
    descriptor = None
    for klass in VisualInterface_SystemCursor.__mro__:
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



def test_visualinterface_stackcontainer_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_StackContainer)


def test_visualinterface_stackcontainer_constructor_exists():
    assert callable(VisualInterface_StackContainer.__init__)


def test_visualinterface_stackcontainer_constructor_args():
    sig = inspect.signature(VisualInterface_StackContainer.__init__)
    params = list(sig.parameters.keys())



def test_visualinterface_bordercontainer_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_BorderContainer)


def test_visualinterface_bordercontainer_constructor_exists():
    assert callable(VisualInterface_BorderContainer.__init__)


def test_visualinterface_bordercontainer_constructor_args():
    sig = inspect.signature(VisualInterface_BorderContainer.__init__)
    params = list(sig.parameters.keys())
    assert "horizontalSpacing" in params, "Missing parameter 'horizontalSpacing'"
    assert "verticalSpacing" in params, "Missing parameter 'verticalSpacing'"

def test_visualinterface_bordercontainer_has_horizontalSpacing():
    assert hasattr(VisualInterface_BorderContainer, "horizontalSpacing")
    descriptor = None
    for klass in VisualInterface_BorderContainer.__mro__:
        if "horizontalSpacing" in klass.__dict__:
            descriptor = klass.__dict__["horizontalSpacing"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_bordercontainer_has_verticalSpacing():
    assert hasattr(VisualInterface_BorderContainer, "verticalSpacing")
    descriptor = None
    for klass in VisualInterface_BorderContainer.__mro__:
        if "verticalSpacing" in klass.__dict__:
            descriptor = klass.__dict__["verticalSpacing"]
            break
    assert isinstance(descriptor, property)



def test_visualinterface_gridcontainer_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_GridContainer)


def test_visualinterface_gridcontainer_constructor_exists():
    assert callable(VisualInterface_GridContainer.__init__)


def test_visualinterface_gridcontainer_constructor_args():
    sig = inspect.signature(VisualInterface_GridContainer.__init__)
    params = list(sig.parameters.keys())
    assert "marginHeight" in params, "Missing parameter 'marginHeight'"
    assert "verticalSpacing" in params, "Missing parameter 'verticalSpacing'"
    assert "marginWidth" in params, "Missing parameter 'marginWidth'"
    assert "equalWidth" in params, "Missing parameter 'equalWidth'"
    assert "columns" in params, "Missing parameter 'columns'"
    assert "horizontalSpacing" in params, "Missing parameter 'horizontalSpacing'"

def test_visualinterface_gridcontainer_has_marginHeight():
    assert hasattr(VisualInterface_GridContainer, "marginHeight")
    descriptor = None
    for klass in VisualInterface_GridContainer.__mro__:
        if "marginHeight" in klass.__dict__:
            descriptor = klass.__dict__["marginHeight"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_gridcontainer_has_verticalSpacing():
    assert hasattr(VisualInterface_GridContainer, "verticalSpacing")
    descriptor = None
    for klass in VisualInterface_GridContainer.__mro__:
        if "verticalSpacing" in klass.__dict__:
            descriptor = klass.__dict__["verticalSpacing"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_gridcontainer_has_marginWidth():
    assert hasattr(VisualInterface_GridContainer, "marginWidth")
    descriptor = None
    for klass in VisualInterface_GridContainer.__mro__:
        if "marginWidth" in klass.__dict__:
            descriptor = klass.__dict__["marginWidth"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_gridcontainer_has_equalWidth():
    assert hasattr(VisualInterface_GridContainer, "equalWidth")
    descriptor = None
    for klass in VisualInterface_GridContainer.__mro__:
        if "equalWidth" in klass.__dict__:
            descriptor = klass.__dict__["equalWidth"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_gridcontainer_has_columns():
    assert hasattr(VisualInterface_GridContainer, "columns")
    descriptor = None
    for klass in VisualInterface_GridContainer.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_gridcontainer_has_horizontalSpacing():
    assert hasattr(VisualInterface_GridContainer, "horizontalSpacing")
    descriptor = None
    for klass in VisualInterface_GridContainer.__mro__:
        if "horizontalSpacing" in klass.__dict__:
            descriptor = klass.__dict__["horizontalSpacing"]
            break
    assert isinstance(descriptor, property)



def test_visualinterface_xycontainer_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_XYContainer)


def test_visualinterface_xycontainer_constructor_exists():
    assert callable(VisualInterface_XYContainer.__init__)


def test_visualinterface_xycontainer_constructor_args():
    sig = inspect.signature(VisualInterface_XYContainer.__init__)
    params = list(sig.parameters.keys())



def test_visualinterface_position_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Position)


def test_visualinterface_position_constructor_exists():
    assert callable(VisualInterface_Position.__init__)


def test_visualinterface_position_constructor_args():
    sig = inspect.signature(VisualInterface_Position.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_visualinterface_position_has_x():
    assert hasattr(VisualInterface_Position, "x")
    descriptor = None
    for klass in VisualInterface_Position.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_position_has_y():
    assert hasattr(VisualInterface_Position, "y")
    descriptor = None
    for klass in VisualInterface_Position.__mro__:
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



def test_visualinterface_gridchild_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_GridChild)


def test_visualinterface_gridchild_constructor_exists():
    assert callable(VisualInterface_GridChild.__init__)


def test_visualinterface_gridchild_constructor_args():
    sig = inspect.signature(VisualInterface_GridChild.__init__)
    params = list(sig.parameters.keys())
    assert "widthHint" in params, "Missing parameter 'widthHint'"
    assert "spanRows" in params, "Missing parameter 'spanRows'"
    assert "grabHorizontalSpace" in params, "Missing parameter 'grabHorizontalSpace'"
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"
    assert "spanCols" in params, "Missing parameter 'spanCols'"
    assert "grabVerticalSpace" in params, "Missing parameter 'grabVerticalSpace'"
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"
    assert "heightHint" in params, "Missing parameter 'heightHint'"

def test_visualinterface_gridchild_has_widthHint():
    assert hasattr(VisualInterface_GridChild, "widthHint")
    descriptor = None
    for klass in VisualInterface_GridChild.__mro__:
        if "widthHint" in klass.__dict__:
            descriptor = klass.__dict__["widthHint"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_gridchild_has_spanRows():
    assert hasattr(VisualInterface_GridChild, "spanRows")
    descriptor = None
    for klass in VisualInterface_GridChild.__mro__:
        if "spanRows" in klass.__dict__:
            descriptor = klass.__dict__["spanRows"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_gridchild_has_grabHorizontalSpace():
    assert hasattr(VisualInterface_GridChild, "grabHorizontalSpace")
    descriptor = None
    for klass in VisualInterface_GridChild.__mro__:
        if "grabHorizontalSpace" in klass.__dict__:
            descriptor = klass.__dict__["grabHorizontalSpace"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_gridchild_has_verticalAlignment():
    assert hasattr(VisualInterface_GridChild, "verticalAlignment")
    descriptor = None
    for klass in VisualInterface_GridChild.__mro__:
        if "verticalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_gridchild_has_spanCols():
    assert hasattr(VisualInterface_GridChild, "spanCols")
    descriptor = None
    for klass in VisualInterface_GridChild.__mro__:
        if "spanCols" in klass.__dict__:
            descriptor = klass.__dict__["spanCols"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_gridchild_has_grabVerticalSpace():
    assert hasattr(VisualInterface_GridChild, "grabVerticalSpace")
    descriptor = None
    for klass in VisualInterface_GridChild.__mro__:
        if "grabVerticalSpace" in klass.__dict__:
            descriptor = klass.__dict__["grabVerticalSpace"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_gridchild_has_horizontalAlignment():
    assert hasattr(VisualInterface_GridChild, "horizontalAlignment")
    descriptor = None
    for klass in VisualInterface_GridChild.__mro__:
        if "horizontalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["horizontalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_gridchild_has_heightHint():
    assert hasattr(VisualInterface_GridChild, "heightHint")
    descriptor = None
    for klass in VisualInterface_GridChild.__mro__:
        if "heightHint" in klass.__dict__:
            descriptor = klass.__dict__["heightHint"]
            break
    assert isinstance(descriptor, property)



def test_visualinterface_borderchild_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_BorderChild)


def test_visualinterface_borderchild_constructor_exists():
    assert callable(VisualInterface_BorderChild.__init__)


def test_visualinterface_borderchild_constructor_args():
    sig = inspect.signature(VisualInterface_BorderChild.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_visualinterface_borderchild_has_alignment():
    assert hasattr(VisualInterface_BorderChild, "alignment")
    descriptor = None
    for klass in VisualInterface_BorderChild.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_visualinterface_xychild_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_XYChild)


def test_visualinterface_xychild_constructor_exists():
    assert callable(VisualInterface_XYChild.__init__)


def test_visualinterface_xychild_constructor_args():
    sig = inspect.signature(VisualInterface_XYChild.__init__)
    params = list(sig.parameters.keys())



def test_visualinterface_child_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Child)


def test_visualinterface_child_constructor_exists():
    assert callable(VisualInterface_Child.__init__)


def test_visualinterface_child_constructor_args():
    sig = inspect.signature(VisualInterface_Child.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_visualinterface_child_has_name():
    assert hasattr(VisualInterface_Child, "name")
    descriptor = None
    for klass in VisualInterface_Child.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_visualinterface_figurecontainer_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_FigureContainer)


def test_visualinterface_figurecontainer_constructor_exists():
    assert callable(VisualInterface_FigureContainer.__init__)


def test_visualinterface_figurecontainer_constructor_args():
    sig = inspect.signature(VisualInterface_FigureContainer.__init__)
    params = list(sig.parameters.keys())



def test_visualinterface_image_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Image)


def test_visualinterface_image_constructor_exists():
    assert callable(VisualInterface_Image.__init__)


def test_visualinterface_image_constructor_args():
    sig = inspect.signature(VisualInterface_Image.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_visualinterface_image_has_uri():
    assert hasattr(VisualInterface_Image, "uri")
    descriptor = None
    for klass in VisualInterface_Image.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_visualinterface_shape_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Shape)


def test_visualinterface_shape_constructor_exists():
    assert callable(VisualInterface_Shape.__init__)


def test_visualinterface_shape_constructor_args():
    sig = inspect.signature(VisualInterface_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "antialias" in params, "Missing parameter 'antialias'"
    assert "outline" in params, "Missing parameter 'outline'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "fill" in params, "Missing parameter 'fill'"
    assert "alpha" in params, "Missing parameter 'alpha'"

def test_visualinterface_shape_has_antialias():
    assert hasattr(VisualInterface_Shape, "antialias")
    descriptor = None
    for klass in VisualInterface_Shape.__mro__:
        if "antialias" in klass.__dict__:
            descriptor = klass.__dict__["antialias"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_shape_has_outline():
    assert hasattr(VisualInterface_Shape, "outline")
    descriptor = None
    for klass in VisualInterface_Shape.__mro__:
        if "outline" in klass.__dict__:
            descriptor = klass.__dict__["outline"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_shape_has_lineWidth():
    assert hasattr(VisualInterface_Shape, "lineWidth")
    descriptor = None
    for klass in VisualInterface_Shape.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_shape_has_fill():
    assert hasattr(VisualInterface_Shape, "fill")
    descriptor = None
    for klass in VisualInterface_Shape.__mro__:
        if "fill" in klass.__dict__:
            descriptor = klass.__dict__["fill"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_shape_has_alpha():
    assert hasattr(VisualInterface_Shape, "alpha")
    descriptor = None
    for klass in VisualInterface_Shape.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_visualinterface_figure_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Figure)


def test_visualinterface_figure_constructor_exists():
    assert callable(VisualInterface_Figure.__init__)


def test_visualinterface_figure_constructor_args():
    sig = inspect.signature(VisualInterface_Figure.__init__)
    params = list(sig.parameters.keys())
    assert "onDoubleClick" in params, "Missing parameter 'onDoubleClick'"
    assert "onClick" in params, "Missing parameter 'onClick'"
    assert "toolTip" in params, "Missing parameter 'toolTip'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "border" in params, "Missing parameter 'border'"
    assert "opaque" in params, "Missing parameter 'opaque'"
    assert "foregroundColor" in params, "Missing parameter 'foregroundColor'"

def test_visualinterface_figure_has_onDoubleClick():
    assert hasattr(VisualInterface_Figure, "onDoubleClick")
    descriptor = None
    for klass in VisualInterface_Figure.__mro__:
        if "onDoubleClick" in klass.__dict__:
            descriptor = klass.__dict__["onDoubleClick"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_figure_has_onClick():
    assert hasattr(VisualInterface_Figure, "onClick")
    descriptor = None
    for klass in VisualInterface_Figure.__mro__:
        if "onClick" in klass.__dict__:
            descriptor = klass.__dict__["onClick"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_figure_has_toolTip():
    assert hasattr(VisualInterface_Figure, "toolTip")
    descriptor = None
    for klass in VisualInterface_Figure.__mro__:
        if "toolTip" in klass.__dict__:
            descriptor = klass.__dict__["toolTip"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_figure_has_backgroundColor():
    assert hasattr(VisualInterface_Figure, "backgroundColor")
    descriptor = None
    for klass in VisualInterface_Figure.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_figure_has_visible():
    assert hasattr(VisualInterface_Figure, "visible")
    descriptor = None
    for klass in VisualInterface_Figure.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_figure_has_border():
    assert hasattr(VisualInterface_Figure, "border")
    descriptor = None
    for klass in VisualInterface_Figure.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_figure_has_opaque():
    assert hasattr(VisualInterface_Figure, "opaque")
    descriptor = None
    for klass in VisualInterface_Figure.__mro__:
        if "opaque" in klass.__dict__:
            descriptor = klass.__dict__["opaque"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_figure_has_foregroundColor():
    assert hasattr(VisualInterface_Figure, "foregroundColor")
    descriptor = None
    for klass in VisualInterface_Figure.__mro__:
        if "foregroundColor" in klass.__dict__:
            descriptor = klass.__dict__["foregroundColor"]
            break
    assert isinstance(descriptor, property)



def test_visualinterface_symbolreference_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_SymbolReference)


def test_visualinterface_symbolreference_constructor_exists():
    assert callable(VisualInterface_SymbolReference.__init__)


def test_visualinterface_symbolreference_constructor_args():
    sig = inspect.signature(VisualInterface_SymbolReference.__init__)
    params = list(sig.parameters.keys())
    assert "zoom" in params, "Missing parameter 'zoom'"
    assert "onCreateProperties" in params, "Missing parameter 'onCreateProperties'"
    assert "uri" in params, "Missing parameter 'uri'"

def test_visualinterface_symbolreference_has_zoom():
    assert hasattr(VisualInterface_SymbolReference, "zoom")
    descriptor = None
    for klass in VisualInterface_SymbolReference.__mro__:
        if "zoom" in klass.__dict__:
            descriptor = klass.__dict__["zoom"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_symbolreference_has_onCreateProperties():
    assert hasattr(VisualInterface_SymbolReference, "onCreateProperties")
    descriptor = None
    for klass in VisualInterface_SymbolReference.__mro__:
        if "onCreateProperties" in klass.__dict__:
            descriptor = klass.__dict__["onCreateProperties"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_symbolreference_has_uri():
    assert hasattr(VisualInterface_SymbolReference, "uri")
    descriptor = None
    for klass in VisualInterface_SymbolReference.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_visualinterface_container_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Container)


def test_visualinterface_container_constructor_exists():
    assert callable(VisualInterface_Container.__init__)


def test_visualinterface_container_constructor_args():
    sig = inspect.signature(VisualInterface_Container.__init__)
    params = list(sig.parameters.keys())



def test_visualinterface_connection_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Connection)


def test_visualinterface_connection_constructor_exists():
    assert callable(VisualInterface_Connection.__init__)


def test_visualinterface_connection_constructor_args():
    sig = inspect.signature(VisualInterface_Connection.__init__)
    params = list(sig.parameters.keys())



def test_visualinterface_dimension_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Dimension)


def test_visualinterface_dimension_constructor_exists():
    assert callable(VisualInterface_Dimension.__init__)


def test_visualinterface_dimension_constructor_args():
    sig = inspect.signature(VisualInterface_Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_visualinterface_dimension_has_width():
    assert hasattr(VisualInterface_Dimension, "width")
    descriptor = None
    for klass in VisualInterface_Dimension.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_dimension_has_height():
    assert hasattr(VisualInterface_Dimension, "height")
    descriptor = None
    for klass in VisualInterface_Dimension.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_visualinterface_cursor_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Cursor)


def test_visualinterface_cursor_constructor_exists():
    assert callable(VisualInterface_Cursor.__init__)


def test_visualinterface_cursor_constructor_args():
    sig = inspect.signature(VisualInterface_Cursor.__init__)
    params = list(sig.parameters.keys())



def test_visualinterface_stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_StringToStringMap)


def test_visualinterface_stringtostringmap_constructor_exists():
    assert callable(VisualInterface_StringToStringMap.__init__)


def test_visualinterface_stringtostringmap_constructor_args():
    sig = inspect.signature(VisualInterface_StringToStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_visualinterface_stringtostringmap_has_key():
    assert hasattr(VisualInterface_StringToStringMap, "key")
    descriptor = None
    for klass in VisualInterface_StringToStringMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_stringtostringmap_has_value():
    assert hasattr(VisualInterface_StringToStringMap, "value")
    descriptor = None
    for klass in VisualInterface_StringToStringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_visualinterface_primitive_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Primitive)


def test_visualinterface_primitive_constructor_exists():
    assert callable(VisualInterface_Primitive.__init__)


def test_visualinterface_primitive_constructor_args():
    sig = inspect.signature(VisualInterface_Primitive.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_visualinterface_primitive_has_name():
    assert hasattr(VisualInterface_Primitive, "name")
    descriptor = None
    for klass in VisualInterface_Primitive.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_visualinterface_symbol_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Symbol)


def test_visualinterface_symbol_constructor_exists():
    assert callable(VisualInterface_Symbol.__init__)


def test_visualinterface_symbol_constructor_args():
    sig = inspect.signature(VisualInterface_Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "scriptModules" in params, "Missing parameter 'scriptModules'"
    assert "onInit" in params, "Missing parameter 'onInit'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "onUpdate" in params, "Missing parameter 'onUpdate'"
    assert "onDispose" in params, "Missing parameter 'onDispose'"

def test_visualinterface_symbol_has_scriptModules():
    assert hasattr(VisualInterface_Symbol, "scriptModules")
    descriptor = None
    for klass in VisualInterface_Symbol.__mro__:
        if "scriptModules" in klass.__dict__:
            descriptor = klass.__dict__["scriptModules"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_symbol_has_onInit():
    assert hasattr(VisualInterface_Symbol, "onInit")
    descriptor = None
    for klass in VisualInterface_Symbol.__mro__:
        if "onInit" in klass.__dict__:
            descriptor = klass.__dict__["onInit"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_symbol_has_backgroundColor():
    assert hasattr(VisualInterface_Symbol, "backgroundColor")
    descriptor = None
    for klass in VisualInterface_Symbol.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_symbol_has_onUpdate():
    assert hasattr(VisualInterface_Symbol, "onUpdate")
    descriptor = None
    for klass in VisualInterface_Symbol.__mro__:
        if "onUpdate" in klass.__dict__:
            descriptor = klass.__dict__["onUpdate"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_symbol_has_onDispose():
    assert hasattr(VisualInterface_Symbol, "onDispose")
    descriptor = None
    for klass in VisualInterface_Symbol.__mro__:
        if "onDispose" in klass.__dict__:
            descriptor = klass.__dict__["onDispose"]
            break
    assert isinstance(descriptor, property)



def test_visualinterface_text_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Text)


def test_visualinterface_text_constructor_exists():
    assert callable(VisualInterface_Text.__init__)


def test_visualinterface_text_constructor_args():
    sig = inspect.signature(VisualInterface_Text.__init__)
    params = list(sig.parameters.keys())
    assert "textPlacement" in params, "Missing parameter 'textPlacement'"
    assert "iconAlignment" in params, "Missing parameter 'iconAlignment'"
    assert "fontItalic" in params, "Missing parameter 'fontItalic'"
    assert "fontName" in params, "Missing parameter 'fontName'"
    assert "textAlignment" in params, "Missing parameter 'textAlignment'"
    assert "labelAlignment" in params, "Missing parameter 'labelAlignment'"
    assert "fontSize" in params, "Missing parameter 'fontSize'"
    assert "fontBold" in params, "Missing parameter 'fontBold'"
    assert "text" in params, "Missing parameter 'text'"

def test_visualinterface_text_has_textPlacement():
    assert hasattr(VisualInterface_Text, "textPlacement")
    descriptor = None
    for klass in VisualInterface_Text.__mro__:
        if "textPlacement" in klass.__dict__:
            descriptor = klass.__dict__["textPlacement"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_text_has_iconAlignment():
    assert hasattr(VisualInterface_Text, "iconAlignment")
    descriptor = None
    for klass in VisualInterface_Text.__mro__:
        if "iconAlignment" in klass.__dict__:
            descriptor = klass.__dict__["iconAlignment"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_text_has_fontItalic():
    assert hasattr(VisualInterface_Text, "fontItalic")
    descriptor = None
    for klass in VisualInterface_Text.__mro__:
        if "fontItalic" in klass.__dict__:
            descriptor = klass.__dict__["fontItalic"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_text_has_fontName():
    assert hasattr(VisualInterface_Text, "fontName")
    descriptor = None
    for klass in VisualInterface_Text.__mro__:
        if "fontName" in klass.__dict__:
            descriptor = klass.__dict__["fontName"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_text_has_textAlignment():
    assert hasattr(VisualInterface_Text, "textAlignment")
    descriptor = None
    for klass in VisualInterface_Text.__mro__:
        if "textAlignment" in klass.__dict__:
            descriptor = klass.__dict__["textAlignment"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_text_has_labelAlignment():
    assert hasattr(VisualInterface_Text, "labelAlignment")
    descriptor = None
    for klass in VisualInterface_Text.__mro__:
        if "labelAlignment" in klass.__dict__:
            descriptor = klass.__dict__["labelAlignment"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_text_has_fontSize():
    assert hasattr(VisualInterface_Text, "fontSize")
    descriptor = None
    for klass in VisualInterface_Text.__mro__:
        if "fontSize" in klass.__dict__:
            descriptor = klass.__dict__["fontSize"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_text_has_fontBold():
    assert hasattr(VisualInterface_Text, "fontBold")
    descriptor = None
    for klass in VisualInterface_Text.__mro__:
        if "fontBold" in klass.__dict__:
            descriptor = klass.__dict__["fontBold"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_text_has_text():
    assert hasattr(VisualInterface_Text, "text")
    descriptor = None
    for klass in VisualInterface_Text.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_visualinterface_rectangle_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Rectangle)


def test_visualinterface_rectangle_constructor_exists():
    assert callable(VisualInterface_Rectangle.__init__)


def test_visualinterface_rectangle_constructor_args():
    sig = inspect.signature(VisualInterface_Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_visualinterface_line_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Line)


def test_visualinterface_line_constructor_exists():
    assert callable(VisualInterface_Line.__init__)


def test_visualinterface_line_constructor_args():
    sig = inspect.signature(VisualInterface_Line.__init__)
    params = list(sig.parameters.keys())



def test_visualinterface_arc_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Arc)


def test_visualinterface_arc_constructor_exists():
    assert callable(VisualInterface_Arc.__init__)


def test_visualinterface_arc_constructor_args():
    sig = inspect.signature(VisualInterface_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "length" in params, "Missing parameter 'length'"

def test_visualinterface_arc_has_start():
    assert hasattr(VisualInterface_Arc, "start")
    descriptor = None
    for klass in VisualInterface_Arc.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_visualinterface_arc_has_length():
    assert hasattr(VisualInterface_Arc, "length")
    descriptor = None
    for klass in VisualInterface_Arc.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_visualinterface_ellipse_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Ellipse)


def test_visualinterface_ellipse_constructor_exists():
    assert callable(VisualInterface_Ellipse.__init__)


def test_visualinterface_ellipse_constructor_args():
    sig = inspect.signature(VisualInterface_Ellipse.__init__)
    params = list(sig.parameters.keys())

def test_systemcursortype_exists():
    # Check that the Enumeration exists
    assert SystemCursorType is not None

def test_systemcursortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SystemCursorType]
    expected_literals = [
        "HAND",
        "ARROW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SystemCursorType"

def test_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "RIGHT",
        "LEFT",
        "CENTER",
        "BOTTOM",
        "TOP",
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
        "NORTH",
        "WEST",
        "SOUTH",
        "EAST",
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
        "BEGINNING",
        "END",
        "FILL",
        "CENTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GridAlignment"


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
VisualInterface_SystemCursor_strategy = st.builds(
    VisualInterface_SystemCursor,
    type=
        safe_text
)
Container_strategy = st.builds(
    Container,
)
VisualInterface_StackContainer_strategy = st.builds(
    VisualInterface_StackContainer,
)
VisualInterface_BorderContainer_strategy = st.builds(
    VisualInterface_BorderContainer,
    horizontalSpacing=
        st.integers(),
    verticalSpacing=
        st.integers()
)
VisualInterface_GridContainer_strategy = st.builds(
    VisualInterface_GridContainer,
    marginHeight=
        st.integers(),
    verticalSpacing=
        st.integers(),
    marginWidth=
        st.integers(),
    equalWidth=
        st.booleans(),
    columns=
        st.integers(),
    horizontalSpacing=
        st.integers()
)
VisualInterface_XYContainer_strategy = st.builds(
    VisualInterface_XYContainer,
)
VisualInterface_Position_strategy = st.builds(
    VisualInterface_Position,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Child_strategy = st.builds(
    Child,
)
VisualInterface_GridChild_strategy = st.builds(
    VisualInterface_GridChild,
    widthHint=
        safe_text,
    spanRows=
        safe_text,
    grabHorizontalSpace=
        st.booleans(),
    verticalAlignment=
        safe_text,
    spanCols=
        st.integers(),
    grabVerticalSpace=
        st.booleans(),
    horizontalAlignment=
        safe_text,
    heightHint=
        safe_text
)
VisualInterface_BorderChild_strategy = st.builds(
    VisualInterface_BorderChild,
    alignment=
        safe_text
)
VisualInterface_XYChild_strategy = st.builds(
    VisualInterface_XYChild,
)
VisualInterface_Child_strategy = st.builds(
    VisualInterface_Child,
    name=
        safe_text
)
Figure_strategy = st.builds(
    Figure,
)
VisualInterface_FigureContainer_strategy = st.builds(
    VisualInterface_FigureContainer,
)
VisualInterface_Image_strategy = st.builds(
    VisualInterface_Image,
    uri=
        safe_text
)
VisualInterface_Shape_strategy = st.builds(
    VisualInterface_Shape,
    antialias=
        safe_text,
    outline=
        st.booleans(),
    lineWidth=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    fill=
        st.booleans(),
    alpha=
        safe_text
)
Primitive_strategy = st.builds(
    Primitive,
)
VisualInterface_Figure_strategy = st.builds(
    VisualInterface_Figure,
    onDoubleClick=
        safe_text,
    onClick=
        safe_text,
    toolTip=
        safe_text,
    backgroundColor=
        safe_text,
    visible=
        st.booleans(),
    border=
        safe_text,
    opaque=
        safe_text,
    foregroundColor=
        safe_text
)
VisualInterface_SymbolReference_strategy = st.builds(
    VisualInterface_SymbolReference,
    zoom=
        safe_text,
    onCreateProperties=
        safe_text,
    uri=
        safe_text
)
VisualInterface_Container_strategy = st.builds(
    VisualInterface_Container,
)
VisualInterface_Connection_strategy = st.builds(
    VisualInterface_Connection,
)
VisualInterface_Dimension_strategy = st.builds(
    VisualInterface_Dimension,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
VisualInterface_Cursor_strategy = st.builds(
    VisualInterface_Cursor,
)
VisualInterface_StringToStringMap_strategy = st.builds(
    VisualInterface_StringToStringMap,
    key=
        safe_text,
    value=
        safe_text
)
VisualInterface_Primitive_strategy = st.builds(
    VisualInterface_Primitive,
    name=
        safe_text
)
VisualInterface_Symbol_strategy = st.builds(
    VisualInterface_Symbol,
    scriptModules=
        safe_text,
    onInit=
        safe_text,
    backgroundColor=
        safe_text,
    onUpdate=
        safe_text,
    onDispose=
        safe_text
)
VisualInterface_Text_strategy = st.builds(
    VisualInterface_Text,
    textPlacement=
        safe_text,
    iconAlignment=
        safe_text,
    fontItalic=
        st.booleans(),
    fontName=
        safe_text,
    textAlignment=
        safe_text,
    labelAlignment=
        safe_text,
    fontSize=
        st.integers(),
    fontBold=
        st.booleans(),
    text=
        safe_text
)
Shape_strategy = st.builds(
    Shape,
)
VisualInterface_Rectangle_strategy = st.builds(
    VisualInterface_Rectangle,
)
VisualInterface_Line_strategy = st.builds(
    VisualInterface_Line,
)
VisualInterface_Arc_strategy = st.builds(
    VisualInterface_Arc,
    start=
        st.integers(),
    length=
        st.integers()
)
VisualInterface_Ellipse_strategy = st.builds(
    VisualInterface_Ellipse,
)

@given(instance=Cursor_strategy)
@settings(max_examples=50)
def test_cursor_instantiation(instance):
    assert isinstance(instance, Cursor)

@given(instance=VisualInterface_SystemCursor_strategy)
@settings(max_examples=50)
def test_visualinterface_systemcursor_instantiation(instance):
    assert isinstance(instance, VisualInterface_SystemCursor)



@given(instance=VisualInterface_SystemCursor_strategy)
def test_visualinterface_systemcursor_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Container_strategy)
@settings(max_examples=50)
def test_container_instantiation(instance):
    assert isinstance(instance, Container)

@given(instance=VisualInterface_StackContainer_strategy)
@settings(max_examples=50)
def test_visualinterface_stackcontainer_instantiation(instance):
    assert isinstance(instance, VisualInterface_StackContainer)

@given(instance=VisualInterface_BorderContainer_strategy)
@settings(max_examples=50)
def test_visualinterface_bordercontainer_instantiation(instance):
    assert isinstance(instance, VisualInterface_BorderContainer)



@given(instance=VisualInterface_BorderContainer_strategy)
def test_visualinterface_bordercontainer_horizontalSpacing_setter(instance):
    original = instance.horizontalSpacing
    instance.horizontalSpacing = original
    assert instance.horizontalSpacing == original



@given(instance=VisualInterface_BorderContainer_strategy)
def test_visualinterface_bordercontainer_verticalSpacing_setter(instance):
    original = instance.verticalSpacing
    instance.verticalSpacing = original
    assert instance.verticalSpacing == original

@given(instance=VisualInterface_GridContainer_strategy)
@settings(max_examples=50)
def test_visualinterface_gridcontainer_instantiation(instance):
    assert isinstance(instance, VisualInterface_GridContainer)



@given(instance=VisualInterface_GridContainer_strategy)
def test_visualinterface_gridcontainer_marginHeight_setter(instance):
    original = instance.marginHeight
    instance.marginHeight = original
    assert instance.marginHeight == original



@given(instance=VisualInterface_GridContainer_strategy)
def test_visualinterface_gridcontainer_verticalSpacing_setter(instance):
    original = instance.verticalSpacing
    instance.verticalSpacing = original
    assert instance.verticalSpacing == original



@given(instance=VisualInterface_GridContainer_strategy)
def test_visualinterface_gridcontainer_marginWidth_setter(instance):
    original = instance.marginWidth
    instance.marginWidth = original
    assert instance.marginWidth == original



@given(instance=VisualInterface_GridContainer_strategy)
def test_visualinterface_gridcontainer_equalWidth_setter(instance):
    original = instance.equalWidth
    instance.equalWidth = original
    assert instance.equalWidth == original



@given(instance=VisualInterface_GridContainer_strategy)
def test_visualinterface_gridcontainer_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original



@given(instance=VisualInterface_GridContainer_strategy)
def test_visualinterface_gridcontainer_horizontalSpacing_setter(instance):
    original = instance.horizontalSpacing
    instance.horizontalSpacing = original
    assert instance.horizontalSpacing == original

@given(instance=VisualInterface_XYContainer_strategy)
@settings(max_examples=50)
def test_visualinterface_xycontainer_instantiation(instance):
    assert isinstance(instance, VisualInterface_XYContainer)

@given(instance=VisualInterface_Position_strategy)
@settings(max_examples=50)
def test_visualinterface_position_instantiation(instance):
    assert isinstance(instance, VisualInterface_Position)



@given(instance=VisualInterface_Position_strategy)
def test_visualinterface_position_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=VisualInterface_Position_strategy)
def test_visualinterface_position_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Child_strategy)
@settings(max_examples=50)
def test_child_instantiation(instance):
    assert isinstance(instance, Child)

@given(instance=VisualInterface_GridChild_strategy)
@settings(max_examples=50)
def test_visualinterface_gridchild_instantiation(instance):
    assert isinstance(instance, VisualInterface_GridChild)



@given(instance=VisualInterface_GridChild_strategy)
def test_visualinterface_gridchild_widthHint_setter(instance):
    original = instance.widthHint
    instance.widthHint = original
    assert instance.widthHint == original



@given(instance=VisualInterface_GridChild_strategy)
def test_visualinterface_gridchild_spanRows_setter(instance):
    original = instance.spanRows
    instance.spanRows = original
    assert instance.spanRows == original



@given(instance=VisualInterface_GridChild_strategy)
def test_visualinterface_gridchild_grabHorizontalSpace_setter(instance):
    original = instance.grabHorizontalSpace
    instance.grabHorizontalSpace = original
    assert instance.grabHorizontalSpace == original



@given(instance=VisualInterface_GridChild_strategy)
def test_visualinterface_gridchild_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original



@given(instance=VisualInterface_GridChild_strategy)
def test_visualinterface_gridchild_spanCols_setter(instance):
    original = instance.spanCols
    instance.spanCols = original
    assert instance.spanCols == original



@given(instance=VisualInterface_GridChild_strategy)
def test_visualinterface_gridchild_grabVerticalSpace_setter(instance):
    original = instance.grabVerticalSpace
    instance.grabVerticalSpace = original
    assert instance.grabVerticalSpace == original



@given(instance=VisualInterface_GridChild_strategy)
def test_visualinterface_gridchild_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original



@given(instance=VisualInterface_GridChild_strategy)
def test_visualinterface_gridchild_heightHint_setter(instance):
    original = instance.heightHint
    instance.heightHint = original
    assert instance.heightHint == original

@given(instance=VisualInterface_BorderChild_strategy)
@settings(max_examples=50)
def test_visualinterface_borderchild_instantiation(instance):
    assert isinstance(instance, VisualInterface_BorderChild)



@given(instance=VisualInterface_BorderChild_strategy)
def test_visualinterface_borderchild_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=VisualInterface_XYChild_strategy)
@settings(max_examples=50)
def test_visualinterface_xychild_instantiation(instance):
    assert isinstance(instance, VisualInterface_XYChild)

@given(instance=VisualInterface_Child_strategy)
@settings(max_examples=50)
def test_visualinterface_child_instantiation(instance):
    assert isinstance(instance, VisualInterface_Child)



@given(instance=VisualInterface_Child_strategy)
def test_visualinterface_child_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Figure_strategy)
@settings(max_examples=50)
def test_figure_instantiation(instance):
    assert isinstance(instance, Figure)

@given(instance=VisualInterface_FigureContainer_strategy)
@settings(max_examples=50)
def test_visualinterface_figurecontainer_instantiation(instance):
    assert isinstance(instance, VisualInterface_FigureContainer)

@given(instance=VisualInterface_Image_strategy)
@settings(max_examples=50)
def test_visualinterface_image_instantiation(instance):
    assert isinstance(instance, VisualInterface_Image)



@given(instance=VisualInterface_Image_strategy)
def test_visualinterface_image_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=VisualInterface_Shape_strategy)
@settings(max_examples=50)
def test_visualinterface_shape_instantiation(instance):
    assert isinstance(instance, VisualInterface_Shape)



@given(instance=VisualInterface_Shape_strategy)
def test_visualinterface_shape_antialias_setter(instance):
    original = instance.antialias
    instance.antialias = original
    assert instance.antialias == original



@given(instance=VisualInterface_Shape_strategy)
def test_visualinterface_shape_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original



@given(instance=VisualInterface_Shape_strategy)
def test_visualinterface_shape_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original



@given(instance=VisualInterface_Shape_strategy)
def test_visualinterface_shape_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original



@given(instance=VisualInterface_Shape_strategy)
def test_visualinterface_shape_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=VisualInterface_Figure_strategy)
@settings(max_examples=50)
def test_visualinterface_figure_instantiation(instance):
    assert isinstance(instance, VisualInterface_Figure)



@given(instance=VisualInterface_Figure_strategy)
def test_visualinterface_figure_onDoubleClick_setter(instance):
    original = instance.onDoubleClick
    instance.onDoubleClick = original
    assert instance.onDoubleClick == original



@given(instance=VisualInterface_Figure_strategy)
def test_visualinterface_figure_onClick_setter(instance):
    original = instance.onClick
    instance.onClick = original
    assert instance.onClick == original



@given(instance=VisualInterface_Figure_strategy)
def test_visualinterface_figure_toolTip_setter(instance):
    original = instance.toolTip
    instance.toolTip = original
    assert instance.toolTip == original



@given(instance=VisualInterface_Figure_strategy)
def test_visualinterface_figure_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=VisualInterface_Figure_strategy)
def test_visualinterface_figure_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=VisualInterface_Figure_strategy)
def test_visualinterface_figure_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original



@given(instance=VisualInterface_Figure_strategy)
def test_visualinterface_figure_opaque_setter(instance):
    original = instance.opaque
    instance.opaque = original
    assert instance.opaque == original



@given(instance=VisualInterface_Figure_strategy)
def test_visualinterface_figure_foregroundColor_setter(instance):
    original = instance.foregroundColor
    instance.foregroundColor = original
    assert instance.foregroundColor == original

@given(instance=VisualInterface_SymbolReference_strategy)
@settings(max_examples=50)
def test_visualinterface_symbolreference_instantiation(instance):
    assert isinstance(instance, VisualInterface_SymbolReference)



@given(instance=VisualInterface_SymbolReference_strategy)
def test_visualinterface_symbolreference_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original



@given(instance=VisualInterface_SymbolReference_strategy)
def test_visualinterface_symbolreference_onCreateProperties_setter(instance):
    original = instance.onCreateProperties
    instance.onCreateProperties = original
    assert instance.onCreateProperties == original



@given(instance=VisualInterface_SymbolReference_strategy)
def test_visualinterface_symbolreference_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=VisualInterface_Container_strategy)
@settings(max_examples=50)
def test_visualinterface_container_instantiation(instance):
    assert isinstance(instance, VisualInterface_Container)

@given(instance=VisualInterface_Connection_strategy)
@settings(max_examples=50)
def test_visualinterface_connection_instantiation(instance):
    assert isinstance(instance, VisualInterface_Connection)

@given(instance=VisualInterface_Dimension_strategy)
@settings(max_examples=50)
def test_visualinterface_dimension_instantiation(instance):
    assert isinstance(instance, VisualInterface_Dimension)



@given(instance=VisualInterface_Dimension_strategy)
def test_visualinterface_dimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=VisualInterface_Dimension_strategy)
def test_visualinterface_dimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=VisualInterface_Cursor_strategy)
@settings(max_examples=50)
def test_visualinterface_cursor_instantiation(instance):
    assert isinstance(instance, VisualInterface_Cursor)

@given(instance=VisualInterface_StringToStringMap_strategy)
@settings(max_examples=50)
def test_visualinterface_stringtostringmap_instantiation(instance):
    assert isinstance(instance, VisualInterface_StringToStringMap)



@given(instance=VisualInterface_StringToStringMap_strategy)
def test_visualinterface_stringtostringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=VisualInterface_StringToStringMap_strategy)
def test_visualinterface_stringtostringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=VisualInterface_Primitive_strategy)
@settings(max_examples=50)
def test_visualinterface_primitive_instantiation(instance):
    assert isinstance(instance, VisualInterface_Primitive)



@given(instance=VisualInterface_Primitive_strategy)
def test_visualinterface_primitive_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=VisualInterface_Symbol_strategy)
@settings(max_examples=50)
def test_visualinterface_symbol_instantiation(instance):
    assert isinstance(instance, VisualInterface_Symbol)



@given(instance=VisualInterface_Symbol_strategy)
def test_visualinterface_symbol_scriptModules_setter(instance):
    original = instance.scriptModules
    instance.scriptModules = original
    assert instance.scriptModules == original



@given(instance=VisualInterface_Symbol_strategy)
def test_visualinterface_symbol_onInit_setter(instance):
    original = instance.onInit
    instance.onInit = original
    assert instance.onInit == original



@given(instance=VisualInterface_Symbol_strategy)
def test_visualinterface_symbol_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=VisualInterface_Symbol_strategy)
def test_visualinterface_symbol_onUpdate_setter(instance):
    original = instance.onUpdate
    instance.onUpdate = original
    assert instance.onUpdate == original



@given(instance=VisualInterface_Symbol_strategy)
def test_visualinterface_symbol_onDispose_setter(instance):
    original = instance.onDispose
    instance.onDispose = original
    assert instance.onDispose == original

@given(instance=VisualInterface_Text_strategy)
@settings(max_examples=50)
def test_visualinterface_text_instantiation(instance):
    assert isinstance(instance, VisualInterface_Text)



@given(instance=VisualInterface_Text_strategy)
def test_visualinterface_text_textPlacement_setter(instance):
    original = instance.textPlacement
    instance.textPlacement = original
    assert instance.textPlacement == original



@given(instance=VisualInterface_Text_strategy)
def test_visualinterface_text_iconAlignment_setter(instance):
    original = instance.iconAlignment
    instance.iconAlignment = original
    assert instance.iconAlignment == original



@given(instance=VisualInterface_Text_strategy)
def test_visualinterface_text_fontItalic_setter(instance):
    original = instance.fontItalic
    instance.fontItalic = original
    assert instance.fontItalic == original



@given(instance=VisualInterface_Text_strategy)
def test_visualinterface_text_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original



@given(instance=VisualInterface_Text_strategy)
def test_visualinterface_text_textAlignment_setter(instance):
    original = instance.textAlignment
    instance.textAlignment = original
    assert instance.textAlignment == original



@given(instance=VisualInterface_Text_strategy)
def test_visualinterface_text_labelAlignment_setter(instance):
    original = instance.labelAlignment
    instance.labelAlignment = original
    assert instance.labelAlignment == original



@given(instance=VisualInterface_Text_strategy)
def test_visualinterface_text_fontSize_setter(instance):
    original = instance.fontSize
    instance.fontSize = original
    assert instance.fontSize == original



@given(instance=VisualInterface_Text_strategy)
def test_visualinterface_text_fontBold_setter(instance):
    original = instance.fontBold
    instance.fontBold = original
    assert instance.fontBold == original



@given(instance=VisualInterface_Text_strategy)
def test_visualinterface_text_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=VisualInterface_Rectangle_strategy)
@settings(max_examples=50)
def test_visualinterface_rectangle_instantiation(instance):
    assert isinstance(instance, VisualInterface_Rectangle)

@given(instance=VisualInterface_Line_strategy)
@settings(max_examples=50)
def test_visualinterface_line_instantiation(instance):
    assert isinstance(instance, VisualInterface_Line)

@given(instance=VisualInterface_Arc_strategy)
@settings(max_examples=50)
def test_visualinterface_arc_instantiation(instance):
    assert isinstance(instance, VisualInterface_Arc)



@given(instance=VisualInterface_Arc_strategy)
def test_visualinterface_arc_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=VisualInterface_Arc_strategy)
def test_visualinterface_arc_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=VisualInterface_Ellipse_strategy)
@settings(max_examples=50)
def test_visualinterface_ellipse_instantiation(instance):
    assert isinstance(instance, VisualInterface_Ellipse)
