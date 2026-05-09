import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    td1::Program,
    td1::Component,
    td1::DataType,
    td1::Action,
    td1::Guard,
    td1::Trigger,
    td1::Port,
    td1::Variable,
    td1::Transition,
    td1::State,
    td1::Process,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_td1::program_is_not_abstract():
    assert not inspect.isabstract(td1::Program)


def test_td1::program_constructor_exists():
    assert callable(td1::Program.__init__)


def test_td1::program_constructor_args():
    sig = inspect.signature(td1::Program.__init__)
    params = list(sig.parameters.keys())
    assert "ComponentSize" in params, "Missing parameter 'ComponentSize'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1::program_has_ComponentSize():
    assert hasattr(td1::Program, "ComponentSize")
    descriptor = None
    for klass in td1::Program.__mro__:
        if "ComponentSize" in klass.__dict__:
            descriptor = klass.__dict__["ComponentSize"]
            break
    assert isinstance(descriptor, property)

def test_td1::program_has_Name():
    assert hasattr(td1::Program, "Name")
    descriptor = None
    for klass in td1::Program.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_td1::component_is_not_abstract():
    assert not inspect.isabstract(td1::Component)


def test_td1::component_constructor_exists():
    assert callable(td1::Component.__init__)


def test_td1::component_constructor_args():
    sig = inspect.signature(td1::Component.__init__)
    params = list(sig.parameters.keys())
    assert "ProcessSize" in params, "Missing parameter 'ProcessSize'"
    assert "VarSize" in params, "Missing parameter 'VarSize'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1::component_has_ProcessSize():
    assert hasattr(td1::Component, "ProcessSize")
    descriptor = None
    for klass in td1::Component.__mro__:
        if "ProcessSize" in klass.__dict__:
            descriptor = klass.__dict__["ProcessSize"]
            break
    assert isinstance(descriptor, property)

def test_td1::component_has_VarSize():
    assert hasattr(td1::Component, "VarSize")
    descriptor = None
    for klass in td1::Component.__mro__:
        if "VarSize" in klass.__dict__:
            descriptor = klass.__dict__["VarSize"]
            break
    assert isinstance(descriptor, property)

def test_td1::component_has_Name():
    assert hasattr(td1::Component, "Name")
    descriptor = None
    for klass in td1::Component.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_td1::datatype_is_not_abstract():
    assert not inspect.isabstract(td1::DataType)


def test_td1::datatype_constructor_exists():
    assert callable(td1::DataType.__init__)


def test_td1::datatype_constructor_args():
    sig = inspect.signature(td1::DataType.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1::datatype_has_Name():
    assert hasattr(td1::DataType, "Name")
    descriptor = None
    for klass in td1::DataType.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_td1::action_is_not_abstract():
    assert not inspect.isabstract(td1::Action)


def test_td1::action_constructor_exists():
    assert callable(td1::Action.__init__)


def test_td1::action_constructor_args():
    sig = inspect.signature(td1::Action.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Body" in params, "Missing parameter 'Body'"
    assert "codeFiacre" in params, "Missing parameter 'codeFiacre'"

def test_td1::action_has_Name():
    assert hasattr(td1::Action, "Name")
    descriptor = None
    for klass in td1::Action.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_td1::action_has_Body():
    assert hasattr(td1::Action, "Body")
    descriptor = None
    for klass in td1::Action.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)

def test_td1::action_has_codeFiacre():
    assert hasattr(td1::Action, "codeFiacre")
    descriptor = None
    for klass in td1::Action.__mro__:
        if "codeFiacre" in klass.__dict__:
            descriptor = klass.__dict__["codeFiacre"]
            break
    assert isinstance(descriptor, property)



def test_td1::guard_is_not_abstract():
    assert not inspect.isabstract(td1::Guard)


def test_td1::guard_constructor_exists():
    assert callable(td1::Guard.__init__)


def test_td1::guard_constructor_args():
    sig = inspect.signature(td1::Guard.__init__)
    params = list(sig.parameters.keys())
    assert "Body" in params, "Missing parameter 'Body'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "codeFiacre" in params, "Missing parameter 'codeFiacre'"

def test_td1::guard_has_Body():
    assert hasattr(td1::Guard, "Body")
    descriptor = None
    for klass in td1::Guard.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)

def test_td1::guard_has_Name():
    assert hasattr(td1::Guard, "Name")
    descriptor = None
    for klass in td1::Guard.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_td1::guard_has_codeFiacre():
    assert hasattr(td1::Guard, "codeFiacre")
    descriptor = None
    for klass in td1::Guard.__mro__:
        if "codeFiacre" in klass.__dict__:
            descriptor = klass.__dict__["codeFiacre"]
            break
    assert isinstance(descriptor, property)



def test_td1::trigger_is_not_abstract():
    assert not inspect.isabstract(td1::Trigger)


def test_td1::trigger_constructor_exists():
    assert callable(td1::Trigger.__init__)


def test_td1::trigger_constructor_args():
    sig = inspect.signature(td1::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "Body" in params, "Missing parameter 'Body'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ArgSize" in params, "Missing parameter 'ArgSize'"
    assert "codeFiacre" in params, "Missing parameter 'codeFiacre'"

def test_td1::trigger_has_Body():
    assert hasattr(td1::Trigger, "Body")
    descriptor = None
    for klass in td1::Trigger.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)

def test_td1::trigger_has_Name():
    assert hasattr(td1::Trigger, "Name")
    descriptor = None
    for klass in td1::Trigger.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_td1::trigger_has_ArgSize():
    assert hasattr(td1::Trigger, "ArgSize")
    descriptor = None
    for klass in td1::Trigger.__mro__:
        if "ArgSize" in klass.__dict__:
            descriptor = klass.__dict__["ArgSize"]
            break
    assert isinstance(descriptor, property)

def test_td1::trigger_has_codeFiacre():
    assert hasattr(td1::Trigger, "codeFiacre")
    descriptor = None
    for klass in td1::Trigger.__mro__:
        if "codeFiacre" in klass.__dict__:
            descriptor = klass.__dict__["codeFiacre"]
            break
    assert isinstance(descriptor, property)



def test_td1::port_is_not_abstract():
    assert not inspect.isabstract(td1::Port)


def test_td1::port_constructor_exists():
    assert callable(td1::Port.__init__)


def test_td1::port_constructor_args():
    sig = inspect.signature(td1::Port.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1::port_has_Name():
    assert hasattr(td1::Port, "Name")
    descriptor = None
    for klass in td1::Port.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_td1::variable_is_not_abstract():
    assert not inspect.isabstract(td1::Variable)


def test_td1::variable_constructor_exists():
    assert callable(td1::Variable.__init__)


def test_td1::variable_constructor_args():
    sig = inspect.signature(td1::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "initVal" in params, "Missing parameter 'initVal'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1::variable_has_initVal():
    assert hasattr(td1::Variable, "initVal")
    descriptor = None
    for klass in td1::Variable.__mro__:
        if "initVal" in klass.__dict__:
            descriptor = klass.__dict__["initVal"]
            break
    assert isinstance(descriptor, property)

def test_td1::variable_has_Name():
    assert hasattr(td1::Variable, "Name")
    descriptor = None
    for klass in td1::Variable.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_td1::transition_is_not_abstract():
    assert not inspect.isabstract(td1::Transition)


def test_td1::transition_constructor_exists():
    assert callable(td1::Transition.__init__)


def test_td1::transition_constructor_args():
    sig = inspect.signature(td1::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1::transition_has_Name():
    assert hasattr(td1::Transition, "Name")
    descriptor = None
    for klass in td1::Transition.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_td1::state_is_not_abstract():
    assert not inspect.isabstract(td1::State)


def test_td1::state_constructor_exists():
    assert callable(td1::State.__init__)


def test_td1::state_constructor_args():
    sig = inspect.signature(td1::State.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1::state_has_Name():
    assert hasattr(td1::State, "Name")
    descriptor = None
    for klass in td1::State.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_td1::process_is_not_abstract():
    assert not inspect.isabstract(td1::Process)


def test_td1::process_constructor_exists():
    assert callable(td1::Process.__init__)


def test_td1::process_constructor_args():
    sig = inspect.signature(td1::Process.__init__)
    params = list(sig.parameters.keys())
    assert "StateSize" in params, "Missing parameter 'StateSize'"
    assert "VarSize" in params, "Missing parameter 'VarSize'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_td1::process_has_StateSize():
    assert hasattr(td1::Process, "StateSize")
    descriptor = None
    for klass in td1::Process.__mro__:
        if "StateSize" in klass.__dict__:
            descriptor = klass.__dict__["StateSize"]
            break
    assert isinstance(descriptor, property)

def test_td1::process_has_VarSize():
    assert hasattr(td1::Process, "VarSize")
    descriptor = None
    for klass in td1::Process.__mro__:
        if "VarSize" in klass.__dict__:
            descriptor = klass.__dict__["VarSize"]
            break
    assert isinstance(descriptor, property)

def test_td1::process_has_Name():
    assert hasattr(td1::Process, "Name")
    descriptor = None
    for klass in td1::Process.__mro__:
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
td1::Program_strategy = st.builds(
    td1::Program,
    ComponentSize=
        st.integers(),
    Name=
        safe_text
)
td1::Component_strategy = st.builds(
    td1::Component,
    ProcessSize=
        st.integers(),
    VarSize=
        st.integers(),
    Name=
        safe_text
)
td1::DataType_strategy = st.builds(
    td1::DataType,
    Name=
        safe_text
)
td1::Action_strategy = st.builds(
    td1::Action,
    Name=
        safe_text,
    Body=
        safe_text,
    codeFiacre=
        safe_text
)
td1::Guard_strategy = st.builds(
    td1::Guard,
    Body=
        safe_text,
    Name=
        safe_text,
    codeFiacre=
        safe_text
)
td1::Trigger_strategy = st.builds(
    td1::Trigger,
    Body=
        safe_text,
    Name=
        safe_text,
    ArgSize=
        st.integers(),
    codeFiacre=
        safe_text
)
td1::Port_strategy = st.builds(
    td1::Port,
    Name=
        safe_text
)
td1::Variable_strategy = st.builds(
    td1::Variable,
    initVal=
        safe_text,
    Name=
        safe_text
)
td1::Transition_strategy = st.builds(
    td1::Transition,
    Name=
        safe_text
)
td1::State_strategy = st.builds(
    td1::State,
    Name=
        safe_text
)
td1::Process_strategy = st.builds(
    td1::Process,
    StateSize=
        st.integers(),
    VarSize=
        st.integers(),
    Name=
        safe_text
)

@given(instance=td1::Program_strategy)
@settings(max_examples=50)
def test_td1::program_instantiation(instance):
    assert isinstance(instance, td1::Program)

@given(instance=td1::Program_strategy)
def test_td1::program_ComponentSize_type(instance):
    assert isinstance(instance.ComponentSize, int)


@given(instance=td1::Program_strategy)
def test_td1::program_ComponentSize_setter(instance):
    original = instance.ComponentSize
    instance.ComponentSize = original
    assert instance.ComponentSize == original

@given(instance=td1::Program_strategy)
def test_td1::program_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=td1::Program_strategy)
def test_td1::program_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1::Component_strategy)
@settings(max_examples=50)
def test_td1::component_instantiation(instance):
    assert isinstance(instance, td1::Component)

@given(instance=td1::Component_strategy)
def test_td1::component_ProcessSize_type(instance):
    assert isinstance(instance.ProcessSize, int)


@given(instance=td1::Component_strategy)
def test_td1::component_ProcessSize_setter(instance):
    original = instance.ProcessSize
    instance.ProcessSize = original
    assert instance.ProcessSize == original

@given(instance=td1::Component_strategy)
def test_td1::component_VarSize_type(instance):
    assert isinstance(instance.VarSize, int)


@given(instance=td1::Component_strategy)
def test_td1::component_VarSize_setter(instance):
    original = instance.VarSize
    instance.VarSize = original
    assert instance.VarSize == original

@given(instance=td1::Component_strategy)
def test_td1::component_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=td1::Component_strategy)
def test_td1::component_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1::DataType_strategy)
@settings(max_examples=50)
def test_td1::datatype_instantiation(instance):
    assert isinstance(instance, td1::DataType)

@given(instance=td1::DataType_strategy)
def test_td1::datatype_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=td1::DataType_strategy)
def test_td1::datatype_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1::Action_strategy)
@settings(max_examples=50)
def test_td1::action_instantiation(instance):
    assert isinstance(instance, td1::Action)

@given(instance=td1::Action_strategy)
def test_td1::action_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=td1::Action_strategy)
def test_td1::action_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1::Action_strategy)
def test_td1::action_Body_type(instance):
    assert isinstance(instance.Body, str)


@given(instance=td1::Action_strategy)
def test_td1::action_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original

@given(instance=td1::Action_strategy)
def test_td1::action_codeFiacre_type(instance):
    assert isinstance(instance.codeFiacre, str)


@given(instance=td1::Action_strategy)
def test_td1::action_codeFiacre_setter(instance):
    original = instance.codeFiacre
    instance.codeFiacre = original
    assert instance.codeFiacre == original

@given(instance=td1::Guard_strategy)
@settings(max_examples=50)
def test_td1::guard_instantiation(instance):
    assert isinstance(instance, td1::Guard)

@given(instance=td1::Guard_strategy)
def test_td1::guard_Body_type(instance):
    assert isinstance(instance.Body, str)


@given(instance=td1::Guard_strategy)
def test_td1::guard_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original

@given(instance=td1::Guard_strategy)
def test_td1::guard_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=td1::Guard_strategy)
def test_td1::guard_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1::Guard_strategy)
def test_td1::guard_codeFiacre_type(instance):
    assert isinstance(instance.codeFiacre, str)


@given(instance=td1::Guard_strategy)
def test_td1::guard_codeFiacre_setter(instance):
    original = instance.codeFiacre
    instance.codeFiacre = original
    assert instance.codeFiacre == original

@given(instance=td1::Trigger_strategy)
@settings(max_examples=50)
def test_td1::trigger_instantiation(instance):
    assert isinstance(instance, td1::Trigger)

@given(instance=td1::Trigger_strategy)
def test_td1::trigger_Body_type(instance):
    assert isinstance(instance.Body, str)


@given(instance=td1::Trigger_strategy)
def test_td1::trigger_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original

@given(instance=td1::Trigger_strategy)
def test_td1::trigger_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=td1::Trigger_strategy)
def test_td1::trigger_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1::Trigger_strategy)
def test_td1::trigger_ArgSize_type(instance):
    assert isinstance(instance.ArgSize, int)


@given(instance=td1::Trigger_strategy)
def test_td1::trigger_ArgSize_setter(instance):
    original = instance.ArgSize
    instance.ArgSize = original
    assert instance.ArgSize == original

@given(instance=td1::Trigger_strategy)
def test_td1::trigger_codeFiacre_type(instance):
    assert isinstance(instance.codeFiacre, str)


@given(instance=td1::Trigger_strategy)
def test_td1::trigger_codeFiacre_setter(instance):
    original = instance.codeFiacre
    instance.codeFiacre = original
    assert instance.codeFiacre == original

@given(instance=td1::Port_strategy)
@settings(max_examples=50)
def test_td1::port_instantiation(instance):
    assert isinstance(instance, td1::Port)

@given(instance=td1::Port_strategy)
def test_td1::port_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=td1::Port_strategy)
def test_td1::port_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1::Variable_strategy)
@settings(max_examples=50)
def test_td1::variable_instantiation(instance):
    assert isinstance(instance, td1::Variable)

@given(instance=td1::Variable_strategy)
def test_td1::variable_initVal_type(instance):
    assert isinstance(instance.initVal, str)


@given(instance=td1::Variable_strategy)
def test_td1::variable_initVal_setter(instance):
    original = instance.initVal
    instance.initVal = original
    assert instance.initVal == original

@given(instance=td1::Variable_strategy)
def test_td1::variable_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=td1::Variable_strategy)
def test_td1::variable_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1::Transition_strategy)
@settings(max_examples=50)
def test_td1::transition_instantiation(instance):
    assert isinstance(instance, td1::Transition)

@given(instance=td1::Transition_strategy)
def test_td1::transition_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=td1::Transition_strategy)
def test_td1::transition_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1::State_strategy)
@settings(max_examples=50)
def test_td1::state_instantiation(instance):
    assert isinstance(instance, td1::State)

@given(instance=td1::State_strategy)
def test_td1::state_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=td1::State_strategy)
def test_td1::state_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=td1::Process_strategy)
@settings(max_examples=50)
def test_td1::process_instantiation(instance):
    assert isinstance(instance, td1::Process)

@given(instance=td1::Process_strategy)
def test_td1::process_StateSize_type(instance):
    assert isinstance(instance.StateSize, int)


@given(instance=td1::Process_strategy)
def test_td1::process_StateSize_setter(instance):
    original = instance.StateSize
    instance.StateSize = original
    assert instance.StateSize == original

@given(instance=td1::Process_strategy)
def test_td1::process_VarSize_type(instance):
    assert isinstance(instance.VarSize, int)


@given(instance=td1::Process_strategy)
def test_td1::process_VarSize_setter(instance):
    original = instance.VarSize
    instance.VarSize = original
    assert instance.VarSize == original

@given(instance=td1::Process_strategy)
def test_td1::process_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=td1::Process_strategy)
def test_td1::process_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
