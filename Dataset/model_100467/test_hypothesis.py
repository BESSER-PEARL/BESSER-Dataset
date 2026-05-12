import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BuiltinEventSpec,
    stext_AlwaysEvent,
    stext_ExitEvent,
    stext_EntryEvent,
    stext_State,
    Expression,
    stext_EventValueReferenceExpression,
    stext_ActiveStateReferenceExpression,
    stext_EventRaisingExpression,
    Effect,
    stext_ReactionEffect,
    Trigger,
    stext_DefaultTrigger,
    stext_ReactionTrigger,
    stext_Import,
    NamedElement,
    StatechartScope,
    stext_ImportScope,
    stext_InternalScope,
    stext_InterfaceScope,
    Scope,
    stext_SimpleScope,
    stext_StatechartScope,
    stext_Scope,
    EventSpec,
    stext_BuiltinEventSpec,
    stext_TimeEventSpec,
    stext_RegularEventSpec,
    stext_EventSpec,
    ReactionProperty,
    stext_ExitPointSpec,
    stext_EntryPointSpec,
    stext_Guard,
    Reaction,
    stext_TransitionReaction,
    Operation,
    Declaration,
    stext_LocalReaction,
    stext_OperationDefinition,
    stext_Expression,
    Property,
    Variable,
    stext_VariableDefinition,
    Event,
    stext_EventDefinition,
    ScopedElement,
    stext_TransitionSpecification,
    stext_StateSpecification,
    stext_StatechartSpecification,
    DefRoot,
    stext_TransitionRoot,
    stext_StateRoot,
    stext_StatechartRoot,
    stext_DefRoot,
    stext_Root,
    Direction,
    TimeUnit,
    TimeEventType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_builtineventspec_is_not_abstract():
    assert not inspect.isabstract(BuiltinEventSpec)


def test_builtineventspec_constructor_exists():
    assert callable(BuiltinEventSpec.__init__)


def test_builtineventspec_constructor_args():
    sig = inspect.signature(BuiltinEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext_alwaysevent_is_not_abstract():
    assert not inspect.isabstract(stext_AlwaysEvent)


def test_stext_alwaysevent_constructor_exists():
    assert callable(stext_AlwaysEvent.__init__)


def test_stext_alwaysevent_constructor_args():
    sig = inspect.signature(stext_AlwaysEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext_exitevent_is_not_abstract():
    assert not inspect.isabstract(stext_ExitEvent)


def test_stext_exitevent_constructor_exists():
    assert callable(stext_ExitEvent.__init__)


def test_stext_exitevent_constructor_args():
    sig = inspect.signature(stext_ExitEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext_entryevent_is_not_abstract():
    assert not inspect.isabstract(stext_EntryEvent)


def test_stext_entryevent_constructor_exists():
    assert callable(stext_EntryEvent.__init__)


def test_stext_entryevent_constructor_args():
    sig = inspect.signature(stext_EntryEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext_state_is_not_abstract():
    assert not inspect.isabstract(stext_State)


def test_stext_state_constructor_exists():
    assert callable(stext_State.__init__)


def test_stext_state_constructor_args():
    sig = inspect.signature(stext_State.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_stext_eventvaluereferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext_EventValueReferenceExpression)


def test_stext_eventvaluereferenceexpression_constructor_exists():
    assert callable(stext_EventValueReferenceExpression.__init__)


def test_stext_eventvaluereferenceexpression_constructor_args():
    sig = inspect.signature(stext_EventValueReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_activestatereferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext_ActiveStateReferenceExpression)


def test_stext_activestatereferenceexpression_constructor_exists():
    assert callable(stext_ActiveStateReferenceExpression.__init__)


def test_stext_activestatereferenceexpression_constructor_args():
    sig = inspect.signature(stext_ActiveStateReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_eventraisingexpression_is_not_abstract():
    assert not inspect.isabstract(stext_EventRaisingExpression)


def test_stext_eventraisingexpression_constructor_exists():
    assert callable(stext_EventRaisingExpression.__init__)


def test_stext_eventraisingexpression_constructor_args():
    sig = inspect.signature(stext_EventRaisingExpression.__init__)
    params = list(sig.parameters.keys())



def test_effect_is_not_abstract():
    assert not inspect.isabstract(Effect)


def test_effect_constructor_exists():
    assert callable(Effect.__init__)


def test_effect_constructor_args():
    sig = inspect.signature(Effect.__init__)
    params = list(sig.parameters.keys())



def test_stext_reactioneffect_is_not_abstract():
    assert not inspect.isabstract(stext_ReactionEffect)


def test_stext_reactioneffect_constructor_exists():
    assert callable(stext_ReactionEffect.__init__)


def test_stext_reactioneffect_constructor_args():
    sig = inspect.signature(stext_ReactionEffect.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_stext_defaulttrigger_is_not_abstract():
    assert not inspect.isabstract(stext_DefaultTrigger)


def test_stext_defaulttrigger_constructor_exists():
    assert callable(stext_DefaultTrigger.__init__)


def test_stext_defaulttrigger_constructor_args():
    sig = inspect.signature(stext_DefaultTrigger.__init__)
    params = list(sig.parameters.keys())



def test_stext_reactiontrigger_is_not_abstract():
    assert not inspect.isabstract(stext_ReactionTrigger)


def test_stext_reactiontrigger_constructor_exists():
    assert callable(stext_ReactionTrigger.__init__)


def test_stext_reactiontrigger_constructor_args():
    sig = inspect.signature(stext_ReactionTrigger.__init__)
    params = list(sig.parameters.keys())



def test_stext_import_is_not_abstract():
    assert not inspect.isabstract(stext_Import)


def test_stext_import_constructor_exists():
    assert callable(stext_Import.__init__)


def test_stext_import_constructor_args():
    sig = inspect.signature(stext_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_stext_import_has_importedNamespace():
    assert hasattr(stext_Import, "importedNamespace")
    descriptor = None
    for klass in stext_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statechartscope_is_not_abstract():
    assert not inspect.isabstract(StatechartScope)


def test_statechartscope_constructor_exists():
    assert callable(StatechartScope.__init__)


def test_statechartscope_constructor_args():
    sig = inspect.signature(StatechartScope.__init__)
    params = list(sig.parameters.keys())



def test_stext_importscope_is_not_abstract():
    assert not inspect.isabstract(stext_ImportScope)


def test_stext_importscope_constructor_exists():
    assert callable(stext_ImportScope.__init__)


def test_stext_importscope_constructor_args():
    sig = inspect.signature(stext_ImportScope.__init__)
    params = list(sig.parameters.keys())



def test_stext_internalscope_is_not_abstract():
    assert not inspect.isabstract(stext_InternalScope)


def test_stext_internalscope_constructor_exists():
    assert callable(stext_InternalScope.__init__)


def test_stext_internalscope_constructor_args():
    sig = inspect.signature(stext_InternalScope.__init__)
    params = list(sig.parameters.keys())



def test_stext_interfacescope_is_not_abstract():
    assert not inspect.isabstract(stext_InterfaceScope)


def test_stext_interfacescope_constructor_exists():
    assert callable(stext_InterfaceScope.__init__)


def test_stext_interfacescope_constructor_args():
    sig = inspect.signature(stext_InterfaceScope.__init__)
    params = list(sig.parameters.keys())



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_stext_simplescope_is_not_abstract():
    assert not inspect.isabstract(stext_SimpleScope)


def test_stext_simplescope_constructor_exists():
    assert callable(stext_SimpleScope.__init__)


def test_stext_simplescope_constructor_args():
    sig = inspect.signature(stext_SimpleScope.__init__)
    params = list(sig.parameters.keys())



def test_stext_statechartscope_is_not_abstract():
    assert not inspect.isabstract(stext_StatechartScope)


def test_stext_statechartscope_constructor_exists():
    assert callable(stext_StatechartScope.__init__)


def test_stext_statechartscope_constructor_args():
    sig = inspect.signature(stext_StatechartScope.__init__)
    params = list(sig.parameters.keys())



def test_stext_scope_is_not_abstract():
    assert not inspect.isabstract(stext_Scope)


def test_stext_scope_constructor_exists():
    assert callable(stext_Scope.__init__)


def test_stext_scope_constructor_args():
    sig = inspect.signature(stext_Scope.__init__)
    params = list(sig.parameters.keys())



def test_eventspec_is_not_abstract():
    assert not inspect.isabstract(EventSpec)


def test_eventspec_constructor_exists():
    assert callable(EventSpec.__init__)


def test_eventspec_constructor_args():
    sig = inspect.signature(EventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext_builtineventspec_is_not_abstract():
    assert not inspect.isabstract(stext_BuiltinEventSpec)


def test_stext_builtineventspec_constructor_exists():
    assert callable(stext_BuiltinEventSpec.__init__)


def test_stext_builtineventspec_constructor_args():
    sig = inspect.signature(stext_BuiltinEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext_timeeventspec_is_not_abstract():
    assert not inspect.isabstract(stext_TimeEventSpec)


def test_stext_timeeventspec_constructor_exists():
    assert callable(stext_TimeEventSpec.__init__)


def test_stext_timeeventspec_constructor_args():
    sig = inspect.signature(stext_TimeEventSpec.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_stext_timeeventspec_has_type():
    assert hasattr(stext_TimeEventSpec, "type")
    descriptor = None
    for klass in stext_TimeEventSpec.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_stext_timeeventspec_has_unit():
    assert hasattr(stext_TimeEventSpec, "unit")
    descriptor = None
    for klass in stext_TimeEventSpec.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_stext_regulareventspec_is_not_abstract():
    assert not inspect.isabstract(stext_RegularEventSpec)


def test_stext_regulareventspec_constructor_exists():
    assert callable(stext_RegularEventSpec.__init__)


def test_stext_regulareventspec_constructor_args():
    sig = inspect.signature(stext_RegularEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext_eventspec_is_not_abstract():
    assert not inspect.isabstract(stext_EventSpec)


def test_stext_eventspec_constructor_exists():
    assert callable(stext_EventSpec.__init__)


def test_stext_eventspec_constructor_args():
    sig = inspect.signature(stext_EventSpec.__init__)
    params = list(sig.parameters.keys())



def test_reactionproperty_is_not_abstract():
    assert not inspect.isabstract(ReactionProperty)


def test_reactionproperty_constructor_exists():
    assert callable(ReactionProperty.__init__)


def test_reactionproperty_constructor_args():
    sig = inspect.signature(ReactionProperty.__init__)
    params = list(sig.parameters.keys())



def test_stext_exitpointspec_is_not_abstract():
    assert not inspect.isabstract(stext_ExitPointSpec)


def test_stext_exitpointspec_constructor_exists():
    assert callable(stext_ExitPointSpec.__init__)


def test_stext_exitpointspec_constructor_args():
    sig = inspect.signature(stext_ExitPointSpec.__init__)
    params = list(sig.parameters.keys())
    assert "exitpoint" in params, "Missing parameter 'exitpoint'"

def test_stext_exitpointspec_has_exitpoint():
    assert hasattr(stext_ExitPointSpec, "exitpoint")
    descriptor = None
    for klass in stext_ExitPointSpec.__mro__:
        if "exitpoint" in klass.__dict__:
            descriptor = klass.__dict__["exitpoint"]
            break
    assert isinstance(descriptor, property)



def test_stext_entrypointspec_is_not_abstract():
    assert not inspect.isabstract(stext_EntryPointSpec)


def test_stext_entrypointspec_constructor_exists():
    assert callable(stext_EntryPointSpec.__init__)


def test_stext_entrypointspec_constructor_args():
    sig = inspect.signature(stext_EntryPointSpec.__init__)
    params = list(sig.parameters.keys())
    assert "entrypoint" in params, "Missing parameter 'entrypoint'"

def test_stext_entrypointspec_has_entrypoint():
    assert hasattr(stext_EntryPointSpec, "entrypoint")
    descriptor = None
    for klass in stext_EntryPointSpec.__mro__:
        if "entrypoint" in klass.__dict__:
            descriptor = klass.__dict__["entrypoint"]
            break
    assert isinstance(descriptor, property)



def test_stext_guard_is_not_abstract():
    assert not inspect.isabstract(stext_Guard)


def test_stext_guard_constructor_exists():
    assert callable(stext_Guard.__init__)


def test_stext_guard_constructor_args():
    sig = inspect.signature(stext_Guard.__init__)
    params = list(sig.parameters.keys())



def test_reaction_is_not_abstract():
    assert not inspect.isabstract(Reaction)


def test_reaction_constructor_exists():
    assert callable(Reaction.__init__)


def test_reaction_constructor_args():
    sig = inspect.signature(Reaction.__init__)
    params = list(sig.parameters.keys())



def test_stext_transitionreaction_is_not_abstract():
    assert not inspect.isabstract(stext_TransitionReaction)


def test_stext_transitionreaction_constructor_exists():
    assert callable(stext_TransitionReaction.__init__)


def test_stext_transitionreaction_constructor_args():
    sig = inspect.signature(stext_TransitionReaction.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_stext_localreaction_is_not_abstract():
    assert not inspect.isabstract(stext_LocalReaction)


def test_stext_localreaction_constructor_exists():
    assert callable(stext_LocalReaction.__init__)


def test_stext_localreaction_constructor_args():
    sig = inspect.signature(stext_LocalReaction.__init__)
    params = list(sig.parameters.keys())



def test_stext_operationdefinition_is_not_abstract():
    assert not inspect.isabstract(stext_OperationDefinition)


def test_stext_operationdefinition_constructor_exists():
    assert callable(stext_OperationDefinition.__init__)


def test_stext_operationdefinition_constructor_args():
    sig = inspect.signature(stext_OperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_stext_expression_is_not_abstract():
    assert not inspect.isabstract(stext_Expression)


def test_stext_expression_constructor_exists():
    assert callable(stext_Expression.__init__)


def test_stext_expression_constructor_args():
    sig = inspect.signature(stext_Expression.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_stext_variabledefinition_is_not_abstract():
    assert not inspect.isabstract(stext_VariableDefinition)


def test_stext_variabledefinition_constructor_exists():
    assert callable(stext_VariableDefinition.__init__)


def test_stext_variabledefinition_constructor_args():
    sig = inspect.signature(stext_VariableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "readonly" in params, "Missing parameter 'readonly'"
    assert "external" in params, "Missing parameter 'external'"

def test_stext_variabledefinition_has_readonly():
    assert hasattr(stext_VariableDefinition, "readonly")
    descriptor = None
    for klass in stext_VariableDefinition.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)

def test_stext_variabledefinition_has_external():
    assert hasattr(stext_VariableDefinition, "external")
    descriptor = None
    for klass in stext_VariableDefinition.__mro__:
        if "external" in klass.__dict__:
            descriptor = klass.__dict__["external"]
            break
    assert isinstance(descriptor, property)



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_stext_eventdefinition_is_not_abstract():
    assert not inspect.isabstract(stext_EventDefinition)


def test_stext_eventdefinition_constructor_exists():
    assert callable(stext_EventDefinition.__init__)


def test_stext_eventdefinition_constructor_args():
    sig = inspect.signature(stext_EventDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_stext_eventdefinition_has_direction():
    assert hasattr(stext_EventDefinition, "direction")
    descriptor = None
    for klass in stext_EventDefinition.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_scopedelement_is_not_abstract():
    assert not inspect.isabstract(ScopedElement)


def test_scopedelement_constructor_exists():
    assert callable(ScopedElement.__init__)


def test_scopedelement_constructor_args():
    sig = inspect.signature(ScopedElement.__init__)
    params = list(sig.parameters.keys())



def test_stext_transitionspecification_is_not_abstract():
    assert not inspect.isabstract(stext_TransitionSpecification)


def test_stext_transitionspecification_constructor_exists():
    assert callable(stext_TransitionSpecification.__init__)


def test_stext_transitionspecification_constructor_args():
    sig = inspect.signature(stext_TransitionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_stext_statespecification_is_not_abstract():
    assert not inspect.isabstract(stext_StateSpecification)


def test_stext_statespecification_constructor_exists():
    assert callable(stext_StateSpecification.__init__)


def test_stext_statespecification_constructor_args():
    sig = inspect.signature(stext_StateSpecification.__init__)
    params = list(sig.parameters.keys())



def test_stext_statechartspecification_is_not_abstract():
    assert not inspect.isabstract(stext_StatechartSpecification)


def test_stext_statechartspecification_constructor_exists():
    assert callable(stext_StatechartSpecification.__init__)


def test_stext_statechartspecification_constructor_args():
    sig = inspect.signature(stext_StatechartSpecification.__init__)
    params = list(sig.parameters.keys())



def test_defroot_is_not_abstract():
    assert not inspect.isabstract(DefRoot)


def test_defroot_constructor_exists():
    assert callable(DefRoot.__init__)


def test_defroot_constructor_args():
    sig = inspect.signature(DefRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext_transitionroot_is_not_abstract():
    assert not inspect.isabstract(stext_TransitionRoot)


def test_stext_transitionroot_constructor_exists():
    assert callable(stext_TransitionRoot.__init__)


def test_stext_transitionroot_constructor_args():
    sig = inspect.signature(stext_TransitionRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext_stateroot_is_not_abstract():
    assert not inspect.isabstract(stext_StateRoot)


def test_stext_stateroot_constructor_exists():
    assert callable(stext_StateRoot.__init__)


def test_stext_stateroot_constructor_args():
    sig = inspect.signature(stext_StateRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext_statechartroot_is_not_abstract():
    assert not inspect.isabstract(stext_StatechartRoot)


def test_stext_statechartroot_constructor_exists():
    assert callable(stext_StatechartRoot.__init__)


def test_stext_statechartroot_constructor_args():
    sig = inspect.signature(stext_StatechartRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext_defroot_is_not_abstract():
    assert not inspect.isabstract(stext_DefRoot)


def test_stext_defroot_constructor_exists():
    assert callable(stext_DefRoot.__init__)


def test_stext_defroot_constructor_args():
    sig = inspect.signature(stext_DefRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext_root_is_not_abstract():
    assert not inspect.isabstract(stext_Root)


def test_stext_root_constructor_exists():
    assert callable(stext_Root.__init__)


def test_stext_root_constructor_args():
    sig = inspect.signature(stext_Root.__init__)
    params = list(sig.parameters.keys())

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "OUT",
        "IN",
        "LOCAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "microsecond",
        "second",
        "millisecond",
        "nanosecond",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnit"

def test_timeeventtype_exists():
    # Check that the Enumeration exists
    assert TimeEventType is not None

def test_timeeventtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeEventType]
    expected_literals = [
        "every",
        "after",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeEventType"


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
BuiltinEventSpec_strategy = st.builds(
    BuiltinEventSpec,
)
stext_AlwaysEvent_strategy = st.builds(
    stext_AlwaysEvent,
)
stext_ExitEvent_strategy = st.builds(
    stext_ExitEvent,
)
stext_EntryEvent_strategy = st.builds(
    stext_EntryEvent,
)
stext_State_strategy = st.builds(
    stext_State,
)
Expression_strategy = st.builds(
    Expression,
)
stext_EventValueReferenceExpression_strategy = st.builds(
    stext_EventValueReferenceExpression,
)
stext_ActiveStateReferenceExpression_strategy = st.builds(
    stext_ActiveStateReferenceExpression,
)
stext_EventRaisingExpression_strategy = st.builds(
    stext_EventRaisingExpression,
)
Effect_strategy = st.builds(
    Effect,
)
stext_ReactionEffect_strategy = st.builds(
    stext_ReactionEffect,
)
Trigger_strategy = st.builds(
    Trigger,
)
stext_DefaultTrigger_strategy = st.builds(
    stext_DefaultTrigger,
)
stext_ReactionTrigger_strategy = st.builds(
    stext_ReactionTrigger,
)
stext_Import_strategy = st.builds(
    stext_Import,
    importedNamespace=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
StatechartScope_strategy = st.builds(
    StatechartScope,
)
stext_ImportScope_strategy = st.builds(
    stext_ImportScope,
)
stext_InternalScope_strategy = st.builds(
    stext_InternalScope,
)
stext_InterfaceScope_strategy = st.builds(
    stext_InterfaceScope,
)
Scope_strategy = st.builds(
    Scope,
)
stext_SimpleScope_strategy = st.builds(
    stext_SimpleScope,
)
stext_StatechartScope_strategy = st.builds(
    stext_StatechartScope,
)
stext_Scope_strategy = st.builds(
    stext_Scope,
)
EventSpec_strategy = st.builds(
    EventSpec,
)
stext_BuiltinEventSpec_strategy = st.builds(
    stext_BuiltinEventSpec,
)
stext_TimeEventSpec_strategy = st.builds(
    stext_TimeEventSpec,
    type=
        safe_text,
    unit=
        safe_text
)
stext_RegularEventSpec_strategy = st.builds(
    stext_RegularEventSpec,
)
stext_EventSpec_strategy = st.builds(
    stext_EventSpec,
)
ReactionProperty_strategy = st.builds(
    ReactionProperty,
)
stext_ExitPointSpec_strategy = st.builds(
    stext_ExitPointSpec,
    exitpoint=
        safe_text
)
stext_EntryPointSpec_strategy = st.builds(
    stext_EntryPointSpec,
    entrypoint=
        safe_text
)
stext_Guard_strategy = st.builds(
    stext_Guard,
)
Reaction_strategy = st.builds(
    Reaction,
)
stext_TransitionReaction_strategy = st.builds(
    stext_TransitionReaction,
)
Operation_strategy = st.builds(
    Operation,
)
Declaration_strategy = st.builds(
    Declaration,
)
stext_LocalReaction_strategy = st.builds(
    stext_LocalReaction,
)
stext_OperationDefinition_strategy = st.builds(
    stext_OperationDefinition,
)
stext_Expression_strategy = st.builds(
    stext_Expression,
)
Property_strategy = st.builds(
    Property,
)
Variable_strategy = st.builds(
    Variable,
)
stext_VariableDefinition_strategy = st.builds(
    stext_VariableDefinition,
    readonly=
        st.booleans(),
    external=
        st.booleans()
)
Event_strategy = st.builds(
    Event,
)
stext_EventDefinition_strategy = st.builds(
    stext_EventDefinition,
    direction=
        safe_text
)
ScopedElement_strategy = st.builds(
    ScopedElement,
)
stext_TransitionSpecification_strategy = st.builds(
    stext_TransitionSpecification,
)
stext_StateSpecification_strategy = st.builds(
    stext_StateSpecification,
)
stext_StatechartSpecification_strategy = st.builds(
    stext_StatechartSpecification,
)
DefRoot_strategy = st.builds(
    DefRoot,
)
stext_TransitionRoot_strategy = st.builds(
    stext_TransitionRoot,
)
stext_StateRoot_strategy = st.builds(
    stext_StateRoot,
)
stext_StatechartRoot_strategy = st.builds(
    stext_StatechartRoot,
)
stext_DefRoot_strategy = st.builds(
    stext_DefRoot,
)
stext_Root_strategy = st.builds(
    stext_Root,
)

@given(instance=BuiltinEventSpec_strategy)
@settings(max_examples=50)
def test_builtineventspec_instantiation(instance):
    assert isinstance(instance, BuiltinEventSpec)

@given(instance=stext_AlwaysEvent_strategy)
@settings(max_examples=50)
def test_stext_alwaysevent_instantiation(instance):
    assert isinstance(instance, stext_AlwaysEvent)

@given(instance=stext_ExitEvent_strategy)
@settings(max_examples=50)
def test_stext_exitevent_instantiation(instance):
    assert isinstance(instance, stext_ExitEvent)

@given(instance=stext_EntryEvent_strategy)
@settings(max_examples=50)
def test_stext_entryevent_instantiation(instance):
    assert isinstance(instance, stext_EntryEvent)

@given(instance=stext_State_strategy)
@settings(max_examples=50)
def test_stext_state_instantiation(instance):
    assert isinstance(instance, stext_State)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=stext_EventValueReferenceExpression_strategy)
@settings(max_examples=50)
def test_stext_eventvaluereferenceexpression_instantiation(instance):
    assert isinstance(instance, stext_EventValueReferenceExpression)

@given(instance=stext_ActiveStateReferenceExpression_strategy)
@settings(max_examples=50)
def test_stext_activestatereferenceexpression_instantiation(instance):
    assert isinstance(instance, stext_ActiveStateReferenceExpression)

@given(instance=stext_EventRaisingExpression_strategy)
@settings(max_examples=50)
def test_stext_eventraisingexpression_instantiation(instance):
    assert isinstance(instance, stext_EventRaisingExpression)

@given(instance=Effect_strategy)
@settings(max_examples=50)
def test_effect_instantiation(instance):
    assert isinstance(instance, Effect)

@given(instance=stext_ReactionEffect_strategy)
@settings(max_examples=50)
def test_stext_reactioneffect_instantiation(instance):
    assert isinstance(instance, stext_ReactionEffect)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=stext_DefaultTrigger_strategy)
@settings(max_examples=50)
def test_stext_defaulttrigger_instantiation(instance):
    assert isinstance(instance, stext_DefaultTrigger)

@given(instance=stext_ReactionTrigger_strategy)
@settings(max_examples=50)
def test_stext_reactiontrigger_instantiation(instance):
    assert isinstance(instance, stext_ReactionTrigger)

@given(instance=stext_Import_strategy)
@settings(max_examples=50)
def test_stext_import_instantiation(instance):
    assert isinstance(instance, stext_Import)



@given(instance=stext_Import_strategy)
def test_stext_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=StatechartScope_strategy)
@settings(max_examples=50)
def test_statechartscope_instantiation(instance):
    assert isinstance(instance, StatechartScope)

@given(instance=stext_ImportScope_strategy)
@settings(max_examples=50)
def test_stext_importscope_instantiation(instance):
    assert isinstance(instance, stext_ImportScope)

@given(instance=stext_InternalScope_strategy)
@settings(max_examples=50)
def test_stext_internalscope_instantiation(instance):
    assert isinstance(instance, stext_InternalScope)

@given(instance=stext_InterfaceScope_strategy)
@settings(max_examples=50)
def test_stext_interfacescope_instantiation(instance):
    assert isinstance(instance, stext_InterfaceScope)

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=stext_SimpleScope_strategy)
@settings(max_examples=50)
def test_stext_simplescope_instantiation(instance):
    assert isinstance(instance, stext_SimpleScope)

@given(instance=stext_StatechartScope_strategy)
@settings(max_examples=50)
def test_stext_statechartscope_instantiation(instance):
    assert isinstance(instance, stext_StatechartScope)

@given(instance=stext_Scope_strategy)
@settings(max_examples=50)
def test_stext_scope_instantiation(instance):
    assert isinstance(instance, stext_Scope)

@given(instance=EventSpec_strategy)
@settings(max_examples=50)
def test_eventspec_instantiation(instance):
    assert isinstance(instance, EventSpec)

@given(instance=stext_BuiltinEventSpec_strategy)
@settings(max_examples=50)
def test_stext_builtineventspec_instantiation(instance):
    assert isinstance(instance, stext_BuiltinEventSpec)

@given(instance=stext_TimeEventSpec_strategy)
@settings(max_examples=50)
def test_stext_timeeventspec_instantiation(instance):
    assert isinstance(instance, stext_TimeEventSpec)



@given(instance=stext_TimeEventSpec_strategy)
def test_stext_timeeventspec_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=stext_TimeEventSpec_strategy)
def test_stext_timeeventspec_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=stext_RegularEventSpec_strategy)
@settings(max_examples=50)
def test_stext_regulareventspec_instantiation(instance):
    assert isinstance(instance, stext_RegularEventSpec)

@given(instance=stext_EventSpec_strategy)
@settings(max_examples=50)
def test_stext_eventspec_instantiation(instance):
    assert isinstance(instance, stext_EventSpec)

@given(instance=ReactionProperty_strategy)
@settings(max_examples=50)
def test_reactionproperty_instantiation(instance):
    assert isinstance(instance, ReactionProperty)

@given(instance=stext_ExitPointSpec_strategy)
@settings(max_examples=50)
def test_stext_exitpointspec_instantiation(instance):
    assert isinstance(instance, stext_ExitPointSpec)



@given(instance=stext_ExitPointSpec_strategy)
def test_stext_exitpointspec_exitpoint_setter(instance):
    original = instance.exitpoint
    instance.exitpoint = original
    assert instance.exitpoint == original

@given(instance=stext_EntryPointSpec_strategy)
@settings(max_examples=50)
def test_stext_entrypointspec_instantiation(instance):
    assert isinstance(instance, stext_EntryPointSpec)



@given(instance=stext_EntryPointSpec_strategy)
def test_stext_entrypointspec_entrypoint_setter(instance):
    original = instance.entrypoint
    instance.entrypoint = original
    assert instance.entrypoint == original

@given(instance=stext_Guard_strategy)
@settings(max_examples=50)
def test_stext_guard_instantiation(instance):
    assert isinstance(instance, stext_Guard)

@given(instance=Reaction_strategy)
@settings(max_examples=50)
def test_reaction_instantiation(instance):
    assert isinstance(instance, Reaction)

@given(instance=stext_TransitionReaction_strategy)
@settings(max_examples=50)
def test_stext_transitionreaction_instantiation(instance):
    assert isinstance(instance, stext_TransitionReaction)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=stext_LocalReaction_strategy)
@settings(max_examples=50)
def test_stext_localreaction_instantiation(instance):
    assert isinstance(instance, stext_LocalReaction)

@given(instance=stext_OperationDefinition_strategy)
@settings(max_examples=50)
def test_stext_operationdefinition_instantiation(instance):
    assert isinstance(instance, stext_OperationDefinition)

@given(instance=stext_Expression_strategy)
@settings(max_examples=50)
def test_stext_expression_instantiation(instance):
    assert isinstance(instance, stext_Expression)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=stext_VariableDefinition_strategy)
@settings(max_examples=50)
def test_stext_variabledefinition_instantiation(instance):
    assert isinstance(instance, stext_VariableDefinition)



@given(instance=stext_VariableDefinition_strategy)
def test_stext_variabledefinition_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original



@given(instance=stext_VariableDefinition_strategy)
def test_stext_variabledefinition_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=stext_EventDefinition_strategy)
@settings(max_examples=50)
def test_stext_eventdefinition_instantiation(instance):
    assert isinstance(instance, stext_EventDefinition)



@given(instance=stext_EventDefinition_strategy)
def test_stext_eventdefinition_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=ScopedElement_strategy)
@settings(max_examples=50)
def test_scopedelement_instantiation(instance):
    assert isinstance(instance, ScopedElement)

@given(instance=stext_TransitionSpecification_strategy)
@settings(max_examples=50)
def test_stext_transitionspecification_instantiation(instance):
    assert isinstance(instance, stext_TransitionSpecification)

@given(instance=stext_StateSpecification_strategy)
@settings(max_examples=50)
def test_stext_statespecification_instantiation(instance):
    assert isinstance(instance, stext_StateSpecification)

@given(instance=stext_StatechartSpecification_strategy)
@settings(max_examples=50)
def test_stext_statechartspecification_instantiation(instance):
    assert isinstance(instance, stext_StatechartSpecification)

@given(instance=DefRoot_strategy)
@settings(max_examples=50)
def test_defroot_instantiation(instance):
    assert isinstance(instance, DefRoot)

@given(instance=stext_TransitionRoot_strategy)
@settings(max_examples=50)
def test_stext_transitionroot_instantiation(instance):
    assert isinstance(instance, stext_TransitionRoot)

@given(instance=stext_StateRoot_strategy)
@settings(max_examples=50)
def test_stext_stateroot_instantiation(instance):
    assert isinstance(instance, stext_StateRoot)

@given(instance=stext_StatechartRoot_strategy)
@settings(max_examples=50)
def test_stext_statechartroot_instantiation(instance):
    assert isinstance(instance, stext_StatechartRoot)

@given(instance=stext_DefRoot_strategy)
@settings(max_examples=50)
def test_stext_defroot_instantiation(instance):
    assert isinstance(instance, stext_DefRoot)

@given(instance=stext_Root_strategy)
@settings(max_examples=50)
def test_stext_root_instantiation(instance):
    assert isinstance(instance, stext_Root)
