import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SimpleRDBMS::RdbmsModelElement,
    RdbmsModelElement,
    SimpleRDBMS::RdbmsSchema,
    SimpleRDBMS::RdbmsTable,
    SimpleRDBMS::RdbmsKey,
    SimpleRDBMS::RdbmsForeignKey,
    SimpleRDBMS::RdbmsColumn,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplerdbms::rdbmsmodelelement_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::RdbmsModelElement)


def test_simplerdbms::rdbmsmodelelement_constructor_exists():
    assert callable(SimpleRDBMS::RdbmsModelElement.__init__)


def test_simplerdbms::rdbmsmodelelement_constructor_args():
    sig = inspect.signature(SimpleRDBMS::RdbmsModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "rdbmsKind" in params, "Missing parameter 'rdbmsKind'"
    assert "id" in params, "Missing parameter 'id'"
    assert "rdbmsName" in params, "Missing parameter 'rdbmsName'"

def test_simplerdbms::rdbmsmodelelement_has_rdbmsKind():
    assert hasattr(SimpleRDBMS::RdbmsModelElement, "rdbmsKind")
    descriptor = None
    for klass in SimpleRDBMS::RdbmsModelElement.__mro__:
        if "rdbmsKind" in klass.__dict__:
            descriptor = klass.__dict__["rdbmsKind"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms::rdbmsmodelelement_has_id():
    assert hasattr(SimpleRDBMS::RdbmsModelElement, "id")
    descriptor = None
    for klass in SimpleRDBMS::RdbmsModelElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms::rdbmsmodelelement_has_rdbmsName():
    assert hasattr(SimpleRDBMS::RdbmsModelElement, "rdbmsName")
    descriptor = None
    for klass in SimpleRDBMS::RdbmsModelElement.__mro__:
        if "rdbmsName" in klass.__dict__:
            descriptor = klass.__dict__["rdbmsName"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsmodelelement_is_not_abstract():
    assert not inspect.isabstract(RdbmsModelElement)


def test_rdbmsmodelelement_constructor_exists():
    assert callable(RdbmsModelElement.__init__)


def test_rdbmsmodelelement_constructor_args():
    sig = inspect.signature(RdbmsModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::rdbmsschema_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::RdbmsSchema)


def test_simplerdbms::rdbmsschema_constructor_exists():
    assert callable(SimpleRDBMS::RdbmsSchema.__init__)


def test_simplerdbms::rdbmsschema_constructor_args():
    sig = inspect.signature(SimpleRDBMS::RdbmsSchema.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::rdbmstable_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::RdbmsTable)


def test_simplerdbms::rdbmstable_constructor_exists():
    assert callable(SimpleRDBMS::RdbmsTable.__init__)


def test_simplerdbms::rdbmstable_constructor_args():
    sig = inspect.signature(SimpleRDBMS::RdbmsTable.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::rdbmskey_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::RdbmsKey)


def test_simplerdbms::rdbmskey_constructor_exists():
    assert callable(SimpleRDBMS::RdbmsKey.__init__)


def test_simplerdbms::rdbmskey_constructor_args():
    sig = inspect.signature(SimpleRDBMS::RdbmsKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::rdbmsforeignkey_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::RdbmsForeignKey)


def test_simplerdbms::rdbmsforeignkey_constructor_exists():
    assert callable(SimpleRDBMS::RdbmsForeignKey.__init__)


def test_simplerdbms::rdbmsforeignkey_constructor_args():
    sig = inspect.signature(SimpleRDBMS::RdbmsForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::rdbmscolumn_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::RdbmsColumn)


def test_simplerdbms::rdbmscolumn_constructor_exists():
    assert callable(SimpleRDBMS::RdbmsColumn.__init__)


def test_simplerdbms::rdbmscolumn_constructor_args():
    sig = inspect.signature(SimpleRDBMS::RdbmsColumn.__init__)
    params = list(sig.parameters.keys())
    assert "rdbmsType" in params, "Missing parameter 'rdbmsType'"

def test_simplerdbms::rdbmscolumn_has_rdbmsType():
    assert hasattr(SimpleRDBMS::RdbmsColumn, "rdbmsType")
    descriptor = None
    for klass in SimpleRDBMS::RdbmsColumn.__mro__:
        if "rdbmsType" in klass.__dict__:
            descriptor = klass.__dict__["rdbmsType"]
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
SimpleRDBMS::RdbmsModelElement_strategy = st.builds(
    SimpleRDBMS::RdbmsModelElement,
    rdbmsKind=
        safe_text,
    id=
        safe_text,
    rdbmsName=
        safe_text
)
RdbmsModelElement_strategy = st.builds(
    RdbmsModelElement,
)
SimpleRDBMS::RdbmsSchema_strategy = st.builds(
    SimpleRDBMS::RdbmsSchema,
)
SimpleRDBMS::RdbmsTable_strategy = st.builds(
    SimpleRDBMS::RdbmsTable,
)
SimpleRDBMS::RdbmsKey_strategy = st.builds(
    SimpleRDBMS::RdbmsKey,
)
SimpleRDBMS::RdbmsForeignKey_strategy = st.builds(
    SimpleRDBMS::RdbmsForeignKey,
)
SimpleRDBMS::RdbmsColumn_strategy = st.builds(
    SimpleRDBMS::RdbmsColumn,
    rdbmsType=
        safe_text
)

@given(instance=SimpleRDBMS::RdbmsModelElement_strategy)
@settings(max_examples=50)
def test_simplerdbms::rdbmsmodelelement_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::RdbmsModelElement)

@given(instance=SimpleRDBMS::RdbmsModelElement_strategy)
def test_simplerdbms::rdbmsmodelelement_rdbmsKind_type(instance):
    assert isinstance(instance.rdbmsKind, str)


@given(instance=SimpleRDBMS::RdbmsModelElement_strategy)
def test_simplerdbms::rdbmsmodelelement_rdbmsKind_setter(instance):
    original = instance.rdbmsKind
    instance.rdbmsKind = original
    assert instance.rdbmsKind == original

@given(instance=SimpleRDBMS::RdbmsModelElement_strategy)
def test_simplerdbms::rdbmsmodelelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=SimpleRDBMS::RdbmsModelElement_strategy)
def test_simplerdbms::rdbmsmodelelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SimpleRDBMS::RdbmsModelElement_strategy)
def test_simplerdbms::rdbmsmodelelement_rdbmsName_type(instance):
    assert isinstance(instance.rdbmsName, str)


@given(instance=SimpleRDBMS::RdbmsModelElement_strategy)
def test_simplerdbms::rdbmsmodelelement_rdbmsName_setter(instance):
    original = instance.rdbmsName
    instance.rdbmsName = original
    assert instance.rdbmsName == original

@given(instance=RdbmsModelElement_strategy)
@settings(max_examples=50)
def test_rdbmsmodelelement_instantiation(instance):
    assert isinstance(instance, RdbmsModelElement)

@given(instance=SimpleRDBMS::RdbmsSchema_strategy)
@settings(max_examples=50)
def test_simplerdbms::rdbmsschema_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::RdbmsSchema)

@given(instance=SimpleRDBMS::RdbmsTable_strategy)
@settings(max_examples=50)
def test_simplerdbms::rdbmstable_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::RdbmsTable)

@given(instance=SimpleRDBMS::RdbmsKey_strategy)
@settings(max_examples=50)
def test_simplerdbms::rdbmskey_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::RdbmsKey)

@given(instance=SimpleRDBMS::RdbmsForeignKey_strategy)
@settings(max_examples=50)
def test_simplerdbms::rdbmsforeignkey_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::RdbmsForeignKey)

@given(instance=SimpleRDBMS::RdbmsColumn_strategy)
@settings(max_examples=50)
def test_simplerdbms::rdbmscolumn_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::RdbmsColumn)

@given(instance=SimpleRDBMS::RdbmsColumn_strategy)
def test_simplerdbms::rdbmscolumn_rdbmsType_type(instance):
    assert isinstance(instance.rdbmsType, str)


@given(instance=SimpleRDBMS::RdbmsColumn_strategy)
def test_simplerdbms::rdbmscolumn_rdbmsType_setter(instance):
    original = instance.rdbmsType
    instance.rdbmsType = original
    assert instance.rdbmsType == original
