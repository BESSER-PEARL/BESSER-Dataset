import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Map_Address,
    Map_Map,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_map_address_is_not_abstract():
    assert not inspect.isabstract(Map_Address)


def test_map_address_constructor_exists():
    assert callable(Map_Address.__init__)


def test_map_address_constructor_args():
    sig = inspect.signature(Map_Address.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pictures" in params, "Missing parameter 'pictures'"
    assert "description" in params, "Missing parameter 'description'"
    assert "downtown" in params, "Missing parameter 'downtown'"
    assert "telephone" in params, "Missing parameter 'telephone'"
    assert "latitude" in params, "Missing parameter 'latitude'"
    assert "longitude" in params, "Missing parameter 'longitude'"

def test_map_address_has_name():
    assert hasattr(Map_Address, "name")
    descriptor = None
    for klass in Map_Address.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_map_address_has_pictures():
    assert hasattr(Map_Address, "pictures")
    descriptor = None
    for klass in Map_Address.__mro__:
        if "pictures" in klass.__dict__:
            descriptor = klass.__dict__["pictures"]
            break
    assert isinstance(descriptor, property)

def test_map_address_has_description():
    assert hasattr(Map_Address, "description")
    descriptor = None
    for klass in Map_Address.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_map_address_has_downtown():
    assert hasattr(Map_Address, "downtown")
    descriptor = None
    for klass in Map_Address.__mro__:
        if "downtown" in klass.__dict__:
            descriptor = klass.__dict__["downtown"]
            break
    assert isinstance(descriptor, property)

def test_map_address_has_telephone():
    assert hasattr(Map_Address, "telephone")
    descriptor = None
    for klass in Map_Address.__mro__:
        if "telephone" in klass.__dict__:
            descriptor = klass.__dict__["telephone"]
            break
    assert isinstance(descriptor, property)

def test_map_address_has_latitude():
    assert hasattr(Map_Address, "latitude")
    descriptor = None
    for klass in Map_Address.__mro__:
        if "latitude" in klass.__dict__:
            descriptor = klass.__dict__["latitude"]
            break
    assert isinstance(descriptor, property)

def test_map_address_has_longitude():
    assert hasattr(Map_Address, "longitude")
    descriptor = None
    for klass in Map_Address.__mro__:
        if "longitude" in klass.__dict__:
            descriptor = klass.__dict__["longitude"]
            break
    assert isinstance(descriptor, property)



def test_map_map_is_not_abstract():
    assert not inspect.isabstract(Map_Map)


def test_map_map_constructor_exists():
    assert callable(Map_Map.__init__)


def test_map_map_constructor_args():
    sig = inspect.signature(Map_Map.__init__)
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
Map_Address_strategy = st.builds(
    Map_Address,
    name=
        safe_text,
    pictures=
        safe_text,
    description=
        safe_text,
    downtown=
        st.booleans(),
    telephone=
        safe_text,
    latitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    longitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Map_Map_strategy = st.builds(
    Map_Map,
)

@given(instance=Map_Address_strategy)
@settings(max_examples=50)
def test_map_address_instantiation(instance):
    assert isinstance(instance, Map_Address)



@given(instance=Map_Address_strategy)
def test_map_address_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Map_Address_strategy)
def test_map_address_pictures_setter(instance):
    original = instance.pictures
    instance.pictures = original
    assert instance.pictures == original



@given(instance=Map_Address_strategy)
def test_map_address_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Map_Address_strategy)
def test_map_address_downtown_setter(instance):
    original = instance.downtown
    instance.downtown = original
    assert instance.downtown == original



@given(instance=Map_Address_strategy)
def test_map_address_telephone_setter(instance):
    original = instance.telephone
    instance.telephone = original
    assert instance.telephone == original



@given(instance=Map_Address_strategy)
def test_map_address_latitude_setter(instance):
    original = instance.latitude
    instance.latitude = original
    assert instance.latitude == original



@given(instance=Map_Address_strategy)
def test_map_address_longitude_setter(instance):
    original = instance.longitude
    instance.longitude = original
    assert instance.longitude == original

@given(instance=Map_Map_strategy)
@settings(max_examples=50)
def test_map_map_instantiation(instance):
    assert isinstance(instance, Map_Map)
