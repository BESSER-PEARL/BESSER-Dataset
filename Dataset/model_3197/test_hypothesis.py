import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    expressions::Selection,
    timedAutomata::core::TemplateInstantiation,
    timedAutomata::core::System,
    System,
    timedAutomata::core::SimpleSystem,
    TemplateInstantiation,
    timedAutomata::core::SystemDefinition,
    core::timedAutomata::Label,
    base::Commentable,
    core::timedAutomata::Nail,
    Updates,
    Selections,
    Guards,
    Edge,
    core::timedAutomata::Parameter,
    Location,
    timedAutomata::core::ComplexSystem,
    SystemDefinition,
    Template,
    TAElement,
    timedAutomata::core::Project,
    declarations::FieldDeclaration,
    Type,
    timedAutomata::types::SimpleType,
    timedAutomata::types::Scalar,
    timedAutomata::types::Struct,
    timedAutomata::types::IntegerRange,
    timedAutomata::types::IdentifierType,
    timedAutomata::types::Type,
    base::Identifyable,
    base::Nameable,
    timedAutomata::core::TAElement,
    core::TAElement,
    timedAutomata::core::Template,
    timedAutomata::declarations::ChannelExpression,
    declarations::ChannelExpression,
    ChannelPriority,
    timedAutomata::declarations::ComplexChannelPriority,
    timedAutomata::declarations::SimpleChannelPriority,
    timedAutomata::declarations::DefaultChannelPriority,
    timedAutomata::declarations::ChannelPriority,
    ChannelExpression,
    timedAutomata::declarations::ExpressionChannelExpression,
    timedAutomata::declarations::IdentifierChannelExpression,
    Statement,
    timedAutomata::declarations::ForLoopStatement,
    timedAutomata::declarations::ReturnStatement,
    timedAutomata::declarations::WhileLoopStatement,
    timedAutomata::declarations::IfStatement,
    timedAutomata::declarations::DoWhileLoopStatement,
    timedAutomata::declarations::ExpressionStatement,
    timedAutomata::declarations::Statement,
    declarations::Statement,
    declarations::Declaration,
    timedAutomata::declarations::Block,
    TAParameter,
    timedAutomata::declarations::CallByReferenceParameter,
    timedAutomata::declarations::CallByValueParameter,
    timedAutomata::declarations::TAParameter,
    Initialiser,
    timedAutomata::declarations::ArrayInitialiser,
    timedAutomata::declarations::ExpressionInitialiser,
    timedAutomata::declarations::Initialiser,
    timedAutomata::declarations::IterationStatement,
    ArrayDeclarationType,
    timedAutomata::declarations::ArrayExpressionType,
    timedAutomata::declarations::ArrayDeclarationType,
    timedAutomata::declarations::ArrayDeclaration,
    timedAutomata::declarations::FieldDeclaration,
    declarations::ChannelPriority,
    declarations::Block,
    timedAutomata::declarations::BlockStatement,
    declarations::TAParameter,
    timedAutomata::declarations::ArrayTypeType,
    declarations::Initialiser,
    declarations::ArrayDeclarationType,
    timedAutomata::declarations::VariableIdentifier,
    declarations::VariableIdentifier,
    Declaration,
    timedAutomata::declarations::ChannelPriorityDeclaration,
    timedAutomata::declarations::VariableDeclaration,
    timedAutomata::expressions::Selection,
    types::Type,
    timedAutomata::declarations::FunctionDeclaration,
    declarations::ArrayDeclaration,
    timedAutomata::declarations::TypeDeclaration,
    Identifier,
    Synchronisation,
    timedAutomata::bnf::ReceiveSynchronisation,
    timedAutomata::bnf::SendSynchronisation,
    expressions::Expression,
    Expression,
    timedAutomata::expressions::IncDecExpression,
    timedAutomata::expressions::BinaryExpression,
    timedAutomata::expressions::FixedExpression,
    timedAutomata::expressions::AssignmentExpression,
    timedAutomata::expressions::IdentifierExpression,
    timedAutomata::expressions::SimpleIfExpression,
    timedAutomata::expressions::ArrayVariableExpression,
    timedAutomata::expressions::WithArgumentsExpression,
    timedAutomata::expressions::ForallExpression,
    timedAutomata::expressions::VariableExpression,
    timedAutomata::expressions::PointExpression,
    timedAutomata::expressions::GroupingExpression,
    timedAutomata::expressions::ExistsExpression,
    timedAutomata::expressions::UnaryExpression,
    timedAutomata::expressions::ConstantExpression,
    Commentable,
    timedAutomata::declarations::Declaration,
    timedAutomata::expressions::Expression,
    timedAutomata::base::Identifyable,
    timedAutomata::base::Commentable,
    Position,
    timedAutomata::core::Selections,
    timedAutomata::core::Edge,
    timedAutomata::core::Location,
    timedAutomata::core::Updates,
    timedAutomata::core::Guards,
    timedAutomata::bnf::Synchronisation,
    timedAutomata::bnf::Identifier,
    timedAutomata::base::Nameable,
    TypeId,
    PriorityOperator,
    FixedExpressionType,
    TypePrefix,
    UnaryOperator,
    BinaryOperator,
    AssignOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expressions::selection_is_not_abstract():
    assert not inspect.isabstract(expressions::Selection)


def test_expressions::selection_constructor_exists():
    assert callable(expressions::Selection.__init__)


def test_expressions::selection_constructor_args():
    sig = inspect.signature(expressions::Selection.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::core::templateinstantiation_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::core::TemplateInstantiation)


def test_timedautomata::core::templateinstantiation_constructor_exists():
    assert callable(timedAutomata::core::TemplateInstantiation.__init__)


def test_timedautomata::core::templateinstantiation_constructor_args():
    sig = inspect.signature(timedAutomata::core::TemplateInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::core::system_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::core::System)


def test_timedautomata::core::system_constructor_exists():
    assert callable(timedAutomata::core::System.__init__)


def test_timedautomata::core::system_constructor_args():
    sig = inspect.signature(timedAutomata::core::System.__init__)
    params = list(sig.parameters.keys())



def test_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_system_constructor_exists():
    assert callable(System.__init__)


def test_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::core::simplesystem_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::core::SimpleSystem)


def test_timedautomata::core::simplesystem_constructor_exists():
    assert callable(timedAutomata::core::SimpleSystem.__init__)


def test_timedautomata::core::simplesystem_constructor_args():
    sig = inspect.signature(timedAutomata::core::SimpleSystem.__init__)
    params = list(sig.parameters.keys())



def test_templateinstantiation_is_not_abstract():
    assert not inspect.isabstract(TemplateInstantiation)


def test_templateinstantiation_constructor_exists():
    assert callable(TemplateInstantiation.__init__)


def test_templateinstantiation_constructor_args():
    sig = inspect.signature(TemplateInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::core::systemdefinition_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::core::SystemDefinition)


def test_timedautomata::core::systemdefinition_constructor_exists():
    assert callable(timedAutomata::core::SystemDefinition.__init__)


def test_timedautomata::core::systemdefinition_constructor_args():
    sig = inspect.signature(timedAutomata::core::SystemDefinition.__init__)
    params = list(sig.parameters.keys())



def test_core::timedautomata::label_is_not_abstract():
    assert not inspect.isabstract(core::timedAutomata::Label)


def test_core::timedautomata::label_constructor_exists():
    assert callable(core::timedAutomata::Label.__init__)


def test_core::timedautomata::label_constructor_args():
    sig = inspect.signature(core::timedAutomata::Label.__init__)
    params = list(sig.parameters.keys())



def test_base::commentable_is_not_abstract():
    assert not inspect.isabstract(base::Commentable)


def test_base::commentable_constructor_exists():
    assert callable(base::Commentable.__init__)


def test_base::commentable_constructor_args():
    sig = inspect.signature(base::Commentable.__init__)
    params = list(sig.parameters.keys())



def test_core::timedautomata::nail_is_not_abstract():
    assert not inspect.isabstract(core::timedAutomata::Nail)


def test_core::timedautomata::nail_constructor_exists():
    assert callable(core::timedAutomata::Nail.__init__)


def test_core::timedautomata::nail_constructor_args():
    sig = inspect.signature(core::timedAutomata::Nail.__init__)
    params = list(sig.parameters.keys())



def test_updates_is_not_abstract():
    assert not inspect.isabstract(Updates)


def test_updates_constructor_exists():
    assert callable(Updates.__init__)


def test_updates_constructor_args():
    sig = inspect.signature(Updates.__init__)
    params = list(sig.parameters.keys())



def test_selections_is_not_abstract():
    assert not inspect.isabstract(Selections)


def test_selections_constructor_exists():
    assert callable(Selections.__init__)


def test_selections_constructor_args():
    sig = inspect.signature(Selections.__init__)
    params = list(sig.parameters.keys())



def test_guards_is_not_abstract():
    assert not inspect.isabstract(Guards)


def test_guards_constructor_exists():
    assert callable(Guards.__init__)


def test_guards_constructor_args():
    sig = inspect.signature(Guards.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_core::timedautomata::parameter_is_not_abstract():
    assert not inspect.isabstract(core::timedAutomata::Parameter)


def test_core::timedautomata::parameter_constructor_exists():
    assert callable(core::timedAutomata::Parameter.__init__)


def test_core::timedautomata::parameter_constructor_args():
    sig = inspect.signature(core::timedAutomata::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_location_constructor_exists():
    assert callable(Location.__init__)


def test_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::core::complexsystem_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::core::ComplexSystem)


def test_timedautomata::core::complexsystem_constructor_exists():
    assert callable(timedAutomata::core::ComplexSystem.__init__)


def test_timedautomata::core::complexsystem_constructor_args():
    sig = inspect.signature(timedAutomata::core::ComplexSystem.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_timedautomata::core::complexsystem_has_operator():
    assert hasattr(timedAutomata::core::ComplexSystem, "operator")
    descriptor = None
    for klass in timedAutomata::core::ComplexSystem.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_systemdefinition_is_not_abstract():
    assert not inspect.isabstract(SystemDefinition)


def test_systemdefinition_constructor_exists():
    assert callable(SystemDefinition.__init__)


def test_systemdefinition_constructor_args():
    sig = inspect.signature(SystemDefinition.__init__)
    params = list(sig.parameters.keys())



def test_template_is_not_abstract():
    assert not inspect.isabstract(Template)


def test_template_constructor_exists():
    assert callable(Template.__init__)


def test_template_constructor_args():
    sig = inspect.signature(Template.__init__)
    params = list(sig.parameters.keys())



def test_taelement_is_not_abstract():
    assert not inspect.isabstract(TAElement)


def test_taelement_constructor_exists():
    assert callable(TAElement.__init__)


def test_taelement_constructor_args():
    sig = inspect.signature(TAElement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::core::project_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::core::Project)


def test_timedautomata::core::project_constructor_exists():
    assert callable(timedAutomata::core::Project.__init__)


def test_timedautomata::core::project_constructor_args():
    sig = inspect.signature(timedAutomata::core::Project.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_timedautomata::core::project_has_id():
    assert hasattr(timedAutomata::core::Project, "id")
    descriptor = None
    for klass in timedAutomata::core::Project.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_declarations::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(declarations::FieldDeclaration)


def test_declarations::fielddeclaration_constructor_exists():
    assert callable(declarations::FieldDeclaration.__init__)


def test_declarations::fielddeclaration_constructor_args():
    sig = inspect.signature(declarations::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::types::simpletype_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::types::SimpleType)


def test_timedautomata::types::simpletype_constructor_exists():
    assert callable(timedAutomata::types::SimpleType.__init__)


def test_timedautomata::types::simpletype_constructor_args():
    sig = inspect.signature(timedAutomata::types::SimpleType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_timedautomata::types::simpletype_has_type():
    assert hasattr(timedAutomata::types::SimpleType, "type")
    descriptor = None
    for klass in timedAutomata::types::SimpleType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata::types::scalar_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::types::Scalar)


def test_timedautomata::types::scalar_constructor_exists():
    assert callable(timedAutomata::types::Scalar.__init__)


def test_timedautomata::types::scalar_constructor_args():
    sig = inspect.signature(timedAutomata::types::Scalar.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::types::struct_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::types::Struct)


def test_timedautomata::types::struct_constructor_exists():
    assert callable(timedAutomata::types::Struct.__init__)


def test_timedautomata::types::struct_constructor_args():
    sig = inspect.signature(timedAutomata::types::Struct.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::types::integerrange_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::types::IntegerRange)


def test_timedautomata::types::integerrange_constructor_exists():
    assert callable(timedAutomata::types::IntegerRange.__init__)


def test_timedautomata::types::integerrange_constructor_args():
    sig = inspect.signature(timedAutomata::types::IntegerRange.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::types::identifiertype_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::types::IdentifierType)


def test_timedautomata::types::identifiertype_constructor_exists():
    assert callable(timedAutomata::types::IdentifierType.__init__)


def test_timedautomata::types::identifiertype_constructor_args():
    sig = inspect.signature(timedAutomata::types::IdentifierType.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::types::type_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::types::Type)


def test_timedautomata::types::type_constructor_exists():
    assert callable(timedAutomata::types::Type.__init__)


def test_timedautomata::types::type_constructor_args():
    sig = inspect.signature(timedAutomata::types::Type.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_timedautomata::types::type_has_prefix():
    assert hasattr(timedAutomata::types::Type, "prefix")
    descriptor = None
    for klass in timedAutomata::types::Type.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_base::identifyable_is_not_abstract():
    assert not inspect.isabstract(base::Identifyable)


def test_base::identifyable_constructor_exists():
    assert callable(base::Identifyable.__init__)


def test_base::identifyable_constructor_args():
    sig = inspect.signature(base::Identifyable.__init__)
    params = list(sig.parameters.keys())



def test_base::nameable_is_not_abstract():
    assert not inspect.isabstract(base::Nameable)


def test_base::nameable_constructor_exists():
    assert callable(base::Nameable.__init__)


def test_base::nameable_constructor_args():
    sig = inspect.signature(base::Nameable.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::core::taelement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::core::TAElement)


def test_timedautomata::core::taelement_constructor_exists():
    assert callable(timedAutomata::core::TAElement.__init__)


def test_timedautomata::core::taelement_constructor_args():
    sig = inspect.signature(timedAutomata::core::TAElement.__init__)
    params = list(sig.parameters.keys())



def test_core::taelement_is_not_abstract():
    assert not inspect.isabstract(core::TAElement)


def test_core::taelement_constructor_exists():
    assert callable(core::TAElement.__init__)


def test_core::taelement_constructor_args():
    sig = inspect.signature(core::TAElement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::core::template_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::core::Template)


def test_timedautomata::core::template_constructor_exists():
    assert callable(timedAutomata::core::Template.__init__)


def test_timedautomata::core::template_constructor_args():
    sig = inspect.signature(timedAutomata::core::Template.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::channelexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::ChannelExpression)


def test_timedautomata::declarations::channelexpression_constructor_exists():
    assert callable(timedAutomata::declarations::ChannelExpression.__init__)


def test_timedautomata::declarations::channelexpression_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::ChannelExpression.__init__)
    params = list(sig.parameters.keys())



def test_declarations::channelexpression_is_not_abstract():
    assert not inspect.isabstract(declarations::ChannelExpression)


def test_declarations::channelexpression_constructor_exists():
    assert callable(declarations::ChannelExpression.__init__)


def test_declarations::channelexpression_constructor_args():
    sig = inspect.signature(declarations::ChannelExpression.__init__)
    params = list(sig.parameters.keys())



def test_channelpriority_is_not_abstract():
    assert not inspect.isabstract(ChannelPriority)


def test_channelpriority_constructor_exists():
    assert callable(ChannelPriority.__init__)


def test_channelpriority_constructor_args():
    sig = inspect.signature(ChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::complexchannelpriority_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::ComplexChannelPriority)


def test_timedautomata::declarations::complexchannelpriority_constructor_exists():
    assert callable(timedAutomata::declarations::ComplexChannelPriority.__init__)


def test_timedautomata::declarations::complexchannelpriority_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::ComplexChannelPriority.__init__)
    params = list(sig.parameters.keys())
    assert "channelOperator" in params, "Missing parameter 'channelOperator'"

def test_timedautomata::declarations::complexchannelpriority_has_channelOperator():
    assert hasattr(timedAutomata::declarations::ComplexChannelPriority, "channelOperator")
    descriptor = None
    for klass in timedAutomata::declarations::ComplexChannelPriority.__mro__:
        if "channelOperator" in klass.__dict__:
            descriptor = klass.__dict__["channelOperator"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata::declarations::simplechannelpriority_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::SimpleChannelPriority)


def test_timedautomata::declarations::simplechannelpriority_constructor_exists():
    assert callable(timedAutomata::declarations::SimpleChannelPriority.__init__)


def test_timedautomata::declarations::simplechannelpriority_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::SimpleChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::defaultchannelpriority_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::DefaultChannelPriority)


def test_timedautomata::declarations::defaultchannelpriority_constructor_exists():
    assert callable(timedAutomata::declarations::DefaultChannelPriority.__init__)


def test_timedautomata::declarations::defaultchannelpriority_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::DefaultChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::channelpriority_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::ChannelPriority)


def test_timedautomata::declarations::channelpriority_constructor_exists():
    assert callable(timedAutomata::declarations::ChannelPriority.__init__)


def test_timedautomata::declarations::channelpriority_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::ChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_channelexpression_is_not_abstract():
    assert not inspect.isabstract(ChannelExpression)


def test_channelexpression_constructor_exists():
    assert callable(ChannelExpression.__init__)


def test_channelexpression_constructor_args():
    sig = inspect.signature(ChannelExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::expressionchannelexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::ExpressionChannelExpression)


def test_timedautomata::declarations::expressionchannelexpression_constructor_exists():
    assert callable(timedAutomata::declarations::ExpressionChannelExpression.__init__)


def test_timedautomata::declarations::expressionchannelexpression_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::ExpressionChannelExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::identifierchannelexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::IdentifierChannelExpression)


def test_timedautomata::declarations::identifierchannelexpression_constructor_exists():
    assert callable(timedAutomata::declarations::IdentifierChannelExpression.__init__)


def test_timedautomata::declarations::identifierchannelexpression_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::IdentifierChannelExpression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::forloopstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::ForLoopStatement)


def test_timedautomata::declarations::forloopstatement_constructor_exists():
    assert callable(timedAutomata::declarations::ForLoopStatement.__init__)


def test_timedautomata::declarations::forloopstatement_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::ForLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::returnstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::ReturnStatement)


def test_timedautomata::declarations::returnstatement_constructor_exists():
    assert callable(timedAutomata::declarations::ReturnStatement.__init__)


def test_timedautomata::declarations::returnstatement_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::whileloopstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::WhileLoopStatement)


def test_timedautomata::declarations::whileloopstatement_constructor_exists():
    assert callable(timedAutomata::declarations::WhileLoopStatement.__init__)


def test_timedautomata::declarations::whileloopstatement_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::WhileLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::ifstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::IfStatement)


def test_timedautomata::declarations::ifstatement_constructor_exists():
    assert callable(timedAutomata::declarations::IfStatement.__init__)


def test_timedautomata::declarations::ifstatement_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::dowhileloopstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::DoWhileLoopStatement)


def test_timedautomata::declarations::dowhileloopstatement_constructor_exists():
    assert callable(timedAutomata::declarations::DoWhileLoopStatement.__init__)


def test_timedautomata::declarations::dowhileloopstatement_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::DoWhileLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::ExpressionStatement)


def test_timedautomata::declarations::expressionstatement_constructor_exists():
    assert callable(timedAutomata::declarations::ExpressionStatement.__init__)


def test_timedautomata::declarations::expressionstatement_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::statement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::Statement)


def test_timedautomata::declarations::statement_constructor_exists():
    assert callable(timedAutomata::declarations::Statement.__init__)


def test_timedautomata::declarations::statement_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::Statement.__init__)
    params = list(sig.parameters.keys())



def test_declarations::statement_is_not_abstract():
    assert not inspect.isabstract(declarations::Statement)


def test_declarations::statement_constructor_exists():
    assert callable(declarations::Statement.__init__)


def test_declarations::statement_constructor_args():
    sig = inspect.signature(declarations::Statement.__init__)
    params = list(sig.parameters.keys())



def test_declarations::declaration_is_not_abstract():
    assert not inspect.isabstract(declarations::Declaration)


def test_declarations::declaration_constructor_exists():
    assert callable(declarations::Declaration.__init__)


def test_declarations::declaration_constructor_args():
    sig = inspect.signature(declarations::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::block_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::Block)


def test_timedautomata::declarations::block_constructor_exists():
    assert callable(timedAutomata::declarations::Block.__init__)


def test_timedautomata::declarations::block_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::Block.__init__)
    params = list(sig.parameters.keys())



def test_taparameter_is_not_abstract():
    assert not inspect.isabstract(TAParameter)


def test_taparameter_constructor_exists():
    assert callable(TAParameter.__init__)


def test_taparameter_constructor_args():
    sig = inspect.signature(TAParameter.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::callbyreferenceparameter_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::CallByReferenceParameter)


def test_timedautomata::declarations::callbyreferenceparameter_constructor_exists():
    assert callable(timedAutomata::declarations::CallByReferenceParameter.__init__)


def test_timedautomata::declarations::callbyreferenceparameter_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::CallByReferenceParameter.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::callbyvalueparameter_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::CallByValueParameter)


def test_timedautomata::declarations::callbyvalueparameter_constructor_exists():
    assert callable(timedAutomata::declarations::CallByValueParameter.__init__)


def test_timedautomata::declarations::callbyvalueparameter_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::CallByValueParameter.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::taparameter_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::TAParameter)


def test_timedautomata::declarations::taparameter_constructor_exists():
    assert callable(timedAutomata::declarations::TAParameter.__init__)


def test_timedautomata::declarations::taparameter_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::TAParameter.__init__)
    params = list(sig.parameters.keys())



def test_initialiser_is_not_abstract():
    assert not inspect.isabstract(Initialiser)


def test_initialiser_constructor_exists():
    assert callable(Initialiser.__init__)


def test_initialiser_constructor_args():
    sig = inspect.signature(Initialiser.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::arrayinitialiser_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::ArrayInitialiser)


def test_timedautomata::declarations::arrayinitialiser_constructor_exists():
    assert callable(timedAutomata::declarations::ArrayInitialiser.__init__)


def test_timedautomata::declarations::arrayinitialiser_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::ArrayInitialiser.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::expressioninitialiser_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::ExpressionInitialiser)


def test_timedautomata::declarations::expressioninitialiser_constructor_exists():
    assert callable(timedAutomata::declarations::ExpressionInitialiser.__init__)


def test_timedautomata::declarations::expressioninitialiser_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::ExpressionInitialiser.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::initialiser_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::Initialiser)


def test_timedautomata::declarations::initialiser_constructor_exists():
    assert callable(timedAutomata::declarations::Initialiser.__init__)


def test_timedautomata::declarations::initialiser_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::Initialiser.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::iterationstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::IterationStatement)


def test_timedautomata::declarations::iterationstatement_constructor_exists():
    assert callable(timedAutomata::declarations::IterationStatement.__init__)


def test_timedautomata::declarations::iterationstatement_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::IterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_arraydeclarationtype_is_not_abstract():
    assert not inspect.isabstract(ArrayDeclarationType)


def test_arraydeclarationtype_constructor_exists():
    assert callable(ArrayDeclarationType.__init__)


def test_arraydeclarationtype_constructor_args():
    sig = inspect.signature(ArrayDeclarationType.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::arrayexpressiontype_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::ArrayExpressionType)


def test_timedautomata::declarations::arrayexpressiontype_constructor_exists():
    assert callable(timedAutomata::declarations::ArrayExpressionType.__init__)


def test_timedautomata::declarations::arrayexpressiontype_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::ArrayExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::arraydeclarationtype_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::ArrayDeclarationType)


def test_timedautomata::declarations::arraydeclarationtype_constructor_exists():
    assert callable(timedAutomata::declarations::ArrayDeclarationType.__init__)


def test_timedautomata::declarations::arraydeclarationtype_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::ArrayDeclarationType.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::arraydeclaration_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::ArrayDeclaration)


def test_timedautomata::declarations::arraydeclaration_constructor_exists():
    assert callable(timedAutomata::declarations::ArrayDeclaration.__init__)


def test_timedautomata::declarations::arraydeclaration_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::ArrayDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::FieldDeclaration)


def test_timedautomata::declarations::fielddeclaration_constructor_exists():
    assert callable(timedAutomata::declarations::FieldDeclaration.__init__)


def test_timedautomata::declarations::fielddeclaration_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_declarations::channelpriority_is_not_abstract():
    assert not inspect.isabstract(declarations::ChannelPriority)


def test_declarations::channelpriority_constructor_exists():
    assert callable(declarations::ChannelPriority.__init__)


def test_declarations::channelpriority_constructor_args():
    sig = inspect.signature(declarations::ChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_declarations::block_is_not_abstract():
    assert not inspect.isabstract(declarations::Block)


def test_declarations::block_constructor_exists():
    assert callable(declarations::Block.__init__)


def test_declarations::block_constructor_args():
    sig = inspect.signature(declarations::Block.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::blockstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::BlockStatement)


def test_timedautomata::declarations::blockstatement_constructor_exists():
    assert callable(timedAutomata::declarations::BlockStatement.__init__)


def test_timedautomata::declarations::blockstatement_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_declarations::taparameter_is_not_abstract():
    assert not inspect.isabstract(declarations::TAParameter)


def test_declarations::taparameter_constructor_exists():
    assert callable(declarations::TAParameter.__init__)


def test_declarations::taparameter_constructor_args():
    sig = inspect.signature(declarations::TAParameter.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::arraytypetype_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::ArrayTypeType)


def test_timedautomata::declarations::arraytypetype_constructor_exists():
    assert callable(timedAutomata::declarations::ArrayTypeType.__init__)


def test_timedautomata::declarations::arraytypetype_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::ArrayTypeType.__init__)
    params = list(sig.parameters.keys())



def test_declarations::initialiser_is_not_abstract():
    assert not inspect.isabstract(declarations::Initialiser)


def test_declarations::initialiser_constructor_exists():
    assert callable(declarations::Initialiser.__init__)


def test_declarations::initialiser_constructor_args():
    sig = inspect.signature(declarations::Initialiser.__init__)
    params = list(sig.parameters.keys())



def test_declarations::arraydeclarationtype_is_not_abstract():
    assert not inspect.isabstract(declarations::ArrayDeclarationType)


def test_declarations::arraydeclarationtype_constructor_exists():
    assert callable(declarations::ArrayDeclarationType.__init__)


def test_declarations::arraydeclarationtype_constructor_args():
    sig = inspect.signature(declarations::ArrayDeclarationType.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::variableidentifier_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::VariableIdentifier)


def test_timedautomata::declarations::variableidentifier_constructor_exists():
    assert callable(timedAutomata::declarations::VariableIdentifier.__init__)


def test_timedautomata::declarations::variableidentifier_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::VariableIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_declarations::variableidentifier_is_not_abstract():
    assert not inspect.isabstract(declarations::VariableIdentifier)


def test_declarations::variableidentifier_constructor_exists():
    assert callable(declarations::VariableIdentifier.__init__)


def test_declarations::variableidentifier_constructor_args():
    sig = inspect.signature(declarations::VariableIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::channelprioritydeclaration_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::ChannelPriorityDeclaration)


def test_timedautomata::declarations::channelprioritydeclaration_constructor_exists():
    assert callable(timedAutomata::declarations::ChannelPriorityDeclaration.__init__)


def test_timedautomata::declarations::channelprioritydeclaration_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::ChannelPriorityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::VariableDeclaration)


def test_timedautomata::declarations::variabledeclaration_constructor_exists():
    assert callable(timedAutomata::declarations::VariableDeclaration.__init__)


def test_timedautomata::declarations::variabledeclaration_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::expressions::selection_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::Selection)


def test_timedautomata::expressions::selection_constructor_exists():
    assert callable(timedAutomata::expressions::Selection.__init__)


def test_timedautomata::expressions::selection_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::Selection.__init__)
    params = list(sig.parameters.keys())



def test_types::type_is_not_abstract():
    assert not inspect.isabstract(types::Type)


def test_types::type_constructor_exists():
    assert callable(types::Type.__init__)


def test_types::type_constructor_args():
    sig = inspect.signature(types::Type.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::FunctionDeclaration)


def test_timedautomata::declarations::functiondeclaration_constructor_exists():
    assert callable(timedAutomata::declarations::FunctionDeclaration.__init__)


def test_timedautomata::declarations::functiondeclaration_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_declarations::arraydeclaration_is_not_abstract():
    assert not inspect.isabstract(declarations::ArrayDeclaration)


def test_declarations::arraydeclaration_constructor_exists():
    assert callable(declarations::ArrayDeclaration.__init__)


def test_declarations::arraydeclaration_constructor_args():
    sig = inspect.signature(declarations::ArrayDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::TypeDeclaration)


def test_timedautomata::declarations::typedeclaration_constructor_exists():
    assert callable(timedAutomata::declarations::TypeDeclaration.__init__)


def test_timedautomata::declarations::typedeclaration_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_synchronisation_is_not_abstract():
    assert not inspect.isabstract(Synchronisation)


def test_synchronisation_constructor_exists():
    assert callable(Synchronisation.__init__)


def test_synchronisation_constructor_args():
    sig = inspect.signature(Synchronisation.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::bnf::receivesynchronisation_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::bnf::ReceiveSynchronisation)


def test_timedautomata::bnf::receivesynchronisation_constructor_exists():
    assert callable(timedAutomata::bnf::ReceiveSynchronisation.__init__)


def test_timedautomata::bnf::receivesynchronisation_constructor_args():
    sig = inspect.signature(timedAutomata::bnf::ReceiveSynchronisation.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::bnf::sendsynchronisation_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::bnf::SendSynchronisation)


def test_timedautomata::bnf::sendsynchronisation_constructor_exists():
    assert callable(timedAutomata::bnf::SendSynchronisation.__init__)


def test_timedautomata::bnf::sendsynchronisation_constructor_args():
    sig = inspect.signature(timedAutomata::bnf::SendSynchronisation.__init__)
    params = list(sig.parameters.keys())



def test_expressions::expression_is_not_abstract():
    assert not inspect.isabstract(expressions::Expression)


def test_expressions::expression_constructor_exists():
    assert callable(expressions::Expression.__init__)


def test_expressions::expression_constructor_args():
    sig = inspect.signature(expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::expressions::incdecexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::IncDecExpression)


def test_timedautomata::expressions::incdecexpression_constructor_exists():
    assert callable(timedAutomata::expressions::IncDecExpression.__init__)


def test_timedautomata::expressions::incdecexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::IncDecExpression.__init__)
    params = list(sig.parameters.keys())
    assert "increment" in params, "Missing parameter 'increment'"
    assert "beforeExpression" in params, "Missing parameter 'beforeExpression'"

def test_timedautomata::expressions::incdecexpression_has_increment():
    assert hasattr(timedAutomata::expressions::IncDecExpression, "increment")
    descriptor = None
    for klass in timedAutomata::expressions::IncDecExpression.__mro__:
        if "increment" in klass.__dict__:
            descriptor = klass.__dict__["increment"]
            break
    assert isinstance(descriptor, property)

def test_timedautomata::expressions::incdecexpression_has_beforeExpression():
    assert hasattr(timedAutomata::expressions::IncDecExpression, "beforeExpression")
    descriptor = None
    for klass in timedAutomata::expressions::IncDecExpression.__mro__:
        if "beforeExpression" in klass.__dict__:
            descriptor = klass.__dict__["beforeExpression"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata::expressions::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::BinaryExpression)


def test_timedautomata::expressions::binaryexpression_constructor_exists():
    assert callable(timedAutomata::expressions::BinaryExpression.__init__)


def test_timedautomata::expressions::binaryexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_timedautomata::expressions::binaryexpression_has_operator():
    assert hasattr(timedAutomata::expressions::BinaryExpression, "operator")
    descriptor = None
    for klass in timedAutomata::expressions::BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata::expressions::fixedexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::FixedExpression)


def test_timedautomata::expressions::fixedexpression_constructor_exists():
    assert callable(timedAutomata::expressions::FixedExpression.__init__)


def test_timedautomata::expressions::fixedexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::FixedExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_timedautomata::expressions::fixedexpression_has_type():
    assert hasattr(timedAutomata::expressions::FixedExpression, "type")
    descriptor = None
    for klass in timedAutomata::expressions::FixedExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata::expressions::assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::AssignmentExpression)


def test_timedautomata::expressions::assignmentexpression_constructor_exists():
    assert callable(timedAutomata::expressions::AssignmentExpression.__init__)


def test_timedautomata::expressions::assignmentexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::AssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_timedautomata::expressions::assignmentexpression_has_operator():
    assert hasattr(timedAutomata::expressions::AssignmentExpression, "operator")
    descriptor = None
    for klass in timedAutomata::expressions::AssignmentExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata::expressions::identifierexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::IdentifierExpression)


def test_timedautomata::expressions::identifierexpression_constructor_exists():
    assert callable(timedAutomata::expressions::IdentifierExpression.__init__)


def test_timedautomata::expressions::identifierexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::IdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::expressions::simpleifexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::SimpleIfExpression)


def test_timedautomata::expressions::simpleifexpression_constructor_exists():
    assert callable(timedAutomata::expressions::SimpleIfExpression.__init__)


def test_timedautomata::expressions::simpleifexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::SimpleIfExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::expressions::arrayvariableexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::ArrayVariableExpression)


def test_timedautomata::expressions::arrayvariableexpression_constructor_exists():
    assert callable(timedAutomata::expressions::ArrayVariableExpression.__init__)


def test_timedautomata::expressions::arrayvariableexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::ArrayVariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::expressions::withargumentsexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::WithArgumentsExpression)


def test_timedautomata::expressions::withargumentsexpression_constructor_exists():
    assert callable(timedAutomata::expressions::WithArgumentsExpression.__init__)


def test_timedautomata::expressions::withargumentsexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::WithArgumentsExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::expressions::forallexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::ForallExpression)


def test_timedautomata::expressions::forallexpression_constructor_exists():
    assert callable(timedAutomata::expressions::ForallExpression.__init__)


def test_timedautomata::expressions::forallexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::ForallExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::expressions::variableexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::VariableExpression)


def test_timedautomata::expressions::variableexpression_constructor_exists():
    assert callable(timedAutomata::expressions::VariableExpression.__init__)


def test_timedautomata::expressions::variableexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::expressions::pointexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::PointExpression)


def test_timedautomata::expressions::pointexpression_constructor_exists():
    assert callable(timedAutomata::expressions::PointExpression.__init__)


def test_timedautomata::expressions::pointexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::PointExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::expressions::groupingexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::GroupingExpression)


def test_timedautomata::expressions::groupingexpression_constructor_exists():
    assert callable(timedAutomata::expressions::GroupingExpression.__init__)


def test_timedautomata::expressions::groupingexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::GroupingExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::expressions::existsexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::ExistsExpression)


def test_timedautomata::expressions::existsexpression_constructor_exists():
    assert callable(timedAutomata::expressions::ExistsExpression.__init__)


def test_timedautomata::expressions::existsexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::ExistsExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::expressions::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::UnaryExpression)


def test_timedautomata::expressions::unaryexpression_constructor_exists():
    assert callable(timedAutomata::expressions::UnaryExpression.__init__)


def test_timedautomata::expressions::unaryexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_timedautomata::expressions::unaryexpression_has_operator():
    assert hasattr(timedAutomata::expressions::UnaryExpression, "operator")
    descriptor = None
    for klass in timedAutomata::expressions::UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata::expressions::constantexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::ConstantExpression)


def test_timedautomata::expressions::constantexpression_constructor_exists():
    assert callable(timedAutomata::expressions::ConstantExpression.__init__)


def test_timedautomata::expressions::constantexpression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::ConstantExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_timedautomata::expressions::constantexpression_has_value():
    assert hasattr(timedAutomata::expressions::ConstantExpression, "value")
    descriptor = None
    for klass in timedAutomata::expressions::ConstantExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_commentable_is_not_abstract():
    assert not inspect.isabstract(Commentable)


def test_commentable_constructor_exists():
    assert callable(Commentable.__init__)


def test_commentable_constructor_args():
    sig = inspect.signature(Commentable.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::declarations::declaration_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::declarations::Declaration)


def test_timedautomata::declarations::declaration_constructor_exists():
    assert callable(timedAutomata::declarations::Declaration.__init__)


def test_timedautomata::declarations::declaration_constructor_args():
    sig = inspect.signature(timedAutomata::declarations::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::expressions::expression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::expressions::Expression)


def test_timedautomata::expressions::expression_constructor_exists():
    assert callable(timedAutomata::expressions::Expression.__init__)


def test_timedautomata::expressions::expression_constructor_args():
    sig = inspect.signature(timedAutomata::expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::base::identifyable_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::base::Identifyable)


def test_timedautomata::base::identifyable_constructor_exists():
    assert callable(timedAutomata::base::Identifyable.__init__)


def test_timedautomata::base::identifyable_constructor_args():
    sig = inspect.signature(timedAutomata::base::Identifyable.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_timedautomata::base::identifyable_has_id():
    assert hasattr(timedAutomata::base::Identifyable, "id")
    descriptor = None
    for klass in timedAutomata::base::Identifyable.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata::base::commentable_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::base::Commentable)


def test_timedautomata::base::commentable_constructor_exists():
    assert callable(timedAutomata::base::Commentable.__init__)


def test_timedautomata::base::commentable_constructor_args():
    sig = inspect.signature(timedAutomata::base::Commentable.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_timedautomata::base::commentable_has_comment():
    assert hasattr(timedAutomata::base::Commentable, "comment")
    descriptor = None
    for klass in timedAutomata::base::Commentable.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_position_is_not_abstract():
    assert not inspect.isabstract(Position)


def test_position_constructor_exists():
    assert callable(Position.__init__)


def test_position_constructor_args():
    sig = inspect.signature(Position.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::core::selections_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::core::Selections)


def test_timedautomata::core::selections_constructor_exists():
    assert callable(timedAutomata::core::Selections.__init__)


def test_timedautomata::core::selections_constructor_args():
    sig = inspect.signature(timedAutomata::core::Selections.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::core::edge_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::core::Edge)


def test_timedautomata::core::edge_constructor_exists():
    assert callable(timedAutomata::core::Edge.__init__)


def test_timedautomata::core::edge_constructor_args():
    sig = inspect.signature(timedAutomata::core::Edge.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::core::location_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::core::Location)


def test_timedautomata::core::location_constructor_exists():
    assert callable(timedAutomata::core::Location.__init__)


def test_timedautomata::core::location_constructor_args():
    sig = inspect.signature(timedAutomata::core::Location.__init__)
    params = list(sig.parameters.keys())
    assert "committed" in params, "Missing parameter 'committed'"
    assert "urgent" in params, "Missing parameter 'urgent'"

def test_timedautomata::core::location_has_committed():
    assert hasattr(timedAutomata::core::Location, "committed")
    descriptor = None
    for klass in timedAutomata::core::Location.__mro__:
        if "committed" in klass.__dict__:
            descriptor = klass.__dict__["committed"]
            break
    assert isinstance(descriptor, property)

def test_timedautomata::core::location_has_urgent():
    assert hasattr(timedAutomata::core::Location, "urgent")
    descriptor = None
    for klass in timedAutomata::core::Location.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata::core::updates_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::core::Updates)


def test_timedautomata::core::updates_constructor_exists():
    assert callable(timedAutomata::core::Updates.__init__)


def test_timedautomata::core::updates_constructor_args():
    sig = inspect.signature(timedAutomata::core::Updates.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::core::guards_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::core::Guards)


def test_timedautomata::core::guards_constructor_exists():
    assert callable(timedAutomata::core::Guards.__init__)


def test_timedautomata::core::guards_constructor_args():
    sig = inspect.signature(timedAutomata::core::Guards.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::bnf::synchronisation_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::bnf::Synchronisation)


def test_timedautomata::bnf::synchronisation_constructor_exists():
    assert callable(timedAutomata::bnf::Synchronisation.__init__)


def test_timedautomata::bnf::synchronisation_constructor_args():
    sig = inspect.signature(timedAutomata::bnf::Synchronisation.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata::bnf::identifier_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::bnf::Identifier)


def test_timedautomata::bnf::identifier_constructor_exists():
    assert callable(timedAutomata::bnf::Identifier.__init__)


def test_timedautomata::bnf::identifier_constructor_args():
    sig = inspect.signature(timedAutomata::bnf::Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_timedautomata::bnf::identifier_has_name():
    assert hasattr(timedAutomata::bnf::Identifier, "name")
    descriptor = None
    for klass in timedAutomata::bnf::Identifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata::base::nameable_is_not_abstract():
    assert not inspect.isabstract(timedAutomata::base::Nameable)


def test_timedautomata::base::nameable_constructor_exists():
    assert callable(timedAutomata::base::Nameable.__init__)


def test_timedautomata::base::nameable_constructor_args():
    sig = inspect.signature(timedAutomata::base::Nameable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_timedautomata::base::nameable_has_name():
    assert hasattr(timedAutomata::base::Nameable, "name")
    descriptor = None
    for klass in timedAutomata::base::Nameable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_typeid_exists():
    # Check that the Enumeration exists
    assert TypeId is not None

def test_typeid_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeId]
    expected_literals = [
        "Void",
        "Channel",
        "Clock",
        "Boolean",
        "Integer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeId"

def test_priorityoperator_exists():
    # Check that the Enumeration exists
    assert PriorityOperator is not None

def test_priorityoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PriorityOperator]
    expected_literals = [
        "LessThan",
        "Seperator",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PriorityOperator"

def test_fixedexpressiontype_exists():
    # Check that the Enumeration exists
    assert FixedExpressionType is not None

def test_fixedexpressiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FixedExpressionType]
    expected_literals = [
        "False_",
        "True_",
        "Deadlock",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FixedExpressionType"

def test_typeprefix_exists():
    # Check that the Enumeration exists
    assert TypePrefix is not None

def test_typeprefix_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypePrefix]
    expected_literals = [
        "BROADCAST",
        "CONSTANT",
        "NONE",
        "META",
        "URGENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypePrefix"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "PLUS",
        "NOT",
        "MINUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_binaryoperator_exists():
    # Check that the Enumeration exists
    assert BinaryOperator is not None

def test_binaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOperator]
    expected_literals = [
        "MODULO",
        "BITWISE_OR",
        "EQUALS",
        "NONE",
        "MULTIPLICATION",
        "RIGHT_BITSHIFT",
        "GREATER_THAN_OR_EQUAL",
        "ADDITION",
        "IMPLY",
        "LESS_THAN",
        "LOGICAL_NEGATION",
        "MAXIMUM",
        "LOGICAL_OR",
        "DECREMENT",
        "BITWISE_AND",
        "LOGICAL_AND",
        "RIGHT_BITSHIFT_ASSIGN",
        "SUBSTRACTION",
        "INCREMENT",
        "BITWISE_XOR_ASIGN",
        "BITWISE_OR_ASSIGN",
        "BITWISE_AND_ASSIGN",
        "MINIMUM",
        "LEFT_BITSHIFT_ASSIGN",
        "LESS_THAN_OR_EQUAL",
        "GREATER_THAN",
        "DIVISION",
        "LEFT_BITSHIFT",
        "BITWISE_XOR",
        "NOT_EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOperator"

def test_assignoperator_exists():
    # Check that the Enumeration exists
    assert AssignOperator is not None

def test_assignoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignOperator]
    expected_literals = [
        "MOD_ASSIGN",
        "MULT_ASSIGN",
        "ADD_ASIGN",
        "SUB_ASSIGN",
        "DIV_ASSIGN",
        "ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignOperator"


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
expressions::Selection_strategy = st.builds(
    expressions::Selection,
)
timedAutomata::core::TemplateInstantiation_strategy = st.builds(
    timedAutomata::core::TemplateInstantiation,
)
timedAutomata::core::System_strategy = st.builds(
    timedAutomata::core::System,
)
System_strategy = st.builds(
    System,
)
timedAutomata::core::SimpleSystem_strategy = st.builds(
    timedAutomata::core::SimpleSystem,
)
TemplateInstantiation_strategy = st.builds(
    TemplateInstantiation,
)
timedAutomata::core::SystemDefinition_strategy = st.builds(
    timedAutomata::core::SystemDefinition,
)
core::timedAutomata::Label_strategy = st.builds(
    core::timedAutomata::Label,
)
base::Commentable_strategy = st.builds(
    base::Commentable,
)
core::timedAutomata::Nail_strategy = st.builds(
    core::timedAutomata::Nail,
)
Updates_strategy = st.builds(
    Updates,
)
Selections_strategy = st.builds(
    Selections,
)
Guards_strategy = st.builds(
    Guards,
)
Edge_strategy = st.builds(
    Edge,
)
core::timedAutomata::Parameter_strategy = st.builds(
    core::timedAutomata::Parameter,
)
Location_strategy = st.builds(
    Location,
)
timedAutomata::core::ComplexSystem_strategy = st.builds(
    timedAutomata::core::ComplexSystem,
    operator=
        safe_text
)
SystemDefinition_strategy = st.builds(
    SystemDefinition,
)
Template_strategy = st.builds(
    Template,
)
TAElement_strategy = st.builds(
    TAElement,
)
timedAutomata::core::Project_strategy = st.builds(
    timedAutomata::core::Project,
    id=
        safe_text
)
declarations::FieldDeclaration_strategy = st.builds(
    declarations::FieldDeclaration,
)
Type_strategy = st.builds(
    Type,
)
timedAutomata::types::SimpleType_strategy = st.builds(
    timedAutomata::types::SimpleType,
    type=
        safe_text
)
timedAutomata::types::Scalar_strategy = st.builds(
    timedAutomata::types::Scalar,
)
timedAutomata::types::Struct_strategy = st.builds(
    timedAutomata::types::Struct,
)
timedAutomata::types::IntegerRange_strategy = st.builds(
    timedAutomata::types::IntegerRange,
)
timedAutomata::types::IdentifierType_strategy = st.builds(
    timedAutomata::types::IdentifierType,
)
timedAutomata::types::Type_strategy = st.builds(
    timedAutomata::types::Type,
    prefix=
        safe_text
)
base::Identifyable_strategy = st.builds(
    base::Identifyable,
)
base::Nameable_strategy = st.builds(
    base::Nameable,
)
timedAutomata::core::TAElement_strategy = st.builds(
    timedAutomata::core::TAElement,
)
core::TAElement_strategy = st.builds(
    core::TAElement,
)
timedAutomata::core::Template_strategy = st.builds(
    timedAutomata::core::Template,
)
timedAutomata::declarations::ChannelExpression_strategy = st.builds(
    timedAutomata::declarations::ChannelExpression,
)
declarations::ChannelExpression_strategy = st.builds(
    declarations::ChannelExpression,
)
ChannelPriority_strategy = st.builds(
    ChannelPriority,
)
timedAutomata::declarations::ComplexChannelPriority_strategy = st.builds(
    timedAutomata::declarations::ComplexChannelPriority,
    channelOperator=
        safe_text
)
timedAutomata::declarations::SimpleChannelPriority_strategy = st.builds(
    timedAutomata::declarations::SimpleChannelPriority,
)
timedAutomata::declarations::DefaultChannelPriority_strategy = st.builds(
    timedAutomata::declarations::DefaultChannelPriority,
)
timedAutomata::declarations::ChannelPriority_strategy = st.builds(
    timedAutomata::declarations::ChannelPriority,
)
ChannelExpression_strategy = st.builds(
    ChannelExpression,
)
timedAutomata::declarations::ExpressionChannelExpression_strategy = st.builds(
    timedAutomata::declarations::ExpressionChannelExpression,
)
timedAutomata::declarations::IdentifierChannelExpression_strategy = st.builds(
    timedAutomata::declarations::IdentifierChannelExpression,
)
Statement_strategy = st.builds(
    Statement,
)
timedAutomata::declarations::ForLoopStatement_strategy = st.builds(
    timedAutomata::declarations::ForLoopStatement,
)
timedAutomata::declarations::ReturnStatement_strategy = st.builds(
    timedAutomata::declarations::ReturnStatement,
)
timedAutomata::declarations::WhileLoopStatement_strategy = st.builds(
    timedAutomata::declarations::WhileLoopStatement,
)
timedAutomata::declarations::IfStatement_strategy = st.builds(
    timedAutomata::declarations::IfStatement,
)
timedAutomata::declarations::DoWhileLoopStatement_strategy = st.builds(
    timedAutomata::declarations::DoWhileLoopStatement,
)
timedAutomata::declarations::ExpressionStatement_strategy = st.builds(
    timedAutomata::declarations::ExpressionStatement,
)
timedAutomata::declarations::Statement_strategy = st.builds(
    timedAutomata::declarations::Statement,
)
declarations::Statement_strategy = st.builds(
    declarations::Statement,
)
declarations::Declaration_strategy = st.builds(
    declarations::Declaration,
)
timedAutomata::declarations::Block_strategy = st.builds(
    timedAutomata::declarations::Block,
)
TAParameter_strategy = st.builds(
    TAParameter,
)
timedAutomata::declarations::CallByReferenceParameter_strategy = st.builds(
    timedAutomata::declarations::CallByReferenceParameter,
)
timedAutomata::declarations::CallByValueParameter_strategy = st.builds(
    timedAutomata::declarations::CallByValueParameter,
)
timedAutomata::declarations::TAParameter_strategy = st.builds(
    timedAutomata::declarations::TAParameter,
)
Initialiser_strategy = st.builds(
    Initialiser,
)
timedAutomata::declarations::ArrayInitialiser_strategy = st.builds(
    timedAutomata::declarations::ArrayInitialiser,
)
timedAutomata::declarations::ExpressionInitialiser_strategy = st.builds(
    timedAutomata::declarations::ExpressionInitialiser,
)
timedAutomata::declarations::Initialiser_strategy = st.builds(
    timedAutomata::declarations::Initialiser,
)
timedAutomata::declarations::IterationStatement_strategy = st.builds(
    timedAutomata::declarations::IterationStatement,
)
ArrayDeclarationType_strategy = st.builds(
    ArrayDeclarationType,
)
timedAutomata::declarations::ArrayExpressionType_strategy = st.builds(
    timedAutomata::declarations::ArrayExpressionType,
)
timedAutomata::declarations::ArrayDeclarationType_strategy = st.builds(
    timedAutomata::declarations::ArrayDeclarationType,
)
timedAutomata::declarations::ArrayDeclaration_strategy = st.builds(
    timedAutomata::declarations::ArrayDeclaration,
)
timedAutomata::declarations::FieldDeclaration_strategy = st.builds(
    timedAutomata::declarations::FieldDeclaration,
)
declarations::ChannelPriority_strategy = st.builds(
    declarations::ChannelPriority,
)
declarations::Block_strategy = st.builds(
    declarations::Block,
)
timedAutomata::declarations::BlockStatement_strategy = st.builds(
    timedAutomata::declarations::BlockStatement,
)
declarations::TAParameter_strategy = st.builds(
    declarations::TAParameter,
)
timedAutomata::declarations::ArrayTypeType_strategy = st.builds(
    timedAutomata::declarations::ArrayTypeType,
)
declarations::Initialiser_strategy = st.builds(
    declarations::Initialiser,
)
declarations::ArrayDeclarationType_strategy = st.builds(
    declarations::ArrayDeclarationType,
)
timedAutomata::declarations::VariableIdentifier_strategy = st.builds(
    timedAutomata::declarations::VariableIdentifier,
)
declarations::VariableIdentifier_strategy = st.builds(
    declarations::VariableIdentifier,
)
Declaration_strategy = st.builds(
    Declaration,
)
timedAutomata::declarations::ChannelPriorityDeclaration_strategy = st.builds(
    timedAutomata::declarations::ChannelPriorityDeclaration,
)
timedAutomata::declarations::VariableDeclaration_strategy = st.builds(
    timedAutomata::declarations::VariableDeclaration,
)
timedAutomata::expressions::Selection_strategy = st.builds(
    timedAutomata::expressions::Selection,
)
types::Type_strategy = st.builds(
    types::Type,
)
timedAutomata::declarations::FunctionDeclaration_strategy = st.builds(
    timedAutomata::declarations::FunctionDeclaration,
)
declarations::ArrayDeclaration_strategy = st.builds(
    declarations::ArrayDeclaration,
)
timedAutomata::declarations::TypeDeclaration_strategy = st.builds(
    timedAutomata::declarations::TypeDeclaration,
)
Identifier_strategy = st.builds(
    Identifier,
)
Synchronisation_strategy = st.builds(
    Synchronisation,
)
timedAutomata::bnf::ReceiveSynchronisation_strategy = st.builds(
    timedAutomata::bnf::ReceiveSynchronisation,
)
timedAutomata::bnf::SendSynchronisation_strategy = st.builds(
    timedAutomata::bnf::SendSynchronisation,
)
expressions::Expression_strategy = st.builds(
    expressions::Expression,
)
Expression_strategy = st.builds(
    Expression,
)
timedAutomata::expressions::IncDecExpression_strategy = st.builds(
    timedAutomata::expressions::IncDecExpression,
    increment=
        st.booleans(),
    beforeExpression=
        st.booleans()
)
timedAutomata::expressions::BinaryExpression_strategy = st.builds(
    timedAutomata::expressions::BinaryExpression,
    operator=
        safe_text
)
timedAutomata::expressions::FixedExpression_strategy = st.builds(
    timedAutomata::expressions::FixedExpression,
    type=
        safe_text
)
timedAutomata::expressions::AssignmentExpression_strategy = st.builds(
    timedAutomata::expressions::AssignmentExpression,
    operator=
        safe_text
)
timedAutomata::expressions::IdentifierExpression_strategy = st.builds(
    timedAutomata::expressions::IdentifierExpression,
)
timedAutomata::expressions::SimpleIfExpression_strategy = st.builds(
    timedAutomata::expressions::SimpleIfExpression,
)
timedAutomata::expressions::ArrayVariableExpression_strategy = st.builds(
    timedAutomata::expressions::ArrayVariableExpression,
)
timedAutomata::expressions::WithArgumentsExpression_strategy = st.builds(
    timedAutomata::expressions::WithArgumentsExpression,
)
timedAutomata::expressions::ForallExpression_strategy = st.builds(
    timedAutomata::expressions::ForallExpression,
)
timedAutomata::expressions::VariableExpression_strategy = st.builds(
    timedAutomata::expressions::VariableExpression,
)
timedAutomata::expressions::PointExpression_strategy = st.builds(
    timedAutomata::expressions::PointExpression,
)
timedAutomata::expressions::GroupingExpression_strategy = st.builds(
    timedAutomata::expressions::GroupingExpression,
)
timedAutomata::expressions::ExistsExpression_strategy = st.builds(
    timedAutomata::expressions::ExistsExpression,
)
timedAutomata::expressions::UnaryExpression_strategy = st.builds(
    timedAutomata::expressions::UnaryExpression,
    operator=
        safe_text
)
timedAutomata::expressions::ConstantExpression_strategy = st.builds(
    timedAutomata::expressions::ConstantExpression,
    value=
        st.integers()
)
Commentable_strategy = st.builds(
    Commentable,
)
timedAutomata::declarations::Declaration_strategy = st.builds(
    timedAutomata::declarations::Declaration,
)
timedAutomata::expressions::Expression_strategy = st.builds(
    timedAutomata::expressions::Expression,
)
timedAutomata::base::Identifyable_strategy = st.builds(
    timedAutomata::base::Identifyable,
    id=
        st.integers()
)
timedAutomata::base::Commentable_strategy = st.builds(
    timedAutomata::base::Commentable,
    comment=
        safe_text
)
Position_strategy = st.builds(
    Position,
)
timedAutomata::core::Selections_strategy = st.builds(
    timedAutomata::core::Selections,
)
timedAutomata::core::Edge_strategy = st.builds(
    timedAutomata::core::Edge,
)
timedAutomata::core::Location_strategy = st.builds(
    timedAutomata::core::Location,
    committed=
        safe_text,
    urgent=
        safe_text
)
timedAutomata::core::Updates_strategy = st.builds(
    timedAutomata::core::Updates,
)
timedAutomata::core::Guards_strategy = st.builds(
    timedAutomata::core::Guards,
)
timedAutomata::bnf::Synchronisation_strategy = st.builds(
    timedAutomata::bnf::Synchronisation,
)
timedAutomata::bnf::Identifier_strategy = st.builds(
    timedAutomata::bnf::Identifier,
    name=
        safe_text
)
timedAutomata::base::Nameable_strategy = st.builds(
    timedAutomata::base::Nameable,
    name=
        safe_text
)

@given(instance=expressions::Selection_strategy)
@settings(max_examples=50)
def test_expressions::selection_instantiation(instance):
    assert isinstance(instance, expressions::Selection)

@given(instance=timedAutomata::core::TemplateInstantiation_strategy)
@settings(max_examples=50)
def test_timedautomata::core::templateinstantiation_instantiation(instance):
    assert isinstance(instance, timedAutomata::core::TemplateInstantiation)

@given(instance=timedAutomata::core::System_strategy)
@settings(max_examples=50)
def test_timedautomata::core::system_instantiation(instance):
    assert isinstance(instance, timedAutomata::core::System)

@given(instance=System_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, System)

@given(instance=timedAutomata::core::SimpleSystem_strategy)
@settings(max_examples=50)
def test_timedautomata::core::simplesystem_instantiation(instance):
    assert isinstance(instance, timedAutomata::core::SimpleSystem)

@given(instance=TemplateInstantiation_strategy)
@settings(max_examples=50)
def test_templateinstantiation_instantiation(instance):
    assert isinstance(instance, TemplateInstantiation)

@given(instance=timedAutomata::core::SystemDefinition_strategy)
@settings(max_examples=50)
def test_timedautomata::core::systemdefinition_instantiation(instance):
    assert isinstance(instance, timedAutomata::core::SystemDefinition)

@given(instance=core::timedAutomata::Label_strategy)
@settings(max_examples=50)
def test_core::timedautomata::label_instantiation(instance):
    assert isinstance(instance, core::timedAutomata::Label)

@given(instance=base::Commentable_strategy)
@settings(max_examples=50)
def test_base::commentable_instantiation(instance):
    assert isinstance(instance, base::Commentable)

@given(instance=core::timedAutomata::Nail_strategy)
@settings(max_examples=50)
def test_core::timedautomata::nail_instantiation(instance):
    assert isinstance(instance, core::timedAutomata::Nail)

@given(instance=Updates_strategy)
@settings(max_examples=50)
def test_updates_instantiation(instance):
    assert isinstance(instance, Updates)

@given(instance=Selections_strategy)
@settings(max_examples=50)
def test_selections_instantiation(instance):
    assert isinstance(instance, Selections)

@given(instance=Guards_strategy)
@settings(max_examples=50)
def test_guards_instantiation(instance):
    assert isinstance(instance, Guards)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=core::timedAutomata::Parameter_strategy)
@settings(max_examples=50)
def test_core::timedautomata::parameter_instantiation(instance):
    assert isinstance(instance, core::timedAutomata::Parameter)

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)

@given(instance=timedAutomata::core::ComplexSystem_strategy)
@settings(max_examples=50)
def test_timedautomata::core::complexsystem_instantiation(instance):
    assert isinstance(instance, timedAutomata::core::ComplexSystem)

@given(instance=timedAutomata::core::ComplexSystem_strategy)
def test_timedautomata::core::complexsystem_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=timedAutomata::core::ComplexSystem_strategy)
def test_timedautomata::core::complexsystem_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=SystemDefinition_strategy)
@settings(max_examples=50)
def test_systemdefinition_instantiation(instance):
    assert isinstance(instance, SystemDefinition)

@given(instance=Template_strategy)
@settings(max_examples=50)
def test_template_instantiation(instance):
    assert isinstance(instance, Template)

@given(instance=TAElement_strategy)
@settings(max_examples=50)
def test_taelement_instantiation(instance):
    assert isinstance(instance, TAElement)

@given(instance=timedAutomata::core::Project_strategy)
@settings(max_examples=50)
def test_timedautomata::core::project_instantiation(instance):
    assert isinstance(instance, timedAutomata::core::Project)

@given(instance=timedAutomata::core::Project_strategy)
def test_timedautomata::core::project_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=timedAutomata::core::Project_strategy)
def test_timedautomata::core::project_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=declarations::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_declarations::fielddeclaration_instantiation(instance):
    assert isinstance(instance, declarations::FieldDeclaration)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=timedAutomata::types::SimpleType_strategy)
@settings(max_examples=50)
def test_timedautomata::types::simpletype_instantiation(instance):
    assert isinstance(instance, timedAutomata::types::SimpleType)

@given(instance=timedAutomata::types::SimpleType_strategy)
def test_timedautomata::types::simpletype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=timedAutomata::types::SimpleType_strategy)
def test_timedautomata::types::simpletype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=timedAutomata::types::Scalar_strategy)
@settings(max_examples=50)
def test_timedautomata::types::scalar_instantiation(instance):
    assert isinstance(instance, timedAutomata::types::Scalar)

@given(instance=timedAutomata::types::Struct_strategy)
@settings(max_examples=50)
def test_timedautomata::types::struct_instantiation(instance):
    assert isinstance(instance, timedAutomata::types::Struct)

@given(instance=timedAutomata::types::IntegerRange_strategy)
@settings(max_examples=50)
def test_timedautomata::types::integerrange_instantiation(instance):
    assert isinstance(instance, timedAutomata::types::IntegerRange)

@given(instance=timedAutomata::types::IdentifierType_strategy)
@settings(max_examples=50)
def test_timedautomata::types::identifiertype_instantiation(instance):
    assert isinstance(instance, timedAutomata::types::IdentifierType)

@given(instance=timedAutomata::types::Type_strategy)
@settings(max_examples=50)
def test_timedautomata::types::type_instantiation(instance):
    assert isinstance(instance, timedAutomata::types::Type)

@given(instance=timedAutomata::types::Type_strategy)
def test_timedautomata::types::type_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=timedAutomata::types::Type_strategy)
def test_timedautomata::types::type_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=base::Identifyable_strategy)
@settings(max_examples=50)
def test_base::identifyable_instantiation(instance):
    assert isinstance(instance, base::Identifyable)

@given(instance=base::Nameable_strategy)
@settings(max_examples=50)
def test_base::nameable_instantiation(instance):
    assert isinstance(instance, base::Nameable)

@given(instance=timedAutomata::core::TAElement_strategy)
@settings(max_examples=50)
def test_timedautomata::core::taelement_instantiation(instance):
    assert isinstance(instance, timedAutomata::core::TAElement)

@given(instance=core::TAElement_strategy)
@settings(max_examples=50)
def test_core::taelement_instantiation(instance):
    assert isinstance(instance, core::TAElement)

@given(instance=timedAutomata::core::Template_strategy)
@settings(max_examples=50)
def test_timedautomata::core::template_instantiation(instance):
    assert isinstance(instance, timedAutomata::core::Template)

@given(instance=timedAutomata::declarations::ChannelExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::channelexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::ChannelExpression)

@given(instance=declarations::ChannelExpression_strategy)
@settings(max_examples=50)
def test_declarations::channelexpression_instantiation(instance):
    assert isinstance(instance, declarations::ChannelExpression)

@given(instance=ChannelPriority_strategy)
@settings(max_examples=50)
def test_channelpriority_instantiation(instance):
    assert isinstance(instance, ChannelPriority)

@given(instance=timedAutomata::declarations::ComplexChannelPriority_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::complexchannelpriority_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::ComplexChannelPriority)

@given(instance=timedAutomata::declarations::ComplexChannelPriority_strategy)
def test_timedautomata::declarations::complexchannelpriority_channelOperator_type(instance):
    assert isinstance(instance.channelOperator, str)


@given(instance=timedAutomata::declarations::ComplexChannelPriority_strategy)
def test_timedautomata::declarations::complexchannelpriority_channelOperator_setter(instance):
    original = instance.channelOperator
    instance.channelOperator = original
    assert instance.channelOperator == original

@given(instance=timedAutomata::declarations::SimpleChannelPriority_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::simplechannelpriority_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::SimpleChannelPriority)

@given(instance=timedAutomata::declarations::DefaultChannelPriority_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::defaultchannelpriority_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::DefaultChannelPriority)

@given(instance=timedAutomata::declarations::ChannelPriority_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::channelpriority_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::ChannelPriority)

@given(instance=ChannelExpression_strategy)
@settings(max_examples=50)
def test_channelexpression_instantiation(instance):
    assert isinstance(instance, ChannelExpression)

@given(instance=timedAutomata::declarations::ExpressionChannelExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::expressionchannelexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::ExpressionChannelExpression)

@given(instance=timedAutomata::declarations::IdentifierChannelExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::identifierchannelexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::IdentifierChannelExpression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=timedAutomata::declarations::ForLoopStatement_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::forloopstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::ForLoopStatement)

@given(instance=timedAutomata::declarations::ReturnStatement_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::returnstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::ReturnStatement)

@given(instance=timedAutomata::declarations::WhileLoopStatement_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::whileloopstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::WhileLoopStatement)

@given(instance=timedAutomata::declarations::IfStatement_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::ifstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::IfStatement)

@given(instance=timedAutomata::declarations::DoWhileLoopStatement_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::dowhileloopstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::DoWhileLoopStatement)

@given(instance=timedAutomata::declarations::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::expressionstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::ExpressionStatement)

@given(instance=timedAutomata::declarations::Statement_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::statement_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::Statement)

@given(instance=declarations::Statement_strategy)
@settings(max_examples=50)
def test_declarations::statement_instantiation(instance):
    assert isinstance(instance, declarations::Statement)

@given(instance=declarations::Declaration_strategy)
@settings(max_examples=50)
def test_declarations::declaration_instantiation(instance):
    assert isinstance(instance, declarations::Declaration)

@given(instance=timedAutomata::declarations::Block_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::block_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::Block)

@given(instance=TAParameter_strategy)
@settings(max_examples=50)
def test_taparameter_instantiation(instance):
    assert isinstance(instance, TAParameter)

@given(instance=timedAutomata::declarations::CallByReferenceParameter_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::callbyreferenceparameter_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::CallByReferenceParameter)

@given(instance=timedAutomata::declarations::CallByValueParameter_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::callbyvalueparameter_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::CallByValueParameter)

@given(instance=timedAutomata::declarations::TAParameter_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::taparameter_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::TAParameter)

@given(instance=Initialiser_strategy)
@settings(max_examples=50)
def test_initialiser_instantiation(instance):
    assert isinstance(instance, Initialiser)

@given(instance=timedAutomata::declarations::ArrayInitialiser_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::arrayinitialiser_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::ArrayInitialiser)

@given(instance=timedAutomata::declarations::ExpressionInitialiser_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::expressioninitialiser_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::ExpressionInitialiser)

@given(instance=timedAutomata::declarations::Initialiser_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::initialiser_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::Initialiser)

@given(instance=timedAutomata::declarations::IterationStatement_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::iterationstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::IterationStatement)

@given(instance=ArrayDeclarationType_strategy)
@settings(max_examples=50)
def test_arraydeclarationtype_instantiation(instance):
    assert isinstance(instance, ArrayDeclarationType)

@given(instance=timedAutomata::declarations::ArrayExpressionType_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::arrayexpressiontype_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::ArrayExpressionType)

@given(instance=timedAutomata::declarations::ArrayDeclarationType_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::arraydeclarationtype_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::ArrayDeclarationType)

@given(instance=timedAutomata::declarations::ArrayDeclaration_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::arraydeclaration_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::ArrayDeclaration)

@given(instance=timedAutomata::declarations::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::fielddeclaration_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::FieldDeclaration)

@given(instance=declarations::ChannelPriority_strategy)
@settings(max_examples=50)
def test_declarations::channelpriority_instantiation(instance):
    assert isinstance(instance, declarations::ChannelPriority)

@given(instance=declarations::Block_strategy)
@settings(max_examples=50)
def test_declarations::block_instantiation(instance):
    assert isinstance(instance, declarations::Block)

@given(instance=timedAutomata::declarations::BlockStatement_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::blockstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::BlockStatement)

@given(instance=declarations::TAParameter_strategy)
@settings(max_examples=50)
def test_declarations::taparameter_instantiation(instance):
    assert isinstance(instance, declarations::TAParameter)

@given(instance=timedAutomata::declarations::ArrayTypeType_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::arraytypetype_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::ArrayTypeType)

@given(instance=declarations::Initialiser_strategy)
@settings(max_examples=50)
def test_declarations::initialiser_instantiation(instance):
    assert isinstance(instance, declarations::Initialiser)

@given(instance=declarations::ArrayDeclarationType_strategy)
@settings(max_examples=50)
def test_declarations::arraydeclarationtype_instantiation(instance):
    assert isinstance(instance, declarations::ArrayDeclarationType)

@given(instance=timedAutomata::declarations::VariableIdentifier_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::variableidentifier_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::VariableIdentifier)

@given(instance=declarations::VariableIdentifier_strategy)
@settings(max_examples=50)
def test_declarations::variableidentifier_instantiation(instance):
    assert isinstance(instance, declarations::VariableIdentifier)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=timedAutomata::declarations::ChannelPriorityDeclaration_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::channelprioritydeclaration_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::ChannelPriorityDeclaration)

@given(instance=timedAutomata::declarations::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::variabledeclaration_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::VariableDeclaration)

@given(instance=timedAutomata::expressions::Selection_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::selection_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::Selection)

@given(instance=types::Type_strategy)
@settings(max_examples=50)
def test_types::type_instantiation(instance):
    assert isinstance(instance, types::Type)

@given(instance=timedAutomata::declarations::FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::functiondeclaration_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::FunctionDeclaration)

@given(instance=declarations::ArrayDeclaration_strategy)
@settings(max_examples=50)
def test_declarations::arraydeclaration_instantiation(instance):
    assert isinstance(instance, declarations::ArrayDeclaration)

@given(instance=timedAutomata::declarations::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::typedeclaration_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::TypeDeclaration)

@given(instance=Identifier_strategy)
@settings(max_examples=50)
def test_identifier_instantiation(instance):
    assert isinstance(instance, Identifier)

@given(instance=Synchronisation_strategy)
@settings(max_examples=50)
def test_synchronisation_instantiation(instance):
    assert isinstance(instance, Synchronisation)

@given(instance=timedAutomata::bnf::ReceiveSynchronisation_strategy)
@settings(max_examples=50)
def test_timedautomata::bnf::receivesynchronisation_instantiation(instance):
    assert isinstance(instance, timedAutomata::bnf::ReceiveSynchronisation)

@given(instance=timedAutomata::bnf::SendSynchronisation_strategy)
@settings(max_examples=50)
def test_timedautomata::bnf::sendsynchronisation_instantiation(instance):
    assert isinstance(instance, timedAutomata::bnf::SendSynchronisation)

@given(instance=expressions::Expression_strategy)
@settings(max_examples=50)
def test_expressions::expression_instantiation(instance):
    assert isinstance(instance, expressions::Expression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=timedAutomata::expressions::IncDecExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::incdecexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::IncDecExpression)

@given(instance=timedAutomata::expressions::IncDecExpression_strategy)
def test_timedautomata::expressions::incdecexpression_increment_type(instance):
    assert isinstance(instance.increment, bool)


@given(instance=timedAutomata::expressions::IncDecExpression_strategy)
def test_timedautomata::expressions::incdecexpression_increment_setter(instance):
    original = instance.increment
    instance.increment = original
    assert instance.increment == original

@given(instance=timedAutomata::expressions::IncDecExpression_strategy)
def test_timedautomata::expressions::incdecexpression_beforeExpression_type(instance):
    assert isinstance(instance.beforeExpression, bool)


@given(instance=timedAutomata::expressions::IncDecExpression_strategy)
def test_timedautomata::expressions::incdecexpression_beforeExpression_setter(instance):
    original = instance.beforeExpression
    instance.beforeExpression = original
    assert instance.beforeExpression == original

@given(instance=timedAutomata::expressions::BinaryExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::binaryexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::BinaryExpression)

@given(instance=timedAutomata::expressions::BinaryExpression_strategy)
def test_timedautomata::expressions::binaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=timedAutomata::expressions::BinaryExpression_strategy)
def test_timedautomata::expressions::binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=timedAutomata::expressions::FixedExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::fixedexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::FixedExpression)

@given(instance=timedAutomata::expressions::FixedExpression_strategy)
def test_timedautomata::expressions::fixedexpression_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=timedAutomata::expressions::FixedExpression_strategy)
def test_timedautomata::expressions::fixedexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=timedAutomata::expressions::AssignmentExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::assignmentexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::AssignmentExpression)

@given(instance=timedAutomata::expressions::AssignmentExpression_strategy)
def test_timedautomata::expressions::assignmentexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=timedAutomata::expressions::AssignmentExpression_strategy)
def test_timedautomata::expressions::assignmentexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=timedAutomata::expressions::IdentifierExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::identifierexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::IdentifierExpression)

@given(instance=timedAutomata::expressions::SimpleIfExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::simpleifexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::SimpleIfExpression)

@given(instance=timedAutomata::expressions::ArrayVariableExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::arrayvariableexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::ArrayVariableExpression)

@given(instance=timedAutomata::expressions::WithArgumentsExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::withargumentsexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::WithArgumentsExpression)

@given(instance=timedAutomata::expressions::ForallExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::forallexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::ForallExpression)

@given(instance=timedAutomata::expressions::VariableExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::variableexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::VariableExpression)

@given(instance=timedAutomata::expressions::PointExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::pointexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::PointExpression)

@given(instance=timedAutomata::expressions::GroupingExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::groupingexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::GroupingExpression)

@given(instance=timedAutomata::expressions::ExistsExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::existsexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::ExistsExpression)

@given(instance=timedAutomata::expressions::UnaryExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::unaryexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::UnaryExpression)

@given(instance=timedAutomata::expressions::UnaryExpression_strategy)
def test_timedautomata::expressions::unaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=timedAutomata::expressions::UnaryExpression_strategy)
def test_timedautomata::expressions::unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=timedAutomata::expressions::ConstantExpression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::constantexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::ConstantExpression)

@given(instance=timedAutomata::expressions::ConstantExpression_strategy)
def test_timedautomata::expressions::constantexpression_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=timedAutomata::expressions::ConstantExpression_strategy)
def test_timedautomata::expressions::constantexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Commentable_strategy)
@settings(max_examples=50)
def test_commentable_instantiation(instance):
    assert isinstance(instance, Commentable)

@given(instance=timedAutomata::declarations::Declaration_strategy)
@settings(max_examples=50)
def test_timedautomata::declarations::declaration_instantiation(instance):
    assert isinstance(instance, timedAutomata::declarations::Declaration)

@given(instance=timedAutomata::expressions::Expression_strategy)
@settings(max_examples=50)
def test_timedautomata::expressions::expression_instantiation(instance):
    assert isinstance(instance, timedAutomata::expressions::Expression)

@given(instance=timedAutomata::base::Identifyable_strategy)
@settings(max_examples=50)
def test_timedautomata::base::identifyable_instantiation(instance):
    assert isinstance(instance, timedAutomata::base::Identifyable)

@given(instance=timedAutomata::base::Identifyable_strategy)
def test_timedautomata::base::identifyable_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=timedAutomata::base::Identifyable_strategy)
def test_timedautomata::base::identifyable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=timedAutomata::base::Commentable_strategy)
@settings(max_examples=50)
def test_timedautomata::base::commentable_instantiation(instance):
    assert isinstance(instance, timedAutomata::base::Commentable)

@given(instance=timedAutomata::base::Commentable_strategy)
def test_timedautomata::base::commentable_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=timedAutomata::base::Commentable_strategy)
def test_timedautomata::base::commentable_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=Position_strategy)
@settings(max_examples=50)
def test_position_instantiation(instance):
    assert isinstance(instance, Position)

@given(instance=timedAutomata::core::Selections_strategy)
@settings(max_examples=50)
def test_timedautomata::core::selections_instantiation(instance):
    assert isinstance(instance, timedAutomata::core::Selections)

@given(instance=timedAutomata::core::Edge_strategy)
@settings(max_examples=50)
def test_timedautomata::core::edge_instantiation(instance):
    assert isinstance(instance, timedAutomata::core::Edge)

@given(instance=timedAutomata::core::Location_strategy)
@settings(max_examples=50)
def test_timedautomata::core::location_instantiation(instance):
    assert isinstance(instance, timedAutomata::core::Location)

@given(instance=timedAutomata::core::Location_strategy)
def test_timedautomata::core::location_committed_type(instance):
    assert isinstance(instance.committed, str)


@given(instance=timedAutomata::core::Location_strategy)
def test_timedautomata::core::location_committed_setter(instance):
    original = instance.committed
    instance.committed = original
    assert instance.committed == original

@given(instance=timedAutomata::core::Location_strategy)
def test_timedautomata::core::location_urgent_type(instance):
    assert isinstance(instance.urgent, str)


@given(instance=timedAutomata::core::Location_strategy)
def test_timedautomata::core::location_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original

@given(instance=timedAutomata::core::Updates_strategy)
@settings(max_examples=50)
def test_timedautomata::core::updates_instantiation(instance):
    assert isinstance(instance, timedAutomata::core::Updates)

@given(instance=timedAutomata::core::Guards_strategy)
@settings(max_examples=50)
def test_timedautomata::core::guards_instantiation(instance):
    assert isinstance(instance, timedAutomata::core::Guards)

@given(instance=timedAutomata::bnf::Synchronisation_strategy)
@settings(max_examples=50)
def test_timedautomata::bnf::synchronisation_instantiation(instance):
    assert isinstance(instance, timedAutomata::bnf::Synchronisation)

@given(instance=timedAutomata::bnf::Identifier_strategy)
@settings(max_examples=50)
def test_timedautomata::bnf::identifier_instantiation(instance):
    assert isinstance(instance, timedAutomata::bnf::Identifier)

@given(instance=timedAutomata::bnf::Identifier_strategy)
def test_timedautomata::bnf::identifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=timedAutomata::bnf::Identifier_strategy)
def test_timedautomata::bnf::identifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=timedAutomata::base::Nameable_strategy)
@settings(max_examples=50)
def test_timedautomata::base::nameable_instantiation(instance):
    assert isinstance(instance, timedAutomata::base::Nameable)

@given(instance=timedAutomata::base::Nameable_strategy)
def test_timedautomata::base::nameable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=timedAutomata::base::Nameable_strategy)
def test_timedautomata::base::nameable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
