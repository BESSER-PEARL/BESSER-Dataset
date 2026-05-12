import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    library_OclLibrary,
    library_OclExpression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_ocllibrary_is_not_abstract():
    assert not inspect.isabstract(library_OclLibrary)


def test_library_ocllibrary_constructor_exists():
    assert callable(library_OclLibrary.__init__)


def test_library_ocllibrary_constructor_args():
    sig = inspect.signature(library_OclLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_ocllibrary_has_name():
    assert hasattr(library_OclLibrary, "name")
    descriptor = None
    for klass in library_OclLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library_oclexpression_is_not_abstract():
    assert not inspect.isabstract(library_OclExpression)


def test_library_oclexpression_constructor_exists():
    assert callable(library_OclExpression.__init__)


def test_library_oclexpression_constructor_args():
    sig = inspect.signature(library_OclExpression.__init__)
    params = list(sig.parameters.keys())
    assert "query" in params, "Missing parameter 'query'"
    assert "name" in params, "Missing parameter 'name'"
    assert "context" in params, "Missing parameter 'context'"
    assert "description" in params, "Missing parameter 'description'"

def test_library_oclexpression_has_query():
    assert hasattr(library_OclExpression, "query")
    descriptor = None
    for klass in library_OclExpression.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)

def test_library_oclexpression_has_name():
    assert hasattr(library_OclExpression, "name")
    descriptor = None
    for klass in library_OclExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_library_oclexpression_has_context():
    assert hasattr(library_OclExpression, "context")
    descriptor = None
    for klass in library_OclExpression.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)

def test_library_oclexpression_has_description():
    assert hasattr(library_OclExpression, "description")
    descriptor = None
    for klass in library_OclExpression.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
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
library_OclLibrary_strategy = st.builds(
    library_OclLibrary,
    name=
        safe_text
)
library_OclExpression_strategy = st.builds(
    library_OclExpression,
    query=
        safe_text,
    name=
        safe_text,
    context=
        safe_text,
    description=
        safe_text
)

@given(instance=library_OclLibrary_strategy)
@settings(max_examples=50)
def test_library_ocllibrary_instantiation(instance):
    assert isinstance(instance, library_OclLibrary)



@given(instance=library_OclLibrary_strategy)
def test_library_ocllibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library_OclExpression_strategy)
@settings(max_examples=50)
def test_library_oclexpression_instantiation(instance):
    assert isinstance(instance, library_OclExpression)



@given(instance=library_OclExpression_strategy)
def test_library_oclexpression_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original



@given(instance=library_OclExpression_strategy)
def test_library_oclexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=library_OclExpression_strategy)
def test_library_oclexpression_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original



@given(instance=library_OclExpression_strategy)
def test_library_oclexpression_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
