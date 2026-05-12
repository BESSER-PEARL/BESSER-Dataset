import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ControlTask,
    mission_Join,
    mission_Fork,
    Task,
    mission_PointTask,
    mission_PolygonTask,
    mission_LineTask,
    mission_ControlTask,
    mission_Coordinate,
    mission_Swarm,
    NamedElement,
    mission_TaskDependency,
    mission_Drone,
    mission_Task,
    mission_Mission,
    mission_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_controltask_is_not_abstract():
    assert not inspect.isabstract(ControlTask)


def test_controltask_constructor_exists():
    assert callable(ControlTask.__init__)


def test_controltask_constructor_args():
    sig = inspect.signature(ControlTask.__init__)
    params = list(sig.parameters.keys())



def test_mission_join_is_not_abstract():
    assert not inspect.isabstract(mission_Join)


def test_mission_join_constructor_exists():
    assert callable(mission_Join.__init__)


def test_mission_join_constructor_args():
    sig = inspect.signature(mission_Join.__init__)
    params = list(sig.parameters.keys())



def test_mission_fork_is_not_abstract():
    assert not inspect.isabstract(mission_Fork)


def test_mission_fork_constructor_exists():
    assert callable(mission_Fork.__init__)


def test_mission_fork_constructor_args():
    sig = inspect.signature(mission_Fork.__init__)
    params = list(sig.parameters.keys())



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_mission_pointtask_is_not_abstract():
    assert not inspect.isabstract(mission_PointTask)


def test_mission_pointtask_constructor_exists():
    assert callable(mission_PointTask.__init__)


def test_mission_pointtask_constructor_args():
    sig = inspect.signature(mission_PointTask.__init__)
    params = list(sig.parameters.keys())



def test_mission_polygontask_is_not_abstract():
    assert not inspect.isabstract(mission_PolygonTask)


def test_mission_polygontask_constructor_exists():
    assert callable(mission_PolygonTask.__init__)


def test_mission_polygontask_constructor_args():
    sig = inspect.signature(mission_PolygonTask.__init__)
    params = list(sig.parameters.keys())



def test_mission_linetask_is_not_abstract():
    assert not inspect.isabstract(mission_LineTask)


def test_mission_linetask_constructor_exists():
    assert callable(mission_LineTask.__init__)


def test_mission_linetask_constructor_args():
    sig = inspect.signature(mission_LineTask.__init__)
    params = list(sig.parameters.keys())



def test_mission_controltask_is_not_abstract():
    assert not inspect.isabstract(mission_ControlTask)


def test_mission_controltask_constructor_exists():
    assert callable(mission_ControlTask.__init__)


def test_mission_controltask_constructor_args():
    sig = inspect.signature(mission_ControlTask.__init__)
    params = list(sig.parameters.keys())



def test_mission_coordinate_is_not_abstract():
    assert not inspect.isabstract(mission_Coordinate)


def test_mission_coordinate_constructor_exists():
    assert callable(mission_Coordinate.__init__)


def test_mission_coordinate_constructor_args():
    sig = inspect.signature(mission_Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "latitude" in params, "Missing parameter 'latitude'"
    assert "longitude" in params, "Missing parameter 'longitude'"
    assert "altitude" in params, "Missing parameter 'altitude'"

def test_mission_coordinate_has_latitude():
    assert hasattr(mission_Coordinate, "latitude")
    descriptor = None
    for klass in mission_Coordinate.__mro__:
        if "latitude" in klass.__dict__:
            descriptor = klass.__dict__["latitude"]
            break
    assert isinstance(descriptor, property)

def test_mission_coordinate_has_longitude():
    assert hasattr(mission_Coordinate, "longitude")
    descriptor = None
    for klass in mission_Coordinate.__mro__:
        if "longitude" in klass.__dict__:
            descriptor = klass.__dict__["longitude"]
            break
    assert isinstance(descriptor, property)

def test_mission_coordinate_has_altitude():
    assert hasattr(mission_Coordinate, "altitude")
    descriptor = None
    for klass in mission_Coordinate.__mro__:
        if "altitude" in klass.__dict__:
            descriptor = klass.__dict__["altitude"]
            break
    assert isinstance(descriptor, property)



def test_mission_swarm_is_not_abstract():
    assert not inspect.isabstract(mission_Swarm)


def test_mission_swarm_constructor_exists():
    assert callable(mission_Swarm.__init__)


def test_mission_swarm_constructor_args():
    sig = inspect.signature(mission_Swarm.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_mission_taskdependency_is_not_abstract():
    assert not inspect.isabstract(mission_TaskDependency)


def test_mission_taskdependency_constructor_exists():
    assert callable(mission_TaskDependency.__init__)


def test_mission_taskdependency_constructor_args():
    sig = inspect.signature(mission_TaskDependency.__init__)
    params = list(sig.parameters.keys())



def test_mission_drone_is_not_abstract():
    assert not inspect.isabstract(mission_Drone)


def test_mission_drone_constructor_exists():
    assert callable(mission_Drone.__init__)


def test_mission_drone_constructor_args():
    sig = inspect.signature(mission_Drone.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "returnHome" in params, "Missing parameter 'returnHome'"

def test_mission_drone_has_type():
    assert hasattr(mission_Drone, "type")
    descriptor = None
    for klass in mission_Drone.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mission_drone_has_returnHome():
    assert hasattr(mission_Drone, "returnHome")
    descriptor = None
    for klass in mission_Drone.__mro__:
        if "returnHome" in klass.__dict__:
            descriptor = klass.__dict__["returnHome"]
            break
    assert isinstance(descriptor, property)



def test_mission_task_is_not_abstract():
    assert not inspect.isabstract(mission_Task)


def test_mission_task_constructor_exists():
    assert callable(mission_Task.__init__)


def test_mission_task_constructor_args():
    sig = inspect.signature(mission_Task.__init__)
    params = list(sig.parameters.keys())



def test_mission_mission_is_not_abstract():
    assert not inspect.isabstract(mission_Mission)


def test_mission_mission_constructor_exists():
    assert callable(mission_Mission.__init__)


def test_mission_mission_constructor_args():
    sig = inspect.signature(mission_Mission.__init__)
    params = list(sig.parameters.keys())
    assert "crs" in params, "Missing parameter 'crs'"

def test_mission_mission_has_crs():
    assert hasattr(mission_Mission, "crs")
    descriptor = None
    for klass in mission_Mission.__mro__:
        if "crs" in klass.__dict__:
            descriptor = klass.__dict__["crs"]
            break
    assert isinstance(descriptor, property)



def test_mission_namedelement_is_not_abstract():
    assert not inspect.isabstract(mission_NamedElement)


def test_mission_namedelement_constructor_exists():
    assert callable(mission_NamedElement.__init__)


def test_mission_namedelement_constructor_args():
    sig = inspect.signature(mission_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mission_namedelement_has_name():
    assert hasattr(mission_NamedElement, "name")
    descriptor = None
    for klass in mission_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
ControlTask_strategy = st.builds(
    ControlTask,
)
mission_Join_strategy = st.builds(
    mission_Join,
)
mission_Fork_strategy = st.builds(
    mission_Fork,
)
Task_strategy = st.builds(
    Task,
)
mission_PointTask_strategy = st.builds(
    mission_PointTask,
)
mission_PolygonTask_strategy = st.builds(
    mission_PolygonTask,
)
mission_LineTask_strategy = st.builds(
    mission_LineTask,
)
mission_ControlTask_strategy = st.builds(
    mission_ControlTask,
)
mission_Coordinate_strategy = st.builds(
    mission_Coordinate,
    latitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    longitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    altitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
mission_Swarm_strategy = st.builds(
    mission_Swarm,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
mission_TaskDependency_strategy = st.builds(
    mission_TaskDependency,
)
mission_Drone_strategy = st.builds(
    mission_Drone,
    type=
        safe_text,
    returnHome=
        st.booleans()
)
mission_Task_strategy = st.builds(
    mission_Task,
)
mission_Mission_strategy = st.builds(
    mission_Mission,
    crs=
        safe_text
)
mission_NamedElement_strategy = st.builds(
    mission_NamedElement,
    name=
        safe_text
)

@given(instance=ControlTask_strategy)
@settings(max_examples=50)
def test_controltask_instantiation(instance):
    assert isinstance(instance, ControlTask)

@given(instance=mission_Join_strategy)
@settings(max_examples=50)
def test_mission_join_instantiation(instance):
    assert isinstance(instance, mission_Join)

@given(instance=mission_Fork_strategy)
@settings(max_examples=50)
def test_mission_fork_instantiation(instance):
    assert isinstance(instance, mission_Fork)

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=mission_PointTask_strategy)
@settings(max_examples=50)
def test_mission_pointtask_instantiation(instance):
    assert isinstance(instance, mission_PointTask)

@given(instance=mission_PolygonTask_strategy)
@settings(max_examples=50)
def test_mission_polygontask_instantiation(instance):
    assert isinstance(instance, mission_PolygonTask)

@given(instance=mission_LineTask_strategy)
@settings(max_examples=50)
def test_mission_linetask_instantiation(instance):
    assert isinstance(instance, mission_LineTask)

@given(instance=mission_ControlTask_strategy)
@settings(max_examples=50)
def test_mission_controltask_instantiation(instance):
    assert isinstance(instance, mission_ControlTask)

@given(instance=mission_Coordinate_strategy)
@settings(max_examples=50)
def test_mission_coordinate_instantiation(instance):
    assert isinstance(instance, mission_Coordinate)



@given(instance=mission_Coordinate_strategy)
def test_mission_coordinate_latitude_setter(instance):
    original = instance.latitude
    instance.latitude = original
    assert instance.latitude == original



@given(instance=mission_Coordinate_strategy)
def test_mission_coordinate_longitude_setter(instance):
    original = instance.longitude
    instance.longitude = original
    assert instance.longitude == original



@given(instance=mission_Coordinate_strategy)
def test_mission_coordinate_altitude_setter(instance):
    original = instance.altitude
    instance.altitude = original
    assert instance.altitude == original

@given(instance=mission_Swarm_strategy)
@settings(max_examples=50)
def test_mission_swarm_instantiation(instance):
    assert isinstance(instance, mission_Swarm)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=mission_TaskDependency_strategy)
@settings(max_examples=50)
def test_mission_taskdependency_instantiation(instance):
    assert isinstance(instance, mission_TaskDependency)

@given(instance=mission_Drone_strategy)
@settings(max_examples=50)
def test_mission_drone_instantiation(instance):
    assert isinstance(instance, mission_Drone)



@given(instance=mission_Drone_strategy)
def test_mission_drone_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=mission_Drone_strategy)
def test_mission_drone_returnHome_setter(instance):
    original = instance.returnHome
    instance.returnHome = original
    assert instance.returnHome == original

@given(instance=mission_Task_strategy)
@settings(max_examples=50)
def test_mission_task_instantiation(instance):
    assert isinstance(instance, mission_Task)

@given(instance=mission_Mission_strategy)
@settings(max_examples=50)
def test_mission_mission_instantiation(instance):
    assert isinstance(instance, mission_Mission)



@given(instance=mission_Mission_strategy)
def test_mission_mission_crs_setter(instance):
    original = instance.crs
    instance.crs = original
    assert instance.crs == original

@given(instance=mission_NamedElement_strategy)
@settings(max_examples=50)
def test_mission_namedelement_instantiation(instance):
    assert isinstance(instance, mission_NamedElement)



@given(instance=mission_NamedElement_strategy)
def test_mission_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
