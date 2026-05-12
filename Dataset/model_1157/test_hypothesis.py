import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    EModelElement,
    fiacremm_Guard,
    fiacremm_Transition,
    fiacremm_Program,
    fiacremm_Action,
    fiacremm_Process,
    fiacremm_Component,
    fiacremm_Trigger,
    fiacremm_DataType,
    fiacremm_Port,
    fiacremm_State,
    fiacremm_Variable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_fiacremm_guard_is_not_abstract():
    assert not inspect.isabstract(fiacremm_Guard)


def test_fiacremm_guard_constructor_exists():
    assert callable(fiacremm_Guard.__init__)


def test_fiacremm_guard_constructor_args():
    sig = inspect.signature(fiacremm_Guard.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "codeFiacre" in params, "Missing parameter 'codeFiacre'"
    assert "Body" in params, "Missing parameter 'Body'"

def test_fiacremm_guard_has_Name():
    assert hasattr(fiacremm_Guard, "Name")
    descriptor = None
    for klass in fiacremm_Guard.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm_guard_has_codeFiacre():
    assert hasattr(fiacremm_Guard, "codeFiacre")
    descriptor = None
    for klass in fiacremm_Guard.__mro__:
        if "codeFiacre" in klass.__dict__:
            descriptor = klass.__dict__["codeFiacre"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm_guard_has_Body():
    assert hasattr(fiacremm_Guard, "Body")
    descriptor = None
    for klass in fiacremm_Guard.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm_transition_is_not_abstract():
    assert not inspect.isabstract(fiacremm_Transition)


def test_fiacremm_transition_constructor_exists():
    assert callable(fiacremm_Transition.__init__)


def test_fiacremm_transition_constructor_args():
    sig = inspect.signature(fiacremm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_fiacremm_transition_has_Name():
    assert hasattr(fiacremm_Transition, "Name")
    descriptor = None
    for klass in fiacremm_Transition.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm_program_is_not_abstract():
    assert not inspect.isabstract(fiacremm_Program)


def test_fiacremm_program_constructor_exists():
    assert callable(fiacremm_Program.__init__)


def test_fiacremm_program_constructor_args():
    sig = inspect.signature(fiacremm_Program.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ComponentSize" in params, "Missing parameter 'ComponentSize'"

def test_fiacremm_program_has_Name():
    assert hasattr(fiacremm_Program, "Name")
    descriptor = None
    for klass in fiacremm_Program.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm_program_has_ComponentSize():
    assert hasattr(fiacremm_Program, "ComponentSize")
    descriptor = None
    for klass in fiacremm_Program.__mro__:
        if "ComponentSize" in klass.__dict__:
            descriptor = klass.__dict__["ComponentSize"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm_action_is_not_abstract():
    assert not inspect.isabstract(fiacremm_Action)


def test_fiacremm_action_constructor_exists():
    assert callable(fiacremm_Action.__init__)


def test_fiacremm_action_constructor_args():
    sig = inspect.signature(fiacremm_Action.__init__)
    params = list(sig.parameters.keys())
    assert "Body" in params, "Missing parameter 'Body'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "codeFiacre" in params, "Missing parameter 'codeFiacre'"

def test_fiacremm_action_has_Body():
    assert hasattr(fiacremm_Action, "Body")
    descriptor = None
    for klass in fiacremm_Action.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm_action_has_Name():
    assert hasattr(fiacremm_Action, "Name")
    descriptor = None
    for klass in fiacremm_Action.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm_action_has_codeFiacre():
    assert hasattr(fiacremm_Action, "codeFiacre")
    descriptor = None
    for klass in fiacremm_Action.__mro__:
        if "codeFiacre" in klass.__dict__:
            descriptor = klass.__dict__["codeFiacre"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm_process_is_not_abstract():
    assert not inspect.isabstract(fiacremm_Process)


def test_fiacremm_process_constructor_exists():
    assert callable(fiacremm_Process.__init__)


def test_fiacremm_process_constructor_args():
    sig = inspect.signature(fiacremm_Process.__init__)
    params = list(sig.parameters.keys())
    assert "StateSize" in params, "Missing parameter 'StateSize'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "VarSize" in params, "Missing parameter 'VarSize'"

def test_fiacremm_process_has_StateSize():
    assert hasattr(fiacremm_Process, "StateSize")
    descriptor = None
    for klass in fiacremm_Process.__mro__:
        if "StateSize" in klass.__dict__:
            descriptor = klass.__dict__["StateSize"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm_process_has_Name():
    assert hasattr(fiacremm_Process, "Name")
    descriptor = None
    for klass in fiacremm_Process.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm_process_has_VarSize():
    assert hasattr(fiacremm_Process, "VarSize")
    descriptor = None
    for klass in fiacremm_Process.__mro__:
        if "VarSize" in klass.__dict__:
            descriptor = klass.__dict__["VarSize"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm_component_is_not_abstract():
    assert not inspect.isabstract(fiacremm_Component)


def test_fiacremm_component_constructor_exists():
    assert callable(fiacremm_Component.__init__)


def test_fiacremm_component_constructor_args():
    sig = inspect.signature(fiacremm_Component.__init__)
    params = list(sig.parameters.keys())
    assert "VarSize" in params, "Missing parameter 'VarSize'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ProcessSize" in params, "Missing parameter 'ProcessSize'"

def test_fiacremm_component_has_VarSize():
    assert hasattr(fiacremm_Component, "VarSize")
    descriptor = None
    for klass in fiacremm_Component.__mro__:
        if "VarSize" in klass.__dict__:
            descriptor = klass.__dict__["VarSize"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm_component_has_Name():
    assert hasattr(fiacremm_Component, "Name")
    descriptor = None
    for klass in fiacremm_Component.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm_component_has_ProcessSize():
    assert hasattr(fiacremm_Component, "ProcessSize")
    descriptor = None
    for klass in fiacremm_Component.__mro__:
        if "ProcessSize" in klass.__dict__:
            descriptor = klass.__dict__["ProcessSize"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm_trigger_is_not_abstract():
    assert not inspect.isabstract(fiacremm_Trigger)


def test_fiacremm_trigger_constructor_exists():
    assert callable(fiacremm_Trigger.__init__)


def test_fiacremm_trigger_constructor_args():
    sig = inspect.signature(fiacremm_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "Body" in params, "Missing parameter 'Body'"
    assert "ArgSize" in params, "Missing parameter 'ArgSize'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "codeFiacre" in params, "Missing parameter 'codeFiacre'"

def test_fiacremm_trigger_has_Body():
    assert hasattr(fiacremm_Trigger, "Body")
    descriptor = None
    for klass in fiacremm_Trigger.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm_trigger_has_ArgSize():
    assert hasattr(fiacremm_Trigger, "ArgSize")
    descriptor = None
    for klass in fiacremm_Trigger.__mro__:
        if "ArgSize" in klass.__dict__:
            descriptor = klass.__dict__["ArgSize"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm_trigger_has_Name():
    assert hasattr(fiacremm_Trigger, "Name")
    descriptor = None
    for klass in fiacremm_Trigger.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm_trigger_has_codeFiacre():
    assert hasattr(fiacremm_Trigger, "codeFiacre")
    descriptor = None
    for klass in fiacremm_Trigger.__mro__:
        if "codeFiacre" in klass.__dict__:
            descriptor = klass.__dict__["codeFiacre"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm_datatype_is_not_abstract():
    assert not inspect.isabstract(fiacremm_DataType)


def test_fiacremm_datatype_constructor_exists():
    assert callable(fiacremm_DataType.__init__)


def test_fiacremm_datatype_constructor_args():
    sig = inspect.signature(fiacremm_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_fiacremm_datatype_has_Name():
    assert hasattr(fiacremm_DataType, "Name")
    descriptor = None
    for klass in fiacremm_DataType.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm_port_is_not_abstract():
    assert not inspect.isabstract(fiacremm_Port)


def test_fiacremm_port_constructor_exists():
    assert callable(fiacremm_Port.__init__)


def test_fiacremm_port_constructor_args():
    sig = inspect.signature(fiacremm_Port.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_fiacremm_port_has_Name():
    assert hasattr(fiacremm_Port, "Name")
    descriptor = None
    for klass in fiacremm_Port.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm_state_is_not_abstract():
    assert not inspect.isabstract(fiacremm_State)


def test_fiacremm_state_constructor_exists():
    assert callable(fiacremm_State.__init__)


def test_fiacremm_state_constructor_args():
    sig = inspect.signature(fiacremm_State.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_fiacremm_state_has_Name():
    assert hasattr(fiacremm_State, "Name")
    descriptor = None
    for klass in fiacremm_State.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm_variable_is_not_abstract():
    assert not inspect.isabstract(fiacremm_Variable)


def test_fiacremm_variable_constructor_exists():
    assert callable(fiacremm_Variable.__init__)


def test_fiacremm_variable_constructor_args():
    sig = inspect.signature(fiacremm_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "initVal" in params, "Missing parameter 'initVal'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_fiacremm_variable_has_initVal():
    assert hasattr(fiacremm_Variable, "initVal")
    descriptor = None
    for klass in fiacremm_Variable.__mro__:
        if "initVal" in klass.__dict__:
            descriptor = klass.__dict__["initVal"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm_variable_has_Name():
    assert hasattr(fiacremm_Variable, "Name")
    descriptor = None
    for klass in fiacremm_Variable.__mro__:
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
EModelElement_strategy = st.builds(
    EModelElement,
)
fiacremm_Guard_strategy = st.builds(
    fiacremm_Guard,
    Name=
        safe_text,
    codeFiacre=
        safe_text,
    Body=
        safe_text
)
fiacremm_Transition_strategy = st.builds(
    fiacremm_Transition,
    Name=
        safe_text
)
fiacremm_Program_strategy = st.builds(
    fiacremm_Program,
    Name=
        safe_text,
    ComponentSize=
        st.integers()
)
fiacremm_Action_strategy = st.builds(
    fiacremm_Action,
    Body=
        safe_text,
    Name=
        safe_text,
    codeFiacre=
        safe_text
)
fiacremm_Process_strategy = st.builds(
    fiacremm_Process,
    StateSize=
        st.integers(),
    Name=
        safe_text,
    VarSize=
        st.integers()
)
fiacremm_Component_strategy = st.builds(
    fiacremm_Component,
    VarSize=
        st.integers(),
    Name=
        safe_text,
    ProcessSize=
        st.integers()
)
fiacremm_Trigger_strategy = st.builds(
    fiacremm_Trigger,
    Body=
        safe_text,
    ArgSize=
        st.integers(),
    Name=
        safe_text,
    codeFiacre=
        safe_text
)
fiacremm_DataType_strategy = st.builds(
    fiacremm_DataType,
    Name=
        safe_text
)
fiacremm_Port_strategy = st.builds(
    fiacremm_Port,
    Name=
        safe_text
)
fiacremm_State_strategy = st.builds(
    fiacremm_State,
    Name=
        safe_text
)
fiacremm_Variable_strategy = st.builds(
    fiacremm_Variable,
    initVal=
        safe_text,
    Name=
        safe_text
)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=fiacremm_Guard_strategy)
@settings(max_examples=50)
def test_fiacremm_guard_instantiation(instance):
    assert isinstance(instance, fiacremm_Guard)



@given(instance=fiacremm_Guard_strategy)
def test_fiacremm_guard_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=fiacremm_Guard_strategy)
def test_fiacremm_guard_codeFiacre_setter(instance):
    original = instance.codeFiacre
    instance.codeFiacre = original
    assert instance.codeFiacre == original



@given(instance=fiacremm_Guard_strategy)
def test_fiacremm_guard_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original

@given(instance=fiacremm_Transition_strategy)
@settings(max_examples=50)
def test_fiacremm_transition_instantiation(instance):
    assert isinstance(instance, fiacremm_Transition)



@given(instance=fiacremm_Transition_strategy)
def test_fiacremm_transition_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=fiacremm_Program_strategy)
@settings(max_examples=50)
def test_fiacremm_program_instantiation(instance):
    assert isinstance(instance, fiacremm_Program)



@given(instance=fiacremm_Program_strategy)
def test_fiacremm_program_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=fiacremm_Program_strategy)
def test_fiacremm_program_ComponentSize_setter(instance):
    original = instance.ComponentSize
    instance.ComponentSize = original
    assert instance.ComponentSize == original

@given(instance=fiacremm_Action_strategy)
@settings(max_examples=50)
def test_fiacremm_action_instantiation(instance):
    assert isinstance(instance, fiacremm_Action)



@given(instance=fiacremm_Action_strategy)
def test_fiacremm_action_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original



@given(instance=fiacremm_Action_strategy)
def test_fiacremm_action_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=fiacremm_Action_strategy)
def test_fiacremm_action_codeFiacre_setter(instance):
    original = instance.codeFiacre
    instance.codeFiacre = original
    assert instance.codeFiacre == original

@given(instance=fiacremm_Process_strategy)
@settings(max_examples=50)
def test_fiacremm_process_instantiation(instance):
    assert isinstance(instance, fiacremm_Process)



@given(instance=fiacremm_Process_strategy)
def test_fiacremm_process_StateSize_setter(instance):
    original = instance.StateSize
    instance.StateSize = original
    assert instance.StateSize == original



@given(instance=fiacremm_Process_strategy)
def test_fiacremm_process_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=fiacremm_Process_strategy)
def test_fiacremm_process_VarSize_setter(instance):
    original = instance.VarSize
    instance.VarSize = original
    assert instance.VarSize == original

@given(instance=fiacremm_Component_strategy)
@settings(max_examples=50)
def test_fiacremm_component_instantiation(instance):
    assert isinstance(instance, fiacremm_Component)



@given(instance=fiacremm_Component_strategy)
def test_fiacremm_component_VarSize_setter(instance):
    original = instance.VarSize
    instance.VarSize = original
    assert instance.VarSize == original



@given(instance=fiacremm_Component_strategy)
def test_fiacremm_component_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=fiacremm_Component_strategy)
def test_fiacremm_component_ProcessSize_setter(instance):
    original = instance.ProcessSize
    instance.ProcessSize = original
    assert instance.ProcessSize == original

@given(instance=fiacremm_Trigger_strategy)
@settings(max_examples=50)
def test_fiacremm_trigger_instantiation(instance):
    assert isinstance(instance, fiacremm_Trigger)



@given(instance=fiacremm_Trigger_strategy)
def test_fiacremm_trigger_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original



@given(instance=fiacremm_Trigger_strategy)
def test_fiacremm_trigger_ArgSize_setter(instance):
    original = instance.ArgSize
    instance.ArgSize = original
    assert instance.ArgSize == original



@given(instance=fiacremm_Trigger_strategy)
def test_fiacremm_trigger_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=fiacremm_Trigger_strategy)
def test_fiacremm_trigger_codeFiacre_setter(instance):
    original = instance.codeFiacre
    instance.codeFiacre = original
    assert instance.codeFiacre == original

@given(instance=fiacremm_DataType_strategy)
@settings(max_examples=50)
def test_fiacremm_datatype_instantiation(instance):
    assert isinstance(instance, fiacremm_DataType)



@given(instance=fiacremm_DataType_strategy)
def test_fiacremm_datatype_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=fiacremm_Port_strategy)
@settings(max_examples=50)
def test_fiacremm_port_instantiation(instance):
    assert isinstance(instance, fiacremm_Port)



@given(instance=fiacremm_Port_strategy)
def test_fiacremm_port_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=fiacremm_State_strategy)
@settings(max_examples=50)
def test_fiacremm_state_instantiation(instance):
    assert isinstance(instance, fiacremm_State)



@given(instance=fiacremm_State_strategy)
def test_fiacremm_state_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=fiacremm_Variable_strategy)
@settings(max_examples=50)
def test_fiacremm_variable_instantiation(instance):
    assert isinstance(instance, fiacremm_Variable)



@given(instance=fiacremm_Variable_strategy)
def test_fiacremm_variable_initVal_setter(instance):
    original = instance.initVal
    instance.initVal = original
    assert instance.initVal == original



@given(instance=fiacremm_Variable_strategy)
def test_fiacremm_variable_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
