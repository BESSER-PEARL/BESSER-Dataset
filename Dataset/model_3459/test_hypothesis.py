import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Influence,
    FeatureConstraint,
    Conncection,
    FCORE::Conncection,
    FCORE::Influence,
    SingleFeatureConnection,
    FCORE::CardinalityConnection,
    Feature,
    FCORE::SingleFeatureConnection,
    FCORE::FeatureConstraint,
    FCORE::InfluenceAttribute,
    FCORE::InfluenceFeature,
    FCORE::Softgoal,
    FCORE::ExcludesFeatureConstraint,
    FCORE::RequiresFeatureConstraint,
    FCORE::AttributeConstraint,
    FCORE::Attribute,
    FCORE::FeatureGroup,
    FCORE::SolitaryFeature,
    FCORE::GroupFeature,
    FCORE::RootFeature,
    FCORE::FeatureModel,
    FCORE::Feature,
    FCORE::AttributeConstraintConnection,
    FCORE::GroupToFeatureConnection,
    FCORE::FeatureToGroupConnection,
    FCORE::OptionalConnection,
    FCORE::MandatoryConnection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_influence_is_not_abstract():
    assert not inspect.isabstract(Influence)


def test_influence_constructor_exists():
    assert callable(Influence.__init__)


def test_influence_constructor_args():
    sig = inspect.signature(Influence.__init__)
    params = list(sig.parameters.keys())



def test_featureconstraint_is_not_abstract():
    assert not inspect.isabstract(FeatureConstraint)


def test_featureconstraint_constructor_exists():
    assert callable(FeatureConstraint.__init__)


def test_featureconstraint_constructor_args():
    sig = inspect.signature(FeatureConstraint.__init__)
    params = list(sig.parameters.keys())



def test_conncection_is_not_abstract():
    assert not inspect.isabstract(Conncection)


def test_conncection_constructor_exists():
    assert callable(Conncection.__init__)


def test_conncection_constructor_args():
    sig = inspect.signature(Conncection.__init__)
    params = list(sig.parameters.keys())



def test_fcore::conncection_is_not_abstract():
    assert not inspect.isabstract(FCORE::Conncection)


def test_fcore::conncection_constructor_exists():
    assert callable(FCORE::Conncection.__init__)


def test_fcore::conncection_constructor_args():
    sig = inspect.signature(FCORE::Conncection.__init__)
    params = list(sig.parameters.keys())



def test_fcore::influence_is_not_abstract():
    assert not inspect.isabstract(FCORE::Influence)


def test_fcore::influence_constructor_exists():
    assert callable(FCORE::Influence.__init__)


def test_fcore::influence_constructor_args():
    sig = inspect.signature(FCORE::Influence.__init__)
    params = list(sig.parameters.keys())
    assert "contribution" in params, "Missing parameter 'contribution'"

def test_fcore::influence_has_contribution():
    assert hasattr(FCORE::Influence, "contribution")
    descriptor = None
    for klass in FCORE::Influence.__mro__:
        if "contribution" in klass.__dict__:
            descriptor = klass.__dict__["contribution"]
            break
    assert isinstance(descriptor, property)



def test_singlefeatureconnection_is_not_abstract():
    assert not inspect.isabstract(SingleFeatureConnection)


def test_singlefeatureconnection_constructor_exists():
    assert callable(SingleFeatureConnection.__init__)


def test_singlefeatureconnection_constructor_args():
    sig = inspect.signature(SingleFeatureConnection.__init__)
    params = list(sig.parameters.keys())



def test_fcore::cardinalityconnection_is_not_abstract():
    assert not inspect.isabstract(FCORE::CardinalityConnection)


def test_fcore::cardinalityconnection_constructor_exists():
    assert callable(FCORE::CardinalityConnection.__init__)


def test_fcore::cardinalityconnection_constructor_args():
    sig = inspect.signature(FCORE::CardinalityConnection.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_fcore::cardinalityconnection_has_min():
    assert hasattr(FCORE::CardinalityConnection, "min")
    descriptor = None
    for klass in FCORE::CardinalityConnection.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_fcore::cardinalityconnection_has_max():
    assert hasattr(FCORE::CardinalityConnection, "max")
    descriptor = None
    for klass in FCORE::CardinalityConnection.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_fcore::singlefeatureconnection_is_not_abstract():
    assert not inspect.isabstract(FCORE::SingleFeatureConnection)


def test_fcore::singlefeatureconnection_constructor_exists():
    assert callable(FCORE::SingleFeatureConnection.__init__)


def test_fcore::singlefeatureconnection_constructor_args():
    sig = inspect.signature(FCORE::SingleFeatureConnection.__init__)
    params = list(sig.parameters.keys())



def test_fcore::featureconstraint_is_not_abstract():
    assert not inspect.isabstract(FCORE::FeatureConstraint)


def test_fcore::featureconstraint_constructor_exists():
    assert callable(FCORE::FeatureConstraint.__init__)


def test_fcore::featureconstraint_constructor_args():
    sig = inspect.signature(FCORE::FeatureConstraint.__init__)
    params = list(sig.parameters.keys())



def test_fcore::influenceattribute_is_not_abstract():
    assert not inspect.isabstract(FCORE::InfluenceAttribute)


def test_fcore::influenceattribute_constructor_exists():
    assert callable(FCORE::InfluenceAttribute.__init__)


def test_fcore::influenceattribute_constructor_args():
    sig = inspect.signature(FCORE::InfluenceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_fcore::influencefeature_is_not_abstract():
    assert not inspect.isabstract(FCORE::InfluenceFeature)


def test_fcore::influencefeature_constructor_exists():
    assert callable(FCORE::InfluenceFeature.__init__)


def test_fcore::influencefeature_constructor_args():
    sig = inspect.signature(FCORE::InfluenceFeature.__init__)
    params = list(sig.parameters.keys())



def test_fcore::softgoal_is_not_abstract():
    assert not inspect.isabstract(FCORE::Softgoal)


def test_fcore::softgoal_constructor_exists():
    assert callable(FCORE::Softgoal.__init__)


def test_fcore::softgoal_constructor_args():
    sig = inspect.signature(FCORE::Softgoal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "weighting" in params, "Missing parameter 'weighting'"

def test_fcore::softgoal_has_name():
    assert hasattr(FCORE::Softgoal, "name")
    descriptor = None
    for klass in FCORE::Softgoal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fcore::softgoal_has_weighting():
    assert hasattr(FCORE::Softgoal, "weighting")
    descriptor = None
    for klass in FCORE::Softgoal.__mro__:
        if "weighting" in klass.__dict__:
            descriptor = klass.__dict__["weighting"]
            break
    assert isinstance(descriptor, property)



def test_fcore::excludesfeatureconstraint_is_not_abstract():
    assert not inspect.isabstract(FCORE::ExcludesFeatureConstraint)


def test_fcore::excludesfeatureconstraint_constructor_exists():
    assert callable(FCORE::ExcludesFeatureConstraint.__init__)


def test_fcore::excludesfeatureconstraint_constructor_args():
    sig = inspect.signature(FCORE::ExcludesFeatureConstraint.__init__)
    params = list(sig.parameters.keys())



def test_fcore::requiresfeatureconstraint_is_not_abstract():
    assert not inspect.isabstract(FCORE::RequiresFeatureConstraint)


def test_fcore::requiresfeatureconstraint_constructor_exists():
    assert callable(FCORE::RequiresFeatureConstraint.__init__)


def test_fcore::requiresfeatureconstraint_constructor_args():
    sig = inspect.signature(FCORE::RequiresFeatureConstraint.__init__)
    params = list(sig.parameters.keys())



def test_fcore::attributeconstraint_is_not_abstract():
    assert not inspect.isabstract(FCORE::AttributeConstraint)


def test_fcore::attributeconstraint_constructor_exists():
    assert callable(FCORE::AttributeConstraint.__init__)


def test_fcore::attributeconstraint_constructor_args():
    sig = inspect.signature(FCORE::AttributeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "equation" in params, "Missing parameter 'equation'"

def test_fcore::attributeconstraint_has_equation():
    assert hasattr(FCORE::AttributeConstraint, "equation")
    descriptor = None
    for klass in FCORE::AttributeConstraint.__mro__:
        if "equation" in klass.__dict__:
            descriptor = klass.__dict__["equation"]
            break
    assert isinstance(descriptor, property)



def test_fcore::attribute_is_not_abstract():
    assert not inspect.isabstract(FCORE::Attribute)


def test_fcore::attribute_constructor_exists():
    assert callable(FCORE::Attribute.__init__)


def test_fcore::attribute_constructor_args():
    sig = inspect.signature(FCORE::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"
    assert "name" in params, "Missing parameter 'name'"

def test_fcore::attribute_has_value():
    assert hasattr(FCORE::Attribute, "value")
    descriptor = None
    for klass in FCORE::Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fcore::attribute_has_max():
    assert hasattr(FCORE::Attribute, "max")
    descriptor = None
    for klass in FCORE::Attribute.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_fcore::attribute_has_min():
    assert hasattr(FCORE::Attribute, "min")
    descriptor = None
    for klass in FCORE::Attribute.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_fcore::attribute_has_name():
    assert hasattr(FCORE::Attribute, "name")
    descriptor = None
    for klass in FCORE::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fcore::featuregroup_is_not_abstract():
    assert not inspect.isabstract(FCORE::FeatureGroup)


def test_fcore::featuregroup_constructor_exists():
    assert callable(FCORE::FeatureGroup.__init__)


def test_fcore::featuregroup_constructor_args():
    sig = inspect.signature(FCORE::FeatureGroup.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_fcore::featuregroup_has_max():
    assert hasattr(FCORE::FeatureGroup, "max")
    descriptor = None
    for klass in FCORE::FeatureGroup.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_fcore::featuregroup_has_min():
    assert hasattr(FCORE::FeatureGroup, "min")
    descriptor = None
    for klass in FCORE::FeatureGroup.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_fcore::solitaryfeature_is_not_abstract():
    assert not inspect.isabstract(FCORE::SolitaryFeature)


def test_fcore::solitaryfeature_constructor_exists():
    assert callable(FCORE::SolitaryFeature.__init__)


def test_fcore::solitaryfeature_constructor_args():
    sig = inspect.signature(FCORE::SolitaryFeature.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_fcore::solitaryfeature_has_max():
    assert hasattr(FCORE::SolitaryFeature, "max")
    descriptor = None
    for klass in FCORE::SolitaryFeature.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_fcore::solitaryfeature_has_min():
    assert hasattr(FCORE::SolitaryFeature, "min")
    descriptor = None
    for klass in FCORE::SolitaryFeature.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_fcore::groupfeature_is_not_abstract():
    assert not inspect.isabstract(FCORE::GroupFeature)


def test_fcore::groupfeature_constructor_exists():
    assert callable(FCORE::GroupFeature.__init__)


def test_fcore::groupfeature_constructor_args():
    sig = inspect.signature(FCORE::GroupFeature.__init__)
    params = list(sig.parameters.keys())



def test_fcore::rootfeature_is_not_abstract():
    assert not inspect.isabstract(FCORE::RootFeature)


def test_fcore::rootfeature_constructor_exists():
    assert callable(FCORE::RootFeature.__init__)


def test_fcore::rootfeature_constructor_args():
    sig = inspect.signature(FCORE::RootFeature.__init__)
    params = list(sig.parameters.keys())



def test_fcore::featuremodel_is_not_abstract():
    assert not inspect.isabstract(FCORE::FeatureModel)


def test_fcore::featuremodel_constructor_exists():
    assert callable(FCORE::FeatureModel.__init__)


def test_fcore::featuremodel_constructor_args():
    sig = inspect.signature(FCORE::FeatureModel.__init__)
    params = list(sig.parameters.keys())



def test_fcore::feature_is_not_abstract():
    assert not inspect.isabstract(FCORE::Feature)


def test_fcore::feature_constructor_exists():
    assert callable(FCORE::Feature.__init__)


def test_fcore::feature_constructor_args():
    sig = inspect.signature(FCORE::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "selected" in params, "Missing parameter 'selected'"

def test_fcore::feature_has_name():
    assert hasattr(FCORE::Feature, "name")
    descriptor = None
    for klass in FCORE::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fcore::feature_has_selected():
    assert hasattr(FCORE::Feature, "selected")
    descriptor = None
    for klass in FCORE::Feature.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)



def test_fcore::attributeconstraintconnection_is_not_abstract():
    assert not inspect.isabstract(FCORE::AttributeConstraintConnection)


def test_fcore::attributeconstraintconnection_constructor_exists():
    assert callable(FCORE::AttributeConstraintConnection.__init__)


def test_fcore::attributeconstraintconnection_constructor_args():
    sig = inspect.signature(FCORE::AttributeConstraintConnection.__init__)
    params = list(sig.parameters.keys())



def test_fcore::grouptofeatureconnection_is_not_abstract():
    assert not inspect.isabstract(FCORE::GroupToFeatureConnection)


def test_fcore::grouptofeatureconnection_constructor_exists():
    assert callable(FCORE::GroupToFeatureConnection.__init__)


def test_fcore::grouptofeatureconnection_constructor_args():
    sig = inspect.signature(FCORE::GroupToFeatureConnection.__init__)
    params = list(sig.parameters.keys())



def test_fcore::featuretogroupconnection_is_not_abstract():
    assert not inspect.isabstract(FCORE::FeatureToGroupConnection)


def test_fcore::featuretogroupconnection_constructor_exists():
    assert callable(FCORE::FeatureToGroupConnection.__init__)


def test_fcore::featuretogroupconnection_constructor_args():
    sig = inspect.signature(FCORE::FeatureToGroupConnection.__init__)
    params = list(sig.parameters.keys())



def test_fcore::optionalconnection_is_not_abstract():
    assert not inspect.isabstract(FCORE::OptionalConnection)


def test_fcore::optionalconnection_constructor_exists():
    assert callable(FCORE::OptionalConnection.__init__)


def test_fcore::optionalconnection_constructor_args():
    sig = inspect.signature(FCORE::OptionalConnection.__init__)
    params = list(sig.parameters.keys())



def test_fcore::mandatoryconnection_is_not_abstract():
    assert not inspect.isabstract(FCORE::MandatoryConnection)


def test_fcore::mandatoryconnection_constructor_exists():
    assert callable(FCORE::MandatoryConnection.__init__)


def test_fcore::mandatoryconnection_constructor_args():
    sig = inspect.signature(FCORE::MandatoryConnection.__init__)
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
Influence_strategy = st.builds(
    Influence,
)
FeatureConstraint_strategy = st.builds(
    FeatureConstraint,
)
Conncection_strategy = st.builds(
    Conncection,
)
FCORE::Conncection_strategy = st.builds(
    FCORE::Conncection,
)
FCORE::Influence_strategy = st.builds(
    FCORE::Influence,
    contribution=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SingleFeatureConnection_strategy = st.builds(
    SingleFeatureConnection,
)
FCORE::CardinalityConnection_strategy = st.builds(
    FCORE::CardinalityConnection,
    min=
        st.integers(),
    max=
        st.integers()
)
Feature_strategy = st.builds(
    Feature,
)
FCORE::SingleFeatureConnection_strategy = st.builds(
    FCORE::SingleFeatureConnection,
)
FCORE::FeatureConstraint_strategy = st.builds(
    FCORE::FeatureConstraint,
)
FCORE::InfluenceAttribute_strategy = st.builds(
    FCORE::InfluenceAttribute,
)
FCORE::InfluenceFeature_strategy = st.builds(
    FCORE::InfluenceFeature,
)
FCORE::Softgoal_strategy = st.builds(
    FCORE::Softgoal,
    name=
        safe_text,
    weighting=
        safe_text
)
FCORE::ExcludesFeatureConstraint_strategy = st.builds(
    FCORE::ExcludesFeatureConstraint,
)
FCORE::RequiresFeatureConstraint_strategy = st.builds(
    FCORE::RequiresFeatureConstraint,
)
FCORE::AttributeConstraint_strategy = st.builds(
    FCORE::AttributeConstraint,
    equation=
        safe_text
)
FCORE::Attribute_strategy = st.builds(
    FCORE::Attribute,
    value=
        st.integers(),
    max=
        st.integers(),
    min=
        st.integers(),
    name=
        safe_text
)
FCORE::FeatureGroup_strategy = st.builds(
    FCORE::FeatureGroup,
    max=
        st.integers(),
    min=
        st.integers()
)
FCORE::SolitaryFeature_strategy = st.builds(
    FCORE::SolitaryFeature,
    max=
        st.integers(),
    min=
        st.integers()
)
FCORE::GroupFeature_strategy = st.builds(
    FCORE::GroupFeature,
)
FCORE::RootFeature_strategy = st.builds(
    FCORE::RootFeature,
)
FCORE::FeatureModel_strategy = st.builds(
    FCORE::FeatureModel,
)
FCORE::Feature_strategy = st.builds(
    FCORE::Feature,
    name=
        safe_text,
    selected=
        st.booleans()
)
FCORE::AttributeConstraintConnection_strategy = st.builds(
    FCORE::AttributeConstraintConnection,
)
FCORE::GroupToFeatureConnection_strategy = st.builds(
    FCORE::GroupToFeatureConnection,
)
FCORE::FeatureToGroupConnection_strategy = st.builds(
    FCORE::FeatureToGroupConnection,
)
FCORE::OptionalConnection_strategy = st.builds(
    FCORE::OptionalConnection,
)
FCORE::MandatoryConnection_strategy = st.builds(
    FCORE::MandatoryConnection,
)

@given(instance=Influence_strategy)
@settings(max_examples=50)
def test_influence_instantiation(instance):
    assert isinstance(instance, Influence)

@given(instance=FeatureConstraint_strategy)
@settings(max_examples=50)
def test_featureconstraint_instantiation(instance):
    assert isinstance(instance, FeatureConstraint)

@given(instance=Conncection_strategy)
@settings(max_examples=50)
def test_conncection_instantiation(instance):
    assert isinstance(instance, Conncection)

@given(instance=FCORE::Conncection_strategy)
@settings(max_examples=50)
def test_fcore::conncection_instantiation(instance):
    assert isinstance(instance, FCORE::Conncection)

@given(instance=FCORE::Influence_strategy)
@settings(max_examples=50)
def test_fcore::influence_instantiation(instance):
    assert isinstance(instance, FCORE::Influence)

@given(instance=FCORE::Influence_strategy)
def test_fcore::influence_contribution_type(instance):
    assert isinstance(instance.contribution, float)


@given(instance=FCORE::Influence_strategy)
def test_fcore::influence_contribution_setter(instance):
    original = instance.contribution
    instance.contribution = original
    assert instance.contribution == original

@given(instance=SingleFeatureConnection_strategy)
@settings(max_examples=50)
def test_singlefeatureconnection_instantiation(instance):
    assert isinstance(instance, SingleFeatureConnection)

@given(instance=FCORE::CardinalityConnection_strategy)
@settings(max_examples=50)
def test_fcore::cardinalityconnection_instantiation(instance):
    assert isinstance(instance, FCORE::CardinalityConnection)

@given(instance=FCORE::CardinalityConnection_strategy)
def test_fcore::cardinalityconnection_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=FCORE::CardinalityConnection_strategy)
def test_fcore::cardinalityconnection_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=FCORE::CardinalityConnection_strategy)
def test_fcore::cardinalityconnection_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=FCORE::CardinalityConnection_strategy)
def test_fcore::cardinalityconnection_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=FCORE::SingleFeatureConnection_strategy)
@settings(max_examples=50)
def test_fcore::singlefeatureconnection_instantiation(instance):
    assert isinstance(instance, FCORE::SingleFeatureConnection)

@given(instance=FCORE::FeatureConstraint_strategy)
@settings(max_examples=50)
def test_fcore::featureconstraint_instantiation(instance):
    assert isinstance(instance, FCORE::FeatureConstraint)

@given(instance=FCORE::InfluenceAttribute_strategy)
@settings(max_examples=50)
def test_fcore::influenceattribute_instantiation(instance):
    assert isinstance(instance, FCORE::InfluenceAttribute)

@given(instance=FCORE::InfluenceFeature_strategy)
@settings(max_examples=50)
def test_fcore::influencefeature_instantiation(instance):
    assert isinstance(instance, FCORE::InfluenceFeature)

@given(instance=FCORE::Softgoal_strategy)
@settings(max_examples=50)
def test_fcore::softgoal_instantiation(instance):
    assert isinstance(instance, FCORE::Softgoal)

@given(instance=FCORE::Softgoal_strategy)
def test_fcore::softgoal_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FCORE::Softgoal_strategy)
def test_fcore::softgoal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FCORE::Softgoal_strategy)
def test_fcore::softgoal_weighting_type(instance):
    assert isinstance(instance.weighting, str)


@given(instance=FCORE::Softgoal_strategy)
def test_fcore::softgoal_weighting_setter(instance):
    original = instance.weighting
    instance.weighting = original
    assert instance.weighting == original

@given(instance=FCORE::ExcludesFeatureConstraint_strategy)
@settings(max_examples=50)
def test_fcore::excludesfeatureconstraint_instantiation(instance):
    assert isinstance(instance, FCORE::ExcludesFeatureConstraint)

@given(instance=FCORE::RequiresFeatureConstraint_strategy)
@settings(max_examples=50)
def test_fcore::requiresfeatureconstraint_instantiation(instance):
    assert isinstance(instance, FCORE::RequiresFeatureConstraint)

@given(instance=FCORE::AttributeConstraint_strategy)
@settings(max_examples=50)
def test_fcore::attributeconstraint_instantiation(instance):
    assert isinstance(instance, FCORE::AttributeConstraint)

@given(instance=FCORE::AttributeConstraint_strategy)
def test_fcore::attributeconstraint_equation_type(instance):
    assert isinstance(instance.equation, str)


@given(instance=FCORE::AttributeConstraint_strategy)
def test_fcore::attributeconstraint_equation_setter(instance):
    original = instance.equation
    instance.equation = original
    assert instance.equation == original

@given(instance=FCORE::Attribute_strategy)
@settings(max_examples=50)
def test_fcore::attribute_instantiation(instance):
    assert isinstance(instance, FCORE::Attribute)

@given(instance=FCORE::Attribute_strategy)
def test_fcore::attribute_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=FCORE::Attribute_strategy)
def test_fcore::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=FCORE::Attribute_strategy)
def test_fcore::attribute_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=FCORE::Attribute_strategy)
def test_fcore::attribute_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=FCORE::Attribute_strategy)
def test_fcore::attribute_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=FCORE::Attribute_strategy)
def test_fcore::attribute_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=FCORE::Attribute_strategy)
def test_fcore::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FCORE::Attribute_strategy)
def test_fcore::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FCORE::FeatureGroup_strategy)
@settings(max_examples=50)
def test_fcore::featuregroup_instantiation(instance):
    assert isinstance(instance, FCORE::FeatureGroup)

@given(instance=FCORE::FeatureGroup_strategy)
def test_fcore::featuregroup_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=FCORE::FeatureGroup_strategy)
def test_fcore::featuregroup_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=FCORE::FeatureGroup_strategy)
def test_fcore::featuregroup_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=FCORE::FeatureGroup_strategy)
def test_fcore::featuregroup_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=FCORE::SolitaryFeature_strategy)
@settings(max_examples=50)
def test_fcore::solitaryfeature_instantiation(instance):
    assert isinstance(instance, FCORE::SolitaryFeature)

@given(instance=FCORE::SolitaryFeature_strategy)
def test_fcore::solitaryfeature_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=FCORE::SolitaryFeature_strategy)
def test_fcore::solitaryfeature_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=FCORE::SolitaryFeature_strategy)
def test_fcore::solitaryfeature_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=FCORE::SolitaryFeature_strategy)
def test_fcore::solitaryfeature_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=FCORE::GroupFeature_strategy)
@settings(max_examples=50)
def test_fcore::groupfeature_instantiation(instance):
    assert isinstance(instance, FCORE::GroupFeature)

@given(instance=FCORE::RootFeature_strategy)
@settings(max_examples=50)
def test_fcore::rootfeature_instantiation(instance):
    assert isinstance(instance, FCORE::RootFeature)

@given(instance=FCORE::FeatureModel_strategy)
@settings(max_examples=50)
def test_fcore::featuremodel_instantiation(instance):
    assert isinstance(instance, FCORE::FeatureModel)

@given(instance=FCORE::Feature_strategy)
@settings(max_examples=50)
def test_fcore::feature_instantiation(instance):
    assert isinstance(instance, FCORE::Feature)

@given(instance=FCORE::Feature_strategy)
def test_fcore::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FCORE::Feature_strategy)
def test_fcore::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FCORE::Feature_strategy)
def test_fcore::feature_selected_type(instance):
    assert isinstance(instance.selected, bool)


@given(instance=FCORE::Feature_strategy)
def test_fcore::feature_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=FCORE::AttributeConstraintConnection_strategy)
@settings(max_examples=50)
def test_fcore::attributeconstraintconnection_instantiation(instance):
    assert isinstance(instance, FCORE::AttributeConstraintConnection)

@given(instance=FCORE::GroupToFeatureConnection_strategy)
@settings(max_examples=50)
def test_fcore::grouptofeatureconnection_instantiation(instance):
    assert isinstance(instance, FCORE::GroupToFeatureConnection)

@given(instance=FCORE::FeatureToGroupConnection_strategy)
@settings(max_examples=50)
def test_fcore::featuretogroupconnection_instantiation(instance):
    assert isinstance(instance, FCORE::FeatureToGroupConnection)

@given(instance=FCORE::OptionalConnection_strategy)
@settings(max_examples=50)
def test_fcore::optionalconnection_instantiation(instance):
    assert isinstance(instance, FCORE::OptionalConnection)

@given(instance=FCORE::MandatoryConnection_strategy)
@settings(max_examples=50)
def test_fcore::mandatoryconnection_instantiation(instance):
    assert isinstance(instance, FCORE::MandatoryConnection)
