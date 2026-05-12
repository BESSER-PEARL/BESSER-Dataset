import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Actor,
    UseCase::NamedElement,
    UseCase::BehavioredClassifier,
    UseCase::UseCaseContainer,
    UseCase::Include,
    Extend,
    Include,
    NamedElement,
    UseCase::Association,
    UseCase::UseCase,
    UseCase::Actor,
    UseCase,
    UseCase::Extend,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_actor_is_not_abstract():
    assert not inspect.isabstract(Actor)


def test_actor_constructor_exists():
    assert callable(Actor.__init__)


def test_actor_constructor_args():
    sig = inspect.signature(Actor.__init__)
    params = list(sig.parameters.keys())



def test_usecase::namedelement_is_not_abstract():
    assert not inspect.isabstract(UseCase::NamedElement)


def test_usecase::namedelement_constructor_exists():
    assert callable(UseCase::NamedElement.__init__)


def test_usecase::namedelement_constructor_args():
    sig = inspect.signature(UseCase::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_usecase::namedelement_has_name():
    assert hasattr(UseCase::NamedElement, "name")
    descriptor = None
    for klass in UseCase::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_usecase::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UseCase::BehavioredClassifier)


def test_usecase::behavioredclassifier_constructor_exists():
    assert callable(UseCase::BehavioredClassifier.__init__)


def test_usecase::behavioredclassifier_constructor_args():
    sig = inspect.signature(UseCase::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_usecase::usecasecontainer_is_not_abstract():
    assert not inspect.isabstract(UseCase::UseCaseContainer)


def test_usecase::usecasecontainer_constructor_exists():
    assert callable(UseCase::UseCaseContainer.__init__)


def test_usecase::usecasecontainer_constructor_args():
    sig = inspect.signature(UseCase::UseCaseContainer.__init__)
    params = list(sig.parameters.keys())



def test_usecase::include_is_not_abstract():
    assert not inspect.isabstract(UseCase::Include)


def test_usecase::include_constructor_exists():
    assert callable(UseCase::Include.__init__)


def test_usecase::include_constructor_args():
    sig = inspect.signature(UseCase::Include.__init__)
    params = list(sig.parameters.keys())



def test_extend_is_not_abstract():
    assert not inspect.isabstract(Extend)


def test_extend_constructor_exists():
    assert callable(Extend.__init__)


def test_extend_constructor_args():
    sig = inspect.signature(Extend.__init__)
    params = list(sig.parameters.keys())



def test_include_is_not_abstract():
    assert not inspect.isabstract(Include)


def test_include_constructor_exists():
    assert callable(Include.__init__)


def test_include_constructor_args():
    sig = inspect.signature(Include.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_usecase::association_is_not_abstract():
    assert not inspect.isabstract(UseCase::Association)


def test_usecase::association_constructor_exists():
    assert callable(UseCase::Association.__init__)


def test_usecase::association_constructor_args():
    sig = inspect.signature(UseCase::Association.__init__)
    params = list(sig.parameters.keys())



def test_usecase::usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase::UseCase)


def test_usecase::usecase_constructor_exists():
    assert callable(UseCase::UseCase.__init__)


def test_usecase::usecase_constructor_args():
    sig = inspect.signature(UseCase::UseCase.__init__)
    params = list(sig.parameters.keys())



def test_usecase::actor_is_not_abstract():
    assert not inspect.isabstract(UseCase::Actor)


def test_usecase::actor_constructor_exists():
    assert callable(UseCase::Actor.__init__)


def test_usecase::actor_constructor_args():
    sig = inspect.signature(UseCase::Actor.__init__)
    params = list(sig.parameters.keys())



def test_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase)


def test_usecase_constructor_exists():
    assert callable(UseCase.__init__)


def test_usecase_constructor_args():
    sig = inspect.signature(UseCase.__init__)
    params = list(sig.parameters.keys())



def test_usecase::extend_is_not_abstract():
    assert not inspect.isabstract(UseCase::Extend)


def test_usecase::extend_constructor_exists():
    assert callable(UseCase::Extend.__init__)


def test_usecase::extend_constructor_args():
    sig = inspect.signature(UseCase::Extend.__init__)
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
Actor_strategy = st.builds(
    Actor,
)
UseCase::NamedElement_strategy = st.builds(
    UseCase::NamedElement,
    name=
        safe_text
)
UseCase::BehavioredClassifier_strategy = st.builds(
    UseCase::BehavioredClassifier,
)
UseCase::UseCaseContainer_strategy = st.builds(
    UseCase::UseCaseContainer,
)
UseCase::Include_strategy = st.builds(
    UseCase::Include,
)
Extend_strategy = st.builds(
    Extend,
)
Include_strategy = st.builds(
    Include,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
UseCase::Association_strategy = st.builds(
    UseCase::Association,
)
UseCase::UseCase_strategy = st.builds(
    UseCase::UseCase,
)
UseCase::Actor_strategy = st.builds(
    UseCase::Actor,
)
UseCase_strategy = st.builds(
    UseCase,
)
UseCase::Extend_strategy = st.builds(
    UseCase::Extend,
)

@given(instance=Actor_strategy)
@settings(max_examples=50)
def test_actor_instantiation(instance):
    assert isinstance(instance, Actor)

@given(instance=UseCase::NamedElement_strategy)
@settings(max_examples=50)
def test_usecase::namedelement_instantiation(instance):
    assert isinstance(instance, UseCase::NamedElement)

@given(instance=UseCase::NamedElement_strategy)
def test_usecase::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UseCase::NamedElement_strategy)
def test_usecase::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UseCase::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_usecase::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UseCase::BehavioredClassifier)

@given(instance=UseCase::UseCaseContainer_strategy)
@settings(max_examples=50)
def test_usecase::usecasecontainer_instantiation(instance):
    assert isinstance(instance, UseCase::UseCaseContainer)

@given(instance=UseCase::Include_strategy)
@settings(max_examples=50)
def test_usecase::include_instantiation(instance):
    assert isinstance(instance, UseCase::Include)

@given(instance=Extend_strategy)
@settings(max_examples=50)
def test_extend_instantiation(instance):
    assert isinstance(instance, Extend)

@given(instance=Include_strategy)
@settings(max_examples=50)
def test_include_instantiation(instance):
    assert isinstance(instance, Include)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=UseCase::Association_strategy)
@settings(max_examples=50)
def test_usecase::association_instantiation(instance):
    assert isinstance(instance, UseCase::Association)

@given(instance=UseCase::UseCase_strategy)
@settings(max_examples=50)
def test_usecase::usecase_instantiation(instance):
    assert isinstance(instance, UseCase::UseCase)

@given(instance=UseCase::Actor_strategy)
@settings(max_examples=50)
def test_usecase::actor_instantiation(instance):
    assert isinstance(instance, UseCase::Actor)

@given(instance=UseCase_strategy)
@settings(max_examples=50)
def test_usecase_instantiation(instance):
    assert isinstance(instance, UseCase)

@given(instance=UseCase::Extend_strategy)
@settings(max_examples=50)
def test_usecase::extend_instantiation(instance):
    assert isinstance(instance, UseCase::Extend)
