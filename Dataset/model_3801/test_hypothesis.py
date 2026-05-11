import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Connection::EntityRelationship,
    entityrelationship::Attribute::Composite,
    entityrelationship::Connection::EntityRelationship,
    entityrelationship::Generalization,
    entityrelationship::Attribute,
    entityrelationship::Connection::With::Attribute,
    entityrelationship::Connection::E::R::Restriction,
    entityrelationship::Connection::Generalization::Entity,
    entityrelationship::Connection::ConnectionEntityRelationship2Attribute,
    entityrelationship::Connection::Relationship2Entity,
    entityrelationship::Connection::Entity2Relationship,
    entityrelationship::Relationships::Restriction,
    Elements::with::Attributes,
    entityrelationship::Relationship,
    entityrelationship::Entity,
    entityrelationship::Elements::with::Attributes,
    entityrelationship::Entity::Relationship::Model,
    TypeAttribute,
    TypeRestriction,
    TypeIdentifier,
    TypeRestriction2,
    TypeRelationship,
    TypeRestrictionInheritance2,
    TypeEntity,
    TypeRestrictionInheritance1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_connection::entityrelationship_is_not_abstract():
    assert not inspect.isabstract(Connection::EntityRelationship)


def test_connection::entityrelationship_constructor_exists():
    assert callable(Connection::EntityRelationship.__init__)


def test_connection::entityrelationship_constructor_args():
    sig = inspect.signature(Connection::EntityRelationship.__init__)
    params = list(sig.parameters.keys())



def test_entityrelationship::attribute::composite_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Attribute::Composite)


def test_entityrelationship::attribute::composite_constructor_exists():
    assert callable(entityrelationship::Attribute::Composite.__init__)


def test_entityrelationship::attribute::composite_constructor_args():
    sig = inspect.signature(entityrelationship::Attribute::Composite.__init__)
    params = list(sig.parameters.keys())
    assert "identifier_at_composite" in params, "Missing parameter 'identifier_at_composite'"
    assert "name_at_composite" in params, "Missing parameter 'name_at_composite'"

def test_entityrelationship::attribute::composite_has_identifier_at_composite():
    assert hasattr(entityrelationship::Attribute::Composite, "identifier_at_composite")
    descriptor = None
    for klass in entityrelationship::Attribute::Composite.__mro__:
        if "identifier_at_composite" in klass.__dict__:
            descriptor = klass.__dict__["identifier_at_composite"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship::attribute::composite_has_name_at_composite():
    assert hasattr(entityrelationship::Attribute::Composite, "name_at_composite")
    descriptor = None
    for klass in entityrelationship::Attribute::Composite.__mro__:
        if "name_at_composite" in klass.__dict__:
            descriptor = klass.__dict__["name_at_composite"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship::connection::entityrelationship_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Connection::EntityRelationship)


def test_entityrelationship::connection::entityrelationship_constructor_exists():
    assert callable(entityrelationship::Connection::EntityRelationship.__init__)


def test_entityrelationship::connection::entityrelationship_constructor_args():
    sig = inspect.signature(entityrelationship::Connection::EntityRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "role" in params, "Missing parameter 'role'"
    assert "maximum_cardinality" in params, "Missing parameter 'maximum_cardinality'"
    assert "minimum_cardinality" in params, "Missing parameter 'minimum_cardinality'"

def test_entityrelationship::connection::entityrelationship_has_role():
    assert hasattr(entityrelationship::Connection::EntityRelationship, "role")
    descriptor = None
    for klass in entityrelationship::Connection::EntityRelationship.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship::connection::entityrelationship_has_maximum_cardinality():
    assert hasattr(entityrelationship::Connection::EntityRelationship, "maximum_cardinality")
    descriptor = None
    for klass in entityrelationship::Connection::EntityRelationship.__mro__:
        if "maximum_cardinality" in klass.__dict__:
            descriptor = klass.__dict__["maximum_cardinality"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship::connection::entityrelationship_has_minimum_cardinality():
    assert hasattr(entityrelationship::Connection::EntityRelationship, "minimum_cardinality")
    descriptor = None
    for klass in entityrelationship::Connection::EntityRelationship.__mro__:
        if "minimum_cardinality" in klass.__dict__:
            descriptor = klass.__dict__["minimum_cardinality"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship::generalization_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Generalization)


def test_entityrelationship::generalization_constructor_exists():
    assert callable(entityrelationship::Generalization.__init__)


def test_entityrelationship::generalization_constructor_args():
    sig = inspect.signature(entityrelationship::Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "restriction_inheritance_2" in params, "Missing parameter 'restriction_inheritance_2'"
    assert "restriction_inheritance_1" in params, "Missing parameter 'restriction_inheritance_1'"

def test_entityrelationship::generalization_has_restriction_inheritance_2():
    assert hasattr(entityrelationship::Generalization, "restriction_inheritance_2")
    descriptor = None
    for klass in entityrelationship::Generalization.__mro__:
        if "restriction_inheritance_2" in klass.__dict__:
            descriptor = klass.__dict__["restriction_inheritance_2"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship::generalization_has_restriction_inheritance_1():
    assert hasattr(entityrelationship::Generalization, "restriction_inheritance_1")
    descriptor = None
    for klass in entityrelationship::Generalization.__mro__:
        if "restriction_inheritance_1" in klass.__dict__:
            descriptor = klass.__dict__["restriction_inheritance_1"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship::attribute_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Attribute)


def test_entityrelationship::attribute_constructor_exists():
    assert callable(entityrelationship::Attribute.__init__)


def test_entityrelationship::attribute_constructor_args():
    sig = inspect.signature(entityrelationship::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "name_attribute" in params, "Missing parameter 'name_attribute'"

def test_entityrelationship::attribute_has_identifier():
    assert hasattr(entityrelationship::Attribute, "identifier")
    descriptor = None
    for klass in entityrelationship::Attribute.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship::attribute_has_name_attribute():
    assert hasattr(entityrelationship::Attribute, "name_attribute")
    descriptor = None
    for klass in entityrelationship::Attribute.__mro__:
        if "name_attribute" in klass.__dict__:
            descriptor = klass.__dict__["name_attribute"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship::connection::with::attribute_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Connection::With::Attribute)


def test_entityrelationship::connection::with::attribute_constructor_exists():
    assert callable(entityrelationship::Connection::With::Attribute.__init__)


def test_entityrelationship::connection::with::attribute_constructor_args():
    sig = inspect.signature(entityrelationship::Connection::With::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type_attribute" in params, "Missing parameter 'type_attribute'"

def test_entityrelationship::connection::with::attribute_has_type_attribute():
    assert hasattr(entityrelationship::Connection::With::Attribute, "type_attribute")
    descriptor = None
    for klass in entityrelationship::Connection::With::Attribute.__mro__:
        if "type_attribute" in klass.__dict__:
            descriptor = klass.__dict__["type_attribute"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship::connection::e::r::restriction_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Connection::E::R::Restriction)


def test_entityrelationship::connection::e::r::restriction_constructor_exists():
    assert callable(entityrelationship::Connection::E::R::Restriction.__init__)


def test_entityrelationship::connection::e::r::restriction_constructor_args():
    sig = inspect.signature(entityrelationship::Connection::E::R::Restriction.__init__)
    params = list(sig.parameters.keys())
    assert "type_restriction" in params, "Missing parameter 'type_restriction'"

def test_entityrelationship::connection::e::r::restriction_has_type_restriction():
    assert hasattr(entityrelationship::Connection::E::R::Restriction, "type_restriction")
    descriptor = None
    for klass in entityrelationship::Connection::E::R::Restriction.__mro__:
        if "type_restriction" in klass.__dict__:
            descriptor = klass.__dict__["type_restriction"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship::connection::generalization::entity_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Connection::Generalization::Entity)


def test_entityrelationship::connection::generalization::entity_constructor_exists():
    assert callable(entityrelationship::Connection::Generalization::Entity.__init__)


def test_entityrelationship::connection::generalization::entity_constructor_args():
    sig = inspect.signature(entityrelationship::Connection::Generalization::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "maximum_cardinality" in params, "Missing parameter 'maximum_cardinality'"
    assert "minimum_cardinality" in params, "Missing parameter 'minimum_cardinality'"

def test_entityrelationship::connection::generalization::entity_has_maximum_cardinality():
    assert hasattr(entityrelationship::Connection::Generalization::Entity, "maximum_cardinality")
    descriptor = None
    for klass in entityrelationship::Connection::Generalization::Entity.__mro__:
        if "maximum_cardinality" in klass.__dict__:
            descriptor = klass.__dict__["maximum_cardinality"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship::connection::generalization::entity_has_minimum_cardinality():
    assert hasattr(entityrelationship::Connection::Generalization::Entity, "minimum_cardinality")
    descriptor = None
    for klass in entityrelationship::Connection::Generalization::Entity.__mro__:
        if "minimum_cardinality" in klass.__dict__:
            descriptor = klass.__dict__["minimum_cardinality"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship::connection::connectionentityrelationship2attribute_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Connection::ConnectionEntityRelationship2Attribute)


def test_entityrelationship::connection::connectionentityrelationship2attribute_constructor_exists():
    assert callable(entityrelationship::Connection::ConnectionEntityRelationship2Attribute.__init__)


def test_entityrelationship::connection::connectionentityrelationship2attribute_constructor_args():
    sig = inspect.signature(entityrelationship::Connection::ConnectionEntityRelationship2Attribute.__init__)
    params = list(sig.parameters.keys())



def test_entityrelationship::connection::relationship2entity_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Connection::Relationship2Entity)


def test_entityrelationship::connection::relationship2entity_constructor_exists():
    assert callable(entityrelationship::Connection::Relationship2Entity.__init__)


def test_entityrelationship::connection::relationship2entity_constructor_args():
    sig = inspect.signature(entityrelationship::Connection::Relationship2Entity.__init__)
    params = list(sig.parameters.keys())



def test_entityrelationship::connection::entity2relationship_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Connection::Entity2Relationship)


def test_entityrelationship::connection::entity2relationship_constructor_exists():
    assert callable(entityrelationship::Connection::Entity2Relationship.__init__)


def test_entityrelationship::connection::entity2relationship_constructor_args():
    sig = inspect.signature(entityrelationship::Connection::Entity2Relationship.__init__)
    params = list(sig.parameters.keys())



def test_entityrelationship::relationships::restriction_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Relationships::Restriction)


def test_entityrelationship::relationships::restriction_constructor_exists():
    assert callable(entityrelationship::Relationships::Restriction.__init__)


def test_entityrelationship::relationships::restriction_constructor_args():
    sig = inspect.signature(entityrelationship::Relationships::Restriction.__init__)
    params = list(sig.parameters.keys())
    assert "type_restriction" in params, "Missing parameter 'type_restriction'"

def test_entityrelationship::relationships::restriction_has_type_restriction():
    assert hasattr(entityrelationship::Relationships::Restriction, "type_restriction")
    descriptor = None
    for klass in entityrelationship::Relationships::Restriction.__mro__:
        if "type_restriction" in klass.__dict__:
            descriptor = klass.__dict__["type_restriction"]
            break
    assert isinstance(descriptor, property)



def test_elements::with::attributes_is_not_abstract():
    assert not inspect.isabstract(Elements::with::Attributes)


def test_elements::with::attributes_constructor_exists():
    assert callable(Elements::with::Attributes.__init__)


def test_elements::with::attributes_constructor_args():
    sig = inspect.signature(Elements::with::Attributes.__init__)
    params = list(sig.parameters.keys())



def test_entityrelationship::relationship_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Relationship)


def test_entityrelationship::relationship_constructor_exists():
    assert callable(entityrelationship::Relationship.__init__)


def test_entityrelationship::relationship_constructor_args():
    sig = inspect.signature(entityrelationship::Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "type_relationship" in params, "Missing parameter 'type_relationship'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"
    assert "name_relationship" in params, "Missing parameter 'name_relationship'"
    assert "order" in params, "Missing parameter 'order'"

def test_entityrelationship::relationship_has_type_relationship():
    assert hasattr(entityrelationship::Relationship, "type_relationship")
    descriptor = None
    for klass in entityrelationship::Relationship.__mro__:
        if "type_relationship" in klass.__dict__:
            descriptor = klass.__dict__["type_relationship"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship::relationship_has_cardinality():
    assert hasattr(entityrelationship::Relationship, "cardinality")
    descriptor = None
    for klass in entityrelationship::Relationship.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship::relationship_has_name_relationship():
    assert hasattr(entityrelationship::Relationship, "name_relationship")
    descriptor = None
    for klass in entityrelationship::Relationship.__mro__:
        if "name_relationship" in klass.__dict__:
            descriptor = klass.__dict__["name_relationship"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship::relationship_has_order():
    assert hasattr(entityrelationship::Relationship, "order")
    descriptor = None
    for klass in entityrelationship::Relationship.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship::entity_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Entity)


def test_entityrelationship::entity_constructor_exists():
    assert callable(entityrelationship::Entity.__init__)


def test_entityrelationship::entity_constructor_args():
    sig = inspect.signature(entityrelationship::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "type_entity" in params, "Missing parameter 'type_entity'"
    assert "name_entity" in params, "Missing parameter 'name_entity'"

def test_entityrelationship::entity_has_type_entity():
    assert hasattr(entityrelationship::Entity, "type_entity")
    descriptor = None
    for klass in entityrelationship::Entity.__mro__:
        if "type_entity" in klass.__dict__:
            descriptor = klass.__dict__["type_entity"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship::entity_has_name_entity():
    assert hasattr(entityrelationship::Entity, "name_entity")
    descriptor = None
    for klass in entityrelationship::Entity.__mro__:
        if "name_entity" in klass.__dict__:
            descriptor = klass.__dict__["name_entity"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship::elements::with::attributes_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Elements::with::Attributes)


def test_entityrelationship::elements::with::attributes_constructor_exists():
    assert callable(entityrelationship::Elements::with::Attributes.__init__)


def test_entityrelationship::elements::with::attributes_constructor_args():
    sig = inspect.signature(entityrelationship::Elements::with::Attributes.__init__)
    params = list(sig.parameters.keys())



def test_entityrelationship::entity::relationship::model_is_not_abstract():
    assert not inspect.isabstract(entityrelationship::Entity::Relationship::Model)


def test_entityrelationship::entity::relationship::model_constructor_exists():
    assert callable(entityrelationship::Entity::Relationship::Model.__init__)


def test_entityrelationship::entity::relationship::model_constructor_args():
    sig = inspect.signature(entityrelationship::Entity::Relationship::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entityrelationship::entity::relationship::model_has_name():
    assert hasattr(entityrelationship::Entity::Relationship::Model, "name")
    descriptor = None
    for klass in entityrelationship::Entity::Relationship::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_typeattribute_exists():
    # Check that the Enumeration exists
    assert TypeAttribute is not None

def test_typeattribute_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeAttribute]
    expected_literals = [
        "Optional",
        "Composite",
        "Dependence_in_identification",
        "Multivalued",
        "Derived",
        "Normal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeAttribute"

def test_typerestriction_exists():
    # Check that the Enumeration exists
    assert TypeRestriction is not None

def test_typerestriction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeRestriction]
    expected_literals = [
        "Inclusion",
        "Exclusion",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeRestriction"

def test_typeidentifier_exists():
    # Check that the Enumeration exists
    assert TypeIdentifier is not None

def test_typeidentifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeIdentifier]
    expected_literals = [
        "AlternativeIdentifier",
        "NoIdentifier",
        "PrimaryIdentifier",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeIdentifier"

def test_typerestriction2_exists():
    # Check that the Enumeration exists
    assert TypeRestriction2 is not None

def test_typerestriction2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeRestriction2]
    expected_literals = [
        "Exclusiveness",
        "Inclusiveness",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeRestriction2"

def test_typerelationship_exists():
    # Check that the Enumeration exists
    assert TypeRelationship is not None

def test_typerelationship_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeRelationship]
    expected_literals = [
        "Regular",
        "Weak_dependence_in_existence",
        "Weak_dependence_in_identification",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeRelationship"

def test_typerestrictioninheritance2_exists():
    # Check that the Enumeration exists
    assert TypeRestrictionInheritance2 is not None

def test_typerestrictioninheritance2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeRestrictionInheritance2]
    expected_literals = [
        "Overlapped",
        "Exclusive",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeRestrictionInheritance2"

def test_typeentity_exists():
    # Check that the Enumeration exists
    assert TypeEntity is not None

def test_typeentity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeEntity]
    expected_literals = [
        "Regular",
        "Weak",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeEntity"

def test_typerestrictioninheritance1_exists():
    # Check that the Enumeration exists
    assert TypeRestrictionInheritance1 is not None

def test_typerestrictioninheritance1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeRestrictionInheritance1]
    expected_literals = [
        "Total",
        "Partial",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeRestrictionInheritance1"


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
Connection::EntityRelationship_strategy = st.builds(
    Connection::EntityRelationship,
)
entityrelationship::Attribute::Composite_strategy = st.builds(
    entityrelationship::Attribute::Composite,
    identifier_at_composite=
        safe_text,
    name_at_composite=
        safe_text
)
entityrelationship::Connection::EntityRelationship_strategy = st.builds(
    entityrelationship::Connection::EntityRelationship,
    role=
        safe_text,
    maximum_cardinality=
        safe_text,
    minimum_cardinality=
        safe_text
)
entityrelationship::Generalization_strategy = st.builds(
    entityrelationship::Generalization,
    restriction_inheritance_2=
        safe_text,
    restriction_inheritance_1=
        safe_text
)
entityrelationship::Attribute_strategy = st.builds(
    entityrelationship::Attribute,
    identifier=
        safe_text,
    name_attribute=
        safe_text
)
entityrelationship::Connection::With::Attribute_strategy = st.builds(
    entityrelationship::Connection::With::Attribute,
    type_attribute=
        safe_text
)
entityrelationship::Connection::E::R::Restriction_strategy = st.builds(
    entityrelationship::Connection::E::R::Restriction,
    type_restriction=
        safe_text
)
entityrelationship::Connection::Generalization::Entity_strategy = st.builds(
    entityrelationship::Connection::Generalization::Entity,
    maximum_cardinality=
        safe_text,
    minimum_cardinality=
        safe_text
)
entityrelationship::Connection::ConnectionEntityRelationship2Attribute_strategy = st.builds(
    entityrelationship::Connection::ConnectionEntityRelationship2Attribute,
)
entityrelationship::Connection::Relationship2Entity_strategy = st.builds(
    entityrelationship::Connection::Relationship2Entity,
)
entityrelationship::Connection::Entity2Relationship_strategy = st.builds(
    entityrelationship::Connection::Entity2Relationship,
)
entityrelationship::Relationships::Restriction_strategy = st.builds(
    entityrelationship::Relationships::Restriction,
    type_restriction=
        safe_text
)
Elements::with::Attributes_strategy = st.builds(
    Elements::with::Attributes,
)
entityrelationship::Relationship_strategy = st.builds(
    entityrelationship::Relationship,
    type_relationship=
        safe_text,
    cardinality=
        safe_text,
    name_relationship=
        safe_text,
    order=
        st.integers()
)
entityrelationship::Entity_strategy = st.builds(
    entityrelationship::Entity,
    type_entity=
        safe_text,
    name_entity=
        safe_text
)
entityrelationship::Elements::with::Attributes_strategy = st.builds(
    entityrelationship::Elements::with::Attributes,
)
entityrelationship::Entity::Relationship::Model_strategy = st.builds(
    entityrelationship::Entity::Relationship::Model,
    name=
        safe_text
)

@given(instance=Connection::EntityRelationship_strategy)
@settings(max_examples=50)
def test_connection::entityrelationship_instantiation(instance):
    assert isinstance(instance, Connection::EntityRelationship)

@given(instance=entityrelationship::Attribute::Composite_strategy)
@settings(max_examples=50)
def test_entityrelationship::attribute::composite_instantiation(instance):
    assert isinstance(instance, entityrelationship::Attribute::Composite)

@given(instance=entityrelationship::Attribute::Composite_strategy)
def test_entityrelationship::attribute::composite_identifier_at_composite_type(instance):
    assert isinstance(instance.identifier_at_composite, str)


@given(instance=entityrelationship::Attribute::Composite_strategy)
def test_entityrelationship::attribute::composite_identifier_at_composite_setter(instance):
    original = instance.identifier_at_composite
    instance.identifier_at_composite = original
    assert instance.identifier_at_composite == original

@given(instance=entityrelationship::Attribute::Composite_strategy)
def test_entityrelationship::attribute::composite_name_at_composite_type(instance):
    assert isinstance(instance.name_at_composite, str)


@given(instance=entityrelationship::Attribute::Composite_strategy)
def test_entityrelationship::attribute::composite_name_at_composite_setter(instance):
    original = instance.name_at_composite
    instance.name_at_composite = original
    assert instance.name_at_composite == original

@given(instance=entityrelationship::Connection::EntityRelationship_strategy)
@settings(max_examples=50)
def test_entityrelationship::connection::entityrelationship_instantiation(instance):
    assert isinstance(instance, entityrelationship::Connection::EntityRelationship)

@given(instance=entityrelationship::Connection::EntityRelationship_strategy)
def test_entityrelationship::connection::entityrelationship_role_type(instance):
    assert isinstance(instance.role, str)


@given(instance=entityrelationship::Connection::EntityRelationship_strategy)
def test_entityrelationship::connection::entityrelationship_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=entityrelationship::Connection::EntityRelationship_strategy)
def test_entityrelationship::connection::entityrelationship_maximum_cardinality_type(instance):
    assert isinstance(instance.maximum_cardinality, str)


@given(instance=entityrelationship::Connection::EntityRelationship_strategy)
def test_entityrelationship::connection::entityrelationship_maximum_cardinality_setter(instance):
    original = instance.maximum_cardinality
    instance.maximum_cardinality = original
    assert instance.maximum_cardinality == original

@given(instance=entityrelationship::Connection::EntityRelationship_strategy)
def test_entityrelationship::connection::entityrelationship_minimum_cardinality_type(instance):
    assert isinstance(instance.minimum_cardinality, str)


@given(instance=entityrelationship::Connection::EntityRelationship_strategy)
def test_entityrelationship::connection::entityrelationship_minimum_cardinality_setter(instance):
    original = instance.minimum_cardinality
    instance.minimum_cardinality = original
    assert instance.minimum_cardinality == original

@given(instance=entityrelationship::Generalization_strategy)
@settings(max_examples=50)
def test_entityrelationship::generalization_instantiation(instance):
    assert isinstance(instance, entityrelationship::Generalization)

@given(instance=entityrelationship::Generalization_strategy)
def test_entityrelationship::generalization_restriction_inheritance_2_type(instance):
    assert isinstance(instance.restriction_inheritance_2, str)


@given(instance=entityrelationship::Generalization_strategy)
def test_entityrelationship::generalization_restriction_inheritance_2_setter(instance):
    original = instance.restriction_inheritance_2
    instance.restriction_inheritance_2 = original
    assert instance.restriction_inheritance_2 == original

@given(instance=entityrelationship::Generalization_strategy)
def test_entityrelationship::generalization_restriction_inheritance_1_type(instance):
    assert isinstance(instance.restriction_inheritance_1, str)


@given(instance=entityrelationship::Generalization_strategy)
def test_entityrelationship::generalization_restriction_inheritance_1_setter(instance):
    original = instance.restriction_inheritance_1
    instance.restriction_inheritance_1 = original
    assert instance.restriction_inheritance_1 == original

@given(instance=entityrelationship::Attribute_strategy)
@settings(max_examples=50)
def test_entityrelationship::attribute_instantiation(instance):
    assert isinstance(instance, entityrelationship::Attribute)

@given(instance=entityrelationship::Attribute_strategy)
def test_entityrelationship::attribute_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=entityrelationship::Attribute_strategy)
def test_entityrelationship::attribute_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=entityrelationship::Attribute_strategy)
def test_entityrelationship::attribute_name_attribute_type(instance):
    assert isinstance(instance.name_attribute, str)


@given(instance=entityrelationship::Attribute_strategy)
def test_entityrelationship::attribute_name_attribute_setter(instance):
    original = instance.name_attribute
    instance.name_attribute = original
    assert instance.name_attribute == original

@given(instance=entityrelationship::Connection::With::Attribute_strategy)
@settings(max_examples=50)
def test_entityrelationship::connection::with::attribute_instantiation(instance):
    assert isinstance(instance, entityrelationship::Connection::With::Attribute)

@given(instance=entityrelationship::Connection::With::Attribute_strategy)
def test_entityrelationship::connection::with::attribute_type_attribute_type(instance):
    assert isinstance(instance.type_attribute, str)


@given(instance=entityrelationship::Connection::With::Attribute_strategy)
def test_entityrelationship::connection::with::attribute_type_attribute_setter(instance):
    original = instance.type_attribute
    instance.type_attribute = original
    assert instance.type_attribute == original

@given(instance=entityrelationship::Connection::E::R::Restriction_strategy)
@settings(max_examples=50)
def test_entityrelationship::connection::e::r::restriction_instantiation(instance):
    assert isinstance(instance, entityrelationship::Connection::E::R::Restriction)

@given(instance=entityrelationship::Connection::E::R::Restriction_strategy)
def test_entityrelationship::connection::e::r::restriction_type_restriction_type(instance):
    assert isinstance(instance.type_restriction, str)


@given(instance=entityrelationship::Connection::E::R::Restriction_strategy)
def test_entityrelationship::connection::e::r::restriction_type_restriction_setter(instance):
    original = instance.type_restriction
    instance.type_restriction = original
    assert instance.type_restriction == original

@given(instance=entityrelationship::Connection::Generalization::Entity_strategy)
@settings(max_examples=50)
def test_entityrelationship::connection::generalization::entity_instantiation(instance):
    assert isinstance(instance, entityrelationship::Connection::Generalization::Entity)

@given(instance=entityrelationship::Connection::Generalization::Entity_strategy)
def test_entityrelationship::connection::generalization::entity_maximum_cardinality_type(instance):
    assert isinstance(instance.maximum_cardinality, str)


@given(instance=entityrelationship::Connection::Generalization::Entity_strategy)
def test_entityrelationship::connection::generalization::entity_maximum_cardinality_setter(instance):
    original = instance.maximum_cardinality
    instance.maximum_cardinality = original
    assert instance.maximum_cardinality == original

@given(instance=entityrelationship::Connection::Generalization::Entity_strategy)
def test_entityrelationship::connection::generalization::entity_minimum_cardinality_type(instance):
    assert isinstance(instance.minimum_cardinality, str)


@given(instance=entityrelationship::Connection::Generalization::Entity_strategy)
def test_entityrelationship::connection::generalization::entity_minimum_cardinality_setter(instance):
    original = instance.minimum_cardinality
    instance.minimum_cardinality = original
    assert instance.minimum_cardinality == original

@given(instance=entityrelationship::Connection::ConnectionEntityRelationship2Attribute_strategy)
@settings(max_examples=50)
def test_entityrelationship::connection::connectionentityrelationship2attribute_instantiation(instance):
    assert isinstance(instance, entityrelationship::Connection::ConnectionEntityRelationship2Attribute)

@given(instance=entityrelationship::Connection::Relationship2Entity_strategy)
@settings(max_examples=50)
def test_entityrelationship::connection::relationship2entity_instantiation(instance):
    assert isinstance(instance, entityrelationship::Connection::Relationship2Entity)

@given(instance=entityrelationship::Connection::Entity2Relationship_strategy)
@settings(max_examples=50)
def test_entityrelationship::connection::entity2relationship_instantiation(instance):
    assert isinstance(instance, entityrelationship::Connection::Entity2Relationship)

@given(instance=entityrelationship::Relationships::Restriction_strategy)
@settings(max_examples=50)
def test_entityrelationship::relationships::restriction_instantiation(instance):
    assert isinstance(instance, entityrelationship::Relationships::Restriction)

@given(instance=entityrelationship::Relationships::Restriction_strategy)
def test_entityrelationship::relationships::restriction_type_restriction_type(instance):
    assert isinstance(instance.type_restriction, str)


@given(instance=entityrelationship::Relationships::Restriction_strategy)
def test_entityrelationship::relationships::restriction_type_restriction_setter(instance):
    original = instance.type_restriction
    instance.type_restriction = original
    assert instance.type_restriction == original

@given(instance=Elements::with::Attributes_strategy)
@settings(max_examples=50)
def test_elements::with::attributes_instantiation(instance):
    assert isinstance(instance, Elements::with::Attributes)

@given(instance=entityrelationship::Relationship_strategy)
@settings(max_examples=50)
def test_entityrelationship::relationship_instantiation(instance):
    assert isinstance(instance, entityrelationship::Relationship)

@given(instance=entityrelationship::Relationship_strategy)
def test_entityrelationship::relationship_type_relationship_type(instance):
    assert isinstance(instance.type_relationship, str)


@given(instance=entityrelationship::Relationship_strategy)
def test_entityrelationship::relationship_type_relationship_setter(instance):
    original = instance.type_relationship
    instance.type_relationship = original
    assert instance.type_relationship == original

@given(instance=entityrelationship::Relationship_strategy)
def test_entityrelationship::relationship_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=entityrelationship::Relationship_strategy)
def test_entityrelationship::relationship_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=entityrelationship::Relationship_strategy)
def test_entityrelationship::relationship_name_relationship_type(instance):
    assert isinstance(instance.name_relationship, str)


@given(instance=entityrelationship::Relationship_strategy)
def test_entityrelationship::relationship_name_relationship_setter(instance):
    original = instance.name_relationship
    instance.name_relationship = original
    assert instance.name_relationship == original

@given(instance=entityrelationship::Relationship_strategy)
def test_entityrelationship::relationship_order_type(instance):
    assert isinstance(instance.order, int)


@given(instance=entityrelationship::Relationship_strategy)
def test_entityrelationship::relationship_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=entityrelationship::Entity_strategy)
@settings(max_examples=50)
def test_entityrelationship::entity_instantiation(instance):
    assert isinstance(instance, entityrelationship::Entity)

@given(instance=entityrelationship::Entity_strategy)
def test_entityrelationship::entity_type_entity_type(instance):
    assert isinstance(instance.type_entity, str)


@given(instance=entityrelationship::Entity_strategy)
def test_entityrelationship::entity_type_entity_setter(instance):
    original = instance.type_entity
    instance.type_entity = original
    assert instance.type_entity == original

@given(instance=entityrelationship::Entity_strategy)
def test_entityrelationship::entity_name_entity_type(instance):
    assert isinstance(instance.name_entity, str)


@given(instance=entityrelationship::Entity_strategy)
def test_entityrelationship::entity_name_entity_setter(instance):
    original = instance.name_entity
    instance.name_entity = original
    assert instance.name_entity == original

@given(instance=entityrelationship::Elements::with::Attributes_strategy)
@settings(max_examples=50)
def test_entityrelationship::elements::with::attributes_instantiation(instance):
    assert isinstance(instance, entityrelationship::Elements::with::Attributes)

@given(instance=entityrelationship::Entity::Relationship::Model_strategy)
@settings(max_examples=50)
def test_entityrelationship::entity::relationship::model_instantiation(instance):
    assert isinstance(instance, entityrelationship::Entity::Relationship::Model)

@given(instance=entityrelationship::Entity::Relationship::Model_strategy)
def test_entityrelationship::entity::relationship::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entityrelationship::Entity::Relationship::Model_strategy)
def test_entityrelationship::entity::relationship::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
