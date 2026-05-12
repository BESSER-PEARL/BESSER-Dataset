import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Test,
    TestStand,
    M6,
    Engine,
    Tennis,
    Car,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_is_not_abstract():
    assert not inspect.isabstract(Test)


def test_test_constructor_exists():
    assert callable(Test.__init__)


def test_test_constructor_args():
    sig = inspect.signature(Test.__init__)
    params = list(sig.parameters.keys())



def test_teststand_is_not_abstract():
    assert not inspect.isabstract(TestStand)


def test_teststand_constructor_exists():
    assert callable(TestStand.__init__)


def test_teststand_constructor_args():
    sig = inspect.signature(TestStand.__init__)
    params = list(sig.parameters.keys())
    assert "carToBeTested" in params, "Missing parameter 'carToBeTested'"

def test_teststand_has_carToBeTested():
    assert hasattr(TestStand, "carToBeTested")
    descriptor = None
    for klass in TestStand.__mro__:
        if "carToBeTested" in klass.__dict__:
            descriptor = klass.__dict__["carToBeTested"]
            break
    assert isinstance(descriptor, property)



def test_m6_is_not_abstract():
    assert not inspect.isabstract(M6)


def test_m6_constructor_exists():
    assert callable(M6.__init__)


def test_m6_constructor_args():
    sig = inspect.signature(M6.__init__)
    params = list(sig.parameters.keys())
    assert "manufacturer" in params, "Missing parameter 'manufacturer'"
    assert "color" in params, "Missing parameter 'color'"
    assert "engine" in params, "Missing parameter 'engine'"

def test_m6_has_manufacturer():
    assert hasattr(M6, "manufacturer")
    descriptor = None
    for klass in M6.__mro__:
        if "manufacturer" in klass.__dict__:
            descriptor = klass.__dict__["manufacturer"]
            break
    assert isinstance(descriptor, property)

def test_m6_has_color():
    assert hasattr(M6, "color")
    descriptor = None
    for klass in M6.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_m6_has_engine():
    assert hasattr(M6, "engine")
    descriptor = None
    for klass in M6.__mro__:
        if "engine" in klass.__dict__:
            descriptor = klass.__dict__["engine"]
            break
    assert isinstance(descriptor, property)



def test_engine_is_not_abstract():
    assert not inspect.isabstract(Engine)


def test_engine_constructor_exists():
    assert callable(Engine.__init__)


def test_engine_constructor_args():
    sig = inspect.signature(Engine.__init__)
    params = list(sig.parameters.keys())
    assert "engineSpeed" in params, "Missing parameter 'engineSpeed'"
    assert "efficiencyCoefficient" in params, "Missing parameter 'efficiencyCoefficient'"
    assert "type" in params, "Missing parameter 'type'"

def test_engine_has_engineSpeed():
    assert hasattr(Engine, "engineSpeed")
    descriptor = None
    for klass in Engine.__mro__:
        if "engineSpeed" in klass.__dict__:
            descriptor = klass.__dict__["engineSpeed"]
            break
    assert isinstance(descriptor, property)

def test_engine_has_efficiencyCoefficient():
    assert hasattr(Engine, "efficiencyCoefficient")
    descriptor = None
    for klass in Engine.__mro__:
        if "efficiencyCoefficient" in klass.__dict__:
            descriptor = klass.__dict__["efficiencyCoefficient"]
            break
    assert isinstance(descriptor, property)

def test_engine_has_type():
    assert hasattr(Engine, "type")
    descriptor = None
    for klass in Engine.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_tennis_is_not_abstract():
    assert not inspect.isabstract(Tennis)


def test_tennis_constructor_exists():
    assert callable(Tennis.__init__)


def test_tennis_constructor_args():
    sig = inspect.signature(Tennis.__init__)
    params = list(sig.parameters.keys())
    assert "manufacturer" in params, "Missing parameter 'manufacturer'"
    assert "color" in params, "Missing parameter 'color'"
    assert "engine" in params, "Missing parameter 'engine'"

def test_tennis_has_manufacturer():
    assert hasattr(Tennis, "manufacturer")
    descriptor = None
    for klass in Tennis.__mro__:
        if "manufacturer" in klass.__dict__:
            descriptor = klass.__dict__["manufacturer"]
            break
    assert isinstance(descriptor, property)

def test_tennis_has_color():
    assert hasattr(Tennis, "color")
    descriptor = None
    for klass in Tennis.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_tennis_has_engine():
    assert hasattr(Tennis, "engine")
    descriptor = None
    for klass in Tennis.__mro__:
        if "engine" in klass.__dict__:
            descriptor = klass.__dict__["engine"]
            break
    assert isinstance(descriptor, property)



def test_car_is_not_abstract():
    assert not inspect.isabstract(Car)


def test_car_constructor_exists():
    assert callable(Car.__init__)


def test_car_constructor_args():
    sig = inspect.signature(Car.__init__)
    params = list(sig.parameters.keys())


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
Test_strategy = st.builds(
    Test,
)
TestStand_strategy = st.builds(
    TestStand,
    carToBeTested=
        st.none()
)
M6_strategy = st.builds(
    M6,
    manufacturer=
        safe_text,
    color=
        safe_text,
    engine=
        st.none()
)
Engine_strategy = st.builds(
    Engine,
    engineSpeed=
        st.integers(),
    efficiencyCoefficient=
        st.integers(),
    type=
        safe_text
)
Tennis_strategy = st.builds(
    Tennis,
    manufacturer=
        safe_text,
    color=
        safe_text,
    engine=
        st.none()
)
Car_strategy = st.builds(
    Car,
)

@given(instance=Test_strategy)
@settings(max_examples=50)
def test_test_instantiation(instance):
    assert isinstance(instance, Test)

@given(instance=TestStand_strategy)
@settings(max_examples=50)
def test_teststand_instantiation(instance):
    assert isinstance(instance, TestStand)



@given(instance=TestStand_strategy)
def test_teststand_carToBeTested_setter(instance):
    original = instance.carToBeTested
    instance.carToBeTested = original
    assert instance.carToBeTested == original

@given(instance=M6_strategy)
@settings(max_examples=50)
def test_m6_instantiation(instance):
    assert isinstance(instance, M6)



@given(instance=M6_strategy)
def test_m6_manufacturer_setter(instance):
    original = instance.manufacturer
    instance.manufacturer = original
    assert instance.manufacturer == original



@given(instance=M6_strategy)
def test_m6_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=M6_strategy)
def test_m6_engine_setter(instance):
    original = instance.engine
    instance.engine = original
    assert instance.engine == original

@given(instance=Engine_strategy)
@settings(max_examples=50)
def test_engine_instantiation(instance):
    assert isinstance(instance, Engine)



@given(instance=Engine_strategy)
def test_engine_engineSpeed_setter(instance):
    original = instance.engineSpeed
    instance.engineSpeed = original
    assert instance.engineSpeed == original



@given(instance=Engine_strategy)
def test_engine_efficiencyCoefficient_setter(instance):
    original = instance.efficiencyCoefficient
    instance.efficiencyCoefficient = original
    assert instance.efficiencyCoefficient == original



@given(instance=Engine_strategy)
def test_engine_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Tennis_strategy)
@settings(max_examples=50)
def test_tennis_instantiation(instance):
    assert isinstance(instance, Tennis)



@given(instance=Tennis_strategy)
def test_tennis_manufacturer_setter(instance):
    original = instance.manufacturer
    instance.manufacturer = original
    assert instance.manufacturer == original



@given(instance=Tennis_strategy)
def test_tennis_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=Tennis_strategy)
def test_tennis_engine_setter(instance):
    original = instance.engine
    instance.engine = original
    assert instance.engine == original

@given(instance=Car_strategy)
@settings(max_examples=50)
def test_car_instantiation(instance):
    assert isinstance(instance, Car)
