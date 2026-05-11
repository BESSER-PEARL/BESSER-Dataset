import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Layout,
    gmfgraph::FlowLayout,
    gmfgraph::StackLayout,
    gmfgraph::GridLayout,
    gmfgraph::BorderLayout,
    gmfgraph::XYLayout,
    gmfgraph::Layout,
    LayoutData,
    gmfgraph::BorderLayoutData,
    gmfgraph::XYLayoutData,
    gmfgraph::GridLayoutData,
    gmfgraph::Layoutable,
    gmfgraph::LayoutData,
    Font,
    gmfgraph::BasicFont,
    Border,
    gmfgraph::CompoundBorder,
    gmfgraph::MarginBorder,
    gmfgraph::LineBorder,
    gmfgraph::FigureAccessor,
    Color,
    gmfgraph::ConstantColor,
    gmfgraph::RGBColor,
    CustomFigure,
    CustomClass,
    gmfgraph::CustomLayout,
    gmfgraph::CustomLayoutData,
    gmfgraph::CustomBorder,
    gmfgraph::CustomAttribute,
    gmfgraph::CustomClass,
    DecorationFigure,
    gmfgraph::CustomDecoration,
    ConnectionFigure,
    gmfgraph::CustomConnection,
    Polygon,
    gmfgraph::PolygonDecoration,
    gmfgraph::ScalablePolygon,
    Polyline,
    gmfgraph::PolylineConnection,
    gmfgraph::PolylineDecoration,
    gmfgraph::Polygon,
    AbstractFigure,
    Shape,
    gmfgraph::Ellipse,
    gmfgraph::Polyline,
    gmfgraph::RoundedRectangle,
    gmfgraph::Rectangle,
    RealFigure,
    gmfgraph::DecorationFigure,
    gmfgraph::CustomFigure,
    gmfgraph::LabeledContainer,
    gmfgraph::Shape,
    gmfgraph::Label,
    gmfgraph::ConnectionFigure,
    gmfgraph::FigureRef,
    gmfgraph::Color,
    Figure,
    gmfgraph::AbstractFigure,
    gmfgraph::Point,
    gmfgraph::Border,
    gmfgraph::Insets,
    gmfgraph::Font,
    gmfgraph::ChildAccess,
    Layoutable,
    gmfgraph::Figure,
    gmfgraph::Dimension,
    VisualFacet,
    gmfgraph::AlignmentFacet,
    gmfgraph::LabelOffsetFacet,
    gmfgraph::DefaultSizeFacet,
    gmfgraph::GradientFacet,
    gmfgraph::GeneralFacet,
    Node,
    AbstractNode,
    gmfgraph::Node,
    DiagramElement,
    gmfgraph::Connection,
    gmfgraph::AbstractNode,
    gmfgraph::VisualFacet,
    gmfgraph::Identity,
    gmfgraph::RealFigure,
    gmfgraph::DiagramLabel,
    gmfgraph::Compartment,
    Identity,
    gmfgraph::FigureDescriptor,
    gmfgraph::DiagramElement,
    gmfgraph::FigureGallery,
    gmfgraph::Canvas,
    ColorConstants,
    Direction,
    LineKind,
    FontStyle,
    Alignment,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_layout_is_not_abstract():
    assert not inspect.isabstract(Layout)


def test_layout_constructor_exists():
    assert callable(Layout.__init__)


def test_layout_constructor_args():
    sig = inspect.signature(Layout.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::flowlayout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::FlowLayout)


def test_gmfgraph::flowlayout_constructor_exists():
    assert callable(gmfgraph::FlowLayout.__init__)


def test_gmfgraph::flowlayout_constructor_args():
    sig = inspect.signature(gmfgraph::FlowLayout.__init__)
    params = list(sig.parameters.keys())
    assert "majorSpacing" in params, "Missing parameter 'majorSpacing'"
    assert "majorAlignment" in params, "Missing parameter 'majorAlignment'"
    assert "forceSingleLine" in params, "Missing parameter 'forceSingleLine'"
    assert "matchMinorSize" in params, "Missing parameter 'matchMinorSize'"
    assert "vertical" in params, "Missing parameter 'vertical'"
    assert "minorAlignment" in params, "Missing parameter 'minorAlignment'"
    assert "minorSpacing" in params, "Missing parameter 'minorSpacing'"

def test_gmfgraph::flowlayout_has_majorSpacing():
    assert hasattr(gmfgraph::FlowLayout, "majorSpacing")
    descriptor = None
    for klass in gmfgraph::FlowLayout.__mro__:
        if "majorSpacing" in klass.__dict__:
            descriptor = klass.__dict__["majorSpacing"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::flowlayout_has_majorAlignment():
    assert hasattr(gmfgraph::FlowLayout, "majorAlignment")
    descriptor = None
    for klass in gmfgraph::FlowLayout.__mro__:
        if "majorAlignment" in klass.__dict__:
            descriptor = klass.__dict__["majorAlignment"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::flowlayout_has_forceSingleLine():
    assert hasattr(gmfgraph::FlowLayout, "forceSingleLine")
    descriptor = None
    for klass in gmfgraph::FlowLayout.__mro__:
        if "forceSingleLine" in klass.__dict__:
            descriptor = klass.__dict__["forceSingleLine"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::flowlayout_has_matchMinorSize():
    assert hasattr(gmfgraph::FlowLayout, "matchMinorSize")
    descriptor = None
    for klass in gmfgraph::FlowLayout.__mro__:
        if "matchMinorSize" in klass.__dict__:
            descriptor = klass.__dict__["matchMinorSize"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::flowlayout_has_vertical():
    assert hasattr(gmfgraph::FlowLayout, "vertical")
    descriptor = None
    for klass in gmfgraph::FlowLayout.__mro__:
        if "vertical" in klass.__dict__:
            descriptor = klass.__dict__["vertical"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::flowlayout_has_minorAlignment():
    assert hasattr(gmfgraph::FlowLayout, "minorAlignment")
    descriptor = None
    for klass in gmfgraph::FlowLayout.__mro__:
        if "minorAlignment" in klass.__dict__:
            descriptor = klass.__dict__["minorAlignment"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::flowlayout_has_minorSpacing():
    assert hasattr(gmfgraph::FlowLayout, "minorSpacing")
    descriptor = None
    for klass in gmfgraph::FlowLayout.__mro__:
        if "minorSpacing" in klass.__dict__:
            descriptor = klass.__dict__["minorSpacing"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::stacklayout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::StackLayout)


def test_gmfgraph::stacklayout_constructor_exists():
    assert callable(gmfgraph::StackLayout.__init__)


def test_gmfgraph::stacklayout_constructor_args():
    sig = inspect.signature(gmfgraph::StackLayout.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::gridlayout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::GridLayout)


def test_gmfgraph::gridlayout_constructor_exists():
    assert callable(gmfgraph::GridLayout.__init__)


def test_gmfgraph::gridlayout_constructor_args():
    sig = inspect.signature(gmfgraph::GridLayout.__init__)
    params = list(sig.parameters.keys())
    assert "equalWidth" in params, "Missing parameter 'equalWidth'"
    assert "numColumns" in params, "Missing parameter 'numColumns'"

def test_gmfgraph::gridlayout_has_equalWidth():
    assert hasattr(gmfgraph::GridLayout, "equalWidth")
    descriptor = None
    for klass in gmfgraph::GridLayout.__mro__:
        if "equalWidth" in klass.__dict__:
            descriptor = klass.__dict__["equalWidth"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::gridlayout_has_numColumns():
    assert hasattr(gmfgraph::GridLayout, "numColumns")
    descriptor = None
    for klass in gmfgraph::GridLayout.__mro__:
        if "numColumns" in klass.__dict__:
            descriptor = klass.__dict__["numColumns"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::borderlayout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::BorderLayout)


def test_gmfgraph::borderlayout_constructor_exists():
    assert callable(gmfgraph::BorderLayout.__init__)


def test_gmfgraph::borderlayout_constructor_args():
    sig = inspect.signature(gmfgraph::BorderLayout.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::xylayout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::XYLayout)


def test_gmfgraph::xylayout_constructor_exists():
    assert callable(gmfgraph::XYLayout.__init__)


def test_gmfgraph::xylayout_constructor_args():
    sig = inspect.signature(gmfgraph::XYLayout.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::layout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Layout)


def test_gmfgraph::layout_constructor_exists():
    assert callable(gmfgraph::Layout.__init__)


def test_gmfgraph::layout_constructor_args():
    sig = inspect.signature(gmfgraph::Layout.__init__)
    params = list(sig.parameters.keys())



def test_layoutdata_is_not_abstract():
    assert not inspect.isabstract(LayoutData)


def test_layoutdata_constructor_exists():
    assert callable(LayoutData.__init__)


def test_layoutdata_constructor_args():
    sig = inspect.signature(LayoutData.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::borderlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::BorderLayoutData)


def test_gmfgraph::borderlayoutdata_constructor_exists():
    assert callable(gmfgraph::BorderLayoutData.__init__)


def test_gmfgraph::borderlayoutdata_constructor_args():
    sig = inspect.signature(gmfgraph::BorderLayoutData.__init__)
    params = list(sig.parameters.keys())
    assert "vertical" in params, "Missing parameter 'vertical'"
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_gmfgraph::borderlayoutdata_has_vertical():
    assert hasattr(gmfgraph::BorderLayoutData, "vertical")
    descriptor = None
    for klass in gmfgraph::BorderLayoutData.__mro__:
        if "vertical" in klass.__dict__:
            descriptor = klass.__dict__["vertical"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::borderlayoutdata_has_alignment():
    assert hasattr(gmfgraph::BorderLayoutData, "alignment")
    descriptor = None
    for klass in gmfgraph::BorderLayoutData.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::xylayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::XYLayoutData)


def test_gmfgraph::xylayoutdata_constructor_exists():
    assert callable(gmfgraph::XYLayoutData.__init__)


def test_gmfgraph::xylayoutdata_constructor_args():
    sig = inspect.signature(gmfgraph::XYLayoutData.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::gridlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::GridLayoutData)


def test_gmfgraph::gridlayoutdata_constructor_exists():
    assert callable(gmfgraph::GridLayoutData.__init__)


def test_gmfgraph::gridlayoutdata_constructor_args():
    sig = inspect.signature(gmfgraph::GridLayoutData.__init__)
    params = list(sig.parameters.keys())
    assert "grabExcessHorizontalSpace" in params, "Missing parameter 'grabExcessHorizontalSpace'"
    assert "horizontalIndent" in params, "Missing parameter 'horizontalIndent'"
    assert "verticalSpan" in params, "Missing parameter 'verticalSpan'"
    assert "grabExcessVerticalSpace" in params, "Missing parameter 'grabExcessVerticalSpace'"
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"
    assert "horizontalSpan" in params, "Missing parameter 'horizontalSpan'"

def test_gmfgraph::gridlayoutdata_has_grabExcessHorizontalSpace():
    assert hasattr(gmfgraph::GridLayoutData, "grabExcessHorizontalSpace")
    descriptor = None
    for klass in gmfgraph::GridLayoutData.__mro__:
        if "grabExcessHorizontalSpace" in klass.__dict__:
            descriptor = klass.__dict__["grabExcessHorizontalSpace"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::gridlayoutdata_has_horizontalIndent():
    assert hasattr(gmfgraph::GridLayoutData, "horizontalIndent")
    descriptor = None
    for klass in gmfgraph::GridLayoutData.__mro__:
        if "horizontalIndent" in klass.__dict__:
            descriptor = klass.__dict__["horizontalIndent"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::gridlayoutdata_has_verticalSpan():
    assert hasattr(gmfgraph::GridLayoutData, "verticalSpan")
    descriptor = None
    for klass in gmfgraph::GridLayoutData.__mro__:
        if "verticalSpan" in klass.__dict__:
            descriptor = klass.__dict__["verticalSpan"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::gridlayoutdata_has_grabExcessVerticalSpace():
    assert hasattr(gmfgraph::GridLayoutData, "grabExcessVerticalSpace")
    descriptor = None
    for klass in gmfgraph::GridLayoutData.__mro__:
        if "grabExcessVerticalSpace" in klass.__dict__:
            descriptor = klass.__dict__["grabExcessVerticalSpace"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::gridlayoutdata_has_horizontalAlignment():
    assert hasattr(gmfgraph::GridLayoutData, "horizontalAlignment")
    descriptor = None
    for klass in gmfgraph::GridLayoutData.__mro__:
        if "horizontalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["horizontalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::gridlayoutdata_has_verticalAlignment():
    assert hasattr(gmfgraph::GridLayoutData, "verticalAlignment")
    descriptor = None
    for klass in gmfgraph::GridLayoutData.__mro__:
        if "verticalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::gridlayoutdata_has_horizontalSpan():
    assert hasattr(gmfgraph::GridLayoutData, "horizontalSpan")
    descriptor = None
    for klass in gmfgraph::GridLayoutData.__mro__:
        if "horizontalSpan" in klass.__dict__:
            descriptor = klass.__dict__["horizontalSpan"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::layoutable_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Layoutable)


def test_gmfgraph::layoutable_constructor_exists():
    assert callable(gmfgraph::Layoutable.__init__)


def test_gmfgraph::layoutable_constructor_args():
    sig = inspect.signature(gmfgraph::Layoutable.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::layoutdata_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::LayoutData)


def test_gmfgraph::layoutdata_constructor_exists():
    assert callable(gmfgraph::LayoutData.__init__)


def test_gmfgraph::layoutdata_constructor_args():
    sig = inspect.signature(gmfgraph::LayoutData.__init__)
    params = list(sig.parameters.keys())



def test_font_is_not_abstract():
    assert not inspect.isabstract(Font)


def test_font_constructor_exists():
    assert callable(Font.__init__)


def test_font_constructor_args():
    sig = inspect.signature(Font.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::basicfont_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::BasicFont)


def test_gmfgraph::basicfont_constructor_exists():
    assert callable(gmfgraph::BasicFont.__init__)


def test_gmfgraph::basicfont_constructor_args():
    sig = inspect.signature(gmfgraph::BasicFont.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "faceName" in params, "Missing parameter 'faceName'"
    assert "height" in params, "Missing parameter 'height'"

def test_gmfgraph::basicfont_has_style():
    assert hasattr(gmfgraph::BasicFont, "style")
    descriptor = None
    for klass in gmfgraph::BasicFont.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::basicfont_has_faceName():
    assert hasattr(gmfgraph::BasicFont, "faceName")
    descriptor = None
    for klass in gmfgraph::BasicFont.__mro__:
        if "faceName" in klass.__dict__:
            descriptor = klass.__dict__["faceName"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::basicfont_has_height():
    assert hasattr(gmfgraph::BasicFont, "height")
    descriptor = None
    for klass in gmfgraph::BasicFont.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_border_is_not_abstract():
    assert not inspect.isabstract(Border)


def test_border_constructor_exists():
    assert callable(Border.__init__)


def test_border_constructor_args():
    sig = inspect.signature(Border.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::compoundborder_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::CompoundBorder)


def test_gmfgraph::compoundborder_constructor_exists():
    assert callable(gmfgraph::CompoundBorder.__init__)


def test_gmfgraph::compoundborder_constructor_args():
    sig = inspect.signature(gmfgraph::CompoundBorder.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::marginborder_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::MarginBorder)


def test_gmfgraph::marginborder_constructor_exists():
    assert callable(gmfgraph::MarginBorder.__init__)


def test_gmfgraph::marginborder_constructor_args():
    sig = inspect.signature(gmfgraph::MarginBorder.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::lineborder_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::LineBorder)


def test_gmfgraph::lineborder_constructor_exists():
    assert callable(gmfgraph::LineBorder.__init__)


def test_gmfgraph::lineborder_constructor_args():
    sig = inspect.signature(gmfgraph::LineBorder.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"

def test_gmfgraph::lineborder_has_width():
    assert hasattr(gmfgraph::LineBorder, "width")
    descriptor = None
    for klass in gmfgraph::LineBorder.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::figureaccessor_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::FigureAccessor)


def test_gmfgraph::figureaccessor_constructor_exists():
    assert callable(gmfgraph::FigureAccessor.__init__)


def test_gmfgraph::figureaccessor_constructor_args():
    sig = inspect.signature(gmfgraph::FigureAccessor.__init__)
    params = list(sig.parameters.keys())
    assert "accessor" in params, "Missing parameter 'accessor'"

def test_gmfgraph::figureaccessor_has_accessor():
    assert hasattr(gmfgraph::FigureAccessor, "accessor")
    descriptor = None
    for klass in gmfgraph::FigureAccessor.__mro__:
        if "accessor" in klass.__dict__:
            descriptor = klass.__dict__["accessor"]
            break
    assert isinstance(descriptor, property)



def test_color_is_not_abstract():
    assert not inspect.isabstract(Color)


def test_color_constructor_exists():
    assert callable(Color.__init__)


def test_color_constructor_args():
    sig = inspect.signature(Color.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::constantcolor_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::ConstantColor)


def test_gmfgraph::constantcolor_constructor_exists():
    assert callable(gmfgraph::ConstantColor.__init__)


def test_gmfgraph::constantcolor_constructor_args():
    sig = inspect.signature(gmfgraph::ConstantColor.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gmfgraph::constantcolor_has_value():
    assert hasattr(gmfgraph::ConstantColor, "value")
    descriptor = None
    for klass in gmfgraph::ConstantColor.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::rgbcolor_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::RGBColor)


def test_gmfgraph::rgbcolor_constructor_exists():
    assert callable(gmfgraph::RGBColor.__init__)


def test_gmfgraph::rgbcolor_constructor_args():
    sig = inspect.signature(gmfgraph::RGBColor.__init__)
    params = list(sig.parameters.keys())
    assert "blue" in params, "Missing parameter 'blue'"
    assert "green" in params, "Missing parameter 'green'"
    assert "red" in params, "Missing parameter 'red'"

def test_gmfgraph::rgbcolor_has_blue():
    assert hasattr(gmfgraph::RGBColor, "blue")
    descriptor = None
    for klass in gmfgraph::RGBColor.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::rgbcolor_has_green():
    assert hasattr(gmfgraph::RGBColor, "green")
    descriptor = None
    for klass in gmfgraph::RGBColor.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::rgbcolor_has_red():
    assert hasattr(gmfgraph::RGBColor, "red")
    descriptor = None
    for klass in gmfgraph::RGBColor.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)



def test_customfigure_is_not_abstract():
    assert not inspect.isabstract(CustomFigure)


def test_customfigure_constructor_exists():
    assert callable(CustomFigure.__init__)


def test_customfigure_constructor_args():
    sig = inspect.signature(CustomFigure.__init__)
    params = list(sig.parameters.keys())



def test_customclass_is_not_abstract():
    assert not inspect.isabstract(CustomClass)


def test_customclass_constructor_exists():
    assert callable(CustomClass.__init__)


def test_customclass_constructor_args():
    sig = inspect.signature(CustomClass.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::customlayout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::CustomLayout)


def test_gmfgraph::customlayout_constructor_exists():
    assert callable(gmfgraph::CustomLayout.__init__)


def test_gmfgraph::customlayout_constructor_args():
    sig = inspect.signature(gmfgraph::CustomLayout.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::customlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::CustomLayoutData)


def test_gmfgraph::customlayoutdata_constructor_exists():
    assert callable(gmfgraph::CustomLayoutData.__init__)


def test_gmfgraph::customlayoutdata_constructor_args():
    sig = inspect.signature(gmfgraph::CustomLayoutData.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::customborder_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::CustomBorder)


def test_gmfgraph::customborder_constructor_exists():
    assert callable(gmfgraph::CustomBorder.__init__)


def test_gmfgraph::customborder_constructor_args():
    sig = inspect.signature(gmfgraph::CustomBorder.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::customattribute_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::CustomAttribute)


def test_gmfgraph::customattribute_constructor_exists():
    assert callable(gmfgraph::CustomAttribute.__init__)


def test_gmfgraph::customattribute_constructor_args():
    sig = inspect.signature(gmfgraph::CustomAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "multiStatementValue" in params, "Missing parameter 'multiStatementValue'"
    assert "directAccess" in params, "Missing parameter 'directAccess'"
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_gmfgraph::customattribute_has_multiStatementValue():
    assert hasattr(gmfgraph::CustomAttribute, "multiStatementValue")
    descriptor = None
    for klass in gmfgraph::CustomAttribute.__mro__:
        if "multiStatementValue" in klass.__dict__:
            descriptor = klass.__dict__["multiStatementValue"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::customattribute_has_directAccess():
    assert hasattr(gmfgraph::CustomAttribute, "directAccess")
    descriptor = None
    for klass in gmfgraph::CustomAttribute.__mro__:
        if "directAccess" in klass.__dict__:
            descriptor = klass.__dict__["directAccess"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::customattribute_has_name():
    assert hasattr(gmfgraph::CustomAttribute, "name")
    descriptor = None
    for klass in gmfgraph::CustomAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::customattribute_has_value():
    assert hasattr(gmfgraph::CustomAttribute, "value")
    descriptor = None
    for klass in gmfgraph::CustomAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::customclass_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::CustomClass)


def test_gmfgraph::customclass_constructor_exists():
    assert callable(gmfgraph::CustomClass.__init__)


def test_gmfgraph::customclass_constructor_args():
    sig = inspect.signature(gmfgraph::CustomClass.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedClassName" in params, "Missing parameter 'qualifiedClassName'"

def test_gmfgraph::customclass_has_qualifiedClassName():
    assert hasattr(gmfgraph::CustomClass, "qualifiedClassName")
    descriptor = None
    for klass in gmfgraph::CustomClass.__mro__:
        if "qualifiedClassName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedClassName"]
            break
    assert isinstance(descriptor, property)



def test_decorationfigure_is_not_abstract():
    assert not inspect.isabstract(DecorationFigure)


def test_decorationfigure_constructor_exists():
    assert callable(DecorationFigure.__init__)


def test_decorationfigure_constructor_args():
    sig = inspect.signature(DecorationFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::customdecoration_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::CustomDecoration)


def test_gmfgraph::customdecoration_constructor_exists():
    assert callable(gmfgraph::CustomDecoration.__init__)


def test_gmfgraph::customdecoration_constructor_args():
    sig = inspect.signature(gmfgraph::CustomDecoration.__init__)
    params = list(sig.parameters.keys())



def test_connectionfigure_is_not_abstract():
    assert not inspect.isabstract(ConnectionFigure)


def test_connectionfigure_constructor_exists():
    assert callable(ConnectionFigure.__init__)


def test_connectionfigure_constructor_args():
    sig = inspect.signature(ConnectionFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::customconnection_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::CustomConnection)


def test_gmfgraph::customconnection_constructor_exists():
    assert callable(gmfgraph::CustomConnection.__init__)


def test_gmfgraph::customconnection_constructor_args():
    sig = inspect.signature(gmfgraph::CustomConnection.__init__)
    params = list(sig.parameters.keys())



def test_polygon_is_not_abstract():
    assert not inspect.isabstract(Polygon)


def test_polygon_constructor_exists():
    assert callable(Polygon.__init__)


def test_polygon_constructor_args():
    sig = inspect.signature(Polygon.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::polygondecoration_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::PolygonDecoration)


def test_gmfgraph::polygondecoration_constructor_exists():
    assert callable(gmfgraph::PolygonDecoration.__init__)


def test_gmfgraph::polygondecoration_constructor_args():
    sig = inspect.signature(gmfgraph::PolygonDecoration.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::scalablepolygon_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::ScalablePolygon)


def test_gmfgraph::scalablepolygon_constructor_exists():
    assert callable(gmfgraph::ScalablePolygon.__init__)


def test_gmfgraph::scalablepolygon_constructor_args():
    sig = inspect.signature(gmfgraph::ScalablePolygon.__init__)
    params = list(sig.parameters.keys())



def test_polyline_is_not_abstract():
    assert not inspect.isabstract(Polyline)


def test_polyline_constructor_exists():
    assert callable(Polyline.__init__)


def test_polyline_constructor_args():
    sig = inspect.signature(Polyline.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::polylineconnection_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::PolylineConnection)


def test_gmfgraph::polylineconnection_constructor_exists():
    assert callable(gmfgraph::PolylineConnection.__init__)


def test_gmfgraph::polylineconnection_constructor_args():
    sig = inspect.signature(gmfgraph::PolylineConnection.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::polylinedecoration_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::PolylineDecoration)


def test_gmfgraph::polylinedecoration_constructor_exists():
    assert callable(gmfgraph::PolylineDecoration.__init__)


def test_gmfgraph::polylinedecoration_constructor_args():
    sig = inspect.signature(gmfgraph::PolylineDecoration.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::polygon_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Polygon)


def test_gmfgraph::polygon_constructor_exists():
    assert callable(gmfgraph::Polygon.__init__)


def test_gmfgraph::polygon_constructor_args():
    sig = inspect.signature(gmfgraph::Polygon.__init__)
    params = list(sig.parameters.keys())



def test_abstractfigure_is_not_abstract():
    assert not inspect.isabstract(AbstractFigure)


def test_abstractfigure_constructor_exists():
    assert callable(AbstractFigure.__init__)


def test_abstractfigure_constructor_args():
    sig = inspect.signature(AbstractFigure.__init__)
    params = list(sig.parameters.keys())



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::ellipse_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Ellipse)


def test_gmfgraph::ellipse_constructor_exists():
    assert callable(gmfgraph::Ellipse.__init__)


def test_gmfgraph::ellipse_constructor_args():
    sig = inspect.signature(gmfgraph::Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::polyline_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Polyline)


def test_gmfgraph::polyline_constructor_exists():
    assert callable(gmfgraph::Polyline.__init__)


def test_gmfgraph::polyline_constructor_args():
    sig = inspect.signature(gmfgraph::Polyline.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::roundedrectangle_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::RoundedRectangle)


def test_gmfgraph::roundedrectangle_constructor_exists():
    assert callable(gmfgraph::RoundedRectangle.__init__)


def test_gmfgraph::roundedrectangle_constructor_args():
    sig = inspect.signature(gmfgraph::RoundedRectangle.__init__)
    params = list(sig.parameters.keys())
    assert "cornerWidth" in params, "Missing parameter 'cornerWidth'"
    assert "cornerHeight" in params, "Missing parameter 'cornerHeight'"

def test_gmfgraph::roundedrectangle_has_cornerWidth():
    assert hasattr(gmfgraph::RoundedRectangle, "cornerWidth")
    descriptor = None
    for klass in gmfgraph::RoundedRectangle.__mro__:
        if "cornerWidth" in klass.__dict__:
            descriptor = klass.__dict__["cornerWidth"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::roundedrectangle_has_cornerHeight():
    assert hasattr(gmfgraph::RoundedRectangle, "cornerHeight")
    descriptor = None
    for klass in gmfgraph::RoundedRectangle.__mro__:
        if "cornerHeight" in klass.__dict__:
            descriptor = klass.__dict__["cornerHeight"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::rectangle_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Rectangle)


def test_gmfgraph::rectangle_constructor_exists():
    assert callable(gmfgraph::Rectangle.__init__)


def test_gmfgraph::rectangle_constructor_args():
    sig = inspect.signature(gmfgraph::Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_realfigure_is_not_abstract():
    assert not inspect.isabstract(RealFigure)


def test_realfigure_constructor_exists():
    assert callable(RealFigure.__init__)


def test_realfigure_constructor_args():
    sig = inspect.signature(RealFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::decorationfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::DecorationFigure)


def test_gmfgraph::decorationfigure_constructor_exists():
    assert callable(gmfgraph::DecorationFigure.__init__)


def test_gmfgraph::decorationfigure_constructor_args():
    sig = inspect.signature(gmfgraph::DecorationFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::customfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::CustomFigure)


def test_gmfgraph::customfigure_constructor_exists():
    assert callable(gmfgraph::CustomFigure.__init__)


def test_gmfgraph::customfigure_constructor_args():
    sig = inspect.signature(gmfgraph::CustomFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::labeledcontainer_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::LabeledContainer)


def test_gmfgraph::labeledcontainer_constructor_exists():
    assert callable(gmfgraph::LabeledContainer.__init__)


def test_gmfgraph::labeledcontainer_constructor_args():
    sig = inspect.signature(gmfgraph::LabeledContainer.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::shape_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Shape)


def test_gmfgraph::shape_constructor_exists():
    assert callable(gmfgraph::Shape.__init__)


def test_gmfgraph::shape_constructor_args():
    sig = inspect.signature(gmfgraph::Shape.__init__)
    params = list(sig.parameters.keys())
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "fill" in params, "Missing parameter 'fill'"
    assert "xorFill" in params, "Missing parameter 'xorFill'"
    assert "outline" in params, "Missing parameter 'outline'"
    assert "lineKind" in params, "Missing parameter 'lineKind'"
    assert "xorOutline" in params, "Missing parameter 'xorOutline'"

def test_gmfgraph::shape_has_lineWidth():
    assert hasattr(gmfgraph::Shape, "lineWidth")
    descriptor = None
    for klass in gmfgraph::Shape.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::shape_has_fill():
    assert hasattr(gmfgraph::Shape, "fill")
    descriptor = None
    for klass in gmfgraph::Shape.__mro__:
        if "fill" in klass.__dict__:
            descriptor = klass.__dict__["fill"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::shape_has_xorFill():
    assert hasattr(gmfgraph::Shape, "xorFill")
    descriptor = None
    for klass in gmfgraph::Shape.__mro__:
        if "xorFill" in klass.__dict__:
            descriptor = klass.__dict__["xorFill"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::shape_has_outline():
    assert hasattr(gmfgraph::Shape, "outline")
    descriptor = None
    for klass in gmfgraph::Shape.__mro__:
        if "outline" in klass.__dict__:
            descriptor = klass.__dict__["outline"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::shape_has_lineKind():
    assert hasattr(gmfgraph::Shape, "lineKind")
    descriptor = None
    for klass in gmfgraph::Shape.__mro__:
        if "lineKind" in klass.__dict__:
            descriptor = klass.__dict__["lineKind"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::shape_has_xorOutline():
    assert hasattr(gmfgraph::Shape, "xorOutline")
    descriptor = None
    for klass in gmfgraph::Shape.__mro__:
        if "xorOutline" in klass.__dict__:
            descriptor = klass.__dict__["xorOutline"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::label_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Label)


def test_gmfgraph::label_constructor_exists():
    assert callable(gmfgraph::Label.__init__)


def test_gmfgraph::label_constructor_args():
    sig = inspect.signature(gmfgraph::Label.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_gmfgraph::label_has_text():
    assert hasattr(gmfgraph::Label, "text")
    descriptor = None
    for klass in gmfgraph::Label.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::connectionfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::ConnectionFigure)


def test_gmfgraph::connectionfigure_constructor_exists():
    assert callable(gmfgraph::ConnectionFigure.__init__)


def test_gmfgraph::connectionfigure_constructor_args():
    sig = inspect.signature(gmfgraph::ConnectionFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::figureref_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::FigureRef)


def test_gmfgraph::figureref_constructor_exists():
    assert callable(gmfgraph::FigureRef.__init__)


def test_gmfgraph::figureref_constructor_args():
    sig = inspect.signature(gmfgraph::FigureRef.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::color_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Color)


def test_gmfgraph::color_constructor_exists():
    assert callable(gmfgraph::Color.__init__)


def test_gmfgraph::color_constructor_args():
    sig = inspect.signature(gmfgraph::Color.__init__)
    params = list(sig.parameters.keys())



def test_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::abstractfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::AbstractFigure)


def test_gmfgraph::abstractfigure_constructor_exists():
    assert callable(gmfgraph::AbstractFigure.__init__)


def test_gmfgraph::abstractfigure_constructor_args():
    sig = inspect.signature(gmfgraph::AbstractFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::point_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Point)


def test_gmfgraph::point_constructor_exists():
    assert callable(gmfgraph::Point.__init__)


def test_gmfgraph::point_constructor_args():
    sig = inspect.signature(gmfgraph::Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_gmfgraph::point_has_y():
    assert hasattr(gmfgraph::Point, "y")
    descriptor = None
    for klass in gmfgraph::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::point_has_x():
    assert hasattr(gmfgraph::Point, "x")
    descriptor = None
    for klass in gmfgraph::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::border_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Border)


def test_gmfgraph::border_constructor_exists():
    assert callable(gmfgraph::Border.__init__)


def test_gmfgraph::border_constructor_args():
    sig = inspect.signature(gmfgraph::Border.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::insets_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Insets)


def test_gmfgraph::insets_constructor_exists():
    assert callable(gmfgraph::Insets.__init__)


def test_gmfgraph::insets_constructor_args():
    sig = inspect.signature(gmfgraph::Insets.__init__)
    params = list(sig.parameters.keys())
    assert "left" in params, "Missing parameter 'left'"
    assert "bottom" in params, "Missing parameter 'bottom'"
    assert "top" in params, "Missing parameter 'top'"
    assert "right" in params, "Missing parameter 'right'"

def test_gmfgraph::insets_has_left():
    assert hasattr(gmfgraph::Insets, "left")
    descriptor = None
    for klass in gmfgraph::Insets.__mro__:
        if "left" in klass.__dict__:
            descriptor = klass.__dict__["left"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::insets_has_bottom():
    assert hasattr(gmfgraph::Insets, "bottom")
    descriptor = None
    for klass in gmfgraph::Insets.__mro__:
        if "bottom" in klass.__dict__:
            descriptor = klass.__dict__["bottom"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::insets_has_top():
    assert hasattr(gmfgraph::Insets, "top")
    descriptor = None
    for klass in gmfgraph::Insets.__mro__:
        if "top" in klass.__dict__:
            descriptor = klass.__dict__["top"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::insets_has_right():
    assert hasattr(gmfgraph::Insets, "right")
    descriptor = None
    for klass in gmfgraph::Insets.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::font_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Font)


def test_gmfgraph::font_constructor_exists():
    assert callable(gmfgraph::Font.__init__)


def test_gmfgraph::font_constructor_args():
    sig = inspect.signature(gmfgraph::Font.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::childaccess_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::ChildAccess)


def test_gmfgraph::childaccess_constructor_exists():
    assert callable(gmfgraph::ChildAccess.__init__)


def test_gmfgraph::childaccess_constructor_args():
    sig = inspect.signature(gmfgraph::ChildAccess.__init__)
    params = list(sig.parameters.keys())
    assert "accessor" in params, "Missing parameter 'accessor'"

def test_gmfgraph::childaccess_has_accessor():
    assert hasattr(gmfgraph::ChildAccess, "accessor")
    descriptor = None
    for klass in gmfgraph::ChildAccess.__mro__:
        if "accessor" in klass.__dict__:
            descriptor = klass.__dict__["accessor"]
            break
    assert isinstance(descriptor, property)



def test_layoutable_is_not_abstract():
    assert not inspect.isabstract(Layoutable)


def test_layoutable_constructor_exists():
    assert callable(Layoutable.__init__)


def test_layoutable_constructor_args():
    sig = inspect.signature(Layoutable.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::figure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Figure)


def test_gmfgraph::figure_constructor_exists():
    assert callable(gmfgraph::Figure.__init__)


def test_gmfgraph::figure_constructor_args():
    sig = inspect.signature(gmfgraph::Figure.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::dimension_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Dimension)


def test_gmfgraph::dimension_constructor_exists():
    assert callable(gmfgraph::Dimension.__init__)


def test_gmfgraph::dimension_constructor_args():
    sig = inspect.signature(gmfgraph::Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "dx" in params, "Missing parameter 'dx'"
    assert "dy" in params, "Missing parameter 'dy'"

def test_gmfgraph::dimension_has_dx():
    assert hasattr(gmfgraph::Dimension, "dx")
    descriptor = None
    for klass in gmfgraph::Dimension.__mro__:
        if "dx" in klass.__dict__:
            descriptor = klass.__dict__["dx"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::dimension_has_dy():
    assert hasattr(gmfgraph::Dimension, "dy")
    descriptor = None
    for klass in gmfgraph::Dimension.__mro__:
        if "dy" in klass.__dict__:
            descriptor = klass.__dict__["dy"]
            break
    assert isinstance(descriptor, property)



def test_visualfacet_is_not_abstract():
    assert not inspect.isabstract(VisualFacet)


def test_visualfacet_constructor_exists():
    assert callable(VisualFacet.__init__)


def test_visualfacet_constructor_args():
    sig = inspect.signature(VisualFacet.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::alignmentfacet_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::AlignmentFacet)


def test_gmfgraph::alignmentfacet_constructor_exists():
    assert callable(gmfgraph::AlignmentFacet.__init__)


def test_gmfgraph::alignmentfacet_constructor_args():
    sig = inspect.signature(gmfgraph::AlignmentFacet.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_gmfgraph::alignmentfacet_has_alignment():
    assert hasattr(gmfgraph::AlignmentFacet, "alignment")
    descriptor = None
    for klass in gmfgraph::AlignmentFacet.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::labeloffsetfacet_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::LabelOffsetFacet)


def test_gmfgraph::labeloffsetfacet_constructor_exists():
    assert callable(gmfgraph::LabelOffsetFacet.__init__)


def test_gmfgraph::labeloffsetfacet_constructor_args():
    sig = inspect.signature(gmfgraph::LabelOffsetFacet.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_gmfgraph::labeloffsetfacet_has_x():
    assert hasattr(gmfgraph::LabelOffsetFacet, "x")
    descriptor = None
    for klass in gmfgraph::LabelOffsetFacet.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::labeloffsetfacet_has_y():
    assert hasattr(gmfgraph::LabelOffsetFacet, "y")
    descriptor = None
    for klass in gmfgraph::LabelOffsetFacet.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::defaultsizefacet_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::DefaultSizeFacet)


def test_gmfgraph::defaultsizefacet_constructor_exists():
    assert callable(gmfgraph::DefaultSizeFacet.__init__)


def test_gmfgraph::defaultsizefacet_constructor_args():
    sig = inspect.signature(gmfgraph::DefaultSizeFacet.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::gradientfacet_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::GradientFacet)


def test_gmfgraph::gradientfacet_constructor_exists():
    assert callable(gmfgraph::GradientFacet.__init__)


def test_gmfgraph::gradientfacet_constructor_args():
    sig = inspect.signature(gmfgraph::GradientFacet.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_gmfgraph::gradientfacet_has_direction():
    assert hasattr(gmfgraph::GradientFacet, "direction")
    descriptor = None
    for klass in gmfgraph::GradientFacet.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::generalfacet_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::GeneralFacet)


def test_gmfgraph::generalfacet_constructor_exists():
    assert callable(gmfgraph::GeneralFacet.__init__)


def test_gmfgraph::generalfacet_constructor_args():
    sig = inspect.signature(gmfgraph::GeneralFacet.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_gmfgraph::generalfacet_has_data():
    assert hasattr(gmfgraph::GeneralFacet, "data")
    descriptor = None
    for klass in gmfgraph::GeneralFacet.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::generalfacet_has_identifier():
    assert hasattr(gmfgraph::GeneralFacet, "identifier")
    descriptor = None
    for klass in gmfgraph::GeneralFacet.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_abstractnode_is_not_abstract():
    assert not inspect.isabstract(AbstractNode)


def test_abstractnode_constructor_exists():
    assert callable(AbstractNode.__init__)


def test_abstractnode_constructor_args():
    sig = inspect.signature(AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::node_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Node)


def test_gmfgraph::node_constructor_exists():
    assert callable(gmfgraph::Node.__init__)


def test_gmfgraph::node_constructor_args():
    sig = inspect.signature(gmfgraph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "affixedParentSide" in params, "Missing parameter 'affixedParentSide'"
    assert "resizeConstraint" in params, "Missing parameter 'resizeConstraint'"

def test_gmfgraph::node_has_affixedParentSide():
    assert hasattr(gmfgraph::Node, "affixedParentSide")
    descriptor = None
    for klass in gmfgraph::Node.__mro__:
        if "affixedParentSide" in klass.__dict__:
            descriptor = klass.__dict__["affixedParentSide"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::node_has_resizeConstraint():
    assert hasattr(gmfgraph::Node, "resizeConstraint")
    descriptor = None
    for klass in gmfgraph::Node.__mro__:
        if "resizeConstraint" in klass.__dict__:
            descriptor = klass.__dict__["resizeConstraint"]
            break
    assert isinstance(descriptor, property)



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::connection_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Connection)


def test_gmfgraph::connection_constructor_exists():
    assert callable(gmfgraph::Connection.__init__)


def test_gmfgraph::connection_constructor_args():
    sig = inspect.signature(gmfgraph::Connection.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::abstractnode_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::AbstractNode)


def test_gmfgraph::abstractnode_constructor_exists():
    assert callable(gmfgraph::AbstractNode.__init__)


def test_gmfgraph::abstractnode_constructor_args():
    sig = inspect.signature(gmfgraph::AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::visualfacet_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::VisualFacet)


def test_gmfgraph::visualfacet_constructor_exists():
    assert callable(gmfgraph::VisualFacet.__init__)


def test_gmfgraph::visualfacet_constructor_args():
    sig = inspect.signature(gmfgraph::VisualFacet.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::identity_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Identity)


def test_gmfgraph::identity_constructor_exists():
    assert callable(gmfgraph::Identity.__init__)


def test_gmfgraph::identity_constructor_args():
    sig = inspect.signature(gmfgraph::Identity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gmfgraph::identity_has_name():
    assert hasattr(gmfgraph::Identity, "name")
    descriptor = None
    for klass in gmfgraph::Identity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::realfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::RealFigure)


def test_gmfgraph::realfigure_constructor_exists():
    assert callable(gmfgraph::RealFigure.__init__)


def test_gmfgraph::realfigure_constructor_args():
    sig = inspect.signature(gmfgraph::RealFigure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gmfgraph::realfigure_has_name():
    assert hasattr(gmfgraph::RealFigure, "name")
    descriptor = None
    for klass in gmfgraph::RealFigure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::diagramlabel_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::DiagramLabel)


def test_gmfgraph::diagramlabel_constructor_exists():
    assert callable(gmfgraph::DiagramLabel.__init__)


def test_gmfgraph::diagramlabel_constructor_args():
    sig = inspect.signature(gmfgraph::DiagramLabel.__init__)
    params = list(sig.parameters.keys())
    assert "external" in params, "Missing parameter 'external'"
    assert "elementIcon" in params, "Missing parameter 'elementIcon'"

def test_gmfgraph::diagramlabel_has_external():
    assert hasattr(gmfgraph::DiagramLabel, "external")
    descriptor = None
    for klass in gmfgraph::DiagramLabel.__mro__:
        if "external" in klass.__dict__:
            descriptor = klass.__dict__["external"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::diagramlabel_has_elementIcon():
    assert hasattr(gmfgraph::DiagramLabel, "elementIcon")
    descriptor = None
    for klass in gmfgraph::DiagramLabel.__mro__:
        if "elementIcon" in klass.__dict__:
            descriptor = klass.__dict__["elementIcon"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::compartment_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Compartment)


def test_gmfgraph::compartment_constructor_exists():
    assert callable(gmfgraph::Compartment.__init__)


def test_gmfgraph::compartment_constructor_args():
    sig = inspect.signature(gmfgraph::Compartment.__init__)
    params = list(sig.parameters.keys())
    assert "collapsible" in params, "Missing parameter 'collapsible'"
    assert "needsTitle" in params, "Missing parameter 'needsTitle'"

def test_gmfgraph::compartment_has_collapsible():
    assert hasattr(gmfgraph::Compartment, "collapsible")
    descriptor = None
    for klass in gmfgraph::Compartment.__mro__:
        if "collapsible" in klass.__dict__:
            descriptor = klass.__dict__["collapsible"]
            break
    assert isinstance(descriptor, property)

def test_gmfgraph::compartment_has_needsTitle():
    assert hasattr(gmfgraph::Compartment, "needsTitle")
    descriptor = None
    for klass in gmfgraph::Compartment.__mro__:
        if "needsTitle" in klass.__dict__:
            descriptor = klass.__dict__["needsTitle"]
            break
    assert isinstance(descriptor, property)



def test_identity_is_not_abstract():
    assert not inspect.isabstract(Identity)


def test_identity_constructor_exists():
    assert callable(Identity.__init__)


def test_identity_constructor_args():
    sig = inspect.signature(Identity.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::figuredescriptor_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::FigureDescriptor)


def test_gmfgraph::figuredescriptor_constructor_exists():
    assert callable(gmfgraph::FigureDescriptor.__init__)


def test_gmfgraph::figuredescriptor_constructor_args():
    sig = inspect.signature(gmfgraph::FigureDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::diagramelement_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::DiagramElement)


def test_gmfgraph::diagramelement_constructor_exists():
    assert callable(gmfgraph::DiagramElement.__init__)


def test_gmfgraph::diagramelement_constructor_args():
    sig = inspect.signature(gmfgraph::DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::figuregallery_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::FigureGallery)


def test_gmfgraph::figuregallery_constructor_exists():
    assert callable(gmfgraph::FigureGallery.__init__)


def test_gmfgraph::figuregallery_constructor_args():
    sig = inspect.signature(gmfgraph::FigureGallery.__init__)
    params = list(sig.parameters.keys())
    assert "implementationBundle" in params, "Missing parameter 'implementationBundle'"

def test_gmfgraph::figuregallery_has_implementationBundle():
    assert hasattr(gmfgraph::FigureGallery, "implementationBundle")
    descriptor = None
    for klass in gmfgraph::FigureGallery.__mro__:
        if "implementationBundle" in klass.__dict__:
            descriptor = klass.__dict__["implementationBundle"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::canvas_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Canvas)


def test_gmfgraph::canvas_constructor_exists():
    assert callable(gmfgraph::Canvas.__init__)


def test_gmfgraph::canvas_constructor_args():
    sig = inspect.signature(gmfgraph::Canvas.__init__)
    params = list(sig.parameters.keys())

def test_colorconstants_exists():
    # Check that the Enumeration exists
    assert ColorConstants is not None

def test_colorconstants_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColorConstants]
    expected_literals = [
        "gray",
        "yellow",
        "darkGray",
        "white",
        "black",
        "red",
        "lightGray",
        "lightGreen",
        "cyan",
        "green",
        "darkGreen",
        "orange",
        "blue",
        "lightBlue",
        "darkBlue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColorConstants"

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "SOUTH",
        "EAST",
        "SOUTH_EAST",
        "NORTH_EAST",
        "NORTH_WEST",
        "NORTH_SOUTH",
        "NORTH",
        "NONE",
        "SOUTH_WEST",
        "NSEW",
        "WEST",
        "EAST_WEST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_linekind_exists():
    # Check that the Enumeration exists
    assert LineKind is not None

def test_linekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineKind]
    expected_literals = [
        "LINE_DASH",
        "LINE_DASHDOTDOT",
        "LINE_DASHDOT",
        "LINE_SOLID",
        "LINE_DOT",
        "LINE_CUSTOM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineKind"

def test_fontstyle_exists():
    # Check that the Enumeration exists
    assert FontStyle is not None

def test_fontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontStyle]
    expected_literals = [
        "ITALIC",
        "NORMAL",
        "BOLD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontStyle"

def test_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "FILL",
        "END",
        "CENTER",
        "BEGINNING",
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
Layout_strategy = st.builds(
    Layout,
)
gmfgraph::FlowLayout_strategy = st.builds(
    gmfgraph::FlowLayout,
    majorSpacing=
        st.integers(),
    majorAlignment=
        safe_text,
    forceSingleLine=
        st.booleans(),
    matchMinorSize=
        st.booleans(),
    vertical=
        st.booleans(),
    minorAlignment=
        safe_text,
    minorSpacing=
        st.integers()
)
gmfgraph::StackLayout_strategy = st.builds(
    gmfgraph::StackLayout,
)
gmfgraph::GridLayout_strategy = st.builds(
    gmfgraph::GridLayout,
    equalWidth=
        st.booleans(),
    numColumns=
        st.integers()
)
gmfgraph::BorderLayout_strategy = st.builds(
    gmfgraph::BorderLayout,
)
gmfgraph::XYLayout_strategy = st.builds(
    gmfgraph::XYLayout,
)
gmfgraph::Layout_strategy = st.builds(
    gmfgraph::Layout,
)
LayoutData_strategy = st.builds(
    LayoutData,
)
gmfgraph::BorderLayoutData_strategy = st.builds(
    gmfgraph::BorderLayoutData,
    vertical=
        st.booleans(),
    alignment=
        safe_text
)
gmfgraph::XYLayoutData_strategy = st.builds(
    gmfgraph::XYLayoutData,
)
gmfgraph::GridLayoutData_strategy = st.builds(
    gmfgraph::GridLayoutData,
    grabExcessHorizontalSpace=
        st.booleans(),
    horizontalIndent=
        st.integers(),
    verticalSpan=
        st.integers(),
    grabExcessVerticalSpace=
        st.booleans(),
    horizontalAlignment=
        safe_text,
    verticalAlignment=
        safe_text,
    horizontalSpan=
        st.integers()
)
gmfgraph::Layoutable_strategy = st.builds(
    gmfgraph::Layoutable,
)
gmfgraph::LayoutData_strategy = st.builds(
    gmfgraph::LayoutData,
)
Font_strategy = st.builds(
    Font,
)
gmfgraph::BasicFont_strategy = st.builds(
    gmfgraph::BasicFont,
    style=
        safe_text,
    faceName=
        safe_text,
    height=
        st.integers()
)
Border_strategy = st.builds(
    Border,
)
gmfgraph::CompoundBorder_strategy = st.builds(
    gmfgraph::CompoundBorder,
)
gmfgraph::MarginBorder_strategy = st.builds(
    gmfgraph::MarginBorder,
)
gmfgraph::LineBorder_strategy = st.builds(
    gmfgraph::LineBorder,
    width=
        st.integers()
)
gmfgraph::FigureAccessor_strategy = st.builds(
    gmfgraph::FigureAccessor,
    accessor=
        safe_text
)
Color_strategy = st.builds(
    Color,
)
gmfgraph::ConstantColor_strategy = st.builds(
    gmfgraph::ConstantColor,
    value=
        safe_text
)
gmfgraph::RGBColor_strategy = st.builds(
    gmfgraph::RGBColor,
    blue=
        st.integers(),
    green=
        st.integers(),
    red=
        st.integers()
)
CustomFigure_strategy = st.builds(
    CustomFigure,
)
CustomClass_strategy = st.builds(
    CustomClass,
)
gmfgraph::CustomLayout_strategy = st.builds(
    gmfgraph::CustomLayout,
)
gmfgraph::CustomLayoutData_strategy = st.builds(
    gmfgraph::CustomLayoutData,
)
gmfgraph::CustomBorder_strategy = st.builds(
    gmfgraph::CustomBorder,
)
gmfgraph::CustomAttribute_strategy = st.builds(
    gmfgraph::CustomAttribute,
    multiStatementValue=
        st.booleans(),
    directAccess=
        st.booleans(),
    name=
        safe_text,
    value=
        safe_text
)
gmfgraph::CustomClass_strategy = st.builds(
    gmfgraph::CustomClass,
    qualifiedClassName=
        safe_text
)
DecorationFigure_strategy = st.builds(
    DecorationFigure,
)
gmfgraph::CustomDecoration_strategy = st.builds(
    gmfgraph::CustomDecoration,
)
ConnectionFigure_strategy = st.builds(
    ConnectionFigure,
)
gmfgraph::CustomConnection_strategy = st.builds(
    gmfgraph::CustomConnection,
)
Polygon_strategy = st.builds(
    Polygon,
)
gmfgraph::PolygonDecoration_strategy = st.builds(
    gmfgraph::PolygonDecoration,
)
gmfgraph::ScalablePolygon_strategy = st.builds(
    gmfgraph::ScalablePolygon,
)
Polyline_strategy = st.builds(
    Polyline,
)
gmfgraph::PolylineConnection_strategy = st.builds(
    gmfgraph::PolylineConnection,
)
gmfgraph::PolylineDecoration_strategy = st.builds(
    gmfgraph::PolylineDecoration,
)
gmfgraph::Polygon_strategy = st.builds(
    gmfgraph::Polygon,
)
AbstractFigure_strategy = st.builds(
    AbstractFigure,
)
Shape_strategy = st.builds(
    Shape,
)
gmfgraph::Ellipse_strategy = st.builds(
    gmfgraph::Ellipse,
)
gmfgraph::Polyline_strategy = st.builds(
    gmfgraph::Polyline,
)
gmfgraph::RoundedRectangle_strategy = st.builds(
    gmfgraph::RoundedRectangle,
    cornerWidth=
        st.integers(),
    cornerHeight=
        st.integers()
)
gmfgraph::Rectangle_strategy = st.builds(
    gmfgraph::Rectangle,
)
RealFigure_strategy = st.builds(
    RealFigure,
)
gmfgraph::DecorationFigure_strategy = st.builds(
    gmfgraph::DecorationFigure,
)
gmfgraph::CustomFigure_strategy = st.builds(
    gmfgraph::CustomFigure,
)
gmfgraph::LabeledContainer_strategy = st.builds(
    gmfgraph::LabeledContainer,
)
gmfgraph::Shape_strategy = st.builds(
    gmfgraph::Shape,
    lineWidth=
        st.integers(),
    fill=
        st.booleans(),
    xorFill=
        st.booleans(),
    outline=
        st.booleans(),
    lineKind=
        safe_text,
    xorOutline=
        st.booleans()
)
gmfgraph::Label_strategy = st.builds(
    gmfgraph::Label,
    text=
        safe_text
)
gmfgraph::ConnectionFigure_strategy = st.builds(
    gmfgraph::ConnectionFigure,
)
gmfgraph::FigureRef_strategy = st.builds(
    gmfgraph::FigureRef,
)
gmfgraph::Color_strategy = st.builds(
    gmfgraph::Color,
)
Figure_strategy = st.builds(
    Figure,
)
gmfgraph::AbstractFigure_strategy = st.builds(
    gmfgraph::AbstractFigure,
)
gmfgraph::Point_strategy = st.builds(
    gmfgraph::Point,
    y=
        st.integers(),
    x=
        st.integers()
)
gmfgraph::Border_strategy = st.builds(
    gmfgraph::Border,
)
gmfgraph::Insets_strategy = st.builds(
    gmfgraph::Insets,
    left=
        st.integers(),
    bottom=
        st.integers(),
    top=
        st.integers(),
    right=
        st.integers()
)
gmfgraph::Font_strategy = st.builds(
    gmfgraph::Font,
)
gmfgraph::ChildAccess_strategy = st.builds(
    gmfgraph::ChildAccess,
    accessor=
        safe_text
)
Layoutable_strategy = st.builds(
    Layoutable,
)
gmfgraph::Figure_strategy = st.builds(
    gmfgraph::Figure,
)
gmfgraph::Dimension_strategy = st.builds(
    gmfgraph::Dimension,
    dx=
        st.integers(),
    dy=
        st.integers()
)
VisualFacet_strategy = st.builds(
    VisualFacet,
)
gmfgraph::AlignmentFacet_strategy = st.builds(
    gmfgraph::AlignmentFacet,
    alignment=
        safe_text
)
gmfgraph::LabelOffsetFacet_strategy = st.builds(
    gmfgraph::LabelOffsetFacet,
    x=
        st.integers(),
    y=
        st.integers()
)
gmfgraph::DefaultSizeFacet_strategy = st.builds(
    gmfgraph::DefaultSizeFacet,
)
gmfgraph::GradientFacet_strategy = st.builds(
    gmfgraph::GradientFacet,
    direction=
        safe_text
)
gmfgraph::GeneralFacet_strategy = st.builds(
    gmfgraph::GeneralFacet,
    data=
        safe_text,
    identifier=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
gmfgraph::Node_strategy = st.builds(
    gmfgraph::Node,
    affixedParentSide=
        safe_text,
    resizeConstraint=
        safe_text
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
gmfgraph::Connection_strategy = st.builds(
    gmfgraph::Connection,
)
gmfgraph::AbstractNode_strategy = st.builds(
    gmfgraph::AbstractNode,
)
gmfgraph::VisualFacet_strategy = st.builds(
    gmfgraph::VisualFacet,
)
gmfgraph::Identity_strategy = st.builds(
    gmfgraph::Identity,
    name=
        safe_text
)
gmfgraph::RealFigure_strategy = st.builds(
    gmfgraph::RealFigure,
    name=
        safe_text
)
gmfgraph::DiagramLabel_strategy = st.builds(
    gmfgraph::DiagramLabel,
    external=
        st.booleans(),
    elementIcon=
        st.booleans()
)
gmfgraph::Compartment_strategy = st.builds(
    gmfgraph::Compartment,
    collapsible=
        st.booleans(),
    needsTitle=
        st.booleans()
)
Identity_strategy = st.builds(
    Identity,
)
gmfgraph::FigureDescriptor_strategy = st.builds(
    gmfgraph::FigureDescriptor,
)
gmfgraph::DiagramElement_strategy = st.builds(
    gmfgraph::DiagramElement,
)
gmfgraph::FigureGallery_strategy = st.builds(
    gmfgraph::FigureGallery,
    implementationBundle=
        safe_text
)
gmfgraph::Canvas_strategy = st.builds(
    gmfgraph::Canvas,
)

@given(instance=Layout_strategy)
@settings(max_examples=50)
def test_layout_instantiation(instance):
    assert isinstance(instance, Layout)

@given(instance=gmfgraph::FlowLayout_strategy)
@settings(max_examples=50)
def test_gmfgraph::flowlayout_instantiation(instance):
    assert isinstance(instance, gmfgraph::FlowLayout)

@given(instance=gmfgraph::FlowLayout_strategy)
def test_gmfgraph::flowlayout_majorSpacing_type(instance):
    assert isinstance(instance.majorSpacing, int)


@given(instance=gmfgraph::FlowLayout_strategy)
def test_gmfgraph::flowlayout_majorSpacing_setter(instance):
    original = instance.majorSpacing
    instance.majorSpacing = original
    assert instance.majorSpacing == original

@given(instance=gmfgraph::FlowLayout_strategy)
def test_gmfgraph::flowlayout_majorAlignment_type(instance):
    assert isinstance(instance.majorAlignment, str)


@given(instance=gmfgraph::FlowLayout_strategy)
def test_gmfgraph::flowlayout_majorAlignment_setter(instance):
    original = instance.majorAlignment
    instance.majorAlignment = original
    assert instance.majorAlignment == original

@given(instance=gmfgraph::FlowLayout_strategy)
def test_gmfgraph::flowlayout_forceSingleLine_type(instance):
    assert isinstance(instance.forceSingleLine, bool)


@given(instance=gmfgraph::FlowLayout_strategy)
def test_gmfgraph::flowlayout_forceSingleLine_setter(instance):
    original = instance.forceSingleLine
    instance.forceSingleLine = original
    assert instance.forceSingleLine == original

@given(instance=gmfgraph::FlowLayout_strategy)
def test_gmfgraph::flowlayout_matchMinorSize_type(instance):
    assert isinstance(instance.matchMinorSize, bool)


@given(instance=gmfgraph::FlowLayout_strategy)
def test_gmfgraph::flowlayout_matchMinorSize_setter(instance):
    original = instance.matchMinorSize
    instance.matchMinorSize = original
    assert instance.matchMinorSize == original

@given(instance=gmfgraph::FlowLayout_strategy)
def test_gmfgraph::flowlayout_vertical_type(instance):
    assert isinstance(instance.vertical, bool)


@given(instance=gmfgraph::FlowLayout_strategy)
def test_gmfgraph::flowlayout_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original

@given(instance=gmfgraph::FlowLayout_strategy)
def test_gmfgraph::flowlayout_minorAlignment_type(instance):
    assert isinstance(instance.minorAlignment, str)


@given(instance=gmfgraph::FlowLayout_strategy)
def test_gmfgraph::flowlayout_minorAlignment_setter(instance):
    original = instance.minorAlignment
    instance.minorAlignment = original
    assert instance.minorAlignment == original

@given(instance=gmfgraph::FlowLayout_strategy)
def test_gmfgraph::flowlayout_minorSpacing_type(instance):
    assert isinstance(instance.minorSpacing, int)


@given(instance=gmfgraph::FlowLayout_strategy)
def test_gmfgraph::flowlayout_minorSpacing_setter(instance):
    original = instance.minorSpacing
    instance.minorSpacing = original
    assert instance.minorSpacing == original

@given(instance=gmfgraph::StackLayout_strategy)
@settings(max_examples=50)
def test_gmfgraph::stacklayout_instantiation(instance):
    assert isinstance(instance, gmfgraph::StackLayout)

@given(instance=gmfgraph::GridLayout_strategy)
@settings(max_examples=50)
def test_gmfgraph::gridlayout_instantiation(instance):
    assert isinstance(instance, gmfgraph::GridLayout)

@given(instance=gmfgraph::GridLayout_strategy)
def test_gmfgraph::gridlayout_equalWidth_type(instance):
    assert isinstance(instance.equalWidth, bool)


@given(instance=gmfgraph::GridLayout_strategy)
def test_gmfgraph::gridlayout_equalWidth_setter(instance):
    original = instance.equalWidth
    instance.equalWidth = original
    assert instance.equalWidth == original

@given(instance=gmfgraph::GridLayout_strategy)
def test_gmfgraph::gridlayout_numColumns_type(instance):
    assert isinstance(instance.numColumns, int)


@given(instance=gmfgraph::GridLayout_strategy)
def test_gmfgraph::gridlayout_numColumns_setter(instance):
    original = instance.numColumns
    instance.numColumns = original
    assert instance.numColumns == original

@given(instance=gmfgraph::BorderLayout_strategy)
@settings(max_examples=50)
def test_gmfgraph::borderlayout_instantiation(instance):
    assert isinstance(instance, gmfgraph::BorderLayout)

@given(instance=gmfgraph::XYLayout_strategy)
@settings(max_examples=50)
def test_gmfgraph::xylayout_instantiation(instance):
    assert isinstance(instance, gmfgraph::XYLayout)

@given(instance=gmfgraph::Layout_strategy)
@settings(max_examples=50)
def test_gmfgraph::layout_instantiation(instance):
    assert isinstance(instance, gmfgraph::Layout)

@given(instance=LayoutData_strategy)
@settings(max_examples=50)
def test_layoutdata_instantiation(instance):
    assert isinstance(instance, LayoutData)

@given(instance=gmfgraph::BorderLayoutData_strategy)
@settings(max_examples=50)
def test_gmfgraph::borderlayoutdata_instantiation(instance):
    assert isinstance(instance, gmfgraph::BorderLayoutData)

@given(instance=gmfgraph::BorderLayoutData_strategy)
def test_gmfgraph::borderlayoutdata_vertical_type(instance):
    assert isinstance(instance.vertical, bool)


@given(instance=gmfgraph::BorderLayoutData_strategy)
def test_gmfgraph::borderlayoutdata_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original

@given(instance=gmfgraph::BorderLayoutData_strategy)
def test_gmfgraph::borderlayoutdata_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=gmfgraph::BorderLayoutData_strategy)
def test_gmfgraph::borderlayoutdata_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=gmfgraph::XYLayoutData_strategy)
@settings(max_examples=50)
def test_gmfgraph::xylayoutdata_instantiation(instance):
    assert isinstance(instance, gmfgraph::XYLayoutData)

@given(instance=gmfgraph::GridLayoutData_strategy)
@settings(max_examples=50)
def test_gmfgraph::gridlayoutdata_instantiation(instance):
    assert isinstance(instance, gmfgraph::GridLayoutData)

@given(instance=gmfgraph::GridLayoutData_strategy)
def test_gmfgraph::gridlayoutdata_grabExcessHorizontalSpace_type(instance):
    assert isinstance(instance.grabExcessHorizontalSpace, bool)


@given(instance=gmfgraph::GridLayoutData_strategy)
def test_gmfgraph::gridlayoutdata_grabExcessHorizontalSpace_setter(instance):
    original = instance.grabExcessHorizontalSpace
    instance.grabExcessHorizontalSpace = original
    assert instance.grabExcessHorizontalSpace == original

@given(instance=gmfgraph::GridLayoutData_strategy)
def test_gmfgraph::gridlayoutdata_horizontalIndent_type(instance):
    assert isinstance(instance.horizontalIndent, int)


@given(instance=gmfgraph::GridLayoutData_strategy)
def test_gmfgraph::gridlayoutdata_horizontalIndent_setter(instance):
    original = instance.horizontalIndent
    instance.horizontalIndent = original
    assert instance.horizontalIndent == original

@given(instance=gmfgraph::GridLayoutData_strategy)
def test_gmfgraph::gridlayoutdata_verticalSpan_type(instance):
    assert isinstance(instance.verticalSpan, int)


@given(instance=gmfgraph::GridLayoutData_strategy)
def test_gmfgraph::gridlayoutdata_verticalSpan_setter(instance):
    original = instance.verticalSpan
    instance.verticalSpan = original
    assert instance.verticalSpan == original

@given(instance=gmfgraph::GridLayoutData_strategy)
def test_gmfgraph::gridlayoutdata_grabExcessVerticalSpace_type(instance):
    assert isinstance(instance.grabExcessVerticalSpace, bool)


@given(instance=gmfgraph::GridLayoutData_strategy)
def test_gmfgraph::gridlayoutdata_grabExcessVerticalSpace_setter(instance):
    original = instance.grabExcessVerticalSpace
    instance.grabExcessVerticalSpace = original
    assert instance.grabExcessVerticalSpace == original

@given(instance=gmfgraph::GridLayoutData_strategy)
def test_gmfgraph::gridlayoutdata_horizontalAlignment_type(instance):
    assert isinstance(instance.horizontalAlignment, str)


@given(instance=gmfgraph::GridLayoutData_strategy)
def test_gmfgraph::gridlayoutdata_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original

@given(instance=gmfgraph::GridLayoutData_strategy)
def test_gmfgraph::gridlayoutdata_verticalAlignment_type(instance):
    assert isinstance(instance.verticalAlignment, str)


@given(instance=gmfgraph::GridLayoutData_strategy)
def test_gmfgraph::gridlayoutdata_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original

@given(instance=gmfgraph::GridLayoutData_strategy)
def test_gmfgraph::gridlayoutdata_horizontalSpan_type(instance):
    assert isinstance(instance.horizontalSpan, int)


@given(instance=gmfgraph::GridLayoutData_strategy)
def test_gmfgraph::gridlayoutdata_horizontalSpan_setter(instance):
    original = instance.horizontalSpan
    instance.horizontalSpan = original
    assert instance.horizontalSpan == original

@given(instance=gmfgraph::Layoutable_strategy)
@settings(max_examples=50)
def test_gmfgraph::layoutable_instantiation(instance):
    assert isinstance(instance, gmfgraph::Layoutable)

@given(instance=gmfgraph::LayoutData_strategy)
@settings(max_examples=50)
def test_gmfgraph::layoutdata_instantiation(instance):
    assert isinstance(instance, gmfgraph::LayoutData)

@given(instance=Font_strategy)
@settings(max_examples=50)
def test_font_instantiation(instance):
    assert isinstance(instance, Font)

@given(instance=gmfgraph::BasicFont_strategy)
@settings(max_examples=50)
def test_gmfgraph::basicfont_instantiation(instance):
    assert isinstance(instance, gmfgraph::BasicFont)

@given(instance=gmfgraph::BasicFont_strategy)
def test_gmfgraph::basicfont_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=gmfgraph::BasicFont_strategy)
def test_gmfgraph::basicfont_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=gmfgraph::BasicFont_strategy)
def test_gmfgraph::basicfont_faceName_type(instance):
    assert isinstance(instance.faceName, str)


@given(instance=gmfgraph::BasicFont_strategy)
def test_gmfgraph::basicfont_faceName_setter(instance):
    original = instance.faceName
    instance.faceName = original
    assert instance.faceName == original

@given(instance=gmfgraph::BasicFont_strategy)
def test_gmfgraph::basicfont_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=gmfgraph::BasicFont_strategy)
def test_gmfgraph::basicfont_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=Border_strategy)
@settings(max_examples=50)
def test_border_instantiation(instance):
    assert isinstance(instance, Border)

@given(instance=gmfgraph::CompoundBorder_strategy)
@settings(max_examples=50)
def test_gmfgraph::compoundborder_instantiation(instance):
    assert isinstance(instance, gmfgraph::CompoundBorder)

@given(instance=gmfgraph::MarginBorder_strategy)
@settings(max_examples=50)
def test_gmfgraph::marginborder_instantiation(instance):
    assert isinstance(instance, gmfgraph::MarginBorder)

@given(instance=gmfgraph::LineBorder_strategy)
@settings(max_examples=50)
def test_gmfgraph::lineborder_instantiation(instance):
    assert isinstance(instance, gmfgraph::LineBorder)

@given(instance=gmfgraph::LineBorder_strategy)
def test_gmfgraph::lineborder_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=gmfgraph::LineBorder_strategy)
def test_gmfgraph::lineborder_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=gmfgraph::FigureAccessor_strategy)
@settings(max_examples=50)
def test_gmfgraph::figureaccessor_instantiation(instance):
    assert isinstance(instance, gmfgraph::FigureAccessor)

@given(instance=gmfgraph::FigureAccessor_strategy)
def test_gmfgraph::figureaccessor_accessor_type(instance):
    assert isinstance(instance.accessor, str)


@given(instance=gmfgraph::FigureAccessor_strategy)
def test_gmfgraph::figureaccessor_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original

@given(instance=Color_strategy)
@settings(max_examples=50)
def test_color_instantiation(instance):
    assert isinstance(instance, Color)

@given(instance=gmfgraph::ConstantColor_strategy)
@settings(max_examples=50)
def test_gmfgraph::constantcolor_instantiation(instance):
    assert isinstance(instance, gmfgraph::ConstantColor)

@given(instance=gmfgraph::ConstantColor_strategy)
def test_gmfgraph::constantcolor_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=gmfgraph::ConstantColor_strategy)
def test_gmfgraph::constantcolor_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gmfgraph::RGBColor_strategy)
@settings(max_examples=50)
def test_gmfgraph::rgbcolor_instantiation(instance):
    assert isinstance(instance, gmfgraph::RGBColor)

@given(instance=gmfgraph::RGBColor_strategy)
def test_gmfgraph::rgbcolor_blue_type(instance):
    assert isinstance(instance.blue, int)


@given(instance=gmfgraph::RGBColor_strategy)
def test_gmfgraph::rgbcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

@given(instance=gmfgraph::RGBColor_strategy)
def test_gmfgraph::rgbcolor_green_type(instance):
    assert isinstance(instance.green, int)


@given(instance=gmfgraph::RGBColor_strategy)
def test_gmfgraph::rgbcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original

@given(instance=gmfgraph::RGBColor_strategy)
def test_gmfgraph::rgbcolor_red_type(instance):
    assert isinstance(instance.red, int)


@given(instance=gmfgraph::RGBColor_strategy)
def test_gmfgraph::rgbcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=CustomFigure_strategy)
@settings(max_examples=50)
def test_customfigure_instantiation(instance):
    assert isinstance(instance, CustomFigure)

@given(instance=CustomClass_strategy)
@settings(max_examples=50)
def test_customclass_instantiation(instance):
    assert isinstance(instance, CustomClass)

@given(instance=gmfgraph::CustomLayout_strategy)
@settings(max_examples=50)
def test_gmfgraph::customlayout_instantiation(instance):
    assert isinstance(instance, gmfgraph::CustomLayout)

@given(instance=gmfgraph::CustomLayoutData_strategy)
@settings(max_examples=50)
def test_gmfgraph::customlayoutdata_instantiation(instance):
    assert isinstance(instance, gmfgraph::CustomLayoutData)

@given(instance=gmfgraph::CustomBorder_strategy)
@settings(max_examples=50)
def test_gmfgraph::customborder_instantiation(instance):
    assert isinstance(instance, gmfgraph::CustomBorder)

@given(instance=gmfgraph::CustomAttribute_strategy)
@settings(max_examples=50)
def test_gmfgraph::customattribute_instantiation(instance):
    assert isinstance(instance, gmfgraph::CustomAttribute)

@given(instance=gmfgraph::CustomAttribute_strategy)
def test_gmfgraph::customattribute_multiStatementValue_type(instance):
    assert isinstance(instance.multiStatementValue, bool)


@given(instance=gmfgraph::CustomAttribute_strategy)
def test_gmfgraph::customattribute_multiStatementValue_setter(instance):
    original = instance.multiStatementValue
    instance.multiStatementValue = original
    assert instance.multiStatementValue == original

@given(instance=gmfgraph::CustomAttribute_strategy)
def test_gmfgraph::customattribute_directAccess_type(instance):
    assert isinstance(instance.directAccess, bool)


@given(instance=gmfgraph::CustomAttribute_strategy)
def test_gmfgraph::customattribute_directAccess_setter(instance):
    original = instance.directAccess
    instance.directAccess = original
    assert instance.directAccess == original

@given(instance=gmfgraph::CustomAttribute_strategy)
def test_gmfgraph::customattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gmfgraph::CustomAttribute_strategy)
def test_gmfgraph::customattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gmfgraph::CustomAttribute_strategy)
def test_gmfgraph::customattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=gmfgraph::CustomAttribute_strategy)
def test_gmfgraph::customattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gmfgraph::CustomClass_strategy)
@settings(max_examples=50)
def test_gmfgraph::customclass_instantiation(instance):
    assert isinstance(instance, gmfgraph::CustomClass)

@given(instance=gmfgraph::CustomClass_strategy)
def test_gmfgraph::customclass_qualifiedClassName_type(instance):
    assert isinstance(instance.qualifiedClassName, str)


@given(instance=gmfgraph::CustomClass_strategy)
def test_gmfgraph::customclass_qualifiedClassName_setter(instance):
    original = instance.qualifiedClassName
    instance.qualifiedClassName = original
    assert instance.qualifiedClassName == original

@given(instance=DecorationFigure_strategy)
@settings(max_examples=50)
def test_decorationfigure_instantiation(instance):
    assert isinstance(instance, DecorationFigure)

@given(instance=gmfgraph::CustomDecoration_strategy)
@settings(max_examples=50)
def test_gmfgraph::customdecoration_instantiation(instance):
    assert isinstance(instance, gmfgraph::CustomDecoration)

@given(instance=ConnectionFigure_strategy)
@settings(max_examples=50)
def test_connectionfigure_instantiation(instance):
    assert isinstance(instance, ConnectionFigure)

@given(instance=gmfgraph::CustomConnection_strategy)
@settings(max_examples=50)
def test_gmfgraph::customconnection_instantiation(instance):
    assert isinstance(instance, gmfgraph::CustomConnection)

@given(instance=Polygon_strategy)
@settings(max_examples=50)
def test_polygon_instantiation(instance):
    assert isinstance(instance, Polygon)

@given(instance=gmfgraph::PolygonDecoration_strategy)
@settings(max_examples=50)
def test_gmfgraph::polygondecoration_instantiation(instance):
    assert isinstance(instance, gmfgraph::PolygonDecoration)

@given(instance=gmfgraph::ScalablePolygon_strategy)
@settings(max_examples=50)
def test_gmfgraph::scalablepolygon_instantiation(instance):
    assert isinstance(instance, gmfgraph::ScalablePolygon)

@given(instance=Polyline_strategy)
@settings(max_examples=50)
def test_polyline_instantiation(instance):
    assert isinstance(instance, Polyline)

@given(instance=gmfgraph::PolylineConnection_strategy)
@settings(max_examples=50)
def test_gmfgraph::polylineconnection_instantiation(instance):
    assert isinstance(instance, gmfgraph::PolylineConnection)

@given(instance=gmfgraph::PolylineDecoration_strategy)
@settings(max_examples=50)
def test_gmfgraph::polylinedecoration_instantiation(instance):
    assert isinstance(instance, gmfgraph::PolylineDecoration)

@given(instance=gmfgraph::Polygon_strategy)
@settings(max_examples=50)
def test_gmfgraph::polygon_instantiation(instance):
    assert isinstance(instance, gmfgraph::Polygon)

@given(instance=AbstractFigure_strategy)
@settings(max_examples=50)
def test_abstractfigure_instantiation(instance):
    assert isinstance(instance, AbstractFigure)

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=gmfgraph::Ellipse_strategy)
@settings(max_examples=50)
def test_gmfgraph::ellipse_instantiation(instance):
    assert isinstance(instance, gmfgraph::Ellipse)

@given(instance=gmfgraph::Polyline_strategy)
@settings(max_examples=50)
def test_gmfgraph::polyline_instantiation(instance):
    assert isinstance(instance, gmfgraph::Polyline)

@given(instance=gmfgraph::RoundedRectangle_strategy)
@settings(max_examples=50)
def test_gmfgraph::roundedrectangle_instantiation(instance):
    assert isinstance(instance, gmfgraph::RoundedRectangle)

@given(instance=gmfgraph::RoundedRectangle_strategy)
def test_gmfgraph::roundedrectangle_cornerWidth_type(instance):
    assert isinstance(instance.cornerWidth, int)


@given(instance=gmfgraph::RoundedRectangle_strategy)
def test_gmfgraph::roundedrectangle_cornerWidth_setter(instance):
    original = instance.cornerWidth
    instance.cornerWidth = original
    assert instance.cornerWidth == original

@given(instance=gmfgraph::RoundedRectangle_strategy)
def test_gmfgraph::roundedrectangle_cornerHeight_type(instance):
    assert isinstance(instance.cornerHeight, int)


@given(instance=gmfgraph::RoundedRectangle_strategy)
def test_gmfgraph::roundedrectangle_cornerHeight_setter(instance):
    original = instance.cornerHeight
    instance.cornerHeight = original
    assert instance.cornerHeight == original

@given(instance=gmfgraph::Rectangle_strategy)
@settings(max_examples=50)
def test_gmfgraph::rectangle_instantiation(instance):
    assert isinstance(instance, gmfgraph::Rectangle)

@given(instance=RealFigure_strategy)
@settings(max_examples=50)
def test_realfigure_instantiation(instance):
    assert isinstance(instance, RealFigure)

@given(instance=gmfgraph::DecorationFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph::decorationfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph::DecorationFigure)

@given(instance=gmfgraph::CustomFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph::customfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph::CustomFigure)

@given(instance=gmfgraph::LabeledContainer_strategy)
@settings(max_examples=50)
def test_gmfgraph::labeledcontainer_instantiation(instance):
    assert isinstance(instance, gmfgraph::LabeledContainer)

@given(instance=gmfgraph::Shape_strategy)
@settings(max_examples=50)
def test_gmfgraph::shape_instantiation(instance):
    assert isinstance(instance, gmfgraph::Shape)

@given(instance=gmfgraph::Shape_strategy)
def test_gmfgraph::shape_lineWidth_type(instance):
    assert isinstance(instance.lineWidth, int)


@given(instance=gmfgraph::Shape_strategy)
def test_gmfgraph::shape_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=gmfgraph::Shape_strategy)
def test_gmfgraph::shape_fill_type(instance):
    assert isinstance(instance.fill, bool)


@given(instance=gmfgraph::Shape_strategy)
def test_gmfgraph::shape_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original

@given(instance=gmfgraph::Shape_strategy)
def test_gmfgraph::shape_xorFill_type(instance):
    assert isinstance(instance.xorFill, bool)


@given(instance=gmfgraph::Shape_strategy)
def test_gmfgraph::shape_xorFill_setter(instance):
    original = instance.xorFill
    instance.xorFill = original
    assert instance.xorFill == original

@given(instance=gmfgraph::Shape_strategy)
def test_gmfgraph::shape_outline_type(instance):
    assert isinstance(instance.outline, bool)


@given(instance=gmfgraph::Shape_strategy)
def test_gmfgraph::shape_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original

@given(instance=gmfgraph::Shape_strategy)
def test_gmfgraph::shape_lineKind_type(instance):
    assert isinstance(instance.lineKind, str)


@given(instance=gmfgraph::Shape_strategy)
def test_gmfgraph::shape_lineKind_setter(instance):
    original = instance.lineKind
    instance.lineKind = original
    assert instance.lineKind == original

@given(instance=gmfgraph::Shape_strategy)
def test_gmfgraph::shape_xorOutline_type(instance):
    assert isinstance(instance.xorOutline, bool)


@given(instance=gmfgraph::Shape_strategy)
def test_gmfgraph::shape_xorOutline_setter(instance):
    original = instance.xorOutline
    instance.xorOutline = original
    assert instance.xorOutline == original

@given(instance=gmfgraph::Label_strategy)
@settings(max_examples=50)
def test_gmfgraph::label_instantiation(instance):
    assert isinstance(instance, gmfgraph::Label)

@given(instance=gmfgraph::Label_strategy)
def test_gmfgraph::label_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=gmfgraph::Label_strategy)
def test_gmfgraph::label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=gmfgraph::ConnectionFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph::connectionfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph::ConnectionFigure)

@given(instance=gmfgraph::FigureRef_strategy)
@settings(max_examples=50)
def test_gmfgraph::figureref_instantiation(instance):
    assert isinstance(instance, gmfgraph::FigureRef)

@given(instance=gmfgraph::Color_strategy)
@settings(max_examples=50)
def test_gmfgraph::color_instantiation(instance):
    assert isinstance(instance, gmfgraph::Color)

@given(instance=Figure_strategy)
@settings(max_examples=50)
def test_figure_instantiation(instance):
    assert isinstance(instance, Figure)

@given(instance=gmfgraph::AbstractFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph::abstractfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph::AbstractFigure)

@given(instance=gmfgraph::Point_strategy)
@settings(max_examples=50)
def test_gmfgraph::point_instantiation(instance):
    assert isinstance(instance, gmfgraph::Point)

@given(instance=gmfgraph::Point_strategy)
def test_gmfgraph::point_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=gmfgraph::Point_strategy)
def test_gmfgraph::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=gmfgraph::Point_strategy)
def test_gmfgraph::point_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=gmfgraph::Point_strategy)
def test_gmfgraph::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=gmfgraph::Border_strategy)
@settings(max_examples=50)
def test_gmfgraph::border_instantiation(instance):
    assert isinstance(instance, gmfgraph::Border)

@given(instance=gmfgraph::Insets_strategy)
@settings(max_examples=50)
def test_gmfgraph::insets_instantiation(instance):
    assert isinstance(instance, gmfgraph::Insets)

@given(instance=gmfgraph::Insets_strategy)
def test_gmfgraph::insets_left_type(instance):
    assert isinstance(instance.left, int)


@given(instance=gmfgraph::Insets_strategy)
def test_gmfgraph::insets_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original

@given(instance=gmfgraph::Insets_strategy)
def test_gmfgraph::insets_bottom_type(instance):
    assert isinstance(instance.bottom, int)


@given(instance=gmfgraph::Insets_strategy)
def test_gmfgraph::insets_bottom_setter(instance):
    original = instance.bottom
    instance.bottom = original
    assert instance.bottom == original

@given(instance=gmfgraph::Insets_strategy)
def test_gmfgraph::insets_top_type(instance):
    assert isinstance(instance.top, int)


@given(instance=gmfgraph::Insets_strategy)
def test_gmfgraph::insets_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original

@given(instance=gmfgraph::Insets_strategy)
def test_gmfgraph::insets_right_type(instance):
    assert isinstance(instance.right, int)


@given(instance=gmfgraph::Insets_strategy)
def test_gmfgraph::insets_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=gmfgraph::Font_strategy)
@settings(max_examples=50)
def test_gmfgraph::font_instantiation(instance):
    assert isinstance(instance, gmfgraph::Font)

@given(instance=gmfgraph::ChildAccess_strategy)
@settings(max_examples=50)
def test_gmfgraph::childaccess_instantiation(instance):
    assert isinstance(instance, gmfgraph::ChildAccess)

@given(instance=gmfgraph::ChildAccess_strategy)
def test_gmfgraph::childaccess_accessor_type(instance):
    assert isinstance(instance.accessor, str)


@given(instance=gmfgraph::ChildAccess_strategy)
def test_gmfgraph::childaccess_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original

@given(instance=Layoutable_strategy)
@settings(max_examples=50)
def test_layoutable_instantiation(instance):
    assert isinstance(instance, Layoutable)

@given(instance=gmfgraph::Figure_strategy)
@settings(max_examples=50)
def test_gmfgraph::figure_instantiation(instance):
    assert isinstance(instance, gmfgraph::Figure)

@given(instance=gmfgraph::Dimension_strategy)
@settings(max_examples=50)
def test_gmfgraph::dimension_instantiation(instance):
    assert isinstance(instance, gmfgraph::Dimension)

@given(instance=gmfgraph::Dimension_strategy)
def test_gmfgraph::dimension_dx_type(instance):
    assert isinstance(instance.dx, int)


@given(instance=gmfgraph::Dimension_strategy)
def test_gmfgraph::dimension_dx_setter(instance):
    original = instance.dx
    instance.dx = original
    assert instance.dx == original

@given(instance=gmfgraph::Dimension_strategy)
def test_gmfgraph::dimension_dy_type(instance):
    assert isinstance(instance.dy, int)


@given(instance=gmfgraph::Dimension_strategy)
def test_gmfgraph::dimension_dy_setter(instance):
    original = instance.dy
    instance.dy = original
    assert instance.dy == original

@given(instance=VisualFacet_strategy)
@settings(max_examples=50)
def test_visualfacet_instantiation(instance):
    assert isinstance(instance, VisualFacet)

@given(instance=gmfgraph::AlignmentFacet_strategy)
@settings(max_examples=50)
def test_gmfgraph::alignmentfacet_instantiation(instance):
    assert isinstance(instance, gmfgraph::AlignmentFacet)

@given(instance=gmfgraph::AlignmentFacet_strategy)
def test_gmfgraph::alignmentfacet_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=gmfgraph::AlignmentFacet_strategy)
def test_gmfgraph::alignmentfacet_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=gmfgraph::LabelOffsetFacet_strategy)
@settings(max_examples=50)
def test_gmfgraph::labeloffsetfacet_instantiation(instance):
    assert isinstance(instance, gmfgraph::LabelOffsetFacet)

@given(instance=gmfgraph::LabelOffsetFacet_strategy)
def test_gmfgraph::labeloffsetfacet_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=gmfgraph::LabelOffsetFacet_strategy)
def test_gmfgraph::labeloffsetfacet_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=gmfgraph::LabelOffsetFacet_strategy)
def test_gmfgraph::labeloffsetfacet_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=gmfgraph::LabelOffsetFacet_strategy)
def test_gmfgraph::labeloffsetfacet_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=gmfgraph::DefaultSizeFacet_strategy)
@settings(max_examples=50)
def test_gmfgraph::defaultsizefacet_instantiation(instance):
    assert isinstance(instance, gmfgraph::DefaultSizeFacet)

@given(instance=gmfgraph::GradientFacet_strategy)
@settings(max_examples=50)
def test_gmfgraph::gradientfacet_instantiation(instance):
    assert isinstance(instance, gmfgraph::GradientFacet)

@given(instance=gmfgraph::GradientFacet_strategy)
def test_gmfgraph::gradientfacet_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=gmfgraph::GradientFacet_strategy)
def test_gmfgraph::gradientfacet_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=gmfgraph::GeneralFacet_strategy)
@settings(max_examples=50)
def test_gmfgraph::generalfacet_instantiation(instance):
    assert isinstance(instance, gmfgraph::GeneralFacet)

@given(instance=gmfgraph::GeneralFacet_strategy)
def test_gmfgraph::generalfacet_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=gmfgraph::GeneralFacet_strategy)
def test_gmfgraph::generalfacet_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=gmfgraph::GeneralFacet_strategy)
def test_gmfgraph::generalfacet_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=gmfgraph::GeneralFacet_strategy)
def test_gmfgraph::generalfacet_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=AbstractNode_strategy)
@settings(max_examples=50)
def test_abstractnode_instantiation(instance):
    assert isinstance(instance, AbstractNode)

@given(instance=gmfgraph::Node_strategy)
@settings(max_examples=50)
def test_gmfgraph::node_instantiation(instance):
    assert isinstance(instance, gmfgraph::Node)

@given(instance=gmfgraph::Node_strategy)
def test_gmfgraph::node_affixedParentSide_type(instance):
    assert isinstance(instance.affixedParentSide, str)


@given(instance=gmfgraph::Node_strategy)
def test_gmfgraph::node_affixedParentSide_setter(instance):
    original = instance.affixedParentSide
    instance.affixedParentSide = original
    assert instance.affixedParentSide == original

@given(instance=gmfgraph::Node_strategy)
def test_gmfgraph::node_resizeConstraint_type(instance):
    assert isinstance(instance.resizeConstraint, str)


@given(instance=gmfgraph::Node_strategy)
def test_gmfgraph::node_resizeConstraint_setter(instance):
    original = instance.resizeConstraint
    instance.resizeConstraint = original
    assert instance.resizeConstraint == original

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=gmfgraph::Connection_strategy)
@settings(max_examples=50)
def test_gmfgraph::connection_instantiation(instance):
    assert isinstance(instance, gmfgraph::Connection)

@given(instance=gmfgraph::AbstractNode_strategy)
@settings(max_examples=50)
def test_gmfgraph::abstractnode_instantiation(instance):
    assert isinstance(instance, gmfgraph::AbstractNode)

@given(instance=gmfgraph::VisualFacet_strategy)
@settings(max_examples=50)
def test_gmfgraph::visualfacet_instantiation(instance):
    assert isinstance(instance, gmfgraph::VisualFacet)

@given(instance=gmfgraph::Identity_strategy)
@settings(max_examples=50)
def test_gmfgraph::identity_instantiation(instance):
    assert isinstance(instance, gmfgraph::Identity)

@given(instance=gmfgraph::Identity_strategy)
def test_gmfgraph::identity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gmfgraph::Identity_strategy)
def test_gmfgraph::identity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gmfgraph::RealFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph::realfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph::RealFigure)

@given(instance=gmfgraph::RealFigure_strategy)
def test_gmfgraph::realfigure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gmfgraph::RealFigure_strategy)
def test_gmfgraph::realfigure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gmfgraph::DiagramLabel_strategy)
@settings(max_examples=50)
def test_gmfgraph::diagramlabel_instantiation(instance):
    assert isinstance(instance, gmfgraph::DiagramLabel)

@given(instance=gmfgraph::DiagramLabel_strategy)
def test_gmfgraph::diagramlabel_external_type(instance):
    assert isinstance(instance.external, bool)


@given(instance=gmfgraph::DiagramLabel_strategy)
def test_gmfgraph::diagramlabel_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original

@given(instance=gmfgraph::DiagramLabel_strategy)
def test_gmfgraph::diagramlabel_elementIcon_type(instance):
    assert isinstance(instance.elementIcon, bool)


@given(instance=gmfgraph::DiagramLabel_strategy)
def test_gmfgraph::diagramlabel_elementIcon_setter(instance):
    original = instance.elementIcon
    instance.elementIcon = original
    assert instance.elementIcon == original

@given(instance=gmfgraph::Compartment_strategy)
@settings(max_examples=50)
def test_gmfgraph::compartment_instantiation(instance):
    assert isinstance(instance, gmfgraph::Compartment)

@given(instance=gmfgraph::Compartment_strategy)
def test_gmfgraph::compartment_collapsible_type(instance):
    assert isinstance(instance.collapsible, bool)


@given(instance=gmfgraph::Compartment_strategy)
def test_gmfgraph::compartment_collapsible_setter(instance):
    original = instance.collapsible
    instance.collapsible = original
    assert instance.collapsible == original

@given(instance=gmfgraph::Compartment_strategy)
def test_gmfgraph::compartment_needsTitle_type(instance):
    assert isinstance(instance.needsTitle, bool)


@given(instance=gmfgraph::Compartment_strategy)
def test_gmfgraph::compartment_needsTitle_setter(instance):
    original = instance.needsTitle
    instance.needsTitle = original
    assert instance.needsTitle == original

@given(instance=Identity_strategy)
@settings(max_examples=50)
def test_identity_instantiation(instance):
    assert isinstance(instance, Identity)

@given(instance=gmfgraph::FigureDescriptor_strategy)
@settings(max_examples=50)
def test_gmfgraph::figuredescriptor_instantiation(instance):
    assert isinstance(instance, gmfgraph::FigureDescriptor)

@given(instance=gmfgraph::DiagramElement_strategy)
@settings(max_examples=50)
def test_gmfgraph::diagramelement_instantiation(instance):
    assert isinstance(instance, gmfgraph::DiagramElement)

@given(instance=gmfgraph::FigureGallery_strategy)
@settings(max_examples=50)
def test_gmfgraph::figuregallery_instantiation(instance):
    assert isinstance(instance, gmfgraph::FigureGallery)

@given(instance=gmfgraph::FigureGallery_strategy)
def test_gmfgraph::figuregallery_implementationBundle_type(instance):
    assert isinstance(instance.implementationBundle, str)


@given(instance=gmfgraph::FigureGallery_strategy)
def test_gmfgraph::figuregallery_implementationBundle_setter(instance):
    original = instance.implementationBundle
    instance.implementationBundle = original
    assert instance.implementationBundle == original

@given(instance=gmfgraph::Canvas_strategy)
@settings(max_examples=50)
def test_gmfgraph::canvas_instantiation(instance):
    assert isinstance(instance, gmfgraph::Canvas)
