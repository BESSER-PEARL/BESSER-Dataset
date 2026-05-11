import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    iot::IotActivity,
    iot::Sketch,
    iot::Board,
    iot::System,
    HWComp,
    iot::Actuator,
    iot::Sensor,
    iot::HWComp,
    iot::IotOperationDef,
    BoardType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iot::iotactivity_is_not_abstract():
    assert not inspect.isabstract(iot::IotActivity)


def test_iot::iotactivity_constructor_exists():
    assert callable(iot::IotActivity.__init__)


def test_iot::iotactivity_constructor_args():
    sig = inspect.signature(iot::IotActivity.__init__)
    params = list(sig.parameters.keys())



def test_iot::sketch_is_not_abstract():
    assert not inspect.isabstract(iot::Sketch)


def test_iot::sketch_constructor_exists():
    assert callable(iot::Sketch.__init__)


def test_iot::sketch_constructor_args():
    sig = inspect.signature(iot::Sketch.__init__)
    params = list(sig.parameters.keys())



def test_iot::board_is_not_abstract():
    assert not inspect.isabstract(iot::Board)


def test_iot::board_constructor_exists():
    assert callable(iot::Board.__init__)


def test_iot::board_constructor_args():
    sig = inspect.signature(iot::Board.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_iot::board_has_name():
    assert hasattr(iot::Board, "name")
    descriptor = None
    for klass in iot::Board.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_iot::board_has_type():
    assert hasattr(iot::Board, "type")
    descriptor = None
    for klass in iot::Board.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_iot::system_is_not_abstract():
    assert not inspect.isabstract(iot::System)


def test_iot::system_constructor_exists():
    assert callable(iot::System.__init__)


def test_iot::system_constructor_args():
    sig = inspect.signature(iot::System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot::system_has_name():
    assert hasattr(iot::System, "name")
    descriptor = None
    for klass in iot::System.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hwcomp_is_not_abstract():
    assert not inspect.isabstract(HWComp)


def test_hwcomp_constructor_exists():
    assert callable(HWComp.__init__)


def test_hwcomp_constructor_args():
    sig = inspect.signature(HWComp.__init__)
    params = list(sig.parameters.keys())



def test_iot::actuator_is_not_abstract():
    assert not inspect.isabstract(iot::Actuator)


def test_iot::actuator_constructor_exists():
    assert callable(iot::Actuator.__init__)


def test_iot::actuator_constructor_args():
    sig = inspect.signature(iot::Actuator.__init__)
    params = list(sig.parameters.keys())



def test_iot::sensor_is_not_abstract():
    assert not inspect.isabstract(iot::Sensor)


def test_iot::sensor_constructor_exists():
    assert callable(iot::Sensor.__init__)


def test_iot::sensor_constructor_args():
    sig = inspect.signature(iot::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_iot::hwcomp_is_not_abstract():
    assert not inspect.isabstract(iot::HWComp)


def test_iot::hwcomp_constructor_exists():
    assert callable(iot::HWComp.__init__)


def test_iot::hwcomp_constructor_args():
    sig = inspect.signature(iot::HWComp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot::hwcomp_has_name():
    assert hasattr(iot::HWComp, "name")
    descriptor = None
    for klass in iot::HWComp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot::iotoperationdef_is_not_abstract():
    assert not inspect.isabstract(iot::IotOperationDef)


def test_iot::iotoperationdef_constructor_exists():
    assert callable(iot::IotOperationDef.__init__)


def test_iot::iotoperationdef_constructor_args():
    sig = inspect.signature(iot::IotOperationDef.__init__)
    params = list(sig.parameters.keys())

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
iot::IotActivity_strategy = st.builds(
    iot::IotActivity,
)
iot::Sketch_strategy = st.builds(
    iot::Sketch,
)
iot::Board_strategy = st.builds(
    iot::Board,
    name=
        safe_text,
    type=
        safe_text
)
iot::System_strategy = st.builds(
    iot::System,
    name=
        safe_text
)
HWComp_strategy = st.builds(
    HWComp,
)
iot::Actuator_strategy = st.builds(
    iot::Actuator,
)
iot::Sensor_strategy = st.builds(
    iot::Sensor,
)
iot::HWComp_strategy = st.builds(
    iot::HWComp,
    name=
        safe_text
)
iot::IotOperationDef_strategy = st.builds(
    iot::IotOperationDef,
)

@given(instance=iot::IotActivity_strategy)
@settings(max_examples=50)
def test_iot::iotactivity_instantiation(instance):
    assert isinstance(instance, iot::IotActivity)

@given(instance=iot::Sketch_strategy)
@settings(max_examples=50)
def test_iot::sketch_instantiation(instance):
    assert isinstance(instance, iot::Sketch)

@given(instance=iot::Board_strategy)
@settings(max_examples=50)
def test_iot::board_instantiation(instance):
    assert isinstance(instance, iot::Board)

@given(instance=iot::Board_strategy)
def test_iot::board_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iot::Board_strategy)
def test_iot::board_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot::Board_strategy)
def test_iot::board_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=iot::Board_strategy)
def test_iot::board_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=iot::System_strategy)
@settings(max_examples=50)
def test_iot::system_instantiation(instance):
    assert isinstance(instance, iot::System)

@given(instance=iot::System_strategy)
def test_iot::system_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iot::System_strategy)
def test_iot::system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HWComp_strategy)
@settings(max_examples=50)
def test_hwcomp_instantiation(instance):
    assert isinstance(instance, HWComp)

@given(instance=iot::Actuator_strategy)
@settings(max_examples=50)
def test_iot::actuator_instantiation(instance):
    assert isinstance(instance, iot::Actuator)

@given(instance=iot::Sensor_strategy)
@settings(max_examples=50)
def test_iot::sensor_instantiation(instance):
    assert isinstance(instance, iot::Sensor)

@given(instance=iot::HWComp_strategy)
@settings(max_examples=50)
def test_iot::hwcomp_instantiation(instance):
    assert isinstance(instance, iot::HWComp)

@given(instance=iot::HWComp_strategy)
def test_iot::hwcomp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iot::HWComp_strategy)
def test_iot::hwcomp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot::IotOperationDef_strategy)
@settings(max_examples=50)
def test_iot::iotoperationdef_instantiation(instance):
    assert isinstance(instance, iot::IotOperationDef)
