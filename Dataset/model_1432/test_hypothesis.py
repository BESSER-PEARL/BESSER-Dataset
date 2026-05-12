import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    scmodel_AbstractState,
    scmodel_StateMachine,
    State,
    scmodel_History,
    scmodel_FinalState,
    AbstractState,
    scmodel_CompositeState,
    scmodel_PseudoState,
    scmodel_State,
    scmodel_Transition,
    TriggerTypes,
    PseudoStateTypes,
    LanguageTypes,
    MessageCheckerTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scmodel_abstractstate_is_not_abstract():
    assert not inspect.isabstract(scmodel_AbstractState)


def test_scmodel_abstractstate_constructor_exists():
    assert callable(scmodel_AbstractState.__init__)


def test_scmodel_abstractstate_constructor_args():
    sig = inspect.signature(scmodel_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "onEnterImports" in params, "Missing parameter 'onEnterImports'"
    assert "id" in params, "Missing parameter 'id'"
    assert "uuid" in params, "Missing parameter 'uuid'"
    assert "language" in params, "Missing parameter 'language'"
    assert "onExitImports" in params, "Missing parameter 'onExitImports'"
    assert "onExit" in params, "Missing parameter 'onExit'"
    assert "onEnter" in params, "Missing parameter 'onEnter'"

def test_scmodel_abstractstate_has_onEnterImports():
    assert hasattr(scmodel_AbstractState, "onEnterImports")
    descriptor = None
    for klass in scmodel_AbstractState.__mro__:
        if "onEnterImports" in klass.__dict__:
            descriptor = klass.__dict__["onEnterImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_abstractstate_has_id():
    assert hasattr(scmodel_AbstractState, "id")
    descriptor = None
    for klass in scmodel_AbstractState.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_abstractstate_has_uuid():
    assert hasattr(scmodel_AbstractState, "uuid")
    descriptor = None
    for klass in scmodel_AbstractState.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_abstractstate_has_language():
    assert hasattr(scmodel_AbstractState, "language")
    descriptor = None
    for klass in scmodel_AbstractState.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_abstractstate_has_onExitImports():
    assert hasattr(scmodel_AbstractState, "onExitImports")
    descriptor = None
    for klass in scmodel_AbstractState.__mro__:
        if "onExitImports" in klass.__dict__:
            descriptor = klass.__dict__["onExitImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_abstractstate_has_onExit():
    assert hasattr(scmodel_AbstractState, "onExit")
    descriptor = None
    for klass in scmodel_AbstractState.__mro__:
        if "onExit" in klass.__dict__:
            descriptor = klass.__dict__["onExit"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_abstractstate_has_onEnter():
    assert hasattr(scmodel_AbstractState, "onEnter")
    descriptor = None
    for klass in scmodel_AbstractState.__mro__:
        if "onEnter" in klass.__dict__:
            descriptor = klass.__dict__["onEnter"]
            break
    assert isinstance(descriptor, property)



def test_scmodel_statemachine_is_not_abstract():
    assert not inspect.isabstract(scmodel_StateMachine)


def test_scmodel_statemachine_constructor_exists():
    assert callable(scmodel_StateMachine.__init__)


def test_scmodel_statemachine_constructor_args():
    sig = inspect.signature(scmodel_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "nextID" in params, "Missing parameter 'nextID'"
    assert "id" in params, "Missing parameter 'id'"
    assert "package" in params, "Missing parameter 'package'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "uuid" in params, "Missing parameter 'uuid'"
    assert "className" in params, "Missing parameter 'className'"
    assert "agentType" in params, "Missing parameter 'agentType'"

def test_scmodel_statemachine_has_language():
    assert hasattr(scmodel_StateMachine, "language")
    descriptor = None
    for klass in scmodel_StateMachine.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_statemachine_has_nextID():
    assert hasattr(scmodel_StateMachine, "nextID")
    descriptor = None
    for klass in scmodel_StateMachine.__mro__:
        if "nextID" in klass.__dict__:
            descriptor = klass.__dict__["nextID"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_statemachine_has_id():
    assert hasattr(scmodel_StateMachine, "id")
    descriptor = None
    for klass in scmodel_StateMachine.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_statemachine_has_package():
    assert hasattr(scmodel_StateMachine, "package")
    descriptor = None
    for klass in scmodel_StateMachine.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_statemachine_has_priority():
    assert hasattr(scmodel_StateMachine, "priority")
    descriptor = None
    for klass in scmodel_StateMachine.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_statemachine_has_uuid():
    assert hasattr(scmodel_StateMachine, "uuid")
    descriptor = None
    for klass in scmodel_StateMachine.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_statemachine_has_className():
    assert hasattr(scmodel_StateMachine, "className")
    descriptor = None
    for klass in scmodel_StateMachine.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_statemachine_has_agentType():
    assert hasattr(scmodel_StateMachine, "agentType")
    descriptor = None
    for klass in scmodel_StateMachine.__mro__:
        if "agentType" in klass.__dict__:
            descriptor = klass.__dict__["agentType"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_scmodel_history_is_not_abstract():
    assert not inspect.isabstract(scmodel_History)


def test_scmodel_history_constructor_exists():
    assert callable(scmodel_History.__init__)


def test_scmodel_history_constructor_args():
    sig = inspect.signature(scmodel_History.__init__)
    params = list(sig.parameters.keys())
    assert "shallow" in params, "Missing parameter 'shallow'"

def test_scmodel_history_has_shallow():
    assert hasattr(scmodel_History, "shallow")
    descriptor = None
    for klass in scmodel_History.__mro__:
        if "shallow" in klass.__dict__:
            descriptor = klass.__dict__["shallow"]
            break
    assert isinstance(descriptor, property)



def test_scmodel_finalstate_is_not_abstract():
    assert not inspect.isabstract(scmodel_FinalState)


def test_scmodel_finalstate_constructor_exists():
    assert callable(scmodel_FinalState.__init__)


def test_scmodel_finalstate_constructor_args():
    sig = inspect.signature(scmodel_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_scmodel_compositestate_is_not_abstract():
    assert not inspect.isabstract(scmodel_CompositeState)


def test_scmodel_compositestate_constructor_exists():
    assert callable(scmodel_CompositeState.__init__)


def test_scmodel_compositestate_constructor_args():
    sig = inspect.signature(scmodel_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_scmodel_pseudostate_is_not_abstract():
    assert not inspect.isabstract(scmodel_PseudoState)


def test_scmodel_pseudostate_constructor_exists():
    assert callable(scmodel_PseudoState.__init__)


def test_scmodel_pseudostate_constructor_args():
    sig = inspect.signature(scmodel_PseudoState.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_scmodel_pseudostate_has_type():
    assert hasattr(scmodel_PseudoState, "type")
    descriptor = None
    for klass in scmodel_PseudoState.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_scmodel_state_is_not_abstract():
    assert not inspect.isabstract(scmodel_State)


def test_scmodel_state_constructor_exists():
    assert callable(scmodel_State.__init__)


def test_scmodel_state_constructor_args():
    sig = inspect.signature(scmodel_State.__init__)
    params = list(sig.parameters.keys())



def test_scmodel_transition_is_not_abstract():
    assert not inspect.isabstract(scmodel_Transition)


def test_scmodel_transition_constructor_exists():
    assert callable(scmodel_Transition.__init__)


def test_scmodel_transition_constructor_args():
    sig = inspect.signature(scmodel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"
    assert "triggerTimedCodeImports" in params, "Missing parameter 'triggerTimedCodeImports'"
    assert "onTransitionImports" in params, "Missing parameter 'onTransitionImports'"
    assert "triggerExpRateCode" in params, "Missing parameter 'triggerExpRateCode'"
    assert "triggerTime" in params, "Missing parameter 'triggerTime'"
    assert "triggerProbCode" in params, "Missing parameter 'triggerProbCode'"
    assert "selfTransition" in params, "Missing parameter 'selfTransition'"
    assert "onTransition" in params, "Missing parameter 'onTransition'"
    assert "messageCheckerCode" in params, "Missing parameter 'messageCheckerCode'"
    assert "uuid" in params, "Missing parameter 'uuid'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "triggerConditionCode" in params, "Missing parameter 'triggerConditionCode'"
    assert "messageCheckerClass" in params, "Missing parameter 'messageCheckerClass'"
    assert "guardImports" in params, "Missing parameter 'guardImports'"
    assert "messageCheckerCodeImports" in params, "Missing parameter 'messageCheckerCodeImports'"
    assert "triggerCodeLanguage" in params, "Missing parameter 'triggerCodeLanguage'"
    assert "triggerType" in params, "Missing parameter 'triggerType'"
    assert "id" in params, "Missing parameter 'id'"
    assert "triggerTimedCode" in params, "Missing parameter 'triggerTimedCode'"
    assert "outOfBranch" in params, "Missing parameter 'outOfBranch'"
    assert "triggerConditionCodeImports" in params, "Missing parameter 'triggerConditionCodeImports'"
    assert "triggerExpRateCodeImports" in params, "Missing parameter 'triggerExpRateCodeImports'"
    assert "defaultTransition" in params, "Missing parameter 'defaultTransition'"
    assert "messageCheckerConditionLanguage" in params, "Missing parameter 'messageCheckerConditionLanguage'"
    assert "triggerProbCodeImports" in params, "Missing parameter 'triggerProbCodeImports'"
    assert "messageCheckerType" in params, "Missing parameter 'messageCheckerType'"

def test_scmodel_transition_has_guard():
    assert hasattr(scmodel_Transition, "guard")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_triggerTimedCodeImports():
    assert hasattr(scmodel_Transition, "triggerTimedCodeImports")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "triggerTimedCodeImports" in klass.__dict__:
            descriptor = klass.__dict__["triggerTimedCodeImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_onTransitionImports():
    assert hasattr(scmodel_Transition, "onTransitionImports")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "onTransitionImports" in klass.__dict__:
            descriptor = klass.__dict__["onTransitionImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_triggerExpRateCode():
    assert hasattr(scmodel_Transition, "triggerExpRateCode")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "triggerExpRateCode" in klass.__dict__:
            descriptor = klass.__dict__["triggerExpRateCode"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_triggerTime():
    assert hasattr(scmodel_Transition, "triggerTime")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "triggerTime" in klass.__dict__:
            descriptor = klass.__dict__["triggerTime"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_triggerProbCode():
    assert hasattr(scmodel_Transition, "triggerProbCode")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "triggerProbCode" in klass.__dict__:
            descriptor = klass.__dict__["triggerProbCode"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_selfTransition():
    assert hasattr(scmodel_Transition, "selfTransition")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "selfTransition" in klass.__dict__:
            descriptor = klass.__dict__["selfTransition"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_onTransition():
    assert hasattr(scmodel_Transition, "onTransition")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "onTransition" in klass.__dict__:
            descriptor = klass.__dict__["onTransition"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_messageCheckerCode():
    assert hasattr(scmodel_Transition, "messageCheckerCode")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "messageCheckerCode" in klass.__dict__:
            descriptor = klass.__dict__["messageCheckerCode"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_uuid():
    assert hasattr(scmodel_Transition, "uuid")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_priority():
    assert hasattr(scmodel_Transition, "priority")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_triggerConditionCode():
    assert hasattr(scmodel_Transition, "triggerConditionCode")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "triggerConditionCode" in klass.__dict__:
            descriptor = klass.__dict__["triggerConditionCode"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_messageCheckerClass():
    assert hasattr(scmodel_Transition, "messageCheckerClass")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "messageCheckerClass" in klass.__dict__:
            descriptor = klass.__dict__["messageCheckerClass"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_guardImports():
    assert hasattr(scmodel_Transition, "guardImports")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "guardImports" in klass.__dict__:
            descriptor = klass.__dict__["guardImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_messageCheckerCodeImports():
    assert hasattr(scmodel_Transition, "messageCheckerCodeImports")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "messageCheckerCodeImports" in klass.__dict__:
            descriptor = klass.__dict__["messageCheckerCodeImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_triggerCodeLanguage():
    assert hasattr(scmodel_Transition, "triggerCodeLanguage")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "triggerCodeLanguage" in klass.__dict__:
            descriptor = klass.__dict__["triggerCodeLanguage"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_triggerType():
    assert hasattr(scmodel_Transition, "triggerType")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "triggerType" in klass.__dict__:
            descriptor = klass.__dict__["triggerType"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_id():
    assert hasattr(scmodel_Transition, "id")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_triggerTimedCode():
    assert hasattr(scmodel_Transition, "triggerTimedCode")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "triggerTimedCode" in klass.__dict__:
            descriptor = klass.__dict__["triggerTimedCode"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_outOfBranch():
    assert hasattr(scmodel_Transition, "outOfBranch")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "outOfBranch" in klass.__dict__:
            descriptor = klass.__dict__["outOfBranch"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_triggerConditionCodeImports():
    assert hasattr(scmodel_Transition, "triggerConditionCodeImports")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "triggerConditionCodeImports" in klass.__dict__:
            descriptor = klass.__dict__["triggerConditionCodeImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_triggerExpRateCodeImports():
    assert hasattr(scmodel_Transition, "triggerExpRateCodeImports")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "triggerExpRateCodeImports" in klass.__dict__:
            descriptor = klass.__dict__["triggerExpRateCodeImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_defaultTransition():
    assert hasattr(scmodel_Transition, "defaultTransition")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "defaultTransition" in klass.__dict__:
            descriptor = klass.__dict__["defaultTransition"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_messageCheckerConditionLanguage():
    assert hasattr(scmodel_Transition, "messageCheckerConditionLanguage")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "messageCheckerConditionLanguage" in klass.__dict__:
            descriptor = klass.__dict__["messageCheckerConditionLanguage"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_triggerProbCodeImports():
    assert hasattr(scmodel_Transition, "triggerProbCodeImports")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "triggerProbCodeImports" in klass.__dict__:
            descriptor = klass.__dict__["triggerProbCodeImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel_transition_has_messageCheckerType():
    assert hasattr(scmodel_Transition, "messageCheckerType")
    descriptor = None
    for klass in scmodel_Transition.__mro__:
        if "messageCheckerType" in klass.__dict__:
            descriptor = klass.__dict__["messageCheckerType"]
            break
    assert isinstance(descriptor, property)

def test_triggertypes_exists():
    # Check that the Enumeration exists
    assert TriggerTypes is not None

def test_triggertypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerTypes]
    expected_literals = [
        "always",
        "message",
        "exponential",
        "timed",
        "probability",
        "condition",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriggerTypes"

def test_pseudostatetypes_exists():
    # Check that the Enumeration exists
    assert PseudoStateTypes is not None

def test_pseudostatetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudoStateTypes]
    expected_literals = [
        "entry",
        "choice",
        "initial",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudoStateTypes"

def test_languagetypes_exists():
    # Check that the Enumeration exists
    assert LanguageTypes is not None

def test_languagetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LanguageTypes]
    expected_literals = [
        "java",
        "groovy",
        "relogo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LanguageTypes"

def test_messagecheckertypes_exists():
    # Check that the Enumeration exists
    assert MessageCheckerTypes is not None

def test_messagecheckertypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageCheckerTypes]
    expected_literals = [
        "equals",
        "conditional",
        "unconditional",
        "always",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageCheckerTypes"


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
scmodel_AbstractState_strategy = st.builds(
    scmodel_AbstractState,
    onEnterImports=
        safe_text,
    id=
        safe_text,
    uuid=
        safe_text,
    language=
        safe_text,
    onExitImports=
        safe_text,
    onExit=
        safe_text,
    onEnter=
        safe_text
)
scmodel_StateMachine_strategy = st.builds(
    scmodel_StateMachine,
    language=
        safe_text,
    nextID=
        st.integers(),
    id=
        safe_text,
    package=
        safe_text,
    priority=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    uuid=
        safe_text,
    className=
        safe_text,
    agentType=
        safe_text
)
State_strategy = st.builds(
    State,
)
scmodel_History_strategy = st.builds(
    scmodel_History,
    shallow=
        st.booleans()
)
scmodel_FinalState_strategy = st.builds(
    scmodel_FinalState,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
scmodel_CompositeState_strategy = st.builds(
    scmodel_CompositeState,
)
scmodel_PseudoState_strategy = st.builds(
    scmodel_PseudoState,
    type=
        safe_text
)
scmodel_State_strategy = st.builds(
    scmodel_State,
)
scmodel_Transition_strategy = st.builds(
    scmodel_Transition,
    guard=
        safe_text,
    triggerTimedCodeImports=
        safe_text,
    onTransitionImports=
        safe_text,
    triggerExpRateCode=
        safe_text,
    triggerTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    triggerProbCode=
        safe_text,
    selfTransition=
        st.booleans(),
    onTransition=
        safe_text,
    messageCheckerCode=
        safe_text,
    uuid=
        safe_text,
    priority=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    triggerConditionCode=
        safe_text,
    messageCheckerClass=
        safe_text,
    guardImports=
        safe_text,
    messageCheckerCodeImports=
        safe_text,
    triggerCodeLanguage=
        safe_text,
    triggerType=
        safe_text,
    id=
        safe_text,
    triggerTimedCode=
        safe_text,
    outOfBranch=
        st.booleans(),
    triggerConditionCodeImports=
        safe_text,
    triggerExpRateCodeImports=
        safe_text,
    defaultTransition=
        st.booleans(),
    messageCheckerConditionLanguage=
        safe_text,
    triggerProbCodeImports=
        safe_text,
    messageCheckerType=
        safe_text
)

@given(instance=scmodel_AbstractState_strategy)
@settings(max_examples=50)
def test_scmodel_abstractstate_instantiation(instance):
    assert isinstance(instance, scmodel_AbstractState)



@given(instance=scmodel_AbstractState_strategy)
def test_scmodel_abstractstate_onEnterImports_setter(instance):
    original = instance.onEnterImports
    instance.onEnterImports = original
    assert instance.onEnterImports == original



@given(instance=scmodel_AbstractState_strategy)
def test_scmodel_abstractstate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scmodel_AbstractState_strategy)
def test_scmodel_abstractstate_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original



@given(instance=scmodel_AbstractState_strategy)
def test_scmodel_abstractstate_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=scmodel_AbstractState_strategy)
def test_scmodel_abstractstate_onExitImports_setter(instance):
    original = instance.onExitImports
    instance.onExitImports = original
    assert instance.onExitImports == original



@given(instance=scmodel_AbstractState_strategy)
def test_scmodel_abstractstate_onExit_setter(instance):
    original = instance.onExit
    instance.onExit = original
    assert instance.onExit == original



@given(instance=scmodel_AbstractState_strategy)
def test_scmodel_abstractstate_onEnter_setter(instance):
    original = instance.onEnter
    instance.onEnter = original
    assert instance.onEnter == original

@given(instance=scmodel_StateMachine_strategy)
@settings(max_examples=50)
def test_scmodel_statemachine_instantiation(instance):
    assert isinstance(instance, scmodel_StateMachine)



@given(instance=scmodel_StateMachine_strategy)
def test_scmodel_statemachine_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=scmodel_StateMachine_strategy)
def test_scmodel_statemachine_nextID_setter(instance):
    original = instance.nextID
    instance.nextID = original
    assert instance.nextID == original



@given(instance=scmodel_StateMachine_strategy)
def test_scmodel_statemachine_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scmodel_StateMachine_strategy)
def test_scmodel_statemachine_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original



@given(instance=scmodel_StateMachine_strategy)
def test_scmodel_statemachine_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=scmodel_StateMachine_strategy)
def test_scmodel_statemachine_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original



@given(instance=scmodel_StateMachine_strategy)
def test_scmodel_statemachine_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original



@given(instance=scmodel_StateMachine_strategy)
def test_scmodel_statemachine_agentType_setter(instance):
    original = instance.agentType
    instance.agentType = original
    assert instance.agentType == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=scmodel_History_strategy)
@settings(max_examples=50)
def test_scmodel_history_instantiation(instance):
    assert isinstance(instance, scmodel_History)



@given(instance=scmodel_History_strategy)
def test_scmodel_history_shallow_setter(instance):
    original = instance.shallow
    instance.shallow = original
    assert instance.shallow == original

@given(instance=scmodel_FinalState_strategy)
@settings(max_examples=50)
def test_scmodel_finalstate_instantiation(instance):
    assert isinstance(instance, scmodel_FinalState)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=scmodel_CompositeState_strategy)
@settings(max_examples=50)
def test_scmodel_compositestate_instantiation(instance):
    assert isinstance(instance, scmodel_CompositeState)

@given(instance=scmodel_PseudoState_strategy)
@settings(max_examples=50)
def test_scmodel_pseudostate_instantiation(instance):
    assert isinstance(instance, scmodel_PseudoState)



@given(instance=scmodel_PseudoState_strategy)
def test_scmodel_pseudostate_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scmodel_State_strategy)
@settings(max_examples=50)
def test_scmodel_state_instantiation(instance):
    assert isinstance(instance, scmodel_State)

@given(instance=scmodel_Transition_strategy)
@settings(max_examples=50)
def test_scmodel_transition_instantiation(instance):
    assert isinstance(instance, scmodel_Transition)



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_triggerTimedCodeImports_setter(instance):
    original = instance.triggerTimedCodeImports
    instance.triggerTimedCodeImports = original
    assert instance.triggerTimedCodeImports == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_onTransitionImports_setter(instance):
    original = instance.onTransitionImports
    instance.onTransitionImports = original
    assert instance.onTransitionImports == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_triggerExpRateCode_setter(instance):
    original = instance.triggerExpRateCode
    instance.triggerExpRateCode = original
    assert instance.triggerExpRateCode == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_triggerTime_setter(instance):
    original = instance.triggerTime
    instance.triggerTime = original
    assert instance.triggerTime == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_triggerProbCode_setter(instance):
    original = instance.triggerProbCode
    instance.triggerProbCode = original
    assert instance.triggerProbCode == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_selfTransition_setter(instance):
    original = instance.selfTransition
    instance.selfTransition = original
    assert instance.selfTransition == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_onTransition_setter(instance):
    original = instance.onTransition
    instance.onTransition = original
    assert instance.onTransition == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_messageCheckerCode_setter(instance):
    original = instance.messageCheckerCode
    instance.messageCheckerCode = original
    assert instance.messageCheckerCode == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_triggerConditionCode_setter(instance):
    original = instance.triggerConditionCode
    instance.triggerConditionCode = original
    assert instance.triggerConditionCode == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_messageCheckerClass_setter(instance):
    original = instance.messageCheckerClass
    instance.messageCheckerClass = original
    assert instance.messageCheckerClass == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_guardImports_setter(instance):
    original = instance.guardImports
    instance.guardImports = original
    assert instance.guardImports == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_messageCheckerCodeImports_setter(instance):
    original = instance.messageCheckerCodeImports
    instance.messageCheckerCodeImports = original
    assert instance.messageCheckerCodeImports == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_triggerCodeLanguage_setter(instance):
    original = instance.triggerCodeLanguage
    instance.triggerCodeLanguage = original
    assert instance.triggerCodeLanguage == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_triggerType_setter(instance):
    original = instance.triggerType
    instance.triggerType = original
    assert instance.triggerType == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_triggerTimedCode_setter(instance):
    original = instance.triggerTimedCode
    instance.triggerTimedCode = original
    assert instance.triggerTimedCode == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_outOfBranch_setter(instance):
    original = instance.outOfBranch
    instance.outOfBranch = original
    assert instance.outOfBranch == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_triggerConditionCodeImports_setter(instance):
    original = instance.triggerConditionCodeImports
    instance.triggerConditionCodeImports = original
    assert instance.triggerConditionCodeImports == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_triggerExpRateCodeImports_setter(instance):
    original = instance.triggerExpRateCodeImports
    instance.triggerExpRateCodeImports = original
    assert instance.triggerExpRateCodeImports == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_defaultTransition_setter(instance):
    original = instance.defaultTransition
    instance.defaultTransition = original
    assert instance.defaultTransition == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_messageCheckerConditionLanguage_setter(instance):
    original = instance.messageCheckerConditionLanguage
    instance.messageCheckerConditionLanguage = original
    assert instance.messageCheckerConditionLanguage == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_triggerProbCodeImports_setter(instance):
    original = instance.triggerProbCodeImports
    instance.triggerProbCodeImports = original
    assert instance.triggerProbCodeImports == original



@given(instance=scmodel_Transition_strategy)
def test_scmodel_transition_messageCheckerType_setter(instance):
    original = instance.messageCheckerType
    instance.messageCheckerType = original
    assert instance.messageCheckerType == original
