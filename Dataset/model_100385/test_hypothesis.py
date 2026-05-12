import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ResourceImport,
    scxmlxt_DomainDataImport,
    scxmlxt_DomainModelImport,
    IntLiteral,
    scxmlxt_DelayLiteral,
    scxmlxt_EObject,
    scxmlxt_EObjectReference,
    ResourceUriLiteral,
    scxmlxt_EObjectUriLiteral,
    AbstractUriLiteral,
    scxmlxt_ResourceUriLiteral,
    scxmlxt_UriLiteral,
    Expression,
    scxmlxt_VarRef,
    Literal,
    scxmlxt_StringLiteral,
    scxmlxt_IntLiteral,
    scxmlxt_AbstractUriLiteral,
    scxmlxt_FloatLiteral,
    scxmlxt_BooleanLiteral,
    scxmlxt_Literal,
    scxmlxt_ScriptExpression,
    scxmlxt_EStepFilter,
    scxmlxt_EStep,
    scxmlxt_EPath,
    Typed,
    scxmlxt_EClassifier,
    scxmlxt_Typed,
    Action,
    scxmlxt_AssignmentAction,
    scxmlxt_ScriptAction,
    scxmlxt_SymbolicAction,
    scxmlxt_Expression,
    AbstractTransitionEvent,
    scxmlxt_EnterEvent,
    scxmlxt_ExitEvent,
    scxmlxt_TransitionEvent,
    Event,
    scxmlxt_TimerEvent,
    scxmlxt_ScriptEvent,
    scxmlxt_AbstractTransitionEvent,
    scxmlxt_SymbolicEvent,
    AbstractTransition,
    scxmlxt_InternalTransition,
    scxmlxt_Transition,
    scxmlxt_Condition,
    scxmlxt_Event,
    scxmlxt_VarDef,
    scxmlxt_AbstractTransition,
    scxmlxt_AbstractState,
    scxmlxt_Action,
    scxmlxt_InitialTransition,
    scxmlxt_ResourceImport,
    AbstractState,
    scxmlxt_State,
    scxmlxt_StateMachine,
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



def test_scxmlxt_domaindataimport_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_DomainDataImport)


def test_scxmlxt_domaindataimport_constructor_exists():
    assert callable(scxmlxt_DomainDataImport.__init__)


def test_scxmlxt_domaindataimport_constructor_args():
    sig = inspect.signature(scxmlxt_DomainDataImport.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_domainmodelimport_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_DomainModelImport)


def test_scxmlxt_domainmodelimport_constructor_exists():
    assert callable(scxmlxt_DomainModelImport.__init__)


def test_scxmlxt_domainmodelimport_constructor_args():
    sig = inspect.signature(scxmlxt_DomainModelImport.__init__)
    params = list(sig.parameters.keys())



def test_intliteral_is_not_abstract():
    assert not inspect.isabstract(IntLiteral)


def test_intliteral_constructor_exists():
    assert callable(IntLiteral.__init__)


def test_intliteral_constructor_args():
    sig = inspect.signature(IntLiteral.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_delayliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_DelayLiteral)


def test_scxmlxt_delayliteral_constructor_exists():
    assert callable(scxmlxt_DelayLiteral.__init__)


def test_scxmlxt_delayliteral_constructor_args():
    sig = inspect.signature(scxmlxt_DelayLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "timeUnit" in params, "Missing parameter 'timeUnit'"

def test_scxmlxt_delayliteral_has_timeUnit():
    assert hasattr(scxmlxt_DelayLiteral, "timeUnit")
    descriptor = None
    for klass in scxmlxt_DelayLiteral.__mro__:
        if "timeUnit" in klass.__dict__:
            descriptor = klass.__dict__["timeUnit"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_eobject_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_EObject)


def test_scxmlxt_eobject_constructor_exists():
    assert callable(scxmlxt_EObject.__init__)


def test_scxmlxt_eobject_constructor_args():
    sig = inspect.signature(scxmlxt_EObject.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_eobjectreference_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_EObjectReference)


def test_scxmlxt_eobjectreference_constructor_exists():
    assert callable(scxmlxt_EObjectReference.__init__)


def test_scxmlxt_eobjectreference_constructor_args():
    sig = inspect.signature(scxmlxt_EObjectReference.__init__)
    params = list(sig.parameters.keys())



def test_resourceuriliteral_is_not_abstract():
    assert not inspect.isabstract(ResourceUriLiteral)


def test_resourceuriliteral_constructor_exists():
    assert callable(ResourceUriLiteral.__init__)


def test_resourceuriliteral_constructor_args():
    sig = inspect.signature(ResourceUriLiteral.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_eobjecturiliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_EObjectUriLiteral)


def test_scxmlxt_eobjecturiliteral_constructor_exists():
    assert callable(scxmlxt_EObjectUriLiteral.__init__)


def test_scxmlxt_eobjecturiliteral_constructor_args():
    sig = inspect.signature(scxmlxt_EObjectUriLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "uriFragment" in params, "Missing parameter 'uriFragment'"

def test_scxmlxt_eobjecturiliteral_has_uriFragment():
    assert hasattr(scxmlxt_EObjectUriLiteral, "uriFragment")
    descriptor = None
    for klass in scxmlxt_EObjectUriLiteral.__mro__:
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



def test_scxmlxt_resourceuriliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_ResourceUriLiteral)


def test_scxmlxt_resourceuriliteral_constructor_exists():
    assert callable(scxmlxt_ResourceUriLiteral.__init__)


def test_scxmlxt_resourceuriliteral_constructor_args():
    sig = inspect.signature(scxmlxt_ResourceUriLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "resourceUri" in params, "Missing parameter 'resourceUri'"

def test_scxmlxt_resourceuriliteral_has_resourceUri():
    assert hasattr(scxmlxt_ResourceUriLiteral, "resourceUri")
    descriptor = None
    for klass in scxmlxt_ResourceUriLiteral.__mro__:
        if "resourceUri" in klass.__dict__:
            descriptor = klass.__dict__["resourceUri"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_uriliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_UriLiteral)


def test_scxmlxt_uriliteral_constructor_exists():
    assert callable(scxmlxt_UriLiteral.__init__)


def test_scxmlxt_uriliteral_constructor_args():
    sig = inspect.signature(scxmlxt_UriLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "uriValue" in params, "Missing parameter 'uriValue'"

def test_scxmlxt_uriliteral_has_uriValue():
    assert hasattr(scxmlxt_UriLiteral, "uriValue")
    descriptor = None
    for klass in scxmlxt_UriLiteral.__mro__:
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



def test_scxmlxt_varref_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_VarRef)


def test_scxmlxt_varref_constructor_exists():
    assert callable(scxmlxt_VarRef.__init__)


def test_scxmlxt_varref_constructor_args():
    sig = inspect.signature(scxmlxt_VarRef.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_stringliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_StringLiteral)


def test_scxmlxt_stringliteral_constructor_exists():
    assert callable(scxmlxt_StringLiteral.__init__)


def test_scxmlxt_stringliteral_constructor_args():
    sig = inspect.signature(scxmlxt_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "stringValue" in params, "Missing parameter 'stringValue'"

def test_scxmlxt_stringliteral_has_stringValue():
    assert hasattr(scxmlxt_StringLiteral, "stringValue")
    descriptor = None
    for klass in scxmlxt_StringLiteral.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_intliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_IntLiteral)


def test_scxmlxt_intliteral_constructor_exists():
    assert callable(scxmlxt_IntLiteral.__init__)


def test_scxmlxt_intliteral_constructor_args():
    sig = inspect.signature(scxmlxt_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "intValue" in params, "Missing parameter 'intValue'"

def test_scxmlxt_intliteral_has_intValue():
    assert hasattr(scxmlxt_IntLiteral, "intValue")
    descriptor = None
    for klass in scxmlxt_IntLiteral.__mro__:
        if "intValue" in klass.__dict__:
            descriptor = klass.__dict__["intValue"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_abstracturiliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_AbstractUriLiteral)


def test_scxmlxt_abstracturiliteral_constructor_exists():
    assert callable(scxmlxt_AbstractUriLiteral.__init__)


def test_scxmlxt_abstracturiliteral_constructor_args():
    sig = inspect.signature(scxmlxt_AbstractUriLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_scxmlxt_abstracturiliteral_has_uri():
    assert hasattr(scxmlxt_AbstractUriLiteral, "uri")
    descriptor = None
    for klass in scxmlxt_AbstractUriLiteral.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_floatliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_FloatLiteral)


def test_scxmlxt_floatliteral_constructor_exists():
    assert callable(scxmlxt_FloatLiteral.__init__)


def test_scxmlxt_floatliteral_constructor_args():
    sig = inspect.signature(scxmlxt_FloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "floatValue" in params, "Missing parameter 'floatValue'"

def test_scxmlxt_floatliteral_has_floatValue():
    assert hasattr(scxmlxt_FloatLiteral, "floatValue")
    descriptor = None
    for klass in scxmlxt_FloatLiteral.__mro__:
        if "floatValue" in klass.__dict__:
            descriptor = klass.__dict__["floatValue"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_BooleanLiteral)


def test_scxmlxt_booleanliteral_constructor_exists():
    assert callable(scxmlxt_BooleanLiteral.__init__)


def test_scxmlxt_booleanliteral_constructor_args():
    sig = inspect.signature(scxmlxt_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_scxmlxt_booleanliteral_has_booleanValue():
    assert hasattr(scxmlxt_BooleanLiteral, "booleanValue")
    descriptor = None
    for klass in scxmlxt_BooleanLiteral.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_literal_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_Literal)


def test_scxmlxt_literal_constructor_exists():
    assert callable(scxmlxt_Literal.__init__)


def test_scxmlxt_literal_constructor_args():
    sig = inspect.signature(scxmlxt_Literal.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_scriptexpression_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_ScriptExpression)


def test_scxmlxt_scriptexpression_constructor_exists():
    assert callable(scxmlxt_ScriptExpression.__init__)


def test_scxmlxt_scriptexpression_constructor_args():
    sig = inspect.signature(scxmlxt_ScriptExpression.__init__)
    params = list(sig.parameters.keys())
    assert "script" in params, "Missing parameter 'script'"

def test_scxmlxt_scriptexpression_has_script():
    assert hasattr(scxmlxt_ScriptExpression, "script")
    descriptor = None
    for klass in scxmlxt_ScriptExpression.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_estepfilter_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_EStepFilter)


def test_scxmlxt_estepfilter_constructor_exists():
    assert callable(scxmlxt_EStepFilter.__init__)


def test_scxmlxt_estepfilter_constructor_args():
    sig = inspect.signature(scxmlxt_EStepFilter.__init__)
    params = list(sig.parameters.keys())
    assert "freeVarName" in params, "Missing parameter 'freeVarName'"

def test_scxmlxt_estepfilter_has_freeVarName():
    assert hasattr(scxmlxt_EStepFilter, "freeVarName")
    descriptor = None
    for klass in scxmlxt_EStepFilter.__mro__:
        if "freeVarName" in klass.__dict__:
            descriptor = klass.__dict__["freeVarName"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_estep_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_EStep)


def test_scxmlxt_estep_constructor_exists():
    assert callable(scxmlxt_EStep.__init__)


def test_scxmlxt_estep_constructor_args():
    sig = inspect.signature(scxmlxt_EStep.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_scxmlxt_estep_has_featureName():
    assert hasattr(scxmlxt_EStep, "featureName")
    descriptor = None
    for klass in scxmlxt_EStep.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_epath_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_EPath)


def test_scxmlxt_epath_constructor_exists():
    assert callable(scxmlxt_EPath.__init__)


def test_scxmlxt_epath_constructor_args():
    sig = inspect.signature(scxmlxt_EPath.__init__)
    params = list(sig.parameters.keys())



def test_typed_is_not_abstract():
    assert not inspect.isabstract(Typed)


def test_typed_constructor_exists():
    assert callable(Typed.__init__)


def test_typed_constructor_args():
    sig = inspect.signature(Typed.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_eclassifier_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_EClassifier)


def test_scxmlxt_eclassifier_constructor_exists():
    assert callable(scxmlxt_EClassifier.__init__)


def test_scxmlxt_eclassifier_constructor_args():
    sig = inspect.signature(scxmlxt_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_typed_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_Typed)


def test_scxmlxt_typed_constructor_exists():
    assert callable(scxmlxt_Typed.__init__)


def test_scxmlxt_typed_constructor_args():
    sig = inspect.signature(scxmlxt_Typed.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"

def test_scxmlxt_typed_has_many():
    assert hasattr(scxmlxt_Typed, "many")
    descriptor = None
    for klass in scxmlxt_Typed.__mro__:
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



def test_scxmlxt_assignmentaction_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_AssignmentAction)


def test_scxmlxt_assignmentaction_constructor_exists():
    assert callable(scxmlxt_AssignmentAction.__init__)


def test_scxmlxt_assignmentaction_constructor_args():
    sig = inspect.signature(scxmlxt_AssignmentAction.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_scriptaction_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_ScriptAction)


def test_scxmlxt_scriptaction_constructor_exists():
    assert callable(scxmlxt_ScriptAction.__init__)


def test_scxmlxt_scriptaction_constructor_args():
    sig = inspect.signature(scxmlxt_ScriptAction.__init__)
    params = list(sig.parameters.keys())
    assert "script" in params, "Missing parameter 'script'"

def test_scxmlxt_scriptaction_has_script():
    assert hasattr(scxmlxt_ScriptAction, "script")
    descriptor = None
    for klass in scxmlxt_ScriptAction.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_symbolicaction_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_SymbolicAction)


def test_scxmlxt_symbolicaction_constructor_exists():
    assert callable(scxmlxt_SymbolicAction.__init__)


def test_scxmlxt_symbolicaction_constructor_args():
    sig = inspect.signature(scxmlxt_SymbolicAction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_scxmlxt_symbolicaction_has_name():
    assert hasattr(scxmlxt_SymbolicAction, "name")
    descriptor = None
    for klass in scxmlxt_SymbolicAction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_expression_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_Expression)


def test_scxmlxt_expression_constructor_exists():
    assert callable(scxmlxt_Expression.__init__)


def test_scxmlxt_expression_constructor_args():
    sig = inspect.signature(scxmlxt_Expression.__init__)
    params = list(sig.parameters.keys())



def test_abstracttransitionevent_is_not_abstract():
    assert not inspect.isabstract(AbstractTransitionEvent)


def test_abstracttransitionevent_constructor_exists():
    assert callable(AbstractTransitionEvent.__init__)


def test_abstracttransitionevent_constructor_args():
    sig = inspect.signature(AbstractTransitionEvent.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_enterevent_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_EnterEvent)


def test_scxmlxt_enterevent_constructor_exists():
    assert callable(scxmlxt_EnterEvent.__init__)


def test_scxmlxt_enterevent_constructor_args():
    sig = inspect.signature(scxmlxt_EnterEvent.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_exitevent_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_ExitEvent)


def test_scxmlxt_exitevent_constructor_exists():
    assert callable(scxmlxt_ExitEvent.__init__)


def test_scxmlxt_exitevent_constructor_args():
    sig = inspect.signature(scxmlxt_ExitEvent.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_transitionevent_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_TransitionEvent)


def test_scxmlxt_transitionevent_constructor_exists():
    assert callable(scxmlxt_TransitionEvent.__init__)


def test_scxmlxt_transitionevent_constructor_args():
    sig = inspect.signature(scxmlxt_TransitionEvent.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_timerevent_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_TimerEvent)


def test_scxmlxt_timerevent_constructor_exists():
    assert callable(scxmlxt_TimerEvent.__init__)


def test_scxmlxt_timerevent_constructor_args():
    sig = inspect.signature(scxmlxt_TimerEvent.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_scriptevent_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_ScriptEvent)


def test_scxmlxt_scriptevent_constructor_exists():
    assert callable(scxmlxt_ScriptEvent.__init__)


def test_scxmlxt_scriptevent_constructor_args():
    sig = inspect.signature(scxmlxt_ScriptEvent.__init__)
    params = list(sig.parameters.keys())
    assert "script" in params, "Missing parameter 'script'"

def test_scxmlxt_scriptevent_has_script():
    assert hasattr(scxmlxt_ScriptEvent, "script")
    descriptor = None
    for klass in scxmlxt_ScriptEvent.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_abstracttransitionevent_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_AbstractTransitionEvent)


def test_scxmlxt_abstracttransitionevent_constructor_exists():
    assert callable(scxmlxt_AbstractTransitionEvent.__init__)


def test_scxmlxt_abstracttransitionevent_constructor_args():
    sig = inspect.signature(scxmlxt_AbstractTransitionEvent.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_symbolicevent_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_SymbolicEvent)


def test_scxmlxt_symbolicevent_constructor_exists():
    assert callable(scxmlxt_SymbolicEvent.__init__)


def test_scxmlxt_symbolicevent_constructor_args():
    sig = inspect.signature(scxmlxt_SymbolicEvent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_scxmlxt_symbolicevent_has_name():
    assert hasattr(scxmlxt_SymbolicEvent, "name")
    descriptor = None
    for klass in scxmlxt_SymbolicEvent.__mro__:
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



def test_scxmlxt_internaltransition_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_InternalTransition)


def test_scxmlxt_internaltransition_constructor_exists():
    assert callable(scxmlxt_InternalTransition.__init__)


def test_scxmlxt_internaltransition_constructor_args():
    sig = inspect.signature(scxmlxt_InternalTransition.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_transition_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_Transition)


def test_scxmlxt_transition_constructor_exists():
    assert callable(scxmlxt_Transition.__init__)


def test_scxmlxt_transition_constructor_args():
    sig = inspect.signature(scxmlxt_Transition.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_condition_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_Condition)


def test_scxmlxt_condition_constructor_exists():
    assert callable(scxmlxt_Condition.__init__)


def test_scxmlxt_condition_constructor_args():
    sig = inspect.signature(scxmlxt_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "script" in params, "Missing parameter 'script'"

def test_scxmlxt_condition_has_script():
    assert hasattr(scxmlxt_Condition, "script")
    descriptor = None
    for klass in scxmlxt_Condition.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_event_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_Event)


def test_scxmlxt_event_constructor_exists():
    assert callable(scxmlxt_Event.__init__)


def test_scxmlxt_event_constructor_args():
    sig = inspect.signature(scxmlxt_Event.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_vardef_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_VarDef)


def test_scxmlxt_vardef_constructor_exists():
    assert callable(scxmlxt_VarDef.__init__)


def test_scxmlxt_vardef_constructor_args():
    sig = inspect.signature(scxmlxt_VarDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_scxmlxt_vardef_has_name():
    assert hasattr(scxmlxt_VarDef, "name")
    descriptor = None
    for klass in scxmlxt_VarDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_abstracttransition_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_AbstractTransition)


def test_scxmlxt_abstracttransition_constructor_exists():
    assert callable(scxmlxt_AbstractTransition.__init__)


def test_scxmlxt_abstracttransition_constructor_args():
    sig = inspect.signature(scxmlxt_AbstractTransition.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_abstractstate_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_AbstractState)


def test_scxmlxt_abstractstate_constructor_exists():
    assert callable(scxmlxt_AbstractState.__init__)


def test_scxmlxt_abstractstate_constructor_args():
    sig = inspect.signature(scxmlxt_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_action_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_Action)


def test_scxmlxt_action_constructor_exists():
    assert callable(scxmlxt_Action.__init__)


def test_scxmlxt_action_constructor_args():
    sig = inspect.signature(scxmlxt_Action.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_initialtransition_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_InitialTransition)


def test_scxmlxt_initialtransition_constructor_exists():
    assert callable(scxmlxt_InitialTransition.__init__)


def test_scxmlxt_initialtransition_constructor_args():
    sig = inspect.signature(scxmlxt_InitialTransition.__init__)
    params = list(sig.parameters.keys())



def test_scxmlxt_resourceimport_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_ResourceImport)


def test_scxmlxt_resourceimport_constructor_exists():
    assert callable(scxmlxt_ResourceImport.__init__)


def test_scxmlxt_resourceimport_constructor_args():
    sig = inspect.signature(scxmlxt_ResourceImport.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_scxmlxt_resourceimport_has_importURI():
    assert hasattr(scxmlxt_ResourceImport, "importURI")
    descriptor = None
    for klass in scxmlxt_ResourceImport.__mro__:
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



def test_scxmlxt_state_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_State)


def test_scxmlxt_state_constructor_exists():
    assert callable(scxmlxt_State.__init__)


def test_scxmlxt_state_constructor_args():
    sig = inspect.signature(scxmlxt_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_scxmlxt_state_has_name():
    assert hasattr(scxmlxt_State, "name")
    descriptor = None
    for klass in scxmlxt_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_scxmlxt_statemachine_is_not_abstract():
    assert not inspect.isabstract(scxmlxt_StateMachine)


def test_scxmlxt_statemachine_constructor_exists():
    assert callable(scxmlxt_StateMachine.__init__)


def test_scxmlxt_statemachine_constructor_args():
    sig = inspect.signature(scxmlxt_StateMachine.__init__)
    params = list(sig.parameters.keys())

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "ms",
        "m",
        "s",
        "h",
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
scxmlxt_DomainDataImport_strategy = st.builds(
    scxmlxt_DomainDataImport,
)
scxmlxt_DomainModelImport_strategy = st.builds(
    scxmlxt_DomainModelImport,
)
IntLiteral_strategy = st.builds(
    IntLiteral,
)
scxmlxt_DelayLiteral_strategy = st.builds(
    scxmlxt_DelayLiteral,
    timeUnit=
        safe_text
)
scxmlxt_EObject_strategy = st.builds(
    scxmlxt_EObject,
)
scxmlxt_EObjectReference_strategy = st.builds(
    scxmlxt_EObjectReference,
)
ResourceUriLiteral_strategy = st.builds(
    ResourceUriLiteral,
)
scxmlxt_EObjectUriLiteral_strategy = st.builds(
    scxmlxt_EObjectUriLiteral,
    uriFragment=
        safe_text
)
AbstractUriLiteral_strategy = st.builds(
    AbstractUriLiteral,
)
scxmlxt_ResourceUriLiteral_strategy = st.builds(
    scxmlxt_ResourceUriLiteral,
    resourceUri=
        safe_text
)
scxmlxt_UriLiteral_strategy = st.builds(
    scxmlxt_UriLiteral,
    uriValue=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
scxmlxt_VarRef_strategy = st.builds(
    scxmlxt_VarRef,
)
Literal_strategy = st.builds(
    Literal,
)
scxmlxt_StringLiteral_strategy = st.builds(
    scxmlxt_StringLiteral,
    stringValue=
        safe_text
)
scxmlxt_IntLiteral_strategy = st.builds(
    scxmlxt_IntLiteral,
    intValue=
        st.integers()
)
scxmlxt_AbstractUriLiteral_strategy = st.builds(
    scxmlxt_AbstractUriLiteral,
    uri=
        safe_text
)
scxmlxt_FloatLiteral_strategy = st.builds(
    scxmlxt_FloatLiteral,
    floatValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
scxmlxt_BooleanLiteral_strategy = st.builds(
    scxmlxt_BooleanLiteral,
    booleanValue=
        st.booleans()
)
scxmlxt_Literal_strategy = st.builds(
    scxmlxt_Literal,
)
scxmlxt_ScriptExpression_strategy = st.builds(
    scxmlxt_ScriptExpression,
    script=
        safe_text
)
scxmlxt_EStepFilter_strategy = st.builds(
    scxmlxt_EStepFilter,
    freeVarName=
        safe_text
)
scxmlxt_EStep_strategy = st.builds(
    scxmlxt_EStep,
    featureName=
        safe_text
)
scxmlxt_EPath_strategy = st.builds(
    scxmlxt_EPath,
)
Typed_strategy = st.builds(
    Typed,
)
scxmlxt_EClassifier_strategy = st.builds(
    scxmlxt_EClassifier,
)
scxmlxt_Typed_strategy = st.builds(
    scxmlxt_Typed,
    many=
        st.booleans()
)
Action_strategy = st.builds(
    Action,
)
scxmlxt_AssignmentAction_strategy = st.builds(
    scxmlxt_AssignmentAction,
)
scxmlxt_ScriptAction_strategy = st.builds(
    scxmlxt_ScriptAction,
    script=
        safe_text
)
scxmlxt_SymbolicAction_strategy = st.builds(
    scxmlxt_SymbolicAction,
    name=
        safe_text
)
scxmlxt_Expression_strategy = st.builds(
    scxmlxt_Expression,
)
AbstractTransitionEvent_strategy = st.builds(
    AbstractTransitionEvent,
)
scxmlxt_EnterEvent_strategy = st.builds(
    scxmlxt_EnterEvent,
)
scxmlxt_ExitEvent_strategy = st.builds(
    scxmlxt_ExitEvent,
)
scxmlxt_TransitionEvent_strategy = st.builds(
    scxmlxt_TransitionEvent,
)
Event_strategy = st.builds(
    Event,
)
scxmlxt_TimerEvent_strategy = st.builds(
    scxmlxt_TimerEvent,
)
scxmlxt_ScriptEvent_strategy = st.builds(
    scxmlxt_ScriptEvent,
    script=
        safe_text
)
scxmlxt_AbstractTransitionEvent_strategy = st.builds(
    scxmlxt_AbstractTransitionEvent,
)
scxmlxt_SymbolicEvent_strategy = st.builds(
    scxmlxt_SymbolicEvent,
    name=
        safe_text
)
AbstractTransition_strategy = st.builds(
    AbstractTransition,
)
scxmlxt_InternalTransition_strategy = st.builds(
    scxmlxt_InternalTransition,
)
scxmlxt_Transition_strategy = st.builds(
    scxmlxt_Transition,
)
scxmlxt_Condition_strategy = st.builds(
    scxmlxt_Condition,
    script=
        safe_text
)
scxmlxt_Event_strategy = st.builds(
    scxmlxt_Event,
)
scxmlxt_VarDef_strategy = st.builds(
    scxmlxt_VarDef,
    name=
        safe_text
)
scxmlxt_AbstractTransition_strategy = st.builds(
    scxmlxt_AbstractTransition,
)
scxmlxt_AbstractState_strategy = st.builds(
    scxmlxt_AbstractState,
)
scxmlxt_Action_strategy = st.builds(
    scxmlxt_Action,
)
scxmlxt_InitialTransition_strategy = st.builds(
    scxmlxt_InitialTransition,
)
scxmlxt_ResourceImport_strategy = st.builds(
    scxmlxt_ResourceImport,
    importURI=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
scxmlxt_State_strategy = st.builds(
    scxmlxt_State,
    name=
        safe_text
)
scxmlxt_StateMachine_strategy = st.builds(
    scxmlxt_StateMachine,
)

@given(instance=ResourceImport_strategy)
@settings(max_examples=50)
def test_resourceimport_instantiation(instance):
    assert isinstance(instance, ResourceImport)

@given(instance=scxmlxt_DomainDataImport_strategy)
@settings(max_examples=50)
def test_scxmlxt_domaindataimport_instantiation(instance):
    assert isinstance(instance, scxmlxt_DomainDataImport)

@given(instance=scxmlxt_DomainModelImport_strategy)
@settings(max_examples=50)
def test_scxmlxt_domainmodelimport_instantiation(instance):
    assert isinstance(instance, scxmlxt_DomainModelImport)

@given(instance=IntLiteral_strategy)
@settings(max_examples=50)
def test_intliteral_instantiation(instance):
    assert isinstance(instance, IntLiteral)

@given(instance=scxmlxt_DelayLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt_delayliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt_DelayLiteral)



@given(instance=scxmlxt_DelayLiteral_strategy)
def test_scxmlxt_delayliteral_timeUnit_setter(instance):
    original = instance.timeUnit
    instance.timeUnit = original
    assert instance.timeUnit == original

@given(instance=scxmlxt_EObject_strategy)
@settings(max_examples=50)
def test_scxmlxt_eobject_instantiation(instance):
    assert isinstance(instance, scxmlxt_EObject)

@given(instance=scxmlxt_EObjectReference_strategy)
@settings(max_examples=50)
def test_scxmlxt_eobjectreference_instantiation(instance):
    assert isinstance(instance, scxmlxt_EObjectReference)

@given(instance=ResourceUriLiteral_strategy)
@settings(max_examples=50)
def test_resourceuriliteral_instantiation(instance):
    assert isinstance(instance, ResourceUriLiteral)

@given(instance=scxmlxt_EObjectUriLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt_eobjecturiliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt_EObjectUriLiteral)



@given(instance=scxmlxt_EObjectUriLiteral_strategy)
def test_scxmlxt_eobjecturiliteral_uriFragment_setter(instance):
    original = instance.uriFragment
    instance.uriFragment = original
    assert instance.uriFragment == original

@given(instance=AbstractUriLiteral_strategy)
@settings(max_examples=50)
def test_abstracturiliteral_instantiation(instance):
    assert isinstance(instance, AbstractUriLiteral)

@given(instance=scxmlxt_ResourceUriLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt_resourceuriliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt_ResourceUriLiteral)



@given(instance=scxmlxt_ResourceUriLiteral_strategy)
def test_scxmlxt_resourceuriliteral_resourceUri_setter(instance):
    original = instance.resourceUri
    instance.resourceUri = original
    assert instance.resourceUri == original

@given(instance=scxmlxt_UriLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt_uriliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt_UriLiteral)



@given(instance=scxmlxt_UriLiteral_strategy)
def test_scxmlxt_uriliteral_uriValue_setter(instance):
    original = instance.uriValue
    instance.uriValue = original
    assert instance.uriValue == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=scxmlxt_VarRef_strategy)
@settings(max_examples=50)
def test_scxmlxt_varref_instantiation(instance):
    assert isinstance(instance, scxmlxt_VarRef)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=scxmlxt_StringLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt_stringliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt_StringLiteral)



@given(instance=scxmlxt_StringLiteral_strategy)
def test_scxmlxt_stringliteral_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=scxmlxt_IntLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt_intliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt_IntLiteral)



@given(instance=scxmlxt_IntLiteral_strategy)
def test_scxmlxt_intliteral_intValue_setter(instance):
    original = instance.intValue
    instance.intValue = original
    assert instance.intValue == original

@given(instance=scxmlxt_AbstractUriLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt_abstracturiliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt_AbstractUriLiteral)



@given(instance=scxmlxt_AbstractUriLiteral_strategy)
def test_scxmlxt_abstracturiliteral_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=scxmlxt_FloatLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt_floatliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt_FloatLiteral)



@given(instance=scxmlxt_FloatLiteral_strategy)
def test_scxmlxt_floatliteral_floatValue_setter(instance):
    original = instance.floatValue
    instance.floatValue = original
    assert instance.floatValue == original

@given(instance=scxmlxt_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_scxmlxt_booleanliteral_instantiation(instance):
    assert isinstance(instance, scxmlxt_BooleanLiteral)



@given(instance=scxmlxt_BooleanLiteral_strategy)
def test_scxmlxt_booleanliteral_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=scxmlxt_Literal_strategy)
@settings(max_examples=50)
def test_scxmlxt_literal_instantiation(instance):
    assert isinstance(instance, scxmlxt_Literal)

@given(instance=scxmlxt_ScriptExpression_strategy)
@settings(max_examples=50)
def test_scxmlxt_scriptexpression_instantiation(instance):
    assert isinstance(instance, scxmlxt_ScriptExpression)



@given(instance=scxmlxt_ScriptExpression_strategy)
def test_scxmlxt_scriptexpression_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original

@given(instance=scxmlxt_EStepFilter_strategy)
@settings(max_examples=50)
def test_scxmlxt_estepfilter_instantiation(instance):
    assert isinstance(instance, scxmlxt_EStepFilter)



@given(instance=scxmlxt_EStepFilter_strategy)
def test_scxmlxt_estepfilter_freeVarName_setter(instance):
    original = instance.freeVarName
    instance.freeVarName = original
    assert instance.freeVarName == original

@given(instance=scxmlxt_EStep_strategy)
@settings(max_examples=50)
def test_scxmlxt_estep_instantiation(instance):
    assert isinstance(instance, scxmlxt_EStep)



@given(instance=scxmlxt_EStep_strategy)
def test_scxmlxt_estep_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=scxmlxt_EPath_strategy)
@settings(max_examples=50)
def test_scxmlxt_epath_instantiation(instance):
    assert isinstance(instance, scxmlxt_EPath)

@given(instance=Typed_strategy)
@settings(max_examples=50)
def test_typed_instantiation(instance):
    assert isinstance(instance, Typed)

@given(instance=scxmlxt_EClassifier_strategy)
@settings(max_examples=50)
def test_scxmlxt_eclassifier_instantiation(instance):
    assert isinstance(instance, scxmlxt_EClassifier)

@given(instance=scxmlxt_Typed_strategy)
@settings(max_examples=50)
def test_scxmlxt_typed_instantiation(instance):
    assert isinstance(instance, scxmlxt_Typed)



@given(instance=scxmlxt_Typed_strategy)
def test_scxmlxt_typed_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=scxmlxt_AssignmentAction_strategy)
@settings(max_examples=50)
def test_scxmlxt_assignmentaction_instantiation(instance):
    assert isinstance(instance, scxmlxt_AssignmentAction)

@given(instance=scxmlxt_ScriptAction_strategy)
@settings(max_examples=50)
def test_scxmlxt_scriptaction_instantiation(instance):
    assert isinstance(instance, scxmlxt_ScriptAction)



@given(instance=scxmlxt_ScriptAction_strategy)
def test_scxmlxt_scriptaction_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original

@given(instance=scxmlxt_SymbolicAction_strategy)
@settings(max_examples=50)
def test_scxmlxt_symbolicaction_instantiation(instance):
    assert isinstance(instance, scxmlxt_SymbolicAction)



@given(instance=scxmlxt_SymbolicAction_strategy)
def test_scxmlxt_symbolicaction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scxmlxt_Expression_strategy)
@settings(max_examples=50)
def test_scxmlxt_expression_instantiation(instance):
    assert isinstance(instance, scxmlxt_Expression)

@given(instance=AbstractTransitionEvent_strategy)
@settings(max_examples=50)
def test_abstracttransitionevent_instantiation(instance):
    assert isinstance(instance, AbstractTransitionEvent)

@given(instance=scxmlxt_EnterEvent_strategy)
@settings(max_examples=50)
def test_scxmlxt_enterevent_instantiation(instance):
    assert isinstance(instance, scxmlxt_EnterEvent)

@given(instance=scxmlxt_ExitEvent_strategy)
@settings(max_examples=50)
def test_scxmlxt_exitevent_instantiation(instance):
    assert isinstance(instance, scxmlxt_ExitEvent)

@given(instance=scxmlxt_TransitionEvent_strategy)
@settings(max_examples=50)
def test_scxmlxt_transitionevent_instantiation(instance):
    assert isinstance(instance, scxmlxt_TransitionEvent)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=scxmlxt_TimerEvent_strategy)
@settings(max_examples=50)
def test_scxmlxt_timerevent_instantiation(instance):
    assert isinstance(instance, scxmlxt_TimerEvent)

@given(instance=scxmlxt_ScriptEvent_strategy)
@settings(max_examples=50)
def test_scxmlxt_scriptevent_instantiation(instance):
    assert isinstance(instance, scxmlxt_ScriptEvent)



@given(instance=scxmlxt_ScriptEvent_strategy)
def test_scxmlxt_scriptevent_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original

@given(instance=scxmlxt_AbstractTransitionEvent_strategy)
@settings(max_examples=50)
def test_scxmlxt_abstracttransitionevent_instantiation(instance):
    assert isinstance(instance, scxmlxt_AbstractTransitionEvent)

@given(instance=scxmlxt_SymbolicEvent_strategy)
@settings(max_examples=50)
def test_scxmlxt_symbolicevent_instantiation(instance):
    assert isinstance(instance, scxmlxt_SymbolicEvent)



@given(instance=scxmlxt_SymbolicEvent_strategy)
def test_scxmlxt_symbolicevent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractTransition_strategy)
@settings(max_examples=50)
def test_abstracttransition_instantiation(instance):
    assert isinstance(instance, AbstractTransition)

@given(instance=scxmlxt_InternalTransition_strategy)
@settings(max_examples=50)
def test_scxmlxt_internaltransition_instantiation(instance):
    assert isinstance(instance, scxmlxt_InternalTransition)

@given(instance=scxmlxt_Transition_strategy)
@settings(max_examples=50)
def test_scxmlxt_transition_instantiation(instance):
    assert isinstance(instance, scxmlxt_Transition)

@given(instance=scxmlxt_Condition_strategy)
@settings(max_examples=50)
def test_scxmlxt_condition_instantiation(instance):
    assert isinstance(instance, scxmlxt_Condition)



@given(instance=scxmlxt_Condition_strategy)
def test_scxmlxt_condition_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original

@given(instance=scxmlxt_Event_strategy)
@settings(max_examples=50)
def test_scxmlxt_event_instantiation(instance):
    assert isinstance(instance, scxmlxt_Event)

@given(instance=scxmlxt_VarDef_strategy)
@settings(max_examples=50)
def test_scxmlxt_vardef_instantiation(instance):
    assert isinstance(instance, scxmlxt_VarDef)



@given(instance=scxmlxt_VarDef_strategy)
def test_scxmlxt_vardef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scxmlxt_AbstractTransition_strategy)
@settings(max_examples=50)
def test_scxmlxt_abstracttransition_instantiation(instance):
    assert isinstance(instance, scxmlxt_AbstractTransition)

@given(instance=scxmlxt_AbstractState_strategy)
@settings(max_examples=50)
def test_scxmlxt_abstractstate_instantiation(instance):
    assert isinstance(instance, scxmlxt_AbstractState)

@given(instance=scxmlxt_Action_strategy)
@settings(max_examples=50)
def test_scxmlxt_action_instantiation(instance):
    assert isinstance(instance, scxmlxt_Action)

@given(instance=scxmlxt_InitialTransition_strategy)
@settings(max_examples=50)
def test_scxmlxt_initialtransition_instantiation(instance):
    assert isinstance(instance, scxmlxt_InitialTransition)

@given(instance=scxmlxt_ResourceImport_strategy)
@settings(max_examples=50)
def test_scxmlxt_resourceimport_instantiation(instance):
    assert isinstance(instance, scxmlxt_ResourceImport)



@given(instance=scxmlxt_ResourceImport_strategy)
def test_scxmlxt_resourceimport_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=scxmlxt_State_strategy)
@settings(max_examples=50)
def test_scxmlxt_state_instantiation(instance):
    assert isinstance(instance, scxmlxt_State)



@given(instance=scxmlxt_State_strategy)
def test_scxmlxt_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scxmlxt_StateMachine_strategy)
@settings(max_examples=50)
def test_scxmlxt_statemachine_instantiation(instance):
    assert isinstance(instance, scxmlxt_StateMachine)
