import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    genericsql_Constraint,
    Constraint,
    genericsql_Unique,
    genericsql_Check,
    genericsql_NamedElement,
    NamedElement,
    genericsql_PrimaryKey,
    genericsql_Field,
    genericsql_Table,
    genericsql_ForeignKey,
    genericsql_DataBase,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_genericsql_constraint_is_not_abstract():
    assert not inspect.isabstract(genericsql_Constraint)


def test_genericsql_constraint_constructor_exists():
    assert callable(genericsql_Constraint.__init__)


def test_genericsql_constraint_constructor_args():
    sig = inspect.signature(genericsql_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_genericsql_unique_is_not_abstract():
    assert not inspect.isabstract(genericsql_Unique)


def test_genericsql_unique_constructor_exists():
    assert callable(genericsql_Unique.__init__)


def test_genericsql_unique_constructor_args():
    sig = inspect.signature(genericsql_Unique.__init__)
    params = list(sig.parameters.keys())



def test_genericsql_check_is_not_abstract():
    assert not inspect.isabstract(genericsql_Check)


def test_genericsql_check_constructor_exists():
    assert callable(genericsql_Check.__init__)


def test_genericsql_check_constructor_args():
    sig = inspect.signature(genericsql_Check.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_genericsql_check_has_expression():
    assert hasattr(genericsql_Check, "expression")
    descriptor = None
    for klass in genericsql_Check.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_genericsql_namedelement_is_not_abstract():
    assert not inspect.isabstract(genericsql_NamedElement)


def test_genericsql_namedelement_constructor_exists():
    assert callable(genericsql_NamedElement.__init__)


def test_genericsql_namedelement_constructor_args():
    sig = inspect.signature(genericsql_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_genericsql_namedelement_has_name():
    assert hasattr(genericsql_NamedElement, "name")
    descriptor = None
    for klass in genericsql_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_genericsql_namedelement_has_comment():
    assert hasattr(genericsql_NamedElement, "comment")
    descriptor = None
    for klass in genericsql_NamedElement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_genericsql_primarykey_is_not_abstract():
    assert not inspect.isabstract(genericsql_PrimaryKey)


def test_genericsql_primarykey_constructor_exists():
    assert callable(genericsql_PrimaryKey.__init__)


def test_genericsql_primarykey_constructor_args():
    sig = inspect.signature(genericsql_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_genericsql_field_is_not_abstract():
    assert not inspect.isabstract(genericsql_Field)


def test_genericsql_field_constructor_exists():
    assert callable(genericsql_Field.__init__)


def test_genericsql_field_constructor_args():
    sig = inspect.signature(genericsql_Field.__init__)
    params = list(sig.parameters.keys())
    assert "autoIcrement" in params, "Missing parameter 'autoIcrement'"
    assert "type" in params, "Missing parameter 'type'"
    assert "notNull" in params, "Missing parameter 'notNull'"
    assert "specificType" in params, "Missing parameter 'specificType'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "size" in params, "Missing parameter 'size'"

def test_genericsql_field_has_autoIcrement():
    assert hasattr(genericsql_Field, "autoIcrement")
    descriptor = None
    for klass in genericsql_Field.__mro__:
        if "autoIcrement" in klass.__dict__:
            descriptor = klass.__dict__["autoIcrement"]
            break
    assert isinstance(descriptor, property)

def test_genericsql_field_has_type():
    assert hasattr(genericsql_Field, "type")
    descriptor = None
    for klass in genericsql_Field.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_genericsql_field_has_notNull():
    assert hasattr(genericsql_Field, "notNull")
    descriptor = None
    for klass in genericsql_Field.__mro__:
        if "notNull" in klass.__dict__:
            descriptor = klass.__dict__["notNull"]
            break
    assert isinstance(descriptor, property)

def test_genericsql_field_has_specificType():
    assert hasattr(genericsql_Field, "specificType")
    descriptor = None
    for klass in genericsql_Field.__mro__:
        if "specificType" in klass.__dict__:
            descriptor = klass.__dict__["specificType"]
            break
    assert isinstance(descriptor, property)

def test_genericsql_field_has_defaultValue():
    assert hasattr(genericsql_Field, "defaultValue")
    descriptor = None
    for klass in genericsql_Field.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_genericsql_field_has_unique():
    assert hasattr(genericsql_Field, "unique")
    descriptor = None
    for klass in genericsql_Field.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_genericsql_field_has_size():
    assert hasattr(genericsql_Field, "size")
    descriptor = None
    for klass in genericsql_Field.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_genericsql_table_is_not_abstract():
    assert not inspect.isabstract(genericsql_Table)


def test_genericsql_table_constructor_exists():
    assert callable(genericsql_Table.__init__)


def test_genericsql_table_constructor_args():
    sig = inspect.signature(genericsql_Table.__init__)
    params = list(sig.parameters.keys())



def test_genericsql_foreignkey_is_not_abstract():
    assert not inspect.isabstract(genericsql_ForeignKey)


def test_genericsql_foreignkey_constructor_exists():
    assert callable(genericsql_ForeignKey.__init__)


def test_genericsql_foreignkey_constructor_args():
    sig = inspect.signature(genericsql_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_genericsql_database_is_not_abstract():
    assert not inspect.isabstract(genericsql_DataBase)


def test_genericsql_database_constructor_exists():
    assert callable(genericsql_DataBase.__init__)


def test_genericsql_database_constructor_args():
    sig = inspect.signature(genericsql_DataBase.__init__)
    params = list(sig.parameters.keys())

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "undefined",
        "int",
        "varchar",
        "double",
        "bigInt",
        "date",
        "byteArray",
        "boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
genericsql_Constraint_strategy = st.builds(
    genericsql_Constraint,
)
Constraint_strategy = st.builds(
    Constraint,
)
genericsql_Unique_strategy = st.builds(
    genericsql_Unique,
)
genericsql_Check_strategy = st.builds(
    genericsql_Check,
    expression=
        safe_text
)
genericsql_NamedElement_strategy = st.builds(
    genericsql_NamedElement,
    name=
        safe_text,
    comment=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
genericsql_PrimaryKey_strategy = st.builds(
    genericsql_PrimaryKey,
)
genericsql_Field_strategy = st.builds(
    genericsql_Field,
    autoIcrement=
        st.booleans(),
    type=
        safe_text,
    notNull=
        st.booleans(),
    specificType=
        safe_text,
    defaultValue=
        safe_text,
    unique=
        st.booleans(),
    size=
        st.integers()
)
genericsql_Table_strategy = st.builds(
    genericsql_Table,
)
genericsql_ForeignKey_strategy = st.builds(
    genericsql_ForeignKey,
)
genericsql_DataBase_strategy = st.builds(
    genericsql_DataBase,
)

@given(instance=genericsql_Constraint_strategy)
@settings(max_examples=50)
def test_genericsql_constraint_instantiation(instance):
    assert isinstance(instance, genericsql_Constraint)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=genericsql_Unique_strategy)
@settings(max_examples=50)
def test_genericsql_unique_instantiation(instance):
    assert isinstance(instance, genericsql_Unique)

@given(instance=genericsql_Check_strategy)
@settings(max_examples=50)
def test_genericsql_check_instantiation(instance):
    assert isinstance(instance, genericsql_Check)



@given(instance=genericsql_Check_strategy)
def test_genericsql_check_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=genericsql_NamedElement_strategy)
@settings(max_examples=50)
def test_genericsql_namedelement_instantiation(instance):
    assert isinstance(instance, genericsql_NamedElement)



@given(instance=genericsql_NamedElement_strategy)
def test_genericsql_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=genericsql_NamedElement_strategy)
def test_genericsql_namedelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=genericsql_PrimaryKey_strategy)
@settings(max_examples=50)
def test_genericsql_primarykey_instantiation(instance):
    assert isinstance(instance, genericsql_PrimaryKey)

@given(instance=genericsql_Field_strategy)
@settings(max_examples=50)
def test_genericsql_field_instantiation(instance):
    assert isinstance(instance, genericsql_Field)



@given(instance=genericsql_Field_strategy)
def test_genericsql_field_autoIcrement_setter(instance):
    original = instance.autoIcrement
    instance.autoIcrement = original
    assert instance.autoIcrement == original



@given(instance=genericsql_Field_strategy)
def test_genericsql_field_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=genericsql_Field_strategy)
def test_genericsql_field_notNull_setter(instance):
    original = instance.notNull
    instance.notNull = original
    assert instance.notNull == original



@given(instance=genericsql_Field_strategy)
def test_genericsql_field_specificType_setter(instance):
    original = instance.specificType
    instance.specificType = original
    assert instance.specificType == original



@given(instance=genericsql_Field_strategy)
def test_genericsql_field_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=genericsql_Field_strategy)
def test_genericsql_field_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=genericsql_Field_strategy)
def test_genericsql_field_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=genericsql_Table_strategy)
@settings(max_examples=50)
def test_genericsql_table_instantiation(instance):
    assert isinstance(instance, genericsql_Table)

@given(instance=genericsql_ForeignKey_strategy)
@settings(max_examples=50)
def test_genericsql_foreignkey_instantiation(instance):
    assert isinstance(instance, genericsql_ForeignKey)

@given(instance=genericsql_DataBase_strategy)
@settings(max_examples=50)
def test_genericsql_database_instantiation(instance):
    assert isinstance(instance, genericsql_DataBase)
