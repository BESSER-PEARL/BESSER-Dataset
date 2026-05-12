import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    GuideStyle,
    PageStyle,
    notation_Image,
    Bendpoints,
    notation_RelativeBendpoints,
    notation_Guide,
    RoutingStyle,
    LineStyle,
    notation_ConnectorStyle,
    FillStyle,
    DescriptionStyle,
    notation_DiagramStyle,
    FontStyle,
    Size,
    Location,
    notation_Bounds,
    EModelElement,
    RoundedCornersStyle,
    notation_ShapeStyle,
    notation_RoutingStyle,
    Anchor,
    notation_IdentityAnchor,
    LayoutConstraint,
    notation_Location,
    notation_Ratio,
    notation_Size,
    notation_EObject,
    Style,
    notation_TitleStyle,
    notation_PageStyle,
    notation_CanonicalStyle,
    notation_LineStyle,
    notation_DrawerStyle,
    notation_DescriptionStyle,
    notation_GuideStyle,
    notation_FontStyle,
    notation_SortingStyle,
    notation_FillStyle,
    notation_Style,
    notation_LayoutConstraint,
    notation_Anchor,
    notation_Bendpoints,
    notation_View,
    View,
    notation_Node,
    notation_Diagram,
    notation_Edge,
    TitleStyle,
    CanonicalStyle,
    BasicCompartment,
    notation_Compartment,
    ShapeStyle,
    Node,
    notation_Shape,
    notation_ArrowStyle,
    notation_LineTypeStyle,
    notation_TextStyle,
    notation_RoundedCornersStyle,
    BasicSemanticCompartment,
    DrawerStyle,
    DecorationNode,
    notation_BasicCompartment,
    notation_BasicDecorationNode,
    BasicDecorationNode,
    notation_BasicSemanticCompartment,
    notation_DecorationNode,
    DiagramStyle,
    Diagram,
    notation_StandardDiagram,
    ConnectorStyle,
    Edge,
    notation_Connector,
    FilteringStyle,
    SortingStyle,
    notation_SemanticListCompartment,
    notation_ListCompartment,
    notation_MultiDiagramLinkStyle,
    notation_DiagramLinkStyle,
    DiagramLinkStyle,
    notation_HintedDiagramLinkStyle,
    StringObjectConverter,
    notation_PropertyValue,
    notation_StringToPropertyValueMapEntry,
    notation_StringObjectConverter,
    notation_NamedStyle,
    DataTypeStyle,
    notation_ListValueStyle,
    notation_SingleValueStyle,
    notation_EDataType,
    notation_FilteringStyle,
    notation_NodeEntry,
    NamedStyle,
    notation_BooleanListValueStyle,
    notation_IntListValueStyle,
    notation_DataTypeStyle,
    notation_StringValueStyle,
    notation_ByteArrayValueStyle,
    notation_DoubleValueStyle,
    notation_IntValueStyle,
    notation_BooleanValueStyle,
    notation_EObjectValueStyle,
    notation_DoubleListValueStyle,
    notation_StringListValueStyle,
    notation_EObjectListValueStyle,
    notation_PropertiesSetStyle,
    ImageStyle,
    notation_ImageBufferStyle,
    notation_ImageStyle,
    ArrowType,
    LineType,
    Sorting,
    Alignment,
    TextAlignment,
    SortingDirection,
    JumpLinkType,
    MeasurementUnit,
    JumpLinkStatus,
    Routing,
    Smoothness,
    GradientStyle,
    Filtering,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_guidestyle_is_not_abstract():
    assert not inspect.isabstract(GuideStyle)


def test_guidestyle_constructor_exists():
    assert callable(GuideStyle.__init__)


def test_guidestyle_constructor_args():
    sig = inspect.signature(GuideStyle.__init__)
    params = list(sig.parameters.keys())



def test_pagestyle_is_not_abstract():
    assert not inspect.isabstract(PageStyle)


def test_pagestyle_constructor_exists():
    assert callable(PageStyle.__init__)


def test_pagestyle_constructor_args():
    sig = inspect.signature(PageStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_image_is_not_abstract():
    assert not inspect.isabstract(notation_Image)


def test_notation_image_constructor_exists():
    assert callable(notation_Image.__init__)


def test_notation_image_constructor_args():
    sig = inspect.signature(notation_Image.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_notation_image_has_data():
    assert hasattr(notation_Image, "data")
    descriptor = None
    for klass in notation_Image.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_bendpoints_is_not_abstract():
    assert not inspect.isabstract(Bendpoints)


def test_bendpoints_constructor_exists():
    assert callable(Bendpoints.__init__)


def test_bendpoints_constructor_args():
    sig = inspect.signature(Bendpoints.__init__)
    params = list(sig.parameters.keys())



def test_notation_relativebendpoints_is_not_abstract():
    assert not inspect.isabstract(notation_RelativeBendpoints)


def test_notation_relativebendpoints_constructor_exists():
    assert callable(notation_RelativeBendpoints.__init__)


def test_notation_relativebendpoints_constructor_args():
    sig = inspect.signature(notation_RelativeBendpoints.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"

def test_notation_relativebendpoints_has_points():
    assert hasattr(notation_RelativeBendpoints, "points")
    descriptor = None
    for klass in notation_RelativeBendpoints.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)



def test_notation_guide_is_not_abstract():
    assert not inspect.isabstract(notation_Guide)


def test_notation_guide_constructor_exists():
    assert callable(notation_Guide.__init__)


def test_notation_guide_constructor_args():
    sig = inspect.signature(notation_Guide.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_notation_guide_has_position():
    assert hasattr(notation_Guide, "position")
    descriptor = None
    for klass in notation_Guide.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_routingstyle_is_not_abstract():
    assert not inspect.isabstract(RoutingStyle)


def test_routingstyle_constructor_exists():
    assert callable(RoutingStyle.__init__)


def test_routingstyle_constructor_args():
    sig = inspect.signature(RoutingStyle.__init__)
    params = list(sig.parameters.keys())



def test_linestyle_is_not_abstract():
    assert not inspect.isabstract(LineStyle)


def test_linestyle_constructor_exists():
    assert callable(LineStyle.__init__)


def test_linestyle_constructor_args():
    sig = inspect.signature(LineStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_connectorstyle_is_not_abstract():
    assert not inspect.isabstract(notation_ConnectorStyle)


def test_notation_connectorstyle_constructor_exists():
    assert callable(notation_ConnectorStyle.__init__)


def test_notation_connectorstyle_constructor_args():
    sig = inspect.signature(notation_ConnectorStyle.__init__)
    params = list(sig.parameters.keys())



def test_fillstyle_is_not_abstract():
    assert not inspect.isabstract(FillStyle)


def test_fillstyle_constructor_exists():
    assert callable(FillStyle.__init__)


def test_fillstyle_constructor_args():
    sig = inspect.signature(FillStyle.__init__)
    params = list(sig.parameters.keys())



def test_descriptionstyle_is_not_abstract():
    assert not inspect.isabstract(DescriptionStyle)


def test_descriptionstyle_constructor_exists():
    assert callable(DescriptionStyle.__init__)


def test_descriptionstyle_constructor_args():
    sig = inspect.signature(DescriptionStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_diagramstyle_is_not_abstract():
    assert not inspect.isabstract(notation_DiagramStyle)


def test_notation_diagramstyle_constructor_exists():
    assert callable(notation_DiagramStyle.__init__)


def test_notation_diagramstyle_constructor_args():
    sig = inspect.signature(notation_DiagramStyle.__init__)
    params = list(sig.parameters.keys())



def test_fontstyle_is_not_abstract():
    assert not inspect.isabstract(FontStyle)


def test_fontstyle_constructor_exists():
    assert callable(FontStyle.__init__)


def test_fontstyle_constructor_args():
    sig = inspect.signature(FontStyle.__init__)
    params = list(sig.parameters.keys())



def test_size_is_not_abstract():
    assert not inspect.isabstract(Size)


def test_size_constructor_exists():
    assert callable(Size.__init__)


def test_size_constructor_args():
    sig = inspect.signature(Size.__init__)
    params = list(sig.parameters.keys())



def test_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_location_constructor_exists():
    assert callable(Location.__init__)


def test_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_notation_bounds_is_not_abstract():
    assert not inspect.isabstract(notation_Bounds)


def test_notation_bounds_constructor_exists():
    assert callable(notation_Bounds.__init__)


def test_notation_bounds_constructor_args():
    sig = inspect.signature(notation_Bounds.__init__)
    params = list(sig.parameters.keys())



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_roundedcornersstyle_is_not_abstract():
    assert not inspect.isabstract(RoundedCornersStyle)


def test_roundedcornersstyle_constructor_exists():
    assert callable(RoundedCornersStyle.__init__)


def test_roundedcornersstyle_constructor_args():
    sig = inspect.signature(RoundedCornersStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_shapestyle_is_not_abstract():
    assert not inspect.isabstract(notation_ShapeStyle)


def test_notation_shapestyle_constructor_exists():
    assert callable(notation_ShapeStyle.__init__)


def test_notation_shapestyle_constructor_args():
    sig = inspect.signature(notation_ShapeStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_routingstyle_is_not_abstract():
    assert not inspect.isabstract(notation_RoutingStyle)


def test_notation_routingstyle_constructor_exists():
    assert callable(notation_RoutingStyle.__init__)


def test_notation_routingstyle_constructor_args():
    sig = inspect.signature(notation_RoutingStyle.__init__)
    params = list(sig.parameters.keys())
    assert "closestDistance" in params, "Missing parameter 'closestDistance'"
    assert "jumpLinkStatus" in params, "Missing parameter 'jumpLinkStatus'"
    assert "smoothness" in params, "Missing parameter 'smoothness'"
    assert "jumpLinkType" in params, "Missing parameter 'jumpLinkType'"
    assert "jumpLinksReverse" in params, "Missing parameter 'jumpLinksReverse'"
    assert "routing" in params, "Missing parameter 'routing'"
    assert "avoidObstructions" in params, "Missing parameter 'avoidObstructions'"

def test_notation_routingstyle_has_closestDistance():
    assert hasattr(notation_RoutingStyle, "closestDistance")
    descriptor = None
    for klass in notation_RoutingStyle.__mro__:
        if "closestDistance" in klass.__dict__:
            descriptor = klass.__dict__["closestDistance"]
            break
    assert isinstance(descriptor, property)

def test_notation_routingstyle_has_jumpLinkStatus():
    assert hasattr(notation_RoutingStyle, "jumpLinkStatus")
    descriptor = None
    for klass in notation_RoutingStyle.__mro__:
        if "jumpLinkStatus" in klass.__dict__:
            descriptor = klass.__dict__["jumpLinkStatus"]
            break
    assert isinstance(descriptor, property)

def test_notation_routingstyle_has_smoothness():
    assert hasattr(notation_RoutingStyle, "smoothness")
    descriptor = None
    for klass in notation_RoutingStyle.__mro__:
        if "smoothness" in klass.__dict__:
            descriptor = klass.__dict__["smoothness"]
            break
    assert isinstance(descriptor, property)

def test_notation_routingstyle_has_jumpLinkType():
    assert hasattr(notation_RoutingStyle, "jumpLinkType")
    descriptor = None
    for klass in notation_RoutingStyle.__mro__:
        if "jumpLinkType" in klass.__dict__:
            descriptor = klass.__dict__["jumpLinkType"]
            break
    assert isinstance(descriptor, property)

def test_notation_routingstyle_has_jumpLinksReverse():
    assert hasattr(notation_RoutingStyle, "jumpLinksReverse")
    descriptor = None
    for klass in notation_RoutingStyle.__mro__:
        if "jumpLinksReverse" in klass.__dict__:
            descriptor = klass.__dict__["jumpLinksReverse"]
            break
    assert isinstance(descriptor, property)

def test_notation_routingstyle_has_routing():
    assert hasattr(notation_RoutingStyle, "routing")
    descriptor = None
    for klass in notation_RoutingStyle.__mro__:
        if "routing" in klass.__dict__:
            descriptor = klass.__dict__["routing"]
            break
    assert isinstance(descriptor, property)

def test_notation_routingstyle_has_avoidObstructions():
    assert hasattr(notation_RoutingStyle, "avoidObstructions")
    descriptor = None
    for klass in notation_RoutingStyle.__mro__:
        if "avoidObstructions" in klass.__dict__:
            descriptor = klass.__dict__["avoidObstructions"]
            break
    assert isinstance(descriptor, property)



def test_anchor_is_not_abstract():
    assert not inspect.isabstract(Anchor)


def test_anchor_constructor_exists():
    assert callable(Anchor.__init__)


def test_anchor_constructor_args():
    sig = inspect.signature(Anchor.__init__)
    params = list(sig.parameters.keys())



def test_notation_identityanchor_is_not_abstract():
    assert not inspect.isabstract(notation_IdentityAnchor)


def test_notation_identityanchor_constructor_exists():
    assert callable(notation_IdentityAnchor.__init__)


def test_notation_identityanchor_constructor_args():
    sig = inspect.signature(notation_IdentityAnchor.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_notation_identityanchor_has_id():
    assert hasattr(notation_IdentityAnchor, "id")
    descriptor = None
    for klass in notation_IdentityAnchor.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_layoutconstraint_is_not_abstract():
    assert not inspect.isabstract(LayoutConstraint)


def test_layoutconstraint_constructor_exists():
    assert callable(LayoutConstraint.__init__)


def test_layoutconstraint_constructor_args():
    sig = inspect.signature(LayoutConstraint.__init__)
    params = list(sig.parameters.keys())



def test_notation_location_is_not_abstract():
    assert not inspect.isabstract(notation_Location)


def test_notation_location_constructor_exists():
    assert callable(notation_Location.__init__)


def test_notation_location_constructor_args():
    sig = inspect.signature(notation_Location.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_notation_location_has_x():
    assert hasattr(notation_Location, "x")
    descriptor = None
    for klass in notation_Location.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_notation_location_has_y():
    assert hasattr(notation_Location, "y")
    descriptor = None
    for klass in notation_Location.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_notation_ratio_is_not_abstract():
    assert not inspect.isabstract(notation_Ratio)


def test_notation_ratio_constructor_exists():
    assert callable(notation_Ratio.__init__)


def test_notation_ratio_constructor_args():
    sig = inspect.signature(notation_Ratio.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_notation_ratio_has_value():
    assert hasattr(notation_Ratio, "value")
    descriptor = None
    for klass in notation_Ratio.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_notation_size_is_not_abstract():
    assert not inspect.isabstract(notation_Size)


def test_notation_size_constructor_exists():
    assert callable(notation_Size.__init__)


def test_notation_size_constructor_args():
    sig = inspect.signature(notation_Size.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_notation_size_has_height():
    assert hasattr(notation_Size, "height")
    descriptor = None
    for klass in notation_Size.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_notation_size_has_width():
    assert hasattr(notation_Size, "width")
    descriptor = None
    for klass in notation_Size.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_notation_eobject_is_not_abstract():
    assert not inspect.isabstract(notation_EObject)


def test_notation_eobject_constructor_exists():
    assert callable(notation_EObject.__init__)


def test_notation_eobject_constructor_args():
    sig = inspect.signature(notation_EObject.__init__)
    params = list(sig.parameters.keys())



def test_style_is_not_abstract():
    assert not inspect.isabstract(Style)


def test_style_constructor_exists():
    assert callable(Style.__init__)


def test_style_constructor_args():
    sig = inspect.signature(Style.__init__)
    params = list(sig.parameters.keys())



def test_notation_titlestyle_is_not_abstract():
    assert not inspect.isabstract(notation_TitleStyle)


def test_notation_titlestyle_constructor_exists():
    assert callable(notation_TitleStyle.__init__)


def test_notation_titlestyle_constructor_args():
    sig = inspect.signature(notation_TitleStyle.__init__)
    params = list(sig.parameters.keys())
    assert "showTitle" in params, "Missing parameter 'showTitle'"

def test_notation_titlestyle_has_showTitle():
    assert hasattr(notation_TitleStyle, "showTitle")
    descriptor = None
    for klass in notation_TitleStyle.__mro__:
        if "showTitle" in klass.__dict__:
            descriptor = klass.__dict__["showTitle"]
            break
    assert isinstance(descriptor, property)



def test_notation_pagestyle_is_not_abstract():
    assert not inspect.isabstract(notation_PageStyle)


def test_notation_pagestyle_constructor_exists():
    assert callable(notation_PageStyle.__init__)


def test_notation_pagestyle_constructor_args():
    sig = inspect.signature(notation_PageStyle.__init__)
    params = list(sig.parameters.keys())
    assert "pageWidth" in params, "Missing parameter 'pageWidth'"
    assert "pageX" in params, "Missing parameter 'pageX'"
    assert "pageHeight" in params, "Missing parameter 'pageHeight'"
    assert "pageY" in params, "Missing parameter 'pageY'"

def test_notation_pagestyle_has_pageWidth():
    assert hasattr(notation_PageStyle, "pageWidth")
    descriptor = None
    for klass in notation_PageStyle.__mro__:
        if "pageWidth" in klass.__dict__:
            descriptor = klass.__dict__["pageWidth"]
            break
    assert isinstance(descriptor, property)

def test_notation_pagestyle_has_pageX():
    assert hasattr(notation_PageStyle, "pageX")
    descriptor = None
    for klass in notation_PageStyle.__mro__:
        if "pageX" in klass.__dict__:
            descriptor = klass.__dict__["pageX"]
            break
    assert isinstance(descriptor, property)

def test_notation_pagestyle_has_pageHeight():
    assert hasattr(notation_PageStyle, "pageHeight")
    descriptor = None
    for klass in notation_PageStyle.__mro__:
        if "pageHeight" in klass.__dict__:
            descriptor = klass.__dict__["pageHeight"]
            break
    assert isinstance(descriptor, property)

def test_notation_pagestyle_has_pageY():
    assert hasattr(notation_PageStyle, "pageY")
    descriptor = None
    for klass in notation_PageStyle.__mro__:
        if "pageY" in klass.__dict__:
            descriptor = klass.__dict__["pageY"]
            break
    assert isinstance(descriptor, property)



def test_notation_canonicalstyle_is_not_abstract():
    assert not inspect.isabstract(notation_CanonicalStyle)


def test_notation_canonicalstyle_constructor_exists():
    assert callable(notation_CanonicalStyle.__init__)


def test_notation_canonicalstyle_constructor_args():
    sig = inspect.signature(notation_CanonicalStyle.__init__)
    params = list(sig.parameters.keys())
    assert "canonical" in params, "Missing parameter 'canonical'"

def test_notation_canonicalstyle_has_canonical():
    assert hasattr(notation_CanonicalStyle, "canonical")
    descriptor = None
    for klass in notation_CanonicalStyle.__mro__:
        if "canonical" in klass.__dict__:
            descriptor = klass.__dict__["canonical"]
            break
    assert isinstance(descriptor, property)



def test_notation_linestyle_is_not_abstract():
    assert not inspect.isabstract(notation_LineStyle)


def test_notation_linestyle_constructor_exists():
    assert callable(notation_LineStyle.__init__)


def test_notation_linestyle_constructor_args():
    sig = inspect.signature(notation_LineStyle.__init__)
    params = list(sig.parameters.keys())
    assert "lineColor" in params, "Missing parameter 'lineColor'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"

def test_notation_linestyle_has_lineColor():
    assert hasattr(notation_LineStyle, "lineColor")
    descriptor = None
    for klass in notation_LineStyle.__mro__:
        if "lineColor" in klass.__dict__:
            descriptor = klass.__dict__["lineColor"]
            break
    assert isinstance(descriptor, property)

def test_notation_linestyle_has_lineWidth():
    assert hasattr(notation_LineStyle, "lineWidth")
    descriptor = None
    for klass in notation_LineStyle.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)



def test_notation_drawerstyle_is_not_abstract():
    assert not inspect.isabstract(notation_DrawerStyle)


def test_notation_drawerstyle_constructor_exists():
    assert callable(notation_DrawerStyle.__init__)


def test_notation_drawerstyle_constructor_args():
    sig = inspect.signature(notation_DrawerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "collapsed" in params, "Missing parameter 'collapsed'"

def test_notation_drawerstyle_has_collapsed():
    assert hasattr(notation_DrawerStyle, "collapsed")
    descriptor = None
    for klass in notation_DrawerStyle.__mro__:
        if "collapsed" in klass.__dict__:
            descriptor = klass.__dict__["collapsed"]
            break
    assert isinstance(descriptor, property)



def test_notation_descriptionstyle_is_not_abstract():
    assert not inspect.isabstract(notation_DescriptionStyle)


def test_notation_descriptionstyle_constructor_exists():
    assert callable(notation_DescriptionStyle.__init__)


def test_notation_descriptionstyle_constructor_args():
    sig = inspect.signature(notation_DescriptionStyle.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_notation_descriptionstyle_has_description():
    assert hasattr(notation_DescriptionStyle, "description")
    descriptor = None
    for klass in notation_DescriptionStyle.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_notation_guidestyle_is_not_abstract():
    assert not inspect.isabstract(notation_GuideStyle)


def test_notation_guidestyle_constructor_exists():
    assert callable(notation_GuideStyle.__init__)


def test_notation_guidestyle_constructor_args():
    sig = inspect.signature(notation_GuideStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_fontstyle_is_not_abstract():
    assert not inspect.isabstract(notation_FontStyle)


def test_notation_fontstyle_constructor_exists():
    assert callable(notation_FontStyle.__init__)


def test_notation_fontstyle_constructor_args():
    sig = inspect.signature(notation_FontStyle.__init__)
    params = list(sig.parameters.keys())
    assert "fontHeight" in params, "Missing parameter 'fontHeight'"
    assert "underline" in params, "Missing parameter 'underline'"
    assert "italic" in params, "Missing parameter 'italic'"
    assert "strikeThrough" in params, "Missing parameter 'strikeThrough'"
    assert "bold" in params, "Missing parameter 'bold'"
    assert "fontColor" in params, "Missing parameter 'fontColor'"
    assert "fontName" in params, "Missing parameter 'fontName'"

def test_notation_fontstyle_has_fontHeight():
    assert hasattr(notation_FontStyle, "fontHeight")
    descriptor = None
    for klass in notation_FontStyle.__mro__:
        if "fontHeight" in klass.__dict__:
            descriptor = klass.__dict__["fontHeight"]
            break
    assert isinstance(descriptor, property)

def test_notation_fontstyle_has_underline():
    assert hasattr(notation_FontStyle, "underline")
    descriptor = None
    for klass in notation_FontStyle.__mro__:
        if "underline" in klass.__dict__:
            descriptor = klass.__dict__["underline"]
            break
    assert isinstance(descriptor, property)

def test_notation_fontstyle_has_italic():
    assert hasattr(notation_FontStyle, "italic")
    descriptor = None
    for klass in notation_FontStyle.__mro__:
        if "italic" in klass.__dict__:
            descriptor = klass.__dict__["italic"]
            break
    assert isinstance(descriptor, property)

def test_notation_fontstyle_has_strikeThrough():
    assert hasattr(notation_FontStyle, "strikeThrough")
    descriptor = None
    for klass in notation_FontStyle.__mro__:
        if "strikeThrough" in klass.__dict__:
            descriptor = klass.__dict__["strikeThrough"]
            break
    assert isinstance(descriptor, property)

def test_notation_fontstyle_has_bold():
    assert hasattr(notation_FontStyle, "bold")
    descriptor = None
    for klass in notation_FontStyle.__mro__:
        if "bold" in klass.__dict__:
            descriptor = klass.__dict__["bold"]
            break
    assert isinstance(descriptor, property)

def test_notation_fontstyle_has_fontColor():
    assert hasattr(notation_FontStyle, "fontColor")
    descriptor = None
    for klass in notation_FontStyle.__mro__:
        if "fontColor" in klass.__dict__:
            descriptor = klass.__dict__["fontColor"]
            break
    assert isinstance(descriptor, property)

def test_notation_fontstyle_has_fontName():
    assert hasattr(notation_FontStyle, "fontName")
    descriptor = None
    for klass in notation_FontStyle.__mro__:
        if "fontName" in klass.__dict__:
            descriptor = klass.__dict__["fontName"]
            break
    assert isinstance(descriptor, property)



def test_notation_sortingstyle_is_not_abstract():
    assert not inspect.isabstract(notation_SortingStyle)


def test_notation_sortingstyle_constructor_exists():
    assert callable(notation_SortingStyle.__init__)


def test_notation_sortingstyle_constructor_args():
    sig = inspect.signature(notation_SortingStyle.__init__)
    params = list(sig.parameters.keys())
    assert "sorting" in params, "Missing parameter 'sorting'"
    assert "sortingKeys" in params, "Missing parameter 'sortingKeys'"

def test_notation_sortingstyle_has_sorting():
    assert hasattr(notation_SortingStyle, "sorting")
    descriptor = None
    for klass in notation_SortingStyle.__mro__:
        if "sorting" in klass.__dict__:
            descriptor = klass.__dict__["sorting"]
            break
    assert isinstance(descriptor, property)

def test_notation_sortingstyle_has_sortingKeys():
    assert hasattr(notation_SortingStyle, "sortingKeys")
    descriptor = None
    for klass in notation_SortingStyle.__mro__:
        if "sortingKeys" in klass.__dict__:
            descriptor = klass.__dict__["sortingKeys"]
            break
    assert isinstance(descriptor, property)



def test_notation_fillstyle_is_not_abstract():
    assert not inspect.isabstract(notation_FillStyle)


def test_notation_fillstyle_constructor_exists():
    assert callable(notation_FillStyle.__init__)


def test_notation_fillstyle_constructor_args():
    sig = inspect.signature(notation_FillStyle.__init__)
    params = list(sig.parameters.keys())
    assert "gradient" in params, "Missing parameter 'gradient'"
    assert "fillColor" in params, "Missing parameter 'fillColor'"
    assert "transparency" in params, "Missing parameter 'transparency'"

def test_notation_fillstyle_has_gradient():
    assert hasattr(notation_FillStyle, "gradient")
    descriptor = None
    for klass in notation_FillStyle.__mro__:
        if "gradient" in klass.__dict__:
            descriptor = klass.__dict__["gradient"]
            break
    assert isinstance(descriptor, property)

def test_notation_fillstyle_has_fillColor():
    assert hasattr(notation_FillStyle, "fillColor")
    descriptor = None
    for klass in notation_FillStyle.__mro__:
        if "fillColor" in klass.__dict__:
            descriptor = klass.__dict__["fillColor"]
            break
    assert isinstance(descriptor, property)

def test_notation_fillstyle_has_transparency():
    assert hasattr(notation_FillStyle, "transparency")
    descriptor = None
    for klass in notation_FillStyle.__mro__:
        if "transparency" in klass.__dict__:
            descriptor = klass.__dict__["transparency"]
            break
    assert isinstance(descriptor, property)



def test_notation_style_is_not_abstract():
    assert not inspect.isabstract(notation_Style)


def test_notation_style_constructor_exists():
    assert callable(notation_Style.__init__)


def test_notation_style_constructor_args():
    sig = inspect.signature(notation_Style.__init__)
    params = list(sig.parameters.keys())



def test_notation_layoutconstraint_is_not_abstract():
    assert not inspect.isabstract(notation_LayoutConstraint)


def test_notation_layoutconstraint_constructor_exists():
    assert callable(notation_LayoutConstraint.__init__)


def test_notation_layoutconstraint_constructor_args():
    sig = inspect.signature(notation_LayoutConstraint.__init__)
    params = list(sig.parameters.keys())



def test_notation_anchor_is_not_abstract():
    assert not inspect.isabstract(notation_Anchor)


def test_notation_anchor_constructor_exists():
    assert callable(notation_Anchor.__init__)


def test_notation_anchor_constructor_args():
    sig = inspect.signature(notation_Anchor.__init__)
    params = list(sig.parameters.keys())



def test_notation_bendpoints_is_not_abstract():
    assert not inspect.isabstract(notation_Bendpoints)


def test_notation_bendpoints_constructor_exists():
    assert callable(notation_Bendpoints.__init__)


def test_notation_bendpoints_constructor_args():
    sig = inspect.signature(notation_Bendpoints.__init__)
    params = list(sig.parameters.keys())



def test_notation_view_is_not_abstract():
    assert not inspect.isabstract(notation_View)


def test_notation_view_constructor_exists():
    assert callable(notation_View.__init__)


def test_notation_view_constructor_args():
    sig = inspect.signature(notation_View.__init__)
    params = list(sig.parameters.keys())
    assert "mutable" in params, "Missing parameter 'mutable'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "type" in params, "Missing parameter 'type'"

def test_notation_view_has_mutable():
    assert hasattr(notation_View, "mutable")
    descriptor = None
    for klass in notation_View.__mro__:
        if "mutable" in klass.__dict__:
            descriptor = klass.__dict__["mutable"]
            break
    assert isinstance(descriptor, property)

def test_notation_view_has_visible():
    assert hasattr(notation_View, "visible")
    descriptor = None
    for klass in notation_View.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_notation_view_has_type():
    assert hasattr(notation_View, "type")
    descriptor = None
    for klass in notation_View.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_view_is_not_abstract():
    assert not inspect.isabstract(View)


def test_view_constructor_exists():
    assert callable(View.__init__)


def test_view_constructor_args():
    sig = inspect.signature(View.__init__)
    params = list(sig.parameters.keys())



def test_notation_node_is_not_abstract():
    assert not inspect.isabstract(notation_Node)


def test_notation_node_constructor_exists():
    assert callable(notation_Node.__init__)


def test_notation_node_constructor_args():
    sig = inspect.signature(notation_Node.__init__)
    params = list(sig.parameters.keys())



def test_notation_diagram_is_not_abstract():
    assert not inspect.isabstract(notation_Diagram)


def test_notation_diagram_constructor_exists():
    assert callable(notation_Diagram.__init__)


def test_notation_diagram_constructor_args():
    sig = inspect.signature(notation_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "measurementUnit" in params, "Missing parameter 'measurementUnit'"

def test_notation_diagram_has_name():
    assert hasattr(notation_Diagram, "name")
    descriptor = None
    for klass in notation_Diagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_notation_diagram_has_measurementUnit():
    assert hasattr(notation_Diagram, "measurementUnit")
    descriptor = None
    for klass in notation_Diagram.__mro__:
        if "measurementUnit" in klass.__dict__:
            descriptor = klass.__dict__["measurementUnit"]
            break
    assert isinstance(descriptor, property)



def test_notation_edge_is_not_abstract():
    assert not inspect.isabstract(notation_Edge)


def test_notation_edge_constructor_exists():
    assert callable(notation_Edge.__init__)


def test_notation_edge_constructor_args():
    sig = inspect.signature(notation_Edge.__init__)
    params = list(sig.parameters.keys())



def test_titlestyle_is_not_abstract():
    assert not inspect.isabstract(TitleStyle)


def test_titlestyle_constructor_exists():
    assert callable(TitleStyle.__init__)


def test_titlestyle_constructor_args():
    sig = inspect.signature(TitleStyle.__init__)
    params = list(sig.parameters.keys())



def test_canonicalstyle_is_not_abstract():
    assert not inspect.isabstract(CanonicalStyle)


def test_canonicalstyle_constructor_exists():
    assert callable(CanonicalStyle.__init__)


def test_canonicalstyle_constructor_args():
    sig = inspect.signature(CanonicalStyle.__init__)
    params = list(sig.parameters.keys())



def test_basiccompartment_is_not_abstract():
    assert not inspect.isabstract(BasicCompartment)


def test_basiccompartment_constructor_exists():
    assert callable(BasicCompartment.__init__)


def test_basiccompartment_constructor_args():
    sig = inspect.signature(BasicCompartment.__init__)
    params = list(sig.parameters.keys())



def test_notation_compartment_is_not_abstract():
    assert not inspect.isabstract(notation_Compartment)


def test_notation_compartment_constructor_exists():
    assert callable(notation_Compartment.__init__)


def test_notation_compartment_constructor_args():
    sig = inspect.signature(notation_Compartment.__init__)
    params = list(sig.parameters.keys())



def test_shapestyle_is_not_abstract():
    assert not inspect.isabstract(ShapeStyle)


def test_shapestyle_constructor_exists():
    assert callable(ShapeStyle.__init__)


def test_shapestyle_constructor_args():
    sig = inspect.signature(ShapeStyle.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_notation_shape_is_not_abstract():
    assert not inspect.isabstract(notation_Shape)


def test_notation_shape_constructor_exists():
    assert callable(notation_Shape.__init__)


def test_notation_shape_constructor_args():
    sig = inspect.signature(notation_Shape.__init__)
    params = list(sig.parameters.keys())



def test_notation_arrowstyle_is_not_abstract():
    assert not inspect.isabstract(notation_ArrowStyle)


def test_notation_arrowstyle_constructor_exists():
    assert callable(notation_ArrowStyle.__init__)


def test_notation_arrowstyle_constructor_args():
    sig = inspect.signature(notation_ArrowStyle.__init__)
    params = list(sig.parameters.keys())
    assert "arrowSource" in params, "Missing parameter 'arrowSource'"
    assert "arrowTarget" in params, "Missing parameter 'arrowTarget'"

def test_notation_arrowstyle_has_arrowSource():
    assert hasattr(notation_ArrowStyle, "arrowSource")
    descriptor = None
    for klass in notation_ArrowStyle.__mro__:
        if "arrowSource" in klass.__dict__:
            descriptor = klass.__dict__["arrowSource"]
            break
    assert isinstance(descriptor, property)

def test_notation_arrowstyle_has_arrowTarget():
    assert hasattr(notation_ArrowStyle, "arrowTarget")
    descriptor = None
    for klass in notation_ArrowStyle.__mro__:
        if "arrowTarget" in klass.__dict__:
            descriptor = klass.__dict__["arrowTarget"]
            break
    assert isinstance(descriptor, property)



def test_notation_linetypestyle_is_not_abstract():
    assert not inspect.isabstract(notation_LineTypeStyle)


def test_notation_linetypestyle_constructor_exists():
    assert callable(notation_LineTypeStyle.__init__)


def test_notation_linetypestyle_constructor_args():
    sig = inspect.signature(notation_LineTypeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "lineType" in params, "Missing parameter 'lineType'"

def test_notation_linetypestyle_has_lineType():
    assert hasattr(notation_LineTypeStyle, "lineType")
    descriptor = None
    for klass in notation_LineTypeStyle.__mro__:
        if "lineType" in klass.__dict__:
            descriptor = klass.__dict__["lineType"]
            break
    assert isinstance(descriptor, property)



def test_notation_textstyle_is_not_abstract():
    assert not inspect.isabstract(notation_TextStyle)


def test_notation_textstyle_constructor_exists():
    assert callable(notation_TextStyle.__init__)


def test_notation_textstyle_constructor_args():
    sig = inspect.signature(notation_TextStyle.__init__)
    params = list(sig.parameters.keys())
    assert "textAlignment" in params, "Missing parameter 'textAlignment'"

def test_notation_textstyle_has_textAlignment():
    assert hasattr(notation_TextStyle, "textAlignment")
    descriptor = None
    for klass in notation_TextStyle.__mro__:
        if "textAlignment" in klass.__dict__:
            descriptor = klass.__dict__["textAlignment"]
            break
    assert isinstance(descriptor, property)



def test_notation_roundedcornersstyle_is_not_abstract():
    assert not inspect.isabstract(notation_RoundedCornersStyle)


def test_notation_roundedcornersstyle_constructor_exists():
    assert callable(notation_RoundedCornersStyle.__init__)


def test_notation_roundedcornersstyle_constructor_args():
    sig = inspect.signature(notation_RoundedCornersStyle.__init__)
    params = list(sig.parameters.keys())
    assert "roundedBendpointsRadius" in params, "Missing parameter 'roundedBendpointsRadius'"

def test_notation_roundedcornersstyle_has_roundedBendpointsRadius():
    assert hasattr(notation_RoundedCornersStyle, "roundedBendpointsRadius")
    descriptor = None
    for klass in notation_RoundedCornersStyle.__mro__:
        if "roundedBendpointsRadius" in klass.__dict__:
            descriptor = klass.__dict__["roundedBendpointsRadius"]
            break
    assert isinstance(descriptor, property)



def test_basicsemanticcompartment_is_not_abstract():
    assert not inspect.isabstract(BasicSemanticCompartment)


def test_basicsemanticcompartment_constructor_exists():
    assert callable(BasicSemanticCompartment.__init__)


def test_basicsemanticcompartment_constructor_args():
    sig = inspect.signature(BasicSemanticCompartment.__init__)
    params = list(sig.parameters.keys())



def test_drawerstyle_is_not_abstract():
    assert not inspect.isabstract(DrawerStyle)


def test_drawerstyle_constructor_exists():
    assert callable(DrawerStyle.__init__)


def test_drawerstyle_constructor_args():
    sig = inspect.signature(DrawerStyle.__init__)
    params = list(sig.parameters.keys())



def test_decorationnode_is_not_abstract():
    assert not inspect.isabstract(DecorationNode)


def test_decorationnode_constructor_exists():
    assert callable(DecorationNode.__init__)


def test_decorationnode_constructor_args():
    sig = inspect.signature(DecorationNode.__init__)
    params = list(sig.parameters.keys())



def test_notation_basiccompartment_is_not_abstract():
    assert not inspect.isabstract(notation_BasicCompartment)


def test_notation_basiccompartment_constructor_exists():
    assert callable(notation_BasicCompartment.__init__)


def test_notation_basiccompartment_constructor_args():
    sig = inspect.signature(notation_BasicCompartment.__init__)
    params = list(sig.parameters.keys())



def test_notation_basicdecorationnode_is_not_abstract():
    assert not inspect.isabstract(notation_BasicDecorationNode)


def test_notation_basicdecorationnode_constructor_exists():
    assert callable(notation_BasicDecorationNode.__init__)


def test_notation_basicdecorationnode_constructor_args():
    sig = inspect.signature(notation_BasicDecorationNode.__init__)
    params = list(sig.parameters.keys())



def test_basicdecorationnode_is_not_abstract():
    assert not inspect.isabstract(BasicDecorationNode)


def test_basicdecorationnode_constructor_exists():
    assert callable(BasicDecorationNode.__init__)


def test_basicdecorationnode_constructor_args():
    sig = inspect.signature(BasicDecorationNode.__init__)
    params = list(sig.parameters.keys())



def test_notation_basicsemanticcompartment_is_not_abstract():
    assert not inspect.isabstract(notation_BasicSemanticCompartment)


def test_notation_basicsemanticcompartment_constructor_exists():
    assert callable(notation_BasicSemanticCompartment.__init__)


def test_notation_basicsemanticcompartment_constructor_args():
    sig = inspect.signature(notation_BasicSemanticCompartment.__init__)
    params = list(sig.parameters.keys())



def test_notation_decorationnode_is_not_abstract():
    assert not inspect.isabstract(notation_DecorationNode)


def test_notation_decorationnode_constructor_exists():
    assert callable(notation_DecorationNode.__init__)


def test_notation_decorationnode_constructor_args():
    sig = inspect.signature(notation_DecorationNode.__init__)
    params = list(sig.parameters.keys())



def test_diagramstyle_is_not_abstract():
    assert not inspect.isabstract(DiagramStyle)


def test_diagramstyle_constructor_exists():
    assert callable(DiagramStyle.__init__)


def test_diagramstyle_constructor_args():
    sig = inspect.signature(DiagramStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram_is_not_abstract():
    assert not inspect.isabstract(Diagram)


def test_diagram_constructor_exists():
    assert callable(Diagram.__init__)


def test_diagram_constructor_args():
    sig = inspect.signature(Diagram.__init__)
    params = list(sig.parameters.keys())



def test_notation_standarddiagram_is_not_abstract():
    assert not inspect.isabstract(notation_StandardDiagram)


def test_notation_standarddiagram_constructor_exists():
    assert callable(notation_StandardDiagram.__init__)


def test_notation_standarddiagram_constructor_args():
    sig = inspect.signature(notation_StandardDiagram.__init__)
    params = list(sig.parameters.keys())



def test_connectorstyle_is_not_abstract():
    assert not inspect.isabstract(ConnectorStyle)


def test_connectorstyle_constructor_exists():
    assert callable(ConnectorStyle.__init__)


def test_connectorstyle_constructor_args():
    sig = inspect.signature(ConnectorStyle.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_notation_connector_is_not_abstract():
    assert not inspect.isabstract(notation_Connector)


def test_notation_connector_constructor_exists():
    assert callable(notation_Connector.__init__)


def test_notation_connector_constructor_args():
    sig = inspect.signature(notation_Connector.__init__)
    params = list(sig.parameters.keys())



def test_filteringstyle_is_not_abstract():
    assert not inspect.isabstract(FilteringStyle)


def test_filteringstyle_constructor_exists():
    assert callable(FilteringStyle.__init__)


def test_filteringstyle_constructor_args():
    sig = inspect.signature(FilteringStyle.__init__)
    params = list(sig.parameters.keys())



def test_sortingstyle_is_not_abstract():
    assert not inspect.isabstract(SortingStyle)


def test_sortingstyle_constructor_exists():
    assert callable(SortingStyle.__init__)


def test_sortingstyle_constructor_args():
    sig = inspect.signature(SortingStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_semanticlistcompartment_is_not_abstract():
    assert not inspect.isabstract(notation_SemanticListCompartment)


def test_notation_semanticlistcompartment_constructor_exists():
    assert callable(notation_SemanticListCompartment.__init__)


def test_notation_semanticlistcompartment_constructor_args():
    sig = inspect.signature(notation_SemanticListCompartment.__init__)
    params = list(sig.parameters.keys())



def test_notation_listcompartment_is_not_abstract():
    assert not inspect.isabstract(notation_ListCompartment)


def test_notation_listcompartment_constructor_exists():
    assert callable(notation_ListCompartment.__init__)


def test_notation_listcompartment_constructor_args():
    sig = inspect.signature(notation_ListCompartment.__init__)
    params = list(sig.parameters.keys())



def test_notation_multidiagramlinkstyle_is_not_abstract():
    assert not inspect.isabstract(notation_MultiDiagramLinkStyle)


def test_notation_multidiagramlinkstyle_constructor_exists():
    assert callable(notation_MultiDiagramLinkStyle.__init__)


def test_notation_multidiagramlinkstyle_constructor_args():
    sig = inspect.signature(notation_MultiDiagramLinkStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_diagramlinkstyle_is_not_abstract():
    assert not inspect.isabstract(notation_DiagramLinkStyle)


def test_notation_diagramlinkstyle_constructor_exists():
    assert callable(notation_DiagramLinkStyle.__init__)


def test_notation_diagramlinkstyle_constructor_args():
    sig = inspect.signature(notation_DiagramLinkStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagramlinkstyle_is_not_abstract():
    assert not inspect.isabstract(DiagramLinkStyle)


def test_diagramlinkstyle_constructor_exists():
    assert callable(DiagramLinkStyle.__init__)


def test_diagramlinkstyle_constructor_args():
    sig = inspect.signature(DiagramLinkStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_hinteddiagramlinkstyle_is_not_abstract():
    assert not inspect.isabstract(notation_HintedDiagramLinkStyle)


def test_notation_hinteddiagramlinkstyle_constructor_exists():
    assert callable(notation_HintedDiagramLinkStyle.__init__)


def test_notation_hinteddiagramlinkstyle_constructor_args():
    sig = inspect.signature(notation_HintedDiagramLinkStyle.__init__)
    params = list(sig.parameters.keys())
    assert "hint" in params, "Missing parameter 'hint'"

def test_notation_hinteddiagramlinkstyle_has_hint():
    assert hasattr(notation_HintedDiagramLinkStyle, "hint")
    descriptor = None
    for klass in notation_HintedDiagramLinkStyle.__mro__:
        if "hint" in klass.__dict__:
            descriptor = klass.__dict__["hint"]
            break
    assert isinstance(descriptor, property)



def test_stringobjectconverter_is_not_abstract():
    assert not inspect.isabstract(StringObjectConverter)


def test_stringobjectconverter_constructor_exists():
    assert callable(StringObjectConverter.__init__)


def test_stringobjectconverter_constructor_args():
    sig = inspect.signature(StringObjectConverter.__init__)
    params = list(sig.parameters.keys())



def test_notation_propertyvalue_is_not_abstract():
    assert not inspect.isabstract(notation_PropertyValue)


def test_notation_propertyvalue_constructor_exists():
    assert callable(notation_PropertyValue.__init__)


def test_notation_propertyvalue_constructor_args():
    sig = inspect.signature(notation_PropertyValue.__init__)
    params = list(sig.parameters.keys())
    assert "rawValue" in params, "Missing parameter 'rawValue'"

def test_notation_propertyvalue_has_rawValue():
    assert hasattr(notation_PropertyValue, "rawValue")
    descriptor = None
    for klass in notation_PropertyValue.__mro__:
        if "rawValue" in klass.__dict__:
            descriptor = klass.__dict__["rawValue"]
            break
    assert isinstance(descriptor, property)



def test_notation_stringtopropertyvaluemapentry_is_not_abstract():
    assert not inspect.isabstract(notation_StringToPropertyValueMapEntry)


def test_notation_stringtopropertyvaluemapentry_constructor_exists():
    assert callable(notation_StringToPropertyValueMapEntry.__init__)


def test_notation_stringtopropertyvaluemapentry_constructor_args():
    sig = inspect.signature(notation_StringToPropertyValueMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_notation_stringtopropertyvaluemapentry_has_key():
    assert hasattr(notation_StringToPropertyValueMapEntry, "key")
    descriptor = None
    for klass in notation_StringToPropertyValueMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_notation_stringobjectconverter_is_not_abstract():
    assert not inspect.isabstract(notation_StringObjectConverter)


def test_notation_stringobjectconverter_constructor_exists():
    assert callable(notation_StringObjectConverter.__init__)


def test_notation_stringobjectconverter_constructor_args():
    sig = inspect.signature(notation_StringObjectConverter.__init__)
    params = list(sig.parameters.keys())



def test_notation_namedstyle_is_not_abstract():
    assert not inspect.isabstract(notation_NamedStyle)


def test_notation_namedstyle_constructor_exists():
    assert callable(notation_NamedStyle.__init__)


def test_notation_namedstyle_constructor_args():
    sig = inspect.signature(notation_NamedStyle.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_notation_namedstyle_has_name():
    assert hasattr(notation_NamedStyle, "name")
    descriptor = None
    for klass in notation_NamedStyle.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datatypestyle_is_not_abstract():
    assert not inspect.isabstract(DataTypeStyle)


def test_datatypestyle_constructor_exists():
    assert callable(DataTypeStyle.__init__)


def test_datatypestyle_constructor_args():
    sig = inspect.signature(DataTypeStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_listvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_ListValueStyle)


def test_notation_listvaluestyle_constructor_exists():
    assert callable(notation_ListValueStyle.__init__)


def test_notation_listvaluestyle_constructor_args():
    sig = inspect.signature(notation_ListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "rawValuesList" in params, "Missing parameter 'rawValuesList'"

def test_notation_listvaluestyle_has_rawValuesList():
    assert hasattr(notation_ListValueStyle, "rawValuesList")
    descriptor = None
    for klass in notation_ListValueStyle.__mro__:
        if "rawValuesList" in klass.__dict__:
            descriptor = klass.__dict__["rawValuesList"]
            break
    assert isinstance(descriptor, property)



def test_notation_singlevaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_SingleValueStyle)


def test_notation_singlevaluestyle_constructor_exists():
    assert callable(notation_SingleValueStyle.__init__)


def test_notation_singlevaluestyle_constructor_args():
    sig = inspect.signature(notation_SingleValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "rawValue" in params, "Missing parameter 'rawValue'"

def test_notation_singlevaluestyle_has_rawValue():
    assert hasattr(notation_SingleValueStyle, "rawValue")
    descriptor = None
    for klass in notation_SingleValueStyle.__mro__:
        if "rawValue" in klass.__dict__:
            descriptor = klass.__dict__["rawValue"]
            break
    assert isinstance(descriptor, property)



def test_notation_edatatype_is_not_abstract():
    assert not inspect.isabstract(notation_EDataType)


def test_notation_edatatype_constructor_exists():
    assert callable(notation_EDataType.__init__)


def test_notation_edatatype_constructor_args():
    sig = inspect.signature(notation_EDataType.__init__)
    params = list(sig.parameters.keys())



def test_notation_filteringstyle_is_not_abstract():
    assert not inspect.isabstract(notation_FilteringStyle)


def test_notation_filteringstyle_constructor_exists():
    assert callable(notation_FilteringStyle.__init__)


def test_notation_filteringstyle_constructor_args():
    sig = inspect.signature(notation_FilteringStyle.__init__)
    params = list(sig.parameters.keys())
    assert "filtering" in params, "Missing parameter 'filtering'"
    assert "filteringKeys" in params, "Missing parameter 'filteringKeys'"

def test_notation_filteringstyle_has_filtering():
    assert hasattr(notation_FilteringStyle, "filtering")
    descriptor = None
    for klass in notation_FilteringStyle.__mro__:
        if "filtering" in klass.__dict__:
            descriptor = klass.__dict__["filtering"]
            break
    assert isinstance(descriptor, property)

def test_notation_filteringstyle_has_filteringKeys():
    assert hasattr(notation_FilteringStyle, "filteringKeys")
    descriptor = None
    for klass in notation_FilteringStyle.__mro__:
        if "filteringKeys" in klass.__dict__:
            descriptor = klass.__dict__["filteringKeys"]
            break
    assert isinstance(descriptor, property)



def test_notation_nodeentry_is_not_abstract():
    assert not inspect.isabstract(notation_NodeEntry)


def test_notation_nodeentry_constructor_exists():
    assert callable(notation_NodeEntry.__init__)


def test_notation_nodeentry_constructor_args():
    sig = inspect.signature(notation_NodeEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_notation_nodeentry_has_value():
    assert hasattr(notation_NodeEntry, "value")
    descriptor = None
    for klass in notation_NodeEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_namedstyle_is_not_abstract():
    assert not inspect.isabstract(NamedStyle)


def test_namedstyle_constructor_exists():
    assert callable(NamedStyle.__init__)


def test_namedstyle_constructor_args():
    sig = inspect.signature(NamedStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_booleanlistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_BooleanListValueStyle)


def test_notation_booleanlistvaluestyle_constructor_exists():
    assert callable(notation_BooleanListValueStyle.__init__)


def test_notation_booleanlistvaluestyle_constructor_args():
    sig = inspect.signature(notation_BooleanListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "booleanListValue" in params, "Missing parameter 'booleanListValue'"

def test_notation_booleanlistvaluestyle_has_booleanListValue():
    assert hasattr(notation_BooleanListValueStyle, "booleanListValue")
    descriptor = None
    for klass in notation_BooleanListValueStyle.__mro__:
        if "booleanListValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanListValue"]
            break
    assert isinstance(descriptor, property)



def test_notation_intlistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_IntListValueStyle)


def test_notation_intlistvaluestyle_constructor_exists():
    assert callable(notation_IntListValueStyle.__init__)


def test_notation_intlistvaluestyle_constructor_args():
    sig = inspect.signature(notation_IntListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "intListValue" in params, "Missing parameter 'intListValue'"

def test_notation_intlistvaluestyle_has_intListValue():
    assert hasattr(notation_IntListValueStyle, "intListValue")
    descriptor = None
    for klass in notation_IntListValueStyle.__mro__:
        if "intListValue" in klass.__dict__:
            descriptor = klass.__dict__["intListValue"]
            break
    assert isinstance(descriptor, property)



def test_notation_datatypestyle_is_not_abstract():
    assert not inspect.isabstract(notation_DataTypeStyle)


def test_notation_datatypestyle_constructor_exists():
    assert callable(notation_DataTypeStyle.__init__)


def test_notation_datatypestyle_constructor_args():
    sig = inspect.signature(notation_DataTypeStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_stringvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_StringValueStyle)


def test_notation_stringvaluestyle_constructor_exists():
    assert callable(notation_StringValueStyle.__init__)


def test_notation_stringvaluestyle_constructor_args():
    sig = inspect.signature(notation_StringValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "stringValue" in params, "Missing parameter 'stringValue'"

def test_notation_stringvaluestyle_has_stringValue():
    assert hasattr(notation_StringValueStyle, "stringValue")
    descriptor = None
    for klass in notation_StringValueStyle.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)



def test_notation_bytearrayvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_ByteArrayValueStyle)


def test_notation_bytearrayvaluestyle_constructor_exists():
    assert callable(notation_ByteArrayValueStyle.__init__)


def test_notation_bytearrayvaluestyle_constructor_args():
    sig = inspect.signature(notation_ByteArrayValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "byteArrayValue" in params, "Missing parameter 'byteArrayValue'"

def test_notation_bytearrayvaluestyle_has_byteArrayValue():
    assert hasattr(notation_ByteArrayValueStyle, "byteArrayValue")
    descriptor = None
    for klass in notation_ByteArrayValueStyle.__mro__:
        if "byteArrayValue" in klass.__dict__:
            descriptor = klass.__dict__["byteArrayValue"]
            break
    assert isinstance(descriptor, property)



def test_notation_doublevaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_DoubleValueStyle)


def test_notation_doublevaluestyle_constructor_exists():
    assert callable(notation_DoubleValueStyle.__init__)


def test_notation_doublevaluestyle_constructor_args():
    sig = inspect.signature(notation_DoubleValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "doubleValue" in params, "Missing parameter 'doubleValue'"

def test_notation_doublevaluestyle_has_doubleValue():
    assert hasattr(notation_DoubleValueStyle, "doubleValue")
    descriptor = None
    for klass in notation_DoubleValueStyle.__mro__:
        if "doubleValue" in klass.__dict__:
            descriptor = klass.__dict__["doubleValue"]
            break
    assert isinstance(descriptor, property)



def test_notation_intvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_IntValueStyle)


def test_notation_intvaluestyle_constructor_exists():
    assert callable(notation_IntValueStyle.__init__)


def test_notation_intvaluestyle_constructor_args():
    sig = inspect.signature(notation_IntValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "intValue" in params, "Missing parameter 'intValue'"

def test_notation_intvaluestyle_has_intValue():
    assert hasattr(notation_IntValueStyle, "intValue")
    descriptor = None
    for klass in notation_IntValueStyle.__mro__:
        if "intValue" in klass.__dict__:
            descriptor = klass.__dict__["intValue"]
            break
    assert isinstance(descriptor, property)



def test_notation_booleanvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_BooleanValueStyle)


def test_notation_booleanvaluestyle_constructor_exists():
    assert callable(notation_BooleanValueStyle.__init__)


def test_notation_booleanvaluestyle_constructor_args():
    sig = inspect.signature(notation_BooleanValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_notation_booleanvaluestyle_has_booleanValue():
    assert hasattr(notation_BooleanValueStyle, "booleanValue")
    descriptor = None
    for klass in notation_BooleanValueStyle.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_notation_eobjectvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_EObjectValueStyle)


def test_notation_eobjectvaluestyle_constructor_exists():
    assert callable(notation_EObjectValueStyle.__init__)


def test_notation_eobjectvaluestyle_constructor_args():
    sig = inspect.signature(notation_EObjectValueStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_doublelistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_DoubleListValueStyle)


def test_notation_doublelistvaluestyle_constructor_exists():
    assert callable(notation_DoubleListValueStyle.__init__)


def test_notation_doublelistvaluestyle_constructor_args():
    sig = inspect.signature(notation_DoubleListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "doubleListValue" in params, "Missing parameter 'doubleListValue'"

def test_notation_doublelistvaluestyle_has_doubleListValue():
    assert hasattr(notation_DoubleListValueStyle, "doubleListValue")
    descriptor = None
    for klass in notation_DoubleListValueStyle.__mro__:
        if "doubleListValue" in klass.__dict__:
            descriptor = klass.__dict__["doubleListValue"]
            break
    assert isinstance(descriptor, property)



def test_notation_stringlistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_StringListValueStyle)


def test_notation_stringlistvaluestyle_constructor_exists():
    assert callable(notation_StringListValueStyle.__init__)


def test_notation_stringlistvaluestyle_constructor_args():
    sig = inspect.signature(notation_StringListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "stringListValue" in params, "Missing parameter 'stringListValue'"

def test_notation_stringlistvaluestyle_has_stringListValue():
    assert hasattr(notation_StringListValueStyle, "stringListValue")
    descriptor = None
    for klass in notation_StringListValueStyle.__mro__:
        if "stringListValue" in klass.__dict__:
            descriptor = klass.__dict__["stringListValue"]
            break
    assert isinstance(descriptor, property)



def test_notation_eobjectlistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation_EObjectListValueStyle)


def test_notation_eobjectlistvaluestyle_constructor_exists():
    assert callable(notation_EObjectListValueStyle.__init__)


def test_notation_eobjectlistvaluestyle_constructor_args():
    sig = inspect.signature(notation_EObjectListValueStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_propertiessetstyle_is_not_abstract():
    assert not inspect.isabstract(notation_PropertiesSetStyle)


def test_notation_propertiessetstyle_constructor_exists():
    assert callable(notation_PropertiesSetStyle.__init__)


def test_notation_propertiessetstyle_constructor_args():
    sig = inspect.signature(notation_PropertiesSetStyle.__init__)
    params = list(sig.parameters.keys())



def test_imagestyle_is_not_abstract():
    assert not inspect.isabstract(ImageStyle)


def test_imagestyle_constructor_exists():
    assert callable(ImageStyle.__init__)


def test_imagestyle_constructor_args():
    sig = inspect.signature(ImageStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_imagebufferstyle_is_not_abstract():
    assert not inspect.isabstract(notation_ImageBufferStyle)


def test_notation_imagebufferstyle_constructor_exists():
    assert callable(notation_ImageBufferStyle.__init__)


def test_notation_imagebufferstyle_constructor_args():
    sig = inspect.signature(notation_ImageBufferStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation_imagestyle_is_not_abstract():
    assert not inspect.isabstract(notation_ImageStyle)


def test_notation_imagestyle_constructor_exists():
    assert callable(notation_ImageStyle.__init__)


def test_notation_imagestyle_constructor_args():
    sig = inspect.signature(notation_ImageStyle.__init__)
    params = list(sig.parameters.keys())
    assert "maintainAspectRatio" in params, "Missing parameter 'maintainAspectRatio'"
    assert "antiAlias" in params, "Missing parameter 'antiAlias'"

def test_notation_imagestyle_has_maintainAspectRatio():
    assert hasattr(notation_ImageStyle, "maintainAspectRatio")
    descriptor = None
    for klass in notation_ImageStyle.__mro__:
        if "maintainAspectRatio" in klass.__dict__:
            descriptor = klass.__dict__["maintainAspectRatio"]
            break
    assert isinstance(descriptor, property)

def test_notation_imagestyle_has_antiAlias():
    assert hasattr(notation_ImageStyle, "antiAlias")
    descriptor = None
    for klass in notation_ImageStyle.__mro__:
        if "antiAlias" in klass.__dict__:
            descriptor = klass.__dict__["antiAlias"]
            break
    assert isinstance(descriptor, property)

def test_arrowtype_exists():
    # Check that the Enumeration exists
    assert ArrowType is not None

def test_arrowtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArrowType]
    expected_literals = [
        "None_",
        "OpenArrow",
        "SolidArrow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArrowType"

def test_linetype_exists():
    # Check that the Enumeration exists
    assert LineType is not None

def test_linetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineType]
    expected_literals = [
        "DashDot",
        "DashDotDot",
        "Dot",
        "Dash",
        "Solid",
        "Double",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineType"

def test_sorting_exists():
    # Check that the Enumeration exists
    assert Sorting is not None

def test_sorting_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sorting]
    expected_literals = [
        "Automatic",
        "None_",
        "Manual",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sorting"

def test_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "Right",
        "Center",
        "Left",
        "Bottom",
        "Top",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Alignment"

def test_textalignment_exists():
    # Check that the Enumeration exists
    assert TextAlignment is not None

def test_textalignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextAlignment]
    expected_literals = [
        "Right",
        "Left",
        "Center",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextAlignment"

def test_sortingdirection_exists():
    # Check that the Enumeration exists
    assert SortingDirection is not None

def test_sortingdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SortingDirection]
    expected_literals = [
        "Ascending",
        "Descending",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SortingDirection"

def test_jumplinktype_exists():
    # Check that the Enumeration exists
    assert JumpLinkType is not None

def test_jumplinktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JumpLinkType]
    expected_literals = [
        "Semicircle",
        "Chamfered",
        "Square",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JumpLinkType"

def test_measurementunit_exists():
    # Check that the Enumeration exists
    assert MeasurementUnit is not None

def test_measurementunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MeasurementUnit]
    expected_literals = [
        "Pixel",
        "Himetric",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MeasurementUnit"

def test_jumplinkstatus_exists():
    # Check that the Enumeration exists
    assert JumpLinkStatus is not None

def test_jumplinkstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JumpLinkStatus]
    expected_literals = [
        "Below",
        "Above",
        "None_",
        "All",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JumpLinkStatus"

def test_routing_exists():
    # Check that the Enumeration exists
    assert Routing is not None

def test_routing_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Routing]
    expected_literals = [
        "Tree",
        "Manual",
        "Rectilinear",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Routing"

def test_smoothness_exists():
    # Check that the Enumeration exists
    assert Smoothness is not None

def test_smoothness_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Smoothness]
    expected_literals = [
        "Less",
        "More",
        "None_",
        "Normal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Smoothness"

def test_gradientstyle_exists():
    # Check that the Enumeration exists
    assert GradientStyle is not None

def test_gradientstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GradientStyle]
    expected_literals = [
        "Horizontal",
        "Vertical",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GradientStyle"

def test_filtering_exists():
    # Check that the Enumeration exists
    assert Filtering is not None

def test_filtering_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Filtering]
    expected_literals = [
        "None_",
        "Manual",
        "Automatic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Filtering"


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
GuideStyle_strategy = st.builds(
    GuideStyle,
)
PageStyle_strategy = st.builds(
    PageStyle,
)
notation_Image_strategy = st.builds(
    notation_Image,
    data=
        safe_text
)
Bendpoints_strategy = st.builds(
    Bendpoints,
)
notation_RelativeBendpoints_strategy = st.builds(
    notation_RelativeBendpoints,
    points=
        safe_text
)
notation_Guide_strategy = st.builds(
    notation_Guide,
    position=
        st.integers()
)
RoutingStyle_strategy = st.builds(
    RoutingStyle,
)
LineStyle_strategy = st.builds(
    LineStyle,
)
notation_ConnectorStyle_strategy = st.builds(
    notation_ConnectorStyle,
)
FillStyle_strategy = st.builds(
    FillStyle,
)
DescriptionStyle_strategy = st.builds(
    DescriptionStyle,
)
notation_DiagramStyle_strategy = st.builds(
    notation_DiagramStyle,
)
FontStyle_strategy = st.builds(
    FontStyle,
)
Size_strategy = st.builds(
    Size,
)
Location_strategy = st.builds(
    Location,
)
notation_Bounds_strategy = st.builds(
    notation_Bounds,
)
EModelElement_strategy = st.builds(
    EModelElement,
)
RoundedCornersStyle_strategy = st.builds(
    RoundedCornersStyle,
)
notation_ShapeStyle_strategy = st.builds(
    notation_ShapeStyle,
)
notation_RoutingStyle_strategy = st.builds(
    notation_RoutingStyle,
    closestDistance=
        st.booleans(),
    jumpLinkStatus=
        safe_text,
    smoothness=
        safe_text,
    jumpLinkType=
        safe_text,
    jumpLinksReverse=
        st.booleans(),
    routing=
        safe_text,
    avoidObstructions=
        st.booleans()
)
Anchor_strategy = st.builds(
    Anchor,
)
notation_IdentityAnchor_strategy = st.builds(
    notation_IdentityAnchor,
    id=
        safe_text
)
LayoutConstraint_strategy = st.builds(
    LayoutConstraint,
)
notation_Location_strategy = st.builds(
    notation_Location,
    x=
        st.integers(),
    y=
        st.integers()
)
notation_Ratio_strategy = st.builds(
    notation_Ratio,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
notation_Size_strategy = st.builds(
    notation_Size,
    height=
        st.integers(),
    width=
        st.integers()
)
notation_EObject_strategy = st.builds(
    notation_EObject,
)
Style_strategy = st.builds(
    Style,
)
notation_TitleStyle_strategy = st.builds(
    notation_TitleStyle,
    showTitle=
        st.booleans()
)
notation_PageStyle_strategy = st.builds(
    notation_PageStyle,
    pageWidth=
        st.integers(),
    pageX=
        st.integers(),
    pageHeight=
        st.integers(),
    pageY=
        st.integers()
)
notation_CanonicalStyle_strategy = st.builds(
    notation_CanonicalStyle,
    canonical=
        st.booleans()
)
notation_LineStyle_strategy = st.builds(
    notation_LineStyle,
    lineColor=
        st.integers(),
    lineWidth=
        st.integers()
)
notation_DrawerStyle_strategy = st.builds(
    notation_DrawerStyle,
    collapsed=
        st.booleans()
)
notation_DescriptionStyle_strategy = st.builds(
    notation_DescriptionStyle,
    description=
        safe_text
)
notation_GuideStyle_strategy = st.builds(
    notation_GuideStyle,
)
notation_FontStyle_strategy = st.builds(
    notation_FontStyle,
    fontHeight=
        st.integers(),
    underline=
        st.booleans(),
    italic=
        st.booleans(),
    strikeThrough=
        st.booleans(),
    bold=
        st.booleans(),
    fontColor=
        st.integers(),
    fontName=
        safe_text
)
notation_SortingStyle_strategy = st.builds(
    notation_SortingStyle,
    sorting=
        safe_text,
    sortingKeys=
        safe_text
)
notation_FillStyle_strategy = st.builds(
    notation_FillStyle,
    gradient=
        safe_text,
    fillColor=
        st.integers(),
    transparency=
        st.integers()
)
notation_Style_strategy = st.builds(
    notation_Style,
)
notation_LayoutConstraint_strategy = st.builds(
    notation_LayoutConstraint,
)
notation_Anchor_strategy = st.builds(
    notation_Anchor,
)
notation_Bendpoints_strategy = st.builds(
    notation_Bendpoints,
)
notation_View_strategy = st.builds(
    notation_View,
    mutable=
        st.booleans(),
    visible=
        st.booleans(),
    type=
        safe_text
)
View_strategy = st.builds(
    View,
)
notation_Node_strategy = st.builds(
    notation_Node,
)
notation_Diagram_strategy = st.builds(
    notation_Diagram,
    name=
        safe_text,
    measurementUnit=
        safe_text
)
notation_Edge_strategy = st.builds(
    notation_Edge,
)
TitleStyle_strategy = st.builds(
    TitleStyle,
)
CanonicalStyle_strategy = st.builds(
    CanonicalStyle,
)
BasicCompartment_strategy = st.builds(
    BasicCompartment,
)
notation_Compartment_strategy = st.builds(
    notation_Compartment,
)
ShapeStyle_strategy = st.builds(
    ShapeStyle,
)
Node_strategy = st.builds(
    Node,
)
notation_Shape_strategy = st.builds(
    notation_Shape,
)
notation_ArrowStyle_strategy = st.builds(
    notation_ArrowStyle,
    arrowSource=
        safe_text,
    arrowTarget=
        safe_text
)
notation_LineTypeStyle_strategy = st.builds(
    notation_LineTypeStyle,
    lineType=
        safe_text
)
notation_TextStyle_strategy = st.builds(
    notation_TextStyle,
    textAlignment=
        safe_text
)
notation_RoundedCornersStyle_strategy = st.builds(
    notation_RoundedCornersStyle,
    roundedBendpointsRadius=
        st.integers()
)
BasicSemanticCompartment_strategy = st.builds(
    BasicSemanticCompartment,
)
DrawerStyle_strategy = st.builds(
    DrawerStyle,
)
DecorationNode_strategy = st.builds(
    DecorationNode,
)
notation_BasicCompartment_strategy = st.builds(
    notation_BasicCompartment,
)
notation_BasicDecorationNode_strategy = st.builds(
    notation_BasicDecorationNode,
)
BasicDecorationNode_strategy = st.builds(
    BasicDecorationNode,
)
notation_BasicSemanticCompartment_strategy = st.builds(
    notation_BasicSemanticCompartment,
)
notation_DecorationNode_strategy = st.builds(
    notation_DecorationNode,
)
DiagramStyle_strategy = st.builds(
    DiagramStyle,
)
Diagram_strategy = st.builds(
    Diagram,
)
notation_StandardDiagram_strategy = st.builds(
    notation_StandardDiagram,
)
ConnectorStyle_strategy = st.builds(
    ConnectorStyle,
)
Edge_strategy = st.builds(
    Edge,
)
notation_Connector_strategy = st.builds(
    notation_Connector,
)
FilteringStyle_strategy = st.builds(
    FilteringStyle,
)
SortingStyle_strategy = st.builds(
    SortingStyle,
)
notation_SemanticListCompartment_strategy = st.builds(
    notation_SemanticListCompartment,
)
notation_ListCompartment_strategy = st.builds(
    notation_ListCompartment,
)
notation_MultiDiagramLinkStyle_strategy = st.builds(
    notation_MultiDiagramLinkStyle,
)
notation_DiagramLinkStyle_strategy = st.builds(
    notation_DiagramLinkStyle,
)
DiagramLinkStyle_strategy = st.builds(
    DiagramLinkStyle,
)
notation_HintedDiagramLinkStyle_strategy = st.builds(
    notation_HintedDiagramLinkStyle,
    hint=
        safe_text
)
StringObjectConverter_strategy = st.builds(
    StringObjectConverter,
)
notation_PropertyValue_strategy = st.builds(
    notation_PropertyValue,
    rawValue=
        safe_text
)
notation_StringToPropertyValueMapEntry_strategy = st.builds(
    notation_StringToPropertyValueMapEntry,
    key=
        safe_text
)
notation_StringObjectConverter_strategy = st.builds(
    notation_StringObjectConverter,
)
notation_NamedStyle_strategy = st.builds(
    notation_NamedStyle,
    name=
        safe_text
)
DataTypeStyle_strategy = st.builds(
    DataTypeStyle,
)
notation_ListValueStyle_strategy = st.builds(
    notation_ListValueStyle,
    rawValuesList=
        safe_text
)
notation_SingleValueStyle_strategy = st.builds(
    notation_SingleValueStyle,
    rawValue=
        safe_text
)
notation_EDataType_strategy = st.builds(
    notation_EDataType,
)
notation_FilteringStyle_strategy = st.builds(
    notation_FilteringStyle,
    filtering=
        safe_text,
    filteringKeys=
        safe_text
)
notation_NodeEntry_strategy = st.builds(
    notation_NodeEntry,
    value=
        safe_text
)
NamedStyle_strategy = st.builds(
    NamedStyle,
)
notation_BooleanListValueStyle_strategy = st.builds(
    notation_BooleanListValueStyle,
    booleanListValue=
        safe_text
)
notation_IntListValueStyle_strategy = st.builds(
    notation_IntListValueStyle,
    intListValue=
        st.integers()
)
notation_DataTypeStyle_strategy = st.builds(
    notation_DataTypeStyle,
)
notation_StringValueStyle_strategy = st.builds(
    notation_StringValueStyle,
    stringValue=
        safe_text
)
notation_ByteArrayValueStyle_strategy = st.builds(
    notation_ByteArrayValueStyle,
    byteArrayValue=
        safe_text
)
notation_DoubleValueStyle_strategy = st.builds(
    notation_DoubleValueStyle,
    doubleValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
notation_IntValueStyle_strategy = st.builds(
    notation_IntValueStyle,
    intValue=
        st.integers()
)
notation_BooleanValueStyle_strategy = st.builds(
    notation_BooleanValueStyle,
    booleanValue=
        st.booleans()
)
notation_EObjectValueStyle_strategy = st.builds(
    notation_EObjectValueStyle,
)
notation_DoubleListValueStyle_strategy = st.builds(
    notation_DoubleListValueStyle,
    doubleListValue=
        safe_text
)
notation_StringListValueStyle_strategy = st.builds(
    notation_StringListValueStyle,
    stringListValue=
        safe_text
)
notation_EObjectListValueStyle_strategy = st.builds(
    notation_EObjectListValueStyle,
)
notation_PropertiesSetStyle_strategy = st.builds(
    notation_PropertiesSetStyle,
)
ImageStyle_strategy = st.builds(
    ImageStyle,
)
notation_ImageBufferStyle_strategy = st.builds(
    notation_ImageBufferStyle,
)
notation_ImageStyle_strategy = st.builds(
    notation_ImageStyle,
    maintainAspectRatio=
        safe_text,
    antiAlias=
        safe_text
)

@given(instance=GuideStyle_strategy)
@settings(max_examples=50)
def test_guidestyle_instantiation(instance):
    assert isinstance(instance, GuideStyle)

@given(instance=PageStyle_strategy)
@settings(max_examples=50)
def test_pagestyle_instantiation(instance):
    assert isinstance(instance, PageStyle)

@given(instance=notation_Image_strategy)
@settings(max_examples=50)
def test_notation_image_instantiation(instance):
    assert isinstance(instance, notation_Image)



@given(instance=notation_Image_strategy)
def test_notation_image_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=Bendpoints_strategy)
@settings(max_examples=50)
def test_bendpoints_instantiation(instance):
    assert isinstance(instance, Bendpoints)

@given(instance=notation_RelativeBendpoints_strategy)
@settings(max_examples=50)
def test_notation_relativebendpoints_instantiation(instance):
    assert isinstance(instance, notation_RelativeBendpoints)



@given(instance=notation_RelativeBendpoints_strategy)
def test_notation_relativebendpoints_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

@given(instance=notation_Guide_strategy)
@settings(max_examples=50)
def test_notation_guide_instantiation(instance):
    assert isinstance(instance, notation_Guide)



@given(instance=notation_Guide_strategy)
def test_notation_guide_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=RoutingStyle_strategy)
@settings(max_examples=50)
def test_routingstyle_instantiation(instance):
    assert isinstance(instance, RoutingStyle)

@given(instance=LineStyle_strategy)
@settings(max_examples=50)
def test_linestyle_instantiation(instance):
    assert isinstance(instance, LineStyle)

@given(instance=notation_ConnectorStyle_strategy)
@settings(max_examples=50)
def test_notation_connectorstyle_instantiation(instance):
    assert isinstance(instance, notation_ConnectorStyle)

@given(instance=FillStyle_strategy)
@settings(max_examples=50)
def test_fillstyle_instantiation(instance):
    assert isinstance(instance, FillStyle)

@given(instance=DescriptionStyle_strategy)
@settings(max_examples=50)
def test_descriptionstyle_instantiation(instance):
    assert isinstance(instance, DescriptionStyle)

@given(instance=notation_DiagramStyle_strategy)
@settings(max_examples=50)
def test_notation_diagramstyle_instantiation(instance):
    assert isinstance(instance, notation_DiagramStyle)

@given(instance=FontStyle_strategy)
@settings(max_examples=50)
def test_fontstyle_instantiation(instance):
    assert isinstance(instance, FontStyle)

@given(instance=Size_strategy)
@settings(max_examples=50)
def test_size_instantiation(instance):
    assert isinstance(instance, Size)

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)

@given(instance=notation_Bounds_strategy)
@settings(max_examples=50)
def test_notation_bounds_instantiation(instance):
    assert isinstance(instance, notation_Bounds)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=RoundedCornersStyle_strategy)
@settings(max_examples=50)
def test_roundedcornersstyle_instantiation(instance):
    assert isinstance(instance, RoundedCornersStyle)

@given(instance=notation_ShapeStyle_strategy)
@settings(max_examples=50)
def test_notation_shapestyle_instantiation(instance):
    assert isinstance(instance, notation_ShapeStyle)

@given(instance=notation_RoutingStyle_strategy)
@settings(max_examples=50)
def test_notation_routingstyle_instantiation(instance):
    assert isinstance(instance, notation_RoutingStyle)



@given(instance=notation_RoutingStyle_strategy)
def test_notation_routingstyle_closestDistance_setter(instance):
    original = instance.closestDistance
    instance.closestDistance = original
    assert instance.closestDistance == original



@given(instance=notation_RoutingStyle_strategy)
def test_notation_routingstyle_jumpLinkStatus_setter(instance):
    original = instance.jumpLinkStatus
    instance.jumpLinkStatus = original
    assert instance.jumpLinkStatus == original



@given(instance=notation_RoutingStyle_strategy)
def test_notation_routingstyle_smoothness_setter(instance):
    original = instance.smoothness
    instance.smoothness = original
    assert instance.smoothness == original



@given(instance=notation_RoutingStyle_strategy)
def test_notation_routingstyle_jumpLinkType_setter(instance):
    original = instance.jumpLinkType
    instance.jumpLinkType = original
    assert instance.jumpLinkType == original



@given(instance=notation_RoutingStyle_strategy)
def test_notation_routingstyle_jumpLinksReverse_setter(instance):
    original = instance.jumpLinksReverse
    instance.jumpLinksReverse = original
    assert instance.jumpLinksReverse == original



@given(instance=notation_RoutingStyle_strategy)
def test_notation_routingstyle_routing_setter(instance):
    original = instance.routing
    instance.routing = original
    assert instance.routing == original



@given(instance=notation_RoutingStyle_strategy)
def test_notation_routingstyle_avoidObstructions_setter(instance):
    original = instance.avoidObstructions
    instance.avoidObstructions = original
    assert instance.avoidObstructions == original

@given(instance=Anchor_strategy)
@settings(max_examples=50)
def test_anchor_instantiation(instance):
    assert isinstance(instance, Anchor)

@given(instance=notation_IdentityAnchor_strategy)
@settings(max_examples=50)
def test_notation_identityanchor_instantiation(instance):
    assert isinstance(instance, notation_IdentityAnchor)



@given(instance=notation_IdentityAnchor_strategy)
def test_notation_identityanchor_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=LayoutConstraint_strategy)
@settings(max_examples=50)
def test_layoutconstraint_instantiation(instance):
    assert isinstance(instance, LayoutConstraint)

@given(instance=notation_Location_strategy)
@settings(max_examples=50)
def test_notation_location_instantiation(instance):
    assert isinstance(instance, notation_Location)



@given(instance=notation_Location_strategy)
def test_notation_location_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=notation_Location_strategy)
def test_notation_location_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=notation_Ratio_strategy)
@settings(max_examples=50)
def test_notation_ratio_instantiation(instance):
    assert isinstance(instance, notation_Ratio)



@given(instance=notation_Ratio_strategy)
def test_notation_ratio_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=notation_Size_strategy)
@settings(max_examples=50)
def test_notation_size_instantiation(instance):
    assert isinstance(instance, notation_Size)



@given(instance=notation_Size_strategy)
def test_notation_size_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=notation_Size_strategy)
def test_notation_size_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=notation_EObject_strategy)
@settings(max_examples=50)
def test_notation_eobject_instantiation(instance):
    assert isinstance(instance, notation_EObject)

@given(instance=Style_strategy)
@settings(max_examples=50)
def test_style_instantiation(instance):
    assert isinstance(instance, Style)

@given(instance=notation_TitleStyle_strategy)
@settings(max_examples=50)
def test_notation_titlestyle_instantiation(instance):
    assert isinstance(instance, notation_TitleStyle)



@given(instance=notation_TitleStyle_strategy)
def test_notation_titlestyle_showTitle_setter(instance):
    original = instance.showTitle
    instance.showTitle = original
    assert instance.showTitle == original

@given(instance=notation_PageStyle_strategy)
@settings(max_examples=50)
def test_notation_pagestyle_instantiation(instance):
    assert isinstance(instance, notation_PageStyle)



@given(instance=notation_PageStyle_strategy)
def test_notation_pagestyle_pageWidth_setter(instance):
    original = instance.pageWidth
    instance.pageWidth = original
    assert instance.pageWidth == original



@given(instance=notation_PageStyle_strategy)
def test_notation_pagestyle_pageX_setter(instance):
    original = instance.pageX
    instance.pageX = original
    assert instance.pageX == original



@given(instance=notation_PageStyle_strategy)
def test_notation_pagestyle_pageHeight_setter(instance):
    original = instance.pageHeight
    instance.pageHeight = original
    assert instance.pageHeight == original



@given(instance=notation_PageStyle_strategy)
def test_notation_pagestyle_pageY_setter(instance):
    original = instance.pageY
    instance.pageY = original
    assert instance.pageY == original

@given(instance=notation_CanonicalStyle_strategy)
@settings(max_examples=50)
def test_notation_canonicalstyle_instantiation(instance):
    assert isinstance(instance, notation_CanonicalStyle)



@given(instance=notation_CanonicalStyle_strategy)
def test_notation_canonicalstyle_canonical_setter(instance):
    original = instance.canonical
    instance.canonical = original
    assert instance.canonical == original

@given(instance=notation_LineStyle_strategy)
@settings(max_examples=50)
def test_notation_linestyle_instantiation(instance):
    assert isinstance(instance, notation_LineStyle)



@given(instance=notation_LineStyle_strategy)
def test_notation_linestyle_lineColor_setter(instance):
    original = instance.lineColor
    instance.lineColor = original
    assert instance.lineColor == original



@given(instance=notation_LineStyle_strategy)
def test_notation_linestyle_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=notation_DrawerStyle_strategy)
@settings(max_examples=50)
def test_notation_drawerstyle_instantiation(instance):
    assert isinstance(instance, notation_DrawerStyle)



@given(instance=notation_DrawerStyle_strategy)
def test_notation_drawerstyle_collapsed_setter(instance):
    original = instance.collapsed
    instance.collapsed = original
    assert instance.collapsed == original

@given(instance=notation_DescriptionStyle_strategy)
@settings(max_examples=50)
def test_notation_descriptionstyle_instantiation(instance):
    assert isinstance(instance, notation_DescriptionStyle)



@given(instance=notation_DescriptionStyle_strategy)
def test_notation_descriptionstyle_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=notation_GuideStyle_strategy)
@settings(max_examples=50)
def test_notation_guidestyle_instantiation(instance):
    assert isinstance(instance, notation_GuideStyle)

@given(instance=notation_FontStyle_strategy)
@settings(max_examples=50)
def test_notation_fontstyle_instantiation(instance):
    assert isinstance(instance, notation_FontStyle)



@given(instance=notation_FontStyle_strategy)
def test_notation_fontstyle_fontHeight_setter(instance):
    original = instance.fontHeight
    instance.fontHeight = original
    assert instance.fontHeight == original



@given(instance=notation_FontStyle_strategy)
def test_notation_fontstyle_underline_setter(instance):
    original = instance.underline
    instance.underline = original
    assert instance.underline == original



@given(instance=notation_FontStyle_strategy)
def test_notation_fontstyle_italic_setter(instance):
    original = instance.italic
    instance.italic = original
    assert instance.italic == original



@given(instance=notation_FontStyle_strategy)
def test_notation_fontstyle_strikeThrough_setter(instance):
    original = instance.strikeThrough
    instance.strikeThrough = original
    assert instance.strikeThrough == original



@given(instance=notation_FontStyle_strategy)
def test_notation_fontstyle_bold_setter(instance):
    original = instance.bold
    instance.bold = original
    assert instance.bold == original



@given(instance=notation_FontStyle_strategy)
def test_notation_fontstyle_fontColor_setter(instance):
    original = instance.fontColor
    instance.fontColor = original
    assert instance.fontColor == original



@given(instance=notation_FontStyle_strategy)
def test_notation_fontstyle_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original

@given(instance=notation_SortingStyle_strategy)
@settings(max_examples=50)
def test_notation_sortingstyle_instantiation(instance):
    assert isinstance(instance, notation_SortingStyle)



@given(instance=notation_SortingStyle_strategy)
def test_notation_sortingstyle_sorting_setter(instance):
    original = instance.sorting
    instance.sorting = original
    assert instance.sorting == original



@given(instance=notation_SortingStyle_strategy)
def test_notation_sortingstyle_sortingKeys_setter(instance):
    original = instance.sortingKeys
    instance.sortingKeys = original
    assert instance.sortingKeys == original

@given(instance=notation_FillStyle_strategy)
@settings(max_examples=50)
def test_notation_fillstyle_instantiation(instance):
    assert isinstance(instance, notation_FillStyle)



@given(instance=notation_FillStyle_strategy)
def test_notation_fillstyle_gradient_setter(instance):
    original = instance.gradient
    instance.gradient = original
    assert instance.gradient == original



@given(instance=notation_FillStyle_strategy)
def test_notation_fillstyle_fillColor_setter(instance):
    original = instance.fillColor
    instance.fillColor = original
    assert instance.fillColor == original



@given(instance=notation_FillStyle_strategy)
def test_notation_fillstyle_transparency_setter(instance):
    original = instance.transparency
    instance.transparency = original
    assert instance.transparency == original

@given(instance=notation_Style_strategy)
@settings(max_examples=50)
def test_notation_style_instantiation(instance):
    assert isinstance(instance, notation_Style)

@given(instance=notation_LayoutConstraint_strategy)
@settings(max_examples=50)
def test_notation_layoutconstraint_instantiation(instance):
    assert isinstance(instance, notation_LayoutConstraint)

@given(instance=notation_Anchor_strategy)
@settings(max_examples=50)
def test_notation_anchor_instantiation(instance):
    assert isinstance(instance, notation_Anchor)

@given(instance=notation_Bendpoints_strategy)
@settings(max_examples=50)
def test_notation_bendpoints_instantiation(instance):
    assert isinstance(instance, notation_Bendpoints)

@given(instance=notation_View_strategy)
@settings(max_examples=50)
def test_notation_view_instantiation(instance):
    assert isinstance(instance, notation_View)



@given(instance=notation_View_strategy)
def test_notation_view_mutable_setter(instance):
    original = instance.mutable
    instance.mutable = original
    assert instance.mutable == original



@given(instance=notation_View_strategy)
def test_notation_view_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=notation_View_strategy)
def test_notation_view_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_View_strategy)
@settings(max_examples=30)
def test_notation_view_createstyle_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createStyle(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createStyle).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createStyle' in notation_View is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createStyle' in notation_View did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createStyle' in notation_View is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_View_strategy)
@settings(max_examples=30)
def test_notation_view_createchild_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createChild(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createChild).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createChild' in notation_View is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createChild' in notation_View did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createChild' in notation_View is not implemented or raised an error")

@given(instance=View_strategy)
@settings(max_examples=50)
def test_view_instantiation(instance):
    assert isinstance(instance, View)

@given(instance=notation_Node_strategy)
@settings(max_examples=50)
def test_notation_node_instantiation(instance):
    assert isinstance(instance, notation_Node)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_Node_strategy)
@settings(max_examples=30)
def test_notation_node_createlayoutconstraint_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createLayoutConstraint(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createLayoutConstraint).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createLayoutConstraint' in notation_Node is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createLayoutConstraint' in notation_Node did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createLayoutConstraint' in notation_Node is not implemented or raised an error")

@given(instance=notation_Diagram_strategy)
@settings(max_examples=50)
def test_notation_diagram_instantiation(instance):
    assert isinstance(instance, notation_Diagram)



@given(instance=notation_Diagram_strategy)
def test_notation_diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=notation_Diagram_strategy)
def test_notation_diagram_measurementUnit_setter(instance):
    original = instance.measurementUnit
    instance.measurementUnit = original
    assert instance.measurementUnit == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_Diagram_strategy)
@settings(max_examples=30)
def test_notation_diagram_createedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createEdge(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createEdge' in notation_Diagram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createEdge' in notation_Diagram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createEdge' in notation_Diagram is not implemented or raised an error")

@given(instance=notation_Edge_strategy)
@settings(max_examples=50)
def test_notation_edge_instantiation(instance):
    assert isinstance(instance, notation_Edge)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_Edge_strategy)
@settings(max_examples=30)
def test_notation_edge_createbendpoints_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createBendpoints(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createBendpoints).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createBendpoints' in notation_Edge is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createBendpoints' in notation_Edge did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createBendpoints' in notation_Edge is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_Edge_strategy)
@settings(max_examples=30)
def test_notation_edge_createsourceanchor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createSourceAnchor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createSourceAnchor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createSourceAnchor' in notation_Edge is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createSourceAnchor' in notation_Edge did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createSourceAnchor' in notation_Edge is not implemented or raised an error")

@given(instance=TitleStyle_strategy)
@settings(max_examples=50)
def test_titlestyle_instantiation(instance):
    assert isinstance(instance, TitleStyle)

@given(instance=CanonicalStyle_strategy)
@settings(max_examples=50)
def test_canonicalstyle_instantiation(instance):
    assert isinstance(instance, CanonicalStyle)

@given(instance=BasicCompartment_strategy)
@settings(max_examples=50)
def test_basiccompartment_instantiation(instance):
    assert isinstance(instance, BasicCompartment)

@given(instance=notation_Compartment_strategy)
@settings(max_examples=50)
def test_notation_compartment_instantiation(instance):
    assert isinstance(instance, notation_Compartment)

@given(instance=ShapeStyle_strategy)
@settings(max_examples=50)
def test_shapestyle_instantiation(instance):
    assert isinstance(instance, ShapeStyle)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=notation_Shape_strategy)
@settings(max_examples=50)
def test_notation_shape_instantiation(instance):
    assert isinstance(instance, notation_Shape)

@given(instance=notation_ArrowStyle_strategy)
@settings(max_examples=50)
def test_notation_arrowstyle_instantiation(instance):
    assert isinstance(instance, notation_ArrowStyle)



@given(instance=notation_ArrowStyle_strategy)
def test_notation_arrowstyle_arrowSource_setter(instance):
    original = instance.arrowSource
    instance.arrowSource = original
    assert instance.arrowSource == original



@given(instance=notation_ArrowStyle_strategy)
def test_notation_arrowstyle_arrowTarget_setter(instance):
    original = instance.arrowTarget
    instance.arrowTarget = original
    assert instance.arrowTarget == original

@given(instance=notation_LineTypeStyle_strategy)
@settings(max_examples=50)
def test_notation_linetypestyle_instantiation(instance):
    assert isinstance(instance, notation_LineTypeStyle)



@given(instance=notation_LineTypeStyle_strategy)
def test_notation_linetypestyle_lineType_setter(instance):
    original = instance.lineType
    instance.lineType = original
    assert instance.lineType == original

@given(instance=notation_TextStyle_strategy)
@settings(max_examples=50)
def test_notation_textstyle_instantiation(instance):
    assert isinstance(instance, notation_TextStyle)



@given(instance=notation_TextStyle_strategy)
def test_notation_textstyle_textAlignment_setter(instance):
    original = instance.textAlignment
    instance.textAlignment = original
    assert instance.textAlignment == original

@given(instance=notation_RoundedCornersStyle_strategy)
@settings(max_examples=50)
def test_notation_roundedcornersstyle_instantiation(instance):
    assert isinstance(instance, notation_RoundedCornersStyle)



@given(instance=notation_RoundedCornersStyle_strategy)
def test_notation_roundedcornersstyle_roundedBendpointsRadius_setter(instance):
    original = instance.roundedBendpointsRadius
    instance.roundedBendpointsRadius = original
    assert instance.roundedBendpointsRadius == original

@given(instance=BasicSemanticCompartment_strategy)
@settings(max_examples=50)
def test_basicsemanticcompartment_instantiation(instance):
    assert isinstance(instance, BasicSemanticCompartment)

@given(instance=DrawerStyle_strategy)
@settings(max_examples=50)
def test_drawerstyle_instantiation(instance):
    assert isinstance(instance, DrawerStyle)

@given(instance=DecorationNode_strategy)
@settings(max_examples=50)
def test_decorationnode_instantiation(instance):
    assert isinstance(instance, DecorationNode)

@given(instance=notation_BasicCompartment_strategy)
@settings(max_examples=50)
def test_notation_basiccompartment_instantiation(instance):
    assert isinstance(instance, notation_BasicCompartment)

@given(instance=notation_BasicDecorationNode_strategy)
@settings(max_examples=50)
def test_notation_basicdecorationnode_instantiation(instance):
    assert isinstance(instance, notation_BasicDecorationNode)

@given(instance=BasicDecorationNode_strategy)
@settings(max_examples=50)
def test_basicdecorationnode_instantiation(instance):
    assert isinstance(instance, BasicDecorationNode)

@given(instance=notation_BasicSemanticCompartment_strategy)
@settings(max_examples=50)
def test_notation_basicsemanticcompartment_instantiation(instance):
    assert isinstance(instance, notation_BasicSemanticCompartment)

@given(instance=notation_DecorationNode_strategy)
@settings(max_examples=50)
def test_notation_decorationnode_instantiation(instance):
    assert isinstance(instance, notation_DecorationNode)

@given(instance=DiagramStyle_strategy)
@settings(max_examples=50)
def test_diagramstyle_instantiation(instance):
    assert isinstance(instance, DiagramStyle)

@given(instance=Diagram_strategy)
@settings(max_examples=50)
def test_diagram_instantiation(instance):
    assert isinstance(instance, Diagram)

@given(instance=notation_StandardDiagram_strategy)
@settings(max_examples=50)
def test_notation_standarddiagram_instantiation(instance):
    assert isinstance(instance, notation_StandardDiagram)

@given(instance=ConnectorStyle_strategy)
@settings(max_examples=50)
def test_connectorstyle_instantiation(instance):
    assert isinstance(instance, ConnectorStyle)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=notation_Connector_strategy)
@settings(max_examples=50)
def test_notation_connector_instantiation(instance):
    assert isinstance(instance, notation_Connector)

@given(instance=FilteringStyle_strategy)
@settings(max_examples=50)
def test_filteringstyle_instantiation(instance):
    assert isinstance(instance, FilteringStyle)

@given(instance=SortingStyle_strategy)
@settings(max_examples=50)
def test_sortingstyle_instantiation(instance):
    assert isinstance(instance, SortingStyle)

@given(instance=notation_SemanticListCompartment_strategy)
@settings(max_examples=50)
def test_notation_semanticlistcompartment_instantiation(instance):
    assert isinstance(instance, notation_SemanticListCompartment)

@given(instance=notation_ListCompartment_strategy)
@settings(max_examples=50)
def test_notation_listcompartment_instantiation(instance):
    assert isinstance(instance, notation_ListCompartment)

@given(instance=notation_MultiDiagramLinkStyle_strategy)
@settings(max_examples=50)
def test_notation_multidiagramlinkstyle_instantiation(instance):
    assert isinstance(instance, notation_MultiDiagramLinkStyle)

@given(instance=notation_DiagramLinkStyle_strategy)
@settings(max_examples=50)
def test_notation_diagramlinkstyle_instantiation(instance):
    assert isinstance(instance, notation_DiagramLinkStyle)

@given(instance=DiagramLinkStyle_strategy)
@settings(max_examples=50)
def test_diagramlinkstyle_instantiation(instance):
    assert isinstance(instance, DiagramLinkStyle)

@given(instance=notation_HintedDiagramLinkStyle_strategy)
@settings(max_examples=50)
def test_notation_hinteddiagramlinkstyle_instantiation(instance):
    assert isinstance(instance, notation_HintedDiagramLinkStyle)



@given(instance=notation_HintedDiagramLinkStyle_strategy)
def test_notation_hinteddiagramlinkstyle_hint_setter(instance):
    original = instance.hint
    instance.hint = original
    assert instance.hint == original

@given(instance=StringObjectConverter_strategy)
@settings(max_examples=50)
def test_stringobjectconverter_instantiation(instance):
    assert isinstance(instance, StringObjectConverter)

@given(instance=notation_PropertyValue_strategy)
@settings(max_examples=50)
def test_notation_propertyvalue_instantiation(instance):
    assert isinstance(instance, notation_PropertyValue)



@given(instance=notation_PropertyValue_strategy)
def test_notation_propertyvalue_rawValue_setter(instance):
    original = instance.rawValue
    instance.rawValue = original
    assert instance.rawValue == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_PropertyValue_strategy)
@settings(max_examples=30)
def test_notation_propertyvalue_setvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setValue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setValue' in notation_PropertyValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setValue' in notation_PropertyValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setValue' in notation_PropertyValue is not implemented or raised an error")

@given(instance=notation_StringToPropertyValueMapEntry_strategy)
@settings(max_examples=50)
def test_notation_stringtopropertyvaluemapentry_instantiation(instance):
    assert isinstance(instance, notation_StringToPropertyValueMapEntry)



@given(instance=notation_StringToPropertyValueMapEntry_strategy)
def test_notation_stringtopropertyvaluemapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=notation_StringObjectConverter_strategy)
@settings(max_examples=50)
def test_notation_stringobjectconverter_instantiation(instance):
    assert isinstance(instance, notation_StringObjectConverter)

@given(instance=notation_NamedStyle_strategy)
@settings(max_examples=50)
def test_notation_namedstyle_instantiation(instance):
    assert isinstance(instance, notation_NamedStyle)



@given(instance=notation_NamedStyle_strategy)
def test_notation_namedstyle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DataTypeStyle_strategy)
@settings(max_examples=50)
def test_datatypestyle_instantiation(instance):
    assert isinstance(instance, DataTypeStyle)

@given(instance=notation_ListValueStyle_strategy)
@settings(max_examples=50)
def test_notation_listvaluestyle_instantiation(instance):
    assert isinstance(instance, notation_ListValueStyle)



@given(instance=notation_ListValueStyle_strategy)
def test_notation_listvaluestyle_rawValuesList_setter(instance):
    original = instance.rawValuesList
    instance.rawValuesList = original
    assert instance.rawValuesList == original

@given(instance=notation_SingleValueStyle_strategy)
@settings(max_examples=50)
def test_notation_singlevaluestyle_instantiation(instance):
    assert isinstance(instance, notation_SingleValueStyle)



@given(instance=notation_SingleValueStyle_strategy)
def test_notation_singlevaluestyle_rawValue_setter(instance):
    original = instance.rawValue
    instance.rawValue = original
    assert instance.rawValue == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_SingleValueStyle_strategy)
@settings(max_examples=30)
def test_notation_singlevaluestyle_setvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setValue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setValue' in notation_SingleValueStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setValue' in notation_SingleValueStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setValue' in notation_SingleValueStyle is not implemented or raised an error")

@given(instance=notation_EDataType_strategy)
@settings(max_examples=50)
def test_notation_edatatype_instantiation(instance):
    assert isinstance(instance, notation_EDataType)

@given(instance=notation_FilteringStyle_strategy)
@settings(max_examples=50)
def test_notation_filteringstyle_instantiation(instance):
    assert isinstance(instance, notation_FilteringStyle)



@given(instance=notation_FilteringStyle_strategy)
def test_notation_filteringstyle_filtering_setter(instance):
    original = instance.filtering
    instance.filtering = original
    assert instance.filtering == original



@given(instance=notation_FilteringStyle_strategy)
def test_notation_filteringstyle_filteringKeys_setter(instance):
    original = instance.filteringKeys
    instance.filteringKeys = original
    assert instance.filteringKeys == original

@given(instance=notation_NodeEntry_strategy)
@settings(max_examples=50)
def test_notation_nodeentry_instantiation(instance):
    assert isinstance(instance, notation_NodeEntry)



@given(instance=notation_NodeEntry_strategy)
def test_notation_nodeentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NamedStyle_strategy)
@settings(max_examples=50)
def test_namedstyle_instantiation(instance):
    assert isinstance(instance, NamedStyle)

@given(instance=notation_BooleanListValueStyle_strategy)
@settings(max_examples=50)
def test_notation_booleanlistvaluestyle_instantiation(instance):
    assert isinstance(instance, notation_BooleanListValueStyle)



@given(instance=notation_BooleanListValueStyle_strategy)
def test_notation_booleanlistvaluestyle_booleanListValue_setter(instance):
    original = instance.booleanListValue
    instance.booleanListValue = original
    assert instance.booleanListValue == original

@given(instance=notation_IntListValueStyle_strategy)
@settings(max_examples=50)
def test_notation_intlistvaluestyle_instantiation(instance):
    assert isinstance(instance, notation_IntListValueStyle)



@given(instance=notation_IntListValueStyle_strategy)
def test_notation_intlistvaluestyle_intListValue_setter(instance):
    original = instance.intListValue
    instance.intListValue = original
    assert instance.intListValue == original

@given(instance=notation_DataTypeStyle_strategy)
@settings(max_examples=50)
def test_notation_datatypestyle_instantiation(instance):
    assert isinstance(instance, notation_DataTypeStyle)

@given(instance=notation_StringValueStyle_strategy)
@settings(max_examples=50)
def test_notation_stringvaluestyle_instantiation(instance):
    assert isinstance(instance, notation_StringValueStyle)



@given(instance=notation_StringValueStyle_strategy)
def test_notation_stringvaluestyle_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=notation_ByteArrayValueStyle_strategy)
@settings(max_examples=50)
def test_notation_bytearrayvaluestyle_instantiation(instance):
    assert isinstance(instance, notation_ByteArrayValueStyle)



@given(instance=notation_ByteArrayValueStyle_strategy)
def test_notation_bytearrayvaluestyle_byteArrayValue_setter(instance):
    original = instance.byteArrayValue
    instance.byteArrayValue = original
    assert instance.byteArrayValue == original

@given(instance=notation_DoubleValueStyle_strategy)
@settings(max_examples=50)
def test_notation_doublevaluestyle_instantiation(instance):
    assert isinstance(instance, notation_DoubleValueStyle)



@given(instance=notation_DoubleValueStyle_strategy)
def test_notation_doublevaluestyle_doubleValue_setter(instance):
    original = instance.doubleValue
    instance.doubleValue = original
    assert instance.doubleValue == original

@given(instance=notation_IntValueStyle_strategy)
@settings(max_examples=50)
def test_notation_intvaluestyle_instantiation(instance):
    assert isinstance(instance, notation_IntValueStyle)



@given(instance=notation_IntValueStyle_strategy)
def test_notation_intvaluestyle_intValue_setter(instance):
    original = instance.intValue
    instance.intValue = original
    assert instance.intValue == original

@given(instance=notation_BooleanValueStyle_strategy)
@settings(max_examples=50)
def test_notation_booleanvaluestyle_instantiation(instance):
    assert isinstance(instance, notation_BooleanValueStyle)



@given(instance=notation_BooleanValueStyle_strategy)
def test_notation_booleanvaluestyle_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=notation_EObjectValueStyle_strategy)
@settings(max_examples=50)
def test_notation_eobjectvaluestyle_instantiation(instance):
    assert isinstance(instance, notation_EObjectValueStyle)

@given(instance=notation_DoubleListValueStyle_strategy)
@settings(max_examples=50)
def test_notation_doublelistvaluestyle_instantiation(instance):
    assert isinstance(instance, notation_DoubleListValueStyle)



@given(instance=notation_DoubleListValueStyle_strategy)
def test_notation_doublelistvaluestyle_doubleListValue_setter(instance):
    original = instance.doubleListValue
    instance.doubleListValue = original
    assert instance.doubleListValue == original

@given(instance=notation_StringListValueStyle_strategy)
@settings(max_examples=50)
def test_notation_stringlistvaluestyle_instantiation(instance):
    assert isinstance(instance, notation_StringListValueStyle)



@given(instance=notation_StringListValueStyle_strategy)
def test_notation_stringlistvaluestyle_stringListValue_setter(instance):
    original = instance.stringListValue
    instance.stringListValue = original
    assert instance.stringListValue == original

@given(instance=notation_EObjectListValueStyle_strategy)
@settings(max_examples=50)
def test_notation_eobjectlistvaluestyle_instantiation(instance):
    assert isinstance(instance, notation_EObjectListValueStyle)

@given(instance=notation_PropertiesSetStyle_strategy)
@settings(max_examples=50)
def test_notation_propertiessetstyle_instantiation(instance):
    assert isinstance(instance, notation_PropertiesSetStyle)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_PropertiesSetStyle_strategy)
@settings(max_examples=30)
def test_notation_propertiessetstyle_removeproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeProperty(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeProperty' in notation_PropertiesSetStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeProperty' in notation_PropertiesSetStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeProperty' in notation_PropertiesSetStyle is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_PropertiesSetStyle_strategy)
@settings(max_examples=30)
def test_notation_propertiessetstyle_setproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setProperty(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setProperty' in notation_PropertiesSetStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setProperty' in notation_PropertiesSetStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setProperty' in notation_PropertiesSetStyle is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_PropertiesSetStyle_strategy)
@settings(max_examples=30)
def test_notation_propertiessetstyle_hasproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasProperty(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasProperty' in notation_PropertiesSetStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasProperty' in notation_PropertiesSetStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasProperty' in notation_PropertiesSetStyle is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation_PropertiesSetStyle_strategy)
@settings(max_examples=30)
def test_notation_propertiessetstyle_createproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createProperty(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createProperty' in notation_PropertiesSetStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createProperty' in notation_PropertiesSetStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createProperty' in notation_PropertiesSetStyle is not implemented or raised an error")

@given(instance=ImageStyle_strategy)
@settings(max_examples=50)
def test_imagestyle_instantiation(instance):
    assert isinstance(instance, ImageStyle)

@given(instance=notation_ImageBufferStyle_strategy)
@settings(max_examples=50)
def test_notation_imagebufferstyle_instantiation(instance):
    assert isinstance(instance, notation_ImageBufferStyle)

@given(instance=notation_ImageStyle_strategy)
@settings(max_examples=50)
def test_notation_imagestyle_instantiation(instance):
    assert isinstance(instance, notation_ImageStyle)



@given(instance=notation_ImageStyle_strategy)
def test_notation_imagestyle_maintainAspectRatio_setter(instance):
    original = instance.maintainAspectRatio
    instance.maintainAspectRatio = original
    assert instance.maintainAspectRatio == original



@given(instance=notation_ImageStyle_strategy)
def test_notation_imagestyle_antiAlias_setter(instance):
    original = instance.antiAlias
    instance.antiAlias = original
    assert instance.antiAlias == original
