import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ChangingOverTime_LinkKind,
    TimeStampedElement,
    ChangingOverTime_BindingKind,
    ChangingOverTime_Entity,
    ChangingOverTime_NodeKind,
    ChangingOverTime_Tree,
    ChangingOverTime_TimeStampedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_changingovertime_linkkind_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime_LinkKind)


def test_changingovertime_linkkind_constructor_exists():
    assert callable(ChangingOverTime_LinkKind.__init__)


def test_changingovertime_linkkind_constructor_args():
    sig = inspect.signature(ChangingOverTime_LinkKind.__init__)
    params = list(sig.parameters.keys())



def test_timestampedelement_is_not_abstract():
    assert not inspect.isabstract(TimeStampedElement)


def test_timestampedelement_constructor_exists():
    assert callable(TimeStampedElement.__init__)


def test_timestampedelement_constructor_args():
    sig = inspect.signature(TimeStampedElement.__init__)
    params = list(sig.parameters.keys())



def test_changingovertime_bindingkind_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime_BindingKind)


def test_changingovertime_bindingkind_constructor_exists():
    assert callable(ChangingOverTime_BindingKind.__init__)


def test_changingovertime_bindingkind_constructor_args():
    sig = inspect.signature(ChangingOverTime_BindingKind.__init__)
    params = list(sig.parameters.keys())



def test_changingovertime_entity_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime_Entity)


def test_changingovertime_entity_constructor_exists():
    assert callable(ChangingOverTime_Entity.__init__)


def test_changingovertime_entity_constructor_args():
    sig = inspect.signature(ChangingOverTime_Entity.__init__)
    params = list(sig.parameters.keys())



def test_changingovertime_nodekind_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime_NodeKind)


def test_changingovertime_nodekind_constructor_exists():
    assert callable(ChangingOverTime_NodeKind.__init__)


def test_changingovertime_nodekind_constructor_args():
    sig = inspect.signature(ChangingOverTime_NodeKind.__init__)
    params = list(sig.parameters.keys())



def test_changingovertime_tree_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime_Tree)


def test_changingovertime_tree_constructor_exists():
    assert callable(ChangingOverTime_Tree.__init__)


def test_changingovertime_tree_constructor_args():
    sig = inspect.signature(ChangingOverTime_Tree.__init__)
    params = list(sig.parameters.keys())



def test_changingovertime_timestampedelement_is_not_abstract():
    assert not inspect.isabstract(ChangingOverTime_TimeStampedElement)


def test_changingovertime_timestampedelement_constructor_exists():
    assert callable(ChangingOverTime_TimeStampedElement.__init__)


def test_changingovertime_timestampedelement_constructor_args():
    sig = inspect.signature(ChangingOverTime_TimeStampedElement.__init__)
    params = list(sig.parameters.keys())
    assert "effectiveDate" in params, "Missing parameter 'effectiveDate'"
    assert "expirationDate" in params, "Missing parameter 'expirationDate'"

def test_changingovertime_timestampedelement_has_effectiveDate():
    assert hasattr(ChangingOverTime_TimeStampedElement, "effectiveDate")
    descriptor = None
    for klass in ChangingOverTime_TimeStampedElement.__mro__:
        if "effectiveDate" in klass.__dict__:
            descriptor = klass.__dict__["effectiveDate"]
            break
    assert isinstance(descriptor, property)

def test_changingovertime_timestampedelement_has_expirationDate():
    assert hasattr(ChangingOverTime_TimeStampedElement, "expirationDate")
    descriptor = None
    for klass in ChangingOverTime_TimeStampedElement.__mro__:
        if "expirationDate" in klass.__dict__:
            descriptor = klass.__dict__["expirationDate"]
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
ChangingOverTime_LinkKind_strategy = st.builds(
    ChangingOverTime_LinkKind,
)
TimeStampedElement_strategy = st.builds(
    TimeStampedElement,
)
ChangingOverTime_BindingKind_strategy = st.builds(
    ChangingOverTime_BindingKind,
)
ChangingOverTime_Entity_strategy = st.builds(
    ChangingOverTime_Entity,
)
ChangingOverTime_NodeKind_strategy = st.builds(
    ChangingOverTime_NodeKind,
)
ChangingOverTime_Tree_strategy = st.builds(
    ChangingOverTime_Tree,
)
ChangingOverTime_TimeStampedElement_strategy = st.builds(
    ChangingOverTime_TimeStampedElement,
    effectiveDate=
        st.dates(),
    expirationDate=
        st.dates()
)

@given(instance=ChangingOverTime_LinkKind_strategy)
@settings(max_examples=50)
def test_changingovertime_linkkind_instantiation(instance):
    assert isinstance(instance, ChangingOverTime_LinkKind)

@given(instance=TimeStampedElement_strategy)
@settings(max_examples=50)
def test_timestampedelement_instantiation(instance):
    assert isinstance(instance, TimeStampedElement)

@given(instance=ChangingOverTime_BindingKind_strategy)
@settings(max_examples=50)
def test_changingovertime_bindingkind_instantiation(instance):
    assert isinstance(instance, ChangingOverTime_BindingKind)

@given(instance=ChangingOverTime_Entity_strategy)
@settings(max_examples=50)
def test_changingovertime_entity_instantiation(instance):
    assert isinstance(instance, ChangingOverTime_Entity)

@given(instance=ChangingOverTime_NodeKind_strategy)
@settings(max_examples=50)
def test_changingovertime_nodekind_instantiation(instance):
    assert isinstance(instance, ChangingOverTime_NodeKind)

@given(instance=ChangingOverTime_Tree_strategy)
@settings(max_examples=50)
def test_changingovertime_tree_instantiation(instance):
    assert isinstance(instance, ChangingOverTime_Tree)

@given(instance=ChangingOverTime_TimeStampedElement_strategy)
@settings(max_examples=50)
def test_changingovertime_timestampedelement_instantiation(instance):
    assert isinstance(instance, ChangingOverTime_TimeStampedElement)



@given(instance=ChangingOverTime_TimeStampedElement_strategy)
def test_changingovertime_timestampedelement_effectiveDate_setter(instance):
    original = instance.effectiveDate
    instance.effectiveDate = original
    assert instance.effectiveDate == original



@given(instance=ChangingOverTime_TimeStampedElement_strategy)
def test_changingovertime_timestampedelement_expirationDate_setter(instance):
    original = instance.expirationDate
    instance.expirationDate = original
    assert instance.expirationDate == original
