import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TextualCode,
    synccharts::TextualCode,
    Action,
    synccharts::EObject,
    synccharts::Substitution,
    Scope,
    synccharts::State,
    synccharts::Region,
    synccharts::Signal,
    synccharts::Transition,
    synccharts::Expression,
    synccharts::Effect,
    Annotatable,
    synccharts::Scope,
    synccharts::Action,
    synccharts::Variable,
    Effect,
    synccharts::TextEffect,
    synccharts::Emission,
    synccharts::Assignment,
    StateType,
    TransitionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_textualcode_is_not_abstract():
    assert not inspect.isabstract(TextualCode)


def test_textualcode_constructor_exists():
    assert callable(TextualCode.__init__)


def test_textualcode_constructor_args():
    sig = inspect.signature(TextualCode.__init__)
    params = list(sig.parameters.keys())



def test_synccharts::textualcode_is_not_abstract():
    assert not inspect.isabstract(synccharts::TextualCode)


def test_synccharts::textualcode_constructor_exists():
    assert callable(synccharts::TextualCode.__init__)


def test_synccharts::textualcode_constructor_args():
    sig = inspect.signature(synccharts::TextualCode.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_synccharts::eobject_is_not_abstract():
    assert not inspect.isabstract(synccharts::EObject)


def test_synccharts::eobject_constructor_exists():
    assert callable(synccharts::EObject.__init__)


def test_synccharts::eobject_constructor_args():
    sig = inspect.signature(synccharts::EObject.__init__)
    params = list(sig.parameters.keys())



def test_synccharts::substitution_is_not_abstract():
    assert not inspect.isabstract(synccharts::Substitution)


def test_synccharts::substitution_constructor_exists():
    assert callable(synccharts::Substitution.__init__)


def test_synccharts::substitution_constructor_args():
    sig = inspect.signature(synccharts::Substitution.__init__)
    params = list(sig.parameters.keys())
    assert "actual" in params, "Missing parameter 'actual'"
    assert "formal" in params, "Missing parameter 'formal'"

def test_synccharts::substitution_has_actual():
    assert hasattr(synccharts::Substitution, "actual")
    descriptor = None
    for klass in synccharts::Substitution.__mro__:
        if "actual" in klass.__dict__:
            descriptor = klass.__dict__["actual"]
            break
    assert isinstance(descriptor, property)

def test_synccharts::substitution_has_formal():
    assert hasattr(synccharts::Substitution, "formal")
    descriptor = None
    for klass in synccharts::Substitution.__mro__:
        if "formal" in klass.__dict__:
            descriptor = klass.__dict__["formal"]
            break
    assert isinstance(descriptor, property)



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_synccharts::state_is_not_abstract():
    assert not inspect.isabstract(synccharts::State)


def test_synccharts::state_constructor_exists():
    assert callable(synccharts::State.__init__)


def test_synccharts::state_constructor_args():
    sig = inspect.signature(synccharts::State.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "isInitial" in params, "Missing parameter 'isInitial'"

def test_synccharts::state_has_type():
    assert hasattr(synccharts::State, "type")
    descriptor = None
    for klass in synccharts::State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_synccharts::state_has_isFinal():
    assert hasattr(synccharts::State, "isFinal")
    descriptor = None
    for klass in synccharts::State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_synccharts::state_has_isInitial():
    assert hasattr(synccharts::State, "isInitial")
    descriptor = None
    for klass in synccharts::State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)



def test_synccharts::region_is_not_abstract():
    assert not inspect.isabstract(synccharts::Region)


def test_synccharts::region_constructor_exists():
    assert callable(synccharts::Region.__init__)


def test_synccharts::region_constructor_args():
    sig = inspect.signature(synccharts::Region.__init__)
    params = list(sig.parameters.keys())



def test_synccharts::signal_is_not_abstract():
    assert not inspect.isabstract(synccharts::Signal)


def test_synccharts::signal_constructor_exists():
    assert callable(synccharts::Signal.__init__)


def test_synccharts::signal_constructor_args():
    sig = inspect.signature(synccharts::Signal.__init__)
    params = list(sig.parameters.keys())



def test_synccharts::transition_is_not_abstract():
    assert not inspect.isabstract(synccharts::Transition)


def test_synccharts::transition_constructor_exists():
    assert callable(synccharts::Transition.__init__)


def test_synccharts::transition_constructor_args():
    sig = inspect.signature(synccharts::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "isHistory" in params, "Missing parameter 'isHistory'"
    assert "type" in params, "Missing parameter 'type'"

def test_synccharts::transition_has_priority():
    assert hasattr(synccharts::Transition, "priority")
    descriptor = None
    for klass in synccharts::Transition.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_synccharts::transition_has_isHistory():
    assert hasattr(synccharts::Transition, "isHistory")
    descriptor = None
    for klass in synccharts::Transition.__mro__:
        if "isHistory" in klass.__dict__:
            descriptor = klass.__dict__["isHistory"]
            break
    assert isinstance(descriptor, property)

def test_synccharts::transition_has_type():
    assert hasattr(synccharts::Transition, "type")
    descriptor = None
    for klass in synccharts::Transition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_synccharts::expression_is_not_abstract():
    assert not inspect.isabstract(synccharts::Expression)


def test_synccharts::expression_constructor_exists():
    assert callable(synccharts::Expression.__init__)


def test_synccharts::expression_constructor_args():
    sig = inspect.signature(synccharts::Expression.__init__)
    params = list(sig.parameters.keys())



def test_synccharts::effect_is_not_abstract():
    assert not inspect.isabstract(synccharts::Effect)


def test_synccharts::effect_constructor_exists():
    assert callable(synccharts::Effect.__init__)


def test_synccharts::effect_constructor_args():
    sig = inspect.signature(synccharts::Effect.__init__)
    params = list(sig.parameters.keys())



def test_annotatable_is_not_abstract():
    assert not inspect.isabstract(Annotatable)


def test_annotatable_constructor_exists():
    assert callable(Annotatable.__init__)


def test_annotatable_constructor_args():
    sig = inspect.signature(Annotatable.__init__)
    params = list(sig.parameters.keys())



def test_synccharts::scope_is_not_abstract():
    assert not inspect.isabstract(synccharts::Scope)


def test_synccharts::scope_constructor_exists():
    assert callable(synccharts::Scope.__init__)


def test_synccharts::scope_constructor_args():
    sig = inspect.signature(synccharts::Scope.__init__)
    params = list(sig.parameters.keys())
    assert "interfaceDeclaration" in params, "Missing parameter 'interfaceDeclaration'"
    assert "id" in params, "Missing parameter 'id'"
    assert "label" in params, "Missing parameter 'label'"

def test_synccharts::scope_has_interfaceDeclaration():
    assert hasattr(synccharts::Scope, "interfaceDeclaration")
    descriptor = None
    for klass in synccharts::Scope.__mro__:
        if "interfaceDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["interfaceDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_synccharts::scope_has_id():
    assert hasattr(synccharts::Scope, "id")
    descriptor = None
    for klass in synccharts::Scope.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_synccharts::scope_has_label():
    assert hasattr(synccharts::Scope, "label")
    descriptor = None
    for klass in synccharts::Scope.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_synccharts::action_is_not_abstract():
    assert not inspect.isabstract(synccharts::Action)


def test_synccharts::action_constructor_exists():
    assert callable(synccharts::Action.__init__)


def test_synccharts::action_constructor_args():
    sig = inspect.signature(synccharts::Action.__init__)
    params = list(sig.parameters.keys())
    assert "isImmediate" in params, "Missing parameter 'isImmediate'"
    assert "label" in params, "Missing parameter 'label'"
    assert "delay" in params, "Missing parameter 'delay'"

def test_synccharts::action_has_isImmediate():
    assert hasattr(synccharts::Action, "isImmediate")
    descriptor = None
    for klass in synccharts::Action.__mro__:
        if "isImmediate" in klass.__dict__:
            descriptor = klass.__dict__["isImmediate"]
            break
    assert isinstance(descriptor, property)

def test_synccharts::action_has_label():
    assert hasattr(synccharts::Action, "label")
    descriptor = None
    for klass in synccharts::Action.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_synccharts::action_has_delay():
    assert hasattr(synccharts::Action, "delay")
    descriptor = None
    for klass in synccharts::Action.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)



def test_synccharts::variable_is_not_abstract():
    assert not inspect.isabstract(synccharts::Variable)


def test_synccharts::variable_constructor_exists():
    assert callable(synccharts::Variable.__init__)


def test_synccharts::variable_constructor_args():
    sig = inspect.signature(synccharts::Variable.__init__)
    params = list(sig.parameters.keys())



def test_effect_is_not_abstract():
    assert not inspect.isabstract(Effect)


def test_effect_constructor_exists():
    assert callable(Effect.__init__)


def test_effect_constructor_args():
    sig = inspect.signature(Effect.__init__)
    params = list(sig.parameters.keys())



def test_synccharts::texteffect_is_not_abstract():
    assert not inspect.isabstract(synccharts::TextEffect)


def test_synccharts::texteffect_constructor_exists():
    assert callable(synccharts::TextEffect.__init__)


def test_synccharts::texteffect_constructor_args():
    sig = inspect.signature(synccharts::TextEffect.__init__)
    params = list(sig.parameters.keys())



def test_synccharts::emission_is_not_abstract():
    assert not inspect.isabstract(synccharts::Emission)


def test_synccharts::emission_constructor_exists():
    assert callable(synccharts::Emission.__init__)


def test_synccharts::emission_constructor_args():
    sig = inspect.signature(synccharts::Emission.__init__)
    params = list(sig.parameters.keys())



def test_synccharts::assignment_is_not_abstract():
    assert not inspect.isabstract(synccharts::Assignment)


def test_synccharts::assignment_constructor_exists():
    assert callable(synccharts::Assignment.__init__)


def test_synccharts::assignment_constructor_args():
    sig = inspect.signature(synccharts::Assignment.__init__)
    params = list(sig.parameters.keys())

def test_statetype_exists():
    # Check that the Enumeration exists
    assert StateType is not None

def test_statetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateType]
    expected_literals = [
        "REFERENCE",
        "NORMAL",
        "TEXTUAL",
        "CONDITIONAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StateType"

def test_transitiontype_exists():
    # Check that the Enumeration exists
    assert TransitionType is not None

def test_transitiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionType]
    expected_literals = [
        "STRONGABORT",
        "WEAKABORT",
        "NORMALTERMINATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionType"


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
TextualCode_strategy = st.builds(
    TextualCode,
)
synccharts::TextualCode_strategy = st.builds(
    synccharts::TextualCode,
)
Action_strategy = st.builds(
    Action,
)
synccharts::EObject_strategy = st.builds(
    synccharts::EObject,
)
synccharts::Substitution_strategy = st.builds(
    synccharts::Substitution,
    actual=
        safe_text,
    formal=
        safe_text
)
Scope_strategy = st.builds(
    Scope,
)
synccharts::State_strategy = st.builds(
    synccharts::State,
    type=
        safe_text,
    isFinal=
        st.booleans(),
    isInitial=
        st.booleans()
)
synccharts::Region_strategy = st.builds(
    synccharts::Region,
)
synccharts::Signal_strategy = st.builds(
    synccharts::Signal,
)
synccharts::Transition_strategy = st.builds(
    synccharts::Transition,
    priority=
        st.integers(),
    isHistory=
        st.booleans(),
    type=
        safe_text
)
synccharts::Expression_strategy = st.builds(
    synccharts::Expression,
)
synccharts::Effect_strategy = st.builds(
    synccharts::Effect,
)
Annotatable_strategy = st.builds(
    Annotatable,
)
synccharts::Scope_strategy = st.builds(
    synccharts::Scope,
    interfaceDeclaration=
        safe_text,
    id=
        safe_text,
    label=
        safe_text
)
synccharts::Action_strategy = st.builds(
    synccharts::Action,
    isImmediate=
        st.booleans(),
    label=
        safe_text,
    delay=
        st.integers()
)
synccharts::Variable_strategy = st.builds(
    synccharts::Variable,
)
Effect_strategy = st.builds(
    Effect,
)
synccharts::TextEffect_strategy = st.builds(
    synccharts::TextEffect,
)
synccharts::Emission_strategy = st.builds(
    synccharts::Emission,
)
synccharts::Assignment_strategy = st.builds(
    synccharts::Assignment,
)

@given(instance=TextualCode_strategy)
@settings(max_examples=50)
def test_textualcode_instantiation(instance):
    assert isinstance(instance, TextualCode)

@given(instance=synccharts::TextualCode_strategy)
@settings(max_examples=50)
def test_synccharts::textualcode_instantiation(instance):
    assert isinstance(instance, synccharts::TextualCode)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=synccharts::EObject_strategy)
@settings(max_examples=50)
def test_synccharts::eobject_instantiation(instance):
    assert isinstance(instance, synccharts::EObject)

@given(instance=synccharts::Substitution_strategy)
@settings(max_examples=50)
def test_synccharts::substitution_instantiation(instance):
    assert isinstance(instance, synccharts::Substitution)

@given(instance=synccharts::Substitution_strategy)
def test_synccharts::substitution_actual_type(instance):
    assert isinstance(instance.actual, str)


@given(instance=synccharts::Substitution_strategy)
def test_synccharts::substitution_actual_setter(instance):
    original = instance.actual
    instance.actual = original
    assert instance.actual == original

@given(instance=synccharts::Substitution_strategy)
def test_synccharts::substitution_formal_type(instance):
    assert isinstance(instance.formal, str)


@given(instance=synccharts::Substitution_strategy)
def test_synccharts::substitution_formal_setter(instance):
    original = instance.formal
    instance.formal = original
    assert instance.formal == original

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=synccharts::State_strategy)
@settings(max_examples=50)
def test_synccharts::state_instantiation(instance):
    assert isinstance(instance, synccharts::State)

@given(instance=synccharts::State_strategy)
def test_synccharts::state_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=synccharts::State_strategy)
def test_synccharts::state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=synccharts::State_strategy)
def test_synccharts::state_isFinal_type(instance):
    assert isinstance(instance.isFinal, bool)


@given(instance=synccharts::State_strategy)
def test_synccharts::state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=synccharts::State_strategy)
def test_synccharts::state_isInitial_type(instance):
    assert isinstance(instance.isInitial, bool)


@given(instance=synccharts::State_strategy)
def test_synccharts::state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=synccharts::Region_strategy)
@settings(max_examples=50)
def test_synccharts::region_instantiation(instance):
    assert isinstance(instance, synccharts::Region)

@given(instance=synccharts::Signal_strategy)
@settings(max_examples=50)
def test_synccharts::signal_instantiation(instance):
    assert isinstance(instance, synccharts::Signal)

@given(instance=synccharts::Transition_strategy)
@settings(max_examples=50)
def test_synccharts::transition_instantiation(instance):
    assert isinstance(instance, synccharts::Transition)

@given(instance=synccharts::Transition_strategy)
def test_synccharts::transition_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=synccharts::Transition_strategy)
def test_synccharts::transition_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=synccharts::Transition_strategy)
def test_synccharts::transition_isHistory_type(instance):
    assert isinstance(instance.isHistory, bool)


@given(instance=synccharts::Transition_strategy)
def test_synccharts::transition_isHistory_setter(instance):
    original = instance.isHistory
    instance.isHistory = original
    assert instance.isHistory == original

@given(instance=synccharts::Transition_strategy)
def test_synccharts::transition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=synccharts::Transition_strategy)
def test_synccharts::transition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=synccharts::Expression_strategy)
@settings(max_examples=50)
def test_synccharts::expression_instantiation(instance):
    assert isinstance(instance, synccharts::Expression)

@given(instance=synccharts::Effect_strategy)
@settings(max_examples=50)
def test_synccharts::effect_instantiation(instance):
    assert isinstance(instance, synccharts::Effect)

@given(instance=Annotatable_strategy)
@settings(max_examples=50)
def test_annotatable_instantiation(instance):
    assert isinstance(instance, Annotatable)

@given(instance=synccharts::Scope_strategy)
@settings(max_examples=50)
def test_synccharts::scope_instantiation(instance):
    assert isinstance(instance, synccharts::Scope)

@given(instance=synccharts::Scope_strategy)
def test_synccharts::scope_interfaceDeclaration_type(instance):
    assert isinstance(instance.interfaceDeclaration, str)


@given(instance=synccharts::Scope_strategy)
def test_synccharts::scope_interfaceDeclaration_setter(instance):
    original = instance.interfaceDeclaration
    instance.interfaceDeclaration = original
    assert instance.interfaceDeclaration == original

@given(instance=synccharts::Scope_strategy)
def test_synccharts::scope_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=synccharts::Scope_strategy)
def test_synccharts::scope_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=synccharts::Scope_strategy)
def test_synccharts::scope_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=synccharts::Scope_strategy)
def test_synccharts::scope_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=synccharts::Action_strategy)
@settings(max_examples=50)
def test_synccharts::action_instantiation(instance):
    assert isinstance(instance, synccharts::Action)

@given(instance=synccharts::Action_strategy)
def test_synccharts::action_isImmediate_type(instance):
    assert isinstance(instance.isImmediate, bool)


@given(instance=synccharts::Action_strategy)
def test_synccharts::action_isImmediate_setter(instance):
    original = instance.isImmediate
    instance.isImmediate = original
    assert instance.isImmediate == original

@given(instance=synccharts::Action_strategy)
def test_synccharts::action_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=synccharts::Action_strategy)
def test_synccharts::action_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=synccharts::Action_strategy)
def test_synccharts::action_delay_type(instance):
    assert isinstance(instance.delay, int)


@given(instance=synccharts::Action_strategy)
def test_synccharts::action_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original

@given(instance=synccharts::Variable_strategy)
@settings(max_examples=50)
def test_synccharts::variable_instantiation(instance):
    assert isinstance(instance, synccharts::Variable)

@given(instance=Effect_strategy)
@settings(max_examples=50)
def test_effect_instantiation(instance):
    assert isinstance(instance, Effect)

@given(instance=synccharts::TextEffect_strategy)
@settings(max_examples=50)
def test_synccharts::texteffect_instantiation(instance):
    assert isinstance(instance, synccharts::TextEffect)

@given(instance=synccharts::Emission_strategy)
@settings(max_examples=50)
def test_synccharts::emission_instantiation(instance):
    assert isinstance(instance, synccharts::Emission)

@given(instance=synccharts::Assignment_strategy)
@settings(max_examples=50)
def test_synccharts::assignment_instantiation(instance):
    assert isinstance(instance, synccharts::Assignment)
