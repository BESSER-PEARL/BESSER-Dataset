import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    scmodel::History,
    scmodel::FinalState,
    AbstractState,
    scmodel::PseudoState,
    scmodel::CompositeState,
    scmodel::State,
    scmodel::Transition,
    scmodel::AbstractState,
    scmodel::StateMachine,
    TriggerTypes,
    PseudoStateTypes,
    LanguageTypes,
    MessageCheckerTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_scmodel::history_is_not_abstract():
    assert not inspect.isabstract(scmodel::History)


def test_scmodel::history_constructor_exists():
    assert callable(scmodel::History.__init__)


def test_scmodel::history_constructor_args():
    sig = inspect.signature(scmodel::History.__init__)
    params = list(sig.parameters.keys())
    assert "shallow" in params, "Missing parameter 'shallow'"

def test_scmodel::history_has_shallow():
    assert hasattr(scmodel::History, "shallow")
    descriptor = None
    for klass in scmodel::History.__mro__:
        if "shallow" in klass.__dict__:
            descriptor = klass.__dict__["shallow"]
            break
    assert isinstance(descriptor, property)



def test_scmodel::finalstate_is_not_abstract():
    assert not inspect.isabstract(scmodel::FinalState)


def test_scmodel::finalstate_constructor_exists():
    assert callable(scmodel::FinalState.__init__)


def test_scmodel::finalstate_constructor_args():
    sig = inspect.signature(scmodel::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_scmodel::pseudostate_is_not_abstract():
    assert not inspect.isabstract(scmodel::PseudoState)


def test_scmodel::pseudostate_constructor_exists():
    assert callable(scmodel::PseudoState.__init__)


def test_scmodel::pseudostate_constructor_args():
    sig = inspect.signature(scmodel::PseudoState.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_scmodel::pseudostate_has_type():
    assert hasattr(scmodel::PseudoState, "type")
    descriptor = None
    for klass in scmodel::PseudoState.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_scmodel::compositestate_is_not_abstract():
    assert not inspect.isabstract(scmodel::CompositeState)


def test_scmodel::compositestate_constructor_exists():
    assert callable(scmodel::CompositeState.__init__)


def test_scmodel::compositestate_constructor_args():
    sig = inspect.signature(scmodel::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_scmodel::state_is_not_abstract():
    assert not inspect.isabstract(scmodel::State)


def test_scmodel::state_constructor_exists():
    assert callable(scmodel::State.__init__)


def test_scmodel::state_constructor_args():
    sig = inspect.signature(scmodel::State.__init__)
    params = list(sig.parameters.keys())



def test_scmodel::transition_is_not_abstract():
    assert not inspect.isabstract(scmodel::Transition)


def test_scmodel::transition_constructor_exists():
    assert callable(scmodel::Transition.__init__)


def test_scmodel::transition_constructor_args():
    sig = inspect.signature(scmodel::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "messageCheckerCodeImports" in params, "Missing parameter 'messageCheckerCodeImports'"
    assert "triggerExpRateCodeImports" in params, "Missing parameter 'triggerExpRateCodeImports'"
    assert "messageCheckerCode" in params, "Missing parameter 'messageCheckerCode'"
    assert "outOfBranch" in params, "Missing parameter 'outOfBranch'"
    assert "triggerType" in params, "Missing parameter 'triggerType'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "triggerCodeLanguage" in params, "Missing parameter 'triggerCodeLanguage'"
    assert "triggerProbCode" in params, "Missing parameter 'triggerProbCode'"
    assert "triggerExpRateCode" in params, "Missing parameter 'triggerExpRateCode'"
    assert "triggerTimedCodeImports" in params, "Missing parameter 'triggerTimedCodeImports'"
    assert "onTransition" in params, "Missing parameter 'onTransition'"
    assert "messageCheckerType" in params, "Missing parameter 'messageCheckerType'"
    assert "triggerConditionCodeImports" in params, "Missing parameter 'triggerConditionCodeImports'"
    assert "messageCheckerConditionLanguage" in params, "Missing parameter 'messageCheckerConditionLanguage'"
    assert "id" in params, "Missing parameter 'id'"
    assert "triggerTimedCode" in params, "Missing parameter 'triggerTimedCode'"
    assert "triggerConditionCode" in params, "Missing parameter 'triggerConditionCode'"
    assert "uuid" in params, "Missing parameter 'uuid'"
    assert "triggerProbCodeImports" in params, "Missing parameter 'triggerProbCodeImports'"
    assert "defaultTransition" in params, "Missing parameter 'defaultTransition'"
    assert "selfTransition" in params, "Missing parameter 'selfTransition'"
    assert "messageCheckerClass" in params, "Missing parameter 'messageCheckerClass'"
    assert "onTransitionImports" in params, "Missing parameter 'onTransitionImports'"
    assert "guardImports" in params, "Missing parameter 'guardImports'"
    assert "triggerTime" in params, "Missing parameter 'triggerTime'"

def test_scmodel::transition_has_messageCheckerCodeImports():
    assert hasattr(scmodel::Transition, "messageCheckerCodeImports")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "messageCheckerCodeImports" in klass.__dict__:
            descriptor = klass.__dict__["messageCheckerCodeImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_triggerExpRateCodeImports():
    assert hasattr(scmodel::Transition, "triggerExpRateCodeImports")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "triggerExpRateCodeImports" in klass.__dict__:
            descriptor = klass.__dict__["triggerExpRateCodeImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_messageCheckerCode():
    assert hasattr(scmodel::Transition, "messageCheckerCode")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "messageCheckerCode" in klass.__dict__:
            descriptor = klass.__dict__["messageCheckerCode"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_outOfBranch():
    assert hasattr(scmodel::Transition, "outOfBranch")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "outOfBranch" in klass.__dict__:
            descriptor = klass.__dict__["outOfBranch"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_triggerType():
    assert hasattr(scmodel::Transition, "triggerType")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "triggerType" in klass.__dict__:
            descriptor = klass.__dict__["triggerType"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_priority():
    assert hasattr(scmodel::Transition, "priority")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_guard():
    assert hasattr(scmodel::Transition, "guard")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_triggerCodeLanguage():
    assert hasattr(scmodel::Transition, "triggerCodeLanguage")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "triggerCodeLanguage" in klass.__dict__:
            descriptor = klass.__dict__["triggerCodeLanguage"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_triggerProbCode():
    assert hasattr(scmodel::Transition, "triggerProbCode")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "triggerProbCode" in klass.__dict__:
            descriptor = klass.__dict__["triggerProbCode"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_triggerExpRateCode():
    assert hasattr(scmodel::Transition, "triggerExpRateCode")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "triggerExpRateCode" in klass.__dict__:
            descriptor = klass.__dict__["triggerExpRateCode"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_triggerTimedCodeImports():
    assert hasattr(scmodel::Transition, "triggerTimedCodeImports")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "triggerTimedCodeImports" in klass.__dict__:
            descriptor = klass.__dict__["triggerTimedCodeImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_onTransition():
    assert hasattr(scmodel::Transition, "onTransition")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "onTransition" in klass.__dict__:
            descriptor = klass.__dict__["onTransition"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_messageCheckerType():
    assert hasattr(scmodel::Transition, "messageCheckerType")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "messageCheckerType" in klass.__dict__:
            descriptor = klass.__dict__["messageCheckerType"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_triggerConditionCodeImports():
    assert hasattr(scmodel::Transition, "triggerConditionCodeImports")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "triggerConditionCodeImports" in klass.__dict__:
            descriptor = klass.__dict__["triggerConditionCodeImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_messageCheckerConditionLanguage():
    assert hasattr(scmodel::Transition, "messageCheckerConditionLanguage")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "messageCheckerConditionLanguage" in klass.__dict__:
            descriptor = klass.__dict__["messageCheckerConditionLanguage"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_id():
    assert hasattr(scmodel::Transition, "id")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_triggerTimedCode():
    assert hasattr(scmodel::Transition, "triggerTimedCode")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "triggerTimedCode" in klass.__dict__:
            descriptor = klass.__dict__["triggerTimedCode"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_triggerConditionCode():
    assert hasattr(scmodel::Transition, "triggerConditionCode")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "triggerConditionCode" in klass.__dict__:
            descriptor = klass.__dict__["triggerConditionCode"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_uuid():
    assert hasattr(scmodel::Transition, "uuid")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_triggerProbCodeImports():
    assert hasattr(scmodel::Transition, "triggerProbCodeImports")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "triggerProbCodeImports" in klass.__dict__:
            descriptor = klass.__dict__["triggerProbCodeImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_defaultTransition():
    assert hasattr(scmodel::Transition, "defaultTransition")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "defaultTransition" in klass.__dict__:
            descriptor = klass.__dict__["defaultTransition"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_selfTransition():
    assert hasattr(scmodel::Transition, "selfTransition")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "selfTransition" in klass.__dict__:
            descriptor = klass.__dict__["selfTransition"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_messageCheckerClass():
    assert hasattr(scmodel::Transition, "messageCheckerClass")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "messageCheckerClass" in klass.__dict__:
            descriptor = klass.__dict__["messageCheckerClass"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_onTransitionImports():
    assert hasattr(scmodel::Transition, "onTransitionImports")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "onTransitionImports" in klass.__dict__:
            descriptor = klass.__dict__["onTransitionImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_guardImports():
    assert hasattr(scmodel::Transition, "guardImports")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "guardImports" in klass.__dict__:
            descriptor = klass.__dict__["guardImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::transition_has_triggerTime():
    assert hasattr(scmodel::Transition, "triggerTime")
    descriptor = None
    for klass in scmodel::Transition.__mro__:
        if "triggerTime" in klass.__dict__:
            descriptor = klass.__dict__["triggerTime"]
            break
    assert isinstance(descriptor, property)



def test_scmodel::abstractstate_is_not_abstract():
    assert not inspect.isabstract(scmodel::AbstractState)


def test_scmodel::abstractstate_constructor_exists():
    assert callable(scmodel::AbstractState.__init__)


def test_scmodel::abstractstate_constructor_args():
    sig = inspect.signature(scmodel::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "uuid" in params, "Missing parameter 'uuid'"
    assert "id" in params, "Missing parameter 'id'"
    assert "language" in params, "Missing parameter 'language'"
    assert "onExit" in params, "Missing parameter 'onExit'"
    assert "onExitImports" in params, "Missing parameter 'onExitImports'"
    assert "onEnterImports" in params, "Missing parameter 'onEnterImports'"
    assert "onEnter" in params, "Missing parameter 'onEnter'"

def test_scmodel::abstractstate_has_uuid():
    assert hasattr(scmodel::AbstractState, "uuid")
    descriptor = None
    for klass in scmodel::AbstractState.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::abstractstate_has_id():
    assert hasattr(scmodel::AbstractState, "id")
    descriptor = None
    for klass in scmodel::AbstractState.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::abstractstate_has_language():
    assert hasattr(scmodel::AbstractState, "language")
    descriptor = None
    for klass in scmodel::AbstractState.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::abstractstate_has_onExit():
    assert hasattr(scmodel::AbstractState, "onExit")
    descriptor = None
    for klass in scmodel::AbstractState.__mro__:
        if "onExit" in klass.__dict__:
            descriptor = klass.__dict__["onExit"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::abstractstate_has_onExitImports():
    assert hasattr(scmodel::AbstractState, "onExitImports")
    descriptor = None
    for klass in scmodel::AbstractState.__mro__:
        if "onExitImports" in klass.__dict__:
            descriptor = klass.__dict__["onExitImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::abstractstate_has_onEnterImports():
    assert hasattr(scmodel::AbstractState, "onEnterImports")
    descriptor = None
    for klass in scmodel::AbstractState.__mro__:
        if "onEnterImports" in klass.__dict__:
            descriptor = klass.__dict__["onEnterImports"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::abstractstate_has_onEnter():
    assert hasattr(scmodel::AbstractState, "onEnter")
    descriptor = None
    for klass in scmodel::AbstractState.__mro__:
        if "onEnter" in klass.__dict__:
            descriptor = klass.__dict__["onEnter"]
            break
    assert isinstance(descriptor, property)



def test_scmodel::statemachine_is_not_abstract():
    assert not inspect.isabstract(scmodel::StateMachine)


def test_scmodel::statemachine_constructor_exists():
    assert callable(scmodel::StateMachine.__init__)


def test_scmodel::statemachine_constructor_args():
    sig = inspect.signature(scmodel::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "uuid" in params, "Missing parameter 'uuid'"
    assert "className" in params, "Missing parameter 'className'"
    assert "nextID" in params, "Missing parameter 'nextID'"
    assert "id" in params, "Missing parameter 'id'"
    assert "package" in params, "Missing parameter 'package'"
    assert "language" in params, "Missing parameter 'language'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "agentType" in params, "Missing parameter 'agentType'"

def test_scmodel::statemachine_has_uuid():
    assert hasattr(scmodel::StateMachine, "uuid")
    descriptor = None
    for klass in scmodel::StateMachine.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::statemachine_has_className():
    assert hasattr(scmodel::StateMachine, "className")
    descriptor = None
    for klass in scmodel::StateMachine.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::statemachine_has_nextID():
    assert hasattr(scmodel::StateMachine, "nextID")
    descriptor = None
    for klass in scmodel::StateMachine.__mro__:
        if "nextID" in klass.__dict__:
            descriptor = klass.__dict__["nextID"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::statemachine_has_id():
    assert hasattr(scmodel::StateMachine, "id")
    descriptor = None
    for klass in scmodel::StateMachine.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::statemachine_has_package():
    assert hasattr(scmodel::StateMachine, "package")
    descriptor = None
    for klass in scmodel::StateMachine.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::statemachine_has_language():
    assert hasattr(scmodel::StateMachine, "language")
    descriptor = None
    for klass in scmodel::StateMachine.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::statemachine_has_priority():
    assert hasattr(scmodel::StateMachine, "priority")
    descriptor = None
    for klass in scmodel::StateMachine.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_scmodel::statemachine_has_agentType():
    assert hasattr(scmodel::StateMachine, "agentType")
    descriptor = None
    for klass in scmodel::StateMachine.__mro__:
        if "agentType" in klass.__dict__:
            descriptor = klass.__dict__["agentType"]
            break
    assert isinstance(descriptor, property)

def test_triggertypes_exists():
    # Check that the Enumeration exists
    assert TriggerTypes is not None

def test_triggertypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriggerTypes]
    expected_literals = [
        "timed",
        "exponential",
        "condition",
        "message",
        "always",
        "probability",
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
        "choice",
        "initial",
        "entry",
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
        "groovy",
        "relogo",
        "java",
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
        "always",
        "conditional",
        "equals",
        "unconditional",
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
State_strategy = st.builds(
    State,
)
scmodel::History_strategy = st.builds(
    scmodel::History,
    shallow=
        st.booleans()
)
scmodel::FinalState_strategy = st.builds(
    scmodel::FinalState,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
scmodel::PseudoState_strategy = st.builds(
    scmodel::PseudoState,
    type=
        safe_text
)
scmodel::CompositeState_strategy = st.builds(
    scmodel::CompositeState,
)
scmodel::State_strategy = st.builds(
    scmodel::State,
)
scmodel::Transition_strategy = st.builds(
    scmodel::Transition,
    messageCheckerCodeImports=
        safe_text,
    triggerExpRateCodeImports=
        safe_text,
    messageCheckerCode=
        safe_text,
    outOfBranch=
        st.booleans(),
    triggerType=
        safe_text,
    priority=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    guard=
        safe_text,
    triggerCodeLanguage=
        safe_text,
    triggerProbCode=
        safe_text,
    triggerExpRateCode=
        safe_text,
    triggerTimedCodeImports=
        safe_text,
    onTransition=
        safe_text,
    messageCheckerType=
        safe_text,
    triggerConditionCodeImports=
        safe_text,
    messageCheckerConditionLanguage=
        safe_text,
    id=
        safe_text,
    triggerTimedCode=
        safe_text,
    triggerConditionCode=
        safe_text,
    uuid=
        safe_text,
    triggerProbCodeImports=
        safe_text,
    defaultTransition=
        st.booleans(),
    selfTransition=
        st.booleans(),
    messageCheckerClass=
        safe_text,
    onTransitionImports=
        safe_text,
    guardImports=
        safe_text,
    triggerTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
scmodel::AbstractState_strategy = st.builds(
    scmodel::AbstractState,
    uuid=
        safe_text,
    id=
        safe_text,
    language=
        safe_text,
    onExit=
        safe_text,
    onExitImports=
        safe_text,
    onEnterImports=
        safe_text,
    onEnter=
        safe_text
)
scmodel::StateMachine_strategy = st.builds(
    scmodel::StateMachine,
    uuid=
        safe_text,
    className=
        safe_text,
    nextID=
        st.integers(),
    id=
        safe_text,
    package=
        safe_text,
    language=
        safe_text,
    priority=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    agentType=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=scmodel::History_strategy)
@settings(max_examples=50)
def test_scmodel::history_instantiation(instance):
    assert isinstance(instance, scmodel::History)

@given(instance=scmodel::History_strategy)
def test_scmodel::history_shallow_type(instance):
    assert isinstance(instance.shallow, bool)


@given(instance=scmodel::History_strategy)
def test_scmodel::history_shallow_setter(instance):
    original = instance.shallow
    instance.shallow = original
    assert instance.shallow == original

@given(instance=scmodel::FinalState_strategy)
@settings(max_examples=50)
def test_scmodel::finalstate_instantiation(instance):
    assert isinstance(instance, scmodel::FinalState)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=scmodel::PseudoState_strategy)
@settings(max_examples=50)
def test_scmodel::pseudostate_instantiation(instance):
    assert isinstance(instance, scmodel::PseudoState)

@given(instance=scmodel::PseudoState_strategy)
def test_scmodel::pseudostate_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scmodel::PseudoState_strategy)
def test_scmodel::pseudostate_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scmodel::CompositeState_strategy)
@settings(max_examples=50)
def test_scmodel::compositestate_instantiation(instance):
    assert isinstance(instance, scmodel::CompositeState)

@given(instance=scmodel::State_strategy)
@settings(max_examples=50)
def test_scmodel::state_instantiation(instance):
    assert isinstance(instance, scmodel::State)

@given(instance=scmodel::Transition_strategy)
@settings(max_examples=50)
def test_scmodel::transition_instantiation(instance):
    assert isinstance(instance, scmodel::Transition)

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_messageCheckerCodeImports_type(instance):
    assert isinstance(instance.messageCheckerCodeImports, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_messageCheckerCodeImports_setter(instance):
    original = instance.messageCheckerCodeImports
    instance.messageCheckerCodeImports = original
    assert instance.messageCheckerCodeImports == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerExpRateCodeImports_type(instance):
    assert isinstance(instance.triggerExpRateCodeImports, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerExpRateCodeImports_setter(instance):
    original = instance.triggerExpRateCodeImports
    instance.triggerExpRateCodeImports = original
    assert instance.triggerExpRateCodeImports == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_messageCheckerCode_type(instance):
    assert isinstance(instance.messageCheckerCode, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_messageCheckerCode_setter(instance):
    original = instance.messageCheckerCode
    instance.messageCheckerCode = original
    assert instance.messageCheckerCode == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_outOfBranch_type(instance):
    assert isinstance(instance.outOfBranch, bool)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_outOfBranch_setter(instance):
    original = instance.outOfBranch
    instance.outOfBranch = original
    assert instance.outOfBranch == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerType_type(instance):
    assert isinstance(instance.triggerType, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerType_setter(instance):
    original = instance.triggerType
    instance.triggerType = original
    assert instance.triggerType == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_priority_type(instance):
    assert isinstance(instance.priority, float)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerCodeLanguage_type(instance):
    assert isinstance(instance.triggerCodeLanguage, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerCodeLanguage_setter(instance):
    original = instance.triggerCodeLanguage
    instance.triggerCodeLanguage = original
    assert instance.triggerCodeLanguage == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerProbCode_type(instance):
    assert isinstance(instance.triggerProbCode, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerProbCode_setter(instance):
    original = instance.triggerProbCode
    instance.triggerProbCode = original
    assert instance.triggerProbCode == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerExpRateCode_type(instance):
    assert isinstance(instance.triggerExpRateCode, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerExpRateCode_setter(instance):
    original = instance.triggerExpRateCode
    instance.triggerExpRateCode = original
    assert instance.triggerExpRateCode == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerTimedCodeImports_type(instance):
    assert isinstance(instance.triggerTimedCodeImports, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerTimedCodeImports_setter(instance):
    original = instance.triggerTimedCodeImports
    instance.triggerTimedCodeImports = original
    assert instance.triggerTimedCodeImports == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_onTransition_type(instance):
    assert isinstance(instance.onTransition, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_onTransition_setter(instance):
    original = instance.onTransition
    instance.onTransition = original
    assert instance.onTransition == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_messageCheckerType_type(instance):
    assert isinstance(instance.messageCheckerType, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_messageCheckerType_setter(instance):
    original = instance.messageCheckerType
    instance.messageCheckerType = original
    assert instance.messageCheckerType == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerConditionCodeImports_type(instance):
    assert isinstance(instance.triggerConditionCodeImports, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerConditionCodeImports_setter(instance):
    original = instance.triggerConditionCodeImports
    instance.triggerConditionCodeImports = original
    assert instance.triggerConditionCodeImports == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_messageCheckerConditionLanguage_type(instance):
    assert isinstance(instance.messageCheckerConditionLanguage, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_messageCheckerConditionLanguage_setter(instance):
    original = instance.messageCheckerConditionLanguage
    instance.messageCheckerConditionLanguage = original
    assert instance.messageCheckerConditionLanguage == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerTimedCode_type(instance):
    assert isinstance(instance.triggerTimedCode, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerTimedCode_setter(instance):
    original = instance.triggerTimedCode
    instance.triggerTimedCode = original
    assert instance.triggerTimedCode == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerConditionCode_type(instance):
    assert isinstance(instance.triggerConditionCode, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerConditionCode_setter(instance):
    original = instance.triggerConditionCode
    instance.triggerConditionCode = original
    assert instance.triggerConditionCode == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_uuid_type(instance):
    assert isinstance(instance.uuid, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerProbCodeImports_type(instance):
    assert isinstance(instance.triggerProbCodeImports, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerProbCodeImports_setter(instance):
    original = instance.triggerProbCodeImports
    instance.triggerProbCodeImports = original
    assert instance.triggerProbCodeImports == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_defaultTransition_type(instance):
    assert isinstance(instance.defaultTransition, bool)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_defaultTransition_setter(instance):
    original = instance.defaultTransition
    instance.defaultTransition = original
    assert instance.defaultTransition == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_selfTransition_type(instance):
    assert isinstance(instance.selfTransition, bool)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_selfTransition_setter(instance):
    original = instance.selfTransition
    instance.selfTransition = original
    assert instance.selfTransition == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_messageCheckerClass_type(instance):
    assert isinstance(instance.messageCheckerClass, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_messageCheckerClass_setter(instance):
    original = instance.messageCheckerClass
    instance.messageCheckerClass = original
    assert instance.messageCheckerClass == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_onTransitionImports_type(instance):
    assert isinstance(instance.onTransitionImports, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_onTransitionImports_setter(instance):
    original = instance.onTransitionImports
    instance.onTransitionImports = original
    assert instance.onTransitionImports == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_guardImports_type(instance):
    assert isinstance(instance.guardImports, str)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_guardImports_setter(instance):
    original = instance.guardImports
    instance.guardImports = original
    assert instance.guardImports == original

@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerTime_type(instance):
    assert isinstance(instance.triggerTime, float)


@given(instance=scmodel::Transition_strategy)
def test_scmodel::transition_triggerTime_setter(instance):
    original = instance.triggerTime
    instance.triggerTime = original
    assert instance.triggerTime == original

@given(instance=scmodel::AbstractState_strategy)
@settings(max_examples=50)
def test_scmodel::abstractstate_instantiation(instance):
    assert isinstance(instance, scmodel::AbstractState)

@given(instance=scmodel::AbstractState_strategy)
def test_scmodel::abstractstate_uuid_type(instance):
    assert isinstance(instance.uuid, str)


@given(instance=scmodel::AbstractState_strategy)
def test_scmodel::abstractstate_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original

@given(instance=scmodel::AbstractState_strategy)
def test_scmodel::abstractstate_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scmodel::AbstractState_strategy)
def test_scmodel::abstractstate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scmodel::AbstractState_strategy)
def test_scmodel::abstractstate_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=scmodel::AbstractState_strategy)
def test_scmodel::abstractstate_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=scmodel::AbstractState_strategy)
def test_scmodel::abstractstate_onExit_type(instance):
    assert isinstance(instance.onExit, str)


@given(instance=scmodel::AbstractState_strategy)
def test_scmodel::abstractstate_onExit_setter(instance):
    original = instance.onExit
    instance.onExit = original
    assert instance.onExit == original

@given(instance=scmodel::AbstractState_strategy)
def test_scmodel::abstractstate_onExitImports_type(instance):
    assert isinstance(instance.onExitImports, str)


@given(instance=scmodel::AbstractState_strategy)
def test_scmodel::abstractstate_onExitImports_setter(instance):
    original = instance.onExitImports
    instance.onExitImports = original
    assert instance.onExitImports == original

@given(instance=scmodel::AbstractState_strategy)
def test_scmodel::abstractstate_onEnterImports_type(instance):
    assert isinstance(instance.onEnterImports, str)


@given(instance=scmodel::AbstractState_strategy)
def test_scmodel::abstractstate_onEnterImports_setter(instance):
    original = instance.onEnterImports
    instance.onEnterImports = original
    assert instance.onEnterImports == original

@given(instance=scmodel::AbstractState_strategy)
def test_scmodel::abstractstate_onEnter_type(instance):
    assert isinstance(instance.onEnter, str)


@given(instance=scmodel::AbstractState_strategy)
def test_scmodel::abstractstate_onEnter_setter(instance):
    original = instance.onEnter
    instance.onEnter = original
    assert instance.onEnter == original

@given(instance=scmodel::StateMachine_strategy)
@settings(max_examples=50)
def test_scmodel::statemachine_instantiation(instance):
    assert isinstance(instance, scmodel::StateMachine)

@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_uuid_type(instance):
    assert isinstance(instance.uuid, str)


@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original

@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_nextID_type(instance):
    assert isinstance(instance.nextID, int)


@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_nextID_setter(instance):
    original = instance.nextID
    instance.nextID = original
    assert instance.nextID == original

@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_priority_type(instance):
    assert isinstance(instance.priority, float)


@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_agentType_type(instance):
    assert isinstance(instance.agentType, str)


@given(instance=scmodel::StateMachine_strategy)
def test_scmodel::statemachine_agentType_setter(instance):
    original = instance.agentType
    instance.agentType = original
    assert instance.agentType == original
