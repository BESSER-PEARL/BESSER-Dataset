import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    data_Variable,
    data_Variables,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data_variable_is_not_abstract():
    assert not inspect.isabstract(data_Variable)


def test_data_variable_constructor_exists():
    assert callable(data_Variable.__init__)


def test_data_variable_constructor_args():
    sig = inspect.signature(data_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_data_variable_has_id():
    assert hasattr(data_Variable, "id")
    descriptor = None
    for klass in data_Variable.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_data_variables_is_not_abstract():
    assert not inspect.isabstract(data_Variables)


def test_data_variables_constructor_exists():
    assert callable(data_Variables.__init__)


def test_data_variables_constructor_args():
    sig = inspect.signature(data_Variables.__init__)
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
data_Variable_strategy = st.builds(
    data_Variable,
    id=
        safe_text
)
data_Variables_strategy = st.builds(
    data_Variables,
)

@given(instance=data_Variable_strategy)
@settings(max_examples=50)
def test_data_variable_instantiation(instance):
    assert isinstance(instance, data_Variable)



@given(instance=data_Variable_strategy)
def test_data_variable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=data_Variables_strategy)
@settings(max_examples=50)
def test_data_variables_instantiation(instance):
    assert isinstance(instance, data_Variables)
