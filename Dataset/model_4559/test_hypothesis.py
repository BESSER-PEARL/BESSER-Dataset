import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    platoon::World,
    platoon::Constraint,
    Constraint,
    platoon::HeadwayConstraint,
    Command,
    platoon::TurnCommand,
    platoon::ForwardCommand,
    platoon::Constraints,
    platoon::Command,
    platoon::Route,
    platoon::Platoon,
    Vehicle,
    platoon::LeadingVehicle,
    platoon::FollowVehicle,
    platoon::Vehicle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_platoon::world_is_not_abstract():
    assert not inspect.isabstract(platoon::World)


def test_platoon::world_constructor_exists():
    assert callable(platoon::World.__init__)


def test_platoon::world_constructor_args():
    sig = inspect.signature(platoon::World.__init__)
    params = list(sig.parameters.keys())



def test_platoon::constraint_is_not_abstract():
    assert not inspect.isabstract(platoon::Constraint)


def test_platoon::constraint_constructor_exists():
    assert callable(platoon::Constraint.__init__)


def test_platoon::constraint_constructor_args():
    sig = inspect.signature(platoon::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_platoon::headwayconstraint_is_not_abstract():
    assert not inspect.isabstract(platoon::HeadwayConstraint)


def test_platoon::headwayconstraint_constructor_exists():
    assert callable(platoon::HeadwayConstraint.__init__)


def test_platoon::headwayconstraint_constructor_args():
    sig = inspect.signature(platoon::HeadwayConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_platoon::headwayconstraint_has_max():
    assert hasattr(platoon::HeadwayConstraint, "max")
    descriptor = None
    for klass in platoon::HeadwayConstraint.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_platoon::headwayconstraint_has_min():
    assert hasattr(platoon::HeadwayConstraint, "min")
    descriptor = None
    for klass in platoon::HeadwayConstraint.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_command_constructor_exists():
    assert callable(Command.__init__)


def test_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_platoon::turncommand_is_not_abstract():
    assert not inspect.isabstract(platoon::TurnCommand)


def test_platoon::turncommand_constructor_exists():
    assert callable(platoon::TurnCommand.__init__)


def test_platoon::turncommand_constructor_args():
    sig = inspect.signature(platoon::TurnCommand.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_platoon::turncommand_has_direction():
    assert hasattr(platoon::TurnCommand, "direction")
    descriptor = None
    for klass in platoon::TurnCommand.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_platoon::forwardcommand_is_not_abstract():
    assert not inspect.isabstract(platoon::ForwardCommand)


def test_platoon::forwardcommand_constructor_exists():
    assert callable(platoon::ForwardCommand.__init__)


def test_platoon::forwardcommand_constructor_args():
    sig = inspect.signature(platoon::ForwardCommand.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_platoon::forwardcommand_has_distance():
    assert hasattr(platoon::ForwardCommand, "distance")
    descriptor = None
    for klass in platoon::ForwardCommand.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_platoon::constraints_is_not_abstract():
    assert not inspect.isabstract(platoon::Constraints)


def test_platoon::constraints_constructor_exists():
    assert callable(platoon::Constraints.__init__)


def test_platoon::constraints_constructor_args():
    sig = inspect.signature(platoon::Constraints.__init__)
    params = list(sig.parameters.keys())



def test_platoon::command_is_not_abstract():
    assert not inspect.isabstract(platoon::Command)


def test_platoon::command_constructor_exists():
    assert callable(platoon::Command.__init__)


def test_platoon::command_constructor_args():
    sig = inspect.signature(platoon::Command.__init__)
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



def test_vehicle_is_not_abstract():
    assert not inspect.isabstract(Vehicle)


def test_vehicle_constructor_exists():
    assert callable(Vehicle.__init__)


def test_vehicle_constructor_args():
    sig = inspect.signature(Vehicle.__init__)
    params = list(sig.parameters.keys())



def test_platoon::leadingvehicle_is_not_abstract():
    assert not inspect.isabstract(platoon::LeadingVehicle)


def test_platoon::leadingvehicle_constructor_exists():
    assert callable(platoon::LeadingVehicle.__init__)


def test_platoon::leadingvehicle_constructor_args():
    sig = inspect.signature(platoon::LeadingVehicle.__init__)
    params = list(sig.parameters.keys())



def test_platoon::followvehicle_is_not_abstract():
    assert not inspect.isabstract(platoon::FollowVehicle)


def test_platoon::followvehicle_constructor_exists():
    assert callable(platoon::FollowVehicle.__init__)


def test_platoon::followvehicle_constructor_args():
    sig = inspect.signature(platoon::FollowVehicle.__init__)
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
platoon::World_strategy = st.builds(
    platoon::World,
)
platoon::Constraint_strategy = st.builds(
    platoon::Constraint,
)
Constraint_strategy = st.builds(
    Constraint,
)
platoon::HeadwayConstraint_strategy = st.builds(
    platoon::HeadwayConstraint,
    max=
        st.integers(),
    min=
        st.integers()
)
Command_strategy = st.builds(
    Command,
)
platoon::TurnCommand_strategy = st.builds(
    platoon::TurnCommand,
    direction=
        safe_text
)
platoon::ForwardCommand_strategy = st.builds(
    platoon::ForwardCommand,
    distance=
        st.integers()
)
platoon::Constraints_strategy = st.builds(
    platoon::Constraints,
)
platoon::Command_strategy = st.builds(
    platoon::Command,
)
platoon::Route_strategy = st.builds(
    platoon::Route,
    name=
        safe_text
)
platoon::Platoon_strategy = st.builds(
    platoon::Platoon,
)
Vehicle_strategy = st.builds(
    Vehicle,
)
platoon::LeadingVehicle_strategy = st.builds(
    platoon::LeadingVehicle,
)
platoon::FollowVehicle_strategy = st.builds(
    platoon::FollowVehicle,
)
platoon::Vehicle_strategy = st.builds(
    platoon::Vehicle,
    name=
        safe_text
)

@given(instance=platoon::World_strategy)
@settings(max_examples=50)
def test_platoon::world_instantiation(instance):
    assert isinstance(instance, platoon::World)

@given(instance=platoon::Constraint_strategy)
@settings(max_examples=50)
def test_platoon::constraint_instantiation(instance):
    assert isinstance(instance, platoon::Constraint)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=platoon::HeadwayConstraint_strategy)
@settings(max_examples=50)
def test_platoon::headwayconstraint_instantiation(instance):
    assert isinstance(instance, platoon::HeadwayConstraint)

@given(instance=platoon::HeadwayConstraint_strategy)
def test_platoon::headwayconstraint_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=platoon::HeadwayConstraint_strategy)
def test_platoon::headwayconstraint_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=platoon::HeadwayConstraint_strategy)
def test_platoon::headwayconstraint_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=platoon::HeadwayConstraint_strategy)
def test_platoon::headwayconstraint_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=platoon::TurnCommand_strategy)
@settings(max_examples=50)
def test_platoon::turncommand_instantiation(instance):
    assert isinstance(instance, platoon::TurnCommand)

@given(instance=platoon::TurnCommand_strategy)
def test_platoon::turncommand_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=platoon::TurnCommand_strategy)
def test_platoon::turncommand_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=platoon::ForwardCommand_strategy)
@settings(max_examples=50)
def test_platoon::forwardcommand_instantiation(instance):
    assert isinstance(instance, platoon::ForwardCommand)

@given(instance=platoon::ForwardCommand_strategy)
def test_platoon::forwardcommand_distance_type(instance):
    assert isinstance(instance.distance, int)


@given(instance=platoon::ForwardCommand_strategy)
def test_platoon::forwardcommand_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=platoon::Constraints_strategy)
@settings(max_examples=50)
def test_platoon::constraints_instantiation(instance):
    assert isinstance(instance, platoon::Constraints)

@given(instance=platoon::Command_strategy)
@settings(max_examples=50)
def test_platoon::command_instantiation(instance):
    assert isinstance(instance, platoon::Command)

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

@given(instance=Vehicle_strategy)
@settings(max_examples=50)
def test_vehicle_instantiation(instance):
    assert isinstance(instance, Vehicle)

@given(instance=platoon::LeadingVehicle_strategy)
@settings(max_examples=50)
def test_platoon::leadingvehicle_instantiation(instance):
    assert isinstance(instance, platoon::LeadingVehicle)

@given(instance=platoon::FollowVehicle_strategy)
@settings(max_examples=50)
def test_platoon::followvehicle_instantiation(instance):
    assert isinstance(instance, platoon::FollowVehicle)

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
