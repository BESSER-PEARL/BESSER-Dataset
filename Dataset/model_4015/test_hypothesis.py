import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Data::Attribut,
    Data::Classe,
    Data::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data::attribut_is_not_abstract():
    assert not inspect.isabstract(Data::Attribut)


def test_data::attribut_constructor_exists():
    assert callable(Data::Attribut.__init__)


def test_data::attribut_constructor_args():
    sig = inspect.signature(Data::Attribut.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_data::attribut_has_name():
    assert hasattr(Data::Attribut, "name")
    descriptor = None
    for klass in Data::Attribut.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_data::attribut_has_type():
    assert hasattr(Data::Attribut, "type")
    descriptor = None
    for klass in Data::Attribut.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_data::classe_is_not_abstract():
    assert not inspect.isabstract(Data::Classe)


def test_data::classe_constructor_exists():
    assert callable(Data::Classe.__init__)


def test_data::classe_constructor_args():
    sig = inspect.signature(Data::Classe.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_data::classe_has_name():
    assert hasattr(Data::Classe, "name")
    descriptor = None
    for klass in Data::Classe.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_data::model_is_not_abstract():
    assert not inspect.isabstract(Data::Model)


def test_data::model_constructor_exists():
    assert callable(Data::Model.__init__)


def test_data::model_constructor_args():
    sig = inspect.signature(Data::Model.__init__)
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
Data::Attribut_strategy = st.builds(
    Data::Attribut,
    name=
        safe_text,
    type=
        safe_text
)
Data::Classe_strategy = st.builds(
    Data::Classe,
    name=
        safe_text
)
Data::Model_strategy = st.builds(
    Data::Model,
)

@given(instance=Data::Attribut_strategy)
@settings(max_examples=50)
def test_data::attribut_instantiation(instance):
    assert isinstance(instance, Data::Attribut)

@given(instance=Data::Attribut_strategy)
def test_data::attribut_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Attribut_strategy)
def test_data::attribut_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data::Attribut_strategy)
def test_data::attribut_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Data::Attribut_strategy)
def test_data::attribut_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Data::Classe_strategy)
@settings(max_examples=50)
def test_data::classe_instantiation(instance):
    assert isinstance(instance, Data::Classe)

@given(instance=Data::Classe_strategy)
def test_data::classe_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Classe_strategy)
def test_data::classe_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data::Model_strategy)
@settings(max_examples=50)
def test_data::model_instantiation(instance):
    assert isinstance(instance, Data::Model)
