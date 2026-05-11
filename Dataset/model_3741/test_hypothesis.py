import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    genericsql::Constraint,
    Constraint,
    genericsql::Unique,
    genericsql::Check,
    genericsql::NamedElement,
    NamedElement,
    genericsql::Table,
    genericsql::Field,
    genericsql::ForeignKey,
    genericsql::PrimaryKey,
    genericsql::DataBase,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_genericsql::constraint_is_not_abstract():
    assert not inspect.isabstract(genericsql::Constraint)


def test_genericsql::constraint_constructor_exists():
    assert callable(genericsql::Constraint.__init__)


def test_genericsql::constraint_constructor_args():
    sig = inspect.signature(genericsql::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_genericsql::unique_is_not_abstract():
    assert not inspect.isabstract(genericsql::Unique)


def test_genericsql::unique_constructor_exists():
    assert callable(genericsql::Unique.__init__)


def test_genericsql::unique_constructor_args():
    sig = inspect.signature(genericsql::Unique.__init__)
    params = list(sig.parameters.keys())



def test_genericsql::check_is_not_abstract():
    assert not inspect.isabstract(genericsql::Check)


def test_genericsql::check_constructor_exists():
    assert callable(genericsql::Check.__init__)


def test_genericsql::check_constructor_args():
    sig = inspect.signature(genericsql::Check.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_genericsql::check_has_expression():
    assert hasattr(genericsql::Check, "expression")
    descriptor = None
    for klass in genericsql::Check.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_genericsql::namedelement_is_not_abstract():
    assert not inspect.isabstract(genericsql::NamedElement)


def test_genericsql::namedelement_constructor_exists():
    assert callable(genericsql::NamedElement.__init__)


def test_genericsql::namedelement_constructor_args():
    sig = inspect.signature(genericsql::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_genericsql::namedelement_has_name():
    assert hasattr(genericsql::NamedElement, "name")
    descriptor = None
    for klass in genericsql::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_genericsql::namedelement_has_comment():
    assert hasattr(genericsql::NamedElement, "comment")
    descriptor = None
    for klass in genericsql::NamedElement.__mro__:
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



def test_genericsql::table_is_not_abstract():
    assert not inspect.isabstract(genericsql::Table)


def test_genericsql::table_constructor_exists():
    assert callable(genericsql::Table.__init__)


def test_genericsql::table_constructor_args():
    sig = inspect.signature(genericsql::Table.__init__)
    params = list(sig.parameters.keys())



def test_genericsql::field_is_not_abstract():
    assert not inspect.isabstract(genericsql::Field)


def test_genericsql::field_constructor_exists():
    assert callable(genericsql::Field.__init__)


def test_genericsql::field_constructor_args():
    sig = inspect.signature(genericsql::Field.__init__)
    params = list(sig.parameters.keys())
    assert "autoIcrement" in params, "Missing parameter 'autoIcrement'"
    assert "specificType" in params, "Missing parameter 'specificType'"
    assert "type" in params, "Missing parameter 'type'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "notNull" in params, "Missing parameter 'notNull'"
    assert "size" in params, "Missing parameter 'size'"

def test_genericsql::field_has_autoIcrement():
    assert hasattr(genericsql::Field, "autoIcrement")
    descriptor = None
    for klass in genericsql::Field.__mro__:
        if "autoIcrement" in klass.__dict__:
            descriptor = klass.__dict__["autoIcrement"]
            break
    assert isinstance(descriptor, property)

def test_genericsql::field_has_specificType():
    assert hasattr(genericsql::Field, "specificType")
    descriptor = None
    for klass in genericsql::Field.__mro__:
        if "specificType" in klass.__dict__:
            descriptor = klass.__dict__["specificType"]
            break
    assert isinstance(descriptor, property)

def test_genericsql::field_has_type():
    assert hasattr(genericsql::Field, "type")
    descriptor = None
    for klass in genericsql::Field.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_genericsql::field_has_unique():
    assert hasattr(genericsql::Field, "unique")
    descriptor = None
    for klass in genericsql::Field.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_genericsql::field_has_defaultValue():
    assert hasattr(genericsql::Field, "defaultValue")
    descriptor = None
    for klass in genericsql::Field.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_genericsql::field_has_notNull():
    assert hasattr(genericsql::Field, "notNull")
    descriptor = None
    for klass in genericsql::Field.__mro__:
        if "notNull" in klass.__dict__:
            descriptor = klass.__dict__["notNull"]
            break
    assert isinstance(descriptor, property)

def test_genericsql::field_has_size():
    assert hasattr(genericsql::Field, "size")
    descriptor = None
    for klass in genericsql::Field.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_genericsql::foreignkey_is_not_abstract():
    assert not inspect.isabstract(genericsql::ForeignKey)


def test_genericsql::foreignkey_constructor_exists():
    assert callable(genericsql::ForeignKey.__init__)


def test_genericsql::foreignkey_constructor_args():
    sig = inspect.signature(genericsql::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_genericsql::primarykey_is_not_abstract():
    assert not inspect.isabstract(genericsql::PrimaryKey)


def test_genericsql::primarykey_constructor_exists():
    assert callable(genericsql::PrimaryKey.__init__)


def test_genericsql::primarykey_constructor_args():
    sig = inspect.signature(genericsql::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_genericsql::database_is_not_abstract():
    assert not inspect.isabstract(genericsql::DataBase)


def test_genericsql::database_constructor_exists():
    assert callable(genericsql::DataBase.__init__)


def test_genericsql::database_constructor_args():
    sig = inspect.signature(genericsql::DataBase.__init__)
    params = list(sig.parameters.keys())

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "bigInt",
        "double",
        "byteArray",
        "int",
        "undefined",
        "varchar",
        "date",
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
genericsql::Constraint_strategy = st.builds(
    genericsql::Constraint,
)
Constraint_strategy = st.builds(
    Constraint,
)
genericsql::Unique_strategy = st.builds(
    genericsql::Unique,
)
genericsql::Check_strategy = st.builds(
    genericsql::Check,
    expression=
        safe_text
)
genericsql::NamedElement_strategy = st.builds(
    genericsql::NamedElement,
    name=
        safe_text,
    comment=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
genericsql::Table_strategy = st.builds(
    genericsql::Table,
)
genericsql::Field_strategy = st.builds(
    genericsql::Field,
    autoIcrement=
        st.booleans(),
    specificType=
        safe_text,
    type=
        safe_text,
    unique=
        st.booleans(),
    defaultValue=
        safe_text,
    notNull=
        st.booleans(),
    size=
        st.integers()
)
genericsql::ForeignKey_strategy = st.builds(
    genericsql::ForeignKey,
)
genericsql::PrimaryKey_strategy = st.builds(
    genericsql::PrimaryKey,
)
genericsql::DataBase_strategy = st.builds(
    genericsql::DataBase,
)

@given(instance=genericsql::Constraint_strategy)
@settings(max_examples=50)
def test_genericsql::constraint_instantiation(instance):
    assert isinstance(instance, genericsql::Constraint)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=genericsql::Unique_strategy)
@settings(max_examples=50)
def test_genericsql::unique_instantiation(instance):
    assert isinstance(instance, genericsql::Unique)

@given(instance=genericsql::Check_strategy)
@settings(max_examples=50)
def test_genericsql::check_instantiation(instance):
    assert isinstance(instance, genericsql::Check)

@given(instance=genericsql::Check_strategy)
def test_genericsql::check_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=genericsql::Check_strategy)
def test_genericsql::check_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=genericsql::NamedElement_strategy)
@settings(max_examples=50)
def test_genericsql::namedelement_instantiation(instance):
    assert isinstance(instance, genericsql::NamedElement)

@given(instance=genericsql::NamedElement_strategy)
def test_genericsql::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=genericsql::NamedElement_strategy)
def test_genericsql::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=genericsql::NamedElement_strategy)
def test_genericsql::namedelement_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=genericsql::NamedElement_strategy)
def test_genericsql::namedelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=genericsql::Table_strategy)
@settings(max_examples=50)
def test_genericsql::table_instantiation(instance):
    assert isinstance(instance, genericsql::Table)

@given(instance=genericsql::Field_strategy)
@settings(max_examples=50)
def test_genericsql::field_instantiation(instance):
    assert isinstance(instance, genericsql::Field)

@given(instance=genericsql::Field_strategy)
def test_genericsql::field_autoIcrement_type(instance):
    assert isinstance(instance.autoIcrement, bool)


@given(instance=genericsql::Field_strategy)
def test_genericsql::field_autoIcrement_setter(instance):
    original = instance.autoIcrement
    instance.autoIcrement = original
    assert instance.autoIcrement == original

@given(instance=genericsql::Field_strategy)
def test_genericsql::field_specificType_type(instance):
    assert isinstance(instance.specificType, str)


@given(instance=genericsql::Field_strategy)
def test_genericsql::field_specificType_setter(instance):
    original = instance.specificType
    instance.specificType = original
    assert instance.specificType == original

@given(instance=genericsql::Field_strategy)
def test_genericsql::field_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=genericsql::Field_strategy)
def test_genericsql::field_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=genericsql::Field_strategy)
def test_genericsql::field_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=genericsql::Field_strategy)
def test_genericsql::field_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=genericsql::Field_strategy)
def test_genericsql::field_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=genericsql::Field_strategy)
def test_genericsql::field_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=genericsql::Field_strategy)
def test_genericsql::field_notNull_type(instance):
    assert isinstance(instance.notNull, bool)


@given(instance=genericsql::Field_strategy)
def test_genericsql::field_notNull_setter(instance):
    original = instance.notNull
    instance.notNull = original
    assert instance.notNull == original

@given(instance=genericsql::Field_strategy)
def test_genericsql::field_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=genericsql::Field_strategy)
def test_genericsql::field_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=genericsql::ForeignKey_strategy)
@settings(max_examples=50)
def test_genericsql::foreignkey_instantiation(instance):
    assert isinstance(instance, genericsql::ForeignKey)

@given(instance=genericsql::PrimaryKey_strategy)
@settings(max_examples=50)
def test_genericsql::primarykey_instantiation(instance):
    assert isinstance(instance, genericsql::PrimaryKey)

@given(instance=genericsql::DataBase_strategy)
@settings(max_examples=50)
def test_genericsql::database_instantiation(instance):
    assert isinstance(instance, genericsql::DataBase)
