import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SimpleRDBMS_RdbmsModelElement,
    RdbmsModelElement,
    SimpleRDBMS_RdbmsKey,
    SimpleRDBMS_RdbmsSchema,
    SimpleRDBMS_RdbmsTable,
    SimpleRDBMS_RdbmsColumn,
    SimpleRDBMS_RdbmsForeignKey,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplerdbms_rdbmsmodelelement_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_RdbmsModelElement)


def test_simplerdbms_rdbmsmodelelement_constructor_exists():
    assert callable(SimpleRDBMS_RdbmsModelElement.__init__)


def test_simplerdbms_rdbmsmodelelement_constructor_args():
    sig = inspect.signature(SimpleRDBMS_RdbmsModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "rdbmsName" in params, "Missing parameter 'rdbmsName'"
    assert "rdbmsKind" in params, "Missing parameter 'rdbmsKind'"
    assert "id" in params, "Missing parameter 'id'"

def test_simplerdbms_rdbmsmodelelement_has_rdbmsName():
    assert hasattr(SimpleRDBMS_RdbmsModelElement, "rdbmsName")
    descriptor = None
    for klass in SimpleRDBMS_RdbmsModelElement.__mro__:
        if "rdbmsName" in klass.__dict__:
            descriptor = klass.__dict__["rdbmsName"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms_rdbmsmodelelement_has_rdbmsKind():
    assert hasattr(SimpleRDBMS_RdbmsModelElement, "rdbmsKind")
    descriptor = None
    for klass in SimpleRDBMS_RdbmsModelElement.__mro__:
        if "rdbmsKind" in klass.__dict__:
            descriptor = klass.__dict__["rdbmsKind"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms_rdbmsmodelelement_has_id():
    assert hasattr(SimpleRDBMS_RdbmsModelElement, "id")
    descriptor = None
    for klass in SimpleRDBMS_RdbmsModelElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsmodelelement_is_not_abstract():
    assert not inspect.isabstract(RdbmsModelElement)


def test_rdbmsmodelelement_constructor_exists():
    assert callable(RdbmsModelElement.__init__)


def test_rdbmsmodelelement_constructor_args():
    sig = inspect.signature(RdbmsModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_rdbmskey_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_RdbmsKey)


def test_simplerdbms_rdbmskey_constructor_exists():
    assert callable(SimpleRDBMS_RdbmsKey.__init__)


def test_simplerdbms_rdbmskey_constructor_args():
    sig = inspect.signature(SimpleRDBMS_RdbmsKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_rdbmsschema_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_RdbmsSchema)


def test_simplerdbms_rdbmsschema_constructor_exists():
    assert callable(SimpleRDBMS_RdbmsSchema.__init__)


def test_simplerdbms_rdbmsschema_constructor_args():
    sig = inspect.signature(SimpleRDBMS_RdbmsSchema.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_rdbmstable_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_RdbmsTable)


def test_simplerdbms_rdbmstable_constructor_exists():
    assert callable(SimpleRDBMS_RdbmsTable.__init__)


def test_simplerdbms_rdbmstable_constructor_args():
    sig = inspect.signature(SimpleRDBMS_RdbmsTable.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_rdbmscolumn_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_RdbmsColumn)


def test_simplerdbms_rdbmscolumn_constructor_exists():
    assert callable(SimpleRDBMS_RdbmsColumn.__init__)


def test_simplerdbms_rdbmscolumn_constructor_args():
    sig = inspect.signature(SimpleRDBMS_RdbmsColumn.__init__)
    params = list(sig.parameters.keys())
    assert "rdbmsType" in params, "Missing parameter 'rdbmsType'"

def test_simplerdbms_rdbmscolumn_has_rdbmsType():
    assert hasattr(SimpleRDBMS_RdbmsColumn, "rdbmsType")
    descriptor = None
    for klass in SimpleRDBMS_RdbmsColumn.__mro__:
        if "rdbmsType" in klass.__dict__:
            descriptor = klass.__dict__["rdbmsType"]
            break
    assert isinstance(descriptor, property)



def test_simplerdbms_rdbmsforeignkey_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_RdbmsForeignKey)


def test_simplerdbms_rdbmsforeignkey_constructor_exists():
    assert callable(SimpleRDBMS_RdbmsForeignKey.__init__)


def test_simplerdbms_rdbmsforeignkey_constructor_args():
    sig = inspect.signature(SimpleRDBMS_RdbmsForeignKey.__init__)
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
SimpleRDBMS_RdbmsModelElement_strategy = st.builds(
    SimpleRDBMS_RdbmsModelElement,
    rdbmsName=
        safe_text,
    rdbmsKind=
        safe_text,
    id=
        safe_text
)
RdbmsModelElement_strategy = st.builds(
    RdbmsModelElement,
)
SimpleRDBMS_RdbmsKey_strategy = st.builds(
    SimpleRDBMS_RdbmsKey,
)
SimpleRDBMS_RdbmsSchema_strategy = st.builds(
    SimpleRDBMS_RdbmsSchema,
)
SimpleRDBMS_RdbmsTable_strategy = st.builds(
    SimpleRDBMS_RdbmsTable,
)
SimpleRDBMS_RdbmsColumn_strategy = st.builds(
    SimpleRDBMS_RdbmsColumn,
    rdbmsType=
        safe_text
)
SimpleRDBMS_RdbmsForeignKey_strategy = st.builds(
    SimpleRDBMS_RdbmsForeignKey,
)

@given(instance=SimpleRDBMS_RdbmsModelElement_strategy)
@settings(max_examples=50)
def test_simplerdbms_rdbmsmodelelement_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_RdbmsModelElement)



@given(instance=SimpleRDBMS_RdbmsModelElement_strategy)
def test_simplerdbms_rdbmsmodelelement_rdbmsName_setter(instance):
    original = instance.rdbmsName
    instance.rdbmsName = original
    assert instance.rdbmsName == original



@given(instance=SimpleRDBMS_RdbmsModelElement_strategy)
def test_simplerdbms_rdbmsmodelelement_rdbmsKind_setter(instance):
    original = instance.rdbmsKind
    instance.rdbmsKind = original
    assert instance.rdbmsKind == original



@given(instance=SimpleRDBMS_RdbmsModelElement_strategy)
def test_simplerdbms_rdbmsmodelelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=RdbmsModelElement_strategy)
@settings(max_examples=50)
def test_rdbmsmodelelement_instantiation(instance):
    assert isinstance(instance, RdbmsModelElement)

@given(instance=SimpleRDBMS_RdbmsKey_strategy)
@settings(max_examples=50)
def test_simplerdbms_rdbmskey_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_RdbmsKey)

@given(instance=SimpleRDBMS_RdbmsSchema_strategy)
@settings(max_examples=50)
def test_simplerdbms_rdbmsschema_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_RdbmsSchema)

@given(instance=SimpleRDBMS_RdbmsTable_strategy)
@settings(max_examples=50)
def test_simplerdbms_rdbmstable_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_RdbmsTable)

@given(instance=SimpleRDBMS_RdbmsColumn_strategy)
@settings(max_examples=50)
def test_simplerdbms_rdbmscolumn_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_RdbmsColumn)



@given(instance=SimpleRDBMS_RdbmsColumn_strategy)
def test_simplerdbms_rdbmscolumn_rdbmsType_setter(instance):
    original = instance.rdbmsType
    instance.rdbmsType = original
    assert instance.rdbmsType == original

@given(instance=SimpleRDBMS_RdbmsForeignKey_strategy)
@settings(max_examples=50)
def test_simplerdbms_rdbmsforeignkey_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_RdbmsForeignKey)
