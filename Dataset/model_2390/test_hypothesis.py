import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    simpleRDBMS_Table,
    simpleRDBMS_Key,
    simpleRDBMS_Column,
    simpleRDBMS_ForeignKey,
    simpleRDBMS_Schema,
    simpleRDBMS_NamedElement,
    simpleRDBMS_RDBMSModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_table_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS_Table)


def test_simplerdbms_table_constructor_exists():
    assert callable(simpleRDBMS_Table.__init__)


def test_simplerdbms_table_constructor_args():
    sig = inspect.signature(simpleRDBMS_Table.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_key_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS_Key)


def test_simplerdbms_key_constructor_exists():
    assert callable(simpleRDBMS_Key.__init__)


def test_simplerdbms_key_constructor_args():
    sig = inspect.signature(simpleRDBMS_Key.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_column_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS_Column)


def test_simplerdbms_column_constructor_exists():
    assert callable(simpleRDBMS_Column.__init__)


def test_simplerdbms_column_constructor_args():
    sig = inspect.signature(simpleRDBMS_Column.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_foreignkey_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS_ForeignKey)


def test_simplerdbms_foreignkey_constructor_exists():
    assert callable(simpleRDBMS_ForeignKey.__init__)


def test_simplerdbms_foreignkey_constructor_args():
    sig = inspect.signature(simpleRDBMS_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_schema_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS_Schema)


def test_simplerdbms_schema_constructor_exists():
    assert callable(simpleRDBMS_Schema.__init__)


def test_simplerdbms_schema_constructor_args():
    sig = inspect.signature(simpleRDBMS_Schema.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_namedelement_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS_NamedElement)


def test_simplerdbms_namedelement_constructor_exists():
    assert callable(simpleRDBMS_NamedElement.__init__)


def test_simplerdbms_namedelement_constructor_args():
    sig = inspect.signature(simpleRDBMS_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplerdbms_namedelement_has_name():
    assert hasattr(simpleRDBMS_NamedElement, "name")
    descriptor = None
    for klass in simpleRDBMS_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplerdbms_rdbmsmodel_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS_RDBMSModel)


def test_simplerdbms_rdbmsmodel_constructor_exists():
    assert callable(simpleRDBMS_RDBMSModel.__init__)


def test_simplerdbms_rdbmsmodel_constructor_args():
    sig = inspect.signature(simpleRDBMS_RDBMSModel.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
simpleRDBMS_Table_strategy = st.builds(
    simpleRDBMS_Table,
)
simpleRDBMS_Key_strategy = st.builds(
    simpleRDBMS_Key,
)
simpleRDBMS_Column_strategy = st.builds(
    simpleRDBMS_Column,
)
simpleRDBMS_ForeignKey_strategy = st.builds(
    simpleRDBMS_ForeignKey,
)
simpleRDBMS_Schema_strategy = st.builds(
    simpleRDBMS_Schema,
)
simpleRDBMS_NamedElement_strategy = st.builds(
    simpleRDBMS_NamedElement,
    name=
        safe_text
)
simpleRDBMS_RDBMSModel_strategy = st.builds(
    simpleRDBMS_RDBMSModel,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simpleRDBMS_Table_strategy)
@settings(max_examples=50)
def test_simplerdbms_table_instantiation(instance):
    assert isinstance(instance, simpleRDBMS_Table)

@given(instance=simpleRDBMS_Key_strategy)
@settings(max_examples=50)
def test_simplerdbms_key_instantiation(instance):
    assert isinstance(instance, simpleRDBMS_Key)

@given(instance=simpleRDBMS_Column_strategy)
@settings(max_examples=50)
def test_simplerdbms_column_instantiation(instance):
    assert isinstance(instance, simpleRDBMS_Column)

@given(instance=simpleRDBMS_ForeignKey_strategy)
@settings(max_examples=50)
def test_simplerdbms_foreignkey_instantiation(instance):
    assert isinstance(instance, simpleRDBMS_ForeignKey)

@given(instance=simpleRDBMS_Schema_strategy)
@settings(max_examples=50)
def test_simplerdbms_schema_instantiation(instance):
    assert isinstance(instance, simpleRDBMS_Schema)

@given(instance=simpleRDBMS_NamedElement_strategy)
@settings(max_examples=50)
def test_simplerdbms_namedelement_instantiation(instance):
    assert isinstance(instance, simpleRDBMS_NamedElement)



@given(instance=simpleRDBMS_NamedElement_strategy)
def test_simplerdbms_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleRDBMS_RDBMSModel_strategy)
@settings(max_examples=50)
def test_simplerdbms_rdbmsmodel_instantiation(instance):
    assert isinstance(instance, simpleRDBMS_RDBMSModel)
