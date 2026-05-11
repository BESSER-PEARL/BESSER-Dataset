import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Port,
    thingml::ProvidedPort,
    thingml::RequiredPort,
    Region,
    thingml::ParallelRegion,
    State,
    thingml::CompositeState,
    Expression,
    thingml::ExternExpression,
    Action,
    thingml::ExternStatement,
    thingml::SendAction,
    thingml::ActionBlock,
    CompositeState,
    ThingMLElement,
    thingml::AnnotatedElement,
    thingml::Event,
    thingml::PlatformAnnotation,
    Handler,
    thingml::Transition,
    thingml::InternalTransition,
    Variable,
    thingml::StateMachine,
    thingml::Property,
    Type,
    thingml::PrimitiveType,
    thingml::Enumeration,
    thingml::Thing,
    thingml::Action,
    thingml::Expression,
    thingml::TypedElement,
    thingml::ThingMLElement,
    thingml::Parameter,
    TypedElement,
    AnnotatedElement,
    thingml::PropertyAssign,
    thingml::State,
    thingml::EnumerationLiteral,
    thingml::Port,
    thingml::Handler,
    thingml::Variable,
    thingml::Message,
    thingml::Region,
    thingml::Function,
    thingml::Configuration,
    thingml::Type,
    thingml::ThingMLModel,
    thingml::InstanceRef,
    thingml::LocalVariable,
    FunctionCall,
    thingml::FunctionCallExpression,
    thingml::FunctionCallStatement,
    thingml::FunctionCall,
    thingml::PrintAction,
    thingml::ReturnAction,
    thingml::ExpressionGroup,
    PropertyReference,
    thingml::DictionaryReference,
    thingml::ArrayIndex,
    thingml::PropertyReference,
    thingml::ConfigPropertyAssign,
    thingml::ConfigInclude,
    thingml::Connector,
    thingml::Instance,
    thingml::ErrorAction,
    thingml::BinaryExpression,
    UnaryExpression,
    thingml::UnaryMinus,
    thingml::NotExpression,
    thingml::UnaryExpression,
    Literal,
    thingml::BooleanLiteral,
    thingml::DoubleLiteral,
    thingml::IntegerLiteral,
    thingml::StringLiteral,
    thingml::EnumLiteralRef,
    ControlStructure,
    thingml::ConditionalAction,
    thingml::LoopAction,
    thingml::ControlStructure,
    BinaryExpression,
    thingml::MinusExpression,
    thingml::GreaterExpression,
    thingml::DivExpression,
    thingml::LowerExpression,
    thingml::AndExpression,
    thingml::EqualsExpression,
    thingml::ModExpression,
    thingml::OrExpression,
    thingml::TimesExpression,
    thingml::PlusExpression,
    Property,
    thingml::Dictionary,
    Event,
    thingml::ReceiveMessage,
    thingml::VariableAssignment,
    thingml::Literal,
    thingml::EventReference,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_thingml::providedport_is_not_abstract():
    assert not inspect.isabstract(thingml::ProvidedPort)


def test_thingml::providedport_constructor_exists():
    assert callable(thingml::ProvidedPort.__init__)


def test_thingml::providedport_constructor_args():
    sig = inspect.signature(thingml::ProvidedPort.__init__)
    params = list(sig.parameters.keys())



def test_thingml::requiredport_is_not_abstract():
    assert not inspect.isabstract(thingml::RequiredPort)


def test_thingml::requiredport_constructor_exists():
    assert callable(thingml::RequiredPort.__init__)


def test_thingml::requiredport_constructor_args():
    sig = inspect.signature(thingml::RequiredPort.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"

def test_thingml::requiredport_has_optional():
    assert hasattr(thingml::RequiredPort, "optional")
    descriptor = None
    for klass in thingml::RequiredPort.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_region_is_not_abstract():
    assert not inspect.isabstract(Region)


def test_region_constructor_exists():
    assert callable(Region.__init__)


def test_region_constructor_args():
    sig = inspect.signature(Region.__init__)
    params = list(sig.parameters.keys())



def test_thingml::parallelregion_is_not_abstract():
    assert not inspect.isabstract(thingml::ParallelRegion)


def test_thingml::parallelregion_constructor_exists():
    assert callable(thingml::ParallelRegion.__init__)


def test_thingml::parallelregion_constructor_args():
    sig = inspect.signature(thingml::ParallelRegion.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_thingml::compositestate_is_not_abstract():
    assert not inspect.isabstract(thingml::CompositeState)


def test_thingml::compositestate_constructor_exists():
    assert callable(thingml::CompositeState.__init__)


def test_thingml::compositestate_constructor_args():
    sig = inspect.signature(thingml::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::externexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::ExternExpression)


def test_thingml::externexpression_constructor_exists():
    assert callable(thingml::ExternExpression.__init__)


def test_thingml::externexpression_constructor_args():
    sig = inspect.signature(thingml::ExternExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_thingml::externexpression_has_expression():
    assert hasattr(thingml::ExternExpression, "expression")
    descriptor = None
    for klass in thingml::ExternExpression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_thingml::externstatement_is_not_abstract():
    assert not inspect.isabstract(thingml::ExternStatement)


def test_thingml::externstatement_constructor_exists():
    assert callable(thingml::ExternStatement.__init__)


def test_thingml::externstatement_constructor_args():
    sig = inspect.signature(thingml::ExternStatement.__init__)
    params = list(sig.parameters.keys())
    assert "statement" in params, "Missing parameter 'statement'"

def test_thingml::externstatement_has_statement():
    assert hasattr(thingml::ExternStatement, "statement")
    descriptor = None
    for klass in thingml::ExternStatement.__mro__:
        if "statement" in klass.__dict__:
            descriptor = klass.__dict__["statement"]
            break
    assert isinstance(descriptor, property)



def test_thingml::sendaction_is_not_abstract():
    assert not inspect.isabstract(thingml::SendAction)


def test_thingml::sendaction_constructor_exists():
    assert callable(thingml::SendAction.__init__)


def test_thingml::sendaction_constructor_args():
    sig = inspect.signature(thingml::SendAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml::actionblock_is_not_abstract():
    assert not inspect.isabstract(thingml::ActionBlock)


def test_thingml::actionblock_constructor_exists():
    assert callable(thingml::ActionBlock.__init__)


def test_thingml::actionblock_constructor_args():
    sig = inspect.signature(thingml::ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_compositestate_is_not_abstract():
    assert not inspect.isabstract(CompositeState)


def test_compositestate_constructor_exists():
    assert callable(CompositeState.__init__)


def test_compositestate_constructor_args():
    sig = inspect.signature(CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_thingmlelement_is_not_abstract():
    assert not inspect.isabstract(ThingMLElement)


def test_thingmlelement_constructor_exists():
    assert callable(ThingMLElement.__init__)


def test_thingmlelement_constructor_args():
    sig = inspect.signature(ThingMLElement.__init__)
    params = list(sig.parameters.keys())



def test_thingml::annotatedelement_is_not_abstract():
    assert not inspect.isabstract(thingml::AnnotatedElement)


def test_thingml::annotatedelement_constructor_exists():
    assert callable(thingml::AnnotatedElement.__init__)


def test_thingml::annotatedelement_constructor_args():
    sig = inspect.signature(thingml::AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_thingml::event_is_not_abstract():
    assert not inspect.isabstract(thingml::Event)


def test_thingml::event_constructor_exists():
    assert callable(thingml::Event.__init__)


def test_thingml::event_constructor_args():
    sig = inspect.signature(thingml::Event.__init__)
    params = list(sig.parameters.keys())



def test_thingml::platformannotation_is_not_abstract():
    assert not inspect.isabstract(thingml::PlatformAnnotation)


def test_thingml::platformannotation_constructor_exists():
    assert callable(thingml::PlatformAnnotation.__init__)


def test_thingml::platformannotation_constructor_args():
    sig = inspect.signature(thingml::PlatformAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_thingml::platformannotation_has_value():
    assert hasattr(thingml::PlatformAnnotation, "value")
    descriptor = None
    for klass in thingml::PlatformAnnotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_handler_is_not_abstract():
    assert not inspect.isabstract(Handler)


def test_handler_constructor_exists():
    assert callable(Handler.__init__)


def test_handler_constructor_args():
    sig = inspect.signature(Handler.__init__)
    params = list(sig.parameters.keys())



def test_thingml::transition_is_not_abstract():
    assert not inspect.isabstract(thingml::Transition)


def test_thingml::transition_constructor_exists():
    assert callable(thingml::Transition.__init__)


def test_thingml::transition_constructor_args():
    sig = inspect.signature(thingml::Transition.__init__)
    params = list(sig.parameters.keys())



def test_thingml::internaltransition_is_not_abstract():
    assert not inspect.isabstract(thingml::InternalTransition)


def test_thingml::internaltransition_constructor_exists():
    assert callable(thingml::InternalTransition.__init__)


def test_thingml::internaltransition_constructor_args():
    sig = inspect.signature(thingml::InternalTransition.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_thingml::statemachine_is_not_abstract():
    assert not inspect.isabstract(thingml::StateMachine)


def test_thingml::statemachine_constructor_exists():
    assert callable(thingml::StateMachine.__init__)


def test_thingml::statemachine_constructor_args():
    sig = inspect.signature(thingml::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_thingml::property_is_not_abstract():
    assert not inspect.isabstract(thingml::Property)


def test_thingml::property_constructor_exists():
    assert callable(thingml::Property.__init__)


def test_thingml::property_constructor_args():
    sig = inspect.signature(thingml::Property.__init__)
    params = list(sig.parameters.keys())
    assert "changeable" in params, "Missing parameter 'changeable'"

def test_thingml::property_has_changeable():
    assert hasattr(thingml::Property, "changeable")
    descriptor = None
    for klass in thingml::Property.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_thingml::primitivetype_is_not_abstract():
    assert not inspect.isabstract(thingml::PrimitiveType)


def test_thingml::primitivetype_constructor_exists():
    assert callable(thingml::PrimitiveType.__init__)


def test_thingml::primitivetype_constructor_args():
    sig = inspect.signature(thingml::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_thingml::enumeration_is_not_abstract():
    assert not inspect.isabstract(thingml::Enumeration)


def test_thingml::enumeration_constructor_exists():
    assert callable(thingml::Enumeration.__init__)


def test_thingml::enumeration_constructor_args():
    sig = inspect.signature(thingml::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_thingml::thing_is_not_abstract():
    assert not inspect.isabstract(thingml::Thing)


def test_thingml::thing_constructor_exists():
    assert callable(thingml::Thing.__init__)


def test_thingml::thing_constructor_args():
    sig = inspect.signature(thingml::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "fragment" in params, "Missing parameter 'fragment'"

def test_thingml::thing_has_fragment():
    assert hasattr(thingml::Thing, "fragment")
    descriptor = None
    for klass in thingml::Thing.__mro__:
        if "fragment" in klass.__dict__:
            descriptor = klass.__dict__["fragment"]
            break
    assert isinstance(descriptor, property)



def test_thingml::action_is_not_abstract():
    assert not inspect.isabstract(thingml::Action)


def test_thingml::action_constructor_exists():
    assert callable(thingml::Action.__init__)


def test_thingml::action_constructor_args():
    sig = inspect.signature(thingml::Action.__init__)
    params = list(sig.parameters.keys())



def test_thingml::expression_is_not_abstract():
    assert not inspect.isabstract(thingml::Expression)


def test_thingml::expression_constructor_exists():
    assert callable(thingml::Expression.__init__)


def test_thingml::expression_constructor_args():
    sig = inspect.signature(thingml::Expression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::typedelement_is_not_abstract():
    assert not inspect.isabstract(thingml::TypedElement)


def test_thingml::typedelement_constructor_exists():
    assert callable(thingml::TypedElement.__init__)


def test_thingml::typedelement_constructor_args():
    sig = inspect.signature(thingml::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_thingml::thingmlelement_is_not_abstract():
    assert not inspect.isabstract(thingml::ThingMLElement)


def test_thingml::thingmlelement_constructor_exists():
    assert callable(thingml::ThingMLElement.__init__)


def test_thingml::thingmlelement_constructor_args():
    sig = inspect.signature(thingml::ThingMLElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::thingmlelement_has_name():
    assert hasattr(thingml::ThingMLElement, "name")
    descriptor = None
    for klass in thingml::ThingMLElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::parameter_is_not_abstract():
    assert not inspect.isabstract(thingml::Parameter)


def test_thingml::parameter_constructor_exists():
    assert callable(thingml::Parameter.__init__)


def test_thingml::parameter_constructor_args():
    sig = inspect.signature(thingml::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatedElement)


def test_annotatedelement_constructor_exists():
    assert callable(AnnotatedElement.__init__)


def test_annotatedelement_constructor_args():
    sig = inspect.signature(AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_thingml::propertyassign_is_not_abstract():
    assert not inspect.isabstract(thingml::PropertyAssign)


def test_thingml::propertyassign_constructor_exists():
    assert callable(thingml::PropertyAssign.__init__)


def test_thingml::propertyassign_constructor_args():
    sig = inspect.signature(thingml::PropertyAssign.__init__)
    params = list(sig.parameters.keys())



def test_thingml::state_is_not_abstract():
    assert not inspect.isabstract(thingml::State)


def test_thingml::state_constructor_exists():
    assert callable(thingml::State.__init__)


def test_thingml::state_constructor_args():
    sig = inspect.signature(thingml::State.__init__)
    params = list(sig.parameters.keys())



def test_thingml::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(thingml::EnumerationLiteral)


def test_thingml::enumerationliteral_constructor_exists():
    assert callable(thingml::EnumerationLiteral.__init__)


def test_thingml::enumerationliteral_constructor_args():
    sig = inspect.signature(thingml::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_thingml::port_is_not_abstract():
    assert not inspect.isabstract(thingml::Port)


def test_thingml::port_constructor_exists():
    assert callable(thingml::Port.__init__)


def test_thingml::port_constructor_args():
    sig = inspect.signature(thingml::Port.__init__)
    params = list(sig.parameters.keys())



def test_thingml::handler_is_not_abstract():
    assert not inspect.isabstract(thingml::Handler)


def test_thingml::handler_constructor_exists():
    assert callable(thingml::Handler.__init__)


def test_thingml::handler_constructor_args():
    sig = inspect.signature(thingml::Handler.__init__)
    params = list(sig.parameters.keys())



def test_thingml::variable_is_not_abstract():
    assert not inspect.isabstract(thingml::Variable)


def test_thingml::variable_constructor_exists():
    assert callable(thingml::Variable.__init__)


def test_thingml::variable_constructor_args():
    sig = inspect.signature(thingml::Variable.__init__)
    params = list(sig.parameters.keys())



def test_thingml::message_is_not_abstract():
    assert not inspect.isabstract(thingml::Message)


def test_thingml::message_constructor_exists():
    assert callable(thingml::Message.__init__)


def test_thingml::message_constructor_args():
    sig = inspect.signature(thingml::Message.__init__)
    params = list(sig.parameters.keys())



def test_thingml::region_is_not_abstract():
    assert not inspect.isabstract(thingml::Region)


def test_thingml::region_constructor_exists():
    assert callable(thingml::Region.__init__)


def test_thingml::region_constructor_args():
    sig = inspect.signature(thingml::Region.__init__)
    params = list(sig.parameters.keys())
    assert "history" in params, "Missing parameter 'history'"

def test_thingml::region_has_history():
    assert hasattr(thingml::Region, "history")
    descriptor = None
    for klass in thingml::Region.__mro__:
        if "history" in klass.__dict__:
            descriptor = klass.__dict__["history"]
            break
    assert isinstance(descriptor, property)



def test_thingml::function_is_not_abstract():
    assert not inspect.isabstract(thingml::Function)


def test_thingml::function_constructor_exists():
    assert callable(thingml::Function.__init__)


def test_thingml::function_constructor_args():
    sig = inspect.signature(thingml::Function.__init__)
    params = list(sig.parameters.keys())



def test_thingml::configuration_is_not_abstract():
    assert not inspect.isabstract(thingml::Configuration)


def test_thingml::configuration_constructor_exists():
    assert callable(thingml::Configuration.__init__)


def test_thingml::configuration_constructor_args():
    sig = inspect.signature(thingml::Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "fragment" in params, "Missing parameter 'fragment'"

def test_thingml::configuration_has_fragment():
    assert hasattr(thingml::Configuration, "fragment")
    descriptor = None
    for klass in thingml::Configuration.__mro__:
        if "fragment" in klass.__dict__:
            descriptor = klass.__dict__["fragment"]
            break
    assert isinstance(descriptor, property)



def test_thingml::type_is_not_abstract():
    assert not inspect.isabstract(thingml::Type)


def test_thingml::type_constructor_exists():
    assert callable(thingml::Type.__init__)


def test_thingml::type_constructor_args():
    sig = inspect.signature(thingml::Type.__init__)
    params = list(sig.parameters.keys())



def test_thingml::thingmlmodel_is_not_abstract():
    assert not inspect.isabstract(thingml::ThingMLModel)


def test_thingml::thingmlmodel_constructor_exists():
    assert callable(thingml::ThingMLModel.__init__)


def test_thingml::thingmlmodel_constructor_args():
    sig = inspect.signature(thingml::ThingMLModel.__init__)
    params = list(sig.parameters.keys())



def test_thingml::instanceref_is_not_abstract():
    assert not inspect.isabstract(thingml::InstanceRef)


def test_thingml::instanceref_constructor_exists():
    assert callable(thingml::InstanceRef.__init__)


def test_thingml::instanceref_constructor_args():
    sig = inspect.signature(thingml::InstanceRef.__init__)
    params = list(sig.parameters.keys())



def test_thingml::localvariable_is_not_abstract():
    assert not inspect.isabstract(thingml::LocalVariable)


def test_thingml::localvariable_constructor_exists():
    assert callable(thingml::LocalVariable.__init__)


def test_thingml::localvariable_constructor_args():
    sig = inspect.signature(thingml::LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "changeable" in params, "Missing parameter 'changeable'"

def test_thingml::localvariable_has_changeable():
    assert hasattr(thingml::LocalVariable, "changeable")
    descriptor = None
    for klass in thingml::LocalVariable.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)



def test_functioncall_is_not_abstract():
    assert not inspect.isabstract(FunctionCall)


def test_functioncall_constructor_exists():
    assert callable(FunctionCall.__init__)


def test_functioncall_constructor_args():
    sig = inspect.signature(FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_thingml::functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::FunctionCallExpression)


def test_thingml::functioncallexpression_constructor_exists():
    assert callable(thingml::FunctionCallExpression.__init__)


def test_thingml::functioncallexpression_constructor_args():
    sig = inspect.signature(thingml::FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(thingml::FunctionCallStatement)


def test_thingml::functioncallstatement_constructor_exists():
    assert callable(thingml::FunctionCallStatement.__init__)


def test_thingml::functioncallstatement_constructor_args():
    sig = inspect.signature(thingml::FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_thingml::functioncall_is_not_abstract():
    assert not inspect.isabstract(thingml::FunctionCall)


def test_thingml::functioncall_constructor_exists():
    assert callable(thingml::FunctionCall.__init__)


def test_thingml::functioncall_constructor_args():
    sig = inspect.signature(thingml::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_thingml::printaction_is_not_abstract():
    assert not inspect.isabstract(thingml::PrintAction)


def test_thingml::printaction_constructor_exists():
    assert callable(thingml::PrintAction.__init__)


def test_thingml::printaction_constructor_args():
    sig = inspect.signature(thingml::PrintAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml::returnaction_is_not_abstract():
    assert not inspect.isabstract(thingml::ReturnAction)


def test_thingml::returnaction_constructor_exists():
    assert callable(thingml::ReturnAction.__init__)


def test_thingml::returnaction_constructor_args():
    sig = inspect.signature(thingml::ReturnAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml::expressiongroup_is_not_abstract():
    assert not inspect.isabstract(thingml::ExpressionGroup)


def test_thingml::expressiongroup_constructor_exists():
    assert callable(thingml::ExpressionGroup.__init__)


def test_thingml::expressiongroup_constructor_args():
    sig = inspect.signature(thingml::ExpressionGroup.__init__)
    params = list(sig.parameters.keys())



def test_propertyreference_is_not_abstract():
    assert not inspect.isabstract(PropertyReference)


def test_propertyreference_constructor_exists():
    assert callable(PropertyReference.__init__)


def test_propertyreference_constructor_args():
    sig = inspect.signature(PropertyReference.__init__)
    params = list(sig.parameters.keys())



def test_thingml::dictionaryreference_is_not_abstract():
    assert not inspect.isabstract(thingml::DictionaryReference)


def test_thingml::dictionaryreference_constructor_exists():
    assert callable(thingml::DictionaryReference.__init__)


def test_thingml::dictionaryreference_constructor_args():
    sig = inspect.signature(thingml::DictionaryReference.__init__)
    params = list(sig.parameters.keys())



def test_thingml::arrayindex_is_not_abstract():
    assert not inspect.isabstract(thingml::ArrayIndex)


def test_thingml::arrayindex_constructor_exists():
    assert callable(thingml::ArrayIndex.__init__)


def test_thingml::arrayindex_constructor_args():
    sig = inspect.signature(thingml::ArrayIndex.__init__)
    params = list(sig.parameters.keys())



def test_thingml::propertyreference_is_not_abstract():
    assert not inspect.isabstract(thingml::PropertyReference)


def test_thingml::propertyreference_constructor_exists():
    assert callable(thingml::PropertyReference.__init__)


def test_thingml::propertyreference_constructor_args():
    sig = inspect.signature(thingml::PropertyReference.__init__)
    params = list(sig.parameters.keys())



def test_thingml::configpropertyassign_is_not_abstract():
    assert not inspect.isabstract(thingml::ConfigPropertyAssign)


def test_thingml::configpropertyassign_constructor_exists():
    assert callable(thingml::ConfigPropertyAssign.__init__)


def test_thingml::configpropertyassign_constructor_args():
    sig = inspect.signature(thingml::ConfigPropertyAssign.__init__)
    params = list(sig.parameters.keys())



def test_thingml::configinclude_is_not_abstract():
    assert not inspect.isabstract(thingml::ConfigInclude)


def test_thingml::configinclude_constructor_exists():
    assert callable(thingml::ConfigInclude.__init__)


def test_thingml::configinclude_constructor_args():
    sig = inspect.signature(thingml::ConfigInclude.__init__)
    params = list(sig.parameters.keys())



def test_thingml::connector_is_not_abstract():
    assert not inspect.isabstract(thingml::Connector)


def test_thingml::connector_constructor_exists():
    assert callable(thingml::Connector.__init__)


def test_thingml::connector_constructor_args():
    sig = inspect.signature(thingml::Connector.__init__)
    params = list(sig.parameters.keys())



def test_thingml::instance_is_not_abstract():
    assert not inspect.isabstract(thingml::Instance)


def test_thingml::instance_constructor_exists():
    assert callable(thingml::Instance.__init__)


def test_thingml::instance_constructor_args():
    sig = inspect.signature(thingml::Instance.__init__)
    params = list(sig.parameters.keys())



def test_thingml::erroraction_is_not_abstract():
    assert not inspect.isabstract(thingml::ErrorAction)


def test_thingml::erroraction_constructor_exists():
    assert callable(thingml::ErrorAction.__init__)


def test_thingml::erroraction_constructor_args():
    sig = inspect.signature(thingml::ErrorAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::BinaryExpression)


def test_thingml::binaryexpression_constructor_exists():
    assert callable(thingml::BinaryExpression.__init__)


def test_thingml::binaryexpression_constructor_args():
    sig = inspect.signature(thingml::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::unaryminus_is_not_abstract():
    assert not inspect.isabstract(thingml::UnaryMinus)


def test_thingml::unaryminus_constructor_exists():
    assert callable(thingml::UnaryMinus.__init__)


def test_thingml::unaryminus_constructor_args():
    sig = inspect.signature(thingml::UnaryMinus.__init__)
    params = list(sig.parameters.keys())



def test_thingml::notexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::NotExpression)


def test_thingml::notexpression_constructor_exists():
    assert callable(thingml::NotExpression.__init__)


def test_thingml::notexpression_constructor_args():
    sig = inspect.signature(thingml::NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::UnaryExpression)


def test_thingml::unaryexpression_constructor_exists():
    assert callable(thingml::UnaryExpression.__init__)


def test_thingml::unaryexpression_constructor_args():
    sig = inspect.signature(thingml::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_thingml::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(thingml::BooleanLiteral)


def test_thingml::booleanliteral_constructor_exists():
    assert callable(thingml::BooleanLiteral.__init__)


def test_thingml::booleanliteral_constructor_args():
    sig = inspect.signature(thingml::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "boolValue" in params, "Missing parameter 'boolValue'"

def test_thingml::booleanliteral_has_boolValue():
    assert hasattr(thingml::BooleanLiteral, "boolValue")
    descriptor = None
    for klass in thingml::BooleanLiteral.__mro__:
        if "boolValue" in klass.__dict__:
            descriptor = klass.__dict__["boolValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml::doubleliteral_is_not_abstract():
    assert not inspect.isabstract(thingml::DoubleLiteral)


def test_thingml::doubleliteral_constructor_exists():
    assert callable(thingml::DoubleLiteral.__init__)


def test_thingml::doubleliteral_constructor_args():
    sig = inspect.signature(thingml::DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "doubleValue" in params, "Missing parameter 'doubleValue'"

def test_thingml::doubleliteral_has_doubleValue():
    assert hasattr(thingml::DoubleLiteral, "doubleValue")
    descriptor = None
    for klass in thingml::DoubleLiteral.__mro__:
        if "doubleValue" in klass.__dict__:
            descriptor = klass.__dict__["doubleValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml::integerliteral_is_not_abstract():
    assert not inspect.isabstract(thingml::IntegerLiteral)


def test_thingml::integerliteral_constructor_exists():
    assert callable(thingml::IntegerLiteral.__init__)


def test_thingml::integerliteral_constructor_args():
    sig = inspect.signature(thingml::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "intValue" in params, "Missing parameter 'intValue'"

def test_thingml::integerliteral_has_intValue():
    assert hasattr(thingml::IntegerLiteral, "intValue")
    descriptor = None
    for klass in thingml::IntegerLiteral.__mro__:
        if "intValue" in klass.__dict__:
            descriptor = klass.__dict__["intValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml::stringliteral_is_not_abstract():
    assert not inspect.isabstract(thingml::StringLiteral)


def test_thingml::stringliteral_constructor_exists():
    assert callable(thingml::StringLiteral.__init__)


def test_thingml::stringliteral_constructor_args():
    sig = inspect.signature(thingml::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "stringValue" in params, "Missing parameter 'stringValue'"

def test_thingml::stringliteral_has_stringValue():
    assert hasattr(thingml::StringLiteral, "stringValue")
    descriptor = None
    for klass in thingml::StringLiteral.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml::enumliteralref_is_not_abstract():
    assert not inspect.isabstract(thingml::EnumLiteralRef)


def test_thingml::enumliteralref_constructor_exists():
    assert callable(thingml::EnumLiteralRef.__init__)


def test_thingml::enumliteralref_constructor_args():
    sig = inspect.signature(thingml::EnumLiteralRef.__init__)
    params = list(sig.parameters.keys())



def test_controlstructure_is_not_abstract():
    assert not inspect.isabstract(ControlStructure)


def test_controlstructure_constructor_exists():
    assert callable(ControlStructure.__init__)


def test_controlstructure_constructor_args():
    sig = inspect.signature(ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_thingml::conditionalaction_is_not_abstract():
    assert not inspect.isabstract(thingml::ConditionalAction)


def test_thingml::conditionalaction_constructor_exists():
    assert callable(thingml::ConditionalAction.__init__)


def test_thingml::conditionalaction_constructor_args():
    sig = inspect.signature(thingml::ConditionalAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml::loopaction_is_not_abstract():
    assert not inspect.isabstract(thingml::LoopAction)


def test_thingml::loopaction_constructor_exists():
    assert callable(thingml::LoopAction.__init__)


def test_thingml::loopaction_constructor_args():
    sig = inspect.signature(thingml::LoopAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml::controlstructure_is_not_abstract():
    assert not inspect.isabstract(thingml::ControlStructure)


def test_thingml::controlstructure_constructor_exists():
    assert callable(thingml::ControlStructure.__init__)


def test_thingml::controlstructure_constructor_args():
    sig = inspect.signature(thingml::ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::minusexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::MinusExpression)


def test_thingml::minusexpression_constructor_exists():
    assert callable(thingml::MinusExpression.__init__)


def test_thingml::minusexpression_constructor_args():
    sig = inspect.signature(thingml::MinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::greaterexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::GreaterExpression)


def test_thingml::greaterexpression_constructor_exists():
    assert callable(thingml::GreaterExpression.__init__)


def test_thingml::greaterexpression_constructor_args():
    sig = inspect.signature(thingml::GreaterExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::divexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::DivExpression)


def test_thingml::divexpression_constructor_exists():
    assert callable(thingml::DivExpression.__init__)


def test_thingml::divexpression_constructor_args():
    sig = inspect.signature(thingml::DivExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::lowerexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::LowerExpression)


def test_thingml::lowerexpression_constructor_exists():
    assert callable(thingml::LowerExpression.__init__)


def test_thingml::lowerexpression_constructor_args():
    sig = inspect.signature(thingml::LowerExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::andexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::AndExpression)


def test_thingml::andexpression_constructor_exists():
    assert callable(thingml::AndExpression.__init__)


def test_thingml::andexpression_constructor_args():
    sig = inspect.signature(thingml::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::equalsexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::EqualsExpression)


def test_thingml::equalsexpression_constructor_exists():
    assert callable(thingml::EqualsExpression.__init__)


def test_thingml::equalsexpression_constructor_args():
    sig = inspect.signature(thingml::EqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::modexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::ModExpression)


def test_thingml::modexpression_constructor_exists():
    assert callable(thingml::ModExpression.__init__)


def test_thingml::modexpression_constructor_args():
    sig = inspect.signature(thingml::ModExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::orexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::OrExpression)


def test_thingml::orexpression_constructor_exists():
    assert callable(thingml::OrExpression.__init__)


def test_thingml::orexpression_constructor_args():
    sig = inspect.signature(thingml::OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::timesexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::TimesExpression)


def test_thingml::timesexpression_constructor_exists():
    assert callable(thingml::TimesExpression.__init__)


def test_thingml::timesexpression_constructor_args():
    sig = inspect.signature(thingml::TimesExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::plusexpression_is_not_abstract():
    assert not inspect.isabstract(thingml::PlusExpression)


def test_thingml::plusexpression_constructor_exists():
    assert callable(thingml::PlusExpression.__init__)


def test_thingml::plusexpression_constructor_args():
    sig = inspect.signature(thingml::PlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_thingml::dictionary_is_not_abstract():
    assert not inspect.isabstract(thingml::Dictionary)


def test_thingml::dictionary_constructor_exists():
    assert callable(thingml::Dictionary.__init__)


def test_thingml::dictionary_constructor_args():
    sig = inspect.signature(thingml::Dictionary.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_thingml::receivemessage_is_not_abstract():
    assert not inspect.isabstract(thingml::ReceiveMessage)


def test_thingml::receivemessage_constructor_exists():
    assert callable(thingml::ReceiveMessage.__init__)


def test_thingml::receivemessage_constructor_args():
    sig = inspect.signature(thingml::ReceiveMessage.__init__)
    params = list(sig.parameters.keys())



def test_thingml::variableassignment_is_not_abstract():
    assert not inspect.isabstract(thingml::VariableAssignment)


def test_thingml::variableassignment_constructor_exists():
    assert callable(thingml::VariableAssignment.__init__)


def test_thingml::variableassignment_constructor_args():
    sig = inspect.signature(thingml::VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_thingml::literal_is_not_abstract():
    assert not inspect.isabstract(thingml::Literal)


def test_thingml::literal_constructor_exists():
    assert callable(thingml::Literal.__init__)


def test_thingml::literal_constructor_args():
    sig = inspect.signature(thingml::Literal.__init__)
    params = list(sig.parameters.keys())



def test_thingml::eventreference_is_not_abstract():
    assert not inspect.isabstract(thingml::EventReference)


def test_thingml::eventreference_constructor_exists():
    assert callable(thingml::EventReference.__init__)


def test_thingml::eventreference_constructor_args():
    sig = inspect.signature(thingml::EventReference.__init__)
    params = list(sig.parameters.keys())


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
Port_strategy = st.builds(
    Port,
)
thingml::ProvidedPort_strategy = st.builds(
    thingml::ProvidedPort,
)
thingml::RequiredPort_strategy = st.builds(
    thingml::RequiredPort,
    optional=
        st.booleans()
)
Region_strategy = st.builds(
    Region,
)
thingml::ParallelRegion_strategy = st.builds(
    thingml::ParallelRegion,
)
State_strategy = st.builds(
    State,
)
thingml::CompositeState_strategy = st.builds(
    thingml::CompositeState,
)
Expression_strategy = st.builds(
    Expression,
)
thingml::ExternExpression_strategy = st.builds(
    thingml::ExternExpression,
    expression=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
thingml::ExternStatement_strategy = st.builds(
    thingml::ExternStatement,
    statement=
        safe_text
)
thingml::SendAction_strategy = st.builds(
    thingml::SendAction,
)
thingml::ActionBlock_strategy = st.builds(
    thingml::ActionBlock,
)
CompositeState_strategy = st.builds(
    CompositeState,
)
ThingMLElement_strategy = st.builds(
    ThingMLElement,
)
thingml::AnnotatedElement_strategy = st.builds(
    thingml::AnnotatedElement,
)
thingml::Event_strategy = st.builds(
    thingml::Event,
)
thingml::PlatformAnnotation_strategy = st.builds(
    thingml::PlatformAnnotation,
    value=
        safe_text
)
Handler_strategy = st.builds(
    Handler,
)
thingml::Transition_strategy = st.builds(
    thingml::Transition,
)
thingml::InternalTransition_strategy = st.builds(
    thingml::InternalTransition,
)
Variable_strategy = st.builds(
    Variable,
)
thingml::StateMachine_strategy = st.builds(
    thingml::StateMachine,
)
thingml::Property_strategy = st.builds(
    thingml::Property,
    changeable=
        st.booleans()
)
Type_strategy = st.builds(
    Type,
)
thingml::PrimitiveType_strategy = st.builds(
    thingml::PrimitiveType,
)
thingml::Enumeration_strategy = st.builds(
    thingml::Enumeration,
)
thingml::Thing_strategy = st.builds(
    thingml::Thing,
    fragment=
        st.booleans()
)
thingml::Action_strategy = st.builds(
    thingml::Action,
)
thingml::Expression_strategy = st.builds(
    thingml::Expression,
)
thingml::TypedElement_strategy = st.builds(
    thingml::TypedElement,
)
thingml::ThingMLElement_strategy = st.builds(
    thingml::ThingMLElement,
    name=
        safe_text
)
thingml::Parameter_strategy = st.builds(
    thingml::Parameter,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
AnnotatedElement_strategy = st.builds(
    AnnotatedElement,
)
thingml::PropertyAssign_strategy = st.builds(
    thingml::PropertyAssign,
)
thingml::State_strategy = st.builds(
    thingml::State,
)
thingml::EnumerationLiteral_strategy = st.builds(
    thingml::EnumerationLiteral,
)
thingml::Port_strategy = st.builds(
    thingml::Port,
)
thingml::Handler_strategy = st.builds(
    thingml::Handler,
)
thingml::Variable_strategy = st.builds(
    thingml::Variable,
)
thingml::Message_strategy = st.builds(
    thingml::Message,
)
thingml::Region_strategy = st.builds(
    thingml::Region,
    history=
        st.booleans()
)
thingml::Function_strategy = st.builds(
    thingml::Function,
)
thingml::Configuration_strategy = st.builds(
    thingml::Configuration,
    fragment=
        st.booleans()
)
thingml::Type_strategy = st.builds(
    thingml::Type,
)
thingml::ThingMLModel_strategy = st.builds(
    thingml::ThingMLModel,
)
thingml::InstanceRef_strategy = st.builds(
    thingml::InstanceRef,
)
thingml::LocalVariable_strategy = st.builds(
    thingml::LocalVariable,
    changeable=
        st.booleans()
)
FunctionCall_strategy = st.builds(
    FunctionCall,
)
thingml::FunctionCallExpression_strategy = st.builds(
    thingml::FunctionCallExpression,
)
thingml::FunctionCallStatement_strategy = st.builds(
    thingml::FunctionCallStatement,
)
thingml::FunctionCall_strategy = st.builds(
    thingml::FunctionCall,
)
thingml::PrintAction_strategy = st.builds(
    thingml::PrintAction,
)
thingml::ReturnAction_strategy = st.builds(
    thingml::ReturnAction,
)
thingml::ExpressionGroup_strategy = st.builds(
    thingml::ExpressionGroup,
)
PropertyReference_strategy = st.builds(
    PropertyReference,
)
thingml::DictionaryReference_strategy = st.builds(
    thingml::DictionaryReference,
)
thingml::ArrayIndex_strategy = st.builds(
    thingml::ArrayIndex,
)
thingml::PropertyReference_strategy = st.builds(
    thingml::PropertyReference,
)
thingml::ConfigPropertyAssign_strategy = st.builds(
    thingml::ConfigPropertyAssign,
)
thingml::ConfigInclude_strategy = st.builds(
    thingml::ConfigInclude,
)
thingml::Connector_strategy = st.builds(
    thingml::Connector,
)
thingml::Instance_strategy = st.builds(
    thingml::Instance,
)
thingml::ErrorAction_strategy = st.builds(
    thingml::ErrorAction,
)
thingml::BinaryExpression_strategy = st.builds(
    thingml::BinaryExpression,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
thingml::UnaryMinus_strategy = st.builds(
    thingml::UnaryMinus,
)
thingml::NotExpression_strategy = st.builds(
    thingml::NotExpression,
)
thingml::UnaryExpression_strategy = st.builds(
    thingml::UnaryExpression,
)
Literal_strategy = st.builds(
    Literal,
)
thingml::BooleanLiteral_strategy = st.builds(
    thingml::BooleanLiteral,
    boolValue=
        st.booleans()
)
thingml::DoubleLiteral_strategy = st.builds(
    thingml::DoubleLiteral,
    doubleValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
thingml::IntegerLiteral_strategy = st.builds(
    thingml::IntegerLiteral,
    intValue=
        st.integers()
)
thingml::StringLiteral_strategy = st.builds(
    thingml::StringLiteral,
    stringValue=
        safe_text
)
thingml::EnumLiteralRef_strategy = st.builds(
    thingml::EnumLiteralRef,
)
ControlStructure_strategy = st.builds(
    ControlStructure,
)
thingml::ConditionalAction_strategy = st.builds(
    thingml::ConditionalAction,
)
thingml::LoopAction_strategy = st.builds(
    thingml::LoopAction,
)
thingml::ControlStructure_strategy = st.builds(
    thingml::ControlStructure,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
thingml::MinusExpression_strategy = st.builds(
    thingml::MinusExpression,
)
thingml::GreaterExpression_strategy = st.builds(
    thingml::GreaterExpression,
)
thingml::DivExpression_strategy = st.builds(
    thingml::DivExpression,
)
thingml::LowerExpression_strategy = st.builds(
    thingml::LowerExpression,
)
thingml::AndExpression_strategy = st.builds(
    thingml::AndExpression,
)
thingml::EqualsExpression_strategy = st.builds(
    thingml::EqualsExpression,
)
thingml::ModExpression_strategy = st.builds(
    thingml::ModExpression,
)
thingml::OrExpression_strategy = st.builds(
    thingml::OrExpression,
)
thingml::TimesExpression_strategy = st.builds(
    thingml::TimesExpression,
)
thingml::PlusExpression_strategy = st.builds(
    thingml::PlusExpression,
)
Property_strategy = st.builds(
    Property,
)
thingml::Dictionary_strategy = st.builds(
    thingml::Dictionary,
)
Event_strategy = st.builds(
    Event,
)
thingml::ReceiveMessage_strategy = st.builds(
    thingml::ReceiveMessage,
)
thingml::VariableAssignment_strategy = st.builds(
    thingml::VariableAssignment,
)
thingml::Literal_strategy = st.builds(
    thingml::Literal,
)
thingml::EventReference_strategy = st.builds(
    thingml::EventReference,
)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=thingml::ProvidedPort_strategy)
@settings(max_examples=50)
def test_thingml::providedport_instantiation(instance):
    assert isinstance(instance, thingml::ProvidedPort)

@given(instance=thingml::RequiredPort_strategy)
@settings(max_examples=50)
def test_thingml::requiredport_instantiation(instance):
    assert isinstance(instance, thingml::RequiredPort)

@given(instance=thingml::RequiredPort_strategy)
def test_thingml::requiredport_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=thingml::RequiredPort_strategy)
def test_thingml::requiredport_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=Region_strategy)
@settings(max_examples=50)
def test_region_instantiation(instance):
    assert isinstance(instance, Region)

@given(instance=thingml::ParallelRegion_strategy)
@settings(max_examples=50)
def test_thingml::parallelregion_instantiation(instance):
    assert isinstance(instance, thingml::ParallelRegion)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=thingml::CompositeState_strategy)
@settings(max_examples=50)
def test_thingml::compositestate_instantiation(instance):
    assert isinstance(instance, thingml::CompositeState)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=thingml::ExternExpression_strategy)
@settings(max_examples=50)
def test_thingml::externexpression_instantiation(instance):
    assert isinstance(instance, thingml::ExternExpression)

@given(instance=thingml::ExternExpression_strategy)
def test_thingml::externexpression_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=thingml::ExternExpression_strategy)
def test_thingml::externexpression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=thingml::ExternStatement_strategy)
@settings(max_examples=50)
def test_thingml::externstatement_instantiation(instance):
    assert isinstance(instance, thingml::ExternStatement)

@given(instance=thingml::ExternStatement_strategy)
def test_thingml::externstatement_statement_type(instance):
    assert isinstance(instance.statement, str)


@given(instance=thingml::ExternStatement_strategy)
def test_thingml::externstatement_statement_setter(instance):
    original = instance.statement
    instance.statement = original
    assert instance.statement == original

@given(instance=thingml::SendAction_strategy)
@settings(max_examples=50)
def test_thingml::sendaction_instantiation(instance):
    assert isinstance(instance, thingml::SendAction)

@given(instance=thingml::ActionBlock_strategy)
@settings(max_examples=50)
def test_thingml::actionblock_instantiation(instance):
    assert isinstance(instance, thingml::ActionBlock)

@given(instance=CompositeState_strategy)
@settings(max_examples=50)
def test_compositestate_instantiation(instance):
    assert isinstance(instance, CompositeState)

@given(instance=ThingMLElement_strategy)
@settings(max_examples=50)
def test_thingmlelement_instantiation(instance):
    assert isinstance(instance, ThingMLElement)

@given(instance=thingml::AnnotatedElement_strategy)
@settings(max_examples=50)
def test_thingml::annotatedelement_instantiation(instance):
    assert isinstance(instance, thingml::AnnotatedElement)

@given(instance=thingml::Event_strategy)
@settings(max_examples=50)
def test_thingml::event_instantiation(instance):
    assert isinstance(instance, thingml::Event)

@given(instance=thingml::PlatformAnnotation_strategy)
@settings(max_examples=50)
def test_thingml::platformannotation_instantiation(instance):
    assert isinstance(instance, thingml::PlatformAnnotation)

@given(instance=thingml::PlatformAnnotation_strategy)
def test_thingml::platformannotation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=thingml::PlatformAnnotation_strategy)
def test_thingml::platformannotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Handler_strategy)
@settings(max_examples=50)
def test_handler_instantiation(instance):
    assert isinstance(instance, Handler)

@given(instance=thingml::Transition_strategy)
@settings(max_examples=50)
def test_thingml::transition_instantiation(instance):
    assert isinstance(instance, thingml::Transition)

@given(instance=thingml::InternalTransition_strategy)
@settings(max_examples=50)
def test_thingml::internaltransition_instantiation(instance):
    assert isinstance(instance, thingml::InternalTransition)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=thingml::StateMachine_strategy)
@settings(max_examples=50)
def test_thingml::statemachine_instantiation(instance):
    assert isinstance(instance, thingml::StateMachine)

@given(instance=thingml::Property_strategy)
@settings(max_examples=50)
def test_thingml::property_instantiation(instance):
    assert isinstance(instance, thingml::Property)

@given(instance=thingml::Property_strategy)
def test_thingml::property_changeable_type(instance):
    assert isinstance(instance.changeable, bool)


@given(instance=thingml::Property_strategy)
def test_thingml::property_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=thingml::PrimitiveType_strategy)
@settings(max_examples=50)
def test_thingml::primitivetype_instantiation(instance):
    assert isinstance(instance, thingml::PrimitiveType)

@given(instance=thingml::Enumeration_strategy)
@settings(max_examples=50)
def test_thingml::enumeration_instantiation(instance):
    assert isinstance(instance, thingml::Enumeration)

@given(instance=thingml::Thing_strategy)
@settings(max_examples=50)
def test_thingml::thing_instantiation(instance):
    assert isinstance(instance, thingml::Thing)

@given(instance=thingml::Thing_strategy)
def test_thingml::thing_fragment_type(instance):
    assert isinstance(instance.fragment, bool)


@given(instance=thingml::Thing_strategy)
def test_thingml::thing_fragment_setter(instance):
    original = instance.fragment
    instance.fragment = original
    assert instance.fragment == original

@given(instance=thingml::Action_strategy)
@settings(max_examples=50)
def test_thingml::action_instantiation(instance):
    assert isinstance(instance, thingml::Action)

@given(instance=thingml::Expression_strategy)
@settings(max_examples=50)
def test_thingml::expression_instantiation(instance):
    assert isinstance(instance, thingml::Expression)

@given(instance=thingml::TypedElement_strategy)
@settings(max_examples=50)
def test_thingml::typedelement_instantiation(instance):
    assert isinstance(instance, thingml::TypedElement)

@given(instance=thingml::ThingMLElement_strategy)
@settings(max_examples=50)
def test_thingml::thingmlelement_instantiation(instance):
    assert isinstance(instance, thingml::ThingMLElement)

@given(instance=thingml::ThingMLElement_strategy)
def test_thingml::thingmlelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingml::ThingMLElement_strategy)
def test_thingml::thingmlelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingml::Parameter_strategy)
@settings(max_examples=50)
def test_thingml::parameter_instantiation(instance):
    assert isinstance(instance, thingml::Parameter)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=AnnotatedElement_strategy)
@settings(max_examples=50)
def test_annotatedelement_instantiation(instance):
    assert isinstance(instance, AnnotatedElement)

@given(instance=thingml::PropertyAssign_strategy)
@settings(max_examples=50)
def test_thingml::propertyassign_instantiation(instance):
    assert isinstance(instance, thingml::PropertyAssign)

@given(instance=thingml::State_strategy)
@settings(max_examples=50)
def test_thingml::state_instantiation(instance):
    assert isinstance(instance, thingml::State)

@given(instance=thingml::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_thingml::enumerationliteral_instantiation(instance):
    assert isinstance(instance, thingml::EnumerationLiteral)

@given(instance=thingml::Port_strategy)
@settings(max_examples=50)
def test_thingml::port_instantiation(instance):
    assert isinstance(instance, thingml::Port)

@given(instance=thingml::Handler_strategy)
@settings(max_examples=50)
def test_thingml::handler_instantiation(instance):
    assert isinstance(instance, thingml::Handler)

@given(instance=thingml::Variable_strategy)
@settings(max_examples=50)
def test_thingml::variable_instantiation(instance):
    assert isinstance(instance, thingml::Variable)

@given(instance=thingml::Message_strategy)
@settings(max_examples=50)
def test_thingml::message_instantiation(instance):
    assert isinstance(instance, thingml::Message)

@given(instance=thingml::Region_strategy)
@settings(max_examples=50)
def test_thingml::region_instantiation(instance):
    assert isinstance(instance, thingml::Region)

@given(instance=thingml::Region_strategy)
def test_thingml::region_history_type(instance):
    assert isinstance(instance.history, bool)


@given(instance=thingml::Region_strategy)
def test_thingml::region_history_setter(instance):
    original = instance.history
    instance.history = original
    assert instance.history == original

@given(instance=thingml::Function_strategy)
@settings(max_examples=50)
def test_thingml::function_instantiation(instance):
    assert isinstance(instance, thingml::Function)

@given(instance=thingml::Configuration_strategy)
@settings(max_examples=50)
def test_thingml::configuration_instantiation(instance):
    assert isinstance(instance, thingml::Configuration)

@given(instance=thingml::Configuration_strategy)
def test_thingml::configuration_fragment_type(instance):
    assert isinstance(instance.fragment, bool)


@given(instance=thingml::Configuration_strategy)
def test_thingml::configuration_fragment_setter(instance):
    original = instance.fragment
    instance.fragment = original
    assert instance.fragment == original

@given(instance=thingml::Type_strategy)
@settings(max_examples=50)
def test_thingml::type_instantiation(instance):
    assert isinstance(instance, thingml::Type)

@given(instance=thingml::ThingMLModel_strategy)
@settings(max_examples=50)
def test_thingml::thingmlmodel_instantiation(instance):
    assert isinstance(instance, thingml::ThingMLModel)

@given(instance=thingml::InstanceRef_strategy)
@settings(max_examples=50)
def test_thingml::instanceref_instantiation(instance):
    assert isinstance(instance, thingml::InstanceRef)

@given(instance=thingml::LocalVariable_strategy)
@settings(max_examples=50)
def test_thingml::localvariable_instantiation(instance):
    assert isinstance(instance, thingml::LocalVariable)

@given(instance=thingml::LocalVariable_strategy)
def test_thingml::localvariable_changeable_type(instance):
    assert isinstance(instance.changeable, bool)


@given(instance=thingml::LocalVariable_strategy)
def test_thingml::localvariable_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original

@given(instance=FunctionCall_strategy)
@settings(max_examples=50)
def test_functioncall_instantiation(instance):
    assert isinstance(instance, FunctionCall)

@given(instance=thingml::FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_thingml::functioncallexpression_instantiation(instance):
    assert isinstance(instance, thingml::FunctionCallExpression)

@given(instance=thingml::FunctionCallStatement_strategy)
@settings(max_examples=50)
def test_thingml::functioncallstatement_instantiation(instance):
    assert isinstance(instance, thingml::FunctionCallStatement)

@given(instance=thingml::FunctionCall_strategy)
@settings(max_examples=50)
def test_thingml::functioncall_instantiation(instance):
    assert isinstance(instance, thingml::FunctionCall)

@given(instance=thingml::PrintAction_strategy)
@settings(max_examples=50)
def test_thingml::printaction_instantiation(instance):
    assert isinstance(instance, thingml::PrintAction)

@given(instance=thingml::ReturnAction_strategy)
@settings(max_examples=50)
def test_thingml::returnaction_instantiation(instance):
    assert isinstance(instance, thingml::ReturnAction)

@given(instance=thingml::ExpressionGroup_strategy)
@settings(max_examples=50)
def test_thingml::expressiongroup_instantiation(instance):
    assert isinstance(instance, thingml::ExpressionGroup)

@given(instance=PropertyReference_strategy)
@settings(max_examples=50)
def test_propertyreference_instantiation(instance):
    assert isinstance(instance, PropertyReference)

@given(instance=thingml::DictionaryReference_strategy)
@settings(max_examples=50)
def test_thingml::dictionaryreference_instantiation(instance):
    assert isinstance(instance, thingml::DictionaryReference)

@given(instance=thingml::ArrayIndex_strategy)
@settings(max_examples=50)
def test_thingml::arrayindex_instantiation(instance):
    assert isinstance(instance, thingml::ArrayIndex)

@given(instance=thingml::PropertyReference_strategy)
@settings(max_examples=50)
def test_thingml::propertyreference_instantiation(instance):
    assert isinstance(instance, thingml::PropertyReference)

@given(instance=thingml::ConfigPropertyAssign_strategy)
@settings(max_examples=50)
def test_thingml::configpropertyassign_instantiation(instance):
    assert isinstance(instance, thingml::ConfigPropertyAssign)

@given(instance=thingml::ConfigInclude_strategy)
@settings(max_examples=50)
def test_thingml::configinclude_instantiation(instance):
    assert isinstance(instance, thingml::ConfigInclude)

@given(instance=thingml::Connector_strategy)
@settings(max_examples=50)
def test_thingml::connector_instantiation(instance):
    assert isinstance(instance, thingml::Connector)

@given(instance=thingml::Instance_strategy)
@settings(max_examples=50)
def test_thingml::instance_instantiation(instance):
    assert isinstance(instance, thingml::Instance)

@given(instance=thingml::ErrorAction_strategy)
@settings(max_examples=50)
def test_thingml::erroraction_instantiation(instance):
    assert isinstance(instance, thingml::ErrorAction)

@given(instance=thingml::BinaryExpression_strategy)
@settings(max_examples=50)
def test_thingml::binaryexpression_instantiation(instance):
    assert isinstance(instance, thingml::BinaryExpression)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=thingml::UnaryMinus_strategy)
@settings(max_examples=50)
def test_thingml::unaryminus_instantiation(instance):
    assert isinstance(instance, thingml::UnaryMinus)

@given(instance=thingml::NotExpression_strategy)
@settings(max_examples=50)
def test_thingml::notexpression_instantiation(instance):
    assert isinstance(instance, thingml::NotExpression)

@given(instance=thingml::UnaryExpression_strategy)
@settings(max_examples=50)
def test_thingml::unaryexpression_instantiation(instance):
    assert isinstance(instance, thingml::UnaryExpression)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=thingml::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_thingml::booleanliteral_instantiation(instance):
    assert isinstance(instance, thingml::BooleanLiteral)

@given(instance=thingml::BooleanLiteral_strategy)
def test_thingml::booleanliteral_boolValue_type(instance):
    assert isinstance(instance.boolValue, bool)


@given(instance=thingml::BooleanLiteral_strategy)
def test_thingml::booleanliteral_boolValue_setter(instance):
    original = instance.boolValue
    instance.boolValue = original
    assert instance.boolValue == original

@given(instance=thingml::DoubleLiteral_strategy)
@settings(max_examples=50)
def test_thingml::doubleliteral_instantiation(instance):
    assert isinstance(instance, thingml::DoubleLiteral)

@given(instance=thingml::DoubleLiteral_strategy)
def test_thingml::doubleliteral_doubleValue_type(instance):
    assert isinstance(instance.doubleValue, float)


@given(instance=thingml::DoubleLiteral_strategy)
def test_thingml::doubleliteral_doubleValue_setter(instance):
    original = instance.doubleValue
    instance.doubleValue = original
    assert instance.doubleValue == original

@given(instance=thingml::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_thingml::integerliteral_instantiation(instance):
    assert isinstance(instance, thingml::IntegerLiteral)

@given(instance=thingml::IntegerLiteral_strategy)
def test_thingml::integerliteral_intValue_type(instance):
    assert isinstance(instance.intValue, int)


@given(instance=thingml::IntegerLiteral_strategy)
def test_thingml::integerliteral_intValue_setter(instance):
    original = instance.intValue
    instance.intValue = original
    assert instance.intValue == original

@given(instance=thingml::StringLiteral_strategy)
@settings(max_examples=50)
def test_thingml::stringliteral_instantiation(instance):
    assert isinstance(instance, thingml::StringLiteral)

@given(instance=thingml::StringLiteral_strategy)
def test_thingml::stringliteral_stringValue_type(instance):
    assert isinstance(instance.stringValue, str)


@given(instance=thingml::StringLiteral_strategy)
def test_thingml::stringliteral_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=thingml::EnumLiteralRef_strategy)
@settings(max_examples=50)
def test_thingml::enumliteralref_instantiation(instance):
    assert isinstance(instance, thingml::EnumLiteralRef)

@given(instance=ControlStructure_strategy)
@settings(max_examples=50)
def test_controlstructure_instantiation(instance):
    assert isinstance(instance, ControlStructure)

@given(instance=thingml::ConditionalAction_strategy)
@settings(max_examples=50)
def test_thingml::conditionalaction_instantiation(instance):
    assert isinstance(instance, thingml::ConditionalAction)

@given(instance=thingml::LoopAction_strategy)
@settings(max_examples=50)
def test_thingml::loopaction_instantiation(instance):
    assert isinstance(instance, thingml::LoopAction)

@given(instance=thingml::ControlStructure_strategy)
@settings(max_examples=50)
def test_thingml::controlstructure_instantiation(instance):
    assert isinstance(instance, thingml::ControlStructure)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=thingml::MinusExpression_strategy)
@settings(max_examples=50)
def test_thingml::minusexpression_instantiation(instance):
    assert isinstance(instance, thingml::MinusExpression)

@given(instance=thingml::GreaterExpression_strategy)
@settings(max_examples=50)
def test_thingml::greaterexpression_instantiation(instance):
    assert isinstance(instance, thingml::GreaterExpression)

@given(instance=thingml::DivExpression_strategy)
@settings(max_examples=50)
def test_thingml::divexpression_instantiation(instance):
    assert isinstance(instance, thingml::DivExpression)

@given(instance=thingml::LowerExpression_strategy)
@settings(max_examples=50)
def test_thingml::lowerexpression_instantiation(instance):
    assert isinstance(instance, thingml::LowerExpression)

@given(instance=thingml::AndExpression_strategy)
@settings(max_examples=50)
def test_thingml::andexpression_instantiation(instance):
    assert isinstance(instance, thingml::AndExpression)

@given(instance=thingml::EqualsExpression_strategy)
@settings(max_examples=50)
def test_thingml::equalsexpression_instantiation(instance):
    assert isinstance(instance, thingml::EqualsExpression)

@given(instance=thingml::ModExpression_strategy)
@settings(max_examples=50)
def test_thingml::modexpression_instantiation(instance):
    assert isinstance(instance, thingml::ModExpression)

@given(instance=thingml::OrExpression_strategy)
@settings(max_examples=50)
def test_thingml::orexpression_instantiation(instance):
    assert isinstance(instance, thingml::OrExpression)

@given(instance=thingml::TimesExpression_strategy)
@settings(max_examples=50)
def test_thingml::timesexpression_instantiation(instance):
    assert isinstance(instance, thingml::TimesExpression)

@given(instance=thingml::PlusExpression_strategy)
@settings(max_examples=50)
def test_thingml::plusexpression_instantiation(instance):
    assert isinstance(instance, thingml::PlusExpression)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=thingml::Dictionary_strategy)
@settings(max_examples=50)
def test_thingml::dictionary_instantiation(instance):
    assert isinstance(instance, thingml::Dictionary)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=thingml::ReceiveMessage_strategy)
@settings(max_examples=50)
def test_thingml::receivemessage_instantiation(instance):
    assert isinstance(instance, thingml::ReceiveMessage)

@given(instance=thingml::VariableAssignment_strategy)
@settings(max_examples=50)
def test_thingml::variableassignment_instantiation(instance):
    assert isinstance(instance, thingml::VariableAssignment)

@given(instance=thingml::Literal_strategy)
@settings(max_examples=50)
def test_thingml::literal_instantiation(instance):
    assert isinstance(instance, thingml::Literal)

@given(instance=thingml::EventReference_strategy)
@settings(max_examples=50)
def test_thingml::eventreference_instantiation(instance):
    assert isinstance(instance, thingml::EventReference)
