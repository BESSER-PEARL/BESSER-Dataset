import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    routeCommand,
    Vehicle,
    platoon::Vehicle,
    platoon::TurnRight,
    platoon::Root,
    platoon::Forward,
    platoon::FollowingVehicle,
    platoon::LeaderVehicle,
    platoon::routeCommand,
    platoon::Constraints,
    platoon::Route,
    platoon::Platoon,
    platoon::TurnLeft,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_routecommand_is_not_abstract():
    assert not inspect.isabstract(routeCommand)


def test_routecommand_constructor_exists():
    assert callable(routeCommand.__init__)


def test_routecommand_constructor_args():
    sig = inspect.signature(routeCommand.__init__)
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



def test_platoon::turnright_is_not_abstract():
    assert not inspect.isabstract(platoon::TurnRight)


def test_platoon::turnright_constructor_exists():
    assert callable(platoon::TurnRight.__init__)


def test_platoon::turnright_constructor_args():
    sig = inspect.signature(platoon::TurnRight.__init__)
    params = list(sig.parameters.keys())



def test_platoon::root_is_not_abstract():
    assert not inspect.isabstract(platoon::Root)


def test_platoon::root_constructor_exists():
    assert callable(platoon::Root.__init__)


def test_platoon::root_constructor_args():
    sig = inspect.signature(platoon::Root.__init__)
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



def test_platoon::followingvehicle_is_not_abstract():
    assert not inspect.isabstract(platoon::FollowingVehicle)


def test_platoon::followingvehicle_constructor_exists():
    assert callable(platoon::FollowingVehicle.__init__)


def test_platoon::followingvehicle_constructor_args():
    sig = inspect.signature(platoon::FollowingVehicle.__init__)
    params = list(sig.parameters.keys())



def test_platoon::leadervehicle_is_not_abstract():
    assert not inspect.isabstract(platoon::LeaderVehicle)


def test_platoon::leadervehicle_constructor_exists():
    assert callable(platoon::LeaderVehicle.__init__)


def test_platoon::leadervehicle_constructor_args():
    sig = inspect.signature(platoon::LeaderVehicle.__init__)
    params = list(sig.parameters.keys())



def test_platoon::routecommand_is_not_abstract():
    assert not inspect.isabstract(platoon::routeCommand)


def test_platoon::routecommand_constructor_exists():
    assert callable(platoon::routeCommand.__init__)


def test_platoon::routecommand_constructor_args():
    sig = inspect.signature(platoon::routeCommand.__init__)
    params = list(sig.parameters.keys())



def test_platoon::constraints_is_not_abstract():
    assert not inspect.isabstract(platoon::Constraints)


def test_platoon::constraints_constructor_exists():
    assert callable(platoon::Constraints.__init__)


def test_platoon::constraints_constructor_args():
    sig = inspect.signature(platoon::Constraints.__init__)
    params = list(sig.parameters.keys())
    assert "lbound" in params, "Missing parameter 'lbound'"
    assert "ubound" in params, "Missing parameter 'ubound'"

def test_platoon::constraints_has_lbound():
    assert hasattr(platoon::Constraints, "lbound")
    descriptor = None
    for klass in platoon::Constraints.__mro__:
        if "lbound" in klass.__dict__:
            descriptor = klass.__dict__["lbound"]
            break
    assert isinstance(descriptor, property)

def test_platoon::constraints_has_ubound():
    assert hasattr(platoon::Constraints, "ubound")
    descriptor = None
    for klass in platoon::Constraints.__mro__:
        if "ubound" in klass.__dict__:
            descriptor = klass.__dict__["ubound"]
            break
    assert isinstance(descriptor, property)



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



def test_platoon::turnleft_is_not_abstract():
    assert not inspect.isabstract(platoon::TurnLeft)


def test_platoon::turnleft_constructor_exists():
    assert callable(platoon::TurnLeft.__init__)


def test_platoon::turnleft_constructor_args():
    sig = inspect.signature(platoon::TurnLeft.__init__)
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
routeCommand_strategy = st.builds(
    routeCommand,
)
Vehicle_strategy = st.builds(
    Vehicle,
)
platoon::Vehicle_strategy = st.builds(
    platoon::Vehicle,
    name=
        safe_text
)
platoon::TurnRight_strategy = st.builds(
    platoon::TurnRight,
)
platoon::Root_strategy = st.builds(
    platoon::Root,
)
platoon::Forward_strategy = st.builds(
    platoon::Forward,
    distance=
        st.integers()
)
platoon::FollowingVehicle_strategy = st.builds(
    platoon::FollowingVehicle,
)
platoon::LeaderVehicle_strategy = st.builds(
    platoon::LeaderVehicle,
)
platoon::routeCommand_strategy = st.builds(
    platoon::routeCommand,
)
platoon::Constraints_strategy = st.builds(
    platoon::Constraints,
    lbound=
        st.integers(),
    ubound=
        st.integers()
)
platoon::Route_strategy = st.builds(
    platoon::Route,
    name=
        safe_text
)
platoon::Platoon_strategy = st.builds(
    platoon::Platoon,
)
platoon::TurnLeft_strategy = st.builds(
    platoon::TurnLeft,
)

@given(instance=routeCommand_strategy)
@settings(max_examples=50)
def test_routecommand_instantiation(instance):
    assert isinstance(instance, routeCommand)

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

@given(instance=platoon::TurnRight_strategy)
@settings(max_examples=50)
def test_platoon::turnright_instantiation(instance):
    assert isinstance(instance, platoon::TurnRight)

@given(instance=platoon::Root_strategy)
@settings(max_examples=50)
def test_platoon::root_instantiation(instance):
    assert isinstance(instance, platoon::Root)

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

@given(instance=platoon::FollowingVehicle_strategy)
@settings(max_examples=50)
def test_platoon::followingvehicle_instantiation(instance):
    assert isinstance(instance, platoon::FollowingVehicle)

@given(instance=platoon::LeaderVehicle_strategy)
@settings(max_examples=50)
def test_platoon::leadervehicle_instantiation(instance):
    assert isinstance(instance, platoon::LeaderVehicle)

@given(instance=platoon::routeCommand_strategy)
@settings(max_examples=50)
def test_platoon::routecommand_instantiation(instance):
    assert isinstance(instance, platoon::routeCommand)

@given(instance=platoon::Constraints_strategy)
@settings(max_examples=50)
def test_platoon::constraints_instantiation(instance):
    assert isinstance(instance, platoon::Constraints)

@given(instance=platoon::Constraints_strategy)
def test_platoon::constraints_lbound_type(instance):
    assert isinstance(instance.lbound, int)


@given(instance=platoon::Constraints_strategy)
def test_platoon::constraints_lbound_setter(instance):
    original = instance.lbound
    instance.lbound = original
    assert instance.lbound == original

@given(instance=platoon::Constraints_strategy)
def test_platoon::constraints_ubound_type(instance):
    assert isinstance(instance.ubound, int)


@given(instance=platoon::Constraints_strategy)
def test_platoon::constraints_ubound_setter(instance):
    original = instance.ubound
    instance.ubound = original
    assert instance.ubound == original

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

@given(instance=platoon::TurnLeft_strategy)
@settings(max_examples=50)
def test_platoon::turnleft_instantiation(instance):
    assert isinstance(instance, platoon::TurnLeft)
