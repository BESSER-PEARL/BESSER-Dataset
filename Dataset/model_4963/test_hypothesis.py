import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RoleConstraint,
    crom::l1::RoleEquivalence,
    crom::l1::RoleImplication,
    Constraint,
    crom::l1::Test,
    crom::l1::RoleConstraint,
    crom::l1::Part,
    crom::l1::RoleProhibition,
    crom::l1::Constraint,
    RoleGroupElement,
    Inheritance,
    crom::l1::CompartmentInheritance,
    crom::l1::DataInheritance,
    crom::l1::NaturalInheritance,
    crom::l1::Player,
    crom::l1::AbstractRole,
    Relation,
    crom::l1::Inheritance,
    crom::l1::Fulfillment,
    AntiRigidType,
    AbstractRole,
    Player,
    RigidType,
    crom::l1::CompartmentType,
    crom::l1::DataType,
    crom::l1::NaturalType,
    crom::l1::AbstractRoleRef,
    crom::l1::RoleGroupElement,
    TypedElement,
    crom::l1::Operation,
    crom::l1::Parameter,
    Model,
    ModelElement,
    crom::l1::Group,
    Type,
    crom::l1::AntiRigidType,
    crom::l1::RigidType,
    crom::l1::Relation,
    crom::l1::Model,
    NamedElement,
    crom::l1::RelationTarget,
    crom::l1::TypedElement,
    crom::l1::ModelElement,
    crom::l1::NamedElement,
    RelationTarget,
    crom::l1::Type,
    crom::l1::RoleGroup,
    crom::l1::RoleType,
    crom::l1::Attribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_roleconstraint_is_not_abstract():
    assert not inspect.isabstract(RoleConstraint)


def test_roleconstraint_constructor_exists():
    assert callable(RoleConstraint.__init__)


def test_roleconstraint_constructor_args():
    sig = inspect.signature(RoleConstraint.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::roleequivalence_is_not_abstract():
    assert not inspect.isabstract(crom::l1::RoleEquivalence)


def test_crom::l1::roleequivalence_constructor_exists():
    assert callable(crom::l1::RoleEquivalence.__init__)


def test_crom::l1::roleequivalence_constructor_args():
    sig = inspect.signature(crom::l1::RoleEquivalence.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::roleimplication_is_not_abstract():
    assert not inspect.isabstract(crom::l1::RoleImplication)


def test_crom::l1::roleimplication_constructor_exists():
    assert callable(crom::l1::RoleImplication.__init__)


def test_crom::l1::roleimplication_constructor_args():
    sig = inspect.signature(crom::l1::RoleImplication.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::test_is_not_abstract():
    assert not inspect.isabstract(crom::l1::Test)


def test_crom::l1::test_constructor_exists():
    assert callable(crom::l1::Test.__init__)


def test_crom::l1::test_constructor_args():
    sig = inspect.signature(crom::l1::Test.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::roleconstraint_is_not_abstract():
    assert not inspect.isabstract(crom::l1::RoleConstraint)


def test_crom::l1::roleconstraint_constructor_exists():
    assert callable(crom::l1::RoleConstraint.__init__)


def test_crom::l1::roleconstraint_constructor_args():
    sig = inspect.signature(crom::l1::RoleConstraint.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::part_is_not_abstract():
    assert not inspect.isabstract(crom::l1::Part)


def test_crom::l1::part_constructor_exists():
    assert callable(crom::l1::Part.__init__)


def test_crom::l1::part_constructor_args():
    sig = inspect.signature(crom::l1::Part.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_crom::l1::part_has_lower():
    assert hasattr(crom::l1::Part, "lower")
    descriptor = None
    for klass in crom::l1::Part.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_crom::l1::part_has_upper():
    assert hasattr(crom::l1::Part, "upper")
    descriptor = None
    for klass in crom::l1::Part.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_crom::l1::roleprohibition_is_not_abstract():
    assert not inspect.isabstract(crom::l1::RoleProhibition)


def test_crom::l1::roleprohibition_constructor_exists():
    assert callable(crom::l1::RoleProhibition.__init__)


def test_crom::l1::roleprohibition_constructor_args():
    sig = inspect.signature(crom::l1::RoleProhibition.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::constraint_is_not_abstract():
    assert not inspect.isabstract(crom::l1::Constraint)


def test_crom::l1::constraint_constructor_exists():
    assert callable(crom::l1::Constraint.__init__)


def test_crom::l1::constraint_constructor_args():
    sig = inspect.signature(crom::l1::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_rolegroupelement_is_not_abstract():
    assert not inspect.isabstract(RoleGroupElement)


def test_rolegroupelement_constructor_exists():
    assert callable(RoleGroupElement.__init__)


def test_rolegroupelement_constructor_args():
    sig = inspect.signature(RoleGroupElement.__init__)
    params = list(sig.parameters.keys())



def test_inheritance_is_not_abstract():
    assert not inspect.isabstract(Inheritance)


def test_inheritance_constructor_exists():
    assert callable(Inheritance.__init__)


def test_inheritance_constructor_args():
    sig = inspect.signature(Inheritance.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::compartmentinheritance_is_not_abstract():
    assert not inspect.isabstract(crom::l1::CompartmentInheritance)


def test_crom::l1::compartmentinheritance_constructor_exists():
    assert callable(crom::l1::CompartmentInheritance.__init__)


def test_crom::l1::compartmentinheritance_constructor_args():
    sig = inspect.signature(crom::l1::CompartmentInheritance.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::datainheritance_is_not_abstract():
    assert not inspect.isabstract(crom::l1::DataInheritance)


def test_crom::l1::datainheritance_constructor_exists():
    assert callable(crom::l1::DataInheritance.__init__)


def test_crom::l1::datainheritance_constructor_args():
    sig = inspect.signature(crom::l1::DataInheritance.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::naturalinheritance_is_not_abstract():
    assert not inspect.isabstract(crom::l1::NaturalInheritance)


def test_crom::l1::naturalinheritance_constructor_exists():
    assert callable(crom::l1::NaturalInheritance.__init__)


def test_crom::l1::naturalinheritance_constructor_args():
    sig = inspect.signature(crom::l1::NaturalInheritance.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::player_is_not_abstract():
    assert not inspect.isabstract(crom::l1::Player)


def test_crom::l1::player_constructor_exists():
    assert callable(crom::l1::Player.__init__)


def test_crom::l1::player_constructor_args():
    sig = inspect.signature(crom::l1::Player.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::abstractrole_is_not_abstract():
    assert not inspect.isabstract(crom::l1::AbstractRole)


def test_crom::l1::abstractrole_constructor_exists():
    assert callable(crom::l1::AbstractRole.__init__)


def test_crom::l1::abstractrole_constructor_args():
    sig = inspect.signature(crom::l1::AbstractRole.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::inheritance_is_not_abstract():
    assert not inspect.isabstract(crom::l1::Inheritance)


def test_crom::l1::inheritance_constructor_exists():
    assert callable(crom::l1::Inheritance.__init__)


def test_crom::l1::inheritance_constructor_args():
    sig = inspect.signature(crom::l1::Inheritance.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::fulfillment_is_not_abstract():
    assert not inspect.isabstract(crom::l1::Fulfillment)


def test_crom::l1::fulfillment_constructor_exists():
    assert callable(crom::l1::Fulfillment.__init__)


def test_crom::l1::fulfillment_constructor_args():
    sig = inspect.signature(crom::l1::Fulfillment.__init__)
    params = list(sig.parameters.keys())



def test_antirigidtype_is_not_abstract():
    assert not inspect.isabstract(AntiRigidType)


def test_antirigidtype_constructor_exists():
    assert callable(AntiRigidType.__init__)


def test_antirigidtype_constructor_args():
    sig = inspect.signature(AntiRigidType.__init__)
    params = list(sig.parameters.keys())



def test_abstractrole_is_not_abstract():
    assert not inspect.isabstract(AbstractRole)


def test_abstractrole_constructor_exists():
    assert callable(AbstractRole.__init__)


def test_abstractrole_constructor_args():
    sig = inspect.signature(AbstractRole.__init__)
    params = list(sig.parameters.keys())



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())



def test_rigidtype_is_not_abstract():
    assert not inspect.isabstract(RigidType)


def test_rigidtype_constructor_exists():
    assert callable(RigidType.__init__)


def test_rigidtype_constructor_args():
    sig = inspect.signature(RigidType.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::compartmenttype_is_not_abstract():
    assert not inspect.isabstract(crom::l1::CompartmentType)


def test_crom::l1::compartmenttype_constructor_exists():
    assert callable(crom::l1::CompartmentType.__init__)


def test_crom::l1::compartmenttype_constructor_args():
    sig = inspect.signature(crom::l1::CompartmentType.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::datatype_is_not_abstract():
    assert not inspect.isabstract(crom::l1::DataType)


def test_crom::l1::datatype_constructor_exists():
    assert callable(crom::l1::DataType.__init__)


def test_crom::l1::datatype_constructor_args():
    sig = inspect.signature(crom::l1::DataType.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::naturaltype_is_not_abstract():
    assert not inspect.isabstract(crom::l1::NaturalType)


def test_crom::l1::naturaltype_constructor_exists():
    assert callable(crom::l1::NaturalType.__init__)


def test_crom::l1::naturaltype_constructor_args():
    sig = inspect.signature(crom::l1::NaturalType.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::abstractroleref_is_not_abstract():
    assert not inspect.isabstract(crom::l1::AbstractRoleRef)


def test_crom::l1::abstractroleref_constructor_exists():
    assert callable(crom::l1::AbstractRoleRef.__init__)


def test_crom::l1::abstractroleref_constructor_args():
    sig = inspect.signature(crom::l1::AbstractRoleRef.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::rolegroupelement_is_not_abstract():
    assert not inspect.isabstract(crom::l1::RoleGroupElement)


def test_crom::l1::rolegroupelement_constructor_exists():
    assert callable(crom::l1::RoleGroupElement.__init__)


def test_crom::l1::rolegroupelement_constructor_args():
    sig = inspect.signature(crom::l1::RoleGroupElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::operation_is_not_abstract():
    assert not inspect.isabstract(crom::l1::Operation)


def test_crom::l1::operation_constructor_exists():
    assert callable(crom::l1::Operation.__init__)


def test_crom::l1::operation_constructor_args():
    sig = inspect.signature(crom::l1::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_crom::l1::operation_has_operation():
    assert hasattr(crom::l1::Operation, "operation")
    descriptor = None
    for klass in crom::l1::Operation.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_crom::l1::parameter_is_not_abstract():
    assert not inspect.isabstract(crom::l1::Parameter)


def test_crom::l1::parameter_constructor_exists():
    assert callable(crom::l1::Parameter.__init__)


def test_crom::l1::parameter_constructor_args():
    sig = inspect.signature(crom::l1::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_model_is_not_abstract():
    assert not inspect.isabstract(Model)


def test_model_constructor_exists():
    assert callable(Model.__init__)


def test_model_constructor_args():
    sig = inspect.signature(Model.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::group_is_not_abstract():
    assert not inspect.isabstract(crom::l1::Group)


def test_crom::l1::group_constructor_exists():
    assert callable(crom::l1::Group.__init__)


def test_crom::l1::group_constructor_args():
    sig = inspect.signature(crom::l1::Group.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::antirigidtype_is_not_abstract():
    assert not inspect.isabstract(crom::l1::AntiRigidType)


def test_crom::l1::antirigidtype_constructor_exists():
    assert callable(crom::l1::AntiRigidType.__init__)


def test_crom::l1::antirigidtype_constructor_args():
    sig = inspect.signature(crom::l1::AntiRigidType.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::rigidtype_is_not_abstract():
    assert not inspect.isabstract(crom::l1::RigidType)


def test_crom::l1::rigidtype_constructor_exists():
    assert callable(crom::l1::RigidType.__init__)


def test_crom::l1::rigidtype_constructor_args():
    sig = inspect.signature(crom::l1::RigidType.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::relation_is_not_abstract():
    assert not inspect.isabstract(crom::l1::Relation)


def test_crom::l1::relation_constructor_exists():
    assert callable(crom::l1::Relation.__init__)


def test_crom::l1::relation_constructor_args():
    sig = inspect.signature(crom::l1::Relation.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::model_is_not_abstract():
    assert not inspect.isabstract(crom::l1::Model)


def test_crom::l1::model_constructor_exists():
    assert callable(crom::l1::Model.__init__)


def test_crom::l1::model_constructor_args():
    sig = inspect.signature(crom::l1::Model.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::relationtarget_is_not_abstract():
    assert not inspect.isabstract(crom::l1::RelationTarget)


def test_crom::l1::relationtarget_constructor_exists():
    assert callable(crom::l1::RelationTarget.__init__)


def test_crom::l1::relationtarget_constructor_args():
    sig = inspect.signature(crom::l1::RelationTarget.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::typedelement_is_not_abstract():
    assert not inspect.isabstract(crom::l1::TypedElement)


def test_crom::l1::typedelement_constructor_exists():
    assert callable(crom::l1::TypedElement.__init__)


def test_crom::l1::typedelement_constructor_args():
    sig = inspect.signature(crom::l1::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::modelelement_is_not_abstract():
    assert not inspect.isabstract(crom::l1::ModelElement)


def test_crom::l1::modelelement_constructor_exists():
    assert callable(crom::l1::ModelElement.__init__)


def test_crom::l1::modelelement_constructor_args():
    sig = inspect.signature(crom::l1::ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::namedelement_is_not_abstract():
    assert not inspect.isabstract(crom::l1::NamedElement)


def test_crom::l1::namedelement_constructor_exists():
    assert callable(crom::l1::NamedElement.__init__)


def test_crom::l1::namedelement_constructor_args():
    sig = inspect.signature(crom::l1::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_crom::l1::namedelement_has_name():
    assert hasattr(crom::l1::NamedElement, "name")
    descriptor = None
    for klass in crom::l1::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relationtarget_is_not_abstract():
    assert not inspect.isabstract(RelationTarget)


def test_relationtarget_constructor_exists():
    assert callable(RelationTarget.__init__)


def test_relationtarget_constructor_args():
    sig = inspect.signature(RelationTarget.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::type_is_not_abstract():
    assert not inspect.isabstract(crom::l1::Type)


def test_crom::l1::type_constructor_exists():
    assert callable(crom::l1::Type.__init__)


def test_crom::l1::type_constructor_args():
    sig = inspect.signature(crom::l1::Type.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::rolegroup_is_not_abstract():
    assert not inspect.isabstract(crom::l1::RoleGroup)


def test_crom::l1::rolegroup_constructor_exists():
    assert callable(crom::l1::RoleGroup.__init__)


def test_crom::l1::rolegroup_constructor_args():
    sig = inspect.signature(crom::l1::RoleGroup.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_crom::l1::rolegroup_has_lower():
    assert hasattr(crom::l1::RoleGroup, "lower")
    descriptor = None
    for klass in crom::l1::RoleGroup.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_crom::l1::rolegroup_has_upper():
    assert hasattr(crom::l1::RoleGroup, "upper")
    descriptor = None
    for klass in crom::l1::RoleGroup.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_crom::l1::roletype_is_not_abstract():
    assert not inspect.isabstract(crom::l1::RoleType)


def test_crom::l1::roletype_constructor_exists():
    assert callable(crom::l1::RoleType.__init__)


def test_crom::l1::roletype_constructor_args():
    sig = inspect.signature(crom::l1::RoleType.__init__)
    params = list(sig.parameters.keys())



def test_crom::l1::attribute_is_not_abstract():
    assert not inspect.isabstract(crom::l1::Attribute)


def test_crom::l1::attribute_constructor_exists():
    assert callable(crom::l1::Attribute.__init__)


def test_crom::l1::attribute_constructor_args():
    sig = inspect.signature(crom::l1::Attribute.__init__)
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
RoleConstraint_strategy = st.builds(
    RoleConstraint,
)
crom::l1::RoleEquivalence_strategy = st.builds(
    crom::l1::RoleEquivalence,
)
crom::l1::RoleImplication_strategy = st.builds(
    crom::l1::RoleImplication,
)
Constraint_strategy = st.builds(
    Constraint,
)
crom::l1::Test_strategy = st.builds(
    crom::l1::Test,
)
crom::l1::RoleConstraint_strategy = st.builds(
    crom::l1::RoleConstraint,
)
crom::l1::Part_strategy = st.builds(
    crom::l1::Part,
    lower=
        st.integers(),
    upper=
        st.integers()
)
crom::l1::RoleProhibition_strategy = st.builds(
    crom::l1::RoleProhibition,
)
crom::l1::Constraint_strategy = st.builds(
    crom::l1::Constraint,
)
RoleGroupElement_strategy = st.builds(
    RoleGroupElement,
)
Inheritance_strategy = st.builds(
    Inheritance,
)
crom::l1::CompartmentInheritance_strategy = st.builds(
    crom::l1::CompartmentInheritance,
)
crom::l1::DataInheritance_strategy = st.builds(
    crom::l1::DataInheritance,
)
crom::l1::NaturalInheritance_strategy = st.builds(
    crom::l1::NaturalInheritance,
)
crom::l1::Player_strategy = st.builds(
    crom::l1::Player,
)
crom::l1::AbstractRole_strategy = st.builds(
    crom::l1::AbstractRole,
)
Relation_strategy = st.builds(
    Relation,
)
crom::l1::Inheritance_strategy = st.builds(
    crom::l1::Inheritance,
)
crom::l1::Fulfillment_strategy = st.builds(
    crom::l1::Fulfillment,
)
AntiRigidType_strategy = st.builds(
    AntiRigidType,
)
AbstractRole_strategy = st.builds(
    AbstractRole,
)
Player_strategy = st.builds(
    Player,
)
RigidType_strategy = st.builds(
    RigidType,
)
crom::l1::CompartmentType_strategy = st.builds(
    crom::l1::CompartmentType,
)
crom::l1::DataType_strategy = st.builds(
    crom::l1::DataType,
)
crom::l1::NaturalType_strategy = st.builds(
    crom::l1::NaturalType,
)
crom::l1::AbstractRoleRef_strategy = st.builds(
    crom::l1::AbstractRoleRef,
)
crom::l1::RoleGroupElement_strategy = st.builds(
    crom::l1::RoleGroupElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
crom::l1::Operation_strategy = st.builds(
    crom::l1::Operation,
    operation=
        safe_text
)
crom::l1::Parameter_strategy = st.builds(
    crom::l1::Parameter,
)
Model_strategy = st.builds(
    Model,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
crom::l1::Group_strategy = st.builds(
    crom::l1::Group,
)
Type_strategy = st.builds(
    Type,
)
crom::l1::AntiRigidType_strategy = st.builds(
    crom::l1::AntiRigidType,
)
crom::l1::RigidType_strategy = st.builds(
    crom::l1::RigidType,
)
crom::l1::Relation_strategy = st.builds(
    crom::l1::Relation,
)
crom::l1::Model_strategy = st.builds(
    crom::l1::Model,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
crom::l1::RelationTarget_strategy = st.builds(
    crom::l1::RelationTarget,
)
crom::l1::TypedElement_strategy = st.builds(
    crom::l1::TypedElement,
)
crom::l1::ModelElement_strategy = st.builds(
    crom::l1::ModelElement,
)
crom::l1::NamedElement_strategy = st.builds(
    crom::l1::NamedElement,
    name=
        safe_text
)
RelationTarget_strategy = st.builds(
    RelationTarget,
)
crom::l1::Type_strategy = st.builds(
    crom::l1::Type,
)
crom::l1::RoleGroup_strategy = st.builds(
    crom::l1::RoleGroup,
    lower=
        st.integers(),
    upper=
        st.integers()
)
crom::l1::RoleType_strategy = st.builds(
    crom::l1::RoleType,
)
crom::l1::Attribute_strategy = st.builds(
    crom::l1::Attribute,
)

@given(instance=RoleConstraint_strategy)
@settings(max_examples=50)
def test_roleconstraint_instantiation(instance):
    assert isinstance(instance, RoleConstraint)

@given(instance=crom::l1::RoleEquivalence_strategy)
@settings(max_examples=50)
def test_crom::l1::roleequivalence_instantiation(instance):
    assert isinstance(instance, crom::l1::RoleEquivalence)

@given(instance=crom::l1::RoleImplication_strategy)
@settings(max_examples=50)
def test_crom::l1::roleimplication_instantiation(instance):
    assert isinstance(instance, crom::l1::RoleImplication)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=crom::l1::Test_strategy)
@settings(max_examples=50)
def test_crom::l1::test_instantiation(instance):
    assert isinstance(instance, crom::l1::Test)

@given(instance=crom::l1::RoleConstraint_strategy)
@settings(max_examples=50)
def test_crom::l1::roleconstraint_instantiation(instance):
    assert isinstance(instance, crom::l1::RoleConstraint)

@given(instance=crom::l1::Part_strategy)
@settings(max_examples=50)
def test_crom::l1::part_instantiation(instance):
    assert isinstance(instance, crom::l1::Part)

@given(instance=crom::l1::Part_strategy)
def test_crom::l1::part_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=crom::l1::Part_strategy)
def test_crom::l1::part_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=crom::l1::Part_strategy)
def test_crom::l1::part_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=crom::l1::Part_strategy)
def test_crom::l1::part_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=crom::l1::RoleProhibition_strategy)
@settings(max_examples=50)
def test_crom::l1::roleprohibition_instantiation(instance):
    assert isinstance(instance, crom::l1::RoleProhibition)

@given(instance=crom::l1::Constraint_strategy)
@settings(max_examples=50)
def test_crom::l1::constraint_instantiation(instance):
    assert isinstance(instance, crom::l1::Constraint)

@given(instance=RoleGroupElement_strategy)
@settings(max_examples=50)
def test_rolegroupelement_instantiation(instance):
    assert isinstance(instance, RoleGroupElement)

@given(instance=Inheritance_strategy)
@settings(max_examples=50)
def test_inheritance_instantiation(instance):
    assert isinstance(instance, Inheritance)

@given(instance=crom::l1::CompartmentInheritance_strategy)
@settings(max_examples=50)
def test_crom::l1::compartmentinheritance_instantiation(instance):
    assert isinstance(instance, crom::l1::CompartmentInheritance)

@given(instance=crom::l1::DataInheritance_strategy)
@settings(max_examples=50)
def test_crom::l1::datainheritance_instantiation(instance):
    assert isinstance(instance, crom::l1::DataInheritance)

@given(instance=crom::l1::NaturalInheritance_strategy)
@settings(max_examples=50)
def test_crom::l1::naturalinheritance_instantiation(instance):
    assert isinstance(instance, crom::l1::NaturalInheritance)

@given(instance=crom::l1::Player_strategy)
@settings(max_examples=50)
def test_crom::l1::player_instantiation(instance):
    assert isinstance(instance, crom::l1::Player)

@given(instance=crom::l1::AbstractRole_strategy)
@settings(max_examples=50)
def test_crom::l1::abstractrole_instantiation(instance):
    assert isinstance(instance, crom::l1::AbstractRole)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=crom::l1::Inheritance_strategy)
@settings(max_examples=50)
def test_crom::l1::inheritance_instantiation(instance):
    assert isinstance(instance, crom::l1::Inheritance)

@given(instance=crom::l1::Fulfillment_strategy)
@settings(max_examples=50)
def test_crom::l1::fulfillment_instantiation(instance):
    assert isinstance(instance, crom::l1::Fulfillment)

@given(instance=AntiRigidType_strategy)
@settings(max_examples=50)
def test_antirigidtype_instantiation(instance):
    assert isinstance(instance, AntiRigidType)

@given(instance=AbstractRole_strategy)
@settings(max_examples=50)
def test_abstractrole_instantiation(instance):
    assert isinstance(instance, AbstractRole)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)

@given(instance=RigidType_strategy)
@settings(max_examples=50)
def test_rigidtype_instantiation(instance):
    assert isinstance(instance, RigidType)

@given(instance=crom::l1::CompartmentType_strategy)
@settings(max_examples=50)
def test_crom::l1::compartmenttype_instantiation(instance):
    assert isinstance(instance, crom::l1::CompartmentType)

@given(instance=crom::l1::DataType_strategy)
@settings(max_examples=50)
def test_crom::l1::datatype_instantiation(instance):
    assert isinstance(instance, crom::l1::DataType)

@given(instance=crom::l1::NaturalType_strategy)
@settings(max_examples=50)
def test_crom::l1::naturaltype_instantiation(instance):
    assert isinstance(instance, crom::l1::NaturalType)

@given(instance=crom::l1::AbstractRoleRef_strategy)
@settings(max_examples=50)
def test_crom::l1::abstractroleref_instantiation(instance):
    assert isinstance(instance, crom::l1::AbstractRoleRef)

@given(instance=crom::l1::RoleGroupElement_strategy)
@settings(max_examples=50)
def test_crom::l1::rolegroupelement_instantiation(instance):
    assert isinstance(instance, crom::l1::RoleGroupElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=crom::l1::Operation_strategy)
@settings(max_examples=50)
def test_crom::l1::operation_instantiation(instance):
    assert isinstance(instance, crom::l1::Operation)

@given(instance=crom::l1::Operation_strategy)
def test_crom::l1::operation_operation_type(instance):
    assert isinstance(instance.operation, str)


@given(instance=crom::l1::Operation_strategy)
def test_crom::l1::operation_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=crom::l1::Parameter_strategy)
@settings(max_examples=50)
def test_crom::l1::parameter_instantiation(instance):
    assert isinstance(instance, crom::l1::Parameter)

@given(instance=Model_strategy)
@settings(max_examples=50)
def test_model_instantiation(instance):
    assert isinstance(instance, Model)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=crom::l1::Group_strategy)
@settings(max_examples=50)
def test_crom::l1::group_instantiation(instance):
    assert isinstance(instance, crom::l1::Group)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=crom::l1::AntiRigidType_strategy)
@settings(max_examples=50)
def test_crom::l1::antirigidtype_instantiation(instance):
    assert isinstance(instance, crom::l1::AntiRigidType)

@given(instance=crom::l1::RigidType_strategy)
@settings(max_examples=50)
def test_crom::l1::rigidtype_instantiation(instance):
    assert isinstance(instance, crom::l1::RigidType)

@given(instance=crom::l1::Relation_strategy)
@settings(max_examples=50)
def test_crom::l1::relation_instantiation(instance):
    assert isinstance(instance, crom::l1::Relation)

@given(instance=crom::l1::Model_strategy)
@settings(max_examples=50)
def test_crom::l1::model_instantiation(instance):
    assert isinstance(instance, crom::l1::Model)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=crom::l1::RelationTarget_strategy)
@settings(max_examples=50)
def test_crom::l1::relationtarget_instantiation(instance):
    assert isinstance(instance, crom::l1::RelationTarget)

@given(instance=crom::l1::TypedElement_strategy)
@settings(max_examples=50)
def test_crom::l1::typedelement_instantiation(instance):
    assert isinstance(instance, crom::l1::TypedElement)

@given(instance=crom::l1::ModelElement_strategy)
@settings(max_examples=50)
def test_crom::l1::modelelement_instantiation(instance):
    assert isinstance(instance, crom::l1::ModelElement)

@given(instance=crom::l1::NamedElement_strategy)
@settings(max_examples=50)
def test_crom::l1::namedelement_instantiation(instance):
    assert isinstance(instance, crom::l1::NamedElement)

@given(instance=crom::l1::NamedElement_strategy)
def test_crom::l1::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=crom::l1::NamedElement_strategy)
def test_crom::l1::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RelationTarget_strategy)
@settings(max_examples=50)
def test_relationtarget_instantiation(instance):
    assert isinstance(instance, RelationTarget)

@given(instance=crom::l1::Type_strategy)
@settings(max_examples=50)
def test_crom::l1::type_instantiation(instance):
    assert isinstance(instance, crom::l1::Type)

@given(instance=crom::l1::RoleGroup_strategy)
@settings(max_examples=50)
def test_crom::l1::rolegroup_instantiation(instance):
    assert isinstance(instance, crom::l1::RoleGroup)

@given(instance=crom::l1::RoleGroup_strategy)
def test_crom::l1::rolegroup_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=crom::l1::RoleGroup_strategy)
def test_crom::l1::rolegroup_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=crom::l1::RoleGroup_strategy)
def test_crom::l1::rolegroup_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=crom::l1::RoleGroup_strategy)
def test_crom::l1::rolegroup_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=crom::l1::RoleType_strategy)
@settings(max_examples=50)
def test_crom::l1::roletype_instantiation(instance):
    assert isinstance(instance, crom::l1::RoleType)

@given(instance=crom::l1::Attribute_strategy)
@settings(max_examples=50)
def test_crom::l1::attribute_instantiation(instance):
    assert isinstance(instance, crom::l1::Attribute)
