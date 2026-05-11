import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Constraint,
    UML2::IntervalConstraint,
    UML2::InteractionConstraint,
    UML2::Operation,
    UML2::Constraint,
    IntervalConstraint,
    UML2::TimeConstraint,
    UML2::DurationConstraint,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2::IntervalConstraint)


def test_uml2::intervalconstraint_constructor_exists():
    assert callable(UML2::IntervalConstraint.__init__)


def test_uml2::intervalconstraint_constructor_args():
    sig = inspect.signature(UML2::IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2::InteractionConstraint)


def test_uml2::interactionconstraint_constructor_exists():
    assert callable(UML2::InteractionConstraint.__init__)


def test_uml2::interactionconstraint_constructor_args():
    sig = inspect.signature(UML2::InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::operation_is_not_abstract():
    assert not inspect.isabstract(UML2::Operation)


def test_uml2::operation_constructor_exists():
    assert callable(UML2::Operation.__init__)


def test_uml2::operation_constructor_args():
    sig = inspect.signature(UML2::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isQuery" in params, "Missing parameter 'isQuery'"

def test_uml2::operation_has_isQuery():
    assert hasattr(UML2::Operation, "isQuery")
    descriptor = None
    for klass in UML2::Operation.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)



def test_uml2::constraint_is_not_abstract():
    assert not inspect.isabstract(UML2::Constraint)


def test_uml2::constraint_constructor_exists():
    assert callable(UML2::Constraint.__init__)


def test_uml2::constraint_constructor_args():
    sig = inspect.signature(UML2::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(IntervalConstraint)


def test_intervalconstraint_constructor_exists():
    assert callable(IntervalConstraint.__init__)


def test_intervalconstraint_constructor_args():
    sig = inspect.signature(IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::timeconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeConstraint)


def test_uml2::timeconstraint_constructor_exists():
    assert callable(UML2::TimeConstraint.__init__)


def test_uml2::timeconstraint_constructor_args():
    sig = inspect.signature(UML2::TimeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::durationconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2::DurationConstraint)


def test_uml2::durationconstraint_constructor_exists():
    assert callable(UML2::DurationConstraint.__init__)


def test_uml2::durationconstraint_constructor_args():
    sig = inspect.signature(UML2::DurationConstraint.__init__)
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
Constraint_strategy = st.builds(
    Constraint,
)
UML2::IntervalConstraint_strategy = st.builds(
    UML2::IntervalConstraint,
)
UML2::InteractionConstraint_strategy = st.builds(
    UML2::InteractionConstraint,
)
UML2::Operation_strategy = st.builds(
    UML2::Operation,
    isQuery=
        st.booleans()
)
UML2::Constraint_strategy = st.builds(
    UML2::Constraint,
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
UML2::TimeConstraint_strategy = st.builds(
    UML2::TimeConstraint,
)
UML2::DurationConstraint_strategy = st.builds(
    UML2::DurationConstraint,
)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=UML2::IntervalConstraint_strategy)
@settings(max_examples=50)
def test_uml2::intervalconstraint_instantiation(instance):
    assert isinstance(instance, UML2::IntervalConstraint)

@given(instance=UML2::InteractionConstraint_strategy)
@settings(max_examples=50)
def test_uml2::interactionconstraint_instantiation(instance):
    assert isinstance(instance, UML2::InteractionConstraint)

@given(instance=UML2::Operation_strategy)
@settings(max_examples=50)
def test_uml2::operation_instantiation(instance):
    assert isinstance(instance, UML2::Operation)

@given(instance=UML2::Operation_strategy)
def test_uml2::operation_isQuery_type(instance):
    assert isinstance(instance.isQuery, bool)


@given(instance=UML2::Operation_strategy)
def test_uml2::operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=UML2::Constraint_strategy)
@settings(max_examples=50)
def test_uml2::constraint_instantiation(instance):
    assert isinstance(instance, UML2::Constraint)

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=UML2::TimeConstraint_strategy)
@settings(max_examples=50)
def test_uml2::timeconstraint_instantiation(instance):
    assert isinstance(instance, UML2::TimeConstraint)

@given(instance=UML2::DurationConstraint_strategy)
@settings(max_examples=50)
def test_uml2::durationconstraint_instantiation(instance):
    assert isinstance(instance, UML2::DurationConstraint)
