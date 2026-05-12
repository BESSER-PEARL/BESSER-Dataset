import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpleRdbms_RModelElement,
    RModelElement,
    simpleRdbms_ForeignKey,
    simpleRdbms_Table,
    simpleRdbms_Key,
    simpleRdbms_Column,
    simpleRdbms_Schema,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplerdbms_rmodelelement_is_not_abstract():
    assert not inspect.isabstract(simpleRdbms_RModelElement)


def test_simplerdbms_rmodelelement_constructor_exists():
    assert callable(simpleRdbms_RModelElement.__init__)


def test_simplerdbms_rmodelelement_constructor_args():
    sig = inspect.signature(simpleRdbms_RModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_simplerdbms_rmodelelement_has_name():
    assert hasattr(simpleRdbms_RModelElement, "name")
    descriptor = None
    for klass in simpleRdbms_RModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms_rmodelelement_has_kind():
    assert hasattr(simpleRdbms_RModelElement, "kind")
    descriptor = None
    for klass in simpleRdbms_RModelElement.__mro__:
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



def test_simplerdbms_foreignkey_is_not_abstract():
    assert not inspect.isabstract(simpleRdbms_ForeignKey)


def test_simplerdbms_foreignkey_constructor_exists():
    assert callable(simpleRdbms_ForeignKey.__init__)


def test_simplerdbms_foreignkey_constructor_args():
    sig = inspect.signature(simpleRdbms_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_table_is_not_abstract():
    assert not inspect.isabstract(simpleRdbms_Table)


def test_simplerdbms_table_constructor_exists():
    assert callable(simpleRdbms_Table.__init__)


def test_simplerdbms_table_constructor_args():
    sig = inspect.signature(simpleRdbms_Table.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_key_is_not_abstract():
    assert not inspect.isabstract(simpleRdbms_Key)


def test_simplerdbms_key_constructor_exists():
    assert callable(simpleRdbms_Key.__init__)


def test_simplerdbms_key_constructor_args():
    sig = inspect.signature(simpleRdbms_Key.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_column_is_not_abstract():
    assert not inspect.isabstract(simpleRdbms_Column)


def test_simplerdbms_column_constructor_exists():
    assert callable(simpleRdbms_Column.__init__)


def test_simplerdbms_column_constructor_args():
    sig = inspect.signature(simpleRdbms_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_simplerdbms_column_has_type():
    assert hasattr(simpleRdbms_Column, "type")
    descriptor = None
    for klass in simpleRdbms_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_simplerdbms_schema_is_not_abstract():
    assert not inspect.isabstract(simpleRdbms_Schema)


def test_simplerdbms_schema_constructor_exists():
    assert callable(simpleRdbms_Schema.__init__)


def test_simplerdbms_schema_constructor_args():
    sig = inspect.signature(simpleRdbms_Schema.__init__)
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
simpleRdbms_RModelElement_strategy = st.builds(
    simpleRdbms_RModelElement,
    name=
        safe_text,
    kind=
        safe_text
)
RModelElement_strategy = st.builds(
    RModelElement,
)
simpleRdbms_ForeignKey_strategy = st.builds(
    simpleRdbms_ForeignKey,
)
simpleRdbms_Table_strategy = st.builds(
    simpleRdbms_Table,
)
simpleRdbms_Key_strategy = st.builds(
    simpleRdbms_Key,
)
simpleRdbms_Column_strategy = st.builds(
    simpleRdbms_Column,
    type=
        safe_text
)
simpleRdbms_Schema_strategy = st.builds(
    simpleRdbms_Schema,
)

@given(instance=simpleRdbms_RModelElement_strategy)
@settings(max_examples=50)
def test_simplerdbms_rmodelelement_instantiation(instance):
    assert isinstance(instance, simpleRdbms_RModelElement)



@given(instance=simpleRdbms_RModelElement_strategy)
def test_simplerdbms_rmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=simpleRdbms_RModelElement_strategy)
def test_simplerdbms_rmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=RModelElement_strategy)
@settings(max_examples=50)
def test_rmodelelement_instantiation(instance):
    assert isinstance(instance, RModelElement)

@given(instance=simpleRdbms_ForeignKey_strategy)
@settings(max_examples=50)
def test_simplerdbms_foreignkey_instantiation(instance):
    assert isinstance(instance, simpleRdbms_ForeignKey)

@given(instance=simpleRdbms_Table_strategy)
@settings(max_examples=50)
def test_simplerdbms_table_instantiation(instance):
    assert isinstance(instance, simpleRdbms_Table)

@given(instance=simpleRdbms_Key_strategy)
@settings(max_examples=50)
def test_simplerdbms_key_instantiation(instance):
    assert isinstance(instance, simpleRdbms_Key)

@given(instance=simpleRdbms_Column_strategy)
@settings(max_examples=50)
def test_simplerdbms_column_instantiation(instance):
    assert isinstance(instance, simpleRdbms_Column)



@given(instance=simpleRdbms_Column_strategy)
def test_simplerdbms_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=simpleRdbms_Schema_strategy)
@settings(max_examples=50)
def test_simplerdbms_schema_instantiation(instance):
    assert isinstance(instance, simpleRdbms_Schema)
