import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Cursor,
    model::SystemCursor,
    Container,
    model::StackContainer,
    model::BorderContainer,
    model::GridContainer,
    model::XYContainer,
    model::Position,
    Child,
    model::BorderChild,
    model::GridChild,
    model::XYChild,
    model::Child,
    model::Connection,
    model::Dimension,
    model::Cursor,
    model::StringToStringMap,
    model::Primitive,
    model::Symbol,
    Shape,
    model::Line,
    model::Arc,
    model::Ellipse,
    model::Rectangle,
    Figure,
    model::Text,
    model::FigureContainer,
    model::Image,
    model::Shape,
    Primitive,
    model::Figure,
    model::SymbolReference,
    model::Container,
    Orientation,
    SystemCursorType,
    GridAlignment,
    Alignment,
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



def test_model::systemcursor_is_not_abstract():
    assert not inspect.isabstract(model::SystemCursor)


def test_model::systemcursor_constructor_exists():
    assert callable(model::SystemCursor.__init__)


def test_model::systemcursor_constructor_args():
    sig = inspect.signature(model::SystemCursor.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model::systemcursor_has_type():
    assert hasattr(model::SystemCursor, "type")
    descriptor = None
    for klass in model::SystemCursor.__mro__:
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



def test_model::stackcontainer_is_not_abstract():
    assert not inspect.isabstract(model::StackContainer)


def test_model::stackcontainer_constructor_exists():
    assert callable(model::StackContainer.__init__)


def test_model::stackcontainer_constructor_args():
    sig = inspect.signature(model::StackContainer.__init__)
    params = list(sig.parameters.keys())



def test_model::bordercontainer_is_not_abstract():
    assert not inspect.isabstract(model::BorderContainer)


def test_model::bordercontainer_constructor_exists():
    assert callable(model::BorderContainer.__init__)


def test_model::bordercontainer_constructor_args():
    sig = inspect.signature(model::BorderContainer.__init__)
    params = list(sig.parameters.keys())
    assert "horizontalSpacing" in params, "Missing parameter 'horizontalSpacing'"
    assert "verticalSpacing" in params, "Missing parameter 'verticalSpacing'"

def test_model::bordercontainer_has_horizontalSpacing():
    assert hasattr(model::BorderContainer, "horizontalSpacing")
    descriptor = None
    for klass in model::BorderContainer.__mro__:
        if "horizontalSpacing" in klass.__dict__:
            descriptor = klass.__dict__["horizontalSpacing"]
            break
    assert isinstance(descriptor, property)

def test_model::bordercontainer_has_verticalSpacing():
    assert hasattr(model::BorderContainer, "verticalSpacing")
    descriptor = None
    for klass in model::BorderContainer.__mro__:
        if "verticalSpacing" in klass.__dict__:
            descriptor = klass.__dict__["verticalSpacing"]
            break
    assert isinstance(descriptor, property)



def test_model::gridcontainer_is_not_abstract():
    assert not inspect.isabstract(model::GridContainer)


def test_model::gridcontainer_constructor_exists():
    assert callable(model::GridContainer.__init__)


def test_model::gridcontainer_constructor_args():
    sig = inspect.signature(model::GridContainer.__init__)
    params = list(sig.parameters.keys())
    assert "marginWidth" in params, "Missing parameter 'marginWidth'"
    assert "marginHeight" in params, "Missing parameter 'marginHeight'"
    assert "horizontalSpacing" in params, "Missing parameter 'horizontalSpacing'"
    assert "equalWidth" in params, "Missing parameter 'equalWidth'"
    assert "verticalSpacing" in params, "Missing parameter 'verticalSpacing'"
    assert "columns" in params, "Missing parameter 'columns'"

def test_model::gridcontainer_has_marginWidth():
    assert hasattr(model::GridContainer, "marginWidth")
    descriptor = None
    for klass in model::GridContainer.__mro__:
        if "marginWidth" in klass.__dict__:
            descriptor = klass.__dict__["marginWidth"]
            break
    assert isinstance(descriptor, property)

def test_model::gridcontainer_has_marginHeight():
    assert hasattr(model::GridContainer, "marginHeight")
    descriptor = None
    for klass in model::GridContainer.__mro__:
        if "marginHeight" in klass.__dict__:
            descriptor = klass.__dict__["marginHeight"]
            break
    assert isinstance(descriptor, property)

def test_model::gridcontainer_has_horizontalSpacing():
    assert hasattr(model::GridContainer, "horizontalSpacing")
    descriptor = None
    for klass in model::GridContainer.__mro__:
        if "horizontalSpacing" in klass.__dict__:
            descriptor = klass.__dict__["horizontalSpacing"]
            break
    assert isinstance(descriptor, property)

def test_model::gridcontainer_has_equalWidth():
    assert hasattr(model::GridContainer, "equalWidth")
    descriptor = None
    for klass in model::GridContainer.__mro__:
        if "equalWidth" in klass.__dict__:
            descriptor = klass.__dict__["equalWidth"]
            break
    assert isinstance(descriptor, property)

def test_model::gridcontainer_has_verticalSpacing():
    assert hasattr(model::GridContainer, "verticalSpacing")
    descriptor = None
    for klass in model::GridContainer.__mro__:
        if "verticalSpacing" in klass.__dict__:
            descriptor = klass.__dict__["verticalSpacing"]
            break
    assert isinstance(descriptor, property)

def test_model::gridcontainer_has_columns():
    assert hasattr(model::GridContainer, "columns")
    descriptor = None
    for klass in model::GridContainer.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)



def test_model::xycontainer_is_not_abstract():
    assert not inspect.isabstract(model::XYContainer)


def test_model::xycontainer_constructor_exists():
    assert callable(model::XYContainer.__init__)


def test_model::xycontainer_constructor_args():
    sig = inspect.signature(model::XYContainer.__init__)
    params = list(sig.parameters.keys())



def test_model::position_is_not_abstract():
    assert not inspect.isabstract(model::Position)


def test_model::position_constructor_exists():
    assert callable(model::Position.__init__)


def test_model::position_constructor_args():
    sig = inspect.signature(model::Position.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_model::position_has_x():
    assert hasattr(model::Position, "x")
    descriptor = None
    for klass in model::Position.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_model::position_has_y():
    assert hasattr(model::Position, "y")
    descriptor = None
    for klass in model::Position.__mro__:
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



def test_model::borderchild_is_not_abstract():
    assert not inspect.isabstract(model::BorderChild)


def test_model::borderchild_constructor_exists():
    assert callable(model::BorderChild.__init__)


def test_model::borderchild_constructor_args():
    sig = inspect.signature(model::BorderChild.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_model::borderchild_has_alignment():
    assert hasattr(model::BorderChild, "alignment")
    descriptor = None
    for klass in model::BorderChild.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_model::gridchild_is_not_abstract():
    assert not inspect.isabstract(model::GridChild)


def test_model::gridchild_constructor_exists():
    assert callable(model::GridChild.__init__)


def test_model::gridchild_constructor_args():
    sig = inspect.signature(model::GridChild.__init__)
    params = list(sig.parameters.keys())
    assert "grabVerticalSpace" in params, "Missing parameter 'grabVerticalSpace'"
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"
    assert "spanRows" in params, "Missing parameter 'spanRows'"
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"
    assert "grabHorizontalSpace" in params, "Missing parameter 'grabHorizontalSpace'"
    assert "widthHint" in params, "Missing parameter 'widthHint'"
    assert "heightHint" in params, "Missing parameter 'heightHint'"
    assert "spanCols" in params, "Missing parameter 'spanCols'"

def test_model::gridchild_has_grabVerticalSpace():
    assert hasattr(model::GridChild, "grabVerticalSpace")
    descriptor = None
    for klass in model::GridChild.__mro__:
        if "grabVerticalSpace" in klass.__dict__:
            descriptor = klass.__dict__["grabVerticalSpace"]
            break
    assert isinstance(descriptor, property)

def test_model::gridchild_has_horizontalAlignment():
    assert hasattr(model::GridChild, "horizontalAlignment")
    descriptor = None
    for klass in model::GridChild.__mro__:
        if "horizontalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["horizontalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_model::gridchild_has_spanRows():
    assert hasattr(model::GridChild, "spanRows")
    descriptor = None
    for klass in model::GridChild.__mro__:
        if "spanRows" in klass.__dict__:
            descriptor = klass.__dict__["spanRows"]
            break
    assert isinstance(descriptor, property)

def test_model::gridchild_has_verticalAlignment():
    assert hasattr(model::GridChild, "verticalAlignment")
    descriptor = None
    for klass in model::GridChild.__mro__:
        if "verticalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_model::gridchild_has_grabHorizontalSpace():
    assert hasattr(model::GridChild, "grabHorizontalSpace")
    descriptor = None
    for klass in model::GridChild.__mro__:
        if "grabHorizontalSpace" in klass.__dict__:
            descriptor = klass.__dict__["grabHorizontalSpace"]
            break
    assert isinstance(descriptor, property)

def test_model::gridchild_has_widthHint():
    assert hasattr(model::GridChild, "widthHint")
    descriptor = None
    for klass in model::GridChild.__mro__:
        if "widthHint" in klass.__dict__:
            descriptor = klass.__dict__["widthHint"]
            break
    assert isinstance(descriptor, property)

def test_model::gridchild_has_heightHint():
    assert hasattr(model::GridChild, "heightHint")
    descriptor = None
    for klass in model::GridChild.__mro__:
        if "heightHint" in klass.__dict__:
            descriptor = klass.__dict__["heightHint"]
            break
    assert isinstance(descriptor, property)

def test_model::gridchild_has_spanCols():
    assert hasattr(model::GridChild, "spanCols")
    descriptor = None
    for klass in model::GridChild.__mro__:
        if "spanCols" in klass.__dict__:
            descriptor = klass.__dict__["spanCols"]
            break
    assert isinstance(descriptor, property)



def test_model::xychild_is_not_abstract():
    assert not inspect.isabstract(model::XYChild)


def test_model::xychild_constructor_exists():
    assert callable(model::XYChild.__init__)


def test_model::xychild_constructor_args():
    sig = inspect.signature(model::XYChild.__init__)
    params = list(sig.parameters.keys())



def test_model::child_is_not_abstract():
    assert not inspect.isabstract(model::Child)


def test_model::child_constructor_exists():
    assert callable(model::Child.__init__)


def test_model::child_constructor_args():
    sig = inspect.signature(model::Child.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::child_has_name():
    assert hasattr(model::Child, "name")
    descriptor = None
    for klass in model::Child.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::connection_is_not_abstract():
    assert not inspect.isabstract(model::Connection)


def test_model::connection_constructor_exists():
    assert callable(model::Connection.__init__)


def test_model::connection_constructor_args():
    sig = inspect.signature(model::Connection.__init__)
    params = list(sig.parameters.keys())



def test_model::dimension_is_not_abstract():
    assert not inspect.isabstract(model::Dimension)


def test_model::dimension_constructor_exists():
    assert callable(model::Dimension.__init__)


def test_model::dimension_constructor_args():
    sig = inspect.signature(model::Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_model::dimension_has_width():
    assert hasattr(model::Dimension, "width")
    descriptor = None
    for klass in model::Dimension.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_model::dimension_has_height():
    assert hasattr(model::Dimension, "height")
    descriptor = None
    for klass in model::Dimension.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_model::cursor_is_not_abstract():
    assert not inspect.isabstract(model::Cursor)


def test_model::cursor_constructor_exists():
    assert callable(model::Cursor.__init__)


def test_model::cursor_constructor_args():
    sig = inspect.signature(model::Cursor.__init__)
    params = list(sig.parameters.keys())



def test_model::stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(model::StringToStringMap)


def test_model::stringtostringmap_constructor_exists():
    assert callable(model::StringToStringMap.__init__)


def test_model::stringtostringmap_constructor_args():
    sig = inspect.signature(model::StringToStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_model::stringtostringmap_has_key():
    assert hasattr(model::StringToStringMap, "key")
    descriptor = None
    for klass in model::StringToStringMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_model::stringtostringmap_has_value():
    assert hasattr(model::StringToStringMap, "value")
    descriptor = None
    for klass in model::StringToStringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model::primitive_is_not_abstract():
    assert not inspect.isabstract(model::Primitive)


def test_model::primitive_constructor_exists():
    assert callable(model::Primitive.__init__)


def test_model::primitive_constructor_args():
    sig = inspect.signature(model::Primitive.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::primitive_has_name():
    assert hasattr(model::Primitive, "name")
    descriptor = None
    for klass in model::Primitive.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::symbol_is_not_abstract():
    assert not inspect.isabstract(model::Symbol)


def test_model::symbol_constructor_exists():
    assert callable(model::Symbol.__init__)


def test_model::symbol_constructor_args():
    sig = inspect.signature(model::Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "onDispose" in params, "Missing parameter 'onDispose'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "scriptModules" in params, "Missing parameter 'scriptModules'"
    assert "onInit" in params, "Missing parameter 'onInit'"
    assert "onUpdate" in params, "Missing parameter 'onUpdate'"

def test_model::symbol_has_onDispose():
    assert hasattr(model::Symbol, "onDispose")
    descriptor = None
    for klass in model::Symbol.__mro__:
        if "onDispose" in klass.__dict__:
            descriptor = klass.__dict__["onDispose"]
            break
    assert isinstance(descriptor, property)

def test_model::symbol_has_backgroundColor():
    assert hasattr(model::Symbol, "backgroundColor")
    descriptor = None
    for klass in model::Symbol.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_model::symbol_has_scriptModules():
    assert hasattr(model::Symbol, "scriptModules")
    descriptor = None
    for klass in model::Symbol.__mro__:
        if "scriptModules" in klass.__dict__:
            descriptor = klass.__dict__["scriptModules"]
            break
    assert isinstance(descriptor, property)

def test_model::symbol_has_onInit():
    assert hasattr(model::Symbol, "onInit")
    descriptor = None
    for klass in model::Symbol.__mro__:
        if "onInit" in klass.__dict__:
            descriptor = klass.__dict__["onInit"]
            break
    assert isinstance(descriptor, property)

def test_model::symbol_has_onUpdate():
    assert hasattr(model::Symbol, "onUpdate")
    descriptor = None
    for klass in model::Symbol.__mro__:
        if "onUpdate" in klass.__dict__:
            descriptor = klass.__dict__["onUpdate"]
            break
    assert isinstance(descriptor, property)



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_model::line_is_not_abstract():
    assert not inspect.isabstract(model::Line)


def test_model::line_constructor_exists():
    assert callable(model::Line.__init__)


def test_model::line_constructor_args():
    sig = inspect.signature(model::Line.__init__)
    params = list(sig.parameters.keys())



def test_model::arc_is_not_abstract():
    assert not inspect.isabstract(model::Arc)


def test_model::arc_constructor_exists():
    assert callable(model::Arc.__init__)


def test_model::arc_constructor_args():
    sig = inspect.signature(model::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "length" in params, "Missing parameter 'length'"

def test_model::arc_has_start():
    assert hasattr(model::Arc, "start")
    descriptor = None
    for klass in model::Arc.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_model::arc_has_length():
    assert hasattr(model::Arc, "length")
    descriptor = None
    for klass in model::Arc.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_model::ellipse_is_not_abstract():
    assert not inspect.isabstract(model::Ellipse)


def test_model::ellipse_constructor_exists():
    assert callable(model::Ellipse.__init__)


def test_model::ellipse_constructor_args():
    sig = inspect.signature(model::Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_model::rectangle_is_not_abstract():
    assert not inspect.isabstract(model::Rectangle)


def test_model::rectangle_constructor_exists():
    assert callable(model::Rectangle.__init__)


def test_model::rectangle_constructor_args():
    sig = inspect.signature(model::Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_model::text_is_not_abstract():
    assert not inspect.isabstract(model::Text)


def test_model::text_constructor_exists():
    assert callable(model::Text.__init__)


def test_model::text_constructor_args():
    sig = inspect.signature(model::Text.__init__)
    params = list(sig.parameters.keys())
    assert "textPlacement" in params, "Missing parameter 'textPlacement'"
    assert "text" in params, "Missing parameter 'text'"
    assert "textAlignment" in params, "Missing parameter 'textAlignment'"
    assert "fontItalic" in params, "Missing parameter 'fontItalic'"
    assert "fontSize" in params, "Missing parameter 'fontSize'"
    assert "fontName" in params, "Missing parameter 'fontName'"
    assert "iconAlignment" in params, "Missing parameter 'iconAlignment'"
    assert "fontBold" in params, "Missing parameter 'fontBold'"
    assert "labelAlignment" in params, "Missing parameter 'labelAlignment'"

def test_model::text_has_textPlacement():
    assert hasattr(model::Text, "textPlacement")
    descriptor = None
    for klass in model::Text.__mro__:
        if "textPlacement" in klass.__dict__:
            descriptor = klass.__dict__["textPlacement"]
            break
    assert isinstance(descriptor, property)

def test_model::text_has_text():
    assert hasattr(model::Text, "text")
    descriptor = None
    for klass in model::Text.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_model::text_has_textAlignment():
    assert hasattr(model::Text, "textAlignment")
    descriptor = None
    for klass in model::Text.__mro__:
        if "textAlignment" in klass.__dict__:
            descriptor = klass.__dict__["textAlignment"]
            break
    assert isinstance(descriptor, property)

def test_model::text_has_fontItalic():
    assert hasattr(model::Text, "fontItalic")
    descriptor = None
    for klass in model::Text.__mro__:
        if "fontItalic" in klass.__dict__:
            descriptor = klass.__dict__["fontItalic"]
            break
    assert isinstance(descriptor, property)

def test_model::text_has_fontSize():
    assert hasattr(model::Text, "fontSize")
    descriptor = None
    for klass in model::Text.__mro__:
        if "fontSize" in klass.__dict__:
            descriptor = klass.__dict__["fontSize"]
            break
    assert isinstance(descriptor, property)

def test_model::text_has_fontName():
    assert hasattr(model::Text, "fontName")
    descriptor = None
    for klass in model::Text.__mro__:
        if "fontName" in klass.__dict__:
            descriptor = klass.__dict__["fontName"]
            break
    assert isinstance(descriptor, property)

def test_model::text_has_iconAlignment():
    assert hasattr(model::Text, "iconAlignment")
    descriptor = None
    for klass in model::Text.__mro__:
        if "iconAlignment" in klass.__dict__:
            descriptor = klass.__dict__["iconAlignment"]
            break
    assert isinstance(descriptor, property)

def test_model::text_has_fontBold():
    assert hasattr(model::Text, "fontBold")
    descriptor = None
    for klass in model::Text.__mro__:
        if "fontBold" in klass.__dict__:
            descriptor = klass.__dict__["fontBold"]
            break
    assert isinstance(descriptor, property)

def test_model::text_has_labelAlignment():
    assert hasattr(model::Text, "labelAlignment")
    descriptor = None
    for klass in model::Text.__mro__:
        if "labelAlignment" in klass.__dict__:
            descriptor = klass.__dict__["labelAlignment"]
            break
    assert isinstance(descriptor, property)



def test_model::figurecontainer_is_not_abstract():
    assert not inspect.isabstract(model::FigureContainer)


def test_model::figurecontainer_constructor_exists():
    assert callable(model::FigureContainer.__init__)


def test_model::figurecontainer_constructor_args():
    sig = inspect.signature(model::FigureContainer.__init__)
    params = list(sig.parameters.keys())



def test_model::image_is_not_abstract():
    assert not inspect.isabstract(model::Image)


def test_model::image_constructor_exists():
    assert callable(model::Image.__init__)


def test_model::image_constructor_args():
    sig = inspect.signature(model::Image.__init__)
    params = list(sig.parameters.keys())
    assert "imageAlignment" in params, "Missing parameter 'imageAlignment'"
    assert "uri" in params, "Missing parameter 'uri'"

def test_model::image_has_imageAlignment():
    assert hasattr(model::Image, "imageAlignment")
    descriptor = None
    for klass in model::Image.__mro__:
        if "imageAlignment" in klass.__dict__:
            descriptor = klass.__dict__["imageAlignment"]
            break
    assert isinstance(descriptor, property)

def test_model::image_has_uri():
    assert hasattr(model::Image, "uri")
    descriptor = None
    for klass in model::Image.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_model::shape_is_not_abstract():
    assert not inspect.isabstract(model::Shape)


def test_model::shape_constructor_exists():
    assert callable(model::Shape.__init__)


def test_model::shape_constructor_args():
    sig = inspect.signature(model::Shape.__init__)
    params = list(sig.parameters.keys())
    assert "fill" in params, "Missing parameter 'fill'"
    assert "alpha" in params, "Missing parameter 'alpha'"
    assert "antialias" in params, "Missing parameter 'antialias'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "outline" in params, "Missing parameter 'outline'"

def test_model::shape_has_fill():
    assert hasattr(model::Shape, "fill")
    descriptor = None
    for klass in model::Shape.__mro__:
        if "fill" in klass.__dict__:
            descriptor = klass.__dict__["fill"]
            break
    assert isinstance(descriptor, property)

def test_model::shape_has_alpha():
    assert hasattr(model::Shape, "alpha")
    descriptor = None
    for klass in model::Shape.__mro__:
        if "alpha" in klass.__dict__:
            descriptor = klass.__dict__["alpha"]
            break
    assert isinstance(descriptor, property)

def test_model::shape_has_antialias():
    assert hasattr(model::Shape, "antialias")
    descriptor = None
    for klass in model::Shape.__mro__:
        if "antialias" in klass.__dict__:
            descriptor = klass.__dict__["antialias"]
            break
    assert isinstance(descriptor, property)

def test_model::shape_has_lineWidth():
    assert hasattr(model::Shape, "lineWidth")
    descriptor = None
    for klass in model::Shape.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_model::shape_has_outline():
    assert hasattr(model::Shape, "outline")
    descriptor = None
    for klass in model::Shape.__mro__:
        if "outline" in klass.__dict__:
            descriptor = klass.__dict__["outline"]
            break
    assert isinstance(descriptor, property)



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_model::figure_is_not_abstract():
    assert not inspect.isabstract(model::Figure)


def test_model::figure_constructor_exists():
    assert callable(model::Figure.__init__)


def test_model::figure_constructor_args():
    sig = inspect.signature(model::Figure.__init__)
    params = list(sig.parameters.keys())
    assert "onClick" in params, "Missing parameter 'onClick'"
    assert "onDoubleClick" in params, "Missing parameter 'onDoubleClick'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "opaque" in params, "Missing parameter 'opaque'"
    assert "foregroundColor" in params, "Missing parameter 'foregroundColor'"
    assert "border" in params, "Missing parameter 'border'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "toolTip" in params, "Missing parameter 'toolTip'"
    assert "onMouseMove" in params, "Missing parameter 'onMouseMove'"
    assert "onMouseHover" in params, "Missing parameter 'onMouseHover'"
    assert "onMouseDrag" in params, "Missing parameter 'onMouseDrag'"
    assert "onMouseIn" in params, "Missing parameter 'onMouseIn'"
    assert "onMouseOut" in params, "Missing parameter 'onMouseOut'"

def test_model::figure_has_onClick():
    assert hasattr(model::Figure, "onClick")
    descriptor = None
    for klass in model::Figure.__mro__:
        if "onClick" in klass.__dict__:
            descriptor = klass.__dict__["onClick"]
            break
    assert isinstance(descriptor, property)

def test_model::figure_has_onDoubleClick():
    assert hasattr(model::Figure, "onDoubleClick")
    descriptor = None
    for klass in model::Figure.__mro__:
        if "onDoubleClick" in klass.__dict__:
            descriptor = klass.__dict__["onDoubleClick"]
            break
    assert isinstance(descriptor, property)

def test_model::figure_has_backgroundColor():
    assert hasattr(model::Figure, "backgroundColor")
    descriptor = None
    for klass in model::Figure.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_model::figure_has_opaque():
    assert hasattr(model::Figure, "opaque")
    descriptor = None
    for klass in model::Figure.__mro__:
        if "opaque" in klass.__dict__:
            descriptor = klass.__dict__["opaque"]
            break
    assert isinstance(descriptor, property)

def test_model::figure_has_foregroundColor():
    assert hasattr(model::Figure, "foregroundColor")
    descriptor = None
    for klass in model::Figure.__mro__:
        if "foregroundColor" in klass.__dict__:
            descriptor = klass.__dict__["foregroundColor"]
            break
    assert isinstance(descriptor, property)

def test_model::figure_has_border():
    assert hasattr(model::Figure, "border")
    descriptor = None
    for klass in model::Figure.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)

def test_model::figure_has_visible():
    assert hasattr(model::Figure, "visible")
    descriptor = None
    for klass in model::Figure.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_model::figure_has_toolTip():
    assert hasattr(model::Figure, "toolTip")
    descriptor = None
    for klass in model::Figure.__mro__:
        if "toolTip" in klass.__dict__:
            descriptor = klass.__dict__["toolTip"]
            break
    assert isinstance(descriptor, property)

def test_model::figure_has_onMouseMove():
    assert hasattr(model::Figure, "onMouseMove")
    descriptor = None
    for klass in model::Figure.__mro__:
        if "onMouseMove" in klass.__dict__:
            descriptor = klass.__dict__["onMouseMove"]
            break
    assert isinstance(descriptor, property)

def test_model::figure_has_onMouseHover():
    assert hasattr(model::Figure, "onMouseHover")
    descriptor = None
    for klass in model::Figure.__mro__:
        if "onMouseHover" in klass.__dict__:
            descriptor = klass.__dict__["onMouseHover"]
            break
    assert isinstance(descriptor, property)

def test_model::figure_has_onMouseDrag():
    assert hasattr(model::Figure, "onMouseDrag")
    descriptor = None
    for klass in model::Figure.__mro__:
        if "onMouseDrag" in klass.__dict__:
            descriptor = klass.__dict__["onMouseDrag"]
            break
    assert isinstance(descriptor, property)

def test_model::figure_has_onMouseIn():
    assert hasattr(model::Figure, "onMouseIn")
    descriptor = None
    for klass in model::Figure.__mro__:
        if "onMouseIn" in klass.__dict__:
            descriptor = klass.__dict__["onMouseIn"]
            break
    assert isinstance(descriptor, property)

def test_model::figure_has_onMouseOut():
    assert hasattr(model::Figure, "onMouseOut")
    descriptor = None
    for klass in model::Figure.__mro__:
        if "onMouseOut" in klass.__dict__:
            descriptor = klass.__dict__["onMouseOut"]
            break
    assert isinstance(descriptor, property)



def test_model::symbolreference_is_not_abstract():
    assert not inspect.isabstract(model::SymbolReference)


def test_model::symbolreference_constructor_exists():
    assert callable(model::SymbolReference.__init__)


def test_model::symbolreference_constructor_args():
    sig = inspect.signature(model::SymbolReference.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"
    assert "zoom" in params, "Missing parameter 'zoom'"
    assert "onCreateProperties" in params, "Missing parameter 'onCreateProperties'"

def test_model::symbolreference_has_uri():
    assert hasattr(model::SymbolReference, "uri")
    descriptor = None
    for klass in model::SymbolReference.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)

def test_model::symbolreference_has_zoom():
    assert hasattr(model::SymbolReference, "zoom")
    descriptor = None
    for klass in model::SymbolReference.__mro__:
        if "zoom" in klass.__dict__:
            descriptor = klass.__dict__["zoom"]
            break
    assert isinstance(descriptor, property)

def test_model::symbolreference_has_onCreateProperties():
    assert hasattr(model::SymbolReference, "onCreateProperties")
    descriptor = None
    for klass in model::SymbolReference.__mro__:
        if "onCreateProperties" in klass.__dict__:
            descriptor = klass.__dict__["onCreateProperties"]
            break
    assert isinstance(descriptor, property)



def test_model::container_is_not_abstract():
    assert not inspect.isabstract(model::Container)


def test_model::container_constructor_exists():
    assert callable(model::Container.__init__)


def test_model::container_constructor_args():
    sig = inspect.signature(model::Container.__init__)
    params = list(sig.parameters.keys())

def test_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "WEST",
        "EAST",
        "NORTH",
        "SOUTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"

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

def test_gridalignment_exists():
    # Check that the Enumeration exists
    assert GridAlignment is not None

def test_gridalignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GridAlignment]
    expected_literals = [
        "CENTER",
        "BEGINNING",
        "FILL",
        "END",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GridAlignment"

def test_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "BOTTOM",
        "TOP",
        "LEFT",
        "CENTER",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Alignment"


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
model::SystemCursor_strategy = st.builds(
    model::SystemCursor,
    type=
        safe_text
)
Container_strategy = st.builds(
    Container,
)
model::StackContainer_strategy = st.builds(
    model::StackContainer,
)
model::BorderContainer_strategy = st.builds(
    model::BorderContainer,
    horizontalSpacing=
        st.integers(),
    verticalSpacing=
        st.integers()
)
model::GridContainer_strategy = st.builds(
    model::GridContainer,
    marginWidth=
        st.integers(),
    marginHeight=
        st.integers(),
    horizontalSpacing=
        st.integers(),
    equalWidth=
        st.booleans(),
    verticalSpacing=
        st.integers(),
    columns=
        st.integers()
)
model::XYContainer_strategy = st.builds(
    model::XYContainer,
)
model::Position_strategy = st.builds(
    model::Position,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Child_strategy = st.builds(
    Child,
)
model::BorderChild_strategy = st.builds(
    model::BorderChild,
    alignment=
        safe_text
)
model::GridChild_strategy = st.builds(
    model::GridChild,
    grabVerticalSpace=
        st.booleans(),
    horizontalAlignment=
        safe_text,
    spanRows=
        safe_text,
    verticalAlignment=
        safe_text,
    grabHorizontalSpace=
        st.booleans(),
    widthHint=
        safe_text,
    heightHint=
        safe_text,
    spanCols=
        st.integers()
)
model::XYChild_strategy = st.builds(
    model::XYChild,
)
model::Child_strategy = st.builds(
    model::Child,
    name=
        safe_text
)
model::Connection_strategy = st.builds(
    model::Connection,
)
model::Dimension_strategy = st.builds(
    model::Dimension,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model::Cursor_strategy = st.builds(
    model::Cursor,
)
model::StringToStringMap_strategy = st.builds(
    model::StringToStringMap,
    key=
        safe_text,
    value=
        safe_text
)
model::Primitive_strategy = st.builds(
    model::Primitive,
    name=
        safe_text
)
model::Symbol_strategy = st.builds(
    model::Symbol,
    onDispose=
        safe_text,
    backgroundColor=
        safe_text,
    scriptModules=
        safe_text,
    onInit=
        safe_text,
    onUpdate=
        safe_text
)
Shape_strategy = st.builds(
    Shape,
)
model::Line_strategy = st.builds(
    model::Line,
)
model::Arc_strategy = st.builds(
    model::Arc,
    start=
        st.integers(),
    length=
        st.integers()
)
model::Ellipse_strategy = st.builds(
    model::Ellipse,
)
model::Rectangle_strategy = st.builds(
    model::Rectangle,
)
Figure_strategy = st.builds(
    Figure,
)
model::Text_strategy = st.builds(
    model::Text,
    textPlacement=
        safe_text,
    text=
        safe_text,
    textAlignment=
        safe_text,
    fontItalic=
        st.booleans(),
    fontSize=
        st.integers(),
    fontName=
        safe_text,
    iconAlignment=
        safe_text,
    fontBold=
        st.booleans(),
    labelAlignment=
        safe_text
)
model::FigureContainer_strategy = st.builds(
    model::FigureContainer,
)
model::Image_strategy = st.builds(
    model::Image,
    imageAlignment=
        safe_text,
    uri=
        safe_text
)
model::Shape_strategy = st.builds(
    model::Shape,
    fill=
        st.booleans(),
    alpha=
        safe_text,
    antialias=
        safe_text,
    lineWidth=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    outline=
        st.booleans()
)
Primitive_strategy = st.builds(
    Primitive,
)
model::Figure_strategy = st.builds(
    model::Figure,
    onClick=
        safe_text,
    onDoubleClick=
        safe_text,
    backgroundColor=
        safe_text,
    opaque=
        safe_text,
    foregroundColor=
        safe_text,
    border=
        safe_text,
    visible=
        st.booleans(),
    toolTip=
        safe_text,
    onMouseMove=
        safe_text,
    onMouseHover=
        safe_text,
    onMouseDrag=
        safe_text,
    onMouseIn=
        safe_text,
    onMouseOut=
        safe_text
)
model::SymbolReference_strategy = st.builds(
    model::SymbolReference,
    uri=
        safe_text,
    zoom=
        safe_text,
    onCreateProperties=
        safe_text
)
model::Container_strategy = st.builds(
    model::Container,
)

@given(instance=Cursor_strategy)
@settings(max_examples=50)
def test_cursor_instantiation(instance):
    assert isinstance(instance, Cursor)

@given(instance=model::SystemCursor_strategy)
@settings(max_examples=50)
def test_model::systemcursor_instantiation(instance):
    assert isinstance(instance, model::SystemCursor)

@given(instance=model::SystemCursor_strategy)
def test_model::systemcursor_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::SystemCursor_strategy)
def test_model::systemcursor_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Container_strategy)
@settings(max_examples=50)
def test_container_instantiation(instance):
    assert isinstance(instance, Container)

@given(instance=model::StackContainer_strategy)
@settings(max_examples=50)
def test_model::stackcontainer_instantiation(instance):
    assert isinstance(instance, model::StackContainer)

@given(instance=model::BorderContainer_strategy)
@settings(max_examples=50)
def test_model::bordercontainer_instantiation(instance):
    assert isinstance(instance, model::BorderContainer)

@given(instance=model::BorderContainer_strategy)
def test_model::bordercontainer_horizontalSpacing_type(instance):
    assert isinstance(instance.horizontalSpacing, int)


@given(instance=model::BorderContainer_strategy)
def test_model::bordercontainer_horizontalSpacing_setter(instance):
    original = instance.horizontalSpacing
    instance.horizontalSpacing = original
    assert instance.horizontalSpacing == original

@given(instance=model::BorderContainer_strategy)
def test_model::bordercontainer_verticalSpacing_type(instance):
    assert isinstance(instance.verticalSpacing, int)


@given(instance=model::BorderContainer_strategy)
def test_model::bordercontainer_verticalSpacing_setter(instance):
    original = instance.verticalSpacing
    instance.verticalSpacing = original
    assert instance.verticalSpacing == original

@given(instance=model::GridContainer_strategy)
@settings(max_examples=50)
def test_model::gridcontainer_instantiation(instance):
    assert isinstance(instance, model::GridContainer)

@given(instance=model::GridContainer_strategy)
def test_model::gridcontainer_marginWidth_type(instance):
    assert isinstance(instance.marginWidth, int)


@given(instance=model::GridContainer_strategy)
def test_model::gridcontainer_marginWidth_setter(instance):
    original = instance.marginWidth
    instance.marginWidth = original
    assert instance.marginWidth == original

@given(instance=model::GridContainer_strategy)
def test_model::gridcontainer_marginHeight_type(instance):
    assert isinstance(instance.marginHeight, int)


@given(instance=model::GridContainer_strategy)
def test_model::gridcontainer_marginHeight_setter(instance):
    original = instance.marginHeight
    instance.marginHeight = original
    assert instance.marginHeight == original

@given(instance=model::GridContainer_strategy)
def test_model::gridcontainer_horizontalSpacing_type(instance):
    assert isinstance(instance.horizontalSpacing, int)


@given(instance=model::GridContainer_strategy)
def test_model::gridcontainer_horizontalSpacing_setter(instance):
    original = instance.horizontalSpacing
    instance.horizontalSpacing = original
    assert instance.horizontalSpacing == original

@given(instance=model::GridContainer_strategy)
def test_model::gridcontainer_equalWidth_type(instance):
    assert isinstance(instance.equalWidth, bool)


@given(instance=model::GridContainer_strategy)
def test_model::gridcontainer_equalWidth_setter(instance):
    original = instance.equalWidth
    instance.equalWidth = original
    assert instance.equalWidth == original

@given(instance=model::GridContainer_strategy)
def test_model::gridcontainer_verticalSpacing_type(instance):
    assert isinstance(instance.verticalSpacing, int)


@given(instance=model::GridContainer_strategy)
def test_model::gridcontainer_verticalSpacing_setter(instance):
    original = instance.verticalSpacing
    instance.verticalSpacing = original
    assert instance.verticalSpacing == original

@given(instance=model::GridContainer_strategy)
def test_model::gridcontainer_columns_type(instance):
    assert isinstance(instance.columns, int)


@given(instance=model::GridContainer_strategy)
def test_model::gridcontainer_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original

@given(instance=model::XYContainer_strategy)
@settings(max_examples=50)
def test_model::xycontainer_instantiation(instance):
    assert isinstance(instance, model::XYContainer)

@given(instance=model::Position_strategy)
@settings(max_examples=50)
def test_model::position_instantiation(instance):
    assert isinstance(instance, model::Position)

@given(instance=model::Position_strategy)
def test_model::position_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=model::Position_strategy)
def test_model::position_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=model::Position_strategy)
def test_model::position_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=model::Position_strategy)
def test_model::position_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Child_strategy)
@settings(max_examples=50)
def test_child_instantiation(instance):
    assert isinstance(instance, Child)

@given(instance=model::BorderChild_strategy)
@settings(max_examples=50)
def test_model::borderchild_instantiation(instance):
    assert isinstance(instance, model::BorderChild)

@given(instance=model::BorderChild_strategy)
def test_model::borderchild_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=model::BorderChild_strategy)
def test_model::borderchild_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=model::GridChild_strategy)
@settings(max_examples=50)
def test_model::gridchild_instantiation(instance):
    assert isinstance(instance, model::GridChild)

@given(instance=model::GridChild_strategy)
def test_model::gridchild_grabVerticalSpace_type(instance):
    assert isinstance(instance.grabVerticalSpace, bool)


@given(instance=model::GridChild_strategy)
def test_model::gridchild_grabVerticalSpace_setter(instance):
    original = instance.grabVerticalSpace
    instance.grabVerticalSpace = original
    assert instance.grabVerticalSpace == original

@given(instance=model::GridChild_strategy)
def test_model::gridchild_horizontalAlignment_type(instance):
    assert isinstance(instance.horizontalAlignment, str)


@given(instance=model::GridChild_strategy)
def test_model::gridchild_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original

@given(instance=model::GridChild_strategy)
def test_model::gridchild_spanRows_type(instance):
    assert isinstance(instance.spanRows, str)


@given(instance=model::GridChild_strategy)
def test_model::gridchild_spanRows_setter(instance):
    original = instance.spanRows
    instance.spanRows = original
    assert instance.spanRows == original

@given(instance=model::GridChild_strategy)
def test_model::gridchild_verticalAlignment_type(instance):
    assert isinstance(instance.verticalAlignment, str)


@given(instance=model::GridChild_strategy)
def test_model::gridchild_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original

@given(instance=model::GridChild_strategy)
def test_model::gridchild_grabHorizontalSpace_type(instance):
    assert isinstance(instance.grabHorizontalSpace, bool)


@given(instance=model::GridChild_strategy)
def test_model::gridchild_grabHorizontalSpace_setter(instance):
    original = instance.grabHorizontalSpace
    instance.grabHorizontalSpace = original
    assert instance.grabHorizontalSpace == original

@given(instance=model::GridChild_strategy)
def test_model::gridchild_widthHint_type(instance):
    assert isinstance(instance.widthHint, str)


@given(instance=model::GridChild_strategy)
def test_model::gridchild_widthHint_setter(instance):
    original = instance.widthHint
    instance.widthHint = original
    assert instance.widthHint == original

@given(instance=model::GridChild_strategy)
def test_model::gridchild_heightHint_type(instance):
    assert isinstance(instance.heightHint, str)


@given(instance=model::GridChild_strategy)
def test_model::gridchild_heightHint_setter(instance):
    original = instance.heightHint
    instance.heightHint = original
    assert instance.heightHint == original

@given(instance=model::GridChild_strategy)
def test_model::gridchild_spanCols_type(instance):
    assert isinstance(instance.spanCols, int)


@given(instance=model::GridChild_strategy)
def test_model::gridchild_spanCols_setter(instance):
    original = instance.spanCols
    instance.spanCols = original
    assert instance.spanCols == original

@given(instance=model::XYChild_strategy)
@settings(max_examples=50)
def test_model::xychild_instantiation(instance):
    assert isinstance(instance, model::XYChild)

@given(instance=model::Child_strategy)
@settings(max_examples=50)
def test_model::child_instantiation(instance):
    assert isinstance(instance, model::Child)

@given(instance=model::Child_strategy)
def test_model::child_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Child_strategy)
def test_model::child_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Connection_strategy)
@settings(max_examples=50)
def test_model::connection_instantiation(instance):
    assert isinstance(instance, model::Connection)

@given(instance=model::Dimension_strategy)
@settings(max_examples=50)
def test_model::dimension_instantiation(instance):
    assert isinstance(instance, model::Dimension)

@given(instance=model::Dimension_strategy)
def test_model::dimension_width_type(instance):
    assert isinstance(instance.width, float)


@given(instance=model::Dimension_strategy)
def test_model::dimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=model::Dimension_strategy)
def test_model::dimension_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=model::Dimension_strategy)
def test_model::dimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=model::Cursor_strategy)
@settings(max_examples=50)
def test_model::cursor_instantiation(instance):
    assert isinstance(instance, model::Cursor)

@given(instance=model::StringToStringMap_strategy)
@settings(max_examples=50)
def test_model::stringtostringmap_instantiation(instance):
    assert isinstance(instance, model::StringToStringMap)

@given(instance=model::StringToStringMap_strategy)
def test_model::stringtostringmap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=model::StringToStringMap_strategy)
def test_model::stringtostringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=model::StringToStringMap_strategy)
def test_model::stringtostringmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::StringToStringMap_strategy)
def test_model::stringtostringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::Primitive_strategy)
@settings(max_examples=50)
def test_model::primitive_instantiation(instance):
    assert isinstance(instance, model::Primitive)

@given(instance=model::Primitive_strategy)
def test_model::primitive_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Primitive_strategy)
def test_model::primitive_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Symbol_strategy)
@settings(max_examples=50)
def test_model::symbol_instantiation(instance):
    assert isinstance(instance, model::Symbol)

@given(instance=model::Symbol_strategy)
def test_model::symbol_onDispose_type(instance):
    assert isinstance(instance.onDispose, str)


@given(instance=model::Symbol_strategy)
def test_model::symbol_onDispose_setter(instance):
    original = instance.onDispose
    instance.onDispose = original
    assert instance.onDispose == original

@given(instance=model::Symbol_strategy)
def test_model::symbol_backgroundColor_type(instance):
    assert isinstance(instance.backgroundColor, str)


@given(instance=model::Symbol_strategy)
def test_model::symbol_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original

@given(instance=model::Symbol_strategy)
def test_model::symbol_scriptModules_type(instance):
    assert isinstance(instance.scriptModules, str)


@given(instance=model::Symbol_strategy)
def test_model::symbol_scriptModules_setter(instance):
    original = instance.scriptModules
    instance.scriptModules = original
    assert instance.scriptModules == original

@given(instance=model::Symbol_strategy)
def test_model::symbol_onInit_type(instance):
    assert isinstance(instance.onInit, str)


@given(instance=model::Symbol_strategy)
def test_model::symbol_onInit_setter(instance):
    original = instance.onInit
    instance.onInit = original
    assert instance.onInit == original

@given(instance=model::Symbol_strategy)
def test_model::symbol_onUpdate_type(instance):
    assert isinstance(instance.onUpdate, str)


@given(instance=model::Symbol_strategy)
def test_model::symbol_onUpdate_setter(instance):
    original = instance.onUpdate
    instance.onUpdate = original
    assert instance.onUpdate == original

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=model::Line_strategy)
@settings(max_examples=50)
def test_model::line_instantiation(instance):
    assert isinstance(instance, model::Line)

@given(instance=model::Arc_strategy)
@settings(max_examples=50)
def test_model::arc_instantiation(instance):
    assert isinstance(instance, model::Arc)

@given(instance=model::Arc_strategy)
def test_model::arc_start_type(instance):
    assert isinstance(instance.start, int)


@given(instance=model::Arc_strategy)
def test_model::arc_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=model::Arc_strategy)
def test_model::arc_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=model::Arc_strategy)
def test_model::arc_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=model::Ellipse_strategy)
@settings(max_examples=50)
def test_model::ellipse_instantiation(instance):
    assert isinstance(instance, model::Ellipse)

@given(instance=model::Rectangle_strategy)
@settings(max_examples=50)
def test_model::rectangle_instantiation(instance):
    assert isinstance(instance, model::Rectangle)

@given(instance=Figure_strategy)
@settings(max_examples=50)
def test_figure_instantiation(instance):
    assert isinstance(instance, Figure)

@given(instance=model::Text_strategy)
@settings(max_examples=50)
def test_model::text_instantiation(instance):
    assert isinstance(instance, model::Text)

@given(instance=model::Text_strategy)
def test_model::text_textPlacement_type(instance):
    assert isinstance(instance.textPlacement, str)


@given(instance=model::Text_strategy)
def test_model::text_textPlacement_setter(instance):
    original = instance.textPlacement
    instance.textPlacement = original
    assert instance.textPlacement == original

@given(instance=model::Text_strategy)
def test_model::text_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=model::Text_strategy)
def test_model::text_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=model::Text_strategy)
def test_model::text_textAlignment_type(instance):
    assert isinstance(instance.textAlignment, str)


@given(instance=model::Text_strategy)
def test_model::text_textAlignment_setter(instance):
    original = instance.textAlignment
    instance.textAlignment = original
    assert instance.textAlignment == original

@given(instance=model::Text_strategy)
def test_model::text_fontItalic_type(instance):
    assert isinstance(instance.fontItalic, bool)


@given(instance=model::Text_strategy)
def test_model::text_fontItalic_setter(instance):
    original = instance.fontItalic
    instance.fontItalic = original
    assert instance.fontItalic == original

@given(instance=model::Text_strategy)
def test_model::text_fontSize_type(instance):
    assert isinstance(instance.fontSize, int)


@given(instance=model::Text_strategy)
def test_model::text_fontSize_setter(instance):
    original = instance.fontSize
    instance.fontSize = original
    assert instance.fontSize == original

@given(instance=model::Text_strategy)
def test_model::text_fontName_type(instance):
    assert isinstance(instance.fontName, str)


@given(instance=model::Text_strategy)
def test_model::text_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original

@given(instance=model::Text_strategy)
def test_model::text_iconAlignment_type(instance):
    assert isinstance(instance.iconAlignment, str)


@given(instance=model::Text_strategy)
def test_model::text_iconAlignment_setter(instance):
    original = instance.iconAlignment
    instance.iconAlignment = original
    assert instance.iconAlignment == original

@given(instance=model::Text_strategy)
def test_model::text_fontBold_type(instance):
    assert isinstance(instance.fontBold, bool)


@given(instance=model::Text_strategy)
def test_model::text_fontBold_setter(instance):
    original = instance.fontBold
    instance.fontBold = original
    assert instance.fontBold == original

@given(instance=model::Text_strategy)
def test_model::text_labelAlignment_type(instance):
    assert isinstance(instance.labelAlignment, str)


@given(instance=model::Text_strategy)
def test_model::text_labelAlignment_setter(instance):
    original = instance.labelAlignment
    instance.labelAlignment = original
    assert instance.labelAlignment == original

@given(instance=model::FigureContainer_strategy)
@settings(max_examples=50)
def test_model::figurecontainer_instantiation(instance):
    assert isinstance(instance, model::FigureContainer)

@given(instance=model::Image_strategy)
@settings(max_examples=50)
def test_model::image_instantiation(instance):
    assert isinstance(instance, model::Image)

@given(instance=model::Image_strategy)
def test_model::image_imageAlignment_type(instance):
    assert isinstance(instance.imageAlignment, str)


@given(instance=model::Image_strategy)
def test_model::image_imageAlignment_setter(instance):
    original = instance.imageAlignment
    instance.imageAlignment = original
    assert instance.imageAlignment == original

@given(instance=model::Image_strategy)
def test_model::image_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=model::Image_strategy)
def test_model::image_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=model::Shape_strategy)
@settings(max_examples=50)
def test_model::shape_instantiation(instance):
    assert isinstance(instance, model::Shape)

@given(instance=model::Shape_strategy)
def test_model::shape_fill_type(instance):
    assert isinstance(instance.fill, bool)


@given(instance=model::Shape_strategy)
def test_model::shape_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original

@given(instance=model::Shape_strategy)
def test_model::shape_alpha_type(instance):
    assert isinstance(instance.alpha, str)


@given(instance=model::Shape_strategy)
def test_model::shape_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original

@given(instance=model::Shape_strategy)
def test_model::shape_antialias_type(instance):
    assert isinstance(instance.antialias, str)


@given(instance=model::Shape_strategy)
def test_model::shape_antialias_setter(instance):
    original = instance.antialias
    instance.antialias = original
    assert instance.antialias == original

@given(instance=model::Shape_strategy)
def test_model::shape_lineWidth_type(instance):
    assert isinstance(instance.lineWidth, float)


@given(instance=model::Shape_strategy)
def test_model::shape_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=model::Shape_strategy)
def test_model::shape_outline_type(instance):
    assert isinstance(instance.outline, bool)


@given(instance=model::Shape_strategy)
def test_model::shape_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=model::Figure_strategy)
@settings(max_examples=50)
def test_model::figure_instantiation(instance):
    assert isinstance(instance, model::Figure)

@given(instance=model::Figure_strategy)
def test_model::figure_onClick_type(instance):
    assert isinstance(instance.onClick, str)


@given(instance=model::Figure_strategy)
def test_model::figure_onClick_setter(instance):
    original = instance.onClick
    instance.onClick = original
    assert instance.onClick == original

@given(instance=model::Figure_strategy)
def test_model::figure_onDoubleClick_type(instance):
    assert isinstance(instance.onDoubleClick, str)


@given(instance=model::Figure_strategy)
def test_model::figure_onDoubleClick_setter(instance):
    original = instance.onDoubleClick
    instance.onDoubleClick = original
    assert instance.onDoubleClick == original

@given(instance=model::Figure_strategy)
def test_model::figure_backgroundColor_type(instance):
    assert isinstance(instance.backgroundColor, str)


@given(instance=model::Figure_strategy)
def test_model::figure_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original

@given(instance=model::Figure_strategy)
def test_model::figure_opaque_type(instance):
    assert isinstance(instance.opaque, str)


@given(instance=model::Figure_strategy)
def test_model::figure_opaque_setter(instance):
    original = instance.opaque
    instance.opaque = original
    assert instance.opaque == original

@given(instance=model::Figure_strategy)
def test_model::figure_foregroundColor_type(instance):
    assert isinstance(instance.foregroundColor, str)


@given(instance=model::Figure_strategy)
def test_model::figure_foregroundColor_setter(instance):
    original = instance.foregroundColor
    instance.foregroundColor = original
    assert instance.foregroundColor == original

@given(instance=model::Figure_strategy)
def test_model::figure_border_type(instance):
    assert isinstance(instance.border, str)


@given(instance=model::Figure_strategy)
def test_model::figure_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original

@given(instance=model::Figure_strategy)
def test_model::figure_visible_type(instance):
    assert isinstance(instance.visible, bool)


@given(instance=model::Figure_strategy)
def test_model::figure_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=model::Figure_strategy)
def test_model::figure_toolTip_type(instance):
    assert isinstance(instance.toolTip, str)


@given(instance=model::Figure_strategy)
def test_model::figure_toolTip_setter(instance):
    original = instance.toolTip
    instance.toolTip = original
    assert instance.toolTip == original

@given(instance=model::Figure_strategy)
def test_model::figure_onMouseMove_type(instance):
    assert isinstance(instance.onMouseMove, str)


@given(instance=model::Figure_strategy)
def test_model::figure_onMouseMove_setter(instance):
    original = instance.onMouseMove
    instance.onMouseMove = original
    assert instance.onMouseMove == original

@given(instance=model::Figure_strategy)
def test_model::figure_onMouseHover_type(instance):
    assert isinstance(instance.onMouseHover, str)


@given(instance=model::Figure_strategy)
def test_model::figure_onMouseHover_setter(instance):
    original = instance.onMouseHover
    instance.onMouseHover = original
    assert instance.onMouseHover == original

@given(instance=model::Figure_strategy)
def test_model::figure_onMouseDrag_type(instance):
    assert isinstance(instance.onMouseDrag, str)


@given(instance=model::Figure_strategy)
def test_model::figure_onMouseDrag_setter(instance):
    original = instance.onMouseDrag
    instance.onMouseDrag = original
    assert instance.onMouseDrag == original

@given(instance=model::Figure_strategy)
def test_model::figure_onMouseIn_type(instance):
    assert isinstance(instance.onMouseIn, str)


@given(instance=model::Figure_strategy)
def test_model::figure_onMouseIn_setter(instance):
    original = instance.onMouseIn
    instance.onMouseIn = original
    assert instance.onMouseIn == original

@given(instance=model::Figure_strategy)
def test_model::figure_onMouseOut_type(instance):
    assert isinstance(instance.onMouseOut, str)


@given(instance=model::Figure_strategy)
def test_model::figure_onMouseOut_setter(instance):
    original = instance.onMouseOut
    instance.onMouseOut = original
    assert instance.onMouseOut == original

@given(instance=model::SymbolReference_strategy)
@settings(max_examples=50)
def test_model::symbolreference_instantiation(instance):
    assert isinstance(instance, model::SymbolReference)

@given(instance=model::SymbolReference_strategy)
def test_model::symbolreference_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=model::SymbolReference_strategy)
def test_model::symbolreference_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=model::SymbolReference_strategy)
def test_model::symbolreference_zoom_type(instance):
    assert isinstance(instance.zoom, str)


@given(instance=model::SymbolReference_strategy)
def test_model::symbolreference_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original

@given(instance=model::SymbolReference_strategy)
def test_model::symbolreference_onCreateProperties_type(instance):
    assert isinstance(instance.onCreateProperties, str)


@given(instance=model::SymbolReference_strategy)
def test_model::symbolreference_onCreateProperties_setter(instance):
    original = instance.onCreateProperties
    instance.onCreateProperties = original
    assert instance.onCreateProperties == original

@given(instance=model::Container_strategy)
@settings(max_examples=50)
def test_model::container_instantiation(instance):
    assert isinstance(instance, model::Container)
