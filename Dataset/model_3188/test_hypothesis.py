import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    uppaal::visuals::Point,
    uppaal::visuals::LinearElement,
    Point,
    uppaal::visuals::PlanarElement,
    uppaal::visuals::ColoredElement,
    expressions::Expression,
    BinaryExpression,
    uppaal::expressions::BitShiftExpression,
    uppaal::expressions::BitwiseExpression,
    uppaal::expressions::CompareExpression,
    uppaal::expressions::ArithmeticExpression,
    uppaal::expressions::LogicalExpression,
    uppaal::expressions::MinMaxExpression,
    uppaal::expressions::AssignmentExpression,
    uppaal::expressions::Expression,
    statements::Statement,
    uppaal::templates::Synchronization,
    Selection,
    Synchronization,
    Statement,
    uppaal::statements::DoWhileLoop,
    uppaal::statements::ExpressionStatement,
    uppaal::statements::ForLoop,
    uppaal::statements::ReturnStatement,
    uppaal::statements::WhileLoop,
    uppaal::statements::IfStatement,
    uppaal::statements::EmptyStatement,
    uppaal::statements::Block,
    uppaal::statements::Statement,
    visuals::LinearElement,
    visuals::ColoredElement,
    visuals::PlanarElement,
    system::TemplateDeclaration,
    Location,
    LocalDeclarations,
    Edge,
    AbstractTemplate,
    uppaal::templates::Template,
    uppaal::templates::RedefinedTemplate,
    uppaal::system::InstantiationList,
    system::InstantiationList,
    uppaal::system::System,
    uppaal::system::ProgressMeasure,
    ChannelPriorityItem,
    uppaal::global::ChannelList,
    uppaal::global::ChannelPriorityItem,
    global::ChannelPriorityItem,
    uppaal::global::ChannelPriority,
    uppaal::declarations::Initializer,
    RedefinedTemplate,
    uppaal::global::DefaultChannelPriority,
    IdentifierExpression,
    uppaal::declarations::VariableContainer,
    uppaal::declarations::Index,
    Initializer,
    uppaal::declarations::ArrayInitializer,
    uppaal::declarations::ExpressionInitializer,
    uppaal::declarations::Parameter,
    Variable,
    Parameter,
    Block,
    Function,
    VariableContainer,
    uppaal::templates::Selection,
    DeclaredType,
    declarations::VariableContainer,
    uppaal::statements::Iteration,
    uppaal::expressions::QuantificationExpression,
    declarations::Declaration,
    uppaal::declarations::VariableDeclaration,
    uppaal::declarations::Declaration,
    system::ProgressMeasure,
    system::System,
    global::ChannelPriority,
    VariableDeclaration,
    uppaal::declarations::ClockVariableDeclaration,
    uppaal::declarations::DataVariableDeclaration,
    uppaal::declarations::ChannelVariableDeclaration,
    uppaal::types::Library,
    uppaal::types::IntegerBounds,
    IntegerBounds,
    DataVariableDeclaration,
    Declarations,
    uppaal::declarations::SystemDeclarations,
    uppaal::declarations::LocalDeclarations,
    uppaal::declarations::GlobalDeclarations,
    Declaration,
    uppaal::declarations::TypeDeclaration,
    uppaal::declarations::FunctionDeclaration,
    uppaal::system::TemplateDeclaration,
    uppaal::declarations::Declarations,
    uppaal::types::TypeDefinition,
    TypeDefinition,
    TypeDeclaration,
    Type,
    uppaal::types::DeclaredType,
    uppaal::types::PredefinedType,
    TypeSpecification,
    uppaal::types::StructTypeSpecification,
    uppaal::types::RangeTypeSpecification,
    Expression,
    uppaal::expressions::PlusExpression,
    uppaal::expressions::IncrementDecrementExpression,
    uppaal::expressions::NegationExpression,
    uppaal::expressions::ScopedIdentifierExpression,
    uppaal::expressions::MinusExpression,
    uppaal::expressions::BinaryExpression,
    uppaal::expressions::ConditionExpression,
    uppaal::expressions::FunctionCallExpression,
    uppaal::expressions::LiteralExpression,
    uppaal::expressions::IdentifierExpression,
    uppaal::types::ScalarTypeSpecification,
    uppaal::types::TypeSpecification,
    uppaal::types::TypeReference,
    uppaal::core::NamedElement,
    PredefinedType,
    Index,
    uppaal::declarations::TypeIndex,
    uppaal::declarations::ValueIndex,
    NamedElement,
    uppaal::declarations::Function,
    uppaal::declarations::Variable,
    uppaal::types::Type,
    uppaal::core::CommentableElement,
    core::CommentableElement,
    uppaal::templates::Edge,
    core::NamedElement,
    uppaal::templates::AbstractTemplate,
    uppaal::templates::Location,
    uppaal::NTA,
    SystemDeclarations,
    Template,
    GlobalDeclarations,
    CompareOperator,
    IncrementDecrementOperator,
    CallType,
    LogicalOperator,
    BitwiseOperator,
    MinMaxOperator,
    DataVariablePrefix,
    Quantifier,
    AssignmentOperator,
    BitShiftOperator,
    LocationKind,
    ArithmeticOperator,
    ColorKind,
    IncrementDecrementPosition,
    BuiltInType,
    SynchronizationKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uppaal::visuals::point_is_not_abstract():
    assert not inspect.isabstract(uppaal::visuals::Point)


def test_uppaal::visuals::point_constructor_exists():
    assert callable(uppaal::visuals::Point.__init__)


def test_uppaal::visuals::point_constructor_args():
    sig = inspect.signature(uppaal::visuals::Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_uppaal::visuals::point_has_y():
    assert hasattr(uppaal::visuals::Point, "y")
    descriptor = None
    for klass in uppaal::visuals::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::visuals::point_has_x():
    assert hasattr(uppaal::visuals::Point, "x")
    descriptor = None
    for klass in uppaal::visuals::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::visuals::linearelement_is_not_abstract():
    assert not inspect.isabstract(uppaal::visuals::LinearElement)


def test_uppaal::visuals::linearelement_constructor_exists():
    assert callable(uppaal::visuals::LinearElement.__init__)


def test_uppaal::visuals::linearelement_constructor_args():
    sig = inspect.signature(uppaal::visuals::LinearElement.__init__)
    params = list(sig.parameters.keys())



def test_point_is_not_abstract():
    assert not inspect.isabstract(Point)


def test_point_constructor_exists():
    assert callable(Point.__init__)


def test_point_constructor_args():
    sig = inspect.signature(Point.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::visuals::planarelement_is_not_abstract():
    assert not inspect.isabstract(uppaal::visuals::PlanarElement)


def test_uppaal::visuals::planarelement_constructor_exists():
    assert callable(uppaal::visuals::PlanarElement.__init__)


def test_uppaal::visuals::planarelement_constructor_args():
    sig = inspect.signature(uppaal::visuals::PlanarElement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::visuals::coloredelement_is_not_abstract():
    assert not inspect.isabstract(uppaal::visuals::ColoredElement)


def test_uppaal::visuals::coloredelement_constructor_exists():
    assert callable(uppaal::visuals::ColoredElement.__init__)


def test_uppaal::visuals::coloredelement_constructor_args():
    sig = inspect.signature(uppaal::visuals::ColoredElement.__init__)
    params = list(sig.parameters.keys())
    assert "colorCode" in params, "Missing parameter 'colorCode'"
    assert "color" in params, "Missing parameter 'color'"

def test_uppaal::visuals::coloredelement_has_colorCode():
    assert hasattr(uppaal::visuals::ColoredElement, "colorCode")
    descriptor = None
    for klass in uppaal::visuals::ColoredElement.__mro__:
        if "colorCode" in klass.__dict__:
            descriptor = klass.__dict__["colorCode"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::visuals::coloredelement_has_color():
    assert hasattr(uppaal::visuals::ColoredElement, "color")
    descriptor = None
    for klass in uppaal::visuals::ColoredElement.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_expressions::expression_is_not_abstract():
    assert not inspect.isabstract(expressions::Expression)


def test_expressions::expression_constructor_exists():
    assert callable(expressions::Expression.__init__)


def test_expressions::expression_constructor_args():
    sig = inspect.signature(expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::bitshiftexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::BitShiftExpression)


def test_uppaal::expressions::bitshiftexpression_constructor_exists():
    assert callable(uppaal::expressions::BitShiftExpression.__init__)


def test_uppaal::expressions::bitshiftexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::BitShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal::expressions::bitshiftexpression_has_operator():
    assert hasattr(uppaal::expressions::BitShiftExpression, "operator")
    descriptor = None
    for klass in uppaal::expressions::BitShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::expressions::bitwiseexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::BitwiseExpression)


def test_uppaal::expressions::bitwiseexpression_constructor_exists():
    assert callable(uppaal::expressions::BitwiseExpression.__init__)


def test_uppaal::expressions::bitwiseexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::BitwiseExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal::expressions::bitwiseexpression_has_operator():
    assert hasattr(uppaal::expressions::BitwiseExpression, "operator")
    descriptor = None
    for klass in uppaal::expressions::BitwiseExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::expressions::compareexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::CompareExpression)


def test_uppaal::expressions::compareexpression_constructor_exists():
    assert callable(uppaal::expressions::CompareExpression.__init__)


def test_uppaal::expressions::compareexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::CompareExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal::expressions::compareexpression_has_operator():
    assert hasattr(uppaal::expressions::CompareExpression, "operator")
    descriptor = None
    for klass in uppaal::expressions::CompareExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::expressions::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::ArithmeticExpression)


def test_uppaal::expressions::arithmeticexpression_constructor_exists():
    assert callable(uppaal::expressions::ArithmeticExpression.__init__)


def test_uppaal::expressions::arithmeticexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal::expressions::arithmeticexpression_has_operator():
    assert hasattr(uppaal::expressions::ArithmeticExpression, "operator")
    descriptor = None
    for klass in uppaal::expressions::ArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::expressions::logicalexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::LogicalExpression)


def test_uppaal::expressions::logicalexpression_constructor_exists():
    assert callable(uppaal::expressions::LogicalExpression.__init__)


def test_uppaal::expressions::logicalexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::LogicalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal::expressions::logicalexpression_has_operator():
    assert hasattr(uppaal::expressions::LogicalExpression, "operator")
    descriptor = None
    for klass in uppaal::expressions::LogicalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::expressions::minmaxexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::MinMaxExpression)


def test_uppaal::expressions::minmaxexpression_constructor_exists():
    assert callable(uppaal::expressions::MinMaxExpression.__init__)


def test_uppaal::expressions::minmaxexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::MinMaxExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal::expressions::minmaxexpression_has_operator():
    assert hasattr(uppaal::expressions::MinMaxExpression, "operator")
    descriptor = None
    for klass in uppaal::expressions::MinMaxExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::expressions::assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::AssignmentExpression)


def test_uppaal::expressions::assignmentexpression_constructor_exists():
    assert callable(uppaal::expressions::AssignmentExpression.__init__)


def test_uppaal::expressions::assignmentexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::AssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal::expressions::assignmentexpression_has_operator():
    assert hasattr(uppaal::expressions::AssignmentExpression, "operator")
    descriptor = None
    for klass in uppaal::expressions::AssignmentExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::expressions::expression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::Expression)


def test_uppaal::expressions::expression_constructor_exists():
    assert callable(uppaal::expressions::Expression.__init__)


def test_uppaal::expressions::expression_constructor_args():
    sig = inspect.signature(uppaal::expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statements::statement_is_not_abstract():
    assert not inspect.isabstract(statements::Statement)


def test_statements::statement_constructor_exists():
    assert callable(statements::Statement.__init__)


def test_statements::statement_constructor_args():
    sig = inspect.signature(statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::templates::synchronization_is_not_abstract():
    assert not inspect.isabstract(uppaal::templates::Synchronization)


def test_uppaal::templates::synchronization_constructor_exists():
    assert callable(uppaal::templates::Synchronization.__init__)


def test_uppaal::templates::synchronization_constructor_args():
    sig = inspect.signature(uppaal::templates::Synchronization.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uppaal::templates::synchronization_has_kind():
    assert hasattr(uppaal::templates::Synchronization, "kind")
    descriptor = None
    for klass in uppaal::templates::Synchronization.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_selection_is_not_abstract():
    assert not inspect.isabstract(Selection)


def test_selection_constructor_exists():
    assert callable(Selection.__init__)


def test_selection_constructor_args():
    sig = inspect.signature(Selection.__init__)
    params = list(sig.parameters.keys())



def test_synchronization_is_not_abstract():
    assert not inspect.isabstract(Synchronization)


def test_synchronization_constructor_exists():
    assert callable(Synchronization.__init__)


def test_synchronization_constructor_args():
    sig = inspect.signature(Synchronization.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::dowhileloop_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::DoWhileLoop)


def test_uppaal::statements::dowhileloop_constructor_exists():
    assert callable(uppaal::statements::DoWhileLoop.__init__)


def test_uppaal::statements::dowhileloop_constructor_args():
    sig = inspect.signature(uppaal::statements::DoWhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::ExpressionStatement)


def test_uppaal::statements::expressionstatement_constructor_exists():
    assert callable(uppaal::statements::ExpressionStatement.__init__)


def test_uppaal::statements::expressionstatement_constructor_args():
    sig = inspect.signature(uppaal::statements::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::forloop_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::ForLoop)


def test_uppaal::statements::forloop_constructor_exists():
    assert callable(uppaal::statements::ForLoop.__init__)


def test_uppaal::statements::forloop_constructor_args():
    sig = inspect.signature(uppaal::statements::ForLoop.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::returnstatement_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::ReturnStatement)


def test_uppaal::statements::returnstatement_constructor_exists():
    assert callable(uppaal::statements::ReturnStatement.__init__)


def test_uppaal::statements::returnstatement_constructor_args():
    sig = inspect.signature(uppaal::statements::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::whileloop_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::WhileLoop)


def test_uppaal::statements::whileloop_constructor_exists():
    assert callable(uppaal::statements::WhileLoop.__init__)


def test_uppaal::statements::whileloop_constructor_args():
    sig = inspect.signature(uppaal::statements::WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::ifstatement_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::IfStatement)


def test_uppaal::statements::ifstatement_constructor_exists():
    assert callable(uppaal::statements::IfStatement.__init__)


def test_uppaal::statements::ifstatement_constructor_args():
    sig = inspect.signature(uppaal::statements::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::emptystatement_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::EmptyStatement)


def test_uppaal::statements::emptystatement_constructor_exists():
    assert callable(uppaal::statements::EmptyStatement.__init__)


def test_uppaal::statements::emptystatement_constructor_args():
    sig = inspect.signature(uppaal::statements::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::block_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::Block)


def test_uppaal::statements::block_constructor_exists():
    assert callable(uppaal::statements::Block.__init__)


def test_uppaal::statements::block_constructor_args():
    sig = inspect.signature(uppaal::statements::Block.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::statement_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::Statement)


def test_uppaal::statements::statement_constructor_exists():
    assert callable(uppaal::statements::Statement.__init__)


def test_uppaal::statements::statement_constructor_args():
    sig = inspect.signature(uppaal::statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_visuals::linearelement_is_not_abstract():
    assert not inspect.isabstract(visuals::LinearElement)


def test_visuals::linearelement_constructor_exists():
    assert callable(visuals::LinearElement.__init__)


def test_visuals::linearelement_constructor_args():
    sig = inspect.signature(visuals::LinearElement.__init__)
    params = list(sig.parameters.keys())



def test_visuals::coloredelement_is_not_abstract():
    assert not inspect.isabstract(visuals::ColoredElement)


def test_visuals::coloredelement_constructor_exists():
    assert callable(visuals::ColoredElement.__init__)


def test_visuals::coloredelement_constructor_args():
    sig = inspect.signature(visuals::ColoredElement.__init__)
    params = list(sig.parameters.keys())



def test_visuals::planarelement_is_not_abstract():
    assert not inspect.isabstract(visuals::PlanarElement)


def test_visuals::planarelement_constructor_exists():
    assert callable(visuals::PlanarElement.__init__)


def test_visuals::planarelement_constructor_args():
    sig = inspect.signature(visuals::PlanarElement.__init__)
    params = list(sig.parameters.keys())



def test_system::templatedeclaration_is_not_abstract():
    assert not inspect.isabstract(system::TemplateDeclaration)


def test_system::templatedeclaration_constructor_exists():
    assert callable(system::TemplateDeclaration.__init__)


def test_system::templatedeclaration_constructor_args():
    sig = inspect.signature(system::TemplateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_location_constructor_exists():
    assert callable(Location.__init__)


def test_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_localdeclarations_is_not_abstract():
    assert not inspect.isabstract(LocalDeclarations)


def test_localdeclarations_constructor_exists():
    assert callable(LocalDeclarations.__init__)


def test_localdeclarations_constructor_args():
    sig = inspect.signature(LocalDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_abstracttemplate_is_not_abstract():
    assert not inspect.isabstract(AbstractTemplate)


def test_abstracttemplate_constructor_exists():
    assert callable(AbstractTemplate.__init__)


def test_abstracttemplate_constructor_args():
    sig = inspect.signature(AbstractTemplate.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::templates::template_is_not_abstract():
    assert not inspect.isabstract(uppaal::templates::Template)


def test_uppaal::templates::template_constructor_exists():
    assert callable(uppaal::templates::Template.__init__)


def test_uppaal::templates::template_constructor_args():
    sig = inspect.signature(uppaal::templates::Template.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::templates::redefinedtemplate_is_not_abstract():
    assert not inspect.isabstract(uppaal::templates::RedefinedTemplate)


def test_uppaal::templates::redefinedtemplate_constructor_exists():
    assert callable(uppaal::templates::RedefinedTemplate.__init__)


def test_uppaal::templates::redefinedtemplate_constructor_args():
    sig = inspect.signature(uppaal::templates::RedefinedTemplate.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::system::instantiationlist_is_not_abstract():
    assert not inspect.isabstract(uppaal::system::InstantiationList)


def test_uppaal::system::instantiationlist_constructor_exists():
    assert callable(uppaal::system::InstantiationList.__init__)


def test_uppaal::system::instantiationlist_constructor_args():
    sig = inspect.signature(uppaal::system::InstantiationList.__init__)
    params = list(sig.parameters.keys())



def test_system::instantiationlist_is_not_abstract():
    assert not inspect.isabstract(system::InstantiationList)


def test_system::instantiationlist_constructor_exists():
    assert callable(system::InstantiationList.__init__)


def test_system::instantiationlist_constructor_args():
    sig = inspect.signature(system::InstantiationList.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::system::system_is_not_abstract():
    assert not inspect.isabstract(uppaal::system::System)


def test_uppaal::system::system_constructor_exists():
    assert callable(uppaal::system::System.__init__)


def test_uppaal::system::system_constructor_args():
    sig = inspect.signature(uppaal::system::System.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::system::progressmeasure_is_not_abstract():
    assert not inspect.isabstract(uppaal::system::ProgressMeasure)


def test_uppaal::system::progressmeasure_constructor_exists():
    assert callable(uppaal::system::ProgressMeasure.__init__)


def test_uppaal::system::progressmeasure_constructor_args():
    sig = inspect.signature(uppaal::system::ProgressMeasure.__init__)
    params = list(sig.parameters.keys())



def test_channelpriorityitem_is_not_abstract():
    assert not inspect.isabstract(ChannelPriorityItem)


def test_channelpriorityitem_constructor_exists():
    assert callable(ChannelPriorityItem.__init__)


def test_channelpriorityitem_constructor_args():
    sig = inspect.signature(ChannelPriorityItem.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::global::channellist_is_not_abstract():
    assert not inspect.isabstract(uppaal::global::ChannelList)


def test_uppaal::global::channellist_constructor_exists():
    assert callable(uppaal::global::ChannelList.__init__)


def test_uppaal::global::channellist_constructor_args():
    sig = inspect.signature(uppaal::global::ChannelList.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::global::channelpriorityitem_is_not_abstract():
    assert not inspect.isabstract(uppaal::global::ChannelPriorityItem)


def test_uppaal::global::channelpriorityitem_constructor_exists():
    assert callable(uppaal::global::ChannelPriorityItem.__init__)


def test_uppaal::global::channelpriorityitem_constructor_args():
    sig = inspect.signature(uppaal::global::ChannelPriorityItem.__init__)
    params = list(sig.parameters.keys())



def test_global::channelpriorityitem_is_not_abstract():
    assert not inspect.isabstract(global::ChannelPriorityItem)


def test_global::channelpriorityitem_constructor_exists():
    assert callable(global::ChannelPriorityItem.__init__)


def test_global::channelpriorityitem_constructor_args():
    sig = inspect.signature(global::ChannelPriorityItem.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::global::channelpriority_is_not_abstract():
    assert not inspect.isabstract(uppaal::global::ChannelPriority)


def test_uppaal::global::channelpriority_constructor_exists():
    assert callable(uppaal::global::ChannelPriority.__init__)


def test_uppaal::global::channelpriority_constructor_args():
    sig = inspect.signature(uppaal::global::ChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::initializer_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::Initializer)


def test_uppaal::declarations::initializer_constructor_exists():
    assert callable(uppaal::declarations::Initializer.__init__)


def test_uppaal::declarations::initializer_constructor_args():
    sig = inspect.signature(uppaal::declarations::Initializer.__init__)
    params = list(sig.parameters.keys())



def test_redefinedtemplate_is_not_abstract():
    assert not inspect.isabstract(RedefinedTemplate)


def test_redefinedtemplate_constructor_exists():
    assert callable(RedefinedTemplate.__init__)


def test_redefinedtemplate_constructor_args():
    sig = inspect.signature(RedefinedTemplate.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::global::defaultchannelpriority_is_not_abstract():
    assert not inspect.isabstract(uppaal::global::DefaultChannelPriority)


def test_uppaal::global::defaultchannelpriority_constructor_exists():
    assert callable(uppaal::global::DefaultChannelPriority.__init__)


def test_uppaal::global::defaultchannelpriority_constructor_args():
    sig = inspect.signature(uppaal::global::DefaultChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_identifierexpression_is_not_abstract():
    assert not inspect.isabstract(IdentifierExpression)


def test_identifierexpression_constructor_exists():
    assert callable(IdentifierExpression.__init__)


def test_identifierexpression_constructor_args():
    sig = inspect.signature(IdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::variablecontainer_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::VariableContainer)


def test_uppaal::declarations::variablecontainer_constructor_exists():
    assert callable(uppaal::declarations::VariableContainer.__init__)


def test_uppaal::declarations::variablecontainer_constructor_args():
    sig = inspect.signature(uppaal::declarations::VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::index_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::Index)


def test_uppaal::declarations::index_constructor_exists():
    assert callable(uppaal::declarations::Index.__init__)


def test_uppaal::declarations::index_constructor_args():
    sig = inspect.signature(uppaal::declarations::Index.__init__)
    params = list(sig.parameters.keys())



def test_initializer_is_not_abstract():
    assert not inspect.isabstract(Initializer)


def test_initializer_constructor_exists():
    assert callable(Initializer.__init__)


def test_initializer_constructor_args():
    sig = inspect.signature(Initializer.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::ArrayInitializer)


def test_uppaal::declarations::arrayinitializer_constructor_exists():
    assert callable(uppaal::declarations::ArrayInitializer.__init__)


def test_uppaal::declarations::arrayinitializer_constructor_args():
    sig = inspect.signature(uppaal::declarations::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::expressioninitializer_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::ExpressionInitializer)


def test_uppaal::declarations::expressioninitializer_constructor_exists():
    assert callable(uppaal::declarations::ExpressionInitializer.__init__)


def test_uppaal::declarations::expressioninitializer_constructor_args():
    sig = inspect.signature(uppaal::declarations::ExpressionInitializer.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::parameter_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::Parameter)


def test_uppaal::declarations::parameter_constructor_exists():
    assert callable(uppaal::declarations::Parameter.__init__)


def test_uppaal::declarations::parameter_constructor_args():
    sig = inspect.signature(uppaal::declarations::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "callType" in params, "Missing parameter 'callType'"

def test_uppaal::declarations::parameter_has_callType():
    assert hasattr(uppaal::declarations::Parameter, "callType")
    descriptor = None
    for klass in uppaal::declarations::Parameter.__mro__:
        if "callType" in klass.__dict__:
            descriptor = klass.__dict__["callType"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_variablecontainer_is_not_abstract():
    assert not inspect.isabstract(VariableContainer)


def test_variablecontainer_constructor_exists():
    assert callable(VariableContainer.__init__)


def test_variablecontainer_constructor_args():
    sig = inspect.signature(VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::templates::selection_is_not_abstract():
    assert not inspect.isabstract(uppaal::templates::Selection)


def test_uppaal::templates::selection_constructor_exists():
    assert callable(uppaal::templates::Selection.__init__)


def test_uppaal::templates::selection_constructor_args():
    sig = inspect.signature(uppaal::templates::Selection.__init__)
    params = list(sig.parameters.keys())



def test_declaredtype_is_not_abstract():
    assert not inspect.isabstract(DeclaredType)


def test_declaredtype_constructor_exists():
    assert callable(DeclaredType.__init__)


def test_declaredtype_constructor_args():
    sig = inspect.signature(DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_declarations::variablecontainer_is_not_abstract():
    assert not inspect.isabstract(declarations::VariableContainer)


def test_declarations::variablecontainer_constructor_exists():
    assert callable(declarations::VariableContainer.__init__)


def test_declarations::variablecontainer_constructor_args():
    sig = inspect.signature(declarations::VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::iteration_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::Iteration)


def test_uppaal::statements::iteration_constructor_exists():
    assert callable(uppaal::statements::Iteration.__init__)


def test_uppaal::statements::iteration_constructor_args():
    sig = inspect.signature(uppaal::statements::Iteration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::quantificationexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::QuantificationExpression)


def test_uppaal::expressions::quantificationexpression_constructor_exists():
    assert callable(uppaal::expressions::QuantificationExpression.__init__)


def test_uppaal::expressions::quantificationexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::QuantificationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "quantifier" in params, "Missing parameter 'quantifier'"

def test_uppaal::expressions::quantificationexpression_has_quantifier():
    assert hasattr(uppaal::expressions::QuantificationExpression, "quantifier")
    descriptor = None
    for klass in uppaal::expressions::QuantificationExpression.__mro__:
        if "quantifier" in klass.__dict__:
            descriptor = klass.__dict__["quantifier"]
            break
    assert isinstance(descriptor, property)



def test_declarations::declaration_is_not_abstract():
    assert not inspect.isabstract(declarations::Declaration)


def test_declarations::declaration_constructor_exists():
    assert callable(declarations::Declaration.__init__)


def test_declarations::declaration_constructor_args():
    sig = inspect.signature(declarations::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::VariableDeclaration)


def test_uppaal::declarations::variabledeclaration_constructor_exists():
    assert callable(uppaal::declarations::VariableDeclaration.__init__)


def test_uppaal::declarations::variabledeclaration_constructor_args():
    sig = inspect.signature(uppaal::declarations::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::declaration_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::Declaration)


def test_uppaal::declarations::declaration_constructor_exists():
    assert callable(uppaal::declarations::Declaration.__init__)


def test_uppaal::declarations::declaration_constructor_args():
    sig = inspect.signature(uppaal::declarations::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_system::progressmeasure_is_not_abstract():
    assert not inspect.isabstract(system::ProgressMeasure)


def test_system::progressmeasure_constructor_exists():
    assert callable(system::ProgressMeasure.__init__)


def test_system::progressmeasure_constructor_args():
    sig = inspect.signature(system::ProgressMeasure.__init__)
    params = list(sig.parameters.keys())



def test_system::system_is_not_abstract():
    assert not inspect.isabstract(system::System)


def test_system::system_constructor_exists():
    assert callable(system::System.__init__)


def test_system::system_constructor_args():
    sig = inspect.signature(system::System.__init__)
    params = list(sig.parameters.keys())



def test_global::channelpriority_is_not_abstract():
    assert not inspect.isabstract(global::ChannelPriority)


def test_global::channelpriority_constructor_exists():
    assert callable(global::ChannelPriority.__init__)


def test_global::channelpriority_constructor_args():
    sig = inspect.signature(global::ChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::clockvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::ClockVariableDeclaration)


def test_uppaal::declarations::clockvariabledeclaration_constructor_exists():
    assert callable(uppaal::declarations::ClockVariableDeclaration.__init__)


def test_uppaal::declarations::clockvariabledeclaration_constructor_args():
    sig = inspect.signature(uppaal::declarations::ClockVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::datavariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::DataVariableDeclaration)


def test_uppaal::declarations::datavariabledeclaration_constructor_exists():
    assert callable(uppaal::declarations::DataVariableDeclaration.__init__)


def test_uppaal::declarations::datavariabledeclaration_constructor_args():
    sig = inspect.signature(uppaal::declarations::DataVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_uppaal::declarations::datavariabledeclaration_has_prefix():
    assert hasattr(uppaal::declarations::DataVariableDeclaration, "prefix")
    descriptor = None
    for klass in uppaal::declarations::DataVariableDeclaration.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::declarations::channelvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::ChannelVariableDeclaration)


def test_uppaal::declarations::channelvariabledeclaration_constructor_exists():
    assert callable(uppaal::declarations::ChannelVariableDeclaration.__init__)


def test_uppaal::declarations::channelvariabledeclaration_constructor_args():
    sig = inspect.signature(uppaal::declarations::ChannelVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "urgent" in params, "Missing parameter 'urgent'"
    assert "broadcast" in params, "Missing parameter 'broadcast'"

def test_uppaal::declarations::channelvariabledeclaration_has_urgent():
    assert hasattr(uppaal::declarations::ChannelVariableDeclaration, "urgent")
    descriptor = None
    for klass in uppaal::declarations::ChannelVariableDeclaration.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::declarations::channelvariabledeclaration_has_broadcast():
    assert hasattr(uppaal::declarations::ChannelVariableDeclaration, "broadcast")
    descriptor = None
    for klass in uppaal::declarations::ChannelVariableDeclaration.__mro__:
        if "broadcast" in klass.__dict__:
            descriptor = klass.__dict__["broadcast"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::types::library_is_not_abstract():
    assert not inspect.isabstract(uppaal::types::Library)


def test_uppaal::types::library_constructor_exists():
    assert callable(uppaal::types::Library.__init__)


def test_uppaal::types::library_constructor_args():
    sig = inspect.signature(uppaal::types::Library.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::types::integerbounds_is_not_abstract():
    assert not inspect.isabstract(uppaal::types::IntegerBounds)


def test_uppaal::types::integerbounds_constructor_exists():
    assert callable(uppaal::types::IntegerBounds.__init__)


def test_uppaal::types::integerbounds_constructor_args():
    sig = inspect.signature(uppaal::types::IntegerBounds.__init__)
    params = list(sig.parameters.keys())



def test_integerbounds_is_not_abstract():
    assert not inspect.isabstract(IntegerBounds)


def test_integerbounds_constructor_exists():
    assert callable(IntegerBounds.__init__)


def test_integerbounds_constructor_args():
    sig = inspect.signature(IntegerBounds.__init__)
    params = list(sig.parameters.keys())



def test_datavariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(DataVariableDeclaration)


def test_datavariabledeclaration_constructor_exists():
    assert callable(DataVariableDeclaration.__init__)


def test_datavariabledeclaration_constructor_args():
    sig = inspect.signature(DataVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_declarations_is_not_abstract():
    assert not inspect.isabstract(Declarations)


def test_declarations_constructor_exists():
    assert callable(Declarations.__init__)


def test_declarations_constructor_args():
    sig = inspect.signature(Declarations.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::systemdeclarations_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::SystemDeclarations)


def test_uppaal::declarations::systemdeclarations_constructor_exists():
    assert callable(uppaal::declarations::SystemDeclarations.__init__)


def test_uppaal::declarations::systemdeclarations_constructor_args():
    sig = inspect.signature(uppaal::declarations::SystemDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::localdeclarations_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::LocalDeclarations)


def test_uppaal::declarations::localdeclarations_constructor_exists():
    assert callable(uppaal::declarations::LocalDeclarations.__init__)


def test_uppaal::declarations::localdeclarations_constructor_args():
    sig = inspect.signature(uppaal::declarations::LocalDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::globaldeclarations_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::GlobalDeclarations)


def test_uppaal::declarations::globaldeclarations_constructor_exists():
    assert callable(uppaal::declarations::GlobalDeclarations.__init__)


def test_uppaal::declarations::globaldeclarations_constructor_args():
    sig = inspect.signature(uppaal::declarations::GlobalDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::TypeDeclaration)


def test_uppaal::declarations::typedeclaration_constructor_exists():
    assert callable(uppaal::declarations::TypeDeclaration.__init__)


def test_uppaal::declarations::typedeclaration_constructor_args():
    sig = inspect.signature(uppaal::declarations::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::FunctionDeclaration)


def test_uppaal::declarations::functiondeclaration_constructor_exists():
    assert callable(uppaal::declarations::FunctionDeclaration.__init__)


def test_uppaal::declarations::functiondeclaration_constructor_args():
    sig = inspect.signature(uppaal::declarations::FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::system::templatedeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal::system::TemplateDeclaration)


def test_uppaal::system::templatedeclaration_constructor_exists():
    assert callable(uppaal::system::TemplateDeclaration.__init__)


def test_uppaal::system::templatedeclaration_constructor_args():
    sig = inspect.signature(uppaal::system::TemplateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::declarations_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::Declarations)


def test_uppaal::declarations::declarations_constructor_exists():
    assert callable(uppaal::declarations::Declarations.__init__)


def test_uppaal::declarations::declarations_constructor_args():
    sig = inspect.signature(uppaal::declarations::Declarations.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::types::typedefinition_is_not_abstract():
    assert not inspect.isabstract(uppaal::types::TypeDefinition)


def test_uppaal::types::typedefinition_constructor_exists():
    assert callable(uppaal::types::TypeDefinition.__init__)


def test_uppaal::types::typedefinition_constructor_args():
    sig = inspect.signature(uppaal::types::TypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "baseType" in params, "Missing parameter 'baseType'"

def test_uppaal::types::typedefinition_has_baseType():
    assert hasattr(uppaal::types::TypeDefinition, "baseType")
    descriptor = None
    for klass in uppaal::types::TypeDefinition.__mro__:
        if "baseType" in klass.__dict__:
            descriptor = klass.__dict__["baseType"]
            break
    assert isinstance(descriptor, property)



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::types::declaredtype_is_not_abstract():
    assert not inspect.isabstract(uppaal::types::DeclaredType)


def test_uppaal::types::declaredtype_constructor_exists():
    assert callable(uppaal::types::DeclaredType.__init__)


def test_uppaal::types::declaredtype_constructor_args():
    sig = inspect.signature(uppaal::types::DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::types::predefinedtype_is_not_abstract():
    assert not inspect.isabstract(uppaal::types::PredefinedType)


def test_uppaal::types::predefinedtype_constructor_exists():
    assert callable(uppaal::types::PredefinedType.__init__)


def test_uppaal::types::predefinedtype_constructor_args():
    sig = inspect.signature(uppaal::types::PredefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_uppaal::types::predefinedtype_has_type():
    assert hasattr(uppaal::types::PredefinedType, "type")
    descriptor = None
    for klass in uppaal::types::PredefinedType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_typespecification_is_not_abstract():
    assert not inspect.isabstract(TypeSpecification)


def test_typespecification_constructor_exists():
    assert callable(TypeSpecification.__init__)


def test_typespecification_constructor_args():
    sig = inspect.signature(TypeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::types::structtypespecification_is_not_abstract():
    assert not inspect.isabstract(uppaal::types::StructTypeSpecification)


def test_uppaal::types::structtypespecification_constructor_exists():
    assert callable(uppaal::types::StructTypeSpecification.__init__)


def test_uppaal::types::structtypespecification_constructor_args():
    sig = inspect.signature(uppaal::types::StructTypeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::types::rangetypespecification_is_not_abstract():
    assert not inspect.isabstract(uppaal::types::RangeTypeSpecification)


def test_uppaal::types::rangetypespecification_constructor_exists():
    assert callable(uppaal::types::RangeTypeSpecification.__init__)


def test_uppaal::types::rangetypespecification_constructor_args():
    sig = inspect.signature(uppaal::types::RangeTypeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::plusexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::PlusExpression)


def test_uppaal::expressions::plusexpression_constructor_exists():
    assert callable(uppaal::expressions::PlusExpression.__init__)


def test_uppaal::expressions::plusexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::PlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::incrementdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::IncrementDecrementExpression)


def test_uppaal::expressions::incrementdecrementexpression_constructor_exists():
    assert callable(uppaal::expressions::IncrementDecrementExpression.__init__)


def test_uppaal::expressions::incrementdecrementexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::IncrementDecrementExpression.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal::expressions::incrementdecrementexpression_has_position():
    assert hasattr(uppaal::expressions::IncrementDecrementExpression, "position")
    descriptor = None
    for klass in uppaal::expressions::IncrementDecrementExpression.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::expressions::incrementdecrementexpression_has_operator():
    assert hasattr(uppaal::expressions::IncrementDecrementExpression, "operator")
    descriptor = None
    for klass in uppaal::expressions::IncrementDecrementExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::expressions::negationexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::NegationExpression)


def test_uppaal::expressions::negationexpression_constructor_exists():
    assert callable(uppaal::expressions::NegationExpression.__init__)


def test_uppaal::expressions::negationexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::NegationExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::scopedidentifierexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::ScopedIdentifierExpression)


def test_uppaal::expressions::scopedidentifierexpression_constructor_exists():
    assert callable(uppaal::expressions::ScopedIdentifierExpression.__init__)


def test_uppaal::expressions::scopedidentifierexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::ScopedIdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::minusexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::MinusExpression)


def test_uppaal::expressions::minusexpression_constructor_exists():
    assert callable(uppaal::expressions::MinusExpression.__init__)


def test_uppaal::expressions::minusexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::MinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::BinaryExpression)


def test_uppaal::expressions::binaryexpression_constructor_exists():
    assert callable(uppaal::expressions::BinaryExpression.__init__)


def test_uppaal::expressions::binaryexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::conditionexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::ConditionExpression)


def test_uppaal::expressions::conditionexpression_constructor_exists():
    assert callable(uppaal::expressions::ConditionExpression.__init__)


def test_uppaal::expressions::conditionexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::ConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::FunctionCallExpression)


def test_uppaal::expressions::functioncallexpression_constructor_exists():
    assert callable(uppaal::expressions::FunctionCallExpression.__init__)


def test_uppaal::expressions::functioncallexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::literalexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::LiteralExpression)


def test_uppaal::expressions::literalexpression_constructor_exists():
    assert callable(uppaal::expressions::LiteralExpression.__init__)


def test_uppaal::expressions::literalexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::LiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_uppaal::expressions::literalexpression_has_text():
    assert hasattr(uppaal::expressions::LiteralExpression, "text")
    descriptor = None
    for klass in uppaal::expressions::LiteralExpression.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::expressions::identifierexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::IdentifierExpression)


def test_uppaal::expressions::identifierexpression_constructor_exists():
    assert callable(uppaal::expressions::IdentifierExpression.__init__)


def test_uppaal::expressions::identifierexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::IdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::types::scalartypespecification_is_not_abstract():
    assert not inspect.isabstract(uppaal::types::ScalarTypeSpecification)


def test_uppaal::types::scalartypespecification_constructor_exists():
    assert callable(uppaal::types::ScalarTypeSpecification.__init__)


def test_uppaal::types::scalartypespecification_constructor_args():
    sig = inspect.signature(uppaal::types::ScalarTypeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::types::typespecification_is_not_abstract():
    assert not inspect.isabstract(uppaal::types::TypeSpecification)


def test_uppaal::types::typespecification_constructor_exists():
    assert callable(uppaal::types::TypeSpecification.__init__)


def test_uppaal::types::typespecification_constructor_args():
    sig = inspect.signature(uppaal::types::TypeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::types::typereference_is_not_abstract():
    assert not inspect.isabstract(uppaal::types::TypeReference)


def test_uppaal::types::typereference_constructor_exists():
    assert callable(uppaal::types::TypeReference.__init__)


def test_uppaal::types::typereference_constructor_args():
    sig = inspect.signature(uppaal::types::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::core::namedelement_is_not_abstract():
    assert not inspect.isabstract(uppaal::core::NamedElement)


def test_uppaal::core::namedelement_constructor_exists():
    assert callable(uppaal::core::NamedElement.__init__)


def test_uppaal::core::namedelement_constructor_args():
    sig = inspect.signature(uppaal::core::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uppaal::core::namedelement_has_name():
    assert hasattr(uppaal::core::NamedElement, "name")
    descriptor = None
    for klass in uppaal::core::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(PredefinedType)


def test_predefinedtype_constructor_exists():
    assert callable(PredefinedType.__init__)


def test_predefinedtype_constructor_args():
    sig = inspect.signature(PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_index_is_not_abstract():
    assert not inspect.isabstract(Index)


def test_index_constructor_exists():
    assert callable(Index.__init__)


def test_index_constructor_args():
    sig = inspect.signature(Index.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::typeindex_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::TypeIndex)


def test_uppaal::declarations::typeindex_constructor_exists():
    assert callable(uppaal::declarations::TypeIndex.__init__)


def test_uppaal::declarations::typeindex_constructor_args():
    sig = inspect.signature(uppaal::declarations::TypeIndex.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::valueindex_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::ValueIndex)


def test_uppaal::declarations::valueindex_constructor_exists():
    assert callable(uppaal::declarations::ValueIndex.__init__)


def test_uppaal::declarations::valueindex_constructor_args():
    sig = inspect.signature(uppaal::declarations::ValueIndex.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::function_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::Function)


def test_uppaal::declarations::function_constructor_exists():
    assert callable(uppaal::declarations::Function.__init__)


def test_uppaal::declarations::function_constructor_args():
    sig = inspect.signature(uppaal::declarations::Function.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::variable_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::Variable)


def test_uppaal::declarations::variable_constructor_exists():
    assert callable(uppaal::declarations::Variable.__init__)


def test_uppaal::declarations::variable_constructor_args():
    sig = inspect.signature(uppaal::declarations::Variable.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::types::type_is_not_abstract():
    assert not inspect.isabstract(uppaal::types::Type)


def test_uppaal::types::type_constructor_exists():
    assert callable(uppaal::types::Type.__init__)


def test_uppaal::types::type_constructor_args():
    sig = inspect.signature(uppaal::types::Type.__init__)
    params = list(sig.parameters.keys())
    assert "baseType" in params, "Missing parameter 'baseType'"

def test_uppaal::types::type_has_baseType():
    assert hasattr(uppaal::types::Type, "baseType")
    descriptor = None
    for klass in uppaal::types::Type.__mro__:
        if "baseType" in klass.__dict__:
            descriptor = klass.__dict__["baseType"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::core::commentableelement_is_not_abstract():
    assert not inspect.isabstract(uppaal::core::CommentableElement)


def test_uppaal::core::commentableelement_constructor_exists():
    assert callable(uppaal::core::CommentableElement.__init__)


def test_uppaal::core::commentableelement_constructor_args():
    sig = inspect.signature(uppaal::core::CommentableElement.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_uppaal::core::commentableelement_has_comment():
    assert hasattr(uppaal::core::CommentableElement, "comment")
    descriptor = None
    for klass in uppaal::core::CommentableElement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_core::commentableelement_is_not_abstract():
    assert not inspect.isabstract(core::CommentableElement)


def test_core::commentableelement_constructor_exists():
    assert callable(core::CommentableElement.__init__)


def test_core::commentableelement_constructor_args():
    sig = inspect.signature(core::CommentableElement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::templates::edge_is_not_abstract():
    assert not inspect.isabstract(uppaal::templates::Edge)


def test_uppaal::templates::edge_constructor_exists():
    assert callable(uppaal::templates::Edge.__init__)


def test_uppaal::templates::edge_constructor_args():
    sig = inspect.signature(uppaal::templates::Edge.__init__)
    params = list(sig.parameters.keys())



def test_core::namedelement_is_not_abstract():
    assert not inspect.isabstract(core::NamedElement)


def test_core::namedelement_constructor_exists():
    assert callable(core::NamedElement.__init__)


def test_core::namedelement_constructor_args():
    sig = inspect.signature(core::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::templates::abstracttemplate_is_not_abstract():
    assert not inspect.isabstract(uppaal::templates::AbstractTemplate)


def test_uppaal::templates::abstracttemplate_constructor_exists():
    assert callable(uppaal::templates::AbstractTemplate.__init__)


def test_uppaal::templates::abstracttemplate_constructor_args():
    sig = inspect.signature(uppaal::templates::AbstractTemplate.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::templates::location_is_not_abstract():
    assert not inspect.isabstract(uppaal::templates::Location)


def test_uppaal::templates::location_constructor_exists():
    assert callable(uppaal::templates::Location.__init__)


def test_uppaal::templates::location_constructor_args():
    sig = inspect.signature(uppaal::templates::Location.__init__)
    params = list(sig.parameters.keys())
    assert "locationTimeKind" in params, "Missing parameter 'locationTimeKind'"

def test_uppaal::templates::location_has_locationTimeKind():
    assert hasattr(uppaal::templates::Location, "locationTimeKind")
    descriptor = None
    for klass in uppaal::templates::Location.__mro__:
        if "locationTimeKind" in klass.__dict__:
            descriptor = klass.__dict__["locationTimeKind"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::nta_is_not_abstract():
    assert not inspect.isabstract(uppaal::NTA)


def test_uppaal::nta_constructor_exists():
    assert callable(uppaal::NTA.__init__)


def test_uppaal::nta_constructor_args():
    sig = inspect.signature(uppaal::NTA.__init__)
    params = list(sig.parameters.keys())



def test_systemdeclarations_is_not_abstract():
    assert not inspect.isabstract(SystemDeclarations)


def test_systemdeclarations_constructor_exists():
    assert callable(SystemDeclarations.__init__)


def test_systemdeclarations_constructor_args():
    sig = inspect.signature(SystemDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_template_is_not_abstract():
    assert not inspect.isabstract(Template)


def test_template_constructor_exists():
    assert callable(Template.__init__)


def test_template_constructor_args():
    sig = inspect.signature(Template.__init__)
    params = list(sig.parameters.keys())



def test_globaldeclarations_is_not_abstract():
    assert not inspect.isabstract(GlobalDeclarations)


def test_globaldeclarations_constructor_exists():
    assert callable(GlobalDeclarations.__init__)


def test_globaldeclarations_constructor_args():
    sig = inspect.signature(GlobalDeclarations.__init__)
    params = list(sig.parameters.keys())

def test_compareoperator_exists():
    # Check that the Enumeration exists
    assert CompareOperator is not None

def test_compareoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CompareOperator]
    expected_literals = [
        "LESS",
        "GREATER",
        "GREATER_OR_EQUAL",
        "EQUAL",
        "LESS_OR_EQUAL",
        "UNEQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CompareOperator"

def test_incrementdecrementoperator_exists():
    # Check that the Enumeration exists
    assert IncrementDecrementOperator is not None

def test_incrementdecrementoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IncrementDecrementOperator]
    expected_literals = [
        "INCREMENT",
        "DECREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IncrementDecrementOperator"

def test_calltype_exists():
    # Check that the Enumeration exists
    assert CallType is not None

def test_calltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallType]
    expected_literals = [
        "CALL_BY_VALUE",
        "CALL_BY_REFERENCE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallType"

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "AND",
        "IMPLY",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"

def test_bitwiseoperator_exists():
    # Check that the Enumeration exists
    assert BitwiseOperator is not None

def test_bitwiseoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BitwiseOperator]
    expected_literals = [
        "OR",
        "AND",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BitwiseOperator"

def test_minmaxoperator_exists():
    # Check that the Enumeration exists
    assert MinMaxOperator is not None

def test_minmaxoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MinMaxOperator]
    expected_literals = [
        "MIN",
        "MAX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MinMaxOperator"

def test_datavariableprefix_exists():
    # Check that the Enumeration exists
    assert DataVariablePrefix is not None

def test_datavariableprefix_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataVariablePrefix]
    expected_literals = [
        "NONE",
        "CONST",
        "META",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataVariablePrefix"

def test_quantifier_exists():
    # Check that the Enumeration exists
    assert Quantifier is not None

def test_quantifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Quantifier]
    expected_literals = [
        "UNIVERSAL",
        "EXISTENTIAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Quantifier"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "MODULO_EQUAL",
        "BIT_RIGHT_EQUAL",
        "BIT_LEFT_EQUAL",
        "EQUAL",
        "PLUS_EQUAL",
        "MINUS_EQUAL",
        "BIT_OR_EQUAL",
        "DIVIDE_EQUAL",
        "TIMES_EQUAL",
        "BIT_AND_EQUAL",
        "BIT_XOR_EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_bitshiftoperator_exists():
    # Check that the Enumeration exists
    assert BitShiftOperator is not None

def test_bitshiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BitShiftOperator]
    expected_literals = [
        "RIGHT",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BitShiftOperator"

def test_locationkind_exists():
    # Check that the Enumeration exists
    assert LocationKind is not None

def test_locationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LocationKind]
    expected_literals = [
        "COMMITED",
        "NORMAL",
        "URGENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LocationKind"

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "DIVIDE",
        "MULTIPLICATE",
        "SUBTRACT",
        "MODULO",
        "ADD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_colorkind_exists():
    # Check that the Enumeration exists
    assert ColorKind is not None

def test_colorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColorKind]
    expected_literals = [
        "ORANGE",
        "GREEN",
        "WHITE",
        "SELF_DEFINED",
        "LIGHTGREY",
        "YELLOW",
        "CYAN",
        "BLACK",
        "MAGENTA",
        "DEFAULT",
        "PINK",
        "BLUE",
        "DARKGREY",
        "RED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColorKind"

def test_incrementdecrementposition_exists():
    # Check that the Enumeration exists
    assert IncrementDecrementPosition is not None

def test_incrementdecrementposition_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IncrementDecrementPosition]
    expected_literals = [
        "PRE",
        "POST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IncrementDecrementPosition"

def test_builtintype_exists():
    # Check that the Enumeration exists
    assert BuiltInType is not None

def test_builtintype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltInType]
    expected_literals = [
        "VOID",
        "CLOCK",
        "INT",
        "CHAN",
        "BOOL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInType"

def test_synchronizationkind_exists():
    # Check that the Enumeration exists
    assert SynchronizationKind is not None

def test_synchronizationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SynchronizationKind]
    expected_literals = [
        "RECEIVE",
        "SEND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SynchronizationKind"


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
uppaal::visuals::Point_strategy = st.builds(
    uppaal::visuals::Point,
    y=
        st.integers(),
    x=
        st.integers()
)
uppaal::visuals::LinearElement_strategy = st.builds(
    uppaal::visuals::LinearElement,
)
Point_strategy = st.builds(
    Point,
)
uppaal::visuals::PlanarElement_strategy = st.builds(
    uppaal::visuals::PlanarElement,
)
uppaal::visuals::ColoredElement_strategy = st.builds(
    uppaal::visuals::ColoredElement,
    colorCode=
        safe_text,
    color=
        safe_text
)
expressions::Expression_strategy = st.builds(
    expressions::Expression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
uppaal::expressions::BitShiftExpression_strategy = st.builds(
    uppaal::expressions::BitShiftExpression,
    operator=
        safe_text
)
uppaal::expressions::BitwiseExpression_strategy = st.builds(
    uppaal::expressions::BitwiseExpression,
    operator=
        safe_text
)
uppaal::expressions::CompareExpression_strategy = st.builds(
    uppaal::expressions::CompareExpression,
    operator=
        safe_text
)
uppaal::expressions::ArithmeticExpression_strategy = st.builds(
    uppaal::expressions::ArithmeticExpression,
    operator=
        safe_text
)
uppaal::expressions::LogicalExpression_strategy = st.builds(
    uppaal::expressions::LogicalExpression,
    operator=
        safe_text
)
uppaal::expressions::MinMaxExpression_strategy = st.builds(
    uppaal::expressions::MinMaxExpression,
    operator=
        safe_text
)
uppaal::expressions::AssignmentExpression_strategy = st.builds(
    uppaal::expressions::AssignmentExpression,
    operator=
        safe_text
)
uppaal::expressions::Expression_strategy = st.builds(
    uppaal::expressions::Expression,
)
statements::Statement_strategy = st.builds(
    statements::Statement,
)
uppaal::templates::Synchronization_strategy = st.builds(
    uppaal::templates::Synchronization,
    kind=
        safe_text
)
Selection_strategy = st.builds(
    Selection,
)
Synchronization_strategy = st.builds(
    Synchronization,
)
Statement_strategy = st.builds(
    Statement,
)
uppaal::statements::DoWhileLoop_strategy = st.builds(
    uppaal::statements::DoWhileLoop,
)
uppaal::statements::ExpressionStatement_strategy = st.builds(
    uppaal::statements::ExpressionStatement,
)
uppaal::statements::ForLoop_strategy = st.builds(
    uppaal::statements::ForLoop,
)
uppaal::statements::ReturnStatement_strategy = st.builds(
    uppaal::statements::ReturnStatement,
)
uppaal::statements::WhileLoop_strategy = st.builds(
    uppaal::statements::WhileLoop,
)
uppaal::statements::IfStatement_strategy = st.builds(
    uppaal::statements::IfStatement,
)
uppaal::statements::EmptyStatement_strategy = st.builds(
    uppaal::statements::EmptyStatement,
)
uppaal::statements::Block_strategy = st.builds(
    uppaal::statements::Block,
)
uppaal::statements::Statement_strategy = st.builds(
    uppaal::statements::Statement,
)
visuals::LinearElement_strategy = st.builds(
    visuals::LinearElement,
)
visuals::ColoredElement_strategy = st.builds(
    visuals::ColoredElement,
)
visuals::PlanarElement_strategy = st.builds(
    visuals::PlanarElement,
)
system::TemplateDeclaration_strategy = st.builds(
    system::TemplateDeclaration,
)
Location_strategy = st.builds(
    Location,
)
LocalDeclarations_strategy = st.builds(
    LocalDeclarations,
)
Edge_strategy = st.builds(
    Edge,
)
AbstractTemplate_strategy = st.builds(
    AbstractTemplate,
)
uppaal::templates::Template_strategy = st.builds(
    uppaal::templates::Template,
)
uppaal::templates::RedefinedTemplate_strategy = st.builds(
    uppaal::templates::RedefinedTemplate,
)
uppaal::system::InstantiationList_strategy = st.builds(
    uppaal::system::InstantiationList,
)
system::InstantiationList_strategy = st.builds(
    system::InstantiationList,
)
uppaal::system::System_strategy = st.builds(
    uppaal::system::System,
)
uppaal::system::ProgressMeasure_strategy = st.builds(
    uppaal::system::ProgressMeasure,
)
ChannelPriorityItem_strategy = st.builds(
    ChannelPriorityItem,
)
uppaal::global::ChannelList_strategy = st.builds(
    uppaal::global::ChannelList,
)
uppaal::global::ChannelPriorityItem_strategy = st.builds(
    uppaal::global::ChannelPriorityItem,
)
global::ChannelPriorityItem_strategy = st.builds(
    global::ChannelPriorityItem,
)
uppaal::global::ChannelPriority_strategy = st.builds(
    uppaal::global::ChannelPriority,
)
uppaal::declarations::Initializer_strategy = st.builds(
    uppaal::declarations::Initializer,
)
RedefinedTemplate_strategy = st.builds(
    RedefinedTemplate,
)
uppaal::global::DefaultChannelPriority_strategy = st.builds(
    uppaal::global::DefaultChannelPriority,
)
IdentifierExpression_strategy = st.builds(
    IdentifierExpression,
)
uppaal::declarations::VariableContainer_strategy = st.builds(
    uppaal::declarations::VariableContainer,
)
uppaal::declarations::Index_strategy = st.builds(
    uppaal::declarations::Index,
)
Initializer_strategy = st.builds(
    Initializer,
)
uppaal::declarations::ArrayInitializer_strategy = st.builds(
    uppaal::declarations::ArrayInitializer,
)
uppaal::declarations::ExpressionInitializer_strategy = st.builds(
    uppaal::declarations::ExpressionInitializer,
)
uppaal::declarations::Parameter_strategy = st.builds(
    uppaal::declarations::Parameter,
    callType=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
Parameter_strategy = st.builds(
    Parameter,
)
Block_strategy = st.builds(
    Block,
)
Function_strategy = st.builds(
    Function,
)
VariableContainer_strategy = st.builds(
    VariableContainer,
)
uppaal::templates::Selection_strategy = st.builds(
    uppaal::templates::Selection,
)
DeclaredType_strategy = st.builds(
    DeclaredType,
)
declarations::VariableContainer_strategy = st.builds(
    declarations::VariableContainer,
)
uppaal::statements::Iteration_strategy = st.builds(
    uppaal::statements::Iteration,
)
uppaal::expressions::QuantificationExpression_strategy = st.builds(
    uppaal::expressions::QuantificationExpression,
    quantifier=
        safe_text
)
declarations::Declaration_strategy = st.builds(
    declarations::Declaration,
)
uppaal::declarations::VariableDeclaration_strategy = st.builds(
    uppaal::declarations::VariableDeclaration,
)
uppaal::declarations::Declaration_strategy = st.builds(
    uppaal::declarations::Declaration,
)
system::ProgressMeasure_strategy = st.builds(
    system::ProgressMeasure,
)
system::System_strategy = st.builds(
    system::System,
)
global::ChannelPriority_strategy = st.builds(
    global::ChannelPriority,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
uppaal::declarations::ClockVariableDeclaration_strategy = st.builds(
    uppaal::declarations::ClockVariableDeclaration,
)
uppaal::declarations::DataVariableDeclaration_strategy = st.builds(
    uppaal::declarations::DataVariableDeclaration,
    prefix=
        safe_text
)
uppaal::declarations::ChannelVariableDeclaration_strategy = st.builds(
    uppaal::declarations::ChannelVariableDeclaration,
    urgent=
        st.booleans(),
    broadcast=
        st.booleans()
)
uppaal::types::Library_strategy = st.builds(
    uppaal::types::Library,
)
uppaal::types::IntegerBounds_strategy = st.builds(
    uppaal::types::IntegerBounds,
)
IntegerBounds_strategy = st.builds(
    IntegerBounds,
)
DataVariableDeclaration_strategy = st.builds(
    DataVariableDeclaration,
)
Declarations_strategy = st.builds(
    Declarations,
)
uppaal::declarations::SystemDeclarations_strategy = st.builds(
    uppaal::declarations::SystemDeclarations,
)
uppaal::declarations::LocalDeclarations_strategy = st.builds(
    uppaal::declarations::LocalDeclarations,
)
uppaal::declarations::GlobalDeclarations_strategy = st.builds(
    uppaal::declarations::GlobalDeclarations,
)
Declaration_strategy = st.builds(
    Declaration,
)
uppaal::declarations::TypeDeclaration_strategy = st.builds(
    uppaal::declarations::TypeDeclaration,
)
uppaal::declarations::FunctionDeclaration_strategy = st.builds(
    uppaal::declarations::FunctionDeclaration,
)
uppaal::system::TemplateDeclaration_strategy = st.builds(
    uppaal::system::TemplateDeclaration,
)
uppaal::declarations::Declarations_strategy = st.builds(
    uppaal::declarations::Declarations,
)
uppaal::types::TypeDefinition_strategy = st.builds(
    uppaal::types::TypeDefinition,
    baseType=
        safe_text
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
Type_strategy = st.builds(
    Type,
)
uppaal::types::DeclaredType_strategy = st.builds(
    uppaal::types::DeclaredType,
)
uppaal::types::PredefinedType_strategy = st.builds(
    uppaal::types::PredefinedType,
    type=
        safe_text
)
TypeSpecification_strategy = st.builds(
    TypeSpecification,
)
uppaal::types::StructTypeSpecification_strategy = st.builds(
    uppaal::types::StructTypeSpecification,
)
uppaal::types::RangeTypeSpecification_strategy = st.builds(
    uppaal::types::RangeTypeSpecification,
)
Expression_strategy = st.builds(
    Expression,
)
uppaal::expressions::PlusExpression_strategy = st.builds(
    uppaal::expressions::PlusExpression,
)
uppaal::expressions::IncrementDecrementExpression_strategy = st.builds(
    uppaal::expressions::IncrementDecrementExpression,
    position=
        safe_text,
    operator=
        safe_text
)
uppaal::expressions::NegationExpression_strategy = st.builds(
    uppaal::expressions::NegationExpression,
)
uppaal::expressions::ScopedIdentifierExpression_strategy = st.builds(
    uppaal::expressions::ScopedIdentifierExpression,
)
uppaal::expressions::MinusExpression_strategy = st.builds(
    uppaal::expressions::MinusExpression,
)
uppaal::expressions::BinaryExpression_strategy = st.builds(
    uppaal::expressions::BinaryExpression,
)
uppaal::expressions::ConditionExpression_strategy = st.builds(
    uppaal::expressions::ConditionExpression,
)
uppaal::expressions::FunctionCallExpression_strategy = st.builds(
    uppaal::expressions::FunctionCallExpression,
)
uppaal::expressions::LiteralExpression_strategy = st.builds(
    uppaal::expressions::LiteralExpression,
    text=
        safe_text
)
uppaal::expressions::IdentifierExpression_strategy = st.builds(
    uppaal::expressions::IdentifierExpression,
)
uppaal::types::ScalarTypeSpecification_strategy = st.builds(
    uppaal::types::ScalarTypeSpecification,
)
uppaal::types::TypeSpecification_strategy = st.builds(
    uppaal::types::TypeSpecification,
)
uppaal::types::TypeReference_strategy = st.builds(
    uppaal::types::TypeReference,
)
uppaal::core::NamedElement_strategy = st.builds(
    uppaal::core::NamedElement,
    name=
        safe_text
)
PredefinedType_strategy = st.builds(
    PredefinedType,
)
Index_strategy = st.builds(
    Index,
)
uppaal::declarations::TypeIndex_strategy = st.builds(
    uppaal::declarations::TypeIndex,
)
uppaal::declarations::ValueIndex_strategy = st.builds(
    uppaal::declarations::ValueIndex,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uppaal::declarations::Function_strategy = st.builds(
    uppaal::declarations::Function,
)
uppaal::declarations::Variable_strategy = st.builds(
    uppaal::declarations::Variable,
)
uppaal::types::Type_strategy = st.builds(
    uppaal::types::Type,
    baseType=
        safe_text
)
uppaal::core::CommentableElement_strategy = st.builds(
    uppaal::core::CommentableElement,
    comment=
        safe_text
)
core::CommentableElement_strategy = st.builds(
    core::CommentableElement,
)
uppaal::templates::Edge_strategy = st.builds(
    uppaal::templates::Edge,
)
core::NamedElement_strategy = st.builds(
    core::NamedElement,
)
uppaal::templates::AbstractTemplate_strategy = st.builds(
    uppaal::templates::AbstractTemplate,
)
uppaal::templates::Location_strategy = st.builds(
    uppaal::templates::Location,
    locationTimeKind=
        safe_text
)
uppaal::NTA_strategy = st.builds(
    uppaal::NTA,
)
SystemDeclarations_strategy = st.builds(
    SystemDeclarations,
)
Template_strategy = st.builds(
    Template,
)
GlobalDeclarations_strategy = st.builds(
    GlobalDeclarations,
)

@given(instance=uppaal::visuals::Point_strategy)
@settings(max_examples=50)
def test_uppaal::visuals::point_instantiation(instance):
    assert isinstance(instance, uppaal::visuals::Point)

@given(instance=uppaal::visuals::Point_strategy)
def test_uppaal::visuals::point_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=uppaal::visuals::Point_strategy)
def test_uppaal::visuals::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=uppaal::visuals::Point_strategy)
def test_uppaal::visuals::point_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=uppaal::visuals::Point_strategy)
def test_uppaal::visuals::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=uppaal::visuals::LinearElement_strategy)
@settings(max_examples=50)
def test_uppaal::visuals::linearelement_instantiation(instance):
    assert isinstance(instance, uppaal::visuals::LinearElement)

@given(instance=Point_strategy)
@settings(max_examples=50)
def test_point_instantiation(instance):
    assert isinstance(instance, Point)

@given(instance=uppaal::visuals::PlanarElement_strategy)
@settings(max_examples=50)
def test_uppaal::visuals::planarelement_instantiation(instance):
    assert isinstance(instance, uppaal::visuals::PlanarElement)

@given(instance=uppaal::visuals::ColoredElement_strategy)
@settings(max_examples=50)
def test_uppaal::visuals::coloredelement_instantiation(instance):
    assert isinstance(instance, uppaal::visuals::ColoredElement)

@given(instance=uppaal::visuals::ColoredElement_strategy)
def test_uppaal::visuals::coloredelement_colorCode_type(instance):
    assert isinstance(instance.colorCode, str)


@given(instance=uppaal::visuals::ColoredElement_strategy)
def test_uppaal::visuals::coloredelement_colorCode_setter(instance):
    original = instance.colorCode
    instance.colorCode = original
    assert instance.colorCode == original

@given(instance=uppaal::visuals::ColoredElement_strategy)
def test_uppaal::visuals::coloredelement_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=uppaal::visuals::ColoredElement_strategy)
def test_uppaal::visuals::coloredelement_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=expressions::Expression_strategy)
@settings(max_examples=50)
def test_expressions::expression_instantiation(instance):
    assert isinstance(instance, expressions::Expression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=uppaal::expressions::BitShiftExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::bitshiftexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::BitShiftExpression)

@given(instance=uppaal::expressions::BitShiftExpression_strategy)
def test_uppaal::expressions::bitshiftexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=uppaal::expressions::BitShiftExpression_strategy)
def test_uppaal::expressions::bitshiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal::expressions::BitwiseExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::bitwiseexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::BitwiseExpression)

@given(instance=uppaal::expressions::BitwiseExpression_strategy)
def test_uppaal::expressions::bitwiseexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=uppaal::expressions::BitwiseExpression_strategy)
def test_uppaal::expressions::bitwiseexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal::expressions::CompareExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::compareexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::CompareExpression)

@given(instance=uppaal::expressions::CompareExpression_strategy)
def test_uppaal::expressions::compareexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=uppaal::expressions::CompareExpression_strategy)
def test_uppaal::expressions::compareexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal::expressions::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::ArithmeticExpression)

@given(instance=uppaal::expressions::ArithmeticExpression_strategy)
def test_uppaal::expressions::arithmeticexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=uppaal::expressions::ArithmeticExpression_strategy)
def test_uppaal::expressions::arithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal::expressions::LogicalExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::logicalexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::LogicalExpression)

@given(instance=uppaal::expressions::LogicalExpression_strategy)
def test_uppaal::expressions::logicalexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=uppaal::expressions::LogicalExpression_strategy)
def test_uppaal::expressions::logicalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal::expressions::MinMaxExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::minmaxexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::MinMaxExpression)

@given(instance=uppaal::expressions::MinMaxExpression_strategy)
def test_uppaal::expressions::minmaxexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=uppaal::expressions::MinMaxExpression_strategy)
def test_uppaal::expressions::minmaxexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal::expressions::AssignmentExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::assignmentexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::AssignmentExpression)

@given(instance=uppaal::expressions::AssignmentExpression_strategy)
def test_uppaal::expressions::assignmentexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=uppaal::expressions::AssignmentExpression_strategy)
def test_uppaal::expressions::assignmentexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal::expressions::Expression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::expression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::Expression)

@given(instance=statements::Statement_strategy)
@settings(max_examples=50)
def test_statements::statement_instantiation(instance):
    assert isinstance(instance, statements::Statement)

@given(instance=uppaal::templates::Synchronization_strategy)
@settings(max_examples=50)
def test_uppaal::templates::synchronization_instantiation(instance):
    assert isinstance(instance, uppaal::templates::Synchronization)

@given(instance=uppaal::templates::Synchronization_strategy)
def test_uppaal::templates::synchronization_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=uppaal::templates::Synchronization_strategy)
def test_uppaal::templates::synchronization_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Selection_strategy)
@settings(max_examples=50)
def test_selection_instantiation(instance):
    assert isinstance(instance, Selection)

@given(instance=Synchronization_strategy)
@settings(max_examples=50)
def test_synchronization_instantiation(instance):
    assert isinstance(instance, Synchronization)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=uppaal::statements::DoWhileLoop_strategy)
@settings(max_examples=50)
def test_uppaal::statements::dowhileloop_instantiation(instance):
    assert isinstance(instance, uppaal::statements::DoWhileLoop)

@given(instance=uppaal::statements::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_uppaal::statements::expressionstatement_instantiation(instance):
    assert isinstance(instance, uppaal::statements::ExpressionStatement)

@given(instance=uppaal::statements::ForLoop_strategy)
@settings(max_examples=50)
def test_uppaal::statements::forloop_instantiation(instance):
    assert isinstance(instance, uppaal::statements::ForLoop)

@given(instance=uppaal::statements::ReturnStatement_strategy)
@settings(max_examples=50)
def test_uppaal::statements::returnstatement_instantiation(instance):
    assert isinstance(instance, uppaal::statements::ReturnStatement)

@given(instance=uppaal::statements::WhileLoop_strategy)
@settings(max_examples=50)
def test_uppaal::statements::whileloop_instantiation(instance):
    assert isinstance(instance, uppaal::statements::WhileLoop)

@given(instance=uppaal::statements::IfStatement_strategy)
@settings(max_examples=50)
def test_uppaal::statements::ifstatement_instantiation(instance):
    assert isinstance(instance, uppaal::statements::IfStatement)

@given(instance=uppaal::statements::EmptyStatement_strategy)
@settings(max_examples=50)
def test_uppaal::statements::emptystatement_instantiation(instance):
    assert isinstance(instance, uppaal::statements::EmptyStatement)

@given(instance=uppaal::statements::Block_strategy)
@settings(max_examples=50)
def test_uppaal::statements::block_instantiation(instance):
    assert isinstance(instance, uppaal::statements::Block)

@given(instance=uppaal::statements::Statement_strategy)
@settings(max_examples=50)
def test_uppaal::statements::statement_instantiation(instance):
    assert isinstance(instance, uppaal::statements::Statement)

@given(instance=visuals::LinearElement_strategy)
@settings(max_examples=50)
def test_visuals::linearelement_instantiation(instance):
    assert isinstance(instance, visuals::LinearElement)

@given(instance=visuals::ColoredElement_strategy)
@settings(max_examples=50)
def test_visuals::coloredelement_instantiation(instance):
    assert isinstance(instance, visuals::ColoredElement)

@given(instance=visuals::PlanarElement_strategy)
@settings(max_examples=50)
def test_visuals::planarelement_instantiation(instance):
    assert isinstance(instance, visuals::PlanarElement)

@given(instance=system::TemplateDeclaration_strategy)
@settings(max_examples=50)
def test_system::templatedeclaration_instantiation(instance):
    assert isinstance(instance, system::TemplateDeclaration)

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)

@given(instance=LocalDeclarations_strategy)
@settings(max_examples=50)
def test_localdeclarations_instantiation(instance):
    assert isinstance(instance, LocalDeclarations)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=AbstractTemplate_strategy)
@settings(max_examples=50)
def test_abstracttemplate_instantiation(instance):
    assert isinstance(instance, AbstractTemplate)

@given(instance=uppaal::templates::Template_strategy)
@settings(max_examples=50)
def test_uppaal::templates::template_instantiation(instance):
    assert isinstance(instance, uppaal::templates::Template)

@given(instance=uppaal::templates::RedefinedTemplate_strategy)
@settings(max_examples=50)
def test_uppaal::templates::redefinedtemplate_instantiation(instance):
    assert isinstance(instance, uppaal::templates::RedefinedTemplate)

@given(instance=uppaal::system::InstantiationList_strategy)
@settings(max_examples=50)
def test_uppaal::system::instantiationlist_instantiation(instance):
    assert isinstance(instance, uppaal::system::InstantiationList)

@given(instance=system::InstantiationList_strategy)
@settings(max_examples=50)
def test_system::instantiationlist_instantiation(instance):
    assert isinstance(instance, system::InstantiationList)

@given(instance=uppaal::system::System_strategy)
@settings(max_examples=50)
def test_uppaal::system::system_instantiation(instance):
    assert isinstance(instance, uppaal::system::System)

@given(instance=uppaal::system::ProgressMeasure_strategy)
@settings(max_examples=50)
def test_uppaal::system::progressmeasure_instantiation(instance):
    assert isinstance(instance, uppaal::system::ProgressMeasure)

@given(instance=ChannelPriorityItem_strategy)
@settings(max_examples=50)
def test_channelpriorityitem_instantiation(instance):
    assert isinstance(instance, ChannelPriorityItem)

@given(instance=uppaal::global::ChannelList_strategy)
@settings(max_examples=50)
def test_uppaal::global::channellist_instantiation(instance):
    assert isinstance(instance, uppaal::global::ChannelList)

@given(instance=uppaal::global::ChannelPriorityItem_strategy)
@settings(max_examples=50)
def test_uppaal::global::channelpriorityitem_instantiation(instance):
    assert isinstance(instance, uppaal::global::ChannelPriorityItem)

@given(instance=global::ChannelPriorityItem_strategy)
@settings(max_examples=50)
def test_global::channelpriorityitem_instantiation(instance):
    assert isinstance(instance, global::ChannelPriorityItem)

@given(instance=uppaal::global::ChannelPriority_strategy)
@settings(max_examples=50)
def test_uppaal::global::channelpriority_instantiation(instance):
    assert isinstance(instance, uppaal::global::ChannelPriority)

@given(instance=uppaal::declarations::Initializer_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::initializer_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::Initializer)

@given(instance=RedefinedTemplate_strategy)
@settings(max_examples=50)
def test_redefinedtemplate_instantiation(instance):
    assert isinstance(instance, RedefinedTemplate)

@given(instance=uppaal::global::DefaultChannelPriority_strategy)
@settings(max_examples=50)
def test_uppaal::global::defaultchannelpriority_instantiation(instance):
    assert isinstance(instance, uppaal::global::DefaultChannelPriority)

@given(instance=IdentifierExpression_strategy)
@settings(max_examples=50)
def test_identifierexpression_instantiation(instance):
    assert isinstance(instance, IdentifierExpression)

@given(instance=uppaal::declarations::VariableContainer_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::variablecontainer_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::VariableContainer)

@given(instance=uppaal::declarations::Index_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::index_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::Index)

@given(instance=Initializer_strategy)
@settings(max_examples=50)
def test_initializer_instantiation(instance):
    assert isinstance(instance, Initializer)

@given(instance=uppaal::declarations::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::arrayinitializer_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::ArrayInitializer)

@given(instance=uppaal::declarations::ExpressionInitializer_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::expressioninitializer_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::ExpressionInitializer)

@given(instance=uppaal::declarations::Parameter_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::parameter_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::Parameter)

@given(instance=uppaal::declarations::Parameter_strategy)
def test_uppaal::declarations::parameter_callType_type(instance):
    assert isinstance(instance.callType, str)


@given(instance=uppaal::declarations::Parameter_strategy)
def test_uppaal::declarations::parameter_callType_setter(instance):
    original = instance.callType
    instance.callType = original
    assert instance.callType == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=VariableContainer_strategy)
@settings(max_examples=50)
def test_variablecontainer_instantiation(instance):
    assert isinstance(instance, VariableContainer)

@given(instance=uppaal::templates::Selection_strategy)
@settings(max_examples=50)
def test_uppaal::templates::selection_instantiation(instance):
    assert isinstance(instance, uppaal::templates::Selection)

@given(instance=DeclaredType_strategy)
@settings(max_examples=50)
def test_declaredtype_instantiation(instance):
    assert isinstance(instance, DeclaredType)

@given(instance=declarations::VariableContainer_strategy)
@settings(max_examples=50)
def test_declarations::variablecontainer_instantiation(instance):
    assert isinstance(instance, declarations::VariableContainer)

@given(instance=uppaal::statements::Iteration_strategy)
@settings(max_examples=50)
def test_uppaal::statements::iteration_instantiation(instance):
    assert isinstance(instance, uppaal::statements::Iteration)

@given(instance=uppaal::expressions::QuantificationExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::quantificationexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::QuantificationExpression)

@given(instance=uppaal::expressions::QuantificationExpression_strategy)
def test_uppaal::expressions::quantificationexpression_quantifier_type(instance):
    assert isinstance(instance.quantifier, str)


@given(instance=uppaal::expressions::QuantificationExpression_strategy)
def test_uppaal::expressions::quantificationexpression_quantifier_setter(instance):
    original = instance.quantifier
    instance.quantifier = original
    assert instance.quantifier == original

@given(instance=declarations::Declaration_strategy)
@settings(max_examples=50)
def test_declarations::declaration_instantiation(instance):
    assert isinstance(instance, declarations::Declaration)

@given(instance=uppaal::declarations::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::variabledeclaration_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::VariableDeclaration)

@given(instance=uppaal::declarations::Declaration_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::declaration_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::Declaration)

@given(instance=system::ProgressMeasure_strategy)
@settings(max_examples=50)
def test_system::progressmeasure_instantiation(instance):
    assert isinstance(instance, system::ProgressMeasure)

@given(instance=system::System_strategy)
@settings(max_examples=50)
def test_system::system_instantiation(instance):
    assert isinstance(instance, system::System)

@given(instance=global::ChannelPriority_strategy)
@settings(max_examples=50)
def test_global::channelpriority_instantiation(instance):
    assert isinstance(instance, global::ChannelPriority)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=uppaal::declarations::ClockVariableDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::clockvariabledeclaration_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::ClockVariableDeclaration)

@given(instance=uppaal::declarations::DataVariableDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::datavariabledeclaration_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::DataVariableDeclaration)

@given(instance=uppaal::declarations::DataVariableDeclaration_strategy)
def test_uppaal::declarations::datavariabledeclaration_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=uppaal::declarations::DataVariableDeclaration_strategy)
def test_uppaal::declarations::datavariabledeclaration_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=uppaal::declarations::ChannelVariableDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::channelvariabledeclaration_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::ChannelVariableDeclaration)

@given(instance=uppaal::declarations::ChannelVariableDeclaration_strategy)
def test_uppaal::declarations::channelvariabledeclaration_urgent_type(instance):
    assert isinstance(instance.urgent, bool)


@given(instance=uppaal::declarations::ChannelVariableDeclaration_strategy)
def test_uppaal::declarations::channelvariabledeclaration_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original

@given(instance=uppaal::declarations::ChannelVariableDeclaration_strategy)
def test_uppaal::declarations::channelvariabledeclaration_broadcast_type(instance):
    assert isinstance(instance.broadcast, bool)


@given(instance=uppaal::declarations::ChannelVariableDeclaration_strategy)
def test_uppaal::declarations::channelvariabledeclaration_broadcast_setter(instance):
    original = instance.broadcast
    instance.broadcast = original
    assert instance.broadcast == original

@given(instance=uppaal::types::Library_strategy)
@settings(max_examples=50)
def test_uppaal::types::library_instantiation(instance):
    assert isinstance(instance, uppaal::types::Library)

@given(instance=uppaal::types::IntegerBounds_strategy)
@settings(max_examples=50)
def test_uppaal::types::integerbounds_instantiation(instance):
    assert isinstance(instance, uppaal::types::IntegerBounds)

@given(instance=IntegerBounds_strategy)
@settings(max_examples=50)
def test_integerbounds_instantiation(instance):
    assert isinstance(instance, IntegerBounds)

@given(instance=DataVariableDeclaration_strategy)
@settings(max_examples=50)
def test_datavariabledeclaration_instantiation(instance):
    assert isinstance(instance, DataVariableDeclaration)

@given(instance=Declarations_strategy)
@settings(max_examples=50)
def test_declarations_instantiation(instance):
    assert isinstance(instance, Declarations)

@given(instance=uppaal::declarations::SystemDeclarations_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::systemdeclarations_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::SystemDeclarations)

@given(instance=uppaal::declarations::LocalDeclarations_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::localdeclarations_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::LocalDeclarations)

@given(instance=uppaal::declarations::GlobalDeclarations_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::globaldeclarations_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::GlobalDeclarations)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=uppaal::declarations::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::typedeclaration_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::TypeDeclaration)

@given(instance=uppaal::declarations::FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::functiondeclaration_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::FunctionDeclaration)

@given(instance=uppaal::system::TemplateDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal::system::templatedeclaration_instantiation(instance):
    assert isinstance(instance, uppaal::system::TemplateDeclaration)

@given(instance=uppaal::declarations::Declarations_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::declarations_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::Declarations)

@given(instance=uppaal::types::TypeDefinition_strategy)
@settings(max_examples=50)
def test_uppaal::types::typedefinition_instantiation(instance):
    assert isinstance(instance, uppaal::types::TypeDefinition)

@given(instance=uppaal::types::TypeDefinition_strategy)
def test_uppaal::types::typedefinition_baseType_type(instance):
    assert isinstance(instance.baseType, str)


@given(instance=uppaal::types::TypeDefinition_strategy)
def test_uppaal::types::typedefinition_baseType_setter(instance):
    original = instance.baseType
    instance.baseType = original
    assert instance.baseType == original

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=uppaal::types::DeclaredType_strategy)
@settings(max_examples=50)
def test_uppaal::types::declaredtype_instantiation(instance):
    assert isinstance(instance, uppaal::types::DeclaredType)

@given(instance=uppaal::types::PredefinedType_strategy)
@settings(max_examples=50)
def test_uppaal::types::predefinedtype_instantiation(instance):
    assert isinstance(instance, uppaal::types::PredefinedType)

@given(instance=uppaal::types::PredefinedType_strategy)
def test_uppaal::types::predefinedtype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=uppaal::types::PredefinedType_strategy)
def test_uppaal::types::predefinedtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=TypeSpecification_strategy)
@settings(max_examples=50)
def test_typespecification_instantiation(instance):
    assert isinstance(instance, TypeSpecification)

@given(instance=uppaal::types::StructTypeSpecification_strategy)
@settings(max_examples=50)
def test_uppaal::types::structtypespecification_instantiation(instance):
    assert isinstance(instance, uppaal::types::StructTypeSpecification)

@given(instance=uppaal::types::RangeTypeSpecification_strategy)
@settings(max_examples=50)
def test_uppaal::types::rangetypespecification_instantiation(instance):
    assert isinstance(instance, uppaal::types::RangeTypeSpecification)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=uppaal::expressions::PlusExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::plusexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::PlusExpression)

@given(instance=uppaal::expressions::IncrementDecrementExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::incrementdecrementexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::IncrementDecrementExpression)

@given(instance=uppaal::expressions::IncrementDecrementExpression_strategy)
def test_uppaal::expressions::incrementdecrementexpression_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=uppaal::expressions::IncrementDecrementExpression_strategy)
def test_uppaal::expressions::incrementdecrementexpression_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=uppaal::expressions::IncrementDecrementExpression_strategy)
def test_uppaal::expressions::incrementdecrementexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=uppaal::expressions::IncrementDecrementExpression_strategy)
def test_uppaal::expressions::incrementdecrementexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal::expressions::NegationExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::negationexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::NegationExpression)

@given(instance=uppaal::expressions::ScopedIdentifierExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::scopedidentifierexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::ScopedIdentifierExpression)

@given(instance=uppaal::expressions::MinusExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::minusexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::MinusExpression)

@given(instance=uppaal::expressions::BinaryExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::binaryexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::BinaryExpression)

@given(instance=uppaal::expressions::ConditionExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::conditionexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::ConditionExpression)

@given(instance=uppaal::expressions::FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::functioncallexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::FunctionCallExpression)

@given(instance=uppaal::expressions::LiteralExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::literalexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::LiteralExpression)

@given(instance=uppaal::expressions::LiteralExpression_strategy)
def test_uppaal::expressions::literalexpression_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=uppaal::expressions::LiteralExpression_strategy)
def test_uppaal::expressions::literalexpression_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=uppaal::expressions::IdentifierExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::identifierexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::IdentifierExpression)

@given(instance=uppaal::types::ScalarTypeSpecification_strategy)
@settings(max_examples=50)
def test_uppaal::types::scalartypespecification_instantiation(instance):
    assert isinstance(instance, uppaal::types::ScalarTypeSpecification)

@given(instance=uppaal::types::TypeSpecification_strategy)
@settings(max_examples=50)
def test_uppaal::types::typespecification_instantiation(instance):
    assert isinstance(instance, uppaal::types::TypeSpecification)

@given(instance=uppaal::types::TypeReference_strategy)
@settings(max_examples=50)
def test_uppaal::types::typereference_instantiation(instance):
    assert isinstance(instance, uppaal::types::TypeReference)

@given(instance=uppaal::core::NamedElement_strategy)
@settings(max_examples=50)
def test_uppaal::core::namedelement_instantiation(instance):
    assert isinstance(instance, uppaal::core::NamedElement)

@given(instance=uppaal::core::NamedElement_strategy)
def test_uppaal::core::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uppaal::core::NamedElement_strategy)
def test_uppaal::core::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PredefinedType_strategy)
@settings(max_examples=50)
def test_predefinedtype_instantiation(instance):
    assert isinstance(instance, PredefinedType)

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=uppaal::declarations::TypeIndex_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::typeindex_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::TypeIndex)

@given(instance=uppaal::declarations::ValueIndex_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::valueindex_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::ValueIndex)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uppaal::declarations::Function_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::function_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::Function)

@given(instance=uppaal::declarations::Variable_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::variable_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::Variable)

@given(instance=uppaal::types::Type_strategy)
@settings(max_examples=50)
def test_uppaal::types::type_instantiation(instance):
    assert isinstance(instance, uppaal::types::Type)

@given(instance=uppaal::types::Type_strategy)
def test_uppaal::types::type_baseType_type(instance):
    assert isinstance(instance.baseType, str)


@given(instance=uppaal::types::Type_strategy)
def test_uppaal::types::type_baseType_setter(instance):
    original = instance.baseType
    instance.baseType = original
    assert instance.baseType == original

@given(instance=uppaal::core::CommentableElement_strategy)
@settings(max_examples=50)
def test_uppaal::core::commentableelement_instantiation(instance):
    assert isinstance(instance, uppaal::core::CommentableElement)

@given(instance=uppaal::core::CommentableElement_strategy)
def test_uppaal::core::commentableelement_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=uppaal::core::CommentableElement_strategy)
def test_uppaal::core::commentableelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=core::CommentableElement_strategy)
@settings(max_examples=50)
def test_core::commentableelement_instantiation(instance):
    assert isinstance(instance, core::CommentableElement)

@given(instance=uppaal::templates::Edge_strategy)
@settings(max_examples=50)
def test_uppaal::templates::edge_instantiation(instance):
    assert isinstance(instance, uppaal::templates::Edge)

@given(instance=core::NamedElement_strategy)
@settings(max_examples=50)
def test_core::namedelement_instantiation(instance):
    assert isinstance(instance, core::NamedElement)

@given(instance=uppaal::templates::AbstractTemplate_strategy)
@settings(max_examples=50)
def test_uppaal::templates::abstracttemplate_instantiation(instance):
    assert isinstance(instance, uppaal::templates::AbstractTemplate)

@given(instance=uppaal::templates::Location_strategy)
@settings(max_examples=50)
def test_uppaal::templates::location_instantiation(instance):
    assert isinstance(instance, uppaal::templates::Location)

@given(instance=uppaal::templates::Location_strategy)
def test_uppaal::templates::location_locationTimeKind_type(instance):
    assert isinstance(instance.locationTimeKind, str)


@given(instance=uppaal::templates::Location_strategy)
def test_uppaal::templates::location_locationTimeKind_setter(instance):
    original = instance.locationTimeKind
    instance.locationTimeKind = original
    assert instance.locationTimeKind == original

@given(instance=uppaal::NTA_strategy)
@settings(max_examples=50)
def test_uppaal::nta_instantiation(instance):
    assert isinstance(instance, uppaal::NTA)

@given(instance=SystemDeclarations_strategy)
@settings(max_examples=50)
def test_systemdeclarations_instantiation(instance):
    assert isinstance(instance, SystemDeclarations)

@given(instance=Template_strategy)
@settings(max_examples=50)
def test_template_instantiation(instance):
    assert isinstance(instance, Template)

@given(instance=GlobalDeclarations_strategy)
@settings(max_examples=50)
def test_globaldeclarations_instantiation(instance):
    assert isinstance(instance, GlobalDeclarations)
