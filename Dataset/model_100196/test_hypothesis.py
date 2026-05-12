import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Key,
    Value,
    SQLDDL::NullVal,
    SQLDDL::StringVal,
    SQLDDL::IntegerVal,
    SQLDDL::ForeignKey,
    SQLDDL::PrimaryKey,
    SQLDDL::SimpleKey,
    Column,
    Parameter,
    TableElement,
    SQLDDL::Key,
    ForeignKey,
    Type,
    SQLDDL::Column,
    LocatedElement,
    SQLDDL::Value,
    SQLDDL::TableElement,
    SQLDDL::NamedElement,
    SQLDDL::LocatedElement,
    Database,
    Table,
    NamedElement,
    SQLDDL::Table,
    SQLDDL::Parameter,
    SQLDDL::Type,
    SQLDDL::Database,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_sqlddl::nullval_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::NullVal)


def test_sqlddl::nullval_constructor_exists():
    assert callable(SQLDDL::NullVal.__init__)


def test_sqlddl::nullval_constructor_args():
    sig = inspect.signature(SQLDDL::NullVal.__init__)
    params = list(sig.parameters.keys())



def test_sqlddl::stringval_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::StringVal)


def test_sqlddl::stringval_constructor_exists():
    assert callable(SQLDDL::StringVal.__init__)


def test_sqlddl::stringval_constructor_args():
    sig = inspect.signature(SQLDDL::StringVal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sqlddl::stringval_has_value():
    assert hasattr(SQLDDL::StringVal, "value")
    descriptor = None
    for klass in SQLDDL::StringVal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sqlddl::integerval_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::IntegerVal)


def test_sqlddl::integerval_constructor_exists():
    assert callable(SQLDDL::IntegerVal.__init__)


def test_sqlddl::integerval_constructor_args():
    sig = inspect.signature(SQLDDL::IntegerVal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sqlddl::integerval_has_value():
    assert hasattr(SQLDDL::IntegerVal, "value")
    descriptor = None
    for klass in SQLDDL::IntegerVal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sqlddl::foreignkey_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::ForeignKey)


def test_sqlddl::foreignkey_constructor_exists():
    assert callable(SQLDDL::ForeignKey.__init__)


def test_sqlddl::foreignkey_constructor_args():
    sig = inspect.signature(SQLDDL::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_sqlddl::primarykey_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::PrimaryKey)


def test_sqlddl::primarykey_constructor_exists():
    assert callable(SQLDDL::PrimaryKey.__init__)


def test_sqlddl::primarykey_constructor_args():
    sig = inspect.signature(SQLDDL::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_sqlddl::simplekey_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::SimpleKey)


def test_sqlddl::simplekey_constructor_exists():
    assert callable(SQLDDL::SimpleKey.__init__)


def test_sqlddl::simplekey_constructor_args():
    sig = inspect.signature(SQLDDL::SimpleKey.__init__)
    params = list(sig.parameters.keys())



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_tableelement_is_not_abstract():
    assert not inspect.isabstract(TableElement)


def test_tableelement_constructor_exists():
    assert callable(TableElement.__init__)


def test_tableelement_constructor_args():
    sig = inspect.signature(TableElement.__init__)
    params = list(sig.parameters.keys())



def test_sqlddl::key_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::Key)


def test_sqlddl::key_constructor_exists():
    assert callable(SQLDDL::Key.__init__)


def test_sqlddl::key_constructor_args():
    sig = inspect.signature(SQLDDL::Key.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_sqlddl::key_has_name():
    assert hasattr(SQLDDL::Key, "name")
    descriptor = None
    for klass in SQLDDL::Key.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sqlddl::key_has_isUnique():
    assert hasattr(SQLDDL::Key, "isUnique")
    descriptor = None
    for klass in SQLDDL::Key.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_foreignkey_is_not_abstract():
    assert not inspect.isabstract(ForeignKey)


def test_foreignkey_constructor_exists():
    assert callable(ForeignKey.__init__)


def test_foreignkey_constructor_args():
    sig = inspect.signature(ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_sqlddl::column_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::Column)


def test_sqlddl::column_constructor_exists():
    assert callable(SQLDDL::Column.__init__)


def test_sqlddl::column_constructor_args():
    sig = inspect.signature(SQLDDL::Column.__init__)
    params = list(sig.parameters.keys())
    assert "canBeNull" in params, "Missing parameter 'canBeNull'"
    assert "name" in params, "Missing parameter 'name'"

def test_sqlddl::column_has_canBeNull():
    assert hasattr(SQLDDL::Column, "canBeNull")
    descriptor = None
    for klass in SQLDDL::Column.__mro__:
        if "canBeNull" in klass.__dict__:
            descriptor = klass.__dict__["canBeNull"]
            break
    assert isinstance(descriptor, property)

def test_sqlddl::column_has_name():
    assert hasattr(SQLDDL::Column, "name")
    descriptor = None
    for klass in SQLDDL::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_sqlddl::value_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::Value)


def test_sqlddl::value_constructor_exists():
    assert callable(SQLDDL::Value.__init__)


def test_sqlddl::value_constructor_args():
    sig = inspect.signature(SQLDDL::Value.__init__)
    params = list(sig.parameters.keys())



def test_sqlddl::tableelement_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::TableElement)


def test_sqlddl::tableelement_constructor_exists():
    assert callable(SQLDDL::TableElement.__init__)


def test_sqlddl::tableelement_constructor_args():
    sig = inspect.signature(SQLDDL::TableElement.__init__)
    params = list(sig.parameters.keys())



def test_sqlddl::namedelement_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::NamedElement)


def test_sqlddl::namedelement_constructor_exists():
    assert callable(SQLDDL::NamedElement.__init__)


def test_sqlddl::namedelement_constructor_args():
    sig = inspect.signature(SQLDDL::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlddl::namedelement_has_name():
    assert hasattr(SQLDDL::NamedElement, "name")
    descriptor = None
    for klass in SQLDDL::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlddl::locatedelement_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::LocatedElement)


def test_sqlddl::locatedelement_constructor_exists():
    assert callable(SQLDDL::LocatedElement.__init__)


def test_sqlddl::locatedelement_constructor_args():
    sig = inspect.signature(SQLDDL::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"

def test_sqlddl::locatedelement_has_commentsAfter():
    assert hasattr(SQLDDL::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in SQLDDL::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_sqlddl::locatedelement_has_location():
    assert hasattr(SQLDDL::LocatedElement, "location")
    descriptor = None
    for klass in SQLDDL::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_sqlddl::locatedelement_has_commentsBefore():
    assert hasattr(SQLDDL::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in SQLDDL::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)



def test_database_is_not_abstract():
    assert not inspect.isabstract(Database)


def test_database_constructor_exists():
    assert callable(Database.__init__)


def test_database_constructor_args():
    sig = inspect.signature(Database.__init__)
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



def test_sqlddl::table_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::Table)


def test_sqlddl::table_constructor_exists():
    assert callable(SQLDDL::Table.__init__)


def test_sqlddl::table_constructor_args():
    sig = inspect.signature(SQLDDL::Table.__init__)
    params = list(sig.parameters.keys())



def test_sqlddl::parameter_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::Parameter)


def test_sqlddl::parameter_constructor_exists():
    assert callable(SQLDDL::Parameter.__init__)


def test_sqlddl::parameter_constructor_args():
    sig = inspect.signature(SQLDDL::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_sqlddl::type_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::Type)


def test_sqlddl::type_constructor_exists():
    assert callable(SQLDDL::Type.__init__)


def test_sqlddl::type_constructor_args():
    sig = inspect.signature(SQLDDL::Type.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "isUnsigned" in params, "Missing parameter 'isUnsigned'"

def test_sqlddl::type_has_length():
    assert hasattr(SQLDDL::Type, "length")
    descriptor = None
    for klass in SQLDDL::Type.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_sqlddl::type_has_isUnsigned():
    assert hasattr(SQLDDL::Type, "isUnsigned")
    descriptor = None
    for klass in SQLDDL::Type.__mro__:
        if "isUnsigned" in klass.__dict__:
            descriptor = klass.__dict__["isUnsigned"]
            break
    assert isinstance(descriptor, property)



def test_sqlddl::database_is_not_abstract():
    assert not inspect.isabstract(SQLDDL::Database)


def test_sqlddl::database_constructor_exists():
    assert callable(SQLDDL::Database.__init__)


def test_sqlddl::database_constructor_args():
    sig = inspect.signature(SQLDDL::Database.__init__)
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
Key_strategy = st.builds(
    Key,
)
Value_strategy = st.builds(
    Value,
)
SQLDDL::NullVal_strategy = st.builds(
    SQLDDL::NullVal,
)
SQLDDL::StringVal_strategy = st.builds(
    SQLDDL::StringVal,
    value=
        safe_text
)
SQLDDL::IntegerVal_strategy = st.builds(
    SQLDDL::IntegerVal,
    value=
        safe_text
)
SQLDDL::ForeignKey_strategy = st.builds(
    SQLDDL::ForeignKey,
)
SQLDDL::PrimaryKey_strategy = st.builds(
    SQLDDL::PrimaryKey,
)
SQLDDL::SimpleKey_strategy = st.builds(
    SQLDDL::SimpleKey,
)
Column_strategy = st.builds(
    Column,
)
Parameter_strategy = st.builds(
    Parameter,
)
TableElement_strategy = st.builds(
    TableElement,
)
SQLDDL::Key_strategy = st.builds(
    SQLDDL::Key,
    name=
        safe_text,
    isUnique=
        safe_text
)
ForeignKey_strategy = st.builds(
    ForeignKey,
)
Type_strategy = st.builds(
    Type,
)
SQLDDL::Column_strategy = st.builds(
    SQLDDL::Column,
    canBeNull=
        safe_text,
    name=
        safe_text
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
SQLDDL::Value_strategy = st.builds(
    SQLDDL::Value,
)
SQLDDL::TableElement_strategy = st.builds(
    SQLDDL::TableElement,
)
SQLDDL::NamedElement_strategy = st.builds(
    SQLDDL::NamedElement,
    name=
        safe_text
)
SQLDDL::LocatedElement_strategy = st.builds(
    SQLDDL::LocatedElement,
    commentsAfter=
        safe_text,
    location=
        safe_text,
    commentsBefore=
        safe_text
)
Database_strategy = st.builds(
    Database,
)
Table_strategy = st.builds(
    Table,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
SQLDDL::Table_strategy = st.builds(
    SQLDDL::Table,
)
SQLDDL::Parameter_strategy = st.builds(
    SQLDDL::Parameter,
)
SQLDDL::Type_strategy = st.builds(
    SQLDDL::Type,
    length=
        safe_text,
    isUnsigned=
        safe_text
)
SQLDDL::Database_strategy = st.builds(
    SQLDDL::Database,
)

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=SQLDDL::NullVal_strategy)
@settings(max_examples=50)
def test_sqlddl::nullval_instantiation(instance):
    assert isinstance(instance, SQLDDL::NullVal)

@given(instance=SQLDDL::StringVal_strategy)
@settings(max_examples=50)
def test_sqlddl::stringval_instantiation(instance):
    assert isinstance(instance, SQLDDL::StringVal)

@given(instance=SQLDDL::StringVal_strategy)
def test_sqlddl::stringval_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SQLDDL::StringVal_strategy)
def test_sqlddl::stringval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQLDDL::IntegerVal_strategy)
@settings(max_examples=50)
def test_sqlddl::integerval_instantiation(instance):
    assert isinstance(instance, SQLDDL::IntegerVal)

@given(instance=SQLDDL::IntegerVal_strategy)
def test_sqlddl::integerval_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SQLDDL::IntegerVal_strategy)
def test_sqlddl::integerval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SQLDDL::ForeignKey_strategy)
@settings(max_examples=50)
def test_sqlddl::foreignkey_instantiation(instance):
    assert isinstance(instance, SQLDDL::ForeignKey)

@given(instance=SQLDDL::PrimaryKey_strategy)
@settings(max_examples=50)
def test_sqlddl::primarykey_instantiation(instance):
    assert isinstance(instance, SQLDDL::PrimaryKey)

@given(instance=SQLDDL::SimpleKey_strategy)
@settings(max_examples=50)
def test_sqlddl::simplekey_instantiation(instance):
    assert isinstance(instance, SQLDDL::SimpleKey)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=SQLDDL::Key_strategy)
@settings(max_examples=50)
def test_sqlddl::key_instantiation(instance):
    assert isinstance(instance, SQLDDL::Key)

@given(instance=SQLDDL::Key_strategy)
def test_sqlddl::key_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQLDDL::Key_strategy)
def test_sqlddl::key_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQLDDL::Key_strategy)
def test_sqlddl::key_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=SQLDDL::Key_strategy)
def test_sqlddl::key_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=ForeignKey_strategy)
@settings(max_examples=50)
def test_foreignkey_instantiation(instance):
    assert isinstance(instance, ForeignKey)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=SQLDDL::Column_strategy)
@settings(max_examples=50)
def test_sqlddl::column_instantiation(instance):
    assert isinstance(instance, SQLDDL::Column)

@given(instance=SQLDDL::Column_strategy)
def test_sqlddl::column_canBeNull_type(instance):
    assert isinstance(instance.canBeNull, str)


@given(instance=SQLDDL::Column_strategy)
def test_sqlddl::column_canBeNull_setter(instance):
    original = instance.canBeNull
    instance.canBeNull = original
    assert instance.canBeNull == original

@given(instance=SQLDDL::Column_strategy)
def test_sqlddl::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQLDDL::Column_strategy)
def test_sqlddl::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=SQLDDL::Value_strategy)
@settings(max_examples=50)
def test_sqlddl::value_instantiation(instance):
    assert isinstance(instance, SQLDDL::Value)

@given(instance=SQLDDL::TableElement_strategy)
@settings(max_examples=50)
def test_sqlddl::tableelement_instantiation(instance):
    assert isinstance(instance, SQLDDL::TableElement)

@given(instance=SQLDDL::NamedElement_strategy)
@settings(max_examples=50)
def test_sqlddl::namedelement_instantiation(instance):
    assert isinstance(instance, SQLDDL::NamedElement)

@given(instance=SQLDDL::NamedElement_strategy)
def test_sqlddl::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SQLDDL::NamedElement_strategy)
def test_sqlddl::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SQLDDL::LocatedElement_strategy)
@settings(max_examples=50)
def test_sqlddl::locatedelement_instantiation(instance):
    assert isinstance(instance, SQLDDL::LocatedElement)

@given(instance=SQLDDL::LocatedElement_strategy)
def test_sqlddl::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=SQLDDL::LocatedElement_strategy)
def test_sqlddl::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=SQLDDL::LocatedElement_strategy)
def test_sqlddl::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=SQLDDL::LocatedElement_strategy)
def test_sqlddl::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=SQLDDL::LocatedElement_strategy)
def test_sqlddl::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=SQLDDL::LocatedElement_strategy)
def test_sqlddl::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original

@given(instance=Database_strategy)
@settings(max_examples=50)
def test_database_instantiation(instance):
    assert isinstance(instance, Database)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=SQLDDL::Table_strategy)
@settings(max_examples=50)
def test_sqlddl::table_instantiation(instance):
    assert isinstance(instance, SQLDDL::Table)

@given(instance=SQLDDL::Parameter_strategy)
@settings(max_examples=50)
def test_sqlddl::parameter_instantiation(instance):
    assert isinstance(instance, SQLDDL::Parameter)

@given(instance=SQLDDL::Type_strategy)
@settings(max_examples=50)
def test_sqlddl::type_instantiation(instance):
    assert isinstance(instance, SQLDDL::Type)

@given(instance=SQLDDL::Type_strategy)
def test_sqlddl::type_length_type(instance):
    assert isinstance(instance.length, str)


@given(instance=SQLDDL::Type_strategy)
def test_sqlddl::type_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=SQLDDL::Type_strategy)
def test_sqlddl::type_isUnsigned_type(instance):
    assert isinstance(instance.isUnsigned, str)


@given(instance=SQLDDL::Type_strategy)
def test_sqlddl::type_isUnsigned_setter(instance):
    original = instance.isUnsigned
    instance.isUnsigned = original
    assert instance.isUnsigned == original

@given(instance=SQLDDL::Database_strategy)
@settings(max_examples=50)
def test_sqlddl::database_instantiation(instance):
    assert isinstance(instance, SQLDDL::Database)
