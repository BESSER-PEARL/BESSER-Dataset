import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    data::Variable,
    data::Variables,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data::variable_is_not_abstract():
    assert not inspect.isabstract(data::Variable)


def test_data::variable_constructor_exists():
    assert callable(data::Variable.__init__)


def test_data::variable_constructor_args():
    sig = inspect.signature(data::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_data::variable_has_id():
    assert hasattr(data::Variable, "id")
    descriptor = None
    for klass in data::Variable.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_data::variables_is_not_abstract():
    assert not inspect.isabstract(data::Variables)


def test_data::variables_constructor_exists():
    assert callable(data::Variables.__init__)


def test_data::variables_constructor_args():
    sig = inspect.signature(data::Variables.__init__)
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
data::Variable_strategy = st.builds(
    data::Variable,
    id=
        safe_text
)
data::Variables_strategy = st.builds(
    data::Variables,
)

@given(instance=data::Variable_strategy)
@settings(max_examples=50)
def test_data::variable_instantiation(instance):
    assert isinstance(instance, data::Variable)

@given(instance=data::Variable_strategy)
def test_data::variable_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=data::Variable_strategy)
def test_data::variable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=data::Variables_strategy)
@settings(max_examples=50)
def test_data::variables_instantiation(instance):
    assert isinstance(instance, data::Variables)
