import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    metamodel_Column,
    metamodel_Constraint,
    metamodel_Cell,
    metamodel_Sequence,
    metamodel_Table,
    metamodel_Database,
    metamodel_Row,
    Datatype,
    ConstraintType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodel_column_is_not_abstract():
    assert not inspect.isabstract(metamodel_Column)


def test_metamodel_column_constructor_exists():
    assert callable(metamodel_Column.__init__)


def test_metamodel_column_constructor_args():
    sig = inspect.signature(metamodel_Column.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel_column_has_size():
    assert hasattr(metamodel_Column, "size")
    descriptor = None
    for klass in metamodel_Column.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_column_has_nullable():
    assert hasattr(metamodel_Column, "nullable")
    descriptor = None
    for klass in metamodel_Column.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_column_has_type():
    assert hasattr(metamodel_Column, "type")
    descriptor = None
    for klass in metamodel_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_column_has_name():
    assert hasattr(metamodel_Column, "name")
    descriptor = None
    for klass in metamodel_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_constraint_is_not_abstract():
    assert not inspect.isabstract(metamodel_Constraint)


def test_metamodel_constraint_constructor_exists():
    assert callable(metamodel_Constraint.__init__)


def test_metamodel_constraint_constructor_args():
    sig = inspect.signature(metamodel_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "reference" in params, "Missing parameter 'reference'"

def test_metamodel_constraint_has_type():
    assert hasattr(metamodel_Constraint, "type")
    descriptor = None
    for klass in metamodel_Constraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_constraint_has_name():
    assert hasattr(metamodel_Constraint, "name")
    descriptor = None
    for klass in metamodel_Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_constraint_has_reference():
    assert hasattr(metamodel_Constraint, "reference")
    descriptor = None
    for klass in metamodel_Constraint.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_cell_is_not_abstract():
    assert not inspect.isabstract(metamodel_Cell)


def test_metamodel_cell_constructor_exists():
    assert callable(metamodel_Cell.__init__)


def test_metamodel_cell_constructor_args():
    sig = inspect.signature(metamodel_Cell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_metamodel_cell_has_value():
    assert hasattr(metamodel_Cell, "value")
    descriptor = None
    for klass in metamodel_Cell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_sequence_is_not_abstract():
    assert not inspect.isabstract(metamodel_Sequence)


def test_metamodel_sequence_constructor_exists():
    assert callable(metamodel_Sequence.__init__)


def test_metamodel_sequence_constructor_args():
    sig = inspect.signature(metamodel_Sequence.__init__)
    params = list(sig.parameters.keys())
    assert "cycle" in params, "Missing parameter 'cycle'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "minValue" in params, "Missing parameter 'minValue'"
    assert "incrementby" in params, "Missing parameter 'incrementby'"
    assert "startwith" in params, "Missing parameter 'startwith'"
    assert "currentValue" in params, "Missing parameter 'currentValue'"
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel_sequence_has_cycle():
    assert hasattr(metamodel_Sequence, "cycle")
    descriptor = None
    for klass in metamodel_Sequence.__mro__:
        if "cycle" in klass.__dict__:
            descriptor = klass.__dict__["cycle"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_sequence_has_maxValue():
    assert hasattr(metamodel_Sequence, "maxValue")
    descriptor = None
    for klass in metamodel_Sequence.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_sequence_has_minValue():
    assert hasattr(metamodel_Sequence, "minValue")
    descriptor = None
    for klass in metamodel_Sequence.__mro__:
        if "minValue" in klass.__dict__:
            descriptor = klass.__dict__["minValue"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_sequence_has_incrementby():
    assert hasattr(metamodel_Sequence, "incrementby")
    descriptor = None
    for klass in metamodel_Sequence.__mro__:
        if "incrementby" in klass.__dict__:
            descriptor = klass.__dict__["incrementby"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_sequence_has_startwith():
    assert hasattr(metamodel_Sequence, "startwith")
    descriptor = None
    for klass in metamodel_Sequence.__mro__:
        if "startwith" in klass.__dict__:
            descriptor = klass.__dict__["startwith"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_sequence_has_currentValue():
    assert hasattr(metamodel_Sequence, "currentValue")
    descriptor = None
    for klass in metamodel_Sequence.__mro__:
        if "currentValue" in klass.__dict__:
            descriptor = klass.__dict__["currentValue"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_sequence_has_name():
    assert hasattr(metamodel_Sequence, "name")
    descriptor = None
    for klass in metamodel_Sequence.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_table_is_not_abstract():
    assert not inspect.isabstract(metamodel_Table)


def test_metamodel_table_constructor_exists():
    assert callable(metamodel_Table.__init__)


def test_metamodel_table_constructor_args():
    sig = inspect.signature(metamodel_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel_table_has_name():
    assert hasattr(metamodel_Table, "name")
    descriptor = None
    for klass in metamodel_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_database_is_not_abstract():
    assert not inspect.isabstract(metamodel_Database)


def test_metamodel_database_constructor_exists():
    assert callable(metamodel_Database.__init__)


def test_metamodel_database_constructor_args():
    sig = inspect.signature(metamodel_Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel_database_has_name():
    assert hasattr(metamodel_Database, "name")
    descriptor = None
    for klass in metamodel_Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_row_is_not_abstract():
    assert not inspect.isabstract(metamodel_Row)


def test_metamodel_row_constructor_exists():
    assert callable(metamodel_Row.__init__)


def test_metamodel_row_constructor_args():
    sig = inspect.signature(metamodel_Row.__init__)
    params = list(sig.parameters.keys())

def test_datatype_exists():
    # Check that the Enumeration exists
    assert Datatype is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Datatype]
    expected_literals = [
        "TEXT",
        "CHAR",
        "BOOLEAN",
        "TINYTEXT",
        "STRING",
        "DOUBLE",
        "BLOB",
        "FLOAT",
        "BIGINT",
        "TIMESTAMP",
        "SMALLINT",
        "DATETIME",
        "DECIMAL",
        "DATE",
        "VARCHAR",
        "LONGTEXT",
        "INT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Datatype"

def test_constrainttype_exists():
    # Check that the Enumeration exists
    assert ConstraintType is not None

def test_constrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintType]
    expected_literals = [
        "UNIQUE",
        "FOREIGN_KEY",
        "PRIMARY_KEY",
        "COMPOSITE_PRIMARY_KEY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConstraintType"


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
metamodel_Column_strategy = st.builds(
    metamodel_Column,
    size=
        safe_text,
    nullable=
        st.booleans(),
    type=
        safe_text,
    name=
        safe_text
)
metamodel_Constraint_strategy = st.builds(
    metamodel_Constraint,
    type=
        safe_text,
    name=
        safe_text,
    reference=
        safe_text
)
metamodel_Cell_strategy = st.builds(
    metamodel_Cell,
    value=
        safe_text
)
metamodel_Sequence_strategy = st.builds(
    metamodel_Sequence,
    cycle=
        st.booleans(),
    maxValue=
        safe_text,
    minValue=
        st.integers(),
    incrementby=
        st.integers(),
    startwith=
        safe_text,
    currentValue=
        safe_text,
    name=
        safe_text
)
metamodel_Table_strategy = st.builds(
    metamodel_Table,
    name=
        safe_text
)
metamodel_Database_strategy = st.builds(
    metamodel_Database,
    name=
        safe_text
)
metamodel_Row_strategy = st.builds(
    metamodel_Row,
)

@given(instance=metamodel_Column_strategy)
@settings(max_examples=50)
def test_metamodel_column_instantiation(instance):
    assert isinstance(instance, metamodel_Column)



@given(instance=metamodel_Column_strategy)
def test_metamodel_column_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=metamodel_Column_strategy)
def test_metamodel_column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=metamodel_Column_strategy)
def test_metamodel_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=metamodel_Column_strategy)
def test_metamodel_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel_Constraint_strategy)
@settings(max_examples=50)
def test_metamodel_constraint_instantiation(instance):
    assert isinstance(instance, metamodel_Constraint)



@given(instance=metamodel_Constraint_strategy)
def test_metamodel_constraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=metamodel_Constraint_strategy)
def test_metamodel_constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=metamodel_Constraint_strategy)
def test_metamodel_constraint_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=metamodel_Cell_strategy)
@settings(max_examples=50)
def test_metamodel_cell_instantiation(instance):
    assert isinstance(instance, metamodel_Cell)



@given(instance=metamodel_Cell_strategy)
def test_metamodel_cell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=metamodel_Sequence_strategy)
@settings(max_examples=50)
def test_metamodel_sequence_instantiation(instance):
    assert isinstance(instance, metamodel_Sequence)



@given(instance=metamodel_Sequence_strategy)
def test_metamodel_sequence_cycle_setter(instance):
    original = instance.cycle
    instance.cycle = original
    assert instance.cycle == original



@given(instance=metamodel_Sequence_strategy)
def test_metamodel_sequence_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original



@given(instance=metamodel_Sequence_strategy)
def test_metamodel_sequence_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original



@given(instance=metamodel_Sequence_strategy)
def test_metamodel_sequence_incrementby_setter(instance):
    original = instance.incrementby
    instance.incrementby = original
    assert instance.incrementby == original



@given(instance=metamodel_Sequence_strategy)
def test_metamodel_sequence_startwith_setter(instance):
    original = instance.startwith
    instance.startwith = original
    assert instance.startwith == original



@given(instance=metamodel_Sequence_strategy)
def test_metamodel_sequence_currentValue_setter(instance):
    original = instance.currentValue
    instance.currentValue = original
    assert instance.currentValue == original



@given(instance=metamodel_Sequence_strategy)
def test_metamodel_sequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel_Table_strategy)
@settings(max_examples=50)
def test_metamodel_table_instantiation(instance):
    assert isinstance(instance, metamodel_Table)



@given(instance=metamodel_Table_strategy)
def test_metamodel_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel_Database_strategy)
@settings(max_examples=50)
def test_metamodel_database_instantiation(instance):
    assert isinstance(instance, metamodel_Database)



@given(instance=metamodel_Database_strategy)
def test_metamodel_database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel_Row_strategy)
@settings(max_examples=50)
def test_metamodel_row_instantiation(instance):
    assert isinstance(instance, metamodel_Row)
