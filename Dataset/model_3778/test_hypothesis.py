import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    features_Feature,
    features_Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_features_feature_is_not_abstract():
    assert not inspect.isabstract(features_Feature)


def test_features_feature_constructor_exists():
    assert callable(features_Feature.__init__)


def test_features_feature_constructor_args():
    sig = inspect.signature(features_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_features_feature_has_nome():
    assert hasattr(features_Feature, "nome")
    descriptor = None
    for klass in features_Feature.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)

def test_features_feature_has_mandatory():
    assert hasattr(features_Feature, "mandatory")
    descriptor = None
    for klass in features_Feature.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_features_root_is_not_abstract():
    assert not inspect.isabstract(features_Root)


def test_features_root_constructor_exists():
    assert callable(features_Root.__init__)


def test_features_root_constructor_args():
    sig = inspect.signature(features_Root.__init__)
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
features_Feature_strategy = st.builds(
    features_Feature,
    nome=
        safe_text,
    mandatory=
        st.booleans()
)
features_Root_strategy = st.builds(
    features_Root,
)

@given(instance=features_Feature_strategy)
@settings(max_examples=50)
def test_features_feature_instantiation(instance):
    assert isinstance(instance, features_Feature)



@given(instance=features_Feature_strategy)
def test_features_feature_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



@given(instance=features_Feature_strategy)
def test_features_feature_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=features_Root_strategy)
@settings(max_examples=50)
def test_features_root_instantiation(instance):
    assert isinstance(instance, features_Root)
