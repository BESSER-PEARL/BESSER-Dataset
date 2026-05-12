import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rdbmsMM_RModelElement,
    RModelElement,
    rdbmsMM_Schema,
    rdbmsMM_Key,
    rdbmsMM_Column,
    rdbmsMM_Table,
    rdbmsMM_ForeignKey,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbmsmm_rmodelelement_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM_RModelElement)


def test_rdbmsmm_rmodelelement_constructor_exists():
    assert callable(rdbmsMM_RModelElement.__init__)


def test_rdbmsmm_rmodelelement_constructor_args():
    sig = inspect.signature(rdbmsMM_RModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_rdbmsmm_rmodelelement_has_name():
    assert hasattr(rdbmsMM_RModelElement, "name")
    descriptor = None
    for klass in rdbmsMM_RModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbmsmm_rmodelelement_has_kind():
    assert hasattr(rdbmsMM_RModelElement, "kind")
    descriptor = None
    for klass in rdbmsMM_RModelElement.__mro__:
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



def test_rdbmsmm_schema_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM_Schema)


def test_rdbmsmm_schema_constructor_exists():
    assert callable(rdbmsMM_Schema.__init__)


def test_rdbmsmm_schema_constructor_args():
    sig = inspect.signature(rdbmsMM_Schema.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsmm_key_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM_Key)


def test_rdbmsmm_key_constructor_exists():
    assert callable(rdbmsMM_Key.__init__)


def test_rdbmsmm_key_constructor_args():
    sig = inspect.signature(rdbmsMM_Key.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsmm_column_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM_Column)


def test_rdbmsmm_column_constructor_exists():
    assert callable(rdbmsMM_Column.__init__)


def test_rdbmsmm_column_constructor_args():
    sig = inspect.signature(rdbmsMM_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_rdbmsmm_column_has_type():
    assert hasattr(rdbmsMM_Column, "type")
    descriptor = None
    for klass in rdbmsMM_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsmm_table_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM_Table)


def test_rdbmsmm_table_constructor_exists():
    assert callable(rdbmsMM_Table.__init__)


def test_rdbmsmm_table_constructor_args():
    sig = inspect.signature(rdbmsMM_Table.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsmm_foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM_ForeignKey)


def test_rdbmsmm_foreignkey_constructor_exists():
    assert callable(rdbmsMM_ForeignKey.__init__)


def test_rdbmsmm_foreignkey_constructor_args():
    sig = inspect.signature(rdbmsMM_ForeignKey.__init__)
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
rdbmsMM_RModelElement_strategy = st.builds(
    rdbmsMM_RModelElement,
    name=
        safe_text,
    kind=
        safe_text
)
RModelElement_strategy = st.builds(
    RModelElement,
)
rdbmsMM_Schema_strategy = st.builds(
    rdbmsMM_Schema,
)
rdbmsMM_Key_strategy = st.builds(
    rdbmsMM_Key,
)
rdbmsMM_Column_strategy = st.builds(
    rdbmsMM_Column,
    type=
        safe_text
)
rdbmsMM_Table_strategy = st.builds(
    rdbmsMM_Table,
)
rdbmsMM_ForeignKey_strategy = st.builds(
    rdbmsMM_ForeignKey,
)

@given(instance=rdbmsMM_RModelElement_strategy)
@settings(max_examples=50)
def test_rdbmsmm_rmodelelement_instantiation(instance):
    assert isinstance(instance, rdbmsMM_RModelElement)



@given(instance=rdbmsMM_RModelElement_strategy)
def test_rdbmsmm_rmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rdbmsMM_RModelElement_strategy)
def test_rdbmsmm_rmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=RModelElement_strategy)
@settings(max_examples=50)
def test_rmodelelement_instantiation(instance):
    assert isinstance(instance, RModelElement)

@given(instance=rdbmsMM_Schema_strategy)
@settings(max_examples=50)
def test_rdbmsmm_schema_instantiation(instance):
    assert isinstance(instance, rdbmsMM_Schema)

@given(instance=rdbmsMM_Key_strategy)
@settings(max_examples=50)
def test_rdbmsmm_key_instantiation(instance):
    assert isinstance(instance, rdbmsMM_Key)

@given(instance=rdbmsMM_Column_strategy)
@settings(max_examples=50)
def test_rdbmsmm_column_instantiation(instance):
    assert isinstance(instance, rdbmsMM_Column)



@given(instance=rdbmsMM_Column_strategy)
def test_rdbmsmm_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rdbmsMM_Table_strategy)
@settings(max_examples=50)
def test_rdbmsmm_table_instantiation(instance):
    assert isinstance(instance, rdbmsMM_Table)

@given(instance=rdbmsMM_ForeignKey_strategy)
@settings(max_examples=50)
def test_rdbmsmm_foreignkey_instantiation(instance):
    assert isinstance(instance, rdbmsMM_ForeignKey)
