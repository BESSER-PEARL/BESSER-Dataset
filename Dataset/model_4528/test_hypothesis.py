import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    platoon::Vehicle,
    Vehicle,
    Turn,
    platoon::Right,
    platoon::Left,
    Action,
    platoon::Forward,
    platoon::Turn,
    platoon::Action,
    platoon::FV,
    platoon::LV,
    platoon::Constraints,
    platoon::Route,
    platoon::Platoon,
    platoon::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_vehicle_is_not_abstract():
    assert not inspect.isabstract(Vehicle)


def test_vehicle_constructor_exists():
    assert callable(Vehicle.__init__)


def test_vehicle_constructor_args():
    sig = inspect.signature(Vehicle.__init__)
    params = list(sig.parameters.keys())



def test_turn_is_not_abstract():
    assert not inspect.isabstract(Turn)


def test_turn_constructor_exists():
    assert callable(Turn.__init__)


def test_turn_constructor_args():
    sig = inspect.signature(Turn.__init__)
    params = list(sig.parameters.keys())



def test_platoon::right_is_not_abstract():
    assert not inspect.isabstract(platoon::Right)


def test_platoon::right_constructor_exists():
    assert callable(platoon::Right.__init__)


def test_platoon::right_constructor_args():
    sig = inspect.signature(platoon::Right.__init__)
    params = list(sig.parameters.keys())



def test_platoon::left_is_not_abstract():
    assert not inspect.isabstract(platoon::Left)


def test_platoon::left_constructor_exists():
    assert callable(platoon::Left.__init__)


def test_platoon::left_constructor_args():
    sig = inspect.signature(platoon::Left.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
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



def test_platoon::turn_is_not_abstract():
    assert not inspect.isabstract(platoon::Turn)


def test_platoon::turn_constructor_exists():
    assert callable(platoon::Turn.__init__)


def test_platoon::turn_constructor_args():
    sig = inspect.signature(platoon::Turn.__init__)
    params = list(sig.parameters.keys())



def test_platoon::action_is_not_abstract():
    assert not inspect.isabstract(platoon::Action)


def test_platoon::action_constructor_exists():
    assert callable(platoon::Action.__init__)


def test_platoon::action_constructor_args():
    sig = inspect.signature(platoon::Action.__init__)
    params = list(sig.parameters.keys())



def test_platoon::fv_is_not_abstract():
    assert not inspect.isabstract(platoon::FV)


def test_platoon::fv_constructor_exists():
    assert callable(platoon::FV.__init__)


def test_platoon::fv_constructor_args():
    sig = inspect.signature(platoon::FV.__init__)
    params = list(sig.parameters.keys())



def test_platoon::lv_is_not_abstract():
    assert not inspect.isabstract(platoon::LV)


def test_platoon::lv_constructor_exists():
    assert callable(platoon::LV.__init__)


def test_platoon::lv_constructor_args():
    sig = inspect.signature(platoon::LV.__init__)
    params = list(sig.parameters.keys())



def test_platoon::constraints_is_not_abstract():
    assert not inspect.isabstract(platoon::Constraints)


def test_platoon::constraints_constructor_exists():
    assert callable(platoon::Constraints.__init__)


def test_platoon::constraints_constructor_args():
    sig = inspect.signature(platoon::Constraints.__init__)
    params = list(sig.parameters.keys())
    assert "minHeadway" in params, "Missing parameter 'minHeadway'"
    assert "maxHeadway" in params, "Missing parameter 'maxHeadway'"

def test_platoon::constraints_has_minHeadway():
    assert hasattr(platoon::Constraints, "minHeadway")
    descriptor = None
    for klass in platoon::Constraints.__mro__:
        if "minHeadway" in klass.__dict__:
            descriptor = klass.__dict__["minHeadway"]
            break
    assert isinstance(descriptor, property)

def test_platoon::constraints_has_maxHeadway():
    assert hasattr(platoon::Constraints, "maxHeadway")
    descriptor = None
    for klass in platoon::Constraints.__mro__:
        if "maxHeadway" in klass.__dict__:
            descriptor = klass.__dict__["maxHeadway"]
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



def test_platoon::model_is_not_abstract():
    assert not inspect.isabstract(platoon::Model)


def test_platoon::model_constructor_exists():
    assert callable(platoon::Model.__init__)


def test_platoon::model_constructor_args():
    sig = inspect.signature(platoon::Model.__init__)
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
platoon::Vehicle_strategy = st.builds(
    platoon::Vehicle,
    name=
        safe_text
)
Vehicle_strategy = st.builds(
    Vehicle,
)
Turn_strategy = st.builds(
    Turn,
)
platoon::Right_strategy = st.builds(
    platoon::Right,
)
platoon::Left_strategy = st.builds(
    platoon::Left,
)
Action_strategy = st.builds(
    Action,
)
platoon::Forward_strategy = st.builds(
    platoon::Forward,
    distance=
        st.integers()
)
platoon::Turn_strategy = st.builds(
    platoon::Turn,
)
platoon::Action_strategy = st.builds(
    platoon::Action,
)
platoon::FV_strategy = st.builds(
    platoon::FV,
)
platoon::LV_strategy = st.builds(
    platoon::LV,
)
platoon::Constraints_strategy = st.builds(
    platoon::Constraints,
    minHeadway=
        st.integers(),
    maxHeadway=
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
platoon::Model_strategy = st.builds(
    platoon::Model,
)

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

@given(instance=Vehicle_strategy)
@settings(max_examples=50)
def test_vehicle_instantiation(instance):
    assert isinstance(instance, Vehicle)

@given(instance=Turn_strategy)
@settings(max_examples=50)
def test_turn_instantiation(instance):
    assert isinstance(instance, Turn)

@given(instance=platoon::Right_strategy)
@settings(max_examples=50)
def test_platoon::right_instantiation(instance):
    assert isinstance(instance, platoon::Right)

@given(instance=platoon::Left_strategy)
@settings(max_examples=50)
def test_platoon::left_instantiation(instance):
    assert isinstance(instance, platoon::Left)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

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

@given(instance=platoon::Turn_strategy)
@settings(max_examples=50)
def test_platoon::turn_instantiation(instance):
    assert isinstance(instance, platoon::Turn)

@given(instance=platoon::Action_strategy)
@settings(max_examples=50)
def test_platoon::action_instantiation(instance):
    assert isinstance(instance, platoon::Action)

@given(instance=platoon::FV_strategy)
@settings(max_examples=50)
def test_platoon::fv_instantiation(instance):
    assert isinstance(instance, platoon::FV)

@given(instance=platoon::LV_strategy)
@settings(max_examples=50)
def test_platoon::lv_instantiation(instance):
    assert isinstance(instance, platoon::LV)

@given(instance=platoon::Constraints_strategy)
@settings(max_examples=50)
def test_platoon::constraints_instantiation(instance):
    assert isinstance(instance, platoon::Constraints)

@given(instance=platoon::Constraints_strategy)
def test_platoon::constraints_minHeadway_type(instance):
    assert isinstance(instance.minHeadway, int)


@given(instance=platoon::Constraints_strategy)
def test_platoon::constraints_minHeadway_setter(instance):
    original = instance.minHeadway
    instance.minHeadway = original
    assert instance.minHeadway == original

@given(instance=platoon::Constraints_strategy)
def test_platoon::constraints_maxHeadway_type(instance):
    assert isinstance(instance.maxHeadway, int)


@given(instance=platoon::Constraints_strategy)
def test_platoon::constraints_maxHeadway_setter(instance):
    original = instance.maxHeadway
    instance.maxHeadway = original
    assert instance.maxHeadway == original

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

@given(instance=platoon::Model_strategy)
@settings(max_examples=50)
def test_platoon::model_instantiation(instance):
    assert isinstance(instance, platoon::Model)
