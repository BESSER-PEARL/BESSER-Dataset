import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EModelElement,
    fiacremm::Component,
    fiacremm::Port,
    fiacremm::Action,
    fiacremm::Trigger,
    fiacremm::Process,
    fiacremm::Transition,
    fiacremm::DataType,
    fiacremm::Guard,
    fiacremm::Program,
    fiacremm::State,
    fiacremm::Variable,
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



def test_fiacremm::component_is_not_abstract():
    assert not inspect.isabstract(fiacremm::Component)


def test_fiacremm::component_constructor_exists():
    assert callable(fiacremm::Component.__init__)


def test_fiacremm::component_constructor_args():
    sig = inspect.signature(fiacremm::Component.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ProcessSize" in params, "Missing parameter 'ProcessSize'"
    assert "VarSize" in params, "Missing parameter 'VarSize'"

def test_fiacremm::component_has_Name():
    assert hasattr(fiacremm::Component, "Name")
    descriptor = None
    for klass in fiacremm::Component.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm::component_has_ProcessSize():
    assert hasattr(fiacremm::Component, "ProcessSize")
    descriptor = None
    for klass in fiacremm::Component.__mro__:
        if "ProcessSize" in klass.__dict__:
            descriptor = klass.__dict__["ProcessSize"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm::component_has_VarSize():
    assert hasattr(fiacremm::Component, "VarSize")
    descriptor = None
    for klass in fiacremm::Component.__mro__:
        if "VarSize" in klass.__dict__:
            descriptor = klass.__dict__["VarSize"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm::port_is_not_abstract():
    assert not inspect.isabstract(fiacremm::Port)


def test_fiacremm::port_constructor_exists():
    assert callable(fiacremm::Port.__init__)


def test_fiacremm::port_constructor_args():
    sig = inspect.signature(fiacremm::Port.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_fiacremm::port_has_Name():
    assert hasattr(fiacremm::Port, "Name")
    descriptor = None
    for klass in fiacremm::Port.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm::action_is_not_abstract():
    assert not inspect.isabstract(fiacremm::Action)


def test_fiacremm::action_constructor_exists():
    assert callable(fiacremm::Action.__init__)


def test_fiacremm::action_constructor_args():
    sig = inspect.signature(fiacremm::Action.__init__)
    params = list(sig.parameters.keys())
    assert "Body" in params, "Missing parameter 'Body'"
    assert "codeFiacre" in params, "Missing parameter 'codeFiacre'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_fiacremm::action_has_Body():
    assert hasattr(fiacremm::Action, "Body")
    descriptor = None
    for klass in fiacremm::Action.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm::action_has_codeFiacre():
    assert hasattr(fiacremm::Action, "codeFiacre")
    descriptor = None
    for klass in fiacremm::Action.__mro__:
        if "codeFiacre" in klass.__dict__:
            descriptor = klass.__dict__["codeFiacre"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm::action_has_Name():
    assert hasattr(fiacremm::Action, "Name")
    descriptor = None
    for klass in fiacremm::Action.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm::trigger_is_not_abstract():
    assert not inspect.isabstract(fiacremm::Trigger)


def test_fiacremm::trigger_constructor_exists():
    assert callable(fiacremm::Trigger.__init__)


def test_fiacremm::trigger_constructor_args():
    sig = inspect.signature(fiacremm::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ArgSize" in params, "Missing parameter 'ArgSize'"
    assert "codeFiacre" in params, "Missing parameter 'codeFiacre'"
    assert "Body" in params, "Missing parameter 'Body'"

def test_fiacremm::trigger_has_Name():
    assert hasattr(fiacremm::Trigger, "Name")
    descriptor = None
    for klass in fiacremm::Trigger.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm::trigger_has_ArgSize():
    assert hasattr(fiacremm::Trigger, "ArgSize")
    descriptor = None
    for klass in fiacremm::Trigger.__mro__:
        if "ArgSize" in klass.__dict__:
            descriptor = klass.__dict__["ArgSize"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm::trigger_has_codeFiacre():
    assert hasattr(fiacremm::Trigger, "codeFiacre")
    descriptor = None
    for klass in fiacremm::Trigger.__mro__:
        if "codeFiacre" in klass.__dict__:
            descriptor = klass.__dict__["codeFiacre"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm::trigger_has_Body():
    assert hasattr(fiacremm::Trigger, "Body")
    descriptor = None
    for klass in fiacremm::Trigger.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm::process_is_not_abstract():
    assert not inspect.isabstract(fiacremm::Process)


def test_fiacremm::process_constructor_exists():
    assert callable(fiacremm::Process.__init__)


def test_fiacremm::process_constructor_args():
    sig = inspect.signature(fiacremm::Process.__init__)
    params = list(sig.parameters.keys())
    assert "StateSize" in params, "Missing parameter 'StateSize'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "VarSize" in params, "Missing parameter 'VarSize'"

def test_fiacremm::process_has_StateSize():
    assert hasattr(fiacremm::Process, "StateSize")
    descriptor = None
    for klass in fiacremm::Process.__mro__:
        if "StateSize" in klass.__dict__:
            descriptor = klass.__dict__["StateSize"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm::process_has_Name():
    assert hasattr(fiacremm::Process, "Name")
    descriptor = None
    for klass in fiacremm::Process.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm::process_has_VarSize():
    assert hasattr(fiacremm::Process, "VarSize")
    descriptor = None
    for klass in fiacremm::Process.__mro__:
        if "VarSize" in klass.__dict__:
            descriptor = klass.__dict__["VarSize"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm::transition_is_not_abstract():
    assert not inspect.isabstract(fiacremm::Transition)


def test_fiacremm::transition_constructor_exists():
    assert callable(fiacremm::Transition.__init__)


def test_fiacremm::transition_constructor_args():
    sig = inspect.signature(fiacremm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_fiacremm::transition_has_Name():
    assert hasattr(fiacremm::Transition, "Name")
    descriptor = None
    for klass in fiacremm::Transition.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm::datatype_is_not_abstract():
    assert not inspect.isabstract(fiacremm::DataType)


def test_fiacremm::datatype_constructor_exists():
    assert callable(fiacremm::DataType.__init__)


def test_fiacremm::datatype_constructor_args():
    sig = inspect.signature(fiacremm::DataType.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_fiacremm::datatype_has_Name():
    assert hasattr(fiacremm::DataType, "Name")
    descriptor = None
    for klass in fiacremm::DataType.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm::guard_is_not_abstract():
    assert not inspect.isabstract(fiacremm::Guard)


def test_fiacremm::guard_constructor_exists():
    assert callable(fiacremm::Guard.__init__)


def test_fiacremm::guard_constructor_args():
    sig = inspect.signature(fiacremm::Guard.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "codeFiacre" in params, "Missing parameter 'codeFiacre'"
    assert "Body" in params, "Missing parameter 'Body'"

def test_fiacremm::guard_has_Name():
    assert hasattr(fiacremm::Guard, "Name")
    descriptor = None
    for klass in fiacremm::Guard.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm::guard_has_codeFiacre():
    assert hasattr(fiacremm::Guard, "codeFiacre")
    descriptor = None
    for klass in fiacremm::Guard.__mro__:
        if "codeFiacre" in klass.__dict__:
            descriptor = klass.__dict__["codeFiacre"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm::guard_has_Body():
    assert hasattr(fiacremm::Guard, "Body")
    descriptor = None
    for klass in fiacremm::Guard.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm::program_is_not_abstract():
    assert not inspect.isabstract(fiacremm::Program)


def test_fiacremm::program_constructor_exists():
    assert callable(fiacremm::Program.__init__)


def test_fiacremm::program_constructor_args():
    sig = inspect.signature(fiacremm::Program.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ComponentSize" in params, "Missing parameter 'ComponentSize'"

def test_fiacremm::program_has_Name():
    assert hasattr(fiacremm::Program, "Name")
    descriptor = None
    for klass in fiacremm::Program.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm::program_has_ComponentSize():
    assert hasattr(fiacremm::Program, "ComponentSize")
    descriptor = None
    for klass in fiacremm::Program.__mro__:
        if "ComponentSize" in klass.__dict__:
            descriptor = klass.__dict__["ComponentSize"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm::state_is_not_abstract():
    assert not inspect.isabstract(fiacremm::State)


def test_fiacremm::state_constructor_exists():
    assert callable(fiacremm::State.__init__)


def test_fiacremm::state_constructor_args():
    sig = inspect.signature(fiacremm::State.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_fiacremm::state_has_Name():
    assert hasattr(fiacremm::State, "Name")
    descriptor = None
    for klass in fiacremm::State.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_fiacremm::variable_is_not_abstract():
    assert not inspect.isabstract(fiacremm::Variable)


def test_fiacremm::variable_constructor_exists():
    assert callable(fiacremm::Variable.__init__)


def test_fiacremm::variable_constructor_args():
    sig = inspect.signature(fiacremm::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "initVal" in params, "Missing parameter 'initVal'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_fiacremm::variable_has_initVal():
    assert hasattr(fiacremm::Variable, "initVal")
    descriptor = None
    for klass in fiacremm::Variable.__mro__:
        if "initVal" in klass.__dict__:
            descriptor = klass.__dict__["initVal"]
            break
    assert isinstance(descriptor, property)

def test_fiacremm::variable_has_Name():
    assert hasattr(fiacremm::Variable, "Name")
    descriptor = None
    for klass in fiacremm::Variable.__mro__:
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
fiacremm::Component_strategy = st.builds(
    fiacremm::Component,
    Name=
        safe_text,
    ProcessSize=
        st.integers(),
    VarSize=
        st.integers()
)
fiacremm::Port_strategy = st.builds(
    fiacremm::Port,
    Name=
        safe_text
)
fiacremm::Action_strategy = st.builds(
    fiacremm::Action,
    Body=
        safe_text,
    codeFiacre=
        safe_text,
    Name=
        safe_text
)
fiacremm::Trigger_strategy = st.builds(
    fiacremm::Trigger,
    Name=
        safe_text,
    ArgSize=
        st.integers(),
    codeFiacre=
        safe_text,
    Body=
        safe_text
)
fiacremm::Process_strategy = st.builds(
    fiacremm::Process,
    StateSize=
        st.integers(),
    Name=
        safe_text,
    VarSize=
        st.integers()
)
fiacremm::Transition_strategy = st.builds(
    fiacremm::Transition,
    Name=
        safe_text
)
fiacremm::DataType_strategy = st.builds(
    fiacremm::DataType,
    Name=
        safe_text
)
fiacremm::Guard_strategy = st.builds(
    fiacremm::Guard,
    Name=
        safe_text,
    codeFiacre=
        safe_text,
    Body=
        safe_text
)
fiacremm::Program_strategy = st.builds(
    fiacremm::Program,
    Name=
        safe_text,
    ComponentSize=
        st.integers()
)
fiacremm::State_strategy = st.builds(
    fiacremm::State,
    Name=
        safe_text
)
fiacremm::Variable_strategy = st.builds(
    fiacremm::Variable,
    initVal=
        safe_text,
    Name=
        safe_text
)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=fiacremm::Component_strategy)
@settings(max_examples=50)
def test_fiacremm::component_instantiation(instance):
    assert isinstance(instance, fiacremm::Component)

@given(instance=fiacremm::Component_strategy)
def test_fiacremm::component_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=fiacremm::Component_strategy)
def test_fiacremm::component_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=fiacremm::Component_strategy)
def test_fiacremm::component_ProcessSize_type(instance):
    assert isinstance(instance.ProcessSize, int)


@given(instance=fiacremm::Component_strategy)
def test_fiacremm::component_ProcessSize_setter(instance):
    original = instance.ProcessSize
    instance.ProcessSize = original
    assert instance.ProcessSize == original

@given(instance=fiacremm::Component_strategy)
def test_fiacremm::component_VarSize_type(instance):
    assert isinstance(instance.VarSize, int)


@given(instance=fiacremm::Component_strategy)
def test_fiacremm::component_VarSize_setter(instance):
    original = instance.VarSize
    instance.VarSize = original
    assert instance.VarSize == original

@given(instance=fiacremm::Port_strategy)
@settings(max_examples=50)
def test_fiacremm::port_instantiation(instance):
    assert isinstance(instance, fiacremm::Port)

@given(instance=fiacremm::Port_strategy)
def test_fiacremm::port_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=fiacremm::Port_strategy)
def test_fiacremm::port_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=fiacremm::Action_strategy)
@settings(max_examples=50)
def test_fiacremm::action_instantiation(instance):
    assert isinstance(instance, fiacremm::Action)

@given(instance=fiacremm::Action_strategy)
def test_fiacremm::action_Body_type(instance):
    assert isinstance(instance.Body, str)


@given(instance=fiacremm::Action_strategy)
def test_fiacremm::action_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original

@given(instance=fiacremm::Action_strategy)
def test_fiacremm::action_codeFiacre_type(instance):
    assert isinstance(instance.codeFiacre, str)


@given(instance=fiacremm::Action_strategy)
def test_fiacremm::action_codeFiacre_setter(instance):
    original = instance.codeFiacre
    instance.codeFiacre = original
    assert instance.codeFiacre == original

@given(instance=fiacremm::Action_strategy)
def test_fiacremm::action_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=fiacremm::Action_strategy)
def test_fiacremm::action_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=fiacremm::Trigger_strategy)
@settings(max_examples=50)
def test_fiacremm::trigger_instantiation(instance):
    assert isinstance(instance, fiacremm::Trigger)

@given(instance=fiacremm::Trigger_strategy)
def test_fiacremm::trigger_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=fiacremm::Trigger_strategy)
def test_fiacremm::trigger_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=fiacremm::Trigger_strategy)
def test_fiacremm::trigger_ArgSize_type(instance):
    assert isinstance(instance.ArgSize, int)


@given(instance=fiacremm::Trigger_strategy)
def test_fiacremm::trigger_ArgSize_setter(instance):
    original = instance.ArgSize
    instance.ArgSize = original
    assert instance.ArgSize == original

@given(instance=fiacremm::Trigger_strategy)
def test_fiacremm::trigger_codeFiacre_type(instance):
    assert isinstance(instance.codeFiacre, str)


@given(instance=fiacremm::Trigger_strategy)
def test_fiacremm::trigger_codeFiacre_setter(instance):
    original = instance.codeFiacre
    instance.codeFiacre = original
    assert instance.codeFiacre == original

@given(instance=fiacremm::Trigger_strategy)
def test_fiacremm::trigger_Body_type(instance):
    assert isinstance(instance.Body, str)


@given(instance=fiacremm::Trigger_strategy)
def test_fiacremm::trigger_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original

@given(instance=fiacremm::Process_strategy)
@settings(max_examples=50)
def test_fiacremm::process_instantiation(instance):
    assert isinstance(instance, fiacremm::Process)

@given(instance=fiacremm::Process_strategy)
def test_fiacremm::process_StateSize_type(instance):
    assert isinstance(instance.StateSize, int)


@given(instance=fiacremm::Process_strategy)
def test_fiacremm::process_StateSize_setter(instance):
    original = instance.StateSize
    instance.StateSize = original
    assert instance.StateSize == original

@given(instance=fiacremm::Process_strategy)
def test_fiacremm::process_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=fiacremm::Process_strategy)
def test_fiacremm::process_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=fiacremm::Process_strategy)
def test_fiacremm::process_VarSize_type(instance):
    assert isinstance(instance.VarSize, int)


@given(instance=fiacremm::Process_strategy)
def test_fiacremm::process_VarSize_setter(instance):
    original = instance.VarSize
    instance.VarSize = original
    assert instance.VarSize == original

@given(instance=fiacremm::Transition_strategy)
@settings(max_examples=50)
def test_fiacremm::transition_instantiation(instance):
    assert isinstance(instance, fiacremm::Transition)

@given(instance=fiacremm::Transition_strategy)
def test_fiacremm::transition_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=fiacremm::Transition_strategy)
def test_fiacremm::transition_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=fiacremm::DataType_strategy)
@settings(max_examples=50)
def test_fiacremm::datatype_instantiation(instance):
    assert isinstance(instance, fiacremm::DataType)

@given(instance=fiacremm::DataType_strategy)
def test_fiacremm::datatype_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=fiacremm::DataType_strategy)
def test_fiacremm::datatype_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=fiacremm::Guard_strategy)
@settings(max_examples=50)
def test_fiacremm::guard_instantiation(instance):
    assert isinstance(instance, fiacremm::Guard)

@given(instance=fiacremm::Guard_strategy)
def test_fiacremm::guard_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=fiacremm::Guard_strategy)
def test_fiacremm::guard_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=fiacremm::Guard_strategy)
def test_fiacremm::guard_codeFiacre_type(instance):
    assert isinstance(instance.codeFiacre, str)


@given(instance=fiacremm::Guard_strategy)
def test_fiacremm::guard_codeFiacre_setter(instance):
    original = instance.codeFiacre
    instance.codeFiacre = original
    assert instance.codeFiacre == original

@given(instance=fiacremm::Guard_strategy)
def test_fiacremm::guard_Body_type(instance):
    assert isinstance(instance.Body, str)


@given(instance=fiacremm::Guard_strategy)
def test_fiacremm::guard_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original

@given(instance=fiacremm::Program_strategy)
@settings(max_examples=50)
def test_fiacremm::program_instantiation(instance):
    assert isinstance(instance, fiacremm::Program)

@given(instance=fiacremm::Program_strategy)
def test_fiacremm::program_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=fiacremm::Program_strategy)
def test_fiacremm::program_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=fiacremm::Program_strategy)
def test_fiacremm::program_ComponentSize_type(instance):
    assert isinstance(instance.ComponentSize, int)


@given(instance=fiacremm::Program_strategy)
def test_fiacremm::program_ComponentSize_setter(instance):
    original = instance.ComponentSize
    instance.ComponentSize = original
    assert instance.ComponentSize == original

@given(instance=fiacremm::State_strategy)
@settings(max_examples=50)
def test_fiacremm::state_instantiation(instance):
    assert isinstance(instance, fiacremm::State)

@given(instance=fiacremm::State_strategy)
def test_fiacremm::state_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=fiacremm::State_strategy)
def test_fiacremm::state_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=fiacremm::Variable_strategy)
@settings(max_examples=50)
def test_fiacremm::variable_instantiation(instance):
    assert isinstance(instance, fiacremm::Variable)

@given(instance=fiacremm::Variable_strategy)
def test_fiacremm::variable_initVal_type(instance):
    assert isinstance(instance.initVal, str)


@given(instance=fiacremm::Variable_strategy)
def test_fiacremm::variable_initVal_setter(instance):
    original = instance.initVal
    instance.initVal = original
    assert instance.initVal == original

@given(instance=fiacremm::Variable_strategy)
def test_fiacremm::variable_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=fiacremm::Variable_strategy)
def test_fiacremm::variable_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
