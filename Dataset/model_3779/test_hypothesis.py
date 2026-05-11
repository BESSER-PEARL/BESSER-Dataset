import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SimpleIdentifier,
    feature::SimpleFeature,
    feature::EvidenceCode,
    feature::SimpleOntologyTerm,
    feature::Value,
    feature::SimpleIdentifier,
    SimpleFeature,
    feature::Feature,
    feature::FeatureSet,
    feature::AnnotatedSimpleFeature,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleidentifier_is_not_abstract():
    assert not inspect.isabstract(SimpleIdentifier)


def test_simpleidentifier_constructor_exists():
    assert callable(SimpleIdentifier.__init__)


def test_simpleidentifier_constructor_args():
    sig = inspect.signature(SimpleIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_feature::simplefeature_is_not_abstract():
    assert not inspect.isabstract(feature::SimpleFeature)


def test_feature::simplefeature_constructor_exists():
    assert callable(feature::SimpleFeature.__init__)


def test_feature::simplefeature_constructor_args():
    sig = inspect.signature(feature::SimpleFeature.__init__)
    params = list(sig.parameters.keys())
    assert "valueString" in params, "Missing parameter 'valueString'"

def test_feature::simplefeature_has_valueString():
    assert hasattr(feature::SimpleFeature, "valueString")
    descriptor = None
    for klass in feature::SimpleFeature.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)



def test_feature::evidencecode_is_not_abstract():
    assert not inspect.isabstract(feature::EvidenceCode)


def test_feature::evidencecode_constructor_exists():
    assert callable(feature::EvidenceCode.__init__)


def test_feature::evidencecode_constructor_args():
    sig = inspect.signature(feature::EvidenceCode.__init__)
    params = list(sig.parameters.keys())



def test_feature::simpleontologyterm_is_not_abstract():
    assert not inspect.isabstract(feature::SimpleOntologyTerm)


def test_feature::simpleontologyterm_constructor_exists():
    assert callable(feature::SimpleOntologyTerm.__init__)


def test_feature::simpleontologyterm_constructor_args():
    sig = inspect.signature(feature::SimpleOntologyTerm.__init__)
    params = list(sig.parameters.keys())



def test_feature::value_is_not_abstract():
    assert not inspect.isabstract(feature::Value)


def test_feature::value_constructor_exists():
    assert callable(feature::Value.__init__)


def test_feature::value_constructor_args():
    sig = inspect.signature(feature::Value.__init__)
    params = list(sig.parameters.keys())



def test_feature::simpleidentifier_is_not_abstract():
    assert not inspect.isabstract(feature::SimpleIdentifier)


def test_feature::simpleidentifier_constructor_exists():
    assert callable(feature::SimpleIdentifier.__init__)


def test_feature::simpleidentifier_constructor_args():
    sig = inspect.signature(feature::SimpleIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_simplefeature_is_not_abstract():
    assert not inspect.isabstract(SimpleFeature)


def test_simplefeature_constructor_exists():
    assert callable(SimpleFeature.__init__)


def test_simplefeature_constructor_args():
    sig = inspect.signature(SimpleFeature.__init__)
    params = list(sig.parameters.keys())



def test_feature::feature_is_not_abstract():
    assert not inspect.isabstract(feature::Feature)


def test_feature::feature_constructor_exists():
    assert callable(feature::Feature.__init__)


def test_feature::feature_constructor_args():
    sig = inspect.signature(feature::Feature.__init__)
    params = list(sig.parameters.keys())



def test_feature::featureset_is_not_abstract():
    assert not inspect.isabstract(feature::FeatureSet)


def test_feature::featureset_constructor_exists():
    assert callable(feature::FeatureSet.__init__)


def test_feature::featureset_constructor_args():
    sig = inspect.signature(feature::FeatureSet.__init__)
    params = list(sig.parameters.keys())



def test_feature::annotatedsimplefeature_is_not_abstract():
    assert not inspect.isabstract(feature::AnnotatedSimpleFeature)


def test_feature::annotatedsimplefeature_constructor_exists():
    assert callable(feature::AnnotatedSimpleFeature.__init__)


def test_feature::annotatedsimplefeature_constructor_args():
    sig = inspect.signature(feature::AnnotatedSimpleFeature.__init__)
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
SimpleIdentifier_strategy = st.builds(
    SimpleIdentifier,
)
feature::SimpleFeature_strategy = st.builds(
    feature::SimpleFeature,
    valueString=
        safe_text
)
feature::EvidenceCode_strategy = st.builds(
    feature::EvidenceCode,
)
feature::SimpleOntologyTerm_strategy = st.builds(
    feature::SimpleOntologyTerm,
)
feature::Value_strategy = st.builds(
    feature::Value,
)
feature::SimpleIdentifier_strategy = st.builds(
    feature::SimpleIdentifier,
)
SimpleFeature_strategy = st.builds(
    SimpleFeature,
)
feature::Feature_strategy = st.builds(
    feature::Feature,
)
feature::FeatureSet_strategy = st.builds(
    feature::FeatureSet,
)
feature::AnnotatedSimpleFeature_strategy = st.builds(
    feature::AnnotatedSimpleFeature,
)

@given(instance=SimpleIdentifier_strategy)
@settings(max_examples=50)
def test_simpleidentifier_instantiation(instance):
    assert isinstance(instance, SimpleIdentifier)

@given(instance=feature::SimpleFeature_strategy)
@settings(max_examples=50)
def test_feature::simplefeature_instantiation(instance):
    assert isinstance(instance, feature::SimpleFeature)

@given(instance=feature::SimpleFeature_strategy)
def test_feature::simplefeature_valueString_type(instance):
    assert isinstance(instance.valueString, str)


@given(instance=feature::SimpleFeature_strategy)
def test_feature::simplefeature_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original

@given(instance=feature::EvidenceCode_strategy)
@settings(max_examples=50)
def test_feature::evidencecode_instantiation(instance):
    assert isinstance(instance, feature::EvidenceCode)

@given(instance=feature::SimpleOntologyTerm_strategy)
@settings(max_examples=50)
def test_feature::simpleontologyterm_instantiation(instance):
    assert isinstance(instance, feature::SimpleOntologyTerm)

@given(instance=feature::Value_strategy)
@settings(max_examples=50)
def test_feature::value_instantiation(instance):
    assert isinstance(instance, feature::Value)

@given(instance=feature::SimpleIdentifier_strategy)
@settings(max_examples=50)
def test_feature::simpleidentifier_instantiation(instance):
    assert isinstance(instance, feature::SimpleIdentifier)

@given(instance=SimpleFeature_strategy)
@settings(max_examples=50)
def test_simplefeature_instantiation(instance):
    assert isinstance(instance, SimpleFeature)

@given(instance=feature::Feature_strategy)
@settings(max_examples=50)
def test_feature::feature_instantiation(instance):
    assert isinstance(instance, feature::Feature)

@given(instance=feature::FeatureSet_strategy)
@settings(max_examples=50)
def test_feature::featureset_instantiation(instance):
    assert isinstance(instance, feature::FeatureSet)

@given(instance=feature::AnnotatedSimpleFeature_strategy)
@settings(max_examples=50)
def test_feature::annotatedsimplefeature_instantiation(instance):
    assert isinstance(instance, feature::AnnotatedSimpleFeature)
