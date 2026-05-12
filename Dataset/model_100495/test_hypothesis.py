import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    umlTransition_NamedElement,
    EventRule,
    umlTransition_TimeEventRule,
    umlTransition_AnyReceiveEventRule,
    umlTransition_CallOrSignalEventRule,
    umlTransition_EffectRule,
    umlTransition_GuardRule,
    umlTransition_EventRule,
    umlTransition_ChangeEventRule,
    TimeEventRule,
    umlTransition_AbsoluteTimeEventRule,
    umlTransition_RelativeTimeEventRule,
    umlTransition_TransitionRule,
    BehaviorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_umltransition_namedelement_is_not_abstract():
    assert not inspect.isabstract(umlTransition_NamedElement)


def test_umltransition_namedelement_constructor_exists():
    assert callable(umlTransition_NamedElement.__init__)


def test_umltransition_namedelement_constructor_args():
    sig = inspect.signature(umlTransition_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_eventrule_is_not_abstract():
    assert not inspect.isabstract(EventRule)


def test_eventrule_constructor_exists():
    assert callable(EventRule.__init__)


def test_eventrule_constructor_args():
    sig = inspect.signature(EventRule.__init__)
    params = list(sig.parameters.keys())



def test_umltransition_timeeventrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition_TimeEventRule)


def test_umltransition_timeeventrule_constructor_exists():
    assert callable(umlTransition_TimeEventRule.__init__)


def test_umltransition_timeeventrule_constructor_args():
    sig = inspect.signature(umlTransition_TimeEventRule.__init__)
    params = list(sig.parameters.keys())
    assert "expr" in params, "Missing parameter 'expr'"

def test_umltransition_timeeventrule_has_expr():
    assert hasattr(umlTransition_TimeEventRule, "expr")
    descriptor = None
    for klass in umlTransition_TimeEventRule.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)



def test_umltransition_anyreceiveeventrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition_AnyReceiveEventRule)


def test_umltransition_anyreceiveeventrule_constructor_exists():
    assert callable(umlTransition_AnyReceiveEventRule.__init__)


def test_umltransition_anyreceiveeventrule_constructor_args():
    sig = inspect.signature(umlTransition_AnyReceiveEventRule.__init__)
    params = list(sig.parameters.keys())
    assert "isAReceiveEvent" in params, "Missing parameter 'isAReceiveEvent'"

def test_umltransition_anyreceiveeventrule_has_isAReceiveEvent():
    assert hasattr(umlTransition_AnyReceiveEventRule, "isAReceiveEvent")
    descriptor = None
    for klass in umlTransition_AnyReceiveEventRule.__mro__:
        if "isAReceiveEvent" in klass.__dict__:
            descriptor = klass.__dict__["isAReceiveEvent"]
            break
    assert isinstance(descriptor, property)



def test_umltransition_callorsignaleventrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition_CallOrSignalEventRule)


def test_umltransition_callorsignaleventrule_constructor_exists():
    assert callable(umlTransition_CallOrSignalEventRule.__init__)


def test_umltransition_callorsignaleventrule_constructor_args():
    sig = inspect.signature(umlTransition_CallOrSignalEventRule.__init__)
    params = list(sig.parameters.keys())



def test_umltransition_effectrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition_EffectRule)


def test_umltransition_effectrule_constructor_exists():
    assert callable(umlTransition_EffectRule.__init__)


def test_umltransition_effectrule_constructor_args():
    sig = inspect.signature(umlTransition_EffectRule.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "behaviorName" in params, "Missing parameter 'behaviorName'"

def test_umltransition_effectrule_has_kind():
    assert hasattr(umlTransition_EffectRule, "kind")
    descriptor = None
    for klass in umlTransition_EffectRule.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_umltransition_effectrule_has_behaviorName():
    assert hasattr(umlTransition_EffectRule, "behaviorName")
    descriptor = None
    for klass in umlTransition_EffectRule.__mro__:
        if "behaviorName" in klass.__dict__:
            descriptor = klass.__dict__["behaviorName"]
            break
    assert isinstance(descriptor, property)



def test_umltransition_guardrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition_GuardRule)


def test_umltransition_guardrule_constructor_exists():
    assert callable(umlTransition_GuardRule.__init__)


def test_umltransition_guardrule_constructor_args():
    sig = inspect.signature(umlTransition_GuardRule.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"

def test_umltransition_guardrule_has_constraint():
    assert hasattr(umlTransition_GuardRule, "constraint")
    descriptor = None
    for klass in umlTransition_GuardRule.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)



def test_umltransition_eventrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition_EventRule)


def test_umltransition_eventrule_constructor_exists():
    assert callable(umlTransition_EventRule.__init__)


def test_umltransition_eventrule_constructor_args():
    sig = inspect.signature(umlTransition_EventRule.__init__)
    params = list(sig.parameters.keys())



def test_umltransition_changeeventrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition_ChangeEventRule)


def test_umltransition_changeeventrule_constructor_exists():
    assert callable(umlTransition_ChangeEventRule.__init__)


def test_umltransition_changeeventrule_constructor_args():
    sig = inspect.signature(umlTransition_ChangeEventRule.__init__)
    params = list(sig.parameters.keys())
    assert "exp" in params, "Missing parameter 'exp'"

def test_umltransition_changeeventrule_has_exp():
    assert hasattr(umlTransition_ChangeEventRule, "exp")
    descriptor = None
    for klass in umlTransition_ChangeEventRule.__mro__:
        if "exp" in klass.__dict__:
            descriptor = klass.__dict__["exp"]
            break
    assert isinstance(descriptor, property)



def test_timeeventrule_is_not_abstract():
    assert not inspect.isabstract(TimeEventRule)


def test_timeeventrule_constructor_exists():
    assert callable(TimeEventRule.__init__)


def test_timeeventrule_constructor_args():
    sig = inspect.signature(TimeEventRule.__init__)
    params = list(sig.parameters.keys())



def test_umltransition_absolutetimeeventrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition_AbsoluteTimeEventRule)


def test_umltransition_absolutetimeeventrule_constructor_exists():
    assert callable(umlTransition_AbsoluteTimeEventRule.__init__)


def test_umltransition_absolutetimeeventrule_constructor_args():
    sig = inspect.signature(umlTransition_AbsoluteTimeEventRule.__init__)
    params = list(sig.parameters.keys())



def test_umltransition_relativetimeeventrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition_RelativeTimeEventRule)


def test_umltransition_relativetimeeventrule_constructor_exists():
    assert callable(umlTransition_RelativeTimeEventRule.__init__)


def test_umltransition_relativetimeeventrule_constructor_args():
    sig = inspect.signature(umlTransition_RelativeTimeEventRule.__init__)
    params = list(sig.parameters.keys())



def test_umltransition_transitionrule_is_not_abstract():
    assert not inspect.isabstract(umlTransition_TransitionRule)


def test_umltransition_transitionrule_constructor_exists():
    assert callable(umlTransition_TransitionRule.__init__)


def test_umltransition_transitionrule_constructor_args():
    sig = inspect.signature(umlTransition_TransitionRule.__init__)
    params = list(sig.parameters.keys())

def test_behaviorkind_exists():
    # Check that the Enumeration exists
    assert BehaviorKind is not None

def test_behaviorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BehaviorKind]
    expected_literals = [
        "OPAQUE_BEHAVIOR",
        "STATE_MACHINE",
        "ACTIVITY",
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
umlTransition_NamedElement_strategy = st.builds(
    umlTransition_NamedElement,
)
EventRule_strategy = st.builds(
    EventRule,
)
umlTransition_TimeEventRule_strategy = st.builds(
    umlTransition_TimeEventRule,
    expr=
        safe_text
)
umlTransition_AnyReceiveEventRule_strategy = st.builds(
    umlTransition_AnyReceiveEventRule,
    isAReceiveEvent=
        safe_text
)
umlTransition_CallOrSignalEventRule_strategy = st.builds(
    umlTransition_CallOrSignalEventRule,
)
umlTransition_EffectRule_strategy = st.builds(
    umlTransition_EffectRule,
    kind=
        safe_text,
    behaviorName=
        safe_text
)
umlTransition_GuardRule_strategy = st.builds(
    umlTransition_GuardRule,
    constraint=
        safe_text
)
umlTransition_EventRule_strategy = st.builds(
    umlTransition_EventRule,
)
umlTransition_ChangeEventRule_strategy = st.builds(
    umlTransition_ChangeEventRule,
    exp=
        safe_text
)
TimeEventRule_strategy = st.builds(
    TimeEventRule,
)
umlTransition_AbsoluteTimeEventRule_strategy = st.builds(
    umlTransition_AbsoluteTimeEventRule,
)
umlTransition_RelativeTimeEventRule_strategy = st.builds(
    umlTransition_RelativeTimeEventRule,
)
umlTransition_TransitionRule_strategy = st.builds(
    umlTransition_TransitionRule,
)

@given(instance=umlTransition_NamedElement_strategy)
@settings(max_examples=50)
def test_umltransition_namedelement_instantiation(instance):
    assert isinstance(instance, umlTransition_NamedElement)

@given(instance=EventRule_strategy)
@settings(max_examples=50)
def test_eventrule_instantiation(instance):
    assert isinstance(instance, EventRule)

@given(instance=umlTransition_TimeEventRule_strategy)
@settings(max_examples=50)
def test_umltransition_timeeventrule_instantiation(instance):
    assert isinstance(instance, umlTransition_TimeEventRule)



@given(instance=umlTransition_TimeEventRule_strategy)
def test_umltransition_timeeventrule_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=umlTransition_AnyReceiveEventRule_strategy)
@settings(max_examples=50)
def test_umltransition_anyreceiveeventrule_instantiation(instance):
    assert isinstance(instance, umlTransition_AnyReceiveEventRule)



@given(instance=umlTransition_AnyReceiveEventRule_strategy)
def test_umltransition_anyreceiveeventrule_isAReceiveEvent_setter(instance):
    original = instance.isAReceiveEvent
    instance.isAReceiveEvent = original
    assert instance.isAReceiveEvent == original

@given(instance=umlTransition_CallOrSignalEventRule_strategy)
@settings(max_examples=50)
def test_umltransition_callorsignaleventrule_instantiation(instance):
    assert isinstance(instance, umlTransition_CallOrSignalEventRule)

@given(instance=umlTransition_EffectRule_strategy)
@settings(max_examples=50)
def test_umltransition_effectrule_instantiation(instance):
    assert isinstance(instance, umlTransition_EffectRule)



@given(instance=umlTransition_EffectRule_strategy)
def test_umltransition_effectrule_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=umlTransition_EffectRule_strategy)
def test_umltransition_effectrule_behaviorName_setter(instance):
    original = instance.behaviorName
    instance.behaviorName = original
    assert instance.behaviorName == original

@given(instance=umlTransition_GuardRule_strategy)
@settings(max_examples=50)
def test_umltransition_guardrule_instantiation(instance):
    assert isinstance(instance, umlTransition_GuardRule)



@given(instance=umlTransition_GuardRule_strategy)
def test_umltransition_guardrule_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original

@given(instance=umlTransition_EventRule_strategy)
@settings(max_examples=50)
def test_umltransition_eventrule_instantiation(instance):
    assert isinstance(instance, umlTransition_EventRule)

@given(instance=umlTransition_ChangeEventRule_strategy)
@settings(max_examples=50)
def test_umltransition_changeeventrule_instantiation(instance):
    assert isinstance(instance, umlTransition_ChangeEventRule)



@given(instance=umlTransition_ChangeEventRule_strategy)
def test_umltransition_changeeventrule_exp_setter(instance):
    original = instance.exp
    instance.exp = original
    assert instance.exp == original

@given(instance=TimeEventRule_strategy)
@settings(max_examples=50)
def test_timeeventrule_instantiation(instance):
    assert isinstance(instance, TimeEventRule)

@given(instance=umlTransition_AbsoluteTimeEventRule_strategy)
@settings(max_examples=50)
def test_umltransition_absolutetimeeventrule_instantiation(instance):
    assert isinstance(instance, umlTransition_AbsoluteTimeEventRule)

@given(instance=umlTransition_RelativeTimeEventRule_strategy)
@settings(max_examples=50)
def test_umltransition_relativetimeeventrule_instantiation(instance):
    assert isinstance(instance, umlTransition_RelativeTimeEventRule)

@given(instance=umlTransition_TransitionRule_strategy)
@settings(max_examples=50)
def test_umltransition_transitionrule_instantiation(instance):
    assert isinstance(instance, umlTransition_TransitionRule)
