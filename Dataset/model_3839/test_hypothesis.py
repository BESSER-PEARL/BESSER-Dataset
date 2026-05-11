import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BinaryCondition,
    sql4csv::OrCondition,
    sql4csv::AndCondition,
    sql4csv::ValueEquality,
    sql4csv::ColumnEquality,
    sql4csv::Condition,
    sql4csv::Table,
    sql4csv::Column,
    sql4csv::Query,
    sql4csv::EObject,
    sql4csv::Program,
    sql4csv::SQL4CSV,
    Condition,
    sql4csv::BinaryCondition,
    sql4csv::Equality,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binarycondition_is_not_abstract():
    assert not inspect.isabstract(BinaryCondition)


def test_binarycondition_constructor_exists():
    assert callable(BinaryCondition.__init__)


def test_binarycondition_constructor_args():
    sig = inspect.signature(BinaryCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql4csv::orcondition_is_not_abstract():
    assert not inspect.isabstract(sql4csv::OrCondition)


def test_sql4csv::orcondition_constructor_exists():
    assert callable(sql4csv::OrCondition.__init__)


def test_sql4csv::orcondition_constructor_args():
    sig = inspect.signature(sql4csv::OrCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql4csv::andcondition_is_not_abstract():
    assert not inspect.isabstract(sql4csv::AndCondition)


def test_sql4csv::andcondition_constructor_exists():
    assert callable(sql4csv::AndCondition.__init__)


def test_sql4csv::andcondition_constructor_args():
    sig = inspect.signature(sql4csv::AndCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql4csv::valueequality_is_not_abstract():
    assert not inspect.isabstract(sql4csv::ValueEquality)


def test_sql4csv::valueequality_constructor_exists():
    assert callable(sql4csv::ValueEquality.__init__)


def test_sql4csv::valueequality_constructor_args():
    sig = inspect.signature(sql4csv::ValueEquality.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"

def test_sql4csv::valueequality_has_right():
    assert hasattr(sql4csv::ValueEquality, "right")
    descriptor = None
    for klass in sql4csv::ValueEquality.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)



def test_sql4csv::columnequality_is_not_abstract():
    assert not inspect.isabstract(sql4csv::ColumnEquality)


def test_sql4csv::columnequality_constructor_exists():
    assert callable(sql4csv::ColumnEquality.__init__)


def test_sql4csv::columnequality_constructor_args():
    sig = inspect.signature(sql4csv::ColumnEquality.__init__)
    params = list(sig.parameters.keys())



def test_sql4csv::condition_is_not_abstract():
    assert not inspect.isabstract(sql4csv::Condition)


def test_sql4csv::condition_constructor_exists():
    assert callable(sql4csv::Condition.__init__)


def test_sql4csv::condition_constructor_args():
    sig = inspect.signature(sql4csv::Condition.__init__)
    params = list(sig.parameters.keys())



def test_sql4csv::table_is_not_abstract():
    assert not inspect.isabstract(sql4csv::Table)


def test_sql4csv::table_constructor_exists():
    assert callable(sql4csv::Table.__init__)


def test_sql4csv::table_constructor_args():
    sig = inspect.signature(sql4csv::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql4csv::table_has_name():
    assert hasattr(sql4csv::Table, "name")
    descriptor = None
    for klass in sql4csv::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql4csv::column_is_not_abstract():
    assert not inspect.isabstract(sql4csv::Column)


def test_sql4csv::column_constructor_exists():
    assert callable(sql4csv::Column.__init__)


def test_sql4csv::column_constructor_args():
    sig = inspect.signature(sql4csv::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql4csv::column_has_name():
    assert hasattr(sql4csv::Column, "name")
    descriptor = None
    for klass in sql4csv::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql4csv::query_is_not_abstract():
    assert not inspect.isabstract(sql4csv::Query)


def test_sql4csv::query_constructor_exists():
    assert callable(sql4csv::Query.__init__)


def test_sql4csv::query_constructor_args():
    sig = inspect.signature(sql4csv::Query.__init__)
    params = list(sig.parameters.keys())



def test_sql4csv::eobject_is_not_abstract():
    assert not inspect.isabstract(sql4csv::EObject)


def test_sql4csv::eobject_constructor_exists():
    assert callable(sql4csv::EObject.__init__)


def test_sql4csv::eobject_constructor_args():
    sig = inspect.signature(sql4csv::EObject.__init__)
    params = list(sig.parameters.keys())



def test_sql4csv::program_is_not_abstract():
    assert not inspect.isabstract(sql4csv::Program)


def test_sql4csv::program_constructor_exists():
    assert callable(sql4csv::Program.__init__)


def test_sql4csv::program_constructor_args():
    sig = inspect.signature(sql4csv::Program.__init__)
    params = list(sig.parameters.keys())



def test_sql4csv::sql4csv_is_not_abstract():
    assert not inspect.isabstract(sql4csv::SQL4CSV)


def test_sql4csv::sql4csv_constructor_exists():
    assert callable(sql4csv::SQL4CSV.__init__)


def test_sql4csv::sql4csv_constructor_args():
    sig = inspect.signature(sql4csv::SQL4CSV.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_sql4csv::binarycondition_is_not_abstract():
    assert not inspect.isabstract(sql4csv::BinaryCondition)


def test_sql4csv::binarycondition_constructor_exists():
    assert callable(sql4csv::BinaryCondition.__init__)


def test_sql4csv::binarycondition_constructor_args():
    sig = inspect.signature(sql4csv::BinaryCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql4csv::equality_is_not_abstract():
    assert not inspect.isabstract(sql4csv::Equality)


def test_sql4csv::equality_constructor_exists():
    assert callable(sql4csv::Equality.__init__)


def test_sql4csv::equality_constructor_args():
    sig = inspect.signature(sql4csv::Equality.__init__)
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
BinaryCondition_strategy = st.builds(
    BinaryCondition,
)
sql4csv::OrCondition_strategy = st.builds(
    sql4csv::OrCondition,
)
sql4csv::AndCondition_strategy = st.builds(
    sql4csv::AndCondition,
)
sql4csv::ValueEquality_strategy = st.builds(
    sql4csv::ValueEquality,
    right=
        safe_text
)
sql4csv::ColumnEquality_strategy = st.builds(
    sql4csv::ColumnEquality,
)
sql4csv::Condition_strategy = st.builds(
    sql4csv::Condition,
)
sql4csv::Table_strategy = st.builds(
    sql4csv::Table,
    name=
        safe_text
)
sql4csv::Column_strategy = st.builds(
    sql4csv::Column,
    name=
        safe_text
)
sql4csv::Query_strategy = st.builds(
    sql4csv::Query,
)
sql4csv::EObject_strategy = st.builds(
    sql4csv::EObject,
)
sql4csv::Program_strategy = st.builds(
    sql4csv::Program,
)
sql4csv::SQL4CSV_strategy = st.builds(
    sql4csv::SQL4CSV,
)
Condition_strategy = st.builds(
    Condition,
)
sql4csv::BinaryCondition_strategy = st.builds(
    sql4csv::BinaryCondition,
)
sql4csv::Equality_strategy = st.builds(
    sql4csv::Equality,
)

@given(instance=BinaryCondition_strategy)
@settings(max_examples=50)
def test_binarycondition_instantiation(instance):
    assert isinstance(instance, BinaryCondition)

@given(instance=sql4csv::OrCondition_strategy)
@settings(max_examples=50)
def test_sql4csv::orcondition_instantiation(instance):
    assert isinstance(instance, sql4csv::OrCondition)

@given(instance=sql4csv::AndCondition_strategy)
@settings(max_examples=50)
def test_sql4csv::andcondition_instantiation(instance):
    assert isinstance(instance, sql4csv::AndCondition)

@given(instance=sql4csv::ValueEquality_strategy)
@settings(max_examples=50)
def test_sql4csv::valueequality_instantiation(instance):
    assert isinstance(instance, sql4csv::ValueEquality)

@given(instance=sql4csv::ValueEquality_strategy)
def test_sql4csv::valueequality_right_type(instance):
    assert isinstance(instance.right, str)


@given(instance=sql4csv::ValueEquality_strategy)
def test_sql4csv::valueequality_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=sql4csv::ColumnEquality_strategy)
@settings(max_examples=50)
def test_sql4csv::columnequality_instantiation(instance):
    assert isinstance(instance, sql4csv::ColumnEquality)

@given(instance=sql4csv::Condition_strategy)
@settings(max_examples=50)
def test_sql4csv::condition_instantiation(instance):
    assert isinstance(instance, sql4csv::Condition)

@given(instance=sql4csv::Table_strategy)
@settings(max_examples=50)
def test_sql4csv::table_instantiation(instance):
    assert isinstance(instance, sql4csv::Table)

@given(instance=sql4csv::Table_strategy)
def test_sql4csv::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sql4csv::Table_strategy)
def test_sql4csv::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sql4csv::Column_strategy)
@settings(max_examples=50)
def test_sql4csv::column_instantiation(instance):
    assert isinstance(instance, sql4csv::Column)

@given(instance=sql4csv::Column_strategy)
def test_sql4csv::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sql4csv::Column_strategy)
def test_sql4csv::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sql4csv::Query_strategy)
@settings(max_examples=50)
def test_sql4csv::query_instantiation(instance):
    assert isinstance(instance, sql4csv::Query)

@given(instance=sql4csv::EObject_strategy)
@settings(max_examples=50)
def test_sql4csv::eobject_instantiation(instance):
    assert isinstance(instance, sql4csv::EObject)

@given(instance=sql4csv::Program_strategy)
@settings(max_examples=50)
def test_sql4csv::program_instantiation(instance):
    assert isinstance(instance, sql4csv::Program)

@given(instance=sql4csv::SQL4CSV_strategy)
@settings(max_examples=50)
def test_sql4csv::sql4csv_instantiation(instance):
    assert isinstance(instance, sql4csv::SQL4CSV)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=sql4csv::BinaryCondition_strategy)
@settings(max_examples=50)
def test_sql4csv::binarycondition_instantiation(instance):
    assert isinstance(instance, sql4csv::BinaryCondition)

@given(instance=sql4csv::Equality_strategy)
@settings(max_examples=50)
def test_sql4csv::equality_instantiation(instance):
    assert isinstance(instance, sql4csv::Equality)
