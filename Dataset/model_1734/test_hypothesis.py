import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    transientotm_TWriter,
    transientotm_TBook,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transientotm_twriter_is_not_abstract():
    assert not inspect.isabstract(transientotm_TWriter)


def test_transientotm_twriter_constructor_exists():
    assert callable(transientotm_TWriter.__init__)


def test_transientotm_twriter_constructor_args():
    sig = inspect.signature(transientotm_TWriter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_transientotm_twriter_has_name():
    assert hasattr(transientotm_TWriter, "name")
    descriptor = None
    for klass in transientotm_TWriter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_transientotm_tbook_is_not_abstract():
    assert not inspect.isabstract(transientotm_TBook)


def test_transientotm_tbook_constructor_exists():
    assert callable(transientotm_TBook.__init__)


def test_transientotm_tbook_constructor_args():
    sig = inspect.signature(transientotm_TBook.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_transientotm_tbook_has_title():
    assert hasattr(transientotm_TBook, "title")
    descriptor = None
    for klass in transientotm_TBook.__mro__:
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
transientotm_TWriter_strategy = st.builds(
    transientotm_TWriter,
    name=
        safe_text
)
transientotm_TBook_strategy = st.builds(
    transientotm_TBook,
    title=
        safe_text
)

@given(instance=transientotm_TWriter_strategy)
@settings(max_examples=50)
def test_transientotm_twriter_instantiation(instance):
    assert isinstance(instance, transientotm_TWriter)



@given(instance=transientotm_TWriter_strategy)
def test_transientotm_twriter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=transientotm_TBook_strategy)
@settings(max_examples=50)
def test_transientotm_tbook_instantiation(instance):
    assert isinstance(instance, transientotm_TBook)



@given(instance=transientotm_TBook_strategy)
def test_transientotm_tbook_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
