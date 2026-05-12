import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    iot_IotActivity,
    iot_Sketch,
    iot_Board,
    iot_System,
    HWComp,
    iot_Actuator,
    iot_Sensor,
    iot_HWComp,
    iot_IotOperationDef,
    BoardType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iot_iotactivity_is_not_abstract():
    assert not inspect.isabstract(iot_IotActivity)


def test_iot_iotactivity_constructor_exists():
    assert callable(iot_IotActivity.__init__)


def test_iot_iotactivity_constructor_args():
    sig = inspect.signature(iot_IotActivity.__init__)
    params = list(sig.parameters.keys())



def test_iot_sketch_is_not_abstract():
    assert not inspect.isabstract(iot_Sketch)


def test_iot_sketch_constructor_exists():
    assert callable(iot_Sketch.__init__)


def test_iot_sketch_constructor_args():
    sig = inspect.signature(iot_Sketch.__init__)
    params = list(sig.parameters.keys())



def test_iot_board_is_not_abstract():
    assert not inspect.isabstract(iot_Board)


def test_iot_board_constructor_exists():
    assert callable(iot_Board.__init__)


def test_iot_board_constructor_args():
    sig = inspect.signature(iot_Board.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_iot_board_has_name():
    assert hasattr(iot_Board, "name")
    descriptor = None
    for klass in iot_Board.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_iot_board_has_type():
    assert hasattr(iot_Board, "type")
    descriptor = None
    for klass in iot_Board.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_iot_system_is_not_abstract():
    assert not inspect.isabstract(iot_System)


def test_iot_system_constructor_exists():
    assert callable(iot_System.__init__)


def test_iot_system_constructor_args():
    sig = inspect.signature(iot_System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot_system_has_name():
    assert hasattr(iot_System, "name")
    descriptor = None
    for klass in iot_System.__mro__:
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



def test_iot_actuator_is_not_abstract():
    assert not inspect.isabstract(iot_Actuator)


def test_iot_actuator_constructor_exists():
    assert callable(iot_Actuator.__init__)


def test_iot_actuator_constructor_args():
    sig = inspect.signature(iot_Actuator.__init__)
    params = list(sig.parameters.keys())



def test_iot_sensor_is_not_abstract():
    assert not inspect.isabstract(iot_Sensor)


def test_iot_sensor_constructor_exists():
    assert callable(iot_Sensor.__init__)


def test_iot_sensor_constructor_args():
    sig = inspect.signature(iot_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_iot_hwcomp_is_not_abstract():
    assert not inspect.isabstract(iot_HWComp)


def test_iot_hwcomp_constructor_exists():
    assert callable(iot_HWComp.__init__)


def test_iot_hwcomp_constructor_args():
    sig = inspect.signature(iot_HWComp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot_hwcomp_has_name():
    assert hasattr(iot_HWComp, "name")
    descriptor = None
    for klass in iot_HWComp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot_iotoperationdef_is_not_abstract():
    assert not inspect.isabstract(iot_IotOperationDef)


def test_iot_iotoperationdef_constructor_exists():
    assert callable(iot_IotOperationDef.__init__)


def test_iot_iotoperationdef_constructor_args():
    sig = inspect.signature(iot_IotOperationDef.__init__)
    params = list(sig.parameters.keys())

def test_boardtype_exists():
    # Check that the Enumeration exists
    assert BoardType is not None

def test_boardtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BoardType]
    expected_literals = [
        "BeagleBoard",
        "Arduino",
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
iot_IotActivity_strategy = st.builds(
    iot_IotActivity,
)
iot_Sketch_strategy = st.builds(
    iot_Sketch,
)
iot_Board_strategy = st.builds(
    iot_Board,
    name=
        safe_text,
    type=
        safe_text
)
iot_System_strategy = st.builds(
    iot_System,
    name=
        safe_text
)
HWComp_strategy = st.builds(
    HWComp,
)
iot_Actuator_strategy = st.builds(
    iot_Actuator,
)
iot_Sensor_strategy = st.builds(
    iot_Sensor,
)
iot_HWComp_strategy = st.builds(
    iot_HWComp,
    name=
        safe_text
)
iot_IotOperationDef_strategy = st.builds(
    iot_IotOperationDef,
)

@given(instance=iot_IotActivity_strategy)
@settings(max_examples=50)
def test_iot_iotactivity_instantiation(instance):
    assert isinstance(instance, iot_IotActivity)

@given(instance=iot_Sketch_strategy)
@settings(max_examples=50)
def test_iot_sketch_instantiation(instance):
    assert isinstance(instance, iot_Sketch)

@given(instance=iot_Board_strategy)
@settings(max_examples=50)
def test_iot_board_instantiation(instance):
    assert isinstance(instance, iot_Board)



@given(instance=iot_Board_strategy)
def test_iot_board_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=iot_Board_strategy)
def test_iot_board_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=iot_System_strategy)
@settings(max_examples=50)
def test_iot_system_instantiation(instance):
    assert isinstance(instance, iot_System)



@given(instance=iot_System_strategy)
def test_iot_system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HWComp_strategy)
@settings(max_examples=50)
def test_hwcomp_instantiation(instance):
    assert isinstance(instance, HWComp)

@given(instance=iot_Actuator_strategy)
@settings(max_examples=50)
def test_iot_actuator_instantiation(instance):
    assert isinstance(instance, iot_Actuator)

@given(instance=iot_Sensor_strategy)
@settings(max_examples=50)
def test_iot_sensor_instantiation(instance):
    assert isinstance(instance, iot_Sensor)

@given(instance=iot_HWComp_strategy)
@settings(max_examples=50)
def test_iot_hwcomp_instantiation(instance):
    assert isinstance(instance, iot_HWComp)



@given(instance=iot_HWComp_strategy)
def test_iot_hwcomp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot_IotOperationDef_strategy)
@settings(max_examples=50)
def test_iot_iotoperationdef_instantiation(instance):
    assert isinstance(instance, iot_IotOperationDef)
