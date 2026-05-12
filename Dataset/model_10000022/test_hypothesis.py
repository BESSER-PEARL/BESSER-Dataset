import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BankAccount,
    Manufacturer,
    Wheel,
    Engine,
    Car1,
    Car,
    Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bankaccount_is_not_abstract():
    assert not inspect.isabstract(BankAccount)


def test_bankaccount_constructor_exists():
    assert callable(BankAccount.__init__)


def test_bankaccount_constructor_args():
    sig = inspect.signature(BankAccount.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "owner" in params, "Missing parameter 'owner'"

def test_bankaccount_has_balance():
    assert hasattr(BankAccount, "balance")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_bankaccount_has_owner():
    assert hasattr(BankAccount, "owner")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)



def test_manufacturer_is_not_abstract():
    assert not inspect.isabstract(Manufacturer)


def test_manufacturer_constructor_exists():
    assert callable(Manufacturer.__init__)


def test_manufacturer_constructor_args():
    sig = inspect.signature(Manufacturer.__init__)
    params = list(sig.parameters.keys())
    assert "brand" in params, "Missing parameter 'brand'"
    assert "location" in params, "Missing parameter 'location'"

def test_manufacturer_has_brand():
    assert hasattr(Manufacturer, "brand")
    descriptor = None
    for klass in Manufacturer.__mro__:
        if "brand" in klass.__dict__:
            descriptor = klass.__dict__["brand"]
            break
    assert isinstance(descriptor, property)

def test_manufacturer_has_location():
    assert hasattr(Manufacturer, "location")
    descriptor = None
    for klass in Manufacturer.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_wheel_is_not_abstract():
    assert not inspect.isabstract(Wheel)


def test_wheel_constructor_exists():
    assert callable(Wheel.__init__)


def test_wheel_constructor_args():
    sig = inspect.signature(Wheel.__init__)
    params = list(sig.parameters.keys())
    assert "manufacturer" in params, "Missing parameter 'manufacturer'"
    assert "diameter" in params, "Missing parameter 'diameter'"
    assert "width" in params, "Missing parameter 'width'"

def test_wheel_has_manufacturer():
    assert hasattr(Wheel, "manufacturer")
    descriptor = None
    for klass in Wheel.__mro__:
        if "manufacturer" in klass.__dict__:
            descriptor = klass.__dict__["manufacturer"]
            break
    assert isinstance(descriptor, property)

def test_wheel_has_diameter():
    assert hasattr(Wheel, "diameter")
    descriptor = None
    for klass in Wheel.__mro__:
        if "diameter" in klass.__dict__:
            descriptor = klass.__dict__["diameter"]
            break
    assert isinstance(descriptor, property)

def test_wheel_has_width():
    assert hasattr(Wheel, "width")
    descriptor = None
    for klass in Wheel.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_engine_is_not_abstract():
    assert not inspect.isabstract(Engine)


def test_engine_constructor_exists():
    assert callable(Engine.__init__)


def test_engine_constructor_args():
    sig = inspect.signature(Engine.__init__)
    params = list(sig.parameters.keys())
    assert "volume" in params, "Missing parameter 'volume'"
    assert "power" in params, "Missing parameter 'power'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "rpm" in params, "Missing parameter 'rpm'"
    assert "manufacturer" in params, "Missing parameter 'manufacturer'"

def test_engine_has_volume():
    assert hasattr(Engine, "volume")
    descriptor = None
    for klass in Engine.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_engine_has_power():
    assert hasattr(Engine, "power")
    descriptor = None
    for klass in Engine.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
            break
    assert isinstance(descriptor, property)

def test_engine_has_weight():
    assert hasattr(Engine, "weight")
    descriptor = None
    for klass in Engine.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_engine_has_rpm():
    assert hasattr(Engine, "rpm")
    descriptor = None
    for klass in Engine.__mro__:
        if "rpm" in klass.__dict__:
            descriptor = klass.__dict__["rpm"]
            break
    assert isinstance(descriptor, property)

def test_engine_has_manufacturer():
    assert hasattr(Engine, "manufacturer")
    descriptor = None
    for klass in Engine.__mro__:
        if "manufacturer" in klass.__dict__:
            descriptor = klass.__dict__["manufacturer"]
            break
    assert isinstance(descriptor, property)



def test_car1_is_not_abstract():
    assert not inspect.isabstract(Car1)


def test_car1_constructor_exists():
    assert callable(Car1.__init__)


def test_car1_constructor_args():
    sig = inspect.signature(Car1.__init__)
    params = list(sig.parameters.keys())
    assert "engine" in params, "Missing parameter 'engine'"
    assert "doors" in params, "Missing parameter 'doors'"
    assert "length" in params, "Missing parameter 'length'"
    assert "wheels" in params, "Missing parameter 'wheels'"
    assert "height" in params, "Missing parameter 'height'"
    assert "model" in params, "Missing parameter 'model'"
    assert "width" in params, "Missing parameter 'width'"

def test_car1_has_engine():
    assert hasattr(Car1, "engine")
    descriptor = None
    for klass in Car1.__mro__:
        if "engine" in klass.__dict__:
            descriptor = klass.__dict__["engine"]
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

def test_car1_has_length():
    assert hasattr(Car1, "length")
    descriptor = None
    for klass in Car1.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_car1_has_wheels():
    assert hasattr(Car1, "wheels")
    descriptor = None
    for klass in Car1.__mro__:
        if "wheels" in klass.__dict__:
            descriptor = klass.__dict__["wheels"]
            break
    assert isinstance(descriptor, property)

def test_car1_has_height():
    assert hasattr(Car1, "height")
    descriptor = None
    for klass in Car1.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_car1_has_model():
    assert hasattr(Car1, "model")
    descriptor = None
    for klass in Car1.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_car1_has_width():
    assert hasattr(Car1, "width")
    descriptor = None
    for klass in Car1.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_car_is_not_abstract():
    assert not inspect.isabstract(Car)


def test_car_constructor_exists():
    assert callable(Car.__init__)


def test_car_constructor_args():
    sig = inspect.signature(Car.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "wheels" in params, "Missing parameter 'wheels'"
    assert "model" in params, "Missing parameter 'model'"
    assert "width" in params, "Missing parameter 'width'"
    assert "engine" in params, "Missing parameter 'engine'"
    assert "height" in params, "Missing parameter 'height'"
    assert "doors" in params, "Missing parameter 'doors'"

def test_car_has_length():
    assert hasattr(Car, "length")
    descriptor = None
    for klass in Car.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
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

def test_car_has_model():
    assert hasattr(Car, "model")
    descriptor = None
    for klass in Car.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
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

def test_car_has_engine():
    assert hasattr(Car, "engine")
    descriptor = None
    for klass in Car.__mro__:
        if "engine" in klass.__dict__:
            descriptor = klass.__dict__["engine"]
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

def test_car_has_doors():
    assert hasattr(Car, "doors")
    descriptor = None
    for klass in Car.__mro__:
        if "doors" in klass.__dict__:
            descriptor = klass.__dict__["doors"]
            break
    assert isinstance(descriptor, property)



def test_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_book_constructor_exists():
    assert callable(Book.__init__)


def test_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())
    assert "autor" in params, "Missing parameter 'autor'"
    assert "realese_date" in params, "Missing parameter 'realese_date'"
    assert "name" in params, "Missing parameter 'name'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_book_has_autor():
    assert hasattr(Book, "autor")
    descriptor = None
    for klass in Book.__mro__:
        if "autor" in klass.__dict__:
            descriptor = klass.__dict__["autor"]
            break
    assert isinstance(descriptor, property)

def test_book_has_realese_date():
    assert hasattr(Book, "realese_date")
    descriptor = None
    for klass in Book.__mro__:
        if "realese_date" in klass.__dict__:
            descriptor = klass.__dict__["realese_date"]
            break
    assert isinstance(descriptor, property)

def test_book_has_name():
    assert hasattr(Book, "name")
    descriptor = None
    for klass in Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_book_has_pages():
    assert hasattr(Book, "pages")
    descriptor = None
    for klass in Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
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
BankAccount_strategy = st.builds(
    BankAccount,
    balance=
        safe_text,
    owner=
        safe_text
)
Manufacturer_strategy = st.builds(
    Manufacturer,
    brand=
        safe_text,
    location=
        safe_text
)
Wheel_strategy = st.builds(
    Wheel,
    manufacturer=
        st.none(),
    diameter=
        st.integers(),
    width=
        st.integers()
)
Engine_strategy = st.builds(
    Engine,
    volume=
        st.integers(),
    power=
        st.integers(),
    weight=
        st.integers(),
    rpm=
        st.integers(),
    manufacturer=
        safe_text
)
Car1_strategy = st.builds(
    Car1,
    engine=
        safe_text,
    doors=
        st.integers(),
    length=
        st.integers(),
    wheels=
        safe_text,
    height=
        st.integers(),
    model=
        safe_text,
    width=
        st.integers()
)
Car_strategy = st.builds(
    Car,
    length=
        st.integers(),
    wheels=
        safe_text,
    model=
        safe_text,
    width=
        st.integers(),
    engine=
        safe_text,
    height=
        st.integers(),
    doors=
        st.integers()
)
Book_strategy = st.builds(
    Book,
    autor=
        safe_text,
    realese_date=
        safe_text,
    name=
        safe_text,
    pages=
        st.integers()
)

@given(instance=BankAccount_strategy)
@settings(max_examples=50)
def test_bankaccount_instantiation(instance):
    assert isinstance(instance, BankAccount)



@given(instance=BankAccount_strategy)
def test_bankaccount_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=BankAccount_strategy)
def test_bankaccount_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original

@given(instance=Manufacturer_strategy)
@settings(max_examples=50)
def test_manufacturer_instantiation(instance):
    assert isinstance(instance, Manufacturer)



@given(instance=Manufacturer_strategy)
def test_manufacturer_brand_setter(instance):
    original = instance.brand
    instance.brand = original
    assert instance.brand == original



@given(instance=Manufacturer_strategy)
def test_manufacturer_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Wheel_strategy)
@settings(max_examples=50)
def test_wheel_instantiation(instance):
    assert isinstance(instance, Wheel)



@given(instance=Wheel_strategy)
def test_wheel_manufacturer_setter(instance):
    original = instance.manufacturer
    instance.manufacturer = original
    assert instance.manufacturer == original



@given(instance=Wheel_strategy)
def test_wheel_diameter_setter(instance):
    original = instance.diameter
    instance.diameter = original
    assert instance.diameter == original



@given(instance=Wheel_strategy)
def test_wheel_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=Engine_strategy)
@settings(max_examples=50)
def test_engine_instantiation(instance):
    assert isinstance(instance, Engine)



@given(instance=Engine_strategy)
def test_engine_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original



@given(instance=Engine_strategy)
def test_engine_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original



@given(instance=Engine_strategy)
def test_engine_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=Engine_strategy)
def test_engine_rpm_setter(instance):
    original = instance.rpm
    instance.rpm = original
    assert instance.rpm == original



@given(instance=Engine_strategy)
def test_engine_manufacturer_setter(instance):
    original = instance.manufacturer
    instance.manufacturer = original
    assert instance.manufacturer == original

@given(instance=Car1_strategy)
@settings(max_examples=50)
def test_car1_instantiation(instance):
    assert isinstance(instance, Car1)



@given(instance=Car1_strategy)
def test_car1_engine_setter(instance):
    original = instance.engine
    instance.engine = original
    assert instance.engine == original



@given(instance=Car1_strategy)
def test_car1_doors_setter(instance):
    original = instance.doors
    instance.doors = original
    assert instance.doors == original



@given(instance=Car1_strategy)
def test_car1_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=Car1_strategy)
def test_car1_wheels_setter(instance):
    original = instance.wheels
    instance.wheels = original
    assert instance.wheels == original



@given(instance=Car1_strategy)
def test_car1_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=Car1_strategy)
def test_car1_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=Car1_strategy)
def test_car1_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=Car_strategy)
@settings(max_examples=50)
def test_car_instantiation(instance):
    assert isinstance(instance, Car)



@given(instance=Car_strategy)
def test_car_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=Car_strategy)
def test_car_wheels_setter(instance):
    original = instance.wheels
    instance.wheels = original
    assert instance.wheels == original



@given(instance=Car_strategy)
def test_car_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=Car_strategy)
def test_car_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=Car_strategy)
def test_car_engine_setter(instance):
    original = instance.engine
    instance.engine = original
    assert instance.engine == original



@given(instance=Car_strategy)
def test_car_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=Car_strategy)
def test_car_doors_setter(instance):
    original = instance.doors
    instance.doors = original
    assert instance.doors == original

@given(instance=Book_strategy)
@settings(max_examples=50)
def test_book_instantiation(instance):
    assert isinstance(instance, Book)



@given(instance=Book_strategy)
def test_book_autor_setter(instance):
    original = instance.autor
    instance.autor = original
    assert instance.autor == original



@given(instance=Book_strategy)
def test_book_realese_date_setter(instance):
    original = instance.realese_date
    instance.realese_date = original
    assert instance.realese_date == original



@given(instance=Book_strategy)
def test_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Book_strategy)
def test_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original
