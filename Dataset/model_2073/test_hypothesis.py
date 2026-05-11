import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Feature,
    featuretree::TreeFeature,
    core::ITopLevelElement,
    features::IFeatureDomain,
    core::AbstractModelElement,
    featuretree::FeatureTree,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_featuretree::treefeature_is_not_abstract():
    assert not inspect.isabstract(featuretree::TreeFeature)


def test_featuretree::treefeature_constructor_exists():
    assert callable(featuretree::TreeFeature.__init__)


def test_featuretree::treefeature_constructor_args():
    sig = inspect.signature(featuretree::TreeFeature.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_featuretree::treefeature_has_mandatory():
    assert hasattr(featuretree::TreeFeature, "mandatory")
    descriptor = None
    for klass in featuretree::TreeFeature.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_core::itoplevelelement_is_not_abstract():
    assert not inspect.isabstract(core::ITopLevelElement)


def test_core::itoplevelelement_constructor_exists():
    assert callable(core::ITopLevelElement.__init__)


def test_core::itoplevelelement_constructor_args():
    sig = inspect.signature(core::ITopLevelElement.__init__)
    params = list(sig.parameters.keys())



def test_features::ifeaturedomain_is_not_abstract():
    assert not inspect.isabstract(features::IFeatureDomain)


def test_features::ifeaturedomain_constructor_exists():
    assert callable(features::IFeatureDomain.__init__)


def test_features::ifeaturedomain_constructor_args():
    sig = inspect.signature(features::IFeatureDomain.__init__)
    params = list(sig.parameters.keys())



def test_core::abstractmodelelement_is_not_abstract():
    assert not inspect.isabstract(core::AbstractModelElement)


def test_core::abstractmodelelement_constructor_exists():
    assert callable(core::AbstractModelElement.__init__)


def test_core::abstractmodelelement_constructor_args():
    sig = inspect.signature(core::AbstractModelElement.__init__)
    params = list(sig.parameters.keys())



def test_featuretree::featuretree_is_not_abstract():
    assert not inspect.isabstract(featuretree::FeatureTree)


def test_featuretree::featuretree_constructor_exists():
    assert callable(featuretree::FeatureTree.__init__)


def test_featuretree::featuretree_constructor_args():
    sig = inspect.signature(featuretree::FeatureTree.__init__)
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
Feature_strategy = st.builds(
    Feature,
)
featuretree::TreeFeature_strategy = st.builds(
    featuretree::TreeFeature,
    mandatory=
        st.booleans()
)
core::ITopLevelElement_strategy = st.builds(
    core::ITopLevelElement,
)
features::IFeatureDomain_strategy = st.builds(
    features::IFeatureDomain,
)
core::AbstractModelElement_strategy = st.builds(
    core::AbstractModelElement,
)
featuretree::FeatureTree_strategy = st.builds(
    featuretree::FeatureTree,
)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=featuretree::TreeFeature_strategy)
@settings(max_examples=50)
def test_featuretree::treefeature_instantiation(instance):
    assert isinstance(instance, featuretree::TreeFeature)

@given(instance=featuretree::TreeFeature_strategy)
def test_featuretree::treefeature_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=featuretree::TreeFeature_strategy)
def test_featuretree::treefeature_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=core::ITopLevelElement_strategy)
@settings(max_examples=50)
def test_core::itoplevelelement_instantiation(instance):
    assert isinstance(instance, core::ITopLevelElement)

@given(instance=features::IFeatureDomain_strategy)
@settings(max_examples=50)
def test_features::ifeaturedomain_instantiation(instance):
    assert isinstance(instance, features::IFeatureDomain)

@given(instance=core::AbstractModelElement_strategy)
@settings(max_examples=50)
def test_core::abstractmodelelement_instantiation(instance):
    assert isinstance(instance, core::AbstractModelElement)

@given(instance=featuretree::FeatureTree_strategy)
@settings(max_examples=50)
def test_featuretree::featuretree_instantiation(instance):
    assert isinstance(instance, featuretree::FeatureTree)
