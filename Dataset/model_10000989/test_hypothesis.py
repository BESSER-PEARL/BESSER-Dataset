import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MaglevCar,
    ElectricTrain,
    Maglev,
    ContainerCar,
    PassengerCar,
    EngineCar,
    PassengerTrain,
    FreightTrain,
    T,
    Train,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_maglevcar_is_not_abstract():
    assert not inspect.isabstract(MaglevCar)


def test_maglevcar_constructor_exists():
    assert callable(MaglevCar.__init__)


def test_maglevcar_constructor_args():
    sig = inspect.signature(MaglevCar.__init__)
    params = list(sig.parameters.keys())
    assert "numSeatsOccupied" in params, "Missing parameter 'numSeatsOccupied'"
    assert "NUMSEATS" in params, "Missing parameter 'NUMSEATS'"

def test_maglevcar_has_numSeatsOccupied():
    assert hasattr(MaglevCar, "numSeatsOccupied")
    descriptor = None
    for klass in MaglevCar.__mro__:
        if "numSeatsOccupied" in klass.__dict__:
            descriptor = klass.__dict__["numSeatsOccupied"]
            break
    assert isinstance(descriptor, property)

def test_maglevcar_has_NUMSEATS():
    assert hasattr(MaglevCar, "NUMSEATS")
    descriptor = None
    for klass in MaglevCar.__mro__:
        if "NUMSEATS" in klass.__dict__:
            descriptor = klass.__dict__["NUMSEATS"]
            break
    assert isinstance(descriptor, property)



def test_electrictrain_is_not_abstract():
    assert not inspect.isabstract(ElectricTrain)


def test_electrictrain_constructor_exists():
    assert callable(ElectricTrain.__init__)


def test_electrictrain_constructor_args():
    sig = inspect.signature(ElectricTrain.__init__)
    params = list(sig.parameters.keys())
    assert "MAXSPEED" in params, "Missing parameter 'MAXSPEED'"

def test_electrictrain_has_MAXSPEED():
    assert hasattr(ElectricTrain, "MAXSPEED")
    descriptor = None
    for klass in ElectricTrain.__mro__:
        if "MAXSPEED" in klass.__dict__:
            descriptor = klass.__dict__["MAXSPEED"]
            break
    assert isinstance(descriptor, property)



def test_maglev_is_not_abstract():
    assert not inspect.isabstract(Maglev)


def test_maglev_constructor_exists():
    assert callable(Maglev.__init__)


def test_maglev_constructor_args():
    sig = inspect.signature(Maglev.__init__)
    params = list(sig.parameters.keys())
    assert "MAXSPEED" in params, "Missing parameter 'MAXSPEED'"

def test_maglev_has_MAXSPEED():
    assert hasattr(Maglev, "MAXSPEED")
    descriptor = None
    for klass in Maglev.__mro__:
        if "MAXSPEED" in klass.__dict__:
            descriptor = klass.__dict__["MAXSPEED"]
            break
    assert isinstance(descriptor, property)



def test_containercar_is_not_abstract():
    assert not inspect.isabstract(ContainerCar)


def test_containercar_constructor_exists():
    assert callable(ContainerCar.__init__)


def test_containercar_constructor_args():
    sig = inspect.signature(ContainerCar.__init__)
    params = list(sig.parameters.keys())
    assert "cubicFeet" in params, "Missing parameter 'cubicFeet'"
    assert "climateControlled" in params, "Missing parameter 'climateControlled'"
    assert "temp" in params, "Missing parameter 'temp'"

def test_containercar_has_cubicFeet():
    assert hasattr(ContainerCar, "cubicFeet")
    descriptor = None
    for klass in ContainerCar.__mro__:
        if "cubicFeet" in klass.__dict__:
            descriptor = klass.__dict__["cubicFeet"]
            break
    assert isinstance(descriptor, property)

def test_containercar_has_climateControlled():
    assert hasattr(ContainerCar, "climateControlled")
    descriptor = None
    for klass in ContainerCar.__mro__:
        if "climateControlled" in klass.__dict__:
            descriptor = klass.__dict__["climateControlled"]
            break
    assert isinstance(descriptor, property)

def test_containercar_has_temp():
    assert hasattr(ContainerCar, "temp")
    descriptor = None
    for klass in ContainerCar.__mro__:
        if "temp" in klass.__dict__:
            descriptor = klass.__dict__["temp"]
            break
    assert isinstance(descriptor, property)



def test_passengercar_is_not_abstract():
    assert not inspect.isabstract(PassengerCar)


def test_passengercar_constructor_exists():
    assert callable(PassengerCar.__init__)


def test_passengercar_constructor_args():
    sig = inspect.signature(PassengerCar.__init__)
    params = list(sig.parameters.keys())
    assert "NUMSEATS" in params, "Missing parameter 'NUMSEATS'"
    assert "numSeatsOccupied" in params, "Missing parameter 'numSeatsOccupied'"

def test_passengercar_has_NUMSEATS():
    assert hasattr(PassengerCar, "NUMSEATS")
    descriptor = None
    for klass in PassengerCar.__mro__:
        if "NUMSEATS" in klass.__dict__:
            descriptor = klass.__dict__["NUMSEATS"]
            break
    assert isinstance(descriptor, property)

def test_passengercar_has_numSeatsOccupied():
    assert hasattr(PassengerCar, "numSeatsOccupied")
    descriptor = None
    for klass in PassengerCar.__mro__:
        if "numSeatsOccupied" in klass.__dict__:
            descriptor = klass.__dict__["numSeatsOccupied"]
            break
    assert isinstance(descriptor, property)



def test_enginecar_is_not_abstract():
    assert not inspect.isabstract(EngineCar)


def test_enginecar_constructor_exists():
    assert callable(EngineCar.__init__)


def test_enginecar_constructor_args():
    sig = inspect.signature(EngineCar.__init__)
    params = list(sig.parameters.keys())
    assert "MAXSPEED" in params, "Missing parameter 'MAXSPEED'"

def test_enginecar_has_MAXSPEED():
    assert hasattr(EngineCar, "MAXSPEED")
    descriptor = None
    for klass in EngineCar.__mro__:
        if "MAXSPEED" in klass.__dict__:
            descriptor = klass.__dict__["MAXSPEED"]
            break
    assert isinstance(descriptor, property)



def test_passengertrain_is_not_abstract():
    assert not inspect.isabstract(PassengerTrain)


def test_passengertrain_constructor_exists():
    assert callable(PassengerTrain.__init__)


def test_passengertrain_constructor_args():
    sig = inspect.signature(PassengerTrain.__init__)
    params = list(sig.parameters.keys())



def test_freighttrain_is_not_abstract():
    assert not inspect.isabstract(FreightTrain)


def test_freighttrain_constructor_exists():
    assert callable(FreightTrain.__init__)


def test_freighttrain_constructor_args():
    sig = inspect.signature(FreightTrain.__init__)
    params = list(sig.parameters.keys())
    assert "containerTrain" in params, "Missing parameter 'containerTrain'"

def test_freighttrain_has_containerTrain():
    assert hasattr(FreightTrain, "containerTrain")
    descriptor = None
    for klass in FreightTrain.__mro__:
        if "containerTrain" in klass.__dict__:
            descriptor = klass.__dict__["containerTrain"]
            break
    assert isinstance(descriptor, property)



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_train_is_not_abstract():
    assert not inspect.isabstract(Train)


def test_train_constructor_exists():
    assert callable(Train.__init__)


def test_train_constructor_args():
    sig = inspect.signature(Train.__init__)
    params = list(sig.parameters.keys())
    assert "totalCars" in params, "Missing parameter 'totalCars'"
    assert "milesPerHour" in params, "Missing parameter 'milesPerHour'"

def test_train_has_totalCars():
    assert hasattr(Train, "totalCars")
    descriptor = None
    for klass in Train.__mro__:
        if "totalCars" in klass.__dict__:
            descriptor = klass.__dict__["totalCars"]
            break
    assert isinstance(descriptor, property)

def test_train_has_milesPerHour():
    assert hasattr(Train, "milesPerHour")
    descriptor = None
    for klass in Train.__mro__:
        if "milesPerHour" in klass.__dict__:
            descriptor = klass.__dict__["milesPerHour"]
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
MaglevCar_strategy = st.builds(
    MaglevCar,
    numSeatsOccupied=
        st.integers(),
    NUMSEATS=
        st.integers()
)
ElectricTrain_strategy = st.builds(
    ElectricTrain,
    MAXSPEED=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Maglev_strategy = st.builds(
    Maglev,
    MAXSPEED=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ContainerCar_strategy = st.builds(
    ContainerCar,
    cubicFeet=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    climateControlled=
        st.booleans(),
    temp=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
PassengerCar_strategy = st.builds(
    PassengerCar,
    NUMSEATS=
        st.integers(),
    numSeatsOccupied=
        st.integers()
)
EngineCar_strategy = st.builds(
    EngineCar,
    MAXSPEED=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
PassengerTrain_strategy = st.builds(
    PassengerTrain,
)
FreightTrain_strategy = st.builds(
    FreightTrain,
    containerTrain=
        st.booleans()
)
T_strategy = st.builds(
    T,
)
Train_strategy = st.builds(
    Train,
    totalCars=
        st.integers(),
    milesPerHour=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=MaglevCar_strategy)
@settings(max_examples=50)
def test_maglevcar_instantiation(instance):
    assert isinstance(instance, MaglevCar)



@given(instance=MaglevCar_strategy)
def test_maglevcar_numSeatsOccupied_setter(instance):
    original = instance.numSeatsOccupied
    instance.numSeatsOccupied = original
    assert instance.numSeatsOccupied == original



@given(instance=MaglevCar_strategy)
def test_maglevcar_NUMSEATS_setter(instance):
    original = instance.NUMSEATS
    instance.NUMSEATS = original
    assert instance.NUMSEATS == original

@given(instance=ElectricTrain_strategy)
@settings(max_examples=50)
def test_electrictrain_instantiation(instance):
    assert isinstance(instance, ElectricTrain)



@given(instance=ElectricTrain_strategy)
def test_electrictrain_MAXSPEED_setter(instance):
    original = instance.MAXSPEED
    instance.MAXSPEED = original
    assert instance.MAXSPEED == original

@given(instance=Maglev_strategy)
@settings(max_examples=50)
def test_maglev_instantiation(instance):
    assert isinstance(instance, Maglev)



@given(instance=Maglev_strategy)
def test_maglev_MAXSPEED_setter(instance):
    original = instance.MAXSPEED
    instance.MAXSPEED = original
    assert instance.MAXSPEED == original

@given(instance=ContainerCar_strategy)
@settings(max_examples=50)
def test_containercar_instantiation(instance):
    assert isinstance(instance, ContainerCar)



@given(instance=ContainerCar_strategy)
def test_containercar_cubicFeet_setter(instance):
    original = instance.cubicFeet
    instance.cubicFeet = original
    assert instance.cubicFeet == original



@given(instance=ContainerCar_strategy)
def test_containercar_climateControlled_setter(instance):
    original = instance.climateControlled
    instance.climateControlled = original
    assert instance.climateControlled == original



@given(instance=ContainerCar_strategy)
def test_containercar_temp_setter(instance):
    original = instance.temp
    instance.temp = original
    assert instance.temp == original

@given(instance=PassengerCar_strategy)
@settings(max_examples=50)
def test_passengercar_instantiation(instance):
    assert isinstance(instance, PassengerCar)



@given(instance=PassengerCar_strategy)
def test_passengercar_NUMSEATS_setter(instance):
    original = instance.NUMSEATS
    instance.NUMSEATS = original
    assert instance.NUMSEATS == original



@given(instance=PassengerCar_strategy)
def test_passengercar_numSeatsOccupied_setter(instance):
    original = instance.numSeatsOccupied
    instance.numSeatsOccupied = original
    assert instance.numSeatsOccupied == original

@given(instance=EngineCar_strategy)
@settings(max_examples=50)
def test_enginecar_instantiation(instance):
    assert isinstance(instance, EngineCar)



@given(instance=EngineCar_strategy)
def test_enginecar_MAXSPEED_setter(instance):
    original = instance.MAXSPEED
    instance.MAXSPEED = original
    assert instance.MAXSPEED == original

@given(instance=PassengerTrain_strategy)
@settings(max_examples=50)
def test_passengertrain_instantiation(instance):
    assert isinstance(instance, PassengerTrain)

@given(instance=FreightTrain_strategy)
@settings(max_examples=50)
def test_freighttrain_instantiation(instance):
    assert isinstance(instance, FreightTrain)



@given(instance=FreightTrain_strategy)
def test_freighttrain_containerTrain_setter(instance):
    original = instance.containerTrain
    instance.containerTrain = original
    assert instance.containerTrain == original

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=Train_strategy)
@settings(max_examples=50)
def test_train_instantiation(instance):
    assert isinstance(instance, Train)



@given(instance=Train_strategy)
def test_train_totalCars_setter(instance):
    original = instance.totalCars
    instance.totalCars = original
    assert instance.totalCars == original



@given(instance=Train_strategy)
def test_train_milesPerHour_setter(instance):
    original = instance.milesPerHour
    instance.milesPerHour = original
    assert instance.milesPerHour == original
