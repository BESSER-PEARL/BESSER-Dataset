import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stext::ReactionProperty,
    TransitionStatement,
    stext::ReactionProperties,
    Reaction,
    stext::TransitionReaction,
    Declaration,
    stext::LocalReaction,
    BuiltinEventSpec,
    stext::OnCycleEvent,
    stext::AlwaysEvent,
    stext::ExitEvent,
    stext::DefaultEvent,
    stext::EntryEvent,
    stext::Event,
    EventSpec,
    stext::BuiltinEventSpec,
    stext::TimeEventSpec,
    stext::RegularEventSpec,
    stext::EventSpec,
    stext::Exitpoint,
    stext::Entrypoint,
    stext::EventDerivation,
    stext::Scope,
    stext::TransitionStatement,
    stext::StatechartDefinition,
    DefRoot,
    stext::TransitionRoot,
    stext::StateRoot,
    stext::StatechartRoot,
    stext::DefRoot,
    stext::Root,
    stext::StateDeclaration,
    Variable,
    stext::VariableDefinition,
    stext::Statement,
    Effect,
    stext::ReactionEffect,
    Trigger,
    stext::ReactionTrigger,
    stext::Operation,
    stext::Clock,
    stext::Declaration,
    Expression,
    stext::PrimitiveValueExpression,
    stext::LogicalOrExpression,
    stext::NumericalAddSubtractExpression,
    stext::EventValueReferenceExpression,
    stext::BitwiseAndExpression,
    stext::LogicalRelationExpression,
    stext::ShiftExpression,
    stext::OperationCall,
    stext::ConditionalExpression,
    stext::NumericalMultiplyDivideExpression,
    stext::NumericalUnaryExpression,
    stext::BitwiseOrExpression,
    stext::LogicalAndExpression,
    stext::LogicalNotExpression,
    stext::BitwiseXorExpression,
    stext::ElementReferenceExpression,
    Event,
    stext::EventDefinition,
    Scope,
    stext::InterfaceScope,
    stext::InternalScope,
    stext::SimpleScope,
    Literal,
    stext::IntLiteral,
    stext::HexLiteral,
    stext::RealLiteral,
    stext::BoolLiteral,
    stext::Literal,
    stext::RegularState,
    stext::ActiveStateReferenceExpression,
    stext::EventRaisedReferenceExpression,
    stext::Variable,
    Statement,
    stext::Expression,
    stext::Assignment,
    stext::EventRaising,
    ReactionProperty,
    stext::ExitPointSpec,
    stext::EntryPointSpec,
    stext::ReactionPriority,
    AdditiveOperator,
    TimeEventType,
    Type,
    TimeUnit,
    MultiplicativeOperator,
    RelationalOperator,
    ShiftOperator,
    UnaryOperator,
    AssignmentOperator,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stext::reactionproperty_is_not_abstract():
    assert not inspect.isabstract(stext::ReactionProperty)


def test_stext::reactionproperty_constructor_exists():
    assert callable(stext::ReactionProperty.__init__)


def test_stext::reactionproperty_constructor_args():
    sig = inspect.signature(stext::ReactionProperty.__init__)
    params = list(sig.parameters.keys())



def test_transitionstatement_is_not_abstract():
    assert not inspect.isabstract(TransitionStatement)


def test_transitionstatement_constructor_exists():
    assert callable(TransitionStatement.__init__)


def test_transitionstatement_constructor_args():
    sig = inspect.signature(TransitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_stext::reactionproperties_is_not_abstract():
    assert not inspect.isabstract(stext::ReactionProperties)


def test_stext::reactionproperties_constructor_exists():
    assert callable(stext::ReactionProperties.__init__)


def test_stext::reactionproperties_constructor_args():
    sig = inspect.signature(stext::ReactionProperties.__init__)
    params = list(sig.parameters.keys())



def test_reaction_is_not_abstract():
    assert not inspect.isabstract(Reaction)


def test_reaction_constructor_exists():
    assert callable(Reaction.__init__)


def test_reaction_constructor_args():
    sig = inspect.signature(Reaction.__init__)
    params = list(sig.parameters.keys())



def test_stext::transitionreaction_is_not_abstract():
    assert not inspect.isabstract(stext::TransitionReaction)


def test_stext::transitionreaction_constructor_exists():
    assert callable(stext::TransitionReaction.__init__)


def test_stext::transitionreaction_constructor_args():
    sig = inspect.signature(stext::TransitionReaction.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_stext::localreaction_is_not_abstract():
    assert not inspect.isabstract(stext::LocalReaction)


def test_stext::localreaction_constructor_exists():
    assert callable(stext::LocalReaction.__init__)


def test_stext::localreaction_constructor_args():
    sig = inspect.signature(stext::LocalReaction.__init__)
    params = list(sig.parameters.keys())



def test_builtineventspec_is_not_abstract():
    assert not inspect.isabstract(BuiltinEventSpec)


def test_builtineventspec_constructor_exists():
    assert callable(BuiltinEventSpec.__init__)


def test_builtineventspec_constructor_args():
    sig = inspect.signature(BuiltinEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext::oncycleevent_is_not_abstract():
    assert not inspect.isabstract(stext::OnCycleEvent)


def test_stext::oncycleevent_constructor_exists():
    assert callable(stext::OnCycleEvent.__init__)


def test_stext::oncycleevent_constructor_args():
    sig = inspect.signature(stext::OnCycleEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext::alwaysevent_is_not_abstract():
    assert not inspect.isabstract(stext::AlwaysEvent)


def test_stext::alwaysevent_constructor_exists():
    assert callable(stext::AlwaysEvent.__init__)


def test_stext::alwaysevent_constructor_args():
    sig = inspect.signature(stext::AlwaysEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext::exitevent_is_not_abstract():
    assert not inspect.isabstract(stext::ExitEvent)


def test_stext::exitevent_constructor_exists():
    assert callable(stext::ExitEvent.__init__)


def test_stext::exitevent_constructor_args():
    sig = inspect.signature(stext::ExitEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext::defaultevent_is_not_abstract():
    assert not inspect.isabstract(stext::DefaultEvent)


def test_stext::defaultevent_constructor_exists():
    assert callable(stext::DefaultEvent.__init__)


def test_stext::defaultevent_constructor_args():
    sig = inspect.signature(stext::DefaultEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext::entryevent_is_not_abstract():
    assert not inspect.isabstract(stext::EntryEvent)


def test_stext::entryevent_constructor_exists():
    assert callable(stext::EntryEvent.__init__)


def test_stext::entryevent_constructor_args():
    sig = inspect.signature(stext::EntryEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext::event_is_not_abstract():
    assert not inspect.isabstract(stext::Event)


def test_stext::event_constructor_exists():
    assert callable(stext::Event.__init__)


def test_stext::event_constructor_args():
    sig = inspect.signature(stext::Event.__init__)
    params = list(sig.parameters.keys())



def test_eventspec_is_not_abstract():
    assert not inspect.isabstract(EventSpec)


def test_eventspec_constructor_exists():
    assert callable(EventSpec.__init__)


def test_eventspec_constructor_args():
    sig = inspect.signature(EventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext::builtineventspec_is_not_abstract():
    assert not inspect.isabstract(stext::BuiltinEventSpec)


def test_stext::builtineventspec_constructor_exists():
    assert callable(stext::BuiltinEventSpec.__init__)


def test_stext::builtineventspec_constructor_args():
    sig = inspect.signature(stext::BuiltinEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext::timeeventspec_is_not_abstract():
    assert not inspect.isabstract(stext::TimeEventSpec)


def test_stext::timeeventspec_constructor_exists():
    assert callable(stext::TimeEventSpec.__init__)


def test_stext::timeeventspec_constructor_args():
    sig = inspect.signature(stext::TimeEventSpec.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "type" in params, "Missing parameter 'type'"

def test_stext::timeeventspec_has_value():
    assert hasattr(stext::TimeEventSpec, "value")
    descriptor = None
    for klass in stext::TimeEventSpec.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_stext::timeeventspec_has_unit():
    assert hasattr(stext::TimeEventSpec, "unit")
    descriptor = None
    for klass in stext::TimeEventSpec.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_stext::timeeventspec_has_type():
    assert hasattr(stext::TimeEventSpec, "type")
    descriptor = None
    for klass in stext::TimeEventSpec.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_stext::regulareventspec_is_not_abstract():
    assert not inspect.isabstract(stext::RegularEventSpec)


def test_stext::regulareventspec_constructor_exists():
    assert callable(stext::RegularEventSpec.__init__)


def test_stext::regulareventspec_constructor_args():
    sig = inspect.signature(stext::RegularEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext::eventspec_is_not_abstract():
    assert not inspect.isabstract(stext::EventSpec)


def test_stext::eventspec_constructor_exists():
    assert callable(stext::EventSpec.__init__)


def test_stext::eventspec_constructor_args():
    sig = inspect.signature(stext::EventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext::exitpoint_is_not_abstract():
    assert not inspect.isabstract(stext::Exitpoint)


def test_stext::exitpoint_constructor_exists():
    assert callable(stext::Exitpoint.__init__)


def test_stext::exitpoint_constructor_args():
    sig = inspect.signature(stext::Exitpoint.__init__)
    params = list(sig.parameters.keys())



def test_stext::entrypoint_is_not_abstract():
    assert not inspect.isabstract(stext::Entrypoint)


def test_stext::entrypoint_constructor_exists():
    assert callable(stext::Entrypoint.__init__)


def test_stext::entrypoint_constructor_args():
    sig = inspect.signature(stext::Entrypoint.__init__)
    params = list(sig.parameters.keys())



def test_stext::eventderivation_is_not_abstract():
    assert not inspect.isabstract(stext::EventDerivation)


def test_stext::eventderivation_constructor_exists():
    assert callable(stext::EventDerivation.__init__)


def test_stext::eventderivation_constructor_args():
    sig = inspect.signature(stext::EventDerivation.__init__)
    params = list(sig.parameters.keys())



def test_stext::scope_is_not_abstract():
    assert not inspect.isabstract(stext::Scope)


def test_stext::scope_constructor_exists():
    assert callable(stext::Scope.__init__)


def test_stext::scope_constructor_args():
    sig = inspect.signature(stext::Scope.__init__)
    params = list(sig.parameters.keys())



def test_stext::transitionstatement_is_not_abstract():
    assert not inspect.isabstract(stext::TransitionStatement)


def test_stext::transitionstatement_constructor_exists():
    assert callable(stext::TransitionStatement.__init__)


def test_stext::transitionstatement_constructor_args():
    sig = inspect.signature(stext::TransitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_stext::statechartdefinition_is_not_abstract():
    assert not inspect.isabstract(stext::StatechartDefinition)


def test_stext::statechartdefinition_constructor_exists():
    assert callable(stext::StatechartDefinition.__init__)


def test_stext::statechartdefinition_constructor_args():
    sig = inspect.signature(stext::StatechartDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_stext::statechartdefinition_has_namespace():
    assert hasattr(stext::StatechartDefinition, "namespace")
    descriptor = None
    for klass in stext::StatechartDefinition.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_defroot_is_not_abstract():
    assert not inspect.isabstract(DefRoot)


def test_defroot_constructor_exists():
    assert callable(DefRoot.__init__)


def test_defroot_constructor_args():
    sig = inspect.signature(DefRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext::transitionroot_is_not_abstract():
    assert not inspect.isabstract(stext::TransitionRoot)


def test_stext::transitionroot_constructor_exists():
    assert callable(stext::TransitionRoot.__init__)


def test_stext::transitionroot_constructor_args():
    sig = inspect.signature(stext::TransitionRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext::stateroot_is_not_abstract():
    assert not inspect.isabstract(stext::StateRoot)


def test_stext::stateroot_constructor_exists():
    assert callable(stext::StateRoot.__init__)


def test_stext::stateroot_constructor_args():
    sig = inspect.signature(stext::StateRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext::statechartroot_is_not_abstract():
    assert not inspect.isabstract(stext::StatechartRoot)


def test_stext::statechartroot_constructor_exists():
    assert callable(stext::StatechartRoot.__init__)


def test_stext::statechartroot_constructor_args():
    sig = inspect.signature(stext::StatechartRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext::defroot_is_not_abstract():
    assert not inspect.isabstract(stext::DefRoot)


def test_stext::defroot_constructor_exists():
    assert callable(stext::DefRoot.__init__)


def test_stext::defroot_constructor_args():
    sig = inspect.signature(stext::DefRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext::root_is_not_abstract():
    assert not inspect.isabstract(stext::Root)


def test_stext::root_constructor_exists():
    assert callable(stext::Root.__init__)


def test_stext::root_constructor_args():
    sig = inspect.signature(stext::Root.__init__)
    params = list(sig.parameters.keys())



def test_stext::statedeclaration_is_not_abstract():
    assert not inspect.isabstract(stext::StateDeclaration)


def test_stext::statedeclaration_constructor_exists():
    assert callable(stext::StateDeclaration.__init__)


def test_stext::statedeclaration_constructor_args():
    sig = inspect.signature(stext::StateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_stext::variabledefinition_is_not_abstract():
    assert not inspect.isabstract(stext::VariableDefinition)


def test_stext::variabledefinition_constructor_exists():
    assert callable(stext::VariableDefinition.__init__)


def test_stext::variabledefinition_constructor_args():
    sig = inspect.signature(stext::VariableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "external" in params, "Missing parameter 'external'"
    assert "readonly" in params, "Missing parameter 'readonly'"
    assert "type" in params, "Missing parameter 'type'"

def test_stext::variabledefinition_has_external():
    assert hasattr(stext::VariableDefinition, "external")
    descriptor = None
    for klass in stext::VariableDefinition.__mro__:
        if "external" in klass.__dict__:
            descriptor = klass.__dict__["external"]
            break
    assert isinstance(descriptor, property)

def test_stext::variabledefinition_has_readonly():
    assert hasattr(stext::VariableDefinition, "readonly")
    descriptor = None
    for klass in stext::VariableDefinition.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)

def test_stext::variabledefinition_has_type():
    assert hasattr(stext::VariableDefinition, "type")
    descriptor = None
    for klass in stext::VariableDefinition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_stext::statement_is_not_abstract():
    assert not inspect.isabstract(stext::Statement)


def test_stext::statement_constructor_exists():
    assert callable(stext::Statement.__init__)


def test_stext::statement_constructor_args():
    sig = inspect.signature(stext::Statement.__init__)
    params = list(sig.parameters.keys())



def test_effect_is_not_abstract():
    assert not inspect.isabstract(Effect)


def test_effect_constructor_exists():
    assert callable(Effect.__init__)


def test_effect_constructor_args():
    sig = inspect.signature(Effect.__init__)
    params = list(sig.parameters.keys())



def test_stext::reactioneffect_is_not_abstract():
    assert not inspect.isabstract(stext::ReactionEffect)


def test_stext::reactioneffect_constructor_exists():
    assert callable(stext::ReactionEffect.__init__)


def test_stext::reactioneffect_constructor_args():
    sig = inspect.signature(stext::ReactionEffect.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_stext::reactiontrigger_is_not_abstract():
    assert not inspect.isabstract(stext::ReactionTrigger)


def test_stext::reactiontrigger_constructor_exists():
    assert callable(stext::ReactionTrigger.__init__)


def test_stext::reactiontrigger_constructor_args():
    sig = inspect.signature(stext::ReactionTrigger.__init__)
    params = list(sig.parameters.keys())



def test_stext::operation_is_not_abstract():
    assert not inspect.isabstract(stext::Operation)


def test_stext::operation_constructor_exists():
    assert callable(stext::Operation.__init__)


def test_stext::operation_constructor_args():
    sig = inspect.signature(stext::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "paramTypes" in params, "Missing parameter 'paramTypes'"

def test_stext::operation_has_type():
    assert hasattr(stext::Operation, "type")
    descriptor = None
    for klass in stext::Operation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_stext::operation_has_paramTypes():
    assert hasattr(stext::Operation, "paramTypes")
    descriptor = None
    for klass in stext::Operation.__mro__:
        if "paramTypes" in klass.__dict__:
            descriptor = klass.__dict__["paramTypes"]
            break
    assert isinstance(descriptor, property)



def test_stext::clock_is_not_abstract():
    assert not inspect.isabstract(stext::Clock)


def test_stext::clock_constructor_exists():
    assert callable(stext::Clock.__init__)


def test_stext::clock_constructor_args():
    sig = inspect.signature(stext::Clock.__init__)
    params = list(sig.parameters.keys())



def test_stext::declaration_is_not_abstract():
    assert not inspect.isabstract(stext::Declaration)


def test_stext::declaration_constructor_exists():
    assert callable(stext::Declaration.__init__)


def test_stext::declaration_constructor_args():
    sig = inspect.signature(stext::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_stext::primitivevalueexpression_is_not_abstract():
    assert not inspect.isabstract(stext::PrimitiveValueExpression)


def test_stext::primitivevalueexpression_constructor_exists():
    assert callable(stext::PrimitiveValueExpression.__init__)


def test_stext::primitivevalueexpression_constructor_args():
    sig = inspect.signature(stext::PrimitiveValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext::logicalorexpression_is_not_abstract():
    assert not inspect.isabstract(stext::LogicalOrExpression)


def test_stext::logicalorexpression_constructor_exists():
    assert callable(stext::LogicalOrExpression.__init__)


def test_stext::logicalorexpression_constructor_args():
    sig = inspect.signature(stext::LogicalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext::numericaladdsubtractexpression_is_not_abstract():
    assert not inspect.isabstract(stext::NumericalAddSubtractExpression)


def test_stext::numericaladdsubtractexpression_constructor_exists():
    assert callable(stext::NumericalAddSubtractExpression.__init__)


def test_stext::numericaladdsubtractexpression_constructor_args():
    sig = inspect.signature(stext::NumericalAddSubtractExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_stext::numericaladdsubtractexpression_has_operator():
    assert hasattr(stext::NumericalAddSubtractExpression, "operator")
    descriptor = None
    for klass in stext::NumericalAddSubtractExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_stext::eventvaluereferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext::EventValueReferenceExpression)


def test_stext::eventvaluereferenceexpression_constructor_exists():
    assert callable(stext::EventValueReferenceExpression.__init__)


def test_stext::eventvaluereferenceexpression_constructor_args():
    sig = inspect.signature(stext::EventValueReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext::bitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(stext::BitwiseAndExpression)


def test_stext::bitwiseandexpression_constructor_exists():
    assert callable(stext::BitwiseAndExpression.__init__)


def test_stext::bitwiseandexpression_constructor_args():
    sig = inspect.signature(stext::BitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext::logicalrelationexpression_is_not_abstract():
    assert not inspect.isabstract(stext::LogicalRelationExpression)


def test_stext::logicalrelationexpression_constructor_exists():
    assert callable(stext::LogicalRelationExpression.__init__)


def test_stext::logicalrelationexpression_constructor_args():
    sig = inspect.signature(stext::LogicalRelationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_stext::logicalrelationexpression_has_operator():
    assert hasattr(stext::LogicalRelationExpression, "operator")
    descriptor = None
    for klass in stext::LogicalRelationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_stext::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(stext::ShiftExpression)


def test_stext::shiftexpression_constructor_exists():
    assert callable(stext::ShiftExpression.__init__)


def test_stext::shiftexpression_constructor_args():
    sig = inspect.signature(stext::ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_stext::shiftexpression_has_operator():
    assert hasattr(stext::ShiftExpression, "operator")
    descriptor = None
    for klass in stext::ShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_stext::operationcall_is_not_abstract():
    assert not inspect.isabstract(stext::OperationCall)


def test_stext::operationcall_constructor_exists():
    assert callable(stext::OperationCall.__init__)


def test_stext::operationcall_constructor_args():
    sig = inspect.signature(stext::OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_stext::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(stext::ConditionalExpression)


def test_stext::conditionalexpression_constructor_exists():
    assert callable(stext::ConditionalExpression.__init__)


def test_stext::conditionalexpression_constructor_args():
    sig = inspect.signature(stext::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext::numericalmultiplydivideexpression_is_not_abstract():
    assert not inspect.isabstract(stext::NumericalMultiplyDivideExpression)


def test_stext::numericalmultiplydivideexpression_constructor_exists():
    assert callable(stext::NumericalMultiplyDivideExpression.__init__)


def test_stext::numericalmultiplydivideexpression_constructor_args():
    sig = inspect.signature(stext::NumericalMultiplyDivideExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_stext::numericalmultiplydivideexpression_has_operator():
    assert hasattr(stext::NumericalMultiplyDivideExpression, "operator")
    descriptor = None
    for klass in stext::NumericalMultiplyDivideExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_stext::numericalunaryexpression_is_not_abstract():
    assert not inspect.isabstract(stext::NumericalUnaryExpression)


def test_stext::numericalunaryexpression_constructor_exists():
    assert callable(stext::NumericalUnaryExpression.__init__)


def test_stext::numericalunaryexpression_constructor_args():
    sig = inspect.signature(stext::NumericalUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_stext::numericalunaryexpression_has_operator():
    assert hasattr(stext::NumericalUnaryExpression, "operator")
    descriptor = None
    for klass in stext::NumericalUnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_stext::bitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(stext::BitwiseOrExpression)


def test_stext::bitwiseorexpression_constructor_exists():
    assert callable(stext::BitwiseOrExpression.__init__)


def test_stext::bitwiseorexpression_constructor_args():
    sig = inspect.signature(stext::BitwiseOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext::logicalandexpression_is_not_abstract():
    assert not inspect.isabstract(stext::LogicalAndExpression)


def test_stext::logicalandexpression_constructor_exists():
    assert callable(stext::LogicalAndExpression.__init__)


def test_stext::logicalandexpression_constructor_args():
    sig = inspect.signature(stext::LogicalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext::logicalnotexpression_is_not_abstract():
    assert not inspect.isabstract(stext::LogicalNotExpression)


def test_stext::logicalnotexpression_constructor_exists():
    assert callable(stext::LogicalNotExpression.__init__)


def test_stext::logicalnotexpression_constructor_args():
    sig = inspect.signature(stext::LogicalNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext::bitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(stext::BitwiseXorExpression)


def test_stext::bitwisexorexpression_constructor_exists():
    assert callable(stext::BitwiseXorExpression.__init__)


def test_stext::bitwisexorexpression_constructor_args():
    sig = inspect.signature(stext::BitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext::elementreferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext::ElementReferenceExpression)


def test_stext::elementreferenceexpression_constructor_exists():
    assert callable(stext::ElementReferenceExpression.__init__)


def test_stext::elementreferenceexpression_constructor_args():
    sig = inspect.signature(stext::ElementReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_stext::eventdefinition_is_not_abstract():
    assert not inspect.isabstract(stext::EventDefinition)


def test_stext::eventdefinition_constructor_exists():
    assert callable(stext::EventDefinition.__init__)


def test_stext::eventdefinition_constructor_args():
    sig = inspect.signature(stext::EventDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "type" in params, "Missing parameter 'type'"

def test_stext::eventdefinition_has_direction():
    assert hasattr(stext::EventDefinition, "direction")
    descriptor = None
    for klass in stext::EventDefinition.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_stext::eventdefinition_has_type():
    assert hasattr(stext::EventDefinition, "type")
    descriptor = None
    for klass in stext::EventDefinition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_stext::interfacescope_is_not_abstract():
    assert not inspect.isabstract(stext::InterfaceScope)


def test_stext::interfacescope_constructor_exists():
    assert callable(stext::InterfaceScope.__init__)


def test_stext::interfacescope_constructor_args():
    sig = inspect.signature(stext::InterfaceScope.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stext::interfacescope_has_name():
    assert hasattr(stext::InterfaceScope, "name")
    descriptor = None
    for klass in stext::InterfaceScope.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stext::internalscope_is_not_abstract():
    assert not inspect.isabstract(stext::InternalScope)


def test_stext::internalscope_constructor_exists():
    assert callable(stext::InternalScope.__init__)


def test_stext::internalscope_constructor_args():
    sig = inspect.signature(stext::InternalScope.__init__)
    params = list(sig.parameters.keys())



def test_stext::simplescope_is_not_abstract():
    assert not inspect.isabstract(stext::SimpleScope)


def test_stext::simplescope_constructor_exists():
    assert callable(stext::SimpleScope.__init__)


def test_stext::simplescope_constructor_args():
    sig = inspect.signature(stext::SimpleScope.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_stext::intliteral_is_not_abstract():
    assert not inspect.isabstract(stext::IntLiteral)


def test_stext::intliteral_constructor_exists():
    assert callable(stext::IntLiteral.__init__)


def test_stext::intliteral_constructor_args():
    sig = inspect.signature(stext::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_stext::intliteral_has_value():
    assert hasattr(stext::IntLiteral, "value")
    descriptor = None
    for klass in stext::IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_stext::hexliteral_is_not_abstract():
    assert not inspect.isabstract(stext::HexLiteral)


def test_stext::hexliteral_constructor_exists():
    assert callable(stext::HexLiteral.__init__)


def test_stext::hexliteral_constructor_args():
    sig = inspect.signature(stext::HexLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_stext::hexliteral_has_value():
    assert hasattr(stext::HexLiteral, "value")
    descriptor = None
    for klass in stext::HexLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_stext::realliteral_is_not_abstract():
    assert not inspect.isabstract(stext::RealLiteral)


def test_stext::realliteral_constructor_exists():
    assert callable(stext::RealLiteral.__init__)


def test_stext::realliteral_constructor_args():
    sig = inspect.signature(stext::RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_stext::realliteral_has_value():
    assert hasattr(stext::RealLiteral, "value")
    descriptor = None
    for klass in stext::RealLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_stext::boolliteral_is_not_abstract():
    assert not inspect.isabstract(stext::BoolLiteral)


def test_stext::boolliteral_constructor_exists():
    assert callable(stext::BoolLiteral.__init__)


def test_stext::boolliteral_constructor_args():
    sig = inspect.signature(stext::BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_stext::boolliteral_has_value():
    assert hasattr(stext::BoolLiteral, "value")
    descriptor = None
    for klass in stext::BoolLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_stext::literal_is_not_abstract():
    assert not inspect.isabstract(stext::Literal)


def test_stext::literal_constructor_exists():
    assert callable(stext::Literal.__init__)


def test_stext::literal_constructor_args():
    sig = inspect.signature(stext::Literal.__init__)
    params = list(sig.parameters.keys())



def test_stext::regularstate_is_not_abstract():
    assert not inspect.isabstract(stext::RegularState)


def test_stext::regularstate_constructor_exists():
    assert callable(stext::RegularState.__init__)


def test_stext::regularstate_constructor_args():
    sig = inspect.signature(stext::RegularState.__init__)
    params = list(sig.parameters.keys())



def test_stext::activestatereferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext::ActiveStateReferenceExpression)


def test_stext::activestatereferenceexpression_constructor_exists():
    assert callable(stext::ActiveStateReferenceExpression.__init__)


def test_stext::activestatereferenceexpression_constructor_args():
    sig = inspect.signature(stext::ActiveStateReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext::eventraisedreferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext::EventRaisedReferenceExpression)


def test_stext::eventraisedreferenceexpression_constructor_exists():
    assert callable(stext::EventRaisedReferenceExpression.__init__)


def test_stext::eventraisedreferenceexpression_constructor_args():
    sig = inspect.signature(stext::EventRaisedReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext::variable_is_not_abstract():
    assert not inspect.isabstract(stext::Variable)


def test_stext::variable_constructor_exists():
    assert callable(stext::Variable.__init__)


def test_stext::variable_constructor_args():
    sig = inspect.signature(stext::Variable.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_stext::expression_is_not_abstract():
    assert not inspect.isabstract(stext::Expression)


def test_stext::expression_constructor_exists():
    assert callable(stext::Expression.__init__)


def test_stext::expression_constructor_args():
    sig = inspect.signature(stext::Expression.__init__)
    params = list(sig.parameters.keys())



def test_stext::assignment_is_not_abstract():
    assert not inspect.isabstract(stext::Assignment)


def test_stext::assignment_constructor_exists():
    assert callable(stext::Assignment.__init__)


def test_stext::assignment_constructor_args():
    sig = inspect.signature(stext::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_stext::assignment_has_operator():
    assert hasattr(stext::Assignment, "operator")
    descriptor = None
    for klass in stext::Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_stext::eventraising_is_not_abstract():
    assert not inspect.isabstract(stext::EventRaising)


def test_stext::eventraising_constructor_exists():
    assert callable(stext::EventRaising.__init__)


def test_stext::eventraising_constructor_args():
    sig = inspect.signature(stext::EventRaising.__init__)
    params = list(sig.parameters.keys())



def test_reactionproperty_is_not_abstract():
    assert not inspect.isabstract(ReactionProperty)


def test_reactionproperty_constructor_exists():
    assert callable(ReactionProperty.__init__)


def test_reactionproperty_constructor_args():
    sig = inspect.signature(ReactionProperty.__init__)
    params = list(sig.parameters.keys())



def test_stext::exitpointspec_is_not_abstract():
    assert not inspect.isabstract(stext::ExitPointSpec)


def test_stext::exitpointspec_constructor_exists():
    assert callable(stext::ExitPointSpec.__init__)


def test_stext::exitpointspec_constructor_args():
    sig = inspect.signature(stext::ExitPointSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext::entrypointspec_is_not_abstract():
    assert not inspect.isabstract(stext::EntryPointSpec)


def test_stext::entrypointspec_constructor_exists():
    assert callable(stext::EntryPointSpec.__init__)


def test_stext::entrypointspec_constructor_args():
    sig = inspect.signature(stext::EntryPointSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext::reactionpriority_is_not_abstract():
    assert not inspect.isabstract(stext::ReactionPriority)


def test_stext::reactionpriority_constructor_exists():
    assert callable(stext::ReactionPriority.__init__)


def test_stext::reactionpriority_constructor_args():
    sig = inspect.signature(stext::ReactionPriority.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_stext::reactionpriority_has_priority():
    assert hasattr(stext::ReactionPriority, "priority")
    descriptor = None
    for klass in stext::ReactionPriority.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_additiveoperator_exists():
    # Check that the Enumeration exists
    assert AdditiveOperator is not None

def test_additiveoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdditiveOperator]
    expected_literals = [
        "minus",
        "plus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditiveOperator"

def test_timeeventtype_exists():
    # Check that the Enumeration exists
    assert TimeEventType is not None

def test_timeeventtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeEventType]
    expected_literals = [
        "after",
        "every",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeEventType"

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "void",
        "boolean",
        "string",
        "real",
        "integer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "nanosecond",
        "millisecond",
        "second",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnit"

def test_multiplicativeoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicativeOperator is not None

def test_multiplicativeoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicativeOperator]
    expected_literals = [
        "mul",
        "div",
        "mod",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicativeOperator"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "smallerEqual",
        "greaterEqual",
        "equals",
        "notEquals",
        "smaller",
        "greater",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_shiftoperator_exists():
    # Check that the Enumeration exists
    assert ShiftOperator is not None

def test_shiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShiftOperator]
    expected_literals = [
        "left",
        "right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShiftOperator"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "positive",
        "negative",
        "complement",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "assign",
        "xorAssign",
        "addAssign",
        "subAssign",
        "andAssign",
        "modAssign",
        "leftShiftAssign",
        "multAssign",
        "rightShiftAssign",
        "orAssign",
        "divAssign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "LOCAL",
        "OUT",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"


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
stext::ReactionProperty_strategy = st.builds(
    stext::ReactionProperty,
)
TransitionStatement_strategy = st.builds(
    TransitionStatement,
)
stext::ReactionProperties_strategy = st.builds(
    stext::ReactionProperties,
)
Reaction_strategy = st.builds(
    Reaction,
)
stext::TransitionReaction_strategy = st.builds(
    stext::TransitionReaction,
)
Declaration_strategy = st.builds(
    Declaration,
)
stext::LocalReaction_strategy = st.builds(
    stext::LocalReaction,
)
BuiltinEventSpec_strategy = st.builds(
    BuiltinEventSpec,
)
stext::OnCycleEvent_strategy = st.builds(
    stext::OnCycleEvent,
)
stext::AlwaysEvent_strategy = st.builds(
    stext::AlwaysEvent,
)
stext::ExitEvent_strategy = st.builds(
    stext::ExitEvent,
)
stext::DefaultEvent_strategy = st.builds(
    stext::DefaultEvent,
)
stext::EntryEvent_strategy = st.builds(
    stext::EntryEvent,
)
stext::Event_strategy = st.builds(
    stext::Event,
)
EventSpec_strategy = st.builds(
    EventSpec,
)
stext::BuiltinEventSpec_strategy = st.builds(
    stext::BuiltinEventSpec,
)
stext::TimeEventSpec_strategy = st.builds(
    stext::TimeEventSpec,
    value=
        st.integers(),
    unit=
        safe_text,
    type=
        safe_text
)
stext::RegularEventSpec_strategy = st.builds(
    stext::RegularEventSpec,
)
stext::EventSpec_strategy = st.builds(
    stext::EventSpec,
)
stext::Exitpoint_strategy = st.builds(
    stext::Exitpoint,
)
stext::Entrypoint_strategy = st.builds(
    stext::Entrypoint,
)
stext::EventDerivation_strategy = st.builds(
    stext::EventDerivation,
)
stext::Scope_strategy = st.builds(
    stext::Scope,
)
stext::TransitionStatement_strategy = st.builds(
    stext::TransitionStatement,
)
stext::StatechartDefinition_strategy = st.builds(
    stext::StatechartDefinition,
    namespace=
        safe_text
)
DefRoot_strategy = st.builds(
    DefRoot,
)
stext::TransitionRoot_strategy = st.builds(
    stext::TransitionRoot,
)
stext::StateRoot_strategy = st.builds(
    stext::StateRoot,
)
stext::StatechartRoot_strategy = st.builds(
    stext::StatechartRoot,
)
stext::DefRoot_strategy = st.builds(
    stext::DefRoot,
)
stext::Root_strategy = st.builds(
    stext::Root,
)
stext::StateDeclaration_strategy = st.builds(
    stext::StateDeclaration,
)
Variable_strategy = st.builds(
    Variable,
)
stext::VariableDefinition_strategy = st.builds(
    stext::VariableDefinition,
    external=
        st.booleans(),
    readonly=
        st.booleans(),
    type=
        safe_text
)
stext::Statement_strategy = st.builds(
    stext::Statement,
)
Effect_strategy = st.builds(
    Effect,
)
stext::ReactionEffect_strategy = st.builds(
    stext::ReactionEffect,
)
Trigger_strategy = st.builds(
    Trigger,
)
stext::ReactionTrigger_strategy = st.builds(
    stext::ReactionTrigger,
)
stext::Operation_strategy = st.builds(
    stext::Operation,
    type=
        safe_text,
    paramTypes=
        safe_text
)
stext::Clock_strategy = st.builds(
    stext::Clock,
)
stext::Declaration_strategy = st.builds(
    stext::Declaration,
)
Expression_strategy = st.builds(
    Expression,
)
stext::PrimitiveValueExpression_strategy = st.builds(
    stext::PrimitiveValueExpression,
)
stext::LogicalOrExpression_strategy = st.builds(
    stext::LogicalOrExpression,
)
stext::NumericalAddSubtractExpression_strategy = st.builds(
    stext::NumericalAddSubtractExpression,
    operator=
        safe_text
)
stext::EventValueReferenceExpression_strategy = st.builds(
    stext::EventValueReferenceExpression,
)
stext::BitwiseAndExpression_strategy = st.builds(
    stext::BitwiseAndExpression,
)
stext::LogicalRelationExpression_strategy = st.builds(
    stext::LogicalRelationExpression,
    operator=
        safe_text
)
stext::ShiftExpression_strategy = st.builds(
    stext::ShiftExpression,
    operator=
        safe_text
)
stext::OperationCall_strategy = st.builds(
    stext::OperationCall,
)
stext::ConditionalExpression_strategy = st.builds(
    stext::ConditionalExpression,
)
stext::NumericalMultiplyDivideExpression_strategy = st.builds(
    stext::NumericalMultiplyDivideExpression,
    operator=
        safe_text
)
stext::NumericalUnaryExpression_strategy = st.builds(
    stext::NumericalUnaryExpression,
    operator=
        safe_text
)
stext::BitwiseOrExpression_strategy = st.builds(
    stext::BitwiseOrExpression,
)
stext::LogicalAndExpression_strategy = st.builds(
    stext::LogicalAndExpression,
)
stext::LogicalNotExpression_strategy = st.builds(
    stext::LogicalNotExpression,
)
stext::BitwiseXorExpression_strategy = st.builds(
    stext::BitwiseXorExpression,
)
stext::ElementReferenceExpression_strategy = st.builds(
    stext::ElementReferenceExpression,
)
Event_strategy = st.builds(
    Event,
)
stext::EventDefinition_strategy = st.builds(
    stext::EventDefinition,
    direction=
        safe_text,
    type=
        safe_text
)
Scope_strategy = st.builds(
    Scope,
)
stext::InterfaceScope_strategy = st.builds(
    stext::InterfaceScope,
    name=
        safe_text
)
stext::InternalScope_strategy = st.builds(
    stext::InternalScope,
)
stext::SimpleScope_strategy = st.builds(
    stext::SimpleScope,
)
Literal_strategy = st.builds(
    Literal,
)
stext::IntLiteral_strategy = st.builds(
    stext::IntLiteral,
    value=
        st.integers()
)
stext::HexLiteral_strategy = st.builds(
    stext::HexLiteral,
    value=
        st.integers()
)
stext::RealLiteral_strategy = st.builds(
    stext::RealLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
stext::BoolLiteral_strategy = st.builds(
    stext::BoolLiteral,
    value=
        st.booleans()
)
stext::Literal_strategy = st.builds(
    stext::Literal,
)
stext::RegularState_strategy = st.builds(
    stext::RegularState,
)
stext::ActiveStateReferenceExpression_strategy = st.builds(
    stext::ActiveStateReferenceExpression,
)
stext::EventRaisedReferenceExpression_strategy = st.builds(
    stext::EventRaisedReferenceExpression,
)
stext::Variable_strategy = st.builds(
    stext::Variable,
)
Statement_strategy = st.builds(
    Statement,
)
stext::Expression_strategy = st.builds(
    stext::Expression,
)
stext::Assignment_strategy = st.builds(
    stext::Assignment,
    operator=
        safe_text
)
stext::EventRaising_strategy = st.builds(
    stext::EventRaising,
)
ReactionProperty_strategy = st.builds(
    ReactionProperty,
)
stext::ExitPointSpec_strategy = st.builds(
    stext::ExitPointSpec,
)
stext::EntryPointSpec_strategy = st.builds(
    stext::EntryPointSpec,
)
stext::ReactionPriority_strategy = st.builds(
    stext::ReactionPriority,
    priority=
        st.integers()
)

@given(instance=stext::ReactionProperty_strategy)
@settings(max_examples=50)
def test_stext::reactionproperty_instantiation(instance):
    assert isinstance(instance, stext::ReactionProperty)

@given(instance=TransitionStatement_strategy)
@settings(max_examples=50)
def test_transitionstatement_instantiation(instance):
    assert isinstance(instance, TransitionStatement)

@given(instance=stext::ReactionProperties_strategy)
@settings(max_examples=50)
def test_stext::reactionproperties_instantiation(instance):
    assert isinstance(instance, stext::ReactionProperties)

@given(instance=Reaction_strategy)
@settings(max_examples=50)
def test_reaction_instantiation(instance):
    assert isinstance(instance, Reaction)

@given(instance=stext::TransitionReaction_strategy)
@settings(max_examples=50)
def test_stext::transitionreaction_instantiation(instance):
    assert isinstance(instance, stext::TransitionReaction)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=stext::LocalReaction_strategy)
@settings(max_examples=50)
def test_stext::localreaction_instantiation(instance):
    assert isinstance(instance, stext::LocalReaction)

@given(instance=BuiltinEventSpec_strategy)
@settings(max_examples=50)
def test_builtineventspec_instantiation(instance):
    assert isinstance(instance, BuiltinEventSpec)

@given(instance=stext::OnCycleEvent_strategy)
@settings(max_examples=50)
def test_stext::oncycleevent_instantiation(instance):
    assert isinstance(instance, stext::OnCycleEvent)

@given(instance=stext::AlwaysEvent_strategy)
@settings(max_examples=50)
def test_stext::alwaysevent_instantiation(instance):
    assert isinstance(instance, stext::AlwaysEvent)

@given(instance=stext::ExitEvent_strategy)
@settings(max_examples=50)
def test_stext::exitevent_instantiation(instance):
    assert isinstance(instance, stext::ExitEvent)

@given(instance=stext::DefaultEvent_strategy)
@settings(max_examples=50)
def test_stext::defaultevent_instantiation(instance):
    assert isinstance(instance, stext::DefaultEvent)

@given(instance=stext::EntryEvent_strategy)
@settings(max_examples=50)
def test_stext::entryevent_instantiation(instance):
    assert isinstance(instance, stext::EntryEvent)

@given(instance=stext::Event_strategy)
@settings(max_examples=50)
def test_stext::event_instantiation(instance):
    assert isinstance(instance, stext::Event)

@given(instance=EventSpec_strategy)
@settings(max_examples=50)
def test_eventspec_instantiation(instance):
    assert isinstance(instance, EventSpec)

@given(instance=stext::BuiltinEventSpec_strategy)
@settings(max_examples=50)
def test_stext::builtineventspec_instantiation(instance):
    assert isinstance(instance, stext::BuiltinEventSpec)

@given(instance=stext::TimeEventSpec_strategy)
@settings(max_examples=50)
def test_stext::timeeventspec_instantiation(instance):
    assert isinstance(instance, stext::TimeEventSpec)

@given(instance=stext::TimeEventSpec_strategy)
def test_stext::timeeventspec_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=stext::TimeEventSpec_strategy)
def test_stext::timeeventspec_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stext::TimeEventSpec_strategy)
def test_stext::timeeventspec_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=stext::TimeEventSpec_strategy)
def test_stext::timeeventspec_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=stext::TimeEventSpec_strategy)
def test_stext::timeeventspec_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=stext::TimeEventSpec_strategy)
def test_stext::timeeventspec_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=stext::RegularEventSpec_strategy)
@settings(max_examples=50)
def test_stext::regulareventspec_instantiation(instance):
    assert isinstance(instance, stext::RegularEventSpec)

@given(instance=stext::EventSpec_strategy)
@settings(max_examples=50)
def test_stext::eventspec_instantiation(instance):
    assert isinstance(instance, stext::EventSpec)

@given(instance=stext::Exitpoint_strategy)
@settings(max_examples=50)
def test_stext::exitpoint_instantiation(instance):
    assert isinstance(instance, stext::Exitpoint)

@given(instance=stext::Entrypoint_strategy)
@settings(max_examples=50)
def test_stext::entrypoint_instantiation(instance):
    assert isinstance(instance, stext::Entrypoint)

@given(instance=stext::EventDerivation_strategy)
@settings(max_examples=50)
def test_stext::eventderivation_instantiation(instance):
    assert isinstance(instance, stext::EventDerivation)

@given(instance=stext::Scope_strategy)
@settings(max_examples=50)
def test_stext::scope_instantiation(instance):
    assert isinstance(instance, stext::Scope)

@given(instance=stext::TransitionStatement_strategy)
@settings(max_examples=50)
def test_stext::transitionstatement_instantiation(instance):
    assert isinstance(instance, stext::TransitionStatement)

@given(instance=stext::StatechartDefinition_strategy)
@settings(max_examples=50)
def test_stext::statechartdefinition_instantiation(instance):
    assert isinstance(instance, stext::StatechartDefinition)

@given(instance=stext::StatechartDefinition_strategy)
def test_stext::statechartdefinition_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=stext::StatechartDefinition_strategy)
def test_stext::statechartdefinition_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=DefRoot_strategy)
@settings(max_examples=50)
def test_defroot_instantiation(instance):
    assert isinstance(instance, DefRoot)

@given(instance=stext::TransitionRoot_strategy)
@settings(max_examples=50)
def test_stext::transitionroot_instantiation(instance):
    assert isinstance(instance, stext::TransitionRoot)

@given(instance=stext::StateRoot_strategy)
@settings(max_examples=50)
def test_stext::stateroot_instantiation(instance):
    assert isinstance(instance, stext::StateRoot)

@given(instance=stext::StatechartRoot_strategy)
@settings(max_examples=50)
def test_stext::statechartroot_instantiation(instance):
    assert isinstance(instance, stext::StatechartRoot)

@given(instance=stext::DefRoot_strategy)
@settings(max_examples=50)
def test_stext::defroot_instantiation(instance):
    assert isinstance(instance, stext::DefRoot)

@given(instance=stext::Root_strategy)
@settings(max_examples=50)
def test_stext::root_instantiation(instance):
    assert isinstance(instance, stext::Root)

@given(instance=stext::StateDeclaration_strategy)
@settings(max_examples=50)
def test_stext::statedeclaration_instantiation(instance):
    assert isinstance(instance, stext::StateDeclaration)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=stext::VariableDefinition_strategy)
@settings(max_examples=50)
def test_stext::variabledefinition_instantiation(instance):
    assert isinstance(instance, stext::VariableDefinition)

@given(instance=stext::VariableDefinition_strategy)
def test_stext::variabledefinition_external_type(instance):
    assert isinstance(instance.external, bool)


@given(instance=stext::VariableDefinition_strategy)
def test_stext::variabledefinition_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original

@given(instance=stext::VariableDefinition_strategy)
def test_stext::variabledefinition_readonly_type(instance):
    assert isinstance(instance.readonly, bool)


@given(instance=stext::VariableDefinition_strategy)
def test_stext::variabledefinition_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=stext::VariableDefinition_strategy)
def test_stext::variabledefinition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=stext::VariableDefinition_strategy)
def test_stext::variabledefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=stext::Statement_strategy)
@settings(max_examples=50)
def test_stext::statement_instantiation(instance):
    assert isinstance(instance, stext::Statement)

@given(instance=Effect_strategy)
@settings(max_examples=50)
def test_effect_instantiation(instance):
    assert isinstance(instance, Effect)

@given(instance=stext::ReactionEffect_strategy)
@settings(max_examples=50)
def test_stext::reactioneffect_instantiation(instance):
    assert isinstance(instance, stext::ReactionEffect)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=stext::ReactionTrigger_strategy)
@settings(max_examples=50)
def test_stext::reactiontrigger_instantiation(instance):
    assert isinstance(instance, stext::ReactionTrigger)

@given(instance=stext::Operation_strategy)
@settings(max_examples=50)
def test_stext::operation_instantiation(instance):
    assert isinstance(instance, stext::Operation)

@given(instance=stext::Operation_strategy)
def test_stext::operation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=stext::Operation_strategy)
def test_stext::operation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=stext::Operation_strategy)
def test_stext::operation_paramTypes_type(instance):
    assert isinstance(instance.paramTypes, str)


@given(instance=stext::Operation_strategy)
def test_stext::operation_paramTypes_setter(instance):
    original = instance.paramTypes
    instance.paramTypes = original
    assert instance.paramTypes == original

@given(instance=stext::Clock_strategy)
@settings(max_examples=50)
def test_stext::clock_instantiation(instance):
    assert isinstance(instance, stext::Clock)

@given(instance=stext::Declaration_strategy)
@settings(max_examples=50)
def test_stext::declaration_instantiation(instance):
    assert isinstance(instance, stext::Declaration)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=stext::PrimitiveValueExpression_strategy)
@settings(max_examples=50)
def test_stext::primitivevalueexpression_instantiation(instance):
    assert isinstance(instance, stext::PrimitiveValueExpression)

@given(instance=stext::LogicalOrExpression_strategy)
@settings(max_examples=50)
def test_stext::logicalorexpression_instantiation(instance):
    assert isinstance(instance, stext::LogicalOrExpression)

@given(instance=stext::NumericalAddSubtractExpression_strategy)
@settings(max_examples=50)
def test_stext::numericaladdsubtractexpression_instantiation(instance):
    assert isinstance(instance, stext::NumericalAddSubtractExpression)

@given(instance=stext::NumericalAddSubtractExpression_strategy)
def test_stext::numericaladdsubtractexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=stext::NumericalAddSubtractExpression_strategy)
def test_stext::numericaladdsubtractexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext::EventValueReferenceExpression_strategy)
@settings(max_examples=50)
def test_stext::eventvaluereferenceexpression_instantiation(instance):
    assert isinstance(instance, stext::EventValueReferenceExpression)

@given(instance=stext::BitwiseAndExpression_strategy)
@settings(max_examples=50)
def test_stext::bitwiseandexpression_instantiation(instance):
    assert isinstance(instance, stext::BitwiseAndExpression)

@given(instance=stext::LogicalRelationExpression_strategy)
@settings(max_examples=50)
def test_stext::logicalrelationexpression_instantiation(instance):
    assert isinstance(instance, stext::LogicalRelationExpression)

@given(instance=stext::LogicalRelationExpression_strategy)
def test_stext::logicalrelationexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=stext::LogicalRelationExpression_strategy)
def test_stext::logicalrelationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext::ShiftExpression_strategy)
@settings(max_examples=50)
def test_stext::shiftexpression_instantiation(instance):
    assert isinstance(instance, stext::ShiftExpression)

@given(instance=stext::ShiftExpression_strategy)
def test_stext::shiftexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=stext::ShiftExpression_strategy)
def test_stext::shiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext::OperationCall_strategy)
@settings(max_examples=50)
def test_stext::operationcall_instantiation(instance):
    assert isinstance(instance, stext::OperationCall)

@given(instance=stext::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_stext::conditionalexpression_instantiation(instance):
    assert isinstance(instance, stext::ConditionalExpression)

@given(instance=stext::NumericalMultiplyDivideExpression_strategy)
@settings(max_examples=50)
def test_stext::numericalmultiplydivideexpression_instantiation(instance):
    assert isinstance(instance, stext::NumericalMultiplyDivideExpression)

@given(instance=stext::NumericalMultiplyDivideExpression_strategy)
def test_stext::numericalmultiplydivideexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=stext::NumericalMultiplyDivideExpression_strategy)
def test_stext::numericalmultiplydivideexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext::NumericalUnaryExpression_strategy)
@settings(max_examples=50)
def test_stext::numericalunaryexpression_instantiation(instance):
    assert isinstance(instance, stext::NumericalUnaryExpression)

@given(instance=stext::NumericalUnaryExpression_strategy)
def test_stext::numericalunaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=stext::NumericalUnaryExpression_strategy)
def test_stext::numericalunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext::BitwiseOrExpression_strategy)
@settings(max_examples=50)
def test_stext::bitwiseorexpression_instantiation(instance):
    assert isinstance(instance, stext::BitwiseOrExpression)

@given(instance=stext::LogicalAndExpression_strategy)
@settings(max_examples=50)
def test_stext::logicalandexpression_instantiation(instance):
    assert isinstance(instance, stext::LogicalAndExpression)

@given(instance=stext::LogicalNotExpression_strategy)
@settings(max_examples=50)
def test_stext::logicalnotexpression_instantiation(instance):
    assert isinstance(instance, stext::LogicalNotExpression)

@given(instance=stext::BitwiseXorExpression_strategy)
@settings(max_examples=50)
def test_stext::bitwisexorexpression_instantiation(instance):
    assert isinstance(instance, stext::BitwiseXorExpression)

@given(instance=stext::ElementReferenceExpression_strategy)
@settings(max_examples=50)
def test_stext::elementreferenceexpression_instantiation(instance):
    assert isinstance(instance, stext::ElementReferenceExpression)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=stext::EventDefinition_strategy)
@settings(max_examples=50)
def test_stext::eventdefinition_instantiation(instance):
    assert isinstance(instance, stext::EventDefinition)

@given(instance=stext::EventDefinition_strategy)
def test_stext::eventdefinition_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=stext::EventDefinition_strategy)
def test_stext::eventdefinition_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=stext::EventDefinition_strategy)
def test_stext::eventdefinition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=stext::EventDefinition_strategy)
def test_stext::eventdefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=stext::InterfaceScope_strategy)
@settings(max_examples=50)
def test_stext::interfacescope_instantiation(instance):
    assert isinstance(instance, stext::InterfaceScope)

@given(instance=stext::InterfaceScope_strategy)
def test_stext::interfacescope_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stext::InterfaceScope_strategy)
def test_stext::interfacescope_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stext::InternalScope_strategy)
@settings(max_examples=50)
def test_stext::internalscope_instantiation(instance):
    assert isinstance(instance, stext::InternalScope)

@given(instance=stext::SimpleScope_strategy)
@settings(max_examples=50)
def test_stext::simplescope_instantiation(instance):
    assert isinstance(instance, stext::SimpleScope)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=stext::IntLiteral_strategy)
@settings(max_examples=50)
def test_stext::intliteral_instantiation(instance):
    assert isinstance(instance, stext::IntLiteral)

@given(instance=stext::IntLiteral_strategy)
def test_stext::intliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=stext::IntLiteral_strategy)
def test_stext::intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stext::HexLiteral_strategy)
@settings(max_examples=50)
def test_stext::hexliteral_instantiation(instance):
    assert isinstance(instance, stext::HexLiteral)

@given(instance=stext::HexLiteral_strategy)
def test_stext::hexliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=stext::HexLiteral_strategy)
def test_stext::hexliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stext::RealLiteral_strategy)
@settings(max_examples=50)
def test_stext::realliteral_instantiation(instance):
    assert isinstance(instance, stext::RealLiteral)

@given(instance=stext::RealLiteral_strategy)
def test_stext::realliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=stext::RealLiteral_strategy)
def test_stext::realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stext::BoolLiteral_strategy)
@settings(max_examples=50)
def test_stext::boolliteral_instantiation(instance):
    assert isinstance(instance, stext::BoolLiteral)

@given(instance=stext::BoolLiteral_strategy)
def test_stext::boolliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=stext::BoolLiteral_strategy)
def test_stext::boolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stext::Literal_strategy)
@settings(max_examples=50)
def test_stext::literal_instantiation(instance):
    assert isinstance(instance, stext::Literal)

@given(instance=stext::RegularState_strategy)
@settings(max_examples=50)
def test_stext::regularstate_instantiation(instance):
    assert isinstance(instance, stext::RegularState)

@given(instance=stext::ActiveStateReferenceExpression_strategy)
@settings(max_examples=50)
def test_stext::activestatereferenceexpression_instantiation(instance):
    assert isinstance(instance, stext::ActiveStateReferenceExpression)

@given(instance=stext::EventRaisedReferenceExpression_strategy)
@settings(max_examples=50)
def test_stext::eventraisedreferenceexpression_instantiation(instance):
    assert isinstance(instance, stext::EventRaisedReferenceExpression)

@given(instance=stext::Variable_strategy)
@settings(max_examples=50)
def test_stext::variable_instantiation(instance):
    assert isinstance(instance, stext::Variable)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=stext::Expression_strategy)
@settings(max_examples=50)
def test_stext::expression_instantiation(instance):
    assert isinstance(instance, stext::Expression)

@given(instance=stext::Assignment_strategy)
@settings(max_examples=50)
def test_stext::assignment_instantiation(instance):
    assert isinstance(instance, stext::Assignment)

@given(instance=stext::Assignment_strategy)
def test_stext::assignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=stext::Assignment_strategy)
def test_stext::assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext::EventRaising_strategy)
@settings(max_examples=50)
def test_stext::eventraising_instantiation(instance):
    assert isinstance(instance, stext::EventRaising)

@given(instance=ReactionProperty_strategy)
@settings(max_examples=50)
def test_reactionproperty_instantiation(instance):
    assert isinstance(instance, ReactionProperty)

@given(instance=stext::ExitPointSpec_strategy)
@settings(max_examples=50)
def test_stext::exitpointspec_instantiation(instance):
    assert isinstance(instance, stext::ExitPointSpec)

@given(instance=stext::EntryPointSpec_strategy)
@settings(max_examples=50)
def test_stext::entrypointspec_instantiation(instance):
    assert isinstance(instance, stext::EntryPointSpec)

@given(instance=stext::ReactionPriority_strategy)
@settings(max_examples=50)
def test_stext::reactionpriority_instantiation(instance):
    assert isinstance(instance, stext::ReactionPriority)

@given(instance=stext::ReactionPriority_strategy)
def test_stext::reactionpriority_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=stext::ReactionPriority_strategy)
def test_stext::reactionpriority_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original
