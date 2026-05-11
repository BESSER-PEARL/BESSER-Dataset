import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    scxml::Cancel,
    scxml::Script,
    scxml::OnExit,
    scxml::OnEntry,
    NamedElement,
    scxml::InitialState,
    scxml::FinalState,
    scxml::Parallel,
    scxml::State,
    scxml::Transition,
    scxml::DataModel,
    scxml::NamedElement,
    scxml::Finalize,
    scxml::Data,
    scxml::Content,
    scxml::Else,
    scxml::ElseIf,
    scxml::Validate,
    scxml::Send,
    scxml::Raise,
    scxml::Param,
    scxml::Log,
    scxml::If,
    scxml::Donedata,
    scxml::ServiceTemplate,
    scxml::Assign,
    scxml::Invoke,
    scxml::Anchor,
    scxml::HistoryState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_scxml::script_is_not_abstract():
    assert not inspect.isabstract(scxml::Script)


def test_scxml::script_constructor_exists():
    assert callable(scxml::Script.__init__)


def test_scxml::script_constructor_args():
    sig = inspect.signature(scxml::Script.__init__)
    params = list(sig.parameters.keys())



def test_scxml::onexit_is_not_abstract():
    assert not inspect.isabstract(scxml::OnExit)


def test_scxml::onexit_constructor_exists():
    assert callable(scxml::OnExit.__init__)


def test_scxml::onexit_constructor_args():
    sig = inspect.signature(scxml::OnExit.__init__)
    params = list(sig.parameters.keys())



def test_scxml::onentry_is_not_abstract():
    assert not inspect.isabstract(scxml::OnEntry)


def test_scxml::onentry_constructor_exists():
    assert callable(scxml::OnEntry.__init__)


def test_scxml::onentry_constructor_args():
    sig = inspect.signature(scxml::OnEntry.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_scxml::initialstate_is_not_abstract():
    assert not inspect.isabstract(scxml::InitialState)


def test_scxml::initialstate_constructor_exists():
    assert callable(scxml::InitialState.__init__)


def test_scxml::initialstate_constructor_args():
    sig = inspect.signature(scxml::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_scxml::finalstate_is_not_abstract():
    assert not inspect.isabstract(scxml::FinalState)


def test_scxml::finalstate_constructor_exists():
    assert callable(scxml::FinalState.__init__)


def test_scxml::finalstate_constructor_args():
    sig = inspect.signature(scxml::FinalState.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_scxml::finalstate_has_id():
    assert hasattr(scxml::FinalState, "id")
    descriptor = None
    for klass in scxml::FinalState.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_scxml::parallel_is_not_abstract():
    assert not inspect.isabstract(scxml::Parallel)


def test_scxml::parallel_constructor_exists():
    assert callable(scxml::Parallel.__init__)


def test_scxml::parallel_constructor_args():
    sig = inspect.signature(scxml::Parallel.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_scxml::parallel_has_id():
    assert hasattr(scxml::Parallel, "id")
    descriptor = None
    for klass in scxml::Parallel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_scxml::state_is_not_abstract():
    assert not inspect.isabstract(scxml::State)


def test_scxml::state_constructor_exists():
    assert callable(scxml::State.__init__)


def test_scxml::state_constructor_args():
    sig = inspect.signature(scxml::State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_scxml::state_has_id():
    assert hasattr(scxml::State, "id")
    descriptor = None
    for klass in scxml::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_scxml::transition_is_not_abstract():
    assert not inspect.isabstract(scxml::Transition)


def test_scxml::transition_constructor_exists():
    assert callable(scxml::Transition.__init__)


def test_scxml::transition_constructor_args():
    sig = inspect.signature(scxml::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "cond" in params, "Missing parameter 'cond'"
    assert "event" in params, "Missing parameter 'event'"
    assert "anchor" in params, "Missing parameter 'anchor'"

def test_scxml::transition_has_cond():
    assert hasattr(scxml::Transition, "cond")
    descriptor = None
    for klass in scxml::Transition.__mro__:
        if "cond" in klass.__dict__:
            descriptor = klass.__dict__["cond"]
            break
    assert isinstance(descriptor, property)

def test_scxml::transition_has_event():
    assert hasattr(scxml::Transition, "event")
    descriptor = None
    for klass in scxml::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_scxml::transition_has_anchor():
    assert hasattr(scxml::Transition, "anchor")
    descriptor = None
    for klass in scxml::Transition.__mro__:
        if "anchor" in klass.__dict__:
            descriptor = klass.__dict__["anchor"]
            break
    assert isinstance(descriptor, property)



def test_scxml::datamodel_is_not_abstract():
    assert not inspect.isabstract(scxml::DataModel)


def test_scxml::datamodel_constructor_exists():
    assert callable(scxml::DataModel.__init__)


def test_scxml::datamodel_constructor_args():
    sig = inspect.signature(scxml::DataModel.__init__)
    params = list(sig.parameters.keys())
    assert "schema" in params, "Missing parameter 'schema'"

def test_scxml::datamodel_has_schema():
    assert hasattr(scxml::DataModel, "schema")
    descriptor = None
    for klass in scxml::DataModel.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)



def test_scxml::namedelement_is_not_abstract():
    assert not inspect.isabstract(scxml::NamedElement)


def test_scxml::namedelement_constructor_exists():
    assert callable(scxml::NamedElement.__init__)


def test_scxml::namedelement_constructor_args():
    sig = inspect.signature(scxml::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_scxml::finalize_is_not_abstract():
    assert not inspect.isabstract(scxml::Finalize)


def test_scxml::finalize_constructor_exists():
    assert callable(scxml::Finalize.__init__)


def test_scxml::finalize_constructor_args():
    sig = inspect.signature(scxml::Finalize.__init__)
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



def test_scxml::content_is_not_abstract():
    assert not inspect.isabstract(scxml::Content)


def test_scxml::content_constructor_exists():
    assert callable(scxml::Content.__init__)


def test_scxml::content_constructor_args():
    sig = inspect.signature(scxml::Content.__init__)
    params = list(sig.parameters.keys())



def test_scxml::else_is_not_abstract():
    assert not inspect.isabstract(scxml::Else)


def test_scxml::else_constructor_exists():
    assert callable(scxml::Else.__init__)


def test_scxml::else_constructor_args():
    sig = inspect.signature(scxml::Else.__init__)
    params = list(sig.parameters.keys())



def test_scxml::elseif_is_not_abstract():
    assert not inspect.isabstract(scxml::ElseIf)


def test_scxml::elseif_constructor_exists():
    assert callable(scxml::ElseIf.__init__)


def test_scxml::elseif_constructor_args():
    sig = inspect.signature(scxml::ElseIf.__init__)
    params = list(sig.parameters.keys())
    assert "cond" in params, "Missing parameter 'cond'"

def test_scxml::elseif_has_cond():
    assert hasattr(scxml::ElseIf, "cond")
    descriptor = None
    for klass in scxml::ElseIf.__mro__:
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



def test_scxml::send_is_not_abstract():
    assert not inspect.isabstract(scxml::Send)


def test_scxml::send_constructor_exists():
    assert callable(scxml::Send.__init__)


def test_scxml::send_constructor_args():
    sig = inspect.signature(scxml::Send.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "target" in params, "Missing parameter 'target'"
    assert "typeexpr" in params, "Missing parameter 'typeexpr'"
    assert "idlocation" in params, "Missing parameter 'idlocation'"
    assert "delay" in params, "Missing parameter 'delay'"
    assert "delayexpr" in params, "Missing parameter 'delayexpr'"
    assert "eventexpr" in params, "Missing parameter 'eventexpr'"
    assert "event" in params, "Missing parameter 'event'"
    assert "targetexpr" in params, "Missing parameter 'targetexpr'"
    assert "namelist" in params, "Missing parameter 'namelist'"
    assert "type" in params, "Missing parameter 'type'"
    assert "hintsexpr" in params, "Missing parameter 'hintsexpr'"
    assert "hints" in params, "Missing parameter 'hints'"

def test_scxml::send_has_id():
    assert hasattr(scxml::Send, "id")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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

def test_scxml::send_has_typeexpr():
    assert hasattr(scxml::Send, "typeexpr")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "typeexpr" in klass.__dict__:
            descriptor = klass.__dict__["typeexpr"]
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

def test_scxml::send_has_delay():
    assert hasattr(scxml::Send, "delay")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
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

def test_scxml::send_has_eventexpr():
    assert hasattr(scxml::Send, "eventexpr")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "eventexpr" in klass.__dict__:
            descriptor = klass.__dict__["eventexpr"]
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

def test_scxml::send_has_targetexpr():
    assert hasattr(scxml::Send, "targetexpr")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "targetexpr" in klass.__dict__:
            descriptor = klass.__dict__["targetexpr"]
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

def test_scxml::send_has_type():
    assert hasattr(scxml::Send, "type")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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

def test_scxml::send_has_hints():
    assert hasattr(scxml::Send, "hints")
    descriptor = None
    for klass in scxml::Send.__mro__:
        if "hints" in klass.__dict__:
            descriptor = klass.__dict__["hints"]
            break
    assert isinstance(descriptor, property)



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



def test_scxml::param_is_not_abstract():
    assert not inspect.isabstract(scxml::Param)


def test_scxml::param_constructor_exists():
    assert callable(scxml::Param.__init__)


def test_scxml::param_constructor_args():
    sig = inspect.signature(scxml::Param.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "expr" in params, "Missing parameter 'expr'"

def test_scxml::param_has_name():
    assert hasattr(scxml::Param, "name")
    descriptor = None
    for klass in scxml::Param.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_scxml::param_has_expr():
    assert hasattr(scxml::Param, "expr")
    descriptor = None
    for klass in scxml::Param.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)



def test_scxml::log_is_not_abstract():
    assert not inspect.isabstract(scxml::Log)


def test_scxml::log_constructor_exists():
    assert callable(scxml::Log.__init__)


def test_scxml::log_constructor_args():
    sig = inspect.signature(scxml::Log.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "level" in params, "Missing parameter 'level'"
    assert "expr" in params, "Missing parameter 'expr'"

def test_scxml::log_has_label():
    assert hasattr(scxml::Log, "label")
    descriptor = None
    for klass in scxml::Log.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_scxml::log_has_level():
    assert hasattr(scxml::Log, "level")
    descriptor = None
    for klass in scxml::Log.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
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



def test_scxml::if_is_not_abstract():
    assert not inspect.isabstract(scxml::If)


def test_scxml::if_constructor_exists():
    assert callable(scxml::If.__init__)


def test_scxml::if_constructor_args():
    sig = inspect.signature(scxml::If.__init__)
    params = list(sig.parameters.keys())
    assert "cond" in params, "Missing parameter 'cond'"

def test_scxml::if_has_cond():
    assert hasattr(scxml::If, "cond")
    descriptor = None
    for klass in scxml::If.__mro__:
        if "cond" in klass.__dict__:
            descriptor = klass.__dict__["cond"]
            break
    assert isinstance(descriptor, property)



def test_scxml::donedata_is_not_abstract():
    assert not inspect.isabstract(scxml::Donedata)


def test_scxml::donedata_constructor_exists():
    assert callable(scxml::Donedata.__init__)


def test_scxml::donedata_constructor_args():
    sig = inspect.signature(scxml::Donedata.__init__)
    params = list(sig.parameters.keys())



def test_scxml::servicetemplate_is_not_abstract():
    assert not inspect.isabstract(scxml::ServiceTemplate)


def test_scxml::servicetemplate_constructor_exists():
    assert callable(scxml::ServiceTemplate.__init__)


def test_scxml::servicetemplate_constructor_args():
    sig = inspect.signature(scxml::ServiceTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "xmlns" in params, "Missing parameter 'xmlns'"
    assert "name" in params, "Missing parameter 'name'"
    assert "profile" in params, "Missing parameter 'profile'"
    assert "version" in params, "Missing parameter 'version'"
    assert "exmode" in params, "Missing parameter 'exmode'"

def test_scxml::servicetemplate_has_xmlns():
    assert hasattr(scxml::ServiceTemplate, "xmlns")
    descriptor = None
    for klass in scxml::ServiceTemplate.__mro__:
        if "xmlns" in klass.__dict__:
            descriptor = klass.__dict__["xmlns"]
            break
    assert isinstance(descriptor, property)

def test_scxml::servicetemplate_has_name():
    assert hasattr(scxml::ServiceTemplate, "name")
    descriptor = None
    for klass in scxml::ServiceTemplate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_scxml::servicetemplate_has_profile():
    assert hasattr(scxml::ServiceTemplate, "profile")
    descriptor = None
    for klass in scxml::ServiceTemplate.__mro__:
        if "profile" in klass.__dict__:
            descriptor = klass.__dict__["profile"]
            break
    assert isinstance(descriptor, property)

def test_scxml::servicetemplate_has_version():
    assert hasattr(scxml::ServiceTemplate, "version")
    descriptor = None
    for klass in scxml::ServiceTemplate.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_scxml::servicetemplate_has_exmode():
    assert hasattr(scxml::ServiceTemplate, "exmode")
    descriptor = None
    for klass in scxml::ServiceTemplate.__mro__:
        if "exmode" in klass.__dict__:
            descriptor = klass.__dict__["exmode"]
            break
    assert isinstance(descriptor, property)



def test_scxml::assign_is_not_abstract():
    assert not inspect.isabstract(scxml::Assign)


def test_scxml::assign_constructor_exists():
    assert callable(scxml::Assign.__init__)


def test_scxml::assign_constructor_args():
    sig = inspect.signature(scxml::Assign.__init__)
    params = list(sig.parameters.keys())
    assert "expr" in params, "Missing parameter 'expr'"
    assert "dataid" in params, "Missing parameter 'dataid'"
    assert "location" in params, "Missing parameter 'location'"

def test_scxml::assign_has_expr():
    assert hasattr(scxml::Assign, "expr")
    descriptor = None
    for klass in scxml::Assign.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::assign_has_dataid():
    assert hasattr(scxml::Assign, "dataid")
    descriptor = None
    for klass in scxml::Assign.__mro__:
        if "dataid" in klass.__dict__:
            descriptor = klass.__dict__["dataid"]
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



def test_scxml::invoke_is_not_abstract():
    assert not inspect.isabstract(scxml::Invoke)


def test_scxml::invoke_constructor_exists():
    assert callable(scxml::Invoke.__init__)


def test_scxml::invoke_constructor_args():
    sig = inspect.signature(scxml::Invoke.__init__)
    params = list(sig.parameters.keys())
    assert "autoforward" in params, "Missing parameter 'autoforward'"
    assert "id" in params, "Missing parameter 'id'"
    assert "typeexpr" in params, "Missing parameter 'typeexpr'"
    assert "type" in params, "Missing parameter 'type'"
    assert "idlocation" in params, "Missing parameter 'idlocation'"
    assert "namelist" in params, "Missing parameter 'namelist'"
    assert "src" in params, "Missing parameter 'src'"
    assert "srcexpr" in params, "Missing parameter 'srcexpr'"

def test_scxml::invoke_has_autoforward():
    assert hasattr(scxml::Invoke, "autoforward")
    descriptor = None
    for klass in scxml::Invoke.__mro__:
        if "autoforward" in klass.__dict__:
            descriptor = klass.__dict__["autoforward"]
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

def test_scxml::invoke_has_typeexpr():
    assert hasattr(scxml::Invoke, "typeexpr")
    descriptor = None
    for klass in scxml::Invoke.__mro__:
        if "typeexpr" in klass.__dict__:
            descriptor = klass.__dict__["typeexpr"]
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

def test_scxml::invoke_has_src():
    assert hasattr(scxml::Invoke, "src")
    descriptor = None
    for klass in scxml::Invoke.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
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



def test_scxml::anchor_is_not_abstract():
    assert not inspect.isabstract(scxml::Anchor)


def test_scxml::anchor_constructor_exists():
    assert callable(scxml::Anchor.__init__)


def test_scxml::anchor_constructor_args():
    sig = inspect.signature(scxml::Anchor.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "snapshot" in params, "Missing parameter 'snapshot'"

def test_scxml::anchor_has_type():
    assert hasattr(scxml::Anchor, "type")
    descriptor = None
    for klass in scxml::Anchor.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scxml::anchor_has_snapshot():
    assert hasattr(scxml::Anchor, "snapshot")
    descriptor = None
    for klass in scxml::Anchor.__mro__:
        if "snapshot" in klass.__dict__:
            descriptor = klass.__dict__["snapshot"]
            break
    assert isinstance(descriptor, property)



def test_scxml::historystate_is_not_abstract():
    assert not inspect.isabstract(scxml::HistoryState)


def test_scxml::historystate_constructor_exists():
    assert callable(scxml::HistoryState.__init__)


def test_scxml::historystate_constructor_args():
    sig = inspect.signature(scxml::HistoryState.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

def test_scxml::historystate_has_type():
    assert hasattr(scxml::HistoryState, "type")
    descriptor = None
    for klass in scxml::HistoryState.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scxml::historystate_has_id():
    assert hasattr(scxml::HistoryState, "id")
    descriptor = None
    for klass in scxml::HistoryState.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)


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
scxml::Cancel_strategy = st.builds(
    scxml::Cancel,
    sendid=
        safe_text,
    sendidexpr=
        safe_text
)
scxml::Script_strategy = st.builds(
    scxml::Script,
)
scxml::OnExit_strategy = st.builds(
    scxml::OnExit,
)
scxml::OnEntry_strategy = st.builds(
    scxml::OnEntry,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
scxml::InitialState_strategy = st.builds(
    scxml::InitialState,
)
scxml::FinalState_strategy = st.builds(
    scxml::FinalState,
    id=
        safe_text
)
scxml::Parallel_strategy = st.builds(
    scxml::Parallel,
    id=
        safe_text
)
scxml::State_strategy = st.builds(
    scxml::State,
    id=
        safe_text
)
scxml::Transition_strategy = st.builds(
    scxml::Transition,
    cond=
        safe_text,
    event=
        safe_text,
    anchor=
        safe_text
)
scxml::DataModel_strategy = st.builds(
    scxml::DataModel,
    schema=
        safe_text
)
scxml::NamedElement_strategy = st.builds(
    scxml::NamedElement,
)
scxml::Finalize_strategy = st.builds(
    scxml::Finalize,
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
scxml::Content_strategy = st.builds(
    scxml::Content,
)
scxml::Else_strategy = st.builds(
    scxml::Else,
)
scxml::ElseIf_strategy = st.builds(
    scxml::ElseIf,
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
scxml::Send_strategy = st.builds(
    scxml::Send,
    id=
        safe_text,
    target=
        safe_text,
    typeexpr=
        safe_text,
    idlocation=
        safe_text,
    delay=
        safe_text,
    delayexpr=
        safe_text,
    eventexpr=
        safe_text,
    event=
        safe_text,
    targetexpr=
        safe_text,
    namelist=
        safe_text,
    type=
        safe_text,
    hintsexpr=
        safe_text,
    hints=
        safe_text
)
scxml::Raise_strategy = st.builds(
    scxml::Raise,
    event=
        safe_text
)
scxml::Param_strategy = st.builds(
    scxml::Param,
    name=
        safe_text,
    expr=
        safe_text
)
scxml::Log_strategy = st.builds(
    scxml::Log,
    label=
        safe_text,
    level=
        safe_text,
    expr=
        safe_text
)
scxml::If_strategy = st.builds(
    scxml::If,
    cond=
        safe_text
)
scxml::Donedata_strategy = st.builds(
    scxml::Donedata,
)
scxml::ServiceTemplate_strategy = st.builds(
    scxml::ServiceTemplate,
    xmlns=
        safe_text,
    name=
        safe_text,
    profile=
        safe_text,
    version=
        safe_text,
    exmode=
        safe_text
)
scxml::Assign_strategy = st.builds(
    scxml::Assign,
    expr=
        safe_text,
    dataid=
        safe_text,
    location=
        safe_text
)
scxml::Invoke_strategy = st.builds(
    scxml::Invoke,
    autoforward=
        safe_text,
    id=
        safe_text,
    typeexpr=
        safe_text,
    type=
        safe_text,
    idlocation=
        safe_text,
    namelist=
        safe_text,
    src=
        safe_text,
    srcexpr=
        safe_text
)
scxml::Anchor_strategy = st.builds(
    scxml::Anchor,
    type=
        safe_text,
    snapshot=
        safe_text
)
scxml::HistoryState_strategy = st.builds(
    scxml::HistoryState,
    type=
        safe_text,
    id=
        safe_text
)

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

@given(instance=scxml::Script_strategy)
@settings(max_examples=50)
def test_scxml::script_instantiation(instance):
    assert isinstance(instance, scxml::Script)

@given(instance=scxml::OnExit_strategy)
@settings(max_examples=50)
def test_scxml::onexit_instantiation(instance):
    assert isinstance(instance, scxml::OnExit)

@given(instance=scxml::OnEntry_strategy)
@settings(max_examples=50)
def test_scxml::onentry_instantiation(instance):
    assert isinstance(instance, scxml::OnEntry)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=scxml::InitialState_strategy)
@settings(max_examples=50)
def test_scxml::initialstate_instantiation(instance):
    assert isinstance(instance, scxml::InitialState)

@given(instance=scxml::FinalState_strategy)
@settings(max_examples=50)
def test_scxml::finalstate_instantiation(instance):
    assert isinstance(instance, scxml::FinalState)

@given(instance=scxml::FinalState_strategy)
def test_scxml::finalstate_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::FinalState_strategy)
def test_scxml::finalstate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::Parallel_strategy)
@settings(max_examples=50)
def test_scxml::parallel_instantiation(instance):
    assert isinstance(instance, scxml::Parallel)

@given(instance=scxml::Parallel_strategy)
def test_scxml::parallel_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::Parallel_strategy)
def test_scxml::parallel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::State_strategy)
@settings(max_examples=50)
def test_scxml::state_instantiation(instance):
    assert isinstance(instance, scxml::State)

@given(instance=scxml::State_strategy)
def test_scxml::state_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::State_strategy)
def test_scxml::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::Transition_strategy)
@settings(max_examples=50)
def test_scxml::transition_instantiation(instance):
    assert isinstance(instance, scxml::Transition)

@given(instance=scxml::Transition_strategy)
def test_scxml::transition_cond_type(instance):
    assert isinstance(instance.cond, str)


@given(instance=scxml::Transition_strategy)
def test_scxml::transition_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original

@given(instance=scxml::Transition_strategy)
def test_scxml::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=scxml::Transition_strategy)
def test_scxml::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=scxml::Transition_strategy)
def test_scxml::transition_anchor_type(instance):
    assert isinstance(instance.anchor, str)


@given(instance=scxml::Transition_strategy)
def test_scxml::transition_anchor_setter(instance):
    original = instance.anchor
    instance.anchor = original
    assert instance.anchor == original

@given(instance=scxml::DataModel_strategy)
@settings(max_examples=50)
def test_scxml::datamodel_instantiation(instance):
    assert isinstance(instance, scxml::DataModel)

@given(instance=scxml::DataModel_strategy)
def test_scxml::datamodel_schema_type(instance):
    assert isinstance(instance.schema, str)


@given(instance=scxml::DataModel_strategy)
def test_scxml::datamodel_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original

@given(instance=scxml::NamedElement_strategy)
@settings(max_examples=50)
def test_scxml::namedelement_instantiation(instance):
    assert isinstance(instance, scxml::NamedElement)

@given(instance=scxml::Finalize_strategy)
@settings(max_examples=50)
def test_scxml::finalize_instantiation(instance):
    assert isinstance(instance, scxml::Finalize)

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

@given(instance=scxml::Content_strategy)
@settings(max_examples=50)
def test_scxml::content_instantiation(instance):
    assert isinstance(instance, scxml::Content)

@given(instance=scxml::Else_strategy)
@settings(max_examples=50)
def test_scxml::else_instantiation(instance):
    assert isinstance(instance, scxml::Else)

@given(instance=scxml::ElseIf_strategy)
@settings(max_examples=50)
def test_scxml::elseif_instantiation(instance):
    assert isinstance(instance, scxml::ElseIf)

@given(instance=scxml::ElseIf_strategy)
def test_scxml::elseif_cond_type(instance):
    assert isinstance(instance.cond, str)


@given(instance=scxml::ElseIf_strategy)
def test_scxml::elseif_cond_setter(instance):
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

@given(instance=scxml::Send_strategy)
@settings(max_examples=50)
def test_scxml::send_instantiation(instance):
    assert isinstance(instance, scxml::Send)

@given(instance=scxml::Send_strategy)
def test_scxml::send_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_typeexpr_type(instance):
    assert isinstance(instance.typeexpr, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_typeexpr_setter(instance):
    original = instance.typeexpr
    instance.typeexpr = original
    assert instance.typeexpr == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_idlocation_type(instance):
    assert isinstance(instance.idlocation, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_idlocation_setter(instance):
    original = instance.idlocation
    instance.idlocation = original
    assert instance.idlocation == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_delay_type(instance):
    assert isinstance(instance.delay, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_delayexpr_type(instance):
    assert isinstance(instance.delayexpr, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_delayexpr_setter(instance):
    original = instance.delayexpr
    instance.delayexpr = original
    assert instance.delayexpr == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_eventexpr_type(instance):
    assert isinstance(instance.eventexpr, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_eventexpr_setter(instance):
    original = instance.eventexpr
    instance.eventexpr = original
    assert instance.eventexpr == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_targetexpr_type(instance):
    assert isinstance(instance.targetexpr, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_targetexpr_setter(instance):
    original = instance.targetexpr
    instance.targetexpr = original
    assert instance.targetexpr == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_namelist_type(instance):
    assert isinstance(instance.namelist, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_namelist_setter(instance):
    original = instance.namelist
    instance.namelist = original
    assert instance.namelist == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_hintsexpr_type(instance):
    assert isinstance(instance.hintsexpr, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_hintsexpr_setter(instance):
    original = instance.hintsexpr
    instance.hintsexpr = original
    assert instance.hintsexpr == original

@given(instance=scxml::Send_strategy)
def test_scxml::send_hints_type(instance):
    assert isinstance(instance.hints, str)


@given(instance=scxml::Send_strategy)
def test_scxml::send_hints_setter(instance):
    original = instance.hints
    instance.hints = original
    assert instance.hints == original

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

@given(instance=scxml::Param_strategy)
@settings(max_examples=50)
def test_scxml::param_instantiation(instance):
    assert isinstance(instance, scxml::Param)

@given(instance=scxml::Param_strategy)
def test_scxml::param_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scxml::Param_strategy)
def test_scxml::param_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scxml::Param_strategy)
def test_scxml::param_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=scxml::Param_strategy)
def test_scxml::param_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=scxml::Log_strategy)
@settings(max_examples=50)
def test_scxml::log_instantiation(instance):
    assert isinstance(instance, scxml::Log)

@given(instance=scxml::Log_strategy)
def test_scxml::log_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=scxml::Log_strategy)
def test_scxml::log_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=scxml::Log_strategy)
def test_scxml::log_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=scxml::Log_strategy)
def test_scxml::log_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=scxml::Log_strategy)
def test_scxml::log_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=scxml::Log_strategy)
def test_scxml::log_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=scxml::If_strategy)
@settings(max_examples=50)
def test_scxml::if_instantiation(instance):
    assert isinstance(instance, scxml::If)

@given(instance=scxml::If_strategy)
def test_scxml::if_cond_type(instance):
    assert isinstance(instance.cond, str)


@given(instance=scxml::If_strategy)
def test_scxml::if_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original

@given(instance=scxml::Donedata_strategy)
@settings(max_examples=50)
def test_scxml::donedata_instantiation(instance):
    assert isinstance(instance, scxml::Donedata)

@given(instance=scxml::ServiceTemplate_strategy)
@settings(max_examples=50)
def test_scxml::servicetemplate_instantiation(instance):
    assert isinstance(instance, scxml::ServiceTemplate)

@given(instance=scxml::ServiceTemplate_strategy)
def test_scxml::servicetemplate_xmlns_type(instance):
    assert isinstance(instance.xmlns, str)


@given(instance=scxml::ServiceTemplate_strategy)
def test_scxml::servicetemplate_xmlns_setter(instance):
    original = instance.xmlns
    instance.xmlns = original
    assert instance.xmlns == original

@given(instance=scxml::ServiceTemplate_strategy)
def test_scxml::servicetemplate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scxml::ServiceTemplate_strategy)
def test_scxml::servicetemplate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scxml::ServiceTemplate_strategy)
def test_scxml::servicetemplate_profile_type(instance):
    assert isinstance(instance.profile, str)


@given(instance=scxml::ServiceTemplate_strategy)
def test_scxml::servicetemplate_profile_setter(instance):
    original = instance.profile
    instance.profile = original
    assert instance.profile == original

@given(instance=scxml::ServiceTemplate_strategy)
def test_scxml::servicetemplate_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=scxml::ServiceTemplate_strategy)
def test_scxml::servicetemplate_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=scxml::ServiceTemplate_strategy)
def test_scxml::servicetemplate_exmode_type(instance):
    assert isinstance(instance.exmode, str)


@given(instance=scxml::ServiceTemplate_strategy)
def test_scxml::servicetemplate_exmode_setter(instance):
    original = instance.exmode
    instance.exmode = original
    assert instance.exmode == original

@given(instance=scxml::Assign_strategy)
@settings(max_examples=50)
def test_scxml::assign_instantiation(instance):
    assert isinstance(instance, scxml::Assign)

@given(instance=scxml::Assign_strategy)
def test_scxml::assign_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=scxml::Assign_strategy)
def test_scxml::assign_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=scxml::Assign_strategy)
def test_scxml::assign_dataid_type(instance):
    assert isinstance(instance.dataid, str)


@given(instance=scxml::Assign_strategy)
def test_scxml::assign_dataid_setter(instance):
    original = instance.dataid
    instance.dataid = original
    assert instance.dataid == original

@given(instance=scxml::Assign_strategy)
def test_scxml::assign_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=scxml::Assign_strategy)
def test_scxml::assign_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=scxml::Invoke_strategy)
@settings(max_examples=50)
def test_scxml::invoke_instantiation(instance):
    assert isinstance(instance, scxml::Invoke)

@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_autoforward_type(instance):
    assert isinstance(instance.autoforward, str)


@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_autoforward_setter(instance):
    original = instance.autoforward
    instance.autoforward = original
    assert instance.autoforward == original

@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_typeexpr_type(instance):
    assert isinstance(instance.typeexpr, str)


@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_typeexpr_setter(instance):
    original = instance.typeexpr
    instance.typeexpr = original
    assert instance.typeexpr == original

@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

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
def test_scxml::invoke_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_srcexpr_type(instance):
    assert isinstance(instance.srcexpr, str)


@given(instance=scxml::Invoke_strategy)
def test_scxml::invoke_srcexpr_setter(instance):
    original = instance.srcexpr
    instance.srcexpr = original
    assert instance.srcexpr == original

@given(instance=scxml::Anchor_strategy)
@settings(max_examples=50)
def test_scxml::anchor_instantiation(instance):
    assert isinstance(instance, scxml::Anchor)

@given(instance=scxml::Anchor_strategy)
def test_scxml::anchor_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scxml::Anchor_strategy)
def test_scxml::anchor_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scxml::Anchor_strategy)
def test_scxml::anchor_snapshot_type(instance):
    assert isinstance(instance.snapshot, str)


@given(instance=scxml::Anchor_strategy)
def test_scxml::anchor_snapshot_setter(instance):
    original = instance.snapshot
    instance.snapshot = original
    assert instance.snapshot == original

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

@given(instance=scxml::HistoryState_strategy)
def test_scxml::historystate_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::HistoryState_strategy)
def test_scxml::historystate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
