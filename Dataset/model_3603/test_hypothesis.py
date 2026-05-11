import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractConnector,
    thingML::ExternalConnector,
    thingML::Connector,
    thingML::InstanceRef,
    thingML::ConfigPropertyAssign,
    Expression,
    thingML::UnaryMinus,
    thingML::MinusExpression,
    thingML::GreaterOrEqualExpression,
    thingML::FunctionCallExpression,
    thingML::BooleanLiteral,
    thingML::NotEqualsExpression,
    thingML::TimesExpression,
    thingML::AndExpression,
    thingML::DoubleLiteral,
    thingML::StringLiteral,
    thingML::DivExpression,
    thingML::PlusExpression,
    thingML::ArrayIndex,
    thingML::PropertyReference,
    thingML::EnumLiteralRef,
    thingML::LowerExpression,
    thingML::NotExpression,
    thingML::LowerOrEqualExpression,
    thingML::OrExpression,
    thingML::Reference,
    thingML::IntegerLiteral,
    thingML::GreaterExpression,
    thingML::ModExpression,
    thingML::EqualsExpression,
    thingML::ExternExpression,
    Handler,
    thingML::Event,
    thingML::Transition,
    thingML::InternalTransition,
    thingML::Action,
    Action,
    thingML::ConditionalAction,
    thingML::ExternStatement,
    thingML::VariableAssignment,
    thingML::PrintAction,
    thingML::ReturnAction,
    thingML::FunctionCallStatement,
    thingML::LoopAction,
    thingML::Decrement,
    thingML::Increment,
    thingML::StartSession,
    thingML::ErrorAction,
    thingML::Variable,
    Event,
    State,
    Region,
    thingML::Region,
    ElmtProperty,
    thingML::ArrayParamRef,
    thingML::LengthArray,
    thingML::SimpleParamRef,
    Source,
    thingML::ElmtProperty,
    thingML::ReferencedElmt,
    thingML::ViewSource,
    thingML::SendAction,
    thingML::Source,
    ViewSource,
    thingML::TimeWindow,
    thingML::LengthWindow,
    thingML::Filter,
    Variable,
    ReferencedElmt,
    thingML::MessageParameter,
    thingML::JoinSources,
    thingML::MergeSources,
    thingML::SimpleSource,
    thingML::ReceiveMessage,
    thingML::ActionBlock,
    Port,
    thingML::ProvidedPort,
    thingML::InternalPort,
    thingML::RequiredPort,
    thingML::EnumerationLiteral,
    thingML::TypeRef,
    thingML::AnnotatedElement,
    thingML::PlatformAnnotation,
    thingML::Import,
    Type,
    thingML::ObjectType,
    thingML::Thing,
    thingML::Enumeration,
    thingML::PrimitiveType,
    AnnotatedElement,
    thingML::CompositeState,
    thingML::Message,
    thingML::Function,
    thingML::Configuration,
    thingML::AbstractConnector,
    thingML::State,
    thingML::FinalState,
    thingML::Instance,
    thingML::Property,
    thingML::Protocol,
    thingML::Type,
    thingML::Port,
    thingML::ParallelRegion,
    thingML::PropertyAssign,
    thingML::Stream,
    thingML::Session,
    thingML::Handler,
    thingML::LocalVariable,
    thingML::Parameter,
    thingML::Expression,
    thingML::ThingMLModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractconnector_is_not_abstract():
    assert not inspect.isabstract(AbstractConnector)


def test_abstractconnector_constructor_exists():
    assert callable(AbstractConnector.__init__)


def test_abstractconnector_constructor_args():
    sig = inspect.signature(AbstractConnector.__init__)
    params = list(sig.parameters.keys())



def test_thingml::externalconnector_is_not_abstract():
    assert not inspect.isabstract(thingML::ExternalConnector)


def test_thingml::externalconnector_constructor_exists():
    assert callable(thingML::ExternalConnector.__init__)


def test_thingml::externalconnector_constructor_args():
    sig = inspect.signature(thingML::ExternalConnector.__init__)
    params = list(sig.parameters.keys())



def test_thingml::connector_is_not_abstract():
    assert not inspect.isabstract(thingML::Connector)


def test_thingml::connector_constructor_exists():
    assert callable(thingML::Connector.__init__)


def test_thingml::connector_constructor_args():
    sig = inspect.signature(thingML::Connector.__init__)
    params = list(sig.parameters.keys())



def test_thingml::instanceref_is_not_abstract():
    assert not inspect.isabstract(thingML::InstanceRef)


def test_thingml::instanceref_constructor_exists():
    assert callable(thingML::InstanceRef.__init__)


def test_thingml::instanceref_constructor_args():
    sig = inspect.signature(thingML::InstanceRef.__init__)
    params = list(sig.parameters.keys())



def test_thingml::configpropertyassign_is_not_abstract():
    assert not inspect.isabstract(thingML::ConfigPropertyAssign)


def test_thingml::configpropertyassign_constructor_exists():
    assert callable(thingML::ConfigPropertyAssign.__init__)


def test_thingml::configpropertyassign_constructor_args():
    sig = inspect.signature(thingML::ConfigPropertyAssign.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::unaryminus_is_not_abstract():
    assert not inspect.isabstract(thingML::UnaryMinus)


def test_thingml::unaryminus_constructor_exists():
    assert callable(thingML::UnaryMinus.__init__)


def test_thingml::unaryminus_constructor_args():
    sig = inspect.signature(thingML::UnaryMinus.__init__)
    params = list(sig.parameters.keys())



def test_thingml::minusexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::MinusExpression)


def test_thingml::minusexpression_constructor_exists():
    assert callable(thingML::MinusExpression.__init__)


def test_thingml::minusexpression_constructor_args():
    sig = inspect.signature(thingML::MinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::greaterorequalexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::GreaterOrEqualExpression)


def test_thingml::greaterorequalexpression_constructor_exists():
    assert callable(thingML::GreaterOrEqualExpression.__init__)


def test_thingml::greaterorequalexpression_constructor_args():
    sig = inspect.signature(thingML::GreaterOrEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::FunctionCallExpression)


def test_thingml::functioncallexpression_constructor_exists():
    assert callable(thingML::FunctionCallExpression.__init__)


def test_thingml::functioncallexpression_constructor_args():
    sig = inspect.signature(thingML::FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(thingML::BooleanLiteral)


def test_thingml::booleanliteral_constructor_exists():
    assert callable(thingML::BooleanLiteral.__init__)


def test_thingml::booleanliteral_constructor_args():
    sig = inspect.signature(thingML::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "boolValue" in params, "Missing parameter 'boolValue'"

def test_thingml::booleanliteral_has_boolValue():
    assert hasattr(thingML::BooleanLiteral, "boolValue")
    descriptor = None
    for klass in thingML::BooleanLiteral.__mro__:
        if "boolValue" in klass.__dict__:
            descriptor = klass.__dict__["boolValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml::notequalsexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::NotEqualsExpression)


def test_thingml::notequalsexpression_constructor_exists():
    assert callable(thingML::NotEqualsExpression.__init__)


def test_thingml::notequalsexpression_constructor_args():
    sig = inspect.signature(thingML::NotEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::timesexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::TimesExpression)


def test_thingml::timesexpression_constructor_exists():
    assert callable(thingML::TimesExpression.__init__)


def test_thingml::timesexpression_constructor_args():
    sig = inspect.signature(thingML::TimesExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::andexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::AndExpression)


def test_thingml::andexpression_constructor_exists():
    assert callable(thingML::AndExpression.__init__)


def test_thingml::andexpression_constructor_args():
    sig = inspect.signature(thingML::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::doubleliteral_is_not_abstract():
    assert not inspect.isabstract(thingML::DoubleLiteral)


def test_thingml::doubleliteral_constructor_exists():
    assert callable(thingML::DoubleLiteral.__init__)


def test_thingml::doubleliteral_constructor_args():
    sig = inspect.signature(thingML::DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "doubleValue" in params, "Missing parameter 'doubleValue'"

def test_thingml::doubleliteral_has_doubleValue():
    assert hasattr(thingML::DoubleLiteral, "doubleValue")
    descriptor = None
    for klass in thingML::DoubleLiteral.__mro__:
        if "doubleValue" in klass.__dict__:
            descriptor = klass.__dict__["doubleValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml::stringliteral_is_not_abstract():
    assert not inspect.isabstract(thingML::StringLiteral)


def test_thingml::stringliteral_constructor_exists():
    assert callable(thingML::StringLiteral.__init__)


def test_thingml::stringliteral_constructor_args():
    sig = inspect.signature(thingML::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "stringValue" in params, "Missing parameter 'stringValue'"

def test_thingml::stringliteral_has_stringValue():
    assert hasattr(thingML::StringLiteral, "stringValue")
    descriptor = None
    for klass in thingML::StringLiteral.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml::divexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::DivExpression)


def test_thingml::divexpression_constructor_exists():
    assert callable(thingML::DivExpression.__init__)


def test_thingml::divexpression_constructor_args():
    sig = inspect.signature(thingML::DivExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::plusexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::PlusExpression)


def test_thingml::plusexpression_constructor_exists():
    assert callable(thingML::PlusExpression.__init__)


def test_thingml::plusexpression_constructor_args():
    sig = inspect.signature(thingML::PlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::arrayindex_is_not_abstract():
    assert not inspect.isabstract(thingML::ArrayIndex)


def test_thingml::arrayindex_constructor_exists():
    assert callable(thingML::ArrayIndex.__init__)


def test_thingml::arrayindex_constructor_args():
    sig = inspect.signature(thingML::ArrayIndex.__init__)
    params = list(sig.parameters.keys())



def test_thingml::propertyreference_is_not_abstract():
    assert not inspect.isabstract(thingML::PropertyReference)


def test_thingml::propertyreference_constructor_exists():
    assert callable(thingML::PropertyReference.__init__)


def test_thingml::propertyreference_constructor_args():
    sig = inspect.signature(thingML::PropertyReference.__init__)
    params = list(sig.parameters.keys())



def test_thingml::enumliteralref_is_not_abstract():
    assert not inspect.isabstract(thingML::EnumLiteralRef)


def test_thingml::enumliteralref_constructor_exists():
    assert callable(thingML::EnumLiteralRef.__init__)


def test_thingml::enumliteralref_constructor_args():
    sig = inspect.signature(thingML::EnumLiteralRef.__init__)
    params = list(sig.parameters.keys())



def test_thingml::lowerexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::LowerExpression)


def test_thingml::lowerexpression_constructor_exists():
    assert callable(thingML::LowerExpression.__init__)


def test_thingml::lowerexpression_constructor_args():
    sig = inspect.signature(thingML::LowerExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::notexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::NotExpression)


def test_thingml::notexpression_constructor_exists():
    assert callable(thingML::NotExpression.__init__)


def test_thingml::notexpression_constructor_args():
    sig = inspect.signature(thingML::NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::lowerorequalexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::LowerOrEqualExpression)


def test_thingml::lowerorequalexpression_constructor_exists():
    assert callable(thingML::LowerOrEqualExpression.__init__)


def test_thingml::lowerorequalexpression_constructor_args():
    sig = inspect.signature(thingML::LowerOrEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::orexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::OrExpression)


def test_thingml::orexpression_constructor_exists():
    assert callable(thingML::OrExpression.__init__)


def test_thingml::orexpression_constructor_args():
    sig = inspect.signature(thingML::OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::reference_is_not_abstract():
    assert not inspect.isabstract(thingML::Reference)


def test_thingml::reference_constructor_exists():
    assert callable(thingML::Reference.__init__)


def test_thingml::reference_constructor_args():
    sig = inspect.signature(thingML::Reference.__init__)
    params = list(sig.parameters.keys())



def test_thingml::integerliteral_is_not_abstract():
    assert not inspect.isabstract(thingML::IntegerLiteral)


def test_thingml::integerliteral_constructor_exists():
    assert callable(thingML::IntegerLiteral.__init__)


def test_thingml::integerliteral_constructor_args():
    sig = inspect.signature(thingML::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "intValue" in params, "Missing parameter 'intValue'"

def test_thingml::integerliteral_has_intValue():
    assert hasattr(thingML::IntegerLiteral, "intValue")
    descriptor = None
    for klass in thingML::IntegerLiteral.__mro__:
        if "intValue" in klass.__dict__:
            descriptor = klass.__dict__["intValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml::greaterexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::GreaterExpression)


def test_thingml::greaterexpression_constructor_exists():
    assert callable(thingML::GreaterExpression.__init__)


def test_thingml::greaterexpression_constructor_args():
    sig = inspect.signature(thingML::GreaterExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::modexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::ModExpression)


def test_thingml::modexpression_constructor_exists():
    assert callable(thingML::ModExpression.__init__)


def test_thingml::modexpression_constructor_args():
    sig = inspect.signature(thingML::ModExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::equalsexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::EqualsExpression)


def test_thingml::equalsexpression_constructor_exists():
    assert callable(thingML::EqualsExpression.__init__)


def test_thingml::equalsexpression_constructor_args():
    sig = inspect.signature(thingML::EqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::externexpression_is_not_abstract():
    assert not inspect.isabstract(thingML::ExternExpression)


def test_thingml::externexpression_constructor_exists():
    assert callable(thingML::ExternExpression.__init__)


def test_thingml::externexpression_constructor_args():
    sig = inspect.signature(thingML::ExternExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_thingml::externexpression_has_expression():
    assert hasattr(thingML::ExternExpression, "expression")
    descriptor = None
    for klass in thingML::ExternExpression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_handler_is_not_abstract():
    assert not inspect.isabstract(Handler)


def test_handler_constructor_exists():
    assert callable(Handler.__init__)


def test_handler_constructor_args():
    sig = inspect.signature(Handler.__init__)
    params = list(sig.parameters.keys())



def test_thingml::event_is_not_abstract():
    assert not inspect.isabstract(thingML::Event)


def test_thingml::event_constructor_exists():
    assert callable(thingML::Event.__init__)


def test_thingml::event_constructor_args():
    sig = inspect.signature(thingML::Event.__init__)
    params = list(sig.parameters.keys())



def test_thingml::transition_is_not_abstract():
    assert not inspect.isabstract(thingML::Transition)


def test_thingml::transition_constructor_exists():
    assert callable(thingML::Transition.__init__)


def test_thingml::transition_constructor_args():
    sig = inspect.signature(thingML::Transition.__init__)
    params = list(sig.parameters.keys())



def test_thingml::internaltransition_is_not_abstract():
    assert not inspect.isabstract(thingML::InternalTransition)


def test_thingml::internaltransition_constructor_exists():
    assert callable(thingML::InternalTransition.__init__)


def test_thingml::internaltransition_constructor_args():
    sig = inspect.signature(thingML::InternalTransition.__init__)
    params = list(sig.parameters.keys())



def test_thingml::action_is_not_abstract():
    assert not inspect.isabstract(thingML::Action)


def test_thingml::action_constructor_exists():
    assert callable(thingML::Action.__init__)


def test_thingml::action_constructor_args():
    sig = inspect.signature(thingML::Action.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_thingml::conditionalaction_is_not_abstract():
    assert not inspect.isabstract(thingML::ConditionalAction)


def test_thingml::conditionalaction_constructor_exists():
    assert callable(thingML::ConditionalAction.__init__)


def test_thingml::conditionalaction_constructor_args():
    sig = inspect.signature(thingML::ConditionalAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml::externstatement_is_not_abstract():
    assert not inspect.isabstract(thingML::ExternStatement)


def test_thingml::externstatement_constructor_exists():
    assert callable(thingML::ExternStatement.__init__)


def test_thingml::externstatement_constructor_args():
    sig = inspect.signature(thingML::ExternStatement.__init__)
    params = list(sig.parameters.keys())
    assert "statement" in params, "Missing parameter 'statement'"

def test_thingml::externstatement_has_statement():
    assert hasattr(thingML::ExternStatement, "statement")
    descriptor = None
    for klass in thingML::ExternStatement.__mro__:
        if "statement" in klass.__dict__:
            descriptor = klass.__dict__["statement"]
            break
    assert isinstance(descriptor, property)



def test_thingml::variableassignment_is_not_abstract():
    assert not inspect.isabstract(thingML::VariableAssignment)


def test_thingml::variableassignment_constructor_exists():
    assert callable(thingML::VariableAssignment.__init__)


def test_thingml::variableassignment_constructor_args():
    sig = inspect.signature(thingML::VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_thingml::printaction_is_not_abstract():
    assert not inspect.isabstract(thingML::PrintAction)


def test_thingml::printaction_constructor_exists():
    assert callable(thingML::PrintAction.__init__)


def test_thingml::printaction_constructor_args():
    sig = inspect.signature(thingML::PrintAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml::returnaction_is_not_abstract():
    assert not inspect.isabstract(thingML::ReturnAction)


def test_thingml::returnaction_constructor_exists():
    assert callable(thingML::ReturnAction.__init__)


def test_thingml::returnaction_constructor_args():
    sig = inspect.signature(thingML::ReturnAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml::functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(thingML::FunctionCallStatement)


def test_thingml::functioncallstatement_constructor_exists():
    assert callable(thingML::FunctionCallStatement.__init__)


def test_thingml::functioncallstatement_constructor_args():
    sig = inspect.signature(thingML::FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_thingml::loopaction_is_not_abstract():
    assert not inspect.isabstract(thingML::LoopAction)


def test_thingml::loopaction_constructor_exists():
    assert callable(thingML::LoopAction.__init__)


def test_thingml::loopaction_constructor_args():
    sig = inspect.signature(thingML::LoopAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml::decrement_is_not_abstract():
    assert not inspect.isabstract(thingML::Decrement)


def test_thingml::decrement_constructor_exists():
    assert callable(thingML::Decrement.__init__)


def test_thingml::decrement_constructor_args():
    sig = inspect.signature(thingML::Decrement.__init__)
    params = list(sig.parameters.keys())



def test_thingml::increment_is_not_abstract():
    assert not inspect.isabstract(thingML::Increment)


def test_thingml::increment_constructor_exists():
    assert callable(thingML::Increment.__init__)


def test_thingml::increment_constructor_args():
    sig = inspect.signature(thingML::Increment.__init__)
    params = list(sig.parameters.keys())



def test_thingml::startsession_is_not_abstract():
    assert not inspect.isabstract(thingML::StartSession)


def test_thingml::startsession_constructor_exists():
    assert callable(thingML::StartSession.__init__)


def test_thingml::startsession_constructor_args():
    sig = inspect.signature(thingML::StartSession.__init__)
    params = list(sig.parameters.keys())



def test_thingml::erroraction_is_not_abstract():
    assert not inspect.isabstract(thingML::ErrorAction)


def test_thingml::erroraction_constructor_exists():
    assert callable(thingML::ErrorAction.__init__)


def test_thingml::erroraction_constructor_args():
    sig = inspect.signature(thingML::ErrorAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml::variable_is_not_abstract():
    assert not inspect.isabstract(thingML::Variable)


def test_thingml::variable_constructor_exists():
    assert callable(thingML::Variable.__init__)


def test_thingml::variable_constructor_args():
    sig = inspect.signature(thingML::Variable.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_region_is_not_abstract():
    assert not inspect.isabstract(Region)


def test_region_constructor_exists():
    assert callable(Region.__init__)


def test_region_constructor_args():
    sig = inspect.signature(Region.__init__)
    params = list(sig.parameters.keys())



def test_thingml::region_is_not_abstract():
    assert not inspect.isabstract(thingML::Region)


def test_thingml::region_constructor_exists():
    assert callable(thingML::Region.__init__)


def test_thingml::region_constructor_args():
    sig = inspect.signature(thingML::Region.__init__)
    params = list(sig.parameters.keys())



def test_elmtproperty_is_not_abstract():
    assert not inspect.isabstract(ElmtProperty)


def test_elmtproperty_constructor_exists():
    assert callable(ElmtProperty.__init__)


def test_elmtproperty_constructor_args():
    sig = inspect.signature(ElmtProperty.__init__)
    params = list(sig.parameters.keys())



def test_thingml::arrayparamref_is_not_abstract():
    assert not inspect.isabstract(thingML::ArrayParamRef)


def test_thingml::arrayparamref_constructor_exists():
    assert callable(thingML::ArrayParamRef.__init__)


def test_thingml::arrayparamref_constructor_args():
    sig = inspect.signature(thingML::ArrayParamRef.__init__)
    params = list(sig.parameters.keys())



def test_thingml::lengtharray_is_not_abstract():
    assert not inspect.isabstract(thingML::LengthArray)


def test_thingml::lengtharray_constructor_exists():
    assert callable(thingML::LengthArray.__init__)


def test_thingml::lengtharray_constructor_args():
    sig = inspect.signature(thingML::LengthArray.__init__)
    params = list(sig.parameters.keys())



def test_thingml::simpleparamref_is_not_abstract():
    assert not inspect.isabstract(thingML::SimpleParamRef)


def test_thingml::simpleparamref_constructor_exists():
    assert callable(thingML::SimpleParamRef.__init__)


def test_thingml::simpleparamref_constructor_args():
    sig = inspect.signature(thingML::SimpleParamRef.__init__)
    params = list(sig.parameters.keys())



def test_source_is_not_abstract():
    assert not inspect.isabstract(Source)


def test_source_constructor_exists():
    assert callable(Source.__init__)


def test_source_constructor_args():
    sig = inspect.signature(Source.__init__)
    params = list(sig.parameters.keys())



def test_thingml::elmtproperty_is_not_abstract():
    assert not inspect.isabstract(thingML::ElmtProperty)


def test_thingml::elmtproperty_constructor_exists():
    assert callable(thingML::ElmtProperty.__init__)


def test_thingml::elmtproperty_constructor_args():
    sig = inspect.signature(thingML::ElmtProperty.__init__)
    params = list(sig.parameters.keys())



def test_thingml::referencedelmt_is_not_abstract():
    assert not inspect.isabstract(thingML::ReferencedElmt)


def test_thingml::referencedelmt_constructor_exists():
    assert callable(thingML::ReferencedElmt.__init__)


def test_thingml::referencedelmt_constructor_args():
    sig = inspect.signature(thingML::ReferencedElmt.__init__)
    params = list(sig.parameters.keys())



def test_thingml::viewsource_is_not_abstract():
    assert not inspect.isabstract(thingML::ViewSource)


def test_thingml::viewsource_constructor_exists():
    assert callable(thingML::ViewSource.__init__)


def test_thingml::viewsource_constructor_args():
    sig = inspect.signature(thingML::ViewSource.__init__)
    params = list(sig.parameters.keys())



def test_thingml::sendaction_is_not_abstract():
    assert not inspect.isabstract(thingML::SendAction)


def test_thingml::sendaction_constructor_exists():
    assert callable(thingML::SendAction.__init__)


def test_thingml::sendaction_constructor_args():
    sig = inspect.signature(thingML::SendAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml::source_is_not_abstract():
    assert not inspect.isabstract(thingML::Source)


def test_thingml::source_constructor_exists():
    assert callable(thingML::Source.__init__)


def test_thingml::source_constructor_args():
    sig = inspect.signature(thingML::Source.__init__)
    params = list(sig.parameters.keys())



def test_viewsource_is_not_abstract():
    assert not inspect.isabstract(ViewSource)


def test_viewsource_constructor_exists():
    assert callable(ViewSource.__init__)


def test_viewsource_constructor_args():
    sig = inspect.signature(ViewSource.__init__)
    params = list(sig.parameters.keys())



def test_thingml::timewindow_is_not_abstract():
    assert not inspect.isabstract(thingML::TimeWindow)


def test_thingml::timewindow_constructor_exists():
    assert callable(thingML::TimeWindow.__init__)


def test_thingml::timewindow_constructor_args():
    sig = inspect.signature(thingML::TimeWindow.__init__)
    params = list(sig.parameters.keys())



def test_thingml::lengthwindow_is_not_abstract():
    assert not inspect.isabstract(thingML::LengthWindow)


def test_thingml::lengthwindow_constructor_exists():
    assert callable(thingML::LengthWindow.__init__)


def test_thingml::lengthwindow_constructor_args():
    sig = inspect.signature(thingML::LengthWindow.__init__)
    params = list(sig.parameters.keys())



def test_thingml::filter_is_not_abstract():
    assert not inspect.isabstract(thingML::Filter)


def test_thingml::filter_constructor_exists():
    assert callable(thingML::Filter.__init__)


def test_thingml::filter_constructor_args():
    sig = inspect.signature(thingML::Filter.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_referencedelmt_is_not_abstract():
    assert not inspect.isabstract(ReferencedElmt)


def test_referencedelmt_constructor_exists():
    assert callable(ReferencedElmt.__init__)


def test_referencedelmt_constructor_args():
    sig = inspect.signature(ReferencedElmt.__init__)
    params = list(sig.parameters.keys())



def test_thingml::messageparameter_is_not_abstract():
    assert not inspect.isabstract(thingML::MessageParameter)


def test_thingml::messageparameter_constructor_exists():
    assert callable(thingML::MessageParameter.__init__)


def test_thingml::messageparameter_constructor_args():
    sig = inspect.signature(thingML::MessageParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::messageparameter_has_name():
    assert hasattr(thingML::MessageParameter, "name")
    descriptor = None
    for klass in thingML::MessageParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::joinsources_is_not_abstract():
    assert not inspect.isabstract(thingML::JoinSources)


def test_thingml::joinsources_constructor_exists():
    assert callable(thingML::JoinSources.__init__)


def test_thingml::joinsources_constructor_args():
    sig = inspect.signature(thingML::JoinSources.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::joinsources_has_name():
    assert hasattr(thingML::JoinSources, "name")
    descriptor = None
    for klass in thingML::JoinSources.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::mergesources_is_not_abstract():
    assert not inspect.isabstract(thingML::MergeSources)


def test_thingml::mergesources_constructor_exists():
    assert callable(thingML::MergeSources.__init__)


def test_thingml::mergesources_constructor_args():
    sig = inspect.signature(thingML::MergeSources.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::mergesources_has_name():
    assert hasattr(thingML::MergeSources, "name")
    descriptor = None
    for klass in thingML::MergeSources.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::simplesource_is_not_abstract():
    assert not inspect.isabstract(thingML::SimpleSource)


def test_thingml::simplesource_constructor_exists():
    assert callable(thingML::SimpleSource.__init__)


def test_thingml::simplesource_constructor_args():
    sig = inspect.signature(thingML::SimpleSource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::simplesource_has_name():
    assert hasattr(thingML::SimpleSource, "name")
    descriptor = None
    for klass in thingML::SimpleSource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::receivemessage_is_not_abstract():
    assert not inspect.isabstract(thingML::ReceiveMessage)


def test_thingml::receivemessage_constructor_exists():
    assert callable(thingML::ReceiveMessage.__init__)


def test_thingml::receivemessage_constructor_args():
    sig = inspect.signature(thingML::ReceiveMessage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::receivemessage_has_name():
    assert hasattr(thingML::ReceiveMessage, "name")
    descriptor = None
    for klass in thingML::ReceiveMessage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::actionblock_is_not_abstract():
    assert not inspect.isabstract(thingML::ActionBlock)


def test_thingml::actionblock_constructor_exists():
    assert callable(thingML::ActionBlock.__init__)


def test_thingml::actionblock_constructor_args():
    sig = inspect.signature(thingML::ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_thingml::providedport_is_not_abstract():
    assert not inspect.isabstract(thingML::ProvidedPort)


def test_thingml::providedport_constructor_exists():
    assert callable(thingML::ProvidedPort.__init__)


def test_thingml::providedport_constructor_args():
    sig = inspect.signature(thingML::ProvidedPort.__init__)
    params = list(sig.parameters.keys())



def test_thingml::internalport_is_not_abstract():
    assert not inspect.isabstract(thingML::InternalPort)


def test_thingml::internalport_constructor_exists():
    assert callable(thingML::InternalPort.__init__)


def test_thingml::internalport_constructor_args():
    sig = inspect.signature(thingML::InternalPort.__init__)
    params = list(sig.parameters.keys())



def test_thingml::requiredport_is_not_abstract():
    assert not inspect.isabstract(thingML::RequiredPort)


def test_thingml::requiredport_constructor_exists():
    assert callable(thingML::RequiredPort.__init__)


def test_thingml::requiredport_constructor_args():
    sig = inspect.signature(thingML::RequiredPort.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"

def test_thingml::requiredport_has_optional():
    assert hasattr(thingML::RequiredPort, "optional")
    descriptor = None
    for klass in thingML::RequiredPort.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_thingml::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(thingML::EnumerationLiteral)


def test_thingml::enumerationliteral_constructor_exists():
    assert callable(thingML::EnumerationLiteral.__init__)


def test_thingml::enumerationliteral_constructor_args():
    sig = inspect.signature(thingML::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::enumerationliteral_has_name():
    assert hasattr(thingML::EnumerationLiteral, "name")
    descriptor = None
    for klass in thingML::EnumerationLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::typeref_is_not_abstract():
    assert not inspect.isabstract(thingML::TypeRef)


def test_thingml::typeref_constructor_exists():
    assert callable(thingML::TypeRef.__init__)


def test_thingml::typeref_constructor_args():
    sig = inspect.signature(thingML::TypeRef.__init__)
    params = list(sig.parameters.keys())
    assert "isArray" in params, "Missing parameter 'isArray'"

def test_thingml::typeref_has_isArray():
    assert hasattr(thingML::TypeRef, "isArray")
    descriptor = None
    for klass in thingML::TypeRef.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)



def test_thingml::annotatedelement_is_not_abstract():
    assert not inspect.isabstract(thingML::AnnotatedElement)


def test_thingml::annotatedelement_constructor_exists():
    assert callable(thingML::AnnotatedElement.__init__)


def test_thingml::annotatedelement_constructor_args():
    sig = inspect.signature(thingML::AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_thingml::platformannotation_is_not_abstract():
    assert not inspect.isabstract(thingML::PlatformAnnotation)


def test_thingml::platformannotation_constructor_exists():
    assert callable(thingML::PlatformAnnotation.__init__)


def test_thingml::platformannotation_constructor_args():
    sig = inspect.signature(thingML::PlatformAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::platformannotation_has_value():
    assert hasattr(thingML::PlatformAnnotation, "value")
    descriptor = None
    for klass in thingML::PlatformAnnotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_thingml::platformannotation_has_name():
    assert hasattr(thingML::PlatformAnnotation, "name")
    descriptor = None
    for klass in thingML::PlatformAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::import_is_not_abstract():
    assert not inspect.isabstract(thingML::Import)


def test_thingml::import_constructor_exists():
    assert callable(thingML::Import.__init__)


def test_thingml::import_constructor_args():
    sig = inspect.signature(thingML::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_thingml::import_has_importURI():
    assert hasattr(thingML::Import, "importURI")
    descriptor = None
    for klass in thingML::Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_thingml::objecttype_is_not_abstract():
    assert not inspect.isabstract(thingML::ObjectType)


def test_thingml::objecttype_constructor_exists():
    assert callable(thingML::ObjectType.__init__)


def test_thingml::objecttype_constructor_args():
    sig = inspect.signature(thingML::ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_thingml::thing_is_not_abstract():
    assert not inspect.isabstract(thingML::Thing)


def test_thingml::thing_constructor_exists():
    assert callable(thingML::Thing.__init__)


def test_thingml::thing_constructor_args():
    sig = inspect.signature(thingML::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "fragment" in params, "Missing parameter 'fragment'"

def test_thingml::thing_has_fragment():
    assert hasattr(thingML::Thing, "fragment")
    descriptor = None
    for klass in thingML::Thing.__mro__:
        if "fragment" in klass.__dict__:
            descriptor = klass.__dict__["fragment"]
            break
    assert isinstance(descriptor, property)



def test_thingml::enumeration_is_not_abstract():
    assert not inspect.isabstract(thingML::Enumeration)


def test_thingml::enumeration_constructor_exists():
    assert callable(thingML::Enumeration.__init__)


def test_thingml::enumeration_constructor_args():
    sig = inspect.signature(thingML::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_thingml::primitivetype_is_not_abstract():
    assert not inspect.isabstract(thingML::PrimitiveType)


def test_thingml::primitivetype_constructor_exists():
    assert callable(thingML::PrimitiveType.__init__)


def test_thingml::primitivetype_constructor_args():
    sig = inspect.signature(thingML::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "ByteSize" in params, "Missing parameter 'ByteSize'"

def test_thingml::primitivetype_has_ByteSize():
    assert hasattr(thingML::PrimitiveType, "ByteSize")
    descriptor = None
    for klass in thingML::PrimitiveType.__mro__:
        if "ByteSize" in klass.__dict__:
            descriptor = klass.__dict__["ByteSize"]
            break
    assert isinstance(descriptor, property)



def test_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatedElement)


def test_annotatedelement_constructor_exists():
    assert callable(AnnotatedElement.__init__)


def test_annotatedelement_constructor_args():
    sig = inspect.signature(AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_thingml::compositestate_is_not_abstract():
    assert not inspect.isabstract(thingML::CompositeState)


def test_thingml::compositestate_constructor_exists():
    assert callable(thingML::CompositeState.__init__)


def test_thingml::compositestate_constructor_args():
    sig = inspect.signature(thingML::CompositeState.__init__)
    params = list(sig.parameters.keys())
    assert "history" in params, "Missing parameter 'history'"

def test_thingml::compositestate_has_history():
    assert hasattr(thingML::CompositeState, "history")
    descriptor = None
    for klass in thingML::CompositeState.__mro__:
        if "history" in klass.__dict__:
            descriptor = klass.__dict__["history"]
            break
    assert isinstance(descriptor, property)



def test_thingml::message_is_not_abstract():
    assert not inspect.isabstract(thingML::Message)


def test_thingml::message_constructor_exists():
    assert callable(thingML::Message.__init__)


def test_thingml::message_constructor_args():
    sig = inspect.signature(thingML::Message.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::message_has_name():
    assert hasattr(thingML::Message, "name")
    descriptor = None
    for klass in thingML::Message.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::function_is_not_abstract():
    assert not inspect.isabstract(thingML::Function)


def test_thingml::function_constructor_exists():
    assert callable(thingML::Function.__init__)


def test_thingml::function_constructor_args():
    sig = inspect.signature(thingML::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::function_has_name():
    assert hasattr(thingML::Function, "name")
    descriptor = None
    for klass in thingML::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::configuration_is_not_abstract():
    assert not inspect.isabstract(thingML::Configuration)


def test_thingml::configuration_constructor_exists():
    assert callable(thingML::Configuration.__init__)


def test_thingml::configuration_constructor_args():
    sig = inspect.signature(thingML::Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::configuration_has_name():
    assert hasattr(thingML::Configuration, "name")
    descriptor = None
    for klass in thingML::Configuration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::abstractconnector_is_not_abstract():
    assert not inspect.isabstract(thingML::AbstractConnector)


def test_thingml::abstractconnector_constructor_exists():
    assert callable(thingML::AbstractConnector.__init__)


def test_thingml::abstractconnector_constructor_args():
    sig = inspect.signature(thingML::AbstractConnector.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::abstractconnector_has_name():
    assert hasattr(thingML::AbstractConnector, "name")
    descriptor = None
    for klass in thingML::AbstractConnector.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::state_is_not_abstract():
    assert not inspect.isabstract(thingML::State)


def test_thingml::state_constructor_exists():
    assert callable(thingML::State.__init__)


def test_thingml::state_constructor_args():
    sig = inspect.signature(thingML::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::state_has_name():
    assert hasattr(thingML::State, "name")
    descriptor = None
    for klass in thingML::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::finalstate_is_not_abstract():
    assert not inspect.isabstract(thingML::FinalState)


def test_thingml::finalstate_constructor_exists():
    assert callable(thingML::FinalState.__init__)


def test_thingml::finalstate_constructor_args():
    sig = inspect.signature(thingML::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_thingml::instance_is_not_abstract():
    assert not inspect.isabstract(thingML::Instance)


def test_thingml::instance_constructor_exists():
    assert callable(thingML::Instance.__init__)


def test_thingml::instance_constructor_args():
    sig = inspect.signature(thingML::Instance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::instance_has_name():
    assert hasattr(thingML::Instance, "name")
    descriptor = None
    for klass in thingML::Instance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::property_is_not_abstract():
    assert not inspect.isabstract(thingML::Property)


def test_thingml::property_constructor_exists():
    assert callable(thingML::Property.__init__)


def test_thingml::property_constructor_args():
    sig = inspect.signature(thingML::Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "changeable" in params, "Missing parameter 'changeable'"

def test_thingml::property_has_name():
    assert hasattr(thingML::Property, "name")
    descriptor = None
    for klass in thingML::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_thingml::property_has_changeable():
    assert hasattr(thingML::Property, "changeable")
    descriptor = None
    for klass in thingML::Property.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)



def test_thingml::protocol_is_not_abstract():
    assert not inspect.isabstract(thingML::Protocol)


def test_thingml::protocol_constructor_exists():
    assert callable(thingML::Protocol.__init__)


def test_thingml::protocol_constructor_args():
    sig = inspect.signature(thingML::Protocol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::protocol_has_name():
    assert hasattr(thingML::Protocol, "name")
    descriptor = None
    for klass in thingML::Protocol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::type_is_not_abstract():
    assert not inspect.isabstract(thingML::Type)


def test_thingml::type_constructor_exists():
    assert callable(thingML::Type.__init__)


def test_thingml::type_constructor_args():
    sig = inspect.signature(thingML::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::type_has_name():
    assert hasattr(thingML::Type, "name")
    descriptor = None
    for klass in thingML::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::port_is_not_abstract():
    assert not inspect.isabstract(thingML::Port)


def test_thingml::port_constructor_exists():
    assert callable(thingML::Port.__init__)


def test_thingml::port_constructor_args():
    sig = inspect.signature(thingML::Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::port_has_name():
    assert hasattr(thingML::Port, "name")
    descriptor = None
    for klass in thingML::Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::parallelregion_is_not_abstract():
    assert not inspect.isabstract(thingML::ParallelRegion)


def test_thingml::parallelregion_constructor_exists():
    assert callable(thingML::ParallelRegion.__init__)


def test_thingml::parallelregion_constructor_args():
    sig = inspect.signature(thingML::ParallelRegion.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "history" in params, "Missing parameter 'history'"

def test_thingml::parallelregion_has_name():
    assert hasattr(thingML::ParallelRegion, "name")
    descriptor = None
    for klass in thingML::ParallelRegion.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_thingml::parallelregion_has_history():
    assert hasattr(thingML::ParallelRegion, "history")
    descriptor = None
    for klass in thingML::ParallelRegion.__mro__:
        if "history" in klass.__dict__:
            descriptor = klass.__dict__["history"]
            break
    assert isinstance(descriptor, property)



def test_thingml::propertyassign_is_not_abstract():
    assert not inspect.isabstract(thingML::PropertyAssign)


def test_thingml::propertyassign_constructor_exists():
    assert callable(thingML::PropertyAssign.__init__)


def test_thingml::propertyassign_constructor_args():
    sig = inspect.signature(thingML::PropertyAssign.__init__)
    params = list(sig.parameters.keys())



def test_thingml::stream_is_not_abstract():
    assert not inspect.isabstract(thingML::Stream)


def test_thingml::stream_constructor_exists():
    assert callable(thingML::Stream.__init__)


def test_thingml::stream_constructor_args():
    sig = inspect.signature(thingML::Stream.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::stream_has_name():
    assert hasattr(thingML::Stream, "name")
    descriptor = None
    for klass in thingML::Stream.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::session_is_not_abstract():
    assert not inspect.isabstract(thingML::Session)


def test_thingml::session_constructor_exists():
    assert callable(thingML::Session.__init__)


def test_thingml::session_constructor_args():
    sig = inspect.signature(thingML::Session.__init__)
    params = list(sig.parameters.keys())
    assert "maxInstances" in params, "Missing parameter 'maxInstances'"

def test_thingml::session_has_maxInstances():
    assert hasattr(thingML::Session, "maxInstances")
    descriptor = None
    for klass in thingML::Session.__mro__:
        if "maxInstances" in klass.__dict__:
            descriptor = klass.__dict__["maxInstances"]
            break
    assert isinstance(descriptor, property)



def test_thingml::handler_is_not_abstract():
    assert not inspect.isabstract(thingML::Handler)


def test_thingml::handler_constructor_exists():
    assert callable(thingML::Handler.__init__)


def test_thingml::handler_constructor_args():
    sig = inspect.signature(thingML::Handler.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::handler_has_name():
    assert hasattr(thingML::Handler, "name")
    descriptor = None
    for klass in thingML::Handler.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::localvariable_is_not_abstract():
    assert not inspect.isabstract(thingML::LocalVariable)


def test_thingml::localvariable_constructor_exists():
    assert callable(thingML::LocalVariable.__init__)


def test_thingml::localvariable_constructor_args():
    sig = inspect.signature(thingML::LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "changeable" in params, "Missing parameter 'changeable'"

def test_thingml::localvariable_has_name():
    assert hasattr(thingML::LocalVariable, "name")
    descriptor = None
    for klass in thingML::LocalVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_thingml::localvariable_has_changeable():
    assert hasattr(thingML::LocalVariable, "changeable")
    descriptor = None
    for klass in thingML::LocalVariable.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)



def test_thingml::parameter_is_not_abstract():
    assert not inspect.isabstract(thingML::Parameter)


def test_thingml::parameter_constructor_exists():
    assert callable(thingML::Parameter.__init__)


def test_thingml::parameter_constructor_args():
    sig = inspect.signature(thingML::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml::parameter_has_name():
    assert hasattr(thingML::Parameter, "name")
    descriptor = None
    for klass in thingML::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml::expression_is_not_abstract():
    assert not inspect.isabstract(thingML::Expression)


def test_thingml::expression_constructor_exists():
    assert callable(thingML::Expression.__init__)


def test_thingml::expression_constructor_args():
    sig = inspect.signature(thingML::Expression.__init__)
    params = list(sig.parameters.keys())



def test_thingml::thingmlmodel_is_not_abstract():
    assert not inspect.isabstract(thingML::ThingMLModel)


def test_thingml::thingmlmodel_constructor_exists():
    assert callable(thingML::ThingMLModel.__init__)


def test_thingml::thingmlmodel_constructor_args():
    sig = inspect.signature(thingML::ThingMLModel.__init__)
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
AbstractConnector_strategy = st.builds(
    AbstractConnector,
)
thingML::ExternalConnector_strategy = st.builds(
    thingML::ExternalConnector,
)
thingML::Connector_strategy = st.builds(
    thingML::Connector,
)
thingML::InstanceRef_strategy = st.builds(
    thingML::InstanceRef,
)
thingML::ConfigPropertyAssign_strategy = st.builds(
    thingML::ConfigPropertyAssign,
)
Expression_strategy = st.builds(
    Expression,
)
thingML::UnaryMinus_strategy = st.builds(
    thingML::UnaryMinus,
)
thingML::MinusExpression_strategy = st.builds(
    thingML::MinusExpression,
)
thingML::GreaterOrEqualExpression_strategy = st.builds(
    thingML::GreaterOrEqualExpression,
)
thingML::FunctionCallExpression_strategy = st.builds(
    thingML::FunctionCallExpression,
)
thingML::BooleanLiteral_strategy = st.builds(
    thingML::BooleanLiteral,
    boolValue=
        safe_text
)
thingML::NotEqualsExpression_strategy = st.builds(
    thingML::NotEqualsExpression,
)
thingML::TimesExpression_strategy = st.builds(
    thingML::TimesExpression,
)
thingML::AndExpression_strategy = st.builds(
    thingML::AndExpression,
)
thingML::DoubleLiteral_strategy = st.builds(
    thingML::DoubleLiteral,
    doubleValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
thingML::StringLiteral_strategy = st.builds(
    thingML::StringLiteral,
    stringValue=
        safe_text
)
thingML::DivExpression_strategy = st.builds(
    thingML::DivExpression,
)
thingML::PlusExpression_strategy = st.builds(
    thingML::PlusExpression,
)
thingML::ArrayIndex_strategy = st.builds(
    thingML::ArrayIndex,
)
thingML::PropertyReference_strategy = st.builds(
    thingML::PropertyReference,
)
thingML::EnumLiteralRef_strategy = st.builds(
    thingML::EnumLiteralRef,
)
thingML::LowerExpression_strategy = st.builds(
    thingML::LowerExpression,
)
thingML::NotExpression_strategy = st.builds(
    thingML::NotExpression,
)
thingML::LowerOrEqualExpression_strategy = st.builds(
    thingML::LowerOrEqualExpression,
)
thingML::OrExpression_strategy = st.builds(
    thingML::OrExpression,
)
thingML::Reference_strategy = st.builds(
    thingML::Reference,
)
thingML::IntegerLiteral_strategy = st.builds(
    thingML::IntegerLiteral,
    intValue=
        st.integers()
)
thingML::GreaterExpression_strategy = st.builds(
    thingML::GreaterExpression,
)
thingML::ModExpression_strategy = st.builds(
    thingML::ModExpression,
)
thingML::EqualsExpression_strategy = st.builds(
    thingML::EqualsExpression,
)
thingML::ExternExpression_strategy = st.builds(
    thingML::ExternExpression,
    expression=
        safe_text
)
Handler_strategy = st.builds(
    Handler,
)
thingML::Event_strategy = st.builds(
    thingML::Event,
)
thingML::Transition_strategy = st.builds(
    thingML::Transition,
)
thingML::InternalTransition_strategy = st.builds(
    thingML::InternalTransition,
)
thingML::Action_strategy = st.builds(
    thingML::Action,
)
Action_strategy = st.builds(
    Action,
)
thingML::ConditionalAction_strategy = st.builds(
    thingML::ConditionalAction,
)
thingML::ExternStatement_strategy = st.builds(
    thingML::ExternStatement,
    statement=
        safe_text
)
thingML::VariableAssignment_strategy = st.builds(
    thingML::VariableAssignment,
)
thingML::PrintAction_strategy = st.builds(
    thingML::PrintAction,
)
thingML::ReturnAction_strategy = st.builds(
    thingML::ReturnAction,
)
thingML::FunctionCallStatement_strategy = st.builds(
    thingML::FunctionCallStatement,
)
thingML::LoopAction_strategy = st.builds(
    thingML::LoopAction,
)
thingML::Decrement_strategy = st.builds(
    thingML::Decrement,
)
thingML::Increment_strategy = st.builds(
    thingML::Increment,
)
thingML::StartSession_strategy = st.builds(
    thingML::StartSession,
)
thingML::ErrorAction_strategy = st.builds(
    thingML::ErrorAction,
)
thingML::Variable_strategy = st.builds(
    thingML::Variable,
)
Event_strategy = st.builds(
    Event,
)
State_strategy = st.builds(
    State,
)
Region_strategy = st.builds(
    Region,
)
thingML::Region_strategy = st.builds(
    thingML::Region,
)
ElmtProperty_strategy = st.builds(
    ElmtProperty,
)
thingML::ArrayParamRef_strategy = st.builds(
    thingML::ArrayParamRef,
)
thingML::LengthArray_strategy = st.builds(
    thingML::LengthArray,
)
thingML::SimpleParamRef_strategy = st.builds(
    thingML::SimpleParamRef,
)
Source_strategy = st.builds(
    Source,
)
thingML::ElmtProperty_strategy = st.builds(
    thingML::ElmtProperty,
)
thingML::ReferencedElmt_strategy = st.builds(
    thingML::ReferencedElmt,
)
thingML::ViewSource_strategy = st.builds(
    thingML::ViewSource,
)
thingML::SendAction_strategy = st.builds(
    thingML::SendAction,
)
thingML::Source_strategy = st.builds(
    thingML::Source,
)
ViewSource_strategy = st.builds(
    ViewSource,
)
thingML::TimeWindow_strategy = st.builds(
    thingML::TimeWindow,
)
thingML::LengthWindow_strategy = st.builds(
    thingML::LengthWindow,
)
thingML::Filter_strategy = st.builds(
    thingML::Filter,
)
Variable_strategy = st.builds(
    Variable,
)
ReferencedElmt_strategy = st.builds(
    ReferencedElmt,
)
thingML::MessageParameter_strategy = st.builds(
    thingML::MessageParameter,
    name=
        safe_text
)
thingML::JoinSources_strategy = st.builds(
    thingML::JoinSources,
    name=
        safe_text
)
thingML::MergeSources_strategy = st.builds(
    thingML::MergeSources,
    name=
        safe_text
)
thingML::SimpleSource_strategy = st.builds(
    thingML::SimpleSource,
    name=
        safe_text
)
thingML::ReceiveMessage_strategy = st.builds(
    thingML::ReceiveMessage,
    name=
        safe_text
)
thingML::ActionBlock_strategy = st.builds(
    thingML::ActionBlock,
)
Port_strategy = st.builds(
    Port,
)
thingML::ProvidedPort_strategy = st.builds(
    thingML::ProvidedPort,
)
thingML::InternalPort_strategy = st.builds(
    thingML::InternalPort,
)
thingML::RequiredPort_strategy = st.builds(
    thingML::RequiredPort,
    optional=
        st.booleans()
)
thingML::EnumerationLiteral_strategy = st.builds(
    thingML::EnumerationLiteral,
    name=
        safe_text
)
thingML::TypeRef_strategy = st.builds(
    thingML::TypeRef,
    isArray=
        st.booleans()
)
thingML::AnnotatedElement_strategy = st.builds(
    thingML::AnnotatedElement,
)
thingML::PlatformAnnotation_strategy = st.builds(
    thingML::PlatformAnnotation,
    value=
        safe_text,
    name=
        safe_text
)
thingML::Import_strategy = st.builds(
    thingML::Import,
    importURI=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
thingML::ObjectType_strategy = st.builds(
    thingML::ObjectType,
)
thingML::Thing_strategy = st.builds(
    thingML::Thing,
    fragment=
        st.booleans()
)
thingML::Enumeration_strategy = st.builds(
    thingML::Enumeration,
)
thingML::PrimitiveType_strategy = st.builds(
    thingML::PrimitiveType,
    ByteSize=
        st.integers()
)
AnnotatedElement_strategy = st.builds(
    AnnotatedElement,
)
thingML::CompositeState_strategy = st.builds(
    thingML::CompositeState,
    history=
        st.booleans()
)
thingML::Message_strategy = st.builds(
    thingML::Message,
    name=
        safe_text
)
thingML::Function_strategy = st.builds(
    thingML::Function,
    name=
        safe_text
)
thingML::Configuration_strategy = st.builds(
    thingML::Configuration,
    name=
        safe_text
)
thingML::AbstractConnector_strategy = st.builds(
    thingML::AbstractConnector,
    name=
        safe_text
)
thingML::State_strategy = st.builds(
    thingML::State,
    name=
        safe_text
)
thingML::FinalState_strategy = st.builds(
    thingML::FinalState,
)
thingML::Instance_strategy = st.builds(
    thingML::Instance,
    name=
        safe_text
)
thingML::Property_strategy = st.builds(
    thingML::Property,
    name=
        safe_text,
    changeable=
        st.booleans()
)
thingML::Protocol_strategy = st.builds(
    thingML::Protocol,
    name=
        safe_text
)
thingML::Type_strategy = st.builds(
    thingML::Type,
    name=
        safe_text
)
thingML::Port_strategy = st.builds(
    thingML::Port,
    name=
        safe_text
)
thingML::ParallelRegion_strategy = st.builds(
    thingML::ParallelRegion,
    name=
        safe_text,
    history=
        st.booleans()
)
thingML::PropertyAssign_strategy = st.builds(
    thingML::PropertyAssign,
)
thingML::Stream_strategy = st.builds(
    thingML::Stream,
    name=
        safe_text
)
thingML::Session_strategy = st.builds(
    thingML::Session,
    maxInstances=
        st.integers()
)
thingML::Handler_strategy = st.builds(
    thingML::Handler,
    name=
        safe_text
)
thingML::LocalVariable_strategy = st.builds(
    thingML::LocalVariable,
    name=
        safe_text,
    changeable=
        st.booleans()
)
thingML::Parameter_strategy = st.builds(
    thingML::Parameter,
    name=
        safe_text
)
thingML::Expression_strategy = st.builds(
    thingML::Expression,
)
thingML::ThingMLModel_strategy = st.builds(
    thingML::ThingMLModel,
)

@given(instance=AbstractConnector_strategy)
@settings(max_examples=50)
def test_abstractconnector_instantiation(instance):
    assert isinstance(instance, AbstractConnector)

@given(instance=thingML::ExternalConnector_strategy)
@settings(max_examples=50)
def test_thingml::externalconnector_instantiation(instance):
    assert isinstance(instance, thingML::ExternalConnector)

@given(instance=thingML::Connector_strategy)
@settings(max_examples=50)
def test_thingml::connector_instantiation(instance):
    assert isinstance(instance, thingML::Connector)

@given(instance=thingML::InstanceRef_strategy)
@settings(max_examples=50)
def test_thingml::instanceref_instantiation(instance):
    assert isinstance(instance, thingML::InstanceRef)

@given(instance=thingML::ConfigPropertyAssign_strategy)
@settings(max_examples=50)
def test_thingml::configpropertyassign_instantiation(instance):
    assert isinstance(instance, thingML::ConfigPropertyAssign)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=thingML::UnaryMinus_strategy)
@settings(max_examples=50)
def test_thingml::unaryminus_instantiation(instance):
    assert isinstance(instance, thingML::UnaryMinus)

@given(instance=thingML::MinusExpression_strategy)
@settings(max_examples=50)
def test_thingml::minusexpression_instantiation(instance):
    assert isinstance(instance, thingML::MinusExpression)

@given(instance=thingML::GreaterOrEqualExpression_strategy)
@settings(max_examples=50)
def test_thingml::greaterorequalexpression_instantiation(instance):
    assert isinstance(instance, thingML::GreaterOrEqualExpression)

@given(instance=thingML::FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_thingml::functioncallexpression_instantiation(instance):
    assert isinstance(instance, thingML::FunctionCallExpression)

@given(instance=thingML::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_thingml::booleanliteral_instantiation(instance):
    assert isinstance(instance, thingML::BooleanLiteral)

@given(instance=thingML::BooleanLiteral_strategy)
def test_thingml::booleanliteral_boolValue_type(instance):
    assert isinstance(instance.boolValue, str)


@given(instance=thingML::BooleanLiteral_strategy)
def test_thingml::booleanliteral_boolValue_setter(instance):
    original = instance.boolValue
    instance.boolValue = original
    assert instance.boolValue == original

@given(instance=thingML::NotEqualsExpression_strategy)
@settings(max_examples=50)
def test_thingml::notequalsexpression_instantiation(instance):
    assert isinstance(instance, thingML::NotEqualsExpression)

@given(instance=thingML::TimesExpression_strategy)
@settings(max_examples=50)
def test_thingml::timesexpression_instantiation(instance):
    assert isinstance(instance, thingML::TimesExpression)

@given(instance=thingML::AndExpression_strategy)
@settings(max_examples=50)
def test_thingml::andexpression_instantiation(instance):
    assert isinstance(instance, thingML::AndExpression)

@given(instance=thingML::DoubleLiteral_strategy)
@settings(max_examples=50)
def test_thingml::doubleliteral_instantiation(instance):
    assert isinstance(instance, thingML::DoubleLiteral)

@given(instance=thingML::DoubleLiteral_strategy)
def test_thingml::doubleliteral_doubleValue_type(instance):
    assert isinstance(instance.doubleValue, float)


@given(instance=thingML::DoubleLiteral_strategy)
def test_thingml::doubleliteral_doubleValue_setter(instance):
    original = instance.doubleValue
    instance.doubleValue = original
    assert instance.doubleValue == original

@given(instance=thingML::StringLiteral_strategy)
@settings(max_examples=50)
def test_thingml::stringliteral_instantiation(instance):
    assert isinstance(instance, thingML::StringLiteral)

@given(instance=thingML::StringLiteral_strategy)
def test_thingml::stringliteral_stringValue_type(instance):
    assert isinstance(instance.stringValue, str)


@given(instance=thingML::StringLiteral_strategy)
def test_thingml::stringliteral_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=thingML::DivExpression_strategy)
@settings(max_examples=50)
def test_thingml::divexpression_instantiation(instance):
    assert isinstance(instance, thingML::DivExpression)

@given(instance=thingML::PlusExpression_strategy)
@settings(max_examples=50)
def test_thingml::plusexpression_instantiation(instance):
    assert isinstance(instance, thingML::PlusExpression)

@given(instance=thingML::ArrayIndex_strategy)
@settings(max_examples=50)
def test_thingml::arrayindex_instantiation(instance):
    assert isinstance(instance, thingML::ArrayIndex)

@given(instance=thingML::PropertyReference_strategy)
@settings(max_examples=50)
def test_thingml::propertyreference_instantiation(instance):
    assert isinstance(instance, thingML::PropertyReference)

@given(instance=thingML::EnumLiteralRef_strategy)
@settings(max_examples=50)
def test_thingml::enumliteralref_instantiation(instance):
    assert isinstance(instance, thingML::EnumLiteralRef)

@given(instance=thingML::LowerExpression_strategy)
@settings(max_examples=50)
def test_thingml::lowerexpression_instantiation(instance):
    assert isinstance(instance, thingML::LowerExpression)

@given(instance=thingML::NotExpression_strategy)
@settings(max_examples=50)
def test_thingml::notexpression_instantiation(instance):
    assert isinstance(instance, thingML::NotExpression)

@given(instance=thingML::LowerOrEqualExpression_strategy)
@settings(max_examples=50)
def test_thingml::lowerorequalexpression_instantiation(instance):
    assert isinstance(instance, thingML::LowerOrEqualExpression)

@given(instance=thingML::OrExpression_strategy)
@settings(max_examples=50)
def test_thingml::orexpression_instantiation(instance):
    assert isinstance(instance, thingML::OrExpression)

@given(instance=thingML::Reference_strategy)
@settings(max_examples=50)
def test_thingml::reference_instantiation(instance):
    assert isinstance(instance, thingML::Reference)

@given(instance=thingML::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_thingml::integerliteral_instantiation(instance):
    assert isinstance(instance, thingML::IntegerLiteral)

@given(instance=thingML::IntegerLiteral_strategy)
def test_thingml::integerliteral_intValue_type(instance):
    assert isinstance(instance.intValue, int)


@given(instance=thingML::IntegerLiteral_strategy)
def test_thingml::integerliteral_intValue_setter(instance):
    original = instance.intValue
    instance.intValue = original
    assert instance.intValue == original

@given(instance=thingML::GreaterExpression_strategy)
@settings(max_examples=50)
def test_thingml::greaterexpression_instantiation(instance):
    assert isinstance(instance, thingML::GreaterExpression)

@given(instance=thingML::ModExpression_strategy)
@settings(max_examples=50)
def test_thingml::modexpression_instantiation(instance):
    assert isinstance(instance, thingML::ModExpression)

@given(instance=thingML::EqualsExpression_strategy)
@settings(max_examples=50)
def test_thingml::equalsexpression_instantiation(instance):
    assert isinstance(instance, thingML::EqualsExpression)

@given(instance=thingML::ExternExpression_strategy)
@settings(max_examples=50)
def test_thingml::externexpression_instantiation(instance):
    assert isinstance(instance, thingML::ExternExpression)

@given(instance=thingML::ExternExpression_strategy)
def test_thingml::externexpression_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=thingML::ExternExpression_strategy)
def test_thingml::externexpression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=Handler_strategy)
@settings(max_examples=50)
def test_handler_instantiation(instance):
    assert isinstance(instance, Handler)

@given(instance=thingML::Event_strategy)
@settings(max_examples=50)
def test_thingml::event_instantiation(instance):
    assert isinstance(instance, thingML::Event)

@given(instance=thingML::Transition_strategy)
@settings(max_examples=50)
def test_thingml::transition_instantiation(instance):
    assert isinstance(instance, thingML::Transition)

@given(instance=thingML::InternalTransition_strategy)
@settings(max_examples=50)
def test_thingml::internaltransition_instantiation(instance):
    assert isinstance(instance, thingML::InternalTransition)

@given(instance=thingML::Action_strategy)
@settings(max_examples=50)
def test_thingml::action_instantiation(instance):
    assert isinstance(instance, thingML::Action)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=thingML::ConditionalAction_strategy)
@settings(max_examples=50)
def test_thingml::conditionalaction_instantiation(instance):
    assert isinstance(instance, thingML::ConditionalAction)

@given(instance=thingML::ExternStatement_strategy)
@settings(max_examples=50)
def test_thingml::externstatement_instantiation(instance):
    assert isinstance(instance, thingML::ExternStatement)

@given(instance=thingML::ExternStatement_strategy)
def test_thingml::externstatement_statement_type(instance):
    assert isinstance(instance.statement, str)


@given(instance=thingML::ExternStatement_strategy)
def test_thingml::externstatement_statement_setter(instance):
    original = instance.statement
    instance.statement = original
    assert instance.statement == original

@given(instance=thingML::VariableAssignment_strategy)
@settings(max_examples=50)
def test_thingml::variableassignment_instantiation(instance):
    assert isinstance(instance, thingML::VariableAssignment)

@given(instance=thingML::PrintAction_strategy)
@settings(max_examples=50)
def test_thingml::printaction_instantiation(instance):
    assert isinstance(instance, thingML::PrintAction)

@given(instance=thingML::ReturnAction_strategy)
@settings(max_examples=50)
def test_thingml::returnaction_instantiation(instance):
    assert isinstance(instance, thingML::ReturnAction)

@given(instance=thingML::FunctionCallStatement_strategy)
@settings(max_examples=50)
def test_thingml::functioncallstatement_instantiation(instance):
    assert isinstance(instance, thingML::FunctionCallStatement)

@given(instance=thingML::LoopAction_strategy)
@settings(max_examples=50)
def test_thingml::loopaction_instantiation(instance):
    assert isinstance(instance, thingML::LoopAction)

@given(instance=thingML::Decrement_strategy)
@settings(max_examples=50)
def test_thingml::decrement_instantiation(instance):
    assert isinstance(instance, thingML::Decrement)

@given(instance=thingML::Increment_strategy)
@settings(max_examples=50)
def test_thingml::increment_instantiation(instance):
    assert isinstance(instance, thingML::Increment)

@given(instance=thingML::StartSession_strategy)
@settings(max_examples=50)
def test_thingml::startsession_instantiation(instance):
    assert isinstance(instance, thingML::StartSession)

@given(instance=thingML::ErrorAction_strategy)
@settings(max_examples=50)
def test_thingml::erroraction_instantiation(instance):
    assert isinstance(instance, thingML::ErrorAction)

@given(instance=thingML::Variable_strategy)
@settings(max_examples=50)
def test_thingml::variable_instantiation(instance):
    assert isinstance(instance, thingML::Variable)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=Region_strategy)
@settings(max_examples=50)
def test_region_instantiation(instance):
    assert isinstance(instance, Region)

@given(instance=thingML::Region_strategy)
@settings(max_examples=50)
def test_thingml::region_instantiation(instance):
    assert isinstance(instance, thingML::Region)

@given(instance=ElmtProperty_strategy)
@settings(max_examples=50)
def test_elmtproperty_instantiation(instance):
    assert isinstance(instance, ElmtProperty)

@given(instance=thingML::ArrayParamRef_strategy)
@settings(max_examples=50)
def test_thingml::arrayparamref_instantiation(instance):
    assert isinstance(instance, thingML::ArrayParamRef)

@given(instance=thingML::LengthArray_strategy)
@settings(max_examples=50)
def test_thingml::lengtharray_instantiation(instance):
    assert isinstance(instance, thingML::LengthArray)

@given(instance=thingML::SimpleParamRef_strategy)
@settings(max_examples=50)
def test_thingml::simpleparamref_instantiation(instance):
    assert isinstance(instance, thingML::SimpleParamRef)

@given(instance=Source_strategy)
@settings(max_examples=50)
def test_source_instantiation(instance):
    assert isinstance(instance, Source)

@given(instance=thingML::ElmtProperty_strategy)
@settings(max_examples=50)
def test_thingml::elmtproperty_instantiation(instance):
    assert isinstance(instance, thingML::ElmtProperty)

@given(instance=thingML::ReferencedElmt_strategy)
@settings(max_examples=50)
def test_thingml::referencedelmt_instantiation(instance):
    assert isinstance(instance, thingML::ReferencedElmt)

@given(instance=thingML::ViewSource_strategy)
@settings(max_examples=50)
def test_thingml::viewsource_instantiation(instance):
    assert isinstance(instance, thingML::ViewSource)

@given(instance=thingML::SendAction_strategy)
@settings(max_examples=50)
def test_thingml::sendaction_instantiation(instance):
    assert isinstance(instance, thingML::SendAction)

@given(instance=thingML::Source_strategy)
@settings(max_examples=50)
def test_thingml::source_instantiation(instance):
    assert isinstance(instance, thingML::Source)

@given(instance=ViewSource_strategy)
@settings(max_examples=50)
def test_viewsource_instantiation(instance):
    assert isinstance(instance, ViewSource)

@given(instance=thingML::TimeWindow_strategy)
@settings(max_examples=50)
def test_thingml::timewindow_instantiation(instance):
    assert isinstance(instance, thingML::TimeWindow)

@given(instance=thingML::LengthWindow_strategy)
@settings(max_examples=50)
def test_thingml::lengthwindow_instantiation(instance):
    assert isinstance(instance, thingML::LengthWindow)

@given(instance=thingML::Filter_strategy)
@settings(max_examples=50)
def test_thingml::filter_instantiation(instance):
    assert isinstance(instance, thingML::Filter)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=ReferencedElmt_strategy)
@settings(max_examples=50)
def test_referencedelmt_instantiation(instance):
    assert isinstance(instance, ReferencedElmt)

@given(instance=thingML::MessageParameter_strategy)
@settings(max_examples=50)
def test_thingml::messageparameter_instantiation(instance):
    assert isinstance(instance, thingML::MessageParameter)

@given(instance=thingML::MessageParameter_strategy)
def test_thingml::messageparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::MessageParameter_strategy)
def test_thingml::messageparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::JoinSources_strategy)
@settings(max_examples=50)
def test_thingml::joinsources_instantiation(instance):
    assert isinstance(instance, thingML::JoinSources)

@given(instance=thingML::JoinSources_strategy)
def test_thingml::joinsources_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::JoinSources_strategy)
def test_thingml::joinsources_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::MergeSources_strategy)
@settings(max_examples=50)
def test_thingml::mergesources_instantiation(instance):
    assert isinstance(instance, thingML::MergeSources)

@given(instance=thingML::MergeSources_strategy)
def test_thingml::mergesources_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::MergeSources_strategy)
def test_thingml::mergesources_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::SimpleSource_strategy)
@settings(max_examples=50)
def test_thingml::simplesource_instantiation(instance):
    assert isinstance(instance, thingML::SimpleSource)

@given(instance=thingML::SimpleSource_strategy)
def test_thingml::simplesource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::SimpleSource_strategy)
def test_thingml::simplesource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::ReceiveMessage_strategy)
@settings(max_examples=50)
def test_thingml::receivemessage_instantiation(instance):
    assert isinstance(instance, thingML::ReceiveMessage)

@given(instance=thingML::ReceiveMessage_strategy)
def test_thingml::receivemessage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::ReceiveMessage_strategy)
def test_thingml::receivemessage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::ActionBlock_strategy)
@settings(max_examples=50)
def test_thingml::actionblock_instantiation(instance):
    assert isinstance(instance, thingML::ActionBlock)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=thingML::ProvidedPort_strategy)
@settings(max_examples=50)
def test_thingml::providedport_instantiation(instance):
    assert isinstance(instance, thingML::ProvidedPort)

@given(instance=thingML::InternalPort_strategy)
@settings(max_examples=50)
def test_thingml::internalport_instantiation(instance):
    assert isinstance(instance, thingML::InternalPort)

@given(instance=thingML::RequiredPort_strategy)
@settings(max_examples=50)
def test_thingml::requiredport_instantiation(instance):
    assert isinstance(instance, thingML::RequiredPort)

@given(instance=thingML::RequiredPort_strategy)
def test_thingml::requiredport_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=thingML::RequiredPort_strategy)
def test_thingml::requiredport_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=thingML::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_thingml::enumerationliteral_instantiation(instance):
    assert isinstance(instance, thingML::EnumerationLiteral)

@given(instance=thingML::EnumerationLiteral_strategy)
def test_thingml::enumerationliteral_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::EnumerationLiteral_strategy)
def test_thingml::enumerationliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::TypeRef_strategy)
@settings(max_examples=50)
def test_thingml::typeref_instantiation(instance):
    assert isinstance(instance, thingML::TypeRef)

@given(instance=thingML::TypeRef_strategy)
def test_thingml::typeref_isArray_type(instance):
    assert isinstance(instance.isArray, bool)


@given(instance=thingML::TypeRef_strategy)
def test_thingml::typeref_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original

@given(instance=thingML::AnnotatedElement_strategy)
@settings(max_examples=50)
def test_thingml::annotatedelement_instantiation(instance):
    assert isinstance(instance, thingML::AnnotatedElement)

@given(instance=thingML::PlatformAnnotation_strategy)
@settings(max_examples=50)
def test_thingml::platformannotation_instantiation(instance):
    assert isinstance(instance, thingML::PlatformAnnotation)

@given(instance=thingML::PlatformAnnotation_strategy)
def test_thingml::platformannotation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=thingML::PlatformAnnotation_strategy)
def test_thingml::platformannotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=thingML::PlatformAnnotation_strategy)
def test_thingml::platformannotation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::PlatformAnnotation_strategy)
def test_thingml::platformannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::Import_strategy)
@settings(max_examples=50)
def test_thingml::import_instantiation(instance):
    assert isinstance(instance, thingML::Import)

@given(instance=thingML::Import_strategy)
def test_thingml::import_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=thingML::Import_strategy)
def test_thingml::import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=thingML::ObjectType_strategy)
@settings(max_examples=50)
def test_thingml::objecttype_instantiation(instance):
    assert isinstance(instance, thingML::ObjectType)

@given(instance=thingML::Thing_strategy)
@settings(max_examples=50)
def test_thingml::thing_instantiation(instance):
    assert isinstance(instance, thingML::Thing)

@given(instance=thingML::Thing_strategy)
def test_thingml::thing_fragment_type(instance):
    assert isinstance(instance.fragment, bool)


@given(instance=thingML::Thing_strategy)
def test_thingml::thing_fragment_setter(instance):
    original = instance.fragment
    instance.fragment = original
    assert instance.fragment == original

@given(instance=thingML::Enumeration_strategy)
@settings(max_examples=50)
def test_thingml::enumeration_instantiation(instance):
    assert isinstance(instance, thingML::Enumeration)

@given(instance=thingML::PrimitiveType_strategy)
@settings(max_examples=50)
def test_thingml::primitivetype_instantiation(instance):
    assert isinstance(instance, thingML::PrimitiveType)

@given(instance=thingML::PrimitiveType_strategy)
def test_thingml::primitivetype_ByteSize_type(instance):
    assert isinstance(instance.ByteSize, int)


@given(instance=thingML::PrimitiveType_strategy)
def test_thingml::primitivetype_ByteSize_setter(instance):
    original = instance.ByteSize
    instance.ByteSize = original
    assert instance.ByteSize == original

@given(instance=AnnotatedElement_strategy)
@settings(max_examples=50)
def test_annotatedelement_instantiation(instance):
    assert isinstance(instance, AnnotatedElement)

@given(instance=thingML::CompositeState_strategy)
@settings(max_examples=50)
def test_thingml::compositestate_instantiation(instance):
    assert isinstance(instance, thingML::CompositeState)

@given(instance=thingML::CompositeState_strategy)
def test_thingml::compositestate_history_type(instance):
    assert isinstance(instance.history, bool)


@given(instance=thingML::CompositeState_strategy)
def test_thingml::compositestate_history_setter(instance):
    original = instance.history
    instance.history = original
    assert instance.history == original

@given(instance=thingML::Message_strategy)
@settings(max_examples=50)
def test_thingml::message_instantiation(instance):
    assert isinstance(instance, thingML::Message)

@given(instance=thingML::Message_strategy)
def test_thingml::message_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::Message_strategy)
def test_thingml::message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::Function_strategy)
@settings(max_examples=50)
def test_thingml::function_instantiation(instance):
    assert isinstance(instance, thingML::Function)

@given(instance=thingML::Function_strategy)
def test_thingml::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::Function_strategy)
def test_thingml::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::Configuration_strategy)
@settings(max_examples=50)
def test_thingml::configuration_instantiation(instance):
    assert isinstance(instance, thingML::Configuration)

@given(instance=thingML::Configuration_strategy)
def test_thingml::configuration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::Configuration_strategy)
def test_thingml::configuration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::AbstractConnector_strategy)
@settings(max_examples=50)
def test_thingml::abstractconnector_instantiation(instance):
    assert isinstance(instance, thingML::AbstractConnector)

@given(instance=thingML::AbstractConnector_strategy)
def test_thingml::abstractconnector_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::AbstractConnector_strategy)
def test_thingml::abstractconnector_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::State_strategy)
@settings(max_examples=50)
def test_thingml::state_instantiation(instance):
    assert isinstance(instance, thingML::State)

@given(instance=thingML::State_strategy)
def test_thingml::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::State_strategy)
def test_thingml::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::FinalState_strategy)
@settings(max_examples=50)
def test_thingml::finalstate_instantiation(instance):
    assert isinstance(instance, thingML::FinalState)

@given(instance=thingML::Instance_strategy)
@settings(max_examples=50)
def test_thingml::instance_instantiation(instance):
    assert isinstance(instance, thingML::Instance)

@given(instance=thingML::Instance_strategy)
def test_thingml::instance_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::Instance_strategy)
def test_thingml::instance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::Property_strategy)
@settings(max_examples=50)
def test_thingml::property_instantiation(instance):
    assert isinstance(instance, thingML::Property)

@given(instance=thingML::Property_strategy)
def test_thingml::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::Property_strategy)
def test_thingml::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::Property_strategy)
def test_thingml::property_changeable_type(instance):
    assert isinstance(instance.changeable, bool)


@given(instance=thingML::Property_strategy)
def test_thingml::property_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original

@given(instance=thingML::Protocol_strategy)
@settings(max_examples=50)
def test_thingml::protocol_instantiation(instance):
    assert isinstance(instance, thingML::Protocol)

@given(instance=thingML::Protocol_strategy)
def test_thingml::protocol_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::Protocol_strategy)
def test_thingml::protocol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::Type_strategy)
@settings(max_examples=50)
def test_thingml::type_instantiation(instance):
    assert isinstance(instance, thingML::Type)

@given(instance=thingML::Type_strategy)
def test_thingml::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::Type_strategy)
def test_thingml::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::Port_strategy)
@settings(max_examples=50)
def test_thingml::port_instantiation(instance):
    assert isinstance(instance, thingML::Port)

@given(instance=thingML::Port_strategy)
def test_thingml::port_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::Port_strategy)
def test_thingml::port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::ParallelRegion_strategy)
@settings(max_examples=50)
def test_thingml::parallelregion_instantiation(instance):
    assert isinstance(instance, thingML::ParallelRegion)

@given(instance=thingML::ParallelRegion_strategy)
def test_thingml::parallelregion_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::ParallelRegion_strategy)
def test_thingml::parallelregion_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::ParallelRegion_strategy)
def test_thingml::parallelregion_history_type(instance):
    assert isinstance(instance.history, bool)


@given(instance=thingML::ParallelRegion_strategy)
def test_thingml::parallelregion_history_setter(instance):
    original = instance.history
    instance.history = original
    assert instance.history == original

@given(instance=thingML::PropertyAssign_strategy)
@settings(max_examples=50)
def test_thingml::propertyassign_instantiation(instance):
    assert isinstance(instance, thingML::PropertyAssign)

@given(instance=thingML::Stream_strategy)
@settings(max_examples=50)
def test_thingml::stream_instantiation(instance):
    assert isinstance(instance, thingML::Stream)

@given(instance=thingML::Stream_strategy)
def test_thingml::stream_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::Stream_strategy)
def test_thingml::stream_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::Session_strategy)
@settings(max_examples=50)
def test_thingml::session_instantiation(instance):
    assert isinstance(instance, thingML::Session)

@given(instance=thingML::Session_strategy)
def test_thingml::session_maxInstances_type(instance):
    assert isinstance(instance.maxInstances, int)


@given(instance=thingML::Session_strategy)
def test_thingml::session_maxInstances_setter(instance):
    original = instance.maxInstances
    instance.maxInstances = original
    assert instance.maxInstances == original

@given(instance=thingML::Handler_strategy)
@settings(max_examples=50)
def test_thingml::handler_instantiation(instance):
    assert isinstance(instance, thingML::Handler)

@given(instance=thingML::Handler_strategy)
def test_thingml::handler_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::Handler_strategy)
def test_thingml::handler_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::LocalVariable_strategy)
@settings(max_examples=50)
def test_thingml::localvariable_instantiation(instance):
    assert isinstance(instance, thingML::LocalVariable)

@given(instance=thingML::LocalVariable_strategy)
def test_thingml::localvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::LocalVariable_strategy)
def test_thingml::localvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::LocalVariable_strategy)
def test_thingml::localvariable_changeable_type(instance):
    assert isinstance(instance.changeable, bool)


@given(instance=thingML::LocalVariable_strategy)
def test_thingml::localvariable_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original

@given(instance=thingML::Parameter_strategy)
@settings(max_examples=50)
def test_thingml::parameter_instantiation(instance):
    assert isinstance(instance, thingML::Parameter)

@given(instance=thingML::Parameter_strategy)
def test_thingml::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=thingML::Parameter_strategy)
def test_thingml::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML::Expression_strategy)
@settings(max_examples=50)
def test_thingml::expression_instantiation(instance):
    assert isinstance(instance, thingML::Expression)

@given(instance=thingML::ThingMLModel_strategy)
@settings(max_examples=50)
def test_thingml::thingmlmodel_instantiation(instance):
    assert isinstance(instance, thingML::ThingMLModel)
