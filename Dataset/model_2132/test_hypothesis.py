import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TextualCode,
    synccharts_TextualCode,
    synccharts_EObject,
    Action,
    synccharts_Transition,
    synccharts_Substitution,
    Scope,
    synccharts_State,
    synccharts_Region,
    synccharts_Signal,
    synccharts_Variable,
    Effect,
    synccharts_Emission,
    synccharts_TextEffect,
    synccharts_Assignment,
    synccharts_Expression,
    synccharts_Effect,
    Annotatable,
    synccharts_Scope,
    synccharts_Action,
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



def test_synccharts_textualcode_is_not_abstract():
    assert not inspect.isabstract(synccharts_TextualCode)


def test_synccharts_textualcode_constructor_exists():
    assert callable(synccharts_TextualCode.__init__)


def test_synccharts_textualcode_constructor_args():
    sig = inspect.signature(synccharts_TextualCode.__init__)
    params = list(sig.parameters.keys())



def test_synccharts_eobject_is_not_abstract():
    assert not inspect.isabstract(synccharts_EObject)


def test_synccharts_eobject_constructor_exists():
    assert callable(synccharts_EObject.__init__)


def test_synccharts_eobject_constructor_args():
    sig = inspect.signature(synccharts_EObject.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_synccharts_transition_is_not_abstract():
    assert not inspect.isabstract(synccharts_Transition)


def test_synccharts_transition_constructor_exists():
    assert callable(synccharts_Transition.__init__)


def test_synccharts_transition_constructor_args():
    sig = inspect.signature(synccharts_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "isHistory" in params, "Missing parameter 'isHistory'"
    assert "type" in params, "Missing parameter 'type'"
    assert "priority" in params, "Missing parameter 'priority'"

def test_synccharts_transition_has_isHistory():
    assert hasattr(synccharts_Transition, "isHistory")
    descriptor = None
    for klass in synccharts_Transition.__mro__:
        if "isHistory" in klass.__dict__:
            descriptor = klass.__dict__["isHistory"]
            break
    assert isinstance(descriptor, property)

def test_synccharts_transition_has_type():
    assert hasattr(synccharts_Transition, "type")
    descriptor = None
    for klass in synccharts_Transition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_synccharts_transition_has_priority():
    assert hasattr(synccharts_Transition, "priority")
    descriptor = None
    for klass in synccharts_Transition.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_synccharts_substitution_is_not_abstract():
    assert not inspect.isabstract(synccharts_Substitution)


def test_synccharts_substitution_constructor_exists():
    assert callable(synccharts_Substitution.__init__)


def test_synccharts_substitution_constructor_args():
    sig = inspect.signature(synccharts_Substitution.__init__)
    params = list(sig.parameters.keys())
    assert "formal" in params, "Missing parameter 'formal'"
    assert "actual" in params, "Missing parameter 'actual'"

def test_synccharts_substitution_has_formal():
    assert hasattr(synccharts_Substitution, "formal")
    descriptor = None
    for klass in synccharts_Substitution.__mro__:
        if "formal" in klass.__dict__:
            descriptor = klass.__dict__["formal"]
            break
    assert isinstance(descriptor, property)

def test_synccharts_substitution_has_actual():
    assert hasattr(synccharts_Substitution, "actual")
    descriptor = None
    for klass in synccharts_Substitution.__mro__:
        if "actual" in klass.__dict__:
            descriptor = klass.__dict__["actual"]
            break
    assert isinstance(descriptor, property)



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_synccharts_state_is_not_abstract():
    assert not inspect.isabstract(synccharts_State)


def test_synccharts_state_constructor_exists():
    assert callable(synccharts_State.__init__)


def test_synccharts_state_constructor_args():
    sig = inspect.signature(synccharts_State.__init__)
    params = list(sig.parameters.keys())
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "type" in params, "Missing parameter 'type'"
    assert "isInitial" in params, "Missing parameter 'isInitial'"

def test_synccharts_state_has_isFinal():
    assert hasattr(synccharts_State, "isFinal")
    descriptor = None
    for klass in synccharts_State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_synccharts_state_has_type():
    assert hasattr(synccharts_State, "type")
    descriptor = None
    for klass in synccharts_State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_synccharts_state_has_isInitial():
    assert hasattr(synccharts_State, "isInitial")
    descriptor = None
    for klass in synccharts_State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)



def test_synccharts_region_is_not_abstract():
    assert not inspect.isabstract(synccharts_Region)


def test_synccharts_region_constructor_exists():
    assert callable(synccharts_Region.__init__)


def test_synccharts_region_constructor_args():
    sig = inspect.signature(synccharts_Region.__init__)
    params = list(sig.parameters.keys())



def test_synccharts_signal_is_not_abstract():
    assert not inspect.isabstract(synccharts_Signal)


def test_synccharts_signal_constructor_exists():
    assert callable(synccharts_Signal.__init__)


def test_synccharts_signal_constructor_args():
    sig = inspect.signature(synccharts_Signal.__init__)
    params = list(sig.parameters.keys())



def test_synccharts_variable_is_not_abstract():
    assert not inspect.isabstract(synccharts_Variable)


def test_synccharts_variable_constructor_exists():
    assert callable(synccharts_Variable.__init__)


def test_synccharts_variable_constructor_args():
    sig = inspect.signature(synccharts_Variable.__init__)
    params = list(sig.parameters.keys())



def test_effect_is_not_abstract():
    assert not inspect.isabstract(Effect)


def test_effect_constructor_exists():
    assert callable(Effect.__init__)


def test_effect_constructor_args():
    sig = inspect.signature(Effect.__init__)
    params = list(sig.parameters.keys())



def test_synccharts_emission_is_not_abstract():
    assert not inspect.isabstract(synccharts_Emission)


def test_synccharts_emission_constructor_exists():
    assert callable(synccharts_Emission.__init__)


def test_synccharts_emission_constructor_args():
    sig = inspect.signature(synccharts_Emission.__init__)
    params = list(sig.parameters.keys())



def test_synccharts_texteffect_is_not_abstract():
    assert not inspect.isabstract(synccharts_TextEffect)


def test_synccharts_texteffect_constructor_exists():
    assert callable(synccharts_TextEffect.__init__)


def test_synccharts_texteffect_constructor_args():
    sig = inspect.signature(synccharts_TextEffect.__init__)
    params = list(sig.parameters.keys())



def test_synccharts_assignment_is_not_abstract():
    assert not inspect.isabstract(synccharts_Assignment)


def test_synccharts_assignment_constructor_exists():
    assert callable(synccharts_Assignment.__init__)


def test_synccharts_assignment_constructor_args():
    sig = inspect.signature(synccharts_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_synccharts_expression_is_not_abstract():
    assert not inspect.isabstract(synccharts_Expression)


def test_synccharts_expression_constructor_exists():
    assert callable(synccharts_Expression.__init__)


def test_synccharts_expression_constructor_args():
    sig = inspect.signature(synccharts_Expression.__init__)
    params = list(sig.parameters.keys())



def test_synccharts_effect_is_not_abstract():
    assert not inspect.isabstract(synccharts_Effect)


def test_synccharts_effect_constructor_exists():
    assert callable(synccharts_Effect.__init__)


def test_synccharts_effect_constructor_args():
    sig = inspect.signature(synccharts_Effect.__init__)
    params = list(sig.parameters.keys())



def test_annotatable_is_not_abstract():
    assert not inspect.isabstract(Annotatable)


def test_annotatable_constructor_exists():
    assert callable(Annotatable.__init__)


def test_annotatable_constructor_args():
    sig = inspect.signature(Annotatable.__init__)
    params = list(sig.parameters.keys())



def test_synccharts_scope_is_not_abstract():
    assert not inspect.isabstract(synccharts_Scope)


def test_synccharts_scope_constructor_exists():
    assert callable(synccharts_Scope.__init__)


def test_synccharts_scope_constructor_args():
    sig = inspect.signature(synccharts_Scope.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "label" in params, "Missing parameter 'label'"
    assert "interfaceDeclaration" in params, "Missing parameter 'interfaceDeclaration'"

def test_synccharts_scope_has_id():
    assert hasattr(synccharts_Scope, "id")
    descriptor = None
    for klass in synccharts_Scope.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_synccharts_scope_has_label():
    assert hasattr(synccharts_Scope, "label")
    descriptor = None
    for klass in synccharts_Scope.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_synccharts_scope_has_interfaceDeclaration():
    assert hasattr(synccharts_Scope, "interfaceDeclaration")
    descriptor = None
    for klass in synccharts_Scope.__mro__:
        if "interfaceDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["interfaceDeclaration"]
            break
    assert isinstance(descriptor, property)



def test_synccharts_action_is_not_abstract():
    assert not inspect.isabstract(synccharts_Action)


def test_synccharts_action_constructor_exists():
    assert callable(synccharts_Action.__init__)


def test_synccharts_action_constructor_args():
    sig = inspect.signature(synccharts_Action.__init__)
    params = list(sig.parameters.keys())
    assert "delay" in params, "Missing parameter 'delay'"
    assert "label" in params, "Missing parameter 'label'"
    assert "isImmediate" in params, "Missing parameter 'isImmediate'"

def test_synccharts_action_has_delay():
    assert hasattr(synccharts_Action, "delay")
    descriptor = None
    for klass in synccharts_Action.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)

def test_synccharts_action_has_label():
    assert hasattr(synccharts_Action, "label")
    descriptor = None
    for klass in synccharts_Action.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_synccharts_action_has_isImmediate():
    assert hasattr(synccharts_Action, "isImmediate")
    descriptor = None
    for klass in synccharts_Action.__mro__:
        if "isImmediate" in klass.__dict__:
            descriptor = klass.__dict__["isImmediate"]
            break
    assert isinstance(descriptor, property)

def test_statetype_exists():
    # Check that the Enumeration exists
    assert StateType is not None

def test_statetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateType]
    expected_literals = [
        "CONDITIONAL",
        "REFERENCE",
        "NORMAL",
        "TEXTUAL",
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
        "WEAKABORT",
        "NORMALTERMINATION",
        "STRONGABORT",
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
synccharts_TextualCode_strategy = st.builds(
    synccharts_TextualCode,
)
synccharts_EObject_strategy = st.builds(
    synccharts_EObject,
)
Action_strategy = st.builds(
    Action,
)
synccharts_Transition_strategy = st.builds(
    synccharts_Transition,
    isHistory=
        st.booleans(),
    type=
        safe_text,
    priority=
        st.integers()
)
synccharts_Substitution_strategy = st.builds(
    synccharts_Substitution,
    formal=
        safe_text,
    actual=
        safe_text
)
Scope_strategy = st.builds(
    Scope,
)
synccharts_State_strategy = st.builds(
    synccharts_State,
    isFinal=
        st.booleans(),
    type=
        safe_text,
    isInitial=
        st.booleans()
)
synccharts_Region_strategy = st.builds(
    synccharts_Region,
)
synccharts_Signal_strategy = st.builds(
    synccharts_Signal,
)
synccharts_Variable_strategy = st.builds(
    synccharts_Variable,
)
Effect_strategy = st.builds(
    Effect,
)
synccharts_Emission_strategy = st.builds(
    synccharts_Emission,
)
synccharts_TextEffect_strategy = st.builds(
    synccharts_TextEffect,
)
synccharts_Assignment_strategy = st.builds(
    synccharts_Assignment,
)
synccharts_Expression_strategy = st.builds(
    synccharts_Expression,
)
synccharts_Effect_strategy = st.builds(
    synccharts_Effect,
)
Annotatable_strategy = st.builds(
    Annotatable,
)
synccharts_Scope_strategy = st.builds(
    synccharts_Scope,
    id=
        safe_text,
    label=
        safe_text,
    interfaceDeclaration=
        safe_text
)
synccharts_Action_strategy = st.builds(
    synccharts_Action,
    delay=
        st.integers(),
    label=
        safe_text,
    isImmediate=
        st.booleans()
)

@given(instance=TextualCode_strategy)
@settings(max_examples=50)
def test_textualcode_instantiation(instance):
    assert isinstance(instance, TextualCode)

@given(instance=synccharts_TextualCode_strategy)
@settings(max_examples=50)
def test_synccharts_textualcode_instantiation(instance):
    assert isinstance(instance, synccharts_TextualCode)

@given(instance=synccharts_EObject_strategy)
@settings(max_examples=50)
def test_synccharts_eobject_instantiation(instance):
    assert isinstance(instance, synccharts_EObject)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=synccharts_Transition_strategy)
@settings(max_examples=50)
def test_synccharts_transition_instantiation(instance):
    assert isinstance(instance, synccharts_Transition)



@given(instance=synccharts_Transition_strategy)
def test_synccharts_transition_isHistory_setter(instance):
    original = instance.isHistory
    instance.isHistory = original
    assert instance.isHistory == original



@given(instance=synccharts_Transition_strategy)
def test_synccharts_transition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=synccharts_Transition_strategy)
def test_synccharts_transition_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=synccharts_Substitution_strategy)
@settings(max_examples=50)
def test_synccharts_substitution_instantiation(instance):
    assert isinstance(instance, synccharts_Substitution)



@given(instance=synccharts_Substitution_strategy)
def test_synccharts_substitution_formal_setter(instance):
    original = instance.formal
    instance.formal = original
    assert instance.formal == original



@given(instance=synccharts_Substitution_strategy)
def test_synccharts_substitution_actual_setter(instance):
    original = instance.actual
    instance.actual = original
    assert instance.actual == original

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=synccharts_State_strategy)
@settings(max_examples=50)
def test_synccharts_state_instantiation(instance):
    assert isinstance(instance, synccharts_State)



@given(instance=synccharts_State_strategy)
def test_synccharts_state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original



@given(instance=synccharts_State_strategy)
def test_synccharts_state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=synccharts_State_strategy)
def test_synccharts_state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=synccharts_Region_strategy)
@settings(max_examples=50)
def test_synccharts_region_instantiation(instance):
    assert isinstance(instance, synccharts_Region)

@given(instance=synccharts_Signal_strategy)
@settings(max_examples=50)
def test_synccharts_signal_instantiation(instance):
    assert isinstance(instance, synccharts_Signal)

@given(instance=synccharts_Variable_strategy)
@settings(max_examples=50)
def test_synccharts_variable_instantiation(instance):
    assert isinstance(instance, synccharts_Variable)

@given(instance=Effect_strategy)
@settings(max_examples=50)
def test_effect_instantiation(instance):
    assert isinstance(instance, Effect)

@given(instance=synccharts_Emission_strategy)
@settings(max_examples=50)
def test_synccharts_emission_instantiation(instance):
    assert isinstance(instance, synccharts_Emission)

@given(instance=synccharts_TextEffect_strategy)
@settings(max_examples=50)
def test_synccharts_texteffect_instantiation(instance):
    assert isinstance(instance, synccharts_TextEffect)

@given(instance=synccharts_Assignment_strategy)
@settings(max_examples=50)
def test_synccharts_assignment_instantiation(instance):
    assert isinstance(instance, synccharts_Assignment)

@given(instance=synccharts_Expression_strategy)
@settings(max_examples=50)
def test_synccharts_expression_instantiation(instance):
    assert isinstance(instance, synccharts_Expression)

@given(instance=synccharts_Effect_strategy)
@settings(max_examples=50)
def test_synccharts_effect_instantiation(instance):
    assert isinstance(instance, synccharts_Effect)

@given(instance=Annotatable_strategy)
@settings(max_examples=50)
def test_annotatable_instantiation(instance):
    assert isinstance(instance, Annotatable)

@given(instance=synccharts_Scope_strategy)
@settings(max_examples=50)
def test_synccharts_scope_instantiation(instance):
    assert isinstance(instance, synccharts_Scope)



@given(instance=synccharts_Scope_strategy)
def test_synccharts_scope_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=synccharts_Scope_strategy)
def test_synccharts_scope_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=synccharts_Scope_strategy)
def test_synccharts_scope_interfaceDeclaration_setter(instance):
    original = instance.interfaceDeclaration
    instance.interfaceDeclaration = original
    assert instance.interfaceDeclaration == original

@given(instance=synccharts_Action_strategy)
@settings(max_examples=50)
def test_synccharts_action_instantiation(instance):
    assert isinstance(instance, synccharts_Action)



@given(instance=synccharts_Action_strategy)
def test_synccharts_action_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original



@given(instance=synccharts_Action_strategy)
def test_synccharts_action_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=synccharts_Action_strategy)
def test_synccharts_action_isImmediate_setter(instance):
    original = instance.isImmediate
    instance.isImmediate = original
    assert instance.isImmediate == original
