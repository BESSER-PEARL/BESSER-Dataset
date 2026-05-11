import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ControlTask,
    mission::Join,
    mission::Fork,
    Task,
    mission::PolygonTask,
    mission::PointTask,
    mission::LineTask,
    mission::ControlTask,
    mission::Coordinate,
    mission::Swarm,
    NamedElement,
    mission::Drone,
    mission::Task,
    mission::TaskDependency,
    mission::Mission,
    mission::NamedElement,
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



def test_mission::join_is_not_abstract():
    assert not inspect.isabstract(mission::Join)


def test_mission::join_constructor_exists():
    assert callable(mission::Join.__init__)


def test_mission::join_constructor_args():
    sig = inspect.signature(mission::Join.__init__)
    params = list(sig.parameters.keys())



def test_mission::fork_is_not_abstract():
    assert not inspect.isabstract(mission::Fork)


def test_mission::fork_constructor_exists():
    assert callable(mission::Fork.__init__)


def test_mission::fork_constructor_args():
    sig = inspect.signature(mission::Fork.__init__)
    params = list(sig.parameters.keys())



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_mission::polygontask_is_not_abstract():
    assert not inspect.isabstract(mission::PolygonTask)


def test_mission::polygontask_constructor_exists():
    assert callable(mission::PolygonTask.__init__)


def test_mission::polygontask_constructor_args():
    sig = inspect.signature(mission::PolygonTask.__init__)
    params = list(sig.parameters.keys())



def test_mission::pointtask_is_not_abstract():
    assert not inspect.isabstract(mission::PointTask)


def test_mission::pointtask_constructor_exists():
    assert callable(mission::PointTask.__init__)


def test_mission::pointtask_constructor_args():
    sig = inspect.signature(mission::PointTask.__init__)
    params = list(sig.parameters.keys())



def test_mission::linetask_is_not_abstract():
    assert not inspect.isabstract(mission::LineTask)


def test_mission::linetask_constructor_exists():
    assert callable(mission::LineTask.__init__)


def test_mission::linetask_constructor_args():
    sig = inspect.signature(mission::LineTask.__init__)
    params = list(sig.parameters.keys())



def test_mission::controltask_is_not_abstract():
    assert not inspect.isabstract(mission::ControlTask)


def test_mission::controltask_constructor_exists():
    assert callable(mission::ControlTask.__init__)


def test_mission::controltask_constructor_args():
    sig = inspect.signature(mission::ControlTask.__init__)
    params = list(sig.parameters.keys())



def test_mission::coordinate_is_not_abstract():
    assert not inspect.isabstract(mission::Coordinate)


def test_mission::coordinate_constructor_exists():
    assert callable(mission::Coordinate.__init__)


def test_mission::coordinate_constructor_args():
    sig = inspect.signature(mission::Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "latitude" in params, "Missing parameter 'latitude'"
    assert "longitude" in params, "Missing parameter 'longitude'"
    assert "altitude" in params, "Missing parameter 'altitude'"

def test_mission::coordinate_has_latitude():
    assert hasattr(mission::Coordinate, "latitude")
    descriptor = None
    for klass in mission::Coordinate.__mro__:
        if "latitude" in klass.__dict__:
            descriptor = klass.__dict__["latitude"]
            break
    assert isinstance(descriptor, property)

def test_mission::coordinate_has_longitude():
    assert hasattr(mission::Coordinate, "longitude")
    descriptor = None
    for klass in mission::Coordinate.__mro__:
        if "longitude" in klass.__dict__:
            descriptor = klass.__dict__["longitude"]
            break
    assert isinstance(descriptor, property)

def test_mission::coordinate_has_altitude():
    assert hasattr(mission::Coordinate, "altitude")
    descriptor = None
    for klass in mission::Coordinate.__mro__:
        if "altitude" in klass.__dict__:
            descriptor = klass.__dict__["altitude"]
            break
    assert isinstance(descriptor, property)



def test_mission::swarm_is_not_abstract():
    assert not inspect.isabstract(mission::Swarm)


def test_mission::swarm_constructor_exists():
    assert callable(mission::Swarm.__init__)


def test_mission::swarm_constructor_args():
    sig = inspect.signature(mission::Swarm.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_mission::drone_is_not_abstract():
    assert not inspect.isabstract(mission::Drone)


def test_mission::drone_constructor_exists():
    assert callable(mission::Drone.__init__)


def test_mission::drone_constructor_args():
    sig = inspect.signature(mission::Drone.__init__)
    params = list(sig.parameters.keys())
    assert "returnHome" in params, "Missing parameter 'returnHome'"
    assert "type" in params, "Missing parameter 'type'"

def test_mission::drone_has_returnHome():
    assert hasattr(mission::Drone, "returnHome")
    descriptor = None
    for klass in mission::Drone.__mro__:
        if "returnHome" in klass.__dict__:
            descriptor = klass.__dict__["returnHome"]
            break
    assert isinstance(descriptor, property)

def test_mission::drone_has_type():
    assert hasattr(mission::Drone, "type")
    descriptor = None
    for klass in mission::Drone.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mission::task_is_not_abstract():
    assert not inspect.isabstract(mission::Task)


def test_mission::task_constructor_exists():
    assert callable(mission::Task.__init__)


def test_mission::task_constructor_args():
    sig = inspect.signature(mission::Task.__init__)
    params = list(sig.parameters.keys())



def test_mission::taskdependency_is_not_abstract():
    assert not inspect.isabstract(mission::TaskDependency)


def test_mission::taskdependency_constructor_exists():
    assert callable(mission::TaskDependency.__init__)


def test_mission::taskdependency_constructor_args():
    sig = inspect.signature(mission::TaskDependency.__init__)
    params = list(sig.parameters.keys())



def test_mission::mission_is_not_abstract():
    assert not inspect.isabstract(mission::Mission)


def test_mission::mission_constructor_exists():
    assert callable(mission::Mission.__init__)


def test_mission::mission_constructor_args():
    sig = inspect.signature(mission::Mission.__init__)
    params = list(sig.parameters.keys())
    assert "crs" in params, "Missing parameter 'crs'"

def test_mission::mission_has_crs():
    assert hasattr(mission::Mission, "crs")
    descriptor = None
    for klass in mission::Mission.__mro__:
        if "crs" in klass.__dict__:
            descriptor = klass.__dict__["crs"]
            break
    assert isinstance(descriptor, property)



def test_mission::namedelement_is_not_abstract():
    assert not inspect.isabstract(mission::NamedElement)


def test_mission::namedelement_constructor_exists():
    assert callable(mission::NamedElement.__init__)


def test_mission::namedelement_constructor_args():
    sig = inspect.signature(mission::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mission::namedelement_has_name():
    assert hasattr(mission::NamedElement, "name")
    descriptor = None
    for klass in mission::NamedElement.__mro__:
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
mission::Join_strategy = st.builds(
    mission::Join,
)
mission::Fork_strategy = st.builds(
    mission::Fork,
)
Task_strategy = st.builds(
    Task,
)
mission::PolygonTask_strategy = st.builds(
    mission::PolygonTask,
)
mission::PointTask_strategy = st.builds(
    mission::PointTask,
)
mission::LineTask_strategy = st.builds(
    mission::LineTask,
)
mission::ControlTask_strategy = st.builds(
    mission::ControlTask,
)
mission::Coordinate_strategy = st.builds(
    mission::Coordinate,
    latitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    longitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    altitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
mission::Swarm_strategy = st.builds(
    mission::Swarm,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
mission::Drone_strategy = st.builds(
    mission::Drone,
    returnHome=
        st.booleans(),
    type=
        safe_text
)
mission::Task_strategy = st.builds(
    mission::Task,
)
mission::TaskDependency_strategy = st.builds(
    mission::TaskDependency,
)
mission::Mission_strategy = st.builds(
    mission::Mission,
    crs=
        safe_text
)
mission::NamedElement_strategy = st.builds(
    mission::NamedElement,
    name=
        safe_text
)

@given(instance=ControlTask_strategy)
@settings(max_examples=50)
def test_controltask_instantiation(instance):
    assert isinstance(instance, ControlTask)

@given(instance=mission::Join_strategy)
@settings(max_examples=50)
def test_mission::join_instantiation(instance):
    assert isinstance(instance, mission::Join)

@given(instance=mission::Fork_strategy)
@settings(max_examples=50)
def test_mission::fork_instantiation(instance):
    assert isinstance(instance, mission::Fork)

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=mission::PolygonTask_strategy)
@settings(max_examples=50)
def test_mission::polygontask_instantiation(instance):
    assert isinstance(instance, mission::PolygonTask)

@given(instance=mission::PointTask_strategy)
@settings(max_examples=50)
def test_mission::pointtask_instantiation(instance):
    assert isinstance(instance, mission::PointTask)

@given(instance=mission::LineTask_strategy)
@settings(max_examples=50)
def test_mission::linetask_instantiation(instance):
    assert isinstance(instance, mission::LineTask)

@given(instance=mission::ControlTask_strategy)
@settings(max_examples=50)
def test_mission::controltask_instantiation(instance):
    assert isinstance(instance, mission::ControlTask)

@given(instance=mission::Coordinate_strategy)
@settings(max_examples=50)
def test_mission::coordinate_instantiation(instance):
    assert isinstance(instance, mission::Coordinate)

@given(instance=mission::Coordinate_strategy)
def test_mission::coordinate_latitude_type(instance):
    assert isinstance(instance.latitude, float)


@given(instance=mission::Coordinate_strategy)
def test_mission::coordinate_latitude_setter(instance):
    original = instance.latitude
    instance.latitude = original
    assert instance.latitude == original

@given(instance=mission::Coordinate_strategy)
def test_mission::coordinate_longitude_type(instance):
    assert isinstance(instance.longitude, float)


@given(instance=mission::Coordinate_strategy)
def test_mission::coordinate_longitude_setter(instance):
    original = instance.longitude
    instance.longitude = original
    assert instance.longitude == original

@given(instance=mission::Coordinate_strategy)
def test_mission::coordinate_altitude_type(instance):
    assert isinstance(instance.altitude, float)


@given(instance=mission::Coordinate_strategy)
def test_mission::coordinate_altitude_setter(instance):
    original = instance.altitude
    instance.altitude = original
    assert instance.altitude == original

@given(instance=mission::Swarm_strategy)
@settings(max_examples=50)
def test_mission::swarm_instantiation(instance):
    assert isinstance(instance, mission::Swarm)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=mission::Drone_strategy)
@settings(max_examples=50)
def test_mission::drone_instantiation(instance):
    assert isinstance(instance, mission::Drone)

@given(instance=mission::Drone_strategy)
def test_mission::drone_returnHome_type(instance):
    assert isinstance(instance.returnHome, bool)


@given(instance=mission::Drone_strategy)
def test_mission::drone_returnHome_setter(instance):
    original = instance.returnHome
    instance.returnHome = original
    assert instance.returnHome == original

@given(instance=mission::Drone_strategy)
def test_mission::drone_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=mission::Drone_strategy)
def test_mission::drone_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mission::Task_strategy)
@settings(max_examples=50)
def test_mission::task_instantiation(instance):
    assert isinstance(instance, mission::Task)

@given(instance=mission::TaskDependency_strategy)
@settings(max_examples=50)
def test_mission::taskdependency_instantiation(instance):
    assert isinstance(instance, mission::TaskDependency)

@given(instance=mission::Mission_strategy)
@settings(max_examples=50)
def test_mission::mission_instantiation(instance):
    assert isinstance(instance, mission::Mission)

@given(instance=mission::Mission_strategy)
def test_mission::mission_crs_type(instance):
    assert isinstance(instance.crs, str)


@given(instance=mission::Mission_strategy)
def test_mission::mission_crs_setter(instance):
    original = instance.crs
    instance.crs = original
    assert instance.crs == original

@given(instance=mission::NamedElement_strategy)
@settings(max_examples=50)
def test_mission::namedelement_instantiation(instance):
    assert isinstance(instance, mission::NamedElement)

@given(instance=mission::NamedElement_strategy)
def test_mission::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mission::NamedElement_strategy)
def test_mission::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
