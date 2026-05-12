import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dSL_Angle,
    dSL_Distance,
    dSL_Condition,
    dSL_ActionList,
    dSL_Action,
    dSL_Rule,
    dSL_Specification,
    dSL_ConditionList,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsl_angle_is_not_abstract():
    assert not inspect.isabstract(dSL_Angle)


def test_dsl_angle_constructor_exists():
    assert callable(dSL_Angle.__init__)


def test_dsl_angle_constructor_args():
    sig = inspect.signature(dSL_Angle.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "away" in params, "Missing parameter 'away'"

def test_dsl_angle_has_value():
    assert hasattr(dSL_Angle, "value")
    descriptor = None
    for klass in dSL_Angle.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_dsl_angle_has_away():
    assert hasattr(dSL_Angle, "away")
    descriptor = None
    for klass in dSL_Angle.__mro__:
        if "away" in klass.__dict__:
            descriptor = klass.__dict__["away"]
            break
    assert isinstance(descriptor, property)



def test_dsl_distance_is_not_abstract():
    assert not inspect.isabstract(dSL_Distance)


def test_dsl_distance_constructor_exists():
    assert callable(dSL_Distance.__init__)


def test_dsl_distance_constructor_args():
    sig = inspect.signature(dSL_Distance.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dsl_distance_has_value():
    assert hasattr(dSL_Distance, "value")
    descriptor = None
    for klass in dSL_Distance.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dsl_condition_is_not_abstract():
    assert not inspect.isabstract(dSL_Condition)


def test_dsl_condition_constructor_exists():
    assert callable(dSL_Condition.__init__)


def test_dsl_condition_constructor_args():
    sig = inspect.signature(dSL_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "isProbed" in params, "Missing parameter 'isProbed'"
    assert "atLake" in params, "Missing parameter 'atLake'"
    assert "allLakes" in params, "Missing parameter 'allLakes'"
    assert "collision" in params, "Missing parameter 'collision'"

def test_dsl_condition_has_not_():
    assert hasattr(dSL_Condition, "not_")
    descriptor = None
    for klass in dSL_Condition.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)

def test_dsl_condition_has_isProbed():
    assert hasattr(dSL_Condition, "isProbed")
    descriptor = None
    for klass in dSL_Condition.__mro__:
        if "isProbed" in klass.__dict__:
            descriptor = klass.__dict__["isProbed"]
            break
    assert isinstance(descriptor, property)

def test_dsl_condition_has_atLake():
    assert hasattr(dSL_Condition, "atLake")
    descriptor = None
    for klass in dSL_Condition.__mro__:
        if "atLake" in klass.__dict__:
            descriptor = klass.__dict__["atLake"]
            break
    assert isinstance(descriptor, property)

def test_dsl_condition_has_allLakes():
    assert hasattr(dSL_Condition, "allLakes")
    descriptor = None
    for klass in dSL_Condition.__mro__:
        if "allLakes" in klass.__dict__:
            descriptor = klass.__dict__["allLakes"]
            break
    assert isinstance(descriptor, property)

def test_dsl_condition_has_collision():
    assert hasattr(dSL_Condition, "collision")
    descriptor = None
    for klass in dSL_Condition.__mro__:
        if "collision" in klass.__dict__:
            descriptor = klass.__dict__["collision"]
            break
    assert isinstance(descriptor, property)



def test_dsl_actionlist_is_not_abstract():
    assert not inspect.isabstract(dSL_ActionList)


def test_dsl_actionlist_constructor_exists():
    assert callable(dSL_ActionList.__init__)


def test_dsl_actionlist_constructor_args():
    sig = inspect.signature(dSL_ActionList.__init__)
    params = list(sig.parameters.keys())



def test_dsl_action_is_not_abstract():
    assert not inspect.isabstract(dSL_Action)


def test_dsl_action_constructor_exists():
    assert callable(dSL_Action.__init__)


def test_dsl_action_constructor_args():
    sig = inspect.signature(dSL_Action.__init__)
    params = list(sig.parameters.keys())
    assert "driveDistance" in params, "Missing parameter 'driveDistance'"
    assert "showLakes" in params, "Missing parameter 'showLakes'"
    assert "driveDirection" in params, "Missing parameter 'driveDirection'"
    assert "steer" in params, "Missing parameter 'steer'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "blinkLights" in params, "Missing parameter 'blinkLights'"
    assert "probeLake" in params, "Missing parameter 'probeLake'"

def test_dsl_action_has_driveDistance():
    assert hasattr(dSL_Action, "driveDistance")
    descriptor = None
    for klass in dSL_Action.__mro__:
        if "driveDistance" in klass.__dict__:
            descriptor = klass.__dict__["driveDistance"]
            break
    assert isinstance(descriptor, property)

def test_dsl_action_has_showLakes():
    assert hasattr(dSL_Action, "showLakes")
    descriptor = None
    for klass in dSL_Action.__mro__:
        if "showLakes" in klass.__dict__:
            descriptor = klass.__dict__["showLakes"]
            break
    assert isinstance(descriptor, property)

def test_dsl_action_has_driveDirection():
    assert hasattr(dSL_Action, "driveDirection")
    descriptor = None
    for klass in dSL_Action.__mro__:
        if "driveDirection" in klass.__dict__:
            descriptor = klass.__dict__["driveDirection"]
            break
    assert isinstance(descriptor, property)

def test_dsl_action_has_steer():
    assert hasattr(dSL_Action, "steer")
    descriptor = None
    for klass in dSL_Action.__mro__:
        if "steer" in klass.__dict__:
            descriptor = klass.__dict__["steer"]
            break
    assert isinstance(descriptor, property)

def test_dsl_action_has_direction():
    assert hasattr(dSL_Action, "direction")
    descriptor = None
    for klass in dSL_Action.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_dsl_action_has_blinkLights():
    assert hasattr(dSL_Action, "blinkLights")
    descriptor = None
    for klass in dSL_Action.__mro__:
        if "blinkLights" in klass.__dict__:
            descriptor = klass.__dict__["blinkLights"]
            break
    assert isinstance(descriptor, property)

def test_dsl_action_has_probeLake():
    assert hasattr(dSL_Action, "probeLake")
    descriptor = None
    for klass in dSL_Action.__mro__:
        if "probeLake" in klass.__dict__:
            descriptor = klass.__dict__["probeLake"]
            break
    assert isinstance(descriptor, property)



def test_dsl_rule_is_not_abstract():
    assert not inspect.isabstract(dSL_Rule)


def test_dsl_rule_constructor_exists():
    assert callable(dSL_Rule.__init__)


def test_dsl_rule_constructor_args():
    sig = inspect.signature(dSL_Rule.__init__)
    params = list(sig.parameters.keys())



def test_dsl_specification_is_not_abstract():
    assert not inspect.isabstract(dSL_Specification)


def test_dsl_specification_constructor_exists():
    assert callable(dSL_Specification.__init__)


def test_dsl_specification_constructor_args():
    sig = inspect.signature(dSL_Specification.__init__)
    params = list(sig.parameters.keys())



def test_dsl_conditionlist_is_not_abstract():
    assert not inspect.isabstract(dSL_ConditionList)


def test_dsl_conditionlist_constructor_exists():
    assert callable(dSL_ConditionList.__init__)


def test_dsl_conditionlist_constructor_args():
    sig = inspect.signature(dSL_ConditionList.__init__)
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
dSL_Angle_strategy = st.builds(
    dSL_Angle,
    value=
        st.integers(),
    away=
        st.booleans()
)
dSL_Distance_strategy = st.builds(
    dSL_Distance,
    value=
        st.integers()
)
dSL_Condition_strategy = st.builds(
    dSL_Condition,
    not_=
        st.booleans(),
    isProbed=
        st.booleans(),
    atLake=
        st.booleans(),
    allLakes=
        st.booleans(),
    collision=
        st.booleans()
)
dSL_ActionList_strategy = st.builds(
    dSL_ActionList,
)
dSL_Action_strategy = st.builds(
    dSL_Action,
    driveDistance=
        st.booleans(),
    showLakes=
        st.booleans(),
    driveDirection=
        st.booleans(),
    steer=
        st.booleans(),
    direction=
        safe_text,
    blinkLights=
        st.booleans(),
    probeLake=
        st.booleans()
)
dSL_Rule_strategy = st.builds(
    dSL_Rule,
)
dSL_Specification_strategy = st.builds(
    dSL_Specification,
)
dSL_ConditionList_strategy = st.builds(
    dSL_ConditionList,
)

@given(instance=dSL_Angle_strategy)
@settings(max_examples=50)
def test_dsl_angle_instantiation(instance):
    assert isinstance(instance, dSL_Angle)



@given(instance=dSL_Angle_strategy)
def test_dsl_angle_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=dSL_Angle_strategy)
def test_dsl_angle_away_setter(instance):
    original = instance.away
    instance.away = original
    assert instance.away == original

@given(instance=dSL_Distance_strategy)
@settings(max_examples=50)
def test_dsl_distance_instantiation(instance):
    assert isinstance(instance, dSL_Distance)



@given(instance=dSL_Distance_strategy)
def test_dsl_distance_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dSL_Condition_strategy)
@settings(max_examples=50)
def test_dsl_condition_instantiation(instance):
    assert isinstance(instance, dSL_Condition)



@given(instance=dSL_Condition_strategy)
def test_dsl_condition_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original



@given(instance=dSL_Condition_strategy)
def test_dsl_condition_isProbed_setter(instance):
    original = instance.isProbed
    instance.isProbed = original
    assert instance.isProbed == original



@given(instance=dSL_Condition_strategy)
def test_dsl_condition_atLake_setter(instance):
    original = instance.atLake
    instance.atLake = original
    assert instance.atLake == original



@given(instance=dSL_Condition_strategy)
def test_dsl_condition_allLakes_setter(instance):
    original = instance.allLakes
    instance.allLakes = original
    assert instance.allLakes == original



@given(instance=dSL_Condition_strategy)
def test_dsl_condition_collision_setter(instance):
    original = instance.collision
    instance.collision = original
    assert instance.collision == original

@given(instance=dSL_ActionList_strategy)
@settings(max_examples=50)
def test_dsl_actionlist_instantiation(instance):
    assert isinstance(instance, dSL_ActionList)

@given(instance=dSL_Action_strategy)
@settings(max_examples=50)
def test_dsl_action_instantiation(instance):
    assert isinstance(instance, dSL_Action)



@given(instance=dSL_Action_strategy)
def test_dsl_action_driveDistance_setter(instance):
    original = instance.driveDistance
    instance.driveDistance = original
    assert instance.driveDistance == original



@given(instance=dSL_Action_strategy)
def test_dsl_action_showLakes_setter(instance):
    original = instance.showLakes
    instance.showLakes = original
    assert instance.showLakes == original



@given(instance=dSL_Action_strategy)
def test_dsl_action_driveDirection_setter(instance):
    original = instance.driveDirection
    instance.driveDirection = original
    assert instance.driveDirection == original



@given(instance=dSL_Action_strategy)
def test_dsl_action_steer_setter(instance):
    original = instance.steer
    instance.steer = original
    assert instance.steer == original



@given(instance=dSL_Action_strategy)
def test_dsl_action_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=dSL_Action_strategy)
def test_dsl_action_blinkLights_setter(instance):
    original = instance.blinkLights
    instance.blinkLights = original
    assert instance.blinkLights == original



@given(instance=dSL_Action_strategy)
def test_dsl_action_probeLake_setter(instance):
    original = instance.probeLake
    instance.probeLake = original
    assert instance.probeLake == original

@given(instance=dSL_Rule_strategy)
@settings(max_examples=50)
def test_dsl_rule_instantiation(instance):
    assert isinstance(instance, dSL_Rule)

@given(instance=dSL_Specification_strategy)
@settings(max_examples=50)
def test_dsl_specification_instantiation(instance):
    assert isinstance(instance, dSL_Specification)

@given(instance=dSL_ConditionList_strategy)
@settings(max_examples=50)
def test_dsl_conditionlist_instantiation(instance):
    assert isinstance(instance, dSL_ConditionList)
