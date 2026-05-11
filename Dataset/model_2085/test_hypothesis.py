import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sxfm::Data,
    sxfm::Literal,
    Literal,
    sxfm::Atom,
    sxfm::Not,
    sxfm::ConstraintableElement,
    sxfm::ContainableElement,
    sxfm::ContainerElement,
    sxfm::CommonFeature,
    sxfm::VariableFeature,
    sxfm::FeatureChoice,
    VariableFeature,
    CommonFeature,
    ConstraintableElement,
    Feature,
    ContainableElement,
    ContainerElement,
    sxfm::Optional,
    sxfm::Mandatory,
    sxfm::Or,
    sxfm::Constraint,
    sxfm::GroupedFeature,
    CardinalizedElement,
    sxfm::CardinalizedElement,
    sxfm::Root,
    sxfm::FeatureModelConfiguaration,
    sxfm::MetadataSet,
    sxfm::FeatureTree,
    sxfm::ConstraintsSet,
    sxfm::FeatureModel,
    sxfm::Group,
    sxfm::Feature,
    DecisionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sxfm::data_is_not_abstract():
    assert not inspect.isabstract(sxfm::Data)


def test_sxfm::data_constructor_exists():
    assert callable(sxfm::Data.__init__)


def test_sxfm::data_constructor_args():
    sig = inspect.signature(sxfm::Data.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_sxfm::data_has_value():
    assert hasattr(sxfm::Data, "value")
    descriptor = None
    for klass in sxfm::Data.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sxfm::data_has_name():
    assert hasattr(sxfm::Data, "name")
    descriptor = None
    for klass in sxfm::Data.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sxfm::literal_is_not_abstract():
    assert not inspect.isabstract(sxfm::Literal)


def test_sxfm::literal_constructor_exists():
    assert callable(sxfm::Literal.__init__)


def test_sxfm::literal_constructor_args():
    sig = inspect.signature(sxfm::Literal.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::atom_is_not_abstract():
    assert not inspect.isabstract(sxfm::Atom)


def test_sxfm::atom_constructor_exists():
    assert callable(sxfm::Atom.__init__)


def test_sxfm::atom_constructor_args():
    sig = inspect.signature(sxfm::Atom.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::not_is_not_abstract():
    assert not inspect.isabstract(sxfm::Not)


def test_sxfm::not_constructor_exists():
    assert callable(sxfm::Not.__init__)


def test_sxfm::not_constructor_args():
    sig = inspect.signature(sxfm::Not.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::constraintableelement_is_not_abstract():
    assert not inspect.isabstract(sxfm::ConstraintableElement)


def test_sxfm::constraintableelement_constructor_exists():
    assert callable(sxfm::ConstraintableElement.__init__)


def test_sxfm::constraintableelement_constructor_args():
    sig = inspect.signature(sxfm::ConstraintableElement.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::containableelement_is_not_abstract():
    assert not inspect.isabstract(sxfm::ContainableElement)


def test_sxfm::containableelement_constructor_exists():
    assert callable(sxfm::ContainableElement.__init__)


def test_sxfm::containableelement_constructor_args():
    sig = inspect.signature(sxfm::ContainableElement.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::containerelement_is_not_abstract():
    assert not inspect.isabstract(sxfm::ContainerElement)


def test_sxfm::containerelement_constructor_exists():
    assert callable(sxfm::ContainerElement.__init__)


def test_sxfm::containerelement_constructor_args():
    sig = inspect.signature(sxfm::ContainerElement.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::commonfeature_is_not_abstract():
    assert not inspect.isabstract(sxfm::CommonFeature)


def test_sxfm::commonfeature_constructor_exists():
    assert callable(sxfm::CommonFeature.__init__)


def test_sxfm::commonfeature_constructor_args():
    sig = inspect.signature(sxfm::CommonFeature.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::variablefeature_is_not_abstract():
    assert not inspect.isabstract(sxfm::VariableFeature)


def test_sxfm::variablefeature_constructor_exists():
    assert callable(sxfm::VariableFeature.__init__)


def test_sxfm::variablefeature_constructor_args():
    sig = inspect.signature(sxfm::VariableFeature.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::featurechoice_is_not_abstract():
    assert not inspect.isabstract(sxfm::FeatureChoice)


def test_sxfm::featurechoice_constructor_exists():
    assert callable(sxfm::FeatureChoice.__init__)


def test_sxfm::featurechoice_constructor_args():
    sig = inspect.signature(sxfm::FeatureChoice.__init__)
    params = list(sig.parameters.keys())
    assert "decisionType" in params, "Missing parameter 'decisionType'"
    assert "selected" in params, "Missing parameter 'selected'"
    assert "decisionStep" in params, "Missing parameter 'decisionStep'"

def test_sxfm::featurechoice_has_decisionType():
    assert hasattr(sxfm::FeatureChoice, "decisionType")
    descriptor = None
    for klass in sxfm::FeatureChoice.__mro__:
        if "decisionType" in klass.__dict__:
            descriptor = klass.__dict__["decisionType"]
            break
    assert isinstance(descriptor, property)

def test_sxfm::featurechoice_has_selected():
    assert hasattr(sxfm::FeatureChoice, "selected")
    descriptor = None
    for klass in sxfm::FeatureChoice.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_sxfm::featurechoice_has_decisionStep():
    assert hasattr(sxfm::FeatureChoice, "decisionStep")
    descriptor = None
    for klass in sxfm::FeatureChoice.__mro__:
        if "decisionStep" in klass.__dict__:
            descriptor = klass.__dict__["decisionStep"]
            break
    assert isinstance(descriptor, property)



def test_variablefeature_is_not_abstract():
    assert not inspect.isabstract(VariableFeature)


def test_variablefeature_constructor_exists():
    assert callable(VariableFeature.__init__)


def test_variablefeature_constructor_args():
    sig = inspect.signature(VariableFeature.__init__)
    params = list(sig.parameters.keys())



def test_commonfeature_is_not_abstract():
    assert not inspect.isabstract(CommonFeature)


def test_commonfeature_constructor_exists():
    assert callable(CommonFeature.__init__)


def test_commonfeature_constructor_args():
    sig = inspect.signature(CommonFeature.__init__)
    params = list(sig.parameters.keys())



def test_constraintableelement_is_not_abstract():
    assert not inspect.isabstract(ConstraintableElement)


def test_constraintableelement_constructor_exists():
    assert callable(ConstraintableElement.__init__)


def test_constraintableelement_constructor_args():
    sig = inspect.signature(ConstraintableElement.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_containableelement_is_not_abstract():
    assert not inspect.isabstract(ContainableElement)


def test_containableelement_constructor_exists():
    assert callable(ContainableElement.__init__)


def test_containableelement_constructor_args():
    sig = inspect.signature(ContainableElement.__init__)
    params = list(sig.parameters.keys())



def test_containerelement_is_not_abstract():
    assert not inspect.isabstract(ContainerElement)


def test_containerelement_constructor_exists():
    assert callable(ContainerElement.__init__)


def test_containerelement_constructor_args():
    sig = inspect.signature(ContainerElement.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::optional_is_not_abstract():
    assert not inspect.isabstract(sxfm::Optional)


def test_sxfm::optional_constructor_exists():
    assert callable(sxfm::Optional.__init__)


def test_sxfm::optional_constructor_args():
    sig = inspect.signature(sxfm::Optional.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::mandatory_is_not_abstract():
    assert not inspect.isabstract(sxfm::Mandatory)


def test_sxfm::mandatory_constructor_exists():
    assert callable(sxfm::Mandatory.__init__)


def test_sxfm::mandatory_constructor_args():
    sig = inspect.signature(sxfm::Mandatory.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::or_is_not_abstract():
    assert not inspect.isabstract(sxfm::Or)


def test_sxfm::or_constructor_exists():
    assert callable(sxfm::Or.__init__)


def test_sxfm::or_constructor_args():
    sig = inspect.signature(sxfm::Or.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::constraint_is_not_abstract():
    assert not inspect.isabstract(sxfm::Constraint)


def test_sxfm::constraint_constructor_exists():
    assert callable(sxfm::Constraint.__init__)


def test_sxfm::constraint_constructor_args():
    sig = inspect.signature(sxfm::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_sxfm::constraint_has_id():
    assert hasattr(sxfm::Constraint, "id")
    descriptor = None
    for klass in sxfm::Constraint.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_sxfm::groupedfeature_is_not_abstract():
    assert not inspect.isabstract(sxfm::GroupedFeature)


def test_sxfm::groupedfeature_constructor_exists():
    assert callable(sxfm::GroupedFeature.__init__)


def test_sxfm::groupedfeature_constructor_args():
    sig = inspect.signature(sxfm::GroupedFeature.__init__)
    params = list(sig.parameters.keys())



def test_cardinalizedelement_is_not_abstract():
    assert not inspect.isabstract(CardinalizedElement)


def test_cardinalizedelement_constructor_exists():
    assert callable(CardinalizedElement.__init__)


def test_cardinalizedelement_constructor_args():
    sig = inspect.signature(CardinalizedElement.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::cardinalizedelement_is_not_abstract():
    assert not inspect.isabstract(sxfm::CardinalizedElement)


def test_sxfm::cardinalizedelement_constructor_exists():
    assert callable(sxfm::CardinalizedElement.__init__)


def test_sxfm::cardinalizedelement_constructor_args():
    sig = inspect.signature(sxfm::CardinalizedElement.__init__)
    params = list(sig.parameters.keys())
    assert "minCardinality" in params, "Missing parameter 'minCardinality'"
    assert "maxCardinality" in params, "Missing parameter 'maxCardinality'"

def test_sxfm::cardinalizedelement_has_minCardinality():
    assert hasattr(sxfm::CardinalizedElement, "minCardinality")
    descriptor = None
    for klass in sxfm::CardinalizedElement.__mro__:
        if "minCardinality" in klass.__dict__:
            descriptor = klass.__dict__["minCardinality"]
            break
    assert isinstance(descriptor, property)

def test_sxfm::cardinalizedelement_has_maxCardinality():
    assert hasattr(sxfm::CardinalizedElement, "maxCardinality")
    descriptor = None
    for klass in sxfm::CardinalizedElement.__mro__:
        if "maxCardinality" in klass.__dict__:
            descriptor = klass.__dict__["maxCardinality"]
            break
    assert isinstance(descriptor, property)



def test_sxfm::root_is_not_abstract():
    assert not inspect.isabstract(sxfm::Root)


def test_sxfm::root_constructor_exists():
    assert callable(sxfm::Root.__init__)


def test_sxfm::root_constructor_args():
    sig = inspect.signature(sxfm::Root.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::featuremodelconfiguaration_is_not_abstract():
    assert not inspect.isabstract(sxfm::FeatureModelConfiguaration)


def test_sxfm::featuremodelconfiguaration_constructor_exists():
    assert callable(sxfm::FeatureModelConfiguaration.__init__)


def test_sxfm::featuremodelconfiguaration_constructor_args():
    sig = inspect.signature(sxfm::FeatureModelConfiguaration.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::metadataset_is_not_abstract():
    assert not inspect.isabstract(sxfm::MetadataSet)


def test_sxfm::metadataset_constructor_exists():
    assert callable(sxfm::MetadataSet.__init__)


def test_sxfm::metadataset_constructor_args():
    sig = inspect.signature(sxfm::MetadataSet.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::featuretree_is_not_abstract():
    assert not inspect.isabstract(sxfm::FeatureTree)


def test_sxfm::featuretree_constructor_exists():
    assert callable(sxfm::FeatureTree.__init__)


def test_sxfm::featuretree_constructor_args():
    sig = inspect.signature(sxfm::FeatureTree.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::constraintsset_is_not_abstract():
    assert not inspect.isabstract(sxfm::ConstraintsSet)


def test_sxfm::constraintsset_constructor_exists():
    assert callable(sxfm::ConstraintsSet.__init__)


def test_sxfm::constraintsset_constructor_args():
    sig = inspect.signature(sxfm::ConstraintsSet.__init__)
    params = list(sig.parameters.keys())



def test_sxfm::featuremodel_is_not_abstract():
    assert not inspect.isabstract(sxfm::FeatureModel)


def test_sxfm::featuremodel_constructor_exists():
    assert callable(sxfm::FeatureModel.__init__)


def test_sxfm::featuremodel_constructor_args():
    sig = inspect.signature(sxfm::FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sxfm::featuremodel_has_name():
    assert hasattr(sxfm::FeatureModel, "name")
    descriptor = None
    for klass in sxfm::FeatureModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sxfm::group_is_not_abstract():
    assert not inspect.isabstract(sxfm::Group)


def test_sxfm::group_constructor_exists():
    assert callable(sxfm::Group.__init__)


def test_sxfm::group_constructor_args():
    sig = inspect.signature(sxfm::Group.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_sxfm::group_has_id():
    assert hasattr(sxfm::Group, "id")
    descriptor = None
    for klass in sxfm::Group.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_sxfm::feature_is_not_abstract():
    assert not inspect.isabstract(sxfm::Feature)


def test_sxfm::feature_constructor_exists():
    assert callable(sxfm::Feature.__init__)


def test_sxfm::feature_constructor_args():
    sig = inspect.signature(sxfm::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "treeLevel" in params, "Missing parameter 'treeLevel'"

def test_sxfm::feature_has_name():
    assert hasattr(sxfm::Feature, "name")
    descriptor = None
    for klass in sxfm::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sxfm::feature_has_description():
    assert hasattr(sxfm::Feature, "description")
    descriptor = None
    for klass in sxfm::Feature.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_sxfm::feature_has_id():
    assert hasattr(sxfm::Feature, "id")
    descriptor = None
    for klass in sxfm::Feature.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sxfm::feature_has_treeLevel():
    assert hasattr(sxfm::Feature, "treeLevel")
    descriptor = None
    for klass in sxfm::Feature.__mro__:
        if "treeLevel" in klass.__dict__:
            descriptor = klass.__dict__["treeLevel"]
            break
    assert isinstance(descriptor, property)

def test_decisiontype_exists():
    # Check that the Enumeration exists
    assert DecisionType is not None

def test_decisiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DecisionType]
    expected_literals = [
        "manual",
        "autocompleted",
        "propagated",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DecisionType"


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
sxfm::Data_strategy = st.builds(
    sxfm::Data,
    value=
        safe_text,
    name=
        safe_text
)
sxfm::Literal_strategy = st.builds(
    sxfm::Literal,
)
Literal_strategy = st.builds(
    Literal,
)
sxfm::Atom_strategy = st.builds(
    sxfm::Atom,
)
sxfm::Not_strategy = st.builds(
    sxfm::Not,
)
sxfm::ConstraintableElement_strategy = st.builds(
    sxfm::ConstraintableElement,
)
sxfm::ContainableElement_strategy = st.builds(
    sxfm::ContainableElement,
)
sxfm::ContainerElement_strategy = st.builds(
    sxfm::ContainerElement,
)
sxfm::CommonFeature_strategy = st.builds(
    sxfm::CommonFeature,
)
sxfm::VariableFeature_strategy = st.builds(
    sxfm::VariableFeature,
)
sxfm::FeatureChoice_strategy = st.builds(
    sxfm::FeatureChoice,
    decisionType=
        safe_text,
    selected=
        st.booleans(),
    decisionStep=
        st.integers()
)
VariableFeature_strategy = st.builds(
    VariableFeature,
)
CommonFeature_strategy = st.builds(
    CommonFeature,
)
ConstraintableElement_strategy = st.builds(
    ConstraintableElement,
)
Feature_strategy = st.builds(
    Feature,
)
ContainableElement_strategy = st.builds(
    ContainableElement,
)
ContainerElement_strategy = st.builds(
    ContainerElement,
)
sxfm::Optional_strategy = st.builds(
    sxfm::Optional,
)
sxfm::Mandatory_strategy = st.builds(
    sxfm::Mandatory,
)
sxfm::Or_strategy = st.builds(
    sxfm::Or,
)
sxfm::Constraint_strategy = st.builds(
    sxfm::Constraint,
    id=
        st.integers()
)
sxfm::GroupedFeature_strategy = st.builds(
    sxfm::GroupedFeature,
)
CardinalizedElement_strategy = st.builds(
    CardinalizedElement,
)
sxfm::CardinalizedElement_strategy = st.builds(
    sxfm::CardinalizedElement,
    minCardinality=
        st.integers(),
    maxCardinality=
        st.integers()
)
sxfm::Root_strategy = st.builds(
    sxfm::Root,
)
sxfm::FeatureModelConfiguaration_strategy = st.builds(
    sxfm::FeatureModelConfiguaration,
)
sxfm::MetadataSet_strategy = st.builds(
    sxfm::MetadataSet,
)
sxfm::FeatureTree_strategy = st.builds(
    sxfm::FeatureTree,
)
sxfm::ConstraintsSet_strategy = st.builds(
    sxfm::ConstraintsSet,
)
sxfm::FeatureModel_strategy = st.builds(
    sxfm::FeatureModel,
    name=
        safe_text
)
sxfm::Group_strategy = st.builds(
    sxfm::Group,
    id=
        safe_text
)
sxfm::Feature_strategy = st.builds(
    sxfm::Feature,
    name=
        safe_text,
    description=
        safe_text,
    id=
        safe_text,
    treeLevel=
        st.integers()
)

@given(instance=sxfm::Data_strategy)
@settings(max_examples=50)
def test_sxfm::data_instantiation(instance):
    assert isinstance(instance, sxfm::Data)

@given(instance=sxfm::Data_strategy)
def test_sxfm::data_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sxfm::Data_strategy)
def test_sxfm::data_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sxfm::Data_strategy)
def test_sxfm::data_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sxfm::Data_strategy)
def test_sxfm::data_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sxfm::Literal_strategy)
@settings(max_examples=50)
def test_sxfm::literal_instantiation(instance):
    assert isinstance(instance, sxfm::Literal)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=sxfm::Atom_strategy)
@settings(max_examples=50)
def test_sxfm::atom_instantiation(instance):
    assert isinstance(instance, sxfm::Atom)

@given(instance=sxfm::Not_strategy)
@settings(max_examples=50)
def test_sxfm::not_instantiation(instance):
    assert isinstance(instance, sxfm::Not)

@given(instance=sxfm::ConstraintableElement_strategy)
@settings(max_examples=50)
def test_sxfm::constraintableelement_instantiation(instance):
    assert isinstance(instance, sxfm::ConstraintableElement)

@given(instance=sxfm::ContainableElement_strategy)
@settings(max_examples=50)
def test_sxfm::containableelement_instantiation(instance):
    assert isinstance(instance, sxfm::ContainableElement)

@given(instance=sxfm::ContainerElement_strategy)
@settings(max_examples=50)
def test_sxfm::containerelement_instantiation(instance):
    assert isinstance(instance, sxfm::ContainerElement)

@given(instance=sxfm::CommonFeature_strategy)
@settings(max_examples=50)
def test_sxfm::commonfeature_instantiation(instance):
    assert isinstance(instance, sxfm::CommonFeature)

@given(instance=sxfm::VariableFeature_strategy)
@settings(max_examples=50)
def test_sxfm::variablefeature_instantiation(instance):
    assert isinstance(instance, sxfm::VariableFeature)

@given(instance=sxfm::FeatureChoice_strategy)
@settings(max_examples=50)
def test_sxfm::featurechoice_instantiation(instance):
    assert isinstance(instance, sxfm::FeatureChoice)

@given(instance=sxfm::FeatureChoice_strategy)
def test_sxfm::featurechoice_decisionType_type(instance):
    assert isinstance(instance.decisionType, str)


@given(instance=sxfm::FeatureChoice_strategy)
def test_sxfm::featurechoice_decisionType_setter(instance):
    original = instance.decisionType
    instance.decisionType = original
    assert instance.decisionType == original

@given(instance=sxfm::FeatureChoice_strategy)
def test_sxfm::featurechoice_selected_type(instance):
    assert isinstance(instance.selected, bool)


@given(instance=sxfm::FeatureChoice_strategy)
def test_sxfm::featurechoice_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=sxfm::FeatureChoice_strategy)
def test_sxfm::featurechoice_decisionStep_type(instance):
    assert isinstance(instance.decisionStep, int)


@given(instance=sxfm::FeatureChoice_strategy)
def test_sxfm::featurechoice_decisionStep_setter(instance):
    original = instance.decisionStep
    instance.decisionStep = original
    assert instance.decisionStep == original

@given(instance=VariableFeature_strategy)
@settings(max_examples=50)
def test_variablefeature_instantiation(instance):
    assert isinstance(instance, VariableFeature)

@given(instance=CommonFeature_strategy)
@settings(max_examples=50)
def test_commonfeature_instantiation(instance):
    assert isinstance(instance, CommonFeature)

@given(instance=ConstraintableElement_strategy)
@settings(max_examples=50)
def test_constraintableelement_instantiation(instance):
    assert isinstance(instance, ConstraintableElement)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=ContainableElement_strategy)
@settings(max_examples=50)
def test_containableelement_instantiation(instance):
    assert isinstance(instance, ContainableElement)

@given(instance=ContainerElement_strategy)
@settings(max_examples=50)
def test_containerelement_instantiation(instance):
    assert isinstance(instance, ContainerElement)

@given(instance=sxfm::Optional_strategy)
@settings(max_examples=50)
def test_sxfm::optional_instantiation(instance):
    assert isinstance(instance, sxfm::Optional)

@given(instance=sxfm::Mandatory_strategy)
@settings(max_examples=50)
def test_sxfm::mandatory_instantiation(instance):
    assert isinstance(instance, sxfm::Mandatory)

@given(instance=sxfm::Or_strategy)
@settings(max_examples=50)
def test_sxfm::or_instantiation(instance):
    assert isinstance(instance, sxfm::Or)

@given(instance=sxfm::Constraint_strategy)
@settings(max_examples=50)
def test_sxfm::constraint_instantiation(instance):
    assert isinstance(instance, sxfm::Constraint)

@given(instance=sxfm::Constraint_strategy)
def test_sxfm::constraint_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=sxfm::Constraint_strategy)
def test_sxfm::constraint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sxfm::GroupedFeature_strategy)
@settings(max_examples=50)
def test_sxfm::groupedfeature_instantiation(instance):
    assert isinstance(instance, sxfm::GroupedFeature)

@given(instance=CardinalizedElement_strategy)
@settings(max_examples=50)
def test_cardinalizedelement_instantiation(instance):
    assert isinstance(instance, CardinalizedElement)

@given(instance=sxfm::CardinalizedElement_strategy)
@settings(max_examples=50)
def test_sxfm::cardinalizedelement_instantiation(instance):
    assert isinstance(instance, sxfm::CardinalizedElement)

@given(instance=sxfm::CardinalizedElement_strategy)
def test_sxfm::cardinalizedelement_minCardinality_type(instance):
    assert isinstance(instance.minCardinality, int)


@given(instance=sxfm::CardinalizedElement_strategy)
def test_sxfm::cardinalizedelement_minCardinality_setter(instance):
    original = instance.minCardinality
    instance.minCardinality = original
    assert instance.minCardinality == original

@given(instance=sxfm::CardinalizedElement_strategy)
def test_sxfm::cardinalizedelement_maxCardinality_type(instance):
    assert isinstance(instance.maxCardinality, int)


@given(instance=sxfm::CardinalizedElement_strategy)
def test_sxfm::cardinalizedelement_maxCardinality_setter(instance):
    original = instance.maxCardinality
    instance.maxCardinality = original
    assert instance.maxCardinality == original

@given(instance=sxfm::Root_strategy)
@settings(max_examples=50)
def test_sxfm::root_instantiation(instance):
    assert isinstance(instance, sxfm::Root)

@given(instance=sxfm::FeatureModelConfiguaration_strategy)
@settings(max_examples=50)
def test_sxfm::featuremodelconfiguaration_instantiation(instance):
    assert isinstance(instance, sxfm::FeatureModelConfiguaration)

@given(instance=sxfm::MetadataSet_strategy)
@settings(max_examples=50)
def test_sxfm::metadataset_instantiation(instance):
    assert isinstance(instance, sxfm::MetadataSet)

@given(instance=sxfm::FeatureTree_strategy)
@settings(max_examples=50)
def test_sxfm::featuretree_instantiation(instance):
    assert isinstance(instance, sxfm::FeatureTree)

@given(instance=sxfm::ConstraintsSet_strategy)
@settings(max_examples=50)
def test_sxfm::constraintsset_instantiation(instance):
    assert isinstance(instance, sxfm::ConstraintsSet)

@given(instance=sxfm::FeatureModel_strategy)
@settings(max_examples=50)
def test_sxfm::featuremodel_instantiation(instance):
    assert isinstance(instance, sxfm::FeatureModel)

@given(instance=sxfm::FeatureModel_strategy)
def test_sxfm::featuremodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sxfm::FeatureModel_strategy)
def test_sxfm::featuremodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sxfm::Group_strategy)
@settings(max_examples=50)
def test_sxfm::group_instantiation(instance):
    assert isinstance(instance, sxfm::Group)

@given(instance=sxfm::Group_strategy)
def test_sxfm::group_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=sxfm::Group_strategy)
def test_sxfm::group_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sxfm::Feature_strategy)
@settings(max_examples=50)
def test_sxfm::feature_instantiation(instance):
    assert isinstance(instance, sxfm::Feature)

@given(instance=sxfm::Feature_strategy)
def test_sxfm::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sxfm::Feature_strategy)
def test_sxfm::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sxfm::Feature_strategy)
def test_sxfm::feature_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=sxfm::Feature_strategy)
def test_sxfm::feature_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=sxfm::Feature_strategy)
def test_sxfm::feature_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=sxfm::Feature_strategy)
def test_sxfm::feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sxfm::Feature_strategy)
def test_sxfm::feature_treeLevel_type(instance):
    assert isinstance(instance.treeLevel, int)


@given(instance=sxfm::Feature_strategy)
def test_sxfm::feature_treeLevel_setter(instance):
    original = instance.treeLevel
    instance.treeLevel = original
    assert instance.treeLevel == original
