import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    roverDSL::DetectBottle,
    roverDSL::Colors,
    roverDSL::Mission,
    roverDSL::Robot,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_roverdsl::detectbottle_is_not_abstract():
    assert not inspect.isabstract(roverDSL::DetectBottle)


def test_roverdsl::detectbottle_constructor_exists():
    assert callable(roverDSL::DetectBottle.__init__)


def test_roverdsl::detectbottle_constructor_args():
    sig = inspect.signature(roverDSL::DetectBottle.__init__)
    params = list(sig.parameters.keys())
    assert "maxDistance" in params, "Missing parameter 'maxDistance'"

def test_roverdsl::detectbottle_has_maxDistance():
    assert hasattr(roverDSL::DetectBottle, "maxDistance")
    descriptor = None
    for klass in roverDSL::DetectBottle.__mro__:
        if "maxDistance" in klass.__dict__:
            descriptor = klass.__dict__["maxDistance"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::colors_is_not_abstract():
    assert not inspect.isabstract(roverDSL::Colors)


def test_roverdsl::colors_constructor_exists():
    assert callable(roverDSL::Colors.__init__)


def test_roverdsl::colors_constructor_args():
    sig = inspect.signature(roverDSL::Colors.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_roverdsl::colors_has_color():
    assert hasattr(roverDSL::Colors, "color")
    descriptor = None
    for klass in roverDSL::Colors.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::mission_is_not_abstract():
    assert not inspect.isabstract(roverDSL::Mission)


def test_roverdsl::mission_constructor_exists():
    assert callable(roverDSL::Mission.__init__)


def test_roverdsl::mission_constructor_args():
    sig = inspect.signature(roverDSL::Mission.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_roverdsl::mission_has_id():
    assert hasattr(roverDSL::Mission, "id")
    descriptor = None
    for klass in roverDSL::Mission.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::robot_is_not_abstract():
    assert not inspect.isabstract(roverDSL::Robot)


def test_roverdsl::robot_constructor_exists():
    assert callable(roverDSL::Robot.__init__)


def test_roverdsl::robot_constructor_args():
    sig = inspect.signature(roverDSL::Robot.__init__)
    params = list(sig.parameters.keys())
    assert "defaultSpeed" in params, "Missing parameter 'defaultSpeed'"
    assert "slowSpeed" in params, "Missing parameter 'slowSpeed'"
    assert "minAngle" in params, "Missing parameter 'minAngle'"
    assert "maxAngle" in params, "Missing parameter 'maxAngle'"

def test_roverdsl::robot_has_defaultSpeed():
    assert hasattr(roverDSL::Robot, "defaultSpeed")
    descriptor = None
    for klass in roverDSL::Robot.__mro__:
        if "defaultSpeed" in klass.__dict__:
            descriptor = klass.__dict__["defaultSpeed"]
            break
    assert isinstance(descriptor, property)

def test_roverdsl::robot_has_slowSpeed():
    assert hasattr(roverDSL::Robot, "slowSpeed")
    descriptor = None
    for klass in roverDSL::Robot.__mro__:
        if "slowSpeed" in klass.__dict__:
            descriptor = klass.__dict__["slowSpeed"]
            break
    assert isinstance(descriptor, property)

def test_roverdsl::robot_has_minAngle():
    assert hasattr(roverDSL::Robot, "minAngle")
    descriptor = None
    for klass in roverDSL::Robot.__mro__:
        if "minAngle" in klass.__dict__:
            descriptor = klass.__dict__["minAngle"]
            break
    assert isinstance(descriptor, property)

def test_roverdsl::robot_has_maxAngle():
    assert hasattr(roverDSL::Robot, "maxAngle")
    descriptor = None
    for klass in roverDSL::Robot.__mro__:
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
roverDSL::DetectBottle_strategy = st.builds(
    roverDSL::DetectBottle,
    maxDistance=
        st.integers()
)
roverDSL::Colors_strategy = st.builds(
    roverDSL::Colors,
    color=
        safe_text
)
roverDSL::Mission_strategy = st.builds(
    roverDSL::Mission,
    id=
        safe_text
)
roverDSL::Robot_strategy = st.builds(
    roverDSL::Robot,
    defaultSpeed=
        st.integers(),
    slowSpeed=
        st.integers(),
    minAngle=
        st.integers(),
    maxAngle=
        st.integers()
)

@given(instance=roverDSL::DetectBottle_strategy)
@settings(max_examples=50)
def test_roverdsl::detectbottle_instantiation(instance):
    assert isinstance(instance, roverDSL::DetectBottle)

@given(instance=roverDSL::DetectBottle_strategy)
def test_roverdsl::detectbottle_maxDistance_type(instance):
    assert isinstance(instance.maxDistance, int)


@given(instance=roverDSL::DetectBottle_strategy)
def test_roverdsl::detectbottle_maxDistance_setter(instance):
    original = instance.maxDistance
    instance.maxDistance = original
    assert instance.maxDistance == original

@given(instance=roverDSL::Colors_strategy)
@settings(max_examples=50)
def test_roverdsl::colors_instantiation(instance):
    assert isinstance(instance, roverDSL::Colors)

@given(instance=roverDSL::Colors_strategy)
def test_roverdsl::colors_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=roverDSL::Colors_strategy)
def test_roverdsl::colors_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=roverDSL::Mission_strategy)
@settings(max_examples=50)
def test_roverdsl::mission_instantiation(instance):
    assert isinstance(instance, roverDSL::Mission)

@given(instance=roverDSL::Mission_strategy)
def test_roverdsl::mission_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=roverDSL::Mission_strategy)
def test_roverdsl::mission_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=roverDSL::Robot_strategy)
@settings(max_examples=50)
def test_roverdsl::robot_instantiation(instance):
    assert isinstance(instance, roverDSL::Robot)

@given(instance=roverDSL::Robot_strategy)
def test_roverdsl::robot_defaultSpeed_type(instance):
    assert isinstance(instance.defaultSpeed, int)


@given(instance=roverDSL::Robot_strategy)
def test_roverdsl::robot_defaultSpeed_setter(instance):
    original = instance.defaultSpeed
    instance.defaultSpeed = original
    assert instance.defaultSpeed == original

@given(instance=roverDSL::Robot_strategy)
def test_roverdsl::robot_slowSpeed_type(instance):
    assert isinstance(instance.slowSpeed, int)


@given(instance=roverDSL::Robot_strategy)
def test_roverdsl::robot_slowSpeed_setter(instance):
    original = instance.slowSpeed
    instance.slowSpeed = original
    assert instance.slowSpeed == original

@given(instance=roverDSL::Robot_strategy)
def test_roverdsl::robot_minAngle_type(instance):
    assert isinstance(instance.minAngle, int)


@given(instance=roverDSL::Robot_strategy)
def test_roverdsl::robot_minAngle_setter(instance):
    original = instance.minAngle
    instance.minAngle = original
    assert instance.minAngle == original

@given(instance=roverDSL::Robot_strategy)
def test_roverdsl::robot_maxAngle_type(instance):
    assert isinstance(instance.maxAngle, int)


@given(instance=roverDSL::Robot_strategy)
def test_roverdsl::robot_maxAngle_setter(instance):
    original = instance.maxAngle
    instance.maxAngle = original
    assert instance.maxAngle == original
