import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    stext::EventValueReferenceExpression,
    stext::EventRaisingExpression,
    Effect,
    stext::ReactionEffect,
    stext::State,
    stext::ActiveStateReferenceExpression,
    BuiltinEventSpec,
    stext::ExitEvent,
    stext::AlwaysEvent,
    stext::EntryEvent,
    EventSpec,
    stext::TimeEventSpec,
    stext::BuiltinEventSpec,
    stext::RegularEventSpec,
    stext::EventSpec,
    ReactionProperty,
    stext::ExitPointSpec,
    stext::EntryPointSpec,
    Trigger,
    stext::DefaultTrigger,
    stext::ReactionTrigger,
    Declaration,
    stext::Expression,
    Property,
    Variable,
    stext::VariableDefinition,
    Event,
    stext::EventDefinition,
    stext::Import,
    NamedElement,
    StatechartScope,
    stext::ImportScope,
    stext::InternalScope,
    stext::InterfaceScope,
    Scope,
    stext::SimpleScope,
    stext::StatechartScope,
    stext::Guard,
    Reaction,
    stext::TransitionReaction,
    stext::LocalReaction,
    Operation,
    stext::OperationDefinition,
    stext::TransitionSpecification,
    stext::StateSpecification,
    DefRoot,
    stext::TransitionRoot,
    stext::StateRoot,
    stext::StatechartRoot,
    stext::DefRoot,
    stext::Root,
    stext::Scope,
    ScopedElement,
    stext::StatechartSpecification,
    TimeUnit,
    TimeEventType,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_stext::eventvaluereferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext::EventValueReferenceExpression)


def test_stext::eventvaluereferenceexpression_constructor_exists():
    assert callable(stext::EventValueReferenceExpression.__init__)


def test_stext::eventvaluereferenceexpression_constructor_args():
    sig = inspect.signature(stext::EventValueReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext::eventraisingexpression_is_not_abstract():
    assert not inspect.isabstract(stext::EventRaisingExpression)


def test_stext::eventraisingexpression_constructor_exists():
    assert callable(stext::EventRaisingExpression.__init__)


def test_stext::eventraisingexpression_constructor_args():
    sig = inspect.signature(stext::EventRaisingExpression.__init__)
    params = list(sig.parameters.keys())



def test_effect_is_not_abstract():
    assert not inspect.isabstract(Effect)


def test_effect_constructor_exists():
    assert callable(Effect.__init__)


def test_effect_constructor_args():
    sig = inspect.signature(Effect.__init__)
    params = list(sig.parameters.keys())



def test_stext::reactioneffect_is_not_abstract():
    assert not inspect.isabstract(stext::ReactionEffect)


def test_stext::reactioneffect_constructor_exists():
    assert callable(stext::ReactionEffect.__init__)


def test_stext::reactioneffect_constructor_args():
    sig = inspect.signature(stext::ReactionEffect.__init__)
    params = list(sig.parameters.keys())



def test_stext::state_is_not_abstract():
    assert not inspect.isabstract(stext::State)


def test_stext::state_constructor_exists():
    assert callable(stext::State.__init__)


def test_stext::state_constructor_args():
    sig = inspect.signature(stext::State.__init__)
    params = list(sig.parameters.keys())



def test_stext::activestatereferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext::ActiveStateReferenceExpression)


def test_stext::activestatereferenceexpression_constructor_exists():
    assert callable(stext::ActiveStateReferenceExpression.__init__)


def test_stext::activestatereferenceexpression_constructor_args():
    sig = inspect.signature(stext::ActiveStateReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_builtineventspec_is_not_abstract():
    assert not inspect.isabstract(BuiltinEventSpec)


def test_builtineventspec_constructor_exists():
    assert callable(BuiltinEventSpec.__init__)


def test_builtineventspec_constructor_args():
    sig = inspect.signature(BuiltinEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext::exitevent_is_not_abstract():
    assert not inspect.isabstract(stext::ExitEvent)


def test_stext::exitevent_constructor_exists():
    assert callable(stext::ExitEvent.__init__)


def test_stext::exitevent_constructor_args():
    sig = inspect.signature(stext::ExitEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext::alwaysevent_is_not_abstract():
    assert not inspect.isabstract(stext::AlwaysEvent)


def test_stext::alwaysevent_constructor_exists():
    assert callable(stext::AlwaysEvent.__init__)


def test_stext::alwaysevent_constructor_args():
    sig = inspect.signature(stext::AlwaysEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext::entryevent_is_not_abstract():
    assert not inspect.isabstract(stext::EntryEvent)


def test_stext::entryevent_constructor_exists():
    assert callable(stext::EntryEvent.__init__)


def test_stext::entryevent_constructor_args():
    sig = inspect.signature(stext::EntryEvent.__init__)
    params = list(sig.parameters.keys())



def test_eventspec_is_not_abstract():
    assert not inspect.isabstract(EventSpec)


def test_eventspec_constructor_exists():
    assert callable(EventSpec.__init__)


def test_eventspec_constructor_args():
    sig = inspect.signature(EventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext::timeeventspec_is_not_abstract():
    assert not inspect.isabstract(stext::TimeEventSpec)


def test_stext::timeeventspec_constructor_exists():
    assert callable(stext::TimeEventSpec.__init__)


def test_stext::timeeventspec_constructor_args():
    sig = inspect.signature(stext::TimeEventSpec.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "type" in params, "Missing parameter 'type'"

def test_stext::timeeventspec_has_unit():
    assert hasattr(stext::TimeEventSpec, "unit")
    descriptor = None
    for klass in stext::TimeEventSpec.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_stext::timeeventspec_has_type():
    assert hasattr(stext::TimeEventSpec, "type")
    descriptor = None
    for klass in stext::TimeEventSpec.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_stext::builtineventspec_is_not_abstract():
    assert not inspect.isabstract(stext::BuiltinEventSpec)


def test_stext::builtineventspec_constructor_exists():
    assert callable(stext::BuiltinEventSpec.__init__)


def test_stext::builtineventspec_constructor_args():
    sig = inspect.signature(stext::BuiltinEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext::regulareventspec_is_not_abstract():
    assert not inspect.isabstract(stext::RegularEventSpec)


def test_stext::regulareventspec_constructor_exists():
    assert callable(stext::RegularEventSpec.__init__)


def test_stext::regulareventspec_constructor_args():
    sig = inspect.signature(stext::RegularEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext::eventspec_is_not_abstract():
    assert not inspect.isabstract(stext::EventSpec)


def test_stext::eventspec_constructor_exists():
    assert callable(stext::EventSpec.__init__)


def test_stext::eventspec_constructor_args():
    sig = inspect.signature(stext::EventSpec.__init__)
    params = list(sig.parameters.keys())



def test_reactionproperty_is_not_abstract():
    assert not inspect.isabstract(ReactionProperty)


def test_reactionproperty_constructor_exists():
    assert callable(ReactionProperty.__init__)


def test_reactionproperty_constructor_args():
    sig = inspect.signature(ReactionProperty.__init__)
    params = list(sig.parameters.keys())



def test_stext::exitpointspec_is_not_abstract():
    assert not inspect.isabstract(stext::ExitPointSpec)


def test_stext::exitpointspec_constructor_exists():
    assert callable(stext::ExitPointSpec.__init__)


def test_stext::exitpointspec_constructor_args():
    sig = inspect.signature(stext::ExitPointSpec.__init__)
    params = list(sig.parameters.keys())
    assert "exitpoint" in params, "Missing parameter 'exitpoint'"

def test_stext::exitpointspec_has_exitpoint():
    assert hasattr(stext::ExitPointSpec, "exitpoint")
    descriptor = None
    for klass in stext::ExitPointSpec.__mro__:
        if "exitpoint" in klass.__dict__:
            descriptor = klass.__dict__["exitpoint"]
            break
    assert isinstance(descriptor, property)



def test_stext::entrypointspec_is_not_abstract():
    assert not inspect.isabstract(stext::EntryPointSpec)


def test_stext::entrypointspec_constructor_exists():
    assert callable(stext::EntryPointSpec.__init__)


def test_stext::entrypointspec_constructor_args():
    sig = inspect.signature(stext::EntryPointSpec.__init__)
    params = list(sig.parameters.keys())
    assert "entrypoint" in params, "Missing parameter 'entrypoint'"

def test_stext::entrypointspec_has_entrypoint():
    assert hasattr(stext::EntryPointSpec, "entrypoint")
    descriptor = None
    for klass in stext::EntryPointSpec.__mro__:
        if "entrypoint" in klass.__dict__:
            descriptor = klass.__dict__["entrypoint"]
            break
    assert isinstance(descriptor, property)



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_stext::defaulttrigger_is_not_abstract():
    assert not inspect.isabstract(stext::DefaultTrigger)


def test_stext::defaulttrigger_constructor_exists():
    assert callable(stext::DefaultTrigger.__init__)


def test_stext::defaulttrigger_constructor_args():
    sig = inspect.signature(stext::DefaultTrigger.__init__)
    params = list(sig.parameters.keys())



def test_stext::reactiontrigger_is_not_abstract():
    assert not inspect.isabstract(stext::ReactionTrigger)


def test_stext::reactiontrigger_constructor_exists():
    assert callable(stext::ReactionTrigger.__init__)


def test_stext::reactiontrigger_constructor_args():
    sig = inspect.signature(stext::ReactionTrigger.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_stext::expression_is_not_abstract():
    assert not inspect.isabstract(stext::Expression)


def test_stext::expression_constructor_exists():
    assert callable(stext::Expression.__init__)


def test_stext::expression_constructor_args():
    sig = inspect.signature(stext::Expression.__init__)
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



def test_stext::variabledefinition_is_not_abstract():
    assert not inspect.isabstract(stext::VariableDefinition)


def test_stext::variabledefinition_constructor_exists():
    assert callable(stext::VariableDefinition.__init__)


def test_stext::variabledefinition_constructor_args():
    sig = inspect.signature(stext::VariableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "external" in params, "Missing parameter 'external'"
    assert "readonly" in params, "Missing parameter 'readonly'"

def test_stext::variabledefinition_has_external():
    assert hasattr(stext::VariableDefinition, "external")
    descriptor = None
    for klass in stext::VariableDefinition.__mro__:
        if "external" in klass.__dict__:
            descriptor = klass.__dict__["external"]
            break
    assert isinstance(descriptor, property)

def test_stext::variabledefinition_has_readonly():
    assert hasattr(stext::VariableDefinition, "readonly")
    descriptor = None
    for klass in stext::VariableDefinition.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_stext::eventdefinition_is_not_abstract():
    assert not inspect.isabstract(stext::EventDefinition)


def test_stext::eventdefinition_constructor_exists():
    assert callable(stext::EventDefinition.__init__)


def test_stext::eventdefinition_constructor_args():
    sig = inspect.signature(stext::EventDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_stext::eventdefinition_has_direction():
    assert hasattr(stext::EventDefinition, "direction")
    descriptor = None
    for klass in stext::EventDefinition.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_stext::import_is_not_abstract():
    assert not inspect.isabstract(stext::Import)


def test_stext::import_constructor_exists():
    assert callable(stext::Import.__init__)


def test_stext::import_constructor_args():
    sig = inspect.signature(stext::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_stext::import_has_importedNamespace():
    assert hasattr(stext::Import, "importedNamespace")
    descriptor = None
    for klass in stext::Import.__mro__:
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



def test_stext::importscope_is_not_abstract():
    assert not inspect.isabstract(stext::ImportScope)


def test_stext::importscope_constructor_exists():
    assert callable(stext::ImportScope.__init__)


def test_stext::importscope_constructor_args():
    sig = inspect.signature(stext::ImportScope.__init__)
    params = list(sig.parameters.keys())



def test_stext::internalscope_is_not_abstract():
    assert not inspect.isabstract(stext::InternalScope)


def test_stext::internalscope_constructor_exists():
    assert callable(stext::InternalScope.__init__)


def test_stext::internalscope_constructor_args():
    sig = inspect.signature(stext::InternalScope.__init__)
    params = list(sig.parameters.keys())



def test_stext::interfacescope_is_not_abstract():
    assert not inspect.isabstract(stext::InterfaceScope)


def test_stext::interfacescope_constructor_exists():
    assert callable(stext::InterfaceScope.__init__)


def test_stext::interfacescope_constructor_args():
    sig = inspect.signature(stext::InterfaceScope.__init__)
    params = list(sig.parameters.keys())



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_stext::simplescope_is_not_abstract():
    assert not inspect.isabstract(stext::SimpleScope)


def test_stext::simplescope_constructor_exists():
    assert callable(stext::SimpleScope.__init__)


def test_stext::simplescope_constructor_args():
    sig = inspect.signature(stext::SimpleScope.__init__)
    params = list(sig.parameters.keys())



def test_stext::statechartscope_is_not_abstract():
    assert not inspect.isabstract(stext::StatechartScope)


def test_stext::statechartscope_constructor_exists():
    assert callable(stext::StatechartScope.__init__)


def test_stext::statechartscope_constructor_args():
    sig = inspect.signature(stext::StatechartScope.__init__)
    params = list(sig.parameters.keys())



def test_stext::guard_is_not_abstract():
    assert not inspect.isabstract(stext::Guard)


def test_stext::guard_constructor_exists():
    assert callable(stext::Guard.__init__)


def test_stext::guard_constructor_args():
    sig = inspect.signature(stext::Guard.__init__)
    params = list(sig.parameters.keys())



def test_reaction_is_not_abstract():
    assert not inspect.isabstract(Reaction)


def test_reaction_constructor_exists():
    assert callable(Reaction.__init__)


def test_reaction_constructor_args():
    sig = inspect.signature(Reaction.__init__)
    params = list(sig.parameters.keys())



def test_stext::transitionreaction_is_not_abstract():
    assert not inspect.isabstract(stext::TransitionReaction)


def test_stext::transitionreaction_constructor_exists():
    assert callable(stext::TransitionReaction.__init__)


def test_stext::transitionreaction_constructor_args():
    sig = inspect.signature(stext::TransitionReaction.__init__)
    params = list(sig.parameters.keys())



def test_stext::localreaction_is_not_abstract():
    assert not inspect.isabstract(stext::LocalReaction)


def test_stext::localreaction_constructor_exists():
    assert callable(stext::LocalReaction.__init__)


def test_stext::localreaction_constructor_args():
    sig = inspect.signature(stext::LocalReaction.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_stext::operationdefinition_is_not_abstract():
    assert not inspect.isabstract(stext::OperationDefinition)


def test_stext::operationdefinition_constructor_exists():
    assert callable(stext::OperationDefinition.__init__)


def test_stext::operationdefinition_constructor_args():
    sig = inspect.signature(stext::OperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_stext::transitionspecification_is_not_abstract():
    assert not inspect.isabstract(stext::TransitionSpecification)


def test_stext::transitionspecification_constructor_exists():
    assert callable(stext::TransitionSpecification.__init__)


def test_stext::transitionspecification_constructor_args():
    sig = inspect.signature(stext::TransitionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_stext::statespecification_is_not_abstract():
    assert not inspect.isabstract(stext::StateSpecification)


def test_stext::statespecification_constructor_exists():
    assert callable(stext::StateSpecification.__init__)


def test_stext::statespecification_constructor_args():
    sig = inspect.signature(stext::StateSpecification.__init__)
    params = list(sig.parameters.keys())



def test_defroot_is_not_abstract():
    assert not inspect.isabstract(DefRoot)


def test_defroot_constructor_exists():
    assert callable(DefRoot.__init__)


def test_defroot_constructor_args():
    sig = inspect.signature(DefRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext::transitionroot_is_not_abstract():
    assert not inspect.isabstract(stext::TransitionRoot)


def test_stext::transitionroot_constructor_exists():
    assert callable(stext::TransitionRoot.__init__)


def test_stext::transitionroot_constructor_args():
    sig = inspect.signature(stext::TransitionRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext::stateroot_is_not_abstract():
    assert not inspect.isabstract(stext::StateRoot)


def test_stext::stateroot_constructor_exists():
    assert callable(stext::StateRoot.__init__)


def test_stext::stateroot_constructor_args():
    sig = inspect.signature(stext::StateRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext::statechartroot_is_not_abstract():
    assert not inspect.isabstract(stext::StatechartRoot)


def test_stext::statechartroot_constructor_exists():
    assert callable(stext::StatechartRoot.__init__)


def test_stext::statechartroot_constructor_args():
    sig = inspect.signature(stext::StatechartRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext::defroot_is_not_abstract():
    assert not inspect.isabstract(stext::DefRoot)


def test_stext::defroot_constructor_exists():
    assert callable(stext::DefRoot.__init__)


def test_stext::defroot_constructor_args():
    sig = inspect.signature(stext::DefRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext::root_is_not_abstract():
    assert not inspect.isabstract(stext::Root)


def test_stext::root_constructor_exists():
    assert callable(stext::Root.__init__)


def test_stext::root_constructor_args():
    sig = inspect.signature(stext::Root.__init__)
    params = list(sig.parameters.keys())



def test_stext::scope_is_not_abstract():
    assert not inspect.isabstract(stext::Scope)


def test_stext::scope_constructor_exists():
    assert callable(stext::Scope.__init__)


def test_stext::scope_constructor_args():
    sig = inspect.signature(stext::Scope.__init__)
    params = list(sig.parameters.keys())



def test_scopedelement_is_not_abstract():
    assert not inspect.isabstract(ScopedElement)


def test_scopedelement_constructor_exists():
    assert callable(ScopedElement.__init__)


def test_scopedelement_constructor_args():
    sig = inspect.signature(ScopedElement.__init__)
    params = list(sig.parameters.keys())



def test_stext::statechartspecification_is_not_abstract():
    assert not inspect.isabstract(stext::StatechartSpecification)


def test_stext::statechartspecification_constructor_exists():
    assert callable(stext::StatechartSpecification.__init__)


def test_stext::statechartspecification_constructor_args():
    sig = inspect.signature(stext::StatechartSpecification.__init__)
    params = list(sig.parameters.keys())

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "second",
        "microsecond",
        "nanosecond",
        "millisecond",
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
        "after",
        "every",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeEventType"

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
Expression_strategy = st.builds(
    Expression,
)
stext::EventValueReferenceExpression_strategy = st.builds(
    stext::EventValueReferenceExpression,
)
stext::EventRaisingExpression_strategy = st.builds(
    stext::EventRaisingExpression,
)
Effect_strategy = st.builds(
    Effect,
)
stext::ReactionEffect_strategy = st.builds(
    stext::ReactionEffect,
)
stext::State_strategy = st.builds(
    stext::State,
)
stext::ActiveStateReferenceExpression_strategy = st.builds(
    stext::ActiveStateReferenceExpression,
)
BuiltinEventSpec_strategy = st.builds(
    BuiltinEventSpec,
)
stext::ExitEvent_strategy = st.builds(
    stext::ExitEvent,
)
stext::AlwaysEvent_strategy = st.builds(
    stext::AlwaysEvent,
)
stext::EntryEvent_strategy = st.builds(
    stext::EntryEvent,
)
EventSpec_strategy = st.builds(
    EventSpec,
)
stext::TimeEventSpec_strategy = st.builds(
    stext::TimeEventSpec,
    unit=
        safe_text,
    type=
        safe_text
)
stext::BuiltinEventSpec_strategy = st.builds(
    stext::BuiltinEventSpec,
)
stext::RegularEventSpec_strategy = st.builds(
    stext::RegularEventSpec,
)
stext::EventSpec_strategy = st.builds(
    stext::EventSpec,
)
ReactionProperty_strategy = st.builds(
    ReactionProperty,
)
stext::ExitPointSpec_strategy = st.builds(
    stext::ExitPointSpec,
    exitpoint=
        safe_text
)
stext::EntryPointSpec_strategy = st.builds(
    stext::EntryPointSpec,
    entrypoint=
        safe_text
)
Trigger_strategy = st.builds(
    Trigger,
)
stext::DefaultTrigger_strategy = st.builds(
    stext::DefaultTrigger,
)
stext::ReactionTrigger_strategy = st.builds(
    stext::ReactionTrigger,
)
Declaration_strategy = st.builds(
    Declaration,
)
stext::Expression_strategy = st.builds(
    stext::Expression,
)
Property_strategy = st.builds(
    Property,
)
Variable_strategy = st.builds(
    Variable,
)
stext::VariableDefinition_strategy = st.builds(
    stext::VariableDefinition,
    external=
        st.booleans(),
    readonly=
        st.booleans()
)
Event_strategy = st.builds(
    Event,
)
stext::EventDefinition_strategy = st.builds(
    stext::EventDefinition,
    direction=
        safe_text
)
stext::Import_strategy = st.builds(
    stext::Import,
    importedNamespace=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
StatechartScope_strategy = st.builds(
    StatechartScope,
)
stext::ImportScope_strategy = st.builds(
    stext::ImportScope,
)
stext::InternalScope_strategy = st.builds(
    stext::InternalScope,
)
stext::InterfaceScope_strategy = st.builds(
    stext::InterfaceScope,
)
Scope_strategy = st.builds(
    Scope,
)
stext::SimpleScope_strategy = st.builds(
    stext::SimpleScope,
)
stext::StatechartScope_strategy = st.builds(
    stext::StatechartScope,
)
stext::Guard_strategy = st.builds(
    stext::Guard,
)
Reaction_strategy = st.builds(
    Reaction,
)
stext::TransitionReaction_strategy = st.builds(
    stext::TransitionReaction,
)
stext::LocalReaction_strategy = st.builds(
    stext::LocalReaction,
)
Operation_strategy = st.builds(
    Operation,
)
stext::OperationDefinition_strategy = st.builds(
    stext::OperationDefinition,
)
stext::TransitionSpecification_strategy = st.builds(
    stext::TransitionSpecification,
)
stext::StateSpecification_strategy = st.builds(
    stext::StateSpecification,
)
DefRoot_strategy = st.builds(
    DefRoot,
)
stext::TransitionRoot_strategy = st.builds(
    stext::TransitionRoot,
)
stext::StateRoot_strategy = st.builds(
    stext::StateRoot,
)
stext::StatechartRoot_strategy = st.builds(
    stext::StatechartRoot,
)
stext::DefRoot_strategy = st.builds(
    stext::DefRoot,
)
stext::Root_strategy = st.builds(
    stext::Root,
)
stext::Scope_strategy = st.builds(
    stext::Scope,
)
ScopedElement_strategy = st.builds(
    ScopedElement,
)
stext::StatechartSpecification_strategy = st.builds(
    stext::StatechartSpecification,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=stext::EventValueReferenceExpression_strategy)
@settings(max_examples=50)
def test_stext::eventvaluereferenceexpression_instantiation(instance):
    assert isinstance(instance, stext::EventValueReferenceExpression)

@given(instance=stext::EventRaisingExpression_strategy)
@settings(max_examples=50)
def test_stext::eventraisingexpression_instantiation(instance):
    assert isinstance(instance, stext::EventRaisingExpression)

@given(instance=Effect_strategy)
@settings(max_examples=50)
def test_effect_instantiation(instance):
    assert isinstance(instance, Effect)

@given(instance=stext::ReactionEffect_strategy)
@settings(max_examples=50)
def test_stext::reactioneffect_instantiation(instance):
    assert isinstance(instance, stext::ReactionEffect)

@given(instance=stext::State_strategy)
@settings(max_examples=50)
def test_stext::state_instantiation(instance):
    assert isinstance(instance, stext::State)

@given(instance=stext::ActiveStateReferenceExpression_strategy)
@settings(max_examples=50)
def test_stext::activestatereferenceexpression_instantiation(instance):
    assert isinstance(instance, stext::ActiveStateReferenceExpression)

@given(instance=BuiltinEventSpec_strategy)
@settings(max_examples=50)
def test_builtineventspec_instantiation(instance):
    assert isinstance(instance, BuiltinEventSpec)

@given(instance=stext::ExitEvent_strategy)
@settings(max_examples=50)
def test_stext::exitevent_instantiation(instance):
    assert isinstance(instance, stext::ExitEvent)

@given(instance=stext::AlwaysEvent_strategy)
@settings(max_examples=50)
def test_stext::alwaysevent_instantiation(instance):
    assert isinstance(instance, stext::AlwaysEvent)

@given(instance=stext::EntryEvent_strategy)
@settings(max_examples=50)
def test_stext::entryevent_instantiation(instance):
    assert isinstance(instance, stext::EntryEvent)

@given(instance=EventSpec_strategy)
@settings(max_examples=50)
def test_eventspec_instantiation(instance):
    assert isinstance(instance, EventSpec)

@given(instance=stext::TimeEventSpec_strategy)
@settings(max_examples=50)
def test_stext::timeeventspec_instantiation(instance):
    assert isinstance(instance, stext::TimeEventSpec)

@given(instance=stext::TimeEventSpec_strategy)
def test_stext::timeeventspec_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=stext::TimeEventSpec_strategy)
def test_stext::timeeventspec_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=stext::TimeEventSpec_strategy)
def test_stext::timeeventspec_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=stext::TimeEventSpec_strategy)
def test_stext::timeeventspec_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=stext::BuiltinEventSpec_strategy)
@settings(max_examples=50)
def test_stext::builtineventspec_instantiation(instance):
    assert isinstance(instance, stext::BuiltinEventSpec)

@given(instance=stext::RegularEventSpec_strategy)
@settings(max_examples=50)
def test_stext::regulareventspec_instantiation(instance):
    assert isinstance(instance, stext::RegularEventSpec)

@given(instance=stext::EventSpec_strategy)
@settings(max_examples=50)
def test_stext::eventspec_instantiation(instance):
    assert isinstance(instance, stext::EventSpec)

@given(instance=ReactionProperty_strategy)
@settings(max_examples=50)
def test_reactionproperty_instantiation(instance):
    assert isinstance(instance, ReactionProperty)

@given(instance=stext::ExitPointSpec_strategy)
@settings(max_examples=50)
def test_stext::exitpointspec_instantiation(instance):
    assert isinstance(instance, stext::ExitPointSpec)

@given(instance=stext::ExitPointSpec_strategy)
def test_stext::exitpointspec_exitpoint_type(instance):
    assert isinstance(instance.exitpoint, str)


@given(instance=stext::ExitPointSpec_strategy)
def test_stext::exitpointspec_exitpoint_setter(instance):
    original = instance.exitpoint
    instance.exitpoint = original
    assert instance.exitpoint == original

@given(instance=stext::EntryPointSpec_strategy)
@settings(max_examples=50)
def test_stext::entrypointspec_instantiation(instance):
    assert isinstance(instance, stext::EntryPointSpec)

@given(instance=stext::EntryPointSpec_strategy)
def test_stext::entrypointspec_entrypoint_type(instance):
    assert isinstance(instance.entrypoint, str)


@given(instance=stext::EntryPointSpec_strategy)
def test_stext::entrypointspec_entrypoint_setter(instance):
    original = instance.entrypoint
    instance.entrypoint = original
    assert instance.entrypoint == original

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=stext::DefaultTrigger_strategy)
@settings(max_examples=50)
def test_stext::defaulttrigger_instantiation(instance):
    assert isinstance(instance, stext::DefaultTrigger)

@given(instance=stext::ReactionTrigger_strategy)
@settings(max_examples=50)
def test_stext::reactiontrigger_instantiation(instance):
    assert isinstance(instance, stext::ReactionTrigger)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=stext::Expression_strategy)
@settings(max_examples=50)
def test_stext::expression_instantiation(instance):
    assert isinstance(instance, stext::Expression)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=stext::VariableDefinition_strategy)
@settings(max_examples=50)
def test_stext::variabledefinition_instantiation(instance):
    assert isinstance(instance, stext::VariableDefinition)

@given(instance=stext::VariableDefinition_strategy)
def test_stext::variabledefinition_external_type(instance):
    assert isinstance(instance.external, bool)


@given(instance=stext::VariableDefinition_strategy)
def test_stext::variabledefinition_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original

@given(instance=stext::VariableDefinition_strategy)
def test_stext::variabledefinition_readonly_type(instance):
    assert isinstance(instance.readonly, bool)


@given(instance=stext::VariableDefinition_strategy)
def test_stext::variabledefinition_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=stext::EventDefinition_strategy)
@settings(max_examples=50)
def test_stext::eventdefinition_instantiation(instance):
    assert isinstance(instance, stext::EventDefinition)

@given(instance=stext::EventDefinition_strategy)
def test_stext::eventdefinition_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=stext::EventDefinition_strategy)
def test_stext::eventdefinition_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=stext::Import_strategy)
@settings(max_examples=50)
def test_stext::import_instantiation(instance):
    assert isinstance(instance, stext::Import)

@given(instance=stext::Import_strategy)
def test_stext::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=stext::Import_strategy)
def test_stext::import_importedNamespace_setter(instance):
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

@given(instance=stext::ImportScope_strategy)
@settings(max_examples=50)
def test_stext::importscope_instantiation(instance):
    assert isinstance(instance, stext::ImportScope)

@given(instance=stext::InternalScope_strategy)
@settings(max_examples=50)
def test_stext::internalscope_instantiation(instance):
    assert isinstance(instance, stext::InternalScope)

@given(instance=stext::InterfaceScope_strategy)
@settings(max_examples=50)
def test_stext::interfacescope_instantiation(instance):
    assert isinstance(instance, stext::InterfaceScope)

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=stext::SimpleScope_strategy)
@settings(max_examples=50)
def test_stext::simplescope_instantiation(instance):
    assert isinstance(instance, stext::SimpleScope)

@given(instance=stext::StatechartScope_strategy)
@settings(max_examples=50)
def test_stext::statechartscope_instantiation(instance):
    assert isinstance(instance, stext::StatechartScope)

@given(instance=stext::Guard_strategy)
@settings(max_examples=50)
def test_stext::guard_instantiation(instance):
    assert isinstance(instance, stext::Guard)

@given(instance=Reaction_strategy)
@settings(max_examples=50)
def test_reaction_instantiation(instance):
    assert isinstance(instance, Reaction)

@given(instance=stext::TransitionReaction_strategy)
@settings(max_examples=50)
def test_stext::transitionreaction_instantiation(instance):
    assert isinstance(instance, stext::TransitionReaction)

@given(instance=stext::LocalReaction_strategy)
@settings(max_examples=50)
def test_stext::localreaction_instantiation(instance):
    assert isinstance(instance, stext::LocalReaction)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=stext::OperationDefinition_strategy)
@settings(max_examples=50)
def test_stext::operationdefinition_instantiation(instance):
    assert isinstance(instance, stext::OperationDefinition)

@given(instance=stext::TransitionSpecification_strategy)
@settings(max_examples=50)
def test_stext::transitionspecification_instantiation(instance):
    assert isinstance(instance, stext::TransitionSpecification)

@given(instance=stext::StateSpecification_strategy)
@settings(max_examples=50)
def test_stext::statespecification_instantiation(instance):
    assert isinstance(instance, stext::StateSpecification)

@given(instance=DefRoot_strategy)
@settings(max_examples=50)
def test_defroot_instantiation(instance):
    assert isinstance(instance, DefRoot)

@given(instance=stext::TransitionRoot_strategy)
@settings(max_examples=50)
def test_stext::transitionroot_instantiation(instance):
    assert isinstance(instance, stext::TransitionRoot)

@given(instance=stext::StateRoot_strategy)
@settings(max_examples=50)
def test_stext::stateroot_instantiation(instance):
    assert isinstance(instance, stext::StateRoot)

@given(instance=stext::StatechartRoot_strategy)
@settings(max_examples=50)
def test_stext::statechartroot_instantiation(instance):
    assert isinstance(instance, stext::StatechartRoot)

@given(instance=stext::DefRoot_strategy)
@settings(max_examples=50)
def test_stext::defroot_instantiation(instance):
    assert isinstance(instance, stext::DefRoot)

@given(instance=stext::Root_strategy)
@settings(max_examples=50)
def test_stext::root_instantiation(instance):
    assert isinstance(instance, stext::Root)

@given(instance=stext::Scope_strategy)
@settings(max_examples=50)
def test_stext::scope_instantiation(instance):
    assert isinstance(instance, stext::Scope)

@given(instance=ScopedElement_strategy)
@settings(max_examples=50)
def test_scopedelement_instantiation(instance):
    assert isinstance(instance, ScopedElement)

@given(instance=stext::StatechartSpecification_strategy)
@settings(max_examples=50)
def test_stext::statechartspecification_instantiation(instance):
    assert isinstance(instance, stext::StatechartSpecification)
