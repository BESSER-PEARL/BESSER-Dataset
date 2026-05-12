import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Train,
    Car1,
    Airplane,
    Boat,
    Vehicle,
    Car,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_train_is_not_abstract():
    assert not inspect.isabstract(Train)


def test_train_constructor_exists():
    assert callable(Train.__init__)


def test_train_constructor_args():
    sig = inspect.signature(Train.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "trucks" in params, "Missing parameter 'trucks'"

def test_train_has_type():
    assert hasattr(Train, "type")
    descriptor = None
    for klass in Train.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_train_has_trucks():
    assert hasattr(Train, "trucks")
    descriptor = None
    for klass in Train.__mro__:
        if "trucks" in klass.__dict__:
            descriptor = klass.__dict__["trucks"]
            break
    assert isinstance(descriptor, property)



def test_car1_is_not_abstract():
    assert not inspect.isabstract(Car1)


def test_car1_constructor_exists():
    assert callable(Car1.__init__)


def test_car1_constructor_args():
    sig = inspect.signature(Car1.__init__)
    params = list(sig.parameters.keys())
    assert "helmSide" in params, "Missing parameter 'helmSide'"
    assert "doors" in params, "Missing parameter 'doors'"

def test_car1_has_helmSide():
    assert hasattr(Car1, "helmSide")
    descriptor = None
    for klass in Car1.__mro__:
        if "helmSide" in klass.__dict__:
            descriptor = klass.__dict__["helmSide"]
            break
    assert isinstance(descriptor, property)

def test_car1_has_doors():
    assert hasattr(Car1, "doors")
    descriptor = None
    for klass in Car1.__mro__:
        if "doors" in klass.__dict__:
            descriptor = klass.__dict__["doors"]
            break
    assert isinstance(descriptor, property)



def test_airplane_is_not_abstract():
    assert not inspect.isabstract(Airplane)


def test_airplane_constructor_exists():
    assert callable(Airplane.__init__)


def test_airplane_constructor_args():
    sig = inspect.signature(Airplane.__init__)
    params = list(sig.parameters.keys())
    assert "maxAttitude" in params, "Missing parameter 'maxAttitude'"
    assert "maxCarryingWeight" in params, "Missing parameter 'maxCarryingWeight'"

def test_airplane_has_maxAttitude():
    assert hasattr(Airplane, "maxAttitude")
    descriptor = None
    for klass in Airplane.__mro__:
        if "maxAttitude" in klass.__dict__:
            descriptor = klass.__dict__["maxAttitude"]
            break
    assert isinstance(descriptor, property)

def test_airplane_has_maxCarryingWeight():
    assert hasattr(Airplane, "maxCarryingWeight")
    descriptor = None
    for klass in Airplane.__mro__:
        if "maxCarryingWeight" in klass.__dict__:
            descriptor = klass.__dict__["maxCarryingWeight"]
            break
    assert isinstance(descriptor, property)



def test_boat_is_not_abstract():
    assert not inspect.isabstract(Boat)


def test_boat_constructor_exists():
    assert callable(Boat.__init__)


def test_boat_constructor_args():
    sig = inspect.signature(Boat.__init__)
    params = list(sig.parameters.keys())
    assert "maxCarryingWeight" in params, "Missing parameter 'maxCarryingWeight'"

def test_boat_has_maxCarryingWeight():
    assert hasattr(Boat, "maxCarryingWeight")
    descriptor = None
    for klass in Boat.__mro__:
        if "maxCarryingWeight" in klass.__dict__:
            descriptor = klass.__dict__["maxCarryingWeight"]
            break
    assert isinstance(descriptor, property)



def test_vehicle_is_not_abstract():
    assert not inspect.isabstract(Vehicle)


def test_vehicle_constructor_exists():
    assert callable(Vehicle.__init__)


def test_vehicle_constructor_args():
    sig = inspect.signature(Vehicle.__init__)
    params = list(sig.parameters.keys())
    assert "engine" in params, "Missing parameter 'engine'"
    assert "price" in params, "Missing parameter 'price'"
    assert "brand" in params, "Missing parameter 'brand'"

def test_vehicle_has_engine():
    assert hasattr(Vehicle, "engine")
    descriptor = None
    for klass in Vehicle.__mro__:
        if "engine" in klass.__dict__:
            descriptor = klass.__dict__["engine"]
            break
    assert isinstance(descriptor, property)

def test_vehicle_has_price():
    assert hasattr(Vehicle, "price")
    descriptor = None
    for klass in Vehicle.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_vehicle_has_brand():
    assert hasattr(Vehicle, "brand")
    descriptor = None
    for klass in Vehicle.__mro__:
        if "brand" in klass.__dict__:
            descriptor = klass.__dict__["brand"]
            break
    assert isinstance(descriptor, property)



def test_car_is_not_abstract():
    assert not inspect.isabstract(Car)


def test_car_constructor_exists():
    assert callable(Car.__init__)


def test_car_constructor_args():
    sig = inspect.signature(Car.__init__)
    params = list(sig.parameters.keys())
    assert "model" in params, "Missing parameter 'model'"
    assert "wheels" in params, "Missing parameter 'wheels'"
    assert "engine" in params, "Missing parameter 'engine'"
    assert "doors" in params, "Missing parameter 'doors'"
    assert "length" in params, "Missing parameter 'length'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_car_has_model():
    assert hasattr(Car, "model")
    descriptor = None
    for klass in Car.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_car_has_wheels():
    assert hasattr(Car, "wheels")
    descriptor = None
    for klass in Car.__mro__:
        if "wheels" in klass.__dict__:
            descriptor = klass.__dict__["wheels"]
            break
    assert isinstance(descriptor, property)

def test_car_has_engine():
    assert hasattr(Car, "engine")
    descriptor = None
    for klass in Car.__mro__:
        if "engine" in klass.__dict__:
            descriptor = klass.__dict__["engine"]
            break
    assert isinstance(descriptor, property)

def test_car_has_doors():
    assert hasattr(Car, "doors")
    descriptor = None
    for klass in Car.__mro__:
        if "doors" in klass.__dict__:
            descriptor = klass.__dict__["doors"]
            break
    assert isinstance(descriptor, property)

def test_car_has_length():
    assert hasattr(Car, "length")
    descriptor = None
    for klass in Car.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_car_has_width():
    assert hasattr(Car, "width")
    descriptor = None
    for klass in Car.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_car_has_height():
    assert hasattr(Car, "height")
    descriptor = None
    for klass in Car.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
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
Train_strategy = st.builds(
    Train,
    type=
        safe_text,
    trucks=
        st.integers()
)
Car1_strategy = st.builds(
    Car1,
    helmSide=
        safe_text,
    doors=
        st.integers()
)
Airplane_strategy = st.builds(
    Airplane,
    maxAttitude=
        st.integers(),
    maxCarryingWeight=
        st.integers()
)
Boat_strategy = st.builds(
    Boat,
    maxCarryingWeight=
        st.integers()
)
Vehicle_strategy = st.builds(
    Vehicle,
    engine=
        safe_text,
    price=
        safe_text,
    brand=
        safe_text
)
Car_strategy = st.builds(
    Car,
    model=
        safe_text,
    wheels=
        safe_text,
    engine=
        safe_text,
    doors=
        st.integers(),
    length=
        st.integers(),
    width=
        st.integers(),
    height=
        st.integers()
)

@given(instance=Train_strategy)
@settings(max_examples=50)
def test_train_instantiation(instance):
    assert isinstance(instance, Train)



@given(instance=Train_strategy)
def test_train_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Train_strategy)
def test_train_trucks_setter(instance):
    original = instance.trucks
    instance.trucks = original
    assert instance.trucks == original

@given(instance=Car1_strategy)
@settings(max_examples=50)
def test_car1_instantiation(instance):
    assert isinstance(instance, Car1)



@given(instance=Car1_strategy)
def test_car1_helmSide_setter(instance):
    original = instance.helmSide
    instance.helmSide = original
    assert instance.helmSide == original



@given(instance=Car1_strategy)
def test_car1_doors_setter(instance):
    original = instance.doors
    instance.doors = original
    assert instance.doors == original

@given(instance=Airplane_strategy)
@settings(max_examples=50)
def test_airplane_instantiation(instance):
    assert isinstance(instance, Airplane)



@given(instance=Airplane_strategy)
def test_airplane_maxAttitude_setter(instance):
    original = instance.maxAttitude
    instance.maxAttitude = original
    assert instance.maxAttitude == original



@given(instance=Airplane_strategy)
def test_airplane_maxCarryingWeight_setter(instance):
    original = instance.maxCarryingWeight
    instance.maxCarryingWeight = original
    assert instance.maxCarryingWeight == original

@given(instance=Boat_strategy)
@settings(max_examples=50)
def test_boat_instantiation(instance):
    assert isinstance(instance, Boat)



@given(instance=Boat_strategy)
def test_boat_maxCarryingWeight_setter(instance):
    original = instance.maxCarryingWeight
    instance.maxCarryingWeight = original
    assert instance.maxCarryingWeight == original

@given(instance=Vehicle_strategy)
@settings(max_examples=50)
def test_vehicle_instantiation(instance):
    assert isinstance(instance, Vehicle)



@given(instance=Vehicle_strategy)
def test_vehicle_engine_setter(instance):
    original = instance.engine
    instance.engine = original
    assert instance.engine == original



@given(instance=Vehicle_strategy)
def test_vehicle_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Vehicle_strategy)
def test_vehicle_brand_setter(instance):
    original = instance.brand
    instance.brand = original
    assert instance.brand == original

@given(instance=Car_strategy)
@settings(max_examples=50)
def test_car_instantiation(instance):
    assert isinstance(instance, Car)



@given(instance=Car_strategy)
def test_car_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=Car_strategy)
def test_car_wheels_setter(instance):
    original = instance.wheels
    instance.wheels = original
    assert instance.wheels == original



@given(instance=Car_strategy)
def test_car_engine_setter(instance):
    original = instance.engine
    instance.engine = original
    assert instance.engine == original



@given(instance=Car_strategy)
def test_car_doors_setter(instance):
    original = instance.doors
    instance.doors = original
    assert instance.doors == original



@given(instance=Car_strategy)
def test_car_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=Car_strategy)
def test_car_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=Car_strategy)
def test_car_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original
