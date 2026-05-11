import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    b::Ebook,
    b::B,
    b::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b::ebook_is_not_abstract():
    assert not inspect.isabstract(b::Ebook)


def test_b::ebook_constructor_exists():
    assert callable(b::Ebook.__init__)


def test_b::ebook_constructor_args():
    sig = inspect.signature(b::Ebook.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "category" in params, "Missing parameter 'category'"
    assert "date" in params, "Missing parameter 'date'"
    assert "info" in params, "Missing parameter 'info'"

def test_b::ebook_has_label():
    assert hasattr(b::Ebook, "label")
    descriptor = None
    for klass in b::Ebook.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_b::ebook_has_category():
    assert hasattr(b::Ebook, "category")
    descriptor = None
    for klass in b::Ebook.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_b::ebook_has_date():
    assert hasattr(b::Ebook, "date")
    descriptor = None
    for klass in b::Ebook.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_b::ebook_has_info():
    assert hasattr(b::Ebook, "info")
    descriptor = None
    for klass in b::Ebook.__mro__:
        if "info" in klass.__dict__:
            descriptor = klass.__dict__["info"]
            break
    assert isinstance(descriptor, property)



def test_b::b_is_not_abstract():
    assert not inspect.isabstract(b::B)


def test_b::b_constructor_exists():
    assert callable(b::B.__init__)


def test_b::b_constructor_args():
    sig = inspect.signature(b::B.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_b::b_has_id():
    assert hasattr(b::B, "id")
    descriptor = None
    for klass in b::B.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_b::model_is_not_abstract():
    assert not inspect.isabstract(b::Model)


def test_b::model_constructor_exists():
    assert callable(b::Model.__init__)


def test_b::model_constructor_args():
    sig = inspect.signature(b::Model.__init__)
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
b::Ebook_strategy = st.builds(
    b::Ebook,
    label=
        safe_text,
    category=
        safe_text,
    date=
        safe_text,
    info=
        safe_text
)
b::B_strategy = st.builds(
    b::B,
    id=
        safe_text
)
b::Model_strategy = st.builds(
    b::Model,
)

@given(instance=b::Ebook_strategy)
@settings(max_examples=50)
def test_b::ebook_instantiation(instance):
    assert isinstance(instance, b::Ebook)

@given(instance=b::Ebook_strategy)
def test_b::ebook_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=b::Ebook_strategy)
def test_b::ebook_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=b::Ebook_strategy)
def test_b::ebook_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=b::Ebook_strategy)
def test_b::ebook_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=b::Ebook_strategy)
def test_b::ebook_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=b::Ebook_strategy)
def test_b::ebook_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=b::Ebook_strategy)
def test_b::ebook_info_type(instance):
    assert isinstance(instance.info, str)


@given(instance=b::Ebook_strategy)
def test_b::ebook_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original

@given(instance=b::B_strategy)
@settings(max_examples=50)
def test_b::b_instantiation(instance):
    assert isinstance(instance, b::B)

@given(instance=b::B_strategy)
def test_b::b_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=b::B_strategy)
def test_b::b_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=b::Model_strategy)
@settings(max_examples=50)
def test_b::model_instantiation(instance):
    assert isinstance(instance, b::Model)
