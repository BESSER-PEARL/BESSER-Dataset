import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metamodel::Cell,
    metamodel::Sequence,
    metamodel::Table,
    metamodel::Database,
    metamodel::Row,
    metamodel::Column,
    metamodel::Constraint,
    ConstraintType,
    Datatype,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodel::cell_is_not_abstract():
    assert not inspect.isabstract(metamodel::Cell)


def test_metamodel::cell_constructor_exists():
    assert callable(metamodel::Cell.__init__)


def test_metamodel::cell_constructor_args():
    sig = inspect.signature(metamodel::Cell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_metamodel::cell_has_value():
    assert hasattr(metamodel::Cell, "value")
    descriptor = None
    for klass in metamodel::Cell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::sequence_is_not_abstract():
    assert not inspect.isabstract(metamodel::Sequence)


def test_metamodel::sequence_constructor_exists():
    assert callable(metamodel::Sequence.__init__)


def test_metamodel::sequence_constructor_args():
    sig = inspect.signature(metamodel::Sequence.__init__)
    params = list(sig.parameters.keys())
    assert "startwith" in params, "Missing parameter 'startwith'"
    assert "currentValue" in params, "Missing parameter 'currentValue'"
    assert "name" in params, "Missing parameter 'name'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "incrementby" in params, "Missing parameter 'incrementby'"
    assert "minValue" in params, "Missing parameter 'minValue'"
    assert "cycle" in params, "Missing parameter 'cycle'"

def test_metamodel::sequence_has_startwith():
    assert hasattr(metamodel::Sequence, "startwith")
    descriptor = None
    for klass in metamodel::Sequence.__mro__:
        if "startwith" in klass.__dict__:
            descriptor = klass.__dict__["startwith"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::sequence_has_currentValue():
    assert hasattr(metamodel::Sequence, "currentValue")
    descriptor = None
    for klass in metamodel::Sequence.__mro__:
        if "currentValue" in klass.__dict__:
            descriptor = klass.__dict__["currentValue"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::sequence_has_name():
    assert hasattr(metamodel::Sequence, "name")
    descriptor = None
    for klass in metamodel::Sequence.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::sequence_has_maxValue():
    assert hasattr(metamodel::Sequence, "maxValue")
    descriptor = None
    for klass in metamodel::Sequence.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::sequence_has_incrementby():
    assert hasattr(metamodel::Sequence, "incrementby")
    descriptor = None
    for klass in metamodel::Sequence.__mro__:
        if "incrementby" in klass.__dict__:
            descriptor = klass.__dict__["incrementby"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::sequence_has_minValue():
    assert hasattr(metamodel::Sequence, "minValue")
    descriptor = None
    for klass in metamodel::Sequence.__mro__:
        if "minValue" in klass.__dict__:
            descriptor = klass.__dict__["minValue"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::sequence_has_cycle():
    assert hasattr(metamodel::Sequence, "cycle")
    descriptor = None
    for klass in metamodel::Sequence.__mro__:
        if "cycle" in klass.__dict__:
            descriptor = klass.__dict__["cycle"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::table_is_not_abstract():
    assert not inspect.isabstract(metamodel::Table)


def test_metamodel::table_constructor_exists():
    assert callable(metamodel::Table.__init__)


def test_metamodel::table_constructor_args():
    sig = inspect.signature(metamodel::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::table_has_name():
    assert hasattr(metamodel::Table, "name")
    descriptor = None
    for klass in metamodel::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::database_is_not_abstract():
    assert not inspect.isabstract(metamodel::Database)


def test_metamodel::database_constructor_exists():
    assert callable(metamodel::Database.__init__)


def test_metamodel::database_constructor_args():
    sig = inspect.signature(metamodel::Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::database_has_name():
    assert hasattr(metamodel::Database, "name")
    descriptor = None
    for klass in metamodel::Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::row_is_not_abstract():
    assert not inspect.isabstract(metamodel::Row)


def test_metamodel::row_constructor_exists():
    assert callable(metamodel::Row.__init__)


def test_metamodel::row_constructor_args():
    sig = inspect.signature(metamodel::Row.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::column_is_not_abstract():
    assert not inspect.isabstract(metamodel::Column)


def test_metamodel::column_constructor_exists():
    assert callable(metamodel::Column.__init__)


def test_metamodel::column_constructor_args():
    sig = inspect.signature(metamodel::Column.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "nullable" in params, "Missing parameter 'nullable'"

def test_metamodel::column_has_size():
    assert hasattr(metamodel::Column, "size")
    descriptor = None
    for klass in metamodel::Column.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::column_has_name():
    assert hasattr(metamodel::Column, "name")
    descriptor = None
    for klass in metamodel::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::column_has_type():
    assert hasattr(metamodel::Column, "type")
    descriptor = None
    for klass in metamodel::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::column_has_nullable():
    assert hasattr(metamodel::Column, "nullable")
    descriptor = None
    for klass in metamodel::Column.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::constraint_is_not_abstract():
    assert not inspect.isabstract(metamodel::Constraint)


def test_metamodel::constraint_constructor_exists():
    assert callable(metamodel::Constraint.__init__)


def test_metamodel::constraint_constructor_args():
    sig = inspect.signature(metamodel::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "type" in params, "Missing parameter 'type'"

def test_metamodel::constraint_has_name():
    assert hasattr(metamodel::Constraint, "name")
    descriptor = None
    for klass in metamodel::Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::constraint_has_reference():
    assert hasattr(metamodel::Constraint, "reference")
    descriptor = None
    for klass in metamodel::Constraint.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::constraint_has_type():
    assert hasattr(metamodel::Constraint, "type")
    descriptor = None
    for klass in metamodel::Constraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_constrainttype_exists():
    # Check that the Enumeration exists
    assert ConstraintType is not None

def test_constrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintType]
    expected_literals = [
        "PRIMARY_KEY",
        "FOREIGN_KEY",
        "COMPOSITE_PRIMARY_KEY",
        "UNIQUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConstraintType"

def test_datatype_exists():
    # Check that the Enumeration exists
    assert Datatype is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Datatype]
    expected_literals = [
        "TIMESTAMP",
        "DOUBLE",
        "CHAR",
        "FLOAT",
        "STRING",
        "VARCHAR",
        "BIGINT",
        "BOOLEAN",
        "DATE",
        "DECIMAL",
        "INT",
        "TEXT",
        "TINYTEXT",
        "LONGTEXT",
        "SMALLINT",
        "BLOB",
        "DATETIME",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Datatype"


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
metamodel::Cell_strategy = st.builds(
    metamodel::Cell,
    value=
        safe_text
)
metamodel::Sequence_strategy = st.builds(
    metamodel::Sequence,
    startwith=
        safe_text,
    currentValue=
        safe_text,
    name=
        safe_text,
    maxValue=
        safe_text,
    incrementby=
        st.integers(),
    minValue=
        st.integers(),
    cycle=
        st.booleans()
)
metamodel::Table_strategy = st.builds(
    metamodel::Table,
    name=
        safe_text
)
metamodel::Database_strategy = st.builds(
    metamodel::Database,
    name=
        safe_text
)
metamodel::Row_strategy = st.builds(
    metamodel::Row,
)
metamodel::Column_strategy = st.builds(
    metamodel::Column,
    size=
        safe_text,
    name=
        safe_text,
    type=
        safe_text,
    nullable=
        st.booleans()
)
metamodel::Constraint_strategy = st.builds(
    metamodel::Constraint,
    name=
        safe_text,
    reference=
        safe_text,
    type=
        safe_text
)

@given(instance=metamodel::Cell_strategy)
@settings(max_examples=50)
def test_metamodel::cell_instantiation(instance):
    assert isinstance(instance, metamodel::Cell)

@given(instance=metamodel::Cell_strategy)
def test_metamodel::cell_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=metamodel::Cell_strategy)
def test_metamodel::cell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=metamodel::Sequence_strategy)
@settings(max_examples=50)
def test_metamodel::sequence_instantiation(instance):
    assert isinstance(instance, metamodel::Sequence)

@given(instance=metamodel::Sequence_strategy)
def test_metamodel::sequence_startwith_type(instance):
    assert isinstance(instance.startwith, str)


@given(instance=metamodel::Sequence_strategy)
def test_metamodel::sequence_startwith_setter(instance):
    original = instance.startwith
    instance.startwith = original
    assert instance.startwith == original

@given(instance=metamodel::Sequence_strategy)
def test_metamodel::sequence_currentValue_type(instance):
    assert isinstance(instance.currentValue, str)


@given(instance=metamodel::Sequence_strategy)
def test_metamodel::sequence_currentValue_setter(instance):
    original = instance.currentValue
    instance.currentValue = original
    assert instance.currentValue == original

@given(instance=metamodel::Sequence_strategy)
def test_metamodel::sequence_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Sequence_strategy)
def test_metamodel::sequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::Sequence_strategy)
def test_metamodel::sequence_maxValue_type(instance):
    assert isinstance(instance.maxValue, str)


@given(instance=metamodel::Sequence_strategy)
def test_metamodel::sequence_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original

@given(instance=metamodel::Sequence_strategy)
def test_metamodel::sequence_incrementby_type(instance):
    assert isinstance(instance.incrementby, int)


@given(instance=metamodel::Sequence_strategy)
def test_metamodel::sequence_incrementby_setter(instance):
    original = instance.incrementby
    instance.incrementby = original
    assert instance.incrementby == original

@given(instance=metamodel::Sequence_strategy)
def test_metamodel::sequence_minValue_type(instance):
    assert isinstance(instance.minValue, int)


@given(instance=metamodel::Sequence_strategy)
def test_metamodel::sequence_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original

@given(instance=metamodel::Sequence_strategy)
def test_metamodel::sequence_cycle_type(instance):
    assert isinstance(instance.cycle, bool)


@given(instance=metamodel::Sequence_strategy)
def test_metamodel::sequence_cycle_setter(instance):
    original = instance.cycle
    instance.cycle = original
    assert instance.cycle == original

@given(instance=metamodel::Table_strategy)
@settings(max_examples=50)
def test_metamodel::table_instantiation(instance):
    assert isinstance(instance, metamodel::Table)

@given(instance=metamodel::Table_strategy)
def test_metamodel::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Table_strategy)
def test_metamodel::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::Database_strategy)
@settings(max_examples=50)
def test_metamodel::database_instantiation(instance):
    assert isinstance(instance, metamodel::Database)

@given(instance=metamodel::Database_strategy)
def test_metamodel::database_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Database_strategy)
def test_metamodel::database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::Row_strategy)
@settings(max_examples=50)
def test_metamodel::row_instantiation(instance):
    assert isinstance(instance, metamodel::Row)

@given(instance=metamodel::Column_strategy)
@settings(max_examples=50)
def test_metamodel::column_instantiation(instance):
    assert isinstance(instance, metamodel::Column)

@given(instance=metamodel::Column_strategy)
def test_metamodel::column_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=metamodel::Column_strategy)
def test_metamodel::column_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=metamodel::Column_strategy)
def test_metamodel::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Column_strategy)
def test_metamodel::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::Column_strategy)
def test_metamodel::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=metamodel::Column_strategy)
def test_metamodel::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=metamodel::Column_strategy)
def test_metamodel::column_nullable_type(instance):
    assert isinstance(instance.nullable, bool)


@given(instance=metamodel::Column_strategy)
def test_metamodel::column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=metamodel::Constraint_strategy)
@settings(max_examples=50)
def test_metamodel::constraint_instantiation(instance):
    assert isinstance(instance, metamodel::Constraint)

@given(instance=metamodel::Constraint_strategy)
def test_metamodel::constraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Constraint_strategy)
def test_metamodel::constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::Constraint_strategy)
def test_metamodel::constraint_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=metamodel::Constraint_strategy)
def test_metamodel::constraint_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=metamodel::Constraint_strategy)
def test_metamodel::constraint_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=metamodel::Constraint_strategy)
def test_metamodel::constraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
