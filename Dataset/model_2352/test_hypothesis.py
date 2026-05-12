import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rdbms_RModelElement,
    RModelElement,
    rdbms_Table,
    rdbms_ForeignKey,
    rdbms_Schema,
    rdbms_Column,
    rdbms_Key,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbms_rmodelelement_is_not_abstract():
    assert not inspect.isabstract(rdbms_RModelElement)


def test_rdbms_rmodelelement_constructor_exists():
    assert callable(rdbms_RModelElement.__init__)


def test_rdbms_rmodelelement_constructor_args():
    sig = inspect.signature(rdbms_RModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms_rmodelelement_has_kind():
    assert hasattr(rdbms_RModelElement, "kind")
    descriptor = None
    for klass in rdbms_RModelElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_rmodelelement_has_name():
    assert hasattr(rdbms_RModelElement, "name")
    descriptor = None
    for klass in rdbms_RModelElement.__mro__:
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



def test_rdbms_table_is_not_abstract():
    assert not inspect.isabstract(rdbms_Table)


def test_rdbms_table_constructor_exists():
    assert callable(rdbms_Table.__init__)


def test_rdbms_table_constructor_args():
    sig = inspect.signature(rdbms_Table.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdbms_ForeignKey)


def test_rdbms_foreignkey_constructor_exists():
    assert callable(rdbms_ForeignKey.__init__)


def test_rdbms_foreignkey_constructor_args():
    sig = inspect.signature(rdbms_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_schema_is_not_abstract():
    assert not inspect.isabstract(rdbms_Schema)


def test_rdbms_schema_constructor_exists():
    assert callable(rdbms_Schema.__init__)


def test_rdbms_schema_constructor_args():
    sig = inspect.signature(rdbms_Schema.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_column_is_not_abstract():
    assert not inspect.isabstract(rdbms_Column)


def test_rdbms_column_constructor_exists():
    assert callable(rdbms_Column.__init__)


def test_rdbms_column_constructor_args():
    sig = inspect.signature(rdbms_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_rdbms_column_has_type():
    assert hasattr(rdbms_Column, "type")
    descriptor = None
    for klass in rdbms_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_key_is_not_abstract():
    assert not inspect.isabstract(rdbms_Key)


def test_rdbms_key_constructor_exists():
    assert callable(rdbms_Key.__init__)


def test_rdbms_key_constructor_args():
    sig = inspect.signature(rdbms_Key.__init__)
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
rdbms_RModelElement_strategy = st.builds(
    rdbms_RModelElement,
    kind=
        safe_text,
    name=
        safe_text
)
RModelElement_strategy = st.builds(
    RModelElement,
)
rdbms_Table_strategy = st.builds(
    rdbms_Table,
)
rdbms_ForeignKey_strategy = st.builds(
    rdbms_ForeignKey,
)
rdbms_Schema_strategy = st.builds(
    rdbms_Schema,
)
rdbms_Column_strategy = st.builds(
    rdbms_Column,
    type=
        safe_text
)
rdbms_Key_strategy = st.builds(
    rdbms_Key,
)

@given(instance=rdbms_RModelElement_strategy)
@settings(max_examples=50)
def test_rdbms_rmodelelement_instantiation(instance):
    assert isinstance(instance, rdbms_RModelElement)



@given(instance=rdbms_RModelElement_strategy)
def test_rdbms_rmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=rdbms_RModelElement_strategy)
def test_rdbms_rmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RModelElement_strategy)
@settings(max_examples=50)
def test_rmodelelement_instantiation(instance):
    assert isinstance(instance, RModelElement)

@given(instance=rdbms_Table_strategy)
@settings(max_examples=50)
def test_rdbms_table_instantiation(instance):
    assert isinstance(instance, rdbms_Table)

@given(instance=rdbms_ForeignKey_strategy)
@settings(max_examples=50)
def test_rdbms_foreignkey_instantiation(instance):
    assert isinstance(instance, rdbms_ForeignKey)

@given(instance=rdbms_Schema_strategy)
@settings(max_examples=50)
def test_rdbms_schema_instantiation(instance):
    assert isinstance(instance, rdbms_Schema)

@given(instance=rdbms_Column_strategy)
@settings(max_examples=50)
def test_rdbms_column_instantiation(instance):
    assert isinstance(instance, rdbms_Column)



@given(instance=rdbms_Column_strategy)
def test_rdbms_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rdbms_Key_strategy)
@settings(max_examples=50)
def test_rdbms_key_instantiation(instance):
    assert isinstance(instance, rdbms_Key)
