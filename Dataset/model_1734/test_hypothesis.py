import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    transientotm::TWriter,
    transientotm::TBook,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transientotm::twriter_is_not_abstract():
    assert not inspect.isabstract(transientotm::TWriter)


def test_transientotm::twriter_constructor_exists():
    assert callable(transientotm::TWriter.__init__)


def test_transientotm::twriter_constructor_args():
    sig = inspect.signature(transientotm::TWriter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_transientotm::twriter_has_name():
    assert hasattr(transientotm::TWriter, "name")
    descriptor = None
    for klass in transientotm::TWriter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_transientotm::tbook_is_not_abstract():
    assert not inspect.isabstract(transientotm::TBook)


def test_transientotm::tbook_constructor_exists():
    assert callable(transientotm::TBook.__init__)


def test_transientotm::tbook_constructor_args():
    sig = inspect.signature(transientotm::TBook.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_transientotm::tbook_has_title():
    assert hasattr(transientotm::TBook, "title")
    descriptor = None
    for klass in transientotm::TBook.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)


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
transientotm::TWriter_strategy = st.builds(
    transientotm::TWriter,
    name=
        safe_text
)
transientotm::TBook_strategy = st.builds(
    transientotm::TBook,
    title=
        safe_text
)

@given(instance=transientotm::TWriter_strategy)
@settings(max_examples=50)
def test_transientotm::twriter_instantiation(instance):
    assert isinstance(instance, transientotm::TWriter)

@given(instance=transientotm::TWriter_strategy)
def test_transientotm::twriter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=transientotm::TWriter_strategy)
def test_transientotm::twriter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=transientotm::TBook_strategy)
@settings(max_examples=50)
def test_transientotm::tbook_instantiation(instance):
    assert isinstance(instance, transientotm::TBook)

@given(instance=transientotm::TBook_strategy)
def test_transientotm::tbook_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=transientotm::TBook_strategy)
def test_transientotm::tbook_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
