import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Data_Attribut,
    Data_Classe,
    Data_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data_attribut_is_not_abstract():
    assert not inspect.isabstract(Data_Attribut)


def test_data_attribut_constructor_exists():
    assert callable(Data_Attribut.__init__)


def test_data_attribut_constructor_args():
    sig = inspect.signature(Data_Attribut.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_data_attribut_has_name():
    assert hasattr(Data_Attribut, "name")
    descriptor = None
    for klass in Data_Attribut.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_data_attribut_has_type():
    assert hasattr(Data_Attribut, "type")
    descriptor = None
    for klass in Data_Attribut.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_data_classe_is_not_abstract():
    assert not inspect.isabstract(Data_Classe)


def test_data_classe_constructor_exists():
    assert callable(Data_Classe.__init__)


def test_data_classe_constructor_args():
    sig = inspect.signature(Data_Classe.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_data_classe_has_name():
    assert hasattr(Data_Classe, "name")
    descriptor = None
    for klass in Data_Classe.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_data_model_is_not_abstract():
    assert not inspect.isabstract(Data_Model)


def test_data_model_constructor_exists():
    assert callable(Data_Model.__init__)


def test_data_model_constructor_args():
    sig = inspect.signature(Data_Model.__init__)
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
Data_Attribut_strategy = st.builds(
    Data_Attribut,
    name=
        safe_text,
    type=
        safe_text
)
Data_Classe_strategy = st.builds(
    Data_Classe,
    name=
        safe_text
)
Data_Model_strategy = st.builds(
    Data_Model,
)

@given(instance=Data_Attribut_strategy)
@settings(max_examples=50)
def test_data_attribut_instantiation(instance):
    assert isinstance(instance, Data_Attribut)



@given(instance=Data_Attribut_strategy)
def test_data_attribut_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Data_Attribut_strategy)
def test_data_attribut_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Data_Classe_strategy)
@settings(max_examples=50)
def test_data_classe_instantiation(instance):
    assert isinstance(instance, Data_Classe)



@given(instance=Data_Classe_strategy)
def test_data_classe_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data_Model_strategy)
@settings(max_examples=50)
def test_data_model_instantiation(instance):
    assert isinstance(instance, Data_Model)
