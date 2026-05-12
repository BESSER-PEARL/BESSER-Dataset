import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    multiview_Named,
    Named,
    multiview_B,
    multiview_C,
    multiview_E,
    multiview_F,
    multiview_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_multiview_named_is_not_abstract():
    assert not inspect.isabstract(multiview_Named)


def test_multiview_named_constructor_exists():
    assert callable(multiview_Named.__init__)


def test_multiview_named_constructor_args():
    sig = inspect.signature(multiview_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_multiview_named_has_name():
    assert hasattr(multiview_Named, "name")
    descriptor = None
    for klass in multiview_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_multiview_b_is_not_abstract():
    assert not inspect.isabstract(multiview_B)


def test_multiview_b_constructor_exists():
    assert callable(multiview_B.__init__)


def test_multiview_b_constructor_args():
    sig = inspect.signature(multiview_B.__init__)
    params = list(sig.parameters.keys())



def test_multiview_c_is_not_abstract():
    assert not inspect.isabstract(multiview_C)


def test_multiview_c_constructor_exists():
    assert callable(multiview_C.__init__)


def test_multiview_c_constructor_args():
    sig = inspect.signature(multiview_C.__init__)
    params = list(sig.parameters.keys())



def test_multiview_e_is_not_abstract():
    assert not inspect.isabstract(multiview_E)


def test_multiview_e_constructor_exists():
    assert callable(multiview_E.__init__)


def test_multiview_e_constructor_args():
    sig = inspect.signature(multiview_E.__init__)
    params = list(sig.parameters.keys())



def test_multiview_f_is_not_abstract():
    assert not inspect.isabstract(multiview_F)


def test_multiview_f_constructor_exists():
    assert callable(multiview_F.__init__)


def test_multiview_f_constructor_args():
    sig = inspect.signature(multiview_F.__init__)
    params = list(sig.parameters.keys())



def test_multiview_a_is_not_abstract():
    assert not inspect.isabstract(multiview_A)


def test_multiview_a_constructor_exists():
    assert callable(multiview_A.__init__)


def test_multiview_a_constructor_args():
    sig = inspect.signature(multiview_A.__init__)
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
multiview_Named_strategy = st.builds(
    multiview_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
multiview_B_strategy = st.builds(
    multiview_B,
)
multiview_C_strategy = st.builds(
    multiview_C,
)
multiview_E_strategy = st.builds(
    multiview_E,
)
multiview_F_strategy = st.builds(
    multiview_F,
)
multiview_A_strategy = st.builds(
    multiview_A,
)

@given(instance=multiview_Named_strategy)
@settings(max_examples=50)
def test_multiview_named_instantiation(instance):
    assert isinstance(instance, multiview_Named)



@given(instance=multiview_Named_strategy)
def test_multiview_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=multiview_B_strategy)
@settings(max_examples=50)
def test_multiview_b_instantiation(instance):
    assert isinstance(instance, multiview_B)

@given(instance=multiview_C_strategy)
@settings(max_examples=50)
def test_multiview_c_instantiation(instance):
    assert isinstance(instance, multiview_C)

@given(instance=multiview_E_strategy)
@settings(max_examples=50)
def test_multiview_e_instantiation(instance):
    assert isinstance(instance, multiview_E)

@given(instance=multiview_F_strategy)
@settings(max_examples=50)
def test_multiview_f_instantiation(instance):
    assert isinstance(instance, multiview_F)

@given(instance=multiview_A_strategy)
@settings(max_examples=50)
def test_multiview_a_instantiation(instance):
    assert isinstance(instance, multiview_A)
