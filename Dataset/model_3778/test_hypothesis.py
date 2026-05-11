import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    features::Feature,
    features::Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_features::feature_is_not_abstract():
    assert not inspect.isabstract(features::Feature)


def test_features::feature_constructor_exists():
    assert callable(features::Feature.__init__)


def test_features::feature_constructor_args():
    sig = inspect.signature(features::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "nome" in params, "Missing parameter 'nome'"

def test_features::feature_has_mandatory():
    assert hasattr(features::Feature, "mandatory")
    descriptor = None
    for klass in features::Feature.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)

def test_features::feature_has_nome():
    assert hasattr(features::Feature, "nome")
    descriptor = None
    for klass in features::Feature.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)



def test_features::root_is_not_abstract():
    assert not inspect.isabstract(features::Root)


def test_features::root_constructor_exists():
    assert callable(features::Root.__init__)


def test_features::root_constructor_args():
    sig = inspect.signature(features::Root.__init__)
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
features::Feature_strategy = st.builds(
    features::Feature,
    mandatory=
        st.booleans(),
    nome=
        safe_text
)
features::Root_strategy = st.builds(
    features::Root,
)

@given(instance=features::Feature_strategy)
@settings(max_examples=50)
def test_features::feature_instantiation(instance):
    assert isinstance(instance, features::Feature)

@given(instance=features::Feature_strategy)
def test_features::feature_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=features::Feature_strategy)
def test_features::feature_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=features::Feature_strategy)
def test_features::feature_nome_type(instance):
    assert isinstance(instance.nome, str)


@given(instance=features::Feature_strategy)
def test_features::feature_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original

@given(instance=features::Root_strategy)
@settings(max_examples=50)
def test_features::root_instantiation(instance):
    assert isinstance(instance, features::Root)
