import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Command,
    model_Wait,
    model_Repeat,
    model_Rotate,
    model_Light,
    model_Move,
    NamedElement,
    model_Block,
    model_Transition,
    model_Command,
    model_Ozobot,
    model_OzobotProgram,
    model_NamedElement,
    Direction,
    Velocity,
    Color,
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



def test_model_wait_is_not_abstract():
    assert not inspect.isabstract(model_Wait)


def test_model_wait_constructor_exists():
    assert callable(model_Wait.__init__)


def test_model_wait_constructor_args():
    sig = inspect.signature(model_Wait.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_model_wait_has_time():
    assert hasattr(model_Wait, "time")
    descriptor = None
    for klass in model_Wait.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_model_repeat_is_not_abstract():
    assert not inspect.isabstract(model_Repeat)


def test_model_repeat_constructor_exists():
    assert callable(model_Repeat.__init__)


def test_model_repeat_constructor_args():
    sig = inspect.signature(model_Repeat.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_model_repeat_has_count():
    assert hasattr(model_Repeat, "count")
    descriptor = None
    for klass in model_Repeat.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_model_rotate_is_not_abstract():
    assert not inspect.isabstract(model_Rotate)


def test_model_rotate_constructor_exists():
    assert callable(model_Rotate.__init__)


def test_model_rotate_constructor_args():
    sig = inspect.signature(model_Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "velocity" in params, "Missing parameter 'velocity'"

def test_model_rotate_has_angle():
    assert hasattr(model_Rotate, "angle")
    descriptor = None
    for klass in model_Rotate.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)

def test_model_rotate_has_direction():
    assert hasattr(model_Rotate, "direction")
    descriptor = None
    for klass in model_Rotate.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_model_rotate_has_velocity():
    assert hasattr(model_Rotate, "velocity")
    descriptor = None
    for klass in model_Rotate.__mro__:
        if "velocity" in klass.__dict__:
            descriptor = klass.__dict__["velocity"]
            break
    assert isinstance(descriptor, property)



def test_model_light_is_not_abstract():
    assert not inspect.isabstract(model_Light)


def test_model_light_constructor_exists():
    assert callable(model_Light.__init__)


def test_model_light_constructor_args():
    sig = inspect.signature(model_Light.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_model_light_has_color():
    assert hasattr(model_Light, "color")
    descriptor = None
    for klass in model_Light.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_model_move_is_not_abstract():
    assert not inspect.isabstract(model_Move)


def test_model_move_constructor_exists():
    assert callable(model_Move.__init__)


def test_model_move_constructor_args():
    sig = inspect.signature(model_Move.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"
    assert "velocity" in params, "Missing parameter 'velocity'"

def test_model_move_has_distance():
    assert hasattr(model_Move, "distance")
    descriptor = None
    for klass in model_Move.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_model_move_has_velocity():
    assert hasattr(model_Move, "velocity")
    descriptor = None
    for klass in model_Move.__mro__:
        if "velocity" in klass.__dict__:
            descriptor = klass.__dict__["velocity"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_model_block_is_not_abstract():
    assert not inspect.isabstract(model_Block)


def test_model_block_constructor_exists():
    assert callable(model_Block.__init__)


def test_model_block_constructor_args():
    sig = inspect.signature(model_Block.__init__)
    params = list(sig.parameters.keys())



def test_model_transition_is_not_abstract():
    assert not inspect.isabstract(model_Transition)


def test_model_transition_constructor_exists():
    assert callable(model_Transition.__init__)


def test_model_transition_constructor_args():
    sig = inspect.signature(model_Transition.__init__)
    params = list(sig.parameters.keys())



def test_model_command_is_not_abstract():
    assert not inspect.isabstract(model_Command)


def test_model_command_constructor_exists():
    assert callable(model_Command.__init__)


def test_model_command_constructor_args():
    sig = inspect.signature(model_Command.__init__)
    params = list(sig.parameters.keys())



def test_model_ozobot_is_not_abstract():
    assert not inspect.isabstract(model_Ozobot)


def test_model_ozobot_constructor_exists():
    assert callable(model_Ozobot.__init__)


def test_model_ozobot_constructor_args():
    sig = inspect.signature(model_Ozobot.__init__)
    params = list(sig.parameters.keys())



def test_model_ozobotprogram_is_not_abstract():
    assert not inspect.isabstract(model_OzobotProgram)


def test_model_ozobotprogram_constructor_exists():
    assert callable(model_OzobotProgram.__init__)


def test_model_ozobotprogram_constructor_args():
    sig = inspect.signature(model_OzobotProgram.__init__)
    params = list(sig.parameters.keys())



def test_model_namedelement_is_not_abstract():
    assert not inspect.isabstract(model_NamedElement)


def test_model_namedelement_constructor_exists():
    assert callable(model_NamedElement.__init__)


def test_model_namedelement_constructor_args():
    sig = inspect.signature(model_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_namedelement_has_name():
    assert hasattr(model_NamedElement, "name")
    descriptor = None
    for klass in model_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "left",
        "right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_velocity_exists():
    # Check that the Enumeration exists
    assert Velocity is not None

def test_velocity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Velocity]
    expected_literals = [
        "very_fast",
        "very_slow",
        "fast",
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
model_Wait_strategy = st.builds(
    model_Wait,
    time=
        st.integers()
)
model_Repeat_strategy = st.builds(
    model_Repeat,
    count=
        st.integers()
)
model_Rotate_strategy = st.builds(
    model_Rotate,
    angle=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    direction=
        safe_text,
    velocity=
        safe_text
)
model_Light_strategy = st.builds(
    model_Light,
    color=
        safe_text
)
model_Move_strategy = st.builds(
    model_Move,
    distance=
        st.integers(),
    velocity=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
model_Block_strategy = st.builds(
    model_Block,
)
model_Transition_strategy = st.builds(
    model_Transition,
)
model_Command_strategy = st.builds(
    model_Command,
)
model_Ozobot_strategy = st.builds(
    model_Ozobot,
)
model_OzobotProgram_strategy = st.builds(
    model_OzobotProgram,
)
model_NamedElement_strategy = st.builds(
    model_NamedElement,
    name=
        safe_text
)

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=model_Wait_strategy)
@settings(max_examples=50)
def test_model_wait_instantiation(instance):
    assert isinstance(instance, model_Wait)



@given(instance=model_Wait_strategy)
def test_model_wait_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=model_Repeat_strategy)
@settings(max_examples=50)
def test_model_repeat_instantiation(instance):
    assert isinstance(instance, model_Repeat)



@given(instance=model_Repeat_strategy)
def test_model_repeat_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=model_Rotate_strategy)
@settings(max_examples=50)
def test_model_rotate_instantiation(instance):
    assert isinstance(instance, model_Rotate)



@given(instance=model_Rotate_strategy)
def test_model_rotate_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=model_Rotate_strategy)
def test_model_rotate_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=model_Rotate_strategy)
def test_model_rotate_velocity_setter(instance):
    original = instance.velocity
    instance.velocity = original
    assert instance.velocity == original

@given(instance=model_Light_strategy)
@settings(max_examples=50)
def test_model_light_instantiation(instance):
    assert isinstance(instance, model_Light)



@given(instance=model_Light_strategy)
def test_model_light_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=model_Move_strategy)
@settings(max_examples=50)
def test_model_move_instantiation(instance):
    assert isinstance(instance, model_Move)



@given(instance=model_Move_strategy)
def test_model_move_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original



@given(instance=model_Move_strategy)
def test_model_move_velocity_setter(instance):
    original = instance.velocity
    instance.velocity = original
    assert instance.velocity == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=model_Block_strategy)
@settings(max_examples=50)
def test_model_block_instantiation(instance):
    assert isinstance(instance, model_Block)

@given(instance=model_Transition_strategy)
@settings(max_examples=50)
def test_model_transition_instantiation(instance):
    assert isinstance(instance, model_Transition)

@given(instance=model_Command_strategy)
@settings(max_examples=50)
def test_model_command_instantiation(instance):
    assert isinstance(instance, model_Command)

@given(instance=model_Ozobot_strategy)
@settings(max_examples=50)
def test_model_ozobot_instantiation(instance):
    assert isinstance(instance, model_Ozobot)

@given(instance=model_OzobotProgram_strategy)
@settings(max_examples=50)
def test_model_ozobotprogram_instantiation(instance):
    assert isinstance(instance, model_OzobotProgram)

@given(instance=model_NamedElement_strategy)
@settings(max_examples=50)
def test_model_namedelement_instantiation(instance):
    assert isinstance(instance, model_NamedElement)



@given(instance=model_NamedElement_strategy)
def test_model_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
