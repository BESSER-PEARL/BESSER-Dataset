import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Map::Address,
    Map::Map,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_map::address_is_not_abstract():
    assert not inspect.isabstract(Map::Address)


def test_map::address_constructor_exists():
    assert callable(Map::Address.__init__)


def test_map::address_constructor_args():
    sig = inspect.signature(Map::Address.__init__)
    params = list(sig.parameters.keys())
    assert "telephone" in params, "Missing parameter 'telephone'"
    assert "longitude" in params, "Missing parameter 'longitude'"
    assert "pictures" in params, "Missing parameter 'pictures'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "latitude" in params, "Missing parameter 'latitude'"
    assert "downtown" in params, "Missing parameter 'downtown'"

def test_map::address_has_telephone():
    assert hasattr(Map::Address, "telephone")
    descriptor = None
    for klass in Map::Address.__mro__:
        if "telephone" in klass.__dict__:
            descriptor = klass.__dict__["telephone"]
            break
    assert isinstance(descriptor, property)

def test_map::address_has_longitude():
    assert hasattr(Map::Address, "longitude")
    descriptor = None
    for klass in Map::Address.__mro__:
        if "longitude" in klass.__dict__:
            descriptor = klass.__dict__["longitude"]
            break
    assert isinstance(descriptor, property)

def test_map::address_has_pictures():
    assert hasattr(Map::Address, "pictures")
    descriptor = None
    for klass in Map::Address.__mro__:
        if "pictures" in klass.__dict__:
            descriptor = klass.__dict__["pictures"]
            break
    assert isinstance(descriptor, property)

def test_map::address_has_name():
    assert hasattr(Map::Address, "name")
    descriptor = None
    for klass in Map::Address.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_map::address_has_description():
    assert hasattr(Map::Address, "description")
    descriptor = None
    for klass in Map::Address.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_map::address_has_latitude():
    assert hasattr(Map::Address, "latitude")
    descriptor = None
    for klass in Map::Address.__mro__:
        if "latitude" in klass.__dict__:
            descriptor = klass.__dict__["latitude"]
            break
    assert isinstance(descriptor, property)

def test_map::address_has_downtown():
    assert hasattr(Map::Address, "downtown")
    descriptor = None
    for klass in Map::Address.__mro__:
        if "downtown" in klass.__dict__:
            descriptor = klass.__dict__["downtown"]
            break
    assert isinstance(descriptor, property)



def test_map::map_is_not_abstract():
    assert not inspect.isabstract(Map::Map)


def test_map::map_constructor_exists():
    assert callable(Map::Map.__init__)


def test_map::map_constructor_args():
    sig = inspect.signature(Map::Map.__init__)
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
Map::Address_strategy = st.builds(
    Map::Address,
    telephone=
        safe_text,
    longitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    pictures=
        safe_text,
    name=
        safe_text,
    description=
        safe_text,
    latitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    downtown=
        st.booleans()
)
Map::Map_strategy = st.builds(
    Map::Map,
)

@given(instance=Map::Address_strategy)
@settings(max_examples=50)
def test_map::address_instantiation(instance):
    assert isinstance(instance, Map::Address)

@given(instance=Map::Address_strategy)
def test_map::address_telephone_type(instance):
    assert isinstance(instance.telephone, str)


@given(instance=Map::Address_strategy)
def test_map::address_telephone_setter(instance):
    original = instance.telephone
    instance.telephone = original
    assert instance.telephone == original

@given(instance=Map::Address_strategy)
def test_map::address_longitude_type(instance):
    assert isinstance(instance.longitude, float)


@given(instance=Map::Address_strategy)
def test_map::address_longitude_setter(instance):
    original = instance.longitude
    instance.longitude = original
    assert instance.longitude == original

@given(instance=Map::Address_strategy)
def test_map::address_pictures_type(instance):
    assert isinstance(instance.pictures, str)


@given(instance=Map::Address_strategy)
def test_map::address_pictures_setter(instance):
    original = instance.pictures
    instance.pictures = original
    assert instance.pictures == original

@given(instance=Map::Address_strategy)
def test_map::address_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Map::Address_strategy)
def test_map::address_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Map::Address_strategy)
def test_map::address_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=Map::Address_strategy)
def test_map::address_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Map::Address_strategy)
def test_map::address_latitude_type(instance):
    assert isinstance(instance.latitude, float)


@given(instance=Map::Address_strategy)
def test_map::address_latitude_setter(instance):
    original = instance.latitude
    instance.latitude = original
    assert instance.latitude == original

@given(instance=Map::Address_strategy)
def test_map::address_downtown_type(instance):
    assert isinstance(instance.downtown, bool)


@given(instance=Map::Address_strategy)
def test_map::address_downtown_setter(instance):
    original = instance.downtown
    instance.downtown = original
    assert instance.downtown == original

@given(instance=Map::Map_strategy)
@settings(max_examples=50)
def test_map::map_instantiation(instance):
    assert isinstance(instance, Map::Map)
