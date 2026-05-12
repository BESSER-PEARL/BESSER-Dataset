import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Constraint,
    UML2_IntervalConstraint,
    UML2_InteractionConstraint,
    UML2_Operation,
    UML2_Constraint,
    IntervalConstraint,
    UML2_TimeConstraint,
    UML2_DurationConstraint,
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



def test_uml2_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2_IntervalConstraint)


def test_uml2_intervalconstraint_constructor_exists():
    assert callable(UML2_IntervalConstraint.__init__)


def test_uml2_intervalconstraint_constructor_args():
    sig = inspect.signature(UML2_IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2_InteractionConstraint)


def test_uml2_interactionconstraint_constructor_exists():
    assert callable(UML2_InteractionConstraint.__init__)


def test_uml2_interactionconstraint_constructor_args():
    sig = inspect.signature(UML2_InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2_operation_is_not_abstract():
    assert not inspect.isabstract(UML2_Operation)


def test_uml2_operation_constructor_exists():
    assert callable(UML2_Operation.__init__)


def test_uml2_operation_constructor_args():
    sig = inspect.signature(UML2_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isQuery" in params, "Missing parameter 'isQuery'"

def test_uml2_operation_has_isQuery():
    assert hasattr(UML2_Operation, "isQuery")
    descriptor = None
    for klass in UML2_Operation.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)



def test_uml2_constraint_is_not_abstract():
    assert not inspect.isabstract(UML2_Constraint)


def test_uml2_constraint_constructor_exists():
    assert callable(UML2_Constraint.__init__)


def test_uml2_constraint_constructor_args():
    sig = inspect.signature(UML2_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(IntervalConstraint)


def test_intervalconstraint_constructor_exists():
    assert callable(IntervalConstraint.__init__)


def test_intervalconstraint_constructor_args():
    sig = inspect.signature(IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2_timeconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2_TimeConstraint)


def test_uml2_timeconstraint_constructor_exists():
    assert callable(UML2_TimeConstraint.__init__)


def test_uml2_timeconstraint_constructor_args():
    sig = inspect.signature(UML2_TimeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2_durationconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2_DurationConstraint)


def test_uml2_durationconstraint_constructor_exists():
    assert callable(UML2_DurationConstraint.__init__)


def test_uml2_durationconstraint_constructor_args():
    sig = inspect.signature(UML2_DurationConstraint.__init__)
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
UML2_IntervalConstraint_strategy = st.builds(
    UML2_IntervalConstraint,
)
UML2_InteractionConstraint_strategy = st.builds(
    UML2_InteractionConstraint,
)
UML2_Operation_strategy = st.builds(
    UML2_Operation,
    isQuery=
        st.booleans()
)
UML2_Constraint_strategy = st.builds(
    UML2_Constraint,
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
UML2_TimeConstraint_strategy = st.builds(
    UML2_TimeConstraint,
)
UML2_DurationConstraint_strategy = st.builds(
    UML2_DurationConstraint,
)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=UML2_IntervalConstraint_strategy)
@settings(max_examples=50)
def test_uml2_intervalconstraint_instantiation(instance):
    assert isinstance(instance, UML2_IntervalConstraint)

@given(instance=UML2_InteractionConstraint_strategy)
@settings(max_examples=50)
def test_uml2_interactionconstraint_instantiation(instance):
    assert isinstance(instance, UML2_InteractionConstraint)

@given(instance=UML2_Operation_strategy)
@settings(max_examples=50)
def test_uml2_operation_instantiation(instance):
    assert isinstance(instance, UML2_Operation)



@given(instance=UML2_Operation_strategy)
def test_uml2_operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=UML2_Constraint_strategy)
@settings(max_examples=50)
def test_uml2_constraint_instantiation(instance):
    assert isinstance(instance, UML2_Constraint)

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=UML2_TimeConstraint_strategy)
@settings(max_examples=50)
def test_uml2_timeconstraint_instantiation(instance):
    assert isinstance(instance, UML2_TimeConstraint)

@given(instance=UML2_DurationConstraint_strategy)
@settings(max_examples=50)
def test_uml2_durationconstraint_instantiation(instance):
    assert isinstance(instance, UML2_DurationConstraint)
