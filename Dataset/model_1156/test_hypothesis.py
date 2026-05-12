import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    td1_Program,
    td1_Component,
    td1_DataType,
    td1_Action,
    td1_Guard,
    td1_Trigger,
    td1_Port,
    td1_Variable,
    td1_Transition,
    td1_State,
    td1_Process,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_td1_program_is_not_abstract():
    assert not inspect.isabstract(td1_Program)


def test_td1_program_constructor_exists():
    assert callable(td1_Program.__init__)


def test_td1_program_constructor_args():
    sig = inspect.signature(td1_Program.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ComponentSize" in params, "Missing parameter 'ComponentSize'"

def test_td1_program_has_Name():
    assert hasattr(td1_Program, "Name")
    descriptor = None
    for klass in td1_Program.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_td1_program_has_ComponentSize():
    assert hasattr(td1_Program, "ComponentSize")
    descriptor = None
    for klass in td1_Program.__mro__:
        if "ComponentSize" in klass.__dict__:
            descriptor = klass.__dict__["ComponentSize"]
            break
    assert isinstance(descriptor, property)



def test_td1_component_is_not_abstract():
    assert not inspect.isabstract(td1_Component)


def test_td1_component_constructor_exists():
    assert callable(td1_Component.__init__)


def test_td1_component_constructor_args():
    sig = inspect.signature(td1_Component.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ProcessSize" in params, "Missing parameter 'ProcessSize'"
    assert "VarSize" in params, "Missing parameter 'VarSize'"

def test_td1_component_has_Name():
    assert hasattr(td1_Component, "Name")
    descriptor = None
    for klass in td1_Component.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_td1_component_has_ProcessSize():
    assert hasattr(td1_Component, "ProcessSize")
    descriptor = None
    for klass in td1_Component.__mro__:
        if "ProcessSize" in klass.__dict__:
            descriptor = klass.__dict__["ProcessSize"]
            break
    assert isinstance(descriptor, property)

def test_td1_component_has_VarSize():
    assert hasattr(td1_Component, "VarSize")
    descriptor = None
    for klass in td1_Component.__mro__:
        if "VarSize" in klass.__dict__:
            descriptor = klass.__dict__["VarSize"]
            break
    assert isinstance(descriptor, property)



def test_td1_datatype_is_not_abstract():
    assert not inspect.isabstract(td1_DataType)


def test_td1_datatype_constructor_exists():
    assert callable(td1_DataType.__init__)


def test_td1_datatype_constructor_args():
    sig = inspect.signature(td1_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1_datatype_has_Name():
    assert hasattr(td1_DataType, "Name")
    descriptor = None
    for klass in td1_DataType.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_td1_action_is_not_abstract():
    assert not inspect.isabstract(td1_Action)


def test_td1_action_constructor_exists():
    assert callable(td1_Action.__init__)


def test_td1_action_constructor_args():
    sig = inspect.signature(td1_Action.__init__)
    params = list(sig.parameters.keys())
    assert "codeFiacre" in params, "Missing parameter 'codeFiacre'"
    assert "Body" in params, "Missing parameter 'Body'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1_action_has_codeFiacre():
    assert hasattr(td1_Action, "codeFiacre")
    descriptor = None
    for klass in td1_Action.__mro__:
        if "codeFiacre" in klass.__dict__:
            descriptor = klass.__dict__["codeFiacre"]
            break
    assert isinstance(descriptor, property)

def test_td1_action_has_Body():
    assert hasattr(td1_Action, "Body")
    descriptor = None
    for klass in td1_Action.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)

def test_td1_action_has_Name():
    assert hasattr(td1_Action, "Name")
    descriptor = None
    for klass in td1_Action.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_td1_guard_is_not_abstract():
    assert not inspect.isabstract(td1_Guard)


def test_td1_guard_constructor_exists():
    assert callable(td1_Guard.__init__)


def test_td1_guard_constructor_args():
    sig = inspect.signature(td1_Guard.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "codeFiacre" in params, "Missing parameter 'codeFiacre'"
    assert "Body" in params, "Missing parameter 'Body'"

def test_td1_guard_has_Name():
    assert hasattr(td1_Guard, "Name")
    descriptor = None
    for klass in td1_Guard.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_td1_guard_has_codeFiacre():
    assert hasattr(td1_Guard, "codeFiacre")
    descriptor = None
    for klass in td1_Guard.__mro__:
        if "codeFiacre" in klass.__dict__:
            descriptor = klass.__dict__["codeFiacre"]
            break
    assert isinstance(descriptor, property)

def test_td1_guard_has_Body():
    assert hasattr(td1_Guard, "Body")
    descriptor = None
    for klass in td1_Guard.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)



def test_td1_trigger_is_not_abstract():
    assert not inspect.isabstract(td1_Trigger)


def test_td1_trigger_constructor_exists():
    assert callable(td1_Trigger.__init__)


def test_td1_trigger_constructor_args():
    sig = inspect.signature(td1_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "codeFiacre" in params, "Missing parameter 'codeFiacre'"
    assert "Body" in params, "Missing parameter 'Body'"
    assert "ArgSize" in params, "Missing parameter 'ArgSize'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1_trigger_has_codeFiacre():
    assert hasattr(td1_Trigger, "codeFiacre")
    descriptor = None
    for klass in td1_Trigger.__mro__:
        if "codeFiacre" in klass.__dict__:
            descriptor = klass.__dict__["codeFiacre"]
            break
    assert isinstance(descriptor, property)

def test_td1_trigger_has_Body():
    assert hasattr(td1_Trigger, "Body")
    descriptor = None
    for klass in td1_Trigger.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)

def test_td1_trigger_has_ArgSize():
    assert hasattr(td1_Trigger, "ArgSize")
    descriptor = None
    for klass in td1_Trigger.__mro__:
        if "ArgSize" in klass.__dict__:
            descriptor = klass.__dict__["ArgSize"]
            break
    assert isinstance(descriptor, property)

def test_td1_trigger_has_Name():
    assert hasattr(td1_Trigger, "Name")
    descriptor = None
    for klass in td1_Trigger.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_td1_port_is_not_abstract():
    assert not inspect.isabstract(td1_Port)


def test_td1_port_constructor_exists():
    assert callable(td1_Port.__init__)


def test_td1_port_constructor_args():
    sig = inspect.signature(td1_Port.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1_port_has_Name():
    assert hasattr(td1_Port, "Name")
    descriptor = None
    for klass in td1_Port.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_td1_variable_is_not_abstract():
    assert not inspect.isabstract(td1_Variable)


def test_td1_variable_constructor_exists():
    assert callable(td1_Variable.__init__)


def test_td1_variable_constructor_args():
    sig = inspect.signature(td1_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "initVal" in params, "Missing parameter 'initVal'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1_variable_has_initVal():
    assert hasattr(td1_Variable, "initVal")
    descriptor = None
    for klass in td1_Variable.__mro__:
        if "initVal" in klass.__dict__:
            descriptor = klass.__dict__["initVal"]
            break
    assert isinstance(descriptor, property)

def test_td1_variable_has_Name():
    assert hasattr(td1_Variable, "Name")
    descriptor = None
    for klass in td1_Variable.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_td1_transition_is_not_abstract():
    assert not inspect.isabstract(td1_Transition)


def test_td1_transition_constructor_exists():
    assert callable(td1_Transition.__init__)


def test_td1_transition_constructor_args():
    sig = inspect.signature(td1_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1_transition_has_Name():
    assert hasattr(td1_Transition, "Name")
    descriptor = None
    for klass in td1_Transition.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_td1_state_is_not_abstract():
    assert not inspect.isabstract(td1_State)


def test_td1_state_constructor_exists():
    assert callable(td1_State.__init__)


def test_td1_state_constructor_args():
    sig = inspect.signature(td1_State.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1_state_has_Name():
    assert hasattr(td1_State, "Name")
    descriptor = None
    for klass in td1_State.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_td1_process_is_not_abstract():
    assert not inspect.isabstract(td1_Process)


def test_td1_process_constructor_exists():
    assert callable(td1_Process.__init__)


def test_td1_process_constructor_args():
    sig = inspect.signature(td1_Process.__init__)
    params = list(sig.parameters.keys())
    assert "VarSize" in params, "Missing parameter 'VarSize'"
    assert "StateSize" in params, "Missing parameter 'StateSize'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1_process_has_VarSize():
    assert hasattr(td1_Process, "VarSize")
    descriptor = None
    for klass in td1_Process.__mro__:
        if "VarSize" in klass.__dict__:
            descriptor = klass.__dict__["VarSize"]
            break
    assert isinstance(descriptor, property)

def test_td1_process_has_StateSize():
    assert hasattr(td1_Process, "StateSize")
    descriptor = None
    for klass in td1_Process.__mro__:
        if "StateSize" in klass.__dict__:
            descriptor = klass.__dict__["StateSize"]
            break
    assert isinstance(descriptor, property)

def test_td1_process_has_Name():
    assert hasattr(td1_Process, "Name")
    descriptor = None
    for klass in td1_Process.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
td1_Program_strategy = st.builds(
    td1_Program,
    Name=
        safe_text,
    ComponentSize=
        st.integers()
)
td1_Component_strategy = st.builds(
    td1_Component,
    Name=
        safe_text,
    ProcessSize=
        st.integers(),
    VarSize=
        st.integers()
)
td1_DataType_strategy = st.builds(
    td1_DataType,
    Name=
        safe_text
)
td1_Action_strategy = st.builds(
    td1_Action,
    codeFiacre=
        safe_text,
    Body=
        safe_text,
    Name=
        safe_text
)
td1_Guard_strategy = st.builds(
    td1_Guard,
    Name=
        safe_text,
    codeFiacre=
        safe_text,
    Body=
        safe_text
)
td1_Trigger_strategy = st.builds(
    td1_Trigger,
    codeFiacre=
        safe_text,
    Body=
        safe_text,
    ArgSize=
        st.integers(),
    Name=
        safe_text
)
td1_Port_strategy = st.builds(
    td1_Port,
    Name=
        safe_text
)
td1_Variable_strategy = st.builds(
    td1_Variable,
    initVal=
        safe_text,
    Name=
        safe_text
)
td1_Transition_strategy = st.builds(
    td1_Transition,
    Name=
        safe_text
)
td1_State_strategy = st.builds(
    td1_State,
    Name=
        safe_text
)
td1_Process_strategy = st.builds(
    td1_Process,
    VarSize=
        st.integers(),
    StateSize=
        st.integers(),
    Name=
        safe_text
)

@given(instance=td1_Program_strategy)
@settings(max_examples=50)
def test_td1_program_instantiation(instance):
    assert isinstance(instance, td1_Program)



@given(instance=td1_Program_strategy)
def test_td1_program_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=td1_Program_strategy)
def test_td1_program_ComponentSize_setter(instance):
    original = instance.ComponentSize
    instance.ComponentSize = original
    assert instance.ComponentSize == original

@given(instance=td1_Component_strategy)
@settings(max_examples=50)
def test_td1_component_instantiation(instance):
    assert isinstance(instance, td1_Component)



@given(instance=td1_Component_strategy)
def test_td1_component_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=td1_Component_strategy)
def test_td1_component_ProcessSize_setter(instance):
    original = instance.ProcessSize
    instance.ProcessSize = original
    assert instance.ProcessSize == original



@given(instance=td1_Component_strategy)
def test_td1_component_VarSize_setter(instance):
    original = instance.VarSize
    instance.VarSize = original
    assert instance.VarSize == original

@given(instance=td1_DataType_strategy)
@settings(max_examples=50)
def test_td1_datatype_instantiation(instance):
    assert isinstance(instance, td1_DataType)



@given(instance=td1_DataType_strategy)
def test_td1_datatype_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1_Action_strategy)
@settings(max_examples=50)
def test_td1_action_instantiation(instance):
    assert isinstance(instance, td1_Action)



@given(instance=td1_Action_strategy)
def test_td1_action_codeFiacre_setter(instance):
    original = instance.codeFiacre
    instance.codeFiacre = original
    assert instance.codeFiacre == original



@given(instance=td1_Action_strategy)
def test_td1_action_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original



@given(instance=td1_Action_strategy)
def test_td1_action_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1_Guard_strategy)
@settings(max_examples=50)
def test_td1_guard_instantiation(instance):
    assert isinstance(instance, td1_Guard)



@given(instance=td1_Guard_strategy)
def test_td1_guard_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=td1_Guard_strategy)
def test_td1_guard_codeFiacre_setter(instance):
    original = instance.codeFiacre
    instance.codeFiacre = original
    assert instance.codeFiacre == original



@given(instance=td1_Guard_strategy)
def test_td1_guard_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original

@given(instance=td1_Trigger_strategy)
@settings(max_examples=50)
def test_td1_trigger_instantiation(instance):
    assert isinstance(instance, td1_Trigger)



@given(instance=td1_Trigger_strategy)
def test_td1_trigger_codeFiacre_setter(instance):
    original = instance.codeFiacre
    instance.codeFiacre = original
    assert instance.codeFiacre == original



@given(instance=td1_Trigger_strategy)
def test_td1_trigger_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original



@given(instance=td1_Trigger_strategy)
def test_td1_trigger_ArgSize_setter(instance):
    original = instance.ArgSize
    instance.ArgSize = original
    assert instance.ArgSize == original



@given(instance=td1_Trigger_strategy)
def test_td1_trigger_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1_Port_strategy)
@settings(max_examples=50)
def test_td1_port_instantiation(instance):
    assert isinstance(instance, td1_Port)



@given(instance=td1_Port_strategy)
def test_td1_port_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1_Variable_strategy)
@settings(max_examples=50)
def test_td1_variable_instantiation(instance):
    assert isinstance(instance, td1_Variable)



@given(instance=td1_Variable_strategy)
def test_td1_variable_initVal_setter(instance):
    original = instance.initVal
    instance.initVal = original
    assert instance.initVal == original



@given(instance=td1_Variable_strategy)
def test_td1_variable_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1_Transition_strategy)
@settings(max_examples=50)
def test_td1_transition_instantiation(instance):
    assert isinstance(instance, td1_Transition)



@given(instance=td1_Transition_strategy)
def test_td1_transition_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1_State_strategy)
@settings(max_examples=50)
def test_td1_state_instantiation(instance):
    assert isinstance(instance, td1_State)



@given(instance=td1_State_strategy)
def test_td1_state_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1_Process_strategy)
@settings(max_examples=50)
def test_td1_process_instantiation(instance):
    assert isinstance(instance, td1_Process)



@given(instance=td1_Process_strategy)
def test_td1_process_VarSize_setter(instance):
    original = instance.VarSize
    instance.VarSize = original
    assert instance.VarSize == original



@given(instance=td1_Process_strategy)
def test_td1_process_StateSize_setter(instance):
    original = instance.StateSize
    instance.StateSize = original
    assert instance.StateSize == original



@given(instance=td1_Process_strategy)
def test_td1_process_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
