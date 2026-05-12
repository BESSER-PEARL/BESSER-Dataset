import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SimpleIdentifier,
    feature_SimpleFeature,
    feature_EvidenceCode,
    feature_SimpleOntologyTerm,
    feature_Value,
    feature_SimpleIdentifier,
    SimpleFeature,
    feature_FeatureSet,
    feature_Feature,
    feature_AnnotatedSimpleFeature,
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



def test_feature_simplefeature_is_not_abstract():
    assert not inspect.isabstract(feature_SimpleFeature)


def test_feature_simplefeature_constructor_exists():
    assert callable(feature_SimpleFeature.__init__)


def test_feature_simplefeature_constructor_args():
    sig = inspect.signature(feature_SimpleFeature.__init__)
    params = list(sig.parameters.keys())
    assert "valueString" in params, "Missing parameter 'valueString'"

def test_feature_simplefeature_has_valueString():
    assert hasattr(feature_SimpleFeature, "valueString")
    descriptor = None
    for klass in feature_SimpleFeature.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)



def test_feature_evidencecode_is_not_abstract():
    assert not inspect.isabstract(feature_EvidenceCode)


def test_feature_evidencecode_constructor_exists():
    assert callable(feature_EvidenceCode.__init__)


def test_feature_evidencecode_constructor_args():
    sig = inspect.signature(feature_EvidenceCode.__init__)
    params = list(sig.parameters.keys())



def test_feature_simpleontologyterm_is_not_abstract():
    assert not inspect.isabstract(feature_SimpleOntologyTerm)


def test_feature_simpleontologyterm_constructor_exists():
    assert callable(feature_SimpleOntologyTerm.__init__)


def test_feature_simpleontologyterm_constructor_args():
    sig = inspect.signature(feature_SimpleOntologyTerm.__init__)
    params = list(sig.parameters.keys())



def test_feature_value_is_not_abstract():
    assert not inspect.isabstract(feature_Value)


def test_feature_value_constructor_exists():
    assert callable(feature_Value.__init__)


def test_feature_value_constructor_args():
    sig = inspect.signature(feature_Value.__init__)
    params = list(sig.parameters.keys())



def test_feature_simpleidentifier_is_not_abstract():
    assert not inspect.isabstract(feature_SimpleIdentifier)


def test_feature_simpleidentifier_constructor_exists():
    assert callable(feature_SimpleIdentifier.__init__)


def test_feature_simpleidentifier_constructor_args():
    sig = inspect.signature(feature_SimpleIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_simplefeature_is_not_abstract():
    assert not inspect.isabstract(SimpleFeature)


def test_simplefeature_constructor_exists():
    assert callable(SimpleFeature.__init__)


def test_simplefeature_constructor_args():
    sig = inspect.signature(SimpleFeature.__init__)
    params = list(sig.parameters.keys())



def test_feature_featureset_is_not_abstract():
    assert not inspect.isabstract(feature_FeatureSet)


def test_feature_featureset_constructor_exists():
    assert callable(feature_FeatureSet.__init__)


def test_feature_featureset_constructor_args():
    sig = inspect.signature(feature_FeatureSet.__init__)
    params = list(sig.parameters.keys())



def test_feature_feature_is_not_abstract():
    assert not inspect.isabstract(feature_Feature)


def test_feature_feature_constructor_exists():
    assert callable(feature_Feature.__init__)


def test_feature_feature_constructor_args():
    sig = inspect.signature(feature_Feature.__init__)
    params = list(sig.parameters.keys())



def test_feature_annotatedsimplefeature_is_not_abstract():
    assert not inspect.isabstract(feature_AnnotatedSimpleFeature)


def test_feature_annotatedsimplefeature_constructor_exists():
    assert callable(feature_AnnotatedSimpleFeature.__init__)


def test_feature_annotatedsimplefeature_constructor_args():
    sig = inspect.signature(feature_AnnotatedSimpleFeature.__init__)
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
feature_SimpleFeature_strategy = st.builds(
    feature_SimpleFeature,
    valueString=
        safe_text
)
feature_EvidenceCode_strategy = st.builds(
    feature_EvidenceCode,
)
feature_SimpleOntologyTerm_strategy = st.builds(
    feature_SimpleOntologyTerm,
)
feature_Value_strategy = st.builds(
    feature_Value,
)
feature_SimpleIdentifier_strategy = st.builds(
    feature_SimpleIdentifier,
)
SimpleFeature_strategy = st.builds(
    SimpleFeature,
)
feature_FeatureSet_strategy = st.builds(
    feature_FeatureSet,
)
feature_Feature_strategy = st.builds(
    feature_Feature,
)
feature_AnnotatedSimpleFeature_strategy = st.builds(
    feature_AnnotatedSimpleFeature,
)

@given(instance=SimpleIdentifier_strategy)
@settings(max_examples=50)
def test_simpleidentifier_instantiation(instance):
    assert isinstance(instance, SimpleIdentifier)

@given(instance=feature_SimpleFeature_strategy)
@settings(max_examples=50)
def test_feature_simplefeature_instantiation(instance):
    assert isinstance(instance, feature_SimpleFeature)



@given(instance=feature_SimpleFeature_strategy)
def test_feature_simplefeature_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original

@given(instance=feature_EvidenceCode_strategy)
@settings(max_examples=50)
def test_feature_evidencecode_instantiation(instance):
    assert isinstance(instance, feature_EvidenceCode)

@given(instance=feature_SimpleOntologyTerm_strategy)
@settings(max_examples=50)
def test_feature_simpleontologyterm_instantiation(instance):
    assert isinstance(instance, feature_SimpleOntologyTerm)

@given(instance=feature_Value_strategy)
@settings(max_examples=50)
def test_feature_value_instantiation(instance):
    assert isinstance(instance, feature_Value)

@given(instance=feature_SimpleIdentifier_strategy)
@settings(max_examples=50)
def test_feature_simpleidentifier_instantiation(instance):
    assert isinstance(instance, feature_SimpleIdentifier)

@given(instance=SimpleFeature_strategy)
@settings(max_examples=50)
def test_simplefeature_instantiation(instance):
    assert isinstance(instance, SimpleFeature)

@given(instance=feature_FeatureSet_strategy)
@settings(max_examples=50)
def test_feature_featureset_instantiation(instance):
    assert isinstance(instance, feature_FeatureSet)

@given(instance=feature_Feature_strategy)
@settings(max_examples=50)
def test_feature_feature_instantiation(instance):
    assert isinstance(instance, feature_Feature)

@given(instance=feature_AnnotatedSimpleFeature_strategy)
@settings(max_examples=50)
def test_feature_annotatedsimplefeature_instantiation(instance):
    assert isinstance(instance, feature_AnnotatedSimpleFeature)
