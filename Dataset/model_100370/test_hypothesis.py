import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    HSM_AssociationDataStateBase,
    HSM_AssociationStateState,
    AndState,
    Transition,
    StateDataRelation,
    PrimitiveState,
    HSM_StateDataRelation,
    HSM_State,
    HSM_Init,
    Init,
    State,
    CompoundState,
    HSM_AndState,
    HSM_OrState,
    RootFolder,
    HSM_RootFolder,
    OrState,
    StateBase,
    HSM_CompoundState,
    HSM_PrimitiveState,
    AssociationDataStateBase,
    DataVar,
    AssociationStateState,
    MgaObject,
    HSM_Transition,
    HSM_StateDateRelation,
    HSM_StateBase,
    HSM_DataVar,
    HSM_MgaObject,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hsm_associationdatastatebase_is_not_abstract():
    assert not inspect.isabstract(HSM_AssociationDataStateBase)


def test_hsm_associationdatastatebase_constructor_exists():
    assert callable(HSM_AssociationDataStateBase.__init__)


def test_hsm_associationdatastatebase_constructor_args():
    sig = inspect.signature(HSM_AssociationDataStateBase.__init__)
    params = list(sig.parameters.keys())



def test_hsm_associationstatestate_is_not_abstract():
    assert not inspect.isabstract(HSM_AssociationStateState)


def test_hsm_associationstatestate_constructor_exists():
    assert callable(HSM_AssociationStateState.__init__)


def test_hsm_associationstatestate_constructor_args():
    sig = inspect.signature(HSM_AssociationStateState.__init__)
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



def test_hsm_statedatarelation_is_not_abstract():
    assert not inspect.isabstract(HSM_StateDataRelation)


def test_hsm_statedatarelation_constructor_exists():
    assert callable(HSM_StateDataRelation.__init__)


def test_hsm_statedatarelation_constructor_args():
    sig = inspect.signature(HSM_StateDataRelation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "color" in params, "Missing parameter 'color'"

def test_hsm_statedatarelation_has_value():
    assert hasattr(HSM_StateDataRelation, "value")
    descriptor = None
    for klass in HSM_StateDataRelation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_hsm_statedatarelation_has_color():
    assert hasattr(HSM_StateDataRelation, "color")
    descriptor = None
    for klass in HSM_StateDataRelation.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_hsm_state_is_not_abstract():
    assert not inspect.isabstract(HSM_State)


def test_hsm_state_constructor_exists():
    assert callable(HSM_State.__init__)


def test_hsm_state_constructor_args():
    sig = inspect.signature(HSM_State.__init__)
    params = list(sig.parameters.keys())



def test_hsm_init_is_not_abstract():
    assert not inspect.isabstract(HSM_Init)


def test_hsm_init_constructor_exists():
    assert callable(HSM_Init.__init__)


def test_hsm_init_constructor_args():
    sig = inspect.signature(HSM_Init.__init__)
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



def test_hsm_andstate_is_not_abstract():
    assert not inspect.isabstract(HSM_AndState)


def test_hsm_andstate_constructor_exists():
    assert callable(HSM_AndState.__init__)


def test_hsm_andstate_constructor_args():
    sig = inspect.signature(HSM_AndState.__init__)
    params = list(sig.parameters.keys())



def test_hsm_orstate_is_not_abstract():
    assert not inspect.isabstract(HSM_OrState)


def test_hsm_orstate_constructor_exists():
    assert callable(HSM_OrState.__init__)


def test_hsm_orstate_constructor_args():
    sig = inspect.signature(HSM_OrState.__init__)
    params = list(sig.parameters.keys())



def test_rootfolder_is_not_abstract():
    assert not inspect.isabstract(RootFolder)


def test_rootfolder_constructor_exists():
    assert callable(RootFolder.__init__)


def test_rootfolder_constructor_args():
    sig = inspect.signature(RootFolder.__init__)
    params = list(sig.parameters.keys())



def test_hsm_rootfolder_is_not_abstract():
    assert not inspect.isabstract(HSM_RootFolder)


def test_hsm_rootfolder_constructor_exists():
    assert callable(HSM_RootFolder.__init__)


def test_hsm_rootfolder_constructor_args():
    sig = inspect.signature(HSM_RootFolder.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm_rootfolder_has_name():
    assert hasattr(HSM_RootFolder, "name")
    descriptor = None
    for klass in HSM_RootFolder.__mro__:
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



def test_hsm_compoundstate_is_not_abstract():
    assert not inspect.isabstract(HSM_CompoundState)


def test_hsm_compoundstate_constructor_exists():
    assert callable(HSM_CompoundState.__init__)


def test_hsm_compoundstate_constructor_args():
    sig = inspect.signature(HSM_CompoundState.__init__)
    params = list(sig.parameters.keys())



def test_hsm_primitivestate_is_not_abstract():
    assert not inspect.isabstract(HSM_PrimitiveState)


def test_hsm_primitivestate_constructor_exists():
    assert callable(HSM_PrimitiveState.__init__)


def test_hsm_primitivestate_constructor_args():
    sig = inspect.signature(HSM_PrimitiveState.__init__)
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



def test_hsm_transition_is_not_abstract():
    assert not inspect.isabstract(HSM_Transition)


def test_hsm_transition_constructor_exists():
    assert callable(HSM_Transition.__init__)


def test_hsm_transition_constructor_args():
    sig = inspect.signature(HSM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "isSync" in params, "Missing parameter 'isSync'"

def test_hsm_transition_has_action():
    assert hasattr(HSM_Transition, "action")
    descriptor = None
    for klass in HSM_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_hsm_transition_has_guard():
    assert hasattr(HSM_Transition, "guard")
    descriptor = None
    for klass in HSM_Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_hsm_transition_has_trigger():
    assert hasattr(HSM_Transition, "trigger")
    descriptor = None
    for klass in HSM_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_hsm_transition_has_isSync():
    assert hasattr(HSM_Transition, "isSync")
    descriptor = None
    for klass in HSM_Transition.__mro__:
        if "isSync" in klass.__dict__:
            descriptor = klass.__dict__["isSync"]
            break
    assert isinstance(descriptor, property)



def test_hsm_statedaterelation_is_not_abstract():
    assert not inspect.isabstract(HSM_StateDateRelation)


def test_hsm_statedaterelation_constructor_exists():
    assert callable(HSM_StateDateRelation.__init__)


def test_hsm_statedaterelation_constructor_args():
    sig = inspect.signature(HSM_StateDateRelation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "color" in params, "Missing parameter 'color'"

def test_hsm_statedaterelation_has_value():
    assert hasattr(HSM_StateDateRelation, "value")
    descriptor = None
    for klass in HSM_StateDateRelation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_hsm_statedaterelation_has_color():
    assert hasattr(HSM_StateDateRelation, "color")
    descriptor = None
    for klass in HSM_StateDateRelation.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_hsm_statebase_is_not_abstract():
    assert not inspect.isabstract(HSM_StateBase)


def test_hsm_statebase_constructor_exists():
    assert callable(HSM_StateBase.__init__)


def test_hsm_statebase_constructor_args():
    sig = inspect.signature(HSM_StateBase.__init__)
    params = list(sig.parameters.keys())
    assert "defaultTransition" in params, "Missing parameter 'defaultTransition'"
    assert "marked" in params, "Missing parameter 'marked'"

def test_hsm_statebase_has_defaultTransition():
    assert hasattr(HSM_StateBase, "defaultTransition")
    descriptor = None
    for klass in HSM_StateBase.__mro__:
        if "defaultTransition" in klass.__dict__:
            descriptor = klass.__dict__["defaultTransition"]
            break
    assert isinstance(descriptor, property)

def test_hsm_statebase_has_marked():
    assert hasattr(HSM_StateBase, "marked")
    descriptor = None
    for klass in HSM_StateBase.__mro__:
        if "marked" in klass.__dict__:
            descriptor = klass.__dict__["marked"]
            break
    assert isinstance(descriptor, property)



def test_hsm_datavar_is_not_abstract():
    assert not inspect.isabstract(HSM_DataVar)


def test_hsm_datavar_constructor_exists():
    assert callable(HSM_DataVar.__init__)


def test_hsm_datavar_constructor_args():
    sig = inspect.signature(HSM_DataVar.__init__)
    params = list(sig.parameters.keys())



def test_hsm_mgaobject_is_not_abstract():
    assert not inspect.isabstract(HSM_MgaObject)


def test_hsm_mgaobject_constructor_exists():
    assert callable(HSM_MgaObject.__init__)


def test_hsm_mgaobject_constructor_args():
    sig = inspect.signature(HSM_MgaObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "position" in params, "Missing parameter 'position'"

def test_hsm_mgaobject_has_name():
    assert hasattr(HSM_MgaObject, "name")
    descriptor = None
    for klass in HSM_MgaObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hsm_mgaobject_has_position():
    assert hasattr(HSM_MgaObject, "position")
    descriptor = None
    for klass in HSM_MgaObject.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
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
HSM_AssociationDataStateBase_strategy = st.builds(
    HSM_AssociationDataStateBase,
)
HSM_AssociationStateState_strategy = st.builds(
    HSM_AssociationStateState,
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
HSM_StateDataRelation_strategy = st.builds(
    HSM_StateDataRelation,
    value=
        safe_text,
    color=
        safe_text
)
HSM_State_strategy = st.builds(
    HSM_State,
)
HSM_Init_strategy = st.builds(
    HSM_Init,
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
HSM_AndState_strategy = st.builds(
    HSM_AndState,
)
HSM_OrState_strategy = st.builds(
    HSM_OrState,
)
RootFolder_strategy = st.builds(
    RootFolder,
)
HSM_RootFolder_strategy = st.builds(
    HSM_RootFolder,
    name=
        safe_text
)
OrState_strategy = st.builds(
    OrState,
)
StateBase_strategy = st.builds(
    StateBase,
)
HSM_CompoundState_strategy = st.builds(
    HSM_CompoundState,
)
HSM_PrimitiveState_strategy = st.builds(
    HSM_PrimitiveState,
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
HSM_Transition_strategy = st.builds(
    HSM_Transition,
    action=
        safe_text,
    guard=
        safe_text,
    trigger=
        safe_text,
    isSync=
        safe_text
)
HSM_StateDateRelation_strategy = st.builds(
    HSM_StateDateRelation,
    value=
        safe_text,
    color=
        safe_text
)
HSM_StateBase_strategy = st.builds(
    HSM_StateBase,
    defaultTransition=
        safe_text,
    marked=
        safe_text
)
HSM_DataVar_strategy = st.builds(
    HSM_DataVar,
)
HSM_MgaObject_strategy = st.builds(
    HSM_MgaObject,
    name=
        safe_text,
    position=
        safe_text
)

@given(instance=HSM_AssociationDataStateBase_strategy)
@settings(max_examples=50)
def test_hsm_associationdatastatebase_instantiation(instance):
    assert isinstance(instance, HSM_AssociationDataStateBase)

@given(instance=HSM_AssociationStateState_strategy)
@settings(max_examples=50)
def test_hsm_associationstatestate_instantiation(instance):
    assert isinstance(instance, HSM_AssociationStateState)

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

@given(instance=HSM_StateDataRelation_strategy)
@settings(max_examples=50)
def test_hsm_statedatarelation_instantiation(instance):
    assert isinstance(instance, HSM_StateDataRelation)



@given(instance=HSM_StateDataRelation_strategy)
def test_hsm_statedatarelation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=HSM_StateDataRelation_strategy)
def test_hsm_statedatarelation_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=HSM_State_strategy)
@settings(max_examples=50)
def test_hsm_state_instantiation(instance):
    assert isinstance(instance, HSM_State)

@given(instance=HSM_Init_strategy)
@settings(max_examples=50)
def test_hsm_init_instantiation(instance):
    assert isinstance(instance, HSM_Init)

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

@given(instance=HSM_AndState_strategy)
@settings(max_examples=50)
def test_hsm_andstate_instantiation(instance):
    assert isinstance(instance, HSM_AndState)

@given(instance=HSM_OrState_strategy)
@settings(max_examples=50)
def test_hsm_orstate_instantiation(instance):
    assert isinstance(instance, HSM_OrState)

@given(instance=RootFolder_strategy)
@settings(max_examples=50)
def test_rootfolder_instantiation(instance):
    assert isinstance(instance, RootFolder)

@given(instance=HSM_RootFolder_strategy)
@settings(max_examples=50)
def test_hsm_rootfolder_instantiation(instance):
    assert isinstance(instance, HSM_RootFolder)



@given(instance=HSM_RootFolder_strategy)
def test_hsm_rootfolder_name_setter(instance):
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

@given(instance=HSM_CompoundState_strategy)
@settings(max_examples=50)
def test_hsm_compoundstate_instantiation(instance):
    assert isinstance(instance, HSM_CompoundState)

@given(instance=HSM_PrimitiveState_strategy)
@settings(max_examples=50)
def test_hsm_primitivestate_instantiation(instance):
    assert isinstance(instance, HSM_PrimitiveState)

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

@given(instance=HSM_Transition_strategy)
@settings(max_examples=50)
def test_hsm_transition_instantiation(instance):
    assert isinstance(instance, HSM_Transition)



@given(instance=HSM_Transition_strategy)
def test_hsm_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=HSM_Transition_strategy)
def test_hsm_transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original



@given(instance=HSM_Transition_strategy)
def test_hsm_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original



@given(instance=HSM_Transition_strategy)
def test_hsm_transition_isSync_setter(instance):
    original = instance.isSync
    instance.isSync = original
    assert instance.isSync == original

@given(instance=HSM_StateDateRelation_strategy)
@settings(max_examples=50)
def test_hsm_statedaterelation_instantiation(instance):
    assert isinstance(instance, HSM_StateDateRelation)



@given(instance=HSM_StateDateRelation_strategy)
def test_hsm_statedaterelation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=HSM_StateDateRelation_strategy)
def test_hsm_statedaterelation_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=HSM_StateBase_strategy)
@settings(max_examples=50)
def test_hsm_statebase_instantiation(instance):
    assert isinstance(instance, HSM_StateBase)



@given(instance=HSM_StateBase_strategy)
def test_hsm_statebase_defaultTransition_setter(instance):
    original = instance.defaultTransition
    instance.defaultTransition = original
    assert instance.defaultTransition == original



@given(instance=HSM_StateBase_strategy)
def test_hsm_statebase_marked_setter(instance):
    original = instance.marked
    instance.marked = original
    assert instance.marked == original

@given(instance=HSM_DataVar_strategy)
@settings(max_examples=50)
def test_hsm_datavar_instantiation(instance):
    assert isinstance(instance, HSM_DataVar)

@given(instance=HSM_MgaObject_strategy)
@settings(max_examples=50)
def test_hsm_mgaobject_instantiation(instance):
    assert isinstance(instance, HSM_MgaObject)



@given(instance=HSM_MgaObject_strategy)
def test_hsm_mgaobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=HSM_MgaObject_strategy)
def test_hsm_mgaobject_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original
