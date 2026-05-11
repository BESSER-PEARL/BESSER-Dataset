import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rdbmsMM::RModelElement,
    RModelElement,
    rdbmsMM::Table,
    rdbmsMM::Schema,
    rdbmsMM::Key,
    rdbmsMM::ForeignKey,
    rdbmsMM::Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbmsmm::rmodelelement_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM::RModelElement)


def test_rdbmsmm::rmodelelement_constructor_exists():
    assert callable(rdbmsMM::RModelElement.__init__)


def test_rdbmsmm::rmodelelement_constructor_args():
    sig = inspect.signature(rdbmsMM::RModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_rdbmsmm::rmodelelement_has_name():
    assert hasattr(rdbmsMM::RModelElement, "name")
    descriptor = None
    for klass in rdbmsMM::RModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbmsmm::rmodelelement_has_kind():
    assert hasattr(rdbmsMM::RModelElement, "kind")
    descriptor = None
    for klass in rdbmsMM::RModelElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_rmodelelement_is_not_abstract():
    assert not inspect.isabstract(RModelElement)


def test_rmodelelement_constructor_exists():
    assert callable(RModelElement.__init__)


def test_rmodelelement_constructor_args():
    sig = inspect.signature(RModelElement.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsmm::table_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM::Table)


def test_rdbmsmm::table_constructor_exists():
    assert callable(rdbmsMM::Table.__init__)


def test_rdbmsmm::table_constructor_args():
    sig = inspect.signature(rdbmsMM::Table.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsmm::schema_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM::Schema)


def test_rdbmsmm::schema_constructor_exists():
    assert callable(rdbmsMM::Schema.__init__)


def test_rdbmsmm::schema_constructor_args():
    sig = inspect.signature(rdbmsMM::Schema.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsmm::key_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM::Key)


def test_rdbmsmm::key_constructor_exists():
    assert callable(rdbmsMM::Key.__init__)


def test_rdbmsmm::key_constructor_args():
    sig = inspect.signature(rdbmsMM::Key.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsmm::foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM::ForeignKey)


def test_rdbmsmm::foreignkey_constructor_exists():
    assert callable(rdbmsMM::ForeignKey.__init__)


def test_rdbmsmm::foreignkey_constructor_args():
    sig = inspect.signature(rdbmsMM::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsmm::column_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM::Column)


def test_rdbmsmm::column_constructor_exists():
    assert callable(rdbmsMM::Column.__init__)


def test_rdbmsmm::column_constructor_args():
    sig = inspect.signature(rdbmsMM::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_rdbmsmm::column_has_type():
    assert hasattr(rdbmsMM::Column, "type")
    descriptor = None
    for klass in rdbmsMM::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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
rdbmsMM::RModelElement_strategy = st.builds(
    rdbmsMM::RModelElement,
    name=
        safe_text,
    kind=
        safe_text
)
RModelElement_strategy = st.builds(
    RModelElement,
)
rdbmsMM::Table_strategy = st.builds(
    rdbmsMM::Table,
)
rdbmsMM::Schema_strategy = st.builds(
    rdbmsMM::Schema,
)
rdbmsMM::Key_strategy = st.builds(
    rdbmsMM::Key,
)
rdbmsMM::ForeignKey_strategy = st.builds(
    rdbmsMM::ForeignKey,
)
rdbmsMM::Column_strategy = st.builds(
    rdbmsMM::Column,
    type=
        safe_text
)

@given(instance=rdbmsMM::RModelElement_strategy)
@settings(max_examples=50)
def test_rdbmsmm::rmodelelement_instantiation(instance):
    assert isinstance(instance, rdbmsMM::RModelElement)

@given(instance=rdbmsMM::RModelElement_strategy)
def test_rdbmsmm::rmodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbmsMM::RModelElement_strategy)
def test_rdbmsmm::rmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbmsMM::RModelElement_strategy)
def test_rdbmsmm::rmodelelement_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=rdbmsMM::RModelElement_strategy)
def test_rdbmsmm::rmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=RModelElement_strategy)
@settings(max_examples=50)
def test_rmodelelement_instantiation(instance):
    assert isinstance(instance, RModelElement)

@given(instance=rdbmsMM::Table_strategy)
@settings(max_examples=50)
def test_rdbmsmm::table_instantiation(instance):
    assert isinstance(instance, rdbmsMM::Table)

@given(instance=rdbmsMM::Schema_strategy)
@settings(max_examples=50)
def test_rdbmsmm::schema_instantiation(instance):
    assert isinstance(instance, rdbmsMM::Schema)

@given(instance=rdbmsMM::Key_strategy)
@settings(max_examples=50)
def test_rdbmsmm::key_instantiation(instance):
    assert isinstance(instance, rdbmsMM::Key)

@given(instance=rdbmsMM::ForeignKey_strategy)
@settings(max_examples=50)
def test_rdbmsmm::foreignkey_instantiation(instance):
    assert isinstance(instance, rdbmsMM::ForeignKey)

@given(instance=rdbmsMM::Column_strategy)
@settings(max_examples=50)
def test_rdbmsmm::column_instantiation(instance):
    assert isinstance(instance, rdbmsMM::Column)

@given(instance=rdbmsMM::Column_strategy)
def test_rdbmsmm::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=rdbmsMM::Column_strategy)
def test_rdbmsmm::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
