import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    b_Ebook,
    b_B,
    b_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_ebook_is_not_abstract():
    assert not inspect.isabstract(b_Ebook)


def test_b_ebook_constructor_exists():
    assert callable(b_Ebook.__init__)


def test_b_ebook_constructor_args():
    sig = inspect.signature(b_Ebook.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "label" in params, "Missing parameter 'label'"
    assert "category" in params, "Missing parameter 'category'"
    assert "info" in params, "Missing parameter 'info'"

def test_b_ebook_has_date():
    assert hasattr(b_Ebook, "date")
    descriptor = None
    for klass in b_Ebook.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_b_ebook_has_label():
    assert hasattr(b_Ebook, "label")
    descriptor = None
    for klass in b_Ebook.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_b_ebook_has_category():
    assert hasattr(b_Ebook, "category")
    descriptor = None
    for klass in b_Ebook.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_b_ebook_has_info():
    assert hasattr(b_Ebook, "info")
    descriptor = None
    for klass in b_Ebook.__mro__:
        if "info" in klass.__dict__:
            descriptor = klass.__dict__["info"]
            break
    assert isinstance(descriptor, property)



def test_b_b_is_not_abstract():
    assert not inspect.isabstract(b_B)


def test_b_b_constructor_exists():
    assert callable(b_B.__init__)


def test_b_b_constructor_args():
    sig = inspect.signature(b_B.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_b_b_has_id():
    assert hasattr(b_B, "id")
    descriptor = None
    for klass in b_B.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_b_model_is_not_abstract():
    assert not inspect.isabstract(b_Model)


def test_b_model_constructor_exists():
    assert callable(b_Model.__init__)


def test_b_model_constructor_args():
    sig = inspect.signature(b_Model.__init__)
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
b_Ebook_strategy = st.builds(
    b_Ebook,
    date=
        safe_text,
    label=
        safe_text,
    category=
        safe_text,
    info=
        safe_text
)
b_B_strategy = st.builds(
    b_B,
    id=
        safe_text
)
b_Model_strategy = st.builds(
    b_Model,
)

@given(instance=b_Ebook_strategy)
@settings(max_examples=50)
def test_b_ebook_instantiation(instance):
    assert isinstance(instance, b_Ebook)



@given(instance=b_Ebook_strategy)
def test_b_ebook_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=b_Ebook_strategy)
def test_b_ebook_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=b_Ebook_strategy)
def test_b_ebook_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=b_Ebook_strategy)
def test_b_ebook_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original

@given(instance=b_B_strategy)
@settings(max_examples=50)
def test_b_b_instantiation(instance):
    assert isinstance(instance, b_B)



@given(instance=b_B_strategy)
def test_b_b_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=b_Model_strategy)
@settings(max_examples=50)
def test_b_model_instantiation(instance):
    assert isinstance(instance, b_Model)
