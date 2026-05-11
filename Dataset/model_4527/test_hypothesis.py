import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Command,
    helloWeb::Wait,
    helloWeb::Right,
    helloWeb::Left,
    helloWeb::RotateL,
    helloWeb::RotateR,
    helloWeb::Up,
    helloWeb::Backward,
    helloWeb::Forward,
    helloWeb::Down,
    helloWeb::Snapshot,
    SuperCommand,
    helloWeb::FunctionName,
    helloWeb::FeatureMatch,
    helloWeb::Command,
    helloWeb::UserFunction,
    helloWeb::SuperCommand,
    helloWeb::Main,
    helloWeb::Program,
    helloWeb::RecordedFlight,
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



def test_helloweb::wait_is_not_abstract():
    assert not inspect.isabstract(helloWeb::Wait)


def test_helloweb::wait_constructor_exists():
    assert callable(helloWeb::Wait.__init__)


def test_helloweb::wait_constructor_args():
    sig = inspect.signature(helloWeb::Wait.__init__)
    params = list(sig.parameters.keys())
    assert "seconds" in params, "Missing parameter 'seconds'"

def test_helloweb::wait_has_seconds():
    assert hasattr(helloWeb::Wait, "seconds")
    descriptor = None
    for klass in helloWeb::Wait.__mro__:
        if "seconds" in klass.__dict__:
            descriptor = klass.__dict__["seconds"]
            break
    assert isinstance(descriptor, property)



def test_helloweb::right_is_not_abstract():
    assert not inspect.isabstract(helloWeb::Right)


def test_helloweb::right_constructor_exists():
    assert callable(helloWeb::Right.__init__)


def test_helloweb::right_constructor_args():
    sig = inspect.signature(helloWeb::Right.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_helloweb::right_has_distance():
    assert hasattr(helloWeb::Right, "distance")
    descriptor = None
    for klass in helloWeb::Right.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_helloweb::left_is_not_abstract():
    assert not inspect.isabstract(helloWeb::Left)


def test_helloweb::left_constructor_exists():
    assert callable(helloWeb::Left.__init__)


def test_helloweb::left_constructor_args():
    sig = inspect.signature(helloWeb::Left.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_helloweb::left_has_distance():
    assert hasattr(helloWeb::Left, "distance")
    descriptor = None
    for klass in helloWeb::Left.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_helloweb::rotatel_is_not_abstract():
    assert not inspect.isabstract(helloWeb::RotateL)


def test_helloweb::rotatel_constructor_exists():
    assert callable(helloWeb::RotateL.__init__)


def test_helloweb::rotatel_constructor_args():
    sig = inspect.signature(helloWeb::RotateL.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_helloweb::rotatel_has_angle():
    assert hasattr(helloWeb::RotateL, "angle")
    descriptor = None
    for klass in helloWeb::RotateL.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_helloweb::rotater_is_not_abstract():
    assert not inspect.isabstract(helloWeb::RotateR)


def test_helloweb::rotater_constructor_exists():
    assert callable(helloWeb::RotateR.__init__)


def test_helloweb::rotater_constructor_args():
    sig = inspect.signature(helloWeb::RotateR.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_helloweb::rotater_has_angle():
    assert hasattr(helloWeb::RotateR, "angle")
    descriptor = None
    for klass in helloWeb::RotateR.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_helloweb::up_is_not_abstract():
    assert not inspect.isabstract(helloWeb::Up)


def test_helloweb::up_constructor_exists():
    assert callable(helloWeb::Up.__init__)


def test_helloweb::up_constructor_args():
    sig = inspect.signature(helloWeb::Up.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_helloweb::up_has_distance():
    assert hasattr(helloWeb::Up, "distance")
    descriptor = None
    for klass in helloWeb::Up.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_helloweb::backward_is_not_abstract():
    assert not inspect.isabstract(helloWeb::Backward)


def test_helloweb::backward_constructor_exists():
    assert callable(helloWeb::Backward.__init__)


def test_helloweb::backward_constructor_args():
    sig = inspect.signature(helloWeb::Backward.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_helloweb::backward_has_distance():
    assert hasattr(helloWeb::Backward, "distance")
    descriptor = None
    for klass in helloWeb::Backward.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_helloweb::forward_is_not_abstract():
    assert not inspect.isabstract(helloWeb::Forward)


def test_helloweb::forward_constructor_exists():
    assert callable(helloWeb::Forward.__init__)


def test_helloweb::forward_constructor_args():
    sig = inspect.signature(helloWeb::Forward.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_helloweb::forward_has_distance():
    assert hasattr(helloWeb::Forward, "distance")
    descriptor = None
    for klass in helloWeb::Forward.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_helloweb::down_is_not_abstract():
    assert not inspect.isabstract(helloWeb::Down)


def test_helloweb::down_constructor_exists():
    assert callable(helloWeb::Down.__init__)


def test_helloweb::down_constructor_args():
    sig = inspect.signature(helloWeb::Down.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_helloweb::down_has_distance():
    assert hasattr(helloWeb::Down, "distance")
    descriptor = None
    for klass in helloWeb::Down.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_helloweb::snapshot_is_not_abstract():
    assert not inspect.isabstract(helloWeb::Snapshot)


def test_helloweb::snapshot_constructor_exists():
    assert callable(helloWeb::Snapshot.__init__)


def test_helloweb::snapshot_constructor_args():
    sig = inspect.signature(helloWeb::Snapshot.__init__)
    params = list(sig.parameters.keys())
    assert "image_name" in params, "Missing parameter 'image_name'"

def test_helloweb::snapshot_has_image_name():
    assert hasattr(helloWeb::Snapshot, "image_name")
    descriptor = None
    for klass in helloWeb::Snapshot.__mro__:
        if "image_name" in klass.__dict__:
            descriptor = klass.__dict__["image_name"]
            break
    assert isinstance(descriptor, property)



def test_supercommand_is_not_abstract():
    assert not inspect.isabstract(SuperCommand)


def test_supercommand_constructor_exists():
    assert callable(SuperCommand.__init__)


def test_supercommand_constructor_args():
    sig = inspect.signature(SuperCommand.__init__)
    params = list(sig.parameters.keys())



def test_helloweb::functionname_is_not_abstract():
    assert not inspect.isabstract(helloWeb::FunctionName)


def test_helloweb::functionname_constructor_exists():
    assert callable(helloWeb::FunctionName.__init__)


def test_helloweb::functionname_constructor_args():
    sig = inspect.signature(helloWeb::FunctionName.__init__)
    params = list(sig.parameters.keys())
    assert "func_name" in params, "Missing parameter 'func_name'"

def test_helloweb::functionname_has_func_name():
    assert hasattr(helloWeb::FunctionName, "func_name")
    descriptor = None
    for klass in helloWeb::FunctionName.__mro__:
        if "func_name" in klass.__dict__:
            descriptor = klass.__dict__["func_name"]
            break
    assert isinstance(descriptor, property)



def test_helloweb::featurematch_is_not_abstract():
    assert not inspect.isabstract(helloWeb::FeatureMatch)


def test_helloweb::featurematch_constructor_exists():
    assert callable(helloWeb::FeatureMatch.__init__)


def test_helloweb::featurematch_constructor_args():
    sig = inspect.signature(helloWeb::FeatureMatch.__init__)
    params = list(sig.parameters.keys())
    assert "image_name" in params, "Missing parameter 'image_name'"

def test_helloweb::featurematch_has_image_name():
    assert hasattr(helloWeb::FeatureMatch, "image_name")
    descriptor = None
    for klass in helloWeb::FeatureMatch.__mro__:
        if "image_name" in klass.__dict__:
            descriptor = klass.__dict__["image_name"]
            break
    assert isinstance(descriptor, property)



def test_helloweb::command_is_not_abstract():
    assert not inspect.isabstract(helloWeb::Command)


def test_helloweb::command_constructor_exists():
    assert callable(helloWeb::Command.__init__)


def test_helloweb::command_constructor_args():
    sig = inspect.signature(helloWeb::Command.__init__)
    params = list(sig.parameters.keys())



def test_helloweb::userfunction_is_not_abstract():
    assert not inspect.isabstract(helloWeb::UserFunction)


def test_helloweb::userfunction_constructor_exists():
    assert callable(helloWeb::UserFunction.__init__)


def test_helloweb::userfunction_constructor_args():
    sig = inspect.signature(helloWeb::UserFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloweb::userfunction_has_name():
    assert hasattr(helloWeb::UserFunction, "name")
    descriptor = None
    for klass in helloWeb::UserFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_helloweb::supercommand_is_not_abstract():
    assert not inspect.isabstract(helloWeb::SuperCommand)


def test_helloweb::supercommand_constructor_exists():
    assert callable(helloWeb::SuperCommand.__init__)


def test_helloweb::supercommand_constructor_args():
    sig = inspect.signature(helloWeb::SuperCommand.__init__)
    params = list(sig.parameters.keys())



def test_helloweb::main_is_not_abstract():
    assert not inspect.isabstract(helloWeb::Main)


def test_helloweb::main_constructor_exists():
    assert callable(helloWeb::Main.__init__)


def test_helloweb::main_constructor_args():
    sig = inspect.signature(helloWeb::Main.__init__)
    params = list(sig.parameters.keys())
    assert "land" in params, "Missing parameter 'land'"
    assert "takeoff" in params, "Missing parameter 'takeoff'"

def test_helloweb::main_has_land():
    assert hasattr(helloWeb::Main, "land")
    descriptor = None
    for klass in helloWeb::Main.__mro__:
        if "land" in klass.__dict__:
            descriptor = klass.__dict__["land"]
            break
    assert isinstance(descriptor, property)

def test_helloweb::main_has_takeoff():
    assert hasattr(helloWeb::Main, "takeoff")
    descriptor = None
    for klass in helloWeb::Main.__mro__:
        if "takeoff" in klass.__dict__:
            descriptor = klass.__dict__["takeoff"]
            break
    assert isinstance(descriptor, property)



def test_helloweb::program_is_not_abstract():
    assert not inspect.isabstract(helloWeb::Program)


def test_helloweb::program_constructor_exists():
    assert callable(helloWeb::Program.__init__)


def test_helloweb::program_constructor_args():
    sig = inspect.signature(helloWeb::Program.__init__)
    params = list(sig.parameters.keys())



def test_helloweb::recordedflight_is_not_abstract():
    assert not inspect.isabstract(helloWeb::RecordedFlight)


def test_helloweb::recordedflight_constructor_exists():
    assert callable(helloWeb::RecordedFlight.__init__)


def test_helloweb::recordedflight_constructor_args():
    sig = inspect.signature(helloWeb::RecordedFlight.__init__)
    params = list(sig.parameters.keys())
    assert "video_name" in params, "Missing parameter 'video_name'"

def test_helloweb::recordedflight_has_video_name():
    assert hasattr(helloWeb::RecordedFlight, "video_name")
    descriptor = None
    for klass in helloWeb::RecordedFlight.__mro__:
        if "video_name" in klass.__dict__:
            descriptor = klass.__dict__["video_name"]
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
Command_strategy = st.builds(
    Command,
)
helloWeb::Wait_strategy = st.builds(
    helloWeb::Wait,
    seconds=
        safe_text
)
helloWeb::Right_strategy = st.builds(
    helloWeb::Right,
    distance=
        safe_text
)
helloWeb::Left_strategy = st.builds(
    helloWeb::Left,
    distance=
        safe_text
)
helloWeb::RotateL_strategy = st.builds(
    helloWeb::RotateL,
    angle=
        st.integers()
)
helloWeb::RotateR_strategy = st.builds(
    helloWeb::RotateR,
    angle=
        st.integers()
)
helloWeb::Up_strategy = st.builds(
    helloWeb::Up,
    distance=
        safe_text
)
helloWeb::Backward_strategy = st.builds(
    helloWeb::Backward,
    distance=
        safe_text
)
helloWeb::Forward_strategy = st.builds(
    helloWeb::Forward,
    distance=
        safe_text
)
helloWeb::Down_strategy = st.builds(
    helloWeb::Down,
    distance=
        safe_text
)
helloWeb::Snapshot_strategy = st.builds(
    helloWeb::Snapshot,
    image_name=
        safe_text
)
SuperCommand_strategy = st.builds(
    SuperCommand,
)
helloWeb::FunctionName_strategy = st.builds(
    helloWeb::FunctionName,
    func_name=
        safe_text
)
helloWeb::FeatureMatch_strategy = st.builds(
    helloWeb::FeatureMatch,
    image_name=
        safe_text
)
helloWeb::Command_strategy = st.builds(
    helloWeb::Command,
)
helloWeb::UserFunction_strategy = st.builds(
    helloWeb::UserFunction,
    name=
        safe_text
)
helloWeb::SuperCommand_strategy = st.builds(
    helloWeb::SuperCommand,
)
helloWeb::Main_strategy = st.builds(
    helloWeb::Main,
    land=
        safe_text,
    takeoff=
        safe_text
)
helloWeb::Program_strategy = st.builds(
    helloWeb::Program,
)
helloWeb::RecordedFlight_strategy = st.builds(
    helloWeb::RecordedFlight,
    video_name=
        safe_text
)

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=helloWeb::Wait_strategy)
@settings(max_examples=50)
def test_helloweb::wait_instantiation(instance):
    assert isinstance(instance, helloWeb::Wait)

@given(instance=helloWeb::Wait_strategy)
def test_helloweb::wait_seconds_type(instance):
    assert isinstance(instance.seconds, str)


@given(instance=helloWeb::Wait_strategy)
def test_helloweb::wait_seconds_setter(instance):
    original = instance.seconds
    instance.seconds = original
    assert instance.seconds == original

@given(instance=helloWeb::Right_strategy)
@settings(max_examples=50)
def test_helloweb::right_instantiation(instance):
    assert isinstance(instance, helloWeb::Right)

@given(instance=helloWeb::Right_strategy)
def test_helloweb::right_distance_type(instance):
    assert isinstance(instance.distance, str)


@given(instance=helloWeb::Right_strategy)
def test_helloweb::right_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=helloWeb::Left_strategy)
@settings(max_examples=50)
def test_helloweb::left_instantiation(instance):
    assert isinstance(instance, helloWeb::Left)

@given(instance=helloWeb::Left_strategy)
def test_helloweb::left_distance_type(instance):
    assert isinstance(instance.distance, str)


@given(instance=helloWeb::Left_strategy)
def test_helloweb::left_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=helloWeb::RotateL_strategy)
@settings(max_examples=50)
def test_helloweb::rotatel_instantiation(instance):
    assert isinstance(instance, helloWeb::RotateL)

@given(instance=helloWeb::RotateL_strategy)
def test_helloweb::rotatel_angle_type(instance):
    assert isinstance(instance.angle, int)


@given(instance=helloWeb::RotateL_strategy)
def test_helloweb::rotatel_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=helloWeb::RotateR_strategy)
@settings(max_examples=50)
def test_helloweb::rotater_instantiation(instance):
    assert isinstance(instance, helloWeb::RotateR)

@given(instance=helloWeb::RotateR_strategy)
def test_helloweb::rotater_angle_type(instance):
    assert isinstance(instance.angle, int)


@given(instance=helloWeb::RotateR_strategy)
def test_helloweb::rotater_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=helloWeb::Up_strategy)
@settings(max_examples=50)
def test_helloweb::up_instantiation(instance):
    assert isinstance(instance, helloWeb::Up)

@given(instance=helloWeb::Up_strategy)
def test_helloweb::up_distance_type(instance):
    assert isinstance(instance.distance, str)


@given(instance=helloWeb::Up_strategy)
def test_helloweb::up_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=helloWeb::Backward_strategy)
@settings(max_examples=50)
def test_helloweb::backward_instantiation(instance):
    assert isinstance(instance, helloWeb::Backward)

@given(instance=helloWeb::Backward_strategy)
def test_helloweb::backward_distance_type(instance):
    assert isinstance(instance.distance, str)


@given(instance=helloWeb::Backward_strategy)
def test_helloweb::backward_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=helloWeb::Forward_strategy)
@settings(max_examples=50)
def test_helloweb::forward_instantiation(instance):
    assert isinstance(instance, helloWeb::Forward)

@given(instance=helloWeb::Forward_strategy)
def test_helloweb::forward_distance_type(instance):
    assert isinstance(instance.distance, str)


@given(instance=helloWeb::Forward_strategy)
def test_helloweb::forward_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=helloWeb::Down_strategy)
@settings(max_examples=50)
def test_helloweb::down_instantiation(instance):
    assert isinstance(instance, helloWeb::Down)

@given(instance=helloWeb::Down_strategy)
def test_helloweb::down_distance_type(instance):
    assert isinstance(instance.distance, str)


@given(instance=helloWeb::Down_strategy)
def test_helloweb::down_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=helloWeb::Snapshot_strategy)
@settings(max_examples=50)
def test_helloweb::snapshot_instantiation(instance):
    assert isinstance(instance, helloWeb::Snapshot)

@given(instance=helloWeb::Snapshot_strategy)
def test_helloweb::snapshot_image_name_type(instance):
    assert isinstance(instance.image_name, str)


@given(instance=helloWeb::Snapshot_strategy)
def test_helloweb::snapshot_image_name_setter(instance):
    original = instance.image_name
    instance.image_name = original
    assert instance.image_name == original

@given(instance=SuperCommand_strategy)
@settings(max_examples=50)
def test_supercommand_instantiation(instance):
    assert isinstance(instance, SuperCommand)

@given(instance=helloWeb::FunctionName_strategy)
@settings(max_examples=50)
def test_helloweb::functionname_instantiation(instance):
    assert isinstance(instance, helloWeb::FunctionName)

@given(instance=helloWeb::FunctionName_strategy)
def test_helloweb::functionname_func_name_type(instance):
    assert isinstance(instance.func_name, str)


@given(instance=helloWeb::FunctionName_strategy)
def test_helloweb::functionname_func_name_setter(instance):
    original = instance.func_name
    instance.func_name = original
    assert instance.func_name == original

@given(instance=helloWeb::FeatureMatch_strategy)
@settings(max_examples=50)
def test_helloweb::featurematch_instantiation(instance):
    assert isinstance(instance, helloWeb::FeatureMatch)

@given(instance=helloWeb::FeatureMatch_strategy)
def test_helloweb::featurematch_image_name_type(instance):
    assert isinstance(instance.image_name, str)


@given(instance=helloWeb::FeatureMatch_strategy)
def test_helloweb::featurematch_image_name_setter(instance):
    original = instance.image_name
    instance.image_name = original
    assert instance.image_name == original

@given(instance=helloWeb::Command_strategy)
@settings(max_examples=50)
def test_helloweb::command_instantiation(instance):
    assert isinstance(instance, helloWeb::Command)

@given(instance=helloWeb::UserFunction_strategy)
@settings(max_examples=50)
def test_helloweb::userfunction_instantiation(instance):
    assert isinstance(instance, helloWeb::UserFunction)

@given(instance=helloWeb::UserFunction_strategy)
def test_helloweb::userfunction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=helloWeb::UserFunction_strategy)
def test_helloweb::userfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloWeb::SuperCommand_strategy)
@settings(max_examples=50)
def test_helloweb::supercommand_instantiation(instance):
    assert isinstance(instance, helloWeb::SuperCommand)

@given(instance=helloWeb::Main_strategy)
@settings(max_examples=50)
def test_helloweb::main_instantiation(instance):
    assert isinstance(instance, helloWeb::Main)

@given(instance=helloWeb::Main_strategy)
def test_helloweb::main_land_type(instance):
    assert isinstance(instance.land, str)


@given(instance=helloWeb::Main_strategy)
def test_helloweb::main_land_setter(instance):
    original = instance.land
    instance.land = original
    assert instance.land == original

@given(instance=helloWeb::Main_strategy)
def test_helloweb::main_takeoff_type(instance):
    assert isinstance(instance.takeoff, str)


@given(instance=helloWeb::Main_strategy)
def test_helloweb::main_takeoff_setter(instance):
    original = instance.takeoff
    instance.takeoff = original
    assert instance.takeoff == original

@given(instance=helloWeb::Program_strategy)
@settings(max_examples=50)
def test_helloweb::program_instantiation(instance):
    assert isinstance(instance, helloWeb::Program)

@given(instance=helloWeb::RecordedFlight_strategy)
@settings(max_examples=50)
def test_helloweb::recordedflight_instantiation(instance):
    assert isinstance(instance, helloWeb::RecordedFlight)

@given(instance=helloWeb::RecordedFlight_strategy)
def test_helloweb::recordedflight_video_name_type(instance):
    assert isinstance(instance.video_name, str)


@given(instance=helloWeb::RecordedFlight_strategy)
def test_helloweb::recordedflight_video_name_setter(instance):
    original = instance.video_name
    instance.video_name = original
    assert instance.video_name == original
