import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ChangingOverTime::LinkKind,
    TimeStampedElement,
    ChangingOverTime::BindingKind,
    ChangingOverTime::Entity,
    ChangingOverTime::NodeKind,
    ChangingOverTime::Tree,
    ChangingOverTime::TimeStampedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_changingovertime::linkkind_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime::LinkKind)


def test_changingovertime::linkkind_constructor_exists():
    assert callable(ChangingOverTime::LinkKind.__init__)


def test_changingovertime::linkkind_constructor_args():
    sig = inspect.signature(ChangingOverTime::LinkKind.__init__)
    params = list(sig.parameters.keys())



def test_timestampedelement_is_not_abstract():
    assert not inspect.isabstract(TimeStampedElement)


def test_timestampedelement_constructor_exists():
    assert callable(TimeStampedElement.__init__)


def test_timestampedelement_constructor_args():
    sig = inspect.signature(TimeStampedElement.__init__)
    params = list(sig.parameters.keys())



def test_changingovertime::bindingkind_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime::BindingKind)


def test_changingovertime::bindingkind_constructor_exists():
    assert callable(ChangingOverTime::BindingKind.__init__)


def test_changingovertime::bindingkind_constructor_args():
    sig = inspect.signature(ChangingOverTime::BindingKind.__init__)
    params = list(sig.parameters.keys())



def test_changingovertime::entity_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime::Entity)


def test_changingovertime::entity_constructor_exists():
    assert callable(ChangingOverTime::Entity.__init__)


def test_changingovertime::entity_constructor_args():
    sig = inspect.signature(ChangingOverTime::Entity.__init__)
    params = list(sig.parameters.keys())



def test_changingovertime::nodekind_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime::NodeKind)


def test_changingovertime::nodekind_constructor_exists():
    assert callable(ChangingOverTime::NodeKind.__init__)


def test_changingovertime::nodekind_constructor_args():
    sig = inspect.signature(ChangingOverTime::NodeKind.__init__)
    params = list(sig.parameters.keys())



def test_changingovertime::tree_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime::Tree)


def test_changingovertime::tree_constructor_exists():
    assert callable(ChangingOverTime::Tree.__init__)


def test_changingovertime::tree_constructor_args():
    sig = inspect.signature(ChangingOverTime::Tree.__init__)
    params = list(sig.parameters.keys())



def test_changingovertime::timestampedelement_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime::TimeStampedElement)


def test_changingovertime::timestampedelement_constructor_exists():
    assert callable(ChangingOverTime::TimeStampedElement.__init__)


def test_changingovertime::timestampedelement_constructor_args():
    sig = inspect.signature(ChangingOverTime::TimeStampedElement.__init__)
    params = list(sig.parameters.keys())
    assert "expirationDate" in params, "Missing parameter 'expirationDate'"
    assert "effectiveDate" in params, "Missing parameter 'effectiveDate'"

def test_changingovertime::timestampedelement_has_expirationDate():
    assert hasattr(ChangingOverTime::TimeStampedElement, "expirationDate")
    descriptor = None
    for klass in ChangingOverTime::TimeStampedElement.__mro__:
        if "expirationDate" in klass.__dict__:
            descriptor = klass.__dict__["expirationDate"]
            break
    assert isinstance(descriptor, property)

def test_changingovertime::timestampedelement_has_effectiveDate():
    assert hasattr(ChangingOverTime::TimeStampedElement, "effectiveDate")
    descriptor = None
    for klass in ChangingOverTime::TimeStampedElement.__mro__:
        if "effectiveDate" in klass.__dict__:
            descriptor = klass.__dict__["effectiveDate"]
            break
    assert isinstance(descriptor, property)


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
ChangingOverTime::LinkKind_strategy = st.builds(
    ChangingOverTime::LinkKind,
)
TimeStampedElement_strategy = st.builds(
    TimeStampedElement,
)
ChangingOverTime::BindingKind_strategy = st.builds(
    ChangingOverTime::BindingKind,
)
ChangingOverTime::Entity_strategy = st.builds(
    ChangingOverTime::Entity,
)
ChangingOverTime::NodeKind_strategy = st.builds(
    ChangingOverTime::NodeKind,
)
ChangingOverTime::Tree_strategy = st.builds(
    ChangingOverTime::Tree,
)
ChangingOverTime::TimeStampedElement_strategy = st.builds(
    ChangingOverTime::TimeStampedElement,
    expirationDate=
        st.dates(),
    effectiveDate=
        st.dates()
)

@given(instance=ChangingOverTime::LinkKind_strategy)
@settings(max_examples=50)
def test_changingovertime::linkkind_instantiation(instance):
    assert isinstance(instance, ChangingOverTime::LinkKind)

@given(instance=TimeStampedElement_strategy)
@settings(max_examples=50)
def test_timestampedelement_instantiation(instance):
    assert isinstance(instance, TimeStampedElement)

@given(instance=ChangingOverTime::BindingKind_strategy)
@settings(max_examples=50)
def test_changingovertime::bindingkind_instantiation(instance):
    assert isinstance(instance, ChangingOverTime::BindingKind)

@given(instance=ChangingOverTime::Entity_strategy)
@settings(max_examples=50)
def test_changingovertime::entity_instantiation(instance):
    assert isinstance(instance, ChangingOverTime::Entity)

@given(instance=ChangingOverTime::NodeKind_strategy)
@settings(max_examples=50)
def test_changingovertime::nodekind_instantiation(instance):
    assert isinstance(instance, ChangingOverTime::NodeKind)

@given(instance=ChangingOverTime::Tree_strategy)
@settings(max_examples=50)
def test_changingovertime::tree_instantiation(instance):
    assert isinstance(instance, ChangingOverTime::Tree)

@given(instance=ChangingOverTime::TimeStampedElement_strategy)
@settings(max_examples=50)
def test_changingovertime::timestampedelement_instantiation(instance):
    assert isinstance(instance, ChangingOverTime::TimeStampedElement)

@given(instance=ChangingOverTime::TimeStampedElement_strategy)
def test_changingovertime::timestampedelement_expirationDate_type(instance):
    assert isinstance(instance.expirationDate, date)


@given(instance=ChangingOverTime::TimeStampedElement_strategy)
def test_changingovertime::timestampedelement_expirationDate_setter(instance):
    original = instance.expirationDate
    instance.expirationDate = original
    assert instance.expirationDate == original

@given(instance=ChangingOverTime::TimeStampedElement_strategy)
def test_changingovertime::timestampedelement_effectiveDate_type(instance):
    assert isinstance(instance.effectiveDate, date)


@given(instance=ChangingOverTime::TimeStampedElement_strategy)
def test_changingovertime::timestampedelement_effectiveDate_setter(instance):
    original = instance.effectiveDate
    instance.effectiveDate = original
    assert instance.effectiveDate == original
