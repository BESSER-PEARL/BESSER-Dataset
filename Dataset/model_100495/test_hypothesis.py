import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TimeEventRule,
    umlTransition::AbsoluteTimeEventRule,
    umlTransition::RelativeTimeEventRule,
    umlTransition::TransitionRule,
    umlTransition::NamedElement,
    EventRule,
    umlTransition::AnyReceiveEventRule,
    umlTransition::TimeEventRule,
    umlTransition::ChangeEventRule,
    umlTransition::CallOrSignalEventRule,
    umlTransition::EffectRule,
    umlTransition::GuardRule,
    umlTransition::EventRule,
    BehaviorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_timeeventrule_is_not_abstract():
    assert not inspect.isabstract(TimeEventRule)


def test_timeeventrule_constructor_exists():
    assert callable(TimeEventRule.__init__)


def test_timeeventrule_constructor_args():
    sig = inspect.signature(TimeEventRule.__init__)
    params = list(sig.parameters.keys())



def test_umltransition::absolutetimeeventrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition::AbsoluteTimeEventRule)


def test_umltransition::absolutetimeeventrule_constructor_exists():
    assert callable(umlTransition::AbsoluteTimeEventRule.__init__)


def test_umltransition::absolutetimeeventrule_constructor_args():
    sig = inspect.signature(umlTransition::AbsoluteTimeEventRule.__init__)
    params = list(sig.parameters.keys())



def test_umltransition::relativetimeeventrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition::RelativeTimeEventRule)


def test_umltransition::relativetimeeventrule_constructor_exists():
    assert callable(umlTransition::RelativeTimeEventRule.__init__)


def test_umltransition::relativetimeeventrule_constructor_args():
    sig = inspect.signature(umlTransition::RelativeTimeEventRule.__init__)
    params = list(sig.parameters.keys())



def test_umltransition::transitionrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition::TransitionRule)


def test_umltransition::transitionrule_constructor_exists():
    assert callable(umlTransition::TransitionRule.__init__)


def test_umltransition::transitionrule_constructor_args():
    sig = inspect.signature(umlTransition::TransitionRule.__init__)
    params = list(sig.parameters.keys())



def test_umltransition::namedelement_is_not_abstract():
    assert not inspect.isabstract(umlTransition::NamedElement)


def test_umltransition::namedelement_constructor_exists():
    assert callable(umlTransition::NamedElement.__init__)


def test_umltransition::namedelement_constructor_args():
    sig = inspect.signature(umlTransition::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_eventrule_is_not_abstract():
    assert not inspect.isabstract(EventRule)


def test_eventrule_constructor_exists():
    assert callable(EventRule.__init__)


def test_eventrule_constructor_args():
    sig = inspect.signature(EventRule.__init__)
    params = list(sig.parameters.keys())



def test_umltransition::anyreceiveeventrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition::AnyReceiveEventRule)


def test_umltransition::anyreceiveeventrule_constructor_exists():
    assert callable(umlTransition::AnyReceiveEventRule.__init__)


def test_umltransition::anyreceiveeventrule_constructor_args():
    sig = inspect.signature(umlTransition::AnyReceiveEventRule.__init__)
    params = list(sig.parameters.keys())
    assert "isAReceiveEvent" in params, "Missing parameter 'isAReceiveEvent'"

def test_umltransition::anyreceiveeventrule_has_isAReceiveEvent():
    assert hasattr(umlTransition::AnyReceiveEventRule, "isAReceiveEvent")
    descriptor = None
    for klass in umlTransition::AnyReceiveEventRule.__mro__:
        if "isAReceiveEvent" in klass.__dict__:
            descriptor = klass.__dict__["isAReceiveEvent"]
            break
    assert isinstance(descriptor, property)



def test_umltransition::timeeventrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition::TimeEventRule)


def test_umltransition::timeeventrule_constructor_exists():
    assert callable(umlTransition::TimeEventRule.__init__)


def test_umltransition::timeeventrule_constructor_args():
    sig = inspect.signature(umlTransition::TimeEventRule.__init__)
    params = list(sig.parameters.keys())
    assert "expr" in params, "Missing parameter 'expr'"

def test_umltransition::timeeventrule_has_expr():
    assert hasattr(umlTransition::TimeEventRule, "expr")
    descriptor = None
    for klass in umlTransition::TimeEventRule.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)



def test_umltransition::changeeventrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition::ChangeEventRule)


def test_umltransition::changeeventrule_constructor_exists():
    assert callable(umlTransition::ChangeEventRule.__init__)


def test_umltransition::changeeventrule_constructor_args():
    sig = inspect.signature(umlTransition::ChangeEventRule.__init__)
    params = list(sig.parameters.keys())
    assert "exp" in params, "Missing parameter 'exp'"

def test_umltransition::changeeventrule_has_exp():
    assert hasattr(umlTransition::ChangeEventRule, "exp")
    descriptor = None
    for klass in umlTransition::ChangeEventRule.__mro__:
        if "exp" in klass.__dict__:
            descriptor = klass.__dict__["exp"]
            break
    assert isinstance(descriptor, property)



def test_umltransition::callorsignaleventrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition::CallOrSignalEventRule)


def test_umltransition::callorsignaleventrule_constructor_exists():
    assert callable(umlTransition::CallOrSignalEventRule.__init__)


def test_umltransition::callorsignaleventrule_constructor_args():
    sig = inspect.signature(umlTransition::CallOrSignalEventRule.__init__)
    params = list(sig.parameters.keys())



def test_umltransition::effectrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition::EffectRule)


def test_umltransition::effectrule_constructor_exists():
    assert callable(umlTransition::EffectRule.__init__)


def test_umltransition::effectrule_constructor_args():
    sig = inspect.signature(umlTransition::EffectRule.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "behaviorName" in params, "Missing parameter 'behaviorName'"

def test_umltransition::effectrule_has_kind():
    assert hasattr(umlTransition::EffectRule, "kind")
    descriptor = None
    for klass in umlTransition::EffectRule.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_umltransition::effectrule_has_behaviorName():
    assert hasattr(umlTransition::EffectRule, "behaviorName")
    descriptor = None
    for klass in umlTransition::EffectRule.__mro__:
        if "behaviorName" in klass.__dict__:
            descriptor = klass.__dict__["behaviorName"]
            break
    assert isinstance(descriptor, property)



def test_umltransition::guardrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition::GuardRule)


def test_umltransition::guardrule_constructor_exists():
    assert callable(umlTransition::GuardRule.__init__)


def test_umltransition::guardrule_constructor_args():
    sig = inspect.signature(umlTransition::GuardRule.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"

def test_umltransition::guardrule_has_constraint():
    assert hasattr(umlTransition::GuardRule, "constraint")
    descriptor = None
    for klass in umlTransition::GuardRule.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)



def test_umltransition::eventrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition::EventRule)


def test_umltransition::eventrule_constructor_exists():
    assert callable(umlTransition::EventRule.__init__)


def test_umltransition::eventrule_constructor_args():
    sig = inspect.signature(umlTransition::EventRule.__init__)
    params = list(sig.parameters.keys())

def test_behaviorkind_exists():
    # Check that the Enumeration exists
    assert BehaviorKind is not None

def test_behaviorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BehaviorKind]
    expected_literals = [
        "OPAQUE_BEHAVIOR",
        "ACTIVITY",
        "STATE_MACHINE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BehaviorKind"


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
TimeEventRule_strategy = st.builds(
    TimeEventRule,
)
umlTransition::AbsoluteTimeEventRule_strategy = st.builds(
    umlTransition::AbsoluteTimeEventRule,
)
umlTransition::RelativeTimeEventRule_strategy = st.builds(
    umlTransition::RelativeTimeEventRule,
)
umlTransition::TransitionRule_strategy = st.builds(
    umlTransition::TransitionRule,
)
umlTransition::NamedElement_strategy = st.builds(
    umlTransition::NamedElement,
)
EventRule_strategy = st.builds(
    EventRule,
)
umlTransition::AnyReceiveEventRule_strategy = st.builds(
    umlTransition::AnyReceiveEventRule,
    isAReceiveEvent=
        safe_text
)
umlTransition::TimeEventRule_strategy = st.builds(
    umlTransition::TimeEventRule,
    expr=
        safe_text
)
umlTransition::ChangeEventRule_strategy = st.builds(
    umlTransition::ChangeEventRule,
    exp=
        safe_text
)
umlTransition::CallOrSignalEventRule_strategy = st.builds(
    umlTransition::CallOrSignalEventRule,
)
umlTransition::EffectRule_strategy = st.builds(
    umlTransition::EffectRule,
    kind=
        safe_text,
    behaviorName=
        safe_text
)
umlTransition::GuardRule_strategy = st.builds(
    umlTransition::GuardRule,
    constraint=
        safe_text
)
umlTransition::EventRule_strategy = st.builds(
    umlTransition::EventRule,
)

@given(instance=TimeEventRule_strategy)
@settings(max_examples=50)
def test_timeeventrule_instantiation(instance):
    assert isinstance(instance, TimeEventRule)

@given(instance=umlTransition::AbsoluteTimeEventRule_strategy)
@settings(max_examples=50)
def test_umltransition::absolutetimeeventrule_instantiation(instance):
    assert isinstance(instance, umlTransition::AbsoluteTimeEventRule)

@given(instance=umlTransition::RelativeTimeEventRule_strategy)
@settings(max_examples=50)
def test_umltransition::relativetimeeventrule_instantiation(instance):
    assert isinstance(instance, umlTransition::RelativeTimeEventRule)

@given(instance=umlTransition::TransitionRule_strategy)
@settings(max_examples=50)
def test_umltransition::transitionrule_instantiation(instance):
    assert isinstance(instance, umlTransition::TransitionRule)

@given(instance=umlTransition::NamedElement_strategy)
@settings(max_examples=50)
def test_umltransition::namedelement_instantiation(instance):
    assert isinstance(instance, umlTransition::NamedElement)

@given(instance=EventRule_strategy)
@settings(max_examples=50)
def test_eventrule_instantiation(instance):
    assert isinstance(instance, EventRule)

@given(instance=umlTransition::AnyReceiveEventRule_strategy)
@settings(max_examples=50)
def test_umltransition::anyreceiveeventrule_instantiation(instance):
    assert isinstance(instance, umlTransition::AnyReceiveEventRule)

@given(instance=umlTransition::AnyReceiveEventRule_strategy)
def test_umltransition::anyreceiveeventrule_isAReceiveEvent_type(instance):
    assert isinstance(instance.isAReceiveEvent, str)


@given(instance=umlTransition::AnyReceiveEventRule_strategy)
def test_umltransition::anyreceiveeventrule_isAReceiveEvent_setter(instance):
    original = instance.isAReceiveEvent
    instance.isAReceiveEvent = original
    assert instance.isAReceiveEvent == original

@given(instance=umlTransition::TimeEventRule_strategy)
@settings(max_examples=50)
def test_umltransition::timeeventrule_instantiation(instance):
    assert isinstance(instance, umlTransition::TimeEventRule)

@given(instance=umlTransition::TimeEventRule_strategy)
def test_umltransition::timeeventrule_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=umlTransition::TimeEventRule_strategy)
def test_umltransition::timeeventrule_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=umlTransition::ChangeEventRule_strategy)
@settings(max_examples=50)
def test_umltransition::changeeventrule_instantiation(instance):
    assert isinstance(instance, umlTransition::ChangeEventRule)

@given(instance=umlTransition::ChangeEventRule_strategy)
def test_umltransition::changeeventrule_exp_type(instance):
    assert isinstance(instance.exp, str)


@given(instance=umlTransition::ChangeEventRule_strategy)
def test_umltransition::changeeventrule_exp_setter(instance):
    original = instance.exp
    instance.exp = original
    assert instance.exp == original

@given(instance=umlTransition::CallOrSignalEventRule_strategy)
@settings(max_examples=50)
def test_umltransition::callorsignaleventrule_instantiation(instance):
    assert isinstance(instance, umlTransition::CallOrSignalEventRule)

@given(instance=umlTransition::EffectRule_strategy)
@settings(max_examples=50)
def test_umltransition::effectrule_instantiation(instance):
    assert isinstance(instance, umlTransition::EffectRule)

@given(instance=umlTransition::EffectRule_strategy)
def test_umltransition::effectrule_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=umlTransition::EffectRule_strategy)
def test_umltransition::effectrule_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=umlTransition::EffectRule_strategy)
def test_umltransition::effectrule_behaviorName_type(instance):
    assert isinstance(instance.behaviorName, str)


@given(instance=umlTransition::EffectRule_strategy)
def test_umltransition::effectrule_behaviorName_setter(instance):
    original = instance.behaviorName
    instance.behaviorName = original
    assert instance.behaviorName == original

@given(instance=umlTransition::GuardRule_strategy)
@settings(max_examples=50)
def test_umltransition::guardrule_instantiation(instance):
    assert isinstance(instance, umlTransition::GuardRule)

@given(instance=umlTransition::GuardRule_strategy)
def test_umltransition::guardrule_constraint_type(instance):
    assert isinstance(instance.constraint, str)


@given(instance=umlTransition::GuardRule_strategy)
def test_umltransition::guardrule_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original

@given(instance=umlTransition::EventRule_strategy)
@settings(max_examples=50)
def test_umltransition::eventrule_instantiation(instance):
    assert isinstance(instance, umlTransition::EventRule)
