import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mMDSL::Polygon,
    mMDSL::Polyline,
    mMDSL::Line,
    mMDSL::Ellipse,
    mMDSL::Circle,
    mMDSL::Rectangle,
    mMDSL::SVGCommand,
    mMDSL::Mode,
    mMDSL::EnumType,
    mMDSL::RefName,
    mMDSL::Type,
    mMDSL::Reference,
    mMDSL::ClassAttribute,
    mMDSL::ModelType,
    mMDSL::Attribute,
    mMDSL::Relation,
    mMDSL::Class,
    mMDSL::Event,
    mMDSL::Algorithm,
    mMDSL::Metamodel,
    mMDSL::SymbolRelation,
    mMDSL::SymbolClass,
    mMDSL::SymbolStyle,
    mMDSL::Enumeration,
    mMDSL::InsertEmbedCode,
    mMDSL::Method,
    mMDSL::EmbedCode,
    mMDSL::IncludeLibrary,
    mMDSL::EmbedCodeType,
    mMDSL::EmbedPlatformType,
    mMDSL::IncludeLibraryType,
    mMDSL::MethodName,
    mMDSL::Root,
    Expression,
    mMDSL::MultiplicationExpression,
    mMDSL::EqualExpression,
    mMDSL::AdditionExpression,
    mMDSL::AndExpression,
    mMDSL::CompareExpression,
    mMDSL::OrExpression,
    mMDSL::AttributeSet,
    mMDSL::AttributeGet,
    mMDSL::RelationInstanceGetAll,
    mMDSL::RelationInstanceSet,
    mMDSL::RelationInstanceGet,
    mMDSL::RelationInstanceDelete,
    mMDSL::RelationInstanceCreate,
    mMDSL::ClassInstanceGetAll,
    mMDSL::ClassInstanceSet,
    mMDSL::ClassInstanceGet,
    mMDSL::ClassInstanceDelete,
    mMDSL::ClassInstanceCreate,
    mMDSL::RelationInstance,
    mMDSL::ClassInstance,
    mMDSL::ModelIsLoaded,
    mMDSL::ModelLoad,
    mMDSL::ModelSave,
    mMDSL::ModelDiscard,
    mMDSL::ModelDelete,
    mMDSL::ModelCreate,
    mMDSL::RemoveContextItem,
    mMDSL::InsertContextItem,
    mMDSL::RemoveMenuItem,
    mMDSL::InsertMenuItem,
    mMDSL::ContextItem,
    mMDSL::MenuItem,
    mMDSL::ItemOperation,
    mMDSL::ViewBox,
    mMDSL::WarningBox,
    mMDSL::ErrorBox,
    mMDSL::InfoBox,
    mMDSL::EditBox,
    mMDSL::DirList,
    mMDSL::DirDelete,
    mMDSL::DirCreate,
    mMDSL::DirGetWorking,
    mMDSL::DirSetWorking,
    mMDSL::FileWrite,
    mMDSL::FileRead,
    mMDSL::FileCreate,
    mMDSL::FileDelete,
    mMDSL::FileCopy,
    mMDSL::AttributeOperation,
    mMDSL::InstanceOperation,
    mMDSL::ModelOperation,
    mMDSL::SimpleUI,
    mMDSL::DirOperation,
    mMDSL::FileOperation,
    mMDSL::EObject,
    mMDSL::Expression,
    mMDSL::OperatorOr,
    mMDSL::OperatorAnd,
    mMDSL::OperatorEqual,
    mMDSL::OperatorCompare,
    mMDSL::OperatorAdd,
    mMDSL::OperatorMultiply,
    mMDSL::OperatorUnary,
    mMDSL::OperatorMultyAssign,
    mMDSL::VarStatement,
    mMDSL::OperatorAssign,
    mMDSL::BreakContinue,
    mMDSL::ForLoop,
    mMDSL::WhileLoop,
    mMDSL::Expr,
    mMDSL::AlgorithmOperation,
    mMDSL::Variable,
    mMDSL::LoopStatement,
    mMDSL::SelectionStatement,
    mMDSL::Statement,
    mMDSL::StrokeColor,
    mMDSL::PathParametersA,
    mMDSL::PathParametersQ,
    mMDSL::PathParametersS,
    mMDSL::PathParametersC,
    mMDSL::PathParametersHV,
    mMDSL::PathParametersMLT,
    mMDSL::EllipticalArc,
    mMDSL::SmoothQuadraticBezierCurveTo,
    mMDSL::QuadraticBezierCurve,
    mMDSL::SmoothCurveTo,
    mMDSL::CurveTo,
    mMDSL::VerticalLineTo,
    mMDSL::HorizontalLineTo,
    mMDSL::LineTo,
    mMDSL::MoveTo,
    mMDSL::FillColor,
    mMDSL::FontFamily,
    mMDSL::PathData,
    mMDSL::Points,
    mMDSL::Text,
    mMDSL::Path,
    SimpleType,
    Font,
    EventName,
    AccessType,
    AttrGetParams,
    Color,
    AttrSetParams,
    ButtonType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mmdsl::polygon_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Polygon)


def test_mmdsl::polygon_constructor_exists():
    assert callable(mMDSL::Polygon.__init__)


def test_mmdsl::polygon_constructor_args():
    sig = inspect.signature(mMDSL::Polygon.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::polyline_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Polyline)


def test_mmdsl::polyline_constructor_exists():
    assert callable(mMDSL::Polyline.__init__)


def test_mmdsl::polyline_constructor_args():
    sig = inspect.signature(mMDSL::Polyline.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::line_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Line)


def test_mmdsl::line_constructor_exists():
    assert callable(mMDSL::Line.__init__)


def test_mmdsl::line_constructor_args():
    sig = inspect.signature(mMDSL::Line.__init__)
    params = list(sig.parameters.keys())
    assert "y2" in params, "Missing parameter 'y2'"
    assert "y1" in params, "Missing parameter 'y1'"
    assert "x2" in params, "Missing parameter 'x2'"
    assert "x1" in params, "Missing parameter 'x1'"

def test_mmdsl::line_has_y2():
    assert hasattr(mMDSL::Line, "y2")
    descriptor = None
    for klass in mMDSL::Line.__mro__:
        if "y2" in klass.__dict__:
            descriptor = klass.__dict__["y2"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::line_has_y1():
    assert hasattr(mMDSL::Line, "y1")
    descriptor = None
    for klass in mMDSL::Line.__mro__:
        if "y1" in klass.__dict__:
            descriptor = klass.__dict__["y1"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::line_has_x2():
    assert hasattr(mMDSL::Line, "x2")
    descriptor = None
    for klass in mMDSL::Line.__mro__:
        if "x2" in klass.__dict__:
            descriptor = klass.__dict__["x2"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::line_has_x1():
    assert hasattr(mMDSL::Line, "x1")
    descriptor = None
    for klass in mMDSL::Line.__mro__:
        if "x1" in klass.__dict__:
            descriptor = klass.__dict__["x1"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::ellipse_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Ellipse)


def test_mmdsl::ellipse_constructor_exists():
    assert callable(mMDSL::Ellipse.__init__)


def test_mmdsl::ellipse_constructor_args():
    sig = inspect.signature(mMDSL::Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "ry" in params, "Missing parameter 'ry'"
    assert "cy" in params, "Missing parameter 'cy'"
    assert "rx" in params, "Missing parameter 'rx'"
    assert "cx" in params, "Missing parameter 'cx'"

def test_mmdsl::ellipse_has_ry():
    assert hasattr(mMDSL::Ellipse, "ry")
    descriptor = None
    for klass in mMDSL::Ellipse.__mro__:
        if "ry" in klass.__dict__:
            descriptor = klass.__dict__["ry"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::ellipse_has_cy():
    assert hasattr(mMDSL::Ellipse, "cy")
    descriptor = None
    for klass in mMDSL::Ellipse.__mro__:
        if "cy" in klass.__dict__:
            descriptor = klass.__dict__["cy"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::ellipse_has_rx():
    assert hasattr(mMDSL::Ellipse, "rx")
    descriptor = None
    for klass in mMDSL::Ellipse.__mro__:
        if "rx" in klass.__dict__:
            descriptor = klass.__dict__["rx"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::ellipse_has_cx():
    assert hasattr(mMDSL::Ellipse, "cx")
    descriptor = None
    for klass in mMDSL::Ellipse.__mro__:
        if "cx" in klass.__dict__:
            descriptor = klass.__dict__["cx"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::circle_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Circle)


def test_mmdsl::circle_constructor_exists():
    assert callable(mMDSL::Circle.__init__)


def test_mmdsl::circle_constructor_args():
    sig = inspect.signature(mMDSL::Circle.__init__)
    params = list(sig.parameters.keys())
    assert "cx" in params, "Missing parameter 'cx'"
    assert "r" in params, "Missing parameter 'r'"
    assert "cy" in params, "Missing parameter 'cy'"

def test_mmdsl::circle_has_cx():
    assert hasattr(mMDSL::Circle, "cx")
    descriptor = None
    for klass in mMDSL::Circle.__mro__:
        if "cx" in klass.__dict__:
            descriptor = klass.__dict__["cx"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::circle_has_r():
    assert hasattr(mMDSL::Circle, "r")
    descriptor = None
    for klass in mMDSL::Circle.__mro__:
        if "r" in klass.__dict__:
            descriptor = klass.__dict__["r"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::circle_has_cy():
    assert hasattr(mMDSL::Circle, "cy")
    descriptor = None
    for klass in mMDSL::Circle.__mro__:
        if "cy" in klass.__dict__:
            descriptor = klass.__dict__["cy"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::rectangle_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Rectangle)


def test_mmdsl::rectangle_constructor_exists():
    assert callable(mMDSL::Rectangle.__init__)


def test_mmdsl::rectangle_constructor_args():
    sig = inspect.signature(mMDSL::Rectangle.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_mmdsl::rectangle_has_x():
    assert hasattr(mMDSL::Rectangle, "x")
    descriptor = None
    for klass in mMDSL::Rectangle.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::rectangle_has_y():
    assert hasattr(mMDSL::Rectangle, "y")
    descriptor = None
    for klass in mMDSL::Rectangle.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::rectangle_has_height():
    assert hasattr(mMDSL::Rectangle, "height")
    descriptor = None
    for klass in mMDSL::Rectangle.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::rectangle_has_width():
    assert hasattr(mMDSL::Rectangle, "width")
    descriptor = None
    for klass in mMDSL::Rectangle.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::svgcommand_is_not_abstract():
    assert not inspect.isabstract(mMDSL::SVGCommand)


def test_mmdsl::svgcommand_constructor_exists():
    assert callable(mMDSL::SVGCommand.__init__)


def test_mmdsl::svgcommand_constructor_args():
    sig = inspect.signature(mMDSL::SVGCommand.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::mode_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Mode)


def test_mmdsl::mode_constructor_exists():
    assert callable(mMDSL::Mode.__init__)


def test_mmdsl::mode_constructor_args():
    sig = inspect.signature(mMDSL::Mode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::mode_has_name():
    assert hasattr(mMDSL::Mode, "name")
    descriptor = None
    for klass in mMDSL::Mode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::enumtype_is_not_abstract():
    assert not inspect.isabstract(mMDSL::EnumType)


def test_mmdsl::enumtype_constructor_exists():
    assert callable(mMDSL::EnumType.__init__)


def test_mmdsl::enumtype_constructor_args():
    sig = inspect.signature(mMDSL::EnumType.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::refname_is_not_abstract():
    assert not inspect.isabstract(mMDSL::RefName)


def test_mmdsl::refname_constructor_exists():
    assert callable(mMDSL::RefName.__init__)


def test_mmdsl::refname_constructor_args():
    sig = inspect.signature(mMDSL::RefName.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::type_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Type)


def test_mmdsl::type_constructor_exists():
    assert callable(mMDSL::Type.__init__)


def test_mmdsl::type_constructor_args():
    sig = inspect.signature(mMDSL::Type.__init__)
    params = list(sig.parameters.keys())
    assert "simpletype" in params, "Missing parameter 'simpletype'"

def test_mmdsl::type_has_simpletype():
    assert hasattr(mMDSL::Type, "simpletype")
    descriptor = None
    for klass in mMDSL::Type.__mro__:
        if "simpletype" in klass.__dict__:
            descriptor = klass.__dict__["simpletype"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::reference_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Reference)


def test_mmdsl::reference_constructor_exists():
    assert callable(mMDSL::Reference.__init__)


def test_mmdsl::reference_constructor_args():
    sig = inspect.signature(mMDSL::Reference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::reference_has_name():
    assert hasattr(mMDSL::Reference, "name")
    descriptor = None
    for klass in mMDSL::Reference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::classattribute_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ClassAttribute)


def test_mmdsl::classattribute_constructor_exists():
    assert callable(mMDSL::ClassAttribute.__init__)


def test_mmdsl::classattribute_constructor_args():
    sig = inspect.signature(mMDSL::ClassAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::classattribute_has_name():
    assert hasattr(mMDSL::ClassAttribute, "name")
    descriptor = None
    for klass in mMDSL::ClassAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::modeltype_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ModelType)


def test_mmdsl::modeltype_constructor_exists():
    assert callable(mMDSL::ModelType.__init__)


def test_mmdsl::modeltype_constructor_args():
    sig = inspect.signature(mMDSL::ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::modeltype_has_name():
    assert hasattr(mMDSL::ModelType, "name")
    descriptor = None
    for klass in mMDSL::ModelType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::attribute_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Attribute)


def test_mmdsl::attribute_constructor_exists():
    assert callable(mMDSL::Attribute.__init__)


def test_mmdsl::attribute_constructor_args():
    sig = inspect.signature(mMDSL::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "access" in params, "Missing parameter 'access'"
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::attribute_has_access():
    assert hasattr(mMDSL::Attribute, "access")
    descriptor = None
    for klass in mMDSL::Attribute.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::attribute_has_name():
    assert hasattr(mMDSL::Attribute, "name")
    descriptor = None
    for klass in mMDSL::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::relation_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Relation)


def test_mmdsl::relation_constructor_exists():
    assert callable(mMDSL::Relation.__init__)


def test_mmdsl::relation_constructor_args():
    sig = inspect.signature(mMDSL::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::relation_has_name():
    assert hasattr(mMDSL::Relation, "name")
    descriptor = None
    for klass in mMDSL::Relation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::class_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Class)


def test_mmdsl::class_constructor_exists():
    assert callable(mMDSL::Class.__init__)


def test_mmdsl::class_constructor_args():
    sig = inspect.signature(mMDSL::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::class_has_name():
    assert hasattr(mMDSL::Class, "name")
    descriptor = None
    for klass in mMDSL::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::event_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Event)


def test_mmdsl::event_constructor_exists():
    assert callable(mMDSL::Event.__init__)


def test_mmdsl::event_constructor_args():
    sig = inspect.signature(mMDSL::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::event_has_name():
    assert hasattr(mMDSL::Event, "name")
    descriptor = None
    for klass in mMDSL::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::algorithm_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Algorithm)


def test_mmdsl::algorithm_constructor_exists():
    assert callable(mMDSL::Algorithm.__init__)


def test_mmdsl::algorithm_constructor_args():
    sig = inspect.signature(mMDSL::Algorithm.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::algorithm_has_name():
    assert hasattr(mMDSL::Algorithm, "name")
    descriptor = None
    for klass in mMDSL::Algorithm.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::metamodel_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Metamodel)


def test_mmdsl::metamodel_constructor_exists():
    assert callable(mMDSL::Metamodel.__init__)


def test_mmdsl::metamodel_constructor_args():
    sig = inspect.signature(mMDSL::Metamodel.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::symbolrelation_is_not_abstract():
    assert not inspect.isabstract(mMDSL::SymbolRelation)


def test_mmdsl::symbolrelation_constructor_exists():
    assert callable(mMDSL::SymbolRelation.__init__)


def test_mmdsl::symbolrelation_constructor_args():
    sig = inspect.signature(mMDSL::SymbolRelation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::symbolrelation_has_name():
    assert hasattr(mMDSL::SymbolRelation, "name")
    descriptor = None
    for klass in mMDSL::SymbolRelation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::symbolclass_is_not_abstract():
    assert not inspect.isabstract(mMDSL::SymbolClass)


def test_mmdsl::symbolclass_constructor_exists():
    assert callable(mMDSL::SymbolClass.__init__)


def test_mmdsl::symbolclass_constructor_args():
    sig = inspect.signature(mMDSL::SymbolClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::symbolclass_has_name():
    assert hasattr(mMDSL::SymbolClass, "name")
    descriptor = None
    for klass in mMDSL::SymbolClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::symbolstyle_is_not_abstract():
    assert not inspect.isabstract(mMDSL::SymbolStyle)


def test_mmdsl::symbolstyle_constructor_exists():
    assert callable(mMDSL::SymbolStyle.__init__)


def test_mmdsl::symbolstyle_constructor_args():
    sig = inspect.signature(mMDSL::SymbolStyle.__init__)
    params = list(sig.parameters.keys())
    assert "fontsize" in params, "Missing parameter 'fontsize'"
    assert "name" in params, "Missing parameter 'name'"
    assert "strokewidth" in params, "Missing parameter 'strokewidth'"

def test_mmdsl::symbolstyle_has_fontsize():
    assert hasattr(mMDSL::SymbolStyle, "fontsize")
    descriptor = None
    for klass in mMDSL::SymbolStyle.__mro__:
        if "fontsize" in klass.__dict__:
            descriptor = klass.__dict__["fontsize"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::symbolstyle_has_name():
    assert hasattr(mMDSL::SymbolStyle, "name")
    descriptor = None
    for klass in mMDSL::SymbolStyle.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::symbolstyle_has_strokewidth():
    assert hasattr(mMDSL::SymbolStyle, "strokewidth")
    descriptor = None
    for klass in mMDSL::SymbolStyle.__mro__:
        if "strokewidth" in klass.__dict__:
            descriptor = klass.__dict__["strokewidth"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::enumeration_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Enumeration)


def test_mmdsl::enumeration_constructor_exists():
    assert callable(mMDSL::Enumeration.__init__)


def test_mmdsl::enumeration_constructor_args():
    sig = inspect.signature(mMDSL::Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "enumvalues" in params, "Missing parameter 'enumvalues'"

def test_mmdsl::enumeration_has_name():
    assert hasattr(mMDSL::Enumeration, "name")
    descriptor = None
    for klass in mMDSL::Enumeration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::enumeration_has_enumvalues():
    assert hasattr(mMDSL::Enumeration, "enumvalues")
    descriptor = None
    for klass in mMDSL::Enumeration.__mro__:
        if "enumvalues" in klass.__dict__:
            descriptor = klass.__dict__["enumvalues"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::insertembedcode_is_not_abstract():
    assert not inspect.isabstract(mMDSL::InsertEmbedCode)


def test_mmdsl::insertembedcode_constructor_exists():
    assert callable(mMDSL::InsertEmbedCode.__init__)


def test_mmdsl::insertembedcode_constructor_args():
    sig = inspect.signature(mMDSL::InsertEmbedCode.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::method_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Method)


def test_mmdsl::method_constructor_exists():
    assert callable(mMDSL::Method.__init__)


def test_mmdsl::method_constructor_args():
    sig = inspect.signature(mMDSL::Method.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::embedcode_is_not_abstract():
    assert not inspect.isabstract(mMDSL::EmbedCode)


def test_mmdsl::embedcode_constructor_exists():
    assert callable(mMDSL::EmbedCode.__init__)


def test_mmdsl::embedcode_constructor_args():
    sig = inspect.signature(mMDSL::EmbedCode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "embeddedcode" in params, "Missing parameter 'embeddedcode'"

def test_mmdsl::embedcode_has_name():
    assert hasattr(mMDSL::EmbedCode, "name")
    descriptor = None
    for klass in mMDSL::EmbedCode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::embedcode_has_embeddedcode():
    assert hasattr(mMDSL::EmbedCode, "embeddedcode")
    descriptor = None
    for klass in mMDSL::EmbedCode.__mro__:
        if "embeddedcode" in klass.__dict__:
            descriptor = klass.__dict__["embeddedcode"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::includelibrary_is_not_abstract():
    assert not inspect.isabstract(mMDSL::IncludeLibrary)


def test_mmdsl::includelibrary_constructor_exists():
    assert callable(mMDSL::IncludeLibrary.__init__)


def test_mmdsl::includelibrary_constructor_args():
    sig = inspect.signature(mMDSL::IncludeLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::includelibrary_has_name():
    assert hasattr(mMDSL::IncludeLibrary, "name")
    descriptor = None
    for klass in mMDSL::IncludeLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::embedcodetype_is_not_abstract():
    assert not inspect.isabstract(mMDSL::EmbedCodeType)


def test_mmdsl::embedcodetype_constructor_exists():
    assert callable(mMDSL::EmbedCodeType.__init__)


def test_mmdsl::embedcodetype_constructor_args():
    sig = inspect.signature(mMDSL::EmbedCodeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::embedcodetype_has_name():
    assert hasattr(mMDSL::EmbedCodeType, "name")
    descriptor = None
    for klass in mMDSL::EmbedCodeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::embedplatformtype_is_not_abstract():
    assert not inspect.isabstract(mMDSL::EmbedPlatformType)


def test_mmdsl::embedplatformtype_constructor_exists():
    assert callable(mMDSL::EmbedPlatformType.__init__)


def test_mmdsl::embedplatformtype_constructor_args():
    sig = inspect.signature(mMDSL::EmbedPlatformType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::embedplatformtype_has_name():
    assert hasattr(mMDSL::EmbedPlatformType, "name")
    descriptor = None
    for klass in mMDSL::EmbedPlatformType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::includelibrarytype_is_not_abstract():
    assert not inspect.isabstract(mMDSL::IncludeLibraryType)


def test_mmdsl::includelibrarytype_constructor_exists():
    assert callable(mMDSL::IncludeLibraryType.__init__)


def test_mmdsl::includelibrarytype_constructor_args():
    sig = inspect.signature(mMDSL::IncludeLibraryType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::includelibrarytype_has_name():
    assert hasattr(mMDSL::IncludeLibraryType, "name")
    descriptor = None
    for klass in mMDSL::IncludeLibraryType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::methodname_is_not_abstract():
    assert not inspect.isabstract(mMDSL::MethodName)


def test_mmdsl::methodname_constructor_exists():
    assert callable(mMDSL::MethodName.__init__)


def test_mmdsl::methodname_constructor_args():
    sig = inspect.signature(mMDSL::MethodName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::methodname_has_name():
    assert hasattr(mMDSL::MethodName, "name")
    descriptor = None
    for klass in mMDSL::MethodName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::root_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Root)


def test_mmdsl::root_constructor_exists():
    assert callable(mMDSL::Root.__init__)


def test_mmdsl::root_constructor_args():
    sig = inspect.signature(mMDSL::Root.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::multiplicationexpression_is_not_abstract():
    assert not inspect.isabstract(mMDSL::MultiplicationExpression)


def test_mmdsl::multiplicationexpression_constructor_exists():
    assert callable(mMDSL::MultiplicationExpression.__init__)


def test_mmdsl::multiplicationexpression_constructor_args():
    sig = inspect.signature(mMDSL::MultiplicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::equalexpression_is_not_abstract():
    assert not inspect.isabstract(mMDSL::EqualExpression)


def test_mmdsl::equalexpression_constructor_exists():
    assert callable(mMDSL::EqualExpression.__init__)


def test_mmdsl::equalexpression_constructor_args():
    sig = inspect.signature(mMDSL::EqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::additionexpression_is_not_abstract():
    assert not inspect.isabstract(mMDSL::AdditionExpression)


def test_mmdsl::additionexpression_constructor_exists():
    assert callable(mMDSL::AdditionExpression.__init__)


def test_mmdsl::additionexpression_constructor_args():
    sig = inspect.signature(mMDSL::AdditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::andexpression_is_not_abstract():
    assert not inspect.isabstract(mMDSL::AndExpression)


def test_mmdsl::andexpression_constructor_exists():
    assert callable(mMDSL::AndExpression.__init__)


def test_mmdsl::andexpression_constructor_args():
    sig = inspect.signature(mMDSL::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::compareexpression_is_not_abstract():
    assert not inspect.isabstract(mMDSL::CompareExpression)


def test_mmdsl::compareexpression_constructor_exists():
    assert callable(mMDSL::CompareExpression.__init__)


def test_mmdsl::compareexpression_constructor_args():
    sig = inspect.signature(mMDSL::CompareExpression.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::orexpression_is_not_abstract():
    assert not inspect.isabstract(mMDSL::OrExpression)


def test_mmdsl::orexpression_constructor_exists():
    assert callable(mMDSL::OrExpression.__init__)


def test_mmdsl::orexpression_constructor_args():
    sig = inspect.signature(mMDSL::OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::attributeset_is_not_abstract():
    assert not inspect.isabstract(mMDSL::AttributeSet)


def test_mmdsl::attributeset_constructor_exists():
    assert callable(mMDSL::AttributeSet.__init__)


def test_mmdsl::attributeset_constructor_args():
    sig = inspect.signature(mMDSL::AttributeSet.__init__)
    params = list(sig.parameters.keys())
    assert "attrsetparams" in params, "Missing parameter 'attrsetparams'"
    assert "valueRealNumber" in params, "Missing parameter 'valueRealNumber'"
    assert "valueString" in params, "Missing parameter 'valueString'"

def test_mmdsl::attributeset_has_attrsetparams():
    assert hasattr(mMDSL::AttributeSet, "attrsetparams")
    descriptor = None
    for klass in mMDSL::AttributeSet.__mro__:
        if "attrsetparams" in klass.__dict__:
            descriptor = klass.__dict__["attrsetparams"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::attributeset_has_valueRealNumber():
    assert hasattr(mMDSL::AttributeSet, "valueRealNumber")
    descriptor = None
    for klass in mMDSL::AttributeSet.__mro__:
        if "valueRealNumber" in klass.__dict__:
            descriptor = klass.__dict__["valueRealNumber"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::attributeset_has_valueString():
    assert hasattr(mMDSL::AttributeSet, "valueString")
    descriptor = None
    for klass in mMDSL::AttributeSet.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::attributeget_is_not_abstract():
    assert not inspect.isabstract(mMDSL::AttributeGet)


def test_mmdsl::attributeget_constructor_exists():
    assert callable(mMDSL::AttributeGet.__init__)


def test_mmdsl::attributeget_constructor_args():
    sig = inspect.signature(mMDSL::AttributeGet.__init__)
    params = list(sig.parameters.keys())
    assert "attrgetparams" in params, "Missing parameter 'attrgetparams'"

def test_mmdsl::attributeget_has_attrgetparams():
    assert hasattr(mMDSL::AttributeGet, "attrgetparams")
    descriptor = None
    for klass in mMDSL::AttributeGet.__mro__:
        if "attrgetparams" in klass.__dict__:
            descriptor = klass.__dict__["attrgetparams"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::relationinstancegetall_is_not_abstract():
    assert not inspect.isabstract(mMDSL::RelationInstanceGetAll)


def test_mmdsl::relationinstancegetall_constructor_exists():
    assert callable(mMDSL::RelationInstanceGetAll.__init__)


def test_mmdsl::relationinstancegetall_constructor_args():
    sig = inspect.signature(mMDSL::RelationInstanceGetAll.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::relationinstanceset_is_not_abstract():
    assert not inspect.isabstract(mMDSL::RelationInstanceSet)


def test_mmdsl::relationinstanceset_constructor_exists():
    assert callable(mMDSL::RelationInstanceSet.__init__)


def test_mmdsl::relationinstanceset_constructor_args():
    sig = inspect.signature(mMDSL::RelationInstanceSet.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::relationinstanceget_is_not_abstract():
    assert not inspect.isabstract(mMDSL::RelationInstanceGet)


def test_mmdsl::relationinstanceget_constructor_exists():
    assert callable(mMDSL::RelationInstanceGet.__init__)


def test_mmdsl::relationinstanceget_constructor_args():
    sig = inspect.signature(mMDSL::RelationInstanceGet.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::relationinstancedelete_is_not_abstract():
    assert not inspect.isabstract(mMDSL::RelationInstanceDelete)


def test_mmdsl::relationinstancedelete_constructor_exists():
    assert callable(mMDSL::RelationInstanceDelete.__init__)


def test_mmdsl::relationinstancedelete_constructor_args():
    sig = inspect.signature(mMDSL::RelationInstanceDelete.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::relationinstancecreate_is_not_abstract():
    assert not inspect.isabstract(mMDSL::RelationInstanceCreate)


def test_mmdsl::relationinstancecreate_constructor_exists():
    assert callable(mMDSL::RelationInstanceCreate.__init__)


def test_mmdsl::relationinstancecreate_constructor_args():
    sig = inspect.signature(mMDSL::RelationInstanceCreate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::relationinstancecreate_has_name():
    assert hasattr(mMDSL::RelationInstanceCreate, "name")
    descriptor = None
    for klass in mMDSL::RelationInstanceCreate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::classinstancegetall_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ClassInstanceGetAll)


def test_mmdsl::classinstancegetall_constructor_exists():
    assert callable(mMDSL::ClassInstanceGetAll.__init__)


def test_mmdsl::classinstancegetall_constructor_args():
    sig = inspect.signature(mMDSL::ClassInstanceGetAll.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::classinstanceset_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ClassInstanceSet)


def test_mmdsl::classinstanceset_constructor_exists():
    assert callable(mMDSL::ClassInstanceSet.__init__)


def test_mmdsl::classinstanceset_constructor_args():
    sig = inspect.signature(mMDSL::ClassInstanceSet.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::classinstanceget_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ClassInstanceGet)


def test_mmdsl::classinstanceget_constructor_exists():
    assert callable(mMDSL::ClassInstanceGet.__init__)


def test_mmdsl::classinstanceget_constructor_args():
    sig = inspect.signature(mMDSL::ClassInstanceGet.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::classinstancedelete_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ClassInstanceDelete)


def test_mmdsl::classinstancedelete_constructor_exists():
    assert callable(mMDSL::ClassInstanceDelete.__init__)


def test_mmdsl::classinstancedelete_constructor_args():
    sig = inspect.signature(mMDSL::ClassInstanceDelete.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::classinstancecreate_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ClassInstanceCreate)


def test_mmdsl::classinstancecreate_constructor_exists():
    assert callable(mMDSL::ClassInstanceCreate.__init__)


def test_mmdsl::classinstancecreate_constructor_args():
    sig = inspect.signature(mMDSL::ClassInstanceCreate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::classinstancecreate_has_name():
    assert hasattr(mMDSL::ClassInstanceCreate, "name")
    descriptor = None
    for klass in mMDSL::ClassInstanceCreate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::relationinstance_is_not_abstract():
    assert not inspect.isabstract(mMDSL::RelationInstance)


def test_mmdsl::relationinstance_constructor_exists():
    assert callable(mMDSL::RelationInstance.__init__)


def test_mmdsl::relationinstance_constructor_args():
    sig = inspect.signature(mMDSL::RelationInstance.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::classinstance_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ClassInstance)


def test_mmdsl::classinstance_constructor_exists():
    assert callable(mMDSL::ClassInstance.__init__)


def test_mmdsl::classinstance_constructor_args():
    sig = inspect.signature(mMDSL::ClassInstance.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::modelisloaded_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ModelIsLoaded)


def test_mmdsl::modelisloaded_constructor_exists():
    assert callable(mMDSL::ModelIsLoaded.__init__)


def test_mmdsl::modelisloaded_constructor_args():
    sig = inspect.signature(mMDSL::ModelIsLoaded.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::modelload_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ModelLoad)


def test_mmdsl::modelload_constructor_exists():
    assert callable(mMDSL::ModelLoad.__init__)


def test_mmdsl::modelload_constructor_args():
    sig = inspect.signature(mMDSL::ModelLoad.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::modelsave_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ModelSave)


def test_mmdsl::modelsave_constructor_exists():
    assert callable(mMDSL::ModelSave.__init__)


def test_mmdsl::modelsave_constructor_args():
    sig = inspect.signature(mMDSL::ModelSave.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::modeldiscard_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ModelDiscard)


def test_mmdsl::modeldiscard_constructor_exists():
    assert callable(mMDSL::ModelDiscard.__init__)


def test_mmdsl::modeldiscard_constructor_args():
    sig = inspect.signature(mMDSL::ModelDiscard.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::modeldelete_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ModelDelete)


def test_mmdsl::modeldelete_constructor_exists():
    assert callable(mMDSL::ModelDelete.__init__)


def test_mmdsl::modeldelete_constructor_args():
    sig = inspect.signature(mMDSL::ModelDelete.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::modelcreate_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ModelCreate)


def test_mmdsl::modelcreate_constructor_exists():
    assert callable(mMDSL::ModelCreate.__init__)


def test_mmdsl::modelcreate_constructor_args():
    sig = inspect.signature(mMDSL::ModelCreate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::modelcreate_has_name():
    assert hasattr(mMDSL::ModelCreate, "name")
    descriptor = None
    for klass in mMDSL::ModelCreate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::removecontextitem_is_not_abstract():
    assert not inspect.isabstract(mMDSL::RemoveContextItem)


def test_mmdsl::removecontextitem_constructor_exists():
    assert callable(mMDSL::RemoveContextItem.__init__)


def test_mmdsl::removecontextitem_constructor_args():
    sig = inspect.signature(mMDSL::RemoveContextItem.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::insertcontextitem_is_not_abstract():
    assert not inspect.isabstract(mMDSL::InsertContextItem)


def test_mmdsl::insertcontextitem_constructor_exists():
    assert callable(mMDSL::InsertContextItem.__init__)


def test_mmdsl::insertcontextitem_constructor_args():
    sig = inspect.signature(mMDSL::InsertContextItem.__init__)
    params = list(sig.parameters.keys())
    assert "context" in params, "Missing parameter 'context'"
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::insertcontextitem_has_context():
    assert hasattr(mMDSL::InsertContextItem, "context")
    descriptor = None
    for klass in mMDSL::InsertContextItem.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::insertcontextitem_has_name():
    assert hasattr(mMDSL::InsertContextItem, "name")
    descriptor = None
    for klass in mMDSL::InsertContextItem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::removemenuitem_is_not_abstract():
    assert not inspect.isabstract(mMDSL::RemoveMenuItem)


def test_mmdsl::removemenuitem_constructor_exists():
    assert callable(mMDSL::RemoveMenuItem.__init__)


def test_mmdsl::removemenuitem_constructor_args():
    sig = inspect.signature(mMDSL::RemoveMenuItem.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::insertmenuitem_is_not_abstract():
    assert not inspect.isabstract(mMDSL::InsertMenuItem)


def test_mmdsl::insertmenuitem_constructor_exists():
    assert callable(mMDSL::InsertMenuItem.__init__)


def test_mmdsl::insertmenuitem_constructor_args():
    sig = inspect.signature(mMDSL::InsertMenuItem.__init__)
    params = list(sig.parameters.keys())
    assert "menu" in params, "Missing parameter 'menu'"
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::insertmenuitem_has_menu():
    assert hasattr(mMDSL::InsertMenuItem, "menu")
    descriptor = None
    for klass in mMDSL::InsertMenuItem.__mro__:
        if "menu" in klass.__dict__:
            descriptor = klass.__dict__["menu"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::insertmenuitem_has_name():
    assert hasattr(mMDSL::InsertMenuItem, "name")
    descriptor = None
    for klass in mMDSL::InsertMenuItem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::contextitem_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ContextItem)


def test_mmdsl::contextitem_constructor_exists():
    assert callable(mMDSL::ContextItem.__init__)


def test_mmdsl::contextitem_constructor_args():
    sig = inspect.signature(mMDSL::ContextItem.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::menuitem_is_not_abstract():
    assert not inspect.isabstract(mMDSL::MenuItem)


def test_mmdsl::menuitem_constructor_exists():
    assert callable(mMDSL::MenuItem.__init__)


def test_mmdsl::menuitem_constructor_args():
    sig = inspect.signature(mMDSL::MenuItem.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::itemoperation_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ItemOperation)


def test_mmdsl::itemoperation_constructor_exists():
    assert callable(mMDSL::ItemOperation.__init__)


def test_mmdsl::itemoperation_constructor_args():
    sig = inspect.signature(mMDSL::ItemOperation.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::viewbox_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ViewBox)


def test_mmdsl::viewbox_constructor_exists():
    assert callable(mMDSL::ViewBox.__init__)


def test_mmdsl::viewbox_constructor_args():
    sig = inspect.signature(mMDSL::ViewBox.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "title" in params, "Missing parameter 'title'"

def test_mmdsl::viewbox_has_text():
    assert hasattr(mMDSL::ViewBox, "text")
    descriptor = None
    for klass in mMDSL::ViewBox.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::viewbox_has_title():
    assert hasattr(mMDSL::ViewBox, "title")
    descriptor = None
    for klass in mMDSL::ViewBox.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::warningbox_is_not_abstract():
    assert not inspect.isabstract(mMDSL::WarningBox)


def test_mmdsl::warningbox_constructor_exists():
    assert callable(mMDSL::WarningBox.__init__)


def test_mmdsl::warningbox_constructor_args():
    sig = inspect.signature(mMDSL::WarningBox.__init__)
    params = list(sig.parameters.keys())
    assert "buttontype" in params, "Missing parameter 'buttontype'"
    assert "title" in params, "Missing parameter 'title'"
    assert "text" in params, "Missing parameter 'text'"

def test_mmdsl::warningbox_has_buttontype():
    assert hasattr(mMDSL::WarningBox, "buttontype")
    descriptor = None
    for klass in mMDSL::WarningBox.__mro__:
        if "buttontype" in klass.__dict__:
            descriptor = klass.__dict__["buttontype"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::warningbox_has_title():
    assert hasattr(mMDSL::WarningBox, "title")
    descriptor = None
    for klass in mMDSL::WarningBox.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::warningbox_has_text():
    assert hasattr(mMDSL::WarningBox, "text")
    descriptor = None
    for klass in mMDSL::WarningBox.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::errorbox_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ErrorBox)


def test_mmdsl::errorbox_constructor_exists():
    assert callable(mMDSL::ErrorBox.__init__)


def test_mmdsl::errorbox_constructor_args():
    sig = inspect.signature(mMDSL::ErrorBox.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "buttontype" in params, "Missing parameter 'buttontype'"
    assert "text" in params, "Missing parameter 'text'"

def test_mmdsl::errorbox_has_title():
    assert hasattr(mMDSL::ErrorBox, "title")
    descriptor = None
    for klass in mMDSL::ErrorBox.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::errorbox_has_buttontype():
    assert hasattr(mMDSL::ErrorBox, "buttontype")
    descriptor = None
    for klass in mMDSL::ErrorBox.__mro__:
        if "buttontype" in klass.__dict__:
            descriptor = klass.__dict__["buttontype"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::errorbox_has_text():
    assert hasattr(mMDSL::ErrorBox, "text")
    descriptor = None
    for klass in mMDSL::ErrorBox.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::infobox_is_not_abstract():
    assert not inspect.isabstract(mMDSL::InfoBox)


def test_mmdsl::infobox_constructor_exists():
    assert callable(mMDSL::InfoBox.__init__)


def test_mmdsl::infobox_constructor_args():
    sig = inspect.signature(mMDSL::InfoBox.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "text" in params, "Missing parameter 'text'"

def test_mmdsl::infobox_has_title():
    assert hasattr(mMDSL::InfoBox, "title")
    descriptor = None
    for klass in mMDSL::InfoBox.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::infobox_has_text():
    assert hasattr(mMDSL::InfoBox, "text")
    descriptor = None
    for klass in mMDSL::InfoBox.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::editbox_is_not_abstract():
    assert not inspect.isabstract(mMDSL::EditBox)


def test_mmdsl::editbox_constructor_exists():
    assert callable(mMDSL::EditBox.__init__)


def test_mmdsl::editbox_constructor_args():
    sig = inspect.signature(mMDSL::EditBox.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "title" in params, "Missing parameter 'title'"
    assert "okbuttontext" in params, "Missing parameter 'okbuttontext'"

def test_mmdsl::editbox_has_text():
    assert hasattr(mMDSL::EditBox, "text")
    descriptor = None
    for klass in mMDSL::EditBox.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::editbox_has_title():
    assert hasattr(mMDSL::EditBox, "title")
    descriptor = None
    for klass in mMDSL::EditBox.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::editbox_has_okbuttontext():
    assert hasattr(mMDSL::EditBox, "okbuttontext")
    descriptor = None
    for klass in mMDSL::EditBox.__mro__:
        if "okbuttontext" in klass.__dict__:
            descriptor = klass.__dict__["okbuttontext"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::dirlist_is_not_abstract():
    assert not inspect.isabstract(mMDSL::DirList)


def test_mmdsl::dirlist_constructor_exists():
    assert callable(mMDSL::DirList.__init__)


def test_mmdsl::dirlist_constructor_args():
    sig = inspect.signature(mMDSL::DirList.__init__)
    params = list(sig.parameters.keys())
    assert "dirname" in params, "Missing parameter 'dirname'"

def test_mmdsl::dirlist_has_dirname():
    assert hasattr(mMDSL::DirList, "dirname")
    descriptor = None
    for klass in mMDSL::DirList.__mro__:
        if "dirname" in klass.__dict__:
            descriptor = klass.__dict__["dirname"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::dirdelete_is_not_abstract():
    assert not inspect.isabstract(mMDSL::DirDelete)


def test_mmdsl::dirdelete_constructor_exists():
    assert callable(mMDSL::DirDelete.__init__)


def test_mmdsl::dirdelete_constructor_args():
    sig = inspect.signature(mMDSL::DirDelete.__init__)
    params = list(sig.parameters.keys())
    assert "dirname" in params, "Missing parameter 'dirname'"

def test_mmdsl::dirdelete_has_dirname():
    assert hasattr(mMDSL::DirDelete, "dirname")
    descriptor = None
    for klass in mMDSL::DirDelete.__mro__:
        if "dirname" in klass.__dict__:
            descriptor = klass.__dict__["dirname"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::dircreate_is_not_abstract():
    assert not inspect.isabstract(mMDSL::DirCreate)


def test_mmdsl::dircreate_constructor_exists():
    assert callable(mMDSL::DirCreate.__init__)


def test_mmdsl::dircreate_constructor_args():
    sig = inspect.signature(mMDSL::DirCreate.__init__)
    params = list(sig.parameters.keys())
    assert "dirname" in params, "Missing parameter 'dirname'"

def test_mmdsl::dircreate_has_dirname():
    assert hasattr(mMDSL::DirCreate, "dirname")
    descriptor = None
    for klass in mMDSL::DirCreate.__mro__:
        if "dirname" in klass.__dict__:
            descriptor = klass.__dict__["dirname"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::dirgetworking_is_not_abstract():
    assert not inspect.isabstract(mMDSL::DirGetWorking)


def test_mmdsl::dirgetworking_constructor_exists():
    assert callable(mMDSL::DirGetWorking.__init__)


def test_mmdsl::dirgetworking_constructor_args():
    sig = inspect.signature(mMDSL::DirGetWorking.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::dirsetworking_is_not_abstract():
    assert not inspect.isabstract(mMDSL::DirSetWorking)


def test_mmdsl::dirsetworking_constructor_exists():
    assert callable(mMDSL::DirSetWorking.__init__)


def test_mmdsl::dirsetworking_constructor_args():
    sig = inspect.signature(mMDSL::DirSetWorking.__init__)
    params = list(sig.parameters.keys())
    assert "dirname" in params, "Missing parameter 'dirname'"

def test_mmdsl::dirsetworking_has_dirname():
    assert hasattr(mMDSL::DirSetWorking, "dirname")
    descriptor = None
    for klass in mMDSL::DirSetWorking.__mro__:
        if "dirname" in klass.__dict__:
            descriptor = klass.__dict__["dirname"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::filewrite_is_not_abstract():
    assert not inspect.isabstract(mMDSL::FileWrite)


def test_mmdsl::filewrite_constructor_exists():
    assert callable(mMDSL::FileWrite.__init__)


def test_mmdsl::filewrite_constructor_args():
    sig = inspect.signature(mMDSL::FileWrite.__init__)
    params = list(sig.parameters.keys())
    assert "append" in params, "Missing parameter 'append'"
    assert "text" in params, "Missing parameter 'text'"
    assert "filename" in params, "Missing parameter 'filename'"

def test_mmdsl::filewrite_has_append():
    assert hasattr(mMDSL::FileWrite, "append")
    descriptor = None
    for klass in mMDSL::FileWrite.__mro__:
        if "append" in klass.__dict__:
            descriptor = klass.__dict__["append"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::filewrite_has_text():
    assert hasattr(mMDSL::FileWrite, "text")
    descriptor = None
    for klass in mMDSL::FileWrite.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::filewrite_has_filename():
    assert hasattr(mMDSL::FileWrite, "filename")
    descriptor = None
    for klass in mMDSL::FileWrite.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::fileread_is_not_abstract():
    assert not inspect.isabstract(mMDSL::FileRead)


def test_mmdsl::fileread_constructor_exists():
    assert callable(mMDSL::FileRead.__init__)


def test_mmdsl::fileread_constructor_args():
    sig = inspect.signature(mMDSL::FileRead.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_mmdsl::fileread_has_filename():
    assert hasattr(mMDSL::FileRead, "filename")
    descriptor = None
    for klass in mMDSL::FileRead.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::filecreate_is_not_abstract():
    assert not inspect.isabstract(mMDSL::FileCreate)


def test_mmdsl::filecreate_constructor_exists():
    assert callable(mMDSL::FileCreate.__init__)


def test_mmdsl::filecreate_constructor_args():
    sig = inspect.signature(mMDSL::FileCreate.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_mmdsl::filecreate_has_filename():
    assert hasattr(mMDSL::FileCreate, "filename")
    descriptor = None
    for klass in mMDSL::FileCreate.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::filedelete_is_not_abstract():
    assert not inspect.isabstract(mMDSL::FileDelete)


def test_mmdsl::filedelete_constructor_exists():
    assert callable(mMDSL::FileDelete.__init__)


def test_mmdsl::filedelete_constructor_args():
    sig = inspect.signature(mMDSL::FileDelete.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"

def test_mmdsl::filedelete_has_filename():
    assert hasattr(mMDSL::FileDelete, "filename")
    descriptor = None
    for klass in mMDSL::FileDelete.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::filecopy_is_not_abstract():
    assert not inspect.isabstract(mMDSL::FileCopy)


def test_mmdsl::filecopy_constructor_exists():
    assert callable(mMDSL::FileCopy.__init__)


def test_mmdsl::filecopy_constructor_args():
    sig = inspect.signature(mMDSL::FileCopy.__init__)
    params = list(sig.parameters.keys())
    assert "dest" in params, "Missing parameter 'dest'"
    assert "src" in params, "Missing parameter 'src'"

def test_mmdsl::filecopy_has_dest():
    assert hasattr(mMDSL::FileCopy, "dest")
    descriptor = None
    for klass in mMDSL::FileCopy.__mro__:
        if "dest" in klass.__dict__:
            descriptor = klass.__dict__["dest"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::filecopy_has_src():
    assert hasattr(mMDSL::FileCopy, "src")
    descriptor = None
    for klass in mMDSL::FileCopy.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::attributeoperation_is_not_abstract():
    assert not inspect.isabstract(mMDSL::AttributeOperation)


def test_mmdsl::attributeoperation_constructor_exists():
    assert callable(mMDSL::AttributeOperation.__init__)


def test_mmdsl::attributeoperation_constructor_args():
    sig = inspect.signature(mMDSL::AttributeOperation.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::instanceoperation_is_not_abstract():
    assert not inspect.isabstract(mMDSL::InstanceOperation)


def test_mmdsl::instanceoperation_constructor_exists():
    assert callable(mMDSL::InstanceOperation.__init__)


def test_mmdsl::instanceoperation_constructor_args():
    sig = inspect.signature(mMDSL::InstanceOperation.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::modeloperation_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ModelOperation)


def test_mmdsl::modeloperation_constructor_exists():
    assert callable(mMDSL::ModelOperation.__init__)


def test_mmdsl::modeloperation_constructor_args():
    sig = inspect.signature(mMDSL::ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::simpleui_is_not_abstract():
    assert not inspect.isabstract(mMDSL::SimpleUI)


def test_mmdsl::simpleui_constructor_exists():
    assert callable(mMDSL::SimpleUI.__init__)


def test_mmdsl::simpleui_constructor_args():
    sig = inspect.signature(mMDSL::SimpleUI.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::diroperation_is_not_abstract():
    assert not inspect.isabstract(mMDSL::DirOperation)


def test_mmdsl::diroperation_constructor_exists():
    assert callable(mMDSL::DirOperation.__init__)


def test_mmdsl::diroperation_constructor_args():
    sig = inspect.signature(mMDSL::DirOperation.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::fileoperation_is_not_abstract():
    assert not inspect.isabstract(mMDSL::FileOperation)


def test_mmdsl::fileoperation_constructor_exists():
    assert callable(mMDSL::FileOperation.__init__)


def test_mmdsl::fileoperation_constructor_args():
    sig = inspect.signature(mMDSL::FileOperation.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::eobject_is_not_abstract():
    assert not inspect.isabstract(mMDSL::EObject)


def test_mmdsl::eobject_constructor_exists():
    assert callable(mMDSL::EObject.__init__)


def test_mmdsl::eobject_constructor_args():
    sig = inspect.signature(mMDSL::EObject.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::expression_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Expression)


def test_mmdsl::expression_constructor_exists():
    assert callable(mMDSL::Expression.__init__)


def test_mmdsl::expression_constructor_args():
    sig = inspect.signature(mMDSL::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "false" in params, "Missing parameter 'false'"
    assert "valueString" in params, "Missing parameter 'valueString'"
    assert "valueRealNumber" in params, "Missing parameter 'valueRealNumber'"
    assert "true" in params, "Missing parameter 'true'"

def test_mmdsl::expression_has_false():
    assert hasattr(mMDSL::Expression, "false")
    descriptor = None
    for klass in mMDSL::Expression.__mro__:
        if "false" in klass.__dict__:
            descriptor = klass.__dict__["false"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::expression_has_valueString():
    assert hasattr(mMDSL::Expression, "valueString")
    descriptor = None
    for klass in mMDSL::Expression.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::expression_has_valueRealNumber():
    assert hasattr(mMDSL::Expression, "valueRealNumber")
    descriptor = None
    for klass in mMDSL::Expression.__mro__:
        if "valueRealNumber" in klass.__dict__:
            descriptor = klass.__dict__["valueRealNumber"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::expression_has_true():
    assert hasattr(mMDSL::Expression, "true")
    descriptor = None
    for klass in mMDSL::Expression.__mro__:
        if "true" in klass.__dict__:
            descriptor = klass.__dict__["true"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::operatoror_is_not_abstract():
    assert not inspect.isabstract(mMDSL::OperatorOr)


def test_mmdsl::operatoror_constructor_exists():
    assert callable(mMDSL::OperatorOr.__init__)


def test_mmdsl::operatoror_constructor_args():
    sig = inspect.signature(mMDSL::OperatorOr.__init__)
    params = list(sig.parameters.keys())
    assert "or_" in params, "Missing parameter 'or_'"

def test_mmdsl::operatoror_has_or_():
    assert hasattr(mMDSL::OperatorOr, "or_")
    descriptor = None
    for klass in mMDSL::OperatorOr.__mro__:
        if "or_" in klass.__dict__:
            descriptor = klass.__dict__["or_"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::operatorand_is_not_abstract():
    assert not inspect.isabstract(mMDSL::OperatorAnd)


def test_mmdsl::operatorand_constructor_exists():
    assert callable(mMDSL::OperatorAnd.__init__)


def test_mmdsl::operatorand_constructor_args():
    sig = inspect.signature(mMDSL::OperatorAnd.__init__)
    params = list(sig.parameters.keys())
    assert "and_" in params, "Missing parameter 'and_'"

def test_mmdsl::operatorand_has_and_():
    assert hasattr(mMDSL::OperatorAnd, "and_")
    descriptor = None
    for klass in mMDSL::OperatorAnd.__mro__:
        if "and_" in klass.__dict__:
            descriptor = klass.__dict__["and_"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::operatorequal_is_not_abstract():
    assert not inspect.isabstract(mMDSL::OperatorEqual)


def test_mmdsl::operatorequal_constructor_exists():
    assert callable(mMDSL::OperatorEqual.__init__)


def test_mmdsl::operatorequal_constructor_args():
    sig = inspect.signature(mMDSL::OperatorEqual.__init__)
    params = list(sig.parameters.keys())
    assert "equal" in params, "Missing parameter 'equal'"
    assert "notequal" in params, "Missing parameter 'notequal'"

def test_mmdsl::operatorequal_has_equal():
    assert hasattr(mMDSL::OperatorEqual, "equal")
    descriptor = None
    for klass in mMDSL::OperatorEqual.__mro__:
        if "equal" in klass.__dict__:
            descriptor = klass.__dict__["equal"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::operatorequal_has_notequal():
    assert hasattr(mMDSL::OperatorEqual, "notequal")
    descriptor = None
    for klass in mMDSL::OperatorEqual.__mro__:
        if "notequal" in klass.__dict__:
            descriptor = klass.__dict__["notequal"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::operatorcompare_is_not_abstract():
    assert not inspect.isabstract(mMDSL::OperatorCompare)


def test_mmdsl::operatorcompare_constructor_exists():
    assert callable(mMDSL::OperatorCompare.__init__)


def test_mmdsl::operatorcompare_constructor_args():
    sig = inspect.signature(mMDSL::OperatorCompare.__init__)
    params = list(sig.parameters.keys())
    assert "greaterequal" in params, "Missing parameter 'greaterequal'"
    assert "lesserequal" in params, "Missing parameter 'lesserequal'"
    assert "greater" in params, "Missing parameter 'greater'"
    assert "lesser" in params, "Missing parameter 'lesser'"

def test_mmdsl::operatorcompare_has_greaterequal():
    assert hasattr(mMDSL::OperatorCompare, "greaterequal")
    descriptor = None
    for klass in mMDSL::OperatorCompare.__mro__:
        if "greaterequal" in klass.__dict__:
            descriptor = klass.__dict__["greaterequal"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::operatorcompare_has_lesserequal():
    assert hasattr(mMDSL::OperatorCompare, "lesserequal")
    descriptor = None
    for klass in mMDSL::OperatorCompare.__mro__:
        if "lesserequal" in klass.__dict__:
            descriptor = klass.__dict__["lesserequal"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::operatorcompare_has_greater():
    assert hasattr(mMDSL::OperatorCompare, "greater")
    descriptor = None
    for klass in mMDSL::OperatorCompare.__mro__:
        if "greater" in klass.__dict__:
            descriptor = klass.__dict__["greater"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::operatorcompare_has_lesser():
    assert hasattr(mMDSL::OperatorCompare, "lesser")
    descriptor = None
    for klass in mMDSL::OperatorCompare.__mro__:
        if "lesser" in klass.__dict__:
            descriptor = klass.__dict__["lesser"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::operatoradd_is_not_abstract():
    assert not inspect.isabstract(mMDSL::OperatorAdd)


def test_mmdsl::operatoradd_constructor_exists():
    assert callable(mMDSL::OperatorAdd.__init__)


def test_mmdsl::operatoradd_constructor_args():
    sig = inspect.signature(mMDSL::OperatorAdd.__init__)
    params = list(sig.parameters.keys())
    assert "add" in params, "Missing parameter 'add'"
    assert "subtract" in params, "Missing parameter 'subtract'"

def test_mmdsl::operatoradd_has_add():
    assert hasattr(mMDSL::OperatorAdd, "add")
    descriptor = None
    for klass in mMDSL::OperatorAdd.__mro__:
        if "add" in klass.__dict__:
            descriptor = klass.__dict__["add"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::operatoradd_has_subtract():
    assert hasattr(mMDSL::OperatorAdd, "subtract")
    descriptor = None
    for klass in mMDSL::OperatorAdd.__mro__:
        if "subtract" in klass.__dict__:
            descriptor = klass.__dict__["subtract"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::operatormultiply_is_not_abstract():
    assert not inspect.isabstract(mMDSL::OperatorMultiply)


def test_mmdsl::operatormultiply_constructor_exists():
    assert callable(mMDSL::OperatorMultiply.__init__)


def test_mmdsl::operatormultiply_constructor_args():
    sig = inspect.signature(mMDSL::OperatorMultiply.__init__)
    params = list(sig.parameters.keys())
    assert "multiply" in params, "Missing parameter 'multiply'"
    assert "modulo" in params, "Missing parameter 'modulo'"
    assert "divide" in params, "Missing parameter 'divide'"

def test_mmdsl::operatormultiply_has_multiply():
    assert hasattr(mMDSL::OperatorMultiply, "multiply")
    descriptor = None
    for klass in mMDSL::OperatorMultiply.__mro__:
        if "multiply" in klass.__dict__:
            descriptor = klass.__dict__["multiply"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::operatormultiply_has_modulo():
    assert hasattr(mMDSL::OperatorMultiply, "modulo")
    descriptor = None
    for klass in mMDSL::OperatorMultiply.__mro__:
        if "modulo" in klass.__dict__:
            descriptor = klass.__dict__["modulo"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::operatormultiply_has_divide():
    assert hasattr(mMDSL::OperatorMultiply, "divide")
    descriptor = None
    for klass in mMDSL::OperatorMultiply.__mro__:
        if "divide" in klass.__dict__:
            descriptor = klass.__dict__["divide"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::operatorunary_is_not_abstract():
    assert not inspect.isabstract(mMDSL::OperatorUnary)


def test_mmdsl::operatorunary_constructor_exists():
    assert callable(mMDSL::OperatorUnary.__init__)


def test_mmdsl::operatorunary_constructor_args():
    sig = inspect.signature(mMDSL::OperatorUnary.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_mmdsl::operatorunary_has_not_():
    assert hasattr(mMDSL::OperatorUnary, "not_")
    descriptor = None
    for klass in mMDSL::OperatorUnary.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::operatormultyassign_is_not_abstract():
    assert not inspect.isabstract(mMDSL::OperatorMultyAssign)


def test_mmdsl::operatormultyassign_constructor_exists():
    assert callable(mMDSL::OperatorMultyAssign.__init__)


def test_mmdsl::operatormultyassign_constructor_args():
    sig = inspect.signature(mMDSL::OperatorMultyAssign.__init__)
    params = list(sig.parameters.keys())
    assert "addassign" in params, "Missing parameter 'addassign'"
    assert "divassign" in params, "Missing parameter 'divassign'"
    assert "multiassign" in params, "Missing parameter 'multiassign'"
    assert "subassign" in params, "Missing parameter 'subassign'"

def test_mmdsl::operatormultyassign_has_addassign():
    assert hasattr(mMDSL::OperatorMultyAssign, "addassign")
    descriptor = None
    for klass in mMDSL::OperatorMultyAssign.__mro__:
        if "addassign" in klass.__dict__:
            descriptor = klass.__dict__["addassign"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::operatormultyassign_has_divassign():
    assert hasattr(mMDSL::OperatorMultyAssign, "divassign")
    descriptor = None
    for klass in mMDSL::OperatorMultyAssign.__mro__:
        if "divassign" in klass.__dict__:
            descriptor = klass.__dict__["divassign"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::operatormultyassign_has_multiassign():
    assert hasattr(mMDSL::OperatorMultyAssign, "multiassign")
    descriptor = None
    for klass in mMDSL::OperatorMultyAssign.__mro__:
        if "multiassign" in klass.__dict__:
            descriptor = klass.__dict__["multiassign"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::operatormultyassign_has_subassign():
    assert hasattr(mMDSL::OperatorMultyAssign, "subassign")
    descriptor = None
    for klass in mMDSL::OperatorMultyAssign.__mro__:
        if "subassign" in klass.__dict__:
            descriptor = klass.__dict__["subassign"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::varstatement_is_not_abstract():
    assert not inspect.isabstract(mMDSL::VarStatement)


def test_mmdsl::varstatement_constructor_exists():
    assert callable(mMDSL::VarStatement.__init__)


def test_mmdsl::varstatement_constructor_args():
    sig = inspect.signature(mMDSL::VarStatement.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::operatorassign_is_not_abstract():
    assert not inspect.isabstract(mMDSL::OperatorAssign)


def test_mmdsl::operatorassign_constructor_exists():
    assert callable(mMDSL::OperatorAssign.__init__)


def test_mmdsl::operatorassign_constructor_args():
    sig = inspect.signature(mMDSL::OperatorAssign.__init__)
    params = list(sig.parameters.keys())
    assert "assign" in params, "Missing parameter 'assign'"

def test_mmdsl::operatorassign_has_assign():
    assert hasattr(mMDSL::OperatorAssign, "assign")
    descriptor = None
    for klass in mMDSL::OperatorAssign.__mro__:
        if "assign" in klass.__dict__:
            descriptor = klass.__dict__["assign"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::breakcontinue_is_not_abstract():
    assert not inspect.isabstract(mMDSL::BreakContinue)


def test_mmdsl::breakcontinue_constructor_exists():
    assert callable(mMDSL::BreakContinue.__init__)


def test_mmdsl::breakcontinue_constructor_args():
    sig = inspect.signature(mMDSL::BreakContinue.__init__)
    params = list(sig.parameters.keys())
    assert "break_" in params, "Missing parameter 'break_'"
    assert "continue_" in params, "Missing parameter 'continue_'"

def test_mmdsl::breakcontinue_has_break_():
    assert hasattr(mMDSL::BreakContinue, "break_")
    descriptor = None
    for klass in mMDSL::BreakContinue.__mro__:
        if "break_" in klass.__dict__:
            descriptor = klass.__dict__["break_"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::breakcontinue_has_continue_():
    assert hasattr(mMDSL::BreakContinue, "continue_")
    descriptor = None
    for klass in mMDSL::BreakContinue.__mro__:
        if "continue_" in klass.__dict__:
            descriptor = klass.__dict__["continue_"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::forloop_is_not_abstract():
    assert not inspect.isabstract(mMDSL::ForLoop)


def test_mmdsl::forloop_constructor_exists():
    assert callable(mMDSL::ForLoop.__init__)


def test_mmdsl::forloop_constructor_args():
    sig = inspect.signature(mMDSL::ForLoop.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "stop" in params, "Missing parameter 'stop'"
    assert "interval" in params, "Missing parameter 'interval'"

def test_mmdsl::forloop_has_start():
    assert hasattr(mMDSL::ForLoop, "start")
    descriptor = None
    for klass in mMDSL::ForLoop.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::forloop_has_stop():
    assert hasattr(mMDSL::ForLoop, "stop")
    descriptor = None
    for klass in mMDSL::ForLoop.__mro__:
        if "stop" in klass.__dict__:
            descriptor = klass.__dict__["stop"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::forloop_has_interval():
    assert hasattr(mMDSL::ForLoop, "interval")
    descriptor = None
    for klass in mMDSL::ForLoop.__mro__:
        if "interval" in klass.__dict__:
            descriptor = klass.__dict__["interval"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::whileloop_is_not_abstract():
    assert not inspect.isabstract(mMDSL::WhileLoop)


def test_mmdsl::whileloop_constructor_exists():
    assert callable(mMDSL::WhileLoop.__init__)


def test_mmdsl::whileloop_constructor_args():
    sig = inspect.signature(mMDSL::WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::expr_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Expr)


def test_mmdsl::expr_constructor_exists():
    assert callable(mMDSL::Expr.__init__)


def test_mmdsl::expr_constructor_args():
    sig = inspect.signature(mMDSL::Expr.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::algorithmoperation_is_not_abstract():
    assert not inspect.isabstract(mMDSL::AlgorithmOperation)


def test_mmdsl::algorithmoperation_constructor_exists():
    assert callable(mMDSL::AlgorithmOperation.__init__)


def test_mmdsl::algorithmoperation_constructor_args():
    sig = inspect.signature(mMDSL::AlgorithmOperation.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::variable_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Variable)


def test_mmdsl::variable_constructor_exists():
    assert callable(mMDSL::Variable.__init__)


def test_mmdsl::variable_constructor_args():
    sig = inspect.signature(mMDSL::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmdsl::variable_has_name():
    assert hasattr(mMDSL::Variable, "name")
    descriptor = None
    for klass in mMDSL::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::loopstatement_is_not_abstract():
    assert not inspect.isabstract(mMDSL::LoopStatement)


def test_mmdsl::loopstatement_constructor_exists():
    assert callable(mMDSL::LoopStatement.__init__)


def test_mmdsl::loopstatement_constructor_args():
    sig = inspect.signature(mMDSL::LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::selectionstatement_is_not_abstract():
    assert not inspect.isabstract(mMDSL::SelectionStatement)


def test_mmdsl::selectionstatement_constructor_exists():
    assert callable(mMDSL::SelectionStatement.__init__)


def test_mmdsl::selectionstatement_constructor_args():
    sig = inspect.signature(mMDSL::SelectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::statement_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Statement)


def test_mmdsl::statement_constructor_exists():
    assert callable(mMDSL::Statement.__init__)


def test_mmdsl::statement_constructor_args():
    sig = inspect.signature(mMDSL::Statement.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::strokecolor_is_not_abstract():
    assert not inspect.isabstract(mMDSL::StrokeColor)


def test_mmdsl::strokecolor_constructor_exists():
    assert callable(mMDSL::StrokeColor.__init__)


def test_mmdsl::strokecolor_constructor_args():
    sig = inspect.signature(mMDSL::StrokeColor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "hexcolor" in params, "Missing parameter 'hexcolor'"

def test_mmdsl::strokecolor_has_color():
    assert hasattr(mMDSL::StrokeColor, "color")
    descriptor = None
    for klass in mMDSL::StrokeColor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::strokecolor_has_hexcolor():
    assert hasattr(mMDSL::StrokeColor, "hexcolor")
    descriptor = None
    for klass in mMDSL::StrokeColor.__mro__:
        if "hexcolor" in klass.__dict__:
            descriptor = klass.__dict__["hexcolor"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::pathparametersa_is_not_abstract():
    assert not inspect.isabstract(mMDSL::PathParametersA)


def test_mmdsl::pathparametersa_constructor_exists():
    assert callable(mMDSL::PathParametersA.__init__)


def test_mmdsl::pathparametersa_constructor_args():
    sig = inspect.signature(mMDSL::PathParametersA.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "rx" in params, "Missing parameter 'rx'"
    assert "x" in params, "Missing parameter 'x'"
    assert "xaxisrot" in params, "Missing parameter 'xaxisrot'"
    assert "sweepflag" in params, "Missing parameter 'sweepflag'"
    assert "largearcflag" in params, "Missing parameter 'largearcflag'"
    assert "ry" in params, "Missing parameter 'ry'"

def test_mmdsl::pathparametersa_has_y():
    assert hasattr(mMDSL::PathParametersA, "y")
    descriptor = None
    for klass in mMDSL::PathParametersA.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersa_has_rx():
    assert hasattr(mMDSL::PathParametersA, "rx")
    descriptor = None
    for klass in mMDSL::PathParametersA.__mro__:
        if "rx" in klass.__dict__:
            descriptor = klass.__dict__["rx"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersa_has_x():
    assert hasattr(mMDSL::PathParametersA, "x")
    descriptor = None
    for klass in mMDSL::PathParametersA.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersa_has_xaxisrot():
    assert hasattr(mMDSL::PathParametersA, "xaxisrot")
    descriptor = None
    for klass in mMDSL::PathParametersA.__mro__:
        if "xaxisrot" in klass.__dict__:
            descriptor = klass.__dict__["xaxisrot"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersa_has_sweepflag():
    assert hasattr(mMDSL::PathParametersA, "sweepflag")
    descriptor = None
    for klass in mMDSL::PathParametersA.__mro__:
        if "sweepflag" in klass.__dict__:
            descriptor = klass.__dict__["sweepflag"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersa_has_largearcflag():
    assert hasattr(mMDSL::PathParametersA, "largearcflag")
    descriptor = None
    for klass in mMDSL::PathParametersA.__mro__:
        if "largearcflag" in klass.__dict__:
            descriptor = klass.__dict__["largearcflag"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersa_has_ry():
    assert hasattr(mMDSL::PathParametersA, "ry")
    descriptor = None
    for klass in mMDSL::PathParametersA.__mro__:
        if "ry" in klass.__dict__:
            descriptor = klass.__dict__["ry"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::pathparametersq_is_not_abstract():
    assert not inspect.isabstract(mMDSL::PathParametersQ)


def test_mmdsl::pathparametersq_constructor_exists():
    assert callable(mMDSL::PathParametersQ.__init__)


def test_mmdsl::pathparametersq_constructor_args():
    sig = inspect.signature(mMDSL::PathParametersQ.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x1" in params, "Missing parameter 'x1'"
    assert "y1" in params, "Missing parameter 'y1'"
    assert "x" in params, "Missing parameter 'x'"

def test_mmdsl::pathparametersq_has_y():
    assert hasattr(mMDSL::PathParametersQ, "y")
    descriptor = None
    for klass in mMDSL::PathParametersQ.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersq_has_x1():
    assert hasattr(mMDSL::PathParametersQ, "x1")
    descriptor = None
    for klass in mMDSL::PathParametersQ.__mro__:
        if "x1" in klass.__dict__:
            descriptor = klass.__dict__["x1"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersq_has_y1():
    assert hasattr(mMDSL::PathParametersQ, "y1")
    descriptor = None
    for klass in mMDSL::PathParametersQ.__mro__:
        if "y1" in klass.__dict__:
            descriptor = klass.__dict__["y1"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersq_has_x():
    assert hasattr(mMDSL::PathParametersQ, "x")
    descriptor = None
    for klass in mMDSL::PathParametersQ.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::pathparameterss_is_not_abstract():
    assert not inspect.isabstract(mMDSL::PathParametersS)


def test_mmdsl::pathparameterss_constructor_exists():
    assert callable(mMDSL::PathParametersS.__init__)


def test_mmdsl::pathparameterss_constructor_args():
    sig = inspect.signature(mMDSL::PathParametersS.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x2" in params, "Missing parameter 'x2'"
    assert "y2" in params, "Missing parameter 'y2'"

def test_mmdsl::pathparameterss_has_x():
    assert hasattr(mMDSL::PathParametersS, "x")
    descriptor = None
    for klass in mMDSL::PathParametersS.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparameterss_has_y():
    assert hasattr(mMDSL::PathParametersS, "y")
    descriptor = None
    for klass in mMDSL::PathParametersS.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparameterss_has_x2():
    assert hasattr(mMDSL::PathParametersS, "x2")
    descriptor = None
    for klass in mMDSL::PathParametersS.__mro__:
        if "x2" in klass.__dict__:
            descriptor = klass.__dict__["x2"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparameterss_has_y2():
    assert hasattr(mMDSL::PathParametersS, "y2")
    descriptor = None
    for klass in mMDSL::PathParametersS.__mro__:
        if "y2" in klass.__dict__:
            descriptor = klass.__dict__["y2"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::pathparametersc_is_not_abstract():
    assert not inspect.isabstract(mMDSL::PathParametersC)


def test_mmdsl::pathparametersc_constructor_exists():
    assert callable(mMDSL::PathParametersC.__init__)


def test_mmdsl::pathparametersc_constructor_args():
    sig = inspect.signature(mMDSL::PathParametersC.__init__)
    params = list(sig.parameters.keys())
    assert "x1" in params, "Missing parameter 'x1'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "x2" in params, "Missing parameter 'x2'"
    assert "y1" in params, "Missing parameter 'y1'"
    assert "y2" in params, "Missing parameter 'y2'"

def test_mmdsl::pathparametersc_has_x1():
    assert hasattr(mMDSL::PathParametersC, "x1")
    descriptor = None
    for klass in mMDSL::PathParametersC.__mro__:
        if "x1" in klass.__dict__:
            descriptor = klass.__dict__["x1"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersc_has_y():
    assert hasattr(mMDSL::PathParametersC, "y")
    descriptor = None
    for klass in mMDSL::PathParametersC.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersc_has_x():
    assert hasattr(mMDSL::PathParametersC, "x")
    descriptor = None
    for klass in mMDSL::PathParametersC.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersc_has_x2():
    assert hasattr(mMDSL::PathParametersC, "x2")
    descriptor = None
    for klass in mMDSL::PathParametersC.__mro__:
        if "x2" in klass.__dict__:
            descriptor = klass.__dict__["x2"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersc_has_y1():
    assert hasattr(mMDSL::PathParametersC, "y1")
    descriptor = None
    for klass in mMDSL::PathParametersC.__mro__:
        if "y1" in klass.__dict__:
            descriptor = klass.__dict__["y1"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersc_has_y2():
    assert hasattr(mMDSL::PathParametersC, "y2")
    descriptor = None
    for klass in mMDSL::PathParametersC.__mro__:
        if "y2" in klass.__dict__:
            descriptor = klass.__dict__["y2"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::pathparametershv_is_not_abstract():
    assert not inspect.isabstract(mMDSL::PathParametersHV)


def test_mmdsl::pathparametershv_constructor_exists():
    assert callable(mMDSL::PathParametersHV.__init__)


def test_mmdsl::pathparametershv_constructor_args():
    sig = inspect.signature(mMDSL::PathParametersHV.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_mmdsl::pathparametershv_has_x():
    assert hasattr(mMDSL::PathParametersHV, "x")
    descriptor = None
    for klass in mMDSL::PathParametersHV.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::pathparametersmlt_is_not_abstract():
    assert not inspect.isabstract(mMDSL::PathParametersMLT)


def test_mmdsl::pathparametersmlt_constructor_exists():
    assert callable(mMDSL::PathParametersMLT.__init__)


def test_mmdsl::pathparametersmlt_constructor_args():
    sig = inspect.signature(mMDSL::PathParametersMLT.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_mmdsl::pathparametersmlt_has_y():
    assert hasattr(mMDSL::PathParametersMLT, "y")
    descriptor = None
    for klass in mMDSL::PathParametersMLT.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::pathparametersmlt_has_x():
    assert hasattr(mMDSL::PathParametersMLT, "x")
    descriptor = None
    for klass in mMDSL::PathParametersMLT.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::ellipticalarc_is_not_abstract():
    assert not inspect.isabstract(mMDSL::EllipticalArc)


def test_mmdsl::ellipticalarc_constructor_exists():
    assert callable(mMDSL::EllipticalArc.__init__)


def test_mmdsl::ellipticalarc_constructor_args():
    sig = inspect.signature(mMDSL::EllipticalArc.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::smoothquadraticbeziercurveto_is_not_abstract():
    assert not inspect.isabstract(mMDSL::SmoothQuadraticBezierCurveTo)


def test_mmdsl::smoothquadraticbeziercurveto_constructor_exists():
    assert callable(mMDSL::SmoothQuadraticBezierCurveTo.__init__)


def test_mmdsl::smoothquadraticbeziercurveto_constructor_args():
    sig = inspect.signature(mMDSL::SmoothQuadraticBezierCurveTo.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::quadraticbeziercurve_is_not_abstract():
    assert not inspect.isabstract(mMDSL::QuadraticBezierCurve)


def test_mmdsl::quadraticbeziercurve_constructor_exists():
    assert callable(mMDSL::QuadraticBezierCurve.__init__)


def test_mmdsl::quadraticbeziercurve_constructor_args():
    sig = inspect.signature(mMDSL::QuadraticBezierCurve.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::smoothcurveto_is_not_abstract():
    assert not inspect.isabstract(mMDSL::SmoothCurveTo)


def test_mmdsl::smoothcurveto_constructor_exists():
    assert callable(mMDSL::SmoothCurveTo.__init__)


def test_mmdsl::smoothcurveto_constructor_args():
    sig = inspect.signature(mMDSL::SmoothCurveTo.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::curveto_is_not_abstract():
    assert not inspect.isabstract(mMDSL::CurveTo)


def test_mmdsl::curveto_constructor_exists():
    assert callable(mMDSL::CurveTo.__init__)


def test_mmdsl::curveto_constructor_args():
    sig = inspect.signature(mMDSL::CurveTo.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::verticallineto_is_not_abstract():
    assert not inspect.isabstract(mMDSL::VerticalLineTo)


def test_mmdsl::verticallineto_constructor_exists():
    assert callable(mMDSL::VerticalLineTo.__init__)


def test_mmdsl::verticallineto_constructor_args():
    sig = inspect.signature(mMDSL::VerticalLineTo.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::horizontallineto_is_not_abstract():
    assert not inspect.isabstract(mMDSL::HorizontalLineTo)


def test_mmdsl::horizontallineto_constructor_exists():
    assert callable(mMDSL::HorizontalLineTo.__init__)


def test_mmdsl::horizontallineto_constructor_args():
    sig = inspect.signature(mMDSL::HorizontalLineTo.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::lineto_is_not_abstract():
    assert not inspect.isabstract(mMDSL::LineTo)


def test_mmdsl::lineto_constructor_exists():
    assert callable(mMDSL::LineTo.__init__)


def test_mmdsl::lineto_constructor_args():
    sig = inspect.signature(mMDSL::LineTo.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::moveto_is_not_abstract():
    assert not inspect.isabstract(mMDSL::MoveTo)


def test_mmdsl::moveto_constructor_exists():
    assert callable(mMDSL::MoveTo.__init__)


def test_mmdsl::moveto_constructor_args():
    sig = inspect.signature(mMDSL::MoveTo.__init__)
    params = list(sig.parameters.keys())



def test_mmdsl::fillcolor_is_not_abstract():
    assert not inspect.isabstract(mMDSL::FillColor)


def test_mmdsl::fillcolor_constructor_exists():
    assert callable(mMDSL::FillColor.__init__)


def test_mmdsl::fillcolor_constructor_args():
    sig = inspect.signature(mMDSL::FillColor.__init__)
    params = list(sig.parameters.keys())
    assert "hexcolor" in params, "Missing parameter 'hexcolor'"
    assert "color" in params, "Missing parameter 'color'"

def test_mmdsl::fillcolor_has_hexcolor():
    assert hasattr(mMDSL::FillColor, "hexcolor")
    descriptor = None
    for klass in mMDSL::FillColor.__mro__:
        if "hexcolor" in klass.__dict__:
            descriptor = klass.__dict__["hexcolor"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::fillcolor_has_color():
    assert hasattr(mMDSL::FillColor, "color")
    descriptor = None
    for klass in mMDSL::FillColor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::fontfamily_is_not_abstract():
    assert not inspect.isabstract(mMDSL::FontFamily)


def test_mmdsl::fontfamily_constructor_exists():
    assert callable(mMDSL::FontFamily.__init__)


def test_mmdsl::fontfamily_constructor_args():
    sig = inspect.signature(mMDSL::FontFamily.__init__)
    params = list(sig.parameters.keys())
    assert "font" in params, "Missing parameter 'font'"
    assert "fontstr" in params, "Missing parameter 'fontstr'"

def test_mmdsl::fontfamily_has_font():
    assert hasattr(mMDSL::FontFamily, "font")
    descriptor = None
    for klass in mMDSL::FontFamily.__mro__:
        if "font" in klass.__dict__:
            descriptor = klass.__dict__["font"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::fontfamily_has_fontstr():
    assert hasattr(mMDSL::FontFamily, "fontstr")
    descriptor = None
    for klass in mMDSL::FontFamily.__mro__:
        if "fontstr" in klass.__dict__:
            descriptor = klass.__dict__["fontstr"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::pathdata_is_not_abstract():
    assert not inspect.isabstract(mMDSL::PathData)


def test_mmdsl::pathdata_constructor_exists():
    assert callable(mMDSL::PathData.__init__)


def test_mmdsl::pathdata_constructor_args():
    sig = inspect.signature(mMDSL::PathData.__init__)
    params = list(sig.parameters.keys())
    assert "closepath" in params, "Missing parameter 'closepath'"

def test_mmdsl::pathdata_has_closepath():
    assert hasattr(mMDSL::PathData, "closepath")
    descriptor = None
    for klass in mMDSL::PathData.__mro__:
        if "closepath" in klass.__dict__:
            descriptor = klass.__dict__["closepath"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::points_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Points)


def test_mmdsl::points_constructor_exists():
    assert callable(mMDSL::Points.__init__)


def test_mmdsl::points_constructor_args():
    sig = inspect.signature(mMDSL::Points.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_mmdsl::points_has_x():
    assert hasattr(mMDSL::Points, "x")
    descriptor = None
    for klass in mMDSL::Points.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::points_has_y():
    assert hasattr(mMDSL::Points, "y")
    descriptor = None
    for klass in mMDSL::Points.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::text_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Text)


def test_mmdsl::text_constructor_exists():
    assert callable(mMDSL::Text.__init__)


def test_mmdsl::text_constructor_args():
    sig = inspect.signature(mMDSL::Text.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "fontsize" in params, "Missing parameter 'fontsize'"

def test_mmdsl::text_has_value():
    assert hasattr(mMDSL::Text, "value")
    descriptor = None
    for klass in mMDSL::Text.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::text_has_y():
    assert hasattr(mMDSL::Text, "y")
    descriptor = None
    for klass in mMDSL::Text.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::text_has_x():
    assert hasattr(mMDSL::Text, "x")
    descriptor = None
    for klass in mMDSL::Text.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mmdsl::text_has_fontsize():
    assert hasattr(mMDSL::Text, "fontsize")
    descriptor = None
    for klass in mMDSL::Text.__mro__:
        if "fontsize" in klass.__dict__:
            descriptor = klass.__dict__["fontsize"]
            break
    assert isinstance(descriptor, property)



def test_mmdsl::path_is_not_abstract():
    assert not inspect.isabstract(mMDSL::Path)


def test_mmdsl::path_constructor_exists():
    assert callable(mMDSL::Path.__init__)


def test_mmdsl::path_constructor_args():
    sig = inspect.signature(mMDSL::Path.__init__)
    params = list(sig.parameters.keys())

def test_simpletype_exists():
    # Check that the Enumeration exists
    assert SimpleType is not None

def test_simpletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SimpleType]
    expected_literals = [
        "Int",
        "Double",
        "String",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SimpleType"

def test_font_exists():
    # Check that the Enumeration exists
    assert Font is not None

def test_font_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Font]
    expected_literals = [
        "impact",
        "lucidaconsole",
        "symbol",
        "palatinolinotype",
        "msserif",
        "timesnewroman",
        "trebuchetms",
        "verdana",
        "tahoma",
        "georgia",
        "arial",
        "lucidasansunicode",
        "windings",
        "mssansserif",
        "couriernew",
        "comicsansms",
        "webdings",
        "arialblack",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Font"

def test_eventname_exists():
    # Check that the Enumeration exists
    assert EventName is not None

def test_eventname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventName]
    expected_literals = [
        "openmodel",
        "createmodel",
        "createrelationinstance",
        "discardinstance",
        "setattributevalue",
        "aftercreatemodelingnode",
        "deleteinstance",
        "aftercreatemodelingconnector",
        "savemodel",
        "deleterelationinstance",
        "beforecreaterelationinstance",
        "discardmodel",
        "beforedeletemodel",
        "createinstance",
        "beforedeleteinstance",
        "beforecreatemodel",
        "renameinstance",
        "beforediscardmodel",
        "beforesavemodel",
        "aftereditattributevalue",
        "deletemodel",
        "toolinitialized",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventName"

def test_accesstype_exists():
    # Check that the Enumeration exists
    assert AccessType is not None

def test_accesstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessType]
    expected_literals = [
        "internal",
        "read",
        "write",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessType"

def test_attrgetparams_exists():
    # Check that the Enumeration exists
    assert AttrGetParams is not None

def test_attrgetparams_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttrGetParams]
    expected_literals = [
        "name",
        "value",
        "type",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttrGetParams"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "darkorange",
        "sandybrown",
        "indianred",
        "darkgray",
        "lemonchiffon",
        "tan",
        "darkseagreen",
        "lightyellow",
        "black",
        "mediumvioletred",
        "saddlebrown",
        "sienna",
        "silver",
        "lightskyblue",
        "wheat",
        "palegoldenrod",
        "olivedrab",
        "white",
        "blanchedalmond",
        "lightcoral",
        "turquoise",
        "floralwhite",
        "darkcyan",
        "gray",
        "bisque",
        "lightcyan",
        "dodgerblue",
        "cyan",
        "blueviolet",
        "lightmagenta",
        "mediumpurple",
        "darkslategray",
        "khaki",
        "lightslategray",
        "mediumorchid",
        "antiquewhite",
        "forestgreen",
        "darkgreen",
        "cornflowerblue",
        "azure",
        "darkslateblue",
        "dimgray",
        "darkolivegreen",
        "thistle",
        "cadetblue",
        "rosybrown",
        "beige",
        "steelblue",
        "deeppink",
        "lavenderblush",
        "darkorchid",
        "darkred",
        "magenta",
        "oldlace",
        "slateblue",
        "lightgreen",
        "firebrick",
        "mediumturquoise",
        "tomato",
        "snow",
        "lightsteelblue",
        "moccasin",
        "peachpuff",
        "mediumseagreen",
        "darkkhaki",
        "teal",
        "royalblue",
        "chartreuse",
        "linen",
        "orchid",
        "mistyrose",
        "pink",
        "gold",
        "darkviolet",
        "peru",
        "fuchsia",
        "seashell",
        "papayawhip",
        "red",
        "palegreen",
        "lawngreen",
        "hotpink",
        "palevioletred",
        "darkturquoise",
        "maroon",
        "darkmagenta",
        "yellowgreen",
        "darkblue",
        "ivory",
        "gainsboro",
        "midnightblue",
        "lightpink",
        "purple",
        "lightblue",
        "olive",
        "lightgoldenrodyellow",
        "lightsalmon",
        "navajowhite",
        "honeydew",
        "orangered",
        "lightseagreen",
        "mediumaquamarine",
        "green",
        "violet",
        "greenyellow",
        "orange",
        "brown",
        "crimson",
        "slategray",
        "goldenrod",
        "lightgray",
        "navy",
        "limegreen",
        "skyblue",
        "plum",
        "aliceblue",
        "darksalmon",
        "yellow",
        "coral",
        "deepskyblue",
        "powderblue",
        "seagreen",
        "springgreen",
        "aquamarine",
        "chocolate",
        "lime",
        "indigo",
        "salmon",
        "ghostwhite",
        "cornsilk",
        "paleturquoise",
        "burlywood",
        "darkgoldenrod",
        "mediumspringgreen",
        "lavender",
        "mintcream",
        "blue",
        "mediumblue",
        "mediumslateblue",
        "whitesmoke",
        "aqua",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"

def test_attrsetparams_exists():
    # Check that the Enumeration exists
    assert AttrSetParams is not None

def test_attrsetparams_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttrSetParams]
    expected_literals = [
        "value",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttrSetParams"

def test_buttontype_exists():
    # Check that the Enumeration exists
    assert ButtonType is not None

def test_buttontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ButtonType]
    expected_literals = [
        "ok",
        "okcancel",
        "defno",
        "defyes",
        "defretry",
        "yesno",
        "defcancel",
        "retrycancel",
        "defok",
        "yesnocancel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ButtonType"


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
mMDSL::Polygon_strategy = st.builds(
    mMDSL::Polygon,
)
mMDSL::Polyline_strategy = st.builds(
    mMDSL::Polyline,
)
mMDSL::Line_strategy = st.builds(
    mMDSL::Line,
    y2=
        safe_text,
    y1=
        safe_text,
    x2=
        safe_text,
    x1=
        safe_text
)
mMDSL::Ellipse_strategy = st.builds(
    mMDSL::Ellipse,
    ry=
        safe_text,
    cy=
        safe_text,
    rx=
        safe_text,
    cx=
        safe_text
)
mMDSL::Circle_strategy = st.builds(
    mMDSL::Circle,
    cx=
        safe_text,
    r=
        safe_text,
    cy=
        safe_text
)
mMDSL::Rectangle_strategy = st.builds(
    mMDSL::Rectangle,
    x=
        safe_text,
    y=
        safe_text,
    height=
        safe_text,
    width=
        safe_text
)
mMDSL::SVGCommand_strategy = st.builds(
    mMDSL::SVGCommand,
)
mMDSL::Mode_strategy = st.builds(
    mMDSL::Mode,
    name=
        safe_text
)
mMDSL::EnumType_strategy = st.builds(
    mMDSL::EnumType,
)
mMDSL::RefName_strategy = st.builds(
    mMDSL::RefName,
)
mMDSL::Type_strategy = st.builds(
    mMDSL::Type,
    simpletype=
        safe_text
)
mMDSL::Reference_strategy = st.builds(
    mMDSL::Reference,
    name=
        safe_text
)
mMDSL::ClassAttribute_strategy = st.builds(
    mMDSL::ClassAttribute,
    name=
        safe_text
)
mMDSL::ModelType_strategy = st.builds(
    mMDSL::ModelType,
    name=
        safe_text
)
mMDSL::Attribute_strategy = st.builds(
    mMDSL::Attribute,
    access=
        safe_text,
    name=
        safe_text
)
mMDSL::Relation_strategy = st.builds(
    mMDSL::Relation,
    name=
        safe_text
)
mMDSL::Class_strategy = st.builds(
    mMDSL::Class,
    name=
        safe_text
)
mMDSL::Event_strategy = st.builds(
    mMDSL::Event,
    name=
        safe_text
)
mMDSL::Algorithm_strategy = st.builds(
    mMDSL::Algorithm,
    name=
        safe_text
)
mMDSL::Metamodel_strategy = st.builds(
    mMDSL::Metamodel,
)
mMDSL::SymbolRelation_strategy = st.builds(
    mMDSL::SymbolRelation,
    name=
        safe_text
)
mMDSL::SymbolClass_strategy = st.builds(
    mMDSL::SymbolClass,
    name=
        safe_text
)
mMDSL::SymbolStyle_strategy = st.builds(
    mMDSL::SymbolStyle,
    fontsize=
        safe_text,
    name=
        safe_text,
    strokewidth=
        safe_text
)
mMDSL::Enumeration_strategy = st.builds(
    mMDSL::Enumeration,
    name=
        safe_text,
    enumvalues=
        safe_text
)
mMDSL::InsertEmbedCode_strategy = st.builds(
    mMDSL::InsertEmbedCode,
)
mMDSL::Method_strategy = st.builds(
    mMDSL::Method,
)
mMDSL::EmbedCode_strategy = st.builds(
    mMDSL::EmbedCode,
    name=
        safe_text,
    embeddedcode=
        safe_text
)
mMDSL::IncludeLibrary_strategy = st.builds(
    mMDSL::IncludeLibrary,
    name=
        safe_text
)
mMDSL::EmbedCodeType_strategy = st.builds(
    mMDSL::EmbedCodeType,
    name=
        safe_text
)
mMDSL::EmbedPlatformType_strategy = st.builds(
    mMDSL::EmbedPlatformType,
    name=
        safe_text
)
mMDSL::IncludeLibraryType_strategy = st.builds(
    mMDSL::IncludeLibraryType,
    name=
        safe_text
)
mMDSL::MethodName_strategy = st.builds(
    mMDSL::MethodName,
    name=
        safe_text
)
mMDSL::Root_strategy = st.builds(
    mMDSL::Root,
)
Expression_strategy = st.builds(
    Expression,
)
mMDSL::MultiplicationExpression_strategy = st.builds(
    mMDSL::MultiplicationExpression,
)
mMDSL::EqualExpression_strategy = st.builds(
    mMDSL::EqualExpression,
)
mMDSL::AdditionExpression_strategy = st.builds(
    mMDSL::AdditionExpression,
)
mMDSL::AndExpression_strategy = st.builds(
    mMDSL::AndExpression,
)
mMDSL::CompareExpression_strategy = st.builds(
    mMDSL::CompareExpression,
)
mMDSL::OrExpression_strategy = st.builds(
    mMDSL::OrExpression,
)
mMDSL::AttributeSet_strategy = st.builds(
    mMDSL::AttributeSet,
    attrsetparams=
        safe_text,
    valueRealNumber=
        safe_text,
    valueString=
        safe_text
)
mMDSL::AttributeGet_strategy = st.builds(
    mMDSL::AttributeGet,
    attrgetparams=
        safe_text
)
mMDSL::RelationInstanceGetAll_strategy = st.builds(
    mMDSL::RelationInstanceGetAll,
)
mMDSL::RelationInstanceSet_strategy = st.builds(
    mMDSL::RelationInstanceSet,
)
mMDSL::RelationInstanceGet_strategy = st.builds(
    mMDSL::RelationInstanceGet,
)
mMDSL::RelationInstanceDelete_strategy = st.builds(
    mMDSL::RelationInstanceDelete,
)
mMDSL::RelationInstanceCreate_strategy = st.builds(
    mMDSL::RelationInstanceCreate,
    name=
        safe_text
)
mMDSL::ClassInstanceGetAll_strategy = st.builds(
    mMDSL::ClassInstanceGetAll,
)
mMDSL::ClassInstanceSet_strategy = st.builds(
    mMDSL::ClassInstanceSet,
)
mMDSL::ClassInstanceGet_strategy = st.builds(
    mMDSL::ClassInstanceGet,
)
mMDSL::ClassInstanceDelete_strategy = st.builds(
    mMDSL::ClassInstanceDelete,
)
mMDSL::ClassInstanceCreate_strategy = st.builds(
    mMDSL::ClassInstanceCreate,
    name=
        safe_text
)
mMDSL::RelationInstance_strategy = st.builds(
    mMDSL::RelationInstance,
)
mMDSL::ClassInstance_strategy = st.builds(
    mMDSL::ClassInstance,
)
mMDSL::ModelIsLoaded_strategy = st.builds(
    mMDSL::ModelIsLoaded,
)
mMDSL::ModelLoad_strategy = st.builds(
    mMDSL::ModelLoad,
)
mMDSL::ModelSave_strategy = st.builds(
    mMDSL::ModelSave,
)
mMDSL::ModelDiscard_strategy = st.builds(
    mMDSL::ModelDiscard,
)
mMDSL::ModelDelete_strategy = st.builds(
    mMDSL::ModelDelete,
)
mMDSL::ModelCreate_strategy = st.builds(
    mMDSL::ModelCreate,
    name=
        safe_text
)
mMDSL::RemoveContextItem_strategy = st.builds(
    mMDSL::RemoveContextItem,
)
mMDSL::InsertContextItem_strategy = st.builds(
    mMDSL::InsertContextItem,
    context=
        safe_text,
    name=
        safe_text
)
mMDSL::RemoveMenuItem_strategy = st.builds(
    mMDSL::RemoveMenuItem,
)
mMDSL::InsertMenuItem_strategy = st.builds(
    mMDSL::InsertMenuItem,
    menu=
        safe_text,
    name=
        safe_text
)
mMDSL::ContextItem_strategy = st.builds(
    mMDSL::ContextItem,
)
mMDSL::MenuItem_strategy = st.builds(
    mMDSL::MenuItem,
)
mMDSL::ItemOperation_strategy = st.builds(
    mMDSL::ItemOperation,
)
mMDSL::ViewBox_strategy = st.builds(
    mMDSL::ViewBox,
    text=
        safe_text,
    title=
        safe_text
)
mMDSL::WarningBox_strategy = st.builds(
    mMDSL::WarningBox,
    buttontype=
        safe_text,
    title=
        safe_text,
    text=
        safe_text
)
mMDSL::ErrorBox_strategy = st.builds(
    mMDSL::ErrorBox,
    title=
        safe_text,
    buttontype=
        safe_text,
    text=
        safe_text
)
mMDSL::InfoBox_strategy = st.builds(
    mMDSL::InfoBox,
    title=
        safe_text,
    text=
        safe_text
)
mMDSL::EditBox_strategy = st.builds(
    mMDSL::EditBox,
    text=
        safe_text,
    title=
        safe_text,
    okbuttontext=
        safe_text
)
mMDSL::DirList_strategy = st.builds(
    mMDSL::DirList,
    dirname=
        safe_text
)
mMDSL::DirDelete_strategy = st.builds(
    mMDSL::DirDelete,
    dirname=
        safe_text
)
mMDSL::DirCreate_strategy = st.builds(
    mMDSL::DirCreate,
    dirname=
        safe_text
)
mMDSL::DirGetWorking_strategy = st.builds(
    mMDSL::DirGetWorking,
)
mMDSL::DirSetWorking_strategy = st.builds(
    mMDSL::DirSetWorking,
    dirname=
        safe_text
)
mMDSL::FileWrite_strategy = st.builds(
    mMDSL::FileWrite,
    append=
        safe_text,
    text=
        safe_text,
    filename=
        safe_text
)
mMDSL::FileRead_strategy = st.builds(
    mMDSL::FileRead,
    filename=
        safe_text
)
mMDSL::FileCreate_strategy = st.builds(
    mMDSL::FileCreate,
    filename=
        safe_text
)
mMDSL::FileDelete_strategy = st.builds(
    mMDSL::FileDelete,
    filename=
        safe_text
)
mMDSL::FileCopy_strategy = st.builds(
    mMDSL::FileCopy,
    dest=
        safe_text,
    src=
        safe_text
)
mMDSL::AttributeOperation_strategy = st.builds(
    mMDSL::AttributeOperation,
)
mMDSL::InstanceOperation_strategy = st.builds(
    mMDSL::InstanceOperation,
)
mMDSL::ModelOperation_strategy = st.builds(
    mMDSL::ModelOperation,
)
mMDSL::SimpleUI_strategy = st.builds(
    mMDSL::SimpleUI,
)
mMDSL::DirOperation_strategy = st.builds(
    mMDSL::DirOperation,
)
mMDSL::FileOperation_strategy = st.builds(
    mMDSL::FileOperation,
)
mMDSL::EObject_strategy = st.builds(
    mMDSL::EObject,
)
mMDSL::Expression_strategy = st.builds(
    mMDSL::Expression,
    false=
        safe_text,
    valueString=
        safe_text,
    valueRealNumber=
        safe_text,
    true=
        safe_text
)
mMDSL::OperatorOr_strategy = st.builds(
    mMDSL::OperatorOr,
    or_=
        safe_text
)
mMDSL::OperatorAnd_strategy = st.builds(
    mMDSL::OperatorAnd,
    and_=
        safe_text
)
mMDSL::OperatorEqual_strategy = st.builds(
    mMDSL::OperatorEqual,
    equal=
        safe_text,
    notequal=
        safe_text
)
mMDSL::OperatorCompare_strategy = st.builds(
    mMDSL::OperatorCompare,
    greaterequal=
        safe_text,
    lesserequal=
        safe_text,
    greater=
        safe_text,
    lesser=
        safe_text
)
mMDSL::OperatorAdd_strategy = st.builds(
    mMDSL::OperatorAdd,
    add=
        safe_text,
    subtract=
        safe_text
)
mMDSL::OperatorMultiply_strategy = st.builds(
    mMDSL::OperatorMultiply,
    multiply=
        safe_text,
    modulo=
        safe_text,
    divide=
        safe_text
)
mMDSL::OperatorUnary_strategy = st.builds(
    mMDSL::OperatorUnary,
    not_=
        safe_text
)
mMDSL::OperatorMultyAssign_strategy = st.builds(
    mMDSL::OperatorMultyAssign,
    addassign=
        safe_text,
    divassign=
        safe_text,
    multiassign=
        safe_text,
    subassign=
        safe_text
)
mMDSL::VarStatement_strategy = st.builds(
    mMDSL::VarStatement,
)
mMDSL::OperatorAssign_strategy = st.builds(
    mMDSL::OperatorAssign,
    assign=
        safe_text
)
mMDSL::BreakContinue_strategy = st.builds(
    mMDSL::BreakContinue,
    break_=
        safe_text,
    continue_=
        safe_text
)
mMDSL::ForLoop_strategy = st.builds(
    mMDSL::ForLoop,
    start=
        st.integers(),
    stop=
        st.integers(),
    interval=
        st.integers()
)
mMDSL::WhileLoop_strategy = st.builds(
    mMDSL::WhileLoop,
)
mMDSL::Expr_strategy = st.builds(
    mMDSL::Expr,
)
mMDSL::AlgorithmOperation_strategy = st.builds(
    mMDSL::AlgorithmOperation,
)
mMDSL::Variable_strategy = st.builds(
    mMDSL::Variable,
    name=
        safe_text
)
mMDSL::LoopStatement_strategy = st.builds(
    mMDSL::LoopStatement,
)
mMDSL::SelectionStatement_strategy = st.builds(
    mMDSL::SelectionStatement,
)
mMDSL::Statement_strategy = st.builds(
    mMDSL::Statement,
)
mMDSL::StrokeColor_strategy = st.builds(
    mMDSL::StrokeColor,
    color=
        safe_text,
    hexcolor=
        safe_text
)
mMDSL::PathParametersA_strategy = st.builds(
    mMDSL::PathParametersA,
    y=
        safe_text,
    rx=
        safe_text,
    x=
        safe_text,
    xaxisrot=
        safe_text,
    sweepflag=
        safe_text,
    largearcflag=
        safe_text,
    ry=
        safe_text
)
mMDSL::PathParametersQ_strategy = st.builds(
    mMDSL::PathParametersQ,
    y=
        safe_text,
    x1=
        safe_text,
    y1=
        safe_text,
    x=
        safe_text
)
mMDSL::PathParametersS_strategy = st.builds(
    mMDSL::PathParametersS,
    x=
        safe_text,
    y=
        safe_text,
    x2=
        safe_text,
    y2=
        safe_text
)
mMDSL::PathParametersC_strategy = st.builds(
    mMDSL::PathParametersC,
    x1=
        safe_text,
    y=
        safe_text,
    x=
        safe_text,
    x2=
        safe_text,
    y1=
        safe_text,
    y2=
        safe_text
)
mMDSL::PathParametersHV_strategy = st.builds(
    mMDSL::PathParametersHV,
    x=
        safe_text
)
mMDSL::PathParametersMLT_strategy = st.builds(
    mMDSL::PathParametersMLT,
    y=
        safe_text,
    x=
        safe_text
)
mMDSL::EllipticalArc_strategy = st.builds(
    mMDSL::EllipticalArc,
)
mMDSL::SmoothQuadraticBezierCurveTo_strategy = st.builds(
    mMDSL::SmoothQuadraticBezierCurveTo,
)
mMDSL::QuadraticBezierCurve_strategy = st.builds(
    mMDSL::QuadraticBezierCurve,
)
mMDSL::SmoothCurveTo_strategy = st.builds(
    mMDSL::SmoothCurveTo,
)
mMDSL::CurveTo_strategy = st.builds(
    mMDSL::CurveTo,
)
mMDSL::VerticalLineTo_strategy = st.builds(
    mMDSL::VerticalLineTo,
)
mMDSL::HorizontalLineTo_strategy = st.builds(
    mMDSL::HorizontalLineTo,
)
mMDSL::LineTo_strategy = st.builds(
    mMDSL::LineTo,
)
mMDSL::MoveTo_strategy = st.builds(
    mMDSL::MoveTo,
)
mMDSL::FillColor_strategy = st.builds(
    mMDSL::FillColor,
    hexcolor=
        safe_text,
    color=
        safe_text
)
mMDSL::FontFamily_strategy = st.builds(
    mMDSL::FontFamily,
    font=
        safe_text,
    fontstr=
        safe_text
)
mMDSL::PathData_strategy = st.builds(
    mMDSL::PathData,
    closepath=
        safe_text
)
mMDSL::Points_strategy = st.builds(
    mMDSL::Points,
    x=
        safe_text,
    y=
        safe_text
)
mMDSL::Text_strategy = st.builds(
    mMDSL::Text,
    value=
        safe_text,
    y=
        safe_text,
    x=
        safe_text,
    fontsize=
        safe_text
)
mMDSL::Path_strategy = st.builds(
    mMDSL::Path,
)

@given(instance=mMDSL::Polygon_strategy)
@settings(max_examples=50)
def test_mmdsl::polygon_instantiation(instance):
    assert isinstance(instance, mMDSL::Polygon)

@given(instance=mMDSL::Polyline_strategy)
@settings(max_examples=50)
def test_mmdsl::polyline_instantiation(instance):
    assert isinstance(instance, mMDSL::Polyline)

@given(instance=mMDSL::Line_strategy)
@settings(max_examples=50)
def test_mmdsl::line_instantiation(instance):
    assert isinstance(instance, mMDSL::Line)

@given(instance=mMDSL::Line_strategy)
def test_mmdsl::line_y2_type(instance):
    assert isinstance(instance.y2, str)


@given(instance=mMDSL::Line_strategy)
def test_mmdsl::line_y2_setter(instance):
    original = instance.y2
    instance.y2 = original
    assert instance.y2 == original

@given(instance=mMDSL::Line_strategy)
def test_mmdsl::line_y1_type(instance):
    assert isinstance(instance.y1, str)


@given(instance=mMDSL::Line_strategy)
def test_mmdsl::line_y1_setter(instance):
    original = instance.y1
    instance.y1 = original
    assert instance.y1 == original

@given(instance=mMDSL::Line_strategy)
def test_mmdsl::line_x2_type(instance):
    assert isinstance(instance.x2, str)


@given(instance=mMDSL::Line_strategy)
def test_mmdsl::line_x2_setter(instance):
    original = instance.x2
    instance.x2 = original
    assert instance.x2 == original

@given(instance=mMDSL::Line_strategy)
def test_mmdsl::line_x1_type(instance):
    assert isinstance(instance.x1, str)


@given(instance=mMDSL::Line_strategy)
def test_mmdsl::line_x1_setter(instance):
    original = instance.x1
    instance.x1 = original
    assert instance.x1 == original

@given(instance=mMDSL::Ellipse_strategy)
@settings(max_examples=50)
def test_mmdsl::ellipse_instantiation(instance):
    assert isinstance(instance, mMDSL::Ellipse)

@given(instance=mMDSL::Ellipse_strategy)
def test_mmdsl::ellipse_ry_type(instance):
    assert isinstance(instance.ry, str)


@given(instance=mMDSL::Ellipse_strategy)
def test_mmdsl::ellipse_ry_setter(instance):
    original = instance.ry
    instance.ry = original
    assert instance.ry == original

@given(instance=mMDSL::Ellipse_strategy)
def test_mmdsl::ellipse_cy_type(instance):
    assert isinstance(instance.cy, str)


@given(instance=mMDSL::Ellipse_strategy)
def test_mmdsl::ellipse_cy_setter(instance):
    original = instance.cy
    instance.cy = original
    assert instance.cy == original

@given(instance=mMDSL::Ellipse_strategy)
def test_mmdsl::ellipse_rx_type(instance):
    assert isinstance(instance.rx, str)


@given(instance=mMDSL::Ellipse_strategy)
def test_mmdsl::ellipse_rx_setter(instance):
    original = instance.rx
    instance.rx = original
    assert instance.rx == original

@given(instance=mMDSL::Ellipse_strategy)
def test_mmdsl::ellipse_cx_type(instance):
    assert isinstance(instance.cx, str)


@given(instance=mMDSL::Ellipse_strategy)
def test_mmdsl::ellipse_cx_setter(instance):
    original = instance.cx
    instance.cx = original
    assert instance.cx == original

@given(instance=mMDSL::Circle_strategy)
@settings(max_examples=50)
def test_mmdsl::circle_instantiation(instance):
    assert isinstance(instance, mMDSL::Circle)

@given(instance=mMDSL::Circle_strategy)
def test_mmdsl::circle_cx_type(instance):
    assert isinstance(instance.cx, str)


@given(instance=mMDSL::Circle_strategy)
def test_mmdsl::circle_cx_setter(instance):
    original = instance.cx
    instance.cx = original
    assert instance.cx == original

@given(instance=mMDSL::Circle_strategy)
def test_mmdsl::circle_r_type(instance):
    assert isinstance(instance.r, str)


@given(instance=mMDSL::Circle_strategy)
def test_mmdsl::circle_r_setter(instance):
    original = instance.r
    instance.r = original
    assert instance.r == original

@given(instance=mMDSL::Circle_strategy)
def test_mmdsl::circle_cy_type(instance):
    assert isinstance(instance.cy, str)


@given(instance=mMDSL::Circle_strategy)
def test_mmdsl::circle_cy_setter(instance):
    original = instance.cy
    instance.cy = original
    assert instance.cy == original

@given(instance=mMDSL::Rectangle_strategy)
@settings(max_examples=50)
def test_mmdsl::rectangle_instantiation(instance):
    assert isinstance(instance, mMDSL::Rectangle)

@given(instance=mMDSL::Rectangle_strategy)
def test_mmdsl::rectangle_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=mMDSL::Rectangle_strategy)
def test_mmdsl::rectangle_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mMDSL::Rectangle_strategy)
def test_mmdsl::rectangle_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=mMDSL::Rectangle_strategy)
def test_mmdsl::rectangle_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mMDSL::Rectangle_strategy)
def test_mmdsl::rectangle_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=mMDSL::Rectangle_strategy)
def test_mmdsl::rectangle_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=mMDSL::Rectangle_strategy)
def test_mmdsl::rectangle_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=mMDSL::Rectangle_strategy)
def test_mmdsl::rectangle_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=mMDSL::SVGCommand_strategy)
@settings(max_examples=50)
def test_mmdsl::svgcommand_instantiation(instance):
    assert isinstance(instance, mMDSL::SVGCommand)

@given(instance=mMDSL::Mode_strategy)
@settings(max_examples=50)
def test_mmdsl::mode_instantiation(instance):
    assert isinstance(instance, mMDSL::Mode)

@given(instance=mMDSL::Mode_strategy)
def test_mmdsl::mode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::Mode_strategy)
def test_mmdsl::mode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::EnumType_strategy)
@settings(max_examples=50)
def test_mmdsl::enumtype_instantiation(instance):
    assert isinstance(instance, mMDSL::EnumType)

@given(instance=mMDSL::RefName_strategy)
@settings(max_examples=50)
def test_mmdsl::refname_instantiation(instance):
    assert isinstance(instance, mMDSL::RefName)

@given(instance=mMDSL::Type_strategy)
@settings(max_examples=50)
def test_mmdsl::type_instantiation(instance):
    assert isinstance(instance, mMDSL::Type)

@given(instance=mMDSL::Type_strategy)
def test_mmdsl::type_simpletype_type(instance):
    assert isinstance(instance.simpletype, str)


@given(instance=mMDSL::Type_strategy)
def test_mmdsl::type_simpletype_setter(instance):
    original = instance.simpletype
    instance.simpletype = original
    assert instance.simpletype == original

@given(instance=mMDSL::Reference_strategy)
@settings(max_examples=50)
def test_mmdsl::reference_instantiation(instance):
    assert isinstance(instance, mMDSL::Reference)

@given(instance=mMDSL::Reference_strategy)
def test_mmdsl::reference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::Reference_strategy)
def test_mmdsl::reference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::ClassAttribute_strategy)
@settings(max_examples=50)
def test_mmdsl::classattribute_instantiation(instance):
    assert isinstance(instance, mMDSL::ClassAttribute)

@given(instance=mMDSL::ClassAttribute_strategy)
def test_mmdsl::classattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::ClassAttribute_strategy)
def test_mmdsl::classattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::ModelType_strategy)
@settings(max_examples=50)
def test_mmdsl::modeltype_instantiation(instance):
    assert isinstance(instance, mMDSL::ModelType)

@given(instance=mMDSL::ModelType_strategy)
def test_mmdsl::modeltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::ModelType_strategy)
def test_mmdsl::modeltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::Attribute_strategy)
@settings(max_examples=50)
def test_mmdsl::attribute_instantiation(instance):
    assert isinstance(instance, mMDSL::Attribute)

@given(instance=mMDSL::Attribute_strategy)
def test_mmdsl::attribute_access_type(instance):
    assert isinstance(instance.access, str)


@given(instance=mMDSL::Attribute_strategy)
def test_mmdsl::attribute_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original

@given(instance=mMDSL::Attribute_strategy)
def test_mmdsl::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::Attribute_strategy)
def test_mmdsl::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::Relation_strategy)
@settings(max_examples=50)
def test_mmdsl::relation_instantiation(instance):
    assert isinstance(instance, mMDSL::Relation)

@given(instance=mMDSL::Relation_strategy)
def test_mmdsl::relation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::Relation_strategy)
def test_mmdsl::relation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::Class_strategy)
@settings(max_examples=50)
def test_mmdsl::class_instantiation(instance):
    assert isinstance(instance, mMDSL::Class)

@given(instance=mMDSL::Class_strategy)
def test_mmdsl::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::Class_strategy)
def test_mmdsl::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::Event_strategy)
@settings(max_examples=50)
def test_mmdsl::event_instantiation(instance):
    assert isinstance(instance, mMDSL::Event)

@given(instance=mMDSL::Event_strategy)
def test_mmdsl::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::Event_strategy)
def test_mmdsl::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::Algorithm_strategy)
@settings(max_examples=50)
def test_mmdsl::algorithm_instantiation(instance):
    assert isinstance(instance, mMDSL::Algorithm)

@given(instance=mMDSL::Algorithm_strategy)
def test_mmdsl::algorithm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::Algorithm_strategy)
def test_mmdsl::algorithm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::Metamodel_strategy)
@settings(max_examples=50)
def test_mmdsl::metamodel_instantiation(instance):
    assert isinstance(instance, mMDSL::Metamodel)

@given(instance=mMDSL::SymbolRelation_strategy)
@settings(max_examples=50)
def test_mmdsl::symbolrelation_instantiation(instance):
    assert isinstance(instance, mMDSL::SymbolRelation)

@given(instance=mMDSL::SymbolRelation_strategy)
def test_mmdsl::symbolrelation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::SymbolRelation_strategy)
def test_mmdsl::symbolrelation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::SymbolClass_strategy)
@settings(max_examples=50)
def test_mmdsl::symbolclass_instantiation(instance):
    assert isinstance(instance, mMDSL::SymbolClass)

@given(instance=mMDSL::SymbolClass_strategy)
def test_mmdsl::symbolclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::SymbolClass_strategy)
def test_mmdsl::symbolclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::SymbolStyle_strategy)
@settings(max_examples=50)
def test_mmdsl::symbolstyle_instantiation(instance):
    assert isinstance(instance, mMDSL::SymbolStyle)

@given(instance=mMDSL::SymbolStyle_strategy)
def test_mmdsl::symbolstyle_fontsize_type(instance):
    assert isinstance(instance.fontsize, str)


@given(instance=mMDSL::SymbolStyle_strategy)
def test_mmdsl::symbolstyle_fontsize_setter(instance):
    original = instance.fontsize
    instance.fontsize = original
    assert instance.fontsize == original

@given(instance=mMDSL::SymbolStyle_strategy)
def test_mmdsl::symbolstyle_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::SymbolStyle_strategy)
def test_mmdsl::symbolstyle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::SymbolStyle_strategy)
def test_mmdsl::symbolstyle_strokewidth_type(instance):
    assert isinstance(instance.strokewidth, str)


@given(instance=mMDSL::SymbolStyle_strategy)
def test_mmdsl::symbolstyle_strokewidth_setter(instance):
    original = instance.strokewidth
    instance.strokewidth = original
    assert instance.strokewidth == original

@given(instance=mMDSL::Enumeration_strategy)
@settings(max_examples=50)
def test_mmdsl::enumeration_instantiation(instance):
    assert isinstance(instance, mMDSL::Enumeration)

@given(instance=mMDSL::Enumeration_strategy)
def test_mmdsl::enumeration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::Enumeration_strategy)
def test_mmdsl::enumeration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::Enumeration_strategy)
def test_mmdsl::enumeration_enumvalues_type(instance):
    assert isinstance(instance.enumvalues, str)


@given(instance=mMDSL::Enumeration_strategy)
def test_mmdsl::enumeration_enumvalues_setter(instance):
    original = instance.enumvalues
    instance.enumvalues = original
    assert instance.enumvalues == original

@given(instance=mMDSL::InsertEmbedCode_strategy)
@settings(max_examples=50)
def test_mmdsl::insertembedcode_instantiation(instance):
    assert isinstance(instance, mMDSL::InsertEmbedCode)

@given(instance=mMDSL::Method_strategy)
@settings(max_examples=50)
def test_mmdsl::method_instantiation(instance):
    assert isinstance(instance, mMDSL::Method)

@given(instance=mMDSL::EmbedCode_strategy)
@settings(max_examples=50)
def test_mmdsl::embedcode_instantiation(instance):
    assert isinstance(instance, mMDSL::EmbedCode)

@given(instance=mMDSL::EmbedCode_strategy)
def test_mmdsl::embedcode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::EmbedCode_strategy)
def test_mmdsl::embedcode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::EmbedCode_strategy)
def test_mmdsl::embedcode_embeddedcode_type(instance):
    assert isinstance(instance.embeddedcode, str)


@given(instance=mMDSL::EmbedCode_strategy)
def test_mmdsl::embedcode_embeddedcode_setter(instance):
    original = instance.embeddedcode
    instance.embeddedcode = original
    assert instance.embeddedcode == original

@given(instance=mMDSL::IncludeLibrary_strategy)
@settings(max_examples=50)
def test_mmdsl::includelibrary_instantiation(instance):
    assert isinstance(instance, mMDSL::IncludeLibrary)

@given(instance=mMDSL::IncludeLibrary_strategy)
def test_mmdsl::includelibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::IncludeLibrary_strategy)
def test_mmdsl::includelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::EmbedCodeType_strategy)
@settings(max_examples=50)
def test_mmdsl::embedcodetype_instantiation(instance):
    assert isinstance(instance, mMDSL::EmbedCodeType)

@given(instance=mMDSL::EmbedCodeType_strategy)
def test_mmdsl::embedcodetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::EmbedCodeType_strategy)
def test_mmdsl::embedcodetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::EmbedPlatformType_strategy)
@settings(max_examples=50)
def test_mmdsl::embedplatformtype_instantiation(instance):
    assert isinstance(instance, mMDSL::EmbedPlatformType)

@given(instance=mMDSL::EmbedPlatformType_strategy)
def test_mmdsl::embedplatformtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::EmbedPlatformType_strategy)
def test_mmdsl::embedplatformtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::IncludeLibraryType_strategy)
@settings(max_examples=50)
def test_mmdsl::includelibrarytype_instantiation(instance):
    assert isinstance(instance, mMDSL::IncludeLibraryType)

@given(instance=mMDSL::IncludeLibraryType_strategy)
def test_mmdsl::includelibrarytype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::IncludeLibraryType_strategy)
def test_mmdsl::includelibrarytype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::MethodName_strategy)
@settings(max_examples=50)
def test_mmdsl::methodname_instantiation(instance):
    assert isinstance(instance, mMDSL::MethodName)

@given(instance=mMDSL::MethodName_strategy)
def test_mmdsl::methodname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::MethodName_strategy)
def test_mmdsl::methodname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::Root_strategy)
@settings(max_examples=50)
def test_mmdsl::root_instantiation(instance):
    assert isinstance(instance, mMDSL::Root)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mMDSL::MultiplicationExpression_strategy)
@settings(max_examples=50)
def test_mmdsl::multiplicationexpression_instantiation(instance):
    assert isinstance(instance, mMDSL::MultiplicationExpression)

@given(instance=mMDSL::EqualExpression_strategy)
@settings(max_examples=50)
def test_mmdsl::equalexpression_instantiation(instance):
    assert isinstance(instance, mMDSL::EqualExpression)

@given(instance=mMDSL::AdditionExpression_strategy)
@settings(max_examples=50)
def test_mmdsl::additionexpression_instantiation(instance):
    assert isinstance(instance, mMDSL::AdditionExpression)

@given(instance=mMDSL::AndExpression_strategy)
@settings(max_examples=50)
def test_mmdsl::andexpression_instantiation(instance):
    assert isinstance(instance, mMDSL::AndExpression)

@given(instance=mMDSL::CompareExpression_strategy)
@settings(max_examples=50)
def test_mmdsl::compareexpression_instantiation(instance):
    assert isinstance(instance, mMDSL::CompareExpression)

@given(instance=mMDSL::OrExpression_strategy)
@settings(max_examples=50)
def test_mmdsl::orexpression_instantiation(instance):
    assert isinstance(instance, mMDSL::OrExpression)

@given(instance=mMDSL::AttributeSet_strategy)
@settings(max_examples=50)
def test_mmdsl::attributeset_instantiation(instance):
    assert isinstance(instance, mMDSL::AttributeSet)

@given(instance=mMDSL::AttributeSet_strategy)
def test_mmdsl::attributeset_attrsetparams_type(instance):
    assert isinstance(instance.attrsetparams, str)


@given(instance=mMDSL::AttributeSet_strategy)
def test_mmdsl::attributeset_attrsetparams_setter(instance):
    original = instance.attrsetparams
    instance.attrsetparams = original
    assert instance.attrsetparams == original

@given(instance=mMDSL::AttributeSet_strategy)
def test_mmdsl::attributeset_valueRealNumber_type(instance):
    assert isinstance(instance.valueRealNumber, str)


@given(instance=mMDSL::AttributeSet_strategy)
def test_mmdsl::attributeset_valueRealNumber_setter(instance):
    original = instance.valueRealNumber
    instance.valueRealNumber = original
    assert instance.valueRealNumber == original

@given(instance=mMDSL::AttributeSet_strategy)
def test_mmdsl::attributeset_valueString_type(instance):
    assert isinstance(instance.valueString, str)


@given(instance=mMDSL::AttributeSet_strategy)
def test_mmdsl::attributeset_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original

@given(instance=mMDSL::AttributeGet_strategy)
@settings(max_examples=50)
def test_mmdsl::attributeget_instantiation(instance):
    assert isinstance(instance, mMDSL::AttributeGet)

@given(instance=mMDSL::AttributeGet_strategy)
def test_mmdsl::attributeget_attrgetparams_type(instance):
    assert isinstance(instance.attrgetparams, str)


@given(instance=mMDSL::AttributeGet_strategy)
def test_mmdsl::attributeget_attrgetparams_setter(instance):
    original = instance.attrgetparams
    instance.attrgetparams = original
    assert instance.attrgetparams == original

@given(instance=mMDSL::RelationInstanceGetAll_strategy)
@settings(max_examples=50)
def test_mmdsl::relationinstancegetall_instantiation(instance):
    assert isinstance(instance, mMDSL::RelationInstanceGetAll)

@given(instance=mMDSL::RelationInstanceSet_strategy)
@settings(max_examples=50)
def test_mmdsl::relationinstanceset_instantiation(instance):
    assert isinstance(instance, mMDSL::RelationInstanceSet)

@given(instance=mMDSL::RelationInstanceGet_strategy)
@settings(max_examples=50)
def test_mmdsl::relationinstanceget_instantiation(instance):
    assert isinstance(instance, mMDSL::RelationInstanceGet)

@given(instance=mMDSL::RelationInstanceDelete_strategy)
@settings(max_examples=50)
def test_mmdsl::relationinstancedelete_instantiation(instance):
    assert isinstance(instance, mMDSL::RelationInstanceDelete)

@given(instance=mMDSL::RelationInstanceCreate_strategy)
@settings(max_examples=50)
def test_mmdsl::relationinstancecreate_instantiation(instance):
    assert isinstance(instance, mMDSL::RelationInstanceCreate)

@given(instance=mMDSL::RelationInstanceCreate_strategy)
def test_mmdsl::relationinstancecreate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::RelationInstanceCreate_strategy)
def test_mmdsl::relationinstancecreate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::ClassInstanceGetAll_strategy)
@settings(max_examples=50)
def test_mmdsl::classinstancegetall_instantiation(instance):
    assert isinstance(instance, mMDSL::ClassInstanceGetAll)

@given(instance=mMDSL::ClassInstanceSet_strategy)
@settings(max_examples=50)
def test_mmdsl::classinstanceset_instantiation(instance):
    assert isinstance(instance, mMDSL::ClassInstanceSet)

@given(instance=mMDSL::ClassInstanceGet_strategy)
@settings(max_examples=50)
def test_mmdsl::classinstanceget_instantiation(instance):
    assert isinstance(instance, mMDSL::ClassInstanceGet)

@given(instance=mMDSL::ClassInstanceDelete_strategy)
@settings(max_examples=50)
def test_mmdsl::classinstancedelete_instantiation(instance):
    assert isinstance(instance, mMDSL::ClassInstanceDelete)

@given(instance=mMDSL::ClassInstanceCreate_strategy)
@settings(max_examples=50)
def test_mmdsl::classinstancecreate_instantiation(instance):
    assert isinstance(instance, mMDSL::ClassInstanceCreate)

@given(instance=mMDSL::ClassInstanceCreate_strategy)
def test_mmdsl::classinstancecreate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::ClassInstanceCreate_strategy)
def test_mmdsl::classinstancecreate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::RelationInstance_strategy)
@settings(max_examples=50)
def test_mmdsl::relationinstance_instantiation(instance):
    assert isinstance(instance, mMDSL::RelationInstance)

@given(instance=mMDSL::ClassInstance_strategy)
@settings(max_examples=50)
def test_mmdsl::classinstance_instantiation(instance):
    assert isinstance(instance, mMDSL::ClassInstance)

@given(instance=mMDSL::ModelIsLoaded_strategy)
@settings(max_examples=50)
def test_mmdsl::modelisloaded_instantiation(instance):
    assert isinstance(instance, mMDSL::ModelIsLoaded)

@given(instance=mMDSL::ModelLoad_strategy)
@settings(max_examples=50)
def test_mmdsl::modelload_instantiation(instance):
    assert isinstance(instance, mMDSL::ModelLoad)

@given(instance=mMDSL::ModelSave_strategy)
@settings(max_examples=50)
def test_mmdsl::modelsave_instantiation(instance):
    assert isinstance(instance, mMDSL::ModelSave)

@given(instance=mMDSL::ModelDiscard_strategy)
@settings(max_examples=50)
def test_mmdsl::modeldiscard_instantiation(instance):
    assert isinstance(instance, mMDSL::ModelDiscard)

@given(instance=mMDSL::ModelDelete_strategy)
@settings(max_examples=50)
def test_mmdsl::modeldelete_instantiation(instance):
    assert isinstance(instance, mMDSL::ModelDelete)

@given(instance=mMDSL::ModelCreate_strategy)
@settings(max_examples=50)
def test_mmdsl::modelcreate_instantiation(instance):
    assert isinstance(instance, mMDSL::ModelCreate)

@given(instance=mMDSL::ModelCreate_strategy)
def test_mmdsl::modelcreate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::ModelCreate_strategy)
def test_mmdsl::modelcreate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::RemoveContextItem_strategy)
@settings(max_examples=50)
def test_mmdsl::removecontextitem_instantiation(instance):
    assert isinstance(instance, mMDSL::RemoveContextItem)

@given(instance=mMDSL::InsertContextItem_strategy)
@settings(max_examples=50)
def test_mmdsl::insertcontextitem_instantiation(instance):
    assert isinstance(instance, mMDSL::InsertContextItem)

@given(instance=mMDSL::InsertContextItem_strategy)
def test_mmdsl::insertcontextitem_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=mMDSL::InsertContextItem_strategy)
def test_mmdsl::insertcontextitem_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=mMDSL::InsertContextItem_strategy)
def test_mmdsl::insertcontextitem_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::InsertContextItem_strategy)
def test_mmdsl::insertcontextitem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::RemoveMenuItem_strategy)
@settings(max_examples=50)
def test_mmdsl::removemenuitem_instantiation(instance):
    assert isinstance(instance, mMDSL::RemoveMenuItem)

@given(instance=mMDSL::InsertMenuItem_strategy)
@settings(max_examples=50)
def test_mmdsl::insertmenuitem_instantiation(instance):
    assert isinstance(instance, mMDSL::InsertMenuItem)

@given(instance=mMDSL::InsertMenuItem_strategy)
def test_mmdsl::insertmenuitem_menu_type(instance):
    assert isinstance(instance.menu, str)


@given(instance=mMDSL::InsertMenuItem_strategy)
def test_mmdsl::insertmenuitem_menu_setter(instance):
    original = instance.menu
    instance.menu = original
    assert instance.menu == original

@given(instance=mMDSL::InsertMenuItem_strategy)
def test_mmdsl::insertmenuitem_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::InsertMenuItem_strategy)
def test_mmdsl::insertmenuitem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::ContextItem_strategy)
@settings(max_examples=50)
def test_mmdsl::contextitem_instantiation(instance):
    assert isinstance(instance, mMDSL::ContextItem)

@given(instance=mMDSL::MenuItem_strategy)
@settings(max_examples=50)
def test_mmdsl::menuitem_instantiation(instance):
    assert isinstance(instance, mMDSL::MenuItem)

@given(instance=mMDSL::ItemOperation_strategy)
@settings(max_examples=50)
def test_mmdsl::itemoperation_instantiation(instance):
    assert isinstance(instance, mMDSL::ItemOperation)

@given(instance=mMDSL::ViewBox_strategy)
@settings(max_examples=50)
def test_mmdsl::viewbox_instantiation(instance):
    assert isinstance(instance, mMDSL::ViewBox)

@given(instance=mMDSL::ViewBox_strategy)
def test_mmdsl::viewbox_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=mMDSL::ViewBox_strategy)
def test_mmdsl::viewbox_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=mMDSL::ViewBox_strategy)
def test_mmdsl::viewbox_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=mMDSL::ViewBox_strategy)
def test_mmdsl::viewbox_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=mMDSL::WarningBox_strategy)
@settings(max_examples=50)
def test_mmdsl::warningbox_instantiation(instance):
    assert isinstance(instance, mMDSL::WarningBox)

@given(instance=mMDSL::WarningBox_strategy)
def test_mmdsl::warningbox_buttontype_type(instance):
    assert isinstance(instance.buttontype, str)


@given(instance=mMDSL::WarningBox_strategy)
def test_mmdsl::warningbox_buttontype_setter(instance):
    original = instance.buttontype
    instance.buttontype = original
    assert instance.buttontype == original

@given(instance=mMDSL::WarningBox_strategy)
def test_mmdsl::warningbox_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=mMDSL::WarningBox_strategy)
def test_mmdsl::warningbox_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=mMDSL::WarningBox_strategy)
def test_mmdsl::warningbox_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=mMDSL::WarningBox_strategy)
def test_mmdsl::warningbox_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=mMDSL::ErrorBox_strategy)
@settings(max_examples=50)
def test_mmdsl::errorbox_instantiation(instance):
    assert isinstance(instance, mMDSL::ErrorBox)

@given(instance=mMDSL::ErrorBox_strategy)
def test_mmdsl::errorbox_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=mMDSL::ErrorBox_strategy)
def test_mmdsl::errorbox_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=mMDSL::ErrorBox_strategy)
def test_mmdsl::errorbox_buttontype_type(instance):
    assert isinstance(instance.buttontype, str)


@given(instance=mMDSL::ErrorBox_strategy)
def test_mmdsl::errorbox_buttontype_setter(instance):
    original = instance.buttontype
    instance.buttontype = original
    assert instance.buttontype == original

@given(instance=mMDSL::ErrorBox_strategy)
def test_mmdsl::errorbox_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=mMDSL::ErrorBox_strategy)
def test_mmdsl::errorbox_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=mMDSL::InfoBox_strategy)
@settings(max_examples=50)
def test_mmdsl::infobox_instantiation(instance):
    assert isinstance(instance, mMDSL::InfoBox)

@given(instance=mMDSL::InfoBox_strategy)
def test_mmdsl::infobox_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=mMDSL::InfoBox_strategy)
def test_mmdsl::infobox_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=mMDSL::InfoBox_strategy)
def test_mmdsl::infobox_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=mMDSL::InfoBox_strategy)
def test_mmdsl::infobox_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=mMDSL::EditBox_strategy)
@settings(max_examples=50)
def test_mmdsl::editbox_instantiation(instance):
    assert isinstance(instance, mMDSL::EditBox)

@given(instance=mMDSL::EditBox_strategy)
def test_mmdsl::editbox_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=mMDSL::EditBox_strategy)
def test_mmdsl::editbox_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=mMDSL::EditBox_strategy)
def test_mmdsl::editbox_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=mMDSL::EditBox_strategy)
def test_mmdsl::editbox_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=mMDSL::EditBox_strategy)
def test_mmdsl::editbox_okbuttontext_type(instance):
    assert isinstance(instance.okbuttontext, str)


@given(instance=mMDSL::EditBox_strategy)
def test_mmdsl::editbox_okbuttontext_setter(instance):
    original = instance.okbuttontext
    instance.okbuttontext = original
    assert instance.okbuttontext == original

@given(instance=mMDSL::DirList_strategy)
@settings(max_examples=50)
def test_mmdsl::dirlist_instantiation(instance):
    assert isinstance(instance, mMDSL::DirList)

@given(instance=mMDSL::DirList_strategy)
def test_mmdsl::dirlist_dirname_type(instance):
    assert isinstance(instance.dirname, str)


@given(instance=mMDSL::DirList_strategy)
def test_mmdsl::dirlist_dirname_setter(instance):
    original = instance.dirname
    instance.dirname = original
    assert instance.dirname == original

@given(instance=mMDSL::DirDelete_strategy)
@settings(max_examples=50)
def test_mmdsl::dirdelete_instantiation(instance):
    assert isinstance(instance, mMDSL::DirDelete)

@given(instance=mMDSL::DirDelete_strategy)
def test_mmdsl::dirdelete_dirname_type(instance):
    assert isinstance(instance.dirname, str)


@given(instance=mMDSL::DirDelete_strategy)
def test_mmdsl::dirdelete_dirname_setter(instance):
    original = instance.dirname
    instance.dirname = original
    assert instance.dirname == original

@given(instance=mMDSL::DirCreate_strategy)
@settings(max_examples=50)
def test_mmdsl::dircreate_instantiation(instance):
    assert isinstance(instance, mMDSL::DirCreate)

@given(instance=mMDSL::DirCreate_strategy)
def test_mmdsl::dircreate_dirname_type(instance):
    assert isinstance(instance.dirname, str)


@given(instance=mMDSL::DirCreate_strategy)
def test_mmdsl::dircreate_dirname_setter(instance):
    original = instance.dirname
    instance.dirname = original
    assert instance.dirname == original

@given(instance=mMDSL::DirGetWorking_strategy)
@settings(max_examples=50)
def test_mmdsl::dirgetworking_instantiation(instance):
    assert isinstance(instance, mMDSL::DirGetWorking)

@given(instance=mMDSL::DirSetWorking_strategy)
@settings(max_examples=50)
def test_mmdsl::dirsetworking_instantiation(instance):
    assert isinstance(instance, mMDSL::DirSetWorking)

@given(instance=mMDSL::DirSetWorking_strategy)
def test_mmdsl::dirsetworking_dirname_type(instance):
    assert isinstance(instance.dirname, str)


@given(instance=mMDSL::DirSetWorking_strategy)
def test_mmdsl::dirsetworking_dirname_setter(instance):
    original = instance.dirname
    instance.dirname = original
    assert instance.dirname == original

@given(instance=mMDSL::FileWrite_strategy)
@settings(max_examples=50)
def test_mmdsl::filewrite_instantiation(instance):
    assert isinstance(instance, mMDSL::FileWrite)

@given(instance=mMDSL::FileWrite_strategy)
def test_mmdsl::filewrite_append_type(instance):
    assert isinstance(instance.append, str)


@given(instance=mMDSL::FileWrite_strategy)
def test_mmdsl::filewrite_append_setter(instance):
    original = instance.append
    instance.append = original
    assert instance.append == original

@given(instance=mMDSL::FileWrite_strategy)
def test_mmdsl::filewrite_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=mMDSL::FileWrite_strategy)
def test_mmdsl::filewrite_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=mMDSL::FileWrite_strategy)
def test_mmdsl::filewrite_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=mMDSL::FileWrite_strategy)
def test_mmdsl::filewrite_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=mMDSL::FileRead_strategy)
@settings(max_examples=50)
def test_mmdsl::fileread_instantiation(instance):
    assert isinstance(instance, mMDSL::FileRead)

@given(instance=mMDSL::FileRead_strategy)
def test_mmdsl::fileread_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=mMDSL::FileRead_strategy)
def test_mmdsl::fileread_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=mMDSL::FileCreate_strategy)
@settings(max_examples=50)
def test_mmdsl::filecreate_instantiation(instance):
    assert isinstance(instance, mMDSL::FileCreate)

@given(instance=mMDSL::FileCreate_strategy)
def test_mmdsl::filecreate_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=mMDSL::FileCreate_strategy)
def test_mmdsl::filecreate_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=mMDSL::FileDelete_strategy)
@settings(max_examples=50)
def test_mmdsl::filedelete_instantiation(instance):
    assert isinstance(instance, mMDSL::FileDelete)

@given(instance=mMDSL::FileDelete_strategy)
def test_mmdsl::filedelete_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=mMDSL::FileDelete_strategy)
def test_mmdsl::filedelete_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=mMDSL::FileCopy_strategy)
@settings(max_examples=50)
def test_mmdsl::filecopy_instantiation(instance):
    assert isinstance(instance, mMDSL::FileCopy)

@given(instance=mMDSL::FileCopy_strategy)
def test_mmdsl::filecopy_dest_type(instance):
    assert isinstance(instance.dest, str)


@given(instance=mMDSL::FileCopy_strategy)
def test_mmdsl::filecopy_dest_setter(instance):
    original = instance.dest
    instance.dest = original
    assert instance.dest == original

@given(instance=mMDSL::FileCopy_strategy)
def test_mmdsl::filecopy_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=mMDSL::FileCopy_strategy)
def test_mmdsl::filecopy_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=mMDSL::AttributeOperation_strategy)
@settings(max_examples=50)
def test_mmdsl::attributeoperation_instantiation(instance):
    assert isinstance(instance, mMDSL::AttributeOperation)

@given(instance=mMDSL::InstanceOperation_strategy)
@settings(max_examples=50)
def test_mmdsl::instanceoperation_instantiation(instance):
    assert isinstance(instance, mMDSL::InstanceOperation)

@given(instance=mMDSL::ModelOperation_strategy)
@settings(max_examples=50)
def test_mmdsl::modeloperation_instantiation(instance):
    assert isinstance(instance, mMDSL::ModelOperation)

@given(instance=mMDSL::SimpleUI_strategy)
@settings(max_examples=50)
def test_mmdsl::simpleui_instantiation(instance):
    assert isinstance(instance, mMDSL::SimpleUI)

@given(instance=mMDSL::DirOperation_strategy)
@settings(max_examples=50)
def test_mmdsl::diroperation_instantiation(instance):
    assert isinstance(instance, mMDSL::DirOperation)

@given(instance=mMDSL::FileOperation_strategy)
@settings(max_examples=50)
def test_mmdsl::fileoperation_instantiation(instance):
    assert isinstance(instance, mMDSL::FileOperation)

@given(instance=mMDSL::EObject_strategy)
@settings(max_examples=50)
def test_mmdsl::eobject_instantiation(instance):
    assert isinstance(instance, mMDSL::EObject)

@given(instance=mMDSL::Expression_strategy)
@settings(max_examples=50)
def test_mmdsl::expression_instantiation(instance):
    assert isinstance(instance, mMDSL::Expression)

@given(instance=mMDSL::Expression_strategy)
def test_mmdsl::expression_false_type(instance):
    assert isinstance(instance.false, str)


@given(instance=mMDSL::Expression_strategy)
def test_mmdsl::expression_false_setter(instance):
    original = instance.false
    instance.false = original
    assert instance.false == original

@given(instance=mMDSL::Expression_strategy)
def test_mmdsl::expression_valueString_type(instance):
    assert isinstance(instance.valueString, str)


@given(instance=mMDSL::Expression_strategy)
def test_mmdsl::expression_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original

@given(instance=mMDSL::Expression_strategy)
def test_mmdsl::expression_valueRealNumber_type(instance):
    assert isinstance(instance.valueRealNumber, str)


@given(instance=mMDSL::Expression_strategy)
def test_mmdsl::expression_valueRealNumber_setter(instance):
    original = instance.valueRealNumber
    instance.valueRealNumber = original
    assert instance.valueRealNumber == original

@given(instance=mMDSL::Expression_strategy)
def test_mmdsl::expression_true_type(instance):
    assert isinstance(instance.true, str)


@given(instance=mMDSL::Expression_strategy)
def test_mmdsl::expression_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original

@given(instance=mMDSL::OperatorOr_strategy)
@settings(max_examples=50)
def test_mmdsl::operatoror_instantiation(instance):
    assert isinstance(instance, mMDSL::OperatorOr)

@given(instance=mMDSL::OperatorOr_strategy)
def test_mmdsl::operatoror_or__type(instance):
    assert isinstance(instance.or_, str)


@given(instance=mMDSL::OperatorOr_strategy)
def test_mmdsl::operatoror_or__setter(instance):
    original = instance.or_
    instance.or_ = original
    assert instance.or_ == original

@given(instance=mMDSL::OperatorAnd_strategy)
@settings(max_examples=50)
def test_mmdsl::operatorand_instantiation(instance):
    assert isinstance(instance, mMDSL::OperatorAnd)

@given(instance=mMDSL::OperatorAnd_strategy)
def test_mmdsl::operatorand_and__type(instance):
    assert isinstance(instance.and_, str)


@given(instance=mMDSL::OperatorAnd_strategy)
def test_mmdsl::operatorand_and__setter(instance):
    original = instance.and_
    instance.and_ = original
    assert instance.and_ == original

@given(instance=mMDSL::OperatorEqual_strategy)
@settings(max_examples=50)
def test_mmdsl::operatorequal_instantiation(instance):
    assert isinstance(instance, mMDSL::OperatorEqual)

@given(instance=mMDSL::OperatorEqual_strategy)
def test_mmdsl::operatorequal_equal_type(instance):
    assert isinstance(instance.equal, str)


@given(instance=mMDSL::OperatorEqual_strategy)
def test_mmdsl::operatorequal_equal_setter(instance):
    original = instance.equal
    instance.equal = original
    assert instance.equal == original

@given(instance=mMDSL::OperatorEqual_strategy)
def test_mmdsl::operatorequal_notequal_type(instance):
    assert isinstance(instance.notequal, str)


@given(instance=mMDSL::OperatorEqual_strategy)
def test_mmdsl::operatorequal_notequal_setter(instance):
    original = instance.notequal
    instance.notequal = original
    assert instance.notequal == original

@given(instance=mMDSL::OperatorCompare_strategy)
@settings(max_examples=50)
def test_mmdsl::operatorcompare_instantiation(instance):
    assert isinstance(instance, mMDSL::OperatorCompare)

@given(instance=mMDSL::OperatorCompare_strategy)
def test_mmdsl::operatorcompare_greaterequal_type(instance):
    assert isinstance(instance.greaterequal, str)


@given(instance=mMDSL::OperatorCompare_strategy)
def test_mmdsl::operatorcompare_greaterequal_setter(instance):
    original = instance.greaterequal
    instance.greaterequal = original
    assert instance.greaterequal == original

@given(instance=mMDSL::OperatorCompare_strategy)
def test_mmdsl::operatorcompare_lesserequal_type(instance):
    assert isinstance(instance.lesserequal, str)


@given(instance=mMDSL::OperatorCompare_strategy)
def test_mmdsl::operatorcompare_lesserequal_setter(instance):
    original = instance.lesserequal
    instance.lesserequal = original
    assert instance.lesserequal == original

@given(instance=mMDSL::OperatorCompare_strategy)
def test_mmdsl::operatorcompare_greater_type(instance):
    assert isinstance(instance.greater, str)


@given(instance=mMDSL::OperatorCompare_strategy)
def test_mmdsl::operatorcompare_greater_setter(instance):
    original = instance.greater
    instance.greater = original
    assert instance.greater == original

@given(instance=mMDSL::OperatorCompare_strategy)
def test_mmdsl::operatorcompare_lesser_type(instance):
    assert isinstance(instance.lesser, str)


@given(instance=mMDSL::OperatorCompare_strategy)
def test_mmdsl::operatorcompare_lesser_setter(instance):
    original = instance.lesser
    instance.lesser = original
    assert instance.lesser == original

@given(instance=mMDSL::OperatorAdd_strategy)
@settings(max_examples=50)
def test_mmdsl::operatoradd_instantiation(instance):
    assert isinstance(instance, mMDSL::OperatorAdd)

@given(instance=mMDSL::OperatorAdd_strategy)
def test_mmdsl::operatoradd_add_type(instance):
    assert isinstance(instance.add, str)


@given(instance=mMDSL::OperatorAdd_strategy)
def test_mmdsl::operatoradd_add_setter(instance):
    original = instance.add
    instance.add = original
    assert instance.add == original

@given(instance=mMDSL::OperatorAdd_strategy)
def test_mmdsl::operatoradd_subtract_type(instance):
    assert isinstance(instance.subtract, str)


@given(instance=mMDSL::OperatorAdd_strategy)
def test_mmdsl::operatoradd_subtract_setter(instance):
    original = instance.subtract
    instance.subtract = original
    assert instance.subtract == original

@given(instance=mMDSL::OperatorMultiply_strategy)
@settings(max_examples=50)
def test_mmdsl::operatormultiply_instantiation(instance):
    assert isinstance(instance, mMDSL::OperatorMultiply)

@given(instance=mMDSL::OperatorMultiply_strategy)
def test_mmdsl::operatormultiply_multiply_type(instance):
    assert isinstance(instance.multiply, str)


@given(instance=mMDSL::OperatorMultiply_strategy)
def test_mmdsl::operatormultiply_multiply_setter(instance):
    original = instance.multiply
    instance.multiply = original
    assert instance.multiply == original

@given(instance=mMDSL::OperatorMultiply_strategy)
def test_mmdsl::operatormultiply_modulo_type(instance):
    assert isinstance(instance.modulo, str)


@given(instance=mMDSL::OperatorMultiply_strategy)
def test_mmdsl::operatormultiply_modulo_setter(instance):
    original = instance.modulo
    instance.modulo = original
    assert instance.modulo == original

@given(instance=mMDSL::OperatorMultiply_strategy)
def test_mmdsl::operatormultiply_divide_type(instance):
    assert isinstance(instance.divide, str)


@given(instance=mMDSL::OperatorMultiply_strategy)
def test_mmdsl::operatormultiply_divide_setter(instance):
    original = instance.divide
    instance.divide = original
    assert instance.divide == original

@given(instance=mMDSL::OperatorUnary_strategy)
@settings(max_examples=50)
def test_mmdsl::operatorunary_instantiation(instance):
    assert isinstance(instance, mMDSL::OperatorUnary)

@given(instance=mMDSL::OperatorUnary_strategy)
def test_mmdsl::operatorunary_not__type(instance):
    assert isinstance(instance.not_, str)


@given(instance=mMDSL::OperatorUnary_strategy)
def test_mmdsl::operatorunary_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=mMDSL::OperatorMultyAssign_strategy)
@settings(max_examples=50)
def test_mmdsl::operatormultyassign_instantiation(instance):
    assert isinstance(instance, mMDSL::OperatorMultyAssign)

@given(instance=mMDSL::OperatorMultyAssign_strategy)
def test_mmdsl::operatormultyassign_addassign_type(instance):
    assert isinstance(instance.addassign, str)


@given(instance=mMDSL::OperatorMultyAssign_strategy)
def test_mmdsl::operatormultyassign_addassign_setter(instance):
    original = instance.addassign
    instance.addassign = original
    assert instance.addassign == original

@given(instance=mMDSL::OperatorMultyAssign_strategy)
def test_mmdsl::operatormultyassign_divassign_type(instance):
    assert isinstance(instance.divassign, str)


@given(instance=mMDSL::OperatorMultyAssign_strategy)
def test_mmdsl::operatormultyassign_divassign_setter(instance):
    original = instance.divassign
    instance.divassign = original
    assert instance.divassign == original

@given(instance=mMDSL::OperatorMultyAssign_strategy)
def test_mmdsl::operatormultyassign_multiassign_type(instance):
    assert isinstance(instance.multiassign, str)


@given(instance=mMDSL::OperatorMultyAssign_strategy)
def test_mmdsl::operatormultyassign_multiassign_setter(instance):
    original = instance.multiassign
    instance.multiassign = original
    assert instance.multiassign == original

@given(instance=mMDSL::OperatorMultyAssign_strategy)
def test_mmdsl::operatormultyassign_subassign_type(instance):
    assert isinstance(instance.subassign, str)


@given(instance=mMDSL::OperatorMultyAssign_strategy)
def test_mmdsl::operatormultyassign_subassign_setter(instance):
    original = instance.subassign
    instance.subassign = original
    assert instance.subassign == original

@given(instance=mMDSL::VarStatement_strategy)
@settings(max_examples=50)
def test_mmdsl::varstatement_instantiation(instance):
    assert isinstance(instance, mMDSL::VarStatement)

@given(instance=mMDSL::OperatorAssign_strategy)
@settings(max_examples=50)
def test_mmdsl::operatorassign_instantiation(instance):
    assert isinstance(instance, mMDSL::OperatorAssign)

@given(instance=mMDSL::OperatorAssign_strategy)
def test_mmdsl::operatorassign_assign_type(instance):
    assert isinstance(instance.assign, str)


@given(instance=mMDSL::OperatorAssign_strategy)
def test_mmdsl::operatorassign_assign_setter(instance):
    original = instance.assign
    instance.assign = original
    assert instance.assign == original

@given(instance=mMDSL::BreakContinue_strategy)
@settings(max_examples=50)
def test_mmdsl::breakcontinue_instantiation(instance):
    assert isinstance(instance, mMDSL::BreakContinue)

@given(instance=mMDSL::BreakContinue_strategy)
def test_mmdsl::breakcontinue_break__type(instance):
    assert isinstance(instance.break_, str)


@given(instance=mMDSL::BreakContinue_strategy)
def test_mmdsl::breakcontinue_break__setter(instance):
    original = instance.break_
    instance.break_ = original
    assert instance.break_ == original

@given(instance=mMDSL::BreakContinue_strategy)
def test_mmdsl::breakcontinue_continue__type(instance):
    assert isinstance(instance.continue_, str)


@given(instance=mMDSL::BreakContinue_strategy)
def test_mmdsl::breakcontinue_continue__setter(instance):
    original = instance.continue_
    instance.continue_ = original
    assert instance.continue_ == original

@given(instance=mMDSL::ForLoop_strategy)
@settings(max_examples=50)
def test_mmdsl::forloop_instantiation(instance):
    assert isinstance(instance, mMDSL::ForLoop)

@given(instance=mMDSL::ForLoop_strategy)
def test_mmdsl::forloop_start_type(instance):
    assert isinstance(instance.start, int)


@given(instance=mMDSL::ForLoop_strategy)
def test_mmdsl::forloop_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=mMDSL::ForLoop_strategy)
def test_mmdsl::forloop_stop_type(instance):
    assert isinstance(instance.stop, int)


@given(instance=mMDSL::ForLoop_strategy)
def test_mmdsl::forloop_stop_setter(instance):
    original = instance.stop
    instance.stop = original
    assert instance.stop == original

@given(instance=mMDSL::ForLoop_strategy)
def test_mmdsl::forloop_interval_type(instance):
    assert isinstance(instance.interval, int)


@given(instance=mMDSL::ForLoop_strategy)
def test_mmdsl::forloop_interval_setter(instance):
    original = instance.interval
    instance.interval = original
    assert instance.interval == original

@given(instance=mMDSL::WhileLoop_strategy)
@settings(max_examples=50)
def test_mmdsl::whileloop_instantiation(instance):
    assert isinstance(instance, mMDSL::WhileLoop)

@given(instance=mMDSL::Expr_strategy)
@settings(max_examples=50)
def test_mmdsl::expr_instantiation(instance):
    assert isinstance(instance, mMDSL::Expr)

@given(instance=mMDSL::AlgorithmOperation_strategy)
@settings(max_examples=50)
def test_mmdsl::algorithmoperation_instantiation(instance):
    assert isinstance(instance, mMDSL::AlgorithmOperation)

@given(instance=mMDSL::Variable_strategy)
@settings(max_examples=50)
def test_mmdsl::variable_instantiation(instance):
    assert isinstance(instance, mMDSL::Variable)

@given(instance=mMDSL::Variable_strategy)
def test_mmdsl::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mMDSL::Variable_strategy)
def test_mmdsl::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mMDSL::LoopStatement_strategy)
@settings(max_examples=50)
def test_mmdsl::loopstatement_instantiation(instance):
    assert isinstance(instance, mMDSL::LoopStatement)

@given(instance=mMDSL::SelectionStatement_strategy)
@settings(max_examples=50)
def test_mmdsl::selectionstatement_instantiation(instance):
    assert isinstance(instance, mMDSL::SelectionStatement)

@given(instance=mMDSL::Statement_strategy)
@settings(max_examples=50)
def test_mmdsl::statement_instantiation(instance):
    assert isinstance(instance, mMDSL::Statement)

@given(instance=mMDSL::StrokeColor_strategy)
@settings(max_examples=50)
def test_mmdsl::strokecolor_instantiation(instance):
    assert isinstance(instance, mMDSL::StrokeColor)

@given(instance=mMDSL::StrokeColor_strategy)
def test_mmdsl::strokecolor_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=mMDSL::StrokeColor_strategy)
def test_mmdsl::strokecolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=mMDSL::StrokeColor_strategy)
def test_mmdsl::strokecolor_hexcolor_type(instance):
    assert isinstance(instance.hexcolor, str)


@given(instance=mMDSL::StrokeColor_strategy)
def test_mmdsl::strokecolor_hexcolor_setter(instance):
    original = instance.hexcolor
    instance.hexcolor = original
    assert instance.hexcolor == original

@given(instance=mMDSL::PathParametersA_strategy)
@settings(max_examples=50)
def test_mmdsl::pathparametersa_instantiation(instance):
    assert isinstance(instance, mMDSL::PathParametersA)

@given(instance=mMDSL::PathParametersA_strategy)
def test_mmdsl::pathparametersa_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=mMDSL::PathParametersA_strategy)
def test_mmdsl::pathparametersa_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mMDSL::PathParametersA_strategy)
def test_mmdsl::pathparametersa_rx_type(instance):
    assert isinstance(instance.rx, str)


@given(instance=mMDSL::PathParametersA_strategy)
def test_mmdsl::pathparametersa_rx_setter(instance):
    original = instance.rx
    instance.rx = original
    assert instance.rx == original

@given(instance=mMDSL::PathParametersA_strategy)
def test_mmdsl::pathparametersa_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=mMDSL::PathParametersA_strategy)
def test_mmdsl::pathparametersa_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mMDSL::PathParametersA_strategy)
def test_mmdsl::pathparametersa_xaxisrot_type(instance):
    assert isinstance(instance.xaxisrot, str)


@given(instance=mMDSL::PathParametersA_strategy)
def test_mmdsl::pathparametersa_xaxisrot_setter(instance):
    original = instance.xaxisrot
    instance.xaxisrot = original
    assert instance.xaxisrot == original

@given(instance=mMDSL::PathParametersA_strategy)
def test_mmdsl::pathparametersa_sweepflag_type(instance):
    assert isinstance(instance.sweepflag, str)


@given(instance=mMDSL::PathParametersA_strategy)
def test_mmdsl::pathparametersa_sweepflag_setter(instance):
    original = instance.sweepflag
    instance.sweepflag = original
    assert instance.sweepflag == original

@given(instance=mMDSL::PathParametersA_strategy)
def test_mmdsl::pathparametersa_largearcflag_type(instance):
    assert isinstance(instance.largearcflag, str)


@given(instance=mMDSL::PathParametersA_strategy)
def test_mmdsl::pathparametersa_largearcflag_setter(instance):
    original = instance.largearcflag
    instance.largearcflag = original
    assert instance.largearcflag == original

@given(instance=mMDSL::PathParametersA_strategy)
def test_mmdsl::pathparametersa_ry_type(instance):
    assert isinstance(instance.ry, str)


@given(instance=mMDSL::PathParametersA_strategy)
def test_mmdsl::pathparametersa_ry_setter(instance):
    original = instance.ry
    instance.ry = original
    assert instance.ry == original

@given(instance=mMDSL::PathParametersQ_strategy)
@settings(max_examples=50)
def test_mmdsl::pathparametersq_instantiation(instance):
    assert isinstance(instance, mMDSL::PathParametersQ)

@given(instance=mMDSL::PathParametersQ_strategy)
def test_mmdsl::pathparametersq_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=mMDSL::PathParametersQ_strategy)
def test_mmdsl::pathparametersq_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mMDSL::PathParametersQ_strategy)
def test_mmdsl::pathparametersq_x1_type(instance):
    assert isinstance(instance.x1, str)


@given(instance=mMDSL::PathParametersQ_strategy)
def test_mmdsl::pathparametersq_x1_setter(instance):
    original = instance.x1
    instance.x1 = original
    assert instance.x1 == original

@given(instance=mMDSL::PathParametersQ_strategy)
def test_mmdsl::pathparametersq_y1_type(instance):
    assert isinstance(instance.y1, str)


@given(instance=mMDSL::PathParametersQ_strategy)
def test_mmdsl::pathparametersq_y1_setter(instance):
    original = instance.y1
    instance.y1 = original
    assert instance.y1 == original

@given(instance=mMDSL::PathParametersQ_strategy)
def test_mmdsl::pathparametersq_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=mMDSL::PathParametersQ_strategy)
def test_mmdsl::pathparametersq_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mMDSL::PathParametersS_strategy)
@settings(max_examples=50)
def test_mmdsl::pathparameterss_instantiation(instance):
    assert isinstance(instance, mMDSL::PathParametersS)

@given(instance=mMDSL::PathParametersS_strategy)
def test_mmdsl::pathparameterss_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=mMDSL::PathParametersS_strategy)
def test_mmdsl::pathparameterss_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mMDSL::PathParametersS_strategy)
def test_mmdsl::pathparameterss_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=mMDSL::PathParametersS_strategy)
def test_mmdsl::pathparameterss_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mMDSL::PathParametersS_strategy)
def test_mmdsl::pathparameterss_x2_type(instance):
    assert isinstance(instance.x2, str)


@given(instance=mMDSL::PathParametersS_strategy)
def test_mmdsl::pathparameterss_x2_setter(instance):
    original = instance.x2
    instance.x2 = original
    assert instance.x2 == original

@given(instance=mMDSL::PathParametersS_strategy)
def test_mmdsl::pathparameterss_y2_type(instance):
    assert isinstance(instance.y2, str)


@given(instance=mMDSL::PathParametersS_strategy)
def test_mmdsl::pathparameterss_y2_setter(instance):
    original = instance.y2
    instance.y2 = original
    assert instance.y2 == original

@given(instance=mMDSL::PathParametersC_strategy)
@settings(max_examples=50)
def test_mmdsl::pathparametersc_instantiation(instance):
    assert isinstance(instance, mMDSL::PathParametersC)

@given(instance=mMDSL::PathParametersC_strategy)
def test_mmdsl::pathparametersc_x1_type(instance):
    assert isinstance(instance.x1, str)


@given(instance=mMDSL::PathParametersC_strategy)
def test_mmdsl::pathparametersc_x1_setter(instance):
    original = instance.x1
    instance.x1 = original
    assert instance.x1 == original

@given(instance=mMDSL::PathParametersC_strategy)
def test_mmdsl::pathparametersc_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=mMDSL::PathParametersC_strategy)
def test_mmdsl::pathparametersc_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mMDSL::PathParametersC_strategy)
def test_mmdsl::pathparametersc_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=mMDSL::PathParametersC_strategy)
def test_mmdsl::pathparametersc_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mMDSL::PathParametersC_strategy)
def test_mmdsl::pathparametersc_x2_type(instance):
    assert isinstance(instance.x2, str)


@given(instance=mMDSL::PathParametersC_strategy)
def test_mmdsl::pathparametersc_x2_setter(instance):
    original = instance.x2
    instance.x2 = original
    assert instance.x2 == original

@given(instance=mMDSL::PathParametersC_strategy)
def test_mmdsl::pathparametersc_y1_type(instance):
    assert isinstance(instance.y1, str)


@given(instance=mMDSL::PathParametersC_strategy)
def test_mmdsl::pathparametersc_y1_setter(instance):
    original = instance.y1
    instance.y1 = original
    assert instance.y1 == original

@given(instance=mMDSL::PathParametersC_strategy)
def test_mmdsl::pathparametersc_y2_type(instance):
    assert isinstance(instance.y2, str)


@given(instance=mMDSL::PathParametersC_strategy)
def test_mmdsl::pathparametersc_y2_setter(instance):
    original = instance.y2
    instance.y2 = original
    assert instance.y2 == original

@given(instance=mMDSL::PathParametersHV_strategy)
@settings(max_examples=50)
def test_mmdsl::pathparametershv_instantiation(instance):
    assert isinstance(instance, mMDSL::PathParametersHV)

@given(instance=mMDSL::PathParametersHV_strategy)
def test_mmdsl::pathparametershv_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=mMDSL::PathParametersHV_strategy)
def test_mmdsl::pathparametershv_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mMDSL::PathParametersMLT_strategy)
@settings(max_examples=50)
def test_mmdsl::pathparametersmlt_instantiation(instance):
    assert isinstance(instance, mMDSL::PathParametersMLT)

@given(instance=mMDSL::PathParametersMLT_strategy)
def test_mmdsl::pathparametersmlt_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=mMDSL::PathParametersMLT_strategy)
def test_mmdsl::pathparametersmlt_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mMDSL::PathParametersMLT_strategy)
def test_mmdsl::pathparametersmlt_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=mMDSL::PathParametersMLT_strategy)
def test_mmdsl::pathparametersmlt_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mMDSL::EllipticalArc_strategy)
@settings(max_examples=50)
def test_mmdsl::ellipticalarc_instantiation(instance):
    assert isinstance(instance, mMDSL::EllipticalArc)

@given(instance=mMDSL::SmoothQuadraticBezierCurveTo_strategy)
@settings(max_examples=50)
def test_mmdsl::smoothquadraticbeziercurveto_instantiation(instance):
    assert isinstance(instance, mMDSL::SmoothQuadraticBezierCurveTo)

@given(instance=mMDSL::QuadraticBezierCurve_strategy)
@settings(max_examples=50)
def test_mmdsl::quadraticbeziercurve_instantiation(instance):
    assert isinstance(instance, mMDSL::QuadraticBezierCurve)

@given(instance=mMDSL::SmoothCurveTo_strategy)
@settings(max_examples=50)
def test_mmdsl::smoothcurveto_instantiation(instance):
    assert isinstance(instance, mMDSL::SmoothCurveTo)

@given(instance=mMDSL::CurveTo_strategy)
@settings(max_examples=50)
def test_mmdsl::curveto_instantiation(instance):
    assert isinstance(instance, mMDSL::CurveTo)

@given(instance=mMDSL::VerticalLineTo_strategy)
@settings(max_examples=50)
def test_mmdsl::verticallineto_instantiation(instance):
    assert isinstance(instance, mMDSL::VerticalLineTo)

@given(instance=mMDSL::HorizontalLineTo_strategy)
@settings(max_examples=50)
def test_mmdsl::horizontallineto_instantiation(instance):
    assert isinstance(instance, mMDSL::HorizontalLineTo)

@given(instance=mMDSL::LineTo_strategy)
@settings(max_examples=50)
def test_mmdsl::lineto_instantiation(instance):
    assert isinstance(instance, mMDSL::LineTo)

@given(instance=mMDSL::MoveTo_strategy)
@settings(max_examples=50)
def test_mmdsl::moveto_instantiation(instance):
    assert isinstance(instance, mMDSL::MoveTo)

@given(instance=mMDSL::FillColor_strategy)
@settings(max_examples=50)
def test_mmdsl::fillcolor_instantiation(instance):
    assert isinstance(instance, mMDSL::FillColor)

@given(instance=mMDSL::FillColor_strategy)
def test_mmdsl::fillcolor_hexcolor_type(instance):
    assert isinstance(instance.hexcolor, str)


@given(instance=mMDSL::FillColor_strategy)
def test_mmdsl::fillcolor_hexcolor_setter(instance):
    original = instance.hexcolor
    instance.hexcolor = original
    assert instance.hexcolor == original

@given(instance=mMDSL::FillColor_strategy)
def test_mmdsl::fillcolor_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=mMDSL::FillColor_strategy)
def test_mmdsl::fillcolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=mMDSL::FontFamily_strategy)
@settings(max_examples=50)
def test_mmdsl::fontfamily_instantiation(instance):
    assert isinstance(instance, mMDSL::FontFamily)

@given(instance=mMDSL::FontFamily_strategy)
def test_mmdsl::fontfamily_font_type(instance):
    assert isinstance(instance.font, str)


@given(instance=mMDSL::FontFamily_strategy)
def test_mmdsl::fontfamily_font_setter(instance):
    original = instance.font
    instance.font = original
    assert instance.font == original

@given(instance=mMDSL::FontFamily_strategy)
def test_mmdsl::fontfamily_fontstr_type(instance):
    assert isinstance(instance.fontstr, str)


@given(instance=mMDSL::FontFamily_strategy)
def test_mmdsl::fontfamily_fontstr_setter(instance):
    original = instance.fontstr
    instance.fontstr = original
    assert instance.fontstr == original

@given(instance=mMDSL::PathData_strategy)
@settings(max_examples=50)
def test_mmdsl::pathdata_instantiation(instance):
    assert isinstance(instance, mMDSL::PathData)

@given(instance=mMDSL::PathData_strategy)
def test_mmdsl::pathdata_closepath_type(instance):
    assert isinstance(instance.closepath, str)


@given(instance=mMDSL::PathData_strategy)
def test_mmdsl::pathdata_closepath_setter(instance):
    original = instance.closepath
    instance.closepath = original
    assert instance.closepath == original

@given(instance=mMDSL::Points_strategy)
@settings(max_examples=50)
def test_mmdsl::points_instantiation(instance):
    assert isinstance(instance, mMDSL::Points)

@given(instance=mMDSL::Points_strategy)
def test_mmdsl::points_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=mMDSL::Points_strategy)
def test_mmdsl::points_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mMDSL::Points_strategy)
def test_mmdsl::points_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=mMDSL::Points_strategy)
def test_mmdsl::points_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mMDSL::Text_strategy)
@settings(max_examples=50)
def test_mmdsl::text_instantiation(instance):
    assert isinstance(instance, mMDSL::Text)

@given(instance=mMDSL::Text_strategy)
def test_mmdsl::text_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=mMDSL::Text_strategy)
def test_mmdsl::text_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mMDSL::Text_strategy)
def test_mmdsl::text_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=mMDSL::Text_strategy)
def test_mmdsl::text_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mMDSL::Text_strategy)
def test_mmdsl::text_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=mMDSL::Text_strategy)
def test_mmdsl::text_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mMDSL::Text_strategy)
def test_mmdsl::text_fontsize_type(instance):
    assert isinstance(instance.fontsize, str)


@given(instance=mMDSL::Text_strategy)
def test_mmdsl::text_fontsize_setter(instance):
    original = instance.fontsize
    instance.fontsize = original
    assert instance.fontsize == original

@given(instance=mMDSL::Path_strategy)
@settings(max_examples=50)
def test_mmdsl::path_instantiation(instance):
    assert isinstance(instance, mMDSL::Path)
