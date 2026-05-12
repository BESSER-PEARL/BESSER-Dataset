import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    scxml_Finalize,
    scxml_Data,
    scxml_Content,
    scxml_Else,
    scxml_ElseIf,
    scxml_Validate,
    scxml_Send,
    scxml_Raise,
    scxml_Param,
    scxml_Log,
    scxml_If,
    scxml_Donedata,
    scxml_ServiceTemplate,
    scxml_Assign,
    scxml_Invoke,
    scxml_Anchor,
    scxml_Cancel,
    scxml_Script,
    scxml_OnExit,
    scxml_OnEntry,
    NamedElement,
    scxml_Parallel,
    scxml_InitialState,
    scxml_HistoryState,
    scxml_FinalState,
    scxml_State,
    scxml_Transition,
    scxml_DataModel,
    scxml_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scxml_finalize_is_not_abstract():
    assert not inspect.isabstract(scxml_Finalize)


def test_scxml_finalize_constructor_exists():
    assert callable(scxml_Finalize.__init__)


def test_scxml_finalize_constructor_args():
    sig = inspect.signature(scxml_Finalize.__init__)
    params = list(sig.parameters.keys())



def test_scxml_data_is_not_abstract():
    assert not inspect.isabstract(scxml_Data)


def test_scxml_data_constructor_exists():
    assert callable(scxml_Data.__init__)


def test_scxml_data_constructor_args():
    sig = inspect.signature(scxml_Data.__init__)
    params = list(sig.parameters.keys())
    assert "src" in params, "Missing parameter 'src'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "id" in params, "Missing parameter 'id'"

def test_scxml_data_has_src():
    assert hasattr(scxml_Data, "src")
    descriptor = None
    for klass in scxml_Data.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_scxml_data_has_expr():
    assert hasattr(scxml_Data, "expr")
    descriptor = None
    for klass in scxml_Data.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_data_has_id():
    assert hasattr(scxml_Data, "id")
    descriptor = None
    for klass in scxml_Data.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_scxml_content_is_not_abstract():
    assert not inspect.isabstract(scxml_Content)


def test_scxml_content_constructor_exists():
    assert callable(scxml_Content.__init__)


def test_scxml_content_constructor_args():
    sig = inspect.signature(scxml_Content.__init__)
    params = list(sig.parameters.keys())



def test_scxml_else_is_not_abstract():
    assert not inspect.isabstract(scxml_Else)


def test_scxml_else_constructor_exists():
    assert callable(scxml_Else.__init__)


def test_scxml_else_constructor_args():
    sig = inspect.signature(scxml_Else.__init__)
    params = list(sig.parameters.keys())



def test_scxml_elseif_is_not_abstract():
    assert not inspect.isabstract(scxml_ElseIf)


def test_scxml_elseif_constructor_exists():
    assert callable(scxml_ElseIf.__init__)


def test_scxml_elseif_constructor_args():
    sig = inspect.signature(scxml_ElseIf.__init__)
    params = list(sig.parameters.keys())
    assert "cond" in params, "Missing parameter 'cond'"

def test_scxml_elseif_has_cond():
    assert hasattr(scxml_ElseIf, "cond")
    descriptor = None
    for klass in scxml_ElseIf.__mro__:
        if "cond" in klass.__dict__:
            descriptor = klass.__dict__["cond"]
            break
    assert isinstance(descriptor, property)



def test_scxml_validate_is_not_abstract():
    assert not inspect.isabstract(scxml_Validate)


def test_scxml_validate_constructor_exists():
    assert callable(scxml_Validate.__init__)


def test_scxml_validate_constructor_args():
    sig = inspect.signature(scxml_Validate.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "schema" in params, "Missing parameter 'schema'"

def test_scxml_validate_has_location():
    assert hasattr(scxml_Validate, "location")
    descriptor = None
    for klass in scxml_Validate.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_scxml_validate_has_schema():
    assert hasattr(scxml_Validate, "schema")
    descriptor = None
    for klass in scxml_Validate.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)



def test_scxml_send_is_not_abstract():
    assert not inspect.isabstract(scxml_Send)


def test_scxml_send_constructor_exists():
    assert callable(scxml_Send.__init__)


def test_scxml_send_constructor_args():
    sig = inspect.signature(scxml_Send.__init__)
    params = list(sig.parameters.keys())
    assert "delay" in params, "Missing parameter 'delay'"
    assert "targetexpr" in params, "Missing parameter 'targetexpr'"
    assert "type" in params, "Missing parameter 'type'"
    assert "idlocation" in params, "Missing parameter 'idlocation'"
    assert "namelist" in params, "Missing parameter 'namelist'"
    assert "target" in params, "Missing parameter 'target'"
    assert "id" in params, "Missing parameter 'id'"
    assert "hintsexpr" in params, "Missing parameter 'hintsexpr'"
    assert "hints" in params, "Missing parameter 'hints'"
    assert "event" in params, "Missing parameter 'event'"
    assert "eventexpr" in params, "Missing parameter 'eventexpr'"
    assert "typeexpr" in params, "Missing parameter 'typeexpr'"
    assert "delayexpr" in params, "Missing parameter 'delayexpr'"

def test_scxml_send_has_delay():
    assert hasattr(scxml_Send, "delay")
    descriptor = None
    for klass in scxml_Send.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)

def test_scxml_send_has_targetexpr():
    assert hasattr(scxml_Send, "targetexpr")
    descriptor = None
    for klass in scxml_Send.__mro__:
        if "targetexpr" in klass.__dict__:
            descriptor = klass.__dict__["targetexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_send_has_type():
    assert hasattr(scxml_Send, "type")
    descriptor = None
    for klass in scxml_Send.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scxml_send_has_idlocation():
    assert hasattr(scxml_Send, "idlocation")
    descriptor = None
    for klass in scxml_Send.__mro__:
        if "idlocation" in klass.__dict__:
            descriptor = klass.__dict__["idlocation"]
            break
    assert isinstance(descriptor, property)

def test_scxml_send_has_namelist():
    assert hasattr(scxml_Send, "namelist")
    descriptor = None
    for klass in scxml_Send.__mro__:
        if "namelist" in klass.__dict__:
            descriptor = klass.__dict__["namelist"]
            break
    assert isinstance(descriptor, property)

def test_scxml_send_has_target():
    assert hasattr(scxml_Send, "target")
    descriptor = None
    for klass in scxml_Send.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_scxml_send_has_id():
    assert hasattr(scxml_Send, "id")
    descriptor = None
    for klass in scxml_Send.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml_send_has_hintsexpr():
    assert hasattr(scxml_Send, "hintsexpr")
    descriptor = None
    for klass in scxml_Send.__mro__:
        if "hintsexpr" in klass.__dict__:
            descriptor = klass.__dict__["hintsexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_send_has_hints():
    assert hasattr(scxml_Send, "hints")
    descriptor = None
    for klass in scxml_Send.__mro__:
        if "hints" in klass.__dict__:
            descriptor = klass.__dict__["hints"]
            break
    assert isinstance(descriptor, property)

def test_scxml_send_has_event():
    assert hasattr(scxml_Send, "event")
    descriptor = None
    for klass in scxml_Send.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_scxml_send_has_eventexpr():
    assert hasattr(scxml_Send, "eventexpr")
    descriptor = None
    for klass in scxml_Send.__mro__:
        if "eventexpr" in klass.__dict__:
            descriptor = klass.__dict__["eventexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_send_has_typeexpr():
    assert hasattr(scxml_Send, "typeexpr")
    descriptor = None
    for klass in scxml_Send.__mro__:
        if "typeexpr" in klass.__dict__:
            descriptor = klass.__dict__["typeexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_send_has_delayexpr():
    assert hasattr(scxml_Send, "delayexpr")
    descriptor = None
    for klass in scxml_Send.__mro__:
        if "delayexpr" in klass.__dict__:
            descriptor = klass.__dict__["delayexpr"]
            break
    assert isinstance(descriptor, property)



def test_scxml_raise_is_not_abstract():
    assert not inspect.isabstract(scxml_Raise)


def test_scxml_raise_constructor_exists():
    assert callable(scxml_Raise.__init__)


def test_scxml_raise_constructor_args():
    sig = inspect.signature(scxml_Raise.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_scxml_raise_has_event():
    assert hasattr(scxml_Raise, "event")
    descriptor = None
    for klass in scxml_Raise.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_scxml_param_is_not_abstract():
    assert not inspect.isabstract(scxml_Param)


def test_scxml_param_constructor_exists():
    assert callable(scxml_Param.__init__)


def test_scxml_param_constructor_args():
    sig = inspect.signature(scxml_Param.__init__)
    params = list(sig.parameters.keys())
    assert "expr" in params, "Missing parameter 'expr'"
    assert "name" in params, "Missing parameter 'name'"

def test_scxml_param_has_expr():
    assert hasattr(scxml_Param, "expr")
    descriptor = None
    for klass in scxml_Param.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_param_has_name():
    assert hasattr(scxml_Param, "name")
    descriptor = None
    for klass in scxml_Param.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_scxml_log_is_not_abstract():
    assert not inspect.isabstract(scxml_Log)


def test_scxml_log_constructor_exists():
    assert callable(scxml_Log.__init__)


def test_scxml_log_constructor_args():
    sig = inspect.signature(scxml_Log.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "label" in params, "Missing parameter 'label'"

def test_scxml_log_has_level():
    assert hasattr(scxml_Log, "level")
    descriptor = None
    for klass in scxml_Log.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_scxml_log_has_expr():
    assert hasattr(scxml_Log, "expr")
    descriptor = None
    for klass in scxml_Log.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_log_has_label():
    assert hasattr(scxml_Log, "label")
    descriptor = None
    for klass in scxml_Log.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_scxml_if_is_not_abstract():
    assert not inspect.isabstract(scxml_If)


def test_scxml_if_constructor_exists():
    assert callable(scxml_If.__init__)


def test_scxml_if_constructor_args():
    sig = inspect.signature(scxml_If.__init__)
    params = list(sig.parameters.keys())
    assert "cond" in params, "Missing parameter 'cond'"

def test_scxml_if_has_cond():
    assert hasattr(scxml_If, "cond")
    descriptor = None
    for klass in scxml_If.__mro__:
        if "cond" in klass.__dict__:
            descriptor = klass.__dict__["cond"]
            break
    assert isinstance(descriptor, property)



def test_scxml_donedata_is_not_abstract():
    assert not inspect.isabstract(scxml_Donedata)


def test_scxml_donedata_constructor_exists():
    assert callable(scxml_Donedata.__init__)


def test_scxml_donedata_constructor_args():
    sig = inspect.signature(scxml_Donedata.__init__)
    params = list(sig.parameters.keys())



def test_scxml_servicetemplate_is_not_abstract():
    assert not inspect.isabstract(scxml_ServiceTemplate)


def test_scxml_servicetemplate_constructor_exists():
    assert callable(scxml_ServiceTemplate.__init__)


def test_scxml_servicetemplate_constructor_args():
    sig = inspect.signature(scxml_ServiceTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"
    assert "profile" in params, "Missing parameter 'profile'"
    assert "exmode" in params, "Missing parameter 'exmode'"
    assert "xmlns" in params, "Missing parameter 'xmlns'"

def test_scxml_servicetemplate_has_name():
    assert hasattr(scxml_ServiceTemplate, "name")
    descriptor = None
    for klass in scxml_ServiceTemplate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_scxml_servicetemplate_has_version():
    assert hasattr(scxml_ServiceTemplate, "version")
    descriptor = None
    for klass in scxml_ServiceTemplate.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_scxml_servicetemplate_has_profile():
    assert hasattr(scxml_ServiceTemplate, "profile")
    descriptor = None
    for klass in scxml_ServiceTemplate.__mro__:
        if "profile" in klass.__dict__:
            descriptor = klass.__dict__["profile"]
            break
    assert isinstance(descriptor, property)

def test_scxml_servicetemplate_has_exmode():
    assert hasattr(scxml_ServiceTemplate, "exmode")
    descriptor = None
    for klass in scxml_ServiceTemplate.__mro__:
        if "exmode" in klass.__dict__:
            descriptor = klass.__dict__["exmode"]
            break
    assert isinstance(descriptor, property)

def test_scxml_servicetemplate_has_xmlns():
    assert hasattr(scxml_ServiceTemplate, "xmlns")
    descriptor = None
    for klass in scxml_ServiceTemplate.__mro__:
        if "xmlns" in klass.__dict__:
            descriptor = klass.__dict__["xmlns"]
            break
    assert isinstance(descriptor, property)



def test_scxml_assign_is_not_abstract():
    assert not inspect.isabstract(scxml_Assign)


def test_scxml_assign_constructor_exists():
    assert callable(scxml_Assign.__init__)


def test_scxml_assign_constructor_args():
    sig = inspect.signature(scxml_Assign.__init__)
    params = list(sig.parameters.keys())
    assert "dataid" in params, "Missing parameter 'dataid'"
    assert "location" in params, "Missing parameter 'location'"
    assert "expr" in params, "Missing parameter 'expr'"

def test_scxml_assign_has_dataid():
    assert hasattr(scxml_Assign, "dataid")
    descriptor = None
    for klass in scxml_Assign.__mro__:
        if "dataid" in klass.__dict__:
            descriptor = klass.__dict__["dataid"]
            break
    assert isinstance(descriptor, property)

def test_scxml_assign_has_location():
    assert hasattr(scxml_Assign, "location")
    descriptor = None
    for klass in scxml_Assign.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_scxml_assign_has_expr():
    assert hasattr(scxml_Assign, "expr")
    descriptor = None
    for klass in scxml_Assign.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)



def test_scxml_invoke_is_not_abstract():
    assert not inspect.isabstract(scxml_Invoke)


def test_scxml_invoke_constructor_exists():
    assert callable(scxml_Invoke.__init__)


def test_scxml_invoke_constructor_args():
    sig = inspect.signature(scxml_Invoke.__init__)
    params = list(sig.parameters.keys())
    assert "srcexpr" in params, "Missing parameter 'srcexpr'"
    assert "src" in params, "Missing parameter 'src'"
    assert "idlocation" in params, "Missing parameter 'idlocation'"
    assert "type" in params, "Missing parameter 'type'"
    assert "namelist" in params, "Missing parameter 'namelist'"
    assert "id" in params, "Missing parameter 'id'"
    assert "typeexpr" in params, "Missing parameter 'typeexpr'"
    assert "autoforward" in params, "Missing parameter 'autoforward'"

def test_scxml_invoke_has_srcexpr():
    assert hasattr(scxml_Invoke, "srcexpr")
    descriptor = None
    for klass in scxml_Invoke.__mro__:
        if "srcexpr" in klass.__dict__:
            descriptor = klass.__dict__["srcexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_invoke_has_src():
    assert hasattr(scxml_Invoke, "src")
    descriptor = None
    for klass in scxml_Invoke.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_scxml_invoke_has_idlocation():
    assert hasattr(scxml_Invoke, "idlocation")
    descriptor = None
    for klass in scxml_Invoke.__mro__:
        if "idlocation" in klass.__dict__:
            descriptor = klass.__dict__["idlocation"]
            break
    assert isinstance(descriptor, property)

def test_scxml_invoke_has_type():
    assert hasattr(scxml_Invoke, "type")
    descriptor = None
    for klass in scxml_Invoke.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scxml_invoke_has_namelist():
    assert hasattr(scxml_Invoke, "namelist")
    descriptor = None
    for klass in scxml_Invoke.__mro__:
        if "namelist" in klass.__dict__:
            descriptor = klass.__dict__["namelist"]
            break
    assert isinstance(descriptor, property)

def test_scxml_invoke_has_id():
    assert hasattr(scxml_Invoke, "id")
    descriptor = None
    for klass in scxml_Invoke.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml_invoke_has_typeexpr():
    assert hasattr(scxml_Invoke, "typeexpr")
    descriptor = None
    for klass in scxml_Invoke.__mro__:
        if "typeexpr" in klass.__dict__:
            descriptor = klass.__dict__["typeexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_invoke_has_autoforward():
    assert hasattr(scxml_Invoke, "autoforward")
    descriptor = None
    for klass in scxml_Invoke.__mro__:
        if "autoforward" in klass.__dict__:
            descriptor = klass.__dict__["autoforward"]
            break
    assert isinstance(descriptor, property)



def test_scxml_anchor_is_not_abstract():
    assert not inspect.isabstract(scxml_Anchor)


def test_scxml_anchor_constructor_exists():
    assert callable(scxml_Anchor.__init__)


def test_scxml_anchor_constructor_args():
    sig = inspect.signature(scxml_Anchor.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "snapshot" in params, "Missing parameter 'snapshot'"

def test_scxml_anchor_has_type():
    assert hasattr(scxml_Anchor, "type")
    descriptor = None
    for klass in scxml_Anchor.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scxml_anchor_has_snapshot():
    assert hasattr(scxml_Anchor, "snapshot")
    descriptor = None
    for klass in scxml_Anchor.__mro__:
        if "snapshot" in klass.__dict__:
            descriptor = klass.__dict__["snapshot"]
            break
    assert isinstance(descriptor, property)



def test_scxml_cancel_is_not_abstract():
    assert not inspect.isabstract(scxml_Cancel)


def test_scxml_cancel_constructor_exists():
    assert callable(scxml_Cancel.__init__)


def test_scxml_cancel_constructor_args():
    sig = inspect.signature(scxml_Cancel.__init__)
    params = list(sig.parameters.keys())
    assert "sendidexpr" in params, "Missing parameter 'sendidexpr'"
    assert "sendid" in params, "Missing parameter 'sendid'"

def test_scxml_cancel_has_sendidexpr():
    assert hasattr(scxml_Cancel, "sendidexpr")
    descriptor = None
    for klass in scxml_Cancel.__mro__:
        if "sendidexpr" in klass.__dict__:
            descriptor = klass.__dict__["sendidexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_cancel_has_sendid():
    assert hasattr(scxml_Cancel, "sendid")
    descriptor = None
    for klass in scxml_Cancel.__mro__:
        if "sendid" in klass.__dict__:
            descriptor = klass.__dict__["sendid"]
            break
    assert isinstance(descriptor, property)



def test_scxml_script_is_not_abstract():
    assert not inspect.isabstract(scxml_Script)


def test_scxml_script_constructor_exists():
    assert callable(scxml_Script.__init__)


def test_scxml_script_constructor_args():
    sig = inspect.signature(scxml_Script.__init__)
    params = list(sig.parameters.keys())



def test_scxml_onexit_is_not_abstract():
    assert not inspect.isabstract(scxml_OnExit)


def test_scxml_onexit_constructor_exists():
    assert callable(scxml_OnExit.__init__)


def test_scxml_onexit_constructor_args():
    sig = inspect.signature(scxml_OnExit.__init__)
    params = list(sig.parameters.keys())



def test_scxml_onentry_is_not_abstract():
    assert not inspect.isabstract(scxml_OnEntry)


def test_scxml_onentry_constructor_exists():
    assert callable(scxml_OnEntry.__init__)


def test_scxml_onentry_constructor_args():
    sig = inspect.signature(scxml_OnEntry.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_scxml_parallel_is_not_abstract():
    assert not inspect.isabstract(scxml_Parallel)


def test_scxml_parallel_constructor_exists():
    assert callable(scxml_Parallel.__init__)


def test_scxml_parallel_constructor_args():
    sig = inspect.signature(scxml_Parallel.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_scxml_parallel_has_id():
    assert hasattr(scxml_Parallel, "id")
    descriptor = None
    for klass in scxml_Parallel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_scxml_initialstate_is_not_abstract():
    assert not inspect.isabstract(scxml_InitialState)


def test_scxml_initialstate_constructor_exists():
    assert callable(scxml_InitialState.__init__)


def test_scxml_initialstate_constructor_args():
    sig = inspect.signature(scxml_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_scxml_historystate_is_not_abstract():
    assert not inspect.isabstract(scxml_HistoryState)


def test_scxml_historystate_constructor_exists():
    assert callable(scxml_HistoryState.__init__)


def test_scxml_historystate_constructor_args():
    sig = inspect.signature(scxml_HistoryState.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"

def test_scxml_historystate_has_id():
    assert hasattr(scxml_HistoryState, "id")
    descriptor = None
    for klass in scxml_HistoryState.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml_historystate_has_type():
    assert hasattr(scxml_HistoryState, "type")
    descriptor = None
    for klass in scxml_HistoryState.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_scxml_finalstate_is_not_abstract():
    assert not inspect.isabstract(scxml_FinalState)


def test_scxml_finalstate_constructor_exists():
    assert callable(scxml_FinalState.__init__)


def test_scxml_finalstate_constructor_args():
    sig = inspect.signature(scxml_FinalState.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_scxml_finalstate_has_id():
    assert hasattr(scxml_FinalState, "id")
    descriptor = None
    for klass in scxml_FinalState.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_scxml_state_is_not_abstract():
    assert not inspect.isabstract(scxml_State)


def test_scxml_state_constructor_exists():
    assert callable(scxml_State.__init__)


def test_scxml_state_constructor_args():
    sig = inspect.signature(scxml_State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_scxml_state_has_id():
    assert hasattr(scxml_State, "id")
    descriptor = None
    for klass in scxml_State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_scxml_transition_is_not_abstract():
    assert not inspect.isabstract(scxml_Transition)


def test_scxml_transition_constructor_exists():
    assert callable(scxml_Transition.__init__)


def test_scxml_transition_constructor_args():
    sig = inspect.signature(scxml_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "anchor" in params, "Missing parameter 'anchor'"
    assert "cond" in params, "Missing parameter 'cond'"

def test_scxml_transition_has_event():
    assert hasattr(scxml_Transition, "event")
    descriptor = None
    for klass in scxml_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_scxml_transition_has_anchor():
    assert hasattr(scxml_Transition, "anchor")
    descriptor = None
    for klass in scxml_Transition.__mro__:
        if "anchor" in klass.__dict__:
            descriptor = klass.__dict__["anchor"]
            break
    assert isinstance(descriptor, property)

def test_scxml_transition_has_cond():
    assert hasattr(scxml_Transition, "cond")
    descriptor = None
    for klass in scxml_Transition.__mro__:
        if "cond" in klass.__dict__:
            descriptor = klass.__dict__["cond"]
            break
    assert isinstance(descriptor, property)



def test_scxml_datamodel_is_not_abstract():
    assert not inspect.isabstract(scxml_DataModel)


def test_scxml_datamodel_constructor_exists():
    assert callable(scxml_DataModel.__init__)


def test_scxml_datamodel_constructor_args():
    sig = inspect.signature(scxml_DataModel.__init__)
    params = list(sig.parameters.keys())
    assert "schema" in params, "Missing parameter 'schema'"

def test_scxml_datamodel_has_schema():
    assert hasattr(scxml_DataModel, "schema")
    descriptor = None
    for klass in scxml_DataModel.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)



def test_scxml_namedelement_is_not_abstract():
    assert not inspect.isabstract(scxml_NamedElement)


def test_scxml_namedelement_constructor_exists():
    assert callable(scxml_NamedElement.__init__)


def test_scxml_namedelement_constructor_args():
    sig = inspect.signature(scxml_NamedElement.__init__)
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
scxml_Finalize_strategy = st.builds(
    scxml_Finalize,
)
scxml_Data_strategy = st.builds(
    scxml_Data,
    src=
        safe_text,
    expr=
        safe_text,
    id=
        safe_text
)
scxml_Content_strategy = st.builds(
    scxml_Content,
)
scxml_Else_strategy = st.builds(
    scxml_Else,
)
scxml_ElseIf_strategy = st.builds(
    scxml_ElseIf,
    cond=
        safe_text
)
scxml_Validate_strategy = st.builds(
    scxml_Validate,
    location=
        safe_text,
    schema=
        safe_text
)
scxml_Send_strategy = st.builds(
    scxml_Send,
    delay=
        safe_text,
    targetexpr=
        safe_text,
    type=
        safe_text,
    idlocation=
        safe_text,
    namelist=
        safe_text,
    target=
        safe_text,
    id=
        safe_text,
    hintsexpr=
        safe_text,
    hints=
        safe_text,
    event=
        safe_text,
    eventexpr=
        safe_text,
    typeexpr=
        safe_text,
    delayexpr=
        safe_text
)
scxml_Raise_strategy = st.builds(
    scxml_Raise,
    event=
        safe_text
)
scxml_Param_strategy = st.builds(
    scxml_Param,
    expr=
        safe_text,
    name=
        safe_text
)
scxml_Log_strategy = st.builds(
    scxml_Log,
    level=
        safe_text,
    expr=
        safe_text,
    label=
        safe_text
)
scxml_If_strategy = st.builds(
    scxml_If,
    cond=
        safe_text
)
scxml_Donedata_strategy = st.builds(
    scxml_Donedata,
)
scxml_ServiceTemplate_strategy = st.builds(
    scxml_ServiceTemplate,
    name=
        safe_text,
    version=
        safe_text,
    profile=
        safe_text,
    exmode=
        safe_text,
    xmlns=
        safe_text
)
scxml_Assign_strategy = st.builds(
    scxml_Assign,
    dataid=
        safe_text,
    location=
        safe_text,
    expr=
        safe_text
)
scxml_Invoke_strategy = st.builds(
    scxml_Invoke,
    srcexpr=
        safe_text,
    src=
        safe_text,
    idlocation=
        safe_text,
    type=
        safe_text,
    namelist=
        safe_text,
    id=
        safe_text,
    typeexpr=
        safe_text,
    autoforward=
        safe_text
)
scxml_Anchor_strategy = st.builds(
    scxml_Anchor,
    type=
        safe_text,
    snapshot=
        safe_text
)
scxml_Cancel_strategy = st.builds(
    scxml_Cancel,
    sendidexpr=
        safe_text,
    sendid=
        safe_text
)
scxml_Script_strategy = st.builds(
    scxml_Script,
)
scxml_OnExit_strategy = st.builds(
    scxml_OnExit,
)
scxml_OnEntry_strategy = st.builds(
    scxml_OnEntry,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
scxml_Parallel_strategy = st.builds(
    scxml_Parallel,
    id=
        safe_text
)
scxml_InitialState_strategy = st.builds(
    scxml_InitialState,
)
scxml_HistoryState_strategy = st.builds(
    scxml_HistoryState,
    id=
        safe_text,
    type=
        safe_text
)
scxml_FinalState_strategy = st.builds(
    scxml_FinalState,
    id=
        safe_text
)
scxml_State_strategy = st.builds(
    scxml_State,
    id=
        safe_text
)
scxml_Transition_strategy = st.builds(
    scxml_Transition,
    event=
        safe_text,
    anchor=
        safe_text,
    cond=
        safe_text
)
scxml_DataModel_strategy = st.builds(
    scxml_DataModel,
    schema=
        safe_text
)
scxml_NamedElement_strategy = st.builds(
    scxml_NamedElement,
)

@given(instance=scxml_Finalize_strategy)
@settings(max_examples=50)
def test_scxml_finalize_instantiation(instance):
    assert isinstance(instance, scxml_Finalize)

@given(instance=scxml_Data_strategy)
@settings(max_examples=50)
def test_scxml_data_instantiation(instance):
    assert isinstance(instance, scxml_Data)



@given(instance=scxml_Data_strategy)
def test_scxml_data_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=scxml_Data_strategy)
def test_scxml_data_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original



@given(instance=scxml_Data_strategy)
def test_scxml_data_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml_Content_strategy)
@settings(max_examples=50)
def test_scxml_content_instantiation(instance):
    assert isinstance(instance, scxml_Content)

@given(instance=scxml_Else_strategy)
@settings(max_examples=50)
def test_scxml_else_instantiation(instance):
    assert isinstance(instance, scxml_Else)

@given(instance=scxml_ElseIf_strategy)
@settings(max_examples=50)
def test_scxml_elseif_instantiation(instance):
    assert isinstance(instance, scxml_ElseIf)



@given(instance=scxml_ElseIf_strategy)
def test_scxml_elseif_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original

@given(instance=scxml_Validate_strategy)
@settings(max_examples=50)
def test_scxml_validate_instantiation(instance):
    assert isinstance(instance, scxml_Validate)



@given(instance=scxml_Validate_strategy)
def test_scxml_validate_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=scxml_Validate_strategy)
def test_scxml_validate_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original

@given(instance=scxml_Send_strategy)
@settings(max_examples=50)
def test_scxml_send_instantiation(instance):
    assert isinstance(instance, scxml_Send)



@given(instance=scxml_Send_strategy)
def test_scxml_send_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original



@given(instance=scxml_Send_strategy)
def test_scxml_send_targetexpr_setter(instance):
    original = instance.targetexpr
    instance.targetexpr = original
    assert instance.targetexpr == original



@given(instance=scxml_Send_strategy)
def test_scxml_send_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=scxml_Send_strategy)
def test_scxml_send_idlocation_setter(instance):
    original = instance.idlocation
    instance.idlocation = original
    assert instance.idlocation == original



@given(instance=scxml_Send_strategy)
def test_scxml_send_namelist_setter(instance):
    original = instance.namelist
    instance.namelist = original
    assert instance.namelist == original



@given(instance=scxml_Send_strategy)
def test_scxml_send_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=scxml_Send_strategy)
def test_scxml_send_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scxml_Send_strategy)
def test_scxml_send_hintsexpr_setter(instance):
    original = instance.hintsexpr
    instance.hintsexpr = original
    assert instance.hintsexpr == original



@given(instance=scxml_Send_strategy)
def test_scxml_send_hints_setter(instance):
    original = instance.hints
    instance.hints = original
    assert instance.hints == original



@given(instance=scxml_Send_strategy)
def test_scxml_send_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=scxml_Send_strategy)
def test_scxml_send_eventexpr_setter(instance):
    original = instance.eventexpr
    instance.eventexpr = original
    assert instance.eventexpr == original



@given(instance=scxml_Send_strategy)
def test_scxml_send_typeexpr_setter(instance):
    original = instance.typeexpr
    instance.typeexpr = original
    assert instance.typeexpr == original



@given(instance=scxml_Send_strategy)
def test_scxml_send_delayexpr_setter(instance):
    original = instance.delayexpr
    instance.delayexpr = original
    assert instance.delayexpr == original

@given(instance=scxml_Raise_strategy)
@settings(max_examples=50)
def test_scxml_raise_instantiation(instance):
    assert isinstance(instance, scxml_Raise)



@given(instance=scxml_Raise_strategy)
def test_scxml_raise_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=scxml_Param_strategy)
@settings(max_examples=50)
def test_scxml_param_instantiation(instance):
    assert isinstance(instance, scxml_Param)



@given(instance=scxml_Param_strategy)
def test_scxml_param_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original



@given(instance=scxml_Param_strategy)
def test_scxml_param_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scxml_Log_strategy)
@settings(max_examples=50)
def test_scxml_log_instantiation(instance):
    assert isinstance(instance, scxml_Log)



@given(instance=scxml_Log_strategy)
def test_scxml_log_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=scxml_Log_strategy)
def test_scxml_log_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original



@given(instance=scxml_Log_strategy)
def test_scxml_log_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=scxml_If_strategy)
@settings(max_examples=50)
def test_scxml_if_instantiation(instance):
    assert isinstance(instance, scxml_If)



@given(instance=scxml_If_strategy)
def test_scxml_if_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original

@given(instance=scxml_Donedata_strategy)
@settings(max_examples=50)
def test_scxml_donedata_instantiation(instance):
    assert isinstance(instance, scxml_Donedata)

@given(instance=scxml_ServiceTemplate_strategy)
@settings(max_examples=50)
def test_scxml_servicetemplate_instantiation(instance):
    assert isinstance(instance, scxml_ServiceTemplate)



@given(instance=scxml_ServiceTemplate_strategy)
def test_scxml_servicetemplate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=scxml_ServiceTemplate_strategy)
def test_scxml_servicetemplate_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=scxml_ServiceTemplate_strategy)
def test_scxml_servicetemplate_profile_setter(instance):
    original = instance.profile
    instance.profile = original
    assert instance.profile == original



@given(instance=scxml_ServiceTemplate_strategy)
def test_scxml_servicetemplate_exmode_setter(instance):
    original = instance.exmode
    instance.exmode = original
    assert instance.exmode == original



@given(instance=scxml_ServiceTemplate_strategy)
def test_scxml_servicetemplate_xmlns_setter(instance):
    original = instance.xmlns
    instance.xmlns = original
    assert instance.xmlns == original

@given(instance=scxml_Assign_strategy)
@settings(max_examples=50)
def test_scxml_assign_instantiation(instance):
    assert isinstance(instance, scxml_Assign)



@given(instance=scxml_Assign_strategy)
def test_scxml_assign_dataid_setter(instance):
    original = instance.dataid
    instance.dataid = original
    assert instance.dataid == original



@given(instance=scxml_Assign_strategy)
def test_scxml_assign_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=scxml_Assign_strategy)
def test_scxml_assign_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=scxml_Invoke_strategy)
@settings(max_examples=50)
def test_scxml_invoke_instantiation(instance):
    assert isinstance(instance, scxml_Invoke)



@given(instance=scxml_Invoke_strategy)
def test_scxml_invoke_srcexpr_setter(instance):
    original = instance.srcexpr
    instance.srcexpr = original
    assert instance.srcexpr == original



@given(instance=scxml_Invoke_strategy)
def test_scxml_invoke_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=scxml_Invoke_strategy)
def test_scxml_invoke_idlocation_setter(instance):
    original = instance.idlocation
    instance.idlocation = original
    assert instance.idlocation == original



@given(instance=scxml_Invoke_strategy)
def test_scxml_invoke_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=scxml_Invoke_strategy)
def test_scxml_invoke_namelist_setter(instance):
    original = instance.namelist
    instance.namelist = original
    assert instance.namelist == original



@given(instance=scxml_Invoke_strategy)
def test_scxml_invoke_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scxml_Invoke_strategy)
def test_scxml_invoke_typeexpr_setter(instance):
    original = instance.typeexpr
    instance.typeexpr = original
    assert instance.typeexpr == original



@given(instance=scxml_Invoke_strategy)
def test_scxml_invoke_autoforward_setter(instance):
    original = instance.autoforward
    instance.autoforward = original
    assert instance.autoforward == original

@given(instance=scxml_Anchor_strategy)
@settings(max_examples=50)
def test_scxml_anchor_instantiation(instance):
    assert isinstance(instance, scxml_Anchor)



@given(instance=scxml_Anchor_strategy)
def test_scxml_anchor_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=scxml_Anchor_strategy)
def test_scxml_anchor_snapshot_setter(instance):
    original = instance.snapshot
    instance.snapshot = original
    assert instance.snapshot == original

@given(instance=scxml_Cancel_strategy)
@settings(max_examples=50)
def test_scxml_cancel_instantiation(instance):
    assert isinstance(instance, scxml_Cancel)



@given(instance=scxml_Cancel_strategy)
def test_scxml_cancel_sendidexpr_setter(instance):
    original = instance.sendidexpr
    instance.sendidexpr = original
    assert instance.sendidexpr == original



@given(instance=scxml_Cancel_strategy)
def test_scxml_cancel_sendid_setter(instance):
    original = instance.sendid
    instance.sendid = original
    assert instance.sendid == original

@given(instance=scxml_Script_strategy)
@settings(max_examples=50)
def test_scxml_script_instantiation(instance):
    assert isinstance(instance, scxml_Script)

@given(instance=scxml_OnExit_strategy)
@settings(max_examples=50)
def test_scxml_onexit_instantiation(instance):
    assert isinstance(instance, scxml_OnExit)

@given(instance=scxml_OnEntry_strategy)
@settings(max_examples=50)
def test_scxml_onentry_instantiation(instance):
    assert isinstance(instance, scxml_OnEntry)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=scxml_Parallel_strategy)
@settings(max_examples=50)
def test_scxml_parallel_instantiation(instance):
    assert isinstance(instance, scxml_Parallel)



@given(instance=scxml_Parallel_strategy)
def test_scxml_parallel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml_InitialState_strategy)
@settings(max_examples=50)
def test_scxml_initialstate_instantiation(instance):
    assert isinstance(instance, scxml_InitialState)

@given(instance=scxml_HistoryState_strategy)
@settings(max_examples=50)
def test_scxml_historystate_instantiation(instance):
    assert isinstance(instance, scxml_HistoryState)



@given(instance=scxml_HistoryState_strategy)
def test_scxml_historystate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scxml_HistoryState_strategy)
def test_scxml_historystate_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scxml_FinalState_strategy)
@settings(max_examples=50)
def test_scxml_finalstate_instantiation(instance):
    assert isinstance(instance, scxml_FinalState)



@given(instance=scxml_FinalState_strategy)
def test_scxml_finalstate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml_State_strategy)
@settings(max_examples=50)
def test_scxml_state_instantiation(instance):
    assert isinstance(instance, scxml_State)



@given(instance=scxml_State_strategy)
def test_scxml_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml_Transition_strategy)
@settings(max_examples=50)
def test_scxml_transition_instantiation(instance):
    assert isinstance(instance, scxml_Transition)



@given(instance=scxml_Transition_strategy)
def test_scxml_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=scxml_Transition_strategy)
def test_scxml_transition_anchor_setter(instance):
    original = instance.anchor
    instance.anchor = original
    assert instance.anchor == original



@given(instance=scxml_Transition_strategy)
def test_scxml_transition_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original

@given(instance=scxml_DataModel_strategy)
@settings(max_examples=50)
def test_scxml_datamodel_instantiation(instance):
    assert isinstance(instance, scxml_DataModel)



@given(instance=scxml_DataModel_strategy)
def test_scxml_datamodel_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original

@given(instance=scxml_NamedElement_strategy)
@settings(max_examples=50)
def test_scxml_namedelement_instantiation(instance):
    assert isinstance(instance, scxml_NamedElement)
