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
    IncrementDecrementExpression,
    uppaal::expressions::PostIncrementDecrementExpression,
    uppaal::expressions::PreIncrementDecrementExpression,
    expressions::Expression,
    Function,
    BinaryExpression,
    uppaal::expressions::CompareExpression,
    uppaal::expressions::MinMaxExpression,
    uppaal::expressions::BitwiseExpression,
    uppaal::expressions::BitShiftExpression,
    uppaal::expressions::LogicalExpression,
    uppaal::expressions::ArithmeticExpression,
    uppaal::expressions::AssignmentExpression,
    uppaal::expressions::Expression,
    statements::Statement,
    uppaal::templates::Synchronization,
    Statement,
    uppaal::statements::ForLoop,
    uppaal::statements::IfStatement,
    uppaal::statements::DoWhileLoop,
    uppaal::statements::WhileLoop,
    uppaal::statements::ExpressionStatement,
    uppaal::statements::EmptyStatement,
    uppaal::statements::ReturnStatement,
    uppaal::statements::Block,
    uppaal::statements::Statement,
    visuals::LinearElement,
    Selection,
    Synchronization,
    Location,
    LocalDeclarations,
    visuals::ColoredElement,
    visuals::PlanarElement,
    system::TemplateDeclaration,
    Edge,
    RedefinedTemplate,
    IdentifierExpression,
    PriorityItem,
    uppaal::global::DefaultItem,
    uppaal::global::ChannelItem,
    uppaal::global::PriorityItem,
    global::PriorityItem,
    uppaal::global::ChannelPriorityGroup,
    uppaal::system::ProgressMeasure,
    AbstractTemplate,
    uppaal::templates::RedefinedTemplate,
    uppaal::templates::Template,
    uppaal::system::InstantiationList,
    system::InstantiationList,
    uppaal::system::System,
    uppaal::declarations::Initializer,
    Variable,
    uppaal::declarations::Parameter,
    TypedElement,
    uppaal::declarations::TypedElementContainer,
    global::ChannelPriorityGroup,
    Initializer,
    uppaal::declarations::ArrayInitializer,
    uppaal::declarations::ExpressionInitializer,
    declarations::TypedElementContainer,
    uppaal::expressions::QuantificationExpression,
    uppaal::statements::Iteration,
    declarations::Declaration,
    uppaal::declarations::TypedDeclaration,
    DeclaredType,
    uppaal::declarations::Declaration,
    system::ProgressMeasure,
    system::System,
    global::ChannelPriorityDeclaration,
    ParameterContainer,
    Block,
    core::TypedElement,
    uppaal::types::IntegerBounds,
    IntegerBounds,
    TypedDeclaration,
    TypeExpression,
    uppaal::types::StructTypeSpecification,
    uppaal::types::RangeTypeSpecification,
    uppaal::types::ScalarTypeSpecification,
    Declarations,
    uppaal::declarations::SystemDeclarations,
    uppaal::declarations::LocalDeclarations,
    uppaal::declarations::GlobalDeclarations,
    Declaration,
    uppaal::global::ChannelPriorityDeclaration,
    uppaal::declarations::TypeDeclaration,
    uppaal::system::TemplateDeclaration,
    uppaal::declarations::Declarations,
    PredefinedType,
    uppaal::types::Library,
    NamedElement,
    uppaal::templates::AbstractTemplate,
    uppaal::types::Type,
    Expression,
    uppaal::expressions::BinaryExpression,
    uppaal::expressions::DataPrefixExpression,
    uppaal::expressions::LiteralExpression,
    uppaal::expressions::FunctionCallExpression,
    uppaal::expressions::IncrementDecrementExpression,
    uppaal::expressions::ChannelPrefixExpression,
    uppaal::types::TypeExpression,
    uppaal::expressions::PlusExpression,
    uppaal::expressions::MinusExpression,
    uppaal::expressions::ConditionExpression,
    uppaal::expressions::NegationExpression,
    uppaal::expressions::ScopedIdentifierExpression,
    uppaal::expressions::IdentifierExpression,
    TypedElementContainer,
    uppaal::templates::Selection,
    uppaal::declarations::ParameterContainer,
    uppaal::core::TypedElement,
    uppaal::core::CommentableElement,
    uppaal::core::NamedElement,
    TypeDeclaration,
    Type,
    uppaal::types::DeclaredType,
    uppaal::types::PredefinedType,
    core::CommentableElement,
    uppaal::templates::Edge,
    core::NamedElement,
    uppaal::declarations::Function,
    uppaal::templates::Location,
    uppaal::declarations::Variable,
    uppaal::NTA,
    SystemDeclarations,
    Template,
    GlobalDeclarations,
    IncrementDecrementOperator,
    CallType,
    Quantifier,
    CompareOperator,
    MinMaxOperator,
    LocationKind,
    DataVariablePrefix,
    BuiltInType,
    BitShiftOperator,
    AssignmentOperator,
    BitwiseOperator,
    ArithmeticOperator,
    LogicalOperator,
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

def test_uppaal::visuals::coloredelement_has_colorCode():
    assert hasattr(uppaal::visuals::ColoredElement, "colorCode")
    descriptor = None
    for klass in uppaal::visuals::ColoredElement.__mro__:
        if "colorCode" in klass.__dict__:
            descriptor = klass.__dict__["colorCode"]
            break
    assert isinstance(descriptor, property)



def test_incrementdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(IncrementDecrementExpression)


def test_incrementdecrementexpression_constructor_exists():
    assert callable(IncrementDecrementExpression.__init__)


def test_incrementdecrementexpression_constructor_args():
    sig = inspect.signature(IncrementDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::postincrementdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::PostIncrementDecrementExpression)


def test_uppaal::expressions::postincrementdecrementexpression_constructor_exists():
    assert callable(uppaal::expressions::PostIncrementDecrementExpression.__init__)


def test_uppaal::expressions::postincrementdecrementexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::PostIncrementDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::preincrementdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::PreIncrementDecrementExpression)


def test_uppaal::expressions::preincrementdecrementexpression_constructor_exists():
    assert callable(uppaal::expressions::PreIncrementDecrementExpression.__init__)


def test_uppaal::expressions::preincrementdecrementexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::PreIncrementDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::expression_is_not_abstract():
    assert not inspect.isabstract(expressions::Expression)


def test_expressions::expression_constructor_exists():
    assert callable(expressions::Expression.__init__)


def test_expressions::expression_constructor_args():
    sig = inspect.signature(expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



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



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::forloop_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::ForLoop)


def test_uppaal::statements::forloop_constructor_exists():
    assert callable(uppaal::statements::ForLoop.__init__)


def test_uppaal::statements::forloop_constructor_args():
    sig = inspect.signature(uppaal::statements::ForLoop.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::ifstatement_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::IfStatement)


def test_uppaal::statements::ifstatement_constructor_exists():
    assert callable(uppaal::statements::IfStatement.__init__)


def test_uppaal::statements::ifstatement_constructor_args():
    sig = inspect.signature(uppaal::statements::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::dowhileloop_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::DoWhileLoop)


def test_uppaal::statements::dowhileloop_constructor_exists():
    assert callable(uppaal::statements::DoWhileLoop.__init__)


def test_uppaal::statements::dowhileloop_constructor_args():
    sig = inspect.signature(uppaal::statements::DoWhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::whileloop_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::WhileLoop)


def test_uppaal::statements::whileloop_constructor_exists():
    assert callable(uppaal::statements::WhileLoop.__init__)


def test_uppaal::statements::whileloop_constructor_args():
    sig = inspect.signature(uppaal::statements::WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::ExpressionStatement)


def test_uppaal::statements::expressionstatement_constructor_exists():
    assert callable(uppaal::statements::ExpressionStatement.__init__)


def test_uppaal::statements::expressionstatement_constructor_args():
    sig = inspect.signature(uppaal::statements::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::emptystatement_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::EmptyStatement)


def test_uppaal::statements::emptystatement_constructor_exists():
    assert callable(uppaal::statements::EmptyStatement.__init__)


def test_uppaal::statements::emptystatement_constructor_args():
    sig = inspect.signature(uppaal::statements::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::statements::returnstatement_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::ReturnStatement)


def test_uppaal::statements::returnstatement_constructor_exists():
    assert callable(uppaal::statements::ReturnStatement.__init__)


def test_uppaal::statements::returnstatement_constructor_args():
    sig = inspect.signature(uppaal::statements::ReturnStatement.__init__)
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



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_redefinedtemplate_is_not_abstract():
    assert not inspect.isabstract(RedefinedTemplate)


def test_redefinedtemplate_constructor_exists():
    assert callable(RedefinedTemplate.__init__)


def test_redefinedtemplate_constructor_args():
    sig = inspect.signature(RedefinedTemplate.__init__)
    params = list(sig.parameters.keys())



def test_identifierexpression_is_not_abstract():
    assert not inspect.isabstract(IdentifierExpression)


def test_identifierexpression_constructor_exists():
    assert callable(IdentifierExpression.__init__)


def test_identifierexpression_constructor_args():
    sig = inspect.signature(IdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_priorityitem_is_not_abstract():
    assert not inspect.isabstract(PriorityItem)


def test_priorityitem_constructor_exists():
    assert callable(PriorityItem.__init__)


def test_priorityitem_constructor_args():
    sig = inspect.signature(PriorityItem.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::global::defaultitem_is_not_abstract():
    assert not inspect.isabstract(uppaal::global::DefaultItem)


def test_uppaal::global::defaultitem_constructor_exists():
    assert callable(uppaal::global::DefaultItem.__init__)


def test_uppaal::global::defaultitem_constructor_args():
    sig = inspect.signature(uppaal::global::DefaultItem.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::global::channelitem_is_not_abstract():
    assert not inspect.isabstract(uppaal::global::ChannelItem)


def test_uppaal::global::channelitem_constructor_exists():
    assert callable(uppaal::global::ChannelItem.__init__)


def test_uppaal::global::channelitem_constructor_args():
    sig = inspect.signature(uppaal::global::ChannelItem.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::global::priorityitem_is_not_abstract():
    assert not inspect.isabstract(uppaal::global::PriorityItem)


def test_uppaal::global::priorityitem_constructor_exists():
    assert callable(uppaal::global::PriorityItem.__init__)


def test_uppaal::global::priorityitem_constructor_args():
    sig = inspect.signature(uppaal::global::PriorityItem.__init__)
    params = list(sig.parameters.keys())



def test_global::priorityitem_is_not_abstract():
    assert not inspect.isabstract(global::PriorityItem)


def test_global::priorityitem_constructor_exists():
    assert callable(global::PriorityItem.__init__)


def test_global::priorityitem_constructor_args():
    sig = inspect.signature(global::PriorityItem.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::global::channelprioritygroup_is_not_abstract():
    assert not inspect.isabstract(uppaal::global::ChannelPriorityGroup)


def test_uppaal::global::channelprioritygroup_constructor_exists():
    assert callable(uppaal::global::ChannelPriorityGroup.__init__)


def test_uppaal::global::channelprioritygroup_constructor_args():
    sig = inspect.signature(uppaal::global::ChannelPriorityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::system::progressmeasure_is_not_abstract():
    assert not inspect.isabstract(uppaal::system::ProgressMeasure)


def test_uppaal::system::progressmeasure_constructor_exists():
    assert callable(uppaal::system::ProgressMeasure.__init__)


def test_uppaal::system::progressmeasure_constructor_args():
    sig = inspect.signature(uppaal::system::ProgressMeasure.__init__)
    params = list(sig.parameters.keys())



def test_abstracttemplate_is_not_abstract():
    assert not inspect.isabstract(AbstractTemplate)


def test_abstracttemplate_constructor_exists():
    assert callable(AbstractTemplate.__init__)


def test_abstracttemplate_constructor_args():
    sig = inspect.signature(AbstractTemplate.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::templates::redefinedtemplate_is_not_abstract():
    assert not inspect.isabstract(uppaal::templates::RedefinedTemplate)


def test_uppaal::templates::redefinedtemplate_constructor_exists():
    assert callable(uppaal::templates::RedefinedTemplate.__init__)


def test_uppaal::templates::redefinedtemplate_constructor_args():
    sig = inspect.signature(uppaal::templates::RedefinedTemplate.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::templates::template_is_not_abstract():
    assert not inspect.isabstract(uppaal::templates::Template)


def test_uppaal::templates::template_constructor_exists():
    assert callable(uppaal::templates::Template.__init__)


def test_uppaal::templates::template_constructor_args():
    sig = inspect.signature(uppaal::templates::Template.__init__)
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



def test_uppaal::declarations::initializer_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::Initializer)


def test_uppaal::declarations::initializer_constructor_exists():
    assert callable(uppaal::declarations::Initializer.__init__)


def test_uppaal::declarations::initializer_constructor_args():
    sig = inspect.signature(uppaal::declarations::Initializer.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
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



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::typedelementcontainer_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::TypedElementContainer)


def test_uppaal::declarations::typedelementcontainer_constructor_exists():
    assert callable(uppaal::declarations::TypedElementContainer.__init__)


def test_uppaal::declarations::typedelementcontainer_constructor_args():
    sig = inspect.signature(uppaal::declarations::TypedElementContainer.__init__)
    params = list(sig.parameters.keys())



def test_global::channelprioritygroup_is_not_abstract():
    assert not inspect.isabstract(global::ChannelPriorityGroup)


def test_global::channelprioritygroup_constructor_exists():
    assert callable(global::ChannelPriorityGroup.__init__)


def test_global::channelprioritygroup_constructor_args():
    sig = inspect.signature(global::ChannelPriorityGroup.__init__)
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



def test_declarations::typedelementcontainer_is_not_abstract():
    assert not inspect.isabstract(declarations::TypedElementContainer)


def test_declarations::typedelementcontainer_constructor_exists():
    assert callable(declarations::TypedElementContainer.__init__)


def test_declarations::typedelementcontainer_constructor_args():
    sig = inspect.signature(declarations::TypedElementContainer.__init__)
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



def test_uppaal::statements::iteration_is_not_abstract():
    assert not inspect.isabstract(uppaal::statements::Iteration)


def test_uppaal::statements::iteration_constructor_exists():
    assert callable(uppaal::statements::Iteration.__init__)


def test_uppaal::statements::iteration_constructor_args():
    sig = inspect.signature(uppaal::statements::Iteration.__init__)
    params = list(sig.parameters.keys())



def test_declarations::declaration_is_not_abstract():
    assert not inspect.isabstract(declarations::Declaration)


def test_declarations::declaration_constructor_exists():
    assert callable(declarations::Declaration.__init__)


def test_declarations::declaration_constructor_args():
    sig = inspect.signature(declarations::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::TypedDeclaration)


def test_uppaal::declarations::typeddeclaration_constructor_exists():
    assert callable(uppaal::declarations::TypedDeclaration.__init__)


def test_uppaal::declarations::typeddeclaration_constructor_args():
    sig = inspect.signature(uppaal::declarations::TypedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_declaredtype_is_not_abstract():
    assert not inspect.isabstract(DeclaredType)


def test_declaredtype_constructor_exists():
    assert callable(DeclaredType.__init__)


def test_declaredtype_constructor_args():
    sig = inspect.signature(DeclaredType.__init__)
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



def test_global::channelprioritydeclaration_is_not_abstract():
    assert not inspect.isabstract(global::ChannelPriorityDeclaration)


def test_global::channelprioritydeclaration_constructor_exists():
    assert callable(global::ChannelPriorityDeclaration.__init__)


def test_global::channelprioritydeclaration_constructor_args():
    sig = inspect.signature(global::ChannelPriorityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_parametercontainer_is_not_abstract():
    assert not inspect.isabstract(ParameterContainer)


def test_parametercontainer_constructor_exists():
    assert callable(ParameterContainer.__init__)


def test_parametercontainer_constructor_args():
    sig = inspect.signature(ParameterContainer.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_core::typedelement_is_not_abstract():
    assert not inspect.isabstract(core::TypedElement)


def test_core::typedelement_constructor_exists():
    assert callable(core::TypedElement.__init__)


def test_core::typedelement_constructor_args():
    sig = inspect.signature(core::TypedElement.__init__)
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



def test_typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(TypedDeclaration)


def test_typeddeclaration_constructor_exists():
    assert callable(TypedDeclaration.__init__)


def test_typeddeclaration_constructor_args():
    sig = inspect.signature(TypedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_typeexpression_is_not_abstract():
    assert not inspect.isabstract(TypeExpression)


def test_typeexpression_constructor_exists():
    assert callable(TypeExpression.__init__)


def test_typeexpression_constructor_args():
    sig = inspect.signature(TypeExpression.__init__)
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



def test_uppaal::types::scalartypespecification_is_not_abstract():
    assert not inspect.isabstract(uppaal::types::ScalarTypeSpecification)


def test_uppaal::types::scalartypespecification_constructor_exists():
    assert callable(uppaal::types::ScalarTypeSpecification.__init__)


def test_uppaal::types::scalartypespecification_constructor_args():
    sig = inspect.signature(uppaal::types::ScalarTypeSpecification.__init__)
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



def test_uppaal::global::channelprioritydeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal::global::ChannelPriorityDeclaration)


def test_uppaal::global::channelprioritydeclaration_constructor_exists():
    assert callable(uppaal::global::ChannelPriorityDeclaration.__init__)


def test_uppaal::global::channelprioritydeclaration_constructor_args():
    sig = inspect.signature(uppaal::global::ChannelPriorityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::TypeDeclaration)


def test_uppaal::declarations::typedeclaration_constructor_exists():
    assert callable(uppaal::declarations::TypeDeclaration.__init__)


def test_uppaal::declarations::typedeclaration_constructor_args():
    sig = inspect.signature(uppaal::declarations::TypeDeclaration.__init__)
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



def test_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(PredefinedType)


def test_predefinedtype_constructor_exists():
    assert callable(PredefinedType.__init__)


def test_predefinedtype_constructor_args():
    sig = inspect.signature(PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::types::library_is_not_abstract():
    assert not inspect.isabstract(uppaal::types::Library)


def test_uppaal::types::library_constructor_exists():
    assert callable(uppaal::types::Library.__init__)


def test_uppaal::types::library_constructor_args():
    sig = inspect.signature(uppaal::types::Library.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::templates::abstracttemplate_is_not_abstract():
    assert not inspect.isabstract(uppaal::templates::AbstractTemplate)


def test_uppaal::templates::abstracttemplate_constructor_exists():
    assert callable(uppaal::templates::AbstractTemplate.__init__)


def test_uppaal::templates::abstracttemplate_constructor_args():
    sig = inspect.signature(uppaal::templates::AbstractTemplate.__init__)
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



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::BinaryExpression)


def test_uppaal::expressions::binaryexpression_constructor_exists():
    assert callable(uppaal::expressions::BinaryExpression.__init__)


def test_uppaal::expressions::binaryexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::dataprefixexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::DataPrefixExpression)


def test_uppaal::expressions::dataprefixexpression_constructor_exists():
    assert callable(uppaal::expressions::DataPrefixExpression.__init__)


def test_uppaal::expressions::dataprefixexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::DataPrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_uppaal::expressions::dataprefixexpression_has_prefix():
    assert hasattr(uppaal::expressions::DataPrefixExpression, "prefix")
    descriptor = None
    for klass in uppaal::expressions::DataPrefixExpression.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



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



def test_uppaal::expressions::functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::FunctionCallExpression)


def test_uppaal::expressions::functioncallexpression_constructor_exists():
    assert callable(uppaal::expressions::FunctionCallExpression.__init__)


def test_uppaal::expressions::functioncallexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::incrementdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::IncrementDecrementExpression)


def test_uppaal::expressions::incrementdecrementexpression_constructor_exists():
    assert callable(uppaal::expressions::IncrementDecrementExpression.__init__)


def test_uppaal::expressions::incrementdecrementexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::IncrementDecrementExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal::expressions::incrementdecrementexpression_has_operator():
    assert hasattr(uppaal::expressions::IncrementDecrementExpression, "operator")
    descriptor = None
    for klass in uppaal::expressions::IncrementDecrementExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::expressions::channelprefixexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::ChannelPrefixExpression)


def test_uppaal::expressions::channelprefixexpression_constructor_exists():
    assert callable(uppaal::expressions::ChannelPrefixExpression.__init__)


def test_uppaal::expressions::channelprefixexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::ChannelPrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "urgent" in params, "Missing parameter 'urgent'"
    assert "broadcast" in params, "Missing parameter 'broadcast'"

def test_uppaal::expressions::channelprefixexpression_has_urgent():
    assert hasattr(uppaal::expressions::ChannelPrefixExpression, "urgent")
    descriptor = None
    for klass in uppaal::expressions::ChannelPrefixExpression.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::expressions::channelprefixexpression_has_broadcast():
    assert hasattr(uppaal::expressions::ChannelPrefixExpression, "broadcast")
    descriptor = None
    for klass in uppaal::expressions::ChannelPrefixExpression.__mro__:
        if "broadcast" in klass.__dict__:
            descriptor = klass.__dict__["broadcast"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::types::typeexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::types::TypeExpression)


def test_uppaal::types::typeexpression_constructor_exists():
    assert callable(uppaal::types::TypeExpression.__init__)


def test_uppaal::types::typeexpression_constructor_args():
    sig = inspect.signature(uppaal::types::TypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::plusexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::PlusExpression)


def test_uppaal::expressions::plusexpression_constructor_exists():
    assert callable(uppaal::expressions::PlusExpression.__init__)


def test_uppaal::expressions::plusexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::PlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::minusexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::MinusExpression)


def test_uppaal::expressions::minusexpression_constructor_exists():
    assert callable(uppaal::expressions::MinusExpression.__init__)


def test_uppaal::expressions::minusexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::MinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::expressions::conditionexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::ConditionExpression)


def test_uppaal::expressions::conditionexpression_constructor_exists():
    assert callable(uppaal::expressions::ConditionExpression.__init__)


def test_uppaal::expressions::conditionexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::ConditionExpression.__init__)
    params = list(sig.parameters.keys())



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



def test_uppaal::expressions::identifierexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal::expressions::IdentifierExpression)


def test_uppaal::expressions::identifierexpression_constructor_exists():
    assert callable(uppaal::expressions::IdentifierExpression.__init__)


def test_uppaal::expressions::identifierexpression_constructor_args():
    sig = inspect.signature(uppaal::expressions::IdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_typedelementcontainer_is_not_abstract():
    assert not inspect.isabstract(TypedElementContainer)


def test_typedelementcontainer_constructor_exists():
    assert callable(TypedElementContainer.__init__)


def test_typedelementcontainer_constructor_args():
    sig = inspect.signature(TypedElementContainer.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::templates::selection_is_not_abstract():
    assert not inspect.isabstract(uppaal::templates::Selection)


def test_uppaal::templates::selection_constructor_exists():
    assert callable(uppaal::templates::Selection.__init__)


def test_uppaal::templates::selection_constructor_args():
    sig = inspect.signature(uppaal::templates::Selection.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::declarations::parametercontainer_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::ParameterContainer)


def test_uppaal::declarations::parametercontainer_constructor_exists():
    assert callable(uppaal::declarations::ParameterContainer.__init__)


def test_uppaal::declarations::parametercontainer_constructor_args():
    sig = inspect.signature(uppaal::declarations::ParameterContainer.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::core::typedelement_is_not_abstract():
    assert not inspect.isabstract(uppaal::core::TypedElement)


def test_uppaal::core::typedelement_constructor_exists():
    assert callable(uppaal::core::TypedElement.__init__)


def test_uppaal::core::typedelement_constructor_args():
    sig = inspect.signature(uppaal::core::TypedElement.__init__)
    params = list(sig.parameters.keys())



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



def test_uppaal::declarations::function_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::Function)


def test_uppaal::declarations::function_constructor_exists():
    assert callable(uppaal::declarations::Function.__init__)


def test_uppaal::declarations::function_constructor_args():
    sig = inspect.signature(uppaal::declarations::Function.__init__)
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



def test_uppaal::declarations::variable_is_not_abstract():
    assert not inspect.isabstract(uppaal::declarations::Variable)


def test_uppaal::declarations::variable_constructor_exists():
    assert callable(uppaal::declarations::Variable.__init__)


def test_uppaal::declarations::variable_constructor_args():
    sig = inspect.signature(uppaal::declarations::Variable.__init__)
    params = list(sig.parameters.keys())



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
        "CALL_BY_REFERENCE",
        "CALL_BY_VALUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallType"

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

def test_compareoperator_exists():
    # Check that the Enumeration exists
    assert CompareOperator is not None

def test_compareoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CompareOperator]
    expected_literals = [
        "GREATER",
        "EQUAL",
        "LESS",
        "UNEQUAL",
        "GREATER_OR_EQUAL",
        "LESS_OR_EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CompareOperator"

def test_minmaxoperator_exists():
    # Check that the Enumeration exists
    assert MinMaxOperator is not None

def test_minmaxoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MinMaxOperator]
    expected_literals = [
        "MAX",
        "MIN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MinMaxOperator"

def test_locationkind_exists():
    # Check that the Enumeration exists
    assert LocationKind is not None

def test_locationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LocationKind]
    expected_literals = [
        "URGENT",
        "NORMAL",
        "COMMITED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LocationKind"

def test_datavariableprefix_exists():
    # Check that the Enumeration exists
    assert DataVariablePrefix is not None

def test_datavariableprefix_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataVariablePrefix]
    expected_literals = [
        "CONST",
        "META",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataVariablePrefix"

def test_builtintype_exists():
    # Check that the Enumeration exists
    assert BuiltInType is not None

def test_builtintype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltInType]
    expected_literals = [
        "VOID",
        "INT",
        "CLOCK",
        "CHAN",
        "BOOL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInType"

def test_bitshiftoperator_exists():
    # Check that the Enumeration exists
    assert BitShiftOperator is not None

def test_bitshiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BitShiftOperator]
    expected_literals = [
        "LEFT",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BitShiftOperator"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "DIVIDE_EQUAL",
        "BIT_OR_EQUAL",
        "BIT_LEFT_EQUAL",
        "TIMES_EQUAL",
        "PLUS_EQUAL",
        "EQUAL",
        "MINUS_EQUAL",
        "BIT_XOR_EQUAL",
        "BIT_AND_EQUAL",
        "MODULO_EQUAL",
        "BIT_RIGHT_EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_bitwiseoperator_exists():
    # Check that the Enumeration exists
    assert BitwiseOperator is not None

def test_bitwiseoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BitwiseOperator]
    expected_literals = [
        "AND",
        "OR",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BitwiseOperator"

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "ADD",
        "SUBTRACT",
        "DIVIDE",
        "MODULO",
        "MULTIPLICATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "AND",
        "OR",
        "IMPLY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"

def test_synchronizationkind_exists():
    # Check that the Enumeration exists
    assert SynchronizationKind is not None

def test_synchronizationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SynchronizationKind]
    expected_literals = [
        "SEND",
        "RECEIVE",
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
        safe_text
)
IncrementDecrementExpression_strategy = st.builds(
    IncrementDecrementExpression,
)
uppaal::expressions::PostIncrementDecrementExpression_strategy = st.builds(
    uppaal::expressions::PostIncrementDecrementExpression,
)
uppaal::expressions::PreIncrementDecrementExpression_strategy = st.builds(
    uppaal::expressions::PreIncrementDecrementExpression,
)
expressions::Expression_strategy = st.builds(
    expressions::Expression,
)
Function_strategy = st.builds(
    Function,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
uppaal::expressions::CompareExpression_strategy = st.builds(
    uppaal::expressions::CompareExpression,
    operator=
        safe_text
)
uppaal::expressions::MinMaxExpression_strategy = st.builds(
    uppaal::expressions::MinMaxExpression,
    operator=
        safe_text
)
uppaal::expressions::BitwiseExpression_strategy = st.builds(
    uppaal::expressions::BitwiseExpression,
    operator=
        safe_text
)
uppaal::expressions::BitShiftExpression_strategy = st.builds(
    uppaal::expressions::BitShiftExpression,
    operator=
        safe_text
)
uppaal::expressions::LogicalExpression_strategy = st.builds(
    uppaal::expressions::LogicalExpression,
    operator=
        safe_text
)
uppaal::expressions::ArithmeticExpression_strategy = st.builds(
    uppaal::expressions::ArithmeticExpression,
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
Statement_strategy = st.builds(
    Statement,
)
uppaal::statements::ForLoop_strategy = st.builds(
    uppaal::statements::ForLoop,
)
uppaal::statements::IfStatement_strategy = st.builds(
    uppaal::statements::IfStatement,
)
uppaal::statements::DoWhileLoop_strategy = st.builds(
    uppaal::statements::DoWhileLoop,
)
uppaal::statements::WhileLoop_strategy = st.builds(
    uppaal::statements::WhileLoop,
)
uppaal::statements::ExpressionStatement_strategy = st.builds(
    uppaal::statements::ExpressionStatement,
)
uppaal::statements::EmptyStatement_strategy = st.builds(
    uppaal::statements::EmptyStatement,
)
uppaal::statements::ReturnStatement_strategy = st.builds(
    uppaal::statements::ReturnStatement,
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
Selection_strategy = st.builds(
    Selection,
)
Synchronization_strategy = st.builds(
    Synchronization,
)
Location_strategy = st.builds(
    Location,
)
LocalDeclarations_strategy = st.builds(
    LocalDeclarations,
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
Edge_strategy = st.builds(
    Edge,
)
RedefinedTemplate_strategy = st.builds(
    RedefinedTemplate,
)
IdentifierExpression_strategy = st.builds(
    IdentifierExpression,
)
PriorityItem_strategy = st.builds(
    PriorityItem,
)
uppaal::global::DefaultItem_strategy = st.builds(
    uppaal::global::DefaultItem,
)
uppaal::global::ChannelItem_strategy = st.builds(
    uppaal::global::ChannelItem,
)
uppaal::global::PriorityItem_strategy = st.builds(
    uppaal::global::PriorityItem,
)
global::PriorityItem_strategy = st.builds(
    global::PriorityItem,
)
uppaal::global::ChannelPriorityGroup_strategy = st.builds(
    uppaal::global::ChannelPriorityGroup,
)
uppaal::system::ProgressMeasure_strategy = st.builds(
    uppaal::system::ProgressMeasure,
)
AbstractTemplate_strategy = st.builds(
    AbstractTemplate,
)
uppaal::templates::RedefinedTemplate_strategy = st.builds(
    uppaal::templates::RedefinedTemplate,
)
uppaal::templates::Template_strategy = st.builds(
    uppaal::templates::Template,
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
uppaal::declarations::Initializer_strategy = st.builds(
    uppaal::declarations::Initializer,
)
Variable_strategy = st.builds(
    Variable,
)
uppaal::declarations::Parameter_strategy = st.builds(
    uppaal::declarations::Parameter,
    callType=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
uppaal::declarations::TypedElementContainer_strategy = st.builds(
    uppaal::declarations::TypedElementContainer,
)
global::ChannelPriorityGroup_strategy = st.builds(
    global::ChannelPriorityGroup,
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
declarations::TypedElementContainer_strategy = st.builds(
    declarations::TypedElementContainer,
)
uppaal::expressions::QuantificationExpression_strategy = st.builds(
    uppaal::expressions::QuantificationExpression,
    quantifier=
        safe_text
)
uppaal::statements::Iteration_strategy = st.builds(
    uppaal::statements::Iteration,
)
declarations::Declaration_strategy = st.builds(
    declarations::Declaration,
)
uppaal::declarations::TypedDeclaration_strategy = st.builds(
    uppaal::declarations::TypedDeclaration,
)
DeclaredType_strategy = st.builds(
    DeclaredType,
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
global::ChannelPriorityDeclaration_strategy = st.builds(
    global::ChannelPriorityDeclaration,
)
ParameterContainer_strategy = st.builds(
    ParameterContainer,
)
Block_strategy = st.builds(
    Block,
)
core::TypedElement_strategy = st.builds(
    core::TypedElement,
)
uppaal::types::IntegerBounds_strategy = st.builds(
    uppaal::types::IntegerBounds,
)
IntegerBounds_strategy = st.builds(
    IntegerBounds,
)
TypedDeclaration_strategy = st.builds(
    TypedDeclaration,
)
TypeExpression_strategy = st.builds(
    TypeExpression,
)
uppaal::types::StructTypeSpecification_strategy = st.builds(
    uppaal::types::StructTypeSpecification,
)
uppaal::types::RangeTypeSpecification_strategy = st.builds(
    uppaal::types::RangeTypeSpecification,
)
uppaal::types::ScalarTypeSpecification_strategy = st.builds(
    uppaal::types::ScalarTypeSpecification,
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
uppaal::global::ChannelPriorityDeclaration_strategy = st.builds(
    uppaal::global::ChannelPriorityDeclaration,
)
uppaal::declarations::TypeDeclaration_strategy = st.builds(
    uppaal::declarations::TypeDeclaration,
)
uppaal::system::TemplateDeclaration_strategy = st.builds(
    uppaal::system::TemplateDeclaration,
)
uppaal::declarations::Declarations_strategy = st.builds(
    uppaal::declarations::Declarations,
)
PredefinedType_strategy = st.builds(
    PredefinedType,
)
uppaal::types::Library_strategy = st.builds(
    uppaal::types::Library,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uppaal::templates::AbstractTemplate_strategy = st.builds(
    uppaal::templates::AbstractTemplate,
)
uppaal::types::Type_strategy = st.builds(
    uppaal::types::Type,
    baseType=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
uppaal::expressions::BinaryExpression_strategy = st.builds(
    uppaal::expressions::BinaryExpression,
)
uppaal::expressions::DataPrefixExpression_strategy = st.builds(
    uppaal::expressions::DataPrefixExpression,
    prefix=
        safe_text
)
uppaal::expressions::LiteralExpression_strategy = st.builds(
    uppaal::expressions::LiteralExpression,
    text=
        safe_text
)
uppaal::expressions::FunctionCallExpression_strategy = st.builds(
    uppaal::expressions::FunctionCallExpression,
)
uppaal::expressions::IncrementDecrementExpression_strategy = st.builds(
    uppaal::expressions::IncrementDecrementExpression,
    operator=
        safe_text
)
uppaal::expressions::ChannelPrefixExpression_strategy = st.builds(
    uppaal::expressions::ChannelPrefixExpression,
    urgent=
        st.booleans(),
    broadcast=
        st.booleans()
)
uppaal::types::TypeExpression_strategy = st.builds(
    uppaal::types::TypeExpression,
)
uppaal::expressions::PlusExpression_strategy = st.builds(
    uppaal::expressions::PlusExpression,
)
uppaal::expressions::MinusExpression_strategy = st.builds(
    uppaal::expressions::MinusExpression,
)
uppaal::expressions::ConditionExpression_strategy = st.builds(
    uppaal::expressions::ConditionExpression,
)
uppaal::expressions::NegationExpression_strategy = st.builds(
    uppaal::expressions::NegationExpression,
)
uppaal::expressions::ScopedIdentifierExpression_strategy = st.builds(
    uppaal::expressions::ScopedIdentifierExpression,
)
uppaal::expressions::IdentifierExpression_strategy = st.builds(
    uppaal::expressions::IdentifierExpression,
)
TypedElementContainer_strategy = st.builds(
    TypedElementContainer,
)
uppaal::templates::Selection_strategy = st.builds(
    uppaal::templates::Selection,
)
uppaal::declarations::ParameterContainer_strategy = st.builds(
    uppaal::declarations::ParameterContainer,
)
uppaal::core::TypedElement_strategy = st.builds(
    uppaal::core::TypedElement,
)
uppaal::core::CommentableElement_strategy = st.builds(
    uppaal::core::CommentableElement,
    comment=
        safe_text
)
uppaal::core::NamedElement_strategy = st.builds(
    uppaal::core::NamedElement,
    name=
        safe_text
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
core::CommentableElement_strategy = st.builds(
    core::CommentableElement,
)
uppaal::templates::Edge_strategy = st.builds(
    uppaal::templates::Edge,
)
core::NamedElement_strategy = st.builds(
    core::NamedElement,
)
uppaal::declarations::Function_strategy = st.builds(
    uppaal::declarations::Function,
)
uppaal::templates::Location_strategy = st.builds(
    uppaal::templates::Location,
    locationTimeKind=
        safe_text
)
uppaal::declarations::Variable_strategy = st.builds(
    uppaal::declarations::Variable,
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

@given(instance=IncrementDecrementExpression_strategy)
@settings(max_examples=50)
def test_incrementdecrementexpression_instantiation(instance):
    assert isinstance(instance, IncrementDecrementExpression)

@given(instance=uppaal::expressions::PostIncrementDecrementExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::postincrementdecrementexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::PostIncrementDecrementExpression)

@given(instance=uppaal::expressions::PreIncrementDecrementExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::preincrementdecrementexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::PreIncrementDecrementExpression)

@given(instance=expressions::Expression_strategy)
@settings(max_examples=50)
def test_expressions::expression_instantiation(instance):
    assert isinstance(instance, expressions::Expression)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

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

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=uppaal::statements::ForLoop_strategy)
@settings(max_examples=50)
def test_uppaal::statements::forloop_instantiation(instance):
    assert isinstance(instance, uppaal::statements::ForLoop)

@given(instance=uppaal::statements::IfStatement_strategy)
@settings(max_examples=50)
def test_uppaal::statements::ifstatement_instantiation(instance):
    assert isinstance(instance, uppaal::statements::IfStatement)

@given(instance=uppaal::statements::DoWhileLoop_strategy)
@settings(max_examples=50)
def test_uppaal::statements::dowhileloop_instantiation(instance):
    assert isinstance(instance, uppaal::statements::DoWhileLoop)

@given(instance=uppaal::statements::WhileLoop_strategy)
@settings(max_examples=50)
def test_uppaal::statements::whileloop_instantiation(instance):
    assert isinstance(instance, uppaal::statements::WhileLoop)

@given(instance=uppaal::statements::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_uppaal::statements::expressionstatement_instantiation(instance):
    assert isinstance(instance, uppaal::statements::ExpressionStatement)

@given(instance=uppaal::statements::EmptyStatement_strategy)
@settings(max_examples=50)
def test_uppaal::statements::emptystatement_instantiation(instance):
    assert isinstance(instance, uppaal::statements::EmptyStatement)

@given(instance=uppaal::statements::ReturnStatement_strategy)
@settings(max_examples=50)
def test_uppaal::statements::returnstatement_instantiation(instance):
    assert isinstance(instance, uppaal::statements::ReturnStatement)

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

@given(instance=Selection_strategy)
@settings(max_examples=50)
def test_selection_instantiation(instance):
    assert isinstance(instance, Selection)

@given(instance=Synchronization_strategy)
@settings(max_examples=50)
def test_synchronization_instantiation(instance):
    assert isinstance(instance, Synchronization)

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)

@given(instance=LocalDeclarations_strategy)
@settings(max_examples=50)
def test_localdeclarations_instantiation(instance):
    assert isinstance(instance, LocalDeclarations)

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

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=RedefinedTemplate_strategy)
@settings(max_examples=50)
def test_redefinedtemplate_instantiation(instance):
    assert isinstance(instance, RedefinedTemplate)

@given(instance=IdentifierExpression_strategy)
@settings(max_examples=50)
def test_identifierexpression_instantiation(instance):
    assert isinstance(instance, IdentifierExpression)

@given(instance=PriorityItem_strategy)
@settings(max_examples=50)
def test_priorityitem_instantiation(instance):
    assert isinstance(instance, PriorityItem)

@given(instance=uppaal::global::DefaultItem_strategy)
@settings(max_examples=50)
def test_uppaal::global::defaultitem_instantiation(instance):
    assert isinstance(instance, uppaal::global::DefaultItem)

@given(instance=uppaal::global::ChannelItem_strategy)
@settings(max_examples=50)
def test_uppaal::global::channelitem_instantiation(instance):
    assert isinstance(instance, uppaal::global::ChannelItem)

@given(instance=uppaal::global::PriorityItem_strategy)
@settings(max_examples=50)
def test_uppaal::global::priorityitem_instantiation(instance):
    assert isinstance(instance, uppaal::global::PriorityItem)

@given(instance=global::PriorityItem_strategy)
@settings(max_examples=50)
def test_global::priorityitem_instantiation(instance):
    assert isinstance(instance, global::PriorityItem)

@given(instance=uppaal::global::ChannelPriorityGroup_strategy)
@settings(max_examples=50)
def test_uppaal::global::channelprioritygroup_instantiation(instance):
    assert isinstance(instance, uppaal::global::ChannelPriorityGroup)

@given(instance=uppaal::system::ProgressMeasure_strategy)
@settings(max_examples=50)
def test_uppaal::system::progressmeasure_instantiation(instance):
    assert isinstance(instance, uppaal::system::ProgressMeasure)

@given(instance=AbstractTemplate_strategy)
@settings(max_examples=50)
def test_abstracttemplate_instantiation(instance):
    assert isinstance(instance, AbstractTemplate)

@given(instance=uppaal::templates::RedefinedTemplate_strategy)
@settings(max_examples=50)
def test_uppaal::templates::redefinedtemplate_instantiation(instance):
    assert isinstance(instance, uppaal::templates::RedefinedTemplate)

@given(instance=uppaal::templates::Template_strategy)
@settings(max_examples=50)
def test_uppaal::templates::template_instantiation(instance):
    assert isinstance(instance, uppaal::templates::Template)

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

@given(instance=uppaal::declarations::Initializer_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::initializer_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::Initializer)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

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

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=uppaal::declarations::TypedElementContainer_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::typedelementcontainer_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::TypedElementContainer)

@given(instance=global::ChannelPriorityGroup_strategy)
@settings(max_examples=50)
def test_global::channelprioritygroup_instantiation(instance):
    assert isinstance(instance, global::ChannelPriorityGroup)

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

@given(instance=declarations::TypedElementContainer_strategy)
@settings(max_examples=50)
def test_declarations::typedelementcontainer_instantiation(instance):
    assert isinstance(instance, declarations::TypedElementContainer)

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

@given(instance=uppaal::statements::Iteration_strategy)
@settings(max_examples=50)
def test_uppaal::statements::iteration_instantiation(instance):
    assert isinstance(instance, uppaal::statements::Iteration)

@given(instance=declarations::Declaration_strategy)
@settings(max_examples=50)
def test_declarations::declaration_instantiation(instance):
    assert isinstance(instance, declarations::Declaration)

@given(instance=uppaal::declarations::TypedDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::typeddeclaration_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::TypedDeclaration)

@given(instance=DeclaredType_strategy)
@settings(max_examples=50)
def test_declaredtype_instantiation(instance):
    assert isinstance(instance, DeclaredType)

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

@given(instance=global::ChannelPriorityDeclaration_strategy)
@settings(max_examples=50)
def test_global::channelprioritydeclaration_instantiation(instance):
    assert isinstance(instance, global::ChannelPriorityDeclaration)

@given(instance=ParameterContainer_strategy)
@settings(max_examples=50)
def test_parametercontainer_instantiation(instance):
    assert isinstance(instance, ParameterContainer)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=core::TypedElement_strategy)
@settings(max_examples=50)
def test_core::typedelement_instantiation(instance):
    assert isinstance(instance, core::TypedElement)

@given(instance=uppaal::types::IntegerBounds_strategy)
@settings(max_examples=50)
def test_uppaal::types::integerbounds_instantiation(instance):
    assert isinstance(instance, uppaal::types::IntegerBounds)

@given(instance=IntegerBounds_strategy)
@settings(max_examples=50)
def test_integerbounds_instantiation(instance):
    assert isinstance(instance, IntegerBounds)

@given(instance=TypedDeclaration_strategy)
@settings(max_examples=50)
def test_typeddeclaration_instantiation(instance):
    assert isinstance(instance, TypedDeclaration)

@given(instance=TypeExpression_strategy)
@settings(max_examples=50)
def test_typeexpression_instantiation(instance):
    assert isinstance(instance, TypeExpression)

@given(instance=uppaal::types::StructTypeSpecification_strategy)
@settings(max_examples=50)
def test_uppaal::types::structtypespecification_instantiation(instance):
    assert isinstance(instance, uppaal::types::StructTypeSpecification)

@given(instance=uppaal::types::RangeTypeSpecification_strategy)
@settings(max_examples=50)
def test_uppaal::types::rangetypespecification_instantiation(instance):
    assert isinstance(instance, uppaal::types::RangeTypeSpecification)

@given(instance=uppaal::types::ScalarTypeSpecification_strategy)
@settings(max_examples=50)
def test_uppaal::types::scalartypespecification_instantiation(instance):
    assert isinstance(instance, uppaal::types::ScalarTypeSpecification)

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

@given(instance=uppaal::global::ChannelPriorityDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal::global::channelprioritydeclaration_instantiation(instance):
    assert isinstance(instance, uppaal::global::ChannelPriorityDeclaration)

@given(instance=uppaal::declarations::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::typedeclaration_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::TypeDeclaration)

@given(instance=uppaal::system::TemplateDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal::system::templatedeclaration_instantiation(instance):
    assert isinstance(instance, uppaal::system::TemplateDeclaration)

@given(instance=uppaal::declarations::Declarations_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::declarations_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::Declarations)

@given(instance=PredefinedType_strategy)
@settings(max_examples=50)
def test_predefinedtype_instantiation(instance):
    assert isinstance(instance, PredefinedType)

@given(instance=uppaal::types::Library_strategy)
@settings(max_examples=50)
def test_uppaal::types::library_instantiation(instance):
    assert isinstance(instance, uppaal::types::Library)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uppaal::templates::AbstractTemplate_strategy)
@settings(max_examples=50)
def test_uppaal::templates::abstracttemplate_instantiation(instance):
    assert isinstance(instance, uppaal::templates::AbstractTemplate)

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

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=uppaal::expressions::BinaryExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::binaryexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::BinaryExpression)

@given(instance=uppaal::expressions::DataPrefixExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::dataprefixexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::DataPrefixExpression)

@given(instance=uppaal::expressions::DataPrefixExpression_strategy)
def test_uppaal::expressions::dataprefixexpression_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=uppaal::expressions::DataPrefixExpression_strategy)
def test_uppaal::expressions::dataprefixexpression_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

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

@given(instance=uppaal::expressions::FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::functioncallexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::FunctionCallExpression)

@given(instance=uppaal::expressions::IncrementDecrementExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::incrementdecrementexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::IncrementDecrementExpression)

@given(instance=uppaal::expressions::IncrementDecrementExpression_strategy)
def test_uppaal::expressions::incrementdecrementexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=uppaal::expressions::IncrementDecrementExpression_strategy)
def test_uppaal::expressions::incrementdecrementexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal::expressions::ChannelPrefixExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::channelprefixexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::ChannelPrefixExpression)

@given(instance=uppaal::expressions::ChannelPrefixExpression_strategy)
def test_uppaal::expressions::channelprefixexpression_urgent_type(instance):
    assert isinstance(instance.urgent, bool)


@given(instance=uppaal::expressions::ChannelPrefixExpression_strategy)
def test_uppaal::expressions::channelprefixexpression_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original

@given(instance=uppaal::expressions::ChannelPrefixExpression_strategy)
def test_uppaal::expressions::channelprefixexpression_broadcast_type(instance):
    assert isinstance(instance.broadcast, bool)


@given(instance=uppaal::expressions::ChannelPrefixExpression_strategy)
def test_uppaal::expressions::channelprefixexpression_broadcast_setter(instance):
    original = instance.broadcast
    instance.broadcast = original
    assert instance.broadcast == original

@given(instance=uppaal::types::TypeExpression_strategy)
@settings(max_examples=50)
def test_uppaal::types::typeexpression_instantiation(instance):
    assert isinstance(instance, uppaal::types::TypeExpression)

@given(instance=uppaal::expressions::PlusExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::plusexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::PlusExpression)

@given(instance=uppaal::expressions::MinusExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::minusexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::MinusExpression)

@given(instance=uppaal::expressions::ConditionExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::conditionexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::ConditionExpression)

@given(instance=uppaal::expressions::NegationExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::negationexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::NegationExpression)

@given(instance=uppaal::expressions::ScopedIdentifierExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::scopedidentifierexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::ScopedIdentifierExpression)

@given(instance=uppaal::expressions::IdentifierExpression_strategy)
@settings(max_examples=50)
def test_uppaal::expressions::identifierexpression_instantiation(instance):
    assert isinstance(instance, uppaal::expressions::IdentifierExpression)

@given(instance=TypedElementContainer_strategy)
@settings(max_examples=50)
def test_typedelementcontainer_instantiation(instance):
    assert isinstance(instance, TypedElementContainer)

@given(instance=uppaal::templates::Selection_strategy)
@settings(max_examples=50)
def test_uppaal::templates::selection_instantiation(instance):
    assert isinstance(instance, uppaal::templates::Selection)

@given(instance=uppaal::declarations::ParameterContainer_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::parametercontainer_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::ParameterContainer)

@given(instance=uppaal::core::TypedElement_strategy)
@settings(max_examples=50)
def test_uppaal::core::typedelement_instantiation(instance):
    assert isinstance(instance, uppaal::core::TypedElement)

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

@given(instance=uppaal::declarations::Function_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::function_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::Function)

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

@given(instance=uppaal::declarations::Variable_strategy)
@settings(max_examples=50)
def test_uppaal::declarations::variable_instantiation(instance):
    assert isinstance(instance, uppaal::declarations::Variable)

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
