import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Referenced,
    ModelRoot,
    region::RgRegion,
    region::RgTransition,
    Named,
    region::RgState,
    region::RgInitialPseudostate,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_referenced_is_not_abstract():
    assert not inspect.isabstract(Referenced)


def test_referenced_constructor_exists():
    assert callable(Referenced.__init__)


def test_referenced_constructor_args():
    sig = inspect.signature(Referenced.__init__)
    params = list(sig.parameters.keys())



def test_modelroot_is_not_abstract():
    assert not inspect.isabstract(ModelRoot)


def test_modelroot_constructor_exists():
    assert callable(ModelRoot.__init__)


def test_modelroot_constructor_args():
    sig = inspect.signature(ModelRoot.__init__)
    params = list(sig.parameters.keys())



def test_region::rgregion_is_not_abstract():
    assert not inspect.isabstract(region::RgRegion)


def test_region::rgregion_constructor_exists():
    assert callable(region::RgRegion.__init__)


def test_region::rgregion_constructor_args():
    sig = inspect.signature(region::RgRegion.__init__)
    params = list(sig.parameters.keys())
    assert "containerClass" in params, "Missing parameter 'containerClass'"

def test_region::rgregion_has_containerClass():
    assert hasattr(region::RgRegion, "containerClass")
    descriptor = None
    for klass in region::RgRegion.__mro__:
        if "containerClass" in klass.__dict__:
            descriptor = klass.__dict__["containerClass"]
            break
    assert isinstance(descriptor, property)



def test_region::rgtransition_is_not_abstract():
    assert not inspect.isabstract(region::RgTransition)


def test_region::rgtransition_constructor_exists():
    assert callable(region::RgTransition.__init__)


def test_region::rgtransition_constructor_args():
    sig = inspect.signature(region::RgTransition.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "event" in params, "Missing parameter 'event'"
    assert "effect" in params, "Missing parameter 'effect'"

def test_region::rgtransition_has_message():
    assert hasattr(region::RgTransition, "message")
    descriptor = None
    for klass in region::RgTransition.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_region::rgtransition_has_event():
    assert hasattr(region::RgTransition, "event")
    descriptor = None
    for klass in region::RgTransition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_region::rgtransition_has_effect():
    assert hasattr(region::RgTransition, "effect")
    descriptor = None
    for klass in region::RgTransition.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_region::rgstate_is_not_abstract():
    assert not inspect.isabstract(region::RgState)


def test_region::rgstate_constructor_exists():
    assert callable(region::RgState.__init__)


def test_region::rgstate_constructor_args():
    sig = inspect.signature(region::RgState.__init__)
    params = list(sig.parameters.keys())
    assert "entry" in params, "Missing parameter 'entry'"
    assert "exit" in params, "Missing parameter 'exit'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"

def test_region::rgstate_has_entry():
    assert hasattr(region::RgState, "entry")
    descriptor = None
    for klass in region::RgState.__mro__:
        if "entry" in klass.__dict__:
            descriptor = klass.__dict__["entry"]
            break
    assert isinstance(descriptor, property)

def test_region::rgstate_has_exit():
    assert hasattr(region::RgState, "exit")
    descriptor = None
    for klass in region::RgState.__mro__:
        if "exit" in klass.__dict__:
            descriptor = klass.__dict__["exit"]
            break
    assert isinstance(descriptor, property)

def test_region::rgstate_has_isFinal():
    assert hasattr(region::RgState, "isFinal")
    descriptor = None
    for klass in region::RgState.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)



def test_region::rginitialpseudostate_is_not_abstract():
    assert not inspect.isabstract(region::RgInitialPseudostate)


def test_region::rginitialpseudostate_constructor_exists():
    assert callable(region::RgInitialPseudostate.__init__)


def test_region::rginitialpseudostate_constructor_args():
    sig = inspect.signature(region::RgInitialPseudostate.__init__)
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
Referenced_strategy = st.builds(
    Referenced,
)
ModelRoot_strategy = st.builds(
    ModelRoot,
)
region::RgRegion_strategy = st.builds(
    region::RgRegion,
    containerClass=
        safe_text
)
region::RgTransition_strategy = st.builds(
    region::RgTransition,
    message=
        safe_text,
    event=
        safe_text,
    effect=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
region::RgState_strategy = st.builds(
    region::RgState,
    entry=
        safe_text,
    exit=
        safe_text,
    isFinal=
        st.booleans()
)
region::RgInitialPseudostate_strategy = st.builds(
    region::RgInitialPseudostate,
)

@given(instance=Referenced_strategy)
@settings(max_examples=50)
def test_referenced_instantiation(instance):
    assert isinstance(instance, Referenced)

@given(instance=ModelRoot_strategy)
@settings(max_examples=50)
def test_modelroot_instantiation(instance):
    assert isinstance(instance, ModelRoot)

@given(instance=region::RgRegion_strategy)
@settings(max_examples=50)
def test_region::rgregion_instantiation(instance):
    assert isinstance(instance, region::RgRegion)

@given(instance=region::RgRegion_strategy)
def test_region::rgregion_containerClass_type(instance):
    assert isinstance(instance.containerClass, str)


@given(instance=region::RgRegion_strategy)
def test_region::rgregion_containerClass_setter(instance):
    original = instance.containerClass
    instance.containerClass = original
    assert instance.containerClass == original

@given(instance=region::RgTransition_strategy)
@settings(max_examples=50)
def test_region::rgtransition_instantiation(instance):
    assert isinstance(instance, region::RgTransition)

@given(instance=region::RgTransition_strategy)
def test_region::rgtransition_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=region::RgTransition_strategy)
def test_region::rgtransition_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=region::RgTransition_strategy)
def test_region::rgtransition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=region::RgTransition_strategy)
def test_region::rgtransition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=region::RgTransition_strategy)
def test_region::rgtransition_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=region::RgTransition_strategy)
def test_region::rgtransition_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=region::RgState_strategy)
@settings(max_examples=50)
def test_region::rgstate_instantiation(instance):
    assert isinstance(instance, region::RgState)

@given(instance=region::RgState_strategy)
def test_region::rgstate_entry_type(instance):
    assert isinstance(instance.entry, str)


@given(instance=region::RgState_strategy)
def test_region::rgstate_entry_setter(instance):
    original = instance.entry
    instance.entry = original
    assert instance.entry == original

@given(instance=region::RgState_strategy)
def test_region::rgstate_exit_type(instance):
    assert isinstance(instance.exit, str)


@given(instance=region::RgState_strategy)
def test_region::rgstate_exit_setter(instance):
    original = instance.exit
    instance.exit = original
    assert instance.exit == original

@given(instance=region::RgState_strategy)
def test_region::rgstate_isFinal_type(instance):
    assert isinstance(instance.isFinal, bool)


@given(instance=region::RgState_strategy)
def test_region::rgstate_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=region::RgInitialPseudostate_strategy)
@settings(max_examples=50)
def test_region::rginitialpseudostate_instantiation(instance):
    assert isinstance(instance, region::RgInitialPseudostate)
