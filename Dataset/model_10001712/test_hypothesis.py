import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Coach,
    FirstClass,
    PassengerTrain,
    CargoTrain,
    Train,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_coach_is_not_abstract():
    assert not inspect.isabstract(Coach)


def test_coach_constructor_exists():
    assert callable(Coach.__init__)


def test_coach_constructor_args():
    sig = inspect.signature(Coach.__init__)
    params = list(sig.parameters.keys())
    assert "seatsFilled" in params, "Missing parameter 'seatsFilled'"
    assert "numberOfSeats" in params, "Missing parameter 'numberOfSeats'"

def test_coach_has_seatsFilled():
    assert hasattr(Coach, "seatsFilled")
    descriptor = None
    for klass in Coach.__mro__:
        if "seatsFilled" in klass.__dict__:
            descriptor = klass.__dict__["seatsFilled"]
            break
    assert isinstance(descriptor, property)

def test_coach_has_numberOfSeats():
    assert hasattr(Coach, "numberOfSeats")
    descriptor = None
    for klass in Coach.__mro__:
        if "numberOfSeats" in klass.__dict__:
            descriptor = klass.__dict__["numberOfSeats"]
            break
    assert isinstance(descriptor, property)



def test_firstclass_is_not_abstract():
    assert not inspect.isabstract(FirstClass)


def test_firstclass_constructor_exists():
    assert callable(FirstClass.__init__)


def test_firstclass_constructor_args():
    sig = inspect.signature(FirstClass.__init__)
    params = list(sig.parameters.keys())
    assert "seatsFilled" in params, "Missing parameter 'seatsFilled'"
    assert "numberOfSeats" in params, "Missing parameter 'numberOfSeats'"

def test_firstclass_has_seatsFilled():
    assert hasattr(FirstClass, "seatsFilled")
    descriptor = None
    for klass in FirstClass.__mro__:
        if "seatsFilled" in klass.__dict__:
            descriptor = klass.__dict__["seatsFilled"]
            break
    assert isinstance(descriptor, property)

def test_firstclass_has_numberOfSeats():
    assert hasattr(FirstClass, "numberOfSeats")
    descriptor = None
    for klass in FirstClass.__mro__:
        if "numberOfSeats" in klass.__dict__:
            descriptor = klass.__dict__["numberOfSeats"]
            break
    assert isinstance(descriptor, property)



def test_passengertrain_is_not_abstract():
    assert not inspect.isabstract(PassengerTrain)


def test_passengertrain_constructor_exists():
    assert callable(PassengerTrain.__init__)


def test_passengertrain_constructor_args():
    sig = inspect.signature(PassengerTrain.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfPassengers" in params, "Missing parameter 'numberOfPassengers'"
    assert "Stops" in params, "Missing parameter 'Stops'"
    assert "Origin" in params, "Missing parameter 'Origin'"

def test_passengertrain_has_numberOfPassengers():
    assert hasattr(PassengerTrain, "numberOfPassengers")
    descriptor = None
    for klass in PassengerTrain.__mro__:
        if "numberOfPassengers" in klass.__dict__:
            descriptor = klass.__dict__["numberOfPassengers"]
            break
    assert isinstance(descriptor, property)

def test_passengertrain_has_Stops():
    assert hasattr(PassengerTrain, "Stops")
    descriptor = None
    for klass in PassengerTrain.__mro__:
        if "Stops" in klass.__dict__:
            descriptor = klass.__dict__["Stops"]
            break
    assert isinstance(descriptor, property)

def test_passengertrain_has_Origin():
    assert hasattr(PassengerTrain, "Origin")
    descriptor = None
    for klass in PassengerTrain.__mro__:
        if "Origin" in klass.__dict__:
            descriptor = klass.__dict__["Origin"]
            break
    assert isinstance(descriptor, property)



def test_cargotrain_is_not_abstract():
    assert not inspect.isabstract(CargoTrain)


def test_cargotrain_constructor_exists():
    assert callable(CargoTrain.__init__)


def test_cargotrain_constructor_args():
    sig = inspect.signature(CargoTrain.__init__)
    params = list(sig.parameters.keys())
    assert "Containers" in params, "Missing parameter 'Containers'"
    assert "Stops" in params, "Missing parameter 'Stops'"
    assert "Origin" in params, "Missing parameter 'Origin'"

def test_cargotrain_has_Containers():
    assert hasattr(CargoTrain, "Containers")
    descriptor = None
    for klass in CargoTrain.__mro__:
        if "Containers" in klass.__dict__:
            descriptor = klass.__dict__["Containers"]
            break
    assert isinstance(descriptor, property)

def test_cargotrain_has_Stops():
    assert hasattr(CargoTrain, "Stops")
    descriptor = None
    for klass in CargoTrain.__mro__:
        if "Stops" in klass.__dict__:
            descriptor = klass.__dict__["Stops"]
            break
    assert isinstance(descriptor, property)

def test_cargotrain_has_Origin():
    assert hasattr(CargoTrain, "Origin")
    descriptor = None
    for klass in CargoTrain.__mro__:
        if "Origin" in klass.__dict__:
            descriptor = klass.__dict__["Origin"]
            break
    assert isinstance(descriptor, property)



def test_train_is_not_abstract():
    assert not inspect.isabstract(Train)


def test_train_constructor_exists():
    assert callable(Train.__init__)


def test_train_constructor_args():
    sig = inspect.signature(Train.__init__)
    params = list(sig.parameters.keys())
    assert "Cars" in params, "Missing parameter 'Cars'"
    assert "Manufacturer" in params, "Missing parameter 'Manufacturer'"
    assert "Operator" in params, "Missing parameter 'Operator'"
    assert "Power" in params, "Missing parameter 'Power'"

def test_train_has_Cars():
    assert hasattr(Train, "Cars")
    descriptor = None
    for klass in Train.__mro__:
        if "Cars" in klass.__dict__:
            descriptor = klass.__dict__["Cars"]
            break
    assert isinstance(descriptor, property)

def test_train_has_Manufacturer():
    assert hasattr(Train, "Manufacturer")
    descriptor = None
    for klass in Train.__mro__:
        if "Manufacturer" in klass.__dict__:
            descriptor = klass.__dict__["Manufacturer"]
            break
    assert isinstance(descriptor, property)

def test_train_has_Operator():
    assert hasattr(Train, "Operator")
    descriptor = None
    for klass in Train.__mro__:
        if "Operator" in klass.__dict__:
            descriptor = klass.__dict__["Operator"]
            break
    assert isinstance(descriptor, property)

def test_train_has_Power():
    assert hasattr(Train, "Power")
    descriptor = None
    for klass in Train.__mro__:
        if "Power" in klass.__dict__:
            descriptor = klass.__dict__["Power"]
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
Coach_strategy = st.builds(
    Coach,
    seatsFilled=
        st.integers(),
    numberOfSeats=
        st.integers()
)
FirstClass_strategy = st.builds(
    FirstClass,
    seatsFilled=
        st.integers(),
    numberOfSeats=
        st.integers()
)
PassengerTrain_strategy = st.builds(
    PassengerTrain,
    numberOfPassengers=
        st.integers(),
    Stops=
        safe_text,
    Origin=
        safe_text
)
CargoTrain_strategy = st.builds(
    CargoTrain,
    Containers=
        safe_text,
    Stops=
        safe_text,
    Origin=
        safe_text
)
Train_strategy = st.builds(
    Train,
    Cars=
        safe_text,
    Manufacturer=
        safe_text,
    Operator=
        safe_text,
    Power=
        safe_text
)

@given(instance=Coach_strategy)
@settings(max_examples=50)
def test_coach_instantiation(instance):
    assert isinstance(instance, Coach)



@given(instance=Coach_strategy)
def test_coach_seatsFilled_setter(instance):
    original = instance.seatsFilled
    instance.seatsFilled = original
    assert instance.seatsFilled == original



@given(instance=Coach_strategy)
def test_coach_numberOfSeats_setter(instance):
    original = instance.numberOfSeats
    instance.numberOfSeats = original
    assert instance.numberOfSeats == original

@given(instance=FirstClass_strategy)
@settings(max_examples=50)
def test_firstclass_instantiation(instance):
    assert isinstance(instance, FirstClass)



@given(instance=FirstClass_strategy)
def test_firstclass_seatsFilled_setter(instance):
    original = instance.seatsFilled
    instance.seatsFilled = original
    assert instance.seatsFilled == original



@given(instance=FirstClass_strategy)
def test_firstclass_numberOfSeats_setter(instance):
    original = instance.numberOfSeats
    instance.numberOfSeats = original
    assert instance.numberOfSeats == original

@given(instance=PassengerTrain_strategy)
@settings(max_examples=50)
def test_passengertrain_instantiation(instance):
    assert isinstance(instance, PassengerTrain)



@given(instance=PassengerTrain_strategy)
def test_passengertrain_numberOfPassengers_setter(instance):
    original = instance.numberOfPassengers
    instance.numberOfPassengers = original
    assert instance.numberOfPassengers == original



@given(instance=PassengerTrain_strategy)
def test_passengertrain_Stops_setter(instance):
    original = instance.Stops
    instance.Stops = original
    assert instance.Stops == original



@given(instance=PassengerTrain_strategy)
def test_passengertrain_Origin_setter(instance):
    original = instance.Origin
    instance.Origin = original
    assert instance.Origin == original

@given(instance=CargoTrain_strategy)
@settings(max_examples=50)
def test_cargotrain_instantiation(instance):
    assert isinstance(instance, CargoTrain)



@given(instance=CargoTrain_strategy)
def test_cargotrain_Containers_setter(instance):
    original = instance.Containers
    instance.Containers = original
    assert instance.Containers == original



@given(instance=CargoTrain_strategy)
def test_cargotrain_Stops_setter(instance):
    original = instance.Stops
    instance.Stops = original
    assert instance.Stops == original



@given(instance=CargoTrain_strategy)
def test_cargotrain_Origin_setter(instance):
    original = instance.Origin
    instance.Origin = original
    assert instance.Origin == original

@given(instance=Train_strategy)
@settings(max_examples=50)
def test_train_instantiation(instance):
    assert isinstance(instance, Train)



@given(instance=Train_strategy)
def test_train_Cars_setter(instance):
    original = instance.Cars
    instance.Cars = original
    assert instance.Cars == original



@given(instance=Train_strategy)
def test_train_Manufacturer_setter(instance):
    original = instance.Manufacturer
    instance.Manufacturer = original
    assert instance.Manufacturer == original



@given(instance=Train_strategy)
def test_train_Operator_setter(instance):
    original = instance.Operator
    instance.Operator = original
    assert instance.Operator == original



@given(instance=Train_strategy)
def test_train_Power_setter(instance):
    original = instance.Power
    instance.Power = original
    assert instance.Power == original
