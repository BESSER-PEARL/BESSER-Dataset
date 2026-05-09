import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library::OclLibrary,
    library::OclExpression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::ocllibrary_is_not_abstract():
    assert not inspect.isabstract(library::OclLibrary)


def test_library::ocllibrary_constructor_exists():
    assert callable(library::OclLibrary.__init__)


def test_library::ocllibrary_constructor_args():
    sig = inspect.signature(library::OclLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::ocllibrary_has_name():
    assert hasattr(library::OclLibrary, "name")
    descriptor = None
    for klass in library::OclLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::oclexpression_is_not_abstract():
    assert not inspect.isabstract(library::OclExpression)


def test_library::oclexpression_constructor_exists():
    assert callable(library::OclExpression.__init__)


def test_library::oclexpression_constructor_args():
    sig = inspect.signature(library::OclExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "query" in params, "Missing parameter 'query'"
    assert "context" in params, "Missing parameter 'context'"
    assert "description" in params, "Missing parameter 'description'"

def test_library::oclexpression_has_name():
    assert hasattr(library::OclExpression, "name")
    descriptor = None
    for klass in library::OclExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_library::oclexpression_has_query():
    assert hasattr(library::OclExpression, "query")
    descriptor = None
    for klass in library::OclExpression.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)

def test_library::oclexpression_has_context():
    assert hasattr(library::OclExpression, "context")
    descriptor = None
    for klass in library::OclExpression.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)

def test_library::oclexpression_has_description():
    assert hasattr(library::OclExpression, "description")
    descriptor = None
    for klass in library::OclExpression.__mro__:
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
library::OclLibrary_strategy = st.builds(
    library::OclLibrary,
    name=
        safe_text
)
library::OclExpression_strategy = st.builds(
    library::OclExpression,
    name=
        safe_text,
    query=
        safe_text,
    context=
        safe_text,
    description=
        safe_text
)

@given(instance=library::OclLibrary_strategy)
@settings(max_examples=50)
def test_library::ocllibrary_instantiation(instance):
    assert isinstance(instance, library::OclLibrary)

@given(instance=library::OclLibrary_strategy)
def test_library::ocllibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::OclLibrary_strategy)
def test_library::ocllibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library::OclExpression_strategy)
@settings(max_examples=50)
def test_library::oclexpression_instantiation(instance):
    assert isinstance(instance, library::OclExpression)

@given(instance=library::OclExpression_strategy)
def test_library::oclexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::OclExpression_strategy)
def test_library::oclexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library::OclExpression_strategy)
def test_library::oclexpression_query_type(instance):
    assert isinstance(instance.query, str)


@given(instance=library::OclExpression_strategy)
def test_library::oclexpression_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original

@given(instance=library::OclExpression_strategy)
def test_library::oclexpression_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=library::OclExpression_strategy)
def test_library::oclexpression_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=library::OclExpression_strategy)
def test_library::oclexpression_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=library::OclExpression_strategy)
def test_library::oclexpression_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
