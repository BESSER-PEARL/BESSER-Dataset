import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    yyf_NamedElement,
    yyf_Output,
    yyf_Foo,
    NamedElement,
    yyf_Relation,
    yyf_Base,
    yyf_Bar,
    yyf_Alias,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yyf_namedelement_is_not_abstract():
    assert not inspect.isabstract(yyf_NamedElement)


def test_yyf_namedelement_constructor_exists():
    assert callable(yyf_NamedElement.__init__)


def test_yyf_namedelement_constructor_args():
    sig = inspect.signature(yyf_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_yyf_namedelement_has_name():
    assert hasattr(yyf_NamedElement, "name")
    descriptor = None
    for klass in yyf_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_yyf_output_is_not_abstract():
    assert not inspect.isabstract(yyf_Output)


def test_yyf_output_constructor_exists():
    assert callable(yyf_Output.__init__)


def test_yyf_output_constructor_args():
    sig = inspect.signature(yyf_Output.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyf_output_has_id():
    assert hasattr(yyf_Output, "id")
    descriptor = None
    for klass in yyf_Output.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyf_foo_is_not_abstract():
    assert not inspect.isabstract(yyf_Foo)


def test_yyf_foo_constructor_exists():
    assert callable(yyf_Foo.__init__)


def test_yyf_foo_constructor_args():
    sig = inspect.signature(yyf_Foo.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyf_foo_has_id():
    assert hasattr(yyf_Foo, "id")
    descriptor = None
    for klass in yyf_Foo.__mro__:
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



def test_yyf_relation_is_not_abstract():
    assert not inspect.isabstract(yyf_Relation)


def test_yyf_relation_constructor_exists():
    assert callable(yyf_Relation.__init__)


def test_yyf_relation_constructor_args():
    sig = inspect.signature(yyf_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yyf_relation_has_since():
    assert hasattr(yyf_Relation, "since")
    descriptor = None
    for klass in yyf_Relation.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yyf_base_is_not_abstract():
    assert not inspect.isabstract(yyf_Base)


def test_yyf_base_constructor_exists():
    assert callable(yyf_Base.__init__)


def test_yyf_base_constructor_args():
    sig = inspect.signature(yyf_Base.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyf_base_has_id():
    assert hasattr(yyf_Base, "id")
    descriptor = None
    for klass in yyf_Base.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyf_bar_is_not_abstract():
    assert not inspect.isabstract(yyf_Bar)


def test_yyf_bar_constructor_exists():
    assert callable(yyf_Bar.__init__)


def test_yyf_bar_constructor_args():
    sig = inspect.signature(yyf_Bar.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyf_bar_has_id():
    assert hasattr(yyf_Bar, "id")
    descriptor = None
    for klass in yyf_Bar.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyf_alias_is_not_abstract():
    assert not inspect.isabstract(yyf_Alias)


def test_yyf_alias_constructor_exists():
    assert callable(yyf_Alias.__init__)


def test_yyf_alias_constructor_args():
    sig = inspect.signature(yyf_Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyf_alias_has_id():
    assert hasattr(yyf_Alias, "id")
    descriptor = None
    for klass in yyf_Alias.__mro__:
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
yyf_NamedElement_strategy = st.builds(
    yyf_NamedElement,
    name=
        safe_text
)
yyf_Output_strategy = st.builds(
    yyf_Output,
    id=
        safe_text
)
yyf_Foo_strategy = st.builds(
    yyf_Foo,
    id=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
yyf_Relation_strategy = st.builds(
    yyf_Relation,
    since=
        safe_text
)
yyf_Base_strategy = st.builds(
    yyf_Base,
    id=
        st.integers()
)
yyf_Bar_strategy = st.builds(
    yyf_Bar,
    id=
        safe_text
)
yyf_Alias_strategy = st.builds(
    yyf_Alias,
    id=
        safe_text
)

@given(instance=yyf_NamedElement_strategy)
@settings(max_examples=50)
def test_yyf_namedelement_instantiation(instance):
    assert isinstance(instance, yyf_NamedElement)



@given(instance=yyf_NamedElement_strategy)
def test_yyf_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=yyf_Output_strategy)
@settings(max_examples=50)
def test_yyf_output_instantiation(instance):
    assert isinstance(instance, yyf_Output)



@given(instance=yyf_Output_strategy)
def test_yyf_output_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyf_Foo_strategy)
@settings(max_examples=50)
def test_yyf_foo_instantiation(instance):
    assert isinstance(instance, yyf_Foo)



@given(instance=yyf_Foo_strategy)
def test_yyf_foo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=yyf_Relation_strategy)
@settings(max_examples=50)
def test_yyf_relation_instantiation(instance):
    assert isinstance(instance, yyf_Relation)



@given(instance=yyf_Relation_strategy)
def test_yyf_relation_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yyf_Base_strategy)
@settings(max_examples=50)
def test_yyf_base_instantiation(instance):
    assert isinstance(instance, yyf_Base)



@given(instance=yyf_Base_strategy)
def test_yyf_base_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyf_Bar_strategy)
@settings(max_examples=50)
def test_yyf_bar_instantiation(instance):
    assert isinstance(instance, yyf_Bar)



@given(instance=yyf_Bar_strategy)
def test_yyf_bar_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyf_Alias_strategy)
@settings(max_examples=50)
def test_yyf_alias_instantiation(instance):
    assert isinstance(instance, yyf_Alias)



@given(instance=yyf_Alias_strategy)
def test_yyf_alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
