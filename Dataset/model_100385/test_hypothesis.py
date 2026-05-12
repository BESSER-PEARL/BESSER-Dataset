import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ResourceImport,
    scxmlxt::DomainDataImport,
    scxmlxt::DomainModelImport,
    IntLiteral,
    scxmlxt::DelayLiteral,
    scxmlxt::EObject,
    scxmlxt::EObjectReference,
    ResourceUriLiteral,
    scxmlxt::EObjectUriLiteral,
    AbstractUriLiteral,
    scxmlxt::ResourceUriLiteral,
    scxmlxt::UriLiteral,
    Expression,
    scxmlxt::VarRef,
    Literal,
    scxmlxt::AbstractUriLiteral,
    scxmlxt::FloatLiteral,
    scxmlxt::StringLiteral,
    scxmlxt::IntLiteral,
    scxmlxt::BooleanLiteral,
    scxmlxt::Literal,
    scxmlxt::ScriptExpression,
    scxmlxt::EStepFilter,
    scxmlxt::EStep,
    scxmlxt::EPath,
    Typed,
    scxmlxt::EClassifier,
    scxmlxt::Typed,
    Action,
    scxmlxt::AssignmentAction,
    scxmlxt::ScriptAction,
    scxmlxt::SymbolicAction,
    scxmlxt::Expression,
    AbstractTransitionEvent,
    scxmlxt::EnterEvent,
    scxmlxt::ExitEvent,
    scxmlxt::TransitionEvent,
    Event,
    scxmlxt::TimerEvent,
    scxmlxt::AbstractTransitionEvent,
    scxmlxt::ScriptEvent,
    scxmlxt::SymbolicEvent,
    AbstractTransition,
    scxmlxt::InternalTransition,
    scxmlxt::Transition,
    scxmlxt::Condition,
    scxmlxt::Event,
    scxmlxt::VarDef,
    scxmlxt::AbstractTransition,
    scxmlxt::AbstractState,
    scxmlxt::Action,
    scxmlxt::InitialTransition,
    scxmlxt::ResourceImport,
    AbstractState,
    scxmlxt::State,
    scxmlxt::StateMachine,
    TimeUnit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_resourceimport_is_not_abstract():
    assert not inspect.isabstract(ResourceImport)


def test_resourceimport_constructor_exists():
    assert callable(ResourceImport.__init__)


def test_resourceimport_constructor_args():
    sig = inspect.signature(ResourceImport.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::domaindataimport_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::DomainDataImport)


def test_scxmlxt::domaindataimport_constructor_exists():
    assert callable(scxmlxt::DomainDataImport.__init__)


def test_scxmlxt::domaindataimport_constructor_args():
    sig = inspect.signature(scxmlxt::DomainDataImport.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::domainmodelimport_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::DomainModelImport)


def test_scxmlxt::domainmodelimport_constructor_exists():
    assert callable(scxmlxt::DomainModelImport.__init__)


def test_scxmlxt::domainmodelimport_constructor_args():
    sig = inspect.signature(scxmlxt::DomainModelImport.__init__)
    params = list(sig.parameters.keys())



def test_intliteral_is_not_abstract():
    assert not inspect.isabstract(IntLiteral)


def test_intliteral_constructor_exists():
    assert callable(IntLiteral.__init__)


def test_intliteral_constructor_args():
    sig = inspect.signature(IntLiteral.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::delayliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::DelayLiteral)


def test_scxmlxt::delayliteral_constructor_exists():
    assert callable(scxmlxt::DelayLiteral.__init__)


def test_scxmlxt::delayliteral_constructor_args():
    sig = inspect.signature(scxmlxt::DelayLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "timeUnit" in params, "Missing parameter 'timeUnit'"

def test_scxmlxt::delayliteral_has_timeUnit():
    assert hasattr(scxmlxt::DelayLiteral, "timeUnit")
    descriptor = None
    for klass in scxmlxt::DelayLiteral.__mro__:
        if "timeUnit" in klass.__dict__:
            descriptor = klass.__dict__["timeUnit"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::eobject_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::EObject)


def test_scxmlxt::eobject_constructor_exists():
    assert callable(scxmlxt::EObject.__init__)


def test_scxmlxt::eobject_constructor_args():
    sig = inspect.signature(scxmlxt::EObject.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::eobjectreference_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::EObjectReference)


def test_scxmlxt::eobjectreference_constructor_exists():
    assert callable(scxmlxt::EObjectReference.__init__)


def test_scxmlxt::eobjectreference_constructor_args():
    sig = inspect.signature(scxmlxt::EObjectReference.__init__)
    params = list(sig.parameters.keys())



def test_resourceuriliteral_is_not_abstract():
    assert not inspect.isabstract(ResourceUriLiteral)


def test_resourceuriliteral_constructor_exists():
    assert callable(ResourceUriLiteral.__init__)


def test_resourceuriliteral_constructor_args():
    sig = inspect.signature(ResourceUriLiteral.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::eobjecturiliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::EObjectUriLiteral)


def test_scxmlxt::eobjecturiliteral_constructor_exists():
    assert callable(scxmlxt::EObjectUriLiteral.__init__)


def test_scxmlxt::eobjecturiliteral_constructor_args():
    sig = inspect.signature(scxmlxt::EObjectUriLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "uriFragment" in params, "Missing parameter 'uriFragment'"

def test_scxmlxt::eobjecturiliteral_has_uriFragment():
    assert hasattr(scxmlxt::EObjectUriLiteral, "uriFragment")
    descriptor = None
    for klass in scxmlxt::EObjectUriLiteral.__mro__:
        if "uriFragment" in klass.__dict__:
            descriptor = klass.__dict__["uriFragment"]
            break
    assert isinstance(descriptor, property)



def test_abstracturiliteral_is_not_abstract():
    assert not inspect.isabstract(AbstractUriLiteral)


def test_abstracturiliteral_constructor_exists():
    assert callable(AbstractUriLiteral.__init__)


def test_abstracturiliteral_constructor_args():
    sig = inspect.signature(AbstractUriLiteral.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::resourceuriliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::ResourceUriLiteral)


def test_scxmlxt::resourceuriliteral_constructor_exists():
    assert callable(scxmlxt::ResourceUriLiteral.__init__)


def test_scxmlxt::resourceuriliteral_constructor_args():
    sig = inspect.signature(scxmlxt::ResourceUriLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "resourceUri" in params, "Missing parameter 'resourceUri'"

def test_scxmlxt::resourceuriliteral_has_resourceUri():
    assert hasattr(scxmlxt::ResourceUriLiteral, "resourceUri")
    descriptor = None
    for klass in scxmlxt::ResourceUriLiteral.__mro__:
        if "resourceUri" in klass.__dict__:
            descriptor = klass.__dict__["resourceUri"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::uriliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::UriLiteral)


def test_scxmlxt::uriliteral_constructor_exists():
    assert callable(scxmlxt::UriLiteral.__init__)


def test_scxmlxt::uriliteral_constructor_args():
    sig = inspect.signature(scxmlxt::UriLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "uriValue" in params, "Missing parameter 'uriValue'"

def test_scxmlxt::uriliteral_has_uriValue():
    assert hasattr(scxmlxt::UriLiteral, "uriValue")
    descriptor = None
    for klass in scxmlxt::UriLiteral.__mro__:
        if "uriValue" in klass.__dict__:
            descriptor = klass.__dict__["uriValue"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::varref_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::VarRef)


def test_scxmlxt::varref_constructor_exists():
    assert callable(scxmlxt::VarRef.__init__)


def test_scxmlxt::varref_constructor_args():
    sig = inspect.signature(scxmlxt::VarRef.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::abstracturiliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::AbstractUriLiteral)


def test_scxmlxt::abstracturiliteral_constructor_exists():
    assert callable(scxmlxt::AbstractUriLiteral.__init__)


def test_scxmlxt::abstracturiliteral_constructor_args():
    sig = inspect.signature(scxmlxt::AbstractUriLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_scxmlxt::abstracturiliteral_has_uri():
    assert hasattr(scxmlxt::AbstractUriLiteral, "uri")
    descriptor = None
    for klass in scxmlxt::AbstractUriLiteral.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::floatliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::FloatLiteral)


def test_scxmlxt::floatliteral_constructor_exists():
    assert callable(scxmlxt::FloatLiteral.__init__)


def test_scxmlxt::floatliteral_constructor_args():
    sig = inspect.signature(scxmlxt::FloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "floatValue" in params, "Missing parameter 'floatValue'"

def test_scxmlxt::floatliteral_has_floatValue():
    assert hasattr(scxmlxt::FloatLiteral, "floatValue")
    descriptor = None
    for klass in scxmlxt::FloatLiteral.__mro__:
        if "floatValue" in klass.__dict__:
            descriptor = klass.__dict__["floatValue"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::stringliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::StringLiteral)


def test_scxmlxt::stringliteral_constructor_exists():
    assert callable(scxmlxt::StringLiteral.__init__)


def test_scxmlxt::stringliteral_constructor_args():
    sig = inspect.signature(scxmlxt::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "stringValue" in params, "Missing parameter 'stringValue'"

def test_scxmlxt::stringliteral_has_stringValue():
    assert hasattr(scxmlxt::StringLiteral, "stringValue")
    descriptor = None
    for klass in scxmlxt::StringLiteral.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::intliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::IntLiteral)


def test_scxmlxt::intliteral_constructor_exists():
    assert callable(scxmlxt::IntLiteral.__init__)


def test_scxmlxt::intliteral_constructor_args():
    sig = inspect.signature(scxmlxt::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "intValue" in params, "Missing parameter 'intValue'"

def test_scxmlxt::intliteral_has_intValue():
    assert hasattr(scxmlxt::IntLiteral, "intValue")
    descriptor = None
    for klass in scxmlxt::IntLiteral.__mro__:
        if "intValue" in klass.__dict__:
            descriptor = klass.__dict__["intValue"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::BooleanLiteral)


def test_scxmlxt::booleanliteral_constructor_exists():
    assert callable(scxmlxt::BooleanLiteral.__init__)


def test_scxmlxt::booleanliteral_constructor_args():
    sig = inspect.signature(scxmlxt::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_scxmlxt::booleanliteral_has_booleanValue():
    assert hasattr(scxmlxt::BooleanLiteral, "booleanValue")
    descriptor = None
    for klass in scxmlxt::BooleanLiteral.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::literal_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::Literal)


def test_scxmlxt::literal_constructor_exists():
    assert callable(scxmlxt::Literal.__init__)


def test_scxmlxt::literal_constructor_args():
    sig = inspect.signature(scxmlxt::Literal.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::scriptexpression_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::ScriptExpression)


def test_scxmlxt::scriptexpression_constructor_exists():
    assert callable(scxmlxt::ScriptExpression.__init__)


def test_scxmlxt::scriptexpression_constructor_args():
    sig = inspect.signature(scxmlxt::ScriptExpression.__init__)
    params = list(sig.parameters.keys())
    assert "script" in params, "Missing parameter 'script'"

def test_scxmlxt::scriptexpression_has_script():
    assert hasattr(scxmlxt::ScriptExpression, "script")
    descriptor = None
    for klass in scxmlxt::ScriptExpression.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::estepfilter_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::EStepFilter)


def test_scxmlxt::estepfilter_constructor_exists():
    assert callable(scxmlxt::EStepFilter.__init__)


def test_scxmlxt::estepfilter_constructor_args():
    sig = inspect.signature(scxmlxt::EStepFilter.__init__)
    params = list(sig.parameters.keys())
    assert "freeVarName" in params, "Missing parameter 'freeVarName'"

def test_scxmlxt::estepfilter_has_freeVarName():
    assert hasattr(scxmlxt::EStepFilter, "freeVarName")
    descriptor = None
    for klass in scxmlxt::EStepFilter.__mro__:
        if "freeVarName" in klass.__dict__:
            descriptor = klass.__dict__["freeVarName"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::estep_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::EStep)


def test_scxmlxt::estep_constructor_exists():
    assert callable(scxmlxt::EStep.__init__)


def test_scxmlxt::estep_constructor_args():
    sig = inspect.signature(scxmlxt::EStep.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_scxmlxt::estep_has_featureName():
    assert hasattr(scxmlxt::EStep, "featureName")
    descriptor = None
    for klass in scxmlxt::EStep.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::epath_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::EPath)


def test_scxmlxt::epath_constructor_exists():
    assert callable(scxmlxt::EPath.__init__)


def test_scxmlxt::epath_constructor_args():
    sig = inspect.signature(scxmlxt::EPath.__init__)
    params = list(sig.parameters.keys())



def test_typed_is_not_abstract():
    assert not inspect.isabstract(Typed)


def test_typed_constructor_exists():
    assert callable(Typed.__init__)


def test_typed_constructor_args():
    sig = inspect.signature(Typed.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::eclassifier_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::EClassifier)


def test_scxmlxt::eclassifier_constructor_exists():
    assert callable(scxmlxt::EClassifier.__init__)


def test_scxmlxt::eclassifier_constructor_args():
    sig = inspect.signature(scxmlxt::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::typed_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::Typed)


def test_scxmlxt::typed_constructor_exists():
    assert callable(scxmlxt::Typed.__init__)


def test_scxmlxt::typed_constructor_args():
    sig = inspect.signature(scxmlxt::Typed.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"

def test_scxmlxt::typed_has_many():
    assert hasattr(scxmlxt::Typed, "many")
    descriptor = None
    for klass in scxmlxt::Typed.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::assignmentaction_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::AssignmentAction)


def test_scxmlxt::assignmentaction_constructor_exists():
    assert callable(scxmlxt::AssignmentAction.__init__)


def test_scxmlxt::assignmentaction_constructor_args():
    sig = inspect.signature(scxmlxt::AssignmentAction.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::scriptaction_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::ScriptAction)


def test_scxmlxt::scriptaction_constructor_exists():
    assert callable(scxmlxt::ScriptAction.__init__)


def test_scxmlxt::scriptaction_constructor_args():
    sig = inspect.signature(scxmlxt::ScriptAction.__init__)
    params = list(sig.parameters.keys())
    assert "script" in params, "Missing parameter 'script'"

def test_scxmlxt::scriptaction_has_script():
    assert hasattr(scxmlxt::ScriptAction, "script")
    descriptor = None
    for klass in scxmlxt::ScriptAction.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::symbolicaction_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::SymbolicAction)


def test_scxmlxt::symbolicaction_constructor_exists():
    assert callable(scxmlxt::SymbolicAction.__init__)


def test_scxmlxt::symbolicaction_constructor_args():
    sig = inspect.signature(scxmlxt::SymbolicAction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_scxmlxt::symbolicaction_has_name():
    assert hasattr(scxmlxt::SymbolicAction, "name")
    descriptor = None
    for klass in scxmlxt::SymbolicAction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::expression_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::Expression)


def test_scxmlxt::expression_constructor_exists():
    assert callable(scxmlxt::Expression.__init__)


def test_scxmlxt::expression_constructor_args():
    sig = inspect.signature(scxmlxt::Expression.__init__)
    params = list(sig.parameters.keys())



def test_abstracttransitionevent_is_not_abstract():
    assert not inspect.isabstract(AbstractTransitionEvent)


def test_abstracttransitionevent_constructor_exists():
    assert callable(AbstractTransitionEvent.__init__)


def test_abstracttransitionevent_constructor_args():
    sig = inspect.signature(AbstractTransitionEvent.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::enterevent_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::EnterEvent)


def test_scxmlxt::enterevent_constructor_exists():
    assert callable(scxmlxt::EnterEvent.__init__)


def test_scxmlxt::enterevent_constructor_args():
    sig = inspect.signature(scxmlxt::EnterEvent.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::exitevent_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::ExitEvent)


def test_scxmlxt::exitevent_constructor_exists():
    assert callable(scxmlxt::ExitEvent.__init__)


def test_scxmlxt::exitevent_constructor_args():
    sig = inspect.signature(scxmlxt::ExitEvent.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::transitionevent_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::TransitionEvent)


def test_scxmlxt::transitionevent_constructor_exists():
    assert callable(scxmlxt::TransitionEvent.__init__)


def test_scxmlxt::transitionevent_constructor_args():
    sig = inspect.signature(scxmlxt::TransitionEvent.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::timerevent_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::TimerEvent)


def test_scxmlxt::timerevent_constructor_exists():
    assert callable(scxmlxt::TimerEvent.__init__)


def test_scxmlxt::timerevent_constructor_args():
    sig = inspect.signature(scxmlxt::TimerEvent.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::abstracttransitionevent_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::AbstractTransitionEvent)


def test_scxmlxt::abstracttransitionevent_constructor_exists():
    assert callable(scxmlxt::AbstractTransitionEvent.__init__)


def test_scxmlxt::abstracttransitionevent_constructor_args():
    sig = inspect.signature(scxmlxt::AbstractTransitionEvent.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::scriptevent_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::ScriptEvent)


def test_scxmlxt::scriptevent_constructor_exists():
    assert callable(scxmlxt::ScriptEvent.__init__)


def test_scxmlxt::scriptevent_constructor_args():
    sig = inspect.signature(scxmlxt::ScriptEvent.__init__)
    params = list(sig.parameters.keys())
    assert "script" in params, "Missing parameter 'script'"

def test_scxmlxt::scriptevent_has_script():
    assert hasattr(scxmlxt::ScriptEvent, "script")
    descriptor = None
    for klass in scxmlxt::ScriptEvent.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::symbolicevent_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::SymbolicEvent)


def test_scxmlxt::symbolicevent_constructor_exists():
    assert callable(scxmlxt::SymbolicEvent.__init__)


def test_scxmlxt::symbolicevent_constructor_args():
    sig = inspect.signature(scxmlxt::SymbolicEvent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_scxmlxt::symbolicevent_has_name():
    assert hasattr(scxmlxt::SymbolicEvent, "name")
    descriptor = None
    for klass in scxmlxt::SymbolicEvent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstracttransition_is_not_abstract():
    assert not inspect.isabstract(AbstractTransition)


def test_abstracttransition_constructor_exists():
    assert callable(AbstractTransition.__init__)


def test_abstracttransition_constructor_args():
    sig = inspect.signature(AbstractTransition.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::internaltransition_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::InternalTransition)


def test_scxmlxt::internaltransition_constructor_exists():
    assert callable(scxmlxt::InternalTransition.__init__)


def test_scxmlxt::internaltransition_constructor_args():
    sig = inspect.signature(scxmlxt::InternalTransition.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::transition_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::Transition)


def test_scxmlxt::transition_constructor_exists():
    assert callable(scxmlxt::Transition.__init__)


def test_scxmlxt::transition_constructor_args():
    sig = inspect.signature(scxmlxt::Transition.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::condition_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::Condition)


def test_scxmlxt::condition_constructor_exists():
    assert callable(scxmlxt::Condition.__init__)


def test_scxmlxt::condition_constructor_args():
    sig = inspect.signature(scxmlxt::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "script" in params, "Missing parameter 'script'"

def test_scxmlxt::condition_has_script():
    assert hasattr(scxmlxt::Condition, "script")
    descriptor = None
    for klass in scxmlxt::Condition.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::event_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::Event)


def test_scxmlxt::event_constructor_exists():
    assert callable(scxmlxt::Event.__init__)


def test_scxmlxt::event_constructor_args():
    sig = inspect.signature(scxmlxt::Event.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::vardef_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::VarDef)


def test_scxmlxt::vardef_constructor_exists():
    assert callable(scxmlxt::VarDef.__init__)


def test_scxmlxt::vardef_constructor_args():
    sig = inspect.signature(scxmlxt::VarDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_scxmlxt::vardef_has_name():
    assert hasattr(scxmlxt::VarDef, "name")
    descriptor = None
    for klass in scxmlxt::VarDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::abstracttransition_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::AbstractTransition)


def test_scxmlxt::abstracttransition_constructor_exists():
    assert callable(scxmlxt::AbstractTransition.__init__)


def test_scxmlxt::abstracttransition_constructor_args():
    sig = inspect.signature(scxmlxt::AbstractTransition.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::abstractstate_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::AbstractState)


def test_scxmlxt::abstractstate_constructor_exists():
    assert callable(scxmlxt::AbstractState.__init__)


def test_scxmlxt::abstractstate_constructor_args():
    sig = inspect.signature(scxmlxt::AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::action_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::Action)


def test_scxmlxt::action_constructor_exists():
    assert callable(scxmlxt::Action.__init__)


def test_scxmlxt::action_constructor_args():
    sig = inspect.signature(scxmlxt::Action.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::initialtransition_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::InitialTransition)


def test_scxmlxt::initialtransition_constructor_exists():
    assert callable(scxmlxt::InitialTransition.__init__)


def test_scxmlxt::initialtransition_constructor_args():
    sig = inspect.signature(scxmlxt::InitialTransition.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::resourceimport_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::ResourceImport)


def test_scxmlxt::resourceimport_constructor_exists():
    assert callable(scxmlxt::ResourceImport.__init__)


def test_scxmlxt::resourceimport_constructor_args():
    sig = inspect.signature(scxmlxt::ResourceImport.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_scxmlxt::resourceimport_has_importURI():
    assert hasattr(scxmlxt::ResourceImport, "importURI")
    descriptor = None
    for klass in scxmlxt::ResourceImport.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt::state_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::State)


def test_scxmlxt::state_constructor_exists():
    assert callable(scxmlxt::State.__init__)


def test_scxmlxt::state_constructor_args():
    sig = inspect.signature(scxmlxt::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_scxmlxt::state_has_name():
    assert hasattr(scxmlxt::State, "name")
    descriptor = None
    for klass in scxmlxt::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt::statemachine_is_not_abstract():
    assert not inspect.isabstract(scxmlxt::StateMachine)


def test_scxmlxt::statemachine_constructor_exists():
    assert callable(scxmlxt::StateMachine.__init__)


def test_scxmlxt::statemachine_constructor_args():
    sig = inspect.signature(scxmlxt::StateMachine.__init__)
    params = list(sig.parameters.keys())

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "h",
        "m",
        "ms",
        "s",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnit"


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
ResourceImport_strategy = st.builds(
    ResourceImport,
)
scxmlxt::DomainDataImport_strategy = st.builds(
    scxmlxt::DomainDataImport,
)
scxmlxt::DomainModelImport_strategy = st.builds(
    scxmlxt::DomainModelImport,
)
IntLiteral_strategy = st.builds(
    IntLiteral,
)
scxmlxt::DelayLiteral_strategy = st.builds(
    scxmlxt::DelayLiteral,
    timeUnit=
        safe_text
)
scxmlxt::EObject_strategy = st.builds(
    scxmlxt::EObject,
)
scxmlxt::EObjectReference_strategy = st.builds(
    scxmlxt::EObjectReference,
)
ResourceUriLiteral_strategy = st.builds(
    ResourceUriLiteral,
)
scxmlxt::EObjectUriLiteral_strategy = st.builds(
    scxmlxt::EObjectUriLiteral,
    uriFragment=
        safe_text
)
AbstractUriLiteral_strategy = st.builds(
    AbstractUriLiteral,
)
scxmlxt::ResourceUriLiteral_strategy = st.builds(
    scxmlxt::ResourceUriLiteral,
    resourceUri=
        safe_text
)
scxmlxt::UriLiteral_strategy = st.builds(
    scxmlxt::UriLiteral,
    uriValue=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
scxmlxt::VarRef_strategy = st.builds(
    scxmlxt::VarRef,
)
Literal_strategy = st.builds(
    Literal,
)
scxmlxt::AbstractUriLiteral_strategy = st.builds(
    scxmlxt::AbstractUriLiteral,
    uri=
        safe_text
)
scxmlxt::FloatLiteral_strategy = st.builds(
    scxmlxt::FloatLiteral,
    floatValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
scxmlxt::StringLiteral_strategy = st.builds(
    scxmlxt::StringLiteral,
    stringValue=
        safe_text
)
scxmlxt::IntLiteral_strategy = st.builds(
    scxmlxt::IntLiteral,
    intValue=
        st.integers()
)
scxmlxt::BooleanLiteral_strategy = st.builds(
    scxmlxt::BooleanLiteral,
    booleanValue=
        st.booleans()
)
scxmlxt::Literal_strategy = st.builds(
    scxmlxt::Literal,
)
scxmlxt::ScriptExpression_strategy = st.builds(
    scxmlxt::ScriptExpression,
    script=
        safe_text
)
scxmlxt::EStepFilter_strategy = st.builds(
    scxmlxt::EStepFilter,
    freeVarName=
        safe_text
)
scxmlxt::EStep_strategy = st.builds(
    scxmlxt::EStep,
    featureName=
        safe_text
)
scxmlxt::EPath_strategy = st.builds(
    scxmlxt::EPath,
)
Typed_strategy = st.builds(
    Typed,
)
scxmlxt::EClassifier_strategy = st.builds(
    scxmlxt::EClassifier,
)
scxmlxt::Typed_strategy = st.builds(
    scxmlxt::Typed,
    many=
        st.booleans()
)
Action_strategy = st.builds(
    Action,
)
scxmlxt::AssignmentAction_strategy = st.builds(
    scxmlxt::AssignmentAction,
)
scxmlxt::ScriptAction_strategy = st.builds(
    scxmlxt::ScriptAction,
    script=
        safe_text
)
scxmlxt::SymbolicAction_strategy = st.builds(
    scxmlxt::SymbolicAction,
    name=
        safe_text
)
scxmlxt::Expression_strategy = st.builds(
    scxmlxt::Expression,
)
AbstractTransitionEvent_strategy = st.builds(
    AbstractTransitionEvent,
)
scxmlxt::EnterEvent_strategy = st.builds(
    scxmlxt::EnterEvent,
)
scxmlxt::ExitEvent_strategy = st.builds(
    scxmlxt::ExitEvent,
)
scxmlxt::TransitionEvent_strategy = st.builds(
    scxmlxt::TransitionEvent,
)
Event_strategy = st.builds(
    Event,
)
scxmlxt::TimerEvent_strategy = st.builds(
    scxmlxt::TimerEvent,
)
scxmlxt::AbstractTransitionEvent_strategy = st.builds(
    scxmlxt::AbstractTransitionEvent,
)
scxmlxt::ScriptEvent_strategy = st.builds(
    scxmlxt::ScriptEvent,
    script=
        safe_text
)
scxmlxt::SymbolicEvent_strategy = st.builds(
    scxmlxt::SymbolicEvent,
    name=
        safe_text
)
AbstractTransition_strategy = st.builds(
    AbstractTransition,
)
scxmlxt::InternalTransition_strategy = st.builds(
    scxmlxt::InternalTransition,
)
scxmlxt::Transition_strategy = st.builds(
    scxmlxt::Transition,
)
scxmlxt::Condition_strategy = st.builds(
    scxmlxt::Condition,
    script=
        safe_text
)
scxmlxt::Event_strategy = st.builds(
    scxmlxt::Event,
)
scxmlxt::VarDef_strategy = st.builds(
    scxmlxt::VarDef,
    name=
        safe_text
)
scxmlxt::AbstractTransition_strategy = st.builds(
    scxmlxt::AbstractTransition,
)
scxmlxt::AbstractState_strategy = st.builds(
    scxmlxt::AbstractState,
)
scxmlxt::Action_strategy = st.builds(
    scxmlxt::Action,
)
scxmlxt::InitialTransition_strategy = st.builds(
    scxmlxt::InitialTransition,
)
scxmlxt::ResourceImport_strategy = st.builds(
    scxmlxt::ResourceImport,
    importURI=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
scxmlxt::State_strategy = st.builds(
    scxmlxt::State,
    name=
        safe_text
)
scxmlxt::StateMachine_strategy = st.builds(
    scxmlxt::StateMachine,
)

@given(instance=ResourceImport_strategy)
@settings(max_examples=50)
def test_resourceimport_instantiation(instance):
    assert isinstance(instance, ResourceImport)

@given(instance=scxmlxt::DomainDataImport_strategy)
@settings(max_examples=50)
def test_scxmlxt::domaindataimport_instantiation(instance):
    assert isinstance(instance, scxmlxt::DomainDataImport)

@given(instance=scxmlxt::DomainModelImport_strategy)
@settings(max_examples=50)
def test_scxmlxt::domainmodelimport_instantiation(instance):
    assert isinstance(instance, scxmlxt::DomainModelImport)

@given(instance=IntLiteral_strategy)
@settings(max_examples=50)
def test_intliteral_instantiation(instance):
    assert isinstance(instance, IntLiteral)

@given(instance=scxmlxt::DelayLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt::delayliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt::DelayLiteral)

@given(instance=scxmlxt::DelayLiteral_strategy)
def test_scxmlxt::delayliteral_timeUnit_type(instance):
    assert isinstance(instance.timeUnit, str)


@given(instance=scxmlxt::DelayLiteral_strategy)
def test_scxmlxt::delayliteral_timeUnit_setter(instance):
    original = instance.timeUnit
    instance.timeUnit = original
    assert instance.timeUnit == original

@given(instance=scxmlxt::EObject_strategy)
@settings(max_examples=50)
def test_scxmlxt::eobject_instantiation(instance):
    assert isinstance(instance, scxmlxt::EObject)

@given(instance=scxmlxt::EObjectReference_strategy)
@settings(max_examples=50)
def test_scxmlxt::eobjectreference_instantiation(instance):
    assert isinstance(instance, scxmlxt::EObjectReference)

@given(instance=ResourceUriLiteral_strategy)
@settings(max_examples=50)
def test_resourceuriliteral_instantiation(instance):
    assert isinstance(instance, ResourceUriLiteral)

@given(instance=scxmlxt::EObjectUriLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt::eobjecturiliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt::EObjectUriLiteral)

@given(instance=scxmlxt::EObjectUriLiteral_strategy)
def test_scxmlxt::eobjecturiliteral_uriFragment_type(instance):
    assert isinstance(instance.uriFragment, str)


@given(instance=scxmlxt::EObjectUriLiteral_strategy)
def test_scxmlxt::eobjecturiliteral_uriFragment_setter(instance):
    original = instance.uriFragment
    instance.uriFragment = original
    assert instance.uriFragment == original

@given(instance=AbstractUriLiteral_strategy)
@settings(max_examples=50)
def test_abstracturiliteral_instantiation(instance):
    assert isinstance(instance, AbstractUriLiteral)

@given(instance=scxmlxt::ResourceUriLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt::resourceuriliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt::ResourceUriLiteral)

@given(instance=scxmlxt::ResourceUriLiteral_strategy)
def test_scxmlxt::resourceuriliteral_resourceUri_type(instance):
    assert isinstance(instance.resourceUri, str)


@given(instance=scxmlxt::ResourceUriLiteral_strategy)
def test_scxmlxt::resourceuriliteral_resourceUri_setter(instance):
    original = instance.resourceUri
    instance.resourceUri = original
    assert instance.resourceUri == original

@given(instance=scxmlxt::UriLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt::uriliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt::UriLiteral)

@given(instance=scxmlxt::UriLiteral_strategy)
def test_scxmlxt::uriliteral_uriValue_type(instance):
    assert isinstance(instance.uriValue, str)


@given(instance=scxmlxt::UriLiteral_strategy)
def test_scxmlxt::uriliteral_uriValue_setter(instance):
    original = instance.uriValue
    instance.uriValue = original
    assert instance.uriValue == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=scxmlxt::VarRef_strategy)
@settings(max_examples=50)
def test_scxmlxt::varref_instantiation(instance):
    assert isinstance(instance, scxmlxt::VarRef)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=scxmlxt::AbstractUriLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt::abstracturiliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt::AbstractUriLiteral)

@given(instance=scxmlxt::AbstractUriLiteral_strategy)
def test_scxmlxt::abstracturiliteral_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=scxmlxt::AbstractUriLiteral_strategy)
def test_scxmlxt::abstracturiliteral_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=scxmlxt::FloatLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt::floatliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt::FloatLiteral)

@given(instance=scxmlxt::FloatLiteral_strategy)
def test_scxmlxt::floatliteral_floatValue_type(instance):
    assert isinstance(instance.floatValue, float)


@given(instance=scxmlxt::FloatLiteral_strategy)
def test_scxmlxt::floatliteral_floatValue_setter(instance):
    original = instance.floatValue
    instance.floatValue = original
    assert instance.floatValue == original

@given(instance=scxmlxt::StringLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt::stringliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt::StringLiteral)

@given(instance=scxmlxt::StringLiteral_strategy)
def test_scxmlxt::stringliteral_stringValue_type(instance):
    assert isinstance(instance.stringValue, str)


@given(instance=scxmlxt::StringLiteral_strategy)
def test_scxmlxt::stringliteral_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=scxmlxt::IntLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt::intliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt::IntLiteral)

@given(instance=scxmlxt::IntLiteral_strategy)
def test_scxmlxt::intliteral_intValue_type(instance):
    assert isinstance(instance.intValue, int)


@given(instance=scxmlxt::IntLiteral_strategy)
def test_scxmlxt::intliteral_intValue_setter(instance):
    original = instance.intValue
    instance.intValue = original
    assert instance.intValue == original

@given(instance=scxmlxt::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt::booleanliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt::BooleanLiteral)

@given(instance=scxmlxt::BooleanLiteral_strategy)
def test_scxmlxt::booleanliteral_booleanValue_type(instance):
    assert isinstance(instance.booleanValue, bool)


@given(instance=scxmlxt::BooleanLiteral_strategy)
def test_scxmlxt::booleanliteral_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=scxmlxt::Literal_strategy)
@settings(max_examples=50)
def test_scxmlxt::literal_instantiation(instance):
    assert isinstance(instance, scxmlxt::Literal)

@given(instance=scxmlxt::ScriptExpression_strategy)
@settings(max_examples=50)
def test_scxmlxt::scriptexpression_instantiation(instance):
    assert isinstance(instance, scxmlxt::ScriptExpression)

@given(instance=scxmlxt::ScriptExpression_strategy)
def test_scxmlxt::scriptexpression_script_type(instance):
    assert isinstance(instance.script, str)


@given(instance=scxmlxt::ScriptExpression_strategy)
def test_scxmlxt::scriptexpression_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original

@given(instance=scxmlxt::EStepFilter_strategy)
@settings(max_examples=50)
def test_scxmlxt::estepfilter_instantiation(instance):
    assert isinstance(instance, scxmlxt::EStepFilter)

@given(instance=scxmlxt::EStepFilter_strategy)
def test_scxmlxt::estepfilter_freeVarName_type(instance):
    assert isinstance(instance.freeVarName, str)


@given(instance=scxmlxt::EStepFilter_strategy)
def test_scxmlxt::estepfilter_freeVarName_setter(instance):
    original = instance.freeVarName
    instance.freeVarName = original
    assert instance.freeVarName == original

@given(instance=scxmlxt::EStep_strategy)
@settings(max_examples=50)
def test_scxmlxt::estep_instantiation(instance):
    assert isinstance(instance, scxmlxt::EStep)

@given(instance=scxmlxt::EStep_strategy)
def test_scxmlxt::estep_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=scxmlxt::EStep_strategy)
def test_scxmlxt::estep_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=scxmlxt::EPath_strategy)
@settings(max_examples=50)
def test_scxmlxt::epath_instantiation(instance):
    assert isinstance(instance, scxmlxt::EPath)

@given(instance=Typed_strategy)
@settings(max_examples=50)
def test_typed_instantiation(instance):
    assert isinstance(instance, Typed)

@given(instance=scxmlxt::EClassifier_strategy)
@settings(max_examples=50)
def test_scxmlxt::eclassifier_instantiation(instance):
    assert isinstance(instance, scxmlxt::EClassifier)

@given(instance=scxmlxt::Typed_strategy)
@settings(max_examples=50)
def test_scxmlxt::typed_instantiation(instance):
    assert isinstance(instance, scxmlxt::Typed)

@given(instance=scxmlxt::Typed_strategy)
def test_scxmlxt::typed_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=scxmlxt::Typed_strategy)
def test_scxmlxt::typed_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=scxmlxt::AssignmentAction_strategy)
@settings(max_examples=50)
def test_scxmlxt::assignmentaction_instantiation(instance):
    assert isinstance(instance, scxmlxt::AssignmentAction)

@given(instance=scxmlxt::ScriptAction_strategy)
@settings(max_examples=50)
def test_scxmlxt::scriptaction_instantiation(instance):
    assert isinstance(instance, scxmlxt::ScriptAction)

@given(instance=scxmlxt::ScriptAction_strategy)
def test_scxmlxt::scriptaction_script_type(instance):
    assert isinstance(instance.script, str)


@given(instance=scxmlxt::ScriptAction_strategy)
def test_scxmlxt::scriptaction_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original

@given(instance=scxmlxt::SymbolicAction_strategy)
@settings(max_examples=50)
def test_scxmlxt::symbolicaction_instantiation(instance):
    assert isinstance(instance, scxmlxt::SymbolicAction)

@given(instance=scxmlxt::SymbolicAction_strategy)
def test_scxmlxt::symbolicaction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scxmlxt::SymbolicAction_strategy)
def test_scxmlxt::symbolicaction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scxmlxt::Expression_strategy)
@settings(max_examples=50)
def test_scxmlxt::expression_instantiation(instance):
    assert isinstance(instance, scxmlxt::Expression)

@given(instance=AbstractTransitionEvent_strategy)
@settings(max_examples=50)
def test_abstracttransitionevent_instantiation(instance):
    assert isinstance(instance, AbstractTransitionEvent)

@given(instance=scxmlxt::EnterEvent_strategy)
@settings(max_examples=50)
def test_scxmlxt::enterevent_instantiation(instance):
    assert isinstance(instance, scxmlxt::EnterEvent)

@given(instance=scxmlxt::ExitEvent_strategy)
@settings(max_examples=50)
def test_scxmlxt::exitevent_instantiation(instance):
    assert isinstance(instance, scxmlxt::ExitEvent)

@given(instance=scxmlxt::TransitionEvent_strategy)
@settings(max_examples=50)
def test_scxmlxt::transitionevent_instantiation(instance):
    assert isinstance(instance, scxmlxt::TransitionEvent)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=scxmlxt::TimerEvent_strategy)
@settings(max_examples=50)
def test_scxmlxt::timerevent_instantiation(instance):
    assert isinstance(instance, scxmlxt::TimerEvent)

@given(instance=scxmlxt::AbstractTransitionEvent_strategy)
@settings(max_examples=50)
def test_scxmlxt::abstracttransitionevent_instantiation(instance):
    assert isinstance(instance, scxmlxt::AbstractTransitionEvent)

@given(instance=scxmlxt::ScriptEvent_strategy)
@settings(max_examples=50)
def test_scxmlxt::scriptevent_instantiation(instance):
    assert isinstance(instance, scxmlxt::ScriptEvent)

@given(instance=scxmlxt::ScriptEvent_strategy)
def test_scxmlxt::scriptevent_script_type(instance):
    assert isinstance(instance.script, str)


@given(instance=scxmlxt::ScriptEvent_strategy)
def test_scxmlxt::scriptevent_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original

@given(instance=scxmlxt::SymbolicEvent_strategy)
@settings(max_examples=50)
def test_scxmlxt::symbolicevent_instantiation(instance):
    assert isinstance(instance, scxmlxt::SymbolicEvent)

@given(instance=scxmlxt::SymbolicEvent_strategy)
def test_scxmlxt::symbolicevent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scxmlxt::SymbolicEvent_strategy)
def test_scxmlxt::symbolicevent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractTransition_strategy)
@settings(max_examples=50)
def test_abstracttransition_instantiation(instance):
    assert isinstance(instance, AbstractTransition)

@given(instance=scxmlxt::InternalTransition_strategy)
@settings(max_examples=50)
def test_scxmlxt::internaltransition_instantiation(instance):
    assert isinstance(instance, scxmlxt::InternalTransition)

@given(instance=scxmlxt::Transition_strategy)
@settings(max_examples=50)
def test_scxmlxt::transition_instantiation(instance):
    assert isinstance(instance, scxmlxt::Transition)

@given(instance=scxmlxt::Condition_strategy)
@settings(max_examples=50)
def test_scxmlxt::condition_instantiation(instance):
    assert isinstance(instance, scxmlxt::Condition)

@given(instance=scxmlxt::Condition_strategy)
def test_scxmlxt::condition_script_type(instance):
    assert isinstance(instance.script, str)


@given(instance=scxmlxt::Condition_strategy)
def test_scxmlxt::condition_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original

@given(instance=scxmlxt::Event_strategy)
@settings(max_examples=50)
def test_scxmlxt::event_instantiation(instance):
    assert isinstance(instance, scxmlxt::Event)

@given(instance=scxmlxt::VarDef_strategy)
@settings(max_examples=50)
def test_scxmlxt::vardef_instantiation(instance):
    assert isinstance(instance, scxmlxt::VarDef)

@given(instance=scxmlxt::VarDef_strategy)
def test_scxmlxt::vardef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scxmlxt::VarDef_strategy)
def test_scxmlxt::vardef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scxmlxt::AbstractTransition_strategy)
@settings(max_examples=50)
def test_scxmlxt::abstracttransition_instantiation(instance):
    assert isinstance(instance, scxmlxt::AbstractTransition)

@given(instance=scxmlxt::AbstractState_strategy)
@settings(max_examples=50)
def test_scxmlxt::abstractstate_instantiation(instance):
    assert isinstance(instance, scxmlxt::AbstractState)

@given(instance=scxmlxt::Action_strategy)
@settings(max_examples=50)
def test_scxmlxt::action_instantiation(instance):
    assert isinstance(instance, scxmlxt::Action)

@given(instance=scxmlxt::InitialTransition_strategy)
@settings(max_examples=50)
def test_scxmlxt::initialtransition_instantiation(instance):
    assert isinstance(instance, scxmlxt::InitialTransition)

@given(instance=scxmlxt::ResourceImport_strategy)
@settings(max_examples=50)
def test_scxmlxt::resourceimport_instantiation(instance):
    assert isinstance(instance, scxmlxt::ResourceImport)

@given(instance=scxmlxt::ResourceImport_strategy)
def test_scxmlxt::resourceimport_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=scxmlxt::ResourceImport_strategy)
def test_scxmlxt::resourceimport_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=scxmlxt::State_strategy)
@settings(max_examples=50)
def test_scxmlxt::state_instantiation(instance):
    assert isinstance(instance, scxmlxt::State)

@given(instance=scxmlxt::State_strategy)
def test_scxmlxt::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scxmlxt::State_strategy)
def test_scxmlxt::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scxmlxt::StateMachine_strategy)
@settings(max_examples=50)
def test_scxmlxt::statemachine_instantiation(instance):
    assert isinstance(instance, scxmlxt::StateMachine)
