import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    roverDSL_DetectBottle,
    roverDSL_Colors,
    roverDSL_Mission,
    roverDSL_Robot,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_roverdsl_detectbottle_is_not_abstract():
    assert not inspect.isabstract(roverDSL_DetectBottle)


def test_roverdsl_detectbottle_constructor_exists():
    assert callable(roverDSL_DetectBottle.__init__)


def test_roverdsl_detectbottle_constructor_args():
    sig = inspect.signature(roverDSL_DetectBottle.__init__)
    params = list(sig.parameters.keys())
    assert "maxDistance" in params, "Missing parameter 'maxDistance'"

def test_roverdsl_detectbottle_has_maxDistance():
    assert hasattr(roverDSL_DetectBottle, "maxDistance")
    descriptor = None
    for klass in roverDSL_DetectBottle.__mro__:
        if "maxDistance" in klass.__dict__:
            descriptor = klass.__dict__["maxDistance"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_colors_is_not_abstract():
    assert not inspect.isabstract(roverDSL_Colors)


def test_roverdsl_colors_constructor_exists():
    assert callable(roverDSL_Colors.__init__)


def test_roverdsl_colors_constructor_args():
    sig = inspect.signature(roverDSL_Colors.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_roverdsl_colors_has_color():
    assert hasattr(roverDSL_Colors, "color")
    descriptor = None
    for klass in roverDSL_Colors.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_mission_is_not_abstract():
    assert not inspect.isabstract(roverDSL_Mission)


def test_roverdsl_mission_constructor_exists():
    assert callable(roverDSL_Mission.__init__)


def test_roverdsl_mission_constructor_args():
    sig = inspect.signature(roverDSL_Mission.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_roverdsl_mission_has_id():
    assert hasattr(roverDSL_Mission, "id")
    descriptor = None
    for klass in roverDSL_Mission.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_robot_is_not_abstract():
    assert not inspect.isabstract(roverDSL_Robot)


def test_roverdsl_robot_constructor_exists():
    assert callable(roverDSL_Robot.__init__)


def test_roverdsl_robot_constructor_args():
    sig = inspect.signature(roverDSL_Robot.__init__)
    params = list(sig.parameters.keys())
    assert "defaultSpeed" in params, "Missing parameter 'defaultSpeed'"
    assert "minAngle" in params, "Missing parameter 'minAngle'"
    assert "slowSpeed" in params, "Missing parameter 'slowSpeed'"
    assert "maxAngle" in params, "Missing parameter 'maxAngle'"

def test_roverdsl_robot_has_defaultSpeed():
    assert hasattr(roverDSL_Robot, "defaultSpeed")
    descriptor = None
    for klass in roverDSL_Robot.__mro__:
        if "defaultSpeed" in klass.__dict__:
            descriptor = klass.__dict__["defaultSpeed"]
            break
    assert isinstance(descriptor, property)

def test_roverdsl_robot_has_minAngle():
    assert hasattr(roverDSL_Robot, "minAngle")
    descriptor = None
    for klass in roverDSL_Robot.__mro__:
        if "minAngle" in klass.__dict__:
            descriptor = klass.__dict__["minAngle"]
            break
    assert isinstance(descriptor, property)

def test_roverdsl_robot_has_slowSpeed():
    assert hasattr(roverDSL_Robot, "slowSpeed")
    descriptor = None
    for klass in roverDSL_Robot.__mro__:
        if "slowSpeed" in klass.__dict__:
            descriptor = klass.__dict__["slowSpeed"]
            break
    assert isinstance(descriptor, property)

def test_roverdsl_robot_has_maxAngle():
    assert hasattr(roverDSL_Robot, "maxAngle")
    descriptor = None
    for klass in roverDSL_Robot.__mro__:
        if "maxAngle" in klass.__dict__:
            descriptor = klass.__dict__["maxAngle"]
            break
    assert isinstance(descriptor, property)

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "blue",
        "yellow",
        "red",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"


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
roverDSL_DetectBottle_strategy = st.builds(
    roverDSL_DetectBottle,
    maxDistance=
        st.integers()
)
roverDSL_Colors_strategy = st.builds(
    roverDSL_Colors,
    color=
        safe_text
)
roverDSL_Mission_strategy = st.builds(
    roverDSL_Mission,
    id=
        safe_text
)
roverDSL_Robot_strategy = st.builds(
    roverDSL_Robot,
    defaultSpeed=
        st.integers(),
    minAngle=
        st.integers(),
    slowSpeed=
        st.integers(),
    maxAngle=
        st.integers()
)

@given(instance=roverDSL_DetectBottle_strategy)
@settings(max_examples=50)
def test_roverdsl_detectbottle_instantiation(instance):
    assert isinstance(instance, roverDSL_DetectBottle)



@given(instance=roverDSL_DetectBottle_strategy)
def test_roverdsl_detectbottle_maxDistance_setter(instance):
    original = instance.maxDistance
    instance.maxDistance = original
    assert instance.maxDistance == original

@given(instance=roverDSL_Colors_strategy)
@settings(max_examples=50)
def test_roverdsl_colors_instantiation(instance):
    assert isinstance(instance, roverDSL_Colors)



@given(instance=roverDSL_Colors_strategy)
def test_roverdsl_colors_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=roverDSL_Mission_strategy)
@settings(max_examples=50)
def test_roverdsl_mission_instantiation(instance):
    assert isinstance(instance, roverDSL_Mission)



@given(instance=roverDSL_Mission_strategy)
def test_roverdsl_mission_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=roverDSL_Robot_strategy)
@settings(max_examples=50)
def test_roverdsl_robot_instantiation(instance):
    assert isinstance(instance, roverDSL_Robot)



@given(instance=roverDSL_Robot_strategy)
def test_roverdsl_robot_defaultSpeed_setter(instance):
    original = instance.defaultSpeed
    instance.defaultSpeed = original
    assert instance.defaultSpeed == original



@given(instance=roverDSL_Robot_strategy)
def test_roverdsl_robot_minAngle_setter(instance):
    original = instance.minAngle
    instance.minAngle = original
    assert instance.minAngle == original



@given(instance=roverDSL_Robot_strategy)
def test_roverdsl_robot_slowSpeed_setter(instance):
    original = instance.slowSpeed
    instance.slowSpeed = original
    assert instance.slowSpeed == original



@given(instance=roverDSL_Robot_strategy)
def test_roverdsl_robot_maxAngle_setter(instance):
    original = instance.maxAngle
    instance.maxAngle = original
    assert instance.maxAngle == original
