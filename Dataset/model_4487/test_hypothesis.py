import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Command,
    model::Repeat,
    model::Light,
    model::Rotate,
    model::Wait,
    model::Move,
    NamedElement,
    model::Transition,
    model::Ozobot,
    model::Command,
    model::Block,
    model::OzobotProgram,
    model::NamedElement,
    Velocity,
    Color,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_command_constructor_exists():
    assert callable(Command.__init__)


def test_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_model::repeat_is_not_abstract():
    assert not inspect.isabstract(model::Repeat)


def test_model::repeat_constructor_exists():
    assert callable(model::Repeat.__init__)


def test_model::repeat_constructor_args():
    sig = inspect.signature(model::Repeat.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_model::repeat_has_count():
    assert hasattr(model::Repeat, "count")
    descriptor = None
    for klass in model::Repeat.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_model::light_is_not_abstract():
    assert not inspect.isabstract(model::Light)


def test_model::light_constructor_exists():
    assert callable(model::Light.__init__)


def test_model::light_constructor_args():
    sig = inspect.signature(model::Light.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_model::light_has_color():
    assert hasattr(model::Light, "color")
    descriptor = None
    for klass in model::Light.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_model::rotate_is_not_abstract():
    assert not inspect.isabstract(model::Rotate)


def test_model::rotate_constructor_exists():
    assert callable(model::Rotate.__init__)


def test_model::rotate_constructor_args():
    sig = inspect.signature(model::Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "velocity" in params, "Missing parameter 'velocity'"
    assert "angle" in params, "Missing parameter 'angle'"

def test_model::rotate_has_direction():
    assert hasattr(model::Rotate, "direction")
    descriptor = None
    for klass in model::Rotate.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_model::rotate_has_velocity():
    assert hasattr(model::Rotate, "velocity")
    descriptor = None
    for klass in model::Rotate.__mro__:
        if "velocity" in klass.__dict__:
            descriptor = klass.__dict__["velocity"]
            break
    assert isinstance(descriptor, property)

def test_model::rotate_has_angle():
    assert hasattr(model::Rotate, "angle")
    descriptor = None
    for klass in model::Rotate.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_model::wait_is_not_abstract():
    assert not inspect.isabstract(model::Wait)


def test_model::wait_constructor_exists():
    assert callable(model::Wait.__init__)


def test_model::wait_constructor_args():
    sig = inspect.signature(model::Wait.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_model::wait_has_time():
    assert hasattr(model::Wait, "time")
    descriptor = None
    for klass in model::Wait.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_model::move_is_not_abstract():
    assert not inspect.isabstract(model::Move)


def test_model::move_constructor_exists():
    assert callable(model::Move.__init__)


def test_model::move_constructor_args():
    sig = inspect.signature(model::Move.__init__)
    params = list(sig.parameters.keys())
    assert "velocity" in params, "Missing parameter 'velocity'"
    assert "distance" in params, "Missing parameter 'distance'"

def test_model::move_has_velocity():
    assert hasattr(model::Move, "velocity")
    descriptor = None
    for klass in model::Move.__mro__:
        if "velocity" in klass.__dict__:
            descriptor = klass.__dict__["velocity"]
            break
    assert isinstance(descriptor, property)

def test_model::move_has_distance():
    assert hasattr(model::Move, "distance")
    descriptor = None
    for klass in model::Move.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_model::transition_is_not_abstract():
    assert not inspect.isabstract(model::Transition)


def test_model::transition_constructor_exists():
    assert callable(model::Transition.__init__)


def test_model::transition_constructor_args():
    sig = inspect.signature(model::Transition.__init__)
    params = list(sig.parameters.keys())



def test_model::ozobot_is_not_abstract():
    assert not inspect.isabstract(model::Ozobot)


def test_model::ozobot_constructor_exists():
    assert callable(model::Ozobot.__init__)


def test_model::ozobot_constructor_args():
    sig = inspect.signature(model::Ozobot.__init__)
    params = list(sig.parameters.keys())



def test_model::command_is_not_abstract():
    assert not inspect.isabstract(model::Command)


def test_model::command_constructor_exists():
    assert callable(model::Command.__init__)


def test_model::command_constructor_args():
    sig = inspect.signature(model::Command.__init__)
    params = list(sig.parameters.keys())



def test_model::block_is_not_abstract():
    assert not inspect.isabstract(model::Block)


def test_model::block_constructor_exists():
    assert callable(model::Block.__init__)


def test_model::block_constructor_args():
    sig = inspect.signature(model::Block.__init__)
    params = list(sig.parameters.keys())



def test_model::ozobotprogram_is_not_abstract():
    assert not inspect.isabstract(model::OzobotProgram)


def test_model::ozobotprogram_constructor_exists():
    assert callable(model::OzobotProgram.__init__)


def test_model::ozobotprogram_constructor_args():
    sig = inspect.signature(model::OzobotProgram.__init__)
    params = list(sig.parameters.keys())



def test_model::namedelement_is_not_abstract():
    assert not inspect.isabstract(model::NamedElement)


def test_model::namedelement_constructor_exists():
    assert callable(model::NamedElement.__init__)


def test_model::namedelement_constructor_args():
    sig = inspect.signature(model::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::namedelement_has_name():
    assert hasattr(model::NamedElement, "name")
    descriptor = None
    for klass in model::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_velocity_exists():
    # Check that the Enumeration exists
    assert Velocity is not None

def test_velocity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Velocity]
    expected_literals = [
        "very_slow",
        "fast",
        "very_fast",
        "slow",
        "medium",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Velocity"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "red",
        "none",
        "green",
        "yellow",
        "blue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "right",
        "left",
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
Command_strategy = st.builds(
    Command,
)
model::Repeat_strategy = st.builds(
    model::Repeat,
    count=
        st.integers()
)
model::Light_strategy = st.builds(
    model::Light,
    color=
        safe_text
)
model::Rotate_strategy = st.builds(
    model::Rotate,
    direction=
        safe_text,
    velocity=
        safe_text,
    angle=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model::Wait_strategy = st.builds(
    model::Wait,
    time=
        st.integers()
)
model::Move_strategy = st.builds(
    model::Move,
    velocity=
        safe_text,
    distance=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
model::Transition_strategy = st.builds(
    model::Transition,
)
model::Ozobot_strategy = st.builds(
    model::Ozobot,
)
model::Command_strategy = st.builds(
    model::Command,
)
model::Block_strategy = st.builds(
    model::Block,
)
model::OzobotProgram_strategy = st.builds(
    model::OzobotProgram,
)
model::NamedElement_strategy = st.builds(
    model::NamedElement,
    name=
        safe_text
)

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=model::Repeat_strategy)
@settings(max_examples=50)
def test_model::repeat_instantiation(instance):
    assert isinstance(instance, model::Repeat)

@given(instance=model::Repeat_strategy)
def test_model::repeat_count_type(instance):
    assert isinstance(instance.count, int)


@given(instance=model::Repeat_strategy)
def test_model::repeat_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=model::Light_strategy)
@settings(max_examples=50)
def test_model::light_instantiation(instance):
    assert isinstance(instance, model::Light)

@given(instance=model::Light_strategy)
def test_model::light_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=model::Light_strategy)
def test_model::light_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=model::Rotate_strategy)
@settings(max_examples=50)
def test_model::rotate_instantiation(instance):
    assert isinstance(instance, model::Rotate)

@given(instance=model::Rotate_strategy)
def test_model::rotate_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=model::Rotate_strategy)
def test_model::rotate_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=model::Rotate_strategy)
def test_model::rotate_velocity_type(instance):
    assert isinstance(instance.velocity, str)


@given(instance=model::Rotate_strategy)
def test_model::rotate_velocity_setter(instance):
    original = instance.velocity
    instance.velocity = original
    assert instance.velocity == original

@given(instance=model::Rotate_strategy)
def test_model::rotate_angle_type(instance):
    assert isinstance(instance.angle, float)


@given(instance=model::Rotate_strategy)
def test_model::rotate_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=model::Wait_strategy)
@settings(max_examples=50)
def test_model::wait_instantiation(instance):
    assert isinstance(instance, model::Wait)

@given(instance=model::Wait_strategy)
def test_model::wait_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=model::Wait_strategy)
def test_model::wait_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=model::Move_strategy)
@settings(max_examples=50)
def test_model::move_instantiation(instance):
    assert isinstance(instance, model::Move)

@given(instance=model::Move_strategy)
def test_model::move_velocity_type(instance):
    assert isinstance(instance.velocity, str)


@given(instance=model::Move_strategy)
def test_model::move_velocity_setter(instance):
    original = instance.velocity
    instance.velocity = original
    assert instance.velocity == original

@given(instance=model::Move_strategy)
def test_model::move_distance_type(instance):
    assert isinstance(instance.distance, int)


@given(instance=model::Move_strategy)
def test_model::move_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=model::Transition_strategy)
@settings(max_examples=50)
def test_model::transition_instantiation(instance):
    assert isinstance(instance, model::Transition)

@given(instance=model::Ozobot_strategy)
@settings(max_examples=50)
def test_model::ozobot_instantiation(instance):
    assert isinstance(instance, model::Ozobot)

@given(instance=model::Command_strategy)
@settings(max_examples=50)
def test_model::command_instantiation(instance):
    assert isinstance(instance, model::Command)

@given(instance=model::Block_strategy)
@settings(max_examples=50)
def test_model::block_instantiation(instance):
    assert isinstance(instance, model::Block)

@given(instance=model::OzobotProgram_strategy)
@settings(max_examples=50)
def test_model::ozobotprogram_instantiation(instance):
    assert isinstance(instance, model::OzobotProgram)

@given(instance=model::NamedElement_strategy)
@settings(max_examples=50)
def test_model::namedelement_instantiation(instance):
    assert isinstance(instance, model::NamedElement)

@given(instance=model::NamedElement_strategy)
def test_model::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::NamedElement_strategy)
def test_model::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
