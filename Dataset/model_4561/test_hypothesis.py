import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    platoon::PlatooningSystem,
    platoon::JoiningPosition,
    platoon::JoinPlatoonCoord,
    platoon::Platoon,
    platoon::FrontGap,
    Vehicle,
    platoon::PlatoonVehicle,
    platoon::JoiningVehicle,
    platoon::Vehicle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_platoon::platooningsystem_is_not_abstract():
    assert not inspect.isabstract(platoon::PlatooningSystem)


def test_platoon::platooningsystem_constructor_exists():
    assert callable(platoon::PlatooningSystem.__init__)


def test_platoon::platooningsystem_constructor_args():
    sig = inspect.signature(platoon::PlatooningSystem.__init__)
    params = list(sig.parameters.keys())



def test_platoon::joiningposition_is_not_abstract():
    assert not inspect.isabstract(platoon::JoiningPosition)


def test_platoon::joiningposition_constructor_exists():
    assert callable(platoon::JoiningPosition.__init__)


def test_platoon::joiningposition_constructor_args():
    sig = inspect.signature(platoon::JoiningPosition.__init__)
    params = list(sig.parameters.keys())



def test_platoon::joinplatooncoord_is_not_abstract():
    assert not inspect.isabstract(platoon::JoinPlatoonCoord)


def test_platoon::joinplatooncoord_constructor_exists():
    assert callable(platoon::JoinPlatoonCoord.__init__)


def test_platoon::joinplatooncoord_constructor_args():
    sig = inspect.signature(platoon::JoinPlatoonCoord.__init__)
    params = list(sig.parameters.keys())



def test_platoon::platoon_is_not_abstract():
    assert not inspect.isabstract(platoon::Platoon)


def test_platoon::platoon_constructor_exists():
    assert callable(platoon::Platoon.__init__)


def test_platoon::platoon_constructor_args():
    sig = inspect.signature(platoon::Platoon.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "desiredGapSize" in params, "Missing parameter 'desiredGapSize'"

def test_platoon::platoon_has_length():
    assert hasattr(platoon::Platoon, "length")
    descriptor = None
    for klass in platoon::Platoon.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_platoon::platoon_has_desiredGapSize():
    assert hasattr(platoon::Platoon, "desiredGapSize")
    descriptor = None
    for klass in platoon::Platoon.__mro__:
        if "desiredGapSize" in klass.__dict__:
            descriptor = klass.__dict__["desiredGapSize"]
            break
    assert isinstance(descriptor, property)



def test_platoon::frontgap_is_not_abstract():
    assert not inspect.isabstract(platoon::FrontGap)


def test_platoon::frontgap_constructor_exists():
    assert callable(platoon::FrontGap.__init__)


def test_platoon::frontgap_constructor_args():
    sig = inspect.signature(platoon::FrontGap.__init__)
    params = list(sig.parameters.keys())
    assert "actualGapSize" in params, "Missing parameter 'actualGapSize'"

def test_platoon::frontgap_has_actualGapSize():
    assert hasattr(platoon::FrontGap, "actualGapSize")
    descriptor = None
    for klass in platoon::FrontGap.__mro__:
        if "actualGapSize" in klass.__dict__:
            descriptor = klass.__dict__["actualGapSize"]
            break
    assert isinstance(descriptor, property)



def test_vehicle_is_not_abstract():
    assert not inspect.isabstract(Vehicle)


def test_vehicle_constructor_exists():
    assert callable(Vehicle.__init__)


def test_vehicle_constructor_args():
    sig = inspect.signature(Vehicle.__init__)
    params = list(sig.parameters.keys())



def test_platoon::platoonvehicle_is_not_abstract():
    assert not inspect.isabstract(platoon::PlatoonVehicle)


def test_platoon::platoonvehicle_constructor_exists():
    assert callable(platoon::PlatoonVehicle.__init__)


def test_platoon::platoonvehicle_constructor_args():
    sig = inspect.signature(platoon::PlatoonVehicle.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_platoon::platoonvehicle_has_position():
    assert hasattr(platoon::PlatoonVehicle, "position")
    descriptor = None
    for klass in platoon::PlatoonVehicle.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_platoon::joiningvehicle_is_not_abstract():
    assert not inspect.isabstract(platoon::JoiningVehicle)


def test_platoon::joiningvehicle_constructor_exists():
    assert callable(platoon::JoiningVehicle.__init__)


def test_platoon::joiningvehicle_constructor_args():
    sig = inspect.signature(platoon::JoiningVehicle.__init__)
    params = list(sig.parameters.keys())



def test_platoon::vehicle_is_not_abstract():
    assert not inspect.isabstract(platoon::Vehicle)


def test_platoon::vehicle_constructor_exists():
    assert callable(platoon::Vehicle.__init__)


def test_platoon::vehicle_constructor_args():
    sig = inspect.signature(platoon::Vehicle.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_platoon::vehicle_has_id():
    assert hasattr(platoon::Vehicle, "id")
    descriptor = None
    for klass in platoon::Vehicle.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
platoon::PlatooningSystem_strategy = st.builds(
    platoon::PlatooningSystem,
)
platoon::JoiningPosition_strategy = st.builds(
    platoon::JoiningPosition,
)
platoon::JoinPlatoonCoord_strategy = st.builds(
    platoon::JoinPlatoonCoord,
)
platoon::Platoon_strategy = st.builds(
    platoon::Platoon,
    length=
        st.integers(),
    desiredGapSize=
        st.integers()
)
platoon::FrontGap_strategy = st.builds(
    platoon::FrontGap,
    actualGapSize=
        st.integers()
)
Vehicle_strategy = st.builds(
    Vehicle,
)
platoon::PlatoonVehicle_strategy = st.builds(
    platoon::PlatoonVehicle,
    position=
        st.integers()
)
platoon::JoiningVehicle_strategy = st.builds(
    platoon::JoiningVehicle,
)
platoon::Vehicle_strategy = st.builds(
    platoon::Vehicle,
    id=
        st.integers()
)

@given(instance=platoon::PlatooningSystem_strategy)
@settings(max_examples=50)
def test_platoon::platooningsystem_instantiation(instance):
    assert isinstance(instance, platoon::PlatooningSystem)

@given(instance=platoon::JoiningPosition_strategy)
@settings(max_examples=50)
def test_platoon::joiningposition_instantiation(instance):
    assert isinstance(instance, platoon::JoiningPosition)

@given(instance=platoon::JoinPlatoonCoord_strategy)
@settings(max_examples=50)
def test_platoon::joinplatooncoord_instantiation(instance):
    assert isinstance(instance, platoon::JoinPlatoonCoord)

@given(instance=platoon::Platoon_strategy)
@settings(max_examples=50)
def test_platoon::platoon_instantiation(instance):
    assert isinstance(instance, platoon::Platoon)

@given(instance=platoon::Platoon_strategy)
def test_platoon::platoon_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=platoon::Platoon_strategy)
def test_platoon::platoon_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=platoon::Platoon_strategy)
def test_platoon::platoon_desiredGapSize_type(instance):
    assert isinstance(instance.desiredGapSize, int)


@given(instance=platoon::Platoon_strategy)
def test_platoon::platoon_desiredGapSize_setter(instance):
    original = instance.desiredGapSize
    instance.desiredGapSize = original
    assert instance.desiredGapSize == original

@given(instance=platoon::FrontGap_strategy)
@settings(max_examples=50)
def test_platoon::frontgap_instantiation(instance):
    assert isinstance(instance, platoon::FrontGap)

@given(instance=platoon::FrontGap_strategy)
def test_platoon::frontgap_actualGapSize_type(instance):
    assert isinstance(instance.actualGapSize, int)


@given(instance=platoon::FrontGap_strategy)
def test_platoon::frontgap_actualGapSize_setter(instance):
    original = instance.actualGapSize
    instance.actualGapSize = original
    assert instance.actualGapSize == original

@given(instance=Vehicle_strategy)
@settings(max_examples=50)
def test_vehicle_instantiation(instance):
    assert isinstance(instance, Vehicle)

@given(instance=platoon::PlatoonVehicle_strategy)
@settings(max_examples=50)
def test_platoon::platoonvehicle_instantiation(instance):
    assert isinstance(instance, platoon::PlatoonVehicle)

@given(instance=platoon::PlatoonVehicle_strategy)
def test_platoon::platoonvehicle_position_type(instance):
    assert isinstance(instance.position, int)


@given(instance=platoon::PlatoonVehicle_strategy)
def test_platoon::platoonvehicle_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=platoon::JoiningVehicle_strategy)
@settings(max_examples=50)
def test_platoon::joiningvehicle_instantiation(instance):
    assert isinstance(instance, platoon::JoiningVehicle)

@given(instance=platoon::Vehicle_strategy)
@settings(max_examples=50)
def test_platoon::vehicle_instantiation(instance):
    assert isinstance(instance, platoon::Vehicle)

@given(instance=platoon::Vehicle_strategy)
def test_platoon::vehicle_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=platoon::Vehicle_strategy)
def test_platoon::vehicle_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
