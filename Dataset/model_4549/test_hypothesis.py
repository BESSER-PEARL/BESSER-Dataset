import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dronesSimulation::Obstacle,
    Observation,
    dronesSimulation::DroneObservation,
    dronesSimulation::ObstacleObservation,
    dronesSimulation::Task,
    dronesSimulation::Observation,
    dronesSimulation::RoleInstance,
    dronesSimulation::Position,
    dronesSimulation::Drone,
    dronesSimulation::DroneInstance,
    dronesSimulation::TaskInstance,
    dronesSimulation::Scenario,
    dronesSimulation::DronesSimulation,
    dronesSimulation::Role,
    TaskState,
    DroneState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dronessimulation::obstacle_is_not_abstract():
    assert not inspect.isabstract(dronesSimulation::Obstacle)


def test_dronessimulation::obstacle_constructor_exists():
    assert callable(dronesSimulation::Obstacle.__init__)


def test_dronessimulation::obstacle_constructor_args():
    sig = inspect.signature(dronesSimulation::Obstacle.__init__)
    params = list(sig.parameters.keys())



def test_observation_is_not_abstract():
    assert not inspect.isabstract(Observation)


def test_observation_constructor_exists():
    assert callable(Observation.__init__)


def test_observation_constructor_args():
    sig = inspect.signature(Observation.__init__)
    params = list(sig.parameters.keys())



def test_dronessimulation::droneobservation_is_not_abstract():
    assert not inspect.isabstract(dronesSimulation::DroneObservation)


def test_dronessimulation::droneobservation_constructor_exists():
    assert callable(dronesSimulation::DroneObservation.__init__)


def test_dronessimulation::droneobservation_constructor_args():
    sig = inspect.signature(dronesSimulation::DroneObservation.__init__)
    params = list(sig.parameters.keys())



def test_dronessimulation::obstacleobservation_is_not_abstract():
    assert not inspect.isabstract(dronesSimulation::ObstacleObservation)


def test_dronessimulation::obstacleobservation_constructor_exists():
    assert callable(dronesSimulation::ObstacleObservation.__init__)


def test_dronessimulation::obstacleobservation_constructor_args():
    sig = inspect.signature(dronesSimulation::ObstacleObservation.__init__)
    params = list(sig.parameters.keys())



def test_dronessimulation::task_is_not_abstract():
    assert not inspect.isabstract(dronesSimulation::Task)


def test_dronessimulation::task_constructor_exists():
    assert callable(dronesSimulation::Task.__init__)


def test_dronessimulation::task_constructor_args():
    sig = inspect.signature(dronesSimulation::Task.__init__)
    params = list(sig.parameters.keys())



def test_dronessimulation::observation_is_not_abstract():
    assert not inspect.isabstract(dronesSimulation::Observation)


def test_dronessimulation::observation_constructor_exists():
    assert callable(dronesSimulation::Observation.__init__)


def test_dronessimulation::observation_constructor_args():
    sig = inspect.signature(dronesSimulation::Observation.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "id" in params, "Missing parameter 'id'"

def test_dronessimulation::observation_has_time():
    assert hasattr(dronesSimulation::Observation, "time")
    descriptor = None
    for klass in dronesSimulation::Observation.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_dronessimulation::observation_has_id():
    assert hasattr(dronesSimulation::Observation, "id")
    descriptor = None
    for klass in dronesSimulation::Observation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dronessimulation::roleinstance_is_not_abstract():
    assert not inspect.isabstract(dronesSimulation::RoleInstance)


def test_dronessimulation::roleinstance_constructor_exists():
    assert callable(dronesSimulation::RoleInstance.__init__)


def test_dronessimulation::roleinstance_constructor_args():
    sig = inspect.signature(dronesSimulation::RoleInstance.__init__)
    params = list(sig.parameters.keys())



def test_dronessimulation::position_is_not_abstract():
    assert not inspect.isabstract(dronesSimulation::Position)


def test_dronessimulation::position_constructor_exists():
    assert callable(dronesSimulation::Position.__init__)


def test_dronessimulation::position_constructor_args():
    sig = inspect.signature(dronesSimulation::Position.__init__)
    params = list(sig.parameters.keys())



def test_dronessimulation::drone_is_not_abstract():
    assert not inspect.isabstract(dronesSimulation::Drone)


def test_dronessimulation::drone_constructor_exists():
    assert callable(dronesSimulation::Drone.__init__)


def test_dronessimulation::drone_constructor_args():
    sig = inspect.signature(dronesSimulation::Drone.__init__)
    params = list(sig.parameters.keys())



def test_dronessimulation::droneinstance_is_not_abstract():
    assert not inspect.isabstract(dronesSimulation::DroneInstance)


def test_dronessimulation::droneinstance_constructor_exists():
    assert callable(dronesSimulation::DroneInstance.__init__)


def test_dronessimulation::droneinstance_constructor_args():
    sig = inspect.signature(dronesSimulation::DroneInstance.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"
    assert "currentBattery" in params, "Missing parameter 'currentBattery'"

def test_dronessimulation::droneinstance_has_state():
    assert hasattr(dronesSimulation::DroneInstance, "state")
    descriptor = None
    for klass in dronesSimulation::DroneInstance.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_dronessimulation::droneinstance_has_currentBattery():
    assert hasattr(dronesSimulation::DroneInstance, "currentBattery")
    descriptor = None
    for klass in dronesSimulation::DroneInstance.__mro__:
        if "currentBattery" in klass.__dict__:
            descriptor = klass.__dict__["currentBattery"]
            break
    assert isinstance(descriptor, property)



def test_dronessimulation::taskinstance_is_not_abstract():
    assert not inspect.isabstract(dronesSimulation::TaskInstance)


def test_dronessimulation::taskinstance_constructor_exists():
    assert callable(dronesSimulation::TaskInstance.__init__)


def test_dronessimulation::taskinstance_constructor_args():
    sig = inspect.signature(dronesSimulation::TaskInstance.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"

def test_dronessimulation::taskinstance_has_state():
    assert hasattr(dronesSimulation::TaskInstance, "state")
    descriptor = None
    for klass in dronesSimulation::TaskInstance.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_dronessimulation::scenario_is_not_abstract():
    assert not inspect.isabstract(dronesSimulation::Scenario)


def test_dronessimulation::scenario_constructor_exists():
    assert callable(dronesSimulation::Scenario.__init__)


def test_dronessimulation::scenario_constructor_args():
    sig = inspect.signature(dronesSimulation::Scenario.__init__)
    params = list(sig.parameters.keys())



def test_dronessimulation::dronessimulation_is_not_abstract():
    assert not inspect.isabstract(dronesSimulation::DronesSimulation)


def test_dronessimulation::dronessimulation_constructor_exists():
    assert callable(dronesSimulation::DronesSimulation.__init__)


def test_dronessimulation::dronessimulation_constructor_args():
    sig = inspect.signature(dronesSimulation::DronesSimulation.__init__)
    params = list(sig.parameters.keys())



def test_dronessimulation::role_is_not_abstract():
    assert not inspect.isabstract(dronesSimulation::Role)


def test_dronessimulation::role_constructor_exists():
    assert callable(dronesSimulation::Role.__init__)


def test_dronessimulation::role_constructor_args():
    sig = inspect.signature(dronesSimulation::Role.__init__)
    params = list(sig.parameters.keys())

def test_taskstate_exists():
    # Check that the Enumeration exists
    assert TaskState is not None

def test_taskstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TaskState]
    expected_literals = [
        "IN_PROGRESS",
        "NOT_STARTED",
        "WAITING",
        "DONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TaskState"

def test_dronestate_exists():
    # Check that the Enumeration exists
    assert DroneState is not None

def test_dronestate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DroneState]
    expected_literals = [
        "CREATED",
        "MOVING",
        "DONE",
        "HOVERING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DroneState"


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
dronesSimulation::Obstacle_strategy = st.builds(
    dronesSimulation::Obstacle,
)
Observation_strategy = st.builds(
    Observation,
)
dronesSimulation::DroneObservation_strategy = st.builds(
    dronesSimulation::DroneObservation,
)
dronesSimulation::ObstacleObservation_strategy = st.builds(
    dronesSimulation::ObstacleObservation,
)
dronesSimulation::Task_strategy = st.builds(
    dronesSimulation::Task,
)
dronesSimulation::Observation_strategy = st.builds(
    dronesSimulation::Observation,
    time=
        safe_text,
    id=
        safe_text
)
dronesSimulation::RoleInstance_strategy = st.builds(
    dronesSimulation::RoleInstance,
)
dronesSimulation::Position_strategy = st.builds(
    dronesSimulation::Position,
)
dronesSimulation::Drone_strategy = st.builds(
    dronesSimulation::Drone,
)
dronesSimulation::DroneInstance_strategy = st.builds(
    dronesSimulation::DroneInstance,
    state=
        safe_text,
    currentBattery=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dronesSimulation::TaskInstance_strategy = st.builds(
    dronesSimulation::TaskInstance,
    state=
        safe_text
)
dronesSimulation::Scenario_strategy = st.builds(
    dronesSimulation::Scenario,
)
dronesSimulation::DronesSimulation_strategy = st.builds(
    dronesSimulation::DronesSimulation,
)
dronesSimulation::Role_strategy = st.builds(
    dronesSimulation::Role,
)

@given(instance=dronesSimulation::Obstacle_strategy)
@settings(max_examples=50)
def test_dronessimulation::obstacle_instantiation(instance):
    assert isinstance(instance, dronesSimulation::Obstacle)

@given(instance=Observation_strategy)
@settings(max_examples=50)
def test_observation_instantiation(instance):
    assert isinstance(instance, Observation)

@given(instance=dronesSimulation::DroneObservation_strategy)
@settings(max_examples=50)
def test_dronessimulation::droneobservation_instantiation(instance):
    assert isinstance(instance, dronesSimulation::DroneObservation)

@given(instance=dronesSimulation::ObstacleObservation_strategy)
@settings(max_examples=50)
def test_dronessimulation::obstacleobservation_instantiation(instance):
    assert isinstance(instance, dronesSimulation::ObstacleObservation)

@given(instance=dronesSimulation::Task_strategy)
@settings(max_examples=50)
def test_dronessimulation::task_instantiation(instance):
    assert isinstance(instance, dronesSimulation::Task)

@given(instance=dronesSimulation::Observation_strategy)
@settings(max_examples=50)
def test_dronessimulation::observation_instantiation(instance):
    assert isinstance(instance, dronesSimulation::Observation)

@given(instance=dronesSimulation::Observation_strategy)
def test_dronessimulation::observation_time_type(instance):
    assert isinstance(instance.time, str)


@given(instance=dronesSimulation::Observation_strategy)
def test_dronessimulation::observation_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=dronesSimulation::Observation_strategy)
def test_dronessimulation::observation_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dronesSimulation::Observation_strategy)
def test_dronessimulation::observation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dronesSimulation::RoleInstance_strategy)
@settings(max_examples=50)
def test_dronessimulation::roleinstance_instantiation(instance):
    assert isinstance(instance, dronesSimulation::RoleInstance)

@given(instance=dronesSimulation::Position_strategy)
@settings(max_examples=50)
def test_dronessimulation::position_instantiation(instance):
    assert isinstance(instance, dronesSimulation::Position)

@given(instance=dronesSimulation::Drone_strategy)
@settings(max_examples=50)
def test_dronessimulation::drone_instantiation(instance):
    assert isinstance(instance, dronesSimulation::Drone)

@given(instance=dronesSimulation::DroneInstance_strategy)
@settings(max_examples=50)
def test_dronessimulation::droneinstance_instantiation(instance):
    assert isinstance(instance, dronesSimulation::DroneInstance)

@given(instance=dronesSimulation::DroneInstance_strategy)
def test_dronessimulation::droneinstance_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=dronesSimulation::DroneInstance_strategy)
def test_dronessimulation::droneinstance_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=dronesSimulation::DroneInstance_strategy)
def test_dronessimulation::droneinstance_currentBattery_type(instance):
    assert isinstance(instance.currentBattery, float)


@given(instance=dronesSimulation::DroneInstance_strategy)
def test_dronessimulation::droneinstance_currentBattery_setter(instance):
    original = instance.currentBattery
    instance.currentBattery = original
    assert instance.currentBattery == original

@given(instance=dronesSimulation::TaskInstance_strategy)
@settings(max_examples=50)
def test_dronessimulation::taskinstance_instantiation(instance):
    assert isinstance(instance, dronesSimulation::TaskInstance)

@given(instance=dronesSimulation::TaskInstance_strategy)
def test_dronessimulation::taskinstance_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=dronesSimulation::TaskInstance_strategy)
def test_dronessimulation::taskinstance_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=dronesSimulation::Scenario_strategy)
@settings(max_examples=50)
def test_dronessimulation::scenario_instantiation(instance):
    assert isinstance(instance, dronesSimulation::Scenario)

@given(instance=dronesSimulation::DronesSimulation_strategy)
@settings(max_examples=50)
def test_dronessimulation::dronessimulation_instantiation(instance):
    assert isinstance(instance, dronesSimulation::DronesSimulation)

@given(instance=dronesSimulation::Role_strategy)
@settings(max_examples=50)
def test_dronessimulation::role_instantiation(instance):
    assert isinstance(instance, dronesSimulation::Role)
