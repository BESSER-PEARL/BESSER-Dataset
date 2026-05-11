import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Existence,
    model::NotExists,
    model::Exists,
    model::BooleanOperation,
    model::Condition,
    model::TableAlias,
    model::Table,
    model::ColumnAlias,
    model::Union,
    Condition,
    model::Existence,
    model::Comparison,
    BooleanOperation,
    model::Or,
    model::And,
    ComparisonOperator,
    model::GreaterThan,
    model::LessThan,
    model::NotEquals,
    model::Equals,
    model::ComparisonOperator,
    model::Where,
    model::From,
    model::Column,
    model::Select,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_existence_is_not_abstract():
    assert not inspect.isabstract(Existence)


def test_existence_constructor_exists():
    assert callable(Existence.__init__)


def test_existence_constructor_args():
    sig = inspect.signature(Existence.__init__)
    params = list(sig.parameters.keys())



def test_model::notexists_is_not_abstract():
    assert not inspect.isabstract(model::NotExists)


def test_model::notexists_constructor_exists():
    assert callable(model::NotExists.__init__)


def test_model::notexists_constructor_args():
    sig = inspect.signature(model::NotExists.__init__)
    params = list(sig.parameters.keys())



def test_model::exists_is_not_abstract():
    assert not inspect.isabstract(model::Exists)


def test_model::exists_constructor_exists():
    assert callable(model::Exists.__init__)


def test_model::exists_constructor_args():
    sig = inspect.signature(model::Exists.__init__)
    params = list(sig.parameters.keys())



def test_model::booleanoperation_is_not_abstract():
    assert not inspect.isabstract(model::BooleanOperation)


def test_model::booleanoperation_constructor_exists():
    assert callable(model::BooleanOperation.__init__)


def test_model::booleanoperation_constructor_args():
    sig = inspect.signature(model::BooleanOperation.__init__)
    params = list(sig.parameters.keys())



def test_model::condition_is_not_abstract():
    assert not inspect.isabstract(model::Condition)


def test_model::condition_constructor_exists():
    assert callable(model::Condition.__init__)


def test_model::condition_constructor_args():
    sig = inspect.signature(model::Condition.__init__)
    params = list(sig.parameters.keys())



def test_model::tablealias_is_not_abstract():
    assert not inspect.isabstract(model::TableAlias)


def test_model::tablealias_constructor_exists():
    assert callable(model::TableAlias.__init__)


def test_model::tablealias_constructor_args():
    sig = inspect.signature(model::TableAlias.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::tablealias_has_name():
    assert hasattr(model::TableAlias, "name")
    descriptor = None
    for klass in model::TableAlias.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::table_is_not_abstract():
    assert not inspect.isabstract(model::Table)


def test_model::table_constructor_exists():
    assert callable(model::Table.__init__)


def test_model::table_constructor_args():
    sig = inspect.signature(model::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::table_has_name():
    assert hasattr(model::Table, "name")
    descriptor = None
    for klass in model::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::columnalias_is_not_abstract():
    assert not inspect.isabstract(model::ColumnAlias)


def test_model::columnalias_constructor_exists():
    assert callable(model::ColumnAlias.__init__)


def test_model::columnalias_constructor_args():
    sig = inspect.signature(model::ColumnAlias.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::columnalias_has_name():
    assert hasattr(model::ColumnAlias, "name")
    descriptor = None
    for klass in model::ColumnAlias.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::union_is_not_abstract():
    assert not inspect.isabstract(model::Union)


def test_model::union_constructor_exists():
    assert callable(model::Union.__init__)


def test_model::union_constructor_args():
    sig = inspect.signature(model::Union.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_model::existence_is_not_abstract():
    assert not inspect.isabstract(model::Existence)


def test_model::existence_constructor_exists():
    assert callable(model::Existence.__init__)


def test_model::existence_constructor_args():
    sig = inspect.signature(model::Existence.__init__)
    params = list(sig.parameters.keys())



def test_model::comparison_is_not_abstract():
    assert not inspect.isabstract(model::Comparison)


def test_model::comparison_constructor_exists():
    assert callable(model::Comparison.__init__)


def test_model::comparison_constructor_args():
    sig = inspect.signature(model::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "lhs" in params, "Missing parameter 'lhs'"
    assert "rhs" in params, "Missing parameter 'rhs'"

def test_model::comparison_has_lhs():
    assert hasattr(model::Comparison, "lhs")
    descriptor = None
    for klass in model::Comparison.__mro__:
        if "lhs" in klass.__dict__:
            descriptor = klass.__dict__["lhs"]
            break
    assert isinstance(descriptor, property)

def test_model::comparison_has_rhs():
    assert hasattr(model::Comparison, "rhs")
    descriptor = None
    for klass in model::Comparison.__mro__:
        if "rhs" in klass.__dict__:
            descriptor = klass.__dict__["rhs"]
            break
    assert isinstance(descriptor, property)



def test_booleanoperation_is_not_abstract():
    assert not inspect.isabstract(BooleanOperation)


def test_booleanoperation_constructor_exists():
    assert callable(BooleanOperation.__init__)


def test_booleanoperation_constructor_args():
    sig = inspect.signature(BooleanOperation.__init__)
    params = list(sig.parameters.keys())



def test_model::or_is_not_abstract():
    assert not inspect.isabstract(model::Or)


def test_model::or_constructor_exists():
    assert callable(model::Or.__init__)


def test_model::or_constructor_args():
    sig = inspect.signature(model::Or.__init__)
    params = list(sig.parameters.keys())



def test_model::and_is_not_abstract():
    assert not inspect.isabstract(model::And)


def test_model::and_constructor_exists():
    assert callable(model::And.__init__)


def test_model::and_constructor_args():
    sig = inspect.signature(model::And.__init__)
    params = list(sig.parameters.keys())



def test_comparisonoperator_is_not_abstract():
    assert not inspect.isabstract(ComparisonOperator)


def test_comparisonoperator_constructor_exists():
    assert callable(ComparisonOperator.__init__)


def test_comparisonoperator_constructor_args():
    sig = inspect.signature(ComparisonOperator.__init__)
    params = list(sig.parameters.keys())



def test_model::greaterthan_is_not_abstract():
    assert not inspect.isabstract(model::GreaterThan)


def test_model::greaterthan_constructor_exists():
    assert callable(model::GreaterThan.__init__)


def test_model::greaterthan_constructor_args():
    sig = inspect.signature(model::GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_model::lessthan_is_not_abstract():
    assert not inspect.isabstract(model::LessThan)


def test_model::lessthan_constructor_exists():
    assert callable(model::LessThan.__init__)


def test_model::lessthan_constructor_args():
    sig = inspect.signature(model::LessThan.__init__)
    params = list(sig.parameters.keys())



def test_model::notequals_is_not_abstract():
    assert not inspect.isabstract(model::NotEquals)


def test_model::notequals_constructor_exists():
    assert callable(model::NotEquals.__init__)


def test_model::notequals_constructor_args():
    sig = inspect.signature(model::NotEquals.__init__)
    params = list(sig.parameters.keys())



def test_model::equals_is_not_abstract():
    assert not inspect.isabstract(model::Equals)


def test_model::equals_constructor_exists():
    assert callable(model::Equals.__init__)


def test_model::equals_constructor_args():
    sig = inspect.signature(model::Equals.__init__)
    params = list(sig.parameters.keys())



def test_model::comparisonoperator_is_not_abstract():
    assert not inspect.isabstract(model::ComparisonOperator)


def test_model::comparisonoperator_constructor_exists():
    assert callable(model::ComparisonOperator.__init__)


def test_model::comparisonoperator_constructor_args():
    sig = inspect.signature(model::ComparisonOperator.__init__)
    params = list(sig.parameters.keys())



def test_model::where_is_not_abstract():
    assert not inspect.isabstract(model::Where)


def test_model::where_constructor_exists():
    assert callable(model::Where.__init__)


def test_model::where_constructor_args():
    sig = inspect.signature(model::Where.__init__)
    params = list(sig.parameters.keys())



def test_model::from_is_not_abstract():
    assert not inspect.isabstract(model::From)


def test_model::from_constructor_exists():
    assert callable(model::From.__init__)


def test_model::from_constructor_args():
    sig = inspect.signature(model::From.__init__)
    params = list(sig.parameters.keys())



def test_model::column_is_not_abstract():
    assert not inspect.isabstract(model::Column)


def test_model::column_constructor_exists():
    assert callable(model::Column.__init__)


def test_model::column_constructor_args():
    sig = inspect.signature(model::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::column_has_name():
    assert hasattr(model::Column, "name")
    descriptor = None
    for klass in model::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::select_is_not_abstract():
    assert not inspect.isabstract(model::Select)


def test_model::select_constructor_exists():
    assert callable(model::Select.__init__)


def test_model::select_constructor_args():
    sig = inspect.signature(model::Select.__init__)
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
Existence_strategy = st.builds(
    Existence,
)
model::NotExists_strategy = st.builds(
    model::NotExists,
)
model::Exists_strategy = st.builds(
    model::Exists,
)
model::BooleanOperation_strategy = st.builds(
    model::BooleanOperation,
)
model::Condition_strategy = st.builds(
    model::Condition,
)
model::TableAlias_strategy = st.builds(
    model::TableAlias,
    name=
        safe_text
)
model::Table_strategy = st.builds(
    model::Table,
    name=
        safe_text
)
model::ColumnAlias_strategy = st.builds(
    model::ColumnAlias,
    name=
        safe_text
)
model::Union_strategy = st.builds(
    model::Union,
)
Condition_strategy = st.builds(
    Condition,
)
model::Existence_strategy = st.builds(
    model::Existence,
)
model::Comparison_strategy = st.builds(
    model::Comparison,
    lhs=
        safe_text,
    rhs=
        safe_text
)
BooleanOperation_strategy = st.builds(
    BooleanOperation,
)
model::Or_strategy = st.builds(
    model::Or,
)
model::And_strategy = st.builds(
    model::And,
)
ComparisonOperator_strategy = st.builds(
    ComparisonOperator,
)
model::GreaterThan_strategy = st.builds(
    model::GreaterThan,
)
model::LessThan_strategy = st.builds(
    model::LessThan,
)
model::NotEquals_strategy = st.builds(
    model::NotEquals,
)
model::Equals_strategy = st.builds(
    model::Equals,
)
model::ComparisonOperator_strategy = st.builds(
    model::ComparisonOperator,
)
model::Where_strategy = st.builds(
    model::Where,
)
model::From_strategy = st.builds(
    model::From,
)
model::Column_strategy = st.builds(
    model::Column,
    name=
        safe_text
)
model::Select_strategy = st.builds(
    model::Select,
)

@given(instance=Existence_strategy)
@settings(max_examples=50)
def test_existence_instantiation(instance):
    assert isinstance(instance, Existence)

@given(instance=model::NotExists_strategy)
@settings(max_examples=50)
def test_model::notexists_instantiation(instance):
    assert isinstance(instance, model::NotExists)

@given(instance=model::Exists_strategy)
@settings(max_examples=50)
def test_model::exists_instantiation(instance):
    assert isinstance(instance, model::Exists)

@given(instance=model::BooleanOperation_strategy)
@settings(max_examples=50)
def test_model::booleanoperation_instantiation(instance):
    assert isinstance(instance, model::BooleanOperation)

@given(instance=model::Condition_strategy)
@settings(max_examples=50)
def test_model::condition_instantiation(instance):
    assert isinstance(instance, model::Condition)

@given(instance=model::TableAlias_strategy)
@settings(max_examples=50)
def test_model::tablealias_instantiation(instance):
    assert isinstance(instance, model::TableAlias)

@given(instance=model::TableAlias_strategy)
def test_model::tablealias_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::TableAlias_strategy)
def test_model::tablealias_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Table_strategy)
@settings(max_examples=50)
def test_model::table_instantiation(instance):
    assert isinstance(instance, model::Table)

@given(instance=model::Table_strategy)
def test_model::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Table_strategy)
def test_model::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::ColumnAlias_strategy)
@settings(max_examples=50)
def test_model::columnalias_instantiation(instance):
    assert isinstance(instance, model::ColumnAlias)

@given(instance=model::ColumnAlias_strategy)
def test_model::columnalias_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::ColumnAlias_strategy)
def test_model::columnalias_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Union_strategy)
@settings(max_examples=50)
def test_model::union_instantiation(instance):
    assert isinstance(instance, model::Union)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=model::Existence_strategy)
@settings(max_examples=50)
def test_model::existence_instantiation(instance):
    assert isinstance(instance, model::Existence)

@given(instance=model::Comparison_strategy)
@settings(max_examples=50)
def test_model::comparison_instantiation(instance):
    assert isinstance(instance, model::Comparison)

@given(instance=model::Comparison_strategy)
def test_model::comparison_lhs_type(instance):
    assert isinstance(instance.lhs, str)


@given(instance=model::Comparison_strategy)
def test_model::comparison_lhs_setter(instance):
    original = instance.lhs
    instance.lhs = original
    assert instance.lhs == original

@given(instance=model::Comparison_strategy)
def test_model::comparison_rhs_type(instance):
    assert isinstance(instance.rhs, str)


@given(instance=model::Comparison_strategy)
def test_model::comparison_rhs_setter(instance):
    original = instance.rhs
    instance.rhs = original
    assert instance.rhs == original

@given(instance=BooleanOperation_strategy)
@settings(max_examples=50)
def test_booleanoperation_instantiation(instance):
    assert isinstance(instance, BooleanOperation)

@given(instance=model::Or_strategy)
@settings(max_examples=50)
def test_model::or_instantiation(instance):
    assert isinstance(instance, model::Or)

@given(instance=model::And_strategy)
@settings(max_examples=50)
def test_model::and_instantiation(instance):
    assert isinstance(instance, model::And)

@given(instance=ComparisonOperator_strategy)
@settings(max_examples=50)
def test_comparisonoperator_instantiation(instance):
    assert isinstance(instance, ComparisonOperator)

@given(instance=model::GreaterThan_strategy)
@settings(max_examples=50)
def test_model::greaterthan_instantiation(instance):
    assert isinstance(instance, model::GreaterThan)

@given(instance=model::LessThan_strategy)
@settings(max_examples=50)
def test_model::lessthan_instantiation(instance):
    assert isinstance(instance, model::LessThan)

@given(instance=model::NotEquals_strategy)
@settings(max_examples=50)
def test_model::notequals_instantiation(instance):
    assert isinstance(instance, model::NotEquals)

@given(instance=model::Equals_strategy)
@settings(max_examples=50)
def test_model::equals_instantiation(instance):
    assert isinstance(instance, model::Equals)

@given(instance=model::ComparisonOperator_strategy)
@settings(max_examples=50)
def test_model::comparisonoperator_instantiation(instance):
    assert isinstance(instance, model::ComparisonOperator)

@given(instance=model::Where_strategy)
@settings(max_examples=50)
def test_model::where_instantiation(instance):
    assert isinstance(instance, model::Where)

@given(instance=model::From_strategy)
@settings(max_examples=50)
def test_model::from_instantiation(instance):
    assert isinstance(instance, model::From)

@given(instance=model::Column_strategy)
@settings(max_examples=50)
def test_model::column_instantiation(instance):
    assert isinstance(instance, model::Column)

@given(instance=model::Column_strategy)
def test_model::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Column_strategy)
def test_model::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Select_strategy)
@settings(max_examples=50)
def test_model::select_instantiation(instance):
    assert isinstance(instance, model::Select)
