import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    JPA_Anotation,
    JPA_Property,
    JPA_Entity,
    JPA_PersistenceUnit,
    Anotation,
    JPA_ManyToOne,
    JPA_ManyToMany,
    JPA_Column,
    JPA_Table,
    JPA_OneToOne,
    JPA_OneToMany,
    JPA_EntityPk,
    Fetch,
    Cascade,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jpa_anotation_is_not_abstract():
    assert not inspect.isabstract(JPA_Anotation)


def test_jpa_anotation_constructor_exists():
    assert callable(JPA_Anotation.__init__)


def test_jpa_anotation_constructor_args():
    sig = inspect.signature(JPA_Anotation.__init__)
    params = list(sig.parameters.keys())



def test_jpa_property_is_not_abstract():
    assert not inspect.isabstract(JPA_Property)


def test_jpa_property_constructor_exists():
    assert callable(JPA_Property.__init__)


def test_jpa_property_constructor_args():
    sig = inspect.signature(JPA_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_jpa_property_has_name():
    assert hasattr(JPA_Property, "name")
    descriptor = None
    for klass in JPA_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpa_property_has_comment():
    assert hasattr(JPA_Property, "comment")
    descriptor = None
    for klass in JPA_Property.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_jpa_entity_is_not_abstract():
    assert not inspect.isabstract(JPA_Entity)


def test_jpa_entity_constructor_exists():
    assert callable(JPA_Entity.__init__)


def test_jpa_entity_constructor_args():
    sig = inspect.signature(JPA_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_jpa_entity_has_comment():
    assert hasattr(JPA_Entity, "comment")
    descriptor = None
    for klass in JPA_Entity.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_jpa_entity_has_name():
    assert hasattr(JPA_Entity, "name")
    descriptor = None
    for klass in JPA_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpa_persistenceunit_is_not_abstract():
    assert not inspect.isabstract(JPA_PersistenceUnit)


def test_jpa_persistenceunit_constructor_exists():
    assert callable(JPA_PersistenceUnit.__init__)


def test_jpa_persistenceunit_constructor_args():
    sig = inspect.signature(JPA_PersistenceUnit.__init__)
    params = list(sig.parameters.keys())



def test_anotation_is_not_abstract():
    assert not inspect.isabstract(Anotation)


def test_anotation_constructor_exists():
    assert callable(Anotation.__init__)


def test_anotation_constructor_args():
    sig = inspect.signature(Anotation.__init__)
    params = list(sig.parameters.keys())



def test_jpa_manytoone_is_not_abstract():
    assert not inspect.isabstract(JPA_ManyToOne)


def test_jpa_manytoone_constructor_exists():
    assert callable(JPA_ManyToOne.__init__)


def test_jpa_manytoone_constructor_args():
    sig = inspect.signature(JPA_ManyToOne.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "referencedEntityName" in params, "Missing parameter 'referencedEntityName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "referencedPropertyName" in params, "Missing parameter 'referencedPropertyName'"

def test_jpa_manytoone_has_type():
    assert hasattr(JPA_ManyToOne, "type")
    descriptor = None
    for klass in JPA_ManyToOne.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_jpa_manytoone_has_referencedEntityName():
    assert hasattr(JPA_ManyToOne, "referencedEntityName")
    descriptor = None
    for klass in JPA_ManyToOne.__mro__:
        if "referencedEntityName" in klass.__dict__:
            descriptor = klass.__dict__["referencedEntityName"]
            break
    assert isinstance(descriptor, property)

def test_jpa_manytoone_has_name():
    assert hasattr(JPA_ManyToOne, "name")
    descriptor = None
    for klass in JPA_ManyToOne.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpa_manytoone_has_referencedPropertyName():
    assert hasattr(JPA_ManyToOne, "referencedPropertyName")
    descriptor = None
    for klass in JPA_ManyToOne.__mro__:
        if "referencedPropertyName" in klass.__dict__:
            descriptor = klass.__dict__["referencedPropertyName"]
            break
    assert isinstance(descriptor, property)



def test_jpa_manytomany_is_not_abstract():
    assert not inspect.isabstract(JPA_ManyToMany)


def test_jpa_manytomany_constructor_exists():
    assert callable(JPA_ManyToMany.__init__)


def test_jpa_manytomany_constructor_args():
    sig = inspect.signature(JPA_ManyToMany.__init__)
    params = list(sig.parameters.keys())



def test_jpa_column_is_not_abstract():
    assert not inspect.isabstract(JPA_Column)


def test_jpa_column_constructor_exists():
    assert callable(JPA_Column.__init__)


def test_jpa_column_constructor_args():
    sig = inspect.signature(JPA_Column.__init__)
    params = list(sig.parameters.keys())
    assert "fetch" in params, "Missing parameter 'fetch'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "nullable" in params, "Missing parameter 'nullable'"

def test_jpa_column_has_fetch():
    assert hasattr(JPA_Column, "fetch")
    descriptor = None
    for klass in JPA_Column.__mro__:
        if "fetch" in klass.__dict__:
            descriptor = klass.__dict__["fetch"]
            break
    assert isinstance(descriptor, property)

def test_jpa_column_has_type():
    assert hasattr(JPA_Column, "type")
    descriptor = None
    for klass in JPA_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_jpa_column_has_name():
    assert hasattr(JPA_Column, "name")
    descriptor = None
    for klass in JPA_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpa_column_has_nullable():
    assert hasattr(JPA_Column, "nullable")
    descriptor = None
    for klass in JPA_Column.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)



def test_jpa_table_is_not_abstract():
    assert not inspect.isabstract(JPA_Table)


def test_jpa_table_constructor_exists():
    assert callable(JPA_Table.__init__)


def test_jpa_table_constructor_args():
    sig = inspect.signature(JPA_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpa_table_has_name():
    assert hasattr(JPA_Table, "name")
    descriptor = None
    for klass in JPA_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpa_onetoone_is_not_abstract():
    assert not inspect.isabstract(JPA_OneToOne)


def test_jpa_onetoone_constructor_exists():
    assert callable(JPA_OneToOne.__init__)


def test_jpa_onetoone_constructor_args():
    sig = inspect.signature(JPA_OneToOne.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "referencedPropertyName" in params, "Missing parameter 'referencedPropertyName'"
    assert "type" in params, "Missing parameter 'type'"
    assert "referencedEntityName" in params, "Missing parameter 'referencedEntityName'"

def test_jpa_onetoone_has_name():
    assert hasattr(JPA_OneToOne, "name")
    descriptor = None
    for klass in JPA_OneToOne.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpa_onetoone_has_referencedPropertyName():
    assert hasattr(JPA_OneToOne, "referencedPropertyName")
    descriptor = None
    for klass in JPA_OneToOne.__mro__:
        if "referencedPropertyName" in klass.__dict__:
            descriptor = klass.__dict__["referencedPropertyName"]
            break
    assert isinstance(descriptor, property)

def test_jpa_onetoone_has_type():
    assert hasattr(JPA_OneToOne, "type")
    descriptor = None
    for klass in JPA_OneToOne.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_jpa_onetoone_has_referencedEntityName():
    assert hasattr(JPA_OneToOne, "referencedEntityName")
    descriptor = None
    for klass in JPA_OneToOne.__mro__:
        if "referencedEntityName" in klass.__dict__:
            descriptor = klass.__dict__["referencedEntityName"]
            break
    assert isinstance(descriptor, property)



def test_jpa_onetomany_is_not_abstract():
    assert not inspect.isabstract(JPA_OneToMany)


def test_jpa_onetomany_constructor_exists():
    assert callable(JPA_OneToMany.__init__)


def test_jpa_onetomany_constructor_args():
    sig = inspect.signature(JPA_OneToMany.__init__)
    params = list(sig.parameters.keys())
    assert "referencedEntityName" in params, "Missing parameter 'referencedEntityName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_jpa_onetomany_has_referencedEntityName():
    assert hasattr(JPA_OneToMany, "referencedEntityName")
    descriptor = None
    for klass in JPA_OneToMany.__mro__:
        if "referencedEntityName" in klass.__dict__:
            descriptor = klass.__dict__["referencedEntityName"]
            break
    assert isinstance(descriptor, property)

def test_jpa_onetomany_has_name():
    assert hasattr(JPA_OneToMany, "name")
    descriptor = None
    for klass in JPA_OneToMany.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpa_onetomany_has_type():
    assert hasattr(JPA_OneToMany, "type")
    descriptor = None
    for klass in JPA_OneToMany.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_jpa_entitypk_is_not_abstract():
    assert not inspect.isabstract(JPA_EntityPk)


def test_jpa_entitypk_constructor_exists():
    assert callable(JPA_EntityPk.__init__)


def test_jpa_entitypk_constructor_args():
    sig = inspect.signature(JPA_EntityPk.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpa_entitypk_has_name():
    assert hasattr(JPA_EntityPk, "name")
    descriptor = None
    for klass in JPA_EntityPk.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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

def test_cascade_exists():
    # Check that the Enumeration exists
    assert Cascade is not None

def test_cascade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cascade]
    expected_literals = [
        "REFRESH",
        "PERSIST",
        "ALL",
        "MERGE",
        "REMOVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cascade"


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
JPA_Anotation_strategy = st.builds(
    JPA_Anotation,
)
JPA_Property_strategy = st.builds(
    JPA_Property,
    name=
        safe_text,
    comment=
        safe_text
)
JPA_Entity_strategy = st.builds(
    JPA_Entity,
    comment=
        safe_text,
    name=
        safe_text
)
JPA_PersistenceUnit_strategy = st.builds(
    JPA_PersistenceUnit,
)
Anotation_strategy = st.builds(
    Anotation,
)
JPA_ManyToOne_strategy = st.builds(
    JPA_ManyToOne,
    type=
        safe_text,
    referencedEntityName=
        safe_text,
    name=
        safe_text,
    referencedPropertyName=
        safe_text
)
JPA_ManyToMany_strategy = st.builds(
    JPA_ManyToMany,
)
JPA_Column_strategy = st.builds(
    JPA_Column,
    fetch=
        safe_text,
    type=
        safe_text,
    name=
        safe_text,
    nullable=
        st.booleans()
)
JPA_Table_strategy = st.builds(
    JPA_Table,
    name=
        safe_text
)
JPA_OneToOne_strategy = st.builds(
    JPA_OneToOne,
    name=
        safe_text,
    referencedPropertyName=
        safe_text,
    type=
        safe_text,
    referencedEntityName=
        safe_text
)
JPA_OneToMany_strategy = st.builds(
    JPA_OneToMany,
    referencedEntityName=
        safe_text,
    name=
        safe_text,
    type=
        safe_text
)
JPA_EntityPk_strategy = st.builds(
    JPA_EntityPk,
    name=
        safe_text
)

@given(instance=JPA_Anotation_strategy)
@settings(max_examples=50)
def test_jpa_anotation_instantiation(instance):
    assert isinstance(instance, JPA_Anotation)

@given(instance=JPA_Property_strategy)
@settings(max_examples=50)
def test_jpa_property_instantiation(instance):
    assert isinstance(instance, JPA_Property)



@given(instance=JPA_Property_strategy)
def test_jpa_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=JPA_Property_strategy)
def test_jpa_property_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=JPA_Entity_strategy)
@settings(max_examples=50)
def test_jpa_entity_instantiation(instance):
    assert isinstance(instance, JPA_Entity)



@given(instance=JPA_Entity_strategy)
def test_jpa_entity_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=JPA_Entity_strategy)
def test_jpa_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JPA_PersistenceUnit_strategy)
@settings(max_examples=50)
def test_jpa_persistenceunit_instantiation(instance):
    assert isinstance(instance, JPA_PersistenceUnit)

@given(instance=Anotation_strategy)
@settings(max_examples=50)
def test_anotation_instantiation(instance):
    assert isinstance(instance, Anotation)

@given(instance=JPA_ManyToOne_strategy)
@settings(max_examples=50)
def test_jpa_manytoone_instantiation(instance):
    assert isinstance(instance, JPA_ManyToOne)



@given(instance=JPA_ManyToOne_strategy)
def test_jpa_manytoone_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=JPA_ManyToOne_strategy)
def test_jpa_manytoone_referencedEntityName_setter(instance):
    original = instance.referencedEntityName
    instance.referencedEntityName = original
    assert instance.referencedEntityName == original



@given(instance=JPA_ManyToOne_strategy)
def test_jpa_manytoone_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=JPA_ManyToOne_strategy)
def test_jpa_manytoone_referencedPropertyName_setter(instance):
    original = instance.referencedPropertyName
    instance.referencedPropertyName = original
    assert instance.referencedPropertyName == original

@given(instance=JPA_ManyToMany_strategy)
@settings(max_examples=50)
def test_jpa_manytomany_instantiation(instance):
    assert isinstance(instance, JPA_ManyToMany)

@given(instance=JPA_Column_strategy)
@settings(max_examples=50)
def test_jpa_column_instantiation(instance):
    assert isinstance(instance, JPA_Column)



@given(instance=JPA_Column_strategy)
def test_jpa_column_fetch_setter(instance):
    original = instance.fetch
    instance.fetch = original
    assert instance.fetch == original



@given(instance=JPA_Column_strategy)
def test_jpa_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=JPA_Column_strategy)
def test_jpa_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=JPA_Column_strategy)
def test_jpa_column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=JPA_Table_strategy)
@settings(max_examples=50)
def test_jpa_table_instantiation(instance):
    assert isinstance(instance, JPA_Table)



@given(instance=JPA_Table_strategy)
def test_jpa_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JPA_OneToOne_strategy)
@settings(max_examples=50)
def test_jpa_onetoone_instantiation(instance):
    assert isinstance(instance, JPA_OneToOne)



@given(instance=JPA_OneToOne_strategy)
def test_jpa_onetoone_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=JPA_OneToOne_strategy)
def test_jpa_onetoone_referencedPropertyName_setter(instance):
    original = instance.referencedPropertyName
    instance.referencedPropertyName = original
    assert instance.referencedPropertyName == original



@given(instance=JPA_OneToOne_strategy)
def test_jpa_onetoone_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=JPA_OneToOne_strategy)
def test_jpa_onetoone_referencedEntityName_setter(instance):
    original = instance.referencedEntityName
    instance.referencedEntityName = original
    assert instance.referencedEntityName == original

@given(instance=JPA_OneToMany_strategy)
@settings(max_examples=50)
def test_jpa_onetomany_instantiation(instance):
    assert isinstance(instance, JPA_OneToMany)



@given(instance=JPA_OneToMany_strategy)
def test_jpa_onetomany_referencedEntityName_setter(instance):
    original = instance.referencedEntityName
    instance.referencedEntityName = original
    assert instance.referencedEntityName == original



@given(instance=JPA_OneToMany_strategy)
def test_jpa_onetomany_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=JPA_OneToMany_strategy)
def test_jpa_onetomany_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=JPA_EntityPk_strategy)
@settings(max_examples=50)
def test_jpa_entitypk_instantiation(instance):
    assert isinstance(instance, JPA_EntityPk)



@given(instance=JPA_EntityPk_strategy)
def test_jpa_entitypk_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
