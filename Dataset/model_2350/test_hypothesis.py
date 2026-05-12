import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simplerdbms_RModelElement,
    RModelElement,
    simplerdbms_Table,
    simplerdbms_ForeignKey,
    simplerdbms_Key,
    simplerdbms_Schema,
    simplerdbms_Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplerdbms_rmodelelement_is_not_abstract():
    assert not inspect.isabstract(simplerdbms_RModelElement)


def test_simplerdbms_rmodelelement_constructor_exists():
    assert callable(simplerdbms_RModelElement.__init__)


def test_simplerdbms_rmodelelement_constructor_args():
    sig = inspect.signature(simplerdbms_RModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplerdbms_rmodelelement_has_kind():
    assert hasattr(simplerdbms_RModelElement, "kind")
    descriptor = None
    for klass in simplerdbms_RModelElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms_rmodelelement_has_name():
    assert hasattr(simplerdbms_RModelElement, "name")
    descriptor = None
    for klass in simplerdbms_RModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rmodelelement_is_not_abstract():
    assert not inspect.isabstract(RModelElement)


def test_rmodelelement_constructor_exists():
    assert callable(RModelElement.__init__)


def test_rmodelelement_constructor_args():
    sig = inspect.signature(RModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_table_is_not_abstract():
    assert not inspect.isabstract(simplerdbms_Table)


def test_simplerdbms_table_constructor_exists():
    assert callable(simplerdbms_Table.__init__)


def test_simplerdbms_table_constructor_args():
    sig = inspect.signature(simplerdbms_Table.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_foreignkey_is_not_abstract():
    assert not inspect.isabstract(simplerdbms_ForeignKey)


def test_simplerdbms_foreignkey_constructor_exists():
    assert callable(simplerdbms_ForeignKey.__init__)


def test_simplerdbms_foreignkey_constructor_args():
    sig = inspect.signature(simplerdbms_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_key_is_not_abstract():
    assert not inspect.isabstract(simplerdbms_Key)


def test_simplerdbms_key_constructor_exists():
    assert callable(simplerdbms_Key.__init__)


def test_simplerdbms_key_constructor_args():
    sig = inspect.signature(simplerdbms_Key.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_schema_is_not_abstract():
    assert not inspect.isabstract(simplerdbms_Schema)


def test_simplerdbms_schema_constructor_exists():
    assert callable(simplerdbms_Schema.__init__)


def test_simplerdbms_schema_constructor_args():
    sig = inspect.signature(simplerdbms_Schema.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_column_is_not_abstract():
    assert not inspect.isabstract(simplerdbms_Column)


def test_simplerdbms_column_constructor_exists():
    assert callable(simplerdbms_Column.__init__)


def test_simplerdbms_column_constructor_args():
    sig = inspect.signature(simplerdbms_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_simplerdbms_column_has_type():
    assert hasattr(simplerdbms_Column, "type")
    descriptor = None
    for klass in simplerdbms_Column.__mro__:
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
simplerdbms_RModelElement_strategy = st.builds(
    simplerdbms_RModelElement,
    kind=
        safe_text,
    name=
        safe_text
)
RModelElement_strategy = st.builds(
    RModelElement,
)
simplerdbms_Table_strategy = st.builds(
    simplerdbms_Table,
)
simplerdbms_ForeignKey_strategy = st.builds(
    simplerdbms_ForeignKey,
)
simplerdbms_Key_strategy = st.builds(
    simplerdbms_Key,
)
simplerdbms_Schema_strategy = st.builds(
    simplerdbms_Schema,
)
simplerdbms_Column_strategy = st.builds(
    simplerdbms_Column,
    type=
        safe_text
)

@given(instance=simplerdbms_RModelElement_strategy)
@settings(max_examples=50)
def test_simplerdbms_rmodelelement_instantiation(instance):
    assert isinstance(instance, simplerdbms_RModelElement)



@given(instance=simplerdbms_RModelElement_strategy)
def test_simplerdbms_rmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=simplerdbms_RModelElement_strategy)
def test_simplerdbms_rmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RModelElement_strategy)
@settings(max_examples=50)
def test_rmodelelement_instantiation(instance):
    assert isinstance(instance, RModelElement)

@given(instance=simplerdbms_Table_strategy)
@settings(max_examples=50)
def test_simplerdbms_table_instantiation(instance):
    assert isinstance(instance, simplerdbms_Table)

@given(instance=simplerdbms_ForeignKey_strategy)
@settings(max_examples=50)
def test_simplerdbms_foreignkey_instantiation(instance):
    assert isinstance(instance, simplerdbms_ForeignKey)

@given(instance=simplerdbms_Key_strategy)
@settings(max_examples=50)
def test_simplerdbms_key_instantiation(instance):
    assert isinstance(instance, simplerdbms_Key)

@given(instance=simplerdbms_Schema_strategy)
@settings(max_examples=50)
def test_simplerdbms_schema_instantiation(instance):
    assert isinstance(instance, simplerdbms_Schema)

@given(instance=simplerdbms_Column_strategy)
@settings(max_examples=50)
def test_simplerdbms_column_instantiation(instance):
    assert isinstance(instance, simplerdbms_Column)



@given(instance=simplerdbms_Column_strategy)
def test_simplerdbms_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
