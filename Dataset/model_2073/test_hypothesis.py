import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Feature,
    featuretree_TreeFeature,
    core_ITopLevelElement,
    features_IFeatureDomain,
    core_AbstractModelElement,
    featuretree_FeatureTree,
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



def test_featuretree_treefeature_is_not_abstract():
    assert not inspect.isabstract(featuretree_TreeFeature)


def test_featuretree_treefeature_constructor_exists():
    assert callable(featuretree_TreeFeature.__init__)


def test_featuretree_treefeature_constructor_args():
    sig = inspect.signature(featuretree_TreeFeature.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_featuretree_treefeature_has_mandatory():
    assert hasattr(featuretree_TreeFeature, "mandatory")
    descriptor = None
    for klass in featuretree_TreeFeature.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_core_itoplevelelement_is_not_abstract():
    assert not inspect.isabstract(core_ITopLevelElement)


def test_core_itoplevelelement_constructor_exists():
    assert callable(core_ITopLevelElement.__init__)


def test_core_itoplevelelement_constructor_args():
    sig = inspect.signature(core_ITopLevelElement.__init__)
    params = list(sig.parameters.keys())



def test_features_ifeaturedomain_is_not_abstract():
    assert not inspect.isabstract(features_IFeatureDomain)


def test_features_ifeaturedomain_constructor_exists():
    assert callable(features_IFeatureDomain.__init__)


def test_features_ifeaturedomain_constructor_args():
    sig = inspect.signature(features_IFeatureDomain.__init__)
    params = list(sig.parameters.keys())



def test_core_abstractmodelelement_is_not_abstract():
    assert not inspect.isabstract(core_AbstractModelElement)


def test_core_abstractmodelelement_constructor_exists():
    assert callable(core_AbstractModelElement.__init__)


def test_core_abstractmodelelement_constructor_args():
    sig = inspect.signature(core_AbstractModelElement.__init__)
    params = list(sig.parameters.keys())



def test_featuretree_featuretree_is_not_abstract():
    assert not inspect.isabstract(featuretree_FeatureTree)


def test_featuretree_featuretree_constructor_exists():
    assert callable(featuretree_FeatureTree.__init__)


def test_featuretree_featuretree_constructor_args():
    sig = inspect.signature(featuretree_FeatureTree.__init__)
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
featuretree_TreeFeature_strategy = st.builds(
    featuretree_TreeFeature,
    mandatory=
        st.booleans()
)
core_ITopLevelElement_strategy = st.builds(
    core_ITopLevelElement,
)
features_IFeatureDomain_strategy = st.builds(
    features_IFeatureDomain,
)
core_AbstractModelElement_strategy = st.builds(
    core_AbstractModelElement,
)
featuretree_FeatureTree_strategy = st.builds(
    featuretree_FeatureTree,
)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=featuretree_TreeFeature_strategy)
@settings(max_examples=50)
def test_featuretree_treefeature_instantiation(instance):
    assert isinstance(instance, featuretree_TreeFeature)



@given(instance=featuretree_TreeFeature_strategy)
def test_featuretree_treefeature_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=core_ITopLevelElement_strategy)
@settings(max_examples=50)
def test_core_itoplevelelement_instantiation(instance):
    assert isinstance(instance, core_ITopLevelElement)

@given(instance=features_IFeatureDomain_strategy)
@settings(max_examples=50)
def test_features_ifeaturedomain_instantiation(instance):
    assert isinstance(instance, features_IFeatureDomain)

@given(instance=core_AbstractModelElement_strategy)
@settings(max_examples=50)
def test_core_abstractmodelelement_instantiation(instance):
    assert isinstance(instance, core_AbstractModelElement)

@given(instance=featuretree_FeatureTree_strategy)
@settings(max_examples=50)
def test_featuretree_featuretree_instantiation(instance):
    assert isinstance(instance, featuretree_FeatureTree)
