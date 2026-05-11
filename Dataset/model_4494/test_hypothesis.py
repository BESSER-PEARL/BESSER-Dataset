import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dSL::Angle,
    dSL::Distance,
    dSL::Condition,
    dSL::ActionList,
    dSL::Action,
    dSL::Rule,
    dSL::Specification,
    dSL::ConditionList,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsl::angle_is_not_abstract():
    assert not inspect.isabstract(dSL::Angle)


def test_dsl::angle_constructor_exists():
    assert callable(dSL::Angle.__init__)


def test_dsl::angle_constructor_args():
    sig = inspect.signature(dSL::Angle.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "away" in params, "Missing parameter 'away'"

def test_dsl::angle_has_value():
    assert hasattr(dSL::Angle, "value")
    descriptor = None
    for klass in dSL::Angle.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_dsl::angle_has_away():
    assert hasattr(dSL::Angle, "away")
    descriptor = None
    for klass in dSL::Angle.__mro__:
        if "away" in klass.__dict__:
            descriptor = klass.__dict__["away"]
            break
    assert isinstance(descriptor, property)



def test_dsl::distance_is_not_abstract():
    assert not inspect.isabstract(dSL::Distance)


def test_dsl::distance_constructor_exists():
    assert callable(dSL::Distance.__init__)


def test_dsl::distance_constructor_args():
    sig = inspect.signature(dSL::Distance.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dsl::distance_has_value():
    assert hasattr(dSL::Distance, "value")
    descriptor = None
    for klass in dSL::Distance.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dsl::condition_is_not_abstract():
    assert not inspect.isabstract(dSL::Condition)


def test_dsl::condition_constructor_exists():
    assert callable(dSL::Condition.__init__)


def test_dsl::condition_constructor_args():
    sig = inspect.signature(dSL::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "isProbed" in params, "Missing parameter 'isProbed'"
    assert "allLakes" in params, "Missing parameter 'allLakes'"
    assert "collision" in params, "Missing parameter 'collision'"
    assert "atLake" in params, "Missing parameter 'atLake'"
    assert "not_" in params, "Missing parameter 'not_'"

def test_dsl::condition_has_isProbed():
    assert hasattr(dSL::Condition, "isProbed")
    descriptor = None
    for klass in dSL::Condition.__mro__:
        if "isProbed" in klass.__dict__:
            descriptor = klass.__dict__["isProbed"]
            break
    assert isinstance(descriptor, property)

def test_dsl::condition_has_allLakes():
    assert hasattr(dSL::Condition, "allLakes")
    descriptor = None
    for klass in dSL::Condition.__mro__:
        if "allLakes" in klass.__dict__:
            descriptor = klass.__dict__["allLakes"]
            break
    assert isinstance(descriptor, property)

def test_dsl::condition_has_collision():
    assert hasattr(dSL::Condition, "collision")
    descriptor = None
    for klass in dSL::Condition.__mro__:
        if "collision" in klass.__dict__:
            descriptor = klass.__dict__["collision"]
            break
    assert isinstance(descriptor, property)

def test_dsl::condition_has_atLake():
    assert hasattr(dSL::Condition, "atLake")
    descriptor = None
    for klass in dSL::Condition.__mro__:
        if "atLake" in klass.__dict__:
            descriptor = klass.__dict__["atLake"]
            break
    assert isinstance(descriptor, property)

def test_dsl::condition_has_not_():
    assert hasattr(dSL::Condition, "not_")
    descriptor = None
    for klass in dSL::Condition.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_dsl::actionlist_is_not_abstract():
    assert not inspect.isabstract(dSL::ActionList)


def test_dsl::actionlist_constructor_exists():
    assert callable(dSL::ActionList.__init__)


def test_dsl::actionlist_constructor_args():
    sig = inspect.signature(dSL::ActionList.__init__)
    params = list(sig.parameters.keys())



def test_dsl::action_is_not_abstract():
    assert not inspect.isabstract(dSL::Action)


def test_dsl::action_constructor_exists():
    assert callable(dSL::Action.__init__)


def test_dsl::action_constructor_args():
    sig = inspect.signature(dSL::Action.__init__)
    params = list(sig.parameters.keys())
    assert "probeLake" in params, "Missing parameter 'probeLake'"
    assert "driveDistance" in params, "Missing parameter 'driveDistance'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "showLakes" in params, "Missing parameter 'showLakes'"
    assert "blinkLights" in params, "Missing parameter 'blinkLights'"
    assert "driveDirection" in params, "Missing parameter 'driveDirection'"
    assert "steer" in params, "Missing parameter 'steer'"

def test_dsl::action_has_probeLake():
    assert hasattr(dSL::Action, "probeLake")
    descriptor = None
    for klass in dSL::Action.__mro__:
        if "probeLake" in klass.__dict__:
            descriptor = klass.__dict__["probeLake"]
            break
    assert isinstance(descriptor, property)

def test_dsl::action_has_driveDistance():
    assert hasattr(dSL::Action, "driveDistance")
    descriptor = None
    for klass in dSL::Action.__mro__:
        if "driveDistance" in klass.__dict__:
            descriptor = klass.__dict__["driveDistance"]
            break
    assert isinstance(descriptor, property)

def test_dsl::action_has_direction():
    assert hasattr(dSL::Action, "direction")
    descriptor = None
    for klass in dSL::Action.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_dsl::action_has_showLakes():
    assert hasattr(dSL::Action, "showLakes")
    descriptor = None
    for klass in dSL::Action.__mro__:
        if "showLakes" in klass.__dict__:
            descriptor = klass.__dict__["showLakes"]
            break
    assert isinstance(descriptor, property)

def test_dsl::action_has_blinkLights():
    assert hasattr(dSL::Action, "blinkLights")
    descriptor = None
    for klass in dSL::Action.__mro__:
        if "blinkLights" in klass.__dict__:
            descriptor = klass.__dict__["blinkLights"]
            break
    assert isinstance(descriptor, property)

def test_dsl::action_has_driveDirection():
    assert hasattr(dSL::Action, "driveDirection")
    descriptor = None
    for klass in dSL::Action.__mro__:
        if "driveDirection" in klass.__dict__:
            descriptor = klass.__dict__["driveDirection"]
            break
    assert isinstance(descriptor, property)

def test_dsl::action_has_steer():
    assert hasattr(dSL::Action, "steer")
    descriptor = None
    for klass in dSL::Action.__mro__:
        if "steer" in klass.__dict__:
            descriptor = klass.__dict__["steer"]
            break
    assert isinstance(descriptor, property)



def test_dsl::rule_is_not_abstract():
    assert not inspect.isabstract(dSL::Rule)


def test_dsl::rule_constructor_exists():
    assert callable(dSL::Rule.__init__)


def test_dsl::rule_constructor_args():
    sig = inspect.signature(dSL::Rule.__init__)
    params = list(sig.parameters.keys())



def test_dsl::specification_is_not_abstract():
    assert not inspect.isabstract(dSL::Specification)


def test_dsl::specification_constructor_exists():
    assert callable(dSL::Specification.__init__)


def test_dsl::specification_constructor_args():
    sig = inspect.signature(dSL::Specification.__init__)
    params = list(sig.parameters.keys())



def test_dsl::conditionlist_is_not_abstract():
    assert not inspect.isabstract(dSL::ConditionList)


def test_dsl::conditionlist_constructor_exists():
    assert callable(dSL::ConditionList.__init__)


def test_dsl::conditionlist_constructor_args():
    sig = inspect.signature(dSL::ConditionList.__init__)
    params = list(sig.parameters.keys())

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "BACKWARD",
        "FORWARD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"


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
dSL::Angle_strategy = st.builds(
    dSL::Angle,
    value=
        st.integers(),
    away=
        st.booleans()
)
dSL::Distance_strategy = st.builds(
    dSL::Distance,
    value=
        st.integers()
)
dSL::Condition_strategy = st.builds(
    dSL::Condition,
    isProbed=
        st.booleans(),
    allLakes=
        st.booleans(),
    collision=
        st.booleans(),
    atLake=
        st.booleans(),
    not_=
        st.booleans()
)
dSL::ActionList_strategy = st.builds(
    dSL::ActionList,
)
dSL::Action_strategy = st.builds(
    dSL::Action,
    probeLake=
        st.booleans(),
    driveDistance=
        st.booleans(),
    direction=
        safe_text,
    showLakes=
        st.booleans(),
    blinkLights=
        st.booleans(),
    driveDirection=
        st.booleans(),
    steer=
        st.booleans()
)
dSL::Rule_strategy = st.builds(
    dSL::Rule,
)
dSL::Specification_strategy = st.builds(
    dSL::Specification,
)
dSL::ConditionList_strategy = st.builds(
    dSL::ConditionList,
)

@given(instance=dSL::Angle_strategy)
@settings(max_examples=50)
def test_dsl::angle_instantiation(instance):
    assert isinstance(instance, dSL::Angle)

@given(instance=dSL::Angle_strategy)
def test_dsl::angle_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=dSL::Angle_strategy)
def test_dsl::angle_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dSL::Angle_strategy)
def test_dsl::angle_away_type(instance):
    assert isinstance(instance.away, bool)


@given(instance=dSL::Angle_strategy)
def test_dsl::angle_away_setter(instance):
    original = instance.away
    instance.away = original
    assert instance.away == original

@given(instance=dSL::Distance_strategy)
@settings(max_examples=50)
def test_dsl::distance_instantiation(instance):
    assert isinstance(instance, dSL::Distance)

@given(instance=dSL::Distance_strategy)
def test_dsl::distance_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=dSL::Distance_strategy)
def test_dsl::distance_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dSL::Condition_strategy)
@settings(max_examples=50)
def test_dsl::condition_instantiation(instance):
    assert isinstance(instance, dSL::Condition)

@given(instance=dSL::Condition_strategy)
def test_dsl::condition_isProbed_type(instance):
    assert isinstance(instance.isProbed, bool)


@given(instance=dSL::Condition_strategy)
def test_dsl::condition_isProbed_setter(instance):
    original = instance.isProbed
    instance.isProbed = original
    assert instance.isProbed == original

@given(instance=dSL::Condition_strategy)
def test_dsl::condition_allLakes_type(instance):
    assert isinstance(instance.allLakes, bool)


@given(instance=dSL::Condition_strategy)
def test_dsl::condition_allLakes_setter(instance):
    original = instance.allLakes
    instance.allLakes = original
    assert instance.allLakes == original

@given(instance=dSL::Condition_strategy)
def test_dsl::condition_collision_type(instance):
    assert isinstance(instance.collision, bool)


@given(instance=dSL::Condition_strategy)
def test_dsl::condition_collision_setter(instance):
    original = instance.collision
    instance.collision = original
    assert instance.collision == original

@given(instance=dSL::Condition_strategy)
def test_dsl::condition_atLake_type(instance):
    assert isinstance(instance.atLake, bool)


@given(instance=dSL::Condition_strategy)
def test_dsl::condition_atLake_setter(instance):
    original = instance.atLake
    instance.atLake = original
    assert instance.atLake == original

@given(instance=dSL::Condition_strategy)
def test_dsl::condition_not__type(instance):
    assert isinstance(instance.not_, bool)


@given(instance=dSL::Condition_strategy)
def test_dsl::condition_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=dSL::ActionList_strategy)
@settings(max_examples=50)
def test_dsl::actionlist_instantiation(instance):
    assert isinstance(instance, dSL::ActionList)

@given(instance=dSL::Action_strategy)
@settings(max_examples=50)
def test_dsl::action_instantiation(instance):
    assert isinstance(instance, dSL::Action)

@given(instance=dSL::Action_strategy)
def test_dsl::action_probeLake_type(instance):
    assert isinstance(instance.probeLake, bool)


@given(instance=dSL::Action_strategy)
def test_dsl::action_probeLake_setter(instance):
    original = instance.probeLake
    instance.probeLake = original
    assert instance.probeLake == original

@given(instance=dSL::Action_strategy)
def test_dsl::action_driveDistance_type(instance):
    assert isinstance(instance.driveDistance, bool)


@given(instance=dSL::Action_strategy)
def test_dsl::action_driveDistance_setter(instance):
    original = instance.driveDistance
    instance.driveDistance = original
    assert instance.driveDistance == original

@given(instance=dSL::Action_strategy)
def test_dsl::action_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=dSL::Action_strategy)
def test_dsl::action_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=dSL::Action_strategy)
def test_dsl::action_showLakes_type(instance):
    assert isinstance(instance.showLakes, bool)


@given(instance=dSL::Action_strategy)
def test_dsl::action_showLakes_setter(instance):
    original = instance.showLakes
    instance.showLakes = original
    assert instance.showLakes == original

@given(instance=dSL::Action_strategy)
def test_dsl::action_blinkLights_type(instance):
    assert isinstance(instance.blinkLights, bool)


@given(instance=dSL::Action_strategy)
def test_dsl::action_blinkLights_setter(instance):
    original = instance.blinkLights
    instance.blinkLights = original
    assert instance.blinkLights == original

@given(instance=dSL::Action_strategy)
def test_dsl::action_driveDirection_type(instance):
    assert isinstance(instance.driveDirection, bool)


@given(instance=dSL::Action_strategy)
def test_dsl::action_driveDirection_setter(instance):
    original = instance.driveDirection
    instance.driveDirection = original
    assert instance.driveDirection == original

@given(instance=dSL::Action_strategy)
def test_dsl::action_steer_type(instance):
    assert isinstance(instance.steer, bool)


@given(instance=dSL::Action_strategy)
def test_dsl::action_steer_setter(instance):
    original = instance.steer
    instance.steer = original
    assert instance.steer == original

@given(instance=dSL::Rule_strategy)
@settings(max_examples=50)
def test_dsl::rule_instantiation(instance):
    assert isinstance(instance, dSL::Rule)

@given(instance=dSL::Specification_strategy)
@settings(max_examples=50)
def test_dsl::specification_instantiation(instance):
    assert isinstance(instance, dSL::Specification)

@given(instance=dSL::ConditionList_strategy)
@settings(max_examples=50)
def test_dsl::conditionlist_instantiation(instance):
    assert isinstance(instance, dSL::ConditionList)
