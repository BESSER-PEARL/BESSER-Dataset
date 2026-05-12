import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RelationalDBContent::TupleElement,
    TupleElement,
    RelationalDBContent::Tuple,
    Tuple,
    DataBase,
    Table,
    NamedElement,
    RelationalDBContent::Table,
    RelationalDBContent::DataBase,
    RelationalDBContent::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relationaldbcontent::tupleelement_is_not_abstract():
    assert not inspect.isabstract(RelationalDBContent::TupleElement)


def test_relationaldbcontent::tupleelement_constructor_exists():
    assert callable(RelationalDBContent::TupleElement.__init__)


def test_relationaldbcontent::tupleelement_constructor_args():
    sig = inspect.signature(RelationalDBContent::TupleElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_relationaldbcontent::tupleelement_has_value():
    assert hasattr(RelationalDBContent::TupleElement, "value")
    descriptor = None
    for klass in RelationalDBContent::TupleElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tupleelement_is_not_abstract():
    assert not inspect.isabstract(TupleElement)


def test_tupleelement_constructor_exists():
    assert callable(TupleElement.__init__)


def test_tupleelement_constructor_args():
    sig = inspect.signature(TupleElement.__init__)
    params = list(sig.parameters.keys())



def test_relationaldbcontent::tuple_is_not_abstract():
    assert not inspect.isabstract(RelationalDBContent::Tuple)


def test_relationaldbcontent::tuple_constructor_exists():
    assert callable(RelationalDBContent::Tuple.__init__)


def test_relationaldbcontent::tuple_constructor_args():
    sig = inspect.signature(RelationalDBContent::Tuple.__init__)
    params = list(sig.parameters.keys())



def test_tuple_is_not_abstract():
    assert not inspect.isabstract(Tuple)


def test_tuple_constructor_exists():
    assert callable(Tuple.__init__)


def test_tuple_constructor_args():
    sig = inspect.signature(Tuple.__init__)
    params = list(sig.parameters.keys())



def test_database_is_not_abstract():
    assert not inspect.isabstract(DataBase)


def test_database_constructor_exists():
    assert callable(DataBase.__init__)


def test_database_constructor_args():
    sig = inspect.signature(DataBase.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_relationaldbcontent::table_is_not_abstract():
    assert not inspect.isabstract(RelationalDBContent::Table)


def test_relationaldbcontent::table_constructor_exists():
    assert callable(RelationalDBContent::Table.__init__)


def test_relationaldbcontent::table_constructor_args():
    sig = inspect.signature(RelationalDBContent::Table.__init__)
    params = list(sig.parameters.keys())



def test_relationaldbcontent::database_is_not_abstract():
    assert not inspect.isabstract(RelationalDBContent::DataBase)


def test_relationaldbcontent::database_constructor_exists():
    assert callable(RelationalDBContent::DataBase.__init__)


def test_relationaldbcontent::database_constructor_args():
    sig = inspect.signature(RelationalDBContent::DataBase.__init__)
    params = list(sig.parameters.keys())
    assert "SGBDname" in params, "Missing parameter 'SGBDname'"

def test_relationaldbcontent::database_has_SGBDname():
    assert hasattr(RelationalDBContent::DataBase, "SGBDname")
    descriptor = None
    for klass in RelationalDBContent::DataBase.__mro__:
        if "SGBDname" in klass.__dict__:
            descriptor = klass.__dict__["SGBDname"]
            break
    assert isinstance(descriptor, property)



def test_relationaldbcontent::namedelement_is_not_abstract():
    assert not inspect.isabstract(RelationalDBContent::NamedElement)


def test_relationaldbcontent::namedelement_constructor_exists():
    assert callable(RelationalDBContent::NamedElement.__init__)


def test_relationaldbcontent::namedelement_constructor_args():
    sig = inspect.signature(RelationalDBContent::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relationaldbcontent::namedelement_has_name():
    assert hasattr(RelationalDBContent::NamedElement, "name")
    descriptor = None
    for klass in RelationalDBContent::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
RelationalDBContent::TupleElement_strategy = st.builds(
    RelationalDBContent::TupleElement,
    value=
        safe_text
)
TupleElement_strategy = st.builds(
    TupleElement,
)
RelationalDBContent::Tuple_strategy = st.builds(
    RelationalDBContent::Tuple,
)
Tuple_strategy = st.builds(
    Tuple,
)
DataBase_strategy = st.builds(
    DataBase,
)
Table_strategy = st.builds(
    Table,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
RelationalDBContent::Table_strategy = st.builds(
    RelationalDBContent::Table,
)
RelationalDBContent::DataBase_strategy = st.builds(
    RelationalDBContent::DataBase,
    SGBDname=
        safe_text
)
RelationalDBContent::NamedElement_strategy = st.builds(
    RelationalDBContent::NamedElement,
    name=
        safe_text
)

@given(instance=RelationalDBContent::TupleElement_strategy)
@settings(max_examples=50)
def test_relationaldbcontent::tupleelement_instantiation(instance):
    assert isinstance(instance, RelationalDBContent::TupleElement)

@given(instance=RelationalDBContent::TupleElement_strategy)
def test_relationaldbcontent::tupleelement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=RelationalDBContent::TupleElement_strategy)
def test_relationaldbcontent::tupleelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TupleElement_strategy)
@settings(max_examples=50)
def test_tupleelement_instantiation(instance):
    assert isinstance(instance, TupleElement)

@given(instance=RelationalDBContent::Tuple_strategy)
@settings(max_examples=50)
def test_relationaldbcontent::tuple_instantiation(instance):
    assert isinstance(instance, RelationalDBContent::Tuple)

@given(instance=Tuple_strategy)
@settings(max_examples=50)
def test_tuple_instantiation(instance):
    assert isinstance(instance, Tuple)

@given(instance=DataBase_strategy)
@settings(max_examples=50)
def test_database_instantiation(instance):
    assert isinstance(instance, DataBase)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=RelationalDBContent::Table_strategy)
@settings(max_examples=50)
def test_relationaldbcontent::table_instantiation(instance):
    assert isinstance(instance, RelationalDBContent::Table)

@given(instance=RelationalDBContent::DataBase_strategy)
@settings(max_examples=50)
def test_relationaldbcontent::database_instantiation(instance):
    assert isinstance(instance, RelationalDBContent::DataBase)

@given(instance=RelationalDBContent::DataBase_strategy)
def test_relationaldbcontent::database_SGBDname_type(instance):
    assert isinstance(instance.SGBDname, str)


@given(instance=RelationalDBContent::DataBase_strategy)
def test_relationaldbcontent::database_SGBDname_setter(instance):
    original = instance.SGBDname
    instance.SGBDname = original
    assert instance.SGBDname == original

@given(instance=RelationalDBContent::NamedElement_strategy)
@settings(max_examples=50)
def test_relationaldbcontent::namedelement_instantiation(instance):
    assert isinstance(instance, RelationalDBContent::NamedElement)

@given(instance=RelationalDBContent::NamedElement_strategy)
def test_relationaldbcontent::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RelationalDBContent::NamedElement_strategy)
def test_relationaldbcontent::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
