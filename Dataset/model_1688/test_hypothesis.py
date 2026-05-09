import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    yyf::NamedElement,
    yyf::Output,
    yyf::Foo,
    NamedElement,
    yyf::Relation,
    yyf::Base,
    yyf::Bar,
    yyf::Alias,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yyf::namedelement_is_not_abstract():
    assert not inspect.isabstract(yyf::NamedElement)


def test_yyf::namedelement_constructor_exists():
    assert callable(yyf::NamedElement.__init__)


def test_yyf::namedelement_constructor_args():
    sig = inspect.signature(yyf::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_yyf::namedelement_has_name():
    assert hasattr(yyf::NamedElement, "name")
    descriptor = None
    for klass in yyf::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_yyf::output_is_not_abstract():
    assert not inspect.isabstract(yyf::Output)


def test_yyf::output_constructor_exists():
    assert callable(yyf::Output.__init__)


def test_yyf::output_constructor_args():
    sig = inspect.signature(yyf::Output.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyf::output_has_id():
    assert hasattr(yyf::Output, "id")
    descriptor = None
    for klass in yyf::Output.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyf::foo_is_not_abstract():
    assert not inspect.isabstract(yyf::Foo)


def test_yyf::foo_constructor_exists():
    assert callable(yyf::Foo.__init__)


def test_yyf::foo_constructor_args():
    sig = inspect.signature(yyf::Foo.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyf::foo_has_id():
    assert hasattr(yyf::Foo, "id")
    descriptor = None
    for klass in yyf::Foo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_yyf::relation_is_not_abstract():
    assert not inspect.isabstract(yyf::Relation)


def test_yyf::relation_constructor_exists():
    assert callable(yyf::Relation.__init__)


def test_yyf::relation_constructor_args():
    sig = inspect.signature(yyf::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yyf::relation_has_since():
    assert hasattr(yyf::Relation, "since")
    descriptor = None
    for klass in yyf::Relation.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yyf::base_is_not_abstract():
    assert not inspect.isabstract(yyf::Base)


def test_yyf::base_constructor_exists():
    assert callable(yyf::Base.__init__)


def test_yyf::base_constructor_args():
    sig = inspect.signature(yyf::Base.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyf::base_has_id():
    assert hasattr(yyf::Base, "id")
    descriptor = None
    for klass in yyf::Base.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyf::bar_is_not_abstract():
    assert not inspect.isabstract(yyf::Bar)


def test_yyf::bar_constructor_exists():
    assert callable(yyf::Bar.__init__)


def test_yyf::bar_constructor_args():
    sig = inspect.signature(yyf::Bar.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyf::bar_has_id():
    assert hasattr(yyf::Bar, "id")
    descriptor = None
    for klass in yyf::Bar.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyf::alias_is_not_abstract():
    assert not inspect.isabstract(yyf::Alias)


def test_yyf::alias_constructor_exists():
    assert callable(yyf::Alias.__init__)


def test_yyf::alias_constructor_args():
    sig = inspect.signature(yyf::Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyf::alias_has_id():
    assert hasattr(yyf::Alias, "id")
    descriptor = None
    for klass in yyf::Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
yyf::NamedElement_strategy = st.builds(
    yyf::NamedElement,
    name=
        safe_text
)
yyf::Output_strategy = st.builds(
    yyf::Output,
    id=
        safe_text
)
yyf::Foo_strategy = st.builds(
    yyf::Foo,
    id=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
yyf::Relation_strategy = st.builds(
    yyf::Relation,
    since=
        safe_text
)
yyf::Base_strategy = st.builds(
    yyf::Base,
    id=
        st.integers()
)
yyf::Bar_strategy = st.builds(
    yyf::Bar,
    id=
        safe_text
)
yyf::Alias_strategy = st.builds(
    yyf::Alias,
    id=
        safe_text
)

@given(instance=yyf::NamedElement_strategy)
@settings(max_examples=50)
def test_yyf::namedelement_instantiation(instance):
    assert isinstance(instance, yyf::NamedElement)

@given(instance=yyf::NamedElement_strategy)
def test_yyf::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=yyf::NamedElement_strategy)
def test_yyf::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=yyf::Output_strategy)
@settings(max_examples=50)
def test_yyf::output_instantiation(instance):
    assert isinstance(instance, yyf::Output)

@given(instance=yyf::Output_strategy)
def test_yyf::output_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyf::Output_strategy)
def test_yyf::output_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyf::Foo_strategy)
@settings(max_examples=50)
def test_yyf::foo_instantiation(instance):
    assert isinstance(instance, yyf::Foo)

@given(instance=yyf::Foo_strategy)
def test_yyf::foo_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyf::Foo_strategy)
def test_yyf::foo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=yyf::Relation_strategy)
@settings(max_examples=50)
def test_yyf::relation_instantiation(instance):
    assert isinstance(instance, yyf::Relation)

@given(instance=yyf::Relation_strategy)
def test_yyf::relation_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=yyf::Relation_strategy)
def test_yyf::relation_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yyf::Base_strategy)
@settings(max_examples=50)
def test_yyf::base_instantiation(instance):
    assert isinstance(instance, yyf::Base)

@given(instance=yyf::Base_strategy)
def test_yyf::base_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=yyf::Base_strategy)
def test_yyf::base_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyf::Bar_strategy)
@settings(max_examples=50)
def test_yyf::bar_instantiation(instance):
    assert isinstance(instance, yyf::Bar)

@given(instance=yyf::Bar_strategy)
def test_yyf::bar_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyf::Bar_strategy)
def test_yyf::bar_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyf::Alias_strategy)
@settings(max_examples=50)
def test_yyf::alias_instantiation(instance):
    assert isinstance(instance, yyf::Alias)

@given(instance=yyf::Alias_strategy)
def test_yyf::alias_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyf::Alias_strategy)
def test_yyf::alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
