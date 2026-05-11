import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Step,
    platoon::Turn,
    platoon::Forward,
    platoon::Step,
    Vehicle,
    platoon::Vehicle,
    Constraint,
    platoon::headway,
    platoon::Constraint,
    Turn,
    platoon::TurnRight,
    platoon::TurnLeft,
    platoon::Constraints,
    platoon::Route,
    platoon::Platoon,
    platoon::World,
    platoon::FollowVehicle,
    platoon::LeadVehicle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_step_is_not_abstract():
    assert not inspect.isabstract(Step)


def test_step_constructor_exists():
    assert callable(Step.__init__)


def test_step_constructor_args():
    sig = inspect.signature(Step.__init__)
    params = list(sig.parameters.keys())



def test_platoon::turn_is_not_abstract():
    assert not inspect.isabstract(platoon::Turn)


def test_platoon::turn_constructor_exists():
    assert callable(platoon::Turn.__init__)


def test_platoon::turn_constructor_args():
    sig = inspect.signature(platoon::Turn.__init__)
    params = list(sig.parameters.keys())



def test_platoon::forward_is_not_abstract():
    assert not inspect.isabstract(platoon::Forward)


def test_platoon::forward_constructor_exists():
    assert callable(platoon::Forward.__init__)


def test_platoon::forward_constructor_args():
    sig = inspect.signature(platoon::Forward.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_platoon::forward_has_distance():
    assert hasattr(platoon::Forward, "distance")
    descriptor = None
    for klass in platoon::Forward.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_platoon::step_is_not_abstract():
    assert not inspect.isabstract(platoon::Step)


def test_platoon::step_constructor_exists():
    assert callable(platoon::Step.__init__)


def test_platoon::step_constructor_args():
    sig = inspect.signature(platoon::Step.__init__)
    params = list(sig.parameters.keys())



def test_vehicle_is_not_abstract():
    assert not inspect.isabstract(Vehicle)


def test_vehicle_constructor_exists():
    assert callable(Vehicle.__init__)


def test_vehicle_constructor_args():
    sig = inspect.signature(Vehicle.__init__)
    params = list(sig.parameters.keys())



def test_platoon::vehicle_is_not_abstract():
    assert not inspect.isabstract(platoon::Vehicle)


def test_platoon::vehicle_constructor_exists():
    assert callable(platoon::Vehicle.__init__)


def test_platoon::vehicle_constructor_args():
    sig = inspect.signature(platoon::Vehicle.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_platoon::vehicle_has_name():
    assert hasattr(platoon::Vehicle, "name")
    descriptor = None
    for klass in platoon::Vehicle.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_platoon::headway_is_not_abstract():
    assert not inspect.isabstract(platoon::headway)


def test_platoon::headway_constructor_exists():
    assert callable(platoon::headway.__init__)


def test_platoon::headway_constructor_args():
    sig = inspect.signature(platoon::headway.__init__)
    params = list(sig.parameters.keys())
    assert "lowbound" in params, "Missing parameter 'lowbound'"
    assert "upbound" in params, "Missing parameter 'upbound'"

def test_platoon::headway_has_lowbound():
    assert hasattr(platoon::headway, "lowbound")
    descriptor = None
    for klass in platoon::headway.__mro__:
        if "lowbound" in klass.__dict__:
            descriptor = klass.__dict__["lowbound"]
            break
    assert isinstance(descriptor, property)

def test_platoon::headway_has_upbound():
    assert hasattr(platoon::headway, "upbound")
    descriptor = None
    for klass in platoon::headway.__mro__:
        if "upbound" in klass.__dict__:
            descriptor = klass.__dict__["upbound"]
            break
    assert isinstance(descriptor, property)



def test_platoon::constraint_is_not_abstract():
    assert not inspect.isabstract(platoon::Constraint)


def test_platoon::constraint_constructor_exists():
    assert callable(platoon::Constraint.__init__)


def test_platoon::constraint_constructor_args():
    sig = inspect.signature(platoon::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_turn_is_not_abstract():
    assert not inspect.isabstract(Turn)


def test_turn_constructor_exists():
    assert callable(Turn.__init__)


def test_turn_constructor_args():
    sig = inspect.signature(Turn.__init__)
    params = list(sig.parameters.keys())



def test_platoon::turnright_is_not_abstract():
    assert not inspect.isabstract(platoon::TurnRight)


def test_platoon::turnright_constructor_exists():
    assert callable(platoon::TurnRight.__init__)


def test_platoon::turnright_constructor_args():
    sig = inspect.signature(platoon::TurnRight.__init__)
    params = list(sig.parameters.keys())



def test_platoon::turnleft_is_not_abstract():
    assert not inspect.isabstract(platoon::TurnLeft)


def test_platoon::turnleft_constructor_exists():
    assert callable(platoon::TurnLeft.__init__)


def test_platoon::turnleft_constructor_args():
    sig = inspect.signature(platoon::TurnLeft.__init__)
    params = list(sig.parameters.keys())



def test_platoon::constraints_is_not_abstract():
    assert not inspect.isabstract(platoon::Constraints)


def test_platoon::constraints_constructor_exists():
    assert callable(platoon::Constraints.__init__)


def test_platoon::constraints_constructor_args():
    sig = inspect.signature(platoon::Constraints.__init__)
    params = list(sig.parameters.keys())



def test_platoon::route_is_not_abstract():
    assert not inspect.isabstract(platoon::Route)


def test_platoon::route_constructor_exists():
    assert callable(platoon::Route.__init__)


def test_platoon::route_constructor_args():
    sig = inspect.signature(platoon::Route.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_platoon::route_has_name():
    assert hasattr(platoon::Route, "name")
    descriptor = None
    for klass in platoon::Route.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_platoon::platoon_is_not_abstract():
    assert not inspect.isabstract(platoon::Platoon)


def test_platoon::platoon_constructor_exists():
    assert callable(platoon::Platoon.__init__)


def test_platoon::platoon_constructor_args():
    sig = inspect.signature(platoon::Platoon.__init__)
    params = list(sig.parameters.keys())



def test_platoon::world_is_not_abstract():
    assert not inspect.isabstract(platoon::World)


def test_platoon::world_constructor_exists():
    assert callable(platoon::World.__init__)


def test_platoon::world_constructor_args():
    sig = inspect.signature(platoon::World.__init__)
    params = list(sig.parameters.keys())



def test_platoon::followvehicle_is_not_abstract():
    assert not inspect.isabstract(platoon::FollowVehicle)


def test_platoon::followvehicle_constructor_exists():
    assert callable(platoon::FollowVehicle.__init__)


def test_platoon::followvehicle_constructor_args():
    sig = inspect.signature(platoon::FollowVehicle.__init__)
    params = list(sig.parameters.keys())



def test_platoon::leadvehicle_is_not_abstract():
    assert not inspect.isabstract(platoon::LeadVehicle)


def test_platoon::leadvehicle_constructor_exists():
    assert callable(platoon::LeadVehicle.__init__)


def test_platoon::leadvehicle_constructor_args():
    sig = inspect.signature(platoon::LeadVehicle.__init__)
    params = list(sig.parameters.keys())


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
Step_strategy = st.builds(
    Step,
)
platoon::Turn_strategy = st.builds(
    platoon::Turn,
)
platoon::Forward_strategy = st.builds(
    platoon::Forward,
    distance=
        st.integers()
)
platoon::Step_strategy = st.builds(
    platoon::Step,
)
Vehicle_strategy = st.builds(
    Vehicle,
)
platoon::Vehicle_strategy = st.builds(
    platoon::Vehicle,
    name=
        safe_text
)
Constraint_strategy = st.builds(
    Constraint,
)
platoon::headway_strategy = st.builds(
    platoon::headway,
    lowbound=
        st.integers(),
    upbound=
        st.integers()
)
platoon::Constraint_strategy = st.builds(
    platoon::Constraint,
)
Turn_strategy = st.builds(
    Turn,
)
platoon::TurnRight_strategy = st.builds(
    platoon::TurnRight,
)
platoon::TurnLeft_strategy = st.builds(
    platoon::TurnLeft,
)
platoon::Constraints_strategy = st.builds(
    platoon::Constraints,
)
platoon::Route_strategy = st.builds(
    platoon::Route,
    name=
        safe_text
)
platoon::Platoon_strategy = st.builds(
    platoon::Platoon,
)
platoon::World_strategy = st.builds(
    platoon::World,
)
platoon::FollowVehicle_strategy = st.builds(
    platoon::FollowVehicle,
)
platoon::LeadVehicle_strategy = st.builds(
    platoon::LeadVehicle,
)

@given(instance=Step_strategy)
@settings(max_examples=50)
def test_step_instantiation(instance):
    assert isinstance(instance, Step)

@given(instance=platoon::Turn_strategy)
@settings(max_examples=50)
def test_platoon::turn_instantiation(instance):
    assert isinstance(instance, platoon::Turn)

@given(instance=platoon::Forward_strategy)
@settings(max_examples=50)
def test_platoon::forward_instantiation(instance):
    assert isinstance(instance, platoon::Forward)

@given(instance=platoon::Forward_strategy)
def test_platoon::forward_distance_type(instance):
    assert isinstance(instance.distance, int)


@given(instance=platoon::Forward_strategy)
def test_platoon::forward_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=platoon::Step_strategy)
@settings(max_examples=50)
def test_platoon::step_instantiation(instance):
    assert isinstance(instance, platoon::Step)

@given(instance=Vehicle_strategy)
@settings(max_examples=50)
def test_vehicle_instantiation(instance):
    assert isinstance(instance, Vehicle)

@given(instance=platoon::Vehicle_strategy)
@settings(max_examples=50)
def test_platoon::vehicle_instantiation(instance):
    assert isinstance(instance, platoon::Vehicle)

@given(instance=platoon::Vehicle_strategy)
def test_platoon::vehicle_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=platoon::Vehicle_strategy)
def test_platoon::vehicle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=platoon::headway_strategy)
@settings(max_examples=50)
def test_platoon::headway_instantiation(instance):
    assert isinstance(instance, platoon::headway)

@given(instance=platoon::headway_strategy)
def test_platoon::headway_lowbound_type(instance):
    assert isinstance(instance.lowbound, int)


@given(instance=platoon::headway_strategy)
def test_platoon::headway_lowbound_setter(instance):
    original = instance.lowbound
    instance.lowbound = original
    assert instance.lowbound == original

@given(instance=platoon::headway_strategy)
def test_platoon::headway_upbound_type(instance):
    assert isinstance(instance.upbound, int)


@given(instance=platoon::headway_strategy)
def test_platoon::headway_upbound_setter(instance):
    original = instance.upbound
    instance.upbound = original
    assert instance.upbound == original

@given(instance=platoon::Constraint_strategy)
@settings(max_examples=50)
def test_platoon::constraint_instantiation(instance):
    assert isinstance(instance, platoon::Constraint)

@given(instance=Turn_strategy)
@settings(max_examples=50)
def test_turn_instantiation(instance):
    assert isinstance(instance, Turn)

@given(instance=platoon::TurnRight_strategy)
@settings(max_examples=50)
def test_platoon::turnright_instantiation(instance):
    assert isinstance(instance, platoon::TurnRight)

@given(instance=platoon::TurnLeft_strategy)
@settings(max_examples=50)
def test_platoon::turnleft_instantiation(instance):
    assert isinstance(instance, platoon::TurnLeft)

@given(instance=platoon::Constraints_strategy)
@settings(max_examples=50)
def test_platoon::constraints_instantiation(instance):
    assert isinstance(instance, platoon::Constraints)

@given(instance=platoon::Route_strategy)
@settings(max_examples=50)
def test_platoon::route_instantiation(instance):
    assert isinstance(instance, platoon::Route)

@given(instance=platoon::Route_strategy)
def test_platoon::route_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=platoon::Route_strategy)
def test_platoon::route_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=platoon::Platoon_strategy)
@settings(max_examples=50)
def test_platoon::platoon_instantiation(instance):
    assert isinstance(instance, platoon::Platoon)

@given(instance=platoon::World_strategy)
@settings(max_examples=50)
def test_platoon::world_instantiation(instance):
    assert isinstance(instance, platoon::World)

@given(instance=platoon::FollowVehicle_strategy)
@settings(max_examples=50)
def test_platoon::followvehicle_instantiation(instance):
    assert isinstance(instance, platoon::FollowVehicle)

@given(instance=platoon::LeadVehicle_strategy)
@settings(max_examples=50)
def test_platoon::leadvehicle_instantiation(instance):
    assert isinstance(instance, platoon::LeadVehicle)
