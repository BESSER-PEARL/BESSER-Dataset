import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    iot2_Sketch,
    HWComponent,
    iot2_Actuator,
    iot2_Sensor,
    iot2_OperationDef,
    iot2_Activity,
    iot2_Board,
    iot2_HWComponent,
    iot2_System,
    BoardType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iot2_sketch_is_not_abstract():
    assert not inspect.isabstract(iot2_Sketch)


def test_iot2_sketch_constructor_exists():
    assert callable(iot2_Sketch.__init__)


def test_iot2_sketch_constructor_args():
    sig = inspect.signature(iot2_Sketch.__init__)
    params = list(sig.parameters.keys())



def test_hwcomponent_is_not_abstract():
    assert not inspect.isabstract(HWComponent)


def test_hwcomponent_constructor_exists():
    assert callable(HWComponent.__init__)


def test_hwcomponent_constructor_args():
    sig = inspect.signature(HWComponent.__init__)
    params = list(sig.parameters.keys())



def test_iot2_actuator_is_not_abstract():
    assert not inspect.isabstract(iot2_Actuator)


def test_iot2_actuator_constructor_exists():
    assert callable(iot2_Actuator.__init__)


def test_iot2_actuator_constructor_args():
    sig = inspect.signature(iot2_Actuator.__init__)
    params = list(sig.parameters.keys())



def test_iot2_sensor_is_not_abstract():
    assert not inspect.isabstract(iot2_Sensor)


def test_iot2_sensor_constructor_exists():
    assert callable(iot2_Sensor.__init__)


def test_iot2_sensor_constructor_args():
    sig = inspect.signature(iot2_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_iot2_operationdef_is_not_abstract():
    assert not inspect.isabstract(iot2_OperationDef)


def test_iot2_operationdef_constructor_exists():
    assert callable(iot2_OperationDef.__init__)


def test_iot2_operationdef_constructor_args():
    sig = inspect.signature(iot2_OperationDef.__init__)
    params = list(sig.parameters.keys())



def test_iot2_activity_is_not_abstract():
    assert not inspect.isabstract(iot2_Activity)


def test_iot2_activity_constructor_exists():
    assert callable(iot2_Activity.__init__)


def test_iot2_activity_constructor_args():
    sig = inspect.signature(iot2_Activity.__init__)
    params = list(sig.parameters.keys())



def test_iot2_board_is_not_abstract():
    assert not inspect.isabstract(iot2_Board)


def test_iot2_board_constructor_exists():
    assert callable(iot2_Board.__init__)


def test_iot2_board_constructor_args():
    sig = inspect.signature(iot2_Board.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_iot2_board_has_type():
    assert hasattr(iot2_Board, "type")
    descriptor = None
    for klass in iot2_Board.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_iot2_board_has_name():
    assert hasattr(iot2_Board, "name")
    descriptor = None
    for klass in iot2_Board.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot2_hwcomponent_is_not_abstract():
    assert not inspect.isabstract(iot2_HWComponent)


def test_iot2_hwcomponent_constructor_exists():
    assert callable(iot2_HWComponent.__init__)


def test_iot2_hwcomponent_constructor_args():
    sig = inspect.signature(iot2_HWComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot2_hwcomponent_has_name():
    assert hasattr(iot2_HWComponent, "name")
    descriptor = None
    for klass in iot2_HWComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot2_system_is_not_abstract():
    assert not inspect.isabstract(iot2_System)


def test_iot2_system_constructor_exists():
    assert callable(iot2_System.__init__)


def test_iot2_system_constructor_args():
    sig = inspect.signature(iot2_System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot2_system_has_name():
    assert hasattr(iot2_System, "name")
    descriptor = None
    for klass in iot2_System.__mro__:
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
iot2_Sketch_strategy = st.builds(
    iot2_Sketch,
)
HWComponent_strategy = st.builds(
    HWComponent,
)
iot2_Actuator_strategy = st.builds(
    iot2_Actuator,
)
iot2_Sensor_strategy = st.builds(
    iot2_Sensor,
)
iot2_OperationDef_strategy = st.builds(
    iot2_OperationDef,
)
iot2_Activity_strategy = st.builds(
    iot2_Activity,
)
iot2_Board_strategy = st.builds(
    iot2_Board,
    type=
        safe_text,
    name=
        safe_text
)
iot2_HWComponent_strategy = st.builds(
    iot2_HWComponent,
    name=
        safe_text
)
iot2_System_strategy = st.builds(
    iot2_System,
    name=
        safe_text
)

@given(instance=iot2_Sketch_strategy)
@settings(max_examples=50)
def test_iot2_sketch_instantiation(instance):
    assert isinstance(instance, iot2_Sketch)

@given(instance=HWComponent_strategy)
@settings(max_examples=50)
def test_hwcomponent_instantiation(instance):
    assert isinstance(instance, HWComponent)

@given(instance=iot2_Actuator_strategy)
@settings(max_examples=50)
def test_iot2_actuator_instantiation(instance):
    assert isinstance(instance, iot2_Actuator)

@given(instance=iot2_Sensor_strategy)
@settings(max_examples=50)
def test_iot2_sensor_instantiation(instance):
    assert isinstance(instance, iot2_Sensor)

@given(instance=iot2_OperationDef_strategy)
@settings(max_examples=50)
def test_iot2_operationdef_instantiation(instance):
    assert isinstance(instance, iot2_OperationDef)

@given(instance=iot2_Activity_strategy)
@settings(max_examples=50)
def test_iot2_activity_instantiation(instance):
    assert isinstance(instance, iot2_Activity)

@given(instance=iot2_Board_strategy)
@settings(max_examples=50)
def test_iot2_board_instantiation(instance):
    assert isinstance(instance, iot2_Board)



@given(instance=iot2_Board_strategy)
def test_iot2_board_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=iot2_Board_strategy)
def test_iot2_board_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot2_HWComponent_strategy)
@settings(max_examples=50)
def test_iot2_hwcomponent_instantiation(instance):
    assert isinstance(instance, iot2_HWComponent)



@given(instance=iot2_HWComponent_strategy)
def test_iot2_hwcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot2_System_strategy)
@settings(max_examples=50)
def test_iot2_system_instantiation(instance):
    assert isinstance(instance, iot2_System)



@given(instance=iot2_System_strategy)
def test_iot2_system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
