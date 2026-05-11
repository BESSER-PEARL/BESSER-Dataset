import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    iot2::Sketch,
    HWComponent,
    iot2::Actuator,
    iot2::Sensor,
    iot2::OperationDef,
    iot2::Activity,
    iot2::Board,
    iot2::HWComponent,
    iot2::System,
    BoardType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iot2::sketch_is_not_abstract():
    assert not inspect.isabstract(iot2::Sketch)


def test_iot2::sketch_constructor_exists():
    assert callable(iot2::Sketch.__init__)


def test_iot2::sketch_constructor_args():
    sig = inspect.signature(iot2::Sketch.__init__)
    params = list(sig.parameters.keys())



def test_hwcomponent_is_not_abstract():
    assert not inspect.isabstract(HWComponent)


def test_hwcomponent_constructor_exists():
    assert callable(HWComponent.__init__)


def test_hwcomponent_constructor_args():
    sig = inspect.signature(HWComponent.__init__)
    params = list(sig.parameters.keys())



def test_iot2::actuator_is_not_abstract():
    assert not inspect.isabstract(iot2::Actuator)


def test_iot2::actuator_constructor_exists():
    assert callable(iot2::Actuator.__init__)


def test_iot2::actuator_constructor_args():
    sig = inspect.signature(iot2::Actuator.__init__)
    params = list(sig.parameters.keys())



def test_iot2::sensor_is_not_abstract():
    assert not inspect.isabstract(iot2::Sensor)


def test_iot2::sensor_constructor_exists():
    assert callable(iot2::Sensor.__init__)


def test_iot2::sensor_constructor_args():
    sig = inspect.signature(iot2::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_iot2::operationdef_is_not_abstract():
    assert not inspect.isabstract(iot2::OperationDef)


def test_iot2::operationdef_constructor_exists():
    assert callable(iot2::OperationDef.__init__)


def test_iot2::operationdef_constructor_args():
    sig = inspect.signature(iot2::OperationDef.__init__)
    params = list(sig.parameters.keys())



def test_iot2::activity_is_not_abstract():
    assert not inspect.isabstract(iot2::Activity)


def test_iot2::activity_constructor_exists():
    assert callable(iot2::Activity.__init__)


def test_iot2::activity_constructor_args():
    sig = inspect.signature(iot2::Activity.__init__)
    params = list(sig.parameters.keys())



def test_iot2::board_is_not_abstract():
    assert not inspect.isabstract(iot2::Board)


def test_iot2::board_constructor_exists():
    assert callable(iot2::Board.__init__)


def test_iot2::board_constructor_args():
    sig = inspect.signature(iot2::Board.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_iot2::board_has_name():
    assert hasattr(iot2::Board, "name")
    descriptor = None
    for klass in iot2::Board.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_iot2::board_has_type():
    assert hasattr(iot2::Board, "type")
    descriptor = None
    for klass in iot2::Board.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_iot2::hwcomponent_is_not_abstract():
    assert not inspect.isabstract(iot2::HWComponent)


def test_iot2::hwcomponent_constructor_exists():
    assert callable(iot2::HWComponent.__init__)


def test_iot2::hwcomponent_constructor_args():
    sig = inspect.signature(iot2::HWComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot2::hwcomponent_has_name():
    assert hasattr(iot2::HWComponent, "name")
    descriptor = None
    for klass in iot2::HWComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot2::system_is_not_abstract():
    assert not inspect.isabstract(iot2::System)


def test_iot2::system_constructor_exists():
    assert callable(iot2::System.__init__)


def test_iot2::system_constructor_args():
    sig = inspect.signature(iot2::System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot2::system_has_name():
    assert hasattr(iot2::System, "name")
    descriptor = None
    for klass in iot2::System.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_boardtype_exists():
    # Check that the Enumeration exists
    assert BoardType is not None

def test_boardtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BoardType]
    expected_literals = [
        "Arduino",
        "BeagleBoard",
        "RaspberryPi",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BoardType"


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
iot2::Sketch_strategy = st.builds(
    iot2::Sketch,
)
HWComponent_strategy = st.builds(
    HWComponent,
)
iot2::Actuator_strategy = st.builds(
    iot2::Actuator,
)
iot2::Sensor_strategy = st.builds(
    iot2::Sensor,
)
iot2::OperationDef_strategy = st.builds(
    iot2::OperationDef,
)
iot2::Activity_strategy = st.builds(
    iot2::Activity,
)
iot2::Board_strategy = st.builds(
    iot2::Board,
    name=
        safe_text,
    type=
        safe_text
)
iot2::HWComponent_strategy = st.builds(
    iot2::HWComponent,
    name=
        safe_text
)
iot2::System_strategy = st.builds(
    iot2::System,
    name=
        safe_text
)

@given(instance=iot2::Sketch_strategy)
@settings(max_examples=50)
def test_iot2::sketch_instantiation(instance):
    assert isinstance(instance, iot2::Sketch)

@given(instance=HWComponent_strategy)
@settings(max_examples=50)
def test_hwcomponent_instantiation(instance):
    assert isinstance(instance, HWComponent)

@given(instance=iot2::Actuator_strategy)
@settings(max_examples=50)
def test_iot2::actuator_instantiation(instance):
    assert isinstance(instance, iot2::Actuator)

@given(instance=iot2::Sensor_strategy)
@settings(max_examples=50)
def test_iot2::sensor_instantiation(instance):
    assert isinstance(instance, iot2::Sensor)

@given(instance=iot2::OperationDef_strategy)
@settings(max_examples=50)
def test_iot2::operationdef_instantiation(instance):
    assert isinstance(instance, iot2::OperationDef)

@given(instance=iot2::Activity_strategy)
@settings(max_examples=50)
def test_iot2::activity_instantiation(instance):
    assert isinstance(instance, iot2::Activity)

@given(instance=iot2::Board_strategy)
@settings(max_examples=50)
def test_iot2::board_instantiation(instance):
    assert isinstance(instance, iot2::Board)

@given(instance=iot2::Board_strategy)
def test_iot2::board_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iot2::Board_strategy)
def test_iot2::board_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot2::Board_strategy)
def test_iot2::board_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=iot2::Board_strategy)
def test_iot2::board_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=iot2::HWComponent_strategy)
@settings(max_examples=50)
def test_iot2::hwcomponent_instantiation(instance):
    assert isinstance(instance, iot2::HWComponent)

@given(instance=iot2::HWComponent_strategy)
def test_iot2::hwcomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iot2::HWComponent_strategy)
def test_iot2::hwcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot2::System_strategy)
@settings(max_examples=50)
def test_iot2::system_instantiation(instance):
    assert isinstance(instance, iot2::System)

@given(instance=iot2::System_strategy)
def test_iot2::system_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iot2::System_strategy)
def test_iot2::system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
