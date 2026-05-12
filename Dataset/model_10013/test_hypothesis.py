import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PublicSpace,
    maps::Square,
    maps::Garden,
    Road,
    maps::Boulevard,
    maps::Pedestrian,
    maps::Street,
    maps::Road,
    maps::map,
    maps::PublicSpace,
    cards,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_publicspace_is_not_abstract():
    assert not inspect.isabstract(PublicSpace)


def test_publicspace_constructor_exists():
    assert callable(PublicSpace.__init__)


def test_publicspace_constructor_args():
    sig = inspect.signature(PublicSpace.__init__)
    params = list(sig.parameters.keys())



def test_maps::square_is_not_abstract():
    assert not inspect.isabstract(maps::Square)


def test_maps::square_constructor_exists():
    assert callable(maps::Square.__init__)


def test_maps::square_constructor_args():
    sig = inspect.signature(maps::Square.__init__)
    params = list(sig.parameters.keys())



def test_maps::garden_is_not_abstract():
    assert not inspect.isabstract(maps::Garden)


def test_maps::garden_constructor_exists():
    assert callable(maps::Garden.__init__)


def test_maps::garden_constructor_args():
    sig = inspect.signature(maps::Garden.__init__)
    params = list(sig.parameters.keys())



def test_road_is_not_abstract():
    assert not inspect.isabstract(Road)


def test_road_constructor_exists():
    assert callable(Road.__init__)


def test_road_constructor_args():
    sig = inspect.signature(Road.__init__)
    params = list(sig.parameters.keys())



def test_maps::boulevard_is_not_abstract():
    assert not inspect.isabstract(maps::Boulevard)


def test_maps::boulevard_constructor_exists():
    assert callable(maps::Boulevard.__init__)


def test_maps::boulevard_constructor_args():
    sig = inspect.signature(maps::Boulevard.__init__)
    params = list(sig.parameters.keys())



def test_maps::pedestrian_is_not_abstract():
    assert not inspect.isabstract(maps::Pedestrian)


def test_maps::pedestrian_constructor_exists():
    assert callable(maps::Pedestrian.__init__)


def test_maps::pedestrian_constructor_args():
    sig = inspect.signature(maps::Pedestrian.__init__)
    params = list(sig.parameters.keys())



def test_maps::street_is_not_abstract():
    assert not inspect.isabstract(maps::Street)


def test_maps::street_constructor_exists():
    assert callable(maps::Street.__init__)


def test_maps::street_constructor_args():
    sig = inspect.signature(maps::Street.__init__)
    params = list(sig.parameters.keys())



def test_maps::road_is_not_abstract():
    assert not inspect.isabstract(maps::Road)


def test_maps::road_constructor_exists():
    assert callable(maps::Road.__init__)


def test_maps::road_constructor_args():
    sig = inspect.signature(maps::Road.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "name" in params, "Missing parameter 'name'"
    assert "district" in params, "Missing parameter 'district'"

def test_maps::road_has_length():
    assert hasattr(maps::Road, "length")
    descriptor = None
    for klass in maps::Road.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_maps::road_has_name():
    assert hasattr(maps::Road, "name")
    descriptor = None
    for klass in maps::Road.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_maps::road_has_district():
    assert hasattr(maps::Road, "district")
    descriptor = None
    for klass in maps::Road.__mro__:
        if "district" in klass.__dict__:
            descriptor = klass.__dict__["district"]
            break
    assert isinstance(descriptor, property)



def test_maps::map_is_not_abstract():
    assert not inspect.isabstract(maps::map)


def test_maps::map_constructor_exists():
    assert callable(maps::map.__init__)


def test_maps::map_constructor_args():
    sig = inspect.signature(maps::map.__init__)
    params = list(sig.parameters.keys())
    assert "isCity" in params, "Missing parameter 'isCity'"
    assert "country" in params, "Missing parameter 'country'"
    assert "size" in params, "Missing parameter 'size'"
    assert "name" in params, "Missing parameter 'name'"

def test_maps::map_has_isCity():
    assert hasattr(maps::map, "isCity")
    descriptor = None
    for klass in maps::map.__mro__:
        if "isCity" in klass.__dict__:
            descriptor = klass.__dict__["isCity"]
            break
    assert isinstance(descriptor, property)

def test_maps::map_has_country():
    assert hasattr(maps::map, "country")
    descriptor = None
    for klass in maps::map.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_maps::map_has_size():
    assert hasattr(maps::map, "size")
    descriptor = None
    for klass in maps::map.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_maps::map_has_name():
    assert hasattr(maps::map, "name")
    descriptor = None
    for klass in maps::map.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_maps::publicspace_is_not_abstract():
    assert not inspect.isabstract(maps::PublicSpace)


def test_maps::publicspace_constructor_exists():
    assert callable(maps::PublicSpace.__init__)


def test_maps::publicspace_constructor_args():
    sig = inspect.signature(maps::PublicSpace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_maps::publicspace_has_name():
    assert hasattr(maps::PublicSpace, "name")
    descriptor = None
    for klass in maps::PublicSpace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cards_exists():
    # Check that the Enumeration exists
    assert cards is not None

def test_cards_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in cards]
    expected_literals = [
        "big",
        "medium",
        "small",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in cards"


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
PublicSpace_strategy = st.builds(
    PublicSpace,
)
maps::Square_strategy = st.builds(
    maps::Square,
)
maps::Garden_strategy = st.builds(
    maps::Garden,
)
Road_strategy = st.builds(
    Road,
)
maps::Boulevard_strategy = st.builds(
    maps::Boulevard,
)
maps::Pedestrian_strategy = st.builds(
    maps::Pedestrian,
)
maps::Street_strategy = st.builds(
    maps::Street,
)
maps::Road_strategy = st.builds(
    maps::Road,
    length=
        st.integers(),
    name=
        safe_text,
    district=
        safe_text
)
maps::map_strategy = st.builds(
    maps::map,
    isCity=
        st.booleans(),
    country=
        safe_text,
    size=
        safe_text,
    name=
        safe_text
)
maps::PublicSpace_strategy = st.builds(
    maps::PublicSpace,
    name=
        safe_text
)

@given(instance=PublicSpace_strategy)
@settings(max_examples=50)
def test_publicspace_instantiation(instance):
    assert isinstance(instance, PublicSpace)

@given(instance=maps::Square_strategy)
@settings(max_examples=50)
def test_maps::square_instantiation(instance):
    assert isinstance(instance, maps::Square)

@given(instance=maps::Garden_strategy)
@settings(max_examples=50)
def test_maps::garden_instantiation(instance):
    assert isinstance(instance, maps::Garden)

@given(instance=Road_strategy)
@settings(max_examples=50)
def test_road_instantiation(instance):
    assert isinstance(instance, Road)

@given(instance=maps::Boulevard_strategy)
@settings(max_examples=50)
def test_maps::boulevard_instantiation(instance):
    assert isinstance(instance, maps::Boulevard)

@given(instance=maps::Pedestrian_strategy)
@settings(max_examples=50)
def test_maps::pedestrian_instantiation(instance):
    assert isinstance(instance, maps::Pedestrian)

@given(instance=maps::Street_strategy)
@settings(max_examples=50)
def test_maps::street_instantiation(instance):
    assert isinstance(instance, maps::Street)

@given(instance=maps::Road_strategy)
@settings(max_examples=50)
def test_maps::road_instantiation(instance):
    assert isinstance(instance, maps::Road)

@given(instance=maps::Road_strategy)
def test_maps::road_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=maps::Road_strategy)
def test_maps::road_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=maps::Road_strategy)
def test_maps::road_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=maps::Road_strategy)
def test_maps::road_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=maps::Road_strategy)
def test_maps::road_district_type(instance):
    assert isinstance(instance.district, str)


@given(instance=maps::Road_strategy)
def test_maps::road_district_setter(instance):
    original = instance.district
    instance.district = original
    assert instance.district == original

@given(instance=maps::map_strategy)
@settings(max_examples=50)
def test_maps::map_instantiation(instance):
    assert isinstance(instance, maps::map)

@given(instance=maps::map_strategy)
def test_maps::map_isCity_type(instance):
    assert isinstance(instance.isCity, bool)


@given(instance=maps::map_strategy)
def test_maps::map_isCity_setter(instance):
    original = instance.isCity
    instance.isCity = original
    assert instance.isCity == original

@given(instance=maps::map_strategy)
def test_maps::map_country_type(instance):
    assert isinstance(instance.country, str)


@given(instance=maps::map_strategy)
def test_maps::map_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original

@given(instance=maps::map_strategy)
def test_maps::map_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=maps::map_strategy)
def test_maps::map_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=maps::map_strategy)
def test_maps::map_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=maps::map_strategy)
def test_maps::map_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=maps::PublicSpace_strategy)
@settings(max_examples=50)
def test_maps::publicspace_instantiation(instance):
    assert isinstance(instance, maps::PublicSpace)

@given(instance=maps::PublicSpace_strategy)
def test_maps::publicspace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=maps::PublicSpace_strategy)
def test_maps::publicspace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
