import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    featureModelMetamodel::ConfigurationModel,
    Selection,
    featureModelMetamodel::ClonableSelection,
    featureModelMetamodel::Selection,
    Multiplicity_,
    Feature,
    featureModelMetamodel::ClonableFeature,
    featureModelMetamodel::VariableFeature,
    featureModelMetamodel::Attribute,
    featureModelMetamodel::GroupMultiplicity,
    featureModelMetamodel::Feature,
    featureModelMetamodel::FeatureModel,
    featureModelMetamodel::Constraint,
    featureModelMetamodel::AbstractFeature,
    featureModelMetamodel::Multiplicity_,
    SelectionState,
    VariabilityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_featuremodelmetamodel::configurationmodel_is_not_abstract():
    assert not inspect.isabstract(featureModelMetamodel::ConfigurationModel)


def test_featuremodelmetamodel::configurationmodel_constructor_exists():
    assert callable(featureModelMetamodel::ConfigurationModel.__init__)


def test_featuremodelmetamodel::configurationmodel_constructor_args():
    sig = inspect.signature(featureModelMetamodel::ConfigurationModel.__init__)
    params = list(sig.parameters.keys())



def test_selection_is_not_abstract():
    assert not inspect.isabstract(Selection)


def test_selection_constructor_exists():
    assert callable(Selection.__init__)


def test_selection_constructor_args():
    sig = inspect.signature(Selection.__init__)
    params = list(sig.parameters.keys())



def test_featuremodelmetamodel::clonableselection_is_not_abstract():
    assert not inspect.isabstract(featureModelMetamodel::ClonableSelection)


def test_featuremodelmetamodel::clonableselection_constructor_exists():
    assert callable(featureModelMetamodel::ClonableSelection.__init__)


def test_featuremodelmetamodel::clonableselection_constructor_args():
    sig = inspect.signature(featureModelMetamodel::ClonableSelection.__init__)
    params = list(sig.parameters.keys())
    assert "instance" in params, "Missing parameter 'instance'"

def test_featuremodelmetamodel::clonableselection_has_instance():
    assert hasattr(featureModelMetamodel::ClonableSelection, "instance")
    descriptor = None
    for klass in featureModelMetamodel::ClonableSelection.__mro__:
        if "instance" in klass.__dict__:
            descriptor = klass.__dict__["instance"]
            break
    assert isinstance(descriptor, property)



def test_featuremodelmetamodel::selection_is_not_abstract():
    assert not inspect.isabstract(featureModelMetamodel::Selection)


def test_featuremodelmetamodel::selection_constructor_exists():
    assert callable(featureModelMetamodel::Selection.__init__)


def test_featuremodelmetamodel::selection_constructor_args():
    sig = inspect.signature(featureModelMetamodel::Selection.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"
    assert "name" in params, "Missing parameter 'name'"

def test_featuremodelmetamodel::selection_has_state():
    assert hasattr(featureModelMetamodel::Selection, "state")
    descriptor = None
    for klass in featureModelMetamodel::Selection.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_featuremodelmetamodel::selection_has_name():
    assert hasattr(featureModelMetamodel::Selection, "name")
    descriptor = None
    for klass in featureModelMetamodel::Selection.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_multiplicity__is_not_abstract():
    assert not inspect.isabstract(Multiplicity_)


def test_multiplicity__constructor_exists():
    assert callable(Multiplicity_.__init__)


def test_multiplicity__constructor_args():
    sig = inspect.signature(Multiplicity_.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_featuremodelmetamodel::clonablefeature_is_not_abstract():
    assert not inspect.isabstract(featureModelMetamodel::ClonableFeature)


def test_featuremodelmetamodel::clonablefeature_constructor_exists():
    assert callable(featureModelMetamodel::ClonableFeature.__init__)


def test_featuremodelmetamodel::clonablefeature_constructor_args():
    sig = inspect.signature(featureModelMetamodel::ClonableFeature.__init__)
    params = list(sig.parameters.keys())



def test_featuremodelmetamodel::variablefeature_is_not_abstract():
    assert not inspect.isabstract(featureModelMetamodel::VariableFeature)


def test_featuremodelmetamodel::variablefeature_constructor_exists():
    assert callable(featureModelMetamodel::VariableFeature.__init__)


def test_featuremodelmetamodel::variablefeature_constructor_args():
    sig = inspect.signature(featureModelMetamodel::VariableFeature.__init__)
    params = list(sig.parameters.keys())



def test_featuremodelmetamodel::attribute_is_not_abstract():
    assert not inspect.isabstract(featureModelMetamodel::Attribute)


def test_featuremodelmetamodel::attribute_constructor_exists():
    assert callable(featureModelMetamodel::Attribute.__init__)


def test_featuremodelmetamodel::attribute_constructor_args():
    sig = inspect.signature(featureModelMetamodel::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_featuremodelmetamodel::groupmultiplicity_is_not_abstract():
    assert not inspect.isabstract(featureModelMetamodel::GroupMultiplicity)


def test_featuremodelmetamodel::groupmultiplicity_constructor_exists():
    assert callable(featureModelMetamodel::GroupMultiplicity.__init__)


def test_featuremodelmetamodel::groupmultiplicity_constructor_args():
    sig = inspect.signature(featureModelMetamodel::GroupMultiplicity.__init__)
    params = list(sig.parameters.keys())



def test_featuremodelmetamodel::feature_is_not_abstract():
    assert not inspect.isabstract(featureModelMetamodel::Feature)


def test_featuremodelmetamodel::feature_constructor_exists():
    assert callable(featureModelMetamodel::Feature.__init__)


def test_featuremodelmetamodel::feature_constructor_args():
    sig = inspect.signature(featureModelMetamodel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "variabilityType" in params, "Missing parameter 'variabilityType'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_featuremodelmetamodel::feature_has_variabilityType():
    assert hasattr(featureModelMetamodel::Feature, "variabilityType")
    descriptor = None
    for klass in featureModelMetamodel::Feature.__mro__:
        if "variabilityType" in klass.__dict__:
            descriptor = klass.__dict__["variabilityType"]
            break
    assert isinstance(descriptor, property)

def test_featuremodelmetamodel::feature_has_id():
    assert hasattr(featureModelMetamodel::Feature, "id")
    descriptor = None
    for klass in featureModelMetamodel::Feature.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_featuremodelmetamodel::feature_has_name():
    assert hasattr(featureModelMetamodel::Feature, "name")
    descriptor = None
    for klass in featureModelMetamodel::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_featuremodelmetamodel::featuremodel_is_not_abstract():
    assert not inspect.isabstract(featureModelMetamodel::FeatureModel)


def test_featuremodelmetamodel::featuremodel_constructor_exists():
    assert callable(featureModelMetamodel::FeatureModel.__init__)


def test_featuremodelmetamodel::featuremodel_constructor_args():
    sig = inspect.signature(featureModelMetamodel::FeatureModel.__init__)
    params = list(sig.parameters.keys())



def test_featuremodelmetamodel::constraint_is_not_abstract():
    assert not inspect.isabstract(featureModelMetamodel::Constraint)


def test_featuremodelmetamodel::constraint_constructor_exists():
    assert callable(featureModelMetamodel::Constraint.__init__)


def test_featuremodelmetamodel::constraint_constructor_args():
    sig = inspect.signature(featureModelMetamodel::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "id" in params, "Missing parameter 'id'"
    assert "language" in params, "Missing parameter 'language'"

def test_featuremodelmetamodel::constraint_has_code():
    assert hasattr(featureModelMetamodel::Constraint, "code")
    descriptor = None
    for klass in featureModelMetamodel::Constraint.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_featuremodelmetamodel::constraint_has_id():
    assert hasattr(featureModelMetamodel::Constraint, "id")
    descriptor = None
    for klass in featureModelMetamodel::Constraint.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_featuremodelmetamodel::constraint_has_language():
    assert hasattr(featureModelMetamodel::Constraint, "language")
    descriptor = None
    for klass in featureModelMetamodel::Constraint.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_featuremodelmetamodel::abstractfeature_is_not_abstract():
    assert not inspect.isabstract(featureModelMetamodel::AbstractFeature)


def test_featuremodelmetamodel::abstractfeature_constructor_exists():
    assert callable(featureModelMetamodel::AbstractFeature.__init__)


def test_featuremodelmetamodel::abstractfeature_constructor_args():
    sig = inspect.signature(featureModelMetamodel::AbstractFeature.__init__)
    params = list(sig.parameters.keys())



def test_featuremodelmetamodel::multiplicity__is_not_abstract():
    assert not inspect.isabstract(featureModelMetamodel::Multiplicity_)


def test_featuremodelmetamodel::multiplicity__constructor_exists():
    assert callable(featureModelMetamodel::Multiplicity_.__init__)


def test_featuremodelmetamodel::multiplicity__constructor_args():
    sig = inspect.signature(featureModelMetamodel::Multiplicity_.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_featuremodelmetamodel::multiplicity__has_lower():
    assert hasattr(featureModelMetamodel::Multiplicity_, "lower")
    descriptor = None
    for klass in featureModelMetamodel::Multiplicity_.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_featuremodelmetamodel::multiplicity__has_upper():
    assert hasattr(featureModelMetamodel::Multiplicity_, "upper")
    descriptor = None
    for klass in featureModelMetamodel::Multiplicity_.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_selectionstate_exists():
    # Check that the Enumeration exists
    assert SelectionState is not None

def test_selectionstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SelectionState]
    expected_literals = [
        "selected",
        "unselected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SelectionState"

def test_variabilitytype_exists():
    # Check that the Enumeration exists
    assert VariabilityType is not None

def test_variabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariabilityType]
    expected_literals = [
        "alternative",
        "optional",
        "or_",
        "mandatory",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariabilityType"


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
featureModelMetamodel::ConfigurationModel_strategy = st.builds(
    featureModelMetamodel::ConfigurationModel,
)
Selection_strategy = st.builds(
    Selection,
)
featureModelMetamodel::ClonableSelection_strategy = st.builds(
    featureModelMetamodel::ClonableSelection,
    instance=
        safe_text
)
featureModelMetamodel::Selection_strategy = st.builds(
    featureModelMetamodel::Selection,
    state=
        safe_text,
    name=
        safe_text
)
Multiplicity__strategy = st.builds(
    Multiplicity_,
)
Feature_strategy = st.builds(
    Feature,
)
featureModelMetamodel::ClonableFeature_strategy = st.builds(
    featureModelMetamodel::ClonableFeature,
)
featureModelMetamodel::VariableFeature_strategy = st.builds(
    featureModelMetamodel::VariableFeature,
)
featureModelMetamodel::Attribute_strategy = st.builds(
    featureModelMetamodel::Attribute,
)
featureModelMetamodel::GroupMultiplicity_strategy = st.builds(
    featureModelMetamodel::GroupMultiplicity,
)
featureModelMetamodel::Feature_strategy = st.builds(
    featureModelMetamodel::Feature,
    variabilityType=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
featureModelMetamodel::FeatureModel_strategy = st.builds(
    featureModelMetamodel::FeatureModel,
)
featureModelMetamodel::Constraint_strategy = st.builds(
    featureModelMetamodel::Constraint,
    code=
        safe_text,
    id=
        safe_text,
    language=
        safe_text
)
featureModelMetamodel::AbstractFeature_strategy = st.builds(
    featureModelMetamodel::AbstractFeature,
)
featureModelMetamodel::Multiplicity__strategy = st.builds(
    featureModelMetamodel::Multiplicity_,
    lower=
        safe_text,
    upper=
        safe_text
)

@given(instance=featureModelMetamodel::ConfigurationModel_strategy)
@settings(max_examples=50)
def test_featuremodelmetamodel::configurationmodel_instantiation(instance):
    assert isinstance(instance, featureModelMetamodel::ConfigurationModel)

@given(instance=Selection_strategy)
@settings(max_examples=50)
def test_selection_instantiation(instance):
    assert isinstance(instance, Selection)

@given(instance=featureModelMetamodel::ClonableSelection_strategy)
@settings(max_examples=50)
def test_featuremodelmetamodel::clonableselection_instantiation(instance):
    assert isinstance(instance, featureModelMetamodel::ClonableSelection)

@given(instance=featureModelMetamodel::ClonableSelection_strategy)
def test_featuremodelmetamodel::clonableselection_instance_type(instance):
    assert isinstance(instance.instance, str)


@given(instance=featureModelMetamodel::ClonableSelection_strategy)
def test_featuremodelmetamodel::clonableselection_instance_setter(instance):
    original = instance.instance
    instance.instance = original
    assert instance.instance == original

@given(instance=featureModelMetamodel::Selection_strategy)
@settings(max_examples=50)
def test_featuremodelmetamodel::selection_instantiation(instance):
    assert isinstance(instance, featureModelMetamodel::Selection)

@given(instance=featureModelMetamodel::Selection_strategy)
def test_featuremodelmetamodel::selection_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=featureModelMetamodel::Selection_strategy)
def test_featuremodelmetamodel::selection_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=featureModelMetamodel::Selection_strategy)
def test_featuremodelmetamodel::selection_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featureModelMetamodel::Selection_strategy)
def test_featuremodelmetamodel::selection_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Multiplicity__strategy)
@settings(max_examples=50)
def test_multiplicity__instantiation(instance):
    assert isinstance(instance, Multiplicity_)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=featureModelMetamodel::ClonableFeature_strategy)
@settings(max_examples=50)
def test_featuremodelmetamodel::clonablefeature_instantiation(instance):
    assert isinstance(instance, featureModelMetamodel::ClonableFeature)

@given(instance=featureModelMetamodel::VariableFeature_strategy)
@settings(max_examples=50)
def test_featuremodelmetamodel::variablefeature_instantiation(instance):
    assert isinstance(instance, featureModelMetamodel::VariableFeature)

@given(instance=featureModelMetamodel::Attribute_strategy)
@settings(max_examples=50)
def test_featuremodelmetamodel::attribute_instantiation(instance):
    assert isinstance(instance, featureModelMetamodel::Attribute)

@given(instance=featureModelMetamodel::GroupMultiplicity_strategy)
@settings(max_examples=50)
def test_featuremodelmetamodel::groupmultiplicity_instantiation(instance):
    assert isinstance(instance, featureModelMetamodel::GroupMultiplicity)

@given(instance=featureModelMetamodel::Feature_strategy)
@settings(max_examples=50)
def test_featuremodelmetamodel::feature_instantiation(instance):
    assert isinstance(instance, featureModelMetamodel::Feature)

@given(instance=featureModelMetamodel::Feature_strategy)
def test_featuremodelmetamodel::feature_variabilityType_type(instance):
    assert isinstance(instance.variabilityType, str)


@given(instance=featureModelMetamodel::Feature_strategy)
def test_featuremodelmetamodel::feature_variabilityType_setter(instance):
    original = instance.variabilityType
    instance.variabilityType = original
    assert instance.variabilityType == original

@given(instance=featureModelMetamodel::Feature_strategy)
def test_featuremodelmetamodel::feature_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=featureModelMetamodel::Feature_strategy)
def test_featuremodelmetamodel::feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=featureModelMetamodel::Feature_strategy)
def test_featuremodelmetamodel::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featureModelMetamodel::Feature_strategy)
def test_featuremodelmetamodel::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featureModelMetamodel::FeatureModel_strategy)
@settings(max_examples=50)
def test_featuremodelmetamodel::featuremodel_instantiation(instance):
    assert isinstance(instance, featureModelMetamodel::FeatureModel)

@given(instance=featureModelMetamodel::Constraint_strategy)
@settings(max_examples=50)
def test_featuremodelmetamodel::constraint_instantiation(instance):
    assert isinstance(instance, featureModelMetamodel::Constraint)

@given(instance=featureModelMetamodel::Constraint_strategy)
def test_featuremodelmetamodel::constraint_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=featureModelMetamodel::Constraint_strategy)
def test_featuremodelmetamodel::constraint_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=featureModelMetamodel::Constraint_strategy)
def test_featuremodelmetamodel::constraint_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=featureModelMetamodel::Constraint_strategy)
def test_featuremodelmetamodel::constraint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=featureModelMetamodel::Constraint_strategy)
def test_featuremodelmetamodel::constraint_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=featureModelMetamodel::Constraint_strategy)
def test_featuremodelmetamodel::constraint_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=featureModelMetamodel::AbstractFeature_strategy)
@settings(max_examples=50)
def test_featuremodelmetamodel::abstractfeature_instantiation(instance):
    assert isinstance(instance, featureModelMetamodel::AbstractFeature)

@given(instance=featureModelMetamodel::Multiplicity__strategy)
@settings(max_examples=50)
def test_featuremodelmetamodel::multiplicity__instantiation(instance):
    assert isinstance(instance, featureModelMetamodel::Multiplicity_)

@given(instance=featureModelMetamodel::Multiplicity__strategy)
def test_featuremodelmetamodel::multiplicity__lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=featureModelMetamodel::Multiplicity__strategy)
def test_featuremodelmetamodel::multiplicity__lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=featureModelMetamodel::Multiplicity__strategy)
def test_featuremodelmetamodel::multiplicity__upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=featureModelMetamodel::Multiplicity__strategy)
def test_featuremodelmetamodel::multiplicity__upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original
