import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Connection_EntityRelationship,
    entityrelationship_Attribute_Composite,
    entityrelationship_Connection_EntityRelationship,
    entityrelationship_Generalization,
    entityrelationship_Attribute,
    entityrelationship_Connection_With_Attribute,
    entityrelationship_Connection_E_R_Restriction,
    entityrelationship_Connection_Generalization_Entity,
    entityrelationship_Connection_ConnectionEntityRelationship2Attribute,
    entityrelationship_Connection_Relationship2Entity,
    entityrelationship_Connection_Entity2Relationship,
    entityrelationship_Relationships_Restriction,
    Elements_with_Attributes,
    entityrelationship_Relationship,
    entityrelationship_Entity,
    entityrelationship_Elements_with_Attributes,
    entityrelationship_Entity_Relationship_Model,
    TypeRestriction2,
    TypeAttribute,
    TypeRestrictionInheritance1,
    TypeRestrictionInheritance2,
    TypeIdentifier,
    TypeEntity,
    TypeRestriction,
    TypeRelationship,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_connection_entityrelationship_is_not_abstract():
    assert not inspect.isabstract(Connection_EntityRelationship)


def test_connection_entityrelationship_constructor_exists():
    assert callable(Connection_EntityRelationship.__init__)


def test_connection_entityrelationship_constructor_args():
    sig = inspect.signature(Connection_EntityRelationship.__init__)
    params = list(sig.parameters.keys())



def test_entityrelationship_attribute_composite_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Attribute_Composite)


def test_entityrelationship_attribute_composite_constructor_exists():
    assert callable(entityrelationship_Attribute_Composite.__init__)


def test_entityrelationship_attribute_composite_constructor_args():
    sig = inspect.signature(entityrelationship_Attribute_Composite.__init__)
    params = list(sig.parameters.keys())
    assert "identifier_at_composite" in params, "Missing parameter 'identifier_at_composite'"
    assert "name_at_composite" in params, "Missing parameter 'name_at_composite'"

def test_entityrelationship_attribute_composite_has_identifier_at_composite():
    assert hasattr(entityrelationship_Attribute_Composite, "identifier_at_composite")
    descriptor = None
    for klass in entityrelationship_Attribute_Composite.__mro__:
        if "identifier_at_composite" in klass.__dict__:
            descriptor = klass.__dict__["identifier_at_composite"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship_attribute_composite_has_name_at_composite():
    assert hasattr(entityrelationship_Attribute_Composite, "name_at_composite")
    descriptor = None
    for klass in entityrelationship_Attribute_Composite.__mro__:
        if "name_at_composite" in klass.__dict__:
            descriptor = klass.__dict__["name_at_composite"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship_connection_entityrelationship_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Connection_EntityRelationship)


def test_entityrelationship_connection_entityrelationship_constructor_exists():
    assert callable(entityrelationship_Connection_EntityRelationship.__init__)


def test_entityrelationship_connection_entityrelationship_constructor_args():
    sig = inspect.signature(entityrelationship_Connection_EntityRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "minimum_cardinality" in params, "Missing parameter 'minimum_cardinality'"
    assert "maximum_cardinality" in params, "Missing parameter 'maximum_cardinality'"
    assert "role" in params, "Missing parameter 'role'"

def test_entityrelationship_connection_entityrelationship_has_minimum_cardinality():
    assert hasattr(entityrelationship_Connection_EntityRelationship, "minimum_cardinality")
    descriptor = None
    for klass in entityrelationship_Connection_EntityRelationship.__mro__:
        if "minimum_cardinality" in klass.__dict__:
            descriptor = klass.__dict__["minimum_cardinality"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship_connection_entityrelationship_has_maximum_cardinality():
    assert hasattr(entityrelationship_Connection_EntityRelationship, "maximum_cardinality")
    descriptor = None
    for klass in entityrelationship_Connection_EntityRelationship.__mro__:
        if "maximum_cardinality" in klass.__dict__:
            descriptor = klass.__dict__["maximum_cardinality"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship_connection_entityrelationship_has_role():
    assert hasattr(entityrelationship_Connection_EntityRelationship, "role")
    descriptor = None
    for klass in entityrelationship_Connection_EntityRelationship.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship_generalization_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Generalization)


def test_entityrelationship_generalization_constructor_exists():
    assert callable(entityrelationship_Generalization.__init__)


def test_entityrelationship_generalization_constructor_args():
    sig = inspect.signature(entityrelationship_Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "restriction_inheritance_2" in params, "Missing parameter 'restriction_inheritance_2'"
    assert "restriction_inheritance_1" in params, "Missing parameter 'restriction_inheritance_1'"

def test_entityrelationship_generalization_has_restriction_inheritance_2():
    assert hasattr(entityrelationship_Generalization, "restriction_inheritance_2")
    descriptor = None
    for klass in entityrelationship_Generalization.__mro__:
        if "restriction_inheritance_2" in klass.__dict__:
            descriptor = klass.__dict__["restriction_inheritance_2"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship_generalization_has_restriction_inheritance_1():
    assert hasattr(entityrelationship_Generalization, "restriction_inheritance_1")
    descriptor = None
    for klass in entityrelationship_Generalization.__mro__:
        if "restriction_inheritance_1" in klass.__dict__:
            descriptor = klass.__dict__["restriction_inheritance_1"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship_attribute_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Attribute)


def test_entityrelationship_attribute_constructor_exists():
    assert callable(entityrelationship_Attribute.__init__)


def test_entityrelationship_attribute_constructor_args():
    sig = inspect.signature(entityrelationship_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "name_attribute" in params, "Missing parameter 'name_attribute'"

def test_entityrelationship_attribute_has_identifier():
    assert hasattr(entityrelationship_Attribute, "identifier")
    descriptor = None
    for klass in entityrelationship_Attribute.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship_attribute_has_name_attribute():
    assert hasattr(entityrelationship_Attribute, "name_attribute")
    descriptor = None
    for klass in entityrelationship_Attribute.__mro__:
        if "name_attribute" in klass.__dict__:
            descriptor = klass.__dict__["name_attribute"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship_connection_with_attribute_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Connection_With_Attribute)


def test_entityrelationship_connection_with_attribute_constructor_exists():
    assert callable(entityrelationship_Connection_With_Attribute.__init__)


def test_entityrelationship_connection_with_attribute_constructor_args():
    sig = inspect.signature(entityrelationship_Connection_With_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type_attribute" in params, "Missing parameter 'type_attribute'"

def test_entityrelationship_connection_with_attribute_has_type_attribute():
    assert hasattr(entityrelationship_Connection_With_Attribute, "type_attribute")
    descriptor = None
    for klass in entityrelationship_Connection_With_Attribute.__mro__:
        if "type_attribute" in klass.__dict__:
            descriptor = klass.__dict__["type_attribute"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship_connection_e_r_restriction_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Connection_E_R_Restriction)


def test_entityrelationship_connection_e_r_restriction_constructor_exists():
    assert callable(entityrelationship_Connection_E_R_Restriction.__init__)


def test_entityrelationship_connection_e_r_restriction_constructor_args():
    sig = inspect.signature(entityrelationship_Connection_E_R_Restriction.__init__)
    params = list(sig.parameters.keys())
    assert "type_restriction" in params, "Missing parameter 'type_restriction'"

def test_entityrelationship_connection_e_r_restriction_has_type_restriction():
    assert hasattr(entityrelationship_Connection_E_R_Restriction, "type_restriction")
    descriptor = None
    for klass in entityrelationship_Connection_E_R_Restriction.__mro__:
        if "type_restriction" in klass.__dict__:
            descriptor = klass.__dict__["type_restriction"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship_connection_generalization_entity_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Connection_Generalization_Entity)


def test_entityrelationship_connection_generalization_entity_constructor_exists():
    assert callable(entityrelationship_Connection_Generalization_Entity.__init__)


def test_entityrelationship_connection_generalization_entity_constructor_args():
    sig = inspect.signature(entityrelationship_Connection_Generalization_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "maximum_cardinality" in params, "Missing parameter 'maximum_cardinality'"
    assert "minimum_cardinality" in params, "Missing parameter 'minimum_cardinality'"

def test_entityrelationship_connection_generalization_entity_has_maximum_cardinality():
    assert hasattr(entityrelationship_Connection_Generalization_Entity, "maximum_cardinality")
    descriptor = None
    for klass in entityrelationship_Connection_Generalization_Entity.__mro__:
        if "maximum_cardinality" in klass.__dict__:
            descriptor = klass.__dict__["maximum_cardinality"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship_connection_generalization_entity_has_minimum_cardinality():
    assert hasattr(entityrelationship_Connection_Generalization_Entity, "minimum_cardinality")
    descriptor = None
    for klass in entityrelationship_Connection_Generalization_Entity.__mro__:
        if "minimum_cardinality" in klass.__dict__:
            descriptor = klass.__dict__["minimum_cardinality"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship_connection_connectionentityrelationship2attribute_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Connection_ConnectionEntityRelationship2Attribute)


def test_entityrelationship_connection_connectionentityrelationship2attribute_constructor_exists():
    assert callable(entityrelationship_Connection_ConnectionEntityRelationship2Attribute.__init__)


def test_entityrelationship_connection_connectionentityrelationship2attribute_constructor_args():
    sig = inspect.signature(entityrelationship_Connection_ConnectionEntityRelationship2Attribute.__init__)
    params = list(sig.parameters.keys())



def test_entityrelationship_connection_relationship2entity_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Connection_Relationship2Entity)


def test_entityrelationship_connection_relationship2entity_constructor_exists():
    assert callable(entityrelationship_Connection_Relationship2Entity.__init__)


def test_entityrelationship_connection_relationship2entity_constructor_args():
    sig = inspect.signature(entityrelationship_Connection_Relationship2Entity.__init__)
    params = list(sig.parameters.keys())



def test_entityrelationship_connection_entity2relationship_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Connection_Entity2Relationship)


def test_entityrelationship_connection_entity2relationship_constructor_exists():
    assert callable(entityrelationship_Connection_Entity2Relationship.__init__)


def test_entityrelationship_connection_entity2relationship_constructor_args():
    sig = inspect.signature(entityrelationship_Connection_Entity2Relationship.__init__)
    params = list(sig.parameters.keys())



def test_entityrelationship_relationships_restriction_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Relationships_Restriction)


def test_entityrelationship_relationships_restriction_constructor_exists():
    assert callable(entityrelationship_Relationships_Restriction.__init__)


def test_entityrelationship_relationships_restriction_constructor_args():
    sig = inspect.signature(entityrelationship_Relationships_Restriction.__init__)
    params = list(sig.parameters.keys())
    assert "type_restriction" in params, "Missing parameter 'type_restriction'"

def test_entityrelationship_relationships_restriction_has_type_restriction():
    assert hasattr(entityrelationship_Relationships_Restriction, "type_restriction")
    descriptor = None
    for klass in entityrelationship_Relationships_Restriction.__mro__:
        if "type_restriction" in klass.__dict__:
            descriptor = klass.__dict__["type_restriction"]
            break
    assert isinstance(descriptor, property)



def test_elements_with_attributes_is_not_abstract():
    assert not inspect.isabstract(Elements_with_Attributes)


def test_elements_with_attributes_constructor_exists():
    assert callable(Elements_with_Attributes.__init__)


def test_elements_with_attributes_constructor_args():
    sig = inspect.signature(Elements_with_Attributes.__init__)
    params = list(sig.parameters.keys())



def test_entityrelationship_relationship_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Relationship)


def test_entityrelationship_relationship_constructor_exists():
    assert callable(entityrelationship_Relationship.__init__)


def test_entityrelationship_relationship_constructor_args():
    sig = inspect.signature(entityrelationship_Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"
    assert "name_relationship" in params, "Missing parameter 'name_relationship'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"
    assert "type_relationship" in params, "Missing parameter 'type_relationship'"

def test_entityrelationship_relationship_has_order():
    assert hasattr(entityrelationship_Relationship, "order")
    descriptor = None
    for klass in entityrelationship_Relationship.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship_relationship_has_name_relationship():
    assert hasattr(entityrelationship_Relationship, "name_relationship")
    descriptor = None
    for klass in entityrelationship_Relationship.__mro__:
        if "name_relationship" in klass.__dict__:
            descriptor = klass.__dict__["name_relationship"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship_relationship_has_cardinality():
    assert hasattr(entityrelationship_Relationship, "cardinality")
    descriptor = None
    for klass in entityrelationship_Relationship.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship_relationship_has_type_relationship():
    assert hasattr(entityrelationship_Relationship, "type_relationship")
    descriptor = None
    for klass in entityrelationship_Relationship.__mro__:
        if "type_relationship" in klass.__dict__:
            descriptor = klass.__dict__["type_relationship"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship_entity_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Entity)


def test_entityrelationship_entity_constructor_exists():
    assert callable(entityrelationship_Entity.__init__)


def test_entityrelationship_entity_constructor_args():
    sig = inspect.signature(entityrelationship_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name_entity" in params, "Missing parameter 'name_entity'"
    assert "type_entity" in params, "Missing parameter 'type_entity'"

def test_entityrelationship_entity_has_name_entity():
    assert hasattr(entityrelationship_Entity, "name_entity")
    descriptor = None
    for klass in entityrelationship_Entity.__mro__:
        if "name_entity" in klass.__dict__:
            descriptor = klass.__dict__["name_entity"]
            break
    assert isinstance(descriptor, property)

def test_entityrelationship_entity_has_type_entity():
    assert hasattr(entityrelationship_Entity, "type_entity")
    descriptor = None
    for klass in entityrelationship_Entity.__mro__:
        if "type_entity" in klass.__dict__:
            descriptor = klass.__dict__["type_entity"]
            break
    assert isinstance(descriptor, property)



def test_entityrelationship_elements_with_attributes_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Elements_with_Attributes)


def test_entityrelationship_elements_with_attributes_constructor_exists():
    assert callable(entityrelationship_Elements_with_Attributes.__init__)


def test_entityrelationship_elements_with_attributes_constructor_args():
    sig = inspect.signature(entityrelationship_Elements_with_Attributes.__init__)
    params = list(sig.parameters.keys())



def test_entityrelationship_entity_relationship_model_is_not_abstract():
    assert not inspect.isabstract(entityrelationship_Entity_Relationship_Model)


def test_entityrelationship_entity_relationship_model_constructor_exists():
    assert callable(entityrelationship_Entity_Relationship_Model.__init__)


def test_entityrelationship_entity_relationship_model_constructor_args():
    sig = inspect.signature(entityrelationship_Entity_Relationship_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entityrelationship_entity_relationship_model_has_name():
    assert hasattr(entityrelationship_Entity_Relationship_Model, "name")
    descriptor = None
    for klass in entityrelationship_Entity_Relationship_Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_typerestriction2_exists():
    # Check that the Enumeration exists
    assert TypeRestriction2 is not None

def test_typerestriction2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeRestriction2]
    expected_literals = [
        "Inclusiveness",
        "Exclusiveness",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeRestriction2"

def test_typeattribute_exists():
    # Check that the Enumeration exists
    assert TypeAttribute is not None

def test_typeattribute_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeAttribute]
    expected_literals = [
        "Dependence_in_identification",
        "Optional",
        "Multivalued",
        "Derived",
        "Composite",
        "Normal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeAttribute"

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

def test_typeidentifier_exists():
    # Check that the Enumeration exists
    assert TypeIdentifier is not None

def test_typeidentifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeIdentifier]
    expected_literals = [
        "NoIdentifier",
        "AlternativeIdentifier",
        "PrimaryIdentifier",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeIdentifier"

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

def test_typerestriction_exists():
    # Check that the Enumeration exists
    assert TypeRestriction is not None

def test_typerestriction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeRestriction]
    expected_literals = [
        "Exclusion",
        "Inclusion",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeRestriction"

def test_typerelationship_exists():
    # Check that the Enumeration exists
    assert TypeRelationship is not None

def test_typerelationship_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeRelationship]
    expected_literals = [
        "Weak_dependence_in_identification",
        "Weak_dependence_in_existence",
        "Regular",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeRelationship"


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
Connection_EntityRelationship_strategy = st.builds(
    Connection_EntityRelationship,
)
entityrelationship_Attribute_Composite_strategy = st.builds(
    entityrelationship_Attribute_Composite,
    identifier_at_composite=
        safe_text,
    name_at_composite=
        safe_text
)
entityrelationship_Connection_EntityRelationship_strategy = st.builds(
    entityrelationship_Connection_EntityRelationship,
    minimum_cardinality=
        safe_text,
    maximum_cardinality=
        safe_text,
    role=
        safe_text
)
entityrelationship_Generalization_strategy = st.builds(
    entityrelationship_Generalization,
    restriction_inheritance_2=
        safe_text,
    restriction_inheritance_1=
        safe_text
)
entityrelationship_Attribute_strategy = st.builds(
    entityrelationship_Attribute,
    identifier=
        safe_text,
    name_attribute=
        safe_text
)
entityrelationship_Connection_With_Attribute_strategy = st.builds(
    entityrelationship_Connection_With_Attribute,
    type_attribute=
        safe_text
)
entityrelationship_Connection_E_R_Restriction_strategy = st.builds(
    entityrelationship_Connection_E_R_Restriction,
    type_restriction=
        safe_text
)
entityrelationship_Connection_Generalization_Entity_strategy = st.builds(
    entityrelationship_Connection_Generalization_Entity,
    maximum_cardinality=
        safe_text,
    minimum_cardinality=
        safe_text
)
entityrelationship_Connection_ConnectionEntityRelationship2Attribute_strategy = st.builds(
    entityrelationship_Connection_ConnectionEntityRelationship2Attribute,
)
entityrelationship_Connection_Relationship2Entity_strategy = st.builds(
    entityrelationship_Connection_Relationship2Entity,
)
entityrelationship_Connection_Entity2Relationship_strategy = st.builds(
    entityrelationship_Connection_Entity2Relationship,
)
entityrelationship_Relationships_Restriction_strategy = st.builds(
    entityrelationship_Relationships_Restriction,
    type_restriction=
        safe_text
)
Elements_with_Attributes_strategy = st.builds(
    Elements_with_Attributes,
)
entityrelationship_Relationship_strategy = st.builds(
    entityrelationship_Relationship,
    order=
        st.integers(),
    name_relationship=
        safe_text,
    cardinality=
        safe_text,
    type_relationship=
        safe_text
)
entityrelationship_Entity_strategy = st.builds(
    entityrelationship_Entity,
    name_entity=
        safe_text,
    type_entity=
        safe_text
)
entityrelationship_Elements_with_Attributes_strategy = st.builds(
    entityrelationship_Elements_with_Attributes,
)
entityrelationship_Entity_Relationship_Model_strategy = st.builds(
    entityrelationship_Entity_Relationship_Model,
    name=
        safe_text
)

@given(instance=Connection_EntityRelationship_strategy)
@settings(max_examples=50)
def test_connection_entityrelationship_instantiation(instance):
    assert isinstance(instance, Connection_EntityRelationship)

@given(instance=entityrelationship_Attribute_Composite_strategy)
@settings(max_examples=50)
def test_entityrelationship_attribute_composite_instantiation(instance):
    assert isinstance(instance, entityrelationship_Attribute_Composite)



@given(instance=entityrelationship_Attribute_Composite_strategy)
def test_entityrelationship_attribute_composite_identifier_at_composite_setter(instance):
    original = instance.identifier_at_composite
    instance.identifier_at_composite = original
    assert instance.identifier_at_composite == original



@given(instance=entityrelationship_Attribute_Composite_strategy)
def test_entityrelationship_attribute_composite_name_at_composite_setter(instance):
    original = instance.name_at_composite
    instance.name_at_composite = original
    assert instance.name_at_composite == original

@given(instance=entityrelationship_Connection_EntityRelationship_strategy)
@settings(max_examples=50)
def test_entityrelationship_connection_entityrelationship_instantiation(instance):
    assert isinstance(instance, entityrelationship_Connection_EntityRelationship)



@given(instance=entityrelationship_Connection_EntityRelationship_strategy)
def test_entityrelationship_connection_entityrelationship_minimum_cardinality_setter(instance):
    original = instance.minimum_cardinality
    instance.minimum_cardinality = original
    assert instance.minimum_cardinality == original



@given(instance=entityrelationship_Connection_EntityRelationship_strategy)
def test_entityrelationship_connection_entityrelationship_maximum_cardinality_setter(instance):
    original = instance.maximum_cardinality
    instance.maximum_cardinality = original
    assert instance.maximum_cardinality == original



@given(instance=entityrelationship_Connection_EntityRelationship_strategy)
def test_entityrelationship_connection_entityrelationship_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=entityrelationship_Generalization_strategy)
@settings(max_examples=50)
def test_entityrelationship_generalization_instantiation(instance):
    assert isinstance(instance, entityrelationship_Generalization)



@given(instance=entityrelationship_Generalization_strategy)
def test_entityrelationship_generalization_restriction_inheritance_2_setter(instance):
    original = instance.restriction_inheritance_2
    instance.restriction_inheritance_2 = original
    assert instance.restriction_inheritance_2 == original



@given(instance=entityrelationship_Generalization_strategy)
def test_entityrelationship_generalization_restriction_inheritance_1_setter(instance):
    original = instance.restriction_inheritance_1
    instance.restriction_inheritance_1 = original
    assert instance.restriction_inheritance_1 == original

@given(instance=entityrelationship_Attribute_strategy)
@settings(max_examples=50)
def test_entityrelationship_attribute_instantiation(instance):
    assert isinstance(instance, entityrelationship_Attribute)



@given(instance=entityrelationship_Attribute_strategy)
def test_entityrelationship_attribute_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=entityrelationship_Attribute_strategy)
def test_entityrelationship_attribute_name_attribute_setter(instance):
    original = instance.name_attribute
    instance.name_attribute = original
    assert instance.name_attribute == original

@given(instance=entityrelationship_Connection_With_Attribute_strategy)
@settings(max_examples=50)
def test_entityrelationship_connection_with_attribute_instantiation(instance):
    assert isinstance(instance, entityrelationship_Connection_With_Attribute)



@given(instance=entityrelationship_Connection_With_Attribute_strategy)
def test_entityrelationship_connection_with_attribute_type_attribute_setter(instance):
    original = instance.type_attribute
    instance.type_attribute = original
    assert instance.type_attribute == original

@given(instance=entityrelationship_Connection_E_R_Restriction_strategy)
@settings(max_examples=50)
def test_entityrelationship_connection_e_r_restriction_instantiation(instance):
    assert isinstance(instance, entityrelationship_Connection_E_R_Restriction)



@given(instance=entityrelationship_Connection_E_R_Restriction_strategy)
def test_entityrelationship_connection_e_r_restriction_type_restriction_setter(instance):
    original = instance.type_restriction
    instance.type_restriction = original
    assert instance.type_restriction == original

@given(instance=entityrelationship_Connection_Generalization_Entity_strategy)
@settings(max_examples=50)
def test_entityrelationship_connection_generalization_entity_instantiation(instance):
    assert isinstance(instance, entityrelationship_Connection_Generalization_Entity)



@given(instance=entityrelationship_Connection_Generalization_Entity_strategy)
def test_entityrelationship_connection_generalization_entity_maximum_cardinality_setter(instance):
    original = instance.maximum_cardinality
    instance.maximum_cardinality = original
    assert instance.maximum_cardinality == original



@given(instance=entityrelationship_Connection_Generalization_Entity_strategy)
def test_entityrelationship_connection_generalization_entity_minimum_cardinality_setter(instance):
    original = instance.minimum_cardinality
    instance.minimum_cardinality = original
    assert instance.minimum_cardinality == original

@given(instance=entityrelationship_Connection_ConnectionEntityRelationship2Attribute_strategy)
@settings(max_examples=50)
def test_entityrelationship_connection_connectionentityrelationship2attribute_instantiation(instance):
    assert isinstance(instance, entityrelationship_Connection_ConnectionEntityRelationship2Attribute)

@given(instance=entityrelationship_Connection_Relationship2Entity_strategy)
@settings(max_examples=50)
def test_entityrelationship_connection_relationship2entity_instantiation(instance):
    assert isinstance(instance, entityrelationship_Connection_Relationship2Entity)

@given(instance=entityrelationship_Connection_Entity2Relationship_strategy)
@settings(max_examples=50)
def test_entityrelationship_connection_entity2relationship_instantiation(instance):
    assert isinstance(instance, entityrelationship_Connection_Entity2Relationship)

@given(instance=entityrelationship_Relationships_Restriction_strategy)
@settings(max_examples=50)
def test_entityrelationship_relationships_restriction_instantiation(instance):
    assert isinstance(instance, entityrelationship_Relationships_Restriction)



@given(instance=entityrelationship_Relationships_Restriction_strategy)
def test_entityrelationship_relationships_restriction_type_restriction_setter(instance):
    original = instance.type_restriction
    instance.type_restriction = original
    assert instance.type_restriction == original

@given(instance=Elements_with_Attributes_strategy)
@settings(max_examples=50)
def test_elements_with_attributes_instantiation(instance):
    assert isinstance(instance, Elements_with_Attributes)

@given(instance=entityrelationship_Relationship_strategy)
@settings(max_examples=50)
def test_entityrelationship_relationship_instantiation(instance):
    assert isinstance(instance, entityrelationship_Relationship)



@given(instance=entityrelationship_Relationship_strategy)
def test_entityrelationship_relationship_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original



@given(instance=entityrelationship_Relationship_strategy)
def test_entityrelationship_relationship_name_relationship_setter(instance):
    original = instance.name_relationship
    instance.name_relationship = original
    assert instance.name_relationship == original



@given(instance=entityrelationship_Relationship_strategy)
def test_entityrelationship_relationship_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original



@given(instance=entityrelationship_Relationship_strategy)
def test_entityrelationship_relationship_type_relationship_setter(instance):
    original = instance.type_relationship
    instance.type_relationship = original
    assert instance.type_relationship == original

@given(instance=entityrelationship_Entity_strategy)
@settings(max_examples=50)
def test_entityrelationship_entity_instantiation(instance):
    assert isinstance(instance, entityrelationship_Entity)



@given(instance=entityrelationship_Entity_strategy)
def test_entityrelationship_entity_name_entity_setter(instance):
    original = instance.name_entity
    instance.name_entity = original
    assert instance.name_entity == original



@given(instance=entityrelationship_Entity_strategy)
def test_entityrelationship_entity_type_entity_setter(instance):
    original = instance.type_entity
    instance.type_entity = original
    assert instance.type_entity == original

@given(instance=entityrelationship_Elements_with_Attributes_strategy)
@settings(max_examples=50)
def test_entityrelationship_elements_with_attributes_instantiation(instance):
    assert isinstance(instance, entityrelationship_Elements_with_Attributes)

@given(instance=entityrelationship_Entity_Relationship_Model_strategy)
@settings(max_examples=50)
def test_entityrelationship_entity_relationship_model_instantiation(instance):
    assert isinstance(instance, entityrelationship_Entity_Relationship_Model)



@given(instance=entityrelationship_Entity_Relationship_Model_strategy)
def test_entityrelationship_entity_relationship_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
