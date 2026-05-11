import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    JPA::Anotation,
    JPA::Property,
    JPA::Entity,
    JPA::PersistenceUnit,
    Anotation,
    JPA::OneToMany,
    JPA::ManyToOne,
    JPA::Column,
    JPA::Table,
    JPA::OneToOne,
    JPA::ManyToMany,
    JPA::EntityPk,
    Cascade,
    Fetch,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jpa::anotation_is_not_abstract():
    assert not inspect.isabstract(JPA::Anotation)


def test_jpa::anotation_constructor_exists():
    assert callable(JPA::Anotation.__init__)


def test_jpa::anotation_constructor_args():
    sig = inspect.signature(JPA::Anotation.__init__)
    params = list(sig.parameters.keys())



def test_jpa::property_is_not_abstract():
    assert not inspect.isabstract(JPA::Property)


def test_jpa::property_constructor_exists():
    assert callable(JPA::Property.__init__)


def test_jpa::property_constructor_args():
    sig = inspect.signature(JPA::Property.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpa::property_has_comment():
    assert hasattr(JPA::Property, "comment")
    descriptor = None
    for klass in JPA::Property.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_jpa::property_has_name():
    assert hasattr(JPA::Property, "name")
    descriptor = None
    for klass in JPA::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpa::entity_is_not_abstract():
    assert not inspect.isabstract(JPA::Entity)


def test_jpa::entity_constructor_exists():
    assert callable(JPA::Entity.__init__)


def test_jpa::entity_constructor_args():
    sig = inspect.signature(JPA::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpa::entity_has_comment():
    assert hasattr(JPA::Entity, "comment")
    descriptor = None
    for klass in JPA::Entity.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_jpa::entity_has_name():
    assert hasattr(JPA::Entity, "name")
    descriptor = None
    for klass in JPA::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpa::persistenceunit_is_not_abstract():
    assert not inspect.isabstract(JPA::PersistenceUnit)


def test_jpa::persistenceunit_constructor_exists():
    assert callable(JPA::PersistenceUnit.__init__)


def test_jpa::persistenceunit_constructor_args():
    sig = inspect.signature(JPA::PersistenceUnit.__init__)
    params = list(sig.parameters.keys())



def test_anotation_is_not_abstract():
    assert not inspect.isabstract(Anotation)


def test_anotation_constructor_exists():
    assert callable(Anotation.__init__)


def test_anotation_constructor_args():
    sig = inspect.signature(Anotation.__init__)
    params = list(sig.parameters.keys())



def test_jpa::onetomany_is_not_abstract():
    assert not inspect.isabstract(JPA::OneToMany)


def test_jpa::onetomany_constructor_exists():
    assert callable(JPA::OneToMany.__init__)


def test_jpa::onetomany_constructor_args():
    sig = inspect.signature(JPA::OneToMany.__init__)
    params = list(sig.parameters.keys())
    assert "fetch" in params, "Missing parameter 'fetch'"
    assert "cascade" in params, "Missing parameter 'cascade'"

def test_jpa::onetomany_has_fetch():
    assert hasattr(JPA::OneToMany, "fetch")
    descriptor = None
    for klass in JPA::OneToMany.__mro__:
        if "fetch" in klass.__dict__:
            descriptor = klass.__dict__["fetch"]
            break
    assert isinstance(descriptor, property)

def test_jpa::onetomany_has_cascade():
    assert hasattr(JPA::OneToMany, "cascade")
    descriptor = None
    for klass in JPA::OneToMany.__mro__:
        if "cascade" in klass.__dict__:
            descriptor = klass.__dict__["cascade"]
            break
    assert isinstance(descriptor, property)



def test_jpa::manytoone_is_not_abstract():
    assert not inspect.isabstract(JPA::ManyToOne)


def test_jpa::manytoone_constructor_exists():
    assert callable(JPA::ManyToOne.__init__)


def test_jpa::manytoone_constructor_args():
    sig = inspect.signature(JPA::ManyToOne.__init__)
    params = list(sig.parameters.keys())
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "fetch" in params, "Missing parameter 'fetch'"
    assert "joinColumn" in params, "Missing parameter 'joinColumn'"

def test_jpa::manytoone_has_nullable():
    assert hasattr(JPA::ManyToOne, "nullable")
    descriptor = None
    for klass in JPA::ManyToOne.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_jpa::manytoone_has_fetch():
    assert hasattr(JPA::ManyToOne, "fetch")
    descriptor = None
    for klass in JPA::ManyToOne.__mro__:
        if "fetch" in klass.__dict__:
            descriptor = klass.__dict__["fetch"]
            break
    assert isinstance(descriptor, property)

def test_jpa::manytoone_has_joinColumn():
    assert hasattr(JPA::ManyToOne, "joinColumn")
    descriptor = None
    for klass in JPA::ManyToOne.__mro__:
        if "joinColumn" in klass.__dict__:
            descriptor = klass.__dict__["joinColumn"]
            break
    assert isinstance(descriptor, property)



def test_jpa::column_is_not_abstract():
    assert not inspect.isabstract(JPA::Column)


def test_jpa::column_constructor_exists():
    assert callable(JPA::Column.__init__)


def test_jpa::column_constructor_args():
    sig = inspect.signature(JPA::Column.__init__)
    params = list(sig.parameters.keys())
    assert "fetch" in params, "Missing parameter 'fetch'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "nullable" in params, "Missing parameter 'nullable'"

def test_jpa::column_has_fetch():
    assert hasattr(JPA::Column, "fetch")
    descriptor = None
    for klass in JPA::Column.__mro__:
        if "fetch" in klass.__dict__:
            descriptor = klass.__dict__["fetch"]
            break
    assert isinstance(descriptor, property)

def test_jpa::column_has_type():
    assert hasattr(JPA::Column, "type")
    descriptor = None
    for klass in JPA::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_jpa::column_has_name():
    assert hasattr(JPA::Column, "name")
    descriptor = None
    for klass in JPA::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpa::column_has_nullable():
    assert hasattr(JPA::Column, "nullable")
    descriptor = None
    for klass in JPA::Column.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)



def test_jpa::table_is_not_abstract():
    assert not inspect.isabstract(JPA::Table)


def test_jpa::table_constructor_exists():
    assert callable(JPA::Table.__init__)


def test_jpa::table_constructor_args():
    sig = inspect.signature(JPA::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpa::table_has_name():
    assert hasattr(JPA::Table, "name")
    descriptor = None
    for klass in JPA::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpa::onetoone_is_not_abstract():
    assert not inspect.isabstract(JPA::OneToOne)


def test_jpa::onetoone_constructor_exists():
    assert callable(JPA::OneToOne.__init__)


def test_jpa::onetoone_constructor_args():
    sig = inspect.signature(JPA::OneToOne.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "referencedColumnName" in params, "Missing parameter 'referencedColumnName'"
    assert "updatable" in params, "Missing parameter 'updatable'"

def test_jpa::onetoone_has_name():
    assert hasattr(JPA::OneToOne, "name")
    descriptor = None
    for klass in JPA::OneToOne.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpa::onetoone_has_referencedColumnName():
    assert hasattr(JPA::OneToOne, "referencedColumnName")
    descriptor = None
    for klass in JPA::OneToOne.__mro__:
        if "referencedColumnName" in klass.__dict__:
            descriptor = klass.__dict__["referencedColumnName"]
            break
    assert isinstance(descriptor, property)

def test_jpa::onetoone_has_updatable():
    assert hasattr(JPA::OneToOne, "updatable")
    descriptor = None
    for klass in JPA::OneToOne.__mro__:
        if "updatable" in klass.__dict__:
            descriptor = klass.__dict__["updatable"]
            break
    assert isinstance(descriptor, property)



def test_jpa::manytomany_is_not_abstract():
    assert not inspect.isabstract(JPA::ManyToMany)


def test_jpa::manytomany_constructor_exists():
    assert callable(JPA::ManyToMany.__init__)


def test_jpa::manytomany_constructor_args():
    sig = inspect.signature(JPA::ManyToMany.__init__)
    params = list(sig.parameters.keys())
    assert "joinColumn" in params, "Missing parameter 'joinColumn'"
    assert "inverseJoinColumn" in params, "Missing parameter 'inverseJoinColumn'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpa::manytomany_has_joinColumn():
    assert hasattr(JPA::ManyToMany, "joinColumn")
    descriptor = None
    for klass in JPA::ManyToMany.__mro__:
        if "joinColumn" in klass.__dict__:
            descriptor = klass.__dict__["joinColumn"]
            break
    assert isinstance(descriptor, property)

def test_jpa::manytomany_has_inverseJoinColumn():
    assert hasattr(JPA::ManyToMany, "inverseJoinColumn")
    descriptor = None
    for klass in JPA::ManyToMany.__mro__:
        if "inverseJoinColumn" in klass.__dict__:
            descriptor = klass.__dict__["inverseJoinColumn"]
            break
    assert isinstance(descriptor, property)

def test_jpa::manytomany_has_name():
    assert hasattr(JPA::ManyToMany, "name")
    descriptor = None
    for klass in JPA::ManyToMany.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpa::entitypk_is_not_abstract():
    assert not inspect.isabstract(JPA::EntityPk)


def test_jpa::entitypk_constructor_exists():
    assert callable(JPA::EntityPk.__init__)


def test_jpa::entitypk_constructor_args():
    sig = inspect.signature(JPA::EntityPk.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpa::entitypk_has_name():
    assert hasattr(JPA::EntityPk, "name")
    descriptor = None
    for klass in JPA::EntityPk.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cascade_exists():
    # Check that the Enumeration exists
    assert Cascade is not None

def test_cascade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cascade]
    expected_literals = [
        "REFRESH",
        "MERGE",
        "PERSIST",
        "REMOVE",
        "ALL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cascade"

def test_fetch_exists():
    # Check that the Enumeration exists
    assert Fetch is not None

def test_fetch_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Fetch]
    expected_literals = [
        "LAZY",
        "EAGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Fetch"


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
JPA::Anotation_strategy = st.builds(
    JPA::Anotation,
)
JPA::Property_strategy = st.builds(
    JPA::Property,
    comment=
        safe_text,
    name=
        safe_text
)
JPA::Entity_strategy = st.builds(
    JPA::Entity,
    comment=
        safe_text,
    name=
        safe_text
)
JPA::PersistenceUnit_strategy = st.builds(
    JPA::PersistenceUnit,
)
Anotation_strategy = st.builds(
    Anotation,
)
JPA::OneToMany_strategy = st.builds(
    JPA::OneToMany,
    fetch=
        safe_text,
    cascade=
        safe_text
)
JPA::ManyToOne_strategy = st.builds(
    JPA::ManyToOne,
    nullable=
        st.booleans(),
    fetch=
        safe_text,
    joinColumn=
        safe_text
)
JPA::Column_strategy = st.builds(
    JPA::Column,
    fetch=
        safe_text,
    type=
        safe_text,
    name=
        safe_text,
    nullable=
        st.booleans()
)
JPA::Table_strategy = st.builds(
    JPA::Table,
    name=
        safe_text
)
JPA::OneToOne_strategy = st.builds(
    JPA::OneToOne,
    name=
        safe_text,
    referencedColumnName=
        safe_text,
    updatable=
        st.booleans()
)
JPA::ManyToMany_strategy = st.builds(
    JPA::ManyToMany,
    joinColumn=
        safe_text,
    inverseJoinColumn=
        safe_text,
    name=
        safe_text
)
JPA::EntityPk_strategy = st.builds(
    JPA::EntityPk,
    name=
        safe_text
)

@given(instance=JPA::Anotation_strategy)
@settings(max_examples=50)
def test_jpa::anotation_instantiation(instance):
    assert isinstance(instance, JPA::Anotation)

@given(instance=JPA::Property_strategy)
@settings(max_examples=50)
def test_jpa::property_instantiation(instance):
    assert isinstance(instance, JPA::Property)

@given(instance=JPA::Property_strategy)
def test_jpa::property_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=JPA::Property_strategy)
def test_jpa::property_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=JPA::Property_strategy)
def test_jpa::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JPA::Property_strategy)
def test_jpa::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JPA::Entity_strategy)
@settings(max_examples=50)
def test_jpa::entity_instantiation(instance):
    assert isinstance(instance, JPA::Entity)

@given(instance=JPA::Entity_strategy)
def test_jpa::entity_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=JPA::Entity_strategy)
def test_jpa::entity_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=JPA::Entity_strategy)
def test_jpa::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JPA::Entity_strategy)
def test_jpa::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JPA::PersistenceUnit_strategy)
@settings(max_examples=50)
def test_jpa::persistenceunit_instantiation(instance):
    assert isinstance(instance, JPA::PersistenceUnit)

@given(instance=Anotation_strategy)
@settings(max_examples=50)
def test_anotation_instantiation(instance):
    assert isinstance(instance, Anotation)

@given(instance=JPA::OneToMany_strategy)
@settings(max_examples=50)
def test_jpa::onetomany_instantiation(instance):
    assert isinstance(instance, JPA::OneToMany)

@given(instance=JPA::OneToMany_strategy)
def test_jpa::onetomany_fetch_type(instance):
    assert isinstance(instance.fetch, str)


@given(instance=JPA::OneToMany_strategy)
def test_jpa::onetomany_fetch_setter(instance):
    original = instance.fetch
    instance.fetch = original
    assert instance.fetch == original

@given(instance=JPA::OneToMany_strategy)
def test_jpa::onetomany_cascade_type(instance):
    assert isinstance(instance.cascade, str)


@given(instance=JPA::OneToMany_strategy)
def test_jpa::onetomany_cascade_setter(instance):
    original = instance.cascade
    instance.cascade = original
    assert instance.cascade == original

@given(instance=JPA::ManyToOne_strategy)
@settings(max_examples=50)
def test_jpa::manytoone_instantiation(instance):
    assert isinstance(instance, JPA::ManyToOne)

@given(instance=JPA::ManyToOne_strategy)
def test_jpa::manytoone_nullable_type(instance):
    assert isinstance(instance.nullable, bool)


@given(instance=JPA::ManyToOne_strategy)
def test_jpa::manytoone_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=JPA::ManyToOne_strategy)
def test_jpa::manytoone_fetch_type(instance):
    assert isinstance(instance.fetch, str)


@given(instance=JPA::ManyToOne_strategy)
def test_jpa::manytoone_fetch_setter(instance):
    original = instance.fetch
    instance.fetch = original
    assert instance.fetch == original

@given(instance=JPA::ManyToOne_strategy)
def test_jpa::manytoone_joinColumn_type(instance):
    assert isinstance(instance.joinColumn, str)


@given(instance=JPA::ManyToOne_strategy)
def test_jpa::manytoone_joinColumn_setter(instance):
    original = instance.joinColumn
    instance.joinColumn = original
    assert instance.joinColumn == original

@given(instance=JPA::Column_strategy)
@settings(max_examples=50)
def test_jpa::column_instantiation(instance):
    assert isinstance(instance, JPA::Column)

@given(instance=JPA::Column_strategy)
def test_jpa::column_fetch_type(instance):
    assert isinstance(instance.fetch, str)


@given(instance=JPA::Column_strategy)
def test_jpa::column_fetch_setter(instance):
    original = instance.fetch
    instance.fetch = original
    assert instance.fetch == original

@given(instance=JPA::Column_strategy)
def test_jpa::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=JPA::Column_strategy)
def test_jpa::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=JPA::Column_strategy)
def test_jpa::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JPA::Column_strategy)
def test_jpa::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JPA::Column_strategy)
def test_jpa::column_nullable_type(instance):
    assert isinstance(instance.nullable, bool)


@given(instance=JPA::Column_strategy)
def test_jpa::column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=JPA::Table_strategy)
@settings(max_examples=50)
def test_jpa::table_instantiation(instance):
    assert isinstance(instance, JPA::Table)

@given(instance=JPA::Table_strategy)
def test_jpa::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JPA::Table_strategy)
def test_jpa::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JPA::OneToOne_strategy)
@settings(max_examples=50)
def test_jpa::onetoone_instantiation(instance):
    assert isinstance(instance, JPA::OneToOne)

@given(instance=JPA::OneToOne_strategy)
def test_jpa::onetoone_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JPA::OneToOne_strategy)
def test_jpa::onetoone_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JPA::OneToOne_strategy)
def test_jpa::onetoone_referencedColumnName_type(instance):
    assert isinstance(instance.referencedColumnName, str)


@given(instance=JPA::OneToOne_strategy)
def test_jpa::onetoone_referencedColumnName_setter(instance):
    original = instance.referencedColumnName
    instance.referencedColumnName = original
    assert instance.referencedColumnName == original

@given(instance=JPA::OneToOne_strategy)
def test_jpa::onetoone_updatable_type(instance):
    assert isinstance(instance.updatable, bool)


@given(instance=JPA::OneToOne_strategy)
def test_jpa::onetoone_updatable_setter(instance):
    original = instance.updatable
    instance.updatable = original
    assert instance.updatable == original

@given(instance=JPA::ManyToMany_strategy)
@settings(max_examples=50)
def test_jpa::manytomany_instantiation(instance):
    assert isinstance(instance, JPA::ManyToMany)

@given(instance=JPA::ManyToMany_strategy)
def test_jpa::manytomany_joinColumn_type(instance):
    assert isinstance(instance.joinColumn, str)


@given(instance=JPA::ManyToMany_strategy)
def test_jpa::manytomany_joinColumn_setter(instance):
    original = instance.joinColumn
    instance.joinColumn = original
    assert instance.joinColumn == original

@given(instance=JPA::ManyToMany_strategy)
def test_jpa::manytomany_inverseJoinColumn_type(instance):
    assert isinstance(instance.inverseJoinColumn, str)


@given(instance=JPA::ManyToMany_strategy)
def test_jpa::manytomany_inverseJoinColumn_setter(instance):
    original = instance.inverseJoinColumn
    instance.inverseJoinColumn = original
    assert instance.inverseJoinColumn == original

@given(instance=JPA::ManyToMany_strategy)
def test_jpa::manytomany_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JPA::ManyToMany_strategy)
def test_jpa::manytomany_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JPA::EntityPk_strategy)
@settings(max_examples=50)
def test_jpa::entitypk_instantiation(instance):
    assert isinstance(instance, JPA::EntityPk)

@given(instance=JPA::EntityPk_strategy)
def test_jpa::entitypk_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JPA::EntityPk_strategy)
def test_jpa::entitypk_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
