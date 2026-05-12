import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PublicSpace,
    maps_Square,
    maps_Garden,
    Road,
    maps_Pedestrian,
    maps_Boulevard,
    maps_Street,
    maps_Road,
    maps_map,
    maps_PublicSpace,
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



def test_maps_square_is_not_abstract():
    assert not inspect.isabstract(maps_Square)


def test_maps_square_constructor_exists():
    assert callable(maps_Square.__init__)


def test_maps_square_constructor_args():
    sig = inspect.signature(maps_Square.__init__)
    params = list(sig.parameters.keys())



def test_maps_garden_is_not_abstract():
    assert not inspect.isabstract(maps_Garden)


def test_maps_garden_constructor_exists():
    assert callable(maps_Garden.__init__)


def test_maps_garden_constructor_args():
    sig = inspect.signature(maps_Garden.__init__)
    params = list(sig.parameters.keys())



def test_road_is_not_abstract():
    assert not inspect.isabstract(Road)


def test_road_constructor_exists():
    assert callable(Road.__init__)


def test_road_constructor_args():
    sig = inspect.signature(Road.__init__)
    params = list(sig.parameters.keys())



def test_maps_pedestrian_is_not_abstract():
    assert not inspect.isabstract(maps_Pedestrian)


def test_maps_pedestrian_constructor_exists():
    assert callable(maps_Pedestrian.__init__)


def test_maps_pedestrian_constructor_args():
    sig = inspect.signature(maps_Pedestrian.__init__)
    params = list(sig.parameters.keys())



def test_maps_boulevard_is_not_abstract():
    assert not inspect.isabstract(maps_Boulevard)


def test_maps_boulevard_constructor_exists():
    assert callable(maps_Boulevard.__init__)


def test_maps_boulevard_constructor_args():
    sig = inspect.signature(maps_Boulevard.__init__)
    params = list(sig.parameters.keys())



def test_maps_street_is_not_abstract():
    assert not inspect.isabstract(maps_Street)


def test_maps_street_constructor_exists():
    assert callable(maps_Street.__init__)


def test_maps_street_constructor_args():
    sig = inspect.signature(maps_Street.__init__)
    params = list(sig.parameters.keys())



def test_maps_road_is_not_abstract():
    assert not inspect.isabstract(maps_Road)


def test_maps_road_constructor_exists():
    assert callable(maps_Road.__init__)


def test_maps_road_constructor_args():
    sig = inspect.signature(maps_Road.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "district" in params, "Missing parameter 'district'"
    assert "name" in params, "Missing parameter 'name'"

def test_maps_road_has_length():
    assert hasattr(maps_Road, "length")
    descriptor = None
    for klass in maps_Road.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_maps_road_has_district():
    assert hasattr(maps_Road, "district")
    descriptor = None
    for klass in maps_Road.__mro__:
        if "district" in klass.__dict__:
            descriptor = klass.__dict__["district"]
            break
    assert isinstance(descriptor, property)

def test_maps_road_has_name():
    assert hasattr(maps_Road, "name")
    descriptor = None
    for klass in maps_Road.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_maps_map_is_not_abstract():
    assert not inspect.isabstract(maps_map)


def test_maps_map_constructor_exists():
    assert callable(maps_map.__init__)


def test_maps_map_constructor_args():
    sig = inspect.signature(maps_map.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "size" in params, "Missing parameter 'size'"
    assert "country" in params, "Missing parameter 'country'"
    assert "isCity" in params, "Missing parameter 'isCity'"

def test_maps_map_has_name():
    assert hasattr(maps_map, "name")
    descriptor = None
    for klass in maps_map.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_maps_map_has_size():
    assert hasattr(maps_map, "size")
    descriptor = None
    for klass in maps_map.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_maps_map_has_country():
    assert hasattr(maps_map, "country")
    descriptor = None
    for klass in maps_map.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_maps_map_has_isCity():
    assert hasattr(maps_map, "isCity")
    descriptor = None
    for klass in maps_map.__mro__:
        if "isCity" in klass.__dict__:
            descriptor = klass.__dict__["isCity"]
            break
    assert isinstance(descriptor, property)



def test_maps_publicspace_is_not_abstract():
    assert not inspect.isabstract(maps_PublicSpace)


def test_maps_publicspace_constructor_exists():
    assert callable(maps_PublicSpace.__init__)


def test_maps_publicspace_constructor_args():
    sig = inspect.signature(maps_PublicSpace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_maps_publicspace_has_name():
    assert hasattr(maps_PublicSpace, "name")
    descriptor = None
    for klass in maps_PublicSpace.__mro__:
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
        "small",
        "medium",
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
maps_Square_strategy = st.builds(
    maps_Square,
)
maps_Garden_strategy = st.builds(
    maps_Garden,
)
Road_strategy = st.builds(
    Road,
)
maps_Pedestrian_strategy = st.builds(
    maps_Pedestrian,
)
maps_Boulevard_strategy = st.builds(
    maps_Boulevard,
)
maps_Street_strategy = st.builds(
    maps_Street,
)
maps_Road_strategy = st.builds(
    maps_Road,
    length=
        st.integers(),
    district=
        safe_text,
    name=
        safe_text
)
maps_map_strategy = st.builds(
    maps_map,
    name=
        safe_text,
    size=
        safe_text,
    country=
        safe_text,
    isCity=
        st.booleans()
)
maps_PublicSpace_strategy = st.builds(
    maps_PublicSpace,
    name=
        safe_text
)

@given(instance=PublicSpace_strategy)
@settings(max_examples=50)
def test_publicspace_instantiation(instance):
    assert isinstance(instance, PublicSpace)

@given(instance=maps_Square_strategy)
@settings(max_examples=50)
def test_maps_square_instantiation(instance):
    assert isinstance(instance, maps_Square)

@given(instance=maps_Garden_strategy)
@settings(max_examples=50)
def test_maps_garden_instantiation(instance):
    assert isinstance(instance, maps_Garden)

@given(instance=Road_strategy)
@settings(max_examples=50)
def test_road_instantiation(instance):
    assert isinstance(instance, Road)

@given(instance=maps_Pedestrian_strategy)
@settings(max_examples=50)
def test_maps_pedestrian_instantiation(instance):
    assert isinstance(instance, maps_Pedestrian)

@given(instance=maps_Boulevard_strategy)
@settings(max_examples=50)
def test_maps_boulevard_instantiation(instance):
    assert isinstance(instance, maps_Boulevard)

@given(instance=maps_Street_strategy)
@settings(max_examples=50)
def test_maps_street_instantiation(instance):
    assert isinstance(instance, maps_Street)

@given(instance=maps_Road_strategy)
@settings(max_examples=50)
def test_maps_road_instantiation(instance):
    assert isinstance(instance, maps_Road)



@given(instance=maps_Road_strategy)
def test_maps_road_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=maps_Road_strategy)
def test_maps_road_district_setter(instance):
    original = instance.district
    instance.district = original
    assert instance.district == original



@given(instance=maps_Road_strategy)
def test_maps_road_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=maps_map_strategy)
@settings(max_examples=50)
def test_maps_map_instantiation(instance):
    assert isinstance(instance, maps_map)



@given(instance=maps_map_strategy)
def test_maps_map_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=maps_map_strategy)
def test_maps_map_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=maps_map_strategy)
def test_maps_map_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=maps_map_strategy)
def test_maps_map_isCity_setter(instance):
    original = instance.isCity
    instance.isCity = original
    assert instance.isCity == original

@given(instance=maps_PublicSpace_strategy)
@settings(max_examples=50)
def test_maps_publicspace_instantiation(instance):
    assert isinstance(instance, maps_PublicSpace)



@given(instance=maps_PublicSpace_strategy)
def test_maps_publicspace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
