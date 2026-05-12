import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    HSM::AssociationDataStateBase,
    HSM::AssociationStateState,
    AndState,
    Transition,
    StateDataRelation,
    PrimitiveState,
    HSM::State,
    HSM::StateDataRelation,
    HSM::Init,
    Init,
    State,
    CompoundState,
    HSM::AndState,
    HSM::OrState,
    RootFolder,
    HSM::RootFolder,
    OrState,
    StateBase,
    HSM::PrimitiveState,
    HSM::CompoundState,
    AssociationDataStateBase,
    DataVar,
    AssociationStateState,
    MgaObject,
    HSM::StateDateRelation,
    HSM::Transition,
    HSM::StateBase,
    HSM::DataVar,
    HSM::MgaObject,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hsm::associationdatastatebase_is_not_abstract():
    assert not inspect.isabstract(HSM::AssociationDataStateBase)


def test_hsm::associationdatastatebase_constructor_exists():
    assert callable(HSM::AssociationDataStateBase.__init__)


def test_hsm::associationdatastatebase_constructor_args():
    sig = inspect.signature(HSM::AssociationDataStateBase.__init__)
    params = list(sig.parameters.keys())



def test_hsm::associationstatestate_is_not_abstract():
    assert not inspect.isabstract(HSM::AssociationStateState)


def test_hsm::associationstatestate_constructor_exists():
    assert callable(HSM::AssociationStateState.__init__)


def test_hsm::associationstatestate_constructor_args():
    sig = inspect.signature(HSM::AssociationStateState.__init__)
    params = list(sig.parameters.keys())



def test_andstate_is_not_abstract():
    assert not inspect.isabstract(AndState)


def test_andstate_constructor_exists():
    assert callable(AndState.__init__)


def test_andstate_constructor_args():
    sig = inspect.signature(AndState.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_statedatarelation_is_not_abstract():
    assert not inspect.isabstract(StateDataRelation)


def test_statedatarelation_constructor_exists():
    assert callable(StateDataRelation.__init__)


def test_statedatarelation_constructor_args():
    sig = inspect.signature(StateDataRelation.__init__)
    params = list(sig.parameters.keys())



def test_primitivestate_is_not_abstract():
    assert not inspect.isabstract(PrimitiveState)


def test_primitivestate_constructor_exists():
    assert callable(PrimitiveState.__init__)


def test_primitivestate_constructor_args():
    sig = inspect.signature(PrimitiveState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::state_is_not_abstract():
    assert not inspect.isabstract(HSM::State)


def test_hsm::state_constructor_exists():
    assert callable(HSM::State.__init__)


def test_hsm::state_constructor_args():
    sig = inspect.signature(HSM::State.__init__)
    params = list(sig.parameters.keys())



def test_hsm::statedatarelation_is_not_abstract():
    assert not inspect.isabstract(HSM::StateDataRelation)


def test_hsm::statedatarelation_constructor_exists():
    assert callable(HSM::StateDataRelation.__init__)


def test_hsm::statedatarelation_constructor_args():
    sig = inspect.signature(HSM::StateDataRelation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "color" in params, "Missing parameter 'color'"

def test_hsm::statedatarelation_has_value():
    assert hasattr(HSM::StateDataRelation, "value")
    descriptor = None
    for klass in HSM::StateDataRelation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_hsm::statedatarelation_has_color():
    assert hasattr(HSM::StateDataRelation, "color")
    descriptor = None
    for klass in HSM::StateDataRelation.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_hsm::init_is_not_abstract():
    assert not inspect.isabstract(HSM::Init)


def test_hsm::init_constructor_exists():
    assert callable(HSM::Init.__init__)


def test_hsm::init_constructor_args():
    sig = inspect.signature(HSM::Init.__init__)
    params = list(sig.parameters.keys())



def test_init_is_not_abstract():
    assert not inspect.isabstract(Init)


def test_init_constructor_exists():
    assert callable(Init.__init__)


def test_init_constructor_args():
    sig = inspect.signature(Init.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_compoundstate_is_not_abstract():
    assert not inspect.isabstract(CompoundState)


def test_compoundstate_constructor_exists():
    assert callable(CompoundState.__init__)


def test_compoundstate_constructor_args():
    sig = inspect.signature(CompoundState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::andstate_is_not_abstract():
    assert not inspect.isabstract(HSM::AndState)


def test_hsm::andstate_constructor_exists():
    assert callable(HSM::AndState.__init__)


def test_hsm::andstate_constructor_args():
    sig = inspect.signature(HSM::AndState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::orstate_is_not_abstract():
    assert not inspect.isabstract(HSM::OrState)


def test_hsm::orstate_constructor_exists():
    assert callable(HSM::OrState.__init__)


def test_hsm::orstate_constructor_args():
    sig = inspect.signature(HSM::OrState.__init__)
    params = list(sig.parameters.keys())



def test_rootfolder_is_not_abstract():
    assert not inspect.isabstract(RootFolder)


def test_rootfolder_constructor_exists():
    assert callable(RootFolder.__init__)


def test_rootfolder_constructor_args():
    sig = inspect.signature(RootFolder.__init__)
    params = list(sig.parameters.keys())



def test_hsm::rootfolder_is_not_abstract():
    assert not inspect.isabstract(HSM::RootFolder)


def test_hsm::rootfolder_constructor_exists():
    assert callable(HSM::RootFolder.__init__)


def test_hsm::rootfolder_constructor_args():
    sig = inspect.signature(HSM::RootFolder.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm::rootfolder_has_name():
    assert hasattr(HSM::RootFolder, "name")
    descriptor = None
    for klass in HSM::RootFolder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_orstate_is_not_abstract():
    assert not inspect.isabstract(OrState)


def test_orstate_constructor_exists():
    assert callable(OrState.__init__)


def test_orstate_constructor_args():
    sig = inspect.signature(OrState.__init__)
    params = list(sig.parameters.keys())



def test_statebase_is_not_abstract():
    assert not inspect.isabstract(StateBase)


def test_statebase_constructor_exists():
    assert callable(StateBase.__init__)


def test_statebase_constructor_args():
    sig = inspect.signature(StateBase.__init__)
    params = list(sig.parameters.keys())



def test_hsm::primitivestate_is_not_abstract():
    assert not inspect.isabstract(HSM::PrimitiveState)


def test_hsm::primitivestate_constructor_exists():
    assert callable(HSM::PrimitiveState.__init__)


def test_hsm::primitivestate_constructor_args():
    sig = inspect.signature(HSM::PrimitiveState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::compoundstate_is_not_abstract():
    assert not inspect.isabstract(HSM::CompoundState)


def test_hsm::compoundstate_constructor_exists():
    assert callable(HSM::CompoundState.__init__)


def test_hsm::compoundstate_constructor_args():
    sig = inspect.signature(HSM::CompoundState.__init__)
    params = list(sig.parameters.keys())



def test_associationdatastatebase_is_not_abstract():
    assert not inspect.isabstract(AssociationDataStateBase)


def test_associationdatastatebase_constructor_exists():
    assert callable(AssociationDataStateBase.__init__)


def test_associationdatastatebase_constructor_args():
    sig = inspect.signature(AssociationDataStateBase.__init__)
    params = list(sig.parameters.keys())



def test_datavar_is_not_abstract():
    assert not inspect.isabstract(DataVar)


def test_datavar_constructor_exists():
    assert callable(DataVar.__init__)


def test_datavar_constructor_args():
    sig = inspect.signature(DataVar.__init__)
    params = list(sig.parameters.keys())



def test_associationstatestate_is_not_abstract():
    assert not inspect.isabstract(AssociationStateState)


def test_associationstatestate_constructor_exists():
    assert callable(AssociationStateState.__init__)


def test_associationstatestate_constructor_args():
    sig = inspect.signature(AssociationStateState.__init__)
    params = list(sig.parameters.keys())



def test_mgaobject_is_not_abstract():
    assert not inspect.isabstract(MgaObject)


def test_mgaobject_constructor_exists():
    assert callable(MgaObject.__init__)


def test_mgaobject_constructor_args():
    sig = inspect.signature(MgaObject.__init__)
    params = list(sig.parameters.keys())



def test_hsm::statedaterelation_is_not_abstract():
    assert not inspect.isabstract(HSM::StateDateRelation)


def test_hsm::statedaterelation_constructor_exists():
    assert callable(HSM::StateDateRelation.__init__)


def test_hsm::statedaterelation_constructor_args():
    sig = inspect.signature(HSM::StateDateRelation.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "value" in params, "Missing parameter 'value'"

def test_hsm::statedaterelation_has_color():
    assert hasattr(HSM::StateDateRelation, "color")
    descriptor = None
    for klass in HSM::StateDateRelation.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_hsm::statedaterelation_has_value():
    assert hasattr(HSM::StateDateRelation, "value")
    descriptor = None
    for klass in HSM::StateDateRelation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hsm::transition_is_not_abstract():
    assert not inspect.isabstract(HSM::Transition)


def test_hsm::transition_constructor_exists():
    assert callable(HSM::Transition.__init__)


def test_hsm::transition_constructor_args():
    sig = inspect.signature(HSM::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "isSync" in params, "Missing parameter 'isSync'"
    assert "guard" in params, "Missing parameter 'guard'"

def test_hsm::transition_has_action():
    assert hasattr(HSM::Transition, "action")
    descriptor = None
    for klass in HSM::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_hsm::transition_has_trigger():
    assert hasattr(HSM::Transition, "trigger")
    descriptor = None
    for klass in HSM::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_hsm::transition_has_isSync():
    assert hasattr(HSM::Transition, "isSync")
    descriptor = None
    for klass in HSM::Transition.__mro__:
        if "isSync" in klass.__dict__:
            descriptor = klass.__dict__["isSync"]
            break
    assert isinstance(descriptor, property)

def test_hsm::transition_has_guard():
    assert hasattr(HSM::Transition, "guard")
    descriptor = None
    for klass in HSM::Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_hsm::statebase_is_not_abstract():
    assert not inspect.isabstract(HSM::StateBase)


def test_hsm::statebase_constructor_exists():
    assert callable(HSM::StateBase.__init__)


def test_hsm::statebase_constructor_args():
    sig = inspect.signature(HSM::StateBase.__init__)
    params = list(sig.parameters.keys())
    assert "marked" in params, "Missing parameter 'marked'"
    assert "defaultTransition" in params, "Missing parameter 'defaultTransition'"

def test_hsm::statebase_has_marked():
    assert hasattr(HSM::StateBase, "marked")
    descriptor = None
    for klass in HSM::StateBase.__mro__:
        if "marked" in klass.__dict__:
            descriptor = klass.__dict__["marked"]
            break
    assert isinstance(descriptor, property)

def test_hsm::statebase_has_defaultTransition():
    assert hasattr(HSM::StateBase, "defaultTransition")
    descriptor = None
    for klass in HSM::StateBase.__mro__:
        if "defaultTransition" in klass.__dict__:
            descriptor = klass.__dict__["defaultTransition"]
            break
    assert isinstance(descriptor, property)



def test_hsm::datavar_is_not_abstract():
    assert not inspect.isabstract(HSM::DataVar)


def test_hsm::datavar_constructor_exists():
    assert callable(HSM::DataVar.__init__)


def test_hsm::datavar_constructor_args():
    sig = inspect.signature(HSM::DataVar.__init__)
    params = list(sig.parameters.keys())



def test_hsm::mgaobject_is_not_abstract():
    assert not inspect.isabstract(HSM::MgaObject)


def test_hsm::mgaobject_constructor_exists():
    assert callable(HSM::MgaObject.__init__)


def test_hsm::mgaobject_constructor_args():
    sig = inspect.signature(HSM::MgaObject.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "name" in params, "Missing parameter 'name'"

def test_hsm::mgaobject_has_position():
    assert hasattr(HSM::MgaObject, "position")
    descriptor = None
    for klass in HSM::MgaObject.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_hsm::mgaobject_has_name():
    assert hasattr(HSM::MgaObject, "name")
    descriptor = None
    for klass in HSM::MgaObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
HSM::AssociationDataStateBase_strategy = st.builds(
    HSM::AssociationDataStateBase,
)
HSM::AssociationStateState_strategy = st.builds(
    HSM::AssociationStateState,
)
AndState_strategy = st.builds(
    AndState,
)
Transition_strategy = st.builds(
    Transition,
)
StateDataRelation_strategy = st.builds(
    StateDataRelation,
)
PrimitiveState_strategy = st.builds(
    PrimitiveState,
)
HSM::State_strategy = st.builds(
    HSM::State,
)
HSM::StateDataRelation_strategy = st.builds(
    HSM::StateDataRelation,
    value=
        safe_text,
    color=
        safe_text
)
HSM::Init_strategy = st.builds(
    HSM::Init,
)
Init_strategy = st.builds(
    Init,
)
State_strategy = st.builds(
    State,
)
CompoundState_strategy = st.builds(
    CompoundState,
)
HSM::AndState_strategy = st.builds(
    HSM::AndState,
)
HSM::OrState_strategy = st.builds(
    HSM::OrState,
)
RootFolder_strategy = st.builds(
    RootFolder,
)
HSM::RootFolder_strategy = st.builds(
    HSM::RootFolder,
    name=
        safe_text
)
OrState_strategy = st.builds(
    OrState,
)
StateBase_strategy = st.builds(
    StateBase,
)
HSM::PrimitiveState_strategy = st.builds(
    HSM::PrimitiveState,
)
HSM::CompoundState_strategy = st.builds(
    HSM::CompoundState,
)
AssociationDataStateBase_strategy = st.builds(
    AssociationDataStateBase,
)
DataVar_strategy = st.builds(
    DataVar,
)
AssociationStateState_strategy = st.builds(
    AssociationStateState,
)
MgaObject_strategy = st.builds(
    MgaObject,
)
HSM::StateDateRelation_strategy = st.builds(
    HSM::StateDateRelation,
    color=
        safe_text,
    value=
        safe_text
)
HSM::Transition_strategy = st.builds(
    HSM::Transition,
    action=
        safe_text,
    trigger=
        safe_text,
    isSync=
        safe_text,
    guard=
        safe_text
)
HSM::StateBase_strategy = st.builds(
    HSM::StateBase,
    marked=
        safe_text,
    defaultTransition=
        safe_text
)
HSM::DataVar_strategy = st.builds(
    HSM::DataVar,
)
HSM::MgaObject_strategy = st.builds(
    HSM::MgaObject,
    position=
        safe_text,
    name=
        safe_text
)

@given(instance=HSM::AssociationDataStateBase_strategy)
@settings(max_examples=50)
def test_hsm::associationdatastatebase_instantiation(instance):
    assert isinstance(instance, HSM::AssociationDataStateBase)

@given(instance=HSM::AssociationStateState_strategy)
@settings(max_examples=50)
def test_hsm::associationstatestate_instantiation(instance):
    assert isinstance(instance, HSM::AssociationStateState)

@given(instance=AndState_strategy)
@settings(max_examples=50)
def test_andstate_instantiation(instance):
    assert isinstance(instance, AndState)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=StateDataRelation_strategy)
@settings(max_examples=50)
def test_statedatarelation_instantiation(instance):
    assert isinstance(instance, StateDataRelation)

@given(instance=PrimitiveState_strategy)
@settings(max_examples=50)
def test_primitivestate_instantiation(instance):
    assert isinstance(instance, PrimitiveState)

@given(instance=HSM::State_strategy)
@settings(max_examples=50)
def test_hsm::state_instantiation(instance):
    assert isinstance(instance, HSM::State)

@given(instance=HSM::StateDataRelation_strategy)
@settings(max_examples=50)
def test_hsm::statedatarelation_instantiation(instance):
    assert isinstance(instance, HSM::StateDataRelation)

@given(instance=HSM::StateDataRelation_strategy)
def test_hsm::statedatarelation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=HSM::StateDataRelation_strategy)
def test_hsm::statedatarelation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HSM::StateDataRelation_strategy)
def test_hsm::statedatarelation_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=HSM::StateDataRelation_strategy)
def test_hsm::statedatarelation_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=HSM::Init_strategy)
@settings(max_examples=50)
def test_hsm::init_instantiation(instance):
    assert isinstance(instance, HSM::Init)

@given(instance=Init_strategy)
@settings(max_examples=50)
def test_init_instantiation(instance):
    assert isinstance(instance, Init)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=CompoundState_strategy)
@settings(max_examples=50)
def test_compoundstate_instantiation(instance):
    assert isinstance(instance, CompoundState)

@given(instance=HSM::AndState_strategy)
@settings(max_examples=50)
def test_hsm::andstate_instantiation(instance):
    assert isinstance(instance, HSM::AndState)

@given(instance=HSM::OrState_strategy)
@settings(max_examples=50)
def test_hsm::orstate_instantiation(instance):
    assert isinstance(instance, HSM::OrState)

@given(instance=RootFolder_strategy)
@settings(max_examples=50)
def test_rootfolder_instantiation(instance):
    assert isinstance(instance, RootFolder)

@given(instance=HSM::RootFolder_strategy)
@settings(max_examples=50)
def test_hsm::rootfolder_instantiation(instance):
    assert isinstance(instance, HSM::RootFolder)

@given(instance=HSM::RootFolder_strategy)
def test_hsm::rootfolder_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HSM::RootFolder_strategy)
def test_hsm::rootfolder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OrState_strategy)
@settings(max_examples=50)
def test_orstate_instantiation(instance):
    assert isinstance(instance, OrState)

@given(instance=StateBase_strategy)
@settings(max_examples=50)
def test_statebase_instantiation(instance):
    assert isinstance(instance, StateBase)

@given(instance=HSM::PrimitiveState_strategy)
@settings(max_examples=50)
def test_hsm::primitivestate_instantiation(instance):
    assert isinstance(instance, HSM::PrimitiveState)

@given(instance=HSM::CompoundState_strategy)
@settings(max_examples=50)
def test_hsm::compoundstate_instantiation(instance):
    assert isinstance(instance, HSM::CompoundState)

@given(instance=AssociationDataStateBase_strategy)
@settings(max_examples=50)
def test_associationdatastatebase_instantiation(instance):
    assert isinstance(instance, AssociationDataStateBase)

@given(instance=DataVar_strategy)
@settings(max_examples=50)
def test_datavar_instantiation(instance):
    assert isinstance(instance, DataVar)

@given(instance=AssociationStateState_strategy)
@settings(max_examples=50)
def test_associationstatestate_instantiation(instance):
    assert isinstance(instance, AssociationStateState)

@given(instance=MgaObject_strategy)
@settings(max_examples=50)
def test_mgaobject_instantiation(instance):
    assert isinstance(instance, MgaObject)

@given(instance=HSM::StateDateRelation_strategy)
@settings(max_examples=50)
def test_hsm::statedaterelation_instantiation(instance):
    assert isinstance(instance, HSM::StateDateRelation)

@given(instance=HSM::StateDateRelation_strategy)
def test_hsm::statedaterelation_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=HSM::StateDateRelation_strategy)
def test_hsm::statedaterelation_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=HSM::StateDateRelation_strategy)
def test_hsm::statedaterelation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=HSM::StateDateRelation_strategy)
def test_hsm::statedaterelation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HSM::Transition_strategy)
@settings(max_examples=50)
def test_hsm::transition_instantiation(instance):
    assert isinstance(instance, HSM::Transition)

@given(instance=HSM::Transition_strategy)
def test_hsm::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=HSM::Transition_strategy)
def test_hsm::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=HSM::Transition_strategy)
def test_hsm::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=HSM::Transition_strategy)
def test_hsm::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=HSM::Transition_strategy)
def test_hsm::transition_isSync_type(instance):
    assert isinstance(instance.isSync, str)


@given(instance=HSM::Transition_strategy)
def test_hsm::transition_isSync_setter(instance):
    original = instance.isSync
    instance.isSync = original
    assert instance.isSync == original

@given(instance=HSM::Transition_strategy)
def test_hsm::transition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=HSM::Transition_strategy)
def test_hsm::transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=HSM::StateBase_strategy)
@settings(max_examples=50)
def test_hsm::statebase_instantiation(instance):
    assert isinstance(instance, HSM::StateBase)

@given(instance=HSM::StateBase_strategy)
def test_hsm::statebase_marked_type(instance):
    assert isinstance(instance.marked, str)


@given(instance=HSM::StateBase_strategy)
def test_hsm::statebase_marked_setter(instance):
    original = instance.marked
    instance.marked = original
    assert instance.marked == original

@given(instance=HSM::StateBase_strategy)
def test_hsm::statebase_defaultTransition_type(instance):
    assert isinstance(instance.defaultTransition, str)


@given(instance=HSM::StateBase_strategy)
def test_hsm::statebase_defaultTransition_setter(instance):
    original = instance.defaultTransition
    instance.defaultTransition = original
    assert instance.defaultTransition == original

@given(instance=HSM::DataVar_strategy)
@settings(max_examples=50)
def test_hsm::datavar_instantiation(instance):
    assert isinstance(instance, HSM::DataVar)

@given(instance=HSM::MgaObject_strategy)
@settings(max_examples=50)
def test_hsm::mgaobject_instantiation(instance):
    assert isinstance(instance, HSM::MgaObject)

@given(instance=HSM::MgaObject_strategy)
def test_hsm::mgaobject_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=HSM::MgaObject_strategy)
def test_hsm::mgaobject_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=HSM::MgaObject_strategy)
def test_hsm::mgaobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HSM::MgaObject_strategy)
def test_hsm::mgaobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
