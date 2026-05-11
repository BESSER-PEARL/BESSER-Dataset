import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    scxml::Description,
    IAdaptable,
    scxml::DescriptionContainer,
    scxml::DatamodelContainer,
    scxml::EClass,
    scxml::IAdaptable,
    Data,
    scxml::XData,
    scxml::XObject,
    scxml::Else,
    Conditional,
    scxml::ElseIf,
    scxml::Conditional,
    scxml::Validate,
    scxml::Assign,
    scxml::Cancel,
    Donedata,
    scxml::Send,
    scxml::ExecutableContent,
    InitialState,
    scxml::Invoke,
    scxml::AbstractSimpleState,
    State,
    scxml::Raise,
    scxml::Log,
    scxml::EObject,
    scxml::Donedata,
    scxml::Param,
    Transition,
    scxml::Content,
    scxml::ParallelState,
    scxml::AbstractState,
    scxml::CondEventTransition,
    Node,
    scxml::TransitionTarget,
    scxml::TransitionSource,
    ExecutableContent,
    scxml::OnEntry,
    scxml::If,
    scxml::OnExit,
    TransitionSource,
    TransitionTarget,
    scxml::FinalState,
    scxml::HistoryState,
    scxml::Script,
    DescriptionContainer,
    scxml::Transition,
    scxml::Data,
    scxml::Node,
    scxml::Datamodel,
    scxml::InitialState,
    DatamodelContainer,
    AbstractSimpleState,
    scxml::SimpleState,
    AbstractState,
    scxml::State,
    scxml::StateChart,
    ExmodeDatatype,
    HistoryTypeDatatype,
    AdapterToken,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scxml::description_is_not_abstract():
    assert not inspect.isabstract(scxml::Description)


def test_scxml::description_constructor_exists():
    assert callable(scxml::Description.__init__)


def test_scxml::description_constructor_args():
    sig = inspect.signature(scxml::Description.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_scxml::description_has_value():
    assert hasattr(scxml::Description, "value")
    descriptor = None
    for klass in scxml::Description.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iadaptable_is_not_abstract():
    assert not inspect.isabstract(IAdaptable)


def test_iadaptable_constructor_exists():
    assert callable(IAdaptable.__init__)


def test_iadaptable_constructor_args():
    sig = inspect.signature(IAdaptable.__init__)
    params = list(sig.parameters.keys())



def test_scxml::descriptioncontainer_is_not_abstract():
    assert not inspect.isabstract(scxml::DescriptionContainer)


def test_scxml::descriptioncontainer_constructor_exists():
    assert callable(scxml::DescriptionContainer.__init__)


def test_scxml::descriptioncontainer_constructor_args():
    sig = inspect.signature(scxml::DescriptionContainer.__init__)
    params = list(sig.parameters.keys())



def test_scxml::datamodelcontainer_is_not_abstract():
    assert not inspect.isabstract(scxml::DatamodelContainer)


def test_scxml::datamodelcontainer_constructor_exists():
    assert callable(scxml::DatamodelContainer.__init__)


def test_scxml::datamodelcontainer_constructor_args():
    sig = inspect.signature(scxml::DatamodelContainer.__init__)
    params = list(sig.parameters.keys())



def test_scxml::eclass_is_not_abstract():
    assert not inspect.isabstract(scxml::EClass)


def test_scxml::eclass_constructor_exists():
    assert callable(scxml::EClass.__init__)


def test_scxml::eclass_constructor_args():
    sig = inspect.signature(scxml::EClass.__init__)
    params = list(sig.parameters.keys())



def test_scxml::iadaptable_is_not_abstract():
    assert not inspect.isabstract(scxml::IAdaptable)


def test_scxml::iadaptable_constructor_exists():
    assert callable(scxml::IAdaptable.__init__)


def test_scxml::iadaptable_constructor_args():
    sig = inspect.signature(scxml::IAdaptable.__init__)
    params = list(sig.parameters.keys())



def test_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_data_constructor_exists():
    assert callable(Data.__init__)


def test_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_scxml::xdata_is_not_abstract():
    assert not inspect.isabstract(scxml::XData)


def test_scxml::xdata_constructor_exists():
    assert callable(scxml::XData.__init__)


def test_scxml::xdata_constructor_args():
    sig = inspect.signature(scxml::XData.__init__)
    params = list(sig.parameters.keys())



def test_scxml::xobject_is_not_abstract():
    assert not inspect.isabstract(scxml::XObject)


def test_scxml::xobject_constructor_exists():
    assert callable(scxml::XObject.__init__)


def test_scxml::xobject_constructor_args():
    sig = inspect.signature(scxml::XObject.__init__)
    params = list(sig.parameters.keys())
    assert "exchange" in params, "Missing parameter 'exchange'"
    assert "classifierName" in params, "Missing parameter 'classifierName'"
    assert "nsUri" in params, "Missing parameter 'nsUri'"

def test_scxml::xobject_has_exchange():
    assert hasattr(scxml::XObject, "exchange")
    descriptor = None
    for klass in scxml::XObject.__mro__:
        if "exchange" in klass.__dict__:
            descriptor = klass.__dict__["exchange"]
            break
    assert isinstance(descriptor, property)

def test_scxml::xobject_has_classifierName():
    assert hasattr(scxml::XObject, "classifierName")
    descriptor = None
    for klass in scxml::XObject.__mro__:
        if "classifierName" in klass.__dict__:
            descriptor = klass.__dict__["classifierName"]
            break
    assert isinstance(descriptor, property)

def test_scxml::xobject_has_nsUri():
    assert hasattr(scxml::XObject, "nsUri")
    descriptor = None
    for klass in scxml::XObject.__mro__:
        if "nsUri" in klass.__dict__:
            descriptor = klass.__dict__["nsUri"]
            break
    assert isinstance(descriptor, property)



def test_scxml::else_is_not_abstract():
    assert not inspect.isabstract(scxml::Else)


def test_scxml::else_constructor_exists():
    assert callable(scxml::Else.__init__)


def test_scxml::else_constructor_args():
    sig = inspect.signature(scxml::Else.__init__)
    params = list(sig.parameters.keys())



def test_conditional_is_not_abstract():
    assert not inspect.isabstract(Conditional)


def test_conditional_constructor_exists():
    assert callable(Conditional.__init__)


def test_conditional_constructor_args():
    sig = inspect.signature(Conditional.__init__)
    params = list(sig.parameters.keys())



def test_scxml::elseif_is_not_abstract():
    assert not inspect.isabstract(scxml::ElseIf)


def test_scxml::elseif_constructor_exists():
    assert callable(scxml::ElseIf.__init__)


def test_scxml::elseif_constructor_args():
    sig = inspect.signature(scxml::ElseIf.__init__)
    params = list(sig.parameters.keys())



def test_scxml::conditional_is_not_abstract():
    assert not inspect.isabstract(scxml::Conditional)


def test_scxml::conditional_constructor_exists():
    assert callable(scxml::Conditional.__init__)


def test_scxml::conditional_constructor_args():
    sig = inspect.signature(scxml::Conditional.__init__)
    params = list(sig.parameters.keys())
    assert "cond" in params, "Missing parameter 'cond'"

def test_scxml::conditional_has_cond():
    assert hasattr(scxml::Conditional, "cond")
    descriptor = None
    for klass in scxml::Conditional.__mro__:
        if "cond" in klass.__dict__:
            descriptor = klass.__dict__["cond"]
            break
    assert isinstance(descriptor, property)



def test_scxml::validate_is_not_abstract():
    assert not inspect.isabstract(scxml::Validate)


def test_scxml::validate_constructor_exists():
    assert callable(scxml::Validate.__init__)


def test_scxml::validate_constructor_args():
    sig = inspect.signature(scxml::Validate.__init__)
    params = list(sig.parameters.keys())
    assert "schema" in params, "Missing parameter 'schema'"
    assert "location" in params, "Missing parameter 'location'"

def test_scxml::validate_has_schema():
    assert hasattr(scxml::Validate, "schema")
    descriptor = None
    for klass in scxml::Validate.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)

def test_scxml::validate_has_location():
    assert hasattr(scxml::Validate, "location")
    descriptor = None
    for klass in scxml::Validate.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_scxml::assign_is_not_abstract():
    assert not inspect.isabstract(scxml::Assign)


def test_scxml::assign_constructor_exists():
    assert callable(scxml::Assign.__init__)


def test_scxml::assign_constructor_args():
    sig = inspect.signature(scxml::Assign.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "location" in params, "Missing parameter 'location'"
    assert "expr" in params, "Missing parameter 'expr'"

def test_scxml::assign_has_name():
    assert hasattr(scxml::Assign, "name")
    descriptor = None
    for klass in scxml::Assign.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_scxml::assign_has_location():
    assert hasattr(scxml::Assign, "location")
    descriptor = None
    for klass in scxml::Assign.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_scxml::assign_has_expr():
    assert hasattr(scxml::Assign, "expr")
    descriptor = None
    for klass in scxml::Assign.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)



def test_scxml::cancel_is_not_abstract():
    assert not inspect.isabstract(scxml::Cancel)


def test_scxml::cancel_constructor_exists():
    assert callable(scxml::Cancel.__init__)


def test_scxml::cancel_constructor_args():
    sig = inspect.signature(scxml::Cancel.__init__)
    params = list(sig.parameters.keys())
    assert "sendid" in params, "Missing parameter 'sendid'"
    assert "sendidexpr" in params, "Missing parameter 'sendidexpr'"

def test_scxml::cancel_has_sendid():
    assert hasattr(scxml::Cancel, "sendid")
    descriptor = None
    for klass in scxml::Cancel.__mro__:
        if "sendid" in klass.__dict__:
            descriptor = klass.__dict__["sendid"]
            break
    assert isinstance(descriptor, property)

def test_scxml::cancel_has_sendidexpr():
    assert hasattr(scxml::Cancel, "sendidexpr")
    descriptor = None
    for klass in scxml::Cancel.__mro__:
        if "sendidexpr" in klass.__dict__:
            descriptor = klass.__dict__["sendidexpr"]
            break
    assert isinstance(descriptor, property)



def test_donedata_is_not_abstract():
    assert not inspect.isabstract(Donedata)


def test_donedata_constructor_exists():
    assert callable(Donedata.__init__)


def test_donedata_constructor_args():
    sig = inspect.signature(Donedata.__init__)
    params = list(sig.parameters.keys())



def test_scxml::send_is_not_abstract():
    assert not inspect.isabstract(scxml::Send)


def test_scxml::send_constructor_exists():
    assert callable(scxml::Send.__init__)


def test_scxml::send_constructor_args():
    sig = inspect.signature(scxml::Send.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "delay" in params, "Missing parameter 'delay'"
    assert "targetexpr" in params, "Missing parameter 'targetexpr'"
    assert "id" in params, "Missing parameter 'id'"
    assert "namelist" in params, "Missing parameter 'namelist'"
    assert "hintsexpr" in params, "Missing parameter 'hintsexpr'"
    assert "target" in params, "Missing parameter 'target'"
    assert "idlocation" in params, "Missing parameter 'idlocation'"
    assert "delayexpr" in params, "Missing parameter 'delayexpr'"
    assert "typeexpr" in params, "Missing parameter 'typeexpr'"
    assert "eventexpr" in params, "Missing parameter 'eventexpr'"
    assert "hints" in params, "Missing parameter 'hints'"
    assert "event" in params, "Missing parameter 'event'"

def test_scxml::send_has_type():
    assert hasattr(scxml::Send, "type")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scxml::send_has_delay():
    assert hasattr(scxml::Send, "delay")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)

def test_scxml::send_has_targetexpr():
    assert hasattr(scxml::Send, "targetexpr")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "targetexpr" in klass.__dict__:
            descriptor = klass.__dict__["targetexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::send_has_id():
    assert hasattr(scxml::Send, "id")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml::send_has_namelist():
    assert hasattr(scxml::Send, "namelist")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "namelist" in klass.__dict__:
            descriptor = klass.__dict__["namelist"]
            break
    assert isinstance(descriptor, property)

def test_scxml::send_has_hintsexpr():
    assert hasattr(scxml::Send, "hintsexpr")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "hintsexpr" in klass.__dict__:
            descriptor = klass.__dict__["hintsexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::send_has_target():
    assert hasattr(scxml::Send, "target")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_scxml::send_has_idlocation():
    assert hasattr(scxml::Send, "idlocation")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "idlocation" in klass.__dict__:
            descriptor = klass.__dict__["idlocation"]
            break
    assert isinstance(descriptor, property)

def test_scxml::send_has_delayexpr():
    assert hasattr(scxml::Send, "delayexpr")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "delayexpr" in klass.__dict__:
            descriptor = klass.__dict__["delayexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::send_has_typeexpr():
    assert hasattr(scxml::Send, "typeexpr")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "typeexpr" in klass.__dict__:
            descriptor = klass.__dict__["typeexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::send_has_eventexpr():
    assert hasattr(scxml::Send, "eventexpr")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "eventexpr" in klass.__dict__:
            descriptor = klass.__dict__["eventexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::send_has_hints():
    assert hasattr(scxml::Send, "hints")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "hints" in klass.__dict__:
            descriptor = klass.__dict__["hints"]
            break
    assert isinstance(descriptor, property)

def test_scxml::send_has_event():
    assert hasattr(scxml::Send, "event")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_scxml::executablecontent_is_not_abstract():
    assert not inspect.isabstract(scxml::ExecutableContent)


def test_scxml::executablecontent_constructor_exists():
    assert callable(scxml::ExecutableContent.__init__)


def test_scxml::executablecontent_constructor_args():
    sig = inspect.signature(scxml::ExecutableContent.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_scxml::executablecontent_has_group():
    assert hasattr(scxml::ExecutableContent, "group")
    descriptor = None
    for klass in scxml::ExecutableContent.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_initialstate_is_not_abstract():
    assert not inspect.isabstract(InitialState)


def test_initialstate_constructor_exists():
    assert callable(InitialState.__init__)


def test_initialstate_constructor_args():
    sig = inspect.signature(InitialState.__init__)
    params = list(sig.parameters.keys())



def test_scxml::invoke_is_not_abstract():
    assert not inspect.isabstract(scxml::Invoke)


def test_scxml::invoke_constructor_exists():
    assert callable(scxml::Invoke.__init__)


def test_scxml::invoke_constructor_args():
    sig = inspect.signature(scxml::Invoke.__init__)
    params = list(sig.parameters.keys())
    assert "idlocation" in params, "Missing parameter 'idlocation'"
    assert "namelist" in params, "Missing parameter 'namelist'"
    assert "autoforward" in params, "Missing parameter 'autoforward'"
    assert "typeexpr" in params, "Missing parameter 'typeexpr'"
    assert "srcexpr" in params, "Missing parameter 'srcexpr'"
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"
    assert "src" in params, "Missing parameter 'src'"

def test_scxml::invoke_has_idlocation():
    assert hasattr(scxml::Invoke, "idlocation")
    descriptor = None
    for klass in scxml::Invoke.__mro__:
        if "idlocation" in klass.__dict__:
            descriptor = klass.__dict__["idlocation"]
            break
    assert isinstance(descriptor, property)

def test_scxml::invoke_has_namelist():
    assert hasattr(scxml::Invoke, "namelist")
    descriptor = None
    for klass in scxml::Invoke.__mro__:
        if "namelist" in klass.__dict__:
            descriptor = klass.__dict__["namelist"]
            break
    assert isinstance(descriptor, property)

def test_scxml::invoke_has_autoforward():
    assert hasattr(scxml::Invoke, "autoforward")
    descriptor = None
    for klass in scxml::Invoke.__mro__:
        if "autoforward" in klass.__dict__:
            descriptor = klass.__dict__["autoforward"]
            break
    assert isinstance(descriptor, property)

def test_scxml::invoke_has_typeexpr():
    assert hasattr(scxml::Invoke, "typeexpr")
    descriptor = None
    for klass in scxml::Invoke.__mro__:
        if "typeexpr" in klass.__dict__:
            descriptor = klass.__dict__["typeexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::invoke_has_srcexpr():
    assert hasattr(scxml::Invoke, "srcexpr")
    descriptor = None
    for klass in scxml::Invoke.__mro__:
        if "srcexpr" in klass.__dict__:
            descriptor = klass.__dict__["srcexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::invoke_has_type():
    assert hasattr(scxml::Invoke, "type")
    descriptor = None
    for klass in scxml::Invoke.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scxml::invoke_has_id():
    assert hasattr(scxml::Invoke, "id")
    descriptor = None
    for klass in scxml::Invoke.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml::invoke_has_src():
    assert hasattr(scxml::Invoke, "src")
    descriptor = None
    for klass in scxml::Invoke.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)



def test_scxml::abstractsimplestate_is_not_abstract():
    assert not inspect.isabstract(scxml::AbstractSimpleState)


def test_scxml::abstractsimplestate_constructor_exists():
    assert callable(scxml::AbstractSimpleState.__init__)


def test_scxml::abstractsimplestate_constructor_args():
    sig = inspect.signature(scxml::AbstractSimpleState.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_scxml::raise_is_not_abstract():
    assert not inspect.isabstract(scxml::Raise)


def test_scxml::raise_constructor_exists():
    assert callable(scxml::Raise.__init__)


def test_scxml::raise_constructor_args():
    sig = inspect.signature(scxml::Raise.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_scxml::raise_has_event():
    assert hasattr(scxml::Raise, "event")
    descriptor = None
    for klass in scxml::Raise.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_scxml::log_is_not_abstract():
    assert not inspect.isabstract(scxml::Log)


def test_scxml::log_constructor_exists():
    assert callable(scxml::Log.__init__)


def test_scxml::log_constructor_args():
    sig = inspect.signature(scxml::Log.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "label" in params, "Missing parameter 'label'"
    assert "expr" in params, "Missing parameter 'expr'"

def test_scxml::log_has_level():
    assert hasattr(scxml::Log, "level")
    descriptor = None
    for klass in scxml::Log.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_scxml::log_has_label():
    assert hasattr(scxml::Log, "label")
    descriptor = None
    for klass in scxml::Log.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_scxml::log_has_expr():
    assert hasattr(scxml::Log, "expr")
    descriptor = None
    for klass in scxml::Log.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)



def test_scxml::eobject_is_not_abstract():
    assert not inspect.isabstract(scxml::EObject)


def test_scxml::eobject_constructor_exists():
    assert callable(scxml::EObject.__init__)


def test_scxml::eobject_constructor_args():
    sig = inspect.signature(scxml::EObject.__init__)
    params = list(sig.parameters.keys())



def test_scxml::donedata_is_not_abstract():
    assert not inspect.isabstract(scxml::Donedata)


def test_scxml::donedata_constructor_exists():
    assert callable(scxml::Donedata.__init__)


def test_scxml::donedata_constructor_args():
    sig = inspect.signature(scxml::Donedata.__init__)
    params = list(sig.parameters.keys())



def test_scxml::param_is_not_abstract():
    assert not inspect.isabstract(scxml::Param)


def test_scxml::param_constructor_exists():
    assert callable(scxml::Param.__init__)


def test_scxml::param_constructor_args():
    sig = inspect.signature(scxml::Param.__init__)
    params = list(sig.parameters.keys())
    assert "expr" in params, "Missing parameter 'expr'"
    assert "name" in params, "Missing parameter 'name'"

def test_scxml::param_has_expr():
    assert hasattr(scxml::Param, "expr")
    descriptor = None
    for klass in scxml::Param.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::param_has_name():
    assert hasattr(scxml::Param, "name")
    descriptor = None
    for klass in scxml::Param.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_scxml::content_is_not_abstract():
    assert not inspect.isabstract(scxml::Content)


def test_scxml::content_constructor_exists():
    assert callable(scxml::Content.__init__)


def test_scxml::content_constructor_args():
    sig = inspect.signature(scxml::Content.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_scxml::content_has_value():
    assert hasattr(scxml::Content, "value")
    descriptor = None
    for klass in scxml::Content.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_scxml::parallelstate_is_not_abstract():
    assert not inspect.isabstract(scxml::ParallelState)


def test_scxml::parallelstate_constructor_exists():
    assert callable(scxml::ParallelState.__init__)


def test_scxml::parallelstate_constructor_args():
    sig = inspect.signature(scxml::ParallelState.__init__)
    params = list(sig.parameters.keys())



def test_scxml::abstractstate_is_not_abstract():
    assert not inspect.isabstract(scxml::AbstractState)


def test_scxml::abstractstate_constructor_exists():
    assert callable(scxml::AbstractState.__init__)


def test_scxml::abstractstate_constructor_args():
    sig = inspect.signature(scxml::AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_scxml::condeventtransition_is_not_abstract():
    assert not inspect.isabstract(scxml::CondEventTransition)


def test_scxml::condeventtransition_constructor_exists():
    assert callable(scxml::CondEventTransition.__init__)


def test_scxml::condeventtransition_constructor_args():
    sig = inspect.signature(scxml::CondEventTransition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "cond" in params, "Missing parameter 'cond'"

def test_scxml::condeventtransition_has_event():
    assert hasattr(scxml::CondEventTransition, "event")
    descriptor = None
    for klass in scxml::CondEventTransition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_scxml::condeventtransition_has_cond():
    assert hasattr(scxml::CondEventTransition, "cond")
    descriptor = None
    for klass in scxml::CondEventTransition.__mro__:
        if "cond" in klass.__dict__:
            descriptor = klass.__dict__["cond"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_scxml::transitiontarget_is_not_abstract():
    assert not inspect.isabstract(scxml::TransitionTarget)


def test_scxml::transitiontarget_constructor_exists():
    assert callable(scxml::TransitionTarget.__init__)


def test_scxml::transitiontarget_constructor_args():
    sig = inspect.signature(scxml::TransitionTarget.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_scxml::transitiontarget_has_id():
    assert hasattr(scxml::TransitionTarget, "id")
    descriptor = None
    for klass in scxml::TransitionTarget.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_scxml::transitionsource_is_not_abstract():
    assert not inspect.isabstract(scxml::TransitionSource)


def test_scxml::transitionsource_constructor_exists():
    assert callable(scxml::TransitionSource.__init__)


def test_scxml::transitionsource_constructor_args():
    sig = inspect.signature(scxml::TransitionSource.__init__)
    params = list(sig.parameters.keys())



def test_executablecontent_is_not_abstract():
    assert not inspect.isabstract(ExecutableContent)


def test_executablecontent_constructor_exists():
    assert callable(ExecutableContent.__init__)


def test_executablecontent_constructor_args():
    sig = inspect.signature(ExecutableContent.__init__)
    params = list(sig.parameters.keys())



def test_scxml::onentry_is_not_abstract():
    assert not inspect.isabstract(scxml::OnEntry)


def test_scxml::onentry_constructor_exists():
    assert callable(scxml::OnEntry.__init__)


def test_scxml::onentry_constructor_args():
    sig = inspect.signature(scxml::OnEntry.__init__)
    params = list(sig.parameters.keys())



def test_scxml::if_is_not_abstract():
    assert not inspect.isabstract(scxml::If)


def test_scxml::if_constructor_exists():
    assert callable(scxml::If.__init__)


def test_scxml::if_constructor_args():
    sig = inspect.signature(scxml::If.__init__)
    params = list(sig.parameters.keys())



def test_scxml::onexit_is_not_abstract():
    assert not inspect.isabstract(scxml::OnExit)


def test_scxml::onexit_constructor_exists():
    assert callable(scxml::OnExit.__init__)


def test_scxml::onexit_constructor_args():
    sig = inspect.signature(scxml::OnExit.__init__)
    params = list(sig.parameters.keys())



def test_transitionsource_is_not_abstract():
    assert not inspect.isabstract(TransitionSource)


def test_transitionsource_constructor_exists():
    assert callable(TransitionSource.__init__)


def test_transitionsource_constructor_args():
    sig = inspect.signature(TransitionSource.__init__)
    params = list(sig.parameters.keys())



def test_transitiontarget_is_not_abstract():
    assert not inspect.isabstract(TransitionTarget)


def test_transitiontarget_constructor_exists():
    assert callable(TransitionTarget.__init__)


def test_transitiontarget_constructor_args():
    sig = inspect.signature(TransitionTarget.__init__)
    params = list(sig.parameters.keys())



def test_scxml::finalstate_is_not_abstract():
    assert not inspect.isabstract(scxml::FinalState)


def test_scxml::finalstate_constructor_exists():
    assert callable(scxml::FinalState.__init__)


def test_scxml::finalstate_constructor_args():
    sig = inspect.signature(scxml::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_scxml::historystate_is_not_abstract():
    assert not inspect.isabstract(scxml::HistoryState)


def test_scxml::historystate_constructor_exists():
    assert callable(scxml::HistoryState.__init__)


def test_scxml::historystate_constructor_args():
    sig = inspect.signature(scxml::HistoryState.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_scxml::historystate_has_type():
    assert hasattr(scxml::HistoryState, "type")
    descriptor = None
    for klass in scxml::HistoryState.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_scxml::script_is_not_abstract():
    assert not inspect.isabstract(scxml::Script)


def test_scxml::script_constructor_exists():
    assert callable(scxml::Script.__init__)


def test_scxml::script_constructor_args():
    sig = inspect.signature(scxml::Script.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_scxml::script_has_value():
    assert hasattr(scxml::Script, "value")
    descriptor = None
    for klass in scxml::Script.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_descriptioncontainer_is_not_abstract():
    assert not inspect.isabstract(DescriptionContainer)


def test_descriptioncontainer_constructor_exists():
    assert callable(DescriptionContainer.__init__)


def test_descriptioncontainer_constructor_args():
    sig = inspect.signature(DescriptionContainer.__init__)
    params = list(sig.parameters.keys())



def test_scxml::transition_is_not_abstract():
    assert not inspect.isabstract(scxml::Transition)


def test_scxml::transition_constructor_exists():
    assert callable(scxml::Transition.__init__)


def test_scxml::transition_constructor_args():
    sig = inspect.signature(scxml::Transition.__init__)
    params = list(sig.parameters.keys())



def test_scxml::data_is_not_abstract():
    assert not inspect.isabstract(scxml::Data)


def test_scxml::data_constructor_exists():
    assert callable(scxml::Data.__init__)


def test_scxml::data_constructor_args():
    sig = inspect.signature(scxml::Data.__init__)
    params = list(sig.parameters.keys())
    assert "expr" in params, "Missing parameter 'expr'"
    assert "id" in params, "Missing parameter 'id'"
    assert "src" in params, "Missing parameter 'src'"

def test_scxml::data_has_expr():
    assert hasattr(scxml::Data, "expr")
    descriptor = None
    for klass in scxml::Data.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::data_has_id():
    assert hasattr(scxml::Data, "id")
    descriptor = None
    for klass in scxml::Data.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml::data_has_src():
    assert hasattr(scxml::Data, "src")
    descriptor = None
    for klass in scxml::Data.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)



def test_scxml::node_is_not_abstract():
    assert not inspect.isabstract(scxml::Node)


def test_scxml::node_constructor_exists():
    assert callable(scxml::Node.__init__)


def test_scxml::node_constructor_args():
    sig = inspect.signature(scxml::Node.__init__)
    params = list(sig.parameters.keys())



def test_scxml::datamodel_is_not_abstract():
    assert not inspect.isabstract(scxml::Datamodel)


def test_scxml::datamodel_constructor_exists():
    assert callable(scxml::Datamodel.__init__)


def test_scxml::datamodel_constructor_args():
    sig = inspect.signature(scxml::Datamodel.__init__)
    params = list(sig.parameters.keys())
    assert "schema" in params, "Missing parameter 'schema'"

def test_scxml::datamodel_has_schema():
    assert hasattr(scxml::Datamodel, "schema")
    descriptor = None
    for klass in scxml::Datamodel.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)



def test_scxml::initialstate_is_not_abstract():
    assert not inspect.isabstract(scxml::InitialState)


def test_scxml::initialstate_constructor_exists():
    assert callable(scxml::InitialState.__init__)


def test_scxml::initialstate_constructor_args():
    sig = inspect.signature(scxml::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_datamodelcontainer_is_not_abstract():
    assert not inspect.isabstract(DatamodelContainer)


def test_datamodelcontainer_constructor_exists():
    assert callable(DatamodelContainer.__init__)


def test_datamodelcontainer_constructor_args():
    sig = inspect.signature(DatamodelContainer.__init__)
    params = list(sig.parameters.keys())



def test_abstractsimplestate_is_not_abstract():
    assert not inspect.isabstract(AbstractSimpleState)


def test_abstractsimplestate_constructor_exists():
    assert callable(AbstractSimpleState.__init__)


def test_abstractsimplestate_constructor_args():
    sig = inspect.signature(AbstractSimpleState.__init__)
    params = list(sig.parameters.keys())



def test_scxml::simplestate_is_not_abstract():
    assert not inspect.isabstract(scxml::SimpleState)


def test_scxml::simplestate_constructor_exists():
    assert callable(scxml::SimpleState.__init__)


def test_scxml::simplestate_constructor_args():
    sig = inspect.signature(scxml::SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_scxml::state_is_not_abstract():
    assert not inspect.isabstract(scxml::State)


def test_scxml::state_constructor_exists():
    assert callable(scxml::State.__init__)


def test_scxml::state_constructor_args():
    sig = inspect.signature(scxml::State.__init__)
    params = list(sig.parameters.keys())



def test_scxml::statechart_is_not_abstract():
    assert not inspect.isabstract(scxml::StateChart)


def test_scxml::statechart_constructor_exists():
    assert callable(scxml::StateChart.__init__)


def test_scxml::statechart_constructor_args():
    sig = inspect.signature(scxml::StateChart.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "version" in params, "Missing parameter 'version'"
    assert "exmode" in params, "Missing parameter 'exmode'"
    assert "profile" in params, "Missing parameter 'profile'"
    assert "xmlns" in params, "Missing parameter 'xmlns'"

def test_scxml::statechart_has_id():
    assert hasattr(scxml::StateChart, "id")
    descriptor = None
    for klass in scxml::StateChart.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml::statechart_has_version():
    assert hasattr(scxml::StateChart, "version")
    descriptor = None
    for klass in scxml::StateChart.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_scxml::statechart_has_exmode():
    assert hasattr(scxml::StateChart, "exmode")
    descriptor = None
    for klass in scxml::StateChart.__mro__:
        if "exmode" in klass.__dict__:
            descriptor = klass.__dict__["exmode"]
            break
    assert isinstance(descriptor, property)

def test_scxml::statechart_has_profile():
    assert hasattr(scxml::StateChart, "profile")
    descriptor = None
    for klass in scxml::StateChart.__mro__:
        if "profile" in klass.__dict__:
            descriptor = klass.__dict__["profile"]
            break
    assert isinstance(descriptor, property)

def test_scxml::statechart_has_xmlns():
    assert hasattr(scxml::StateChart, "xmlns")
    descriptor = None
    for klass in scxml::StateChart.__mro__:
        if "xmlns" in klass.__dict__:
            descriptor = klass.__dict__["xmlns"]
            break
    assert isinstance(descriptor, property)

def test_exmodedatatype_exists():
    # Check that the Enumeration exists
    assert ExmodeDatatype is not None

def test_exmodedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExmodeDatatype]
    expected_literals = [
        "lax",
        "strict",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExmodeDatatype"

def test_historytypedatatype_exists():
    # Check that the Enumeration exists
    assert HistoryTypeDatatype is not None

def test_historytypedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HistoryTypeDatatype]
    expected_literals = [
        "deep",
        "shallow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HistoryTypeDatatype"

def test_adaptertoken_exists():
    # Check that the Enumeration exists
    assert AdapterToken is not None

def test_adaptertoken_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdapterToken]
    expected_literals = [
        "DESCRIPTION",
        "DATAMODEL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdapterToken"


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
scxml::Description_strategy = st.builds(
    scxml::Description,
    value=
        safe_text
)
IAdaptable_strategy = st.builds(
    IAdaptable,
)
scxml::DescriptionContainer_strategy = st.builds(
    scxml::DescriptionContainer,
)
scxml::DatamodelContainer_strategy = st.builds(
    scxml::DatamodelContainer,
)
scxml::EClass_strategy = st.builds(
    scxml::EClass,
)
scxml::IAdaptable_strategy = st.builds(
    scxml::IAdaptable,
)
Data_strategy = st.builds(
    Data,
)
scxml::XData_strategy = st.builds(
    scxml::XData,
)
scxml::XObject_strategy = st.builds(
    scxml::XObject,
    exchange=
        st.booleans(),
    classifierName=
        safe_text,
    nsUri=
        safe_text
)
scxml::Else_strategy = st.builds(
    scxml::Else,
)
Conditional_strategy = st.builds(
    Conditional,
)
scxml::ElseIf_strategy = st.builds(
    scxml::ElseIf,
)
scxml::Conditional_strategy = st.builds(
    scxml::Conditional,
    cond=
        safe_text
)
scxml::Validate_strategy = st.builds(
    scxml::Validate,
    schema=
        safe_text,
    location=
        safe_text
)
scxml::Assign_strategy = st.builds(
    scxml::Assign,
    name=
        safe_text,
    location=
        safe_text,
    expr=
        safe_text
)
scxml::Cancel_strategy = st.builds(
    scxml::Cancel,
    sendid=
        safe_text,
    sendidexpr=
        safe_text
)
Donedata_strategy = st.builds(
    Donedata,
)
scxml::Send_strategy = st.builds(
    scxml::Send,
    type=
        safe_text,
    delay=
        safe_text,
    targetexpr=
        safe_text,
    id=
        safe_text,
    namelist=
        safe_text,
    hintsexpr=
        safe_text,
    target=
        safe_text,
    idlocation=
        safe_text,
    delayexpr=
        safe_text,
    typeexpr=
        safe_text,
    eventexpr=
        safe_text,
    hints=
        safe_text,
    event=
        safe_text
)
scxml::ExecutableContent_strategy = st.builds(
    scxml::ExecutableContent,
    group=
        safe_text
)
InitialState_strategy = st.builds(
    InitialState,
)
scxml::Invoke_strategy = st.builds(
    scxml::Invoke,
    idlocation=
        safe_text,
    namelist=
        safe_text,
    autoforward=
        safe_text,
    typeexpr=
        safe_text,
    srcexpr=
        safe_text,
    type=
        safe_text,
    id=
        safe_text,
    src=
        safe_text
)
scxml::AbstractSimpleState_strategy = st.builds(
    scxml::AbstractSimpleState,
)
State_strategy = st.builds(
    State,
)
scxml::Raise_strategy = st.builds(
    scxml::Raise,
    event=
        safe_text
)
scxml::Log_strategy = st.builds(
    scxml::Log,
    level=
        safe_text,
    label=
        safe_text,
    expr=
        safe_text
)
scxml::EObject_strategy = st.builds(
    scxml::EObject,
)
scxml::Donedata_strategy = st.builds(
    scxml::Donedata,
)
scxml::Param_strategy = st.builds(
    scxml::Param,
    expr=
        safe_text,
    name=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
scxml::Content_strategy = st.builds(
    scxml::Content,
    value=
        safe_text
)
scxml::ParallelState_strategy = st.builds(
    scxml::ParallelState,
)
scxml::AbstractState_strategy = st.builds(
    scxml::AbstractState,
)
scxml::CondEventTransition_strategy = st.builds(
    scxml::CondEventTransition,
    event=
        safe_text,
    cond=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
scxml::TransitionTarget_strategy = st.builds(
    scxml::TransitionTarget,
    id=
        safe_text
)
scxml::TransitionSource_strategy = st.builds(
    scxml::TransitionSource,
)
ExecutableContent_strategy = st.builds(
    ExecutableContent,
)
scxml::OnEntry_strategy = st.builds(
    scxml::OnEntry,
)
scxml::If_strategy = st.builds(
    scxml::If,
)
scxml::OnExit_strategy = st.builds(
    scxml::OnExit,
)
TransitionSource_strategy = st.builds(
    TransitionSource,
)
TransitionTarget_strategy = st.builds(
    TransitionTarget,
)
scxml::FinalState_strategy = st.builds(
    scxml::FinalState,
)
scxml::HistoryState_strategy = st.builds(
    scxml::HistoryState,
    type=
        safe_text
)
scxml::Script_strategy = st.builds(
    scxml::Script,
    value=
        safe_text
)
DescriptionContainer_strategy = st.builds(
    DescriptionContainer,
)
scxml::Transition_strategy = st.builds(
    scxml::Transition,
)
scxml::Data_strategy = st.builds(
    scxml::Data,
    expr=
        safe_text,
    id=
        safe_text,
    src=
        safe_text
)
scxml::Node_strategy = st.builds(
    scxml::Node,
)
scxml::Datamodel_strategy = st.builds(
    scxml::Datamodel,
    schema=
        safe_text
)
scxml::InitialState_strategy = st.builds(
    scxml::InitialState,
)
DatamodelContainer_strategy = st.builds(
    DatamodelContainer,
)
AbstractSimpleState_strategy = st.builds(
    AbstractSimpleState,
)
scxml::SimpleState_strategy = st.builds(
    scxml::SimpleState,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
scxml::State_strategy = st.builds(
    scxml::State,
)
scxml::StateChart_strategy = st.builds(
    scxml::StateChart,
    id=
        safe_text,
    version=
        safe_text,
    exmode=
        safe_text,
    profile=
        safe_text,
    xmlns=
        safe_text
)

@given(instance=scxml::Description_strategy)
@settings(max_examples=50)
def test_scxml::description_instantiation(instance):
    assert isinstance(instance, scxml::Description)

@given(instance=scxml::Description_strategy)
def test_scxml::description_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=scxml::Description_strategy)
def test_scxml::description_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=IAdaptable_strategy)
@settings(max_examples=50)
def test_iadaptable_instantiation(instance):
    assert isinstance(instance, IAdaptable)

@given(instance=scxml::DescriptionContainer_strategy)
@settings(max_examples=50)
def test_scxml::descriptioncontainer_instantiation(instance):
    assert isinstance(instance, scxml::DescriptionContainer)

@given(instance=scxml::DatamodelContainer_strategy)
@settings(max_examples=50)
def test_scxml::datamodelcontainer_instantiation(instance):
    assert isinstance(instance, scxml::DatamodelContainer)

@given(instance=scxml::EClass_strategy)
@settings(max_examples=50)
def test_scxml::eclass_instantiation(instance):
    assert isinstance(instance, scxml::EClass)

@given(instance=scxml::IAdaptable_strategy)
@settings(max_examples=50)
def test_scxml::iadaptable_instantiation(instance):
    assert isinstance(instance, scxml::IAdaptable)

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=scxml::XData_strategy)
@settings(max_examples=50)
def test_scxml::xdata_instantiation(instance):
    assert isinstance(instance, scxml::XData)

@given(instance=scxml::XObject_strategy)
@settings(max_examples=50)
def test_scxml::xobject_instantiation(instance):
    assert isinstance(instance, scxml::XObject)

@given(instance=scxml::XObject_strategy)
def test_scxml::xobject_exchange_type(instance):
    assert isinstance(instance.exchange, bool)


@given(instance=scxml::XObject_strategy)
def test_scxml::xobject_exchange_setter(instance):
    original = instance.exchange
    instance.exchange = original
    assert instance.exchange == original

@given(instance=scxml::XObject_strategy)
def test_scxml::xobject_classifierName_type(instance):
    assert isinstance(instance.classifierName, str)


@given(instance=scxml::XObject_strategy)
def test_scxml::xobject_classifierName_setter(instance):
    original = instance.classifierName
    instance.classifierName = original
    assert instance.classifierName == original

@given(instance=scxml::XObject_strategy)
def test_scxml::xobject_nsUri_type(instance):
    assert isinstance(instance.nsUri, str)


@given(instance=scxml::XObject_strategy)
def test_scxml::xobject_nsUri_setter(instance):
    original = instance.nsUri
    instance.nsUri = original
    assert instance.nsUri == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=scxml::XObject_strategy)
@settings(max_examples=30)
def test_scxml::xobject_registeradapter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.registerAdapter()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.registerAdapter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'registerAdapter' in scxml::XObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'registerAdapter' in scxml::XObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'registerAdapter' in scxml::XObject is not implemented or raised an error")

@given(instance=scxml::Else_strategy)
@settings(max_examples=50)
def test_scxml::else_instantiation(instance):
    assert isinstance(instance, scxml::Else)

@given(instance=Conditional_strategy)
@settings(max_examples=50)
def test_conditional_instantiation(instance):
    assert isinstance(instance, Conditional)

@given(instance=scxml::ElseIf_strategy)
@settings(max_examples=50)
def test_scxml::elseif_instantiation(instance):
    assert isinstance(instance, scxml::ElseIf)

@given(instance=scxml::Conditional_strategy)
@settings(max_examples=50)
def test_scxml::conditional_instantiation(instance):
    assert isinstance(instance, scxml::Conditional)

@given(instance=scxml::Conditional_strategy)
def test_scxml::conditional_cond_type(instance):
    assert isinstance(instance.cond, str)


@given(instance=scxml::Conditional_strategy)
def test_scxml::conditional_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original

@given(instance=scxml::Validate_strategy)
@settings(max_examples=50)
def test_scxml::validate_instantiation(instance):
    assert isinstance(instance, scxml::Validate)

@given(instance=scxml::Validate_strategy)
def test_scxml::validate_schema_type(instance):
    assert isinstance(instance.schema, str)


@given(instance=scxml::Validate_strategy)
def test_scxml::validate_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original

@given(instance=scxml::Validate_strategy)
def test_scxml::validate_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=scxml::Validate_strategy)
def test_scxml::validate_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=scxml::Assign_strategy)
@settings(max_examples=50)
def test_scxml::assign_instantiation(instance):
    assert isinstance(instance, scxml::Assign)

@given(instance=scxml::Assign_strategy)
def test_scxml::assign_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scxml::Assign_strategy)
def test_scxml::assign_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scxml::Assign_strategy)
def test_scxml::assign_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=scxml::Assign_strategy)
def test_scxml::assign_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=scxml::Assign_strategy)
def test_scxml::assign_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=scxml::Assign_strategy)
def test_scxml::assign_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=scxml::Cancel_strategy)
@settings(max_examples=50)
def test_scxml::cancel_instantiation(instance):
    assert isinstance(instance, scxml::Cancel)

@given(instance=scxml::Cancel_strategy)
def test_scxml::cancel_sendid_type(instance):
    assert isinstance(instance.sendid, str)


@given(instance=scxml::Cancel_strategy)
def test_scxml::cancel_sendid_setter(instance):
    original = instance.sendid
    instance.sendid = original
    assert instance.sendid == original

@given(instance=scxml::Cancel_strategy)
def test_scxml::cancel_sendidexpr_type(instance):
    assert isinstance(instance.sendidexpr, str)


@given(instance=scxml::Cancel_strategy)
def test_scxml::cancel_sendidexpr_setter(instance):
    original = instance.sendidexpr
    instance.sendidexpr = original
    assert instance.sendidexpr == original

@given(instance=Donedata_strategy)
@settings(max_examples=50)
def test_donedata_instantiation(instance):
    assert isinstance(instance, Donedata)

@given(instance=scxml::Send_strategy)
@settings(max_examples=50)
def test_scxml::send_instantiation(instance):
    assert isinstance(instance, scxml::Send)

@given(instance=scxml::Send_strategy)
def test_scxml::send_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_delay_type(instance):
    assert isinstance(instance.delay, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_targetexpr_type(instance):
    assert isinstance(instance.targetexpr, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_targetexpr_setter(instance):
    original = instance.targetexpr
    instance.targetexpr = original
    assert instance.targetexpr == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_namelist_type(instance):
    assert isinstance(instance.namelist, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_namelist_setter(instance):
    original = instance.namelist
    instance.namelist = original
    assert instance.namelist == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_hintsexpr_type(instance):
    assert isinstance(instance.hintsexpr, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_hintsexpr_setter(instance):
    original = instance.hintsexpr
    instance.hintsexpr = original
    assert instance.hintsexpr == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_idlocation_type(instance):
    assert isinstance(instance.idlocation, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_idlocation_setter(instance):
    original = instance.idlocation
    instance.idlocation = original
    assert instance.idlocation == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_delayexpr_type(instance):
    assert isinstance(instance.delayexpr, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_delayexpr_setter(instance):
    original = instance.delayexpr
    instance.delayexpr = original
    assert instance.delayexpr == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_typeexpr_type(instance):
    assert isinstance(instance.typeexpr, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_typeexpr_setter(instance):
    original = instance.typeexpr
    instance.typeexpr = original
    assert instance.typeexpr == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_eventexpr_type(instance):
    assert isinstance(instance.eventexpr, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_eventexpr_setter(instance):
    original = instance.eventexpr
    instance.eventexpr = original
    assert instance.eventexpr == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_hints_type(instance):
    assert isinstance(instance.hints, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_hints_setter(instance):
    original = instance.hints
    instance.hints = original
    assert instance.hints == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=scxml::ExecutableContent_strategy)
@settings(max_examples=50)
def test_scxml::executablecontent_instantiation(instance):
    assert isinstance(instance, scxml::ExecutableContent)

@given(instance=scxml::ExecutableContent_strategy)
def test_scxml::executablecontent_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=scxml::ExecutableContent_strategy)
def test_scxml::executablecontent_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=InitialState_strategy)
@settings(max_examples=50)
def test_initialstate_instantiation(instance):
    assert isinstance(instance, InitialState)

@given(instance=scxml::Invoke_strategy)
@settings(max_examples=50)
def test_scxml::invoke_instantiation(instance):
    assert isinstance(instance, scxml::Invoke)

@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_idlocation_type(instance):
    assert isinstance(instance.idlocation, str)


@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_idlocation_setter(instance):
    original = instance.idlocation
    instance.idlocation = original
    assert instance.idlocation == original

@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_namelist_type(instance):
    assert isinstance(instance.namelist, str)


@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_namelist_setter(instance):
    original = instance.namelist
    instance.namelist = original
    assert instance.namelist == original

@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_autoforward_type(instance):
    assert isinstance(instance.autoforward, str)


@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_autoforward_setter(instance):
    original = instance.autoforward
    instance.autoforward = original
    assert instance.autoforward == original

@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_typeexpr_type(instance):
    assert isinstance(instance.typeexpr, str)


@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_typeexpr_setter(instance):
    original = instance.typeexpr
    instance.typeexpr = original
    assert instance.typeexpr == original

@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_srcexpr_type(instance):
    assert isinstance(instance.srcexpr, str)


@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_srcexpr_setter(instance):
    original = instance.srcexpr
    instance.srcexpr = original
    assert instance.srcexpr == original

@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=scxml::AbstractSimpleState_strategy)
@settings(max_examples=50)
def test_scxml::abstractsimplestate_instantiation(instance):
    assert isinstance(instance, scxml::AbstractSimpleState)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=scxml::Raise_strategy)
@settings(max_examples=50)
def test_scxml::raise_instantiation(instance):
    assert isinstance(instance, scxml::Raise)

@given(instance=scxml::Raise_strategy)
def test_scxml::raise_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=scxml::Raise_strategy)
def test_scxml::raise_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=scxml::Log_strategy)
@settings(max_examples=50)
def test_scxml::log_instantiation(instance):
    assert isinstance(instance, scxml::Log)

@given(instance=scxml::Log_strategy)
def test_scxml::log_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=scxml::Log_strategy)
def test_scxml::log_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=scxml::Log_strategy)
def test_scxml::log_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=scxml::Log_strategy)
def test_scxml::log_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=scxml::Log_strategy)
def test_scxml::log_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=scxml::Log_strategy)
def test_scxml::log_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=scxml::EObject_strategy)
@settings(max_examples=50)
def test_scxml::eobject_instantiation(instance):
    assert isinstance(instance, scxml::EObject)

@given(instance=scxml::Donedata_strategy)
@settings(max_examples=50)
def test_scxml::donedata_instantiation(instance):
    assert isinstance(instance, scxml::Donedata)

@given(instance=scxml::Param_strategy)
@settings(max_examples=50)
def test_scxml::param_instantiation(instance):
    assert isinstance(instance, scxml::Param)

@given(instance=scxml::Param_strategy)
def test_scxml::param_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=scxml::Param_strategy)
def test_scxml::param_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=scxml::Param_strategy)
def test_scxml::param_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scxml::Param_strategy)
def test_scxml::param_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=scxml::Content_strategy)
@settings(max_examples=50)
def test_scxml::content_instantiation(instance):
    assert isinstance(instance, scxml::Content)

@given(instance=scxml::Content_strategy)
def test_scxml::content_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=scxml::Content_strategy)
def test_scxml::content_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=scxml::ParallelState_strategy)
@settings(max_examples=50)
def test_scxml::parallelstate_instantiation(instance):
    assert isinstance(instance, scxml::ParallelState)

@given(instance=scxml::AbstractState_strategy)
@settings(max_examples=50)
def test_scxml::abstractstate_instantiation(instance):
    assert isinstance(instance, scxml::AbstractState)

@given(instance=scxml::CondEventTransition_strategy)
@settings(max_examples=50)
def test_scxml::condeventtransition_instantiation(instance):
    assert isinstance(instance, scxml::CondEventTransition)

@given(instance=scxml::CondEventTransition_strategy)
def test_scxml::condeventtransition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=scxml::CondEventTransition_strategy)
def test_scxml::condeventtransition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=scxml::CondEventTransition_strategy)
def test_scxml::condeventtransition_cond_type(instance):
    assert isinstance(instance.cond, str)


@given(instance=scxml::CondEventTransition_strategy)
def test_scxml::condeventtransition_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=scxml::TransitionTarget_strategy)
@settings(max_examples=50)
def test_scxml::transitiontarget_instantiation(instance):
    assert isinstance(instance, scxml::TransitionTarget)

@given(instance=scxml::TransitionTarget_strategy)
def test_scxml::transitiontarget_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::TransitionTarget_strategy)
def test_scxml::transitiontarget_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::TransitionSource_strategy)
@settings(max_examples=50)
def test_scxml::transitionsource_instantiation(instance):
    assert isinstance(instance, scxml::TransitionSource)

@given(instance=ExecutableContent_strategy)
@settings(max_examples=50)
def test_executablecontent_instantiation(instance):
    assert isinstance(instance, ExecutableContent)

@given(instance=scxml::OnEntry_strategy)
@settings(max_examples=50)
def test_scxml::onentry_instantiation(instance):
    assert isinstance(instance, scxml::OnEntry)

@given(instance=scxml::If_strategy)
@settings(max_examples=50)
def test_scxml::if_instantiation(instance):
    assert isinstance(instance, scxml::If)

@given(instance=scxml::OnExit_strategy)
@settings(max_examples=50)
def test_scxml::onexit_instantiation(instance):
    assert isinstance(instance, scxml::OnExit)

@given(instance=TransitionSource_strategy)
@settings(max_examples=50)
def test_transitionsource_instantiation(instance):
    assert isinstance(instance, TransitionSource)

@given(instance=TransitionTarget_strategy)
@settings(max_examples=50)
def test_transitiontarget_instantiation(instance):
    assert isinstance(instance, TransitionTarget)

@given(instance=scxml::FinalState_strategy)
@settings(max_examples=50)
def test_scxml::finalstate_instantiation(instance):
    assert isinstance(instance, scxml::FinalState)

@given(instance=scxml::HistoryState_strategy)
@settings(max_examples=50)
def test_scxml::historystate_instantiation(instance):
    assert isinstance(instance, scxml::HistoryState)

@given(instance=scxml::HistoryState_strategy)
def test_scxml::historystate_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scxml::HistoryState_strategy)
def test_scxml::historystate_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scxml::Script_strategy)
@settings(max_examples=50)
def test_scxml::script_instantiation(instance):
    assert isinstance(instance, scxml::Script)

@given(instance=scxml::Script_strategy)
def test_scxml::script_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=scxml::Script_strategy)
def test_scxml::script_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DescriptionContainer_strategy)
@settings(max_examples=50)
def test_descriptioncontainer_instantiation(instance):
    assert isinstance(instance, DescriptionContainer)

@given(instance=scxml::Transition_strategy)
@settings(max_examples=50)
def test_scxml::transition_instantiation(instance):
    assert isinstance(instance, scxml::Transition)

@given(instance=scxml::Data_strategy)
@settings(max_examples=50)
def test_scxml::data_instantiation(instance):
    assert isinstance(instance, scxml::Data)

@given(instance=scxml::Data_strategy)
def test_scxml::data_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=scxml::Data_strategy)
def test_scxml::data_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=scxml::Data_strategy)
def test_scxml::data_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::Data_strategy)
def test_scxml::data_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::Data_strategy)
def test_scxml::data_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=scxml::Data_strategy)
def test_scxml::data_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=scxml::Node_strategy)
@settings(max_examples=50)
def test_scxml::node_instantiation(instance):
    assert isinstance(instance, scxml::Node)

@given(instance=scxml::Datamodel_strategy)
@settings(max_examples=50)
def test_scxml::datamodel_instantiation(instance):
    assert isinstance(instance, scxml::Datamodel)

@given(instance=scxml::Datamodel_strategy)
def test_scxml::datamodel_schema_type(instance):
    assert isinstance(instance.schema, str)


@given(instance=scxml::Datamodel_strategy)
def test_scxml::datamodel_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original

@given(instance=scxml::InitialState_strategy)
@settings(max_examples=50)
def test_scxml::initialstate_instantiation(instance):
    assert isinstance(instance, scxml::InitialState)

@given(instance=DatamodelContainer_strategy)
@settings(max_examples=50)
def test_datamodelcontainer_instantiation(instance):
    assert isinstance(instance, DatamodelContainer)

@given(instance=AbstractSimpleState_strategy)
@settings(max_examples=50)
def test_abstractsimplestate_instantiation(instance):
    assert isinstance(instance, AbstractSimpleState)

@given(instance=scxml::SimpleState_strategy)
@settings(max_examples=50)
def test_scxml::simplestate_instantiation(instance):
    assert isinstance(instance, scxml::SimpleState)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=scxml::State_strategy)
@settings(max_examples=50)
def test_scxml::state_instantiation(instance):
    assert isinstance(instance, scxml::State)

@given(instance=scxml::StateChart_strategy)
@settings(max_examples=50)
def test_scxml::statechart_instantiation(instance):
    assert isinstance(instance, scxml::StateChart)

@given(instance=scxml::StateChart_strategy)
def test_scxml::statechart_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::StateChart_strategy)
def test_scxml::statechart_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::StateChart_strategy)
def test_scxml::statechart_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=scxml::StateChart_strategy)
def test_scxml::statechart_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=scxml::StateChart_strategy)
def test_scxml::statechart_exmode_type(instance):
    assert isinstance(instance.exmode, str)


@given(instance=scxml::StateChart_strategy)
def test_scxml::statechart_exmode_setter(instance):
    original = instance.exmode
    instance.exmode = original
    assert instance.exmode == original

@given(instance=scxml::StateChart_strategy)
def test_scxml::statechart_profile_type(instance):
    assert isinstance(instance.profile, str)


@given(instance=scxml::StateChart_strategy)
def test_scxml::statechart_profile_setter(instance):
    original = instance.profile
    instance.profile = original
    assert instance.profile == original

@given(instance=scxml::StateChart_strategy)
def test_scxml::statechart_xmlns_type(instance):
    assert isinstance(instance.xmlns, str)


@given(instance=scxml::StateChart_strategy)
def test_scxml::statechart_xmlns_setter(instance):
    original = instance.xmlns
    instance.xmlns = original
    assert instance.xmlns == original
